---
title: "Training Compute Allocation"
type: concept
tags: [compute, model-training, ai-infrastructure]
sources: [138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]
last_updated: 2026-07-08
---

# Training Compute Allocation

Training compute allocation is the problem of deciding how scarce cards and infrastructure should be divided among research exploration, pretraining, post-training, evaluation, and agent rollouts. In [[138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]], [[LuoFuli]] says agent workflows make card count a sharper bottleneck because agents speed up idea generation, code implementation, and experiment setup.

The source's concrete heuristic is that a frontier-style team aiming at high agent capability may need research, pretraining, and post-training resources closer to a 3:1:1 ratio, and that top teams may already be moving pretraining and post-training investment toward near parity. The claim is not just about more compute; it is about more parallelism once [[MLCoding]] and [[AgentPostTraining]] lower the human time needed to produce new experiments.

## Key Claims
- Faster idea-to-code loops move the bottleneck from researcher time toward cards, evaluation, and experiment scheduling.
- Agent-era compute demand includes post-training and rollout, not only base-model pretraining.
- Teams need enough research compute to test many ideas in parallel before committing to a large training direction.
- The value of compute depends on [[ResearchTaste]], because cheap experiments can still waste scarce infrastructure if the question is weak.
- Compute allocation is an [[AIOrganizationDesign]] issue as well as an infrastructure issue: rigid group boundaries can prevent resources and people from moving to the current bottleneck.

## Connections
- [[LuoFuli]], [[Xiaomi]], and [[MemoVR]] — source team and model context.
- [[FrontierModelScaling]] — broader scaling pressure around parameters, data, and training efficiency.
- [[AgentPostTraining]] and [[AgentRL]] — post-training and rollout demand that changes allocation.
- [[MLCoding]], [[ResearchTaste]], and [[ProblemDefinitionInResearch]] — faster experiment loops and idea quality.
- [[AIInferenceCostStructure]] and [[ModelRoutingCostControl]] — serving-side counterpart where model cost must be routed by task value.
