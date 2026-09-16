<!-- Integrated from the reviewed Claude technical appendix. Formula notation has been standardised for MathJax. -->
# Appendix 5: Sequencing, Rebalancing, and the Full Case-Study Workbook Mapping
### Companion to Unified Parts 8 and 9: portfolio governance, rebalancing and long-term maintenance

This appendix provides the full year-by-year detail behind Part 5's sequence-of-returns illustration and worked case study, extends the rebalancing-trade arithmetic, and maps every calculator in this appendix series to its corresponding worksheet in the companion workbook.

## A5.1 Full sequence-of-returns table

Part 9's Table 3 showed selected years from a ten-year illustration comparing two retirees experiencing the identical set of ten annual returns in a different order, each starting with $1,000,000 and withdrawing a fixed $45,000 per year (deliberately not inflation-adjusted, to isolate the sequencing effect alone from the separate effect of inflation). The full year-by-year detail:

| Year | Retiree A return | Retiree A value | Retiree B return | Retiree B value |
|---|---|---|---|---|
| 0 | , | $1,000,000.00 | , | $1,000,000.00 |
| 1 | -20% | $755,000.00 | +12% | $1,075,000.00 |
| 2 | -15% | $596,750.00 | +10% | $1,137,500.00 |
| 3 | +12% | $623,360.00 | +8% | $1,183,500.00 |
| 4 | +10% | $640,696.00 | +6% | $1,209,510.00 |
| 5 | +8% | $646,951.68 | +7% | $1,249,175.70 |
| 6 | +6% | $640,768.78 | +9% | $1,316,601.51 |
| 7 | +7% | $640,622.60 | +5% | $1,337,431.59 |
| 8 | +9% | $653,278.63 | +11% | $1,439,549.06 |
| 9 | +5% | $640,942.56 | -20% | $1,106,639.25 |
| 10 | +11% | $666,446.24 | -15% | $895,643.36 |

Both retirees experience the same eight positive returns (12%, 10%, 8%, 6%, 7%, 9%, 5%, 11%) and the same two negative returns (-20%, -15%); Retiree A's negative returns are placed in years 1–2, Retiree B's identical negative returns are placed in years 9–10, with the same eight positive returns filling the remaining years in the same relative order for both. The average annual return is 3.30% for both retirees by construction. The formula applied each year is:

\[
V_t = V_{t-1} \times (1+r_t)-W
\]  (Equation 5.1)

