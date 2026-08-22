---
title: "Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation"
canonical_url: "https://arxiv.org/abs/2608.20316"
author_or_publisher: "Adam Fisch et al."
publication_date: "2026-08-20"
discovered_via: "Daily web/arXiv watch"
alert_topic: "MMALS routing"
reviewed_at: "2026-08-22"
source_type: "arXiv preprint"
relevance: "High"
evidence_quality: "Medium-high"
related_tracks: ["MMALS", "Diderot ML"]
related_concepts: ["routing", "value of information", "specialist selection", "cost-aware inference"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper formulates routing among heterogeneous specialists as a Pandora's Box problem in which better estimates of specialist value are themselves costly. It derives value-of-information rules for deciding whether the expected gain from refining a routing estimate justifies that extra cost.

## What the source actually provides

Source-derived facts: the authors develop centralized and decentralized routing policies under a Gaussian signal model and evaluate them across a multi-LLM benchmark, retrieval-augmented specialists, and variable test-time reasoning. The reported centralized policy matches exhaustive-estimation routing quality while invoking expensive value estimators less often. The decentralized variant can become strategically distorted when estimates of competitors are noisy.

## Limitations and uncertainty

The theoretical assumptions are stylized, the work is not yet peer-reviewed, and the evaluated specialists are predefined rather than autonomously discovered latent contexts. Performance gains do not establish that the underlying contexts are meaningful or causal.

## Consequence for current work

Reviewer inference: MMALS should distinguish uncertainty about a route from the expected value of spending more computation to resolve that uncertainty. A useful baseline is a two-stage router: cheap geometric/context score first, then a more expensive competence estimator only when the expected downstream gain exceeds its cost. This can also serve as a falsification test against always-on sophisticated routing.

## Follow-up

Add a cost-aware routing ablation comparing: cheap router only; exhaustive expert evaluation; and value-of-information-gated refinement, while measuring task gain, route regret, compute cost, and abstention.

## Provenance note

Claims about the method and reported experiments are source-derived. The mapping to MMALS host routing and the proposed ablation are reviewer inference.
