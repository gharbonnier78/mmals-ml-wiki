---
title: "Interactive POMDPs — foundational source note"
publication_date: "2005-2019"
reviewed_at: "2026-09-23"
source_type: "primary research"
epistemic_status: "source-derived"
relevance: "Foundation for reasoning about other agents under partial observability; possible future MMALS extension"
retention_verdict: "retain"
---

# Interactive POMDPs — foundational source note

## Established literature

**Interactive POMDP (I-POMDP)** is an established multi-agent sequential-decision formalism, not a Diderot/MMALS coinage.

Primary anchor:

Piotr J. Gmytrasiewicz and Prashant Doshi.  
**A Framework for Sequential Planning in Multi-Agent Settings.**  
*Journal of Artificial Intelligence Research* 24 (2005), 49-79.  
DOI: https://doi.org/10.1613/jair.1579  
Accessible copy: https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume24/gmytrasiewicz05a.pdf

The paper extends POMDP reasoning by incorporating models of other agents into the state representation. An agent maintains beliefs over physical state and over models of the other agent(s), potentially including their beliefs, preferences and capabilities. The resulting interactive beliefs may be hierarchically nested. Other agents' internal models are treated as neither directly observable nor directly manipulable by the focal agent.

A later computational line includes:

- Prashant Doshi and Piotr J. Gmytrasiewicz, **A Particle Filtering Based Approach to Approximating Interactive POMDPs** (AAAI 2005), motivated by the increased complexity of nested belief updates.
- Yanlin Han and Piotr Gmytrasiewicz, **IPOMDP-Net: A Deep Neural Network for Partially Observable Multi-Agent Planning Using Interactive POMDPs**, AAAI 2019, DOI https://doi.org/10.1609/aaai.v33i01.33016062.

## What is established

The literature supports the following bounded statements:

- I-POMDPs extend POMDP-style sequential decision making to settings in which another agent's model is itself decision-relevant.
- The focal agent may maintain a belief over both physical state and models of other agents.
- Those models may themselves contain beliefs, producing nested interactive beliefs.
- Solutions map interactive belief states to actions.
- This richer representation incurs substantial computational complexity and motivates approximate methods.

## What is not established by these sources

These papers do **not** establish:

- that a Scientist/Reviewer LLM workflow should be implemented as an I-POMDP;
- that reviewer outputs should always be modeled as intentional-agent observations rather than as ordinary noisy observations;
- that I-POMDPs improve scientific review, test governance or MMALS;
- that the project-specific GO or ED layers defined in Diderot/MMALS are standard I-POMDP extensions;
- that a mutualistic objective follows from I-POMDP theory.

Those are project-level hypotheses.

## Diderot/MMALS relevance

The established I-POMDP distinction suggests a clean future boundary:

```text
POMDP:
uncertainty about the world

I-POMDP:
uncertainty about the world
+ decision-relevant uncertainty about other agents' models
```

This may become relevant when another reviewer/expert/agent cannot be treated adequately as a stationary observation channel `P(o_j | s)` because its response depends materially on what it believes, knows, prefers, or infers about the focal agent.

The transfer remains unreviewed and should be challenged separately.
