# Appendix 2 — Diversification and Blended-Cost Mathematics
### Companion to Part 2: Core Portfolio Construction

This appendix derives the portfolio-variance and blended-expense-ratio formulas used in Part 2, extends each worked example across a wider range of assumptions, and shows the arithmetic behind the sizing-discipline guidance given in the main article. As in Appendix 1, every volatility and correlation figure used below is a clearly labelled illustrative assumption, not a forecast or a historical guarantee.

## A2.1 Two-asset portfolio variance, derived

For a portfolio of two assets with weights w₁ and w₂ (w₁ + w₂ = 1), individual standard deviations σ₁ and σ₂, and correlation ρ between their returns, portfolio variance is:

**σₚ² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂**  (Equation 2.1, expanded)

Portfolio standard deviation is simply the square root of this quantity. The formula follows directly from the definition of the variance of a weighted sum of two random variables: Var(w₁X₁ + w₂X₂) = w₁²Var(X₁) + w₂²Var(X₂) + 2w₁w₂Cov(X₁,X₂), and Cov(X₁,X₂) = ρσ₁σ₂ by the definition of correlation. When ρ = 1 (the two assets move in perfect lockstep), the cross term reaches its maximum and σₚ collapses to the simple weighted average w₁σ₁ + w₂σ₂ — there is no diversification benefit at all, which is the boundary case worth checking any implementation of this formula against.

**Worked check (70/30, ρ = 0.10):**
σₚ² = (0.70)²(0.16)² + (0.30)²(0.06)² + 2(0.70)(0.30)(0.10)(0.16)(0.06)
σₚ² = 0.012544 + 0.000324 + 0.0004032 = 0.0132712
σₚ = √0.0132712 = 0.1152, i.e., 11.52%, matching Table 1 in the main article.

## A2.2 Sensitivity to the correlation assumption

Because the cross term in Equation 2.1 is the only place correlation enters, and because it is added (not subtracted) when correlation is positive, a lower or negative correlation assumption always produces a lower portfolio standard deviation for fixed weights and fixed individual volatilities. The table below holds the 70/30 stock/bond weighting and the 16%/6% volatility assumptions fixed while varying only the correlation assumption, to show how much of the diversification benefit is actually being driven by an assumption the investor does not directly observe or control:

| Correlation assumption (ρ) | Portfolio SD | Naive linear blend | Diversification benefit |
|---|---|---|---|
| −0.30 | 10.80% | 13.00% | 2.20 pp |
| −0.10 | 11.16% | 13.00% | 1.84 pp |
| 0.00 | 11.34% | 13.00% | 1.66 pp |
| +0.10 | 11.52% | 13.00% | 1.48 pp |
| +0.30 | 11.86% | 13.00% | 1.14 pp |
| +0.50 | 12.20% | 13.00% | 0.80 pp |
| +1.00 | 13.00% | 13.00% | 0.00 pp |

The diversification benefit shrinks steadily as the correlation assumption rises and vanishes entirely at ρ = 1. This is the mathematical reason a period of unusually high positive stock-bond correlation — such as 2022, referenced in the main article — reduces the ballast effect a bond core is normally expected to provide: the formula has not changed, but the realized correlation input to it moved toward the range where diversification benefit is smaller.

## A2.3 Extending to three assets: adding a satellite sleeve to the variance calculation

The two-asset formula generalizes to any number of assets by summing over every pairwise combination, including each asset paired with itself (which reproduces the wᵢ²σᵢ² terms):

**σₚ² = Σᵢ Σⱼ wᵢwⱼρᵢⱼσᵢσⱼ**  (Equation 2.3, where ρᵢᵢ = 1)

Applying this to an illustrative three-asset mix — an equity core, a bond core, and a sector satellite — with illustrative volatilities of 16% (equity), 6% (bonds), and 28% (a concentrated sector satellite, reflecting its lower diversification), and illustrative correlations of 0.10 (equity–bond), 0.75 (equity–satellite, reflecting that a US sector fund still moves substantially with the broad market), and 0.05 (bond–satellite), a 55/15/30 weighting produces:

σₚ² = (0.55²)(0.16²) + (0.15²)(0.06²) + (0.30²)(0.28²) + 2(0.55)(0.15)(0.10)(0.16)(0.06) + 2(0.55)(0.30)(0.75)(0.16)(0.28) + 2(0.15)(0.30)(0.05)(0.06)(0.28)

σₚ = 16.19%, versus a naive linear blend of 18.10% — a 1.91-percentage-point diversification benefit, smaller in relative terms than the pure two-asset case because the high illustrative equity–satellite correlation (0.75) means the satellite sleeve is not adding much genuine diversification even though it is concentrated in a single sector; most of its risk-reduction contribution to the blend comes from its relatively small 30% weight rather than from behaving differently than the equity core. This is the appendix-level version of a point made qualitatively in Part 3: a satellite sleeve chosen for thematic conviction does not automatically function as a diversifier, and a satellite that is highly correlated with the core it sits alongside should be understood as adding concentrated exposure to a single theme, not as reducing the portfolio's overall risk.

## A2.4 Blended expense ratio: reverse-solving for a cost cap

Section 2's blended-expense-ratio formula (Equation 2.2) can be inverted to answer a practical sizing question directly: given a target blended-expense-ratio ceiling, how large can a single higher-cost satellite sleeve be before it breaches that ceiling, holding the rest of the portfolio at its own blended rate? For a two-part split between "the rest of the portfolio" (illustrative blended rate 0.03%) and a single satellite sleeve priced at 0.33% (matching the sector-satellite example used in Part 2's Table 2):

**w(satellite, max) = (Cap − ER(rest)) / (ER(satellite) − ER(rest))**  (Equation 2.4)

| Blended ER cap | Maximum satellite weight (rest of portfolio at ~0.03%) |
|---|---|
| 0.05% | 6.7% |
| 0.08% | 16.7% |
| 0.10% | 23.3% |
| 0.15% | 40.0% |

This table is a cost constraint only — it says nothing about the separate, and generally more binding, concentration-risk constraint discussed in Part 2's sizing-discipline section and developed further in Part 3. In practice the concentration constraint (commonly a 15–20% combined satellite cap, well below the 40% a pure cost ceiling of 0.15% would technically allow) is almost always the binding one; the cost-based ceiling in this table matters mainly as a sanity check that a chosen satellite weight is not accidentally imposing an outsized cost burden on the whole portfolio, not as the primary sizing rule.

## A2.5 Reproducibility note

Every figure in this appendix follows from Equations 2.1, 2.3, and 2.4 applied to the stated weights, volatilities, and correlation assumptions, computed programmatically and cross-checked by direct substitution into the two- and three-asset variance formulas shown above. A reader can verify any entry in Tables 1 and 2 of the main article, or any row of the sensitivity tables above, with a calculator and the stated inputs; no software beyond basic arithmetic is required, though the companion workbook accompanying this series reproduces all of these calculations on a live spreadsheet with the weights, volatilities, and correlation assumptions all exposed as editable inputs, so that a reader can substitute their own assumptions and see every dependent figure recalculate automatically.

---

*This appendix uses the same reference numbering as Part 2; no additional sources beyond those cited in the main article were required for the derivations above.*
