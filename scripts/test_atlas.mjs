import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {populationLabel,regionalYear,markersFor,pointOnSphere} from '../public/atlas-model.mjs';
const data=JSON.parse(fs.readFileSync(new URL('../public/data/atlas.json',import.meta.url)));
test('unknown population never becomes zero or a fabricated estimate',()=>{
 for(const event of data.events.filter(e=>e.year===null||e.year<1900)){assert.equal(event.population,null);assert.equal(populationLabel(event.population?.value),'Not established')}
 assert.equal(data.events[0].year,null);assert.deepEqual(markersFor(data,data.events[0]),[]);
});
test('2026 keeps the regional snapshot in 2020 and the global estimate in 2026',()=>{
 const event=data.events.at(-1);assert.equal(event.year,2026);assert.equal(event.population.value,2105142000);assert.equal(event.population.series,'wcd');assert.equal(regionalYear(event),2020);
 for(const m of markersFor(data,event)){assert.equal(m.year,2020);assert.equal(m.value,data.regions.find(r=>r.id===m.id).snapshots['2020'].value)}
});
test('every connection has a cited chapter and valid place endpoints',()=>{
 const ids=new Set(data.places.map(p=>p.id));assert.equal(ids.size,data.places.length);
 for(const event of data.events){assert.ok(event.sources.length);for(const s of event.sources)assert.ok(data.sources[s]?.url.startsWith('https://'));for(const p of event.places)assert.ok(ids.has(p));for(const edge of event.links){assert.equal(edge.length,2);for(const p of edge)assert.ok(ids.has(p)&&event.places.includes(p))}}
});
test('regional calculations preserve rounded source inputs and valid locations',()=>{
 for(const r of data.regions){assert.ok(Math.abs(r.lat)<=90&&Math.abs(r.lon)<=180);for(const y of [2010,2020]){const s=r.snapshots[y];assert.equal(s.value,Math.round(s.total*s.muslimPercent/100))}}
});
test('sphere coordinates match equirectangular texture orientation',()=>{
 const approx=(a,b)=>a.forEach((n,i)=>assert.ok(Math.abs(n-b[i])<1e-10));
 approx(pointOnSphere(0,0),[1,0,0]);approx(pointOnSphere(0,90),[0,0,-1]);approx(pointOnSphere(90,0),[0,1,0]);
 for(const p of data.places){assert.ok(Math.abs(Math.hypot(...pointOnSphere(p.lat,p.lon))-1)<1e-10)}
});
