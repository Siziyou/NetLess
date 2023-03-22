# NetLess：基于Serverless架构的分布式神经网络推理系统

NetLess:Distributed Deep Neural Network Inference System based on Serverless

---

## 资源

[Demo设计](%E5%9F%BA%E4%BA%8EServerless%E6%9E%B6%E6%9E%84%E7%9A%84%E5%88%86%E5%B8%83%E5%BC%8F%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F%207f1b4cdc23324eccb030b594ee7f6cfc/Demo%E8%AE%BE%E8%AE%A1%203319e1088c8e48b085150f8338eaae99.md)

[周报](%E5%9F%BA%E4%BA%8EServerless%E6%9E%B6%E6%9E%84%E7%9A%84%E5%88%86%E5%B8%83%E5%BC%8F%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F%207f1b4cdc23324eccb030b594ee7f6cfc/%E5%91%A8%E6%8A%A5%20158d14e0b8ff4a148d2bc10a88b67b07.md)

[实现方案](%E5%9F%BA%E4%BA%8EServerless%E6%9E%B6%E6%9E%84%E7%9A%84%E5%88%86%E5%B8%83%E5%BC%8F%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F%207f1b4cdc23324eccb030b594ee7f6cfc/%E5%AE%9E%E7%8E%B0%E6%96%B9%E6%A1%88%200c480ce7b92c4acc9188221deb224471.md)

[相关论文](%E5%9F%BA%E4%BA%8EServerless%E6%9E%B6%E6%9E%84%E7%9A%84%E5%88%86%E5%B8%83%E5%BC%8F%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F%207f1b4cdc23324eccb030b594ee7f6cfc/%E7%9B%B8%E5%85%B3%E8%AE%BA%E6%96%87%20e29edafc2e9e4c339d20bde77ef37784.md)

[参考文档](%E5%9F%BA%E4%BA%8EServerless%E6%9E%B6%E6%9E%84%E7%9A%84%E5%88%86%E5%B8%83%E5%BC%8F%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F%207f1b4cdc23324eccb030b594ee7f6cfc/%E5%8F%82%E8%80%83%E6%96%87%E6%A1%A3%206058ff6759154ea5a9018783b7eb814b.md)

---

## 概述

人工智能的迅速发展的背后是不断攀升的模型参数量，即便仅仅使用模型进行推理任务，也依然为主机带来很大的硬件门槛。

考虑到当前互联网产品需要快速、敏捷的人工智能应用，而Serverless作为云计算方兴未艾的服务模式，在需要使用神经网络模型的图片处理、目标识别等基本任务中，可以充分发挥其弹性伸缩、高可用的特性，最为重要的是，利用背后k8s的集群管理方案，可以有效进行神经网络在不同主机上的分布式推理任务，以此降低其硬件门槛。

于是我们希望构造一种系统——将现有神经网络模型自动化拆解、构建、封装为面向Serverless框架的一批镜像，在开源Severless框架中实施部署以完成神经网络的分布式推理。

## Serverless简介

Serverless是一种云计算服务模式，其基本思想是将应用程序的部署和管理从基础设施和操作系统中分离出来。使用Serverless，开发者可以专注于编写应用程序代码，而不必关心底层基础设施的管理。通常，Serverless平台会自动扩展和缩减应用程序的资源，使其具有高可用性和弹性。此外，Serverless也通常以按需付费的方式计费，使得开发者可以根据实际的资源使用情况来支付费用，而不必预先购买或租赁硬件设备。

---

## 详细子文档

[拆解模型](%E5%9F%BA%E4%BA%8EServerless%E6%9E%B6%E6%9E%84%E7%9A%84%E5%88%86%E5%B8%83%E5%BC%8F%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F%207f1b4cdc23324eccb030b594ee7f6cfc/%E6%8B%86%E8%A7%A3%E6%A8%A1%E5%9E%8B%20f5e72f222fd946e89c596fd8f52dfaa0.md)

[函数组织](%E5%9F%BA%E4%BA%8EServerless%E6%9E%B6%E6%9E%84%E7%9A%84%E5%88%86%E5%B8%83%E5%BC%8F%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F%207f1b4cdc23324eccb030b594ee7f6cfc/%E5%87%BD%E6%95%B0%E7%BB%84%E7%BB%87%20b5b1a548129941049ebc07f6b0ff7569.md)

---
