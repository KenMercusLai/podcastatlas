---
title: "Production Robot Scenario Selection"
type: concept
tags: [robotics, commercialization, product-strategy]
sources: [chef-vs-robot, jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, 132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan]
last_updated: 2026-07-08
---

# Production Robot Scenario Selection

[[chef-vs-robot]] adds a restaurant-kitchen scenario through [[RobbyWokbot]]. The case fits a bounded production scene: repeated wok motions, predictable ingredient prompts, high labor intensity, and visible throughput gains, but it also exposes quality and breakdown constraints through [[WokHei]] and [[RobotChefCostQualityTradeoff]].

Production robot scenario selection is [[GaoJiyang]]'s method for deciding where [[Xinghaitu]] should commercialize [[EmbodiedAI]]. The source frames good early scenes as those where current robot capability can create real value without requiring extreme speed, zero-error reliability, or narrow one-off customization.

[[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] adds [[RobotLogisticsSorting]] as a concrete humanoid-robot wedge. Logistics sorting is bounded enough to show customer value, but still exposes tail cases such as soft packages, odd shapes, fallen objects, and labels that need flipping or flattening.

## Key Claims
- Gao defines the supply side through speed, precision, and generalization, with current attention on near-human speed, centimeter-level manipulation, and few-shot or zero-shot adaptation.
- Good early scenes should not demand very high speed, should tolerate limited failure cost, and should have global scaling potential.
- The source groups labor actions as Carry, Pick, Pack, Fold, and Operate.
- The scenes Gao names favor warehouse logistics, bin picking, and in-factory logistics over broad household generalization.
- Scenario choice is connected to data: the right scene should create useful, repeated, grounded data for model improvement.
- The LateTalk source reinforces logistics as a realistic early proving ground because it combines repeatable labor, messy manipulation, and clearer buyer understanding than entertainment-style robot demos.
- Restaurant wok automation is another bounded scene, but customer taste judgment and service downtime make the failure-cost calculation different from warehouse sorting.

## Connections
- [[Xinghaitu]] and [[GaoJiyang]] — company and source speaker.
- [[WheelBasedDualArmRobots]] — robot form chosen for the target work.
- [[PhysicalWorldDataFlywheel]] and [[RealRobotDataStrategy]] — data loop that depends on scene access.
- [[ProductLedWillingnessToPay]] and [[CustomerPull]] — demand signals the production scene must eventually prove.
- [[RobotLogisticsSorting]], [[FigureAI]], [[XingdongEra]], and [[DexterousManipulation]] — Q2 2026 logistics-sorting examples and manipulation constraints.
- [[RobbyWokbot]], [[RestaurantAutomation]], [[WokHei]], and [[RobotChefCostQualityTradeoff]] - restaurant production scenario added by Planet Money.
