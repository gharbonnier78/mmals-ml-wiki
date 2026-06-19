# Diderot v0.2.2 release-metadata correction

Apply this patch after the v0.2.2 EcoSpec patch.

It fixes a packaging inconsistency where the homepage footer still displayed v0.2.1, the README presented v0.2.0 as the current package, and inherited pages retained older footer metadata.

## Corrected

- all rendered HTML footers now display `Release v0.2.2 · Reviewed 2026-06-19`;
- the README explicitly declares v0.2.2 as the current release;
- `CITATION.cff` now declares version 0.2.2 and release date 2026-06-19;
- the research registry badge and current branch/repository counts are synchronized;
- the Diderot branch card reports v0.2.2;
- CI now runs `scripts/check_release_consistency.py` to prevent recurrence.

## Suggested commit

```text
fix: synchronize Diderot release metadata for v0.2.2
```
