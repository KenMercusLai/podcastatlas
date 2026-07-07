---
title: "Output Quality Gates"
type: concept
tags: [ai, quality, workflow, verification]
sources: [e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb]
last_updated: 2026-07-08
---

# Output Quality Gates

Output quality gates are explicit standards that decide whether AI work is accepted, revised, or rejected. In [[e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb]], [[PingGe]] argues that users need to define what counts as good output, what violates expectation, and which requirements must trigger a redo.

The concept generalizes [[AICodingVerification]] beyond code. In software, gates include compilation, tests, CI, deployment, and runtime checks. For writing, research, operations, design, or personal assistants, gates may include source grounding, tone, completeness, decision usefulness, privacy boundaries, or fit to the user's style and values.

## Key Claims

- AI work improves when the user can say why an output is unacceptable rather than only saying it "feels wrong."
- Gates are reusable context: once written down, they can become part of [[AISkills]], project memory, or review checklists.
- Output standards should include both objective checks and user-specific preferences.
- Clear gates reduce polite but mediocre answers because the agent knows what will be rejected.
- Gates are part of "raising AI": feedback becomes durable only if it changes future acceptance behavior.
- Non-code tasks need gates because they often lack compiler-like signals; the human must specify what equivalent evidence or review looks like.
- Gates also protect [[AIUsePacing]] by letting the user review at boundaries instead of continuously watching the agent.

## Connections

- [[AICodingVerification]] — code-specific version of explicit quality gates.
- [[AISkills]] — gates can be packaged into reusable procedures.
- [[ContextEngineering]] and [[PersistentAgentMemory]] — gates become durable context and preference memory.
- [[HumanJudgmentUnderAI]] — humans remain accountable for whether the gate is meaningful.
- [[AICommunicationAbility]] — acceptance criteria must be communicated clearly.
- [[AgenticWorkflow]] — gates define when an agentic task can proceed, stop, or ask for help.
