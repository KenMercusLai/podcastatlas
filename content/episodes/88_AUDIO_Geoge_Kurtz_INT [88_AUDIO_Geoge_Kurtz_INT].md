+++
title = 'Crowdstrike CEO: AI Cyberattack Wave, Hyperspeed Hacks, & The Patching Problem'
date = 2026-11-24T02:30:00Z
show = 'All-In with Chamath, Jason, Sacks & Friedberg'
source_url = 'https://dts.podtrac.com/redirect.mp3/traffic.libsyn.com/secure/allinchamathjason/88_AUDIO_Geoge_Kurtz_INT.mp3?dest-id=1928300'
duration = '3208'
draft = false
+++

# AI Agents, Cybersecurity, and the New “Break or Breach” Era

## Overview

CrowdStrike CEO George Kurtz explains how frontier AI and autonomous agents are reshaping cybersecurity. AI can now discover, combine, and exploit software vulnerabilities at unprecedented speed, giving ordinary criminals and hacktivists capabilities once associated with nation-states.

The discussion connects the rapid growth in disclosed vulnerabilities with a new operational dilemma: organizations must either deploy patches quickly and risk breaking complex systems, or delay and risk being breached. Kurtz argues that many recent outages may reflect this rushed remediation cycle rather than direct cyberattacks.

The conversation also examines autonomous attack frameworks, open-weight models, local AI, credential theft, deepfakes, and North Korean operatives obtaining legitimate remote jobs. Its central conclusion is that perfect code will not eliminate breaches; defenders need AI capabilities comparable to those available to attackers.

## Segmented Summary

[00:00] **Are recent outages evidence of a growing cyber threat?**

[Fact] The host asks whether Americans should be concerned about cyber threats amid a series of widely reported outages and growing public anxiety.

[Fact] Kurtz says the situation is serious because vulnerabilities are being found so quickly and at such volume that companies and governments are struggling to keep up.

[Fact] He distinguishes between confirmed cyberattacks and outages whose causes may instead involve IT changes, upgrades, or remediation work.

[01:38] **The lesson from an autonomous AI attack**

[Fact] Kurtz describes a watershed incident in which agents conducted an end-to-end autonomous attack after operating with limited guardrails.

[Fact] He argues that the most important lesson was not merely that autonomous attacks are possible, but that defenders lacked equivalent frontier-model capabilities to understand and respond.

[Fact] According to Kurtz, defenders had to turn to other models after frontier systems refused some of their requests.

[Inference] The incident illustrates an emerging asymmetry in which safety restrictions may constrain legitimate defenders more than attackers using unrestricted models.

[07:28] **Frontier models provide nation-state-level capabilities**

[Fact] CrowdStrike participates in trusted-access programs associated with Anthropic and OpenAI and works with their advanced models.

[Fact] Kurtz says frontier models, especially when paired with effective harness engineering, can give users capabilities that previously required the resources of a nation-state.

[Fact] Open-weight models may trail leading systems by only a few months, while post-training that removes refusal behavior can make them highly capable.

[Fact] Different models can also be combined to improve attack or security performance.

[10:16] **The adversary pyramid collapses into an “agent state”**

[Fact] Kurtz organizes cyber adversaries into hacktivists, e-crime groups, nation-states, and a new apex category he calls the “agent state.”

[Fact] In the traditional hierarchy, nation-states possessed the greatest sophistication, while hacktivists were more numerous but less capable.

[Fact] AI agents collapse this hierarchy by making nation-state-like capabilities available throughout the pyramid.

[Fact] Kurtz characterizes the result as both the creation of more adversaries and the democratization of destructive capability.

[12:22] **Motivations and the growth of cybercrime**

[Fact] Hacktivists may pursue political causes, experimentation, or amusement; e-crime groups seek money; nation-states pursue intelligence and strategic assets.

[Fact] AI agents are not a separate motivation group but a capability available to all of these actors.

[Fact] Kurtz describes e-crime as a $20 billion business driven by ransomware, extortion, and organizations paying to recover or prevent disclosure of their data.

