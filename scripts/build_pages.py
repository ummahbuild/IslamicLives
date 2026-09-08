"""Generate crawlable HTML entry points, sitemap, robots.txt, and llms.txt."""
import html, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PUBLIC=ROOT/'public'
SITE='https://islamic-lives.pages.dev'
SOCIAL_IMAGE=SITE+'/og.png'
data=json.loads((PUBLIC/'data/people.json').read_text())

def e(value): return html.escape(str(value), quote=True)
def shell(title,description,canonical,body,route,schema):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#101411"><title>{e(title)}</title><meta name="description" content="{e(description)}"><meta name="author" content="ummah.build"><link rel="canonical" href="{e(canonical)}"><link rel="author" href="https://ummah.build"><link rel="me" href="https://www.youtube.com/@ummah_build"><meta property="og:type" content="article"><meta property="og:site_name" content="Islamic Lives"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{e(canonical)}"><meta name="twitter:card" content="summary"><meta name="twitter:creator" content="@ummahbuild"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(description)}"><link rel="stylesheet" href="/style.css"><link rel="icon" href="/icon.svg" type="image/svg+xml"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False).replace('</','<\\/')}</script><script>window.__INITIAL_ROUTE__={json.dumps(route)}</script><script src="/app.js" type="module"></script></head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="/"><span class="seal">✧</span> ISLAMIC LIVES</a><nav aria-label="Main"><a href="/people/">People</a><a href="/scholars/">Scholars</a><a href="/#spread">The spread of Islam</a><a href="/#about">Sources &amp; approach</a></nav></header><main id="main" tabindex="-1">{body}</main><footer data-site-footer></footer></body></html>'''

def add_social(path):
 page=path.read_text()
 social=f'<meta property="og:image" content="{SOCIAL_IMAGE}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Islamic Lives — Qur’an, Sunnah, History"><meta name="twitter:image" content="{SOCIAL_IMAGE}"><meta name="twitter:image:alt" content="Islamic Lives — Qur’an, Sunnah, History">'
 page=page.replace('<meta name="twitter:card" content="summary">',social+'<meta name="twitter:card" content="summary_large_image">')
 path.write_text(page)

urls=[SITE+'/']
for p in data['people']:
 kind='prophets' if p['category']=='Prophets' else 'people'
 path=f'/{kind}/{p["id"]}/'; canonical=SITE+path
 description=f'{p["name"]}: {p["role"]}. A sourced Islamic Lives profile with evidence notes and references.'
 sections=''.join(f'<section><h2>{e(c["title"])}</h2><p>{e(c["text"])}</p></section>' for c in p['chapters'])
 sunnah=p.get('sunnahEvidence')
 sunnah_html='' if not sunnah else f'<section><h2>Sunnah reference</h2><p><strong>{e(sunnah["status"])}</strong>: {e(sunnah["text"])}</p></section>'
 passages=p.get('keyQuranPassages',[])
 passage_html='' if not passages else '<section><h2>Key Qur’anic passages</h2><p>A curated narrative reading list; not an exhaustive tafsir index.</p><ul>'+''.join(f'<li><a href="https://quran.com/{e(ref.replace(":","/"))}">Qur’an {e(ref)}</a></li>' for ref in passages)+'</ul></section>'
 check=p.get('factCheck')
 check_html='' if not check else f'<section><h2>Review status</h2><p><strong>{e(check["status"])}</strong> · {e(check["checked"])}</p><p>{e(check["scope"])}</p></section>'
 source_html='<section><h2>Sources</h2><ol>'+''.join(f'<li><a href="{e(s["url"])}">{e(s["title"])}</a> — {e(s["kind"])}</li>' for s in p['sources'])+'</ol></section>'
 source_types=' · '.join(dict.fromkeys(s['kind'] for s in p['sources']))
 facts=f'<dl class="fact-grid" aria-label="Profile facts"><div><dt>Date</dt><dd>{e(p["date"])}</dd></div><div><dt>Associated place</dt><dd>{e(p["place"])}</dd></div><div><dt>Collection</dt><dd>{e(p["category"])}</dd></div><div><dt>Source types</dt><dd>{e(source_types)}</dd></div></dl>'
 body=f'<article class="article static-fallback"><p class="eyebrow">{e(p["category"])} · sourced profile</p><div class="arabic" lang="ar" dir="rtl">{e(p["arabic"])}</div><h1>{e(p["name"])}</h1><p class="lede">{e(p["role"])}</p>{facts}{sections}<p class="note">{e(p["uncertainty"])}</p>{passage_html}{sunnah_html}{check_html}{source_html}</article>'
 schema={'@context':'https://schema.org','@type':'ProfilePage','name':title if (title:=p['name']+' — Islamic Lives') else '', 'description':description,'url':canonical,'mainEntity':{'@type':'Person','name':p['name'],'description':p['role']}}
 target=PUBLIC/path.strip('/')/'index.html'; target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(shell(title,description,canonical,body,f'journey/{p["id"]}/story',schema))
 urls.append(canonical)

