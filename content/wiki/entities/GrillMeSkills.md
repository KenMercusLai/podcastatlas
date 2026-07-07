---
title: "GrillMe Skills"
type: entity
tags: [ai-tool, skills, workflow]
sources: [vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]
last_updated: 2026-07-07
---

# GrillMe Skills

GrillMe Skills are discussed in [[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]] as Matpaco's lighter, manually invoked alternative to an always-on [[Superpowers]] workflow. The hosts describe using this style of skill to ask sharper requirement questions, produce specs or ADRs, write PRDs, decompose issues, and then hand execution to [[Codex]], GLM, or another agent.

The episode's distinction is control. [[Superpowers]] gives a fixed end-to-end process that can help non-experts, while GrillMe-style skills leave the experienced user in charge of when a workflow deserves extra questioning, planning, or review.

## Source Position
- GrillMe Skills are treated as useful because they preserve [[AIEngineeringThinking]] without forcing every task through a large process.
- The hosts say they moved away from automatic Superpowers hooks because manual skill selection reduces token use and keeps small tasks from becoming over-engineered.
- The pattern reinforces the [[AISkills]] rule that a skill is valuable when it encodes a recurring judgment or workflow, not merely because it is fashionable.

## Connections
- [[AISkills]] — broader concept for reusable instructions and workflow assets.
- [[Superpowers]] — heavier orchestration bundle contrasted with GrillMe-style manual control.
- [[AgentHarness]] — runtime and process layer where skills are loaded and invoked.
- [[Fable5]], [[Codex]], and [[AICodingVerification]] — model and verification workflow that the skills support.
