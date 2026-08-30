# Diderot source & epistemic audit — World-model / dynamics bridge

**Date:** 2026-08-30  
**Scope:** all 59 individual concept pages in the current Diderot branch  
**Status:** Step 2 audit layer implemented; independent Claude review preserved under `docs/reviews/` and handled through a separate disposition record

## 1. Purpose

This audit answers a different question from conceptual completeness.

Step 1 asked: **Can a reader navigate the concepts without an undefined jump?**

Step 2 asks:

- Is the concept externally established, internally defined, or only a working synthesis?
- Does the definition stay faithful to its reference tradition?
- Does a source support the general concept, or are we accidentally treating it as evidence for MMALS?
- Is the mathematics canonical only under restricted assumptions?
- Is a graph edge a genuine conceptual relation or merely an analogy?
- Is a toy being used for mechanism/falsification, or being over-promoted to external validity?

A citation never promotes an MMALS hypothesis to validated evidence by itself.

## 2. Epistemic taxonomy

Every concept page now receives a generated audit panel from `data/concept-audit.json`.

The main classes are:

1. **Established external concept** — standard mathematics, control, probability, dynamical systems, causal inference, POMDP or information theory.
2. **Reference-consistent modeling pattern** — widely used but not necessarily governed by one unique formal definition (for example some uses of latent state or rollout).
3. **Working synthesis** — our current cross-domain formulation over established ingredients; must be challengeable and revisable.
4. **MMALS program concept** — canonical inside the research program, not external consensus terminology.
5. **MMALS hypothesis / constructed diagnostic** — new proposal requiring ablation, falsification and comparison.
6. **Contested research term** — notably `world model`; multiple legitimate traditions coexist and no universal official definition is assumed.
7. **Scientific-method rule** — notably the role of toy models.

## 3. Reference anchors

The registry currently contains 23 reference anchors. They are intentionally a mix of primary papers, expert references, textbooks/reviews and internal primary provenance.

### State, estimation, decision and control

- R. E. Kalman (1960), *A New Approach to Linear Filtering and Prediction Problems*, DOI `10.1115/1.3662552`.
- R. E. Kalman (1960), *On the general theory of control systems*, DOI `10.1016/S1474-6670(17)70094-8`.
- Kaelbling, Littman & Cassandra (1998), *Planning and acting in partially observable stochastic domains*, DOI `10.1016/S0004-3702(98)00023-X`.
- Judea Pearl (2009), *Causality: Models, Reasoning, and Inference*, 2nd ed., DOI `10.1017/CBO9780511803161`.

### Signal, reconstruction and information

- Claude E. Shannon (1949), *Communication in the Presence of Noise*, DOI `10.1109/JRPROC.1949.232969`.
- Floris Takens (1981), *Detecting strange attractors in turbulence*, DOI `10.1007/BFb0091924`.
- Tishby, Pereira & Bialek (2000), *The information bottleneck method*, arXiv `physics/0004057`.
- John M. Lee (2012), *Introduction to Smooth Manifolds*, 2nd ed., DOI `10.1007/978-1-4419-9982-5`.

### Dynamical and stochastic systems

- Edward N. Lorenz (1963), *Deterministic Nonperiodic Flow*.
- Paul Langevin (1908), *Sur la théorie du mouvement brownien*.
- Kloeden & Platen (1992), *Numerical Solution of Stochastic Differential Equations*.
- Steven H. Strogatz (2018), *Nonlinear Dynamics and Chaos*, 2nd ed.
- John W. Milnor (2006), *Attractor*, Scholarpedia.
- Edward Ott (2006), *Basin of attraction*, Scholarpedia.
- Eckmann, Kamphorst & Ruelle (1987), *Recurrence Plots of Dynamical Systems*.
- Weinan E & Eric Vanden-Eijnden (2010), *Transition-path theory and path-finding algorithms for the study of rare events*.
- Charó, Galatolo, Cazzaniga & Faranda (2026), *Hitting times, recurrence, and local dimension under nonstationary forcing with applications to climate data*.

### Continual learning and scientific modeling

- Parisi et al. (2019), *Continual lifelong learning with neural networks: A review*.
- Richard Levins (1966), *The Strategy of Model Building in Population Biology*.
- MMALS public repository and research chronicle (living internal primary provenance).

### World-model traditions

- David Ha & Jürgen Schmidhuber (2018), *World Models*.
- Yann LeCun (2022), *A Path Towards Autonomous Machine Intelligence*.
- Chen et al. (2026), *A Definition and Roadmap for World Models*.

## 4. Important audit findings

### 4.1 World model is not treated as an official definition

The page remains a **multi-source working definition**. Ha & Schmidhuber, LeCun, and Chen et al. provide related but non-identical framings. Diderot therefore separates:

- source traditions;
- a minimal shared working core;
- our current MMALS belief;
- the explicit statement that current MMALS is **not** being relabeled as a world model.

### 4.2 `Sufficient state` is target-relative

The word *sufficient* is dangerous if left absolute. The current audit requires it to mean sufficient **for a stated prediction, decision or control objective**, not a lossless representation of the whole world.

### 4.3 Latent state is not automatically dynamical state

