---
title: "Deep Research"
type: concept
tags: [ai, agents, research, search]
sources: [e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]
last_updated: 2026-07-08
---

# Deep Research

Deep Research is the episode's frame for agentic search, planning, evidence gathering, synthesis, and tool use over longer research tasks. In [[e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]], [[DuShaolei]] says [[Apodex]] started with Deep Research because search is a basic capability for post-training and self-improvement: a model that wants to improve itself must find relevant code, papers, examples, failure cases, and candidate answers.

The source treats Deep Research as part of a larger loop rather than only a user-facing report product. Apodex's post-trained [[Qwen]]-based model is described as improving planning, search, and agent-team work, and benchmark results are discussed cautiously because search benchmarks can be contaminated by public answers.

## Key Claims
- Deep Research combines search, planning, long-horizon reasoning, and synthesis.
- Search is not a side feature; it supplies material for post-training task creation and verification.
- Agent-team design can strengthen Deep Research by letting different agents search, solve, cross-check, and preserve intermediate memory.
- Benchmark success is useful but fragile when answers can be found directly online or leak into training/evaluation.
- Deep Research becomes more valuable when connected to [[AIVerification]] and [[RecursiveSelfImprovement]], not just report generation.

## Connections
- [[Apodex]], [[DuShaolei]], [[LiBeibin]], and [[Qwen]] — company, speakers, and model context in the source.
- [[RecursiveSelfImprovement]], [[DiscoveryModel]], and [[AIVerification]] — broader loop Deep Research supports.
- [[MultiAgentCollaboration]], [[AgentHarness]], and [[PersistentAgentMemory]] — agent-system mechanisms needed for longer research tasks.
- [[Deerflow]] — existing open-source project in the wiki that began as a Deep Research-like capability.
