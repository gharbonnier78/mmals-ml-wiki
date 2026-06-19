#!/usr/bin/env python3
"""Fail CI when rendered pages or metadata disagree on the current release."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
version = str(config["version"])
reviewed = str(config["last_reviewed"])
errors: list[str] = []

if str(manifest.get("version")) != version:
    errors.append(f"manifest.json version={manifest.get('version')} != site.config.json version={version}")
if str(manifest.get("last_reviewed")) != reviewed:
    errors.append("manifest.json last_reviewed does not match site.config.json")

citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
if not re.search(rf"^version:\s*{re.escape(version)}\s*$", citation, re.M):
    errors.append("CITATION.cff version is not current")
if not re.search(rf"^date-released:\s*{re.escape(reviewed)}\s*$", citation, re.M):
    errors.append("CITATION.cff date-released is not current")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if f"Current release: v{version}" not in readme:
    errors.append("README.md does not declare the current release")

expected_footer = f"Release v{version} · Reviewed {reviewed}"
for page in ROOT.rglob("*.html"):
    text = page.read_text(encoding="utf-8")
    if '<footer class="footer">' in text and expected_footer not in text:
        errors.append(f"stale or missing footer metadata: {page.relative_to(ROOT)}")

research = (ROOT / "research" / "index.html").read_text(encoding="utf-8")
if f"v{version} registry" not in research:
    errors.append("research/index.html registry badge is stale")

if errors:
    print("Release consistency check FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"Release consistency OK: v{version}, reviewed {reviewed}")
