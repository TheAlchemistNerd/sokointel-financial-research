# Appendix 4; Amortisation, household DCF and stress

## Scope and timing

This is a household rent-versus-buy model, not a corporate enterprise valuation. Financing uses equal monthly periods and a nominal annual rate divided by twelve, with no actual-day accrual. Payments are recast using the current balance and remaining term, including after extra principal. Terms up to 360 months are supported. The comparison horizon is a whole number of years from one to thirty. Monthly operating flows are aggregated at each year end for valuation. Initial cash occurs at time zero and sale at the selected horizon. Rates and flows are nominal. Actual lender reset dates, fees, penalties, day-count conventions and transaction costs must replace the illustrative assumptions where they differ.

## Dictionary

| Symbol | Meaning | Base / units |
|---|---|---|
| V₀ | Purchase price | KES 6 million |
| α | Deposit fraction | 20% |
| kᵦ, kₛ | Purchase / sale cost fractions | 4%, 3%; assumed |
| L₀ | Loan principal | KES 4.8 million |
| n | Contractual term | 240 months |
| j, r | Nominal annual / monthly rate | 13%; r=j/12 |
| Mₘ | Scheduled payment | KES/month |
| Bₘ | Closing loan balance | KES |
| Iₘ, Aₘ | Interest / principal paid | KES/month |
| T, Q | Taxable pay before interest / reliefs | KES 170,000 / 3,150 monthly |
| Rₜ | Annual rent avoided | KES; starts at 360,000 |
| Oₜ | Ownership costs | KES; opening value×cost fraction |
| H | Sale horizon | 20 years |
| d | Opportunity discount rate | 9% nominal, after tax and fees |
| ΔCFₜ | Buy-minus-rent cash difference | Positive favours buying |
| Zₜ | Renter-minus-buyer accumulated wealth | Positive favours renting |

## Equation (4.1): initial cash

> Deposit = αV₀ = 0.20×6,000,000 = 1,200,000  
> Purchase costs = kᵦV₀ = 0.04×6,000,000 = 240,000  
> Initial cash C₀ = 1,200,000+240,000 = **1,440,000**  
> Loan = 6,000,000−1,200,000 = **4,800,000**

The KES 300,000 emergency reserve is additional. The cost allowance is not a universal statutory rate and should be replaced by the actual transaction cost schedule.

## Equation (4.2): payment derivation and amortisation

With constant monthly rate r and payment M at month end:

> Bₘ = Bₘ₋₁(1+r)−M  
> Bₙ = L₀(1+r)ⁿ−M[(1+r)ⁿ−1]/r

Set Bₙ=0 and solve:

> M = L₀r÷[1−(1+r)⁻ⁿ]

If r=0, M=L₀/n. The workbook has an explicit zero-rate branch.

> r = 0.13÷12 = 0.010833333333  
> M = 4,800,000×0.010833333333÷[1−1.010833333333⁻²⁴⁰]  
> ≈ **56,235.634141**

First-month allocation:

> I₁ = 4,800,000×0.13/12 = **52,000**  
> A₁ = 56,235.634141−52,000 = **4,235.634141**  
> B₁ = 4,800,000−4,235.634141 = **4,795,764.365859**

Constant-rate full-term check:

> Payments = 240×56,235.634141 = **13,496,552.19**  
> Interest = 13,496,552.19−4,800,000 = **8,696,552.19**

At a reset, use the outstanding balance and remaining months. Extra principal is capped at the balance after scheduled principal. This model reduces later payments through recasting rather than automatically shortening the term. Prepayment penalties and lender-specific rules require separate treatment.

## Equation (4.3): tax saving and housing cash

B(T) is the tax-band function from Appendix 1:

> Dₘ = min(qualifying Iₘ,30,000)  
> Savingₘ = max(0,B(T)−Q)−max(0,B(max(0,T−Dₘ))−Q)

Manual first month:

> D₁ = min(52,000,30,000) = 30,000  
> B(170,000) = 2,400+2,083.25+(170,000−32,333)×30% = 45,783.35  
> PAYE before interest = 45,783.35−3,150 = 42,633.35  
> B(140,000) = 2,400+2,083.25+(140,000−32,333)×30% = 36,783.35  
> PAYE after interest = 36,783.35−3,150 = 33,633.35  
> Saving = 42,633.35−33,633.35 = **9,000**

