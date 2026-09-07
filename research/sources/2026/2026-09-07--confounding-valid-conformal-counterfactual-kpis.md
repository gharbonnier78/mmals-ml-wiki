---
title: "Confounding-Valid Conformal Inference for Counterfactual KPIs in Wireless Networks"
canonical_url: "https://arxiv.org/abs/2609.05073"
author_or_publisher: "Abdessamed Qchohi, Jessica Moysen Cortes, Matteo Zecchin"
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: ""
reviewed_at: "2026-09-07"
source_type: "arXiv preprint"
relevance: "Very high: safe conformal calibration and counterfactual engineering decisions"
evidence_quality: "Medium-high"
related_tracks: ["MMALS-CAL", "GO-ED-POMDP", "Test Authority"]
related_concepts: ["conformal inference", "hidden confounding", "counterfactual KPIs", "randomized telemetry"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper proposes Confounding-Valid Counterfactual Conformal Inference (CV-CCI), combining abundant but potentially confounded observational telemetry with scarce randomized telemetry so counterfactual prediction sets can retain finite-sample coverage under arbitrary hidden confounding while remaining more informative than methods based only on randomized data.

## What the source actually provides

Source-derived facts: logged controller telemetry may omit variables used by the controller and thereby invalidate counterfactual guarantees. CV-CCI uses the GESPI principle to exploit observational data for efficiency while using randomized data for validity. Experiments on two radio-access-network control tasks report valid coverage under hidden confounding and more efficient prediction sets than confounding-valid baselines.

## Limitations and uncertainty

The guarantee depends on the availability and validity of randomized telemetry and on the paper's formal setup. Two RAN tasks do not establish robustness for sequential MMALS decisions, adaptive data collection, inferred regimes, or changing policies.

## Consequence for current work

Reviewer inference: MMALS-CAL should explicitly distinguish calibration under ordinary exchangeability from calibration when action-selection policy creates confounding. This paper gives a concrete route for combining operational telemetry with a smaller deliberately randomized evidence stream rather than treating all logged experience as equally valid counterfactual evidence.

## Follow-up

Add a hidden-confounding stress test to the CAL evaluation plan: compare observational-only conformal, randomized-only conformal, and mixed confounding-valid calibration under policy-driven selection bias.

## Provenance note

The method, finite-sample claim and RAN experiments are source-derived. The proposed MMALS stress test and telemetry policy are reviewer inference.