from pathlib import Path
import json, math, re, shutil
import numpy as np

base=Path(__file__).resolve().parent
root=base.parent if base.name=='Research' else base.parent/'Kenyan Equities and Company Analysis'/'Four Part Series'
sources=json.loads((base/'sources.json').read_text(encoding='utf-8'))
if (base/'sources.json').resolve()!=(root/'Research'/'sources.json').resolve():shutil.copy(base/'sources.json',root/'Research'/'sources.json')
books=[]; book=None; sheet=None
def col(n):
    out=''
    while n:
        n,r=divmod(n-1,26); out=chr(65+r)+out
    return out
def start(name,title):
    global book
    book={'name':name,'title':title,'sheets':[],'dictionary':[]};books.append(book)
def tab(name,headers,notes='',widths=None):
    global sheet
    sheet={'name':name,'headers':headers,'notes':notes,'cells':{},'formats':{},'widths':widths or {},'charts':[]};book['sheets'].append(sheet);return sheet
def v(cell,x,fmt=None):
    sheet['cells'][cell]=x
    if fmt: sheet['formats'][cell]=fmt
def row(n,values):
    for i,x in enumerate(values):
        if x is not None:v(f'{col(i+1)}{n}',x)
def f(cell,formula,meaning='',maths='',units=''):
    v(cell,formula)
    if meaning:book['dictionary'].append([sheet['name'],cell,formula,meaning,maths,units])
def inputs(rows):
    tab('Inputs',['Input','Value','Units','Basis'],'Blue figures are editable assumptions. All unlabelled company models are fictional.',{'A':36,'D':80})
    for r,vals in enumerate(rows,7):row(r,vals)
def finish():
    d=book['dictionary']
    tab('Formula dictionary',['Sheet','Cell example','Excel formula','Definition','Mathematical equivalence','Units and scope'],'Each formula family is documented; copied rows follow the same rule.',{'A':24,'B':18,'C':70,'D':43,'E':67,'F':65})
    for i,x in enumerate(d,7):row(i,[x[0],x[1],"'"+x[2],*x[3:]])
    tab('Sources',['ID','Author or institution','Title','URL','Scope'],'Research checked 7 September 2026. Illustrative inputs are separate from published observations.',{'B':35,'C':60,'D':95,'E':95})
    for i,x in enumerate(sources,7):row(i,x)

start('01-Screening-and-Income','Kenyan equity screening and Treasury bills')
inputs([['Dividend withholding',.05,'fraction','Resident individual qualifying dividend teaching case [3].'],['Bill withholding',.15,'fraction','Interest withheld through purchase settlement [2].'],['All-in buy cost',.02,'fraction','Illustrative broker commission, levies and execution allowance; replace with quote.'],['Minimum net ordinary yield',.04,'fraction','Editable screening preference, not a quality guarantee.'],['Maximum payout',.85,'fraction','Research threshold; review reserves and sector context.'],['Days in pricing year',365,'days','CBK price reconciliation.'],['Minimum bill face',50000,'KES','Next auction in notice dated7Sep2026 [1].'],['Bill face increment',50000,'KES','Illustrative allocation increment; confirm auction instructions.'],['Dividend cut stress',.3,'fraction','Reduction in ordinary dividend; specials excluded.']])
directory=json.loads((root/'Research'/'issuer_directory.json').read_text())
tab('Issuer directory',['Ticker','Issuer','Directory sector','Trading status','Source URL'],'68 deduplicated directory records; includes fund/REIT and legacy entries. Confirm admission, suspension and delisting before screening.',{'B':55,'C':38,'D':56,'E':65})
for r,vals in enumerate(directory,7):row(r,vals)
seeds={'EQTY':[70,5.75,0,19.1,'2025-12-31',7],'KCB':[65,4,3,None,'2025-12-31',6],'COOP':[25,2.5,0,None,'2025-12-31',10],'BAT':[450,70,0,52.46,'2025-12-31',8],'JUB':[300,15,0,5781962/72473,'2025-12-31',9],'KEGN':[9,.9,0,None,'2025-06-30',11],'SCOM':[35,2,0,None,'2026-03-31',12]}
tab('Market screen',['Ticker','Sector','Illustrative price KES','Ordinary DPS KES','Special DPS KES','EPS KES','Fiscal year end','Data source URL','Gross ordinary yield','Net yield on cost','All distributions yield','Payout ratio','Stressed net yield','Research result'], 'Seven dated dividend examples. Prices are illustrative, not market quotes. Blank financials need source extraction; specials excluded from recurring income.',{'B':32,'H':85,'N':35})
for r,d in enumerate(directory,7):
    ticker=d[0]; seed=seeds.get(ticker)
    row(r,[ticker,d[2]])
    if seed:
        price,dps,special,eps,period,src=seed;row(r,[ticker,d[2],price,dps,special,eps,period,sources[src-1][3]])
    for cell,formula,meaning,eq in [
      ('I',f'=IF(OR(C{r}="",D{r}="",C{r}<=0),"",D{r}/C{r})','Ordinary dividend yield','y = D / P'),
      ('J',f'=IF(I{r}="","",I{r}*(1-\'Inputs\'!$B$7)/(1+\'Inputs\'!$B$9))','After-tax ordinary yield on acquisition outlay','y_net = D(1−t) / [P(1+c)]'),
      ('K',f'=IF(OR(I{r}="",E{r}=""),"",(D{r}+E{r})/C{r})','Gross declared distributions yield','y_all = (ordinary + special) / P'),
      ('L',f'=IF(OR(D{r}="",F{r}="",F{r}<=0),"",D{r}/F{r})','Ordinary payout; blank when earnings nonpositive or absent','payout = D / EPS'),
      ('M',f'=IF(J{r}="","",J{r}*(1-\'Inputs\'!$B$15))','Dividend cut sensitivity','y_stress = y_net (1−cut)'),
      ('N',f'=IF(J{r}="","Needs dividend and price",IF(L{r}="","Needs earnings review",IF(AND(J{r}>=\'Inputs\'!$B$10,L{r}<=\'Inputs\'!$B$11),"Meets income filters","Review yield or payout")))','Editable filter outcome; not an investment instruction','screen = yield≥threshold AND payout≤threshold')]:
        f(f'{cell}{r}',formula,meaning if r==7 else '',eq,'Sector analysis and trading eligibility remain separate.')
    for c in 'IJKLM':sheet['formats'][f'{c}{r}']='0.00%'
tab('Bill pricing',['Tenor days','Accepted annual yield','Face KES','Clean price','Gross discount','Tax at purchase','Settlement outlay','Maturity net gain','Holding-period return','Effective annual return','Published price /100','Price residual'], 'Official auction dated7Sep2026. Tax is added to clean purchase price; maturity pays face. Effective annual return assumes identical reinvestment terms.',{'A':18})
for r,(days,y,pr) in enumerate([(91,.087687,97.8606),(182,.089331,95.7356),(364,.090737,91.7020)],7):
    row(r,[days,y,100000,None,None,None,None,None,None,None,pr])
    formulas={'D':(f'=C{r}/(1+B{r}*A{r}/\'Inputs\'!$B$12)','Clean bill price','P=F/(1+yd/365)'), 'E':(f'=C{r}-D{r}','Gross discount','I=F−P'), 'F':(f'=E{r}*\'Inputs\'!$B$8','Withholding added at purchase','T=tI'),'G':(f'=D{r}+F{r}','Settlement cash','S=P+T'),'H':(f'=C{r}-G{r}','Net gain','G=F−S'),'I':(f'=H{r}/G{r}','Return on settlement outlay','h=G/S'),'J':(f'=(C{r}/G{r})^(\'Inputs\'!$B$12/A{r})-1','Effective annualised return','a=(F/S)^(365/d)−1'),'L':(f'=D{r}/C{r}*100-K{r}','Published clean-price reconciliation','residual=100P/F−published price')}
    for c,(form,definition,eq) in formulas.items():f(f'{c}{r}',form,definition if r==7 else '',eq,'KES except returns; residual can reflect published rounding.')
    for c in ['B','I','J']:sheet['formats'][f'{c}{r}']='0.0000%'
