---
title: "Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents"
canonical_url: "https://arxiv.org/abs/2609.05261"
author_or_publisher: "Jiazheng Sun, Boyu Yang, Binhao Yuan, Mingxuan Li, Xin Peng"
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: ""
reviewed_at: "2026-09-07"
source_type: "arXiv preprint"
relevance: "High: geometry-aware memory and experience consolidation"
evidence_quality: "Medium"
related_tracks: ["MMALS Chronicle", "geometry-aware routing", "agentic systems"]
related_concepts: ["execution traces", "spectral decomposition", "skill hierarchy", "transition dynamics", "verifier feedback"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Trace2Tower converts raw agent trajectories into a transition-aware graph and uses contrastive spectral decomposition to identify stable, success-associated behavioral modes, organizing them into a hierarchy of action templates, procedures and task strategies that are subsequently refined with verifier feedback.

## What the source actually provides

Source-derived facts: the method canonicalizes step-level interactions, builds a graph using semantic compatibility, transition dynamics and outcome evidence, then applies an EigenTrace-style spectral decomposition. Reported performance is 87.31% success on ALFWorld with 10.35 steps and 0.26 invalid actions, and 50.67% exact success on WebShop, with claimed gains over existing baselines in task mastery and context-efficient reuse.

## Limitations and uncertainty

The contribution bundles canonicalization, graph construction, spectral decomposition, hierarchy construction and verifier feedback, so causal attribution is weak without ablation. ALFWorld and WebShop are limited proxies for long-lived engineering learning. Spectral modes should not be equated with true latent regimes merely because they correlate with successful outcomes.

## Consequence for current work

Reviewer inference: this is a relevant geometry-aware Chronicle comparator because it operationalizes the idea that memory should preserve transition structure and outcome evidence rather than only semantic similarity. It is also a caution against prematurely assuming that spectral structure discovered in traces has semantic or causal meaning.

## Follow-up

Compare simple transition-count/prototype consolidation against spectral skill induction before considering a similar mechanism in MMALS; require ablations that isolate the value of spectral decomposition from graph construction and verifier feedback.

## Provenance note

Architecture and reported benchmark results are source-derived. The MMALS comparator role and caution about semantic interpretation are reviewer inference.