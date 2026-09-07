---
title: "TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents"
canonical_url: "https://arxiv.org/abs/2609.05079"
author_or_publisher: "Zhibo Yang, Chen Zhang, Yuewei Zhang, Hao Wang"
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: ""
reviewed_at: "2026-09-07"
source_type: "arXiv benchmark paper with public code/data"
relevance: "High: Diderot scientific harness and agent evidence"
evidence_quality: "Medium-high"
related_tracks: ["Diderot", "scientific research harness", "agentic systems", "Test Authority"]
related_concepts: ["scientific discovery", "evidence grounding", "falsifiability", "robustness", "agent evaluation"]
retention_verdict: "retain"
---

# Source note

## Central contribution

TruthInsightBench evaluates agents on blind scientific-analysis tasks where the target study's conclusions and analysis path are withheld, shifting evaluation from reproducing a known result toward determining what claims the available data actually justify.

## What the source actually provides

Source-derived facts: the benchmark contains 40 tasks from 40 peer-reviewed studies across 10 domains. Agents receive a neutral objective and frozen data but not expected conclusions. Evaluation uses six dimensions decomposed into 29 artifact-grounded items with deterministic aggregation around a fixed LLM judge. On one frozen base model, four coding agents cluster at 58.4–60.3/100 with no statistically reliable pairwise separation; reported weaknesses concentrate in controls, robustness, falsifiability, and cross-dataset generalization rather than basic execution/documentation. Code and data are public.

## Limitations and uncertainty

The benchmark is small, uses a fixed LLM judge for item scoring, and one base model for the reported agent comparison. Blind reconstruction of findings is still not equivalent to genuinely novel science, and benchmark design can encode the authors' view of scientific maturity.

## Consequence for current work

Reviewer inference: Diderot should explicitly separate executable analysis from defensible scientific claim formation. Controls, robustness, falsifiability and cross-dataset generalization should be first-class evidence dimensions rather than optional reviewer commentary.

## Follow-up

Map TruthInsightBench's evidence dimensions to the existing Diderot review form and identify which can be checked deterministically versus by human/scientific review.

## Provenance note

Task construction, scoring design and reported plateau are source-derived. The proposed Diderot mapping is reviewer inference.