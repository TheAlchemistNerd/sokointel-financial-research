# US Markets Workbook Lineage

## Canonical workbook

`US_Markets_Portfolio_Construction_Final_Workbook.xlsx` is the sole reader-facing workbook for the unified nine-part series. It is derived from the final Claude handoff workbook, reconciled on 15 September 2026 so that the ten-year case study applies the 0.095% blended expense ratio to the 8.00% gross return before calculating monthly balances. On 16 September 2026, its presentation was refactored so every worksheet is visibly mapped to Parts 01 through 09 while preserving the underlying calculation scope.

## Retired local workbook identities

| Former location | SHA-256 before retirement | Role retained in the source record | Reason superseded |
| --- | --- | --- | --- |
| `US_Markets_Portfolio_Construction_Workbook.xlsx` | `b3f7c3a342b529b765983c7d7698ddbe7babfce3aeb2448cc4dddc7c37eef573` | Early root model with allocation, risk, fee, wheel, rebalancing and scenario views | Repeated schedules contained stored values rather than complete formula propagation. |
| `US_Markets_Portfolio_Construction_Five_Part_Series_FINAL/US_Markets_Portfolio_Construction_Workbook.xlsx` | `1ac9ea8dfe63615ec0ce0997b5e97ed50621c6fbfdc8ed43201960b9046ecb14` | Formula-driven predecessor for the original five-part series | Narrower nine-sheet scope without the final tax and maintenance calculators. |
| `outputs/us-markets-final-20260913/US_Markets_Portfolio_Construction_Final_Workbook.xlsx` | `e61458955cbb054c7c650252293ef9b81cc8a563385486c883c30cdf0683a120` | Earlier 13-sheet Sokointel export | Some sensitivity, sequence and case-study rows were stored values rather than live formulas. |
| `claude/US_Markets_Portfolio_Construction_Workbook.xlsx` | `09a556d6d1e4497f18def0a021ee3d23642df68baa63952d84e3dfeb1f14cd65` | Final Claude handoff calculation source | Reconciled and promoted into the canonical workbook after correcting the unused case-study expense-ratio input. |

## Traceability controls

The final Claude articles, appendices, `build_workbook.py`, this ledger and the Git history retain the source trace. The canonical workbook uses the same sheet-level calculation scope as the final handoff. The presentation refactor renamed and regrouped the worksheets, added the nine-part guide and retained the reconciled formulas and outputs.

## Canonical release record

Reconciled release date: 16 September 2026.

- Reconciled pre-refactor SHA-256: `2684f8a7c6c5cd93bdce93a6bc956668778663679eaaa789a6c29e766aa8eb4e`
- Nine-part presentation release SHA-256: `5a040bdadf9c5682f5370a882c44aec18bb6359ea96bcd8121b634d35620ab38`
- Replaced historic export: `outputs/us-markets-final-20260913/US_Markets_Portfolio_Construction_Final_Workbook.xlsx`
- Deployed Sokointel asset: `content/assets/us-markets-portfolio-construction-final.xlsx` in the Sokointel repository

The canonical file, historic export replacement and deployed asset share the nine-part presentation release hash. The release formula applies the linked 0.095% blended expense ratio before calculating the 120 monthly case-study balances. At the base assumptions, month 120 remains `$196,510.08`.
