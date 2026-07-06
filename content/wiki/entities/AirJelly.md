---
title: "AirJelly"
type: entity
tags: [ai-tool, agent, startup]
sources: [openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]
last_updated: 2026-07-07
---

# AirJelly

AirJelly is the proactive context-aware personal-agent product discussed in [[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]]. Founder [[HuangBote]] describes it as a partner that remembers what the user is doing across places, understands task state, and appears at the right moment to help rather than waiting for a fully specified prompt.

The product descends from [[Mycontext]], but changes the capture strategy from periodic screenshots toward event- and intent-triggered context. Its signature mechanism is treating Enter as an [[IntentContext]] signal across IM, chatbot, and search workflows; when the user submits something, AirJelly captures the surrounding screen and then organizes the result into events and entities for [[PersistentAgentMemory]].

## Key Points
- AirJelly combines [[OSLevelContext]], memory, and execution ability: it can read documents and code, call skills, use a browser, operate a computer, and use stored context.
- [[OpenClaw]] and [[ClaudeCode]] influenced the product, but also pushed the team away from simplified task-execution tooling toward context acquisition, storage, and recall as the harder layer.
- The product tries to make [[ProactiveAgents]] task-continuing rather than distracting: suggestions should extend the user's current intent instead of adding loosely related information.
- Privacy is a central risk because the product touches screenshots and personal context; the source says AirJelly plans local storage for images/virtual context, end-to-end encryption, and PII desensitization.
- The team is also experimenting with an internal team version where personal agents coordinate in a group, while keeping sharing voluntary rather than turning AirJelly into monitoring software.

## Connections
- [[HuangBote]] — founder and main speaker in the episode.
- [[Yihao]] and [[QuickStone]] — investor context for the company.
- [[Mycontext]] — predecessor project behind the context-capture idea.
- [[ProactiveAgents]], [[IntentContext]], [[OSLevelContext]], and [[PersistentAgentMemory]] — core product thesis.
- [[HumanAgentCollaboration]] and [[AgentNativeSoftware]] — broader product-design frame.
- [[OpenClaw]], [[ClaudeCode]], [[Manus]], and [[ChatGPT]] — comparison products used to define AirJelly's difference.
