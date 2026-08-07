---
title: "Mixture of Experts"
type: concept
tags: [ai, model-architecture, infrastructure, semiconductors]
sources: [e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149, 147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]
last_updated: 2026-08-07
---

# Mixture of Experts

Mixture of Experts is the model-architecture pattern discussed in [[e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149]] through its impact on [[TPU]] topology. [[HenryTPUEngineer|Henry]] says earlier TPU generations struggled with MoE because expert routing requires all-to-all communication, while older 2D Torus layouts mostly connected neighboring chips.

The source treats MoE as a practical example of [[ASICWorkloadPredictionRisk]]. A chip family can be well suited to dense [[TransformerArchitecture|Transformer]] workloads and then need topology, optical switching, and [[XLACompiler|compiler]] adaptation when sparse routing becomes important. Later 3D Torus and configurable switching are presented as attempts to make TPU more MoE-friendly.

[[147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]] adds a model-training engineering case from [[AntLingbo|蚂蚁灵波]]. [[ShenYujun|沈宇军]] says the team failed dozens of times over roughly two months before balancing expert activation in its video-model work, making MoE a practical training-stability problem rather than only a sparse-parameter efficiency idea.

## Key Claims
- MoE changes the communication pattern as much as the arithmetic pattern.
- All-to-all expert routing can make [[AIClusterNetworking]] a first-order model-performance issue.
- Specialized hardware can adapt to architecture shifts, but only if the shift remains close enough to existing workload assumptions.
- MoE therefore links model design to [[TPUPodSystemOptimization]], not only to parameter counts or benchmark scores.
- In the Ant Lingbo source, MoE also links architecture design to training convergence and expert-load balancing inside robot-adjacent video modeling.

## Connections
- [[TPU]], [[TPUPodSystemOptimization]], and [[XLACompiler]] — source hardware/software context.
- [[TransformerArchitecture]], [[DeepSeek]], and [[Gemini]] — model-family context.
- [[AIClusterNetworking]], [[AIChipSpecialization]], and [[ASICWorkloadPredictionRisk]] — infrastructure and prediction-risk frame.
- [[AntLingbo]], [[ShenYujun]], [[WorldActionModels]], and [[EmbodiedNativeFoundationModels]] — embodied-model engineering context added by episode 147.
