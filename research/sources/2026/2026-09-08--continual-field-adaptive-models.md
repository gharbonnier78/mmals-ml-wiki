---
title: "Continual Field-Adaptive Models (CFAMs) for Post-Deployment Physical AI"
canonical_url: "https://arxiv.org/abs/2609.04552"
author_or_publisher: "Amarjot Singh et al."
publication_date: "2026-09-03"
discovered_via: "arXiv daily watch"
alert_topic: "continual learning / robotics"
reviewed_at: "2026-09-08"
source_type: "arXiv preprint"
relevance: "very high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "continual learning", "robotics", "Chronicle"]
related_concepts: ["fast-slow learning", "gradient-free adaptation", "competence memory", "verified near-OOD experience", "catastrophic forgetting"]
retention_verdict: "retain"
---

# Source note

## Central contribution

CFAM proposes post-deployment continual adaptation using a frozen slow component plus a fast-learning, gradient-free Capsule Field that stores one-shot competence updates. The design explicitly separates stable pretrained competence from field-acquired experience and limits its claim to bounded near-OOD adaptation rather than open-world novelty.

## What the source actually provides

Source-derived facts: CFAM is evaluated across five embodiments (manipulator, quadruped, humanoid, quadrotor, off-road vehicle). The paper compares against pi0, CogACT and SpatialVLA on the same in-house multi-embodiment data. It reports reaching a standard-policy operating point with 40% of the prior-training data, a +13.9 percentage-point action-success gain after autonomously capturing verified near-OOD cases, and -0.5 percentage-point backward transfer in sequential simulation versus -11.4 for LoRA.

The architecture has separate Sensor, Reasoning and Action cortices in its slow component; field experience is installed as Competence Capsules without gradient updates.

## Limitations and uncertainty

The central dataset is in-house, so independent reproducibility and external validity remain uncertain. The comparison bundles architecture, representation, update mechanism and experience-selection policy. Open-world novelty is explicitly outside scope. The reported forgetting advantage over LoRA does not establish superiority over the broader continual-learning literature, especially replay, adapter-routing or task-free methods under matched budgets.

## Consequence for current work

Reviewer inference: CFAM is a strong external comparator for MMALS because it operationalizes a principle already emerging in the roadmap: preserve a stable base, admit only verified field experience, and adapt outside the main weights. The most important comparison is not architecture-to-architecture but **where plasticity lives**: model weights, external competence memory, or a routed hybrid.

## Follow-up

Add CFAM-style fast/slow external competence as a benchmark family for MMALS. Compare `full/LoRA update`, `frozen base + external competence`, and `MMALS inferred-context routing + external competence` under matched adaptation samples, compute and forgetting metrics. Require separate evaluation of near-OOD versus truly novel regimes.

## Provenance note

Reported metrics and scope restrictions are source-derived. Mapping CFAM to the MMALS fast/slow and Chronicle architecture is reviewer inference.
