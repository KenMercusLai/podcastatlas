---
title: "Interactive Theorem Proving"
type: concept
tags: [formal-methods, theorem-proving, verification]
sources: [137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb]
last_updated: 2026-07-08
---

# Interactive Theorem Proving

Interactive theorem proving is the proof-assistant mode where a human or AI works inside a formal system and the checker validates each proof step or tactic. In [[137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb]], [[HongLetong]] distinguishes this from older automatic theorem proving and says current AI systems often replace more of the human interaction loop while still relying on a formal checker.

## Key Claims
- The formal checker gives [[AIVerification]] a stronger signal than ordinary natural-language reasoning.
- The hard work includes translating informal goals into formal statements, choosing tactics, managing proof state, and using existing library material.
- [[LeanTheoremProver]] and [[Mathlib]] make interactive theorem proving usable for modern mathematics, but library gaps and slow verification remain bottlenecks.
- AI theorem proving can produce correct but long proofs, so proof quality and proof elegance remain separate evaluation dimensions.

## Connections
- [[AxiomProver]], [[AIForMath]], and [[AIMathematician]] — AI systems and goals built around theorem proving.
- [[AutoFormalization]] and [[FormalSpecification]] — upstream translation and precise-statement requirements.
- [[FormalVerification]] and [[AICodingVerification]] — software and systems verification branch.
