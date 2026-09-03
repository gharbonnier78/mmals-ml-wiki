---
title: "Modeling What Changes: Sparse, Residual World Models for Object-Centric Manipulation"
canonical_url: "https://arxiv.org/abs/2609.02046"
author_or_publisher: "Param Thakkar, Parsika Paresh Shah, Manisha Sushant Gote"
publication_date: "2026-09-02"
discovered_via: "MMALS daily web research watch"
alert_topic: "world models / residual learning / robotics"
reviewed_at: "2026-09-03"
source_type: "arXiv preprint"
relevance: "P0/P1"
evidence_quality: "medium-high preprint: controlled MuJoCo study, parameter-efficiency comparisons, rollout and planner tests; no real-robot evidence yet"
related_tracks: ["MMALS", "Diderot ML", "Robotics"]
related_concepts: ["residual world model", "change gate", "engineering prior", "sparse dynamics", "object-centric prediction"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper tests a deliberately simple inductive bias: predict only what changes instead of reconstructing the entire next state. A per-object gate identifies changing objects and a residual head predicts only their state deltas.

## What the source actually provides

Source-derived facts: on a MuJoCo tabletop-pushing benchmark from 3 to 8 objects, the sparse/residual model reports 2.5–4.6× lower next-state pose error than a dense MLP with 8.6–11.1× fewer parameters. Change-detection F1 remains 0.80–0.87, zero-retraining transfer across object counts retains 99.4% of F1, and about 90% of full-data accuracy is reached with one quarter of the data. Autoregressive rollouts drift less. Inside a sampling planner, prediction-only models fail; after training on planner-visited states, the sparse model reaches 0.23±0.06 task success over three seeds while the dense baseline remains at zero. The authors state that code/data/checkpoints will be released on publication.

## Limitations and uncertainty

This is a synthetic object-centric domain with explicit object states and a known notion of change. Planning success remains low in absolute terms. The strongest comparisons are against a dense MLP rather than a broad family of structured dynamics models. Real-world robustness and observation uncertainty are not yet demonstrated.

## Consequence for current work

Reviewer inference: this is unusually aligned with the MMALS principle of combining known stable structure with learned residuals. It supports a baseline in which stable regime/state components are preserved and adaptation capacity is spent only on detected change, before introducing a richer universal world model.

## Follow-up

Add a residual-dynamics baseline to the MMALS/world-model experiment ladder: predict full state vs stable-state + learned delta, with explicit measurement of compute, data efficiency, compounding rollout error and failure when the change detector misses a true transition.

## Provenance note

Reported numerical results and method details are source-derived. The engineering-prior/MMALS mapping is reviewer inference.