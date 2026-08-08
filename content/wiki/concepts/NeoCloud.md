---
title: "Neo Cloud"
type: concept
tags: [ai, cloud, infrastructure, gpu]
sources: [jia-yangqing-wo-suo-jingli-de-rengongzhineng-yisi-dao-ai-dianfu-shijie-de-shunian-jubian-chuantai-shengdongjixi-s10e24-a3884ade-4669-4d5c-ab2e-f98aa580f429, e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41, e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b]
last_updated: 2026-08-08
---

# Neo Cloud

[[jia-yangqing-wo-suo-jingli-de-rengongzhineng-yisi-dao-ai-dianfu-shijie-de-shunian-jubian-chuantai-shengdongjixi-s10e24-a3884ade-4669-4d5c-ab2e-f98aa580f429]] adds [[LeptonAI|Lepton AI]] as a founder-operator view of the neocloud category. [[JiaYangqing|Jia Yangqing]] distinguishes AI cloud from traditional cloud by the need for tightly connected [[GPU|GPU]] capacity, scheduling, model-serving layers, and hardware-software fit.

[[e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]] adds the open-model competition version. [[WangTiezhen|王铁镇]] argues that neoclouds can use strong open-weight models such as [[KimiK3|Kimi K3]] to compete against closed API providers, because the serving layer can focus on hardware efficiency, scheduling, model hosting, and lower token prices rather than owning a closed frontier model.

Neo cloud is the AI-native GPU-cloud model discussed in [[e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b]]. [[AlexGMICloud|Alex]] contrasts neoclouds with hyperscalers: hyperscalers grew from CPU and storage cloud and often expose VM-oriented abstractions, while neoclouds are more likely to use k8s clusters and bare-metal access to preserve GPU efficiency.

The concept belongs under [[MaaSInfrastructure]] because customers are not only renting machines. In the source, a stronger neocloud offers earlier [[Nvidia]] GPU access, cluster management, model services, and kernel optimization so AI teams can convert accelerators into useful training and inference capacity.

## Key Claims
- Neoclouds compete on AI workload fit rather than generic cloud breadth.
- Bare-metal efficiency can matter when virtualization overhead reduces expensive GPU utilization.
- K8s cluster management, model services, and kernel optimization can turn raw hardware into a more defensible product.
- Neoclouds still face [[DataCenterPowerBottleneck|land and power]], supply-chain, and SLA constraints.
- Strong open weights can let neoclouds sell model serving and optimization without first building a proprietary frontier model.

## Connections
- [[GMICloud]], [[AlexGMICloud|Alex]], and [[GPUCloudOperations]] - source case and operating requirements.
- [[Nvidia]], [[GPU]], and [[AIInfrastructureFullStackMoat]] - hardware and ecosystem context.
- [[MaaSInfrastructure]], [[AIComputeContinuity]], and [[StrategicAIInfrastructureDependence]] - platform and dependence frame.
- [[KimiK3]], [[OpenWeightCommercialLicensing]], [[ClosedModelAPIMoatPressure]], and [[AgentInferenceWorkload]] - open-model serving branch added by E246.
