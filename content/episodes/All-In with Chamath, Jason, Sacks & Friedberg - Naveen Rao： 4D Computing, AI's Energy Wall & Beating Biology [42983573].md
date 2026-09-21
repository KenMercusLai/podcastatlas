+++
title = "Naveen Rao: 4D Computing, AI's Energy Wall & Beating Biology"
date = 2026-09-21T21:03:00Z
show = 'All-In with Chamath, Jason, Sacks & Friedberg'
source_url = 'https://allinchamathjason.libsyn.com/naveen-rao-4d-computing-ais-energy-wall-beating-biology'
duration = '1355'
draft = false
+++

# 4D Computing, AI’s Energy Wall, and Beating Biology

## 概览

Naveen Rao, co-founder and CEO of Unconventional AI, argues that energy—not chip availability or data-center floor space—is becoming the primary constraint on AI growth. As models and demand expand, conventional computing architectures spend too much energy moving data between memory and compute.

Drawing inspiration from the efficiency of biological brains and other naturally occurring dynamical systems, Rao proposes a different computing substrate. Instead of implementing neural networks through layers of digital abstractions and conventional linear algebra, Unconventional AI uses the physical, time-varying behavior of interconnected oscillators to perform computation.

Rao presents the company’s first physical dynamical-computing prototype, which generated images at roughly 500 nanojoules per image in its initial demonstration. He describes this architecture as “4D computing”: three physical dimensions enabled by die stacking, plus time as an intrinsic computational dimension.

The long-term ambition is to improve “intelligence per watt” by 1,000 times, eventually surpass biological efficiency, and enable AI to move beyond gigawatt-scale centralized data centers into distributed infrastructure and energy-constrained robots.

## 分段落总结

[00:00] **Rao’s background and thesis on AI**

[事实] Rao is introduced as the co-founder and CEO of Unconventional AI and as an entrepreneur who previously built and sold two deep-technology companies.

[事实] He describes himself as the opposite of an AI doomer and sees AI as a transformational technology capable of advancing humanity’s evolution.

[事实] His central thesis is that further progress in intelligence requires innovation in the underlying hardware substrate.

[01:14] **From childhood computing to neuroscience**

[事实] Rao began programming as a child after his family acquired a computer in the late 1970s.

[事实] His interest in science fiction and intelligent machines led him to electrical engineering, followed later by a PhD in neuroscience.

[事实] He says the combination of computer engineering and neuroscience positioned him to revisit the question of how machines can become intelligent.

[02:05] **Building AI chip and infrastructure companies**

[事实] Rao founded Nirvana Systems in 2014, describing it as the first AI chip company, at a time when AI was not yet part of common industry language.

[事实] After selling Nirvana Systems to Intel, he started and ran Intel’s AI group.

[事实] In 2020, he began building infrastructure that made large GPU clusters easier to scale and use for model development.

[事实] Demand accelerated after ChatGPT’s arrival in 2022, and the business joined Databricks in 2023; Rao says it now accounts for roughly one quarter of Databricks’ revenue.

[03:22] **Unconventional AI’s first-principles approach**

[事实] Unconventional AI is attempting to redesign computers from first principles for dramatically better power efficiency.

[事实] The company initially targeted a 1,000-fold efficiency gain within five years, but Rao shortened that target to three and a half years after progress exceeded expectations.

[事实] Its team spans mathematical and neuroscience theorists, model researchers, circuit designers, chip architects, and systems engineers.

[事实] Concepts are tested as trainable models on real data before being translated into physical circuits, boards, systems, and products.

[04:44] **AI’s approaching energy wall**

[事实] Rao cites Google’s reported monthly volume of 3.2 quadrillion tokens and estimates that, at 10 joules per token, this workload would correspond to 12 gigawatts.

[事实] He compares this with roughly 40 gigawatts consumed by US data centers and less than 100 gigawatts of total global data-center capacity.

[事实] Rao estimates that continued growth in model size and demand could cause AI to encounter an energy shortage within approximately three years.

[推测] The calculation is intended to demonstrate the scale of the constraint, but the transcript does not independently validate its assumptions about average energy per token or how the cited token volume maps to continuous power demand.

[05:53] **Power becomes the defining data-center resource**

[事实] Rao says data-center planning has shifted from prioritizing floor space, networking, and GPUs to securing an energy contract first.

[事实] He claims that energy represents about half the cost of serving a token, with hardware capital expenditure, facilities, and related costs making up the remainder.

[事实] Unconventional AI’s commercial proposition is to monetize each available watt up to 1,000 times more effectively than existing hardware.

