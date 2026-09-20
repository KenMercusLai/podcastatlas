---
title: "Behavioral Alignment Patching"
type: concept
knowledge_schema: synthesis-v1
tags: [ai, alignment, prompts, safety]
sources:
  - tech-20260915-tech-pod-128-tech-20260915-tech-pod-128
last_updated: 2026-09-21
---

# Behavioral Alignment Patching

## Definition
Behavioral alignment patching is the practice of suppressing an observed unwanted model behavior through system instructions, reinforcement, or similar post-training controls without fully identifying or removing the underlying learned association.

## Current Synthesis
The source frames patching as necessary but causally incomplete. A provider can tell a model not to mention goblins, but success on that visible symptom does not show where the displaced behavior went, whether the model now over-refuses, or which adjacent associations were strengthened.

Shane's "duct tape and glue" metaphor turns alignment into an iterative maintenance problem: discover a failure, add a control, observe a new side effect, and patch again. The concept complements [[AIAlignmentGovernance]] by focusing on product-level behavioral repair while preserving the governance question of how fixes are tested, disclosed, and held accountable.

## Key Claims
- A system prompt can suppress a visible symptom without removing the behavior's underlying cause.
- Behavioral controls can create refusal, displacement, or other unintended effects outside the original test case.
- Alignment work therefore requires regression testing across adjacent behavior, not only confirmation that the named output disappeared.
- Prompting and reinforcement can both produce outcomes that differ from the designer's intended instruction.
- Incomplete visibility into learned associations makes alignment an ongoing maintenance process rather than a one-time fix.

## Evidence
### Symptom-level suppression
- [[tech-20260915-tech-pod-128-tech-20260915-tech-pod-128]] says OpenAI reportedly added an instruction discouraging goblin language except where necessary.

### Displacement risk
- [[tech-20260915-tech-pod-128-tech-20260915-tech-pod-128]] uses the image of taping one bulge only for another to appear elsewhere and raises the possibility that the model could instead refuse goblin-related discussion.

### Iterative repair cycle
- [[tech-20260915-tech-pod-128-tech-20260915-tech-pod-128]] describes a repeated sequence of finding problems, patching them, and then patching problems created by those fixes.

## Counterevidence & Qualifications
- The episode does not provide before-and-after evaluations showing the actual effect of the reported OpenAI instruction.
- Some behavioral patches may be robust when paired with training, evaluation, monitoring, and model-level changes; the source does not compare mitigation methods systematically.
- The Grok example remains an analogy based on reported prompting rather than a complete technical incident record.

## What Changed
- Created a canonical concept for symptom suppression, behavioral displacement, and iterative alignment maintenance.

## Related Concepts
- [[AIAlignmentGovernance]] - institutional accountability layer around alignment decisions and outcomes.
- [[FineTuningExampleSignalAmplification]] - upstream mechanism that can create an unwanted behavioral pattern.
- [[ChatbotSafetyGuardrailDecay]] - adjacent failure where safety behavior weakens across conversational context.
- [[ModelValueEmbedding]] - broader account of how data, reward, prompts, and product policy shape behavior.
- [[AIVerification]] - testing discipline needed to detect regressions and side effects after a patch.
