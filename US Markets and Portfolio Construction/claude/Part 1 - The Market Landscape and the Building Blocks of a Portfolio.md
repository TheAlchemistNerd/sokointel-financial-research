# US Markets and Portfolio Construction
## Part 1 of 5: The Market Landscape and the Building Blocks of a Portfolio

Anyone assembling a portfolio out of US-listed securities is really making two decisions layered on top of each other, whether or not they notice it. The first is which slice of the market to own. The second is which legal wrapper to own it through. Both decisions carry costs, and both sets of costs compound quietly over years in ways that rarely show up in a single account statement. This five-part series works through both decisions in turn, and this opening part supplies the vocabulary and the arithmetic that the later, more strategic parts lean on.

The series moves from mechanics to strategy. Part 2 turns the building blocks introduced here into a deliberate core allocation, using the core, core-plus and core-satellite frameworks. Part 3 looks at satellite and thematic positions, with a semiconductor-sector case study. Part 4 develops the mathematics of risk and diversification, together with the tax rules that determine what an investor actually keeps. Part 5 closes with implementation: contribution scheduling, rebalancing, and a fully worked model portfolio. Because a meaningful share of the money in US-listed funds now originates outside the United States, this first part also covers what changes, mechanically, once an investor's tax residence sits outside the US border.

### What "the US market" actually means

There is no single object called "the US market." What exists instead is a set of indices, each built by a different rulebook, and each answering a slightly different question about what counts as representative. The S&P 500 is the most quoted of these. It is a float-adjusted, market-capitalization-weighted index of roughly 500 large US companies, where each constituent's weight is scaled by an Investable Weight Factor that reflects only the shares actually available for public trading, not a company's full share count [1]. A firm twice the size of another, by that float-adjusted measure, carries roughly twice the influence on the index's daily movement.

The Nasdaq-100 answers a different question. Its defining rule is not a size cutoff but an exclusion: financial companies are not eligible for inclusion at all, regardless of size, and constituents must be listed on the Nasdaq Global Select Market and meet minimum liquidity and public-float tests [3]. The index is then weighted by a modified market-capitalization method that caps the influence of any single mega-cap name, a mechanism specifically designed to stop one or two dominant companies from steering the whole benchmark. The practical result — a technology- and growth-heavy index — is a side effect of the financial-sector exclusion rule, not a deliberate sector bet by the index provider.

It is worth separating the Nasdaq-100 from "the Nasdaq" as a loose figure of speech, since the two get conflated constantly in casual conversation. Nasdaq is a stock exchange, home to several thousand listed companies across every sector, financial firms included. The Nasdaq Composite is a much broader index built from nearly all of those common-stock listings, financials and all, and so behaves quite differently from the curated, financial-sector-excluded Nasdaq-100. When an investor buys a fund tracking "the Nasdaq," it matters a great deal which of these two indices — the broad Composite or the curated 100 — actually sits underneath it, since the exclusion rule in the Nasdaq-100 is the entire reason it behaves like a growth-tilted benchmark rather than a full cross-section of Nasdaq-listed business.

The Dow Jones Industrial Average works differently again, and the difference matters more than its age might suggest. It is price-weighted, not capitalization-weighted: the value of the index is simply the sum of the 30 component share prices, divided by the Dow Divisor, a figure adjusted over time for stock splits and constituent changes so those events do not distort the index level on their own [2]. A $400 stock moves the Dow four times as much as a $100 stock, irrespective of which company is actually larger by total market value, and the 30 constituents themselves are chosen by a committee rather than by a fixed quantitative screen. An index built this way is not "wrong," but it measures something structurally different from the S&P 500 or the Nasdaq-100, and conflating the three is a common source of confused portfolio talk.

A fourth reference point worth knowing is the Russell family, maintained by FTSE Russell. The Russell 3000 is built to represent roughly 98% of investable US equity value, combining large-, mid- and small-cap names, while the Russell 2000 carves out the smallest roughly 2,000 constituents of that broader index as a small-cap benchmark, both weighted by float-adjusted market capitalization [4]. Where the S&P 500 and Nasdaq-100 are curated by inclusion committees applying qualitative and liquidity screens on top of quantitative rules, the Russell indices are closer to purely rules-based: a company that clears the size and eligibility bar at the annual reconstitution is in, full stop. Part 2 returns to these four families when it discusses which index best serves as the "core" of a portfolio.

### Three ways to buy the same exposure

