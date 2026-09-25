# From the 25 September architecture material to SokoIntel calculators and research

**Review date:** 25 September 2026, Africa/Nairobi.  
**Visibility:** INTERNAL ONLY; not a public article, asset catalogue entry or downloadable reader document.  
**Repositories:** `financial material` and `business and technical website blog`.  
**Boundary:** review the Markdown material created/copied or modified on this date within the website repository's `product_architecture`, including children. Preserve the original specification, external source materials, article bodies and workbooks. The authorised follow-up makes only the three internal index/reference corrections recorded below. Flag files for later consolidation or relocation; do not delete them.

## 1. Finding

The material is substantially relevant to SokoIntel, but it is not one undifferentiated implementation backlog. Its strongest immediate contribution is a set of connected, inspectable financial cases: **reported earnings → sustainable operating cash → dated financing obligations → capital and liquidity constraints → the cash belonging to an identified investor**. The public Project 2 calculators are an appropriate first application. They should demonstrate the relationships transparently, with the deeper sector, historical-data and institutional work kept explicit.

The useful next step for articles and workbooks is predominantly to extend their numerical schedules, source records and scenario explanations. The notes repeatedly recognise that much of the narrative already exists. Adding another general explanation of owner earnings, guarantees, cash flow or bank capital would repeat established material. A dated case that reconciles receipts, payment dates, financing and distributions would add more value.

The largest scope risk is interpreting every imported banking, trading, accounting or neural-model discussion as part of the first public release. FRTB, derivative capital, calibrated deposit behaviour, live trading and operational accounting are specialist workstreams with separate data, validation and institutional responsibilities. They are related to the enterprise ambition, but they are not prerequisites for a useful listed-company valuation calculator.

The commercial positioning remains coherent: The Motley Fool is the reference for research, education and a recurring membership relationship; Moody's Analytics is the reference for data, models and governed professional workflows. These are strategic comparisons, not a claim of present parity. The current publishing platform is the distribution and demand-discovery channel. The intended C# calculation core, Excel-DNA, VSTO, ASP.NET services and Azure enterprise deployment remain the destination. Nothing in the imported material warrants replacing the existing Django platform or the chosen enterprise stack.

## 2. What was actually reviewed

The local date filter identified **128 files**, including **46 Markdown files**. The remaining 82 consist of 32 HTML files, 17 JSON files, 23 text files, six Python files, three stylesheets and one CSV. The Markdown inventory contains **40 distinct SHA-256 values**: six file instances are exact duplicates. Five further document pairs differ only by a project-copy footer after local links are normalised for comparison. They represent repeated substantive review text, not five extra analytical developments.

All distinct Markdown content was read. Exact duplicate bodies were represented by one read with every path preserved. Near-duplicate bodies were compared, including their different footer/context. Long output that was truncated was recovered through narrower reads. The supporting import manifest and selected reading/verification records were inspected as provenance. Imported Python scripts were not run. The long historical raw conversations and earlier canonical specification were not freshly reread in full; their documented placement and source pointers were assessed through the date-qualified review documents.

The import manifest's **“45 matching files” does not mean 45 Markdown files authored today**. It counts files mentioning SokoIntel, including HTML renderings. Its separate total is 121 copied files. Forty-two of the 46 scoped Markdown files have original-source entries in that manifest, and all 42 copy hashes matched at the initial review snapshot. Two imported copies subsequently received the explicitly authorised reference-label correction; their new hashes are recorded separately without rewriting the historical import manifest. The other four documents are the collection README and three root-level documents. Initial file-level evidence is in [source_inventory.csv](source_inventory.csv); current correction evidence is in [copy_corrections_2026-09-25.json](copy_corrections_2026-09-25.json).

Important date distinctions:

