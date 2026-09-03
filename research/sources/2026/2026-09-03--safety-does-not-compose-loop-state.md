---
title: "Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents"
canonical_url: "https://arxiv.org/abs/2608.27141"
author_or_publisher: "Chenhao Wu et al."
publication_date: "2026-08-27; revised 2026-09-02"
discovered_via: "MMALS daily web research watch"
alert_topic: "agent safety / persistent harness state"
reviewed_at: "2026-09-03"
source_type: "arXiv preprint, revised version"
relevance: "P0"
evidence_quality: "medium-high preprint: formal separation plus benchmark protocol, ablations and adaptive red team; not independent peer review"
related_tracks: ["Diderot ML", "Test Authority", "MMALS"]
related_concepts: ["persistent safety state", "agent loops", "composition failure", "irreversible actions", "Chronicle"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The paper argues that safety controls scoped to one trajectory do not compose across long-running autonomous loops when harmful evidence is fragmented across iterations. It proposes a persistent, non-decaying loop-level safety state (LoopHarness) rather than resetting or geometrically decaying risk after each trajectory.

## What the source actually provides

Source-derived facts: the paper proves a separation in a constructed attack setting where any trajectory-scoped monitor has true-positive rate equal to false-positive rate because decisive evidence never co-occurs inside one trajectory window, while a cross-iteration monitor can separate clean from attacked cases. It further argues that geometric risk decay leaves a constant cooling-off period exploitable by patient adversaries. LoopHarness uses persistent state, mediated commits and an arbiter; the authors derive an expected unauthorized-irreversible-action bound that is constant in horizon N under stated assumptions. The paper provides an evaluation protocol on Agent-SafetyBench with paired clean/attacked episodes, outer-state attacks, component ablations and adaptive white-box red teaming.

## Limitations and uncertainty

The strongest result depends on a deliberately adversarial construction and assumptions about mediated commits and arbiter detection. Persistent non-decaying state can itself accumulate false positives or stale suspicion if poorly designed. The paper is not yet independent evidence that the specific LoopHarness implementation works robustly in production organizations.

## Consequence for current work

Reviewer inference: this is directly relevant to Chronicle and Test Authority governance. Safety-relevant evidence should survive workflow boundaries when the underlying risk has not been discharged. Resetting risk because a new agent session, PR, job or subtask starts is an architectural error if the authorization decision spans those boundaries.

## Follow-up

Define an explicit persistent risk/evidence ledger for long-running agent workflows and test three policies on fragmented multi-iteration hazards: reset-per-run, decaying score, and state retained until explicit evidence-backed discharge.

## Provenance note

Formal claims, architecture and benchmark protocol are source-derived. Mapping to enterprise workflow/Chronicle governance is reviewer inference.