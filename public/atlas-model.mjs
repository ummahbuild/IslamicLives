export function populationLabel(value){
 if(value==null)return 'Not established';
 return value>=1e9?`≈ ${(value/1e9).toFixed(1)} billion`:value>=1e6?`≈ ${Math.round(value/1e6).toLocaleString('en')} million`:`≈ ${Math.round(value/1e3).toLocaleString('en')} thousand`;
}
export function regionalYear(event){return event.year>=2020?2020:event.year===2010?2010:null}
export function markersFor(data,event){
 const year=regionalYear(event);
 return year?data.regions.map(r=>({...r,value:r.snapshots[year].value,year,kind:'population'})):event.places.map(id=>({...data.places.find(p=>p.id===id),value:null,kind:'history'}));
}
export function pointOnSphere(lat,lon,radius=1){
 const a=lat*Math.PI/180,o=lon*Math.PI/180;
 return [radius*Math.cos(a)*Math.cos(o),radius*Math.sin(a),-radius*Math.cos(a)*Math.sin(o)];
}
export function playbackDelay(speed,base=5000){return base/Math.max(.5,Math.min(2,Number(speed)||1))}
export function cumulativeAtlasContext(data,index){
 const current=data.events[index],earlier=data.events.slice(0,index),markers=markersFor(data,current),year=regionalYear(current);
 return {extentIds:year?[...new Set(markers.map(marker=>marker.id))]:[...new Set([...earlier.flatMap(event=>event.places),...current.places])],priorLinks:earlier.flatMap(event=>event.links)};
}
export function tourStops(markers){return markers.map(({id,lat,lon})=>({id,lat,lon}))}
