# Appendix 04 — Provider comparison and reporting-vector audit

### Companion to Part 01

This appendix asks whether the difference between two Kenya 2025 startup-funding totals is explained by report timing, data coverage, or both. It does not treat the total as a stand-alone scalar. It separates the reporting period from publication date, transaction dates, provider record/vintage dates, amounts and instruments, geography, eligibility and count units. The article and workbook use the same source observations and calculations.

## A4.1 What each provider actually reported

| Dimension | Africa: The Big Deal (ATBD) | Partech Africa Tech VC | Analytical consequence |
|---|---|---|---|
| Reported activity period | Calendar 2025 | Calendar 2025 | Nominal period matches. This does not establish which transaction event assigns a record to that period. |
| Primary publication date | 13 January 2026 | 22 January 2026 | Nine calendar days apart. Publication date is not the data cutoff. |
| Kenya headline | Primary post says “almost” US$1bn | About US$1.04bn | Both public headlines are rounded at source level, but not to the same precision. |
| Exact US$984m value | Contemporary press reports attribute US$984m to ATBD on 15 and 19 January 2026 | Not applicable | Exact ATBD value is corroborated by reporting; it is not printed in the inspected 13 January primary post. |
| Published Kenya instruments | US$582m debt; US$383m equity | US$498m debt; US$539m equity | Mix differs materially; there is no transaction-level bridge in the public summaries. |
| Total growth | +52% as stated | +72% as stated | The rates use provider-specific comparison series. Do not treat them as directly comparable before matching each prior-year vintage. |
| Deal threshold and eligibility | ATBD's public tracker describes deals at or above US$100k; its broader reporting covers equity, debt and grants and excludes exits | Equity or debt rounds at or above US$200k for African technology/digital startups | The eligibility universes differ. The 2025 Kenya summary does not identify which deals drive the difference. |
| Geographic allocation | Country-tagged tracker series; the inspected year-end summary does not state a detailed company-by-company Kenya assignment rule | A startup is African when its primary market, based on operations and/or revenue, is in Africa | A legal recipient, headquarters and operating market need not be the same entity or place. |
| Count unit | 75 Kenyan ventures raising at least US$100k, down 23% | 91 Kenya deals: 72 equity and 19 debt | A company/venture count is not a transaction count. Do not use one as a denominator for the other. |
| Disclosure | ATBD later says public disclosures and confidential investor information can arrive with delay | Partech says fully disclosed, partially disclosed and confidential data are used | Both datasets can include nonpublic information; this does not make their record sets identical. |
| Access to underlying records | ATBD's public year-end post links to a subscription for the full underlying data; its database page describes a monthly updated Excel product with 30+ fields | The inspected 2025 report publishes aggregate results and disclosure metadata; confidential observations are sourced through private engagement | Request each report vintage, current snapshot and change log. A live/current product is not automatically the historical dataset used for the January 2026 headline. |
| Last included transaction date | Not stated in inspected 2025 public summary | Not stated in inspected report | The underlying event cutoff is unknown. |
| Record-added date / frozen snapshot | No dated export or record history inspected | No dated export or record history stated | We cannot tell which transactions appeared between releases or whether prior-year records were revised. |
| Year-assignment rule | Not stated in inspected summary | Not stated in inspected report | Announcement, signing, commitment, closing, drawdown, cash receipt and first-seen dates cannot be presumed equivalent. |

The nine-day gap is an observable **document-publication interval**. It is not an observable interval between database cutoffs. The ATBD date is its public year-end post; Partech's date is its formal report release. An internal data export could have been prepared or frozen before either publication date. Neither inspected summary publishes such an export date.

## A4.2 Reporting is a vector

For provider report *r*, preserve a report-level record such as:

`Rᵣ = (provider, activity period, report/publication date, source/version, data cutoff, export/as-of date, scope, threshold, instrument coverage, geography rule, count unit, rounding/precision, disclosure basis)`

For each underlying transaction *i*, preserve a distinct observation:

`Tᵢ = (company, legal recipient, investor/lender, amount, original currency, instrument, announcement date, agreement/signing date, commitment, close date, drawn amount/date, cash received/date, provider first-seen date, provider-assigned year, assignment basis, country allocation, disclosure state, evidence source, provider snapshot ID)`

These are two linked records, not a single number plus one date. Amount is itself qualified: a signed credit facility, its committed limit, its drawdown and the cash that reached an operating entity are different values. A currency conversion also requires an original amount, FX source/rate and conversion date. One announcement can map to multiple providers or tranches, and one company can have more than one legal recipient.

