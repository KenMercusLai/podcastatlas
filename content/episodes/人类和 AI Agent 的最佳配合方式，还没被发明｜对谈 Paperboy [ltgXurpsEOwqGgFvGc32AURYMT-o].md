+++
title = '人类和 AI Agent 的最佳配合方式，还没被发明｜对谈 Paperboy'
date = 2026-05-20T16:00:00Z
show = '十字路口Crossing'
source_url = 'https://www.xiaoyuzhoufm.com/episode/6a0be0cfe1eb34a939abced5'
duration = '3332'
draft = false
+++

# 人类和 AI Agent 的最佳配合方式，还没被发明｜对谈 Paperboy

## 概览

本期对谈请到 Paperboy 创始人匠杨和 founding engineer 杰德辰，围绕一个核心判断展开：人类和 AI Agent 协作的最佳方式还没有被发明出来。Paperboy 试图解决当前 Agent 产品过于依赖聊天框、session、手动 prompt 和短期上下文的问题。

讨论的主线从产品理念进入技术与交互：Paperboy 认为 Agent 应该从用户的 OS 活动、屏幕、输入、会议、消息和搜索等环境中学习，形成更持久、更个性化的记忆，而不是只依赖用户与 Agent 的聊天历史。它的产品形态也从“AI Slack”转向更接近 IM/inbox 的界面，把 Agent 带到用户已有的工作场景中。

后半段转向创业、团队和竞争判断。两位嘉宾讨论了 OpenAI、Anthropic、Cursor、Codex、Claude Code、Slack 等产品与公司的优势，也谈到 Paperboy 如何在巨头竞争中依靠产品品味、界面探索和企业场景寻找机会。最后还延伸到市场选择、管理学习、大学价值、招聘、模型公司与产品公司的关系，以及 robotics 和 AI security 的机会。

## 分段落总结

[00:00] **嘉宾背景与开场快问快答**

[事实] 本期嘉宾是 Paperboy 创始人匠杨，以及 founding engineer 杰德辰。

[事实] 两位嘉宾分别提到自己 21 岁和 19 岁，教育背景包括上海的双语学校，以及 CMU 大一刚结束。

[事实] 匠杨说 Paperboy 是自己的第二家公司，之前做过 Millian，在 React ecosystem 里做开源 DevTools，也做过 Same.Dev，用一句话和 URL 生成类似网页 UI。

[事实] 杰德辰在 Paperboy 之前是高中生，喜欢开源和 CTF，做过 EarthKit，用多模态推测照片拍摄地点。

[01:36] **Paperboy 要解决什么问题**

[事实] 匠杨说 Paperboy 源于他对现有 AI 协作产品的不满：不应该把文件、邮件和个人信息都丢进聊天框里。

[事实] 他认为如果人和人需要一起与 Agent 协作，产品应该让他们在同一层面上共同工作，而不是只是一对一聊天。

[事实] 他批评现有产品大多是 session-based，一旦 session 结束，就很难从过去的 context window 继续下去。

[事实] 他希望 Agent 在知道用户很多信息后，可以 proactive 地提前帮用户做一些事情。

[03:13] **融资、发布计划与团队规模**

[事实] 转录稿中提到 Paperboy 已融资 4.7 万美元；该数字按转录稿记录呈现。

[事实] 嘉宾说当前收入为零、利润为负，并表示“每天都在亏钱”。

[事实] 团队曾把一个从 OS activities 学习的 Agent prototype 给朋友使用，但因为成本太高，不太可行。

[事实] Paperboy 当时有 12 位全职员工，其中 10 位是 engineer。

[04:07] **“最佳配合方式还没被发明”是一个移动目标**

[事实] 主持人提到匠杨曾在内部文档中写下：“人类和 AI 配合工作的最佳方式，很可能还没有被发明出来。”

[事实] 匠杨说这个目标是一个 moving target，因为每次出现新产品，市场和用户都会看到新的可能性，也会发现新的痛点。

[事实] 主持人提到从 Claude Code、OpenAI 相关产品到其他 Agent 产品，过去半年变化剧烈；匠杨回应说 Paperboy 的方向没有发生剧烈变化。

[推测] Paperboy 的核心 thesis 不是追逐某个单点功能，而是持续寻找新的 Agent 协作形态。

[06:21] **Agent 产品的三个关键维度**

[事实] 匠杨把问题拆成几个角度：从用户环境中学习、把用户环境和电脑中的资料转化为可用上下文，以及个性化。

[事实] 他认为个性化意味着用户不需要太多 prompt，也能更信任 Agent 处理复杂困难的事情和更高级的决策。

