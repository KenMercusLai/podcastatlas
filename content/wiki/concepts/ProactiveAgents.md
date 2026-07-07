---
title: "Proactive Agents"
type: concept
tags: [agents, productivity, product-design]
sources: [20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto, renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o, vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1, vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1, openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]
last_updated: 2026-07-07
---

# Proactive Agents

Proactive agents are agents that help before the user fully specifies a task. In [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]], [[Paperboy]] presents proactivity as a result of [[OSLevelContext]] and [[PersistentAgentMemory]]: the agent can notice an upcoming meeting, infer what autocomplete would help, summarize daily efficiency, suggest candidate research, or connect recent research to product strategy.

[[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] adds a personal-life version through [[JustinYan]]'s [[OpenClaw]]-inspired agent: scheduled English prompts, repeated reminders, evening follow-ups, random surprises, personal questions, health-data reports, and multimodal input all show how proactivity can become a relationship and habit design problem.

[[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]] adds [[WangJunyu]]'s implementation-level simplification: proactivity can begin with a crude scheduled wakeup, such as an agent checking in every thirty minutes. The value is not the timer itself, but the combination of wakeup, memory, tools, and feedback that lets the agent notice or continue work.

[[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]] adds [[AirJelly]]'s stricter definition. [[HuangBote]] says broad proactive AI can include reminders, scheduled tasks, and periodic scanning, but useful proactive agents need both [[IntentContext]] and surrounding [[OSLevelContext]]. AirJelly's desired behavior is to continue the user's current task at the right moment, not to expand into loosely related information that increases cognitive load.

[[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] adds a task-scheduling and social-presence version through [[OpenClaw]]. The episode describes smart-home schedules, community bots, meeting reminders, and social monitoring as places where an agent's initiative matters, while also noting that automatic likes, comments, or high-permission actions can become unwelcome without clear boundaries.

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

## Connections
- [[HumanAgentCollaboration]] — collaboration improves when the agent can anticipate needs without demanding full prompts.
- [[AgenticWorkflow]] — proactive assistance is one way agents enter real workflows.
- [[ContextEngineering]] — determines whether proactive suggestions are grounded enough to be useful.
- [[HumanJudgmentUnderAI]] — humans retain responsibility for decisions, escalation, and taste.
- [[OpenClaw]] and [[AgentPermissionBoundaries]] — personal-agent case where proactive behavior needs explicit safety limits.
- [[WangJunyu]], [[PersistentAgentMemory]], and [[AISkills]] — Vol. 165's simple wakeup plus trainable-method interpretation.
- [[AirJelly]], [[IntentContext]], and [[OSLevelContext]] — AirJelly case where proactivity is grounded in explicit intent and screen/task context.
- [[IMAgentInterfaces]], [[LocalAgentExecution]], [[YaGe]], and [[Haoda]] — OpenClaw examples of scheduled tasks, social bots, and user-tolerated initiative.
