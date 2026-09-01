---
title: "Planning and Acting in Partially Observable Stochastic Domains"
canonical_url: "https://doi.org/10.1016/S0004-3702(98)00023-X"
author_or_publisher: "Leslie Pack Kaelbling, Michael L. Littman, Anthony R. Cassandra"
publication_date: "1998-05-01"
source_type: "peer-reviewed journal article"
reviewed_at: "2026-09-01"
relevance: "P0"
evidence_quality: "high for foundational POMDP definitions and planning formalism"
related_tracks: ["machine learning foundations", "GO-ED-POMDP", "world-model research"]
related_concepts: ["POMDP", "belief state", "policy", "value function", "planning", "partial observability"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Kaelbling, Littman and Cassandra present the classical POMDP formulation for choosing actions when the underlying state is not directly observable. The paper treats a belief distribution over hidden state as the information state on which planning can operate and discusses optimal policies, value functions and approximate solution methods.

## What the source supports for Diderot

Source-derived concepts used in this teaching path:

- hidden system state is distinguished from observations;
- the agent can maintain a posterior belief over hidden state from action-observation history;
- a policy maps the current information state to an action rather than prescribing one immutable action sequence in advance;
- multi-step value depends on future rewards/costs under future observations and future actions;
- partial observability can make information-gathering behavior valuable because observations affect later choices.

## Boundary

This source does not define MMALS, GO-ED-POMDP or a modern machine-learning `world model`. Diderot uses it as authority for foundational POMDP language only. Project-specific phrases such as `contingent sufficiency` remain local research refinements unless independently anchored in broader literature.

## Pedagogical consequence

The Diderot pathway should not jump directly from `belief state` to a single next action. It should expose the intermediate distinction between action, policy and finite-horizon value, then show why an information-gathering action can be useful even when its immediate reward is negative.
