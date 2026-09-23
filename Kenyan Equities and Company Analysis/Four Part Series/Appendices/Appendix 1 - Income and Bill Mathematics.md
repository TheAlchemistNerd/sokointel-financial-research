# Appendix 1 ; Income, Treasury-bill pricing, and screening

Research cutoff: 7 September 2026. Currency: Kenyan shillings unless indicated. Formula dictionaries at the end of this appendix map the workbook's calculation families to mathematical equivalents. The accompanying formula-audit CSV records every implemented formula and cell.

## A1.1 Dividend yield and purchase outlay

Article equation (1.1):

\[
Gross ordinary yield y = D / P
\]

| Symbol | Definition | Unit |
| --- | --- | --- |
| D | Ordinary distribution per share for the identified period | KES/share |
| S | Special distribution per share, separately identified | KES/share |
| P | Entry price, with timestamp | KES/share |
| t | Investor's applicable dividend withholding fraction | Decimal fraction |
| c | All-in acquisition cost as a fraction of traded value | Decimal fraction |
| q | Shares acquired | Whole shares |

KCB dated example: ordinary dividend \(D = 4\) and 11 September 2026 NSE VWAP \(P = 94\). Thus \(y = 4 / 94 = 0.042553\), or **4.26%**. The KES 3 special distribution is recorded separately rather than treated as recurring income.

Article equation (1.2):

\[
Net yield on acquisition outlay = D(1 - t) / [P(1 + c)]
\]
\[
Net dividend = 3 \times (1 - 0.05) = 2.85
\]
\[
Outlay per share = 40 \times 1.02 = 40.80
\]
\[
Net yield = 2.85 \div 40.80 = **6.9853%**
\]

For nonlinear brokerage costs, replace cP with the actual fee function, including a minimum commission where applicable. The model's proportional cost is an illustrative input, not a published fee tariff.

The KCB FY2025 example uses ordinary D = 4 and special S = 3, from the issuer's dividend schedule. At illustrative P = 65:

\[
Ordinary yield = 4 / 65 = **6.1538%**
\]
\[
All-distribution yield = (4 + 3) / 65 = **10.7692%**
\]

The forward ordinary-dividend assumption should be set separately after reviewing current earnings and policy. A fiscal-year total, trailing cash paid, approved dividend, and forecast dividend are separate data concepts.

## A1.2 Total return and taxes

Article equation (1.3), assuming a sale at the end of the period:

\[
R = [P_{1}(1 - cₛ) + (D + S)(1 - t) - P_{0}(1 + cᵦ)] / [P_{0}(1 + cᵦ)]
\]

Here cᵦ and cₛ are acquisition and disposal cost fractions; P_0 and P_1 are opening and exit prices. Dividends are received in cash without intermediate reinvestment in this example. Qualifying exchange-traded capital gains are assumed exempt for the specified listed-equity transaction. Off-market transfers and business-income classification require their own tax analysis.

\[
P_{0} = 40; P_{1} = 44; D = 3; S = 0; cᵦ = cₛ = 0.02; t = 0.05
\]
\[
Net sale = 44 \times 0.98 = 43.12
\]
\[
Gain = 43.12 + 2.85 - 40.80 = 5.17
\]
\[
R = 5.17 / 40.80 = **12.6716%**
\]

If P_1 = 32, net sale = 31.36, gain = 31.36 + 2.85 minus 40.80 = -6.59, and R = **-16.1520%**.

## A1.3 Payout and dividend stress

\[
Ordinary payout = D / EPS, for EPS > 0
\]
\[
Stressed ordinary dividend = D \times (1 - cut)
\]
\[
Stressed income yield = original net yield \times (1 - cut)
\]

BAT's FY2025 announced D = 70 and reported EPS = 52.46 give 70 / 52.46 = **133.4350%**. This is a reported-year comparison, not a forecast of the next payment. Review reserves, ordinary cash generation, capital commitments, and the issuer's stated distribution policy before selecting a forward assumption.

If earnings are zero, negative, or absent, the workbook leaves the payout ratio uncalculated and requests an earnings review. Missing dividends are distinct from a confirmed zero distribution. Screening thresholds are editable research preferences; the screen's result is separate from trading eligibility, valuation, and position sizing.

## A1.4 Treasury-bill pricing and tax settlement

Define face F, annual accepted simple yield y, actual tenor d days, pricing year B = 365, and withholding fraction t = 0.15 in the teaching case. The dated CBK auction prices reconcile to:

\[
Clean price P = F / (1 + yd/B)
\]
\[
Gross discount I = F - P
\]
\[
Withholding T = tI
\]
\[
Settlement outlay S = P + T
\]
\[
Maturity receipt = F
\]
\[
Net gain G = F - S = I(1 - t)
\]

This expands article equation (1.4). CBK's financial-markets worked example confirms the tax-inclusive settlement convention. The bill is not modelled as paying a separate coupon; tax is included in the initial cash requirement and face is received at maturity.

