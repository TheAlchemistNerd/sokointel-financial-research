# Appendix A Mathematical Formulae

This appendix documents the calculations used in the core portfolio and three-month DCA model. Symbols describe the calculation; the workbook carries the editable Excel expressions.

## A.1 Investable securities value

**Formula:** S = C / (1 + c)

**Mathematical equivalence:** total cash C is divided by one plus the transaction-cost rate c. S is the cash available for securities after reserving costs.

**Excel expression:** =TotalCash/(1+TransactionCostRate)

## A.2 Transaction-cost provision

**Formula:** F = C - S

**Mathematical equivalence:** the provision F is the difference between total cash C and investable securities value S.

**Excel expression:** =TotalCash-InvestableSecurities

## A.3 Monthly securities budget

**Formula:** M = S / n

**Mathematical equivalence:** the securities budget M for each purchase month equals investable securities value S divided by the number of deployment months n.

**Excel expression:** =InvestableSecurities/DeploymentMonths

## A.4 Security allocation

**Formula:** A_i = S x w_i

**Mathematical equivalence:** allocation A for counter i equals investable securities value S multiplied by the target portfolio weight w for that counter.

**Excel expression:** =InvestableSecurities*TargetWeight

## A.5 Whole-share quantity

**Formula:** q_i = floor(M x w_i / P_i)

**Mathematical equivalence:** whole shares q for counter i are the integer part of the monthly allocation M times target weight w, divided by live share price P. The floor operation prevents an order from exceeding its allocation before charges.

**Excel expression:** =ROUNDDOWN(MonthlyTarget/ReferencePrice,0)

## A.6 Indicative dividend yield

**Formula:** y_i = D_i / P_i

**Mathematical equivalence:** indicative yield y for counter i equals the stated dividend per share D divided by reference price P.

**Excel expression:** =DividendPerShare/ReferencePrice

## A.7 Gross annual dividend income

**Formula:** G_i = A_i x y_i

**Mathematical equivalence:** gross annual dividend income G for counter i equals capital allocated A multiplied by indicative yield y. Portfolio gross income is the sum of all counter-level gross income values.

**Excel expression:** =TargetCapital*IndicativeYield

## A.8 Resident withholding tax and net income

**Formula:** T = G x t; N = G - T

**Mathematical equivalence:** withholding tax T equals gross dividend income G multiplied by withholding-tax rate t. Net dividend income N equals gross income less tax.

**Excel expression:** =GrossIncome*WithholdingTaxRate and =GrossIncome-WithholdingTax

## A.9 Dividend scenario testing

**Formula:** G_s = G x (1 + s); N_s = G_s x (1 - t)

**Mathematical equivalence:** scenario gross income G_s applies a dividend-change assumption s to base gross income G. Scenario net income N_s applies the withholding-tax rate t after the change.

**Excel expression:** =BaseGrossIncome*(1+ScenarioChange) and =ScenarioGrossIncome*(1-WithholdingTaxRate)

## A.10 Net yield on total cash

**Formula:** y_net = N / C

**Mathematical equivalence:** net cash yield equals net annual dividend income N divided by the original total cash C, including the cost provision.

**Excel expression:** =NetDividendIncome/TotalCash
