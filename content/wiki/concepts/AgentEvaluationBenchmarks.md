---
title: "Agent Evaluation Benchmarks"
type: concept
tags: [agents, evaluation, safety]
sources:
  - cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi
  - women-shi-ruhe-dingyi-openclaw-for-teams-xin-chanpin-xingtai-de-duitan-kuse-junior-lianchuang-jian-cto-yuhao-lkp1a0todflxoyycyo3zhrap3ebv
  - e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

# Agent Evaluation Benchmarks

## Definition
Agent evaluation benchmarks are repeatable tests of whether an agent can complete useful work across tools, state, time, and safety constraints, including cases where correct behavior is to refuse, pause, or avoid an action.

## Current Synthesis
The sources move agent evaluation beyond static final-answer scoring. [[Kuse]] treats evaluation as product infrastructure for detecting behavior shifts across models, runtimes, multi-turn state, tool actions, security attacks, and situations where an agent should not act. [[EvolventAI|Evolvent AI]] adds simulated work environments and multidimensional scoring, with the complication that benchmark trajectories may later feed post-training or synthetic-data loops.

[[AgentsLastExam|Agent's Last Exam]] extends the same architecture across professional and engineering domains. A valuable task combines real-work relevance with usable tools, an execution environment, and credible verification through program checks, state inspection, rubrics, specialist models, or humans. Leaderboard gains are useful evidence only when evaluation tasks remain held out and improvement transfers; narrow specialization, arbitrary aggregation, task defects, leakage, and saturation can make scores overstate general capability.

## Key Claims
- Agent evaluation should cover trajectories, environment state, tools, and long-horizon behavior, not only final prose.
- Safety benchmarks need negative tests for refusal, disclosure, installation, spending, and other inappropriate actions.
- Authentic work relevance makes optimization more valuable but does not guarantee generalization.
- Multidimensional scoring is necessary when agents can reach a result through unsafe, wasteful, or invalid paths.
- Benchmark traces can become training data, increasing the need for explicit provenance and held-out separation.
- Human technical judgment remains necessary for new capabilities that fixed test suites do not yet represent.

## Evidence
- Product regression and safety - [[women-shi-ruhe-dingyi-openclaw-for-teams-xin-chanpin-xingtai-de-duitan-kuse-junior-lianchuang-jian-cto-yuhao-lkp1a0todflxoyycyo3zhrap3ebv]] describes automated tests across model and runtime changes, state, tools, phishing, prompt injection, disclosure, and non-action.
- Environment and data loop - [[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]] links simulated work, multiple scoring dimensions, trajectories, and post-training data production.
- Cross-domain real work - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] presents Agent's Last Exam as a project for verifiable work beyond code.
- Score interpretation - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] distinguishes meaningful real-task optimization from leakage, specialization, arbitrary weights, flawed tests, and saturation.

## Counterevidence & Qualifications
Benchmark performance is not deployment proof. Simulators can omit real permissions, latency, failure costs, users, and institutional constraints; public tests can leak into training; aggregate scores hide domain weights; and a benchmark near saturation may retain mostly ambiguous or defective cases. Online A/B tests and user preferences can also disagree with offline evaluation without providing a clean truth standard.

## What Changed
- Added real-work correspondence and held-out integrity as tests for whether benchmark optimization is meaningful.
- Added benchmark saturation, weighting, and defective residual tasks as limits on score interpretation.
- Added expert-submission authenticity as an upstream benchmark-quality problem.

## Related Concepts
- [[EnvironmentBasedAgentBenchmarks]] - interactive task architecture inside the broader benchmark category.
- [[BenchmarkTrainingDataSeparation]] - rule protecting measurement from training contamination.
- [[AgentsLastExam|Agent's Last Exam]] - cross-domain benchmark project used as the newest case.
- [[AIVerification]] - broader problem of establishing correctness and fitness for use.
- [[AgentPermissionBoundaries]] - authority limits that safety benchmarks must exercise.
- [[SyntheticAgentData]] - trajectory output that can support training but complicates provenance.
- [[HumanJudgmentUnderAI]] - interpretation and novel-capability judgment not fully captured by fixed tests.
