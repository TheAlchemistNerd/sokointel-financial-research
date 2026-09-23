# Formula dictionaries

Cell expressions below are literal Excel formulas. Mathematical equivalents and variable definitions are expanded in the numbered appendices. Policy parameters are versioned inputs, and all amounts are KES unless labelled otherwise.


## 01-PAYE-and-Cash-Flow


### Payroll: B8

**Mathematical equivalent:** N = 0.06 × min(pensionable pay, earnings ceiling)

**Variables and assumptions:** Ceiling 72,000 January; 108,000 February–December. Employee only; S05–S06.

**Excel:**

> ='Policy'!$B$21*MIN('Monthly inputs'!D8,'Policy'!$B$23)


### Payroll: C8

**Mathematical equivalent:** A = 0.015 × AHL base

**Variables and assumptions:** S11; employer match excluded from employee cash.

**Excel:**

> ='Policy'!$B$18*'Monthly inputs'!E8


### Payroll: D8

**Mathematical equivalent:** H = max(300, 0.0275 × SHIF base)

**Variables and assumptions:** S07; active salaried membership for all 12 months.

**Excel:**

> =MAX('Policy'!$B$20,'Policy'!$B$19*'Monthly inputs'!F8)


### Payroll: E8

**Mathematical equivalent:** P = min(N + private pension, 0.30 × pension tax income, 30,000)

**Variables and assumptions:** S02–S04; section 22A occupational defined-contribution illustration. Separate tax pensionable income and NSSF earnings inputs; section 22B individual-fund rules require separate review.

**Excel:**

> =MIN(B8+'Monthly inputs'!G8,'Policy'!$B$13*'Monthly inputs'!L8,'Policy'!$B$12)


### Payroll: F8

**Mathematical equivalent:** R = min(PRMF cash contribution, 15,000)

**Variables and assumptions:** S02; separate qualifying fund deduction.

**Excel:**

> =MIN('Monthly inputs'!H8,'Policy'!$B$14)


### Payroll: G8

**Mathematical equivalent:** I = min(qualifying interest paid, 30,000)

**Variables and assumptions:** S02; principal is not deductible.

**Excel:**

> =MIN('Monthly inputs'!J8,'Policy'!$B$15)


### Payroll: H8

**Mathematical equivalent:** T = max(0, cash gross + taxable noncash − A − H − P − R − I)

**Variables and assumptions:** Monthly taxable employment income.

**Excel:**

> =MAX(0,'Monthly inputs'!B8+'Monthly inputs'!C8-SUM(C8:G8))


### Payroll: I8

**Mathematical equivalent:** B(T) = Σ rateⱼ × max(0, min(T − lowerⱼ, widthⱼ))

**Variables and assumptions:** Monthly widths 24,000; 8,333; 467,667; 300,000; unbounded. Rates 10%,25%,30%,32.5%,35%. S01.

**Excel:**

> ='Policy'!$F$7*MIN(MAX(0,(H8)-'Policy'!$D$7),'Policy'!$E$7)+'Policy'!$F$8*MIN(MAX(0,(H8)-'Policy'!$D$8),'Policy'!$E$8)+'Policy'!$F$9*MIN(MAX(0,(H8)-'Policy'!$D$9),'Policy'!$E$9)+'Policy'!$F$10*MIN(MAX(0,(H8)-'Policy'!$D$10),'Policy'!$E$10)+'Policy'!$F$11*MIN(MAX(0,(H8)-'Policy'!$D$11),'Policy'!$E$11)


### Payroll: J8

**Mathematical equivalent:** Q = min(0.15 × qualifying premium, 5,000)

**Variables and assumptions:** S08. Relief is non-refundable; annual cap 60,000.

**Excel:**

> =MIN('Policy'!$B$16*'Monthly inputs'!I8,'Policy'!$B$17)


### Payroll: K8

**Mathematical equivalent:** PAYE = max(0, B(T) − personal relief − Q)

**Variables and assumptions:** Resident personal relief 2,400 monthly.

**Excel:**

> =MAX(0,I8-'Policy'!$B$11-J8)


### Payroll: L8

**Mathematical equivalent:** C = gross cash − NSSF − AHL − SHIF − PAYE − private pension − PRMF − premium − interest

**Variables and assumptions:** After listed commitments, whether payroll withheld or paid separately. Principal and other debt must enter household spending.

**Excel:**

