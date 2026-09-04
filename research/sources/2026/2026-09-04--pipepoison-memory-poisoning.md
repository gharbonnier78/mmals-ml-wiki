---
title: "Transferable End-to-End Optimization for Indirect Long-Term Memory Poisoning in LLM Agents"
canonical_url: "https://arxiv.org/abs/2609.00523"
author_or_publisher: "Chuanchao Zang et al."
publication_date: "2026-09-01"
discovered_via: "Daily research watch"
alert_topic: "agent memory security"
reviewed_at: "2026-09-04"
source_type: "arXiv preprint"
relevance: "High"
evidence_quality: "Medium-high"
related_tracks: ["MMALS", "Chronicle", "agentic systems", "AI testing"]
related_concepts: ["persistent memory", "memory poisoning", "write-retrieve-use pipeline", "stage coupling"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Treats indirect long-term memory poisoning as an end-to-end problem across memory writing, retrieval, and utilization rather than as three separable attack surfaces. PipePoison optimizes against the full chain and identifies stage bottlenecks.

## What the source actually provides

Source-derived facts: the authors evaluate across three agent frameworks and four memory mechanisms. They report a 19.1 percentage-point improvement in attack utilization rate over baselines and a 16-point advantage on fully unseen victim configurations, with effectiveness persisting under eight representative defenses. The attack uses local shadow systems, per-stage feedback, chain-structured losses, and stability-calibrated weighting.

## Limitations and uncertainty

This is a fresh preprint, not peer reviewed. Reported transferability remains limited to the tested frameworks, memory mechanisms, attack model, and defenses. Security conclusions concern LLM-agent memory pipelines and should not be generalized directly to all MMALS functional memory. Attack effectiveness also depends on the adversary being able to place content that enters the memory pipeline.

## Consequence for current work

Reviewer inference: Chronicle safety should be tested end-to-end across admission/write, transformation, retention, retrieval/exposure, and actual downstream use. A stage that appears robust in isolation may become the weak link after upstream transformations. The security test matrix should therefore include cross-stage attack propagation and not only per-stage controls.

## Follow-up

Add a Chronicle threat-model experiment that injects adversarial evidence before write-time transformation and measures survival through write, retention, retrieval, and action. Compare stage-local defenses with end-to-end controls.

## Provenance note

Performance claims and tested configurations above are source-derived. Mapping the attack pipeline to Chronicle admission/retention/exposure controls is reviewer inference.
