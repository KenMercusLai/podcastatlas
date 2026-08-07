---
title: "Mixture of Experts"
type: concept
tags: [ai, model-architecture, infrastructure, semiconductors]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1, yao-shunyu-laidao-tengxun-300tian-1-176-1, 148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims, e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149, 147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]
last_updated: 2026-08-08
---

# Mixture of Experts

[[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] adds [[KimiK3|Kimi K3]] as a large sparse-MoE routing case. The source says K3 routes each token to a small subset of experts from a very large pool, making load balance a training-stability problem. [[QuantileBalancing]] is presented as K3's answer to the quality-versus-balance tradeoff in auxiliary losses and the tuning burden in fixed-step bias updates.

[[yao-shunyu-laidao-tengxun-300tian-1-176-1]] adds MoE as part of Tencent's model-scale and organization discussion. The source frames Hunyuan 3 as a roughly 300B MoE model and says [[WeChatVLM]] had a 258B MoE model for WeChat-internal use, making MoE a marker of both architecture choice and duplicated internal model investment inside [[Tencent]].

Mixture of Experts is the model-architecture pattern discussed in [[e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149]] through its impact on [[TPU]] topology. [[HenryTPUEngineer|Henry]] says earlier TPU generations struggled with MoE because expert routing requires all-to-all communication, while older 2D Torus layouts mostly connected neighboring chips.

The source treats MoE as a practical example of [[ASICWorkloadPredictionRisk]]. A chip family can be well suited to dense [[TransformerArchitecture|Transformer]] workloads and then need topology, optical switching, and [[XLACompiler|compiler]] adaptation when sparse routing becomes important. Later 3D Torus and configurable switching are presented as attempts to make TPU more MoE-friendly.

[[147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]] adds a model-training engineering case from [[AntLingbo|蚂蚁灵波]]. [[ShenYujun|沈宇军]] says the team failed dozens of times over roughly two months before balancing expert activation in its video-model work, making MoE a practical training-stability problem rather than only a sparse-parameter efficiency idea.

[[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]] adds the inference-engine version through [[VLLM|vLLM]] and [[DeepSeek]]. [[YuKaichao|游凯超]] frames MoE as a serving challenge around fine-grained experts, dynamic routing, expert parallelism, and communication, making it a direct case for [[ModelInfraCoDesign]] rather than only a model-architecture choice.

## Key Claims
- MoE changes the communication pattern as much as the arithmetic pattern.
- All-to-all expert routing can make [[AIClusterNetworking]] a first-order model-performance issue.
- Specialized hardware can adapt to architecture shifts, but only if the shift remains close enough to existing workload assumptions.
- MoE therefore links model design to [[TPUPodSystemOptimization]], not only to parameter counts or benchmark scores.
- In the Ant Lingbo source, MoE also links architecture design to training convergence and expert-load balancing inside robot-adjacent video modeling.
- In the vLLM source, MoE also links open-model support to inference-engine scheduling, communication, and deployment complexity.
- In the Tencent source, MoE also becomes an organizational cost question because Hunyuan and WeChat can each pursue sparse large models under limited compute.
- In the K3 source, MoE also becomes a routing-statistics problem because extreme sparsity makes expert-load balance central to successful scale-up.

## Connections
- [[TPU]], [[TPUPodSystemOptimization]], and [[XLACompiler]] — source hardware/software context.
- [[TransformerArchitecture]], [[DeepSeek]], and [[Gemini]] — model-family context.
- [[AIClusterNetworking]], [[AIChipSpecialization]], and [[ASICWorkloadPredictionRisk]] — infrastructure and prediction-risk frame.
- [[AntLingbo]], [[ShenYujun]], [[WorldActionModels]], and [[EmbodiedNativeFoundationModels]] — embodied-model engineering context added by episode 147.
- [[VLLM|vLLM]], [[YuKaichao|游凯超]], [[DeepSeek]], and [[ModelInfraCoDesign]] — inference-engine co-design context added by episode 148.
- [[TencentHunyuan]], [[WeChatVLM]], [[YaoShunyu]], and [[FederatedAIOrganization]] — Tencent model-organization context added by LateTalk episode 176.
- [[KimiK3]], [[QuantileBalancing]], [[ZengZhiyuan]], and [[ModelInfraCoDesign]] — K3 expert-routing branch added by LateTalk episode 177.
