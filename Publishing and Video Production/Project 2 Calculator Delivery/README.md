# Project 2 calculator delivery — 25 September 2026

Internal research-to-product release record. The seven public tools are implemented and locally validated in the sibling SokoIntel website repository. Deployment is a separate step. None of the architecture review documents belongs in the public research catalogue.

## Research and tool connections

| Research | Public route under `/calculators/valuation/` | Calculation and boundary |
|---|---|---|
| Parts 6–7, Appendix 01 and Appendix 02 | `earnings-bridge/` | Profit-to-CFO reconciliation, normalized operating working capital, maintenance range and two alternative SBC conventions. Separate growth, principal and reserve uses; not automatic dividend permission. |
| Part 8, Appendix 02, `Asset Heavy!D13:D18` | `reinvestment/` | Stabilized contribution, revenue stress and cost overrun; separate annual capital-budget classification. Simple yield is not IRR. |
| Part 7, Appendix 02 | `sbc-dilution/` | Compensation treatment, issued shares and actual repurchases; opening/closing denominator sensitivity is not reported EPS. |
| Parts 6 and 10, Appendix 01, `Valuation!C16:G25` | `equity-value/` | Five-year equity cash flow, terminal value, sensitivity and price-implied growth. Required reinvestment and financing must already be reflected in the equity cash claim; no second debt subtraction. |
| Part 9, Appendix 03, `Bank Insurance!D16:D23` | `bank-capital/` | Capital, incremental stress loss, RWA, retained buffer and separate liquidity/legal ceilings. One illustrative ratio, not a statutory solvency model. |
| Part 9, Appendix 03 and 25 September timing review | `insurer-remittances/` | Subsidiary capital/cash/permission limits, dated parent obligations and remittance, explicit bridge borrowing and repayment. A prior cash-reserve breach blocks distribution capacity. |
| Parts 7–10, Appendix 04, `Profile Stress!E7:L15` | `sector-stress/` | Nine editable normalized profiles. Compare each with its own base; these are not issuer valuations, current forecasts or a cross-sector ranking. |

All default cases are fictional. No SEC/NSE retrieval or API credentials are required. Public form inputs are not retained in profiles or lead lists. Existing single-asset DCA, portfolio DCA, compounding and cash-flow calculations were not changed.

## Numerical and presentation evidence

- [Workbook reconciliation](workbook-reconciliation.json): **76 checks** against selected inputs, cached results and recorded formulas. The unchanged XLSX hash is recorded. This is a selected-case reconciliation, not a full workbook audit.
- Website focused suite: **38 tests** covering all seven tools, security/input boundaries, independent valuation identities, reverse solver endpoints, units, source links and insurer timing.
- Website regression suite: **174 tests passed** across calculators, core and newsletter, including 13 title/sequence/repair tests. Tests use an isolated in-memory database. Edition automation was enabled only inside that test process so the existing queue tests retain their normal behavior; no production jobs are involved. Django reported no new migrations.
- [Browser verification](Browser%20QA/browser-qa.json): seven new tools plus existing DCF and simple credit at 1,365 and 390 pixels, **18 page/viewport combinations**. Actual submissions, desktop CSV downloads, TeX symbol rendering, invalid-rate rejection and JavaScript-disabled fallback passed. Wide numeric results scroll inside their container; mobile symbol definitions wrap.
- Screenshots in `Browser QA/` record the local preview, not the deployed website.

Reproduce from this research repository with Python plus `openpyxl`:

```powershell
python scripts/verify_project2_calculators.py --website '../business and technical website blog'
```

The [browser script](../../scripts/check_project2_browser.cjs) accepts an output folder and optional local origin. It requires Playwright and Edge; set `PLAYWRIGHT_MODULE` for another installation. The website's `scripts.project2_test_settings` uses an isolated SQLite database and disabled edition automation for previews.

### Reconciled examples