[推测] If that efficiency target is realized at production scale, power availability could become less restrictive for AI operators, although other costs and bottlenecks would remain.

[07:04] **Biology as proof of efficient intelligence**

[事实] Rao points to the human brain’s approximate 20-watt power consumption as evidence that sophisticated intelligence can operate at far lower energy levels than current AI systems.

[事实] He says a monkey brain uses roughly one watt, comparable to a mobile phone, while smaller animal brains operate at milliwatt scale.

[事实] As an example, he says a squirrel brain consumes about eight milliwatts while supporting highly accurate movement between branches.

[事实] Rao concludes that biology has developed a physical substrate exceptionally well suited to intelligence.

[08:07] **Data movement as the primary source of inefficiency**

[事实] Rao argues that most energy in a modern computing system is spent moving information rather than performing computation.

[事实] He compares the human cortex, which he says moves roughly 16 billion bits per second, with a high-end GPU system moving nearly 30 trillion bits per second between chip and memory.

[事实] He adds that data movement inside the chip may be approximately 100 times greater than its external memory traffic.

[事实] In his account, synthetic systems consume so much power because they move vastly more information than biological brains.

[09:01] **Why conventional architecture reached its limit**

[事实] Rao traces computing from mechanical and analog machines to the digital architecture established in the 1930s and 1940s.

[事实] Modern computers still broadly separate memory from compute and move bits between them, much like early digital machines such as ENIAC.

[事实] This architecture was optimized for speed rather than energy efficiency.

[事实] Rao says transistor counts continued rising while clock frequency, single-threaded performance, and eventually efficiency gains stopped scaling at earlier rates.

[事实] He characterizes the efficiency benefits of transistor shrinking associated with Moore’s law as largely exhausted.

[10:23] **Removing layers of abstraction**

[事实] Digital computation abstracts continuous physical transistor states into binary ones and zeros.

[事实] Additional abstractions were subsequently layered on top, culminating in neural networks and learning systems implemented through digital operations.

[事实] Rao argues that each abstraction discards some of the physical system’s complexity and introduces inefficiency.

[事实] Unconventional AI instead seeks to connect an abstraction of semiconductor physics directly to the neural network.

[事实] Rao notes that brains do not explicitly perform floating-point arithmetic or linear algebra; intelligence emerges from the physical behavior of neurons.

[11:26] **Computation through dynamical systems**

[事实] Rao uses bird flocks and ant colonies to illustrate how simple local behaviors can produce complex, emergent collective behavior.

[事实] He identifies dynamical systems theory as the study of how such properties emerge from interactions among simpler components.

[事实] Unconventional AI applies these principles to circuit design, aiming to make computation arise from the physical evolution of the system itself.

[12:04] **Metronomes as a model for physical computation**

[事实] Multiple metronomes placed on a movable platform will gradually synchronize because each one influences the platform and therefore the others.

[事实] The system converges from different initial phases into a coordinated state through its physical coupling rather than through centrally executed instructions.

[事实] Rao suggests that more complex coupling patterns could produce multiple synchronized groups or opposing phase relationships.

[推测] The example reframes computation as controlled physical convergence toward useful states rather than as a sequence of conventional digital instructions.

[13:06] **UNO demonstrates oscillator-based image generation**

[事实] Unconventional AI released UNO, an open-source image-generation model constructed from simulated oscillators.

[事实] Rao presents UNO as the first demonstration that this type of dynamical system could be scaled, trained, and used to generate meaningful outputs.

[事实] When conditioned to generate objects such as airplanes, cars, or birds, the system follows different trajectories through its state space.

[事实] The images shown during the presentation were actual outputs generated by the model.

[14:11] **Sparsity improves efficiency and scalability**

[事实] Fully connecting a system causes the number of connections to grow quadratically, making large systems difficult to scale.

[事实] Sparsity removes some connections while attempting to preserve the behavior of the overall system.

[事实] Rao says the company found that sparse systems could become not only more efficient and scalable but also easier to train and higher-performing.

[事实] He reports achieving these results in both simulations and real physical systems.

[15:26] **The first physical dynamical-computing prototype**

[事实] Rao publicly unveils what he calls the first physical dynamical computer ever built.

[事实] The company produced the prototype in approximately five months, sending the design to fabrication on June 1 and later testing the returned chip in its laboratory.

[事实] Rao shows what he describes as the first images generated by this type of physical computer.

[事实] He says the architecture can also support tasks such as sequence modeling and language modeling.

[16:12] **Initial energy-efficiency result**

[事实] Rao reports that the prototype generates an image using approximately 500 nanojoules.

