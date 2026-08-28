---
title: "DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows"
canonical_url: "https://arxiv.org/abs/2608.26546"
author_or_publisher: "Zechun Niu et al."
publication_date: "2026-08-27"
discovered_via: "Daily web/arXiv watch"
alert_topic: "agentic systems / AI testing"
reviewed_at: "2026-08-28"
source_type: "arXiv benchmark paper with public code/data"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["Diderot", "AI testing", "Test Authority", "agentic systems"]
related_concepts: ["real-session benchmark", "environmental complexity", "workflow state", "robustness", "framework-model interaction"]
retention_verdict: "retain"
---

# Source note

## Central contribution

DuMateBench reconstructs agent tasks from real production sessions and preserves pre-solution history, persistent configuration and workspace state, then injects insufficient, unstable and noisy environment conditions.

## What the source actually provides

Source-derived facts: 200 tasks span 8 broad scenarios and 17 fine-grained capability categories. Tasks run in isolated Docker containers and are evaluated with a mix of deterministic checks and LLM-as-a-judge. Experiments across five agent frameworks and four frontier LLMs show substantial strict-completion gaps and indicate that robustness depends jointly on the base model and surrounding harness/framework.

## Limitations and uncertainty

The benchmark is only 200 tasks and includes LLM-judge components; anonymization and reconstruction can alter some production context. It is an agent benchmark, not a continual-learning benchmark.

## Consequence for current work

Reviewer inference: Diderot/Test Authority should evaluate model+harness+environment as one system and explicitly inject instability/noise/missing resources. This also provides a useful counterweight to clean benchmark-only claims for self-improving agents.

## Follow-up

Reuse the three environmental-complexity classes as a small fault taxonomy for agentic engineering evaluations: insufficient dependency, unstable dependency, noisy/irrelevant state.

## Provenance note

Benchmark composition and evaluation setup are source-derived from the arXiv listing. The proposed testing taxonomy is reviewer inference.
