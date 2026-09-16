# Part 07: Options Income as a Tactical Sleeve

*US Markets and Portfolio Construction, unified nine-part series. Research edition: 15 September 2026.*

Options income changes a portfolio's payoff profile and operating burden. It needs a separate mandate, collateral rule and stress test.

## Series scope

A strategic U.S. ETF core can be paired with an **options wheel** intended to generate premium income. The wheel is often explained as a simple loop: sell a cash-secured put, accept assignment if it occurs, sell a covered call on the acquired shares, and repeat when the shares are called away. Mechanically, that description is correct. Economically, it is incomplete.

An option seller receives premium because the seller accepts an obligation. A cash-secured put can lead to the purchase of 100 shares at the strike price even after the market has fallen sharply. A covered call can cap upside precisely when the stock rallies strongly. The wheel therefore does not manufacture yield from nothing; it **reshapes the distribution of equity returns**.

The U.S. Securities and Exchange Commission’s updated 2026 options bulletin emphasizes that options involve rights and obligations and can expose investors to substantial losses [1]. The Options Clearing Corporation states that a standard equity option normally represents 100 shares of the underlying security [2]. The Options Industry Council describes a cash-secured put as a short put combined with enough cash to buy the stock if assigned [3], and a covered call as a short call backed by an equivalent long stock position [4]. Those definitions form the basis of the calculations below.

This is educational analysis. The examples use hypothetical prices, premiums and strikes and are not trade recommendations.

![The cash-secured-put, assignment and covered-call cycle of an options wheel.](/static/site/us-wheel-cycle.png "Options wheel cycle")

## 1. What the wheel is actually doing

A wheel strategy has two states.

**State A: cash-secured put:** The investor holds cash collateral and sells a put option. If the option expires out of the money, the investor keeps the premium and can sell another put. If assigned, the investor buys shares at the strike price.

**State B: covered call:** The investor owns the shares and sells a call. If the call expires out of the money, the shares remain in the account and another call can be sold. If assigned, the shares are sold at the call strike.

The strategy is “circular” only operationally. From a risk perspective, the two states are linked by the same underlying equity. A falling share price turns the cash-secured put into long stock exposure; a continuing fall then affects the covered-call phase. The strategy therefore has substantial equity beta.

The wheel is best classified as a **tactical payoff-modification satellite**, not a bond substitute and not a guaranteed-income product.

## 2. The cash-secured put payoff

Let:

- \(K_p\) = put strike;
- \(P_p\) = premium received per share;
- \(S_T\) = stock price at expiration;
- \(N\) = number of option contracts;
- multiplier = 100 shares per standard contract [2].

The short-put profit at expiration per share is:

\[
\Pi_{put}=P_p-\max(K_p-S_T,0).
\]

For a fully cash-secured position, required strike collateral is approximately:

\[
Collateral=K_p\times100\times N.
\]

Premium cash received is:

\[
Premium=P_p\times100\times N.
\]

If assigned, the effective acquisition cost before commissions and tax is:

\[
Basis=K_p-P_p.
\]

### Calculation table 1: one hypothetical cash-secured put

Assume a stock trades at $102. An investor sells one 30-day $95 put for a $2.40 premium.

| Item | Calculation | Result |
|---|---:|---:|
| Strike collateral | $95 multiplied by 100 | $9,500 |
| Premium received | $2.40 multiplied by 100 | $240 |
| Effective purchase basis if assigned | $95 - $2.40 | $92.60/share |
| Maximum profit at expiration | Premium | $240 |
| Breakeven at expiration | $95 - $2.40 | $92.60 |
| Severe downside if stock goes to $0 | $9,500 - $240 | $9,260 loss |

The $240 premium can feel like “income,” but the last row reveals the economic trade. The premium is small relative to the capital at risk. OIC explicitly notes that the maximum loss of a cash-secured put is limited but substantial because the assigned stock can theoretically fall to zero [3].

## 3. Scenario analysis for the put

Using the same $95 strike and $2.40 premium:

