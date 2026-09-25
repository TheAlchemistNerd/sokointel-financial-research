from pathlib import Path
import json
import pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import Image,ImageChops
A=Path(__file__).resolve().parents[1]
# Crop without retouching: retain the calculation table and exclude a known percentage-formatting card.
f=A/'Evidence/Web/dca-dividend-summary.png'; im=Image.open(f)
im.crop((0,300,860,815)).save(A/'Evidence/Web/dca-dividend-table-crop.png')
bm=A/'Evidence/Workbooks/bat-capture-manifest.json'
if bm.exists():
 e=json.loads(bm.read_text(encoding='utf-8-sig')); pdf=A/'Evidence/Workbooks/OE-VALUATION-06-BAT.pdf'
 doc=pdfium.PdfDocument(str(pdf));im=doc[0].render(scale=2.1).to_pil().convert('RGB')
 box=ImageChops.difference(im,Image.new('RGB',im.size,'white')).convert('L').point(lambda x:255 if x>22 else 0).getbbox()
 im=im.crop((max(0,box[0]-12),max(0,box[1]-12),min(im.width,box[2]+12),min(im.height,box[3]+12)))
 dest=A/'Evidence/Workbooks/OE-VALUATION-06-BAT-p1.png';im.save(dest,optimize=True)
 e['images']=[str(dest.relative_to(A)).replace('\\','/')];e['pdf']=str(pdf.relative_to(A)).replace('\\','/');e['pdf_text']='\n'.join(p.extract_text() or '' for p in PdfReader(str(pdf)).pages)
 src=A/'content/source-material.json'; data=json.loads(src.read_text(encoding='utf-8')); a=next(a for a in data['articles'] if a['id']==e['episode']);a['evidence']=[e]+[x for x in a['evidence'] if x['asset_id'] not in ('OE-VALUATION-06-01','OE-VALUATION-06-BAT')];src.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('Saved exact-source table crop and BAT evidence metadata.')
