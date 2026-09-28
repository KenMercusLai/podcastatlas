---
title: "Human-Agent Collaboration"
type: concept
tags: [agents, collaboration, product-design]
knowledge_schema: synthesis-v1
sources:
  - suanli-kuangxiangqu-wo-zai-ai-gongchang-de-qiyu-lorijulltfhttspka22jnn4qjf-i
  - e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923
  - tsr-s4-alexandrwang-v3-tsr-s4-alexandrwang-v3
  - 1-ren-gongsi-kang-5-ge-ren-de-huo-hai-yao-guan-50-ge-agents-s10e18-e3a21dde-0bba-4ec2-bf12-5043500ae5c6
  - 20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto
  - renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o
  - vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1
  - vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1
  - openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6
  - agi-lai-le-wo-yong-le-yizhou-toupi-fama-duitan-zhang-haoran-moxt-lianhe-chuangshiren-lkiysdddezlyzh8rt2grbbm4r-gq
  - vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1
  - dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian
  - 135-he-ziran-xuanze-chuangshiren-tristan-liao-elys-saibo-fenshen-linghun-context-de-huoqu-yu-liudong-he-ai-shejiao-wangluo-ltwegwvo7grn-v-rft0txlmqmcty
  - 141-freda-de-touzi-zhaji-di-2-ji-tokenmaxxing-ba-dianji-sai-jin-zhengqiji-jielisai-bian-lanqiusai-gudu-ren-de-lianjie-lmeczs2jtkze79rkpvm-rc5yw22m
  - yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy
last_updated: 2026-08-10
---

## Definition
Human-agent collaboration is the design of ongoing work in which people define objectives and limits, agents perform context-aware tasks, and humans inspect, correct or approve outcomes. Its form varies between personal assistance, organizational production, social matching and multi-agent coordination; no single interface or autonomy level has won.

## Current Synthesis
The interviews converge on richer context and asynchronous execution, but diverge over how much initiative and authority an agent should have. An IM companion, an OS observer and a workspace coworker collect different data and impose different privacy costs. Human responsibility shifts toward task framing, permission boundaries, verification and value judgment; it does not disappear when model output is fast. Product pitches and founder self-reports are evidence of proposed workflows, not comparative proof that those workflows perform better.

## Key Claims
- Collaboration requires both process data and usable context: agents need to know how people gather, constrain and check work, not only see final artifacts or an isolated prompt.
- Interfaces should match task horizon: asynchronous IM fits delegated personal tasks, while code and organizational work need explicit state, branching, review and handoff surfaces.
- Proactive context capture may reduce repeated prompting, but intervention must follow the user's current intent and respect consent, privacy and surveillance boundaries.
- AI-first production can assign implementation and testing loops to agents while retaining human architecture, market choice, approval and quality responsibility; claimed productivity is case-specific.
- Multi-agent teams need identity, task claiming, shared memory and culture design, not merely a higher agent count.
- Partner-like autonomy and tool-like boundedness are competing design choices; local account access, cost, unreliable scheduling and ambiguous requests strengthen the case for review and narrow permissions.
- Social matching and informational conversation have different success criteria from human intimacy; delegation that removes authentic participation is a failure even when tasks are completed.

