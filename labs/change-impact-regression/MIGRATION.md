# Change Impact & Regression Evidence — migration record

## Canonical home

This interactive lab belongs in `gharbonnier78/mmals-ml-wiki`, the Diderot MMALS / ML Interactive Encyclopedia.

The first executable prototype was mistakenly implemented in `gharbonnier78/diderot-machine-learning-specialization`, draft PR #3 (`lab: add change-impact regression simulator`). That repository remains useful as the original Python implementation and migration source, but it is not the canonical public home of the lab.

## Source implementation retained for migration

The source prototype provides:

- a synthetic distributed identity-platform scenario;
- hidden `G_true` versus incomplete/noisy `G_observed`;
- stochastic change propagation;
- R0–R5 regression strategies;
- failure-mode-specific detection probabilities;
- explicit fault injection;
- Monte Carlo completeness experiments;
- Python tests and notebook visualizations.

The governance and methodological claims remain in the private Test Authority engineering-governance repository. Diderot is the interactive explanatory and experimental surface.

## Cross-implementation contract

`data/change-impact-regression/parity-v0.json` freezes a reference run reconstructed from the Python implementation with:

- change `CHG_CACHE_TTL`;
- graph seed `11`;
- propagation seed `17`;
- observed-graph completeness `0.78`;
- false-edge rate `0.03`;
- execution budget `22`;
- R5 probability threshold `0.35`.

The browser core must reproduce, on this frozen observed graph and hidden outcome:

1. R0–R5 selected test lists;
2. R0–R5 predicted impact sets;
3. impact recall and critical-impact recall;
4. impacted-node coverage;
5. mean and critical POD metrics;
6. the explicit invariant `covered == true` with `POD == 0` for a failure mode not observed by the selected oracles.

CI runs `node scripts/check_change_impact_parity.js`.

## RNG boundary

The Python source uses NumPy PCG64. The browser uses a small deterministic JavaScript PRNG for interactive synthetic worlds. Arbitrary browser seeds are therefore **not** claimed to reproduce NumPy sample-for-sample.

The migration parity fixture isolates the deterministic selector/evaluation contract from the RNG implementation. Exact cross-language RNG parity can be added later if it provides research value.

## R5 boundary

The Python source uses standardized logistic regression from scikit-learn. The browser interactive mode trains a small deterministic logistic baseline with the same feature contract but a different optimizer. The frozen parity mode supplies the Python probabilities directly and verifies R5 selection/evaluation parity.

No superiority claim is attached to R5. Ties and regressions against R4 are valid results.

## Completion rule

The misplaced Diderot-specialization PR should be closed as superseded only after:

- this Diderot-wiki PR passes internal-link, release-consistency, and parity CI;
- the interactive lab is reviewable in the canonical repository;
- no migration-only information remains unique to the misplaced PR.