| Stock at expiration | Option outcome | Put P&L | Effective position consequence |
|---:|---|---:|---|
| $110 | Expires worthless | +$240 | Cash remains available |
| $100 | Expires worthless | +$240 | Cash remains available |
| $95 | At strike | +$240 | Assignment possible depending on exercise/settlement details |
| $90 | Assigned / intrinsic loss $5 | -$260 | Shares effectively acquired at $92.60 basis |
| $80 | Assigned / intrinsic loss $15 | -$1,260 | Material unrealized equity loss |
| $50 | Assigned / intrinsic loss $45 | -$4,260 | Large loss despite premium |

The put seller is effectively saying: **I am willing to own this security at the strike and can tolerate owning it even if the market price is much lower when assignment occurs.** If that statement is not true, the wheel begins with a contradiction.

## 4. Premium yield is not annual return

A common presentation error is to annualize a 30-day option premium mechanically and call the result an expected annual return.

In the example, premium divided by strike collateral is:

\[
Yield_{30d}=\frac{240}{9500}=2.526\%.
\]

A naïve simple annualization would be:

\[
2.526\%\times\frac{365}{30}=30.7\%.
\]

That number is **not** a forecasted annual portfolio return. It assumes the same premium can be earned repeatedly, ignores losses and assignment, ignores changing volatility, ignores idle days, ignores transaction costs, and assumes capital can always be redeployed at the same economics. Annualized premium yield can be a standardized comparison metric, but it should never be presented as guaranteed income.

A more honest wheel workbook tracks realized cash flows, assignment basis, open share P&L, call-away proceeds and total capital at risk.

## 5. The covered call payoff

After assignment, suppose the investor owns 100 shares at an effective basis \(B\). The investor sells one call with strike \(K_c\) for premium \(P_c\).

At expiration, ignoring prior put premium if it has already been incorporated into basis, covered-call profit per share can be written:

\[
\Pi_{cc}=S_T-B+P_c-\max(S_T-K_c,0).
\]

If the stock finishes above the call strike and the shares are called away, maximum profit over the covered-call phase is:

\[
MaxProfit=(K_c-B+P_c)\times100.
\]

The downside remains substantial because the long stock can decline almost to zero. OIC states that the covered call’s maximum gain is limited while maximum loss remains substantial; the premium provides only a small downside cushion [4].

### Calculation table 2: covered call after put assignment

Continue the earlier example. Shares have effective basis $92.60. The investor sells one $100 call for $2.00.

| Stock at call expiration | Call outcome | Share value / sale | Call premium | Total P&L from $92.60 basis |
|---:|---|---:|---:|---:|
| $70 | Expires worthless | $7,000 | +$200 | -$2,060 |
| $90 | Expires worthless | $9,000 | +$200 | -$60 |
| $95 | Expires worthless | $9,500 | +$200 | +$440 |
| $100 | At/above strike | ~$10,000 sale if assigned | +$200 | +$940 |
| $110 | Shares called at $100 | $10,000 | +$200 | +$940 |
| $130 | Shares called at $100 | $10,000 | +$200 | +$940 |

The final two rows demonstrate the covered call’s central trade-off. Once called away at $100, the investor no longer participates in upside above the strike during that option cycle. The premium compensated the investor for accepting that cap.

## 6. Full-cycle wheel accounting

Suppose the original put premium is $240, the investor is assigned at $95, then sells a $100 covered call for $200, and the shares are eventually called away at $100.

Cash flows are:

1. Put premium: +$240.
2. Assignment purchase: -$9,500.
3. Call premium: +$200.
4. Call-away sale: +$10,000.

Net profit:

\[
240-9500+200+10000=\$940.
\]

Capital measured against the $9,500 strike collateral gives a simple cycle return of:

\[
\frac{940}{9500}=9.89\%.
\]

That is a realized return for this **hypothetical path**, not a general return expectation. If instead the shares fall to $70 and the call expires, the account has received $440 of total premiums but owns stock worth $7,000 after paying $9,500. Mark-to-market P&L is approximately -$2,060, exactly as the table shows.

