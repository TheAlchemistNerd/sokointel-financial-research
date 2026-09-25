# Equation export verification

Local verification fixture, 25 September 2026. Not a replacement publication edition.

## MSME owner earnings and cash headroom

\[ \mathrm{OE} = N + D + A - M - \Delta W \]

OE is estimated annual owner earnings; N is annual normalized net income after replacing owner labour; D is depreciation/amortisation already expensed; A is other justified noncash adjustment; M is annual maintenance investment; ΔW is an increase in required operating working capital. All are KES/year. A release of working capital is negative.

\[ H = C + R - U - X - B, \qquad H_{\mathrm{reviewed}} = H - Q \]

H is dated headroom, C stated available cash, R additional confirmed collections, U listed due uses, X restricted cash, B the retained reserve and Q the disputed/uncollected amount counted in C or R. All are KES over the stated cash horizon. Subtract the proposed draw from reviewed H.

## Thirteen-week operating cash planner

\[ C_t = C_{t-1} + R_t + E_t + F_t - U_t \]

Cₜ is week-end cash; Cₜ₋₁ is opening cash; Rₜ is operating cash received, Eₜ new owner funds, Fₜ new borrowing and Uₜ all scheduled cash uses. Values are KES in week t; t runs from 1 to 13.

\[ \text{Reserve funding need} = \max\!\left(0, B - \min_{0 \leq t \leq 13} C_t\right) \]

B is the chosen KES reserve floor and C₀ opening unrestricted cash. This is the initial buffer required to cover the deepest forecast gap, assuming the remaining cash flows are unchanged.

## Business cash stress and warning planner

\[ C_t = C_{t-1} + R_t + E_t + F_t - U_t \]

All terms are KES for week t: closing cash C, operating receipts R, new owner funds E, new borrowing F and all cash uses U. Opening cash C₀ is unrestricted. No emergency financing is inserted automatically.

\[ \mathrm{CCC} = \mathrm{DIO} + \mathrm{DSO} - \mathrm{DPO} \]

CCC is the cash conversion cycle in days. DIO is inventory days, DSO receivable days and DPO payable days. Use comparable periods and denominators; overdue claims still require review.

\[ \text{Extra weekly cash cost} = S \times \frac{m_b - m_s}{100} \]

S is the illustrative KES weekly sales input, mᵦ base contribution margin and mₛ downside margin, entered as percentages. This stress assumes constant sales and immediately paid variable costs; it is separate from editable baseline supplier payments.

## Detailed business credit and repayment planner

\[ I_j = B_j r \frac{\Delta d_j}{Y}, \qquad \text{cost} = \sum_j I_j + \text{fees} \]

Iⱼ is interest for interval j (KES), Bⱼ its opening principal (KES), r annual nominal rate as a decimal, Δdⱼ actual whole days in that interval and Y the chosen 360/365 day basis. Fees are percentage-of-original-principal plus fixed KES fees.

\[ N = P - \text{withheld charges}, \qquad \sum_j \frac{R_j}{(1+y)^{d_j/365}} = N \]

N is net day-zero advance and P actual original principal, both KES. Rⱼ is the KES repayment at day dⱼ after draw. y is the effective annual cash-flow yield, solved from the displayed dated repayments; a 365-day year is used for this yield.

\[ \text{Simple annualised cost} = \frac{\text{cost}}{P} \times \frac{365}{d} \]

P is original principal and d the facility tenor in days. This simple principal-based comparison differs from the cash-flow yield and is not a regulatory APR.

## Unicode exception (retained verbatim)

FV = PV × (1 + r)ⁿ. σ² is variance.