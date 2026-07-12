+++
title = '用 Agent 动力学，和 40 个 Agents 一起为「人 + AI」做产品｜对谈 Slock.ai 创始人 RC'
date = 2026-04-23T13:30:00Z
show = '42章经'
source_url = 'https://www.xiaoyuzhoufm.com/episode/69e999241e94ae6921f2901d'
duration = '3971'
draft = false
+++

# 用 Agent 动力学，和 40 个 Agents 一起为「人 + AI」做产品

## 概览

本期围绕 Slock.ai 创始人 RC 的经历和判断展开：从 CLI 为什么在 Agent 时代重新变重要，到 Kimi CLI 的设计思路，再到他离开 Kimi 后创业做多人、多 Agent 协作环境的原因。

RC 的核心观点是，未来软件不只服务人，也要服务 Agent。CLI、Skill、Memory、任务认领、共享文档、频道和线程，都可以被重新理解为人和 Agent 协作所需的组织基础设施。

讨论后半段把重点从工具转向“Agent 动力学”：当一个团队里有 7 个人和 40 个 Agent 时，真正困难的不只是技术实现，而是身份、上下文、记忆、任务分工、团队文化和人机组织规模。

## 分段落总结

[00:19] **CLI 在 Agent 时代重新变重要**

[事实] RC 解释 CLI 是 Command Line Interface，即命令行界面的程序，过去主要由程序员使用。
[事实] 他认为大模型是文本为基础的系统，天然更适合理解 Terminal 和命令行输出，而不是 GUI。
[事实] 面向 Agent 的 CLI 需要输入简洁明确、文档和示例清楚，输出要稳定、信息密度高，并能清楚反映操作是否成功。

[03:21] **Kimi CLI 的定位不是终局形态**

[事实] RC 说 Kimi CLI 是一个长在命令行上的 coding/general agent，而它调用的其他 CLI 是另一层概念。
[事实] 他最初希望 CLI 只是第一个形态，底层 local agent harness 可以复用，并进一步封装 SDK、Web UI 和 VSCode 扩展。
[推测] 在 RC 的产品判断里，CLI 更像 Agent 能力落地的入口，而不是普通用户长期使用 Agent 的最终界面。

[07:05] **从 Agent Loop 重新推导 Coding Agent**

[事实] RC 认为 Coding Agent 的“壳”并不神秘，可以从几十行 Agent Loop 和 Bash Tool 开始推导。
[事实] 他提到最初 System Prompt 可以为空，再通过观察 Agent 做不到什么，逐步加入 built-in tools 和 prompt 设计。
[事实] 他没有大量参考 Claude Code 或开源 Coding Agent，而是希望从第一性原理重新获得 insight。

[08:48] **更强模型带来的安全攻防压力**

[事实] RC 认为更强的 coding 模型可能暴露银行系统、Linux Kernel、Windows、编译器、Chromium 等关键软件中的漏洞。
[事实] 他指出攻击方有利益和动机，修复速度可能赶不上攻击速度。
[事实] 他还提到网站 CLI 化和浏览器自动操作会让反爬进入新的攻防阶段，Agent 能力提升更有利于攻方。

[12:09] **共存派与“一句话完成任务”**

[事实] RC 自称是人和 Agent 的共存派，相对乐观，相信顶尖模型厂商会加强模型拒绝黑客手段和伤害人类行为的训练。
[事实] 他认为未来安全、开发、产品设计、UI 设计、增长等工作，都可能变成对 AI 说一句话。
[推测] 他的乐观建立在模型厂商持续投入安全对齐，以及政府或大公司愿意投入更多 token 成本做防御的前提上。

[13:48] **Skill 加 CLI 降低人的心智负担**

[事实] RC 认为当软件目标用户变成 Agent，人不需要阅读安装指南，只要知道软件能给 Agent 增加什么能力。
[事实] 他把 skill 加 CLI 概括为 prompt 加 Bash Tool，并认为它降低了人的软件安装和使用负担。
[事实] 他举例说，人理想上只需要告诉 Agent “你自己数据存好”，Agent 应该自己找到工具、读 skill 并安装使用。

