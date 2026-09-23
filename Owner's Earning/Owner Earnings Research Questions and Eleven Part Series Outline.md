# Owner Earnings: Research Questions and Eleven-Part Series Outline

> **Traceability note, 22 September 2026:** This eleven-part outline is preserved as the original editorial plan. The active plan is [Canonical Research Programme - Three Projects and Thirteen Parts.md](Canonical%20Research%20Programme%20-%20Three%20Projects%20and%20Thirteen%20Parts.md), informed by the separate [Supplemental Source Record - MSME Operations and Failure Analysis.md](Supplemental%20Source%20Record%20-%20MSME%20Operations%20and%20Failure%20Analysis.md). The body below has not been revised to match the new part count.

## Purpose of this document

This document converts the supplied source material into a rigorous research programme for small-business owners, micro, small and medium enterprises (MSMEs), investors and analysts. It is an editorial and research plan, not a finished article. The source document is preserved separately as `Warren Buffett - Source Document.md`.

The supplied document contains four explicit prompts, but those prompts combine several distinct accounting, operating, financing and valuation problems. Treating each prompt as one article would force important definitions and limitations into brief side notes. The recommended structure is:

- **Eleven progressive parts**
- **Approximately 3,500 words per part**
- **Forty-four core research questions**, four per part
- **Approximately 38,500 words for the full series**, excluding appendices, references, captions and workbook notes

The progression moves from definition, through estimation and small-business use, into listed-company reconstruction and valuation. It then develops separate treatments for software, banks, insurers, energy, utilities, agriculture, manufacturing, telecommunications, property and other large-company settings before ending with an NSE cross-sector casebook.

## Source-document audit

The source was converted from the supplied Word document with Pandoc and then reviewed line by line. The resulting Markdown contains 819 lines, 469 nonblank lines and approximately 4,243 words. Its 23 embedded media files were extracted into `assets/media/`. All 14 hyperlink occurrences embedded in the Word package were retained exactly in the Markdown, representing five unique URLs.

The substantive material occupies four main blocks:

1. Definition, formula and the Scott Fetzer context.
2. Uses for small-business and MSME owners.
3. Use in public-company stock valuation.
4. Adjustments for software and other asset-light businesses.

Several other passages are search-interface text, privacy notices, sharing controls and source-card extracts. Those passages remain in the faithful source conversion. They are evidence about how the source was assembled, but they should not appear in the publishable articles.

Some visible source cards name Wikipedia, Old School Value, Yahoo Finance, YouTube, Seeking Alpha, LinkedIn, Finrepo and stockterminal. The supplied Word file does not embed destination hyperlinks for those cards. Their names and snippets are retained as source leads, but missing URLs have not been invented.

## Governing definition and necessary corrections

The series should begin with Buffett's original 1986 formulation:

\[
\text{Owner earnings}
= \text{Reported earnings}
+ \text{Depreciation, depletion and amortisation}
+ \text{Other non-cash charges}
- \text{Average annual capital expenditure required to maintain competitive position and unit volume}
- \text{Additional working capital required for that purpose}
\]

The working-capital term is a deduction when additional operating capital is required. It should not be presented as an unrestricted plus-or-minus plug. A release of genuinely surplus working capital can increase cash available in a particular period, but it should be separated from sustainable earning power.

The final articles must correct or qualify the following issues in the source:

1. **Maintenance capital expenditure is an estimate.** Buffett explicitly describes it as a figure that must be guessed and may be difficult to estimate. The articles should use methods, ranges and confidence levels rather than a single supposedly precise number.
2. **Depreciation is not economically harmless.** It is a non-cash charge in the current period, but productive assets eventually require repair or replacement. Adding it back without estimating maintenance expenditure overstates distributable cash.
3. **Owner earnings is not Seller's Discretionary Earnings.** SDE may add back one owner's compensation and certain discretionary expenses for small-business transactions. Owner earnings asks a different question about sustainable cash after necessary reinvestment.
4. **Owner earnings is not automatically safe to withdraw.** Tax, debt service, liquidity reserves, seasonality, legal restrictions, working-capital needs and attractive growth investment can all reduce cash available for distribution.
5. **Private-company multiples require evidence.** The source's generic 2.5 to 4 times range must not be generalized across industries, sizes, growth rates, customer concentrations and owner dependence.
6. **Free cash flow labels vary.** The series must distinguish cash flow from operations less capital expenditure, free cash flow to the firm and free cash flow to equity.
7. **The claim being valued must match the discount rate.** A net-income-based owner-earnings stream is normally closer to equity cash flow. Calling its discounted value an enterprise value without a debt and cash bridge is a category error.
8. **Valuation is a range, not a precise point.** The phrases “precise intrinsic value”, “accurate pricing” and “ultimate input” should be replaced with scenario ranges, sensitivity analysis and explicit uncertainty.
9. **Stock-based compensation needs careful treatment.** GAAP net income already includes the expense. Analysts should reverse the cash-flow-statement add-back, model dilution, or both as appropriate. Subtracting the same expense again from net income can double count it.
10. **Software and research expenditure depend on the reporting regime and activity.** US GAAP and IFRS differ, and software developed for sale is treated differently from internal-use software.
11. **Deferred revenue is useful financing but also a performance obligation.** Upfront cash is not permanently free if the business must still deliver service and support.
12. **Hypothetical examples must remain labelled hypothetical.** Company XYZ and TechX cannot be presented as actual ticker studies.
13. **Some industries require different primary measures.** Banks, insurers, real-estate investment trusts, regulated utilities, commodity producers and lease-intensive businesses need sector-specific treatment.

