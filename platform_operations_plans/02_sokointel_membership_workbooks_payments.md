# Sokointel: Membership, Workbooks and Payments

## Recommended model

Sokointel should use a hybrid research-library and digital-product model.

A membership grants unlimited reading access to the active member library. Workbooks remain separately priced products because they contain editable models, input structures, formula logic, scenario tools, and release support. Non-members can buy a workbook once. Members receive a configurable lower workbook price.

| Customer | Entitlement |
| --- | --- |
| Visitor | Public articles, selected calculators, previews, and selected infographics |
| Registered reader | Saved progress, newsletter, and selected free downloads |
| Research member | Member articles, collections, editions, videos, calculators, notes, and future library updates while active |
| Workbook buyer | Named workbook or collection under a personal-use licence |
| Member workbook buyer | Purchased workbook at the member price |
| Organisation later | Named seats and an internal-use licence |

Membership should not promise unlimited download access to every Excel workbook. A workbook purchase should normally remain available after membership expires. Member-library access ends when its paid period ends.

## Catalogue

| Product | Example | Access rule |
| --- | --- | --- |
| Public research | Introductory article or calculator | Open |
| Member collection | Complete research series and protected editions | Active membership |
| One-off workbook | Kenyan dividend-growth model | Purchased asset |
| Workbook collection | US Markets companion bundle | Purchased collection |
| Member workbook price | Lower price for active members | Membership plus purchase |
| Institutional licence later | Classroom or team use | Defined seats and renewal |

Start with one membership plan and a small number of workbook collections. More tiers should follow evidence, not assumptions.

## What Sokointel sells

Sokointel sells research selection, dated sources, transparent methods, editorial judgement, a coherent learning path, practical tools, updates, and time saved. It does not need to claim that facts are secret.

Present the material as general research and education. Do not market it as tailored advice to buy, sell, or hold a security for an individual person. Kenya's CMA treats paid securities analysis and advice as part of the investment-adviser field. Obtain Kenyan legal review before offering personalised advice, portfolio management, execution, or marketing that might cross that boundary. See the [CMA handbook](https://www.cma.or.ke/wp-content/uploads/2023/05/CMA-Handbook-2021.pdf) and [CMA license register](https://licensees.cma.or.ke/).

## Entitlement records

| Record | Purpose |
| --- | --- |
| Collection | Groups articles, editions, video, and workbooks |
| Digital asset | Protected download or media |
| Membership plan | Recurring access rules |
| Price book | Market, currency, tax, and effective dates |
| Order | Commercial checkout record |
| Payment event | Provider event and verification result |
| Entitlement | Specific reader access |
| Asset licence | Purchased workbook and permitted use |
| Refund or revocation | Audited change to access |

Access comes from server-side entitlements. It must not come from a hard-coded URL list or a browser-side price check.

## Checkout rule

1. Reader selects membership, workbook, or both.
2. Server calculates the price from the current price book and active membership.
3. Provider checkout opens.
4. Reader returns to a pending order page.
5. Server webhook verifies signature, reference, amount, currency, status, and idempotency.
6. The verified event grants entitlement.
7. Postmark sends receipt and access confirmation.
8. Refund, cancellation, chargeback, and expiry change entitlement through audited server-side events.

The browser return is never proof of payment. The current code supports Paystack and Stripe paths. Use sandbox accounts, keep provider keys outside Git, and enable live payment only after webhook tests pass.

## Price management

Keep local, regional, continental, and international prices in an editable price book. Each row needs product, market, currency, normal price, member price, tax treatment, effective date, promotion expiry, and approving administrator. Do not hard-code prices in templates or JavaScript.

Measure article-to-account conversion, account-to-member conversion, one-off workbook purchase, member workbook attachment, renewal, refund, and returning readers. Consider an annual workbook credit only if it improves retention without undermining workbook economics.