scholars=[p for p in data['people'] if p['category']=='Islamic scholars']
prophets=[p for p in data['people'] if p['category']=='Prophets']
people_body='<article class="wide static-fallback"><p class="eyebrow">The people collection</p><h1>Lives worth knowing.</h1><p>All 25 traditionally listed Qur’anic prophets, Islamic scholars, Companions, and people across Islamic history.</p><ul>'+''.join(f'<li><a href="/{"prophets" if p["category"]=="Prophets" else "people"}/{e(p["id"])}/">{e(p["name"])}</a> — {e(p["role"])}</li>' for p in data['people'])+'</ul></article>'
people_schema={'@context':'https://schema.org','@type':'CollectionPage','name':'People — Islamic Lives','description':'Browse sourced profiles of Qur’anic prophets, scholars, Companions, and historical people.','url':SITE+'/people/'}
target=PUBLIC/'people/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(shell(people_schema['name'],people_schema['description'],people_schema['url'],people_body,'library',people_schema));urls.append(people_schema['url'])
add_social(target)
explore_body='<article class="wide static-fallback"><p class="eyebrow">Explore Islamic Lives</p><h1>Choose a path through the collection.</h1><p>Explore Qur’anic prophets, Islamic scholars, all people, or the historical atlas.</p><ul><li><a href="/prophets/">Explore the Prophets</a></li><li><a href="/scholars/">Islamic Scholars</a></li><li><a href="/people/">All People</a></li><li><a href="/#spread">The Spread of Islam</a></li></ul></article>'
explore_schema={'@context':'https://schema.org','@type':'CollectionPage','name':'Explore Islamic Lives','description':'Explore Qur’anic prophets, Islamic scholars, historical people, and the spread of Islam.','url':SITE+'/explore/'}
target=PUBLIC/'explore/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(shell(explore_schema['name'],explore_schema['description'],explore_schema['url'],explore_body,'explore',explore_schema));urls.append(explore_schema['url'])
add_social(target)
prophet_body='<article class="wide static-fallback"><p class="eyebrow">Explore the prophets</p><h1>Twenty-five lives, traceable to their sources.</h1><p>Every profile in the commonly taught list has Qur’anic references and an explicit verified-reference or research-gap status for Sunnah coverage.</p><ol>'+''.join(f'<li><a href="/prophets/{e(p["id"])}/">{e(p["name"])}</a> — {e(p["role"])}; {e(p["sunnahEvidence"]["status"])}</li>' for p in prophets)+'</ol></article>'
prophet_schema={'@context':'https://schema.org','@type':'CollectionPage','name':'Explore the Prophets — Islamic Lives','description':'Explore 25 sourced prophet profiles with Qur’an references, verified Sunnah references, and visible research gaps.','url':SITE+'/prophets/','numberOfItems':25}
target=PUBLIC/'prophets/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(shell(prophet_schema['name'],prophet_schema['description'],prophet_schema['url'],prophet_body,'prophets',prophet_schema));urls.append(prophet_schema['url'])
add_social(target)
body='<article class="wide static-fallback"><p class="eyebrow">Islamic scholars</p><h1>Learning rooted in Qur’an and Sunnah.</h1><p>A bounded, sourced introduction to scholars whose work shaped Islamic law and the transmission of knowledge.</p><ul>'+''.join(f'<li><a href="/people/{e(p["id"])}/">{e(p["name"])}</a> — {e(p["role"])}</li>' for p in scholars)+'</ul></article>'
schema={'@context':'https://schema.org','@type':'CollectionPage','name':'Islamic Scholars — Islamic Lives','description':'Sourced profiles of Islamic scholars, with Qur’an and Sunnah references.','url':SITE+'/scholars/'}
target=PUBLIC/'scholars/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(shell(schema['name'],schema['description'],schema['url'],body,'scholars',schema));urls.append(schema['url'])
add_social(target)
coverage=json.loads((PUBLIC/'data/coverage.json').read_text())
about_body='<article class="article static-fallback"><p class="eyebrow">Sources and approach</p><h1>Named people. Traceable accounts. Honest limits.</h1><p>Qur’anic accounts, hadith reports, historical primary texts, and modern scholarship are labelled separately. Unsupported dates, locations, dialogue, and appearance are not invented.</p><h2>Coverage</h2><ul>'+''.join(f'<li><strong>{e(row["collection"])}</strong>: {e(row["status"])}</li>' for row in coverage)+'</ul><p><a href="/data/people.json">Download the people data</a> · <a href="/data/coverage.json">Download the coverage record</a></p></article>'
about_schema={'@context':'https://schema.org','@type':'AboutPage','name':'Sources and approach — Islamic Lives','description':'How Islamic Lives separates scripture, transmitted reports, history, and uncertainty.','url':SITE+'/about/'}
target=PUBLIC/'about/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(shell(about_schema['name'],about_schema['description'],about_schema['url'],about_body,'about',about_schema));urls.append(about_schema['url'])
add_social(target)
spread_data=json.loads((PUBLIC/'data/spread.json').read_text())
spread_body=f'<article class="wide static-fallback"><p class="eyebrow">Historical atlas</p><h1>The spread of Islam.</h1><p>{len(spread_data)} sourced chapters connect places, people, and periods through the 2026 research horizon. The interactive globe enhances this page when JavaScript is available.</p><ol>'+''.join(f'<li><strong>{e(item.get("title",item.get("year","Chapter")))}</strong> — {e(item.get("text",item.get("description","")))}</li>' for item in spread_data)+'</ol></article>'
spread_schema={'@context':'https://schema.org','@type':'CollectionPage','name':'The Spread of Islam — Islamic Lives','description':'A sourced historical atlas of the spread of Islam through the 2026 research horizon.','url':SITE+'/spread/','numberOfItems':len(spread_data)}
target=PUBLIC/'spread/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(shell(spread_schema['name'],spread_schema['description'],spread_schema['url'],spread_body,'spread',spread_schema));urls.append(spread_schema['url'])
add_social(target)
home=PUBLIC/'index.html'
home_html=home.read_text()
if 'name="twitter:title"' not in home_html:
 home_html=home_html.replace('<title>Islamic Lives', '<meta name="twitter:title" content="Islamic Lives — Qur’anic prophets, scholars, and history"><meta name="twitter:description" content="Explore sourced lives from the Qur’an, Sunnah, and Islamic history."><title>Islamic Lives')
