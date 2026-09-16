# Part 2: Choosing the Wrapper and Understanding the Full Cost

*US Markets and Portfolio Construction, unified nine-part series. Research edition: 15 September 2026.*

When preparing this material, the author returned to a familiar comparison: if two funds follow the same index, why would an investor buy the more expensive one? The answer depends on what the investor needs the fund to do. Holding a position for twenty years and trading an option around that position next month are different uses of capital.

Part 1 separated the market from the benchmark and the fund. This part examines the fund itself. We will distinguish ownership structures, explain how ETF prices relate to underlying assets, and put the expense ratio into a wider cost framework. That prepares us to choose a portfolio architecture without letting an attractive ticker determine the entire design.

## Three ways to hold an exposure

A direct shareholding makes the investor responsible for company selection and position size. A mutual fund pools investors' capital and ordinarily transacts at a calculated end-of-day net asset value. An ETF also pools capital, but its shares trade on an exchange during the trading session.

| Vehicle | How the investor transacts | Principal decision | Additional operational consideration |
|---|---|---|---|
| Individual stock | Exchange purchase or sale | Which business and valuation justify ownership? | Company risk, corporate actions and position size |
| Mutual fund | Subscription or redemption under fund rules | Does the mandate suit the desired exposure? | Cutoff times, fees and distribution policy |
| ETF | Exchange purchase or sale | Does the benchmark and wrapper suit the role? | Spread, premium or discount, order execution |
| Direct bond | Purchase of a specified debt claim | Can the issuer pay, and does maturity fit the liability? | Lot size, accrued interest and sale liquidity |
| Bond ETF | Exchange purchase of a changing bond portfolio | Does credit quality and duration fit the purpose? | Fund duration persists as holdings turn over |

An ETF's net asset value is:

\[ NAV=\frac{\text{assets}-\text{liabilities}}{\text{shares outstanding}}. \]

Its exchange price is determined by buyers and sellers. The two values are connected, but they are not the same observation. The SEC explains that ordinary investors trade ETF shares at market prices, while authorized participants transact with funds in larger creation units. [SEC ETF bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-24). A mutual fund's daily pricing can be entirely adequate for an investor who does not need intraday execution. The ETF format adds flexibility, while also placing an execution decision in the investor's hands. Flexibility has value only if it is used sensibly.

## Why the creation and redemption mechanism matters

An authorized participant can exchange an eligible basket of securities or cash for newly created ETF shares under the fund's procedures. Redemption reverses that process. If the ETF price departs sufficiently from the value of the underlying basket, the economics of creating or redeeming shares can encourage trading that narrows the difference. This mechanism links the exchange price to the assets. It does not guarantee a fixed spread or eliminate dislocations. The basket may itself be expensive to trade, markets may be operating on different hours, and authorized participants need compensation for risk and transaction costs. In-kind transactions can also reduce the need for the fund to sell appreciated holdings to meet redemptions. That is one reason many equity ETFs can be tax efficient at the fund level. Cash redemptions, portfolio turnover and the nature of the assets can change the outcome. An investor should not infer that every ETF distribution is tax free or that selling ETF shares cannot produce a taxable gain. The more useful conclusion is specific: inspect the fund's mandate, transaction process and distribution history. The word ETF describes a trading structure; it does not settle every economic or tax question.

## Legal structure can change without changing the benchmark

Invesco announced QQQ's conversion from a unit investment trust to an open-end fund in December 2025, alongside a reduction in total expenses from 0.20% to 0.18%. Its Nasdaq-100 objective remained in place. QQQM also follows that benchmark and has a stated 0.15% total expense ratio. QQQ and QQQM are separate funds, rather than share classes of one fund. [Invesco modernization announcement](https://www.invesco.com/qqq-etf/en/market-outlook/whats-new-about-qqq.html), [Invesco product table](https://www.invesco.com/us/en/solutions/innovation-suite.html). For the investor, the relevant decision is whether a difference in execution, option-market access, tax consequences of switching or broker availability justifies the recurring fee difference. A long-term holder might reasonably favour lower holding costs. An active derivatives user might value a different trading ecosystem. Neither use case determines the correct weight of Nasdaq-100 exposure in the portfolio. A ticker change also deserves careful treatment in data work. Research should identify the continuing fund by its legal and security identifiers, not assume a new ticker establishes a new investment history. Any historical series must document predecessor names, benchmark changes and corporate actions before its performance is compared.

