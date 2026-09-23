# Appendix 3; Medical claims and emergency liquidity

## Scope and dictionary

This is a contract-mechanics illustration with invented policy terms, not an implementation of the SHA benefit schedule or any insurer’s product. It models one material annual medical event, an annual deductible and payment limit, and one possible earnings interruption. Public payment is an assumed fraction of the gross bill. Private eligibility applies to the residual after public payment. Actual contract coordination must replace that assumption. The opening reserve is available after the premium is funded separately. Final annual costs are modelled; hospital deposits, reimbursement delays, repeated claims and family sublimits require a dated claims schedule. All claims, policy terms and probabilities are hypothetical, not calibrated to the historical Kenyan study cited in Part 3.

| Symbol | Meaning | Base assumption |
|---|---|---:|
| L | Gross bill, KES | Scenario or simulated |
| a | Public payment fraction | 20% |
| e | Private eligible share of residual | 85% |
| d | Annual deductible, KES | 20,000 |
| c | Patient coinsurance after deductible | 10% |
| M | Private payment limit, KES | 500,000 |
| P | Annual private premium, KES | 60,000 |
| O | Other qualifying premiums, KES/year | 0 |
| T | Tax available before insurance relief, after personal relief | KES 300,000/year |
| R | Opening accessible reserve, KES | 300,000 |
| X | Essential spending, KES/month | 75,000 |
| h | Months without earnings | 4 |
| p | Material-event probability | 20% |
| m | Conditional arithmetic mean bill, KES | 300,000 |
| s | Log-bill standard deviation | 0.9 |
| q₁, q₀ | Interruption probabilities with / without event | 25%, 8% |
| N | Simulated years | 2,000 |

## Equation (3.1): claim waterfall

> Public payment A = aL  
> Residual V = L − A  
> Private eligible E = eV  
> After deductible D = max(0,E−d)  
> Private payment B = min(M,D×(1−c))  
> Patient bill Y = L−A−B

Manual KES 300,000 claim:

> A = 0.20×300,000 = 60,000  
> V = 300,000−60,000 = 240,000  
> E = 0.85×240,000 = 204,000  
> D = 204,000−20,000 = 184,000  
> B = min(500,000,184,000×0.90) = 165,600  
> Y = 300,000−60,000−165,600 = **74,400**

Independent allocation check:

> Uncovered residual = 240,000×15% = 36,000  
> Deductible = 20,000  
> Coinsurance = 184,000×10% = 18,400  
> Total patient allocation = 36,000+20,000+18,400 = **74,400**

Manual KES 1 million claim:

> Public payment = 200,000; residual = 800,000  
> Eligible = 800,000×85% = 680,000  
> Uncapped private payment = (680,000−20,000)×90% = 594,000  
> Private payment = min(500,000,594,000) = 500,000  
> Patient bill = 1,000,000−200,000−500,000 = **300,000**

With a zero bill, all payments are zero. Below the deductible, private payment is zero rather than negative. The model requires a, e and c between zero and one and non-negative bills, deductible and limit. Those constraints preserve public payment + private payment + patient payment = gross bill. They do not establish contractual eligibility.

## Equation (3.2): shared relief and annual cost

> Credit with policy = min(60,000,15%×(O+P),T)  
> Credit without policy = min(60,000,15%×O,T)  
> Incremental credit = credit with policy−credit without policy  
> Net premium = P−incremental credit

Base substitution:

> Incremental credit = min(60,000,0.15×60,000,300,000)−0 = 9,000  
> Net premium = 60,000−9,000 = **51,000**  
> Cost in the KES 300,000 claim year = 51,000+74,400 = **125,400**

If other qualifying premiums total KES 400,000, they already use the KES 60,000 credit ceiling, assuming adequate tax. Incremental relief on this medical premium becomes zero. If tax available is only KES 3,000 and there are no other premiums, the usable credit is KES 3,000. Neither the maximum credit nor the headline 15% is an automatic refund. SHIF is excluded from this private-cost total because payroll handles it separately. PRMF contributions use a separate deduction mechanism.

## Equation (3.3): combined cash need

> Interruption spending = J×h×X, with J either 0 or 1  
> Combined need C = Y+J×h×X  
> Unfunded amount G = max(0,C−R)  
> Shortfall indicator = 1{G>0}

For the first claim and four months without earnings:

> Interruption spending = 4×75,000 = 300,000  
> Combined need = 74,400+300,000 = 374,400  
> Gap = 374,400−300,000 = **74,400**  
> Simple no-claim runway = 300,000÷75,000 = **4 months**