tab('Rollover',['Cycle','Days','Gross annual yield','Opening cash','Cash per face unit','Face bought','Residual cash','Maturity cash','Closing wealth'], 'Four consecutive91-day periods; no settlement gap. Tax at purchase. Whole face allocations retain residual cash at zero return.')
for r in range(7,11):
    row(r,[r-6,91,[.087687,.08,.07,.065][r-7]])
    f(f'D{r}','=1000000' if r==7 else f'=I{r-1}','Opening funds' if r==7 else '', 'W_open=W_prior; initial capital=KES1m','KES')
    for c,form,definition,eq in [('E',f'=(1/(1+C{r}*B{r}/365))+(1-1/(1+C{r}*B{r}/365))*\'Inputs\'!$B$8','Settlement per face unit','s=p+(1−p)t'),('F',f'=INT(D{r}/E{r}/\'Inputs\'!$B$14)*\'Inputs\'!$B$14','Affordable face','F=floor(W/s/increment)increment'),('G',f'=D{r}-F{r}*E{r}','Uninvested balance','cash=W−Fs'),('H',f'=F{r}','Face paid at maturity','maturity=F'),('I',f'=G{r}+H{r}','Closing wealth','W_next=cash+face')]:f(f'{c}{r}',form,definition if r==7 else '',eq,'KES; reinvestment yield editable each cycle.')
    sheet['formats'][f'C{r}']='0.00%'
tab('Income scenarios',['Case','Price KES','Ordinary DPS','Special DPS','Tax','Buy cost','Net recurring yield','Net first-year distributions','Price after one year','Total net return'], 'Fictional counter. Total return includes sale cost assumed equal to buy cost; dividends paid in cash without reinvestment.')
for r,vals in enumerate([['Base',40,3,0,.05,.02,None,None,44],['Dividend cut',40,2.1,0,.05,.02,None,None,32],['Special payout',40,3,2,.05,.02,None,None,39],['Higher entry price',50,3,0,.05,.02,None,None,44]],7):
    row(r,vals)
    for c,form,definition,eq in [('G',f'=C{r}*(1-E{r})/(B{r}*(1+F{r}))','Recurring net yield','D(1−t)/[P0(1+c)]'),('H',f'=(C{r}+D{r})*(1-E{r})','Cash distributions','cash=(D+special)(1−t)'),('J',f'=(I{r}*(1-F{r})+H{r}-B{r}*(1+F{r}))/(B{r}*(1+F{r}))','After-cost total return','R=[P1(1−c)+cash−P0(1+c)]/[P0(1+c)]')]:f(f'{c}{r}',form,definition if r==7 else '',eq,'Illustration; qualifying listed capital gains assumed exempt.')
    for c in ['E','F','G','J']:sheet['formats'][f'{c}{r}']='0.00%'
finish()

start('02-Statements-and-Valuation','Business quality and valuation')
inputs([['Opening revenue',10000,'KES million','Fictional manufacturer at31Dec2026.'],['Opening receivables',1200,'KES million','Trade only.'],['Opening inventory',1000,'KES million','Inventory carrying value.'],['Opening payables',900,'KES million','Trade only.'],['Opening plant',6000,'KES million','Net property plant equipment.'],['Opening cash',1200,'KES million','Unrestricted.'],['Opening debt',2500,'KES million','Interest-bearing debt; leases excluded in this teaching case.'],['Opening equity',6000,'KES million','Assets9400 less liabilities3400.'],['Shares',1000,'million shares','No dilution in base case.'],['WACC',.14,'fraction','NominalKES assumption.'],['Terminal growth',.04,'fraction','Steady-state assumption.'],['Terminal ROIC',.16,'fraction','Supports reinvestment g/ROIC.'],['Minority interests',0,'KES million','Fictional wholly-owned operations.'],['Nonoperating investments',0,'KES million','Add separately only when excluded from operating forecast.'],['Illustrative share price',6,'KES/share','Used for margin of safety.']])
tab('Annual drivers',['Driver','2027','2028','2029','2030','2031'],'Year-end cash flows; drivers are independently editable for every year. Fictional manufacturer.')
driver=[['Revenue growth',.06,.06,.05,.05,.04],['EBITDA margin',.22,.22,.23,.23,.23],['Depreciation / opening plant',.1,.1,.1,.1,.1],['Capital expenditure / revenue',.09,.09,.08,.08,.08],['Cash corporate tax',.3,.3,.3,.3,.3],['Receivables days',44,44,43,42,42],['Inventory days',60,59,58,58,57],['Payables days',50,50,50,50,50],['Cash cost of sales / revenue',.6,.6,.6,.6,.6],['Interest / opening debt',.12,.12,.11,.11,.1],['Debt principal repayment',250,250,250,250,250],['Dividend payout / net profit',.4,.4,.4,.4,.4]]
for r,a in enumerate(driver,7):row(r,a)
tab('Statements',['Line item','2026 opening','2027 forecast','2028 forecast','2029 forecast','2030 forecast','2031 forecast'],'Fictional integrated statements; no cash plug. Interest uses opening debt; year-end dividends and debt repayments.',{'A':39})
labels={7:'Revenue',8:'Cash cost of sales',9:'EBITDA',10:'Depreciation',11:'EBIT',12:'Interest expense',13:'Profit before tax',14:'Cash tax expense',15:'Net profit',17:'Receivables',18:'Inventory',19:'Trade payables',20:'Operating working capital',21:'Change in working capital',23:'Opening plant',24:'Capital expenditure',25:'Closing plant',27:'Opening debt',28:'Principal repayment',29:'Closing debt',31:'Opening equity',32:'Dividends',33:'Closing equity',35:'Opening cash',36:'Operating cash flow',37:'Investing cash flow',38:'Financing cash flow',39:'Closing cash',41:'Total assets',42:'Liabilities plus equity',43:'Balance sheet difference',45:'NOPAT',46:'Unlevered free cash flow',47:'EPS',48:'DPS'}
for r,label in labels.items():v(f'A{r}',label)
for r,ref in [(7,7),(17,8),(18,9),(19,10),(25,11),(39,12),(29,13),(33,14)]:f(f'B{r}',f"='Inputs'!B{ref}",f'Opening {labels[r]}',f'Opening value from Inputs B{ref}','KES million')
f('B20','=B17+B18-B19','Opening working capital','NWC=receivables+inventory−payables','KES million')
for j in range(3,8):
    c=col(j);p=col(j-1);a=col(j-1)
    forms={7:f'={p}7*(1+\'Annual drivers\'!{a}7)',8:f'={c}7*\'Annual drivers\'!{a}15',9:f'={c}7*\'Annual drivers\'!{a}8',10:f'={c}23*\'Annual drivers\'!{a}9',11:f'={c}9-{c}10',12:f'={c}27*\'Annual drivers\'!{a}16',13:f'={c}11-{c}12',14:f'=MAX(0,{c}13)*\'Annual drivers\'!{a}11',15:f'={c}13-{c}14',17:f'={c}7*\'Annual drivers\'!{a}12/365',18:f'={c}8*\'Annual drivers\'!{a}13/365',19:f'={c}8*\'Annual drivers\'!{a}14/365',20:f'={c}17+{c}18-{c}19',21:f'={c}20-{p}20',23:f'={p}25',24:f'={c}7*\'Annual drivers\'!{a}10',25:f'={c}23+{c}24-{c}10',27:f'={p}29',28:f'=MIN({c}27,\'Annual drivers\'!{a}17)',29:f'={c}27-{c}28',31:f'={p}33',32:f'=MAX(0,{c}15)*\'Annual drivers\'!{a}18',33:f'={c}31+{c}15-{c}32',35:f'={p}39',36:f'={c}15+{c}10-{c}21',37:f'=-{c}24',38:f'=-{c}28-{c}32',39:f'={c}35+{c}36+{c}37+{c}38',41:f'={c}17+{c}18+{c}25+{c}39',42:f'={c}19+{c}29+{c}33',43:f'={c}41-{c}42',45:f'={c}11*(1-\'Annual drivers\'!{a}11)',46:f'={c}45+{c}10-{c}24-{c}21',47:f'={c}15/\'Inputs\'!$B$15',48:f'={c}32/\'Inputs\'!$B$15'}
    eqs={7:'Revenue_t=Revenue_(t−1)(1+g_t)',8:'COGS=Revenue×cost ratio',9:'EBITDA=Revenue×margin',10:'D&A=opening plant×depreciation rate',11:'EBIT=EBITDA−D&A',12:'Interest=opening debt×rate',13:'PBT=EBIT−interest',14:'Tax=max(PBT,0)×tax rate; no loss carryforwards',15:'NI=PBT−tax',17:'AR=Revenue×DSO/365',18:'Inventory=COGS×DIO/365',19:'AP=COGS×DPO/365; COGS proxy for purchases',20:'NWC=AR+inventory−AP',21:'ΔNWC=NWC_t−NWC_(t−1)',23:'Opening plant=prior closing plant',24:'Capex=Revenue×capex fraction',25:'Plant_close=Plant_open+Capex−D&A',27:'Debt_open=prior Debt_close',28:'Repayment=min(opening debt,scheduled principal)',29:'Debt_close=Debt_open−repayment',31:'Equity_open=prior Equity_close',32:'Dividends=max(NI,0)×payout',33:'Equity_close=Equity_open+NI−dividends',35:'Cash_open=prior Cash_close',36:'CFO=NI+D&A−ΔNWC',37:'CFI=−Capex',38:'CFF=−repayment−dividends',39:'Cash_close=Cash_open+CFO+CFI+CFF',41:'Assets=AR+Inventory+Plant+Cash',42:'Liabilities+Equity=AP+Debt+Equity',43:'Check=Assets−Liabilities−Equity',45:'NOPAT=EBIT(1−tax rate)',46:'FCFF=NOPAT+D&A−Capex−ΔNWC',47:'EPS=NI/shares',48:'DPS=dividends/shares'}
    for r,form in forms.items():f(f'{c}{r}',form,labels[r] if j==3 else '',eqs[r],'KES million; EPS and DPS KES/share')
