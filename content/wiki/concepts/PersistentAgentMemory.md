---
title: "Persistent Agent Memory"
type: concept
tags: [agents, memory, context]
sources: [e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb, 20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto, renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o, tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3, dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd, openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6, vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1, vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1, vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1, dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]
last_updated: 2026-07-08
---

# Persistent Agent Memory

Persistent agent memory is the durable user model that [[Paperboy]] wants to build from [[OSLevelContext]]. In [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]], [[JieDechen]] describes a memory system that maintains a markdown-like representation of a user's profession, recent days, recent minutes, and current seconds, with finer granularity near the present.

[[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]] adds a tool-harness version through [[ClaudeCode]]. [[LaiXinlu]] describes memory as markdown/file-based state that can be selectively loaded like skills, updated by stop-hook agent passes, and periodically consolidated by an AutoDream-like process after enough sessions accumulate.

[[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]] adds [[HermesAgent]] as a product case where memory is the central differentiator after the [[OpenCloud]] and [[OpenClaw]] wave. The source emphasizes multi-layer memory, user-agent co-adaptation, and memory that can preserve successful workflows as [[AISkills]].

[[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]] adds [[AirJelly]]'s event/entity version of memory. [[HuangBote]] argues that not every recorded moment should become "history"; useful memory should preserve key events, entities, task progress, and changes in state. AirJelly uses merge, time decay, vector retrieval, and reranking to keep personal memory from becoming polluted by equal-weight raw recordings.

[[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] adds [[OpenClaw]]'s perceived "human feel" version. The episode describes a layered memory stack: raw logs, a medium-term memory file, and longer-term preference or user-profile files that preserve taste, opinions, and values. [[YaGe]] and [[Haoda]] treat this memory as part of why the agent feels like a growing assistant rather than a stateless tool.

[[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]] adds a multi-session IM memory case. [[JustinYan]] describes separating Telegram group chats by topic so each agent context can have different settings, reactions, users, and memory, while still drawing on calendar, reminder, and Obsidian records to assemble a daily todo.

[[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]] adds a diary-and-search version from [[WangJunyu]]'s OpenClaw reading. Long memory can be implemented through daily notes plus retrieval over prior conversations, and becomes more useful when paired with [[AISkills]] that preserve how tasks should be done.

[[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]] adds the context-rot and consciousness speculation boundary. The hosts see long memory as necessary for more stable agents, but warn that raw accumulation is not enough: useful memory must be recalled naturally, compressed without losing meaning, and kept from making stale context feel current.

[[dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]] adds the lock-in and portability angle. [[OpenClaw]]'s Memory directory is described as holding conversations, habits, and preferences that become more valuable as they accumulate, making migration harder. The hosts speculate about a third-party "one memory" layer, similar in spirit to a password manager, that could separate durable personal memory from any single assistant app.

[[e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb]] adds the "raising AI" version. Memory is not treated as a magic personality file; it is a habit of feeding back what the user accepts, rejects, prefers, and repeatedly does, then turning those lessons into files, rules, and [[AISkills]] that can be selectively recalled.

## Key Claims
- Memory should preserve useful chat, work, meeting, code, message, and browsing context even after an individual session ends.
- More persistent memory can reduce explicit prompting because the agent already knows the user's taste, work history, and current activity.
- Memory must encode relationship boundaries: the agent should learn what the user would share with different people and ask before crossing uncertain lines.
- Persistent memory enables [[ProactiveAgents]] because the agent can notice upcoming meetings, unfinished work, efficiency problems, or relevant connections across research threads.
- Memory quality is a product problem, not only a database problem: what to store, compress, forget, surface, and ask about depends on the use case.
- Memory and [[AISkills]] can overlap: saved experience, SOPs, task reports, and reusable instructions may be maintained by agents rather than separated into clean product categories.
- Memory can change user behavior because users start treating agent failures partly as training and onboarding problems, not only product bugs.
- For consumer agents, memory can become a moat when weeks or months of accumulated context make switching tools costly.
- Memory systems need forgetting, merging, and weighting, because full capture without curation can make all context look equally important.
- Memory can change user tolerance: failures may be interpreted as onboarding or training a helper when the agent seems to remember and improve.
- Session boundaries can be a memory design feature: different threads or groups may intentionally remember different things to keep persona, permissions, and context from collapsing into one global agent.
- Long memory is more than user profile storage; it can combine daily summaries, searchable history, and reusable task procedures.
- Memory can fail by becoming stale or over-compressed; forgetting and context refresh are part of the product, not merely implementation details.
- Memory portability may become an AI-era lock-in and trust issue because a user's accumulated preferences, conversations, and work methods can be harder to move than ordinary files.
- Useful memory should preserve the user's acceptance and rejection patterns, because those patterns become practical [[OutputQualityGates]] for future work.

## Connections
- [[ContextEngineering]] — broader discipline for making context durable and useful.
- [[AgenticWorkflow]] — workflows compound when context persists across tasks.
- [[HumanAgentCollaboration]] — long-running collaboration requires shared memory.
- [[DigitalEmployees]] — enterprise analog where AI workers need onboarding and organizational memory.
- [[AgentHarness]], [[ClaudeCode]], and [[LearnClaudeCode]] — tool-harness examples where memory is part of the execution environment.
- [[HermesAgent]], [[OpenCloud]], and [[OpenClaw]] — agent-product context where memory stability becomes a visible product requirement.
- [[AirJelly]], [[IntentContext]], and [[Mycontext]] — proactive personal-agent case where memory grows from intent-triggered OS context.
- [[OpenClaw]], [[YaGe]], [[Haoda]], and [[IMAgentInterfaces]] — consumer-agent case where memory reinforces familiarity and relationship-like interaction.
- [[JustinYan]], [[HermesAgent]], [[AgentPermissionBoundaries]], and [[AISkills]] — multi-session personal-agent memory case added by Vol. 167.
- [[WangJunyu]], [[AISkills]], and [[ProactiveAgents]] — Vol. 165's daily-memory and method-memory interpretation.
- [[ContextEngineering]], [[AICommunicationAbility]], and [[AgenticSoftware]] — Vol. 164's memory and context-rot extension.
- [[DataPortabilityAndSustainableTools]] and [[AgentPermissionBoundaries]] — portability and trust questions raised by the Keji Luandun "one memory" discussion.
- [[PingGe]], [[OutputQualityGates]], and [[AIUsePacing]] — E163's memory-as-training and finite-attention extension.