- `Before the Ratio` is an industry article dated **15 September**, copied into two folders on 25 September. Its creation timestamp does not make it a new article.
- The cross-project project notes for Business Credit, MSMEs, Mwendo, Underwrite, KESONIA, insurance/Bayesian interfaces and Workbench candidates are headed **23 September**. Several acquired a 25 September modification time because local links were adjusted during copying.
- The 25 September Owner Earnings follow-up explicitly supersedes the earlier statement that Project 1 was only planned: five drafts and a workbook already existed by 24 September.
- Today’s Treasury, pricing-lifecycle and business/Owner Earnings follow-ups develop earlier notes. Their “proposal”, “not implemented” and “not a workbook-cell audit” statements remain material.

The review uses source IDs AR01–AR46 from the inventory. Each row of [file_action_map.csv](file_action_map.csv) gives its own classification and target. Timestamps are evidence of local file state; the document's own date and the import manifest provide additional authorship/provenance context.

### Conflicts and authoritative resolutions

| Conflicting statement or interpretation | Evidence and resolution | Disposition |
|---|---|---|
| “45 files” interpreted as today's Markdown total | Collection README lines67–74 explicitly counts 45 matching files across formats and121 copied files; the fresh date filter finds46 Markdown files | Preserve the original import statistic and label the new scope separately |
| Created today interpreted as authored today | AR24/AR43 date to15September; older project notes date to23September and were copied/link-adjusted on25September | Keep original authorship date beside local creation/modification timestamps |
| Project1 is still only a planned series/workbook | AR15 is a23September planning note; AR09/AR16 and the current project README record built drafts/workbook on24September | Use the newer state for the active plan; retain the older note as dated evidence |
| Equinix downside residual9.0 | Appendix4 table at review disagrees with workbook `Profile Stress!L8`, whose formula and cached value are8.5 | Canonical and ported appendix correction handled in parallel; preserve correct workbook formula and refresh affected derivative assets |
| DCA lacks a portfolio mode; DCF lacks sensitivities | Older calculator-boundary table conflicted with implemented routes and subsequent release notes | Corrected locally in the boundary document; protected calculator implementations were not changed by this documentation fix |
| All workbooks have version-control/audit features | Project2 README explicitly states no separate change-log or verification-case tabs and visible unprotected formulas | Corrected locally in the boundary/wiki descriptions; additional governance remains future work |
| Project2 appendix index has three companions | Project2 README says three; actual `Appendices/README.md` lists01,02,03 and04 | Change the summary count to four when reconciling project metadata |
| `Before the Ratio` reference[1] identifies “Underwrite for Collection” but links `/read/ambc-02/` | Website `content/catalog.json` maps AMBC-02 to “Making Business Credit Work in Kenya” | Corrected only in AR24/AR43 internal copies; old label retained in each provenance note, URL/access date and external originals preserved |
| Seven new educational tools interpreted as a complete issuer/Treasury/SPV platform | Source proposals require multi-period, institution-specific and operational work beyond the bounded current calculators | Publish only verified tool capability in release notes; keep the remaining adoption map internal |

The user's clarification permits targeted inconsistency corrections in internal documentation. The bounded follow-up adds a current-status note to AR45 and corrects reference[1] only in AR24/AR43. The original label remains in a provenance note within each corrected copy. [The separate correction ledger](copy_corrections_2026-09-25.json) records old/new hashes and checks that the import manifest and external originals remain unchanged. Parallel agents corrected local calculator-boundary, formula-contract and wiki capability wording. Root owns the source/ported-appendix and appendix-count reconciliation. None of these local documentation changes establishes production deployment or a public wiki release.

## 3. Existing capability versus the next deliverable

The website already has four anonymous business tools: detailed business credit, owner cash, thirteen-week cash and failure warnings. The [business-calculator release note](<C:/Users/Nevo/Downloads/business and technical website blog/docs/Business Calculators Release 2026-09-25.md>) records their narrow purposes and example reconciliations. The DCF page has a five-year FCFF/WACC model and sensitivity table. Those do not make Project 2's sector-specific valuation methods redundant.

