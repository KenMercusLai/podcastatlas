---
title: "Production Robot Scenario Selection"
type: concept
tags: [robotics, commercialization, product-strategy]
sources: [yushu-shangshi-baozhang-dan-renxing-jiqiren-de-qian-daodi-cong-nali-zhuan-s10e26-4a50d4a3-a6ff-4c89-b754-367b73ce924b, 173-duihua-yao-song-shenjian-dongfang-kongjian-zaichufa-tiancai-shaonian-shinian-hou-1-173-1, tech-20260106-0106-mp-tech-pod-128-tech-20260106-0106-mp-tech-pod-128, chef-vs-robot, jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, 132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan]
last_updated: 2026-08-24
---

# Production Robot Scenario Selection

[[yushu-shangshi-baozhang-dan-renxing-jiqiren-de-qian-daodi-cong-nali-zhuan-s10e26-4a50d4a3-a6ff-4c89-b754-367b73ce924b]] adds a demand-quality test to scenario selection. The source argues that warehouse logistics robots, industrial collaborative robots, restaurant delivery robots, and hotel delivery robots are more commercially legible because the task is bounded and repeatable, while general home humanoids remain earlier because safety, liability, form, and task frequency are less settled.

[[chef-vs-robot]] adds a restaurant-kitchen scenario through [[RobbyWokbot]]. The case fits a bounded production scene: repeated wok motions, predictable ingredient prompts, high labor intensity, and visible throughput gains, but it also exposes quality and breakdown constraints through [[WokHei]] and [[RobotChefCostQualityTradeoff]].

Production robot scenario selection is [[GaoJiyang]]'s method for deciding where [[Xinghaitu]] should commercialize [[EmbodiedAI]]. The source frames good early scenes as those where current robot capability can create real value without requiring extreme speed, zero-error reliability, or narrow one-off customization.

[[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] adds [[RobotLogisticsSorting]] as a concrete humanoid-robot wedge. Logistics sorting is bounded enough to show customer value, but still exposes tail cases such as soft packages, odd shapes, fallen objects, and labels that need flipping or flattening.

[[tech-20260106-0106-mp-tech-pod-128-tech-20260106-0106-mp-tech-pod-128]] adds [[BlueJ]] as a non-humanoid logistics example. [[AmyWebb]]'s description of overhead robotic arms moving packages faster and more cheaply reinforces the scenario-selection point: near-term robotics value is likelier in bounded operational infrastructure than in general household service.

[[173-duihua-yao-song-shenjian-dongfang-kongjian-zaichufa-tiancai-shaonian-shinian-hou-1-173-1]] adds [[StridingAI]]'s retail and 3C manufacturing scenario route. [[YaoSong]] does not present these scenes as the final limit of physical intelligence; he treats them as early places where current capability, data collection, remote systems, and [[MilestoneCommercialization]] can form a practical loop.

## Key Claims
- Gao defines the supply side through speed, precision, and generalization, with current attention on near-human speed, centimeter-level manipulation, and few-shot or zero-shot adaptation.
- Good early scenes should not demand very high speed, should tolerate limited failure cost, and should have global scaling potential.
- The source groups labor actions as Carry, Pick, Pack, Fold, and Operate.
- The scenes Gao names favor warehouse logistics, bin picking, and in-factory logistics over broad household generalization.
- Scenario choice is connected to data: the right scene should create useful, repeated, grounded data for model improvement.
- The LateTalk source reinforces logistics as a realistic early proving ground because it combines repeatable labor, messy manipulation, and clearer buyer understanding than entertainment-style robot demos.
- Restaurant wok automation is another bounded scene, but customer taste judgment and service downtime make the failure-cost calculation different from warehouse sorting.
- BlueJ adds a package-handling example where the task is concrete enough to link robotics progress directly to throughput, cost, and labor concerns.
- Striding AI adds a partner-access version: scenes can be selected not only for task fit, but also for whether the founder can secure enough deployment permission, data, and commercial feedback to improve the full stack.
- The Unitree listing source adds that scenario quality should include [[RobotRepurchaseDemand]]: a buyer who purchases every year is stronger evidence than one-off research, government, or performance demand.

## Connections
- [[Xinghaitu]] and [[GaoJiyang]] — company and source speaker.
- [[WheelBasedDualArmRobots]] — robot form chosen for the target work.
- [[PhysicalWorldDataFlywheel]] and [[RealRobotDataStrategy]] — data loop that depends on scene access.
- [[ProductLedWillingnessToPay]] and [[CustomerPull]] — demand signals the production scene must eventually prove.
- [[RobotLogisticsSorting]], [[FigureAI]], [[XingdongEra]], and [[DexterousManipulation]] — Q2 2026 logistics-sorting examples and manipulation constraints.
- [[RobbyWokbot]], [[RestaurantAutomation]], [[WokHei]], and [[RobotChefCostQualityTradeoff]] - restaurant production scenario added by Planet Money.
- [[Amazon]], [[BlueJ]], [[PhysicalAI]], and [[AutomationDisplacementEffect]] - overhead package-handling scenario added by Marketplace Tech.
- [[StridingAI]], [[YaoSong]], [[CPGroup]], [[PhysicalIntelligenceSystemStack]], and [[MilestoneCommercialization]] — retail and 3C manufacturing scenario route added by episode 173.
- [[RobotRepurchaseDemand]], [[UnitreeIPOValuation]], and [[HumanoidRobotCommercialization]] — S10E26's repeat-demand and public-market proof branch.
