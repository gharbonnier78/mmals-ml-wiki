---
title: "What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness"
canonical_url: "https://arxiv.org/abs/2609.01222"
author_or_publisher: "Zichuan Li et al."
publication_date: "2026-09-01"
discovered_via: "Daily research watch"
alert_topic: "agent harness security"
reviewed_at: "2026-09-04"
source_type: "arXiv preprint"
relevance: "High"
evidence_quality: "Medium-high"
related_tracks: ["Test Authority", "Diderot", "agentic systems", "MMALS"]
related_concepts: ["context assembly", "privilege boundaries", "persistent context", "instruction hierarchy"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Introduces two context-assembly attack classes in agent harnesses: MessageRole Context Privilege Escalation, where low-privilege attacker content is promoted into a higher-privilege message role, and Cross-Scope Context Privilege Escalation, where attacker-controlled content persists beyond the scope in which it entered.

## What the source actually provides

Source-derived facts: the authors report a systematic analysis of 12 real-world agent harnesses, including Claude Code and Codex. Demonstrated consequences include full agent compromise, remote code execution, denial of service, and manipulated tool or skill invocations. The paper focuses on harness-side context assembly rather than model-side prompt hierarchy alone.

## Limitations and uncertainty

Fresh preprint, not peer reviewed. Harness implementations evolve quickly, and specific vulnerabilities may be patched. The abstract-level evidence does not establish that every deployment or configuration of the named products remains vulnerable. Generalization from coding-agent harnesses to all agent architectures requires care.

## Consequence for current work

Reviewer inference: provenance and privilege must be properties of context fragments, not merely of the final prompt. Diderot/Test Authority agent qualification should verify that low-trust data cannot be elevated by context assembly and that temporary evidence cannot persist across scope/session boundaries without explicit retention authority. Chronicle's persistence mechanism is itself a privilege boundary.

## Follow-up

Add two deterministic harness tests: low-trust-to-high-role promotion and cross-scope persistence. Record source identity, privilege, scope, transformation history, and expiry/retention authority as auditable context metadata.

## Provenance note

Attack categories, studied harness count, and reported consequences are source-derived. The proposed provenance/privilege tests and Chronicle implications are reviewer inference.
