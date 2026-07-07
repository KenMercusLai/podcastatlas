---
title: "133. 对谢赛宁的7小时马拉松访谈：世界模型、逃出硅谷、AMI Labs、两次拒绝Ilya、杨立昆、李飞飞和42"
type: source
tags: [podcast, ai, world-models, research, startups]
sources: []
date: 2026-03-16
source_file: "/home/ken/repos/podcastatlas/content/episodes/133. 对谢赛宁的7小时马拉松访谈：世界模型、逃出硅谷、AMI Labs、两次拒绝Ilya、杨立昆、李飞飞和42 [lqXBPXddXfukbdlAP-NDrFNp-2wn].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/69b77577f8b8079bfa8eb837"
last_updated: 2026-07-08
---

## Summary
This [[ZhangXiaojunCommercialInterviews]] episode is a long interview with [[XieSaining]] about his path from Shanghai Jiao Tong ACM training, [[UCSD]], [[FAIR]], and [[NYU]] into co-founding [[AMILabs]] with [[YannLeCun]]. The technical through-line is [[RepresentationLearning]]: visual recognition, [[SelfSupervisedLearning]], [[ResNeXt]], [[DiffusionTransformers]], REPA/RAE-style representation alignment, [[MultimodalIntelligence]], and eventually [[WorldModels]]. The startup argument is that LLMs are important but insufficient as a route to human-level intelligence, so AMI should build predictive, memory-bearing, controllable world models through real-world data partnerships rather than only scaling internet text.

## Key Claims
- [[XieSaining]] presents his career as a sequence of non-linear choices: choosing computer vision because he cared about it, going to NUS when Microsoft Research Asia did not have a suitable undergraduate vision slot, choosing [[UCSD]] despite ranking anxiety, joining [[FAIR]] for the visual-research culture, then moving to [[NYU]] partly because of [[YannLeCun]] and New York's intellectual environment.
- The episode treats [[RepresentationLearning]] as Xie's durable research trunk. Image recognition, segmentation, video, embodied RL, [[SelfSupervisedLearning]], [[DiffusionTransformers]], REPA, RAE, and [[WorldModels]] are framed as branches of the same problem: learning useful abstractions from data.
- [[KaimingHe]] is presented as a major methodological influence: strong baselines, scalable models, engineering depth, predicting experiment results before running them, and using failed expectations as research signal.
- [[FeiFeiLi]] is presented as influential because [[ImageNet]] did not merely collect data; it defined image classification clearly enough for deep learning to have a tractable arena.
- Xie says he rejected [[OpenAI]] in 2018 because [[FAIR]] had the computer-vision researchers he wanted to work with, then rejected [[IlyaSutskever]] again in 2024 after SSI was founded because his own route had shifted toward world models at [[NYU]].
- The source argues that language models are not pure self-supervised learning in the ordinary sense, because language already compresses human interpretation of the world into token labels.
- Xie argues that language is a powerful interface, but not the whole world and not the only form of thought, decision, or action; this qualifies stronger [[LanguageUserInterface]] claims.
- [[WorldModels]] are defined as systems that learn a transition or prediction function from state plus action/intervention to next state, with abstraction, memory, reasoning, planning, counterfactual or causal inference, controllability, and safety.
- Xie rejects simply tokenizing video frames for LLMs because that flattens continuous physical reality into long sequences rather than learning the right representations and dynamics.
- [[AMILabs]] is presented as a "reverse OpenAI" strategy: instead of downloading internet data, training a foundation model, and pushing it outward, the company wants to form real-world partnerships with people who have problems, data, and deployment contexts.
- The episode frames AMI's organization as neither pure research lab nor closed frontier-model company: it needs a business model, but also wants research openness, credit assignment, and visibility for young researchers.
- The AMI route creates a productive tension with [[CausalWorldModels]]: both reject pure generative realism, but Xie's source emphasizes predictive representation, JEPA-style architecture, real-world partners, and decentralized data loops more than an explicitly causal-variable program.

## Key Quotes
> "LM 不会死，但会 fade away" — Xie's shorthand for treating language models as important tools rather than the final intelligence substrate.

> "反向 OpenAI" — the source's description of [[AMILabs]] building from real-world partners and data instead of only from internet-scale model pretraining.

> "质疑 JEPA、理解 JEPA、成为 JEPA" — Xie's summary of his shift toward [[JointEmbeddingPredictiveArchitecture]] as a broader cognitive architecture.

> "定义问题" — recurring research theme connecting [[FeiFeiLi]], [[ImageNet]], and [[ProblemDefinitionInResearch]].

## Connections
- [[XieSaining]], [[AMILabs]], [[YannLeCun]], [[NYU]], and [[FAIR]] — person, company, collaborator, university context, and earlier research lab.
- [[KaimingHe]], [[FeiFeiLi]], [[IlyaSutskever]], and [[OpenAI]] — major research influences and alternative career-route figures.
- [[RepresentationLearning]], [[SelfSupervisedLearning]], [[ResearchTaste]], and [[ProblemDefinitionInResearch]] — research-method spine of the interview.
- [[ResNeXt]], [[ImageNet]], [[DiffusionTransformers]], and [[JointEmbeddingPredictiveArchitecture]] — architecture, dataset, diffusion, and predictive-model milestones discussed in the source.
- [[WorldModels]], [[MultimodalIntelligence]], [[LanguageUserInterface]], [[VideoModels]], [[EmbodiedAI]], and [[CausalWorldModels]] — technical context for moving beyond text-only systems.
- [[DecentralizedWorldModelStrategy]], [[AIOrganizationDesign]], [[AIPlusTerminals]], [[AICommercializationPressure]], and [[FrontierModelScaling]] — startup, organization, terminal, commercialization, and scaling themes.

## Contradictions
- No direct contradiction with prior wiki content. The source reinforces existing [[WorldModels]] and [[EmbodiedAI]] material while adding a broader research-program and organization-design route through [[AMILabs]].
- The source qualifies earlier [[LanguageUserInterface]] and LLM-centered agent narratives: language remains a powerful interface, but the source argues it should not be mistaken for the whole substrate of intelligence.
- The source creates route-level tension with [[AetherAI]]'s [[CausalWorldModels]] framing: AMI emphasizes predictive representation, JEPA-style architecture, and partner data loops, while Aether AI emphasizes causal variables and structures for robotics. The difference is a technical emphasis, not an explicit contradiction.