The wheel does not remove the need to analyze the underlying security.

## 7. Assignment is not a failure, unless the position was unsuitable

Assignment is built into option selling. A cash-secured put should be sold only if acquiring the shares is acceptable. A covered call should be sold only if selling the shares at the strike is acceptable. Schwab’s educational material on the wheel makes the same operational point: the strategy cycles through put assignment and covered calls and is not guaranteed to be profitable [5].

This creates two thesis tests:

**Put test:** “Would I be comfortable buying 100 shares at this strike if the stock is trading 20% lower by assignment day?”

**Call test:** “Would I be comfortable selling 100 shares at this strike if the stock rallies 25% immediately afterward?”

If either answer is no, the selected strike or underlying may be inconsistent with the strategy.

## 8. Why capital size matters

Standard option contracts normally control 100 shares [2]. That creates lumpy capital requirements. At a $95 put strike, one cash-secured contract requires approximately $9,500 of strike collateral. At a $300 strike, one contract requires $30,000.

This matters for portfolio construction. A $25,000 tactical sleeve cannot run a fully cash-secured wheel on every high-priced ETF without allowing one contract to dominate the sleeve. Smaller-share-price vehicles can improve granularity, but nominal share price alone should not override liquidity and benchmark considerations.

### Calculation table 3: contract concentration

| Put strike | Cash collateral for 1 contract | % of a $25,000 wheel sleeve |
|---:|---:|---:|
| $50 | $5,000 | 20% |
| $100 | $10,000 | 40% |
| $150 | $15,000 | 60% |
| $250 | $25,000 | 100% |
| $400 | $40,000 | 160%: cannot be fully cash secured by the sleeve alone |

A wheel strategy can therefore create **position-size risk through the contract multiplier**, even before market risk is considered.

## 9. SPYM/QQQM as investment holdings versus options underlyings

Long-term ETF selection and options implementation answer different operational questions. A low-cost ETF can be attractive for buy-and-hold accumulation yet have a thinner options market than a flagship trading vehicle. State Street reports that options are available on SPYM [6], but availability is only the first filter. A trader should also inspect live bid-ask spreads, open interest, volume and strike availability before entering a contract.

For the Nasdaq-100, QQQ’s long-established trading ecosystem may be more useful for active derivatives than QQQM even though QQQM has the lower expense ratio. Invesco modernized QQQ in 2025 and reduced its expense ratio to 0.18%, while QQQM’s stated fee remains 0.15% [7], [8]. This is another example of **separating the long-term holding vehicle from the tactical instrument**.

The portfolio does not need one ticker to perform every job.

## 10. The hidden beta in “income” strategies

Calling option premium “income” can obscure risk. Selling a put is economically similar to accepting downside exposure below the strike in exchange for premium. Owning stock and selling a call retains most of the stock’s downside while giving up upside above the strike during the option term.

The resulting return distribution can have many small positive premium observations and occasional large losses. That pattern can look stable until a sharp decline. The correct risk metric therefore includes **maximum drawdown, tail scenarios and assigned equity exposure**, not just monthly premium collected.

An options sleeve should be aggregated with the rest of the equity portfolio. If the wheel uses a technology stock already represented in SPYM, QQQM and a semiconductor ETF, assignment can increase the same underlying factor exposure at the worst possible time.

## 11. Cash collateral is part of the portfolio

Cash reserved for a cash-secured put is not idle in an economic sense: it is supporting a contingent purchase obligation. It should not also be counted as an emergency fund, a rebalance reserve and available capital for a second trade.

A simple collateral rule is:

\[
FreeCash=Cash-CSP\ Collateral-Other\ Obligations.
\]

If free cash becomes negative after considering all open puts, the portfolio is not fully cash secured. Margin can change broker requirements, but it also changes risk. The SEC warns that margin can magnify losses and create forced-sale risk [9]. For an educational core-satellite framework, the cleanest baseline is to model wheel puts as fully cash secured and calls as fully covered by owned shares.

