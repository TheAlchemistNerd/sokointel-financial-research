# Part 06 — Reconstructing owner earnings from public filings

*Revised practical article; source details and figures are dated to their cited filing or event, with current evidence reviewed through 24 September 2026.*

A public company gives us more information than most private businesses, but it does not give us a line called “owner earnings.” We have to build one from the report and keep every analyst judgment visible.

Begin with the filing’s own map. Read the auditor’s opinion, the basis of preparation, the accounting policies and the notes behind profit, working capital, share compensation, leases and capital spending. Record the legal reporting entity, consolidated or parent-only scope, currency, fiscal year, and date the report was published. A group with a Kenyan parent and overseas subsidiaries may report consolidated earnings in a different currency context from the parent’s standalone financial statements.

## Reported cash flow first, estimated earning power second

The first output should be reported values as filed. For each of the last several years, record:

* profit attributable to ordinary shareholders;
* depreciation, amortization and other relevant non-cash items;
* cash generated from operating activities;
* movements in receivables, inventory, payables and contract balances;
* cash capital spending and acquisitions;
* debt raised and repaid, dividends, buybacks and share issuance.

Then reconcile the movement in cash. Accounting earnings, operating cash flow, and cash after total capital spending answer different questions. Dechow, Kothari and Watts show why the relation between accrual earnings and operating cash flows varies across firms and periods [1]. A good analyst does not assume that the earnings-to-cash gap is automatically a red flag. They investigate what caused it and whether the cause is likely to reverse, recur, or grow.

Owner earnings is the next and less mechanical step. Buffett’s formulation begins with reported earnings, adds back relevant non-cash charges, then subtracts the average capital expenditures needed to maintain competitive position and unit volume, and incremental working capital needed for that same purpose [2]. It is not “cash from operations minus all capex” by definition, and it is not “net income plus depreciation.” The analyst must distinguish the cash needed to maintain the existing business from investment aimed at expanding it. Public reports often do not provide a neat split. In that case, say so and test an evidenced range.

Avoid double counting. If starting with net income, show the non-cash adjustment and maintenance investment. If starting with cash from operations, it already reflects reported working-capital changes and several noncash adjustments. Do not add those adjustments again unless you are deliberately restating them, and do not subtract the same working-capital movement twice. Keep a separate reconciliation between your estimate and the actual cash-flow statement.

## A dated Kenyan example

BAT Kenya’s audited FY2025 report gives a useful starting set of reported facts. Revenue was KES 23,191.945 million; EBIT was KES 7,474.835 million; operating cash flow was KES 6,633.154 million; capital expenditure was KES 301.833 million; and earnings per share was KES 52.46 [3]. These numbers tell us about reported scale, operating profit and cash conversion. They do not, by themselves, establish a maintenance-capital estimate.

The tempting shortcut would be to call the KES 301.833 million of total capital expenditure “maintenance” or to assume it is all growth. Neither conclusion follows from the total. A proper bridge would trace additions to the property, plant and equipment note, compare several years of spending with depreciation, inspect the stated purpose of major projects, identify asset replacements, and check what production or competitive capacity those assets support. If the report does not provide enough detail, the conclusion should read: “maintenance capital is not separately disclosed; a defensible owner-earnings estimate requires a supported range or additional operating records.”

The same applies to the KES 6,633.154 million operating cash flow. It is a reported cash-flow measure for a fiscal period. It is not the amount shareholders can distribute because capital spending, debt obligations, working-capital needs, and future investment still matter. A useful article can show the reported bridge and leave the normalized owner-earnings result unavailable pending maintenance evidence. That is more informative than a precise but invented number.

## Make each adjustment traceable

Every analyst adjustment needs a line in a source ledger:

| Field | What to record |
|---|---|
| Filed line | Exact statement/note label and page or table |
| Entity and period | Parent or group, year, currency, reporting date |
| Adjustment | What changes and why |
| Evidence | Filing, management commentary, multi-year record, or external source |
| Status | Filed fact, analyst estimate, hypothesis, or unresolved |
| Sensitivity | How the value changes under a reasonable alternative |

