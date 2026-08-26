---
title: "Restoring Without Forgetting: Continual Learning Across Image Degradations"
canonical_url: "https://arxiv.org/abs/2608.23799"
author_or_publisher: "Alif Ashrafee; Bartosz Krawczyk (RIT)"
publication_date: "2026-08-24"
discovered_via: "Daily research watch / arXiv"
alert_topic: "MMALS inferred-context continual learning"
reviewed_at: "2026-08-26"
source_type: "arXiv preprint + code/benchmark"
relevance: "very high"
evidence_quality: "medium-high"
related_tracks: ["MMALS", "Diderot"]
related_concepts: ["domain-incremental learning", "prototype routing", "adapter isolation", "unknown task identity", "content-confound control"]
retention_verdict: "retain"
---

# Source note

## Central contribution

RwF provides a clean continual-learning baseline where new degradation-specific capabilities are added as isolated adapters and test-time domain identity is inferred without labels via prototype matching in a frozen backbone representation.

## What the source actually provides

The study builds a five-degradation benchmark over shared clean image content to avoid confounding degradation identity with dataset content, then evaluates sequential learning without replay. Prior adapters are frozen, eliminating parameter interference by construction. The router uses early-layer feature statistics and cosine prototype matching. Reported final average PSNR gains over naive sequential fine-tuning are 15.25 dB and 11.83 dB on two backbones; transfer to eleven real-degradation benchmarks reports 89.5% routing accuracy and a +0.94 dB oracle PSNR gap. Code, weights and benchmark are released.

## Limitations and uncertainty

Domains are still well-defined degradation operators encountered one at a time during training. The system does not discover when to create, merge or split latent regimes. Parameter isolation avoids forgetting but causes capacity growth. The synthetic benchmark may understate real context overlap.

## Consequence for current work

Reviewer inference: this is a strong MMALS baseline because it cleanly separates capability isolation from test-time context inference. Its content-confound control is especially important: routing accuracy must not come from incidental dataset identity. MMALS should compare against this simpler prototype-plus-isolated-host design before claiming value from richer geometry or dynamic host evolution.

## Follow-up

Reproduce a simplified analogue on controlled regime streams, then add overlap/composition and ask where prototype routing fails versus learned competence geometry.

## Provenance note

Performance figures and benchmark design are source-derived. The recommendation to use RwF as an MMALS baseline is reviewer inference.
