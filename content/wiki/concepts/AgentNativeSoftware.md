---
title: "Agent Native Software"
type: concept
tags: [agents, software-design, product]
sources: [20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto, vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1, openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6, vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]
last_updated: 2026-07-07
---

# Agent Native Software

Agent-native software is software whose core substrate is an agent rather than a traditional app with an AI feature bolted on. In [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]], [[JustinYan]] and [[Zili]] frame [[OpenClaw]] this way: the surrounding code, tools, channels, UI, and [[AISkills]] act as the agent's hands, senses, and work environment, while the agent itself is what makes the product coherent.

[[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]] adds [[AirJelly]] as a context-first agent-native case. [[HuangBote]] argues that task execution and orchestration alone can be copied quickly, while the harder product layer is giving the agent senses, memory, timing, and privacy-aware context. This reframes agent-native software as not only "what can the agent do," but "what can the agent know safely and at the right moment."

[[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] adds a packaging-centered view. [[YaGe]] and [[Haoda]] argue that [[OpenClaw]] became legible because it combined [[IMAgentInterfaces]], [[LocalAgentExecution]], memory, skills, and tool feedback into a product users could treat as a trainable assistant rather than a normal app with an AI button.

[[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]] extends the form into [[TokenDrivenSoftware]]. Instead of only treating the agent as a worker behind fixed app screens, the hosts imagine software whose interface, interaction flow, and world behavior are generated at run time from context. This makes [[ModelRoutingCostControl]] and [[AIInferenceCostStructure]] part of product design, because dynamic behavior can become expensive if every generated surface uses the top model.

## Key Claims
- Agent-native software differs from AI-assisted software because removing the agent would remove the product's reason to exist.
- The design center shifts from screens and static feature menus toward [[AgentHarness]] choices: tools, permissions, channels, triggers, memory, and feedback loops.
- [[AISkills]] become product surface because they define reusable capabilities and can sometimes be created or refined by the agent itself.
- [[OnDemandApps]] are one possible downstream form: the agent assembles or generates capabilities at the moment of need instead of exposing only prebuilt app functions.
- Agent-native software increases the importance of [[AgentPermissionBoundaries]] because broader action capacity also broadens failure and leakage risk.
- Context capture and memory can be as much a product surface as tools and skills, especially for personal agents that need to act before being prompted.
- Accessibility and entry point can be as important as raw capability: an IM surface plus local runtime can expose existing CLI-agent power to many more users.
- Token-driven interaction broadens agent-native software from task execution into dynamic experience generation, but increases cost, latency, and quality-control requirements.

## Connections
- [[OpenClaw]] — source example of an agent-native product form.
- [[AgentHarness]], [[AgenticWorkflow]], and [[AgentFacingInterfaces]] — infrastructure and interface layer that agent-native software depends on.
- [[AISkills]], [[AgentSelfEvolution]], and [[PersistentAgentMemory]] — mechanisms for durable and self-improving capability.
- [[HeadlessSoftware]] — adjacent thesis that software value should be callable by agents rather than trapped in GUI-first flows.
- [[OnDemandApps]] and [[AgentPermissionBoundaries]] — new concepts added by the same source.
- [[AirJelly]], [[IntentContext]], [[OSLevelContext]], and [[ProactiveAgents]] — context-first agent-native case added by the AirJelly source.
- [[IMAgentInterfaces]], [[LocalAgentExecution]], [[YaGe]], and [[Haoda]] — OpenClaw product-mechanics case added by the 20-question episode.
- [[TokenDrivenSoftware]], [[GeneratedWorkInterfaces]], and [[ModelRoutingCostControl]] — Vol. 170's dynamic-interface and cost-control extension.
