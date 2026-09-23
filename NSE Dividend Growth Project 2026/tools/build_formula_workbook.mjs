import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const outputDir = path.join(root, "Publication", "Output");
await fs.mkdir(outputDir, { recursive: true });

const wb = Workbook.create();
const inputs = wb.worksheets.add("Inputs");
const core = wb.worksheets.add("Core Portfolio");
const dca = wb.worksheets.add("DCA Plan");
const income = wb.worksheets.add("Income Scenarios");
const dictionary = wb.worksheets.add("Formula Dictionary");

const colors = {
  ink: "#173D33",
  sage: "#E8EDDF",
  paper: "#F8F7F2",
  orange: "#CE6939",
  line: "#D8DED4",
  input: "#0000FF",
  linked: "#008000",
  black: "#000000",
};
const font = "Arial";
const titleStyle = { font: { name: font, size: 16, bold: true, color: colors.ink } };
const subtitleStyle = { font: { name: font, size: 10, italic: true, color: "#66736A" } };
const sectionStyle = { fill: colors.ink, font: { name: font, size: 10, bold: true, color: "#FFFFFF" } };
const headerStyle = { fill: "#24374B", font: { name: font, size: 10, bold: true, color: "#FFFFFF" }, horizontalAlignment: "center", verticalAlignment: "center", wrapText: true };
const bodyStyle = { font: { name: font, size: 10, color: colors.black }, verticalAlignment: "center" };
const inputStyle = { fill: "#FFF2CC", font: { name: font, size: 10, color: colors.input }, verticalAlignment: "center" };
const border = { preset: "all", style: "thin", color: colors.line };

function title(sheet, value, subtitle, width = "A1:H1") {
  sheet.getRange(width).merge();
  sheet.getRange("A1").values = [[value]];
  sheet.getRange("A1").format = titleStyle;
  sheet.getRange(width).format.borders = { bottom: { style: "thin", color: colors.line } };
  const subtitleRange = "A2:" + width.split(":")[1].replace("1", "2");
  sheet.getRange(subtitleRange).merge();
  sheet.getRange("A2").values = [[subtitle]];
  sheet.getRange("A2").format = subtitleStyle;
}

function section(sheet, cell, label, width) {
  sheet.getRange(width).merge();
  sheet.getRange(cell).values = [[label]];
  sheet.getRange(cell).format = sectionStyle;
}

function setWidths(sheet, specs) {
  for (const [range, width] of specs) sheet.getRange(range).format.columnWidth = width;
}

for (const sheet of [inputs, core, dca, income, dictionary]) {
  sheet.showGridLines = false;
  sheet.tabColor = colors.ink;
}

