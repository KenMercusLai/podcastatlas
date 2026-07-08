---
title: "OS-Level Context"
type: concept
tags: [agents, context, privacy, product-design]
sources: [renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o, openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6, ai-shidai-de-chaoji-rukou-haishi-shouji-ma-s10e17-523a0d42-4c16-4dd6-a2ab-9277fec1a731]
last_updated: 2026-07-09
---

# OS-Level Context

OS-level context is [[Paperboy]]'s term-level bet that useful agents should learn from the user's computer environment rather than only from chat history. In [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]], [[JieDechen]] argues that computer-use signals are information-dense: screen activity, keyboard and mouse actions, meetings, messages, search, browsing, code, and current app state can reveal intent and work style.

[[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]] adds [[AirJelly]]'s capture strategy. Instead of treating every few seconds of screen activity as equally valuable, [[HuangBote]] argues that Enter-triggered screenshots can capture [[IntentContext]] in IM, chatbot, and search workflows with less browsing noise. The source also makes privacy a first-order design constraint because OS-level screenshots may expose sensitive personal or organizational information.

[[ai-shidai-de-chaoji-rukou-haishi-shouji-ma-s10e17-523a0d42-4c16-4dd6-a2ab-9277fec1a731]] adds the smartphone version. [[ChenYiqiang]] argues that phones contain both physical-world and virtual-world information, making them useful for real-time sensing and user understanding; [[HanBoxiao]] treats recognition and memory as likely terminal-side functions before cloud reasoning is invoked.

## Key Claims
- OS activity can support [[PersistentAgentMemory]] because it captures work behavior that users may never write down in prompts.
- The usefulness of this context depends on compression, summarization, permission boundaries, and application-specific choices.
- Early surfaces include OS-wide autocomplete in WeChat, terminals, GitHub PRs, and other text-entry contexts.
- OS-level context can help agents write commit messages or PR descriptions by combining code changes with browser research, messages, and surrounding work.
- The approach raises trust and privacy questions because the same context that makes agents useful can also expose sensitive personal and organizational information.
- Intent-triggered capture can make OS-level context higher signal than fixed-interval recording, but it may miss long conversations or feedback unless users can supplement context manually.
- Smartphone context extends the idea beyond desktop activity: camera, microphone, files, meetings, location-like surroundings, and personal preferences can all become local signals, which makes the [[EdgeCloudAIBoundary]] and permission design more important.

## Connections
- [[ContextEngineering]] — broader practice of collecting and shaping useful model input.
- [[HumanAgentCollaboration]] — product problem OS-level context tries to improve.
- [[ProactiveAgents]] — agents need environmental context before they can help ahead of explicit requests.
- [[WeChat]] and [[Slack]] — communication contexts where OS-level assistance may appear without replacing the whole product.
- [[AirJelly]], [[IntentContext]], and [[PersistentAgentMemory]] — example of turning OS-level screenshots into events, entities, and memory.
- [[SmartphoneAIHub]], [[OnDeviceAI]], and [[EdgeCloudAIBoundary]] — phone-side context and privacy branch added by S10E17.