[Fact] He says attackers currently have an advantage because powerful models and models stripped of guardrails are readily available.

[16:35] **AI drives an explosion in discovered vulnerabilities**

[Fact] Kurtz explains that Common Vulnerabilities and Exposures, or CVEs, are catalogued software vulnerabilities.

[Fact] He says 25 percent of all historically recorded CVEs were found during the current year discussed in the interview, with roughly 17,000 reported in 2026 at that point.

[Fact] The transcript attributes much of this increase to AI systems searching open-source and commercial software for weaknesses.

[Fact] Kurtz says the volume of vulnerability discoveries is doubling monthly and had risen 300 percent from one October to the next.

[18:44] **Old flaws become newly exploitable**

[Fact] Kurtz says most newly surfaced vulnerabilities were dormant flaws in existing code rather than defects created only by newly generated software.

[Fact] He cites a PHP vulnerability whose origins reportedly reach back to 2004.

[Fact] AI can connect multiple low-risk weaknesses into a chain that produces a high-risk compromise, including remote code execution and complete control of a system.

[Fact] Previously known issues that developers considered impractical to exploit can now be demonstrated as exploitable.

[Inference] The immediate danger comes not only from discovering more individual defects, but from AI’s ability to reason across combinations humans may not prioritize or detect.

[22:07] **The “break or breach” patching dilemma**

[Fact] Organizations once had weeks to test and deploy patches, but the window between disclosure and possible exploitation has sharply contracted.

[Fact] Kurtz calls the resulting choice “break or breach”: rush a patch and risk disrupting production, or delay and risk compromise.

[Fact] He says CEOs have asked whether they should take globally used services offline while patching serious exposures.

[Fact] Many recent outages may involve well-intentioned remediation efforts and failed or disruptive patches rather than attacks.

[Fact] Vulnerability discovery and patch creation are accelerating, but safe patch deployment remains a bottleneck.

[25:58] **Technical debt and forced modernization**

[Fact] Kurtz says the industry is now paying for 25 to 30 years of accumulated technical debt.

[Fact] Companies are becoming more willing to accept planned downtime when they cannot patch rapidly or install adequate mitigating controls.

[Fact] Cloud-native systems can replace temporary workloads from updated templates, making rapid remediation easier.

[Fact] Finance, healthcare, and critical infrastructure carry substantial legacy technology and need modernization to approach near-instantaneous patch cycles.

[29:38] **AI’s indirect role in major service outages**

[Fact] The discussion treats a Microsoft service outage as an infrastructure incident rather than a confirmed hack.

[Fact] Kurtz accepts the public post-mortem at face value but says AI may still be involved indirectly.

[Fact] His explanation is that AI discovers more weaknesses, prompting rushed patching that can trigger cascading operational failures.

[Inference] AI can therefore contribute to disruption even when no AI-powered attacker directly causes the outage.

[30:50] **Artex and autonomous attacks at scale**

[Fact] Kurtz describes Artex as an AI attack framework created by someone in China and released as open source before being removed.

[Fact] The framework can use agents and sub-agents to identify targets, map exposed systems, locate flaws, build exploits, escalate privileges, and steal data.

[Fact] Kurtz says such a framework can completely compromise a company in under three hours.

[Fact] In an investigation involving Korean banks, CrowdStrike reportedly found controllers running agents against approximately 200 organizations.

[Fact] Although the original project was removed, Kurtz says more than 12,000 forks existed and that CrowdStrike received an Artex-related incident call on the morning of the interview.

[33:31] **Open source as both risk and defensive resource**

[Fact] The host argues that open-source attack tools create danger but also provide transparency into their code and derivatives.

[Fact] Kurtz distinguishes open-source models from open-weight models, noting that access to weights enables organizations to modify model behavior.

[Fact] Customers want lower costs, AI sovereignty, and data sovereignty, motivating them to operate and post-train their own models.

[Fact] Organizations may run routine tasks on internal models and route harder requests to frontier systems.