Watch for acquisition effects, discontinued operations, unusual tax benefits, restructuring costs, impairment reversals, capitalized software and development, leases, and share-based compensation. Do not add back a cost just because it is called “non-cash.” Some noncash expenses represent real capital consumed or future dilution. Stock-based compensation, for example, is added back in operating cash flow as a noncash adjustment, while owners can still experience dilution. Use one coherent treatment: keep the expense in earnings, or add it back and separately model the dilution or replacement cost. Do not do both.

## Link earnings to value carefully

Ohlson’s peer-reviewed model relates value to earnings, book values and dividends under explicit accounting relationships [4]. It is a useful reminder that valuation depends on future earnings and the capital that supports them. A current owner-earnings estimate can anchor scenarios, but it is not the whole value. Growth requires reinvestment. Returns on invested capital can fade. Risks change the required return. The value of a listed share also depends on how much of the business’s cash generation is available to that equity claim after other claims.

The KCA series and its four final workbooks already show the value of separating screening, financial statements and valuation, portfolio construction, and compounding. The new model should follow that traceable design while adding explicit maintenance-capital ranges, a working-capital maintenance/growth distinction, and a source status for each adjustment.


## Create a filing model that another analyst can reproduce

Start by recording the issuer’s legal name, fiscal year-end, filing date, currency, units and consolidation scope. A company may present group earnings in one section and parent-only earnings in another. Do not mix them. Each raw input should point to a statement or note and carry a source ID. Preserve the as-filed value; add any reclassification in a separate column with the reason and formula. A reviewer should be able to recreate every output from that source list.

Build the historical model across at least five years where filings allow. The income statement shows revenue, operating costs, taxes, interest, net income and non-controlling interests. The balance sheet supplies opening and closing receivables, inventory, payables, contract balances, cash, debt, leases, fixed assets and equity. The cash-flow statement gives operating cash, tax and interest paid, capital purchases, asset sales, financing and dividends. Notes explain acquisitions, disposals, stock-based compensation, impairments, leases, commitments and policy changes. A five-year trend is not complete if it ignores a major acquisition that changed the perimeter.

Use reconciliation controls, not visual confidence. Revenue should tie to the filed statement. Group profit should reconcile to parent and non-controlling interests. Opening cash plus reported movement should tie to ending cash. Debt balances should tie to current and noncurrent borrowings in the notes. Changes in assets should reconcile to additions, depreciation, disposals and currency effects. If a tie-out fails, show the variance and do not hide it in “other.”

## Move from accounting earnings to a cash estimate

The bridge starts with the claim the analyst wants to value. For equity owners, net income attributable to parent may be a clean starting point, but cash available to equity still reflects capex, working capital, interest and debt repayment. For enterprise value, begin with a pre-financing operating cash measure and later account for debt and lease claims. Keep both approaches consistent. Do not subtract debt from a cash flow after interest and principal were already deducted without explaining the adjustment.

A practical bridge can include reported net income; noncash depreciation and amortization; stock compensation treatment; other material noncash charges; working-capital change; cash capex; tax paid and interest depending on starting point; debt issuance and repayment; acquisitions or disposals; and diluted share count. Then create an analyst owner-earnings estimate that subtracts maintenance spending and additional working capital required to sustain current earning power. Growth investment remains visible but is not mistaken for maintenance. If maintenance cannot be established, show a range and a “not estimable” case.

Noncash charges need different logic. Depreciation is added back to reconcile profit to cash, but replacement spending must be estimated. Impairment is noncash in the period but may indicate weaker future economics. Stock compensation is a real claim on owners. Either leave the expense in earnings and do not add it back, or add it back and model dilution or cash repurchases separately. The model should show both methods side by side if the answer changes materially.

Working capital should be rebuilt from balances, not taken solely from an annual cash-flow line. Calculate year-over-year changes in receivables, inventory, payables, contract assets, accrued expenses and customer advances. Reconcile those movements to cash flow. Acquisitions, foreign exchange, reclassifications and noncash changes can create differences. A rising payable balance can be a temporary source of cash, but if it reflects overdue invoices or supplier distress it is not a durable owner benefit. A customer advance creates cash and a delivery obligation; it is not unrestricted earnings.

## Maintenance capex: make the uncertainty measurable

