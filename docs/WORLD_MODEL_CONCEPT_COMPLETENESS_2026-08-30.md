# World-model / dynamic-systems concept completeness audit — 2026-08-30

Status: **conceptual completeness pass, before source audit and independent review**.

The Diderot Concepts index now exposes **59 individual concept pages**.

## Purpose

Prevent the Diderot world-model pathway from containing undefined conceptual jumps and preserve a reviewable record of why individual concept pages were introduced.

This pass does **not** certify the scientific wording or bibliography of every page. Source/provenance review is the next gate.

## Navigation target

A reader should be able to navigate:

`Encoder -> State -> Latent/Sufficient State -> Markov Property -> MDP/POMDP -> Belief -> Filtering -> Transition/Observation Models -> Observability/Reconstruction -> Stochastic/Chaotic Dynamics -> Attractors/Bifurcations/Regimes -> Dynamic Compatibility -> Minimal Sufficient Dynamic Inference -> Action-conditioned Prediction -> Rollout/Planning -> World Model`

without an undefined semantic jump.

## Newly individualised concept families

### State and representation
- State
- Latent state
- Sufficient state
- Encoder
- State estimator
- Information-preserving compression

### Sequential decision / partial observability
- Markov property
- MDP
- POMDP
- Belief state
- Bayesian filtering
- Transition model
- Observation model

### Prediction / intervention / control
- Action-conditioned prediction
- Rollout
- Counterfactual
- Planning
- Controllability
- Probabilistic predictability

### Dynamical systems
- Stochastic-chaotic system
- Lyapunov exponent
- Dynamical regime
- Bifurcation
- Attractor
- Basin of attraction
- Bistability
- Langevin equation / SDE
- Committor
- Recurrence
- Local dimension
- Delay embedding / Takens
- Sampling and reconstruction

### Scientific method
- Toy model / toy experiment

Existing pages for stochastic dynamics, deterministic chaos, observability/reconstruction, local-to-global structure, local geometry, dynamic compatibility distance, minimal sufficient dynamic inference and world model remain part of the same pathway.

## Toy rule

Toys are deliberately retained as a permanent research and pedagogy tool.

> **Toy evidence is mechanism evidence, not evidence of general superiority or real-world validity.**

Every new concept page should eventually have a toy, counterexample or minimal mechanism illustration when such a toy is meaningful.

Historical MMALS toys such as Split Digits, Split-MNIST, Split-FashionMNIST and route/function controlled counterexamples remain valid research-history artifacts. They must not be retrospectively upgraded into evidence for the world-model program.

## Epistemic boundary

Page existence does not imply:
- the concept is necessary for MMALS;
- the concept is implemented in MMALS;
- the concept improves MMALS;
- the concept is part of a validated world model;
- an interdisciplinary analogy has been proven operationally useful.

Use status labels to distinguish foundational imported concepts, analogies, open MMALS hypotheses and implemented evidence.

## Next gate — source and epistemic audit

For every concept page, verify:
1. primary/reference source where possible;
2. definition fidelity;
3. mathematical notation;
4. common-confusion boundaries;
5. whether the MMALS link is evidence, hypothesis or analogy;
6. whether the toy really isolates the claimed mechanism;
7. outgoing/incoming graph relations;
8. redundancy with another concept page.

## Independent reviewer gate

After visual review, provide the branch/PR to an independent reviewer (Claude) with explicit instructions to find:
- missing concepts;
- unnecessary concept splitting;
- incorrect or contested definitions;
- weak sources;
- analogy-to-claim drift;
- incorrect graph edges;
- toy experiments that fail to isolate mechanisms;
- hidden conflation among task, context, state, belief and regime;
- unjustified use of the term world model.

Review comments should be dispositioned as `ACCEPT`, `PARTIALLY ACCEPT`, or `REJECT`, with rationale and traceable correction.

## Current publication question

The conceptual work supports a possible perspective/research-agenda paper around:

> **What Is a World Model? Our Current Belief, and What We Are Trying to Learn Through MMALS and GO-ED-POMDP**

The intended contribution is a reasoned, falsifiable position rather than a claim to a final universal definition.