## Series-wide analytical rules

Every part should:

- distinguish observed facts, accounting classifications, analyst estimates and management assumptions;
- show a reconciliation from reported figures to the selected owner-earnings estimate;
- explain whether the cash flow belongs to the firm or to equity holders;
- state the measurement period and distinguish normalized earning power from one-period cash movements;
- use low, base and high cases where maintenance investment or normalized margins are uncertain;
- identify taxes, financing claims, liquidity requirements and operational constraints before discussing distributions;
- use real companies only when dated filings and notes have been checked, while clearly labelling pedagogical examples;
- render mathematical notation in TeX and keep Excel implementation instructions in the companion workbook;
- use IEEE-style numbered references, with URLs collected in the reference list rather than interrupting prose;
- include a practical table, calculation or decision tool rather than relying on exposition alone.

## Part 1: The Cash an Owner Can Actually Claim

**Purpose:** Establish the concept, preserve Buffett's original reasoning and prevent readers from confusing accounting profit with spendable cash.

### Research questions

1. **What did Buffett mean by owner earnings in the 1986 Berkshire Hathaway letter, and what problem was he solving with the Scott Fetzer example?**
2. **How does reported profit become cash available to an owner once non-cash charges, maintenance investment and working-capital requirements are considered?**
3. **How does owner earnings differ from net income, EBITDA, cash flow from operations, common free cash flow, FCFF, FCFE and Seller's Discretionary Earnings?**
4. **What does “available to owners” mean after tax, debt service, legal restrictions, operating reserves and liquidity risk?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Opening case | Reconstruct why two businesses with similar accounting profits can require very different cash reinvestment. Introduce Scott Fetzer without turning Buffett's illustration into a universal formula. | 300 |
| Original definition | Present the 1986 definition term by term, including Buffett's warning that maintenance capital expenditure must be estimated. | 550 |
| Profit-to-cash bridge | Trace net income through non-cash charges, capital expenditure and incremental working capital. Separate sustainable cash generation from asset sales, borrowing and temporary working-capital releases. | 650 |
| Metric comparison | Compare owner earnings with net income, EBITDA, CFO, simple FCF, FCFF, FCFE and SDE. Explain the question answered by each measure. | 650 |
| Equal-profit example | Build two simplified businesses with equal profit but different asset replacement and inventory needs. Reconcile both in a calculation table. | 650 |
| Availability constraints | Explain taxes, debt covenants, principal repayment, minimum cash, restricted cash, distributions and minority interests. | 450 |
| Reader checklist | Provide a seven-step first-pass test for judging whether reported profit resembles distributable earning power. | 250 |
| **Total** |  | **3,500** |

### Required tables and figures

- A comparison table covering net income, EBITDA, CFO, FCF, FCFF, FCFE, SDE and owner earnings.
- A waterfall from reported earnings to low, base and high owner-earnings estimates.
- A two-business table showing identical profit but different reinvestment burdens.
- A flow diagram separating operations, investment, financing and distributions.

### Key sources to verify

- Berkshire Hathaway's 1986 shareholder letter.
- Current accounting standards and authoritative definitions for cash-flow classifications.
- Transaction-advisory sources for SDE, used only after checking methodology and context.

## Part 2: The Hard Estimate: Maintenance Capital and Working Capital

**Purpose:** Develop the two estimates that determine whether owner earnings is economically meaningful.

### Research questions

5. **How can an owner or investor estimate the capital expenditure required to maintain competitive position and unit volume?**
6. **How should inflation, asset age, capacity expansion, leases, repairs and intangible investment affect that estimate?**
7. **How do inventory, receivables, payables, customer advances and deferred revenue change the working capital required to sustain operations?**
8. **How should analysts normalize maintenance investment and working capital across seasonal, cyclical or unusually volatile periods?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Why the estimate matters | Show why depreciation, total capital expenditure and maintenance capital expenditure rarely coincide. | 300 |
| Competitive-position test | Define the assets and operating capabilities required to preserve unit volume, service quality, safety, compliance and competitive position. | 600 |
| Five estimation methods | Cover asset-register review, replacement-cycle analysis, depreciation anchors, peer and management guidance, and capacity or unit-economics analysis. State the limitations of each. | 750 |
| Inflation and asset age | Explain historical-cost depreciation, replacement-cost inflation, deferred maintenance and the danger of using one recent year. | 550 |
| Working-capital engine | Analyze inventory, receivables, payables, accrued costs, customer deposits and deferred revenue by business model. | 600 |
| Cycle-normalized example | Use a seasonal business to compare a year-end snapshot, monthly average and through-cycle requirement. | 500 |
| Evidence score | Provide a confidence scale for low, base and high maintenance-capex and working-capital estimates. | 200 |
| **Total** |  | **3,500** |

### Required tables and figures

- Maintenance-capex estimation methods, required evidence and failure modes.
- Asset replacement schedule with inflation and useful-life assumptions.
- Working-capital driver table for retail, manufacturing, services, construction and subscription businesses.
- Seasonal monthly working-capital chart.
- Sensitivity table showing owner earnings under low, base and high maintenance assumptions.

