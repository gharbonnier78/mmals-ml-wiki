---
title: "Beyond Residuals: Energy based solutions of partial differential equations using scientific machine learning"
canonical_url: "https://arxiv.org/abs/2609.08239"
author_or_publisher: "Timon Rabczuk; Yizheng Wang"
publication_date: "2026-09-08"
discovered_via: "Daily research watch"
alert_topic: "ML foundations / physics-informed learning"
reviewed_at: "2026-09-09"
source_type: "arXiv technical analysis"
relevance: "Medium-high learning dependency for physics-informed ML and engineering priors"
evidence_quality: "Medium-high preprint synthesis plus numerical examples"
related_tracks: ["Diderot", "machine learning foundations", "systems engineering"]
related_concepts: ["variational principles", "physics-informed learning", "PINNs", "Deep Energy Method", "engineering priors"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper systematically contrasts residual-based physics-informed neural networks with the Deep Energy Method (DEM), which solves classes of PDE problems by minimizing an energy or incremental-potential functional when the governing equations admit a variational formulation. The contribution is useful less as a new universal architecture than as a reminder that known mathematical structure can change the learning objective itself.

## What the source actually provides

Source-derived facts: DEM is positioned as an alternative to strong-form and weak-form residual minimization for variational PDEs. The paper argues that direct energy minimization can avoid residual-weight tuning and high-order derivatives while enabling physical constraints to enter through the variational structure. It discusses extensions through incremental variational formulations to nonlinear, history-dependent and time-dependent problems, including phase-field fracture and dissipative systems, and provides numerical examples comparing the approach with residual-based physics-informed methods.

## Limitations and uncertainty

The method is applicable only when an appropriate variational/energy formulation exists and is computationally tractable. The paper should not be read as evidence that energy objectives dominate PINNs generally. Numerical examples do not establish broad superiority across all PDE classes, discretizations, optimization regimes or noisy inverse problems.

## Consequence for current work

Reviewer inference: this strengthens the Diderot/MMALS principle that a learner should not re-infer structure already encoded reliably by mathematics or engineering knowledge. The strongest prior may sometimes be neither an input feature nor a regularizer, but the formulation of the admissible objective itself. This is a useful counterweight to prematurely introducing generic world-model or neural machinery.

## Follow-up

Flag for the Scientific chapter track as a pedagogical bridge: PDE -> variational principle -> optimization objective -> learned approximation. Use it to sharpen the taxonomy of ways engineering priors can enter ML: architecture, constraints, objective, simulator, initialization or residual model.

## Provenance note

Claims about DEM/PINN formulation and reported examples are source-derived. The mapping to MMALS and the engineering-prior taxonomy is reviewer inference.
