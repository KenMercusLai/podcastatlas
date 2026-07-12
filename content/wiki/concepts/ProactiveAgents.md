---
title: "Proactive Agents"
type: concept
tags: [agents, productivity, product-design]
sources: [20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto, renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o, vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1, vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1, openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6, 135-he-ziran-xuanze-chuangshiren-tristan-liao-elys-saibo-fenshen-linghun-context-de-huoqu-yu-liudong-he-ai-shejiao-wangluo-ltwegwvo7grn-v-rft0txlmqmcty, zhe-keneng-caishi-ai-peiban-zhenzheng-gai-you-de-yangzi-duitan-shuaping-chanpin-eve-chuangshiren-tristan-lgvcb1tuur-1rf2qk8jv9chmwew, wwdc-26-bu-shang-le-ai-dan-li-zhenzheng-de-ai-zhushou-hai-cha-shenme-s10e15-9ab1512e-a4a8-4ea6-81b5-0ac7ec677d2d]
last_updated: 2026-07-12
---

# Proactive Agents

Proactive agents are agents that help before the user fully specifies a task. In [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]], [[Paperboy]] presents proactivity as a result of [[OSLevelContext]] and [[PersistentAgentMemory]]: the agent can notice an upcoming meeting, infer what autocomplete would help, summarize daily efficiency, suggest candidate research, or connect recent research to product strategy.

[[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] adds a personal-life version through [[JustinYan]]'s [[OpenClaw]]-inspired agent: scheduled English prompts, repeated reminders, evening follow-ups, random surprises, personal questions, health-data reports, and multimodal input all show how proactivity can become a relationship and habit design problem.

[[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]] adds [[WangJunyu]]'s implementation-level simplification: proactivity can begin with a crude scheduled wakeup, such as an agent checking in every thirty minutes. The value is not the timer itself, but the combination of wakeup, memory, tools, and feedback that lets the agent notice or continue work.

[[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]] adds [[AirJelly]]'s stricter definition. [[HuangBote]] says broad proactive AI can include reminders, scheduled tasks, and periodic scanning, but useful proactive agents need both [[IntentContext]] and surrounding [[OSLevelContext]]. AirJelly's desired behavior is to continue the user's current task at the right moment, not to expand into loosely related information that increases cognitive load.

[[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] adds a task-scheduling and social-presence version through [[OpenClaw]]. The episode describes smart-home schedules, community bots, meeting reminders, and social monitoring as places where an agent's initiative matters, while also noting that automatic likes, comments, or high-permission actions can become unwelcome without clear boundaries.

[[135-he-ziran-xuanze-chuangshiren-tristan-liao-elys-saibo-fenshen-linghun-context-de-huoqu-yu-liudong-he-ai-shejiao-wangluo-ltwegwvo7grn-v-rft0txlmqmcty]] adds [[Elys]] as an AI-social-network case. [[Tristan]] argues that the main interaction change in AI products is proactivity: [[CyberAvatars]] should face the social world on the user's behalf, pre-interact with other avatars, and bring back connections that are worth the user's attention.

[[zhe-keneng-caishi-ai-peiban-zhenzheng-gai-you-de-yangzi-duitan-shuaping-chanpin-eve-chuangshiren-tristan-lgvcb1tuur-1rf2qk8jv9chmwew]] adds [[EVE]] as a companion case. Proactivity here is not task execution or social matching, but relationship presence: the AI can send voice messages, call the user, bring up recent events, push timely memes, or ask about a goal from months earlier when [[AICompanionActiveMemory]] makes the moment relevant.

[[wwdc-26-bu-shang-le-ai-dan-li-zhenzheng-de-ai-zhushou-hai-cha-shenme-s10e15-9ab1512e-a4a8-4ea6-81b5-0ac7ec677d2d]] adds a wearable-assistant case. [[DongHongguang]] argues that useful proactive help often depends on the assistant being physically available before the user takes out a phone: reminding, ordering, explaining, or watching context in moments such as riding, visiting a museum, or handling a small life task.

## Key Claims
- Proactivity is only useful when it is grounded in context; otherwise it risks becoming interruption or generic notification.
- The product must calibrate how much initiative to take, from subtle autocomplete to explicit meeting-prep prompts to longer-horizon research help.
- Proactive behavior depends on permission and responsibility design because the agent may act around sensitive work relationships and organizational information.
- The source treats proactivity as different across time scales: second-level text completion is clearer than multi-hour autonomous work, where the right interface is still uncertain.
- Proactive agents still require human review, especially when they make judgments about sharing, priorities, recruiting, or business decisions.
- Personal proactivity must balance surprise and control: useful prompts can become interruptions or unsafe action if the agent has too much permission.
- Timing is part of the product: user work state, app switching, dismissal, and task progress should change when the agent appears.
- Social proactivity needs extra caution because an agent acting inside human communities can quickly cross norms around authenticity, attention, and spam.
- Scheduled wakeups are a minimal proactivity mechanism, but they become useful only when tied to durable memory, tools, and permissions.
- In social products, proactivity must be judged by whether it improves real human connection rather than merely creating more automated comments or messages.
- In companion products, proactivity must be judged by whether it feels like care and shared life rather than interruption or generic notification.
- In wearable products, proactivity must be judged by timing and physical context: the assistant should appear because the user's situation makes action easier now, not because a background process wants attention.

## Connections
- [[HumanAgentCollaboration]] — collaboration improves when the agent can anticipate needs without demanding full prompts.
- [[AgenticWorkflow]] — proactive assistance is one way agents enter real workflows.
- [[ContextEngineering]] — determines whether proactive suggestions are grounded enough to be useful.
- [[HumanJudgmentUnderAI]] — humans retain responsibility for decisions, escalation, and taste.
- [[OpenClaw]] and [[AgentPermissionBoundaries]] — personal-agent case where proactive behavior needs explicit safety limits.
- [[WangJunyu]], [[PersistentAgentMemory]], and [[AISkills]] — Vol. 165's simple wakeup plus trainable-method interpretation.
- [[AirJelly]], [[IntentContext]], and [[OSLevelContext]] — AirJelly case where proactivity is grounded in explicit intent and screen/task context.
- [[IMAgentInterfaces]], [[LocalAgentExecution]], [[YaGe]], and [[Haoda]] — OpenClaw examples of scheduled tasks, social bots, and user-tolerated initiative.
- [[Elys]], [[AISocialNetworks]], [[CyberAvatars]], and [[ContextFlywheel]] — social-network case where proactive avatars do pre-interaction work.
- [[EVE]], [[AICompanionActiveMemory]], and [[AIFriendProducts]] — companion case where proactive behavior expresses memory, timing, and relationship state.
- [[WearableAIAssistant]], [[GuangfanTechnology]], and [[OSLevelContext]] — S10E15's always-on physical-context case.
