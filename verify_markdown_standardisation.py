from pathlib import Path
import re
root=Path(r"C:\Users\Nevo\Downloads\financial material")
targets=[root/'NSE Dividend Growth Project 2026', root/'Kenyan Equities and Company Analysis'/'Four Part Series', root/'NSE Value Investing and Dividend Growth', root/'US Markets and Portfolio Construction'/'Unified Series']
for base in targets:
    files=[p for p in base.rglob('*.md') if 'node_modules' not in p.parts and 'Archive-before-real-company-update' not in p.parts and not (base.name=='NSE Value Investing and Dividend Growth' and 'Research Notes' in p.parts)]
    em=[]; bad=[]; tables=[]
    for p in files:
        t=p.read_text(encoding='utf8')
        if '—' in t: em.append(str(p.relative_to(root)))
        if re.search(r'[²³⁴⁵⁶⁷⁸⁹⁰¹√∑σρβΔπ≤≥≠×÷]',t):bad.append(str(p.relative_to(root)))
        rows=[]
        for n,l in enumerate(t.splitlines(),1):
            if l.startswith('|'): rows.append((n,l.count('|')))
            elif rows:
                if len({c for _,c in rows})>1: tables.append((str(p.relative_to(root)),rows[0][0]))
                rows=[]
        if rows and len({c for _,c in rows})>1:tables.append((str(p.relative_to(root)),rows[0][0]))
    print(base.name, 'files',len(files),'emdash',em,'unicode_formula',bad,'table_issues',tables)