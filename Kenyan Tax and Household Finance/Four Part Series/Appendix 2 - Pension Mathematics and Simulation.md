# Appendix 2; Pension accumulation, inflation and Monte Carlo

## Model boundary and time axis

The accumulation model covers thirty year-end observations, 2027–2056, starting with private pension assets at the beginning of 2027. Contributions enter at each year end after the investment return and asset-based fee. NSSF benefits are excluded. The balance is before any benefit-specific withdrawal tax, and the model does not project post-retirement withdrawals, annuity pricing or longevity. Employee and assumed employer contributions begin at KES 120,000 and KES 60,000 and each grow 5% annually in the base case. Every year has its own editable assumptions. The general controls scale contributions or adjust fees and expected returns, while the dated grid permits a specific later year to differ without changing earlier periods.

## Formula and variable dictionary

| Symbol | Meaning | Units / definition |
|---|---|---|
| W₀ | Opening private pension | KES 500,000 |
| Wₜ | Closing nominal wealth in year t | KES |
| Cₜ | Employee plus employer contribution at year end | KES; multiplier applies to both |
| μₜ | Arithmetic expected gross annual return | Fraction; 0.10 base |
| fₜ | Fee after gross return, before contribution | Fraction; 0.01 base |
| σₜ | Standard deviation of annual log return | 0.12 base, not 12% simple-return volatility |
| πₜ | Annual inflation | Fraction; 0.05 base |
| Pₜ | Cumulative price index | Dimensionless; P₀ = 1 |
| Zᵢₜ | Independent standard normal draw, trial i, year t | Dimensionless |
| g | Contribution growth rate in closed-form check | 0.05; not required constant in workbook |
| K | Real capital target | KES 12,000,000 in starting purchasing power |
| N | Number of simulated paths | 1,000 |

## Equation (2.1): annual accumulation

> Wₜ = Wₜ₋₁ × (1 + μₜ) × (1 − fₜ) + Cₜ  
> Investment gain = Wₜ₋₁ × μₜ  
> Fee = Wₜ₋₁ × (1 + μₜ) × fₜ

First-year manual expansion:

> Investment gain = 500,000 × 0.10 = 50,000  
> Fee = (500,000 + 50,000) × 0.01 = 5,500  
> Contribution = 120,000 + 60,000 = 180,000  
> W₁ = 500,000 + 50,000 − 5,500 + 180,000 = **724,500**

Second-year check:

> C₂ = 180,000 × 1.05 = 189,000  
> Gain₂ = 724,500 × 0.10 = 72,450  
> Fee₂ = 796,950 × 0.01 = 7,969.50  
> W₂ = 724,500 + 72,450 − 7,969.50 + 189,000 = **977,980.50**

The exact net investment rate under this fee convention is:

> a = (1 + 0.10)(1 − 0.01) = 1.089  
> Net rate = a − 1 = **8.9%**

For constant a and contribution growth g, a separate closed-form calculation checks the thirty-year recursion:

> Wₙ = W₀aⁿ + C₁ × [aⁿ − (1+g)ⁿ] ÷ [a − (1+g)]  
> W₃₀ = 500,000 × 1.089³⁰ + 180,000 × [1.089³⁰ − 1.05³⁰] ÷ 0.039  
> W₃₀ ≈ **46,078,527.76**

If a = 1+g, the fraction is replaced by n × aⁿ⁻¹. This avoids division by zero and follows the limit of the geometric sum. The workbook uses annual recursion, so it handles non-constant dated assumptions without relying on this special closed form.

## Equation (2.2): inflation and purchasing power

> Pₜ = Pₜ₋₁ × (1 + πₜ), with P₀ = 1  
> Real wealthₜ = Wₜ ÷ Pₜ  
> P₃₀ = 1.05³⁰ = 4.321942375  
> Real W₃₀ = 46,078,527.76 ÷ 4.321942375 ≈ **10,661,532.19**

The annual real net investment rate under constant assumptions is:

> (1.089 ÷ 1.05) − 1 = **3.7142857%**

It is not exactly 8.9% − 5%. Nominal contributions must also be converted consistently when a real model is used. The workbook first constructs nominal cash and assets, then divides by the cumulative price index, avoiding a mixture of real contributions and nominal returns.

## Equation (2.3): a spending gap is not a withdrawal guarantee

> Annual spending gap = desired spending − dependable other income  
> = 900,000 − 300,000 = **600,000**  
> Capital-to-first-year-gap ratio = 12,000,000 ÷ 600,000 = **20**

