---
title: "Human-Driven Scientific AI"
type: concept
tags: [ai-for-science, human-judgment, research-methods, safety]
sources:
  - ep-8-implementation-of-ai-in-scientific-research
  - ep-6-data-science-ai-talk
  - ep-4-a-i-talk-with-a-rocket-scientist-from-nasa
  - data-ai-and-scientific-research-a-coffee-chat
knowledge_schema: synthesis-v1
last_updated: 2026-08-18
---

## Definition
Human-driven scientific AI uses models to prepare data, detect patterns or suggest experiments while domain researchers choose questions, inspect outputs, verify claims and control physical risk.

## Current Synthesis
Across four interviews from [[DataScienceWithSam]], the binding constraint changes by domain: molecular-data representation, sparse spaceflight events, interpretability of EEG categories, and the quality and safety of laboratory records. [[SamDataScienceWithSam]]'s “human-driven” formulation is an editorial stance of the speakers, not a comparative demonstration that all human-in-the-loop designs work.

## Key Claims
- Scientific usefulness begins with fit between data representation and a domain question, not model size alone.
- Incomplete records, missing failed experiments and disciplinary translation gaps limit model suggestions before any physical experiment.
- Candidate synthesis routes and experimental decisions require biological or chemical interpretation, reproducibility and safety review.
- In spaceflight, sparse one-off events favor bounded imagery-review tasks over unconstrained automation.
- Brain-signal classification and assistive ambitions require replication and user validation; predicting an object category is not reading thoughts.

## Evidence
- Data to interpretation: [[ep-8-implementation-of-ai-in-scientific-research]] describes [[LucasSimon]]'s Baylor [[TherapeuticInnovationCenter]] workflow: [[SequencingDataPipeline]] raw reads become a [[GeneExpressionMatrix]] of roughly 20,000 genes; [[ComputationalBiology]] interprets it downstream of [[Bioinformatics]]. [[SingleCellRNASequencing]] changes bulk experiments of hundreds of samples to tens of thousands or up to about a million cells. A [[SingleCellAutoencoderRepresentation]] is meaningful only if its clusters map to cell types or testable biology, not merely a neat visualization.
- Records and experiment selection: [[data-ai-and-scientific-research-a-coffee-chat]] reports [[EffieDataScienceWithSam]]'s concern about [[ExperimentalScienceDataQuality]], SOP deviations, blinding, and the [[BioinformaticsDomainGap]]; the stained-tissue mutant/wild-type clustering example had a blinded developer. [[MossamDataScienceWithSam]] discusses [[RetrosynthesisAI]] and [[NegativeResultsAsScientificData]]: published successes omit many failed reactions; fluorine-18 or carbon-11 [[RadiochemistryImagingTracers]] constrain timing of final labeling, and proposed routes still need chemist review. The episode mentions blind comparisons of routes without an independent accuracy measure. [[BloodBrainBarrierPrediction]] uses lipophilicity, pKa and polar surface area as candidate filters; [[AIExperimentDocumentation]] by cameras remains a proposal.
- Sparse and abundant space data: [[ep-4-a-i-talk-with-a-rocket-scientist-from-nasa]] has [[KofiBrowning]] explain [[SpaceflightAIDatasetScarcity]] at [[NASA]] but contrast it with [[InternationalSpaceStation]] imagery: [[SpaceImageryAI]] can triage uneventful footage. [[EVAGloveInspectionAI]] assists photographed glove review before spacewalks, including an engineer's Microsoft collaboration; mission control remains responsible. Sam's Artemis lunar-rock classification by texture and curvature is a proposed example, not proven flight deployment; [[AIModelBiasGovernance]] also matters when inputs are omitted.
- Assistive validation: [[ep-6-data-science-ai-talk]] describes [[PaulinaNemkova]]'s [[EEGBrainReading]] work at [[UniversityOfNorthTexas]], replicating/extending related Stanford work and classifying thought-about object categories. [[LockedInSyndromeAssistiveCommunication]] motivates the research, but the episode does not establish a deployed communication device; [[ResearchReplicationIntegrity]] and [[AIResearchLiteratureCurrency]] constrain that inference.

## Counterevidence & Qualifications
All four notes are episodes of one show rather than independent trial evidence. [[ScientificDiscoveryAutomation]] may be useful for routine analysis, but neither a route proposed by software nor a visually plausible cluster proves a result. The speakers do not treat scientific creativity or novel reaction design as reducible to pattern completion. [[MossamDataScienceWithSam]] raises unsupervised radioactive reactions as a prospective hazard, not a documented trial. [[EffieDataScienceWithSam]]'s concern about unknown biology and [[ResearchTaste]] limit confident extrapolation; [[ProblemDefinitionInResearch]] cannot be outsourced simply by collecting more data.

## What Changed
- Recast replacement rhetoric as four distinct verification boundaries with explicit proposed-versus-observed status.
- Distinguished data-preparation, model representation, experiment selection and physical safety.

## Related Concepts
- [[AIForScience]] - wider field in which these bounded researcher-led workflows sit.
- [[HumanJudgmentUnderAI]] - covers responsibility for interpreting model outputs before action.
- [[DomainExpertAlignment]] - explains why bioinformaticians and biologists must reconcile representations and questions.
- [[AIVerification]] - turns a model suggestion into a claim tested against experimental evidence.
- [[AIResearchLiteratureCurrency]] - changing prior work constrains the EEG project's novelty and replication claims.
- [[BiomedicalDeepLearning]] - single-cell-scale modeling must retain biological interpretability.
