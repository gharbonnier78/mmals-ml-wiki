---
title: "Calibration is the Bottleneck: An Action-Class Diagnostic of Multi-Turn Tool-Calling"
canonical_url: "https://arxiv.org/abs/2609.00949"
author_or_publisher: "Kangjia Zhao et al."
publication_date: "2026-09-01"
discovered_via: "Daily research watch / arXiv"
alert_topic: "agent testing; tool calling; action calibration"
reviewed_at: "2026-09-02"
source_type: "peer-reviewed conference paper / arXiv preprint (EMNLP 2026 Findings)"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["Diderot", "Test Authority", "agentic systems", "MMALS-CAL"]
related_concepts: ["action classes", "multi-turn evaluation", "miscalibration", "execution failure", "gold action recall"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper separates multi-turn agent failure into choosing the wrong kind of action and executing a chosen tool action badly. It evaluates a four-class action space (TOOL_CALL/ASK/REFUSE/CONFIRM) and introduces Gold Action Recall (GAR) as a diagnostic bound intended to expose failures hidden by aggregate state graders.

## What the source actually provides

Source-derived facts: the paper is accepted to EMNLP 2026 Findings and evaluates multiple tool-calling models across several multi-turn benchmarks. The authors report substantial action-class miscalibration that ordinary state grading can miss. Context-only perturbations can move accuracy in opposite directions across model families, with reported shifts as large as +11.5 versus -21.0 percentage points in the same scenario.

Reviewer inference: for Test Authority, agent qualification should separately score `was this an appropriate action now?` and `was the action executed correctly?`; aggregate task success can mask an unsafe or context-inappropriate action policy.

## Limitations and uncertainty

The paper uses the word calibration in an action-selection sense, not conformal calibration or a statistical coverage guarantee. GAR depends on the quality and completeness of gold action labels. The four action classes may be too coarse for many engineering agents, and context perturbation sensitivity does not identify the causal reason for model-family differences.

## Consequence for current work

Add action-class diagnostics to agentic qualification alongside executable outcome checks. For GO/evidence-driven agents, distinguish evidence-seeking, clarification, abstention/refusal, confirmation and execution decisions before measuring tool correctness.

## Follow-up

Define a project-specific action taxonomy and measure class confusion plus execution success on existing Diderot/Test Authority agent episodes. Do not merge this metric with conformal CAL evidence.

## Provenance note

The diagnostic structure and reported benchmark behavior are source-derived. The proposed engineering action taxonomy and separation from MMALS statistical calibration are reviewer conclusions.
