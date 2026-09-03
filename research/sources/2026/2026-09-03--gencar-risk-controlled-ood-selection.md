---
title: "GenCAR: Generative Counterfactual Alignment with Risk-Controlled Selection for Out-of-Distribution Recommendation"
canonical_url: "https://arxiv.org/abs/2609.02162"
author_or_publisher: "Qianqian Wang, Yunshan Li, Jiawen Zeng, Wenwu Gong, Lili Yang"
publication_date: "2026-09-02"
discovered_via: "MMALS daily web research watch"
alert_topic: "safe conformal calibration / OOD decision"
reviewed_at: "2026-09-03"
source_type: "arXiv preprint"
relevance: "P0"
evidence_quality: "medium-high preprint: finite-sample guarantees plus empirical FDR audits; domain-specific"
related_tracks: ["MMALS", "Diderot ML", "Test Authority"]
related_concepts: ["conformal p-values", "false discovery rate", "distribution shift", "counterfactual selection", "dependence-aware calibration"]
retention_verdict: "retain"
---

# Source note

## Central contribution

GenCAR combines OOD counterfactual candidate generation with statistically controlled set selection. Instead of merely ranking candidates, it targets false-discovery control of the served set using conformal p-values and multiple-testing procedures.

## What the source actually provides

Source-derived facts: GenCAR fixes a stable-preference representation while intervening on environmental factors, filters generated proposals using preference anchors and a trust radius, then applies conformal p-values with Benjamini–Hochberg selection. The authors state a finite-sample, distribution-free proxy-label FDR guarantee under exchangeability and positive regression dependence, and a Benjamini–Yekutieli guarantee under arbitrary dependence. Experiments audit realized false discovery proportions across several recommendation benchmarks and report improved OOD candidate recovery.

## Limitations and uncertainty

The guarantee concerns proxy-label FDR, not true downstream harm or sequential control risk. Exchangeability and the meaning of the proxy labels remain substantive assumptions. Recommendation serving is also simpler than an evolving MMALS environment with inferred regimes, dependent trajectories and delayed consequences.

## Consequence for current work

Reviewer inference: this is relevant to MMALS-CAL because it broadens the calibration target from single prediction coverage toward **set-level error control under selection and dependence**. For candidate hosts/actions/regime hypotheses, the right question may sometimes be how many admitted candidates are false rather than whether one interval covers a scalar target.

## Follow-up

Prototype a small CAL experiment comparing marginal coverage, selective risk and FDR-style control over candidate host/action sets under controlled regime shift and correlated candidates.

## Provenance note

The conformal/multiple-testing construction and reported guarantees are source-derived. Applying FDR-style control to MMALS candidate regimes or actions is reviewer inference.