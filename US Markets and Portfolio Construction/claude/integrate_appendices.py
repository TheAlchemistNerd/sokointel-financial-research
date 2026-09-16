from pathlib import Path
import re

root = Path(r"C:\Users\Nevo\Downloads\financial material\US Markets and Portfolio Construction")
claude = root / "claude"
unified = root / "Unified Series"
appendix_dir = unified / "Appendices"
appendix_dir.mkdir(exist_ok=True)

sub_map = str.maketrans({"₀":"_0", "₁":"_1", "₂":"_2", "₃":"_3", "₄":"_4", "₅":"_5", "₆":"_6", "₇":"_7", "₈":"_8", "₉":"_9", "ᵢ":"_i", "ⱼ":"_j", "ₚ":"_p", "ₜ":"_t", "ₙ":"_n", "ᵀ":"^T", "ᴺ":"^N", "²":"^2", "³":"^3", "₋":"-", "₌":"=", "−":"-", "×":"\\times", "÷":"\\div", "Σ":"\\Sigma", "∑":"\\sum", "σ":"\\sigma", "ρ":"\\rho", "μ":"\\mu", "π":"\\pi", "√":"\\sqrt", "≤":"\\le", "≥":"\\ge", "≠":"\\ne"})
def texify(value):
    value = value.translate(sub_map)
    value = value.replace(" \\times ", " \\times ").replace("—", ",")
    value = re.sub(r"\^([0-9A-Za-z])", r"^{\1}", value)
    value = value.replace("\\sqrt0.02319", r"\\sqrt{0.02319}")
    value = value.replace("w(satellite, max)", r"w_{\\mathrm{satellite,max}}")
    return value

def clean_appendix(text, number):
    text = text.replace("—", ",")
    text = text.replace("### Companion to Part", "### Companion to the Unified Series, Part")
    def bold_formula(match):
        content = match.group(1)
        if not re.search(r"[=Σσρμπ×÷√]|HHI|Effective N|Trade for sleeve|Balance after", content):
            return match.group(0)
        equation, sep, tail = content.partition("  (Equation")
        rendered = "\\[\n" + texify(equation.strip()) + "\n\\]"
        return rendered + (" (Equation" + tail if sep else "")
    text = re.sub(r"\*\*([^*]+)\*\*", bold_formula, text)
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^(HHI|Effective N|\\sigma|Disallowed portion|V[ₜt]|Trade for sleeve|Balance after each month)\s*=", stripped):
            lines.extend(["\\[", texify(stripped), "\\]"])
        else:
            lines.append(line)
    text = "\n".join(lines) + "\n"
    header = f"<!-- Integrated from the reviewed Claude technical appendix. Formula notation has been standardised for MathJax. -->\n"
    return header + text

sources = [
    ("Appendix 1 - Cost, Compounding, and Withholding Mathematics.md", "Appendix 01 - Cost Compounding and Withholding Mathematics.md"),
    ("Appendix 2 - Diversification and Blended-Cost Mathematics.md", "Appendix 02 - Diversification and Blended-Cost Mathematics.md"),
    ("Appendix 3 - Concentration Mathematics and the Effective-N Derivation.md", "Appendix 03 - Concentration and Effective Holding Count.md"),
    ("Appendix 4 - Matrix Variance, Wheel Economics, and Tax Worked Examples.md", "Appendix 04 - Matrix Variance Options and Tax Cases.md"),
    ("Appendix 5 - Sequencing, Rebalancing, and the Full Case-Study Workbook Mapping.md", "Appendix 05 - Rebalancing Sequence Risk and Case Study.md"),
]
for index, (source_name, target_name) in enumerate(sources, 1):
    text = (claude / source_name).read_text(encoding="utf-8")
    (appendix_dir / target_name).write_text(clean_appendix(text, index), encoding="utf-8")

