from pathlib import Path
import re

ROOT = Path(r"C:\Users\Nevo\Downloads\financial material")
KENYA = ROOT / "Kenyan Equities and Company Analysis" / "Four Part Series"
RESEARCH = KENYA / "Research"

p1 = KENYA / "Part 1 - Building an Income and Research Universe.md"
p2 = KENYA / "Part 2 - Reading Businesses and Estimating Value.md"
coverage = RESEARCH / "Research Questions and Coverage.md"
value_map = ROOT / "NSE Value Investing and Dividend Growth" / "NSE Value Investing Material Map.md"

text = p1.read_text(encoding="utf-8")
old = """KCB provides a concrete illustration of why ordinary and special distributions need separate columns. Its published schedule identifies KES 4 per share of ordinary distributions and KES 3 of special distributions for fiscal 2025 [2]. At an illustrative KES 65 entry price, ordinary yield is approximately 6.15%, while the combined amount produces approximately 10.77%. Both calculations describe something useful, but they answer different questions. The first provides a starting point for evaluating recurring income. The second describes the distributions associated with that fiscal year. A forward budget can begin with an explicit ordinary-dividend assumption and add any separately justified special payment. That structure makes it easy to test how the household's income changes when a special distribution ends, while preserving the value of understanding the company's complete capital-return record."""
new = """KCB provides a dated company case for why ordinary and special distributions need separate columns. Its published schedule identifies KES 4 per share of ordinary distributions and KES 3 of special distributions for fiscal 2025 [2]. The Nairobi Securities Exchange daily price list recorded a KES 94 volume-weighted average price on 11 September 2026 [3]. On that dated observation, ordinary yield is approximately 4.26%, while the combined fiscal-year amount produces approximately 7.45%. Both calculations describe something useful, but they answer different questions. The first provides a starting point for evaluating recurring income. The second describes the distributions associated with that fiscal year. A forward budget can begin with an explicit ordinary-dividend assumption and add any separately justified special payment. That structure makes it easy to test how the household's income changes when a special distribution ends, while preserving the value of understanding the company's complete capital-return record."""
if old not in text:
    raise SystemExit("Part 1 KCB paragraph was not found")
text = text.replace(old, new)
body, refs = text.split("## References", 1)
def shift_citation(match):
    number = int(match.group(1))
    return f"[{number + 1}]" if number >= 3 else match.group(0)
body = re.sub(r"\[(\d+)\]", shift_citation, body)
refs = re.sub(r"(?m)^\[(\d+)\]", shift_citation, refs)
insert = """[3] Nairobi Securities Exchange, “Daily Price List, 11 September 2026”. [Online]. Available: <https://www.nse.co.ke/wp-content/uploads/11-SEP-26.pdf>. Accessed: Sep. 12, 2026.\n\n"""
refs = refs.replace("\n[4]", "\n" + insert + "[4]", 1)
p1.write_text(body + "## References" + refs, encoding="utf-8")

