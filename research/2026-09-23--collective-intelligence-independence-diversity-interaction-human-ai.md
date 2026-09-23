---
title: "Collective intelligence for MMALS: independence, diversity, interaction timing and human-AI complementarity"
date: "2026-09-23"
status: "draft research synthesis / open hypothesis"
epistemic_status: "Diderot synthesis + project hypotheses"
harness_ref: "e80097fe8eb88c9e9340732683710ba1dc2ae008"
source_pack: "research/sources/2026/2026-09--collective-intelligence-primary-source-pack.md"
secondary_source: "research/sources/2026/2026-09--collective-intelligence-decide-t-on-mieux-a-plusieurs.md"
---

# Collective intelligence for MMALS

## Question

Can a scientific or engineering collective composed of humans and/or LLM agents become more reliable by deliberately preserving independent exploration, measuring complementary failure modes, controlling when members interact, and aggregating their outputs with an explicit rule?

This note does **not** assume that the answer is yes. It turns the September 2026 collective-intelligence reading into a falsifiable MMALS research program.

## 1. Immediate correction to the harness interpretation

A previous informal formulation described the desired loop as:

```text
Explore independently
-> Synchronize
-> Explore independently
-> Challenge
-> Aggregate
```

The literature gives a reasonable experimental motivation for testing such a loop, especially Bernstein, Shore & Lazer (2018), but **the current harness does not normatively implement this protocol**.

### Current repository state checked on 2026-09-23

- moving harness `main` HEAD: `e8e043c2b66a74ccacd023d67a32f989885449eb`;
- Diderot immutable harness pin: `e80097fe8eb88c9e9340732683710ba1dc2ae008`;
- harness PR #8, **Add evidence-based independent reviewer contract**, remains open/draft and unmerged;
- harness PR #9, **Phase 0 scientific interaction architecture and conversational CLI contracts**, remains open and unmerged.

Current/pinned `HARNESS.md` requires source traceability, explicit claims, replay, verification, chronology, bounded handoff and navigable delegated review. It distinguishes deterministic replay from statistical independence. It does **not** require independent generation before synchronization, a repeated independent-revision phase, intermittent interaction, or a formal aggregation step.

PR #9 is much closer to the intended direction: its proposed Reviewer contract says the reviewer must preserve independence, must not optimize for agreement, and should return control after each bounded review action; its session protocol prohibits an implicit autonomous review loop and proposes fresh cross-model reconstruction. But that remains a proposed Phase 0 architecture, not the current normative harness.

Therefore:

```text
evidence from collective-intelligence literature
        ->
candidate interaction design
        !=
current harness guarantee
```

This distinction is important enough to preserve as an explicit research/harness finding.

## 2. What the primary literature actually gives us

### 2.1 Competence is necessary but not sufficient

Woolley et al. (2010) and Riedl et al. (2021) support the existence of reusable group-level performance structure across heterogeneous tasks. Bates & Gupta (2017) provide meaningful counter-evidence to a strong process-first account by finding a much larger role for individual IQ.

For MMALS, the safe interpretation is:

```text
collective performance = f(member capability, collaboration process, task)
```

not:

```text
good collaboration process makes member capability irrelevant
```

### 2.2 Useful diversity is functional and error-related

Hong & Page (2004) motivate **functional diversity**: different representations and search heuristics can prevent a team of individually strong but similar solvers from collapsing onto the same local solution.

The Diversity Prediction Theorem sharpens the idea for numeric prediction:

```text
collective squared error
  = mean individual squared error
  - prediction diversity
```

but this identity does not say that adding arbitrary diversity improves a real system. An intervention can increase diversity while simultaneously making individual contributors worse.

For MMALS the measurable object should therefore be a joint profile:

```text
member error
+ pairwise error correlation
+ hypothesis/prediction diversity
+ aggregate error
```

### 2.3 Interaction is neither always good nor always bad

Bernstein, Shore & Lazer (2018) report the central trade-off relevant to our architecture:

- interaction allows social learning and exploitation of good discoveries;
- continuous interaction can reduce independent exploration;
- intermittent interaction can preserve more exploration while still allowing information exchange.

This is a direct reason to add an **interaction-cadence experimental factor**. It is not yet evidence that intermittent interaction improves LLM scientific review.

### 2.4 Aggregation is part of the algorithm

Prelec, Seung & McCoy (2017) show that majority vote is only one possible aggregation rule. Their "surprisingly popular" method uses both a respondent's answer and their prediction of how others will answer to recover specialized minority knowledge.

Kurvers et al. (2016) show that pooling independent medical judgments can improve diagnosis, but contributor competence matters. Adding weak or redundant contributors is not automatically beneficial.

Therefore an ensemble experiment must not treat `N agents` as the intervention while leaving aggregation unspecified.

### 2.5 Human-AI complementarity can be an error-structure phenomenon

