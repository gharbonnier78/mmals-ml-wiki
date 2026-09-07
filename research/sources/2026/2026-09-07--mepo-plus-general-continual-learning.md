---
title: "MePo++: Unifying Representation Refinement and Reconciliation for General Continual Learning"
canonical_url: "https://arxiv.org/abs/2609.05075"
author_or_publisher: "Guanglong Sun et al."
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: ""
reviewed_at: "2026-09-07"
source_type: "arXiv preprint with public code"
relevance: "Very high: task-free/general continual learning"
evidence_quality: "Medium-high"
related_tracks: ["MMALS", "continual learning", "representation learning"]
related_concepts: ["general continual learning", "representation refinement", "representation reconciliation", "pretrained geometry"]
retention_verdict: "retain"
---

# Source note

## Central contribution

MePo++ targets general continual learning without task identities, explicit boundaries, or replay access to past data. It separates two problems: making pretrained representations more plastic before online adaptation and reconciling evolving online features with a stable pretrained geometry during the stream.

## What the source actually provides

Source-derived facts: MetaPrep performs unsupervised meta-refinement on pseudo-continual sequences; StreamAlign aligns evolving representations to a stable pretrained geometry. The authors report consistent gains across multiple pretrained models, datasets and continual-learning baselines, and release code at https://github.com/SunGL001/MePo_Plus.

## Limitations and uncertainty

The current evidence is preprint-level and the abstract does not establish that the preserved pretrained geometry corresponds to semantically correct latent regimes. Better average continual-learning performance does not by itself validate inferred-context routing or memory semantics.

## Consequence for current work

Reviewer inference: this is a strong direct baseline for MMALS because it attacks plasticity/stability in task-free streams without explicit regime discovery. MMALS should beat or complement this simpler representation-reconciliation strategy before claiming value from a more elaborate router/host architecture.

## Follow-up

Benchmark MMALS against MePo++-style representation reconciliation under identical no-task-boundary streams, including ablations for regime discovery, routing, and memory.

## Provenance note

Architecture, setting, public-code availability and reported cross-benchmark consistency are source-derived. The proposed baseline role for MMALS is reviewer inference.