## 12. Strike selection is a risk decision, not an income target

Investors sometimes choose strikes by asking, “How much premium do I want this month?” That reverses the correct logic. The strike determines the price at which ownership or sale becomes acceptable; premium is compensation for taking that obligation.

For puts, a lower strike generally provides more downside distance but receives less premium, all else equal. For covered calls, a higher strike preserves more upside but usually receives less premium. Volatility, time to expiration, interest rates and dividends also affect option prices.

A written policy can specify:

- eligible underlyings;
- maximum contract count;
- maximum collateral as a percentage of portfolio value;
- minimum free-cash reserve;
- whether assignment is always accepted or sometimes managed before expiration;
- maximum single-name look-through exposure after assignment; and
- whether calls may be written on strategic core holdings.

The last point matters. Writing calls on a holding that the investor is unwilling to sell can create a behavioral conflict during a rally.

## 13. Early exercise and operational details

OCC notes that standard U.S. equity options are generally American-style, meaning exercise can occur before expiration [2]. Assignment risk can therefore arise before the final trading day. Dividend timing, deep-in-the-money options and remaining time value can influence exercise behavior.

The SEC also notes that brokers require customers to be approved for options trading based on factors such as financial situation, investment experience and objectives [10]. Investors should receive the OCC’s *Characteristics and Risks of Standardized Options* disclosure document before trading [11].

These operational rules are not administrative trivia. A portfolio model that assumes every contract sits untouched until expiration may not match real brokerage outcomes.

## 14. Taxes and cross-border investors

The economic examples in this article are pre-tax. Realized option premiums, assignment basis, capital gains, withholding and account reporting can depend on tax residence, broker jurisdiction, instrument and holding period. For a non-U.S. investor, additional cross-border tax and estate-planning questions may also arise.

Those issues belong in a dedicated international-investing analysis rather than being guessed inside a U.S. options article. The safe design rule is to keep a **pre-tax strategy model** separate from a **jurisdiction-specific tax layer** and obtain professional advice where required.


### U.S. tax mechanics for U.S. taxpayers

The cross-border framework in Part 3 remains relevant for non-U.S. investors. For a U.S. taxpayer, the tax layer also requires the character and timing of each cash flow to be recorded. Qualified dividends can be taxed at long-term capital-gains rates when statutory holding-period and other requirements are met. Non-qualified dividends are generally taxed as ordinary income. On an illustrative $1,000 dividend at a 15% qualified-dividend rate and a 24% ordinary rate, the after-tax cash is $850 and $760 respectively. The $90 difference does not make a fund suitable by itself. It shows why the cash-flow character belongs in the after-tax comparison [12].

A wash sale can defer a loss when substantially identical securities are acquired within the statutory window around a loss sale. If 100 shares bought at $50 are sold at $40 and all 100 are repurchased at $41 within the window, the $1,000 loss is disallowed currently and is added to the replacement shares' basis. Appendix 4 shows the corresponding partial-repurchase calculation. Options, shares and related funds require fact-specific treatment, so a trade ledger should record dates, identifiers, quantities and replacement positions [12].

Long-term capital-gains brackets also interact with ordinary taxable income. A gain that spans a bracket can be taxed partly at different rates. The companion workbook makes the bracket arithmetic visible using the 2026 thresholds cited in Revenue Procedure 2025-32. It is a planning illustration, not tax advice. Asset location therefore begins with the investor's account types, tax residence, liquidity needs and trading turnover rather than a simple rule that one asset class always belongs in one account [12], [13].

## 15. Wheel performance should be benchmarked correctly

A wheel is not successful merely because premium is positive. A useful benchmark asks what would have happened if the same capital had simply held the underlying or a broad index over the same period.

Define:

\[
ExcessReturn=R_{wheel}-R_{benchmark}.
\]

