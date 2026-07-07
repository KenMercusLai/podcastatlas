---
title: "AI Skills"
type: concept
tags: [skills, agents, workflow]
sources: [20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto, gaoshou-zenme-yong-ai-putongren-zenme-xue-ai-touziren-ruhe-tou-ai-duitan-kedaibiao-lizheng-ljqyo4tz0o2-pmsl-mjx6umsuzsc, ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun, agent-yuannian-di-500-tian-shenme-zai-xiaoshi-shenme-zai-dansheng-weishenme-women-bugai-zai-touzi-gui-siwei-de-ruanjian-lhwdxfpke3bmamjk4e6knk-5sn-b, duihua-minimax-yan-junjie-m3-10x-jihua-10t-moxing-he-zhineng-de-zhongju-lqtilt8flvmv99v0gshhyfyraibe, tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3, dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd, ai-hui-xie-daima-le-weishenme-ni-haishi-zuo-bu-chu-chanpin-1, vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1, vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1, ep124-weishenme-agent-shidai-cli-faner-chengle-zuiyoujie-lufh0-oxxxqthj-guc7o-1mexuax, ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz, vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1, vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1, e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf]
last_updated: 2026-07-08
---

# AI Skills

AI skills are reusable instructions and process packages that help an AI complete a defined class of work. In [[gaoshou-zenme-yong-ai-putongren-zenme-xue-ai-touziren-ruhe-tou-ai-duitan-kedaibiao-lizheng-ljqyo4tz0o2-pmsl-mjx6umsuzsc]], strong skills are described as codifying implicit knowledge: boundaries, steps, tools, quality standards, and required context. In [[ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun]], skills appear more operationally through background delegation and debate-style agent analysis. [[agent-yuannian-di-500-tian-shenme-zai-xiaoshi-shenme-zai-dansheng-weishenme-women-bugai-zai-touzi-gui-siwei-de-ruanjian-lhwdxfpke3bmamjk4e6knk-5sn-b]] adds a market and ecosystem view through PPT skills, Feishu-related skills, [[OpenCloud]], and [[CodePilot]]. [[duihua-minimax-yan-junjie-m3-10x-jihua-10t-moxing-he-zhineng-de-zhongju-lqtilt8flvmv99v0gshhyfyraibe]] adds an engineering-quality use case: [[HeTao]] suggests packaging Clean Code, Google best practices, Amazon best practices, and similar standards into skills or context for agents. [[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]] adds a memory-overlap view: in [[ClaudeCode]]-style systems, skills, memory files, task reports, experience, and SOPs can share markdown/file mechanics and be updated by agents over time.

[[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]] adds [[HermesAgent]] as a clearer memory-to-skill case. The source says successful workflows can be saved as skills so the agent can reproduce the correct path next time, making skills part of [[AgentSelfEvolution]] rather than only user-authored prompt packages.

[[ai-hui-xie-daima-le-weishenme-ni-haishi-zuo-bu-chu-chanpin-1]] adds an everyday engineering-practice version. Tests, logging policies, documentation expectations, code-review prompts, audit rubrics, and business handoffs can act like skills when they repeatedly guide AI through the same class of work.

