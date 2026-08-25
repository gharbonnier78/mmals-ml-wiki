---
title: "Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking"
canonical_url: "https://arxiv.org/abs/2608.21230"
author_or_publisher: "Arulnidhi Karunanidhi"
publication_date: "2026-08-21"
discovered_via: "Daily research watch"
alert_topic: "Agent memory / security / Chronicle"
reviewed_at: "2026-08-25"
source_type: "arXiv preprint with released harnesses/corpora"
relevance: "High"
evidence_quality: "Medium-high"
related_tracks: ["MMALS", "Diderot ML", "Agentic systems", "AI testing"]
related_concepts: ["memory poisoning", "provenance", "persistent memory", "retrieval", "grounding"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper isolates a persistent-memory security failure: plainly worded false assertions can survive content screening and later dominate retrieval. It also shows a nontrivial trade-off in provenance weighting: stronger weights can suppress attacks only by also suppressing legitimate untrusted evidence.

## What the source actually provides

Source-derived facts: poisoning 1.2% of a LongMemEval corpus reportedly reduces accuracy from 0.850 to 0.300. A four-stage write-time screening pipeline with 0.832 recall on indirect prompt injection rejects 0 of 360 poisoned memories. The shipped provenance-weighting configuration is statistically indistinguishable from no defense (p=0.80); stronger weighting recovers utility in one mixed-provenance setting but can drive evidence recall to zero when the answer-bearing evidence is itself untrusted. Harnesses, corpora and aggregate run reports are released.

Reviewer inference: Chronicle needs evidence validity and grounding controls, not just content filters, recency and provenance scores. This aligns with the broader principle that memory can be retained and retrieved correctly while still being false.

## Limitations and uncertainty

Single-paper preprint and an attack model centered on false textual assertions in agent memory. Results should not be generalized directly to all structured or numeric MMALS memory. Provenance weighting is only one defense family.

## Consequence for current work

Add a Chronicle poisoning benchmark with false-but-plausible evidence, including cases where legitimate evidence comes from lower-trust sources. Measure decision degradation, retrieval share, occupancy and recovery, not just whether poison is detected at write time.

## Follow-up

Reproduce the narrow LongMemEval-style attack before considering a more complex trust graph. Compare content screening, provenance weighting, bounded occupancy and external evidence verification.

## Provenance note

Attack results and defense measurements are source-derived. Chronicle implications and proposed controls are reviewer inference.
