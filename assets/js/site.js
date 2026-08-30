
(function(){
  const siteScript=document.currentScript;

  // Render display-math blocks from their canonical TeX source.
  // The repository stores formulas as plain TeX inside `.formula` elements so the
  // source stays readable and diffable. MathJax is loaded only on pages that
  // actually contain formulas; if the CDN is unavailable, the original TeX is restored.
  const formulaNodes=[...document.querySelectorAll('.formula')].filter(el=>el.textContent.trim());
  if(formulaNodes.length){
    const renderWithMathJax=()=>{
      if(!window.MathJax?.typesetPromise)return;
      window.MathJax.typesetPromise(formulaNodes).then(()=>{
        formulaNodes.forEach(el=>{
          el.classList.remove('math-pending');
          el.classList.add('math-rendered');
          el.dataset.mathRendered='true';
        });
      }).catch(err=>{
        console.warn('Diderot formula rendering failed:',err);
        formulaNodes.forEach(el=>{
          const tex=el.dataset.tex||el.textContent;
          el.textContent=tex;
          el.classList.remove('math-pending');
          el.classList.add('math-fallback');
        });
      });
    };

    formulaNodes.forEach(el=>{
      const tex=el.textContent.trim();
      el.dataset.tex=tex;
      el.textContent=`\\[${tex}\\]`;
      el.classList.add('math-pending');
    });

    if(window.MathJax?.typesetPromise){
      renderWithMathJax();
    }else{
      window.MathJax={
        tex:{
          inlineMath:[['\\(','\\)']],
          displayMath:[['\\[','\\]']],
          processEscapes:true
        },
        options:{
          skipHtmlTags:['script','noscript','style','textarea','pre','code']
        },
        startup:{typeset:false}
      };
      const mathScript=document.createElement('script');
      mathScript.src='https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js';
      mathScript.async=true;
      mathScript.dataset.diderotMath='mathjax-3.2.2';
      mathScript.addEventListener('load',renderWithMathJax,{once:true});
      mathScript.addEventListener('error',()=>{
        console.warn('Diderot MathJax dependency unavailable; showing TeX fallback.');
        formulaNodes.forEach(el=>{
          el.textContent=el.dataset.tex||el.textContent;
          el.classList.remove('math-pending');
          el.classList.add('math-fallback');
        });
      },{once:true});
      document.head.appendChild(mathScript);
    }
  }

  document.querySelectorAll('[data-reading-levels]').forEach(root=>{
    const buttons=[...root.querySelectorAll('.level-btn')];
    const panels=[...root.parentElement.querySelectorAll('.level-panel')];
    function activate(level){
      buttons.forEach(b=>b.classList.toggle('active',b.dataset.level===level));
      panels.forEach(p=>p.classList.toggle('active',p.dataset.level===level));
      localStorage.setItem('diderot-reading-level',level);
    }
    buttons.forEach(b=>b.addEventListener('click',()=>activate(b.dataset.level)));
    activate(localStorage.getItem('diderot-reading-level')||'discover');
  });
  document.querySelectorAll('[data-copy]').forEach(btn=>btn.addEventListener('click',async()=>{
    const el=document.querySelector(btn.dataset.copy); if(!el)return;
    try{await navigator.clipboard.writeText(el.value||el.textContent);btn.textContent='Copied';setTimeout(()=>btn.textContent='Copy',1200)}catch(e){el.select?.();document.execCommand('copy')}
  }));
  document.querySelectorAll('[data-current-year]').forEach(el=>el.textContent=new Date().getFullYear());

  // Living chronicle extension after release v0.2.2.
  // The static release history remains frozen; this hypothesis-formation event is
  // inserted before the chronicle page initializes its filters, so it behaves as
  // a normal filterable timeline card without rewriting historical entries.
  const timeline=document.querySelector('.timeline');
  if(timeline && !timeline.querySelector('[data-event-id="2026-08-24-minimal-dynamic-inference"]')){
    const article=document.createElement('article');
    article.className='timeline-event';
    article.dataset.eventId='2026-08-24-minimal-dynamic-inference';
    article.dataset.branch='core-trunk';
    article.dataset.type='transition';
    article.dataset.public='yes';
    article.innerHTML=`<div class="timeline-date">24 August 2026</div><div class="timeline-dot"></div><div class="timeline-card"><div class="meta-row"><span class="tag">transition</span><span class="tag">MMALS core trunk</span><span class="tag">public artifact</span></div><h3>Minimal sufficient dynamic inference becomes an explicit MMALS research direction</h3><p>A cross-disciplinary synthesis proposes that MMALS should prefer reuse, then adaptation, then fork, and nominate a candidate new regime only when existing hosts are no longer dynamically compatible with the evidence.</p><div class="event-outcome"><strong>Research consequence</strong><p>The idea is recorded as a falsifiable program extension—not validated evidence—with non-regression competence contracts, complexity-on-evidence, dynamic compatibility, local domains of validity, and tests against simpler continual-learning and mixture-of-experts baselines.</p></div><div class="small">Provenance: public MMALS program note and chronicle entry, 24 August 2026 · <a href="../../pathways/dynamic-systems-for-mmals/index.html">guided Diderot pathway</a></div></div>`;
    timeline.appendChild(article);
    const throughTag=[...document.querySelectorAll('.page-hero .meta-row .tag')].find(el=>el.textContent.includes('curated through'));
    if(throughTag) throughTag.textContent='curated through 24 August 2026';
  }

  // Step 2 — source + epistemic audit overlay.
  // One central registry keeps status and references consistent across all concept pages.
  // It is an audit layer, not a claim-validation mechanism.
  const conceptMatch=location.pathname.match(/\/concepts\/([^/]+)\/(?:index\.html)?$/);
  if(siteScript && conceptMatch){
    const conceptId=conceptMatch[1];
    const auditUrl=new URL('../../data/concept-audit.json',siteScript.src);
    fetch(auditUrl).then(r=>{if(!r.ok)throw new Error(`audit ${r.status}`);return r.json()}).then(audit=>{
      const item=audit.concepts?.[conceptId];
      const group=item && audit.groups?.[item.group];
      if(!item||!group||document.querySelector('[data-concept-audit]'))return;
      const root=document.querySelector('main .container.narrow')||document.querySelector('main .container');
      if(!root)return;
      const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
      const refs=(item.sources||[]).map(key=>audit.sources?.[key]).filter(Boolean);
      const refHtml=refs.length?refs.map(s=>`<a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer"><strong>${esc(s.authors)} (${esc(s.year)})</strong><span class="small"> — ${esc(s.title)} · ${esc(s.type)}</span></a>`).join(''):'<p class="small">No reference registered yet — reviewer action required.</p>';
      const focus=item.review_focus?`<div class="event-outcome"><strong>Reviewer focus</strong><p>${esc(item.review_focus)}</p></div>`:'';
      const rule=item.rule?`<div class="highlight">${esc(item.rule)}</div>`:'';
      const statusClass=(item.group==='mmals-hypothesis'||item.group==='world-model')?'hypothesis':'foundational';
      const section=document.createElement('section');
      section.className='prose';
      section.dataset.conceptAudit='true';
      section.innerHTML=`<h2>Source & epistemic audit</h2><div class="meta-row"><span class="status ${statusClass}">${esc(group.label)}</span><span class="tag">audit ${esc(audit.audit_date)}</span><span class="tag">${esc(group.graph_edge_review)}</span></div><p><strong>Epistemic status.</strong> ${esc(group.epistemic_status)}</p><p><strong>Definition fidelity.</strong> ${esc(group.definition_fidelity)}</p><p><strong>MMALS evidence status.</strong> ${esc(group.mmals_evidence_status)}</p><p><strong>Toy status.</strong> ${esc(group.toy_status)}</p>${rule}${focus}<h3>Reference anchors</h3><div class="relation-list">${refHtml}</div><p class="small">This panel is generated from <code>data/concept-audit.json</code>. A reference anchor supports terminology or framing; it does not by itself validate the MMALS transfer, analogy or hypothesis.</p>`;
      root.appendChild(section);
    }).catch(err=>console.warn('Diderot concept audit unavailable:',err));
  }
})();
