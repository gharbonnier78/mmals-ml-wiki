---
title: "Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems"
canonical_url: "https://arxiv.org/abs/2609.00237"
author_or_publisher: "Rakibul Hasan Rajib, Mengxing Zheng, Qian Lou"
publication_date: "2026-08-31"
discovered_via: "Daily research watch / arXiv"
alert_topic: "agent memory; routing; selective retention"
reviewed_at: "2026-09-02"
source_type: "peer-reviewed conference paper / arXiv preprint (EMNLP 2026 Main)"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Chronicle", "agentic systems"]
related_concepts: ["memory admission", "retrieval gating", "routing", "adaptive halting", "context compression"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper proposes a multi-agent routing architecture in which the evolving execution state is represented by a learned memory rather than by the query alone or the complete raw history. A write gate admits only selected intermediate reasoning steps, a retrieval gate exposes selected memory to downstream agents, and an adaptive halting controller stops once the stored state is judged sufficient.

## What the source actually provides

Source-derived facts: the work is accepted to EMNLP 2026 Main. It evaluates the method across five reasoning and code-generation benchmarks. The authors report the best average accuracy among their compared systems, +2.44 points over the strongest baseline, and a 31.9% HumanEval inference-cost reduction relative to that baseline. The paper also releases code.

Reviewer inference: the main value for MMALS is not the multi-agent packaging but the explicit separation of memory admission, retrieval exposure, routing and stopping decisions.

## Limitations and uncertainty

The components are learned jointly and the abstract-level evidence does not establish the independent causal value of each gate. Benchmarks are LLM reasoning/code tasks rather than non-stationary continual-learning regimes. A learned write gate can also silently delete information whose future utility is not yet visible, so retention quality must be tested under delayed dependencies and regime recurrence.

## Consequence for current work

Chronicle should keep distinct controls for `write`, `retain/supersede`, `retrieve/expose`, and `stop`, rather than treating memory as one monolithic mechanism. A direct MMALS ablation is: full history vs bounded chronological buffer vs learned admission only vs admission+retrieval gating, holding router/host logic fixed.

## Follow-up

Add a Chronicle experiment measuring future-regret caused by rejected writes and unnecessary retrievals, including delayed-use and recurring-regime cases.

## Provenance note

Performance numbers and architectural components above are source-derived. Mapping them to Chronicle and the proposed ablation is reviewer inference; the paper does not establish MMALS continual-learning performance or safety guarantees.
