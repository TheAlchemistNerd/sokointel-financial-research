# Kenyan tax and household finance

Four articles, four workbooks and four technical appendices. Research cut-off: **7 September 2026**. Household data, property terms, insurance contracts and stochastic parameters are illustrative. Current statutory rules are distinguished from those assumptions.

## Reading order

| Part | Article | Body words | Technical appendix |
|---|---|---:|---|
| 1 | [Part 1 - What Your Payslip Can Actually Fund](<Part 1 - What Your Payslip Can Actually Fund.md>) | 3,552 | [Appendix 1](<Appendix 1 - PAYE and Cash Flow.md>) |
| 2 | [Part 2 - Building a Pension That Can Pay for Life](<Part 2 - Building a Pension That Can Pay for Life.md>) | 3,625 | [Appendix 2](<Appendix 2 - Pension Mathematics and Simulation.md>) |
| 3 | [Part 3 - Paying for Healthcare Without Unravelling the Household](<Part 3 - Paying for Healthcare Without Unravelling the Household.md>) | 3,649 | [Appendix 3](<Appendix 3 - Claims and Emergency Liquidity.md>) |
| 4 | [Part 4 - A Home the Household Can Keep](<Part 4 - A Home the Household Can Keep.md>) | 3,569 | [Appendix 4](<Appendix 4 - Amortisation and Housing Valuation.md>) |

All article prose paragraphs contain 100–150 words. Word counts exclude titles, metadata, diagrams, references and appendices. Each article carries IEEE numbered citations linked to online sources. Four distinct peer-reviewed papers and an academic simulation monograph support the analysis alongside KRA, Kenya Law, NSSF and RBA material.

## Workbooks

- [Part 1 workbook](<C:/Users/Nevo/Downloads/financial material/outputs/01a0789a-5035-7453-ad64-a71cc94b3211/01-PAYE-and-Cash-Flow.xlsx>)
- [Part 2 workbook](<C:/Users/Nevo/Downloads/financial material/outputs/01a0789a-5035-7453-ad64-a71cc94b3211/02-Pensions-and-Retirement.xlsx>)
- [Part 3 workbook](<C:/Users/Nevo/Downloads/financial material/outputs/01a0789a-5035-7453-ad64-a71cc94b3211/03-Medical-and-Emergency-Funds.xlsx>)
- [Part 4 workbook](<C:/Users/Nevo/Downloads/financial material/outputs/01a0789a-5035-7453-ad64-a71cc94b3211/04-Mortgages-and-Housing.xlsx>)

Each workbook contains editable assumptions, formula-driven calculations, a policy table, sources and a formula dictionary. [The companion dictionaries](<Formula Dictionaries.md>) collect the Excel expressions and mathematical equivalents outside Excel as well. Dated forecast assumptions can be changed independently. Blue inputs, black local formulas and green internal links identify cell roles.

## What the models cover

- PAYE: twelve months of 2026, February NSSF change, capped deductions, actual cash commitments, pension sensitivity and annual ordinary-income-tax reconciliation.
- Retirement: thirty annual periods, fees, inflation, contribution changes, fee sensitivity and 1,000 reproducible investment paths.
- Medical protection: claim payment stages, shared insurance relief, 2,000 reproducible event years, conditional income interruption and reserve sensitivity. Three 20,000-trial convergence checks supplement the workbook in Appendix 3.
- Housing: up to 360 monthly loan periods, rate resets and prepayments, a selectable sale horizon, rent-versus-buy DCF, a terminal-wealth reconciliation, discount sensitivity and combined rate/income stresses.

## Scope and use

The payroll pension calculation illustrates section 22A employee contributions to a registered occupational defined-contribution arrangement. It does not implement every section 22B individual-fund interaction. The housing case has its own stated household assumptions; it is not the same salary example as Part 1. The files have no live external workbook links. Reconcile shared inputs when applying them to one household, and never count a reserve more than once.

Simulated probabilities are conditional on invented distributions, not empirical estimates for Kenya. The pension model stops at accumulation and does not provide a lifetime withdrawal or annuity guarantee. Medical payment fractions are not SHA entitlements or insurer quotations. Exit tax is an explicit housing assumption requiring actual transaction analysis. These boundaries are described in detail in the appendices.

## Verification

The build passed 21 input-perturbation checks and 43 independent numerical/error checks. Formula-error scans found no errors in the exported workbooks. Every sheet was rendered and visually reviewed; the editable charts were checked against their source cells. [Verification details](<Verification.json>) record article counts, independent calculations and additional medical simulation runs. Numbered body equations are expanded manually in the matching appendix.

## Publishing

The Markdown articles use portable Unicode equations. Upload the six PNG figures from the Figures folder where referenced. Publish the technical appendix and workbook as companion downloads if the platform supports them. The articles themselves have not been posted to LinkedIn, Medium or Substack.