> ='Monthly inputs'!B8-B8-C8-D8-K8-'Monthly inputs'!G8-'Monthly inputs'!H8-'Monthly inputs'!I8-'Monthly inputs'!J8


### Payroll: M8

**Mathematical equivalent:** S = cash after commitments − essential spending

**Variables and assumptions:** Spending includes rent and other cash costs; no double counting insurance/pension/interest.

**Excel:**

> =L8-'Monthly inputs'!K8


### Annual reconciliation: B7

**Mathematical equivalent:** Annual reconciliation.B7 = sum('Payroll'!H7:H18)

**Variables and assumptions:** Employment taxable income under monthly deduction assumptions.

**Excel:**

> =SUM('Payroll'!H7:H18)


### Annual reconciliation: B8

**Mathematical equivalent:** Annual reconciliation.B8 = 'Inputs'!B7

**Variables and assumptions:** Classify income before entry.

**Excel:**

> ='Inputs'!B7


### Annual reconciliation: B9

**Mathematical equivalent:** Annual reconciliation.B9 = sum(B7:B8)

**Variables and assumptions:** Assumes deductible amounts already assigned correctly; no cross-source loss offset model.

**Excel:**

> =SUM(B7:B8)


### Annual reconciliation: B10

**Mathematical equivalent:** Annual reconciliation.B10 = 'Policy'!$F$15×MIN(MAX(0,(B9)-'Policy'!$D$15),'Policy'!$E$15)+'Policy'!$F$16×MIN(MAX(0,(B9)-'Policy'!$D$16),'Policy'!$E$16)+'Policy'!$F$17×MIN(MAX(0,(B9)-'Policy'!$D$17),'Policy'!$E$17)+'Policy'!$F$18×MIN(MAX(0,(B9)-'Policy'!$D$18),'Policy'!$E$18)+'Policy'!$F$19×MIN(MAX(0,(B9)-'Policy'!$D$19),'Policy'!$E$19)

**Variables and assumptions:** Exact annual bands; monthly rounding differs slightly.

**Excel:**

> ='Policy'!$F$15*MIN(MAX(0,(B9)-'Policy'!$D$15),'Policy'!$E$15)+'Policy'!$F$16*MIN(MAX(0,(B9)-'Policy'!$D$16),'Policy'!$E$16)+'Policy'!$F$17*MIN(MAX(0,(B9)-'Policy'!$D$17),'Policy'!$E$17)+'Policy'!$F$18*MIN(MAX(0,(B9)-'Policy'!$D$18),'Policy'!$E$18)+'Policy'!$F$19*MIN(MAX(0,(B9)-'Policy'!$D$19),'Policy'!$E$19)


### Annual reconciliation: B11

**Mathematical equivalent:** Annual reconciliation.B11 = (12×'Policy'!$B$11)

**Variables and assumptions:** Resident full-year illustration.

**Excel:**

> =(12*'Policy'!$B$11)


### Annual reconciliation: B12

**Mathematical equivalent:** Annual reconciliation.B12 = MIN((12×'Policy'!$B$17),'Policy'!$B$16×sum('Monthly inputs'!I7:I18))

**Variables and assumptions:** Qualifying premiums only.

**Excel:**

> =MIN((12*'Policy'!$B$17),'Policy'!$B$16*SUM('Monthly inputs'!I7:I18))


### Annual reconciliation: B13

**Mathematical equivalent:** Annual reconciliation.B13 = MAX(0,B10-B11-B12)

**Variables and assumptions:** Before income-tax credits.

**Excel:**

> =MAX(0,B10-B11-B12)


### Annual reconciliation: B14

**Mathematical equivalent:** Annual reconciliation.B14 = sum('Payroll'!K7:K18)

**Variables and assumptions:** From payroll schedule.

**Excel:**

> =SUM('Payroll'!K7:K18)


### Annual reconciliation: B15

**Mathematical equivalent:** Annual reconciliation.B15 = sum('Inputs'!B8:B9)

**Variables and assumptions:** No final withholding tax credit assumed.

**Excel:**

> =SUM('Inputs'!B8:B9)


### Annual reconciliation: B16

**Mathematical equivalent:** Annual reconciliation.B16 = B13-B14-B15

**Variables and assumptions:** Positive: further income tax; negative: potential overpayment, subject to reconciliation.

**Excel:**

> =B13-B14-B15


### Annual reconciliation: B17

