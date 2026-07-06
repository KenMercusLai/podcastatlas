---
title: "Agent Harness"
type: concept
tags: [agents, infrastructure, context, tooling]
sources: [tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3, dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd, ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan]
last_updated: 2026-07-06
---

# Agent Harness

Agent harness is the model-external system that lets an AI agent act in the world. In [[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]], [[LaiXinlu]] defines it as everything outside the model: tools, files, runtime state, context, memory, compression, handoff, permissions, and multi-agent governance.

[[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]] adds a work-environment analogy through [[MiniMax]] and [[HermesAgent]]: a harness is like giving a capable coworker tools, accounts, boundaries, feedback, and responsibility for delivery. The source emphasizes that harness design becomes more important once humans become the bottleneck in supervising many agents.

[[ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan]] adds a coding-tool comparison: [[GeminiCLI]] may benefit from loading large code context directly, while [[Cursor]] may use more engineered chunking, indexing, and retrieval to control cost. The episode therefore treats context strategy itself as a harness-level product choice.

## Layers
- Execution ability: CLI tools, file operations, browser use, language interpreters, code-registered tools, and protocol-style extensions.
- Context and environment: system prompt, working directory, dependency state, git state, [[AISkills]], [[PersistentAgentMemory]], context-window management, compression, and task handoff.
- Governance and orchestration: multi-agent roles, permissions, information boundaries, and safeguards against agents mutating the wrong artifacts.
- Feedback and learning: tests, deployments, result checks, memory updates, and successful workflows saved as [[AISkills]].

## Key Claims
- Harness matters because a model without tools and environment is an intelligent system without hands, memory, or operating context.
- The model is still the first source of agent intelligence; harness design should amplify the model rather than replace the model's judgment with rigid flow logic.
- Current agents may work better with more context, more action capacity, and less brittle programmatic control.
- CLI/Unix-style interfaces can be more natural for current models than newer abstractions because command-line patterns are deeply represented in training data.
- Good harnesses should align with the model's operating logic and remain useful as models improve; over-managed context or overly restrictive orchestration can become a bottleneck.
- Harnesses expose real-world feedback that lets agents recover, update memory, and support [[AgentSelfEvolution]] rather than merely produce one-shot answers.
- Harness design must account for [[AgentIdentityAndAuthentication]] when agents operate accounts, payments, code deployment, or other high-impact tools.
- Context loading, indexing, retrieval, and compression choices can determine whether a coding harness preserves enough codebase meaning for hard tasks.

## Connections
- [[ClaudeCode]] and [[LearnClaudeCode]] — concrete harness sample analyzed in the source.
- [[AgenticWorkflow]] — task pattern that exposes whether a harness works.
- [[ContextEngineering]], [[PersistentAgentMemory]], and [[AISkills]] — context layer inside the harness.
- [[AgentFacingInterfaces]] and [[HeadlessSoftware]] — product/interface consequences of giving agents callable tools.
- [[SubagentWorkflow]] — orchestration pattern that needs permissions and handoff.
- [[ModelHarnessCoEvolution]] — adjacent concept describing how models and harnesses improve together.
- [[KComputer]] — Share AI implementation of a lightweight Unix-like harness environment.
- [[HermesAgent]] — open-source framework used to explain harness as tools, main loop, state, errors, memory, and skills.
- [[MultiAgentCollaboration]], [[InterleavedThinking]], and [[AgentIdentityAndAuthentication]] — additional harness requirements from the Hermes Agent source.
- [[GeminiCLI]], [[Cursor]], and [[ContextEngineering]] — coding-context strategy added by EP108.