additions = {
"Part 01 - Understanding the Market Before Choosing a Fund.md": """\n\n## Technical companion\n\nThe cost and ownership mechanics that sit behind fund selection are derived in the [cost, compounding and withholding appendix](<Appendices/Appendix 01 - Cost Compounding and Withholding Mathematics.md>). A fund comparison begins with the market exposure, then carries the selected cost, wrapper and tax assumptions into the implementation model.\n""",
"Part 02 - Choosing the Wrapper and Understanding the Full Cost.md": """\n\n## Technical companion\n\nFor an opening investment (P), regular contribution (C), net annual return (r-e), and (n) annual periods, the recurring-contribution model uses:\n\n\\[\nFV_n = P(1+r-e)^n + C\\frac{(1+r-e)^n-1}{r-e}.\n\\]\n\nThe [cost, compounding and withholding appendix](<Appendices/Appendix 01 - Cost Compounding and Withholding Mathematics.md>) develops the assumptions and cross-checks.\n""",
"Part 03 - Ownership Tax and Cross-Border Implementation.md": """\n\n## Technical companion\n\nThe after-withholding cash distinction is:\n\n\\[\nD_{\\mathrm{net}} = D_{\\mathrm{gross}}(1-w),\n\\]\n\nwhere (w) is the applicable withholding rate. Treaty eligibility, domicile, estate exposure and reporting remain fact-specific. The [withholding mathematics appendix](<Appendices/Appendix 01 - Cost Compounding and Withholding Mathematics.md>) provides the worked ownership cases.\n""",
"Part 04 - Portfolio Architecture Before Fund Selection.md": """\n\n## Technical companion\n\nFor a two-sleeve portfolio, the variance relationship used to test the architecture is:\n\n\\[\n\\sigma_p^2 = w_1^2\\sigma_1^2 + w_2^2\\sigma_2^2 + 2w_1w_2\\rho_{12}\\sigma_1\\sigma_2.\n\\]\n\nThe [diversification and blended-cost appendix](<Appendices/Appendix 02 - Diversification and Blended-Cost Mathematics.md>) shows the derivation and correlation sensitivity.\n""",
"Part 05 - Building a Broad Core and Measuring Overlap.md": """\n\n## Technical companion\n\nA holdings list becomes a concentration measure through:\n\n\\[\nHHI = \\sum_{i=1}^{N}w_i^2, \\qquad N_{\\mathrm{effective}} = \\frac{1}{HHI}.\n\\]\n\nThe [concentration appendix](<Appendices/Appendix 03 - Concentration and Effective Holding Count.md>) derives the equal-weight case and shows how to use a complete holdings file.\n""",
"Part 06 - Satellites Thematic Exposure and Concentration.md": """\n\n## Technical companion\n\nA thematic sleeve should be measured against the core by holdings overlap, weight, liquidity, expense and correlation. The [concentration appendix](<Appendices/Appendix 03 - Concentration and Effective Holding Count.md>) retains the full HHI and effective-holding-count derivation used for that review.\n""",
"Part 07 - Options Income as a Tactical Sleeve.md": """\n\n## Technical companion\n\nFor a cash-secured put, collateral and period yield are calculated as:\n\n\\[\nC = K \\times m \\times q, \\qquad y_{\\mathrm{period}} = \\frac{\\Pi}{C},\n\\]\n\nwhere (K) is strike, (m) is the contract multiplier, (q) is contracts and \\(\\Pi\\) is premium received. The [matrix variance, wheel and tax appendix](<Appendices/Appendix 04 - Matrix Variance Options and Tax Cases.md>) retains the strike sensitivity and wash-sale illustration.\n""",
"Part 08 - Integration Rebalancing and Portfolio Governance.md": """\n\n## Technical companion\n\nA rebalancing trade follows:\n\n\\[\n\\mathrm{Trade}_i = w_i^{\\ast}V_{\\mathrm{portfolio}} - V_i.\n\\]\n\nPositive values are purchases and negative values are sales. The [rebalancing and case-study appendix](<Appendices/Appendix 05 - Rebalancing Sequence Risk and Case Study.md>) carries the full trade reconciliation.\n""",
"Part 09 - Long-Term Maintenance Withdrawals and Review.md": """\n\n## Technical companion\n\nWith an annual withdrawal (W_t), the sequence model is:\n\n\\[\nV_t = V_{t-1}(1+r_t)-W_t.\n\\]\n\nThe order of (r_t) matters once cash leaves the portfolio. The [sequence-risk and case-study appendix](<Appendices/Appendix 05 - Rebalancing Sequence Risk and Case Study.md>) retains the full ten-year paths, rebalancing arithmetic and workbook mapping.\n""",
}
for name, addition in additions.items():
    path = unified / name
    text = path.read_text(encoding="utf-8")
    if "## Technical companion" not in text:
        path.write_text(text.rstrip() + addition, encoding="utf-8")

readme = """# Unified US Series Technical Appendix Index

The five reviewed Claude technical appendices are retained here as MathJax-ready companions to the nine-part unified series. They preserve extended derivations and worked examples that would disrupt the main reading sequence, while the relevant article now introduces each governing equation and links to its companion.

| Appendix | Preserved material | Linked articles |
| --- | --- | --- |
| 01 | Cost compounding, withholding and estate-tax mechanics | Parts 1 to 3 |
| 02 | Variance, correlation and blended-cost derivations | Parts 4 and 5 |
| 03 | HHI and effective holding count | Parts 5 and 6 |
| 04 | Matrix variance, options-wheel sensitivity and tax cases | Parts 4 and 7 |
| 05 | Rebalancing, sequence risk and long-term case study | Parts 8 and 9 |

The companion workbook contains formula-driven versions of these calculations. Illustrative inputs remain clearly distinguished from reported or statutory source material.
"""
(appendix_dir / "README.md").write_text(readme, encoding="utf-8")
print("Integrated 5 technical appendices and 9 article companions")