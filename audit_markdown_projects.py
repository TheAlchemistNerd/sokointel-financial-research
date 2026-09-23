from pathlib import Path
import re
root = Path(r"C:\Users\Nevo\Downloads\financial material")
targets = [root / "NSE Dividend Growth Project 2026", root / "Kenyan Equities and Company Analysis", root / "NSE Value Investing and Dividend Growth", root / "US Markets and Portfolio Construction" / "Unified Series"]
formula_chars = re.compile(r"[²³⁴⁵⁶⁷⁸⁹⁰¹√∑σρβΔπ≤≥≠×÷]")
for base in targets:
    files = list(base.rglob("*.md"))
    em = []
    uni = []
    table_issues = []
    inline_urls = []
    for p in files:
        text = p.read_text(encoding='utf-8')
        if '—' in text: em.append((p.relative_to(root), text.count('—')))
        body = text.split('## References', 1)[0].split('## Sources', 1)[0]
        lines = body.splitlines()
        hits = [(n+1, line.strip()) for n,line in enumerate(lines) if formula_chars.search(line)]
        if hits: uni.append((p.relative_to(root), hits))
        rows = []
        for n,line in enumerate(lines,1):
            if line.startswith('|'):
                rows.append((n,line))
            elif rows:
                counts={r[1].count('|') for r in rows}
                if len(counts)>1: table_issues.append((p.relative_to(root), rows[0][0], sorted(counts)))
                rows=[]
        if rows:
            counts={r[1].count('|') for r in rows}
            if len(counts)>1: table_issues.append((p.relative_to(root), rows[0][0], sorted(counts)))
        for n,line in enumerate(lines,1):
            if 'http://' in line or 'https://' in line:
                inline_urls.append((p.relative_to(root),n,line.strip()[:150]))
    print('\nPROJECT', base.name)
    print('EM_DASH_FILES', len(em), em[:20], 'TOTAL',sum(v for _,v in em))
    print('UNICODE_FORMULA_FILES', len(uni))
    for p,h in uni[:12]: print(' ',p, h[:4])
    print('TABLE_ISSUES', table_issues[:20], 'TOTAL',len(table_issues))
    print('INLINE_URLS', inline_urls[:12], 'TOTAL',len(inline_urls))