Once an investor has chosen which slice of the market to target, there are three broad vehicles for buying it: individual stocks, mutual funds, and exchange-traded funds. A single stock gives direct, undiluted ownership of one company and its single-name risk. A mutual fund pools money from many investors into a portfolio managed toward a stated objective, priced once per trading day at net asset value (NAV), with purchases and redemptions settled directly with the fund company at that end-of-day price. An ETF is structurally a fund — it holds a basket of securities on behalf of many investors — but it trades on an exchange throughout the day like a stock, with a market price that can move independently of, though usually close to, its underlying NAV.

The choice of vehicle also interacts with the choice of account, a topic Part 4 develops in full. A taxable brokerage account can hold any of the three vehicles and exposes the holder to dividend and capital-gains taxation as it occurs; a tax-advantaged account such as an employer retirement plan or an individual retirement account shelters the same holdings from annual taxation but restricts withdrawals and, for a non-US person, may not even be available. Most brokers also let a shareholder enrol in a dividend reinvestment plan, automatically using cash distributions to buy additional fractional shares of the same holding at the next available price rather than depositing the cash — a mechanical convenience that compounds a position faster over time simply by removing the temptation, or the friction, of manually reinvesting small cash amounts.

That intraday tradability is not just a convenience feature; it is the source of costs that a mutual fund investor never has to think about, namely the bid-ask spread and the premium or discount to NAV. It also changes how the fund itself absorbs investor flows. A mutual fund experiencing heavy redemptions must generally raise cash by selling securities inside the fund, which can realize capital gains that get distributed to all remaining shareholders regardless of when they bought in. An ETF handles the equivalent situation through a different mechanism entirely, described next, and that mechanism is the main reason ETFs have become the default wrapper for building a US-market core position.

### How an ETF actually works: creation, redemption, and the tax-efficiency mechanism

ETF shares are not created or redeemed directly by ordinary investors. That role belongs to a small set of large institutions called Authorized Participants (APs), which alone are permitted to transact directly with the fund. When an AP wants to create new ETF shares, it assembles a basket of the underlying securities that mirrors the fund's holdings and delivers that basket to the fund in exchange for a large block of new ETF shares, known as a creation unit, which the AP can then sell to the public on the exchange. Redemption runs the same process in reverse: the AP delivers a creation unit's worth of ETF shares back to the fund and receives the underlying basket of securities in return, "in kind" rather than in cash [5].

This same creation-and-redemption loop is also what keeps an ETF's market price tethered to the value of what it actually holds. If an ETF's share price on the exchange drifts noticeably above its underlying NAV, an Authorized Participant can profit by assembling the cheaper underlying basket, exchanging it for new ETF shares at NAV, and selling those shares into the richer market price — an action that simultaneously increases ETF supply and pushes the market price back down toward NAV. The reverse trade runs when the ETF price drifts below NAV. It is this arbitrage incentive, repeated by multiple competing APs, that ordinarily keeps a large, liquid ETF's premium or discount to a few basis points, and it is also why an ETF's own trading volume is not the full liquidity picture: the liquidity of the underlying basket, which determines how cheaply an AP can assemble or unwind it, matters at least as much as how often the ETF shares themselves change hands on a given day.

This in-kind mechanism is the mechanical root of the ETF tax-efficiency advantage over mutual funds. Because redemptions are typically satisfied by handing over a basket of securities rather than by selling holdings for cash, a fund can direct its lowest-cost-basis, most-appreciated shares out through the redemption process without triggering a taxable sale inside the fund [5]. A mutual fund facing net outflows usually has no equivalent option; it must sell something, and that sale can generate a distributed capital gain even for shareholders who did not redeem a single share that year. This is a structural, not incidental, difference, and it is one reason a fund's legal wrapper deserves as much attention as its index.

### Open-end funds and Unit Investment Trusts: a live case study

Most US ETFs are organized as open-end funds under the Investment Company Act of 1940, giving the manager flexibility to use representative sampling, securities lending, and immediate reinvestment of dividends to track an index efficiently. A smaller, older category is organized instead as a Unit Investment Trust (UIT): a fixed, largely unmanaged basket that must replicate its index exactly, cannot lend out securities, and historically has had to hold dividends in cash until a scheduled distribution date rather than reinvesting them immediately — a small but persistent cash drag relative to an open-end fund tracking the same benchmark.

SPY, the original S&P 500 ETF, remains organized this way today; its own fund page lists ALPS Distributors, Inc. as distributor, the hallmark of the UIT structure that also governs its sibling funds MDY and DIA [6]. For a long time, QQQ sat in the same category, and a great deal of investor commentary — including material this series drew on while researching this article — describes QQQ as a UIT with the attendant cash-drag disadvantage relative to its open-end sibling, QQQM. That description is now out of date, and updating it is itself a useful illustration of why this series insists on checking primary sources rather than repeating older comparisons.

