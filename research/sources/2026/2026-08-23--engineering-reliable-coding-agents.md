---
title: "Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model"
canonical_url: "https://arxiv.org/abs/2608.13867"
author_or_publisher: "Stephanie Jarmak"
publication_date: "2026-08-14"
discovered_via: "Daily web watch / Thoughtworks cross-check"
alert_topic: "agent reliability; harness engineering; evaluation"
reviewed_at: "2026-08-23"
source_type: "technical review and engineering monograph / arXiv"
relevance: "high"
evidence_quality: "medium-high: structured multivocal review plus operational protocols; evidence strength varies by topic"
related_tracks: ["Diderot", "AI testing", "agentic systems", "Test Authority", "scientific-research-harness"]
related_concepts: ["harness reliability", "execution-state management", "permissions", "observability", "fault injection", "system-level evaluation"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The monograph argues that coding-agent reliability is a property of the whole deployed system, not only of the model: task construction, execution environment, retrieval, durable state, permissions, review interfaces, observability, recovery and resource allocation form a dependency chain. Failures or weak evidence at an upstream layer can invalidate conclusions downstream.

## What the source actually provides

Source-derived: the review reports synthesis of 164 scholarly works, 100 practitioner records, 29 benchmark records and 17 author-system case records. It contributes a versioned catalog of 206 reliability records, runnable evaluation/reliability protocols, and explicit procedures including evaluation comparison, failure-trace review, authority-boundary tests, allocation-policy replay and recovery fault injection.

## Limitations and uncertainty

This is a single-author engineering synthesis, not a peer-reviewed controlled study. Evidence quality varies substantially across the catalog; practitioner records and author-system cases cannot carry the same weight as replicated experiments. The breadth of the monograph also makes selective adoption essential.

## Consequence for current work

Reviewer inference: this strongly supports the Diderot/Test Authority principle that agent evaluation must qualify the harness and execution system around the LLM. It independently reinforces Thoughtworks Radar's current emphasis on deterministic feedback sensors, sandboxing and mutation/testing gates, but with a deeper evidence ledger and explicit system-reliability protocols. For MMALS, the analogous lesson is that router/host performance claims must remain separate from memory, execution-state and evaluation-harness effects.

## Follow-up

Compare the monograph's minimum reliability pass and recovery fault-injection protocol with the existing scientific/engineering harness. Reuse only protocol ideas that add a missing falsification or governance obligation; avoid wholesale duplication.

## Provenance note

Claims about corpus size, dependency-chain framing and provided protocols are source-derived. The mapping to Diderot, Test Authority and MMALS is reviewer inference.
