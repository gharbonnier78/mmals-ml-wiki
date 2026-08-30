---
title: "Beyond Scaling: Self-Evolving LLM Agents for Hardware Kernel Optimization via an Experience-Driven Workflow and Experience Graph Memory"
canonical_url: "https://arxiv.org/abs/2608.25570"
author_or_publisher: "Siyuan Chen et al."
publication_date: "2026-08-26"
discovered_via: "arXiv daily watch"
alert_topic: "MMALS / Chronicle / agentic engineering"
reviewed_at: "2026-08-27"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Diderot", "AI testing", "agentic systems"]
related_concepts: ["experience graph memory", "external continual learning", "execution feedback", "fixed model"]
retention_verdict: "retain"
---

# Source note

## Central contribution

KOPE treats completed optimization runs as durable external experience rather than repeatedly solving each task from scratch. It stores decisions, execution feedback, ordering, and alternative branches in an Experience Graph Memory while keeping the foundation model fixed.

## What the source actually provides

Source-derived facts: under the reported GLM-5.2 setting, KOPE reaches a geometric-mean per-operator speedup 1.54x that of the strongest competing baseline. In a 53-operator ablation, Active Context Management and Injection raises pass rate from 60.0% to 84.6% and reduces token use from 15.9B to 1.113B versus passive context construction. Enabling Experience Graph Memory raises full-suite pass rate from 55.2% to 84.6% and yields a 1.43x geometric-mean speedup on valid timing comparisons.

## Limitations and uncertainty

Fresh preprint; kernel optimization provides unusually objective correctness/performance feedback and may be easier than domains with delayed or ambiguous outcomes. The reported memory gains bundle graph representation, retrieval, active context management, and workflow design.

## Consequence for current work

Reviewer inference: this supports a Chronicle design in which experience is not merely a bag of retrieved episodes but an evidence graph linking action, observed consequence, successor decision, and alternatives. It also strengthens the hypothesis that meaningful continual improvement can occur outside model weights.

## Follow-up

Use KOPE as a comparator when defining Chronicle schema: test flat episodic memory versus graph-structured decision-outcome memory under a fixed retrieval/token budget, with downstream task success rather than recall as the primary metric.

## Provenance note

All numeric improvements and architecture descriptions are source-derived. The proposed Chronicle schema and MMALS interpretation are reviewer inference.