**Mathematical equivalent:** Annual reconciliation.B17 = MAX(0,'Policy'!$F$15×MIN(MAX(0,(B7)-'Policy'!$D$15),'Policy'!$E$15)+'Policy'!$F$16×MIN(MAX(0,(B7)-'Policy'!$D$16),'Policy'!$E$16)+'Policy'!$F$17×MIN(MAX(0,(B7)-'Policy'!$D$17),'Policy'!$E$17)+'Policy'!$F$18×MIN(MAX(0,(B7)-'Policy'!$D$18),'Policy'!$E$18)+'Policy'!$F$19×MIN(MAX(0,(B7)-'Policy'!$D$19),'Policy'!$E$19)-B11-B12)

**Variables and assumptions:** Independent annual salary band calculation.

**Excel:**

> =MAX(0,'Policy'!$F$15*MIN(MAX(0,(B7)-'Policy'!$D$15),'Policy'!$E$15)+'Policy'!$F$16*MIN(MAX(0,(B7)-'Policy'!$D$16),'Policy'!$E$16)+'Policy'!$F$17*MIN(MAX(0,(B7)-'Policy'!$D$17),'Policy'!$E$17)+'Policy'!$F$18*MIN(MAX(0,(B7)-'Policy'!$D$18),'Policy'!$E$18)+'Policy'!$F$19*MIN(MAX(0,(B7)-'Policy'!$D$19),'Policy'!$E$19)-B11-B12)


### Annual reconciliation: B18

**Mathematical equivalent:** Annual reconciliation.B18 = B14-B17

**Variables and assumptions:** KES +0.20 typical at this salary due to published integer monthly band.

**Excel:**

> =B14-B17


### Pension sensitivity: E7

**Mathematical equivalent:** PAYE(x) = max(0,B(T(x)) − 2,400 − Q)

**Variables and assumptions:** All other February inputs held constant.

**Excel:**

> =MAX(0,'Policy'!$F$7*MIN(MAX(0,(D7)-'Policy'!$D$7),'Policy'!$E$7)+'Policy'!$F$8*MIN(MAX(0,(D7)-'Policy'!$D$8),'Policy'!$E$8)+'Policy'!$F$9*MIN(MAX(0,(D7)-'Policy'!$D$9),'Policy'!$E$9)+'Policy'!$F$10*MIN(MAX(0,(D7)-'Policy'!$D$10),'Policy'!$E$10)+'Policy'!$F$11*MIN(MAX(0,(D7)-'Policy'!$D$11),'Policy'!$E$11)-'Policy'!$B$11-'Payroll'!J8)


### Pension sensitivity: G7

**Mathematical equivalent:** Tax saving(x) = baseline PAYE − PAYE(x)

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> ='Payroll'!K8-E7


### Pension sensitivity: H7

**Mathematical equivalent:** Net cash cost(x) = extra pension − tax saving(x)

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =A7-G7


### Policy: D8:E11

**Mathematical equivalent:** Monthly lower bound bⱼ = bⱼ₋₁ + widthⱼ₋₁; widths link to B7:B10

**Variables and assumptions:** Tax rates and annual schedule are versioned policy values. Keep annual and monthly schedules coherent when updating legislation.

**Excel:**

> =D7+E7


## 02-Pensions-and-Retirement


### Accumulation: C7

**Mathematical equivalent:** Cₜ = (employeeₜ + employerₜ) × contribution multiplier

**Variables and assumptions:** Annual end-year contributions; employer match assumed, not statutory private-plan entitlement.

**Excel:**

> =SUM('Annual assumptions'!B7:C7)*'Inputs'!$B$9


### Accumulation: E7

**Mathematical equivalent:** Feeₜ = opening wealth × (1 + gross returnₜ) × feeₜ

**Variables and assumptions:** Fee after investment return, before end-year contribution.

**Excel:**

> =(B7+D7)*('Annual assumptions'!F7+'Inputs'!$B$10)


### Accumulation: F7

**Mathematical equivalent:** Wₜ = Wₜ₋₁(1 + μₜ)(1 − fₜ) + Cₜ

**Variables and assumptions:** Deterministic expected-wealth path under independent returns. Excludes benefit withdrawal tax and NSSF account.

**Excel:**

> =B7+C7+D7-E7


### Accumulation: H7

**Mathematical equivalent:** Real Wₜ = Wₜ / Π(1 + inflationⱼ)

**Variables and assumptions:** Base purchasing power at start of first projection year.

**Excel:**

