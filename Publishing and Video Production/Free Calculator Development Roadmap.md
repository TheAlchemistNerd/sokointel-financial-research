# Free calculator development roadmap

Confirmed scope — 25 September 2026: Making Business Credit Work; Owner Earnings Project 1 (MSMEs and Small Businesses); Owner Earnings Project 3 (Failure Retrospectives and Warning Systems). This is the development specification for the next free-tool milestone. The current port/PDF/presentation milestone must not describe these new tools as already live.

## Protected existing tools

Preserve the single-asset DCA, portfolio DCA and compounding/cash-flow calculators: calculation engines, existing forms, formula output and behaviour. Keep regression checks for those routes when shared infrastructure changes. Do not redesign their layout or repurpose their inputs. The user expressly values their present implementation.

Retain the current DCF route and results as the starting point. A future valuation enhancement should add clarity and scenarios without silently substituting owner earnings for unlevered enterprise cash flow.

## 1. Business credit: from quote to cash and repayment

Enhance the existing cost planner through a detailed mode while preserving the four-input quote calculation for existing callers. Use both articles and the canonical business-credit workbook, including the evidence/entity-resolution additions.

Editable inputs: facility principal; invoice/order value; advance rate; tenor and day-count convention; nominal simple rate; upfront fee; fixed fees; withheld charges versus charges payable later; repayment structure; expected collection date; delayed-collection scenario; gross margin; inventory, receivable and payable days; starting usable cash; minimum reserve; other scheduled debt payments. Label an invoice amount separately from the cash actually advanced.

Outputs: dated financing cash flows, net day-zero proceeds, total fees/interest, total repayment, cash available at each repayment date, principal-based annualised cost and clearly distinguished cash-flow annual yield when mathematically valid. Show collection-delay funding gap and break-even contribution after finance costs. A negative net advance, invalid timing or an undefined rate must produce an understandable validation result.

Keep classification upstream: separately enter verified trading receipts, owner funding, borrowed funds, inter-account transfers and unresolved receipts. Exclude non-trading flows from operating receipts. Do not claim to identify common ownership or circular flows from a summary form; the workbook's evidence ledger and actual records remain necessary. Show both an evidence-supported and an unresolved-receipts-excluded case.

Method boundaries: do not label simple annualisation as statutory APR; an invoice-discounting facility, amortising term loan and revolving line have different cash-flow timing. Do not double-count fees as both withheld and paid later.

## 2. MSME owner earnings and distribution bridge

Use Project 1's worked Article Case and related model sheets. Reconcile the current case to KES 990,000 normalised owner earnings and KES 140,000 provisional cash headroom, with KES -60,000 headroom when the disputed KES 200,000 receipt is excluded. Confirm exact workbook cells during implementation; these are a reconciliation target, not a substitute for reading the workbook.

Editable inputs: accounting profit after tax; depreciation/amortisation already included in that profit; documented non-cash adjustments; one-off gains/costs and normalisation; commercial replacement pay for owner labour; maintenance-capital low/base/high estimate; increase in required operating working capital; growth investment; scheduled debt principal; reserve replenishment; actual opening cash and cash collections; proposed owner withdrawal.

Show the bridge in separate layers: normalised operating earnings, estimated owner earnings, cash after committed outflows, and proposed-withdrawal headroom. Owner earnings is not the bank balance and is not automatically distributable cash. Avoid subtracting interest or tax twice when starting from profit after tax. Subtract an increase in working capital; show a release separately and explain whether it can recur.

Outputs include a waterfall/table, maintenance-capital sensitivity, disputed-receipt scenario and an explanation of the binding constraint. Editable cells should be visually identified as on the workbook. The public calculator does not decide a legally permissible dividend.

## 3. Thirteen-week operating cash planner

Build a table with editable weekly rows, not a single average-burn input. Inputs: opening unrestricted cash; customer receipts; other separately classified inflows; payroll; supplier payments; rent/operating costs; taxes; maintenance investment; growth investment; interest; principal; owner distributions; minimum reserve. Scheduled new financing is a separate switch/scenario, never operating revenue.

