---
title: "AI Coding Verification"
type: concept
tags: [ai-coding, software-engineering, verification]
sources: [duihua-minimax-yan-junjie-m3-10x-jihua-10t-moxing-he-zhineng-de-zhongju-lqtilt8flvmv99v0gshhyfyraibe, ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan, ai-hui-xie-daima-le-weishenme-ni-haishi-zuo-bu-chu-chanpin-1]
last_updated: 2026-07-07
---

# AI Coding Verification

AI coding verification is the shift in bottleneck from generating code to proving that the code is correct, maintainable, reviewable, and safe to ship. In [[duihua-minimax-yan-junjie-m3-10x-jihua-10t-moxing-he-zhineng-de-zhongju-lqtilt8flvmv99v0gshhyfyraibe]], [[ZhangJiayuan]], [[HeTao]], and [[YanJunjie]] all treat AI coding as a production-speed breakthrough whose next constraint is engineering discipline.

[[ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan]] adds a productivity-counterexample through [[METR]]: on familiar repositories, experienced developers may spend less time on direct coding, search, and debugging but more time waiting, conversing, and reviewing AI output. The source therefore treats verification overhead as a practical reason [[VibeCoding]] is not automatically faster.

[[ai-hui-xie-daima-le-weishenme-ni-haishi-zuo-bu-chu-chanpin-1]] adds the practitioner workflow version. The hosts describe asking AI to write tests first, measure coverage, run end-to-end checks, generate screenshots, produce documentation, and emit detailed logs so later debugging has enough observable context. The same source warns that legacy systems should be documented and tested before broad AI refactoring.

## Key Claims
- AI coding makes implementation cheaper, but architecture, roadmap choice, complexity control, tests, review, and long-term maintenance still matter.
- Generated code should not reduce the developer's responsibility for commits made under their own identity.
- Existing one-shot SWE-style benchmarks do not fully test whether an agent can care for a long-lived codebase.
- Teams may need to invest as much effort into verification harnesses as they invest into production acceleration.
- [[AISkills]] can package engineering standards such as Clean Code, Google best practices, and Amazon best practices for agent use.
- [[AIAssistedSoftwareDevelopmentRisk]] is the broader failure mode; AI coding verification is the operational response inside engineering workflows.
- AI coding can be slower when review and interaction overhead outweigh generation savings, especially in familiar complex repositories.
- Compilation, lint, tests, diffs, and runtime behavior make coding unusually verifiable compared with open-ended text, image, or video generation.
- AI can help implement verification itself, but only when the user explicitly asks for tests, screenshots, logs, and review rather than accepting generated code as finished.
- Legacy-code modernization should begin with reading, documentation, tests, and observability before asking AI to rewrite core logic.

## Connections
- [[AgenticWorkflow]] — the workflow pattern that accelerates production and creates verification pressure.
- [[MiniMaxM3]] and [[MultiCard]] — model and practitioner case from the source.
- [[HeTao]] and [[ZhangJiayuan]] — guests emphasizing engineering responsibility and maintainer taste.
- [[HumanJudgmentUnderAI]] — the human still owns review, tradeoffs, and taste.
- [[ContextEngineering]] — verification depends on codebase context, tests, rules, and project standards.
- [[METR]], [[Cursor]], and [[VibeCoding]] — productivity and review-overhead case added by EP108.
- [[AIEngineeringThinking]], [[ShengpaiNotice]], and [[ZhangLe]] — workflow and legacy-system cases added by the Keji Luandun episode.