[Inference] Open access expands offensive capability, but it also enables defenders to inspect tools, adapt models, and avoid total dependence on a small number of closed providers.

[36:55] **Local AI and hybrid model deployment**

[Fact] The speakers expect a large share of AI inference to move onto locally controlled computers and enterprise systems.

[Fact] Kurtz compares company-specific models to organizations creating their own Linux distributions from an existing base.

[Fact] He notes that large amounts of existing CPU, GPU, and neural-processing capacity remain underused across deployed devices.

[Fact] Frontier models will continue to handle the most demanding tasks, while local models may be sufficient for spreadsheets, financial models, writing, and presentations.

[Inference] A hybrid architecture combining private local inference with selective frontier-model access could reduce cost and capacity pressure while improving data control.

[42:33] **Phishing, session theft, and compromised email accounts**

[Fact] Kurtz repeats his principle that it is easier for attackers to log in than to break in.

[Fact] AI can automate highly convincing phishing campaigns designed to capture credentials.

[Fact] Multi-factor authentication does not solve every problem because attackers may steal an already authenticated session token.

[Fact] After entering a mailbox, attackers can create hidden routing rules, conceal relevant messages, and communicate with financial or business targets without the legitimate user noticing.

[Fact] The host describes organizations introducing multi-step human verification procedures for sensitive financial communications.

[46:21] **North Korean operatives hired as remote employees**

[Fact] Kurtz describes North Korean operatives applying for legitimate remote jobs, having corporate laptops delivered to intermediaries, and controlling the devices remotely.

[Fact] CrowdStrike first noticed unusual remote keyboard-and-mouse devices and used intelligence analysis to connect the activity to North Korea.

[Fact] Kurtz says CrowdStrike’s first 40 customer notifications about suspected fraudulent employees were correct.

[Fact] One investigated employee had been hired without appearing on camera or meeting anyone in person.

[Fact] In another case, a manager reportedly resisted terminating the fraudulent employee because the person produced the best work on the team.

[Inference] Remote hiring can transform identity verification and insider-risk management into core cybersecurity controls rather than ordinary HR procedures.

[50:06] **Why perfect code would not end breaches**

[Fact] Kurtz rejects the idea that AI-rewritten, vulnerability-free code would eliminate cyber incidents.

[Fact] Even with perfect code, attackers could still exploit identity, authentication, session management, and human behavior.

[Fact] He expects an enduring “spy versus spy” contest between offensive AI and defensive AI.

[Fact] Defensive systems will need to continuously test environments, identify attack paths, and close them before adversaries can use them.

[51:40] **Corporate counterattacks and preparedness**

[Fact] Kurtz says offensive cyber operations in the United States are generally government authorities rather than ordinary corporate powers.

[Fact] He recommends that companies prioritize strong defense and work with law enforcement when incidents occur.

[Fact] Large organizations should establish relationships with local FBI personnel before a crisis rather than making first contact during an active breach.

[Inference] Effective readiness depends as much on prior coordination and incident-response relationships as on technical security products.

## Podcast Review/Summary

This episode’s strongest contribution is its coherent explanation of how several apparently separate developments—autonomous agents, soaring CVE counts, emergency patches, outages, open-weight models, and identity fraud—form one connected cybersecurity transition. The “break or breach” framing is particularly useful for understanding why defensive work itself can cause visible disruption.

The discussion also provides accessible examples of sophisticated threats, including chained vulnerabilities, stolen session tokens, autonomous attack frameworks, and fraudulent remote employees. These examples make the episode valuable to executives, security leaders, IT operators, investors, and anyone responsible for enterprise risk.

Its main limitation is that many statistics, incident interpretations, and named technologies are presented conversationally without supporting documentation in the transcript. Some claims also rely on Kurtz’s direct experience with customers and cannot be independently evaluated from the episode alone.

[Inference] The episode is best treated as an informed strategic briefing rather than a complete technical or evidentiary account. Its durable message is that cybersecurity will remain an adversarial contest, and organizations must modernize systems, strengthen identity controls, equip defenders with advanced AI, and prepare response relationships before incidents occur.
