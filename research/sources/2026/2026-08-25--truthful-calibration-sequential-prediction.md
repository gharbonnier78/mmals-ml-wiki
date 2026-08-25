---
title: "Truthful Calibration Measures for Sequential Prediction"
canonical_url: "https://arxiv.org/abs/2608.21348"
author_or_publisher: "Anagha Gokul; Jason Hartline; Lunjia Hu; Jonathan Ullman; Yifan Wu"
publication_date: "2026-08-21"
discovered_via: "Daily research watch"
alert_topic: "Calibration / sequential prediction"
reviewed_at: "2026-08-25"
source_type: "arXiv manuscript"
relevance: "High"
evidence_quality: "High-theory / preprint"
related_tracks: ["MMALS", "Diderot ML"]
related_concepts: ["calibration", "sequential prediction", "truthfulness", "online learning"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper proves that exact truthfulness of a calibration measure is incompatible with completeness and soundness for sequential binary prediction, even with independent outcomes, then constructs approximately truthful alternatives with stronger guarantees than prior work.

## What the source actually provides

Source-derived facts: the contribution is theoretical. It gives an impossibility result for exact truthfulness and two reductions producing additive and multiplicative approximate-truthfulness guarantees; the multiplicative construction approaches exact truthfulness as sequence length increases under the stated asymptotics.

Reviewer inference: for MMALS this is less about conformal prediction directly and more about the design of sequential calibration metrics. A metric can create incentives or pathological optimization behavior; calibration quality itself should not be treated as a neutral scalar objective.

## Limitations and uncertainty

The setting is sequential binary probabilistic prediction, not conformal set prediction or latent-regime routing. The practical effect on MMALS-CAL is therefore indirect. No empirical MMALS-like deployment claim follows from the theorem.

## Consequence for current work

When evaluating adaptive calibration or router confidence over time, avoid optimizing a single calibration score blindly. Report operational coverage/risk plus calibration diagnostics, and test whether adaptation policies can game the chosen metric without improving decision quality.

## Follow-up

Add a metric-gaming falsification case to a small sequential CAL benchmark: optimize an adaptive policy against one calibration score and audit with independent coverage/risk measures.

## Provenance note

The impossibility and approximate-truthfulness constructions are source-derived. The proposed metric-gaming audit for MMALS is reviewer inference.
