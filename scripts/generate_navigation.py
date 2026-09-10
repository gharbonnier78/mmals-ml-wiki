#!/usr/bin/env python3
"""Generate learner-facing navigation from canonical Diderot project data.

Generated navigation is a derived publication view. It never creates epistemic
authority or scientific evidence. Source HTML must declare explicit GENERATED
marker pairs; layout heuristics are intentionally forbidden.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any

CONCEPT_MARKER_START = "<!-- GENERATED: concept navigation from canonical concept registries -->"
CONCEPT_MARKER_END = "<!-- /GENERATED: concept navigation -->"
PATHWAY_MARKER_START = "<!-- GENERATED: pathway navigation from data/pathways.json -->"
PATHWAY_MARKER_END = "<!-- /GENERATED: pathway navigation -->"
HOME_PATHWAY_MARKER_START = "<!-- GENERATED: home pathway navigation from data/pathways.json -->"
HOME_PATHWAY_MARKER_END = "<!-- /GENERATED: home pathway navigation -->"
HOME_CTA_MARKER_START = "<!-- GENERATED: home primary pathway CTA from data/pathways.json -->"
HOME_CTA_MARKER_END = "<!-- /GENERATED: home primary pathway CTA -->"
HOME_EPISTEMIC_MARKER_START = "<!-- GENERATED: epistemic legend from data/epistemic-statuses.json -->"
HOME_EPISTEMIC_MARKER_END = "<!-- /GENERATED: epistemic legend -->"


class NavigationError(RuntimeError):
    pass


def configure_root(root: Path) -> None:
    global ROOT, DATA, CONCEPTS, PATHWAYS, CONCEPT_INDEX, PATHWAY_INDEX, HOME_INDEX
    global CONCEPT_AUDIT, PATHWAY_REGISTRY, REGISTRY_MANIFEST, EPISTEMIC_REGISTRY
    ROOT = Path(root).resolve()
    DATA = ROOT / "data"
    CONCEPTS = ROOT / "concepts"
    PATHWAYS = ROOT / "pathways"
    CONCEPT_INDEX = CONCEPTS / "index.html"
    PATHWAY_INDEX = PATHWAYS / "index.html"
    HOME_INDEX = ROOT / "index.html"
    CONCEPT_AUDIT = DATA / "concept-audit.json"
    PATHWAY_REGISTRY = DATA / "pathways.json"
    REGISTRY_MANIFEST = DATA / "navigation-registries.json"
    EPISTEMIC_REGISTRY = DATA / "epistemic-statuses.json"


configure_root(Path(__file__).resolve().parents[1])


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


def _manifest_names(key: str, discovered: set[str]) -> list[str]:
    manifest = load_json(REGISTRY_MANIFEST)
    values = manifest.get(key) if isinstance(manifest, dict) else None
    if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v for v in values):
        raise NavigationError(f"data/navigation-registries.json: {key} must be a non-empty string list")
    if len(values) != len(set(values)):
        raise NavigationError(f"data/navigation-registries.json: duplicate {key} entry")
    declared = set(values)
    if declared != discovered:
        files_not_in_manifest = sorted(discovered - declared)
        manifest_without_file = sorted(declared - discovered)
        raise NavigationError(
            f"navigation registry manifest {key} mismatch: "
            f"files_not_in_manifest={files_not_in_manifest}, manifest_without_file={manifest_without_file}"
        )
    return values


def concept_registry_paths() -> list[Path]:
    discovered = {p.name for p in [DATA / "concepts.json", *sorted(DATA.glob("concepts-*.json"))] if p.exists()}
    return [DATA / name for name in _manifest_names("concepts", discovered)]


def relation_registry_paths() -> list[Path]:
    discovered = {p.name for p in [DATA / "relations.json", *sorted(DATA.glob("relations-*.json"))] if p.exists()}
    return [DATA / name for name in _manifest_names("relations", discovered)]


def validate_registry_manifest() -> None:
    concept_registry_paths()
    relation_registry_paths()


def collect_concepts() -> tuple[list[dict[str, str]], list[str]]:
    audit = load_json(CONCEPT_AUDIT)
    audited = audit.get("concepts", {})
    if not isinstance(audited, dict) or not audited:
        raise NavigationError("data/concept-audit.json has no concept map")

    merged: dict[str, dict[str, str]] = {}
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
            if concept_id in merged:
                raise NavigationError(f"duplicate concept id across canonical registries: {concept_id}")
            merged[concept_id] = {
                "id": concept_id,
                "title": title,
                "kicker": nonempty_text(raw.get("kicker")),
                "summary": nonempty_text(raw.get("summary")),
                "_registry_source": str(path.relative_to(ROOT)),
            }

    page_ids = {p.parent.name for p in CONCEPTS.glob("*/index.html")}
    registry_ids = set(merged)
    audit_ids = set(audited)
    if registry_ids != page_ids:
        registry_without_page = sorted(registry_ids - page_ids)
        page_without_registry = sorted(page_ids - registry_ids)
        raise NavigationError(
            "concept registry/page mismatch: "
            f"registry_without_page={registry_without_page}, page_without_registry={page_without_registry}"
        )
    if audit_ids != page_ids:
        audit_without_page = sorted(audit_ids - page_ids)
        page_without_audit = sorted(page_ids - audit_ids)
        raise NavigationError(
            "concept audit/page mismatch: "
            f"audit_without_page={audit_without_page}, page_without_audit={page_without_audit}"
        )

    cards: list[dict[str, str]] = []
    fallback_fields = 0
    for order, concept_id in enumerate(audited, start=1):
        item = dict(merged[concept_id])
        page = CONCEPTS / concept_id / "index.html"
        text_sources: list[str] = []
        if not item["kicker"]:
            item["kicker"] = extract_page_text(page, r'<div class="eyebrow">(.*?)</div>', "eyebrow")
            text_sources.append("kicker=detail-page")
            fallback_fields += 1
        else:
            text_sources.append(f"kicker={item['_registry_source']}")
        if not item["summary"]:
            item["summary"] = extract_page_text(page, r'<p class="lede">(.*?)</p>', "lede")
            text_sources.append("summary=detail-page")
            fallback_fields += 1
        else:
            text_sources.append(f"summary={item['_registry_source']}")
        item["order"] = str(order)
        item["_text_source"] = ";".join(text_sources)
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
    primary_count = 0
    for raw in rows:
        if not isinstance(raw, dict):
            raise NavigationError("data/pathways.json: pathway entry must be an object")
        pathway_id = nonempty_text(raw.get("id"))
        title = nonempty_text(raw.get("title"))
        tag = nonempty_text(raw.get("tag"))
        summary = nonempty_text(raw.get("summary"))
        order = raw.get("order")
        home_primary = raw.get("home_primary", False)
        if not pathway_id or not title or not tag or not summary or not isinstance(order, int):
            raise NavigationError(f"pathway {pathway_id or '<unknown>'}: id/order/tag/title/summary are required")
        if not isinstance(home_primary, bool):
            raise NavigationError(f"pathway {pathway_id}: home_primary must be boolean")
        if pathway_id in seen_ids:
            raise NavigationError(f"duplicate pathway id: {pathway_id}")
        if order in seen_orders:
            raise NavigationError(f"duplicate pathway order: {order}")
        seen_ids.add(pathway_id)
        seen_orders.add(order)
        primary_count += int(home_primary)
        cards.append({
            "id": pathway_id, "title": title, "tag": tag, "summary": summary,
            "order": str(order), "home_primary": "true" if home_primary else "false",
        })

    if primary_count != 1:
        raise NavigationError(f"data/pathways.json must declare exactly one home_primary pathway, found {primary_count}")

    page_ids = {p.parent.name for p in PATHWAYS.glob("*/index.html")}
    if seen_ids != page_ids:
        registry_without_page = sorted(seen_ids - page_ids)
        page_without_registry = sorted(page_ids - seen_ids)
        raise NavigationError(
            "pathway registry/page mismatch: "
            f"registry_without_page={registry_without_page}, page_without_registry={page_without_registry}"
        )
    return sorted(cards, key=lambda item: int(item["order"]))


def collect_epistemic_statuses() -> list[dict[str, str]]:
    data = load_json(EPISTEMIC_REGISTRY)
    statuses = data.get("statuses") if isinstance(data, dict) else None
    if not isinstance(statuses, dict) or not statuses:
        raise NavigationError("data/epistemic-statuses.json has no statuses map")
    result = []
    for status_id, raw in statuses.items():
        if not isinstance(raw, dict):
            raise NavigationError(f"epistemic status {status_id}: entry must be an object")
        label = nonempty_text(raw.get("label"))
        css_class = nonempty_text(raw.get("css_class"))
        description = nonempty_text(raw.get("description"))
        if not label or not css_class or not description:
            raise NavigationError(f"epistemic status {status_id}: label/css_class/description required")
        result.append({"id": status_id, "label": label, "css_class": css_class, "description": description})
    return result


def render_cards(cards: list[dict[str, str]], tag_field: str, *, href_prefix: str = "") -> str:
    rendered: list[str] = []
    for item in cards:
        rendered.append(
            '<a class="card" href="{prefix}{id}/index.html"><span class="tag">{tag}</span>'
            '<h3>{title}</h3><p>{summary}</p></a>'.format(
                prefix=html.escape(href_prefix, quote=True),
                id=html.escape(item["id"], quote=True),
                tag=html.escape(item[tag_field]),
                title=html.escape(item["title"]),
                summary=html.escape(item["summary"]),
            )
        )
    return "\n".join(rendered)


def render_home_pathways(pathways: list[dict[str, str]]) -> str:
    rendered = []
    for item in pathways:
        rendered.append(
            '<a class="card" href="pathways/{id}/index.html"><span class="tag">{tag}</span>'
            '<h3>{title}</h3><p>{summary}</p><span class="arrow">→</span></a>'.format(
                id=html.escape(item["id"], quote=True),
                tag=html.escape(item["tag"]),
                title=html.escape(item["title"]),
                summary=html.escape(item["summary"]),
            )
        )
    return "\n".join(rendered)


def render_home_primary_cta(pathways: list[dict[str, str]]) -> str:
    item = next(p for p in pathways if p["home_primary"] == "true")
    return '<a class="button primary" href="pathways/{id}/index.html">{title}</a>'.format(
        id=html.escape(item["id"], quote=True), title=html.escape(item["title"])
    )


def render_epistemic_legend(statuses: list[dict[str, str]]) -> str:
    return "\n".join(
        '<div class="card"><span class="status {css}">{label}</span><p>{description}</p></div>'.format(
            css=html.escape(item["css_class"], quote=True),
            label=html.escape(item["label"]),
            description=html.escape(item["description"]),
        )
        for item in statuses
    )


def replace_generated_region(text: str, generated_html: str, marker_start: str, marker_end: str, *, label: str) -> str:
    if text.count(marker_start) != 1 or text.count(marker_end) != 1:
        raise NavigationError(f"{label}: expected exactly one committed generated marker pair")
    start = text.index(marker_start)
    end = text.index(marker_end, start)
    if end <= start:
        raise NavigationError(f"{label}: malformed generated marker order")
    replacement = f"{marker_start}\n{generated_html}\n{marker_end}"
    return text[:start] + replacement + text[end + len(marker_end):]


def expected_indexes() -> tuple[dict[Path, str], list[str], list[dict[str, str]], list[dict[str, str]]]:
    validate_registry_manifest()
    concepts, concept_sources = collect_concepts()
    pathways = collect_pathways()
    statuses = collect_epistemic_statuses()

    concept_text = CONCEPT_INDEX.read_text(encoding="utf-8")
    concept_text = replace_generated_region(
        concept_text, render_cards(concepts, "kicker"),
        CONCEPT_MARKER_START, CONCEPT_MARKER_END, label="concept index",
    )
    concept_text, count = re.subn(
        r'<span class="tag" data-generated-count="concepts">\d+\s+concepts</span>',
        f'<span class="tag" data-generated-count="concepts">{len(concepts)} concepts</span>',
        concept_text, count=1,
    )
    if count != 1:
        raise NavigationError("concept index is missing its neutral generated concept-count badge")

    pathway_text = PATHWAY_INDEX.read_text(encoding="utf-8")
    pathway_text = replace_generated_region(
        pathway_text, render_cards(pathways, "tag"),
        PATHWAY_MARKER_START, PATHWAY_MARKER_END, label="pathway index",
    )

    home_text = HOME_INDEX.read_text(encoding="utf-8")
    home_text = replace_generated_region(
        home_text, render_home_pathways(pathways),
        HOME_PATHWAY_MARKER_START, HOME_PATHWAY_MARKER_END, label="home pathway cards",
    )
    home_text = replace_generated_region(
        home_text, render_home_primary_cta(pathways),
        HOME_CTA_MARKER_START, HOME_CTA_MARKER_END, label="home primary pathway CTA",
    )
    home_text = replace_generated_region(
        home_text, render_epistemic_legend(statuses),
        HOME_EPISTEMIC_MARKER_START, HOME_EPISTEMIC_MARKER_END, label="home epistemic legend",
    )

    return ({CONCEPT_INDEX: concept_text, PATHWAY_INDEX: pathway_text, HOME_INDEX: home_text}, concept_sources, concepts, pathways)


def emit_projection(concepts: list[dict[str, str]], pathways: list[dict[str, str]]) -> None:
    print("Derived navigation projection (reviewable build output):")
    for item in concepts:
        print(
            "CONCEPT "
            f"order={item['order']} id={item['id']} title={item['title']!r} "
            f"kicker={item['kicker']!r} summary={item['summary']!r} source={item['_text_source']}"
        )
    for item in pathways:
        print(
            "PATHWAY "
            f"order={item['order']} id={item['id']} title={item['title']!r} "
            f"tag={item['tag']!r} summary={item['summary']!r} home_primary={item['home_primary']}"
        )


def generate_navigation(*, write: bool, report_projection: bool | None = None) -> tuple[int, int, list[str]]:
    expected, concept_sources, concepts, pathways = expected_indexes()
    stale: list[str] = []
    for path, target in expected.items():
        current = path.read_text(encoding="utf-8")
        if current != target:
            stale.append(str(path.relative_to(ROOT)))
            if write:
                path.write_text(target, encoding="utf-8")

    if stale and not write:
        raise NavigationError(f"derived navigation is stale: {', '.join(stale)}")
    if report_projection is None:
        report_projection = write
    if report_projection:
        emit_projection(concepts, pathways)
    return len(concepts), len(pathways), concept_sources


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if prepared navigation differs from canonical sources")
    args = parser.parse_args()
    try:
        concept_count, pathway_count, sources = generate_navigation(write=not args.check, report_projection=True)
    except (NavigationError, json.JSONDecodeError) as exc:
        print(f"Generated navigation FAILED: {exc}")
        raise SystemExit(1)
    mode = "CHECK" if args.check else "WRITE"
    print(f"Generated navigation {mode}: {concept_count} concepts; {pathway_count} pathways")
    print("Concept authorities: " + ", ".join(sources))
    print("Pathway authority: data/pathways.json")
    print("Registry manifest: data/navigation-registries.json")


if __name__ == "__main__":
    main()
