# Owner Earnings Project 2: pricing, treasury and distributable capital

**25 September 2026 · New project destination for the two-paste review**

## 1. Why Project 2 belongs in this review

Project 1 asks what an operating-business owner can safely draw or commit. Project 2 follows the different claims held by investors in listed operating companies, banks and insurers. The pricing and treasury material is directly relevant to these claims: funding cost, repricing, recoveries, capital retention and cash restrictions determine how business activity reaches shareholders.

The [README](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 2 - Listed Companies and Valuation/README.md>) reports five drafts and a workbook built on 24 September. It describes a filing bridge, asset-heavy screen, simplified bank-capital illustration, issuer evidence matrix and normalized stress cases. These are useful existing assets. A full issuer-specific valuation or distributable-capital model remains a further deliverable. The workbook file was located; its cells were not audited here.

## 2. Placement across Parts 6–10

| Destination | Already developed | Useful additional treatment |
|---|---|---|
| [Part 6](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 2 - Listed Companies and Valuation/Part 06 - Reconstructing Owner Earnings from Public Filings.md>) and Appendix 1 | Reconciled cash, financing claims, valuation and per-share evidence | A dictionary connecting each quantity to its entity, date, currency, cash-flow claim and discount basis |
| [Part 7](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 2 - Listed Companies and Valuation/Part 07 - US Technology and Asset Light Economics NVIDIA.md>) | Timed supply commitments, cancellation rights, customer demand and per-share dilution | One obligation-to-cash ladder and a common demand/receivable/funding stress |
| [Part 8](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 2 - Listed Companies and Valuation/Part 08 - Asset Heavy Issuers and Data Centre Infrastructure.md>) | Maintenance, construction, utilization, contracts, debt and the difference between yield and IRR | A full construction-to-operation cash calendar and a debt/equity funding waterfall |
| [Part 9](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 2 - Listed Companies and Valuation/Part 09 - Banks and Insurers Distributable Capital.md>) | Bank normalized earnings and capital; insurer claims, service results and remittance constraints | Separate bank and insurer numerical cases, with funding, losses and payout dates |
| [Part 10](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 2 - Listed Companies and Valuation/Part 10 - NSE Cross Sector Casebook.md>) | Seven distinct issuer approaches and evidence requirements | One dated, evidenced cash/capital bridge per sector, retaining its own units and claim definition |

Part 9 is the principal destination; Part 8 is the second. Parts 6, 7 and 10 provide the interfaces. This assessment is based on full reads of Parts 8–9 and Appendices 1–4; selected detailed passages of Parts 6, 7 and 10; and the full README. It is not a claim to have reread all five articles line by line.

## 3. The bank case: from loan economics to payout capacity

The current Part 9 already distinguishes a bank from an industrial business and develops normalized earnings, capital and residual-income/dividend approaches. Add a worked bridge after “Turn capital into an explicit distribution test.”

Start with dated average loan balances, yields, fees, deposit and wholesale funding costs, operating expenses and credit costs. Use consistent periods and separate reported accounting earnings from a normalized forecasting assumption. Reconcile the loan-level pricing model to the bank forecast. A notional economic-capital charge used in pricing is not a cash payment, and the allocation is not automatically the bank's regulatory-capital requirement.

For each capital constraint, project eligible capital **before the proposed dividend**, with the scenario's profit, losses and other eligible movements. Compare it with the capital needed for the scenario's balance sheet after distribution. Apply the relevant tier, risk-weighted asset, leverage and other tests individually when implementing a real institution's model.

### Hypothetical single-constraint illustration

All values below are invented monetary units, not current regulatory thresholds or a named bank's forecast. Assume one eligible-capital measure and an illustrative 18% target including the chosen buffer.

| Item | Base case | Higher-loss case |
|---|---:|---:|
| Opening eligible capital | 100 | 100 |
| Eligible after-tax profit before dividend | 20 | 12 |
| Other eligible capital movements | 0 | 0 |
| Capital before dividend | 120 | 112 |
| Closing risk-weighted assets before payout | 560 | 560 |
| Assumed target capital, 18% × 560 | 100.8 | 100.8 |
| Capital capacity for dividend | 19.2 | 11.2 |
| Assumed cash capacity for dividend | 14 | 14 |
| **Upper bound under these two tests** | **14** | **11.2** |

The higher-loss case reduces eligible profit by 8. That loss already reduces capital and is not deducted again as a second identical stress allowance. Real losses could also change RWA, funding and liquidity; they are held constant here to isolate the mechanism. Legal distributable reserves, other capital tests, approvals and entity restrictions may lower the bound further. A proposed dividend remains a decision, not the arithmetic maximum.

