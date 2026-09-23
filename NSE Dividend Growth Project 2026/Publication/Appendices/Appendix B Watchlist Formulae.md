# Appendix B Watchlist Formulae

The watchlist uses one common price date and stated dividend basis so that indicative yields can be compared on the same arithmetic basis.

## B.1 Indicative dividend yield

**Formula:** y_i = D_i / P_i

**Mathematical equivalence:** indicative yield y for counter i equals the stated dividend per share D divided by reference price P.

**Excel expression:** =DividendPerShare/ReferencePrice

## B.2 Ordinary dividend normalization

**Formula:** D_ordinary = D_total - D_special

**Mathematical equivalence:** ordinary dividend D_ordinary removes a separately identified special dividend D_special from the total stated dividend D_total. The resulting ordinary yield is D_ordinary divided by price P.

**Excel expression:** =TotalDividend-SpecialDividend and =OrdinaryDividend/ReferencePrice

## B.3 Portfolio weight after a new purchase

**Formula:** w_prime_i = (V_i + B_i) / (V_total + B_total)

**Mathematical equivalence:** revised portfolio weight for holding i equals its existing value V plus new purchase B, divided by existing portfolio value plus the total new capital deployed.

**Excel expression:** =(ExistingHoldingValue+NewPurchase)/(ExistingPortfolioValue+TotalNewCapital)
