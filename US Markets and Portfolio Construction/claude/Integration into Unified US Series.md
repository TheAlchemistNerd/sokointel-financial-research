# Claude material integration into the unified US series

## Decision

The US Markets and Portfolio Construction project will have one authoritative companion workbook. The existing root workbook is the current baseline. The Claude workbook builder is a formula source and extension path, not a second reader download.

The unified nine-part sequence remains progressive:

1. Market concepts and instruments.
2. Fund wrappers, execution and total cost.
3. Ownership, tax and cross-border implementation.
4. Portfolio architecture.
5. Building the broad core and measuring overlap.
6. Satellites, thematic exposure and concentration.
7. Options income as a tactical sleeve.
8. Portfolio integration, rebalancing and governance.
9. Long-term maintenance, withdrawals and review.

The five Claude articles cover the same research questions at a different grouping level. Their main prose should not become a parallel five-part reader path. Their detailed derivations, scenario tables and calculators will be used as technical appendices and workbook sheets linked to the relevant unified part.

## Article and appendix map

| Claude material | Unified destination | Treatment |
|---|---|---|
| Part 1 and Appendix 1: ETF mechanics, ownership cost, withholding and estate arithmetic | Parts 2 and 3 | Retain the cost and contribution derivations with Part 2. Retain withholding and estate calculation explanations with Part 3, subject to a current primary-source legal review. |
| Part 2 and Appendix 2: core construction, variance, correlation and blended cost | Parts 4, 5 and 8 | Use the worked core-policy variants in Part 5 and retain the variance and blended-expense-ratio derivations as the Part 8 technical appendix. |
| Part 3 and Appendix 3: HHI, effective number of holdings and satellite types | Part 6 | Retain the full HHI derivation, editable holdings logic, dividend-sleeve comparison and semiconductor discussion. |
| Part 4 and Appendix 4: matrix variance, wheel economics and tax examples | Parts 3, 7 and 8 | Keep wheel mechanics and strike sensitivity with Part 7. Keep matrix variance with Part 8. Place U.S. taxpayer-specific dividend, wash-sale and capital-gains examples in a clearly scoped tax appendix linked from Part 3. |
| Part 5 and Appendix 5: implementation, rebalancing, sequence risk and ten-year case study | Parts 8 and 9 | Place target-restoration arithmetic with Part 8. Place DCA, sequence risk, withdrawals and the full ten-year case study with Part 9. |

## Single-workbook design

The completed workbook will consolidate overlapping sheets rather than repeat them.

| Final sheet | Combines |
|---|---|
| Guide | Reader instructions, input legend and limitations |
| Research inputs and sources | Current fund inputs, dates, source links and assumptions |
| Fund cost and fee drag | Existing Fee Drag plus Claude Part 1 cost-of-ownership sensitivity |
| Ownership tax scenarios | Nonresident withholding and estate-tax mechanics, with jurisdiction warnings |
| Allocation and blended cost | Existing Allocation plus Claude core-satellite and blended-expense-ratio work |
| Diversification | Two- and three-asset covariance and correlation sensitivity |
| Concentration | Paste-your-own holdings, HHI and effective number of holdings |
| Portfolio risk | Existing Risk Model plus four-asset matrix variance |
| Options wheel | Existing Wheel Model plus strike sensitivity and adverse scenario |
| U.S. tax scenarios | Qualified-dividend, wash-sale and capital-gain illustrations, explicitly limited to the stated tax facts |
| Rebalancing | Existing Rebalancing plus target-restoration trade arithmetic |
| DCA and lump sum | Scenario comparison with clearly illustrative paths |
| Sequencing and case study | Sequence-of-returns mechanics, withdrawal timing and ten-year accumulation |

## Builder assessment, 13 September 2026

`build_workbook.py` currently builds nine sheets through `P4 - Tax Calculators`. Its guide lists four Part 5 sheets, but their creation code is not present and the output path is specific to Claude's temporary environment. It must be completed, redirected to the project’s workbook path, recalculated and checked before its formulas replace or extend the baseline workbook.

The tax content will be published only after review against current primary tax sources. All examples must remain illustrative, identify the assumed taxpayer status, and avoid presenting a generic tax calculation as personalised advice.