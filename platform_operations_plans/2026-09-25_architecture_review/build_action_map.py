"""Build the manually reviewed file-level adoption map; do not mutate sources."""
from pathlib import Path
from datetime import datetime
import csv
import hashlib
import json
import math
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
OUT = Path(__file__).parent
inventory = json.loads((OUT / "source_inventory.json").read_text(encoding="utf-8"))

# Each substantive assessment is authored from the document review. The IDs are
# stable within this dated, saved source inventory, not a general keyword score.
# relevance, priority, target, proposed action, status/evidence gate
assessments = {
"AR01": ("direct", "P1", "Website product_architecture; shared calculator contracts; later C#/Excel-DNA/VSTO", "Adopt typed quantities, dated cases, cash invariants and version binding; stage CR-FR requirements without replacing canonical FR IDs", "Proposed twenty credit requirements, not an implemented lending/SPV engine; validate each adopted module independently"),
"AR02": ("direct", "P1", "Business Credit Part 2; workbook P2 Facility/Entity Review; Owner Earnings P1 Part4", "Extend existing offer and contribution exhibits with debt/receipt dates, availability expiry and cash trough", "Article already covers cash and pricing; preserve existing case or label new hypothetical case; reconcile all dates"),
"AR03": ("direct-support", "P2", "Shared review index and dated adoption record", "Retain as navigation; route status to September25 follow-up instead of treating Project1 as planning-only", "September23 body with September25 update; imported source chronology remains visible"),
"AR04": ("direct", "P1", "Cross-project backlog; Business Credit; Owner Earnings1/2; enterprise Workbench", "Map U01-U20 to bounded case records, keeping advanced modules optional", "Developed means written; does not establish implementation, empirical validation or local regulatory application"),
"AR05": ("direct", "P1", "Shared formula dictionary; credit scenarios; later Treasury notebooks", "Reuse money-first pricing, hazard conventions and reconciliation examples; preserve measurement distinctions", "Hypothetical scalar checks; require complete model contracts and current authority before production adoption"),
"AR06": ("direct-support", "P2", "Review navigation/source provenance", "Retain original project destinations and point duplicate bodies to canonical copies", "Do not interpret external whitepapers as assets maintained in these two repos"),
"AR07": ("direct-support", "P2", "Source evidence archive and reading record", "Retain contiguous source map and cleaned/original distinction; isolate raw captured instructions", "Historical sources not freshly reread in this adoption review; original backup must survive any cleanup"),
"AR08": ("direct-support", "P2", "Reference register for calculator/article methodology", "Keep source links and version boundaries; refresh primary authorities on implementation/publication", "Reference checks dated September23; not evidence of current rates or universally applicable rules"),
"AR09": ("direct", "P0", "Business Credit P2; Owner Earnings1 Part4; Owner Earnings2 Parts6-10", "Use OE01-OE06 mapping and connected borrower/lender/shareholder teaching cases", "Supersedes stale planning-only status; README-derived workbook assessment is not a cell audit"),
"AR10": ("direct", "P2", "Business Credit Part2; P2 Facility and credit-readiness workbook", "Retain historical rationale; adopt specific dated-case extension from AR02 rather than duplicate prose", "September23 note is older evidence, not a newly missing credit comparison foundation"),
"AR11": ("direct", "P1", "Business Credit Part2; P2 Facility", "Replace duplicate body with link to AR02 when cleanup is adopted", "Exact duplicate; preserve copy manifest/source path and repair inbound links"),
"AR12": ("indirect-specialist", "P2", "Owner Earnings2 Part9 insurer interface; external insurance/IFRS17 research", "Reuse event-to-entity mapping for claims/refunds/remittances; retain Bayesian derivations in original project", "Requires policy/claim/cash data and entity-approved accounting; not a new generic credit model"),
"AR13": ("indirect-specialist", "P2", "External Mwendo Parts3-5; future SokoIntel cohort/SPV adapter", "Preserve transaction/event requirements; extract shared dates/records; defer full SPV and neural work", "Controlled term sheet and model specification govern; no live transaction or full waterfall validation"),
"AR14": ("direct", "P0", "Owner Earnings2 Parts6-10; Filing Inputs/Asset Heavy/Bank Insurance/NSE Casebook", "Prioritize bank payout, insurer timing, construction calendar and source-supported sector bridges", "Seven public tool entries under parallel development cover a bounded slice, not all institutional schedules"),
"AR15": ("direct", "P2", "Owner Earnings1 Parts1-5; Debt and Growth/Cash13W", "Keep earlier conceptual bridge; point current status and schedule work to AR16", "September23 planning-only phrasing superseded by drafts/workbook created September24"),
"AR16": ("direct", "P1", "Owner Earnings1 Part4/Appendix3; Debt and Growth/Cash13W", "Extend financing-cost screen into dated balances, fees, cash floors and blocked-draw scenarios", "Use actual contract conventions; 60/90-day hypothetical cases independently reconcile"),
"AR17": ("indirect-specialist", "P2", "External KESONIA Parts1-4; shared SokoIntel rates/date interfaces", "Retain four-part plan; borrow quantity/calendar discipline; route detailed revision to AR38", "Not an implemented overhaul; source data and product-specific conventions needed"),
"AR18": ("direct", "P1", "Website architecture and future professional calculation contract", "Retain PT01-PT10 as provisional candidates; absorb common definitions and structured errors first", "PT07-PT10 optional advanced scope; no rewritten deployment stack or invented current defaults"),
"AR19": ("indirect-specialist", "P2", "External Underwrite Part5; borrower/lender teaching case in two maintained repos", "Reuse money-first and protection-timing paragraphs; avoid duplicating the developed whitepaper", "Written coverage is not fitted-model evidence; compare borrower capacity and lender profitability separately"),
"AR20": ("indirect-specialist", "P3", "Future institutional market-risk backlog; canonical review AR42", "Replace repeated project-copy body with AR42 pointer; keep FRTB outside public Owner Earnings release", "Book/entity/jurisdiction mapping and independently checked calculations required; no trading-book engine exists here"),
"AR21": ("indirect-specialist", "P3", "Future enterprise integration/vendor research; canonical review AR40", "Replace repeated project-copy body with AR40 pointer; reuse event identity and reconciliation only now", "Vendor descriptions do not prove connectivity, licenses, local instruments or deployment"),
"AR22": ("direct", "P2", "Shared dated cash and bank interfaces; canonical review AR36", "Replace repeated project-copy body with AR36 pointer; retain provenance", "Narrative review, not deployed Treasury system"),
"AR23": ("direct", "P2", "SokoIntel credit modules; external Mwendo/Underwrite and public practitioner articles", "Retain shared note once; adopt connected cases and explicit pricing/protection status; synchronize old public claims", "Contract authority, causal effects and transaction cash require separate evidence"),
"AR24": ("direct", "P1", "Business Credit Entity Review; Owner Earnings1 cash provenance; Project3 evidence ledger", "Reuse cash class plus relationship dimension, confidence and temporal ownership; link rather than clone article", "Older September15 article; source URL/title and public references require publication check; related-party status is not automatic fraud"),
"AR25": ("direct", "P2", "Future Mwendo interface; shared note AR23", "Replace exact duplicate with common-note link; preserve original project trace", "No deletion performed; exact-copy cleanup candidate"),
"AR26": ("direct", "P1", "Owner Earnings1 schedule; shared note AR16", "Replace exact duplicate with AR16 pointer", "Preserve project navigation and source provenance"),
"AR27": ("direct", "P0", "Owner Earnings2 public tools and workbook; shared note AR14", "Replace exact duplicate with AR14 pointer", "Preserve original Project2 source trace and source lines"),
"AR28": ("direct-support", "P2", "Credit lifecycle review navigation", "Retain as entry to proposed requirements and worked cases", "Full reading claims belong to historical source review; not new empirical validation"),
"AR29": ("direct", "P1", "Credit calculator contract; shared cash/quantity dictionary; advanced research backlog", "Reuse price/economic profit equations and specific units/cash/authority distinctions; keep optional methods separate", "Source code and implied-volatility outputs not validated implementations"),
"AR30": ("direct", "P2", "Canonical shared editorial note AR23", "Replace repeated body with pointer or retain one master and repair project-copy navigation", "Near-duplicate footer/link context only, not byte-identical"),
"AR31": ("direct", "P1", "Root credit addendum AR01; controlled architecture requirements", "Retain one full requirements body; other location links to it", "Near-duplicate footer/link context only; provisional CR-FR not merged automatically"),
"AR32": ("direct", "P1", "Future credit/revolver/protection scenarios and independent reference vectors", "Retain nine checked illustrative cases; bind each to exact intended use and model version", "Reserve arithmetic is not full waterfall; static OC not loss absorption; scalar CVA not regulatory capital"),
"AR33": ("direct-support", "P2", "Source precedence and validation gates", "Retain controlled-source hierarchy and full/selected reading boundary", "Canonical/executed/approved sources outrank captured conversational claims"),
"AR34": ("direct-support", "P2", "Collected architecture review navigation and import provenance", "Retain index but distinguish 45 matching MD+HTML files from 46 date-qualified Markdown files", "121 copied entries; paths/link repairs preserved; source scripts not executed"),
"AR35": ("direct-support", "P2", "Treasury review navigation", "Keep entry point; link only adopted cases into public tool backlog", "Read/review deliverable, not procurement or live-trading integration"),
"AR36": ("direct", "P2", "Owner Earnings2 bank/commitment cases; shared dates/quantities; external KESONIA series", "Adopt separate NII/EVE/liquidity/payout views and financial responsibilities; keep deep Treasury scope separate", "Four outputs are distinct; no current benchmark or local market assumption inferred"),
"AR37": ("direct", "P2", "Case library: rates, pricing, bank sensitivity and future curve laboratory", "Retain reproducible toy cases and dated historical verification with convention limits", "Historical fixing case is not a complete five-day-lookback contract or current quotation"),
"AR38": ("indirect-specialist", "P2", "External KESONIA Parts1-4; SokoIntel common date/event interfaces", "Use targeted insertion blueprint in original series; borrow shared calculation contract now", "SQL/calendars, posting, local rules and external acknowledgements each need implementation evidence"),
"AR39": ("direct-support", "P2", "Treasury evidence and reference register", "Keep traceability, full-versus-selected reads and source limitations", "No new fresh legal/regulatory authority check or production test in this adoption review"),
"AR40": ("indirect-specialist", "P3", "Enterprise integration/vendor research", "Retain read-only analysis and simulated STP proof-of-concept spec; not an immediate free calculator feature", "Product/version/permissions and sandbox reconciliation precede any integration claim"),
"AR41": ("indirect-specialist", "P2/P3", "Future institutional backlog R01-R18; selected Owner Earnings2 R14", "Extract R14 dated shareholder cases now; retain distinct specialist work packages and prerequisites", "Eighteen items are not current-release acceptance criteria; regression/calibration/jurisdiction gates remain"),
"AR42": ("indirect-specialist", "P3", "Future FRTB/market-risk appendix", "Keep canonical scope note outside initial valuation tools; replace AR20 mirrored body with pointer", "Cannot derive approved market-risk capital from educational ES, generic hedges or SPV diagrams"),
"AR43": ("direct", "P1", "Cash-provenance article AR24", "Replace duplicate imported article with pointer to retained copy or original source", "Exact byte duplicate; published September15, not new September25 authorship"),
"AR44": ("direct", "P2", "Shared pricing/editorial note AR23", "Replace exact duplicate with pointer; preserve Underwrite original location", "Exact byte duplicate; original external manuscript unchanged"),
"AR45": ("direct-support", "P2", "Top-level collection index", "Keep lightweight entry point and link adopted work to current status", "Navigation only, no new product requirement"),
"AR46": ("direct", "P0", "Internal wiki and positioning brief; enterprise product strategy", "Reuse consumer-distribution versus institutional-workflow distinction and measurable pilot gates; public article must be a separate reviewed distillation", "Internal strategy, not capability parity or a ratings business; primary vendor facts checked afresh for external publication"),
}

