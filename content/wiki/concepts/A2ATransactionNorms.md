---
title: "A2A Transaction Norms / 智能体间交易规范"
type: concept
tags: [agents, commerce, protocols, governance]
sources:
  - waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87
knowledge_schema: synthesis-v1
last_updated: 2026-09-19
---

# A2A Transaction Norms / 智能体间交易规范

## Definition
A2A transaction norms / 智能体间交易规范 are the identity, authority, behavior, messaging, settlement, and recourse rules governing commercial interactions in which one or more agents negotiate or transact without a human at every step.

## Current Synthesis
Agent-to-agent commerce is not only a faster version of an API call. Each machine actor needs a legible principal, credential, permission scope, and rule for when renewed human authorization is required. The interaction also needs shared expectations about acceptable behavior, evidence, fulfillment, error handling, and dispute escalation.

Existing consumer cards and wallet accounts may not map cleanly to machine actors. The source therefore raises permissioned machine credentials, organizational authority, working capital, and high-frequency settlement as possible additional layers, while keeping the implementation route open.

## Key Claims
- Every transacting agent should be attributable to a person or organization and a bounded authority.
- Norms must specify when agents may proceed autonomously and when human authorization is mandatory.
- Capability assessment matters because a valid identity does not prove an agent can fulfill a task safely.
- Shared evidence and recourse rules are needed when agents disagree or execution crosses several intermediaries.
- Machine-speed settlement may require different credentials and operational infrastructure from consumer checkout.

## Evidence
- Behavior-norm evidence: [[waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87]] records Pete Lau's argument that an agent internet needs social-like constraints and explicit authorization rules.
- Identity evidence: [[waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87]] records KYA and agent capability assessment as additions to user and business identity checks.
- Credential evidence: [[waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87]] records Yong Lambert's view that agents may need permissioned credentials, enterprise authority, working capital, and rapid settlement.

## Counterevidence & Qualifications
- The panel disagrees implicitly on emphasis: protocol mechanics may be relatively straightforward, while harness enforcement, ecosystem adoption, and consumer trust are harder.
- Blockchain is presented as a possible substrate, not established as necessary or sufficient.
- The source does not define interoperability, legal liability, jurisdiction, revocation, or standard governance in detail.

## What Changed
- Added an A2A governance concept spanning identity, authority, behavior, capability, settlement, and recourse.

## Related Concepts
- [[AgentIdentityAndAuthentication]] - attribution of each machine actor and its principal.
- [[AgentPermissionBoundaries]] - limits on what each agent may negotiate or execute.
- [[AgentPaymentInfrastructure]] - credential, settlement, and dispute layer.
- [[VerifiableIntent]] - durable mandate passed through the agent chain.
- [[B2BToA2A]] - broader commercial shift from human-operated B2B workflows toward agent-mediated exchange.