tab('DCF',['Measure','Value','Explanation'],'Year-end five-year forecast plus sustainable terminal reinvestment. Fictional company.',{'A':38,'C':85})
dcf=[('PV forecast cash flow',"=SUM('Statements'!C46/(1+'Inputs'!B16),'Statements'!D46/(1+'Inputs'!B16)^2,'Statements'!E46/(1+'Inputs'!B16)^3,'Statements'!F46/(1+'Inputs'!B16)^4,'Statements'!G46/(1+'Inputs'!B16)^5)",'PV_FCFF=Σ FCFF_t/(1+WACC)^t'),('Terminal NOPAT',"='Statements'!G45*(1+'Inputs'!B17)",'NOPAT_6=NOPAT_5(1+g)'),('Terminal reinvestment fraction',"='Inputs'!B17/'Inputs'!B18",'RR=g/ROIC'),('Terminal cash flow','=B8*(1-B9)','FCFF_6=NOPAT_6(1−g/ROIC)'),('Terminal enterprise value',"=IF('Inputs'!B16<='Inputs'!B17,\"Invalid WACC <= growth\",B10/('Inputs'!B16-'Inputs'!B17))",'TV_5=FCFF_6/(WACC−g)'),('PV terminal',"=IF(ISNUMBER(B11),B11/(1+'Inputs'!B16)^5,\"Check terminal inputs\")",'PV_TV=TV_5/(1+WACC)^5'),('Enterprise value','=IF(ISNUMBER(B12),B7+B12,"Check terminal inputs")','EV=PV_FCFF+PV_TV'),('Equity value',"=IF(ISNUMBER(B13),B13+'Inputs'!B12-'Inputs'!B13+'Inputs'!B20-'Inputs'!B19,\"Check terminal inputs\")",'Equity=EV+cash−debt+investments−minority interests'),('Value per share',"=IF(ISNUMBER(B14),B14/'Inputs'!B15,\"Check terminal inputs\")",'V=Equity/shares'),('Margin of safety',"=IF(ISNUMBER(B15),1-'Inputs'!B21/B15,\"Check terminal inputs\")",'MOS=1−price/value'),('Terminal share of EV','=IF(ISNUMBER(B13),B12/B13,"Check terminal inputs")','Terminal proportion=PV_TV/EV')]
for r,(label,form,eq) in enumerate(dcf,7):row(r,[label,None,eq]);f(f'B{r}',form,label,eq,'KES million except per-share and fractions')
tab('DCF sensitivity',['WACC / terminal growth',.02,.03,.04,.05,.06],'Each cell recomputes forecast PV and terminal reinvestment; nominalKES value/share. WACC must exceed growth.',{'A':28})
for r,w in enumerate([.10,.12,.14,.16,.18],7):
    v(f'A{r}',w,'0%')
    for j in range(2,7):
        c=col(j);g=f'{c}$6';rate=f'$A{r}'
        pv='+'.join(f"'Statements'!{col(k+2)}46/(1+{rate})^{k}" for k in range(1,6))
        f(f'{c}{r}',f'=IF({rate}<={g},"Invalid",(({pv})+\'Statements\'!G45*(1+{g})*(1-{g}/\'Inputs\'!$B$18)/({rate}-{g})/(1+{rate})^5+\'Inputs\'!$B$12-\'Inputs\'!$B$13+\'Inputs\'!$B$20-\'Inputs\'!$B$19)/\'Inputs\'!$B$15)','Value per share sensitivity' if r==7 and j==2 else '', 'V(w,g)=[ΣFCFF_t/(1+w)^t+NOPAT5(1+g)(1−g/ROIC)/(w−g)/(1+w)^5+cash−debt+investments−NCI]/shares','KES/share')
tab('Bank scenarios',['Case','Opening equity','ROE','Required return','Growth','Opening RWA','RWA growth','Capital requirement','Operating profit pre-loss','Loan-loss expense','Tax','Net profit','Required retained capital','Dividend capacity','Payout','Justified price/book','Equity value'],'Fictional bank, KES million. Equity proxy equals eligible capital for this teaching case; replace with regulatory reconciliation.',{'A':25})
for r,a in enumerate([['Base',10000,.18,.16,.05,65000,.06,.145,4000,1000,.3],['Credit stress',10000,.11,.18,.03,65000,.08,.145,3800,2200,.3],['Capital growth',10000,.18,.16,.07,65000,.15,.145,4300,1100,.3]],7):
    row(r,a)
    forms={'L':('=('+f'I{r}-J{r}'+f')*(1-K{r})','After-tax scenario earnings','NI=(pre-provision profit−credit loss)(1−tax)'), 'M':(f'=MAX(0,F{r}*(1+G{r})*H{r}-B{r})','Required retained capital','retained=max[0,RWA0(1+growth)×capital ratio−opening capital]'),'N':(f'=MAX(0,L{r}-M{r})','Indicative dividend capacity','dividend=max(0,NI−required retention)'),'O':(f'=IF(L{r}>0,N{r}/L{r},"Not meaningful")','Scenario payout','payout=dividend/NI'),'P':(f'=IF(OR(D{r}<=E{r},C{r}<E{r}),"Invalid growth",(C{r}-E{r})/(D{r}-E{r}))','Steady-state justified P/B','P/B=(ROE−g)/(k_e−g)'),'Q':(f'=IF(ISNUMBER(P{r}),P{r}*B{r},"Check growth")','Steady-state equity value','V=B0(ROE−g)/(k_e−g)')}
    for c,(form,desc,eq) in forms.items():f(f'{c}{r}',form,desc if r==7 else '',eq,'Stable ROE valuation separate from one-year earnings stress.')
tab('Insurance scenarios',['Case','Earned premium base','Claims','Expenses','Investment result','Other result','Finance cost','Tax rate','Opening equity','Closing equity','Loss ratio','Expense ratio','Combined ratio','Underwriting result','PBT','PAT','Average equity','ROE'],'Fictional short-tail non-life underwriting bridge; same earned-premium denominator. IFRS17 published ratios require definition mapping.',{'A':22})
for r,a in enumerate([['Base',4000,2600,1080,880,0,100,.3,10000,10500],['Claims stress',4000,3080,1080,700,0,100,.3,10000,10000],['Investment shock',4000,2600,1080,-500,0,100,.3,10000,9600]],7):
    row(r,a)
    forms={'K':(f'=C{r}/B{r}','Loss ratio','LR=claims/earned premium'),'L':(f'=D{r}/B{r}','Expense ratio','ER=expenses/earned premium'),'M':(f'=K{r}+L{r}','Combined ratio','CR=LR+ER'),'N':(f'=B{r}-C{r}-D{r}','Underwriting result','U=earned premium−claims−expenses'),'O':(f'=N{r}+E{r}+F{r}-G{r}','Profit before tax','PBT=U+investment+other−finance'),'P':(f'=O{r}-MAX(0,O{r})*H{r}','Profit after tax','PAT=PBT−max(PBT,0)tax'),'Q':(f'=(I{r}+J{r})/2','Average equity','E_avg=(E_open+E_close)/2'),'R':(f'=P{r}/Q{r}','Return on equity','ROE=PAT/E_avg')}
    for c,(form,desc,eq) in forms.items():f(f'{c}{r}',form,desc if r==7 else '',eq,'No tax credit on losses; other comprehensive income may change closing equity.')