Zöller et al. (2025) provide the strongest direct bridge to MMALS: hybrid human-LLM collectives performed strongly because the contributing systems had complementary strengths and failures.

The key candidate variable is therefore not merely "human + AI" or "model A + model B", but:

```text
complementarity of failure modes
```

Operationally this can be measured through pairwise error correlation and **unique-error recovery**: cases in which one contributor fails and another supplies the information that allows the aggregate to recover.

## 3. Candidate MMALS interaction model

The following is a **project hypothesis**, not a harness rule:

```text
Phase I   independent generation
             |
             v
Phase II  bounded synchronization
             |
             v
Phase III independent reconsideration
             |
             v
Phase IV  adversarial challenge / reviewer
             |
             v
Phase V   explicit aggregation or human decision
```

### Why each boundary exists

**Independent generation** protects against immediate social/model anchoring and lets us measure genuine pre-interaction disagreement.

**Bounded synchronization** exchanges selected claims/evidence rather than full hidden reasoning histories.

**Independent reconsideration** asks each contributor to update after seeing the synchronization packet without allowing a serial "agent 2 edits agent 1" chain to become the only path.

**Challenge** searches for unsupported inference, missing evidence, counterexamples and failure conditions rather than agreement.

**Aggregation/decision** uses an explicit rule and keeps the human decision boundary visible.

This architecture can fail. It may cost more, create artificial disagreement, or add latency without improving outcome quality. The experiment below is designed to detect that.

# 4. Candidate experiment: CI-MMALS-0

## 4.1 Objective

Estimate the effect of **interaction structure** and **contributor heterogeneity** on bounded reasoning performance while measuring error correlation, calibration, diversity collapse and cost.

## 4.2 Primary research questions

**RQ1.** Does intermittent interaction improve final task loss relative to continuous interaction?

**RQ2.** Does a heterogeneous independent ensemble reduce shared error relative to a homogeneous independent ensemble?

**RQ3.** Is any ensemble gain explained by complementary failures rather than agent count alone?

**RQ4.** Does the Scientist/Reviewer-style challenge phase recover errors that simple aggregation leaves unresolved?

## 4.3 Experimental conditions

Use the same predeclared task set across conditions, with fresh stateless sessions and no access to outputs from another condition.

| Arm | Protocol |
|---|---|
| A — Single | One strong model, one pass. |
| B — Homogeneous independent | Multiple fresh instances of the same model/prompt family; no cross-visibility; fixed aggregation. |
| C — Heterogeneous independent | Different model families and/or deliberately different problem-solving contracts; no cross-visibility; same aggregation family as B. |
| D — Continuous interaction | Contributors see preceding outputs during each round and may respond immediately. |
| E — Intermittent interaction | Round 1 independent -> bounded synchronization packet -> fresh independent revision -> bounded challenge -> fixed aggregation. |
| F — Scientist/Reviewer | Scientist produces bounded result; fresh Reviewer independently reconstructs evidence and challenges it; Scientist responds without reviewer rewriting; final decision/aggregation is explicit. |

A later **Phase B** may add a human-AI arm. CI-MMALS-0 should first isolate machine interaction structure because human participation changes cost, expertise and experimental unit.

## 4.4 Task family

Start with tasks that have externally checkable ground truth and that expose multiple plausible reasoning paths.

Recommended first block:

1. **synthetic engineering fault diagnosis** with known injected root cause and distractors;
2. **claim/evidence audit** where the admissible source packet contains both supporting and disconfirming evidence;
3. **numerical/probabilistic estimation** where calibration can be scored.

Avoid open-ended "best essay" judgments in the first study because evaluator subjectivity would confound the interaction effect.

## 4.5 Predeclared outputs per contributor

Before any interaction, each contributor must emit:

```yaml
answer: ...
confidence: 0..1
claims:
  - ...
evidence_refs:
  - ...
alternatives:
  - ...
known_uncertainties:
  - ...
```

The pre-interaction artifact is frozen before synchronization. A contributor must not see peer outputs before this artifact is committed.

## 4.6 Synchronization packet

For the intermittent arm, synchronization should expose only reviewable scientific artifacts:

- answer/claim;
- confidence;
- evidence references;
- explicit alternative explanation;
- major uncertainty.

Do **not** depend on private chain-of-thought. The experiment concerns inspectable epistemic artifacts, not hidden reasoning transcripts.

## 4.7 Aggregation baselines

At minimum predeclare:

- simple majority for categorical answers;
- arithmetic mean for numeric predictions;
- mean probability for calibrated probabilistic outputs;
- reliability-weighted aggregation learned only from a separate validation split.

A "surprisingly popular" aggregator is an optional extension and requires collecting predicted peer-response frequencies. It should not silently replace the simple baseline.

## 4.8 Primary estimands

For a loss function `L`:

