---
title: "COINS: Any-Stage-Valid and Utility-Oriented Sequential Conformal Prediction"
canonical_url: "https://arxiv.org/abs/2609.07112"
author_or_publisher: "Wangcheng Li, Nan Qiao, Xu Guo, Wenguang Sun"
publication_date: "2026-09-07"
discovered_via: "Daily research watch"
alert_topic: "safe conformal calibration"
reviewed_at: "2026-09-10"
source_type: "arXiv preprint"
relevance: "P0 — sequential conformal calibration and decision-time stopping"
evidence_quality: "medium-high: finite-sample theory under exchangeability plus simulations and dermatology application"
related_tracks: ["MMALS-CAL", "GO-ED-POMDP", "Diderot ML"]
related_concepts: ["conformal prediction", "sequential inference", "any-stage validity", "process utility", "stopping decisions"]
retention_verdict: "retain"
---

# Source note

## Central contribution

COINS treats a sequence of intermediate prediction sets as the inferential object rather than calibrating only a terminal output. It defines any-stage validity so that inspecting or stopping at an intermediate stage does not silently invalidate coverage, then optimizes stagewise allocation against process-level utility.

## What the source actually provides

Source-derived facts: the paper develops a structural construction for any-stage-valid conformal sequences and a COINS procedure that allocates a shared finite-sample rejection-count budget across surviving augmented observations. Under exchangeability it claims finite-sample any-stage validity and prediction sets no larger than matched Bonferroni counterparts at each stage. Vopt-COINS learns stage allocation for a specified process-level utility; branchwise and localized extensions address heterogeneous acquisition paths. Simulations and a dermatology diagnosis application are reported.

## Limitations and uncertainty

The guarantee is conditional on exchangeability and on the stated construction. It does not by itself cover non-stationary inferred regimes, adaptive policies that alter data collection, or arbitrary sequential dependence. Utility optimization can also encourage unnecessary sophistication if a simpler fixed policy already meets the engineering decision need.

## Consequence for current work

Reviewer inference: this is directly relevant to MMALS-CAL because an MMALS episode may repeatedly observe, recalibrate, stop, abstain, or request further evidence. Calibration should therefore be qualified across the whole inspected sequence, not only at a final decision. A useful baseline is terminal conformal calibration versus any-stage calibration under adaptive stopping.

## Follow-up

Add an MMALS-CAL experiment where identical episodes are evaluated under fixed stopping, confidence-triggered stopping, and externally interrupted stopping; verify whether nominal coverage survives each policy and compare efficiency against Bonferroni-style protection.

## Provenance note

All methodological and empirical claims above are source-derived from the arXiv abstract. The mapping to MMALS-CAL and the proposed stopping-policy experiment are reviewer inference.