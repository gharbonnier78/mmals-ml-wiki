---
title: "FailureSpot: Label-Efficient Timestamp-Level Failure Detection for Vision-Language-Action Models"
canonical_url: "https://arxiv.org/abs/2609.04277"
author_or_publisher: "Jie Ma, Zongxi Liu, Yi Zhu"
publication_date: "2026-09-03"
discovered_via: "arXiv daily watch"
alert_topic: "robotics / AI testing"
reviewed_at: "2026-09-08"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium"
related_tracks: ["MMALS", "Diderot", "Test Authority", "robotics"]
related_concepts: ["failure localization", "weak supervision", "active learning", "trajectory diagnostics", "VLA"]
retention_verdict: "retain"
---

# Source note

## Central contribution

FailureSpot argues that trajectory-level success/failure labels are too coarse for proactive failure detection because they mark normal pre-failure behavior as failed. It instead builds timestamp-level supervision from action-derived weak signals and spends dense human annotation only on uncertain trajectories selected by active learning.

## What the source actually provides

Source-derived facts: weak supervision is derived from action abnormalities including inconsistent consecutive chunks, frozen/idle actions and aggressive random motions. Active learning selects uncertain trajectories for timestamp-level annotation, after which the detector is fine-tuned. Experiments across multiple VLA policies report improvements at both timestamp and trajectory level.

## Limitations and uncertainty

The abstract does not establish that detected action anomalies are causal precursors rather than correlated symptoms. Weak labels embed assumptions about what failure looks like and may miss semantically wrong but smooth behavior. No claim should be transferred directly from VLA manipulation to general software/agent systems without domain-specific evidence.

## Consequence for current work

Reviewer inference: this directly supports the Test Authority/Diderot distinction between `episode failed` and `where/when evidence first became inconsistent`. For MMALS, failure-localized adaptation should be compared with trajectory-wide adaptation. It also suggests that scarce expert review should be allocated to high-uncertainty traces rather than uniformly labeling complete runs.

## Follow-up

Introduce a timestamp/step-level failure-localization metric into agent/robotics evaluation and test whether localized adaptation reduces collateral forgetting versus updating from whole-episode labels. Compare weak heuristics, model-derived anomaly scores and human-verified timestamps.

## Provenance note

Method and reported experimental direction are source-derived. The mapping to evidence-localized adaptation and Test Authority practice is reviewer inference.
