#!/usr/bin/env python3
"""Prepare the static Diderot artifact for publication.

Source pages intentionally stay compact. This deterministic, idempotent build step:

1. guarantees that every concept page (and every page carrying a `.formula` block) loads
   the shared site runtime used for epistemic-audit overlays and MathJax rendering; and
2. normalizes public footer release metadata from the single `site.config.json` authority.

The second rule matters for generated/pedagogical pages: source HTML may describe itself as a
derived teaching view, but the deployed artifact must still expose the repository's canonical
release/version metadata and pass `check_release_consistency.py`.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_JS = ROOT / "assets" / "js" / "site.js"
CONFIG = json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))
EXPECTED_RELEASE = f"Release v{CONFIG['version']} · Reviewed {CONFIG['last_reviewed']}"
EXPECTED_FOOTER = (
    f"Content: {CONFIG['content_license']} · Code: {CONFIG['code_license']} · {EXPECTED_RELEASE}"
)
FOOTER_METADATA_RE = re.compile(r'(<div class="small">)Content:.*?(</div>)', re.S)


def script_tag_for(page: Path) -> str:
    rel = os.path.relpath(SITE_JS, page.parent).replace(os.sep, "/")
    return f'<script src="{rel}"></script>'


def needs_runtime(page: Path, text: str) -> bool:
    rel = page.relative_to(ROOT)
    is_concept_page = len(rel.parts) == 3 and rel.parts[0] == "concepts" and rel.name == "index.html"
    has_formula = 'class="formula"' in text or "class='formula'" in text
    return is_concept_page or has_formula


def normalize(page: Path) -> tuple[bool, bool]:
    text = page.read_text(encoding="utf-8")
    updated = text
    footer_changed = False
    runtime_changed = False

    # Existing pages are allowed to carry additional footer prose as long as the canonical
    # release signature is already present. New/derived pages without it are normalized.
    if '<footer class="footer">' in updated and EXPECTED_RELEASE not in updated:
        replacement = rf"\1{EXPECTED_FOOTER}\2"
        normalized, count = FOOTER_METADATA_RE.subn(replacement, updated, count=1)
        if count == 0:
            raise RuntimeError(
                f"{page.relative_to(ROOT)}: footer lacks release metadata and no Content/Code slot was found"
            )
        updated = normalized
        footer_changed = True

    if needs_runtime(page, updated):
        tag = script_tag_for(page)
        if tag not in updated:
            if "</body>" not in updated:
                raise RuntimeError(f"{page.relative_to(ROOT)}: cannot inject site runtime; </body> missing")
            updated = updated.replace("</body>", f"{tag}</body>", 1)
            runtime_changed = True

    if updated != text:
        page.write_text(updated, encoding="utf-8")

    return runtime_changed, footer_changed


def main() -> None:
    runtime_changed: list[str] = []
    footer_changed: list[str] = []
    candidates = sorted(ROOT.rglob("*.html"))
    for page in candidates:
        runtime, footer = normalize(page)
        rel = page.relative_to(ROOT).as_posix()
        if runtime:
            runtime_changed.append(rel)
        if footer:
            footer_changed.append(rel)

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
        f"{len(runtime_changed)} runtime injections; "
        f"{len(footer_changed)} footer normalizations."
    )


if __name__ == "__main__":
    main()
