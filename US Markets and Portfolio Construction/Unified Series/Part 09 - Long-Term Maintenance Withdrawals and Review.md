# Part 09: Long-Term Maintenance, Withdrawals and Review

*US Markets and Portfolio Construction, unified nine-part series. Research edition: 15 September 2026.*

A market portfolio has to work in a household as well as on an allocation chart. This final part joins investment implementation to contribution patterns, reserves, withdrawals, taxes and review rules.

The earlier parts establish market language, wrapper economics, cross-border ownership, portfolio architecture, core overlap, thematic satellites, options mechanics and rebalancing governance. This final chapter connects that analysis to the household cash flows that make a policy workable: regular contributions, lump sums, liquidity reserves, withdrawals, taxes, behavioural discipline and periodic review.

### Dollar-cost averaging versus investing a lump sum immediately

A recurring question for anyone with a lump sum to invest, such as an inheritance, bonus or sale proceeds, is whether to invest it all at once or spread it out gradually over several months, a practice commonly called dollar-cost averaging (DCA). Vanguard's own research on this question, examining rolling historical periods across the US, UK, and Australian markets, found that investing a lump sum immediately outperformed spreading the same amount out over 12 months roughly two-thirds of the time [1]. The mechanical reason is straightforward: markets rise more often than they fall over most historical periods, so money that is not yet invested is, on average, sitting out of gains it would otherwise have captured, and every month DCA delays full investment is a month of that opportunity cost.

### Table 1: Lump sum versus DCA under two illustrative one-year scenarios

| Scenario | Lump sum ($6,000 upfront) ending value | DCA ($500/month multiplied by 12) ending value | Lump sum advantage |
|---|---|---|---|
| Steady rise (illustrative +1%/month) | $6,760.95 | $6,404.66 | +$356.29 |
| Dip in months 1–2, then recovery (illustrative) | $6,618.62 | $6,554.34 | +$64.28 |

Both illustrative scenarios in Table 1 favor the lump sum, consistent with Vanguard's finding, but the gap narrows considerably in the scenario where a decline happens early, since DCA's gradual entry allows some of the later contributions to buy in at the lower, post-decline prices rather than the higher starting price. This is the entire case for DCA in a single sentence: it does not raise expected returns relative to a lump sum, but it reduces the specific regret of investing everything immediately before a decline, and it is the only realistic option in any case for money that arrives gradually, such as a salary, rather than all at once. Vanguard's own conclusion is not that DCA is irrational, but that an investor choosing it is deliberately trading expected return for a smoother emotional path into a full position, a trade psychologically real enough that Vanguard's paper explicitly validates it as a reasonable choice for an investor who would otherwise be tempted to delay investing indefinitely rather than commit a lump sum at all [1].

A middle path worth naming is a compressed DCA schedule: spreading a lump sum over three to six months rather than the full twelve Vanguard's research tested, which captures a meaningful share of the psychological benefit of gradual entry while limiting the expected-return cost, since most of the "opportunity cost of waiting" in the twelve-month case comes from the later months of the schedule rather than the first few. None of this changes the more important practical point for most investors following this series: money arriving from ongoing income, rather than a single windfall, is not choosing between DCA and lump-sum investing. It is invested as received, which is DCA by construction. Table 1 therefore addresses a genuine lump sum already sitting in cash.

### Rebalancing in practice: what the research actually supports

Part 4 established that a core-satellite structure needs rebalancing discipline to avoid satellite creep; this part turns to what the evidence says about how to do it. An earlier Vanguard analysis of calendar-based, threshold-based, and combined rebalancing strategies found that, for most broadly diversified stock-and-bond portfolios, risk-adjusted returns did not differ meaningfully across a wide range of specific rules, and recommended annual or semiannual monitoring with a 5% rebalancing threshold as a reasonable, cost-effective default for most individual investors [2]. A more recent Vanguard paper, published in December 2024 and focused on threshold-based methods, found a more specific edge: a threshold-based approach, monitoring an allocation continuously and rebalancing only once it drifts by a set amount, such as 200 basis points, back to a destination somewhat inside that band, such as 175 basis points, outperformed calendar-based rebalancing by roughly 5 to 21 basis points per year on a risk-adjusted basis, with the benefit somewhat larger during retirement withdrawals than during accumulation [3]. Neither finding overturns the other; they agree that some form of systematic rebalancing outperforms no rebalancing at all, and disagree only modestly on how much additional benefit a more sophisticated threshold rule adds over a simple calendar-based one. It is a genuinely smaller practical question than whether to rebalance at all.

