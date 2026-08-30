#!/usr/bin/env python3
"""Validate Diderot concept source/epistemic audit coverage.

This check is structural. It verifies that every concept page is represented in the
central audit registry and that its group/source references resolve. It does not
claim that a cited source validates an MMALS hypothesis.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = ROOT / "concepts"
AUDIT = ROOT / "data" / "concept-audit.json"


def fail(messages: list[str]) -> None:
    for message in messages:
        print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    data = json.loads(AUDIT.read_text(encoding="utf-8"))
    groups = data.get("groups", {})
    sources = data.get("sources", {})
    audited = data.get("concepts", {})

    pages = {p.parent.name for p in CONCEPTS.glob("*/index.html")}
    audited_ids = set(audited)
    errors: list[str] = []

    for concept_id in sorted(pages - audited_ids):
        errors.append(f"concept page has no audit entry: {concept_id}")
    for concept_id in sorted(audited_ids - pages):
        errors.append(f"audit entry has no concept page: {concept_id}")

    required_group_fields = {
        "label",
        "epistemic_status",
        "definition_fidelity",
        "mmals_evidence_status",
        "toy_status",
        "graph_edge_review",
    }
    for group_id, group in groups.items():
        missing = required_group_fields - set(group)
        if missing:
            errors.append(f"group {group_id} missing fields: {sorted(missing)}")

    for concept_id, entry in audited.items():
        group_id = entry.get("group")
        if group_id not in groups:
            errors.append(f"{concept_id}: unknown audit group {group_id!r}")
        keys = entry.get("sources")
        if not isinstance(keys, list) or not keys:
            errors.append(f"{concept_id}: at least one reference anchor is required")
            continue
        for key in keys:
            if key not in sources:
                errors.append(f"{concept_id}: unknown source key {key}")

    for key, source in sources.items():
        for field in ("title", "authors", "year", "type", "url"):
            if not source.get(field):
                errors.append(f"source {key} missing {field}")

    if errors:
        fail(errors)

    review_focus = sum(1 for entry in audited.values() if entry.get("review_focus"))
    print(f"Concept pages checked: {len(pages)}")
    print(f"Audit entries checked: {len(audited)}")
    print(f"Reference anchors checked: {len(sources)}")
    print(f"Independent-review focus entries: {review_focus}")
    print("Concept source/epistemic audit coverage is structurally complete.")


if __name__ == "__main__":
    main()
