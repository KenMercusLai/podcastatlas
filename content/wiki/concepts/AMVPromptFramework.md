---
title: "AMV Prompt Framework"
type: concept
tags: [ai, prompting, frameworks]
sources: [e45-mengyan-duihua-lijigang-ren-heyi-zichu-lva2mfxese7v0sfv3mfpfhbdask]
last_updated: 2026-07-09
---

# AMV Prompt Framework

AMV prompt framework is [[LiJigang]]'s prompting model in [[e45-mengyan-duihua-lijigang-ren-heyi-zichu-lva2mfxese7v0sfv3mfpfhbdask]]. A is the starting point or role position, V is the destination or direction, and M is the mental shape or reasoning path from A to V.

The point of the framework is that role and goal are not enough. If the user only sets a starting role and an endpoint, the model will interpolate in its own way through the answer space. M constrains how the model should think, which frames it should use, and what shape the reasoning should take.

The episode treats AMV as both technical and artistic. It is a practical way to specify prompts, but the difficult part is choosing the right parameters, frames, and paths, much like investing formulas depend on judgment about growth, risk, and context.

## Key Claims
- A specifies where the model should start, often through role, stance, or context.
- V specifies the direction, desired end state, or vector of the answer.
- M specifies the mental path, thinking shape, or reasoning constraints between start and destination.
- Without M, the model may fill the middle with plausible but undesired reasoning.
- The framework works best when paired with rich [[ContextEngineering]] rather than thin roleplay.

## Connections
- [[PromptAsIntentTransmission]] — broader prompting theory that AMV operationalizes.
- [[AICommunicationAbility]] — user skill needed to express A, M, and V clearly.
- [[ContextEngineering]] — supplies the context that makes A and M concrete.
- [[HumanJudgmentUnderAI]] — the user still evaluates whether the chosen path produced a fitting answer.
- [[AISkills]] — AMV-style procedures can be turned into reusable agent instructions.
