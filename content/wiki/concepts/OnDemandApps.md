---
title: "On-Demand Apps"
type: concept
tags: [agents, software-design, personalization]
sources: [vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1, vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1, vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]
last_updated: 2026-07-07
---

# On-Demand Apps

On-demand apps are the source's "现炒 App" idea: software capabilities are assembled, generated, or combined when the user needs them rather than fully prewritten as fixed application features. In [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]], [[JustinYan]] uses his personal [[OpenClaw]]-like agent to describe how fewer than thirty [[AISkills]] can already combine in surprising ways.

[[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]] extends the idea into [[TokenDrivenSoftware]]. The hosts imagine interfaces, map views, camera effects, NPC behavior, and software flows being generated from the user's current context rather than assembled only from prewritten features. This broadens on-demand apps from tool composition into dynamic product experience.

[[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]] adds a practical user-demand boundary. [[WangJunyu]] imagines simple base interfaces that adapt to different user habits, while [[JustinYan]] and [[XuTao]] note that most people may not want to continuously customize or improve software themselves. The concept therefore depends on making customization feel like the default experience, not a chore.

## Key Claims
- [[AgentNativeSoftware]] can make app behavior more dynamic because the agent can choose tools and skills based on the user's immediate goal.
- The concept depends on [[AgentHarness]] quality: the agent needs tools, channel access, memory, and permissions before it can assemble useful capabilities.
- It benefits from [[VibeCoding]] because small custom apps and connectors can be created quickly for one person's workflow.
- Surprise is both value and risk: unexpected combinations can delight users, but they can also create gray-zone behavior or unreviewed actions.
- The concept pressures traditional SaaS when generic workflows can be generated on demand, while secure, financial, and high-accountability workflows still need strong [[AgentPermissionBoundaries]].
- Dynamic generation increases the need for [[ModelRoutingCostControl]] because always using the strongest model for every generated surface can make the product uneconomical.
- User appetite matters: on-demand apps may work best when they hide customization effort and give people useful defaults rather than asking everyone to become a product designer.

## Connections
- [[OpenClaw]] and [[JustinYan]] — source example and builder context.
- [[AISkills]], [[AgentSelfEvolution]], and [[ProactiveAgents]] — mechanisms that let capabilities emerge and improve over time.
- [[HumanAgentCollaboration]] — product question of how people ask for, review, and live with generated capabilities.
- [[AIInferenceCostStructure]] — economic constraint on always-on or frequently generated app behavior.
- [[TokenDrivenSoftware]], [[GeneratedWorkInterfaces]], and [[Fable5]] — Vol. 170's stronger-model extension from app assembly to generated interaction.
- [[WangJunyu]], [[XuTao]], and [[HumanJudgmentUnderAI]] — Vol. 165's caution that adaptive software still needs defaults, taste, and user willingness.
