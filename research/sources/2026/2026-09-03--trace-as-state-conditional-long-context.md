---
title: "Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"
canonical_url: "https://arxiv.org/abs/2609.02702"
author_or_publisher: "Xu Zou, Jie Tang"
publication_date: "2026-09-02"
discovered_via: "MMALS daily web research watch"
alert_topic: "inferred context / memory / long-context reasoning"
reviewed_at: "2026-09-03"
source_type: "arXiv preprint"
relevance: "P0"
evidence_quality: "medium-high preprint: formal worst-case result plus matched positional control across 3 models and 3 datasets"
related_tracks: ["MMALS", "Diderot ML"]
related_concepts: ["conditional state", "belief/state summary", "memory ordering", "long-context reasoning", "POMDP analogy"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper formalizes a causal-processing mismatch: when the condition needed to interpret a long context is discovered only late, a causal processor may require exponentially more memory than when that condition is available first. It then uses a reasoning trace as a proxy for conditional task state and places that state before rereading the context.

## What the source actually provides

Source-derived facts: the authors define conditional state-update tasks and prove a worst-case memory separation between condition-first and condition-last processing. Their Trace-as-State method prepends a collected reasoning trace before a fresh pass over the long context. A matched Trace-Append control uses the same state proxy after the context. Across three models and three datasets, Trace-as-State wins in 26 of 27 reported model/task/metric combinations. On GraphWalks Parents, the abstract reports large exact-match gains for two frontier models.

## Limitations and uncertainty

The state proxy is a generated reasoning trace, which can itself be wrong, verbose or brittle. The theorem is a worst-case result for the formal task family and does not establish exponential practical savings in ordinary workloads. Rereading the context adds compute and does not by itself solve state correctness or provenance.

## Consequence for current work

Reviewer inference: this is highly relevant to MMALS's POMDP-like idea of retaining a sufficient current belief/state rather than the full raw history. It suggests a concrete ordering principle: infer/validate compact state, then use that state to condition subsequent interpretation or routing. Chronicle should therefore distinguish raw history from a validated current-state summary and measure when that summary is actually sufficient.

## Follow-up

Create a benchmark where identical histories become interpretable only after a latent regime/state cue appears late; compare full-history processing, append-only summary, prepend-state reread, and a compact belief-state representation.

## Provenance note

The theorem, method and reported benchmark results are source-derived. The mapping to MMALS belief state and Chronicle compression is reviewer inference.