---
title: "More Data Cannot Break a Symmetry: Identifiability by Design"
canonical_url: "https://arxiv.org/abs/2608.27651"
author_or_publisher: "Jing Xu; Christopher Kanan"
publication_date: "2026-08-27"
discovered_via: "Daily research watch / arXiv"
alert_topic: "representation geometry; identifiability; symmetry"
reviewed_at: "2026-08-31"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high preprint: structural argument plus controlled experiments across 93 representations"
related_tracks: ["MMALS-G2", "Diderot-ML", "experimental-design"]
related_concepts: ["identifiability", "symmetry", "automorphism", "representation-alignment", "experimental-design"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper shows that unsupervised representation alignment can be structurally non-identifiable because symmetries of the stimulus geometry permit multiple equally valid correspondences. More observations or more solver restarts do not resolve a symmetry that is present by design; the remedy is to change the experimental design so that the ambiguity is broken before learning.

## What the source actually provides

Source-derived facts: in the color setting, increasing restart budget by 64x does not solve a symmetric design while an asymmetric design at the same sample count does. Across 3,000 subsets, ability to discriminate representational models and ability to recover correspondence are essentially uncorrelated (reported r=-0.02). Selecting nine colors using the proposed diagnostic, without consulting learned representations, reduces catastrophic alignment failures from 75% to 2% across 93 model representations while keeping models, layers, sample count and solver fixed.

## Limitations and uncertainty

This is a fresh preprint and the strongest demonstrations use settings where candidate geometries and symmetry structure are sufficiently explicit. The result does not imply that all latent-context ambiguity is group-theoretic, nor that every identifiability problem can be solved by simple asymmetry injection. Direct transfer to high-dimensional learned competence spaces must be tested.

## Consequence for current work

Reviewer inference: G2 should add an identifiability gate before learning a geometric router. If two regimes/actions are observationally symmetric under the chosen probes, no amount of additional data from the same design can guarantee recovery of the intended partition. The correct response may be an active experiment or probe that breaks the symmetry, not a more complex metric learner.

## Follow-up

Add a synthetic symmetry case to the MMALS geometry benchmark: construct two latent regimes that are indistinguishable under the default observations, verify router non-identifiability, then add one engineered diagnostic probe and measure whether the partition becomes recoverable. This should precede manifold/curvature complexity.

## Provenance note

Claims about structural ambiguity, restart behavior, correlations and failure-rate reduction are source-derived. The proposed MMALS identifiability gate and active-probe experiment are reviewer inference.