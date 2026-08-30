# Diderot agent instructions

This repository adopts `gharbonnier78/scientific-research-harness` as its versioned method
contract. Treat this file as the short startup map, not as a replacement for the harness.

Before substantive work:

1. Read `harness-adoption.yaml`.
2. Load the exact immutable harness ref declared there, beginning with `HARNESS.md`.
3. Load only the companion contracts relevant to the task.
4. Preserve Diderot's source/evidence/claim boundaries; never infer compliance from memory or
   from a moving `main` branch.
5. For learning-oriented mathematical work, automatically check
   `mathematics/notation/registry.json` whenever a non-trivial notation is introduced or
   meaningfully re-encountered. Apply the pinned harness contract
   `pedagogy/MATHEMATICAL_NOTATION_CAPITALIZATION.md`: update an existing semantic entry when
   possible; create a draft entry only when the concept is genuinely new.
6. New notation entries must include a read-aloud form, formal and plain-language meaning,
   minimal example, prerequisites, encounter provenance, connections/domains and a
   misconception when relevant. Agent-generated entries remain draft until reviewed.
7. Web/search/poster outputs must derive from the canonical registry, not from manually
   duplicated notation lists.

Current immutable harness entrypoint:
`https://raw.githubusercontent.com/gharbonnier78/scientific-research-harness/2d1cefe42676fafde9b4a2fa5bc6d300abdcfb4f/HARNESS.md`

Current notation-capitalization contract:
`https://raw.githubusercontent.com/gharbonnier78/scientific-research-harness/2d1cefe42676fafde9b4a2fa5bc6d300abdcfb4f/pedagogy/MATHEMATICAL_NOTATION_CAPITALIZATION.md`

If either pinned dependency cannot be loaded, report it before claiming harness compliance.
Do not release scientific gates from a remembered or summarized copy of the contract.
