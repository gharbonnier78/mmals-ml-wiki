#!/usr/bin/env python3
"""Validate Diderot's notation registry and the pinned agent bootstrap chain."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "mathematics" / "notation" / "registry.json"
MANIFEST = ROOT / "harness-adoption.yaml"
AGENT_FILES = (ROOT / "AGENTS.md", ROOT / "CLAUDE.md")

errors: list[str] = []

try:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
except Exception as exc:  # pragma: no cover - diagnostic path
    print(f"Notation registry check FAILED\n- registry.json cannot be parsed: {exc}")
    sys.exit(1)

if data.get("schema_version") != "0.1":
    errors.append("registry schema_version must be 0.1")

entries = data.get("entries")
if not isinstance(entries, list) or not entries:
    errors.append("registry entries must be a non-empty list")
    entries = []

required = {
    "id",
    "display",
    "latex",
    "spoken",
    "concept",
    "category",
    "formal",
    "plain_language",
    "why_here",
    "example",
    "prerequisites",
    "encounters",
    "connections",
    "domains",
    "authority",
    "status",
    "maturity",
}
valid_status = {"draft", "reviewed", "stable"}
valid_maturity = {"L0", "L1", "L2", "L3", "L4", "L5"}
seen: set[str] = set()

for i, entry in enumerate(entries):
    label = entry.get("id", f"entry[{i}]") if isinstance(entry, dict) else f"entry[{i}]"
    if not isinstance(entry, dict):
        errors.append(f"{label}: entry must be an object")
        continue
    missing = sorted(required - entry.keys())
    if missing:
        errors.append(f"{label}: missing required fields: {', '.join(missing)}")
    entry_id = entry.get("id")
    if not isinstance(entry_id, str) or not entry_id.strip():
        errors.append(f"{label}: id must be a non-empty string")
    elif entry_id in seen:
        errors.append(f"{label}: duplicate semantic id")
    else:
        seen.add(entry_id)

    spoken = entry.get("spoken", {})
    if not isinstance(spoken, dict) or not spoken.get("fr_literal") or not spoken.get("fr_natural"):
        errors.append(f"{label}: spoken.fr_literal and spoken.fr_natural are required")

    example = entry.get("example", {})
    if not isinstance(example, dict) or not example.get("statement") or not example.get("explanation"):
        errors.append(f"{label}: example.statement and example.explanation are required")

    encounters = entry.get("encounters")
    if not isinstance(encounters, list) or not encounters:
        errors.append(f"{label}: at least one encounter is required")
    else:
        for j, encounter in enumerate(encounters):
            if not isinstance(encounter, dict) or not all(encounter.get(k) for k in ("source_ref", "context", "contribution")):
                errors.append(f"{label}: encounter[{j}] requires source_ref, context and contribution")

    authority = entry.get("authority", {})
    sources = authority.get("mathematical_sources") if isinstance(authority, dict) else None
    if not isinstance(sources, list) or not sources:
        errors.append(f"{label}: authority.mathematical_sources must record at least one provenance item")

    if entry.get("status") not in valid_status:
        errors.append(f"{label}: invalid status {entry.get('status')!r}")
    if entry.get("maturity") not in valid_maturity:
        errors.append(f"{label}: invalid maturity {entry.get('maturity')!r}")

    if entry.get("status") in {"reviewed", "stable"}:
        unresolved = [s for s in (sources or []) if s.get("status") == "source_identity_not_yet_catalogued"]
        if unresolved:
            errors.append(f"{label}: reviewed/stable entry cannot retain unresolved source identity")

manifest_text = MANIFEST.read_text(encoding="utf-8") if MANIFEST.exists() else ""
match = re.search(r'^\s*ref:\s*["\']?([0-9a-f]{40})["\']?\s*$', manifest_text, re.M)
if not match:
    errors.append("harness-adoption.yaml must pin a 40-character immutable commit SHA")
    harness_ref = None
else:
    harness_ref = match.group(1)

for path in AGENT_FILES:
    if not path.exists():
        errors.append(f"missing automatic agent bootstrap: {path.name}")
        continue
    text = path.read_text(encoding="utf-8")
    if "harness-adoption.yaml" not in text:
        errors.append(f"{path.name}: must direct the agent to harness-adoption.yaml")
    if harness_ref and harness_ref not in text:
        errors.append(f"{path.name}: pinned harness URL does not match harness-adoption.yaml")
    if "MATHEMATICAL_NOTATION_CAPITALIZATION.md" not in text:
        errors.append(f"{path.name}: notation-capitalization contract is not discoverable")

for path in (ROOT / "mathematics" / "notation" / "index.html", ROOT / "mathematics" / "notation" / "poster.html"):
    if not path.exists():
        errors.append(f"missing notation publication view: {path.relative_to(ROOT)}")

renderer = ROOT / "assets" / "js" / "notation-atlas.js"
if not renderer.exists() or "registry.json" not in renderer.read_text(encoding="utf-8"):
    errors.append("notation publication views must be driven by the canonical registry")

if errors:
    print("Notation registry / harness bootstrap check FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"Notation registry OK: {len(entries)} entries; harness pin {harness_ref}")
