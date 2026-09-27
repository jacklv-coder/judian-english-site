#!/usr/bin/env python3
"""Check deployable local links and consumer-facing release placeholders."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
ROOT=Path(__file__).resolve().parent
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  self.links += [v for k,v in attrs if k in ('href','src') and v]
errors=[]
for page in ROOT.rglob('*.html'):
 parser=Links();source=page.read_text();parser.feed(source)
 for link in parser.links:
  u=urlsplit(link)
  if u.scheme or not u.path:continue
  target=(page.parent/unquote(u.path)).resolve()
  if not target.is_relative_to(ROOT):errors.append(f'{page}: link escapes site: {link}')
  elif not target.exists():errors.append(f'{page}: missing {link}')
 if 'TODO' in source or 'example.com' in source:errors.append(f'{page}: unresolved placeholder')
for item in errors:print(item)
if errors:raise SystemExit(1)
print('All site page links and assets resolve.')