tab('Sector screens',['Case','Revenue','COGS','Opening stock','Closing stock','Opening AR','Closing AR','Opening AP','Closing AP','Inventory days','Collection days','Payable days','Cash cycle','CFO','Capex','Cash after capex','Dividend','Cash cover'],'Fictional manufacturers; operating trade balances. Payable days uses COGS proxy; reconcile supplier finance separately.')
for r,a in enumerate([['Efficient cycle',10000,6000,500,500,300,300,1200,1200,None,None,None,None,1800,700,None,800],['Slow collections',10000,6000,800,1000,1200,1800,800,900,None,None,None,None,700,700,None,800],['Long payable cycle',10000,6000,500,500,300,300,1800,1800,None,None,None,None,1900,700,None,800]],7):
    row(r,a)
    for c,form,desc,eq in [('J',f'=AVERAGE(D{r}:E{r})/C{r}*365','Inventory days','DIO=average inventory/COGS×365'),('K',f'=AVERAGE(F{r}:G{r})/B{r}*365','Collection days','DSO=average AR/revenue×365'),('L',f'=AVERAGE(H{r}:I{r})/C{r}*365','Payable days','DPO=average AP/COGS×365'),('M',f'=J{r}+K{r}-L{r}','Cash conversion cycle','CCC=DIO+DSO−DPO'),('P',f'=N{r}-O{r}','Cash after capex','FCF_proxy=CFO−capex'),('R',f'=IF(Q{r}>0,P{r}/Q{r},"No dividend")','Cash dividend cover','cover=FCF_proxy/dividend')]:f(f'{c}{r}',form,desc if r==7 else '',eq,'KES million except days and cover multiple')
tab('Review log',['Business question','Evidence to record','Source and period','Assessment','Portfolio consequence'],'Reusable qualitative screening workbook; record a conclusion alongside supporting evidence.',{'A':39,'B':78,'C':45,'D':55,'E':60})
questions=[('Customer economics','Revenue by product, volume and price; customer concentration.','Size exposure to customers and demand shocks.'),('Competition','Pricing power, churn, margins and returns on incremental capital.','Set attainable growth and margin ranges.'),('Management','Capital allocation, related parties, incentives and past forecasts.','Set position limit and engagement questions.'),('Audit','Opinion, key audit matters, restatements and going-concern disclosures.','Prioritise unresolved valuation inputs.'),('Bank assets','NPL stock, write-offs, recoveries, stage migration and coverage definitions.','Re-estimate credit losses and distributable capital.'),('Bank liquidity','Deposit concentration, maturity gap, liquid assets and funding cost.','Add funding stress and sector exposure limit.'),('Insurance','IFRS17 service result, CSM, reserve development and reinsurance recoverability.','Map underwriting and investment contribution.'),('Manufacturing','Trade balances, inventory ageing, supplier finance and maintenance spending.','Test cash conversion and cash dividend cover.'),('Agriculture','Volumes, yields, weather, export receipts and biological fair-value movements.','Use seasonal cash flows and commodity stress.'),('Energy','Tariffs, offtaker receivables, project funding and foreign-currency debt.','Test payment delays and investment requirements.'),('Holding companies','Look-through holdings, holding-company debt and cash distributions.','Value assets less central obligations and leakage.'),('Market access','Trading status, bid/ask, turnover, lot size and custody.','Size executable orders and retain residual cash.')]
for r,(q,e,c) in enumerate(questions,7):row(r,[q,e,'To populate','To assess',c])
tab('Bank diagnostics',['Case','Gross loans','NPL stock','Allowance','Credit loss charge','Opening loans','Net interest income','Average earning assets','Operating expenses','Operating income','Core capital','Total capital','RWA','Core requirement','Total requirement','NPL ratio','Coverage','Cost of risk','NIM','Cost/income','Core ratio','Total ratio','Core headroom','Total headroom'],'Fictional bank inputs inKESmillion. Coverage is allowance/NPL, before collateral adjustments. Annual income and expense flows; regulatory requirements are editable.')
for r,a in enumerate([['Base',80000,8000,5000,1200,74000,6000,95000,3500,10000,11000,15000,80000,.105,.145],['Credit stress',80000,12000,6200,2500,80000,5500,95000,3700,9500,10000,14000,83000,.105,.145]],7):
    row(r,a)
    formulas={'P':(f'=C{r}/B{r}','NPL ratio','NPL/gross loans'),'Q':(f'=D{r}/C{r}','Allowance coverage','allowance/NPL'),'R':(f'=E{r}/AVERAGE(B{r},F{r})','Cost of risk','annual credit loss/average gross loans'),'S':(f'=G{r}/H{r}','Net interest margin','NII/average earning assets'),'T':(f'=I{r}/J{r}','Cost-to-income','operating expense/operating income'),'U':(f'=K{r}/M{r}','Core capital ratio','core capital/RWA'),'V':(f'=L{r}/M{r}','Total capital ratio','total capital/RWA'),'W':(f'=U{r}-N{r}','Core headroom','core ratio−required ratio'),'X':(f'=V{r}-O{r}','Total headroom','total ratio−required ratio')}
    for c,(form,desc,eq) in formulas.items():f(f'{c}{r}',form,desc if r==7 else '',eq,'Fractions; headroom in percentage points when multiplied by100.');sheet['formats'][f'{c}{r}']='0.00%'
tab('Historical quality',['Fiscal year','Revenue','COGS','Net profit','CFO','Assets','Long-term debt','Current assets','Current liabilities','Shares','ROA','Cash ROA','Gross margin','Asset turnover','Leverage','Current ratio'],'Fictional five-year history for demonstrating comparability and financial-strength signals. This is separate from the integrated manufacturer forecast.')
hist=[[2022,8000,5200,700,750,7500,2400,2800,2000,1000],[2023,8500,5450,760,850,8000,2350,3000,2050,1000],[2024,9000,5650,820,900,8500,2300,3300,2100,1000],[2025,9600,5850,950,1100,9000,2200,3600,2100,1000],[2026,10000,6000,1100,1300,9400,2100,3900,2100,1000]]
for r,a in enumerate(hist,7):
    row(r,a)
    for c,form,desc,eq in [('K',f'=D{r}/F{r}','Return on assets','NI/closing assets, same basis each year'),('L',f'=E{r}/F{r}','Cash return on assets','CFO/closing assets'),('M',f'=(B{r}-C{r})/B{r}','Gross margin','(Revenue−COGS)/Revenue'),('N',f'=B{r}/F{r}','Asset turnover','Revenue/closing assets'),('O',f'=G{r}/F{r}','Leverage','Long-term debt/closing assets'),('P',f'=H{r}/I{r}','Current ratio','Current assets/current liabilities')]:f(f'{c}{r}',form,desc if r==7 else '',eq,'Comparable classroom ratios; full Piotroski research conventions use defined asset timing.')
tab('Quality signals',['Signal','Current observation','Previous observation','Point','Interpretation'],'Nine binary financial-strength signals inspired by Piotroski; educational variant using closing-asset denominators, not an exact replication of the paper.',{'A':36,'E':75})
signals=[['Positive ROA','K',0,'>','Profitability'],['Positive cash flow','L',0,'>','Operating cash generation'],['Improving ROA','K','K','>','Profitability change'],['Cash exceeds accrual profit','L','K_current','>','Cash conversion'],['Lower leverage','O','O','<','Balance-sheet change'],['Improving liquidity','P','P','>','Liquidity change'],['No share issuance','J','J','<=','Ownership dilution'],['Improving gross margin','M','M','>','Operating economics'],['Improving asset turnover','N','N','>','Asset efficiency']]
for r,(label,c,prev,op,desc) in enumerate(signals,7):
    row(r,[label,None,None,None,desc]);f(f'B{r}',f"='Historical quality'!{c}11")
    f(f'C{r}','=0' if prev==0 else f"='Historical quality'!{'K11' if prev=='K_current' else str(prev)+'10'}")
    f(f'D{r}',f'=IF(B{r}{op}C{r},1,0)',label,f'point=1{{current {op} comparison}}; else0','Binary signal; see stated denominator conventions.')
f('D17','=SUM(D7:D15)','Combined educational signal count','score=Σ9 binary points','0–9; research prioritisation, not automatic selection');v('A17','Total signals')
finish()

