---
title: "Predictive Representations of State"
canonical_url: "https://proceedings.neurips.cc/paper_files/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html"
author_or_publisher: "Michael L. Littman, Richard S. Sutton, Satinder Singh"
publication_date: "2001"
source_type: "NeurIPS conference paper"
reviewed_at: "2026-09-01"
relevance: "P0"
evidence_quality: "high for predictive-state representation framing"
related_tracks: ["machine learning foundations", "world-model research"]
related_concepts: ["predictive state representation", "state", "action-conditioned prediction", "sufficiency"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Littman, Sutton and Singh show that the state of a controlled stochastic system can be represented by multi-step action-conditional predictions of future observations rather than only by a named latent-state distribution. Their linear predictive-state construction provides a direct bridge between state representation and predictions grounded in observable experience.

## What the source supports for Diderot

Source-derived concepts used in this teaching path:

- `state` need not be synonymous with the original hidden-state coordinates;
- predictions about future observable tests can form a state representation;
- action-conditioned, multi-step predictions are materially different from a single next-observation forecast;
- the usefulness of a representation depends on whether it preserves the system information needed for future prediction/control tasks.

## Boundary

This source does not establish that any learned next-observation predictor is automatically a sufficient predictive state, nor that predictive-state coordinates are always easier to learn in practice. It also does not establish the project-specific finite-horizon `contingent sufficiency` criterion.

## Pedagogical consequence

Diderot should keep three objects separate: the hidden state used by a POMDP model, the belief distribution over that state, and a predictive-state coordinate system expressed through future observable tests. The teaching lab may compare them, but must not silently present an exact predictive transform as a learned empirical discovery.