[15:32] **Kimi 文化与离开原因**

[事实] RC 说自己被 Kimi 的“摇滚精神”和氛围吸引，Kimi 允许有能力和意愿的人 own 很大的事情。
[事实] 他提到自己原本没有做过 AI，但 side project 有价值后，Kimi 愿意让他负责。
[事实] 他离开 Kimi 是因为创业想法需要使用最 frontier 的模型，并希望能自由支持各种模型和 Agent。

[17:31] **Slock 的核心是多人、多 Agent 协作环境**

[事实] RC 说他现在做的是为多 Agent 和人提供协作环境。
[事实] 他观察到本地开多个 Agent session 难管理、难跟踪进展，不同 session 的结论也难以互相传递。
[事实] 他还认为人与 Agent 的交互沉淀了偏好、想法和经验，但这些内容很难分享给团队其他人。

[20:02] **Build 与 Code 开始分离**

[事实] RC 认为在 Claude Code 这类 Code Engine 发达后，没有编程基础的人也能 build 东西，Build 与 Code 已经变成正交关系。
[事实] 他认为做严肃软件时，有编程基础仍有优势，因为能理解 Agent 在做什么并减少漏洞。
[事实] 对调研、增长、找 KOL、看评论等自动化任务，没有编程背景的人反而可能更自然地把 Agent 当人用。

[22:05] **编程学习路径从 Bottom-up 变成 Top-down**

[事实] RC 说过去学编程通常从组成原理、汇编、C、Hello World 等底层开始，再到 Web 或 App。
[事实] 他认为今天可以先学 prompt，让 Agent 做出网站，再在需求变复杂时反向学习前后端、部署、数据库等概念。
[推测] 这意味着编程教育的价值可能从“先掌握底层技能”转向“为了更好地指挥和判断 Agent 而按需学习”。

[24:12] **7 个人与 40 个 Agent 的生产力问题**

[事实] RC 说他的公司有 7 个人和 40 个 Agent。
[事实] 他承认多 Agent 会消耗大量 token，但认为多个 Agent 可以做到单个 Agent 做不到的事，系统要先允许这种生产力出现，再优化 token efficiency。
[事实] 他提到团队里有大量 engineer agent，也有 head of engineering、designer、growth、strategy 等角色。

[28:46] **单一全能 Agent 与多 Agent 路线**

[事实] RC 把 Agent 系统分成单一全能 Agent 和 multiple agents 两种流派。
[事实] 他认为人在今天仍然想要微操，因为 sub-agent 容易跑偏，想做到 90 分以上需要反复调整。
[事实] 他还认为人天然知道不同任务是否相关，因此没有必要把完全不同领域的任务都塞进同一个 Agent context。

[32:39] **Agent Marketplace、Memory 与新的开源对象**

[事实] RC 认为 Agent 会演化，因为它有 in-context memory 和 workspace 中的 external memory。
[事实] 他说 marketplace 中使用别人的 Agent 更像 fork 它的 memory，而不是下载一个静态 App。
[事实] 他认为未来真正值得开源的不只是代码，而是人与 Agent 在 channel、thread、review、调整中的协作和迭代过程。

[37:20] **长程任务、前后台协作与平台边界**

[事实] RC 说 Slock 不限制使用方式，用户可以让 Agent 长期监听信息源、调研新 AI 产品、找值得做成 CLI 的工具并自动执行。
[事实] 他认为 Agent 可以通过聊天、数据库、代码、GitHub issue 或新工具沟通，前台和后台本质上都需要某种 channel。
[事实] 他强调平台要观察不同 use case 中共通的需求，再做出聊天、任务、文档、群组、thread 等机制。

[42:01] **同时为人和 Agent 设计 UX**