[[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] adds a personal-agent version through [[OpenClaw]]. [[JustinYan]] treats skills as lighter than protocol-heavy tool integration and describes a stronger loop where an agent can inspect home services, infer what they can do, and write new skills for itself. The same source adds a security split between trusted skills and agent-written skills, making [[AgentPermissionBoundaries]] part of skill design.

[[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]] adds [[WangJunyu]]'s "trainable newcomer" interpretation. Skills are not only memory about user preferences; they preserve how a task should be done, so feedback can become a reusable work method for an agent operating in a company or personal workflow.

[[ep124-weishenme-agent-shidai-cli-faner-chengle-zuiyoujie-lufh0-oxxxqthj-guc7o-1mexuax]] adds a CLI-composition version through [[Podwise]]. Skills sit above [[AgentOptimizedCLI]] atoms such as search, process, get, and export, letting the user describe an outcome while the agent chooses the command sequence. The source treats this as a practical shift from operating tools to specifying tasks.

[[ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz]] adds a selection and maintenance lens. A skill should survive because it handles repeated work, compensates for a weak domain, or helps an agent verify real output; popularity alone is a weak signal. The episode also treats self-written skills as disposable workflow assets: if a prompt, check, support reply, podcast-processing step, or deployment routine repeats enough times, it can become a skill and later be deleted or revised when the workflow changes.

[[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] adds an ecosystem and consumer-agent version through [[OpenClaw]]. [[YaGe]] describes maintaining personal preference or "axiom" skills for research and synthesis, while the episode treats open-source skills, user PRs, skill markets, and AI-readable smart-home APIs as ways ordinary users can expand what an agent can do.

[[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]] adds a manual skill-selection contrast through [[GrillMeSkills]]. The source says a full automatic bundle such as [[Superpowers]] can help non-experts by enforcing the whole software process, but experienced users may prefer to manually trigger requirement grilling, specs, ADRs, PRDs, or issue decomposition to save tokens and avoid over-structuring small tasks.

[[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]] adds a product-prototype path from conversation to skill. The hosts describe tweaking an agent's behavior through natural language until it reliably handles article selection, translation, note saving, or todo aggregation; once repeated, that behavior can become a reusable workflow asset even if it is not identical to a formal skill file.

[[e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf]] adds the business-software and personal-skill disruption angle. The episode argues that B2B software know-how can become explicit, shareable, and repackaged as skills, weakening software moats based on hidden workflow knowledge. It also gives a personal example where a data-visualization workflow becomes a skill, creating the feeling that years of craft can be compressed into a reusable procedure.

## Key Claims
- A useful skill is more than style imitation.
- Skills become more valuable when tied to [[AgenticWorkflow]] and real tools.
- [[SubagentWorkflow]] shows one practical skill pattern: delegating large or complex work to background agents and integrating results later.
- Skill commercialization may work better as skill as a service than as raw skill-file sales.
- Simple skills may be absorbed by stronger models, while trusted agents, brands, and tool ecosystems may own the longer-term user relationship.
- Skills become more useful when they can call [[AgentFacingInterfaces]] rather than only instruct a chat model.
- Engineering skills can help convert software taste, review standards, and maintainability rules into reusable [[AICodingVerification]] context.
- Skills can sit inside an [[AgentHarness]] as selectively loaded files whose descriptions help the model decide whether to pull in the full procedure.
- Skills can also be generated from successful agent work traces, where [[PersistentAgentMemory]] compresses experience into reusable procedures.
- Practical skills can encode [[AIEngineeringThinking]]: require tests before implementation, collect logs before debugging, and make domain acceptance criteria explicit.
- Personal-agent skills need permission tiers because a markdown-like procedure can still expose private data or operate a powerful tool.
- Skills can make agent training resemble onboarding: a human corrects an agent's work method, and the corrected procedure becomes reusable in future tasks.
- Skills become more powerful when the underlying tool offers small, stable CLI actions that can be discovered, combined, and debugged without custom integration code.
- Skills can turn users into partial developers because a reusable procedure, API description, or tool instruction can become part of the agent's future capability.
- Verification, testing, and release skills may matter more than generic framework skills because they let the agent prove that work is actually done.
- Skills can become [[RoutineAgentAutomation]] when paired with scheduled execution for email, notes, analytics, cost monitoring, or research workflows.
- Skill bloat is a real context and behavior risk; unused fashionable skills should be removed when they do not match actual recurring work.
- The stronger the model, the more important skill loading discipline becomes: [[Fable5]] can do more in one pass, but automatically wrapping every task in a heavy process can waste [[AIInferenceCostStructure]].
- Skills can emerge from repeated personal-agent conversations, but should be hardened into deterministic tools or explicit procedures once the workflow becomes stable enough to justify engineering.
- Skills can expose business-process know-how that previously lived inside software vendors, consultants, or individual experts.

## Connections
- [[ContextEngineering]] — skills package and reuse context.
- [[Codex]] and [[ClaudeCode]] — agent tools that can benefit from structured skills.
- [[HumanJudgmentUnderAI]] — skills improve preparation, but users still need judgment in live contexts.
- [[OpenCloud]] and [[CodePilot]] — projects discussed as part of the emerging skill ecosystem.
- [[AICodingVerification]] — software-quality context that can be expressed through skills.
- [[Deerflow]] and [[HeTao]] — open-source engineering case added by the MiniMax roundtable.
- [[AgentHarness]], [[PersistentAgentMemory]], and [[LearnClaudeCode]] — skill-memory boundary and Claude Code learning context added by the Lai Xinlu source.
- [[HermesAgent]] and [[AgentSelfEvolution]] — memory-to-skill loop added by the Hermes Agent source.
- [[AIEngineeringThinking]], [[AICodingVerification]], and [[ShengpaiNotice]] — engineering-process skill pattern added by the Keji Luandun episode.
- [[OpenClaw]], [[AgentSelfEvolution]], and [[AgentPermissionBoundaries]] — personal-agent skill loop added by the Fengyan Fengyu source.
- [[WangJunyu]], [[DigitalEmployees]], and [[BusinessLedAITransformation]] — trainable-agent and organizational-workflow interpretation added by the Shengdong Jixi crossover.
- [[Podwise]] and [[AgentOptimizedCLI]] — CLI-composition skill case added by EP124.
- [[OpenClaw]], [[YaGe]], [[Haoda]], [[IMAgentInterfaces]], and [[LocalAgentExecution]] — skill-market and consumer-agent case added by the 20-question episode.
- [[RoutineAgentAutomation]], [[Playwright]], and [[WeChatReading]] — repeated automation, verification, and personal knowledge cases added by EP127.
- [[GrillMeSkills]], [[Superpowers]], [[Fable5]], and [[ModelRoutingCostControl]] — manual skill-selection and token-control contrast added by Vol. 170.
- [[IMAgentInterfaces]], [[OpenClaw]], [[HermesAgent]], and [[PersistentAgentMemory]] — conversation-to-workflow asset path added by Vol. 167.
- [[ModelContextProtocol]], [[LanguageUserInterface]], and [[HeadlessSoftware]] — E155's skill-plus-connectivity and software-moat disruption frame.
