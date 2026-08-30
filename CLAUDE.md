# Diderot Claude project instructions

This repository uses the scientific-research-harness as a versioned project contract.
`CLAUDE.md` is only the automatic startup hook into that contract.

Before substantive work:

1. Read `harness-adoption.yaml`.
2. Load the exact immutable harness ref declared there, beginning with `HARNESS.md`.
3. Load the task-relevant companion contracts; do not substitute a moving branch, a previous
   conversation or a remembered summary.
4. Keep authoritative source material, Diderot explanation, scientific evidence and
   pedagogical understanding distinct.
5. In learning-oriented mathematical work, automatically inspect
   `mathematics/notation/registry.json` whenever a non-trivial notation appears or gains a new
   meaning. Apply the pinned
   `pedagogy/MATHEMATICAL_NOTATION_CAPITALIZATION.md` contract.
6. Prefer adding an encounter/alias/domain to an existing concept over creating a duplicate.
   Any agent-created notation entry remains `draft` until independently reviewed or promoted
   by the repository's accountable-human process.
7. Keep the registry as the single source for web/search/print views.

Pinned harness entrypoint:
`https://raw.githubusercontent.com/gharbonnier78/scientific-research-harness/2d1cefe42676fafde9b4a2fa5bc6d300abdcfb4f/HARNESS.md`

Pinned notation contract:
`https://raw.githubusercontent.com/gharbonnier78/scientific-research-harness/2d1cefe42676fafde9b4a2fa5bc6d300abdcfb4f/pedagogy/MATHEMATICAL_NOTATION_CAPITALIZATION.md`

If the pinned dependency cannot be loaded, say so before claiming harness compliance or
releasing a scientific gate. If a local immutable harness copy is later vendored, replace
remote loading with an explicit Claude Code `@path` import to that pinned local entrypoint.
