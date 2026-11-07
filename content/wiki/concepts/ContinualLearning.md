---
title: "Continual Learning"
type: concept
knowledge_schema: synthesis-v1
tags: [agents, learning, memory]
sources:
  - 139-agent-de-zongshu-he-su-yu-liao-agent-jishushi-openclaw-moment-bianjie-de-xiaomi-he-shehui-de-fushe-luffrgudeiighqxam49tfqci63no
  - weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3
  - 174-women-hai-neng-gei-suanfa-dang-duojiu-de-pinwei-laoshi-duitan-yamaxun-agi-cha-sheng-lrs0qgmr9gy1nbdtrsvn2lx5dxza
  - lkbt2upqw6eoxm0yjc1zklr8wlgc-lkbt2upqw6eoxm0yjc1zklr8wlgc
last_updated: 2026-11-08
---

# Continual Learning

## Definition
Continual learning is the ability of an AI system to integrate experience over time into useful behavior or world models without repeatedly starting over, catastrophically forgetting prior abilities, or confusing compressed preference with exact memory.

## Current Synthesis
The bounded sources separate three things often collapsed under one label. [[SuYu]] asks agents to learn the concrete “small worlds” of organizations, software, workflows, people, and task history. [[KangHongwen]] argues that parameter updates cannot substitute for a source-grounded memory layer when exact files, events, or timestamps must be recovered. [[ChaSheng]] treats fast learning without forgetting as a major capability gap between current language models and AGI. [[MaXiaoteng]] adds the idea of compressed experience or “taste”: a system should retain durable judgment from long exposure even when it does not preserve every item in active memory.

The current synthesis is therefore hybrid. Continual learning may need parameter or adapter updates for behavior and judgment, external memory for precise recall and provenance, and evaluation that detects forgetting, drift, and harmful preference absorption. No bounded source provides a settled architecture that joins these layers.

## Key Claims
- Continual learning should build useful models of the environments in which an agent repeatedly operates.
- Accumulated raw history is not sufficient; experience must be compressed into reusable behavior, concepts, or judgment.
- Parameterized preference and “taste” are not substitutes for exact, source-grounded personal memory.
- External memory, skills, post-training, and model updates are complementary pieces rather than interchangeable solutions.
- Fast learning without catastrophic forgetting remains a capability gap for current language-model systems.
- Lightweight adapters may be candidates for durable updates, but ordinary static LoRA does not yet solve long-term learning.

## Evidence
### Learning concrete working worlds
- [[139-agent-de-zongshu-he-su-yu-liao-agent-jishushi-openclaw-moment-bianjie-de-xiaomi-he-shehui-de-fushe-luffrgudeiighqxam49tfqci63no]] defines the target as organizational structure, workflows, software operation, interpersonal context, task history, and theory of mind.

### Exact memory versus learned preference
- [[weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3]] distinguishes probabilistic personalization from a local memory layer that can recover precise older files, clips, claims, and timestamps.

### AGI capability boundary
- [[174-women-hai-neng-gei-suanfa-dang-duojiu-de-pinwei-laoshi-duitan-yamaxun-agi-cha-sheng-lrs0qgmr9gy1nbdtrsvn2lx5dxza]] argues that current paradigms lack human-like fast learning and continual learning without forgetting.

### Compressed experience and taste
- [[lkbt2upqw6eoxm0yjc1zklr8wlgc-lkbt2upqw6eoxm0yjc1zklr8wlgc]] uses a researcher reading many papers to illustrate how details can compress into durable intuition and research taste.
- [[lkbt2upqw6eoxm0yjc1zklr8wlgc-lkbt2upqw6eoxm0yjc1zklr8wlgc]] proposes lightweight, repeatedly updated memory units as a possible direction while explicitly leaving their update method unresolved.

## Counterevidence & Qualifications
- “Continual learning” covers task retention, personalization, memory, self-improvement, post-training, and world-model acquisition; progress on one does not establish progress on the others.
- Parameter updates can blur provenance and may absorb errors or preferences that users cannot inspect or delete precisely.
- External retrieval can preserve exact records but does not by itself create abstraction, judgment, or transferable skill.
- The five-year AGI timing mentioned in one source is a dated expert judgment, not a wiki forecast.
- The lightweight-adapter direction is speculative and lacks architecture, benchmark, or longitudinal evidence in the source.

## What Changed
- Migrated the page to `synthesis-v1` using all prior bounded sources.
- Added compressed experience and research taste as a distinct target alongside world models and exact recall.
- Clarified the hybrid boundary among parameter learning, adapters, skills, and external memory.

## Related Concepts
- [[WorldModels]] - structured understanding of the environment an agent repeatedly inhabits.
- [[PersistentAgentMemory]] - retained experience and context across sessions.
- [[LocalFirstMemoryLayer]] - precise, private, source-grounded recall outside model parameters.
- [[DataToMemoryTransformation]] - conversion of raw archives into reusable memory.
- [[AISkills]] - procedural units that can preserve repeatable behavior.
- [[AgentSelfEvolution]] - broader self-improvement frame that depends on learning and verification.
- [[LowRankAdapterModelDiversity]] - adapter-based specialization and speculative route to lightweight updates.
- [[ResearchTaste]] - compressed judgment that the newest source wants long-term learning to preserve.
