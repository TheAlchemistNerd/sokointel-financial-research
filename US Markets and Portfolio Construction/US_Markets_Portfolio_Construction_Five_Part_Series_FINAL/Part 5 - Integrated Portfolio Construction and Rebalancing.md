# Part 5 — Putting It Together: Allocation, Overlap, Rebalancing, Scenario Testing and Portfolio Governance

## Series scope

The first four articles separated the major decisions hidden inside the supplied U.S. markets research notes. Part 1 treated SPYM as broad U.S. large-cap beta and QQQM as a deliberate Nasdaq-100 growth tilt. Part 2 compared portfolio architectures and argued for a bounded core-satellite/core-plus framework. Part 3 treated a semiconductor ETF as a sector overweight rather than a new asset class. Part 4 treated the option wheel as a payoff-modifying equity strategy rather than guaranteed income.

The final task is integration. A portfolio is not complete when every sleeve is individually reasonable. It is complete when the **combined exposures, capital requirements, risk contributions and decision rules** are coherent.

This article uses an illustrative policy of 60% SPYM, 15% QQQM, 10% semiconductor exposure and 15% wheel/collateral reserve because that structure captures the recurring ideas in the supplied notes while keeping the active sleeves bounded. The percentages are not personalized advice. They are a worked case for the companion workbook.

## 1. Begin with an investment policy, not a forecast

A portfolio policy is a set of rules that can survive changes in headlines. It specifies what the capital is for, how much loss the investor can tolerate, what each sleeve is allowed to own, how far weights may drift, and when the policy itself can be changed.

Investor.gov distinguishes asset allocation from diversification and notes that the appropriate mix depends on time horizon and risk tolerance [1]. It also warns that narrowly focused ETFs do not necessarily provide diversification merely because they contain multiple securities [1]. That point is central here: SPYM, QQQM and a semiconductor ETF are three funds, but all are substantially U.S. equity risk.

The policy therefore needs two layers:

- **capital allocation:** the percentage of dollars assigned to each sleeve; and
- **risk allocation:** how much each sleeve can contribute in normal and stressed markets.

The two are not the same.

## 2. The illustrative four-sleeve policy

| Sleeve | Target weight | Role | Strategic or tactical? |
|---|---:|---|---|
| SPYM | 60% | Broad S&P 500 U.S. large-cap core | Strategic |
| QQQM | 15% | Nasdaq-100 growth/innovation tilt | Strategic tilt |
| Semiconductor ETF | 10% | Bounded industry overweight | Satellite |
| Wheel / collateral reserve | 15% | Option premium, contingent equity purchase, liquidity | Tactical |
| **Total** | **100%** | | |

State Street reports a 0.02% gross expense ratio for SPYM [2]. Invesco reports 0.15% for QQQM [3]. If SOXQ is used for the semiconductor sleeve, its current expense ratio is 0.19% [4]. The wheel sleeve’s cost is not represented by an ETF expense ratio; it has trading costs, bid-ask spreads, possible assignment costs, and opportunity cost on collateral.

The policy’s fund-level weighted expense ratio before wheel trading costs is:

\[
e_p=(0.60)(0.02\%)+(0.15)(0.15\%)+(0.10)(0.19\%)=0.0535\%.
\]

On $100,000, that is approximately $53.50 per year in stated fund expenses attributable to those three sleeves, assuming the weights stay constant. This number is useful, but it does not describe portfolio risk.

## 3. The first integration problem: overlap

SPYM tracks the S&P 500 [2]. QQQM tracks the Nasdaq-100 [3]. A semiconductor ETF adds another layer of exposure to chip designers, manufacturers and equipment companies. The SEC’s diversification guidance explicitly recommends checking whether the top holdings of multiple funds are genuinely different [1].

The correct calculation is look-through aggregation. If ETF \(j\) has portfolio weight \(W_j\) and company \(i\) has fund weight \(h_{ij}\), the company’s total portfolio weight is:

\[
L_i=\sum_jW_jh_{ij}.
\]

Suppose a hypothetical company is 8% of SPYM, 12% of QQQM and 10% of the semiconductor ETF. Its combined portfolio exposure is:

\[
(0.60)(0.08)+(0.15)(0.12)+(0.10)(0.10)=7.6\%.
\]

The 10% sector sleeve has not created a 1% company position; it has added another 1% to an already large exposure. The workbook therefore includes a holdings-overlap area designed for periodically refreshed issuer data.

## 4. The second integration problem: covariance

Markowitz showed that portfolio risk depends on covariance across assets, not simply on the average of standalone risks [5]. For \(N\) sleeves with weight vector \(w\) and covariance matrix \(\Sigma\):

\[
\sigma_p=\sqrt{w'\Sigma w}.
\]

The companion workbook uses editable assumptions rather than claiming that one historical correlation matrix is permanent. A demonstration set might use annualized volatilities of 18% for SPYM, 24% for QQQM, 35% for the semiconductor sleeve and 12% for the wheel/reserve composite. Correlations among the first three are assumed high because the exposures are related U.S. equities; the wheel/reserve correlation is set lower only because part of that sleeve is cash collateral. These are model inputs, not empirical estimates.

### Calculation table 1 — illustrative risk assumptions

| Sleeve | Weight | Assumed volatility | Standalone weighted volatility \(w\sigma\) |
|---|---:|---:|---:|
| SPYM | 60% | 18% | 10.80% |
| QQQM | 15% | 24% | 3.60% |
| Semiconductor | 10% | 35% | 3.50% |
| Wheel/reserve | 15% | 12% | 1.80% |

The table does **not** mean portfolio volatility is 19.7%; correlations determine how the components combine. Its immediate lesson is that a 10% semiconductor sleeve can have nearly the same standalone weighted-volatility magnitude as a 15% QQQM sleeve.

## 5. Risk contribution is more informative than capital weight

For covariance matrix \(\Sigma\), marginal contribution to risk is:

\[
MCR_i=\frac{(\Sigma w)_i}{\sigma_p},
\]

and component risk contribution is:

\[
RC_i=w_iMCR_i.
\]

The sum of \(RC_i\) equals total portfolio volatility. This lets the investor ask whether a small satellite is consuming an outsized share of the risk budget.

The idea is related to risk-parity thinking, where portfolios are designed around the contribution of assets to total risk rather than dollar weights [6]. This series does not propose a leveraged risk-parity portfolio; it borrows the diagnostic because it is useful for any allocation.

If the 10% semiconductor sleeve contributes 20% of modeled volatility, the policy can respond in three ways: accept the concentration, reduce the sector weight, or add genuinely diversifying exposure elsewhere. Pretending the sleeve is “only 10%” is not a fourth option.

## 6. The third integration problem: option collateral

A cash-secured put creates a contingent obligation to buy 100 shares per standard contract [7]. Therefore, the 15% wheel/reserve sleeve cannot be treated as ordinary cash while a put is open.

For a $100,000 portfolio, the sleeve is $15,000. If one put has a $100 strike:

\[
Collateral=100\times100=\$10,000.
\]

That uses 66.7% of the wheel sleeve before other obligations. If another $100-strike put is sold, required strike collateral rises to $20,000, exceeding the policy sleeve. The strategy has crossed from fully cash secured at the sleeve level into leverage against other portfolio capital.

The workbook therefore separates:

- total cash;
- committed put collateral;
- free tactical cash;
- shares acquired through assignment; and
- option premiums received.

Premium is not subtracted from risk as if it eliminated the obligation. It lowers effective basis but does not cap equity downside.

## 7. Stress testing before optimization

Optimization can create precise answers from uncertain inputs. Stress testing is often more transparent. The investor defines a severe but interpretable market path and calculates the portfolio effect.

Consider this deterministic scenario:

| Sleeve | Weight | Stress return | Portfolio contribution |
|---|---:|---:|---:|
| SPYM | 60% | -30% | -18.00% |
| QQQM | 15% | -40% | -6.00% |
| Semiconductor ETF | 10% | -50% | -5.00% |
| Wheel/reserve | 15% | -25% | -3.75% |
| **Portfolio** | **100%** | — | **-32.75%** |

The wheel/reserve stress assumes some cash cushioning and some assigned equity exposure. Another portfolio could have a different result. What matters is that the policy has a **drawdown conversation before the drawdown occurs**.

If -32.75% would cause the investor to abandon the plan, the portfolio is too aggressive for that loss capacity regardless of expected return estimates.

## 8. Scenario tables are better than one forecast

A single expected-return number encourages false confidence. A scenario grid shows how the same allocation behaves across regimes.

### Calculation table 2 — illustrative regime analysis

| Scenario | SPYM | QQQM | Semiconductor | Wheel/reserve | Portfolio return |
|---|---:|---:|---:|---:|---:|
| Broad bull | +15% | +20% | +28% | +8% | +16.00% |
| Growth-led rally | +10% | +28% | +35% | +6% | +14.60% |
| Sideways / premium-friendly | +2% | 0% | -5% | +7% | +1.75% |
| Inflation/rates shock | -15% | -25% | -30% | -8% | -16.95% |
| Deep risk-off | -30% | -40% | -50% | -25% | -32.75% |

These values are hypothetical. They reveal sensitivity: the portfolio performs very well when U.S. growth and semiconductors lead, but three related equity sleeves can fall together in a growth shock. The wheel may improve a sideways path yet remains exposed in a deep sell-off.

## 9. Rebalancing: calendar, threshold or contribution first

Investor.gov describes rebalancing as restoring a portfolio to its target allocation after market movements cause drift [1]. It identifies both calendar-based and threshold-based approaches and notes that investors can rebalance by selling overweight positions, buying underweight positions, or redirecting new contributions [8].

A practical policy can combine these methods:

- **monitor monthly**;
- **formally review quarterly**;
- **trade only when a band is breached or cash flows permit efficient correction**; and
- **use new contributions first** before taxable sales where appropriate.

For a target \(w_i^*\) and current weight \(w_i\), relative drift is:

\[
D_i=\frac{w_i-w_i^*}{w_i^*}.
\]

If the policy allows ±20% relative drift, a 10% semiconductor target has an 8%–12% range. A 60% SPYM target has a 48%–72% range, which may be too wide for a core sleeve. This illustrates why **different sleeves can use different bands**. A policy might use tighter absolute bands for the core and smaller, proportional bands for volatile satellites.

## 10. Worked rebalancing example

Suppose the portfolio grows from $100,000 to $118,000 with the following values:

| Sleeve | Current value | Current weight | Target weight | Target value | Trade to exact target |
|---|---:|---:|---:|---:|---:|
| SPYM | $73,000 | 61.86% | 60% | $70,800 | -$2,200 |
| QQQM | $19,000 | 16.10% | 15% | $17,700 | -$1,300 |
| Semiconductor | $14,000 | 11.86% | 10% | $11,800 | -$2,200 |
| Wheel/reserve | $12,000 | 10.17% | 15% | $17,700 | +$5,700 |
| **Total** | **$118,000** | **100%** | **100%** | **$118,000** | **$0** |

Exact rebalancing would sell $5,700 from the three equity sleeves and transfer it to the wheel/reserve sleeve. But if a $5,000 new contribution is arriving, the first step can be to allocate it to the underweight reserve. After contribution, the portfolio is $123,000 and new targets should be recalculated. Contribution-first rebalancing can materially reduce sales and turnover.

## 11. Rebalancing is a risk-control rule, not a return prediction

Rebalancing systematically trims relative winners and adds to relative losers. It can be uncomfortable because the investor is asked to sell what looks strongest and buy what looks weakest. Investor.gov explicitly notes that this can be psychologically difficult [1].

The purpose is not to guarantee a rebalancing bonus. It is to keep the portfolio near the intended risk profile. If a satellite doubles and grows from 10% to 20%, the portfolio is no longer the one originally approved. Rebalancing makes the risk decision again using policy rather than momentum.

The exception is when the **policy thesis itself changes**. If a fund changes benchmark, an investor’s time horizon shortens, or the option sleeve no longer fits liquidity needs, blindly returning to the old target is not disciplined. The correct process is to amend the policy first, document why, and then rebalance to the new targets.

## 12. Expected returns: use ranges and sensitivity

Expected returns are uncertain. Black and Litterman’s portfolio framework is useful because it treats market equilibrium as a starting point and then incorporates investor views according to confidence rather than replacing the entire portfolio with the strongest view [9]. The general lesson is applicable even without implementing the full model: **uncertain views should produce bounded tilts**.

The workbook therefore uses editable expected-return assumptions and a sensitivity table instead of hard-coded claims that one sleeve “will” return a particular percentage. For example:

| Sleeve | Low case | Base illustration | High case |
|---|---:|---:|---:|
| SPYM | 4% | 7.5% | 10% |
| QQQM | 3% | 8.5% | 12% |
| Semiconductor | 0% | 9.5% | 15% |
| Wheel/reserve | 2% | 6% | 9% |

The expected portfolio return under any column is the weighted sum. In the base illustration:

\[
E[R_p]=(0.60)(7.5)+(0.15)(8.5)+(0.10)(9.5)+(0.15)(6)=7.625\%.
\]

That 7.625% is not a forecast. It is an auditable consequence of visible assumptions.

## 13. Costs: distinguish known from uncertain

Fund expense ratios are relatively easy to verify from issuer pages. Trading costs and taxes are more account-specific. A robust model therefore separates:

**Known/observable inputs:** stated expense ratios, contract multiplier, target weights, current values.

**Market-sensitive inputs:** spreads, implied volatility, option premium, interest rates, current holdings weights.

**Assumptions:** expected returns, volatilities, correlations, stress shocks, tax rates.

**Rules:** rebalance bands, maximum sector weight, collateral ceiling, single-name cap.

Mixing those categories is a common modeling error. A current 0.19% SOXQ expense ratio is a sourced input [4]; a 9.5% semiconductor expected return is an assumption. They should not be formatted or described as if they had the same evidentiary status.

## 14. Risk governance for the semiconductor sleeve

A sector satellite should have three controls.

First, a **target weight** and maximum. Second, a **look-through company concentration limit** after combining the core and satellite. Third, a **thesis review rule** that distinguishes temporary underperformance from a structural change in the industry or benchmark.

One possible educational rule set is:

- target 10%;
- review below 8% or above 12%;
- do not allow the satellite alone to exceed 15%;
- flag any company whose combined look-through exposure exceeds 8%;
- compare the fund’s benchmark and fee annually with alternatives.

The numbers are illustrative. The point is to make concentration an explicit policy variable rather than a surprise discovered after a rally.

## 15. Risk governance for the wheel sleeve

The wheel needs different controls because its exposure is nonlinear and capital commitments can change with assignment.

A policy can require:

- puts to be fully cash secured at the sleeve level;
- calls to be covered by owned shares;
- maximum collateral utilization, such as 80% of wheel capital;
- maximum post-assignment exposure to one underlying;
- no use of emergency liquidity as option collateral;
- premiums tracked separately from mark-to-market equity P&L;
- all trades benchmarked against simply holding the underlying.

OIC’s strategy pages emphasize that both cash-secured puts and covered calls can involve substantial losses even though premium is received [10], [11]. The governance rules should reflect that reality.

## 16. Monitoring dashboard

A dashboard should surface policy exceptions, not invite daily trading. The key questions are whether any sleeve has breached its range, how much wheel capital is committed, how concentrated technology exposure has become, which sleeve dominates modeled risk, and whether the severe-stress loss remains tolerable. A warning flag therefore means **review required**, not automatic trading.

## 17. Model risk and false precision

Portfolio models are decision aids, not forecasts. Expense ratios and option expiration payoffs can be specified precisely; expected returns, correlations and volatilities cannot. The workbook therefore separates sourced facts from assumptions, keeps assumptions editable, and places stress tests beside point estimates. This reduces the risk that a spreadsheet’s numerical precision is mistaken for economic certainty.

## 18. A quarterly portfolio review process

A disciplined quarterly review can:

1. update market values and sourced ETF facts;
2. recalculate weights, overlap and risk contributions;
3. test target-band breaches;
4. review committed option collateral and assignment exposure;
5. refresh scenarios only when the regime or assumptions materially change;
6. compare wheel results with simply holding the underlying;
7. rebalance with cash flows first where practical; and
8. archive the dated model and rationale.

The process is intentionally slower than the news cycle because the strategic core should not be redesigned around short-term headlines.

## 19. What the integrated portfolio is—and is not

The worked policy is a **U.S.-equity-heavy core-satellite portfolio with growth, semiconductor and options tilts**. It is not a complete household balance sheet: it omits dedicated bonds, emergency liquidity, currency matching, tax-residence analysis and estate planning. Those issues should be handled at the broader wealth-management layer rather than forced into the U.S. sleeve.

## 20. Final construction principles

Five principles summarize the series: benchmark before ticker; name every tilt explicitly; model option obligations rather than premiums alone; allocate risk as well as capital; and govern the portfolio with target weights, bands, collateral limits, verified data and periodic review. These controls are knowable. Future market returns are not.

## 21. Takeaways

A 60% SPYM core, 15% QQQM growth tilt, 10% semiconductor satellite and 15% wheel/reserve sleeve can be coherent when managed as one system. Tests are concentration, stress losses, collateral utilization and rebalancing discipline.

Under the illustrative deep risk-off scenario, the portfolio loses 32.75%. This is not a forecast but a governance test of survivability. Rebalancing restores the design instead of predicting the next market move; Investor.gov recognizes calendar, threshold and cash-flow approaches [1], [8].

The goal is not promised outperformance, but an auditable portfolio that explains what it owns, why each sleeve exists, how obligations are funded, and which rules apply when markets move sharply.

---

# Appendix A — Integrated formulas

### A.1 Weighted fund expense ratio

\[
e_p=\sum_iw_ie_i.
\]

### A.2 Look-through security exposure

\[
L_i=\sum_jW_jh_{ij}.
\]

### A.3 Expected return under an assumption set

\[
E[R_p]=w'\mu.
\]

### A.4 Portfolio volatility

\[
\sigma_p=\sqrt{w'\Sigma w}.
\]

### A.5 Component risk contribution

\[
RC_i=w_i\frac{(\Sigma w)_i}{\sigma_p}.
\]

### A.6 Deterministic stress loss

\[
Stress_p=\sum_iw_iShock_i.
\]

### A.7 Exact rebalance trade

\[
Trade_i=w_i^*V-V_i.
\]

### A.8 Relative drift

\[
D_i=\frac{w_i-w_i^*}{w_i^*}.
\]

### A.9 Cash-secured put collateral

\[
Collateral=K\times100\times N.
\]

### A.10 Free tactical cash

\[
FreeCash=WheelCash-CommittedCollateral-OtherObligations.
\]

# Appendix B — Workbook control hierarchy

**Inputs:** portfolio value, target weights, current sleeve values, expected returns, volatilities, correlations, scenario shocks, option strikes, premiums and contract counts.

**Sourced facts:** ETF expense ratios, benchmarks, option multiplier and current issuer information. Each sourced fact should carry an as-of date and URL.

**Calculated outputs:** weighted fee, target-dollar values, rebalance trades, portfolio expected return under assumptions, covariance matrix, modeled volatility, component risk, stress returns, wheel collateral, effective basis and option payoff.

**Policy flags:** weight outside band, sector concentration above limit, collateral utilization above ceiling, free cash below floor, or source data older than the review interval.

# Appendix C — Publication and audit checklist

Before publishing an update to this five-part series, verify each ETF fact against the issuer’s current website; verify index descriptions against the index provider; confirm any academic citation by DOI or publisher page; remove stale ticker or fee claims; label market data with an as-of date; recalculate every table from the workbook; test spreadsheet formulas for errors; confirm article word counts; ensure every in-text IEEE citation has a matching reference; archive the source URLs; and state clearly which numerical inputs are illustrative assumptions.

# Appendix D — Boundaries of the model

This workbook does not model personal taxes, foreign-exchange costs, U.S. estate-tax exposure, Kenyan tax treatment, broker-specific margin rules, assignment fees or real-time option Greeks. Those can materially change implementation for a cross-border investor. They should be added only with jurisdiction-specific, current sources. The absence of those layers is a model boundary, not an assumption that the costs are zero.

# References

[1] U.S. Securities and Exchange Commission, “Asset Allocation and Diversification,” Investor.gov, 2026. [Online]. Available: https://www.investor.gov/introduction-investing/getting-started/asset-allocation. [Accessed: Sep. 11, 2026].

[2] State Street Investment Management, “SPYM: State Street SPDR Portfolio S&P 500 ETF,” 2026. [Online]. Available: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-500-etf-spym. [Accessed: Sep. 11, 2026].

[3] Invesco, “Invesco NASDAQ 100 ETF (QQQM), Q2 2026,” Jun. 30, 2026. [Online]. Available: https://www.invesco.com/us-rest/contentdetail?contentId=5b4d8e58e0737710VgnVCM1000006e36b50aRCRD. [Accessed: Sep. 11, 2026].

[4] Invesco, “Invesco PHLX Semiconductor ETF (SOXQ),” 2026. [Online]. Available: https://www.invesco.com/us/en/financial-products/etfs/invesco-phlx-semiconductor-etf.html. [Accessed: Sep. 11, 2026].

[5] H. Markowitz, “Portfolio selection,” *The Journal of Finance*, vol. 7, no. 1, pp. 77–91, Mar. 1952, doi: 10.1111/j.1540-6261.1952.tb01525.x.

[6] E. Qian, “Risk parity portfolios: Efficient portfolios through true diversification,” PanAgora Asset Management, Sep. 2005. [Online]. Available: https://www.panagora.com/wp-content/uploads/2011/09/PanAgora-Risk-Parity-Portfolios-Efficient-Portfolios-Through-True-Diversification.pdf. [Accessed: Sep. 11, 2026].

[7] The Options Clearing Corporation, “Equity Options Product Specifications,” 2026. [Online]. Available: https://www.theocc.com/clearance-and-settlement/clearing/equity-options-product-specifications. [Accessed: Sep. 11, 2026].

[8] U.S. Securities and Exchange Commission and FINRA, “Investor Bulletin: Year-End Investment Considerations for Individual Investors,” Dec. 6, 2012. [Online]. Available: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-70. [Accessed: Sep. 11, 2026].

[9] F. Black and R. Litterman, “Global portfolio optimization,” *Financial Analysts Journal*, vol. 48, no. 5, pp. 28–43, Sep.–Oct. 1992, doi: 10.2469/faj.v48.n5.28.

[10] The Options Industry Council, “Cash-Secured Put,” 2026. [Online]. Available: https://www.optionseducation.org/strategies/all-strategies/cash-secured-put. [Accessed: Sep. 11, 2026].

[11] The Options Industry Council, “Covered Call (Buy/Write),” 2026. [Online]. Available: https://www.optionseducation.org/strategies/all-strategies/covered-call-buy-write. [Accessed: Sep. 11, 2026].

[12] Financial Industry Regulatory Authority, “Asset Allocation and Diversification,” 2026. [Online]. Available: https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification. [Accessed: Sep. 11, 2026].
