# Part 2 — Beyond Core-Satellite: Choosing a Portfolio Architecture Before Choosing More Funds

## Series scope

Part 1 established a practical distinction between a **broad core** and a **deliberate tilt**. The next question from the supplied research notes is more structural: if core-satellite and core-plus are only two ways to organize a portfolio, what other architectures exist, and when do they make sense?

The answer requires some cleanup because investment vocabulary travels badly across asset classes. Terms such as **core, core-plus, value-add and opportunistic** are widely used in private real estate and infrastructure to describe increasing levels of leverage, operating intensity and business-plan risk. In a liquid ETF portfolio, however, the more useful architecture labels are things such as **strategic allocation, core-satellite, factor tilt, barbell, concentrated/high-conviction, risk parity, portable alpha and tactical allocation**. Reusing a real-estate risk ladder as if it were a universal equity taxonomy can create false precision.

This article therefore treats the original notes as a design prompt, not as an authority. The objective is to identify the economic logic behind each architecture, show the mathematics that makes the differences visible, and build rules for deciding whether a new sleeve genuinely changes the portfolio.

This is educational analysis. Illustrative weights and expected returns are model assumptions, not forecasts or recommendations.

## 1. Architecture is the layer above security selection

Portfolio construction has at least three levels:

1. **Objective:** What problem is the capital supposed to solve?
2. **Architecture:** How will risk and decision rights be divided across sleeves?
3. **Implementation:** Which securities, ETFs, funds or derivatives deliver those sleeves?

Investors often start at level three. They discover a fund, compare fees, and only later ask how it fits with everything else. A stronger process starts with architecture. Markowitz’s portfolio-selection framework formalized the idea that portfolio risk depends not only on each asset’s standalone risk, but on covariance among holdings [1]. That immediately implies that “more holdings” is not a complete design principle.

The architecture should answer questions such as: Which return sources are strategic and which are tactical? How much active risk is allowed? Which sleeve is permitted to deviate from the market? What happens after a 30% drawdown? How often is the policy reviewed? When can a satellite be removed?

Without those rules, a portfolio can drift from an intentional system into a collection of overlapping convictions.

## 2. Strategic market-cap core

The simplest architecture is a predominantly strategic allocation to broad, low-cost beta. In the U.S. equity portion, an S&P 500 ETF such as SPYM is an example of an implementation vehicle, not the architecture itself. State Street describes SPYM as a low-cost S&P 500 building block, while S&P Dow Jones Indices describes the index as float-adjusted market-cap weighted [2], [3].

A pure core structure minimizes the number of discretionary decisions. Its principal advantages are low cost, transparency and behavioral simplicity. Its principal limitation is that the investor accepts the benchmark’s concentration, sector weights and valuation without attempting to correct them.

For a portfolio that is 100% strategic core, the active weight relative to the benchmark is approximately zero before implementation frictions. In simplified notation:

\[
ActiveWeight_i=w_{portfolio,i}-w_{benchmark,i}.
\]

If all holdings replicate the benchmark, the sum of absolute active weights is small. This architecture therefore bets mainly on long-run market beta rather than manager skill or tactical timing.

## 3. Core-satellite

Core-satellite keeps most capital in a low-cost market portfolio and allocates a smaller amount to higher-conviction sleeves. The attraction is governance. The investor can isolate experimentation, sector tilts or active management without allowing those decisions to dominate the entire portfolio.

Suppose the policy is 75% strategic core and 25% satellites. If the core has expected return \(\mu_c\), satellite return \(\mu_s\), and the sleeves have weights \(w_c\) and \(w_s\), then expected portfolio return is:

\[
E[R_p]=w_c\mu_c+w_s\mu_s.
\]

But risk is not a weighted average of volatilities. For two sleeves:

\[
\sigma_p^2=w_c^2\sigma_c^2+w_s^2\sigma_s^2+2w_cw_s\sigma_c\sigma_s\rho_{cs}.
\]

That covariance term explains why a technology satellite can raise portfolio risk more than its 10% weight suggests when the core is already technology-heavy.

The supplied notes propose a U.S. core using SPYM and QQQM, plus satellites such as semiconductor ETFs and an options wheel. That can be coherent if the jobs are explicit. SPYM is broad beta; QQQM is a growth tilt; a semiconductor ETF is a narrower sector tilt; the wheel is a payoff-management strategy. The architecture fails if every satellite is justified by the same thesis—“technology will outperform”—because apparent sleeve diversification masks a single underlying bet.

