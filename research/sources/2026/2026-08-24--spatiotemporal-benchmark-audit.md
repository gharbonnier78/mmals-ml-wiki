---
title: "A Critical Audit of Spatiotemporal Forecasting Benchmark Datasets and Baselines"
canonical_url: "https://arxiv.org/abs/2608.20980"
author_or_publisher: "Kenneth Martin et al."
publication_date: "2026-08-21"
discovered_via: "Daily research watch"
alert_topic: "Benchmark quality / geometry-aware ML"
reviewed_at: "2026-08-24"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS harness", "Diderot", "AI testing"]
related_concepts: ["benchmark audit", "strong simple baselines", "structural bias", "spatiotemporal forecasting"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Audits widely used spatiotemporal forecasting benchmarks and shows that simple spatially-unaware classical models can remain unexpectedly competitive, while dataset preprocessing such as first-order differencing can introduce structural biases that weaken the discriminative value of benchmark comparisons.

## What the source actually provides

The authors analyze commonly used datasets including Chickenpox, PedalMe, WikiMaths, METR-LA and PEMS-BAY using classical time-series methods and statistical diagnostics of spatial and temporal correlation. They report that the analysis explains why simple baselines can rival GNN-based methods and use the findings to motivate a simple hybrid model.

## Limitations and uncertainty

This is an arXiv preprint, not yet peer reviewed. Its conclusions concern a specific family of spatiotemporal forecasting datasets and do not imply that graph or geometry-aware models are broadly unnecessary. The impact depends on protocol details and whether stronger baseline tuning is reproduced independently.

## Consequence for current work

Source-derived fact: benchmark structure can make sophisticated methods appear stronger or weaker for reasons unrelated to the claimed mechanism. Reviewer inference: MMALS benchmark design should explicitly test whether simple non-geometric, non-routing baselines already explain apparent gains before attributing value to inferred contexts, manifolds or specialized hosts.

## Follow-up

Add a benchmark-audit checklist to MMALS experiments: characterize dataset autocorrelation, preprocessing-induced shortcuts, simple baselines, oracle headroom and whether the benchmark can actually discriminate the mechanism under test.

## Provenance note

Dataset and baseline findings are source-derived. The proposed MMALS harness implications are reviewer inference.