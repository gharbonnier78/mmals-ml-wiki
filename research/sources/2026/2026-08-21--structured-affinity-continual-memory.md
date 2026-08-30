---
title: "Structured Affinity for Unsupervised Visual Class-Incremental Memory in Deep Artificial Immune Networks"
canonical_url: "https://arxiv.org/abs/2608.20104"
author_or_publisher: "Siphesihle Sithungu"
publication_date: "2026-08-20"
discovered_via: "Daily research watch / arXiv"
alert_topic: "continual learning, geometry, memory"
reviewed_at: "2026-08-21"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium"
related_tracks: ["MMALS", "geometry-aware routing", "Chronicle"]
related_concepts: ["structured affinity", "replay-free memory", "latent reorganization", "response maps"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper studies replay-free visual class-incremental memory using structured, gradient-free affinities instead of flattened vector similarity. Its key claim is that preserving structured response maps allows the latent coordinate system to reorganize while older class structure remains recoverable.

## What the source actually provides

Experiments cover sklearn digits, MNIST, Fashion-MNIST and KMNIST. Scalar binding-profile variants underperform feature-map versions. Reported final balanced accuracy reaches 0.939 on sklearn digits with logistic-regression probes and 0.902 with 1-NN, with initial-class retention of 0.978; layer-wise scale calibration further improves some configurations.

## Limitations and uncertainty

Single-author fresh preprint, no peer review, and benchmarks are small relative to modern continual-learning standards. External probes establish recoverability, not necessarily autonomous context inference or functional host routing. Artificial-immune terminology should not be mistaken for biological validation.

## Consequence for current work

Source-derived: structured affinity can preserve useful representation structure better than scalarized affinity in this setting. Reviewer inference: MMALS should test whether routing/memory quality depends on preserving local structured response patterns rather than only centroids or flattened embeddings.

## Follow-up

Add one ablation comparing scalar prototype similarity against a structured local-affinity descriptor before considering any immune-network architecture.

## Provenance note

Facts come from arXiv:2608.20104. The proposed MMALS ablation is reviewer inference.