Companies rarely report maintenance capex as a clean number. Build three estimates from evidence. First, inspect asset additions and depreciation by class over several years; this is a starting range, not a conclusion. Second, use the company’s stated renewal plans, engineering reports, operating uptime, useful lives and supplier quotes. Third, compare spending with capacity and output: a large increase in capacity or new factory is growth, while repeated replacement of a worn production line may sustain existing volume. State which method drives low, base and high.

If annual D&A is $1 billion and total capex is $1.4 billion, it does not follow that maintenance is exactly $1 billion and growth $400 million. D&A reflects accounting estimates and past cost; replacement prices and useful lives may differ. Conversely, a year with low capex can mean renewal was deferred. The analyst should check backlogs, repair costs, outages, safety compliance and capitalized software. Record the next evidence needed to narrow the range. A chart that assumes a fixed share of D&A each year may be useful as a sensitivity, but it must remain labeled as an assumption.

Normalized earnings should also handle cycles. Commodity prices, utilization, credit losses, foreign exchange, tax rates and customer ordering can distort a single year. Use several years and identify the economic drivers rather than averaging mechanically. A simple average may combine recession, acquisition, impairment and a different business mix. Create a normalized case with a stated mid-cycle input and stress it against a plausible low case. Use management guidance as an attributed source, not a substitute for independent model logic.

## Convert the estimate into a per-share claim

Diluted shares matter because owners own per-share cash, not an abstract corporate total. Track weighted average basic shares, diluted shares, shares issued, options and restricted awards, buybacks, acquisition consideration and treasury shares. Match the share count to the period and earnings numerator. If the issuer reports repurchases, compare the quantity and price with the net change in diluted shares. Repurchases may offset employee awards rather than reduce the share count. Model future dilution and capital spent to offset it.

Then value with a method suited to the claim. An equity cash flow or residual-income model can fit businesses where book capital is central. Enterprise DCF can fit nonfinancial operations if cash flows are before financing and debt/leases are consistently treated. An earnings yield or comparable multiple is a cross-check, not a cure for inconsistent accounting. Use a reverse valuation to determine what growth, margins, capital intensity and terminal economics the market price implies. The key question is whether that path is supported by capacity, customers and reinvestment—not whether the spreadsheet can produce a point value.

Sensitivity should show economically related combinations. A slower growth case may reduce supplier commitments but also utilization and gross margin. A lower sales case may increase receivables days if buyers pay later. A high-rate case can change debt interest and discount rate together. A one-variable table can help identify sensitivity, but a scenario should tell a coherent operating story. Show low/base/high value ranges and the inputs that drive most of the spread.

## Write the decision after reviewing the open items

Before acting, summarize the evidence in plain language: what was reported; what the analyst changed; what cannot be estimated; and what the current price appears to require. If valuation depends on an uncertain maintenance range, say how a 20% higher replacement need changes owner earnings and value. If one customer concentration or debt maturity dominates, show the trigger for refreshing the analysis. A reader should know which filing note or next quarter disclosure could change the conclusion.

For a public-market investor, the decision need not be “buy” or “sell.” It can be to wait for the next filing, maintain a smaller position, demand a higher expected return, or treat the issuer as outside the circle of competence. The workbook’s role is to make those trade-offs visible and repeatable. It cannot remove uncertainty, but it can stop accounting presentation, inconsistent units or a hidden assumption from deciding the answer by accident.

## Worked bridge: keep the reported year and the normalized year apart

The following example is illustrative, not a restatement of BAT Kenya or any other issuer. Assume a company reports KES 1,000 million of net income, KES 180 million of depreciation and amortization, KES 80 million of share-based compensation, and KES 30 million of gain from selling an old asset. Assume analyst evidence supports KES 260 million of maintenance investment and KES 90 million of additional working capital to sustain the current activity level. A first-pass equity owner-earnings bridge is:

| Line | KES million | Treatment |
|---|---:|---|
| Net income attributable to ordinary shareholders | 1,000 | Filed starting point |
| Add depreciation and amortization | 180 | Noncash expense; replacement cash is estimated below |
| Add share-based compensation | 80 | Only if dilution or replacement cost is modeled separately |
| Remove gain on asset disposal | (30) | Nonrecurring gain included in reported earnings |
| Subtract maintenance investment | (260) | Analyst estimate, supported by asset evidence |
| Subtract incremental working capital | (90) | Growth in cash tied up to sustain the modeled activity |
| Illustrative owner-earnings estimate | 880 | Before any further financing or valuation judgment |

