#!/usr/bin/env python3
"""Validate Diderot concept source/epistemic audit and research-ingestion coverage.

This check is structural. It verifies that every concept page is represented in the
central audit registry, source references resolve, and any local qualified-research
evidence reference resolves to an independently qualified upstream record.

Passing this check establishes traceability/consistency only. It does not claim that
a cited source or accepted review makes an MMALS hypothesis scientifically true.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = ROOT / "concepts"
AUDIT = ROOT / "data" / "concept-audit.json"
INGESTION = ROOT / "data" / "research-evidence-ingestion.json"


def fail(messages: list[str]) -> None:
    for message in messages:
        print(f"ERROR: {message}")
    raise SystemExit(1)


def nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value)
    return value is not None


def validate_ingestion(errors: list[str], audited: dict[str, Any], groups: dict[str, Any]) -> int:
    if not INGESTION.exists():
        errors.append("missing research ingestion registry: data/research-evidence-ingestion.json")
        return 0

    data = json.loads(INGESTION.read_text(encoding="utf-8"))
    diderot_repo = data.get("diderot_repository")
    allowed_dispositions = set(data.get("allowed_dispositions", []))
    allowed_outcomes = set(data.get("allowed_outcomes", []))
    records = data.get("records", {})

    if not diderot_repo:
        errors.append("research ingestion registry missing diderot_repository")
    if not allowed_dispositions:
        errors.append("research ingestion registry has no allowed_dispositions")
    if not allowed_outcomes:
        errors.append("research ingestion registry has no allowed_outcomes")
    if not isinstance(records, dict):
        errors.append("research ingestion registry records must be an object")
        return 0

    required_source = ("repository", "immutable_ref", "artifact_url")
    required_review = ("repository", "url", "reviewed_ref", "disposition")
    moving_refs = {"main", "master", "head", "HEAD"}

    for record_id, record in records.items():
        if not isinstance(record, dict):
            errors.append(f"qualified evidence {record_id}: record must be an object")
            continue

        source = record.get("source", {})
        review = record.get("review", {})
        if not isinstance(source, dict):
            errors.append(f"qualified evidence {record_id}: source must be an object")
            source = {}
        if not isinstance(review, dict):
            errors.append(f"qualified evidence {record_id}: review must be an object")
            review = {}

        for field in required_source:
            if not nonempty(source.get(field)):
                errors.append(f"qualified evidence {record_id}: source missing {field}")
        for field in required_review:
            if not nonempty(review.get(field)):
                errors.append(f"qualified evidence {record_id}: review missing {field}")
        for field in ("claim", "scope", "caveats", "outcome"):
            if not nonempty(record.get(field)):
                errors.append(f"qualified evidence {record_id}: missing {field}")

        source_repo = source.get("repository")
        review_repo = review.get("repository")
        if diderot_repo and source_repo == diderot_repo:
            errors.append(f"qualified evidence {record_id}: Diderot cannot be its own upstream scientific source")
        if diderot_repo and review_repo == diderot_repo:
            errors.append(f"qualified evidence {record_id}: Diderot review cannot qualify Diderot scientific evidence")

        immutable_ref = source.get("immutable_ref")
        if immutable_ref in moving_refs:
            errors.append(f"qualified evidence {record_id}: source immutable_ref is a moving ref: {immutable_ref}")
        if review.get("reviewed_ref") and immutable_ref and review.get("reviewed_ref") != immutable_ref:
            errors.append(
                f"qualified evidence {record_id}: review.reviewed_ref must equal source.immutable_ref in schema v0.1"
            )

        disposition = review.get("disposition")
        if disposition and disposition not in allowed_dispositions:
            errors.append(
                f"qualified evidence {record_id}: disposition {disposition!r} is not qualifying; allowed={sorted(allowed_dispositions)}"
            )
        outcome = record.get("outcome")
        if outcome and outcome not in allowed_outcomes:
            errors.append(
                f"qualified evidence {record_id}: outcome {outcome!r} not in {sorted(allowed_outcomes)}"
            )

        for label, url in (("source.artifact_url", source.get("artifact_url")), ("review.url", review.get("url"))):
            if url and not str(url).startswith(("https://", "http://")):
                errors.append(f"qualified evidence {record_id}: {label} must be a direct URL")

    referenced: set[str] = set()
    qualified_markers = {"qualified research evidence", "qualified_research_evidence", "qualified-research-evidence"}

    for concept_id, entry in audited.items():
        refs = entry.get("qualified_evidence_refs")
        if refs is not None:
            if not isinstance(refs, list) or not refs:
                errors.append(f"{concept_id}: qualified_evidence_refs must be a non-empty list when declared")
                refs = []
            for record_id in refs:
                if record_id not in records:
                    errors.append(f"{concept_id}: unknown qualified evidence record {record_id}")
                else:
                    referenced.add(record_id)

        entry_status = str(entry.get("epistemic_status", "")).strip().lower()
        group_status = ""
        group_id = entry.get("group")
        if group_id in groups:
            group_status = str(groups[group_id].get("epistemic_status", "")).strip().lower()
        if entry_status in qualified_markers or group_status in qualified_markers:
            if not refs:
                errors.append(
                    f"{concept_id}: qualified research evidence status requires qualified_evidence_refs"
                )

    return len(referenced)


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

    qualified_refs = validate_ingestion(errors, audited, groups)

    if errors:
        fail(errors)

    review_focus = sum(1 for entry in audited.values() if entry.get("review_focus"))
    print(f"Concept pages checked: {len(pages)}")
    print(f"Audit entries checked: {len(audited)}")
    print(f"Reference anchors checked: {len(sources)}")
    print(f"Independent-review focus entries: {review_focus}")
    print(f"Qualified local research evidence refs checked: {qualified_refs}")
    print("Concept source/epistemic and research-ingestion audit is structurally complete.")


if __name__ == "__main__":
    main()
