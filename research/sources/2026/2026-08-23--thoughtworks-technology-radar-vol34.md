---
title: "Thoughtworks Technology Radar, Volume 34"
canonical_url: "https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2026/04/tr_technology_radar_vol_34_en.pdf"
author_or_publisher: "Thoughtworks"
publication_date: "2026-04-15"
discovered_via: "Explicit Technology Radar watch"
alert_topic: "AI-augmented engineering; testing; agent governance"
reviewed_at: "2026-08-23"
source_type: "engineering radar / practitioner synthesis"
relevance: "high as discovery and engineering-practice signal"
evidence_quality: "medium: informed practitioner experience, not canonical or controlled scientific evidence"
related_tracks: ["Diderot", "AI testing", "agentic systems", "CI/CD", "Test Authority"]
related_concepts: ["feedback sensors for coding agents", "mutation testing", "sandboxed execution", "Dev Containers", "ADK", "Cursor", "Figma Make", "agent instruction bloat", "MCP by default"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Volume 34 signals a shift from raw agent capability toward engineering controls around agents. In Techniques, Thoughtworks places feedback sensors for coding agents, mutation testing and sandboxed execution in Trial; it also cautions against instruction bloat, coding-agent swarms and MCP-by-default patterns. In Tools, Dev Containers and Figma Make are Trial, while Cursor is Adopt. ADK is shown as Trial in the Languages/Frameworks quadrant.

## What the source actually provides

Source-derived: the Radar is based on Thoughtworks practitioner experience and records ring/status plus short rationales. The volume's four explicit themes are evaluating technology in an agentic world, retaining principles while relinquishing patterns, securing permission-hungry agents, and putting coding agents on a leash. It recommends deterministic feedback mechanisms such as compilers/tests, isolated execution, and renewed use of established engineering disciplines around AI-generated work.

## Limitations and uncertainty

Radar placement is engineering opinion and field experience, not proof of ROI, safety or generalization. Ring status can be influenced by Thoughtworks' own project exposure and may lag or lead wider industry practice. Each promoted pattern still requires primary technical evidence and local qualification before adoption.

## Consequence for current work

Reviewer inference: the Radar is useful as a discovery surface for Diderot/Test Authority, especially because its feedback-sensor + sandbox + mutation-testing combination matches an evidence-driven agent harness. It also supports a broader principle relevant to MMALS: use stable engineering structure as prior/gating knowledge and spend learning/exploration capacity where uncertainty or contradiction remains, rather than asking AI to rediscover every rule.

## Follow-up

Continue monitoring future Radar editions and ring moves. For any material change, trace to primary repositories, standards or controlled engineering evidence before changing the roadmap. No new edition or ring movement was identified in the 2026-08-23 scan.

## Provenance note

Ring/status claims and themes are source-derived from the official Radar. The mapping to Diderot/MMALS and the engineering-prior interpretation are reviewer inferences.
