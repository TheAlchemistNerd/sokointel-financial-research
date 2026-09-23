from pathlib import Path
from PIL import Image, ImageDraw
root=Path(r"C:\Users\Nevo\Downloads\financial material\NSE Dividend Growth Project 2026\qa")
for source, prefix in [(root/"part-one-pdf","part-one"),(root/"part-two-pdf","part-two")]:
    pages=sorted(source.glob("page-*.png"))
    for start in range(0,len(pages),4):
        batch=pages[start:start+4]
        thumbs=[]
        for p in batch:
            im=Image.open(p).convert("RGB")
            im.thumbnail((700,900))
            thumbs.append((p.name,im.copy()))
        canvas=Image.new("RGB",(1460,1900),"#e8eddf")
        draw=ImageDraw.Draw(canvas)
        for i,(name,im) in enumerate(thumbs):
            x=20+(i%2)*720;y=30+(i//2)*940
            canvas.paste(im,(x,y+22))
            draw.text((x,y),name,fill="#173d33")
        canvas.save(root/f"{prefix}-contact-{start//4+1}.png")