| Case | Checked result | Evidence status |
|---|---|---|
| Profit 100, D&A 10, SBC 8, other noncash 2, actual WC use 12 | Reconstructed CFO 108 | New fictional statement bridge |
| Normalized WC 15, maintenance 20; retain SBC expense | Both profit and CFO routes give 77 | New fictional bridge; replacement cost 9 instead gives 76 |
| Capital 10,000, revenue 1,800, cash costs 800, renewal 150 | Contribution 850; simple yield 8.5% | Matches workbook Asset Heavy |
| Bank capital 100, earnings 20, RWA 500 growing 12%, floor 18%, dividend 10 | Closing ratio 19.642857%; post-dividend headroom 9.2 | Matches workbook Bank Insurance; illustrative internal floor |
| Same bank; separate cash limit 14 | Pre-dividend capacity 14; earnings 12 instead gives 11.2 | Implements review's independent constraint example |
| Parent cash 3; obligation 4 on day 60; remittance 12 on day 90; reserve 2 | Earlier reserve gap 3; conditional closing headroom 9; distribution capacity 0 while unfunded | New dated example from internal review |
| Same parent; explicit opening bridge 3 repaid on day 90 | Gap removed; capacity 9 before any bridge cost | Financing is not counted as earnings |
| Equinix normalized profile | `90 − 54 − 27.5 = 8.5` | Correct workbook result; earlier appendix displayed 9.0 |

The canonical Appendix 04, its website source/asset copies and embedded catalogue appendices now show 8.5 with a dated correction note. File metadata has been updated. The workbook itself was not edited. Already-generated PDFs and episode decks have not been regenerated in this calculator milestone; affected editions should be refreshed through the normal versioned pipeline when scheduled, without a bulk worker queue.

## Archived Buffett prototype: reviewed before reuse

The [archived R Markdown research](<../../Owner's Earning/Source Imports/MM-Merton Framework Buffett Research/Buffett_Strategy_Research.rmd>) contains a `CompanyFactsParser` and `BuffettForensicAuditor`. Its source remains unchanged. The following function-level findings explain why no prototype scanner was promoted to the public calculator backend:

| Function | Finding | Current treatment / future requirement |
|---|---|---|
| `annual_series` | Collects alternate tags and groups by fiscal year/filed date; can merge different durations, contexts, units or comparable-period presentations. A calendar-frame filter is not a full fiscal-period reconciliation. | Manual same-period inputs now; future ingestion needs accession, start/end dates, unit, tag priority, amendments and as-of selection. |
| `latest_metrics` | Independently selects each metric's latest year, then labels the set with the maximum year. | Require a common period and entity perimeter; preserve unavailable fields. |
| `estimate_maintenance_capex` | Averages trailing total capex and depreciation; neither establishes the investment necessary to preserve a business. | Explicit low/base/high analyst estimates with evidence; no automatic maintenance proxy. |
| `owner_earnings` | Starts with net income and subtracts SBC, although the expense may already be included. Missing D&A/SBC becomes zero. | Keep the expense once, or replace it once with an explicit cost. Required input gaps are not zero-filled. |
| `working_capital_adjustment` | Uses receivables and inventory only; omits payables and other operating balances and may return zero for absent data. | Require a reconciled operating working-capital use, distinct from financing, and distinguish actual from normalized use. |
| `safe_divide` / `latest_growth` | Guard some missing/zero cases but do not resolve accounting comparability; change divided by absolute prior value needs explicit interpretation across losses. | Do not treat generic ratios as a validated issuer screen. |

Data download is an input stage. Multi-year evidence reconstruction, source-page lineage and sector-specific issuer models remain planned. [SEC API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) explains available filing data; it does not supply the required accounting judgments. [Berkshire's 1986 discussion](https://www.berkshirehathaway.com/letters/1986.html) motivates maintenance judgment rather than a universal payout formula.

## Internal next-work map

See the [46-document review and adoption plan](../../platform_operations_plans/2026-09-25_architecture_review/REVIEW_AND_ADOPTION_PLAN.md) for targeted article/workbook additions: dated facility schedules, construction and commissioning, bank pricing-to-capital, insurer remittance calendars and sourced sector bridges. Those are later controlled extensions, not claims that every company model is complete now.

The [LinkedIn positioning draft](../LinkedIn/SokoIntel%20-%20From%20Research%20to%20Enterprise%20Analytics.md) has 1,997 body words and remains a local draft. Internal architecture sources remain separate from that public-facing article. The enterprise destination remains C#, Excel-DNA, VSTO, ASP.NET/.NET and Azure, with Django publishing and membership as the distribution channel.
