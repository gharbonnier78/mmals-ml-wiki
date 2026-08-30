# Authoring guide

Every concept page follows a shared contract.

1. One-sentence definition
2. Why it matters
3. Discover explanation
4. Engineering explanation
5. Research explanation
6. Formal anchor
7. Current evidence
8. Boundary / non-claim
9. Related concepts
10. Stable publication link
11. Last-reviewed date

## Reading levels

- **Discover**: analogy, minimal vocabulary, visual intuition.
- **Engineer**: architecture, algorithm, metrics, observability, implementation consequences.
- **Research**: assumptions, mathematical formulation, evidence design, ablations, limitations.

## Mathematical notation

When learning-oriented content introduces or meaningfully re-encounters a non-trivial
notation, follow the pinned harness notation-capitalization contract and check
`mathematics/notation/registry.json` before creating a new semantic entry.

A useful entry records how the notation is read aloud, what it means formally and in plain
language, why it appears, a small example, prerequisites, misconceptions, encounter
provenance, connections/domains and its review maturity. Prefer appending a new encounter or
alias to an existing concept over duplicating the same mathematical idea under a second
glyph.

The notation registry is pedagogical metadata, not mathematical authority. Stable promotion
requires source provenance and review. The interactive atlas and printable poster must remain
derived views of the same registry.

## Evidence language

Use one of the canonical statuses: foundational, implemented, smoke tested, multi-seed evidence, mechanistic support, negative result, open hypothesis, or speculative branch.

Do not promote a page because the prose is persuasive. Promote it only when the evidence ledger changes.
