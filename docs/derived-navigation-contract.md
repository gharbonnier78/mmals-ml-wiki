# Derived Navigation Contract

Status: Diderot-local architecture contract for issue #17.

## Purpose

The learner-facing concept and pathway indexes are publication artifacts. They SHOULD be derived from canonical project sources rather than maintained as a second hand-edited catalogue that can drift from the underlying concepts, pathways, evidence status or publication state.

This contract governs navigation derivation only. It does not create scientific evidence, change epistemic authority, or qualify a research claim.

## Authority map

| Concern | Canonical authority | Derived-use rule |
| --- | --- | --- |
| Concept identity and titles | `data/concepts.json` plus `data/concepts-*.json` | `scripts/generate_navigation.py` merges the current registries and rejects conflicting titles. |
| Concept catalogue membership/order | `data/concept-audit.json` concept map | Generated concept cards follow its declared concept order; the concept registries, audit map and detail-page set must agree bidirectionally. |
| Concept card explanatory text | `kicker` / `summary` in a concept registry when present; otherwise the concept detail page's `eyebrow` / `lede` | Historical sparse registries are not silently invented into richer schemas. The fallback is explicit and reported by the generator. |
| Concept relations | `data/relations.json` plus `data/relations-*.json` | Not duplicated into the catalogue cards by #17. |
| Learner-facing epistemic authority | `data/epistemic-statuses.json`, resolved against `data/concept-audit.json` | #17 MUST NOT invent, upgrade or infer epistemic status from generated navigation. |
| Qualified local research evidence | `data/research-evidence-ingestion.json` under `docs/research-ingestion-contract.md` | The #15 qualification gate remains authoritative. Generated navigation cannot satisfy it. |
| Pathway card identity/order/title/tag/summary | `data/pathways.json` | The pathway index is derived from this registry and must match the detail-page set bidirectionally. |
| Mathematical notation | `mathematics/notation/registry.json` | Independent canonical notation authority; not copied into navigation metadata. |
| Release metadata | `site.config.json` | Independent release authority. Navigation generation does not change release state. |
| Research branch/publication state | `data/branches.json`, `data/publications.json` | Independent research/publication authorities. Navigation generation does not promote research maturity. |

## Deterministic generation

`scripts/prepare_pages.py` runs `scripts/generate_navigation.py` before the ordinary page-normalization pass. Therefore the same preparation step used by CI and GitHub Pages replaces the generated regions of:

- `concepts/index.html`;
- `pathways/index.html`.

The source HTML keeps the page-level pedagogical prose and layout shell. Only the card catalogue region and the concept-count badge are derived.

Generated regions carry explicit HTML comments so a reviewer can distinguish hand-authored page framing from derived catalogue content.

## Staleness rule

After preparation, `python scripts/generate_navigation.py --check` MUST pass. It fails if the prepared indexes no longer equal the deterministic projection of the canonical sources.

The normal CI and deployment workflows run preparation before this check. A source-data change therefore causes regeneration rather than leaving the published catalogue stale. A malformed, conflicting or incomplete registry causes the generator to fail closed.

## Reviewability boundary

Issue #17 makes the derivation deterministic and machine-checkable. It does not solve exact pre-merge rendered-preview distribution; that remains the separate issue #19. Reviewers can inspect the canonical registry changes, the generator, the generated-region markers and CI verdict without manually maintaining or comparing dozens of HTML cards.

## Epistemic boundary

A generated card is navigation, not evidence. In particular:

- appearing in an index does not make a concept established;
- a pathway card does not qualify the claims taught inside the pathway;
- an accepted Diderot PR does not turn a project hypothesis into qualified research evidence;
- `qualified research evidence` remains admissible only through the #15 research → independent review → Diderot ingestion contract.
