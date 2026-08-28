---
title: "Vibe Coding"
type: concept
tags: [ai, coding, software, product-development]
knowledge_schema: synthesis-v1
sources:
  - vol-171-jiaru-women-you-wuxian-token-1-6682-1
  - moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk
  - tech-20260313-0313-mp-tech-pod-128-tech-20260313-0313-mp-tech-pod-128
  - e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb
  - vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1
  - ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan
  - ai-hui-xie-daima-le-weishenme-ni-haishi-zuo-bu-chu-chanpin-1
  - ba-7-wei-heikesong-xuanshou-qing-jin-boke-guanjun-guai-cai-he-48-xiaoshi-bumian-de-yexinjia-lhozhsuqbw8csa5tj5tqc7saqrex
  - vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1
  - vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1
  - vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1
  - vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1
  - biancheng-de-neiranji-shidai-neihe-konghuang-71-1-71-1
  - zhongwen-boke-huohuashi-yu-zhen-og-neihe-konghuang-72-1-72-1
  - 1-yi-token-julebu-jibaole-ai-de-ranliao-bugoule-duitan-yu-wenyuan-aliyun-bailian-jishu-fuzeren-ltn5k9jd9e04i5mfdkdo-ycoslsm
  - vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1
  - opc-de-zhenzheng-nanti-shi-ai-hai-mei-xuehui-ti-ni-ba-dongxi-mai-chuqu-1
  - dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian
  - tsr-ycoffsite-pg-audioonly-final-tsr-ycoffsite-pg-audioonly-final
  - all-in-with-chamath-jason-sacks-friedberg-former-intel-ceo-on-what-went-wrong-whats-next-lovable-ceo-on-the-real-promise-of-vibe-coding-42106400
last_updated: 2026-08-29
---

# Vibe Coding

## Definition
Vibe coding is AI-assisted software creation in which people express intent, context, examples, corrections, and acceptance criteria in natural language while model-backed tools or agents generate, modify, test, and explain code.

## Current Synthesis
Across the bounded sources, vibe coding is no longer just autocomplete or throwaway demo generation. It expands who can build software and shifts the human role toward specifying goals, supplying domain context, supervising agents, verifying behavior, and deciding what is worth releasing. The most durable synthesis is conditional: vibe coding becomes useful when paired with architecture, tests, security, permissions, product judgment, customer pull, and maintenance ownership. The Lovable interview adds a stronger production-platform case, showing how hosting, payments, integrations, model routing, security scanning, and business workflows can turn AI-generated apps into internal tools or revenue-producing products.

## Key Claims
- Capability expansion is the stable core: vibe coding lets more people attempt software work and lets experienced builders explore more ideas, but speed gains vary by task and reviewer skill.
- Production viability depends on engineering ownership: tests, security, architecture, data handling, permissions, deployment, and rollback matter more as generated software touches real users or accounts.
- The human bottleneck shifts upward from syntax to product framing, domain knowledge, decomposition, context management, taste, verification, customer discovery, and distribution.
- Agentic and high-token workflows create new operating costs, including quota pressure, model-routing choices, context loss, repeated regressions, and review burden.
- Nontechnical and cross-functional use is strongest around bounded workflows, internal tools, hackathons, side projects, and domain-specific pain where the builder understands the problem.
- Generated code does not by itself create a business; willingness to pay, sales, trust, support, compliance, and customer pull remain outside the model's default competence.
- As tools gain local or platform permissions, vibe coding overlaps with agent governance because generated software and agents can act in files, browsers, accounts, and production systems.