Outputs: opening/closing cash per week, lowest cash, first reserve breach, first funding shortfall, cumulative financing need, and the difference between the base and delayed-receipt cases. Carry week-end cash into the next week. A deficit must remain visible rather than be silently floored at zero. Show whether the horizon ends before a breach; do not call that infinite runway.

## 4. Failure-analysis stress and warning system

Use Project 3's warning models and evidence standards. Combine collections slowing, margin compression, inventory build-up/write-down, supplier terms shortening, maintenance requirements, fixed operating costs, lease/debt service and a funding delay/cessation scenario.

Keep company evidence separate from scenario inputs. Nakumatt, Tuskys, Twiga and Copia are research cases, not prefilled synthetic financial statements presented as historical data. Require a period/currency label and a source or 'illustrative' status. Neither a modelled cash deficit nor owner earnings alone establishes insolvency, fraud, cause of failure or creditor recovery.

Outputs: base/downside 13-week liquidity, cash-conversion-cycle decomposition (DIO+DSO-DPO), sensitivity to supplier withdrawal, required cash buffer and a warning dashboard with explainable thresholds. Increasing DPO can temporarily improve a cash metric while increasing arrears and supply disruption risk; show both. Recovery or claims-waterfall tools require a separate documented legal-priority specification before introduction.

## DCF assessment, retained alongside these priorities

Useful additive improvements: an on-page symbol dictionary; explicit FCFF/enterprise valuation framing; forecast year-by-year table; terminal-value formula and share of value; discount-rate/terminal-growth sensitivity with invalid cells labelled; clear units and dates; treatment of non-operating assets/net debt and diluted shares. Do not subtract net debt a second time from a cash flow already defined as an equity claim. Banks/insurers need distributable-capital/equity models rather than this generic enterprise formula.

## Shared acceptance requirements

- Each symbol is defined beside its formula with units, period and sign convention. Appendices retain derivations.
- Baseline outputs reconcile with named workbook cells and an independently hand-calculated example.
- Inputs are not persisted or sent to a lead-capture system. Free use should not require membership.
- Show dated synthetic defaults as illustrative; never imply live company data.
- Test zero rates, negative cash, cash releases, boundary dates, missing/invalid numbers, extreme values and no-double-counting identities.
- Retain CSRF protection for browser forms and test actual anonymous GET/form POST in a fresh browser.
- Check desktop/mobile tables and readable downloadable schedules; formulas must remain understandable when math rendering is unavailable.
- Validate that the three protected calculator families have unchanged source/behaviour.
- Update relevant article links, episode demonstration plans and screenshots only after the new pages exist.

## Milestone handoff

For each completed calculator, record source workbook/sheet/range, formula map, accepted discrepancies, tests, screenshots and route. Review `git diff`, create a detailed untracked commit-message file, commit and push both repositories at the significant coordinated milestone, as requested by the user. Keep deployment/import verification distinct from a successful Git push.

## Delivery update - 25 September 2026

The four specified tools are implemented and reconciled locally. DCF gains the explicit FCFF/WACC convention, forecast table, terminal formula, symbol dictionary and sensitivity grid while retaining its calculation engine. Existing simple business credit remains available. The protected DCA and compounding/cash-flow families are unchanged.

See [Free Calculator Reconciliation and Recording Map](<Free Calculator Reconciliation and Recording Map.md>) for routes, source hashes, exact workbook cells, accepted timing differences, tests and article/episode demonstrations. This is the dated completion record for the specification above; implementation and local tests do not alone establish Railway deployment. The credit tool currently supports bullet/equal-principal facilities, not a revolving line; cash-cycle days are diagnostic, and repay/collection dates are explicit. CSV output contains calculated schedules. New API keys, migrations and catalog imports are not needed for the calculators.