title(inputs, "NSE Dividend Growth DCA Inputs", "Research snapshot: 10 September 2026. All live prices require an update before use.", "A1:F1");
section(inputs, "A5", "Portfolio inputs", "A5:F5");
inputs.getRange("A6:C12").values = [
  ["Input", "Value", "Unit"],
  ["Total cash", 100000, "KES"],
  ["Maximum transaction cost", 0.021, "%"],
  ["Deployment months", 3, "months"],
  ["Resident withholding tax", 0.05, "%"],
  ["Price reference date", "9 September 2026", "date"],
  ["Research snapshot", "10 September 2026", "date"],
];
inputs.getRange("A6:C6").format = headerStyle;
inputs.getRange("A7:C12").format = bodyStyle;
inputs.getRange("B7:B11").format = inputStyle;
inputs.getRange("A6:C12").format.borders = border;
inputs.getRange("B7").format.numberFormat = '#,##0.00';
inputs.getRange("B8").format.numberFormat = "0.00%";
inputs.getRange("B9").format.numberFormat = "0";
inputs.getRange("B10").format.numberFormat = "0.00%";
section(inputs, "A15", "Core counter inputs", "A15:H15");
inputs.getRange("A16:H23").values = [
  ["Counter", "Ticker", "Reference price", "Dividend per share", "Target weight", "Role", "Price date", "Source"],
  ["Safaricom", "SCOM", 36.65, 2.00, 0.20, "Core growth and income", "9 September 2026", "myStocks [1]"],
  ["Equity Group", "EQTY", 101.50, 5.75, 0.15, "Growth and income bank", "9 September 2026", "myStocks [1]"],
  ["Co-operative Bank", "COOP", 37.85, 2.50, 0.15, "Growth and income bank", "9 September 2026", "myStocks [1]"],
  ["Standard Chartered Kenya", "SCBK", 349.25, 31.00, 0.15, "Income bank", "9 September 2026", "myStocks [1]"],
  ["BAT Kenya", "BAT", 559.00, 70.00, 0.15, "Income equity", "9 September 2026", "myStocks [1]"],
  ["East African Breweries", "EABL", 285.25, 12.70, 0.10, "Consumer diversification", "9 September 2026", "myStocks [1]"],
  ["Nairobi Securities Exchange", "NSE", 28.20, 1.00, 0.10, "Market infrastructure", "9 September 2026", "myStocks [1]"],
];
inputs.getRange("A16:H16").format = headerStyle;
inputs.getRange("A17:H23").format = bodyStyle;
inputs.getRange("C17:E23").format = inputStyle;
inputs.getRange("A16:H23").format.borders = border;
inputs.getRange("C17:D23").format.numberFormat = '#,##0.00';
inputs.getRange("E17:E23").format.numberFormat = "0.0%";
inputs.getRange("A26:H27").merge();
inputs.getRange("A26").values = [["Source context: prices and stated dividend basis come from the manuscript's 9 September 2026 research snapshot. The worksheets are structured so inputs can be refreshed before a new order."]];
inputs.getRange("A26").format = subtitleStyle;
inputs.getRange("A26").format.wrapText = true;
inputs.getRange("A26").format.rowHeight = 36;
setWidths(inputs, [["A:A", 28], ["B:B", 12], ["C:D", 16], ["E:E", 14], ["F:F", 28], ["G:G", 18], ["H:H", 15]]);
inputs.freezePanes.freezeRows(6);

title(core, "Core Portfolio Construction", "Target allocation, transaction-cost reserve and indicative annual dividend income.", "A1:J1");
section(core, "A5", "Portfolio summary", "A5:D5");
core.getRange("A6:B10").values = [
  ["Metric", "Value"],
  ["Total cash", null],
  ["Investable securities", null],
  ["Transaction-cost provision", null],
  ["Monthly securities budget", null],
];
core.getRange("A6:B6").format = headerStyle;
core.getRange("A7:B10").format = bodyStyle;
core.getRange("A6:B10").format.borders = border;
core.getRange("B7:B10").formulas = [
  ["='Inputs'!B7"],
  ["=B7/(1+'Inputs'!B8)"],
  ["=B7-B8"],
  ["=B8/'Inputs'!B9"],
];
core.getRange("B7:B10").format.numberFormat = '#,##0.00';
section(core, "A13", "Core allocation and dividend income", "A13:J13");
core.getRange("A14:J21").values = [
  ["Counter", "Ticker", "Price", "Dividend per share", "Target weight", "Target capital", "Indicative yield", "Gross annual dividend", "Withholding tax", "Net annual dividend"],
  ["Safaricom", "SCOM", null, null, null, null, null, null, null, null],
  ["Equity Group", "EQTY", null, null, null, null, null, null, null, null],
  ["Co-operative Bank", "COOP", null, null, null, null, null, null, null, null],
  ["Standard Chartered Kenya", "SCBK", null, null, null, null, null, null, null, null],
  ["BAT Kenya", "BAT", null, null, null, null, null, null, null, null],
  ["East African Breweries", "EABL", null, null, null, null, null, null, null, null],
  ["Nairobi Securities Exchange", "NSE", null, null, null, null, null, null, null, null],
];
core.getRange("A14:J14").format = headerStyle;
core.getRange("A15:J21").format = bodyStyle;
core.getRange("A14:J21").format.borders = border;
core.getRange("C15").formulas = [["='Inputs'!C17"]];
core.getRange("D15").formulas = [["='Inputs'!D17"]];
core.getRange("E15").formulas = [["='Inputs'!E17"]];
core.getRange("C15:E21").fillDown();
core.getRange("F15").formulas = [["=$B$8*E15"]];
core.getRange("F15:F21").fillDown();
core.getRange("G15").formulas = [["=D15/C15"]];
core.getRange("G15:G21").fillDown();
core.getRange("H15").formulas = [["=F15*G15"]];
core.getRange("H15:H21").fillDown();
core.getRange("I15").formulas = [["=H15*'Inputs'!$B$10"]];
core.getRange("I15:I21").fillDown();
core.getRange("J15").formulas = [["=H15-I15"]];
core.getRange("J15:J21").fillDown();
core.getRange("A22:J22").values = [["Portfolio total", "", "", "", "=SUM(E15:E21)", "=SUM(F15:F21)", "=SUM(H15:H21)/SUM(F15:F21)", "=SUM(H15:H21)", "=SUM(I15:I21)", "=SUM(J15:J21)"]];
core.getRange("A22:J22").format = { fill: colors.sage, font: { name: font, size: 10, bold: true, color: colors.black } };
core.getRange("A22:J22").format.borders = { top: { style: "double", color: colors.ink } };
core.getRange("C15:D21").format.numberFormat = '#,##0.00';
core.getRange("E15:E22").format.numberFormat = "0.0%";
core.getRange("F15:F22").format.numberFormat = '#,##0.00';
core.getRange("G15:G22").format.numberFormat = "0.00%";
core.getRange("H15:J22").format.numberFormat = '#,##0.00';
setWidths(core, [["A:A", 29], ["B:B", 10], ["C:D", 14], ["E:E", 13], ["F:F", 16], ["G:G", 14], ["H:J", 18]]);
core.freezePanes.freezeRows(14);

