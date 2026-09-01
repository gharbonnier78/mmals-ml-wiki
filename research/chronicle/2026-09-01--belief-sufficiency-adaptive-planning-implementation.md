# Implementation state — belief, sufficiency and adaptive planning pathway

Recorded: 2026-09-01

Harness: `gharbonnier78/scientific-research-harness@e80097fe8eb88c9e9340732683710ba1dc2ae008`

Task: `DIDEROT-BELIEF-SUFF-ADAPT-20260901`

## What changed

The startup record identified a pedagogical jump between `belief state` and generic `planning`. This branch fills that gap without promoting the separate world-model/Toy F2 research hypothesis into established evidence.

Added or expanded:

- source notes for classical POMDP planning and predictive-state representations;
- concept pages for policy, finite-horizon value/action value, epistemic action, value of information, contingent policy, receding-horizon replanning, predictive-state representation, decision regret, contingent sufficiency, belief/model/memory separation, and bounded non-regression evidence;
- expanded belief-state, sufficient-state and planning pages;
- a 14-step no-jump pathway from hidden state to adaptive decision sufficiency;
- a deterministic three-part teaching lab for belief update, certainty-vs-decision, and identical one-step values with different contingent multi-step choices;
- canonical notation-registry entries for `b_t`, `π`, `H`, `γ`, `V_H^π`, `Q_H^π` and project-local `R_H`;
- graph/catalog integration for the new concepts;
- an explicit `MVP` engineering-care profile for the public interactive site;
- a Playwright/Chromium browser smoke that operates the public controls and navigation like a user instead of testing only hidden helper functions.

## Scientific and pedagogical boundary

The browser lab is deterministic pedagogical mechanism evidence only. It is not Toy F2 qualification, does not extend `WM-H03`, does not establish a world-model definition, and does not establish that next-observation prediction is generally insufficient.

`contingent sufficiency` remains a project-local hypothesis. The public page explicitly says it must be compared against state abstraction, bisimulation and predictive-state literature before broader terminology is used.

The notation entries are `draft`; agent creation does not promote them to reviewed/stable.

## Notation migration provenance

Because the connected GitHub interface used for this branch exposes whole-file replacement but not line patches, the seven notation records were applied by a one-time idempotent branch workflow. The workflow first validated the resulting canonical registry, committed only `mathematics/notation/registry.json`, and was then removed together with its one-time helper. The surviving canonical source remains the single `registry.json`; no parallel registry was created.

Generated registry commit: `dc119ccb82a307986e32602e5272de9eee8b695d`.

This implementation detail is provenance, not scientific evidence.

## Verification contract

Static PR checks must still pass:

```text
python scripts/prepare_pages.py
python scripts/check_render_contract.py
python scripts/check_internal_links.py
python scripts/check_notation_registry.py
python scripts/check_release_consistency.py
python scripts/check_concept_audit.py
python scripts/check_repository_atlas.py
```

The new browser check additionally runs:

```text
python -m pip install -r requirements-browser.txt
python -m playwright install chromium
python tests/browser/run_belief_adaptive_planning_browser.py
```

CI uses `--with-deps chromium` on the hosted runner.

## Current gate

`IMPLEMENTED / REVIEW PENDING`.

No pedagogical entry added in this branch is promoted to reviewed/stable by this implementation step. The branch must pass automated checks and then receive independent review against the pinned harness before merge.

## Exact next admissible action

Open the Diderot pull request, let both static and browser workflows execute on the exact head, repair any implementation defect without weakening scientific/pedagogical boundaries, then hand the immutable PR/head/harness URLs to the independent reviewer.
