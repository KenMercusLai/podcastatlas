---
title: "Video Models"
type: concept
tags: [video, generative-ai, content]
sources: [all-in-with-chamath-jason-sacks-friedberg-open-source-wins-agi-is-here-and-scorseses-ai-toolkit-with-ceos-of-cerebras-black-forest-labs-42029880, zhizhuxia-xinpian-naxia-jinban-guonei-piaofang-ai-moxing-baofa-jiagezhan-1004403588, duihua-liblib-chenmian-guanyu-huoxialai-yiji-suoyou-jiejin-siwang-de-shike-1-175-1, kuai-yidian-zai-kuai-yidian-kuai-dao-shijie-neng-shishi-shengcheng-he-shengshu-keji-zhang-jintao-liao-vidu-s1-tuili-jiasu-shishi-jiaohu-shipin-lsb53bqrjojiadnlq2qe4sta-b13, e234-weilai-shipai-dianying-hai-cunzai-ma-yu-daoyan-luchuan-liaoliao-ai-gei-yingshiren-de-kongju-yu-ziyou-b2be7093-3366-4ee2-8a7a-625f06206ae5, tech-20251215-1215-mp-tech-pod-128-tech-20251215-1215-mp-tech-pod-128, 263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs, gaoshou-zenme-yong-ai-putongren-zenme-xue-ai-touziren-ruhe-tou-ai-duitan-kedaibiao-lizheng-ljqyo4tz0o2-pmsl-mjx6umsuzsc, cong-qq-huiyuan-dao-doubao-baoyue-zhongguoren-weishenme-zong-juede-ruanjian-gai-mianfei-keji-luandun, bootstrapped-saas-12m-arr-across-5-products-with-a-team-of-10, na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr, 2026-ai-youxi-quanjing-saomiao-si-ceng-tujing-san-da-wuqu-yi-ge-gongshi-quekou-duitan-405-youju-xiaoning-lgk71gytqtsvkc-wipz0hkzkemne, vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1, zhili-bianzhi-de-chunjie-jianwenlu-yu-nachang-zhengzai-yunniang-de-youdai-weiji-1, 266-cong-hongguo-dao-ai-duanju-shui-zai-ge-shui-de-ming-lgzf6bu7bfalr5qvnhlfzkufahob, cong-yangshi-jilupian-dao-baokuan-ai-duanju-di-yi-pi-zhuanshen-de-daoyan-s10e11-3c05e3d5-d8f6-44c1-97ca-698261d7b2bc]
last_updated: 2026-08-20
---

# Video Models

[[all-in-with-chamath-jason-sacks-friedberg-open-source-wins-agi-is-here-and-scorseses-ai-toolkit-with-ceos-of-cerebras-black-forest-labs-42029880]] adds [[BlackForestLabs|Black Forest Labs]]' visual-model roadmap through [[RobinRombach|Robin Rombach]]. The source moves from [[StableDiffusion|Stable Diffusion]], [[LatentDiffusion|latent diffusion]], and [[Flux]] into multimodal models trained on images, video, and audio, then toward action prediction and [[WorldModels|world models]].

Video models are discussed as an investment and content-production theme. The host argues that improvements in AI video generation could let ordinary people express creative ideas more easily, enable new narrative formats, and produce a content-side productivity revolution.

[[zhizhuxia-xinpian-naxia-jinban-guonei-piaofang-ai-moxing-baofa-jiagezhan-1004403588]] adds a price-and-duration competition snapshot. The source says [[ByteDance]]'s C-DANCE 2.5 can generate 30-second clips and support continued extension, while [[MiniMax]] H3 can generate 15-second stereo video at roughly half the price of similar products.

[[duihua-liblib-chenmian-guanyu-huoxialai-yiji-suoyou-jiejin-siwang-de-shike-1-175-1]] adds the downstream product-strategy layer through [[LibTV]]. In this source, the important question is not only whether video models improve, but whether a creative application can price generated video, package the workflow, survive API-cost comparisons, and build enough user value before model providers or copycats compress the category.

[[kuai-yidian-zai-kuai-yidian-kuai-dao-shijie-neng-shishi-shengcheng-he-shengshu-keji-zhang-jintao-liao-vidu-s1-tuili-jiasu-shishi-jiaohu-shipin-lsb53bqrjojiadnlq2qe4sta-b13]] adds [[ViduS1]] as a real-time branch of the category. [[ZhangJintao]] distinguishes offline clip generation from [[StreamingVideoGeneration]]: the model must generate frames faster than playback, preserve long-session consistency, and respond to live user input through [[RealTimeInteractiveVideoGeneration]].

