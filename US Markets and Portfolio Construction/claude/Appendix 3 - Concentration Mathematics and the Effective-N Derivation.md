# Appendix 3 — Concentration Mathematics and the Effective-N Derivation
### Companion to Part 3: Satellite and Thematic Exposures

This appendix derives the Herfindahl-Hirschman Index and effective-N formulas used in Part 3, proves the equal-weight special case referenced there, and walks through a fully worked example a reader can replicate against any fund's actual published holdings.

## A3.1 Proof that equal weighting makes effective N equal the nominal holding count

For a fund holding exactly N positions at equal weight, each holding's weight is wᵢ = 1/N. Substituting into Equation 3.1:

HHI = Σᵢ₌₁ᴺ (1/N)² = N × (1/N²) = 1/N

Applying Equation 3.2:

Effective N = 1 / HHI = 1 / (1/N) = N

This confirms algebraically what Part 3 stated: for a purely equal-weighted fund, effective N always equals the nominal holding count exactly, regardless of how large N is. The table below checks this across a range of nominal holding counts:

| Nominal N (equal-weighted) | HHI | Effective N |
|---|---|---|
| 10 | 0.10000 | 10.0 |
| 25 | 0.04000 | 25.0 |
| 30 | 0.03333 | 30.0 |
| 50 | 0.02000 | 50.0 |
| 100 | 0.01000 | 100.0 |
| 500 | 0.00200 | 500.0 |

## A3.2 How a single dominant holding erodes effective N

A separate way to see the effect of concentration is to hold the nominal count fixed at 30 and vary only the size of a single dominant holding, spreading the remainder equally across the other 29:

| Top holding weight | Weight of each remaining holding | HHI | Effective N |
|---|---|---|---|
| 3.33% (equal-weight case) | 3.333% | 0.0333 | 30.0 |
| 5.00% | 3.276% | 0.0336 | 29.7 |
| 8.00% | 3.172% | 0.0356 | 28.1 |
| 10.00% | 3.103% | 0.0379 | 26.4 |
| 15.00% | 2.931% | 0.0474 | 21.1 |
| 20.00% | 2.759% | 0.0621 | 16.1 |
| 25.00% | 2.586% | 0.0819 | 12.2 |

Effective N degrades slowly at first — a top holding as large as 8% still leaves effective N above 28 out of a nominal 30 — and then considerably faster once a single holding passes roughly 15–20% of the fund, which is the range in which several real-world modified-cap-weighted sector indices, absent an explicit cap, would allow their largest constituent to reach before any capping rule intervenes. This is the mathematical justification for why index providers such as Nasdaq (for the PHLX Semiconductor Sector Index discussed in Part 3) impose explicit single-name caps: without one, a fund's effective diversification can fall well below half its nominal holding count from a single outsized constituent alone.

## A3.3 Fully worked example: computing HHI and effective N from a holdings list

The steps below use an illustrative ten-holding fund (a simplified stand-in for "the largest names plus an aggregated remainder," a common way real fact sheets summarize their long tail of smaller positions) to demonstrate the full calculation a reader can apply directly to any fund's actual published holdings spreadsheet:

**Step 1 — List each holding's weight as a decimal**, confirming they sum to 1.0000 (or 100%):
0.120, 0.100, 0.090, 0.080, 0.075, 0.070, 0.065, 0.060, 0.050, 0.290 (the final figure representing "all other holdings" combined, as many fact sheets report their long tail)

**Step 2 — Square each weight:**
0.01440, 0.01000, 0.00810, 0.00640, 0.00563, 0.00490, 0.00423, 0.00360, 0.00250, 0.08410

**Step 3 — Sum the squares to obtain HHI:**
HHI = 0.01440 + 0.01000 + 0.00810 + 0.00640 + 0.00563 + 0.00490 + 0.00423 + 0.00360 + 0.00250 + 0.08410 = 0.14385

**Step 4 — Invert to obtain effective N:**
Effective N = 1 / 0.14385 = 6.95

Despite ten line items appearing on the fact sheet, this illustrative fund behaves, from a concentration standpoint, like fewer than seven equally weighted holdings — driven mostly by the 29%-weighted "all other holdings" aggregate, which itself likely contains many additional individual names too small to move the calculation much further even if broken out individually. This is a caution worth carrying into any real-world application of this method: a fund that reports its top holdings individually and aggregates the remainder into a single "other" line will slightly overstate true concentration if that aggregate is treated as a single holding in the HHI calculation, since it actually represents many smaller positions each contributing far less than their combined weight suggests. A more precise calculation, where feasible, uses the fund's complete unaggregated holdings list rather than a fact-sheet summary — most issuers publish this as a downloadable spreadsheet alongside the summary fact sheet, as noted in the main article.

## A3.4 Reproducibility note

Every table in this appendix follows mechanically from Equations 3.1 and 3.2 applied to the stated weight distributions, computed programmatically and checked by direct substitution for the equal-weight special case in A3.1. A reader wishing to check any real fund's concentration need only obtain its current full holdings list from the issuer's own website, and apply Steps 1 through 4 above using a spreadsheet's built-in sum-of-squares capability — no specialized software is required. The companion workbook accompanying this series includes a ready-to-use HHI calculator sheet where a reader can paste in up to 50 holding weights and see HHI and effective N recalculate automatically, alongside the other calculators built for Parts 1 and 2.

---

*This appendix uses the same reference numbering as Part 3; no additional sources beyond those cited in the main article were required for the derivations above.*