[事实] 他强调产品设计上需要一种新的工具形态，能把上下文、个性化和电脑协作结合起来。

[推测] 这里的关键不是“模型是否更聪明”，而是 Agent 是否能稳定进入用户真实工作流并积累长期理解。

[07:41] **为什么还需要 Paperboy**

[事实] 匠杨认为 Claude Code 和 Manus 是目前很成功的 Agent，但它们的交互仍然偏项目、session 和一对一消息。

[事实] 他指出现有 Agent 往往是 reactive 的，用户必须非常具体地写 prompt 或维护类似 Agent.md 的文件。

[事实] 他认为用户的 taste、judgment 和最佳实践很难通过文档完整传递给 Agent。

[事实] 许多聊天历史中包含有价值信息，但如果没有被显式保存，就会被丢弃。

[09:42] **Paperboy 的上下文来源：OS 层面的用户数据**

[事实] Paperboy 希望 Agent 自己学习用户如何使用电脑，包括屏幕、键盘、鼠标动作、会议、视频、声音、搜索历史和消息等用户选择提供的信息。

[事实] 杰德辰补充说，Paperboy 与只读 chat history、email 或 messages 的产品不同，它更早押注通过 OS 层面的 context 做 user adaptation。

[事实] 他认为一般的 computer use 信息浓度很高，观察用户使用电脑 60 分钟，比只观察 60 分钟微信聊天能学到更多东西。

[推测] 这种路径也意味着 Paperboy 的产品价值高度依赖用户授权、隐私边界和数据处理能力。

[12:39] **桌面上下文成为行业共识，但用法仍未定型**

[事实] 主持人提到其他桌面客户端或 Chronicle 类产品也在 capture 用户屏幕数据和电脑使用习惯。

[事实] 匠杨回应说，从 Mac 或用户电脑中把机器数据转入记忆是一件会发生的重要事情，不只独立开发者会做，大公司也会做。

[事实] 他强调不同应用会以不同方式处理和压缩流式数据，选择如何设计这些数据直接取决于客户应用场景。

[事实] 杰德辰说，在屏幕数据和 computer use 的基础上，还可以探索很多问题，比如 proactive agents 应该预测下一个 keystroke、未来一小时的行为，还是其他东西。

[15:35] **第一小时的产品价值：meeting prep 和期望建立**

[事实] 匠杨说 Paperboy 可能会从 meeting prep 开始，让用户在短时间内看到产品能做什么。

[事实] 他强调 Paperboy 会随着使用时间变长而变好，因此早期需要让用户相信它会学习。

[事实] 用户打开 Paperboy 后，会看到一个简洁的聊天窗口；在授权日历、邮件等账号后，Paperboy 会开始读取相关信息。

[事实] 它可能会提示用户“我看到这个 meeting 要来了，你想让我看看吗”，以较合理的方式主动通知用户。

[17:08] **团队内部使用：MiniVivian 和 AlderJohn**

[事实] 匠杨提到团队内部有 Vivian 的 Paperboy，叫 MiniVivian；自己的 Paperboy 叫 AlderJohn，它们存在于 Slack 中。

[事实] MiniVivian 被描述为 Vivian 的 recruiting intern，因为它理解会议、Slack 和匠杨关于候选人的判断与品味。

[事实] MiniVivian 可以帮助 Vivian 从 GitHub、Twitter 等地方发现候选人，节省时间。

[事实] 匠杨说 Vivian 从 2 月以来没有使用 Claude，因为 Claude 不知道足够多的上下文，难以替她研究候选人。

[18:43] **反 prompt：高带宽关系比提示词更自然**

[事实] 匠杨明确说自己讨厌 prompting，认为人并不是用 prompt 思考，而是发文本，并期待对方知道自己在说什么。

[事实] 他认为好的关系是高带宽沟通，并且聪明人也会喜欢别人告诉自己不知道的东西，尤其是“不知道自己不知道”的东西。

[事实] 他期待未来 Agent 能作为比自己更聪明的存在，帮助自己思考。

[推测] Paperboy 的理想交互更接近“长期共事的人”而不是“每次都要重新说明背景的工具”。

[19:46] **权限、责任与 Agent 在组织中的角色**

[事实] 匠杨说用户最终必须对自己的 Agent 负责，Agent 并不是突然出现的存在，而需要 onboarding 过程。

[事实] Agent 会询问可以向某个具体的人分享多少信息，并默认模仿用户与不同人的分享程度。

[事实] 杰德辰说，AlderJohn 拥有公司上下文，也在观察匠杨工作时学习到更接近匠杨的 heuristic，因此对工程师做决策有帮助。

