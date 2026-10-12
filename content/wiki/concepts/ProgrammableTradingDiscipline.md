---
title: "Programmable Trading Discipline / 可编程交易纪律"
type: concept
tags: [investing, trading, automation, risk]
sources:
  - xie-yi-fen-jilv-md-daiti-wo-rushi-touzi-lnb4eenlg5uvx2btqppqa87eieuf
knowledge_schema: synthesis-v1
last_updated: 2026-10-12
---

# Programmable Trading Discipline / 可编程交易纪律

## Definition

Programmable trading discipline is a precommitted decision system that defines what may be traded, which observable states trigger entry or exit, and how much exposure is allowed before live market emotion can rewrite the rules.

## Current Synthesis

[[xie-yi-fen-jilv-md-daiti-wo-rushi-touzi-lnb4eenlg5uvx2btqppqa87eieuf]] uses “纪律.md” to turn [[TrendFollowing]] from a chart-reading idea into an operating contract. Data collection, signal generation, task delivery, position targets, exception handling, and execution can be delegated to software or a fixed operator, but the investor still owns rule design, market selection, risk tolerance, and review. The purpose is not to automate certainty; it is to preserve a chosen repeated-game structure when profit, loss, commentary, and fear would otherwise change behavior.

## Key Claims

- The discipline begins with an eligible universe constrained by access, liquidity, asset class, and position capacity.
- Entry and exit rules must cover ordinary transitions as well as skipped states, bad data, failed orders, and market-specific exceptions.
- Instrument size, portfolio exposure, and opportunity density belong in the same rule set as the signal.
- Automation can separate observation and execution from public opinion, but it cannot prove that the underlying strategy has an edge.
- A mature discipline should become simpler after experience identifies which exceptions matter and which parameters merely fit history.
- Long-run adherence is part of the strategy because frequent post-loss parameter changes destroy comparability across repeated trades.

## Evidence

- Rule architecture - [[xie-yi-fen-jilv-md-daiti-wo-rushi-touzi-lnb4eenlg5uvx2btqppqa87eieuf]] specifies market scope, entry and exit states, and position management as the three layers of “纪律.md.”
- Execution separation - [[xie-yi-fen-jilv-md-daiti-wo-rushi-touzi-lnb4eenlg5uvx2btqppqa87eieuf]] describes end-of-day signals, email delivery, opening orders, and a fixed executor who reduces discretionary interference.
- Exception completeness - [[xie-yi-fen-jilv-md-daiti-wo-rushi-touzi-lnb4eenlg5uvx2btqppqa87eieuf]] says rules must address abnormal data, order failure, skipped market states, and conflicting conditions.
- Statistical boundary - [[xie-yi-fen-jilv-md-daiti-wo-rushi-touzi-lnb4eenlg5uvx2btqppqa87eieuf]] keeps low win rates, payoff asymmetry, repeated trials, and overfitting risk inside the operating model.

## Counterevidence & Qualifications

The episode reports one practitioner's method and does not provide audited performance, complete signal definitions, transaction-cost analysis, or an independently reproducible backtest. Clear code can execute a bad strategy consistently. Delegation also creates operational, data, brokerage, and supervision risks, while a discipline designed for one person's capital and tolerance may be unsuitable for another.

## What Changed

- Created a concept separating explicit trading operations from the broader ideas of trend following and investment risk management.

## Related Concepts

- [[TrendFollowing]] - supplies the market-state and right-side entry logic used by the discipline.
- [[NoPredictionTrading]] - explains why the rules can operate without certainty about the next trade.
- [[PositionSizing]] - converts signals into survivable exposure.
- [[StopLossDiscipline]] - defines the loss-bounding exit mechanism.
- [[QuantitativeOverfitting]] - constrains parameter refinement and historical optimization.
- [[HumanAgencyUnderAI]] - keeps objective and acceptance responsibility with the human even when software executes the workflow.
