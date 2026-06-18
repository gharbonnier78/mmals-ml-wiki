#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import argparse,json,datetime,time
ROOT=Path(__file__).resolve().parents[1]
class P(HTMLParser):
    def __init__(self):super().__init__();self.urls=[]
    def handle_starttag(self,t,a):
        d=dict(a)
        for k in ('href','src'):
            u=d.get(k,'')
            if u.startswith(('http://','https://')):self.urls.append(u)
def check(url):
    headers={'User-Agent':'Diderot-Link-Checker/0.1'}
    for method in ('HEAD','GET'):
        try:
            req=Request(url,headers=headers,method=method)
            with urlopen(req,timeout=15) as r:return True,str(r.status)
        except HTTPError as e:
            if e.code in (405,403) and method=='HEAD':continue
            return e.code<500,str(e.code)
        except Exception as e:
            if method=='HEAD':continue
            return False,type(e).__name__
    return False,'unknown'
ap=argparse.ArgumentParser();ap.add_argument('--output',default='data/link-health.json');args=ap.parse_args()
urls=set()
for f in ROOT.rglob('*.html'):
    p=P();p.feed(f.read_text(encoding='utf-8'));urls.update(p.urls)
rows=[]
for u in sorted(urls):
    ok,status=check(u);rows.append({'url':u,'ok':ok,'status':status,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()});time.sleep(.15)
internal_checked=0
try:
    import subprocess
    q=subprocess.run(['python',str(ROOT/'scripts/check_internal_links.py')],capture_output=True,text=True)
    import re
    m=re.search(r'Internal links checked: (\d+)',q.stdout);internal_checked=int(m.group(1)) if m else 0
    internal_broken=0 if q.returncode==0 else 1
except Exception:internal_broken=1
summary={'internal_checked':internal_checked,'internal_ok':internal_checked if internal_broken==0 else 0,'internal_broken':internal_broken,'external_checked':len(rows),'external_ok':sum(x['ok'] for x in rows),'external_warning':sum(not x['ok'] for x in rows),'external_broken':0}
out=ROOT/args.output;out.write_text(json.dumps({'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'network-refresh','summary':summary,'notes':'External failures are warnings until reviewed; internal failures block CI.','links':rows},indent=2),encoding='utf-8')
print(f'Wrote {out} with {len(rows)} external checks.')
