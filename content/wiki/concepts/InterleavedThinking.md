---
title: "Interleaved Thinking"
type: concept
tags: [agents, reasoning, models]
sources: [dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]
last_updated: 2026-07-06
---

# Interleaved Thinking

Interleaved thinking is the agentic-model ability to reason, act, observe, and then reason again after receiving tool or environment feedback. In [[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]], the [[MiniMax]] guests distinguish this from chatbot behavior: a chatbot can answer the present prompt, while an agentic model must explore, correct paths, and update plans as the environment changes.

## Key Claims
- Agentic models need to revise plans after tool calls rather than simply execute the first plan.
- Benchmarks that require cross-source search and multi-condition answers test this behavior better than one-shot chat tasks.
- [[AgentHarness]] matters because the model can only interleave thought and action when it has tools, observable state, and feedback.
- The concept is a model-side complement to [[AgenticWorkflow]] and [[ModelHarnessCoEvolution]].

## Connections
- [[MiniMax]] — company context for the term in the source.
- [[AgentHarness]] — runtime environment that exposes observations and feedback.
- [[AgenticWorkflow]] — task pattern enabled by interleaved reasoning and action.
- [[MultiAgentCollaboration]] — peer checking can help when a single agent's interleaved path drifts.
- [[AICodingVerification]] — software tasks require agents to observe tests, errors, diffs, and reviews before deciding next steps.
