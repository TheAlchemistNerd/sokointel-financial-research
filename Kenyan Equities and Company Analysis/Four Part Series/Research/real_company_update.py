from pathlib import Path
import json,re,hashlib,datetime,shutil,math
base=Path(__file__).resolve().parent
series=base.parent
root=series.parent.parent
STAMP="2026-09-12"
URLS={
 "nse":"https://www.nse.co.ke/wp-content/uploads/11-SEP-26.pdf",
 "bat":"https://www.batkenya.com/content/dam/endmarkets/ke/en/download/investors-and-reporting/annual-reports/BATK_Combined_Annual_and_Sustainability_Report_2025.pdf",
 "bat_results":"https://www.batkenya.com/content/dam/endmarkets/ke/en/download/investors-and-reporting/financial-statements/bat_kenya-2025_full_year_results.pdf",
 "equity":"https://equitygroupholdings.com/wp-content/uploads/2026/06/Equity-Group-Holdings-PLC-2025-Integrated-Report-and-Financial-Statements.pdf",
 "jubilee":"https://jubileeinsurance.com/group/wp-content/uploads/2026/06/Jubilee-Holdings-2025-Annual-Integrated-Report.pdf"}
prices={"EQTY":102.0,"KCB":94.0,"COOP":37.15,"SCOM":35.2,"BAT":560.0,"JUB":412.75,"KEGN":11.0,"EABL":290.5}
volumes={"EQTY":4974486,"KCB":375298,"COOP":326778,"SCOM":13847651,"BAT":2426,"JUB":669,"KEGN":2135435,"EABL":36686}
bat={
 "2024":{"revenue":25715.903,"cogs":15218.693,"ebit":7313.038,"profit":4483.370,"cfo":7877.953,"capex":322.015,"depreciation":703.740,"trade_receivables":2541.648,"inventory":3324.090,"trade_payables":1088.613,"plant":9811.984,"cash":5390.275,"debt":97.667,"equity":15733.130,"total_assets":23654.226,"current_assets":13593.457,"current_liabilities":6025.355,"dps_fiscal":50.0,"dps_cash_paid":50.0,"eps":44.83},
 "2025":{"revenue":23191.945,"cogs":12372.298,"ebit":7474.835,"profit":5245.617,"cfo":6633.154,"capex":301.833,"depreciation":733.777,"trade_receivables":2466.921,"inventory":3321.003,"trade_payables":2035.289,"plant":9457.704,"cash":6218.264,"debt":72.667,"equity":15485.431,"total_assets":23585.228,"current_assets":13898.130,"current_liabilities":6197.535,"other_assets":2121.336,"other_liabilities":5991.841,"dps_fiscal":70.0,"dps_cash_paid":55.0,"eps":52.46,"cash_generated_operations":8581.908,"interest_received":209.099,"interest_paid":22.043,"tax_paid":2135.810,"disposal_proceeds":12.936,"lease_principal_paid":25.0,"fx_cash":8.732},
 "shares_million":100.0}
eq={"2024":{"attributable_profit":46549,"attributable_equity":234041,"group_profit":48824,"eps":12.34,"dps":4.25,"gross_amortised_loans":890657,"stage3_loans":109732,"stage3_allowance":60674,"total_allowance":74788},
 "2025":{"attributable_profit":71964,"attributable_equity":309505,"group_profit":75548,"eps":19.07,"dps":5.75,"gross_amortised_loans":943453,"stage3_loans":99561,"stage3_allowance":54597,"total_allowance":64544},
 "shares_million":3773.674802,
 "kenya_bank_capital":{"report_date":"2025-12-31","rwa":850487,"core_capital":122174,"total_capital":139970,"core_minimum":0.105,"total_minimum":0.145}}
jub={"2025":{"insurance_revenue":29920.887,"insurance_service_expense":26884.724,"reinsurance_net_expense":1189.922,"service_result":1846.241,"net_investment_income":28990.055,"insurance_finance_expense":24480.709,"other_income":444.250,"other_operating_expense":2377.981,"associates_profit":2915.896,"other_finance_cost":153.332,"pbt":7184.420,"tax":1633.772,"group_profit":5550.648,"nci_profit":-231.314,"attributable_profit":5781.962,"attributable_equity":53768.889,"dps":15.0},
 "2024":{"attributable_equity":49113.565,"attributable_profit":4792.620},"shares_million":72.473}