During this review, the parallel implementation introduced seven Project 2 catalogue entries in `apps/calculators/valuation_catalog.py`. The corrected local boundary/wiki/formula documentation records 38 focused tests for the seven bounded tools. This is local implementation and validation evidence, not a Railway deployment check. The implementation agent's final release record owns subsequent validation and deployment conclusions.

| Public Project 2 tool | Useful source connection | What its bounded release can demonstrate | Further work still required |
|---|---|---|---|
| Listed-company earnings bridge | AR14/AR27 §§2,6; Project 2 Part 6 and Appendix 1 | An explicit earnings/CFO reconciliation with maintenance, working capital and shareholder-claim assumptions | Multi-year issuer reconstruction, amendment handling, source-page evidence and controlled analyst adjustments |
| Maintenance/reinvestment scenarios | AR14/AR27 §5; Part 8 and Appendix 2 | Maintenance ranges and their effect on cash capacity | Construction-to-operation calendar, debt draws, interest during construction, commissioning, utilisation and project/equity returns |
| SBC/dilution/repurchases | Part 7, filing/share-count evidence, common quantity dictionary | Separate compensation cost, issued shares and repurchases without double counting | Multi-period employee-award schedules, share-based settlement terms and issuer-specific evidence |
| Equity/reverse valuation | AR14/AR27 §§2,6; Part 6 | Value an identified equity cash-flow claim and solve a stated implied assumption | Full operating forecasts, claim-by-claim debt/lease reconciliation and issuer-specific valuation evidence |
| Bank distribution headroom | AR14/AR27 §3; Part 9/Appendix 3 | Independent capital, liquidity and distribution constraints | Loan economics-to-bank earnings reconciliation, evolving RWA, multiple capital tiers, losses and funding under a common path |
| Insurer remittances | AR14/AR27 §4; Part 9/Appendix 3 | Local permitted remittance, parent obligations and bounded timing sensitivity | Multi-subsidiary currencies, claims/reinsurance settlement schedules, legal permissions and group consolidation |
| US/NSE sector stress | AR14/AR27 §§2,7; Part 10/Appendix 4 | Explain how different profiles respond to selected scenario shocks | Dated, source-supported cash/capital bridges for actual issuers; no cross-sector ranking from normalized indices |

These tools are educational calculations. They are not a SEC ingestion service, bank reporting engine, insurer solvency model or live structured-finance platform. A single-period upper bound is not a forecast of a board-approved dividend. A scenario index is not a money amount, issuer valuation or observed company outcome.

### Documentation drift corrected locally

The [calculator product-boundary document](<C:/Users/Nevo/Downloads/business and technical website blog/docs/Calculator Architecture and Product Boundary.md>) now distinguishes single-asset and portfolio DCA, describes the DCF sensitivity and net-debt bridge, and records seven locally verified Project 2 tools. Its workbook paragraph now qualifies controls by asset/release and accurately identifies Project 2's current limitations. The [internal wiki strategy page](<C:/Users/Nevo/Downloads/business and technical website blog/docs/wiki/SokoIntel-Evolution-and-Industry-Comparators.md>) carries the same current-versus-future distinction. These are local corrections, not evidence that production pages or a wiki were deployed. The protected single-asset DCA, portfolio DCA, compound and cash-flow financial implementations remain outside this correction.

The updated [formula-rendering contract](<C:/Users/Nevo/Downloads/business and technical website blog/docs/Formula Rendering Contract.md>) describes protected inline TeX in symbol tables, adjacent readable fallback text, always-visible meanings/units and Pandoc/native Office Math in reading editions. The shared quantity dictionary still needs to remain consistent across examples and exports: symbol, plain-English meaning, unit, currency, period/date, entity, claim, sign and source status. Existing International Investing/Diaspora Unicode treatment is retained. Local markup/math tests do not prove deployed browser behavior, and correcting the contract does not regenerate an existing PDF. This is a presentation consistency change, not a reason to alter protected financial logic.

## 4. Article and workbook development map

The four named workbook files were located and their actual worksheet names were inspected read-only from XLSX metadata. That verifies the destinations below; it is not a complete formula or accounting audit. Existing text and examples should be preserved, with additions adjacent to the relevant sections and clear links between the web tools, article, appendix and workbook version.

