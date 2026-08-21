---
title: "Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs"
canonical_url: "https://arxiv.org/abs/2608.18578"
author_or_publisher: "Shayan Shahrabi-Farahani, Dara Rahmati"
publication_date: "2026-08-19"
discovered_via: "Daily research watch / arXiv"
alert_topic: "LLM memory, deployment, quantization"
reviewed_at: "2026-08-21"
source_type: "arXiv preprint with released code/data"
relevance: "high adjacent"
evidence_quality: "medium-high"
related_tracks: ["Diderot", "agentic systems", "AI testing", "MMALS Chronicle"]
related_concepts: ["quantization", "proactive interference", "memory regression", "deployment equivalence"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The study shows that post-training quantization can selectively worsen memory interference even when aggregate benchmark accuracy appears largely stable.

## What the source actually provides

Three instruction-tuned models are tested at FP16, INT8 and INT4/NF4 on a fixed overwrite/retrieval task. Under high interference, INT4 lowers accuracy in every model; for Qwen the reported drop is 81.0% to 68.3%. Effects are statistically tested with paired McNemar tests and mixed-effects regression. A control condition reverses the effect for numeric distractors, and an ablation localizes the degradation to the quantized transformer backbone rather than the output head. Code and data are released.

## Limitations and uncertainty

Fresh preprint, narrow task family, only three models and bitsandbytes quantization. The result does not establish a general rule that lower precision harms all memory. It targets semantically dense repeated-overwrite interference.

## Consequence for current work

Source-derived: deployment optimization can change a memory-specific failure mode without visibly moving coarse accuracy. Reviewer inference: Diderot/agentic/MMALS qualification should include memory-interference regression tests across precision changes; deployment equivalence should not be inferred from aggregate benchmarks alone.

## Follow-up

Add a compact proactive-interference test to any future quantized memory-agent or Chronicle deployment benchmark, alongside standard accuracy/latency measurements.

## Provenance note

Facts come from arXiv:2608.18578. The deployment-test recommendation is reviewer inference.