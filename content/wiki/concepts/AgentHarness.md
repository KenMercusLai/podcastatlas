---
title: "Agent Harness"
type: concept
tags: [agents, infrastructure, context, tooling]
sources: [142-yusen-de-chuangtou-guancha-di-2-ji-harness-xia-yige-zijie-2026-da-jihui-he-stanley-druckenmiller-lg4sphlaunrjuulqraxs-1gc5ufz, 20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto, tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3, dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd, ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan, vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1, vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1, ep124-weishenme-agent-shidai-cli-faner-chengle-zuiyoujie-lufh0-oxxxqthj-guc7o-1mexuax, ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz, weishenme-manus-bixu-chuhai-liaoliao-guochan-da-moxing-de-wenkesheng-kunjing-keji-luandun, vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1, vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1, dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian, 138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf, 139-agent-de-zongshu-he-su-yu-liao-agent-jishushi-openclaw-moment-bianjie-de-xiaomi-he-shehui-de-fushe-luffrgudeiighqxam49tfqci63no]
last_updated: 2026-07-08
---

# Agent Harness

Agent harness is the model-external system that lets an AI agent act in the world. In [[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]], [[LaiXinlu]] defines it as everything outside the model: tools, files, runtime state, context, memory, compression, handoff, permissions, and multi-agent governance.

[[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]] adds a work-environment analogy through [[MiniMax]] and [[HermesAgent]]: a harness is like giving a capable coworker tools, accounts, boundaries, feedback, and responsibility for delivery. The source emphasizes that harness design becomes more important once humans become the bottleneck in supervising many agents.

[[138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]] adds a model-training interpretation through [[LuoFuli]]. She treats [[OpenClaw]] and [[OpenCloud]] as a thick middle layer between humans and models: memory, workflow, cost routing, multi-agent structure, skills, simulated user agents, and evaluation all become part of how models should be post-trained and deployed.

[[139-agent-de-zongshu-he-su-yu-liao-agent-jishushi-openclaw-moment-bianjie-de-xiaomi-he-shehui-de-fushe-luffrgudeiighqxam49tfqci63no]] adds a technical-history interpretation through [[SuYu]]. He places the harness inside [[MemoryAutonomyFramework]]: tools, permissions, context, GUI/CLI/API access, and feedback are part of the autonomy layer that lets [[LanguageAgent]] systems become [[ComputerUseAgent]] and eventually [[UniversalDigitalAgent]] systems.

[[ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan]] adds a coding-tool comparison: [[GeminiCLI]] may benefit from loading large code context directly, while [[Cursor]] may use more engineered chunking, indexing, and retrieval to control cost. The episode therefore treats context strategy itself as a harness-level product choice.