```text
Delta_intermit_cont =
    mean(L_continuous) - mean(L_intermittent)

Delta_hetero_homo =
    mean(L_homogeneous_independent) - mean(L_heterogeneous_independent)

Delta_review =
    mean(L_pre_review) - mean(L_post_review)
```

Positive values indicate improvement by the second method named in each contrast.

Estimate uncertainty with paired task-level bootstrap intervals or an explicitly justified hierarchical model. Do not reduce the study to one aggregate accuracy number.

## 4.9 Secondary measures

**Individual competence**
- accuracy / task loss per contributor;
- Brier score or log loss for probabilistic answers.

**Error dependence**
- pairwise correlation of binary error indicators;
- pairwise agreement conditional on being wrong;
- shared-failure rate.

**Complementarity**
- unique-error recovery rate;
- cases recovered by the aggregate when the best single contributor failed;
- marginal contribution of each contributor under ablation.

**Diversity**
- prediction variance for numeric tasks;
- answer entropy for categorical tasks;
- semantic claim diversity only if its metric is separately validated.

**Convergence dynamics**
- disagreement before synchronization;
- disagreement after synchronization;
- disagreement after challenge;
- rate of premature unanimous wrong answers.

**Cost**
- tokens;
- wall-clock latency;
- model calls;
- monetary/compute proxy where available.

## 4.10 Key falsification conditions

The interaction hypothesis is weakened or refuted if, under the preregistered task distribution:

- intermittent interaction does not improve loss over the continuous-interaction baseline within the study's uncertainty;
- any apparent gain disappears when controlling for extra model calls/tokens;
- heterogeneity raises diversity but also raises individual error enough that aggregate performance is unchanged or worse;
- reviewer challenge mostly increases agreement without recovering errors;
- independent contributors exhibit highly correlated failures, showing that nominal model/prompt diversity does not create useful epistemic diversity;
- a simple independent ensemble matches the more complex Scientist/Reviewer loop.

The last condition is especially important under the harness principle of **minimum sufficient mechanism**.

## 4.11 Confounders to control

- model/version drift during the experiment;
- unequal token budgets across arms;
- unequal access to tools or source documents;
- different aggregation rules between B and C;
- cross-condition memory/cache leakage;
- prompt-length advantage in interactive conditions;
- task contamination from model training;
- different number of inference calls masquerading as a protocol effect;
- evaluator leakage when the same model generates and grades tasks.

## 4.12 Interpretation rules

A result such as "intermittent > continuous" supports only the tested task/model/budget regime.

Do not promote:

```text
intermittent interaction worked in CI-MMALS-0
```

into:

```text
all scientific agent systems should use intermittent interaction
```

without transfer experiments.

Likewise, a negative result is useful: it may show that the current Scientist/Reviewer ceremony adds no decision value over a cheaper independent ensemble.

# 5. Implication for M = Mutualistic

The previous MMALS bio-inspiration work frames **Mutualistic** as a normative engineering property rather than a law copied from biology. The collective-intelligence literature gives us a candidate operational test:

A collaboration is not mutualistic merely because all members participate or converge.

A stronger measurable condition is that, over a bounded task distribution:

1. members contribute non-redundant information or recovery paths;
2. those contributions improve the collective outcome relative to simpler baselines;
3. the benefit is not obtained only by silencing or copying one participant;
4. costs and asymmetric dependencies are visible;
5. removal/ablation shows which members or interaction steps actually add value.

This suggests a future distinction:

```text
nominal collaboration
!=
collective intelligence
!=
mutualistic collaboration
```

The third requires an explicit reciprocal-benefit criterion that still needs definition.

# 6. Harness consequence

Do **not** modify `HARNESS.md` to mandate the candidate loop on the basis of this literature review alone.

The justified next reusable step is narrower:

1. record the missing distinction between **reviewer role independence** and **measured pre-interaction independence**;
2. add CI-MMALS-0 as a consumer experiment;
3. only after evidence, decide whether a reusable interaction-cadence rule belongs upstream;
4. preserve PR #8/#9 as proposed architecture rather than pretending their rules are already merged.

# 7. Current disposition

- Primary-source pass: **complete enough to motivate experiment design**.
- Claim that current harness already implements the intermittent loop: **refuted**.
- Claim that intermittent interaction is better for LLM scientific work: **NOT DEMONSTRATED**.
- Claim that complementarity/error structure is a meaningful variable to measure: **supported as a transferable research question**.
- CI-MMALS-0: **candidate / not yet executed**.
- Scientific gate released: **none**.

# 8. Next admissible action

Independent review of this synthesis and experiment design should challenge:

- whether the experimental arms isolate interaction cadence from extra compute;
- whether error-correlation and unique-error-recovery measures are sufficient;
- whether the task family has objective enough ground truth;
- whether the Scientist/Reviewer arm duplicates the intermittent arm;
- whether "mutualistic" can be operationalized without smuggling in an evaluative conclusion;
- whether any literature claim above exceeds its source.
