# Harness meta-documentation

## Why Diderot has a harness

Diderot is a living interpretation and learning layer. The
`scientific-research-harness` is the versioned method contract that constrains how agents
frame, evidence, explain, review and hand off work. It is not another scientific source and
it must not become the authority for the mathematics, paper, dataset or domain under study.

The intended dependency is:

```text
authoritative source / textbook / protocol / expert
                     |
                     v
                Diderot content
                     |
          constrained and made durable by
                     |
                     v
          scientific-research-harness
```

The exact dependency is declared in the repository root `harness-adoption.yaml`.

## Why not one enormous `SKILL.md`

A monolithic prompt duplicates the contract, consumes context and goes stale. Diderot uses a
small auto-discovered vendor bootstrap as a **map** into a versioned system of record:

```text
AGENTS.md (Codex/OpenAI repository agents)
CLAUDE.md (Claude Code)
               |
               v
      harness-adoption.yaml
               |
               v
 immutable harness commit/tag
               |
      +--------+---------+
      |                  |
   HARNESS.md       companion contracts
                         |
                         +-- pedagogy
                         +-- evidence
                         +-- telemetry
                         +-- review/handoff
```

A root `SKILL.md` exists in the harness as a compatibility shim for environments that
discover skills, but it deliberately points to `HARNESS.md`; it does not duplicate the full
contract.

## Automatic loading by agent surface

### Codex / OpenAI repository agents

`AGENTS.md` is the repository bootstrap. Codex aggregates `AGENTS.md` (and overrides) from the
project path into its user instructions. Diderot therefore keeps its root `AGENTS.md` short
and requires it to load the pinned manifest and harness before substantive work.

### Claude Code

`CLAUDE.md` is Claude Code's project briefing/memory surface. Diderot uses it in the same way:
a small startup file that points to the pinned harness and local manifest. If an immutable
harness copy is later vendored locally, Claude Code can use an explicit `@path` import.

### Generic chat surfaces

A repository file cannot force every generic ChatGPT or Claude chat surface to inspect a
GitHub repository automatically. When the runtime does not have repository-instruction
discovery, the surrounding project/workspace/agent configuration must itself load the same
bootstrap at startup. The repository remains the system of record, but runtime wiring is a
separate concern.

This limitation is intentional to document: **declaring a dependency is not the same thing
as proving that a given chat runtime loaded it.**

## Current pinned adoption

At creation time Diderot pins harness commit:

`2d1cefe42676fafde9b4a2fa5bc6d300abdcfb4f`

That commit is the current head of upstream harness PR #18, which introduces mathematical-notation
capitalization, integrates it into `HARNESS.md`, and adds reusable agent bootstrap templates.
The local manifest marks this pin as provisional. If PR #18 is reviewed and merged, Diderot
should upgrade explicitly to the reviewed immutable ref; it must not silently begin following
`main`.

## Mathematical notation capitalization

The first Diderot consumer of the new pedagogy contract is:

`mathematics/notation/registry.json`

For learning-oriented mathematical work, agents are instructed to check the registry when a
non-trivial notation appears or acquires a new role. They must search semantically before
creating a new entry because a single glyph can be overloaded and a single concept can have
multiple notations.

Each notation entry aims to preserve:

- the symbol and LaTeX form;
- how it is read aloud;
- formal and plain-language meanings;
- why it appears in the current argument;
- a minimal example and a likely misconception;
- prerequisites;
- append-only learning encounters;
- related concepts and application domains;
- authority/provenance separate from Diderot synthesis;
- a pedagogical maturity level.

The interactive atlas and A2 print poster are both generated from the same registry.

## Canonicalization and review

Automatic detection is allowed; automatic self-authorization is not. An agent may create or
extend a `draft` entry, but should not promote its own explanation to `reviewed` or `stable`
without the repository's review/human-comprehension process.

A notation review should check at least formal correctness, reading, example validity,
overloading, provenance, duplicate semantics and the distinction between exact definition,
convention, intuition and approximation.

## Meta-governance: how this documentation evolves

The harness owns reusable method. Diderot owns the consumer implementation and learning
history. When Diderot discovers a reusable rule, it should be proposed upstream rather than
copied into every consumer. When the rule is domain-specific, it stays local.

Changes to the pinned harness are explicit dependency upgrades. Historical Diderot entries
retain the provenance of the harness version and source context under which they were
created.

## Useful entrypoints

- `harness-adoption.yaml` — exact dependency and local artifacts.
- `AGENTS.md` — Codex/OpenAI repository-agent bootstrap.
- `CLAUDE.md` — Claude Code bootstrap.
- `mathematics/notation/index.html` — interactive notation atlas.
- `mathematics/notation/poster.html` — A2 printable map.
- `mathematics/notation/README.md` — local notation consumer contract.
- upstream `scientific-research-harness/HARNESS.md` — normative method entrypoint.
