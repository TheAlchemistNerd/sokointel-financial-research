# Appendix 02 — Maintenance, working capital and the weekly cash clock

### Companion to Project 1, Parts 2 and 3

This appendix turns the article's maintenance and cash-cycle discussion into an operating worksheet specification. It distinguishes the amount of cash a business needs to preserve a given level of service from cash required to expand. No single ratio below is a safe threshold; definitions, periods and ledgers must match.

## A2.1 Estimating maintenance investment from service requirements

Depreciation is an accounting allocation. It may lag current replacement cost, use an estimated useful life that differs from actual service life, and include assets with different maintenance requirements. Total capital expenditure also combines replacement, compliance and capacity expansion. A decision-useful register identifies the asset, operating job, current condition, repair history, expected replacement date, lead time, quote, capacity impact and evidence confidence.

For each proposed spend, record the purpose and counterfactual:

| Classification | Test question | Evidence to retain |
|---|---|---|
| Routine maintenance | What repairs and service keep current output safe and reliable? | Work orders, service contracts, failure log |
| Replacement | What exhausted asset must be renewed to preserve present capacity? | Asset register, quote, commissioning record |
| Compliance | What spend is required to keep the current business legally or contractually able to trade? | Regulation, inspection, customer requirement |
| Growth or improvement | What new volume, site, quality or service does the project add? | Capacity plan, customer demand, project cash flows |

A mixed project should be split only where vendor schedules or engineering evidence support the allocation. Where a refrigeration project has replacement and expansion elements but the invoice does not separate them, carry a range and explain what quotation or inspection would resolve it. Do not use a low historical spend as proof that maintenance is low if work has been deferred. Research on capital investment and economic depreciation supports treating asset replacement cost as a distinct question from reported depreciation [1].

## A2.2 The working-capital bridge

Use matched opening and closing balances:

`ΔOWC = Δreceivables + Δinventory + Δcontract assets − Δtrade payables − Δcustomer advances`.

A positive result is a cash use in the period, all else equal. For a forecast, model the balance needed to support planned activity, rather than blindly repeating last year's balance change. Reconcile write-offs, returns, VAT, supplier rebates, foreign exchange, acquisitions and non-trade balances separately.

Common operating indicators are:

- `DSO = average trade receivables ÷ credit sales × days in period`.
- `DIO = average inventory ÷ cost of goods sold × days in period`.
- `DPO = average trade payables ÷ credit purchases × days in period`.
- `CCC = DSO + DIO − DPO`.

Use credit sales rather than total revenue where cash sales are material; use purchases rather than cost of sales when the payable base is more closely related to purchases. Average balances should span the period. A year-end snapshot can be distorted by seasonal buying or deliberate payment timing. A lower CCC is not automatically healthier if it comes from overdue supplier invoices, lost safety stock or customer terms that damage sales. Empirical working-capital studies report sample-specific relationships with profitability and financing constraints, not a universal target [2]–[4].

## A2.3 Worked sensitivity from the wholesaler example

Part 3 describes monthly sales increasing from KSh 4.0m to KSh 4.8m, average collection moving from 30 to 45 days, and an additional KSh 450,000 of stock. The case does not state the proportion of sales made on credit or the payable movement, so a single historical cash requirement cannot be claimed. A transparent sensitivity can still be calculated.

Assume a 30-day month and that the full KSh 4.8m of monthly sales is on credit. Moving from 30 to 45 collection days increases the receivable investment by approximately:

`KSh 4.8m ÷ 30 × 15 = KSh 2.4m`.

If only a fraction `q` of monthly revenue is on credit, the approximate increment is `KSh 2.4m × q`: KSh 1.2m at 50% credit sales, KSh 1.8m at 75%, and KSh 2.4m at 100%. Add the KSh 450,000 of stock only as a separate inventory movement. If incremental payables and customer advances are zero, the combined estimated funding need ranges from KSh 1.65m at 50% credit sales to KSh 2.85m at 100%. If payables rise by KSh 300,000 on agreed terms, subtract that amount from the corresponding cash need; do not count overdue amounts as sustainable funding without a supplier-specific review.

