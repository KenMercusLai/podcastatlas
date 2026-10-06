---
title: "Agent Permission Boundaries"
type: concept
knowledge_schema: synthesis-v1
tags: [agents, security, governance]
sources:
  - vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1
  - e249-token-jingji-zhuandian-openclaw-hermes-dao-bendi-ziyan-de-agent-jinhua-zhi-lu-6242033d-a14a-44e3-a622-cbfc7d3c3817
  - vol-171-jiaru-women-you-wuxian-token-1-6682-1
  - moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk
  - keyi-gei-nide-agent-fa-yidian-linghuaqian-le-s10e22-9a652c19-ceb3-46c2-87b4-bca36e684311
  - tech-20251225-1225-mp-tech-pod-128-tech-20251225-1225-mp-tech-pod-128
  - tsr-s3-dansiroker-v3-tsr-s3-dansiroker-v3
  - e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923
  - tech-20260213-tech-pod-128-tech-20260213-tech-pod-128
  - 1-ren-gongsi-kang-5-ge-ren-de-huo-hai-yao-guan-50-ge-agents-s10e18-e3a21dde-0bba-4ec2-bf12-5043500ae5c6
  - vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1
  - 20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto
  - vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1
  - vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1
  - ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz
  - vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1
  - dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian
  - wwdc-26-bu-shang-le-ai-dan-li-zhenzheng-de-ai-zhushou-hai-cha-shenme-s10e15-9ab1512e-a4a8-4ea6-81b5-0ac7ec677d2d
  - women-shi-ruhe-dingyi-openclaw-for-teams-xin-chanpin-xingtai-de-duitan-kuse-junior-lianchuang-jian-cto-yuhao-lkp1a0todflxoyycyo3zhrap3ebv
  - ep-30-openclaw-the-open-source-ai-agent-that-got-its-creator-hired-by-openai
last_updated: 2026-10-07
---

# Agent Permission Boundaries

## Definition

Agent permission boundaries are the enforceable limits that determine which data, tools, accounts, devices, funds, communications, and physical or social actions an agent may observe or perform automatically, which require approval, and which remain prohibited.

## Current Synthesis

Permission design is part of the [[AgentHarness]] because an agent's practical capability is defined by the authority attached to its tools, not only by model intelligence. Useful systems need more than a binary allow/deny switch: read and write authority, reversible and irreversible actions, task scope, time window, budget, identity, destination, bystander effects, and approval rules should be separable. Least privilege works best with isolated environments, temporary grants, logs, stop and revoke controls, backups, and recovery paths. Repeated confirmations can create [[AgentApprovalFatigue]], but broad standing access converts a mistaken goal, injected instruction, malicious skill, or compromised service into durable harm.

## Key Claims

- Permission scope should follow task, resource, duration, impact, and reversibility rather than model confidence alone.
- Observation, low-impact execution, external communication, spending, deletion, credential use, and production writes require progressively stronger controls.
- Temporary grants, separate identities, isolated environments, logs, backups, revocation, and rollback make delegated authority recoverable.
- Skills, webpages, social platforms, and other third-party inputs are part of the permission boundary because they can redirect an otherwise authorized agent.
- Team agents require role- and organization-aware authority, attribution, disclosure controls, and audit beyond a personal owner's preferences.
- Permission design must include people affected by sensing, messages, purchases, reputation, or physical-world action even when they do not operate the agent.

## Evidence

### Graduated authority and task-scoped access
- [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] separates trusted from agent-written skills, uses a virtual machine and separate accounts, and withholds main-account access.
- [[moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk]] describes temporary task authority that is withdrawn after completion while recognizing that excessive prompts create approval fatigue.
- [[wwdc-26-bu-shang-le-ai-dan-li-zhenzheng-de-ai-zhushou-hai-cha-shenme-s10e15-9ab1512e-a4a8-4ea6-81b5-0ac7ec677d2d]] argues that assistants need graduated authority and user-specific confirmation rules rather than no access or full access.
- [[vol-160-yi-nian-duo-yihou-zai-liao-ai-xie-daima-vibe-coding-1-6623-1]] treats YOLO execution as a scoped coding mode and recommends separation for concurrent agents rather than machine-wide trust.

### Irreversible actions, credentials, and money
- [[e249-token-jingji-zhuandian-openclaw-hermes-dao-bendi-ziyan-de-agent-jinhua-zhi-lu-6242033d-a14a-44e3-a622-cbfc7d3c3817]] pairs broader autonomy with backup, sandboxing, logging, stop controls, and recovery after examples involving data deletion and credential mutation.
- [[keyi-gei-nide-agent-fa-yidian-linghuaqian-le-s10e22-9a652c19-ceb3-46c2-87b4-bca36e684311]] scopes purchases by task, amount, category, merchant context, duration, and reauthorization through payment mandates.
- [[vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1]] shows that hiding plaintext credentials does not remove an agent's practical power to authenticate, contact services, and act.
- [[1-ren-gongsi-kang-5-ge-ren-de-huo-hai-yao-guan-50-ge-agents-s10e18-e3a21dde-0bba-4ec2-bf12-5043500ae5c6]] records red lines around deletion, protocol changes, spending, and socially damaging behavior.