exact = {"AR11":"AR02", "AR25":"AR23", "AR26":"AR16", "AR27":"AR14", "AR43":"AR24", "AR44":"AR23"}
near = {"AR20":"AR42", "AR21":"AR40", "AR22":"AR36", "AR30":"AR23", "AR31":"AR01"}
rows = []
for item in inventory:
    key = item["id"]
    relevance, priority, targets, action, gate = assessments[key]
    content = Path(item["full_path"]).read_text(encoding="utf-8-sig")
    date_hint = "15 September 2026" if key in ("AR24", "AR43") else ("23 September 2026" if "23 September 2026" in "\n".join(content.splitlines()[:6]) else "See document/source manifest")
    flag = "exact-copy consolidation candidate" if key in exact else "repeated-body consolidation candidate" if key in near else "relocate from immediate public-release backlog" if relevance == "indirect-specialist" else "retain"
    rows.append(dict(item, authored_date_hint=date_hint, relevance=relevance, priority=priority,
        removal_or_relocation_flag=flag, recommended_retained_id=exact.get(key,near.get(key,key)),
        target_project_parts_workbook=targets, proposed_action=action, implementation_status_and_evidence_gate=gate,
        reading_scope="Complete distinct Markdown body; duplicate bodies hash-checked; footer variants diff-checked",
        visibility="INTERNAL ONLY; never import architecture/review document into public catalogue",
        disposition="Recommendation only; no deletion or source edit"))

