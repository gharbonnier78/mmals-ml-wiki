# Chronicle — 2026-09-27 — PR #33 accepted; final text corrections

Status: **append-only pedagogical verification record**

## Independent verification disposition

Bounded verification of PR #33 at head `ee06e53383f260d2fe18366f631834ab3ffe3c82` returned **ACCEPT**.

The verifier rendered the formulas in a real browser with MathJax and confirmed zero rendering errors. The new fail-closed check also detected all five intentionally reintroduced defects.

## Final non-review correction

One mathematical wording issue remains before merge: the proper-scoring-rule canonical inequality is currently written in the orientation for a score to be maximized, while Diderot teaches the Brier quantity as a **loss** to be minimized.

The canonical proper-loss inequality is therefore corrected so that truthful reporting minimizes expected loss.

## Legacy follow-up

A pre-existing EcoSpec page still shows a MathJax input error. It predates this PR and sits outside the forecasting-family consistency contract. It will be repaired without changing the accepted forecasting content.

## Merge dependency

PR #33 should still be merged only after Engineering Collective Forecasting PR #1, then re-pinned to the merged research commit and replayed through CI.
