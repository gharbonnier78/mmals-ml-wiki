# Repository & Outcome Atlas — 2026-08-31

## Bind record

- Task: `repository-outcome-atlas-2026-08-31`
- Consumer: `gharbonnier78/mmals-ml-wiki`
- Harness: `gharbonnier78/scientific-research-harness`
- Pinned harness ref: `13b26f717e66e36bb753f2885091d420a99ec878`
- Local manifest: `harness-adoption.yaml`
- Mutation scope: public Diderot repository registry, outcome/status wording, quick links, rendering and structural checks.
- Scientific mutation: none. This work indexes existing repository-owned outcomes and boundaries; it does not create or promote scientific evidence.

## Objective

Replace the June 2026 static repository list with a public, searchable **Repository & Outcome Atlas** that answers two questions separately:

1. Where is the work?
2. What is the strongest bounded outcome currently registered for that repository?

The public flow is:

```text
repository -> current outcome/status -> evidence class -> source artifact -> quick links
```

## Public-scope rule

The atlas is curated rather than account-exhaustive.

Included:

- public MMALS research/evidence repositories;
- public adjacent ML, testing, systems and identity research relevant to the Diderot ecosystem;
- public research-governance/tooling repositories;
- public pedagogy/publication repositories.

Excluded:

- repositories whose GitHub visibility is private;
- repositories whose own governance states that they are not approved for external publication, even if their technical GitHub visibility is public;
- unrelated personal/utility repositories unless intentionally retained as a labelled legacy record.

`mmals-g2-geometric-perspective` is explicitly blocked from the public atlas by the validator because its own repository boundary states that it is not approved for external publication.

## Epistemic contract

The atlas uses explicit statuses:

- `supported` — bounded supporting executed evidence;
- `mixed` — some bounded support with material failures/limits;
- `negative` — a load-bearing/predeclared claim is not demonstrated or not supported;
- `hypothesis` — research direction/protocol/theory bridge not yet qualified;
- `specification` — architecture/specification outcome;
- `tool` — implemented/replayable tool;
- `governance` — reusable method/contract;
- `pedagogy` — learning/publication artifact;
- `legacy` — historical repository without a current research outcome.

A repository, citation, specification, interactive tool, CI pass, successful deployment or Diderot page MUST NOT be read as scientific evidence by itself.

Negative results are first-class outcomes and must remain visible.

## High-risk outcome sources checked for this revision

### MMALS

Source: `https://github.com/gharbonnier78/mmals/blob/main/README.md`

Atlas wording preserves the repository boundary: promising bounded replay-beating evidence exists, while the automatic selector remains insufficiently reliable for replacing safe anchored policies; minimal-sufficient-dynamic-inference remains a research-program hypothesis.

### MMALS-CAL

Source: `https://github.com/gharbonnier78/mmals-cal/blob/main/README.md`

Atlas wording preserves the distinction between restored marginal coverage and competence, including the documented degradation when inferred context selects calibrators on CORe50.

### Geometry-MMALS G1

Source: `https://github.com/gharbonnier78/geometry-mmalls-g1/blob/main/README.md`

Atlas wording preserves the mixed result: bounded support for context geometry/non-arbitrary structure, failure of the smooth-residual route to qualify against R1, and no promotion of mature host-specialization/memory-transport/operational-superiority claims.

### ED-POMDP

Source: `https://github.com/gharbonnier78/ed-pomdp/blob/main/README.md`

Atlas status is intentionally `negative`: Step 2 left `CLM-VOI-001` unsupported and the broad form of `CLM-EQ-001` unsupported. The Theory and Claim Reset remains visible rather than replacing the failed claims with a positive narrative.

### Siamese Embedding Compression Lab

Primary outcome source: `https://github.com/gharbonnier78/siamese-embedding-compression-lab/blob/main/STUDY0_FINAL_REPORT.md`

Atlas status is intentionally `negative`: Study 0 does not demonstrate non-inferiority of the tested 128D compression routes and does not demonstrate added value of Siamese supervision over matched controls. The corrected uncertainty analysis is part of the outcome.

## Implementation artifacts

- `data/repository-outcomes.json` — structured system of record for the public atlas.
- `research/repositories/index.html` — browser surface.
- `assets/js/repository-atlas.js` — filter/render layer.
- `assets/css/repository-atlas.css` — responsive presentation.
- `scripts/check_repository_atlas.py` — structural and high-risk status guard.

## Verification contract

Replay:

```bash
python scripts/prepare_pages.py
python scripts/check_render_contract.py
python scripts/check_internal_links.py
python scripts/check_notation_registry.py
python scripts/check_release_consistency.py
python scripts/check_concept_audit.py
python scripts/check_repository_atlas.py
```

The atlas checker validates structure, status vocabulary, evidence-class discipline for evidence-bearing statuses, direct GitHub quick links, required high-risk outcomes, and the explicit publication exclusion.

It does not prove that every external link remains reachable forever, and it does not independently reproduce the scientific experiments in the source repositories.

## Human-understanding / visual review

A human visual review SHOULD confirm:

- the search and filters are usable on desktop and mobile;
- negative outcomes are visually distinguishable and not hidden;
- `Outcome`, `Paper/Report`, `Evidence`, `Live tool` and `GitHub` links are understandable;
- long outcome statements remain readable on a phone;
- the atlas feels like an evidence index rather than a marketing portfolio.

## Next admissible action

1. Open PR with direct immutable review navigation.
2. Run the full Diderot CI including `check_repository_atlas.py`.
3. Correct structural/link findings if any.
4. Merge only after CI is green.
5. Verify GitHub Pages deployment.
6. Perform human visual review on the published atlas; record any UX corrections separately without rewriting the scientific outcome sources.
