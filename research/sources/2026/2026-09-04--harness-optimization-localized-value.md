---
title: "Where Does Harness-Optimization Value Live? Localized Gains and the Budget-Splitting Trap in Self-Evolving LLM Agents"
canonical_url: "https://arxiv.org/abs/2609.02889"
author_or_publisher: "Michael Nguyen et al."
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: "agentic systems / harness optimization"
reviewed_at: "2026-09-05"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["Diderot", "MMALS", "agentic systems", "scientific harness"]
related_concepts: ["credit assignment", "localized adaptation", "budget allocation", "harness evolution"]
retention_verdict: "retain"
---

# Source note

## Central contribution

HARNESSEVO decomposes an agent harness into role, task strategy, tool/format rules, and reflection/control, then measures where optimization value actually resides rather than evolving the harness as one flat prompt.

## What the source actually provides

On ALFWorld with a frozen 7B backbone and iso-budget comparison, overall HARNESSEVO success is not significantly above stock or flat-string evolution (0.657 vs 0.642/0.642). Leave-one-in attribution localizes nearly all useful gain to reflection/control (+0.119), while other slots are individually null. Uniformly splitting 64 rollouts across four slots can starve each search below its effective floor; concentrating budget on the high-credit control slot reaches 0.761. WebShop shows no such gain, supporting task contingency rather than a universal effect.

## Limitations and uncertainty

Two environments and one frozen backbone do not establish generality. The attribution depends on the chosen slot decomposition and optimizer. Search-floor effects may differ substantially with model scale, task structure, or optimizer design.

## Consequence for current work

Source-derived fact: useful adaptation can be highly localized and uniform search-budget splitting can be harmful. Reviewer inference: for MMALS/Diderot, credit assignment should precede structured adaptation; do not add modules or allocate exploration budget uniformly before demonstrating where residual error or control value actually lives.

## Follow-up

Use as a comparator for selective adaptation: global harness change vs component-localized change vs evidence-guided budget allocation.

## Provenance note

All numeric results above are source-derived. The proposed MMALS/Diderot experimental consequence is reviewer inference.
