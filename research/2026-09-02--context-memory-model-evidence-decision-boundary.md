---
title: "From context to consolidated capability: an evidence-centred decision boundary"
status: "draft research synthesis"
date: "2026-09-02"
language: "en"
harness_ref: "e80097fe8eb88c9e9340732683710ba1dc2ae008"
task_id: "DIDEROT-CONTEXT-CONSOLIDATION-20260902"
source_boundary: "Source-reported facts, Diderot synthesis and MMALS hypotheses are explicitly separated."
related_concepts:
  - belief-model-memory
  - belief-state
  - sufficient-state
  - functional-memory
  - non-regression-evidence
  - value-of-information
  - tput
---

# From context to consolidated capability

## Why this note exists

The learning conversation that led here cannot be reduced to “RAG versus fine-tuning”. It moved through several successive objections:

1. a long context consumes memory and energy on an embedded platform;
2. the relevant question is not automatically “which LLM should the robot carry?”;
3. a mobile robot is not equivalent to an LLM agent with a body;
4. current humanoids run hierarchies of estimators, learned policies and controllers at different time scales;
5. continual learning need not happen on the edge device;
6. repeated, stable and useful contextual information may eventually deserve offline consolidation;
7. a model must never become the sole authority for the institutional knowledge it absorbed.

The durable research question is therefore:

> Given a mission and its evidence requirements, what should remain context, what should be retrieved, what should be represented as current state or belief, what should be stored as memory, what should be consolidated into model parameters, and what should not be computed at all?

This document preserves the reasoning, disagreements, equations, limits and sources. It is a Diderot research synthesis, not scientific evidence.

## 1. Separate the objects before optimizing them

We use the following project notation:

\[
C_t = \text{context assembled for the current inference},
\]

\[
M_t = \text{recoverable memory or evidence retained across episodes},
\]

\[
b_t = \text{belief about the currently hidden state},
\]

\[
z_t = \text{task-relevant latent representation},
\]

\[
\theta_t = \text{model parameters and learned inference function},
\]

\[
g_t = \text{current goal or mission}.
\]

These are related but not interchangeable:

\[
b_t/z_t \neq M_t \neq \theta_t \neq C_t.
\]

Plain-language reading: what the system currently believes, what it remembers, how it computes, and what information is temporarily shown to it obey different update rules and different governance obligations.

A crucial asymmetry follows:

- context can be removed at the next call;
- retrieved memory can be invalidated or replaced while preserving provenance;
- a belief can be recomputed from new observations;
- changing \(\theta\) changes the inference function that may affect every future situation.

Consequently, parametric consolidation carries a stronger non-regression burden:

\[
L_{\mathrm{old}}(\theta_{t+1})
\leq
L_{\mathrm{old}}(\theta_t)+\varepsilon,
\]

where the inequality is a desired bounded-regression condition, not a guarantee obtainable from a finite test suite.

## 2. What the Jetson study measures — and what it does not

Julien Becirovski's public repository benchmarks local LLM inference on a Jetson AGX Orin. The screenshots that initiated the discussion report, for Llama 3.1 8B with llama.cpp and five-run medians:

| Configuration shown | Throughput | Power | Reported energy |
|---|---:|---:|---:|
| MAXN + draft 18 speculative | 46.8 tok/s | 42.0 W | 249 Wh / million generated tokens |
| MAXN + IQ4_XS | 26.8 tok/s | 48.3 W | 501 Wh / million generated tokens |
| MAXN | 22.0 tok/s | 47.6 W | 602 Wh / million generated tokens |
| 30 W “eco” mode | 6.6 tok/s | 18.0 W | 754 Wh / million generated tokens |

The post's engineering lesson is that lower instantaneous watts need not imply lower energy per generated token. Time matters. It also says:

- reading approximately 16,000 log tokens to produce JSON cost about 0.35 Wh in the shown scenario;
- prompt/context processing was reported as roughly thirty times cheaper than generation;
- once loaded, context made later output tokens about 50% more expensive in the example;
- a long-running agent carrying history could therefore pay much more than the one-off prompt ingestion suggests;
- energy figures are comparable only with an explicit measurement window and idle baseline;
- the appropriate hardware configuration depends on the mission profile.

These are source-reported benchmark observations under a specific platform, model, software stack and workload. They are not universal constants. The repository itself is the primary recoverable source; the LinkedIn screenshots are retained here as encounter provenance, not as a substitute for the repository's methods and raw results.

### Correct estimand

The study is best read as estimating:

\[
P(Y\mid A,\text{configuration}),
\]

where \(A\) is the prior decision to run this kind of LLM locally and \(Y\) includes throughput, memory, power and energy.

It does not establish:

