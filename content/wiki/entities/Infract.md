---
title: "Infract"
type: entity
tags: [company, ai-infrastructure, open-source, inference]
sources: [148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]
last_updated: 2026-08-08
---

# Infract

Infract is the company around [[VLLM|vLLM]] discussed in [[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]]. [[YuKaichao|游凯超]] describes it as the organization needed to sustain open-source inference work once vLLM became important production infrastructure.

The source gives a practical reason for the company form. A volunteer community can review code and accept contributions, but it cannot reliably allocate full-time people, sign NDAs with strategic users, secure large cluster resources, do quarterly planning, or support customers under production pressure. Infract is therefore framed as a commercial support layer around [[OpenSourceAIInfrastructure]], not as a replacement for vLLM's open governance.

The episode says Infract explores endpoint service, BYOC, and strategic-customer cooperation. Its preferred business logic is to charge against token value created or costs saved, rather than simply selling engineering hours.

## Connections
- [[VLLM|vLLM]] — core open-source project around which the company operates.
- [[YuKaichao|游凯超]] — co-founder and chief scientist in the source.
- [[PyTorchFoundation|PyTorch Foundation]] — governance home for vLLM's trademark and community ownership.
- [[OpenSourceAIInfrastructure]] and [[LargeCompanyOpenSourceStrategy]] — open-source sustainability context.
- [[AIInferenceCostStructure]], [[ModelInfraCoDesign]], and [[AIInfrastructureFullStackMoat]] — technical and commercial problem space.
