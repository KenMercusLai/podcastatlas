---
title: "Continual Learning"
type: concept
tags: [agents, learning, memory]
sources: [139-agent-de-zongshu-he-su-yu-liao-agent-jishushi-openclaw-moment-bianjie-de-xiaomi-he-shehui-de-fushe-luffrgudeiighqxam49tfqci63no, weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3]
last_updated: 2026-07-09
---

# Continual Learning

Continual learning is the agent-learning bottleneck emphasized by [[SuYu]] in [[139-agent-de-zongshu-he-su-yu-liao-agent-jishushi-openclaw-moment-bianjie-de-xiaomi-he-shehui-de-fushe-luffrgudeiighqxam49tfqci63no]]. The source notes that the term is used broadly, including avoiding task forgetting, personalization, self-improvement, post-training, and OpenClaw-like learning, but Su's main question is what the agent is trying to learn.

His answer is that continual learning should help agents acquire broader [[WorldModels]] of concrete working environments: organization structure, workflows, software operation, interpersonal context, task history, and theory of mind. Without that learning, agents remain unreliable, slow, expensive, and hard to specialize.

[[weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3]] adds a caution from [[KangHongwen]]: retraining or parameter-updating a model can personalize behavior, but it may not preserve precise personal memory. The episode distinguishes probabilistic preference learning from a [[LocalFirstMemoryLayer]] that can recover exact older files, clips, claims, and timestamps.

## Key Claims
- Continual learning is the shared bottleneck behind memory, self-learning, personalization, post-training, and expert-agent behavior.
- Learning should not merely accumulate raw history; it should build useful models of the small world where the agent operates.
- [[PersistentAgentMemory]], [[AISkills]], and [[AgentSelfEvolution]] are product-level pieces of the same learning problem.
- Solving continual learning would make [[SpecializedIntelligence]] and [[UniversalDigitalAgent]] more practical by reducing repeated instruction and failure.
- Continual learning and parameterized personalization should not be mistaken for complete personal memory when exact recall and source grounding matter.

## Connections
- [[WorldModels]] — the source's answer to what continual learning should learn.
- [[SpecializedIntelligence]] — target capability enabled by continual learning.
- [[PersistentAgentMemory]], [[AISkills]], and [[AgentSelfEvolution]] — related wiki concepts for retaining and reusing experience.
- [[AgentPostTraining]] and [[AgentRL]] — adjacent training approaches that can use agent traces and workflow feedback.
- [[LocalFirstMemoryLayer]] and [[DataToMemoryTransformation]] — S10E20's external-memory contrast with parameterized learning.
