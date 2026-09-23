---
title: "Energy per token on AGX Orin"
canonical_url: "https://github.com/jbecirovski/jetson-llm-maxperf/blob/master/campaigns/2026-08-12-energy/README.md"
author_or_publisher: "Julien Becirovski"
publication_date: "2026-08-12"
source_type: "reproducible engineering measurement campaign"
reviewed_at: "2026-09-02"
relevance: "P1"
evidence_quality: "useful bounded empirical evidence for one board/runtime/model campaign; not a general LLM energy law"
related_tracks: ["edge inference", "GO-ED-POMDP", "resource-aware engineering", "MMALS"]
related_concepts: ["information-preserving compression", "sufficient state", "value function", "context cost", "speculative decoding"]
retention_verdict: "retain with bounded scope"
---

# Source note

## Central contribution

The campaign measures energy per input and output token for Llama 3.1 8B variants on one NVIDIA Jetson AGX Orin 64GB. It reports 40 protocol runs plus a smoke test, organized in blocks of five, and retains environment snapshots, commands, logs, raw power samples and computed energy for replay.

For the short-context generation condition, the reported medians are 754 Wh/M output tokens for the 30 W Q4_K_M configuration, 602 for MAXN Q4_K_M, 501 for MAXN IQ4_XS, and 249 for MAXN with a 1B speculative draft. Thus lower instantaneous power did not imply lower energy per generated token in this campaign.

For the long-context condition (15,718 input tokens), the campaign reports output coefficients of 1025, 910, 812 and 372 Wh/M output tokens respectively. The corresponding MAXN input coefficients are around 16–18 Wh/M input tokens. The source therefore provides a concrete edge example in which active-context load, quantization, power mode and decoding strategy materially alter the resource cost of inference.

## What the source supports for Diderot

- Power, latency/throughput and energy per unit of useful work are different quantities.
- Resource-efficient inference is configuration- and workload-dependent; “low power mode” is not synonymous with “low energy per completed task”.
- Active context can have a downstream execution cost beyond the one-time cost of reading the prompt, at least for the measured model/runtime/hardware configuration.
- Quantization and speculative decoding can be treated as candidate execution choices whose value must be measured against mission-relevant quality and resource criteria.
- Edge deployment is a useful special case for goal- and regime-conditioned engineering objectives, not evidence that energy should dominate every agent objective.

## Boundaries and cautions

This is an engineering campaign, not a peer-reviewed general comparison across hardware or models. The measurements are specific to one AGX Orin 64GB setup, Llama 3.1 8B family configurations and llama.cpp-based execution. The onboard INA3221 measurements are explicitly described by the author as a lower bound relative to wall power. The campaign itself warns against mixing instruments and configurations.

The source text says that long-context generation “halves at nearly constant power” while the reported output energy coefficients rise by roughly 50% in several configurations. Taken literally, those two descriptions are not arithmetically equivalent under a constant-power assumption. Diderot therefore retains the measured table values but does not promote that wording into a general quantitative law.

The campaign does not establish that a POMDP belief, a learned compact state or any particular memory architecture is optimal for LLM agents. The connection to sufficient state is a Diderot engineering synthesis: if historical information can be represented more compactly without unacceptable decision regret, there may be resource benefits to keeping memory recoverable without keeping all history active.

## Pedagogical consequence

Use this campaign to separate four questions that are easy to collapse:

1. What information must the agent preserve for the declared decision?
2. Where is that information stored: active context, compact state, external memory or model parameters?
3. What execution configuration is used to act from that information?
4. Which mission-conditioned costs or constraints determine whether the result is acceptable?

The important general lesson is not “minimize energy”. It is “optimize the declared mission objective under the relevant information and resource constraints, then measure the trade-offs in the regime where the system will operate.”
