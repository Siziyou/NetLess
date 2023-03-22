# 基于 OpenFaaS 的函数服务实践 - 知乎

[https://zhuanlan.zhihu.com/p/400359861](https://zhuanlan.zhihu.com/p/400359861)

## 内容摘要

随着云计算的发展，业务系统的服务模型也在不断演变。本文主要是通过讲述团队在过去一段时间不断探索 BFF 开发模式的历程，分享我们在新的业务场景中通过 [OpenFaaS](https://link.zhihu.com/?target=https%3A//link.juejin.cn/%3Ftarget%3Dhttps%253A%252F%252Fwww.openfaas.com) 建设团队自有函数服务的实践经验以及底层原理。

## 背景

首先通过一张图来简要回顾一下云服务的几种模式。这里就不再赘述各个模式的概念，通过这张图我们可以清晰地看出从 IaaS 到 FaaS，开发者需要关心的东西是越来越少的，其本质就是在不断帮助我们减少运维成本、提高研发效率。

![%E5%9F%BA%E4%BA%8E%20OpenFaaS%20%E7%9A%84%E5%87%BD%E6%95%B0%E6%9C%8D%E5%8A%A1%E5%AE%9E%E8%B7%B5%20-%20%E7%9F%A5%E4%B9%8E%20afbb472ea45f4b63aea6b59ca16ecebf/v2-fc00a30c149b4e9f1b17fd6e0218f0ec_720w.webp](%E5%9F%BA%E4%BA%8E%20OpenFaaS%20%E7%9A%84%E5%87%BD%E6%95%B0%E6%9C%8D%E5%8A%A1%E5%AE%9E%E8%B7%B5%20-%20%E7%9F%A5%E4%B9%8E%20afbb472ea45f4b63aea6b59ca16ecebf/v2-fc00a30c149b4e9f1b17fd6e0218f0ec_720w.webp)

目前虽然团队很多业务服务仍然是基于 IaaS 部署的，但是我们也在逐步跟随时代潮流去实践新的开发模式。下面先简单介绍一下团队在不同阶段所采用的一些技术方案。

### 前后端分离

几年前，在业务高速发展时期，部门为了提升前后端的合作效率，决定由前端团队接手 Java Web 应用，负责接口聚合、模板渲染等工作，而几个后端团队则专注于业务流程及数据处理，并提供 RPC 服务。前端当时虽然对应用代码进行了重构，但部署方式仍然是沿用了原有模式，通过 CentOS 虚拟机自行搭建服务器，在不同机房一共部署了 8 台 8U16G 的虚拟机。
不支持在 Docs 外粘贴 block
 这种方式相比传统模式还是有很大优点的，团队分工明确，前端接口和展现可以自给自足。缺点是对前端同学来说，运维成本直线上升，在上线、回滚、扩容、迁移等环节均需要人工介入，耗时耗力。这个阶段的关键词可以概括为：虚拟机、人工运维。

### 微服务

随着业务的快速发展，后端逐步演变为微服务架构。而前端的 Java BFF 应用则逐渐膨胀为一个庞大的单体应用，接口和页面的数量多达几百个，迫切需要一种更为灵活高效的开发模式。

![%E5%9F%BA%E4%BA%8E%20OpenFaaS%20%E7%9A%84%E5%87%BD%E6%95%B0%E6%9C%8D%E5%8A%A1%E5%AE%9E%E8%B7%B5%20-%20%E7%9F%A5%E4%B9%8E%20afbb472ea45f4b63aea6b59ca16ecebf/v2-8266799f7729b7fca06a35994f1b5d2f_720w.webp](%E5%9F%BA%E4%BA%8E%20OpenFaaS%20%E7%9A%84%E5%87%BD%E6%95%B0%E6%9C%8D%E5%8A%A1%E5%AE%9E%E8%B7%B5%20-%20%E7%9F%A5%E4%B9%8E%20afbb472ea45f4b63aea6b59ca16ecebf/v2-8266799f7729b7fca06a35994f1b5d2f_720w.webp)

经过一段时间的探索，我们基于业界的一些技术理念及最佳实践，将原有的 Java BFF 逐步改造成了 Node.js + Docker 的研发模式。后续又将 Web 应用拆分为多个微前端子应用，从而大大降低了系统的复杂性和耦合度。

目前这种方式是线上运行的主要模式，在开发效率和运维成本上都能够基本满足团队的需求。这个阶段的关键词可以概括为：微服务、容器。

### 云原生

随着云技术的发展，像 K8S、Service Mesh、Serverless、FaaS 等技术概念开始出现在我们视野中，弹性扩缩容、低运维成本等特性对现有的开发模式带了新的冲击。
 由于公司基础设施还在逐步建设中，因此前端团队开始自行探索 Serverless 模式在业务落地的可行性。经过调研对比 OpenFaaS、KNative、OpenWhisk 等开源框架后，最终我们决定采用 OpenFaaS 在公司提供的 K8S 集群上搭建自己的函数服务，随后在工具服务、小程序接口、周边业务接口等多个场景进行了实践。
 不支持在 Docs 外粘贴 block
 虽然短期维护 OpenFaaS 确实需要一定人力成本，但是灵活的开发模式也大大提高了团队迭代的效率。而且后续也可以逐步迁移至公司建设的 FaaS 平台上。
 函数服务实践
 下面分享一下我们在搭建及实践 OpenFaaS 服务的一些经验。
 搭建 OpenFaaS 服务
 核心的前置依赖就是需要有一个 K8S 集群 + 私有 Docker 镜像仓库。得益于 K8S 的 Helm 包管理工具，搭建的步骤跟 `npm install` 一样简单，当然各种配置过程中踩坑是不可避免的，需要自行解决。下图是安装成功后，OpenFaaS 运行的核心服务及容器实例。

### 业务实践

实际业务开发中，只需要安装 OpenFaaS [官方](https://link.zhihu.com/?target=https%3A//link.juejin.cn/%3Ftarget%3Dhttps%253A%252F%252Fgithub.com%252Fopenfaas%252Ffaas-cli) [CLI 工具](https://link.zhihu.com/?target=https%3A//link.juejin.cn/%3Ftarget%3Dhttps%253A%252F%252Fgithub.com%252Fopenfaas%252Ffaas-cli)，同时登录到公司内网 Docker Registry，就可以正式开发了。

官方支持 go/python/node 等语言模板，也支持任意自定义 Dockerfile，下面分享一下我们在项目中的实际应用。

**工具服务**

一般通用的工具型服务都可以通过直接引入开源的第三方库来快速实现，例如拼音转换、简繁转换等功能。下面的示例通过 3 行 python 代码快速实现了一个极简版的拼音转换函数：
 # handler.py import pinyin def handle(req): return pinyin.get(str(req), format="strip", delimiter=" ") 复制代码
 通过 CLI 发布之后，我们的服务就相当于完成了部署。省去了申请资源、安装依赖、配置服务等一系列过程。简单测试一下：

工具型的服务都比较离散，逻辑也比较简单。下面以小程序接口为例介绍一下业务模块的开发模式。

**小程序接口**

为了满足业务需求，我们基于公司 IM 快速开发了一个系统对应的小程序版本。由于功能不多，所需要的接口仅十余个，且核心业务逻辑与 Web 端相同。为了降本提效，我们放弃了 Nest BFF 的研发模式，转而采用多个函数的方式组织 API 服务。该服务的目录结构及描述文件大致如下：

```
mobile
├── functions
│   ├── notice                 # 通知接口
│   │   ├── handler.js
│   │   └── package.json
│   └── search                 # 搜索接口
│       ├── handler.js
│       └── package.json
└── mobile.yml
```

```
# file: mobile.yml

version: 1.0
provider:
  name: openfaas
  gateway: https://openfaas.demo.domain
functions:
  m-search:
    lang: node12
    handler: ./functions/search
    image: docker.demo.domain/mobile-search:latest
    secrets:
      - docker-auth
  m-notice:
    lang: node14
    handler: ./functions/notice
    image: docker.demo.domain/mobile-notice:latest
    secrets:
      - docker-auth
```

默认可以通过 CLI 批量发布，由于每个函数本质上是一个单独的镜像，因此是可以参数单独进行发布。

```
# 单独部署 Search 函数
faas up --filter "*search" -f mobile.yml
```

### 函数开发

函数代码的写法比较简洁，与大多数函数平台的开发模式相似，也可以根据需求安装第三方依赖。此外，为了满足开发测试的需求，一般第三方服务的 URL/Token 等信息都通过环境变量来指定。

```
const axios = require('axios');

// 通过环境变量指定 API 地址
const API_URL = process.env.API_URL;

module.exports = async (event, context) => {
  const { q } = event.query;
  const response = await axios.get(API_URL, {/* options */});

  /* process stuff */

  return context.status(200).succeed(data);
}
```

### 用户鉴权

由于小程序版本的接口需要开放公网访问，并且有单独的权限控制，我们的做法是将其封装为一个单独的 NPM 包，然后导出为一个高阶函数来完成鉴权操作。

```
const mobileAuth = require('@internal/mobile-auth');

const handler = async (event, context) => {
  const { user, token } = event.auth;

  /* process stuff */

  return context.status(200).succeed(data);
}

module.exports = mobileAuth(handler);
```

### 调用其他函数

实际业务场景中，函数之间也有互相调用的场景。在 OpenFaaS 中，可以直接通过内部网关 `gateway.openfaas` 进行调用。

```
const axios = require('axios');
const faas = axios.create({
  baseURL: 'http://gateway.openfaas:8080/function/'
});

module.exports = async (event, context) => {
  const { q } = event.query;
  const pinyin = await faas.post('/pinyin', /* data */);

  /* process stuff */

  return context.status(200).succeed(data);
}
```

## 底层原理分析

实践的过程也是一次很好的学习机会。下面我们简要介绍一下 OpenFaaS 的一些整体架构及底层原理。

### 整体技术栈

OpenFaas 整体框架底层基于 K8S 及 Docker，通过 Gateway 组件对外提供服务，同时集成了 Prometheus 及 NATS 等服务用于实现自动扩缩容等功能。平台层面，官方提供了 OpenFaaS Cloud 用于集成研发流程，可以对接至 Github/Gitlab 等代码托管平台。

### 抽象服务流程

上图是 OpenFaaS 的抽象服务流程，下面是各个节点的简单介绍：

- Gateway：HTTP 网关，用于接收用户请求及内部指令。
- NATS Streaming：用于异步执行函数。
- Prometheus / AlertManager：用于收集服务指标及扩缩容操作。
- faas-netes：针对 K8S 的 Provider，可以定制其他的 Provider 例如 Docker Swarm 等。
- Docker Registry：用于拉取函数镜像的仓库。

### 自动扩缩容

自动扩缩容是 FaaS 的核心特性。OpenFaaS 的扩容流程可以总结如下：

1. AlertManager 根据监控指标触发扩容动作；
2. Gateway 向 FaaS Netes 发起创建容器请求；
3. K8S 寻找合适的节点；
4. 拉取镜像；
5. 启动容器实例。

优化思路：

- 减少镜像大小。
- 在节点上预拉取镜像。
- 有规律的流量可以按照规则提前扩容。

```
# file: mobile.yml

functions:
  m-search:
    labels:
      com.openfaas.scale.min: 1
      com.openfaas.scale.max: 20
      com.openfaas.scale.factor: 20
      com.openfaas.scale.zero: false
```

## Watchdog

官方默认的函数模板中，每个容器实例中都有一个 Watchdog 进程，用于代理 Gateway 的请求，并将其转发给用户的函数进程。函数通过处理标准输入输出来响应请求。

## 函数运行时

由于一般开发的函数都用于 HTTP API，因此希望可以获取到更多的请求上下文。这时候也可以通过引入框架来解决问题。下面是通过 Express 框架来封装 Node.js 运行时的部分示例。
 首先是基础镜像，需要引入 watchdog，同时将 `mode` 改为 `http` 模式，同时指定函数入口文件及服务地址。

```
FROM Build software better, together as watchdog
FROM node:12-alpine as ship

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

# 省略部分配置...

COPY function/ ./

RUN npm i

WORKDIR /home/app/

ENV fprocess="node index.js"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:3000"

CMD ["fwatchdog"]
```

函数入口文件部分，我们需要新建一个 Express 应用，在接收到请求时，封装函数事件及上下文对象传递给用户代码执行。

```
const express = require('express');
const handler = require('./function/handler');  // 用户函数代码

const app = express();

// 函数事件
class FunctionEvent {
    constructor(req) {
        this.body = req.body;
        this.headers = req.headers;
        // ...
    }
}

// 函数上下文
class FunctionContext {
    constructor(cb) {
        this.statusValue = 200;
        this.cb = cb;
    }

    status(value) {}

    succeed(value) {}
}

// 构造中间件，执行用户代码
const middleware = async (req, res) => {
    const cb = (err, functionResult) => {
        // res.status().send()
    };

    const fnEvent = new FunctionEvent(req);
    const fnContext = new FunctionContext(cb);

    // handler(fnEvent, fnContext)
};

app.get('/*', middleware);

const port = process.env.http_port || 3000;

app.listen(port, () => {
    console.log(`listening on port: ${port}`)
});
```

## 总结

简单再回顾一下本文的内容。首先我们介绍了 BFF 应用研发模式的发展以及团队探索 OpenFaaS 的背景，然后讲述了团队在业务中的一些实践，最后简单介绍了 OpenFaaS 的一些底层原理。希望对大家有所帮助，感兴趣的同学可以留言讨论。
 最后再分享一下个人的一些看法。在 FaaS 基础设施逐渐完善的情况下，虽然开发运维的效率有所提升，但是业务的复杂度并没有降低，因此怎么构建抽象灵活的 BaaS 服务也是一个非常值得思考的方向。例如我们想快速构建一个视频在线服务，理想的状态就是能够直接通过 FaaS 函数把用户、文件存储、视频转码、数据库等 BaaS 服务串联起来，完全不需要关心服务端的细节，专注于业务流程的封装。

作者：杨鹏飞

[%E5%9F%BA%E4%BA%8E%20OpenFaaS%20%E7%9A%84%E5%87%BD%E6%95%B0%E6%9C%8D%E5%8A%A1%E5%AE%9E%E8%B7%B5%20-%20%E7%9F%A5%E4%B9%8E%20afbb472ea45f4b63aea6b59ca16ecebf/image](%E5%9F%BA%E4%BA%8E%20OpenFaaS%20%E7%9A%84%E5%87%BD%E6%95%B0%E6%9C%8D%E5%8A%A1%E5%AE%9E%E8%B7%B5%20-%20%E7%9F%A5%E4%B9%8E%20afbb472ea45f4b63aea6b59ca16ecebf/image)