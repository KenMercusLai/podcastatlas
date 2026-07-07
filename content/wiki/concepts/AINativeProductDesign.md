---
title: "AI Native Product Design"
type: concept
tags: [ai, product-design, agents]
sources: [130-zhang-yueguang-chuangye-liangnian-shouci-fangtan-miaoya-bushi-ai-native-chanpin-liucheng-dao-shangxiawen-sheji-one-way-door-he-yinv-youxi]
last_updated: 2026-07-08
---

# AI Native Product Design

AI native product design is [[ZhangYueguang]]'s distinction between products that merely use AI well and products whose interaction, output, organization, and value structure are shaped by model behavior. In [[130-zhang-yueguang-chuangye-liangnian-shouci-fangtan-miaoya-bushi-ai-native-chanpin-liucheng-dao-shangxiawen-sheji-one-way-door-he-yinv-youxi]], he says [[Miaoya]] needed AI but still behaved like an internet product with a bounded flow and predictable output.

The design shift is from flow-first to context-first. Traditional internet product work designs screens, buttons, branches, and expected user paths. AI-native work starts by asking what [[ContextEngineering]] the model needs, how open the user input and output can be, where the model boundary sits, and which generated unit should be made reliable before the larger interface is finalized.

## Key Claims
- "Cannot exist without AI" is necessary but not sufficient for an AI-native product.
- Open input and open output change the product manager's job from controlling every branch toward shaping context, constraints, feedback, and quality standards.
- Agent products intensify this shift because the model may interpret language, choose steps, and execute tasks rather than only generate content.
- Product, design, engineering, and model exploration need to work together earlier because taste, context, latency, editability, and model limits define the product surface.
- [[Docky]] applies this by refining the smallest PPT generation unit and context requirements before designing the full user flow.

## Connections
- [[Miaoya]] — strong AI-powered product used as a contrast case.
- [[Docky]] — agent product where Zhang tries to apply the AI-native method directly.
- [[ContextEngineering]] — context-first design substrate.
- [[AgenticWorkflow]], [[AgentFacingInterfaces]], and [[HumanAgentCollaboration]] — adjacent product forms where AI acts over tasks and tools.
- [[AIOrganizationDesign]] — team collaboration pattern required when model effect and product surface are co-designed.
- [[OneWayDoorProduct]] — outcome standard for whether the new AI-native experience changes user behavior.
