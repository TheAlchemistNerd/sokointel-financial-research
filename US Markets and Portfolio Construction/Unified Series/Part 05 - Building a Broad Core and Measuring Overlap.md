# Part 05: Building a Broad Core and Measuring Overlap

*US Markets and Portfolio Construction, unified nine-part series. Research edition: 15 September 2026.*

A broad market fund, a growth index and a headline fee can look simple. This chapter identifies the benchmark, overlap, concentration and full portfolio job behind each choice.

## Series scope

A portfolio is easier to manage when every holding has a job. The starting job in this series is **core exposure**: a low-cost, rules-based allocation intended to capture a large share of the long-run return of U.S. listed equities without requiring repeated security selection. Two widely available examples are **SPYM**, which tracks the S&P 500, and **QQQM**, which tracks the Nasdaq-100. This article uses dated issuer and index information to compare their economic exposure, cost and role in a portfolio.

As of September 2026, State Street reports a **0.02% gross expense ratio** for SPYM and describes it as a low-cost S&P 500 portfolio building block [1]. S&P Dow Jones Indices describes the S&P 500 as a float-adjusted market-capitalization-weighted index covering roughly 80% of available U.S. market capitalization [2]. Invesco reports a **0.15% total expense ratio** for QQQM, while Nasdaq describes the Nasdaq-100 as 100 of the largest non-financial Nasdaq-listed companies, using a modified market-cap weighting process [3], [4]. Those facts make the pair inexpensive and transparent, but they do **not** make the exposures interchangeable.

This is educational portfolio-construction analysis, not a recommendation to buy or sell a security. Returns, volatility and scenario assumptions used below are illustrative inputs for showing the mathematics. They are not forecasts.

## 1. Start with the benchmark, not the ticker

A common mistake is to compare ETFs only by fee, price per share or brand. The more fundamental question is: **what economic exposure does the benchmark deliver?** The ticker is a wrapper around an index mandate.

SPYM seeks to track the S&P 500 before fees and expenses [1]. The S&P 500 is a broad large-cap U.S. equity benchmark. In late August 2026, the index remained meaningfully concentrated in its largest constituents: S&P Dow Jones Indices reported that the top ten represented 37.8% of the index [2]. That concentration is an important reminder that “500 stocks” does not mean “500 equal-sized bets.” Market-cap weighting intentionally gives the largest companies the largest weights.

QQQM, by contrast, tracks the Nasdaq-100 [3]. Nasdaq defines the index around 100 large **non-financial** companies listed on Nasdaq and notes that it is heavily weighted toward technology while also containing consumer discretionary, healthcare and other sectors [4]. It is therefore better understood as a large-cap growth/innovation tilt than as a complete substitute for broad U.S. equity exposure. The absence of financial companies is structural, not temporary.

That difference gives a useful construction principle:

> **A broad-market core and a growth index can coexist, but the second allocation should be treated as an intentional tilt because many of its largest companies are already present in the broad core.**

If 60% of a portfolio is in SPYM and 15% is in QQQM, the portfolio is not “75% diversified U.S. equities” in the naïve sense of two independent sleeves. It is 60% broad U.S. large-cap beta plus an additional 15% tilt toward the Nasdaq-100 universe. The overlap can increase exposure to the same mega-cap growth companies. That may be desirable, but it should be an explicit decision rather than an accidental by-product of owning two famous ETFs.

## 2. SPYM as the broad core

State Street’s current product page reports that SPYM’s benchmark is the S&P 500, its gross expense ratio is 0.02%, and options are available on the fund [1]. The product was formerly known under a different ticker in the historical research trail, which explains why older notes and web pages may use SPLG. For present-day implementation, the current ticker and current prospectus information should control.

The S&P 500 itself is designed to represent leading U.S. large-cap companies and uses float-adjusted market capitalization weighting [2]. This matters operationally. A cap-weighted core automatically lets winners become larger positions and lets declining firms become smaller positions unless index rules remove them. The investor does not need to rebalance every company back to an arbitrary equal weight.

The main strengths of SPYM as a core are therefore structural rather than predictive:

- very low stated fund expenses;
- broad large-cap U.S. coverage through a widely followed benchmark;
- transparent index methodology;
- high diversification relative to single-stock portfolios; and
- low ongoing decision load once the target allocation is established.

