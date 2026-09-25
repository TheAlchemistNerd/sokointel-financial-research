# Appendix 01 — A reproducible retrospective and warning test

### Companion to Project 3, Part 11

A retrospective has two questions that must not be merged: what a decision-maker could know at a date, and what later records reveal about the outcome. This appendix defines a practical procedure, a testable warning, and the limits of any score. It does not provide a calibrated failure probability for Kenyan SMEs or startups.

## A1.1 Preserve the information set at each date

For every proposed warning, record both the date the underlying event happened and the date the information became accessible to the actor being assessed. An internal management account may be known to the finance team but not an outside investor. An administrator's later report can explain a realization but cannot be put into an earlier lender's information set unless it was already public.

| Field | Record |
|---|---|
| Entity | Exact debtor, employer, asset owner, contracting party or parent |
| Signal date | Period in which the underlying cash or operating change occurred |
| Available date | When the person or institution could reasonably access it |
| Source and custodian | Filing, bank ledger, contract, board paper, court record or report |
| Measurement | Amount, unit, denominator, currency and calculation |
| Claim status | Filed fact, court order, party assertion, management statement, secondary report, estimate or unresolved |
| Decision owner | Who could act, under which authority and contract |
| Action window | Time from available date to due obligation or consequence |
| Alternative explanation | Seasonality, planned growth, acquisition, FX, disputed delivery, one-off payment or data error |
| Missing evidence | The document that would confirm, reject or narrow the interpretation |

Write the contemporaneous conclusion before opening later outcome records where possible. Then add a separate retrospective update. Fischhoff's classic experiments show that knowing an outcome can bias judgments of what was foreseeable [1]. The practical safeguard is a dated evidence cut-off and a preserved first-pass assessment, not a claim that analysts can eliminate all hindsight bias.

## A1.2 Convert an indicator into an action

A warning is actionable only when it specifies a measurement, threshold or trigger, responsible person, next action, deadline, and response if the first action fails. For example: “The largest overdue invoices exceed six weeks of payroll” is a trigger only if the business calculated those amounts from its own payroll and ledger. It should then identify who calls the buyer, what credit may be paused, how accepted delivery is evidenced, and when the cash forecast is refreshed. A ratio without an action owner is a dashboard observation.

Use different classes of signal:

- **Cash and claims:** unrestricted cash, dated payables, payroll, tax, debt maturity, restricted cash and payment holds.
- **Operating cycle:** invoice collection, stock ageing, stock-outs, returns, supplier lead times, customer deposits and overdue payables.
- **Unit contribution:** revenue net of returns and variable costs, by customer, route, product or store.
- **Funding quality:** amount announced, committed, closed, drawn, received, restricted, repaid or converted; legal recipient and date.
- **Governance and control:** who can authorize transfers, access accounts, renew a licence, approve credit or replace a key operator.

Working-capital measures should be calculated from ledger data, not a single year-end ratio. DSO, DIO, DPO and the cash-conversion cycle can locate where cash is tied up, but their levels depend on business model, credit terms, season, accounting classification and supplier behavior. Published distress studies use defined samples, labels and horizons; they cannot be transplanted as a Kenyan private-company score [2], [3].

## A1.3 Test the warning against false alarms and missed cases

If a researcher evaluates a rule over a cohort, define the entity, observation date, forecast horizon and distress outcome before counting results. For a binary alert:

| | Distress within stated horizon | No distress within horizon |
|---|---:|---:|
| Alert raised | True positive (TP) | False positive (FP) |
| No alert | False negative (FN) | True negative (TN) |

Common descriptive metrics are:

- `Precision = TP ÷ (TP + FP)`: among alerts, how many were followed by the defined outcome?
- `Recall = TP ÷ (TP + FN)`: among defined outcomes, how many had a prior alert?
- `False-positive rate = FP ÷ (FP + TN)`: among non-events, how often did the rule alert?

A useful evaluation also counts the lead time between alert and event, the action available, the amount at risk and the cost of acting. Precision can look high when the sample contains many distressed entities or the outcome is defined broadly. Survivorship, missing private-company records, censoring and inconsistent “failure” labels can distort every metric. If there is no adequate cohort, report case-level tests and do not print these rates as though validated.

Shumway's hazard-model work treats the timing of bankruptcy as information and discusses time-varying predictors [2]. Campbell, Hilscher and Szilagyi analyze public-company distress risk with accounting and market data [3]. Neither study calibrates the Owner's Earning workbook's warning fields. Merton's contingent-claims framework needs asset value, volatility and debt structure that are usually unavailable for private Kenyan operators [4].

## A1.4 Worked decision-date case from the article

Part 11 presents a fictional distributor with KSh 6.0m unrestricted cash, KSh 12.0m of invoices expected in the next month, and KSh 9.4m of payroll, supplier, tax and debt obligations. A KSh 4.0m invoice is disputed and historically late. The 13-week forecast's minimum is KSh 0.3m in week five.

The available-cash-to-disputed-receipt comparison is `KSh 4.0m ÷ KSh 6.0m = 66.7%`. This is a concentration measure, not a default probability. The obligations total `2.4 + 5.0 + 0.8 + 1.2 = KSh 9.4m`. If all KSh 12.0m of receipts clear by the relevant dates, the undiscounted arithmetic after those listed uses is KSh 8.6m; if the disputed KSh 4.0m does not clear, it is KSh 4.6m. Neither result replaces the weekly schedule, because the article's week-five trough depends on dates and other outflows not summarized in those totals. The practical alert is that a specific disputed invoice must clear before a specific supplier or payroll trough—or the business must take an action that does not assume it will.

## A1.5 Source-to-workbook map

The Project 3 workbook's `Timeline`, `Evidence Ledger`, `Warnings and Actions`, `Cash and CCC`, and `Sources and Checks` tabs implement parts of this protocol. The cash schedule is a fictional teaching case. The workbook does not reconstruct Nakumatt, Tuskys, Twiga or Copia historical monthly cash, and it does not calculate a validated alert score. Those would require contemporaneous management accounts, bank records, contracts, verified claims and a comparable event dataset.

### References

[1] B. Fischhoff, “Hindsight Is Not Equal to Foresight: The Effect of Outcome Knowledge on Judgment Under Uncertainty,” *Journal of Experimental Psychology: Human Perception and Performance*, vol. 1, no. 3, pp. 288–299, 1975, https://doi.org/10.1037/0096-1523.1.3.288.

[2] T. Shumway, “Forecasting Bankruptcy More Accurately: A Simple Hazard Model,” *The Journal of Business*, vol. 74, no. 1, pp. 101–124, 2001, https://doi.org/10.1086/209665.

[3] J. Y. Campbell, J. Hilscher, and J. Szilagyi, “In Search of Distress Risk,” *The Journal of Finance*, vol. 63, no. 6, pp. 2899–2939, 2008, https://doi.org/10.1111/j.1540-6261.2008.01416.x.

[4] R. A. C. Merton, “On the Pricing of Corporate Debt: The Risk Structure of Interest Rates,” *The Journal of Finance*, vol. 29, no. 2, pp. 449–470, 1974, https://doi.org/10.1111/j.1540-6261.1974.tb03058.x.
