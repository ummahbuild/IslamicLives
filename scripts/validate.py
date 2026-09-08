import json
from pathlib import Path
from urllib.parse import urlparse
r=Path(__file__).resolve().parents[1]
data=json.loads((r/'public/data/people.json').read_text()); people=data['people']
assert len({p['id'] for p in people})==len(people),'Duplicate people'
expected={'adam','idris','nuh','hud','salih','ibrahim','lut','ismail','ishaq','yaqub','yusuf','ayyub','shuayb','musa','harun','dhul-kifl','dawud','sulayman','ilyas','alyasa','yunus','zakariyya','yahya','isa','muhammad'}
assert {p['id'] for p in people if p['category']=='Prophets'}==expected
for p in people:
 assert p['uncertainty'] and p['chapters'] and p['sources'],p['id']
 if p['era']=='Qur’anic accounts':assert p['year'] is None and p['coordinates'] is None
 for field in ['dateEvidence','placeEvidence']:
  if field in p:
   e=p[field];assert e['status'] and e['text'] and e['sources']
   assert all(isinstance(i,int) and 0<=i<len(p['sources']) for i in e['sources'])
 for s in p['sources']:assert urlparse(s['url']).scheme=='https' and s['title']
 for c in p['chapters']:
  assert c['text'] and c['sources']
  assert all(isinstance(i,int) and 0<=i<len(p['sources']) for i in c['sources'])
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
print(f'PASS: {len(mentions)} name-index records and source location integrity. Source omissions and unnamed mentions still require a separate audit.')
