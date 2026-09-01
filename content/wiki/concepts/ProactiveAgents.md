---
title: "Proactive Agents"
type: concept
tags: [agents, productivity, product-design]
sources:
  - openclaw-zhihou-wo-zhi-xiang-weilai-3-6-ge-yue-de-shiqing-duitan-sheet0-chuangshiren-wang-wenfeng-lu-d4y7qifag6-rc79tp-roxjp4z
  - 20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto
  - renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o
  - vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1
  - vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1
  - openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6
  - 135-he-ziran-xuanze-chuangshiren-tristan-liao-elys-saibo-fenshen-linghun-context-de-huoqu-yu-liudong-he-ai-shejiao-wangluo-ltwegwvo7grn-v-rft0txlmqmcty
  - zhe-keneng-caishi-ai-peiban-zhenzheng-gai-you-de-yangzi-duitan-shuaping-chanpin-eve-chuangshiren-tristan-lgvcb1tuur-1rf2qk8jv9chmwew
  - wwdc-26-bu-shang-le-ai-dan-li-zhenzheng-de-ai-zhushou-hai-cha-shenme-s10e15-9ab1512e-a4a8-4ea6-81b5-0ac7ec677d2d
  - ep-59-2026-agent-biancheng-xin-qushi-8218230840-466252
last_updated: 2026-09-02
knowledge_schema: synthesis-v1
---

# Proactive Agents

## Definition
Proactive agents are agents that help before the user fully specifies a task, using timing, context, memory, tools, and permission rules to decide when initiative is useful.

## Current Synthesis
The wiki now treats proactivity as a spectrum rather than a single feature. At the low end, agents run scheduled check-ins, reminders, daily summaries, or periodic scans. In the middle, they use OS context, intent context, persistent memory, and current work state to suggest meeting prep, autocomplete, task continuation, or companion messages. At the high end, they prepare new work, set up other agents, pre-interact socially, or open a PR after the human confirms a maintenance suggestion.

The common constraint is timing plus permission. A proactive agent creates value only when it knows enough about the user's situation to act at the right moment and has clear boundaries on what it may do without approval.

## Key Claims
- Proactivity is useful only when grounded in context; otherwise it becomes interruption, spam, or generic notification.
- Time scale matters: autocomplete, scheduled reminders, meeting prep, code-maintenance scans, and autonomous exploratory work need different interfaces and approval gates.
- Persistent memory and OS or workspace context make proactive behavior less random because the agent can connect current state to prior goals and relationships.
- Personal, social, wearable, and coding proactivity have different risk surfaces, but all require explicit permission and responsibility design.
- Code-maintenance proactivity is emerging as a concrete branch: agents can scan repositories, surface TODOs or performance bottlenecks, email suggestions, and create PRs after confirmation.
- Strong proactivity may require meta-agent behavior, where one agent identifies what specialized work should be prepared and where the human must approve escalation.

## Evidence
- OS-level and persistent-memory cases show proactivity through meeting prep, autocomplete, daily summaries, recruiting support, and product-strategy reminders: [[renlei-he-ai-agent-de-zuijia-peihe-fangshi-hai-mei-bei-faming-duitan-paperboy-ltgxurpseowqggfvgc32aurymt-o]].
- OpenClaw-related sources show weak-to-strong proactivity through scheduled prompts, reminders, smart-home actions, social monitoring, and agent setup for exploratory work: [[openclaw-zhihou-wo-zhi-xiang-weilai-3-6-ge-yue-de-shiqing-duitan-sheet0-chuangshiren-wang-wenfeng-lu-d4y7qifag6-rc79tp-roxjp4z]], [[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]], [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]], [[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]].
- AirJelly's stricter framing makes useful proactivity depend on current intent and surrounding OS context, not just background scanning: [[openclaw-zhihou-shui-jiang-dingyi-zhudongshi-ai-de-xin-zhanchang-duitan-airjelly-huang-bote-lplswo8r829akxwgyurfkojelku6]].
- AI-social, companion, and wearable sources show that proactive timing must respect social norms, emotional presence, and physical context: [[135-he-ziran-xuanze-chuangshiren-tristan-liao-elys-saibo-fenshen-linghun-context-de-huoqu-yu-liudong-he-ai-shejiao-wangluo-ltwegwvo7grn-v-rft0txlmqmcty]], [[zhe-keneng-caishi-ai-peiban-zhenzheng-gai-you-de-yangzi-duitan-shuaping-chanpin-eve-chuangshiren-tristan-lgvcb1tuur-1rf2qk8jv9chmwew]], [[wwdc-26-bu-shang-le-ai-dan-li-zhenzheng-de-ai-zhushou-hai-cha-shenme-s10e15-9ab1512e-a4a8-4ea6-81b5-0ac7ec677d2d]].
- Coding-agent proactivity adds a maintenance workflow where repository scans turn into suggestions and optional PRs rather than waiting for a detailed user prompt: [[ep-59-2026-agent-biancheng-xin-qushi-8218230840-466252]].

## Counterevidence & Qualifications
The main counterpressure is attention cost. A proactive agent with weak timing, excessive permissions, or poor taste can create more cognitive load than value. Social and companion proactivity can cross norms around authenticity and care; enterprise and coding proactivity can cross data, security, or production-change boundaries. Human review remains necessary when the agent acts on priorities, people, code, money, or business decisions.

## What Changed
- Code-maintenance agents are now part of the proactive-agent synthesis, not a separate coding-tool footnote.
- The synthesis now separates scheduled wakeups, context-aware suggestions, and high-permission action into different levels of initiative.
- Verification and permission gates are now treated as core requirements for proactive coding agents.

## Related Concepts
- [[ContextEngineering]] - grounding layer that decides whether a suggestion is timely or generic.
- [[PersistentAgentMemory]] - memory mechanism that lets proactive suggestions reference older goals and events.
- [[AgentPermissionBoundaries]] - control layer for what the agent may do before explicit approval.
- [[IMAgentInterfaces]] - communication surface where proactive messages often appear.
- [[AICoworkers]] - collaborator framing for agents that take initiative inside work.
- [[TeamAgentMemory]] - shared context layer that can make team-facing proactive agents less redundant.
- [[AICodingVerification]] - acceptance layer needed before proactive code changes can be trusted.
- [[JuiceCodingAgent]] - concrete coding-agent example for proactive maintenance suggestions and PR creation.