The limitations are equally important. SPYM is still an equity fund, so it can experience severe drawdowns. It is not a complete global portfolio, it does not provide dedicated small-cap exposure, and current S&P 500 concentration means mega-cap companies can dominate results. An investor who calls it “safe” simply because it holds hundreds of companies is confusing diversification with capital protection. The SEC notes that ETF prices fluctuate and may trade above or below net asset value, while equity investments remain exposed to market risk [5].

## 3. QQQM as a deliberate growth tilt

QQQM’s role is more specific. Invesco’s June 2026 fund material reports a 0.15% total expense ratio and identifies the Nasdaq-100 as its underlying index [3]. Nasdaq’s current description states that the index comprises 100 large non-financial Nasdaq-listed companies and uses modified market-cap weighting [4]. It is therefore concentrated by design in a narrower opportunity set than the S&P 500.

The narrower set can be useful when the portfolio objective includes an explicit tilt toward large innovative and growth-oriented businesses. But the same feature creates concentration risk. Adding QQQM to SPYM is not equivalent to adding a diversifying asset class such as high-quality bonds, international equities or cash equivalents. In many market environments, SPYM and QQQM can be driven by the same U.S. mega-cap companies, rates, earnings expectations and risk appetite.

That means the correct mental model is **core + tilt**, not **core + independent diversifier**.

A 60% SPYM / 15% QQQM structure can therefore be written as:

\[
w_{US}=w_{SPYM}+w_{QQQM}=0.60+0.15=0.75
\]

but its economic factor exposure is more concentrated than that arithmetic suggests. If a company has weight \(a\) in SPYM and weight \(b\) in QQQM, its look-through portfolio weight from these two sleeves is:

\[
w_{company}=0.60a+0.15b.
\]

This equation is simple but important. The duplicated exposure is additive. The workbook accompanying this series includes an editable overlap/tilt worksheet so that holdings data can be updated rather than hard-coded forever.

## 4. Comparing QQQ and QQQM with current facts

A long-horizon fee comparison should use the current legal form and stated expense ratio. Invesco announced that, effective in December 2025, QQQ became an open-end ETF and its expense ratio moved to **0.18%** [6]. QQQM remains at **0.15%** [3].

The long-term cost gap therefore still exists, but it is smaller than the old 5-basis-point comparison implied by 0.20% versus 0.15%. It is now approximately 3 basis points before considering bid-ask spreads, brokerage costs, tax, securities lending effects, tracking difference and implementation details.

QQQ may still have advantages for some tactical traders because of its very deep trading ecosystem. Invesco describes QQQ as one of the most actively traded ETFs in the United States [6]. For a buy-and-hold investor who wants the same Nasdaq-100 benchmark and does not need QQQ’s trading depth, the lower stated expense ratio of QQQM remains economically relevant. The decision, however, should be framed using **current** fund structures and fees.

### Calculation table 1: fee-only drag on a static $100,000 position

The table below isolates the expense ratio. It assumes the underlying portfolio earns 8.00% before fund expenses every year and that the fee reduces that return mechanically. Real tracking differences will not equal the expense ratio exactly.

| Fund | Expense ratio | Net illustrative return | Value after 10 years | Value after 20 years | Value after 30 years |
|---|---:|---:|---:|---:|---:|
| SPYM | 0.02% | 7.98% | $215,493 | $464,372 | $1,000,690 |
| QQQM | 0.15% | 7.85% | $212,913 | $453,318 | $965,171 |
| QQQ | 0.18% | 7.82% | $212,321 | $450,803 | $957,150 |

Formula:

\[
FV=P(1+r-e)^n
\]

where \(P\) is starting capital, \(r\) is the assumed gross return, \(e\) is the annual expense ratio and \(n\) is years. The table is a sensitivity illustration, not a prediction of any ETF’s future return.

The lesson is not that the lowest fee always wins. A three- or thirteen-basis-point fee difference cannot compensate for selecting the wrong benchmark. **Exposure first, cost second, implementation third** is a more defensible hierarchy.

## 5. Why apparently tiny fees matter

Annual expense ratios are easy to dismiss because 0.02%, 0.15% and 0.18% all look small. Compounding changes the perspective. A recurring cost applies not only to original capital but also to the gains that would otherwise remain invested.

For a portfolio with contributions, a simplified future-value calculation is:

\[
FV=P(1+i)^n+C\left(\frac{(1+i)^n-1}{i}\right),
\]

where \(i=r-e\) and \(C\) is an annual end-of-year contribution. The workbook calculates this dynamically across user-selected horizons and returns.

