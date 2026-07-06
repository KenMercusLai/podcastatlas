---
title: "OS-Level Context"
type: concept
tags: [agents, context, privacy, product-design]
sources: [renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]
last_updated: 2026-07-06
---

# OS-Level Context

OS-level context is [[Paperboy]]'s term-level bet that useful agents should learn from the user's computer environment rather than only from chat history. In [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]], [[JieDechen]] argues that computer-use signals are information-dense: screen activity, keyboard and mouse actions, meetings, messages, search, browsing, code, and current app state can reveal intent and work style.

## Key Claims
- OS activity can support [[PersistentAgentMemory]] because it captures work behavior that users may never write down in prompts.
- The usefulness of this context depends on compression, summarization, permission boundaries, and application-specific choices.
- Early surfaces include OS-wide autocomplete in WeChat, terminals, GitHub PRs, and other text-entry contexts.
- OS-level context can help agents write commit messages or PR descriptions by combining code changes with browser research, messages, and surrounding work.
- The approach raises trust and privacy questions because the same context that makes agents useful can also expose sensitive personal and organizational information.

## Connections
- [[ContextEngineering]] — broader practice of collecting and shaping useful model input.
- [[HumanAgentCollaboration]] — product problem OS-level context tries to improve.
- [[ProactiveAgents]] — agents need environmental context before they can help ahead of explicit requests.
- [[WeChat]] and [[Slack]] — communication contexts where OS-level assistance may appear without replacing the whole product.
