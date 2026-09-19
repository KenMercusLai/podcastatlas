---
title: "Agent Spend Controls / 智能体消费控制"
type: concept
tags: [agents, payments, governance, security]
sources:
  - keyi-gei-nide-agent-fa-yidian-linghuaqian-le-s10e22-9a652c19-ceb3-46c2-87b4-bca36e684311
  - waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87
knowledge_schema: synthesis-v1
last_updated: 2026-09-19
---

# Agent Spend Controls / 智能体消费控制

## Definition
Agent spend controls / 智能体消费控制 are the monetary limits, eligible uses, time windows, credentials, confirmations, audit evidence, and reauthorization rules that bound how an agent spends for a user or organization.

## Current Synthesis
Spend controls translate general [[AgentPermissionBoundaries]] into payment authority. A useful agent needs enough budget autonomy to complete shopping, booking, token, API, data, or service tasks without asking at every step, but a stored card or broad wallet login makes scope and responsibility ambiguous.

The current synthesis is a graduated mandate: specify an amount ceiling, product or service category, merchant constraints, time window, task purpose, substitution rules, and conditions requiring renewed consent. Pair that mandate with a one-time or otherwise scoped credential, agent identity, execution trace, and dispute evidence.

Trust should determine breadth rather than disappear after one approval. Low-risk recurring tasks can receive standing limits, while high-value, regulated, identity-sensitive, or materially changed purchases require explicit confirmation. The user's willingness to raise the maximum delegated amount is evidence of [[AgentTrustCalibration]], not proof that all purchases should become autonomous.

## Key Claims
- Budget autonomy should be sufficient for task completion but narrower than the user's underlying payment account.
- Amount, category, merchant, duration, purpose, and substitution constraints should travel with the payment mandate.
- Repeated low-value purchases need standing permission with revocation and review, while high-risk purchases need renewed confirmation.
- Separate accounts, one-time credentials, and audit records improve attribution when spending is wrong or compromised.
- Spend limits work best when tied to authenticated principals, known agents, [[VerifiableIntent]], and enforceable execution controls.
- Compensation and dispute handling affect how much users will rationally delegate.

## Evidence
- Mandate evidence: [[keyi-gei-nide-agent-fa-yidian-linghuaqian-le-s10e22-9a652c19-ceb3-46c2-87b4-bca36e684311]] describes price, category, user-intent, merchant, and one-time-payment constraints for agent purchases.
- Self-spend evidence: [[keyi-gei-nide-agent-fa-yidian-linghuaqian-le-s10e22-9a652c19-ceb3-46c2-87b4-bca36e684311]] distinguishes consumer shopping from small budgets for tokens, APIs, reports, images, and other task resources.
- Strong-constraint evidence: [[waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87]] says an initial 100-yuan limit must not be displaced by later task content.
- Delegation evidence: [[waitan-dahui-xianxia-yuanzhuo-gan-ba-qianbao-jiaogei-ai-ma-liaoliao-agent-jiaoyi-baofa-qianye-de-xinren-jijian-78ec2d74-0ad7-4c6f-9764-728eec0e6e87]] uses the maximum amount a user would delegate as a concrete test of authorization, safety, and recourse confidence.

## Counterevidence & Qualifications
- Monetary ceilings do not prevent wrong-product selection, biased recommendations, privacy leakage, or prohibited non-financial actions.
- Confirmation on every purchase creates approval fatigue; standing permission creates stale-authority risk.
- Fiat, card, wallet, and stablecoin systems differ in reversibility, custody, fraud controls, and legal recourse.
- The sources provide design patterns rather than validated universal thresholds for safe delegation.

## What Changed
- Migrated the page to `synthesis-v1` from the complete prior source set.
- Added stable strong constraints, progressive delegated amounts, and recourse as parts of spend control.
- Linked monetary authority explicitly to verifiable intent and trust calibration.

## Related Concepts
- [[AgentPaymentInfrastructure]] - payment and dispute layer implementing spending mandates.
- [[AgentPermissionBoundaries]] - broader authority model within which monetary limits sit.
- [[AgentIdentityAndAuthentication]] - attribution of the principal and acting agent.
- [[VerifiableIntent]] - semantic task and constraint record carried with payment authority.
- [[AgentTrustCalibration]] - basis for increasing or narrowing delegated limits over time.
- [[Stablecoins]] - settlement route with different reversibility and custody assumptions.
