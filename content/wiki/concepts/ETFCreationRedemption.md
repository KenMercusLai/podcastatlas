---
title: "ETF Creation-Redemption / ETF 申赎机制"
type: concept
tags: [investing, etf, market-structure, liquidity]
sources: [vol-266-yi-ci-xing-gao-dong-etf-1002344828]
last_updated: 2026-08-07
---

# ETF Creation-Redemption / ETF 申赎机制

ETF creation-redemption is the backstage mechanism emphasized in [[vol-266-yi-ci-xing-gao-dong-etf-1002344828]]. The source explains that ordinary investors usually buy and sell ETF shares for cash on an exchange, while market makers or authorized participants can exchange a basket of underlying securities for newly created ETF shares, or redeem ETF shares for the underlying basket.

This mechanism helps connect the ETF's exchange price to its net asset value. If the ETF trades too high or too low relative to the basket, arbitrage capital can create or redeem shares and trade the difference, which supports liquidity and makes [[ExchangeTradedFund|ETF]] pricing different from a closed secondary-market claim.

## Key Claims
- Creation-redemption is the core institutional mechanism behind ETF share supply, not just a settlement detail.
- In-kind exchange can make ETFs attractive to institutions that already hold the underlying securities.
- The same mechanism that supports broad index ETFs can also sit underneath more complex products, though leverage and derivatives add other risks.
- Retail investors may never interact with creation-redemption directly, but their trading experience depends on the mechanism working smoothly behind the screen.

## Connections
- [[ExchangeTradedFund]] - product wrapper using the mechanism.
- [[ETFInKindTaxDeferral]] - tax and deferral branch tied to in-kind exchange.
- [[SPY]], [[VOO]], [[StateStreet]], and [[Vanguard]] - scale and origin examples from the source.
- [[HongKongMarketStructure]] and [[CrossMarketLeveragedETFExecutionRisk]] - cases where market structure changes how ETF liquidity feels in practice.
