---
title: "Auto Research"
type: concept
tags: [ai, ai-research, agents]
sources: [ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1]
last_updated: 2026-07-08
---

# Auto Research

Auto Research is the research-automation layer defined in [[ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1]] as AI acting like a researcher: reading papers, forming hypotheses, writing code, running experiments, and analyzing results. It overlaps with [[MLCoding]], [[DeepResearch]], and [[DiscoveryModel]], but the episode uses it specifically as the step before [[RecursiveSelfImprovement]].

The distinction matters. Auto Research can make human researchers faster without proving that the system improves itself. [[RecursiveSelfImprovement]] requires the research loop to improve the next round of model, data, training recipe, benchmark, verifier, or agent system.

## Key Claims
- Auto Research needs long-horizon planning, paper reading, experiment coding, execution, analysis, and iteration.
- Code is the first strong substrate because experiments, data pipelines, benchmark harnesses, and evaluation scripts are executable and reviewable.
- The bottlenecks shift toward [[AICodingVerification]], [[AIVerification]], [[ResearchTaste]], compute allocation, and whether the task is worth optimizing.
- Auto Research can contribute to [[AIForScience]] even before it becomes full RSI.
- Startup and frontier-lab claims in this area should be treated as loop-quality claims, not just benchmark-score claims.

## Connections
- [[RecursiveSelfImprovement]] — stronger loop that Auto Research may enable.
- [[MLCoding]] — coding-heavy version of AI research work.
- [[DeepResearch]], [[DiscoveryModel]], and [[AIForScience]] — adjacent research and discovery frames.
- [[Recursive]] and [[Anthropic]] — source examples tied to auto-research and RSI practice.
- [[AICodingVerification]], [[AIVerification]], and [[ResearchTaste]] — controls needed to keep automated research useful.