with (OUT / "file_action_map.csv").open("w",encoding="utf-8-sig",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)

assert len(rows)==46 and len(assessments)==46
source_changes=[x["id"] for x in inventory if hashlib.sha256(Path(x["full_path"]).read_bytes()).hexdigest()!=x["sha256"]]
assert not source_changes, source_changes

vectors={
    "order_interest_60d":500*.18*60/360,
    "order_cash_day0":250+200+500-600-10,
    "order_cash_day30":340-120,
    "order_cash_day60":220+800-100-500-15,
    "order_delayed_cash_day60":220-100-500-15,
    "order_delayed_gap_to_floor":100-(220-100-500-15),
    "order_interest_90d":500*.18*90/360,
    "order_cash_agreed_90d_maturity":120+800-500-22.5,
    "bank_base_capital_capacity":100+20-.18*560,
    "bank_stress_capital_capacity":100+12-.18*560,
    "bank_base_distribution_bound":min(100+20-.18*560,14),
    "bank_stress_distribution_bound":min(100+12-.18*560,14),
    "insurer_before_receipt_cash":3-4,
    "insurer_gap_to_floor":2-(3-4),
    "insurer_horizon_excess_before_bridge_cost":3+12-4-2,
    "revolver_ead":4e6+.564*6e6,
    "revolver_el":.06*.45*(4e6+.564*6e6),
    "revolver_hurdle_rate":(360000+120000+199368+.14*886080-60000)/4e6,
    "equinix_normalized_downside":90-54-27.5,
    "reserve_cash_sources":50+80+140+50,
    "reserve_cash_uses":300+20+0,
}
expected=[15,340,220,405,-395,495,22.5,397.5,19.2,11.2,14,11.2,-1,3,9,7384000,199368,.1858548,8.5,320,320]
for (name,value),target in zip(vectors.items(),expected):
    assert math.isclose(value,target,abs_tol=1e-8), (name,value,target)

