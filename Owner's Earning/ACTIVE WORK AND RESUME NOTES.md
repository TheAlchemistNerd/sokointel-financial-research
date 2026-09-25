# Owner's Earning — active work and resume notes

Updated: 24 September 2026

## Active goal

Inspect video guides for completed projects outside Owner's Earning, then complete production guides for all four completed Owner's Earning projects: Project 1, Project 2, Project 3 and What Startup Funding Figures Actually Measure. Keep the guide episodes tied to each article, appendix and workbook. The startup-funding reconciliation goal is complete; the Projects 1–3 reporting-vector audit remains deferred and is not a completed source-level audit.

## Current phase: Owner's Earning video guides — guide files drafted and checked

### Reference guides inspected

- `US Markets and Portfolio Construction/Video Tutorial Guide.md` for the compact course map, practical questions, workbook demonstrations, end actions and publishing workflow.
- `NSE Dividend Growth Project 2026/Video Tutorial Guide.md` for the timed episode segments and production checklist.
- The outside-project storyboards in `Publishing and Video Production`: African Markets and Business Credit, International Investing and Diaspora Finance, Kenyan Equities and Company Analysis, and Kenyan Tax and Household Finance. These contribute the evidence-first story flow: decision, opening questions, case inputs, mechanism, calculation, stress, source records, direct answer and next action.
- The shared `Publishing and Video Production/YouTube Production Plan.md` for conversational delivery, source notes, readable visuals, appendices, captions and publication handoff.

### Guide files created

- `Project 1 - MSMEs and Small Businesses/Video Tutorial Guide.md` — five episodes; the Part 1 workshop bridge and dated draw test are shown separately from the workbook's larger general scenario.
- `Project 2 - Listed Companies and Valuation/Video Tutorial Guide.md` — five episodes; includes the U.S. and NSE source periods, and directs viewers through both U.S. asset profiles and all seven NSE industry profiles in `Profile Stress`.
- `Project 3 - Failure Retrospectives and Warning Systems/Video Tutorial Guide.md` — three episodes; distinguishes event/date-known/source dates, court findings from claims, legal entities and fictional operating schedules.
- `What Startup Funding Figures Actually Measure/Video Tutorial Guide.md` — three episodes; includes provider denominators and vectors, debt service and dilution, company evidence and investor-recovery limits.
- Linked each guide from its project README. The guides contain 16 episodes total. They are production guides; no slide decks, narration recordings or finished videos were created in this phase. Canonical public article URLs remain to be added after publication.

### Workbook correction made while mapping the Project 1 demonstrations

- The original Project 1 `Working Capital` formulas had column references shifted across DSO, DIO and DPO, and the monthly net-working-capital formula used the wrong sign/column combination. Corrected the builder so DSO = receivables / credit sales × 30; DIO = inventory / cost of sales × 30; DPO = payables / credit purchases × 30; NWC = receivables + inventory − payables.
- Added an `Article Case` worksheet to reproduce the Part 1/Appendix 01 workshop example and dated draw test. It returns KSh990,000 normalized owner earnings, KSh140,000 provisional headroom, and negative KSh60,000 after removing the disputed receipt. The general `Owner Earnings` worksheet remains a separate scenario, clearly identified in the article and README.
- Rebuilt the Project 1 workbook with 15 sheets and 236 formulas. Its scenario/formula checks passed; the exported ratios and article-case bridge were checked, and the three new bridge residuals are zero. The preview renderer still reports missing worksheet IDs for cross-sheet formulas, so visual layout remains unverified.

### Guide QA

- Local Markdown links resolve in all four video guides.
- Guide episode counts are 5, 5, 3 and 3 respectively.
- Article word-count audit remains above 3,500 body words for every article in all four Owner's Earning projects. No article was shortened in this guide phase.
- Project 2's profile guide names all nine stress scenarios: two U.S. profiles and seven NSE profiles; it labels the normalized residuals as scenarios, not valuations or issuer forecasts.

## Completed phase: startup-funding reporting-vector correction — canonical workbook rebuilt and audited

The current question is whether the Kenya 2025 ATBD and Partech totals differ because of reporting dates, or because the comparison has treated each report as a scalar. The corrected analysis must keep these dimensions separate:

- amount, currency, scale, precision and category subtotals;
- source, source type and source publication date;
- activity period / financial year;
- announcement, signing, close, commitment, drawdown and cash-receipt dates where applicable;
- provider record or first-seen date, snapshot/export date and release vintage;
- provider's rule for assigning an observation to a year;
- legal recipient, operating geography / country allocation, sector eligibility, instrument and threshold;
- count unit (venture, equity round, debt deal or other) and disclosure status;
- what each report does not disclose.