> =F7/G7


### Accumulation: I7

**Mathematical equivalent:** Chart year = calendar year of projection date

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =YEAR(A7)


### Monte Carlo: B7:AE1006

**Mathematical equivalent:** Wₜ = Wₜ₋₁ exp[ln(1+μₜ) − σₜ²/2 + σₜZₜ] (1−fₜ) + Cₜ

**Variables and assumptions:** Z independent standard normal; μ arithmetic expected gross return; σ log-return standard deviation; seed 20260907.

**Excel:**

> ='Inputs'!$B$7*EXP(LN(1+'Annual assumptions'!D7+'Inputs'!$B$11)-'Annual assumptions'!E7^2/2+'Annual assumptions'!E7*'Random draws'!B7)*(1-'Annual assumptions'!F7-'Inputs'!$B$10)+'Accumulation'!C7


### Monte Carlo: AF7:AG1006

**Mathematical equivalent:** Real terminal = W₃₀ / price index; success = 1{real terminal ≥ target}

**Variables and assumptions:** Fixed inflation path; no salary-return correlation, serial dependence, regime changes or withdrawal sequence model.

**Excel:**

> =AE7/'Accumulation'!$G$36


### Results: B7

**Mathematical equivalent:** Results.B7 = 'Accumulation'!F36

**Variables and assumptions:** Expected wealth under model assumptions.

**Excel:**

> ='Accumulation'!F36


### Results: B8

**Mathematical equivalent:** Results.B8 = 'Accumulation'!H36

**Variables and assumptions:** Inflation-adjusted; not the simulated median.

**Excel:**

> ='Accumulation'!H36


### Results: B9

**Mathematical equivalent:** Results.B9 = median('Monte Carlo'!AF7:AF1006)

**Variables and assumptions:** Central result among 1,000 hypothetical paths.

**Excel:**

> =MEDIAN('Monte Carlo'!AF7:AF1006)


### Results: B10

**Mathematical equivalent:** Results.B10 = quantile('Monte Carlo'!AF7:AF1006,0.1)

**Variables and assumptions:** Lower-tail marker, not a guarantee.

**Excel:**

> =PERCENTILE('Monte Carlo'!AF7:AF1006,0.1)


### Results: B11

**Mathematical equivalent:** Results.B11 = quantile('Monte Carlo'!AF7:AF1006,0.9)

**Variables and assumptions:** Upper-tail marker.

**Excel:**

> =PERCENTILE('Monte Carlo'!AF7:AF1006,0.9)


### Results: B12

**Mathematical equivalent:** Results.B12 = mean('Monte Carlo'!AG7:AG1006)

**Variables and assumptions:** Conditional on chosen model and assumptions.

**Excel:**

> =AVERAGE('Monte Carlo'!AG7:AG1006)


### Results: B13

**Mathematical equivalent:** Results.B13 = sqrt(B12×(1-B12)÷1000)

**Variables and assumptions:** Sampling error only; excludes model uncertainty.

**Excel:**

> =SQRT(B12*(1-B12)/1000)


### Results: B14

**Mathematical equivalent:** Results.B14 = mean('Monte Carlo'!AG7:AG506)

**Variables and assumptions:** Batch diagnostic; comparison with full run.

**Excel:**

> =AVERAGE('Monte Carlo'!AG7:AG506)


### Results: B15

**Mathematical equivalent:** Results.B15 = mean('Monte Carlo'!AG507:AG1006)

**Variables and assumptions:** Independent stream segment; no calibration claim.

**Excel:**

> =AVERAGE('Monte Carlo'!AG507:AG1006)


### Results: B16

**Mathematical equivalent:** Results.B16 = MAX(0,B12-1.96×B13)

**Variables and assumptions:** Normal approximation for simulation sampling uncertainty.

**Excel:**

> =MAX(0,B12-1.96*B13)


### Results: B17

**Mathematical equivalent:** Results.B17 = MIN(1,B12+1.96×B13)

**Variables and assumptions:** Not a forecast confidence interval.

**Excel:**

> =MIN(1,B12+1.96*B13)


### Fee sensitivity: B7

**Mathematical equivalent:** Wₜ(δf) = Wₜ₋₁(1+μₜ)(1−fₜ−δf)+Cₜ

**Variables and assumptions:** Only additional fee differs; all dated contribution and return inputs preserved.

**Excel:**

