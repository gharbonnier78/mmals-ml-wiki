---
title: "Procedural Graphs: Self-Evolving Execution Structures for LLM Agents"
canonical_url: "https://arxiv.org/abs/2609.09153"
author_or_publisher: "Yuxing Lu, Yicheng Chen, Shanchan Wu, Sercan Ö. Arık"
publication_date: "2026-09-08"
discovered_via: "Daily research watch"
alert_topic: "agent memory and procedural knowledge"
reviewed_at: "2026-09-10"
source_type: "arXiv preprint"
relevance: "P0 — Chronicle / externalized procedural memory / agent governance"
evidence_quality: "medium-high: multi-dataset, multi-model evaluation with held-out validation gating; preprint"
related_tracks: ["MMALS Chronicle", "Diderot scientific harness", "agentic systems"]
related_concepts: ["procedural memory", "graph memory", "self-evolution", "held-out validation", "rejected-edit memory"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper externalizes procedural knowledge into a directed graph of (procedure, relation, procedure) triplets. At inference time only the local graph neighborhood is converted into situational guidance. Offline, an LLM refiner proposes graph edits by contrasting successful and failed trajectories, but edits are committed only if held-out validation performance is preserved or improved.

## What the source actually provides

Source-derived facts: the framework separates procedural structure from raw conversation history and model weights; localizes the current graph node; generates soft guidance rather than hard-coded action commands; and retains rejected graph edits so the refiner does not repeatedly propose known-bad changes. The authors report consistent gains over memory-based baselines across multiple datasets, task types, and LLMs. The paper states that graphs grown from a minimal skeleton can match or outperform hand-designed graphs and can repair a flawed expert prior.

## Limitations and uncertainty

Several components are bundled: graph representation, localization, guidance-model quality, refinement policy, held-out gating, and rejection memory. The causal source of gains therefore needs ablation. Held-out validation can also overfit if reused repeatedly, and success/failure trajectory contrast does not guarantee causal attribution of the procedural error.

## Consequence for current work

Reviewer inference: this is a strong Chronicle comparator because it suggests that useful long-horizon memory may be neither raw episodes nor text summaries, but validated procedural structure with explicit transitions and failure history. The most transferable element is the commit gate: learned procedural changes should remain proposals until an independent evidence gate accepts them.

## Follow-up

Compare Chronicle variants: episodic text retrieval, linear workflow memory, procedural graph without self-evolution, and procedural graph with validation-gated edits. Hold solver, data, and retrieval budget fixed and track both task success and regression caused by accepted edits.

## Provenance note

Framework and reported performance statements are source-derived. The Chronicle comparison and governance interpretation are reviewer inference.