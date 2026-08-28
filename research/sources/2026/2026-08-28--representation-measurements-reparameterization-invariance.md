---
title: "Representation Measurements Under Function-Preserving Reparameterizations"
canonical_url: "https://arxiv.org/abs/2608.27020"
author_or_publisher: "Abdullah Karasan"
publication_date: "2026-08-27"
discovered_via: "Daily web/arXiv watch"
alert_topic: "geometry-aware representations"
reviewed_at: "2026-08-28"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "geometry", "ML foundations"]
related_concepts: ["representation invariance", "function-preserving reparameterization", "parallel analysis", "geometry qualification"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper argues that representation-derived measurements should be invariant to function-preserving coordinate changes, and shows that a common parallel-analysis procedure can violate this requirement.

## What the source actually provides

Source-derived facts: across five models, three retrieval domains and 75 transformations, the paper reports median component-count disagreement of 0.79 and fixed-threshold decision disagreement of 0.26 under function-preserving reparameterizations. A centering-only control changes 1,141/1,200 component counts despite an unchanged observed covariance spectrum, while orthogonally invariant comparator scores remain stable with similar held-out discrimination.

## Limitations and uncertainty

Single-author, fresh preprint; the result targets particular representation-measurement procedures rather than all geometry-aware diagnostics. It does not show which invariant metric is best for routing or continual learning.

## Consequence for current work

Reviewer inference: any MMALS geometry metric used to justify regime drift, dimensionality, host separation or routing should first pass a function-preserving reparameterization test. Coordinate-sensitive metrics can create apparent geometric change without any functional change in the model.

## Follow-up

Add a G2 falsification test: apply known orthogonal/permutation reparameterizations that preserve function, then verify whether proposed geometry diagnostics and routing decisions remain unchanged.

## Provenance note

Empirical figures and invariance claim are source-derived. The G2 test is reviewer inference.
