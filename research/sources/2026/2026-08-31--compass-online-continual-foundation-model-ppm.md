---
title: "Efficient Online Continual Foundation Model Fine-Tuning for Predictive Process Monitoring"
canonical_url: "https://arxiv.org/abs/2608.28237"
author_or_publisher: "Sjoerd van Straten; Marwan Hassani"
publication_date: "2026-08-28"
discovered_via: "Daily research watch / arXiv"
alert_topic: "task-free continual learning; drift detection; adaptive subspaces"
reviewed_at: "2026-08-31"
source_type: "arXiv preprint"
relevance: "very high"
evidence_quality: "medium-high preprint: task-free/task-aware experiments over nine event streams with multiple backbones"
related_tracks: ["MMALS", "continual-learning", "process-mining", "Diderot-ML"]
related_concepts: ["concept-drift", "task-boundary-inference", "adaptive-subspace", "recurrent-drift", "foundation-model-finetuning"]
retention_verdict: "retain"
---

# Source note

## Central contribution

COMPASS addresses online continual fine-tuning of foundation models under concept drift. It adapts loss-plateau drift detection to autonomously infer task boundaries in event streams and maintains a unified knowledge subspace combining pretrained and task-specific directions.

## What the source actually provides

Source-derived facts: the framework is evaluated on nine synthetic and real event streams, in both task-free and task-aware settings, with multiple backbones and consistent hyperparameter tuning across methods. The authors compare against three state-of-the-art non-foundation-model competitors and two update-strategy baselines, reporting particularly strong gains for recurrent drift and long-running complex cases, with additional computational overhead.

## Limitations and uncertainty

This is a fresh preprint and the claim of being the first such framework is author-reported. Loss plateaus are only an indirect drift signal and may confuse optimization dynamics with environmental regime changes. Process-monitoring event streams also provide a more structured setting than general MMALS inferred-context learning. The unified subspace is not evidence that discovered boundaries are semantically or causally correct.

## Consequence for current work

Reviewer inference: COMPASS is a strong external baseline for the exact MMALS question of whether useful regime boundaries can emerge from operational evidence rather than labels. The most important comparison is not architectural similarity but boundary quality: oracle context versus loss-plateau inferred context versus geometry/support-based context, evaluated on routing regret, recurrent-regime recognition and unnecessary host creation.

## Follow-up

Implement a simple loss-plateau/drift-trigger boundary baseline in the inferred-context experiment before introducing more sophisticated geometric partitioning. Test specifically whether recurrent regimes are recognized as recurrence rather than spawned as new hosts.

## Provenance note

The framework description, datasets, comparison setup and reported performance pattern are source-derived. Mapping it to MMALS regime-boundary inference and the proposed comparator suite is reviewer inference.