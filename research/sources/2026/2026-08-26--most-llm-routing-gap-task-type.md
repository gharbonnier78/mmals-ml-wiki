---
title: "Most of the LLM Routing Gap Is Task Type"
canonical_url: "https://arxiv.org/abs/2608.23023"
author_or_publisher: "Janghoon Lee (Redrob)"
publication_date: "2026-08-24; revised 2026-08-25"
discovered_via: "Daily research watch / arXiv"
alert_topic: "MMALS routing"
reviewed_at: "2026-08-26"
source_type: "arXiv preprint"
relevance: "very high"
evidence_quality: "medium"
related_tracks: ["MMALS", "Diderot", "AI routing"]
related_concepts: ["engineering prior", "routing baseline", "task type", "run-to-run variance", "cost-aware routing"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Across 21 routing methods on five benchmarks, the paper argues that much of the practical routing headroom can be captured by a simple, predefined task-type-to-model table rather than a learned per-query router.

## What the source actually provides

The author evaluates 14 models on 294 questions spanning seven task types and three languages, repeats the full 4,116 model-question matrix twice, and reports 5.37% run-to-run score changes. Under the stricter rule that a model must answer correctly in both runs, 29 questions remain improvable by routing; a static task-type table captures 21 of those, adding language captures two more. The fitted table answers 262/294 questions at reported cost $3.33 versus 245/294 at $7.69 for the best single model.

## Limitations and uncertainty

The static table is fitted and evaluated on the same 294 questions, with no holdout. Results are LLM-benchmark-specific, and task types are known labels rather than latent contexts. This is therefore a strong falsification lead, not evidence that learned routing is generally unnecessary.

## Consequence for current work

Reviewer inference: MMALS should include an explicit hierarchy of baselines: engineering-known rule/table -> simple contextual router -> learned geometric router -> exploratory/VoI refinement. Learned routing should only be credited for residual gain beyond what stable engineering descriptors already explain.

## Follow-up

Add a baseline experiment in which known problem/technique taxonomy is supplied as a prior or static routing table, then measure residual routing gain, cost, and discovery of exceptions on held-out contexts.

## Provenance note

All counts and benchmark claims above are source-derived. The proposed MMALS baseline hierarchy is reviewer inference.
