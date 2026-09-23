# Kenyan equities and company analysis

Four articles connect dividend research, business valuation, portfolio construction, and long-term household outcomes. The research cutoff is **7 September 2026**. The examples use Kenyan shillings, with units stated in each model.

## Read the series

| Part | Article | Body words | Technical companion |
|---|---|---:|---|
| 1 | [What a Kenyan Share Can Pay You;and What It Costs to Own](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Part 1 - Building an Income and Research Universe.md>) | 3,564 | [Calculations and formula dictionary](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Appendices/Appendix 1 - Income and Bill Mathematics.md>) |
| 2 | [Reading the Business Behind a Kenyan Share Price](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Part 2 - Reading Businesses and Estimating Value.md>) | 3,627 | [Calculations and formula dictionary](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Appendices/Appendix 2 - Statements and Valuation Mathematics.md>) |
| 3 | [Building a Kenyan Portfolio You Can Explain and Maintain](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Part 3 - Constructing Portfolios with a Purpose.md>) | 3,667 | [Calculations and formula dictionary](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Appendices/Appendix 3 - Portfolio Mathematics and Implementation.md>) |
| 4 | [Keeping a Kenyan Portfolio Useful as Life and Markets Change](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Part 4 - Compounding Through Uncertain Markets.md>) | 3,660 | [Calculations and formula dictionary](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Appendices/Appendix 4 - Compounding and Simulation Mathematics.md>) |

Each article contains 28 prose paragraphs, all between 100 and 150 words. Word counts exclude headings, tables, illustrations, references, and the separate technical appendices. Eight figures illustrate the cash processes and numerical experiments. Numbered equations use Unicode and ordinary mathematical notation; the appendices expand their assumptions and manual calculations.

## Workbooks

Begin with the Guide sheet, then change the relevant inputs. Blue numbers are supplied values or assumptions; green formulas draw from another worksheet; black formulas calculate locally. Source observations carry their period and provenance. The Formula dictionary sheet explains calculation families, mathematical equivalents, units, and scope. The appendices provide worked examples and links to a complete cell-by-cell formula audit.

| Workbook | Worksheets | Main uses |
|---|---:|---|
| [Kenyan equity screening and Treasury bills](<C:/Users/Nevo/Downloads/financial material/outputs/01a0789a-5035-7453-ad64-a71cc94b3211/kenyan-equities/01-Screening-and-Income.xlsx>) | 9 | NSE directory, income filters, ordinary and special dividends, payout, dividend cuts, bill pricing, tax settlement, rollover and cash returns. |
| [Business quality and valuation](<C:/Users/Nevo/Downloads/financial material/outputs/01a0789a-5035-7453-ad64-a71cc94b3211/kenyan-equities/02-Statements-and-Valuation.xlsx>) | 15 | Five-year integrated statements, working capital, DCF and two-variable sensitivity, bank credit and capital, insurance scenarios, sector screens and historical quality signals. |
| [Portfolio allocation, risk and executable positions](<C:/Users/Nevo/Downloads/financial material/outputs/01a0789a-5035-7453-ad64-a71cc94b3211/kenyan-equities/03-Portfolio-Construction.xlsx>) | 14 | Three allocation policies, correlation and covariance, risk contributions, concentration controls, sampled allocation search, joint stresses, whole-share orders, liquidity and rebalancing. |
| [Compounding, cash flow and simulation](<C:/Users/Nevo/Downloads/financial material/outputs/01a0789a-5035-7453-ad64-a71cc94b3211/kenyan-equities/04-Compounding-and-Simulation.xlsx>) | 14 | Annual savings and spending plans, real wealth, fixed-draw Monte Carlo, goal sensitivity, sequence risk, extended simulations, time-weighted and money-weighted performance and monitoring. |

## Put the models to work

