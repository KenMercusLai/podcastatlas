---
title: "Context Engineering"
type: concept
tags: [context, knowledge-management, agents]
sources: [e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb, gaoshou-zenme-yong-ai-putongren-zenme-xue-ai-touziren-ruhe-tou-ai-duitan-kedaibiao-lizheng-ljqyo4tz0o2-pmsl-mjx6umsuzsc, openai-he-anthropic-gongtong-kanhao-de-fde-ai-shidai-de-xin-gangwei-chuxian-jiu-fengong-songdong-duitan-rolling-ai-ljlatrjimrlnbe-luqmat0c74xo6, ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun, community-led-saas-growth-how-ninety-hit-44m-arr, agent-yuannian-di-500-tian-shenme-zai-xiaoshi-shenme-zai-dansheng-weishenme-women-bugai-zai-touzi-gui-siwei-de-ruanjian-lhwdxfpke3bmamjk4e6knk-5sn-b, renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o, tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3, ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan, ai-hui-xie-daima-le-weishenme-ni-haishi-zuo-bu-chu-chanpin-1, openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6, agi-lai-le-wo-yong-le-yizhou-toupi-fama-duitan-zhang-haoran-moxt-lianhe-chuangshiren-lkiysdddezlyzh8rt2grbbm4r-gq, ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz, vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]
last_updated: 2026-07-08
---

# Context Engineering

Context engineering is the practice of accumulating, organizing, and refining the information that helps AI produce useful work. [[gaoshou-zenme-yong-ai-putongren-zenme-xue-ai-touziren-ruhe-tou-ai-duitan-kedaibiao-lizheng-ljqyo4tz0o2-pmsl-mjx6umsuzsc]] argues that as models and tools converge, differentiated performance will come from context: preferences, examples, standards, documents, workflows, and implicit judgment made explicit. [[openai-he-anthropic-gongtong-kanhao-de-fde-ai-shidai-de-xin-gangwei-chuxian-jiu-fengong-songdong-duitan-rolling-ai-ljlatrjimrlnbe-luqmat0c74xo6]] adds the enterprise version: [[DigitalEmployees]] need company processes, frontline knowledge, system access, and expert examples before they can work, so [[ForwardDeployedEngineer]] practice becomes applied context engineering. [[ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun]] adds that context must include operational details such as data migration constraints and the user's own internalized preparation for live situations. [[community-led-saas-growth-how-ninety-hit-44m-arr]] adds an organizational-data example through [[Mas]], which depends on [[Ninety]]'s accumulated context about vision, values, roles, accountability, rocks, metrics, and feedback. [[agent-yuannian-di-500-tian-shenme-zai-xiaoshi-shenme-zai-dansheng-weishenme-women-bugai-zai-touzi-gui-siwei-de-ruanjian-lhwdxfpke3bmamjk4e6knk-5sn-b]] treats context as the unchanged main thread of the first 500 agent-era days. [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]] adds the personal-computing version through [[OSLevelContext]] and [[PersistentAgentMemory]], where the agent learns from the user's actual computer activity instead of relying only on chat history or manually maintained prompt files. [[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]] adds the harness version: context engineering includes working directory state, dependency and git state, system prompts, skills, memory, context compression, and handoff documents for the next agent.

[[ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan]] adds the [[VibeCoding]] version. The source argues that good module boundaries and interface design help keep agent context tractable, and it contrasts [[GeminiCLI]]'s large-context behavior with [[Cursor]]'s likely chunking, indexing, and retrieval approach.

[[ai-hui-xie-daima-le-weishenme-ni-haishi-zuo-bu-chu-chanpin-1]] adds a logging and observability version. The hosts argue that AI debugging improves when the user has asked the system to emit detailed logs, preserve test results, and document old-code behavior; without those traces, AI has too little context to diagnose logic errors that still compile and run.

[[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]] adds the [[AirJelly]] version: context engineering is not only stuffing more material into a model, but deciding when context has enough signal to save. [[IntentContext]], event/entity extraction, memory merging, time decay, retrieval, and local privacy boundaries become product decisions for turning everyday computer activity into agent-usable context.

[[agi-lai-le-wo-yong-le-yizhou-toupi-fama-duitan-zhang-haoran-moxt-lianhe-chuangshiren-lkiysdddezlyzh8rt2grbbm4r-gq]] adds the [[Moxt]] version: context engineering becomes workspace design. [[ZhangHaoran]] argues that documents, meeting recordings, data definitions, project status, code changes, and comments need to live as [[OrganizationalContext]] in AI-readable formats before [[AICoworkers]] can work with less repeated briefing.

