#!/usr/bin/env python3
"""Validate the Diderot Repository & Outcome Atlas contract."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "repository-outcomes.json"

ALLOWED_STATUS = {
    "supported", "mixed", "negative", "hypothesis", "specification",
    "tool", "governance", "pedagogy", "legacy",
}
ALLOWED_CATEGORY = {
    "mmals-core", "mmals-evidence", "mmals-geometry", "mmals-control",
    "testing-decision", "adjacent-ml", "systems-identity",
    "methods-governance", "pedagogy", "legacy",
}
EVIDENCE_BEARING = {"supported", "mixed", "negative"}
ALLOWED_EVIDENCE_FOR_BEARING = {"executed-evidence", "mechanism-demo"}
REQUIRED_HIGH_RISK = {
    "mmals": "mixed",
    "mmals-cal": "mixed",
    "geometry-g1": "mixed",
    "ed-pomdp": "negative",
    "siamese": "negative",
}
FORBIDDEN_PUBLICATION = {"mmals-g2-geometric-perspective"}


def fail(message: str) -> None:
    raise SystemExit(f"Repository atlas check FAILED: {message}")


def valid_http_url(value: str) -> bool:
    try:
        parsed = urlparse(value)
    except Exception:
        return False
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> None:
    if not REGISTRY.exists():
        fail("data/repository-outcomes.json is missing")
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("schema_version") != "0.2":
        fail("schema_version must be 0.2")
    repos = data.get("repositories")
    if not isinstance(repos, list) or not repos:
        fail("repositories must be a non-empty list")

    ids, names = set(), set()
    for i, repo in enumerate(repos):
        prefix = f"repositories[{i}]"
        for field in ("id", "name", "repository", "category", "role", "summary", "outcome", "quick_links", "last_reviewed"):
            if field not in repo:
                fail(f"{prefix}: missing {field}")
        if repo["id"] in ids:
            fail(f"{prefix}: duplicate id {repo['id']}")
        if repo["repository"] in names:
            fail(f"{prefix}: duplicate repository {repo['repository']}")
        ids.add(repo["id"])
        names.add(repo["repository"])

        if repo["repository"] in FORBIDDEN_PUBLICATION:
            fail(f"{prefix}: publication-blocked repository must not appear in public atlas")
        if repo["category"] not in ALLOWED_CATEGORY:
            fail(f"{prefix}: unsupported category {repo['category']}")

        outcome = repo["outcome"]
        for field in ("status", "statement", "evidence_class", "source_url", "source_label"):
            if not outcome.get(field):
                fail(f"{prefix}.outcome: missing/empty {field}")
        if outcome["status"] not in ALLOWED_STATUS:
            fail(f"{prefix}: unsupported outcome status {outcome['status']}")
        if not valid_http_url(outcome["source_url"]):
            fail(f"{prefix}: invalid outcome source URL")
        if outcome["status"] in EVIDENCE_BEARING and outcome["evidence_class"] not in ALLOWED_EVIDENCE_FOR_BEARING:
            fail(f"{prefix}: evidence-bearing status requires executed evidence/mechanism demo")

        links = repo["quick_links"]
        if not isinstance(links, list) or not links:
            fail(f"{prefix}: at least one quick link is required")
        if not any(link.get("kind") == "repo" for link in links):
            fail(f"{prefix}: a direct GitHub repo quick link is required")
        for j, link in enumerate(links):
            if not link.get("label") or not valid_http_url(link.get("url", "")):
                fail(f"{prefix}.quick_links[{j}]: invalid label/url")

    for repo_id, expected_status in REQUIRED_HIGH_RISK.items():
        row = next((r for r in repos if r["id"] == repo_id), None)
        if row is None:
            fail(f"required high-risk repository {repo_id} missing")
        if row["outcome"]["status"] != expected_status:
            fail(f"{repo_id}: expected status {expected_status}, got {row['outcome']['status']}")

    print(
        "Repository atlas OK: "
        f"{len(repos)} repositories; "
        f"{len({r['category'] for r in repos})} categories; "
        f"{len({r['outcome']['status'] for r in repos})} outcome statuses."
    )


if __name__ == "__main__":
    main()
