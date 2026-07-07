---
title: "Quantitative Overfitting"
type: concept
tags: [investing, statistics, risk]
sources: [ep88-chuanyue-lianghua-zhifu-ximengsi-ai-hui-rang-putongren-geng-rongyi-zhuanqian-haishi-geng-nan-lhvigzza2ugmayezkbrxufkmp4l1, e144-jiaoyi-de-yishu-bu-yuce-tongji-youshi-fensan-hongli-suiji-bodong-llbhc5wemintlslfwrtx4qdxts-0]
last_updated: 2026-07-08
---

# Quantitative Overfitting

Quantitative overfitting is the danger that a trading rule looks profitable in historical data but fails outside the sample. In [[ep88-chuanyue-lianghua-zhifu-ximengsi-ai-hui-rang-putongren-geng-rongyi-zhuanqian-haishi-geng-nan-lhvigzza2ugmayezkbrxufkmp4l1]], [[JimSimons]]'s episode persona treats it as one of the main reasons ordinary investors should distrust backtests, seasonal patterns, and widely circulated "holy grail" strategies.

[[e144-jiaoyi-de-yishu-bu-yuce-tongji-youshi-fensan-hongli-suiji-bodong-llbhc5wemintlslfwrtx4qdxts-0]] adds [[RandomMarketNarratives]] as the narrative counterpart. Its random "山海经神兽" experiment shows how convincing explanations can be generated from price paths even when the underlying process was designed to have no real causal story.

## Key Claims
- A pattern needs a plausible mechanism, not only an attractive chart.
- Out-of-sample testing matters because history contains many accidental regularities.
- Simpler and more robust rules are preferred over complicated rules that perfectly fit past noise.
- Machine learning does not excuse blind pattern mining; researchers still need hypotheses and judgment.
- Overfit signals can decay quickly once they are public or once market conditions change.
- A random experiment can still produce apparent winners, sectors, and themes, so backtests need humility about causality.

## Connections
- [[QuantitativeInvesting]] — method most exposed to this statistical failure mode.
- [[MarketRegimeShift]] — another reason a historical strategy can stop working.
- [[MarketEfficiency]] — alpha is small and temporary when markets are close to efficient.
- [[AIInvestmentResearch]] — AI can accelerate both useful analysis and spurious pattern discovery.
- [[RandomMarketNarratives]] and [[BehavioralInvestingBiases]] — E144's story-generation warning around random price paths.
