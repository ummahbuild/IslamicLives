"""Generate crawlable HTML entry points, sitemap, robots.txt, and llms.txt."""
import html, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PUBLIC=ROOT/'public'
SITE='https://islamic-lives.pages.dev'
data=json.loads((PUBLIC/'data/people.json').read_text())

def e(value): return html.escape(str(value), quote=True)
def shell(title,description,canonical,body,route,schema):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#101411"><title>{e(title)}</title><meta name="description" content="{e(description)}"><meta name="author" content="ummah.build"><link rel="canonical" href="{e(canonical)}"><link rel="author" href="https://ummah.build"><link rel="me" href="https://www.youtube.com/@ummah_build"><meta property="og:type" content="article"><meta property="og:site_name" content="Islamic Lives"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{e(canonical)}"><meta name="twitter:card" content="summary"><meta name="twitter:creator" content="@ummahbuild"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(description)}"><link rel="stylesheet" href="/style.css"><link rel="icon" href="/icon.svg" type="image/svg+xml"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False).replace('</','<\\/')}</script><script>window.__INITIAL_ROUTE__={json.dumps(route)}</script><script src="/app.js" type="module"></script></head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="/"><span class="seal">✧</span> ISLAMIC LIVES</a><nav aria-label="Main"><a href="/people/">People</a><a href="/scholars/">Scholars</a><a href="/#spread">The spread of Islam</a><a href="/#about">Sources &amp; approach</a></nav></header><main id="main" tabindex="-1">{body}</main><footer data-site-footer></footer></body></html>'''

urls=[SITE+'/']
for p in data['people']:
 kind='prophets' if p['category']=='Prophets' else 'people'
 path=f'/{kind}/{p["id"]}/'; canonical=SITE+path
 description=f'{p["name"]}: {p["role"]}. A sourced Islamic Lives profile with evidence notes and references.'
 sections=''.join(f'<section><h2>{e(c["title"])}</h2><p>{e(c["text"])}</p></section>' for c in p['chapters'])
 sunnah=p.get('sunnahEvidence')
 sunnah_html='' if not sunnah else f'<section><h2>Sunnah reference</h2><p><strong>{e(sunnah["status"])}</strong>: {e(sunnah["text"])}</p></section>'
 source_html='<section><h2>Sources</h2><ol>'+''.join(f'<li><a href="{e(s["url"])}">{e(s["title"])}</a> — {e(s["kind"])}</li>' for s in p['sources'])+'</ol></section>'
 body=f'<article class="article static-fallback"><p class="eyebrow">{e(p["category"])} · sourced profile</p><div class="arabic" lang="ar" dir="rtl">{e(p["arabic"])}</div><h1>{e(p["name"])}</h1><p class="lede">{e(p["role"])}</p><p>{e(p["date"])} · {e(p["place"])}</p>{sections}<p class="note">{e(p["uncertainty"])}</p>{sunnah_html}{source_html}</article>'
 schema={'@context':'https://schema.org','@type':'ProfilePage','name':title if (title:=p['name']+' — Islamic Lives') else '', 'description':description,'url':canonical,'mainEntity':{'@type':'Person','name':p['name'],'description':p['role']}}
 target=PUBLIC/path.strip('/')/'index.html'; target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(shell(title,description,canonical,body,f'journey/{p["id"]}/story',schema))
 urls.append(canonical)

scholars=[p for p in data['people'] if p['category']=='Islamic scholars']
people_body='<article class="wide static-fallback"><p class="eyebrow">The people collection</p><h1>Lives worth knowing.</h1><p>All 25 traditionally listed Qur’anic prophets, Islamic scholars, Companions, and people across Islamic history.</p><ul>'+''.join(f'<li><a href="/{"prophets" if p["category"]=="Prophets" else "people"}/{e(p["id"])}/">{e(p["name"])}</a> — {e(p["role"])}</li>' for p in data['people'])+'</ul></article>'
people_schema={'@context':'https://schema.org','@type':'CollectionPage','name':'People — Islamic Lives','description':'Browse sourced profiles of Qur’anic prophets, scholars, Companions, and historical people.','url':SITE+'/people/'}
target=PUBLIC/'people/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(shell(people_schema['name'],people_schema['description'],people_schema['url'],people_body,'library',people_schema));urls.append(people_schema['url'])
body='<article class="wide static-fallback"><p class="eyebrow">Islamic scholars</p><h1>Learning rooted in Qur’an and Sunnah.</h1><p>A bounded, sourced introduction to scholars whose work shaped Islamic law and the transmission of knowledge.</p><ul>'+''.join(f'<li><a href="/people/{e(p["id"])}/">{e(p["name"])}</a> — {e(p["role"])}</li>' for p in scholars)+'</ul></article>'
schema={'@context':'https://schema.org','@type':'CollectionPage','name':'Islamic Scholars — Islamic Lives','description':'Sourced profiles of Islamic scholars, with Qur’an and Sunnah references.','url':SITE+'/scholars/'}
target=PUBLIC/'scholars/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(shell(schema['name'],schema['description'],schema['url'],body,'scholars',schema));urls.append(schema['url'])
(PUBLIC/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+SITE+'/sitemap.xml\n')
(PUBLIC/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{e(u)}</loc></url>' for u in urls)+'</urlset>\n')
(PUBLIC/'llms.txt').write_text('# Islamic Lives\n\nA sourced collection of people in Islamic scripture and history.\n\n- [People dataset](/data/people.json)\n- [Quran mention index](/data/quran-mentions.json)\n- [Coverage and limitations](/data/coverage.json)\n- [Research approach](/#about)\n\nReligious reports, historical claims, and uncertainty notes are labelled separately. Do not treat the collection as exhaustive or as a source of religious rulings.\n')
print(f'Wrote {len(urls)} crawlable URLs')
