---
title: "Futures Roll Cost / 期货展期损耗"
type: concept
tags: [investing, futures, etf, leverage]
sources: [vol-121-cong-tanhua-yixian-de-fenji-jijin-dao-fengtou-zhengjing-de-ganggan-etf-yongyuan-buyao-digu-renxing-de-fengkuang-lusagcitdozvzm8wausvecvi-qmb]
last_updated: 2026-08-06
---

# Futures Roll Cost / 期货展期损耗

Futures roll cost is the implementation drag highlighted in [[vol-121-cong-tanhua-yixian-de-fenji-jijin-dao-fengtou-zhengjing-de-ganggan-etf-yongyuan-buyao-digu-renxing-de-fengkuang-lusagcitdozvzm8wausvecvi-qmb]] for leveraged ETFs that use futures to maintain exposure. When expiring contracts have to be replaced with later contracts, the fund may lose money through the roll process depending on the futures curve and financing environment.

The source uses [[TMF]] to show why product implementation matters even when the macro thesis is plausible. Long-duration Treasury exposure through a three-times daily leveraged futures-based ETF can be eroded by roll cost as well as [[VolatilityDecay|volatility decay]] and fees.

## Key Claims
- Futures-based ETFs must continually maintain exposure as contracts expire.
- Roll cost can make the product underperform a naive expectation based only on the spot or index move.
- Bond leveraged ETFs can combine duration risk, daily reset, volatility drag, and futures implementation cost.
- Investors need to evaluate product mechanics separately from their directional macro view.

## Connections
- [[TMF]] - product case emphasized by the source.
- [[LeveragedETF]], [[DailyLeverageReset]], and [[VolatilityDecay]] - adjacent ETF mechanics.
- [[TreasuryDurationRisk]] - underlying macro exposure related to long bonds.
- [[LeveragedProductSuitability]] and [[PortfolioSuitability]] - suitability frame for long holding periods.
