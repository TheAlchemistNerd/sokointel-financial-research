# Video guides, calculators and formula definitions — audit

Review date: 25 September 2026. Scope: the seven established research series (25 articles), four new projects (16 articles), seven existing public calculator pages, and the episode-by-episode presentation package. The presentation master index is the authoritative file inventory; this document records the editorial and tool gaps that motivated it.

## Existing guide depth

Word counts below are approximate source-guide counts, not a quality score. A long guide can still omit the exact calculation or recording steps.

| Research series | Episodes | Existing guide assessment | Recording work required |
| --- | ---: | --- | --- |
| African Markets and Business Credit / Making Business Credit Work | 2 | Strongest worked-demo specification; about 3,776 words, with named workbook ranges and entity-resolution updates | Capture the stated ranges, show related-party exclusions and connect evidence to credit interpretation |
| International Investing and Diaspora Finance | 3 | About 5,556 words and structured storyboards; repeated generic narration and incomplete range-level instructions | Name source cells, demonstrate transfer/FX costs, separate gross and net return assumptions |
| Kenyan Equities and Company Analysis | 4 | About 7,155 words; strong article sequence, incomplete workbook recording coordinates | Define FCFF versus equity cash flows; reconcile DCF inputs and terminal value; show source evidence |
| Kenyan Tax and Household Finance | 4 | About 7,342 words; broad storyboards, some repeated mechanism language | Tie demonstrations to workbook cells; show tax period/jurisdiction and mortgage timing explicitly |
| NSE Dividend Growth | 2 | About 880 words: useful timed outline, shallow recording instructions | Add precise workbook ranges and demonstrations of costs, weights, rounding and rotation using the existing planner |
| US Markets and Portfolio Construction | 9 | About 995 words over nine episodes: the shallowest per-episode outline among the multi-part series | Expand each episode into its own worked case, calculation, scenario and answer sequence |
| Leadership / Key Person Risk | 1 | About 110-word publication guide, not an actual video script | Build an episode structure, decision case, evidence and workbook demonstration |
| Owner Earnings — MSMEs | 5 | New article-specific guide with workbook references | Preserve the normalised earnings bridge, actual cash budget and uncertain receipt distinction |
| Owner Earnings — Listed Companies | 5 | New article-specific guide; public-filing evidence and scenario workbooks | Keep source dates and adjustments visible; distinguish illustrative profiles from completed issuer valuations |
| Owner Earnings — Failure Retrospectives | 3 | New guide with case evidence and warning-system models | Separate documented events, hypotheses and illustrative cash schedules; do not manufacture historical company ratios |
| What Startup Funding Figures Actually Measure | 3 | New guide covering denominators, instruments and outcomes | Show dataset scope and date vectors; distinguish announced commitments, disbursement, exposure and loss |

A finished PPTX is an editable presentation asset. It is not a recorded video, final narration performance, caption file or published YouTube episode. Those statuses must remain separate in the index.

## Existing calculators and coverage

All seven public pages were checked in a fresh anonymous browser on 25 September 2026. GET and normal form POST returned HTTP 200, with no visible error alert, for the captured scenarios. This does not exclude a browser-specific CSRF failure or a different invalid-input case. `Presentation Assets/Evidence/Web/capture-manifest.json` records URLs, capture timestamps, inputs, results and image names.

| Tool | Already available | Under-represented in guides / presentation opportunity |
| --- | --- | --- |
| Compounding and cash-flow explorer | Lump sum, ordinary/due annuities, sinking fund, perpetuity and inflation views | Payment timing, real-versus-nominal outputs and the discount/growth boundary deserve explicit demonstrations |
| Simple DCA | Compatible single-counter planning mode | Keep its dividend estimate distinction visible: allocation/yield estimate versus dividend on rounded purchased shares |
| Portfolio DCA | Multiple holdings, explicit weights, order costs, rotation, whole-share purchases and income | Existing NSE video outline predates much of this depth; demonstrate the existing tool without refactoring it |
| Business credit cost planner | Principal, days, simple interest, fee and cost comparison | Evidence quality, collection delay, cash conversion, facility structure and repayment capacity need deeper tools |
| Global funding planner | Transfer, conversion and dealing costs plus net-return assumption | Show the fee sequence with a single currency and separate it from actual exchange-rate risk |
| Mortgage repayment | Amortisation, extra repayment, balance, interest savings | Pair the web schedule with the household affordability workbook; do not imply the repayment is total housing cost |
| DCF value explorer | Five-year growth model, terminal value, net debt and per-share bridge | Explain cash-flow claim, terminal dependence and sensitivity; banks/insurers require different models |