[事实] He contrasts this with conventional GPU-based computation operating on the order of millijoules for the comparable example.

[事实] He attributes the improvement to the architecture’s minimal information movement.

[推测] The prototype establishes an encouraging proof of concept, but the transcript provides no independent benchmark methodology, output-quality comparison, or end-to-end system power measurement.

[16:50] **The meaning of 4D computing**

[事实] Traditional CPUs, GPUs, and compute-in-memory designs remain variants of the von Neumann model because they retain a distinction between memory and computation.

[事实] In Rao’s dynamical computer, each computing element also acts as memory, eliminating a separate memory interface.

[事实] The company calls the approach “4D computing” because it combines three-dimensional physical integration with computation unfolding through time.

[事实] Rao says die stacking supplies the vertical physical dimension, while the dynamics of the system supply the temporal dimension.

[17:41] **Optimizing intelligence per watt**

[事实] Rao defines the central optimization target as intelligence per watt.

[事实] He says current computing is roughly ten billion times removed from the thermodynamic efficiency limit, while animal brains are within one or two orders of magnitude.

[事实] The company aims to reach the limits of two-dimensional lithography within three and a half years and ultimately make machines more efficient than biology.

[事实] Rao envisions the technology enabling pervasive computation, including new robotic forms, over roughly the next decade.

[18:32] **Distributed AI and billions of robots**

[事实] Rao predicts a shift from a small number of gigawatt-scale data centers toward many smaller, geographically distributed facilities.

[事实] He expects such infrastructure to be more local, adaptive, and environmentally friendly.

[事实] He also imagines billions of robots dynamically assembling or coordinating to solve large real-world problems.

[推测] These outcomes depend on the architecture achieving production-scale reliability, programmability, manufacturing economics, and efficiency close to the targets presented.

[19:03] **Jevons paradox and market expansion**

[事实] Rao invokes Jevons paradox: when the cost of a resource falls, consumption can rise by more than the savings achieved per unit.

[事实] He argues that making AI computation 1,000 times cheaper could increase total consumption by more than 1,000 times.

[事实] On that basis, he predicts that highly efficient AI computation could create the largest market humanity has ever seen.

[推测] This is an explicitly ambitious market forecast rather than a result demonstrated by the prototype.

[19:36] **Path from prototype to product**

[事实] In response to questions about commercialization, Rao says the company expects to deliver a full product within two years.

[事实] The intended product is a data-center system or complete rack that accepts and returns tokens over a network connection while using a radically different internal architecture.

[事实] Existing model families are expected to work, but models must be ported to the new substrate.

[事实] Rao acknowledges that this transition will require a meaningful amount of computation and engineering work.

[20:55] **Compatibility with existing AI models**

[事实] Rao describes a tradeoff between the size of a technological improvement and the amount of migration difficulty users will accept.

[事实] His strategy is to make the efficiency advantage compelling enough to justify the effort required to move models.

[事实] The system can be mathematically characterized using matrix operations, but it does not physically implement computation as standard matrix multiplication.

[事实] Instead, it realizes the equivalent behavior through time-varying system states and transitions.

[21:38] **An interdisciplinary team and programming layer**

[事实] The company combines dynamical-systems theorists with engineers who know how to design and manufacture chips.

[事实] Rao says coordinating specialists who traditionally do not communicate with one another is among the company’s greatest organizational challenges.

[事实] The company has built Python libraries that allow developers to express time-varying elements with stochastic behavior.

[事实] Rao distinguishes this programming layer from CUDA, describing it as a language-like interface suited to the new architecture.

## 播客点评/总结

The episode’s strongest contribution is its clear framing of AI’s energy problem as an architectural challenge. Rao connects data-center economics, biological efficiency, information movement, dynamical-systems theory, and semiconductor design into a coherent argument for replacing conventional compute-memory separation.

The physical prototype gives the discussion more substance than a purely theoretical proposal. The reported 500-nanojoule image-generation result, rapid chip-development timeline, and planned rack-scale product provide concrete milestones against which the company’s claims can eventually be evaluated.

[推测] The main limitation is that nearly all technical performance claims come from Rao’s presentation. The transcript does not supply standardized comparisons, image-quality metrics, manufacturing details, independent validation, or evidence that the efficiency advantage will survive model porting and complete-system deployment.

[推测] The episode is especially valuable for AI infrastructure engineers, semiconductor researchers, technical founders, investors, and listeners interested in alternatives to GPU-centric computing. It is less useful as a detailed engineering review because the discussion remains at the architectural and strategic level rather than disclosing implementation specifics.
