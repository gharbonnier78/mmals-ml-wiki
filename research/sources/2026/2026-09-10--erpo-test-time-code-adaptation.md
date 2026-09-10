---
title: "Entropy-Regularized Rank-Masked Policy Optimization for Test-Time Reinforcement Learning in Code Generation"
canonical_url: "https://arxiv.org/abs/2609.09135"
author_or_publisher: "Jiacheng Xu, Feng Chen, Xiuneng Xu, Bo An"
publication_date: "2026-09-08"
discovered_via: "Daily research watch"
alert_topic: "test-time adaptation and AI testing"
reviewed_at: "2026-09-10"
source_type: "EMNLP 2026 Main / arXiv"
relevance: "P0/P1 — evidence-guided adaptation, AI testing, conservative updates"
evidence_quality: "high-medium: accepted conference paper with multi-benchmark evaluation"
related_tracks: ["MMALS", "Diderot scientific harness", "AI testing"]
related_concepts: ["test-time reinforcement learning", "behavioral probes", "consensus reward", "reward hacking", "conservative adaptation"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper adapts code generators at test time without canonical answers by creating output-free probe inputs, executing candidate programs, and deriving a behavioral consensus reward. Because that reward is explicitly acknowledged as an imperfect verifier, ERPO uses rank masking and an entropy ceiling to make negative updates conservative and limit policy drift.

## What the source actually provides

Source-derived facts: Probe Consensus Reward compares candidate program behavior on generated probes rather than source-text similarity. The authors note that consensus can be spurious and reward-hacked. ERPO converts low consensus into conservative negative updates and constrains drift with entropy regularization. The paper reports substantial pass@1 and pass@k improvements in both in-domain adaptation and zero-shot transfer and is accepted to EMNLP 2026 Main.

## Limitations and uncertainty

Behavioral agreement is not correctness. Candidate programs can share the same bug, weak probes can miss discriminating cases, and the method still depends on the quality and diversity of generated probes. Improvement on code benchmarks does not establish safe online learning in broader systems.

## Consequence for current work

Reviewer inference: the useful design principle for MMALS is not the specific RL algorithm but the explicit separation between a cheap, imperfect evidence signal and a conservative adaptation policy that knows the verifier can be wrong. This maps naturally to evidence-weighted updates where low-authority evidence may suggest adaptation but cannot justify large irreversible changes.

## Follow-up

Add an imperfect-verifier experiment to MMALS: vary verifier false-positive/false-negative rates and compare unconstrained updates, evidence-weighted updates, and bounded conservative updates. Measure both adaptation gain and irreversible regression.

## Provenance note

Method and benchmark claims are source-derived. The evidence-authority and MMALS adaptation mapping are reviewer inference.