[推测] 这里的 Agent 角色不只是执行任务，也像是组织中带有上下文和判断风格的代理人。

[21:13] **Memory 系统与 OS 级 autocomplete**

[事实] 杰德辰介绍说，他们先把操作系统层面收集到的用户数据放进更好的 memory system。

[事实] 这个系统会有一个持续更新的 Markdown 文档，记录用户职业、过去几天做过什么、过去几秒和几分钟正在做什么；越接近当前，粒度越细。

[事实] Paperboy 找到的第一个应用场景是 OS 中任意位置的 auto-complete，例如微信、命令行、GitHub PR 等。

[事实] 用户可以输入类似触发词和简短指令，也可以不给明确指令，让 Agent 根据当前上下文猜测用户想补全什么。

[23:36] **跨上下文理解让 commit 和 PR 更好写**

[事实] 杰德辰说，在命令行里可以让 Paperboy 自动写 commit message，也可以在 GitHub 里生成 PR description。

[事实] 他认为 Paperboy 生成的 PR 描述在很多时候比 Cursor 或传统 Claude Code 更好，因为它能整合代码、WeChat、浏览器研究等多个上下文。

[事实] 他把这种体验类比为同事只要看一眼或指一下屏幕，就知道你想让他看哪里。

[推测] Paperboy 的优势来自“场景连续性”，而不是某个单一任务上的模型能力。

[24:24] **效率监督、研究辅助与连接思路**

[事实] 杰德辰说自己工作时容易分心，例如等 Claude Code 时会看 Hacker News，结果回来发现任务早已结束。

[事实] 他让 Paperboy 每晚给自己报告当天效率，并在自己不够高效或分心时“骂他”。

[事实] 匠杨说自己的工作现在更多是使用产品、做研究和与人交流，Paperboy 能把这些不同信息来源保存在脑中。

[事实] 他举例说，当自己研究卫星、网络效应业务的历史、成功和失败后，Paperboy 可以帮他把这些点连接到 Paperboy 的产品思考上。

[26:20] **最新界面灵感：从模块化 sidebar 转向 IM**

[事实] 匠杨说他们两周前开始做最新 interface，并讨论了给 VC 等 ICP 提供 personal CRM、meeting、deals、portfolio、LP relationship 等模块的问题。

[事实] 他认为不同 ICP 如 VC、operator、founder、real estate salesman 都需要不同 sidebar，而把这些做成 skills、plugins 或 recipes 并不太说得通。

[事实] Paperboy 指出 IM 是一种“无限列表但不烦人”的应用形态，微信中联系人、群聊和主题群能自然组织生活中的事项。

[事实] 因此他们把最新界面转向 IM/inbox，而不是单独设计一个 inbox feature。

[29:36] **竞争：真正重要的是 OpenAI 和 Anthropic**

[事实] 匠杨说今天真正重要的竞争对手只有 OpenAI 和 Anthropic，其他人都在它们后面。

[事实] 他认为这两家公司拥有模型和分发优势，Paperboy 只能希望像 Cursor 一样在 taste 和新 interface 上取得边缘优势。

[事实] Paperboy 也希望进入 enterprise，因为钱在那里。

[推测] Paperboy 对竞争的判断较务实：承认基础模型和分发不在自己手里，因此把差异化放在产品体验和组织形态上。

[30:07] **为什么 Paperboy 没有继续做 AI Slack**

[事实] 匠杨说 Paperboy 一开始想做的第一个产品是 AI Slack，用来回答“如果最佳 Agent 协作方式还没被发明，该做什么”。

[事实] 他认为 AI Slack 的难点在于如何让企业切换，因为团队才是付费方，迁移 Slack 数据和构建 connectors 都很重。

[事实] 他还说 Slack 本身不是一个令人愉快的产品，但在规模上没有更好的替代品。

[事实] 杰德辰补充说，Slack 的 external connections、integrations 和网络效应让它很难被替代，所以更好的 adoption story 是在 OS 层面或 Slack 之上做互补层。

[33:21] **把 Agent 带到用户已经工作的地方**

[事实] 匠杨说，如果要进企业，Paperboy 会跟 Slack 沟通，而不是试图在 50 人以上团队里快速替代 Slack。

[事实] 他强调要把 agents 带到人们已经在做事的地方，而不是改变和重建一切。

[推测] 这解释了 Paperboy 从“新协作平台”转向“现有工作流上层 Agent”的战略调整。

[33:29] **The Last Interface 与五种速度**

[事实] 主持人提到 Paperboy 官网 blog post《The last interface》里讲到 5 kinds of speed。

