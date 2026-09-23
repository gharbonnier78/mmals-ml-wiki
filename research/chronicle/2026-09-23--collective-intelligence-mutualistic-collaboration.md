---
date: "2026-09-23"
event_type: "research-source-ingestion-and-experiment-design"
status: "draft / review required"
consumer_repo: "gharbonnier78/mmals-ml-wiki"
consumer_base: "0260f425621f57e339852cdbfab6ab9672ed5540"
working_branch: "research/collective-intelligence-human-ai-20260923"
harness_ref: "e80097fe8eb88c9e9340732683710ba1dc2ae008"
---

# Chronicle — collective intelligence, interaction cadence and mutualistic collaboration

## Trigger

User supplied photographs of *Pour la Science* n°597 (September 2026), pp. 15-23, article **“Intelligence collective : décide-t-on mieux à plusieurs ?”** by Mehdi Moussaïd and Guillaume Jacquemont, then explicitly authorized a pass over the cited primary publications and Diderot/MMALS capitalization.

## Harness startup

Loaded before outcome-bearing repository work:

- local manifest: `harness-adoption.yaml`;
- pinned harness: `gharbonnier78/scientific-research-harness@e80097fe8eb88c9e9340732683710ba1dc2ae008`;
- Diderot base used for this work: `main@0260f425621f57e339852cdbfab6ab9672ed5540`.

No scientific gate is released by this work.

## Important harness audit discovered before capitalization

The user challenged the statement that the harness already follows:

```text
explore independently
-> synchronize
-> explore independently
-> challenge
-> aggregate
```

The challenge was valid.

Live repository check on 2026-09-23 found:

- harness moving `main` HEAD = `e8e043c2b66a74ccacd023d67a32f989885449eb`;
- Diderot remains intentionally pinned to reviewed `e80097fe...`;
- harness PR #8 (`agent/reviewer-evidence-contract`) is open, draft, unmerged;
- harness PR #9 (`agent/scientific-interaction-phase0`) is open, unmerged.

The current normative `HARNESS.md` does **not** mandate independent pre-generation, intermittent synchronization or an aggregation phase.

PR #9 does propose useful independence protections — Reviewer must not optimize for agreement or rewrite the result, sessions return control after bounded actions, and fresh independent sessions are used for portability testing — but these are not merged normative rules and still do not instantiate the full repeated interaction cycle.

**Disposition:** previous wording that called the intermittent cycle "our harness" was too strong. Correct wording: it is a **candidate architecture partly anticipated by unmerged Phase 0 work and newly motivated by primary literature**.

## Primary publications checked

The working source pack records:

- Woolley et al., *Science* (2010), DOI 10.1126/science.1193147;
- Bates & Gupta, *Intelligence* (2017), DOI 10.1016/j.intell.2016.11.004;
- Riedl et al., *PNAS* (2021), DOI 10.1073/pnas.2005737118;
- Hong & Page, *PNAS* (2004), DOI 10.1073/pnas.0403723101;
- Bernstein, Shore & Lazer, *PNAS* (2018), DOI 10.1073/pnas.1802407115;
- Kurvers et al., *PNAS* (2016), DOI 10.1073/pnas.1601827113;
- Prelec, Seung & McCoy, *Nature* (2017), DOI 10.1038/nature21054;
- Zöller et al., *PNAS* (2025), DOI 10.1073/pnas.2426153122;
- Danús et al., *PNAS* (2026), DOI 10.1073/pnas.2511050123 as adjacent observational evidence.

## New research objects

Created on the working branch:

1. secondary source note for the supplied *Pour la Science* article;
2. primary-source pack with claim boundaries and counter-evidence;
3. synthesis **Collective intelligence for MMALS: independence, diversity, interaction timing and human-AI complementarity**;
4. candidate experiment **CI-MMALS-0** embedded in that synthesis.

## Main conceptual changes

### Preserved

- `M = Mutualistic` remains a **normative engineering hypothesis**, not a claim that biological or social collectives are universally mutualistic.
- independent review remains valuable for falsification even if it later fails to improve an aggregate benchmark.

### Added

- distinguish **nominal diversity** from **measured error complementarity**;
- distinguish reviewer-role separation from statistical/experimental independence;
- measure pairwise/shared error, unique-error recovery and diversity collapse;
- treat aggregation as part of the collective algorithm;
- test interaction cadence rather than assuming continuous debate or permanent isolation is optimal;
- require a minimum-sufficient-mechanism comparison so a complex reviewer loop can lose to a cheap independent ensemble.

## Candidate CI-MMALS-0 disposition

Status: `CANDIDATE / NOT EXECUTED`.

No preregistered dataset, frozen model roster, power/sample-size calculation or execution environment exists yet.

The synthesis explicitly defines the next review questions but does not authorize execution.

## Exact next admissible action

1. open a draft PR from this branch;
2. request independent source-fidelity and experimental-design review;
3. do not merge or promote to stable concept pages until the review is resolved;
4. separately consider a **bounded harness issue** documenting the gap between current reviewer independence and experimentally controlled interaction cadence — do not change normative `HARNESS.md` before evidence exists.
