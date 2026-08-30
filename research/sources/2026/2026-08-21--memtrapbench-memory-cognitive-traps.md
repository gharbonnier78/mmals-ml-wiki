---
title: "MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use"
canonical_url: "https://arxiv.org/abs/2608.20202"
author_or_publisher: "Mengru Wang et al."
publication_date: "2026-08-20"
discovered_via: "Daily research watch / arXiv"
alert_topic: "memory, agents, benchmark"
reviewed_at: "2026-08-21"
source_type: "arXiv preprint / benchmark work in progress"
relevance: "very high"
evidence_quality: "medium"
related_tracks: ["MMALS Chronicle", "agentic systems", "Diderot"]
related_concepts: ["memory-induced reasoning fixation", "belief distortion", "memory usefulness", "negative-result benchmark"]
retention_verdict: "retain"
---

# Source note

## Central contribution

MemTrapBench tests a failure mode ignored by standard memory benchmarks: a memory can be correctly stored, faithfully retrieved and semantically relevant yet still degrade current reasoning. It separates Reasoning Fixation and Belief Distortion.

## What the source actually provides

Across two model families and five memory frameworks, all evaluated memory strategies underperform the no-memory setting on this benchmark; the strongest methods still lose more than 10%. The authors also propose AdaptiveMem, an inference-time mitigation that reportedly reduces these traps while preserving standard benchmark performance.

## Limitations and uncertainty

The work is explicitly marked work in progress and is not peer reviewed. It is specific to LLM memory use, so the failure taxonomy should not be assumed to transfer unchanged to functional continual-learning hosts. The mitigation may partly depend on prompting behavior.

## Consequence for current work

Source-derived: retrieval correctness is insufficient evidence of memory benefit. Reviewer inference: Chronicle evaluation should include a negative-control test where remembered evidence is valid but potentially misleading for the current context, and should measure downstream decision delta against a no-memory baseline.

## Follow-up

Add a Chronicle "memory can hurt" benchmark condition and require memory utility/harms to be reported separately from recall and retrieval metrics.

## Provenance note

Facts above come from arXiv:2608.20202. The Chronicle qualification proposal is reviewer inference.