## Part 3: Building an Owner-Earnings Statement for a Small Business

**Purpose:** Turn incomplete owner-managed records into an auditable monthly operating view without confusing normalization with cosmetic adjustment.

### Research questions

9. **What minimum records are needed to calculate defensible owner earnings for a small business or MSME?**
10. **How should cash-basis records, accrual accounts, tax returns, bank statements and mobile-money or payment-platform records be reconciled?**
11. **How should owner salary, personal expenses, related-party transactions, one-off items and unpaid owner labour be treated?**
12. **What monthly close, evidence and control process makes the measure useful for recurring decisions rather than a once-a-year estimate?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Minimum viable records | Identify the smallest reliable evidence set and show why bank balance alone is insufficient. | 300 |
| Records and evidence map | Connect sales records, invoices, bank and mobile-money statements, payroll, tax records, loan schedules, asset registers and stock counts. | 650 |
| Cash-to-accrual reconciliation | Explain timing differences, uncollected sales, supplier credit, customer advances and non-operating transfers. | 600 |
| Normalization rules | Separate market-rate owner compensation, personal benefits, related-party terms, one-offs and genuine recurring costs. | 600 |
| Rolling owner-earnings schedule | Build a twelve-month schedule with maintenance investment, working-capital change, tax, debt and liquidity reserve views. | 650 |
| Control and audit trail | Define preparer and reviewer roles, source-document links, change history, close dates and exception review. | 500 |
| Reader checklist | Provide a month-end close checklist and an evidence-quality score. | 200 |
| **Total** |  | **3,500** |

### Required tables and figures

- Minimum-records checklist by business maturity.
- Cash-to-accrual reconciliation example.
- Normalization table distinguishing valid adjustments from unsupported add-backs.
- Twelve-month owner-earnings schedule.
- Monthly close and evidence workflow.

## Part 4: Paying Yourself, Reinvesting and Surviving Growth

**Purpose:** Convert owner earnings into operating decisions while preserving the enterprise's ability to meet obligations and finance sensible growth.

### Research questions

13. **How much of estimated owner earnings can a proprietor or founder safely draw from the business?**
14. **How should an owner distinguish maintenance spending from growth investment, and how should growth opportunities be ranked?**
15. **How can owner earnings inform pricing, hiring, capacity, borrowing and liquidity-reserve decisions?**
16. **Which scenarios and stress tests reveal whether a distribution or expansion plan is sustainable?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| From earnings to distributable cash | Introduce a distribution bridge that deducts tax, contractual payments, reserve replenishment and committed investment. | 350 |
| Owner-pay policy | Separate salary for work, return on ownership, drawings and loan-account movements. Address multiple owners and irregular income. | 650 |
| Reinvestment decision | Compare maintenance, mandatory compliance, capacity expansion and discretionary growth using return on incremental capital and strategic fit. | 650 |
| Operating decisions | Connect pricing, margins, staffing, inventory, equipment and supplier terms to cash earning power. | 550 |
| Financing and resilience | Examine interest coverage, debt amortisation, covenant headroom, minimum cash and emergency reserves. | 650 |
| Scenario analysis | Model revenue decline, margin compression, delayed receipts, inventory build, asset failure and higher interest rates. | 450 |
| Decision checklist | Provide a quarterly capital-allocation and distribution checklist. | 200 |
| **Total** |  | **3,500** |

### Required tables and figures

- Owner-pay bridge from owner earnings to maximum prudent distribution.
- Maintenance, compliance and growth expenditure decision table.
- Debt-service and liquidity stress-test matrix.
- Pricing and hiring break-even calculations.
- Capital-allocation decision tree.

## Part 5: Buying, Selling, Borrowing and Succession

**Purpose:** Show how normalized cash earning power informs transactions and credit without collapsing owner earnings into a generic valuation multiple.

### Research questions

17. **How should owner earnings be reconciled with SDE and EBITDA when a privately held business is being bought or sold?**
18. **Which add-backs are defensible, which require replacement costs, and which merely improve the seller's narrative?**
19. **How should normalized owner earnings be used in income, market and asset-based valuation methods, including the effects of debt and surplus cash?**
20. **How do lenders, successors and prospective buyers adjust for customer concentration, key-person dependence, related parties and weak records?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Transaction context | Explain why sellers, buyers, lenders and successors ask related but different cash-flow questions. | 300 |
| OE, SDE and EBITDA bridge | Reconcile the three measures and show how owner compensation and replacement management change the result. | 700 |
| Add-back discipline | Develop evidence tests for personal expenses, one-offs, related-party rent, family payroll, litigation, grants and unusually low maintenance spending. | 650 |
| Valuation methods | Use owner earnings in discounted cash flow and capitalized-earnings methods, then compare with market and asset approaches. | 600 |
| Debt and purchase-price bridge | Move from enterprise value to equity value and test acquisition debt against cash available for debt service. | 550 |
| Transferability and risk | Address customer concentration, owner dependence, succession, documentation, controls and key-person mitigation. | 500 |
| Due-diligence checklist | Provide evidence requests and red flags for a buyer, lender or successor. | 200 |
| **Total** |  | **3,500** |

### Required tables and figures

- Reconciliation from reported profit to EBITDA, SDE and owner earnings.
- Add-back evidence and replacement-cost table.
- Enterprise-value-to-equity-value bridge.
- Acquisition debt-service scenario table.
- Transferability and key-person risk scorecard.

