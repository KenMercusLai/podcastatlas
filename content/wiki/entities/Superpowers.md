---
title: "Superpowers"
type: entity
tags: [ai-tool, agents, orchestration]
sources: [vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1, ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz, vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]
last_updated: 2026-07-07
---

# Superpowers

Superpowers is discussed in [[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]] as an agent-orchestration tool used with [[ClaudeCode]], [[Codex]], and structured planning documents. The hosts describe a workflow where a user brainstorms, produces design and plan markdown files, and then assigns concrete tasks to coding agents or subagents.

[[ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz]] mentions Superpowers as a hot skill/tool bundle that can be too complex for some users. The contrast strengthens the episode's selection rule: a powerful skill pack is not automatically valuable unless it fits the user's actual workflow and review capacity.

[[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]] sharpens that critique. The hosts say Superpowers is valuable for non-experts because it supplies a full software process, but it can spend too many tokens, over-structure small tasks, and force TDD/review patterns that do not always fit native UI or app work. They contrast it with [[GrillMeSkills]], where an experienced user manually invokes requirement questioning or planning only when needed.

## Source Position
- Superpowers helps turn vague intent into design and execution artifacts before agents start coding.
- The source treats it as useful for bounding long tasks, splitting work, and preserving the main context window.
- Its value comes from process structure as much as raw model capability.
- EP127 adds that orchestration complexity can itself become friction if the user does not know when to apply the bundle.
- Vol. 170 adds the quota side: full-process orchestration can become expensive when paired with a top model such as [[Fable5]].

## Connections
- [[ClaudeCode]] and [[Codex]] — coding agents used in the workflow.
- [[AgentHarness]] and [[SubagentWorkflow]] — orchestration concepts reinforced by the source.
- [[AIEngineeringThinking]] — design and plan documents are part of making agent work verifiable.
- [[VibeCoding]] — broader AI coding practice that Superpowers helps structure.
- [[AISkills]] and [[HumanJudgmentUnderAI]] — EP127's reminder that skill selection and responsibility remain user decisions.
- [[GrillMeSkills]], [[Fable5]], and [[ModelRoutingCostControl]] — lighter skill selection and token-control contrast added by Vol. 170.
