# Derived Navigation Contract

Status: Diderot-local architecture contract for issue #17.

## Purpose

Learner-facing indexes, pathway cards, and other navigation projections SHOULD derive from canonical project sources rather than maintain a second hand-edited copy that can silently drift. This contract governs navigation derivation only. It does not create scientific evidence, change epistemic authority, or qualify a research claim.

## Authority map

| Concern | Canonical authority | Derived-use rule |
| --- | --- | --- |
| Registry file inventory | `data/navigation-registries.json`, checked against the actual `concepts*.json` / `relations*.json` file sets | Both build-time navigation and the Explore graph consume the same manifest. Adding/removing a matching registry without updating the manifest fails CI. |
| Concept identity and titles | Registry files declared by `data/navigation-registries.json` | `scripts/generate_navigation.py` rejects duplicate concept ids rather than silently overlaying them. |
| Concept catalogue membership/order | `data/concept-audit.json` concept map | Generated concept cards follow its declared map order; registries, audit map and detail-page set must agree bidirectionally. |
| Concept card explanatory text | `kicker` / `summary` in a concept registry when present; otherwise the concept detail page's `eyebrow` / `lede` | Historical sparse registries use an explicit transitional fallback. CI prints each card's text source. |
| Concept relations | Relation registries declared by `data/navigation-registries.json` | Explore loads the declared set dynamically. |
| Learner-facing epistemic authority | `data/epistemic-statuses.json`, resolved against `data/concept-audit.json` | The home legend is a generated vocabulary view. Navigation MUST NOT invent or upgrade epistemic status. |
| Qualified local research evidence | `data/research-evidence-ingestion.json` under `docs/research-ingestion-contract.md` | The #15 qualification gate remains authoritative. Generated navigation cannot satisfy it. |
| Pathway identity/order/title/tag/summary | `data/pathways.json` | Pathway index and home pathway cards derive from it. Exactly one `home_primary` entry supplies the primary home CTA. |
| Mathematical notation | `mathematics/notation/registry.json` | Independent canonical notation authority; not copied into navigation metadata. |
| Release metadata | `site.config.json` | Independent release authority. Navigation generation does not change release state. |
| Research branch/publication state | `data/branches.json`, `data/publications.json` | Independent research/publication authorities. Navigation generation does not promote research maturity. |

## Learner-facing derived-view inventory

| View | Treatment in #17 |
| --- | --- |
| `concepts/index.html` concept cards and count | Generated inside committed marker placeholders; count uses a neutral `.tag`, never an epistemic status class. |
| `pathways/index.html` cards | Generated inside committed marker placeholders. |
| Home primary pathway CTA | Generated from the unique `home_primary` pathway. |
| Home pathway cards | Generated from all canonical pathway records; no hand-maintained numeric total. |
| Home epistemic legend | Generated from `data/epistemic-statuses.json`; explanatory prose states that named labels, not color, carry authority. |
| Explore registry list | Generated at runtime from `data/navigation-registries.json`; CI checks manifest/file-set agreement. |
| Explore `categoryById` display taxonomy | Deliberately manual presentation metadata for filtering/color only; it is not identity, title, evidence, or epistemic authority. Follow-up belongs with broader Explore/usability work rather than #17's canonical registry membership gate. |
| Concept-page navigation targets | Existing global-nav inconsistencies are tracked by #30. |
| Legacy concept-page status-colored pills | Pre-existing semantic/visual cleanup remains tracked by #28; the home key now states that color alone carries no authority. |
| Concept-index pathway promotions | Removed as duplicated pathway metadata; replaced by a generic link to the canonical pathway catalogue. |

## Deterministic generation and marker confinement

`scripts/prepare_pages.py` runs `scripts/generate_navigation.py` before ordinary page normalization. Source HTML commits explicit empty GENERATED marker pairs. The generator:

- requires exactly one marker pair for every generated region;
- never searches for a grid/layout heuristic;
- only replaces bytes between those markers;
- fails closed if markers or the neutral concept-count badge are missing;
- prints the full derived concept/pathway projection and text-source provenance in CI build output.

Therefore surrounding pedagogical prose remains hand-authored and reviewable, while the derived projection remains reproducible without committing a second full card catalogue.

## Staleness and failure rule

After preparation, `python scripts/generate_navigation.py --check` MUST pass. A malformed registry, manifest mismatch, duplicate concept id, missing/extra concept or pathway page, missing marker, or malformed count badge fails closed.

`check-links.yml` additionally runs focused fixture tests before preparation so failure paths are exercised independently of the build rewrite. The prepared-tree check remains an idempotency/staleness check of the actual publication artifact.

## Reviewability boundary

Issue #17 does not solve exact pre-merge rendered-preview distribution; that remains #19. For #17, reviewability is provided by canonical data diffs, explicit source placeholders, fail-closed marker confinement, full projection output in CI, focused tests, and the exact-SHA CI verdict.

## Epistemic boundary

A generated card is navigation, not evidence. In particular:

- appearing in an index does not make a concept established;
- a pathway card does not qualify the claims taught inside the pathway;
- only the canonical named epistemic labels carry epistemic meaning; shared colors or generic `.tag` pills do not;
- an accepted Diderot PR does not turn a project hypothesis into qualified research evidence;
- `qualified research evidence` remains admissible only through the #15 research → independent review → Diderot ingestion contract.

## Transitional fallback debt

The detail-page `eyebrow` / `lede` fallback remains intentionally transitional because historical registries are sparse. CI reports the affected text sources for every build. A future migration may enrich registries, but it must not create a parallel authority or silently upgrade status.
