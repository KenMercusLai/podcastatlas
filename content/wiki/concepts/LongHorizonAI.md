---
title: "Long-Horizon AI"
type: concept
tags: [ai, agents, context, training]
sources: [140-dui-yao-shunyu-de-4-xiaoshi-fangtan-qing-yunxu-wo-xiao-feng-yixia-zai-anthropic-he-gemini-xun-moxing-jishu-yuce-yingxiongzhuyi-yi-guoqu-ll7qiciwwgfssorhr4yy-uuqae8h]
last_updated: 2026-07-08
---

# Long-Horizon AI

Long-horizon AI is [[YaoShunyu]]'s frame in [[140-dui-yao-shunyu-de-4-xiaoshi-fangtan-qing-yunxu-wo-xiao-feng-yixia-zai-anthropic-he-gemini-xun-moxing-jishu-yuce-yingxiongzhuyi-yi-guoqu-ll7qiciwwgfssorhr4yy-uuqae8h]] for models that can complete longer task chains than ordinary context windows and benchmark episodes expose. His shorthand is "train with finite context, use as infinite context": train models under bounded context, but deploy them in interactive systems where they can gather information, retrieve, summarize, forget, and keep working over a much longer horizon.

## Key Claims
- Long-horizon capability is not only a larger context-window number; it is the ability to decide what information remains relevant during extended work.
- [[ContextEngineering]] becomes part of model training and post-training, not only a user habit, because the model must learn when to compress, retrieve, ignore, or ask for new context.
- Yao treats continual learning and long-horizon work as closely related: a model's active context and KV cache can be viewed as a temporary form of weight-like state.
- The technical routes include pretraining-side changes such as sparse attention and post-training-side changes such as context management; Yao says his own focus is more on post-training.
- The concept is especially important for agentic work because tasks such as research, software projects, and personal assistance fail when models lose earlier decisions or optimize only the next short step.
- Evaluation must be scientific and comparative; a long-horizon technique matters only if it improves real extended tasks rather than merely making prompts longer.

## Connections
- [[YaoShunyu]] — source speaker and practitioner.
- [[MLCoding]] — current work area where long-horizon ability matters for experiments, code, analysis, and hypothesis loops.
- [[ContextEngineering]], [[PersistentAgentMemory]], and [[AgentHarness]] — adjacent ways of handling state, memory, and environment outside raw model weights.
- [[AICodingVerification]] and [[AgenticWorkflow]] — software-agent cases where extended task chains need review and regression control.
- [[WorldModels]] and [[ProactiveAgents]] — related directions where models must carry state across actions rather than answer isolated prompts.
