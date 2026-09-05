---
title: "Equivariance, Curvature and Symmetry in Functional Covariance Estimation"
canonical_url: "https://arxiv.org/abs/2609.03042"
author_or_publisher: "Jocelyn Nembe"
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: "geometry / statistical invariance"
reviewed_at: "2026-09-05"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Diderot", "geometry"]
related_concepts: ["equivariance", "curvature", "symmetry", "coordinate invariance", "representation diagnostics"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper separates population-level coordinate invariance from estimator-level equivariance and quantifies how nonlinear reparameterization curvature breaks exact commutation in local-linear covariance estimation.

## What the source actually provides

At population level, covariance operators are unitarily conjugate under diffeomorphic reparameterization. For the estimator, exact commutation holds universally iff the reparameterization is affine. For general smooth reparameterizations, the equivariance defect is controlled by normalized curvature. Finite-group symmetry is also analyzed as an orthogonal-projection regularizer, with a risk gain determined by anti-invariant estimation error minus symmetry misspecification rather than by group size alone.

## Limitations and uncertainty

This is a statistical-theory result for functional covariance estimation, not a direct theorem about neural latent spaces or routing. Practical value depends on whether the diagnostic being used has an analogous equivariance property.

## Consequence for current work

Source-derived fact: a population quantity can be geometrically invariant while its finite-sample estimator is not, and symmetry helps only when the assumed invariance is not badly misspecified. Reviewer inference: MMALS geometry diagnostics should be tested under function-preserving/coordinate-preserving transformations at the estimator level, not only justified conceptually at the representation level.

## Follow-up

Add an invariance stress test to G2 experiments: transform coordinates without changing task function and measure whether routing/geometry diagnostics remain stable within sampling error.

## Provenance note

The mathematical characterization is source-derived. The proposed G2 falsification test is reviewer inference.
