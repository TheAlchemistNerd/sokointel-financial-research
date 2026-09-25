# Appendix 01 — Rebuilding the owner cash claim

### Companion to Project 1, Parts 1, 2 and 4

This appendix makes the cash bridge in Part 1 reproducible and separates three numbers that answer different questions: cash generated during a reported period, normalized owner earnings, and cash that can safely be drawn on a particular date. Amounts in the workshop example are fictional KSh millions unless otherwise stated. They are teaching inputs, not a Kenyan business benchmark.

## A1.1 The bridge and its boundaries

For an operating business, define operating working capital consistently as:

`OWC = trade receivables + inventory + contract assets − trade payables − customer advances`.

Exclude bank cash, borrowings, tax balances, and interest balances unless the analysis explicitly brings them into the operating bridge. This avoids mixing operating investment with financing or owner claims. When OWC rises over a period, that increase generally uses cash; when it falls, cash is released. The direction and amount still need to be checked against write-offs, acquisitions, foreign exchange and reclassifications.

A simplified reconciliation beginning with net income is:

`Cash from operations = net income + noncash expenses − increase in OWC + other operating accrual and tax adjustments`.

It is a reconciliation identity only when all material adjustments are included. Adding depreciation and subtracting a change in receivables, stock and payables alone produces a **partial bridge**, not a filed CFO figure. For normalized owner earnings, a useful analytical form is:

`Normalized OE = normalized earnings + justified noncash charges − maintenance investment − incremental OWC required at the normalized activity level − other recurring cash claims`.

The last term can include the extra market cost of replacing work currently performed by an owner for below-market pay. It must not subtract the same wage twice. Berkshire's 1986 explanation emphasizes the cash that can be removed without impairing long-term competitive position or required working capital; it also warns that maintenance estimates can be difficult [1].

## A1.2 Recalculation of the workshop example

The article's illustrative balances and asset classifications produce this bridge:

| Step | Calculation | KSh million | Status |
|---|---:|---:|---|
| Reported net income after proprietor pay | Given | 1.800 | Fictional input |
| Add depreciation | Given | +0.240 | Noncash charge; not a cash receipt by itself |
| Receivables increase | 1.050 − 0.800 | −0.250 | Cash tied up |
| Inventory increase | 1.450 − 1.200 | −0.250 | Cash tied up |
| Trade payables increase | 0.830 − 0.700 | +0.130 | Temporary supplier funding |
| Partial cash from operations | 1.800 + 0.240 − 0.250 − 0.250 + 0.130 | 1.670 | Before other accruals and taxes not in the illustration |
| Total equipment cash paid | Given | −0.680 | Includes replacement and expansion |
| Historical cash after listed capex | 1.670 − 0.680 | 0.990 | Simplified period-cash proxy |

The incremental operating working capital use is KSh 370,000: KSh 250,000 of additional receivables plus KSh 250,000 of additional inventory, less KSh 130,000 of additional payables.

For a no-growth owner-earnings estimate, separate the KSh 680,000 equipment cash outflow into KSh 380,000 of supported replacement spending and KSh 300,000 for the additional service bay. The replacement-pay adjustment is KSh 300,000 because the KSh 900,000 currently expensed for the proprietor's work is KSh 300,000 below the stated KSh 1.2 million market replacement cost. Therefore:

`1.800 + 0.240 − 0.380 − 0.370 − 0.300 = KSh 0.990 million`.

The article's earlier KSh 1.29 million amount is the intermediate result before the replacement-pay gap is deducted. The corrected final estimate is KSh 990,000. It coincides with the historical cash-after-capex proxy only because the KSh 300,000 expansion outlay and KSh 300,000 replacement-pay adjustment happen to be equal. That coincidence is not a reconciliation rule. If the owner's work is already paid at market rates, remove the replacement-pay adjustment; if the growth bay is acquired, test its cash return as a separate investment decision.

