---
title: "Calibration-Preserving Pruning: Compression as a Reliability Contract"
canonical_url: "https://arxiv.org/abs/2608.23744"
author_or_publisher: "Ibne Farabi Shihab, Adria Binte Habib, Anuj Sharma"
publication_date: "2026-08-24"
discovered_via: "Daily research watch"
alert_topic: "safe conformal calibration / model compression"
reviewed_at: "2026-08-30"
source_type: "arXiv preprint"
relevance: "high"
evidence_quality: "medium-high"
related_tracks: ["MMALS-CAL", "Diderot", "MLOps", "AI assurance"]
related_concepts: ["split conformal", "compression", "reliability contract", "prediction-set efficiency", "calibration independence"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper separates conformal validity from post-compression usefulness. For a fixed pruned classifier, an independent split-conformal calibration set restores standard marginal coverage under exchangeability; the pruning method then matters for how informative the valid prediction sets remain. Calibration-Preserving Pruning (CPP) explicitly targets nonconformity-score geometry so that valid post-pruning sets remain smaller.

## What the source actually provides

Source-derived facts: the method uses disjoint pruning, validation-selection, conformal-calibration, and test splits. On five-seed Qwen2.5-1.5B experiments at 50% sparsity, CPP-SparseGPT produces smaller conformal sets in 13 of 15 dataset-sparsity cells and higher accuracy in 11. The authors explicitly report matched controls showing that generic supervised-gradient information explains a substantial part of the gain; true-label CPP is not statistically resolved from a matched Wanda+SNIP control, while threshold-aware candidate-label CPP produces larger efficiency gains at explicit accuracy and offline-compute costs. Transfer diagnostics include RoBERTa-base and Llama-3-8B.

## Limitations and uncertainty

This is a preprint and claims are scoped to reliability-sensitive classification. Split-conformal validity remains the standard generic result and depends on exchangeability plus strict independence of the final calibration split from all pruning/model-selection decisions. Distribution shift, adaptive calibration reuse, or label-population changes can invalidate the guarantee. The paper itself warns against attributing all improvements to CPP-specific saliency because matched gradient baselines explain much of the effect.

## Consequence for current work

Reviewer inference: MMALS-CAL should treat any model/host transformation (pruning, quantization, adapter replacement, compression, retraining) as potentially changing calibration efficiency even when top-line accuracy appears stable. Release qualification should therefore separate (1) validity after fresh independent recalibration, (2) efficiency of the resulting prediction sets, and (3) task utility. This also reinforces strict provenance and isolation of calibration data in Diderot experiments.

## Follow-up

Add a compression/calibration regression experiment when a suitable MMALS host is transformed: freeze the transformed host, recalibrate on an untouched split, and compare coverage, set size, accuracy, and worst-regime behavior against the uncompressed host and a simple generic-gradient compression baseline.

## Provenance note

Method design, experimental comparisons, and stated validity assumptions are source-derived. The proposed MMALS-CAL release-contract interpretation is reviewer inference.