# Verification
### US Markets and Portfolio Construction (Five-Part Series)

This document records what was checked before delivery, and what those checks found — including two substantive corrections made mid-project as a direct result of verification.

## 1. Word counts

Every article's body prose (excluding headings, tables, equations, and the reference list) was measured programmatically and confirmed to clear the 3,500-word floor:

| Part | Word count |
|---|---|
| Part 1 | 3,611 |
| Part 2 | 3,623 |
| Part 3 | 3,620 |
| Part 4 | 3,510 |
| Part 5 | 3,510 |

## 2. Reference-list integrity

Every in-text citation number in every article was checked against that article's own reference list, in both directions: every number cited in the body has a matching numbered definition, and every numbered definition is actually cited at least once in the body. All five articles passed with no missing or unused references (15, 11, 9, 10, and 7 references respectively, none orphaned).

## 3. Source verification standard

Every factual claim requiring a citation was traced to a source located through this project's own live web search during this project, not carried over from the raw research notes supplied at the outset. Where feasible, the primary source itself (the issuer's own fund page or fact sheet, the index provider's own methodology document, the relevant IRS publication or revenue procedure, the SEC's own investor bulletin) was directly fetched and read in full — not inferred from a search-result snippet — before being cited. Secondary sources (financial-media coverage, third-party ETF screeners) were used only where no equivalent primary source exists (for example, corroborating a specific historical transition date) or as supporting confirmation alongside a primary source, and are labelled as such in References.md.

## 4. Independent arithmetic re-verification

Twelve headline figures spanning all five parts were recomputed from scratch, independently of the calculations used to draft the articles, and checked against the published figures:

| Figure | Recomputed value | Published value | Result |
|---|---|---|---|
| SPYM 30-year value ($10,000, 8% gross, 0.02% ER) | $100,069.03 | $100,069.03 | Match |
| QQQ 30-year value (0.18% ER) | $95,714.96 | $95,714.96 | Match |
| NRA withholding gap, no-treaty vs. 15% treaty | $19.50 | $19.50 | Match |
| Net US estate tax at $150,000 US-situs estate | $25,800 | $25,800 | Match |
| 70/30 stock/bond portfolio SD (ρ = 0.10) | 11.52% | 11.52% | Match |
| Blended ER, worked $50,000 core-satellite portfolio | 0.0673% | 0.0673% | Match |
| Effective N, 30-holding equal-weight fund | 30.0 | 30.0 | Match |
| Cash-secured put collateral ($90 strike) | $9,000 | $9,000 | Match |
| CSP breakeven if assigned | $88.00 | $88.00 | Match |
| Qualified vs. ordinary dividend tax gap ($1,000, 15% vs. 24%) | $90.00 | $90.00 | Match |
| Sequence-of-returns gap (10-year, identical average return) | $229,197.12 | $229,197.12 | Match |
| Ten-year case-study ending balance | $198,008.39 | $198,008.39 | Match |

All twelve checks passed. The full derivations behind each figure are in the corresponding appendix.

## 5. Companion workbook

> **Reconciliation note.** This verification note describes the archived source workbook. Its case-study expense-ratio cell was linked to the blended-cost sheet, but the source monthly-return formula did not apply that input. The canonical release corrects that relationship and records the replacement in `../WORKBOOK_LINEAGE.md`.

The workbook (`US_Markets_Portfolio_Construction_Workbook.xlsx`) contains 13 sheets (a Guide plus 12 calculators covering all five parts) built entirely from live formulas — no calculation is a hard-coded result. The workbook was recalculated with LibreOffice after every sheet was added; the final recalculation reports 582 formulas evaluated with zero errors. Spot-checks of recalculated cell values against the corresponding article and appendix tables (documented during construction) confirmed exact matches throughout, including a cross-sheet reference (the ten-year case study pulls its expense-ratio assumption live from the blended-ER sheet rather than duplicating the figure).

## 6. Substantive corrections found during verification

Two errors were caught and corrected during this project's own research process, both illustrating the same underlying risk: a fact that was accurate when a source was written can become outdated, while the source's name, URL, or reputation for authority persists unchanged.

**QQQ's legal structure.** The user-supplied research notes, and a considerable amount of older third-party commentary still in circulation, describe QQQ as a Unit Investment Trust with a 0.20% expense ratio, structurally distinct from the open-end QQQM. Direct verification against Invesco's own disclosures found that QQQ was reclassified from a UIT to an open-end fund effective after market close on December 19, 2025, with its expense ratio cut to 0.18% as part of the same change. This is now correctly reflected throughout Part 1 and is used there as a worked example of why the verification habit matters, rather than silently corrected without comment.

**SOXX's tracked index.** During research for Part 3, a generic web search for Invesco's SOXQ surfaced a claim that iShares' SOXX — despite its product name and URL still referencing "PHLX Semiconductor ETF" — has tracked the NYSE Semiconductor Index (also called the ICE Semiconductor Index) since June 21, 2021, rather than the PHLX Semiconductor Sector Index its name implies. This directly contradicted an earlier draft of Part 3, which had described SOXX and SOXQ as tracking the same underlying index. The draft was corrected before delivery: SOXQ, not SOXX, is the fund that actually tracks the PHLX Semiconductor Sector Index today, and Part 3's discussion, worked example, and reference list were all revised to reflect this — the corrected version argues, if anything, more strongly for SOXQ over SOXX for an investor who specifically wants SOX-index exposure, since the two funds turn out not to be close substitutes for the same underlying benchmark at all.

Both corrections are documented here rather than silently fixed, on the view that showing where verification changed the substance of the analysis is more useful to a reader than a series that only reports what turned out to be right the first time.

## 7. What this verification does not cover

This process checked internal consistency, source traceability, and arithmetic correctness. It did not, and cannot, guarantee that every cited figure remains current at the moment a reader opens this series — expense ratios, AUM, statutory thresholds, and even index methodologies change over time, sometimes (as with QQQ and SOXX) without a corresponding change in a fund's name or ticker. Every reference entry carries an "Accessed" date for exactly this reason: it marks the point at which the cited claim was last confirmed against its source, not a permanent guarantee of currency. Rechecking a load-bearing fact against the cited primary source before relying on it in a real decision is the same habit this series recommends to its own readers in Part 5's closing section, and it applies to this series' own claims as much as to any fund comparison made along the way.
