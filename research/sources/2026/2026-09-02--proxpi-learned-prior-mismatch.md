---
title: "ProxPI: Proximal Prior Injection for Sampling-Based MPC under Learned-Prior Mismatch"
canonical_url: "https://arxiv.org/abs/2609.00941"
author_or_publisher: "Euncheol Im, Myotaeg Lim, Yisoo Lee"
publication_date: "2026-09-01"
discovered_via: "Daily research watch / arXiv"
alert_topic: "robotics; engineering priors; robust adaptation"
reviewed_at: "2026-09-02"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "robotics", "GO-ED-POMDP"]
related_concepts: ["learned prior mismatch", "soft prior", "online correction", "exploration", "model predictive control"]
retention_verdict: "retain"
---

# Source note

## Central contribution

ProxPI studies how to use a learned policy prior inside sampling-based model predictive control without allowing a bad out-of-distribution prior to dominate online search. Instead of centering the sampler on the prior, it keeps nominal-centered exploration and injects the prior as a soft proximity cost.

## What the source actually provides

Source-derived facts: the authors provide a theoretical argument that repeatedly re-centering sampling on an inaccurate prior discards optimizer corrections and that increasing rollout budget does not remove this failure. They report simulations and real-robot experiments showing retained in-distribution performance while recovering toward vanilla MPPI-level behavior under prior mismatch.

Reviewer inference: this is a concrete analogue for MMALS's emerging `engineering prior + learned residual` principle: a prior can reduce search without being granted the authority to collapse the hypothesis/action space when evidence contradicts it.

## Limitations and uncertainty

The setting is sampling-based MPC, not continual learning. A soft proximity cost presumes a meaningful action-space distance to the prior. Real-robot evidence strengthens practicality but the abstract does not establish breadth across robot platforms or highly discontinuous regime changes.

## Consequence for current work

When injecting engineering knowledge into MMALS, prefer a design where prior structure biases search but residual evidence can move the system away from it. Compare hard constraints, prior-centered routing and soft-prior/residual routing under deliberate prior mismatch.

## Follow-up

Add a prior-mismatch stress test to the engineering-prior ablation: correct prior, partially wrong prior and structurally wrong prior; measure recovery time, regret and whether additional compute can compensate for a bad prior.

## Provenance note

The MPC mechanism, theoretical claim and reported evaluation types are source-derived. The MMALS prior/residual analogy and proposed stress test are reviewer inference.
