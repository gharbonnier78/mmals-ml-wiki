# Research triage before qualification

## Why this page exists

A research programme can waste substantial time if every early hypothesis is treated as if it already deserves publication-grade qualification.

The opposite failure is just as dangerous: a quick exploratory result is treated as if it were already robust enough to support a scientific claim.

The useful middle ground is **progressive evidence escalation**.

## Two different questions

Exploratory screening answers:

> Is there enough signal here to justify more work?

Qualification answers:

> Is the claim strong enough, under a frozen decision rule and adequate uncertainty model, to support a consequential scientific or engineering decision?

These are not the same question and should not carry the same cost.

## Stage A — exploratory screening

A screening experiment may intentionally be cheaper:

- fewer predeclared seeds;
- smaller compute budget;
- development or screening data only;
- lightweight uncertainty estimates;
- fast matched controls and ablations;
- no access to untouched qualification TEST data.

Its result must be labelled `EXPLORATORY` (or equivalent). It may justify **continue / stop / redirect**, but not a confirmatory claim.

A negative screening result is useful evidence: it can save the cost of a full qualification campaign.

## Stage B — qualification

If screening shows a plausible signal, surprising contradiction, important decision boundary or sufficient engineering value, the evidence burden escalates.

Qualification may require:

- preregistered estimands and margins;
- frozen datasets and decision rules;
- adequate statistical unit and uncertainty model;
- immutable replay artifacts;
- declared randomness and concurrency semantics;
- provenance and hashes;
- independent review;
- explicit bounded claim wording.

The key rule is simple:

> Screening can decide whether to invest in qualification. Screening cannot become qualification by reinterpretation.

## When a full correction is still necessary

Sometimes the expensive path is unavoidable. If a methodological defect is discovered in evidence that has already become foundational, the correct question is no longer “is the direction promising?” but “could the defect have changed the decision?”.

Then a full correction may be necessary even when the headline result appears unsurprising.

The Siamese embedding-compression Study 0 provided a useful example: the corrected subject-level uncertainty was materially wider than the original pair-level uncertainty, while the bounded negative conclusion remained unchanged. The effort was therefore not wasted; it established that the earlier analysis had been too confident and that the surviving conclusion was robust to the correction.

## What to preserve

For every branch, even one stopped during screening, preserve at least:

- the question asked;
- the evidence mode (`SCREENING` or `QUALIFICATION`);
- the data role used;
- the decision to continue, stop or redirect;
- the reason for escalation if qualification is triggered;
- the main negative result if the branch is abandoned.

This prevents research history from becoming a collection of only successful stories.

## Practical anti-patterns

- Full qualification before checking whether the signal is worth the cost.
- Repeatedly opening the qualification TEST set during exploration.
- Selecting favorable seeds after seeing screening outcomes.
- Treating “not demonstrated” as “proved inferior”.
- Treating a corrected but unchanged conclusion as proof that the original method was sound.
- Hiding negative exploratory branches.
- Adding ceremony that cannot change the decision or evidence quality.

## Decision heuristic

Use the lightest evidence burden that is sufficient for the decision currently being made, then escalate explicitly when the consequence of the decision increases.

This is not lower rigor. It is **rigor applied at the right time**.

## Case origin

This lesson was distilled from the August 2026 correction and replay work in `gharbonnier78/siamese-embedding-compression-lab`, Study 0 / v0.2.2. The reusable content here is methodological; the biometric domain conclusion remains in the source repository.