title(dca, "Three Month DCA Plan", "Whole-share quantities recompute from prices, weights and each month's investable securities budget.", "A1:J1");
section(dca, "A5", "Monthly allocation inputs", "A5:E5");
dca.getRange("A6:E9").values = [
  ["Month", "Securities budget", "Cost provision", "Total cash commitment", "Reference basis"],
  ["Month 1", null, null, null, "Illustration using 9 September 2026 prices"],
  ["Month 2", null, null, null, "Replace price inputs before execution"],
  ["Month 3", null, null, null, "Replace price inputs before execution"],
];
dca.getRange("A6:E6").format = headerStyle;
dca.getRange("A7:E9").format = bodyStyle;
dca.getRange("A6:E9").format.borders = border;
dca.getRange("B7").formulas = [["='Core Portfolio'!$B$10"]];
dca.getRange("B7:B9").fillDown();
dca.getRange("C7").formulas = [["='Core Portfolio'!$B$9/'Inputs'!$B$9"]];
dca.getRange("C7:C9").fillDown();
dca.getRange("D7").formulas = [["=B7+C7"]];
dca.getRange("D7:D9").fillDown();
dca.getRange("B7:D9").format.numberFormat = '#,##0.00';
section(dca, "A12", "Month one whole-share illustration", "A12:H12");
dca.getRange("A13:H20").values = [
  ["Counter", "Target weight", "Monthly target", "Reference price", "Illustrative shares", "Approx. share cost", "Uncommitted amount", "Cost plus maximum fees"],
  ["Safaricom", null, null, null, null, null, null, null],
  ["Equity Group", null, null, null, null, null, null, null],
  ["Co-operative Bank", null, null, null, null, null, null, null],
  ["Standard Chartered Kenya", null, null, null, null, null, null, null],
  ["BAT Kenya", null, null, null, null, null, null, null],
  ["East African Breweries", null, null, null, null, null, null, null],
  ["Nairobi Securities Exchange", null, null, null, null, null, null, null],
];
dca.getRange("A13:H13").format = headerStyle;
dca.getRange("A14:H20").format = bodyStyle;
dca.getRange("A13:H20").format.borders = border;
dca.getRange("B14").formulas = [["='Core Portfolio'!E15"]];
dca.getRange("B14:B20").fillDown();
dca.getRange("C14").formulas = [["=$B$7*B14"]];
dca.getRange("C14:C20").fillDown();
dca.getRange("D14").formulas = [["='Core Portfolio'!C15"]];
dca.getRange("D14:D20").fillDown();
dca.getRange("E14").formulas = [["=ROUNDDOWN(C14/D14,0)"]];
dca.getRange("E14:E20").fillDown();
dca.getRange("F14").formulas = [["=E14*D14"]];
dca.getRange("F14:F20").fillDown();
dca.getRange("G14").formulas = [["=C14-F14"]];
dca.getRange("G14:G20").fillDown();
dca.getRange("H14").formulas = [["=F14*(1+'Inputs'!$B$8)"]];
dca.getRange("H14:H20").fillDown();
dca.getRange("A21:H21").values = [["Total", "=SUM(B14:B20)", "=SUM(C14:C20)", "", "=SUM(E14:E20)", "=SUM(F14:F20)", "=SUM(G14:G20)", "=SUM(H14:H20)"]];
dca.getRange("A21:H21").format = { fill: colors.sage, font: { name: font, size: 10, bold: true, color: colors.black } };
dca.getRange("A21:H21").format.borders = { top: { style: "double", color: colors.ink } };
dca.getRange("B14:B21").format.numberFormat = "0.0%";
dca.getRange("C14:D21").format.numberFormat = '#,##0.00';
dca.getRange("E14:E21").format.numberFormat = '#,##0';
dca.getRange("F14:H21").format.numberFormat = '#,##0.00';
setWidths(dca, [["A:A", 29], ["B:B", 14], ["C:D", 17], ["E:E", 16], ["F:H", 19]]);
dca.freezePanes.freezeRows(13);

