"""Editorial checks: prose length, paragraph minimum, references and worked arithmetic."""
from pathlib import Path
import re
import json
import math

root = Path(__file__).parent
results = []
for path in sorted(root.glob('Part *.md')):
    full = path.read_text(encoding='utf-8')
    body, refs = full.split('## References', 1)
    clean = re.sub(r'```.*?```', '', body, flags=re.S)
    clean = re.sub(r'(?m)^>.*(?:\n|$)', '', clean)
    clean = re.sub(r'\$\$.*?\$\$', '', clean, flags=re.S)
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', clean)
                  if p.strip() and not p.lstrip().startswith(('#', '|', '!['))]
    def words(p):
        p = re.sub(r'\[[0-9]+\]', '', p)
        p = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', p)
        return len(re.findall(r"\S*[A-Za-z0-9]\S*", p))
    counts = [words(p) for p in paragraphs]
    used = set(map(int, re.findall(r'\[(\d+)\]', body)))
    defined = set(map(int, re.findall(r'^\[(\d+)\]', refs, flags=re.M)))
    results.append(dict(file=path.name, prose_words=sum(counts), paragraphs=len(counts),
        shortest_paragraph=min(counts), short_paragraphs=[(i+1,n) for i,n in enumerate(counts) if n<100],
        references=len(defined), missing_references=sorted(used-defined), unused_references=sorted(defined-used),
        flowcharts=body.count('```mermaid')+body.count('![Flowchart:'), calculations=len(re.findall(r'^### Worked calculation',body,re.M))))
checks = {
    'overlap_percent': (0.8*0.06+0.2*0.12)*100,
    'kes_return_percent': (1.08*120/130-1)*100,
    'structural_saving_usd': 100000*((.015*.30+.0003)-(.015*.15+.0007)),
    'compound_difference_usd': 10000*(1.07**20-1.065**20),
    'irish_year8_value_eur': 10000*1.06**8,
    'irish_year8_tax_eur': (10000*1.06**8-10000)*.38,
    'german_advance_income_eur': 10000*.7*.032,
    'remittance_a_kes': (500-5)*165,
    'remittance_b_kes': 500*162,
    'fx_crossover_usd': 2/.0003,
    'dividend_breakeven_yield_percent': (.0007-.0003)/(.30-.15)*100,
    'small_portfolio_after_dealing_usd': 20000*.00185-20,
    'spread_percent': (100.10-99.90)/100*100,
    'spread_roundtrip_usd': 100*(100.10-99.90),
    'loss_recovery_percent': (10000/7000-1)*100,
    'withdrawal_recovery_percent': (10000/6000-1)*100,
    'rebalance_sale_usd': 8400-11400*.70,
    'kenya_average_days': (130+120+120)/3,
    'fig_net_benefit_gbp': 1200-1600,
    'eri_gbp': 1000*.8,
    'eri_adjusted_gain_gbp': 12000-10000-800,
    'irish_remaining_value_eur': 10000*1.06**8-(10000*1.06**8-10000)*.38,
    'german_capped_income_eur': max(0,min(224,100)),
    'german_loss_year_income_eur': max(0,min(224,-500)),
    'credit_additional_tax_units': max(0,250-150),
    'budget_surplus_gbp': 3000-1800-400-300,
    'world_bank_global_cost_usd': 200*.0636,
    'world_bank_digital_cost_usd': 200*.0459,
    'remittance_a_shortfall_percent': (82500-81675)/82500*100,
    'remittance_b_shortfall_percent': (82500-81000)/82500*100,
    'manual_fx_500_usd': max(2,500*.00002),
    'auto_fx_500_usd': 500*.0003,
    'manual_fx_10000_usd': max(2,10000*.00002),
    'auto_fx_10000_usd': 10000*.0003,
    'manual_proportional_threshold_usd': 2/.00002,
    'funding_a_usd': 1000-12-3-1,
    'funding_b_usd': 1000-4-15-1,
    'batch_fee_saving_usd': 12*20-4*20,
    'batch_opportunity_cost_usd': 6000*.06/12,
    'batch_net_advantage_usd': 12*20-4*20-6000*.06/12,
    'support_reserve_gbp': 3*400,
    'support_fx_stress_gbp': 66000/150-66000/165,
    'investment_profit_usd': 12100-10000-2000+500,
}
assert math.isclose(checks['structural_saving_usd'],185)
assert round(checks['compound_difference_usd'],2)==3460.39
assert round(checks['irish_year8_tax_eur'],2)==2256.62
assert math.isclose(checks['german_advance_income_eur'],224)
for article in results:
    assert article['prose_words'] >= 3500, article
    assert article['shortest_paragraph'] >= 100, article
    assert not article['missing_references'] and not article['unused_references'], article
    assert article['flowcharts'] == 2, article
for path in sorted(root.glob('Part *.md')):
    body = path.read_text(encoding='utf-8').split('## References')[0]
    sequence = list(map(int,re.findall(r'^### Worked calculation (\d+)',body,re.M)))
    assert sequence == list(range(1,len(sequence)+1)), sequence
    for target in re.findall(r'!\[[^]]*\]\(<([^>]+)>\)',body):
        assert Path(target).is_file(), target
report = dict(articles=results, arithmetic=checks)
(root/'verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
