---
title: "Vertical Workflow AI"
type: concept
tags: [ai, workflow, product]
sources: [263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs, yige-ai-chuangshiren-de-xurongxin-zhuang-he-yumei-zhidian-duitan-invoko-ai-chuangshiren-mengqi-lsi79o-z19zplvmqdbpzzneogpk3f]
last_updated: 2026-07-09
---

# Vertical Workflow AI

Vertical workflow AI is the source's nameable pattern for AI products that solve a concrete domain workflow rather than only expose model generation. In [[263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs]], the clearest examples are [[MeituDesignStudio]], [[Kaipai]], and [[Wink]], where output has to fit ecommerce, advertising, beauty, video, teleprompter, or training-material needs.

The source argues that AI can often produce a rough 80-point result quickly, but users with existing 95-point workflows still need the final 20 points: taste, correction, consistency, delivery format, batch operations, and business-fit judgment. That last-mile work is where [[AIApplicationLayerMoat]] can remain.

[[yige-ai-chuangshiren-de-xurongxin-zhuang-he-yumei-zhidian-duitan-invoko-ai-chuangshiren-mengqi-lsi79o-z19zplvmqdbpzzneogpk3f]] adds a boundary case. [[InvokoAI]]'s early Sourcing Agent and growth-Agent work looked vertical, but [[Mengqi]] later concluded that automating a low-value slice can still produce a SaaS-like or agency-like product if the user needs process controls, communication, and service follow-through more than the initial AI-generated list.

## Key Claims
- A vertical workflow is defined by the downstream job, not by the model modality.
- The product must understand acceptance criteria, not only generate plausible media.
- Vertical workflow products can use [[ModelContainerStrategy]] because the model is one component of the workflow.
- [[ToAgentDistribution]] can expose vertical workflow capabilities to agents once the capability is stable enough to be called from outside the app.
- A vertical Agent is not automatically a strong vertical workflow product; the product must cover the valuable job, not only the automatable step.
- Expert-user controls can improve reliability while also pulling the product away from end-to-end automation.

## Connections
- [[Meitu]], [[MeituDesignStudio]], [[Kaipai]], and [[Wink]] — source cases.
- [[AIVisualMerchandising]], [[OfflineAIImplementation]], and [[DomainExpertAlignment]] — adjacent wiki concepts.
- [[HumanJudgmentUnderAI]] and [[ProductLedWillingnessToPay]] — judgment and willingness-to-pay boundaries.
- [[VerticalAgentSaaSification]], [[InvokoAI]], and [[Mengqi]] — negative vertical-Agent case added by the 42章经 episode.