\[
P(A\mid g_t,\text{mission},\text{risk},\text{connectivity},\text{resources}).
\]

Plain language: it helps answer “if we run this LLM on this board, what does it cost?” It does not answer the upstream architecture question “should this mission use that LLM at all?”

## 3. Reconstructing the author's belief charitably

An earlier shortcut equated “mobile robotics” with “mobile LLM agent”. That inference was rejected as too strong. The public material supports a narrower reconstruction:

\[
b_{\mathrm{author}}\approx
\begin{cases}
\text{Jetson platforms are relevant to robotic/embedded systems;}\\
\text{some systems may benefit from a local LLM capability;}\\
\text{that capability can be interactive and agentic at a high level;}\\
\text{structured outputs, tool calls, extraction and summarisation are realistic loads;}\\
\text{connectivity cannot always be assumed;}\\
\text{RAM, KV cache, latency, throughput and energy then become design constraints;}\\
\text{the local LLM component should therefore be measured and configured properly.}
\end{cases}
\]

No cited material establishes the stronger belief:

\[
b_{\mathrm{author}}=
\text{“replace SLAM, planning and motor control with an 8B language model”.}
\]

The robot appears in the post primarily as the energy-constrained host and mission context. The defensible reading is an embedded-systems engineer applying RAM, bandwidth, thermal, power and reproducibility reasoning to a new workload.

## 4. What contemporary humanoids actually carry

The current industrial pattern is a multi-rate stack, not “ChatGPT inside a humanoid”:

\[
\text{sensors}
\rightarrow
\text{perception/state estimation}
\rightarrow
\text{semantic/task layer}
\rightarrow
\text{visuomotor policy}
\rightarrow
\text{whole-body control}
\rightarrow
\text{actuators}.
\]

Training data may come from Internet pretraining, human video or motion capture, robot teleoperation, simulation and reinforcement learning. Offline training produces weights, policies, priors, representations and conventional software that are deployed onboard.

Figure's self-reported Helix architecture provides a concrete example:

| Layer | Published role | Published scale/rate | Published training signal |
|---|---|---|---|
| S2 | scene/language understanding and high-level semantic intent | 7B VLM at 7–9 Hz | Internet-scale VLM pretraining plus end-to-end robot training |
| S1 | reactive visuomotor translation of latent intent into targets | 80M transformer at 200 Hz | about 500 h of multi-operator teleoperation; simulated vision pretraining |
| S0 in Helix 02 | balance, contact and full-body coordination | 10M network at 1 kHz | over 1,000 h retargeted human motion; more than 200,000 parallel simulated environments |

S2 asynchronously updates a shared latent intent; S1 consumes the newest latent while operating at a faster rate. S0 handles the fastest physical loop. This supports the architectural distinction:

\[
\underbrace{\text{general semantic model}}_{\text{slow}}
\rightarrow
\underbrace{\text{visuomotor policy}}_{\text{fast}}
\rightarrow
\underbrace{\text{motor prior/control}}_{\text{very fast}}.
\]

It does not prove that Figure's design is optimal, nor that vendor videos demonstrate reliability across deployment distributions. The source is the vendor's technical description and must be treated as self-reported evidence.

## 5. Edge inference does not imply edge continual learning

The user hypothesis differs from permanent on-device learning. The robot can infer locally during disconnected operation, then transfer selected experience upon reconnection:

\[
\text{robot}
\xrightarrow{\text{upload}}
\text{episodes + context + outcomes + provenance}.
\]

Offline infrastructure can perform:

\[
\text{replay}
\rightarrow
\text{analysis}
\rightarrow
\text{adaptation/distillation/CL}
\rightarrow
\text{non-regression}
\rightarrow
\text{qualification}.
\]

The deployed return object need not be a full new model. It can be:

\[
\{\theta_{t+1},\text{adapter},\text{policy},\text{state encoder},
\text{semantic memory},\text{routing rule}\}.
\]

This creates two time scales:

- a fast operational loop carrying only what is needed until the next expected reconnection;
- a slow consolidation loop with greater compute, fleet evidence and qualification resources.

The resulting design variable is the required **informational autonomy horizon**: the smallest sufficient inference and information package that lets the robot fulfil its mission until the next credible consolidation opportunity.

## 6. Context management as an action

Rather than treating memory management as plumbing, the architecture can expose a goal-conditioned choice:

\[
a_t^{\mathrm{memory}}
\in
\{\text{keep in context},\text{store in memory},
\text{compress into state},\text{consolidate into model},\text{forget}\}.
\]

The choice depends on mission value, uncertainty, provenance needs, volatility, future reuse and regression risk.

This connects to the MMALS progression:

