# Research → review → Diderot ingestion contract

## Purpose

Diderot is a pedagogical and synthesis surface. It may explain, reorganize, compare and teach scientific work, but it must not become the upstream authority that qualifies its own scientific claims.

For local research claims, the admissible direction is:

```text
research/evidence source
        ↓
independent review / qualification
        ↓
Diderot capitalization
```

The reverse direction is prohibited as scientific validation. A Diderot concept page, teaching toy, browser smoke, explanatory synthesis or accepted Diderot pull request cannot by itself qualify an upstream scientific claim.

This contract implements Diderot issue #15. It governs **eligibility for qualified local research evidence**. Visible learner-facing epistemic badges remain a separate concern for issue #16.

## Two authority paths

Diderot uses two distinct authority paths and must not confuse them.

### External foundational sources

Established papers, books, standards and other authoritative external references may directly support source-derived teaching content when cited with appropriate scope. They do **not** need to pass through a local MMALS research repository merely to be taught in Diderot.

### Local research evidence

A local MMALS/project result may be treated as **qualified research evidence** only after the ingestion gate below is satisfied. Diderot does not qualify such evidence itself.

## Qualification gate

A local research result is eligible for Diderot qualification only when all of the following are recoverable:

1. **Upstream research source** — a repository or evidence source distinct from Diderot owns the scientific claim/result.
2. **Immutable source coordinate** — the exact commit, tag, frozen artifact or equivalent immutable coordinate reviewed is recorded.
3. **Independent review coordinate** — the review/disposition is directly inspectable and identifies the exact source coordinate it judged.
4. **Qualifying disposition** — for registry schema v0.1 the final disposition must be `ACCEPT`. A prior `PARTIAL ACCEPT / REQUEST CHANGES` does not qualify a changed head until that changed head is re-reviewed and accepted.
5. **Bounded claim** — the record states what is supported, its outcome class, scope and caveats. Qualification of one bounded claim is not qualification of an entire research program.
6. **Diderot registry record** — the result is entered in `data/research-evidence-ingestion.json`.
7. **Consumer reference** — any Diderot concept that relies on the result as qualified local research evidence references that registry record through `qualified_evidence_refs` in `data/concept-audit.json`.

The structural checker verifies traceability and consistency of these fields. It does not independently reproduce the experiment or prove that the scientific conclusion is true.

## Negative and null results

Qualification is not a positivity filter. `negative`, `null`, `mixed`, `method` and `positive` outcomes are all admissible when the upstream result and review support that bounded interpretation.

A negative or null result must not be hidden merely because it is pedagogically inconvenient. Conversely, a positive-looking toy result must not be upgraded because it is intuitive or visually persuasive.

## Diderot self-authority prohibition

A record in `data/research-evidence-ingestion.json` MUST NOT name `gharbonnier78/mmals-ml-wiki` as either:

- the upstream scientific source repository; or
- the repository that owns the qualifying scientific review.

This does not prohibit Diderot code review, editorial review or pedagogical review. It prevents those reviews from being reinterpreted as scientific qualification of the claim being taught.

Repository-name distinctness is only a structural proxy. The checker cannot establish social or organizational independence: a mirror, fork or separately named repository controlled by the same author could still pass that structural test. A reviewer must therefore inspect whether the claimed independent review is substantively independent rather than infer independence from repository naming alone.

## Teaching constructions and scientific results

Teaching constructions may reproduce a mechanism, intuition or falsification shape without being scientific outcome evidence.

For the belief/sufficiency work:

- the Diderot Toy 3 construction is pedagogical only;
- scientific Toy F2 is a separate research object;
- at the time this contract is introduced, Toy F2 is preregistered but not run/qualified;
- therefore no Toy F2 result may appear as qualified research evidence in Diderot until an upstream immutable result and independent `ACCEPT` disposition exist.

A future F2 result may be positive, negative or null. The ingestion rule is the same in every case.

## What an accepted Diderot PR does and does not mean

Acceptance of a Diderot pull request may establish that:

- the page is correctly sourced;
- the pedagogical distinction is clear;
- the implementation behaves as declared;
- the local governance contract is followed.

It does **not** establish that a project hypothesis is scientifically true, that a teaching toy is empirical evidence, or that an upstream result has been independently qualified unless the upstream qualification record exists separately.

## Machine-readable contract

`data/research-evidence-ingestion.json` is the canonical local registry for qualified local research evidence entering Diderot.

Each qualified record must contain at least:

- `source.repository`;
- `source.immutable_ref`;
- `source.artifact_url`;
- `review.repository`;
- `review.url`;
- `review.reviewed_ref`;
- `review.disposition`;
- `outcome`;
- `claim`;
- `scope`;
- `caveats`.

`review.reviewed_ref` must equal `source.immutable_ref` in schema v0.1. If a review qualifies a compound evidence pack rather than one commit, that pack must first receive its own immutable coordinate rather than weakening this equality rule.

Concept-audit entries may contain:

```json
{
  "qualified_evidence_refs": ["<registry-record-id>"]
}
```

A reference that does not resolve is a structural failure. The absence of such a reference means the concept has **not** claimed qualified local research evidence through this contract.

## Boundary with issue #16

This contract deliberately does not define the complete learner-facing epistemic-status vocabulary or rendering rules. Issue #16 may later render statuses such as source-derived, Diderot synthesis, project hypothesis, teaching toy and qualified research evidence.

The hard dependency is one-way: a future visible `qualified research evidence` status must be backed by this ingestion contract; this contract does not require every page to display that status now.

## Review expectation

An independent reviewer of this contract should challenge at least:

- whether an author can make Diderot qualify its own science through an indirect path;
- whether claimed review independence is substantively credible rather than merely encoded as a different repository name;
- whether a `PARTIAL ACCEPT` could be misused as final qualification;
- whether negative/null results remain first-class;
- whether the registry overreaches into external foundational-source governance;
- whether the structural checker distinguishes traceability evidence from scientific truth.