This is a steady-state approximation. It assumes monthly credit sales are uniform, all new sales are collectible, balances reflect the stated days, and there are no returns, seasonality, VAT timing, bad debts or stock obsolescence. It is a sensitivity for asking better questions—not a substitute for invoice-level ageing and a weekly cash forecast.

## A2.4 The 13-week forecast

For each week `t`, model:

`Closing cash(t) = opening unrestricted cash(t) + receipts likely to clear(t) + committed financing(t) − dated cash payments(t)`

and set `opening cash(t+1) = closing cash(t)`. Keep financing draws apart from customer receipts and identify restrictions on cash. Show the weekly minimum, the first week below the reserve, the shortfall amount and the assumptions that cause it. A financing facility belongs in the base case only if it is committed, drawable under current conditions and available before the obligation falls due.

| Forecast line | Input unit | Evidence required | Downside treatment |
|---|---|---|---|
| Customer collections | Invoice and date | Invoice, delivery proof, payment history, dispute status | Delay disputed/large buyer; haircut only with a stated basis |
| Stock and direct purchases | Order and due date | Purchase order, lead time, sell-through, supplier terms | Add required deposits or lost terms |
| Payroll and statutory payments | Legal due date | Payroll register and filing calendar | Do not defer legally due items without advice |
| Rent, utilities and critical service | Contract date | Lease, utility notice, service contract | Include deposit, arrears and shut-off exposure |
| Debt service | Contract schedule | Facility agreement and current statement | Include covenant-triggered repayment or fee only if supported |
| Capital spending | Milestone date | Quote, project approval, safety requirement | Delay discretionary growth; retain necessary replacement |

A rolling review should update actuals, explain variances, preserve the previous forecast and assign a person and due date to each action. Gross burn includes cash operating payments; net burn includes operating receipts. If net burn is zero or positive, runway should be reported as “not meaningful under this simple burn formula,” then forecast as dated cash flows instead. Growth spending, one-offs, owner withdrawals, financing receipts and overdue payables should not disappear inside one monthly net number.

## A2.5 Inventory and supplier actions

An inventory action needs the item, units, age, sales velocity, gross contribution, supplier return rights, lead time, spoilage risk and effect on customer service. ABC ranking by annual usage value can prioritize control, but it does not replace age or criticality: a low-value spare may stop a high-value service. Reorder points should reflect demand during lead time plus a justified safety buffer; the buffer should follow observed variability and service commitments, not an imported percentage.

Accounts-payable ageing should separate not-yet-due amounts, agreed extensions, disputed invoices and overdue balances. DPO is a descriptive ratio, not permission to miss contractual dates. Before delaying a payment, quantify the short-term cash released, fee or discount lost, supply interruption risk and effect on future terms. This makes the operating workbook useful to a real buyer, owner and supplier conversation.

### References

[1] D. Livdan and A. Nezlobin, “Investment, Capital Stock, and Replacement Cost of Assets When Economic Depreciation Is Non-Geometric,” *Journal of Financial Economics*, vol. 142, no. 3, pp. 1444–1469, 2021, https://doi.org/10.1016/j.jfineco.2021.05.021.

[2] M. Deloof, “Does Working Capital Management Affect Profitability of Belgian Firms?” *Journal of Business Finance & Accounting*, vol. 30, nos. 3–4, pp. 573–588, 2003, https://doi.org/10.1111/1468-5957.00008.

[3] P. J. García-Teruel and P. Martínez-Solano, “Effects of Working Capital Management on SME Profitability,” *International Journal of Managerial Finance*, vol. 3, no. 2, pp. 164–177, 2007, https://doi.org/10.1108/17439130710738718.

[4] G. A. Afrifa, “Net Working Capital, Cash Flow and Performance of UK SMEs,” *Review of Accounting and Finance*, vol. 15, no. 1, pp. 21–44, 2016, https://doi.org/10.1108/RAF-02-2015-0031.
