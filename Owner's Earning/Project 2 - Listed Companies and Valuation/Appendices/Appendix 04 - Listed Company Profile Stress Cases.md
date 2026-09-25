# Appendix 04 — Listed-company profile stress cases

### Companion to Project 2, Parts 7–10

This appendix documents the `Profile Stress` worksheet added to the [Project 2 listed-company workbook](../Project%202%20-%20Listed%20Companies%20Owner%20Earnings%20and%20Valuation.xlsx). It tests whether different business and asset profiles respond differently to a named operating shock. The worksheet uses normalized index values and analyst-selected scenario shocks; none is an issuer forecast, reported dollar amount, valuation, or measured probability.

## A4.1 Calculation method

Each profile starts with an illustrative cash-capacity index of 100. The workbook subtracts a profile-specific reinvestment or capital-retention index and a priority-claims index:

`Base residual index = base cash-capacity index − base reinvestment/retention index − base priority-claims index`

It then applies a cash shock and separate shocks to reinvestment/retention and priority claims:

`Stressed residual index = cash × (1 + cash shock) − reinvestment × (1 + reinvestment shock) − priority claims × (1 + claims shock)`

For example, the NVIDIA row uses 100, −20%, 35, +10%, 10 and +25% respectively. Its base residual is 55 index points; stressed residual is 29. The result illustrates why semiconductor demand and margin exposure can interact with inventory and capacity commitments. It does not claim NVIDIA's true owner earnings are 55 units or that its cash generation will fall by 20%.

## A4.2 Profiles and scenario outputs

| Market | Business / asset profile | Illustrative base residual | Illustrative stressed residual | Main shock represented |
|---|---|---:|---:|---|
| US | NVIDIA: semiconductor, inventory and supply commitments | 55.0 | 29.0 | Demand/margin decline with higher inventory and capacity cash needs |
| US | Equinix: data-centre infrastructure, power and renewal | 30.0 | 9.0 | Utilization/power pressure, renewal spending and fixed claims |
| NSE | Equity Group: bank credit and regulatory capital | 35.0 | 5.3 | Credit-loss decline with higher retention and capital needs |
| NSE | Jubilee: insurance claims, reserves and solvency | 35.0 | 0.8 | Claims/reserve pressure with restricted remittances and solvency needs |
| NSE | KenGen: power generation, plant renewal and construction | 40.0 | 2.8 | Lower cash alongside higher project/renewal needs and slower collections |
| NSE | Kakuzi: agribusiness, crop yield and seasonal working capital | 55.0 | 22.0 | Lower crop receipts with more seasonal cash tied up |
| NSE | Safaricom: telecom network renewal and expansion | 45.0 | 22.5 | Service-cash pressure and higher network/spectrum/expansion needs |
| NSE | BAT Kenya: manufacturing, volume, tax and replacement | 45.0 | 22.8 | Lower volume/cash conversion alongside higher tax and renewal pressure |
| NSE | Home Afrika: property completion costs and collections | 30.0 | −11.3 | Slower customer collections and cost overruns against debt claims |

Rounding in this table is to one decimal. Inputs are changeable in the workbook, and the workbook calculates from unrounded values. A negative residual is an illustrative funding gap under that row's assumptions; it is not evidence of an actual liquidity shortfall at Home Afrika or any other named company.

## A4.3 Why the same formula does not mean the same economics

The sheet standardizes only the **scenario arithmetic**, not the underlying financial definition. The cash-capacity index could represent a cash-earnings proxy for one non-financial company and an earnings/capital proxy for a bank or insurer. Those are not directly comparable. Use the row as a prompt to select correct underlying schedules:

- **NVIDIA:** reconcile net income to operating cash flow, all relevant working-capital balances, stock-based compensation, supply commitments and maintenance investment. Receivables and inventory uses alone are not net working-capital investment.
- **Equinix:** separate renewal, capacity expansion, leases, power cost, utilization and construction funding. Issuer-defined recurring capex does not by itself establish total maintenance needs.
- **Bank:** measure credit costs, retained earnings, risk-weighted assets, binding capital requirements and the management buffer. A bank's deposits and loans do not fit a conventional retail cash-conversion-cycle model.
- **Insurer:** reconcile underwriting, investment result, claims development, reinsurance, subsidiary solvency and parent-level permitted remittances. Premium cash is not free cash.
- **Power generation:** distinguish plant maintenance from growth projects and test output, tariff, fuel or hydrology, debt service and offtaker collection timing.
- **Agribusiness:** test harvest volumes, crop mix, shipment timing, biological-asset measurements, seasonal inventory, receivables and supplier funding.
- **Telecom:** separate network renewal from expansion and spectrum, leases, mobile-money regulation, subsidiary investment and currency exposure.
- **Manufacturing:** test volume, price/mix, excise and tax remittances, inventory, supplier terms and replacement equipment.
- **Property:** work project by project through cost to complete, customer deposits, restrictions, completed sales, collections, debt and entity-level claims.

## A4.4 What the cases answer—and do not answer

The sheet answers: “If this profile suffered the displayed operating shock while its reinvestment and priority cash needs also moved as shown, would its illustrative headroom rise or fall?” It does not answer how likely a shock is, what a named issuer's actual cash capacity equals, which listed company is more valuable, or how the stock should be priced. The values 100, 35 and the scenario percentages are deliberately transparent analyst inputs so readers can see and change the mechanics.

The detailed NVIDIA filing bridge and valuation remain in `Filing Inputs`, `NVDA Bridge`, `Assumptions` and `Valuation`. The NSE issuer facts and source IDs remain in `NSE Casebook`; the bank and insurer context remains in `Bank Insurance`. The profile worksheet adds a common stress interface across two US examples and seven NSE industry cases. It does not replace those issuer-specific schedules or fill their missing data.

Before converting any row into a company estimate, replace every index value and shock with dated, sourced inputs, preserve the issuer/legal-entity perimeter, and provide low/base/high scenarios grounded in filing notes, operating records and contractual cash obligations. For regulated firms, obtain regulator returns and entity-level capital. For non-financial firms, reconcile cash earnings, required operating working capital, maintenance, growth investment and senior claims.

## Workbook check

The builder tests that each of the nine profile scenarios calculates a finite stressed residual below its base residual. That test checks the formulas' directional response to the chosen shocks. It does not empirically validate the assumptions or imply that every real-world downside must reduce cash in this exact pattern.