### Established findings to preserve

- Africa: The Big Deal's public 2025 post was published 13 January 2026. It describes Kenya as almost US$1bn, reports US$582m debt, US$383m equity, +52% total growth, +33% debt growth, and 75 Kenyan ventures above US$100k, down 23%.
- Contemporary reporting gives an exact ATBD-attributed Kenya total of US$984m. Business Daily published its report on 19 January 2026 and calculates +54.2% from the previously published US$638m 2024 value. The inspected exact-total coverage begins 15 January (The Star); this is an inspected publication date, not proof it was the first publication anywhere.
- Partech's official 2025 Africa Tech VC report was released 22 January 2026 and reports about US$1.04bn for Kenya, including US$539m equity and US$498m debt. Partech's scope is US$200k+ equity/debt for African tech and digital startups, allocated by primary market (operations and/or revenue); it reports 91 Kenya deals.
- The two annual reports were published nine days apart. The exact-total report and Partech release are seven days apart. These publication dates do not reveal either provider's underlying data cutoff, last included transaction date, record-added date, revision history or assignment-date rule.
- ATBD later stated (12 May 2026) that deal reporting can be delayed and its database uses public sources and confidential investor disclosures. Partech also says its report includes fully disclosed, partially disclosed and confidential data. Those facts make reporting-vintage effects plausible, but neither quantifies a revision to the Kenya 2025 totals. Do not attribute the provider spread to date effects without a transaction-level bridge.
- Reproducible arithmetic: Partech minus ATBD exact secondary-reported total = US$56m, or 5.69% of US$984m; equity difference = +US$156m; debt difference = −US$84m. ATBD debt plus equity = US$965m, leaving US$19m against the US$984m secondary-reported total unassigned. Partech's categories sum to US$1.037bn, about US$3m below its rounded headline. Using US$984m and US$638m gives 54.23%, 2.23 percentage points above ATBD's stated 52%; the source vintage difference is unresolved.

### Work completed in this phase

1. Expanded Part 01 with the report-level and transaction-level date vectors, publication timeline, interpretation limits and a direct finding: publication timing makes a vintage effect plausible but cannot establish it. Corrected the workbook link and map.
2. Created Appendix 04 with provider definitions, a dated publication sequence, calculations, source-vintage limits and the transaction-level reconciliation fields required to quantify a timing effect.
3. Corrected Appendix 01: US$984m is a contemporary secondary-reported ATBD total; ATBD's primary 13 January post says “almost US$1bn.” The US$19m remains unassigned.
4. Updated the README and appendix indexes to include `Reporting Vectors` and Appendix 04.
5. Rebuilt the startup workbook. It has 12 sheets, including `Reporting Vectors`, and separate provider/report/first-seen/snapshot/assigned-period/vintage fields in `Deal Ledger`. Built-in arithmetic/scenario checks passed and the formula audit found 371 formulas with no flagged formula errors.
6. Fresh body-word count using regex word-tokenization and excluding References/Sources/Bibliography: Part 01 6,066; Part 02 3,752; Part 03 3,837. All remain above 3,500; no article was shortened.
7. Rebuilt the Copia source/status update and aligned source-check formulas to the canonical `Startup Funding Market and Outcomes Workbook.xlsx` after the user closed it. The canonical workbook has 12 sheets and 371 formulas; `COPIA-COURT-2026` is present, and Company Outcomes records that the current status is unknown.
8. Reopened the saved canonical workbook and verified cached calculations: provider spread $56m; 54.23% ATBD recomputed growth; the ATBD $19m category remainder remains explicitly unassigned; the Partech rounded category residual is $3m; the loan schedule totals KES100m principal and KES18.75m interest; the downside first-month DSCR is 0.815; and there are no cached formula errors. The loan principal check has KES0.000000015 of floating-point residue. The new ATBD database-access event is formatted as a date and the source/check table shifted correctly after adding `ATBD-DATABASE`.
9. Web review confirmed that ATBD links its full underlying data to a subscription; its product page describes a monthly updated Excel database of $100k+ African startup deals with 30-plus fields. Partech's public report describes fully disclosed, partially disclosed and confidential observations; its reported confidential shares are Africa-wide, not Kenya-specific. The article, Appendix 04 and workbook now tell readers to request the January 2026 ATBD snapshot, a current export and revision history. No dataset was purchased or provided, so the actual deal-date bridge remains unverified. This is an explicit evidence boundary, not a claim that publication timing explains the $56m gap.
10. The bundled workbook preview renderer remains unavailable because it reports missing worksheet IDs for cross-sheet formulas. The saved workbook has no cached formula errors and its built-in scenario/formula audit passed. Structural inspection found an oversized frozen area on `Reporting Vectors`; the builder now freezes only the first five rows, and the exported workbook confirms the pane at A6.