[[ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz]] adds the skill-curation version. Requirement-grilling, architecture maps, project-local skills, podcast transcripts, [[WeChatReading]] notes, and repeated operations tasks all become context assets when they are written down clearly enough for agents to reuse.

[[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]] adds a limit case: more context and project memory help, but stale or compressed context can rot, and agents should sometimes challenge the user's request instead of faithfully executing a weak premise.

[[e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb]] adds the personal external-brain version. [[PingGe]] frames the context window as a scarce working-memory resource, so durable material should live in markdown files, prior writing, transcripts, notes, and indexed folders that can be pulled in only when relevant. The episode also stresses that context is not only documents; it includes why the task exists, who the user is, what output they can accept, and which parts of their taste or "soul" should guide the agent.

## Role In The Sources
- [[KedaibiaoLizheng]] treats context as a personal, team, and company advantage.
- [[AISkills]] are one way to package context into reusable procedures.
- [[AgenticWorkflow]] tools can use context more effectively than isolated chat sessions.
- [[AIAssistedSoftwareDevelopmentRisk]] shows that missing context around production state can cause real user harm.
- [[HumanJudgmentUnderAI]] shows that useful context must eventually become human understanding, not only model input.
- [[Mas]] shows context as a SaaS product asset when organizational operating data becomes queryable by AI.
- [[RollingAI]] shows context as a deployment asset when AI must learn from strong frontline workers and existing systems.
- [[Paperboy]] shows context as a personal-agent asset when OS activity, meetings, messages, code, and current app state become durable memory.
- [[ClaudeCode]] shows context as a harness asset when the system decides which tool outputs to discard, what to summarize, and what the next agent must receive.
- [[GeminiCLI]] and [[Cursor]] show context as a coding-product choice between direct long-context loading and engineered retrieval/indexing.
- [[ShengpaiNotice]] shows context as product/workflow knowledge made explicit enough for AI to implement a usable internal tool.
- Detailed logs, tests, screenshots, and documentation become context assets for future AI debugging and refactoring.
- AirJelly shows that the trigger for collecting context can be as important as the context itself; Enter-triggered capture tries to reduce random browsing noise.
- Moxt shows context as workspace infrastructure: Markdown, CSV, JSON, HTML, file structure, meetings, data, and project traces are shaped for agent work.
- EP127 shows context as skill material: repeated prompts, acceptance criteria, design preferences, reading notes, transcripts, and operational procedures can be compressed into reusable agent instructions.
- Vol. 164 shows context as both asset and risk: memory helps only if it preserves the right signal, stays fresh enough, and supports agent pushback.
- E163 shows context as an external-brain habit: personal archives, style files, memory notes, and acceptance criteria become the material from which agents learn the user.

## Connections
- [[ForwardDeployedEngineer]] — enterprise deployment role that must map company context.
- [[DigitalEmployees]] and [[FrontlineAIEnablement]] — enterprise cases where local context determines AI usefulness.
- [[WeChat]] — platform whose potential agent value comes partly from accumulated user and social context.
- [[SubagentWorkflow]] — delegation pattern that depends on passing and recovering task context.
- [[SaaSTrustMoat]] — business defensibility that can come from trusted, accumulated workflow context.
- [[HeadlessSoftware]] — requires enough context for agents to use product capabilities without relying on GUI walkthroughs.
- [[OSLevelContext]], [[PersistentAgentMemory]], and [[ProactiveAgents]] — Paperboy's context layer for personal agents.
- [[AgentHarness]] and [[KComputer]] — execution environment and context layer that agents use to continue work across tools and sessions.
- [[VibeCoding]], [[GeminiCLI]], and [[AICodingVerification]] — coding-context case added by EP108.
- [[AIEngineeringThinking]], [[ShengpaiNotice]], and [[WangDafu]] — logging, workflow, and operations-context case added by the Keji Luandun episode.
- [[AirJelly]], [[IntentContext]], [[OSLevelContext]], and [[PersistentAgentMemory]] — personal-agent context capture and memory case added by the AirJelly episode.
- [[Moxt]], [[AINativeWorkspace]], [[OrganizationalContext]], and [[AICoworkers]] — organization-level context case added by the Moxt episode.
- [[AISkills]], [[RoutineAgentAutomation]], [[Podwise]], and [[WeChatReading]] — skill-curation and personal knowledge cases added by EP127.
- [[PersistentAgentMemory]], [[AICommunicationAbility]], and [[HumanJudgmentUnderAI]] — Vol. 164's context-rot and prompt-quality case.
- [[PingGe]], [[HumanAgencyUnderAI]], [[AIUsePacing]], and [[OutputQualityGates]] — E163's context, identity, and acceptance-standard extension.
