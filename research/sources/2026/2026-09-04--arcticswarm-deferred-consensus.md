---
title: "ArcticSwarm: Deferring Early Consensus in Long-Horizon Multi-Agent Research"
canonical_url: "https://arxiv.org/abs/2609.01870"
author_or_publisher: "Soyoung Yoon et al."
publication_date: "2026-09-01"
discovered_via: "Daily research watch"
alert_topic: "multi-agent research"
reviewed_at: "2026-09-04"
source_type: "arXiv preprint"
relevance: "High"
evidence_quality: "Medium-high"
related_tracks: ["Diderot", "scientific harness", "agentic systems", "MMALS"]
related_concepts: ["premature consensus", "gated isolation", "evidence integration", "commitment boundaries"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Separates evidence gathering from evidence integration in long-horizon multi-agent research, using gated isolation so selected subagents cannot prematurely converge on peers' hypotheses, plus structured review at commitment boundaries.

## What the source actually provides

Source-derived facts: on BrowseComp-Plus, ArcticSwarm with Qwen 3.5-27B reports 82.6%, compared with 78.8% without gated isolation, 74.5% with structured review also disabled, and 70.6% for aligned MiroFlow runs. On live-web BrowseComp, the paper reports 73.6% with GPT-5 versus 63.4% for MiroFlow and a reported provider system score of 54.9%.

## Limitations and uncertainty

Fresh preprint and benchmark-dependent. Multi-agent research benchmarks do not establish scientific correctness, and gains may depend on prompts, search budgets, tool access, and model choice. Isolation can also duplicate work and increase cost.

## Consequence for current work

Reviewer inference: the scientist/reviewer harness should preserve hypothesis diversity during evidence collection and delay cross-agent convergence until explicit evidence-review boundaries. Shared Chronicle access should not automatically mean unrestricted read access to all partial hypotheses during exploration.

## Follow-up

Test independent evidence-gathering branches versus fully shared scratch state in one Diderot research task, holding search budget constant. Measure hypothesis diversity, duplicated effort, factual accuracy, and final evidence quality.

## Provenance note

Architecture description and benchmark figures are source-derived. Mapping to Diderot's scientist/reviewer process and Chronicle read policies is reviewer inference.