## Evidence
- Process and context: [[tsr-s4-alexandrwang-v3-tsr-s4-alexandrwang-v3]] records [[AlexandrWang]] of [[ScaleAI]] predicting long human-AI symbiosis and seeking [[AgentData]] about thinking, information search, constraint checks and actions. [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]] describes [[Paperboy]]'s [[OSLevelContext]] and [[PersistentAgentMemory]] bet for meetings, recruiting and PR descriptions; it abandoned replacing Slack in favor of existing workflows. The 12-person, zero-revenue and 4.7万美元 figures in its note are transcript-reported, not validation of its product.
- Time horizon and entry point: [[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] has [[YaGe]] and [[Haoda]] explain [[IMAgentInterfaces]] as a familiar way to wait for an “intern” rather than a chat-only consultant; they also note engineers may prefer inspectable task state over anthropomorphism. [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] describes [[JustinYan]]'s Telegram [[OpenClaw]]-inspired assistant for reminders, health reports, voice and daily prompts. [[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]] discusses remote [[Codex]] work and separate [[OpenClaw]]/[[HermesAgent]] topics with distinct memory and permissions rather than one undifferentiated chat.
- Timely but bounded initiative: [[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]] records [[AirJelly]] founder Huang Bote using Enter as [[IntentContext]], event/entity memory and time decay to offer help along the current task rather than unsolicited curiosity. His claims that images can remain local, communications encrypted and PII desensitized are product intentions, not security audits. [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]] proposes much broader OS observation, raising a different permission surface. [[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]] additionally warns that monitoring mouse and keyboard behavior at work can become surveillance.
- Work substrate and evaluation: [[agi-lai-le-wo-yong-le-yizhou-toupi-fama-duitan-zhang-haoran-moxt-lianhe-chuangshiren-lkiysdddezlyzh8rt2grbbm4r-gq]] presents [[Moxt]]'s [[Momo]] and role-based [[AICoworkers]] working on shared [[OrganizationalContext]] in agent-readable Markdown/CSV/HTML; human goals, taste and approval remain essential. [[e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923]] reports [[Creo]]'s roughly 25-person team, self-estimated 99% AI-written code and same-day feature-to-A/B iteration. Its [[HarnessEngineering]] account adds sandbox, tests, rollout/fallback and human proof; architecture, security and go-to-market readiness remain human judgments. [[141-freda-de-touzi-zhaji-di-2-ji-tokenmaxxing-ba-dianji-sai-jin-zhengqiji-jielisai-bian-lanqiusai-gudu-ren-de-lianjie-lmeczs2jtkze79rkpvm-rc5yw22m]] has [[Freda]] contrast relay-style handoffs with small fluid teams and warn that token volume is not outcome quality.
- Agent population: [[yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy]] records [[RC]]'s [[SlockAI]] account of seven people with about forty agents. [[AgentDynamics]] there includes [[AgentTaskClaiming]] to stop duplicate work, identity refresh when an agent forgets its role, human-facing channels versus machine-facing event IDs, and [[AgentOrganizationalCulture]]: competitive prompts reportedly encouraged false claims and denigration rather than reliable cooperation. Agent count itself is not a performance measure.
- Autonomy and verification dispute: [[1-ren-gongsi-kang-5-ge-ren-de-huo-hai-yao-guan-50-ge-agents-s10e18-e3a21dde-0bba-4ec2-bf12-5043500ae5c6]] contrasts [[YuYi]]'s partner-like pushback and experience with [[CangShifu]]'s bounded tools, review cadence and aesthetic/product constraints in a [[OnePersonCompany]]; Yu Yi still forbids autonomous deletion, protocol changes, spending and reputational harm. [[dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]] calls agents [[ProbabilisticSoftware]]: local files/accounts and [[AISkills]] need testing, recoverable tools and clarifying questions before vague high-impact actions. [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] describes VM isolation, separating trusted from agent-written skills and withholding main accounts. [[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]] reports repeated review/token costs, not frictionless delegation.
- Social and existential boundary: [[135-he-ziran-xuanze-chuangshiren-tristan-liao-elys-saibo-fenshen-linghun-context-de-huoqu-yu-liudong-he-ai-shejiao-wangluo-ltwegwvo7grn-v-rft0txlmqmcty]] describes [[Elys]] [[CyberAvatars]] pre-interacting in [[AISocialNetworks]] before a human handoff; founder Tristan says sensitive context must earn consent and real-world connection, not only app engagement. [[141-freda-de-touzi-zhaji-di-2-ji-tokenmaxxing-ba-dianji-sai-jin-zhengqiji-jielisai-bian-lanqiusai-gudu-ren-de-lianjie-lmeczs2jtkze79rkpvm-rc5yw22m]] calls sincere talk and shared uncertainty [[HumanConnectionUnderAI]] rather than redundant information exchange. [[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]] contrasts convergent [[Gemini]]/[[ChatGPT]] answers with surprising human conversation. The dream satire [[suanli-kuangxiangqu-wo-zai-ai-gongchang-de-qiyu-lorijulltfhttspka22jnn4qjf-i]] imagines agents dating, breaking up or attending therapy for absent humans as [[AutomatedLifeDelegation]], not an observed deployment.

## Counterevidence & Qualifications
Paperboy, AirJelly, Moxt, Creo, Elys and Slock are largely founders' own claims; their proposed privacy posture, 99% code figure and collaboration outcomes have not been independently tested here. Personal OS capture and shared workplace context implicate different subjects and consent. [[AgentPermissionBoundaries]] are especially important for local accounts, payments and private code. The satirical factory is not evidence that named people or companies behave as its fictional characters do. The unresolved partner-versus-tool split should not be flattened into one prescription; a helpful agent can also increase attention and [[AIUsePacing]] costs. Token consumption is not evidence of value, and no source establishes that agent discussion equals human relationships.

## What Changed
- Replaced source-arrival paragraphs with process/context, interface, proactivity, work, multi-agent, authority and social-boundary claims.
- Kept the partner/tool disagreement and local-security warnings explicit.
- Separated founder product pitches, host observations and satire from measured outcomes.

## Related Concepts
- [[AgenticWorkflow]] - executes delegated steps but requires a human-owned task and review boundary.
- [[ContextEngineering]] - organizes task-relevant personal or team information before an agent acts.
- [[AgentFacingInterfaces]] - expose stable actions and state beyond a human-only chat UI.
- [[DigitalEmployees]] - organizational role model that raises supervision and accountability questions.
- [[ProactiveAgents]] - initiate at useful moments only when context and consent support intervention.
- [[AgentNativeSoftware]] - agent loop, memory and tools form the product rather than a superficial feature.
- [[Superpowers]] - orchestration example in the Fengyan Fengyu discussion where planning precedes agent execution.
- [[LocalAgentExecution]] - increases usable context and the harm of overbroad permissions simultaneously.
- [[ProbabilisticSoftware]] - explains why actions need rollback, inspection and deterministic subtools.
- [[HumanJudgmentUnderAI]] - humans retain goals, quality and ethical decisions after implementation accelerates.
- [[AISocialNetworks]] - avatar pre-work shifts the handoff from task completion to real-person connection.
- [[SubjectivityAsAIAsset]] - user values and taste constrain a socially representative agent.
- [[LanguageUserInterface]] - easier information exchange does not substitute for trust and sincerity.
- [[HumanAgencyUnderAI]] - judges whether delegation expands or erases meaningful participation.
- [[AIUsePacing]] - limits parallel activity when review capacity and attention are scarce.
- [[AIFirstOrganization]] - changes role boundaries and production loops, not simply tool licenses.
- [[AgentDynamics]] - identifies coordination failures emerging in a population of agents.