## Part 6: Reconstructing Owner Earnings for a Listed Company

**Purpose:** Build a repeatable filing-based method before attempting an intrinsic-value calculation.

### Research questions

21. **Which financial statements, notes and management disclosures are required to reconstruct owner earnings for a listed company?**
22. **How should non-cash charges, acquisitions, restructuring, impairments, leases, pensions and recurring “one-off” items be treated?**
23. **How can an outside investor estimate maintenance capital expenditure and intangible reinvestment with incomplete disclosure?**
24. **Which cross-checks reveal weak cash conversion, aggressive adjustments or a deteriorating business model?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Filing map | Identify the annual report, cash-flow statement, fixed-asset note, segment note, share-count data, debt note and management commentary. | 300 |
| Statement reconstruction | Build the reported-earnings bridge and reconcile it to cash flow from operations. | 650 |
| Adjustment taxonomy | Analyze depreciation, amortisation, impairments, deferred tax, restructuring, leases, pensions, acquisitions and disposals. | 650 |
| Maintenance reinvestment | Compare total capital expenditure, depreciation, asset age, capacity, segment growth and management disclosures. Include intangible investment. | 650 |
| Quality checks | Test working-capital reversals, receivables, capitalized costs, recurring adjustments, acquisitions and share dilution. | 550 |
| Dated company case | Apply the method to a real company using a clearly dated filing, with low, base and high estimates and direct source references. | 500 |
| Analyst checklist | Provide a filing-to-model workflow and evidence grading rubric. | 200 |
| **Total** |  | **3,500** |

### Required tables and figures

- Filing and note retrieval checklist.
- Reported-profit-to-owner-earnings reconciliation.
- Adjustment taxonomy showing cash effect, recurrence and ownership claim.
- Maintenance-capex triangulation table.
- Five-year cash-conversion and dilution dashboard.

## Part 7: Turning Owner Earnings into Intrinsic Value

**Purpose:** Connect a defensible cash-flow estimate to the correct claim, forecast, discount rate and valuation range.

### Research questions

25. **When is owner earnings an equity cash flow, when can it be reformulated as firm cash flow, and what valuation claim follows from each?**
26. **How should an analyst forecast revenue, margins, reinvestment and owner earnings without merely extrapolating the latest year?**
27. **How should discount rates, terminal assumptions, debt, surplus cash, options and diluted shares enter the valuation?**
28. **How do sensitivity analysis, reverse discounted cash flow and a margin-of-safety policy prevent false precision?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Define the claim | Separate equity and enterprise cash flows and pair each with an appropriate discount rate. | 300 |
| Forecast architecture | Develop explicit operating drivers, normalized margins, reinvestment needs and competitive fade. | 650 |
| Multi-stage model | Present forecast-period, transition-period and terminal-value logic with TeX equations. | 650 |
| Discount rate and bridge | Cover cost of equity, weighted average cost of capital, net debt, non-operating assets and minority interests without implying mechanical precision. | 650 |
| Per-share value | Treat options, restricted shares, convertible claims, buybacks and future dilution. | 500 |
| Uncertainty tools | Use two-way sensitivities, scenarios, reverse DCF and valuation distributions to define a range and margin of safety. | 550 |
| Review checklist | Provide model-consistency and valuation-claim tests. | 200 |
| **Total** |  | **3,500** |

### Required tables and figures

- FCFE and FCFF claim-and-discount-rate comparison.
- Forecast-driver table with historical, normalized and scenario values.
- Present-value and terminal-value calculation table.
- Enterprise-to-equity and equity-to-per-share bridges.
- Two-way sensitivity matrix and reverse-DCF table.

### Core equations

For an equity owner-earnings stream:

\[
V_0^{E}=\sum_{t=1}^{n}\frac{OE_t^{E}}{(1+k_e)^t}
+\frac{TV_n^{E}}{(1+k_e)^n}
\]

For a firm cash-flow stream:

\[
V_0^{F}=\sum_{t=1}^{n}\frac{OE_t^{F}}{(1+WACC)^t}
+\frac{TV_n^{F}}{(1+WACC)^n}
\]

The article must define how each cash-flow measure is constructed. It must not use the same owner-earnings label for both without a reconciliation.

## Part 8: Owner Earnings for Software and Asset-Light Businesses

**Purpose:** Adapt the framework where physical capital expenditure is low but employee equity, product development, customer acquisition and future service obligations are economically important.

### Research questions

29. **How should stock-based compensation be treated without double counting its expense or ignoring dilution?**
30. **How do options, restricted stock units, repurchases and changing share counts affect owner earnings per share and intrinsic value?**
31. **When should software development and research expenditure be treated as current operating cost, capitalized investment or an analyst-created intangible asset under US GAAP and IFRS?**
32. **How should deferred revenue, contract liabilities, fulfilment costs, churn, customer acquisition and recurring service obligations affect sustainable owner earnings?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Why “asset-light” can mislead | Show how low physical capital expenditure can coexist with heavy economic reinvestment in people, code, data and distribution. | 300 |
| Stock-based compensation | Trace the expense through net income and CFO, distinguish non-cash settlement from economic cost, and compare reversal, dilution and repurchase-offset methods. | 750 |
| Share-count mechanics | Model options, restricted shares, buybacks, issuance and per-share dilution over time. | 500 |
| Software and R&D | Compare US GAAP and IFRS at a high level and distinguish research, software for sale, internal-use software and implementation costs. | 650 |
| Subscription working capital | Analyze deferred revenue, billing terms, contract liabilities and the cost of fulfilling prepaid service. | 550 |
| Unit economics and case | Integrate churn, retention, customer acquisition, support and product development into a low, base and high owner-earnings case. | 550 |
| Adjustment checklist | Provide a software-company evidence and double-counting checklist. | 200 |
| **Total** |  | **3,500** |

