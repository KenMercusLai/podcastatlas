---
title: "AI Model Orchestration"
type: concept
tags: [ai, models, agents, platforms]
sources: [all-in-with-chamath-jason-sacks-friedberg-microsoft-ceo-satya-nadella-on-ais-business-revolution-what-happens-to-saas-openai-and-microsoft-live-from-davos-39818140]
last_updated: 2026-08-18
---

# AI Model Orchestration

AI model orchestration is the practice of composing multiple models, roles, evaluations, agent calls, and workflow context rather than treating one frontier model as the whole application. In [[all-in-with-chamath-jason-sacks-friedberg-microsoft-ceo-satya-nadella-on-ais-business-revolution-what-happens-to-saas-openai-and-microsoft-live-from-davos-39818140]], [[SatyaNadella|Satya Nadella]] says application builders will use many models and points to [[MicrosoftFoundry|Microsoft Foundry]] as a layer for agent apps, RL gyms, evals, and model orchestration.

The source's healthcare example is a decision orchestrator: prompted roles such as investigator, data analyst, and domain expert can produce better results than asking one model to be everything. That makes orchestration a product and evaluation problem, not only a cost-routing trick.

## Key Claims
- Closed frontier models, open frontier-class models, and firm-specific models can coexist inside one workflow.
- Orchestration needs evaluations because a model can be strong in general but weak for a particular role, data context, latency target, or compliance boundary.
- [[AgenticWorkflow]] pushes orchestration beyond answer selection into tool use, background execution, review, and recovery.
- Application-layer value can sit in task decomposition, context, permissions, and evidence capture even when base model capability is widely available.

## Connections
- [[MicrosoftFoundry|Microsoft Foundry]], [[Azure]], [[OpenAI]], and [[OpenSourceAIModels]] - platform and model contexts in the source.
- [[ModelProviderToolCompetition]], [[ModelRoutingCostControl]], [[FirmSpecificModelKnowledge]], and [[AIApplicationLayerMoat]] - adjacent competition and product-defensibility themes.
- [[EnterpriseAgentGovernance]] and [[AgenticWorkflow]] - governance and work-execution layers.