Then adjust for risk, cash utilization and taxes where appropriate. If the wheel earns 8% while the underlying rises 25%, the strategy may have performed exactly as designed by trading upside for premium, but “8% income” should not be presented as superior without context. Conversely, in a flat market, option premium may improve outcomes relative to buy-and-hold.

The correct question is whether the payoff profile fits the portfolio objective, not whether each month produced cash.

## 16. An illustrative wheel sleeve inside the wider portfolio

Take the illustrative policy used elsewhere in the series:

| Sleeve | Weight | Job |
|---|---:|---|
| SPYM | 60% | Broad U.S. large-cap core |
| QQQM | 15% | Growth tilt |
| Semiconductor ETF | 10% | Sector tilt |
| Wheel / collateral reserve | 15% | Tactical premium and contingent equity purchase |

On a $100,000 portfolio, the wheel sleeve is $15,000. If one put contract requires $9,500 collateral, 63.3% of the sleeve is committed to one underlying. A second identical contract would require $19,000, exceeding the sleeve. This constraint is useful: it prevents the strategy from quietly expanding simply because another attractive premium appears.

A policy can state that any assignment causing total look-through exposure to one company to exceed, for example, 8% of portfolio value requires review. The threshold is an illustrative governance rule, not a universal standard.

## 17. Stress test the wheel with the whole portfolio

Suppose the portfolio enters a broad risk-off event. SPYM falls 30%, QQQM falls 40%, the semiconductor sleeve falls 50%, and the wheel’s underlying falls 45% after put assignment. A wheel that had collected 4% of collateral in premiums over several months still suffers a large equity loss.

If the wheel sleeve is 15% and its net stress return is -35% after premiums, its direct portfolio contribution is:

\[
0.15\times(-35\%)=-5.25\%.
\]

The premium reduces the loss, but it does not convert the sleeve into a defensive asset. This is the correct way to integrate the strategy with portfolio risk.

## 18. Governance checklist before each option cycle

Before opening a cash-secured put, document the underlying thesis, strike, premium, expiration, collateral, effective basis, maximum post-assignment position weight and the reason you are willing to own the shares. Before writing a covered call, document share basis, call strike, maximum sale price, upside surrendered, and whether you are genuinely willing to lose the shares.

After expiration or assignment, record realized premium and mark-to-market equity P&L separately. Do not report only cumulative premium. This prevents a common accounting illusion in which the strategy appears profitable because cash premiums are visible while an assigned stock loss sits unrealized.

## 19. Takeaways

The option wheel is best understood as a structured sequence of **short-option obligations** around an equity position. A cash-secured put exchanges downside purchase obligation for premium. A covered call exchanges some upside for premium while retaining substantial share-price downside. Standard contracts normally control 100 shares, so capital sizing can become lumpy [2].

The strategy can serve as a bounded tactical satellite when the investor has enough collateral, understands assignment, wants to own the underlying at the put strike, is willing to sell at the call strike and measures results against an appropriate benchmark. It should not be treated as a guaranteed yield engine or a substitute for low-risk fixed income.

The final article integrates all four building blocks: SPYM, QQQM, a semiconductor satellite and a wheel sleeve, into one governed portfolio. It adds scenario analysis, covariance-based risk, rebalancing bands, implementation rules and a workbook structure that makes assumptions transparent rather than hiding them in prose.

---

# Appendix A: Option payoff formulas

### A.1 Short cash-secured put at expiration

\[
\Pi_{put}=100N\left[P_p-\max(K_p-S_T,0)\right].
\]

### A.2 Effective assigned basis

\[
Basis=K_p-P_p.
\]

If prior transaction costs are material, include them in basis according to the accounting/tax convention applicable to the investor.

### A.3 Covered call at expiration

\[
\Pi_{cc}=100N\left[S_T-B+P_c-\max(S_T-K_c,0)\right].
\]

### A.4 Called-away profit

\[
\Pi_{max}=100N(K_c-B+P_c).
\]

### A.5 Collateral utilization

\[
Utilization=\frac{Total\ CSP\ strike\ collateral}{Wheel\ sleeve\ capital}.
\]

