---
title: "Airwallex Agent OS"
type: entity
tags: [product, agents, finance, api, airwallex]
sources: [11-nian-110-yi-meijin-ranhou-ne-duihua-airwallex-wu-kai-ai-shidai-xiayizhan-1000-yi-lr4tvdrq25by7fugoqkqojw6vwdk]
last_updated: 2026-08-07
---

# Airwallex Agent OS

Airwallex Agent OS is the agent-facing product layer described in [[11-nian-110-yi-meijin-ranhou-ne-duihua-airwallex-wu-kai-ai-shidai-xiayizhan-1000-yi-lr4tvdrq25by7fugoqkqojw6vwdk]]. [[WuKai]] says it provides command-line and API/MCP-style access so a customer's own agents can call Airwallex's financial capabilities directly.

The product makes [[AgentFacingInterfaces]] concrete in a regulated financial setting. Instead of asking an agent to drive a human GUI, Agent OS exposes financial actions through controlled interfaces that still need authentication, permission, auditability, and safe execution.

## Key Points
- Described as a CLI and API/MCP access layer for Airwallex capabilities.
- Intended for customer-owned agents, not only Airwallex's own assistant.
- Source-scoped examples include product-minded startup finance operators as potential users, not just large enterprises.
- Raises stronger requirements than ordinary tool APIs because financial actions involve money movement, policies, approval, and liability.

## Connections
- [[Airwallex]], [[WuKai]], and [[KaiAirwallex]] — company, speaker, and adjacent assistant product.
- [[AgentFacingInterfaces]], [[ModelContextProtocol]], [[AgentIdentityAndAuthentication]], and [[AgentPermissionBoundaries]] — agent interface and governance context.
- [[AgentPaymentInfrastructure]] and [[MoneyMovementInfrastructure]] — payment and financial-action infrastructure context.
- [[IntelligentFinance]] — broader Airwallex strategy.
