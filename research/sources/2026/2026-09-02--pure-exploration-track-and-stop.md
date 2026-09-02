---
title: "Solving pure exploration tasks in bandit models and beyond"
canonical_url: "https://webtv.univ-lille.fr/video/13393/solving-pure-exploration-tasks-in-bandit-models-and-beyond"
author_or_publisher: "Émilie Kaufmann / Université de Lille / Inria / CNRS"
publication_date: "2025-02-25"
discovered_via: "French-speaking science & mathematics discovery watch"
alert_topic: "pure exploration; bandits; sample complexity; MDP"
reviewed_at: "2026-09-02"
source_type: "university research lecture / pedagogical source"
relevance: "high as learning dependency"
evidence_quality: "high for orientation; primary papers required for formal claims"
related_tracks: ["MMALS", "GO-ED-POMDP", "Scientific chapter"]
related_concepts: ["pure exploration", "best-arm identification", "Track-and-Stop", "Top Two", "sample complexity", "MDP exploration"]
retention_verdict: "retain"
---

# Source note

## Central contribution

This Université de Lille/CRIStAL lecture provides a compact learning path from fixed-confidence pure-exploration bandits to Track-and-Stop, lower-bound-driven sample allocation, computationally cheaper Top Two methods, and extensions to exploration in Markov decision processes.

## What the source actually provides

Source-derived facts: Kaufmann presents pure exploration as learning a target property of unknown arm distributions using as few samples as possible, describes Track-and-Stop as attaining minimal asymptotic sample complexity in the small-error regime, motivates Top Two algorithms as computationally more attractive alternatives with near-optimal guarantees, and closes with exploration questions in MDPs. The primary Track-and-Stop result is Garivier & Kaufmann, COLT 2016; later Top Two theory is developed in peer-reviewed work including Jourdan et al., NeurIPS 2022.

Reviewer inference: this is directly useful for the MMALS question of when to spend an experiment to distinguish candidate regimes or hosts, especially when the objective is identification/certification rather than cumulative reward.

## Limitations and uncertainty

The lecture is pedagogical rather than a new research result and should not itself be used as canonical mathematical evidence. Classical best-arm assumptions can be much simpler than non-stationary latent-context continual learning. Treating hosts/regimes as fixed arms can be invalid when actions change the state or when the candidate set itself evolves.

## Consequence for current work

The scientific pathway should explicitly distinguish reward-maximizing bandits from pure-exploration/best-identification problems. For MMALS, use Track-and-Stop/Top-Two ideas as formal baselines for bounded exploratory probes before inventing an ad hoc VoI controller.

## Follow-up

Flag for the weekly Scientific chapter: derive the fixed-confidence best-arm objective, information-theoretic lower-bound intuition, Track-and-Stop allocation/stopping, then connect carefully to regime identification and active experimentation in POMDP/MDP settings.

## Provenance note

Lecture content and cited algorithmic positioning are source-derived and cross-checked against the primary Track-and-Stop and Top Two literature. The mapping to MMALS probes and the weekly chapter recommendation are reviewer inference.