If an analyst has only an annual report, the unavailable transaction fields should be marked “not disclosed in inspected report,” rather than guessed from press dates. “Unknown” is not a zero and it is not evidence that two providers used the same rule.

## A4.3 Dated publication and evidence sequence

| Publication / event date | Source and evidence | What it supports | What it does not support |
|---|---|---|---|
| 13 Jan 2026 | ATBD's “2025 in review — Mapping the money” | Kenya almost US$1bn; US$582m debt; US$383m equity; +52% growth; 75 ventures above US$100k | Exact US$984m; transaction cutoff; snapshot/vintage; individual date rule |
| 15 Jan 2026 | The Star coverage | Exact US$984m attributed to ATBD appears in inspected public coverage two days after the provider's post | That it was the first publication or reflects a subsequent provider revision |
| 19 Jan 2026 | Business Daily coverage | Exact US$984m and a 54.2% arithmetic growth rate using US$638m as the 2024 comparison | Why that recomputation differs from ATBD's stated +52% |
| 19 Jan 2026 | The EastAfrican coverage | Independent contemporary report of the same exact total attributed to ATBD | A separate transaction-level validation of the tracker or a vintage bridge |
| 22 Jan 2026 | Partech's official release and report | About US$1.04bn for Kenya, +72% YoY; public scope and use of fully, partly and confidential data | Exact underlying transaction cutoff, export version or date-assignment rule |
| 12 May 2026 | ATBD's later investor-participation post | ATBD says that deals may be reported with delay and uses public sources plus confidential investor disclosures | A statement that the Kenya 2025 total was revised, the revised value or the size of any delay effect |

The later methodology note is evidence that reporting delays can happen in ATBD's workflow. It is not evidence that this particular US$984m value was backfilled after 13 January. Partech's disclosure statement likewise describes its source process, not the report's last data date. The correct finding is **possible but unquantified timing effect**.

## A4.4 Reproducible amounts and limits

| Calculation | Arithmetic | Result | Interpretation |
|---|---:|---:|---|
| Total spread | 1,040 − 984 | US$56m | Partech's rounded headline less the exact amount quoted in secondary coverage. |
| Spread relative to ATBD amount | 56 / 984 | 5.69% | Relative scale only; not an error rate. |
| ATBD debt and equity subtotal | 582 + 383 | US$965m | Sum of the two published categories. |
| ATBD unassigned total difference | 984 − 965 | US$19m | Leave unassigned. Do not infer grants, rounding or a revision without a matched export. |
| Partech category subtotal | 539 + 498 | US$1,037m | US$3m below the rounded US$1.04bn headline. |
| Partech equity less ATBD equity | 539 − 383 | +US$156m | Opposite-direction mix difference; no deal explanation is established. |
| Partech debt less ATBD debt | 498 − 582 | −US$84m | Opposite-direction mix difference; no deal explanation is established. |
| Recomputed ATBD annual change | (984 / 638) − 1 | 54.23% | Uses the contemporary exact total and the older published 2024 value. |
| Recomputed minus stated ATBD growth | 54.23% − 52.00% | +2.23 percentage points | Could reflect precision or unmatched data vintages; public evidence inspected does not resolve it. |
| Prior-year base implied by +52% | 984 / 1.52 | US$647.37m | Implied arithmetic base; it is not a verified ATBD 2024 revision. |
| Implied base less published 2024 value | 647.37 − 638 | US$9.37m | Size of the unexplained base difference under these rounded inputs. |

The arithmetic can be exact while the inputs have different precision and scope. In particular, it would be incorrect to label the US$19m as grants because ATBD's wider tracker can include grants; the inspected Kenya summary lists only the US$582m debt and US$383m equity values and does not reconcile an exact US$984m total against them in a dated export.

## A4.5 What a proper date/scope reconciliation requires

Request the same dated data vintage from each provider, including source-record IDs and change history. Then create one row per underlying financing event. Match on legal issuer/recipient, company aliases, investor/lender, original amount/currency, instrument, dates and source citations—not company name and annual total alone. For facilities, separate announced maximum, contracted commitment, availability, draw, receipt and repayment. For a multi-tranche transaction, record each tranche and preserve a round/facility ID so total company funding is not double-counted.

