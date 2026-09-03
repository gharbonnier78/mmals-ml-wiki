#!/usr/bin/env python3
"""Prepare the static Diderot artifact for publication.

Source pages intentionally stay compact. This deterministic, idempotent build step:

1. derives concept/pathway navigation from its canonical authorities;
2. guarantees that every concept page (and every page carrying a `.formula` block) loads
   the shared site runtime used for epistemic-audit overlays and MathJax rendering;
3. guarantees that learner-facing concept/lab/pathway detail pages load the canonical
   epistemic-status runtime; and
4. normalizes public footer release metadata from the single `site.config.json` authority.

The fourth rule matters for generated/pedagogical pages: source HTML may describe itself as a
derived teaching view, but the deployed artifact must still expose the repository's canonical
release/version metadata and pass `check_release_consistency.py`.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

from generate_navigation import generate_navigation

ROOT = Path(__file__).resolve().parents[1]
SITE_JS = ROOT / "assets" / "js" / "site.js"
EPISTEMIC_JS = ROOT / "assets" / "js" / "epistemic-status.js"
CONFIG = json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))
EXPECTED_RELEASE = f"Release v{CONFIG['version']} · Reviewed {CONFIG['last_reviewed']}"
EXPECTED_FOOTER = (
    f"Content: {CONFIG['content_license']} · Code: {CONFIG['code_license']} · {EXPECTED_RELEASE}"
)
FOOTER_METADATA_RE = re.compile(r'(<div class="small">)Content:.*?(</div>)', re.S)


def script_tag_for(page: Path, script: Path) -> str:
    rel = os.path.relpath(script, page.parent).replace(os.sep, "/")
    return f'<script src="{rel}"></script>'


def needs_runtime(page: Path, text: str) -> bool:
    rel = page.relative_to(ROOT)
    is_concept_page = len(rel.parts) == 3 and rel.parts[0] == "concepts" and rel.name == "index.html"
    has_formula = 'class="formula"' in text or "class='formula'" in text
    return is_concept_page or has_formula


def needs_epistemic_runtime(page: Path) -> bool:
    rel = page.relative_to(ROOT)
    return (
        len(rel.parts) == 3
        and rel.parts[0] in {"concepts", "labs", "pathways"}
        and rel.name == "index.html"
    )


def inject_script(page: Path, text: str, script: Path) -> tuple[str, bool]:
    tag = script_tag_for(page, script)
    if tag in text:
        return text, False
    if "</body>" not in text:
        raise RuntimeError(f"{page.relative_to(ROOT)}: cannot inject runtime; </body> missing")
    return text.replace("</body>", f"{tag}</body>", 1), True


def normalize(page: Path) -> tuple[bool, bool, bool]:
    text = page.read_text(encoding="utf-8")
    updated = text
    footer_changed = False
    runtime_changed = False
    epistemic_changed = False

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
        updated, runtime_changed = inject_script(page, updated, SITE_JS)

    if needs_epistemic_runtime(page):
        updated, epistemic_changed = inject_script(page, updated, EPISTEMIC_JS)

    if updated != text:
        page.write_text(updated, encoding="utf-8")

    return runtime_changed, epistemic_changed, footer_changed


def main() -> None:
    concept_navigation, pathway_navigation, _ = generate_navigation(write=True)

    runtime_changed: list[str] = []
    epistemic_changed: list[str] = []
    footer_changed: list[str] = []
    candidates = sorted(ROOT.rglob("*.html"))
    for page in candidates:
        runtime, epistemic, footer = normalize(page)
        rel = page.relative_to(ROOT).as_posix()
        if runtime:
            runtime_changed.append(rel)
        if epistemic:
            epistemic_changed.append(rel)
        if footer:
            footer_changed.append(rel)

    concept_pages = list((ROOT / "concepts").glob("*/index.html"))
    detail_surfaces = [page for page in candidates if needs_epistemic_runtime(page)]
    formula_pages = []
    for page in candidates:
        text = page.read_text(encoding="utf-8")
        if 'class="formula"' in text or "class='formula'" in text:
            formula_pages.append(page)

    print(
        "Prepared Pages artifact: "
        f"{concept_navigation} generated concept cards; "
        f"{pathway_navigation} generated pathway cards; "
        f"{len(concept_pages)} concept pages; "
        f"{len(detail_surfaces)} epistemic-status detail surfaces; "
        f"{len(formula_pages)} formula pages; "
        f"{len(runtime_changed)} shared-runtime injections; "
        f"{len(epistemic_changed)} epistemic-runtime injections; "
        f"{len(footer_changed)} footer normalizations."
    )


if __name__ == "__main__":
    main()
