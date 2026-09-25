# Appendix 01 — From the filed statement to an equity claim

### Companion to Project 2, Parts 6 and 10

The purpose of this appendix is to make the public-filing method repeatable while showing why a filed cash figure is not yet an owner-earnings estimate or a share value. The worked company values below are the dated figures already cited in Part 6 from BAT Kenya's audited FY2025 report. Derived percentages are the appendix author's arithmetic; they are not company-reported ratios or estimates of maintenance spending.

## A1.1 Lock the source perimeter first

Before calculation, record legal issuer, consolidated or separate statements, reporting date, comparative years, currency, unit, audit opinion, filing date, page/note and URL. Preserve original statement signs. A cash-flow statement often displays cash uses in parentheses, while an analyst table may use positive uses and subtract them. Document the convention before linking formulas.

For each year, capture at minimum:

- profit attributable to ordinary equity holders, tax and finance costs;
- depreciation, amortisation, impairment and share-based compensation;
- cash from operations and each material working-capital line;
- property, plant and equipment and intangible additions, disposals and acquisitions;
- debt drawn and repaid, lease payments, dividends and share-count movements;
- cash, restricted cash, investments and non-controlling interests; and
- notes that explain segment, exceptional, related-party, commitment or accounting changes.

A filing-to-cash bridge should reconcile from the selected starting line to reported CFO, then from CFO to cash after capital spending and financing. Do not start with CFO and subtract that period's working-capital outflow a second time. Do not add back share-based compensation without an explicit dilution, replacement-cost or share-repurchase treatment. Dechow, Kothari and Watts document how accrual earnings and cash flows have different persistence and timing properties; that supports reconciling the two, not selecting whichever is higher [1].

## A1.2 BAT Kenya FY2025: reported facts and derived checks

The article cites audited FY2025 revenue of KES 23,191.945 million, EBIT of KES 7,474.835 million, operating cash flow of KES 6,633.154 million, capital expenditure of KES 301.833 million and EPS of KES 52.46 [2]. Arithmetic checks are:

| Measure | Calculation | Result | What it says |
|---|---:|---:|---|
| EBIT margin | 7,474.835 ÷ 23,191.945 | 32.23% | Reported EBIT relative to revenue; not owner cash |
| CFO margin | 6,633.154 ÷ 23,191.945 | 28.60% | Reported CFO relative to revenue; working capital is already reflected in CFO |
| Capex / revenue | 301.833 ÷ 23,191.945 | 1.30% | Total reported capex intensity; does not identify maintenance share |
| CFO less reported capex | 6,633.154 − 301.833 | KES 6,331.321m | Arithmetic subtotal before other claims; not distributable cash |

The model cannot infer maintenance from the last line. To estimate owner earnings, inspect multiple years of additions and depreciation, asset-by-asset replacement needs, compliance projects and capacity changes. Trace material project additions to the PPE note or management discussion. If the report does not identify purpose or service requirement, leave maintenance as a supported range only if evidence supports its endpoints; otherwise mark it unavailable. A placeholder such as “50% of capex” creates numerical precision without analytical evidence.

The five data items above are a reported-year snapshot. They are not a five-year time series, an earnings forecast or a dividend recommendation. A robust next pass should transcribe each comparable year separately, explain accounting-policy and perimeter changes, and compare cycle-normalized volumes and prices. Where the filing does not explain cash conversion or maintenance, the work product should show the exact missing note, asset schedule or management record required to proceed.

## A1.3 Build the owner-earnings range without double counting

Choose one starting point and keep its cash-flow perimeter consistent:

**Starting with earnings:**

`Owner earnings ≈ normalized after-tax operating earnings + justified noncash charges − maintenance investment − normalized increase in operating working capital − other recurring operating claims`.

**Starting with CFO:**

`Cash after investment ≈ reported CFO − cash maintenance and growth investment − acquisitions and other selected cash uses`.

If reported CFO is used, the actual-period working-capital change is already in it. A normalized adjustment may replace that actual movement with a sustainable working-capital requirement, but it must be shown as a bridge from actual to normalized—not silently removed or deducted again. State whether interest is included, whether leases are treated as debt, and whether the measure is unlevered or levered.

Present a range only where each bound has evidence. For example, a low case can use a documented imminent replacement program and a high case a documented multi-year normalized replacement cycle. If only total capex is disclosed and asset records are unavailable, “not estimable from public disclosure” is a valid finding. Livdan and Nezlobin's analysis of non-geometric economic depreciation shows why economic investment and accounting depreciation need not track mechanically [3].

## A1.4 Per-share claim and valuation gates

After deriving a normalized company cash range, ask which claim it represents. Reconcile enterprise value to equity by subtracting interest-bearing debt and debt-like obligations, adding only excess unrestricted cash and non-operating assets, and accounting for non-controlling claims. Use diluted shares appropriate to the valuation date. If the cash flow is to all capital providers, discount at a consistent weighted cost of capital and move from enterprise value to equity. If the cash flow is to equity holders after financing, use an equity discount rate and do not subtract debt twice.

A simple discounted-cash-flow frame is:

`Equity value = present value of forecast equity cash flows + present value of terminal value`.

The terminal value should not conceal the maintenance or reinvestment assumption. Show sensitivity to discount rate, terminal growth, normalized margin, maintenance and working-capital requirement. For residual-income analysis, Ohlson's framework links value to book value and expected residual earnings under specific accounting and forecasting assumptions [4]. It is a cross-check, not a way to bypass weak earnings or book-value quality.

Do not publish a per-share value while a required input is missing or stale. Price, diluted share count, maintenance range, debt and cash must be tied to a date. Record the output as “not calculated” rather than an illustrative valuation range if the required evidence is absent.

## A1.5 Workbook map and reproduction note

The Project 2 workbook's `Filing Inputs`, `NVDA Bridge`, `Assumptions`, `Valuation` and `Sources and Checks` tabs illustrate this workflow. They do not constitute multi-year bridges for every issuer in Part 10. A reviewer should be able to trace each red/source value to a filing and each calculated value to an exposed formula. This appendix reproduces the BAT arithmetic explicitly; recomputing the ratio columns from the five inputs above is sufficient to verify them.

### References

[1] P. M. Dechow, S. P. Kothari, and R. L. Watts, “The Relation Between Earnings and Cash Flows,” *Journal of Accounting and Economics*, vol. 25, no. 2, pp. 133–168, 1998, https://doi.org/10.1016/S0165-4101(98)00020-2.

[2] BAT Kenya PLC, *Combined Annual and Sustainability Report 2025*, https://www.batkenya.com/content/dam/endmarkets/ke/en/download/investors-and-reporting/annual-reports/BATK_Combined_Annual_and_Sustainability_Report_2025.pdf.

[3] D. Livdan and A. Nezlobin, “Investment, Capital Stock, and Replacement Cost of Assets When Economic Depreciation Is Non-Geometric,” *Journal of Financial Economics*, vol. 142, no. 3, pp. 1444–1469, 2021, https://doi.org/10.1016/j.jfineco.2021.05.021.

[4] J. A. Ohlson, “Earnings, Book Values, and Dividends in Equity Valuation,” *Contemporary Accounting Research*, vol. 11, no. 2, pp. 661–687, 1995, https://doi.org/10.1111/j.1911-3846.1995.tb00461.x.
