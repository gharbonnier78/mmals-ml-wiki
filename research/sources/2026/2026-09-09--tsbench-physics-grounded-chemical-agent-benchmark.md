---
title: "TSBench: A physics-grounded benchmark for evaluating LLM understanding of chemical reaction mechanisms"
canonical_url: "https://arxiv.org/abs/2609.08503"
author_or_publisher: "Xiaohu Xu; Tong Zhu"
publication_date: "2026-09-08"
discovered_via: "Daily research watch"
alert_topic: "AI testing / scientific agents"
reviewed_at: "2026-09-09"
source_type: "arXiv benchmark paper"
relevance: "High for Diderot scientific harness and agent qualification"
evidence_quality: "Medium-high preprint evidence"
related_tracks: ["Diderot", "Test Authority", "agentic systems"]
related_concepts: ["deterministic verification", "physics-grounded evaluation", "mechanism-level validation", "iterative repair"]
retention_verdict: "retain"
---

# Source note

## Central contribution

TSBench evaluates whether LLM agents can construct physically valid three-dimensional transition-state guesses for elementary chemical reactions, using structure-editing tools and an automated quantum-chemistry pipeline rather than text-only judging. The central methodological contribution is a benchmark in which an apparently plausible local answer must also satisfy a mechanistic, physics-grounded end-to-end criterion.

## What the source actually provides

Source-derived facts: the benchmark reports 546 evaluations across seven frontier LLMs and 78 elementary reactions. A diagnosis-driven revision loop increases aggregate success from 50.4% to 66.8%. The strongest models approach 90% on the simplest reactions, while performance falls sharply with mechanistic complexity. A major reported failure mode is that agents often propose locally plausible saddle points whose computed reaction paths connect the wrong reactant-product pair.

The verification authority is not an LLM judge alone: candidate structures are passed through an automated quantum-chemical pipeline that yields a physics-grounded pass/fail verdict.

## Limitations and uncertainty

The work is a preprint and the benchmark is specialized to reaction-mechanism construction. Seventy-eight reactions cannot establish general scientific-agent competence. Quantum-chemical verification itself depends on modeling choices and numerical approximations. Improvement after diagnosis-driven revision does not isolate which part of the loop creates the gain.

## Consequence for current work

Reviewer inference: this is strong external support for separating local plausibility from end-to-end mechanistic validity in Diderot and Test Authority evaluation. An agent can satisfy superficial or intermediate checks while still violating the global causal/mechanistic objective. Where an executable scientific or engineering verifier exists, it should outrank generic model judging.

The pattern is directly reusable as: proposed artifact -> deterministic/domain verifier -> failure localization -> bounded revision -> re-verification.

## Follow-up

Map TSBench's evaluation decomposition to the Diderot scientific harness and identify one internal experiment where an LLM-generated result can be checked by a deterministic or model-based engineering oracle rather than semantic similarity.

## Provenance note

Numerical benchmark results and failure descriptions above are source-derived. The proposed Diderot/Test Authority application is reviewer inference and does not imply that chemistry-specific results transfer quantitatively to software or systems engineering.