[事实] 匠杨说“五”并不是因为只有五层，而是一个有意义的分类；他提到 Long Now Foundation 相关的 pace layers 思想，不同层以不同速度变化。

[事实] 他把这种速度层思想用于理解产品和 Agent：真实世界、社会与产品中的任务也有不同时间尺度。

[推测] Paperboy 试图用“速度”来设计 memory 和 interaction，而不是把所有任务都塞进同一种聊天框。

[35:04] **不同时间尺度需要不同 Agent 形态**

[事实] 杰德辰说，用户任务可以按时间长度分类：微信回复可能只需一秒或十秒，而读十份长报告并做商业决策可能需要几个小时。

[事实] 他认为 spectrum 的每一端都会需要某种 AI agent 自动化，但不同端需要做的事情不一样。

[事实] 对微信回复这种短任务，比较好的 form factor 可能是在回复界面自动弹出 autocomplete，Paperboy 已经在做。

[事实] 随着 time horizon 变长，产品形态会越来越不确定，自动化几个小时的任务仍然是值得探索的区域。

[36:33] **匠杨的创业成熟度与市场选择**

[事实] 主持人提到团队成员觉得匠杨有超越年龄的成熟感，匠杨回应说自己仍然很年轻，但团队在短时间内做困难的事情，需要信念、精神和专注。

[事实] 匠杨说 CEO 的第一份工作是把团队的成绩和目标解释清楚，确保每个人的目标和实际行动一致。

[事实] 他提到自己高中时就对探索和理解世界有强驱动力，也在不同公司实习和做问题解决。

[事实] 他从 Millian 的 B2B enterprise 经验中学到，20 岁团队很难 scale enterprise relationships。

[38:43] **市场选择、CEO 杠杆与管理学习**

[事实] 匠杨认为 market picking 是早期 founder 最重要的能力之一，要理解市场、杠杆点和挑战。

[事实] 他认为市场要足够大且可持续，不只是美元规模，还要能让团队和产品在十年维度持续发展。

[事实] 他说 CEO 是公司里最可能浪费最多钱的人，因为 CEO 的想法有很高杠杆，错误方向会带来巨大成本。

[事实] 他通过向 Manus 的 CTO Panpan 提问、阅读《High Output Management》《The Hard Thing About Hard Things》《Trillion Dollar Coach》，以及每周见 CEO coach 学习管理。

[43:14] **AI 时代的团队构成**

[事实] 匠杨说，如果要做严肃的 infrastructure buildout，需要真正理解 infra 的人。

[事实] Paperboy 工程侧招聘两类人：一类像 Jett 一样年轻、高 IQ、有创造力、看到问题就 prototype；另一类是在系统、OS 等领域非常扎实的专家。

[事实] 他举例说团队从 AWS 招了一位做过 Windows kernel 相关 infra 的工程师，并认为 human experts 短期内不会消失。

[推测] Paperboy 并不认为 AI 会立刻替代深度工程经验，反而在高难度 infra 上更需要人类专家。

[44:16] **大学是否仍然有意义**

[事实] 主持人问杰德辰为什么在 AI 时代仍然读大学。

[事实] 杰德辰说，对大多数人来说读大学仍然有意义，因为很多同龄人不确定未来要做什么，也不确定自己能做什么。

[事实] 他认为大学提供相对短的一段时间，用四年做探索和提升技术能力，对大多数人有用。

[事实] 他也说，如果一个人已经确定想做什么，并且有机会去做，那么不上学或离开学校也是理性选择。

[45:22] **为什么加入 Paperboy**

[事实] 杰德辰说，选择创始人时可以看 intercept 和 slope，而他认为匠杨是 high slope founder。

[事实] 他认为匠杨在很短时间里做出了很多厉害的事情，有 agency，学习很快，也有研究、工程和产品品味。

[事实] 他还说自己和匠杨合作很久，对合作顺畅有高信心，并认为匠杨有 charisma。

[推测] 对杰德辰来说，加入 Paperboy 不只是看公司当前状态，也是在押注创始人的学习速度和长期成长曲线。

[46:45] **招聘：不 hard sell，而是匹配与兑现**

[事实] 匠杨说自己会单独对待每个候选人，没有固定 script，也不喜欢 hard sell 公司。

[事实] 他认为比 recruiting 更重要的是自己的 reliability，即招到人后能否兑现对方需要的东西。

[事实] 他强调要选 great people，不能和 mediocre people 聊太多。

[事实] 他会通过候选人的 past work 和 past life decisions 理解对方，因为这些东西很难伪造。

[47:49] **喜欢的产品与拒绝 acqui-hire**