text = p2.read_text(encoding="utf-8")
old = """Valuation begins by asking what the investor expects to receive and what return compensates for committing money to that opportunity. For the fictional manufacturer, the workbook forecasts operating cash available to all capital providers after tax and reinvestment, then discounts those cash flows at a matching required return. A terminal calculation represents the business beyond the explicit forecast. Cash and nonoperating assets are added where appropriate, debt and other claims are deducted, and the result is divided by shares. The appendix contains the detailed discounted-cash-flow formulas and every step of the worked example. The article's practical focus is the set of business assumptions behind them: sales, margins, tax, working capital, productive investment, financing, and the returns the company can earn as it moves towards a more mature operating pattern."""
new = """Valuation begins by asking what the investor expects to receive and what return compensates for committing money to that opportunity. BAT Kenya supplies a dated nonfinancial case rather than a fictional manufacturer. Its FY2025 annual report recorded revenue of KES 23,191.945 million, EBIT of KES 7,474.835 million, operating cash flow of KES 6,633.154 million, capital expenditure of KES 301.833 million and earnings per share of KES 52.46 [10]. The NSE daily price list recorded a KES 560 volume-weighted average price on 11 September 2026 [11]. These reported values establish the operating scale and the price observation. They do not establish a target price.

| BAT Kenya FY2025 evidence | Reported value | Use in the case |
| --- | ---: | --- |
| Revenue | KES 23,191.945 million | Starting scale for the explicit operating scenario |
| EBIT | KES 7,474.835 million | Margin and after-tax operating-profit bridge |
| Operating cash flow | KES 6,633.154 million | Cash-conversion cross-check |
| Capital expenditure | KES 301.833 million | Reinvestment starting point |
| Fiscal dividend per share | KES 70.00 | Distribution-quality and payout discussion |
| Earnings per share | KES 52.46 | Payout and ownership-claim cross-check |
| NSE VWAP, 11 September 2026 | KES 560.00 | Dated price observation, not a guaranteed execution price |

The workbook forecasts operating cash available to all capital providers after tax and reinvestment, then discounts those cash flows at a matching required return. Its five forward years use stated assumptions for revenue growth, EBIT margin, working-capital days, capital expenditure, tax, required return and terminal return on invested capital. They are teaching scenarios calibrated from the FY2025 evidence, not BAT guidance, forecasts, or a recommendation. A terminal calculation represents the business beyond the explicit forecast. Cash and nonoperating assets are added where appropriate, debt and other claims are deducted, and the result is divided by shares. The appendix contains the detailed discounted-cash-flow formulas and every step of the worked case. The practical focus is the set of business assumptions behind them: sales, margins, tax, working capital, productive investment, financing, and the returns the company can earn as it moves towards a more mature operating pattern."""
if old not in text:
    raise SystemExit("Part 2 fictional-manufacturer paragraph was not found")
text = text.replace(old, new)
text = text.replace("In the workbook, a 4% perpetual growth assumption and a 16% return on new capital imply retaining 25% of after-tax operating profit for reinvestment.", "In the BAT Kenya case workbook, the base scenario uses a 3% perpetual growth assumption and an 18% return on new capital, implying that approximately 16.67% of after-tax operating profit is retained for reinvestment in the terminal period.")
references = """\n[10] BAT Kenya PLC, “Combined Annual and Sustainability Report 2025”, 2026. [Online]. Available: <https://www.batkenya.com/content/dam/endmarkets/ke/en/download/investors-and-reporting/annual-reports/BATK_Combined_Annual_and_Sustainability_Report_2025.pdf>. Accessed: Sep. 12, 2026.\n\n[11] Nairobi Securities Exchange, “Daily Price List, 11 September 2026”. [Online]. Available: <https://www.nse.co.ke/wp-content/uploads/11-SEP-26.pdf>. Accessed: Sep. 12, 2026.\n"""
if "[10] BAT Kenya PLC" not in text:
    text = text.rstrip() + references + "\n"
p2.write_text(text, encoding="utf-8")

text = coverage.read_text(encoding="utf-8")
old = """The source manuscripts supply the thematic scope. Current factual claims are supported by the linked research sources; the articles stand on their own. Company-specific projections beyond the dated dividend examples are developed through explicitly fictional teaching cases so that the accounting and valuation relationships can be examined directly."""
new = """The source manuscripts supply the thematic scope. Current factual claims are supported by the linked research sources; the articles stand on their own. The completed company cases use BAT Kenya, Equity Group Holdings and Jubilee Holdings with a dated source ledger. Company-specific projections are explicit teaching scenarios calibrated from the reported period. They are not issuer guidance, current market forecasts, target prices, or investment recommendations."""
if old not in text:
    raise SystemExit("Coverage conclusion was not found")
coverage.write_text(text.replace(old, new), encoding="utf-8")

