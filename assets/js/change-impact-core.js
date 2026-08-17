(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  root.ChangeImpactCore = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  const MECHANISM_TO_FAILURE = {
    call: 'functional', control: 'functional', schema: 'schema_mismatch',
    message: 'schema_mismatch', state: 'stale_state', timing: 'timeout',
    synchronization: 'race', resource: 'latency', configuration: 'misconfiguration',
    security: 'authorization', topology: 'availability', supplier: 'compatibility',
    device: 'acquisition', sensor: 'acquisition', data: 'data_shift', ml: 'model_shift'
  };

  function clamp01(x) { return Math.max(0, Math.min(1, Number(x))); }
  function sortedIds(obj) { return Object.keys(obj).sort(); }

  // Compact deterministic browser RNG. It intentionally does not claim NumPy-PCG64 parity.
  function mulberry32(seed) {
    let a = (seed >>> 0) || 1;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function graphFromEdges(scenario, edges) {
    const out = {};
    for (const id of sortedIds(scenario.nodes)) out[id] = [];
    edges.forEach((e, idx) => {
      if (!out[e.source]) out[e.source] = [];
      out[e.source].push(Object.assign({ key: `${e.mechanism || 'call'}:${idx}`, weight: 1, probability: 1 }, e));
    });
    Object.values(out).forEach(arr => arr.sort((a, b) => (a.target + a.key).localeCompare(b.target + b.key)));
    return out;
  }

  function allEdges(graph) {
    const edges = [];
    for (const source of Object.keys(graph)) for (const e of graph[source]) edges.push(Object.assign({ source }, e));
    return edges;
  }

  function hasEdge(graph, u, v) { return (graph[u] || []).some(e => e.target === v); }
  function indegree(graph, node) { let n = 0; for (const src of Object.keys(graph)) n += (graph[src] || []).filter(e => e.target === node).length; return n; }
  function outdegree(graph, node) { return (graph[node] || []).length; }

  function observeGraph(scenario, completeness = 0.78, falseEdgeRate = 0.03, seed = 11) {
    const rng = mulberry32(seed);
    const kept = [];
    for (const e of scenario.edges) {
      if (e.visible === false) continue;
      if (rng() <= clamp01(completeness)) kept.push(Object.assign({}, e, { observed: true }));
    }
    const graph = graphFromEdges(scenario, kept);
    const nodes = sortedIds(scenario.nodes);
    const candidates = [];
    for (const u of nodes) for (const v of nodes) if (u !== v && !hasEdge(graph, u, v)) candidates.push([u, v]);
    const nFalse = Math.round(falseEdgeRate * Math.max(1, scenario.edges.length));
    for (let pos = 0; pos < Math.min(nFalse, candidates.length); pos++) {
      const index = Math.floor(rng() * candidates.length);
      const pair = candidates.splice(index, 1)[0];
      graph[pair[0]].push({ source: pair[0], target: pair[1], mechanism: 'inferred_noise', probability: 0.25, weight: 0.25, visible: true, observed: true, synthetic_false_positive: true, key: `noise:${pos}` });
    }
    Object.values(graph).forEach(arr => arr.sort((a, b) => (a.target + a.key).localeCompare(b.target + b.key)));
    return graph;
  }

  function simulateChange(scenario, change, seed = 17, maxDepth = 8) {
    const rng = mulberry32(seed);
    const trueGraph = graphFromEdges(scenario, scenario.edges);
    const target = scenario.nodes[change.target];
    const impacted = {};
    impacted[change.target] = { node: change.target, via_mechanism: 'change', failure_mode: (target.failure_modes || ['functional'])[0], depth: 0, criticality: target.criticality };
    const queue = [[change.target, 0]], traversed_edges = [];
    while (queue.length) {
      const [current, depth] = queue.shift();
      if (depth >= maxDepth) continue;
      for (const e of (trueGraph[current] || [])) {
        const p = clamp01(Number(e.probability == null ? 1 : e.probability) * Number(change.magnitude == null ? 1 : change.magnitude));
        if (rng() > p) continue;
        traversed_edges.push([current, e.target, e.mechanism]);
        if (!impacted[e.target]) {
          const node = scenario.nodes[e.target];
          impacted[e.target] = { node: e.target, via_mechanism: e.mechanism, failure_mode: MECHANISM_TO_FAILURE[e.mechanism] || 'functional', depth: depth + 1, criticality: node.criticality };
          queue.push([e.target, depth + 1]);
        }
      }
    }
    return { change, impacted, traversed_edges, seed };
  }

  function bfsDistances(graph, source, allowed = null, maxHops = 5) {
    const dist = { [source]: 0 }, queue = [source];
    while (queue.length) {
      const u = queue.shift(), d = dist[u];
      if (d >= maxHops) continue;
      for (const e of (graph[u] || [])) {
        if (allowed && !allowed.has(e.mechanism)) continue;
        if (dist[e.target] == null) { dist[e.target] = d + 1; queue.push(e.target); }
      }
    }
    return dist;
  }

  function greedy(scenario, utilities, budget) {
    const ranked = Object.values(scenario.tests).slice().sort((a, b) => {
      const ua = Number(utilities[a.id] || 0), ub = Number(utilities[b.id] || 0);
      const ra = ua / Math.max(a.cost, 1e-9), rb = ub / Math.max(b.cost, 1e-9);
      if (Math.abs(rb - ra) > 1e-12) return rb - ra;
      if (Math.abs(ub - ua) > 1e-12) return ub - ua;
      if (a.cost !== b.cost) return a.cost - b.cost;
      return a.id.localeCompare(b.id);
    });
    const selected = []; let spent = 0;
    for (const t of ranked) {
      if ((utilities[t.id] || 0) <= 0) continue;
      if (budget != null && spent + t.cost > budget + 1e-12) continue;
      selected.push(t.id); spent += t.cost;
    }
    return selected;
  }

  function selectR0(scenario) {
    return { strategy: 'R0_full_suite', selected_tests: sortedIds(scenario.tests), predicted_impacts: sortedIds(scenario.nodes), scores: {} };
  }

  function selectR1(scenario, change, budget) {
    const scores = {};
    for (const t of Object.values(scenario.tests)) scores[t.id] = Number((t.historical_relevance || {})[change.category] || 0);
    const selected = greedy(scenario, scores, budget), pred = new Set();
    selected.forEach(id => scenario.tests[id].covers.forEach(n => pred.add(n)));
    return { strategy: 'R1_history', selected_tests: selected, predicted_impacts: Array.from(pred).sort(), scores };
  }

  function graphSelector(strategy, scenario, graph, change, budget, allowed, maxHops, riskWeighted) {
    const distances = bfsDistances(graph, change.target, allowed, maxHops);
    const predicted = new Set(Object.keys(distances));
    const utilities = {};
    for (const t of Object.values(scenario.tests)) {
      const generic = Math.max(0, ...Object.values(t.detects || {}).map(Number));
      if (!riskWeighted) {
        let count = 0; for (const n of t.covers) if (predicted.has(n)) count++;
        utilities[t.id] = count * generic;
      } else {
        let value = 0;
        for (const n of t.covers) if (predicted.has(n)) {
          const proximity = 1 / (1 + 0.25 * (distances[n] == null ? 7 : distances[n]));
          value += Number(scenario.nodes[n].criticality) * generic * proximity;
        }
        utilities[t.id] = value;
      }
    }
    return { strategy, selected_tests: greedy(scenario, utilities, budget), predicted_impacts: Array.from(predicted).sort(), scores: utilities };
  }

  function selectR2(scenario, graph, change, budget, maxHops = 5) { return graphSelector('R2_code_graph', scenario, graph, change, budget, new Set(['call', 'control']), maxHops, false); }
  function selectR3(scenario, graph, change, budget, maxHops = 5) { return graphSelector('R3_system_graph', scenario, graph, change, budget, null, maxHops, false); }
  function selectR4(scenario, graph, change, budget, maxHops = 5) { return graphSelector('R4_risk_aware', scenario, graph, change, budget, null, maxHops, true); }

  function sigmoid(z) { return z >= 0 ? 1 / (1 + Math.exp(-z)) : Math.exp(z) / (1 + Math.exp(z)); }
  function nodeFeatures(scenario, graph, change, candidate) {
    const dist = bfsDistances(graph, change.target, null, 12);
    const source = scenario.nodes[change.target], target = scenario.nodes[candidate];
    const shared = (source.tags || []).filter(x => (target.tags || []).includes(x)).length;
    return [dist[candidate] == null ? 0 : 1, Math.min(dist[candidate] == null ? 12 : dist[candidate], 12), shared, source.zone === target.zone ? 1 : 0, source.kind === target.kind ? 1 : 0, hasEdge(graph, change.target, candidate) ? 1 : 0, indegree(graph, candidate), outdegree(graph, candidate), Number(target.criticality), (target.tags || []).includes(change.category) ? 1 : 0];
  }

  // Small browser logistic baseline. It mirrors the feature contract of the Python baseline,
  // but uses deterministic gradient descent rather than scikit-learn's optimizer.
  function fitBrowserImpactLearner(scenario, graph, history, iterations = 300, lr = 0.08) {
    const X = [], y = [];
    for (const h of history) for (const candidate of sortedIds(scenario.nodes)) {
      X.push(nodeFeatures(scenario, graph, h.change, candidate)); y.push(h.impacted.has(candidate) ? 1 : 0);
    }
    const p = X[0].length, n = X.length;
    const mean = Array(p).fill(0), sd = Array(p).fill(0);
    for (const row of X) row.forEach((v, j) => mean[j] += v / n);
    for (const row of X) row.forEach((v, j) => sd[j] += (v - mean[j]) ** 2 / n);
    for (let j = 0; j < p; j++) sd[j] = Math.sqrt(sd[j]) || 1;
    const Z = X.map(row => row.map((v, j) => (v - mean[j]) / sd[j]));
    const pos = y.reduce((a, b) => a + b, 0), neg = n - pos;
    const wPos = pos ? n / (2 * pos) : 1, wNeg = neg ? n / (2 * neg) : 1;
    const w = Array(p + 1).fill(0);
    for (let it = 0; it < iterations; it++) {
      const g = Array(p + 1).fill(0);
      for (let i = 0; i < n; i++) {
        let z = w[0]; for (let j = 0; j < p; j++) z += w[j + 1] * Z[i][j];
        const pr = sigmoid(z), cw = y[i] ? wPos : wNeg, err = (pr - y[i]) * cw;
        g[0] += err; for (let j = 0; j < p; j++) g[j + 1] += err * Z[i][j];
      }
      for (let j = 0; j < w.length; j++) w[j] -= lr * g[j] / n;
    }
    return {
      predict(change) {
        const out = {};
        for (const id of sortedIds(scenario.nodes)) {
          const raw = nodeFeatures(scenario, graph, change, id).map((v, j) => (v - mean[j]) / sd[j]);
          let z = w[0]; raw.forEach((v, j) => z += w[j + 1] * v); out[id] = sigmoid(z);
        }
        return out;
      }
    };
  }

  function buildBrowserHistory(scenario, currentChange, seed = 117, repetitions = 8) {
    const history = []; let cursor = seed;
    for (const change of Object.values(scenario.changes)) {
      if (change.id === currentChange.id) continue;
      for (let rep = 0; rep < repetitions; rep++) {
        const outcome = simulateChange(scenario, change, cursor + rep);
        history.push({ change, impacted: new Set(Object.keys(outcome.impacted)) });
      }
      cursor += 100;
    }
    return history;
  }

  function selectR5(scenario, graph, change, budget, probabilities = null, threshold = 0.35, maxHops = 5) {
    const base = selectR4(scenario, graph, change, null, maxHops);
    if (!probabilities) {
      const history = buildBrowserHistory(scenario, change, 117, 8);
      probabilities = fitBrowserImpactLearner(scenario, graph, history).predict(change);
    }
    const predicted = new Set(base.predicted_impacts);
    for (const [n, p] of Object.entries(probabilities)) if (p >= threshold) predicted.add(n);
    const distances = bfsDistances(graph, change.target, null, maxHops), utilities = {};
    const baseSet = new Set(base.predicted_impacts);
    for (const t of Object.values(scenario.tests)) {
      const generic = Math.max(0, ...Object.values(t.detects || {}).map(Number)); let value = 0;
      for (const n of t.covers) if (predicted.has(n)) {
        const p = Math.max(Number(probabilities[n] || 0), baseSet.has(n) ? 0.55 : 0);
        const proximity = 1 / (1 + 0.25 * (distances[n] == null ? maxHops + 2 : distances[n]));
        value += Number(scenario.nodes[n].criticality) * generic * p * proximity;
      }
      utilities[t.id] = value;
    }
    return { strategy: 'R5_ai_assisted', selected_tests: greedy(scenario, utilities, budget), predicted_impacts: Array.from(predicted).sort(), scores: utilities, probabilities };
  }

  function selectionCost(scenario, selection) { return selection.selected_tests.reduce((s, id) => s + Number(scenario.tests[id].cost), 0); }
  function detectionProbability(scenario, selection, nodeId, failureMode) {
    let miss = 1;
    for (const id of selection.selected_tests) {
      const t = scenario.tests[id]; if (!(t.covers || []).includes(nodeId)) continue;
      const p = clamp01((t.detects || {})[failureMode] != null ? t.detects[failureMode] : ((t.detects || {})['*'] || 0));
      miss *= 1 - p;
    }
    return 1 - miss;
  }
  function ratio(num, den, dflt = 1) { return den === 0 ? dflt : num / den; }
  function evaluateSelection(scenario, outcome, selection) {
    const trueNodes = new Set(Object.keys(outcome.impacted)), critical = new Set(Object.values(outcome.impacted).filter(e => Number(e.criticality) >= 4).map(e => e.node));
    const predicted = new Set(selection.predicted_impacts), covered = new Set();
    selection.selected_tests.forEach(id => scenario.tests[id].covers.forEach(n => covered.add(n)));
    const pods = {}; for (const [n, e] of Object.entries(outcome.impacted)) pods[n] = detectionProbability(scenario, selection, n, e.failure_mode);
    const vals = Object.values(pods), cp = Array.from(critical).map(n => pods[n]);
    const intersect = (a, b) => Array.from(a).filter(x => b.has(x)).length;
    const mean = arr => arr.length ? arr.reduce((a, b) => a + b, 0) / arr.length : 1;
    return {
      strategy: selection.strategy, tests_executed: selection.selected_tests.length, execution_cost: selectionCost(scenario, selection),
      impact_recall: ratio(intersect(predicted, trueNodes), trueNodes.size, 0), critical_impact_recall: ratio(intersect(predicted, critical), critical.size, 1),
      impacted_node_coverage: ratio(intersect(covered, trueNodes), trueNodes.size, 1), critical_node_coverage: ratio(intersect(covered, critical), critical.size, 1),
      mean_pod: mean(vals), critical_mean_pod: mean(cp), critical_min_pod: cp.length ? Math.min(...cp) : 1,
      critical_regression_miss_rate: cp.length ? cp.filter(p => p <= 0).length / cp.length : 0
    };
  }

  function buildFaultCatalogue(scenario, criticalOnly = false) {
    const faults = [];
    for (const node of Object.values(scenario.nodes)) {
      if (criticalOnly && Number(node.criticality) < 4) continue;
      for (const mode of (node.failure_modes || [])) faults.push({ id: `F_${node.id}_${mode}`, node: node.id, failure_mode: mode, criticality: node.criticality });
    }
    return faults;
  }
  function evaluateFault(scenario, selection, fault) {
    const covered = selection.selected_tests.some(id => scenario.tests[id].covers.includes(fault.node));
    const pod = detectionProbability(scenario, selection, fault.node, fault.failure_mode);
    return Object.assign({}, fault, { covered, pod });
  }

  function fixtureGraph(scenario, fixture) {
    return graphFromEdges(scenario, fixture.observed_edges.map((e, idx) => Object.assign({ probability: 1, visible: true, key: `fixture:${idx}` }, e)));
  }
  function fixtureOutcome(scenario, fixture) {
    return { change: scenario.changes[fixture.config.change_id], impacted: fixture.impacted, traversed_edges: fixture.traversed_edges, seed: fixture.config.propagation_seed };
  }
  function runStrategies(scenario, graph, change, budget, r5Probabilities = null, aiThreshold = 0.35) {
    return {
      R0: selectR0(scenario), R1: selectR1(scenario, change, budget), R2: selectR2(scenario, graph, change, budget),
      R3: selectR3(scenario, graph, change, budget), R4: selectR4(scenario, graph, change, budget), R5: selectR5(scenario, graph, change, budget, r5Probabilities, aiThreshold)
    };
  }

  return { MECHANISM_TO_FAILURE, mulberry32, graphFromEdges, allEdges, observeGraph, simulateChange, bfsDistances, greedy, selectR0, selectR1, selectR2, selectR3, selectR4, selectR5, fitBrowserImpactLearner, buildBrowserHistory, detectionProbability, evaluateSelection, buildFaultCatalogue, evaluateFault, fixtureGraph, fixtureOutcome, runStrategies, selectionCost };
});