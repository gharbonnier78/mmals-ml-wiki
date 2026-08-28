---
title: "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling"
canonical_url: "https://arxiv.org/abs/2608.26623"
author_or_publisher: "Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru"
publication_date: "2026-08-27"
discovered_via: "Daily web/arXiv watch"
alert_topic: "AI testing / agentic evaluation"
reviewed_at: "2026-08-28"
source_type: "EMNLP 2026 main conference paper / arXiv"
relevance: "high"
evidence_quality: "high"
related_tracks: ["Diderot", "AI testing", "Test Authority", "agentic systems"]
related_concepts: ["LLM-as-a-judge", "tool-calling", "workflow DAG", "ground truth", "evaluation reliability"]
retention_verdict: "retain"
---

# Source note

## Central contribution

AgentJudgeBench tests LLM judges specifically on structured agentic tool-calling workflows and shows a difficulty-dependent ceiling that model scale alone does not remove.

## What the source actually provides

Source-derived facts: 3,808 instances span six DAG topologies and three difficulty tiers, with five generators and six judges. Judge alignment degrades monotonically with task difficulty and more quickly without ground truth. On hard no-ground-truth queries all six judges fall in a narrow 77–82% alignment band. Structured rubrics improve alignment by up to 6.5 percentage points but not uniformly; chain-of-thought and temperature changes provide negligible mitigation. The work is accepted as an EMNLP 2026 main paper.

## Limitations and uncertainty

The benchmark is synthetic/structured around tool-calling DAGs and does not cover all open-ended engineering evaluation. The reported ceiling depends partly on prompt and generator characteristics.

## Consequence for current work

Reviewer inference: Diderot and agentic testing should not use a stronger LLM judge as a substitute for executable/programmatic evidence. Evaluation difficulty and workflow structure must be explicit, and rubric improvements should be treated as partial mitigation rather than validation.

## Follow-up

For agentic workflows, classify assertions by evidence type: executable oracle, deterministic structural check, human review, or LLM judge. Quantify where conclusions would change if judge-only items were removed.

## Provenance note

Benchmark design and reported results are source-derived from the arXiv listing. Diderot implications are reviewer inference.