verification=dict(review_date="2026-09-25", generated_local=datetime.now().astimezone().isoformat(),
    scoped_markdown_files=len(rows), unique_sha256=len({x["sha256"] for x in rows}),
    exact_redundant_instances=len(exact), footer_variant_instances=len(near),
    original_manifest_entries=42, original_manifest_copy_hash_matches=42,
    source_hash_changes=source_changes, source_scripts_executed=False,
    original_sources_edited=False, files_deleted=False, visibility="INTERNAL ONLY",
    source_scope="Date-qualified product_architecture Markdown; provenance manifests; research READMEs; workbook sheet metadata plus targeted Profile Stress L8 cached formula check; selected platform route/catalogue/release evidence",
    source_limits="No fresh complete audit of all article bodies/workbook cells, canonical older architecture or historical raw conversations; no fresh external authority validation; no production deployment check",
    teaching_vectors=vectors, scalar_assertions_passed=len(vectors),
    formula_note="Toy cash/capital vectors verify arithmetic only; regulatory/current-market/issuer claims are not inferred")
(OUT / "review_verification.json").write_text(json.dumps(verification,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"file_actions":len(rows),"source_changes":source_changes,"scalar_assertions":len(vectors),"exact_copy_flags":len(exact),"footer_variant_flags":len(near)}))
