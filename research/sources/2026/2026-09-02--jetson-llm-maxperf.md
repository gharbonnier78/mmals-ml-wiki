---
title: "Jetson LLM MaxPerf — context, generation and mission energy"
canonical_url: "https://github.com/jbecirovski/jetson-llm-maxperf"
author_or_publisher: "Julien Becirovski"
publication_date: "2026"
discovered_via: "learner-supplied LinkedIn screenshots and discussion"
alert_topic: "embedded LLM energy and context"
reviewed_at: "2026-09-02"
source_type: "engineering benchmark repository"
relevance: "Runtime evidence for the cost side of a broader context-to-consolidation decision boundary."
evidence_quality: "bounded engineering evidence; platform/model/workload specific; not an architecture-selection study"
related_tracks: ["MMALS", "continual learning", "edge inference", "evidence-centric model lifecycle"]
related_concepts: ["belief-model-memory", "sufficient-state", "tput", "non-regression-evidence"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The repository measures and models LLM inference performance on NVIDIA Jetson hardware rather than relying only on headline tokens per second. It is valuable to Diderot because it makes power, elapsed time, memory traffic, context length and energy-per-token part of a reproducible engineering question.

## What the source actually provides

The learner-supplied screenshots report a Jetson AGX Orin experiment using Llama 3.1 8B, llama.cpp and medians of five runs. Visible configurations span 249 to 754 Wh per million generated tokens. The lowest-watt configuration is not the lowest-energy-per-token configuration because it runs longer.

The screenshots also report that processing a 16,000-token inspection log to produce JSON cost about 0.35 Wh for the shown setup, while retained context raised the cost of later output tokens. These are encounter-level transcriptions and must be verified against repository artifacts before use as cross-platform quantitative claims.

The source supports conditional statements of the form:

\[
P(\text{runtime cost}\mid\text{chosen model, board, software and configuration}).
\]

## Limitations and uncertainty

- one principal board/model/software family in the discussed result;
- hardware, quantisation, prompt shape and output length can change the result;
- energy numbers depend on the declared measurement window and baseline;
- the work does not compare the LLM against non-LLM architectures capable of fulfilling the same mission;
- it does not demonstrate a robotic autonomy architecture, continual learning strategy, or optimal RAG/fine-tuning boundary;
- LinkedIn post wording and screenshots are secondary encounter evidence; repository methods and raw artifacts have authority.

## Consequence for current work

Retain this source as one runtime-measurement block for a larger experiment comparing short context, long context, RAG, memory compression, adapters, fine-tuning, distillation and specialised routing. Do not use it to claim that an LLM should control a robot or that a particular context length is universally optimal.

## Follow-up

- reproduce selected measurements on at least one second hardware/model stack;
- separate prefill from decode energy and latency;
- sweep context length and output length;
- record KV-cache occupancy;
- compare equal-mission treatments rather than only equal-model configurations;
- include offline consolidation and qualification cost in the total lifecycle accounting.

## Provenance note

Source-reported benchmark facts, screenshot transcriptions and Diderot/MMALS inferences are kept separate in the companion synthesis:
\`research/2026-09-02--context-memory-model-evidence-decision-boundary.md\`.
