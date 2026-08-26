---
title: "Harness Continual Learning: Continual Adaptation Beyond Model Parameters"
canonical_url: "https://arxiv.org/abs/2608.19013"
author_or_publisher: "Borui Kang et al."
publication_date: "2026-08-21"
discovered_via: "Daily research watch / arXiv catch-up"
alert_topic: "MMALS / Diderot harness evolution"
reviewed_at: "2026-08-26"
source_type: "arXiv preprint"
relevance: "very high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Diderot", "agentic systems", "scientific harness"]
related_concepts: ["harness continual learning", "capability map", "adaptive router", "guarded evolution", "retention budget", "proposal-evaluation-commit"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper shifts continual learning from model parameters to the mutable execution harness around a frozen foundation model. It formalizes Task Interface, Experience Memory, Capability Map and Adaptive Router as the learning state, then governs updates through propose -> evaluate -> commit with explicit historical-retention and validity constraints.

## What the source actually provides

The authors evaluate harness evolution across textual reasoning, multimodal perception and open-world interaction. They report capability accumulation and failure recovery, but also measurable harness-level forgetting. Historical-retention budgets alter the adaptation/retention operating point, and more permissive updates do not necessarily yield a stronger final harness.

## Limitations and uncertainty

This is a fresh preprint. The notion of harness is broad and may bundle multiple causal mechanisms, making attribution difficult without component ablations. Benchmarks do not establish industrial safety or long-term autonomous self-improvement.

## Consequence for current work

Reviewer inference: this strongly supports treating Diderot/MMALS governance artifacts, memory, routing and capability registries as versioned adaptive state subject to retention tests, rather than regarding only model weights as the continual-learning object. It also independently supports the existing scientific-harness principle that changes must be proposed, evaluated against current plus historical evidence, then committed.

## Follow-up

Compare MMALS adaptation channels separately: model/host update, Chronicle update, capability-map update and router update. Require a retention budget and historical replay/evidence gate before accepting any persistent harness change.

## Provenance note

The harness decomposition and evaluation claims are source-derived. Mapping them onto Diderot/MMALS governance is reviewer inference.
