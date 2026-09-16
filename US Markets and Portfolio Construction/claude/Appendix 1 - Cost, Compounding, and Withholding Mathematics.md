# Appendix 1 — Cost, Compounding, and Withholding Mathematics
### Companion to Part 1: The Market Landscape and the Building Blocks of a Portfolio

This appendix derives every formula used in Part 1, extends each worked example to additional scenarios, and documents the assumptions behind every number so a reader can reproduce or challenge them independently. All growth-rate and yield assumptions used below are clearly labelled educational assumptions, not forecasts, exactly as they were in the main article. Figures are illustrative in scale and are not personalized tax or investment advice.

## A1.1 Notation

- P — initial principal (a lump sum, in US dollars)
- r — assumed gross annual return, before fund-level costs
- e — a fund's annual expense ratio, expressed as a decimal
- n — number of years the position is held
- FV — ending value after n years
- PMT — a level monthly contribution
- i — the equivalent monthly net-of-cost growth rate implied by an annual net rate

## A1.2 Deriving the expense-ratio compounding formula

A fund's expense ratio is deducted from its net asset value continuously, in small daily increments, not as a single annual charge. For a holding period measured in whole years, however, the standard and widely used simplification is to treat the expense ratio as a constant annual drag on the gross return, giving:

**FV = P × (1 + r − e)ⁿ**  (Equation 1.1)

This is an approximation because it assumes the drag compounds once per year rather than daily; the true daily-compounding result is FV = P × (1 + r/365 − e/365)^(365n), which for the expense-ratio magnitudes used in this series (0.02%–0.75%) differs from the annual approximation by less than one dollar on a $10,000 position over 30 years. The annual form is used throughout this series for legibility, consistent with how issuers themselves typically illustrate "cost of ownership" in investor education material.

**Worked check (SPYM, 30 years, 8% gross return):**
FV = 10,000 × (1 + 0.08 − 0.0002)³⁰ = 10,000 × (1.0798)³⁰ = $100,069.03, matching Table 1 in the main article.

## A1.3 Sensitivity of the cost gap to the return assumption

Table 1 in the main article used an 8% illustrative gross return. Because the expense-ratio drag is a fixed percentage while the compounding base grows or shrinks with the return assumption, the dollar-value gap between a cheap and an expensive fund is itself sensitive to which return assumption is used, even though the percentage-point fee gap never changes. The table below repeats the 30-year comparison from Table 1 at five different gross-return assumptions:

| Gross return assumption | SPYM (0.02%) | VOO/IVV (0.03%) | SPY (0.0945%) | QQQM (0.15%) | QQQ (0.18%) | Illustrative active (0.75%) |
|---|---|---|---|---|---|---|
| 3% | $24,132 | $24,061 (−$70) | $23,613 (−$518) | $23,234 (−$897) | $23,032 (−$1,100) | $19,494 (−$4,638) |
| 6% | $57,111 | $56,949 (−$161) | $55,918 (−$1,192) | $55,046 (−$2,065) | $54,580 (−$2,531) | $46,416 (−$10,695) |
| 8% | $100,069 | $99,791 (−$278) | $98,018 (−$2,051) | $96,517 (−$3,552) | $95,715 (−$4,354) | $81,643 (−$18,426) |
| 10% | $173,545 | $173,072 (−$473) | $170,052 (−$3,492) | $167,495 (−$6,050) | $166,128 (−$7,417) | $142,116 (−$31,429) |
| 12% | $297,998 | $297,201 (−$797) | $292,108 (−$5,891) | $287,793 (−$10,206) | $285,486 (−$12,512) | $244,907 (−$53,092) |

The dollar cost of a given fee gap rises with the assumed return, because a higher return means more compounding periods over which the fee differential itself compounds. This is a mathematical property of Equation 1.1, not a claim that higher-returning assets have higher fees — it simply shows that "the fee barely matters" and "the fee matters enormously" are both true statements depending on which return environment is assumed, which is why cost comparisons should always be read alongside their stated assumption rather than as a single fixed dollar figure.

## A1.4 Monthly-contribution version

Most investors build a position through periodic contributions rather than a single lump sum. Equation 1.1 extends to a level monthly contribution PMT using the standard future-value-of-an-annuity formula, with the annual net rate (r − e) converted to an equivalent monthly rate i = (1 + r − e)^(1/12) − 1:

**FV = PMT × [((1 + i)ᵐ − 1) / i]**  (Equation 1.3)

where m is the number of monthly contributions. For a $500 monthly contribution over 20 years (m = 240) at the same 8% illustrative gross return:

| Vehicle | Expense ratio | FV after 20 years ($500/month) | Gap vs. SPYM |
|---|---|---|---|
| SPYM | 0.02% | $283,846 | — |
| VOO / IVV | 0.03% | $283,519 | $326 |
| SPY | 0.0945% | $281,424 | $2,421 |
| QQQM | 0.15% | $279,636 | $4,210 |
| QQQ | 0.18% | $278,674 | $5,172 |
| Illustrative active fund | 0.75% | $261,087 | $22,759 |

The ranking is identical to the lump-sum case because the fee gap operates on the same principle regardless of how the principal accumulates, but the absolute dollar amounts at stake are considerably larger once 240 contributions are compounding rather than one, which is the more realistic picture for most working investors building a position over a career.

## A1.5 NRA dividend withholding: derivation and extended table

