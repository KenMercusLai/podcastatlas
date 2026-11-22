---
title: "Agent Data"
type: concept
tags: [ai, agents, data, workflow]
sources:
  - cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi
  - tech-20260424-0424-mp-tech-pod-128-tech-20260424-0424-mp-tech-pod-128
  - tsr-s4-alexandrwang-v3-tsr-s4-alexandrwang-v3
  - 9492e69c76ab-9492e69c76ab
last_updated: 2026-11-23
knowledge_schema: synthesis-v1
---

## Definition
Agent data is a record of how a person or AI system performs a task across planning, information gathering, constraint checking, tool use, action, feedback, error recovery, evaluation, and completion, rather than only the initial prompt and final answer.

## Current Synthesis
The bounded sources support a narrower claim than “all user activity is valuable training data.” Task trajectories can reveal how capable work is done and can train or evaluate agents that must operate tools over many steps. Their value depends on whether the task, environment, permissions, outcome, and quality signals are legible enough to distinguish useful behavior from noise.

Real traces can capture authentic workflows but carry privacy, consent, employment, surveillance, and compliance risks. Synthetic trajectories can be cleaner and easier to score, but they inherit environment design, verifier, teacher-model, and diversity limits. Ordinary chat history may be less useful when it lacks stable goals and outcomes, yet it is not categorically worthless; different data can support preference learning, safety, evaluation, or product improvement even when it is unsuitable for direct agent training.

## Key Claims
- Agent data is process and outcome data, not merely input-output pairs.
- Coding, computer-use, and vertical workflows can be valuable because tool calls, corrections, and completion criteria are observable.
- Real human workflow traces can improve task realism while creating strong consent, privacy, surveillance, and labor-governance obligations.
- Synthetic agent data shifts leverage toward environment design, verifiers, trace cleaning, and controlled exploration.
- Data value is contextual: noisy chat, expert demonstrations, employee activity, and generated trajectories support different objectives and require different quality tests.
- Human expertise remains important for defining tasks, resolving failure, and judging results where automatic verification is weak.

## Evidence
### Process and expert workflow
- [[tsr-s4-alexandrwang-v3-tsr-s4-alexandrwang-v3]] defines agent data through traces of thinking, gathering information, checking constraints, deciding, and acting in tasks such as travel, contracts, coding, and product work.

### Synthetic environments and improvement loops
- [[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]] says constructed trajectories can be cleaner than ordinary personal history when environments, goals, and scoring are designed, while remaining bounded by cleaning, compliance, and verifier quality.

### Workplace computer-use traces
- [[tech-20260424-0424-mp-tech-pod-128-tech-20260424-0424-mp-tech-pod-128]] reports Meta collecting employee mouse, click, and keystroke activity for computer-use training, illustrating both realistic process data and acute transparency and surveillance risk.

### Chat-versus-agent data allocation
- [[9492e69c76ab-9492e69c76ab]] argues that coding and industry-agent trajectories can be more task-grounded than heterogeneous chat logs because they expose planning, tool use, error correction, and long-horizon execution.

## Counterevidence & Qualifications
The sources do not establish a universal ranking in which agent traces always beat conversation data. Agent trajectories can be unsuccessful, strategically generated, privacy-invasive, biased toward measurable work, or overfit to one harness and environment. Chat records can still support safety analysis, preference learning, customer support, or evaluation after appropriate consent and cleaning. Mouse movements and keystrokes do not reveal intent by themselves, and employer collection creates power asymmetry even when a company promises not to use the data for performance review. Synthetic data can amplify teacher errors or verifier blind spots, while expert demonstrations are expensive and may encode one person's style rather than the best general policy.

## What Changed
- Migrated the page to the synthesis-first schema without removing or reordering its prior evidence inventory.
- Distinguished task-grounded trajectories from heterogeneous chat history without declaring chat data universally worthless.
- Added provider incentives around coding plans, agent SDKs, and harness adoption as a source-scoped data-acquisition hypothesis.
- Made outcome legibility, consent, and verifier quality explicit tests of data value.

## Related Concepts
- [[SyntheticAgentData]] - generated trajectory branch shaped by environments, teachers, and verifiers.
- [[WorkplaceBehaviorTrainingData]] - employee activity branch with heightened consent and surveillance risk.
- [[AIDataInfrastructure]] - systems for collecting, cleaning, governing, and delivering training or evaluation data.
- [[EnvironmentBasedAgentBenchmarks]] - controlled task settings that make action and outcome evaluation possible.
- [[AgentPostTraining]] - model-improvement process that can consume tool-use and task-completion trajectories.
- [[HumanAgentCollaboration]] - source of expert correction, escalation, and judgment inside real workflows.
- [[DataAsEducation]] - interpretation of task traces as teachable sequences rather than static answers.