# All portfolio inputs below are modelling assumptions, not forecasts fitted to NSE prices.
tickers=['EQTY','KCB','COOP','SCOM','BAT','JUB','KEGN','T-bill']
sectors=['Bank','Bank','Bank','Telecom','Consumer','Insurance','Energy','Sovereign']
prices=[70,65,25,35,450,300,9,1]
div=[5.75,4,2.5,2,70,15,.9,0]
mu=np.array([.12,.12,.115,.13,.10,.115,.11,.075])
vol=np.array([.28,.30,.24,.30,.25,.27,.28,.012])
loading=np.array([.70,.75,.70,.60,.45,.60,.55,.10])
corr=np.outer(loading,loading)+np.diag(1-loading**2)
cov=corr*np.outer(vol,vol)
weights=np.array([[.08,.07,.05,.08,.04,.04,.04,.60],[.10,.10,.10,.15,.08,.07,.10,.30],[.12,.10,.08,.20,.10,.08,.12,.20]])
np.random.seed(20260907)
candidates=np.random.dirichlet(np.ones(8)*2,80000)
mask=(candidates[:,:7].max(axis=1)<=.25)&(candidates[:,:3].sum(axis=1)<=.30)&(candidates[:,7]>=.20)&(candidates[:,7]<=.70)
candidates=np.vstack([weights,candidates[mask]])
rets=candidates@mu; risks=np.sqrt(np.einsum('ni,ij,nj->n',candidates,cov,candidates)); sharpes=(rets-.075)/risks
choices={'Minimum variance sampled':int(risks.argmin()),'Maximum Sharpe sampled':int(sharpes.argmax())}
portfolio_result={'assets':tickers,'mu':mu.tolist(),'vol':vol.tolist(),'correlation':corr.tolist(),'covariance':cov.tolist(),'policy_names':['Income reserve','Balanced','Growth'],'weights':weights.tolist(),'candidate_count':len(candidates),'candidate_seed':20260907,'selected':{k:{'weights':candidates[i].tolist(),'return':float(rets[i]),'risk':float(risks[i]),'sharpe':float(sharpes[i])} for k,i in choices.items()}}
(root/'Research'/'portfolio_results.json').write_text(json.dumps(portfolio_result,indent=2))
start('03-Portfolio-Construction','Portfolio allocation, risk and executable positions')
inputs([['Portfolio cash budget',1000000,'KES','Educational portfolio; separate emergency funds.'],['Buy cost',.02,'fraction','Illustrative all-in equity acquisition cost.'],['Sell cost',.02,'fraction','Illustrative disposal cost.'],['Dividend tax',.05,'fraction','Resident qualifying-dividend teaching case.'],['Risk-free comparison',.075,'annual fraction','After-tax return assumption for risk ratios.'],['Single-equity cap',.25,'portfolio fraction','Editable construction constraint.'],['Bank-sector cap',.30,'portfolio fraction','Sum EQTY,KCB,COOP.'],['Bill minimum',.20,'portfolio fraction','Allocation constraint.'],['Rebalance band',.05,'absolute weight','Five percentage points either side of target.'],['Daily turnover participation',.10,'fraction','Illustrative capacity assumption.']])
tab('Asset assumptions',['Asset','Sector','Price KES','Recurring DPS','Expected total return','Annual volatility','Common factor loading','Average daily traded KES','Lot size'],'Prices, expected returns, volatilities, liquidity and lot sizes are illustrative; ordinary dividends trace to workbook01. No future specials assumed.')
for r in range(7,15):
    i=r-7;row(r,[tickers[i],sectors[i],prices[i],div[i],float(mu[i]),float(vol[i]),float(loading[i]),10000000 if i<7 else 1000000000,1])
tab('Correlation',['Asset',*tickers],'Assumed one-factor matrix. Off-diagonal ρij=li×lj; diagonal1 guarantees a valid positive-semidefinite matrix when |l|≤1.')
for i in range(8):
    r=i+7;v(f'A{r}',tickers[i])
    for j in range(8):f(f'{col(j+2)}{r}','=1' if i==j else f"='Asset assumptions'!G{i+7}*'Asset assumptions'!G{j+7}",'Correlation' if i==0 and j==1 else '', 'ρij=li lj; ρii=1','Assumption, not an estimated historical correlation.')
tab('Covariance',['Asset',*tickers],'Annual arithmetic total-return covariance. Consistent with portfolio expected returns.')
for i in range(8):
    r=i+7;v(f'A{r}',tickers[i])
    for j in range(8):f(f'{col(j+2)}{r}',f"='Correlation'!{col(j+2)}{r}*'Asset assumptions'!F{i+7}*'Asset assumptions'!F{j+7}",'Covariance' if i==0 and j==0 else '', 'Σij=ρij σi σj','Annual return squared')
tab('Policies',['Policy',*tickers,'Weight total','Bank weight','Expected return','Volatility','Sharpe','Equity income yield','Constraint count'],'Three editable educational allocations. Income excludes bill interest; total return includes dividends and price changes; dividend tax deducted once.')
for r,w in enumerate(weights,7):
    row(r,[portfolio_result['policy_names'][r-7],*map(float,w)])
    f(f'J{r}',f'=SUM(B{r}:I{r})','Allocation reconciliation' if r==7 else '', 'Σw_i=1','fraction')
    f(f'K{r}',f'=SUM(B{r}:D{r})','Bank sector weight' if r==7 else '', 'w_bank=Σ bank weights','fraction')
    ret='+'.join(f"{col(i+2)}{r}*'Asset assumptions'!E{i+7}" for i in range(8))
    risk='+'.join(f"{col(i+2)}{r}*{col(j+2)}{r}*'Covariance'!{col(j+2)}{i+7}" for i in range(8) for j in range(8))
    f(f'L{r}','='+ret,'Expected gross total return' if r==7 else '', 'μp=Σw_i μ_i','Annual fraction; asset assumptions include distributions.')
    f(f'M{r}',f'=SQRT({risk})','Portfolio volatility' if r==7 else '', 'σp=√(wᵀΣw)','Annual standard deviation')
    f(f'N{r}',f'=(L{r}-\'Inputs\'!$B$11)/M{r}','Sharpe under model assumptions' if r==7 else '', '(μp−r_f)/σp','Mean assumptions are gross of dividend tax; benchmark defined explicitly.')
    income='+'.join(f"{col(i+2)}{r}*'Asset assumptions'!D{i+7}/'Asset assumptions'!C{i+7}*(1-'Inputs'!$B$10)" for i in range(7))
    f(f'O{r}','='+income,'After-tax recurring equity income' if r==7 else '', 'y_income=Σw_i D_i/P_i (1−t_d)','fraction of whole portfolio; bill cash separately budgeted')
    f(f'P{r}',f'=IF(ABS(J{r}-1)>0.000001,1,0)+IF(K{r}>\'Inputs\'!$B$13,1,0)+IF(MAX(B{r}:H{r})>\'Inputs\'!$B$12,1,0)+IF(I{r}<\'Inputs\'!$B$14,1,0)+IF(MIN(B{r}:I{r})<0,1,0)','Constraint violations' if r==7 else '', 'Count budget,bank,single-name,bill-floor,long-only breaches','Nonzero means adjust weights or policy.')
    for c in 'BCDEFGHIJKLMO':sheet['formats'][f'{c}{r}']='0.00%'
tab('Positions',['Asset','Target weight','Allocated budget','Price','Cost fraction','Lot','Units','Security value','Acquisition cost','Unspent cash','Recurring cash income','Actual security weight','Daily turnover KES','Days to acquire'],'Balanced policy. Bill allocation is cash budget reserved for DhowCSD, converted to face in workbook01. Whole equity shares; no fractional holdings.')
for r in range(7,15):
    i=r-7;v(f'A{r}',tickers[i]);f(f'B{r}',f"='Policies'!{col(i+2)}8",'Target allocation' if i==0 else '', 'w_i from selected balanced policy','fraction')
    ff={'C':f"=B{r}*'Inputs'!$B$7",'D':f"='Asset assumptions'!C{r}",'E':"='Inputs'!$B$8" if i<7 else '=0','F':f"='Asset assumptions'!I{r}",'G':f'=INT(C{r}/(D{r}*(1+E{r}))/F{r})*F{r}','H':f'=G{r}*D{r}','I':f'=H{r}*E{r}','J':f'=C{r}-H{r}-I{r}','K':f"=G{r}*'Asset assumptions'!D{r}*(1-'Inputs'!$B$10)",'L':f"=H{r}/'Inputs'!$B$7",'M':f"='Asset assumptions'!H{r}",'N':f"=H{r}/(M{r}*'Inputs'!$B$16)"}
    meaning={'C':'Allocated budget = weight×budget','D':'Price input','E':'Acquisition cost fraction','F':'Lot size','G':'Units = floor[budget/(price(1+fee))/lot]×lot','H':'Security value = units×price','I':'Cost = security value×fee','J':'Residual cash = budget−security value−cost','K':'Income = units×DPS×(1−tax)','L':'Actual security weight = value/initial budget','M':'Turnover assumption','N':'Acquisition days = order value/(daily turnover×participation)'}
    for c,form in ff.items():f(f'{c}{r}',form,meaning[c] if i==0 else '',meaning[c],'KES or explicitly labelled units; no market-impact model beyond assumed participation.')
