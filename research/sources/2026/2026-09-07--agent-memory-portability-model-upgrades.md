---
title: "Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability"
canonical_url: "https://arxiv.org/abs/2609.05339"
author_or_publisher: "Ankit Goyal, Jaideep Ray"
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: ""
reviewed_at: "2026-09-07"
source_type: "arXiv preprint"
relevance: "High: Chronicle durability and model migration"
evidence_quality: "Medium-high"
related_tracks: ["MMALS Chronicle", "agentic systems", "Diderot"]
related_concepts: ["memory portability", "model upgrades", "embedding migration", "source retention"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The study shows that an agent can preserve the same logical memory store yet lose effective memory after a model upgrade because the new model may reinterpret compressed notes differently or because mixed embedding spaces impair retrieval. Fixed-schema knowledge graphs transfer far more reliably in the tested setup than model-written notes.

## What the source actually provides

Source-derived facts: 48 synthetic histories with randomized answer codes, exact scoring, and two open-weight sub-10B models compare raw long-context history, RAG chunks, model-compressed notes, and fixed-schema knowledge graphs. KG-fixed changes by only +0.0004 ± 0.0020 under a writer swap, while NOTES shift by +9.91 or -13.28 percentage points depending on migration direction. A 50/50 mixed embedding index captures only 4.96 points of an 11.90-point full re-embedding gain. Diagnostic decomposition attributes most NOTES deficit to construction loss and most RAG deficit to retrieval failure. Raw source history materially improves repairability.

## Limitations and uncertainty

The histories are synthetic, the model set is small, and the memory tasks are narrower than long-lived engineering evidence. Exact numerical effects should not be generalized to other model families or memory schemas.

## Consequence for current work

Reviewer inference: Chronicle should treat model/embedding version as part of memory provenance, isolate incompatible embedding spaces, prefer stable explicit schemas for durable facts, and retain reconstructible source evidence when feasible. Memory migration should be qualified as a release event rather than assumed transparent.

## Follow-up

Add a Chronicle migration test matrix covering writer-model swap, retriever/embedding swap, partial re-indexing, schema version changes, and recovery with/without raw source evidence.

## Provenance note

Experimental setup and reported migration effects are source-derived. The Chronicle release/migration policy is reviewer inference.