The withholding mechanism is a single-step calculation:

**Net dividend = Gross dividend × (1 − w)**  (Equation 1.2)

where w is the applicable withholding rate — 30% by statutory default, or a lower treaty rate where both a treaty exists and a valid Form W-8BEN has been filed with the broker [see Part 1, references 12–14]. The table below extends the single illustration in the main article's Table 2 across a range of position sizes and illustrative yields, comparing the no-treaty statutory rate against an illustrative 15% treaty rate:

| Position | Illustrative yield | Gross annual dividend | Net at 30% (no treaty) | Net at 15% (illustrative treaty) | Annual gap |
|---|---|---|---|---|---|
| $5,000 | 1.0% | $50.00 | $35.00 | $42.50 | $7.50 |
| $5,000 | 1.8% | $90.00 | $63.00 | $76.50 | $13.50 |
| $10,000 | 1.3% | $130.00 | $91.00 | $110.50 | $19.50 |
| $25,000 | 1.3% | $325.00 | $227.50 | $276.25 | $48.75 |
| $50,000 | 1.8% | $900.00 | $630.00 | $765.00 | $135.00 |
| $100,000 | 1.3% | $1,300.00 | $910.00 | $1,105.00 | $195.00 |
| $100,000 | 1.8% | $1,800.00 | $1,260.00 | $1,530.00 | $270.00 |

Because the gap scales linearly with both position size and yield, an investor can approximate their own annual gap as (position × yield × 0.15) without needing the full table — the 15-percentage-point rate difference (30% − 15%) applied directly to the gross dividend.

## A1.6 NRA estate tax: the unified rate schedule behind the $60,000 figure

The $60,000 figure quoted in the main article is not a direct subtraction from the taxable estate. Mechanically, a nonresident alien's estate is taxed using the same graduated unified rate schedule (Internal Revenue Code §2001(c), commonly called Table A) that applies to US citizens and residents, but the nonresident alien's estate receives a unified credit of only $13,000 against the tentative tax, compared with a credit worth several million dollars for a US citizen or resident [16], [17]. The $60,000 figure is the break-even point: it is the taxable-estate value at which the tentative tax computed under Table A exactly equals the $13,000 credit, producing zero net tax. Table A's first four brackets are:

| Taxable amount over | Not over | Tax on lower bound | Rate on excess |
|---|---|---|---|
| $0 | $10,000 | $0 | 18% |
| $10,000 | $20,000 | $1,800 | 20% |
| $20,000 | $40,000 | $3,800 | 22% |
| $40,000 | $60,000 | $8,200 | 24% |

Applying the schedule: tax on $60,000 = $8,200 + 0.24 × ($60,000 − $40,000) = $8,200 + $4,800 = $13,000 — exactly the unified credit available to a nonresident alien's estate. This is why $60,000 functions as an effective exemption even though the statute frames it as a credit rather than an exemption.

**Extended worked table, net US estate tax after the $13,000 credit:**

| US-situs gross estate | Tentative tax (Table A) | Less unified credit | Net estate tax | Effective rate on excess over $60,000 |
|---|---|---|---|---|
| $60,000 | $13,000 | $13,000 | $0 | 0.0% |
| $100,000 | $23,800 | $13,000 | $10,800 | 27.0% |
| $150,000 | $38,800 | $13,000 | $25,800 | 28.7% |
| $250,000 | $70,800 | $13,000 | $57,800 | 30.4% |
| $500,000 | $155,800 | $13,000 | $142,800 | 32.5% |
| $1,000,000 | $345,800 | $13,000 | $332,800 | 35.4% |
| $2,000,000 | $745,800 | $13,000 | $732,800 | 37.8% |

The effective rate on the excess above $60,000 rises toward, but never reaches, the 40% marginal top rate, because the lower brackets of Table A are always taxed at their lower marginal rates first regardless of total estate size — a standard feature of any graduated schedule, and worth noting because commentary on this topic sometimes implies a flat 40% applies to the entire excess, which the arithmetic above shows is not the case at these estate sizes.

## A1.7 Reproducibility note

Every figure in Part 1 and this appendix was produced from Equations 1.1–1.3 and the Table A schedule above, computed programmatically rather than by hand, and cross-checked against the cited primary sources for each input (expense ratios, inception dates, treaty counts, and statutory thresholds). A reader wishing to verify any cell can do so with four inputs — principal or contribution amount, gross return assumption, expense ratio, and holding period — fed into Equation 1.1 or 1.3, or, for the tax tables, by applying Table A directly to a chosen taxable-estate figure and subtracting the $13,000 credit. The companion workbook accompanying this series reproduces every table in this appendix on a live, editable spreadsheet, with all inputs clearly separated from formulas so that changing an assumption automatically recalculates every dependent figure.

---

## References

[16] Internal Revenue Service, "SOI Tax Stats — International: Nonresident Alien Estate Tax Filing Requirements." [Online]. Available: https://www.irs.gov/node/10081. Accessed: Sep. 11, 2026.

[17] Raveum, "US Estate Tax for Global Investors: What Happens to Your US Real Estate Investment When You Die." [Online]. Available: https://www.raveum.com/resources/guides/us-estate-tax-for-global-investors. Accessed: Sep. 11, 2026.

*Reference numbering in this appendix continues independently of Part 1's reference list; references [1]–[15] cited by number in the body of this appendix refer back to the corresponding numbered sources in Part 1.*
