"""Build the two Sokointel Word and PDF editions from the normalized split Markdown."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from edition_document import build  # noqa: E402

PANDOC = r"C:\Users\Nevo\AppData\Local\Pandoc\pandoc.exe"


def normalize_markdown_tables(markdown):
    """Remove only blank separator lines within Markdown pipe tables for Pandoc."""
    lines = markdown.splitlines()
    normalized = []
    index = 0
    while index < len(lines):
        line = lines[index]
        normalized.append(line)
        if line.startswith("|"):
            index += 1
            while index < len(lines):
                if not lines[index].strip() and index + 1 < len(lines) and lines[index + 1].startswith("|"):
                    index += 1
                    continue
                if lines[index].startswith("|"):
                    normalized.append(lines[index])
                    index += 1
                    continue
                break
            continue
        index += 1
    return "\n".join(normalized)


def manuscript_body(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    expected = "# NSE Dividend-Growth DCA and Watchlist Research Project"
    if lines[:1] != [expected]:
        raise ValueError(f"Unexpected manuscript header in {path.name}")
    # The title and three snapshot fields become branded front matter. All
    # substantive source content begins at the first numbered section.
    return normalize_markdown_tables("\n".join(lines[6:]).strip())


def appendix(name):
    return (ROOT / "Publication" / "Appendices" / name).read_text(encoding="utf-8")


def references():
    lines = (ROOT / "NSE_Dividend_Growth_DCA_and_Watchlist_IEEE_source.md").read_text(encoding="utf-8").splitlines()
    start = lines.index("## References")
    return "\n".join(lines[start:])


def payload(slug, title, part_title, source, appendix_text, canonical_url):
    return {
        "config": {
            "root": str(ROOT),
            "pandoc": PANDOC,
            "pdf_engine": "word",
            "publication_url": "https://sokointel.com",
            "body_font": "Georgia",
            "heading_font": "Segoe UI",
        },
        "snapshot": {
            "slug": slug,
            "title": title,
            "series_title": "NSE Dividend Growth Research",
            "description": "A Sokointel research edition based on the Nairobi Securities Exchange dividend-growth DCA and watchlist project.",
            "research_date": "10 September 2026",
            "edition_date": "2026-09-10",
            "identifier": "sokointel-nse-dividend-growth-2026",
            "canonical_url": canonical_url,
            "license": "CC BY-NC-SA 4.0",
            "questions": [
                "How can KES 100,000 be staged across a dividend-growth portfolio while reserving transaction costs?",
                "Which inputs determine whole-share DCA quantities, dividend income and net yield?",
                "How should a watchlist expand diversification without increasing bank concentration automatically?",
            ],
            "articles": [{"title": part_title, "body": source, "appendix": appendix_text}],
        },
    }


def main():
    part_1 = ROOT / "NSE_Dividend_Growth_Part_1_Core_Portfolio_and_DCA.md"
    part_2 = ROOT / "NSE_Dividend_Growth_Part_2_Watchlist.md"
    if not part_1.is_file() or not part_2.is_file():
        raise SystemExit("Run tools/prepare_manuscript.py before building publications.")
    output = ROOT / "Publication" / "Output"
    part_1_source = manuscript_body(part_1) + "\n\n" + references()
    build(payload(
        "nse-dividend-growth-part-one",
        "NSE Dividend Growth DCA and Watchlist Part One",
        "Core Portfolio and Three Month DCA",
        part_1_source,
        appendix("Appendix A Mathematical Formulae.md"),
        "https://sokointel.com/series/nse-dividend-growth/part-one/",
    ), output / "Part 1 Core Portfolio and DCA")
    build(payload(
        "nse-dividend-growth-part-two",
        "NSE Dividend Growth DCA and Watchlist Part Two",
        "Watchlist and Portfolio Expansion",
        manuscript_body(part_2),
        appendix("Appendix B Watchlist Formulae.md"),
        "https://sokointel.com/series/nse-dividend-growth/part-two/",
    ), output / "Part 2 Watchlist and Portfolio Expansion")


if __name__ == "__main__":
    main()
