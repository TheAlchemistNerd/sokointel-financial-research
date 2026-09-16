# Appendix 4 — Matrix Variance, Wheel Economics, and Tax Worked Examples
### Companion to Part 4: Risk Mathematics, Options Income, and Tax Treatment

This appendix works a full four-asset portfolio through the matrix variance formula introduced in Part 4, extends the options-wheel worked example across a range of strike selections, and adds further worked tax scenarios.

## A4.1 A four-asset matrix variance calculation, worked in full

Consider the illustrative core-satellite portfolio built across this series — 55% SPYM, 15% AGG, 15% QQQM, and 15% in a satellite blend — with illustrative annualized volatilities of 16%, 6%, 22%, and 28% respectively, and an illustrative correlation matrix reflecting that QQQM and the satellite blend move closely with SPYM (0.85 and 0.75) and with each other (0.65), while AGG remains only weakly correlated with all three equity-like sleeves (0.10, 0.05, 0.05):

**Covariance matrix Σ** (each entry = σᵢ × σⱼ × ρᵢⱼ):

| | SPYM | AGG | QQQM | Satellite |
|---|---|---|---|---|
| SPYM | 0.0256 | 0.0010 | 0.0299 | 0.0336 |
| AGG | 0.0010 | 0.0036 | 0.0007 | 0.0008 |
| QQQM | 0.0299 | 0.0007 | 0.0484 | 0.0400 |
| Satellite | 0.0336 | 0.0008 | 0.0400 | 0.0784 |

Applying Equation 4.1 (σₚ² = wᵀΣw) with w = [0.55, 0.15, 0.15, 0.15]:

σₚ² = 0.02319, so σₚ = √0.02319 = 15.23%

A manual double-sum over all 16 pairwise terms (4 assets × 4 assets, including each asset paired with itself) produces the identical figure, confirming that Equation 4.1's matrix notation is simply a compact way of writing the same sum used in Appendix 2's three-asset example, extended here to four assets. For comparison, a naive linear weighted average of the four individual volatilities would suggest 17.20%, so the diversification benefit in this particular illustrative mix is 1.97 percentage points — smaller than the two-asset stock/bond case in Appendix 2 precisely because three of the four sleeves (SPYM, QQQM, and the satellite blend) are assumed here to be fairly highly correlated with one another, leaving AGG as the only sleeve doing substantial diversifying work in this particular illustrative correlation structure.

## A4.2 Options wheel: sensitivity of yield to strike selection

Part 4's worked example used a single $90 strike on a $100 stock. The table below extends that example across a range of strikes at illustrative premiums, holding the stock price fixed at $100, to show how strike selection trades off assignment probability (lower strikes, further out-of-the-money, are less likely to be assigned) against yield (lower strikes also command smaller premiums):

| Strike | % out-of-the-money | Premium | Collateral | Period yield on collateral | Naive annualized (×12) |
|---|---|---|---|---|---|
| $95 | 5% | $3.50 | $9,500 | 3.68% | 44.2% |
| $90 | 10% | $2.00 | $9,000 | 2.22% | 26.7% |
| $85 | 15% | $1.10 | $8,500 | 1.29% | 15.5% |
| $80 | 20% | $0.60 | $8,000 | 0.75% | 9.0% |

The naive annualized figures in the rightmost column are included only to show the shape of the trade-off, not as achievable return targets: they assume an identical trade repeats every month indefinitely with the same premium available and no assignment or adverse price movement interrupting the cycle, none of which holds in practice, and the higher naive annualized yields at closer-to-the-money strikes correspond directly to a higher probability of assignment during a decline, which is precisely the scenario in which the strategy's downside (illustrated in Part 4's crash-scenario worked example) is realized.

## A4.3 Additional wash-sale scenario: partial repurchase

Part 4's wash-sale example assumed the investor repurchased the same number of shares sold. A partial repurchase disallows only the corresponding proportion of the original loss. Consider the same $1,000 loss on 100 shares, but a repurchase of only 40 shares within the 30-day window:

Disallowed portion = Total loss × (shares repurchased / shares sold) = $1,000 × (40/100) = $400

The remaining $600 of the loss (corresponding to the 60 shares not repurchased within the window) is allowed as a current-year capital loss, while the $400 disallowed portion is added to the basis of the 40 repurchased shares, exactly as in the full-repurchase case in Part 4, just scaled to the smaller share count.

## A4.4 Reproducibility note

The four-asset matrix calculation in A4.1 can be reproduced in any spreadsheet using matrix-multiplication functions (such as MMULT in Excel or Google Sheets) applied to the weight vector and covariance matrix shown above, or by the manual double-sum method demonstrated in Appendix 2 extended to four terms per row instead of two or three. The wheel-strategy and wash-sale calculations in A4.2 and A4.3 require only the arithmetic shown directly in each worked example. The companion workbook accompanying this series includes a live four-asset (expandable) matrix-variance calculator alongside a wheel-strategy strike-selection sensitivity table matching A4.2, with all volatility, correlation, and strike assumptions exposed as editable inputs.

---

*This appendix uses the same reference numbering as Part 4; no additional sources beyond those cited in the main article were required for the derivations above.*
