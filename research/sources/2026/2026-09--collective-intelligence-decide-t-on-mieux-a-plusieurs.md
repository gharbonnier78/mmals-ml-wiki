---
title: "Intelligence collective : décide-t-on mieux à plusieurs ?"
canonical_url: null
author_or_publisher: "Mehdi Moussaïd and Guillaume Jacquemont — Pour la Science"
publication_date: "2026-09"
discovered_via: "User-provided photographs of Pour la Science n°597, pp. 15-23"
alert_topic: "collective intelligence, group decision, diversity, prediction markets, human-AI collectives"
reviewed_at: "2026-09-23"
source_type: "science-popularization synthesis"
relevance: "High for MMALS collaboration design; indirect for artificial multi-agent performance"
evidence_quality: "Secondary synthesis; central claims were checked against the primary publications listed in the companion primary-source pack"
related_tracks:
  - "MMALS"
  - "scientific-research-harness"
  - "human-AI collaboration"
  - "multi-agent systems"
retention_verdict: "retain"
---

# Source note

## Central contribution

The article asks when groups make better decisions than individuals and reviews several mechanisms: aggregation of independent estimates, a general collective-intelligence factor, social sensitivity and turn-taking, functional diversity, prediction markets, structured elicitation, metacognitive aggregation, and recent human-AI diagnostic ensembles.

For MMALS, the useful transfer is **not** the slogan "more agents are better." The useful question is whether the collective preserves sufficiently competent and sufficiently non-redundant judgments long enough for an aggregation or challenge protocol to exploit their complementarity.

## What the article supports

The photographed article presents, among other points:

- Galton-style aggregation of numerical estimates;
- Woolley et al.'s collective-intelligence factor and proposed correlates;
- discussion pathologies such as hidden profiles, anchoring, unequal speaking time and brainstorming losses;
- independent elicitation and structured aggregation as remedies;
- Page's diversity-prediction identity;
- prediction markets and the "surprisingly popular" rule;
- Kurvers et al.'s pooling of independent medical diagnoses;
- Zöller et al.'s 2025 human-AI diagnostic collectives.

The article also explicitly recommends practical protections against influence effects, such as eliciting opinions independently before discussion, delaying expert/leader intervention, and iterating rather than forcing immediate consensus.

## Primary-source correction layer

The article is a useful map, but several statements become more conditional when returned to primary literature.

1. **Collective intelligence factor.** Woolley et al. (2010) reported a latent group-performance factor and associations with social sensitivity and more equal conversational turn-taking. Bates and Gupta (2017) failed to replicate those proposed causes and attributed much more of group performance to individual cognitive ability. Riedl et al. (2021), pooling 22 studies, again found a robust collective-intelligence factor and substantial process effects. Therefore the existence of reusable group-level performance structure is better supported than any simple causal recipe for producing it.

2. **Diversity.** Hong and Page (2004) establish a conditional model result: functionally diverse problem solvers can outperform a group selected only for individual ability under assumptions that make top performers increasingly similar. This is not a general empirical law that demographic or arbitrary diversity always improves performance.

3. **Diversity-prediction identity.** For arithmetic-mean aggregation under squared error,
   collective error = mean individual error - prediction diversity.
   This is an exact identity, not a causal proof that increasing diversity in a real system must improve accuracy: changing diversity can also change individual error.

4. **Interaction timing.** Bernstein, Shore and Lazer (2018) experimentally found that intermittent interaction on their problem-solving task retained more exploratory benefit than constant interaction while still allowing social learning. The transfer from human groups solving that task to LLM scientific collaboration is a **project hypothesis**, not a demonstrated result.

5. **Human-AI complementarity.** Zöller et al. (2025) found strong diagnostic performance from hybrid human-LLM ensembles. Their mechanism is primarily independent contributions plus algorithmic aggregation and complementary error patterns; it is not evidence that free-form human-LLM conversation or agent debate is superior.

## What this source does not establish

The article and its cited literature do **not** establish that:

- five LLM instances are five independent epistemic sources;
- debate is inherently better than independent aggregation;
- model diversity is equivalent to error independence;
- a Scientist/Reviewer architecture should automatically converge to consensus;
- intermittent interaction will improve MMALS or scientific-review performance;
- human-AI teams are universally better than the best available human or AI system.

These remain hypotheses requiring a task-specific experiment.

## MMALS consequence

A stronger candidate design statement is:

```text
useful collective performance
    = competent contributors
    + complementary failure modes
    + preserved pre-interaction independence
    + an aggregation/challenge rule suited to the task
    - correlated error / premature convergence
```

For **M = Mutualistic**, this adds a measurable layer to the existing normative idea: reciprocal benefit should not be inferred from coexistence or agreement. A mutualistic collective should demonstrate that distinct members recover one another's errors or improve bounded outcomes without one member merely becoming a duplicated copy of another.

## Companion material

See:

- `research/sources/2026/2026-09--collective-intelligence-primary-source-pack.md`
- `research/2026-09-23--collective-intelligence-independence-diversity-interaction-human-ai.md`
- `research/chronicle/2026-09-23--collective-intelligence-mutualistic-collaboration.md`