For the 91-day rate accepted in the auction dated 7 September 2026:

\[
yd/365 = 0.087687 \times 91 / 365 = 0.02186169041
\]
\[
P = 100,000 / 1.02186169041 = **97,860.60182**
\]
\[
I = 100,000 - 97,860.60182 = **2,139.39818**
\]
\[
T = 2,139.39818 \times 0.15 = **320.90973**
\]
\[
S = 97,860.60182 + 320.90973 = **98,181.51155**
\]
\[
G = 100,000 - 98,181.51155 = **1,818.48845**
\]

The published price per KES 100 is 97.8606. The computed value is 97.86060182; the residual is consistent with rounding. The 182-day and 364-day calculations are performed separately using their actual accepted rates and days.

| Tenor | Accepted annual yield | Clean price for face100,000 | Settlement including tax | Net gain | Holding return |
| --- | ---: | ---: | ---: | ---: | ---: |
| 91 days | 8.7687% | 97,860.60 | 98,181.51 | 1,818.49 | 1.8522% |
| 182 days | 8.9331% | 95,735.64 | 96,375.29 | 3,624.71 | 3.7610% |
| 364 days | 9.0737% | 91,702.03 | 92,946.73 | 7,053.27 | 7.5885% |

## A1.5 Annualisation, rollover, and face increments

\[
Holding-period return h = F/S - 1
\]
\[
Effective annual equivalent a = (F/S)^(365/d) - 1
\]
\[
Simple annualised cash return = h \times 365/d
\]

The effective annual equivalent assumes continuous renewal at identical terms, including identical tax treatment. For the 91-day example, h = 0.0185216995 and a = **7.6388%**. It is a comparison convention. The actual gain on that security is KES 1,818.49 for the specified face.

For a changing-rate rollover, calculate the settlement fraction s_j for each cycle j. With available cash W_j and chosen face increment L:

\[
Face_j = floor[W_{j} / (s_{jL})] \times L
\]
\[
Residual_j = W_{j} - Face_js_j
\]
\[
W_{j}₊_1 = Face_j + Residual_j
\]

The workbook uses a hypothetical KES 1m opening balance, four91-day cycles, and annual yield assumptions8.7687%,8%,7%,6.5%. It assumes no settlement gap and zero interest on residual cash. An actual implementation should include non-invested days and use the allotment/payment instructions for the specific auction. The dated next-auction notice sets a KES 50,000 minimum noncompetitive face; the model's chosen KES 50,000 increment is a planning assumption to confirm against the issue instructions.

## A1.6 Inflation and nominal versus real wealth

Article equation (1.5):

\[
1 + r_{real} = (1 + r_{nominal}) / (1 + inflation)
\]
\[
With8% net nominal return and5% inflation: r_{real} = 1.08/1.05 - 1 = **2.8571%**
\]

For varying inflation rates, use the product of annual factors rather than multiplying the last observed inflation rate by the number of years. Goal-specific cost growth can be substituted where a general inflation assumption does not represent the intended expenditure.

## A1.7 How to extend the issuer screen

Populate an actual price and timestamp, fiscal-period dividends, special payments, attributable earnings, source URL, and trading status. Add separate observation dates for financial statements and market inputs. Review splits, bonus issues, rights issues, and other changes to the share basis. Use the sector worksheets in workbook02 for financial quality before moving a candidate to a portfolio.

The issuer directory is a deduplicated snapshot of 68 entries on the NSE directory page. It includes operating companies, funds, REITs, and legacy entries. All entries need current trading-status confirmation. Seven dividend examples are populated; unverified financial fields remain blank. This provides a broad research structure without converting unavailable data into assumed company results.

## Workbook formula dictionary

### Dictionary entries

Each entry defines a formula family. Copied years, issuers, and simulation paths follow the same relationship. The [cell-by-cell formula audit](<C:/Users/Nevo/Downloads/financial material/Kenyan Equities and Company Analysis/Four Part Series/Research/01-Screening-and-Income-formula-audit.csv>) provides every exact Excel expression. Input units and modelling conventions appear in each workbook’s Guide and Inputs sheets.

#### Market screen: I7 ; Ordinary dividend yield

Mathematical equivalence: `y = D / P`

Units and scope: Sector analysis and trading eligibility remain separate.

```excel
=IF(OR(C7="",D7="",C7<=0),"",D7/C7)
```

#### Market screen: J7 ; After-tax ordinary yield on acquisition outlay

Mathematical equivalence: `y_net = D(1-t) / [P(1+c)]`

Units and scope: Sector analysis and trading eligibility remain separate.

```excel
=IF(I7="","",I7*(1-'Inputs'!$B$7)/(1+'Inputs'!$B$9))
```

#### Market screen: K7 ; Gross declared distributions yield

Mathematical equivalence: `y_all = (ordinary + special) / P`

Units and scope: Sector analysis and trading eligibility remain separate.

```excel
=IF(OR(I7="",E7=""),"",(D7+E7)/C7)
```

