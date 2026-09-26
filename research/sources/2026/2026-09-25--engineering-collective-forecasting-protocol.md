---
title: "Engineering Collective Forecasting — Study 0A/0B revised protocol"
canonical_url: "https://github.com/gharbonnier78/engineering-collective-forecasting/commit/a936054a68b2fd11918000c47ddc751a19ffc520"
author_or_publisher: "Guillaume Harbonnier"
publication_date: "2026-09-25"
updated_at: "2026-09-26"
source_type: "project protocol / research design"
reviewed_at: "2026-09-26"
relevance: "P0"
evidence_quality: "protocol only; bootstrap received PARTIAL ACCEPT and revised protocol awaits rereview; no empirical Study 0 evidence"
related_tracks: ["engineering collective forecasting", "uncertainty", "evidence-guided engineering"]
related_concepts: ["Forecast Contract", "collective forecasting", "meta-prediction", "prediction market", "Brier score", "forecast calibration", "Brier diversity identity"]
retention_verdict: "retain as project-local formalism and protocol history"
---

# Source note

## Revision history

The original bootstrap at commit `c8a3516` centered Study 0 on a prediction-market-versus-private-mean contrast. Independent review returned **PARTIAL ACCEPT**: the scaffold was accepted, but G1 was not released.

The revised protocol at commit `a936054a68b2fd11918000c47ddc751a19ffc520` applies the minimum-sufficient-mechanism critique before any Study 0 outcomes exist.

## Central contribution of the revised protocol

Study 0 is now split into:

- **Study 0A:** a dry Forecast Contract funnel with no participants or market, testing whether real engineering events can be prospectively specified and later resolved cleanly;
- **Study 0B:** private same-time forecasting against institutional references: historical base rate, accountable owner's private probability, official status, and independent participant forecasts plus meta-predictions.

No collective aggregate is exposed before resolution. Prediction markets are moved to a later residual-mechanism study because visible market prices can perturb actors who influence the forecasted outcome.

The Forecast Contract is revised to include not only event and resolution semantics but also institutional references, cluster/timing, data-custody and visibility safeguards.

## What the source supports for Diderot

- a concrete engineering application of private probabilistic forecasting and proper scoring;
- the project-local Forecast Contract formalism;
- the distinction between prediction evidence and decision authority;
- a methodological example of minimum-sufficient-mechanism reasoning;
- a bridge to meta-prediction/shared-information aggregation;
- an explicit example of why prediction markets may be interventions rather than passive sensors.

## Boundary

The repository remains at protocol stage. It contains **no empirical result** showing that private crowds, meta-prediction aggregation, or prediction markets outperform institutional engineering forecasts.

Forecast Contract remains project terminology, not an external standard. The fixed meta-belief transform in the protocol is a project implementation inspired by published work, not an exact reproduction of a cited algorithm.

## Provenance

- Primary PR: https://github.com/gharbonnier78/engineering-collective-forecasting/pull/1
- Original reviewed bootstrap: https://github.com/gharbonnier78/engineering-collective-forecasting/commit/c8a35166870d578efade26eef0eaaef9f5a5251e
- Revised protocol head used by this Diderot update: https://github.com/gharbonnier78/engineering-collective-forecasting/commit/a936054a68b2fd11918000c47ddc751a19ffc520