[[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] adds a personal-agent harness case. [[JustinYan]]'s [[OpenClaw]]-inspired agent makes channels, schedules, trusted versus self-written [[AISkills]], virtual-machine isolation, separate accounts, and automatic versus explicit invocation part of the harness, not merely deployment details.

[[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]] adds a task-orchestration case through [[Superpowers]], [[ClaudeCode]], and [[Codex]]. The harness question becomes how to preserve brainstorm, design, plan, execution, review, repair, and subagent handoff without exhausting the main context or the human supervisor.

[[ep124-weishenme-agent-shidai-cli-faner-chengle-zuiyoujie-lufh0-oxxxqthj-guc7o-1mexuax]] adds the product-client layer through [[Podwise]]. The source shows that an [[AgentHarness]] works better when tools expose [[AgentOptimizedCLI]] commands with discovery, non-interactive authentication, structured output, idempotency, and repair-oriented errors, so the model can recover without a human reading docs.

[[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] adds a consumer-facing harness view through [[OpenClaw]]. [[YaGe]] and [[Haoda]] emphasize that the harness is what turns model ability into work: local runtime, tool calls, memory files, instruction following, context compaction, orchestration, and feedback loops let the agent run, observe failure, revise, and keep going.

[[ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz]] adds a day-to-day harness view. The useful harness is not only a tool list; it is the combination of project-local skills, permissioned accounts, computer-use or browser validation, scheduling, review loops, and release checks that make agents reliable enough for production tasks.

[[weishenme-manus-bixu-chuhai-liaoliao-guochan-da-moxing-de-wenkesheng-kunjing-keji-luandun]] adds a commercial-stability warning through [[Manus]]. The source says agent products may need to rework prompts, routing, and workflow logic when base models change, while 2B customers still expect stable delivery. In that sense, the harness must become a change-isolation and evaluation layer, not only an execution layer.

[[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]] adds a capability-versus-process warning through [[Fable5]]. The hosts see a large jump in practical coding behavior, but they also note that some of the improvement may come from harness and skill design rather than the base model alone. The harness therefore has to balance model power, verification loops, skill loading, and [[ModelRoutingCostControl]] rather than blindly maximizing process.

[[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]] adds a device-and-channel harness case through [[Codex]], [[OpenClaw]], and [[HermesAgent]]. The harness now includes browser extension access, lock-screen background operation, phone-to-computer remote control, IM sessions, group-chat memory, Obsidian/calendar/reminder access, and rules for when an agent can act without interrupting the human.

[[dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]] adds a failure-recovery case. [[OpenClaw]] can run scheduled tasks, modify files, call local tools, and update its own configuration, but the hosts describe cases where identical instructions produced different behavior or an update broke routines. That makes rollback, config isolation, service shutdown, logs, and narrow mounted directories harness requirements rather than optional safety polish.

[[142-yusen-de-chuangtou-guancha-di-2-ji-harness-xia-yige-zijie-2026-da-jihui-he-stanley-druckenmiller-lg4sphlaunrjuulqraxs-1gc5ufz]] adds [[DaiYusen]]'s investor/product version. He compares a harness to an operating system around a model-as-processor and argues that [[ClaudeCode]], [[Codex]], [[Manus]], and [[OpenCloud]] are not disposable wrappers when they own context, tools, runtime, sandbox, permissions, memory, user habits, and workflow data. The source makes harness value explicitly commercial: user loyalty and model-training feedback can accumulate in the harness layer.

## Layers
- Execution ability: CLI tools, file operations, browser use, language interpreters, code-registered tools, and protocol-style extensions.
- Context and environment: system prompt, working directory, dependency state, git state, [[AISkills]], [[PersistentAgentMemory]], context-window management, compression, and task handoff.
- Governance and orchestration: multi-agent roles, permissions, information boundaries, and safeguards against agents mutating the wrong artifacts.
- Feedback and learning: tests, deployments, result checks, memory updates, and successful workflows saved as [[AISkills]].
- Recovery and audit: logs, rollback points, kill switches, scheduled-task traces, and boundaries around which state the agent can mutate.

## Key Claims
- Harness matters because a model without tools and environment is an intelligent system without hands, memory, or operating context.
- The model is still the first source of agent intelligence; harness design should amplify the model rather than replace the model's judgment with rigid flow logic.
- Current agents may work better with more context, more action capacity, and less brittle programmatic control.
- CLI/Unix-style interfaces can be more natural for current models than newer abstractions because command-line patterns are deeply represented in training data.
- Good harnesses should align with the model's operating logic and remain useful as models improve; over-managed context or overly restrictive orchestration can become a bottleneck.
- Harnesses expose real-world feedback that lets agents recover, update memory, and support [[AgentSelfEvolution]] rather than merely produce one-shot answers.
- Harness design must account for [[AgentIdentityAndAuthentication]] when agents operate accounts, payments, code deployment, or other high-impact tools.
- Context loading, indexing, retrieval, and compression choices can determine whether a coding harness preserves enough codebase meaning for hard tasks.
- Personal agents need [[AgentPermissionBoundaries]] that distinguish safe automatic actions from powerful actions requiring explicit user intent.
- Tool clients should do stable deterministic work locally when possible, because forcing the model to recreate fixed conversions or exports wastes context and inference budget.
- Consumer-facing harnesses also need an entry point users will actually tolerate, such as [[IMAgentInterfaces]], plus local permissions that are powerful enough for work but bounded enough for safety.
- Scheduled personal routines extend the harness problem from single-task execution into triggers, recurrence, notifications, and auditability.
- Verification tools such as [[Playwright]] are harness components because they let the model observe runtime behavior and repair failures.
- Enterprise agent products need harness-level versioning, evaluation, and workflow governance so model upgrades do not silently break delivery.
- Stronger models reduce some supervision burden, but harnesses still need step acceptance, review, and cost controls for long tasks.
- Personal-agent harnesses increasingly cross devices and channels, so state, permissions, foreground/background behavior, and notification design become part of the harness rather than UI polish.
- Local harnesses must assume model behavior may drift under the same instruction, so scheduled automation needs stricter checks than one-shot interactive work.
- A harness can become training infrastructure when it generates agent traces, simulated user interactions, skills, and real workflow failures for [[AgentPostTraining]] and [[AgentRL]].
- Harnesses also define the agent's effective action space: a [[LanguageAgent]] may reason broadly, but computer-use reliability depends on the tools, GUI access, API access, memory, and feedback the harness exposes.
- A harness can become the user's durable product relationship when memory, configuration, workflow history, and habit live there rather than in the base model alone.

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
- [[OpenClaw]], [[AgentNativeSoftware]], and [[AgentPermissionBoundaries]] — personal-agent harness case added by the Fengyan Fengyu source.
- [[Superpowers]], [[SubagentWorkflow]], and [[AICodingVerification]] — orchestration and review-loop case added by Vol. 166.
- [[Podwise]] and [[AgentOptimizedCLI]] — CLI client-design layer added by EP124.
- [[IMAgentInterfaces]], [[LocalAgentExecution]], [[YaGe]], and [[Haoda]] — OpenClaw packaging and feedback-loop layer added by the 20-question episode.
- [[RoutineAgentAutomation]], [[Playwright]], and [[AgentPermissionBoundaries]] — scheduled, verifiable, permissioned workflow layer added by EP127.
- [[Manus]], [[AIAgentOverseasCommercialization]], and [[ModelProviderToolCompetition]] — commercial agent-stability and competition case added by the Keji Luandun source.
- [[Fable5]], [[GrillMeSkills]], [[OneShotAICoding]], and [[ModelRoutingCostControl]] — capability, skill-selection, and routing case added by Vol. 170.
- [[Codex]], [[OpenClaw]], [[HermesAgent]], [[IMAgentInterfaces]], and [[AgentPermissionBoundaries]] — cross-device and IM harness case added by Vol. 167.
- [[ProbabilisticSoftware]], [[LocalAgentExecution]], and [[ModelRoutingCostControl]] — Keji Luandun's local-agent reliability and cost-routing case.
- [[LuoFuli]], [[OpenCloud]], [[AgentPostTraining]], [[AgentRL]], and [[MemoVR]] — model-team training interpretation added by episode 138.
- [[SuYu]], [[LanguageAgent]], [[ComputerUseAgent]], [[UniversalDigitalAgent]], and [[MemoryAutonomyFramework]] — technical-history and autonomy-layer interpretation added by episode 139.
- [[DaiYusen]], [[ClaudeCode]], [[Codex]], [[Manus]], and [[OpenCloud]] — investor/product interpretation of harness as operating system, data flywheel, and user-retention layer added by episode 142.
