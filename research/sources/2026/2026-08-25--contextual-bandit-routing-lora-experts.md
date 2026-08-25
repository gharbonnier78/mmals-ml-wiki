---
title: "Contextual Bandit Routing for LoRA Experts"
canonical_url: "https://doi.org/10.53941/tai.2026.100012"
author_or_publisher: "Miavaka Voninahitra Ambinintsoa Rakotovao Valisoa; Hobihery Matio Robinson / Transactions on Artificial Intelligence"
publication_date: "2026-08-24"
discovered_via: "Daily research watch"
alert_topic: "MMALS routing / continual adaptation"
reviewed_at: "2026-08-25"
source_type: "Peer-reviewed journal article"
relevance: "High"
evidence_quality: "Medium-high"
related_tracks: ["MMALS", "Diderot ML"]
related_concepts: ["contextual bandits", "LoRA experts", "routing", "exploration-exploitation", "online adaptation"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper formulates LoRA-expert selection as an online contextual-bandit problem rather than a fixed heuristic or offline learned router. EXP4-LoRA combines context-aware reward estimation with exploration/exploitation, allowing routing to adapt from correctness feedback without explicit domain labels.

## What the source actually provides

Source-derived facts: the published article reports experiments on mixed-domain MMLU with Gemma-2-2B and four specialist LoRA adapters, plus replication on Phi-3-mini. EXP4-LoRA reports 80.1% accuracy after 2000 steps, +4.1 points over EXP3, reaching a 70% threshold in 420 versus 1800 steps; LinTS reaches 79.3%. The article explicitly states that binary correctness feedback is required and also studies proxy rewards. It reports substantial routing overhead, about one base forward-pass latency before caching optimizations.

Reviewer inference: this is a strong comparator for MMALS because it operationalizes a natural middle ground between engineering-fixed routing and a fully learned latent-context router.

## Limitations and uncertainty

The expert set is predefined, the benchmark domains are known in construction, and feedback is much cleaner than many long-horizon MMALS settings. The journal is peer reviewed but relatively new, and the reported advantages over Thompson sampling are modest. The results do not establish autonomous regime discovery.

## Consequence for current work

Add a baseline ladder: engineering rule / static prior -> contextual bandit routing -> richer inferred-context routing. Measure whether extra representation and routing complexity buys statistically defensible regret reduction under equal exploration and compute budgets.

## Follow-up

Reproduce a small contextual-bandit router over predefined MMALS hosts before testing learned geometric routing. Include epsilon/exploration and regret curves, not only final accuracy.

## Provenance note

Performance figures and method description are source-derived. The proposed use as an MMALS baseline and engineering-prior comparator is reviewer inference.