> ='Inputs'!$B$7*(1+'Annual assumptions'!D7+'Inputs'!$B$11)*(1-'Annual assumptions'!F7-'Inputs'!$B$10-$A7)+'Accumulation'!C7


### Fee sensitivity: AF7

**Mathematical equivalent:** Real final = scenario wealth / cumulative price index

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =AE7/'Accumulation'!$G$36


### Policy: D8:E11

**Mathematical equivalent:** Monthly lower bound bⱼ = bⱼ₋₁ + widthⱼ₋₁; widths link to B7:B10

**Variables and assumptions:** Tax rates and annual schedule are versioned policy values. Keep annual and monthly schedules coherent when updating legislation.

**Excel:**

> =D7+E7


## 03-Medical-and-Emergency-Funds


### Claims scenarios: B7

**Mathematical equivalent:** SHA scenario payment = gross bill × assumed fraction

**Variables and assumptions:** Illustrative fraction, not SHA tariff, entitlement or claim adjudication.

**Excel:**

> =A7*'Inputs'!$B$13


### Claims scenarios: C7

**Mathematical equivalent:** Residual = gross bill − SHA payment

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =A7-B7


### Claims scenarios: D7

**Mathematical equivalent:** Eligible residual = residual × private eligible share

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =C7*'Inputs'!$B$14


### Claims scenarios: E7

**Mathematical equivalent:** After deductible = max(0, eligible residual − deductible)

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =MAX(0,D7-'Inputs'!$B$15)


### Claims scenarios: F7

**Mathematical equivalent:** Private payment = min(limit, after deductible × (1 − patient coinsurance))

**Variables and assumptions:** One aggregated material event; coordination of benefits expressly assumed.

**Excel:**

> =MIN('Inputs'!$B$17,E7*(1-'Inputs'!$B$16))


### Claims scenarios: G7

**Mathematical equivalent:** Patient bill = gross bill − public payment − private payment

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =A7-B7-F7


### Claims scenarios: H7

**Mathematical equivalent:** Net premium = premium − incremental usable insurance relief

**Variables and assumptions:** Annual credit cap shared across qualifying policies. Uses tax available after personal relief.

**Excel:**

> ='Inputs'!$B$7-(MIN((12*'Policy'!$B$17),'Policy'!$B$16*('Inputs'!$B$7+'Inputs'!$B$8),'Inputs'!$B$9)-MIN((12*'Policy'!$B$17),'Policy'!$B$16*'Inputs'!$B$8,'Inputs'!$B$9))


### Claims scenarios: I7

**Mathematical equivalent:** Annual household medical cost = patient bill + net premium

**Variables and assumptions:** Excludes statutory SHIF already in payroll.

**Excel:**

> =G7+H7


### Monte Carlo: B7:C2006

**Mathematical equivalent:** L = 1{U < p} × exp[ln(m) − s²/2 + sZ]

**Variables and assumptions:** m conditional arithmetic mean bill; s log standard deviation; U uniform and Z standard normal; seed 20260908.

**Excel:**

> =B7*EXP(LN('Inputs'!$B$11)-'Inputs'!$B$12^2/2+'Inputs'!$B$12*'Random draws'!C7)


### Monte Carlo: H7:L2006

**Mathematical equivalent:** J = 1{V < q(event)}; need = patient bill + J × months × spending; gap = max(0,need−reserve)

**Variables and assumptions:** Conditional dependence is explicit. One event, one annual interruption; reserve assumed accessible and premium funded separately.

**Excel:**

> =G7+I7


### Results: B7

**Mathematical equivalent:** Results.B7 = mean('Monte Carlo'!G7:G2006)

**Variables and assumptions:** Across all years, including no claim.

**Excel:**

> =AVERAGE('Monte Carlo'!G7:G2006)


### Results: B8

**Mathematical equivalent:** Results.B8 = mean('Monte Carlo'!J7:J2006)

**Variables and assumptions:** Medical bill plus assumed income interruption cost.

**Excel:**

> =AVERAGE('Monte Carlo'!J7:J2006)


### Results: B9

**Mathematical equivalent:** Results.B9 = quantile('Monte Carlo'!J7:J2006,.95)

**Variables and assumptions:** Conditional on specified scenario distributions.

**Excel:**

> =PERCENTILE('Monte Carlo'!J7:J2006,.95)


### Results: B10

**Mathematical equivalent:** Results.B10 = quantile('Monte Carlo'!J7:J2006,.99)