### Persistent, repeated, and cross-channel action
- [[ep127-cong-skills-dao-zidonghua-gongzuoliu-lun-agent-ruhe-jieguan-zhenshi-shengchanli-lntwhoxpi433ptke-nhohb-5lbpz]] applies permissions to scheduled email, notes, monitoring, release, and research routines whose mistakes can repeat.
- [[vol-167-token-ru-liushui-agent-si-chaoyang-1-6653-1]] extends the boundary across browser extensions, remote control, locked-screen background work, messaging threads, and separate topic contexts.
- [[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]] shows the core local-versus-cloud tradeoff: local context makes agents useful while exposing files, devices, and accounts.
- [[dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]] reports that a container is only a partial boundary when sensitive directories, browser sessions, tokens, network access, or password-manager capabilities are mounted inside it.

### Enterprise roles, data, and reputation
- [[e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923]] makes broad organizational read access useful but keeps writes, sensitive data, security decisions, and final review narrower and auditable.
- [[women-shi-ruhe-dingyi-openclaw-for-teams-xin-chanpin-xingtai-de-duitan-kuse-junior-lianchuang-jian-cto-yuhao-lkp1a0todflxoyycyo3zhrap3ebv]] adds role-based company memory, phishing, prompt injection, malicious skills, account misuse, data leakage, and reputational harm to the enterprise boundary.

### Third-party inputs and skill supply chains
- [[tech-20260213-tech-pod-128-tech-20260213-tech-pod-128]] reports sensitive-data exposure on an agent social platform, showing that “only talking” to a third-party environment can leak account or memory context.
- [[ep-30-openclaw-the-open-source-ai-agent-that-got-its-creator-hired-by-openai]] reports a third-party OpenClaw skill performing data exfiltration and prompt injection, and recommends sandboxing away from the primary machine.

### Devices, bystanders, commerce, and physical context
- [[tech-20251225-1225-mp-tech-pod-128-tech-20251225-1225-mp-tech-pod-128]] shows that smart glasses can capture or interpret nearby people before any explicit downstream action occurs.
- [[tsr-s3-dansiroker-v3-tsr-s3-dansiroker-v3]] presents consent mode as a boundary that withholds recording until a new voice opts in.
- [[vol-171-jiaru-women-you-wuxian-token-1-6682-1]] extends permissions to household images, objects, routines, private spaces, and dangerous fabrication knowledge.
- [[vol-162-keji-kuaile-xingqiu-44-xin-moxing-sotamen-qihe-xinchun-1-6628-1]] connects shopping and payment agents to product, address, substitution, and human-confirmation controls.

## Counterevidence & Qualifications

- Narrow permissions can make an agent too weak to complete useful cross-system work, so the goal is proportional authority rather than universal denial.
- Frequent approval prompts can train users to click through warnings or grant standing access; good boundaries need task-level grouping and risk-sensitive escalation.
- Sandboxes, containers, and separate devices do not protect resources intentionally mounted, credentials deliberately exposed, or external actions explicitly allowed.
- Cross-agent review and model refusals can reduce some failures but do not replace enforceable controls, attribution, recovery, or human accountability.
- Many examples are practitioner reports, product proposals, or host-reported incidents rather than controlled comparisons of permission systems.
- The EP30 malicious-skill, corporate-ban, and autonomous-behavior claims are not independently documented in the supplied source and should not be generalized into prevalence estimates.

## What Changed

- Reorganized the concept around graduated authority, recoverability, third-party inputs, organizational roles, and affected non-users.
- Added imported skills as a distinct supply-chain path through which authorized tools can be redirected.
- Strengthened sandbox guidance by making clear that mounted data, accounts, and network capabilities remain exposed.
- Preserved approval fatigue as a reason to design task-scoped grants rather than defaulting to standing access.

## Related Concepts

- [[AgentHarness]] - system layer where authority, tools, observation, and approval are enforced.
- [[AgentEnvironmentIsolation]] - separates agent execution from primary systems and sensitive state.
- [[AgentSkillSupplyChainRisk]] - narrows the third-party package and hidden-instruction threat.
- [[AgentIdentityAndAuthentication]] - attributes actions to an agent, user, role, and delegated authority.
- [[AgentSpendControls]] - applies task, amount, merchant, duration, and liability limits to payments.
- [[AgentApprovalFatigue]] - explains why repeated prompts can undermine otherwise strict controls.
- [[LocalAgentExecution]] - increases contextual usefulness and local blast radius together.
- [[EnterpriseAgentGovernance]] - extends personal permission rules into organizational policy and audit.
- [[ConsentBasedRecording]] - protects bystanders affected by wearable or ambient sensing.
