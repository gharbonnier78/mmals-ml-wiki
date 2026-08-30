---
title: "SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation"
canonical_url: "https://arxiv.org/abs/2608.19425"
author_or_publisher: "Dijie Zhu, Seunghun Oh, Ruopeng Huang, Zhiyu Huang, Jiaqi Ma, Chen Tang"
publication_date: "2026-08-19"
discovered_via: "Daily research watch / arXiv"
alert_topic: "robotics, conformal calibration, testing"
reviewed_at: "2026-08-21"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS-CAL", "AI testing", "robotics", "Test Authority"]
related_concepts: ["scenario-conditioned evaluation", "sim-to-real", "conformal prediction", "deployment qualification"]
retention_verdict: "retain"
---

# Source note

## Central contribution

SCAPE estimates scenario-conditioned real-world policy performance from limited paired sim/real data plus large simulation runs, explicitly correcting simulation bias and conformally calibrating uncertainty.

## What the source actually provides

The paper evaluates autonomous driving and quadruped velocity tracking. Reported sim-to-sim scenario-level error reductions are 4.9%/34.7% for driving and 14.5%/27.7% for quadruped tracking relative to scene-conditioned neural and aggregate statistical baselines. It also reports a physical Unitree Go2 deployment, narrower calibrated intervals, improved sample efficiency and better OOD behavior.

## Limitations and uncertainty

This is a fresh preprint, not peer reviewed. Scenario variables are engineered/observable rather than autonomously inferred latent regimes. The abstract does not establish that conformal validity remains conditional on arbitrary learned context partitions.

## Consequence for current work

Source-derived: scenario-average qualification can hide deployment-local variation and SCAPE demonstrates a practical sim+real+conformal correction pattern. Reviewer inference: MMALS-CAL and Test Authority experiments should compare global qualification with context/scenario-conditioned qualification, but inferred-context conditioning must be independently validated rather than assumed valid.

## Follow-up

Add SCAPE as a reference baseline for a future experiment comparing global, oracle-context and inferred-context calibrated policy-performance estimates under sim-to-real shift.

## Provenance note

Facts above come from arXiv:2608.19425. The MMALS/Test Authority mapping is reviewer inference.