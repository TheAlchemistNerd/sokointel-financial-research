"""Read-only source inventory for the explicitly scoped 25 September review.

Writes review artifacts beside this script, never into product_architecture.
Pass document IDs to emit their complete text with long local links abbreviated
for review. Canonical link targets remain in untouched source files.
"""
from pathlib import Path
from datetime import datetime
import csv
import hashlib
import json
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(r"C:\Users\Nevo\Downloads\business and technical website blog\product_architecture")
OUT = Path(__file__).parent
REVIEW_DATE = "2026-09-25"
manifest = json.loads((BASE / "review_materials/2026-09-25_cross_project_review/copy_manifest.json").read_text(encoding="utf-8"))
provenance = {str(Path(x["copy"])): x for x in manifest["files"]}
rows = []
for path in sorted(BASE.rglob("*.md"), key=lambda p: str(p).lower()):
    stat = path.stat()
    created = datetime.fromtimestamp(getattr(stat, "st_birthtime", stat.st_ctime)).isoformat(timespec="seconds")
    modified = datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds")
    if not (created.startswith(REVIEW_DATE) or modified.startswith(REVIEW_DATE)):
        continue
    data = path.read_bytes()
    text = data.decode("utf-8-sig")
    source = provenance.get(str(path), {})
    source_path = Path(source["source"]) if source else None
    rows.append(dict(id=f"AR{len(rows)+1:02d}", relative_path=path.relative_to(BASE).as_posix(),
        full_path=str(path), created_local=created, modified_local=modified,
        bytes=len(data), lines=len(text.splitlines()), words=len(text.split()),
        sha256=hashlib.sha256(data).hexdigest(), title=text.splitlines()[0],
        original_source=str(source_path) if source_path else "",
        manifest_source_sha256=source.get("source_sha256", ""),
        manifest_copy_sha256=source.get("copy_sha256", ""),
        copy_hash_matches_manifest=(hashlib.sha256(data).hexdigest()==source.get("copy_sha256")) if source else "",
        links_adjusted=source.get("links_adjusted", ""),
        original_modified_local=datetime.fromtimestamp(source_path.stat().st_mtime).isoformat(timespec="seconds") if source_path and source_path.exists() else "",
        source_exists=source_path.exists() if source_path else ""))

groups = {}
for row in rows:
    groups.setdefault(row["sha256"], []).append(row["id"])
for row in rows:
    row["exact_duplicate_ids"] = ";".join(x for x in groups[row["sha256"]] if x != row["id"])

if len(sys.argv) > 1:
    for row in rows:
        if row["id"] in sys.argv[1:]:
            print(f"\n{row['id']} {row['relative_path']}\n")
            text = Path(row["full_path"]).read_text(encoding="utf-8-sig")
            text = re.sub(r"\]\(<C:/[^>]+>\)", "](local-source)", text)
            text = re.sub(r"\]\(C:/[^)]+\)", "](local-source)", text)
            for n, line in enumerate(text.splitlines(), 1):
                print(f"{n}: {line}")
else:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "source_inventory.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    with (OUT / "source_inventory.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row["id"], row["relative_path"], row["words"], row["exact_duplicate_ids"])
    print(json.dumps({"files":len(rows),"unique_sha256":len(groups),"words_including_duplicates":sum(x['words'] for x in rows)}))
