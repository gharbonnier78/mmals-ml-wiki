---
title: "HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews"
canonical_url: "https://arxiv.org/abs/2609.03580"
author_or_publisher: "Tzu-Ling Lin et al."
publication_date: "2026-09-04"
discovered_via: "arXiv daily watch"
alert_topic: "scientific review / hallucination detection"
reviewed_at: "2026-09-05"
source_type: "EMNLP Findings 2026 paper and benchmark"
relevance: "high"
evidence_quality: "high"
related_tracks: ["Diderot", "scientific harness", "AI testing"]
related_concepts: ["peer review", "source grounding", "hallucination detection", "claim verification"]
retention_verdict: "retain"
---

# Source note

## Central contribution

HalluPeer builds a peer-review-specific benchmark for detecting, classifying and localizing unsupported claims in scientific reviews, where valid criticism must be distinguished from hallucinated criticism grounded in long technical papers.

## What the source actually provides

Accepted to EMNLP Findings 2026. The benchmark contains aligned paper/review/hallucination-injected-review data and a taxonomy derived for peer-review failure modes. Experiments cover about 12K papers and 38K reviews. Existing detectors struggle to separate hallucinations from legitimate critique, and the authors report that HalluPeer-defined patterns also appear in authentic reviews. A project repository is released.

## Limitations and uncertainty

Injected hallucinations may not perfectly match organically generated reviewer errors, and authentic-review labeling is difficult because disagreement can reflect legitimate scientific interpretation rather than factual fabrication. The benchmark evaluates detection, not the overall quality of peer review.

## Consequence for current work

Source-derived fact: generic hallucination detection is insufficient for scientific review because valid critique and unsupported claims can be linguistically similar. Reviewer inference: Diderot reviewer outputs should retain explicit claim-to-source links and classify unsupported assertions separately from methodological disagreement; reviewer confidence alone is not enough.

## Follow-up

Use HalluPeer's taxonomy as a candidate cross-check against the scientific-harness reviewer form and identify which hallucination classes are already prevented by source-line citation requirements versus which still need explicit review controls.

## Provenance note

Benchmark scale and detector findings are source-derived. The proposed Diderot integration is reviewer inference.
