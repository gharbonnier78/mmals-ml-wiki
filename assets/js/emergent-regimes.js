(function(){
  'use strict';

  const $=id=>document.getElementById(id);
  const controls={
    features:$('features'),regimes:$('regimes'),signal:$('signal'),noise:$('noise'),
    nuisance:$('nuisance'),scale:$('scale'),standardize:$('standardize'),colourMode:$('colourMode')
  };
  const outputs={features:$('featuresO'),regimes:$('regimesO'),signal:$('signalO'),noise:$('noiseO'),nuisance:$('nuisanceO'),scale:$('scaleO')};
  let seed=42,pairIndex=0,last=null;
  const palette=['#82c95d','#53b9ac','#d2aa54','#6fa8dc','#d86a6a','#ba89d8','#eea843','#80d5b5'];

  function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
  function normal(rng){let u=0,v=0;while(!u)u=rng();while(!v)v=rng();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v)}
  function clamp(v,a,b){return Math.max(a,Math.min(b,v))}
  function mean(a){return a.reduce((s,x)=>s+x,0)/a.length}
  function sd(a){const m=mean(a);return Math.sqrt(a.reduce((s,x)=>s+(x-m)*(x-m),0)/Math.max(1,a.length-1))}
  function dot(a,b){let s=0;for(let i=0;i<a.length;i++)s+=a[i]*b[i];return s}

  function params(){return{
    p:+controls.features.value,k:+controls.regimes.value,signal:+controls.signal.value,
    noise:+controls.noise.value,nuisance:+controls.nuisance.value,scale:+controls.scale.value,
    standardize:controls.standardize.checked,n:320
  }}

  function generate(cfg,runSeed){
    const rng=mulberry32(runSeed),a=[],b=[],c=[],scales=[];
    for(let j=0;j<cfg.p;j++){
      a.push(normal(rng));b.push(normal(rng));c.push(normal(rng));
      scales.push(Math.exp(cfg.scale*(2*rng()-1)));
    }
    const X=[],labels=[];
    for(let i=0;i<cfg.n;i++){
      const label=Math.floor(rng()*cfg.k),angle=2*Math.PI*label/cfg.k;
      const cx=Math.cos(angle)+0.18*normal(rng),cy=Math.sin(angle)+0.18*normal(rng);
      const nuisanceScore=normal(rng),row=[];
      for(let j=0;j<cfg.p;j++){
        const regime=0.34*cfg.signal*(cx*a[j]+cy*b[j]);
        const value=(regime+0.32*cfg.nuisance*nuisanceScore*c[j]+cfg.noise*normal(rng))*scales[j];
        row.push(value);
      }
      X.push(row);labels.push(label);
    }
    return{X,labels};
  }

  function preprocess(X,standardize){
    const n=X.length,p=X[0].length,mu=Array(p).fill(0),sigma=Array(p).fill(1);
    for(const row of X)for(let j=0;j<p;j++)mu[j]+=row[j]/n;
    if(standardize){
      for(const row of X)for(let j=0;j<p;j++)sigma[j]+=(row[j]-mu[j])**2/n;
      for(let j=0;j<p;j++)sigma[j]=Math.sqrt(Math.max(1e-9,sigma[j]-1));
    }
    return X.map(row=>row.map((v,j)=>(v-mu[j])/sigma[j]));
  }

  function covariance(X){
    const n=X.length,p=X[0].length,C=Array.from({length:p},()=>Array(p).fill(0));
    for(let i=0;i<n;i++)for(let j=0;j<p;j++)for(let k=0;k<=j;k++)C[j][k]+=X[i][j]*X[i][k]/Math.max(1,n-1);
    for(let j=0;j<p;j++)for(let k=0;k<j;k++)C[k][j]=C[j][k];
    return C;
  }

  function matVec(C,v){return C.map(row=>dot(row,v))}
  function eigenvector(C,previous=[],phase=0){
    const p=C.length;let v=Array.from({length:p},(_,i)=>Math.sin((i+1)*(1.37+phase))+.2*Math.cos((i+1)*.73));
    for(let it=0;it<64;it++){
      let y=matVec(C,v);
      for(const q of previous){const projection=dot(y,q);y=y.map((x,i)=>x-projection*q[i])}
      const norm=Math.sqrt(dot(y,y))||1;v=y.map(x=>x/norm);
    }
    const Cv=matVec(C,v);return{v,lambda:Math.max(0,dot(v,Cv))};
  }

  function pca(X){
    const C=covariance(X),e1=eigenvector(C,[],0),e2=eigenvector(C,[e1.v],1);
    const scores=X.map(row=>[dot(row,e1.v),dot(row,e2.v)]),total=C.reduce((s,row,i)=>s+row[i],0);
    return{scores,lambdas:[e1.lambda,e2.lambda],total};
  }

  function kmeans(points,k){
    const centers=[];
    centers.push(points[0].slice());
    while(centers.length<k){
      let best=points[0],bestD=-1;
      for(const p of points){const d=Math.min(...centers.map(c=>(p[0]-c[0])**2+(p[1]-c[1])**2));if(d>bestD){bestD=d;best=p}}
      centers.push(best.slice());
    }
    let assign=Array(points.length).fill(0);
    for(let it=0;it<30;it++){
      const next=points.map(p=>{let bi=0,bd=Infinity;centers.forEach((c,i)=>{const d=(p[0]-c[0])**2+(p[1]-c[1])**2;if(d<bd){bd=d;bi=i}});return bi});
      if(next.every((x,i)=>x===assign[i])&&it>0)break;assign=next;
      for(let c=0;c<k;c++){const group=points.filter((_,i)=>assign[i]===c);if(group.length)centers[c]=[mean(group.map(x=>x[0])),mean(group.map(x=>x[1]))]}
    }
    return assign;
  }

  function choose2(n){return n*(n-1)/2}
  function adjustedRand(a,b){
    const n=a.length,ca=new Map(),cb=new Map(),joint=new Map();
    for(let i=0;i<n;i++){
      ca.set(a[i],(ca.get(a[i])||0)+1);cb.set(b[i],(cb.get(b[i])||0)+1);
      const key=a[i]+'|'+b[i];joint.set(key,(joint.get(key)||0)+1);
    }
    const sumJoint=[...joint.values()].reduce((s,x)=>s+choose2(x),0),sumA=[...ca.values()].reduce((s,x)=>s+choose2(x),0),sumB=[...cb.values()].reduce((s,x)=>s+choose2(x),0);
    const expected=sumA*sumB/choose2(n),max=.5*(sumA+sumB);return(max-expected)===0?0:(sumJoint-expected)/(max-expected);
  }

  function regimeSignal(points,labels,k){
    const overall=[mean(points.map(p=>p[0])),mean(points.map(p=>p[1]))];let between=0,total=0;
    for(const p of points)total+=(p[0]-overall[0])**2+(p[1]-overall[1])**2;
    for(let c=0;c<k;c++){const g=points.filter((_,i)=>labels[i]===c);if(!g.length)continue;const m=[mean(g.map(p=>p[0])),mean(g.map(p=>p[1]))];between+=g.length*((m[0]-overall[0])**2+(m[1]-overall[1])**2)}
    return total?between/total:0;
  }

  function extent(points,axis){const vals=points.map(p=>p[axis]),lo=Math.min(...vals),hi=Math.max(...vals),pad=(hi-lo||1)*.09;return[lo-pad,hi+pad]}
  function drawScatter(canvas,points,colours,xLabel,yLabel){
    const ctx=canvas.getContext('2d'),W=canvas.width,H=canvas.height,m={l:54,r:22,t:24,b:46},ex=extent(points,0),ey=extent(points,1);
    ctx.clearRect(0,0,W,H);ctx.fillStyle='#0c120e';ctx.fillRect(0,0,W,H);
    ctx.strokeStyle='#27362d';ctx.lineWidth=1;ctx.fillStyle='#819287';ctx.font='12px system-ui';
    for(let i=0;i<=4;i++){const x=m.l+i*(W-m.l-m.r)/4,y=m.t+i*(H-m.t-m.b)/4;ctx.beginPath();ctx.moveTo(x,m.t);ctx.lineTo(x,H-m.b);ctx.stroke();ctx.beginPath();ctx.moveTo(m.l,y);ctx.lineTo(W-m.r,y);ctx.stroke()}
    points.forEach((p,i)=>{const x=m.l+(p[0]-ex[0])/(ex[1]-ex[0])*(W-m.l-m.r),y=H-m.b-(p[1]-ey[0])/(ey[1]-ey[0])*(H-m.t-m.b);ctx.beginPath();ctx.arc(x,y,3.25,0,Math.PI*2);ctx.fillStyle=colours[i];ctx.globalAlpha=.78;ctx.fill()});ctx.globalAlpha=1;
    ctx.fillStyle='#9aab9e';ctx.textAlign='center';ctx.fillText(xLabel,m.l+(W-m.l-m.r)/2,H-12);ctx.save();ctx.translate(16,m.t+(H-m.t-m.b)/2);ctx.rotate(-Math.PI/2);ctx.fillText(yLabel,0,0);ctx.restore();ctx.textAlign='left';
  }

  function drawVariance(canvas,lambdas,total){
    const ctx=canvas.getContext('2d'),W=canvas.width,H=canvas.height,parts=[lambdas[0]/total,lambdas[1]/total,Math.max(0,1-(lambdas[0]+lambdas[1])/total)],labels=['PC1','PC2','Residual dimensions'],cols=['#82c95d','#53b9ac','#27362d'];
    ctx.clearRect(0,0,W,H);ctx.fillStyle='#0c120e';ctx.fillRect(0,0,W,H);const left=150,right=40,barW=W-left-right;
    parts.forEach((v,i)=>{const y=34+i*62;ctx.fillStyle='#18221c';ctx.fillRect(left,y,barW,28);ctx.fillStyle=cols[i];ctx.fillRect(left,y,barW*v,28);ctx.fillStyle='#d9e7d8';ctx.font='14px system-ui';ctx.fillText(labels[i],28,y+20);ctx.fillStyle='#9aab9e';ctx.fillText((100*v).toFixed(1)+'%',left+barW+8,y+20)});
  }

  function coloursFor(mode,labels,clusters){
    if(mode==='hidden')return labels.map(()=>'#9aab9e');const src=mode==='kmeans'?clusters:labels;return src.map(x=>palette[x%palette.length]);
  }

  function compute(runSeed){
    const cfg=params(),data=generate(cfg,runSeed),X=preprocess(data.X,cfg.standardize),projection=pca(X);
    const pairA=(pairIndex*2)%cfg.p,pairB=(pairA+1)%cfg.p,local=X.map(row=>[row[pairA],row[pairB]]),clusters=kmeans(projection.scores,cfg.k);
    return{cfg,data,X,projection,local,clusters,pairA,pairB,localSignal:regimeSignal(local,data.labels,cfg.k),globalSignal:regimeSignal(projection.scores,data.labels,cfg.k),ari:adjustedRand(data.labels,clusters)};
  }

  function diagnosis(result){
    const gain=result.globalSignal-result.localSignal,vr=(result.projection.lambdas[0]+result.projection.lambdas[1])/result.projection.total;
    if(result.globalSignal<.18)return '<strong>Regime signal is fragile.</strong> The first two PCs do not preserve much of the generating structure. Try reducing nuisance variance—or treat the absence as a legitimate negative result.';
    if(gain>.28&&result.ari>.55)return '<strong>Emergence is visible.</strong> Weak local views become a coherent global geometry, and K-means substantially agrees with the hidden regimes. Now change the seed and attack that conclusion.';
    if(vr>.55&&result.ari<.25)return '<strong>High variance, weak clustering.</strong> PCA preserves a lot of variation, but not the regime structure. Variance explained is not decision relevance.';
    return '<strong>Ambiguous evidence.</strong> The collective view improves on the local pair, but the partition remains uncertain. Inspect stability before naming a system regime.';
  }

  function render(){
    Object.entries(outputs).forEach(([k,o])=>o.textContent=(k==='features'||k==='regimes')?controls[k].value:(+controls[k].value).toFixed(2));
    last=compute(seed);const mode=controls.colourMode.value,colours=coloursFor(mode,last.data.labels,last.clusters);
    drawScatter($('localCanvas'),last.local,colours,'feature '+(last.pairA+1),'feature '+(last.pairB+1));
    drawScatter($('pcaCanvas'),last.projection.scores,colours,'principal component 1','principal component 2');
    drawVariance($('varianceCanvas'),last.projection.lambdas,last.projection.total);
    $('pairTitle').textContent='Feature '+(last.pairA+1)+' × feature '+(last.pairB+1);
    $('localSep').textContent=last.localSignal.toFixed(3);$('globalSep').textContent=last.globalSignal.toFixed(3);
    $('variance').textContent=(100*(last.projection.lambdas[0]+last.projection.lambdas[1])/last.projection.total).toFixed(1)+'%';
    $('ari').textContent=last.ari.toFixed(3);$('diagnosis').innerHTML=diagnosis(last);$('stressResult').textContent='Not run for this configuration.';
  }

  function stress(){
    const button=$('stressTest');button.disabled=true;button.textContent='Running…';
    setTimeout(()=>{
      const signals=[],agreements=[];for(let i=0;i<8;i++){const r=compute(seed+7919*(i+1));signals.push(r.globalSignal);agreements.push(r.ari)}
      const sm=mean(signals),ss=sd(signals),am=mean(agreements),as=sd(agreements);
      const verdict=(sm<.18||am<.15)?' · stable negative result: regimes are not recovered':(ss>.12||as>.18?' · fragile across seeds':' · stable positive pattern in this toy');
      $('stressResult').innerHTML='<strong>PCA regime signal:</strong> '+sm.toFixed(3)+' ± '+ss.toFixed(3)+' &nbsp; <strong>ARI:</strong> '+am.toFixed(3)+' ± '+as.toFixed(3)+verdict;
      button.disabled=false;button.textContent='Stress-test 8 seeds';
    },20);
  }

  Object.values(controls).forEach(el=>el.addEventListener('input',render));
  $('newSeed').addEventListener('click',()=>{seed=(seed+104729)%1000003;render()});
  $('nextPair').addEventListener('click',()=>{pairIndex++;render()});
  $('stressTest').addEventListener('click',stress);
  render();
})();
