---
title: "SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting"
canonical_url: "https://arxiv.org/abs/2608.26829"
author_or_publisher: "Haizhao Fan; Xinyi Le / arXiv"
publication_date: "2026-08-27"
discovered_via: "Daily web/arXiv watch"
alert_topic: "MMALS engineering priors; representation"
reviewed_at: "2026-08-29"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium"
related_tracks: ["MMALS", "machine-learning-foundations", "Diderot"]
related_concepts: ["engineering priors", "semantic descriptors", "residual learning", "time-series forecasting"]
retention_verdict: "retain"
---

# Source note

## Central contribution

SAGE injects variable-specific semantic descriptions and statistical descriptors into a time-series forecasting model, while using CLIP visual alignment only during training so no LLM is required in the inference loop. The paper reports state-of-the-art accuracy across eight long-term forecasting benchmarks and M4, with ablations supporting complementary contributions from the multimodal alignment and variable-level knowledge.

## What the source actually provides

Source-derived facts: the method jointly models temporal, cross-variable, textual and visual information; uses frequency-enhanced patches and variable tokens; adds gated residual paths for descriptions and statistical descriptors; freezes the CLIP vision encoder and uses it through a training-only contrastive objective; evaluates across eight long-term benchmarks plus M4; and reports ablations for the main components.

Reviewer inference: this is useful evidence for testing whether stable domain knowledge should be exposed directly to a learner instead of forcing a model to rediscover it from raw observations.

## Limitations and uncertainty

This is a 10-page preprint with no peer-review status reported on arXiv. The evidence is forecasting-specific, and the descriptors are hand-provided. Strong results therefore do not establish that engineering priors will improve latent-context discovery generally. Injected descriptors can also encode wrong or incomplete assumptions and reduce plasticity if treated as hard constraints.

## Consequence for current work

For MMALS, add a falsification baseline comparing: raw learned context; engineered invariant/descriptor context; and engineered descriptors plus learned residual features. This directly tests the hypothesis that learning capacity should be spent on residual uncertainty rather than rediscovering stable engineering structure.

## Follow-up

Reproduce the simplest descriptor-vs-raw ablation on a controlled MMALS stream where some regime variables are known and some are intentionally hidden. Measure performance, routing regret, novelty detection and recovery when an engineering descriptor becomes invalid.

## Provenance note

Claims about SAGE architecture, benchmarks and reported performance are source-derived. The proposed MMALS baseline and interpretation as an engineering-prior experiment are reviewer inference.