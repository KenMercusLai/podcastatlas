+++
title = 'Four CEOs on the Future of AI: CoreWeave, Perplexity, Mistral, and IREN'
date = 2026-03-23T18:07:00Z
show = 'All-In with Chamath, Jason, Sacks & Friedberg'
source_url = 'https://allinchamathjason.libsyn.com/four-ceos-on-the-future-of-ai-coreweave-perplexity-mistral-and-iren'
duration = '5859'
draft = false
+++

# Four CEOs on the Future of AI: CoreWeave, Perplexity, Mistral, and IREN

## 概览

This episode is built around four CEO interviews at Nvidia’s GTC conference, using infrastructure, products, enterprise deployment, and energy as four angles on the same AI boom. The discussion keeps returning to one question: whether AI demand is constrained more by model quality, chips, power, data access, or real-world buildout speed.

CoreWeave presents the AI cloud as a capital markets and operations business, not just an engineering project. Perplexity frames the next interface as AI that controls browsers, computers, files, connectors, and models on behalf of users. Mistral focuses on open models, enterprise customization, data segregation, and governed agent workflows. IREN argues that data centers, power, labor, grid connections, and latency are now central to AI strategy.

[推测] The episode’s broad conclusion is that AI competition is moving beyond “who has the best model” toward who can orchestrate models, finance and deploy compute, connect private data safely, and secure energy at industrial scale.

## 分段落总结

[00:42] **CoreWeave’s Path From Crypto To AI Cloud**

[事实] CoreWeave’s CEO says the company began in 2017 after the founders moved from an algorithmic natural gas hedge fund into crypto and GPU-based Ethereum mining.

[事实] They preferred GPUs over Bitcoin ASICs because GPUs could be redeployed to other use cases beyond mining.

[事实] CoreWeave moved from crypto into CGI rendering, batch computing, medical research, and eventually neural network workloads around 2020-2021.

[推测] The origin story is used to present CoreWeave’s advantage as early operational learning with scarce GPU infrastructure before the ChatGPT demand surge.

[04:00] **Learning AI Infrastructure Through Open Source Researchers**

[事实] CoreWeave bought A100s and donated compute to the EleutherAI open-source community to learn how to run large-scale parallelized computing.

[事实] The CEO describes those GPUs as “tuition” for learning the business, because researchers later wanted the same infrastructure at their day jobs.

[事实] He says that experience helped launch the commercial business.

[05:03] **Scaling Laws And Purpose-Built Compute**

[事实] CoreWeave concluded before the ChatGPT moment that scaling laws would drive demand and that compute “decommoditizes at scale.”

[事实] The company positions itself above Nvidia GPUs and below models, handling software, integration, operations, and observability for AI-specific cloud infrastructure.

[事实] CoreWeave’s first large commercial language-model customer was Inflection, followed by hyperscalers and foundation model companies including OpenAI.

[推测] CoreWeave’s thesis is that generic cloud platforms are less optimized for large AI training and inference than specialized GPU clouds.

[08:00] **Inference As AI Monetization**

[事实] CoreWeave says usage has shifted from research and training into productized inference at massive scale.

[事实] The CEO defines inference as the moment when users ask a model for an answer or ask it to do something.

[事实] He calls inference the monetization of investment in artificial intelligence.

[推测] The discussion implies that sustained inference demand is more important for infrastructure durability than one-time training runs.

[09:25] **GPU Generations, Depreciation, And Useful Life**

[事实] CoreWeave says it was early at bringing H100s, H200s, GB200s, and then GB300s into commercial production at scale.

[事实] The CEO rejects claims that GPUs become obsolete in 16-18 months, saying CoreWeave’s average contract is five years and the company uses six-year depreciation.

[事实] He says A100-class GPUs still have demand, including from new companies, smaller models, inference, experiments, and less bleeding-edge workloads.

[推测] His argument is that GPU value is constrained less by age alone than by whether data-center power can be repurposed for higher-margin use.

[16:18] **GPU Allocation And Competition**

[事实] CoreWeave says more competitors entering GPU cloud is an affirmation that the business is healthy.

[事实] The CEO says Nvidia does not appear to allocate by favoritism; customers place orders and Nvidia fulfills them in order.

[事实] CoreWeave focuses on clients that fit its contract and financing requirements.

[18:44] **The Financing “Box” Model**

[事实] CoreWeave describes creating a financing “box” containing the customer contract, GPUs, data-center contract, and cash-flow waterfall.

[事实] Customer payments go into the box first to pay data center, power, interest, and principal, with remaining cash flowing back to CoreWeave.

