# Episode PowerPoint production package

This package contains one editable PowerPoint per article/video episode: 41 decks across 11 series. The [Master Index](<Master Index.md>) links every file. [Master Index.csv](<Master Index.csv>) supports operational tracking, and [episode-manifest.json](episode-manifest.json) contains slide plans, source links, workbook paths/ranges/hashes, screenshot provenance, file hashes and QA results.

The decks are presentation deliverables, not recorded or published videos. Each contains episode-specific questions, glossary/units, explanatory slides, a worked relationship, a changed-assumption or changed-evidence comparison, an answer and a concrete next record. Actual workbook captures and relevant calculator captures are embedded. Speaker notes supply recording context and the fuller source record. Text, shapes and layout are editable; evidence screenshots remain images so their source appearance is preserved. Equations use editable mathematical Unicode/Cambria Math notation, and the captured calculator equations retain their rendered MathJax notation. No raw TeX is visible on slides.

## Source and scope

The next delivery stage is documented in the [Private Presentations and Staff Production Guides plan](<../../platform_operations_plans/07_sokointel_private_presentations_and_staff_guides.md>): versioned private storage, PowerPoint/PDF pairs, document records, internal guide pages and role-checked downloads. These integrations are planned; bucket configuration alone does not publish this package. Presentation production remains separate from the reading-PDF worker.

- `content/source-material.json` is a portable source snapshot derived from the 41-article catalog and the existing production storyboard CSV. It retains the catalog hash, article sections, references, exact workbook evidence and extracted values. The episode briefs are in `content/existing-episodes.json`, `msme.json`, `valuation-root.json`, `failure.json` and `startup-funding.json`.
- `Evidence/Workbooks` contains the actual Microsoft Excel read-only PDF exports and trimmed PNG renderings. Row and column headings are retained. These are not fabricated spreadsheet pictures. Source workbooks were not saved or changed. The original capture manifest remains preserved.
- The additional BAT capture, `OE-VALUATION-06-BAT`, shows `'NSE Casebook'!C11:F11`, the FY2025 net-revenue record. It replaces the unrelated Equity-row capture in that episode without deleting historical evidence. Its separate manifest records the unchanged source SHA-256.
- `Evidence/Web/capture-manifest.json` describes the older saved production-page captures. `Evidence/Web/20260925-formula-rendering/manifest.json` describes the new local-preview captures, with URLs, timestamps, viewport and actual form inputs. The latter do not prove live deployment. Decks visibly distinguish local-preview evidence.
- International Investing and Diaspora Finance retains Unicode notation. Its USMPC workbook screenshots are explicitly labelled companion teaching bridges, not reconstructions of the article cases. The leadership succession capture is labelled the same way.
- Dated issuer facts, fictional operating cases, analyst stresses and unresolved evidence remain separate. A missing maintenance split, legal recipient, receipt amount or recovery value is not filled with zero.

## Known source and tool issues

**Inherited DCA percentage display.** The saved single-asset DCA page shows `0.01%` for annual net income of KES 1,015.5093 on KES 100,000 cash. The correct percentage is approximately **1.02%**. `dca-dividend-table-crop.png` is an exact crop of the table, excluding that erroneous card; it does not retouch the screenshot. The episode visibly supplies the arithmetic and says the captured page formatting is under review. The original capture and protected calculator are unchanged.

**BAT operating-cash reconciliation.** Part 6 reports KES 6,633.154m while the Part 10/casebook record shows KES 6,642m. This unresolved source-line discrepancy is not silently reconciled. The valuation briefs omit that measure and the replacement BAT crop shows net revenue only. The complete original source snapshot remains available for audit.

**Calculator boundaries.** The DCA portfolio page demonstrates target-weight, purchase-cost and whole-share mechanics; it does not calculate HHI, covariance or stress losses. Those demonstrations stay in the workbook. The compounding explorer demonstrates constant-return contributions and payment timing, not sequence-of-returns withdrawals or stochastic pension outcomes. Generic FCFF/WACC DCF is not used as a bank/insurer model or as a direct substitution for after-interest owner earnings. Detailed credit distinguishes a late customer receipt from an explicitly extended loan tenor.

**Canonical article links.** New article URLs identify the intended catalog records; some may return 404 until the separate import/deployment is completed. Generating these decks does not publish articles or YouTube videos. Source-date refresh and final narration/caption review remain recording tasks.

## Rebuild

Run from the financial-material repository root. The bundled dependencies include Python with `pypdfium2`, `pypdf`, `Pillow`, `openpyxl`, `lxml`, and Node with `pptxgenjs` and `sharp`. Obtain current runtime paths from the Codex workspace-dependencies tool. `CODEX_NODE_MODULES` can override the generator's default bundled Node-module directory.

With the saved source snapshot and evidence, the minimum reproducible build is:

```powershell
& $python -X utf8 'Publishing and Video Production/Presentation Assets/scripts/curate_existing_episodes.py'
& $python -X utf8 'Publishing and Video Production/Presentation Assets/scripts/finalize_evidence.py'
& $node 'Publishing and Video Production/Presentation Assets/scripts/build_episode_decks.cjs'
& $python -X utf8 'Publishing and Video Production/Presentation Assets/scripts/validate_episode_decks.py'
& 'Publishing and Video Production/Presentation Assets/scripts/native_powerpoint_qa.ps1'
& $python -X utf8 'Publishing and Video Production/Presentation Assets/scripts/make_delivery_index.py'
```

Set `$python` and `$node` to the bundled executable paths. Office COM validation needs a normal Windows process permission context; the restricted sandbox can return a generic “could not open the file” even for a valid deck. Native QA opens the deck read-only, closes only presentations it opened, and records possible text overflow. It does not edit the source workbooks or article files. Add `-EpisodeIds 'OE-MSME-01' -Render` to export a representative deck to PNG for visual review.

To rebuild the source snapshot from the current catalog and original exports, run `prepare_deck_sources.py` first. It expects the sibling website repository's `content/catalog.json`; the saved snapshot lets ordinary deck rebuilds proceed without that external file. Run `finalize_evidence.py` afterward to apply the additional BAT source selection and exact DCA table crop. `capture_bat_evidence.ps1` can reproduce the additional read-only Excel PDF from the source workbook and verifies its hash before/after export.

`build_episode_decks.cjs` accepts episode IDs as positional arguments for a targeted rebuild. Any rebuild invalidates earlier file-hash QA, so rerun structural validation and the relevant native checks before updating the manifest. A full native report is `Review/native-qa.json`; representative exports are under `Review/Native`.

## Delivery files and QA boundaries

Keep `Decks`, `content`, `scripts`, the evidence files used by the manifest, the two indexes, this README and `episode-manifest.json`. Compact native-QA reports and contact sheets are useful review evidence. The pre-existing `.build-20260923/node_modules` and other temporary build files are not deliverables and are not needed by the generator. Full-resolution review renders are optional working files rather than source evidence.

Structural validation checks ZIP integrity, actual slide counts, embedded images, recording notes on every slide, raw TeX escapes and Unicode replacement characters. Native PowerPoint checks actual file opening and text bounds; representative images are reviewed separately. These checks do not assert that every source claim is freshly reverified on recording day or that every possible commercial, tax or legal circumstance fits the teaching case.
