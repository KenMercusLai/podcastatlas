---
title: "Auto-Formalization"
type: concept
tags: [ai, formal-methods, mathematics]
sources: [137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb]
last_updated: 2026-07-08
---

# Auto-Formalization

Auto-formalization is the process of turning informal mathematical text into formal definitions, theorem statements, and proofs that a system such as [[LeanTheoremProver]] can check. In [[137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb]], [[HongLetong]] argues that this layer is underappreciated and may be at least as hard as theorem proving itself.

## Key Claims
- Informal mathematical prose leaves definitions, assumptions, notation, and proof steps implicit; formal systems require those choices to be explicit.
- Without auto-formalization, an AI prover can be strong only on problems already converted into formal language.
- Auto-formalization expands [[Mathlib]] and the machine-readable knowledge base that an [[AIMathematician]] can use.
- The same idea connects to [[FormalSpecification]] in software: the system cannot prove code correct until the intended property has been precisely stated.

## Connections
- [[AIForMath]], [[Axiom]], and [[AxiomProver]] — source context for the concept.
- [[LeanTheoremProver]], [[Mathlib]], and [[InteractiveTheoremProving]] — formal substrate and proof loop.
- [[FormalVerification]], [[AIVerification]], and [[AICodingVerification]] — adjacent verification tasks that also depend on precise statements.
