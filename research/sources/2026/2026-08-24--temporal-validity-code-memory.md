---
title: "Temporal Validity on Real Software Histories: Eliminating Stale-Fact Errors in Code-Assistant Memory over GitHub Fixes"
canonical_url: "https://arxiv.org/abs/2608.20685"
author_or_publisher: "Neeraj Yadav"
publication_date: "2026-08-21"
discovered_via: "Daily research watch"
alert_topic: "Agent memory / software engineering"
reviewed_at: "2026-08-24"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["Diderot", "agentic systems", "AI testing", "MMALS Chronicle"]
related_concepts: ["temporal validity", "supersession", "stale memory", "RAG", "software history"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Shows on real software histories that similarity-based retrieval can return superseded facts with high frequency when old and new facts are semantically near-identical. A deterministic supersession memory that represents state transitions explicitly substantially reduces stale-fact errors.

## What the source actually provides

From 707 SWE-bench Lite/Verified GitHub issues, the study extracts 130 clean atomic state transitions. On that subset, MemStrata reports 0.91 answer accuracy versus 0.57-0.59 for RAG. Forced-answer RAG serves superseded values 36-38% of the time, while the supersession memory drives this near zero at roughly comparable retrieval latency and far below the tested LLM reranker latency.

## Limitations and uncertainty

Single-author preprint. Only about 18% of examined fixes form clean atomic transitions suitable for the mechanism; extraction/generalization to richer software changes is explicitly deferred. The study tests temporal validity, not general long-term reasoning or continual learning.

## Consequence for current work

Source-derived fact: semantic similarity alone cannot reliably distinguish current from superseded state. Reviewer inference: Chronicle and Diderot source memory should represent validity intervals/supersession relations explicitly wherever facts evolve, rather than relying only on embeddings and recency heuristics. This also supplies an agent-memory regression case for engineering assistants working over changing repositories.

## Follow-up

Add a stale-memory activation test: after a known state transition, measure whether retrieval, routing or final decisions still use superseded evidence, and compare explicit supersession metadata against similarity-plus-recency baselines.

## Provenance note

Dataset size, subset size, accuracy, stale-answer rates and scope caveat are source-derived. Chronicle/Diderot applications are reviewer inference.