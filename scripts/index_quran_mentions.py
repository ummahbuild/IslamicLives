"""Fetch source-labelled Quranic name references; no source prose is republished.
Follows discovered pagination and requires source counts to reconcile before output.
"""
import hashlib, html, json, re, subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs
ROOT=Path(__file__).resolve().parents[1]
BASE='https://corpus.quran.com/'
def fetch(url):
 if urlparse(url).netloc!='corpus.quran.com':raise ValueError('Unexpected source host')
 return subprocess.run(['curl','--fail','--silent','--show-error','--location','--max-time','30',url],check=True,capture_output=True,text=True).stdout

def parse_page(body,compound=False):
 count=re.search(r'Results\s*<b>(\d+)</b>\s*to\s*<b>(\d+)</b>\s*of\s*<b>(\d+)</b>',body)
 if not count:raise ValueError('Missing source result count')
 refs=re.findall(r'href="wordmorphology\.jsp\?location=\((\d+:\d+:\d+)\)"',body)
 start,end,total=map(int,count.groups())
 matches=len(refs)
 if compound:
  matches=sum(i==0 or ':'.join(refs[i-1].split(':')[:2])!=':'.join(ref.split(':')[:2]) or int(ref.split(':')[2])!=int(refs[i-1].split(':')[2])+1 for i,ref in enumerate(refs))
 if matches!=end-start+1:raise ValueError(f'Incomplete parsed page: {matches} matches vs {end-start+1}')
 links=[html.unescape(x) for x in re.findall(r'href="([^"]+)"',body) if 'page=' in x and 'q=con' in x]
 return total,refs,links

def collect(pair):
 pid,concept=pair
 first=urljoin(BASE,'search.jsp?q=con:'+concept)
 queue=[first];seen=set();refs=set();total=None;proof=[];matched=0
 while queue:
  url=queue.pop(0)
  # Page 1 has two equivalent URL forms, and subsequent navigation repeats pages.
  params=parse_qs(urlparse(url).query)
  key=params.get('page',['1'])[0]
  if key in seen:continue
  seen.add(key);body=fetch(url)
  try:n,found,links=parse_page(body,concept in ['dhul-kifl','abu-lahab','dhul-qarnayn'])
  except ValueError as e:raise ValueError(f'{url}: {e}') from e
  if total is not None and total!=n:raise ValueError('Changing source count')
  total=n;refs.update(found)
  count=re.search(r'Results\s*<b>(\d+)</b>\s*to\s*<b>(\d+)</b>',body)
  matched+=int(count.group(2))-int(count.group(1))+1
  proof.append({'url':url,'sha256':hashlib.sha256(body.encode()).hexdigest(),'parsedLocations':len(found)})
  queue.extend(urljoin(first,l) for l in links)
 if matched!=total:raise ValueError(f'{pid}: {matched} parsed vs {total} source matches')
 refs=sorted(refs,key=lambda s:tuple(map(int,s.split(':'))))
 return {'personId':pid,'concept':concept,'source':first,'retrieved':str(date.today()),'kind':'Source concept-tagged word locations','sourceCount':total,'tokenCount':len(refs),'wordLocations':refs,'verses':sorted({':'.join(x.split(':')[:2]) for x in refs},key=lambda s:tuple(map(int,s.split(':')))),'pages':proof}

def main():
 people=json.loads((ROOT/'public/data/people.json').read_text())['people']
 topics=fetch(BASE+'topics.jsp')
 available=set(re.findall(r'/concept.jsp\?id=([^"&]+)',topics))
 aliases={'dawud':'david','sulayman':'solomon','ilyas':'elijah','alyasa':'elisha','ishaq':'isaac','ismail':'ishmael','isa':'jesus','zakariyya':'zechariah','uzayr':'uzair'}
 targets=[(p['id'],aliases.get(p['id'],p['id'])) for p in people if (p['category'] in ['Prophets','Qur’anic people'] or p['id']=='zayd') and aliases.get(p['id'],p['id']) in available]
 results=list(ThreadPoolExecutor(max_workers=3).map(collect,targets))
 results.sort(key=lambda e:e['personId'])
 output={'source':'Quranic Arabic Corpus, Kais Dukes / University of Leeds, maintained by Quran.com','sourceUrl':BASE,'scope':'References returned by the selected source concept queries. This is not a complete index of all narrative mentions, pronouns, unnamed people, aliases or titles.','attribution':'See /data/MENTIONS-NOTICE.txt','entries':results}
 (ROOT/'public/data/quran-mentions.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
 print(f'Indexed {len(results)} people, {sum(e["tokenCount"] for e in results)} word locations; all source counts reconciled.')
if __name__=='__main__':main()
