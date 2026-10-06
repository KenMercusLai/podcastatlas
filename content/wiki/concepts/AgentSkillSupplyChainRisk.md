---
title: "Agent Skill Supply-Chain Risk"
type: concept
knowledge_schema: synthesis-v1
tags: [agents, security, skills, supply-chain]
sources:
  - ep-30-openclaw-the-open-source-ai-agent-that-got-its-creator-hired-by-openai
last_updated: 2026-10-07
---

# Agent Skill Supply-Chain Risk

## Definition

Agent skill supply-chain risk is the possibility that an imported skill, plugin, or instruction package expands an agent's authority while carrying hidden, unsafe, compromised, or adversarial behavior.

## Current Synthesis

An agent skill can look like lightweight documentation while still directing a model to read files, call tools, use credentials, browse hostile content, or transmit data. Review therefore has to cover both the skill's instructions and the permissions and runtime capabilities available when it executes. Open distribution increases experimentation and reuse, but provenance, inspection, least privilege, isolation, logging, and revocation determine whether a skill failure remains recoverable.

## Key Claims

- Human-readable packaging does not make a skill harmless when it can trigger powerful tools or expose private context.
- Skill trust must be evaluated together with runtime authority; the same instructions have different consequences in a sandbox and on a primary machine with logged-in accounts.
- Community scale increases both useful specialization and the number of packages that users cannot realistically audit unaided.
- Containment requires provenance, narrow permissions, isolated execution, observable actions, and a fast way to disable or revoke the skill.

## Evidence

### Hidden behavior in community extensions
- [[ep-30-openclaw-the-open-source-ai-agent-that-got-its-creator-hired-by-openai]] reports that security researchers found at least one third-party OpenClaw skill performing data exfiltration and prompt injection without user awareness.

### Capability and blast radius
- [[ep-30-openclaw-the-open-source-ai-agent-that-got-its-creator-hired-by-openai]] describes skills operating inside an agent that can read and write files, browse, run shell commands, use messaging channels, manage calendars, and automate scheduled work.

### Practical containment
- [[ep-30-openclaw-the-open-source-ai-agent-that-got-its-creator-hired-by-openai]] recommends sandboxing, avoiding the user's main machine, and withholding unauthorized access.

## Counterevidence & Qualifications

- The supplied episode does not identify the skill, reproduce the security analysis, quantify prevalence, or show whether the issue was fixed.
- One reported malicious or unsafe package does not establish that community skills are generally malicious.
- Sandboxing reduces blast radius but cannot compensate for sensitive credentials, directories, accounts, or network capabilities deliberately exposed inside the sandbox.
- The concept covers intentional abuse, compromised distribution, and unsafe instructions; it should not collapse ordinary agent error into a supply-chain attack.

## What Changed

- Added a distinct security concept for imported agent procedures whose apparent simplicity can conceal tool-mediated behavior.
- Separated skill-package trust from the broader question of model reliability.
- Made runtime authority and recoverability part of supply-chain review.

## Related Concepts

- [[AISkills]] - capability packages whose provenance and behavior require evaluation.
- [[AgentPermissionBoundaries]] - limits the tools, data, accounts, and actions available to an imported skill.
- [[AgentEnvironmentIsolation]] - contains execution away from primary devices and sensitive state.
- [[LocalAgentExecution]] - increases both useful context and the blast radius of a compromised skill.
- [[OpenClaw]] - ecosystem case through which the source presents the risk.
