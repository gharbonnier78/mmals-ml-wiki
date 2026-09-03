---
title: "Coverage, Not Targeting: A Structural Regime in Multi-Turn Agent Credit Assignment"
canonical_url: "https://arxiv.org/abs/2609.02417"
author_or_publisher: "Chenyu Zhou, Qiliang Jiang, Shuning Wu, Xu Zhou"
publication_date: "2026-09-02"
discovered_via: "MMALS daily web research watch"
alert_topic: "agentic evaluation / credit assignment / evidence coverage"
reviewed_at: "2026-09-03"
source_type: "arXiv preprint"
relevance: "P0/P1"
evidence_quality: "medium-high preprint: controlled shared-rollout comparisons, matched controls, preregistered seeds and independent replication"
related_tracks: ["Diderot ML", "Test Authority", "MMALS"]
related_concepts: ["credit assignment", "verifier information density", "evidence coverage", "agentic RL", "test oracle"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper argues that multi-turn credit assignment should first be treated as an **evidence-coverage** problem, not a targeting problem. It introduces verifier information density V_d = k/C: the fraction of the causal chain for which the verifier actually exposes per-turn correctness.

## What the source actually provides

Source-derived facts: on tau^2-bench, controlled shared-rollout comparisons show that spreading a dense reward over the chain can outperform sparse terminal outcome rewards, while concentrating equivalent reward on selected progress turns or random turns can be harmful. The paper reports that terminal-state verification exposes only a final-write turn in 98% of rollouts while successful behavior requires 5–8 prerequisite calls. It reports low measured V_d on tau^2-bench and BFCL V3, a synthetic crossover near high coverage, preregistered multi-seed results on ToolACE-2-8B, an independent replication, and a matched-budget breadth sweep. It proposes a matched-concentration shuffled control for testing targeting claims.

## Limitations and uncertainty

The central structural quantity is new and tested on a limited benchmark family. Reward redistribution that works for training does not directly tell us how to design production evidence. A synthetic phase boundary should not be treated as a universal threshold. Dense intermediate signals can also encode evaluator bias or reward shaping mistakes.

## Consequence for current work

Reviewer inference: this strengthens the Test Authority/Diderot rule that a final verdict is weak evidence when the decisive causal chain is mostly unobserved. For agentic qualification, observability and oracle placement should be designed to cover prerequisite transitions, not only end state. For MMALS experiments, failure localization claims should clear a coverage baseline before sophisticated causal attribution is added.

## Follow-up

Add verifier-information-density and a shuffled-targeting control to agentic test-harness experiments; compare final-state-only, uniformly distributed deterministic checks, and targeted per-step checks under equal verification budget.

## Provenance note

The definition of V_d, experiments and reported thresholds/results are source-derived. Applying the result to Test Authority evidence design and MMALS failure localization is reviewer inference.