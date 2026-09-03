---
title: "What Is Worth Representing? Representational Empowerment for Continual Model Construction"
canonical_url: "https://arxiv.org/abs/2609.02322"
author_or_publisher: "Fei Dai, Hanqi Zhou, Alison Gopnik, Charley Wu"
publication_date: "2026-09-02"
discovered_via: "MMALS daily web research watch"
alert_topic: "continual learning / representation / memory"
reviewed_at: "2026-09-03"
source_type: "arXiv preprint"
relevance: "P0"
evidence_quality: "medium-high preprint: three experiments, matched simulations, ablation; not peer reviewed"
related_tracks: ["MMALS", "Diderot ML"]
related_concepts: ["continual model construction", "representation selection", "bounded memory", "value of information", "abstraction"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper reframes continual adaptation as deciding **what deserves to become part of the model at all**, not only how to estimate parameters inside a fixed representation. It proposes Representational Empowerment (RepEmp), which scores candidate reusable representational elements by how much they expand future capacity to model and plan under bounded resources.

## What the source actually provides

Source-derived facts: the authors formulate an environment-specific model plus a persistent cross-environment library of representational elements and realize this as a hierarchical Curator–Actor architecture. They report three experiments. In a causal-learning setting, human abstraction choices are better predicted by RepEmp than information-gain alternatives; matched simulations attribute structure recovery and transfer partly to RepEmp-guided construction; in an open-vocabulary planning setting, an LLM-supported curator builds more compact symbolic libraries that generalize better than baselines. An ablation removing RepEmp removes the reported benefits.

## Limitations and uncertainty

The paper is a fresh preprint. The tasks are deliberately structured and much smaller than open-ended continual-learning environments. The score may reward representations that are useful for the tested future task distribution while discarding information needed under unanticipated regimes. Human-model agreement is suggestive but is not proof of optimal machine representation design.

## Consequence for current work

Reviewer inference: this is directly relevant to MMALS Chronicle and host/regime construction. It suggests that the persistent state should not grow merely because a novelty detector fires; candidate regimes, descriptors, hosts or memory elements should earn persistence by demonstrated **future functional usefulness**. This provides a principled comparator to information gain, novelty and simple frequency/recency retention.

## Follow-up

Add a falsifiable MMALS ablation: novelty/information-gain retention vs functional-utility retention vs RepEmp-like future-capacity scoring, measured on transfer, memory growth, routing regret and retained task coverage.

## Provenance note

Claims about RepEmp, experimental design and reported results are source-derived. The proposed mapping to MMALS regime birth and Chronicle admission is reviewer inference.