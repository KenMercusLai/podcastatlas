---
title: "Volatility Decay / 波动率损耗"
type: concept
tags: [investing, etf, leverage, volatility]
sources: [vol-124-xinxi-guozai-hou-ruhe-baochi-lengjing-touzi-zhang-fupan-ltpmll0jmcw-dl0-32qesddwem4l, vol-121-cong-tanhua-yixian-de-fenji-jijin-dao-fengtou-zhengjing-de-ganggan-etf-yongyuan-buyao-digu-renxing-de-fengkuang-lusagcitdozvzm8wausvecvi-qmb]
last_updated: 2026-08-06
---

# Volatility Decay / 波动率损耗

Volatility decay is the leveraged-product loss mechanism emphasized in [[vol-121-cong-tanhua-yixian-de-fenji-jijin-dao-fengtou-zhengjing-de-ganggan-etf-yongyuan-buyao-digu-renxing-de-fengkuang-lusagcitdozvzm8wausvecvi-qmb]]. In products with [[DailyLeverageReset|daily leverage reset]], alternating gains and losses can reduce the fund even if the underlying asset has not moved much over the full holding period.

The episode uses a simple example: if an index rises 10% one day and falls 10% the next, the index is nearly flat, but a three-times daily leveraged product loses more because the second day's decline is applied after a leveraged first-day gain. This path-dependence turns volatility itself into a cost.

[[vol-124-xinxi-guozai-hou-ruhe-baochi-lengjing-touzi-zhang-fupan-ltpmll0jmcw-dl0-32qesddwem4l]] adds an April 2025 market-stress reminder. [[DavidWeng|大卫翁]] points to [[TQQQ]] and [[NVDL]] drawdowns during violent technology-stock volatility to show that realized leveraged-product losses can exceed a naive multiple of the underlying move.

## Key Claims
- Volatility decay is strongest when leverage is high and the underlying asset is volatile.
- The mechanism can hurt returns even when the investor's broad directional thesis is not completely wrong.
- Single-stock leveraged ETFs can suffer larger volatility decay because individual stocks can swing more than broad indexes.
- Product documents can show scenarios where an underlying index rises modestly while the leveraged fund still loses money.
- Vol.124 adds that volatility decay is not only theoretical; it becomes visible exactly when anxious investors are most tempted to use leverage for a rebound trade.

## Connections
- [[DailyLeverageReset]] and [[LeveragedETF]] - structural source of the decay.
- [[TQQQ]], [[TMF]], and [[NVDL]] - product examples used by the episode.
- [[SingleStockLeveragedETF]] - high-volatility version of the mechanism.
- [[LeveragedProductSuitability]] and [[InvestmentRiskManagement]] - practical investor response.
- [[PortfolioSuitability]] and [[SleepWellPortfolioTest]] - vol.124's broader fit and behavior response.