row(16,['Total'])
for c in ['B','C','H','I','J','K','L']:f(f'{c}16',f'=SUM({c}7:{c}14)','Column total' if c=='C' else '', 'total=Σ rows','Units follow column')
f('C18','=C16-H16-I16-J16','Budget reconciliation','budget−security value−cost−residual=0','KES')
tab('Risk contributions',['Asset','Balanced weight','Covariance with portfolio','Variance contribution','Share of portfolio variance'],'Contributions add to total variance. Bill sleeve uses an assumed low annual rollover-return volatility.')
for r in range(7,15):
    i=r-7;row(r,[tickers[i]])
    f(f'B{r}',f"='Policies'!{col(i+2)}8")
    f(f'C{r}','='+ '+'.join(f"'Covariance'!{col(j+2)}{r}*'Policies'!{col(j+2)}8" for j in range(8)),'Covariance with portfolio' if i==0 else '', '(Σw)_i=ΣjΣij wj','return squared')
    f(f'D{r}',f'=B{r}*C{r}','Variance contribution' if i==0 else '', 'VC_i=w_i(Σw)_i','return squared')
    f(f'E{r}',f'=D{r}/\'Policies\'!$M$8^2','Variance share' if i==0 else '', 'share_i=VC_i/σp²','fraction')
    sheet['formats'][f'E{r}']='0.00%'
f('D16','=SUM(D7:D14)','Total variance','ΣVC_i=σp²','return squared');f('E16','=SUM(E7:E14)','Risk-share reconciliation','Σshare_i=1','fraction')
tab('Joint stress',['Scenario',*tickers,'Income reserve','Balanced','Growth'],'One-year total returns including dividends; before portfolio trading costs. Deterministic assumptions, no assigned likelihood.')
scenarios=[['Domestic credit shock',-.35,-.4,-.3,-.15,-.1,-.25,-.2,.065],['Shilling and inflation shock',-.2,-.22,-.15,-.25,-.08,-.15,-.3,.08],['Earnings recovery',.25,.3,.2,.25,.15,.2,.18,.06],['Liquidity shock',-.25,-.3,-.25,-.25,-.2,-.35,-.35,.07]]
for r,vals in enumerate(scenarios,7):
    row(r,vals)
    for j in range(3):f(f'{col(10+j)}{r}',f'=SUMPRODUCT(B{r}:I{r},\'Policies\'!B{7+j}:I{7+j})','Weighted scenario return' if r==7 and j==0 else '', 'R_s=Σw_i R_i,s','Annual total-return fraction')
tab('Sampled portfolios',['Candidate',*tickers,'Expected return','Volatility','Sharpe'],'Fixed seeded candidate weights; live metrics. Candidates satisfy initial caps; rerun Research engine to regenerate after changing constraints.')
# Keep a useful audit sample and both selected candidates; full search remains reproducible in Python.
indices=list(range(min(200,len(candidates))))+list(choices.values())
for r,i in enumerate(indices,7):
    row(r,[i,*map(float,candidates[i])])
    f(f'J{r}','='+ '+'.join(f"{col(j+2)}{r}*'Asset assumptions'!E{j+7}" for j in range(8)),'Candidate return' if r==7 else '', 'μp=wᵀμ','Assumed annual total return')
    risk='+'.join(f"{col(j+2)}{r}*{col(k+2)}{r}*'Covariance'!{col(k+2)}{j+7}" for j in range(8) for k in range(8))
    f(f'K{r}',f'=SQRT({risk})','Candidate volatility' if r==7 else '', 'σp=√(wᵀΣw)','Annual')
    f(f'L{r}',f'=(J{r}-\'Inputs\'!$B$11)/K{r}','Candidate Sharpe' if r==7 else '', '(μp−r_f)/σp','Gross-return comparison')
tab('Search results',['Selection',*tickers,'Expected return','Volatility','Sharpe','Candidates tested'],'Python seeded search snapshot; weights are inputs, metrics update in Excel. Approximate sampled search, not a guaranteed global optimum.')
for r,(name,i) in enumerate(choices.items(),7):
    row(r,[name,*map(float,candidates[i]),float(rets[i]),float(risks[i]),float(sharpes[i]),len(candidates)])
    source_row=7+len(indices)-2+(r-7)
    for c in ['J','K','L']:f(f'{c}{r}',f"='Sampled portfolios'!{c}{source_row}",'Selected candidate metric' if r==7 and c=='J' else '', 'Selected metric linked to candidate formulas','Re-run search for changed optimal weights.')
tab('Rebalance',['Asset','Current units','Current price','Current value','Current weight','Target weight','Weight drift','Band exceeded','Target value','Indicative units change','Trade value','Cost fraction','Estimated cost','Net cash needed'],'Illustrative current units and prices. Signed trades: positive buys, negative sells. Costs on both sides. Review current valuation and trading capacity.',{'A':23})
for r in range(7,15):
    i=r-7;row(r,[tickers[i], [1400,1500,3900,4200,174,228,10890,300000][i],prices[i]*(1+[.1,.05,-.1,.2,-.05,0,.15,0][i])])
    ff={'D':f'=B{r}*C{r}','E':f'=D{r}/SUM($D$7:$D$14)','F':f"='Policies'!{col(i+2)}8",'G':f'=E{r}-F{r}','H':f'=IF(ABS(G{r})>\'Inputs\'!$B$15,1,0)','I':f'=F{r}*SUM($D$7:$D$14)','J':f'=IF(I{r}>=D{r},INT((I{r}-D{r})/C{r}),-INT((D{r}-I{r})/C{r}))','K':f'=J{r}*C{r}','L':f'=IF(J{r}>0,\'Inputs\'!$B$8,\'Inputs\'!$B$9)' if i<7 else '=0','M':f'=ABS(K{r})*L{r}','N':f'=K{r}+M{r}'}
    eq={'D':'V=qP','E':'w=V/ΣV','F':'target from balanced policy','G':'drift=current−target','H':'trigger=1{|drift|>band}','I':'target value=target weight×ΣV','J':'signed whole units toward target, rounded toward zero','K':'trade value=units change×price','L':'cost rate=buy or sell rate','M':'cost=|trade value|×rate','N':'cash needed=signed trade value+cost'}
    for c,form in ff.items():f(f'{c}{r}',form,eq[c] if i==0 else '',eq[c],'Preview before cash-cost adjustment; positive total net cash needs additional funding.')
f('N16','=SUM(N7:N14)','Net cash requirement','net cash=Σ(buys−sales+costs)','KES; fund this amount or reduce buys before implementation.');v('A16','Net cash required')
finish()

start('04-Compounding-and-Simulation','Compounding, cash flow and simulation')
inputs([['Opening wealth',1000000,'KES','Investable capital after establishing emergency reserve.'],['Annual contribution',120000,'KES at year end','Nominal amount; editable annual path below.'],['Annual withdrawal',0,'KES at year end','Enter spending after return and contribution.'],['Expected gross total return',float(weights[1]@mu),'annual arithmetic fraction','Balanced portfolio assumption, workbook03.'],['Annual volatility',float(np.sqrt(weights[1]@cov@weights[1])),'annual standard deviation','Balanced covariance model, workbook03.'],['Inflation',.05,'annual fraction','Scenario assumption.'],['Annual implementation drag',.003,'fraction','Trading and monitoring friction assumption, separate from dividend tax.'],['Gross equity dividend yield',float(sum(weights[1,:7]*np.array(div[:7])/np.array(prices[:7]))),'annual fraction','Balanced policy recurring dividend yield, workbook03.'],['Dividend tax',.05,'fraction','Applied to dividend component once.'],['Crisis probability',.08,'annual fraction','Independent annual regime draw; illustrative.'],['Crisis loss',.25,'fraction','Additional proportional loss in crisis year.'],['Horizon',20,'years','Twenty annual steps.'],['Goal in current purchasing power',3000000,'KES','Success test at year20.'],['Workbook paths',500,'trials','Fixed random draws; external engine evaluates10000.']])
v('A18','Workbook horizon');f('B18',"=COLUMNS('Paths'!B6:U6)",'Workbook horizon','n = number of annual path columns','Years; fixed layout, extend model to change horizon.');v('D18','Calculated from the fixed twenty-year worksheet layout.')
v('A20','Workbook path count');f('B20',"=ROWS('Paths'!A7:A506)",'Workbook path count','N = number of simulated path rows','Trials; fixed layout.');v('D20','Calculated from the fixed 500-path worksheet layout.')
tab('Annual plan',['Year','Contribution','Withdrawal','Inflation','Implementation drag','Dividend tax drag','Expected gross return','Volatility'],'Defaults link to Inputs. Override individual years here for a varying plan. Income is already included in total return; only dividend withholding is subtracted.')
for r in range(7,27):
    row(r,[r-6])
    for c,ir in [('B',8),('C',9),('D',12),('E',13)]:f(f'{c}{r}',f"='Inputs'!$B${ir}")
    f(f'F{r}',"='Inputs'!$B$14*'Inputs'!$B$15",'Tax drag' if r==7 else '', 'tax drag = gross dividend yield × dividend tax','Annual fraction')
    f(f'G{r}',"='Inputs'!$B$10");f(f'H{r}',"='Inputs'!$B$11")
