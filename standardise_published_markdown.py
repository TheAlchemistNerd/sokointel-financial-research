from pathlib import Path
import re

root = Path(r"C:\Users\Nevo\Downloads\financial material")
paths = []
paths += list((root / "NSE Dividend Growth Project 2026").glob("NSE_Dividend_Growth_Part_*.md"))
paths += list((root / "NSE Dividend Growth Project 2026" / "Publication" / "Appendices").glob("*.md"))
paths += [root / "NSE Dividend Growth Project 2026" / "IEEE_Sources.md", root / "NSE Dividend Growth Project 2026" / "NSE_Dividend_Growth_DCA_and_Watchlist_IEEE_source.md", root / "NSE Dividend Growth Project 2026" / "NSE_Dividend_Growth_DCA_and_Watchlist_IEEE_source.before_punctuation.md"]
kenya = root / "Kenyan Equities and Company Analysis" / "Four Part Series"
paths += list(kenya.glob("Part *.md")) + list((kenya / "Appendices").glob("*.md")) + [kenya / "README.md"]
paths += [kenya / "Research" / name for name in ["Actual Company Evidence Ledger.md", "NSE Kenyan Equities and Value Investing Reconciliation.md", "Research Questions and Coverage.md", "References.md", "Reproduction Guide.md", "Verification.md"]]
paths += [root / "NSE Value Investing and Dividend Growth" / "NSE Value Investing Material Map.md"]
paths += list((root / "US Markets and Portfolio Construction" / "Unified Series").rglob("*.md"))

symbol_map = {
    "ᵢ": "_i", "ⱼ": "_j", "ₚ": "_p", "ₜ": "_t", "ₙ": "_n", "ᴺ": "^N", "ᵀ": "^T",
    "₀": "_0", "₁": "_1", "₂": "_2", "₃": "_3", "₄": "_4", "₅": "_5", "₆": "_6", "₇": "_7", "₈": "_8", "₉": "_9",
    "²": "^{2}", "³": "^{3}", "⁴": "^{4}", "⁵": "^{5}", "⁶": "^{6}", "⁷": "^{7}", "⁸": "^{8}", "⁹": "^{9}", "⁰": "^{0}", "¹": "^{1}",
    "×": r"\times", "÷": r"\div", "−": "-", "≤": r"\le", "≥": r"\ge", "≠": r"\ne", "≈": r"\approx", "ρ": r"\rho", "σ": r"\sigma", "μ": r"\mu", "π": r"\pi", "β": r"\beta", "Δ": r"\Delta", "Σ": r"\sum", "∑": r"\sum", "∏": r"\prod", "√": r"\sqrt",
}

def texify(value: str) -> str:
    value = value.replace("Σᵢ₌₁ᴺ", r"\sum_{i=1}^{N}")
    value = value.replace("∑ᵢ", r"\sum_i").replace("∏[t=1…n]", r"\prod_{t=1}^{n}")
    value = value.replace("₌", "=").replace("…", r"\ldots")
    for source, target in symbol_map.items():
        value = value.replace(source, target)
    value = re.sub(r"\\sqrt([0-9.]+)", r"\\sqrt{\1}", value)
    value = re.sub(r"(?<![\\\w])([A-Za-z])_([A-Za-z0-9]+)", r"\1_{\2}", value)
    value = re.sub(r"(?<![\\\w])([A-Za-z])\^([0-9A-Za-z])", r"\1^{\2}", value)
    return value

changed = []
for path in paths:
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    original = text
    text = text.replace("—", ";")
    lines = []
    for line in text.splitlines():
        if line.startswith("> ") and re.search(r"[=×÷−√∑ΣσρμβπΔ≤≥≠²³₀₁₂₃₄₅₆₇₈₉]", line):
            expression = line[2:].strip()
            lines.extend(["\\[", texify(expression), "\\]"])
        else:
            lines.append(line)
    text = "\n".join(lines) + ("\n" if original.endswith("\n") else "")
    # Remaining symbolic arithmetic in prose is kept readable as plain language.
    text = text.replace(" × ", " multiplied by ").replace(" ÷ ", " divided by ")
    text = text.replace(" − ", " minus ")
    # Remaining unicode math variables in prose receive ASCII names; displayed derivations above use TeX.
    for source, target in symbol_map.items():
        text = text.replace(source, target.replace("\\", ""))
    text = text.replace("₌", "=").replace("…", "...")
    if text != original:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(root))
print(f"Standardised {len(changed)} Markdown files")
for item in changed:
    print(item)