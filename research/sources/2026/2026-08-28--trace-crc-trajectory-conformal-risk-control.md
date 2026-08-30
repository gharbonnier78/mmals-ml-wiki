---
title: "TRACE-CRC: Trajectory-Adaptive Conformal Risk Control for Multi-Step Channel State Information Prediction"
canonical_url: "https://arxiv.org/abs/2608.27124"
author_or_publisher: "Kiarash Rezaei, Mehdi Sattari, Javad Aliakbari, Tommy Svensson, Paolo Monti, Carlos Natalino"
publication_date: "2026-08-27"
discovered_via: "Daily web/arXiv watch"
alert_topic: "safe conformal calibration"
reviewed_at: "2026-08-28"
source_type: "PMLR conference paper / arXiv"
relevance: "high"
evidence_quality: "high"
related_tracks: ["MMALS", "Diderot", "AI testing"]
related_concepts: ["conformal risk control", "trajectory-level coverage", "multi-step uncertainty", "learn-then-test"]
retention_verdict: "retain"
---

# Source note

## Central contribution

TRACE-CRC calibrates uncertainty at the trajectory level for multi-step prediction, controlling the risk that at least one future frame is uncovered rather than treating each step independently.

## What the source actually provides

Source-derived facts: the method builds Frobenius-norm uncertainty balls, combines horizon-dependent error profiling, trajectory-difficulty stratification and learn-then-test risk control, and reports reliable trajectory-level coverage with smaller uncertainty regions than conservative multi-step corrections while avoiding undercoverage of compact stepwise/adaptive baselines. The paper is published in PMLR volume 329 (COPA 2026).

## Limitations and uncertainty

The application is wireless channel-state prediction, where temporal trajectories and error geometry are explicit. This does not directly establish validity for MMALS latent contexts or arbitrary multi-stage agent decisions.

## Consequence for current work

Reviewer inference: MMALS-CAL should distinguish per-step/per-host calibration from end-to-end trajectory risk. A useful baseline is to compare independent stepwise guarantees, conservative union-style correction, and direct trajectory-level risk control for routing-plus-host-plus-action sequences.

## Follow-up

Design a small synthetic MMALS trajectory benchmark where one failure anywhere in a multi-step route invalidates the final outcome; compare stepwise CP against trajectory-level CRC.

## Provenance note

Facts above are from the arXiv abstract and publication metadata. The proposed MMALS experiment is reviewer inference.
