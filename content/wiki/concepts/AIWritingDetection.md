---
title: "AI Writing Detection"
type: concept
tags: [ai, writing, detection, editing]
sources: [ep-9-chatgpt-and-education-systems, tech-20260824-mp-tech-pod-128-tech-20260824-mp-tech-pod-128, tech-20260814-tech-pod-128-tech-20260814-tech-pod-128, tech-20260810-0810-mp-tech-pod-128-tech-20260810-0810-mp-tech-pod-128, taken-littorally-spains-sudden-crisis-in-ceuta-6a70712c034f16a52ebfaed7]
last_updated: 2026-08-24
---

# AI Writing Detection

[[ep-9-chatgpt-and-education-systems]] adds an early school-response example. [[JosephStrader]] mentions a Princeton student's "Chat Zero" detector as a way to check whether text came from [[ChatGPT]], but the episode's broader frame treats detection as only one part of [[AIAcademicIntegrity]].

[[tech-20260824-mp-tech-pod-128-tech-20260824-mp-tech-pod-128]] adds the named [[NegativeParallelism]] branch through [[WillOremus]] of [[TheAtlantic|The Atlantic]]. The episode treats "not X, but Y" writing as a useful AI tell because [[Pangram]] found it much more often in AI-generated prose, while still warning that the pattern has ordinary human and literary history.

[[tech-20260814-tech-pod-128-tech-20260814-tech-pod-128]] adds the watermarking version through [[Anthropic]] and [[Claude]]. Instead of inferring authorship from style or detector scores, [[AITextWatermarking]] embeds a signal in generated or copied text. The source still keeps detection uncertain in practice because human writing edited through Claude may receive a watermark.

AI writing detection is the attempt to identify machine-generated prose through detectors, stylistic traces, source comparison, or editorial judgment. [[taken-littorally-spains-sudden-crisis-in-ceuta-6a70712c034f16a52ebfaed7]] adds the concept through [[CaitlinTalbot]]'s segment on why AI writing is becoming harder to identify.

The source distinguishes detector scores from writing analysis. Tools such as [[Pangram]] can produce false positives and give little explanation, while The Economist's comparison of human and model-generated prose looks for patterns across word choice, punctuation, sentence structure, and formulaic rhetoric.

[[tech-20260810-0810-mp-tech-pod-128-tech-20260810-0810-mp-tech-pod-128]] adds the platform-integrated detector version through [[Substack]]. [[ChrisBest]] says Substack's [[Pangram]]-powered feature gives users an estimate of human versus AI-written text and lets users report mistakes or remove clearly wrong detections.

The source also adds a behavior risk. Public detector scores can push writers to revise for the detector rather than for readers, so detection can distort writing norms even when its goal is transparency.

## Key Claims
- Detection is a moving target because models are trained on human writing and improved by human feedback.
- EP9 shows that detector hopes appeared immediately in school contexts, but the integrity problem also required teacher literacy and assignment redesign.
- A detector result should be treated as a signal for review, not as standalone proof of authorship.
- Platform-integrated detectors can make AI authorship more legible to readers, but they also create product responsibilities around false positives, appeals, and correction.
- Detector visibility can change writer incentives if authors start optimizing to avoid being publicly labeled as AI-generated.
- The Economist's comparison found AI prose using more polysyllabic, rare, or scientific-sounding words.
- AI prose in the source tends to use less varied punctuation and more long sentences joined by "and."
- Repeated rhetorical shapes such as "not X but Y," "not only but also," and rules of three can make generated prose feel formulaic.
- Named tics such as [[NegativeParallelism]] can support media literacy, but they cannot prove authorship because people can use, parody, or absorb the same style.
- Heavy AI use may blur authorship signals if human writers begin adopting recognizable AI constructions.
- The strongest practical response is not only better detection; it is better editing, audience awareness, detail, and distinctive style.
- Watermarks can identify model involvement more directly than style detectors, but they cannot by themselves distinguish AI authorship from AI-assisted editing.

## Connections
- [[CaitlinTalbot]], [[Pangram]], [[ChatGPT]], [[Claude]], [[Gemini]], and [[Grok]] - source speaker, detector, and model examples.
- [[WillOremus]], [[TheAtlantic|The Atlantic]], and [[NegativeParallelism]] - Marketplace Tech branch on AI-writing tics.
- [[JosephStrader]], [[AIAcademicIntegrity]], and [[TeacherAILiteracy]] - school-detection context added by Data Science With Sam EP9.
- [[Substack]] and [[ChrisBest]] - publishing-platform detector and disclosure case.
- [[AIWritingPedagogy]] and [[AIDetectorBias]] - education-policy and fairness context.
- [[HumanAuthorshipPremium]], [[HumanJudgmentUnderAI]], and [[AIContentProvenance]] - adjacent trust and authorship concepts.
- [[AITextWatermarking]], [[Anthropic]], [[Claude]], and [[EuropeanUnionAIAct]] - model-side detection branch added by Marketplace Tech.
