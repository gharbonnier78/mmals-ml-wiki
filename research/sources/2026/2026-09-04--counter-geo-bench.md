---
title: "Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization"
canonical_url: "https://arxiv.org/abs/2609.02316"
author_or_publisher: "Bing Zheng, Zongyao Zhao, Wenming Yang"
publication_date: "2026-09-02"
discovered_via: "Daily research watch"
alert_topic: "retrieval integrity"
reviewed_at: "2026-09-04"
source_type: "arXiv preprint and benchmark"
relevance: "High"
evidence_quality: "Medium-high"
related_tracks: ["Diderot", "agentic systems", "AI testing"]
related_concepts: ["retrieval manipulation", "generative search", "misinformation", "guardrail mismatch"]
retention_verdict: "retain"
---

# Source note

## Central contribution

Provides a controlled benchmark for defenses against information-distorting generative-engine optimization: ordinary-looking documents are rewritten to increase retrieval/synthesis influence while injecting targeted misinformation.

## What the source actually provides

Source-derived facts: Counter-GEO-Bench contains 247 human-verified, quality-gated queries paired with information-preserving and information-distorting rewrites. It evaluates attack success rate, false-positive rate, and answer quality across three victim LLMs. Three off-the-shelf safety/fact-checking defenses reduce attack success by at most 5.7% relative; one reported reduction is not statistically significant. The authors' C-GEO Guard baseline reports a 47.6% relative ASR reduction with near-zero utility loss.

## Limitations and uncertainty

Fresh preprint. Results cover only the tested search/retrieval setup, models, attack-generation process, and defenses. The proposed defense is a benchmark baseline, not proof of robust protection in open-world web retrieval. Human verification quality and attack realism remain important external-validity questions.

## Consequence for current work

Reviewer inference: Diderot's source intake cannot assume that fluent, relevant, apparently factual retrieved content is benign merely because it passes generic safety filters. Retrieval-quality assurance needs evidence-provenance, source diversity, primary-source tracing, and adversarial tests specifically targeting ranking/synthesis manipulation.

## Follow-up

Add an adversarial retrieval test where semantically optimized but false secondary pages compete with a primary source. Measure whether the resolver preserves primary-source priority and whether provenance/ranking controls prevent evidence distortion.

## Provenance note

Dataset size, tested defenses, and reported attack-reduction figures are source-derived. Mapping to Diderot provenance and source-ranking controls is reviewer inference.
