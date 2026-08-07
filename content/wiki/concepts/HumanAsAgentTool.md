---
title: "Human As Agent Tool / 人作为 AI 工具"
type: concept
tags: [ai, agents, workflow, human-agent-collaboration]
sources: [ep119-duihua-liu-kefan-yong-try-catch-finally-gei-duli-zuo-chanpin-de-neihao-xie-ge-chuli-liucheng-ludjc3ab-jbwpci6tpaajtffsblx]
last_updated: 2026-08-08
---

# Human As Agent Tool / 人作为 AI 工具

Human as agent tool is the workflow pattern [[LiuKefan|刘可凡]] describes in [[ep119-duihua-liu-kefan-yong-try-catch-finally-gei-duli-zuo-chanpin-de-neihao-xie-ge-chuli-liucheng-ludjc3ab-jbwpci6tpaajtffsblx]] when he says the direction may move from "people use AI" toward "AI uses people." In his small experiment, he built an MCP server and connected it to [[ClaudeCode]] so the model could call on a human to perform small real-world actions, like opening a short-video app or finding a podcast, in the same broad pattern as tool calling.

The concept is not a settled claim that AI should command people. In the source, it is a low-cost experiment inside a concrete business workflow: can an agent coordinate enough small human perception or action to improve efficiency? That keeps the idea connected to [[AgenticWorkflow]], [[ModelContextProtocol]], and [[HumanAgentCollaboration]], while preserving [[HumanJudgmentUnderAI]] around permission, interest alignment, and task boundaries.

## Key Claims
- Some useful agent workflows may need human hands, eyes, accounts, or local judgment when no clean API is available.
- Treating the human as callable capability can increase efficiency, but it also raises permission, incentive, dignity, and responsibility questions.
- The pattern is strongest when the human action is narrow, reversible, and reviewed rather than open-ended obedience.
- A human-callable workflow should expose boundaries, expected output, and escalation rules just as ordinary tools should expose permissions and errors.
- The source frames the idea as an experiment to validate workflow efficiency, not as proof that a broad AI-led organization model has already arrived.

## Connections
- [[LiuKefan]] - source person and experimenter.
- [[ClaudeCode]], [[ModelContextProtocol]], [[AgenticWorkflow]], and [[AgentFacingInterfaces]] - infrastructure and interface context.
- [[HumanAgentCollaboration]], [[AgentPermissionBoundaries]], and [[HumanJudgmentUnderAI]] - governance and responsibility boundaries.
- [[AIAsBusinessOperator]] and [[OnePersonCompany]] - business-operator contexts where small human-agent loops may matter.
