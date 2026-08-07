---
title: "Mechanistic Interpretability"
type: concept
tags: [ai, ai-safety, interpretability, neural-networks]
sources: [149-qinli-zhongmei-new-labs-ziben-kuangchao-he-qinghua-liuziming-liao-ai-for-ai-jizhi-kejieshixing-he-max-tegmark-lm33q4n6w8tzcd2fxdbuk9unc2xv]
last_updated: 2026-08-08
---

# Mechanistic Interpretability

Mechanistic interpretability is the attempt to understand the internal mechanisms by which neural networks produce behavior. In [[149-qinli-zhongmei-new-labs-ziben-kuangchao-he-qinghua-liuziming-liao-ai-for-ai-jizhi-kejieshixing-he-max-tegmark-lm33q4n6w8tzcd2fxdbuk9unc2xv]], [[MaxTegmark]] pushes [[LiuZiming|Liu Ziming]]'s group toward the field in late 2022 and early 2023 because large models looked dangerous if their internals remained opaque.

Liu treats the field as close to a biology of AI. It can reveal useful internal structure, but the source also gives a caution: some neuron-level or highly local explanations may fail to survive changes such as random seed variation. That makes [[PhysicsOfAI]] broader than interpretability alone, because it also asks for training dynamics, controlled experiments, and phase-like regularities.

## Key Claims
- Interpretability is tied to AI safety when model capability rises faster than internal understanding.
- Visualization can matter because it lets researchers see more than end-to-end prediction quality.
- Mechanistic claims need robustness checks; an explanation that disappears across seeds may be less fundamental.
- Auto Research could accelerate interpretability work if it can structure experiments and compare mechanisms at scale.
- Liu's route keeps interpretability close to architecture design rather than treating it only as post-hoc explanation.

## Connections
- [[MaxTegmark]] and [[LiuZiming|Liu Ziming]] — source people.
- [[PhysicsOfAI]] — broader scientific frame in which mechanistic interpretability sits.
- [[AIInterpretabilityByAI]] — adjacent wiki concept about AI assisting interpretability.
- [[KolmogorovArnoldNetworks|KAN]] — source case where internal visualization helps evaluate an architecture.
- [[AIAlignmentGovernance]] and [[FrontierModelReleaseGovernance]] — broader wiki safety context.
