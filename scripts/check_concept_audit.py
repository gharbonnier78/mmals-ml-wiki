#!/usr/bin/env python3
"""Validate Diderot concept source/epistemic audit and research-ingestion coverage.

This check is structural. It verifies that every concept page is represented in the
central audit registry, source references resolve, learner-facing epistemic status
comes from the canonical vocabulary, and any local qualified-research evidence
reference resolves to an independently qualified upstream record.

Passing this check establishes traceability/consistency only. It does not claim that
a cited source or accepted review makes an MMALS hypothesis scientifically true.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = ROOT / "concepts"
AUDIT = ROOT / "data" / "concept-audit.json"
INGESTION = ROOT / "data" / "research-evidence-ingestion.json"
STATUS_REGISTRY = ROOT / "data" / "epistemic-statuses.json"


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


def normalized_repo(value: Any) -> str:
    return str(value).strip().casefold() if value is not None else ""


def validate_ingestion_data(
    errors: list[str],
    audited: dict[str, Any],
    groups: dict[str, Any],
    data: dict[str, Any],
) -> int:
    diderot_repo = data.get("diderot_repository")
    diderot_repo_normalized = normalized_repo(diderot_repo)
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
    moving_refs = {"main", "master", "head"}

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

        source_repo = normalized_repo(source.get("repository"))
        review_repo = normalized_repo(review.get("repository"))
        if diderot_repo_normalized and source_repo == diderot_repo_normalized:
            errors.append(f"qualified evidence {record_id}: Diderot cannot be its own upstream scientific source")
        if diderot_repo_normalized and review_repo == diderot_repo_normalized:
            errors.append(f"qualified evidence {record_id}: Diderot review cannot qualify Diderot scientific evidence")

        immutable_ref = source.get("immutable_ref")
        immutable_ref_normalized = str(immutable_ref).strip().casefold() if immutable_ref is not None else ""
        if immutable_ref_normalized in moving_refs:
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


def validate_ingestion(errors: list[str], audited: dict[str, Any], groups: dict[str, Any]) -> int:
    if not INGESTION.exists():
        errors.append("missing research ingestion registry: data/research-evidence-ingestion.json")
        return 0
    data = json.loads(INGESTION.read_text(encoding="utf-8"))
    return validate_ingestion_data(errors, audited, groups, data)


def selftest_registry() -> dict[str, Any]:
    return {
        "diderot_repository": "gharbonnier78/mmals-ml-wiki",
        "allowed_dispositions": ["ACCEPT"],
        "allowed_outcomes": ["positive", "negative", "null", "mixed", "method"],
        "records": {
            "probe": {
                "source": {
                    "repository": "example/research",
                    "immutable_ref": "abc123",
                    "artifact_url": "https://example.invalid/research/abc123",
                },
                "review": {
                    "repository": "example/independent-review",
                    "url": "https://example.invalid/review/abc123",
                    "reviewed_ref": "abc123",
                    "disposition": "ACCEPT",
                },
                "outcome": "null",
                "claim": "bounded self-test claim",
                "scope": "checker self-test only",
                "caveats": ["not research evidence"],
            }
        },
    }


def run_ingestion_negative_selftests(errors: list[str]) -> None:
    valid_errors: list[str] = []
    validate_ingestion_data(valid_errors, {}, {}, selftest_registry())
    if valid_errors:
        errors.append(f"ingestion self-test baseline unexpectedly failed: {valid_errors}")
        return

    cases: list[tuple[str, dict[str, Any], str]] = []

    case = deepcopy(selftest_registry())
    case["records"]["probe"]["source"]["repository"] = "Gharbonnier78/MMALS-ML-WIKI"
    cases.append(("case-insensitive Diderot source", case, "cannot be its own upstream scientific source"))

    case = deepcopy(selftest_registry())
    case["records"]["probe"]["review"]["repository"] = "GHARBONNIER78/MMALS-ML-WIKI"
    cases.append(("case-insensitive Diderot review", case, "Diderot review cannot qualify"))

    case = deepcopy(selftest_registry())
    case["records"]["probe"]["source"]["immutable_ref"] = "MAIN"
    case["records"]["probe"]["review"]["reviewed_ref"] = "MAIN"
    cases.append(("moving source ref", case, "source immutable_ref is a moving ref"))

    case = deepcopy(selftest_registry())
    case["records"]["probe"]["review"]["disposition"] = "PARTIAL ACCEPT / REQUEST CHANGES"
    cases.append(("non-qualifying disposition", case, "is not qualifying"))

    for label, registry, expected in cases:
        case_errors: list[str] = []
        validate_ingestion_data(case_errors, {}, {}, registry)
        if not any(expected in message for message in case_errors):
            errors.append(f"ingestion negative self-test did not reject {label}: expected {expected!r}, got {case_errors}")


def validate_status_registry(
    errors: list[str], audited: dict[str, Any], groups: dict[str, Any]
) -> tuple[int, int]:
    if not STATUS_REGISTRY.exists():
        errors.append("missing epistemic status registry: data/epistemic-statuses.json")
        return 0, 0

    data = json.loads(STATUS_REGISTRY.read_text(encoding="utf-8"))
    statuses = data.get("statuses", {})
    group_defaults = data.get("group_defaults", {})
    overrides = data.get("concept_overrides", {})
    surfaces = data.get("surfaces", {})
    axes = data.get("axis_separation", {})

    required_statuses = {
        "source-derived",
        "diderot-synthesis",
        "project-hypothesis",
        "teaching-toy",
        "qualified-research-evidence",
    }
    if not isinstance(statuses, dict):
        errors.append("epistemic status registry statuses must be an object")
        statuses = {}
    missing_statuses = required_statuses - set(statuses)
    if missing_statuses:
        errors.append(f"epistemic status registry missing canonical statuses: {sorted(missing_statuses)}")

    for key, definition in statuses.items():
        if not isinstance(definition, dict):
            errors.append(f"epistemic status {key}: definition must be an object")
            continue
        for field in ("label", "description", "css_class"):
            if not nonempty(definition.get(field)):
                errors.append(f"epistemic status {key}: missing {field}")

    if not isinstance(axes, dict) or not nonempty(axes.get("epistemic_authority")) or not nonempty(axes.get("pedagogical_maturity")):
        errors.append("epistemic status registry must keep epistemic_authority and pedagogical_maturity as explicit separate axes")

    if not isinstance(group_defaults, dict):
        errors.append("epistemic status registry group_defaults must be an object")
        group_defaults = {}
    for group_id in groups:
        if group_id not in group_defaults:
            errors.append(f"epistemic status registry missing group default for {group_id}")
    for group_id, key in group_defaults.items():
        if group_id not in groups:
            errors.append(f"epistemic status registry has unknown group default {group_id}")
        if key not in statuses:
            errors.append(f"epistemic status registry group {group_id}: unknown canonical status {key!r}")

    if not isinstance(overrides, dict):
        errors.append("epistemic status registry concept_overrides must be an object")
        overrides = {}
    for concept_id, key in overrides.items():
        if concept_id not in audited:
            errors.append(f"epistemic status registry override refers to unknown concept {concept_id}")
        if key not in statuses:
            errors.append(f"epistemic status registry override {concept_id}: unknown canonical status {key!r}")

    ingestion_records: dict[str, Any] = {}
    if INGESTION.exists():
        ingestion_data = json.loads(INGESTION.read_text(encoding="utf-8"))
        if isinstance(ingestion_data.get("records"), dict):
            ingestion_records = ingestion_data["records"]

    for concept_id, entry in audited.items():
        group_id = entry.get("group")
        key = overrides.get(concept_id, group_defaults.get(group_id))
        if key not in statuses:
            errors.append(f"{concept_id}: no valid canonical learner-facing epistemic status resolves")
            continue
        if key == "qualified-research-evidence":
            refs = entry.get("qualified_evidence_refs")
            if not isinstance(refs, list) or not refs:
                errors.append(f"{concept_id}: qualified learner-facing status requires qualified_evidence_refs from issue #15 ingestion")
            else:
                for record_id in refs:
                    if record_id not in ingestion_records:
                        errors.append(f"{concept_id}: qualified learner-facing status references unknown ingestion record {record_id}")

    if not isinstance(surfaces, dict):
        errors.append("epistemic status registry surfaces must be an object")
        surfaces = {}
    expected_surfaces = {
        page.relative_to(ROOT).as_posix()
        for root_name in ("labs", "pathways")
        for page in (ROOT / root_name).glob("*/index.html")
    }
    declared_surfaces = set(surfaces)
    for path in sorted(expected_surfaces - declared_surfaces):
        errors.append(f"learner-facing detail surface has no canonical epistemic status: {path}")
    for path in sorted(declared_surfaces - expected_surfaces):
        errors.append(f"epistemic status registry references unknown lab/pathway detail surface: {path}")
    for path, key in surfaces.items():
        if key not in statuses:
            errors.append(f"epistemic status surface {path}: unknown canonical status {key!r}")

    return len(statuses), len(expected_surfaces)


def main() -> None:
    data = json.loads(AUDIT.read_text(encoding="utf-8"))
    groups = data.get("groups", {})
    sources = data.get("sources", {})
    audited = data.get("concepts", {})

    pages = {p.parent.name for p in CONCEPTS.glob("*/index.html")}
    audited_ids = set(audited)
    errors: list[str] = []

    run_ingestion_negative_selftests(errors)

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
    status_count, surface_count = validate_status_registry(errors, audited, groups)

    if errors:
        fail(errors)

    review_focus = sum(1 for entry in audited.values() if entry.get("review_focus"))
    print("Research-ingestion negative self-tests: PASS (4 rejection paths + valid baseline)")
    print(f"Concept pages checked: {len(pages)}")
    print(f"Audit entries checked: {len(audited)}")
    print(f"Reference anchors checked: {len(sources)}")
    print(f"Independent-review focus entries: {review_focus}")
    print(f"Qualified local research evidence refs checked: {qualified_refs}")
    print(f"Canonical learner-facing epistemic statuses checked: {status_count}")
    print(f"Lab/pathway status surfaces checked: {surface_count}")
    print("Concept source/epistemic, learner-status and research-ingestion audit is structurally complete.")


if __name__ == "__main__":
    main()