**Variables and assumptions:** Tail is particularly sensitive to severity distribution.

**Excel:**

> =PERCENTILE('Monte Carlo'!J7:J2006,.99)


### Results: B11

**Mathematical equivalent:** Results.B11 = mean('Monte Carlo'!L7:L2006)

**Variables and assumptions:** Positive shortfall, not equality to reserve.

**Excel:**

> =AVERAGE('Monte Carlo'!L7:L2006)


### Results: B12

**Mathematical equivalent:** Results.B12 = sqrt(B11×(1-B11)÷2000)

**Variables and assumptions:** Sampling uncertainty; excludes parameter uncertainty.

**Excel:**

> =SQRT(B11*(1-B11)/2000)


### Results: B13

**Mathematical equivalent:** Results.B13 = mean('Monte Carlo'!K7:K2006)

**Variables and assumptions:** Average across all trials; not average conditional on shortfall.

**Excel:**

> =AVERAGE('Monte Carlo'!K7:K2006)


### Results: B14

**Mathematical equivalent:** Results.B14 = 'Claims scenarios'!H7

**Variables and assumptions:** Paid separately from opening liquid reserve.

**Excel:**

> ='Claims scenarios'!H7


### Results: B15

**Mathematical equivalent:** Results.B15 = B7+B14

**Variables and assumptions:** Premium plus simulated average patient bill; excludes income gap.

**Excel:**

> =B7+B14


### Reserve sensitivity: B7

**Mathematical equivalent:** p̂(gap) = count(need > reserve) / N

**Variables and assumptions:** Same simulated paths at each reserve; avoids random comparison noise.

**Excel:**

> =COUNTIF('Monte Carlo'!J7:J2006,">"&A7)/2000


### Reserve sensitivity: C7

**Mathematical equivalent:** Runway months = reserve / essential monthly expenditure

**Variables and assumptions:** No new inflows and no additional medical event for this simple runway metric.

**Excel:**

> =A7/'Inputs'!$B$19


### Policy: D8:E11

**Mathematical equivalent:** Monthly lower bound bⱼ = bⱼ₋₁ + widthⱼ₋₁; widths link to B7:B10

**Variables and assumptions:** Tax rates and annual schedule are versioned policy values. Keep annual and monthly schedules coherent when updating legislation.

**Excel:**

> =D7+E7


## 04-Mortgages-and-Housing


### Amortization: E7

**Mathematical equivalent:** M = Lr / [1 − (1+r)^(−n)]; if r=0, M=L/n

**Variables and assumptions:** L opening loan; r nominal annual rate/12; n months remaining. Payment recast monthly at current rate, including after prepayment.

**Excel:**

> =IF(D7=0,0,IF(C7=0,B7/D7,B7*C7/(1-(1+C7)^(-D7))))


### Amortization: F7

**Mathematical equivalent:** Interestₘ = opening balanceₘ × monthly rateₘ

**Variables and assumptions:** Equal monthly periods, not actual/365 daily lender accrual.

**Excel:**

> =B7*C7


### Amortization: H7

**Mathematical equivalent:** Principal = min(opening balance, scheduled payment − interest + extra principal)

**Variables and assumptions:** No penalty model; add actual fees to cost inputs where applicable.

**Excel:**

> =MIN(B7,MAX(0,E7-F7)+G7)


### Amortization: J7

**Mathematical equivalent:** D = min(eligible mortgage interest, 30,000)

**Variables and assumptions:** Assumes qualifying owner-occupied borrowing and lender; S02.

**Excel:**

> =MIN(F7,'Policy'!$B$15)


### Amortization: K7

**Mathematical equivalent:** Tax saving = PAYE(T) − PAYE(max(0,T−D))

**Variables and assumptions:** Uses full progressive tax function; no blanket marginal-rate shortcut. Current law held constant.

**Excel:**

> =MAX(0,'Policy'!$F$7*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$7),'Policy'!$E$7)+'Policy'!$F$8*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$8),'Policy'!$E$8)+'Policy'!$F$9*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$9),'Policy'!$E$9)+'Policy'!$F$10*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$10),'Policy'!$E$10)+'Policy'!$F$11*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$11),'Policy'!$E$11)-'Inputs'!$B$16)-MAX(0,'Policy'!$F$7*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-J7))-'Policy'!$D$7),'Policy'!$E$7)+'Policy'!$F$8*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-J7))-'Policy'!$D$8),'Policy'!$E$8)+'Policy'!$F$9*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-J7))-'Policy'!$D$9),'Policy'!$E$9)+'Policy'!$F$10*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-J7))-'Policy'!$D$10),'Policy'!$E$10)+'Policy'!$F$11*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-J7))-'Policy'!$D$11),'Policy'!$E$11)-'Inputs'!$B$16)


