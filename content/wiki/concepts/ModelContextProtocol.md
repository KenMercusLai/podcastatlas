---
title: "Model Context Protocol"
type: concept
tags: [ai, agents, protocols, infrastructure]
sources: [e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf]
last_updated: 2026-07-08
---

# Model Context Protocol

Model Context Protocol is the agent-connectivity layer highlighted in [[e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf]]. The episode describes MCP as a unifying standard that lets AI tools connect to databases, GitHub, Slack, ERP systems, and other external tools or data sources without every integration being bespoke.

The episode's metaphor is that MCP is a USB Type-C-like connector for the AI world. In that framing, models need more than reasoning ability: they need a standardized way to reach tools, files, systems, and context.

## Key Claims
- Agent ecosystems need a connector layer because useful work often sits across external services rather than inside the chat window.
- Standardized connectors can reduce integration friction for [[AgenticWorkflow]] and [[HeadlessSoftware]].
- MCP becomes more valuable when paired with [[AISkills]], because a skill can tell an agent how to perform a workflow while MCP gives it access to the relevant systems.
- The episode treats Anthropic's early MCP release as a strategic ecosystem move, not only a developer convenience.
- Protocol standardization does not remove trust, permission, security, or verification problems; it makes those problems more visible and operational.

## Connections
- [[Anthropic]] and [[ClaudeCode]] — source company and agent-product context.
- [[AISkills]] — procedure layer that can sit above MCP-connected tools.
- [[AgentFacingInterfaces]] and [[HeadlessSoftware]] — broader design requirement for agent-callable capability.
- [[AgentHarness]] and [[ContextEngineering]] — surrounding system that decides what context and tools an agent can use.
- [[AgentPermissionBoundaries]] and [[AICodingVerification]] — safety and correctness constraints around tool access.