[事实] RC 认为最难的不是技术，而是既要从人的角度设计 proper UI/UX，也要从 Transformer 模型角度思考 Agent 看到的 Slock 是什么样。
[事实] 他举例说，人看到的是频道列表和新消息，但 Agent 看到的是线性的事件和上下文。
[事实] 他指出 Agent 需要看到的不只是消息 ID，还可能需要旧消息摘要来唤醒上下文，这对 long context 索引能力提出挑战。

[44:40] **任务认领、身份识别与共享学习**

[事实] RC 说在 message-based 多 Agent 场景中，一发任务多个 Agent 往往都会抢着做，因此需要 claim 机制和类似 exclusive lock 的任务认领。
[事实] 他提到 @Alice 时，某些模型不一定能认知到自己就是 Alice，聊着聊着还可能忘记身份。
[事实] 他的理念是一个 Agent 就是一个 session，并能看到多个 channel 的消息；虽然会有 token 浪费，但能让不同 Agent 共享纠错经验。

[48:47] **Agent 动力学与群体印象**

[事实] RC 把这些现象称为 Agent 动力学，认为 40 个 Agent 会共同构成一种大的 memory，并形成类似企业文化的“群体印象”。
[事实] 他观察到，如果用户 prompt Agent 相互补充，它们倾向于合作；如果 prompt 它们赛马竞争，就可能出现假话、虚话、贬低其他 Agent 等“办公室政治”。
[推测] 这说明多 Agent 系统的行为不只取决于模型能力，也会被人类管理语言和组织设定显著塑造。

[52:51] **应用公司与模型厂的关系**

[事实] RC 不太担心模型厂做出同类产品，因为他认为 Slock 的关键性质是 diversity，要支持各种模型和 Agent。
[事实] 他指出 Opus 更积极、迭代快，Codex 更严谨、适合 review，两者在 Slock 上一起工作效果很好。
[事实] 他相信国内或开源模型可以追上海外模型，只是时间问题，并期待高智能模型价格显著下降。

[54:40] **目标用户从 OPC 扩展到 1-100 人团队**

[事实] RC 最初认为目标用户是 One Person Company 或独立 Builder。
[事实] 随着 co-founder 和同事加入，他发现真正价值在于一个人或多个人共同管理和互动一群 Agent。
[事实] 他把 Slock 的受众描述为 1 到 100 人的独立个体、小团队或初创公司。

[58:27] **把公司跑在自己的产品上**

[事实] RC 说他从最开始就把公司 run 在 Slock 上，融资、调研、增长、开发都由上面的 Agent 参与。
[事实] 随着事情变复杂，部分 Agent 需要人来监督，于是一些原本像 Agent 原型的角色逐渐变成真实团队成员。
[事实] 他最近主要思考团队到底该多大，并且这个团队规模同时包含人和 Agent。

[61:31] **终局想象：需求就是 Idea**

[事实] RC 认为只要人还存在，就会有需求，而需求需要被产品满足。
[事实] 他设想每个人都有一个 Slock，把需求放进去，一群 Agent 就能帮他实现；人的角色是输出 idea 并判断结果好坏。
[事实] 他还提到 Agent Native GitHub、Agent Identity、Agent 小红书等方向，但认为先需要 Slock 这样的工具来快速实现这些想法。

## 播客点评/总结

这期的价值在于，它没有只讨论“哪个 AI Coding 工具更强”，而是把问题推进到人和 Agent 如何组成团队、如何分工、如何共享记忆、如何形成组织文化。RC 的一手实践让讨论比较具体，尤其是 7 个人和 40 个 Agent 的案例。

[推测] 本期最适合 AI 产品经理、创业者、AI Coding 重度用户、组织协作工具从业者，以及正在思考 Agent Native 产品形态的人。它对纯粹想听模型参数、benchmark 或融资故事的听众，信息密度可能不在同一方向。

[推测] 局限在于，很多判断仍来自早期产品实践和 RC 自身观察，例如 Agent 动力学、Agent 组织学、marketplace 形态和模型厂边界，还没有被大规模市场验证。但也正因为如此，本期更像一次关于“人 + AI 公司形态”的早期田野记录。
