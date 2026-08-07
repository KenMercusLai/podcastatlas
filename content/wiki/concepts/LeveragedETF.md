---
title: "Leveraged ETF / 杠杆 ETF"
type: concept
tags: [investing, etf, leverage, derivatives]
sources: [vol-266-yi-ci-xing-gao-dong-etf-1002344828, vol-124-xinxi-guozai-hou-ruhe-baochi-lengjing-touzi-zhang-fupan-ltpmll0jmcw-dl0-32qesddwem4l, vol-121-cong-tanhua-yixian-de-fenji-jijin-dao-fengtou-zhengjing-de-ganggan-etf-yongyuan-buyao-digu-renxing-de-fengkuang-lusagcitdozvzm8wausvecvi-qmb]
last_updated: 2026-08-07
---

# Leveraged ETF / 杠杆 ETF

Leveraged ETF enters the wiki through [[vol-121-cong-tanhua-yixian-de-fenji-jijin-dao-fengtou-zhengjing-de-ganggan-etf-yongyuan-buyao-digu-renxing-de-fengkuang-lusagcitdozvzm8wausvecvi-qmb]] as the overseas counterpart to Chinese [[ChineseStructuredFund|structured funds]]. The source describes leveraged ETFs as products that usually use derivatives such as futures or swaps to target a multiple of an index's daily return.

The episode's central distinction is between the ETF wrapper and the product's actual risk engine. A leveraged ETF can be transparent and exchange-traded, but [[DailyLeverageReset|daily reset]], [[VolatilityDecay|volatility decay]], management fees, trading cost, swap cost, and [[FuturesRollCost|roll cost]] can make long holding periods very different from a simple multiple of the underlying asset.

[[vol-124-xinxi-guozai-hou-ruhe-baochi-lengjing-touzi-zhang-fupan-ltpmll0jmcw-dl0-32qesddwem4l]] adds an April 2025 stress example. The source revisits [[TQQQ]] and [[NVDL]] after violent market moves and says their realized drawdowns showed why daily multiple products can lose more than a simple underlying-move calculation suggests when volatility and path dependency are high.

[[vol-266-yi-ci-xing-gao-dong-etf-1002344828]] adds the swap-hedging and cross-market version through [[ETF7709HK|7709.HK]]. The source argues that a leveraged ETF can change the underlying market's behavior when banks hedge swap exposure by buying or selling the underlying stock, especially when trading hours and derivatives depth do not line up across markets.

## Key Claims
- Leveraged ETFs usually target daily performance multiples, not multi-month or multi-year cumulative multiples.
- Derivative-based leverage differs from Chinese structured funds, where A shares effectively financed B shares.
- Daily reset can keep leverage from mechanically rising as NAV falls, but it introduces path dependence.
- The product category may fit short tactical trading better than ordinary long-term asset allocation.
- Bond and commodity versions may add futures roll costs beyond daily reset and volatility effects.
- Vol.124 adds that even a directionally correct technology or Nvidia view can be damaged by the holding path if the product is a daily leveraged ETF.
- Vol.266 adds that large swap-based single-stock products can create [[LeveragedETFHedgingFeedback|hedging feedback]] and [[CrossMarketLeveragedETFExecutionRisk|cross-market execution risk]] beyond the fund's own NAV math.

## Connections
- [[DailyLeverageReset]], [[VolatilityDecay]], and [[FuturesRollCost]] - main mechanisms emphasized by the source.
- [[TQQQ]], [[TMF]], and [[NVDL]] - product examples in the episode.
- [[Rydex]], [[XACT]], and [[ProShares]] - development-history entities.
- [[PassiveInvesting]] and [[LeveragedProductSuitability]] - why ETF form does not imply passive long-horizon suitability.
- [[VolatilityDecay]], [[PortfolioSuitability]], and [[InvestmentRiskManagement]] - vol.124's drawdown and suitability extension.
- [[ETF7709HK|7709.HK]], [[LeveragedETFHedgingFeedback]], and [[CrossMarketLeveragedETFExecutionRisk]] - Vol.266's single-stock swap-hedging extension.