[事实] 匠杨说除了 Paperboy，自己仍然喜欢 Cursor；杰德辰说自己特别喜欢 Codex。

[事实] 主持人提到匠杨第一次创业做 Millian 时，有来自 Cognition、Vercel、Sentry 等公司的收购 offer。

[事实] 匠杨说这些主要是 acqui-hire，是为了人才，不是很多钱；加入后就像普通员工一样在别人的想法上工作。

[事实] 他表示自己不太关心 DevTools，也不想加入 Sentry、Vercel 或 Cognition，因此没有接受。

[49:02] **Codex、Claude Code 与基础设施优势**

[事实] 杰德辰认为 Claude Code 最重要的是体现 Opus 模型有多好，而不是 CLI 本身有多好。

[事实] 他喜欢 Codex 的几个点：核心 agent 和 CLI/agent loop 开源，桌面端 app 的 craft 水平很高，computer use、browser use 做得 polished。

[事实] 他认为 Codex 是较早把多个 agent 高并行同时工作作为主要 UI 的产品。

[事实] 他还认为 OpenAI 在 infra 层面相比 Anthropic 有更大优势，可以补贴更多 compute，因此稳定性更好。

[51:04] **OpenAI、Anthropic 与价值观差异**

[事实] 杰德辰说，如果买二级市场股票，他可能会 80% 买 OpenAI、20% 买 Anthropic。

[事实] 他认为 Anthropic 在 interpretability 和 social impact 上做得很好，但在模型使用方式和道德层面过于 opinionated。

[事实] 他更喜欢 OpenAI 相对 unopinionated 的价值观，即在一定限制下让用户按自己想法使用模型。

[事实] 匠杨说如果按当前估值做投资决策，他不会买这两家公司中的任何一家，但个人更偏好 Anthropic 对 safety 的 commitment。

[52:00] **模型公司与产品公司的边界会模糊**

[事实] 主持人问如何看“模型一切”的说法。

[事实] 杰德辰认为可以 argue 很多公司会提供差不多的模型，产品差异性仍然在产品公司里。

[事实] 他以 Cursor 为例，说 Cursor 一开始是产品公司，但现在既是产品公司也是模型公司，可以用 XAI 的 compute 去做 frontier coding model。

[事实] 他认为公司不能把自己局限为模型公司或产品公司。

[52:58] **假想投资方向：robotics 与 AI security**

[事实] 杰德辰说自己会特别想投 robotics，因为在自动化 knowledge work 之后，很可能最大的市场是用 model capability 进化物理世界。

[事实] 他也看好 AI 加 security，认为这是非常好的领域，需求机会很高。

[事实] 他认为随着模型变强，attacker 和 defender 的能力都会增强，安全公司的市场很大。

[事实] 他提到机会可能在更好的 harness、把人类 security researcher 的 heuristic 放进 agent，或构建大型 multi-agent 系统不断挖漏洞。

[54:24] **安全、国家能力与未回答的结尾问题**

[事实] 杰德辰说安全能力对国家安全非常重要，同时也是创业机会。

[事实] 他认为最强模型的拥有者可能有 incentive 限制模型只给自己国家使用，因此不同国家或利益群体都会需要这类模型，市场很大。

[事实] 主持人在 54:54 追问一年后的 Paperboy 会是什么状态、期待什么、害怕做错什么；转录稿没有保留具体回答，随后进入致谢。

[推测] 结尾问题缺失让本期没有完整呈现 Paperboy 对未来一年里程碑和风险的正式表述。

## 播客点评/总结

[推测] 本期最有价值的部分，是把 Agent 产品的竞争从“谁的模型更强”拉回到“Agent 如何进入人的真实工作流”。Paperboy 的思考集中在 OS 级上下文、长期记忆、主动性、个性化和 IM 化界面，这些问题比单纯聊天框更接近下一代生产力工具的核心矛盾。

[推测] 亮点在于嘉宾非常具体地讨论了产品形态：从 meeting prep、OS autocomplete、PR description、招聘 Agent，到 IM/inbox 界面和 Slack 互补层，都能看到团队不是只在讲愿景，而是在反复寻找可落地的 form factor。

[推测] 局限也很明显：Paperboy 当时产品尚未正式发布，很多效果来自团队内部使用和创始人叙述，缺少外部用户规模、留存、隐私安全机制和商业化验证。尤其是 OS 级数据采集带来的信任问题，在转录稿中没有被充分展开。

[推测] 这期适合关注 AI Agent、个人效率工具、企业协作软件、AI 原生界面和早期创业的人听；如果只想了解已经成熟可用的工具评测，本期会偏战略和产品哲学，而不是操作教程。