This example is intentionally incomplete as a formal cash-flow statement: it supplies no separate tax, interest, other accrual, asset-sale, debt-principal or acquisition data. The 1.67m amount must therefore remain a partial operating-cash estimate. A real business should reconcile it to bank statements and the accounting cash-flow statement before using it for a lender, tax filing or transaction.

## A1.3 Earnings do not authorize a draw

The same business has KSh 1.2m in bank cash and the following near-term uses:

| Dated use | KSh thousand |
|---|---:|
| Payroll | 250 |
| Critical suppliers | 260 |
| Rent and utilities | 80 |
| Tax | 90 |
| Loan principal | 100 |
| Completion cost on a prepaid order | 130 |
| Total listed uses | 910 |
| Chosen minimum reserve | 150 |
| Provisional headroom | `1,200 − 910 − 150 = 140` |

KSh 140,000 is only a provisional ceiling against the listed items. The forecast still needs due dates, supplier criticality, the order's gross margin, unlisted obligations and receipts. If KSh 200,000 of disputed receivables was mistakenly treated as cash when arriving at the KSh 1.2m balance, corrected cash would be KSh 1.0m and headroom would be negative KSh 60,000. A high normalized annual earning estimate cannot repair a cash shortfall next week.

A practical distribution ceiling is:

`Draw ceiling = max(0, cash available on each forecast date − essential due payments − restricted cash − chosen reserve)`.

Take the minimum headroom over the forecast horizon, not just today's closing balance. Model uncertain receipts on expected dates and create a downside case for disputed or concentrated customers. Set the reserve against a named response time or risk—such as payroll and critical supplier cover—not an unexplained fixed percentage.

## A1.4 Controls for applying the calculation

1. Match entity, currency and accounting period across profit, balance-sheet changes and capital spending.
2. Tie opening and closing cash to bank reconciliations; reconcile payment processors and mobile-money accounts separately.
3. Trace large noncash adjustments to notes and remove acquisition, disposal and FX effects before calling them recurring.
4. Support maintenance with asset history, service requirements and current quotes; do not substitute depreciation mechanically.
5. Measure working capital at comparable activity and season points. A year-end movement can hide a seasonal trough.
6. Keep contractual restrictions, tax due, debt principal, owner draws and growth investments visible after the owner-earnings estimate.
7. Revisit the model when prices, volumes, credit terms, asset reliability or customer mix change.

Working-capital studies find associations between receivable, inventory and payable policies and firm performance in specific samples; they do not establish a universal target for a Kenyan enterprise [2], [3]. The point of the bridge is to identify the firm's own cash conversion and test a decision against evidence, not to turn an academic coefficient into a policy threshold.

## A1.5 Reproduction and source note

All arithmetic in Table A1.1 follows from the fictional figures stated in Part 1. Change one balance or assumption and recompute the bridge; do not carry the KSh 990,000 result to another business. The companion workbook's `Article Case` tab now reproduces the workshop bridge and dated draw-headroom figures; `Owner Earnings` holds a separate larger-scale editable scenario, while `Cash13W`, `Working Capital` and `Sources and Checks` support the operating analysis. The appendix still shows the complete calculation so it can be audited without opening the file.

### References

[1] Berkshire Hathaway, “Chairman’s Letter — 1986,” section “Sources of Reported Earnings,” https://www.berkshirehathaway.com/letters/1986.html.

[2] M. Deloof, “Does Working Capital Management Affect Profitability of Belgian Firms?” *Journal of Business Finance & Accounting*, vol. 30, nos. 3–4, pp. 573–588, 2003, https://doi.org/10.1111/1468-5957.00008.

[3] P. J. García-Teruel and P. Martínez-Solano, “Effects of Working Capital Management on SME Profitability,” *International Journal of Managerial Finance*, vol. 3, no. 2, pp. 164–177, 2007, https://doi.org/10.1108/17439130710738718.