[事实] The CEO says this structure helped CoreWeave raise $35 billion in 18 months and pay off principal and interest within about two and a half years of a five-year deal.

[事实] He says CoreWeave’s cost of capital fell by 600 basis points over two years.

[23:47] **Demand, Risk Management, And Supply Bottlenecks**

[事实] CoreWeave says AI compute demand has been relentless and overwhelms global capacity.

[事实] The company protects itself with long-term contracts and large-balance-sheet counterparties in case demand suddenly disappears.

[事实] The CEO says constraints are not only GPUs, but also power, shells, memory, storage, networking, optics, and other components.

[26:30] **Memory, Energy, And Infrastructure Cycles**

[事实] The CEO says memory has become a throttle because AI demand surged while the necessary fab investment cycle did not happen early enough.

[事实] Jason and the CoreWeave CEO compare AI infrastructure to earlier boom-bust cycles in fiber, storage, and energy.

[事实] They discuss how overbuilt infrastructure later enabled products like YouTube, Zoom, and modern video distribution.

[推测] The segment argues that even overinvestment can leave useful infrastructure behind for future companies.

[30:44] **Falling Token Costs And Lower Barriers**

[事实] The CoreWeave CEO cites a discussion where token costs fell from roughly $32 per million tokens around ChatGPT-3 to nine cents.

[事实] He says AI lowers the barrier to operations, letting people with good ideas build software, research tools, or creative products more easily.

[推测] The CoreWeave interview ends on the view that cheaper compute expands the number of people who can create useful products.

[33:05] **Perplexity’s Product Evolution**

[事实] Jason introduces Perplexity through three product phases: choosing among models, real-time information modules, the Comet browser, and Perplexity Computer.

[事实] Perplexity’s CEO says the company has focused for three and a half years on accuracy and trust.

[事实] He says Perplexity Ask gives AI internet access, Comet gives AI browser access, and Computer gives AI access to a full computer environment.

[35:00] **AI As Model Orchestra**

[事实] Perplexity describes Computer as an orchestration layer across GPT, Claude, Gemini, and other models.

[事实] The CEO says models are instruments, sub-agents are musicians, and the output is the work AI completes for the user.

[事实] He says different models specialize in coding, writing, multimodal work, image, video, and audio.

[推测] Perplexity’s strategy is to win by routing work across many specialized models rather than owning a single frontier model.

[37:20] **Personal Computer And Hybrid Execution**

[事实] Perplexity is working on a “personal computer” concept that synchronizes server-side Perplexity Computer with local hardware such as a Mac mini.

[事实] Local private data can be orchestrated locally, while complex or long-running tasks can be delegated to server-side hardware accessible only to the user.

[事实] The CEO says the goal is to avoid users managing API keys, billing, and model access across many services.

[39:17] **Local Models, Workstations, And AI As OS**

[事实] The discussion covers local models running on Mac Studio-class hardware and Nvidia/Dell workstation announcements with large RAM.

[事实] Perplexity’s CEO says local models may initially operate as sub-agents for private materials such as tax returns, photos, emails, calendars, and notes.

[事实] He says AI becomes the operating system because users start from objectives rather than programmatic instructions.

[推测] The future computer described here is less a visible desktop interface and more a persistent AI runtime coordinating files, tools, connectors, and models.

[44:01] **Perplexity’s Business And Enterprise Growth**

[事实] Perplexity says it has several tens of millions of monthly users and thousands of corporate customers.

[事实] The CEO says enterprise is the company’s fastest-growing revenue business.

[事实] Enterprise Pro costs $40 per month and Enterprise Max costs $400 per month, according to the transcript.

[事实] He says every dollar of Perplexity revenue has positive gross margin, though the overall company is not yet profitable.

[47:47] **Independence And Multi-Model Moat**

[事实] Asked why Perplexity stays independent amid competition from OpenAI, Google, Anthropic, xAI, Amazon, and Meta, the CEO points to multi-model orchestration.

[事实] He says Perplexity can use GPT, Gemini, Claude, Llama, DeepSeek, Kimi, Nemotron, Qwen, and other models without betting on one provider.

[事实] He says Perplexity pings models directly rather than bundling users’ subscriptions to other AI services.

[50:32] **Model Council And Shipping Speed**

[事实] Perplexity built “Model Council,” which runs a prompt across multiple models and summarizes agreement, disagreement, and nuance.

[事实] The CEO says speed is Perplexity’s moat and that small-company execution lets it ship faster than larger competitors.

[事实] He says AI coding tools have accelerated Perplexity’s own shipping cadence and helped non-engineers ship code through Slack-based workflows.

[52:24] **Bespoke Software And Automated Workflows**

