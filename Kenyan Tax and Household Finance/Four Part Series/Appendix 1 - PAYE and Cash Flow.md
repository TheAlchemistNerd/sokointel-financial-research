# Appendix 1; PAYE, deductions and annual reconciliation

## Scope and conventions

This appendix expands Equations (1.1)–(1.3) in Part 1. The workbook models one resident employee active for all twelve months of 2026. The pension illustration uses employee contributions under section 22A to a registered occupational defined-contribution arrangement. Section 22B individual-fund rules, including NSSF and employer-contribution interactions, need separate treatment. PRMF, insurance and interest inputs are assumed qualifying. Benefits must be valued before entry. The monthly bands follow KRA’s published integer schedule; annual reconciliation uses the exact annual schedule. Calculations retain precision and display two decimals. The annual reconciliation covers ordinary income tax after separately classified net income and certified credits have been entered. It does not determine the income’s regime or calculate VAT, turnover tax, AHL on non-employment income, penalties, instalment deadlines or other obligations. Reclassification must happen before this model is used for an actual return.

## Symbol dictionary

| Symbol | Meaning | Units / constraint |
|---|---|---|
| G | Cash gross employment pay | KES/month |
| V | Already valued taxable non-cash benefits | KES/month; no cash receipt implied |
| E | NSSF pensionable earnings | KES/month |
| Eₜₐₓ | Pensionable income for the income-tax contribution test | KES/month; separate from NSSF assessment base |
| A, H | Employee AHL and SHIF cash contributions | KES/month; separate assessment bases |
| N | Employee NSSF | KES/month; employer match excluded |
| C | Actual private pension contribution | KES/month |
| P | Allowed aggregate employee pension deduction | KES/month, includes NSSF |
| Rₚ, R | Actual PRMF payment and allowed PRMF deduction | KES/month |
| Iₚ, I | Qualifying interest paid and allowed deduction | KES/month |
| U, Q | Qualifying insurance premium and potential credit | KES/month |
| T | Taxable employment pay | KES/month, floored at zero |
| B(T) | Tax before reliefs at taxable pay T | KES/month |
| L | PAYE after reliefs | KES/month, non-refundable floor zero |
| X | Other household cash spending | KES/month; exclude payments already subtracted |
| S | Household surplus | KES/month; may be negative |

## Policy schedule and deduction mechanics

| Monthly taxable slice | Width, KES | Rate |
|---|---:|---:|
| First 24,000 | 24,000 | 10% |
| Above 24,000 to 32,333 | 8,333 | 25% |
| Above 32,333 to 500,000 | 467,667 | 30% |
| Above 500,000 to 800,000 | 300,000 | 32.5% |
| Above 800,000 | Unbounded | 35% |

The tax function is a sum across slices, not a single rate applied to all pay:

> B(T) = Σⱼ rⱼ × min(max(T − bⱼ, 0), wⱼ)

Here rⱼ is the slice rate, bⱼ its lower bound and wⱼ its width. The `Policy` sheet stores coherent monthly and annual grids. Its last width of 1E100 is a numerical representation of an unbounded top slice, not a statutory cap.

> N = 6% × min(E, applicable upper earnings limit)  
> A = 1.5% × entered AHL assessment base  
> H = max(300, 2.75% × entered salaried SHIF base)  
> P = min(N + C, 30% × Eₜₐₓ, 30,000)  
> R = min(Rₚ, 15,000)  
> I = min(Iₚ, 30,000)  
> T = max(0, G + V − A − H − P − R − I)  
> Q = min(15% × U, 5,000)  
> L = max(0, B(T) − 2,400 − Q)

These are the employee illustration’s rules. The pension income test is not replaced by the monetary ceiling. Separate private accounts do not receive separate aggregate allowances. January uses the earlier NSSF ceiling; February onward uses the fourth-phase ceiling. For a worker below the lower earnings limit, the total employee contribution remains 6% of actual pensionable earnings, subject to the applicable scheme treatment. This workbook does not model opt-outs, contracted-out Tier II destinations, unpaid months or a separate employer pension tax calculation. Employer NSSF is excluded from employee spendable cash. Loan principal must appear in spending or a debt schedule, even though it is absent from the interest deduction.

## Equation (1.1): full February cash calculation

> N = 0.06 × 108,000 = 6,480  
> A = 0.015 × 150,000 = 2,250  
> H = 0.0275 × 150,000 = 4,125  
> P = min(6,480 + 10,000, 45,000, 30,000) = 16,480  
> R = min(3,000, 15,000) = 3,000  
> I = 0  
> Deductions = 2,250 + 4,125 + 16,480 + 3,000 = 25,855  
> T = 150,000 − 25,855 = 124,145

Manual application of the occupied bands:

