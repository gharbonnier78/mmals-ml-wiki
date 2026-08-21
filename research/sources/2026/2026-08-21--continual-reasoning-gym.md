---
title: "Continual Reasoning Gym: Diagnosing and Harnessing Shared Reasoning in Continual RLVR"
canonical_url: "https://arxiv.org/abs/2608.18574"
author_or_publisher: "Lirui Luo, Guoxi Zhang, Hongming Xu, Rongqing Li, Cong Fang, Lifeng Fan"
publication_date: "2026-08-19"
discovered_via: "Daily research watch / arXiv"
alert_topic: "continual learning, reasoning benchmarks"
reviewed_at: "2026-08-21"
source_type: "arXiv preprint / benchmark"
relevance: "medium-high adjacent"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Diderot", "continual learning"]
related_concepts: ["continual RLVR", "shared reasoning", "prompt replay", "forgetting decomposition"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Continual Reasoning Gym separates two effects often conflated in continual learning: forgetting of previous tasks and failure to reach the jointly trained multitask optimum. It introduces five text/visual reasoning task sequences and reports that modest forgetting can coexist with a persistent gap to multitask RLVR.

## What the source actually provides

The authors decompose final performance and identify transferable shared reasoning across tasks. Their Continual Prompt Replay replays earlier prompts but regenerates responses with the current policy; among evaluated methods it is reported to recover multitask-RLVR-level average performance.

## Limitations and uncertainty

Fresh preprint, focused on reasoning models trained with verifiable rewards, not task-free latent-context discovery. Task sequences are defined externally. Prompt replay may not transfer to settings where old data cannot be retained or where regenerated outputs introduce bias.

## Consequence for current work

Source-derived: low measured forgetting does not imply that sequential training has captured all transferable structure available under joint training. Reviewer inference: MMALS evaluations should report both retention and a joint/oracle upper-bound gap, so that apparent success is not declared solely because forgetting is small.

## Follow-up

Add a decomposition to future MMALS benchmarks: forgetting loss versus "missed transfer" gap relative to a jointly trained or oracle-context upper bound.

## Provenance note

Facts come from arXiv:2608.18574. The MMALS metric decomposition is reviewer inference.