In [[cong-qq-huiyuan-dao-doubao-baoyue-zhongguoren-weishenme-zong-juede-ruanjian-gai-mianfei-keji-luandun]], video generation is also treated as a possible paid-feature wedge for [[Doubao]]. The hosts argue that [[ByteDance]]'s video data and product background may make video a stronger Doubao capability than general text, image, or API use.

[[bootstrapped-saas-12m-arr-across-5-products-with-a-team-of-10]] adds a SaaS product case through [[Revid]], an AI video creation and editing tool that [[ThibautLouisLucas]] says became [[TeaMaker]]'s most successful product.

[[na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr]] adds video models as one technical route toward [[WorldModels]]. [[HuangBiwei]] treats video generation and video-rich [[WorldActionModels]] as useful inputs, but argues that rendered plausibility is not the same as causal understanding of physical variables, structures, and state transitions.

[[tech-20251215-1215-mp-tech-pod-128-tech-20251215-1215-mp-tech-pod-128]] adds [[GaryMarcus]]'s version of that caution. Marcus says video prediction can be a step beyond language-only scaling, but pixel-level prediction still falls short when generated scenes produce physically strange outputs such as unstable extra limbs. In the wiki, this reinforces the distinction between watchable video and [[WorldModels]] that track entities, state, action, and causation.

[[2026-ai-youxi-quanjing-saomiao-si-ceng-tujing-san-da-wuqu-yi-ge-gongshi-quekou-duitan-405-youju-xiaoning-lgk71gytqtsvkc-wipz0hkzkemne]] adds an interactive-entertainment view. [[Xiaoning]] argues that AI short video and AI video-first formats may move faster than interactive games because generated video only has to be watchable, while games must remain stable interactive systems. The source links [[YORO]] and Seedance-like capabilities to possible interactive film/game experiments, but still treats [[AIGameIndustrialization]] as the harder layer.

[[vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1]] adds a fresh [[Seedance]] 2.0 case. The hosts highlight clarity, cinematic feel, camera movement, and overseas demand, while noting that famous characters, voices, likenesses, and IP recreation quickly create copyright and rights risks.

[[zhili-bianzhi-de-chunjie-jianwenlu-yu-nachang-zhengzai-yunniang-de-youdai-weiji-1]] adds an earlier production-cost interpretation. The hosts use ByteDance video generation, AI short dramas, AI ads, and movie-shot examples to argue that video models are moving from mockups toward direct content production, which pressures filming, advertising, and some creative labor while making direction and rights handling more important.

[[266-cong-hongguo-dao-ai-duanju-shui-zai-ge-shui-de-ming-lgzf6bu7bfalr5qvnhlfzkufahob]] adds the operating-market version. Video models are valuable when they fit [[AIVideoProductionWorkflow]] and [[ShortDramaEconomics]]: scripts, prompts, image generation, repeated draws, editing, platform feedback, and ad distribution turn model output into [[AIShortDrama]] rather than isolated demos.

[[cong-yangshi-jilupian-dao-baokuan-ai-duanju-di-yi-pi-zhuanshen-de-daoyan-s10e11-3c05e3d5-d8f6-44c1-97ca-698261d7b2bc]] adds a creator-comparison view across model tools. [[Chouxiangzai]] says C-DANCE/[[Seedance]] is stronger for instruction following, multi-reference consistency, and unexpected physical detail, while other tools can still win on 4K texture, image generation, or specific case needs. The source's practical point is that model quality becomes useful only when folded into [[AIDirectorCoreWorkflow]] and project-specific shot requirements.

[[e234-weilai-shipai-dianying-hai-cunzai-ma-yu-daoyan-luchuan-liaoliao-ai-gei-yingshiren-de-kongju-yu-ziyou-b2be7093-3366-4ee2-8a7a-625f06206ae5]] adds the professional film boundary through [[LuChuan]]. The episode says video models can dramatically accelerate visual-effects previsualization and keyframe ideation, but feature films need [[IndustrialGradeFilmModels]], director judgment, rights clearance, and decisions about [[LiveActionFilmUnderAI]] rather than only impressive generated clips.

[[263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs]] adds a product-strategy caution through [[Sora]], [[Meitu]], and [[Jianying]]. The source argues that stronger video generation alone does not guarantee a durable app or platform: quality, cost, workflow fit, editing control, and vertical use cases decide whether video models become usable products.

