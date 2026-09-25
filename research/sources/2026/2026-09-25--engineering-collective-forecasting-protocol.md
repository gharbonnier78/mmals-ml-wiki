---
title: "Engineering Collective Forecasting — Study 0 protocol bootstrap"
canonical_url: "https://github.com/gharbonnier78/engineering-collective-forecasting/commit/c8a35166870d578efade26eef0eaaef9f5a5251e"
author_or_publisher: "Guillaume Harbonnier"
publication_date: "2026-09-25"
source_type: "project protocol / research design"
reviewed_at: "2026-09-25"
relevance: "P0"
evidence_quality: "protocol only; no empirical Study 0 evidence yet"
related_tracks: ["engineering collective forecasting", "uncertainty", "evidence-guided engineering"]
related_concepts: ["Forecast Contract", "collective forecasting", "prediction market", "Brier score", "forecast calibration"]
retention_verdict: "retain as project-local formalism"
---

# Source note

## Central contribution

The repository proposes a shadow-mode Study 0 for evaluating collective forecasting in engineering without letting forecasts influence operational decisions. It introduces a versioned **Forecast Contract** to prospectively fix the event, time bounds, resolution rule, authoritative evidence, resolver and safeguards; it preserves independent pre-market forecasts as a baseline and defines a paired Brier-score comparison at the resolved-contract / operational-cluster level.

## What the source supports for Diderot

- a concrete engineering application of probabilistic forecasting and scoring;
- the project-local Forecast Contract formalism;
- the distinction between prediction evidence and decision authority;
- the need to preserve simple aggregation as a baseline;
- a pedagogically useful bridge from distributed human knowledge to auditable probabilistic evidence.

## Boundary

The repository is at protocol stage. It contains **no empirical result demonstrating that prediction markets improve engineering forecasts**. Forecast Contract is project terminology, not an external standard. Future links to probabilistic ML, evidence contracts or POMDP-style evidence acquisition remain extensions rather than prerequisites.

## Provenance

Primary PR at bootstrap: https://github.com/gharbonnier78/engineering-collective-forecasting/pull/1  
Immutable reviewed-target head for this Diderot update: https://github.com/gharbonnier78/engineering-collective-forecasting/commit/c8a35166870d578efade26eef0eaaef9f5a5251e
