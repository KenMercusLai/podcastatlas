---
title: "AI Verification"
type: concept
tags: [ai, verification, safety, agents]
sources: [e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]
last_updated: 2026-07-08
---

# AI Verification

AI verification is the broader problem of checking whether an AI-generated answer, hypothesis, tool action, training example, or self-improvement step is correct enough to use. [[e242-zuikuai-bannian-ai-paotong-zi-jinhua-yu-chen-tianqiao-shouxi-kexuejia-liaoliao-guigu-moxing-bi-zheng-zhi-di]] makes verification the central constraint on [[RecursiveSelfImprovement]] and [[DiscoveryModel]] work.

The source separates easy-to-check domains from judgment-heavy domains. Code and math can use execution, tests, and formal proof tools, but even code can fail when tests are too broad, too narrow, or written to reward the wrong behavior. For open-ended scientific and research problems, [[Apodex]] uses agent teams: one agent or group proposes, another verifies, redundant agents compare answers, and the system learns which information sources deserve trust.

## Key Claims
- Verification errors can compound across recursive self-improvement loops.
- Code and math are attractive early domains because they have stronger external checkers than ordinary prose.
- Tests are not automatically reliable; a model can pass weak tests while still solving the wrong problem.
- Multi-agent review can reduce single-agent drift, but it still needs source-quality judgment and human oversight.
- Reward hacking is a verification failure: the model optimizes the proxy rather than the human need.
- Scientific discovery needs verification and taste together, because a true but trivial result may still be the wrong target.

## Connections
- [[AICodingVerification]] — software-specific verification branch already tracked in the wiki.
- [[MultiAgentCollaboration]] — agent-team checking pattern used in the source.
- [[RecursiveSelfImprovement]] and [[DiscoveryModel]] — high-stakes loops that depend on verification.
- [[ResearchTaste]], [[HumanJudgmentUnderAI]], and [[DomainExpertAlignment]] — human standards that keep verification grounded.
