# Verification record

Verified on 8 September 2026. Research observations retain the 7 September 2026 cutoff.

## Manuscripts

| Part | Body words | Prose paragraphs | Paragraph range | Cited sources | Figures |
|---|---:|---:|---:|---:|---:|
| 1 | 3,564 | 28 | 116–132 | 8 | 2 |
| 2 | 3,627 | 28 | 123–136 | 9 | 2 |
| 3 | 3,667 | 28 | 125–136 | 8 | 2 |
| 4 | 3,660 | 28 | 127–136 | 2 | 2 |

Each article exceeds 3,500 body words. All article prose paragraphs meet the 100–150-word range. Citation numbers resolve to each article's IEEE reference list; image files and appendix links exist. Formula appendices and references are additional material. Figures were visually inspected, including the bill cash-flow example, statement flow, DCF sensitivity, portfolio allocations, sampled risk-return comparison and simulation outcomes.

## Calculation checks

- The 91-day bill's settlement cash independently reconciles to KES 98,181.51154665, including withholding on the discount. Clean-price differences from the published auction figures are within their four-decimal display rounding.
- A zero share price suppresses yield; restoring the price restores the sourced-dividend calculation.
- The integrated forecast balance sheets reconcile to within floating-point precision. Changing a later-year growth assumption affects that year and its successors while preserving earlier forecast revenue and the balance-sheet equality.
- Independently reconstructed operating cash flows and terminal reinvestment produce DCF value KES 8.39304283190321 per share. Setting WACC equal to terminal growth suppresses the valuation; restoring the assumption restores the result.
- The assumed covariance matrix is symmetric and positive definite. The Balanced allocation's volatility reconciles to approximately 13.555307%. Overallocated weights trigger constraint counts, which return to zero after restoration.
- The deterministic twenty-year result agrees with the closed-form annuity calculation: KES 13,324,123.24 nominal. With volatility and crisis probability set to zero, the first and last spreadsheet simulation paths match that result to less than KES 0.00001.
- Changes to the contribution default reach the final annual-plan year. Changing inflation to 8% produces the expected twenty-year price index of 1.08^{2}^{0}. Test inputs were restored before export.
- Time-weighted performance reconciles to 14.95% over three years. The calculated investor IRR discounts the dated-by-year cash-flow sequence to within KES 0.01 of zero.
- The large simulation and sampled allocation search reproduce with fixed seeds. The DCF heatmap and portfolio figures use the same documented assumptions as their workbook counterparts.

## Workbook checks

All 52 worksheets were visually reviewed through rendered worksheet panels; the native real-wealth chart was also inspected. The review led to clearer percentage formats, six-decimal covariance and variance displays, wider operating-driver labels, and wrapped units. Authoring-time formula scans reported no formula errors. The saved XLSX packages passed ZIP integrity checks, contained the intended worksheet names, and contained no cached Excel error cells. Representative edited-input checks are recorded in `workbook_verification.json`.

These checks validate the implemented relationships and the stated numerical experiments. The source register distinguishes reported observations, academic methods and educational assumptions. The simulation uses an assumed distribution and crisis process; probability estimates remain conditional on those choices. The screening directory contains 68 records with seven populated dividend examples, and the portfolio search reports sampled solutions. These scopes are preserved throughout the articles and workbooks.
