# Free calculator reconciliation and recording map

Milestone: 25 September 2026. Implementation and local acceptance complete; Git delivery and live deployment are distinct checks. This record covers four new free tools plus additive DCF explanation. It does not claim that the deferred PowerPoint or bulk PDF production has resumed.

## Routes and worked examples

| Tool | Public route | Workbook anchor | Default result / recording anchor |
| --- | --- | --- | --- |
| MSME owner earnings and cash headroom | `/calculators/owner-earnings/` | Project 1, Article Case D6:D38; the separate Owner Earnings sheet supplies the general bridge convention | Annual owner earnings KES 990,000; listed uses KES 910,000; provisional headroom KES 140,000; reviewed headroom KES -60,000 |
| Thirteen-week operating cash planner | `/calculators/cash-13-weeks/` | Project 1, Overview D6:D7 and Cash13W rows 6:18 | Base minimum KES 1,050,000 and final cash KES 1,950,000; downside final KES -6,650,000; reserve breach week 2, cash shortfall week 3 |
| Business cash stress and warning planner | `/calculators/failure-warning/` | Project 3, Overview D6:D7 and Cash and CCC rows 6:18 | Base minimum KES 5,580,000 and final KES 6,060,000; downside final KES -3,490,000; reserve breach week 8, cash shortfall week 9 |
| Detailed business credit and repayment planner | `/calculators/business-credit/detailed/` | Business Credit, P2 Facility B7:B14 / E7:E12 and Entity Review B5:B8 / rows 15:23 | Principal KES 520,000; interest KES 7,693.15; fees KES 10,400; finance cost KES 18,093.15; contribution after finance KES 261,906.85; 14-day collection delay leaves a KES 538,093.15 repayment-date gap |
| Existing DCF value explorer | `/calculators/dcf-value/` | Existing five-year web engine, retained; Kenyan Equities Part 2 and listed-company valuation companions | Default per-share value remains approximately KES 4.91; show forecast, terminal dependence and 5-by-5 WACC/terminal-growth sensitivity |

The new tools are anonymous, server-calculated forms. No membership or lead submission is required. Amber fields are editable. Scenario POST responses and CSV exports use `Cache-Control: no-store`; input values are not saved by these views. Browser form CSRF protection remains enabled. CSVs contain the calculated tables, not a saved editable workbook or full input audit trail. Keep the workbook for detailed evidence and repeatable scenarios.

## Source trace

All paths below are relative to the financial-research repository. The source workbooks were read, not modified. The platform's `apps/calculators/data/business_examples.json` stores the two weekly source paths, SHA-256 values, rows and cached baseline closing balances. Tests check all thirteen baseline closes for both models. The article-case and credit defaults are explicit form values with reconciliation tests.

| Source workbook | SHA-256 |
| --- | --- |
| `Owner's Earning/Project 1 - MSMEs and Small Businesses/Project 1 - MSME Owner Earnings and Operations.xlsx` | `43f243daa5fa87c914c73ec53b55652f96b8cbd8482d45327141c2383e47494e` |
| `Owner's Earning/Project 3 - Failure Retrospectives and Warning Systems/Project 3 - Failure Retrospectives and Warning Systems.xlsx` | `056c55f6d4b882fb99469e9092f4f4d1c930676a49b676b7c0dd5ad6e068b14e` |
| `African Markets and Business Credit/Workbook/African Markets and Business Credit - Credit Readiness and Cash Cycle Workbook.xlsx` | `0daf2a874e6e7834bc8ad0342c87b1f82492ac68619bcbbb589ee742f1bf9b36` |

## Reconciliation boundaries and formula map

**Owner earnings.** Normalized profit = reported after-tax/after-interest profit + owner pay already expensed - replacement labour + supported after-tax normalization. Owner earnings then adds justified noncash charges and deducts maintenance investment and increased required operating working capital. Debt principal, separate growth investment and reserve top-up are displayed below this annual measure. The default Article Case deliberately does not import the different general Owner Earnings-sheet scenario. In particular, the historical cash-after-total-capex proxy also happens to equal KES 990,000; that coincidence does not make it the same calculation.

The dated cash test is independent: cash plus additional collections, less listed due uses, restricted cash and reserve, then less any disputed amount mistakenly included in cash/collections. A KES 30,000 proposed withdrawal changes the default reviewed headroom from KES -60,000 to KES -90,000 without changing annual owner earnings. Avoid overlapping restricted/disputed deductions. Review intervening cash troughs in the weekly tool; a single horizon-end figure is not a legal distribution test.

