---
title: "Vertical Workflow AI"
type: concept
tags: [ai, workflow, product]
sources: [263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs]
last_updated: 2026-07-08
---

# Vertical Workflow AI

Vertical workflow AI is the source's nameable pattern for AI products that solve a concrete domain workflow rather than only expose model generation. In [[263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs]], the clearest examples are [[MeituDesignStudio]], [[Kaipai]], and [[Wink]], where output has to fit ecommerce, advertising, beauty, video, teleprompter, or training-material needs.

The source argues that AI can often produce a rough 80-point result quickly, but users with existing 95-point workflows still need the final 20 points: taste, correction, consistency, delivery format, batch operations, and business-fit judgment. That last-mile work is where [[AIApplicationLayerMoat]] can remain.

## Key Claims
- A vertical workflow is defined by the downstream job, not by the model modality.
- The product must understand acceptance criteria, not only generate plausible media.
- Vertical workflow products can use [[ModelContainerStrategy]] because the model is one component of the workflow.
- [[ToAgentDistribution]] can expose vertical workflow capabilities to agents once the capability is stable enough to be called from outside the app.

## Connections
- [[Meitu]], [[MeituDesignStudio]], [[Kaipai]], and [[Wink]] — source cases.
- [[AIVisualMerchandising]], [[OfflineAIImplementation]], and [[DomainExpertAlignment]] — adjacent wiki concepts.
- [[HumanJudgmentUnderAI]] and [[ProductLedWillingnessToPay]] — judgment and willingness-to-pay boundaries.
