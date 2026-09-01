(() => {
  'use strict';

  const clamp = (x, lo = 0, hi = 1) => Math.max(lo, Math.min(hi, x));
  const fmt = (x, digits = 3) => Number(x).toFixed(digits);

  function posterior(prior, likelihoodObsGivenFault, likelihoodObsGivenHealthy) {
    const num = prior * likelihoodObsGivenFault;
    const den = num + (1 - prior) * likelihoodObsGivenHealthy;
    return den === 0 ? prior : clamp(num / den);
  }

  function entropyBernoulli(p) {
    const q = clamp(p, 1e-12, 1 - 1e-12);
    return -(q * Math.log2(q) + (1 - q) * Math.log2(1 - q));
  }

  function actionForRisk(p, threshold) {
    return p >= threshold ? 'ADAPT' : 'REUSE';
  }

  function certainty(p) {
    return Math.abs(p - 0.5) * 2;
  }

  function contingentValues({ gamma, probeCost }) {
    const immediate = { reuse: 4, probe: -probeCost };
    const reuseContinuation = 4;
    const situationAProbeContinuation = 4;
    const situationBProbeContinuation = 12;
    return {
      q1: immediate,
      a: {
        reuse: immediate.reuse + gamma * reuseContinuation,
        probe: immediate.probe + gamma * situationAProbeContinuation,
      },
      b: {
        reuse: immediate.reuse + gamma * reuseContinuation,
        probe: immediate.probe + gamma * situationBProbeContinuation,
      },
    };
  }

  function el(id) {
    return document.getElementById(id);
  }

  function setText(id, value) {
    const node = el(id);
    if (node) node.textContent = value;
  }

  function renderBeliefUpdate() {
    const prior = Number(el('belief-prior').value);
    const tpr = Number(el('sensor-tpr').value);
    const fpr = Number(el('sensor-fpr').value);
    const obs = el('sensor-observation').value;
    const lf = obs === 'warning' ? tpr : 1 - tpr;
    const lh = obs === 'warning' ? fpr : 1 - fpr;
    const post = posterior(prior, lf, lh);

    setText('belief-prior-value', fmt(prior, 2));
    setText('sensor-tpr-value', fmt(tpr, 2));
    setText('sensor-fpr-value', fmt(fpr, 2));
    setText('posterior-value', fmt(post, 3));
    setText('entropy-before', fmt(entropyBernoulli(prior), 3));
    setText('entropy-after', fmt(entropyBernoulli(post), 3));
    el('posterior-bar').style.width = `${post * 100}%`;
  }

  function renderCertaintyDecision() {
    const before = Number(el('decision-before').value);
    const after = Number(el('decision-after').value);
    const threshold = Number(el('decision-threshold').value);
    const beforeAction = actionForRisk(before, threshold);
    const afterAction = actionForRisk(after, threshold);
    const changed = beforeAction !== afterAction;
    const moreCertain = certainty(after) > certainty(before);

    setText('decision-before-value', fmt(before, 2));
    setText('decision-after-value', fmt(after, 2));
    setText('decision-threshold-value', fmt(threshold, 2));
    setText('decision-before-action', beforeAction);
    setText('decision-after-action', afterAction);
    setText('decision-change', changed ? 'YES — the action changed' : 'NO — same action');
    setText('certainty-change', moreCertain ? 'certainty increased' : 'certainty did not increase');
    el('decision-change').dataset.changed = changed ? 'true' : 'false';
  }

  function bestLabel(values) {
    return values.probe > values.reuse ? 'PROBE' : 'REUSE';
  }

  function renderContingentPlan() {
    const gamma = Number(el('contingent-gamma').value);
    const probeCost = Number(el('contingent-cost').value);
    const v = contingentValues({ gamma, probeCost });

    setText('contingent-gamma-value', fmt(gamma, 2));
    setText('contingent-cost-value', fmt(probeCost, 2));
    setText('q1-reuse-a', fmt(v.q1.reuse));
    setText('q1-probe-a', fmt(v.q1.probe));
    setText('q1-reuse-b', fmt(v.q1.reuse));
    setText('q1-probe-b', fmt(v.q1.probe));
    setText('h2-a-reuse', fmt(v.a.reuse));
    setText('h2-a-probe', fmt(v.a.probe));
    setText('h2-b-reuse', fmt(v.b.reuse));
    setText('h2-b-probe', fmt(v.b.probe));
    setText('h2-a-best', bestLabel(v.a));
    setText('h2-b-best', bestLabel(v.b));

    const diverges = bestLabel(v.a) !== bestLabel(v.b);
    setText('contingent-verdict', diverges
      ? 'Same one-step values, different best contingent plans.'
      : 'At these parameters the plans do not diverge; lower probe cost or raise γ to recover the mechanism.');
    el('contingent-verdict').dataset.diverges = diverges ? 'true' : 'false';
  }

  function bind(ids, fn) {
    ids.forEach((id) => {
      const node = el(id);
      if (node) {
        node.addEventListener('input', fn);
        node.addEventListener('change', fn);
      }
    });
    fn();
  }

  function boot() {
    bind(['belief-prior', 'sensor-tpr', 'sensor-fpr', 'sensor-observation'], renderBeliefUpdate);
    bind(['decision-before', 'decision-after', 'decision-threshold'], renderCertaintyDecision);
    bind(['contingent-gamma', 'contingent-cost'], renderContingentPlan);
  }

  window.DiderotBeliefLab = {
    posterior,
    entropyBernoulli,
    actionForRisk,
    certainty,
    contingentValues,
    renderBeliefUpdate,
    renderCertaintyDecision,
    renderContingentPlan,
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