For valuation, connect sustainable equity distributions or residual earnings to the equity claim. Retained capital is part of the reinvestment needed to support growth; an industrial EBITDA-minus-capex shortcut is unsuitable for this case. [Damodaran's financial-services value drivers](https://pages.stern.nyu.edu/adamodar/New_Home_Page/littlebook/bankvaluedriver.htm) offer the conceptual bridge; local requirements and entity data determine the implemented constraints.

**Draft paragraph:** A loan book can grow while dividend capacity tightens. Funding may reprice faster than assets, collections may weaken and the expanding balance sheet may require more capital. Follow these movements from lending income through losses and retained capital before carrying a dividend forward. The investor needs to know both what the bank earns and what it must keep to continue earning it.

## 4. The insurer case: local obligations and parent cash

Part 9 already separates insurance service, investment/finance results, claims, reserves, reinsurance and paying entities. Add a two-ledger example after the discussion of insurer cash reaching shareholders.

**Ledger A — operating insurance entity:** premium and investment receipts; claims, acquisition and operating payments; reinsurance settlements; assets and liabilities; local liquidity and capital tests; permitted remittance and actual payment date.

**Ledger B — parent company:** opening unrestricted cash; remittances received; parent expenses and debt; other restrictions and the chosen liquidity floor; proposed shareholder distribution. The parent needs the local calculation's result, not a second subtraction of the same claims.

### Hypothetical timing illustration

Assume a subsidiary's completed local tests permit a remittance of 12, expected to settle at the parent on day 90. Parent opening cash is 3, parent obligations of 4 fall due on day 60, and its assumed minimum balance is 2. Before remittance, cash would be −1 and the gap to the chosen floor is 3. Over the full period, `3 + 12 − 4 − 2 = 9` appears available above the floor **only if the timing gap has been resolved**. Any bridge repayment, interest or additional obligations must be included. An eventual remittance does not fund an earlier obligation automatically.

IFRS 17 presents insurance service separately from insurance finance effects and recognizes profit as insurance services are provided. The contractual service margin captures unearned profit; it is not a parent cash balance. Use the accounting roll-forward to explain earnings, and the cash/capital ledgers to explain distributions. [IFRS Foundation overview](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/).

**Draft paragraph:** An insurer's reported profit has a route to travel before shareholders can receive cash. Claims and operating payments occur in particular entities, reinsurance may settle later, and local capital and liquidity requirements can limit a subsidiary's remittance. The parent must then meet its own obligations. A useful distribution forecast follows those transfers and dates alongside the accounting result.

Bayesian frequency/severity or recovery models can improve estimates entering these schedules where suitable data exist. They do not replace the contractual, accounting or capital bridge. Retain the Bayesian relativities paper as the home for those derivations and cross-reference the application here.

## 5. Asset-heavy and commitment cases

Part 8 and Appendix 2 already distinguish the hypothetical 8.5% stabilized contribution yield from project IRR and from an issuer valuation. The next exhibit should preserve that introductory calculation and extend it with dates:

- Construction spending, equity subscriptions and debt drawdowns.
- Interest during construction, fees and any capitalisation convention, keeping cash and accounting views reconcilable.
- Commissioning, utilization ramp, customer billing and collection.
- Operating cost, maintenance and separately identified growth commitments.
- Tax, debt service, reserve movements and distributable equity cash.
- Completion delay, power cost, customer-payment delay and refinancing scenarios that can occur together.

Calculate unlevered project and levered equity returns from their respective cash flows. Pair each discounted value with the appropriate claim and discount basis. Debt-service coverage requires the facility's defined cash numerator; a reserve-funded instalment should remain visible as liquidity support. LLCR, if used, needs a specified loan-life cash perimeter and discount convention.

Part 7's commitment schedule can use the same dated-record structure, while retaining technology-specific cancellation rights and inventory/customer-demand relationships. A project SPV adds legal ownership, servicing and waterfall constraints; it does not make a holding-company dividend or bank-capital calculation interchangeable with project cash.

## 6. Quantity dictionary and the workbench connection

| Quantity | Required distinction |
|---|---|
| Borrower rate | Contractual benchmark, spread, fees, reset and day count |
| Bank funding allocation | Institution-specific transfer price and maturity/behavioural assumptions |
| Regulatory and economic capital | Different purposes, definitions, estimation methods and constraints |
| Operating/project cash versus equity cash | Which financing claims have already been deducted |
| Insurer service result and parent cash | Accounting period, legal entity, claims and settlement dates |
| Discount curve or required return | Currency, valuation date, cash-flow risk, claim and method |
| Forecast default/loss and market-implied credit quantities | Estimation objective, probability measure and calibration evidence |

These fields extend the existing SokoIntel calculation/provenance idea. The next specification can give every result an entity, currency, unit, horizon, method version, source status and assumption set. Benchmark observations, lending spreads, a funding curve and an equity required return have distinct uses; none becomes a universal discount input simply because it is expressed as a percentage.

## 7. Deliverables to catalogue for future work

1. **Bank worksheet:** pricing-to-earnings reconciliation, eligible-capital roll-forward, liquidity/payout constraints and loss/funding scenarios.
2. **Insurer worksheet:** local claims/reinsurance/capital schedule and dated parent remittance bridge.
3. **Asset-heavy worksheet:** construction, operational ramp, financing, reserves and equity cash, extending the existing yield screen.
4. **Sector evidence cards:** one supported dated bridge per selected issuer before comparison with dividends or valuation.
5. **Shared calculation contract:** quantity dictionary, scenario IDs, reconciliations and evidence status for later SokoIntel implementation.

These are specific extensions to the present project. Keep the existing normalized stress scenarios as teaching material; their indices are neither money nor a common ranking of bank, insurer and operating-company value. Numerical issuer results require fresh filings and applicable rules. This review introduces no new company valuation, bank target or regulatory interpretation.

See the [central follow-up](<C:/Users/Nevo/Downloads/insuretech & embedded finance/output/pricing_treasury_cross_project_review_2026-09-23/06_BUSINESS_CREDIT_AND_OWNER_EARNINGS_FOLLOWUP_2026-09-25.md>) and the [original catalogue](<C:/Users/Nevo/Downloads/insuretech & embedded finance/output/pricing_treasury_cross_project_review_2026-09-23/01_USEFUL_MATERIAL_CATALOGUE.md>). The cumulative screenshot catalogue remains deferred. Canonical manuscripts and workbooks are preserved.
