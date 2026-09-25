# Appendix 02 — Technology, working capital and asset-heavy reinvestment

### Companion to Project 2, Parts 7 and 8

A high accounting return does not show how much cash can leave a business. Technology companies can consume capital through inventory, receivables, research and commitments; infrastructure operators consume capital through replacement cycles, construction, power and leases. The examples below separate filed data from arithmetic and clearly marked assumptions.

## A2.1 NVIDIA FY2026: a bridge, not a valuation

NVIDIA's Form 10-K for the fiscal year ended 25 January 2026 reports net income of $120.067bn, stock-based compensation expense of $6.386bn, depreciation and amortization of $2.843bn and capital expenditures of $6.100bn [1]. A mechanical subtotal is:

The rounded MD&A figure has a useful cross-statement reconciliation. The cash-flow statement reports $6.042bn of purchases related to property, equipment and intangible assets under investing activities and $0.101bn of principal payments on those assets under financing activities. Their $6.143bn sum rounds to the $6.1bn management disclosure [1]. Keep the original statement classifications intact when reproducing cash flow. This arithmetic does not establish an identical definition between the two disclosures, nor does it split maintenance from growth investment.

`$120.067bn + $6.386bn + $2.843bn − $6.100bn = $123.196bn`.

The subtotal is not operating cash flow, free cash flow or owner earnings. It adds back SBC without pricing its dilution or replacement cost, leaves working-capital movements and other accruals out, and assumes all reported capex can be deducted as if it were the only reinvestment needed. Those are unresolved choices, not rounding issues.

The same filing identifies $15.399bn of cash use from receivables and $11.324bn of cash use from inventory, net of acquisitions [1]. Subtracting only those two lines from the subtotal gives $96.473bn, but this remains incomplete: accounts payable and other operating liabilities may offset some use; other current assets, taxes, acquisitions and noncash reconciling items also matter. The correct first task is to reproduce the 10-K cash-flow statement line by line and tie beginning to ending cash. The second is to replace one year's working-capital movements with an explicitly supported normalized operating cycle.

### SBC treatments that avoid double counting

Two internally consistent treatments are possible:

1. **Expense-and-dilution view:** keep the reported compensation expense in earnings, then forecast diluted shares from awards, vesting, exercises, withholding and repurchases. Do not add SBC back to owner cash and also deduct the same modeled dilution a second time without explaining the relationship.
2. **Cash-cost view:** add back the noncash expense to the cash-flow starting point, then deduct an explicit amount needed to replace employee compensation through cash, buybacks or other economic cost. Explain the horizon and share-price assumptions.

The appropriate method depends on the question and available data. Reported repurchases are not automatically a one-for-one SBC offset: they may serve several capital-allocation purposes and may occur at prices different from grant-date values. Show share count and cash separately.

### Research and development and supplier commitments

R&D is an expense in the income statement and a cash outflow when paid. An analyst may leave all R&D expense in earnings or estimate a portion as an investment with a useful life and amortization schedule. Either approach requires consistent treatment of new spending, historical amortization and future growth. Lev and Sougiannis study the capitalization and value relevance of R&D under their sample and method; that result is not permission to reclassify every research dollar as a durable asset [2].

Purchase commitments and supply reservations are not all current-period capex. Record amount, counterparty, due date, cancellation or change terms, expected inventory or service received, and whether the obligation appears in the filing. A commitment can become a cash use before a customer pays, even if it has not yet appeared as property expenditure. Model committed uses by date and stress a demand or margin decline against inventory already ordered.

## A2.2 Asset-heavy infrastructure: separate the project from the existing service

Part 8's fictional data-centre proposal assumes KES 10bn of construction and equipment cash over two years, stabilized annual revenue of KES 1.8bn, cash operating cost of KES 800m and annual renewal spending of KES 150m. These are invented inputs, not Equinix data or sector benchmarks.

| Case | Annual revenue | Operating cash costs | Renewal | Stabilized contribution | Capital base | Simple stabilized yield |
|---|---:|---:|---:|---:|---:|---:|
| Stated base | KES 1.80bn | KES 0.80bn | KES 0.15bn | KES 0.85bn | KES 10.0bn | 8.50% |
| Revenue 10% lower; costs held flat | 1.62bn | 0.80bn | 0.15bn | 0.67bn | 10.0bn | 6.70% |
| Construction cost 15% higher | 1.80bn | 0.80bn | 0.15bn | 0.85bn | 11.5bn | 7.39% |
| Both stresses together | 1.62bn | 0.80bn | 0.15bn | 0.67bn | 11.5bn | 5.83% |

The yield is only `stabilized annual contribution ÷ stated project cost`. It omits the two-year construction timing, partial occupancy, utility connection, funding cost, tax, working capital, central overhead, lease classification, commissioning risk and terminal value. It is not an IRR or payback period. A decision model should place each construction payment and customer receipt in the period it is expected, then calculate the cash trough, financing requirement, and project return under base and downside schedules. A six-month commissioning delay shifts receipts and may add carrying costs even if stabilized margins are unchanged.

For an existing asset, classify spending by the service it preserves. Replacement cost can differ from accounting depreciation when economic depreciation is not geometric or equipment is exposed to changing replacement prices [3]. The analyst should tie a claimed maintenance amount to capacity utilization, failure and outage records, useful life, parts availability, customer service level and current quotes. If these inputs are private, report an unresolved maintenance estimate rather than assigning an arbitrary percentage of total capex.

## A2.3 Applying the bridge to Equinix

The FY2025 Form 10-K is the primary source for reported revenue, property and equipment, depreciation, cash flows, leases, construction commitments and management-defined measures [4]. The analyst should transcribe at least three comparable years and preserve the issuer's definition of recurring capex or AFFO before recasting it. For each year, reconcile:

1. reported operating cash flow to cash from operations after working-capital movements;
2. total property and equipment additions to construction, expansion, recurring replacement and acquisitions where disclosed;
3. management's non-GAAP measure to GAAP net income and cash flow, with each adjustment listed;
4. leases, debt, equity issuance and dividends to cash available at the parent; and
5. commissioned capacity and customer contracts to power availability, utilization and collected cash.

The filing does not necessarily provide enough evidence to allocate every property dollar between maintenance and expansion. The current Project 2 workbook therefore keeps a reported-issuer evidence screen and a separate fictional project case. It does not publish an Equinix maintenance-capex range or a normalized issuer owner-earnings number. The distinction is intentional and should remain visible until project schedules or better disclosure support an estimate.

### References

[1] NVIDIA Corporation, *Form 10-K for the fiscal year ended January 25, 2026*, filed February 25, 2026, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm.

[2] B. Lev and T. Sougiannis, “The Capitalization, Amortization, and Value-Relevance of R&D,” *Journal of Accounting and Economics*, vol. 21, no. 1, pp. 107–138, 1996, https://doi.org/10.1016/0165-4101(95)00410-6.

[3] D. Livdan and A. Nezlobin, “Investment, Capital Stock, and Replacement Cost of Assets When Economic Depreciation Is Non-Geometric,” *Journal of Financial Economics*, vol. 142, no. 3, pp. 1444–1469, 2021, https://doi.org/10.1016/j.jfineco.2021.05.021.

[4] Equinix, Inc., *Form 10-K for the year ended December 31, 2025*, filed February 11, 2026, https://www.sec.gov/Archives/edgar/data/1101239/000110123926000032/eqix-20251231.htm.