> Ownership allowance = 6,000,000×1%÷12 = 5,000  
> Net housing cost = 56,235.634141+5,000−9,000 = **52,235.634141**  
> Surplus = 125,000−50,000−52,235.634141 = **22,764.365859**

The deduction assumes money borrowed from one of the first six categories of financial institutions specified in the Income Tax Act’s Fourth Schedule to purchase or improve residential premises occupied by the borrower. The interest statement and actual use of the property must support the claim. The annual monetary ceiling is KES 360,000, represented as KES 30,000 monthly in payroll. Principal is not deducted. Current law is held constant in projections. Income-disruption stresses reduce available cash directly and conservatively assume no mortgage tax saving; they do not represent a reconstructed payslip. See Part 4 references [1]–[2] for the conditions and amendment.

## Annual flows and exit equity

> Vₜ = Vₜ₋₁(1+gₜ)  
> Oₜ = opening Vₜ₋₁×cost fractionₜ  
> Operating ΔCFₜ = Rₜ−Σₘ(Iₘ+Aₘ)−Oₜ+Σₘ tax savings  
> Exit equity = Vᴴ(1−kₛ)−debt at H−entered exit tax

Exit equity enters only the selected horizon year. Later comparison cash flows are zero. The loan schedule continues for its full term. At a shorter sale horizon, outstanding debt must be deducted from proceeds. Zero exit tax is an assumption requiring actual tax analysis, not an asserted exemption. There is no perpetual-growth terminal value.

First-year expansion:

> Rent avoided = 360,000  
> Debt service = 12×56,235.634141 = 674,827.609696  
> Ownership costs = 60,000; tax savings = 108,000  
> ΔCF₁ = 360,000−674,827.609696−60,000+108,000  
> = **−266,827.609696**

## NPV and discounted cash flow

> NPV = −C₀+Σₜ₌₁ᴴ ΔCFₜ/(1+d)ᵗ  
> PV₁ = −266,827.609696÷1.09 = **−244,796.89**  
> NPV using the complete annual sequence = **−732,620.764742**

Excel equivalence: NPV(discount rate, year-one through year-thirty differences) minus initial cash. Excel NPV discounts its first listed value one period. Including the deposit in that range would wrongly discount a time-zero payment. The main valuation sheet also shows explicit annual discount factors and present values.

## Terminal-wealth reconciliation

Set Z₀=C₀. For each year through the horizon:

> Zₜ = Zₜ₋₁(1+d)−ΔCFₜ  
> Zᴴ = C₀(1+d)ᴴ−ΣΔCFₜ(1+d)ᴴ⁻ᵗ  
> NPV = −Zᴴ/(1+d)ᴴ

Numerical check:

> Z₂₀ = **4,105,907.702618**  
> −4,105,907.702618÷1.09²⁰ = **−732,620.764742**  
> NPV+Z₂₀/1.09²⁰ ≈ **0**

This checks signs, initial cash, terminal debt and timing. It assumes a common opportunity rate even if intermediate alternative wealth becomes negative. It is a valuation identity, not proof that a household can borrow or invest at that rate without constraints.

## Sensitivity and stress

| Discount rate; other cash flows unchanged | Buy-minus-rent NPV, KES |
|---:|---:|
| 5% | 1,246,523.89 |
| 7% | 51,695.02 |
| 9% | (732,620.76) |
| 11% | (1,246,142.69) |
| 13% | (1,580,214.65) |

The rate-and-income table recalculates the initial payment at rates from 9% to 17%, with combined cases reducing available cash by 25%, 50% or 100%. With monthly deficit D>0, reserve runway=300,000/D. Otherwise it reports “No deficit.” This bridge excludes a simultaneous medical bill. A consolidated household stress must use one reserve and one cash schedule. The medical workbook’s reserve must not be added as if it were separate money.

## Workbook map and evidence

| Modelling sheet | Formula families |
|---|---|
| Amortization | Payment, interest, principal, balance, capped deduction and exact tax difference |
| Rent versus buy | Annual differences, sale equity, discount factors and alternative wealth |
| Results | Initial cash, surplus, NPV and independent reconciliations |
| Rate and income stress | Repriced payment, income loss, deficit and runway |
| Discount sensitivity | Full cash-flow NPV at each rate |

Literal Excel expressions and addresses are in Formula dictionary. IEEE references [1]–[5] in Part 4 support the statutory mechanics and household-risk context, including [Campbell and Cocco](https://doi.org/10.1162/003355303322552847). Prices, rates, costs and valuation outputs are original illustrative assumptions and calculations.