This is not automatically cash available for a dividend. It assumes net income already reflects interest and cash taxes for the period. A working-capital estimate must be consistent with the chosen period and starting method. If the analyst instead begins with operating cash flow, the filed working-capital changes have already affected that line; subtracting them again would double count. The analyst must also explain what happens to the KES 80 million share-based compensation. Leaving it in expenses lowers the result to KES 800 million before other changes; adding it back requires a separate view of future share dilution or repurchases. The correct treatment is the one that values the same economic claim without counting compensation twice.

Suppose the evidence supports maintenance spending from KES 220 million to KES 340 million. The owner-earnings range is KES 920 million to KES 800 million, before other uncertainties. If diluted shares are 100 million, that is KES 9.20 to KES 8.00 per diluted share, subject to the share-compensation treatment. A precise KES 880 million point estimate hides the fact that maintenance evidence is the largest driver. Report the range and the specific asset records that would narrow it.

## Reconcile the model to the filed statements before valuing it

A well-built model has three distinct layers. The first is a transcription layer that reproduces the annual report. The second is an analyst layer that adjusts or normalizes filed amounts. The third is a decision layer that converts the estimate into value, expected return and position size. Mixing these layers makes review difficult because an analyst assumption can appear to be a reported fact.

For each statement line, preserve the label used by the issuer and record page or note, reporting entity, unit, period, original currency, exchange rate if converted, and sign convention. Reconcile subtotals to the report. If operating cash flow does not match the audited statement, stop and resolve it before building the valuation. Check parent versus consolidated accounts, continuing operations, restated comparatives, year-end date, and whether amounts are in shillings, thousands or millions. A thousand-fold unit error can make a sophisticated forecast meaningless.

Build a reconciliation from opening cash to closing cash and from opening debt to closing debt. For cash, show operating, investing and financing flows plus foreign-exchange effects. For debt, show new borrowings, repayments, lease additions, foreign exchange, acquisitions, reclassifications and closing balances. Track restricted cash separately. If the annual report's cash definition differs from the analyst's, explain the bridge rather than silently changing the label.

Then use cross-checks that can expose inconsistent assumptions: revenue growth against receivables and inventory growth; margins against product mix and input costs; depreciation against asset additions; cash taxes against the tax note; interest expense against average debt and disclosed rates; dividends and buybacks against the cash-flow statement; and diluted share count against awards, conversions and repurchases. These are not automatic fraud tests. They are prompts to reconcile a surprising result and ask management or source documents for the explanation.

## Normalize with a business explanation

Do not average a period without identifying what changed. For a cyclical company, map capacity utilization, selling prices, input costs and inventory through a full cycle where possible. For a bank, focus on credit losses, funding cost and regulatory capital instead of applying an industrial maintenance formula. For an insurer, keep insurance service result, investment result, claims and solvency capital distinct. For an acquisitive company, separate acquired earnings from the cash purchase price, integration expense and incremental shares or debt. If the reporting perimeter changed, comparable growth needs a like-for-like bridge.

A one-off add-back is credible only when the cash or accounting item is identified, the event is nonrecurring in economic substance, and the business will not need a similar expense to keep earning revenue. Repeated “one-time” restructuring costs may be part of the operating model. A tax credit can boost earnings without creating recurring operating performance. An impairment reversal may raise accounting income but not customer cash. The filing note and multi-year record are stronger evidence than an issuer's preferred label.

The dates of evidence matter. A result published after the valuation date cannot be used to claim that an investor could have known it earlier. Keep the fiscal year, report publication date and market-price date as separate fields. This is essential in a backtest and useful in a live investment memo because it reveals when an estimate should have changed.

## Make the workbook reviewable by someone who disagrees

A reviewer should be able to change maintenance capex, working-capital intensity, share dilution, discount rate and terminal assumptions without changing the filed inputs. Add a notes field for every analyst assumption: evidence, owner, date entered, rationale, range and next review trigger. A source row should lead to the annual report, page or note; a calculated output should lead to its formula inputs.