### Required tables and figures

- Stock-based compensation treatment map from income statement to cash flow and diluted shares.
- Share-count and repurchase-offset schedule.
- US GAAP and IFRS software and research treatment comparison.
- Deferred-revenue cash-benefit and fulfilment-obligation table.
- Subscription unit-economics and owner-earnings bridge.

## Part 9: Banks and Insurers: Capital, Risk and Distributable Value

**Purpose:** Replace the industrial-company cash-flow formula with capital, risk and claims-based methods suited to financial institutions, with particular attention to NSE-listed banks and insurers.

### Research questions

33. **Why does a conventional owner-earnings calculation break down for a bank, and how can distributable capital be estimated after expected credit losses, growth and regulatory requirements?**
34. **How should asset quality, funding structure, net interest margin, fee income, provisioning, capital adequacy and the credit cycle be normalized for bank valuation?**
35. **How should an insurer's underwriting result, claims reserves, investment income, solvency capital and float be translated into sustainable earning power?**
36. **When should investors use dividend discount, residual income, price-to-book, embedded-value or excess-capital methods for financial institutions, and how should the results be reconciled?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Why the industrial formula fails | Explain why deposits, lending, investment assets and regulatory capital are operating items rather than ordinary financing or working capital. | 300 |
| Bank earning-power engine | Analyze net interest income, fee income, operating efficiency, funding cost, loan growth and capital intensity. | 600 |
| Credit cycle and asset quality | Normalize provisions and losses using non-performing loans, coverage, restructures, write-offs, collateral and stage migration. | 600 |
| Insurance earning-power engine | Separate underwriting, claims development, expenses, reinsurance, investment income, float and reserve uncertainty. | 600 |
| Distributable capital | Estimate capital generated after growth, risk-weighted assets, solvency requirements, buffers and plausible stress losses. | 500 |
| Valuation methods | Compare residual income, justified price-to-book, dividend discount, excess-capital and embedded-value approaches. | 650 |
| NSE evidence checklist | Specify Central Bank, insurance-regulator, audited-report and issuer data needed for dated Kenyan cases. | 250 |
| **Total** |  | **3,500** |

### Required tables and figures

- Industrial owner-earnings formula versus bank and insurer valuation logic.
- Bank income, credit-quality and regulatory-capital bridge.
- Loan-book growth and capital-consumption scenario table.
- Insurance underwriting, reserve and solvency bridge.
- Residual-income, dividend-discount and price-to-book comparison.
- Low, base and stress cases for distributable capital.

## Part 10: Asset-Heavy, Regulated and Cyclical NSE Corporations

**Purpose:** Develop sector-specific owner-oriented cash models for large companies whose economics depend on physical networks, commodity cycles, biological assets, regulation, leases or property values.

### Research questions

37. **How should maintenance investment, regulated returns, fuel or power costs, demand risk and debt be modeled for energy and utility companies?**
38. **How should biological assets, harvest cycles, weather, commodity prices, foreign exchange and land value be treated in agriculture and plantation businesses?**
39. **How do manufacturing, consumer, telecommunications, infrastructure, property and REIT businesses require different definitions of maintenance investment and sustainable cash flow?**
40. **How should investors normalize cycles, inflation, currency changes, regulatory decisions and large replacement programmes before assigning value?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Sector boundary | Explain why one owner-earnings formula cannot be applied mechanically across large NSE corporations. | 250 |
| Energy and utilities | Analyze regulated or contracted revenue, demand, tariffs, generation mix, fuel costs, network losses, mandatory investment, debt and concession obligations. | 550 |
| Agriculture and commodities | Model biological transformation, crop cycles, bearer assets, weather, commodity prices, export currency, land and working capital. | 500 |
| Manufacturing and consumer businesses | Separate replacement, compliance, efficiency and growth capital while normalizing capacity use, input prices and distribution investment. | 500 |
| Telecommunications and infrastructure | Treat spectrum, network renewal, leases, mobile-money economics, customer acquisition, platform investment and regulatory charges. | 500 |
| Property companies and REITs | Reconcile accounting profit, fair-value changes, funds from operations, adjusted funds from operations, development spending, debt and net asset value. | 450 |
| Through-cycle valuation | Build low, base and high cases for inflation, exchange rates, volumes, tariffs, commodity prices and capital expenditure. | 500 |
| Sector checklist | Provide source, adjustment, valuation-method and warning tests. | 250 |
| **Total** |  | **3,500** |

### Required tables and figures

- Sector-specific maintenance-investment matrix.
- Energy and utility regulatory cash-flow bridge.
- Agriculture crop-cycle and commodity-price sensitivity table.
- Manufacturing capacity and replacement-capex schedule.
- Telecommunications network, spectrum and platform-investment bridge.
- REIT funds-from-operations, adjusted-funds-from-operations and net-asset-value reconciliation.

