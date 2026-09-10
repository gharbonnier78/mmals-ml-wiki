#!/usr/bin/env python3
"""Validate Diderot's browser rendering contract after prepare_pages.py."""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from generate_navigation import NavigationError, generate_navigation

ROOT = Path(__file__).resolve().parents[1]
SITE_JS = ROOT / "assets" / "js" / "site.js"
EPISTEMIC_JS = ROOT / "assets" / "js" / "epistemic-status.js"

errors: list[str] = []


def expected_runtime(page: Path, script: Path) -> str:
    rel = os.path.relpath(script, page.parent).replace(os.sep, "/")
    return f'<script src="{rel}"></script>'


concept_pages = sorted((ROOT / "concepts").glob("*/index.html"))
if not concept_pages:
    errors.append("no concept pages found")

detail_surfaces = sorted(
    page
    for root_name in ("concepts", "labs", "pathways")
    for page in (ROOT / root_name).glob("*/index.html")
)

formula_pages: list[Path] = []
formula_count = 0
formula_re = re.compile(r'''<[^>]+class=["'][^"']*\bformula\b[^"']*["'][^>]*>(.*?)</[^>]+>''', re.S)

for page in sorted(ROOT.rglob("*.html")):
    text = page.read_text(encoding="utf-8")
    matches = formula_re.findall(text)
    if matches:
        formula_pages.append(page)
        formula_count += len(matches)
        if any(not re.sub(r"<[^>]+>", "", item).strip() for item in matches):
            errors.append(f"{page.relative_to(ROOT)}: empty formula block")
        if expected_runtime(page, SITE_JS) not in text:
            errors.append(f"{page.relative_to(ROOT)}: formula page does not load shared site runtime")

for page in concept_pages:
    text = page.read_text(encoding="utf-8")
    if expected_runtime(page, SITE_JS) not in text:
        errors.append(f"{page.relative_to(ROOT)}: concept page does not load shared site runtime")

for page in detail_surfaces:
    text = page.read_text(encoding="utf-8")
    if expected_runtime(page, EPISTEMIC_JS) not in text:
        errors.append(f"{page.relative_to(ROOT)}: learner-facing detail page does not load epistemic-status runtime")

site_js = SITE_JS.read_text(encoding="utf-8") if SITE_JS.exists() else ""
for required in (
    "mathjax@3.2.2",
    "MathJax",
    "typesetPromise",
    "document.querySelectorAll('.formula')",
    "data-concept-audit",
):
    if required not in site_js:
        errors.append(f"assets/js/site.js: missing rendering contract token {required!r}")

epistemic_js = EPISTEMIC_JS.read_text(encoding="utf-8") if EPISTEMIC_JS.exists() else ""
for required in (
    "data/epistemic-statuses.json",
    "data-epistemic-badge",
    "data-epistemic-status",
    "qualified-research-evidence",
    "qualified_evidence_refs",
):
    if required not in epistemic_js:
        errors.append(f"assets/js/epistemic-status.js: missing rendering contract token {required!r}")

navigation_counts = (0, 0)
try:
    concept_navigation, pathway_navigation, _ = generate_navigation(write=False)
    navigation_counts = (concept_navigation, pathway_navigation)
except (NavigationError, ValueError) as exc:
    errors.append(f"generated navigation contract failed: {exc}")

if errors:
    print("Diderot rendering contract FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(
    "Diderot rendering contract OK: "
    f"{len(concept_pages)} concept pages; "
    f"{navigation_counts[0]} generated concept cards; "
    f"{navigation_counts[1]} generated pathway cards; "
    f"{len(detail_surfaces)} epistemic-status detail surfaces; "
    f"{len(formula_pages)} formula pages; "
    f"{formula_count} formula blocks; MathJax 3.2.2 pinned."
)
