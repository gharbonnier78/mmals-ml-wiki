#!/usr/bin/env python3
"""Validate Diderot's browser rendering and concept-source consistency contract."""
from __future__ import annotations

import html
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_JS = ROOT / "assets" / "js" / "site.js"
EPISTEMIC_JS = ROOT / "assets" / "js" / "epistemic-status.js"
CONCEPTS_JSON = ROOT / "data" / "concepts.json"

FORECASTING_IDS = {
    "collective-forecasting",
    "prediction-market",
    "proper-scoring-rule",
    "brier-score",
    "forecast-calibration",
    "forecast-contract",
    "meta-prediction",
    "brier-diversity-identity",
}
BARE_TEX_COMMANDS = re.compile(
    r"(?<!\\)\b(?:mathbb|mathcal|mathrm|ldots|mid|approx|le|ge|Omega|theta|frac|sum|bar|qquad)\b"
)

errors: list[str] = []


def expected_runtime(page: Path, script: Path) -> str:
    rel = os.path.relpath(script, page.parent).replace(os.sep, "/")
    return f'<script src="{rel}"></script>'


def plain_text(fragment: str) -> str:
    stripped = re.sub(r"<[^>]+>", "", fragment)
    return html.unescape(stripped)


def normalize_text(value: str) -> str:
    return " ".join(value.split())


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

concept_data = {
    item["id"]: item
    for item in json.loads(CONCEPTS_JSON.read_text(encoding="utf-8"))
    if item.get("id") in FORECASTING_IDS
}

for page in sorted(ROOT.rglob("*.html")):
    text = page.read_text(encoding="utf-8")
    matches = formula_re.findall(text)
    if matches:
        formula_pages.append(page)
        formula_count += len(matches)
        if any(not plain_text(item).strip() for item in matches):
            errors.append(f"{page.relative_to(ROOT)}: empty formula block")
        if expected_runtime(page, SITE_JS) not in text:
            errors.append(f"{page.relative_to(ROOT)}: formula page does not load shared site runtime")

    rel = page.relative_to(ROOT)
    if len(rel.parts) == 3 and rel.parts[0] == "concepts" and rel.name == "index.html":
        concept_id = rel.parts[1]
        if concept_id in FORECASTING_IDS:
            clean_formulas = [plain_text(item).strip() for item in matches]
            if any(any(ord(ch) < 32 and ch not in "\n\r" for ch in formula) for formula in clean_formulas):
                errors.append(f"{rel}: control character found inside formula block")
            for formula in clean_formulas:
                bare = BARE_TEX_COMMANDS.search(formula)
                if bare:
                    errors.append(
                        f"{rel}: possible dropped TeX backslash before {bare.group(0)!r} in formula {formula!r}"
                    )

            concept = concept_data.get(concept_id)
            if concept is None:
                errors.append(f"{rel}: forecasting concept missing from data/concepts.json")
            else:
                canonical_formula = concept.get("formula", "")
                if canonical_formula not in clean_formulas:
                    errors.append(
                        f"{rel}: canonical formula from concepts.json is absent; "
                        f"expected {canonical_formula!r}, found {clean_formulas!r}"
                    )
                page_plain = normalize_text(plain_text(text))
                for field in ("summary", "discover", "engineer", "research"):
                    expected = normalize_text(concept.get(field, ""))
                    if expected and expected not in page_plain:
                        errors.append(
                            f"{rel}: learner page drift from concepts.json field {field!r}"
                        )

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

if errors:
    print("Diderot rendering contract FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(
    "Diderot rendering contract OK: "
    f"{len(concept_pages)} concept pages; "
    f"{len(detail_surfaces)} epistemic-status detail surfaces; "
    f"{len(formula_pages)} formula pages; "
    f"{formula_count} formula blocks; "
    f"{len(FORECASTING_IDS)} forecasting pages consistent with concepts.json; "
    "MathJax 3.2.2 pinned."
)
