---
title: "Long-Horizon AI"
type: concept
tags: [ai, agents, context, training]
sources: [openclaw-zhihou-wo-zhi-xiang-weilai-3-6-ge-yue-de-shiqing-duitan-sheet0-chuangshiren-wang-wenfeng-lu-d4y7qifag6-rc79tp-roxjp4z, 140-dui-yao-shunyu-de-4-xiaoshi-fangtan-qing-yunxu-wo-xiao-feng-yixia-zai-anthropic-he-gemini-xun-moxing-jishu-yuce-yingxiongzhuyi-yi-guoqu-ll7qiciwwgfssorhr4yy-uuqae8h, 138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf, xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]
last_updated: 2026-07-23
---

# Long-Horizon AI

Long-horizon AI is [[YaoShunyu]]'s frame in [[140-dui-yao-shunyu-de-4-xiaoshi-fangtan-qing-yunxu-wo-xiao-feng-yixia-zai-anthropic-he-gemini-xun-moxing-jishu-yuce-yingxiongzhuyi-yi-guoqu-ll7qiciwwgfssorhr4yy-uuqae8h]] for models that can complete longer task chains than ordinary context windows and benchmark episodes expose. His shorthand is "train with finite context, use as infinite context": train models under bounded context, but deploy them in interactive systems where they can gather information, retrieve, summarize, forget, and keep working over a much longer horizon.

[[138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]] adds an architecture and agent-data version through [[LuoFuli]] and [[MemoVR]]. The source treats code, long context, cross-session memory, plan compression, and agent framework traces as training signals, while [[AgentOptimizedModelArchitecture]] tries to make long-context behavior fast and cheap enough for real agent work.

[[xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]] adds the retrieval-boundary version. [[NStudent]] argues that longer context helps some single-document reading tasks, but it does not replace [[RetrievalAugmentedGeneration]] over very large document collections, and long conversations can still suffer [[ContextDecay]] when earlier information becomes vague or stale.

[[openclaw-zhihou-wo-zhi-xiang-weilai-3-6-ge-yue-de-shiqing-duitan-sheet0-chuangshiren-wang-wenfeng-lu-d4y7qifag6-rc79tp-roxjp4z]] adds a file-system practice version through [[WangWenfeng]]. He describes task length in terms of step counts, where current practical work may move from dozens of steps toward hundreds or thousands, and argues that file-system state lets agents record progress, observe errors, repair memory, and keep working without relying on a human to hand-curate all context.

## Key Claims
- Long-horizon capability is not only a larger context-window number; it is the ability to decide what information remains relevant during extended work.
- [[ContextEngineering]] becomes part of model training and post-training, not only a user habit, because the model must learn when to compress, retrieve, ignore, or ask for new context.
- Yao treats continual learning and long-horizon work as closely related: a model's active context and KV cache can be viewed as a temporary form of weight-like state.
- The technical routes include pretraining-side changes such as sparse attention and post-training-side changes such as context management; Yao says his own focus is more on post-training.
- The concept is especially important for agentic work because tasks such as research, software projects, and personal assistance fail when models lose earlier decisions or optimize only the next short step.
- Evaluation must be scientific and comparative; a long-horizon technique matters only if it improves real extended tasks rather than merely making prompts longer.
- Long-horizon ability can be trained indirectly through code and agent workflows because both require dependencies, recovery, planning, and verification over many steps.
- Long context is not a universal substitute for retrieval; large libraries still need [[VectorModelEngineering]], chunking, and ranking.
- File-system state can serve as external working memory for long-horizon agents because progress, failures, and repair notes become inspectable artifacts rather than hidden chat history.

## Connections
- [[YaoShunyu]] — source speaker and practitioner.
- [[MLCoding]] — current work area where long-horizon ability matters for experiments, code, analysis, and hypothesis loops.
- [[ContextEngineering]], [[PersistentAgentMemory]], and [[AgentHarness]] — adjacent ways of handling state, memory, and environment outside raw model weights.
- [[AICodingVerification]] and [[AgenticWorkflow]] — software-agent cases where extended task chains need review and regression control.
- [[WorldModels]] and [[ProactiveAgents]] — related directions where models must carry state across actions rather than answer isolated prompts.
- [[LuoFuli]], [[MemoVR]], [[AgentOptimizedModelArchitecture]], and [[AgentPostTraining]] — long-context architecture and agent-data branch added by episode 138.
- [[RetrievalAugmentedGeneration]], [[ContextDecay]], and [[VectorModelEngineering]] — retrieval-boundary branch added by the Fuyou Tiandi vector-model episode.
- [[WangWenfeng]], [[AgentHarness]], [[AgenticWorkflow]], and [[PersistentAgentMemory]] — step-count and file-system state practice added by the 42章经 source.
