# Minimal patch — Diderot MMALS/ML Wiki v0.2.1

This patch updates the Diderot research registry after confirming that `mmals-cal-evidence-contract` is already a public GitHub repository.

## Apply

Copy the files in this patch over the existing `mmals-ml-wiki` working tree, then run:

```bash
python scripts/check_internal_links.py
git status
git add data/repositories.json data/branches.json data/github-live.json site.config.json manifest.json CHANGELOG.md RELEASE_NOTES_v0.2.1.md PATCH_README_v0.2.1.md research/branches/index.html research/repositories/index.html index.html
git commit -m "fix: mark CAL evidence contract repository as public draft"
git push
```

## Commit message

```text
fix: mark CAL evidence contract repository as public draft

- update mmals-cal-evidence-contract from planned to public
- keep maturity as public draft specification, not stable evidence
- update the CAL evidence contract branch from planned to active
- point the next step to notebook exporters, representative ZIP validation, and stable contract tagging
- update the curated GitHub live snapshot
```