An embedding can be useful for classification while omitting variables required for future prediction. The `latent-state` page is therefore under reviewer focus.

### 4.4 Action-conditioned prediction is not automatically counterfactual

A learned conditional prediction `p(s_{t+1}|s_t,a_t)` does not by itself establish a causal intervention semantics. The `counterfactual` page is anchored to causal-model literature and the graph edge is deliberately marked for independent review.

### 4.5 Linear controllability/observability must not be silently generalized

Kalman's classical concepts provide canonical anchors in linear systems. Their use as metaphors or diagnostics for nonlinear learned MMALS dynamics requires an explicit generalized definition and validation.

### 4.6 Sampling/reconstruction analogies have assumptions

Shannon sampling results depend on structural assumptions such as band limitation. Takens' embedding theorem has its own genericity and dimension assumptions. Neither theorem proves that arbitrary ML representations are reconstructible from sparse observations.

### 4.7 Stochastic and chaotic contributions must be ablated

`stochastic-chaotic system` is kept as a composite label rather than a new fundamental category. A MMALS experiment must separate at least deterministic sensitivity, stochastic forcing, coupling and regime structure.

### 4.8 Probabilistic predictability is deliberately narrow

The phrase

> **unpredictable trajectory != unpredictable risk**

is retained as a research intuition, not a universal theorem. Transition-path theory and recent recurrence/local-dimension work support the possibility of useful transition/event probabilities in systems where exact trajectories are difficult, but the scope and calibration must be demonstrated per system.

### 4.9 Dynamical regime is not a cluster

The audit preserves:

`cluster != dynamical regime != causal regime`

A candidate new MMALS regime therefore needs evidence beyond latent-space separation: persistence, functional consequences, predictive/transition evidence and robustness are candidate requirements.

### 4.10 Local-to-global and local geometry are research bridges

Differential geometry provides genuine local/global mathematical structures. The MMALS transfer remains an analogy/hypothesis until we define what local charts, metrics, transition rules or invariants correspond to operationally and test them.

### 4.11 Dynamic compatibility distance is explicitly non-canonical

There is no claim that the proposed MMALS `dynamic compatibility distance` is an externally established metric. It is a constructed diagnostic that must be ablated against simpler latent, route, behavioral and transition distances.

## 5. Toys remain first-class — and bounded

The audit makes the following rule explicit:

> **Toy evidence is mechanism evidence, not evidence of general superiority or real-world validity.**

Historical MMALS reduced-task evidence remains valid research history, but it is named only at the level directly supported by the pinned public repository. The public record explicitly lists:

- MNIST;
- FashionMNIST;
- RotatedMNIST;
- PermutedMNIST;
- controlled route/function counterexamples involving `D_r`, `D_z`, `D_y`.

Traceability:

- pinned MMALS README: https://github.com/gharbonnier78/mmals/blob/3d9c8e0284f83c9fb39570a7be9aa661062b3c4c/README.md
- pinned FashionMNIST evidence directory: https://github.com/gharbonnier78/mmals/tree/3d9c8e0284f83c9fb39570a7be9aa661062b3c4c/raw_evidence

Earlier shorthand such as “Split Digits / Split-MNIST / Split-FashionMNIST” is not treated as canonical provenance unless a corresponding immutable artifact is identified. The verified historical toys may continue to explain, falsify or isolate mechanisms, but they must not be retrospectively promoted to world-model evidence.

New toys proposed for the dynamic/world-model direction should isolate one mechanism at a time: hidden regimes/POMDP belief, stochastic vs chaotic contributions, reuse/adapt/fork, local geometry, committor/transition risk, and minimal sufficient state.

## 6. Structural enforcement

The repository now includes `scripts/check_concept_audit.py` and runs it in the pull-request CI.

The check fails if:

- a concept page lacks an audit entry;
- an audit entry has no concept page;
- a concept references an unknown group;
- a concept has no reference anchor;
- a source key is unresolved;
- required epistemic fields are absent.

This is **structural enforcement only**. It cannot determine whether a scientific interpretation is correct. That remains a human/reviewer responsibility.

## 7. Independent-review focus

The independent reviewer should concentrate on concepts whose graph edges or terminology can easily overclaim:

- minimal sufficient dynamic inference;
- latent state;
- sufficient state;
- rollout;
- counterfactual;
- controllability;
- stochastic-chaotic system;
- probabilistic predictability;
- dynamical regime;
- committor as a proposed MMALS target;
- local dimension;
- observability/reconstruction;
- sampling/reconstruction;
- Takens delay embedding;
- information-preserving compression;
- local-to-global structure;
- local geometry;
- dynamic compatibility distance;
- world model.

Requested review dispositions remain:

`ACCEPT / PARTIALLY ACCEPT / REJECT + rationale + required change`.

## 8. What Step 2 does not prove

Step 2 does not prove that:

- the new concepts are useful for MMALS;
- the proposed graph is the unique correct ontology;
- MMALS can learn a world model;
- the tentative goal-oriented extension of ED-POMDP improves decisions;
- local geometry improves routing;
- committor prediction is useful in the intended benchmarks;
- a compact state can preserve old competence and future predictability simultaneously.

Those are research questions for the experimental program.
