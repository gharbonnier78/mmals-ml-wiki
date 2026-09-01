# Startup record — belief, sufficiency and adaptive planning pathway

Recorded: 2026-09-01

```yaml
harness_ref: e80097fe8eb88c9e9340732683710ba1dc2ae008
manifest: harness-adoption.yaml
task_id: DIDEROT-BELIEF-SUFF-ADAPT-20260901
authoritative_sources:
  - Kaelbling, Littman & Cassandra (1998), Planning and Acting in Partially Observable Stochastic Domains
  - Littman, Sutton & Singh (2001), Predictive Representations of State
  - gharbonnier78/ed-pomdp pinned research artifacts where directly linked from existing Diderot pages
current_gates:
  - Diderot changes are pedagogical/derived views and must not become new scientific evidence
  - no F2 result may be taught as established because Toy F2 is preregistered but not yet qualified/reviewed
  - new non-trivial notation must be checked against the canonical notation registry and remain draft until reviewed
  - interactive claims must have a browser-level executable smoke path in addition to static/link checks
intended_action: >-
  Build a no-jump pathway from hidden state and belief through policy/value, epistemic action,
  value of information, delayed outcomes, contingent planning and query-relative sufficiency;
  add a small deterministic interactive teaching lab; preserve source/evidence boundaries; and
  make the published interaction executable by automated browser steps that mirror a human user.
missing_context:
  - public immutable release of the separate world-model Toy A/F v0.1.5 evidence package
  - independent review of the preregistered Toy F2 protocol
```

## Why this step exists

The existing Diderot dynamic-systems pathway already contains POMDP, belief state, sufficient state and planning, but it jumps too quickly from a current belief to generic planning. Recent project work exposed several missing intermediate distinctions: an action is not a policy; more certainty need not change a decision; information may have value only because it changes a later branch; the best outcome may be delayed; and reproducing the current action is weaker than preserving the ability to continue adaptive decision-making.

These are useful pedagogical refinements even if the separate research programme later changes its hypotheses. Diderot must therefore teach the established POMDP/decision-theoretic concepts from authoritative literature and label the project-specific `contingent sufficiency` wording as a research refinement rather than a field definition.

## Permitted mutations

- add or revise Diderot concept pages, pathway pages and pedagogical labs;
- add source notes and draft notation encounters;
- add browser-execution validation and proportional public-site engineering documentation;
- update navigation/index surfaces needed to expose the new teaching path.

## Prohibited inference

This work must not claim that:

- MMALS is a world model;
- GO-ED-POMDP is established as superior to simpler decision policies;
- next-observation prediction is generally insufficient;
- belief state is always the minimal useful representation;
- a successful deterministic teaching toy establishes a new scientific result;
- global non-regression can be proven from a finite sentinel set.

## Exact next admissible action

Create the source notes and pedagogical concept/pathway/lab changes against the pinned harness. Run static validators and the new browser-level smoke test. Then open one reviewable PR with immutable navigation links and request independent review before merge.
