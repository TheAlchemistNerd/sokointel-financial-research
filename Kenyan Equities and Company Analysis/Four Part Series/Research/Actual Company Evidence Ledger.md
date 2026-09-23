# Actual Company Evidence Ledger

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