For illustration only, if there were no real investment return, no taxes or charges and exactly level real withdrawals for twenty years, KES 12 million would fund KES 600,000 at each year end and end at zero. That is an arithmetic identity, not a safe withdrawal rule. With a known constant real discount rate q and n end-year withdrawals A, their present value would be A[1−(1+q)⁻ⁿ]/q, or A×n if q=0. Real retirement includes uncertain survival, spending and returns, so annuity or drawdown modelling requires additional inputs and a separate post-retirement schedule. None of the accumulation success probabilities represents a probability of lifetime income adequacy.

## Stochastic returns and mathematical equivalence

The gross investment factor in each simulated year is:

> Fᵢₜ = exp{ln(1+μₜ) − σₜ²/2 + σₜZᵢₜ}  
> Wᵢₜ = Wᵢ,ₜ₋₁ × Fᵢₜ × (1−fₜ) + Cₜ

Since E[exp(σZ)] = exp(σ²/2), E[Fᵢₜ] = 1+μₜ. The subtraction of σ²/2 ensures that the entered 10% is the arithmetic expected return. Omitting it would raise the expected gross factor. Independence of the return draw from prior wealth and the deterministic contributions gives the deterministic recursion the interpretation of expected wealth under this model.

For a zero normal draw in the base year:

> ln(1.10) − 0.12²/2 = 0.09531018 − 0.0072 = 0.08811018  
> F = exp(0.08811018) ≈ 1.09210844  
> W₁ ≈ 500,000 × 1.09210844 × 0.99 + 180,000 ≈ **720,593.68**

This path is below deterministic first-year wealth because a zero log-return draw represents the median gross factor, not its mean. The simulated simple-return standard deviation is (1+μ)√[exp(σ²)−1], which differs from the input log-return standard deviation.

## Reproducible draws

The fixed seed is 20260907. Unsigned 32-bit states follow:

> stateₖ₊₁ = (1,664,525 × stateₖ + 1,013,904,223) modulo 2³²  
> Uₖ = (stateₖ + 0.5) ÷ 2³²  
> Z = √(−2 ln U₁) × cos(2πU₂)

For each trial, thirty normal draws are generated in chronological order, using two successive uniforms per normal and discarding the sine counterpart. The resulting 1,000 × 30 normal matrix is stored on `Random draws`. Excel transforms these fixed draws using live assumptions, so comparison scenarios use common random numbers. This simple generator supports reproducibility of the illustration; it is not presented as a production-grade stochastic risk engine. Its finite period, distribution assumptions and model omissions remain part of the methodological limitations. A specialist implementation could replace the generator and expand the economic process while retaining the same cash-flow definitions and independent checks.

## Results, uncertainty and sensitivity

| Real terminal result | Fixed-run value |
|---|---:|
| Median | KES 9,465,248.19 |
| 10th percentile | KES 5,498,009.97 |
| 90th percentile | KES 17,233,260.20 |
| Paths reaching KES 12 million | 310 / 1,000 |
| First 500 success proportion | 33.6% |
| Second 500 success proportion | 28.4% |

> p̂ = 310 ÷ 1,000 = 0.31  
> SE(p̂) = √[p̂(1−p̂)/N] = √[0.31×0.69/1,000] = 0.01462532  
> Approximate sampling interval = 0.31 ± 1.96×0.01462532  
> = **28.13% to 33.87%**

Percentiles use inclusive linear interpolation, equivalent to Excel `PERCENTILE`. For a sorted sample and probability p, the zero-based position is (N−1)p; interpolate between its adjacent observations. The sampling interval is a normal approximation under the assumed independent trials. It excludes uncertainty about returns, inflation, contributions, parameters and legislation. The model omits serial correlation, market regimes, stochastic inflation, salary-return dependence and withdrawals. Fee sensitivity recalculates every year with an additional fee, preserving dated cash contributions. Contribution pauses and fee/return controls can be tested using the same draws. The simulation is an exploration of assumptions, not an estimate of Kenyan retirement success rates.

## Workbook map

| Modelling sheet | Main equivalence |
|---|---|
| Accumulation | Wealth recursion, fee calculation, inflation product and real conversion |
| Monte Carlo | Lognormal factors, path recursion, real terminal wealth and target indicator |
| Results | Mean/median/percentiles, indicator average, binomial sampling standard error and batch comparisons |
| Fee sensitivity | Repeated wealth recursion with fₜ replaced by fₜ + δf |

Literal representative Excel formulas and cell locations are in `Formula dictionary`. The methodological reference is Part 2 [5], [Glasserman](https://doi.org/10.1007/978-0-387-21617-1). Legal and behavioural references remain numbered in Part 2; they support the stated context rather than calibrating the invented return assumptions.
