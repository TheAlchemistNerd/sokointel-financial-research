"""
Build script for US Markets and Portfolio Construction - companion workbook.
Builds every calculator referenced across the five-part article series and its appendices.
Run with: python3 build_workbook.py
Then recalculate with: python3 /mnt/skills/public/xlsx/scripts/recalc.py <output>.xlsx
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BLUE = Font(name="Arial", color="0000FF")
BLUE_BOLD = Font(name="Arial", color="0000FF", bold=True)
BLACK = Font(name="Arial", color="000000")
BLACK_BOLD = Font(name="Arial", color="000000", bold=True)
GREEN = Font(name="Arial", color="008000")
TITLE = Font(name="Arial", color="000000", bold=True, size=14)
HEADER = Font(name="Arial", color="FFFFFF", bold=True)
HEADER_FILL = PatternFill(start_color="305496", end_color="305496", fill_type="solid")
YELLOW_FILL = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
NOTE = Font(name="Arial", color="595959", italic=True, size=9)
thin = Side(style="thin", color="B7B7B7")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

CUR = '$#,##0.00;($#,##0.00)'
CUR0 = '$#,##0;($#,##0)'
PCT = '0.00%'
PCT1 = '0.0%'
PCT3 = '0.000%'

wb = openpyxl.Workbook()
wb.remove(wb.active)

def sheet(name):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    return ws

def title(ws, cell, text, width=None):
    ws[cell] = text
    ws[cell].font = TITLE
    if width:
        ws.merge_cells(f"{cell}:{width}")

def header_row(ws, row, col_start, headers):
    for i, h in enumerate(headers):
        c = ws.cell(row=row, column=col_start+i, value=h)
        c.font = HEADER
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal="center", wrap_text=True)
        c.border = BORDER

def note(ws, cell, text):
    ws[cell] = text
    ws[cell].font = NOTE
    ws[cell].alignment = Alignment(wrap_text=True, vertical="top")

def setcol(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

# =========================================================================
# GUIDE SHEET
# =========================================================================
g = sheet("Guide")
setcol(g, [38, 70])
title(g, "A1", "US Markets and Portfolio Construction — Companion Workbook", "F1")
g["A2"] = "Every calculation table and worked example across the five-part article series, live and editable."
g["A2"].font = Font(name="Arial", italic=True, size=11)

g["A4"] = "Color legend"
g["A4"].font = BLACK_BOLD
g["A5"] = "Blue text"; g["A5"].font = BLUE
g["B5"] = "A supplied input or assumption. Change these — every formula recalculates."
g["A6"] = "Black text"
g["B6"] = "A formula that calculates using only cells on the same worksheet."
g["A7"] = "Green text"; g["A7"].font = GREEN
g["B7"] = "A formula that pulls a value from a different worksheet in this workbook."
g["A8"] = "Yellow fill"
g["A8"].fill = YELLOW_FILL
g["B8"] = "A key assumption worth double-checking before relying on the sheet."

g["A10"] = "Sheet index"
g["A10"].font = BLACK_BOLD
sheets_index = [
    ("P1 - Cost of Ownership", "Expense-ratio compounding across six vehicles; Part 1, Table 1 and Appendix 1."),
    ("P1 - NRA Tax", "Nonresident-alien dividend withholding and US estate-tax threshold calculators; Part 1 / Appendix 1."),
    ("P2 - Diversification", "Two- and three-asset portfolio variance, with a correlation-sensitivity table; Part 2 / Appendix 2."),
    ("P2 - Blended ER", "Weighted blended expense ratio for a multi-sleeve core-satellite portfolio; Part 2, Table 2."),
    ("P3 - HHI Concentration", "Herfindahl-Hirschman Index and effective-N calculator for up to 30 holdings; Part 3 / Appendix 3."),
    ("P4 - Matrix Variance", "Four-asset portfolio variance in matrix form; Part 4, Equation 4.1 / Appendix 4."),
    ("P4 - Options Wheel", "Cash-secured put and covered-call cycle economics; Part 4, Table 1 / Appendix 4."),
    ("P4 - Tax Calculators", "Qualified-dividend, wash-sale, and 2026 long-term capital-gains bracket calculators; Part 4."),
    ("P5 - Rebalancing", "One-year drift and the rebalancing trade required to restore target weights; Part 5, Table 2 / Appendix 5."),
    ("P5 - DCA vs Lump Sum", "Lump-sum vs. dollar-cost-averaging comparison under two illustrative return paths; Part 5, Table 1."),
    ("P5 - Sequence of Returns", "Identical average return, reordered, showing the effect of withdrawal timing; Part 5, Table 3 / Appendix 5."),
    ("P5 - Case Study", "Ten-year accumulation projection for the full worked case study; Part 5, Table 4 / Appendix 5."),
]
r = 11
for name, desc in sheets_index:
    g.cell(row=r, column=1, value=name).font = BLACK_BOLD
    g.cell(row=r, column=2, value=desc).font = BLACK
    g.cell(row=r, column=2).alignment = Alignment(wrap_text=True)
    r += 1

note(g, "A25", "All growth-rate, volatility, correlation, and yield figures throughout this workbook are clearly labelled "
              "illustrative assumptions for demonstration purposes, matching the corresponding article text — not "
              "forecasts, and not personalized financial or tax advice. Expense ratios, statutory tax thresholds, and "
              "index-methodology facts are sourced from the primary sources cited in each article's reference list, "
              "current as of the 'Accessed' dates shown there.")
g.merge_cells("A25:B25")
g.row_dimensions[25].height = 60

print("Guide sheet built.")

# =========================================================================
# P1 - COST OF OWNERSHIP
# =========================================================================
s = sheet("P1 - Cost of Ownership")
setcol(s, [30, 12, 12, 14, 14, 14, 16])
title(s, "A1", "Part 1 — Cost of Ownership: Expense-Ratio Compounding", "G1")
note(s, "A2", "Change the principal or gross-return assumption below (blue) and every fund's projected value recalculates.")
s.merge_cells("A2:G2")

s["A4"] = "Initial principal ($)"; s["A4"].font = BLACK
s["B4"] = 10000; s["B4"].font = BLUE; s["B4"].number_format = CUR0
s["A5"] = "Assumed gross annual return (before fees)"; s["A5"].font = BLACK
s["B5"] = 0.08; s["B5"].font = BLUE; s["B5"].number_format = PCT1
note(s, "D4", "Equation 1.1: FV = P × (1 + r − e)^n. r and the horizon (10/20/30y) are the only assumptions; "
              "everything else on this sheet is a live formula.")
s.merge_cells("D4:G5")

headers = ["Vehicle", "Expense ratio", "Net return (r−e)", "Value after 10y", "Value after 20y", "Value after 30y", "30y cost vs. cheapest"]
header_row(s, 7, 1, headers)
funds = [
    ("SPYM (S&P 500)", 0.0002),
    ("VOO / IVV (S&P 500)", 0.0003),
    ("SPY (S&P 500, UIT)", 0.000945),
    ("QQQM (Nasdaq-100)", 0.0015),
    ("QQQ (Nasdaq-100)", 0.0018),
    ("Illustrative actively managed fund", 0.0075),
]
first_row = 8
for i, (name, er) in enumerate(funds):
    rr = first_row + i
    s.cell(row=rr, column=1, value=name).font = BLACK
    c = s.cell(row=rr, column=2, value=er); c.font = BLUE; c.number_format = PCT3
    c = s.cell(row=rr, column=3, value=f"=$B$5-B{rr}"); c.font = BLACK; c.number_format = PCT3
    for j, yrs in enumerate([10, 20, 30]):
        col = 4 + j
        cl = get_column_letter(col)
        c = s.cell(row=rr, column=col, value=f"=$B$4*(1+C{rr})^{yrs}")
        c.font = BLACK; c.number_format = CUR
    for rr2 in range(first_row, first_row+len(funds)):
        pass
last_row = first_row + len(funds) - 1
for i in range(len(funds)):
    rr = first_row + i
    c = s.cell(row=rr, column=7, value=f"=$F${first_row}-F{rr}")
    c.font = BLACK; c.number_format = CUR
for col in range(1, 8):
    s.cell(row=first_row-1, column=col).border = BORDER
for rr in range(first_row, last_row+1):
    for col in range(1, 8):
        s.cell(row=rr, column=col).border = BORDER

note(s, f"A{last_row+2}", "Row 1 (SPYM) is the cheapest vehicle in this illustration, so its own 30-year cost-vs-cheapest is $0 by construction.")
s.merge_cells(f"A{last_row+2}:G{last_row+2}")

# Sensitivity block (Appendix 1, A1.3)
srow = last_row + 4
s.cell(row=srow, column=1, value="Sensitivity: 30-year value at different gross-return assumptions (Appendix 1, A1.3)").font = BLACK_BOLD
s.merge_cells(f"A{srow}:G{srow}")
header_row(s, srow+1, 1, ["Gross return"] + [f[0] for f in funds])
sens_returns = [0.03, 0.06, 0.08, 0.10, 0.12]
for i, gr in enumerate(sens_returns):
    rr = srow + 2 + i
    c = s.cell(row=rr, column=1, value=gr); c.font = BLUE; c.number_format = PCT1
    for j, (name, er) in enumerate(funds):
        col = 2+j
        c = s.cell(row=rr, column=col, value=f"=$B$4*(1+$A{rr}-{'$B$'+str(first_row+j)})^30")
        c.font = BLACK; c.number_format = CUR
    for col in range(1, 8):
        s.cell(row=rr, column=col).border = BORDER
header_row2_row = srow+1
for col in range(1,8):
    s.cell(row=header_row2_row, column=col).border=BORDER

# =========================================================================
# P1 - NRA TAX
# =========================================================================
s = sheet("P1 - NRA Tax")
setcol(s, [32, 16, 16, 16, 16])
title(s, "A1", "Part 1 — Nonresident-Alien Withholding and Estate-Tax Thresholds", "E1")

s["A3"] = "1. Dividend withholding"; s["A3"].font = BLACK_BOLD
s["A4"] = "Position size ($)"; s["B4"] = 10000; s["B4"].font = BLUE; s["B4"].number_format = CUR0
s["A5"] = "Illustrative annual yield"; s["B5"] = 0.013; s["B5"].font = BLUE; s["B5"].number_format = PCT1
s["A6"] = "No-treaty statutory withholding rate"; s["B6"] = 0.30; s["B6"].font = BLUE; s["B6"].number_format = PCT1
s["A7"] = "Illustrative treaty withholding rate"; s["B7"] = 0.15; s["B7"].font = BLUE; s["B7"].number_format = PCT1

header_row(s, 9, 1, ["", "Gross annual dividend", "Withholding rate", "Tax withheld", "Net received"])
s["A10"] = "No treaty"; s["A10"].font=BLACK
s["B10"] = "=$B$4*$B$5"; s["B10"].font=BLACK; s["B10"].number_format=CUR
s["C10"] = "=$B$6"; s["C10"].font=BLACK; s["C10"].number_format=PCT1
s["D10"] = "=B10*C10"; s["D10"].font=BLACK; s["D10"].number_format=CUR
s["E10"] = "=B10-D10"; s["E10"].font=BLACK; s["E10"].number_format=CUR
s["A11"] = "Illustrative treaty"; s["A11"].font=BLACK
s["B11"] = "=$B$4*$B$5"; s["B11"].font=BLACK; s["B11"].number_format=CUR
s["C11"] = "=$B$7"; s["C11"].font=BLACK; s["C11"].number_format=PCT1
s["D11"] = "=B11*C11"; s["D11"].font=BLACK; s["D11"].number_format=CUR
s["E11"] = "=B11-D11"; s["E11"].font=BLACK; s["E11"].number_format=CUR
s["A12"] = "Annual gap from lacking a treaty"; s["A12"].font=BLACK
s["D12"] = "=D10-D11"; s["D12"].font=BLACK; s["D12"].number_format=CUR
for row in range(9,13):
    for col in range(1,6):
        s.cell(row=row,column=col).border=BORDER

s["A14"] = "2. US estate tax — Table A unified rate schedule (IRC §2001(c))"; s["A14"].font = BLACK_BOLD
header_row(s, 15, 1, ["Bracket lower", "Bracket upper", "Base tax at lower bound", "Marginal rate on excess"])
brackets = [
    (0, 10000, 0, 0.18), (10000, 20000, 1800, 0.20), (20000, 40000, 3800, 0.22),
    (40000, 60000, 8200, 0.24), (60000, 80000, 13000, 0.26), (80000, 100000, 18200, 0.28),
    (100000, 150000, 23800, 0.30), (150000, 250000, 38800, 0.32), (250000, 500000, 70800, 0.34),
    (500000, 750000, 155800, 0.37), (750000, 1000000, 248300, 0.39), (1000000, 100000000, 345800, 0.40),
]
brow = 16
for lo, hi, base, rate in brackets:
    s.cell(row=brow, column=1, value=lo).font=BLUE; s.cell(row=brow,column=1).number_format=CUR0
    s.cell(row=brow, column=2, value=hi).font=BLUE; s.cell(row=brow,column=2).number_format=CUR0
    s.cell(row=brow, column=3, value=base).font=BLUE; s.cell(row=brow,column=3).number_format=CUR0
    s.cell(row=brow, column=4, value=rate).font=BLUE; s.cell(row=brow,column=4).number_format=PCT1
    for col in range(1,5):
        s.cell(row=brow,column=col).border=BORDER
    brow += 1
last_bracket_row = brow - 1

s["A29"] = "Unified credit (nonresident alien)"; s["B29"]=13000; s["B29"].font=BLUE; s["B29"].number_format=CUR0
s["A30"] = "US-situs gross estate to evaluate"; s["B30"]=150000; s["B30"].font=BLUE; s["B30"].fill=YELLOW_FILL; s["B30"].number_format=CUR0

s["A32"] = "Bracket found (MATCH)"
s["B32"] = "=MATCH(B30,A16:A27)"
s["B32"].font = BLACK
s["A33"] = "Base tax at that bracket"
s["B33"] = "=INDEX(C16:C27,B32)"
s["B33"].font = BLACK; s["B33"].number_format=CUR
s["A34"] = "Rate on excess"
s["B34"] = "=INDEX(D16:D27,B32)"
s["B34"].font = BLACK; s["B34"].number_format=PCT1
s["A35"] = "Bracket lower bound"
s["B35"] = "=INDEX(A16:A27,B32)"
s["B35"].font = BLACK; s["B35"].number_format=CUR0
s["A36"] = "Tentative tax (Table A)"
s["B36"] = "=B33+B34*(B30-B35)"
s["B36"].font = BLACK_BOLD; s["B36"].number_format=CUR
s["A37"] = "Less: unified credit"
s["B37"] = "=$B$29"
s["B37"].font = BLACK; s["B37"].number_format=CUR
s["A38"] = "Net US estate tax"
s["B38"] = "=MAX(0,B36-B37)"
s["B38"].font = BLACK_BOLD; s["B38"].number_format=CUR
s["A39"] = "Form 706-NA filing required?"
s["B39"] = '=IF(B30>=60000,"Yes","No")'
s["B39"].font = BLACK

note(s, "D29", "Change the yellow cell (B30) to any US-situs estate value; the bracket lookup, tentative tax, "
              "and net tax below all recalculate via MATCH/INDEX against the Table A schedule above.")
s.merge_cells("D29:E33")

# =========================================================================
# P2 - DIVERSIFICATION
# =========================================================================
s = sheet("P2 - Diversification")
setcol(s, [26, 14, 14, 16, 18])
title(s, "A1", "Part 2 — Two-Asset Diversification Mathematics (Equation 2.1)", "E1")

s["A3"] = "Equity weight (w1)"; s["B3"]=0.70; s["B3"].font=BLUE; s["B3"].number_format=PCT1
s["A4"] = "Bond weight (w2, = 1-w1)"; s["B4"]="=1-B3"; s["B4"].font=BLACK; s["B4"].number_format=PCT1
s["A5"] = "Equity volatility (sigma1)"; s["B5"]=0.16; s["B5"].font=BLUE; s["B5"].number_format=PCT1
s["A6"] = "Bond volatility (sigma2)"; s["B6"]=0.06; s["B6"].font=BLUE; s["B6"].number_format=PCT1
s["A7"] = "Correlation (rho)"; s["B7"]=0.10; s["B7"].font=BLUE; s["B7"].number_format=PCT1

s["A9"]="Portfolio variance"; s["B9"]="=B3^2*B5^2+B4^2*B6^2+2*B3*B4*B7*B5*B6"; s["B9"].font=BLACK; s["B9"].number_format='0.00000'
s["A10"]="Portfolio standard deviation"; s["B10"]="=SQRT(B9)"; s["B10"].font=BLACK_BOLD; s["B10"].number_format=PCT
s["A11"]="Naive linear-weighted SD"; s["B11"]="=B3*B5+B4*B6"; s["B11"].font=BLACK; s["B11"].number_format=PCT
s["A12"]="Diversification benefit"; s["B12"]="=B11-B10"; s["B12"].font=BLACK_BOLD; s["B12"].number_format=PCT
for r in range(3,13):
    s.cell(row=r,column=1).border=BORDER; s.cell(row=r,column=2).border=BORDER

# Correlation sensitivity table (Appendix 2, A2.2)
s["A15"]="Sensitivity to the correlation assumption (weights and vols fixed at rows 3-6)"; s["A15"].font=BLACK_BOLD
s.merge_cells("A15:E15")
header_row(s,16,1,["Correlation (rho)","Portfolio SD","Naive linear blend","Diversification benefit",""])
rhos = [-0.30,-0.10,0.0,0.10,0.30,0.50,1.00]
rrow=17
for rho in rhos:
    s.cell(row=rrow,column=1,value=rho).font=BLUE; s.cell(row=rrow,column=1).number_format=PCT1
    s.cell(row=rrow,column=2,value=f"=SQRT($B$3^2*$B$5^2+$B$4^2*$B$6^2+2*$B$3*$B$4*A{rrow}*$B$5*$B$6)").font=BLACK
    s.cell(row=rrow,column=2).number_format=PCT
    s.cell(row=rrow,column=3,value="=$B$11").font=BLACK; s.cell(row=rrow,column=3).number_format=PCT
    s.cell(row=rrow,column=4,value=f"=C{rrow}-B{rrow}").font=BLACK; s.cell(row=rrow,column=4).number_format=PCT
    for c in range(1,5):
        s.cell(row=rrow,column=c).border=BORDER
    rrow+=1

# Three-asset example (Appendix 2, A2.3)
s3row = rrow+2
s.cell(row=s3row,column=1,value="Three-asset variance (Appendix 2, A2.3): equity core, bond core, sector satellite").font=BLACK_BOLD
s.merge_cells(f"A{s3row}:E{s3row}")
header_row(s, s3row+1, 1, ["Asset","Weight","Volatility","",""])
assets3 = [("Equity core (eq)",0.55,0.16),("Bond core (bd)",0.15,0.06),("Sector satellite (sat)",0.30,0.28)]
a3start = s3row+2
for i,(name,w,vol) in enumerate(assets3):
    rr=a3start+i
    s.cell(row=rr,column=1,value=name).font=BLACK
    s.cell(row=rr,column=2,value=w).font=BLUE; s.cell(row=rr,column=2).number_format=PCT1
    s.cell(row=rr,column=3,value=vol).font=BLUE; s.cell(row=rr,column=3).number_format=PCT1
    for c in range(1,4):
        s.cell(row=rr,column=c).border=BORDER
corr_row = a3start+3
s.cell(row=corr_row,column=1,value="Correlation eq-bd").font=BLACK
s.cell(row=corr_row,column=2,value=0.10).font=BLUE; s.cell(row=corr_row,column=2).number_format=PCT1
s.cell(row=corr_row+1,column=1,value="Correlation eq-sat").font=BLACK
s.cell(row=corr_row+1,column=2,value=0.75).font=BLUE; s.cell(row=corr_row+1,column=2).number_format=PCT1
s.cell(row=corr_row+2,column=1,value="Correlation bd-sat").font=BLACK
s.cell(row=corr_row+2,column=2,value=0.05).font=BLUE; s.cell(row=corr_row+2,column=2).number_format=PCT1

var3_row = corr_row+4
w_eq,w_bd,w_sat = f"B{a3start}", f"B{a3start+1}", f"B{a3start+2}"
v_eq,v_bd,v_sat = f"C{a3start}", f"C{a3start+1}", f"C{a3start+2}"
r_ebd, r_esat, r_bsat = f"B{corr_row}", f"B{corr_row+1}", f"B{corr_row+2}"
formula3 = (f"={w_eq}^2*{v_eq}^2+{w_bd}^2*{v_bd}^2+{w_sat}^2*{v_sat}^2"
            f"+2*{w_eq}*{w_bd}*{r_ebd}*{v_eq}*{v_bd}"
            f"+2*{w_eq}*{w_sat}*{r_esat}*{v_eq}*{v_sat}"
            f"+2*{w_bd}*{w_sat}*{r_bsat}*{v_bd}*{v_sat}")
s.cell(row=var3_row,column=1,value="Three-asset portfolio variance").font=BLACK
s.cell(row=var3_row,column=2,value=formula3).font=BLACK; s.cell(row=var3_row,column=2).number_format='0.00000'
s.cell(row=var3_row+1,column=1,value="Three-asset portfolio SD").font=BLACK_BOLD
s.cell(row=var3_row+1,column=2,value=f"=SQRT(B{var3_row})").font=BLACK_BOLD; s.cell(row=var3_row+1,column=2).number_format=PCT
s.cell(row=var3_row+2,column=1,value="Naive linear blend").font=BLACK
naive3 = f"={w_eq}*{v_eq}+{w_bd}*{v_bd}+{w_sat}*{v_sat}"
s.cell(row=var3_row+2,column=2,value=naive3).font=BLACK; s.cell(row=var3_row+2,column=2).number_format=PCT
s.cell(row=var3_row+3,column=1,value="Diversification benefit").font=BLACK_BOLD
s.cell(row=var3_row+3,column=2,value=f"=B{var3_row+2}-B{var3_row+1}").font=BLACK_BOLD; s.cell(row=var3_row+3,column=2).number_format=PCT

# =========================================================================
# P2 - BLENDED ER
# =========================================================================
s = sheet("P2 - Blended ER")
setcol(s, [40, 12, 12, 14, 20])
title(s, "A1", "Part 2 — Blended Expense Ratio of a Core-Satellite Portfolio", "E1")
s["A3"]="Total portfolio value ($)"; s["B3"]=50000; s["B3"].font=BLUE; s["B3"].number_format=CUR0

header_row(s,5,1,["Sleeve","Weight","Expense ratio","$ Value","Weighted contribution to blended ER"])
sleeves = [
    ("SPYM (S&P 500 core)",0.55,0.0002),
    ("AGG (US aggregate bond core)",0.15,0.0003),
    ("QQQM (Nasdaq-100, core-plus growth tilt)",0.15,0.0015),
    ("Dividend-quality satellite (e.g., SCHD)",0.075,0.0006),
    ("Sector satellite (e.g., semiconductors)",0.075,0.0033),
]
srow=6
for name,w,er in sleeves:
    s.cell(row=srow,column=1,value=name).font=BLACK
    s.cell(row=srow,column=2,value=w).font=BLUE; s.cell(row=srow,column=2).number_format=PCT1
    s.cell(row=srow,column=3,value=er).font=BLUE; s.cell(row=srow,column=3).number_format=PCT3
    s.cell(row=srow,column=4,value=f"=$B$3*B{srow}").font=BLACK; s.cell(row=srow,column=4).number_format=CUR
    s.cell(row=srow,column=5,value=f"=B{srow}*C{srow}").font=BLACK; s.cell(row=srow,column=5).number_format=PCT3
    for c in range(1,6):
        s.cell(row=srow,column=c).border=BORDER
    srow+=1
total_row = srow
s.cell(row=total_row,column=1,value="Total").font=BLACK_BOLD
s.cell(row=total_row,column=2,value=f"=SUM(B6:B{total_row-1})").font=BLACK_BOLD; s.cell(row=total_row,column=2).number_format=PCT1
s.cell(row=total_row,column=4,value=f"=SUM(D6:D{total_row-1})").font=BLACK_BOLD; s.cell(row=total_row,column=4).number_format=CUR
s.cell(row=total_row,column=5,value=f"=SUM(E6:E{total_row-1})").font=BLACK_BOLD; s.cell(row=total_row,column=5).number_format=PCT3
for c in range(1,6):
    s.cell(row=total_row,column=c).border=BORDER

s.cell(row=total_row+2,column=1,value="Annual dollar cost of the blended ER").font=BLACK
s.cell(row=total_row+2,column=2,value=f"=$B$3*E{total_row}").font=BLACK_BOLD; s.cell(row=total_row+2,column=2).number_format=CUR

# Two risk-posture variants (Part 2, "same framework two risk postures")
vrow = total_row+4
s.cell(row=vrow,column=1,value="Two risk-posture variants").font=BLACK_BOLD
s.merge_cells(f"A{vrow}:E{vrow}")
header_row(s,vrow+1,1,["Sleeve","Conservative weight","Growth-oriented weight","",""])
variant_data = [
    ("SPYM (S&P 500 core)",0.35,0.55),
    ("AGG (bond core)",0.45,0.05),
    ("QQQM (growth tilt)",0.05,0.20),
    ("Dividend-quality satellite",0.10,0.05),
    ("Sector satellite",0.05,0.15),
]
vstart = vrow+2
for name,wc,wg in variant_data:
    rr=vstart+variant_data.index((name,wc,wg))
    s.cell(row=rr,column=1,value=name).font=BLACK
    s.cell(row=rr,column=2,value=wc).font=BLUE; s.cell(row=rr,column=2).number_format=PCT1
    s.cell(row=rr,column=3,value=wg).font=BLUE; s.cell(row=rr,column=3).number_format=PCT1
    for c in range(1,4):
        s.cell(row=rr,column=c).border=BORDER
vend = vstart+len(variant_data)-1
s.cell(row=vend+1,column=1,value="Blended ER (using expense ratios from the table above)").font=BLACK_BOLD
cons_formula = "=" + "+".join([f"B{vstart+i}*C{6+i}" for i in range(len(variant_data))])
grow_formula = "=" + "+".join([f"C{vstart+i}*C{6+i}" for i in range(len(variant_data))])
s.cell(row=vend+1,column=2,value=cons_formula).font=BLACK_BOLD; s.cell(row=vend+1,column=2).number_format=PCT3
s.cell(row=vend+1,column=3,value=grow_formula).font=BLACK_BOLD; s.cell(row=vend+1,column=3).number_format=PCT3

# =========================================================================
# P3 - HHI CONCENTRATION
# =========================================================================
s = sheet("P3 - HHI Concentration")
setcol(s, [10, 14, 30, 14])
title(s, "A1", "Part 3 — Herfindahl-Hirschman Index and Effective-N Calculator", "D1")
note(s, "A2", "Paste up to 30 holding weights (as decimals, e.g. 0.08 for 8%) into column B. Unused rows can be left at 0%.")
s.merge_cells("A2:D2")

header_row(s,4,1,["#","Weight","",""])
illustrative_equal = [1/30]*30
for i in range(30):
    rr=5+i
    s.cell(row=rr,column=1,value=i+1).font=BLACK
    s.cell(row=rr,column=2,value=round(illustrative_equal[i],6)).font=BLUE
    s.cell(row=rr,column=2).number_format=PCT3
    for c in range(1,3):
        s.cell(row=rr,column=c).border=BORDER

s["A36"]="Sum of weights (should be 100%)"; s["B36"]="=SUM(B5:B34)"; s["B36"].font=BLACK; s["B36"].number_format=PCT1
s["A37"]="HHI (=SUMSQ of weights)"; s["B37"]="=SUMSQ(B5:B34)"; s["B37"].font=BLACK_BOLD; s["B37"].number_format='0.0000'
s["A38"]="Effective N (=1/HHI)"; s["B38"]="=1/B37"; s["B38"].font=BLACK_BOLD; s["B38"].number_format='0.0'
s["A39"]="Nominal count of nonzero holdings"; s["B39"]='=COUNTIF(B5:B34,">0")'; s["B39"].font=BLACK

note(s,"D4","This sheet ships pre-loaded with a pure equal-weight, 30-holding example "
            "(effective N should equal 30.0). Overwrite column B with any fund's actual "
            "published weights to check its real concentration.")
s.merge_cells("D4:D10")

# Reference scenarios from Appendix 3, A3.1 and A3.2
rrow=42
s.cell(row=rrow,column=1,value="Reference: equal-weight effective N at different nominal N (Appendix 3, A3.1)").font=BLACK_BOLD
s.merge_cells(f"A{rrow}:D{rrow}")
header_row(s,rrow+1,1,["Nominal N","HHI (=1/N)","Effective N (=N)","" ])
ns = [10,25,30,50,100,500]
nstart=rrow+2
for i,n in enumerate(ns):
    rr=nstart+i
    s.cell(row=rr,column=1,value=n).font=BLUE
    s.cell(row=rr,column=2,value=f"=1/A{rr}").font=BLACK; s.cell(row=rr,column=2).number_format='0.00000'
    s.cell(row=rr,column=3,value=f"=1/B{rr}").font=BLACK; s.cell(row=rr,column=3).number_format='0.0'
    for c in range(1,4):
        s.cell(row=rr,column=c).border=BORDER

# Single dominant holding scenario (Appendix 3, A3.2)
drow = nstart+len(ns)+2
s.cell(row=drow,column=1,value="Reference: effect of one dominant holding in an otherwise-equal 30-name fund (Appendix 3, A3.2)").font=BLACK_BOLD
s.merge_cells(f"A{drow}:D{drow}")
header_row(s,drow+1,1,["Top holding weight","Each remaining holding","HHI","Effective N"])
dstart=drow+2
tops=[0.0333,0.05,0.08,0.10,0.15,0.20,0.25]
for i,top in enumerate(tops):
    rr=dstart+i
    s.cell(row=rr,column=1,value=top).font=BLUE; s.cell(row=rr,column=1).number_format=PCT1
    s.cell(row=rr,column=2,value=f"=(1-A{rr})/29").font=BLACK; s.cell(row=rr,column=2).number_format=PCT3
    s.cell(row=rr,column=3,value=f"=A{rr}^2+29*B{rr}^2").font=BLACK; s.cell(row=rr,column=3).number_format='0.0000'
    s.cell(row=rr,column=4,value=f"=1/C{rr}").font=BLACK; s.cell(row=rr,column=4).number_format='0.0'
    for c in range(1,5):
        s.cell(row=rr,column=c).border=BORDER

# =========================================================================
# P4 - MATRIX VARIANCE
# =========================================================================
s = sheet("P4 - Matrix Variance")
setcol(s, [22, 12, 12, 12, 12])
title(s, "A1", "Part 4 — Four-Asset Portfolio Variance (Equation 4.1: sigma_p^2 = w'.Sigma.w)", "E1")

assets4 = ["SPYM","AGG","QQQM","Satellite blend"]
s["A3"]="Weights"; s["A3"].font=BLACK_BOLD
header_row(s,4,2,assets4)
weights4=[0.55,0.15,0.15,0.15]
for i,w in enumerate(weights4):
    c=s.cell(row=5,column=2+i,value=w); c.font=BLUE; c.number_format=PCT1
s["A5"]="Weight"; s["A5"].font=BLACK

s["A7"]="Volatilities (annualized)"; s["A7"].font=BLACK_BOLD
vols4=[0.16,0.06,0.22,0.28]
header_row(s,8,2,assets4)
for i,v in enumerate(vols4):
    c=s.cell(row=9,column=2+i,value=v); c.font=BLUE; c.number_format=PCT1
s["A9"]="Volatility"; s["A9"].font=BLACK

s["A11"]="Correlation matrix"; s["A11"].font=BLACK_BOLD
header_row(s,12,2,assets4)
corr4 = [
    [1.00,0.10,0.85,0.75],
    [0.10,1.00,0.05,0.05],
    [0.85,0.05,1.00,0.65],
    [0.75,0.05,0.65,1.00],
]
for i,name in enumerate(assets4):
    rr=13+i
    s.cell(row=rr,column=1,value=name).font=BLACK
    for j in range(4):
        c=s.cell(row=rr,column=2+j,value=corr4[i][j]); c.font=BLUE; c.number_format=PCT1
        c.border=BORDER
    s.cell(row=rr,column=1).border=BORDER
for c in range(1,6):
    s.cell(row=12,column=c).border=BORDER

s["A18"]="Covariance matrix (=vol_i * vol_j * rho_ij)"; s["A18"].font=BLACK_BOLD
header_row(s,19,2,assets4)
for i,name in enumerate(assets4):
    rr=20+i
    s.cell(row=rr,column=1,value=name).font=BLACK
    for j in range(4):
        vol_i_cell = f"{get_column_letter(2+i)}$9"
        vol_j_cell = f"{get_column_letter(2+j)}$9"
        corr_cell = f"{get_column_letter(2+j)}{13+i}"
        c=s.cell(row=rr,column=2+j,value=f"={vol_i_cell}*{vol_j_cell}*{corr_cell}")
        c.font=BLACK; c.number_format='0.0000'; c.border=BORDER
    s.cell(row=rr,column=1).border=BORDER
for c in range(1,6):
    s.cell(row=19,column=c).border=BORDER

# Portfolio variance = w' Sigma w, expanded as full double sum
varrow=25
s.cell(row=varrow,column=1,value="Portfolio variance (full double-sum expansion of w'.Sigma.w)").font=BLACK_BOLD
terms = []
for i in range(4):
    for j in range(4):
        wi = f"${get_column_letter(2+i)}$5"
        wj = f"${get_column_letter(2+j)}$5"
        cov = f"{get_column_letter(2+j)}{20+i}"
        terms.append(f"{wi}*{wj}*{cov}")
formula = "=" + "+".join(terms)
s.cell(row=varrow+1,column=1,value="Portfolio variance").font=BLACK
s.cell(row=varrow+1,column=2,value=formula).font=BLACK_BOLD; s.cell(row=varrow+1,column=2).number_format='0.00000'
s.cell(row=varrow+2,column=1,value="Portfolio standard deviation").font=BLACK_BOLD
s.cell(row=varrow+2,column=2,value=f"=SQRT(B{varrow+1})").font=BLACK_BOLD; s.cell(row=varrow+2,column=2).number_format=PCT
s.cell(row=varrow+3,column=1,value="Naive linear-weighted SD").font=BLACK
naive4 = "=" + "+".join([f"{get_column_letter(2+i)}$5*{get_column_letter(2+i)}$9" for i in range(4)])
s.cell(row=varrow+3,column=2,value=naive4).font=BLACK; s.cell(row=varrow+3,column=2).number_format=PCT
s.cell(row=varrow+4,column=1,value="Diversification benefit").font=BLACK_BOLD
s.cell(row=varrow+4,column=2,value=f"=B{varrow+3}-B{varrow+2}").font=BLACK_BOLD; s.cell(row=varrow+4,column=2).number_format=PCT

note(s, f"D{varrow+1}", "The formula in B{0} is the full 16-term double sum (4x4) behind Equation 4.1 — "
                        "algebraically identical to the compact w'.Sigma.w matrix notation used in the article.".format(varrow+1))
s.merge_cells(f"D{varrow+1}:E{varrow+4}")

# =========================================================================
# P4 - OPTIONS WHEEL
# =========================================================================
s = sheet("P4 - Options Wheel")
setcol(s, [30, 14, 14])
title(s, "A1", "Part 4 — Options Wheel: Cash-Secured Put + Covered Call Cycle", "C1")

s["A3"]="Stage 1: Cash-secured put"; s["A3"].font=BLACK_BOLD
s["A4"]="Current stock price"; s["B4"]=100; s["B4"].font=BLUE; s["B4"].number_format=CUR
s["A5"]="Put strike"; s["B5"]=90; s["B5"].font=BLUE; s["B5"].number_format=CUR
s["A6"]="Put premium (per share)"; s["B6"]=2.00; s["B6"].font=BLUE; s["B6"].number_format=CUR
s["A7"]="Contracts"; s["B7"]=1; s["B7"].font=BLUE
s["A9"]="Collateral required (strike x 100 x contracts)"; s["B9"]="=B5*100*B7"; s["B9"].font=BLACK; s["B9"].number_format=CUR
s["A10"]="Premium collected (premium x 100 x contracts)"; s["B10"]="=B6*100*B7"; s["B10"].font=BLACK; s["B10"].number_format=CUR
s["A11"]="Breakeven if assigned (strike - premium)"; s["B11"]="=B5-B6"; s["B11"].font=BLACK; s["B11"].number_format=CUR
s["A12"]="Return on collateral if put expires worthless"; s["B12"]="=B10/B9"; s["B12"].font=BLACK_BOLD; s["B12"].number_format=PCT
s["A13"]="Naive annualized (x12, no compounding, illustrative only)"; s["B13"]="=B12*12"; s["B13"].font=BLACK; s["B13"].number_format=PCT1

for r in range(4,14):
    s.cell(row=r,column=1).border=BORDER; s.cell(row=r,column=2).border=BORDER

s["A16"]="Stage 2: If assigned -> covered call"; s["A16"].font=BLACK_BOLD
s["A17"]="Effective cost basis after assignment (=B11)"; s["B17"]="=B11"; s["B17"].font=BLACK; s["B17"].number_format=CUR
s["A18"]="Covered call strike"; s["B18"]=95; s["B18"].font=BLUE; s["B18"].number_format=CUR
s["A19"]="Covered call premium (per share)"; s["B19"]=1.50; s["B19"].font=BLUE; s["B19"].number_format=CUR
s["A20"]="Effective sale price if called away (strike+premium)"; s["B20"]="=B18+B19"; s["B20"].font=BLACK; s["B20"].number_format=CUR
s["A21"]="Combined gain per share across full cycle"; s["B21"]="=B20-B17"; s["B21"].font=BLACK_BOLD; s["B21"].number_format=CUR
s["A22"]="Combined gain, 100 shares"; s["B22"]="=B21*100*B7"; s["B22"].font=BLACK_BOLD; s["B22"].number_format=CUR
s["A23"]="Total return on effective basis across the cycle"; s["B23"]="=B21/B17"; s["B23"].font=BLACK_BOLD; s["B23"].number_format=PCT
for r in range(17,24):
    s.cell(row=r,column=1).border=BORDER; s.cell(row=r,column=2).border=BORDER

s["A25"]="Adverse scenario: stock falls after assignment"; s["A25"].font=BLACK_BOLD
s["A26"]="Illustrative crash price"; s["B26"]=70; s["B26"].font=BLUE; s["B26"].fill=YELLOW_FILL; s["B26"].number_format=CUR
s["A27"]="Unrealized loss per share vs. effective basis"; s["B27"]="=B17-B26"; s["B27"].font=BLACK; s["B27"].number_format=CUR
s["A28"]="Unrealized loss, 100 shares"; s["B28"]="=B27*100*B7"; s["B28"].font=BLACK_BOLD; s["B28"].number_format=CUR
s["A29"]="Premium income collected so far (Stage 1 only)"; s["B29"]="=B10"; s["B29"].font=BLACK; s["B29"].number_format=CUR
s["A30"]="Net position (premium less unrealized loss)"; s["B30"]="=B29-B28"; s["B30"].font=BLACK_BOLD; s["B30"].number_format=CUR
for r in range(26,31):
    s.cell(row=r,column=1).border=BORDER; s.cell(row=r,column=2).border=BORDER

# Strike sensitivity table (Appendix 4, A4.2)
srow=33
s.cell(row=srow,column=1,value="Sensitivity: yield at different strike selections (Appendix 4, A4.2)").font=BLACK_BOLD
s.merge_cells(f"A{srow}:C{srow}")
header_row(s,srow+1,1,["Strike","Premium (per share)","Period yield on collateral"])
strikes=[(95,3.50),(90,2.00),(85,1.10),(80,0.60)]
sstart=srow+2
for i,(k,p) in enumerate(strikes):
    rr=sstart+i
    s.cell(row=rr,column=1,value=k).font=BLUE; s.cell(row=rr,column=1).number_format=CUR
    s.cell(row=rr,column=2,value=p).font=BLUE; s.cell(row=rr,column=2).number_format=CUR
    s.cell(row=rr,column=3,value=f"=(B{rr}*100)/(A{rr}*100)").font=BLACK; s.cell(row=rr,column=3).number_format=PCT
    for c in range(1,4):
        s.cell(row=rr,column=c).border=BORDER

# =========================================================================
# P4 - TAX CALCULATORS
# =========================================================================
s = sheet("P4 - Tax Calculators")
setcol(s, [34, 16, 16, 16])
title(s, "A1", "Part 4 — Dividend, Wash-Sale, and Capital-Gains Tax Calculators", "D1")

s["A3"]="1. Qualified vs. non-qualified dividend"; s["A3"].font=BLACK_BOLD
s["A4"]="Dividend payout"; s["B4"]=1000; s["B4"].font=BLUE; s["B4"].number_format=CUR0
s["A5"]="Qualified (LTCG) rate"; s["B5"]=0.15; s["B5"].font=BLUE; s["B5"].number_format=PCT1
s["A6"]="Ordinary marginal rate"; s["B6"]=0.24; s["B6"].font=BLUE; s["B6"].number_format=PCT1
s["A7"]="Tax if qualified"; s["B7"]="=B4*B5"; s["B7"].font=BLACK; s["B7"].number_format=CUR
s["A8"]="Tax if non-qualified"; s["B8"]="=B4*B6"; s["B8"].font=BLACK; s["B8"].number_format=CUR
s["A9"]="Net if qualified"; s["B9"]="=B4-B7"; s["B9"].font=BLACK; s["B9"].number_format=CUR
s["A10"]="Net if non-qualified"; s["B10"]="=B4-B8"; s["B10"].font=BLACK; s["B10"].number_format=CUR
s["A11"]="Difference"; s["B11"]="=B8-B7"; s["B11"].font=BLACK_BOLD; s["B11"].number_format=CUR
for r in range(4,12):
    s.cell(row=r,column=1).border=BORDER; s.cell(row=r,column=2).border=BORDER

s["A13"]="2. Wash-sale rule"; s["A13"].font=BLACK_BOLD
s["A14"]="Shares"; s["B14"]=100; s["B14"].font=BLUE
s["A15"]="Buy price"; s["B15"]=50; s["B15"].font=BLUE; s["B15"].number_format=CUR
s["A16"]="Sell price (at a loss)"; s["B16"]=40; s["B16"].font=BLUE; s["B16"].number_format=CUR
s["A17"]="Realized loss"; s["B17"]="=(B15-B16)*B14"; s["B17"].font=BLACK; s["B17"].number_format=CUR
s["A18"]="Repurchase price (within 30 days)"; s["B18"]=41; s["B18"].font=BLUE; s["B18"].number_format=CUR
s["A19"]="Shares repurchased within the window"; s["B19"]=100; s["B19"].font=BLUE
s["A20"]="Disallowed portion of the loss"; s["B20"]="=B17*(B19/B14)"; s["B20"].font=BLACK; s["B20"].number_format=CUR
s["A21"]="Allowed loss this year (not repurchased)"; s["B21"]="=B17-B20"; s["B21"].font=BLACK; s["B21"].number_format=CUR
s["A22"]="New position cost (repurchase price x shares)"; s["B22"]="=B18*B19"; s["B22"].font=BLACK; s["B22"].number_format=CUR
s["A23"]="New basis after adding disallowed loss"; s["B23"]="=B22+B20"; s["B23"].font=BLACK_BOLD; s["B23"].number_format=CUR
s["A24"]="New basis per share"; s["B24"]="=B23/B19"; s["B24"].font=BLACK_BOLD; s["B24"].number_format=CUR
for r in range(14,25):
    s.cell(row=r,column=1).border=BORDER; s.cell(row=r,column=2).border=BORDER

s["A26"]="3. 2026 long-term capital-gains bracket calculator (single filer, Rev. Proc. 2025-32)"; s["A26"].font=BLACK_BOLD
s["A27"]="Ordinary taxable income"; s["B27"]=100000; s["B27"].font=BLUE; s["B27"].fill=YELLOW_FILL; s["B27"].number_format=CUR0
s["A28"]="Long-term capital gain"; s["B28"]=50000; s["B28"].font=BLUE; s["B28"].fill=YELLOW_FILL; s["B28"].number_format=CUR0
s["A29"]="0% bracket ceiling"; s["B29"]=49450; s["B29"].font=BLUE; s["B29"].number_format=CUR0
s["A30"]="15% bracket ceiling"; s["B30"]=545500; s["B30"].font=BLUE; s["B30"].number_format=CUR0
s["A31"]="Total income (ordinary + gain)"; s["B31"]="=B27+B28"; s["B31"].font=BLACK; s["B31"].number_format=CUR0
s["A32"]="Amount taxed at 0%"; s["B32"]="=MAX(0,MIN(B31,B29)-MAX(B27,0))"; s["B32"].font=BLACK; s["B32"].number_format=CUR0
s["A33"]="Amount taxed at 15%"; s["B33"]="=MAX(0,MIN(B31,B30)-MAX(B27,B29))"; s["B33"].font=BLACK; s["B33"].number_format=CUR0
s["A34"]="Amount taxed at 20%"; s["B34"]="=MAX(0,B31-MAX(B27,B30))"; s["B34"].font=BLACK; s["B34"].number_format=CUR0
s["A35"]="LTCG tax owed"; s["B35"]="=B32*0+B33*0.15+B34*0.2"; s["B35"].font=BLACK_BOLD; s["B35"].number_format=CUR
s["A36"]="Effective rate on the gain"; s["B36"]="=B35/B28"; s["B36"].font=BLACK_BOLD; s["B36"].number_format=PCT1
for r in range(27,37):
    s.cell(row=r,column=1).border=BORDER; s.cell(row=r,column=2).border=BORDER

note(s,"D27","Change the two yellow cells (ordinary income, gain). The bracket math correctly "
             "handles a gain that straddles more than one bracket, stacking it on top of ordinary income.")
s.merge_cells("D27:D33")

wb.save("/home/claude/work/output/Workbook/US_Markets_Portfolio_Construction_Workbook.xlsx")
print("Saved checkpoint 9 (P4 Tax Calculators added).")
