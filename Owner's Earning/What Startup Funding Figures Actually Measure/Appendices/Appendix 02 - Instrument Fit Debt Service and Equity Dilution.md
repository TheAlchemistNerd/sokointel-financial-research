# Appendix 02 — Instrument fit, debt service and equity dilution

### Companion to Part 02

This appendix reproduces the workbook's hypothetical financing comparison. The assumptions do not describe a named Kenyan company, actual lender offer or locally available market rate. Replace them with the signed facility or term sheet, bank receipts and a dated cash forecast before using the calculations for a decision.

## A2.1 Equal-principal KSh100 million loan

Assume a borrower receives KSh100 million, pays 18% annual interest, repays over 24 months in equal monthly principal installments, and pays interest monthly on opening principal. Fees, taxes, insurance, grace periods, arrears and prepayment are excluded.

Monthly scheduled principal is:

`KSh100m / 24 = KSh4.1667m`

Month-one interest and service are:

`KSh100m × 18% / 12 = KSh1.5m interest`

`KSh4.1667m principal + KSh1.5m interest = KSh5.6667m service`

Because the principal declines evenly, the sum of monthly opening balances is KSh1,250 million-months. Total interest is therefore:

`18% / 12 × KSh1,250m = KSh18.75m`

Total scheduled cash repayment is KSh118.75 million: KSh100 million of principal plus KSh18.75 million of interest. That is not the full effective borrowing cost if commitment, arrangement, legal, security, insurance or monitoring fees apply. If fees are deducted up front, the borrower receives less than KSh100 million while still owing the contracted principal.

Suppose monthly cash flow available for debt service (CFADS) is KSh6.2 million. Base month-one debt-service coverage is:

`KSh6.2m / KSh5.6667m = 1.094×`

The workbook combines two downside assumptions to show how modest-looking changes can breach coverage: a 20% CFADS haircut reduces CFADS to KSh4.96 million, while a rate shock from 18% to 23% raises month-one service to approximately KSh6.0833 million. Stressed month-one coverage becomes:

`KSh4.96m / KSh6.0833m = 0.815×`, or about **0.82×**.

Coverage below 1.0× means modeled CFADS is insufficient for that period's scheduled service. It is not a probability of default, and it does not account for liquidity reserves, taxes, maintenance, covenant definitions or refinancing. The right next question is which receipts arrive before each due date and whether cash can be lawfully applied to debt service.

## A2.2 Match the instrument to the funded asset

| Funding type | Cash-flow fit to test | Typical contract evidence |
|---|---|---|
| Equity | Long, uncertain path before cash generation; no scheduled principal | Share class, valuation, rights, option pool, liquidation priority and dilution |
| Term or venture debt | Predictable cash source with enough coverage on each due date | Draw conditions, rate, fees, security, repayment schedule, maturity and covenants |
| Asset finance or lease | Asset life and cash generation should extend beyond scheduled payments | Title, residual, useful life, service obligations, guarantees and repossession rights |
| Receivables facility | Eligible invoices and collections should support the borrowing base | Customer concentration, disputes, reserves, dilution, recourse and waterfall |
| Grant | Milestones and restricted budget should match eligible uses | Disbursement schedule, matching funds, audit, permitted costs and clawback |
| Supplier or customer credit | Delivery, payment and refund dates should not create a hidden cash gap | Contract terms, discount loss, penalties, restricted deposits and refunds |

The `Instrument Guide` sheet is a diligence prompt. It does not assume that any transaction in the Africa funding trackers follows a standard form. Facility documents determine the actual borrower, security, cost and claim priority.

## A2.3 Equity dilution cases

For a KSh30 million primary investment at KSh120 million pre-money:

`Post-money = KSh120m + KSh30m = KSh150m`

`New investor ownership = KSh30m / KSh150m = 20%`

For the alternative comparison in Part 2, a KSh100 million investment at KSh400 million pre-money also gives a simplified 20%:

`KSh100m / (KSh400m + KSh100m) = 20%`

At a hypothetical KSh1 billion exit, a 20% pro-rata share would correspond to KSh200 million of gross value before preferences, later dilution, taxes, transaction costs or other share classes. This does not mean the equity investment earns a guaranteed 2× return. The exit value and timing are uncertain, and the investor may receive a different amount under the actual liquidation waterfall.

Debt and equity are not directly comparable by setting the interest rate beside a hypothetical exit multiple. Debt's claim is scheduled and may be secured; equity is residual and absorbs losses after senior claims. Compare the same funded activity over several operating and exit outcomes, including delayed collections, lower prices, maintenance expense and the possible need for another round.

## A2.4 Reproduce the workbook example

On `Debt Service`, the blue inputs set principal, annual base and stress rates, tenor, CFADS and the downside haircut. Monthly scheduled principal is equal; interest uses each month's opening balance. The 24 rows calculate base and stressed service, CFADS coverage and closing principal. The Checks sheet verifies KSh100 million principal, KSh18.75 million base interest and the article's 20% dilution arithmetic.

On `Equity Dilution`, the pre-money and investment cells drive post-money ownership. The second row adds the explicitly hypothetical KSh1 billion exit so a reader can see gross pro-rata proceeds. It is not a company valuation or a forecast. `Deal Ledger` remains empty until source material identifies a specific recipient and instrument.

## Sources

1. A. M. Robb and D. T. Robinson, “The Capital Structure Decisions of New Firms,” *Review of Financial Studies*, vol. 27, no. 1, pp. 153–179, 2014, https://doi.org/10.1093/rfs/hhs072.
2. R. A. Cole and T. Sokolyk, “Debt Financing, Survival, and Growth of Start-up Firms,” *Journal of Corporate Finance*, vol. 50, pp. 609–625, 2018, https://doi.org/10.1016/j.jcorpfin.2017.10.013.
3. A. N. Berger and G. F. Udell, “The Economics of Small Business Finance: The Roles of Private Equity and Debt Markets in the Financial Growth Cycle,” *Journal of Banking & Finance*, vol. 22, nos. 6–8, pp. 613–673, 1998, https://doi.org/10.1016/S0378-4266(98)00038-7.
4. G. de Rassenfosse and T. Fischer, “Venture Debt Financing: Determinants of the Lending Decision,” *Strategic Entrepreneurship Journal*, vol. 10, no. 3, 2016, https://doi.org/10.1002/sej.1220.
