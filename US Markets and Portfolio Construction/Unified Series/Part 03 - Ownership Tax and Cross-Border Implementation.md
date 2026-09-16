# Part 3: Ownership, Tax and Cross-Border Implementation

*US Markets and Portfolio Construction, unified nine-part series. Research edition: 15 September 2026.*

At the beginning of this research, a practical question appeared repeatedly: if two people buy exposure to the same American companies, why can their after-tax outcome, administrative burden, and estate exposure differ so much? The answer is not the ticker alone. It lies in the chain from the company to the fund, the fund to the investor, the investor's residence, and the account through which the holding is owned.

This chapter gives that chain a structure. It is an educational framework, not personal tax advice. Cross-border rules depend on residence, citizenship, domicile, family circumstances, account registration and treaty eligibility. Confirm the current position with the relevant revenue authority and a qualified adviser before acting.

## Start with the investor's legal and economic facts

A brokerage account often displays a trading currency, a fund ticker and a current market value. None of those fields, alone, identify the investor's tax position. A sound record starts with five facts:

| Question | Why it matters | Record to keep |
| --- | --- | --- |
| Where is the investor tax resident? | Residence can determine reporting and personal tax treatment. | Residence evidence and annual tax filing position. |
| Is the investor a US person for tax purposes? | US-person rules are distinct from non-US investor rules. | Current W-9 or equivalent status evidence. |
| What is the fund's domicile and legal structure? | Domicile can affect withholding inside the fund and estate exposure. | Prospectus, factsheet and ISIN. |
| Which account legally owns the asset? | An individual, pension, company and trust can have different rules. | Account agreement and beneficial-owner record. |
| In which currencies are future expenses due? | Currency changes the household value of the result. | Cash-flow plan, reserve currency and reporting currency. |

The first distinction is between a company dividend and the cash an investor sees. An American company may pay a dividend to a fund. Withholding can occur before the fund receives it. The fund may retain the income in an accumulating share class or distribute it. A second jurisdiction may then tax the investor. Calling a fund "tax efficient" without identifying the stage being discussed is incomplete.

## The fund domicile is not the exchange listing

The same economic exposure can appear under more than one ticker. A fund may be domiciled in Ireland, listed in London, trade in dollars or sterling, and hold American securities. The exchange and trading currency help determine execution and conversion mechanics. The domicile identifies the fund's legal home. The ISIN is therefore more useful than a short ticker when comparing apparently similar listings.For a non-US investor, an Irish UCITS fund and a US-domiciled ETF can both offer broad American equity exposure, yet they sit in different legal and withholding chains. That does not make either route universally preferable. The comparison must include the investor's residence, platform access, dealing costs, reporting needs, dividend policy and the intended account size.

## Make withholding a flow, not a slogan

Consider an illustrative $100,000 investment in comparable US equity exposure with a 1.5% gross dividend yield. Assume, solely to show the arithmetic, that one route suffers 30% withholding at the dividend stage and another suffers 15%, while annual fund charges are 0.03% and 0.07% respectively.

| Item | Route A: 30% withholding, 0.03% fee | Route B: 15% withholding, 0.07% fee |
| --- | ---: | ---: |
| Gross dividend | $1,500 | $1,500 |
| Illustrative withholding | $450 | $225 |
| Annual fund charge on starting value | $30 | $70 |
| Simplified annual structural drag | $480 | $295 |

\[\text{Approximate drag} = V\left(y \times w + f\right)\]

Here, \(V\) is portfolio value, \(y\) is gross dividend yield, \(w\) is the withholding rate and \(f\) is the annual fund charge. The comparison excludes personal tax, trading, foreign-exchange cost, tracking difference and the timing of distributions. It does not forecast realised fund returns.The most useful feature of the calculation is its break-even logic. If Route B costs four basis points more each year but reduces the illustrative withholding rate by fifteen percentage points, the gross dividend yield at which that difference offsets the extra fee is:

\[y_{\text{break-even}} = \frac{0.0007 - 0.0003}{0.30 - 0.15} \approx 0.2667\%\]

A result is only as useful as its inputs. A different treaty entitlement, dividend yield, account size or dealing cost can change it. The disciplined action is to keep the assumptions visible and update them when the investor's position changes.

## Estate exposure is a separate question

Income-tax withholding and estate exposure are not the same issue. The US Internal Revenue Service describes a filing threshold for certain nonresident, non-citizen estates with US-situs assets above $60,000. A direct holding of US-domiciled securities can therefore raise a question that a fund's historical return table does not answer. The relevant legal analysis depends on ownership, situs rules, any treaty position and the investor's wider estate plan. Do not treat a social-media threshold as a complete estate plan.A practical inventory helps an investor identify when specialist advice is needed:

| Holding or fact | Review question |
| --- | --- |
| US-domiciled ETF or individual US shares | Is this US-situs property for the investor's estate position? |
| Non-US fund holding US shares | How does the fund's legal structure change the analysis? |
| Joint account, trust or company | Who is the beneficial owner and how is the interest documented? |
| US citizen, green-card holder or US-resident family member | Are US-person rules relevant despite another residence? |
| A growing portfolio nearing a material threshold | Is estate planning being reviewed before an urgent event? |

The $60,000 figure is a filing and review trigger, not a universal exemption from every estate-planning consequence. A nonresident, non-citizen estate can use a $13,000 unified credit against tentative tax under the graduated U.S. estate-tax schedule. The filing question, the computation of tentative tax and the investor's treaty position are separate checks. Appendix 1 and the companion workbook show the illustrative schedule, credit and a Form 706-NA review flag. They do not replace legal or tax advice.

## Currency belongs beside tax and custody

Buying a sterling or shilling trading line does not itself change the currency exposure of the underlying companies. The listing currency affects how an investor transacts. The economic result depends on the asset return, exchange rates between the asset and spending currencies, and any explicit hedge.

\[ R_{\text{home}} = (1 + R_{\text{asset}})\left(\frac{S_1}{S_0}\right) - 1 \]

For an investor reporting in shillings, \(S\) can be KES per dollar. A dollar asset return can be offset or amplified by the change in that exchange rate. This is not an instruction to forecast currencies. It is a reason to separate a near-term reserve for known spending from a long-horizon investment allocation.

## A repeatable implementation record

Before funding an overseas account, record the same facts each time: intended exposure, fund ISIN and domicile, dealing venue, quoted spread, commission, conversion method, personal tax status, the source and date of each rule, and the reason the holding belongs in the policy. Retain trade confirmations, statements and tax forms. A spreadsheet can total costs, but it cannot repair a missing legal fact.![A cross-border investment workflow from investor facts through funding, custody, tax records and review.](/static/site/us-investor-workflow.png "Cross-border investment workflow")

The next chapter moves from ownership constraints to portfolio architecture. The purpose is not to find a universal list of funds. It is to decide what role each holding has, what loss it can create, and which additional idea would genuinely improve the existing policy.

## Sources to verify before a live decision



- US Internal Revenue Service guidance for withholding of US-source income paid to foreign persons and estate-tax filing for nonresident, non-citizen estates.
- The fund issuer's current prospectus, factsheet, Key Information Document and tax documentation.
- The investor's residence-country revenue authority and, where appropriate, a cross-border tax professional.
- The broker's current schedule of dealing, custody, foreign-exchange and transfer charges.

## Technical companion

The after-withholding cash distinction is:

\[
D_{\mathrm{net}} = D_{\mathrm{gross}}(1-w),
\]

where (w) is the applicable withholding rate. Treaty eligibility, domicile, estate exposure and reporting remain fact-specific. The [withholding mathematics appendix](<Appendices/Appendix 01 - Cost Compounding and Withholding Mathematics.md>) provides the worked ownership cases.