Effective after market close on December 19, 2025, following a shareholder vote, Invesco reclassified QQQ from a Unit Investment Trust into an open-end fund registered under the Investment Company Act of 1940 [7]. As part of the same restructuring, QQQ's total expense ratio fell from 0.20% to 0.18%. QQQ is consequently no longer subject to the UIT's dividend-reinvestment and securities-lending restrictions, and the older "QQQ is a UIT, QQQM is not" framing needs to be retired. What has not changed is that QQQM, launched in October 2020 specifically as a lower-cost, buy-and-hold-oriented share class tracking the identical Nasdaq-100 index, still carries the lower expense ratio of the two at 0.15% [8]. The gap between them today is a pure pricing decision by the issuer rather than a structural one: QQQ continues to serve a deep, highly liquid options market that institutional and active traders value, while QQQM is priced for investors who simply want to hold the same exposure at the lowest available cost.

The fee gap that remains between QQQ and QQQM, in other words, is not a leftover structural inefficiency waiting to be arbitraged away — it is a deliberate segmentation of the same underlying exposure into two products serving two different clienteles, and an investor who only ever intends to buy and hold the Nasdaq-100 has little reason to pay for options-market depth they will never use.

### The real cost of ownership

The expense ratio is the most visible cost of holding a fund, but it is not the only one. Three others matter in combination. The bid-ask spread is the gap between the price at which a buyer can purchase and a seller can sell an ETF at a given moment; it is a real, one-time cost paid on every trade, and it tends to matter most for large or frequent trades in less liquid funds. Tracking difference is the gap between what a fund actually returns to investors and what its benchmark index returns over the same period; it usually runs close to the expense ratio but can drift from it because of sampling choices, revenue the fund earns from lending out securities, or residual cash drag. The premium or discount to NAV measures how far an ETF's market price sits from the value of its underlying holdings at any moment; for the large, heavily traded funds discussed in this series it is typically a matter of a few basis points, but it can widen meaningfully in thinly traded or stressed markets.

Tracking difference deserves a concrete illustration, because it is easy to assume it is simply the expense ratio wearing a different label. Suppose an index returns exactly 10.00% over a year and a fund charging a 0.03% expense ratio returns 9.95% net to investors rather than the 9.97% a pure fee deduction would predict. The extra two-basis-point gap is tracking difference beyond the stated fee, and it can run in either direction: securities-lending income earned by the fund can partly offset the expense ratio and narrow the gap, while sampling error, cash drag, or the cost of trading around index reconstitutions can widen it. For the very large, plain-vanilla index funds discussed in this series, tracking difference is usually small and stable from year to year, but it is worth an occasional check against a fund's own reported figures rather than assumed away entirely.

Restricting attention to the expense ratio alone, four vehicles currently give an investor essentially the same S&P 500 exposure at four different prices: SPY at 0.0945% [6], VOO at 0.03% [9], IVV at 0.03% [10], and SPYM — renamed from SPLG on October 31, 2025 — at 0.02% [11]. Because all four track the same underlying index, the spread between them is close to a pure charge for legal structure, brand, and options-market depth rather than a difference in what is actually owned.

### Table 1 — What a fee difference costs in dollars

The table below carries a single illustrative $10,000 lump sum forward at an assumed gross annual return of 8% before fees — a simplifying, clearly labelled assumption used purely to isolate the effect of cost, not a return forecast — and compares outcomes across six expense-ratio levels using Equation (1.1):

FV = P × (1 + r − e)ⁿ  ...(1.1)

where P is the initial principal, r is the assumed gross annual return, e is the fund's expense ratio, and n is the number of years held. This annual approximation slightly understates the true daily-compounding cost, but the resulting error is a few dollars at these magnitudes and does not change the conclusion.

| Vehicle | Expense ratio | Value after 10y | Value after 20y | Value after 30y | 30y cost vs. cheapest |
|---|---|---|---|---|---|
| SPYM (S&P 500) | 0.02% | $21,549 | $46,437 | $100,069 | — |
| VOO / IVV (S&P 500) | 0.03% | $21,529 | $46,351 | $99,791 | $278 |
| SPY (S&P 500, UIT) | 0.0945% | $21,401 | $45,801 | $98,018 | $2,051 |
| QQQM (Nasdaq-100) | 0.15% | $21,291 | $45,332 | $96,517 | $3,552 |
| QQQ (Nasdaq-100) | 0.18% | $21,232 | $45,080 | $95,715 | $4,354 |
| Illustrative actively managed fund | 0.75% | $20,136 | $40,546 | $81,643 | $18,426 |

