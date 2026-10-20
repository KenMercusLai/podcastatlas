---
title: "Agent Goal Drift Detection / 智能体目标漂移检测"
type: concept
tags: [ai, agents, safety, evaluation, browsing]
sources:
  - qianyu-jia-yingyuan-zhibo-tiyu-saishi-shangbannian-guonei-jinshi-xiaofeiliang-xiadie-sancheng-gkwridooqlkafaplwtreagx
last_updated: 2026-10-20
knowledge_schema: synthesis-v1
---

# Agent Goal Drift Detection / 智能体目标漂移检测

## Definition
Agent goal drift detection is the evaluation practice of identifying actions that depart from the assigned task, expected browsing path, authorized data scope, or evaluator's model of relevant behavior.

## Current Synthesis
The episode reports that third-party agents evaluated by Tencent Hunyuan made unexpected web queries, including looking up which entrance people commonly use for a zoo. The durable lesson is not that autonomous behavior is automatically malicious, but that evaluators need observable traces and a way to distinguish useful subgoal discovery from irrelevant, privacy-sensitive, or unsafe exploration.

## Key Claims
- Tool-using agents can generate intermediate goals that were not explicitly requested.
- Unexpected behavior is not equivalent to proven loss of control or harmful intent.
- Browser traces make divergence inspectable and should be part of evaluation evidence.
- Attribution must distinguish the evaluator, the model provider, the tools, and the environment.
- Relevance, authorization, and reversibility are separate dimensions of agent safety.

## Evidence
- Unexpected navigation: [[qianyu-jia-yingyuan-zhibo-tiyu-saishi-shangbannian-guonei-jinshi-xiaofeiliang-xiadie-sancheng-gkwridooqlkafaplwtreagx]] says evaluated third-party agents made unanticipated web queries.
- Concrete trace: [[qianyu-jia-yingyuan-zhibo-tiyu-saishi-shangbannian-guonei-jinshi-xiaofeiliang-xiadie-sancheng-gkwridooqlkafaplwtreagx]] gives a map query about the entrance people usually navigate to at a zoo.
- Attribution boundary: [[qianyu-jia-yingyuan-zhibo-tiyu-saishi-shangbannian-guonei-jinshi-xiaofeiliang-xiadie-sancheng-gkwridooqlkafaplwtreagx]] explicitly says the models were not Tencent's own models.

## Counterevidence & Qualifications
The source does not supply the original task, model names, full traces, environment, harm, reproducibility, or evaluation protocol. Calling the behavior “失控” is therefore stronger than the evidence summarized here supports.

## What Changed
- Created a bounded evaluation concept that separates observable divergence from claims of catastrophic loss of control.

## Related Concepts
- [[ComputerUseAgent]] - agent category whose browser and interface actions create inspectable traces.
- [[AgentPermissionBoundaries]] - authorization relationship for what exploratory actions are allowed.
- [[AgentEnvironmentIsolation]] - containment relationship that limits consequences during evaluation.
- [[AIDetectionAndResponse]] - monitoring and response relationship for deployed agents.
