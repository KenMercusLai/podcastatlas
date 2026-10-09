---
title: "Vertical Agent Architecture"
type: concept
tags: [ai, agents, architecture, enterprise]
sources:
  - e255-moxing-yuelaiyue-qiang-weishenme-yonghu-mei-ganjue-zaifang-aliguojizhanzongcai-zhangkuo-8fa0b58e-8359-4609-8e84-30c9a632df50
last_updated: 2026-10-09
knowledge_schema: synthesis-v1
---

# Vertical Agent Architecture

## Definition
Vertical agent architecture is the joint design of model capability, execution harness, and domain context for agents expected to perform specialized work rather than only generate answers.

## Current Synthesis
E255 expresses the architecture as “model × Harness × Context.” The model supplies reasoning and multimodal capability. The harness connects tools, memory, permissions, orchestration, persistent execution, and verification. Context supplies organization-specific goals, records, communication history, market data, and domain feedback. The multiplicative framing means that a weak layer can constrain the entire system: a smarter model cannot act without tools and authority, while an elaborate runtime cannot compensate for missing business truth.

For cross-border ecommerce, the architecture must also be localized. Available platforms, logistics providers, rules, and operating conventions vary by country, while model training, inference, routing, and the harness need coordinated optimization for quality, latency, and cost. This makes a production vertical agent closer to a continuously operated business system than a prompt layer over one frontier model.

## Key Claims
- Model, harness, and context are complementary system layers rather than interchangeable sources of capability.
- The harness owns tool access, memory, permissions, execution state, orchestration, and recovery.
- Domain context includes proprietary records, interaction history, industry information, and feedback tied to outcomes.
- Regional tool and platform differences require localized execution and context integration.
- Model training, inference serving, routing, and runtime design should be optimized together.
- Sustainable deployment depends on cost as well as accuracy and task coverage.

## Evidence
- Three-layer formulation - [[e255-moxing-yuelaiyue-qiang-weishenme-yonghu-mei-ganjue-zaifang-aliguojizhanzongcai-zhangkuo-8fa0b58e-8359-4609-8e84-30c9a632df50]] attributes “model × Harness × Context” to [[ZhangKuo]] and describes the role of each layer.
- Commerce context - [[e255-moxing-yuelaiyue-qiang-weishenme-yonghu-mei-ganjue-zaifang-aliguojizhanzongcai-zhangkuo-8fa0b58e-8359-4609-8e84-30c9a632df50]] identifies procurement, supply-chain, communication, platform, industry, and trend data as inputs to [[Axio|Accio Work]].
- Full-stack optimization - [[e255-moxing-yuelaiyue-qiang-weishenme-yonghu-mei-ganjue-zaifang-aliguojizhanzongcai-zhangkuo-8fa0b58e-8359-4609-8e84-30c9a632df50]] links model choice, post-training, inference, harness design, context, and routing to accuracy, efficiency, and affordability.

## Counterevidence & Qualifications
The multiplicative formula is a design heuristic, not a measured law, and the source does not isolate the marginal contribution of each layer. Proprietary platform context can improve task grounding while also increasing lock-in, privacy exposure, and evaluation opacity. Existing vertical software providers may possess valuable workflows and records, but integration quality and model capability still determine whether those assets translate into useful agent behavior.

## What Changed
- Established the model–harness–context formulation as a dedicated vertical-agent architecture.
- Added regional adaptation and full-stack cost optimization to the architecture.
- Clarified that proprietary business context is useful only when connected to governed execution and verification.

## Related Concepts
- [[AgentHarness]] - execution and orchestration layer within the architecture.
- [[ContextEngineering]] - practice of selecting and structuring the information available to the agent.
- [[EnterpriseAgentProductionEnvironment]] - production controls and operational setting for deployed agents.
- [[AgentPermissionBoundaries]] - authorization limits within the harness.
- [[ModelRoutingCostControl]] - task-sensitive model selection for capability and affordability.
- [[BusinessAgentBenchmarkGap]] - evaluation gap that reveals weaknesses across the combined stack.
- [[AgenticB2BSourcing]] - vertical workflow in which this architecture is applied.
