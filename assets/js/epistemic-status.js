(function(){
  const statusScript=document.currentScript;
  if(!statusScript)return;

  const siteRoot=new URL('../../',statusScript.src);
  const statusUrl=new URL('data/epistemic-statuses.json',siteRoot);
  const auditUrl=new URL('data/concept-audit.json',siteRoot);

  function relativePagePath(){
    let path=decodeURIComponent(location.pathname);
    const rootPath=decodeURIComponent(siteRoot.pathname);
    if(path.startsWith(rootPath))path=path.slice(rootPath.length);
    path=path.replace(/^\/+/, '');
    if(!path || path.endsWith('/'))path+=path?'index.html':'index.html';
    return path;
  }

  function makeBadge(key,definition){
    const badge=document.createElement('span');
    badge.className=`status ${definition.css_class||'foundational'}`;
    badge.dataset.epistemicBadge=key;
    badge.textContent=definition.label||key;
    badge.title=definition.description||'';
    return badge;
  }

  function renderCanonicalStatus(key,definition){
    if(!key||!definition||document.querySelector('[data-epistemic-badge]'))return;
    const hero=document.querySelector('.page-hero');
    if(!hero)return;
    let meta=hero.querySelector('.meta-row');
    if(!meta){
      meta=document.createElement('div');
      meta.className='meta-row';
      hero.appendChild(meta);
    }
    meta.prepend(makeBadge(key,definition));

    const note=document.createElement('p');
    note.className='small';
    note.dataset.epistemicNote='true';
    const strong=document.createElement('strong');
    strong.textContent='Epistemic status. ';
    note.appendChild(strong);
    note.appendChild(document.createTextNode(definition.description||''));
    note.appendChild(document.createTextNode(' This axis is separate from draft/review/release maturity.'));
    meta.insertAdjacentElement('afterend',note);
  }

  function renderExplicitMarkers(registry){
    document.querySelectorAll('[data-epistemic-status]').forEach(root=>{
      if(root.querySelector('[data-epistemic-badge]'))return;
      const key=root.dataset.epistemicStatus;
      const definition=registry.statuses?.[key];
      if(!definition){
        console.warn(`Diderot unknown epistemic status marker: ${key}`);
        return;
      }
      root.prepend(makeBadge(key,definition));
    });
  }

  async function resolveConceptStatus(registry,path){
    const match=path.match(/^concepts\/([^/]+)\/index\.html$/);
    if(!match)return null;
    const conceptId=match[1];
    const response=await fetch(auditUrl);
    if(!response.ok)throw new Error(`concept audit ${response.status}`);
    const audit=await response.json();
    const item=audit.concepts?.[conceptId];
    if(!item)return null;
    const key=registry.concept_overrides?.[conceptId]||registry.group_defaults?.[item.group];
    if(key==='qualified-research-evidence'&&!(Array.isArray(item.qualified_evidence_refs)&&item.qualified_evidence_refs.length)){
      console.error(`Diderot refused to render qualified research evidence for ${conceptId}: qualified_evidence_refs missing`);
      return {
        key:'contract-error',
        definition:{label:'epistemic status error',css_class:'negative',description:'Qualified research evidence was requested without a qualifying ingestion reference. The page must not present that status.'}
      };
    }
    return key?{key,definition:registry.statuses?.[key]}:null;
  }

  fetch(statusUrl).then(response=>{
    if(!response.ok)throw new Error(`epistemic status registry ${response.status}`);
    return response.json();
  }).then(async registry=>{
    const path=relativePagePath();
    let resolved=await resolveConceptStatus(registry,path);
    if(!resolved){
      const key=registry.surfaces?.[path];
      if(key)resolved={key,definition:registry.statuses?.[key]};
    }
    if(resolved?.definition)renderCanonicalStatus(resolved.key,resolved.definition);
    renderExplicitMarkers(registry);
  }).catch(err=>console.warn('Diderot epistemic status unavailable:',err));
})();
