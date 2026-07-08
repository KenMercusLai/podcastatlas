---
title: "Recursive Self-Improvement"
type: concept
tags: [ai, agents, training, safety]
sources: [e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di, 137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb]
last_updated: 2026-07-08
---

# Recursive Self-Improvement

Recursive self-improvement is the episode's frame for AI systems that help improve future versions of themselves. In [[e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]], [[LiBeibin]] defines the recursive part as a loop where a model finds or creates tasks, solves them, trains on the result, verifies the improvement, and repeats.

The source is careful about the difference between one self-improvement loop and stable recursion. A model may help build post-training data or diagnose a coding weakness before it can safely run many iterations without accumulating recursive drift. That makes [[AIVerification]], [[AICodingVerification]], [[MultiAgentCollaboration]], and human [[ResearchTaste]] part of the RSI mechanism rather than optional governance layers.

[[137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb]] adds [[HongLetong]]'s specialized route. She is less attached to the term AGI and imagines [[Axiom]] pushing from [[AIForMath]] toward specialized superintelligence at the edge of formal reasoning, then spreading into code verification and adjacent scientific domains. The key enabler is self-verifying reasoning: systems that can generate proofs or verification artifacts strong enough to improve the next loop.

## Key Claims
- RSI depends on long-horizon task ability, tool use, search, code generation, and feedback loops.
- Coding is an early route because model training, data pipelines, infrastructure, benchmark construction, and evaluation are code-heavy.
- Self-improvement can happen at several layers: pretraining data collection and cleaning, post-training diagnosis and recipe generation, and [[AgentHarness]] or scaffold improvement.
- A first loop is not the same as indefinite recursion; every iteration can introduce drift, reward hacking, or verification errors.
- Human experts still matter when the model needs to know which task, hypothesis, or scientific direction is worth optimizing.
- Formal proof can make recursive loops safer in math-like domains because the verifier is stronger, but [[FormalSpecification]] and [[AutoFormalization]] remain failure points.

## Connections
- [[Apodex]], [[LiBeibin]], and [[DuShaolei]] — source company and speakers.
- [[AgentSelfEvolution]] — adjacent workflow-layer concept extended by this source into model-training loops.
- [[DeepResearch]], [[ModelHarnessCoEvolution]], and [[AIVerification]] — mechanisms that make recursive improvement plausible.
- [[ResearchTaste]], [[DiscoveryModel]], and [[AIForScience]] — scientific-discovery boundary where self-improvement needs expert standards.
- [[Axiom]], [[AIForMath]], [[AxiomProver]], and [[FormalVerification]] — specialized self-verifying reasoning route added by episode 137.
