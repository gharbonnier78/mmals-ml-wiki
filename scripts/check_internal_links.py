#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, sys
ROOT=Path(__file__).resolve().parents[1]
class Parser(HTMLParser):
    def __init__(self): super().__init__(); self.refs=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        for key in ('href','src'):
            if key in d:self.refs.append((tag,key,d[key]))

def resolve(src,ref):
    ref=unquote(ref.split('#')[0].split('?')[0])
    if not ref:return None
    if ref.startswith(('http://','https://','mailto:','tel:','data:','javascript:')):return None
    if ref.startswith('/'):
        # Project Pages are hosted below /mmals-ml-wiki; root absolute links are forbidden.
        return Path('__ABSOLUTE_PATH_FORBIDDEN__')
    p=(src.parent/ref).resolve()
    if p.is_dir():p=p/'index.html'
    return p
errors=[];checked=0
for f in ROOT.rglob('*.html'):
    p=Parser();p.feed(f.read_text(encoding='utf-8'))
    for _,_,ref in p.refs:
        target=resolve(f,ref)
        if target is None:continue
        checked+=1
        if target.name=='__ABSOLUTE_PATH_FORBIDDEN__' or not target.exists():errors.append((f.relative_to(ROOT),ref))
# Validate redirects target records
rfile=ROOT/'data/redirects.json'
if rfile.exists():
    data=json.loads(rfile.read_text())
    for slug in data:
        checked+=1
        if not (ROOT/'go'/slug/'index.html').exists():errors.append((rfile.relative_to(ROOT),f'missing go/{slug}'))
print(f'Internal links checked: {checked}')
if errors:
    for src,ref in errors:print(f'BROKEN {src}: {ref}')
    sys.exit(1)
print('All internal links are healthy.')