**Weekly liquidity.** Closing cash = opening cash + operating receipts + owner financing + new borrowing - scheduled uses. Negative balances carry forward. The reserve funding requirement is the deepest reserve gap, including opening cash, not a sum of repeated negative balances. No automatic rescue funding is inserted. A weekly model does not prove that each payment clears within the week.

The first six weekly columns retain each workbook's customer receipts, supplier payments, payroll/fixed and other-committed totals. Additional operating receipts, owner funds, borrowing, tax, maintenance, growth, interest, principal and drawings are initially zero. When splitting an existing bucket, reduce it before entering the same use in a detailed category. Defaults are fictional and dated; they are not uploaded company records.

**Stress model.** Downside customer receipts and borrowing can be delayed; receipts after week 13 are disclosed. New borrowing can be excluded from the downside. Supplier payments can be moved earlier without changing their total. Extra stock purchases affect week 1 only. Margin compression adds weekly sales times the contribution-margin reduction to cash costs, assuming constant sales and immediately paid variable costs. Do not layer the same shock into both a stress control and an already revised input row. Inventory write-downs are not cash payments. Overdue supplier claims are evidence warnings; actual payments belong in dated rows.

CCC = inventory days + receivable days - payable days. These inputs are diagnostics and do not also post cash into the weekly schedule. The source's low/downside receipts already differ from the base case. Company names from the failure articles are not attached to fictional cash schedules. A reserve breach is not a probability of failure, an insolvency finding, or a creditor-recovery estimate.

**Credit timing.** Default day zero is the supplier-payment/financing point: workbook day 15. Collection is 30 days after draw, corresponding to workbook day 45. This translation preserves the base case. Fees use original principal; interest uses remaining principal and the selected Actual/360 or Actual/365 convention. Equal-principal instalments use rounded whole-day spacing; one instalment is a bullet. Withheld fees/interest reduce the advance once and are not charged again at repayment. The cash-flow annual yield discounts the displayed repayments to the actual net advance using 365 days; it is distinct from principal-based simple annualisation and is not a statutory APR.

The workbook's late-collection row extends financing from 30 to 44 days, increasing finance cost to KES 21,683.29. The web tool deliberately keeps the contract's original repayment date when the customer is late and displays the funding gap. To reproduce that workbook extension, select 44-day tenor, collection day 44 and no extra delay; this is an explicit revised facility assumption, not an automatic rollover. Default interest, refinancing and late penalties are not invented.

Break-even invoice revenue holds entered order costs and the facility unchanged and adds total financing cost. The account-credit evidence ledger is separate: KES 580,000 observed credits reconcile to KES 380,000 reviewed trading receipts, KES 140,000 non-operating credits and KES 60,000 unresolved. These amounts are not added again to the order cash schedule. A summary form does not resolve ownership or detect circular transfers; use the workbook ledger and source records.

**DCF.** The existing enterprise-valuation calculation is unchanged. New labels explicitly require FCFF before debt payments and a matching WACC; net debt is subtracted once. Forecast cash flows are at year end, with terminal value at year 5. The 5-by-5 sensitivity changes WACC and terminal growth while holding the first five forecast cash flows fixed; invalid combinations are labelled. Non-operating assets/claims outside the simple net-debt bridge and banks/insurers require other models. Do not insert after-interest MSME owner earnings into this FCFF formula.