home_html=home_html.replace('<p class="loading">Opening the collection…</p>', '<div class="loading-shell" role="status" aria-live="polite"><div class="loading-mark" aria-hidden="true"></div><div class="loading-line title" aria-hidden="true"></div><div class="loading-line" aria-hidden="true"></div><div class="loading-line short" aria-hidden="true"></div><p class="loading-label">OPENING THE COLLECTION…</p></div>')
home.write_text(home_html)
add_social(home)
(PUBLIC/'404.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><meta name="theme-color" content="#101411"><title>Page not found — Islamic Lives</title><link rel="stylesheet" href="/style.css"><link rel="icon" href="/icon.svg" type="image/svg+xml"></head><body><header><a class="brand" href="/"><span class="seal">✧</span> ISLAMIC LIVES</a></header><main class="empty"><p class="eyebrow">404</p><h1>That page is not in the collection.</h1><p>The link may have changed, or this life may not have been researched yet.</p><div class="actions"><a class="primary" href="/explore/">Explore the collection</a><a class="secondary" href="/">Return home</a></div></main></body></html>''')
(PUBLIC/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+SITE+'/sitemap.xml\n')
(PUBLIC/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{e(u)}</loc></url>' for u in urls)+'</urlset>\n')
(PUBLIC/'llms.txt').write_text('# Islamic Lives\n\nA sourced collection of people in Islamic scripture and history.\n\n- [People dataset](/data/people.json)\n- [Quran mention index](/data/quran-mentions.json)\n- [Coverage and limitations](/data/coverage.json)\n- [Research approach](/#about)\n\nReligious reports, historical claims, and uncertainty notes are labelled separately. Do not treat the collection as exhaustive or as a source of religious rulings.\n')
print(f'Wrote {len(urls)} crawlable URLs')