[事实] Jason describes asking an AI agent to map LinkedIn relationships and then having it offer to build a CRM.

[事实] Perplexity’s CEO says Computer generated a board memo, a partnership deck, and a press briefing memo internally.

[事实] He says newer models became much better at orchestration, reasoning, tool calls, files, sub-agents, skills, and command-line tools.

[推测] This section frames AI agents as capable of replacing small bespoke internal tools and manual research workflows.

[57:37] **Autonomous Businesses And Job Displacement**

[事实] Perplexity’s CEO says the dream is to help businesses run as autonomously as possible, including ad campaigns, SEO, Stripe, feature shipping, and customer support.

[事实] Jason raises concern that the same tools enabling solo entrepreneurs could reduce hiring needs.

[事实] The CEO argues that temporary job displacement should be weighed against new opportunities for people to build mini businesses with agency and ownership.

[推测] The optimistic view depends on individuals actively learning and using the tools rather than passively waiting for labor markets to adjust.

[62:14] **Comet, Mobile, And Web Agent Access**

[事实] Perplexity says Computer is already available inside the Perplexity app and Comet’s value is that AI can natively control the browser.

[事实] The CEO says browser control remains important because many tasks still require opening tabs, filling forms, clicking, and uploading files.

[事实] Jason argues paid websites should let authenticated user agents perform limited, well-behaved actions on behalf of subscribers.

[事实] Perplexity’s CEO says user choice and win-win API access for websites is where the world should go.

[67:17] **Mistral’s Nvidia Partnership And Open Models**

[事实] Mistral’s CEO says the company is announcing work with Nvidia to train the next generation of frontier models.

[事实] He says Mistral’s goal is to produce the best open-source models and specialize them for enterprise customers through products such as Forge.

[事实] He says specialization includes engineering, physics, science, languages, and government use cases.

[68:16] **Building AI From Europe With A Global Footprint**

[事实] Mistral says 25% of its business is in the United States and 25% of its researchers are in the United States.

[事实] The CEO says he spends time in France, the UK, Singapore, and the US.

[事实] He says European customers include companies that are lagging and want to adopt AI to leap forward, especially in markets with manufacturing and language needs.

[69:49] **Open Models For Enterprise IP**

[事实] Mistral says general-purpose models are needed for orchestration, but enterprises also need specialized models for their intellectual property and physical-system signals.

[事实] The CEO says open models allow deeper customization, added parameters, deployment on any cloud, customer hardware, or the edge.

[事实] Mistral works with subject matter experts to build bespoke business applications by modifying both models and the harness around them.

[推测] Mistral’s position is that closed frontier models alone are insufficient for enterprises with sensitive, domain-specific data.

[71:13] **Data Segregation And Forward Deployment**

[事实] Mistral says data segregation is handled through a portable platform deployed on customer infrastructure.

[事实] The CEO says data does not flow back to Mistral because training tools and data-processing tools stay with the customer.

[事实] Mistral sends PhD-level forward deployment engineers and scientists to work with domain experts before customers can retrain and operate more independently.

[73:16] **Synthetic Data And Human Signal**

[事实] Mistral uses synthetic data to warm up models and train smaller models from larger teacher models.

[事实] The CEO says synthetic data is efficient at the beginning but not enough by itself.

[事实] He says human signal from experts remains necessary and costly because experts must give feedback to machines.

[74:31] **OpenClaw And Enterprise Agent Controls**

[事实] Mistral says OpenClaw showed the autonomy agents can give individual builders, but enterprises need more controls for mission-critical workflows.

[事实] The CEO says enterprise processes such as KYC require deterministic gates, observability, governance, and guarantees for executives.

[事实] He says proper control planes, sandboxes, data-source connections, and access controls can unlock agents safely for employees.

[77:21] **Context Engines And Organizational Change**

[事实] Mistral says enterprise data cannot be treated as one shared pool accessible by everyone.

[事实] The CEO describes a “context engine” that maps where data sits and uses metadata to control who can access it.

[事实] He says compensation data, for example, must not flow broadly through the enterprise.

[推测] The discussion suggests AI agents will force companies to redesign IT systems, management information flows, and customer service operations.

[79:04] **IREN’s Move From Bitcoin To AI**

[事实] Daniel Roberts says IREN began by building large-scale data centers, with Bitcoin mining as the first use case to bootstrap cash flow.

[事实] He says the original thesis was that growth in the digital world would eventually strain the real world.

[事实] IREN is now swapping Bitcoin mining infrastructure for AI chips.

[80:17] **AI Demand And Self-Developed Data Centers**