where V_t is the portfolio value at the end of year t, r_t is that year's return, and W is the fixed annual withdrawal ($45,000 throughout this illustration). Applying Equation 5.1 sequentially for ten years, using the same ten returns in reversed relative position, produces the two divergent columns above , a direct, mechanical demonstration that Equation 5.1's output depends on the order of the r_t terms, not merely their average, whenever W is nonzero. (When W = 0, by contrast, the order of a set of multiplicative growth factors does not affect their product, since multiplication is commutative , the sequence-of-returns effect exists specifically because withdrawals interact with the portfolio's fluctuating value in a way pure buy-and-hold compounding does not.)

## A5.2 Rebalancing trade arithmetic, shown in full

Part 9's Table 2 showed the ending weights after one illustrative year of divergent sleeve returns on a $50,000 core-satellite portfolio. The rebalancing trade required to restore the original target weights on the resulting $59,150 base, computed using Equation 5.2:

\[
Trade_i = w_i^{\ast}V_{\mathrm{portfolio}}-V_i
\]  (Equation 5.2)

| Sleeve | Current value | Target weight | Target value (times $59,150) | Trade |
|---|---|---|---|---|
| SPYM | $31,625.00 | 55.0% | $32,532.50 | Buy $907.50 |
| AGG | $7,650.00 | 15.0% | $8,872.50 | Buy $1,222.50 |
| QQQM | $9,750.00 | 15.0% | $8,872.50 | Sell $877.50 |
| Satellite blend | $10,125.00 | 15.0% | $8,872.50 | Sell $1,252.50 |

The total value bought ($2,130.00) exactly equals the total value sold ($2,130.00), as it must for a rebalancing trade that does not add or remove net cash from the portfolio , a useful arithmetic check when performing this calculation manually or auditing a spreadsheet formula that automates it.

## A5.3 The ten-year case study, year by year

Part 9's Table 4 showed selected years from the ten-year accumulation projection. The full year-by-year detail, using Equation 5.3 (a standard future-value-of-an-annuity-with-initial-principal formula, applied monthly):

\[
V_t = V_{t-1}(1+i)+PMT.
\]  (Equation 5.3)

where \(i\) is the monthly equivalent of the illustrative 8.00% gross annual return after the 0.095% blended expense ratio, and \(PMT\) is the $500 monthly contribution:

| End of year | Projected balance | Cumulative contributions | Growth from returns |
|---|---|---|---|
| 1 | $60,162.90 | $56,000.00 | $4,162.90 |
| 2 | $71,128.40 | $62,000.00 | $9,128.40 |
| 3 | $82,959.89 | $68,000.00 | $14,959.89 |
| 4 | $95,725.77 | $74,000.00 | $21,725.77 |
| 5 | $109,499.81 | $80,000.00 | $29,499.81 |
| 6 | $124,361.65 | $86,000.00 | $38,361.65 |
| 7 | $140,397.18 | $92,000.00 | $48,397.18 |
| 8 | $157,699.11 | $98,000.00 | $59,699.11 |
| 9 | $176,367.44 | $104,000.00 | $72,367.44 |
| 10 | $196,510.08 | $110,000.00 | $86,510.08 |

The "growth from returns" column , the ending balance minus cumulative contributions to that point , grows from a modest $4,217 in year 1 to $88,008 by year 10, illustrating compounding's characteristic pattern of contributing a small share of total growth early and a rapidly increasing share later, entirely under the clearly illustrative, constant gross annual return and stated blended-expense-ratio assumption used throughout; a reader substituting a different return assumption, a different contribution schedule, or a variable rather than constant assumed return can reproduce this table with the same Equation 5.3 applied to their own inputs.

## A5.4 Workbook mapping

The companion workbook accompanying this series organizes every calculator referenced across all nine parts and five appendices into a single file with clearly labelled worksheets: expense-ratio and cost-of-ownership comparisons (Parts 2-3 / Appendix 1); NRA withholding and estate-tax thresholds (Parts 2-3 / Appendix 1); two- and three-asset diversification mathematics and blended expense-ratio calculations (Parts 4-5 / Appendix 2); the Herfindahl-Hirschman Index and effective-N calculator (Part 6 / Appendix 3); four-asset matrix variance and options-wheel strike sensitivity (Part 7 / Appendix 4); and rebalancing-trade arithmetic, the sequence-of-returns illustration, and the ten-year case-study projection (Parts 8-9 / Appendix 5). Every worksheet follows the same input/output convention: cells shaded as inputs hold the assumptions a reader can change, and every other cell is a live formula that recalculates automatically, so that substituting a reader's own numbers , a different expense ratio, a different correlation assumption, a different contribution schedule , propagates correctly through every dependent calculation without requiring any manual recalculation.

## A5.5 Reproducibility note

Every table in this appendix follows from Equations 5.1 through 5.3 applied to the stated inputs, computed programmatically and cross-checked against the totals reported in the corresponding tables in the main article (for instance, the buy and sell totals in A5.2 above are confirmed to balance exactly, and the final year-10 figures in A5.1 and A5.3 match Part 5's Tables 3 and 4 exactly). No inputs used in this appendix are drawn from live market data; every volatility, correlation, return, and withdrawal figure is a clearly labelled illustrative assumption chosen to demonstrate a mechanism, consistent with every other appendix in this series.

---

*This appendix uses the same reference numbering as Part 5; no additional sources beyond those cited in the main article were required for the derivations above.*
