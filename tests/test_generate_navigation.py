#!/usr/bin/env python3
"""Focused tests for issue #17 deterministic/fail-closed navigation generation."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import generate_navigation as nav  # noqa: E402


class NavigationFixture(unittest.TestCase):
    def setUp(self):
        self.original_root = nav.ROOT
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "data").mkdir()
        (self.root / "concepts" / "alpha").mkdir(parents=True)
        (self.root / "pathways" / "p1").mkdir(parents=True)
        self.write_json("data/navigation-registries.json", {"schema_version": "0.1", "concepts": ["concepts.json"], "relations": ["relations.json"]})
        self.write_json("data/concepts.json", [{"id": "alpha", "title": "Alpha", "kicker": "K", "summary": "S"}])
        self.write_json("data/relations.json", [])
        self.write_json("data/concept-audit.json", {"concepts": {"alpha": {}}})
        self.write_json("data/pathways.json", {"pathways": [{"id": "p1", "order": 10, "tag": "guided", "title": "P1", "summary": "Pathway one", "home_primary": True}]})
        self.write_json("data/epistemic-statuses.json", {"statuses": {"source-derived": {"label": "source-derived", "css_class": "foundational", "description": "From cited material."}}})
        self.write("concepts/alpha/index.html", '<div class="eyebrow">Fallback K</div><p class="lede">Fallback S</p>')
        self.write("pathways/p1/index.html", "<h1>P1</h1>")
        self.write("concepts/index.html", 'BEFORE<span class="tag" data-generated-count="concepts">0 concepts</span><div><!-- GENERATED: concept navigation from canonical concept registries --><!-- /GENERATED: concept navigation --></div>AFTER')
        self.write("pathways/index.html", 'PBEFORE<div><!-- GENERATED: pathway navigation from data/pathways.json --><!-- /GENERATED: pathway navigation --></div>PAFTER')
        self.write("index.html", 'HBEFORE<div><!-- GENERATED: home primary pathway CTA from data/pathways.json --><!-- /GENERATED: home primary pathway CTA --></div><div><!-- GENERATED: home pathway navigation from data/pathways.json --><!-- /GENERATED: home pathway navigation --></div><div><!-- GENERATED: epistemic legend from data/epistemic-statuses.json --><!-- /GENERATED: epistemic legend --></div>HAFTER')
        nav.configure_root(self.root)

    def tearDown(self):
        nav.configure_root(self.original_root)
        self.tmp.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def write_json(self, rel, value):
        self.write(rel, json.dumps(value, indent=2) + "\n")

    def assertNavError(self, fragment):
        with self.assertRaises(nav.NavigationError) as ctx:
            nav.generate_navigation(write=True, report_projection=False)
        self.assertIn(fragment, str(ctx.exception))

    def test_generation_is_confined_to_markers_and_preserves_prose(self):
        nav.generate_navigation(write=True, report_projection=False)
        self.assertIn("BEFORE", (self.root / "concepts/index.html").read_text())
        self.assertIn("AFTER", (self.root / "concepts/index.html").read_text())
        self.assertIn("PBEFORE", (self.root / "pathways/index.html").read_text())
        self.assertIn("PAFTER", (self.root / "pathways/index.html").read_text())
        self.assertIn("HBEFORE", (self.root / "index.html").read_text())
        self.assertIn("HAFTER", (self.root / "index.html").read_text())
        nav.generate_navigation(write=False, report_projection=False)

    def test_missing_marker_fails_closed(self):
        self.write("concepts/index.html", '<span class="tag" data-generated-count="concepts">0 concepts</span>NO-MARKERS')
        self.assertNavError("generated marker pair")

    def test_missing_neutral_count_badge_fails_closed(self):
        text = (self.root / "concepts/index.html").read_text()
        self.write("concepts/index.html", text.replace('<span class="tag" data-generated-count="concepts">0 concepts</span>', 'NO-COUNT'))
        self.assertNavError("neutral generated concept-count badge")

    def test_duplicate_concept_id_fails_closed(self):
        self.write_json("data/concepts-extra.json", [{"id": "alpha", "title": "Alpha", "kicker": "Other", "summary": "Other"}])
        self.write_json("data/navigation-registries.json", {"schema_version": "0.1", "concepts": ["concepts.json", "concepts-extra.json"], "relations": ["relations.json"]})
        self.assertNavError("duplicate concept id")

    def test_manifest_must_cover_new_registry(self):
        self.write_json("data/concepts-extra.json", [{"id": "beta", "title": "Beta", "kicker": "K", "summary": "S"}])
        self.assertNavError("files_not_in_manifest")

    def test_missing_pathway_page_fails_closed(self):
        (self.root / "pathways/p1/index.html").unlink()
        (self.root / "pathways/p1").rmdir()
        self.assertNavError("registry_without_page")

    def test_extra_pathway_page_fails_closed(self):
        (self.root / "pathways/p2").mkdir()
        self.write("pathways/p2/index.html", "<h1>P2</h1>")
        self.assertNavError("page_without_registry")


if __name__ == "__main__":
    unittest.main()
