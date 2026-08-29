---
title: "BTS-AgentBench: A Deterministic, Replayable Pipeline from Read-Only Telemetry Logs to Agent Benchmarks"
canonical_url: "https://arxiv.org/abs/2608.27334"
author_or_publisher: "Jeong-Yoon Kim / arXiv"
publication_date: "2026-08-27"
discovered_via: "Daily web/arXiv watch"
alert_topic: "Diderot agent evaluation; telemetry-to-benchmark"
reviewed_at: "2026-08-29"
source_type: "arXiv preprint with public code/artifacts"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["Diderot", "Test Authority", "agentic systems", "systems engineering"]
related_concepts: ["deterministic benchmark construction", "telemetry", "replayability", "evidence attribution", "operator-facing episodes"]
retention_verdict: "retain"
---

# Source note

## Central contribution

BTS-AgentBench defines a deterministic pipeline that converts read-only industrial telemetry into executable, multi-turn agent benchmarks with tool-derived gold answers, bounded operator-facing episodes, timestamp policy, clarification/goal revision and evidence attribution.

## What the source actually provides

Source-derived facts: the release contains 532 rows with a 356/87/89 train/dev/test split; two independent raw-to-episode builds reproduce all 11 logical tool-store exports and the released split exactly; a coded construction-exclusion controller completes 0/532 rows; the same construction path is applied to XAI4HEAT for 204 episodes, including a 41-row held-out test on which the retained GPT-5.5 execution completes all 41. Code, artifacts and replay reports are public via the linked GitHub repository.

Reviewer inference: the main value is not the model score but the benchmark-construction discipline: operational telemetry can become reproducible, evidence-bearing agent qualification material without granting the agent write access to the source system.

## Limitations and uncertainty

Single-author preprint, with a narrow read-only telemetry setting. A perfect result on the 41-row held-out XAI4HEAT slice should not be interpreted as general agent reliability. The benchmark construction itself may encode simplifications that are absent in production systems with incomplete semantics, mutable state, permissions and side effects.

## Consequence for current work

For Diderot/Test Authority, this is a strong pattern for turning existing observability/telemetry into deterministic qualification episodes. It fits the evidence-driven harness better than LLM-as-judge-only evaluation and could inform future OTEL/spec-to-evidence benchmark generation.

## Follow-up

Prototype one telemetry-to-episode transformation on a non-confidential synthetic or public trace set. Require deterministic replay, explicit evidence pointers, controller exclusion tests and a frozen scorer before comparing agents.

## Provenance note

Dataset sizes, reproducibility claims, controller results and reported held-out execution are source-derived. The proposed use for Diderot/Test Authority is reviewer inference.