## Evidence
- Capability expansion and natural-language programming: [[vol-171-jiaru-women-you-wuxian-token-1-6682-1]], [[vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1]], and [[tsr-ycoffsite-pg-audioonly-final-tsr-ycoffsite-pg-audioonly-final]] frame AI coding as a new programming mode where English-like instructions, abundant tokens, and generated code can change who builds and how fast ideas are explored.
- Engineering controls and verification: [[moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk]], [[e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb]], and [[dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]] keep tests, review, deterministic subtools, permissions, prompt injection, local files, and regression control central.
- Product and business bottlenecks: [[ai-hui-xie-daima-le-weishenme-ni-haishi-zuo-bu-chu-chanpin-1]], [[opc-de-zhenzheng-nanti-shi-ai-hai-mei-xuehui-ti-ni-ba-dongxi-mai-chuqu-1]], and [[all-in-with-chamath-jason-sacks-friedberg-former-intel-ceo-on-what-went-wrong-whats-next-lovable-ceo-on-the-real-promise-of-vibe-coding-42106400]] argue that product choice, sales, customer pull, data, strategic experiments, and business operations remain decisive after the code is generated.
- Nontechnical and cross-functional adoption: [[ba-7-wei-heikesong-xuanshou-qing-jin-boke-guanjun-guai-cai-he-48-xiaoshi-bumian-de-yexinjia-lhozhsuqbw8csa5tj5tqc7saqrex]], [[vol-165-zuoke-shengdongjixi-longxia-he-vibe-coding-zhengruhe-gaibian-womende-siwei-laizi-xiaobai-chuangyezhe-he-gongchengshi-butong-shijiao-de-taolun-1-6642-1]], and [[all-in-with-chamath-jason-sacks-friedberg-former-intel-ceo-on-what-went-wrong-whats-next-lovable-ceo-on-the-real-promise-of-vibe-coding-42106400]] show hackathon, beginner, founder, designer, and operator use cases where domain knowledge matters as much as coding knowledge.
- Token, model, and workflow economics: [[1-yi-token-julebu-jibaole-ai-de-ranliao-bugoule-duitan-yu-wenyuan-aliyun-bailian-jishu-fuzeren-ltn5k9jd9e04i5mfdkdo-ycoslsm]], [[ep108-vibe-coding-da-dizhen-cursor-dingjia-zhengyi-windsurf-shougou-fengbo-moxing-changshang-qin-erzi-men-you-jiang-ruhe-jinchang-lqn-icq1xqgk7xxxxzrpunj4fan]], [[vol-166-xianliao-cong-gemini-dao-ai-de-jiasu-yu-hundun-1-6650-1]], and [[vol-170-fable-5-zhongchujianghu-gpt-rengxu-nuli-1-6674-1]] connect coding agents to token scarcity, pricing, model selection, Fable-style artifacts, and the need to route work to the right model or workflow.
- Software-era work shift: [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]], [[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]], [[biancheng-de-neiranji-shidai-neihe-konghuang-71-1-71-1]], and [[zhongwen-boke-huohuashi-yu-zhen-og-neihe-konghuang-72-1-72-1]] place vibe coding inside a broader move toward agentic software, changing programming identity, and anxiety about skill formation.
- Production platform case: [[all-in-with-chamath-jason-sacks-friedberg-former-intel-ceo-on-what-went-wrong-whats-next-lovable-ceo-on-the-real-promise-of-vibe-coding-42106400]] adds Lovable's claims about hosted apps, payments, security scanning, model routing, open-weight and frontier models, reinforcement-learning loops, and businesses running on AI-built software.

## Counterevidence & Qualifications
Several sources warn that vibe coding can slow experienced developers when review and correction costs exceed generation speed. Beginners can ship subtle defects because they cannot recognize architecture, security, edge-case, or maintainability problems. Internal tools and self-use apps are not the same as regulated, public, or enterprise software. High-token workflows can make costs and quotas real constraints. AI-built products still need distribution, pricing, support, compliance, and trust. Local agents and platform integrations increase capability but also increase blast radius when permissions are broad or generated code is accepted without review.

## What Changed
- Migrated the page to the synthesis-v1 concept schema and compressed the legacy source-by-source accumulation into claim-grouped evidence.
- Added Lovable's production-platform account, shifting the synthesis from demos and coding assistance toward hosted, secure, integrated, business-facing software.
- Strengthened the qualification that generated code does not solve product judgment, customer pull, distribution, or operational ownership.

## Related Concepts
- [[AICodingVerification]] - verification is the main boundary between plausible generated code and trustworthy software.
- [[AIEngineeringThinking]] - decomposition, context design, and review remain core human work in vibe coding.
- [[ProductionVibeCoding]] - production subset where generated software becomes hosted, secure, integrated, and business-facing.
- [[AgentPermissionBoundaries]] - local and platform permissions determine the blast radius of agentic coding.
- [[ModelRoutingCostControl]] - model selection and token economics shape coding-agent quality and cost.
- [[OnePersonCompany]] - AI coding makes solo execution cheaper but does not remove sales, compliance, or delivery work.
- [[HumanJudgmentUnderAI]] - product taste, final responsibility, and acceptance decisions remain human-heavy.
- [[CodingDemocratization]] - vibe coding expands software creation beyond traditional programmers.
