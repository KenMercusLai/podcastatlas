---
title: "Proactive Agents"
type: concept
tags: [agents, productivity, product-design]
sources: [renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o, vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1, openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]
last_updated: 2026-07-07
---

# Proactive Agents

Proactive agents are agents that help before the user fully specifies a task. In [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]], [[Paperboy]] presents proactivity as a result of [[OSLevelContext]] and [[PersistentAgentMemory]]: the agent can notice an upcoming meeting, infer what autocomplete would help, summarize daily efficiency, suggest candidate research, or connect recent research to product strategy.

[[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] adds a personal-life version through [[JustinYan]]'s [[OpenClaw]]-inspired agent: scheduled English prompts, repeated reminders, evening follow-ups, random surprises, personal questions, health-data reports, and multimodal input all show how proactivity can become a relationship and habit design problem.

[[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]] adds [[AirJelly]]'s stricter definition. [[HuangBote]] says broad proactive AI can include reminders, scheduled tasks, and periodic scanning, but useful proactive agents need both [[IntentContext]] and surrounding [[OSLevelContext]]. AirJelly's desired behavior is to continue the user's current task at the right moment, not to expand into loosely related information that increases cognitive load.

## Key Claims
- Proactivity is only useful when it is grounded in context; otherwise it risks becoming interruption or generic notification.
- The product must calibrate how much initiative to take, from subtle autocomplete to explicit meeting-prep prompts to longer-horizon research help.
- Proactive behavior depends on permission and responsibility design because the agent may act around sensitive work relationships and organizational information.
- The source treats proactivity as different across time scales: second-level text completion is clearer than multi-hour autonomous work, where the right interface is still uncertain.
- Proactive agents still require human review, especially when they make judgments about sharing, priorities, recruiting, or business decisions.
- Personal proactivity must balance surprise and control: useful prompts can become interruptions or unsafe action if the agent has too much permission.
- Timing is part of the product: user work state, app switching, dismissal, and task progress should change when the agent appears.

## Connections
- [[HumanAgentCollaboration]] — collaboration improves when the agent can anticipate needs without demanding full prompts.
- [[AgenticWorkflow]] — proactive assistance is one way agents enter real workflows.
- [[ContextEngineering]] — determines whether proactive suggestions are grounded enough to be useful.
- [[HumanJudgmentUnderAI]] — humans retain responsibility for decisions, escalation, and taste.
- [[OpenClaw]] and [[AgentPermissionBoundaries]] — personal-agent case where proactive behavior needs explicit safety limits.
- [[AirJelly]], [[IntentContext]], and [[OSLevelContext]] — AirJelly case where proactivity is grounded in explicit intent and screen/task context.
