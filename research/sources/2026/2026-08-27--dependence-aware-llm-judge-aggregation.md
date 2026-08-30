---
title: "Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models"
canonical_url: "https://arxiv.org/abs/2601.22336"
author_or_publisher: "Krishnakumar Balasubramanian, Aleksandr Podkopaev, Shiva Prasad Kasiviswanathan"
publication_date: "2026-01-29"
discovered_via: "Google Alert traced to ICML 2026 / primary paper"
alert_topic: "LLM"
reviewed_at: "2026-08-27"
source_type: "ICML 2026 paper / arXiv preprint"
relevance: "high"
evidence_quality: "high"
related_tracks: ["Diderot", "AI testing", "Test Authority", "MMALS"]
related_concepts: ["LLM-as-a-judge", "dependent evaluators", "Ising models", "evaluation calibration"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Shows that aggregating several LLM judges as if they were conditionally independent can produce confidently wrong aggregate decisions when judges share correlated failure modes. It introduces dependence-aware Ising/latent-factor aggregation models.

## What the source actually provides

Source-derived facts: the paper gives finite-K counterexamples where independence-based aggregation flips the Bayes-optimal label despite matching per-judge marginals, proves non-vanishing excess risk under latent-factor dependence as the number of judges grows, and reports improved performance over classical aggregation baselines on three real datasets. The work appears in the ICML 2026 program.

## Limitations and uncertainty

The study focuses on binary label aggregation, not arbitrary rubric grading or agent trajectories. Model-dependence estimation itself adds sample and modeling requirements. Better aggregation does not turn LLM judges into ground truth.

## Consequence for current work

Reviewer inference: Diderot/Test Authority evaluations must not treat agreement among multiple LLM reviewers as independent evidence. Shared model family, training data, prompting style, or rubric can create correlated errors. This strengthens the requirement for heterogeneous evidence sources and independent executable/ground-truth checks.

## Follow-up

Add an evaluation-harness diagnostic that reports judge provenance/model-family dependence and compares majority vote with a dependence-aware or at least correlation-audited aggregation baseline when LLM ensembles are used.

## Provenance note

The theoretical and empirical aggregation claims are source-derived. The Test Authority/Diderot application is reviewer inference.
