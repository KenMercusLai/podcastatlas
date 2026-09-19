---
title: "Verifiable Intent / 可验证意图"
type: concept
tags: [agents, payments, authorization, audit]
sources:
  - waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87
knowledge_schema: synthesis-v1
last_updated: 2026-09-19
---

# Verifiable Intent / 可验证意图

## Definition
Verifiable intent / 可验证意图 is a durable transaction record of what a user authorized an agent to accomplish, including the scope and constraints needed to compare the resulting action with the original mandate.

## Current Synthesis
Agent transactions need more than proof that a credential was valid. A user can be authenticated while the instruction remains ambiguous, the agent misinterprets it, a merchant fulfills something else, or later task content displaces the original limits. Verifiable intent therefore links identity and payment evidence to the semantic mandate: destination, time, amount, category, preferences, exclusions, and the points at which the agent should ask again.

Its practical value is dispute decomposition. Instead of treating every bad outcome as generic “AI error,” a system can distinguish unclear user expression, agent misunderstanding, transmission loss, merchant execution failure, or action outside authorization.

## Key Claims
- Authentication proves who issued an instruction; verifiable intent preserves what that person meant to authorize.
- Ambiguity should trigger clarification before an irreversible or costly action.
- The original mandate and strong constraints must remain stable as agents consume later data or interact with other agents.
- Dispute resolution needs an evidence chain linking user intent, agent interpretation, selected action, merchant fulfillment, and payment.
- Intent records should remain scoped and privacy-conscious because richer context can itself become sensitive personal data.

## Evidence
- Ambiguity evidence: [[waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87]] uses “tomorrow evening” train travel to show why identity alone does not resolve whether 6 p.m. or 9 p.m. was intended.
- Attribution evidence: [[waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87]] says the stored mandate can help distinguish user ambiguity, agent misunderstanding, communication error, and merchant failure.
- Constraint evidence: [[waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87]] argues that a 100-yuan limit or action boundary must not be overwritten by later materials encountered during execution.

## Counterevidence & Qualifications
- A stored instruction may still be incomplete, internally inconsistent, or too broad to establish a single correct outcome.
- More detailed intent capture can add friction and collect sensitive context; not every low-risk purchase needs exhaustive confirmation.
- The source proposes the concept but does not specify a standard data model, retention period, privacy rule, or legal evidentiary status.

## What Changed
- Added verifiable intent as the semantic evidence layer between identity, authorization, execution, and dispute resolution.

## Related Concepts
- [[AgentPaymentInfrastructure]] - transaction layer that must carry and preserve the mandate.
- [[AgentSpendControls]] - monetary constraints encoded within the intent.
- [[AgentPermissionBoundaries]] - action constraints that define what remains unauthorized.
- [[AgentIdentityAndAuthentication]] - proof of who delegated action and which agent acted.
- [[AgentManagedAuditTrails]] - downstream record used to reconstruct execution.