Use explicit checks. Balance-sheet assets should equal liabilities and equity where the source statements permit. Cash roll-forward should equal reported ending cash. Debt roll-forward and share count should reconcile or display an explained residual. Units should be consistent in each calculation. Formula cells should never contain manually typed overrides without a separate override label. A range check can flag implausible negative shares, a maintenance estimate above total capex, or an implied value that changes solely because currency units were switched.

Dechow, Kothari and Watts document that accrual earnings and cash flows relate differently across firms and time [1]. The practical model implication is to preserve both measures and explain the divergence, rather than forcing them to agree through a hidden plug. Ohlson's valuation framework also makes accounting earnings and book values part of a structured valuation relationship, not interchangeable with cash or intrinsic value [4]. The analyst should show how the selected method uses each measure and what assumptions remain decisive.

## A disciplined output for an investment committee

End the filing analysis with a one-page memo, not just a target price. State the reported facts, analyst adjustments, estimated owner-earnings range, per-share range, major downside mechanism, capital-allocation needs, and the evidence that would change the view. Separate business quality from price: a durable company can be overvalued, and a low multiple can reflect an impaired earnings base.

For BAT Kenya, the published FY2025 figures in the report give revenue, EBIT, operating cash flow, capital expenditure and EPS [3]. Those are a sound starting point, but the article should not manufacture a maintenance split that the report does not disclose. The decision can be explicit: owner earnings remain a range or not estimable until a supported renewal estimate and incremental working-capital requirement are available. That leaves a clear next step—obtain project-level capex, asset-condition and working-capital evidence—instead of disguising uncertainty as precision.

## Workbook map

The [Project 2 workbook](Project%202%20-%20Listed%20Companies%20Owner%20Earnings%20and%20Valuation.xlsx) includes dated NVIDIA FY2026 filing inputs, a separate owner-earnings bridge, editable assumptions, an asset-heavy issuer screen, bank and insurer context, a seven-issuer NSE evidence matrix, nine profile-specific stress cases, a conditional valuation range, and Sources and Checks. `Evidence Vectors` carries each populated issuer/regulator measure with its entity, amount/unit, fiscal period, event/year-end date, filing or report date, source ID, retrieval date and workbook locator; scenarios and empty inputs stay separate. Reported facts remain separate from maintenance and working-capital assumptions. The valuation stays unavailable until earnings, growth, discount and terminal rates, diluted shares and a dated price are entered. The detailed cash bridge is NVIDIA-specific; the NSE matrix is a source-led casebook, and `Profile Stress` uses normalized hypothetical inputs rather than full issuer valuations.

## Technical appendix

- [Appendix 04 — Listed-company profile stress cases](Appendices/Appendix%2004%20-%20Listed%20Company%20Profile%20Stress%20Cases.md)
## Technical appendices

The worked calculations and source boundaries below extend this article's examples. They keep assumptions and unresolved inputs visible so readers can reproduce the steps without mistaking an illustration for an issuer or sector estimate.

- [Appendix 01 - From the filed statement to an equity claim](Appendices/Appendix%2001%20-%20Filing%20Reconstruction%20and%20Equity%20Valuation.md)

## References

[1] P. M. Dechow, S. P. Kothari, and R. L. Watts, “The Relation Between Earnings and Cash Flows,” *Journal of Accounting and Economics*, vol. 25, no. 2, pp. 133–168, 1998, https://doi.org/10.1016/S0165-4101(98)00020-2.

[2] Berkshire Hathaway, “Chairman’s Letter — 1986,” https://www.berkshirehathaway.com/letters/1986.html.

[3] BAT Kenya PLC, *Combined Annual and Sustainability Report 2025*, https://www.batkenya.com/content/dam/endmarkets/ke/en/download/investors-and-reporting/annual-reports/BATK_Combined_Annual_and_Sustainability_Report_2025.pdf.

[4] J. A. Ohlson, “Earnings, Book Values, and Dividends in Equity Valuation,” *Contemporary Accounting Research*, vol. 11, no. 2, pp. 661–687, 1995, https://doi.org/10.1111/j.1911-3846.1995.tb00461.x.













