import json
from pathlib import Path
from urllib.parse import urlparse
r=Path(__file__).resolve().parents[1]
data=json.loads((r/'public/data/people.json').read_text()); people=data['people']
assert len({p['id'] for p in people})==len(people),'Duplicate people'
expected={'adam','idris','nuh','hud','salih','ibrahim','lut','ismail','ishaq','yaqub','yusuf','ayyub','shuayb','musa','harun','dhul-kifl','dawud','sulayman','ilyas','alyasa','yunus','zakariyya','yahya','isa','muhammad'}
assert {p['id'] for p in people if p['category']=='Prophets'}==expected
requested_additions={'bilal','fatimah','anas-ibn-malik','abu-hurayrah','dhul-qarnayn','mother-musa','madyan-elder','adam-son-offering','adam-son-aggressor','asma-bint-abi-bakr','hafsah-bint-umar','umm-salamah','umm-sulaym','ibn-abbas','abu-talha','al-ghazali','ibn-rushd','ibn-khaldun'}
assert len(people)==81,'The complete requested collection currently contains 81 records'
assert requested_additions <= {p['id'] for p in people},'A requested sourced profile is missing'
for p in people:
 assert p['uncertainty'] and p['chapters'] and p['sources'],p['id']
 review=p.get('editorialReview',{})
 assert review.get('status')=='structure-checked' and review.get('reviewedOn') and review.get('scholarReviewed') is False,p['id']
 if p['era']=='Qur’anic accounts':assert p['year'] is None and p['coordinates'] is None
 for field in ['dateEvidence','placeEvidence']:
  if field in p:
   e=p[field];assert e['status'] and e['text'] and e['sources']
   assert all(isinstance(i,int) and 0<=i<len(p['sources']) for i in e['sources'])
 for s in p['sources']:
  assert urlparse(s['url']).scheme=='https' and s['title']
  if 'quran.com/' in s['url']:assert 'Surah ' in s['title'] and __import__('re').search(r'\d{1,3}:\d',s['title']),p['id']
 for c in p['chapters']:
  assert c['text'] and c['sources']
  assert all(isinstance(i,int) and 0<=i<len(p['sources']) for i in c['sources'])
 if p['category']=='Prophets':
  assert 'quranReferences' in p and p['quranReferences'],p['id']
  assert p.get('keyQuranPassages') and p.get('factCheck',{}).get('status')=='Source-alignment checked',p['id']
  assert all(__import__('re').fullmatch(r'\d{1,3}:\d{1,3}(?:-\d{1,3})?',ref) for ref in p['keyQuranPassages']),p['id']
  assert 'sunnahEvidence' in p,p['id']
  se=p['sunnahEvidence']
  assert se['status'] in {'Referenced','Research gap'} and se['text']
  assert all(isinstance(i,int) and 0<=i<len(p['sources']) and p['sources'][i]['kind']=='Hadith' for i in se['sources'])
for event in json.loads((r/'public/data/spread.json').read_text()):assert event['source'] and event['url'].startswith('https://')
assert 'Partial' in data['coverage']
print(f'PASS: {len(people)} unique records; 25 prophet identities; citation integrity; undated-scriptural invariant. This validates structure, not historical truth or exhaustive coverage.')
mentions=json.loads((r/'public/data/quran-mentions.json').read_text())['entries']
assert len({e['personId'] for e in mentions})==len(mentions)
for e in mentions:
 assert e['personId'] in {p['id'] for p in people}
 assert e['tokenCount']==len(set(e['wordLocations']))
 assert set(e['verses'])=={':'.join(w.split(':')[:2]) for w in e['wordLocations']}
 assert all(1<=int(w.split(':')[0])<=114 for w in e['wordLocations'])
 assert e['pages'] and e['source'].startswith('https://corpus.quran.com/')
assert next(e for e in mentions if e['personId']=='musa')['tokenCount']==136
assert next(e for e in mentions if e['personId']=='adam')['tokenCount']==25
generated=r/'public/prophets/index.html'
assert generated.exists() and all(f'/prophets/{pid}/' in generated.read_text() for pid in expected)
assert (r/'public/explore/index.html').exists()
assert all((r/f'public/{route}').exists() for route in ['about/index.html','spread/index.html','404.html'])
print(f'PASS: {len(mentions)} name-index records and source location integrity. Source omissions and unnamed mentions still require a separate audit.')
