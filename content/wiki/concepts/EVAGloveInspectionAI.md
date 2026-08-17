---
title: "EVA Glove Inspection AI"
type: concept
tags: [ai-for-science, computer-vision, nasa, safety]
sources: [ep-4-a-i-talk-with-a-rocket-scientist-from-nasa]
last_updated: 2026-08-18
---

# EVA Glove Inspection AI

EVA glove inspection AI is [[KofiBrowning]]'s safety-specific computer-vision example in [[ep-4-a-i-talk-with-a-rocket-scientist-from-nasa]]. The source says astronauts' gloves are photographed before extravehicular activities to check for holes, cuts, or similar damage, then sent to mission control for review.

Kofi describes a young engineer writing a machine-learning algorithm to help inspect those images and partnering with [[Microsoft]] around the process. The source presents the system as assistance to human review, not a replacement for mission-control responsibility.

## Key Claims
- Spacesuit-glove inspection is a high-stakes visual quality-control task because small defects can matter during EVA.
- The task fits [[SpaceImageryAI]] because it involves repeated images and visible damage patterns.
- The safety context raises the verification threshold: a plausible classification is not enough if the model misses rare or subtle damage.
- Human reviewers remain responsible for final judgment, connecting the example to [[HumanDrivenScientificAI]].
- The example shows how one practical use case can be more credible than a broad claim that AI will transform all space research.

## Connections
- [[NASA]], [[KofiBrowning]], [[Microsoft]], and [[DataScienceWithSam]] - agency, source voice, partner, and show context.
- [[SpaceImageryAI]], [[SpaceflightAIDatasetScarcity]], [[AIVerification]], and [[DomainExpertAlignment]] - AI use-case and constraint context.
- [[HumanDrivenScientificAI]] and [[AIModelBiasGovernance]] - human oversight and reliability context.
- [[MissionDrivenGovernmentEngineering]] - high-stakes engineering responsibility behind the use case.
