+++
title = 'E238｜聊聊Harness时代AI-First的组织架构：从信任人到信任AI'
date = 2026-05-25T00:00:00Z
show = '硅谷101'
source_url = 'https://sv101.fireside.fm/251'
duration = '3921'
draft = false
+++

# E238｜聊聊 Harness 时代 AI-First 的组织架构：从信任人到信任 AI

## 概览

本期围绕 Harness Engineering 与 AI-First 组织重构展开。节目从 Prompt Engineering、Context Engineering 到 Harness Engineering 的演进讲起，重点讨论大模型不只是需要更好的提示词和上下文，更需要一整套能让 Agent 在真实工作流里持续运行、自我修复、自我提升的系统。

Creo 的三位创始人分享了他们在公司内部进行 AI-First 转型的经验：不是在原有流程上给每个人配 AI 工具，而是围绕 AI 的能力重建开发、测试、市场、组织协作和决策流程。他们强调，真正的变化是从“人使用 AI 提效”转向“AI 主导生产，人负责架构、判断和审核”。

讨论也涉及组织角色的变化。产品经理、工程师、设计师、市场人员的边界正在被重新划分，传统对齐成本被 AI 系统吸收，人的价值更多转向系统架构、价值定义、需求判断和结果 review。嘉宾总体对未来保持谨慎乐观，但也承认转型中会有组织阻力、信任问题、合规问题和伦理问题。

## 分段落总结

[00:00] **从 Prompt、Context 到 Harness**

[事实] 主持人回顾了过去三年大模型工程能力的三次概念演进：2023 年关注 Prompt Engineering，2024 年关注 Context Engineering，2026 年开始流行 Harness Engineering。

[事实] Harness 被解释为围绕大模型搭建一套能在真实世界持续工作、自我修复、自我提升的系统。

[事实] 节目介绍 Peter 是 Creo 的 CTO，曾在 Meta Llama 基础模型团队和苹果多模态模型相关方向工作，本期还邀请了 Creo 的 CEO 陈凯和负责 Go-to-market 的 co-founder Clark。

[推测] 本期的核心问题不是“AI 能不能写代码”，而是“公司能不能把工作方式改造成 AI 可以可靠承担主生产力的位置”。

[02:32] **Harness Engineering 的定义**

[事实] Peter 认为 Prompt Engineering 和 Context Engineering 主要关注如何与大模型交互，而 Harness 的范围更大，包含 tooling、sandbox 架构、安全、host service 交互、启动时间和 latency 等系统问题。

[事实] 他强调 Prompt 和 Context 更偏静态优化，而 Harness 是对 general system 的动态系统性优化。

[事实] Harness 的目标不是一次性把 Agent 做好，而是让 Agent 在使用中持续吸收反馈、自我改进。

[推测] 在这个定义下，Harness 更接近 AI 应用时代的软件工程、运维、测试、安全和产品反馈系统的总和。

[04:17] **为什么 Agent 表现好坏差距巨大**

[事实] 主持人提到一个 Agent 可以一夜完成三个人的 SEO 工作流，也可能有 content pipeline 跑了两天后才发现全是垃圾。

[事实] Peter 认为这种差异正说明 Harness 的必要性：当系统效果不好时，关键是系统能否通过人的反馈或自我机制进行 self-healing 和 self-improvement。

[事实] 他提到 inference 阶段的 scaling 包括提供更多 context、更多 tooling、更长思考时间和更长任务执行时间。

[事实] 如果 Harness 做不好，长时间推理、多工具调用和大上下文会带来 hallucination、context overflow 和模型能力下降等问题。

[06:18] **静态 Harness 与动态 Harness 的分歧**

[事实] Peter 认为很多人把 Harness 理解为静态地开发一个系统来发挥大模型优势，但 Creo 更强调动态过程。

[事实] 他们希望系统能不断吸收 marketing signal、产品 signal、用户 signal 和 infrastructure signal，并快速迭代。

[事实] 主持人总结，这种迭代是以 AI 为主导的，而人要做的是把各种 signal feed 给 AI。

[推测] 这里的“AI 主导”并不等于人退出，而是人的工作位置从直接执行转向设计反馈回路和提供判断信号。