The event counted is strictly positive funding shortfall. A need exactly equal to the reserve leaves nothing remaining but is not counted as a shortfall. This boundary matters because interruption spending alone equals the base reserve. Read “reserve exhausted” in the workbook as a positive funding-gap indicator, rather than any depletion of the reserve.

## Monte Carlo formulation and reproducibility

> Event E = 1{U<p}  
> L = E×exp[ln(m)−s²/2+sZ]  
> J = 1{V<q₁} when E=1; otherwise J = 1{V<q₀}

U and V are independent uniforms and Z is standard normal. Bill severity and interruption are independent conditional on event status. The model does not make larger bills increase interruption probability further. This is an explicit limitation.

The generator uses seed **20260908**:

> stateₖ₊₁ = (1,664,525×stateₖ+1,013,904,223) modulo 2³²  
> Uₖ = (stateₖ+0.5)÷2³²  
> Z = √(−2 ln U₁)×cos(2πU₂)

Draw order per trial is event uniform, two uniforms for severity, then interruption uniform. Fixed draws are stored in the workbook and live formulas transform them. The s²/2 adjustment preserves conditional arithmetic mean m. There is no upper cap on the gross bill. The severity family, event frequency and dependence are assumptions, not a fit to patient records. The simple generator is a reproducibility device rather than a production risk engine. A larger or alternative-seed study can improve convergence assessment, but neither more trials nor a more sophisticated generator establishes whether the economic and contractual assumptions are appropriate for a real household. That requires additional evidence and specification.

## Fixed-run results and checks

| Output | Value |
|---|---:|
| Mean patient bill | KES 17,182.09 |
| Mean combined cash need | KES 56,032.09 |
| 95th percentile combined need | KES 331,800.46 |
| 99th percentile combined need | KES 419,307.94 |
| Positive shortfalls | 118/2,000 = 5.9% |
| Mean unfunded amount, all trials | KES 5,848.40 |
| Expected private medical cost in sample | KES 68,182.09 |

Analytical interruption expectation:

> Pr(J=1) = pq₁+(1−p)q₀  
> = 0.20×0.25+0.80×0.08 = **0.114**  
> Expected interruption spending = 0.114×4×75,000 = **34,200**

The fixed sample contains 259 interruptions, or 12.95%, giving KES 38,850 average interruption spending. It reconciles sample averages: 17,182.09+38,850=56,032.09. The sample differs from the analytical expectation and that difference is disclosed, not silently replaced by a theoretical number. Higher-trial and alternative-seed checks are appropriate before small probability differences inform actual policy choices.

> SE(p̂) = √[0.059×0.941÷2,000] = **0.00526873**  
> Approximate 95% sampling interval = 0.059±1.96×0.00526873  
> = **4.87% to 6.93%**

This interval excludes parameter and model uncertainty. Percentiles use inclusive linear interpolation at zero-based sorted position (N−1)p. Reserve sensitivity computes count(C>R)/N on the same paths at each reserve, ensuring a monotone comparison. Policy sensitivity should recalculate the full claim waterfall when terms change.

## Workbook map and evidence

| Modelling sheet | Mathematical families |
|---|---|
| Claims scenarios | Claim waterfall, shared credit cap and annual cost |
| Monte Carlo | Bernoulli event, lognormal severity, conditional interruption and gap |
| Results | Means, percentiles, indicator proportions and standard error |
| Reserve sensitivity | Exceedance frequency and spending runway |

Literal Excel expressions and addresses appear in the workbook’s Formula dictionary. IEEE references [1]–[6] in Part 3 provide the legal and research context. The [Salari et al. study](https://doi.org/10.1136/bmjgh-2019-001809) supplies no calibration for these invented probabilities.


## Additional convergence runs

These independent checks use the same model and draw algorithm. They supplement the editable 2,000-trial workbook without replacing its fixed sample.

| Seed | Trials | Mean combined need, KES | Positive shortfall rate | Interruption rate |
|---:|---:|---:|---:|---:|
| 20260908 | 2,000 | 56,032.09 | 5.900% | 12.950% |
| 20260908 | 20,000 | 53,517.33 | 5.675% | 11.745% |
| 20260909 | 20,000 | 53,249.70 | 5.595% | 11.635% |
| 20260910 | 20,000 | 54,256.30 | 5.820% | 11.825% |

The larger runs produce shortfall rates between 5.595% and 5.820%, compared with 5.900% in the workbook. These differences support cautious interpretation of small scenario changes. They do not resolve model uncertainty or validate the hypothetical insurance terms.
