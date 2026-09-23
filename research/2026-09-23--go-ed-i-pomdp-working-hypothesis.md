---
title: "GO-ED-I-POMDP as a possible MMALS extension"
date: "2026-09-23"
status: "working hypothesis / explicitly unreviewed"
epistemic_status: "project hypothesis"
harness_ref: "e80097fe8eb88c9e9340732683710ba1dc2ae008"
source_note: "research/sources/2026/2026-09--interactive-pomdp-foundational-sources.md"
related_research:
  - "research/2026-09-23--collective-intelligence-independence-diversity-interaction-human-ai.md"
---

# GO-ED-I-POMDP as a possible MMALS extension

## Status warning

**Nothing in this note has yet been independently challenged or reviewed.**

It is preserved because it connects several previously separate project ideas in a potentially useful way. It must remain a **working hypothesis**, even where the underlying ingredients (POMDPs, I-POMDPs, value of information, multi-agent decision models) are established research topics.

Do not cite `GO-ED-I-POMDP` as an established literature term. It is a Diderot/MMALS working label.

## Starting point

Previous project work used a conceptual stack of:

```text
POMDP
-> ED-POMDP
-> GO-ED-POMDP
```

with the following intended separation:

- **POMDP**: represent uncertainty and sequential decision under partial observability;
- **ED (Evidence-Driven)**: make evidence acquisition, test, observation, mitigation and stop/escalate actions explicit and decision-relevant;
- **GO (Goal-Oriented)**: condition decisions on goals, losses, horizons, constraints and stakeholders rather than optimizing an abstract accuracy objective.

The present reflection asks whether the same separation can be retained when the base decision model is extended from POMDP to I-POMDP.

## Candidate extension

The proposed conceptual stack is:

```text
I-POMDP
-> ED-I-POMDP
-> GO-ED-I-POMDP
```

This is a project construction, not a literature claim.

## 1. What I-POMDP changes

In a standard POMDP, a focal agent maintains a belief over hidden world state:

```text
b_t(s)
```

In an I-POMDP, the focal agent may maintain a belief over an **interactive state** combining physical state and another agent model:

```text
IS_i = S x M_j
```

and schematically:

```text
b^I_i(s, m_j)
```

where `m_j` can encode a model of the other agent, potentially including its beliefs, capabilities, preferences or policy.

The important project interpretation is:

```text
uncertainty about world
+
uncertainty about evidence-producing / decision-making agents
```

## 2. Why ED appears to attach naturally

The ED layer can be interpreted as enlarging the action set with explicit epistemic/evidence actions.

For a single-agent POMDP, candidate actions already include:

```text
RUN_TEST
INSPECT_LOG
COLLECT_MEASUREMENT
MITIGATE
ESCALATE
STOP
DECIDE
```

With I-POMDP, an additional family becomes possible:

```text
ASK_INDEPENDENT_REVIEWER
ASK_DOMAIN_EXPERT
REQUEST_COUNTEREXAMPLE
REQUEST_CONFIDENCE
REVEAL_EVIDENCE
WITHHOLD_PEER_OUTPUT
SYNCHRONIZE
ASK_HUMAN
RUN_DISCRIMINATING_EXPERIMENT
```

The working idea is that these can all be evaluated as actions with expected decision value and cost.

A reviewer would then be neither an obligatory ceremony nor automatically authoritative. Asking a reviewer is an **epistemic action** whose usefulness depends on what new observation it is expected to produce.

## 3. Evidence about the world vs evidence through an agent

A potentially important distinction is:

```text
P(o | s)
```

versus:

```text
P(o_j | s, m_j, a)
```

If reviewer/expert output can be treated as a stationary noisy observation channel, an ordinary POMDP may be sufficient.

If the response depends materially on what the other agent believes, knows, has observed, values, or infers about the focal agent, an interactive model may be justified.

This gives a candidate **model-complexity gate**:

> Do not use an I-POMDP merely because another agent exists. Use it only when explicit modeling of that agent changes a decision-relevant prediction or policy.

That proposition itself still requires review.

## 4. Value of information for social/agent interactions

A generic working form is:

```text
VOI(a)
  = E[V(b_{t+1}) | b_t, a]
    - V(b_t)
    - C(a)
```

For I-POMDP-like belief state `b^I_t`, the same idea could evaluate:

```text
VOI(ASK_REVIEWER)
VOI(RUN_TEST)
VOI(ASK_ANOTHER_MODEL)
VOI(SYNCHRONIZE)
VOI(ASK_HUMAN)
```

This connects directly to the existing harness/reviewer principle of preferring the **cheapest discriminating evidence/action**, but does not prove that the harness itself should become an I-POMDP controller.

