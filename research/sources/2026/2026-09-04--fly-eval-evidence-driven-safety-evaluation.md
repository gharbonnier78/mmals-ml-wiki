---
title: "FLY-EVAL++: An Evidence-Driven Evaluation Protocol for Safety-Constrained Flight Prediction with Large Language Models"
canonical_url: "https://arxiv.org/abs/2609.04021"
author_or_publisher: "Yalun Wu et al."
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: "AI testing / safety-critical evaluation"
reviewed_at: "2026-09-05"
source_type: "COLM 2026 conference paper"
relevance: "high"
evidence_quality: "high"
related_tracks: ["Diderot", "Test Authority", "AI testing", "systems engineering"]
related_concepts: ["deterministic verification", "constraint satisfaction", "multi-step rollout", "physics-grounded evaluation"]
retention_verdict: "retain"
---

# Source note

## Central contribution

FLY-EVAL++ evaluates LLM flight predictions using deterministic checks for protocol compliance, physical feasibility and safety constraints rather than accuracy alone, then aggregates these checks into interpretable multidimensional scores.

## What the source actually provides

Published at COLM 2026. The protocol extends PilotBench with history-conditioned and multi-step flight trajectory/attitude prediction. Across 66 LLMs, models with comparable predictive performance differ by more than 28 points in safety score. The study reports recurrent failures where numerically plausible predictions violate safety constraints or become unstable over multi-step rollouts.

## Limitations and uncertainty

The protocol is domain-specific and depends on available physical/operational constraints. A fixed rubric can omit unknown hazards. Results do not imply that every safety-critical AI system can be reduced to deterministic checks.

## Consequence for current work

Source-derived fact: predictive accuracy can conceal large differences in constraint compliance and rollout safety. Reviewer inference: Test Authority and Diderot should treat correctness, physical/operational validity and safety as separate evidence dimensions, with deterministic checks preferred whenever the governing rule is machine-verifiable.

## Follow-up

Map current Test Authority evidence types to an analogous multidimensional structure: task outcome, constraint satisfaction, structured validity, rollout stability, and residual uncertainty.

## Provenance note

The protocol and reported safety-score separation are source-derived. The proposed Test Authority mapping is reviewer inference.
