---
title: "Verifiable official statistics: a blockchain-based approach"
canonical_url: "https://www.bis.org/publications/working-paper-1374-verifiable-official-statistics-blockchain-based-approach"
author_or_publisher: "Bank for International Settlements / Mario Rusev et al."
publication_date: "2026-09-02"
discovered_via: "Google Alerts -> primary BIS source"
alert_topic: "Verifiable credential"
reviewed_at: "2026-09-04"
source_type: "institutional working paper with open reference implementation"
relevance: "Medium-high"
evidence_quality: "High for engineering proof-of-concept; not a standard or production adoption"
related_tracks: ["Diderot", "evidence engineering", "Test Authority", "digital identity"]
related_concepts: ["provenance", "integrity", "W3C Verifiable Credentials", "Merkle batching", "canonicalization"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Builds and tests an end-to-end provenance/integrity mechanism for official SDMX statistics: canonicalize data, hash series, aggregate via a domain-separated Merkle tree, anchor one root on a public ledger, and bind publisher identity through a W3C Verifiable Credential and on-chain attestation.

## What the source actually provides

Source-derived facts: BIS Working Paper 1374 presents an XRPL proof of concept, an open-source reference implementation, and a cost model. Only fingerprints are anchored; underlying datasets remain off-chain. The paper reports median controlled-test publication latency of 3–5 seconds and verification latency of 1–2 seconds. The verification artefact carries ordered Merkle leaves and a signed W3C Verifiable Credential so a consumer can re-derive the root and verify publisher identity with a ledger lookup. BIS explicitly states Working Paper views are those of the authors, not necessarily the institution.

## Limitations and uncertainty

This is a proof of concept, not an ISO/W3C standard update, production deployment, or BIS endorsement of XRPL/XRP as an asset. Performance results are controlled-test measurements and may not generalize to production scale, governance, key compromise, revocation, ledger outages, or cross-jurisdiction deployment. Blockchain is only one possible anchoring mechanism; conventional PKI/transparency logs may be simpler in some environments.

## Consequence for current work

Reviewer inference: the architecture is directly useful as a concrete evidence-chain pattern for Diderot/Test Authority: canonical evidence object -> cryptographic digest -> batch/root -> signed publisher identity -> independently verifiable artefact. The key lesson is not 'use blockchain' but that provenance and integrity can be independently recomputed rather than asserted by the producing system.

## Follow-up

Compare this pattern with Sigstore/transparency-log and conventional PKI approaches for an OTEL/spec-to-evidence artefact chain. Retain the canonicalization, Merkle-batching, signed-identity, and independent-verification properties as requirements before selecting infrastructure.

## Provenance note

Architecture, implementation, latency, and identity-binding details are source-derived from BIS. The proposed Diderot evidence-chain abstraction and recommendation not to assume blockchain is reviewer inference.
