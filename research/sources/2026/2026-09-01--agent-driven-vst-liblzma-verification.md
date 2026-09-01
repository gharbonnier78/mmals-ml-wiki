---
title: "Agent-Driven Verification of Memory Safety for liblzma Decoder Components with VST"
canonical_url: "https://arxiv.org/abs/2608.29716"
author_or_publisher: "Prokhor Shlyakhtun et al."
publication_date: "2026-09-01"
discovered_via: "Web research"
alert_topic: "AI testing / agentic engineering"
reviewed_at: "2026-09-01"
source_type: "arXiv preprint"
relevance: "P0/P1"
evidence_quality: "medium-high"
related_tracks: ["Diderot", "Test Authority", "agentic systems", "software verification"]
related_concepts: ["formal verification", "Rocq", "VST", "proof harness", "human-agent collaboration", "machine-checked evidence"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The work demonstrates AI-agent-assisted formal verification of pre-existing production-scale C components from liblzma using the Verified Software Toolchain and Rocq, with humans retaining control of models/specifications and the proof kernel checking generated proof terms.

## What the source actually provides

Source-derived facts: the authors report 27 completed body proofs covering LZMA2/LZMA1 decoder components, outer decoding paths, and the sliding-window dictionary. The largest proof concerns `lzma_decode`; the process exposed undefined behavior in raw LZMA1 zero-input handling involving null-pointer arithmetic. Agents construct proof scripts and propose refinements, while humans write/review specifications and approve semantic changes; Rocq checks proof terms.

## Limitations and uncertainty

This is an arXiv report and the verification scope is memory safety plus partial functional correctness for selected components, not total correctness of xz-utils. The proof engineering effort is extremely large, and the result does not show that agent assistance makes formal verification economical for ordinary software projects.

## Consequence for current work

Reviewer inference: this is strong evidence for an evidence hierarchy in agentic engineering: agent-generated artifacts can be acceptable when a deterministic formal checker is the authority. It also reinforces the importance of harness feedback, explicit specifications, and separating model/agent productivity from evidence credibility.

## Follow-up

Use this as a reference case in the Test Authority agent-assurance track: compare LLM reviewer evidence, executable tests, static analyzers, mutation testing, and proof-kernel evidence by strength, cost, and applicable scope.

## Provenance note

Verification scope, discovered undefined behavior, and human/agent/kernel roles are source-derived. The evidence-hierarchy interpretation is reviewer inference.
