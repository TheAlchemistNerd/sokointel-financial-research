# Formula rendering verification — 25 September 2026

These are actual local-browser and document-export evidence files from website main commit 81099e8 plus the pending formula rendering correction. They do not claim a production deployment. Earlier evidence remains unchanged.

`manifest.json` records per-page timestamps, URLs, viewport, actual illustrative input values, equation counts and screenshot filenames. Full-page images retain the full calculator; `results` images show the worked output. DCF `forecast` and `sensitivity` images cover the newly expanded sections. No visitor data was entered.

The four business tools render ten equations through the existing MathJax 3.2.2 loader. Definitions remain visible. `mobile-verification.json` records the 390 × 844 viewport check: the page does not overflow horizontally; wide equations scroll within their own box. `credit-detailed-mobile-formulas.png` shows the resulting narrow layout.

`equation-export-sample.md` is a separate fixture assembled from those ten formula/definition pairs and one literal Unicode example. Pandoc produced ten native Office Math equations in the DOCX. The existing Word PDF converter produced two pages; both were rasterized and visually checked. Fractions, sums, subscripts and Unicode display correctly. See `equation-export-report.json`, `equation-export-sample.pdf`, and `equation-export-page-1.png` / `equation-export-page-2.png`.

The PDF fixture tests Markdown → native-equation DOCX → Word PDF. It is not a branded production edition and bypasses publication front matter. LibreOffice is not installed on this machine, so its rendering was not exercised. Published PDFs were not regenerated.

Focused suite: 29 tests passed across `apps.calculators.test_business_formula_rendering`, `apps.calculators.test_business_tools`, `apps.core.test_edition_math`, and `apps.core.test_markdown`, using the isolated `milestone_test_settings` SQLite settings.
