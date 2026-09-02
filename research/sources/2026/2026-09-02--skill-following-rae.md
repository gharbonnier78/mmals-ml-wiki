---
title: "Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents"
canonical_url: "https://arxiv.org/abs/2609.00549"
author_or_publisher: "Seonghyeon Cho, Chanjun Park"
publication_date: "2026-09-01"
discovered_via: "Daily research watch / arXiv"
alert_topic: "retrieval; agent skills; causal evaluation"
reviewed_at: "2026-09-02"
source_type: "peer-reviewed conference paper / arXiv preprint (EMNLP 2026 Findings)"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Chronicle", "Diderot", "agentic systems"]
related_concepts: ["retrieval utility", "counterfactual evaluation", "memory use", "same-task ablation"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper argues that aggregate retrieval lift does not establish that retrieved skills help on the tasks where they are actually invoked. It introduces Retrieval-Invoked Actual-Use Effect (RAE), a matched same-task comparison between skill-enabled and skill-disabled runs restricted to tasks on which retrieval occurred.

## What the source actually provides

Source-derived facts: the paper is accepted to EMNLP 2026 Findings and evaluates 17 LLMs over coding and mathematical domains. It reports cases where aggregate retrieval metrics are positive while RAE is negative; on MBPP+, several models that appear to benefit overall are harmed on the exact tasks where retrieval is invoked.

Reviewer inference: this is a clean evaluation pattern for Chronicle, retrieval tools and engineering priors: measure the conditional causal effect of using the retrieved artifact, not merely system-level averages.

## Limitations and uncertainty

Conditioning on retrieval can itself reflect a policy-selected subset and does not replace randomized intervention where feasible. The benchmark domains are narrow, and skill retrieval is not equivalent to persistent continual-learning memory. The metric identifies harmful actual use but does not by itself explain why the retrieved skill was harmful.

## Consequence for current work

For Chronicle and Diderot retrieval, add a matched `use vs no-use` counterfactual on the same episode whenever practical. Report both aggregate lift and conditional actual-use effect. A positive global score must not be interpreted as evidence that retrieval is beneficial where the router chooses to invoke it.

## Follow-up

Implement an RAE-like metric for Chronicle episodes and for Diderot source/tool retrieval, including rescued outcomes, induced regressions and confidence intervals.

## Provenance note

The RAE definition, evaluated model count and qualitative negative-RAE finding are source-derived. Applying the design to Chronicle/Diderot is reviewer inference.
