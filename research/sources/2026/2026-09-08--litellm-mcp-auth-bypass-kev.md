---
title: "LiteLLM MCP Authentication Bypass (CVE-2026-59822) — CISA KEV"
canonical_url: "https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q"
author_or_publisher: "BerriAI / GitHub Security Advisory; exploitation status confirmed by CISA KEV"
publication_date: "2026-06-30"
discovered_via: "Google Alerts -> traced to vendor advisory and CISA KEV"
alert_topic: "LLM"
reviewed_at: "2026-09-08"
source_type: "vendor security advisory + authoritative exploitation catalog"
relevance: "high"
evidence_quality: "high for vulnerability existence and active exploitation status"
related_tracks: ["Test Authority", "agentic systems", "AI infrastructure", "security"]
related_concepts: ["MCP", "authentication", "tool access", "AI gateway", "known exploited vulnerability"]
retention_verdict: "retain"
---

# Source note

## Central contribution

LiteLLM's MCP Streamable HTTP authentication path allowed an unauthenticated caller to reach configured MCP tooling with an arbitrary Bearer token because a failed LiteLLM key-validation path could fall through to an empty authentication object. The issue is fixed in LiteLLM 1.84.0. CISA added CVE-2026-59822 to the Known Exploited Vulnerabilities catalog on 2026-09-02, elevating it from a theoretical software flaw to a confirmed in-the-wild exploitation concern.

## What the source actually provides

Source-derived facts from the vendor/GitHub advisory: affected versions are `<1.84.0`; the vulnerable MCP Streamable HTTP path could let an unauthenticated attacker establish an effectively authenticated MCP session and list/call configured tools and connected services; 1.84.0 contains the fix.

Source-derived fact from CISA KEV (also independently mirrored by CIRCL's KEV ingestion): CVE-2026-59822 was added on 2026-09-02 as a known exploited vulnerability, with a federal remediation due date of 2026-09-16.

## Limitations and uncertainty

CISA KEV confirms exploitation but does not, in the surfaced public record, provide detailed incident prevalence, exploit-chain frequency or affected deployment topology. Risk depends strongly on whether LiteLLM is deployed, which version is running, whether MCP endpoints are enabled/reachable and what privileges exposed tools carry. This source is operational security evidence, not evidence about agent reasoning quality.

## Consequence for current work

Reviewer inference: AI/agent qualification must include the gateway, MCP/tool-authentication boundary and non-human identity path in scope. A system can have well-tested agent logic while an infrastructure fallback silently bypasses the intended authorization model. This strengthens the Test Authority principle that agent/tool trust must be tested end-to-end, including negative/fallback paths, least privilege and versioned dependency evidence.

## Follow-up

For any internal use of LiteLLM or similar AI gateways, verify inventory/version and MCP exposure; require >=1.84.0 for LiteLLM where applicable. Add authentication-fallback and unauthorized-tool-invocation tests to the agentic infrastructure qualification pattern, alongside explicit source-of-authority and identity metadata.

## Provenance note

Vulnerability mechanics, affected/fixed versions and active-exploitation status are source-derived. The proposed Test Authority qualification implications are reviewer inference.