title(income, "Dividend Income Scenarios", "A simple scenario analysis of the core portfolio's dividend income, excluding share-price movements.", "A1:G1");
section(income, "A5", "Scenario inputs and results", "A5:G5");
income.getRange("A6:G9").values = [
  ["Scenario", "Dividend change", "Gross income", "Withholding tax", "Net income", "Net yield on total cash", "Interpretation"],
  ["Dividends fall 20%", -0.20, null, null, null, null, "Lower distribution scenario"],
  ["Recent dividends repeated", 0, null, null, null, null, "Reference case"],
  ["Dividends increase 10%", 0.10, null, null, null, null, "Higher distribution scenario"],
];
income.getRange("A6:G6").format = headerStyle;
income.getRange("A7:G9").format = bodyStyle;
income.getRange("A6:G9").format.borders = border;
income.getRange("B7:B9").format = inputStyle;
income.getRange("C7").formulas = [["='Core Portfolio'!$H$22*(1+B7)"]];
income.getRange("C7:C9").fillDown();
income.getRange("D7").formulas = [["=C7*'Inputs'!$B$10"]];
income.getRange("D7:D9").fillDown();
income.getRange("E7").formulas = [["=C7-D7"]];
income.getRange("E7:E9").fillDown();
income.getRange("F7").formulas = [["=E7/'Inputs'!$B$7"]];
income.getRange("F7:F9").fillDown();
income.getRange("B7:B9").format.numberFormat = "0.0%";
income.getRange("C7:E9").format.numberFormat = '#,##0.00';
income.getRange("F7:F9").format.numberFormat = "0.00%";
income.getRange("A12:G14").merge();
income.getRange("A12").values = [["Interpretation: these scenarios change dividend income only. They retain the project’s stated 5% resident withholding-tax assumption and do not model capital gains or losses."]];
income.getRange("A12").format = subtitleStyle;
income.getRange("A12").format.wrapText = true;
income.getRange("A12").format.rowHeight = 34;
setWidths(income, [["A:A", 28], ["B:B", 16], ["C:E", 17], ["F:F", 19], ["G:G", 26]]);