[08:12] **Creo 内部的 AI-First 开发节奏**

[事实] 主持人提到 Peter 的帖子称 Creo 是 25 人公司，99% 的代码由 AI 写，早上 10 点写功能，中午做 A/B test，下午根据数据砍掉部分功能，5 点重写更好版本，传统流程可能需要 6 周。

[事实] Peter 将 Creo 的 Harness 分成两部分：一是对 Creo 自身 Agent 系统的 Harness，二是用户在 Creo 上构建自己 Agent 时的 Harness。

[事实] Peter 认为当 feature implementation 只需要一两个小时后，传统上花很长时间做 design 和 testing 的流程就需要被重新纳入 Harness。

[事实] 陈凯强调 AI-First 不是在现有流程上使用 AI 工具，而是围绕 AI 的能力重新构建工作流程和组织形态。

[11:02] **转型首先是人的问题**

[事实] Peter 说推进 Harness 和 AI-First 首先要解决人的问题，即团队能否接受新的工作方式和 mindset alignment。

[事实] 过去要用几个月证明新架构更好，现在借助 AI 可以在一两周内重构前端、后端、architecture 和 infrastructure，并用部署频率、可靠性和效果证明新方式。

[事实] 陈凯补充，AI-First 要求 AI drive 公司方向和日常工作方式，而不仅是人用 AI 提升效率。

[推测] 组织转型的难点不只是技术能力，而是团队是否愿意把控制权、判断流程和协作机制交给系统重新分配。

[14:17] **AI 接管团队对齐与发布反馈**

[事实] 陈凯举例说，过去 Go-to-market 团队和 engineering 团队需要大量沟通对齐，现在 AI 可以告知 marketing team 工程团队要发布哪些功能及其结构。

[事实] Peter 说在 AI mindset 下，团队更关注新 feature 是否带来 top-line metrics 提升，是否有真实用户使用数据。

[事实] 他们搭建数据链后，由 Agent 基于数据决定 feature 是否有用、是否 rollout 或 fallback。

[事实] Peter 提到传统 CICD 多是 rule-based 或 unit testing driven，而现在可以加入 AI-driven integration test、unit test、Playwright 等测试方式。

[17:25] **市场节奏被开发速度反超**

[事实] Clark 说实行新开发机制几个月后，Go-to-market 团队不再需要频繁问工程团队做什么 feature、何时 deliver，因为 feature 数量已经远超市场能卖的能力。

[事实] 他形容现在不再讨论 product roadmap，而是讨论市场需求在哪里，再从已有产品能力中挑出适合市场的点去卖。

[事实] 主持人总结，开发能力已经远快于市场能力，所以市场有新风向时，可以从产品库中选择穿透点进行营销。

[推测] 这意味着传统 SaaS 公司常见的“销售超前于产品”关系被反转，组织瓶颈可能从研发交付转移到市场叙事、定位和分发。

[19:17] **AI 驱动的质量控制与 Bug 修复**

[事实] Peter 认为 bug 是工程中不可避免的，无论 AI 写代码还是人写代码都会产生 bug，关键是能否找到并快速修复。

[事实] Creo 开发了 agent-driven CICD 系统和 agent-driven bug triage 系统，用 Agent 识别 issue、分配给工程师并推动修复。

[事实] Peter 说不同 Agent 可以分别负责前端、后端和 Agent 核心系统的 bug，发现 bug 可能只需一到两分钟，分配只需几秒，整个 cycle 可能一到两个小时；过去可能需要一周。

[事实] 他们还有 autofixing 系统，若修复涉及低风险文件夹，AI 会自动提交 PR，工程师简单 proof 后即可 ship；现在 50% 以上 issue 通过 autofixing 形式处理。

[22:53] **Agent Behavior 的风险边界**

[事实] Peter 将 agent behavior 问题拆成 cost 太高、latency 太高、hallucination、tooling 交互和 authentication 问题等。

[事实] 他说任何系统 issue 都可能导致用户使用 Agent 时无法完成 task。

[事实] 他们关注的是在 cost 最低的情况下，reliably 完成用户 task。

[推测] 在 Agent 产品中，质量不只等于代码质量，还包括成本、延迟、权限、工具调用和任务完成率等综合指标。