## Deferred phase: Projects 1–3 reporting-vector audit — partial work recorded, not complete

### Work completed in this pass

1. Rechecked the canonical programme, research/drafting protocol, project READMEs, workbook builder, relevant workbook maps and the existing vector concerns. The saved protocol records the recursive Markdown and MM–Merton/Buffett Markdown/R Markdown review and the completed-project workbook comparisons; this pass targets evidence-vector gaps in the three current project workbooks.
2. Added a common `Evidence Vectors` sheet to each Project 1–3 workbook. Fields distinguish legal entity/perimeter; measure; amount/unit; observation period; event/measurement date; source-record date; publication/filing date; as-of/retrieval status; source ID; workbook/document locator; evidence state; and limits.
3. Project 1 maps the fictional annual bridge, 13-week cash plan, monthly working-capital schedule, customer and supplier ledgers, inventory example, maintenance register and debt screen. Rows explicitly state that no real entity or source record supports these invented inputs.
4. Project 2 maps NVIDIA and Equinix filing inputs, CBK and Jubilee figures, populated NSE metrics, Home Afrika's missing project measures, nine US/NSE normalized profile scenarios and the fictional KES project screen. Added the missing `EQUITY-25` source record; corrected source metadata for KenGen's June financial year and the dated issuer releases/booklets. Home Afrika blanks remain unavailable, not zero.
5. Project 3 separates Nakumatt's administrator-update and judgment dates; Tuskys petition claims and their calculated subtotal; Copia appointment-effective and Gazette-publication dates; Twiga entity/status/publication dates; the secondary funding aggregate; fictional cash schedules; and historical owner-earnings evidence gaps.
6. Updated the three project READMEs, canonical workbook description and article workbook maps for Parts 1–13. Expanded Part 11 with a source-linked example showing why event, report-preparation and public court dates cannot be collapsed.
7. Rebuilt the workbooks. Existing scenario/formula checks and formula audits passed; exported sheets/formula counts are Project 1: 14 sheets/223 formulas; Project 2: 11 sheets/81 formulas; Project 3: 10 sheets/69 formulas. The preview renderer remains unavailable due missing worksheet IDs in cross-sheet formulas, so visual layout is not verified.
8. Body word counts after the additive edits and before workbook maps/references: Project 1 Parts 1–5 = 3,928; 3,965; 3,892; 3,892; 4,186. Project 2 Parts 6–10 = 3,644; 3,552; 3,555; 3,581; 3,889. Project 3 Parts 11–13 = 3,911; 3,536; 3,632. No article above 3,500 was shortened; Part 11 was expanded to clear the floor.
9. Reopened NVIDIA's primary FY2026 SEC Form 10-K and added a precise capex bridge: $6.042bn property/equipment/intangible purchases in investing cash flow plus $0.101bn principal payments in financing cash flow equals $6.143bn, which rounds to management's $6.1bn MD&A figure. The article, Appendix 02 and Project 2 `Evidence Vectors` now show that calculation and preserve the separate statement classifications; the bridge does not assign maintenance versus growth capex or claim the two disclosures have identical definitions. Project 2 `Sources and Checks` now tests the rounding bridge.
10. Rebuilt all three workbooks after that addition. Project 1: 14 sheets, 223 formulas, 11 evidence-vector records; Project 2: 11 sheets, 82 formulas, 47 records; Project 3: 10 sheets, 69 formulas, 15 records. Existing workbook checks passed, including Project 2's capex-rounding check (zero residual). A fresh body-word count using regex word-tokenization and excluding References/Sources/Bibliography is Project 1 Parts 1–5 = 4,076; 4,148; 4,052; 4,002; 4,248. Project 2 Parts 6–10 = 3,764; 3,779; 3,629; 3,695; 4,057. Project 3 Parts 11–13 = 4,051; 3,672; 3,749. The earlier counts in item 8 used a different counter, so compare each set only with its own method. All remain above 3,500 under the current counting rule.

### Checks to resume when the user returns to this phase

