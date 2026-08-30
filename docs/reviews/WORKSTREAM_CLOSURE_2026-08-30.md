# Workstream closure — Dynamic systems, world models, Diderot and harness

**Date:** 2026-08-30  
**Scope:** the Diderot/MMALS dynamic-systems + world-model workstream, its independent Claude review, related Diderot cleanup, and the notation/harness dependency created during closure.

## 1. Scientific review record

The independent Claude review remains preserved verbatim as:

- `docs/reviews/CLAUDE_INDEPENDENT_WORLD_MODEL_REVIEW_2026-08-30.md`

Original reviewer verdict:

- scientific-semantic: `PARTIALLY ACCEPT`;
- source/provenance: `PARTIALLY ACCEPT`;
- pedagogical/navigation: `PARTIALLY ACCEPT`;
- reviewed-snapshot harness conformance: `NOT VERIFIED` / review-process-only;
- merge recommendation: `YES AFTER REQUIRED CHANGES`;
- human visual review: `YES WITH WARNINGS`.

The author disposition remains separate:

- `docs/reviews/CLAUDE_REVIEW_DISPOSITION_2026-08-30.md`

The historical verdict was not rewritten after fixes.

## 2. Diderot PRs resolved

### PR #7 — dynamic systems bridge for MMALS

**Disposition:** MERGED after review findings were dispositioned and structural CI was green.

Squash merge commit:

`ba1fab9864b179a00ad538fb9938b77bee33e27d`

Key closure changes included:

- GO-ED wording anchored to the actual ED-POMDP programme and explicitly marked tentative;
- durable 24 Aug 2026 chronicle event in `data/research-events.json`;
- bounded public provenance for historical MMALS toys;
- generated epistemic badges no longer hard-coded as foundational;
- consolidated program-level falsification conditions;
- Claude review and author disposition preserved separately.

### PR #8 — mathematical notation atlas and harness bootstraps

**Disposition:** MERGED after resolving conflicts against the reviewed PR #7 mainline and running the combined structural checks.

Squash merge commit:

`4fd739b12565cd9976bc8dcdac4f4e8141c37821`

This added:

- `harness-adoption.yaml`;
- `AGENTS.md` and `CLAUDE.md` bootstraps;
- notation registry, interactive atlas and A2 view;
- notation/harness structural check;
- harness meta-documentation.

This prospective adoption does **not** retroactively change Claude's correct finding that the PR #7 snapshot it reviewed did not itself contain harness-adoption artifacts.

### PR #4 — research triage before qualification

**Disposition:** MERGED after rebasing onto the current Diderot contracts and obtaining a green structural check.

Squash merge commit:

`b7631dd491c05a072b1ff21d2debb772a0acebb4`

The reusable distinction is preserved:

`exploratory screening != qualified evidence`

Screening may justify continue / stop / redirect, but cannot become qualification by reinterpretation.

### PR #2 — RL / MDP / decision-risk note

**Disposition:** CLOSED WITHOUT MERGE.

Reason: the branch predates the current reviewed concept/source-audit ontology. MDP/POMDP foundations now exist in the reviewed mainline, while the broader RL/risk note remains unique branch material. Closure is archival/deferred, not a scientific rejection. Any future reuse should migrate the unique content under the current source/epistemic-audit and harness contracts.

### PR #3 — change-impact regression evidence simulator

**Disposition:** CLOSED WITHOUT MERGE.

Reason: the executable lab/parity work remains unique and is preserved in branch history, but its concept/workflow integration predates the current audit and combined CI contracts. Future migration should preserve the parity fixture and falsification design while adding current concept audit/source provenance and integrating its parity check into present CI.

### PR #5 — accountable-human canonicalization concept

**Disposition:** CLOSED WITHOUT MERGE.

Reason: the concept remains valuable and its Tao-derived branch history is preserved, but the old concept-index snapshot predates the present audit/harness contracts. Future promotion should reintroduce it as an audited concept rather than merging the stale branch wholesale.

### PR #6 — Study-1 evaluation concepts

**Disposition:** CLOSED WITHOUT MERGE.

Reason: the Study-1 pedagogical pages and provenance remain preserved on the branch, but merging unchanged would introduce concept pages outside the current 59/59 source/epistemic-audit contract. Future capitalization should migrate them under the current contract.

At closure there are **no open pull requests in `gharbonnier78/mmals-ml-wiki`**.

## 3. MMALS program PR resolved

MMALS PR #1, `Program extension: minimal sufficient dynamic inference`, was merged as program/hypothesis documentation.

Squash merge commit:

`67b0280d74440288cdbdda86d20d093eafd08460`

The merge does not promote the extension to validated evidence and does not replace the current RC2I evidence line.

At closure there are **no open pull requests in `gharbonnier78/mmals`**.

## 4. Harness dependency resolved

The Diderot notation/harness adoption initially pinned the immutable head of scientific-research-harness PR #18 as a provisional dependency.

Harness PR #18 was then merged:

`13b26f717e66e36bb753f2885091d420a99ec878`

Diderot explicitly upgraded:

- `harness-adoption.yaml`;
- `AGENTS.md`;
- `CLAUDE.md`;
- `docs/harness-meta.md`;
- `docs/harness-meta/index.html`;

to this merged immutable ref.

The active adoption is therefore no longer a provisional PR-head pin.

Other open pull requests in `scientific-research-harness` belong to separate pre-existing research/method workstreams and were deliberately left untouched; “close the current workstream” is not interpreted as authorization to discard unrelated scientific work.

## 5. Structural validation and deployment

After the reviewed Diderot bridge and notation/harness integration, the combined CI covers:

- internal links;
- mathematical-notation registry / harness-bootstrap consistency;
- release consistency;
- concept source/epistemic audit consistency.

The latest checked Diderot mainline run for these combined checks completed successfully before this closure note was added. GitHub Pages deployment on the reviewed mainline also completed successfully.

This structural success is not scientific validation.

## 6. Human-review boundary

No separate human visual/understanding review is invented by this closure.

The user explicitly authorized workstream closure and merge after the independent review findings were addressed. That is merge authorization; it is **not** recorded as evidence that an accountable human independently completed every visual or understanding item from Claude's review.

Diderot therefore preserves both facts:

1. the scientific/epistemic review and its dispositions are complete enough for the merged documentation scope;
2. any later canonical promotion that specifically requires a formal accountable-human understanding gate must still record that gate explicitly rather than inferring it from merge history.

## 7. Closed-state handoff

Current canonical entry points:

- Diderot: `https://github.com/gharbonnier78/mmals-ml-wiki`
- Diderot Pages: `https://gharbonnier78.github.io/mmals-ml-wiki/`
- MMALS: `https://github.com/gharbonnier78/mmals`
- Scientific research harness: `https://github.com/gharbonnier78/scientific-research-harness`
- active harness ref: `13b26f717e66e36bb753f2885091d420a99ec878`

The next dynamic/world-model scientific action should be a new explicitly framed experiment or publication workstream, not an implicit continuation of the closed PR sequence.