## 4. Core-plus: useful concept, dangerous ambiguity

“Core-plus” can mean different things depending on the asset class. In fixed income, it can describe a high-quality bond core with limited allocations to credit sectors outside a traditional aggregate benchmark. In real estate, it often describes assets with somewhat more operating or leverage risk than stabilized core properties. In a personal public-markets portfolio, the phrase is best used descriptively rather than as a standardized category.

A practical interpretation is:

> **Core-plus = a strategic core plus a bounded set of return-enhancing exposures whose risk budget is explicitly limited.**

That is close to core-satellite, but the distinction is philosophical. Core-satellite emphasizes separate sleeves; core-plus emphasizes controlled deviation around a central strategic portfolio. The danger is using “plus” as permission to add anything with higher expected return. A genuine plus sleeve requires a risk limit, implementation rule and exit criterion.

A useful metric is the **satellite loss budget**. If a $100,000 portfolio permits at most a 5% portfolio loss from a specific tactical sleeve in a severe scenario, and the scenario assumes that sleeve can fall 50%, its maximum policy weight is:

\[
w_{max}=\frac{5\%}{50\%}=10\%.
\]

This reverses the normal process. Instead of choosing 10% because it “feels diversified,” the weight is derived from a tolerated portfolio-level loss.

## 5. Factor-tilted core

A factor architecture keeps a diversified base but systematically overweights characteristics such as value, size, profitability/quality or momentum. Fama and French’s 1993 paper documented common risk factors in stock and bond returns and helped establish the empirical foundation for systematic factor analysis [4]. Factor investing does not require predicting individual companies; it changes exposure rules at the portfolio level.

For a factor-tilted core, a simplified return model is:

\[
R_p=\alpha+\beta_M R_M+\beta_V R_V+\beta_S R_S+\epsilon,
\]

where \(R_M\) is the market factor and the additional terms represent chosen factor exposures. The central governance question becomes: **which factor is being paid for, and how long can the portfolio tolerate underperformance?**

Factor tilts are not free diversification. They can lag broad benchmarks for years. If an investor abandons the tilt after a long drought, the architecture can produce the worst of both worlds: active risk on the way down and benchmark chasing on the way back up.

## 6. Barbell architecture

A barbell deliberately combines two very different risk profiles and holds less in the middle. The concept can be implemented in many ways: short-duration safe assets plus aggressive equities; broad beta plus a small venture-like sleeve; or cash/Treasury bills plus concentrated high-volatility opportunities.

The benefit is intuitive: one side preserves liquidity and optionality while the other side provides convex upside or high expected growth. The weakness is that the aggressive side can still dominate total risk.

Consider an illustrative $100,000 barbell:

| Sleeve | Weight | Assumed annual volatility | Dollar amount |
|---|---:|---:|---:|
| T-bill/cash reserve | 40% | 1% | $40,000 |
| Broad equity | 40% | 18% | $40,000 |
| High-volatility satellite | 20% | 40% | $20,000 |

Ignoring covariance for a moment, the volatility contributions scale with \(w_i\sigma_i\): 0.4%, 7.2% and 8.0%. The 20% satellite has the largest standalone risk contribution despite being half the weight of the broad equity sleeve. This is why capital weights are not risk weights.

The barbell is useful when the investor values a large liquidity reserve and consciously accepts a small high-risk sleeve. It is less useful when “safe side” cash is repeatedly raided to average down speculative positions, because that destroys the architecture’s asymmetry.

## 7. Risk parity

Risk parity shifts the design target from equal capital allocation to more balanced **risk contribution**. Edward Qian’s early formulation describes risk-parity portfolios as allocating market risk across asset classes rather than allowing the highest-volatility asset to dominate [5].

For portfolio covariance matrix \(\Sigma\) and weight vector \(w\), portfolio volatility is:

