import * as THREE from './vendor/three/three.module.min.js';
import {pointOnSphere} from './atlas-model.mjs';

export function createGlobe(host,land,onSelect){
 const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
 const scene=new THREE.Scene();
 const camera=new THREE.PerspectiveCamera(36,1,.1,30);camera.position.z=3.8;
 const renderer=new THREE.WebGLRenderer({alpha:true,antialias:true,powerPreference:'low-power'});
 renderer.setPixelRatio(Math.min(devicePixelRatio,2));
 renderer.outputColorSpace=THREE.SRGBColorSpace;
 const canvas=renderer.domElement;canvas.setAttribute('aria-label','Interactive globe. Drag to rotate; use the nearby controls to zoom and the location list to select a place.');canvas.setAttribute('role','img');
 host.append(canvas);
 const root=new THREE.Group();scene.add(root);
 const textureCanvas=document.createElement('canvas');textureCanvas.width=2048;textureCanvas.height=1024;
 const ctx=textureCanvas.getContext('2d');ctx.fillStyle='#101f21';ctx.fillRect(0,0,2048,1024);
 ctx.fillStyle='#3c5145';ctx.strokeStyle='#7e927166';ctx.lineWidth=1;
 for(const feature of land.features){
  const polys=feature.geometry.type==='Polygon'?[feature.geometry.coordinates]:feature.geometry.coordinates;
  for(const polygon of polys){
   ctx.beginPath();
   for(const ring of polygon){ring.forEach(([lon,lat],i)=>{const x=(lon+180)/360*2048,y=(90-lat)/180*1024;i?ctx.lineTo(x,y):ctx.moveTo(x,y)});ctx.closePath()}
   ctx.fill('evenodd');ctx.stroke();
  }
 }
 const texture=new THREE.CanvasTexture(textureCanvas);texture.colorSpace=THREE.SRGBColorSpace;texture.anisotropy=Math.min(4,renderer.capabilities.getMaxAnisotropy());
 root.add(new THREE.Mesh(new THREE.SphereGeometry(1,80,48),new THREE.MeshBasicMaterial({map:texture})));
 // Geographic graticule, clipped by the opaque globe on its far side.
 const grid=[];
 function segment(a,b){grid.push(...pointOnSphere(...a,1.002),...pointOnSphere(...b,1.002))}
 for(let lat=-60;lat<=60;lat+=30)for(let lon=-180;lon<180;lon+=3)segment([lat,lon],[lat,lon+3]);
 for(let lon=-180;lon<180;lon+=30)for(let lat=-90;lat<90;lat+=3)segment([lat,lon],[lat+3,lon]);
 root.add(new THREE.LineSegments(new THREE.BufferGeometry().setAttribute('position',new THREE.Float32BufferAttribute(grid,3)),new THREE.LineBasicMaterial({color:0xabc4a2,transparent:true,opacity:.12})));
 const atmosphere=new THREE.Mesh(new THREE.SphereGeometry(1.035,64,32),new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.BackSide,uniforms:{glowColor:{value:new THREE.Color('#aecb9b')}},vertexShader:'varying vec3 n; varying vec3 v; void main(){ vec4 p=modelViewMatrix*vec4(position,1.0); n=normalize(normalMatrix*normal); v=normalize(-p.xyz); gl_Position=projectionMatrix*p; }',fragmentShader:'uniform vec3 glowColor; varying vec3 n; varying vec3 v; void main(){ float g=pow(1.0-abs(dot(n,v)),3.0); gl_FragColor=vec4(glowColor,g*0.22); }'}));root.add(atmosphere);
 const layer=new THREE.Group();root.add(layer);
 let picks=[],labels=[],frame=0,disposed=false,drag=null,target=null,dirty=true;
 const raycaster=new THREE.Raycaster(),pointer=new THREE.Vector2();
 const abort=new AbortController();
 const listen=(node,type,fn,options={})=>node.addEventListener(type,fn,{...options,signal:abort.signal});
 function clearLayer(){while(layer.children.length){const item=layer.children[0];item.traverse(o=>{o.geometry?.dispose();if(o.material) o.material.dispose()});layer.remove(item)}picks=[];labels.forEach(l=>l.element.remove());labels=[]}
 function focus(lat=20,lon=35){target={x:lat*Math.PI/180,y:-Math.PI/2-lon*Math.PI/180};if(reduced){root.rotation.set(target.x,target.y,0);target=null}dirty=true}
 focus();root.rotation.set(20*Math.PI/180,-Math.PI/2-35*Math.PI/180,0);target=null;
 function update(markers,connections,places){
  clearLayer();
  const positions=new Map(places.map(p=>[p.id,p]));
  for(const [from,to] of connections){
   const a=positions.get(from),b=positions.get(to);if(!a||!b)continue;
   const v1=new THREE.Vector3(...pointOnSphere(a.lat,a.lon)),v2=new THREE.Vector3(...pointOnSphere(b.lat,b.lon));
   const angle=v1.angleTo(v2);const points=[];
   for(let i=0;i<=64;i++){const t=i/64;const v=angle<.001?v1.clone():v1.clone().multiplyScalar(Math.sin((1-t)*angle)).add(v2.clone().multiplyScalar(Math.sin(t*angle))).divideScalar(Math.sin(angle));points.push(v.multiplyScalar(1.012+Math.sin(Math.PI*t)*.13))}
   const line=new THREE.Line(new THREE.BufferGeometry().setFromPoints(points),new THREE.LineDashedMaterial({color:0xd6b776,transparent:true,opacity:.65,dashSize:.025,gapSize:.012}));line.computeLineDistances();layer.add(line);
  }
  for(const marker of markers){
   const population=marker.kind==='population';
   const radius=population?.24*Math.sqrt(marker.value/1.2e9):.012;
   const material=new THREE.MeshBasicMaterial({color:population?0xb7dbaa:0xf2cb80,transparent:true,opacity:population?.65:1,side:THREE.DoubleSide,depthWrite:false});
   const dot=new THREE.Mesh(new THREE.CircleGeometry(radius,48),material);
   const pos=new THREE.Vector3(...pointOnSphere(marker.lat,marker.lon,1.016));dot.position.copy(pos);dot.quaternion.setFromUnitVectors(new THREE.Vector3(0,0,1),pos.clone().normalize());dot.userData.marker=marker;layer.add(dot);picks.push(dot);
   const outline=new THREE.Mesh(new THREE.RingGeometry(Math.max(radius,.022)+.006,Math.max(radius,.022)+.009,48),new THREE.MeshBasicMaterial({color:population?0xc7e6bc:0xd6b776,transparent:true,opacity:.5,side:THREE.DoubleSide,depthWrite:false}));outline.position.copy(pos);outline.quaternion.copy(dot.quaternion);outline.userData.marker=marker;layer.add(outline);picks.push(outline);
   // Invisible but generous picking disk for small regional populations.
   const hit=new THREE.Mesh(new THREE.CircleGeometry(Math.max(radius,.036),24),new THREE.MeshBasicMaterial({visible:false}));hit.position.copy(pos);hit.quaternion.copy(dot.quaternion);hit.userData.marker=marker;layer.add(hit);picks.push(hit);
   const label=document.createElement('span');label.className='globe-place-label';label.textContent=marker.name;label.setAttribute('aria-hidden','true');host.append(label);labels.push({element:label,position:pos});
  }
  if(markers.length){const first=markers[0];focus(first.lat,first.lon)}else focus();
  dirty=true;
 }
 function pick(event){
  const rect=canvas.getBoundingClientRect();pointer.set((event.clientX-rect.left)/rect.width*2-1,-(event.clientY-rect.top)/rect.height*2+1);raycaster.setFromCamera(pointer,camera);
  const hits=raycaster.intersectObjects(picks);for(const h of hits){const normal=h.object.position.clone().applyQuaternion(root.quaternion).normalize();if(normal.dot(camera.position.clone().sub(h.point))>0)return h.object.userData.marker}
  return null;
 }
 listen(canvas,'pointerdown',e=>{if(e.button!==0)return;target=null;drag={id:e.pointerId,x:e.clientX,y:e.clientY,moved:0};canvas.setPointerCapture(e.pointerId);canvas.classList.add('dragging')});
 listen(canvas,'pointermove',e=>{if(drag&&e.pointerId===drag.id){const dx=e.clientX-drag.x,dy=e.clientY-drag.y;drag.moved+=Math.abs(dx)+Math.abs(dy);root.rotation.y+=dx*.006;root.rotation.x=Math.max(-1.4,Math.min(1.4,root.rotation.x+dy*.006));drag.x=e.clientX;drag.y=e.clientY;dirty=true}else canvas.style.cursor=pick(e)?'pointer':'grab'});
 listen(canvas,'pointerup',e=>{if(!drag||e.pointerId!==drag.id)return;if(drag.moved<6){const marker=pick(e);if(marker)onSelect(marker)}drag=null;canvas.classList.remove('dragging')});
 for(const type of ['pointercancel','lostpointercapture'])listen(canvas,type,()=>{drag=null;canvas.classList.remove('dragging')});
 function zoom(delta){camera.position.z=THREE.MathUtils.clamp(camera.position.z+delta,2.4,5.5);dirty=true}
 function resize(){const {width,height}=host.getBoundingClientRect();if(!width||!height)return;renderer.setSize(width,height);camera.aspect=width/height;camera.updateProjectionMatrix();dirty=true}
 const observer=new ResizeObserver(resize);observer.observe(host);resize();
 function tick(){if(disposed)return;frame=requestAnimationFrame(tick);if(document.hidden)return;
  if(target){root.rotation.x=THREE.MathUtils.lerp(root.rotation.x,target.x,.09);root.rotation.y=THREE.MathUtils.lerp(root.rotation.y,target.y,.09);if(Math.abs(root.rotation.x-target.x)+Math.abs(root.rotation.y-target.y)<.002){root.rotation.set(target.x,target.y,0);target=null}dirty=true}
  if(!dirty)return;renderer.render(scene,camera);dirty=false;
  const rect=host.getBoundingClientRect();for(const label of labels){const world=label.position.clone().applyQuaternion(root.quaternion);const visible=world.dot(camera.position.clone().sub(world))>0;const p=world.clone().project(camera);label.element.hidden=!visible||Math.abs(p.x)>.92||Math.abs(p.y)>.9;label.element.style.left=`${(p.x+1)*rect.width/2}px`;label.element.style.top=`${(-p.y+1)*rect.height/2}px`}
 }
 listen(canvas,'webglcontextlost',e=>{e.preventDefault();host.dataset.failed='true';canvas.hidden=true;labels.forEach(l=>l.element.hidden=true);const p=document.createElement('p');p.className='globe-error';p.textContent='The 3D view paused. The timeline and location list remain available. Reload to restore the globe.';host.append(p);disposed=true;cancelAnimationFrame(frame)});
 tick();
 return {update,focus,zoom,reset:()=>{camera.position.z=3.8;focus()},destroy(){disposed=true;cancelAnimationFrame(frame);observer.disconnect();abort.abort();clearLayer();scene.traverse(o=>{o.geometry?.dispose();if(o.material)o.material.dispose()});texture.dispose();renderer.dispose();renderer.forceContextLoss();canvas.remove()}};
}