ledger = """# Actual Company Evidence Ledger

## Scope and retrieval record

This ledger is the publication-facing companion to `real_company_source_ledger.json`. It records the reported data, price observations, source documents, units and intended use for the actual-company cases in the Kenyan Equities and Company Analysis series. It separates reported information from forward valuation assumptions.

Research cutoff: 12 September 2026. Financial-statement figures are in KES millions unless stated otherwise. The price convention is the NSE daily volume-weighted average price. It is an observation for the stated date, not a closing bid or offer, an executable order price, or a valuation conclusion.

| Company | Reported period | Evidence used | Dated market observation | Article use |
| --- | --- | --- | --- | --- |
| BAT Kenya PLC | FY2025, year ended 31 December 2025 | Revenue 23,191.945; EBIT 7,474.835; operating cash flow 6,633.154; capex 301.833; EPS KES 52.46; fiscal DPS KES 70.00 | KES 560.00 VWAP, 11 September 2026 | Part 1 payout quality; Part 2 connected DCF scenario |
| Equity Group Holdings PLC | FY2025, year ended 31 December 2025 | Profit attributable 71,964; attributable equity 309,505; EPS KES 19.07; DPS KES 5.75; gross amortised loans 943,453; Stage 3 loans 99,561 | KES 102.00 VWAP, 11 September 2026 | Part 2 bank capital, DDM and price-to-book cross-checks; Part 3 allocation universe |
| Jubilee Holdings Ltd. | FY2025, year ended 31 December 2025 | Profit attributable 5,781.962; attributable equity 53,768.889; DPS KES 15.00 | KES 412.75 VWAP, 11 September 2026 | Part 2 insurance and ownership-claim analysis; Part 3 allocation universe |
| KCB Group PLC | FY2025, year ended 31 December 2025 | Ordinary DPS KES 4.00; special DPS KES 3.00 | KES 94.00 VWAP, 11 September 2026 | Part 1 recurring-versus-special dividend case; Part 3 allocation universe |

## Source and extraction method

| Evidence class | Primary source | Retrieval and transformation | Control |
| --- | --- | --- | --- |
| BAT Kenya financial statements | BAT Kenya, *Combined Annual and Sustainability Report 2025* | Named statement and note tables checked in PDF text. KES-thousand disclosures divided by 1,000 where necessary. | FY2025 reported values remain separate from all forward scenario inputs. |
| Equity Group financial statements | Equity Group Holdings, *2025 Integrated Report and Financial Statements* | Group and attributable ownership labels recorded with the reported period. Bank-capital data identified at the regulated subsidiary where applicable. | Do not combine group equity with a subsidiary regulatory ratio without a stated bridge. |
| Jubilee financial statements | Jubilee Holdings, *2025 Annual Integrated Report* | Attributable profit and equity identified from the group report and translated from KES thousands to KES millions. | Insurance service, investment and finance effects stay distinct in the analysis. |
| Market prices and volumes | Nairobi Securities Exchange, *Daily Price List, 11 September 2026* | Image-only PDF rendered for inspection. VWAP and daily volume recorded by counter. | Do not relabel VWAP as close, last trade, bid, offer, or guaranteed fill. |

## Scenario boundary

The BAT Kenya DCF, the Equity Group DDM and price-to-book cross-check, and the portfolio expected-return and volatility inputs are educational scenarios. The ledger supplies the factual starting point. Assumptions are stored separately in `real_company_inputs.json` and calculated results in `real_company_results.json`. A scenario must be changed when its operating, capital, tax, price, liquidity or required-return assumption changes.

## References

[1] BAT Kenya PLC, “Combined Annual and Sustainability Report 2025”, 2026. [Online]. Available: <https://www.batkenya.com/content/dam/endmarkets/ke/en/download/investors-and-reporting/annual-reports/BATK_Combined_Annual_and_Sustainability_Report_2025.pdf>. Accessed: Sep. 12, 2026.

[2] Equity Group Holdings PLC, “2025 Integrated Report and Financial Statements”, 2026. [Online]. Available: <https://equitygroupholdings.com/wp-content/uploads/2026/06/Equity-Group-Holdings-PLC-2025-Integrated-Report-and-Financial-Statements.pdf>. Accessed: Sep. 12, 2026.

[3] Jubilee Holdings Ltd., “2025 Annual Integrated Report”, 2026. [Online]. Available: <https://jubileeinsurance.com/group/wp-content/uploads/2026/06/Jubilee-Holdings-2025-Annual-Integrated-Report.pdf>. Accessed: Sep. 12, 2026.

[4] Nairobi Securities Exchange, “Daily Price List, 11 September 2026”, 2026. [Online]. Available: <https://www.nse.co.ke/wp-content/uploads/11-SEP-26.pdf>. Accessed: Sep. 12, 2026.

[5] KCB Group PLC, “Dividends”. [Online]. Available: <https://kcbgroup.com/dividends>. Accessed: Sep. 12, 2026.
"""
(RESEARCH / "Actual Company Evidence Ledger.md").write_text(ledger, encoding="utf-8")

