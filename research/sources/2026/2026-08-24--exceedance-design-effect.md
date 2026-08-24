---
title: "The Exceedance Design Effect: Effective Sample Size for Thresholds under Clustering"
canonical_url: "https://arxiv.org/abs/2608.21262"
author_or_publisher: "Adam Noonan"
publication_date: "2026-08-21"
discovered_via: "Daily research watch"
alert_topic: "MMALS conformal calibration"
reviewed_at: "2026-08-24"
source_type: "arXiv preprint"
relevance: "very high"
evidence_quality: "medium-high"
related_tracks: ["MMALS-CAL", "AI testing", "Diderot"]
related_concepts: ["conformal prediction", "clustered calibration data", "effective sample size", "threshold reliability"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Shows that clustered/dependent calibration examples require a threshold-specific effective sample size rather than the usual mean-oriented design effect. For quantile thresholds used by conformal predictors, abstention gates and safety filters, the effective sample size depends on exceedance dependence at the chosen threshold.

## What the source actually provides

The paper derives a closed-form exceedance design effect and corresponding spread of realized coverage. The author reports that a released calibration set with 25,028 examples can have reliability comparable to only about 1,300 independent observations for the threshold of interest. Verification code and an archival version are linked by the paper.

## Limitations and uncertainty

This is a single-author preprint and has not yet passed peer review. The result addresses clustered dependence in threshold estimation, not all non-exchangeability or distribution shift. The practical value for MMALS depends on whether calibration data are actually clustered by episode, regime, subject, prompt, trace or Chronicle state.

## Consequence for current work

Source-derived fact: nominal calibration-set size can dramatically overstate the information available for a threshold when observations are dependent. Reviewer inference: MMALS-CAL should report a threshold-specific effective sample size or equivalent cluster-aware reliability audit at the actual deployment unit, rather than relying only on raw calibration count or a single generic ESS.

## Follow-up

Add a falsification experiment comparing IID-style conformal calibration with episode/regime-clustered resampling, and quantify how the claimed coverage changes when the same nominal N has different dependence structures.

## Provenance note

Facts above about the theorem, threshold dependence and reported 25,028-to-~1,300 reliability example are source-derived. The proposed MMALS calibration protocol is reviewer inference.