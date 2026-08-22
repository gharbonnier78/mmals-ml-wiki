---
title: "Helpful to a Fault: Measuring Illicit Assistance in Multi-Turn, Multilingual LLM Agents"
canonical_url: "https://arxiv.org/abs/2602.16346"
author_or_publisher: "Nivya Talokar, Ayush K Tarun, Murari Mandal, Maksym Andriushchenko, Antoine Bosselut"
publication_date: "2026-02-18"
discovered_via: "Google Alert -> EPFL institutional news -> primary paper/repository"
alert_topic: "Intelligence artificielle"
reviewed_at: "2026-08-22"
source_type: "ICML 2026 paper + open repository"
relevance: "High for agentic AI testing"
evidence_quality: "High"
related_tracks: ["AI testing", "Agentic systems", "Test Authority", "Diderot ML"]
related_concepts: ["multi-turn red teaming", "tool-using agents", "safety evaluation", "jailbreak discovery", "multilingual testing"]
retention_verdict: "retain"
---

# Source note

## Central contribution

STING (Sequential Testing of Illicit N-step Goal execution) evaluates agent misuse as a multi-turn process rather than a single harmful prompt. It constructs adaptive stepwise attack conversations, measures progression toward illicit task completion, and adds time-to-first-jailbreak style analysis.

## What the source actually provides

Source-derived facts: the paper evaluates 44 AgentHarm scenarios / 176 prompt instances across several frontier and open model families and seven languages. STING yields substantially higher illicit-task completion than single-turn AgentHarm and adapted multi-turn baselines. The authors introduce discovery curves, Restricted Mean Jailbreak Discovery and language-attributed hazard analysis. The EPFL repository exposes the attack-plan generator, multi-turn runner, graders, AgentHarm baseline, translated datasets, defense tests and analysis code, supporting reproducibility. The work is listed as ICML 2026 by the authors and repository.

## Limitations and uncertainty

The framework uses model-based judges and simulated harmful tool environments; benchmark success is not identical to production compromise. Safety conclusions depend on target permissions, tool surfaces and real execution boundaries. The result also concerns adversarial persuasion, not all forms of agent failure.

## Consequence for current work

Reviewer inference: AI Test Authority should include workflow-level safety tests whose unit is the entire sequence of actions and context accumulation, not individual prompts or tool calls. This directly complements sandboxing and deterministic feedback controls: a system can pass per-step checks yet converge toward an unsafe final objective.

## Follow-up

Add a multi-turn safety test pattern to the agent governance/testing catalogue: benign-looking staged requests, cumulative intent tracking, tool-permission boundaries, and end-to-end outcome scoring. Compare single-turn refusal rate against trajectory-level unsafe completion rate.

## Provenance note

Paper design, benchmark scope, metrics and repository availability are source-derived. The Test Authority integration proposal is reviewer inference.
