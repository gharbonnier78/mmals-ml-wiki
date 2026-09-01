---
title: "A Calibration Audit of Confidence in Feed-Forward 3D Reconstruction"
canonical_url: "https://arxiv.org/abs/2608.29705"
author_or_publisher: "Nanxing Nick Deng, Qing Cheng, Niclas Zeller, Daniel Cremers"
publication_date: "2026-08-30"
discovered_via: "Web research"
alert_topic: "MMALS CAL / uncertainty audit"
reviewed_at: "2026-09-01"
source_type: "arXiv preprint"
relevance: "P0/P1"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "CAL", "robotics", "3D perception"]
related_concepts: ["confidence calibration", "risk ranking", "coverage", "out-of-distribution reliability"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper audits whether per-pixel confidence emitted by feed-forward 3D reconstruction models can legitimately be interpreted as uncertainty. Its key contribution is diagnostic: a score trained as a loss weight may rank errors usefully while still being badly miscalibrated as a reliability magnitude.

## What the source actually provides

Source-derived facts: seven released 3D reconstruction backbones are evaluated on thirteen datasets using four properties: error ranking, average level calibration, calibration across the confidence range, and interval coverage. The reported confidence often ranks error well but underestimates uncertainty outside the exact training conditions; the median discrepancy reported across the seven models is about 2.4x, with larger error prediction mismatch at high confidence.

## Limitations and uncertainty

This is a fresh preprint in a specific computer-vision domain. The confidence outputs are model-specific and are not conformal prediction sets. The results establish a reliability failure mode, not a universal numerical correction factor.

## Consequence for current work

Reviewer inference: MMALS should never equate a router score, similarity, margin, or learned confidence with calibrated uncertainty merely because it correlates with errors. CAL evaluation should separately test ranking utility, calibration level, conditional/worst-regime behavior, and coverage/decision risk.

## Follow-up

Add a calibration-audit template to MMALS experiments: rank correlation with error, reliability curve/level error, worst-regime calibration, and conformal coverage where applicable. Compare the raw router confidence with calibrated and conformalized decision layers.

## Provenance note

The seven-model/thirteen-dataset audit and reported miscalibration are source-derived. The mapping to MMALS router/CAL diagnostics is reviewer inference.
