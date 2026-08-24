
(function(){
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
})();
