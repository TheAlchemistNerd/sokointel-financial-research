"""Join structural/native QA and create the human and CSV episode inventory."""
from pathlib import Path
import json,csv
A=Path(__file__).resolve().parents[1]
p=A/'episode-manifest.json';m=json.loads(p.read_text(encoding='utf-8'))
qa=A/'Review/native-qa.json'
native={x['article_id']:x for x in json.loads(qa.read_text(encoding='utf-8-sig'))} if qa.exists() else {}
rows=[]
for e in m['episodes']:
 q=native.get(e['article_id'])
 if q:
  e['qa']['native_open']='passed';e['qa']['native_text_bounds']='passed' if not q['issues'] else 'review_needed';e['qa']['native_issues']=q['issues']
  if not q['issues'] and e['qa']['structural']=='passed':e['status']='editable_pptx_validated'
 renders=A/'Review/Native'/e['article_id']
 e['qa']['native_render_available']=renders.exists()
 e['qa']['visual']='representative native render available; see review record' if renders.exists() else 'native open and text-bound validation; not individually image-reviewed'
 workbook='; '.join("'"+x['sheet']+"'!"+x['range'] for x in e['workbook_sources'])
 web=[x for x in e['screenshots'] if 'url' in x]
 rows.append({'article_id':e['article_id'],'series_id':e['series_id'],'title':e['title'],'slides':e['slides'],'deck_path':e['path'],'article_url':e['article_url'],'workbook_ranges':workbook,'web_tools':'; '.join(x['url'] for x in web),'native_qa':e['qa'].get('native_text_bounds','pending'),'recording_status':e['recording_status'],'publishing_status':e['publishing_status']})
m['known_issues']=[
 {'id':'DCA-PERCENT-FORMATTING','scope':'Inherited single-asset DCA saved page','detail':'Captured page displays 0.01% for net income 1,015.5093 on cash 100,000. Correct yield is 1.0155093%, rounded 1.02%. Deck uses an exact calculation-table crop excluding the incorrect card, and visibly states the correction. Protected calculator unchanged.'},
 {'id':'BAT-OCF-RECONCILIATION','scope':'BAT FY2025 Part 6 vs Part 10/workbook line','detail':'Part 6 operating cash KES 6,633.154m differs from the casebook KES 6,642m. Valuation briefs do not use this disputed figure. Replacement OE-VALUATION-06 capture shows only net revenue C11:F11; historical captures are preserved.'},
 {'id':'ARTICLE-IMPORT','scope':'Canonical public article links','detail':'Canonical links are content identifiers. Some new article pages may return 404 until the catalog is imported/deployed; deck generation does not publish articles.'},
 {'id':'LOCAL-WEB-EVIDENCE','scope':'New formula-rendering captures','detail':'Owner earnings, 13-week cash, failure-warning, detailed credit and updated DCF captures show the local preview; they are not evidence of live deployment.'}
]
m['qa_summary']['native_open_count']=len(native);m['qa_summary']['native_text_bound_pass_count']=sum(not x['issues'] for x in native.values())
p.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
with (A/'Master Index.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
lines=['# Episode PowerPoint delivery index','',f"Delivered: **{m['deck_count']} editable decks, {m['total_slides']} slides, 11 research series**. Each episode has its own file, recording notes, dated source context and workbook evidence. Videos remain unrecorded and unpublished.",'','See [production and rebuild notes](README.md) and [machine-readable manifest](episode-manifest.json). The manifest records full source URLs, input values, exact workbook paths/ranges, hashes, evidence paths and QA status.','', '| Episode | PowerPoint | Slides | Workbook evidence | Web demonstration | Native QA |','|---|---|---:|---|---|---|']
for r in rows:
 tool='; '.join(x['title'] for x in next(e for e in m['episodes'] if e['article_id']==r['article_id'])['slide_plan'] if x['type']=='web-evidence') or 'Not applicable'
 lines.append(f"| {r['article_id']} | [{r['title']}](<{r['deck_path']}>) | {r['slides']} | {r['workbook_ranges']} | {tool} | {r['native_qa']} |")
lines+=['','## Evidence and release boundaries','','- Workbook images are crops of actual Excel read-only PDF exports, with row/column headings and source hashes. IIDF and leadership cross-series teaching bridges are labelled explicitly.','- The new calculator screenshots are labelled local preview; older saved production captures retain their original dates.','- The single-asset DCA percentage card has an inherited formatting error. The deck excludes that card, shows the correct 1.02% calculation, and preserves the untouched original capture.','- BAT operating-cash source-line reconciliation remains open. The Part 6 replacement evidence crop deliberately excludes that disputed measure.','- Some new article URLs may remain unavailable until the separate catalog import is deployed. No YouTube URL or publication status was invented.','']
(A/'Master Index.md').write_text('\n'.join(lines),encoding='utf-8')
print(f"Index updated for {len(rows)} decks; native reports: {len(native)}.")