\[
\sigma_p=\sqrt{w'\Sigma w}.
\]

The marginal contribution to risk of asset \(i\) is:

\[
MCR_i=\frac{(\Sigma w)_i}{\sigma_p},
\]

and total risk contribution is:

\[
RC_i=w_iMCR_i.
\]

A risk-parity target attempts to make the \(RC_i\) values similar, subject to constraints. This often produces larger capital weights in lower-volatility assets and smaller weights in high-volatility equities. Some institutional implementations then use leverage to raise total portfolio risk, which introduces financing and deleveraging risks that may be inappropriate for many individuals.

The idea that transfers well to a personal portfolio is not necessarily leverage; it is the **risk-contribution diagnostic**. The workbook in this series calculates marginal and component risk using editable volatility and correlation assumptions so an investor can see whether a 10% satellite is quietly contributing 25% of modeled risk.

## 8. Concentrated / high-conviction architecture

A concentrated portfolio abandons or reduces the diversified core and puts more capital behind a smaller set of views. This can create meaningful outperformance if the views are correct, but it also increases idiosyncratic risk and the dispersion of outcomes.

William Sharpe’s “The Arithmetic of Active Management” provides a useful baseline: before costs, the average actively managed dollar must collectively equal the market before costs; after higher costs, average active performance must be lower than the market average [6]. That does not say no active investor can outperform. It says active outperformance is competitive and should not be assumed simply because a strategy is selective.

A concentrated architecture therefore requires a stronger governance burden than a core-satellite portfolio: position limits, thesis documentation, sell rules, liquidity standards, and a method for distinguishing a broken thesis from temporary volatility.

### Calculation table 1 — concentration loss mapping

| Position weight | Position drawdown | Portfolio impact before correlations |
|---:|---:|---:|
| 5% | -50% | -2.5% |
| 10% | -50% | -5.0% |
| 20% | -50% | -10.0% |
| 30% | -50% | -15.0% |

The table makes the risk budget visible. A “high-conviction 20% position” is also a willingness to accept a 10% portfolio loss if that holding halves, before considering knock-on correlation effects.

## 9. Portable alpha

Portable alpha separates **beta exposure** from **alpha generation**. In institutional form, derivatives can provide inexpensive benchmark exposure while capital is deployed to an independent return-seeking strategy. The idea is conceptually elegant: do not force the alpha manager to own the same securities required for benchmark beta.

For a retail investor, however, portable alpha is easy to misuse. Derivatives introduce collateral, basis, counterparty/clearing, liquidity and path-dependent risks. A personal portfolio that owns a broad ETF and then sells options on the same equity risk is not automatically “portable alpha.” The active strategy must be evaluated after fees and against its true risk exposures.

A simplified decomposition is:

\[
R_{total}=R_{beta}+R_{alpha}-C_{funding}-C_{implementation}.
\]

If the “alpha” return is simply compensation for selling downside insurance, it may become strongly correlated with equity losses in stressed markets. Labeling it alpha does not make it independent.

Black and Litterman’s global portfolio-optimization framework is relevant here because it begins from equilibrium returns and then allows investor views to tilt the portfolio according to confidence [7]. The larger lesson is that views should be **scaled**, not merely asserted.

## 10. Tactical allocation

Tactical allocation deliberately changes weights in response to valuation, trend, macroeconomic or other signals. It can sit on top of a strategic policy or replace part of it. The problem is not that tactical allocation is inherently invalid; the problem is that discretionary market timing is difficult to evaluate without a pre-specified rule.

A tactical sleeve should therefore identify:

- signal definition;
- decision frequency;
- maximum deviation from strategic weights;
- turnover and tax assumptions;
- benchmark for evaluating the tactical decision; and
- conditions under which the process is stopped.

If a tactical portfolio raises cash after prices fall and buys again only after prices recover, the timing rule may systematically crystallize losses. Backtests should include transaction costs and should avoid tuning dozens of parameters to one historical sample.

## 11. A practical architecture matrix

The following matrix translates theory into portfolio jobs.

| Architecture | Primary objective | Main risk | Governance burden | Good fit for low-cost ETFs? |
|---|---|---|---|---|
| Strategic core | Capture market beta | Market drawdown | Low | Excellent |
| Core-satellite | Preserve core, isolate active bets | Satellite overlap / style drift | Moderate | Excellent |
| Core-plus | Bounded enhancement around core | “Plus” sleeve creep | Moderate | Good |
| Factor tilt | Systematic non-market exposure | Long underperformance cycles | Moderate | Good |
| Barbell | Combine liquidity/safety with high upside | Risk dominated by aggressive side | Moderate | Good |
| Risk parity | Balance risk contributions | Model error; leverage in some versions | High | Possible |
| Concentrated | Maximize impact of conviction | Idiosyncratic loss | High | Possible |
| Portable alpha | Separate beta and active return source | Derivative/funding/hidden beta risk | Very high | Limited |
| Tactical allocation | Vary exposures through time | Timing/model error | High | Good mechanically |

No architecture is universally superior. The best one is the architecture whose failure modes the investor can understand and tolerate.

## 12. Applying the framework to the supplied U.S. portfolio concept

The research notes repeatedly return to five building blocks: SPYM, QQQM, an options wheel, local shares and offshore investing. For the U.S.-markets series, we can isolate the U.S. elements and map them to jobs.

An illustrative architecture is:

- **60% SPYM — strategic U.S. large-cap core**;
- **15% QQQM — explicit large-cap growth tilt**;
- **10% semiconductor ETF — sector satellite**;
- **15% wheel/cash reserve — tactical payoff sleeve and collateral reserve**.

This is more informative than saying “75% core, 25% satellite” because it reveals that QQQM is not neutral core in the same sense as SPYM. It also reveals that the semiconductor sleeve can overlap with both existing ETFs, while the wheel sleeve may still have equity downside if assignment occurs.

### Calculation table 2 — risk-budget thought experiment

Assume the following severe, simultaneous sleeve shocks purely for stress testing:

| Sleeve | Weight | Stress return | Contribution to portfolio stress |
|---|---:|---:|---:|
| SPYM | 60% | -30% | -18.0% |
| QQQM | 15% | -40% | -6.0% |
| Semiconductor ETF | 10% | -50% | -5.0% |
| Wheel/reserve | 15% | -20% | -3.0% |
| **Portfolio** | **100%** | — | **-32.0%** |

This deterministic stress test is not a forecast and ignores dynamic option behavior. Its purpose is governance. If a modeled -32% portfolio event is intolerable, arguing about whether one ETF charges 0.19% or 0.35% is secondary. Architecture dominates product-level fee optimization.

## 13. Rebalancing architecture

FINRA notes that diversification and asset allocation can drift as markets move, making periodic rebalancing relevant [8]. Three common governance styles are:

**Calendar rebalancing:** review quarterly, semiannually or annually. It is simple but can trade even when drift is trivial.

**Threshold rebalancing:** trade when a sleeve moves outside a band, such as ±20% of its target weight. A 10% target with a 20% relative band would trigger below 8% or above 12%.

**Contribution-first rebalancing:** direct new capital and distributions toward underweight sleeves before selling. This can reduce turnover.

The formula for relative drift is:

\[
Drift_i=\frac{w_i-w_i^*}{w_i^*}.
\]

A policy can then trigger when \(|Drift_i|>b\), where \(b\) is the chosen band.

## 14. Architecture should constrain behavior

A good portfolio architecture is partly a behavioral technology. During a rally, it limits how much a successful satellite can grow before rebalancing. During a crash, it prevents a defensive reserve from being reclassified impulsively as “dry powder for one more speculative bet.” During a period of underperformance, it requires the investor to compare outcomes with a pre-defined thesis instead of with the best-performing asset on social media.

That is why written rules matter. Investor.gov and FINRA both emphasize the relationship among goals, risk, asset allocation and diversification [8], [9]. A portfolio policy can be concise: target weights, allowable ranges, eligible instruments, review dates, maximum position size, liquidity floor and conditions for changing the strategic allocation.

## 15. Which architecture belongs in this series?

For the U.S. portfolio described in the notes, a **core-satellite / bounded core-plus hybrid** is the cleanest interpretation. The broad S&P 500 exposure does the heavy lifting. QQQM is a named growth tilt rather than “more diversification.” A semiconductor ETF is a smaller sector satellite. The wheel is an active sleeve whose capital requirement and downside must be modeled separately.

Risk-parity mathematics can still be used diagnostically even if the investor never builds a leveraged risk-parity portfolio. Barbell thinking is useful for protecting a collateral reserve. Factor analysis is useful for understanding that repeated technology sleeves may all load on the same growth factor. Portable-alpha language is best avoided unless beta and alpha are genuinely separated.

The architecture should simplify the portfolio, not provide sophisticated labels for complexity.

## 16. Takeaways

The most useful lesson from the original “what other variants exist?” question is that portfolio architecture is not a menu of fashionable names. Each architecture is a rule for allocating **capital, risk and decision authority**.

Strategic core minimizes active decisions. Core-satellite contains active bets. Core-plus permits bounded deviations. Factor portfolios systematize tilts. Barbells separate conservative and aggressive exposures. Risk parity targets risk contribution rather than capital weight. Concentrated portfolios accept idiosyncratic risk in exchange for conviction. Portable alpha separates beta implementation from active return sources. Tactical allocation changes exposures through time and therefore requires explicit timing rules.

For a practical U.S. ETF portfolio, core-satellite remains a strong default precisely because it is auditable. The next article applies that architecture to the semiconductor sleeve and asks a harder question than “which chip ETF is cheapest?”: **what benchmark methodology, concentration and overlap are we actually buying?**

---

# Appendix A — Architecture formulas

### A.1 Portfolio expected return

\[
E[R_p]=\sum_{i=1}^{N}w_iE[R_i].
\]

### A.2 Portfolio variance

\[
\sigma_p^2=w'\Sigma w.
\]

### A.3 Marginal contribution to risk

\[
MCR_i=\frac{(\Sigma w)_i}{\sigma_p}.
\]

### A.4 Component contribution to risk

\[
RC_i=w_iMCR_i.
\]

The sum of component risk contributions equals portfolio volatility under this decomposition.

### A.5 Satellite loss budget

\[
w_{satellite,max}=\frac{L_{portfolio,max}}{|L_{satellite,stress}|}.
\]

This converts a tolerated portfolio loss into a maximum satellite weight under a specified stress scenario.

# Appendix B — Architecture review worksheet

For each sleeve, document: purpose; benchmark; target weight; minimum and maximum weight; expected holding period; source of expected return; principal risk; correlation thesis; liquidity requirement; fee; turnover; tax considerations; rebalancing trigger; thesis-break condition; and whether the sleeve is strategic, tactical, diversifying, return-seeking or payoff-modifying. A sleeve with no distinct answer should be challenged as redundant.

# Appendix C — Workbook implementation

The master workbook supplied with this series implements a four-sleeve covariance model, component risk calculations, target-versus-current allocation, relative drift bands and deterministic scenario testing. Expected-return, volatility and correlation entries are deliberately editable assumptions. They are not presented as historical estimates. This keeps the model useful even when market conditions change and prevents dated assumptions from masquerading as permanent facts.

### Implementation note

Architecture should be reviewed whenever the investor’s objectives, liabilities, liquidity needs or time horizon change materially. A new ETF, factor or tactical idea should enter the portfolio only after its role, benchmark, risk budget, funding source and rebalancing rule are specified. This keeps product selection subordinate to portfolio design and prevents a watchlist from becoming an accidental strategy. The expected reason for holding it should also be documented.

# References

[1] H. Markowitz, “Portfolio selection,” *The Journal of Finance*, vol. 7, no. 1, pp. 77–91, Mar. 1952, doi: 10.1111/j.1540-6261.1952.tb01525.x.

[2] State Street Investment Management, “SPYM: State Street SPDR Portfolio S&P 500 ETF,” 2026. [Online]. Available: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-500-etf-spym. [Accessed: Sep. 11, 2026].

[3] S&P Dow Jones Indices, “S&P 500,” 2026. [Online]. Available: https://www.spglobal.com/spdji/en/indices/equity/sp-500/. [Accessed: Sep. 11, 2026].

[4] E. F. Fama and K. R. French, “Common risk factors in the returns on stocks and bonds,” *Journal of Financial Economics*, vol. 33, no. 1, pp. 3–56, Feb. 1993, doi: 10.1016/0304-405X(93)90023-5.

[5] E. Qian, “Risk parity portfolios: Efficient portfolios through true diversification,” PanAgora Asset Management, Sep. 2005. [Online]. Available: https://www.panagora.com/wp-content/uploads/2011/09/PanAgora-Risk-Parity-Portfolios-Efficient-Portfolios-Through-True-Diversification.pdf. [Accessed: Sep. 11, 2026].

[6] W. F. Sharpe, “The arithmetic of active management,” *Financial Analysts Journal*, vol. 47, no. 1, pp. 7–9, Jan.–Feb. 1991, doi: 10.2469/faj.v47.n1.7.

[7] F. Black and R. Litterman, “Global portfolio optimization,” *Financial Analysts Journal*, vol. 48, no. 5, pp. 28–43, Sep.–Oct. 1992, doi: 10.2469/faj.v48.n5.28.

[8] Financial Industry Regulatory Authority, “Asset Allocation and Diversification,” 2026. [Online]. Available: https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification. [Accessed: Sep. 11, 2026].

[9] U.S. Securities and Exchange Commission, “Tips for 2026 Investors,” Investor.gov, Mar. 31, 2026. [Online]. Available: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/investorgov-tips-2026-investor-bulletin. [Accessed: Sep. 11, 2026].