## Four layers of cost



| Layer | What is measured | Frequency | Useful evidence |
|---|---|---|---|
| Fund operating expenses | Expenses paid from fund assets | Recurring | Prospectus and fee table |
| Implementation | Spread, commission and market impact | Each trade | Executed price, quote and broker schedule |
| Tracking | Difference between fund and benchmark return | Over the measurement period | Matching NAV and benchmark total-return series |
| Investor-specific friction | Tax, currency conversion, custody and transfers | Depends on account and activity | Statements, fee schedules and applicable rules |

Tracking difference already incorporates the fund's operating expenses in a reported net fund return. Deducting the expense ratio again from that net return would count the same cost twice. Tracking error is different from tracking difference. The former usually measures variability in the fund-minus-benchmark return; the latter measures the return gap itself. A fund can lag by a small, stable amount and have low tracking error. Another can occasionally outperform and occasionally underperform by larger amounts, with a smaller average gap but higher tracking error. Currency conversion can dominate a very small ETF fee saving. If an investor saves a few dollars a year on fund expenses but repeatedly incurs a large conversion spread on small transfers, the total implementation process deserves attention. The correct unit of analysis is the path from the investor's original currency to eventual spendable proceeds.

## A dated fee comparison

The following figures were checked on 12 September 2026. They are stated annual fund expenses, with the definitions retained from the source. Future values in the next table are calculations, not issuer forecasts.