### Calculation table 2: annual fee dollars at different account sizes

| Portfolio value | SPYM at 0.02% | QQQM at 0.15% | QQQ at 0.18% |
|---:|---:|---:|---:|
| $10,000 | $2 | $15 | $18 |
| $50,000 | $10 | $75 | $90 |
| $100,000 | $20 | $150 | $180 |
| $500,000 | $100 | $750 | $900 |
| $1,000,000 | $200 | $1,500 | $1,800 |

These are simple annualized expense-ratio equivalents, not invoices charged separately to an account. They help quantify scale: the difference between 0.02% and 0.15% is $1,300 per year on $1 million, before compounding. That is worth optimizing **after** the benchmark choice is correct.

## 6. Portfolio theory: diversification is about covariance

Markowitz’s foundational portfolio-selection framework shows why counting tickers is a weak measure of diversification [7]. Portfolio risk depends on individual asset variances and on how returns co-move. For two risky sleeves:

\[
\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\sigma_1\sigma_2\rho_{12}.
\]

If two equity funds share many constituents and similar economic sensitivities, \(\rho_{12}\) may be high. The second ETF can still change expected return and risk, but the diversification benefit may be smaller than the number of tickers suggests.

This is why QQQM should be sized as a tilt. If the desired policy is 60% SPYM and 15% QQQM, the remaining 25% should be evaluated according to what risk it adds or offsets. A semiconductor ETF, for example, intensifies a technology bet. A cash reserve reduces equity beta. An options wheel on equities may reshape the payoff but can remain highly exposed to equity downside. Local-market assets can add different currency and economic exposures but may also introduce country, liquidity and governance risks. Those are topics for later parts of this series.

## 7. An illustrative core policy

Consider a $100,000 educational portfolio with a policy allocation of 60% SPYM and 15% QQQM, leaving 25% for satellites and reserves.

| Sleeve | Policy weight | Dollar allocation | Primary job |
|---|---:|---:|---|
| SPYM | 60% | $60,000 | Broad U.S. large-cap beta |
| QQQM | 15% | $15,000 | Nasdaq-100 growth tilt |
| Satellite/reserve | 25% | $25,000 | Deliberate active, sector, income or diversification roles |
| **Total** | **100%** | **$100,000** | |

The policy is not justified merely because the percentages are tidy. It should survive four questions.

First, **can the investor tolerate the drawdown implied by 75% U.S. equity exposure?** Second, **does the QQQM tilt intentionally increase growth and technology sensitivity?** Third, **what is the 25% satellite expected to do that SPYM and QQQM do not already do?** Fourth, **what rule determines when positions are rebalanced?**

If those questions do not have written answers, the allocation is a collection of holdings rather than a portfolio policy.

## 8. Contribution-first rebalancing

Rebalancing does not always require selling. FINRA describes rebalancing as the process of returning a portfolio toward its intended allocation when market movements cause weights to drift [8]. Investors can use new contributions to buy underweight sleeves before selling overweight holdings.

Suppose the $100,000 policy above grows to the following values:

| Sleeve | Current value | Current weight | Target weight | Target value at $108,000 | Gap |
|---|---:|---:|---:|---:|---:|
| SPYM | $67,000 | 62.04% | 60% | $64,800 | -$2,200 |
| QQQM | $17,000 | 15.74% | 15% | $16,200 | -$800 |
| Satellite/reserve | $24,000 | 22.22% | 25% | $27,000 | +$3,000 |
| **Total** | **$108,000** | **100%** | **100%** | **$108,000** | **$0** |

A $3,000 new contribution directed entirely to the satellite/reserve sleeve would restore the portfolio almost exactly without selling the appreciated ETFs. In a taxable account, that can reduce turnover, although tax outcomes depend on jurisdiction and individual circumstances.

## 9. Liquidity is part of total implementation cost

Expense ratios are visible, but transaction costs also matter. ETF shares trade in secondary markets, and the SEC notes that market price can differ from NAV [5]. The relevant implementation variables include bid-ask spread, market depth, order size and execution method.

For a long-term accumulator making periodic purchases, a one- or two-basis-point spread may be economically minor relative to decades of fund expenses. For an options trader or institutional-sized tactical position, market depth can matter much more. This explains why the “cheapest ETF” and the “best trading vehicle” need not be the same ticker.

State Street’s own comparison of SPY and SPYM frames the distinction similarly: SPYM is positioned as a low-cost long-term S&P 500 building block, while SPY’s trading ecosystem can matter to frequent or tactical users [9]. That is an implementation argument, not evidence that one benchmark is superior. The funds target the same S&P 500 exposure.

