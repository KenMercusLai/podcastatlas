---
title: "RSI Data"
type: concept
tags: [ai, rsi, data, model-training]
sources: [cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]
last_updated: 2026-08-09
---

# RSI Data

RSI data is the source's label for long-running trajectories in which one model, agent, or training loop helps improve another model or its own future behavior. In [[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]], [[MengFanqing|孟繁青]] describes this as a likely next demand after ordinary agent data: a model post-trains a smaller model, checks whether it improves, and leaves a complete trace of data, training, evaluation, and revision.

This page treats RSI data as a bridge between [[SyntheticAgentData]] and [[RecursiveSelfImprovement]]. It is not just a good task answer; it is evidence from an improvement loop. That makes it expensive because the trajectory may require hours of environment execution, training knowledge, evaluation design, and anti-cheating checks.

## Key Claims
- RSI data records improvement attempts, not only task completion.
- Valuable trajectories may include environment setup, generated data, training runs, evaluation results, error analysis, and revised strategy.
- The source expects model labs to want this kind of data as ordinary agent-data demand becomes more concentrated around fewer high-value benchmarks.
- RSI data needs hands-on model-training expertise; it cannot be produced reliably by generic crowdsourcing alone.
- The concept sits between current post-training data markets and stronger [[AutoResearch]] or [[RecursiveSelfImprovement]] systems.

## Connections
- [[RecursiveSelfImprovement]], [[AutoResearch]], and [[AIForAI]] — broader self-improvement and research automation frame.
- [[SyntheticAgentData]], [[EnvironmentBasedAgentBenchmarks]], and [[RSIBenchData]] — data, benchmark, and project layer.
- [[AgentPostTraining]], [[ModelPostTrainingBottleneck]], and [[AIVerification]] — training and validation requirements.
- [[DataPricingInAI]] and [[AIDataInfrastructure]] — why these long trajectories can carry high value.
- [[EvolventAI]] and [[MengFanqing]] — source company and speaker.