[24:42] **Architect 与 Operator 的新分工**

[事实] Peter 认为 AI 环境下工程团队可能分为 architecture 和 operator 两类人。

[事实] Architecture 仍然负责决定整体系统，例如 sandbox 和 host 如何交互、安全与 latency 如何优化。

[事实] 他指出 AI coding 通常能给出 solution，但这个 solution 可能有安全隐患或 latency 隐患，因此仍需要 architecture 判断。

[事实] 他提到过去搭建 Agent 系统可能需要 10 到 20 人，现在可能只需要一个 architecture 在一周内完成。

[26:05] **把 AI 当成系统，而不是单个智能**

[事实] 陈凯认为 Harness 的重要价值在于，当 AI 没做好时，不应只想着纠正这个智能，而要思考如何弥补系统。

[事实] 他强调 Harness 是动态改变和提升的过程，不是静态地束缚智能。

[事实] 他用写作举例说，如果发现一个大问题，应该思考系统有没有漏洞，而不是只修一个具体错误。

[推测] 这套观点把“修错”升级成“修反馈机制”，强调问题复发的根因在系统设计而不在单次输出。

[28:53] **Agent 可能成为内容和软件的消费者**

[事实] 陈凯提出，未来内容、图片、视频的受众不一定是人，也可能是 AI 或 Agent。

[事实] 他举例说自己研究 SOC2、ISO 合规服务时，会先让 Agent 帮忙 research，再基于结果判断是否适合公司。

[事实] Peter 说在 task management 产品中，团队更关心 Agent 能否读取和 prioritize task，因此会关注产品是否有更好的 MCP 和 API，而不是只看 dashboard。

[推测] 如果 Agent 成为采购、研究和任务管理的入口，SaaS 产品的接口价值可能从面向人的 UI 转向面向 Agent 的 API、权限和数据结构。

[31:11] **AI-First 转型不是从第一天开始的**

[事实] 陈凯说 Creo 不是第一天就以 AI-First 方式工作，2025 年上半年团队还认为 AI 是辅助人做事，下半年才意识到如果仍由人主导，效率提升有限。

[事实] 他说市场团队和 engineering 团队曾花一两个月反复讨论更好的工作方式，这属于组织进化的一部分。

[事实] Peter 认为这种变化也依赖基础模型能力、Agent 架构和 Agent infrastructure 的提升；一年前让 AI 主导开发在技术上不成立。

[事实] Peter 说他们大约在去年 8、9 月意识到需要重构，真正开始重构代码架构和开发流程是在今年 1 月，用大约两周完成整体架构重构。

[35:04] **AI Planning 能力的跃迁**

[事实] Peter 说过去 AI 在 planning 阶段可能只有 50 分，现在可以给到 90 分，他只需要 criticize 和 challenge plan，而不需要亲自改 plan 或写代码。

[事实] 他表示 2026 年自己没有写过一行代码。

[事实] 他认为 AI 写代码能力肯定在自己之上，但 planning 仍有缺陷，例如 security 和 latency 问题，需要 architecture 通过经验指出。

[事实] 当他把安全性、sandbox 与 host 的准则沉淀成 skill 后，团队其他工程师也可以 reference 这些 skill 来要求 AI follow 原则。

[37:29] **效率提升的量级**

[事实] Peter 估计，如果回到一年前非 AI 主导状态，要开发 Creo 现在的产品，至少需要约 100 人团队花四五个月。

[事实] 现在 Creo 是 25 人公司，工程团队 10 人以下，第一个阶段的产品 deployment 大约花了两周。

[事实] 陈凯说传统软件时代销售和市场概念通常领先产品四五个月，现在则反过来，技术团队超前 marketing 团队三四个月或四五个月。

[推测] 这些数字来自嘉宾自述，反映的是 Creo 内部体验和估算，不一定能直接外推到所有公司。

[39:30] **Go-to-market 的 Agent 化更难评价**

[事实] Clark 说 Creo 的 Go-to-market 也用自家产品构建 AI-first workflow。

[事实] 他认为工程是相对封闭、容易 evaluation 的环境，而 Go-to-market 面向人和 Agent，价值判断更主观。

