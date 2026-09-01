#!/usr/bin/env python3
"""Browser-level smoke test for the belief/adaptive-planning teaching path.

This test intentionally drives the same public controls available to a human user. It is
engineering/test evidence that the pedagogical interaction behaves as declared; it is not
scientific evidence for POMDP theory, MMALS, GO-ED-POMDP, or Toy F2.
"""
from __future__ import annotations

import contextlib
import socket
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import Locator, sync_playwright

ROOT = Path(__file__).resolve().parents[2]
PORT = 8765
URL = f"http://127.0.0.1:{PORT}/labs/belief-adaptive-planning/index.html"
ARTIFACTS = ROOT / "test-artifacts"


def wait_for_server(timeout: float = 10.0) -> None:
    deadline = time.time() + timeout
    while time.time() < deadline:
        with contextlib.closing(socket.socket()) as sock:
            sock.settimeout(0.2)
            if sock.connect_ex(("127.0.0.1", PORT)) == 0:
                return
        time.sleep(0.1)
    raise RuntimeError("local HTTP server did not become ready")


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def value(page, selector: str) -> str:
    return page.locator(selector).inner_text().strip()


def set_range_like_user(locator: Locator, target: float) -> None:
    """Move an HTML range input with keyboard controls a user can actually operate."""
    lo = float(locator.get_attribute("min") or 0.0)
    hi = float(locator.get_attribute("max") or 100.0)
    step = float(locator.get_attribute("step") or 1.0)
    expect(lo <= target <= hi, f"target {target} outside [{lo}, {hi}]")

    locator.focus()
    if abs(target - lo) < step / 2:
        locator.press("Home")
    elif abs(target - hi) < step / 2:
        locator.press("End")
    else:
        locator.press("Home")
        increments = round((target - lo) / step)
        for _ in range(increments):
            locator.press("ArrowRight")

    actual = float(locator.input_value())
    expect(abs(actual - target) <= step / 2 + 1e-9, f"range control reached {actual}, expected {target}")


def main() -> int:
    ARTIFACTS.mkdir(exist_ok=True)
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        wait_for_server()
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1440, "height": 1200})
            try:
                page.goto(URL, wait_until="networkidle")
                expect("Belief, certainty and adaptive planning" in page.locator("h1").inner_text(), "lab title missing")

                # Toy 1: operate the same select/slider controls available to a human.
                posterior_warning = float(value(page, "#posterior-value"))
                expect(0.62 < posterior_warning < 0.65, f"unexpected warning posterior: {posterior_warning}")
                page.locator("#sensor-observation").select_option("clear")
                posterior_clear = float(value(page, "#posterior-value"))
                expect(posterior_clear < posterior_warning, "clear observation should reduce fault posterior in default toy")
                set_range_like_user(page.locator("#belief-prior"), 0.70)
                posterior_high_prior = float(value(page, "#posterior-value"))
                expect(posterior_high_prior > posterior_clear, "raising the prior should raise the posterior for the same clear observation")

                # Toy 2: more certainty can remain on the same side of the decision boundary.
                expect(page.locator("#decision-change").get_attribute("data-changed") == "false", "default decision should remain unchanged")
                expect(value(page, "#decision-before-action") == "REUSE", "unexpected default before action")
                expect(value(page, "#decision-after-action") == "REUSE", "unexpected default after action")
                expect(value(page, "#certainty-change") == "certainty increased", "default example should increase certainty")
                set_range_like_user(page.locator("#decision-after"), 0.85)
                expect(page.locator("#decision-change").get_attribute("data-changed") == "true", "crossing threshold should change action")
                expect(value(page, "#decision-after-action") == "ADAPT", "threshold-crossing action should be ADAPT")

                # Toy 3: identical one-step values, different finite-horizon contingent plans.
                expect(value(page, "#q1-reuse-a") == value(page, "#q1-reuse-b"), "Q1(REUSE) must match across situations")
                expect(value(page, "#q1-probe-a") == value(page, "#q1-probe-b"), "Q1(PROBE) must match across situations")
                expect(value(page, "#h2-a-best") == "REUSE", "default Situation A should prefer REUSE")
                expect(value(page, "#h2-b-best") == "PROBE", "default Situation B should prefer PROBE")
                expect(page.locator("#contingent-verdict").get_attribute("data-diverges") == "true", "default contingent plans should diverge")
                set_range_like_user(page.locator("#contingent-cost"), 8.0)
                expect(page.locator("#contingent-verdict").get_attribute("data-diverges") == "false", "high probe cost should remove the divergence")

                # Preserve a reviewable rendering of the manipulated lab before navigation.
                page.screenshot(path=str(ARTIFACTS / "belief-adaptive-planning-lab.png"), full_page=True)

                # Human-visible pathway navigation should remain executable.
                page.get_by_role("link", name="Open the belief → adaptive decisions pathway").click()
                page.wait_for_load_state("networkidle")
                expect("From belief to adaptive decision sufficiency" in page.locator("h1").inner_text(), "pathway navigation failed")

                # The semantic graph must also load the new registry shard and expose a canonical page.
                page.goto(f"http://127.0.0.1:{PORT}/explore/index.html", wait_until="networkidle")
                policy_node = page.get_by_role("link", name="Policy", exact=True)
                expect(policy_node.count() == 1, "Policy node missing from concept graph")
                policy_node.click()
                page.wait_for_load_state("networkidle")
                expect(page.locator("h1").inner_text().strip() == "Policy", "concept-graph navigation did not open canonical Policy page")

                page.screenshot(path=str(ARTIFACTS / "belief-adaptive-planning-smoke.png"), full_page=True)
            except Exception:
                page.screenshot(path=str(ARTIFACTS / "belief-adaptive-planning-failure.png"), full_page=True)
                raise
            finally:
                browser.close()
    finally:
        server.terminate()
        with contextlib.suppress(subprocess.TimeoutExpired):
            server.wait(timeout=5)
        if server.poll() is None:
            server.kill()

    print("Browser interaction contract OK: belief update, certainty/decision boundary, contingent-plan divergence, pathway navigation, and concept-graph discovery exercised.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