text = value_map.read_text(encoding="utf-8")
text = text.replace("## Deletion decision\n\nThe concepts are now retained in the two surviving projects. The source folder should remain until the Kenyan-equities actual-company evidence set and source ledger are complete, because its named-counter prompts can still help scope that work. After that evidence review, the folder can be removed without losing an unrecorded research concept.", "## Reconciliation status\n\nThe concepts have now been retained in the dividend-growth and Kenyan-equities projects. The Kenyan Equities actual-company evidence set is recorded in `Four Part Series/Research/Actual Company Evidence Ledger.md`, with official issuer reports and the dated NSE price-list observation separated from scenario assumptions. The Value Investing folder is therefore an audit archive, not a required published source. It is retained for traceability and may be removed later without losing an unrecorded research concept.")
value_map.write_text(text, encoding="utf-8")

reconciliation = """# NSE, Kenyan Equities, and Value Investing Reconciliation

## Decision

The three folders are not three competing versions of the same article. The completed structure keeps the dividend-growth project intact, uses the Kenyan Equities series for issuer and portfolio analysis, and treats the earlier Value Investing material as an archived source whose unique concepts have been retained.

| Project | Reader question | Retained role | Material not duplicated |
| --- | --- | --- | --- |
| NSE Dividend Growth Project 2026 | How can an investor build, fund and review a Kenyan dividend-oriented core and watchlist? | DCA implementation, dividend cash-flow analysis, recurring-versus-special distributions, watchlist construction and contribution discipline. | It does not repeat full statement analysis or issuer valuation models. |
| Kenyan Equities and Company Analysis | How should an investor investigate an actual listed company, estimate value and combine holdings? | Financial statements, sector-specific analysis, BAT Kenya DCF scenario, Equity Group and Jubilee equity-value cross-checks, portfolio constraints and simulations. | It does not replace the dividend project’s step-by-step DCA programme. |
| NSE Value Investing and Dividend Growth | Which value-investing disciplines sharpen a Kenyan equity decision? | Archived source material. Circle of competence, value traps, margin of safety, cash conversion, DCF and sustainable-distribution concepts are embedded in Kenyan Equities Part 2. | Its earlier generic rules and dated claims are not reproduced as universal investment rules. |

## Actual-company boundary

The Kenyan Equities series now names actual issuers where evidence is used. BAT Kenya provides the nonfinancial cash-flow case. Equity Group provides the bank capital, dividend-discount and price-to-book cross-check. Jubilee provides the insurance and ownership-claim case. KCB supplies the ordinary-versus-special-dividend example. The evidence, source documents, units, observation dates and transformations are recorded in the Actual Company Evidence Ledger.

Reported results and dated price observations establish a research starting point. Forecasts, expected returns, required returns, terminal growth, margins, capital plans and portfolio risk inputs remain stated scenarios. This preserves the difference between evidence and judgement.

## Value Investing material retained

| Unique value-investing idea | Final destination | Reader outcome |
| --- | --- | --- |
| Understand the business before calculating a multiple | Kenyan Equities Part 2 | A research note begins with economics, financial statements and ownership claims. |
| Test value traps | Kenyan Equities Part 2 | Governance, capital allocation, liquidity and cash-conversion checks sit beside low-multiple analysis. |
| Use a margin of safety as a range, not a slogan | Kenyan Equities Part 2 | Base, weaker and stronger cases expose the assumptions supporting a valuation. |
| Match the valuation method to distributable economics | Kenyan Equities Part 2 | DCF, DDM and price-to-book methods are selected by business and capital structure. |
| Treat dividend income as a portfolio implementation problem | NSE Dividend Growth Parts 1 and 2 | The investor separates recurring from special distributions and manages contributions, watchlists and concentration. |

## Publishing rule

No folder is deleted by this reconciliation. The Value Investing folder is now clearly an audit archive. Its useful material has a published destination, while historical point-in-time figures remain excluded unless rebuilt from current primary sources.
"""
(RESEARCH / "NSE Kenyan Equities and Value Investing Reconciliation.md").write_text(reconciliation, encoding="utf-8")
print("Kenyan reconciliation and actual-company integration completed")