### Table 2: Illustrative one-year drift on the $50,000 core-satellite portfolio (from Part 4)

| Sleeve | Starting weight | Illustrative 1-year return | Ending weight (before rebalancing) | Drift |
|---|---|---|---|---|
| SPYM (equity core) | 55.0% | +15% | 53.5% | -1.53 pp |
| AGG (bond core) | 15.0% | +2% | 12.9% | -2.07 pp |
| QQQM (growth tilt) | 15.0% | +30% | 16.5% | +1.48 pp |
| Satellite blend | 15.0% | +35% | 17.1% | +2.12 pp |

Portfolio value grew from $50,000 to $59,150 under this illustrative set of returns, and the satellite sleeve's weight drifted from its 15.0% target to 17.1%, still inside a 20% combined-satellite ceiling in this particular illustration, but this is precisely the mechanical satellite-creep process Part 4 warned about: a satellite sleeve that simply performs well, with no new conviction added by the investor at all, mechanically grows its share of the portfolio purely through price appreciation. Restoring the original target weights on this $59,150 base requires selling $877.50 from QQQM and $1,252.50 from the satellite blend, while buying $907.50 of SPYM and $1,222.50 of AGG. This disciplined trade involves selling some of what just performed best and buying some of what lagged. That is why rebalancing is behaviorally harder to execute than it is mathematically simple to describe.


Rebalancing by selling appreciated positions can create a capital gain in a taxable account. Directing new contributions toward underweight sleeves can reduce sales and turnover while contributions remain large relative to the portfolio. The method becomes less powerful as the portfolio grows, so it complements rather than replaces a calendar or threshold rule. The workbook shows the exact target trade and the amount that a new contribution can absorb before a sale is required.

### A practical monitoring checklist

Bringing together the sizing and rebalancing rules from across this series into a single cadence, a reasonable monitoring routine for an investor running the core-satellite structure built across Parts 4 through 7 checks, at minimum: current sleeve weights against target weights and the rebalancing threshold chosen (Part 4 and this part); the combined satellite share against its ceiling (Part 4); any single satellite position against its own individual cap (Part 4); the effective N of any satellite fund whose underlying index methodology may have changed since it was last checked (Part 6); and, for any options-wheel positions, upcoming expiration dates and the collateral currently committed against them (Part 7). None of this requires daily attention for a portfolio built from the broad, low-turnover vehicles this series has focused on. The Vanguard research cited above specifically found that more frequent monitoring did not meaningfully improve risk-adjusted outcomes for this kind of portfolio, but it does require checking on a fixed schedule rather than only when a market move prompts an emotional reaction to check.


A workable cadence is a quarterly check of sleeve weights and thresholds, an annual review of each fund's fee, structure, holdings and methodology, and continuous awareness of open option collateral. Record the check dates, decision thresholds and permitted exceptions before a stressful market period. A policy that is only remembered in a drawdown is unlikely to govern behaviour consistently.

### Common implementation failures

Three failures are common. First, an allocation is treated as a one-time purchase rather than a policy that must be reassessed when time horizon, cash needs or capacity for loss changes. Second, an investor applies the rebalancing rule only after losses but hesitates to trim a strong satellite. Third, the investor abandons the policy during a sharp decline. Each failure turns a written allocation into a discretionary response at the point when discipline matters most.

### Sequence-of-returns risk and the debate over safe withdrawal rates

Everything so far in this part concerns building up a portfolio; the mathematics changes once an investor begins withdrawing from it, because a withdrawal taken during a market decline permanently removes shares that can no longer participate in the eventual recovery, a phenomenon called sequence-of-returns risk. The point is easiest to see by holding the average return fixed and varying only the order in which it occurs.