[事实] 他们没有 100% 让 Agent 做决策，而是生成很多 Agent 结果后，由人判断哪些结果好、市场是否 ready。

[事实] Clark 提到他们有很多 feature，但如果认为市场还没有 ready，就不会放到市场上。

[40:38] **权限开放与数据访问的超前性**

[事实] Clark 说一个相对大胆的方向是让每个人的 Agent 都有所有权限可以读写，让更多组织数据开放给 Agent。

[事实] 他也指出这需要更好的技术支持，包括限制个人和 Agent 权限，避免 Agent 读错数据或乱搞导致错误决策。

[事实] 他举例说，以前要问某类用户行为数据需要找数据同学或工程师打表，现在可以直接问 Agent，几秒后得到答复。

[推测] 这个方向的核心矛盾是效率和风险并存：权限越开放，Agent 越有用，但安全、合规和错误传播的风险也越高。

[42:06] **Creo 的产品定位：让用户创建自己的 Agent**

[事实] Peter 认为上一代 general agent 是所有用户使用同一个 Agent，而 Creo 要让用户在系统上搭建属于自己的 Agent。

[事实] 这些 Agent 要具备 self-improvement 和 self-healing 能力，并理解用户 workflow。

[事实] 他用 campaign agent 举例：用户每周做广告 campaign，不是每次都让 general agent 临时做，而是在 Creo 上创建自己的 campaign agent，由系统持续提升 performance、降低 cost。

[事实] 陈凯说 Creo 的目标人群主要是 SMB 和 30 人以内的中小团队，这类团队更容易采用 AI，也更像 Creo 自身。

[43:48] **哪些公司更容易 AI-First 转型**

[事实] 陈凯认为科技公司和传统公司都可以转型，难点不一定取决于人数和规模。

[事实] 大企业更难，是因为合规、人和 legacy 数据库等因素更多。

[事实] 他认为没有太多合规负担、传统数据库和 legacy 系统的公司，是第一批最容易转型的公司。

[事实] 他还指出，很多 SaaS 公司在 2023 年只想把 AI 做成产品功能，但真正的转型可能要求整体产品重构。

[45:42] **领域专家与 Harness 平台的关系**

[事实] 主持人提出，Harness 似乎要求对某个领域非常了解，才能做精确的系统限定。

[事实] Peter 回应说，普通用户不需要理解底层架构，因为 Creo 提供 cloud service 和基础架构；用户需要深入理解自己要完成的任务。

[事实] Creo 负责接入 tooling、maintain Agent 长时间工作和保证安全性。

[事实] 陈凯补充，许多基础工作如市场调研并不一定涉及极深垂直专业知识，但系统 build 好坏会决定人需要介入多少。

[47:50] **组织结构从信任人转向信任 AI**

[事实] 陈凯说组织改造的第一步是信任变化：过去组织信任的是人，现在要先解决能否信任 AI 做决策和执行任务。

[事实] 为了让人信任 AI，需要很多 guardrails 和机制保障 AI 的 planning、execution 和结果可信。

[事实] 在 Creo，产品经理角色不是不存在，而是被拆解到每个工程师和工程管理者身上。

[事实] 陈凯认为产品经理常常是矛盾集中的角色，因为要连接市场和研发；当这个角色被拿掉，并有机制保证团队互信时，对齐成本反而可能降低。

[49:37] **产品经理、工程师和设计师的角色融合**

[事实] 陈凯认为未来仍需要产品经理，但会是新形态的产品经理，甚至可能由团队整体承担产品经理角色。

[事实] 主持人总结，工程师可能承担产品经理角色，而产品经理也可能借助 AI 更快把想法变成产品，两类角色在融合。

[事实] Peter 认为 general 的人会在 AI 环境中更有优势，例如有产品和 marketing sense 的工程师，或有 implementation 能力的产品经理。

[事实] Peter 还特别提到，未来 UX designer 和 UI designer 可能非常重要，但重要的是具有把想法 implement 到产品中的能力。

[53:24] **Junior 与 Senior 工程师在 AI 时代的适应差异**

[事实] Peter 说 junior engineer 通常更容易接受扩大工作 scope，包括参与产品设计、分析 feature deployment 后的数据，并基于分析做判断。

