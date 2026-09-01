---
title: "Understanding Stage-Wise Utility-Risk Trade-offs in LLM Agent Memory"
canonical_url: "https://arxiv.org/abs/2608.30177"
author_or_publisher: "Chuanchao Zang et al."
publication_date: "2026-08-31"
discovered_via: "Web research"
alert_topic: "MMALS Chronicle / agent memory"
reviewed_at: "2026-09-01"
source_type: "arXiv preprint"
relevance: "P0"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Chronicle", "agentic systems", "AI testing"]
related_concepts: ["memory poisoning", "write admission", "memory management", "retrieval exposure", "utility-risk trade-off"]
retention_verdict: "retain"
---

# Source note

## Central contribution

MemGauge decomposes long-term agent memory into three controllable stages—writing admission, management policy, and retrieval exposure—and measures benign utility and poisoning risk under matched conditions rather than evaluating memory as a single opaque component.

## What the source actually provides

Source-derived facts: across 11 LLMs and two long-term-memory benchmarks, the authors report different utility-risk profiles by stage: a threshold-like risk transition during writing, policy-dependent partial decoupling during management, and coupled growth of utility and poisoning risk during retrieval. They also apply analogous measurements to four existing memory systems and report qualitatively consistent diagnostic patterns.

## Limitations and uncertainty

This is a fresh preprint and the threat model is targeted memory poisoning in LLM-agent memory, not the full MMALS functional/experimental Chronicle. Stage effects may depend strongly on benchmark, memory implementation, attack construction, and model family. The work does not provide a general safety guarantee.

## Consequence for current work

Reviewer inference: Chronicle should be evaluated as a pipeline of admission, transformation/retention, and retrieval/use decisions rather than with one aggregate memory score. This also supports maintaining an explicit no-write/no-retrieve action and separate controls for provenance, bounded influence, and retrieval exposure.

## Follow-up

Add a Chronicle ablation matrix that independently varies write admission, supersession/management policy, and retrieval exposure. Measure useful reuse, stale or poisoned reuse, false rejection of valid experience, and downstream decision regret.

## Provenance note

The stage decomposition and reported profiles are source-derived. The mapping to Chronicle controls and proposed ablation are reviewer inference.