title(dictionary, "Formula Dictionary", "Exact Excel expressions, mathematical equivalences and formula locations in this workbook.", "A1:F1");
dictionary.getRange("A5:F15").values = [
  ["Calculation", "Excel expression", "Mathematical equivalence", "Workbook location", "Inputs", "Purpose"],
  ["Investable securities", "'=B7/(1+'Inputs'!B8)", "S = C / (1 + c)", "Core Portfolio!B8", "Total cash; transaction cost", "Reserves maximum transaction costs before securities allocation"],
  ["Cost provision", "'=B7-B8", "F = C - S", "Core Portfolio!B9", "Total cash; investable securities", "Shows cash reserved for transaction costs"],
  ["Monthly securities budget", "'=B8/'Inputs'!B9", "M = S / n", "Core Portfolio!B10", "Investable securities; deployment months", "Sets the securities budget for each purchase month"],
  ["Target capital", "'=$B$8*E15", "A_i = S x w_i", "Core Portfolio!F15:F21", "Investable securities; target weight", "Allocates target capital to each counter"],
  ["Indicative yield", "'=D15/C15", "y_i = D_i / P_i", "Core Portfolio!G15:G21", "Dividend per share; reference price", "Calculates stated dividend yield at the reference price"],
  ["Gross annual dividend", "'=F15*G15", "G_i = A_i x y_i", "Core Portfolio!H15:H21", "Target capital; yield", "Estimates annual gross dividend income"],
  ["Withholding tax", "'=H15*'Inputs'!B10", "T = G x t", "Core Portfolio!I15:I21", "Gross income; tax rate", "Applies the selected resident withholding-tax rate"],
  ["Net annual dividend", "'=H15-I15", "N = G - T", "Core Portfolio!J15:J21", "Gross income; withholding tax", "Calculates net annual dividend income"],
  ["Whole shares", "'=ROUNDDOWN(C14/D14,0)", "q_i = floor(M x w_i / P_i)", "DCA Plan!E14:E20", "Monthly target; price", "Rounds purchase quantities down to whole shares"],
  ["Scenario gross income", "'='Core Portfolio'!H22*(1+B7)", "G_s = G x (1 + s)", "Income Scenarios!C7:C9", "Base gross income; scenario change", "Applies a dividend-change scenario"],
  ["Scenario net yield", "'=E7/'Inputs'!B7", "y_net = N / C", "Income Scenarios!F7:F9", "Net income; total cash", "Expresses net income as a yield on total cash"],
];
dictionary.getRange("A5:F5").format = headerStyle;
dictionary.getRange("A6:F16").format = bodyStyle;
dictionary.getRange("A5:F16").format.borders = border;
dictionary.getRange("B6:B16").format = { fill: colors.sage, font: { name: "Consolas", size: 9, color: colors.black }, wrapText: true, verticalAlignment: "top" };
dictionary.getRange("C6:F16").format.wrapText = true;
dictionary.getRange("A6:F16").format.verticalAlignment = "top";
setWidths(dictionary, [["A:A", 23], ["B:B", 35], ["C:C", 27], ["D:D", 27], ["E:E", 34], ["F:F", 42]]);
dictionary.getRange("A6:F16").format.autofitRows();
dictionary.freezePanes.freezeRows(5);

const inputCheck = await wb.inspect({ kind: "table", range: "Inputs!A6:H23", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 8 });
const formulaCheck = await wb.inspect({ kind: "formula", range: "Core Portfolio!A6:J22", maxChars: 6000, options: { maxResults: 80 } });
const errors = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!", options: { useRegex: true, maxResults: 100 }, summary: "formula error scan" });
console.log(inputCheck.ndjson);
console.log(formulaCheck.ndjson);
console.log(errors.ndjson);

for (const [sheetName, fileName] of [["Inputs", "formula-workbook-inputs.png"], ["Core Portfolio", "formula-workbook-core.png"], ["DCA Plan", "formula-workbook-dca.png"], ["Income Scenarios", "formula-workbook-income.png"], ["Formula Dictionary", "formula-workbook-dictionary.png"]]) {
  const preview = await wb.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(path.join(outputDir, fileName), new Uint8Array(await preview.arrayBuffer()));
}
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(path.join(outputDir, "NSE Dividend Growth Formula Workbook.xlsx"));
console.log("Saved NSE Dividend Growth Formula Workbook.xlsx");
