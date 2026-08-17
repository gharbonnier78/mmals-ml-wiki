(async function () {
  'use strict';
  const C = globalThis.ChangeImpactCore;
  if (!C) throw new Error('ChangeImpactCore not loaded');

  const [scenario, fixture] = await Promise.all([
    fetch('../../data/change-impact-regression/identity-platform.json').then(r => r.json()),
    fetch('../../data/change-impact-regression/parity-v0.json').then(r => r.json())
  ]);

  const el = id => document.getElementById(id);
  const changeSel = el('cirChange'), strategySel = el('cirStrategy'), completeness = el('cirCompleteness'), falseRate = el('cirFalseRate'), budget = el('cirBudget'), seed = el('cirSeed');
  let state = null, reveal = false, injectedFault = null;

  const positions = {
    citizen_app:[70,110], api_gateway:[200,110], enrollment_service:[345,65], identity_service:[500,50], auth_service:[500,150], biometric_service:[500,250], risk_engine:[660,65],
    event_bus:[660,165], identity_db:[660,265], audit_db:[815,55], session_cache:[660,365], config_service:[500,360], policy_service:[815,155], kms:[815,255],
    device_adapter:[500,470], capture_device:[345,500], supplier_sdk:[200,500], ml_model:[815,365], feature_store:[815,470], observability:[950,250]
  };

  for (const c of Object.values(scenario.changes)) {
    const o = document.createElement('option'); o.value = c.id; o.textContent = `${c.id.replace('CHG_','')} — ${c.description}`; changeSel.appendChild(o);
  }
  changeSel.value = 'CHG_CACHE_TTL';

  function selectedCovered(selection) {
    const s = new Set(); selection.selected_tests.forEach(id => scenario.tests[id].covers.forEach(n => s.add(n))); return s;
  }

  function makeSynthetic() {
    const s = Number(seed.value || 11), ch = scenario.changes[changeSel.value];
    const graph = C.observeGraph(scenario, Number(completeness.value), Number(falseRate.value), s);
    const outcome = C.simulateChange(scenario, ch, s + 6);
    const selections = C.runStrategies(scenario, graph, ch, Number(budget.value), null, 0.35);
    const evaluations = {}; for (const [k, v] of Object.entries(selections)) evaluations[k] = C.evaluateSelection(scenario, outcome, v);
    return { mode:'synthetic', graph, outcome, selections, evaluations, change:ch, note:'Browser stochastic simulation. R5 uses a deterministic browser logistic baseline trained on simulated prior changes; it is not scikit-learn numerical parity.' };
  }

  function makeOracle() {
    const graph = C.fixtureGraph(scenario, fixture), outcome = C.fixtureOutcome(scenario, fixture), ch = scenario.changes[fixture.config.change_id];
    const selections = C.runStrategies(scenario, graph, ch, fixture.config.budget, fixture.strategies.R5.probabilities, fixture.config.ai_threshold);
    const evaluations = {}; for (const [k, v] of Object.entries(selections)) evaluations[k] = C.evaluateSelection(scenario, outcome, v);
    changeSel.value = fixture.config.change_id; completeness.value = fixture.config.completeness; falseRate.value = fixture.config.false_edge_rate; budget.value = fixture.config.budget; seed.value = fixture.config.graph_seed;
    return { mode:'oracle', graph, outcome, selections, evaluations, change:ch, note:'Python migration oracle: frozen NumPy/scikit-learn output from the original Diderot-specialization implementation. R0-R5 selections and metrics are parity-checked in CI.' };
  }

  function pct(x) { return `${Math.round(100 * Number(x))}%`; }
  function metricClass(v, inverse=false) { const x = Number(v); const z = inverse ? 1-x : x; return z >= .8 ? 'cir-good' : z >= .5 ? 'cir-warn' : 'cir-bad'; }

  function renderMetrics() {
    const label = strategySel.value, ev = state.evaluations[label], sel = state.selections[label];
    el('cirMetricTests').textContent = ev.tests_executed;
    el('cirMetricCost').textContent = ev.execution_cost.toFixed(0);
    el('cirMetricRecall').textContent = pct(ev.impact_recall); el('cirMetricRecall').className = `value ${metricClass(ev.impact_recall)}`;
    el('cirMetricCriticalRecall').textContent = pct(ev.critical_impact_recall); el('cirMetricCriticalRecall').className = `value ${metricClass(ev.critical_impact_recall)}`;
    el('cirMetricCoverage').textContent = pct(ev.impacted_node_coverage); el('cirMetricCoverage').className = `value ${metricClass(ev.impacted_node_coverage)}`;
    el('cirMetricPod').textContent = pct(ev.critical_mean_pod); el('cirMetricPod').className = `value ${metricClass(ev.critical_mean_pod)}`;
    el('cirMetricMiss').textContent = pct(ev.critical_regression_miss_rate); el('cirMetricMiss').className = `value ${metricClass(ev.critical_regression_miss_rate,true)}`;
    el('cirSelectedTests').textContent = sel.selected_tests.join(' · ');
  }

  function edgeKey(e) { return `${e.source}|${e.target}|${e.mechanism}`; }
  function svgEl(name, attrs={}) { const n = document.createElementNS('http://www.w3.org/2000/svg', name); Object.entries(attrs).forEach(([k,v]) => n.setAttribute(k,v)); return n; }
  function renderGraph() {
    const svg = el('cirGraph'); svg.innerHTML = '';
    const defs = svgEl('defs'); const marker = svgEl('marker',{id:'cirArrow',viewBox:'0 0 10 10',refX:'9',refY:'5',markerWidth:'5',markerHeight:'5',orient:'auto-start-reverse'}); marker.appendChild(svgEl('path',{d:'M 0 0 L 10 5 L 0 10 z',fill:'currentColor'})); defs.appendChild(marker); svg.appendChild(defs);
    const observed = C.allEdges(state.graph), obsKeys = new Set(observed.map(edgeKey));
    let edges = observed.map(e => ({...e, cls:e.synthetic_false_positive?'cir-edge noise':'cir-edge'}));
    if (reveal) for (const e of scenario.edges) if (!obsKeys.has(edgeKey(e))) edges.push({...e,cls:'cir-edge hidden-truth'});
    for (const e of edges) {
      const a = positions[e.source], b = positions[e.target]; if (!a || !b) continue;
      const line = svgEl('line',{x1:a[0],y1:a[1],x2:b[0],y2:b[1],class:e.cls,'marker-end':'url(#cirArrow)'}); const title=svgEl('title'); title.textContent=`${e.source} → ${e.target} · ${e.mechanism}`; line.appendChild(title); svg.appendChild(line);
    }
    const sel = state.selections[strategySel.value], pred = new Set(sel.predicted_impacts), cov = selectedCovered(sel), actual = new Set(Object.keys(state.outcome.impacted));
    for (const [id,node] of Object.entries(scenario.nodes)) {
      const p=positions[id]; if(!p) continue; const classes=['cir-node']; if(id===state.change.target)classes.push('changed'); if(pred.has(id))classes.push('predicted'); if(cov.has(id))classes.push('covered'); if(reveal&&actual.has(id))classes.push('actual'); if(injectedFault&&injectedFault.node===id)classes.push('fault');
      const g=svgEl('g',{class:classes.join(' '),transform:`translate(${p[0]},${p[1]})`});
      g.appendChild(svgEl('circle',{r:Number(node.criticality)>=5?25:21})); const t=svgEl('text',{'text-anchor':'middle',y:'-2'}); t.textContent=id.replaceAll('_',' '); g.appendChild(t); const k=svgEl('text',{'text-anchor':'middle',y:'12',class:'kind'}); k.textContent=`${node.kind} · C${node.criticality}`; g.appendChild(k); svg.appendChild(g);
    }
  }

  function renderTable() {
    const body=el('cirCompareBody'); body.innerHTML='';
    for(const label of ['R0','R1','R2','R3','R4','R5']){
      const e=state.evaluations[label], tr=document.createElement('tr'); if(label===strategySel.value)tr.className='active';
      const vals=[label,e.tests_executed,e.execution_cost.toFixed(0),pct(e.impact_recall),pct(e.critical_impact_recall),pct(e.impacted_node_coverage),pct(e.critical_mean_pod),pct(e.critical_regression_miss_rate)];
      vals.forEach(v=>{const td=document.createElement('td');td.textContent=v;tr.appendChild(td)}); body.appendChild(tr);
    }
  }

  function renderFault() {
    const box=el('cirFaultBox');
    if(!injectedFault){box.innerHTML='<strong>No injected fault.</strong><span class="cir-note">Choose “Inject diagnostic fault” to search the selected regression set for a covered failure mode with weak or zero detection probability.</span>';return}
    const sel=state.selections[strategySel.value], f=C.evaluateFault(scenario,sel,injectedFault);
    box.innerHTML=`<strong>${f.id}</strong><div>Node: <code>${f.node}</code> · mode: <code>${f.failure_mode}</code> · criticality: ${f.criticality}</div><div>Node covered by selected tests: <b>${f.covered}</b> · modeled POD: <b>${pct(f.pod)}</b></div><div class="cir-note">${f.covered && f.pod===0 ? 'This is the explicit Coverage ≠ Detection counterexample: the selected suite traverses the node but has no oracle for this injected failure mode.' : 'Coverage and detection remain separate evidence dimensions.'}</div>`;
  }

  function renderStatus() {
    el('cirStatus').innerHTML=`<strong>${state.mode==='oracle'?'Python parity fixture':'Interactive synthetic run'}</strong> · change <code>${state.change.id}</code> · truth ${reveal?'revealed after selection':'hidden from selectors'}<br><span class="cir-note">${state.note}</span>`;
  }
  function renderAll(){renderStatus();renderMetrics();renderGraph();renderTable();renderFault();}

  function injectDiagnosticFault(){
    const sel=state.selections[strategySel.value], faults=C.buildFaultCatalogue(scenario,true).map(f=>C.evaluateFault(scenario,sel,f));
    faults.sort((a,b)=>(Number(b.covered)-Number(a.covered)) || (a.pod-b.pod) || (b.criticality-a.criticality) || a.id.localeCompare(b.id));
    injectedFault=faults.find(f=>f.covered&&f.pod===0) || faults.find(f=>f.covered) || faults[0]; renderAll();
  }

  function runSynthetic(){reveal=false;injectedFault=null;state=makeSynthetic();renderAll()}
  function loadOracle(){reveal=false;injectedFault=null;state=makeOracle();renderAll()}

  function renderSweep() {
    const svg=el('cirSweep'); svg.innerHTML=''; const W=900,H=360,pad={l:55,r:20,t:20,b:45};
    const xs=[.4,.55,.7,.85,1], labels=['R2','R3','R4','R5'], series={}; labels.forEach(l=>series[l]=[]);
    const ch=scenario.changes[changeSel.value], baseSeed=Number(seed.value||11);
    for(const x of xs){const agg={};labels.forEach(l=>agg[l]=[]);for(let rep=0;rep<5;rep++){const g=C.observeGraph(scenario,x,Number(falseRate.value),baseSeed+rep*13),o=C.simulateChange(scenario,ch,baseSeed+200+rep*17),s=C.runStrategies(scenario,g,ch,Number(budget.value));for(const l of labels)agg[l].push(C.evaluateSelection(scenario,o,s[l]).critical_impact_recall)}for(const l of labels)series[l].push(agg[l].reduce((a,b)=>a+b,0)/agg[l].length)}
    const X=v=>pad.l+(v-.4)/.6*(W-pad.l-pad.r),Y=v=>H-pad.b-v*(H-pad.t-pad.b);
    svg.appendChild(svgEl('line',{x1:pad.l,y1:H-pad.b,x2:W-pad.r,y2:H-pad.b,class:'cir-axis'}));svg.appendChild(svgEl('line',{x1:pad.l,y1:pad.t,x2:pad.l,y2:H-pad.b,class:'cir-axis'}));
    for(let y=0;y<=1.001;y+=.25){const yy=Y(y),t=svgEl('text',{x:pad.l-10,y:yy+4,'text-anchor':'end',fill:'currentColor','font-size':'11'});t.textContent=pct(y);svg.appendChild(t)}
    xs.forEach(x=>{const t=svgEl('text',{x:X(x),y:H-15,'text-anchor':'middle',fill:'currentColor','font-size':'11'});t.textContent=x.toFixed(2);svg.appendChild(t)});
    const colors={R2:'#82aaff',R3:'#c792ea',R4:'#ffcb6b',R5:'#7bd88f'};
    labels.forEach((l,idx)=>{const pts=xs.map((x,i)=>[X(x),Y(series[l][i])]);const p=svgEl('path',{d:pts.map((p,i)=>`${i?'L':'M'}${p[0]},${p[1]}`).join(' '),class:'cir-line',stroke:colors[l]});svg.appendChild(p);pts.forEach(q=>svg.appendChild(svgEl('circle',{cx:q[0],cy:q[1],r:4,class:'cir-point',fill:colors[l],stroke:colors[l]})));const txt=svgEl('text',{x:W-70,y:30+idx*18,fill:colors[l],'font-size':'12'});txt.textContent=l;svg.appendChild(txt)});
    el('cirSweepNote').textContent='Mean critical-impact recall over 5 seeded browser worlds per completeness level. This diagnoses sensitivity to architecture knowledge; it is not a production performance estimate.';
  }

  el('cirRun').addEventListener('click',runSynthetic); el('cirOracle').addEventListener('click',loadOracle); el('cirReveal').addEventListener('click',()=>{reveal=!reveal;renderAll()}); el('cirInject').addEventListener('click',injectDiagnosticFault); el('cirSweepRun').addEventListener('click',renderSweep);
  strategySel.addEventListener('change',()=>{injectedFault=null;renderAll()}); [changeSel,completeness,falseRate,budget,seed].forEach(x=>x.addEventListener('change',()=>{if(state&&state.mode==='synthetic')runSynthetic()}));
  [completeness,falseRate,budget].forEach(x=>x.addEventListener('input',()=>{const out=el(`${x.id}Out`);if(out)out.textContent=x.value}));

  runSynthetic();
})();