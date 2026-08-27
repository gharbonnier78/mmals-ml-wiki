---
title: "Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules"
canonical_url: "https://arxiv.org/abs/2608.25551"
author_or_publisher: "Liviu Aolaritei, Lucas Lévy, Francis Bach, Michael I. Jordan"
publication_date: "2026-08-26"
discovered_via: "arXiv daily watch"
alert_topic: "MMALS / sequential evidence / adaptive computation"
reviewed_at: "2026-08-27"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Diderot", "ML foundations"]
related_concepts: ["adaptive stopping", "confidence sequences", "value of computation", "sequential evidence"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Constructs time-uniform, trajectory-adaptive confidence sequences for strongly convex stochastic optimization so an SGD run can stop when a target accuracy is certified, rather than at a preselected worst-case horizon.

## What the source actually provides

Source-derived facts: the paper derives observable confidence sequences for last-iterate distance and weighted-average suboptimality, proves time-uniform validity with near-optimal 1/t decay up to iterated-log factors, extends the approach to minibatch SGD, and reports numerical experiments in which certified adaptive stopping needs orders of magnitude fewer iterations than natural deterministic horizons.

## Limitations and uncertainty

The theory is for strongly convex stochastic optimization and does not directly certify arbitrary MMALS routing, host selection, or exploration policies. It is a fresh preprint, not yet peer reviewed.

## Consequence for current work

Reviewer inference: this is a strong mathematical analogue for MMALS's emerging question "when is more computation or experimentation still worth paying for?" It suggests replacing fixed reasoning/learning budgets with time-uniform evidence processes that stop once the decision-relevant uncertainty is sufficiently resolved. This is complementary to value-of-information routing: VoI decides whether to continue; confidence sequences can help make the stopping rule statistically defensible.

## Follow-up

Design a toy MMALS experiment comparing fixed exploration budgets against an anytime-valid stopping rule on a controlled host-selection problem, measuring regret, compute, and false early stops.

## Provenance note

Claims about SGD guarantees and numerical savings are source-derived. Application to MMALS exploration and routing is reviewer inference and requires a separate derivation and experiment.