## 10. Concentration and the false comfort of broad labels

The S&P 500 is broad, but it is not equally weighted. Nasdaq-100 is diversified across many companies, but it is not a total-market index. As of August 31, 2026, S&P Dow Jones Indices reported a 37.8% top-ten concentration for the S&P 500 and an information-technology sector weight of 37.9% [2]. Those numbers will change, so they belong in a dated research snapshot rather than a permanent policy assumption.

The portfolio implication is that adding QQQM and then adding a semiconductor ETF can compound exposure to similar drivers. A useful governance test is to classify every satellite as one of three things:

1. **Diversifier**: intended to behave differently from the core in important states of the world.
2. **Return tilt**: intentionally increases exposure to a factor, sector or theme already partly present.
3. **Payoff modifier**: changes the distribution of outcomes, such as an options overlay that exchanges some upside for premium.

QQQM is primarily a **return tilt** relative to SPYM. Calling it a diversifier would overstate what the second ticker accomplishes.

## 11. What not to optimize

Portfolio construction becomes fragile when the investor optimizes variables that do not determine economic outcomes. The nominal share price of an ETF is a weak example; fractional-share availability can make it nearly irrelevant. Last year’s performance ranking is another. A low expense ratio is useful, but only after confirming benchmark fit. A high distribution yield is not the same as a high total return.

The more durable variables are benchmark design, diversification, costs, tax and account constraints, liquidity needs, behavior under drawdown, and written rebalancing rules. The SEC’s ETF guidance encourages investors to read the prospectus and understand objectives, risks, charges and expenses before investing [5]. That is less exciting than chasing a leaderboard, but it is exactly the discipline a core allocation is supposed to create.

## 12. Decision framework: SPYM, QQQM or both?

The choice can be summarized without pretending there is one universally correct allocation.

| Question | If “yes,” implication |
|---|---|
| Do I want broad U.S. large-cap market exposure as the foundation? | SPYM is designed for that role. |
| Do I deliberately want more Nasdaq-100/growth exposure than the S&P 500 already provides? | QQQM can be sized as a tilt. |
| Do I need the deepest tactical trading ecosystem on the Nasdaq-100? | Compare QQQ implementation benefits with QQQM’s lower expense ratio using current data. |
| Am I adding QQQM because recent performance is exciting? | Revisit the thesis; that is performance chasing, not policy design. |
| Have I measured overlap with any sector satellite? | Do so before adding more technology concentration. |
| Is my time horizon short or my loss capacity low? | Reconsider how much of the portfolio belongs in equities at all. |

The critical distinction is between **product selection** and **asset allocation**. Product selection asks which wrapper efficiently delivers a chosen exposure. Asset allocation asks how much exposure belongs in the portfolio. The second question normally has the larger impact on risk.

## 13. Takeaways

SPYM and QQQM are credible low-cost tools, but they solve different problems. SPYM provides broad S&P 500 large-cap exposure at a stated 0.02% expense ratio [1]. QQQM provides Nasdaq-100 exposure at 0.15% [3]. The combination can make sense when QQQM is treated explicitly as a growth tilt layered onto a broad core.

A current QQQ and QQQM comparison begins with their then-current legal structures and stated fees: QQQ is no longer a UIT and now carries a 0.18% expense ratio after its December 2025 modernization [6]. QQQM still has the lower stated fee, but benchmark fit and trading requirements should come before a three-basis-point fee difference.

The next article broadens the framework. Core-satellite is only one portfolio architecture. We will compare core, core-plus, barbell, factor-tilted, risk-parity, concentrated and portable-alpha concepts and show which ideas transfer cleanly from institutional portfolios to a practical ETF portfolio, and which do not.

---

# Appendix A: Core calculations

### A.1 Weighted expense ratio

For a portfolio with fund weights \(w_i\) and expense ratios \(e_i\):

\[
e_p=\sum_i w_ie_i.
\]

For 60% SPYM, 15% QQQM and 25% cash with an assumed zero product expense:

\[
e_p=(0.60)(0.0002)+(0.15)(0.0015)=0.000345=0.0345\%.
\]

On $100,000, that corresponds to approximately $34.50 of annual fund expenses attributable to those two sleeves, before any expenses on the remaining 25% and ignoring tracking difference and transaction costs.

### A.2 Look-through company exposure

