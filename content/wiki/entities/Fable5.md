---
title: "Fable 5"
type: entity
tags: [ai-model, coding, agents]
sources: [vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]
last_updated: 2026-07-07
---

# Fable 5

Fable 5 is the model/product discussed in [[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]] after X-Rapid reopened access. [[JustinYan]] and [[Zili]] treat it less as a benchmark headline and more as a practical coding-workflow event: in their use, it can plan, clarify requirements, implement larger tasks, generate usable interfaces, and assess code-review feedback with fewer severe mistakes than prior models they were using.

The source repeatedly separates model capability from workflow wrapper. Some of the improvement may come from stronger base-model behavior, while some may come from [[AgentHarness]] design, [[AISkills]], and the way the model is used for planning and acceptance.

## Source Position
- Fable 5 is framed as a high-end coding and reasoning model whose strongest value appears in [[OneShotAICoding]], planning, review triage, and product-quality judgment.
- The hosts suspect the reopened version may not be the earliest "full-power" variant, but still describe it as a step change in day-to-day coding work.
- Its practical bottleneck is not only intelligence; Fable-specific limits, subscription constraints, and API spending make [[AIInferenceCostStructure]] central to whether users can rely on it.
- The preferred workflow is to use Fable 5 for discussion, PRD/spec/issue planning, and acceptance review, while delegating implementation or code review to [[Codex]] when appropriate.

## Connections
- [[Codex]] — execution and review counterpart in the described workflow.
- [[Superpowers]] and [[GrillMeSkills]] — process wrappers whose value and token cost are reassessed in light of Fable 5 capability.
- [[AICodingVerification]] and [[AIEngineeringThinking]] — verification and planning disciplines that remain necessary despite stronger one-shot output.
- [[TokenDrivenSoftware]] and [[ModelRoutingCostControl]] — downstream product and cost-control ideas prompted by the model's capability jump.
