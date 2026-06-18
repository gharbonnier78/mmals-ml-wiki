
(async function(){
const root=document.getElementById('graphApp'); if(!root)return;
const base='../';
const [concepts,relations]=await Promise.all([fetch(base+'data/concepts.json').then(r=>r.json()),fetch(base+'data/relations.json').then(r=>r.json())]);
const svg=document.getElementById('conceptGraph'); const ns='http://www.w3.org/2000/svg';
const cats=['all','architecture','routing','memory','geometry','evaluation','control','ecology','semantics','continual-learning'];
const colors={architecture:'#82c95d',routing:'#53b9ac',memory:'#d2aa54',geometry:'#6fa8dc',evaluation:'#c08ade',control:'#eea843',ecology:'#9fcf65',semantics:'#b6c3b8','continual-learning':'#d86a6a'};
let active='all';
const toolbar=document.querySelector('.graph-toolbar'); cats.forEach((cat,i)=>{const b=document.createElement('button');b.textContent=cat.replace('-',' ');b.className=i===0?'active':'';b.onclick=()=>{active=cat;[...toolbar.children].forEach(x=>x.classList.remove('active'));b.classList.add('active');draw()};toolbar.appendChild(b)});
const W=1000,H=560,cx=W/2,cy=H/2;
const categoryById={mmals:'architecture','biological-mapping':'semantics',host:'architecture','fungal-medium':'architecture',mycorrhiza:'ecology','inferred-context':'routing',route:'routing','functional-route':'memory','functional-memory':'memory','reconstructive-synthetic-memory':'memory','host-specialization':'ecology','probability-simplex':'geometry',torus:'geometry','stability-plasticity':'continual-learning',cal:'evaluation',tput:'control'};
const ring=concepts.filter(c=>c.id!=='mmals');
const pos={mmals:{x:cx,y:cy}};ring.forEach((c,i)=>{const a=-Math.PI/2+i*2*Math.PI/ring.length;const rr=i%2?225:180;pos[c.id]={x:cx+Math.cos(a)*rr,y:cy+Math.sin(a)*rr}});
function el(name,attrs={}){const n=document.createElementNS(ns,name);Object.entries(attrs).forEach(([k,v])=>n.setAttribute(k,v));return n}
function draw(){svg.innerHTML='';svg.setAttribute('viewBox',`0 0 ${W} ${H}`);
 const visible=new Set(concepts.filter(c=>active==='all'||categoryById[c.id]===active||c.id==='mmals').map(c=>c.id));
 relations.filter(r=>visible.has(r.source)&&visible.has(r.target)).forEach(r=>{const p=pos[r.source],q=pos[r.target];const line=el('line',{x1:p.x,y1:p.y,x2:q.x,y2:q.y,stroke:'#33433a','stroke-width':'1.4',opacity:'.8'});svg.appendChild(line)});
 concepts.filter(c=>visible.has(c.id)).forEach(c=>{const p=pos[c.id],cat=categoryById[c.id];const g=el('g',{tabindex:'0',role:'link','aria-label':c.title,style:'cursor:pointer'});const rad=c.id==='mmals'?48:32;g.appendChild(el('circle',{cx:p.x,cy:p.y,r:rad,fill:colors[cat]||'#82c95d',opacity:c.id==='mmals'?'.95':'.82',stroke:'#eff5ed','stroke-width':c.id==='mmals'?'2':'1'}));const t=el('text',{x:p.x,y:p.y+4,'text-anchor':'middle',fill:'#071008','font-family':'system-ui','font-size':c.id==='mmals'?'15':'11','font-weight':'700'});const words=c.title.split(' ');if(words.length>2){const a=el('tspan',{x:p.x,dy:'-4'});a.textContent=words.slice(0,2).join(' ');const b=el('tspan',{x:p.x,dy:'14'});b.textContent=words.slice(2).join(' ');t.append(a,b)}else t.textContent=c.title;g.appendChild(t);g.onclick=()=>location.href=`../concepts/${c.id}/index.html`;g.onkeydown=e=>{if(e.key==='Enter')g.onclick()};svg.appendChild(g)});
}
draw();
})();
