---
title: "Kelly Criterion"
type: concept
tags: [investing, trading, risk, position-sizing]
sources: [e153-gushen-de-paiju-fuli-gongshi-kaili-gongshi-lmyvi9mnlaqib-baspjiehz3epqc, e144-jiaoyi-de-yishu-bu-yuce-tongji-youshi-fensan-hongli-suiji-bodong-llbhc5wemintlslfwrtx4qdxts-0, vol-103-wenyi-fuxing-keji-ximengsi-de-fengshen-zhilu-shi-lianghua-zhiwang-gengshi-dongcha-renxing-de-dashi-lulzvnaxdb4klqag-p2yyqlmiikl]
last_updated: 2026-07-15
---

# Kelly Criterion

Kelly Criterion is the repeated-bet sizing frame in [[e153-gushen-de-paiju-fuli-gongshi-kaili-gongshi-lmyvi9mnlaqib-baspjiehz3epqc]]. The episode presents it as a tool for maximizing long-term logarithmic capital growth while avoiding ruin, not as a license to concentrate aggressively on a single attractive trade.

[[e144-jiaoyi-de-yishu-bu-yuce-tongji-youshi-fensan-hongli-suiji-bodong-llbhc5wemintlslfwrtx4qdxts-0]] uses the same repeated-game logic in a trend-trading context. It discusses win rate, payoff ratio, and small signal-combination backtests as inputs one might use to estimate a Kelly-like position, while warning that past signal statistics should not be treated as future certainty.

[[vol-103-wenyi-fuxing-keji-ximengsi-de-fengshen-zhilu-shi-lianghua-zhiwang-gengshi-dongcha-renxing-de-dashi-lulzvnaxdb4klqag-p2yyqlmiikl]] connects Kelly-style sizing to [[ElwynBerlekamp]] and the [[MedallionFund]]'s short-horizon trading turn. The source emphasizes that sizing could not be separated from trading costs, margin, delay, market impact, and [[HumanRiskOverride]].

## Key Claims
- Kelly applies best to repeated or effectively infinite games where survival matters more than one dramatic win.
- The formula requires estimates of win probability and payoff ratio, but the episode stresses that real investors often overestimate both.
- When no edge exists, the Kelly logic says not to play, or to avoid long exposure, rather than force a trade.
- Fractional Kelly, such as half Kelly or quarter Kelly, reduces theoretical maximum return but improves drawdown tolerance and emotional stability.
- The episode's implementation advice is to review one's own trade records by strategy or asset class, estimate win rate and payoff ratio, then discount the result.
- E144 reinforces that a low hit rate can still support a position if payoff asymmetry is high enough, but only if the estimates come from comparable repeated trades.
- High leverage can make a positive-expectation setup fragile because a single bad path can remove the investor from the repeated game.
- Add-on buying requires higher confidence or payoff than the first entry because the position is already exposed to correlated risk.
- Vol.103 adds that Kelly-style logic becomes practical only after execution frictions, leverage, and model-interruption rules are included in the system.

## Connections
- [[EdwardThorp]] and [[ClaudeShannon]] — historical and theoretical figures used to explain the idea.
- [[PositionSizing]] — practical application layer for trades and portfolios.
- [[InvestmentEdge]] — the criterion matters only when the bettor has positive expectation.
- [[CompoundingGrowthFormula]] — Kelly governs the position-size part of the broader growth frame.
- [[InvestmentRiskManagement]], [[StopLossDiscipline]], and [[Pyramiding]] — trading discipline concepts reinforced by the source.
- [[NoPredictionTrading]] — E144's trend-system use case for repeated-bet sizing.
- [[ElwynBerlekamp]], [[ShortTermStatisticalArbitrage]], and [[MedallionFund]] — vol.103's institutional quant use case.
