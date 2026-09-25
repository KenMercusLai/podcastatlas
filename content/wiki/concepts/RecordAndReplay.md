---
title: "Record and Replay"
type: concept
tags: [computer-use, agents, workflow-automation]
sources:
  - ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1
  - vol-175-gpt-6-astra-opus-5-5-jev-zhu-moxing-hunzhan-1-6700-1
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

# Record and Replay

## Definition
Record and replay is a computer-use pattern in which a human demonstrates a GUI workflow and an agent converts the trace into a repeatable skill, reducing the need to rediscover every action from scratch.

## Current Synthesis
The first source describes an [[OpenAI]] mechanism that records human computer work and turns it into repeatable skills, analogous to teleoperation data for robots. Vol. 175 adds direct practitioner experience: demonstrating a web task and asking [[Codex]] to repeat it was faster than making the model reason independently at every step. Together they support a hybrid view: demonstrations can transfer tacit workflow knowledge and reduce search cost, but the resulting routine still needs interface-change detection, permissions, validation, and recovery.

## Key Claims
- Human demonstrations can transfer tacit GUI sequences into agent-readable routines.
- Reusing a demonstrated path can be faster and cheaper than open-ended visual reasoning at every step.
- Record and replay is more structured than free-form clicking but less flexible than a fully general computer-use agent.
- Repeatability depends on stable interfaces, bounded tasks, credential handling, and recovery from changed screens.
- Consequential replay still requires permission checks, verification, stopping rules, and rollback.

## Evidence
- Mechanism and constraints: [[ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1]] describes recording a human GUI workflow into a skill while flagging accuracy, latency, privacy, and permissions.
- Practitioner corroboration: [[vol-175-gpt-6-astra-opus-5-5-jev-zhu-moxing-hunzhan-1-6700-1]] reports that demonstrating a web workflow before Codex repeated it was more efficient than step-by-step autonomous judgment.

## Counterevidence & Qualifications
Neither source provides controlled success rates, cost comparisons, interface-change tests, or evidence across high-stakes domains. A recorded path can fail silently when page structure, account state, localization, or permissions change. Demonstration reduces planning burden but does not establish that the intended action is safe or still appropriate.

## What Changed
- Added hands-on corroboration that demonstration-first computer use can reduce repeated reasoning and improve efficiency.
- Migrated the page to the synthesis-first schema while preserving its complete evidence inventory.

## Related Concepts
- [[ComputerUseAgent]] - broader category for agents operating graphical interfaces.
- [[AgentTrajectoryDistillation]] - learning relationship between recorded behavior and reusable action patterns.
- [[AgentHarness]] - execution layer for validation, retries, and recovery.
- [[AgentPermissionBoundaries]] - authority constraints for replayed actions.
- [[AICodingVerification]] - verification relationship when demonstrations affect code or production systems.