If company X is 8% of SPYM and 12% of QQQM:

\[
w_X=(0.60)(0.08)+(0.15)(0.12)=0.066=6.6\%.
\]

This is why duplicated constituents should be evaluated at the portfolio level rather than fund by fund.

### A.3 Rebalancing trade to target

If total portfolio value is \(V\), target weight is \(w_i^*\), and current sleeve value is \(V_i\), then:

\[
Trade_i=w_i^*V-V_i.
\]

Positive values are purchases; negative values are sales. The workbook also includes a contribution-first version that allocates new cash to underweight positions before generating sells.

# Appendix B: Data governance checklist

Before updating the model, record: the source URL, access date, reported effective date, expense-ratio definition (gross or net), benchmark name, ticker changes, corporate actions, and whether the value is static or market-sensitive. Do not copy a stale fee from an old article when the issuer’s current page is available. Do not mix index constituent counts with ETF holding counts without labeling them. Do not treat historical returns as forecasts. Preserve a dated snapshot so future revisions can distinguish a real product change from a transcription error.

# Appendix C: Workbook linkages

The accompanying workbook contains editable sheets for ETF inputs, fee drag, allocation, risk/covariance assumptions, options-wheel payoff math, rebalancing and scenarios. Blue-font cells are intended as user inputs; formula cells derive from those assumptions. The workbook uses the same fee figures and benchmark definitions cited here so that prose and calculations remain auditable.

### Publication note

Before publication, refresh each issuer fact sheet and confirm that the benchmark, fee, holdings count and fund structure remain current. Recalculate the fee tables if any expense ratio changes. The portfolio examples are educational policy illustrations, not individualized recommendations, and should be interpreted alongside the investor’s tax, currency, liquidity and total-wealth constraints.

# References

[1] State Street Investment Management, “SPYM: State Street SPDR Portfolio S&P 500 ETF,” 2026. [Online]. Available: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-500-etf-spym. [Accessed: Sep. 11, 2026].

[2] S&P Dow Jones Indices, “S&P 500,” 2026. [Online]. Available: https://www.spglobal.com/spdji/en/indices/equity/sp-500/. [Accessed: Sep. 11, 2026].

[3] Invesco, “Invesco NASDAQ 100 ETF (QQQM), Q2 2026,” Jun. 30, 2026. [Online]. Available: https://www.invesco.com/us-rest/contentdetail?contentId=5b4d8e58e0737710VgnVCM1000006e36b50aRCRD. [Accessed: Sep. 11, 2026].

[4] Nasdaq, “What is the Nasdaq-100? A Guide to One of the World’s Most-Watched Indexes,” Aug. 19, 2026. [Online]. Available: https://www.nasdaq.com/newsroom/what-is-the-nasdaq-100-guide-to-one-of-worlds-most-watched-indexes. [Accessed: Sep. 11, 2026].

[5] U.S. Securities and Exchange Commission, Office of Investor Education and Advocacy, “Updated Investor Bulletin: Exchange-Traded Funds (ETFs),” Feb. 23, 2023. [Online]. Available: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-24. [Accessed: Sep. 11, 2026].

[6] Invesco, “What’s new about QQQ?” Dec. 22, 2025. [Online]. Available: https://www.invesco.com/qqq-etf/en/market-outlook/whats-new-about-qqq.html. [Accessed: Sep. 11, 2026].

[7] H. Markowitz, “Portfolio selection,” *The Journal of Finance*, vol. 7, no. 1, pp. 77–91, Mar. 1952, doi: 10.1111/j.1540-6261.1952.tb01525.x.

[8] Financial Industry Regulatory Authority, “Asset Allocation and Diversification,” 2026. [Online]. Available: https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification. [Accessed: Sep. 11, 2026].

[9] State Street Investment Management, “Comparing SPY and SPYM: Two State Street ETFs for S&P 500 exposure,” 2026. [Online]. Available: https://www.ssga.com/us/en/intermediary/insights/comparing-spy-and-spym-two-state-street-etfs-for-s-p-500-exposure. [Accessed: Sep. 11, 2026].

## Technical companion

A holdings list becomes a concentration measure through:

\[
HHI = \sum_{i=1}^{N}w_i^2, \qquad N_{\mathrm{effective}} = \frac{1}{HHI}.
\]

The [concentration appendix](<Appendices/Appendix 03 - Concentration and Effective Holding Count.md>) derives the equal-weight case and shows how to use a complete holdings file.