tab('Deterministic',['Year','Opening wealth','Net return','Investment gain','Contribution','Withdrawal requested','Closing wealth','Unfunded withdrawal','Price index','Real wealth'],'Returns first, then contribution, then withdrawal. Exhaustion recorded explicitly; annual contributions occur at year end.')
for r in range(7,27):
    row(r,[r-6]);ff={'B':"='Inputs'!B7" if r==7 else f'=G{r-1}','C':f"='Annual plan'!G{r}-'Annual plan'!E{r}-'Annual plan'!F{r}",'D':f'=B{r}*C{r}','E':f"='Annual plan'!B{r}",'F':f"='Annual plan'!C{r}",'G':f'=MAX(0,B{r}+D{r}+E{r}-F{r})','H':f'=MAX(0,F{r}-(B{r}+D{r}+E{r}))','I':f"=(1+'Annual plan'!D{r})" if r==7 else f"=I{r-1}*(1+'Annual plan'!D{r})",'J':f'=G{r}/I{r}'}
    eq={'B':'Opening W=prior closing W','C':'net r=gross r−cost drag−dividend tax drag','D':'Gain=W_open×net r','E':'Contribution=C_t','F':'Requested withdrawal=X_t','G':'W_close=max(0,W_open(1+r)+C−X)','H':'Gap=max(0,X−W_open(1+r)−C)','I':'Price index=∏(1+inflation_t)','J':'Real wealth=W_close/price index'}
    for c,form in ff.items():f(f'{c}{r}',form,eq[c] if r==7 else '',eq[c],'KES except rate and price index')
sheet['charts'].append({'range':'A6:A26,J6:J26','title':'Real wealth by year','anchor':['L6','T22']})
tab('Draws',['Path','Year','Normal shock','Crisis uniform'],'Fixed NumPy seed20260908;500paths×20years. Standard normal and independent uniform draws; regenerate via supplied engine.')
rng=np.random.default_rng(20260908);z=rng.standard_normal((500,20));u=rng.random((500,20))
for i in range(500):
    for t in range(20):row(7+i*20+t,[i+1,t+1,float(z[i,t]),float(u[i,t])])
tab('Paths',['Path',*list(range(1,21))],'Annual wealth by path; lognormal total-return shocks with moment-matched arithmetic mean and volatility. Crisis probability/loss add a separate downside regime.')
for i in range(500):
    r=i+7;v(f'A{r}',i+1)
    for t in range(20):
        c=col(t+2); prev="'Inputs'!$B$7" if t==0 else f'{col(t+1)}{r}';dr=7+i*20+t;ar=t+7
        m=f"'Annual plan'!G{ar}";volr=f"'Annual plan'!H{ar}";s2=f'LN(1+({volr}/(1+{m}))^2)'
        gross=f'EXP(LN(1+{m})-({s2})/2+SQRT({s2})*\'Draws\'!C{dr})'
        factor=f"(1-IF('Draws'!D{dr}<'Inputs'!$B$16,'Inputs'!$B$17,0))"
        f(f'{c}{r}',f'=MAX(0,({prev})*MAX(0,{gross}*{factor}-\'Annual plan\'!E{ar}-\'Annual plan\'!F{ar})+\'Annual plan\'!B{ar}-\'Annual plan\'!C{ar})','Annual simulated wealth' if i==0 and t==0 else '', 's²=ln[1+σ²/(1+μ)²]; gross=exp[ln(1+μ)−s²/2+sZ]; W_t=max(0,W_(t−1)max(0,gross(1−J loss)−cost−taxdrag)+C_t−X_t)','J=1{U<p}; independent annual shocks; crisis lowers unconditional expected return.')
tab('Simulation summary',['Year','P05 nominal','Median nominal','P95 nominal','Mean nominal','P05 real','Median real','P95 real'],'500 fixed paths; percentile summaries are conditional model outcomes. Annual values after contributions and withdrawals.')
for r in range(7,27):
    t=r-7;c=col(t+2);row(r,[t+1])
    for j,(prob,label) in enumerate([(.05,'P05'),(.5,'Median'),(.95,'P95')],2):f(f'{col(j)}{r}',f'=PERCENTILE(\'Paths\'!{c}7:{c}506,{prob})',label if r==7 else '', 'q_p=empirical percentile of simulated wealth','KES')
    f(f'E{r}',f'=AVERAGE(\'Paths\'!{c}7:{c}506)','Mean' if r==7 else '', 'mean=ΣW/N','KES')
    for j in range(6,9):f(f'{col(j)}{r}',f'={col(j-4)}{r}/\'Deterministic\'!I{r}','Inflation-adjusted percentile' if r==7 and j==6 else '', 'real percentile=nominal percentile/price index','KES purchasing power at start')
f('B29',"=COUNTIF('Paths'!U7:U506,\">=\"&('Inputs'!B19*'Deterministic'!I26))/500",'Goal success fraction','p̂=count(W20≥realgoal×priceindex)/N','500 simulated paths');v('A29','Goal success')
f('B30','=SQRT(B29*(1-B29)/500)','Sampling standard error','SE=√[p̂(1−p̂)/N]','Excludes uncertainty in μ,σ and model choice');v('A30','Success standard error')
tab('Goal sensitivity',['Real goal KES','Success fraction','Sampling SE'],'Same fixed paths across goals for a clean comparison.')
for r,goal in enumerate([1500000,2000000,2500000,3000000,3500000,4000000,5000000],7):
    row(r,[goal]);f(f'B{r}',f'=COUNTIF(\'Paths\'!U7:U506,">="&(A{r}*\'Deterministic\'!$I$26))/500','Goal probability' if r==7 else '', 'p̂(G)=count(W20≥G×inflationindex)/N','fraction');f(f'C{r}',f'=SQRT(B{r}*(1-B{r})/500)','Probability SE' if r==7 else '', 'SE=√[p̂(1−p̂)/N]','fraction')
tab('Sequence test',['Year','Return A','Return reversed','Wealth A','Wealth reversed','Withdrawal'],'Same returns in different order; openingKES1m, withdrawalsKES100k at year end. Compare both sequences including negative years.')
seq=[-.25,-.10,.08,.15,.22]
for r,x in enumerate(seq,7):
    row(r,[r-6,x,seq[::-1][r-7],None,None,100000])
    for c,rc in [('D','B'),('E','C')]:f(f'{c}{r}',f'=MAX(0,1000000*(1+{rc}{r})-F{r})' if r==7 else f'=MAX(0,{c}{r-1}*(1+{rc}{r})-F{r})','Wealth with withdrawals' if r==7 and c=='D' else '', 'W_t=max[0,W_(t−1)(1+r_t)−X_t]','KES; sequence order matters with cash flows')
