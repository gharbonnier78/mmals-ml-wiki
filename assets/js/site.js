
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
})();
