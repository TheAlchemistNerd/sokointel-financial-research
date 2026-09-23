from pathlib import Path
import json,re

root=Path(__file__).parent
report=json.loads((root/'verification.json').read_text(encoding='utf-8'))
ledger=root/'report-source.md'
content=ledger.read_text(encoding='utf-8')
inventory=[]
for i,path in enumerate(sorted(root.glob('Part *.md')),1):
    refs=path.read_text(encoding='utf-8').split('## References',1)[1].strip()
    inventory.append(f'### Part {i}\n\n'+refs)
content=content.split('## Complete source inventory')[0]+'## Complete source inventory\n\n'+'\n\n'.join(inventory)+'\n'
ledger.write_text(content,encoding='utf-8')

rows=[]
for i,a in enumerate(report['articles'],1):
    target=(root/a['file']).as_posix()
    rows.append(f"| {i} | [{a['file'][9:-3]}](<{target}>) | {a['prose_words']:,} | {a['shortest_paragraph']} | {a['flowcharts']} | {a['calculations']} |")
readme='''# International investing and diaspora finance

A three-part LinkedIn series following a fictional Kenyan family across Nairobi, Manchester, and Dublin. The articles use an exploratory, pragmatic tone, with authoritative and peer-reviewed online sources in IEEE format. Research checked on **7 September 2026**.

| Part | Article | Prose words | Shortest prose paragraph | Flowcharts | Worked calculations |
| --- | --- | ---: | ---: | ---: | ---: |
'''+ '\n'.join(rows)+'''

Every article exceeds 3,500 prose words, and every prose paragraph exceeds 100 words. Counts exclude titles, headings, references, tables, equations, and diagram labels. Across the series: **42 references, including eight peer-reviewed publications; six illustrated flowcharts; 24 worked calculations**. The research distinguishes factual rules from hypothetical assumptions and explains what each calculation demonstrates and leaves out.

## The five questions behind the series

1. What does an investor actually own when choosing an ETF's exposure, domicile, share class, and trading currency?
2. When does an Irish UCITS structure improve results after withholding, fund charges, and transaction costs?
3. How do residence and relocation affect taxable income, gains, wrappers, and reporting?
4. Which IBKR, Wise, bank, and remittance routes work for the actual customer and currency?
5. How can investing and dependable family support share a workable household plan?

## Research and supporting files

'''+f'''- [Research scope, evidence ledger, corrections, and complete source inventory](<{ledger.as_posix()}>)
- [Verification results](<{(root/'verification.json').as_posix()}>)
- [All six flowcharts at a glance](<{(root/'Flowcharts/contact-sheet.png').as_posix()}>)

The individual PNG flowcharts are embedded in the articles and available in the Flowcharts folder for reuse. Editable Mermaid sources are retained beside them. All portfolio returns, remittance quotes, budgets, and exchange rates are illustrative unless specifically identified as sourced figures. The source documents remain unchanged.
'''
(root/'README.md').write_text(readme,encoding='utf-8')
print('Completed research inventory and series index.')