> First slice: 24,000 × 10% = 2,400  
> Second slice: 8,333 × 25% = 2,083.25  
> Third slice: (124,145 − 32,333) × 30% = 91,812 × 30% = 27,543.60  
> B(T) = 2,400 + 2,083.25 + 27,543.60 = 32,026.85  
> Q = 5,000 × 15% = 750  
> PAYE = 32,026.85 − 2,400 − 750 = 28,876.85

The actual cash calculation subtracts payments, not merely deductible portions:

> Cash after commitments = G − N − A − H − L − C − Rₚ − U − Iₚ  
> = 150,000 − 6,480 − 2,250 − 4,125 − 28,876.85 − 10,000 − 3,000 − 5,000  
> = 90,268.15  
> S = 90,268.15 − 75,000 = **15,268.15**

Whether the premium or PRMF payment is withheld by payroll or transferred separately does not change this total after listed commitments. It can change the amount actually credited by the employer, so the workbook deliberately labels this output more broadly than banked net salary.

## Equation (1.2): January-to-February movement

> January NSSF = 72,000 × 6% = 4,320  
> Extra employee NSSF = 6,480 − 4,320 = 2,160  
> PAYE saving = 29,524.85 − 28,876.85 = 648  
> Change in cash = −2,160 + 648 = **−1,512**

The 30% shortcut works here because the entire additional deduction falls in the same 30% slice and no other limit binds. The general method remains a full before-and-after PAYE calculation.

## Equation (1.3): additional pension and the deduction ceiling

> Remaining February deduction headroom = 30,000 − 16,480 = 13,520  
> Extra contribution of 10,000: tax saved = 10,000 × 30% = 3,000  
> Net cash cost = 10,000 − 3,000 = **7,000**  
> Extra contribution of 20,000: extra deductible = min(20,000, 13,520) = 13,520  
> Tax saved = 13,520 × 30% = 4,056  
> Net cash cost = 20,000 − 4,056 = **15,944**

The `Pension sensitivity` sheet recalculates the tax function at each contribution. It does not assume 30% for every possible salary. The allowed contribution also depends on pensionable income, so lowering earnings can move the binding constraint away from the monetary ceiling.

## Annual reconciliation and rounding

The annual widths are 288,000; 100,000; 5,612,000; 3,600,000; and unbounded, with the same rates. The illustration assumes full-year resident personal relief and valid annual insurance premiums.

> Salary taxable = 126,305 + 11 × 124,145 = 1,491,900  
> Combined taxable = 1,491,900 + 240,000 = 1,731,900  
> Annual gross tax = 288,000 × 10% + 100,000 × 25% + (1,731,900 − 388,000) × 30%  
> = 28,800 + 25,000 + 403,170 = 456,970  
> Annual liability = 456,970 − 28,800 − 9,000 = 419,170  
> PAYE withheld = 29,524.85 + 11 × 28,876.85 = 347,170.20  
> Balance = 419,170 − 347,170.20 − 12,000 = **59,999.80**

For salary alone, annual liability is KES 347,170. The monthly schedule allocates KES 4 less annually to the 25% slice and KES 4 more to the 30% slice. Consequently, annualised monthly tax at this income is KES 0.20 above the exact annual result: 4 × (30% − 25%) = 0.20. With annual taxable salary Y, summing the occupied monthly bands gives 0.30Y − 62,599.80 before reliefs; the annual bands give 0.30Y − 62,600. Both use identical total reliefs here. The independently calculated difference should be retained as a small reconciliation item, not silently plugged. Different payroll rounding or income patterns can produce other differences.

## Workbook map and formula equivalence

| Modelling sheet | Main formula families | Mathematical equivalent |
|---|---|---|
| Payroll | Assessment bases, capped deductions, band tax, reliefs, cash | Equations above; surplus S = G − payments − X |
| Annual reconciliation | SUM, annual band tax, relief caps, credits | Tax on combined ordinary taxable income − valid reliefs − PAYE − certified credits |
| Pension sensitivity | Recompute P, T and PAYE for each extra contribution x | Saving(x) = L(0) − L(x); cash cost(x) = x − saving(x) |

The workbook’s `Formula dictionary` contains representative cell addresses, literal Excel expressions, mathematical equivalents and assumptions. `Monthly inputs`, `Inputs`, `Policy` and `Sources` supply values rather than hidden calculated answers. Policy changes require coherent updates to the versioned rule tables, not isolated edits to a formula.

## Evidence

IEEE references [2]–[9] in Part 1 support the statutory mechanics. The income-tax model is original analysis. The underlying statutory text can be verified through [Kenya Law’s Income Tax Act](https://new.kenyalaw.org/akn/ke/act/1973/16/eng%402025-07-01/source) and the [2024 amendment](https://www.kenyalaw.org/kl/fileadmin/pdfdownloads/Acts/2024/TheTaxLaws_Amendment_Act_No.12of2024.pdf), alongside the current KRA and NSSF notices linked in the article and workbook.
