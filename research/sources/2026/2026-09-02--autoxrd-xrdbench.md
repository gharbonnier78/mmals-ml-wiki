---
title: "AutoXRD: Autonomous LLM Agents and Comprehensive Evaluation for Powder Diffraction Analysis"
canonical_url: "https://arxiv.org/abs/2609.00070"
author_or_publisher: "Yuetong Wu, Maojun Sun"
publication_date: "2026-09-01"
discovered_via: "Daily research watch / arXiv"
alert_topic: "scientific agents; executable benchmarks; deterministic checks"
reviewed_at: "2026-09-02"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["Diderot", "Test Authority", "agentic systems", "scientific research harness"]
related_concepts: ["executable scientific workflow", "deterministic verification", "evidence preservation", "benchmark decomposition"]
retention_verdict: "retain"
---

# Source note

## Central contribution

AutoXRD frames autonomous powder-diffraction analysis as an evidence-grounded, stepwise refinement workflow with deterministic crystallographic and physical checks before accepting results. XRDBench separates bounded diagnostic questions from end-to-end executable scientific workflows.

## What the source actually provides

Source-derived facts: XRDBench-QA contains 100 diagnostic tasks and XRDBench-E2E 34 executable workflows. The authors report 1,340 model-task runs across ten recent LLMs. Average score falls from 61.9 on QA to 53.7 on E2E, illustrating a gap between isolated scientific reasoning and complete evidence-preserving execution. Tasks include file inspection, software execution, iterative refinement, result acceptance and reporting.

Reviewer inference: the benchmark architecture is directly relevant to Diderot's scientific harness: evaluate atomic reasoning separately from the ability to compose a valid, auditable experimental trajectory under deterministic domain checks.

## Limitations and uncertainty

This is a fresh preprint in one specialized scientific domain. Benchmark construction may encode expert workflow assumptions and the score scale is domain-specific. Deterministic crystallographic checks can establish local validity conditions but not full scientific truth, and performance numbers should not be generalized to other engineering disciplines.

## Consequence for current work

For scientific and engineering agents, maintain two qualification layers: bounded capability tests and end-to-end executable workflows with preserved evidence, domain-rule checks and reproducible artifacts. Do not infer end-to-end reliability from QA-style competence alone.

## Follow-up

Map one MMALS/Diderot research workflow into an XRDBench-like dual benchmark: atomic derivation/diagnostic cases plus a complete reproducible experiment with fixed evidence checkpoints and failure localization.

## Provenance note

Benchmark sizes, model-run count and reported QA/E2E scores are source-derived. The mapping to the Diderot harness is reviewer inference.