## Part 11: NSE Cross-Sector Casebook and Final Decision Framework

**Purpose:** Apply the full framework to actual, dated NSE-listed companies and show how to compare investment quality without pretending that unlike sector metrics are identical.

### Research questions

41. **How can investors compare cash earning quality across NSE sectors while respecting different accounting, capital and regulatory structures?**
42. **Which filings, notes, regulatory disclosures and market data are required to build reproducible Kenyan listed-company cases?**
43. **How should each sector's primary valuation method be reconciled with an owner-oriented view of distributable value?**
44. **How should valuation range, leverage, governance, liquidity, concentration, inflation, currency and macroeconomic risk be combined into a final investment decision?**

### Detailed outline and word budget

| Section | Treatment | Approximate words |
|---|---|---:|
| Comparative framework | Define comparable outputs, including return on capital, distributable value, reinvestment burden, balance-sheet resilience and valuation range. | 300 |
| Retrieval and reproducibility | Document NSE, CMA, regulator, issuer and audited-report retrieval, dates, units, restatements and source tracing. | 500 |
| Bank or financial-institution case | Apply the Part 9 capital and residual-income framework to a verified NSE-listed issuer. | 350 |
| Insurance case | Apply underwriting, reserve, investment and solvency analysis to a verified NSE-listed insurer. | 350 |
| Telecommunications or platform case | Apply network, spectrum, mobile-money, platform and dilution adjustments to a verified issuer. | 350 |
| Energy or utility case | Apply tariff, network, maintenance-capex, debt and regulatory scenarios to a verified issuer. | 350 |
| Agriculture or commodity case | Apply crop-cycle, biological-asset, weather, currency and commodity normalization to a verified issuer. | 350 |
| Manufacturing, consumer, property or REIT case | Apply the appropriate replacement-capex, cash-conversion, funds-from-operations or net-asset-value method. | 350 |
| Cross-sector comparison | Compare the cases using ranges and sector-appropriate measures rather than a single mechanical multiple. | 400 |
| Final decision checklist | Combine evidence quality, valuation, balance-sheet risk, governance, market liquidity and portfolio exposure. | 200 |
| **Total** |  | **3,500** |

### Required tables and figures

- NSE company source and reporting-period register.
- Sector-to-primary-valuation-method matrix.
- Six-company reconciliation summary using actual dated disclosures.
- Cross-sector quality, reinvestment and balance-sheet dashboard.
- Valuation-range and reverse-assumption comparison.
- Governance, liquidity and concentration risk scorecard.

Actual company names should be selected only after confirming current NSE listing status and obtaining the relevant audited filings. Each case must state its valuation date, price observation date, reporting currency, units, filing period and data-retrieval date.

## How the eleven parts answer the four source prompts

| Source prompt | Parts that answer it | Reason for the expansion |
|---|---|---|
| What is owner earnings? | Parts 1 and 2 | The definition cannot be separated from the estimates of maintenance investment and working capital. |
| How can small-business and MSME owners use it? | Parts 3, 4 and 5 | Record construction, recurring operating decisions and transactions require different evidence and decision rules. |
| How is it used in stock valuation? | Parts 6, 7, 9, 10 and 11 | Reconstructing cash flow from filings must precede valuation, and the method must then be adapted to the economics of each sector. |
| How should it be applied to software and asset-light companies? | Part 8 | Software, platforms and other asset-light businesses require treatment of stock compensation, dilution, intangible reinvestment and customer obligations. |
| Where does the standard formula need modification? | Parts 9 and 10 | Financial institutions and asset-heavy, regulated or cyclical corporations require different definitions of distributable value. |
| How does the framework apply to the Nairobi Securities Exchange? | Part 11 | Actual dated cases connect the general framework to Kenyan issuers while preserving sector-specific methods. |

## Companion workbook architecture

The workbook should deepen the reasoning without making the article depend on spreadsheet syntax. Each calculation sheet should contain inputs, formula logic, checks, outputs and source notes.

| Sheet | Main purpose | Principal outputs |
|---|---|---|
| Guide and Sources | Definitions, conventions, provenance and versioning | Source register, colour legend and model scope |
| P1 Profit-to-Cash | Reconcile accounting profit to owner earnings | Low, base and high owner earnings |
| P2 Maintenance Capex | Apply several estimation methods | Replacement schedule and sensitivity range |
| P2 Working Capital | Model operational cash tied up in the cycle | Monthly and normalized working-capital need |
| P3 MSME Monthly Model | Combine records into a rolling view | Twelve-month owner-earnings statement |
| P3 Normalizations | Record proposed adjustments and evidence | Accepted, rejected and pending adjustments |
| P4 Distribution and Reserve | Test owner pay and liquidity | Prudent distribution range and reserve runway |
| P4 Growth and Debt | Compare projects and financing scenarios | Incremental returns, coverage and covenant headroom |
| P5 Transaction Bridge | Reconcile EBITDA, SDE and owner earnings | Buyer, seller and lender views |
| P5 Valuation and Debt | Test purchase price and financing | Equity value and acquisition debt service |
| P6 Listed Company | Reconstruct figures from filings | Multi-year owner-earnings history |
| P7 DCF and Reverse DCF | Value the correct cash-flow claim | Scenario values, implied growth and margin of safety |
| P8 Software Adjustments | Model SBC, dilution, R&D and deferred revenue | Adjusted per-share cash earning power |
| P9 Bank Model | Model earning power, credit costs, capital growth and distributions | Normalized profit, excess capital and residual value |
| P9 Insurance Model | Model underwriting, reserves, investments and solvency | Sustainable insurance earnings and distributable capital |
| P10 Energy and Utility | Model tariffs, volumes, network losses, capital expenditure and debt | Regulated or contracted cash-flow range |
| P10 Agriculture and Cycles | Model crop volumes, prices, currency, biological assets and weather | Through-cycle earning-power range |
| P10 Industrial and Telecom | Model capacity, replacement investment, networks, spectrum and leases | Sector-adjusted owner earnings |
| P10 Property and REIT | Reconcile profit, fair-value movements, FFO, AFFO and NAV | Property cash flow and asset-value range |
| P11 NSE Casebook | Compare actual dated company cases using sector-appropriate methods | Cross-sector dashboard and valuation ranges |