### Amortization: L7

**Mathematical equivalent:** Check = opening balance − principal − closing balance = 0

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =B7-H7-I7


### Rent versus buy: H7

**Mathematical equivalent:** ΔCFₜ = rent avoided − principal − interest − ownership costs + tax saving

**Variables and assumptions:** Annual end-year aggregation of monthly flows. Positive favours buying. Principal enters cash flow; remaining debt deducted only at sale.

**Excel:**

> =IF(A7<='Inputs'!$B$13,D7-E7-F7+G7,0)


### Rent versus buy: I7

**Mathematical equivalent:** Exit equity = house value × (1 − sale-cost rate) − debt balance − exit tax

**Variables and assumptions:** Sale only at chosen horizon; no infinite terminal growth formula.

**Excel:**

> =IF(A7='Inputs'!$B$13,C7*(1-'Inputs'!$B$11)-'Amortization'!I18-'Inputs'!$B$12,0)


### Rent versus buy: L7

**Mathematical equivalent:** PVₜ = ΔCFₜ / (1+d)^t

**Variables and assumptions:** Nominal annual discount rate and nominal flows. Time-zero costs excluded here.

**Excel:**

> =J7*K7


### Rent versus buy: M7

**Mathematical equivalent:** Rₜ = Rₜ₋₁(1+d) − ΔCFₜ; R₀ = deposit + buying costs

**Variables and assumptions:** Terminal renter-minus-buyer wealth comparison. Negative interim balances imply funding at same discount rate; no borrowing constraint in valuation.

**Excel:**

> =IF(A7<='Inputs'!$B$13,('Inputs'!B7*('Inputs'!B8+'Inputs'!B10))*(1+'Inputs'!$B$14)-J7,0)


### Results: B7

**Mathematical equivalent:** Results.B7 = 'Inputs'!B7×(1-'Inputs'!B8)

**Variables and assumptions:** Deposit excludes buying costs.

**Excel:**

> ='Inputs'!B7*(1-'Inputs'!B8)


### Results: B8

**Mathematical equivalent:** Results.B8 = 'Inputs'!B7×('Inputs'!B8+'Inputs'!B10)

**Variables and assumptions:** Deposit plus purchase costs; emergency reserve additional.

**Excel:**

> ='Inputs'!B7*('Inputs'!B8+'Inputs'!B10)


### Results: B9

**Mathematical equivalent:** Results.B9 = 'Amortization'!E7

**Variables and assumptions:** Constant-rate base case; later resets recalculate.

**Excel:**

> ='Amortization'!E7


### Results: B10

**Mathematical equivalent:** Results.B10 = 'Amortization'!K7

**Variables and assumptions:** Cash benefit assumes timely claim through payroll.

**Excel:**

> ='Amortization'!K7


### Results: B11

**Mathematical equivalent:** Results.B11 = 'Inputs'!B7×'Annual assumptions'!E7÷12

**Variables and assumptions:** Maintenance and other ownership allowance.

**Excel:**

> ='Inputs'!B7*'Annual assumptions'!E7/12


### Results: B12

**Mathematical equivalent:** Results.B12 = 'Inputs'!B17-'Inputs'!B18-B9-B11+B10

**Variables and assumptions:** After housing, tax saving and other essentials.

**Excel:**

> ='Inputs'!B17-'Inputs'!B18-B9-B11+B10


### Results: B13

**Mathematical equivalent:** Results.B13 = sum('Rent versus buy'!L7:L36)-B8

**Variables and assumptions:** Positive favours buying under specified assumptions.

**Excel:**

> =SUM('Rent versus buy'!L7:L36)-B8


### Results: B14

**Mathematical equivalent:** Results.B14 = INDEX('Rent versus buy'!M7:M36,'Inputs'!B13)

**Variables and assumptions:** Negative favours buying.

**Excel:**

> =INDEX('Rent versus buy'!M7:M36,'Inputs'!B13)


### Results: B15

**Mathematical equivalent:** Results.B15 = B13+B14÷(1+'Inputs'!B14)^'Inputs'!B13

**Variables and assumptions:** Must equal zero within floating point tolerance.