1. In workbook 1, use the directory to establish the research universe. The 68 directory records include funds, REITs, and legacy entries. Seven equity rows contain dated dividend examples: Equity, KCB, Co-operative Bank, Safaricom, BAT Kenya, Jubilee, and KenGen. Financial fields on other rows are ready for source extraction. Confirm current trading eligibility and enter dated market prices before comparing candidates.
2. In workbook 2, select the appropriate business framework. The integrated manufacturer, bank, insurer, and historical quality examples are fictional teaching cases. Replace financial inputs with a consistent reporting entity, accounting period, and unit. The Review log connects financial observations to the investment case. The statements reconcile without a balancing cash plug.
3. In workbook 3, start with household objectives, then explore the Income Reserve, Balanced, and Growth policies. Change asset assumptions and weights, inspect risk contributions and constraint counts, and test shared shocks. The Positions sheet converts the Balanced policy into whole-share quantities and reconciles security values, costs, and residual cash to the budget. The bill row reserves a cash budget: use workbook 1 to convert that amount into eligible bill face values and maturities.
4. The Rebalance sheet estimates trades needed to return towards target weights and shows the cash required after costs. Review aggregate cash availability, settlement timing, liquidity and lot sizes before treating those estimates as an implementable order schedule. Its drift band identifies positions for review; indicative target trades are also shown for positions inside the band.
5. In workbook 4, change the main contribution, withdrawal, inflation and implementation-cost inputs to update default annual plans. Replace individual Annual plan formulas with year-specific values when needed. Return, volatility, dividend yield, tax and crisis inputs feed the live model. Horizon and path-count cells report the fixed twenty-year, 500-path layout; extending the experiment requires extending the model.

Workbooks are self-contained. Cross-workbook figures are documented snapshots, so updating a price or allocation in workbook 1 or 3 requires transferring the resulting assumptions to workbook 4. Within each workbook, formulas update their dependent outputs. The sampled-search weights and the Extended simulation sheet are fixed experiment results; their refresh process is described below.

## Understand the numerical experiments

All entry prices, expected returns, volatility, correlations, trading capacity, growth rates and crisis parameters are labelled educational assumptions. Reported dividends and selected earnings observations remain dated source facts. The bill return assumption in portfolio modelling is after bill tax; equity return assumptions include dividends before the separate dividend-tax deduction. Costs and tax are applied according to the stated experiment, without adding dividends twice to total return.

The portfolio search draws 80,000 candidate allocations using seed 20260907, retaining 4,575 that meet the sampling constraints and adding the three policies. It reports the lowest-variance and highest-Sharpe allocations found in that sample. The workbook contains an audit subset and the selected candidates. Changing constraints requires regenerating the candidate set; changing return and covariance assumptions updates displayed candidate metrics but does not automatically select a new winning portfolio.

The live workbook experiment contains 500 aggregate-portfolio paths, with normal and uniform draws fixed using seed 20260908. The larger experiment contains 10,000 asset-level paths per case, using seed 20260909. Its shared normal factor produces related asset returns, while a separate annual crisis draw applies different losses to the equity assets. Annual constant-weight rebalancing, nominal year-end cash flows, inflation, implementation drag, and dividend tax follow the documented conventions. These experiments have different distributions and crisis definitions, so their probabilities answer different conditional questions.

The extended cases compare all three allocations with and without the crisis mixture, then vary Balanced contributions, inflation and withdrawals. Reported measures include wealth percentiles, goal probability and its sampling standard error, annual-checkpoint drawdowns, terminal tail loss, and unfunded withdrawals. Sampling precision describes the numerical experiment; sensitivity analysis explores uncertainty in its assumptions. Historical return estimation, shrinkage and backtesting methods are discussed in the appendix; the supplied portfolio results use stated assumptions rather than a calibrated historical backtest.

## Research and reproducibility

- [Research questions and topic coverage](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Research/Research Questions and Coverage.md>)
- [Source register: 33 authoritative, issuer and academic sources](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Research/References.md>)
- [Calculation, article and workbook verification](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Research/Verification.md>)
- [Reproduce the numerical experiments](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Research/Reproduction Guide.md>)
