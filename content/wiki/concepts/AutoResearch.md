---
title: "Auto Research"
type: concept
tags: [ai, ai-research, agents]
sources:
  - cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi
  - yu-tian-yuandong-liao-rsi-moxing-zi-jinhua-ruhe-daolai-1-178-1
  - ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1
  - 149-qinli-zhongmei-new-labs-ziben-kuangchao-he-qinghua-liuziming-liao-ai-for-ai-jizhi-kejieshixing-he-max-tegmark-lm33q4n6w8tzcd2fxdbuk9unc2xv
  - c11cceb2-07c2-4c2f-9124-95bd1187c7ec-c11cceb2-07c2-4c2f-9124-95bd1187c7ec
last_updated: 2026-11-18
knowledge_schema: synthesis-v1
---

# Auto Research

## Definition

Auto Research is the use of AI agents to read evidence, propose hypotheses, implement experiments, execute and monitor them, analyze results, and iteratively decide what to test next.

## Current Synthesis

Auto Research is already plausible as a human-supervised system of specialized research roles, especially in code-heavy AI work. [[RDAgent]] provides the clearest bounded example in the supplied evidence: research agents propose directions, development agents implement them, experimental results return to the research layer, and success or failure can inform the next cycle. Data, environments, benchmarks, harnesses, and process traces are therefore part of the research system rather than mere support infrastructure.

This remains distinct from [[RecursiveSelfImprovement]]. Automating a research task or closing one experiment loop does not show that the system improves the next generation's research capability. The durable bottlenecks are verifier quality, long-horizon coordination, research-process data, compute allocation, failure interpretation, and human judgment about which objective is worth pursuing.

## Key Claims

- Auto Research combines literature work, hypothesis formation, coding, execution, monitoring, analysis, and revision.
- Code and model post-training are early strong substrates because experiments are executable and feedback cycles are comparatively manageable.
- Specialized agent teams can expand research throughput while humans retain goals, budgets, broad framing, and experiment approval.
- Research automation needs structured observations, interventions, results, failures, and next actions because final papers omit much of the usable process.
- Environments and evaluators are research infrastructure: an agent cannot learn reliably from a loop whose outcome is vague, delayed, or gameable.
- Reusable failure trajectories can improve later search, but only if the system distinguishes genuine lessons from noise and metric artifacts.
- Auto Research can contribute to RSI, but faster experiments and a successful loop are weaker evidence than repeatable successor improvement.

## Evidence

### Operational research loop
- [[c11cceb2-07c2-4c2f-9124-95bd1187c7ec-c11cceb2-07c2-4c2f-9124-95bd1187c7ec]] describes [[RDAgent]] joining research, development, experiment analysis, monitoring, and repeated proposal cycles.
- [[ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1]] defines Auto Research as AI acting like a researcher and separates it from the stronger RSI loop.

### Feedback speed and research judgment
- [[yu-tian-yuandong-liao-rsi-moxing-zi-jinhua-ruhe-daolai-1-178-1]] shows execution speed improving before open-ended direction selection or research taste.

### Data, environments, and process structure
- [[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]] adds long-running trajectories, synthetic agent data, environment design, and benchmark scoring as inputs to research automation.
- [[149-qinli-zhongmei-new-labs-ziben-kuangchao-he-qinghua-liuziming-liao-ai-for-ai-jizhi-kejieshixing-he-max-tegmark-lm33q4n6w8tzcd2fxdbuk9unc2xv]] argues for structured observations, hypotheses, interventions, and training-curve prediction rather than brute-force coding alone.

## Counterevidence & Qualifications

- The sources are interviews and episode summaries, not comparative evaluations of complete autonomous research systems.
- Hundreds of agents do not imply hundreds of independent researchers; orchestration overhead, duplicate work, and human review may be substantial.
- Benchmark progress can reflect leakage, reward hacking, narrow optimization, or harness changes rather than general research improvement.
- Physical science and regulated domains have slower and costlier feedback than software, mathematics, or post-training.
- More experiments can consume more compute without raising insight quality.
- Human researchers still set the objective and decide whether an experiment is meaningful in all supplied operational accounts.

## What Changed

- Added RDAgent as a concrete multi-role research loop.
- Added successful and failed trajectory reuse as a conditional learning mechanism.
- Clarified that research parallelism can raise total compute and coordination costs.
- Migrated the page to the synthesis-v1 evidence structure.

## Related Concepts

- [[AIForAI]] - broader umbrella for applying AI across AI development.
- [[RecursiveSelfImprovement]] - stronger successor-improvement loop that Auto Research may enable.
- [[AIResearchFeedbackCompression]] - explains why automated implementation changes research tempo.
- [[AIVerification]] - guards against false progress and metric gaming.
- [[ResearchTaste]] - selects valuable questions and interprets ambiguous evidence.
- [[ModelHarnessCoEvolution]] - captures joint changes in models and the scaffolds used to train or evaluate them.
