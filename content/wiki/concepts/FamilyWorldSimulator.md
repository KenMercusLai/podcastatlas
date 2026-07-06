---
title: "Family World Simulator"
type: concept
tags: [simulation, robotics, emotional-ai]
sources: [wo-yudao-le-di-yige-zhenzheng-xiang-mai-de-peiban-jiqiren-duihua-shibo-yueban-dongli-chuangshiren-gonglu-boke-lrydelizm0-hbk68u5cqe3ti-epb]
last_updated: 2026-07-06
---

# Family World Simulator

Family world simulator is [[YuebanDongli]]'s simulated home-interaction environment for training and testing [[Xiaoban]] before large amounts of real household data exist. In [[wo-yudao-le-di-yige-zhenzheng-xiang-mai-de-peiban-jiqiren-duihua-shibo-yueban-dongli-chuangshiren-gonglu-boke-lrydelizm0-hbk68u5cqe3ti-epb]], [[Shibo]] says the simulator models active and passive emotional interactions, predicts changes in human emotional state and interaction state, and generates data used to fine-tune the fast and slow brains.

## Role In The Product
- Provides synthetic or simulated interaction data for [[EmotionalInteractionModels]].
- Helps test long-term companion behavior before wide household deployment.
- Extends [[WorldModels]] from physical reasoning into family relationship state, emotion, and interaction dynamics.
- Reduces dependence on collecting raw household audio or images, though the episode leaves open how robust the privacy and data pipeline will be in practice.

## Connections
- [[Xiaoban]] and [[YuebanDongli]] — product and company case.
- [[OnDeviceFastSlowBrain]] — model stack tuned with simulator data.
- [[CompanionRobots]] and [[RobotLiveliness]] — user-facing goals the simulator supports.
- [[EmbodiedAI]] and [[WorldModels]] — broader technical context.
