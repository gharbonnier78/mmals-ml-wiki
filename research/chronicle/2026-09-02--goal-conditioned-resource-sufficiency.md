# Chronicle — goal-conditioned resource sufficiency refinement

Date: 2026-09-02
Harness ref: `e80097fe8eb88c9e9340732683710ba1dc2ae008`
Branch: `agent/goal-conditioned-resource-sufficiency`

## Trigger

A Jetson AGX Orin energy-per-token campaign prompted a question about whether an agent must carry a long active context and whether edge energy should enter the same optimization framework as model/representation compression.

## Existing Diderot state found before mutation

The core information argument was already present:

- `belief-state` states that, under a correctly specified POMDP, belief is a Markov information state for planning;
- `sufficient-state` already defines sufficiency relative to a declared prediction/decision family;
- `contingent-sufficiency` already makes goal, horizon, actions, costs and observations part of the project-local sufficiency scope;
- `information-preserving-compression` already treats compression as target-relative;
- `minimal-sufficient-dynamic-inference` already includes memory, latency and energy among system-complexity terms.

Therefore this change does **not** create a separate “energy-aware agent” foundation. It records a re-encounter and strengthens the bridge between existing concepts.

## Decision

1. Treat active LLM context as an implementation working set, not as the mathematical definition of agent state.
2. In a classical POMDP, retain `belief state` as the canonical information-state reference under the model assumptions. A single best-state estimate is a stronger compression and needs a decision-relative adequacy argument when uncertainty may affect action or value.
3. Treat energy as one possible mission cost, especially important in battery-limited edge regimes, alongside latency, memory, quality, failure consequence, monetary cost, evidence acquisition and human burden.
4. Do not assume that all objectives can safely be traded through weights. Hard constraints may remain non-negotiable.
5. If the operating regime is hidden, do not let a policy condition on the unavailable true regime label; use observable context, a belief over regimes, or another justified information state.
6. Treat latent projection, weight quantization and history/context compression as analogous only at the level of a common engineering question: what can be reduced while preserving the downstream properties declared by the mission? They are not asserted to be the same mathematical operation.

## Source/evidence boundary

Added `research/sources/2026/2026-09-02--becirovski-jetson-energy-per-token.md` as bounded engineering evidence for one AGX Orin campaign. The source supports measured resource trade-offs on that configuration; it does not establish a general agent-state architecture or a universal energy objective.

The source note also records an arithmetic wording caveat: the campaign's phrase “generation halves at nearly constant power” is not promoted as a general quantitative statement because the reported output coefficients rise by about 50%, not 100%, in several configurations.

## Pedagogical mutations

- `concepts/sufficient-state/index.html`: context-window/state distinction; belief versus best-state estimate; goal/regime-relative sufficiency.
- `concepts/information-preserving-compression/index.html`: separates projection, quantization and context/state compression while retaining the common preservation-test bridge; adds the Jetson edge case.
- `concepts/value-function/index.html`: makes multi-cost mission objectives and hard constraints explicit; records hidden-regime information boundary.

No new mathematical notation was introduced in the canonical pages beyond already registered belief/value/regret notation, so no notation-registry entry was created in this change.

## Claims not released

- No claim that shorter context is always better.
- No claim that belief state is the best practical representation for every LLM agent.
- No claim that energy should dominate the cost function outside an explicitly resource-constrained mission.
- No claim that the Jetson measurements generalize to datacenter hardware, other models, other runtimes or wall-power accounting.
- No claim that the MMALS lifecycle is empirically superior because of this source.

## Next admissible action

Run the repository's required static/release checks and inspect the branch diff. If checks are available only through CI after PR creation, keep that missing evidence visible and do not call the change scientifically reviewed merely because the prose is internally consistent.
