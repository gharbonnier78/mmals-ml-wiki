---
title: "Common-Center Geometry and Certified Radial Reconstruction for Energy-Form Full Conformal Regions"
canonical_url: "https://arxiv.org/abs/2608.24964"
author_or_publisher: "Yiheng Feng"
publication_date: "2026-08-26"
discovered_via: "arXiv daily watch"
alert_topic: "MMALS-CAL / conformal geometry"
reviewed_at: "2026-08-27"
source_type: "arXiv theoretical preprint with Lean 4 formalization"
relevance: "high"
evidence_quality: "medium-high theory"
related_tracks: ["MMALS", "geometry", "conformal calibration"]
related_concepts: ["full conformal prediction", "star-shaped regions", "geometric certification", "formal verification"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Characterizes the exact geometry of energy-form full conformal prediction regions and shows that under stated conditions the regions share a common center and can be star-shaped rather than convex. It also derives certified radial inner/outer reconstructions and provides a companion Lean 4 formalization.

## What the source actually provides

Source-derived facts: the paper proves score-specific geometric results for energy-form FullCP regions, including star-shapedness under symmetry/convexity conditions and certified radial envelopes using Lipschitz bounds. It explicitly targets low-dimensional multivariate outputs rather than high-dimensional scaling or runtime gains. A formalized audited release accompanies the paper.

## Limitations and uncertainty

Purely theoretical and low-dimensional in scope. It does not show that an MMALS latent competence region satisfies these assumptions, nor that exact FullCP is computationally appropriate for continual routing.

## Consequence for current work

Reviewer inference: this is valuable primarily as a warning against assuming that calibrated admissible regions must be balls, ellipsoids, or convex clusters. If MMALS later defines conformal competence regions, geometry should be treated as an empirical/theoretical object rather than imposed for convenience.

## Follow-up

Keep as a theory reference for CAL/G2. Do not implement yet; first establish whether non-convex or star-shaped competence regions arise in controlled MMALS experiments.

## Provenance note

The geometric theorems and scope limits are source-derived. The relevance to latent competence regions is reviewer inference.
