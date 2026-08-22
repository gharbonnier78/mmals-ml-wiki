---
title: "Phantom Gains: Auditing Self-Improvement Against a Measured Null"
canonical_url: "https://arxiv.org/abs/2608.20290"
author_or_publisher: "Cheng Xu, Nan Yan, Liming Chen, M-Tahar Kechadi"
publication_date: "2026-08-20"
discovered_via: "Daily web/arXiv watch"
alert_topic: "AI testing / continual improvement"
reviewed_at: "2026-08-22"
source_type: "arXiv preprint with released evaluation artifacts"
relevance: "High"
evidence_quality: "Medium-high"
related_tracks: ["MMALS", "Diderot ML", "AI testing"]
related_concepts: ["measured null", "self-improvement", "multiple testing", "evaluation artifacts", "falsification"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper shows that apparent problem-level gains and losses in self-improving language models can be manufactured by evaluation noise and pipeline artifacts unless every transition statistic is calibrated against a separately measured null produced by frozen controls.

## What the source actually provides

Source-derived facts: the authors run three rounds of rank-32 LoRA self-training on Qwen3-8B alongside a frozen control processed through the same pipeline. They identify seven measurement failures, including single-decode/batching artifacts that create apparent capability changes in an untrained model. They replace heuristic transition thresholds with per-problem exact testing against pooled frozen baselines under false-discovery-rate control. Under this audit, external distillation shows gains on some problems whereas several forms of self-training do not; self-training also corrupts some previously solved problems above the measured floor.

## Limitations and uncertainty

The findings are specific to the tested LLM self-training setup and transition metrics. The paper is a preprint, and its exact null construction may not transfer directly to continual-learning geometry or routing experiments.

## Consequence for current work

Reviewer inference: MMALS should treat any claim such as "this regime was newly learned", "routing improved this subgroup", or "a host was recovered" as a noisy transition claim requiring a measured null. Frozen-pipeline replicates can reveal apparent changes caused by stochastic inference, batching, seeds, or evaluation bookkeeping rather than learning.

## Follow-up

Add a measured-null protocol to MMALS transition-level claims: frozen-model/unchanged-router replicates, repeated inference where stochasticity exists, explicit false-discovery control for per-regime claims, and a requirement that reported improvement exceed the empirically measured transition floor.

## Provenance note

The audit findings and reported experimental results are source-derived. The proposed MMALS governance rule is reviewer inference.
