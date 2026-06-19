# Diderot — MMALS / ML Interactive Encyclopedia

A static, dependency-free knowledge site for MMALS and machine learning concepts. It connects canonical definitions, three reading levels, interactive laboratories, evidence status, research pathways, and stable links that can be cited from articles.

**Current release: v0.2.2** · Reviewed 2026-06-19

Repository: `https://github.com/gharbonnier78/mmals-ml-wiki`

## Included in v0.2.2

- 16 canonical concept pages
- interactive concept graph
- 6 interactive laboratories
- 3 guided reading pathways
- `/go/<concept>` permanent semantic redirects
- evidence ledger and link-health dashboard
- internal and external link-check scripts
- GitHub Pages deployment and scheduled link-status refresh workflows
- LaTeX and Markdown article-integration examples
- MMALS research story, event chronicle, branch map, repository registry, and publication pipeline
- public CAL evidence-contract registration and EcoSpec 1.0 integration

## Local preview

```bash
python -m http.server 8000
```

Open `http://localhost:8000`.

## Validate links

```bash
python scripts/check_internal_links.py
python scripts/check_external_links.py --output data/link-health.json
```

The internal checker is blocking in CI. External failures are recorded in the status file because third-party sites can fail temporarily.

## Publish with GitHub Pages

1. Create the repository `mmals-ml-wiki`.
2. Copy this package to the repository root.
3. Push to `main`.
4. In **Settings → Pages**, choose **GitHub Actions** as the source.
5. The workflow publishes the site at `https://gharbonnier78.github.io/mmals-ml-wiki/`.

## Editorial rule

> Never delete a published semantic URL. Redirect it, preserve its history, and explain its successor.

## Licenses

- Documentation and original explanatory content: CC BY 4.0
- Source code: MIT


## Research chronicle introduced in v0.2.0

The site now includes:

- a curated MMALS research story;
- an interactive, filterable event timeline;
- a branch and dependency map;
- a repository registry mapped to branches;
- a publication pipeline with separate GitHub, arXiv, HAL, and DOI fields;
- provenance governance for conversation-derived research events;
- a scheduled GitHub metadata refresh.

Raw chats are not published. Conversation material is summarized into reviewed event records and linked to public artifacts when possible.
