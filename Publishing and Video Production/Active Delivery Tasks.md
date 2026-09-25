# Active SokoIntel delivery tasks

Updated 25 September 2026. This is the coordinated task breakdown requested by the user. A source file, generated artifact, reviewed artifact, Git push, Railway deployment and database publication are distinct states.

## Work assignments

| ID | Workstream and owner | Current state | Concrete completion check |
| --- | --- | --- | --- |
| PUB-01 | Publication agent: four new projects and public counts | Railway operator audit confirms deployed `52931e8` and bundle 11/41; database/public 7/25 with exactly 16 articles/four series missing. Safe import commands supplied; post-import visibility pending | Each of the four new series and its articles is published in the editorial database; live library shows all 41 articles and 11 series. If Railway access is unavailable, provide a verified audit command and exact controlled import steps rather than claiming publication |
| MATH-01 | Formula agent: calculator and PDF equation rendering | Implemented and verified: ten MathJax equations, visible definitions and mobile containment; native-equation DOCX/PDF fixture checked. Existing published PDFs remain unchanged | New business-tool equations render through existing MathJax, definitions remain visible and fallback is readable; PDF conversion preserves mathematical structure. International Investing and Diaspora Finance remains Unicode |
| PPT-01 | Presentation agent: episode decks and evidence | Complete: 41 editable decks / 458 slides; structural and native PowerPoint checks passed for all 41. Representative renders reviewed; all 15 source-workbook hashes match. Videos remain unrecorded | One editable PowerPoint per article/video episode, 41 total, with episode-specific narrative, actual workbook evidence, relevant calculator screenshots, source/capture notes and a master index. Generated and visually reviewed status recorded separately |
| MEM-01 | Coordinator: membership launch readiness | Code committed and pushed; production configuration/acceptance remains open | Confirm migrations 0010/0011, verified transactional sender and real signup/reset delivery, then selected payment provider, active pricing and entitlement/download checks |
| PDF-01 | Coordinator: branded-edition rollout boundary | Sample accepted; full historical/new-project regeneration not complete | Retain the approved sample and worker design. Do not enqueue a full regeneration as a side effect of catalog repair. Resume batches with explicit count, result and visual-review records when this workstream is resumed |

## Four projects to publish

| Project folder under Owner's Earning | Series code | Articles |
| --- | --- | ---: |
| Project 1 - MSMEs and Small Businesses | OE-MSME | 5 |
| Project 2 - Listed Companies and Valuation | OE-VALUATION | 5 |
| Project 3 - Failure Retrospectives and Warning Systems | OE-FAILURE | 3 |
| What Startup Funding Figures Actually Measure | STARTUP-FUNDING | 3 |
| New-project total | | 16 |

The platform handoff is `docs/Catalog Publication Check.md`. After deploying the audit command, run `python manage.py audit_research_catalog` in the Railway web-service Console. If the bundled catalog is correct and rows are missing, follow the process-only automation-disabled import in that runbook. A plain import preserves existing editorial revisions and publication flags. Do not use broad `--update` to repair missing rows.

The original seven series contain 25 articles. Adding these four produces 11 series and 41 articles. Updating source files alone does not import or publish editorial database records. A database schema migration does not load the article catalog.

## Presentation acceptance

Use `Presentation Assets/Decks/<series>/` for the decks and keep a master index identifying each episode, its article, deck path, slide count, workbook/sheet/range, calculator URL/scenario, evidence status and review status. Source guides and the older `Slide and Research Question Index.csv` provide the starting storyboard. A skeleton, screenshot folder or PDF range export must not be counted as a finished deck.

Each episode should develop its own question and worked example. Keep body text, assumptions, units, definitions, scenario changes and takeaways readable. Put detailed citations and recording instructions in speaker notes. Embed real captures of the source workbook or calculator; distinguish fictional demonstrations from issuer data and legal/corporate evidence. The deck remains an editable production asset, not a recorded or published video.

## Membership operator handoff

The platform repository contains `docs/Public Membership Railway Setup.md`. Deploy the latest platform code, then use the web service Console for `python manage.py migrate` and `python manage.py showmigrations core`. Both `0010_accountemailverification` and `0011_accountrequestlimit` should show applied. The worker uses the same database and does not need a second migration run.

Configure transactional email and a provider-verified sender privately in Railway, then test public signup, verification and password reset using an inbox controlled by the operator. Set `ACCOUNT_SIGNUP_ENABLED=True` for launch after testing. Billing remains a separate gate: configure the chosen provider secrets/webhook, active plan/price and `PAYMENTS_ENABLED` only with verified payment and download behaviour. No secret should be copied into a deck, research document or Git commit. The document worker does not need membership payment secrets.

## Preserved scope and milestones

- Preserve single-asset DCA, portfolio DCA, compounding/cash-flow calculators and the International/Diaspora Unicode source notation.
- The four new free calculators and additive DCF presentation were pushed as platform `81099e8`; the reconciliation/recording handoff was pushed as research `831b6a2`.
- Existing source articles, spreadsheets, rough work and source traces remain intact.
- The coordinator reviews diffs, saves a detailed untracked commit-message file, commits and pushes both repositories at meaningful coordinated milestones. Do not include unrelated review files or deletions.
- Report production actions separately from local tests and generated assets. Do not imply that publication, real email delivery, a payment, a PDF batch or a video occurred without direct evidence.


## Railway operator audit received

The user supplied a read-only audit from revision `52931e8`: bundle 11 series/41 articles, database/public 7 series/25 articles, all 16 new articles and four series missing, no hidden records and no existing source differences. The deployed code is current; the catalog import is missing. The operator was given the automation-disabled migration and plain import commands, followed by another audit. Completion has not yet been reported. The existing edition queue contains 42 queued/32 failed jobs; publication repair is not a retry or regeneration request.


## Presentation package delivered

[Master Index](<Presentation Assets/Master Index.md>) links all 41 PowerPoints. The package includes 458 slides, actual workbook/web captures, formula definitions, recording notes, source references and an editable scenario for each episode. All 41 pass ZIP/slide/image/notes checks and native PowerPoint opening/text-fit checks. Representative contact sheets were visually reviewed; the manifest distinguishes those decks from native-bounds-only checks. Independent verification found no differences in the 15 source-workbook hashes.

The package README documents the inherited simple-DCA yield-formatting discrepancy and the unresolved BAT operating-cash source difference. Neither protected calculator code nor authored source workbooks/articles was changed to hide these issues. New web captures identify their local-preview origin; video recording and public article publication are separate states.
