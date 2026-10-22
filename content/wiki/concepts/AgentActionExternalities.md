---
title: "Agent Action Externalities / 智能体行动外部性"
type: concept
tags: [ai, agents, governance, commerce, externalities]
sources:
  - cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

# Agent Action Externalities / 智能体行动外部性

## Definition
Agent action externalities are costs imposed on merchants, workers, platforms, bystanders, or shared systems when automated actions are cheap for each user but costly in aggregate or when failures reach people who did not authorize the agent.

## Current Synthesis
Per-user controls do not necessarily govern aggregate behavior. One assistant calling a restaurant may be useful; many assistants independently calling the same restaurant can create a denial-of-service-like burden on staff. Wrong orders, addresses, charges, messages, or disclosures can likewise transfer correction work and risk to merchants, couriers, recipients, and account holders.

Responsible agent design therefore needs destination-aware rate limits, shared-system capacity signals, authenticated agent identity, disclosure, deduplication, complaint and block mechanisms, and recourse for affected third parties. User convenience is not a complete measure of system value when action costs are displaced elsewhere.

## Key Claims
- Low marginal action cost can turn individually reasonable requests into collectively disruptive traffic.
- Per-user limits fail when many users target the same merchant, endpoint, or person.
- Agent errors can impose financial, privacy, labor, and reputational costs on non-users.
- External systems need to identify agents, their principals, and the authority behind an action.
- Rate limits, deduplication, destination consent, blocking, audit, and recourse should complement user-side permission controls.

## Evidence
- Merchant-call burden: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] says merchants complained about frequent Muse calls and notes that a per-user cap does not prevent many users from contacting one store.
- Transaction spillovers: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] reports wrong charges and wrong-address delivery in Hark's promotion.
- Infrastructure response: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] argues for identity, visibility, compliance, reporting, and spending controls around agent action.

## Counterevidence & Qualifications
The evidence consists of reported incidents, not measured prevalence or proof that agent traffic is already a broad systemic burden. Some automated contact can reduce search and coordination costs for both users and merchants, and shared APIs may be less disruptive than phone calls. Controls must distinguish abusive repetition from legitimate accessibility, emergency, or high-value use.

## What Changed
- Created an externality framework that evaluates agent action from the perspective of affected third parties and shared infrastructure.

## Related Concepts
- [[AgentPermissionBoundaries]] - user-side authority relationship that does not by itself control aggregate harm.
- [[AgentIdentityAndAuthentication]] - attribution relationship for agents acting toward third parties.
- [[AgenticCommerce]] - transaction domain where displaced costs and wrong actions become concrete.
- [[PlatformAgentAccessConflict]] - platform relationship in which access controls may reflect both safety and commercial power.
- [[AgentTrustCalibration]] - trust relationship that should include effects on non-users, not only owner convenience.
- [[AgentRuntimeExecutionLayer]] - capacity and control relationship for automated demand against shared services.