| Fund | Exposure | Stated annual expense | Definition and source |
|---|---|---:|---|
| SPYM | S&P 500 | 0.02% | Gross, [State Street](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-portfolio-sp-500-etf-spym) |
| QQQM | Nasdaq-100 | 0.15% | Total, [Invesco](https://www.invesco.com/us/en/solutions/innovation-suite.html) |
| QQQ | Nasdaq-100 | 0.18% | Total, [Invesco](https://www.invesco.com/qqq-etf/en/market-outlook/whats-new-about-qqq.html) |
| AGG | US aggregate investment-grade bonds | 0.03% | Prospectus expense, [iShares](https://www.ishares.com/us/products/239458/ishares-core-total-us-bond-market-etf) |

The first three rows do not all represent the same equity universe. The bond row represents a different asset class. Comparing expenses is useful; treating a common assumed return as evidence that these exposures are interchangeable would go beyond what the comparison establishes. Other S&P 500 vehicles, including VOO, IVV and SPY, can enter the same due-diligence process. The decision should use each fund's current prospectus, the broker's actual access terms and the cost of changing an existing holding. A capital gain triggered by switching funds may exceed many years of a small expense saving.

## Turning a fee into a dollar amount

An expense ratio is paid from fund assets, not ordinarily sent as a separate annual invoice. At a constant account value \(V\), its annual dollar equivalent is \(Ve\). A 0.15% fee is approximately $15 on $10,000, $75 on $50,000 and $150 on $100,000. To isolate compounding, assume a $10,000 principal, an 8% effective annual gross return and constant expenses. The simplified annual model is:

\[ FV=P(1+r-e)^n. \]

| Fee used | Value after 10 years | Value after 20 years | Value after 30 years |
|---|---:|---:|---:|
| 0.02% | $21,549 | $46,437 | $100,069 |
| 0.15% | $21,291 | $45,332 | $96,517 |
| 0.18% | $21,232 | $45,080 | $95,715 |

*Calculation note: author calculations using the displayed equation and the fee observations above. Identical gross returns are imposed to isolate expenses; the table predicts no fund's return.*

Under these assumptions, the three-basis-point difference between 0.15% and 0.18% produces about $802 over thirty years on the original $10,000. Its scale rises with invested capital and changes with the assumed return. That is a useful number to compare with switching costs. The annual equation is a teaching convention. A daily expense-accrual model must use a daily return consistent with the chosen annual effective return. Dividing an effective annual return by 365 and compounding it daily silently changes the return assumption. A consistent daily gross rate is:

\[ r_d=(1+r)^{1/365}-1. \]

Actual fund expenses accrue under prospectus accounting, and realized tracking includes other effects. The workbook records the annual convention so a reader can reproduce the table without pretending it is a reconstruction of daily NAV.

## Contributions have their own timing

For an initial principal \(P\), a constant end-of-month contribution \(C\), \(m\) months and a monthly net return \(i\):

\[
FV=P(1+i)^m+C\frac{(1+i)^m-1}{i},
\qquad
i=(1+r-e)^{1/12}-1.
\]

When \(i=0\), the contribution term becomes \(Cm\). Beginning-of-month contributions receive one additional month of growth. The timing convention must be stated before two accumulation tables are compared. In Excel, the workbook converts the annual assumption to a monthly rate and grows each cash flow for the months it is invested. The mathematical relationship belongs here; the exact spreadsheet expressions and cell references are documented inside the workbook.

## An actual price is an observation with a date



| Fund | Observation | USD per share | Observation date | Appropriate use |
|---|---|---:|---|---|
| SPYM | Official closing price | $89.21 | 10 September 2026 | Historical order-size illustration |
| AGG | Official closing price | $95.98 | 11 September 2026 | Historical order-size illustration |
| SOXX | Official closing price | $527.07 | 11 September 2026 | Historical contract-size comparison |
| XSD | Official closing price | $490.47 | 10 September 2026 | Historical order-size illustration |

*Source note: issuer product-page market-price sections, retrieved 12 September 2026: [SPYM](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-portfolio-sp-500-etf-spym), [AGG](https://www.ishares.com/us/products/239458/ishares-core-total-us-bond-market-etf), [SOXX](https://www.ishares.com/us/products/239705/SOX), [XSD](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-semiconductor-etf-xsd). Dates differ explicitly; this is not a same-day performance comparison or a live quote.*

A lower price per share does not establish that a fund is cheaper relative to the assets it owns. It can affect whole-share order size or the capital tied to a standard option contract. Fractional-share availability can reduce the first constraint; it does not change a listed option contract's deliverable.

## A practical wrapper decision

Start with a specified exposure. Identify eligible funds and compare their index definitions, legal structure and fee definitions. Then examine execution for the actual intended order. Finally include the investor's tax position, conversion costs and custody arrangements.

| Intended use | Primary question | Evidence that could change the choice |
|---|---|---|
| Long-term accumulation | Which suitable wrapper minimizes recurring friction? | Fee change, tracking deterioration or broker charges |
| Large occasional trade | Can the order execute near underlying value? | Spread, depth and market impact |
| Repeated options activity | Does the required contract trade efficiently? | Strike-level quotes, volume, open interest and deliverable |
| Existing appreciated holding | Is switching worthwhile after tax and trading costs? | Tax lots and expected holding period |
| Cross-border account | Is the wrapper suitable for the investor's legal status? | Residence, treaty entitlement and estate exposure |

The next part uses these building blocks to define core, core-plus, core-satellite and other portfolio architectures. Those labels become useful when they state who may take which risks, and how much of the portfolio those decisions can affect.

## Technical companion

For an opening investment (P), regular contribution (C), net annual return (r-e), and (n) annual periods, the recurring-contribution model uses:

\[
FV_n = P(1+r-e)^n + C\frac{(1+r-e)^n-1}{r-e}.
\]

The [cost, compounding and withholding appendix](<Appendices/Appendix 01 - Cost Compounding and Withholding Mathematics.md>) develops the assumptions and cross-checks.