Conceptual references: Buffett's owner-earnings discussion in [Berkshire's 1986 letter](https://www.berkshirehathaway.com/letters/1986.html); Damodaran's [valuation framework](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) and [terminal-value discussion](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/termvalapproaches.htm). The numerical examples above are the project's fictional workbook cases, not figures from those external sources.

## Article and episode recording map

| Article / episode | Workbook evidence to show | Web demonstration | Changed-input story |
| --- | --- | --- | --- |
| AMBC-02 | P2 Facility B7:E14, then Entity Review A4:C10 and A14:I23 | Simple credit remains available; open detailed mode, show net advance, repayments, cash gap and evidence classifications | Withhold charges at draw; then delay collection 14 days while retaining the contractual due date. Contrast an explicitly extended 44-day facility |
| OE-MSME-01 and 02 | Article Case C6:F18, C22:F38; normalization/evidence from the appendices | Annual bridge versus dated headroom; identify each symbol and period | Propose KES 30,000 withdrawal; remove the disputed receipt; explain why annual profit cannot fund a payment before collection |
| OE-MSME-03 and 04 | Cash13W rows 6:18 plus Overview D6:D7 | Base/downside weekly schedule and reserve/shortfall dates | Delay customer receipts one week; separate new borrowing from trading receipts; show amounts shifted beyond week 13 |
| OE-MSME-05 | Use the same reconciled bridge with the part's own succession/sale evidence | Follow the companion links as a cash-capacity cross-check | Explain that forecast headroom is not a business sale price or a replacement for transferability analysis |
| OE-FAILURE-11 through 13 | Cash and CCC rows 6:18 and the relevant dated case-evidence appendix | Stress planner and cash-cycle diagnostics | Pull supplier payments one week forward; then remove new borrowing or reduce the illustrative margin. Keep documentary facts separate from invented scenarios |
| KECA-02 and OE-VALUATION-06 through 08 | Relevant valuation workbook/source filings, chosen by episode | Retained DCF, explicit FCFF/WACC labels, forecast, terminal share and sensitivity | Change WACC by one percentage point; show the first five cash forecasts remain unchanged; do not use this generic FCFF page for banking/insurance valuations |

The article pages now expose these companion links without rewriting authored article text. The four new tools appear in the free-tools index and sitemap. Formulae and units are defined on the new pages; DCF and simple business credit gain local symbol dictionaries. Appendices keep the derivation and evidence detail. Protected DCA and compounding/cash-flow pages retain their current explanations; their fuller symbol definitions belong in presentation notes unless separately authorized.

## Validation and production status

- The combined calculator, account, payment and core suite passed 70 tests. New tests reconcile the source cases and all weekly baseline closes, exercise cash releases, negative balances, opening breaches, delayed/out-of-horizon receipts, financing classification, supplier acceleration, withheld charges, equal-principal interest, yield reconciliation, day-count conventions and invalid inputs.
- Anonymous form GET/POST and CSV cases pass with enforced CSRF; missing CSRF is correctly rejected. No CalculatorLead is created. Browser form submissions succeeded for all four new tools and DCF in the isolated local preview.
- At a 390-by-844 viewport all four new pages contained horizontal table scrolling within the page. A DCF navigation overflow was found and fixed with styles scoped to DCF and business credit; the checked page width then fit the viewport. Owner results were visually checked on desktop and mobile. Browser observations are verification, not final slide screenshot assets; capture the deployed pages for the presentation production pass.
- After the final scoped layout change, the two new page acceptance tests passed again and `makemigrations --check --dry-run` reported no changes.
- Source comparison against platform membership commit `6772a56` confirmed the single-asset/portfolio DCA handlers and input schemas, portfolio engine, compounding/time-value engine, lab view and lab template unchanged. DCF's calculation function is unchanged; its display layer is extended. DCA templates and shared existing CSS are outside this change.
- These calculators need no API keys, market-data connection, database migration or catalog reload. Deploy application code and collect static assets. Membership's independent migrations 0010/0011 remain required if not already applied.
- Production email, live payment acceptance and simultaneous PostgreSQL payment callbacks remain the membership launch checks documented separately. No real payment or outbound account email was triggered here.

The next presentation-production pass should use this map, preserve one deck per article/video episode and update the master index. No PPTX completion or new branded PDF batch is claimed by this calculator milestone.


## Presentation and formula delivery update — 25 September 2026

The earlier deferred-presentation statements describe prior milestones. The presentation package now contains 41 generated editable episode decks. Use the [master index](<Presentation Assets/Master Index.md>), manifest and package QA record for the current reviewed status and source/capture provenance. Recording and video publication remain separate steps.

The formula correction and read-only catalog audit were pushed as platform `52931e8`; matching verification evidence and delivery tasks were pushed as research `649bfde`. Thirty-four combined regression tests passed. New tool equations render with MathJax and visible definitions; native DOCX/PDF equations were verified with a separate two-page fixture. International/Diaspora Unicode and the protected DCA/compounding/cash-flow engines remain unchanged. Existing reading PDFs were not regenerated.

The new calculator and DCF captures in `Presentation Assets/Evidence/Web/20260925-formula-rendering/` are from an isolated local preview, with exact inputs and timestamps. They are not claims that Railway has deployed or imported the new articles. A fresh public check at 13:43:38 UTC still showed 7 series/25 articles and a 404 for the new MSME series. The Google verification file returned the expected content. Follow the platform catalog-publication runbook and membership operator guide for the remaining deployment actions.
