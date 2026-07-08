---
title: "Agent Native Software"
type: concept
tags: [agents, software-design, product]
sources: [20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto, vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1, vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1, vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1, openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6, vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1, vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1, 141-freda-de-touzi-zhaji-di-2-ji-tokenmaxxing-ba-dianji-sai-jin-zhengqiji-jielisai-bian-lanqiusai-gudu-ren-de-lianjie-lmeczs2jtkze79rkpvm-rc5yw22m]
last_updated: 2026-07-08
---

# Agent Native Software

Agent-native software is software whose core substrate is an agent rather than a traditional app with an AI feature bolted on. In [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]], [[JustinYan]] and [[Zili]] frame [[OpenClaw]] this way: the surrounding code, tools, channels, UI, and [[AISkills]] act as the agent's hands, senses, and work environment, while the agent itself is what makes the product coherent.

[[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]] sharpens the adjacent [[AgenticSoftware]] definition. The hosts argue that simply adding an AI assistant, MCP-style tool access, or skills to existing software is not enough; the deeper change is decomposing products into callable abilities, dynamic interfaces, and human-agent review loops.

[[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]] adds a non-engineer perception shift. [[XuTao]] starts from an ordinary chat surface and only later realizes that the useful part of "小龙虾" is a programmable, layered system doing work behind the conversation. That makes agent-native software legible as a new way to package back-end routines, memory, and scheduled action for people who would not normally describe themselves as software builders.

[[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]] adds [[AirJelly]] as a context-first agent-native case. [[HuangBote]] argues that task execution and orchestration alone can be copied quickly, while the harder product layer is giving the agent senses, memory, timing, and privacy-aware context. This reframes agent-native software as not only "what can the agent do," but "what can the agent know safely and at the right moment."

[[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] adds a packaging-centered view. [[YaGe]] and [[Haoda]] argue that [[OpenClaw]] became legible because it combined [[IMAgentInterfaces]], [[LocalAgentExecution]], memory, skills, and tool feedback into a product users could treat as a trainable assistant rather than a normal app with an AI button.

[[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]] extends the form into [[TokenDrivenSoftware]]. Instead of only treating the agent as a worker behind fixed app screens, the hosts imagine software whose interface, interaction flow, and world behavior are generated at run time from context. This makes [[ModelRoutingCostControl]] and [[AIInferenceCostStructure]] part of product design, because dynamic behavior can become expensive if every generated surface uses the top model.

[[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]] adds the product-prototyping version. [[OpenClaw]] and [[HermesAgent]]-style agents can be configured in IM threads for article triage, translation, todo aggregation, and calendar/reminder synthesis, letting a builder test a product idea through conversation before deciding whether to engineer it as a stable app or skill.

[[141-freda-de-touzi-zhaji-di-2-ji-tokenmaxxing-ba-dianji-sai-jin-zhengqiji-jielisai-bian-lanqiusai-gudu-ren-de-lianjie-lmeczs2jtkze79rkpvm-rc5yw22m]] adds the enterprise-system redesign version. [[Freda]] argues that many AI CRM or ERP products still resemble old software with automation added. The stronger agent-native opportunity is to record previously invisible decision context, make systems persistent and real-time enough for agents, and redesign communication, permissions, memory, and workflow around nonhuman operators.

## Key Claims
- Agent-native software differs from AI-assisted software because removing the agent would remove the product's reason to exist.
- [[AgenticSoftware]] can include agent-native products, but it also describes how existing software may be rebuilt around [[AtomicCapabilityServices]] and agent-facing access.
- The design center shifts from screens and static feature menus toward [[AgentHarness]] choices: tools, permissions, channels, triggers, memory, and feedback loops.
- [[AISkills]] become product surface because they define reusable capabilities and can sometimes be created or refined by the agent itself.
- [[OnDemandApps]] are one possible downstream form: the agent assembles or generates capabilities at the moment of need instead of exposing only prebuilt app functions.
- Agent-native software increases the importance of [[AgentPermissionBoundaries]] because broader action capacity also broadens failure and leakage risk.
- Context capture and memory can be as much a product surface as tools and skills, especially for personal agents that need to act before being prompted.
- Accessibility and entry point can be as important as raw capability: an IM surface plus local runtime can expose existing CLI-agent power to many more users.
- Token-driven interaction broadens agent-native software from task execution into dynamic experience generation, but increases cost, latency, and quality-control requirements.
- Agent-native prototypes can start as configured conversations, but durable products still need stable memory, permission boundaries, and deterministic pieces when repeated work becomes clear.
- For non-technical users, agent-native software can reveal the programmatic structure behind work: chat becomes the surface for routines, state, memory, and tool execution.
- Agent-native enterprise software may need to capture why decisions were made, who objected, what constraints mattered, and which approvals shaped the outcome, not only the final structured record.
- Persistent, real-time systems can matter because agents may need to stay online, react to events, and maintain state rather than operate as one-shot assistants.

## Connections
- [[OpenClaw]] — source example of an agent-native product form.
- [[ShengdongJixi]], [[XuTao]], and [[VibeCoding]] — crossover case where agent-native software becomes visible to non-engineers through workflow prototypes.
- [[AgentHarness]], [[AgenticWorkflow]], and [[AgentFacingInterfaces]] — infrastructure and interface layer that agent-native software depends on.
- [[AISkills]], [[AgentSelfEvolution]], and [[PersistentAgentMemory]] — mechanisms for durable and self-improving capability.
- [[HeadlessSoftware]] — adjacent thesis that software value should be callable by agents rather than trapped in GUI-first flows.
- [[OnDemandApps]] and [[AgentPermissionBoundaries]] — new concepts added by the same source.
- [[AirJelly]], [[IntentContext]], [[OSLevelContext]], and [[ProactiveAgents]] — context-first agent-native case added by the AirJelly source.
- [[IMAgentInterfaces]], [[LocalAgentExecution]], [[YaGe]], and [[Haoda]] — OpenClaw product-mechanics case added by the 20-question episode.
- [[TokenDrivenSoftware]], [[GeneratedWorkInterfaces]], and [[ModelRoutingCostControl]] — Vol. 170's dynamic-interface and cost-control extension.
- [[IMAgentInterfaces]], [[HermesAgent]], [[PersistentAgentMemory]], and [[AISkills]] — configured personal-agent prototype layer added by Vol. 167.
- [[AgenticSoftware]], [[AtomicCapabilityServices]], and [[TencentMeeting]] — Vol. 164's broader software-architecture frame.
- [[AIEconomicDiffusion]], [[AIOrganizationDesign]], and [[AgentPermissionBoundaries]] — episode 141's workflow, team, and infrastructure redesign frame.
