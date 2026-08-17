---
title: "AI Verification"
type: concept
tags: [ai, verification, safety, agents]
sources: [ep-6-data-science-ai-talk, ep-4-a-i-talk-with-a-rocket-scientist-from-nasa, data-ai-and-scientific-research-a-coffee-chat, yu-tian-yuandong-liao-rsi-moxing-zi-jinhua-ruhe-daolai-1-178-1, jia-yangqing-wo-suo-jingli-de-rengongzhineng-yisi-dao-ai-dianfu-shijie-de-shunian-jubian-chuantai-shengdongjixi-s10e24-a3884ade-4669-4d5c-ab2e-f98aa580f429, tech-20260805-0805-mp-tech-pod-128-tech-20260805-0805-mp-tech-pod-128, e227-meiguo-yiliao-shichang-ai-zhengduozhan-jutou-yazhu-chuangye-gongsi-neng-ying-ma-f14f8686-a6e2-47ea-92c1-ca7e71199f67, e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di, 137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb]
last_updated: 2026-08-18
---

# AI Verification

[[yu-tian-yuandong-liao-rsi-moxing-zi-jinhua-ruhe-daolai-1-178-1]] adds [[TianYuandong|田渊栋]]'s low-level RSI examples. NanoChat speed runs and operator optimization matter because they provide relatively clear metrics; the source implies that [[RecursiveSelfImprovement]] will be much harder in domains where the verifier cannot tell whether a research direction is genuinely better.

[[jia-yangqing-wo-suo-jingli-de-rengongzhineng-yisi-dao-ai-dianfu-shijie-de-shunian-jubian-chuantai-shengdongjixi-s10e24-a3884ade-4669-4d5c-ab2e-f98aa580f429]] adds the agent-reliability version through [[JiaYangqing|Jia Yangqing]]. The source argues that multi-agent systems still need external checks: writer and reviewer agents can agree on incomplete work unless a harness, task criterion, or human reviewer can verify the result.

AI verification is the broader problem of checking whether an AI-generated answer, hypothesis, tool action, training example, or self-improvement step is correct enough to use. [[e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]] makes verification the central constraint on [[RecursiveSelfImprovement]] and [[DiscoveryModel]] work.

The source separates easy-to-check domains from judgment-heavy domains. Code and math can use execution, tests, and formal proof tools, but even code can fail when tests are too broad, too narrow, or written to reward the wrong behavior. For open-ended scientific and research problems, [[Apodex]] uses agent teams: one agent or group proposes, another verifies, redundant agents compare answers, and the system learns which information sources deserve trust.

[[137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb]] adds the formal-math version through [[HongLetong]] and [[Axiom]]. In this source, [[LeanTheoremProver]], [[Mathlib]], and [[InteractiveTheoremProving]] provide a stronger verifier than ordinary tests because proofs become machine-checkable artifacts. The limitation shifts toward [[AutoFormalization]] and [[FormalSpecification]]: the system can verify a proof only after the mathematical or software target has been stated precisely.

[[e227-meiguo-yiliao-shichang-ai-zhengduozhan-jutou-yazhu-chuangye-gongsi-neng-ying-ma-f14f8686-a6e2-47ea-92c1-ca7e71199f67]] adds the medical-conversation version through [[HealthBench]]. The benchmark moves evaluation beyond exam-style questions toward clinician-scored conversations, where the system must manage uncertainty, follow-up, evidence quality, multilingual communication, and [[HumanJudgmentUnderAI]].

[[tech-20260805-0805-mp-tech-pod-128-tech-20260805-0805-mp-tech-pod-128]] adds the legal and tax version through [[BenjaminAlarie]]. In his account, accuracy is only one part of responsible legal AI; systems also need [[LegalAIVerificationAuditability]] so professionals can check answers, identify mistakes, and improve legal judgment or advocacy before relying on generated output.

[[data-ai-and-scientific-research-a-coffee-chat]] adds the experimental-science version. [[MossamDataScienceWithSam|Mossam]] says chemistry outputs need molecular verification through laboratory instruments and reproducible synthesis, while [[EffieDataScienceWithSam|Effie]] emphasizes blinding, randomization, protocol records, and biological quality control. This makes [[ExperimentalScienceDataQuality]] a verifier input, not just background documentation.