### Table 3: Identical average return, different outcome, purely from timing

Consider two hypothetical retirees, each starting with $1,000,000, each withdrawing a fixed $45,000 per year (a simplified illustration that does not adjust for inflation, in order to isolate the sequencing effect alone), and each experiencing the exact same ten annual returns: eight years, averaging positively, plus two sharp decline years of -20% and -15%, differing only in when the two decline years occur:

| Year | Retiree A (decline years 1–2) | Retiree B (decline years 9–10) |
|---|---|---|
| 0 | $1,000,000 | $1,000,000 |
| 2 | $596,750 | $1,137,500 |
| 5 | $646,952 | $1,249,176 |
| 8 | $653,279 | $1,439,549 |
| 10 | $666,446 | $895,643 |

Both retirees experience an identical average annual return of 3.30% over the ten years and take an identical fixed withdrawal every year. The only difference is whether the two decline years land at the start or the end of the sequence. Retiree A ends with $666,446; Retiree B ends with $895,643, a gap of $229,197 that comes entirely from timing, not from any difference in average performance [4]. This is the central, somewhat unsettling fact behind every "safe withdrawal rate" debate: a withdrawal rate that would have been perfectly sustainable against the average historical return can still fail against the specific sequence a real retiree actually lives through, which is why the research in this area tests every historical starting year individually rather than relying on a single average.

### Where the safe-withdrawal-rate research currently stands

Withdrawal-rate research gives conditional planning ranges, not a universal spending promise. Bengen's 1994 historical analysis reported a 4.15% initial rate for its stated portfolio, withdrawal and thirty-year horizon assumptions, the origin of the familiar rounded 4% rule [5]. Morningstar's 2025 forward-looking study estimated a 3.9% maximum starting rate under a different set of capital-market, horizon and probability-of-success assumptions [6]. The figures answer different questions, so they should be used as sensitivity cases rather than competing universal constants. A real spending plan must state its portfolio, time horizon, tax position, other income, inflation rule and willingness to reduce spending after weak returns.


A flexible withdrawal rule can reduce spending after a poor sequence and allow it to recover after strong returns. A liquidity-bucket approach can hold near-term spending in cash or short-duration instruments, a further spending horizon in the bond core, and long-horizon capital in equities. These methods do not eliminate market risk. They reduce the chance that a near-term cash requirement forces an equity sale after a drawdown.

### A full worked case study

Bringing every part of this series together, consider an investor implementing the core-satellite structure introduced in Part 4 with a $50,000 starting position, contributing an additional $500 per month thereafter. The allocation follows Part 4's growth-oriented variant: 55% SPYM, 5% AGG, 20% QQQM, 5% SCHD (dividend satellite), and 15% split between SOXQ (sector satellite) and a modest options-wheel allocation sized within Part 7's collateral framework, with each satellite position individually capped and the combined satellite-plus-growth-tilt allocation monitored against a 40% ceiling on non-core holdings. Contributions are invested via DCA by necessity, since they arrive monthly from income rather than as a lump sum, consistent with this chapter's finding that DCA is the natural approach for ongoing contributions even where Vanguard's research favors a lump sum for money already sitting in cash. The portfolio is monitored quarterly against a 5% rebalancing threshold, consistent with the simpler of the two Vanguard rebalancing approaches discussed above, and each satellite position's effective N (Part 6) is rechecked at least annually against the fund's current published holdings, since weighting methodologies and index compositions can and do change, as the SOXX stock split and the QQQ UIT-to-open-end reclassification discussed earlier in this series both demonstrate. As this investor approaches a spending phase decades later, the withdrawal-rate research summarized above becomes directly relevant, and the sequence-of-returns illustration in Table 3 becomes the reason a bond and cash allocation typically increases as that transition approaches. This is not because bonds outperform equities over long horizons, but because a portfolio drawing down principal is specifically vulnerable to the timing risk Table 3 demonstrates, in a way a portfolio still purely accumulating is not.


