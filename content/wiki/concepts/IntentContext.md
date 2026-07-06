---
title: "Intent Context"
type: concept
tags: [agents, context, product-design]
sources: [openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]
last_updated: 2026-07-07
---

# Intent Context

Intent context is the high-signal slice of user context captured when a user is explicitly trying to do something. In [[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]], [[AirJelly]] uses Enter as the practical trigger: when the user submits a message, chatbot prompt, or search query, the surrounding screen and task state are more likely to reveal current intent than a random periodic screenshot.

The concept sits between [[OSLevelContext]] and [[PersistentAgentMemory]]. OS-level capture supplies raw evidence, but intent context tries to identify the moments worth preserving as events, entities, and task progress. The episode argues that this is what lets [[ProactiveAgents]] help along the current task's extension rather than create generic reminders or distracting suggestions.

## Key Claims
- More context is not automatically better; indiscriminate recording can bury useful signals in noise.
- Intent moments are valuable because the user has just expressed a goal, constraint, or next action.
- Proactive help should be grounded in current intent and context, not only in a profile, schedule, or broad curiosity model.
- Intent context must still be bounded by privacy, permission, local storage, encryption, and user control.
- Durable memory depends on converting intent context into maintained events and entities rather than storing every screenshot as equal-value history.

## Connections
- [[AirJelly]] and [[HuangBote]] — product and founder that make the concept concrete.
- [[OSLevelContext]] — raw environment context from which intent context is selected.
- [[PersistentAgentMemory]] — durable store that intent context feeds.
- [[ProactiveAgents]] — agent behavior that needs intent context to avoid becoming interruption.
- [[ContextEngineering]] and [[HumanAgentCollaboration]] — broader practices for making agent assistance useful.