A policy can set a utilization ceiling below 100% to preserve operational liquidity.

# Appendix B: Workbook fields for each trade

Record trade ID, underlying, option type, dates, contracts, strike, premium, multiplier, fees, collateral, share basis, assignment status, called-away proceeds, cycle P&L, benchmark return, and rule exceptions. Keep option and share P&L separate.

# Appendix C: Failure modes to test

Test worthless puts, assignment with recovery, assignment followed by further decline, stock rallying through the call strike, and higher volatility or spreads that make closing or rolling costly. These paths show why wheel returns are path dependent.

# References

[1] U.S. Securities and Exchange Commission, Office of Investor Education and Advocacy, “An Introduction to Options: Investor Bulletin,” updated Jul. 16, 2026. [Online]. Available: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-63. [Accessed: Sep. 11, 2026].

[2] The Options Clearing Corporation, “Equity Options Product Specifications,” 2026. [Online]. Available: https://www.theocc.com/clearance-and-settlement/clearing/equity-options-product-specifications. [Accessed: Sep. 11, 2026].

[3] The Options Industry Council, “Cash-Secured Put,” 2026. [Online]. Available: https://www.optionseducation.org/strategies/all-strategies/cash-secured-put. [Accessed: Sep. 11, 2026].

[4] The Options Industry Council, “Covered Call (Buy/Write),” 2026. [Online]. Available: https://www.optionseducation.org/strategies/all-strategies/covered-call-buy-write. [Accessed: Sep. 11, 2026].

[5] Charles Schwab, “Three Things to Know About the Wheel Strategy,” May 6, 2025. [Online]. Available: https://www.schwab.com/learn/story/three-things-to-know-about-wheel-strategy. [Accessed: Sep. 11, 2026].

[6] State Street Investment Management, “SPYM: State Street SPDR Portfolio S&P 500 ETF,” 2026. [Online]. Available: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-500-etf-spym. [Accessed: Sep. 11, 2026].

[7] Invesco, “What’s new about QQQ?” Dec. 22, 2025. [Online]. Available: https://www.invesco.com/qqq-etf/en/market-outlook/whats-new-about-qqq.html. [Accessed: Sep. 11, 2026].

[8] Invesco, “Invesco NASDAQ 100 ETF (QQQM), Q2 2026,” Jun. 30, 2026. [Online]. Available: https://www.invesco.com/us-rest/contentdetail?contentId=5b4d8e58e0737710VgnVCM1000006e36b50aRCRD. [Accessed: Sep. 11, 2026].

[9] U.S. Securities and Exchange Commission, “Understanding Margin Accounts,” Investor.gov. [Online]. Available: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-29. [Accessed: Sep. 11, 2026].

[10] U.S. Securities and Exchange Commission, “Opening an Options Trading Account,” Investor.gov, updated Jul. 16, 2026. [Online]. Available: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-77. [Accessed: Sep. 11, 2026].

[11] The Options Clearing Corporation, “Characteristics and Risks of Standardized Options,” 2026. [Online]. Available: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document. [Accessed: Sep. 11, 2026].

[12] Internal Revenue Service, "Publication 550: Investment Income and Expenses," 2026. [Online]. Available: https://www.irs.gov/pub/irs-pdf/p550.pdf. [Accessed: Sep. 15, 2026].

[13] Internal Revenue Service, "Revenue Procedure 2025-32," 2025. [Online]. Available: https://www.irs.gov/pub/irs-drop/rp-25-32.pdf. [Accessed: Sep. 15, 2026].

## Technical companion

For a cash-secured put, collateral and period yield are calculated as:

\[
C = K \times m \times q, \qquad y_{\mathrm{period}} = \frac{\Pi}{C},
\]

where (K) is strike, (m) is the contract multiplier, (q) is contracts and \(\Pi\) is premium received. The [matrix variance, wheel and tax appendix](<Appendices/Appendix 04 - Matrix Variance Options and Tax Cases.md>) retains the strike sensitivity and wash-sale illustration.