A roughly 0.16-percentage-point gap between the cheapest and most expensive S&P 500 vehicle compounds into a $2,051 difference on a single $10,000 investment held 30 years; the same arithmetic applied to a hypothetical 0.75% actively managed fund produces an $18,426 gap. None of these funds needs to outperform its benchmark for the cost difference to matter — it accrues automatically, every year, regardless of what the market does. Full derivations and a version of this table extended to monthly contribution schedules appear in Appendix 1.

### Access from outside the United States

A substantial share of the assets in US-listed ETFs is owned by investors whose tax residence is outside the United States, and two mechanical differences apply to them that a US-resident investor never encounters: dividend withholding and estate tax exposure.

Dividends paid by US companies and US-domiciled funds to a nonresident alien are subject to a statutory 30% US withholding tax at source, deducted before the dividend ever reaches the investor's account [12]. That rate can be reduced, but only if two conditions both hold: the investor's country of tax residence must have an active income tax treaty with the United States, and the investor must file a valid Form W-8BEN with their broker to claim the treaty rate rather than defaulting to the statutory one. As of the most recent Treasury update, the United States maintains active income tax treaties with 68 jurisdictions [13]. Coverage is not universal, however, and several countries with large diaspora populations — Kenya among them — currently have no comprehensive US income tax treaty in force, leaving investors resident there subject to the full 30% statutory rate with no treaty rate available to claim [14].

Form W-8BEN itself is a certification, not a tax payment: it tells the broker or fund custodian which country the investor is a tax resident of, so that the correct withholding rate — treaty-reduced or the 30% statutory default — is applied automatically at the point dividends are paid, rather than being fixed up later through a refund claim. Brokers generally require the form to be recertified every three years, and a lapsed or missing certification typically causes the custodian to default to the full statutory rate until a valid form is back on file, regardless of whether a treaty would otherwise have applied. For an investor whose country of residence has no treaty at all, the form still matters — it is what establishes non-US tax residency in the first place — even though there is no reduced rate for it to unlock.

### Table 2 — Withholding with and without a treaty

Using an illustrative $10,000 position yielding 1.3% annually — a broadly representative, clearly assumed yield for a diversified US equity ETF, not a forecast — Equation (1.2) shows the mechanism:

Net dividend = Gross dividend × (1 − withholding rate)  ...(1.2)

| Scenario | Gross annual dividend | Withholding rate | Tax withheld | Net received |
|---|---|---|---|---|
| No treaty (e.g., Kenya-resident investor) | $130.00 | 30% | $39.00 | $91.00 |
| Illustrative treaty country | $130.00 | 15% | $19.50 | $110.50 |

The $19.50 annual gap in this small illustration scales linearly with position size and is a permanent, recurring cost for as long as the position and the residency are unchanged — it is not a one-time filing inconvenience.

Estate tax exposure is a separate and, in relative terms, potentially larger risk, because it applies once, to the full value of a position, rather than annually to income. US-situs assets owned by a nonresident alien at death — including stock of US corporations, regardless of where the brokerage account or share certificates happen to be held — are subject to US estate tax, with a statutory exemption equivalent of $60,000 before the tax applies, at rates that can reach 40% on the excess, and a Form 706-NA filing obligation once US-situs gross assets meet or exceed that threshold [15]. A US-situs portfolio of $150,000 held by a nonresident alien at death, for instance, leaves $90,000 exposed to tax after the exemption, purely because the underlying stock is legally domestic to the United States.

### Table 3 — When the NRA estate-tax filing threshold is triggered

| US-situs estate value | Taxable base after $60,000 exemption | Form 706-NA required |
|---|---|---|
| $50,000 | $0 | No |
| $60,000 | $0 | Yes |
| $150,000 | $90,000 | Yes |
| $500,000 | $440,000 | Yes |

These two mechanisms — withholding on income and estate tax on the position itself — are the main reason some non-US investors deliberately route their US-market exposure through an intermediate structure, such as an Ireland-domiciled fund holding US equities, rather than buying US-listed ETFs directly, since a different domicile can change which country's withholding and estate-tax rules apply to the position. That structural choice, and its trade-offs, is covered in full in the companion International Investing and Diaspora Finance series rather than repeated here; this article's purpose is only to make clear that the choice of listing venue is not a cosmetic detail.

