---
title: "DreamBench-SWE: A Multi-Session Memory-Hygiene Benchmark for Software Agents"
canonical_url: "https://arxiv.org/abs/2608.20664"
author_or_publisher: "Sarthak Singh"
publication_date: "2026-08-21"
discovered_via: "Daily research watch"
alert_topic: "Agent memory benchmark / software engineering"
reviewed_at: "2026-08-25"
source_type: "arXiv benchmark preprint"
relevance: "High"
evidence_quality: "Medium-high"
related_tracks: ["Diderot ML", "MMALS", "AI testing", "Agentic systems"]
related_concepts: ["multi-session memory", "memory hygiene", "hidden oracles", "preregistration", "software agents"]
retention_verdict: "retain"
---

# Source note

## Central contribution

DreamBench-SWE benchmarks whether software agents retain non-inferable evidence across sessions and later use it correctly, scoring with executable hidden oracles rather than retrieval similarity alone.

## What the source actually provides

Source-derived facts: the successor audit was preregistered before outcome inspection and completed 360 work units / 720 S3 cells. Reported pass rates include 21/180 with no external memory, 82/180 with deterministic verbatim event memory, 83/180 with a typed-plus-raw reference probe, and 97/180 for one pinned hosted Mem0 literal-storage configuration. The paper explicitly refuses stronger claims where mechanism contrasts were unavailable or nonconfirmatory.

Reviewer inference: the benchmark's strongest value for Diderot/MMALS is methodological. Memory should be evaluated by later executable consequences under controlled evidence dependencies, not by recall@k alone.

## Limitations and uncertainty

The benchmark is software-agent-specific and the strongest hosted-memory result characterizes one exact configuration, not a product family. The paper does not establish a causal mechanism for superiority among memory-bearing conditions.

## Consequence for current work

Adopt an analogous benchmark pattern for Chronicle: plant evidence that cannot be reconstructed from the current observation, require later decisions that depend on it, and score by hidden functional oracles. Keep a deterministic raw-memory baseline as a hard comparator.

## Follow-up

Design a minimal MMALS recurrence benchmark with non-inferable earlier evidence and executable outcome scoring; preregister the primary memory comparison before inspecting results.

## Provenance note

Benchmark design, sample sizes and pass counts are source-derived. The Chronicle benchmark translation is reviewer inference.
