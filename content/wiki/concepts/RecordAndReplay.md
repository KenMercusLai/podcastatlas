---
title: "Record and Replay"
type: concept
tags: [computer-use, agents, workflow-automation]
sources: [ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1]
last_updated: 2026-07-08
---

# Record and Replay

Record and Replay is the [[OpenAI]] computer-use mechanism described in [[ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1]]. The source says the system records a human completing a computer task, turns the workflow into a skill, and later lets the AI replay or adapt that process automatically.

The episode compares this to robot teleoperation: a human demonstrates an action path, and the system converts the demonstration into a repeatable capability. Its significance is that [[ComputerUseAgent]] progress may come not only from better visual reasoning, but also from workflow capture, skill libraries, and an [[AgentHarness]] that can replay actions safely.

## Key Claims
- Recording real human workflows can transfer tacit GUI operation into an agent-readable routine.
- Repeatability depends on interface stability, task boundaries, credential handling, latency, and recovery from changed screens.
- Privacy and permission rules matter because recorded workflows may expose accounts, documents, and business processes.
- Record-and-replay systems still need [[HumanJudgmentUnderAI]] and verification when tasks affect money, code, customers, or regulated data.
- The route is more structured than free-form GUI clicking, but less flexible than a fully general reliable computer-use agent.

## Connections
- [[OpenAI]] and [[Codex]] — company and agent context in the source.
- [[ComputerUseAgent]] — broader agent category.
- [[AgentHarness]], [[AgentPermissionBoundaries]], and [[AICodingVerification]] — infrastructure and safety context.
- [[ClaudeTag]] — parallel Q2 route for turning agents into repeatable workplace participants.
