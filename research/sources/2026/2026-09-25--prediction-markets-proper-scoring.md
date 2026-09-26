---
title: "Collective forecasting, prediction markets, meta-predictions, and proper scoring — source synthesis"
publication_date: "2026-09-25"
updated_at: "2026-09-26"
source_type: "Diderot synthesis of external primary/peer-reviewed sources"
relevance: "P0"
evidence_quality: "foundational theory plus forecasting/corporate/experimental evidence"
related_concepts: ["collective forecasting", "prediction market", "proper scoring rule", "Brier score", "forecast calibration", "meta-prediction", "Brier diversity identity"]
retention_verdict: "retain"
---

# Source synthesis

## Core sources

- Brier, G. W. (1950), *Verification of Forecasts Expressed in Terms of Probability*.
- Gneiting, T. & Raftery, A. E. (2007), *Strictly Proper Scoring Rules, Prediction, and Estimation*, DOI 10.1198/016214506000001437.
- Chen, K.-Y. & Plott, C. R. (2002), *Information Aggregation Mechanisms: Concept, Design and Implementation for a Sales Forecasting Problem*.
- Cowgill, B., Wolfers, J. & Zitzewitz, E. (2009), *Using Prediction Markets to Track Information Flows: Evidence from Google*, DOI 10.1007/978-3-642-03821-1_2.
- Cowgill, B. & Zitzewitz, E. (2015), *Corporate Prediction Markets: Evidence from Google, Ford, and Firm X*, DOI 10.1093/restud/rdv014.
- Atanasov, P. et al. (2017), *Distilling the Wisdom of Crowds: Prediction Markets vs. Prediction Polls*, DOI 10.1287/mnsc.2015.2374.
- Dana, J., Atanasov, P., Tetlock, P. & Mellers, B. (2019), *Are Markets More Accurate than Polls? The Surprising Informational Value of Just Asking*, DOI 10.1017/S1930297500003375.
- Baron, J. et al. (2014), *Two Reasons to Make Aggregated Probability Forecasts More Extreme*, DOI 10.1287/deca.2014.0293.
- Palley, A. B. & Soll, J. B. (2019), *Extracting the Wisdom of Crowds When Information Is Shared*, DOI 10.1287/mnsc.2018.3047.
- Martinie, M., Wilkening, T. & Howe, P. D. L. (2020), *Using Meta-Predictions to Identify Experts in the Crowd When Past Performance Is Unknown*, DOI 10.1371/journal.pone.0232058.
- Peker, C. & Wilkening, T. (2025), *Robust Recalibration of Aggregate Probability Forecasts Using Meta-Beliefs*, DOI 10.1016/j.ijforecast.2024.09.005.
- Buehler, R., Griffin, D. & Ross, M. (1994), *Exploring the Planning Fallacy*, DOI 10.1037/0022-3514.67.3.366.
- Howard, R. A. (1988), *Decision Analysis: Practice and Promise*, DOI 10.1287/mnsc.34.6.679.
- Chen, Y. & Wortman Vaughan, J. (2010), *A New Understanding of Prediction Markets via No-Regret Learning*, ACM EC '10 / arXiv:1003.0034.

## What the sources support

Prediction markets are one mechanism for information aggregation. LMSR prices have a softmax form over outstanding shares, and convex cost-function market makers have a no-regret/FTRL interpretation in the learning-theory literature. Direct probability elicitation and carefully designed non-market aggregation are serious comparators. Simple averaging can be conservative; shared information can correlate errors; meta-predictions can provide additional information about shared beliefs or latent expertise. Proper scoring rules provide principled evaluation of probabilistic forecasts, while Brier loss supplies a concrete squared-error score.

Actor/observer differences and corporate-market biases are relevant threats when forecasters can influence or identify with the outcome. These findings motivate design factors; they do not provide transferable engineering effect sizes.

## Brier convention

Diderot's binary page uses the normalized one-component loss BS(p,y)=(p-y)^2. Brier's original categorical score sums squared error across outcome categories, which equals 2(p-y)^2 for a binary two-category vector. The convention must be stated when comparing numbers.

## Boundary

None of these sources establishes that prediction markets, private polls, meta-prediction recalibration, or any specific aggregation rule is superior for engineering qualification or release readiness. Market prices and crowd aggregates are forecasts, not ground truth, causal effects or governance decisions.

The Engineering Collective Forecasting project's fixed meta-belief transform is project-local. It is inspired by the meta-prediction/shared-information literature and is not represented as an exact implementation of any cited algorithm.
