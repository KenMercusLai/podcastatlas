---
title: "Office Agent Harness Design"
type: concept
tags: [ai, agents, office, harness]
sources:
  - 272-cong-feishu-jizuo-dao-agent-youxian-doubao-gongzuo-all-in-one-jinzhui-workbuddy-lqmfcnfkkhoxt440qy26vwpnvswp
knowledge_schema: synthesis-v1
last_updated: 2026-09-03
---

# Office Agent Harness Design

## Definition

Office agent harness design is the product and infrastructure layer that lets an [[AIOfficeAgent|AI office agent]] turn workplace context, tools, files, connectors, model calls, and review loops into reliable task execution.

## Current Synthesis

The source makes office-agent competition less about whether a product can list many skills and more about whether the harness can choose, compress, route, observe, and verify them. In [[DoubaoWork|Doubao Work]], many skills, multiple entry points, file/context handling, and multi-agent execution show meaningful capability coverage, but [[ZhongJingwei|钟静伟]] argues that missing harness details can raise cost and lower reliability.

The strongest design lesson is that office work inherits coding-agent harness problems while losing coding's clean tests. Tool search, tool-schema compression, long-result compression, preloaded time and machine context, visible skill selection, and direct multi-agent delegation all shape whether the agent finishes a task efficiently or burns tokens through indirect coordination.

## Key Claims

- Visible feature coverage is not enough; the harness decides whether tools and context become usable work.
- Skill abundance can become confusing when users cannot see what was loaded, truncated, or ignored.
- Multi-agent orchestration can add cost, latency, and information loss when delegation passes through unnecessary planning layers.
- Tool search, schema compression, result compression, and environment context are office-agent product quality issues.
- Model choice and BYOK are part of workflow fit, cost, and trust design rather than only advanced-user settings.
- Office agents need stronger review and observability because document, meeting, and workflow outputs are harder to test than code.

## Evidence

- **Skill and context handling:** [[272-cong-feishu-jizuo-dao-agent-youxian-doubao-gongzuo-all-in-one-jinzhui-workbuddy-lqmfcnfkkhoxt440qy26vwpnvswp]] reports that Doubao Work preloads many skills, shows context-share effects, and appears to truncate as more skills are added.
- **Multi-agent architecture:** [[272-cong-feishu-jizuo-dao-agent-youxian-doubao-gongzuo-all-in-one-jinzhui-workbuddy-lqmfcnfkkhoxt440qy26vwpnvswp]] says Zhong Jingwei observed an architect-agent layer that dispatches subagents and then aggregates, which he argues may waste tokens and lose information.
- **Missing optimizations:** [[272-cong-feishu-jizuo-dao-agent-youxian-doubao-gongzuo-all-in-one-jinzhui-workbuddy-lqmfcnfkkhoxt440qy26vwpnvswp]] names tool search, tool-schema compression, long-result compression, and basic time/computer context as expected harness optimizations.
- **Competitive significance:** [[272-cong-feishu-jizuo-dao-agent-youxian-doubao-gongzuo-all-in-one-jinzhui-workbuddy-lqmfcnfkkhoxt440qy26vwpnvswp]] compares WorkBuddy as temporarily ahead at the harness layer while Doubao Work may catch up through ByteDance's resources and Feishu context.

## Counterevidence & Qualifications

- The observations come from a small number of reported product tests, so they may not represent every task or later versions.
- More explicit orchestration can still help if it improves safety, planning, permissions, or auditability; the source critiques unnecessary indirection, not all multi-agent structure.
- Office-agent harness quality cannot be separated from model capability, enterprise context, and customer permissions.

## What Changed

- Added an office-specific harness concept grounded in Doubao Work and WorkBuddy product tests.
- Separated visible feature completeness from context/tool orchestration quality.

## Related Concepts

- [[AgentHarness]] - broader model-external system that office-agent harnesses instantiate.
- [[HarnessEngineering]] - engineering practice for building and improving harnesses.
- [[AIOfficeAgent]] - product category where the office harness operates.
- [[MultiAgentCollaboration]] - orchestration pattern affected by delegation cost and information loss.
- [[ContextEngineering]] - context-loading and compression layer inside the harness.
- [[ModelWorkflowFit]] - model and surface fit that changes harness behavior.
- [[AIInferenceCostStructure]] - token and latency cost affected by harness design.
- [[AgentPermissionBoundaries]] - safety and authority layer required for office execution.