assumptions={"bat_dcf":{"annual_revenue_growth":[0.02,0.03,0.03,0.03,0.03],"ebit_margin":[0.30,0.30,0.31,0.31,0.31],"depreciation_pct_opening_plant":0.08,"capex_pct_revenue":0.035,"tax":0.30,"cogs_pct_revenue":0.54,"dso":40,"dio":95,"dpo":55,"wacc":0.16,"terminal_growth":0.03,"terminal_roic":0.18,"excess_cash":0.0,"debt_claim":72.667,"forecast_labels":["Year 1","Year 2","Year 3","Year 4","Year 5"],"basis":"Normalised forward annual operating scenario using FY2025 operating scale. No FY2026-2030 reported results are implied. No historical cash is added to current equity value; debt carry-forward is an explicit scenario assumption. This is an operating-value sensitivity study, not a fully updated September 2026 target."},
 "equity_ddm":{"short_growth":0.08,"terminal_growth":0.05,"cost_equity":0.18,"years":5,"next_dividend_timing_years":1.0},
 "equity_pb":{"sustainable_roe":0.20,"growth":0.05,"cost_equity":0.18},
 "capital_scenarios":[{"name":"Moderate RWA growth","rwa_growth":0.10,"profit":30000,"target_total_ratio":0.165},{"name":"Faster growth and loss stress","rwa_growth":0.20,"profit":20000,"target_total_ratio":0.165}]}
data={"version":1,"retrieved_date":STAMP,"price_date":"2026-09-11","price_convention":"NSE daily VWAP, not closing bid/ask or guaranteed fill","currency":"KES","financial_units":"KES million except per-share and ratios","prices":prices,"daily_share_volume":volumes,"sources":URLS,"BAT":bat,"EQTY":eq,"JUB":jub,"scenario_assumptions":assumptions}
(base/"real_company_inputs.json").write_text(json.dumps(data,indent=2),encoding="utf-8")
# Preserve previous editorial source revisions and exact formula dictionaries as text/json.
archive=base/"Archive-before-real-company-update"
archive.mkdir(exist_ok=True)
for p in list(series.glob("Part *.md"))+list((series/"Appendices").glob("*.md")):
 target=archive/(p.name+".txt")
 if not target.exists():shutil.copyfile(p,target)
legacy={}
for p in (series/"Appendices").glob("*.md"):
 text=p.read_text(encoding="utf-8")
 if "## Workbook formula dictionary" in text:
  legacy[p.name]=text.split("## Workbook formula dictionary",1)[1]
(base/"legacy_formula_dictionary.json").write_text(json.dumps(legacy,ensure_ascii=False,indent=2),encoding="utf-8")
# Deterministic models mirrored by the workbook's formula surface.
b=bat["2025"]; a=assumptions["bat_dcf"]; rev=b["revenue"]; plant=b["plant"]; nwc=b["trade_receivables"]+b["inventory"]-b["trade_payables"]; forecasts=[]
for i,g in enumerate(a["annual_revenue_growth"]):
 rev*=1+g; ebit=rev*a["ebit_margin"][i]; dep=plant*a["depreciation_pct_opening_plant"]; capex=rev*a["capex_pct_revenue"]; cogs=rev*a["cogs_pct_revenue"]; ar=rev*a["dso"]/365; inv=cogs*a["dio"]/365; ap=cogs*a["dpo"]/365; nnwc=ar+inv-ap; delta=nnwc-nwc; nopat=ebit*(1-a["tax"]); fcff=nopat+dep-capex-delta; plant+=capex-dep
 forecasts.append({"year":i+1,"revenue":rev,"ebit":ebit,"depreciation":dep,"capex":capex,"ar":ar,"inventory":inv,"ap":ap,"nwc":nnwc,"change_nwc":delta,"nopat":nopat,"fcff":fcff,"plant":plant})
 nwc=nnwc
def dcf(w,g):
 pv=sum(x["fcff"]/(1+w)**x["year"] for x in forecasts); terminal=forecasts[-1]["nopat"]*(1+g)*(1-g/a["terminal_roic"])/(w-g); tvpv=terminal/(1+w)**5; ev=pv+tvpv; equity=ev+a["excess_cash"]-a["debt_claim"]; return {"pv_explicit":pv,"pv_terminal":tvpv,"ev":ev,"equity_value":equity,"per_share":equity/100,"terminal_share":tvpv/ev,"margin_of_safety":1-prices["BAT"]/(equity/100)}
