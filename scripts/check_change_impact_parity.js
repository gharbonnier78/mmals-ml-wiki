#!/usr/bin/env node
'use strict';
const fs = require('fs');
const path = require('path');
const core = require(path.join(__dirname, '..', 'assets', 'js', 'change-impact-core.js'));
const scenario = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', 'change-impact-regression', 'identity-platform.json'), 'utf8'));
const fixture = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', 'change-impact-regression', 'parity-v0.json'), 'utf8'));

function fail(msg) { console.error('PARITY FAIL:', msg); process.exitCode = 1; }
function close(a, b, eps = 1e-10) { return Math.abs(Number(a) - Number(b)) <= eps; }
function sameArray(a, b) { return JSON.stringify(a) === JSON.stringify(b); }

const graph = core.fixtureGraph(scenario, fixture);
const outcome = core.fixtureOutcome(scenario, fixture);
const change = scenario.changes[fixture.config.change_id];
const r5p = fixture.strategies.R5.probabilities;
const selections = core.runStrategies(scenario, graph, change, fixture.config.budget, r5p, fixture.config.ai_threshold);

for (const label of ['R0','R1','R2','R3','R4','R5']) {
  const expected = fixture.strategies[label];
  const actual = selections[label];
  if (!sameArray(actual.selected_tests, expected.selected_tests)) {
    fail(`${label} selected_tests mismatch\n expected=${JSON.stringify(expected.selected_tests)}\n actual=${JSON.stringify(actual.selected_tests)}`);
  }
  if (!sameArray(actual.predicted_impacts.slice().sort(), expected.predicted_impacts.slice().sort())) fail(`${label} predicted_impacts mismatch`);
  const evalActual = core.evaluateSelection(scenario, outcome, actual);
  for (const [metric, value] of Object.entries(expected.evaluation)) {
    if (!(metric in evalActual)) continue;
    if (!close(evalActual[metric], value)) fail(`${label} ${metric}: expected ${value}, got ${evalActual[metric]}`);
  }
}

const fault = { id: 'F_PARITY_COVERED_ZERO_POD', node: 'identity_service', failure_mode: 'schema_mismatch', criticality: 5 };
const f = core.evaluateFault(scenario, selections.R2, fault);
if (!f.covered) fail('fault invariant expected covered=true');
if (!close(f.pod, 0)) fail(`fault invariant expected POD=0, got ${f.pod}`);

if (!process.exitCode) console.log('Change-impact parity OK: R0-R5 migration fixture + covered/POD=0 invariant.');