\[
\text{REUSE}\rightarrow\text{ADAPT}\rightarrow\text{FORK}\rightarrow\text{NEW REGIME}.
\]

It also connects to representation compression. The philosophical commonality with a learned projection from 512 to 128 dimensions is not that the mechanisms are mathematically identical. It is this principle:

> Do not transport the maximal representation; seek the smallest representation that preserves the properties needed for the mission under an explicit regret or loss bound.

For history \(H_t\) compressed into \(z_t\), a project-level target may be written:

\[
R_H(z_t)\leq\varepsilon,
\]

where \(R_H\) is the decision-relevant regret introduced by replacing the fuller history with \(z_t\). The quantity and its estimator remain to be defined experimentally.

## 7. Beyond “RAG versus fine-tuning”

Suppose \(K\) tokens of institutional context are retrieved for \(N\) requests. Repeated contextual use incurs prompt processing, KV-cache occupancy, longer generation, retrieval infrastructure, latency and energy. Consolidation instead has a fixed cost:

\[
C_{\mathrm{consolidation}}=
C_{\mathrm{data}}+
C_{\mathrm{train}}+
C_{\mathrm{eval}}+
C_{\mathrm{regression}}+
C_{\mathrm{qualification}}+
C_{\mathrm{deployment}}.
\]

A deliberately simplified amortisation threshold is:

\[
N^*\approx
\frac{C_{\mathrm{consolidation}}}
{C_{\mathrm{RAG/query}}-C_{\mathrm{model/query}}}.
\]

This formula is only an intuition pump. It is invalid if the denominator is non-positive and incomplete whenever quality, freshness, provenance or risk differ.

The real decision boundary is multidimensional:

\[
\mathcal D(x)=f(K,N,S,V,Q,P,C,R,H),
\]

with:

- \(K\): required context volume;
- \(N\): reuse frequency;
- \(S\): stability of the information;
- \(V\): change velocity;
- \(Q\): measured task-quality difference;
- \(P\): provenance and audit requirement;
- \(C\): full inference/retrieval/training cost;
- \(R\): regression and catastrophic-forgetting risk;
- \(H\): informational autonomy horizon.

The output is not binary:

\[
\mathcal D(x)\rightarrow
\{\text{context},\text{RAG},\text{memory},\text{adapter},
\text{fine-tune},\text{distill},\text{specialist model},\text{new regime}\}.
\]

### Three information types

1. **Stable invariant or skill.** Example: understanding the distinction between verification and validation. Candidate for parametric or procedural consolidation.
2. **Volatile authoritative fact.** Example: the currently qualified product version. It should normally remain retrieved with date, version and source even if queried frequently.
3. **Evidence-derived organisational knowledge.** Example: a repeatedly observed conjunction of conditions that predicts a qualification risk. It should move from observation to hypothesis to experiment to evidence before model consolidation.

The useful rule is:

> Internalise stable invariants and reusable skills; externalise volatile facts and authoritative evidence; evaluate the intermediate cases.

## 8. Relation to Mistral Forge

Mistral describes Forge as a system for training models on institutional documentation, code, structured data and operational records. Its official description includes pre-training, post-training, reinforcement learning, evaluation, benchmark monitoring and continuous adaptation, with enterprise control over models, data and infrastructure.

Forge therefore demonstrates an industrial direction for turning institutional context into domain-aware model capability. However, its public product description does not itself provide the decision rule proposed here: when repeated context should remain retrieval, become memory, be compressed into a state encoder, or be consolidated into model parameters after full economic and evidential accounting.

The project hypothesis is stricter than “encode institutional knowledge in a model”:

> Consolidate only what evidence shows to be advantageous, while preserving the separate evidence and knowledge objects required to reproduce, challenge, update or replace the model.

## 9. Evidence base and model base

Two organisational assets must remain distinct:

\[
\boxed{\text{Evidence base}}
\qquad\leftrightarrow\qquad
\boxed{\text{Model base}}.
\]

The evidence base contains source documents and versions, observations, experiments, datasets, outcomes, decisions, counterexamples, provenance and applicability conditions.

The model base contains foundation models, specialised models, parameters, adapters, policies, embeddings, state encoders and routers.

Even after:

\[
\text{evidence}\rightarrow\text{training}\rightarrow\theta',
\]

the model is not the authority for the evidence it absorbed. Claims must remain traceable:

\[
\text{claim}\longleftrightarrow\text{evidence}.
\]

The lifecycle is:

\[
E_t
\rightarrow
\text{contextual use}
\rightarrow
\text{candidate consolidation}
\rightarrow
M_{t+1}
\rightarrow
E_{t+1},
\]

never:

\[
M_t\rightarrow\text{truth}.
\]

