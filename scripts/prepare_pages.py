#!/usr/bin/env python3
"""Prepare the static Diderot artifact for publication.

Source concept pages intentionally stay compact. This build step guarantees that every
concept page (and every page carrying a `.formula` block) loads the shared site runtime,
which provides the epistemic-audit overlay and MathJax rendering.

The transformation is deterministic and idempotent.
"""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_JS = ROOT / "assets" / "js" / "site.js"


def script_tag_for(page: Path) -> str:
    rel = os.path.relpath(SITE_JS, page.parent).replace(os.sep, "/")
    return f'<script src="{rel}"></script>'


def needs_runtime(page: Path, text: str) -> bool:
    rel = page.relative_to(ROOT)
    is_concept_page = len(rel.parts) == 3 and rel.parts[0] == "concepts" and rel.name == "index.html"
    has_formula = 'class="formula"' in text or "class='formula'" in text
    return is_concept_page or has_formula


def normalize(page: Path) -> bool:
    text = page.read_text(encoding="utf-8")
    if not needs_runtime(page, text):
        return False

    tag = script_tag_for(page)
    if tag in text:
        return False
    if "</body>" not in text:
        raise RuntimeError(f"{page.relative_to(ROOT)}: cannot inject site runtime; </body> missing")

    updated = text.replace("</body>", f"{tag}</body>", 1)
    page.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    changed = []
    candidates = sorted(ROOT.rglob("*.html"))
    for page in candidates:
        if normalize(page):
            changed.append(page.relative_to(ROOT).as_posix())

    concept_pages = list((ROOT / "concepts").glob("*/index.html"))
    formula_pages = []
    for page in candidates:
        text = page.read_text(encoding="utf-8")
        if 'class="formula"' in text or "class='formula'" in text:
            formula_pages.append(page)

    print(
        "Prepared Pages artifact: "
        f"{len(concept_pages)} concept pages; "
        f"{len(formula_pages)} formula pages; "
        f"{len(changed)} runtime injections."
    )


if __name__ == "__main__":
    main()