#### Market screen: L7 ; Ordinary payout; blank when earnings nonpositive or absent

Mathematical equivalence: `payout = D / EPS`

Units and scope: Sector analysis and trading eligibility remain separate.

```excel
=IF(OR(D7="",F7="",F7<=0),"",D7/F7)
```

#### Market screen: M7 ; Dividend cut sensitivity

Mathematical equivalence: `y_stress = y_net (1-cut)`

Units and scope: Sector analysis and trading eligibility remain separate.

```excel
=IF(J7="","",J7*(1-'Inputs'!$B$15))
```

#### Market screen: N7 ; Editable filter outcome; not an investment instruction

Mathematical equivalence: `screen = yieldgethreshold AND payoutlethreshold`

Units and scope: Sector analysis and trading eligibility remain separate.

```excel
=IF(J7="","Needs dividend and price",IF(L7="","Needs earnings review",IF(AND(J7>='Inputs'!$B$10,L7<='Inputs'!$B$11),"Meets income filters","Review yield or payout")))
```

#### Bill pricing: D7 ; Clean bill price

Mathematical equivalence: `P=F/(1+yd/365)`

Units and scope: KES except returns; residual can reflect published rounding.

```excel
=C7/(1+B7*A7/'Inputs'!$B$12)
```

#### Bill pricing: E7 ; Gross discount

Mathematical equivalence: `I=F-P`

Units and scope: KES except returns; residual can reflect published rounding.

```excel
=C7-D7
```

#### Bill pricing: F7 ; Withholding added at purchase

Mathematical equivalence: `T=tI`

Units and scope: KES except returns; residual can reflect published rounding.

```excel
=E7*'Inputs'!$B$8
```

#### Bill pricing: G7 ; Settlement cash

Mathematical equivalence: `S=P+T`

Units and scope: KES except returns; residual can reflect published rounding.

```excel
=D7+F7
```

#### Bill pricing: H7 ; Net gain

Mathematical equivalence: `G=F-S`

Units and scope: KES except returns; residual can reflect published rounding.

```excel
=C7-G7
```

#### Bill pricing: I7 ; Return on settlement outlay

Mathematical equivalence: `h=G/S`

Units and scope: KES except returns; residual can reflect published rounding.

```excel
=H7/G7
```

#### Bill pricing: J7 ; Effective annualised return

Mathematical equivalence: `a=(F/S)^(365/d)-1`

Units and scope: KES except returns; residual can reflect published rounding.

```excel
=(C7/G7)^('Inputs'!$B$12/A7)-1
```

#### Bill pricing: L7 ; Published clean-price reconciliation

Mathematical equivalence: `residual=100P/F-published price`

Units and scope: KES except returns; residual can reflect published rounding.

```excel
=D7/C7*100-K7
```

#### Rollover: D7 ; Opening funds

Mathematical equivalence: `W_open=W_prior; initial capital=KES1m`

Units and scope: KES

```excel
=1000000
```

#### Rollover: E7 ; Settlement per face unit

Mathematical equivalence: `s=p+(1-p)t`

Units and scope: KES; reinvestment yield editable each cycle.

```excel
=(1/(1+C7*B7/365))+(1-1/(1+C7*B7/365))*'Inputs'!$B$8
```

#### Rollover: F7 ; Affordable face

Mathematical equivalence: `F=floor(W/s/increment)increment`

Units and scope: KES; reinvestment yield editable each cycle.

```excel
=INT(D7/E7/'Inputs'!$B$14)*'Inputs'!$B$14
```

#### Rollover: G7 ; Uninvested balance

Mathematical equivalence: `cash=W-Fs`

Units and scope: KES; reinvestment yield editable each cycle.

```excel
=D7-F7*E7
```

#### Rollover: H7 ; Face paid at maturity

Mathematical equivalence: `maturity=F`

Units and scope: KES; reinvestment yield editable each cycle.

```excel
=F7
```

#### Rollover: I7 ; Closing wealth

Mathematical equivalence: `W_next=cash+face`

Units and scope: KES; reinvestment yield editable each cycle.

```excel
=G7+H7
```

#### Income scenarios: G7 ; Recurring net yield

Mathematical equivalence: `D(1-t)/[P0(1+c)]`

Units and scope: Illustration; qualifying listed capital gains assumed exempt.

```excel
=C7*(1-E7)/(B7*(1+F7))
```

#### Income scenarios: H7 ; Cash distributions

Mathematical equivalence: `cash=(D+special)(1-t)`

Units and scope: Illustration; qualifying listed capital gains assumed exempt.

```excel
=(C7+D7)*(1-E7)
```

#### Income scenarios: J7 ; After-cost total return

Mathematical equivalence: `R=[P1(1-c)+cash-P0(1+c)]/[P0(1+c)]`

Units and scope: Illustration; qualifying listed capital gains assumed exempt.

```excel
=(I7*(1-F7)+H7-B7*(1+F7))/(B7*(1+F7))
```
