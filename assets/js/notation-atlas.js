(async function(){
  const atlas=document.getElementById('notationApp');
  const poster=document.getElementById('posterGrid');
  if(!atlas && !poster) return;

  const response=await fetch('registry.json');
  if(!response.ok) throw new Error(`Notation registry unavailable: ${response.status}`);
  const data=await response.json();
  const entries=data.entries||[];
  const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const join=(xs,sep=', ')=>Array.isArray(xs)?xs.join(sep):'';

  if(atlas){
    const q=document.getElementById('notationSearch');
    const category=document.getElementById('notationCategory');
    const domain=document.getElementById('notationDomain');
    const count=document.getElementById('notationCount');
    const grid=document.getElementById('notationGrid');

    [...new Set(entries.map(e=>e.category).filter(Boolean))].sort().forEach(v=>category.add(new Option(v,v)));
    [...new Set(entries.flatMap(e=>e.domains||[]))].sort().forEach(v=>domain.add(new Option(v,v)));

    function haystack(e){return [e.display,e.latex,e.concept,e.category,e.formal,e.plain_language,e.why_here,e.spoken?.fr_literal,e.spoken?.fr_natural,...(e.aliases||[]),...(e.connections||[]),...(e.domains||[])].join(' ').toLowerCase()}
    function card(e){
      const encounter=(e.encounters||[]).slice(-1)[0];
      const src=(e.authority?.mathematical_sources||[])[0];
      return `<article class="notation-card" data-id="${esc(e.id)}">
        <div class="glyph">${esc(e.display)}</div>
        <div><strong>${esc(e.concept)}</strong> <span class="chip">${esc(e.category)}</span></div>
        <div class="spoken">« ${esc(e.spoken?.fr_literal)} »</div>
        <div class="literal">${esc(e.spoken?.fr_natural)}</div>
        <p>${esc(e.plain_language)}</p>
        <div class="chips">${(e.domains||[]).map(d=>`<span class="chip">${esc(d)}</span>`).join('')}</div>
        <details><summary>Déplier la fiche</summary>
          <dl>
            <dt>LaTeX</dt><dd><code>${esc(e.latex)}</code></dd>
            <dt>Formel</dt><dd>${esc(e.formal)}</dd>
            <dt>Pourquoi ici ?</dt><dd>${esc(e.why_here)}</dd>
            <dt>Exemple</dt><dd><code>${esc(e.example?.statement)}</code><br>${esc(e.example?.explanation)}</dd>
            <dt>Prérequis</dt><dd>${esc(join(e.prerequisites))}</dd>
            <dt>Connexions</dt><dd>${esc(join(e.connections))}</dd>
            <dt>Maturité</dt><dd>${esc(e.maturity)} · ${esc(e.status)}</dd>
            <dt>Rencontré</dt><dd>${esc(encounter?.context)}<br><span class="literal">${esc(encounter?.contribution)}</span></dd>
          </dl>
          ${e.misconception?`<div class="notation-alert"><strong>Piège :</strong> ${esc(e.misconception.wrong)}<br><strong>Correction :</strong> ${esc(e.misconception.correction)}</div>`:''}
          <p class="notation-source"><strong>Autorité enregistrée :</strong> ${esc(src?.reference||'à compléter')} · ${esc(src?.status||'')}</p>
        </details>
      </article>`;
    }
    function render(){
      const query=q.value.trim().toLowerCase();
      const c=category.value,d=domain.value;
      const filtered=entries.filter(e=>(!query||haystack(e).includes(query))&&(!c||e.category===c)&&(!d||(e.domains||[]).includes(d)));
      count.textContent=`${filtered.length} notation${filtered.length>1?'s':''} affichée${filtered.length>1?'s':''} sur ${entries.length}.`;
      grid.innerHTML=filtered.map(card).join('')||'<p>Aucune notation ne correspond aux filtres.</p>';
    }
    [q,category,domain].forEach(el=>el.addEventListener(el===q?'input':'change',render));
    document.getElementById('notationUpdated').textContent=data.updated||'';
    render();
  }

  if(poster){
    const compact=e=>`<article class="poster-card">
      <div class="poster-glyph">${esc(e.display)}</div>
      <div class="poster-name">${esc(e.concept)}</div>
      <div class="poster-read">Se lit : « ${esc(e.spoken?.fr_literal)} »</div>
      <div class="poster-meaning">${esc(e.plain_language)}</div>
      <div class="poster-domains">Domaines : ${esc(join((e.domains||[]).slice(0,4),' · '))}</div>
    </article>`;
    poster.innerHTML=entries.map(compact).join('');
    const pc=document.getElementById('posterCount'); if(pc) pc.textContent=`${entries.length} entrées`;
    const pu=document.getElementById('posterUpdated'); if(pu) pu.textContent=data.updated||'';
  }
})();
