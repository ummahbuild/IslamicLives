import {populationLabel,regionalYear,markersFor,playbackDelay,cumulativeAtlasContext} from './atlas-model.mjs';
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function mountAtlas(main,chapter='tradition'){
 const abort=new AbortController();let disposed=false,globe=null,timer=null,index=0,data=null,speed=1;
 main.innerHTML=`<div class="atlas"><div class="atlas-heading"><div><p class="eyebrow">An atlas of faith · Adam to 2026</p><h1>How Islam <em>spread.</em></h1></div><p>Follow communities across centuries and continents.<br>A world of connections, one chapter at a time.</p></div><div id="atlas-content"><p role="status" class="loading">Preparing the atlas…</p></div></div>`;
 const sourceLink=id=>{const s=data.sources[id];return `<a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.title)} ↗</a>`};
 function pause(){clearInterval(timer);timer=null;const button=main.querySelector('#atlas-play');if(button){button.textContent='▶ Play history';button.setAttribute('aria-pressed','false')}}
 function showMarker(marker){
  const target=main.querySelector('#place-detail');target.hidden=false;
  target.innerHTML=`<strong>${esc(marker.name)}</strong><p>${marker.kind==='population'?`${populationLabel(marker.value)} Muslims · ${marker.year}<br>Approximate whole-region count. The marker is a regional locator, not a city population.`:'A representative location in this chapter. Connections are schematic; a marker does not imply that everyone here was Muslim.'}</p>`;
  main.querySelectorAll('[data-place]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.place===marker.id)));
  globe?.focus(marker.lat,marker.lon);
 }
 function setChapter(next,manual=true){
  if(manual)pause();index=Math.max(0,Math.min(data.events.length-1,next));
  const e=data.events[index],markers=markersFor(data,e),year=regionalYear(e);
  history.replaceState(null,'',`#spread/${e.id}`);
  main.querySelector('#atlas-date').textContent=e.date;
  main.querySelector('#chapter-title').textContent=e.title;
  main.querySelector('#chapter-copy').textContent=e.text;
  main.querySelector('#chapter-kind').textContent=e.mechanism;
  main.querySelector('#population-number').textContent=populationLabel(e.population?.value);
  main.querySelector('#population-note').textContent=e.population?e.population.note:'No reliable worldwide count is supplied for this period.';
  main.querySelector('#population-source').innerHTML=e.population?sourceLink(e.population.series):'';
  main.querySelector('#chapter-sources').innerHTML=e.sources.map(s=>`<li>${sourceLink(s)}</li>`).join('');
  main.querySelector('#map-caption').textContent=year?`${year} regional population snapshot · Pew Research Center`:'Selected historical connections · not territorial boundaries';
  main.querySelector('#map-legend').textContent=year?'● Circle area represents regional Muslim population. Outlined targets help select small circles.':'● Selected places     ┄ Broad connections';
  main.querySelector('#map-context').textContent=year===2020&&e.year===2026?'2026 global estimate above; the regional map is dated 2020.':e.year===null?'Modern coastlines for orientation. No dates or locations are assigned to Adam.':!markers.length?'Global estimate only. No regional distribution is inferred for this year.':'Modern coastlines for orientation; markers do not show religious majorities.';
  main.querySelector('#atlas-slider').value=index;main.querySelector('#atlas-slider').setAttribute('aria-valuetext',e.date+' — '+e.title);
  main.querySelector('#chapter-count').textContent=`${String(index+1).padStart(2,'0')} / ${data.events.length} chapters`;
  main.querySelector('#atlas-prev').disabled=index===0;main.querySelector('#atlas-next').disabled=index===data.events.length-1;
  main.querySelector('#atlas-era').value=index;
  main.querySelector('#place-detail').hidden=true;
  main.querySelector('#location-list').innerHTML=markers.length?markers.map(m=>`<button class="location-choice" data-place="${m.id}" aria-pressed="false"><span>${esc(m.name)}</span>${m.value!=null?`<b>${populationLabel(m.value)}</b>`:'<span aria-hidden="true">↗</span>'}</button>`).join(''):'<p class="subtle">No geographic population distribution is asserted in this chapter.</p>';
  main.querySelectorAll('[data-place]').forEach(button=>button.onclick=()=>showMarker(markers.find(m=>m.id===button.dataset.place)));
  main.querySelectorAll('[data-snapshot]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.snapshot===e.id)));
  globe?.update(markers,e.links,data.places,cumulativeAtlasContext(data,index));
 }
 async function setup(){
  try{
   const r=await fetch('/data/atlas.json',{cache:'no-cache',signal:abort.signal});if(!r.ok)throw Error('Atlas data unavailable');data=await r.json();if(disposed)return;
   const found=data.events.findIndex(e=>e.id===chapter);index=found<0?0:found;
   main.querySelector('#atlas-content').innerHTML=`<div class="atlas-frame"><div class="atlas-world"><div class="map-topline"><span id="map-caption"></span><span class="badge">3D WORLD ATLAS</span></div><div class="globe-host" id="globe-host"><p class="globe-loading" role="status">Drawing the world…</p></div><div class="globe-tools" aria-label="Globe controls"><button id="globe-left" aria-label="Rotate globe west">←</button><button id="globe-right" aria-label="Rotate globe east">→</button><button id="globe-in" aria-label="Zoom in">+</button><button id="globe-out" aria-label="Zoom out">−</button><button id="globe-reset" aria-label="Reset globe view">↺</button></div><div class="map-bottomline"><span id="map-legend"></span><span>Drag to rotate</span></div></div><aside class="atlas-story"><p class="eyebrow" id="atlas-date"></p><span id="chapter-kind" class="badge"></span><h2 id="chapter-title"></h2><p id="chapter-copy"></p><div class="population-panel"><span class="eyebrow">Muslims worldwide · approximate</span><p id="population-number"></p><p id="population-note" class="subtle"></p><p id="population-source" class="subtle"></p></div><details class="chapter-references"><summary>Read this chapter’s sources</summary><ul id="chapter-sources"></ul></details></aside><div class="atlas-controls"><div class="play-controls"><button class="primary" id="atlas-play" aria-pressed="false">▶ Play history</button><button class="secondary" id="atlas-prev" aria-label="Previous chapter">←</button><button class="secondary" id="atlas-next" aria-label="Next chapter">→</button><label class="sr-only" for="atlas-speed">Playback speed</label><select id="atlas-speed" aria-label="Playback speed"><option value="0.5">0.5×</option><option value="1" selected>1×</option><option value="2">2×</option></select><span id="chapter-count" class="subtle"></span><label class="sr-only" for="atlas-era">Jump to a historical chapter</label><select id="atlas-era">${data.events.map((e,i)=>`<option value="${i}">${esc(e.date)} — ${esc(e.title)}</option>`).join('')}</select></div><label for="atlas-slider" class="sr-only">Historical chapter, not a linear year scale</label><input type="range" id="atlas-slider" min="0" max="${data.events.length-1}" step="1" value="0"><div class="atlas-ticks"><span>Adam · undated</span><span>Early Islam</span><span>Global connections</span><span>2026</span></div><p class="subtle">Each step is a chapter. The gaps between years are not equal. Turquoise extents are illustrative areas around sourced locations—not borders, territory, or conversion percentages.</p></div></div><p id="map-context" class="atlas-context"></p><div class="atlas-below"><section><p class="eyebrow">Explore the map</p><h2>Places & communities</h2><div id="location-list"></div><div id="place-detail" class="note" hidden></div></section><section><p class="eyebrow">Population, in perspective</p><h2>Snapshots, not a census.</h2><p class="subtle">Published global estimates. Source methods differ; these are separate snapshots, not one continuous growth series.</p><div class="population-snapshots">${data.events.filter(e=>e.population).map(e=>`<button data-snapshot="${e.id}" aria-pressed="false"><span>${e.year}</span><strong>${populationLabel(e.population.value)}</strong><span class="snapshot-bar" style="--bar:${e.population.value/2105142000*100}%"></span><small>${e.population.series==='pew'?'Pew · 2025 edition':'WCD · 2026 edition'}</small></button>`).join('')}</div></section></div><details class="atlas-method"><summary>How to read this atlas · sources & limits</summary><ul>${data.methodology.map(m=>`<li>${esc(m)}</li>`).join('')}</ul><p>Coastlines: <a href="https://www.naturalearthdata.com/about/terms-of-use/" target="_blank" rel="noopener noreferrer">Natural Earth, public domain</a>. Globe: <a href="https://threejs.org" target="_blank" rel="noopener noreferrer">Three.js</a>. <a href="/vendor/NOTICE.txt">Asset credits</a>.</p><p><a href="/data/atlas.json">Download the sourced atlas data</a> · Reviewed ${esc(data.reviewed)}</p></details>`;
   setChapter(index,false);
   main.querySelector('#atlas-slider').oninput=e=>setChapter(Number(e.target.value));
   main.querySelector('#atlas-era').onchange=e=>setChapter(Number(e.target.value));
   main.querySelector('#atlas-prev').onclick=()=>setChapter(index-1);main.querySelector('#atlas-next').onclick=()=>setChapter(index+1);
   const startPlayback=()=>{const button=main.querySelector('#atlas-play');button.textContent='Ⅱ Pause';button.setAttribute('aria-pressed','true');timer=setInterval(()=>{if(document.hidden)return;if(index>=data.events.length-1){pause();return}setChapter(index+1,false);globe?.tour(markersFor(data,data.events[index]))},playbackDelay(speed))};
   main.querySelector('#atlas-play').onclick=()=>{if(timer){pause();return}if(index===data.events.length-1)setChapter(0,false);startPlayback()};
   main.querySelector('#atlas-speed').onchange=e=>{speed=Number(e.target.value);if(timer){clearInterval(timer);startPlayback()}};
   main.querySelectorAll('[data-snapshot]').forEach(b=>b.onclick=()=>setChapter(data.events.findIndex(e=>e.id===b.dataset.snapshot)));
   const host=main.querySelector('#globe-host');
   try{
    const [module,r]=await Promise.all([import('./world-globe.js'),fetch('/data/maps/land.geojson',{signal:abort.signal})]);if(!r.ok)throw Error('Map unavailable');const land=await r.json();if(disposed)return;
    globe=module.createGlobe(host,land,showMarker);host.querySelector('.globe-loading').remove();
    const current=data.events[index];globe.update(markersFor(data,current),current.links,data.places,{extentIds:current.places,priorLinks:[]});
    let longitude=35;
    main.querySelector('#globe-left').onclick=()=>globe.focus(20,longitude-=35);main.querySelector('#globe-right').onclick=()=>globe.focus(20,longitude+=35);
    main.querySelector('#globe-in').onclick=()=>globe.zoom(-.35);main.querySelector('#globe-out').onclick=()=>globe.zoom(.35);main.querySelector('#globe-reset').onclick=()=>{longitude=35;globe.reset()};
   }catch(error){if(disposed)return;host.replaceChildren();const fallback=document.createElement('p');fallback.className='globe-error';fallback.textContent='The 3D globe is unavailable in this browser. You can still explore every chapter, population estimate and location below.';host.append(fallback);main.querySelectorAll('.globe-tools button').forEach(b=>b.disabled=true)}
  }catch(error){if(disposed)return;main.querySelector('#atlas-content').innerHTML='<div class="note"><p>The atlas could not load. Please check your connection.</p><button class="primary" id="atlas-retry">Retry atlas</button></div>';main.querySelector('#atlas-retry').onclick=setup}
 }
 setup();
 return ()=>{disposed=true;pause();abort.abort();globe?.destroy()};
}