The library has six main tool cards: the simple DCA mode remains reachable through the DCA navigation. A missing main card is not a missing calculator.

## Are formula symbols defined on the calculator itself?

Partially. The pages have explanatory prose and meaningful input labels. They do not consistently provide a complete symbol-by-symbol dictionary next to the formula. Readers should not have to find an appendix to know what a displayed symbol means. The appendix is appropriate for derivations and extensions.

| Calculator | Local formula support now | Symbols / distinctions to make explicit in future authorised edits |
| --- | --- | --- |
| Simple DCA | Plain-language explanations | C cash; c cost rate; I securities budget; m months; w weight as a fraction; T monthly target; P price; N whole shares; d annual dividend/share; tau withholding; D annual income |
| Portfolio DCA | Budget and cumulative-target prose | B budget; R reserve; i holding; t month; A available order budget; S total shares; all rates as fractions. With fixed/minimum fees, cost/share depends on quantity: the displayed affordability expression is implicit, not a general closed-form solution |
| Compounding/cash flow | Rate conversion and timing prose, zero-rate treatment | PV, FV, PMT, i periodic rate, r effective annual rate, m frequency, n periods, t years, G target, C1 next-period cash flow, g growth |
| Business credit | Interest and fee prose | P principal, r annual rate, d days, I interest, F fee; distinguish principal-based annualised cost from a cash-flow-based annual yield/APR |
| Global funding | Cost sequence prose | S starting capital, T fixed transfer cost, X conversion cost, D dealing cost, A0 invested amount, t years, r_net net return; form percentages converted to cash only once |
| Mortgage | P, n and i are identified in prose | PMT, Bk and k; nominal annual rate/12; extra payment and last smaller payment; zero-rate branch |
| DCF | Enterprise/equity bridge prose | FCF must be unlevered FCFF in this enterprise model; r is its discount rate, t year, TV terminal value, g terminal growth; TV5=FCF5(1+g)/(r-g); net debt/share-count conventions |

**User preservation instruction, 25 September 2026:** do not change the simple DCA, portfolio DCA or compounding/cash-flow calculators. This audit does not authorise editing those tools. Explanatory slides can define their existing symbols without changing the website.

## Proposed next free tools

The user confirmed Project 1 (MSMEs) and Project 3 (failure analysis), alongside Making Business Credit Work. See `Free Calculator Development Roadmap.md` for the detailed scope. Project 2 is not the requested new-tool priority. Retain the existing DCF while assessing a clearly labelled enhancement separately.

Priority gaps are an evidence-adjusted credit/cash-cycle planner, an MSME owner-earnings and distribution bridge, an editable 13-week liquidity schedule, and a failure-analysis stress model. These are not yet implemented public calculators. Their workbooks already contain richer analytical material, and that is the starting point for specification and reconciliation tests.

## Production evidence rules

Use a readable crop of the real workbook or webpage. The source workbook, sheet, range, capture date and input scenario belong in the slide notes and index. The illustrative DCA capture uses the earlier project-discussion prices, not current market quotes. A full page may be retained as evidence but should not be shrunk into an unreadable slide.

Do not fill unavailable workbook cells or historical company figures with invented values. Keep synthetic worked cases labelled. If a rendering engine cannot display a workbook correctly, record that limitation and use a verified alternate rendering of the actual workbook. Do not silently replace formula results.

For guides that are currently shallow, add a decision question, explicit assumptions, an observed or illustrative worked case, exact evidence references, one changed-input scenario, and direct answers. A repeated generic script across articles is not a substitute for article-specific explanation.

## Follow-up: implemented free tools - 25 September 2026

The original audit above describes the earlier seven-page inventory. The four gaps identified there now have implemented pages: detailed business credit, MSME owner earnings/cash headroom, thirteen-week cash and cash stress/warnings. Their formulae define symbols and units locally. DCF has explicit FCFF/WACC labels, a symbol dictionary, forecast and sensitivity tables. Simple credit retains its calculation and links to detailed mode. The index now has ten cards; compatible simple DCA remains separately reachable.

Use [Free Calculator Reconciliation and Recording Map](<Free Calculator Reconciliation and Recording Map.md>) for exact source cells, default results, timing differences and article-specific demonstrations. New local browser checks verified anonymous submissions and mobile containment, but are not final recording screenshots. The earlier capture manifest still describes the earlier tools and must not be relabelled as evidence for the newly added pages. Protected DCA and compounding/cash-flow pages have not been refactored. PPTX production remains a separate deferred milestone.