| Priority | Research destination | Exact workbook destination | Change that adds value | Evidence before release |
|---|---|---|---|---|
| P0 | Project 2 Part 6; Appendix 1 | `Filing Inputs`, `NVDA Bridge`, `Assumptions`, `Valuation`, `Evidence Vectors` | Attach a quantity/claim dictionary and as-of evidence to each bridge; reconcile profit and CFO routes; show unavailable estimates rather than filled defaults | Audited filing and period, currency/scale, sign conventions, no second working-capital deduction, share-count/price dates and numerical parity |
| P1 | Project 2 Part 7, “Treat purchase commitments as a timed exposure” | Extend `Filing Inputs` and `NVDA Bridge` with a separately labelled commitment schedule | Maturity ladder of supply obligations, cancellations, customer collections and available funding; joint demand/inventory stress | Contract/filing notes, cancellation rights, amount/date/source and explicit distinction between commitments and recognized liabilities |
| P1 | Project 2 Part 8; Appendix 2 | Preserve `Asset Heavy`; add a construction and operations schedule | Extend the 8.5% stabilized contribution-yield example into dates: capex, financing draws, construction interest, commissioning, utilization, tax, maintenance, reserves and equity cash | Unlevered and equity cash-flow reconciliation; interest/lease conventions; deterministic completion-delay and power-cost cases; yield not relabelled IRR |
| P1 | Project 2 Part 9, after “Turn capital into an explicit distribution test”; Appendix 3 | Preserve `Bank Insurance`; add separate bank and insurer schedules | Bank pricing→earnings→capital→payout; insurer local claims/reinsurance/capital→dated parent remittance | Capital tiers and constraints tested independently; no duplicated loss deduction; cash availability and permissions; insurer payments assigned to the correct entity |
| P1 | Project 2 Part 10; Appendix 4 | `NSE Casebook`, `Profile Stress`, `Evidence Vectors`, `Sources and Checks` | One sourced dated bridge per sector; retain nine normalized stress profiles as a separate teaching layer | Current issuer evidence, sector-specific cash claim and missing-data status; avoid a universal score or imposed value ranking |
| P1 | Business Credit Part 2: offer comparison, order contribution and repayment passages | `P2 Facility`, `Entity Review`, `Credit Readiness` | Add loan/receipt dates, expiry, draw conditions and the minimum-cash date to existing exhibits | Preserve the existing case or clearly identify a separate case; lender and borrower cash reconcile independently |
| P1 | Project 1 Part 4, “Work the debt decision from use to repayment”; Appendix 3 | Extend `Debt and Growth`, linked to `Cash13W`, `Owner Earnings`, `Sources and Checks` | Replace the year-one screen's implied completeness with a full dated term/revolver schedule, cash floor, restricted reserves and stress availability | Contractual principal/interest/fees; maturity distinct from commitment expiry; cash and debt roll-forwards; reserve releases not earnings |
| P1 | Project 1 Parts 2–3 and Project 3 Parts 11–13 | P1 `Working Capital`, `Receivables`, `Inventory`, `Payables`; P3 `Cash and CCC`, `Warnings and Actions`, `Evidence Ledger` | Carry classified operating receipts, overdue supplier balances and dated funding restrictions into warning scenarios | Treat related-party status and economic cash class separately; preserve uncertainty; fictional stress remains separate from company history |
| P2 | Project 1 Part 5; Key-Person Risk companion | `Buy Sell and Succession`, earnings and cash schedules | A distinct buyer/seller/lender bridge for replacement management, working capital and acquisition debt | Actual transaction perimeter and support for every add-back; no invented private-company multiple |
| P2 | Startup Funding companion Parts 2–3 | `Startup Funding Market and Outcomes Workbook.xlsx` (future sheet-level design) | Link instrument conditions, capital calls, repayment dates and restricted funding to operating cash needs and outcomes | Deal status, equity/debt distinction, announced versus disbursed money, recoveries and dated entity status; funding raised is not automatically loss |

