---
title: "Locked-In Syndrome Assistive Communication"
type: concept
tags: [accessibility, assistive-technology, ai, neuroscience]
sources:
  - ep-6-data-science-ai-talk
  - essentials-the-science-of-learning-speaking-languages-dr-eddie-chang-scim7185728420
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

# Locked-In Syndrome Assistive Communication

## Definition
Locked-in syndrome assistive communication is the use of brain-signal, AI, or neuroprosthetic systems to help people express themselves when cognition and awareness remain but voluntary movement or speech output is blocked.

## Current Synthesis
The concept now has two evidence layers. [[ep-6-data-science-ai-talk]] provides the early AI-research version: [[PaulinaNemkova|Paulina Nemkova]] motivates [[EEGBrainReading]] through the possibility that brain-signal classification could eventually help people who can think but cannot express themselves because of paralysis. That source keeps the technical claim modest, treating EEG object-category classification as an early step rather than full thought reading.

The [[EddieChang]] episode adds a more direct clinical-neurotechnology layer through [[SpeechNeuroprosthetics]] and the [[BRAVOTrial]]. There, the target is not merely object-category inference but attempted-speech decoding from implanted cortical electrodes in a person with severe paralysis after brainstem stroke. Together the sources make agency the central criterion: the technology matters when it gives a person a reliable route from intended communication to shared words, while error, invasiveness, training burden, and overclaiming remain serious boundaries.

## Key Claims
- The user's agency is the center of the use case: a model or implant matters only if it helps expression.
- Locked-in communication support has stronger ethical grounding when tied to restoring communication barriers rather than surveillance, spectacle, or enhancement.
- EEG category classification and implanted attempted-speech decoding sit at different capability levels, but neither should be treated as general mind reading.
- Speech neuroprosthetics can target intended articulator movements when a person cannot produce intelligible speech.
- Verification, calibration, training, and error management are essential because false or overconfident interpretation could harm vulnerable users.
- Invasive devices raise separate safety and access questions from noninvasive AI research.

## Evidence
- Early brain-signal motivation: [[ep-6-data-science-ai-talk]] says Paulina Nemkova's EEG project is motivated by helping people who retain thought but cannot express it because of paralysis.
- EEG capability boundary: [[ep-6-data-science-ai-talk]] limits the current claim to classifying object categories, not decoding complete thoughts or consciousness.
- Clinical locked-in scenario: [[essentials-the-science-of-learning-speaking-languages-dr-eddie-chang-scim7185728420]] describes brainstem stroke and ALS as conditions that can leave cognition intact while disrupting voluntary movement and speech.
- Attempted-speech decoding: [[essentials-the-science-of-learning-speaking-languages-dr-eddie-chang-scim7185728420]] describes implanted electrodes, machine-learning decoding, a 50-word early vocabulary, context-based correction, and sentence output in the BRAVO case.

## Counterevidence & Qualifications
The evidence remains source-scoped. The EEG source is early research and does not demonstrate practical communication. The BRAVO source is a public podcast explanation rather than complete clinical-trial data, and its invasive, trained, limited-vocabulary system should not be generalized to all locked-in patients, all paralysis causes, or non-medical enhancement.

## What Changed
- Added the Huberman Lab / Eddie Chang speech-neuroprosthetics case as a direct clinical restoration layer beyond the earlier EEG object-category research.
- Migrated the page to the `synthesis-v1` structure.

## Related Concepts
- [[EEGBrainReading]] - early noninvasive brain-signal classification branch.
- [[SpeechNeuroprosthetics]] - implanted attempted-speech decoding branch.
- [[BRAVOTrial]] - clinical-trial case grounding the speech-neuroprosthetic layer.
- [[AssistiveAI]] - broader accessibility frame.
- [[AIForScience]] - scientific AI context for brain-signal modeling.
- [[AIVerification]] - validation requirement for high-stakes interpretation.
- [[HumanJudgmentUnderAI]] - human-responsibility context for vulnerable users.
- [[ResearchReplicationIntegrity]] - evidence boundary for brain-signal claims.
