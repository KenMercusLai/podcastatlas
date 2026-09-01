---
title: "Subagent Workflow"
type: concept
tags: [agents, workflow, skills]
sources:
  - ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun
  - tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3
  - dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd
  - vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1
  - 137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb
  - ep-59-2026-agent-biancheng-xin-qushi-8218230840-466252
last_updated: 2026-09-02
knowledge_schema: synthesis-v1
---

# Subagent Workflow

## Definition
Subagent workflow is an agentic pattern where a foreground assistant delegates complex, long-running, specialized, or adversarial work to other agents and then integrates, reviews, or verifies their outputs.

## Current Synthesis
Subagents remain a harness-level technique for preserving main-context clarity, expanding search, dividing roles, and cross-checking work. The pattern appears in coding, research, theorem proving, and productized multi-agent systems: one agent may explore code, another may test, another may argue against a plan, and a lead agent may synthesize the result.

The 2026 coding-agent discussion adds a model/harness co-evolution angle. Some workflows now need explicit leader, worker, and verifier roles created dynamically by the harness, but future models may internalize more of that decomposition. The practical conclusion remains unchanged: role boundaries, permissions, handoff documents, and verification make subagents useful rather than just parallel noise.

## Key Claims
- Subagents preserve the foreground context when a task is too large, tool-heavy, or disruptive for the main conversation.
- Role-specific agents are useful when tasks need different permissions, viewpoints, or standards, such as code exploration, testing, adversarial review, or proof repair.
- Multi-agent cross-checking can correct drift and hallucination, but it consumes more tokens and still needs human or verifier acceptance.
- Handoff artifacts are necessary because a subagent's output must be compact enough for another agent or human to reuse.
- Dynamic leader/worker/verifier teams are an emerging harness pattern for agent-native coding work.
- The durability of subagent orchestration depends on model/harness co-evolution: some decomposition may move into models, while permissions and verification remain external.

## Evidence
- Background subagents and adversarial pro/con roles are described as reusable skill patterns for tool-heavy or high-token work: [[ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun]].
- Governance sources emphasize role-specific permissions, information boundaries, and handoff documents so agents do not overstep or repair tests dishonestly: [[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]].
- Multi-agent systems can exchange larger context than human feedback normally provides and can cross-check long-context drift: [[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]].
- Practical coding and theorem-proving sources show subagents used for planning, implementation, review, Lean proof attempts, and verifier-driven repair: [[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]], [[137-dui-hong-letong-de-4-xiaoshi-fangtan-ai-for-math-ba-shuxue-biancheng-lean-shuxue-tianshu-zhong-de-zhengming-zhijue-bei-chuangzao-yu-bei-faxian-de-lha-faiwxtget0qmbcosts3cb5vb]].
- Agent-native coding tools are described as moving toward dynamically generated leader, worker, and verifier teams inside the harness: [[ep-59-2026-agent-biancheng-xin-qushi-8218230840-466252]].

## Counterevidence & Qualifications
Parallel agents do not automatically improve quality. They can multiply wrong assumptions, create integration work, burn tokens, and hide responsibility. Subagent workflows need explicit task boundaries, permission scoping, output contracts, and verification; otherwise the user receives more fluent uncertainty instead of a stronger result.

## What Changed
- Dynamic multi-agent team formation is now included as a 2026 coding-harness pattern.
- The synthesis now ties subagent workflows to model/harness co-evolution, not only current Claude Code or MiniMax-style orchestration.
- Verification roles are now explicit alongside explorer, worker, critic, and synthesizer roles.

## Related Concepts
- [[AgentHarness]] - orchestration layer that creates and constrains subagents.
- [[AISkills]] - packaging mechanism for reusable subagent patterns.
- [[MultiAgentCollaboration]] - broader frame for agents exchanging context and critique.
- [[ContextEngineering]] - task-context design needed for handoff and integration.
- [[AICodingVerification]] - acceptance layer that makes verifier agents meaningful.
- [[ModelHarnessCoEvolution]] - question of which orchestration logic remains outside models.
- [[AgentCommandCenter]] - interface pattern where humans can supervise multiple agent sessions.
- [[AIForMath]] - theorem-proving domain where subagents explore and repair formal proof branches.
