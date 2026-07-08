---
title: "Research Taste"
type: concept
tags: [research, ai, methodology]
sources: [133-dui-xie-saining-de-7-xiaoshi-ma-la-song-fangtan-shijie-moxing-taochu-guigu-ami-labs-liangci-jujue-ilya-yang-likun-li-feifei-he-42, e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di, 140-dui-yao-shunyu-de-4-xiaoshi-fangtan-qing-yunxu-wo-xiao-feng-yixia-zai-anthropic-he-gemini-xun-moxing-jishu-yuce-yingxiongzhuyi-yi-guoqu-ll7qiciwwgfssorhr4yy-uuqae8h, 138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]
last_updated: 2026-07-08
---

# Research Taste

Research taste is the interview's term for the judgment that lets a researcher choose problems, run useful experiments, read the field, pivot, and present work coherently. In [[133-dui-xie-saining-de-7-xiaoshi-ma-la-song-fangtan-shijie-moxing-taochu-guigu-ami-labs-liangci-jujue-ilya-yang-likun-li-feifei-he-42]], [[XieSaining]] uses [[KaimingHe]] as the clearest example.

[[e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]] turns research taste into a training target for [[DiscoveryModel]] systems. [[DuShaolei]] argues that a scientific model needs to learn from top scientists which questions are fundamental, not merely which answers are fluent or publishable. [[LiBeibin]] adds that current models still have weaker taste than ordinary AI scientists, so human experts remain part of the [[RecursiveSelfImprovement]] loop.

[[140-dui-yao-shunyu-de-4-xiaoshi-fangtan-qing-yunxu-wo-xiao-feng-yixia-zai-anthropic-he-gemini-xun-moxing-jishu-yuce-yingxiongzhuyi-yi-guoqu-ll7qiciwwgfssorhr4yy-uuqae8h]] adds a systems version through [[YaoShunyu]]. His physics-to-AI path makes research taste less about lone brilliance and more about choosing objective, feedback-rich problems; designing experiments that rule out bugs and false assumptions; and taking responsibility for how local work affects the full training system.

[[138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]] adds [[LuoFuli]]'s acceleration version. When [[OpenClaw]]-style agents can turn ideas into code and evaluations much faster, taste shifts toward selecting which ideas deserve cards, identifying whether a failure is real or infrastructural, and using parallel agents without drowning in shallow experiments.

## Key Claims
- Good ideas rarely arrive from sitting still and thinking abstractly; they come from input, exploration, engineering, reading, and abstraction.
- Predicting experiment results before running them makes surprises meaningful: a wrong prediction can be a better signal than a small expected gain.
- Strong baselines and infrastructure matter because weak baselines can make shallow improvements look like research.
- Good research often pivots through difficulty and only later gets narrated as a straight line.
- Taste includes presentation, figures, websites, video, and storytelling, not only the technical trick.
- For scientific AI, taste includes knowing which hypotheses deserve verification and which questions are too shallow to spend scarce compute or expert time on.
- Expert preference data may matter disproportionately in post-training because the signal is about standards and problem choice rather than broad factual coverage.
- In large-scale model work, taste includes knowing when an experiment failed because the idea was wrong versus because the environment, data, token horizon, or implementation was flawed.
- Reliability can be part of research taste when the work affects a shared training system rather than only an individual paper.
- In agent-accelerated research, taste includes compute triage: deciding which generated ideas deserve [[TrainingComputeAllocation]] and which should be discarded quickly.

## Connections
- [[XieSaining]] and [[KaimingHe]] — source speaker and main exemplar.
- [[RepresentationLearning]], [[SelfSupervisedLearning]], and [[DiffusionTransformers]] — research domains where the method is applied.
- [[ProblemDefinitionInResearch]] — adjacent ability to define what is worth solving.
- [[FAIR]] and [[NYU]] — institutional contexts where research culture is discussed.
- [[AIOrganizationDesign]] — team structure can either preserve or suppress bottom-up research taste.
- [[Apodex]], [[DuShaolei]], [[LiBeibin]], and [[DiscoveryModel]] — source branch where research taste becomes part of training scientific AI.
- [[YaoShunyu]], [[ProblemDefinitionInResearch]], [[FrontierModelScaling]], and [[AIOrganizationDesign]] — systems and reliable-researcher branch added by episode 140.
- [[LuoFuli]], [[AgentPostTraining]], [[TrainingComputeAllocation]], and [[AIOrganizationDesign]] — agent-accelerated research branch added by episode 138.