## 5. Why GO becomes more interesting, not less

A naive multi-agent extension would assume one collective goal.

The working GO extension instead allows distinct local and shared goals:

```text
g_scientist
g_reviewer
g_engineering
g_business
g_human_owner
g_shared
```

Their roles may intentionally differ.

For example:

```text
Scientist: explain / support a claim
Reviewer: falsify / expose missing controls
Engineering: reduce operational risk
Business: manage time/cost/value
Human owner: retain accountable decision authority
```

The project hypothesis is that GO should make these goal/constraint boundaries explicit rather than forcing every agent into the same local utility.

## 6. Outer framing remains external

The earlier GO-ED-POMDP work treated stakeholder framing, boundary selection and goal construction as an outer activity rather than something the controller invents autonomously.

That remains important here.

Candidate architecture:

```text
framing / stakeholders / boundaries
            |
            v
goals + losses + constraints
            |
            v
interactive belief state
            |
            v
evidence / interaction action
            |
            v
observation + belief update
            |
            v
decision / next information action
```

I-POMDP would enrich the decision model; it would not decide whose goals are legitimate or set system boundaries by itself.

## 7. Candidate relationship to mutualism

This part is especially speculative.

A collective may improve the shared outcome while systematically imposing cost or loss on one participant.

Therefore:

```text
collective performance improvement
!=
mutualism
```

A first working mutualism test might require longitudinally non-negative or acceptable value for participating actors together with positive shared value, for example:

```text
Delta U_i >= 0
Delta U_j >= 0
Delta U_shared > 0
```

over an appropriate horizon, possibly allowing temporary local sacrifices.

This is **not** yet a sufficient definition of mutualism. It ignores bargaining, asymmetric contribution, outside options, delayed benefits, fairness, non-transferable utility and the difficulty of comparing utilities across agents.

It is preserved only as a candidate direction.

## 8. Minimum-sufficient-model rule

Do not collapse all multi-agent uncertainty into I-POMDP.

Use the least complex representation that preserves the decision-relevant uncertainty:

```text
GO-ED-POMDP
  if other-agent behavior can be treated as part of the observation/environment model

GO-ED-Dec-POMDP
  if multiple decentralized actors coordinate under a sufficiently shared objective

GO-ED-I-POMDP
  if a focal actor must explicitly reason about another actor's model/beliefs/preferences/policy
```

The mapping above is conceptual and requires independent challenge, especially because Dec-POMDP and I-POMDP have different formal assumptions and solution concepts.

## 9. Candidate research sequence

Do not start by implementing GO-ED-I-POMDP.

A safer progression is:

```text
CI-MMALS-0
measure interaction effects:
- independence
- error correlation
- complementarity
- cadence
- reviewer contribution
- cost

then, only if adaptation appears decision-relevant:

CI-MMALS-1
compare fixed interaction protocols
vs adaptive information/interaction policy

then, only if explicit other-agent modeling adds value:

candidate GO-ED-I-POMDP study
```

This preserves the minimum-sufficient-mechanism principle.

## 10. Claims to challenge

Independent review should explicitly attempt to refute or narrow:

1. **ED attachment claim** — is treating reviewer/expert consultation as an epistemic action genuinely an ED extension, or merely ordinary POMDP action modeling?
2. **I-POMDP necessity claim** — when does `P(o_j | s)` become insufficient enough to justify explicit `m_j`?
3. **GO attachment claim** — does adding multiple goal structures preserve a coherent decision problem, or does it require game-theoretic/social-choice machinery not captured by the proposed label?
4. **Mutualism claim** — are utility increments an adequate operationalization, or do they confuse cooperative performance with mutualistic relation?
5. **Dec-POMDP boundary** — are the proposed POMDP / Dec-POMDP / I-POMDP selection rules formally defensible?
6. **Computational tractability** — does the richer model add explanatory power that could realistically justify nested-belief complexity?
7. **Scientist/Reviewer fit** — are LLM reviewer interactions stable/intentional enough to merit agent-model inference rather than simpler reliability modeling?
8. **Adaptive protocol value** — could a fixed independent ensemble or simple stopping rule achieve the same outcome at lower cost?

## Current disposition

- I-POMDP as a literature concept: **established**.
- Extension of Diderot/MMALS ED concepts onto I-POMDP: **plausible working hypothesis / unreviewed**.
- Extension of GO concepts onto I-POMDP: **plausible but more structurally uncertain / unreviewed**.
- GO-ED-I-POMDP as a named framework: **project coinage / not established**.
- Mutualistic GO-ED-I-POMDP: **speculative research direction**.
- Scientific gate: **none**.
