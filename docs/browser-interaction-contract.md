# Browser interaction contract

## Purpose

Diderot is a static public teaching site, but some pedagogical claims are expressed through browser interactions rather than prose alone. When the interaction is material to understanding, source-level checks are not enough: the repository should also prove that a user can load the public page, manipulate the declared controls, observe the expected state changes, and follow the intended navigation path.

This document is an engineering/test contract. It does **not** promote UI behavior, screenshots or browser telemetry to scientific evidence.

## Scope

Current reference interaction:

- `labs/belief-adaptive-planning/index.html`
- `assets/js/belief-adaptive-planning.js`
- `tests/browser/run_belief_adaptive_planning_browser.py`

The lab is deterministic. Its numerical construction is a pedagogical mechanism demonstration, not Toy F2 qualification evidence.

## Human-equivalent smoke path

The browser test must drive public controls rather than call hidden scientific helpers as a substitute for the user path. It verifies that a competent human can:

1. open the lab over HTTP;
2. change the observation and prior in the belief-update toy and observe the posterior update;
3. increase certainty while remaining on the same decision side, then cross the threshold and observe an action change;
4. inspect two situations with identical one-step values but different default finite-horizon contingent choices;
5. alter the probe cost until the contingent distinction disappears;
6. navigate from the lab to the guided pathway.

The test may inspect DOM attributes or text after operating the public controls. Those assertions are engineering evidence for the rendered interaction contract, not evidence for the underlying scientific hypothesis.

## Reproducible execution

```bash
python scripts/prepare_pages.py
python -m pip install -r requirements-browser.txt
python -m playwright install chromium
python tests/browser/run_belief_adaptive_planning_browser.py
```

CI uses `python -m playwright install --with-deps chromium` because GitHub-hosted runners need browser system dependencies.

## Failure classes

A failed browser smoke must be classified before drawing conclusions:

- page/runtime failure — JavaScript or browser behavior is broken;
- interaction-contract failure — controls load but declared behavior is not produced;
- navigation failure — linked pedagogical route is inaccessible;
- dependency/infrastructure failure — Playwright/browser installation or CI environment failed;
- scientific disagreement — **not inferable from this test**.

A passing smoke means only that the public pedagogical mechanism is executable as declared.

## Security and operational boundary

The site is static and has no authenticated user data, writable backend, secret-bearing browser API or privileged mutation path in this lab. Browser automation therefore exercises a low-impact public surface. If future Diderot labs add network writes, user data, external model calls or credentials, this contract is insufficient and the engineering/security profile must be escalated before deployment.

## Review expectation

An independent reviewer should inspect both the deterministic equations in `belief-adaptive-planning.js` and the browser path. The reviewer should challenge whether the UI accidentally makes a project hypothesis look like scientific evidence, whether the controls can produce falsifying/boundary cases, and whether the automated path really uses the public interaction rather than bypassing it.
