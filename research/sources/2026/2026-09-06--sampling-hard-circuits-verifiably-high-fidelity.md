---
title: "Sampling hard circuits with verifiably high fidelity"
canonical_url: "https://arxiv.org/abs/2607.25941"
author_or_publisher: "Simon Martiel et al."
publication_date: "2026-07-28"
discovered_via: "Google Alerts -> secondary quantum coverage -> primary arXiv paper"
alert_topic: "Informatique quantique"
reviewed_at: "2026-09-06"
source_type: "arXiv preprint / primary experimental quantum-computing report"
relevance: "high for quantum engineering and evidence/verification engineering; adjacent rather than core MMALS"
evidence_quality: "medium-high: primary experimental report with explicit circuit construction, error-detection mechanism, statistical fidelity certificate and public experimental artifacts; still a preprint and device-dependent"
related_tracks: ["quantum engineering", "Test Authority", "Diderot", "evidence engineering"]
related_concepts: ["quantum advantage", "verification", "error correction", "fidelity certification", "evidence authority"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper proposes structured sampling circuits that try to combine three properties that are usually in tension: computational hardness, quantum error suppression, and a verifiable certificate of execution fidelity. The important engineering contribution is not merely a speed claim; it is the attempt to make a classically hard quantum computation carry an independently interpretable statistical lower bound on how faithfully it was executed.

## What the source actually provides

Source-derived facts: the current arXiv version (v3, revised 2026-09-02) describes a 64-qubit, depth-73 Clifford circuit doped with 314 T gates. The computation is encoded using 76 physical qubits in spacetime codes. After syndrome post-selection, the authors report an effective gate-error suppression of about 10x and a lower bound of 0.349 on output-state fidelity at 95% confidence. The certificate is explicitly described as device-dependent, but the authors argue that it requires weaker noise assumptions than common fidelity-proxy benchmarks. The paper gives a structured circuit construction intended to retain complexity-theoretic hardness while enabling error-detected certification.

The related IBM communication amplified an earlier experimental configuration and characterized the work as evidence of quantum advantage. That corporate characterization is not treated here as independent proof; the retained source is the primary paper.

## Limitations and uncertainty

The result is a benchmark-style sampling computation rather than a useful application workload. The fidelity certificate is device-dependent and relies on the specific circuit/code construction and post-selection procedure. The claim of practical classical intractability depends on the state of classical simulation methods and associated assumptions; it should not be generalized to broad quantum superiority. Post-selection also means that the engineering cost of rejected runs matters when comparing end-to-end system efficiency. The paper is currently an arXiv preprint rather than a peer-reviewed publication.

## Consequence for current work

Reviewer inference: this is a strong evidence-engineering example for Test Authority and Diderot. It illustrates that a system can be too complex for direct reference recomputation, yet still be qualified through a purpose-built evidence mechanism whose assumptions are explicit. The pattern is useful beyond quantum computing:

`hard-to-recompute result -> embedded observables/invariants -> statistical certificate -> bounded claim`

This supports the Test Authority principle that acceptance evidence need not always be a full oracle, but the authority and assumptions of a surrogate certificate must be explicit. For MMALS it is only adjacent: the useful connection is epistemic architecture, not a direct algorithmic component.

## Follow-up

Compare this certificate architecture with conformal risk-control and runtime-assurance patterns already tracked in MMALS/Diderot: identify which guarantees are unconditional, which are assumption-conditioned, and how the evidence source-of-authority should be represented in a common qualification schema.

## Provenance note

All quantitative circuit, qubit, error-suppression and fidelity claims above come from arXiv:2607.25941 v3. The proposed translation into Test Authority/Diderot evidence architecture is reviewer inference and does not appear as a claim of the source.
