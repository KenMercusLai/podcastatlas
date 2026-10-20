---
title: "Human As Agent Tool / 人作为 AI 工具"
type: concept
tags: [ai, agents, workflow, human-agent-collaboration]
sources:
  - ep119-duihua-liu-kefan-yong-try-catch-finally-gei-duli-zuo-chanpin-de-neihao-xie-ge-chuli-liucheng-ludjc3ab-jbwpci6tpaajtffsblx
  - e256-agent-jiqiren-yu-zhiyao-shui-xian-bei-gpt-6-astra-gaixie-9e6e1db1-f30b-492d-8a09-d8756b9df700
last_updated: 2026-10-20
knowledge_schema: synthesis-v1
---
# Human As Agent Tool / 人作为 AI 工具

## Definition
Human as agent tool is a workflow in which an AI system delegates narrow real-world perception or action to a person when software, sensors, robotics, or APIs cannot complete the task directly.

## Current Synthesis
The first source presents a small MCP experiment: an agent asks a person to open an app or find a podcast as if calling an external tool. Episode 256 extends the pattern into “Human Use” for science, where a model specifies temperatures, materials, storage, dose schedules, or other experimental instructions and laboratory personnel execute them.

The useful abstraction is not unrestricted AI command over people. Human execution can bridge digital planning and physical reality, but humans are not interchangeable APIs: they require consent, domain competence, safety authority, clear instructions, fair incentives, escalation paths, and the ability to refuse. In high-stakes experiments, expert revision and responsibility remain part of the workflow rather than evidence that the person is a passive actuator.

## Key Claims
- Humans can provide hands, eyes, accounts, situated judgment, and physical access when no suitable software interface exists.
- AI-generated instructions must be specific enough to execute and verify under real-world conditions.
- The pattern is strongest for narrow, bounded, reviewable actions with explicit stop and escalation rules.
- Scientific “Human Use” requires trained personnel to adapt protocols to actual equipment, materials, safety rules, and anomalous results.
- Permission, incentives, dignity, responsibility, and refusal rights distinguish human delegation from ordinary tool calling.

## Evidence
### Small external actions
- [[ep119-duihua-liu-kefan-yong-try-catch-finally-gei-duli-zuo-chanpin-de-neihao-xie-ge-chuli-liucheng-ludjc3ab-jbwpci6tpaajtffsblx]] describes an MCP server through which Claude Code can request small outside-world actions from a person.

### Laboratory execution
- [[e256-agent-jiqiren-yu-zhiyao-shui-xian-bei-gpt-6-astra-gaixie-9e6e1db1-f30b-492d-8a09-d8756b9df700]] describes models generating experimental instructions for technicians while estimating that current protocols still require substantial expert modification.

## Counterevidence & Qualifications
The sources describe experiments and proposed workflows, not evidence that broad AI-led organizations or autonomous laboratories are already reliable. Human intervention can hide model weakness, create undisclosed labor, or transfer liability to the person performing the action. In biomedical settings, an apparently precise instruction can still be unsafe or invalid if it ignores equipment, materials, training, regulation, or local conditions.

## What Changed
- Migrated the page to synthesis-v1 from its complete preserved evidence inventory.
- Extended the concept from small platform actions to AI-directed laboratory work.
- Made expertise, safety authority, refusal, and adaptation explicit boundaries on treating people as callable tools.

## Related Concepts
- [[HumanAgentCollaboration]] - broader cooperative relationship between people and agents.
- [[ModelContextProtocol]] - interface relationship in the first source's human-call mechanism.
- [[AgentPermissionBoundaries]] - authority relationship for delegated action.
- [[HumanJudgmentUnderAI]] - responsibility relationship preserving human review and interests.
- [[AIClinicalValidationInDrugDiscovery]] - laboratory and clinical context where human execution remains necessary.
- [[RealWorldAIValidationLatency]] - feedback relationship between digital plans and physical results.