[事实] Senior engineer 因为更 specialized，可能更难接受从写代码扩展到代码前的判断和代码后的 impact 分析。

[事实] 他也强调 senior engineer 的 value 现在不能被取代，难的是找到既资深、又能 embrace AI mindset、又有产品 sense 和 marketing knowledge 的人。

[事实] Peter 说这样的人很难找，但对公司非常 valuable；现在可能只需要 1 到 2 个，而非没有 AI 时需要 10 倍或 50 倍以上的人。

[57:24] **拥抱 AI 工具不等于 AI-First**

[事实] 陈凯区分了两种心态：一种是愿意用 AI 工具提升个人效率，另一种是愿意构建系统，让未来工作完全由 AI 驱动，并接受自己角色变化。

[事实] 他认为后者在当前仍是少数，更激进，也更接近真正的 AI-First。

[事实] Peter 补充说，很多有架构能力且愿意拥抱 AI 的人会自己创业，因此 startup 想 hire 这种人仍然很难。

[推测] AI-First 人才的稀缺不在于会不会用工具，而在于是否愿意把自己的工作方法、组织权力和身份边界一起重构。

[58:36] **Peter 对 AI 的长期信念**

[事实] Peter 说自己从刚毕业开始就在做 AI，第一份在苹果的工作就是 AI 相关，也与语言模型有关。

[事实] 他提到 Attention Is All You Need、BERT 和 pre-training 对他的影响，并说当时就意识到 pre-training 的重要性。

[事实] 他澄清自己不是说 AI 一直比人强，也不是说 AI 现在能取代人做任何事情。

[事实] 他认为 AI 已经能主导很多事情，但让 AI 系统运转起来仍需要人进行架构。

[60:38] **未来人的核心价值**

[事实] Peter 认为未来人最需要的能力是系统架构能力，从 implement feature 转向架构和 maintain AI 系统。

[事实] 他认为这不只适用于工程，也适用于 Go-to-market，例如如何搭建能自主运行的 Agent marketing system。

[事实] 陈凯认为人的价值在于定义需求方向和技术迭代方向，并 review 最终结果是否符合人的利益和要求。

[事实] Clark 认为人的价值是判断任何事情是否还有价值，价值定义本身延伸出对需求的定义。

[62:00] **伦理问题与谨慎乐观**

[事实] 陈凯提到，Agent 与 Agent、Agent 与人之间的沟通会带来隐私和道德问题，例如另一个人能不能看这些沟通内容。

[事实] Clark 表示自己对未来相对乐观，认为 AI 可能让工作更高强度，但也让工作和生活切割得更好。

[事实] 陈凯认为创业者总体必须乐观，并用工业革命类比，认为人会找到新的方向实现更大自我价值。

[事实] Peter 表示自己是谨慎乐观，认为变革过程会有痛苦和 noise，但结果可能让人有更多自由时间，或在 AI 辅助下发挥更大价值。

## 播客点评/总结

这期的价值在于它不是泛泛讨论“AI 会不会替代人”，而是从一家 AI 公司内部真实组织实验出发，具体拆解了开发、测试、市场、权限、人才和组织信任如何被 AI 重构。嘉宾提供了很多可操作的观察，例如 agent-driven CICD、autofixing、skill 沉淀、产品经理角色拆解，以及 engineering 超前于 marketing 的新瓶颈。

亮点是讨论足够一线，也足够激进。尤其是“不要把 AI 当成单个智能，而要当成动态系统”“拥抱 AI 工具不等于 AI-First”“人的价值转向架构、需求定义和结果审核”这些观点，能帮助听众跳出现有工具使用层面的理解。

局限也很明显：许多效率数字来自 Creo 自身经验和嘉宾估算，能否复制到其他行业、其他规模组织、强合规企业或非技术团队，仍需要更多案例验证。[推测] 对大多数公司来说，短期内最难复制的可能不是工具，而是让团队接受 AI 主导流程、权限开放和角色重分配。

[推测] 这期适合创业者、产品负责人、工程管理者、AI 产品从业者和正在思考组织转型的人听。普通听众也能从中理解 AI-First 不是“每个人都用 AI”，而是公司如何重新决定谁来执行、谁来判断、谁来负责，以及什么才值得被信任。
