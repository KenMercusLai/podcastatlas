---
title: "Enterprise Agent Store"
type: concept
tags: [ai, enterprise-ai, marketplace, software]
sources: [e225-saasye-shuqianyi-shizhi-zhengfa-ai-ruhe-biange-zuzhi-jiagou]
last_updated: 2026-07-08
---

# Enterprise Agent Store

Enterprise agent store is the marketplace pattern discussed in [[e225-saasye-shuqianyi-shizhi-zhengfa-ai-ruhe-biange-zuzhi-jiagou]], where a platform hosts self-built and partner-built enterprise agents. [[ZhangShaofeng]] contrasts this with consumer GPT-style stores and argues that enterprise agents require a stronger PaaS layer for workflow, permission, billing, integration, evaluation, and result delivery.

## Key Claims
- Consumer agent stores can be led by foundation-model companies, but enterprise agent stores may not be monopolized by one model provider because business workflows and industry integrations are fragmented.
- A useful enterprise store needs more than prompts: agents must connect to private data, systems, role permissions, compliance rules, and acceptance criteria.
- The store gives [[IndependentAgentVendor]] builders a route to market while letting platform owners share revenue.
- Enterprise stores are tied to [[ResultAsAService]] because buyers evaluate agents by task completion and business results, not just installation count.

## Connections
- [[IndependentAgentVendor]] — third-party builder role the store enables.
- [[AIStaffing]] and [[AIBPORollUp]] — commercial modes that can consume store-supplied agents.
- [[AgentFacingInterfaces]] and [[ModelContextProtocol]] — infrastructure patterns for exposing tools and systems to agents.
- [[BairongIntelligence]] — company whose platform ambition anchors the source.
