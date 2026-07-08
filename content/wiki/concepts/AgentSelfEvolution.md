---
title: "Agent Self-Evolution"
type: concept
tags: [agents, learning, memory, workflow]
sources: [dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd, vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1, ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz, vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1, e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di, 138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]
last_updated: 2026-07-08
---

# Agent Self-Evolution

Agent self-evolution is the episode's practical frame for agents improving through memory, saved workflows, skills, and model-harness feedback loops. In [[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]], [[HermesAgent]] turns successful work traces into reusable [[AISkills]], while [[MiniMax]] describes model plus harness doing most of a model-development pipeline with humans keeping judgment, taste, and direction.

[[e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]] raises the same theme from workflow memory into [[RecursiveSelfImprovement]]. [[Apodex]] splits self-evolution into pretraining data work, post-training diagnosis and recipe generation, and harness improvement. The source's boundary is that one self-improvement loop is not full recursion: without [[AIVerification]], [[AICodingVerification]], and [[ResearchTaste]], the loop can drift or optimize the wrong proxy.

[[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] adds a smaller personal-agent example. [[JustinYan]] lets his [[OpenClaw]]-inspired agent inspect available services and write new skills for itself, which turns self-evolution from a model-training idea into a local product behavior inside an [[AgentHarness]].

[[ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz]] adds a work-habit version. The hosts argue that skills often emerge from repeated small tasks: when the same email, podcast, testing, deployment, or cost-monitoring workflow returns enough times, the agent or user can turn it into a reusable skill and keep refining it.

[[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]] adds a user-facing interpretation through [[OpenClaw]]. The episode treats self-evolution less as mystical autonomy and more as an agent repeatedly waking, remembering, using feedback, and improving work methods through [[AISkills]].

[[138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]] adds a model-training version through [[LuoFuli]]. She separates future directions into framework self-evolution, agent self-evolution, human-agent co-evolution, and model-agent mutual adaptation, making self-evolution part of [[AgentPostTraining]] and [[ModelHarnessCoEvolution]] rather than only personal workflow memory.

## Key Claims
- The source's self-evolution is closer to engineering feedback than fully autonomous self-improvement.
- [[PersistentAgentMemory]] lets agents preserve what worked, what failed, and what the user prefers.
- [[AISkills]] compress repeated successful workflows into reusable procedures.
- [[ModelHarnessCoEvolution]] turns real task execution, tests, deployments, and feedback into signals for both model and harness improvement.
- Human goals, taste, creativity, and value judgment remain part of the loop rather than disappearing.
- Self-written skills increase the need for [[AgentPermissionBoundaries]] because the agent can expand its own action surface.
- Repeated mundane work is a practical source of agent improvement because it exposes stable steps, tools, and acceptance criteria.
- [[RoutineAgentAutomation]] makes self-evolution visible at the workflow layer: better routines come from observing what keeps recurring and what keeps failing.
- Scheduled wakeups and feedback loops make self-evolution feel practical to ordinary users because the agent can keep revisiting work instead of waiting for a complete prompt each time.
- Model self-evolution is a stronger version of the pattern: the model may help construct its own data, training tasks, tests, and harness rather than only remembering a user workflow.
- Recursive self-improvement needs verification and taste because repeated loops can amplify small errors, weak tests, or shallow objectives.
- Framework self-evolution needs evaluation systems stronger than today's failure-prevention checks; otherwise the framework may optimize local behavior without improving real tasks.

## Connections
- [[HermesAgent]] and [[Tommy]] — source example of memory becoming skills.
- [[MiniMax]], [[Adao]], and [[Zeying]] — model-company context for model plus harness doing more of the training workflow.
- [[PersistentAgentMemory]], [[AISkills]], and [[AgentHarness]] — mechanisms that make the loop practical.
- [[YouyouAgent]] — adjacent agent-native experiment where an agent pursues a long-running goal.
- [[HumanJudgmentUnderAI]] — boundary condition that humans still set goals and evaluate outputs.
- [[OpenClaw]] and [[AgentNativeSoftware]] — personal-agent case where software can add capability to itself.
- [[RoutineAgentAutomation]] and [[AISkills]] — EP127's repeated-work route to skill accumulation.
- [[WangJunyu]], [[OpenClaw]], and [[ProactiveAgents]] — Vol. 165's scheduled, memory-based, trainable-agent interpretation.
- [[Apodex]], [[RecursiveSelfImprovement]], [[DeepResearch]], and [[AIVerification]] — stronger model-training version added by the Silicon Valley 101 source.
- [[LuoFuli]], [[OpenClaw]], [[OpenCloud]], [[AgentPostTraining]], and [[ModelHarnessCoEvolution]] — framework and model mutual-adaptation version added by episode 138.