File anchors:

- [Project 2 folder/README](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 2 - Listed Companies and Valuation/README.md>) and [workbook](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 2 - Listed Companies and Valuation/Project 2 - Listed Companies Owner Earnings and Valuation.xlsx>).
- [Project 1 folder/README](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 1 - MSMEs and Small Businesses/README.md>) and [workbook](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 1 - MSMEs and Small Businesses/Project 1 - MSME Owner Earnings and Operations.xlsx>).
- [Business Credit Part 2](<C:/Users/Nevo/Downloads/financial material/African Markets and Business Credit/LinkedIn Articles/Part 2 - Business Credit and Fintech.md>) and [workbook](<C:/Users/Nevo/Downloads/financial material/African Markets and Business Credit/Workbook/African Markets and Business Credit - Credit Readiness and Cash Cycle Workbook.xlsx>).
- [Project 3 folder/README](<C:/Users/Nevo/Downloads/financial material/Owner's Earning/Project 3 - Failure Retrospectives and Warning Systems/README.md>).

### A specific numerical correction

At review time, Project 2 Appendix 4's Equinix profile table showed downside residual **9.0**. The actual workbook `Profile Stress!L8` stores a formula with cached value approximately **8.5**, consistent with `90 − 54 − 27.5`. The new calculator's 8.5 result therefore exposes a prose/display mismatch, not a need to force the calculator to 9.0. Root's parallel reconciliation is handling the canonical and ported appendix correction.

Follow the dependency chain after the source correction: article/appendix text, calculator illustration, workbook-linked screenshots, episode slides and published reading editions. Rebuild only affected assets and version their source record. A fresh PPTX or PDF should not be claimed until that asset has actually been regenerated and checked. The workbook formula itself does not need alteration to resolve this discrepancy.

## 5. Reusable numerical cases and their limits

These figures are teaching inputs, not market quotes, current regulatory ratios or reconstructed issuer results. Arithmetic below was independently recomputed for this review; the original sources' broader validation claims were not adopted as production assurance.

| Case | Inputs and checked output | Source | What it tests—and what it does not |
|---|---|---|---|
| MSME order, timely receipt | KES thousands: opening250; deposit200; loan500; fee10; supplier600; staff120; completion100; final receipt800; 18% ACT/360 interest15 at day60. Closes340/220/405; operating surplus180; financing25; increment155 | AR16 lines38–66; AR09 lines69–81 | Cash/principal/expense classification and dates; not an empirical repayment probability |
| MSME delayed receipt | Move800 to day90, keep original debt due day60: cash−395; funding needed to retain floor100 is495 | Same | A liquidity gap, not LGD or permission to extend a loan |
| Separately agreed 90-day loan | Interest22.5; day60 cash120; final397.5; extra cost7.5 | AR16 lines62–66 | Contract comparison with assumptions held constant; not an automatic modification |
| Bank payout upper bound | Opening eligible capital100; profit20 or12; RWA560; illustrative target18%; capital headroom19.2 or11.2; cash limit14 gives14 or11.2 | AR14/AR27 lines31–49 | Separate capital and liquidity constraints; not a complete bank solvency or legal dividend determination |
| Insurer timing | Local remittance12 arrives day90; parent opening3; obligation4 day60; floor2. Before receipt cash−1 and floor gap3; end-period excess9 only after gap funding/repayment is reconciled | AR14/AR27 lines53–69 | A later receipt cannot pay an earlier bill; local claims must not be deducted a second time at parent |
| Revolver lender economics | Drawn4m, undrawn6m, CCF56.4% gives EAD7.384m; EL199,368; contribution20,632; EC886,080; 14% hurdle price18.58548% | AR32 lines27–52 | Distinct interest, fee, exposure and capital bases; not borrower affordability or an official lending rate |
| Reserve-supported debt service | CFADS80/140/50; debt service100/month; initial reserve50. Paid300, residual20, final reserve0: total cash320 reconciles | AR32 lines68–78 | Payment can be met while operating DSCR is0.8/1.4/0.5; not a full SPV waterfall |
| Equinix profile display |90 −54 −27.5 =8.5 | Workbook `Profile Stress!L8`; Appendix4 mismatch at review | Normalized hypothetical sensitivity; not Equinix cash in currency or a forecast |

The pricing casebook also contains hazard/default, migration, static OC, capital-units, CVA and syndication examples. Retain them for the appropriate module. A three-month reserve check does not validate a 36-month transaction waterfall; a static OC identity does not establish loss absorption; a scalar CVA illustration does not implement derivative capital.

## 6. Enterprise concepts worth adopting now as design contracts

AR01/AR31 proposes CR-FR-001–020. The sequence is useful, but these remain provisional identifiers. They should be merged into the controlled requirements register only during an explicit specification update, without silently replacing FR-001–098.

Adopt the inexpensive shared discipline first:

1. **Typed quantities:** money, rates, balances, time, probabilities and index values carry units, entity, currency, date/horizon, claim and formula version. Distinguish source evidence, analyst assumptions and unresolved estimates.
2. **A versioned case:** join source evidence, assumptions, dated cash, calculation outputs, commentary and later observed outcomes by case ID. Bind an article example to the exact model/workbook version used.
3. **Reconciliation invariants:** opening cash plus receipts/funding equals payments plus closing cash; debt balances roll forward; financing is not revenue; reserve movements are not operating earnings; internal allocations cancel on consolidation.
4. **Structured unavailable states:** missing evidence, invalid domains and zero denominators are surfaced. No synthetic current rate or unsupported capital constant should fill a blank invisibly.
5. **Separate public and institutional data:** public forms remain educational; private borrower and tenant payloads do not enter the publishing funnel. A pseudonymous ID does not enforce tenant access.
6. **Report from one calculation result:** PDF, workbook, web and professional adapters should present governed results and provenance, not independently recalculate financial models inside templates.

Professional interfaces can subsequently wrap the validated definitions in the selected C# core and Excel-DNA/VSTO products, with ASP.NET/Azure services where institutional demand warrants them. None of the imported pasted SaaS examples should override that stack. Live trade execution, journal posting and contract amendments remain separate authorised operational capabilities, not implied by an analytical output.

## 7. Relevance, duplication and removal flags

No whole scoped Markdown document was found to be wholly unrelated to SokoIntel's wider intended evolution. Several are indirectly relevant specialist material or provenance support. Deleting every file without “SokoIntel” in its body would remove useful formula, evidence and scope records.

The useful cleanup is **consolidation and relocation**, with original evidence preserved. All flags below are recommendations only; no deletion occurred.

### A. Exact redundant file copies

| Retain one review entry | Redundant imported counterpart(s) | Safe later action |
|---|---|---|
| AR02 business-credit follow-up | AR11 same follow-up in `cross_project/project_notes` | Keep one authoritative review copy; replace the other with a pointer and repair its inbound links |
| AR14 listed-company review | AR27 `owners_earnings_2` copy | Same, retaining both original-source provenance paths in the manifest |
| AR16 MSME follow-up | AR26 `owners_earnings_1` copy | Same |
| AR23 pricing development notes | AR25 `mwendo` and AR44 `underwrite_research` copies | Keep a common casebook with project-specific links; do not maintain three drifting text copies |
| AR24 `Before the Ratio` | AR43 `underwrite_linkedin` copy | Retain the historical article once or link to its original home |

These six excess instances are byte-identical at the recorded snapshot. The choice of retained path is a navigation recommendation, not a change of authorship. Some folders deliberately mirror project destinations; a lightweight pointer can preserve that navigation.

### B. Repeated bodies with a copy footer

AR01/AR31 (credit requirements), AR23/AR30 (pricing/editorial notes), AR22/AR36 (Treasury review), AR21/AR40 (software/STP) and AR20/AR42 (FRTB) have the same substantive body after local links are normalised; project-copy versions add a footer. Flag the extra body for pointer replacement, preserving link context. These are not byte-identical, so do not use their hashes to assert exact duplication.

### C. Move outside the immediate public-calculator backlog

- **AR20/AR42 FRTB:** a specialist banking/trading-book scope. Retain for the future institutional risk branch; exclude from Project 2's initial public calculator deliverable.
- **AR21/AR40 software/STP:** a vendor capability and operational workflow reference. Retain as enterprise integration research; do not imply Bloomberg/MORS/SAP/Oracle connectivity exists or is needed for public tools.
- **AR12 insurance/Bayesian interface:** retain for the insurer data/event boundary; do not copy established frequency/severity derivations into every Owner Earnings article.
- **AR13/AR19 and pricing-lifecycle portions of AR23/AR30:** useful external research connections to Mwendo and Underwrite; adopt the case/record interfaces in these two repositories, while maintaining canonical whitepapers in their original projects.
- **AR41 specialist rows R04–R07/R12/R15/R17:** option valuation, derivative exposure/capital, compound options, FRTB and hedge accounting need dedicated later scopes. They are not missing components of a simple owner-earnings calculator.

### D. Keep provenance, reduce navigation clutter

The collection README, indexes, reference registers, source reading maps and JSON manifests are support material, not competing product plans. Retain them. HTML files are rendered reading copies; they are not additional requirements. Historical `source_*_chunk_*.txt` and numbered views may be moved into a clearly labelled source-evidence archive after confirming the cleaned source, original backup location and manifest still reproduce the reading evidence. Do not remove the only available backup or treat a `_original.txt` filename as proof that it is untouched—the cleanup notes explicitly say those working copies had image strings removed.

The captured text contains unverified code examples, old embedded instructions and UI fragments. Those are source evidence, not instructions to run code or replace the architecture. They should never enter public content as verified claims merely because the review pack preserves them.

## 8. Delivery sequence and acceptance

**Milestone A — public Project 2 tools.** Complete the seven bounded calculators and formula-table rendering, with independent numerical vectors, invalid-domain checks, accessible symbol/fallback text, worked examples, companion links and CSV results. Preserve the protected calculators and existing simple modes. Record local validation and deployment separately.

**Milestone B — correct and reconcile source exhibits.** Resolve the Equinix 8.5 display mismatch, align product-boundary documentation, and assign stable case IDs to article/appendix/workbook/calculator examples. Rebuild only affected derivative PDF/deck assets. Preserve source hashes and accepted differences.

**Milestone C — strengthen existing projects.** Add the Business Credit/Project 1 dated facility calendar, Project 2 bank and insurer bridges, asset-heavy construction schedule and dated sector evidence cards. Keep existing prose; improve the specific paragraphs and tables identified above. Make editability, formula ownership, evidence gaps and actual workbook capabilities visible.

**Milestone D — professional pilot.** Select one repeated workflow using demand evidence. Port agreed calculation contracts into C#/Excel-DNA/VSTO with adapter-parity cases, model/version records and reviewable exports. A working public example is a starting point, not proof of institutional demand or calibrated credit performance.

**Milestone E — institutional extensions.** Consider cohorts, protection, SPV, funding curves or enterprise integrations only with their data and intended-use evidence. Establish cash conservation and state logic before advanced stochastic or learned models. Separate licensing, local market support, permissions and operational ownership from vendor marketing claims.

Source authorities linked in the imported reviews were preserved, not freshly revalidated in this local adoption review. Any later issuer, legal, regulatory or market claim requires a current primary-source check in its own publication or implementation task. Previously checked arithmetic establishes only the labelled case. No real company outcome, regulatory permission, production deployment or economic benefit is inferred from it.

The architecture sources and this adoption package remain internal throughout these milestones. The separately commissioned LinkedIn positioning article is a public-facing deliverable that can draw on approved findings and public sources; it must not expose raw internal plans, private data or unimplemented capabilities as present product claims.