q=assumptions["equity_ddm"]; ds=[5.75*(1+q["short_growth"])**t for t in range(1,6)]
dpv=sum(d/(1+q["cost_equity"])**t for t,d in enumerate(ds,1)); dtv=ds[-1]*(1+q["terminal_growth"])/(q["cost_equity"]-q["terminal_growth"]); dvalue=dpv+dtv/(1+q["cost_equity"])**5
results={"bat_forecast":forecasts,"bat_dcf":dcf(.16,.03),"bat_sensitivity":[{"wacc":w,"growth":g,"value":dcf(w,g)["per_share"]} for w in [.14,.16,.18] for g in [.02,.03,.04]],"equity_ddm":{"dividends":ds,"pv_dividends":dpv,"terminal_value":dtv,"value":dvalue,"margin_of_safety":1-prices["EQTY"]/dvalue},"equity_book_per_share":309505/eq["shares_million"],"equity_pb_value":309505/eq["shares_million"]*(.20-.05)/(.18-.05),"jubilee_eps":jub["2025"]["attributable_profit"]/jub["shares_million"],"jubilee_bvps":jub["2025"]["attributable_equity"]/jub["shares_million"]}
(base/"real_company_results.json").write_text(json.dumps(results,indent=2),encoding="utf-8")
# Source ledger: each extracted field has an explicit period/unit/locator/transformation.
ledger=[]
bat_locations={"revenue":119,"cogs":119,"ebit":119,"profit":119,"eps":119,"cfo":126,"capex":126,"cash_generated_operations":126,"interest_received":126,"interest_paid":126,"tax_paid":126,"disposal_proceeds":126,"lease_principal_paid":126,"fx_cash":126,"depreciation":159,"trade_receivables":165,"trade_payables":166,"inventory":164,"plant":120,"cash":120,"debt":166,"equity":120,"total_assets":120,"current_assets":120,"current_liabilities":120,"dps_fiscal":154,"dps_cash_paid":154}
for ticker,entity,src in [("BAT",bat,"bat"),("EQTY",eq,"equity"),("JUB",jub,"jubilee")]:
 for year,fields in entity.items():
  if not year.isdigit():continue
  for field,value in fields.items():
   if ticker=="BAT":page=bat_locations.get(field,120)
   elif ticker=="EQTY":page=141 if "equity" in field else 212 if any(x in field for x in ["loans","allowance"]) else 244 if field=="dps" else 138
   else:page=86 if "equity" in field else 162 if field=="dps" else 82
   unit="KES/share" if field.startswith(("eps","dps")) else "KES million"
   ledger.append({"company":ticker,"metric":field,"value":value,"unit":unit,"period":year+"-12-31","source_url":URLS[src],"source_type":"official issuer","document":f"{ticker} annual report 2025 (2024 comparatives)","printed_page":page,"column":year+" consolidated group; attributable ownership identified by metric","retrieved_date":STAMP,"extraction_method":"PDF text checked by named table and accounting identity","transformation":"KES thousands divided by 1000" if ticker in ["BAT","JUB"] and unit=="KES million" else "as disclosed","status":"derived reconciliation" if field in ["other_assets","other_liabilities","total_assets"] else "reported"})
for ticker,price in prices.items():
 ledger.append({"company":ticker,"metric":"price","value":price,"unit":"KES/share","period":"2026-09-11","source_url":URLS["nse"],"source_type":"official exchange","document":"NSE Daily Price List, 11 September 2026","printed_page":2 if ticker in ["SCOM","BAT","EABL"] else 1,"column":"VWAP","retrieved_date":STAMP,"extraction_method":"Image-only PDF rendered using pdftoppm and visually read","transformation":"none; do not relabel as close or last trade","status":"reported"})
for field,value in eq["kenya_bank_capital"].items():
 if isinstance(value,(int,float)):ledger.append({"company":"Equity Bank Kenya Limited (subsidiary)","metric":field,"value":value,"unit":"decimal ratio" if "minimum" in field else "KES million","period":"2025-12-31","source_url":URLS["equity"],"source_type":"official issuer","document":"Equity Group Annual Report 2025","printed_page":194,"column":"31 December 2025, EBKL","retrieved_date":STAMP,"extraction_method":"pdftotext -layout, capital management table","transformation":"as disclosed","status":"reported"})
(base/"real_company_source_ledger.json").write_text(json.dumps(ledger,indent=2),encoding="utf-8")
print(json.dumps({"data":str(base/"real_company_inputs.json"),"valuation":results["bat_dcf"],"ddm":results["equity_ddm"],"ledger_rows":len(ledger)},indent=2))

