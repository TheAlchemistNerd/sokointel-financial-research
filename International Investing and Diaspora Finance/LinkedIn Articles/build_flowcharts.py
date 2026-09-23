from pathlib import Path
import re
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
OUT = ROOT/'Flowcharts'
OUT.mkdir(exist_ok=True)
FONT = 'C:/Windows/Fonts/segoeui.ttf'
BOLD = 'C:/Windows/Fonts/segoeuib.ttf'

def chart(name, title, subtitle, nodes, edges, height, width=1200):
    im = Image.new('RGB',(width,height),'#f5f7fa')
    d = ImageDraw.Draw(im)
    d.rectangle((0,0,width,12),fill='#147d86')
    d.text((48,40),title,font=ImageFont.truetype(BOLD,36),fill='#142e45')
    d.text((48,100),subtitle,font=ImageFont.truetype(FONT,21),fill='#536578')
    font = ImageFont.truetype(FONT,25)
    def lines(text,w):
        out=[]
        for line in text.split('\n'):
            cur=''
            for word in line.split():
                trial=(cur+' '+word).strip()
                if d.textlength(trial,font=font)>w:
                    out.append(cur); cur=word
                else: cur=trial
            out.append(cur)
        return out
    boxes={}
    for key,text,x,y,w in nodes:
        ls=lines(text,w-38)
        h=max(88,len(ls)*33+34)
        boxes[key]=(x,y,w,h,ls)
    for src,dst,label in edges:
        x,y,w,h,_=boxes[src]; xx,yy,ww,hh,_=boxes[dst]
        start=(x+w/2,y+h); end=(xx+ww/2,yy)
        mid=(start[1]+end[1])/2
        pts=[start,(start[0],mid),(end[0],mid),end]
        d.line(pts,fill='#668092',width=4)
        d.polygon([(end[0]-7,end[1]-12),(end[0]+7,end[1]-12),end],fill='#668092')
        if label:
            f=ImageFont.truetype(BOLD,20)
            tx=(start[0]+end[0])/2
            tw=d.textlength(label,font=f)
            d.rectangle((tx-tw/2-7,mid-14,tx+tw/2+7,mid+13),fill='#f5f7fa')
            d.text((tx-tw/2,mid-14),label,font=f,fill='#147d86')
    for key,(x,y,w,h,ls) in boxes.items():
        d.rounded_rectangle((x,y,x+w,y+h),radius=13,fill='white',outline='#b7cbd5',width=2)
        d.rounded_rectangle((x,y,x+7,y+h),radius=3,fill='#147d86')
        for i,line in enumerate(ls):
            tw=d.textlength(line,font=font)
            d.text((x+(w-tw)/2,y+17+i*33),line,font=font,fill='#142e45')
        assert y+h < height-65, (name,key,y+h,height)
    d.text((48,height-43),'INTERNATIONAL INVESTING & DIASPORA FINANCE  |  SEPTEMBER 2026',font=ImageFont.truetype(FONT,16),fill='#536578')
    im.save(OUT/f'{name}.png')
    return im

charts=[]
charts.append(chart('01-dividend-path','Follow the dividend','Illustrative ordinary US equity income; investor and treaty assumptions matter.',[
('a','US company dividend',390,180,420),
('b','US fund held by illustrative Kenya-resident investor',65,365,480),
('c','Eligible Irish fund holds US shares',655,365,480),
('d','Ordinary dividend to investor:\nassumed 30% US withholding',65,570,480),
('e','Dividend received inside fund:\ncommonly 15% US withholding',655,570,480),
('f','Net income retained or distributed by share class',655,775,480),
('g','Assess investor residence rules and available relief',330,990,540)],
[('a','b','US route'),('a','c','Irish route'),('b','d',''),('c','e',''),('e','f',''),('d','g',''),('f','g','')],1200))

def linear(name,title,subtitle,labels):
    nodes=[(str(i),text,270,180+i*165,660) for i,text in enumerate(labels)]
    return chart(name,title,subtitle,nodes,[(str(i),str(i+1),'') for i in range(len(labels)-1)],180+len(labels)*165+40)

