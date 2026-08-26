---
title: "Model Context Protocol"
type: concept
tags: [ai, agents, protocols, infrastructure]
sources:
  - all-in-with-chamath-jason-sacks-friedberg-microsoft-ceo-satya-nadella-on-ais-business-revolution-what-happens-to-saas-openai-and-microsoft-live-from-davos-39818140
  - ep119-duihua-liu-kefan-yong-try-catch-finally-gei-duli-zuo-chanpin-de-neihao-xie-ge-chuli-liucheng-ludjc3ab-jbwpci6tpaajtffsblx
  - e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf
  - dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian
  - guanyu-ai-kaiyuan-shangyehua-yu-quanqiuhua-de-jingyan-jiaoxun-he-fangfalun-duitan-pingcap-cto-dongxu-ljw8va0evobhz4ojzrulqzjvxw5
  - weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3
knowledge_schema: synthesis-v1
last_updated: 2026-08-18
---

# Model Context Protocol

## Definition

Model Context Protocol is a standardized connector layer through which AI agents can discover and use external tools, data, and context. It reduces the need to build a bespoke integration for every model-to-system pairing by giving databases, repositories, communication systems, business applications, memory services, and even narrowly scoped human actions a common agent-callable surface.

MCP is an access protocol, not a complete agent architecture. It can expose capabilities and context, but the surrounding [[AgentHarness]] still decides what to call, how to authenticate, what permissions apply, how results enter context, and how actions are verified or audited.

## Current Synthesis

The corpus consistently presents MCP as infrastructure for moving agents beyond the chat window. Coding is the most mature case because repositories, tests, logs, specifications, and dashboards can be joined into a reviewable workflow. The same pattern is extending toward enterprise databases, service transactions, personal memory, and human-in-the-loop actions.

The protocol’s strategic value comes from interoperability and distribution. Providers can make their capabilities legible to many assistants, while agent products can reach a wider set of systems without owning every integration. This may weaken GUI-based entry points and shift recommendation or transaction power toward assistants, which gives incumbent platforms mixed incentives to open themselves.

Standardization does not make agent behavior reliable by itself. Local agents and enterprise systems still face prompt injection, ambiguous instructions, identity, permission, provenance, data leakage, and non-deterministic execution. MCP can make these boundaries explicit and governable, but it can also widen the blast radius when a powerful connector is attached to an unsafe agent.

MCP should also remain distinct from memory and skills. [[AISkills]] encode procedure; memory systems import, understand, structure, retrieve, and govern knowledge; MCP provides a way for an agent to reach those capabilities. Treating the connector as the whole solution obscures the harder work performed behind the interface.

## Key Claims

1. **Agents need a standardized connectivity layer.** Useful work spans code, documents, meetings, logs, databases, SaaS applications, and real-world actions rather than a single model context.
2. **MCP separates access from procedure.** The protocol exposes capabilities, while skills and agent logic determine how those capabilities are combined into a workflow.
3. **Interoperability changes platform power.** Agent-callable services can gain distribution, but assistants may capture user attention, recommendation authority, and the primary interface.
4. **The connector is not the underlying data or memory system.** MCP can expose structured memory or enterprise records, but it does not create, understand, govern, or maintain them.
5. **Standardization increases the need for governance.** Identity, least privilege, provenance, audit, consent, and verification become more important as agents gain access to consequential systems.
6. **MCP can connect software, data, and people.** A human can be exposed as a narrow callable capability, but only with explicit scope and responsibility boundaries.

## Evidence

- **Enterprise and coding context:** [[all-in-with-chamath-jason-sacks-friedberg-microsoft-ceo-satya-nadella-on-ais-business-revolution-what-happens-to-saas-openai-and-microsoft-live-from-davos-39818140]] describes GitHub Copilot reaching beyond repositories into meetings, specs, logs, and dashboards, alongside identity, permission, and provenance requirements for governed agents.
- **Connector and ecosystem framing:** [[e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf]] uses the USB Type-C metaphor for a unifying layer across databases, GitHub, Slack, ERP, and other systems, and pairs MCP with skills in Anthropic’s agent ecosystem.
- **Service-interface incentives and safety:** [[dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]] shows how platforms such as Meituan could expose ordering to assistants while warning that local agents, logged-in state, injected instructions, and broad permissions make connected autonomy risky.
- **Database and enterprise-data access:** [[guanyu-ai-kaiyuan-shangyehua-yu-quanqiuhua-de-jingyan-jiaoxun-he-fangfalun-duitan-pingcap-cto-dongxu-ljw8va0evobhz4ojzrulqzjvxw5]] treats databases and enterprise context as future agent-facing infrastructure while leaving agent-to-agent interaction and shared memory as unsettled layers.
- **Memory boundary:** [[weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3]] places MCP or APIs at the outer interface of a local-first memory stack whose real work includes import, multimodal understanding, structuring, retrieval, scheduling, and governance.
- **Human-callable capability:** [[ep119-duihua-liu-kefan-yong-try-catch-finally-gei-duli-zuo-chanpin-de-neihao-xie-ge-chuli-liucheng-ludjc3ab-jbwpci6tpaajtffsblx]] describes a custom MCP server through which Claude Code can request narrow actions from a person, extending the protocol beyond ordinary software tools.

## Counterevidence & Qualifications

- The sources describe MCP’s role and strategic implications but do not provide comparative measurements showing that every domain benefits equally from protocol standardization.
- MCP does not guarantee connector quality, stable semantics, safe defaults, deterministic behavior, or correct agent planning.
- Open service interfaces can conflict with platform incentives when assistants reduce app browsing, advertising exposure, or merchant visibility.
- A connector to memory is not memory, and a connector to a database is not a governance model; access can amplify poorly structured or improperly authorized data.
- Human-as-tool experiments are illustrative rather than a general operating model and require stronger consent, interruption, and accountability rules than ordinary API calls.

## What Changed

- The page moved from a general connector metaphor to a layered account separating protocol, skills, memory, harness, and governance.
- Enterprise work-context evidence expanded MCP beyond repositories into meetings, specifications, logs, dashboards, and governed agent identity.
- Service-interface cases added platform incentives and the possibility that assistants capture recommendation and transaction entry.
- Memory sources clarified that MCP exposes a memory layer but does not perform data-to-memory transformation.
- A human-callable server broadened the protocol’s scope while sharpening consent and responsibility constraints.

## Related Concepts

- [[AgentFacingInterfaces]] - defines capabilities so agents can discover and invoke them reliably.
- [[AISkills]] - supplies procedural knowledge for workflows that use MCP-connected capabilities.
- [[AgentHarness]] - governs planning, context assembly, execution, recovery, and verification around protocol calls.
- [[AgentPermissionBoundaries]] - limits what connected agents can read, change, or trigger.
- [[AIDataMemoryInfrastructure]] - provides governed data and memory services that MCP may expose.
- [[DataToMemoryTransformation]] - performs the structuring work that a memory connector alone cannot provide.
- [[AIAssistantServiceEntry]] - captures the distribution shift when assistants call services without their traditional interfaces.