Two brief practical notes belong alongside these numbers rather than as an afterthought. First, none of the figures above are personalized tax guidance; actual withholding and estate-tax outcomes depend on the investor's specific country of residence, any treaty in force, the broker's own certification procedures, and the composition of the estate at the relevant date, and a qualified cross-border tax adviser is the appropriate source for an individual determination. Second, the exercise of working through Tables 2 and 3 is itself the more durable takeaway: an investor who can reconstruct the 30%-versus-treaty-rate arithmetic and the $60,000 estate-tax threshold from first principles is far better placed to notice when either figure changes — treaty tables and exemption amounts are periodically revised — than one who only remembers a single cited number from a single point in time. The QQQ reclassification discussed earlier is a reminder that even seemingly stable structural facts about a specific fund can change with a single shareholder vote; the tax thresholds governing cross-border ownership are no more permanent, and are worth rechecking against the primary sources cited here rather than assumed to hold indefinitely.

### Where this leaves the series

Everything in this part — the index families, the vehicle types, the legal structures, the layered cost stack, and the cross-border tax mechanics — functions as the fixed rules of the game rather than a strategy in itself. None of it tells an investor how much to hold in any one fund, how to combine a broad core with more targeted positions, or when to rebalance. Part 2 takes up exactly that question, building a deliberate core allocation out of the vehicles introduced here and formalizing the core, core-plus and core-satellite frameworks with a fully worked portfolio example. Appendix 1, attached to this part, contains the complete formula derivations, the worksheet used to check every figure in Tables 1 through 3, and a reproducibility note so a reader can verify each number independently rather than take the arithmetic on faith.

---

## References

[1] S&P Dow Jones Indices, "S&P U.S. Indices Methodology." [Online]. Available: https://www.spglobal.com/spdji/en/documents/methodologies/methodology-sp-us-indices.pdf. Accessed: Sep. 11, 2026.

[2] S&P Dow Jones Indices, "Dow Jones Averages Methodology." [Online]. Available: https://www.spglobal.com/spdji/en/documents/methodologies/methodology-dj-averages.pdf. Accessed: Sep. 11, 2026.

[3] Nasdaq, Inc., "Nasdaq-100 Index Methodology." [Online]. Available: https://indexes.nasdaqomx.com/docs/Methodology_NDX.pdf. Accessed: Sep. 11, 2026.

[4] London Stock Exchange Group / FTSE Russell, "Russell 2000 Index." [Online]. Available: https://www.lseg.com/en/ftse-russell/indices/russell-2000-index. Accessed: Sep. 11, 2026.

[5] U.S. Securities and Exchange Commission, "Updated Investor Bulletin: Exchange-Traded Funds (ETFs)." [Online]. Available: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-24. Accessed: Sep. 11, 2026.

[6] State Street Global Advisors, "SPY: SPDR S&P 500 ETF Trust — Fund Information." [Online]. Available: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-500-etf-trust-spy. Accessed: Sep. 11, 2026.

[7] Invesco, "QQQ Prospectus Supplement: Reclassification from Unit Investment Trust to Open-End Fund," effective Dec. 19, 2025. [Online]. Available: https://www.invesco.com. Accessed: Sep. 11, 2026.

[8] Invesco, "Invesco NASDAQ 100 ETF (QQQM) Fact Sheet." [Online]. Available: https://www.invesco.com. Accessed: Sep. 11, 2026.

[9] Vanguard, "Vanguard S&P 500 ETF (VOO) Fund Fact Sheet." [Online]. Available: https://fund-docs.vanguard.com/F0968.pdf. Accessed: Sep. 11, 2026.

[10] BlackRock, "iShares Core S&P 500 ETF (IVV) Fund Fact Sheet." [Online]. Available: https://www.ishares.com/us/literature/fact-sheet/ivv-ishares-core-s-p-500-etf-fund-fact-sheet-en-us.pdf. Accessed: Sep. 11, 2026.

[11] State Street Global Advisors, "SPYM: SPDR Portfolio S&P 500 ETF — Fund Information." [Online]. Available: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-500-etf-spym. Accessed: Sep. 11, 2026.

[12] Internal Revenue Service, "Publication 515: Withholding of Tax on Nonresident Aliens and Foreign Entities." [Online]. Available: https://www.irs.gov/publications/p515. Accessed: Sep. 11, 2026.

[13] Internal Revenue Service, "United States Income Tax Treaties — A to Z." [Online]. Available: https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z. Accessed: Sep. 11, 2026.

[14] Clemta, "US Tax Treaty Countries: Full List and Who Qualifies." [Online]. Available: https://clemta.com/blog/us-tax-treaty-countries-list. Accessed: Sep. 11, 2026.

[15] Internal Revenue Service, "SOI Tax Stats — International: Nonresident Alien Estate Tax Filing Requirements." [Online]. Available: https://www.irs.gov/node/10081. Accessed: Sep. 11, 2026.

*Companion appendix: Appendix 1 — Cost, Compounding and Withholding Mathematics.*
