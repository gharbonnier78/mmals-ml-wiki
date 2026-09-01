---
title: "Unifying Detection and Adaptation in Task-Free Continual Learning"
canonical_url: "https://arxiv.org/abs/2608.27070"
author_or_publisher: "Dezheng Han, Anbang Zhang, Zhihao Zhu, Shuaishuai Guo"
publication_date: "2026-08-27"
discovered_via: "Web research"
alert_topic: "MMALS inferred-context continual learning"
reviewed_at: "2026-09-01"
source_type: "arXiv preprint; accepted to Findings of EMNLP 2026"
relevance: "P0"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "continual learning", "geometry-aware routing"]
related_concepts: ["task-free continual learning", "Fisher information", "K-FAC", "subspace routing", "LoRA", "reuse-expand-new"]
retention_verdict: "retain"
---

# Source note

## Central contribution

FiUni jointly performs latent task detection and parameter-efficient continual adaptation without explicit task boundaries. It represents each incoming batch through principal subspaces derived from a K-FAC approximation to the Fisher information matrix, then compares those subspaces with historical ones to choose among reusing an existing adaptation, expanding a related subspace, or creating a new one.

## What the source actually provides

Source-derived facts: the method uses Fisher/K-FAC principal subspaces as a task-similarity representation and constrains low-rank adaptation to frozen Fisher-guided bases. The paper reports experiments in standard, long-sequence and task-free continual-learning settings, with competitive performance against task-aware or advanced CL baselines while using fewer trainable parameters. The paper is listed as accepted to Findings of EMNLP 2026.

## Limitations and uncertainty

The inferred context is batch-level and is derived from model sensitivity geometry, not from a demonstrated causal regime variable. Reuse/expand/new decisions depend on similarity thresholds and the stability of Fisher-subspace estimates. The evaluation does not establish that Fisher geometry is the minimal or best regime detector compared with simpler drift, density, prototype or engineering-rule baselines.

## Consequence for current work

Reviewer inference: FiUni is a particularly strong comparator for MMALS G2 because it makes the latent-context decision explicit and geometrically grounded while remaining substantially simpler than a learned manifold/router stack. A defensible MMALS experiment should compare engineering-known routing, simple drift/prototype detection, Fisher-subspace routing, and any richer geometry-aware router under identical replay and forgetting tests.

## Follow-up

Implement a small synthetic regime benchmark where ground-truth regime boundaries are hidden, then compare `reuse / expand / new-host` decisions using oracle labels, simple statistics/prototypes, and Fisher-subspace overlap. Measure regime-detection accuracy, routing regret, forgetting, and false regime births.

## Provenance note

Claims about the FiUni method and reported evaluation come from the source. The proposed MMALS comparator and falsification experiment are reviewer inference.
