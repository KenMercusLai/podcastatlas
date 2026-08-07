---
title: "On-Policy Distillation"
type: concept
tags: [ai, distillation, reinforcement-learning, post-training]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]
last_updated: 2026-08-08
---

# On-Policy Distillation

On-policy distillation is described in [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] as a post-training method where the student model generates its own trajectories and a teacher model scores them. The teacher therefore supplies denser reward signals over behavior the student actually produced, rather than only providing fixed offline answers.

The source contrasts this with off-policy distillation, where a teacher first generates a data set and the student imitates it offline. In K3's discussion, on-policy distillation is tied to [[MOPDPostTraining|MOPD]], reasoning-effort variation, and the open question of whether a model can improve itself without an external scalable supervision signal.

## Key Claims
- On-policy distillation keeps the training signal closer to the student's current behavior distribution.
- Teacher scoring can supply denser feedback than sparse final-answer rewards.
- The method still depends on external supervision quality; it is not proof that a model can "distill itself" into unbounded improvement.
- Off-policy and on-policy distillation should be separated when evaluating model-training claims or copying accusations.

## Connections
- [[ModelDistillation]], [[MOPDPostTraining]], [[AgentPostTraining]], and [[AgentRL]] — training-method context.
- [[KimiK3]], [[ZengZhiyuan]], and [[AIVerification]] — source and verifier context.
- [[RecursiveSelfImprovement]] and [[ModelPostTrainingBottleneck]] — boundary around self-improvement claims.
