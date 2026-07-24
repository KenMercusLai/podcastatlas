---
title: "Discovery Model"
type: concept
tags: [ai, science, research]
sources: [ai4s-xuyao-kuangren-yu-yexinjia-duihua-yinglingdian-odin-ruguo-shen-cunzai-wo-zenneng-rongren-ziji-bushi-shen-gonglu-boke-lhceyip6dqomrwk38uvqjwoomxyz, e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]
last_updated: 2026-07-24
---

# Discovery Model

A discovery model is the source's name for an AI system that can propose new hypotheses and verify whether they hold. In [[e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]], [[Apodex]] uses this frame to distinguish itself from generative chat, image, or video products: the goal is not only to answer questions, but to solve hard scientific and technical problems.

The episode argues that the hard part is not producing a plausible hypothesis. A useful [[DiscoveryModel]] has to find questions humans have not already written down, search and reason across evidence, use code or simulation when possible, and pass [[AIVerification]]. For open scientific domains, it also needs [[ResearchTaste]]: the ability to prefer fundamental problems over shallow or merely publishable ones.

[[ai4s-xuyao-kuangren-yu-yexinjia-duihua-yinglingdian-odin-ruguo-shen-cunzai-wo-zenneng-rongren-ziji-bushi-shen-gonglu-boke-lhceyip6dqomrwk38uvqjwoomxyz]] adds a wet-lab-facing version through [[YinglingdianAI]]. [[HaotianOdin]]'s [[ScientificDiscoveryAutomation]] goal is to automate data analysis, hypothesis formation, and path search in biological discovery, but the source also shows why discovery models need [[DomainExpertAlignment]] and experiment: molecular candidates are not scientific progress until they survive synthesis, binding, measurement, and application constraints.

## Key Claims
- Discovery requires novelty, but novelty without verification is not enough.
- Out-of-distribution hypotheses are especially hard because the model cannot simply retrieve the training-set answer.
- [[DeepResearch]] is a stepping stone because search, planning, and synthesis are needed before a model can make scientific proposals.
- Code, simulation, formal math, and agent-team critique are all possible verification surfaces.
- Top-scientist feedback is treated as a scarce post-training signal for teaching problem choice and research taste.

## Connections
- [[Apodex]], [[ChenTianqiao]], [[DuShaolei]], and [[LiBeibin]] — company and people attached to the concept in the source.
- [[AIForScience]], [[AIMaterialsDiscovery]], and [[CausalAI]] — adjacent scientific AI themes in the wiki.
- [[ResearchTaste]] and [[ProblemDefinitionInResearch]] — judgment about which scientific questions matter.
- [[RecursiveSelfImprovement]], [[DeepResearch]], and [[AIVerification]] — technical loop needed for discovery rather than answer generation.
- [[YinglingdianAI]], [[AllModalMolecularWorldModel]], [[AIDrugDiscoveryPlatform]], and [[ScientificDiscoveryAutomation]] — biological discovery branch added by the Shizilukou Crossing source.