charts.append(linear('02-investment-decision','Choose the investment in sequence','Revisit earlier choices whenever tax, access, or household needs change.',[
'Define goal, horizon, and spending currency','Choose underlying asset exposure','Identify ISIN, domicile, share class, and trading line','Assess investor tax status and reporting','Confirm suitability and access; revise exposure if needed','Compare funding, FX, fund, and dealing costs','Buy under a written allocation plan','Review when goals, residence, or allocation change']))
charts.append(chart('03-residence-analysis','Establish the tax position','Domestic residence comes first; treaty analysis follows where relevant.',[
('a','Record homes, work, travel days, and relevant status',270,180,660),
('b',"Apply each country's domestic residence tests",270,360,660),
('c','More than one domestic residence?',340,540,520),
('d','Check applicable treaty and individual tie-breakers',65,735,480),
('e','Establish relevant domestic tax scope',655,735,480),
('f','Classify dividends, gains, salary, interest, and capital',270,950,660),
('g','Apply exemptions, credits, and reporting rules',270,1130,660),
('h','Document the conclusion; review when facts change',270,1310,660)],
[('a','b',''),('b','c',''),('c','d','Yes'),('c','e','No'),('d','f','Then assess scope'),('e','f',''),('f','g',''),('g','h','')],1500))
charts.append(linear('04-relocation-review','Review before relocating','Build the plan around dated facts and the actual accounts involved.',[
'Identify proposed move or change in work pattern','Build a residence and transaction timeline','Inventory funds, wrappers, costs, and prior income adjustments','Compare holding, selling, or transferring under applicable rules','Plan tax cash needs and reporting documents','Update providers with accurate residence information','Recheck actual facts after arrival and at year end']))
charts.append(chart('05-money-routes','Give each transfer a purpose','Every arrow requires a supported route for the actual account and currency.',[
('a','Income in actual country and currency',330,180,540),
('b','Reserve essential spending and family support',270,355,660),
('c','Investment contribution',65,540,510),
('d','Family support',680,540,450),
('e','Confirm broker entity, permissions, and deposit instructions',65,710,510),
('f','Compare recipient amount and arrival terms',680,710,450),
('g','Use supported own-name bank route OR eligible Wise integration',65,940,510),
('h','Kenyan bank or supported M-Pesa delivery',680,940,450),
('i','Compare full cost; confirm cash credited and available',65,1170,510),
('j','Reconcile amount received',680,1170,450)],
[('a','b',''),('b','c','Invest'),('b','d','Support'),('c','e',''),('d','f',''),('e','g',''),('f','h',''),('g','i',''),('h','j','')],1390))
charts.append(linear('06-withdrawal-sequence','Plan the withdrawal before the bill','Cash availability, tax records, and delivery are separate stages.',[
'Identify the planned household withdrawal','Review tax position and available reserve','Sell the appropriate holding if needed','Confirm cash availability and withdrawal conditions','Compare necessary FX conversion and transfer','Withdraw through a supported account route','Deliver to the intended household account','Reconcile proceeds, costs, tax, and recipient amount','Update remaining portfolio and support plan']))

names=['01-dividend-path','02-investment-decision','03-residence-analysis','04-relocation-review','05-money-routes','06-withdrawal-sequence']
n=0
for path in sorted(ROOT.glob('Part *.md')):
    text=path.read_text(encoding='utf-8')
    def replacement(match):
        global n
        name=names[n]; n+=1
        (OUT/f'{name}.mmd').write_text(match.group(1).strip()+'\n',encoding='utf-8')
        target=(OUT/f'{name}.png').as_posix()
        return f'![Flowchart: {name[3:].replace("-"," ")}](<{target}>)'
    text=re.sub(r'```mermaid\n(.*?)```',replacement,text,flags=re.S)
    counter=[0]
    def number(match):
        counter[0]+=1
        return '### Worked calculation '+str(counter[0])+' —'
    text=re.sub(r'### Worked calculation \d+ —',number,text)
    path.write_text(text,encoding='utf-8')

contact=Image.new('RGB',(1200,1320),'#e2e8ee')
for i,im in enumerate(charts):
    copy=im.copy(); copy.thumbnail((390,640))
    contact.paste(copy,(i%3*400+(400-copy.width)//2,i//3*660))
contact.save(OUT/'contact-sheet.png')
print('Created six flowchart PNGs and embedded them; Mermaid sources retained.')
