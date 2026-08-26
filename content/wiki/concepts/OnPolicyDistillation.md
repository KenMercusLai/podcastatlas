---
title: "On-Policy Distillation"
type: concept
tags: [ai, distillation, reinforcement-learning, post-training]
sources:
  - xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1
  - 152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6
last_updated: 2026-08-26
knowledge_schema: synthesis-v1
---

# On-Policy Distillation

## Definition
On-policy distillation is a distillation method where the student model generates behavior from its current policy and a teacher model provides feedback, scoring, correction, or learning targets on that student-produced behavior.

## Current Synthesis
The wiki treats OPD as the distillation form most closely aligned with agent and reasoning post-training. Instead of only imitating a fixed teacher-written dataset, the student exposes its current failure modes by generating trajectories or reasoning traces, then receives teacher feedback near its own behavior distribution. In the K3 sources, OPD sits beside [[MOPDPostTraining|MOPD]], [[MultiTeacherDistillation]], QAT, MTP, and reward design. Its value is denser, more relevant supervision; its limit is that teacher quality, task environment, provenance, and evaluation still determine whether the feedback improves the student rather than simply copying style or errors.

## Key Claims
- OPD keeps supervision closer to the student's current behavior than offline teacher-output imitation.
- Teacher feedback can be denser than a sparse final-answer reward, especially for reasoning or agent trajectories.
- OPD can be combined with multiple teachers or domain experts when different capabilities need different feedback sources.
- The method still depends on external supervision quality and does not prove unbounded self-improvement.
- Distinguishing OPD from off-policy distillation matters when evaluating model-training claims, copying accusations, or post-training workflows.

## Evidence
- Student-policy proximity: [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] describes on-policy distillation as student-generated trajectories scored by a teacher rather than a fixed teacher-generated dataset.
- Stepwise correction: [[152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6]] explains OPD as the student producing a reasoning process that the teacher can correct progressively.
- Capability integration: [[152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6]] connects OPD to multi-teacher distillation and post-training management across specialized rewards or abilities.

## Counterevidence & Qualifications
OPD is not a clean escape from the supervision bottleneck. If the teacher is weak, biased, unavailable, restricted by terms, or poorly matched to the task, on-policy feedback can reinforce bad behavior. OPD also needs environments and evaluations that expose meaningful student behavior; a teacher correcting shallow traces is not equivalent to scalable agent competence.

## What Changed
- Adds the progressive-correction explanation from the K3 technical reading.
- Connects OPD more explicitly to [[MultiTeacherDistillation]] and post-training project management.
- Preserves the earlier boundary that OPD is external teacher supervision, not proof of self-contained recursive improvement.

## Related Concepts
- [[ModelDistillation]] - parent technical and governance category.
- [[MultiTeacherDistillation]] - complementary pattern using several teachers or expert models.
- [[MOPDPostTraining]] - K3-adjacent workflow that can merge specialized post-trained capabilities.
- [[AgentPostTraining]] - setting where on-policy trajectories and teacher feedback become useful.
- [[AgentRL]] - reinforcement-learning context that OPD can supplement.
- [[KimiK3]] - model case grounding the current source discussion.