[事实] Roberts says IREN had a false start in AI around 2020 with a Dell MOU, then returned to Bitcoin until AI demand accelerated about two years before the interview.

[事实] IREN develops its own data centers by finding land, getting permits, and applying for grid connections.

[事实] Its flagship Texas site is described as 750 megawatts.

[81:33] **Power Holdings And Time To Compute**

[事实] Roberts says Microsoft is one of IREN’s early partners and that IREN signed a $9.7 billion contract with Microsoft late the prior year.

[事实] He says that Microsoft contract represents 5% of IREN’s capacity.

[事实] IREN has four and a half gigawatts of power, which he compares to almost as much annual power as the Bay Area uses.

[事实] Roberts says IREN’s main constraint is not power but “time to compute.”

[82:26] **Labor, Construction, And Local Communities**

[事实] Time to compute includes tradespeople, foundations, water cooling systems, supply chains, and manual construction work.

[事实] Roberts says IREN needs thousands of people in locations that have not historically supported that scale.

[事实] IREN says it hires locally, supports communities, and is reaching $1 million in cumulative community grants.

[84:27] **Trades, Retraining, And AI Job Creation**

[事实] IREN locates near heavy electrical infrastructure, often where old manufacturing or industry has closed down.

[事实] Roberts says the company leverages sunk capital expenditure, rehires and retrains local workforces, and partners with universities and trade colleges.

[事实] When Jason suggests tradespeople may earn around $150,000 to $300,000, Roberts says the lower end is directionally right.

[推测] The segment contrasts AI-driven white-collar job anxiety with rising demand for skilled physical infrastructure labor.

[86:15] **Renewable Energy And Grid Arbitrage**

[事实] Roberts says IREN has used 100% renewable energy since inception.

[事实] IREN uses hydro in British Columbia and wind and solar in West Texas.

[事实] Roberts says West Texas has around 45-50 gigawatts of wind and solar, while transmission to load centers is about 12 gigawatts.

[事实] He says data centers can locate at the source of low-cost excess renewable energy and export the result as tokens.

[88:26] **Grid Connections And Demand Strength**

[事实] Roberts says IREN does not need to handle battery intermittency directly because utilities guarantee 24/7 reliable power through grid connections.

[事实] He declines to comment on whether OpenAI is a partner.

[事实] He says demand is still “gangbusters,” IREN cannot meet demand, and there are no idle GPUs sitting in data centers.

[89:27] **Jevons Paradox And Compute Demand**

[事实] Jason asks whether software and transport improvements could reduce token costs by 50x.

[事实] Roberts argues the opposite effect is likely: faster and cheaper compute will increase usage.

[事实] He uses image generation as an example, saying if images take five to ten seconds instead of minutes, users will generate more images.

[推测] The argument is that AI compute demand may expand as efficiency improves, rather than shrink.

[90:22] **Custom Silicon, Nvidia, And Local AI Hardware**

[事实] Roberts says custom silicon from companies such as Google, Amazon, and Meta is emerging to various degrees and looking for data-center homes.

[事实] He says Nvidia has a massive head start through its ecosystem and standards.

[事实] He calls following Nvidia’s roadmap the safest path for early large-scale buildout.

[事实] On local AI hardware, Roberts says software breakthroughs, agents, robotics, autonomous vehicles, and local compute demand are real and compounding.

[92:25] **Nuclear, Networking, Space, And Latency**

[事实] Roberts says nuclear projects likely take a decade or longer to reach commissioning, but now is the time for policy, capital, and planning.

[事实] He says small modular reactors near data centers could expand the market and strengthen the US competitive advantage.

[事实] He says data-center networking is critical because latency, cabling, hops, InfiniBand, and Ethernet affect cluster performance.

[事实] Roberts says West Texas latency to Dallas is about six milliseconds round trip, making remote data-center locations viable when fiber exists.

## 播客点评/总结

[推测] The episode’s biggest value is that it connects AI software enthusiasm to the physical and financial systems underneath it: GPUs, depreciation, debt structures, power, memory, grid access, construction labor, and data-center networking.

[推测] The strongest moments come from the CEOs explaining operating details rather than repeating generic AI optimism. CoreWeave’s financing box, Perplexity’s model orchestration, Mistral’s enterprise data segregation, and IREN’s power-location strategy each make the AI boom more concrete.

[推测] The main limitation is that the interviews are founder-led and highly bullish. The transcript includes questions about bubbles, depreciation risk, job displacement, website access, and power constraints, but the answers mostly emphasize continued demand and opportunity.

[推测] This episode is best suited for listeners interested in AI infrastructure, enterprise AI deployment, agent products, data-center economics, and the capital and energy requirements behind frontier AI.
