---
title: "Self-Built Agent Workflow"
type: concept
tags: [agents, workflow, automation, ai-coding]
sources:
  - vol-173-pingguo-huanshuai-claude-5-1-fabu-glm-dijia-toujia-yingweida-yao-mai-hugging-face-deng-1-6689-1
last_updated: 2026-09-05
knowledge_schema: synthesis-v1
---
# Self-Built Agent Workflow

## Definition
A self-built agent workflow is a user-composed automation stack that combines models, coding agents, scripts, chat surfaces, notification channels, and routing rules instead of relying on one bundled AI product.

## Current Synthesis
Vol. 173 presents self-built agent workflows as the natural pattern for advanced AI users whose needs exceed any single app's default interface. The source's examples span Fable-to-Codex-style handoffs, Hermes, Telegram-style control, OpenCrawl comparison, Ultra Fast mode, and model routing among Claude, Codex, GLM, Kimi, Qwen, and others. The implication is that power users treat AI systems as replaceable components in a personal operating layer, with switching costs tied to integrations and habits rather than only model quality.

## Key Claims
- Advanced users often compose their own workflow layer from multiple AI products.
- The workflow layer can outlast individual model preferences because tools are routed by task.
- All-in-one products must beat existing habits, scripts, and messaging-control surfaces to displace custom stacks.
- Self-built workflows increase leverage but also require the user to manage permissions, reliability, context, and failure modes.
- Model access changes or quota limits can be absorbed more easily when the workflow already supports fallback routes.

## Evidence
- Workflow-composition evidence: [[vol-173-pingguo-huanshuai-claude-5-1-fabu-glm-dijia-toujia-yingweida-yao-mai-hugging-face-deng-1-6689-1]] discusses moving work between Fable and Codex and combining agent tools with personal automation.
- Product-substitution evidence: [[vol-173-pingguo-huanshuai-claude-5-1-fabu-glm-dijia-toujia-yingweida-yao-mai-hugging-face-deng-1-6689-1]] says OpenCrawl 2.0 looks broad but may be less useful for a user who already has a custom workflow.
- Resilience evidence: [[vol-173-pingguo-huanshuai-claude-5-1-fabu-glm-dijia-toujia-yingweida-yao-mai-hugging-face-deng-1-6689-1]] places quota problems, Cursor access changes, and cheap-model routing inside the same workflow-management problem.

## Counterevidence & Qualifications
Self-built workflows can be brittle, hard to maintain, and unsafe if permission boundaries are loose. Less technical users may prefer integrated products even when those products are less customizable.

## What Changed
- Created this concept to capture the user's personal AI orchestration layer as a distinct pattern from any one agent product.

## Related Concepts
- [[AgentHarness]] - technical wrapper pattern for coordinating tools and model calls.
- [[OpenCrawl]] - all-in-one workflow product compared with custom stacks.
- [[HermesAgent]] - component referenced in the source's custom workflow discussion.
- [[OpenClaw]] - adjacent browser or agent-control tooling context.
- [[ComputerUseAgent]] - permission and app-control area that custom workflows may invoke.
- [[ModelRoutingCostControl]] - model-selection practice used inside self-built workflows.
- [[TokenEfficientAgentWorkflow]] - efficiency practice that complements custom orchestration.
- [[AgentPermissionBoundaries]] - safety constraint for user-built automation.
- [[IMAgentInterfaces]] - messaging surface pattern for controlling agents.
