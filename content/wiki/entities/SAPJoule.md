---
title: "SAP Joule / Joule Work"
type: entity
tags: [product, sap, agents, enterprise-ai]
sources: [ai-chongji-qiye-ruanjian-jutou-yu-sap-yuanxin-liao-damoxing-to-b-de-dianfu-yu-bianjie-1-174-1]
last_updated: 2026-08-08
---

# SAP Joule / Joule Work

SAP Joule / Joule Work is the SAP assistant and work-entry layer described in [[ai-chongji-qiye-ruanjian-jutou-yu-sap-yuanxin-liao-damoxing-to-b-de-dianfu-yu-bianjie-1-174-1]]. The source says it should recognize user intent through natural language, dispatch agents or assistants, and let users create new agents when existing ones do not cover the workflow.

## Source Position
- Makes [[LanguageUserInterface]] a practical enterprise-software entry point rather than only a consumer chatbot pattern.
- Supports [[AutonomousEnterprise]] while keeping [[HumanJudgmentUnderAI]] in the loop for complex finance, compliance, and data-quality decisions.
- Depends on [[EnterpriseAgentGovernance]], [[EnterpriseOperationalMemory]], and SAP or non-SAP data access rather than model output alone.

## Connections
- [[SAP]], [[YuanXin]], and [[EnterpriseResourcePlanning]] — product and company context.
- [[AgenticWorkflow]], [[EnterpriseAgentGovernance]], and [[EnterpriseAgentMemory]] — agent execution and governance layer.
- [[AutonomousEnterprise]] and [[ERPTrustMoat]] — strategic direction and trust boundary.