This is the meaning of **model/evidence-centric** here: models are governed engineering assets promoted by evidence; evidence remains independently recoverable and contestable.

## 10. Proposed experimental programme

### Decision to support

For a defined task distribution and mission profile, select the least costly information/inference architecture whose decision quality, freshness, provenance and regression risk satisfy predeclared criteria.

### Candidate treatments

- fixed short context;
- long context;
- RAG with several retrieval budgets;
- summarised episodic memory;
- learned sufficient-state encoder;
- adapter/LoRA;
- domain fine-tune;
- distilled specialist;
- router between specialist and generalist;
- periodic offline continual learning with qualified rollback.

### Required measurements

- task utility and decision regret;
- calibration and uncertainty;
- input and output tokens;
- prefill and decode latency;
- KV-cache and peak memory;
- joules or Wh with explicit measurement boundaries;
- retrieval cost and failure modes;
- training, evaluation and qualification cost;
- information freshness and invalidation latency;
- provenance recovery rate;
- old-task regression and catastrophic forgetting;
- novelty/out-of-distribution detection;
- human review effort;
- autonomy horizon until reconnection.

### Baselines and ablations

At minimum, compare against a short-context generalist, long-context generalist and RAG generalist. Ablate memory, learned compression, consolidation, routing and offline update separately. Budget-match comparisons where the scientific question is about architecture rather than raw resource advantage.

### Gates

No consolidation strategy should be promoted unless:

- the target task gain is reproduced;
- old-task loss remains within a preregistered tolerance;
- volatile facts remain source-resolved rather than silently fossilised in weights;
- provenance can be recovered for decision-relevant claims;
- total cost includes training, evaluation, qualification and deployment;
- rollback and model/data version lineage are demonstrated;
- results are separated by regime rather than hidden in one global mean.

## 11. Misconceptions retained from the discussion

**Wrong:** a mobile robot is an LLM agent with wheels or legs.  
**Correction:** an LLM/VLM can be one high-level component in a multi-rate robotic architecture.

**Wrong:** low watts means low energy per token.  
**Correction:** energy integrates power over time; slower execution can cost more total energy.

**Wrong:** prompt ingestion is the entire cost of context.  
**Correction:** context also occupies KV cache and can make subsequent decoding more expensive.

**Wrong:** continual learning must run on the edge device.  
**Correction:** experience can be captured locally and consolidated offline before a qualified update returns.

**Wrong:** repeated retrieval automatically justifies fine-tuning.  
**Correction:** volatility, provenance, quality, regression and qualification can dominate token amortisation.

**Wrong:** a newer model containing more institutional data is necessarily better.  
**Correction:** promotion requires evidence against explicit objectives and non-regression criteria.

**Wrong:** successful vendor demonstrations establish deployment reliability.  
**Correction:** they are useful architecture disclosures and demonstrations, but external validity requires independent evaluation.

## 12. Understanding gate

A learner should be able to:

1. explain the difference among \(C_t\), \(M_t\), \(b_t/z_t\) and \(\theta_t\);
2. explain why the Jetson study answers a conditional runtime question, not the upstream architecture choice;
3. reconstruct the author's belief without attributing “LLM replaces robotics” to him;
4. describe why humanoid control is split across time scales;
5. explain how offline consolidation differs from permanent on-device learning;
6. identify one fact that should remain retrieved even after a million uses;
7. state why a model cannot become the sole source of authority for absorbed evidence;
8. design one falsifiable comparison between long-context/RAG and consolidation.

## 13. Status and unresolved questions

This note captures a coherent research programme, not a validated decision boundary. Open questions include:

- how to define decision-equivalent compression for a task family;
- how to estimate \(R_H\) without hiding rare catastrophic failures;
- how reconnection uncertainty modifies the optimal onboard package;
- how to price provenance, human review and qualification;
- whether novelty routing can safely wake a generalist only when needed;
- how to preserve competence while allowing regime fusion, split and retirement;
- whether the boundary learned on one hardware/model stack transfers elsewhere.

## Primary sources and encounter provenance

- Julien Becirovski, *jetson-llm-maxperf*: https://github.com/jbecirovski/jetson-llm-maxperf
- Mistral AI, *Introducing Forge*, 2026-03-17: https://mistral.ai/news/forge/
- Figure AI, *Helix*, 2025-02-20: https://www.figure.ai/news/helix
- Figure AI, *Helix 02*, 2026-01-27: https://www.figure.ai/news/helix-02
- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, 2020: https://arxiv.org/abs/2005.11401
- Three learner-supplied LinkedIn screenshots captured 2026-09-02; used only to preserve the discussion encounter and visible reported values. The canonical external benchmark source remains the repository above.
