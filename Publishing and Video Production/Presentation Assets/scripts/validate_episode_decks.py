"""Validate the actual OOXML files and update the delivery manifest."""
from pathlib import Path
import json, zipfile, re, hashlib
from lxml import etree
A=Path(__file__).resolve().parents[1]
p=A/'episode-manifest.json'; m=json.loads(p.read_text(encoding='utf-8'))
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
issues=[]
for e in m['episodes']:
 f=A/e['path']; local=[]
 with zipfile.ZipFile(f) as z:
  damaged=z.testzip()
  if damaged:local.append('Bad ZIP member: '+damaged)
  slides=sorted([n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)],key=lambda x:int(re.search(r'(\d+)\.xml',x)[1]))
  notes=[n for n in z.namelist() if re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml',n)]
  media=[n for n in z.namelist() if n.startswith('ppt/media/') and not n.endswith('/')]
  if len(slides)!=e['slides']:local.append('Slide count mismatch')
  if len(notes)!=len(slides):local.append('Missing speaker notes')
  for i,n in enumerate(slides,1):
   tree=etree.fromstring(z.read(n)); text=' '.join(tree.xpath('//a:t/text()',namespaces=ns))
   if re.search(r'\\(?:frac|text|begin|end|sum|times)|\\\[|\\\]',text):local.append(f'Raw TeX on slide {i}')
   if '\ufffd' in text:local.append(f'Unicode replacement character on slide {i}')
   if not text.strip():local.append(f'Empty slide {i}')
   if i==len(slides) and len(text)<250:local.append('Sparse source slide')
  if not media:local.append('No evidence images embedded')
 e['sha256']=hashlib.sha256(f.read_bytes()).hexdigest();e['bytes']=f.stat().st_size
 e['qa'].update(structural='passed' if not local else 'failed',zip_integrity=not damaged,slide_count=len(slides),notes_count=len(notes),media_count=len(media),raw_tex_on_slide=False if not any('Raw TeX' in s for s in local) else True,issues=local)
 issues.extend({'article_id':e['article_id'],'issue':x} for x in local)
m['deck_count']=len(m['episodes']);m['total_slides']=sum(e['slides'] for e in m['episodes']);m['qa_summary']={'structural_pass':not issues,'issues':issues,'total_bytes':sum(e['bytes'] for e in m['episodes'])}
p.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'decks':m['deck_count'],'slides':m['total_slides'],'issues':issues,'total_MB':round(m['qa_summary']['total_bytes']/1e6,2)},ensure_ascii=False))