## Source Notes
- The episode mentions commercial signals from products such as Kling and [[Seedance]], plus a case called Zombie Cleaner.
- The host resists dismissing short-drama-style content, arguing that popular content can still have value.
- The theme connects to the episode's broader [[SecondRenaissance]] idea.
- Doubao's video model is presented as a more plausible paid value area than undifferentiated chatbot functions.
- Revid shows AI video as a revenue-generating SaaS category when paired with [[DistributionLedProductBuilding]].
- In the Aether AI source, video models help with world-model learning but remain incomplete without [[CausalWorldModels]].
- In the AI interactive entertainment source, video-first content is expected to mature before fully interactive AI games because video has fewer system-design and retention constraints.
- Vol. 162 adds that better video generation can raise the value of creative direction while making repetitive style copying and rights enforcement more urgent.
- The Keji Luandun source connects better video generation to [[IntelligenceDevaluation]] because production skill and cost structures may be repriced.
- The Luanfanshu source adds that video-model products still need [[AIApplicationLayerMoat]] and [[VerticalWorkflowAI]] when users require reliable final output rather than impressive samples.
- Episode 266 adds AI short drama as a production market where generation cost, creator workflow, paid traffic, and copyright control decide whether model capability becomes revenue.
- The What's Next source adds a model-selection view: creators choose among video and image tools by shot need, consistency, texture, instruction following, and cost rather than assuming one universal model.
- E234 adds film-grade constraints: previs speed matters, but long-form delivery still needs continuity, aesthetic control, legal rights, and a live-action-versus-generation decision.
- The Marketplace Tech world-model episode adds that video prediction can remain a pixel-sequence method unless it learns stable physical structure and causal state.
- The Vidu S1 source adds that video-model quality is not the only product metric; frame rate, latency, long-session coherence, video understanding, and per-minute serving cost matter when generated video becomes interactive.
- The same source gives a China-video-model explanation based on visual-entertainment data quantity, data quality, preference alignment, and short-video/livestream-commerce ecosystems.
- The LateTalk Lib TV source adds that video-model applications are judged by subscription economics, launch timing, workflow packaging, and margin assumptions, not only by model output quality.
- The 声动早咖啡 source adds that video models are becoming a clearer commercialization lane, but one where price, clip length, audio, editing, and short-drama workflow adoption are now direct competitive variables.
- The All-In Black Forest Labs source adds that video models can be a bridge between media generation and action prediction, but high-end film still needs continuity, control, and rights-safe workflows.

## Connections
- [[WorldModels]] — adjacent model direction for richer scene and environment representation.
- [[VoiceInteraction]] — another interaction/content frontier discussed by the host.
- [[Doubao]] and [[ByteDance]] — product and company case for video-model monetization.
- [[Revid]] and [[TeaMaker]] — SaaS product and company case for AI video tooling.
- [[ProductLedWillingnessToPay]] — pricing depends on whether video capability feels differentiated.
- [[WorldActionModels]] and [[CausalWorldModels]] — world-model routes that absorb video data but differ in causal grounding.
- [[GaryMarcus]] and [[LLMWorldModelGap]] — critique that plausible video prediction is not yet robust world understanding.
- [[YORO]], [[AIInteractiveEntertainment]], and [[AIInteractiveContentPlatforms]] — interactive video and platform directions from the Youju crossover.
- [[ByteDance]], [[Seedance]], [[AIContentProvenance]], and [[AIInteractiveEntertainment]] — Seedance 2.0 and rights-risk context added by Vol. 162 and extended by the Keji Luandun source.
- [[Sora]], [[Meitu]], [[Jianying]], and [[AIApplicationLayerMoat]] — application-layer and workflow caution added by Luanfanshu.
- [[AIShortDrama]], [[AIVideoProductionWorkflow]], [[ShortDramaEconomics]], and [[Hongguo]] — short-drama production and distribution branch added by episode 266.
- [[LuChuan]], [[IndustrialGradeFilmModels]], [[LiveActionFilmUnderAI]], and [[CreativeLaborAIBacklash]] — film-production and industry-backlash branch added by E234.
- [[Chouxiangzai]], [[Taitai]], [[Seedance]], and [[AIDirectorCoreWorkflow]] — director-side model-comparison branch added by What's Next.
- [[Vidu]], [[ViduS1]], [[StreamingVideoGeneration]], [[RealTimeInteractiveVideoGeneration]], and [[InferenceAccelerationStack]] — real-time interactive branch added by the Shizilukou Crossing source.
- [[LibTV]], [[Evoken]], [[Seedance]], [[AISubscriptionEconomics]], and [[AIApplicationSurvivalStrategy]] — downstream video-creation application and pricing branch added by LateTalk.
- [[MiniMax]], [[Seedance]], [[ByteDance]], [[Sora]], and [[AIInferenceCostStructure]] - price, duration, and commercial-usage branch added by 声动早咖啡.
- [[BlackForestLabs|Black Forest Labs]], [[RobinRombach]], [[Flux]], [[GenerativeMediaControlLayers]], [[MartinScorsese]], and [[IPControlledGenerativeModels]] - All-In visual-model and creative-control branch.
