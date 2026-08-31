---
title: "When Muon Meets Task Interference: A Spectral Perspective on Continual Learning and Model Merging"
canonical_url: "https://arxiv.org/abs/2608.27518"
author_or_publisher: "Shangge Liu; Yuehan Yin; Yinghuan Shi; Lei Wang; Wenbin Li"
publication_date: "2026-08-27"
discovered_via: "Daily research watch / arXiv"
alert_topic: "continual learning; task interference; optimizer geometry"
reviewed_at: "2026-08-31"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high preprint: theory plus broad CL/model-merging experiments"
related_tracks: ["MMALS", "continual-learning", "Diderot-ML"]
related_concepts: ["catastrophic-forgetting", "task-interference", "spectral-norm", "optimizer", "model-merging"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper unifies catastrophic forgetting in continual learning and weight-interference errors in model merging as task interference: an update useful for one task changes outputs on another. It expresses the local interference through a layer-wise Frobenius interaction between parameter update and task Jacobian, then derives a bound isolating the spectral norm of the update as an optimizer-controllable factor. Muon is proposed as a useful optimizer because it regulates that norm by construction.

## What the source actually provides

Source-derived facts: the authors derive the interference formulation and spectral-norm upper bound; they report that per-mode analysis tracks a dominant empirical interference component. Replacing AdamW with Muon improves accuracy by up to 5.02 points on an eight-task model-merging benchmark across three CLIP backbones. In continual-learning experiments, Muon reportedly gives positive gains across ten class-incremental protocols, three task-incremental protocols and an 11-task MTIL benchmark.

## Limitations and uncertainty

This is a fresh preprint, not peer reviewed. The abstract reports broad positive results but does not establish that spectral-norm control is sufficient to prevent forgetting, nor that Muon dominates specialized CL mechanisms under all compute/hyperparameter budgets. The theoretical bound can be informative without being tight enough to act as a deployment guarantee. Optimizer-induced parameter geometry is also not the same object as MMALS representation/competence geometry.

## Consequence for current work

Reviewer inference: MMALS should treat the optimizer as a baseline control variable before attributing retention gains to richer routing, host isolation or memory mechanisms. A clean ablation is AdamW versus Muon under the same inferred-context router and host-update policy, measuring both average retention and cross-regime interference. This may reduce unnecessary architectural complexity if a meaningful fraction of forgetting can be mitigated at the optimizer level.

## Follow-up

Add Muon as an optimizer-control baseline to the next continual-learning ablation, with identical learning-rate tuning budget and explicit interference measurements. Do not promote it to a core mechanism unless gains survive matched tuning and recurrent-regime tests.

## Provenance note

Claims about equations, benchmarks and reported gains are source-derived. The proposed MMALS optimizer-control ablation and interpretation as a complexity-reduction baseline are reviewer inference.