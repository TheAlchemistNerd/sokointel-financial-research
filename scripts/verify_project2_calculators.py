"""Read-only XLSX-to-web reconciliation; writes only the requested JSON report."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import openpyxl


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--website', type=Path, default=Path('../business and technical website blog'))
    parser.add_argument('--report', type=Path, default=Path('Publishing and Video Production/Project 2 Calculator Delivery/workbook-reconciliation.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    website = args.website.resolve()
    sys.path.insert(0, str(website))
    from apps.calculators import valuation_engines as engine
    from apps.calculators.valuation_examples import PROFILE_EXAMPLES

    workbook = root / "Owner's Earning/Project 2 - Listed Companies and Valuation/Project 2 - Listed Companies Owner Earnings and Valuation.xlsx"
    cached = openpyxl.load_workbook(workbook, data_only=True)
    formulas = openpyxl.load_workbook(workbook, data_only=False)
    checks = []

    def check(name, actual, expected, locator):
        assert isinstance(expected, (int, float)), (name, 'Missing cached/source value', expected)
        assert math.isclose(actual, expected, rel_tol=1e-10, abs_tol=1e-10), (name, actual, expected)
        checks.append(dict(name=name, actual=actual, expected=expected, workbook_locator=locator))

    values = {}
    keys = ('cash', 'cash_shock', 'reinvestment', 'reinvestment_shock', 'claims', 'claims_shock')
    for i, profile in enumerate(PROFILE_EXAMPLES):
        row = i + 7
        for col, key in enumerate(keys, 5):
            expected = cached['Profile Stress'].cell(row, col).value
            if 'shock' in key:
                expected *= 100
            check(f'Profile {i+1}: {key}', profile[key], expected, f'Profile Stress!{openpyxl.utils.get_column_letter(col)}{row}')
            values[f'p{i}_{key}'] = profile[key]
    rows = engine.profiles(values)['tables'][0]['raw']
    for i, result in enumerate(rows, 7):
        check(f'Profile row {i}: base', result[1], cached['Profile Stress'][f'K{i}'].value, f'Profile Stress!K{i}')
        check(f'Profile row {i}: downside', result[5], cached['Profile Stress'][f'L{i}'].value, f'Profile Stress!L{i}')

    asset = cached['Asset Heavy']
    project = dict(project_cost=asset['D13'].value, revenue=asset['D14'].value,
                   operating_cost=asset['D15'].value, renewal=asset['D16'].value,
                   revenue_shock=-10, cost_overrun=15, total_capex=300, maintenance=150, growth=100)
    result = engine.reinvestment(project)['tables'][0]['raw'][0]
    check('Stabilized contribution', result[4], asset['D17'].value, 'Asset Heavy!D17')
    check('Stabilized yield (%)', result[6], asset['D18'].value*100, 'Asset Heavy!D18')

    bank = cached['Bank Insurance']
    result = engine.bank(dict(capital=bank['D16'].value, rwa=bank['D17'].value,
                             earnings=bank['D18'].value, dividend=bank['D19'].value,
                             rwa_growth=bank['D20'].value*100, minimum_ratio=15, buffer=3,
                             loss=0, liquidity=25, legal_limit=25))
    rows = dict(result['tables'][0]['raw'])
    check('Closing bank capital ratio (%)', rows['Closing capital ratio (%)'], bank['D22'].value*100, 'Bank Insurance!D22')
    check('Bank headroom after dividend', rows['Capital headroom after proposed dividend'], bank['D23'].value, 'Bank Insurance!D23')

    locators = [('Asset Heavy', 'D17'), ('Asset Heavy', 'D18'), ('Bank Insurance', 'D22'), ('Bank Insurance', 'D23')]
    locators += [('Profile Stress', f'{column}{row}') for row in range(7,16) for column in ('K','L')]
    report = dict(status='passed', checks_count=len(checks), workbook=str(workbook.relative_to(root)),
                  workbook_sha256=hashlib.sha256(workbook.read_bytes()).hexdigest(),
                  method='Compare pure web functions with workbook inputs, cached results and recorded formulas; no XLSX modifications or live issuer retrieval.',
                  limits='Cached values are cross-checked for these selected cases; this is not a full workbook audit or validation of issuer estimates.',
                  formulas={f'{sheet}!{cell}':formulas[sheet][cell].value for sheet,cell in locators}, checks=checks)
    output = root / args.report
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'report':str(output)}))


if __name__ == '__main__':
    main()
