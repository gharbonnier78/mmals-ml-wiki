# Curated source notes

This directory is the durable intake layer for external sources that materially contribute to Diderot / MMALS / ML research and related engineering learning.

## Retention rule

A discovery channel (Google Alerts, web search, newsletter, conversation, conference feed, etc.) is not itself evidence. Retain only the underlying source when it adds a useful claim, method, dataset, benchmark, negative result, engineering practice, standard, or research lead.

Do not store raw alert emails or raw chat transcripts here. Store one Markdown note per retained underlying source.

## Processing contract

1. Resolve the underlying source and canonical URL; do not treat the Google Alert wrapper as the source.
2. Read enough of the original source to assess its actual contribution.
3. Prefer primary papers, standards, official technical documentation, datasets, repositories, institutional publications, and direct experimental reports over secondary summaries.
4. Check important claims against stronger or independent evidence when practical.
5. Record what the source supports, what it does not support, and any uncertainty or marketing/hype risk.
6. Link the source to relevant Diderot concepts, experiments, repositories, hypotheses, or learning pathways only when technically justified.
7. Do not elevate a source to project evidence merely because it is interesting. Use the evidence-status taxonomy in `docs/evidence-status.md` when a project claim is affected.
8. After a discovery email has been fully processed, it may be deleted from the inbox only when all retained notes have been successfully committed. If persistence fails, keep the email for retry.

## File convention

Use:

`research/sources/YYYY/YYYY-MM-DD--short-stable-slug.md`

If several sources would produce the same slug, add the publisher or a short disambiguator.

## Minimum note content

Each retained source note should identify: title; canonical URL; author/publisher; publication date when known; discovery channel and alert topic; review date; source type; relevance; evidence quality; related tracks or concepts; retention verdict; central claim or contribution; evidence actually provided; limitations and uncertainty; consequences for current work; and any concrete follow-up experiment, reading, repository change, or falsification test.

The note must distinguish source-derived facts from reviewer inference.
