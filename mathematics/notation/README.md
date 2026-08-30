# Diderot Mathematical Notation Atlas

This directory is the consumer-side implementation of the notation-capitalization method
pinned in `harness-adoption.yaml`.

## Canonical source

`registry.json` is the single source of truth for notation entries. The interactive atlas and
the printable poster read that same registry. Do not maintain a second hand-written symbol
list in HTML, PDF or Markdown.

## Agent rule

For learning-oriented mathematical work, `AGENTS.md` and `CLAUDE.md` require agents to check
this registry whenever a non-trivial notation is introduced or meaningfully re-encountered.

Before creating an entry:

1. search by `id`, `concept`, aliases and semantic meaning;
2. prefer appending a new encounter, domain or alias to an existing concept;
3. distinguish an overloaded glyph from the concept it denotes in the current context;
4. keep agent-generated changes at `status: draft` until reviewed.

## Required fields

Each stable entry should make recoverable:

- visual notation and LaTeX;
- near-literal and natural French readings;
- concept/category and formal meaning;
- plain-language meaning and why the notation appears;
- a minimal hand-checkable example;
- prerequisites;
- encounter history;
- connections and application domains;
- a misconception or context warning when relevant;
- mathematical/source authority distinct from Diderot pedagogical synthesis;
- pedagogical maturity (`L0` to `L5`).

## Encounter provenance

Encounter history is append-only but curated. It records where a notation was met and what
that encounter added; it is not a raw transcript archive.

The first seed entries in this directory come from a learner-supplied course page on
applications and graphs, specifically Definition 5 and the examples immediately following
it. The exact bibliographic identity of that course page has not yet been catalogued, so the
registry says so rather than inventing a citation.

## Publication views

- `index.html` — searchable, filterable learning atlas.
- `poster.html` — large framed A2-landscape print view.

Both views are derived at runtime from `registry.json`.

## Review target

A reviewer should check formal correctness, spoken reading, example validity, overloads,
source provenance and duplicate semantics before promoting an entry from `draft` to
`reviewed` or `stable`.