- Exported workbook inspection is complete: Project 1 has 11, Project 2 has 47 and Project 3 has 15 evidence-vector rows. Key source IDs, the new NVIDIA capex reconciliation, date distinctions and labels were checked in the saved `.xlsx` files; the Kakuzi and BAT rows were corrected so only dividend-per-share values use KES/share. This does not verify visual layout.
- Capture exact filing page/note locators where feasible. Rows flag unrecorded locators; do not invent one.
- Confirm current primary legal and issuer records before publication, especially GT Flow/Templar Field notices and Home Afrika project-level data.
- Continue article-to-workbook spot checks and retain the user's deferred startup-provider questions below.

## User steering recorded for later

- The user emphasized that a financing report is a vector—amount, source, financial year/activity period, declaration/publication date and related timing—not a scalar. This standard has been applied to the startup provider comparison.
- The user asked whether information for Projects 1–3 had the same scalar limitation. A quick structure audit found mixed coverage (described below). The user then asked to finish the current startup work and put these comments in a file to revisit later. No changes to Projects 1–3 were made in this phase.
- Preserve the distinction between report publication date and a transaction's announcement, agreement, close, commitment, drawdown, cash-receipt, first-seen and assigned-period dates. Never infer a provider's cutoff or revision from publication date alone.

## Prior audit findings retained for interpretation

The user asked whether the first three projects had also reduced retrievable evidence to scalar values. A quick inspection found mixed coverage, so do not claim all three already preserve a complete per-observation vector:

- **Project 1 — MSMEs and Small Businesses:** the 13-week cash, invoice, inventory and supplier examples contain dates and operating dimensions, but they are explicitly fictional. The annual owner-earnings bridge has KES amounts without a real entity, financial-year end, source document or report date because it is an illustrative scenario.
- **Project 2 — Listed Companies and Valuation:** filing inputs carry amount, unit, source ID and status; NVIDIA's FY2026 year-end and 10-K filing date are stated at sheet level. NSE cases carry period, measures, units and source IDs. Some date, entity/consolidation and document-locator details remain in source tables or prose instead of on every observation. The normalized profile stresses are scenarios, not retrieved issuer values.
- **Project 3 — Failure Retrospectives and Warning Systems:** this is closest to an evidence vector: it separates legal entities, event dates, “known when,” source class, amount, unit, claim/evidence status and limitations. Some records still combine source/date and need distinct event, report/filing/publication, observation-period, as-of/vintage and retrieval fields.

The new sheets implement this common schema for the identified observations while leaving undisclosed coordinates open. This was a targeted pass; it does not replace final claim-by-claim article verification or visual/print review of the exported workbooks.

## Broader project requirements to retain

- The intended corpus includes all Markdown files under `Owner's Earning` and its nested folders, the relevant R Markdown and TXT source files, and the explicitly requested `Source Imports/MM-Merton Framework Buffett Research` MD/RMD material. Check the completed projects they map to, including their articles and final Excel workbooks, before making structural changes.
- Projects 1, 2 and 3 each have their own workbook. The startup-funding series also has its own workbook. Keep article examples tied to workbook calculations and cite appendices where the completed projects use them.
- The user requested pragmatic, conversational articles at the depth and rigor of the completed project materials, peer-reviewed research where relevant, detailed appendices, independently checked web sources and calculations, and no defensive prose that substitutes caveats for useful analysis.
- Do not reduce any article already at 3,500 words or more. Retain the requested US and NSE industry/asset profile testing in the listed-company project and verify that workbook cases are actually discussed in the related articles.

## Deferred phase: Projects 1–3 reporting-vector audit

- The user asked to finish the startup-funding work, record their questions in this file and return to the Projects 1–3 evidence-vector audit later. The workbook vector sheets were partially updated, but the claim-by-claim and source-level audit remains incomplete. Resume only as a separate later phase; do not imply the current video-guide work completed it.

## Source links for the current phase

- ATBD, 13 January 2026: https://thebigdeal.substack.com/p/2025ir2
- The Star, 15 January 2026: https://www.the-star.co.ke/business/2026-01-15-kenya-tightens-grip-on-africa-startup-capital-attracts-sh126bn-in-2025
- Business Daily, 19 January 2026: https://www.businessdailyafrica.com/bd/markets/market-news/kenya-remains-on-top-with-sh127bn-startup-funding-in-2025-5331672
- Partech, 22 January 2026 release: https://partechpartners.com/news/2025-partech-africa-tech-vc-report-african-tech-funding-rebounds-to-us41b-driven-by-record-debt-activity-and-disciplined-equity-growth
- Partech report: https://partechpartners.com/africa-reports/2025-africa-tech-venture-capital-report
- ATBD later reporting-delay context, 12 May 2026: https://thebigdeal.substack.com/p/invest426
