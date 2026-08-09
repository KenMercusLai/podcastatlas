---
title: "Agent Approval Fatigue"
type: concept
tags: [ai, agents, permissions, governance]
sources: [moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk]
last_updated: 2026-08-10
---

# Agent Approval Fatigue

Agent approval fatigue is the source's practical name for what happens when users or teams have to approve too many small agent actions. In [[moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk]], [[Koji]] describes becoming more willing to let an agent access Gmail as trust increases, while [[DaiGuanlan|戴冠兰]] argues that permissions should often be granted only for a specific task and revoked after completion.

The concept extends [[AgentPermissionBoundaries]] by adding the human-behavior failure mode. If every email read, credential access, file edit, or API call requires approval, the agent becomes too slow to be useful. If the user responds by granting broad standing authority, the blast radius expands. A good [[AgentRuntimeExecutionLayer]] therefore needs temporary scopes, audit trails, risk-tiered actions, and escalation rules that reduce interruptions without turning convenience into unmanaged authority.

## Key Claims
- Approval fatigue is not just a UX issue; it changes the security boundary because tired users may approve too much or disable prompts entirely.
- Task-scoped temporary permissions can preserve agent momentum while limiting standing access.
- Review prompts should distinguish safe observation, low-impact execution, credential use, customer-data access, money movement, and irreversible actions.
- Auditability matters after approval because users and organizations need to reconstruct what the agent did when permission was granted.
- Enterprise systems need to design for changing trust levels: an agent may earn more autonomy in a narrow workflow without earning broad authority over unrelated systems.

## Connections
- [[AgentPermissionBoundaries]] — broader authority and blast-radius frame.
- [[EnterpriseAgentGovernance]] — organization-level review and audit context.
- [[AgentRuntimeExecutionLayer]] — infrastructure layer that can enforce temporary scopes and logs.
- [[AgentIdentityAndAuthentication]] — attribution layer for deciding which actor took an approved action.
- [[AgentSpendControls]] — payment and budget form of approval scoping.
- [[HumanJudgmentUnderAI]] — human responsibility boundary that approval prompts are supposed to preserve.
