---
title: "Trend Following"
type: concept
tags: [investing, trading, risk]
sources:
  - a-gu-de-chun-xia-qiu-dong-zhongshu-zhongliang-zhongcai-ljzicmfbl9guxoqmcdd8ikdn6jbx
  - ep76-chuanyue-1940-wo-yu-gupiao-dazuoshou-lifumoer-de-zuihou-duihua-lr0fb5yfiwoxaamdwjjgh4rjeprg
  - e144-jiaoyi-de-yishu-bu-yuce-tongji-youshi-fensan-hongli-suiji-bodong-llbhc5wemintlslfwrtx4qdxts-0
  - e145-shangzhongle-4000-dian-zhishang-de-xinli-anmo-lrk6eqfqkjnihzf5pimbek4kqm9e
  - xie-yi-fen-jilv-md-daiti-wo-rushi-touzi-lnb4eenlg5uvx2btqppqa87eieuf
knowledge_schema: synthesis-v1
last_updated: 2026-10-12
---

# Trend Following

## Definition

Trend following is a trading discipline that waits for observable market strength before entering, exits when that strength fails, and uses bounded exposure to participate in large moves without claiming to predict exact tops, bottoms, or the next trade.

## Current Synthesis

Across the bounded sources, trend following is best understood as a complete repeated-game system rather than a chart signal. Right-side confirmation sacrifices the first part of a move; stop rules sacrifice some gains near the end; and repeated false starts are accepted so the portfolio remains available for rare, extended trends. The method therefore depends on market selection, explicit state transitions, position sizing, diversification, operational execution, and enough adherence for payoff asymmetry to emerge.

The newest source makes this operating layer explicit through [[ProgrammableTradingDiscipline|“纪律.md.”]] It recommends scanning across asset classes, reducing or stopping exposure when opportunity pools are weak, defining exceptional states before trading, and separating signal execution from commentary and emotion. This strengthens the page's no-prediction interpretation while preserving the central qualification: simple rules can still fail in whipsaw markets, changing regimes, or poorly chosen universes.

## Key Claims

- Trend signals describe observable strength and participation; they do not guarantee that the next position will profit.
- Confirmation, stop losses, and profit-running create an asymmetric payoff structure that can work despite frequent small losses.
- Market and sector breadth matter because forcing trades in a weak opportunity pool can turn selectivity into chronic whipsaw.
- Position size, portfolio limits, and diversification are part of the method rather than later risk overlays.
- A trend trade should not be defended with value-investing language after its exit condition fails.
- Written, programmable rules can reduce emotional interference, but only if data, exceptions, execution, and review are also specified.

## Evidence

- Right-side confirmation and exit discipline - [[ep76-chuanyue-1940-wo-yu-gupiao-dazuoshou-lifumoer-de-zuihou-duihua-lr0fb5yfiwoxaamdwjjgh4rjeprg]] connects moving averages, prior highs, volume, leadership, stop losses, and pyramiding to Livermore's interpretive case.
- Statistical repeated play - [[e144-jiaoyi-de-yishu-bu-yuce-tongji-youshi-fensan-hongli-suiji-bodong-llbhc5wemintlslfwrtx4qdxts-0]] separates signal from forecast and connects broad participation, small entries, payoff ratio, and fat-tailed winners.
- Strategy and holder fit - [[e145-shangzhongle-4000-dian-zhishang-de-xinli-anmo-lrk6eqfqkjnihzf5pimbek4kqm9e]] and [[a-gu-de-chun-xia-qiu-dong-zhongshu-zhongliang-zhongcai-ljzicmfbl9guxoqmcdd8ikdn6jbx]] place trend rules beside valuation, allocation, season, liquidity, and explicit exit discipline rather than treating momentum as universally suitable.
- Programmable operating system - [[xie-yi-fen-jilv-md-daiti-wo-rushi-touzi-lnb4eenlg5uvx2btqppqa87eieuf]] defines the tradable universe, signal transitions, portfolio sizing, exception handling, task delivery, and delegated execution as one discipline.

## Counterevidence & Qualifications

Trend following can lose repeatedly in oscillating or high-level choppy markets, and the source-specific “温、热、平” labels are not fully disclosed or independently validated. Broad scanning adds operational and instrument-specific risk. Reported hit rates and payoff ratios may not survive costs, tax, slippage, crowding, or regime change. The Livermore episode is a fictionalized teaching format, and the newest source reports one practitioner's system rather than audited performance.

## What Changed

- Migrated the page to the synthesis-v1 concept schema without changing the prior source inventory.
- Reframed trend following as an end-to-end operating system rather than a collection of entry signals.
- Added cross-asset opportunity selection, explicit exception handling, and delegated execution.
- Sharpened whipsaw and unvalidated-performance qualifications.

## Related Concepts

- [[ProgrammableTradingDiscipline]] - operationalizes trend rules as data, decisions, tasks, and exceptions.
- [[NoPredictionTrading]] - explains why a signal need not forecast the next outcome.
- [[PositionSizing]] - converts market states into survivable portfolio exposure.
- [[StopLossDiscipline]] - bounds failed entries and enforces invalidation.
- [[QuantitativeOverfitting]] - warns against optimizing trend parameters to accidental history.
- [[InvestmentStrategyFit]] - prevents a trend entry from being rationalized later as another investing style.
