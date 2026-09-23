"""Apply punctuation-only dash changes and split the NSE manuscript at Part 2."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "NSE_Dividend_Growth_DCA_and_Watchlist_IEEE_source.md"
BACKUP = ROOT / "NSE_Dividend_Growth_DCA_and_Watchlist_IEEE_source.before_punctuation.md"
PART_1 = ROOT / "NSE_Dividend_Growth_Part_1_Core_Portfolio_and_DCA.md"
PART_2 = ROOT / "NSE_Dividend_Growth_Part_2_Watchlist.md"

# The only source-text edits permitted by this project are the 24 listed
# em-dash substitutions. Each replacement is selected from its local grammar.
REPLACEMENTS = {
    9: [": ", ", "],
    21: [", ", ", "],
    121: ["-", "-"],
    125: [", ", ", "],
    171: [", "],
    185: [": "],
    189: [": "],
    262: [": ", ", "],
    286: [": "],
    314: [", ", ", "],
    340: [": "],
    358: [": "],
    362: [": "],
    366: [": "],
    368: [": "],
    392: [": "],
    398: [": "],
    408: [": "],
}


def apply_replacements(lines):
    changed = list(lines)
    for line_number, replacements in REPLACEMENTS.items():
        index = line_number - 1
        pieces = changed[index].split("—")
        if len(pieces) - 1 != len(replacements):
            raise ValueError(f"Line {line_number} does not contain the expected em dashes")
        rebuilt = pieces[0]
        for replacement, piece in zip(replacements, pieces[1:]):
            if replacement == "-":
                rebuilt += replacement + piece
            else:
                rebuilt = rebuilt.rstrip() + replacement + piece.lstrip()
        changed[index] = rebuilt
    if any("—" in line for line in changed):
        raise ValueError("An em dash remains after the approved punctuation replacements")
    return changed


def write_lines(path, lines):
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    current = MASTER.read_text(encoding="utf-8")
    if not BACKUP.exists():
        BACKUP.write_text(current, encoding="utf-8")
    original = BACKUP.read_text(encoding="utf-8")
    lines = original.splitlines()
    if sum(line.count("—") for line in lines) != 24:
        raise ValueError("The preserved original must contain exactly 24 em dashes")
    normalized = apply_replacements(lines)
    write_lines(MASTER, normalized)

    split_heading = "## 13. Part 2: Purpose of the Watchlist"
    if normalized[184] != split_heading:
        raise ValueError("The structural Part 2 heading moved; review the split point")
    # Lines 1-183 are Part 1. Part 2 carries the same document identity and
    # begins at the original Part 2 heading. No source words are changed.
    write_lines(PART_1, normalized[:183])
    write_lines(PART_2, normalized[:5] + [""] + normalized[184:])
    print(f"Normalized 24 em dashes and created {PART_1.name} and {PART_2.name}")


if __name__ == "__main__":
    main()