### Table 4: Ten-year accumulation case study after blended fund expenses

The companion workbook models a $50,000 opening balance, $500 contributed at month-end, an illustrative 8.00% gross annual return and the 0.095% blended expense ratio from the growth-oriented allocation. The equivalent monthly net rate is therefore 0.6354%. The model does not forecast returns or include tax, trading costs, rebalancing trades or inflation.

| End of year | Projected balance after fund expenses | Cumulative contributions | Growth after fund expenses |
| ---: | ---: | ---: | ---: |
| 1 | $60,162.90 | $56,000.00 | $4,162.90 |
| 3 | $82,959.89 | $68,000.00 | $14,959.89 |
| 5 | $109,499.81 | $80,000.00 | $29,499.81 |
| 7 | $140,397.18 | $92,000.00 | $48,397.18 |
| 10 | $196,510.08 | $110,000.00 | $86,510.08 |

The expense-aware ending balance is $196,510.08. This makes the fee treatment explicit instead of showing a gross-return projection beside a fee that does not affect the calculation. As spending approaches, the sequence-risk result is one reason to increase the visibility of liquidity reserves and the bond sleeve gradually, rather than making a single abrupt allocation change on a retirement date.

### Closing the series

Across nine parts, this series has moved from the raw vocabulary of US markets: indices, vehicle types, legal structures and layered costs. It then builds a disciplined core-satellite structure, measures the concentration embedded in satellite choices, applies the mathematics and tax rules that shape after-tax outcomes, and ends with the operating discipline needed to run the whole structure over time. Its throughline is a method: trace each material claim to the relevant issuer, regulator or research source, then reassess it when a fund, tax rule or personal objective changes. The companion appendices and workbook make that method usable beyond the final chapter by showing the formulae, inputs and limits of each illustration.

---

## References

[1] Vanguard, "Cost Averaging: Invest Now or Temporarily Hold Your Cash?" [Online]. Available: https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf. Accessed: Sep. 11, 2026.

[2] Vanguard, "Rational Rebalancing: An Analytical Approach to Multiasset Portfolio Rebalancing Strategies." [Online]. Available: https://www.vanguardsouthamerica.com/content/dam/intl/americas/documents/latam/en/2022/10/mx-sa-2558523-rational-rebalancing-an-analytical-approach.pdf. Accessed: Sep. 11, 2026.

[3] Vanguard, "The Rebalancing Edge: Optimizing Target-Date Fund Rebalancing Through Threshold-Based Strategies." [Online]. Available: https://corporate.vanguard.com/content/dam/corp/research/pdf/the_rebalancing_edge_optimizing_target_date_fund_rebalancing_through_threshold_based_strategies.pdf. Accessed: Sep. 11, 2026.

[4] Author's calculation; methodology and full derivation in Appendix 5.

[5] W. P. Bengen, “Determining Withdrawal Rates Using Historical Data,” *Journal of Financial Planning*, Oct. 1994. [Online]. Available: https://www.financialplanningassociation.org/learning/publications/journal/OCT94-determining-withdrawal-rates-using-historical-data. [Accessed: Sep. 15, 2026].

[6] A. C. Arnott, C. Benz and J. Kephart, *The State of Retirement Income: 2025*. Morningstar, 2025. [Online]. Available: https://www.morningstar.com/content/cs-assets/v3/assets/blt9415ea4cc4157833/bltb73b87c5d0c70ead/692f43f57737a31596684522/working_file_11.19_FINAL_REVISE.pdf. [Accessed: Sep. 15, 2026].

*Companion appendix: Appendix 5: Sequencing, Rebalancing, and the Full Case-Study Workbook Mapping.*

## Technical companion

With an annual withdrawal (W_t), the sequence model is:

\[
V_t = V_{t-1}(1+r_t)-W_t.
\]

The order of (r_t) matters once cash leaves the portfolio. The [sequence-risk and case-study appendix](<Appendices/Appendix 05 - Rebalancing Sequence Risk and Case Study.md>) retains the full ten-year paths, rebalancing arithmetic and workbook mapping.
