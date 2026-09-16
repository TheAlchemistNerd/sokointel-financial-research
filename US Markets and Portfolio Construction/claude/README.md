# US Markets and Portfolio Construction
### A Five-Part Series

## What this is

> **Archive status.** This folder is retained as the final Claude source edition. The unified nine-part series is the reader-facing edition. Its canonical workbook is `../US_Markets_Portfolio_Construction_Final_Workbook.xlsx`; `../WORKBOOK_LINEAGE.md` records the source file hash and the reconciliation made before release.

A five-part article series on building and maintaining a portfolio using US-listed securities, moving from market mechanics through portfolio construction, risk mathematics, and long-term maintenance. Each article is a standalone piece (~3,500+ words of body prose) with its own IEEE-numbered reference list; each also has a companion technical appendix that derives every formula and worked calculation used in the article, in enough detail for a reader to reproduce or challenge any number independently. A companion Excel workbook reproduces every calculator across all ten documents as live, editable formulas.

## Structure

```
Articles/
  Part 1 - The Market Landscape and the Building Blocks of a Portfolio.md
  Part 2 - Core Portfolio Construction.md
  Part 3 - Satellite and Thematic Exposures.md
  Part 4 - Risk Mathematics, Options Income, and Tax Treatment.md
  Part 5 - Implementation, Monitoring, and Long-Term Maintenance.md
Appendices/
  Appendix 1 - Cost, Compounding, and Withholding Mathematics.md
  Appendix 2 - Diversification and Blended-Cost Mathematics.md
  Appendix 3 - Concentration Mathematics and the Effective-N Derivation.md
  Appendix 4 - Matrix Variance, Wheel Economics, and Tax Worked Examples.md
  Appendix 5 - Sequencing, Rebalancing, and the Full Case-Study Workbook Mapping.md
Workbook/
  US_Markets_Portfolio_Construction_Workbook.xlsx
References.md   -- consolidated, deduplicated source register for the whole series
Verification.md -- what was checked, and how, before delivery
README.md       -- this file
```

## What each part covers

| Part | Title | Core content |
|---|---|---|
| 1 | The Market Landscape and the Building Blocks of a Portfolio | Major US indices and their weighting rules; ETF vs. mutual fund mechanics; open-end fund vs. Unit Investment Trust structures (using QQQ's Dec. 2025 reclassification as a case study); the layered cost stack; nonresident-alien withholding and estate-tax exposure |
| 2 | Core Portfolio Construction | The core / core-plus / core-satellite frameworks; choosing among S&P 500 vehicles; adding a bond core; two-asset diversification mathematics; a worked blended-portfolio example with conservative and growth-oriented variants |
| 3 | Satellite and Thematic Exposures | The Herfindahl-Hirschman Index and effective-N as a concentration measure; a four-fund semiconductor-ETF case study (SMH, SOXX, SOXQ, XSD); dividend-focused satellites (SCHD, Dividend Aristocrats, and the informally tracked "Dividend Kings") |
| 4 | Risk Mathematics, Options Income, and Tax Treatment | The general matrix form of portfolio variance; the options wheel strategy's mechanics, economics, and risk profile; tax treatment of options premiums, qualified dividends, wash sales, and 2026 capital-gains brackets; asset location |
| 5 | Implementation, Monitoring, and Long-Term Maintenance | Dollar-cost averaging vs. lump-sum investing; rebalancing evidence and mechanics; a monitoring checklist; sequence-of-returns risk and the current safe-withdrawal-rate debate; a full ten-year worked case study |

## How the series was built

Each article was researched independently using live web search and direct source verification (fetching primary documents, not relying on search snippets alone) rather than drawn from the raw research notes supplied at the start of this project — those notes were treated as a starting point for subject coverage, not as a source of verified fact, and several of their claims turned out to be outdated by the time of writing (see Verification.md). Every calculation shown in an article or appendix was computed programmatically and cross-checked, not worked by hand. All growth rates, volatilities, correlations, and yields used in worked examples are explicitly labelled as illustrative assumptions rather than forecasts; every expense ratio, statutory threshold, index-methodology rule, and structural fact is traced to a cited, dated primary source.

## Scope and limitations

This series is educational and general in nature. It is not personalized investment, tax, or legal advice, and nothing in it should be read as a recommendation for any specific reader's allocation, satellite selection, or withdrawal rate — those depend on individual circumstances (risk tolerance, time horizon, tax situation, account access) the series cannot know. Federal US tax treatment is covered; state-level taxation is explicitly out of scope given how much it varies by jurisdiction. Options-trading content in Part 4 is descriptive of a named, publicly documented strategy's mechanics and risk profile, not a recommendation to use it.

## Related series

This project sits alongside two related series also covering personal-finance topics for a similar audience: *Kenyan Equities and Company Analysis* (a four-part series on the Nairobi Securities Exchange) and *International Investing and Diaspora Finance* (covering non-US-domiciled fund structures for cross-border investors). Part 1 of this series references that second project directly where the topics overlap (non-US-resident access to US-listed funds) rather than duplicating that content here.
