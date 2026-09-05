---
title: "LLM-Based Test Oracles: Source-of-Authority Taxonomy -- A Systematic Literature Review"
canonical_url: "https://arxiv.org/abs/2607.05031"
author_or_publisher: "Ali Hassaan Mughal, Muhammad Bilal / IEEE Access"
publication_date: "2026"
discovered_via: "arXiv replacement / IEEE Access"
alert_topic: "AI testing / oracle authority"
reviewed_at: "2026-09-05"
source_type: "peer-reviewed systematic literature review"
relevance: "high"
evidence_quality: "high"
related_tracks: ["Diderot", "Test Authority", "AI testing"]
related_concepts: ["test oracle", "source of authority", "LLM-as-a-judge", "specification grounding", "mutation testing"]
retention_verdict: "retain"
---

# Source note

## Central contribution

The review proposes that LLM-based test oracles should be classified not only by form or mechanism but by the source from which their verdict derives authority.

## What the source actually provides

The review follows PRISMA 2020, screening 2,436 records to 54 included studies and extending to 83 with snowballing. It analyzes source of authority, oracle form and adjudication mechanism. The authors report that just over half of the corpus reaches verdicts without a specification, and that oracle quality is more often assessed by resemblance to a known oracle than by actual fault detection. A replication package is released.

## Limitations and uncertainty

This is a secondary study; its conclusions depend on coding choices and the quality of underlying papers. 'No specification' does not automatically imply an unusable oracle, and specifications can themselves be wrong or incomplete.

## Consequence for current work

Source-derived fact: mechanism labels such as LLM-as-a-judge do not establish why a verdict should be trusted. Reviewer inference: every AI-generated or AI-executed oracle in Test Authority/Diderot should carry an explicit authority field such as written requirement, executable invariant, reference implementation, observed production behavior, expert judgment, or model prior.

## Follow-up

Add source-of-authority as a first-class attribute in the evidence/test-oracle taxonomy and compare mutation-detection performance across authority classes when data permits.

## Provenance note

Corpus counts and review findings are source-derived. The proposed evidence-schema field is reviewer inference.
