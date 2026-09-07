---
title: "Beyond Stationarity in Time Series: Discovering Causal Structures and Latent Regimes via Markov Blankets"
canonical_url: "https://arxiv.org/abs/2609.05150"
author_or_publisher: "Lei Zan, Charles K. Assaad, Emilie Devijver, Eric Gaussier"
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: ""
reviewed_at: "2026-09-07"
source_type: "peer-reviewed workshop paper / arXiv preprint"
relevance: "High: inferred-context continual learning and regime identification"
evidence_quality: "Medium-high"
related_tracks: ["MMALS", "continual learning", "geometry/context inference"]
related_concepts: ["latent regimes", "Markov blankets", "causal discovery", "non-stationarity"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper introduces RCBNB-MB, an iterative method that jointly segments non-stationary time series into latent regimes and discovers a causal graph within each regime, using Markov blankets to preserve predictive information while increasing robustness to causal-discovery errors.

## What the source actually provides

Source-derived facts: the authors define regimes as subsets of time points with stable causal structure; provide theoretical recovery guarantees under stated assumptions; and evaluate on simulated data with known ground truth plus real IT-monitoring data. The abstract reports systematic gains over baseline methods for both regime detection and associated causal-graph recovery. The work is accepted at the 11th AALTD Workshop at ECML PKDD 2026.

## Limitations and uncertainty

The guarantees depend on causal and regime assumptions that may not hold in MMALS streams. Segmentation quality can also be confounded with causal-model misspecification. A recovered latent regime should not automatically be interpreted as a semantically meaningful or causal operating mode.

## Consequence for current work

Reviewer inference: this is a valuable comparator for MMALS inferred-context routing because it tests a stronger hypothesis than generic drift detection: whether regime changes can be inferred from changes in local causal structure. It supports an experimental ladder from simple drift/prototypes to causal-regime inference before introducing more elaborate learned geometric routers.

## Follow-up

Add RCBNB-MB or a simplified Markov-blanket regime detector as a comparator in the inferred-context evaluation plan, with explicit tests for false regime births under causal-model misspecification.

## Provenance note

Method, acceptance status, guarantees and reported empirical comparisons are source-derived. The proposed MMALS comparator and falsification test are reviewer inference.