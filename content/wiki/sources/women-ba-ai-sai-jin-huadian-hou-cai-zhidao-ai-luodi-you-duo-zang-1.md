---
title: "我们把 AI 塞进花店后，才知道AI落地有多脏"
type: source
tags: [podcast, ai, offline-retail, local-services, operations]
sources: []
date: 2026-06-08
source_file: "/home/ken/repos/podcastatlas/content/episodes/我们把 AI 塞进花店后，才知道AI落地有多脏 ｜ 科技乱炖⧸急中生智⧸拼娃时代⧸其他 (1) [我们把-ai-塞进花店后，才知道ai落地有多脏-1].md"
source_url: "https://hosting.wavpub.cn/dao-sub/2026/06/08/%e6%88%91%e4%bb%ac%e6%8a%8a-ai-%e5%a1%9e%e8%bf%9b%e8%8a%b1%e5%ba%97%e5%90%8e%ef%bc%8c%e6%89%8d%e7%9f%a5%e9%81%93ai%e8%90%bd%e5%9c%b0%e6%9c%89%e5%a4%9a%e8%84%8f/"
last_updated: 2026-07-07
---

## Summary
This [[KejiLuandun]] episode expands an earlier flower-shop example into a full [[OfflineAIImplementation]] field report. The hosts describe opening and running a real flower shop to test AI in ordering, product images, substitutions, paid promotion, delivery-platform operations, and store workflow, then conclude that AI value appeared only after they entered the messy work of staff habits, paper tickets, voice prompts, inventory uncertainty, customer confirmation, and platform rules. The source adds [[AIVisualMerchandising]], [[OperationalDataCapture]], and [[LocalLifePlatformDependency]] as concrete patterns, while warning that generic model capability, imagined inventory controls, or software-driven staff micromanagement are not enough.

## Key Claims
- The hosts frame the episode as a reply to "can AI really land?" by using their own flower-shop operation rather than abstract model demos.
- Flower-shop economics overturned their first assumption: because flower input cost can be low relative to successful sales, reducing spoilage was less important than creating demand, selling more bundles, and handling orders well.
- Store workflow is not screen-first. Florists have both hands occupied, external platforms use loud voice prompts, and A4 printouts carry product images, order details, and remarks into the production flow.
- Staff management is a harder bottleneck than software dashboards. The hosts argue that line employees may dismiss system instructions, so ownership, incentives, and responsibility boundaries matter more than attempts to control every action by machine.
- An imagined daily inventory feature was cut because workers were unlikely to count every remaining flower at closing. A more plausible version was to photograph the fridge and let AI process the image later.
- [[AIVisualMerchandising]] became valuable when the system used real store materials to create flower-product references and replacement images. Generic image models or [[Doubao]]-style prompts could produce pretty images, but often failed on specific flower materials and operational constraints.
- The highest-value customer-facing AI use case was material substitution: when a flower was out of stock, the system could mark and replace it in an image so the customer could confirm the change before the florist spent more time or materials.
- [[LocalLifePlatformDependency]] is presented as both useful and constraining. Delivery platforms bring discovery and orders to otherwise low-traffic stores, but they also impose commissions, paid-traffic pressure, response-time rules, opening-time expectations, and fulfillment metrics.
- Platform data access is a practical AI bottleneck. The hosts say APIs are conservative, thresholds are high, and even formal access may not expose the marketing and order details a merchant wants.
- [[OperationalDataCapture]] appears as a workaround: the team put a device between the computer and printer to capture the same order data that would have been printed, then planned to feed it into OCR, AI processing, voice prompts, and agent-style order assistance.
- Delivery-platform speed metrics can create quality pressure. The episode argues that very short delivery promises may favor pre-made or narrow-SKU flowers, while more careful arrangements require time.
- The source includes consumer advice from the operational view: avoid very early flower deliveries if freshness matters, pre-order for holidays, and ask florists what is currently suitable instead of defaulting to stale-looking combinations.
- Gift flowers can cross compliance boundaries when they include cigarettes, packaged food, or other goods, so offline AI tooling must still respect licenses, invoices, and local business rules.

## Key Quotes
> "必须脏手干活" — the episode's central lesson for AI deployment in offline businesses.

> "豆包也能出" — the customer objection used to distinguish generic AI output from a workflow-ready vertical system.

> "顾客咨询，请在一分钟内回复" — the platform prompt that anchors the episode in live merchant pressure.

## Connections
- [[KejiLuandun]] — show context and recurring source for AI commercialization, platform friction, and product-building skepticism.
- [[OfflineAIImplementation]] — the source's main pattern: AI requirements have to be discovered inside real offline work.
- [[AIVisualMerchandising]] — concrete useful AI layer for generating flower-product references and substitution confirmation images.
- [[OperationalDataCapture]] — printer/OCR/order-data workaround created because official platform data access was too limited.
- [[LocalLifePlatformDependency]] — delivery-platform dependence around discovery, paid traffic, response rules, API limits, and fulfillment rankings.
- [[DirtyWork]], [[AIEngineeringThinking]], and [[AIOperationsRole]] — the episode's "dirty hands" claim that domain work must be made explicit before AI can help.
- [[BusinessLedAITransformation]], [[FrontlineAIEnablement]], and [[HumanJudgmentUnderAI]] — organizational frame for why AI should assist local workers and operators rather than simply centralize control.
- [[ChinaAgentMarketFriction]], [[AgentFacingInterfaces]], and [[PlatformDataRegulation]] — platform closure and data-interface constraints that block clean agent integration.
- [[CustomerPull]], [[DistributionLedProductBuilding]], and [[ProductLedWillingnessToPay]] — demand, channel, and value lessons behind deciding which AI features matter.

## Contradictions
- No direct contradiction with prior wiki content. The source deepens the earlier [[ai-hui-xie-daima-le-weishenme-ni-haishi-zuo-bu-chu-chanpin-1]] flower-shop example by showing the fieldwork behind it.
- It creates a useful tension with broad [[FrontlineAIEnablement]] optimism: AI can improve frontline work, but only after staff incentives, hands-busy workflows, platform rules, and data access are handled.
- The operational conclusions are based mainly on one shop and the hosts' own experiments, so claims about flower-shop economics, platform ad performance, and consumer freshness should be treated as source-specific rather than universal retail facts.
