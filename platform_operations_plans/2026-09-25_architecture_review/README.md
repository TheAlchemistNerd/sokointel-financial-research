# SokoIntel architecture material: 25 September 2026 review

**INTERNAL ONLY — product and editorial planning.** Neither this review nor the collected architecture/review documents belong in the public article catalogue. Public articles may use separately reviewed, appropriate findings; internal planning files themselves must not be imported or exposed as reader assets.

**Purpose:** identify what the material created or copied into the website's `product_architecture` directory on 25 September contributes to the two maintained repositories, with public calculators first and targeted article/workbook development next.

**Review status:** source review and adoption map, followed by a bounded internal-copy correction. The initial review changed no source document. The authorised follow-up corrects a reference label in two imported review copies and adds a current-status note to the internal architecture index; their before/after hashes are recorded separately. External originals, the import manifest, article catalogue and workbooks remain unchanged by this agent. The parallel calculator implementation has its own release and verification record. Nothing was deleted.

## Deliverables

- [Detailed findings and adoption plan](REVIEW_AND_ADOPTION_PLAN.md)
- [Per-file action map](file_action_map.csv): initial assessment of all 46 qualifying Markdown files, relevance, disposition, target and evidence gate. Later corrections to AR24, AR43 and AR45 are recorded in the correction ledger and current report rather than replacing this snapshot.
- [Source inventory](source_inventory.csv), also available as [JSON](source_inventory.json): creation/modification times, hashes, exact duplicates and original-source provenance.
- [Review verification](review_verification.json): preservation checks, inventory totals and independently recalculated teaching vectors.
- [Internal-copy correction ledger](copy_corrections_2026-09-25.json): the later authorised index/reference corrections, before/after hashes and preserved original-source/manifest checks. The original inventory and review-verification files remain the initial review snapshot.
- [Inventory helper](review_inventory.py): reads only the date-qualified source documents; writes its inventory beside this README. It never executes imported scripts.
- [Action-map builder](build_action_map.py): records the initial manual semantic assessments and checks preservation plus the labelled arithmetic vectors. Its strict original-hash guard will detect the three authorised follow-up changes; do not rerun it to overwrite the initial snapshot. Use the separate correction ledger for the current state.

The date filter uses Windows local creation **or** modification date. A creation timestamp on a copied file is not its authorship date. The report explains which older materials were imported today and which copies can be consolidated later without losing provenance.