There is a concrete acquisition path for ATBD data: its January 2026 year-end post links to a subscription for the full underlying database, and its product page describes a monthly updated Excel database of $100k+ African startup deals with more than 30 fields [6]. Do not treat the current monthly file as a substitute for the vintage used to prepare the January report. Request the January 2026 snapshot, a current snapshot and the change log or record-added dates. Partech's public methodology says it draws on public sources, network data and confidential disclosures; it does not publish a complete public row-level ledger for the Kenya total [5]. Even a strong public-news reconstruction should therefore be labelled a disclosed-deal subset, not a complete provider match. No purchase was made and no ATBD export was obtained for this analysis.

The reconciliation should classify each unmatched item under a controlled reason: below threshold; sector exclusion; country allocation; instrument exclusion; grant treatment; exit/secondary excluded; duplicate; date-assignment difference; source not disclosed; amount/FX difference; or unresolved. A timing attribution is supportable only if the same deal appears in one provider's later vintage or if a provider documents a dated revision, with amount, status and inclusion date. Otherwise leave the cause unresolved and show known definition differences separately from possible vintage effects.

| Required transaction field | Why it matters |
|---|---|
| Provider and source-record ID | Identifies the observation and permits duplicate/revision tracking. |
| Company, legal recipient and alias | Keeps brand, parent, affiliate and borrower distinct. |
| Amount, original currency, amount basis | Separates total facility, commitment, drawn cash, equity proceeds and reported approximation. |
| Instrument, stage and eligibility threshold | Makes equity/debt/grant and provider universe differences visible. |
| Announcement, signing, close, draw and receipt dates | Separates public news from legal and cash events. |
| Provider first-seen date; assigned activity period and rule | Detects late reporting and year allocation. |
| Report publication date; export/snapshot as-of; vintage | Defines the source version behind an aggregate. |
| Country/sector rule and disclosed/confidential status | Allows attribution and coverage differences to be examined. |
| Evidence link, locator, precision and verification status | Allows an independent reader to reproduce the inclusion decision. |

## A4.6 Workbook map

`Provider Comparison` reproduces the headlines, category differences, growth checks and residuals. `Reporting Vectors` holds the source/report-level comparison, publication timeline and ATBD's subscriber route to the full database; it says explicitly that a current export is not the historical January 2026 vintage. `Deal Ledger` leaves the screenshot's company claims out of the actual transaction rows and now has separate fields for provider/report dates, first-seen date, export as-of, provider-assigned period, assignment basis and release vintage. Those fields are blank because no dated provider export was acquired. `Sources and Checks` records source URLs and tests the arithmetic, including the nine-day publication interval; that check does **not** claim a nine-day underlying data-cutoff difference.

## Sources

1. Africa: The Big Deal, “2025 in review — Mapping the money,” 13 January 2026, https://thebigdeal.substack.com/p/2025ir2.
2. The Star, “Kenya tightens grip on Africa startup capital, attracts Sh126bn in 2025,” 15 January 2026, https://www.the-star.co.ke/business/2026-01-15-kenya-tightens-grip-on-africa-startup-capital-attracts-sh126bn-in-2025.
3. Business Daily Africa, “Kenya remains on top with Sh127bn startup funding in 2025,” 19 January 2026, https://www.businessdailyafrica.com/bd/markets/market-news/kenya-remains-on-top-with-sh127bn-startup-funding-in-2025-5331672.
4. The EastAfrican, “Kenya takes largest share of Africa’s venture capital funding,” 19 January 2026, https://www.theeastafrican.co.ke/tea/business-tech/kenya-takes-largest-share-of-african-venture-capital-funding-5329968.
5. Partech, “2025 Africa Tech VC Report: African Tech Funding Rebounds to US$4.1B,” 22 January 2026, https://partechpartners.com/news/2025-partech-africa-tech-vc-report-african-tech-funding-rebounds-to-us41b-driven-by-record-debt-activity-and-disciplined-equity-growth; report and methodology, https://partechpartners.com/africa-reports/2025-africa-tech-venture-capital-report.
6. Africa: The Big Deal, database product page, https://africathebigdeal.com/, and “2025 in review — Mapping the money,” 13 January 2026, https://thebigdeal.substack.com/p/2025ir2. The provider describes subscriber access to the full data and a monthly updated database; the required dated historical export was not acquired.
6. Africa: The Big Deal, “Where are the investors?”, 12 May 2026, https://thebigdeal.substack.com/p/invest426.
7. Africa: The Big Deal, *2024 Round-Up*, January 2025, https://africathebigdeal.com/wp-content/uploads/2025/01/ATBD-2024-Round-Up.pdf.
