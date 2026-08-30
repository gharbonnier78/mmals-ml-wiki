---
title: "Replicable Conformal Prediction"
canonical_url: "https://arxiv.org/abs/2608.23638"
author_or_publisher: "Marios Papamichalis; Regina Ruane; Theofanis Papamichalis"
publication_date: "2026-08-23"
discovered_via: "Daily research watch / arXiv"
alert_topic: "MMALS conformal calibration"
reviewed_at: "2026-08-26"
source_type: "arXiv preprint"
relevance: "very high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Diderot", "Test Authority"]
related_concepts: ["conformal prediction", "replicability", "multi-site calibration", "auditability", "gaming resistance"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper studies when independently calibrated conformal procedures can yield the same deployed prediction rule, and quantifies the price of reproducibility in set size and calibration sample requirements.

## What the source actually provides

It proves impossibility results for perfect agreement under unrestricted independent calibration, then proposes shared-seed threshold rounding on a common grid. The construction preserves conformal coverage while making independently produced classifiers identical with user-controlled probability. Matching lower bounds characterize unavoidable cost. Experiments use ImageNet outputs, a four-hospital site split, and four language-model families. The paper also shows that replicability limits gaming by repeated recalibration/selection that can silently induce undercoverage in standard CP.

## Limitations and uncertainty

This is a preprint and focuses on threshold-based conformal procedures. Replicability does not imply conditional validity, robustness to distribution shift, or correctness of the underlying model. Coarser grids can reduce efficiency.

## Consequence for current work

Reviewer inference: MMALS-CAL should treat reproducibility/auditability across sites or reruns as a separate qualification axis from nominal coverage. This is particularly relevant for release evidence, cached decisions, and cross-site qualification in engineering governance.

## Follow-up

Add a CAL reproducibility test: independent calibration splits / sites -> compare deployed decision sets, coverage, set size and calibration cost; then assess whether controlled threshold discretization materially improves auditability without unacceptable efficiency loss.

## Provenance note

The mathematical and empirical claims are source-derived. The proposed MMALS/Test Authority qualification axis is reviewer inference.
