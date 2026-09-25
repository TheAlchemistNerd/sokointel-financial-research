from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import re
A=Path(__file__).resolve().parents[1]
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',16)
for folder in (A/'Review/Native').glob('*'):
 files=sorted(folder.glob('*.PNG'),key=lambda x:int(re.search(r'(\d+)\.PNG',x.name,re.I)[1]))
 if not files:files=sorted(folder.glob('*.png'),key=lambda x:int(re.search(r'(\d+)\.png',x.name,re.I)[1]))
 if not files:continue
 out=Image.new('RGB',(1440,((len(files)+2)//3)*300),'#d9d9d9');dr=ImageDraw.Draw(out)
 for i,f in enumerate(files):
  x=(i%3)*480;y=(i//3)*300;im=Image.open(f);im.thumbnail((468,263));out.paste(im,(x+6,y+29));dr.text((x+6,y+5),folder.name+' • '+f.stem,font=font,fill='#163047')
 dest=folder.parent/(folder.name+'-contact-sheet.jpg');out.save(dest,quality=88);print(dest)
