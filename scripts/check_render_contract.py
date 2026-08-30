#!/usr/bin/env python3
"""Validate Diderot's browser rendering contract after prepare_pages.py."""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_JS = ROOT / "assets" / "js" / "site.js"

errors: list[str] = []


def expected_runtime(page: Path) -> str:
    rel = os.path.relpath(SITE_JS, page.parent).replace(os.sep, "/")
    return f'<script src="{rel}"></script>'


concept_pages = sorted((ROOT / "concepts").glob("*/index.html"))
if not concept_pages:
    errors.append("no concept pages found")

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
        if expected_runtime(page) not in text:
            errors.append(f"{page.relative_to(ROOT)}: formula page does not load shared site runtime")

for page in concept_pages:
    text = page.read_text(encoding="utf-8")
    if expected_runtime(page) not in text:
        errors.append(f"{page.relative_to(ROOT)}: concept page does not load shared site runtime")

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

if errors:
    print("Diderot rendering contract FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(
    "Diderot rendering contract OK: "
    f"{len(concept_pages)} concept pages; "
    f"{len(formula_pages)} formula pages; "
    f"{formula_count} formula blocks; MathJax 3.2.2 pinned."
)
