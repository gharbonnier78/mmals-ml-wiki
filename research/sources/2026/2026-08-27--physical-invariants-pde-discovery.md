---
title: "What Should a Large Language Model See? Physical Invariants as a Data Representation for PDE Discovery"
canonical_url: "https://arxiv.org/abs/2608.25189"
author_or_publisher: "Fan Yang, Matt Thomson"
publication_date: "2026-08-26"
discovered_via: "arXiv daily watch"
alert_topic: "engineering priors / scientific ML / MMALS"
reviewed_at: "2026-08-27"
source_type: "arXiv preprint"
relevance: "very high"
evidence_quality: "medium"
related_tracks: ["MMALS", "Diderot", "ML foundations", "systems engineering"]
related_concepts: ["engineering priors", "physical invariants", "representation design", "PDE discovery"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Introduces a data-interpretation stage that converts raw spatiotemporal fields into physically meaningful measured quantities before presenting them to an LLM for equation discovery, instead of asking the model to infer useful physical structure from raw fields indirectly.

## What the source actually provides

Source-derived facts: on the authors' simulated-field benchmark, giving interpreted physical quantities to the model nearly triples recovered-equation accuracy relative to showing raw data, at negligible computational cost and without model training.

## Limitations and uncertainty

Six-page fresh preprint; evidence appears limited to simulated fields and the exact benchmark breadth is modest. The result does not establish that all physically engineered representations outperform learned representations, nor that the chosen invariants are always sufficient.

## Consequence for current work

Reviewer inference: this is unusually close to the active MMALS principle "do not spend learning capacity rediscovering stable engineering knowledge." It supports testing expert-provided sufficient statistics/invariants as a prior representation, while reserving continual learning for residual uncertainty, violations of the prior, and new regimes.

## Follow-up

Add an MMALS baseline in which known engineering descriptors/invariants are given directly to the router and compare against raw learned embeddings and hybrid prior+residual representations. Track performance, sample efficiency, prior violations discovered, and lost novelty.

## Provenance note

The benchmark claim is source-derived. The engineering-prior interpretation and proposed MMALS ablation are reviewer inference.
