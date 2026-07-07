---
title: "Representation Learning"
type: concept
tags: [ai, machine-learning, representations]
sources: [133-dui-xie-saining-de-7-xiaoshi-ma-la-song-fangtan-shijie-moxing-taochu-guigu-ami-labs-liangci-jujue-ilya-yang-likun-li-feifei-he-42]
last_updated: 2026-07-08
---

# Representation Learning

Representation learning is the long research trunk [[XieSaining]] uses in [[133-dui-xie-saining-de-7-xiaoshi-ma-la-song-fangtan-shijie-moxing-taochu-guigu-ami-labs-liangci-jujue-ilya-yang-likun-li-feifei-he-42]] to connect computer vision, self-supervision, diffusion, multimodal work, and [[WorldModels]]. In his framing, the problem is to map data into a space with useful properties for downstream recognition, generation, reasoning, planning, or action.

## Key Claims
- A research career can move across image recognition, segmentation, video, embodied RL, diffusion, and world models while still staying inside one representation-learning trunk.
- Architectures, data, and objectives are three main levers for representation learning.
- Good representations should become more abstract and decision-relevant rather than merely preserving raw perceptual detail.
- [[SelfSupervisedLearning]] is one route for learning representations, but the source says language-model pretraining is not simply ordinary self-supervision because language already contains human-provided abstractions.
- [[WorldModels]] require representation learning because the system must predict state transitions at the right abstraction level rather than simulate every low-level physical detail.

## Connections
- [[XieSaining]] — source speaker who frames his career through this concept.
- [[KaimingHe]], [[FAIR]], and [[ResNeXt]] — architecture and scalable vision-representation thread.
- [[SelfSupervisedLearning]], [[DiffusionTransformers]], and [[MultimodalIntelligence]] — methods and domains connected in the source.
- [[WorldModels]] and [[JointEmbeddingPredictiveArchitecture]] — longer-term predictive-intelligence route.
- [[ProblemDefinitionInResearch]] and [[ResearchTaste]] — methodological companions in the interview.
