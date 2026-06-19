#!/usr/bin/env python3
from pathlib import Path
from urllib.request import Request, urlopen
import json, os, datetime
ROOT=Path(__file__).resolve().parents[1]
OWNER='gharbonnier78'
url=f'https://api.github.com/users/{OWNER}/repos?per_page=100&sort=updated'
headers={'Accept':'application/vnd.github+json','User-Agent':'Diderot-Registry-Refresh/0.2'}
token=os.getenv('GITHUB_TOKEN')
if token: headers['Authorization']=f'Bearer {token}'
with urlopen(Request(url,headers=headers),timeout=30) as response:
    live=json.load(response)
curated=json.loads((ROOT/'data/repositories.json').read_text(encoding='utf-8'))
curated_public={r['id'] for r in curated if r.get('status')=='public'}
live_names={r['name'] for r in live}
rows=[{'name':r['name'],'html_url':r['html_url'],'description':r.get('description'),'language':r.get('language'),'updated_at':r.get('updated_at'),'archived':r.get('archived',False),'visibility':r.get('visibility','public')} for r in live]
out={'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'github-api-refresh','owner':OWNER,'public_repository_count':len(rows),'missing_from_live':sorted(curated_public-live_names),'unmapped_live':sorted(live_names-{r['id'] for r in curated}),'repositories':rows}
(ROOT/'data/github-live.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
print(f"Refreshed {len(rows)} public repositories; {len(out['missing_from_live'])} curated public records missing; {len(out['unmapped_live'])} live repositories unmapped.")
