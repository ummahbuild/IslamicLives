"""Fail when generated HTML points at a missing local static asset or page."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT=Path(__file__).resolve().parents[1]/'public'

class Links(HTMLParser):
 def __init__(self): super().__init__(); self.values=[]
 def handle_starttag(self,tag,attrs):
  fields={'a':'href','link':'href','script':'src','img':'src'}
  wanted=fields.get(tag)
  if wanted:
   value=dict(attrs).get(wanted)
   if value:self.values.append(value)

def target_for(url):
 parsed=urlsplit(url)
 if parsed.scheme or parsed.netloc or url.startswith('//'): return None
 path=parsed.path
 if not path.startswith('/'): return None
 target=ROOT/path.lstrip('/')
 if path.endswith('/'): target=target/'index.html'
 return target

errors=[]; checked=0
for page in ROOT.rglob('*.html'):
 parser=Links();parser.feed(page.read_text())
 for url in parser.values:
  target=target_for(url)
  if target is None: continue
  checked+=1
  if not target.exists(): errors.append(f'{page.relative_to(ROOT)} -> {url}')
if errors: raise SystemExit('Missing internal targets:\n'+'\n'.join(errors))
print(f'PASS: {checked} internal HTML links and assets resolve')