**Excel:**

> =B13+B14/(1+'Inputs'!B14)^'Inputs'!B13


### Results: B16

**Mathematical equivalent:** Results.B16 = sum('Amortization'!F7:F366)

**Variables and assumptions:** Whole contractual term, may exceed comparison horizon.

**Excel:**

> =SUM('Amortization'!F7:F366)


### Results: B17

**Mathematical equivalent:** Results.B17 = 'Amortization'!I366

**Variables and assumptions:** Zero for valid term up to 360 months.

**Excel:**

> ='Amortization'!I366


### Results: B18

**Mathematical equivalent:** Results.B18 = MAX('Amortization'!L7:L366)

**Variables and assumptions:** Must equal zero.

**Excel:**

> =MAX('Amortization'!L7:L366)


### Rate and income stress: C7

**Mathematical equivalent:** M(r) = L(r/12) / [1 − (1+r/12)^(−n)]

**Variables and assumptions:** Immediate repricing of initial loan, not a later-year reset scenario.

**Excel:**

> =IF(A7=0,'Results'!$B$7/'Inputs'!$B$9,'Results'!$B$7*(A7/12)/(1-(1+A7/12)^(-'Inputs'!$B$9)))


### Rate and income stress: D7

**Mathematical equivalent:** Tax saving = exact PAYE difference at unchanged income; zero in income-loss stresses

**Variables and assumptions:** Conservative stress: cash income falls by chosen fraction and tax relief is not assumed usable during disruption. Not a recalculated gross-pay payslip.

**Excel:**

> =IF(B7=0,MAX(0,'Policy'!$F$7*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$7),'Policy'!$E$7)+'Policy'!$F$8*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$8),'Policy'!$E$8)+'Policy'!$F$9*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$9),'Policy'!$E$9)+'Policy'!$F$10*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$10),'Policy'!$E$10)+'Policy'!$F$11*MIN(MAX(0,('Inputs'!$B$15)-'Policy'!$D$11),'Policy'!$E$11)-'Inputs'!$B$16)-MAX(0,'Policy'!$F$7*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-MIN('Results'!$B$7*A7/12,'Policy'!$B$15)))-'Policy'!$D$7),'Policy'!$E$7)+'Policy'!$F$8*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-MIN('Results'!$B$7*A7/12,'Policy'!$B$15)))-'Policy'!$D$8),'Policy'!$E$8)+'Policy'!$F$9*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-MIN('Results'!$B$7*A7/12,'Policy'!$B$15)))-'Policy'!$D$9),'Policy'!$E$9)+'Policy'!$F$10*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-MIN('Results'!$B$7*A7/12,'Policy'!$B$15)))-'Policy'!$D$10),'Policy'!$E$10)+'Policy'!$F$11*MIN(MAX(0,(MAX(0,'Inputs'!$B$15-MIN('Results'!$B$7*A7/12,'Policy'!$B$15)))-'Policy'!$D$11),'Policy'!$E$11)-'Inputs'!$B$16),0)


### Rate and income stress: G7

**Mathematical equivalent:** Surplus = available cash × (1−loss) − debt payment + tax saving − ownership − essentials

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> ='Inputs'!$B$17*(1-B7)-C7+D7-E7-F7


### Rate and income stress: H7

**Mathematical equivalent:** Runway = reserve / monthly deficit, only when deficit > 0

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =IF(G7<0,'Inputs'!$B$19/(-G7),"No deficit")


### Discount sensitivity: B7

**Mathematical equivalent:** NPV(d) = −initial cash + Σ ΔCFₜ/(1+d)^t

**Variables and assumptions:** Only discount rate changes. Annual cash flows already include sale at chosen horizon and zero thereafter.

**Excel:**

> =NPV(A7,'Rent versus buy'!J7:J36)-'Results'!$B$8


### Discount sensitivity: C7

**Mathematical equivalent:** Chart label = percentage representation of the discount rate

**Variables and assumptions:** All amounts KES; see Inputs and sheet headers for timing.

**Excel:**

> =TEXT(A7,"0%")


### Policy: D8:E11

**Mathematical equivalent:** Monthly lower bound bⱼ = bⱼ₋₁ + widthⱼ₋₁; widths link to B7:B10

**Variables and assumptions:** Tax rates and annual schedule are versioned policy values. Keep annual and monthly schedules coherent when updating legislation.

**Excel:**

> =D7+E7
