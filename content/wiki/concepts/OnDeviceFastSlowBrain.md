---
title: "On Device Fast Slow Brain"
type: concept
tags: [ai-architecture, robotics, edge-ai]
sources: [wo-yudao-le-di-yige-zhenzheng-xiang-mai-de-peiban-jiqiren-duihua-shibo-yueban-dongli-chuangshiren-gonglu-boke-lrydelizm0-hbk68u5cqe3ti-epb]
last_updated: 2026-07-06
---

# On Device Fast Slow Brain

On-device fast-slow brain is the architecture described by [[Shibo]] for [[Xiaoban]] in [[wo-yudao-le-di-yige-zhenzheng-xiang-mai-de-peiban-jiqiren-duihua-shibo-yueban-dongli-chuangshiren-gonglu-boke-lrydelizm0-hbk68u5cqe3ti-epb]]. The fast brain is a 1.7B model for immediate behavior decisions, while the slow brain is a 7B model for more complex logic and reasoning.

## Why It Matters
- [[CompanionRobots]] need low-latency embodied response because slow reaction breaks the feeling of presence.
- The episode says [[Xiaoban]] can keep voice, movement, and body feedback latency under about 0.4 seconds.
- The architecture supports 5-to-10-second generated action sequences instead of repeating the same canned animation every time.
- It pairs with cloud long-term memory and [[EmotionalInteractionModels]], but the source says raw audio and image data are not collected; training uses semantic features and embeddings.

## Connections
- [[Xiaoban]] and [[YuebanDongli]] — product and company using the architecture.
- [[Qwen]] and [[OpenSourceAIModels]] — model ecosystem feeding the architecture.
- [[RobotLiveliness]] — product quality that depends on fast embodied response.
- [[FamilyWorldSimulator]] — simulated home data source used to tune behavior.