## Interactive workbook requirements

The workbook is a core project deliverable. It should let a reader replace the worked examples with their own business or company information and immediately see the effect on owner earnings, liquidity, valuation and decision thresholds. The worked cases should remain available as defaults and as checks against accidental formula damage.

### User interaction model

Every analytical sheet should distinguish four cell types visually and consistently:

| Cell type | Purpose | Expected behaviour |
|---|---|---|
| User input | Values the reader may change, such as revenue, margins, asset lives, capital expenditure, working-capital days, debt and discount rates | Unlocked, validated and clearly labelled with units |
| Sourced input | Historical figures taken from records or filings | Includes source, date, reporting period and status |
| Calculated cell | Live formulas derived from inputs | Locked or protected against accidental editing |
| Review output | Results, warnings, ratios and decision flags | Updates automatically and links back to the relevant assumptions |

The workbook should support:

- a clean reset to the supplied worked example;
- editable low, base and high scenarios;
- switches between monthly, quarterly and annual views where appropriate;
- selection of currency and display units without changing the economic calculation;
- input validation for percentages, dates, useful lives, probabilities and non-negative quantities;
- warnings for missing inputs, inconsistent signs, weights that do not sum correctly and assumptions outside a reasonable range;
- named ranges or structured tables so added rows flow through formulas and charts;
- whole-workbook navigation from the Guide sheet;
- short practical notes beside each important input explaining when it is used and what evidence supports it;
- results that update without macros wherever ordinary spreadsheet formulas are sufficient.

### Scenario and sensitivity capabilities

Users should be able to change at least the following assumptions:

| Area | Editable assumptions | Interactive outputs |
|---|---|---|
| Operating performance | Revenue growth, volume, price, gross margin and operating costs | Profit, cash conversion and owner earnings |
| Maintenance investment | Asset life, replacement cost, inflation, repair profile and maintenance share of total capital expenditure | Low, base and high maintenance-capex estimates |
| Working capital | Receivable, inventory and payable days, customer advances, deferred revenue and seasonality | Cash tied up in operations and funding requirement |
| Owner distributions | Salary, tax, minimum cash, reserve months and planned drawings | Prudent distribution range and liquidity runway |
| Growth investment | Project cost, incremental revenue, margin, timing and probability | Return on incremental capital, payback and funding gap |
| Debt | Principal, interest rate, tenor, amortisation and covenants | Debt service, coverage, covenant headroom and stress results |
| Private-business valuation | Normalizations, sustainable owner earnings, capitalization rate or multiple, debt and surplus cash | Enterprise value, equity value and buyer-return scenarios |
| Listed-company valuation | Forecast period, growth, margins, reinvestment, discount rate, terminal assumptions and dilution | Equity or enterprise value, per-share range and reverse-DCF result |
| Software adjustments | Stock compensation, option dilution, repurchases, R&D capitalization assumptions, churn and deferred revenue | Adjusted owner earnings and per-share earning power |
| Banks | Loan growth, margins, credit costs, funding, capital ratios and payout | Distributable capital, residual income and justified book-value range |
| Insurers | Premium growth, loss ratios, expenses, reserves, investment returns and solvency | Sustainable underwriting result and distributable capital |
| Energy and utilities | Tariffs, demand, fuel costs, network losses, maintenance investment and debt | Regulated or contracted cash-flow and stress range |
| Agriculture and commodities | Yield, crop cycle, selling price, weather, exchange rate and replacement investment | Through-cycle earnings and commodity sensitivities |
| Manufacturing and consumer | Capacity use, input cost, pricing, working capital and replacement cycle | Normalized owner earnings and incremental returns |
| Telecommunications and infrastructure | Network investment, spectrum, leases, subscriber economics and platform assumptions | Adjusted cash earning power and capital intensity |
| Property and REITs | Occupancy, rent, maintenance, development spending, debt and capitalization rates | FFO, AFFO, NAV and distribution capacity |
| NSE casebook | Valuation date, reporting period, price, sector method, governance and liquidity | Comparable evidence dashboard and decision range |

Sensitivity tables should be genuine formula-driven model outputs. They should not contain pasted values that cease to respond when the user changes a core assumption.

### Workbook controls and auditability

The finished workbook should include:

1. A `Guide` sheet explaining scope, conventions, colours, units and how to use each part.
2. A `Sources` sheet recording every external figure, document, URL, reporting period, retrieval date and transformation.
3. An `Assumptions` register showing the current value, scenario, owner, rationale and last review date.
4. Visible reconciliation checks, including balance checks, cash-flow bridges, sign checks and valuation-claim checks.
5. A change log for released versions and material model revisions.
6. Formula protection that prevents accidental overwriting while leaving intended input cells editable.
7. No hidden hard-coded outputs, unexplained plug figures or external links required for the workbook to calculate.
8. Error handling that replaces misleading spreadsheet errors with a clear explanation of the missing or invalid input.
9. Print-ready summary pages for an owner, investor, lender or transaction reviewer.
10. A verification sheet containing benchmark cases and expected results for the most important calculations.

### Article and workbook relationship

Each article should contain a compact calculation table using the same terminology and example values as its workbook sheet. The article explains the financial logic and practical interpretation. The workbook provides the editable model, expanded scenarios and detailed calculations. Excel-specific formulas and operating instructions belong in the workbook documentation rather than the article text.

Each part should point to the relevant workbook sheet and state:

- which inputs the user can change;
- which results should be interpreted together;
- which warnings mean the estimate is unreliable;
- which evidence should be gathered before replacing a worked assumption;
- where the model is unsuitable without a sector-specific adjustment.

### Quality gate before publication

The workbook should not be released until:

- every input changes the intended downstream formulas and charts;
- all eleven parts reconcile to their article examples;
- low, base and high scenarios remain internally consistent;
- formulas have been recalculated with no spreadsheet errors;
- important outputs have been independently recomputed or cross-checked;
- the workbook opens without broken links or missing external data connections;
- tables, charts, notes and print areas render clearly at normal zoom and in exported PDF form;
- a user unfamiliar with the model can complete the Guide workflow without editing a protected formula cell.

## Standard structure for every published part

Each article should follow the same reader-facing pattern:

1. A practical question or decision faced by an owner or investor.
2. Definitions and the accounting or economic issue.
3. A step-by-step numerical example.
4. A table summarizing assumptions, evidence and interpretation.
5. A real, dated application where reliable primary evidence is available.
6. Limitations, alternative interpretations and sensitivity analysis.
7. A practical checklist.
8. IEEE-style references collected at the end.

The opening should be conversational but rigorous. It should not discuss defects in unseen source material. Corrections should appear as clear explanations of the concept itself.

## Evidence hierarchy and retrieval standard

Research should be retrieved and recorded in this order:

1. Original shareholder letters, audited financial statements, regulatory filings and accounting-standard materials.
2. Tax authority, central-bank, securities-regulator and official small-business guidance.
3. Company investor-relations materials, with management claims checked against filings.
4. Peer-reviewed research and established professional literature.
5. High-quality practitioner material used for implementation examples, with limitations disclosed.
6. Search-result snippets, social posts and unsourced summaries used only as leads, never as final authority.

For every real-company table, record the company, reporting period, filing date, currency, units, exact statement or note, retrieval date and any transformation. For every analyst estimate, record the method, assumptions, range and confidence level.

## Initial authoritative source map

[1] W. E. Buffett, “Berkshire Hathaway Inc. 1986 Chairman's Letter,” Berkshire Hathaway, 1987. [Online]. Available: https://www.berkshirehathaway.com/letters/1986.html

[2] U.S. Securities and Exchange Commission, “Staff Accounting Bulletin No. 107: Share-Based Payment,” Mar. 29, 2005. [Online]. Available: https://www.sec.gov/rules-regulations/staff-guidance/staff-accounting-bulletins/staff-accounting-bulletin-no-107

[3] Financial Accounting Standards Board, “Summary of Statement No. 2: Accounting for Research and Development Costs.” [Online]. Available: https://fasb.org/page/PageContent?bcpath+=+tff&pageId=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-statement-no-2.html

[4] U.S. Small Business Administration, “Manage your business.” [Online]. Available: https://www.sba.gov/counseling/manage-your-business/

[5] Capital Markets Authority of Kenya, “CMA Resource Center: Listed Companies.” [Online]. Available: https://annualreport.cma.or.ke/

[6] Central Bank of Kenya, “Bank Supervision and Banking Sector Reports.” [Online]. Available: https://www.centralbank.go.ke/reports/bank-supervision-and-banking-sector-reports/

[7] Insurance Regulatory Authority of Kenya, “Insurance Regulatory Authority.” [Online]. Available: https://ira.go.ke/

[8] Energy and Petroleum Regulatory Authority, “EPRA Statistics Reports.” [Online]. Available: https://www.epra.go.ke/statistics-0

[9] Kenya National Bureau of Statistics, “2026 Economic Survey.” [Online]. Available: https://www.knbs.or.ke/reports/2026-economic-survey/

These are starting authorities, not a complete bibliography. Each part needs its own dated source retrieval and verification before drafting.

## Deliverable decision

The expanded project supports **eleven articles of approximately 3,500 words each, organized around 44 core research questions**. This structure preserves the small-business and general valuation material while giving financial institutions, asset-heavy and cyclical sectors, and actual NSE applications enough room for separate methods. It also corrects the accounting, claim-definition, stock-compensation and false-precision problems in the source. Compressing the work into four articles, or placing every non-software sector in one closing article, would make the small-business controls, maintenance-capex estimation, banking and insurance capital analysis, listed-company reconstruction and NSE sector applications too shallow to be practically useful.