[[ep-6-data-science-ai-talk]] adds the AI-for-neuroscience version through [[PaulinaNemkova|Paulina Nemkova]]'s [[EEGBrainReading]] project. The source makes [[ResearchReplicationIntegrity]] the verification boundary: the team begins by replicating related [[StanfordUniversity|Stanford]] work, keeps current with research literature, and distinguishes object-category EEG classification from full thought prediction.

[[ep-4-a-i-talk-with-a-rocket-scientist-from-nasa]] adds the spaceflight version through [[KofiBrowning]]. In that source, verification is constrained by [[SpaceflightAIDatasetScarcity]] and safety stakes: [[SpaceImageryAI]] can help triage visual review, and [[EVAGloveInspectionAI]] can support mission-control inspection, but human reviewers still need to catch rare damage, model blind spots, and [[AIModelBiasGovernance|bias]] problems.

## Key Claims
- Verification errors can compound across recursive self-improvement loops.
- Code and math are attractive early domains because they have stronger external checkers than ordinary prose.
- Tests are not automatically reliable; a model can pass weak tests while still solving the wrong problem.
- Multi-agent review can reduce single-agent drift, but it still needs source-quality judgment and human oversight.
- Reward hacking is a verification failure: the model optimizes the proxy rather than the human need.
- Scientific discovery needs verification and taste together, because a true but trivial result may still be the wrong target.
- Formal proof can give AI systems a stronger correctness signal than prose, but only when the target statement is correctly formalized.
- [[AIForMath]] is attractive because mathematics provides a cleaner digital sandbox for verification than many physical science domains.
- Medical AI verification needs scenario-based review, source grounding, and clinician judgment because correct-looking prose can still fail in patient-specific context.
- Legal AI verification needs auditability and professional review because plausible case law, tax analysis, or legal advice can create real liability when wrong.
- Tian's source adds that low-order RSI is more credible when the task has cheap, strong, hard-to-game metrics; higher-order discovery still needs taste and interpretability as part of verification.
- Data Science With Sam adds that wet-lab verification can be slow, instrument-mediated, and safety-constrained, especially when negative results or radioactive chemistry are involved.
- Data Science With Sam EP6 adds that brain-signal classification needs replication and scope discipline because public interpretations can outrun what the model actually predicts.
- The NASA episode adds that spaceflight verification may be data-scarce, visually bounded, and safety-critical, making human review necessary even when the model is useful.

## Connections
- [[AICodingVerification]] — software-specific verification branch already tracked in the wiki.
- [[MultiAgentCollaboration]] — agent-team checking pattern used in the source.
- [[RecursiveSelfImprovement]] and [[DiscoveryModel]] — high-stakes loops that depend on verification.
- [[ResearchTaste]], [[HumanJudgmentUnderAI]], and [[DomainExpertAlignment]] — human standards that keep verification grounded.
- [[HealthBench]], [[EvidenceGroundedMedicalRAG]], and [[HIPAAConstrainedMedicalAI]] — medical AI evaluation, evidence, and compliance branch added by E227.
- [[AIForMath]], [[AxiomProver]], [[AutoFormalization]], and [[FormalSpecification]] — formal-math verifier branch added by episode 137.
- [[LegalAIVerificationAuditability]], [[LegalAIHallucination]], and [[HumanInTheLoopLegalAI]] - legal and tax verification branch added by Marketplace Tech.
- [[TianYuandong]], [[AIResearchFeedbackCompression]], [[MLCoding]], and [[ResearchTaste]] — LateTalk episode 178's research-loop verification branch.
- [[ExperimentalScienceDataQuality]], [[NegativeResultsAsScientificData]], [[RetrosynthesisAI]], [[BloodBrainBarrierPrediction]], and [[RadiochemistryImagingTracers]] - experimental-science verification branch added by Data Science With Sam.
- [[PaulinaNemkova]], [[EEGBrainReading]], [[ResearchReplicationIntegrity]], [[AIResearchLiteratureCurrency]], and [[LockedInSyndromeAssistiveCommunication]] - AI-for-neuroscience verification branch added by EP6.
- [[KofiBrowning]], [[SpaceflightAIDatasetScarcity]], [[SpaceImageryAI]], [[EVAGloveInspectionAI]], and [[AIModelBiasGovernance]] - spaceflight verification branch added by Data Science With Sam.
