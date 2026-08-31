(function(){
  const root=document.getElementById('repository-atlas');
  if(!root)return;

  const registryUrl=root.dataset.registry;
  const search=document.getElementById('repo-search');
  const category=document.getElementById('repo-category');
  const status=document.getElementById('repo-status');
  const reset=document.getElementById('repo-reset');
  const summary=document.getElementById('atlas-summary');
  const count=document.getElementById('atlas-count');

  const statusClass={
    supported:'implemented',
    mixed:'mechanistic',
    negative:'negative',
    hypothesis:'hypothesis',
    specification:'foundational',
    tool:'implemented',
    governance:'foundational',
    pedagogy:'mechanistic',
    legacy:'negative'
  };

  const categoryLabel={
    'mmals-core':'MMALS core',
    'mmals-evidence':'MMALS evidence',
    'mmals-geometry':'MMALS geometry & dynamics',
    'mmals-control':'MMALS control & specification',
    'testing-decision':'Testing & evidence-driven decisions',
    'adjacent-ml':'Adjacent ML / diagnostics',
    'systems-identity':'Systems & identity',
    'methods-governance':'Methods, governance & tooling',
    'pedagogy':'Pedagogy & publication',
    'legacy':'Legacy'
  };

  const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const safeUrl=value=>{
    try{
      const url=new URL(String(value),location.href);
      return ['https:','http:'].includes(url.protocol)?url.href:'#';
    }catch(_){return '#';}
  };

  function linkHtml(link){
    const url=safeUrl(link.url);
    const external=url.startsWith('http');
    return `<a class="atlas-link" href="${esc(url)}"${external?' target="_blank" rel="noopener noreferrer"':''}>${esc(link.label)}</a>`;
  }

  function card(repo){
    const outcome=repo.outcome||{};
    const cls=statusClass[outcome.status]||'foundational';
    const links=(repo.quick_links||[]).map(linkHtml).join('');
    const tags=(repo.tags||[]).slice(0,5).map(t=>`<span class="tag">${esc(t)}</span>`).join('');
    return `<article class="card atlas-card" id="${esc(repo.id)}" data-category="${esc(repo.category)}" data-status="${esc(outcome.status)}">
      <div class="meta-row">
        <span class="tag">${esc(categoryLabel[repo.category]||repo.category)}</span>
        <span class="status ${cls}">${esc(outcome.status)}</span>
        <span class="tag">${esc(outcome.evidence_class||'status')}</span>
      </div>
      <h3>${esc(repo.name)}</h3>
      <p class="atlas-role">${esc(repo.role)}</p>
      <p>${esc(repo.summary)}</p>
      <div class="atlas-outcome">
        <strong>Current outcome</strong>
        <p>${esc(outcome.statement)}</p>
        <a href="${esc(safeUrl(outcome.source_url))}" target="_blank" rel="noopener noreferrer">${esc(outcome.source_label||'Open outcome source')} →</a>
      </div>
      <div class="atlas-links">${links}</div>
      <div class="meta-row atlas-tags">${tags}</div>
      <div class="small">Repository: <code>gharbonnier78/${esc(repo.repository)}</code> · reviewed ${esc(repo.last_reviewed)}</div>
    </article>`;
  }

  function searchable(repo){
    return [
      repo.name,repo.repository,repo.category,repo.role,repo.summary,
      repo.outcome?.statement,...(repo.tags||[])
    ].join(' ').toLowerCase();
  }

  let registry=null;

  function render(){
    if(!registry)return;
    const q=(search?.value||'').trim().toLowerCase();
    const cat=category?.value||'';
    const st=status?.value||'';
    const rows=registry.repositories.filter(repo=>
      (!q||searchable(repo).includes(q)) &&
      (!cat||repo.category===cat) &&
      (!st||repo.outcome?.status===st)
    );
    root.innerHTML=rows.length?rows.map(card).join(''):`<div class="card"><h3>No matching repository</h3><p>Change or reset the filters.</p></div>`;
    if(summary)summary.textContent=`Showing ${rows.length} of ${registry.repositories.length} curated public repositories.`;
  }

  fetch(registryUrl)
    .then(r=>{if(!r.ok)throw new Error(`registry ${r.status}`);return r.json();})
    .then(data=>{
      registry=data;
      const categories=[...new Set(data.repositories.map(r=>r.category))].sort((a,b)=>(categoryLabel[a]||a).localeCompare(categoryLabel[b]||b));
      categories.forEach(key=>{
        const option=document.createElement('option');
        option.value=key;
        option.textContent=categoryLabel[key]||key;
        category.appendChild(option);
      });

      const preferred=['supported','mixed','negative','hypothesis','specification','tool','governance','pedagogy','legacy'];
      const statuses=[...new Set(data.repositories.map(r=>r.outcome?.status).filter(Boolean))].sort((a,b)=>preferred.indexOf(a)-preferred.indexOf(b));
      statuses.forEach(key=>{
        const option=document.createElement('option');
        option.value=key;
        option.textContent=key;
        status.appendChild(option);
      });

      if(count)count.textContent=`${data.repositories.length} curated repositories`;
      render();
    })
    .catch(err=>{
      console.error('Repository atlas unavailable:',err);
      root.innerHTML='<div class="card"><h3>Repository atlas unavailable</h3><p>The structured registry could not be loaded. Use the GitHub source registry or try again after refreshing.</p></div>';
      if(summary)summary.textContent='Registry unavailable.';
      if(count)count.textContent='registry unavailable';
    });

  [search,category,status].forEach(el=>el?.addEventListener(el===search?'input':'change',render));
  reset?.addEventListener('click',()=>{
    if(search)search.value='';
    if(category)category.value='';
    if(status)status.value='';
    render();
  });
})();