tab('Monitoring',['Review item','Record','Trigger or question','Action log'],'Use after each report, corporate action, contribution and material price move.',{'A':34,'B':60,'C':78,'D':70})
for r,a in enumerate([['Business thesis','Original valuation and assumptions','What changed in cash generation or competitive position?',''],['Income','Declared, approved, ex-date, record-date, payment-date','Compare cash received with expected ordinary distributions.',''],['Portfolio drift','Current weights and policy limits','Use contributions before discretionary sales where practicable.',''],['Liquidity','Cash reserve and maturity schedule','Does the next commitment have a funded payment route?',''],['Performance','Opening wealth, contributions, withdrawals, fees and end wealth','Separate investment return from saving effort; use dated cash flows.',''],['Risk','Sector, sovereign, currency and employer exposures','Re-run shared stress scenarios after material changes.',''],['Data refresh','Price timestamp, report period and source','Update ordinary dividends, specials and share counts separately.','']],7):row(r,a)
tab('Performance',['Year','Opening value','End before external flow','End contribution','End withdrawal','Closing value','Subperiod return','Linked return index','Investor cash flow'],'Fictional annual valuations immediately before year-end flows. Time weighted links period returns; investor IRR uses annual equal spacing.')
for r,a in enumerate([[1,1000000,1100000,200000,0],[2,None,1235000,0,100000],[3,None,1248500,0,0]],7):
    row(r,a)
    if r>7:f(f'B{r}',f'=F{r-1}')
    for c,form,desc,eq in [('F',f'=C{r}+D{r}-E{r}','Closing account value','V_close=V_preflow+C−X'),('G',f'=C{r}/B{r}-1','Subperiod return','r=V_preflow/V_open−1'),('H',f'=1+G{r}' if r==7 else f'=H{r-1}*(1+G{r})','Time-weighted growth index','index=∏(1+r_t)'),('I',f'=E{r}-D{r}'+(f'+F{r}' if r==9 else ''),'Investor cash flow','CF=withdrawal−contribution+terminal value at exit')]:f(f'{c}{r}',form,desc if r==7 else '',eq,'KES except return/index; distributions retained in preflow account valuation.')
row(12,['Initial investor cash flow',-1000000]);f('B13','=I7');f('B14','=I8');f('B15','=I9')
f('B17','=H9-1','Cumulative time-weighted return','TWR=∏(1+r_t)−1','Three-year cumulative fraction');v('A17','Cumulative TWR')
f('B18','=H9^(1/3)-1','Annualised TWR','TWR_annual=index^(1/years)−1','Annual fraction');v('A18','Annualised TWR')
f('B19','=IRR(B12:B15)','Money-weighted return','Find r such that Σ CF_t/(1+r)^t=0','Annual equal intervals; use XIRR for actual dates.');v('A19','Annual investor IRR')
f('B20','=F9-B7-SUM(D7:D9)+SUM(E7:E9)','Investment gain reconciliation','gain=ending−opening−contributions+withdrawals','KES');v('A20','Investment gain KES')
finish()

# External reproducible experiments: common random numbers across allocations and assumptions.
rng=np.random.default_rng(20260909);Z=rng.standard_normal((10000,20,9));U=rng.random((10000,20))
asset_z=Z[:,:,0,None]*loading+Z[:,:,1:]*np.sqrt(1-loading**2)
sig2=np.log1p((vol/(1+mu))**2); gross=np.exp(np.log1p(mu)-sig2/2+np.sqrt(sig2)*asset_z)
crisis=(U<.08); crisis_losses=np.array([.35,.40,.30,.25,.20,.30,.30,0])
gross_crisis=gross*(1-crisis[:,:,None]*crisis_losses)
cases={}
def run(w,g,contrib=120000,infl=.05,withdraw=0):
    wealth=np.full(10000,1000000.);hist=[];unit=np.ones(10000);peak=unit.copy();maxdd=np.zeros(10000);anygap=np.zeros(10000,dtype=bool)
    tax=float(np.sum(w[:7]*np.array(div[:7])/np.array(prices[:7]))*.05)
    for t in range(20):
        factor=np.maximum(0,g[:,t,:]@w-.003-tax)
        unit*=factor;peak=np.maximum(peak,unit);maxdd=np.maximum(maxdd,1-unit/peak)
        available=wealth*factor+contrib;anygap|=(available<withdraw);wealth=np.maximum(0,available-withdraw);hist.append(wealth.copy())
    real=wealth/(1+infl)**20;success=real>=3000000; n=len(real);q=np.quantile(real,[.05,.5,.95]);loss=1-unit
    tail=np.sort(loss)[-int(.05*n):]
    return {'p05_real':float(q[0]),'median_real':float(q[1]),'p95_real':float(q[2]),'mean_real':float(real.mean()),'goal_success':float(success.mean()),'success_se':float(np.sqrt(success.mean()*(1-success.mean())/n)),'median_max_drawdown':float(np.median(maxdd)),'p95_max_drawdown':float(np.quantile(maxdd,.95)),'mean_worst_5pct_terminal_unit_loss':float(tail.mean()),'withdrawal_gap_probability':float(anygap.mean()),'paths':n},np.array(hist)
for i,name in enumerate(portfolio_result['policy_names']):
    for regime,g in [('Baseline',gross),('Crisis mixture',gross_crisis)]:cases[name+' / '+regime],_=run(weights[i],g)
for name,c,inf,x in [('Half contribution',60000,.05,0),('Higher contribution',180000,.05,0),('Higher inflation',120000,.08,0),('Withdrawals',0,.05,100000)]:cases['Balanced / '+name],_=run(weights[1],gross_crisis,c,inf,x)
simulation={'seed':20260909,'paths':10000,'years':20,'crisis_probability':.08,'crisis_asset_losses':crisis_losses.tolist(),'rebalancing':'Annual constant weights; 0.3% drag plus dividend tax; year-end nominal contributions; no transaction lot rounding in simulation','distribution':'Moment-matched asset lognormal gross returns; one-factor latent normals; Pearson simple-return correlations differ slightly from normal-factor correlations','cases':cases}
(root/'Research'/'simulation_results.json').write_text(json.dumps(simulation,indent=2))
# Include the larger experiment in the workbook as an explicitly dated snapshot.
book=books[3]
tab('Extended simulation',['Case','P05 real KES','Median real KES','P95 real KES','Goal success','Sampling SE','Median max drawdown','P95 max drawdown','Any withdrawal gap'],'10,000-path asset-level snapshot; seed20260909,20years. Re-run engine to refresh. Live500-path experiment is a different aggregate model.',{'A':44})
for r,(name,result) in enumerate(cases.items(),7):row(r,[name,*[result[k] for k in ['p05_real','median_real','p95_real','goal_success','success_se','median_max_drawdown','p95_max_drawdown','withdrawal_gap_probability']]])
for r in range(7,17):
    for c in 'EFGHI':sheet['formats'][f'{c}{r}']='0.00%'
# Show per-sheet modelling conventions in a compact guide, with sources in their own table.
for book in books:
    existing=list(book['sheets']);tab('Guide',['Worksheet','Purpose and conventions'],'Educational models. Research cutoff7Sep2026. Blue values editable; green formulas linked; black formulas local. Full mathematical definitions are in Formula dictionary.',{'A':32,'B':125})
    for r,s in enumerate(existing,7):row(r,[s['name'],s['notes']])
    book['sheets']=[book['sheets'][-1]]+book['sheets'][:-1]
    # Consistent formatting of fractions and per-sheet assumptions.
    for s in book['sheets']:
        if s['name']=='Inputs':
            for addr,value in s['cells'].items():
                if addr.startswith('C') and isinstance(value,str) and ('fraction' in value or 'weight' in value):s['formats']['B'+addr[1:]]='0.00%'
        if s['name']=='Annual drivers':
            for r in [7,8,9,10,11,15,16,18]:
                for c in 'BCDEF':s['formats'][f'{c}{r}']='0.0%'
        if s['name']=='DCF':
            for addr in ['B9','B16','B17']:s['formats'][addr]='0.00%'
        if s['name']=='DCF sensitivity':
            for c in 'BCDEF':s['formats'][c+'6']='0%'
        for j,h in enumerate(s['headers'],1):
            if isinstance(h,str) and any(x in h.lower() for x in ['yield','volatility','expected return','total return','weight','headroom','goal success','sampling se','drawdown','subperiod return','stressed net']):
                if not any(x in h.lower() for x in ['weight drift','weighted','amount','value','price']):
                    for addr in s['cells']:
                        if re.match(r'^'+col(j)+r'\d+$',addr):s['formats'][addr]='0.00%'
    # Persist every actual formula for full audit, beyond the compact formula-family dictionary.
    import csv
    with (root/'Research'/(book['name']+'-formula-audit.csv')).open('w',newline='',encoding='utf-8-sig') as handle:
        wr=csv.writer(handle);wr.writerow(['Worksheet','Cell','Excel formula'])
        for s in book['sheets']:
            for addr,value in s['cells'].items():
                if isinstance(value,str) and value.startswith('='):wr.writerow([s['name'],addr,value])
(base/'spec.json').write_text(json.dumps(books,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'books':[(b['name'],len(b['sheets']),sum(len(s['cells']) for s in b['sheets'])) for b in books], 'candidates':len(candidates),'simulation':cases['Balanced / Crisis mixture']},indent=2))
