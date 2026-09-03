#!/usr/bin/env python3
"""Generate learner-facing concept/pathway navigation from canonical project data.

This script owns only derived navigation. It does not create epistemic authority and
must not infer research qualification from page text, PR state, or generated output.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONCEPTS = ROOT / "concepts"
PATHWAYS = ROOT / "pathways"
CONCEPT_INDEX = CONCEPTS / "index.html"
PATHWAY_INDEX = PATHWAYS / "index.html"
CONCEPT_AUDIT = DATA / "concept-audit.json"
PATHWAY_REGISTRY = DATA / "pathways.json"

CONCEPT_MARKER_START = "<!-- GENERATED: concept navigation from canonical concept registries -->"
CONCEPT_MARKER_END = "<!-- /GENERATED: concept navigation -->"
PATHWAY_MARKER_START = "<!-- GENERATED: pathway navigation from data/pathways.json -->"
PATHWAY_MARKER_END = "<!-- /GENERATED: pathway navigation -->"
GRID_START = '<section class="section"><div class="grid grid-3">'


class NavigationError(RuntimeError):
    pass


def load_json(path: Path) -> Any:
    if not path.exists():
        raise NavigationError(f"missing canonical source: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def nonempty_text(value: Any) -> str:
    return str(value).strip() if value is not None else ""


def strip_html(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def extract_page_text(page: Path, pattern: str, label: str) -> str:
    text = page.read_text(encoding="utf-8")
    match = re.search(pattern, text, re.S | re.I)
    if not match:
        raise NavigationError(f"{page.relative_to(ROOT)}: cannot recover {label}")
    value = strip_html(match.group(1))
    if not value:
        raise NavigationError(f"{page.relative_to(ROOT)}: empty {label}")
    return value


def concept_registry_paths() -> list[Path]:
    primary = DATA / "concepts.json"
    supplements = sorted(DATA.glob("concepts-*.json"))
    return [primary, *supplements]


def collect_concepts() -> tuple[list[dict[str, str]], list[str]]:
    audit = load_json(CONCEPT_AUDIT)
    audited = audit.get("concepts", {})
    if not isinstance(audited, dict) or not audited:
        raise NavigationError("data/concept-audit.json has no concept map")

    merged: dict[str, dict[str, str]] = {}
    sources: dict[str, list[str]] = {}
    registry_paths = concept_registry_paths()
    for path in registry_paths:
        data = load_json(path)
        if not isinstance(data, list):
            raise NavigationError(f"{path.relative_to(ROOT)}: concept registry must be a list")
        for raw in data:
            if not isinstance(raw, dict):
                raise NavigationError(f"{path.relative_to(ROOT)}: concept entry must be an object")
            concept_id = nonempty_text(raw.get("id"))
            title = nonempty_text(raw.get("title"))
            if not concept_id or not title:
                raise NavigationError(f"{path.relative_to(ROOT)}: every concept requires id and title")
            incoming = {
                "id": concept_id,
                "title": title,
                "kicker": nonempty_text(raw.get("kicker")),
                "summary": nonempty_text(raw.get("summary")),
            }
            if concept_id in merged:
                current = merged[concept_id]
                if current["title"] != title:
                    raise NavigationError(
                        f"concept {concept_id}: conflicting titles {current['title']!r} vs {title!r}"
                    )
                for field in ("kicker", "summary"):
                    if incoming[field]:
                        if current[field] and current[field] != incoming[field]:
                            raise NavigationError(
                                f"concept {concept_id}: conflicting {field} across canonical registries"
                            )
                        current[field] = incoming[field]
            else:
                merged[concept_id] = incoming
            sources.setdefault(concept_id, []).append(str(path.relative_to(ROOT)))

    page_ids = {p.parent.name for p in CONCEPTS.glob("*/index.html")}
    registry_ids = set(merged)
    audit_ids = set(audited)
    if registry_ids != page_ids:
        missing = sorted(page_ids - registry_ids)
        extra = sorted(registry_ids - page_ids)
        raise NavigationError(f"concept registry/page mismatch: missing={missing}, extra={extra}")
    if audit_ids != page_ids:
        missing = sorted(page_ids - audit_ids)
        extra = sorted(audit_ids - page_ids)
        raise NavigationError(f"concept audit/page mismatch: missing={missing}, extra={extra}")

    cards: list[dict[str, str]] = []
    fallback_fields = 0
    for concept_id in audited:  # JSON order is the canonical catalogue order for this projection.
        item = dict(merged[concept_id])
        page = CONCEPTS / concept_id / "index.html"
        if not item["kicker"]:
            item["kicker"] = extract_page_text(page, r'<div class="eyebrow">(.*?)</div>', "eyebrow")
            fallback_fields += 1
        if not item["summary"]:
            item["summary"] = extract_page_text(page, r'<p class="lede">(.*?)</p>', "lede")
            fallback_fields += 1
        cards.append(item)

    source_names = [str(path.relative_to(ROOT)) for path in registry_paths]
    source_names.append(f"detail-page fallback fields={fallback_fields}")
    return cards, source_names


def collect_pathways() -> list[dict[str, str]]:
    data = load_json(PATHWAY_REGISTRY)
    rows = data.get("pathways", {}) if isinstance(data, dict) else None
    if not isinstance(rows, list) or not rows:
        raise NavigationError("data/pathways.json must contain a non-empty pathways list")

    seen_ids: set[str] = set()
    seen_orders: set[int] = set()
    cards: list[dict[str, str]] = []
    for raw in rows:
        if not isinstance(raw, dict):
            raise NavigationError("data/pathways.json: pathway entry must be an object")
        pathway_id = nonempty_text(raw.get("id"))
        title = nonempty_text(raw.get("title"))
        tag = nonempty_text(raw.get("tag"))
        summary = nonempty_text(raw.get("summary"))
        order = raw.get("order")
        if not pathway_id or not title or not tag or not summary or not isinstance(order, int):
            raise NavigationError(f"pathway {pathway_id or '<unknown>'}: id/order/tag/title/summary are required")
        if pathway_id in seen_ids:
            raise NavigationError(f"duplicate pathway id: {pathway_id}")
        if order in seen_orders:
            raise NavigationError(f"duplicate pathway order: {order}")
        seen_ids.add(pathway_id)
        seen_orders.add(order)
        cards.append({"id": pathway_id, "title": title, "tag": tag, "summary": summary, "order": str(order)})

    page_ids = {p.parent.name for p in PATHWAYS.glob("*/index.html")}
    if seen_ids != page_ids:
        missing = sorted(page_ids - seen_ids)
        extra = sorted(seen_ids - page_ids)
        raise NavigationError(f"pathway registry/page mismatch: missing={missing}, extra={extra}")
    return sorted(cards, key=lambda item: int(item["order"]))


def render_cards(cards: list[dict[str, str]], tag_field: str) -> str:
    rendered: list[str] = []
    for item in cards:
        rendered.append(
            '<a class="card" href="{id}/index.html"><span class="tag">{tag}</span>'
            '<h3>{title}</h3><p>{summary}</p></a>'.format(
                id=html.escape(item["id"], quote=True),
                tag=html.escape(item[tag_field]),
                title=html.escape(item["title"]),
                summary=html.escape(item["summary"]),
            )
        )
    return "\n".join(rendered)


def replace_generated_region(
    text: str,
    cards_html: str,
    marker_start: str,
    marker_end: str,
    trailing_anchor: str,
) -> str:
    replacement = f"{marker_start}\n{cards_html}\n{marker_end}"
    marker_pattern = re.compile(re.escape(marker_start) + r".*?" + re.escape(marker_end), re.S)
    if marker_pattern.search(text):
        return marker_pattern.sub(replacement, text, count=1)

    start = text.find(GRID_START)
    if start < 0:
        raise NavigationError("index page is missing expected grid start")
    body_start = start + len(GRID_START)
    body_end = text.find(trailing_anchor, body_start)
    if body_end < 0:
        raise NavigationError("index page is missing expected grid end anchor")
    return text[:body_start] + "\n" + replacement + "\n" + text[body_end:]


def expected_indexes() -> tuple[dict[Path, str], list[str]]:
    concepts, concept_sources = collect_concepts()
    pathways = collect_pathways()

    concept_text = CONCEPT_INDEX.read_text(encoding="utf-8")
    concept_text = replace_generated_region(
        concept_text,
        render_cards(concepts, "kicker"),
        CONCEPT_MARKER_START,
        CONCEPT_MARKER_END,
        '</div></section><section class="section">',
    )
    concept_text, count = re.subn(
        r'<span class="status foundational">\d+\s+concepts</span>',
        f'<span class="status foundational">{len(concepts)} concepts</span>',
        concept_text,
        count=1,
    )
    if count != 1:
        raise NavigationError("concept index is missing its canonical concept-count badge")

    pathway_text = PATHWAY_INDEX.read_text(encoding="utf-8")
    pathway_text = replace_generated_region(
        pathway_text,
        render_cards(pathways, "tag"),
        PATHWAY_MARKER_START,
        PATHWAY_MARKER_END,
        '</div></section></div></main>',
    )
    return {CONCEPT_INDEX: concept_text, PATHWAY_INDEX: pathway_text}, concept_sources


def generate_navigation(*, write: bool) -> tuple[int, int, list[str]]:
    expected, concept_sources = expected_indexes()
    stale: list[str] = []
    for path, target in expected.items():
        current = path.read_text(encoding="utf-8")
        if current != target:
            stale.append(str(path.relative_to(ROOT)))
            if write:
                path.write_text(target, encoding="utf-8")

    concept_count = len(collect_concepts()[0])
    pathway_count = len(collect_pathways())
    if stale and not write:
        raise NavigationError(f"derived navigation is stale: {', '.join(stale)}")
    return concept_count, pathway_count, concept_sources


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if prepared navigation differs from canonical sources")
    args = parser.parse_args()
    try:
        concept_count, pathway_count, sources = generate_navigation(write=not args.check)
    except (NavigationError, json.JSONDecodeError) as exc:
        print(f"Generated navigation FAILED: {exc}")
        raise SystemExit(1)
    mode = "CHECK" if args.check else "WRITE"
    print(f"Generated navigation {mode}: {concept_count} concepts; {pathway_count} pathways")
    print("Concept authorities: " + ", ".join(sources))
    print("Pathway authority: data/pathways.json")


if __name__ == "__main__":
    main()
