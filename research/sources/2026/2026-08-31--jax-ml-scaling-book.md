---
title: "How to Scale Your Model — A Systems View of LLMs on TPUs"
canonical_url: "https://jax-ml.github.io/scaling-book/"
author_or_publisher: "Jacob Austin et al. / Google DeepMind"
publication_date: "2025-02-04"
discovered_via: "Explicit user source"
alert_topic: "ML systems / LLM scaling"
reviewed_at: "2026-08-31"
source_type: "Online technical book / systems tutorial"
relevance: "High for ML systems pedagogy"
evidence_quality: "High for systems pedagogy; medium as scientific evidence"
related_tracks: ["Diderot ML", "LLM systems", "Transformer foundations", "ML systems engineering"]
related_concepts: ["roofline model", "arithmetic intensity", "compute-bound", "communication-bound", "Transformer FLOPs", "KV cache", "strong scaling", "model parallelism"]
retention_verdict: "retain"
---

# Source note

## Central contribution

*How to Scale Your Model* gives a systems-level account of how large Transformer models map onto real accelerator constraints. Its distinctive pedagogical value is the bridge from relatively simple mathematical objects — tensor dimensions, matrix multiplications, FLOP counts and bytes moved — to system-level regimes such as compute-bound, memory/communication-bound, strong scaling, training/inference trade-offs and distributed parallelism.

The source is especially valuable for Diderot because it connects three levels that are often learned separately: linear-algebraic structure of the model, algorithmic cost, and physical/hardware constraints.

## What the source actually provides

Source-derived scope:

- Chapter 1 introduces roofline analysis in terms of computation rate, communication or memory bandwidth and total memory, then uses arithmetic intensity to reason about compute-bound versus communication-bound regimes.
- Chapter 4 develops the arithmetic of Transformer models: tensor/matrix sizes, parameter counts, FLOPs, forward/backward cost, memory implications and KV-cache sizing.
- Chapters 5 and 7 treat training and inference as different systems problems, including model parallelism, memory-reduction techniques, latency, throughput and KV-cache constraints.
- Chapters 2, 3 and 12 connect these models to TPU/GPU hardware and interconnects; Chapters 9 and 10 move into profiling and JAX implementation.
- The authors explicitly position the book as a systems view of LLM scaling and as a way to estimate training/inference cost and select parallelism strategies.

The book was initially published on 2025-02-04 and states that it is a draft that continues to be revised.

## Limitations and uncertainty

This is an expert technical book/tutorial, not a peer-reviewed experimental paper establishing universal performance laws. Hardware-specific numeric examples can age as accelerator generations change. The presentation is historically TPU-centered, although it now includes a GPU chapter. Simplified roofline reasoning gives useful first-order bounds, but real execution includes imperfect overlap, kernel/runtime overheads, topology effects, implementation details and profiling-specific deviations.

Accordingly, Diderot should treat the source as a strong pedagogical and engineering reference, not as evidence that one parallelization strategy or performance estimate is universally optimal.

## Consequence for current work

Reviewer synthesis: retain this source as the main entry point for a new pedagogical bridge:

`linear algebra -> tensor shapes -> Transformer operations -> FLOPs/bytes -> hardware limits -> scaling regime -> training/inference architecture`.

This complements Transformer/attention study by explaining what the mathematics implies once the model has to run on real hardware. It also provides a concrete example of a broader engineering habit useful beyond LLMs: build the smallest model that explains the dominant regime, identify its validity boundary, then confront it with measurement.

Concept candidates to capitalize during the study, without pre-promoting them as understood, include: roofline model, arithmetic/operational intensity, compute-bound versus memory/communication-bound operation, strong scaling, KV cache, prefill versus decode, and the principal forms of model parallelism.

## Follow-up

Queue a dedicated Diderot study: **From Transformer mathematics to system scaling**.

Recommended sequence:

1. Roofline analysis and arithmetic intensity.
2. Transformer mathematics: tensor shapes, parameter counts, FLOPs and memory.
3. Transformer inference: latency, throughput, prefill/decode and KV cache.
4. GPU/TPU hardware constraints and comparison of rooflines.
5. Training and sharding/parallelism strategies.
6. JAX/profile exercises only after the paper-and-pencil models can be reconstructed.

Expected learning artifacts are derivations that can be rebuilt by hand, small falsifiable performance predictions, and then executable checks. Any non-trivial mathematical notation introduced or meaningfully re-encountered during the study must be reconciled with the canonical Diderot notation registry and remain draft until reviewed.

## Provenance note

Book scope, chapter topics, publication date and the draft/revision status are source-derived from the canonical Scaling Book site. The proposed Diderot learning sequence, concept candidates and interpretation as a linear-algebra-to-systems bridge are reviewer synthesis for this repository.
