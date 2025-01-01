# CloudNative



## 什么是云原生（Cloud Native）?



**云原生（Cloud Native）是一种设计理念和技术架构**，旨在充分利用云环境的优势，来开发、部署和管理**高效、弹性、可扩展和自动化的现代化应用程序**。

云原生的核心目标是让应用程序能够**动态调整资源**，实现**高可用性**、**高可扩展性**和**灵活性**。云原生的实现通常依赖于**容器化技术（如Docker）**、**编排系统（如Kubernetes）**、**微服务架构**和**持续交付/集成（CI/CD）**等技术。





## 云原生的核心思想



**松耦合的架构**

- 传统的“单体应用”与“云原生应用”最大的区别是，云原生应用通过**微服务**将每个模块独立部署、独立扩缩。
- 云原生应用**每个服务模块独立开发、独立测试、独立部署**，互不影响。

**声明式的API**

- 云原生使用**声明式API**（Declarative API）管理基础架构和服务。
- 例如，Kubernetes中的**YAML文件**就是声明式API的典型示例，用户只需要声明期望的状态，而不需要关心如何实现。

**自动化运维 (Self-Healing)**

- 云原生应用依赖**自动化监控和告警系统**。
- Kubernetes中的**重启策略、健康检查（health check）、就绪探针（readiness probe）**，都可以实现自动恢复和修复。
- 在容器失败、崩溃时，Kubernetes会**自动重建Pod**，无需人工干预。

**弹性和自适应能力**

- 云原生应用具备**自动扩容和缩容**的能力。
- 当流量激增时，Kubernetes可以在几秒钟内**自动扩展Pod数量**，当流量下降时，Pod数量会自动减少，降低成本。

**基础设施即代码 (IaC)**

- 云原生强调**一切基础设施和配置都要以代码的形式存在**，这使得环境的创建、变更和销毁都变得可自动化。
- 使用的工具有**Terraform**、**Ansible**、**Helm**等。

**可观测性**

- 在分布式系统中，必须确保系统的**日志（log）**、**指标（metrics）\**和\**追踪（tracing）**。
- 使用Prometheus、Grafana等工具，可以直观地了解云原生系统的运行状态，检测瓶颈和故障点。





## 云原生的四大技术基石



**容器化 (Containerization)**

- 容器是云原生的最核心技术，它提供了一个与操作系统隔离的运行环境，便于**跨平台部署**。
- **Docker** 和 **OCI 容器**（如containerd、Podman）等工具就是容器化的典型代表。
- **好处**：更快的启动、更高的资源利用率、环境一致性和高可移植性。

**动态编排 (Orchestration)**

- 容器化的应用需要一个调度器来管理这些容器的**自动部署、扩缩容和故障修复**。
- **Kubernetes**（K8s）就是这种调度器的代表。
- Kubernetes可以管理**多集群的多节点分布式服务**，以实现跨云平台的高可用部署。

**微服务架构 (Microservices)**

- 将原本的单体应用拆解成多个**可独立开发和部署的微服务**，这些微服务通过**API或消息队列**进行通信。
- 各微服务可以单独部署、扩容、回滚、升级，而不影响其他模块。

**持续交付和持续集成 (CI/CD)**

- **CI/CD**使得开发人员的代码变更能够被**自动化构建、测试和部署**。
- 使用的工具有**Jenkins**、**GitLab CI/CD** 和 **ArgoCD** 等。
- CI/CD流水线可在开发到生产的过程中进行**自动化验证、回滚和监控**。





## 云原生的关键技术栈



| **领域**       | **技术**             | **作用**                             |
| -------------- | -------------------- | ------------------------------------ |
| **容器化**     | Docker, Podman       | 提供标准的容器化运行环境             |
| **容器编排**   | Kubernetes (K8s)     | 管理和编排容器，提供扩缩容和自愈能力 |
| **微服务**     | Spring Boot, Istio   | 支持微服务架构                       |
| **CI/CD**      | Jenkins, GitLab CI   | 持续交付和持续集成                   |
| **监控与日志** | Prometheus, Grafana  | 监控、日志、告警系统                 |
| **网络管理**   | Calico, Flannel      | 容器网络                             |
| **服务网格**   | Istio, Linkerd       | 管理微服务的通信，提供可观察性       |
| **存储**       | Ceph, Rook, Longhorn | 提供云原生的分布式存储解决方案       |
| **配置管理**   | Helm, Ansible        | 管理应用和集群的配置                 |

------





## 云原生的实际场景



1. **电商大促销**
   - 促销活动流量高峰，使用Kubernetes的**HPA（水平自动扩展）**来动态扩展服务实例。
   - 日常流量低时，Pod数量减少，**节省计算资源**。
2. **金融支付系统**
   - **微服务架构**可将支付系统拆分为多个服务：用户服务、支付服务、订单服务等。
   - **服务网格（如Istio）**实现微服务的流量治理、熔断、流量限流和分布式追踪。
3. **DevOps平台**
   - 使用**Jenkins + Docker + Kubernetes**，构建CI/CD流水线，自动化部署到生产环境。
   - **GitOps**使用**ArgoCD**，将代码提交到Git后，自动完成部署。





## 云原生的优势



| **优势**         | **描述**                                       |
| ---------------- | ---------------------------------------------- |
| **敏捷性**       | 通过CI/CD流水线实现快速的迭代发布              |
| **弹性扩展**     | 动态扩缩容，流量高峰期自动扩展，低峰期缩容     |
| **高可用性**     | 故障节点自动恢复，避免宕机                     |
| **多云/混合云**  | 支持跨云部署，避免单一云服务商的锁定           |
| **资源利用率高** | 使用容器化和Kubernetes的资源调度实现资源最优化 |



## 云原生官网

``````
https://www.cncf.io/
``````









# Docker







# CICD













# Prometheus







# 微服务





# Kubernetes



## Kubernets逻辑架构

![alt text](images/image15.png)



## Kubernetes组件



### Kubernetes组件间安全通信

![alt text](images/image28.png)



**Kubernetes集群中有三套CA机制**

- **etcd-ca**        ETCD集群内部的TLS通信
- **kubernetes-ca**    Kubernetes集群内部节点间的双向TLS通信
- **front-proxy-ca**    Kubernetes集群与外部扩展服务简单双向TLS通信





#### 详解Kubernetes-ca



**用途**：Kubernetes 集群内部的双向 TLS 通信



**作用和场景**

- **kubernetes-ca** 是 Kubernetes 集群的**主CA**，为**集群核心组件的内部双向通信**提供 TLS 证书。
- 它确保**集群中的各个核心组件之间的双向 TLS 通信是安全的**。
- 组件通过 **kubernetes-ca** 签发的证书来**验证彼此的身份**，并且**所有的通信内容都会加密**。
- 主要用于**Kubernetes 控制平面组件、工作节点和客户端**之间的通信。



**主要受控的组件和通信场景**

| **通信组件1**      | **通信组件2**               | **使用的证书**        | **使用的CA**      |
| ------------------ | --------------------------- | --------------------- | ----------------- |
| **kube-apiserver** | **kubelet**                 | kubelet-client.crt    | **kubernetes-ca** |
| **kube-apiserver** | **kube-scheduler**          | scheduler-client.crt  | **kubernetes-ca** |
| **kube-apiserver** | **kube-controller-manager** | controller-client.crt | **kubernetes-ca** |
| **kube-apiserver** | **kubectl客户端**           | kubectl.crt           | **kubernetes-ca** |
| **kube-apiserver** | **etcd**                    | etcd-client.crt       | **kubernetes-ca** |
| **kube-apiserver** | **service-account token**   | service-account.crt   | **kubernetes-ca** |
| **kubelet**        | **kube-apiserver**          | kubelet-server.crt    | **kubernetes-ca** |
| **kube-proxy**     | **kube-apiserver**          | kube-proxy-client.crt | **kubernetes-ca** |

> **示例解释：**

- **kube-apiserver 和 kubelet 之间的通信**：

  - kube-apiserver 需要使用客户端证书（`kubelet-client.crt`）通过双向TLS通信访问工作节点的 kubelet API。
  - kubelet 也会使用服务器证书（`kubelet-server.crt`）来确认自己的身份。
  - 这些证书都由 **kubernetes-ca** 签发。

- **kubectl 和 kube-apiserver 的通信**：

  - 用户的 kubectl 命令行工具通过 TLS 连接到 kube-apiserver，**kubectl** 使用的客户端证书（或 KubeConfig 文件）由**kubernetes-ca** 签发。
  - 这确保了**kubectl 的用户身份验证**和**与 API Server 的通信加密**。

  

**典型证书**

- **kubernetes-ca.crt**：根 CA 证书，所有的子证书都由它签发。
- **kube-apiserver.crt**：kube-apiserver 的服务器证书。
- **kube-apiserver-key.pem**：kube-apiserver 证书的私钥。
- **kubelet.crt** 和 **kubelet-key.pem**：kubelet 服务器证书和私钥。
- **kube-controller-manager.crt**：controller manager 使用的客户端证书。
- **kube-scheduler.crt**：scheduler 使用的客户端证书。
- **kube-proxy.crt**：kube-proxy 组件的客户端证书。



####  Front-proxy-ca

**用途：**用于 Kubernetes 的 API 聚合层的 TLS 通信



**作用和场景**

- **front-proxy-ca** 是为了支持**Kubernetes的API聚合层**，确保聚合层组件（如`metrics-server`和`custom-apis`）的通信安全。
- 它的主要目的是**为API代理和扩展API服务器（如Aggregator Server）之间的双向通信提供TLS加密和身份验证**。
- 这使得外部的 API 可以无缝地集成到Kubernetes API中。

> **API 聚合层的场景：**

- **metrics-server** 是一个常见的示例。
- 用户调用 `kubectl top nodes` 命令，kube-apiserver 需要**转发请求到metrics-server**。
- 这时，kube-apiserver 会使用**front-proxy-client.crt** 与**metrics-server**通信，确保数据是加密的，并能**验证metrics-server的身份**。





**主要受控的组件和通信场景**

| **通信组件1**      | **通信组件2**          | **使用的证书**         | **使用的CA**       |
| ------------------ | ---------------------- | ---------------------- | ------------------ |
| **kube-apiserver** | **API聚合层**          | front-proxy-client.crt | **front-proxy-ca** |
| **kube-apiserver** | **metrics-server**     | metrics-server.crt     | **front-proxy-ca** |
| **kube-apiserver** | **Custom API Service** | custom-api.crt         | **front-proxy-ca** |

> **示例解释：**

- **kube-apiserver 和 metrics-server 的通信**：
  - kube-apiserver 通过 TLS 请求 metrics-server。
  - metrics-server 使用**front-proxy-ca** 颁发的证书（如`metrics-server.crt`）来验证自己的身份。
  - **kube-apiserver 也会使用`front-proxy-client.crt` 进行认证和通信**。
- **kube-apiserver 和 Custom API Service 的通信**：
  - 用户可能会在集群中部署一个**自定义 API 扩展**。
  - 这时，kube-apiserver 使用**front-proxy-client.crt** 连接到**Aggregator Server**，并通过TLS通信与扩展API服务通信。





**典型证书**

- **front-proxy-ca.crt**：前端代理CA的根证书。
- **front-proxy-client.crt**：kube-apiserver 连接 API 聚合层（如 metrics-server）的证书。
- **front-proxy-client-key.pem**：kube-apiserver 使用的前端代理的私钥。



#### API聚合器是什么？

API 聚合器是 **kube-apiserver 的一个逻辑组件**，它的主要职责是：

- **将第三方 API 服务和 Kubernetes 自身的 API 进行聚合**。
- **统一暴露 API 端点**，使客户端（例如 `kubectl`）可以像操作原生资源（如Pod、Service）一样操作自定义的 API 资源。
- 通过 `kubectl get`、`kubectl describe` 等命令管理这些**非原生资源**。
- **将多个 API 扩展的路径挂载到 kube-apiserver** 的 URL 结构中，通常路径是 `/apis/{API_GROUP}/{VERSION}/{RESOURCE}`。





**API聚合器的位置和作用**

在 Kubernetes 架构中，API 聚合器是**kube-apiserver的一部分**。如下图所示，API 聚合器与 kube-apiserver 是一体的。

```lua
+------------------------------------------------------+
|                   kube-apiserver                     |
|                                                      |
|   +----------------+  +---------------------------+  |
|   | 原生 API 资源  |  |   自定义 API 聚合层      |  |
|   | (pods, svc)    |  | (metrics-server, custom)  |  |
|   +----------------+  +---------------------------+  |
|                                                      |
+------------------------------------------------------+
                          |
                          |
         +------------------------------------+
         |           API 聚合器                |
         +------------------------------------+
                          |
                          |
         +----------------+      +------------------+
         | 外部 API 服务   |      | 自定义API服务    |
         +----------------+      +------------------+
```

------

**具体的工作流程**

1. **请求的发起**：客户端（如 `kubectl top nodes`）发起 API 请求，路径为 `/apis/metrics.k8s.io/v1beta1/nodes`。
2. **kube-apiserver 路由**：kube-apiserver 识别到 `/apis/metrics.k8s.io/` 是**自定义API路径**，于是将请求转发到**API聚合器**。
3. API聚合器工作：
   - API聚合器通过**front-proxy-client.crt** 证书与**外部的扩展API服务器**通信。
   - 将请求转发到**扩展API服务**，如**metrics-server**。
4. 数据返回：
   - 扩展 API 服务（如 metrics-server）处理请求，并返回**监控数据**。
   - API 聚合器将数据返回给 kube-apiserver，最终返回给 `kubectl`。





## Kubernetes 版本

**通常每年更新四个大版本,从v1.22后已经修改为每年发布3个大版本** 

Kubernetes 的版本以 X.Y.Z 模式命名，其中 X 是主版本号，Y 是小版本号，Z 是补丁版本号。

 Kubernetes 一次支持三个小版本，也就是只支持包含当前的发布版本和两个之前的版本。 

参阅 GitHub 上的  Kubernetes Release 页面以获取最新的发布信息。





## Kubernetes扩展接口
![alt text](images/image16.png)



Kubernetes提供了三个特定功能的接口,kubernetes通过调用这几个接口，来完成相应的功能。

- **容器运行时接口CRI**: Container Runtime Interface 

  - CRI 首次发布于2016年12月的Kubernetes 1.5 版本。 

  - 在此版本之前，Kubernetes 直接与 Docker 通信，没有标准化的接口。 

  - 从 Kubernetes 1.5 开始，CRI 成为 Kubernetes 与容器运行时交互的标准接口，使得 Kubernetes  可以与各种容器运行时进行通信，从而增加了灵活性和可移植性。

  - kubernetes 对于容器的解决方案，只是预留了容器接口，只要符合CRI标准的解决方案都可以使用

![alt text](images/image17.png)
![alt text](images/image18.png)



#### 扩展：dockershim 是什么，为什么它会消失

``````
在 Kubernetes 的早期，我们只支持一个容器运行时。那个运行时是 Docker Engine。当时，没有太多其他选择，Docker 是处理容器的主要工具，所以这不是个有争议的选择。最终，我们开始添加更多的容器运行时，比如 rkt 和 hypernetes，很明显 Kubernetes 用户希望选择最适合他们的运行时。因此 Kubernetes 需要种方法，来允许集群操作者灵活地使用他们选择的任何运行时。

发布CRI[1]（Container Runtime Interface，容器运行时接口）就是为了提供这种灵活性。CRI 的引入对项目和用户来说都很棒，但它也引入了一个问题：Docker Engine 作为容器运行时的使用早于 CRI，Docker Engine 与 CRI 不兼容。为了解决这个问题，引入了一个小软件垫片（"shim"，dockershim）作为 kubelet 组件的一部分，专门用于填补 Docker Engine 和 CRI 之间的空白，允许集群运营商继续使用 Docker Engine 作为他们的容器运行时，基本上不会给中断。

然而，这个小小的软件垫片从来就不是永久的解决方案。多年来，它的存在给 kubelet 本身带来了许多不必要的复杂性。由于这个垫片，Docker 的一些集成实现不一致，导致维护人员的负担增加，并且维护特定于供应商的代码不符合我们的开源理念。为了减少这种维护负担，并向一个支持开放标准的更具协作性的社区发展，KEP-2221 获引入[2]，它建议去掉 dockershim。随着 Kubernetes v1.20 的发布，这一弃用成为
正式。

我们没有很好地传达这一点，不幸的是，弃用声明导致了社区内的一些恐慌。对于 Docker 作为一家公司来说这意味着什么，由 Docker 构建的容器镜像能否运行，以及 Docker Engine 实际是什么导致了社交媒体上的一场大火。这是我们的过失；我们应该更清楚地沟通当时发生了什么以及原因。为了解决这个问题，我们发布了一个博客[3]和相关的常见问题[4]，以减轻社区的恐惧，并纠正一些关于 Docker 是什么，以及容
器如何在 Kubernetes 中工作的误解。由于社区的关注，Docker 和 Mirantis 共同同意以cridocker[5]的形式继续支持 dockershim 代码，允许你在需要时继续使用 Docker Engine 作为你的容器运行时。为了让那些想尝试其他运行时（如 containerd 或 cri-o）的用户感兴趣，编写了迁移文档[6]。

我们后来对社区进行了调查[7]，发现仍然有许多用户有问题和顾虑[8]。作为回应，Kubernetes 维护者和CNCF 致力于通过扩展文档和其他程序来解决这些问题。事实上，这篇博文就是这个计划的一部分。随着如此多的最终用户成功地迁移到其他运行时，以及文档的改进，我们相信现在每个人都有了迁移的道路

无论是作为工具还是作为公司，Docker 都不会消失。它是云原生社区和 Kubernetes 项目历史的重要组成部分。没有他们我们不会有今天。也就是说，从 kubelet 中移除 dockershim 最终对社区、生态系统、项目和整个开源都有好处。这是我们所有人一起支持开放标准的机会，我们很高兴在 Docker 和社区的帮助下这样做。
``````



- 方式1: Containerd 
  - 默认情况下,Kubernetes在创建集群的时候,使用的就是Containerd 方式。 
- 方式2: Docker 
  - Docker Engine 没有实现 CRI， 而这是容器运行时在 Kubernetes 中工作所需要的。  因此必须安装一个额外的服务,早期使用由k8s提供的dockershim,但它在 1.24 版本从 kubelet 中被 移除 还可以借助于Mirantis维护的cri-dockerd插件方式来实现Kubernetes集群的创建。 cri-dockerd 项目站点:  https://github.com/Mirantis/cri-dockerd 
- 方式3: CRI-O 
  - 2016年成立,2019年4月8号加入CNCF孵化。 CRI-O的方式是Kubernetes创建容器最直接的一种方式 在创建集群的时候,需要借助于cri-o插件的方式来实现Kubernetes集群的创建。

![alt text](images/image19.png)
![alt text](images/image20.png)


- **容器网络接口CN**I: Container Network Interface
  - kubernetes 对于网络的解决方案，只是预留了网络接口，只要符合CNI标准的解决方案都可以使用
- **容器存储接口CSI:** Container Storage Interface
  - kubernetes 对于存储的解决方案，只是预留了存储接口，只要符合CSI标准的解决方案都可以使用 此接口非必须





## Kubernetes集群部署



### Kubernetes 集群组件运行模式

#### **独立组件模式** 

- 各关键组件都以二进制方式部署于主机节点上，并以守护进程形式运行 
- 各附件Add-ons 则以Pod形式运行 
- 需要实现各种证书的申请颁发
-  部署过程繁琐复杂

![alt text](images/image21.png)



#### **静态Pod模式**

- **kubelet和容器运行时docker以二进制部署，运行为守护进程**
- 除此之外所有组件为Pod 方式运行

- 控制平台各组件以静态Pod对象运行于Master主机之上
- 静态Pod由kubelet所控制实现创建管理,而无需依赖kube-apiserver等控制平台组件
- kube-proxy等则以Pod形式运行
- 相关pod早期是从仓库k8s.gcr.io下载镜像，新版改为仓库registry.k8s.io
- 使用kubernetes官方提供的kubeadm工具实现kubernetes集群方便快速的部署

![alt text](images/image22.png)



### 基于Kubeadm和 Docker 部署 kubernetes 高可用集群


![alt text](images/image23.png)


参考文档：

``````
https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
https://github.com/kubernetes/kubeadm/blob/master/docs/design/design_v1.10.md
``````



kubeadm是Kubernetes社区提供的集群构建工具

- 负责执行构建一个最小化可用集群并将其启动等必要的基本步骤
- Kubernetes集群全生命周期管理工具，可用于实现集群的部署、升级/降级及卸载等
- kubeadm仅关心如何初始化并拉起一个集群，其职责仅限于下图中背景蓝色的部分
- 蓝色的部分以外的其它组件还需要自行部署 

![alt text](images/image24.png)

注意：在kubeadm方式安装时，Kubernetes 的所有组件中除kubelet 是以传统服务进程的方式运行，其它都以容器运行



#### 部署环境说明

![alt text](images/image25.png)



| IP         | 主机名           | 角色                                      |
| ---------- | ---------------- | ----------------------------------------- |
| 10.0.0.101 | master1.wang.org | K8s 集群主节点 1，Master和etcd            |
| 10.0.0.102 | master2.wang.org | K8s 集群主节点 2，Master和etcd            |
| 10.0.0.103 | master3.wang.org | K8s 集群主节点 3，Master和etcd            |
| 10.0.0.104 | node1.wang.org   | K8s 集群工作节点 1                        |
| 10.0.0.105 | node2.wang.org   | K8s 集群工作节点 2                        |
| 10.0.0.106 | node3.wang.org   | K8s 集群工作节点 3                        |
| 10.0.0.107 | ha1.wang.org     | K8s 主节点访问入口 1,提供高可用及负载均衡 |
| 10.0.0.108 | ha2.wang.org     | K8s 主节点访问入口 2,提供高可用及负载均衡 |
| 10.0.0.109 | harbor.wang.org  | 容器镜像仓库                              |
| 10.0.0.100 | kubeapi.wang.org | VIP，在ha1和ha2主机实现                   |

注意： Master节点内存至少2G以上，否则在初始化时会出错



#### 网络地址规划

``````bash
物理主机网络        10.0.0.0/24 
集群pod网络        --pod-network-cidr=10.244.0.0/16
应用service网络    --service-cidr=10.96.0.0/12 
``````

![alt text](images/image26.png)



#### 基于 kubeadm 和 Docker 实现Kuberenetes集群流程说明

- 每个节点主机的初始环境准备
- 准备代理服务,以便访问k8s.gcr.io，或根据部署过程提示的方法获取相应的I国内镜像的image（可选）
- Kubernetes集群API访问入口的高可用和harbor（可选）
- **在所有Master和Node节点都安装容器运行时 Docker**
- **在所有节点安装和配置 cri-dockerd(kubernetes-v1.24版本以后需要)**
- **在所有Master和Node节点都安装kubeadm 、kubelet、kubectl(集群管理工具,在node节点可 不安装)**
- **在第一个 master 节点运行 kubeadm init 初始化命令 ,并验证 master 节点状态**
- **在第一个 master 节点安装配置CNI规范的网络插件**
- 在其它master节点运行kubeadm join 命令加入到控制平面集群中实现高可用(测试环境可选)
- **在所有 node 节点使用 kubeadm join 命令加入集群 , 并验证 node 节点状态**
- 创建 pod 并启动容器测试访问 ，并测试网络通信



#### 初始环境准备

- 硬件准备环境: 每个主机至少2G以上内存,CPU2核以上
- 操作系统: 最小化安装支持Kubernetes的Linux系统
- 唯一的主机名，MAC地址以及product_uuid和主机名解析
- 保证各个节点网络配置正确,并且保证通信正常
- 禁用 swap 
- 禁用 SELinux
- 放行Kubernetes使用到的相关端口或禁用firewalld/iptables
- 配置正确的时区和时间同步
- 内核参数优化 
- 所有节点实现基于 ssh key 验证(可选)



**检查每台机器的product_uuid，project_uuid要具备唯一性**

``````bash
[root@ubuntu2204 ~]#cat /sys/class/dmi/id/product_uuid
e0c84d56-f33b-6754-eab2-d5e7cb846dc1
 
[root@rocky8 ~]#cat /sys/class/dmi/id/product_uuid
10324d56-9c12-c716-dfa1-196e5242b4d3
``````





**每天机器上设置hostname,并配置/etc/hosts**

``````
# cat >> /etc/hosts <<EOF
10.0.0.100 kubeapi kubeapi.wang.org 
10.0.0.101 master1 master1.wang.org
10.0.0.102 master2 master2.wang.org
10.0.0.103 master3 master3.wang.org
10.0.0.104 node1 node1.wang.org
10.0.0.105 node2 node2.wang.org
10.0.0.106 node3 node3.wang.org
10.0.0.107 ha1 ha1.wang.org
10.0.0.108 ha2 ha2.wang.org
10.0.0.109 harbor harbor.wang.org
EOF
``````



**使用ssh打通每台机器**

``````bash
ssh-keygen

ssh-copy-id 127.0.0.1

for i in {101..108}; do scp -r .ssh 10.0.0.$i:/root/; done
``````



**设置每台主机的主机名**

``````bash
for i in {1..3} ;do ssh 10.0.0.10$i hostnamectl set-hostname master$i;done
for i in {4..6} ;do ssh 10.0.0.10$i hostnamectl set-hostname node$(($i-3));done
ssh 10.0.0.107 hostnamectl set-hostname ha1
ssh 10.0.0.108 hostnamectl set-hostname ha2

``````



**实现主机时间同步**

``````bash
timedatectl set-timezone Asia/Shanghai

apt update
apt install  chrony -y

vim /etc/chrony/chrony.conf
 #加下面一行
pool ntp.aliyun.com        iburst maxsources 2
pool ntp.ubuntu.com        iburst maxsources 4
pool 0.ubuntu.pool.ntp.org iburst maxsources 1
pool 1.ubuntu.pool.ntp.org iburst maxsources 1
pool 2.ubuntu.pool.ntp.org iburst maxsources 2

systemctl enable chrony
systemctl restart chrony
``````



 **关闭SELinux**

``````bash
 ~# setenforce 0
 ~# sed -i 's#^\(SELINUX=\).*#\1disabled#' /etc/sysconfig/selinux
``````



**关闭防火墙**

``````bash
# Rocky
systemctl disable --now firewalld 

# Ubuntu
systemctl disable --now ufw
``````



 **禁用 Swap 设备**

``````bash
#方法1
~# swapoff -a
~# sed -i  '/swap/s/^/#/' /etc/fstab
~# for i in {101..106};do ssh 10.0.0.$i "sed -i  '/swap/s/^/#/' /etc/fstab"; ssh 10.0.0.$i swapoff -a ; done

#方法2
~# systemctl stop  swap.img.swap
~# systemctl mask swap.img.swap 或者 systemctl mask swap.target
 
#方法3
~# systemctl mask swap.img.swap 或者 systemctl mask swap.target
~# reboot

#确认是否禁用swap
~# systemctl -t swap 
~# swapon -s 

``````



**内核优化**  

根据硬件和业务需求,对内核参数做相应的优化 

注意:安装docker时会自动修改内核参数





#### 实现高可用的反向代理



**实现 keepalived**

在两台主机ha1和ha2 按下面步骤部署和配置 keepalived

``````bash
[root@ha1 ~]#apt update && apt -y install keepalived 

#keepalived配置
[root@ha1 ~]#cp  /usr/share/doc/keepalived/samples/keepalived.conf.vrrp /etc/keepalived/keepalived.conf

[root@ha1 ~]#vim /etc/keepalived/keepalived.conf

! Configuration File for keepalived
global_defs {
  notification_email {
    acassen
  }
  notification_email_from Alexandre.Cassen@firewall.loc
  smtp_server 192.168.200.1
  smtp_connect_timeout 30
  router_id ha1.wang.org  #指定router_id,#在ha2上为ha2.wang.org
}
vrrp_script check_haproxy {
   script "/etc/keepalived/check_haproxy.sh"
   interval 1
   weight -30
   fall 3
   rise 2
   timeout 2
}
vrrp_instance VI_1 {
   state MASTER              #在ha2上为BACKUP        
   interface eth0
   garp_master_delay 10
   smtp_alert
   virtual_router_id 66      #指定虚拟路由器ID,ha1和ha2此值必须相同
   priority 100              #在ha2上为80          
   advert_int 1
   authentication {
       auth_type PASS
       auth_pass 123456      #指定验证密码,ha1和ha2此值必须相同  
   }
   virtual_ipaddress {
       10.0.0.100/24 dev eth0  label eth0:1  #指定VIP,ha1和ha2此值必须相同
   }
   track_script {
       check_haproxy 
   }
}
 [root@ha1 ~]#cat /etc/keepalived/check_haproxy.sh
 #!/bin/bash
 /usr/bin/killall -0 haproxy  || systemctl restart haproxy
 [root@ha1 ~]#chmod +x /etc/keepalived/check_haproxy.sh
 [root@ha1 ~]#hostname -I
 10.0.0.107 
[root@ha1 ~]#systemctl start keepalived.service 
#验证keepalived服务是否正常
``````





**实现 Haproxy**

通过 Harproxy 实现 kubernetes Api-server的四层反向代理和负载均衡功能

``````bash
#在两台主机ha1和ha2都执行下面操作
[root@ha1 ~]#cat >> /etc/sysctl.conf <<EOF
net.ipv4.ip_nonlocal_bind = 1
EOF
root@ha1 ~]#sysctl -p 

#安装配置haproxy
[root@ha1 ~]#apt -y install haproxy
[root@ha1 ~]#vim /etc/haproxy/haproxy.cfg 
[root@ha1 ~]#cat /etc/haproxy/haproxy.cfg

global
	log /dev/log	local0
	log /dev/log	local1 notice
	chroot /var/lib/haproxy
	stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
	stats timeout 30s
	user haproxy
	group haproxy
	daemon

	# Default SSL material locations
	ca-base /etc/ssl/certs
	crt-base /etc/ssl/private

	# See: https://ssl-config.mozilla.org/#server=haproxy&server-version=2.0.3&config=intermediate
        ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
        ssl-default-bind-ciphersuites TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
        ssl-default-bind-options ssl-min-ver TLSv1.2 no-tls-tickets

defaults
	log	global
	mode	http
	option	httplog
	option	dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000
	errorfile 400 /etc/haproxy/errors/400.http
	errorfile 403 /etc/haproxy/errors/403.http
	errorfile 408 /etc/haproxy/errors/408.http
	errorfile 500 /etc/haproxy/errors/500.http
	errorfile 502 /etc/haproxy/errors/502.http
	errorfile 503 /etc/haproxy/errors/503.http
	errorfile 504 /etc/haproxy/errors/504.http

##########添加以下内容######################

listen stats
    mode http
    bind 0.0.0.0:8888
    stats enable
    log global
    stats uri /status
    stats auth admin:123456

listen  kubernetes-api-6443
    bind 10.0.0.100:6443
    mode tcp 
    server master1 10.0.0.101:6443 check inter 3s fall 3 rise 3 
    server master2 10.0.0.102:6443 check inter 3s fall 3 rise 3 
    server master3 10.0.0.103:6443 check inter 3s fall 3 rise 3 
``````



浏览器访问： http://ha2.wang.org:8888/status ，可以看到下面界面


![alt text](images/image27.png)



#### 在master和worker上安装docker

``````bash
# master
wget https://www.mysticalrecluse.com/script/Shell/install_docker_offline.sh
bash install_docker_offline.sh
``````



####  所有主机安装 cri-dockerd(v1.24以后版本)

```````bash
wget https://github.com/Mirantis/cri-dockerd/releases/download/v0.3.14/cri-dockerd_0.3.14.3-0.ubuntu-jammy_amd64.deb

# 如果出现依赖问题，使用该命令修复
apt --fix-broken install -y

# 如果出现如下报错
[root@ubuntu2204 ~]#systemctl status cri-docker.service 
○ cri-docker.service - CRI Interface for Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/cri-docker.service; enabled; vendor preset: enabled)
     Active: inactive (dead)
TriggeredBy: × cri-docker.socket
       Docs: https://docs.mirantis.com

12月 15 16:23:19 master2 systemd[1]: Dependency failed for CRI Interface for Docker Application Container Engine.
12月 15 16:23:19 master2 systemd[1]: cri-docker.service: Job cri-docker.service/start failed with result 'dependency'.

# 解决方法：添加docker组
groupadd docker

# 重启cri-docker
systemctl restart cri-docker.service
systemctl status cri-docker.service
```````





#### 所有主机配置 cri-dockerd(v1.24以后版本

``````bash
# vim /lib/systemd/system/cri-docker.service
ExecStart=/usr/bin/cri-dockerd --container-runtime-endpoint fd:// --pod-infra-container-image registry.aliyuncs.com/google_containers/pause:3.9
``````





#### 所有 master 和 node 节点安装kubeadm等相关包

所有 master 和 node 节点都安装kubeadm, kubelet,kubectl 相关包

注意: node节点可以不安装管理工具 kubectl 包,但依赖关系会自动安装



``````bash
# cat install_k8s.sh
#!/bin/bash
apt update && apt-get install -y apt-transport-https
curl -fsSL https://mirrors.aliyun.com/kubernetes-new/core/stable/v1.30/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://mirrors.aliyun.com/kubernetes-new/core/stable/v1.30/deb/ /" | tee /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubelet kubeadm kubectl
``````





#### 在第一个 master 节点运行 kubeadm init 初始化命令

``````
K8S_RELEASE_VERSION=1.30.2 && kubeadm init --control-plane-endpoint kubeapi.wang.org --kubernetes-version=v${K8S_RELEASE_VERSION} --pod-network-cidr 10.244.0.0/16 --service-cidr 10.96.0.0/12 --image-repository registry.aliyuncs.com/google_containers --token-ttl=0 --upload-certs --cri-socket=unix:///run/cri-dockerd.sock
``````



**完整命令**

``````bash
K8S_RELEASE_VERSION=1.30.2 && kubeadm init --control-plane-endpoint master1.mystical.org --kubernetes-version=v${K8S_RELEASE_VERSION} --pod-network-cidr 10.244.0.0/16 --service-cidr 10.96.0.0/12 --image-repository registry.aliyuncs.com/google_containers --token-ttl=0 --upload-certs --cri-socket=unix:///run/cri-dockerd.sock
``````



**逐个字段的详细解释**

1️⃣ `K8S_RELEASE_VERSION=1.30.2`

- **含义**：定义一个环境变量 `K8S_RELEASE_VERSION`，用于指定 Kubernetes 版本。

- **作用**：在 `kubeadm init` 命令中，通过 `${K8S_RELEASE_VERSION}` 引用这个变量，简化版本控制，便于更新 Kubernetes 版本。

- 示例：

  ```
  bashCopy codeK8S_RELEASE_VERSION=1.30.2
  echo $K8S_RELEASE_VERSION  # 输出 1.30.2
  ```



2️⃣ **`kubeadm init`**

- **含义**：`kubeadm init` 命令用于初始化 Kubernetes 控制平面（Master 节点）。
- **作用**：该命令在控制节点上运行，初始化 Kubernetes 集群，生成 token、证书和 Kubeconfig 文件，并生成 `kubeadm join` 命令，以便其他节点加入集群。



3️⃣ **`--control-plane-endpoint kubeapi.wang.org`**

- **含义**：设置 Kubernetes 控制平面的**高可用入口地址**。
- 作用：
  - 如果你有多个 master 控制平面节点，需要为这些控制平面提供一个**统一的访问入口**。
  - 这个控制平面入口（`kubeapi.wang.org`）通常是一个 **VIP (虚拟IP)**，或者是一个可以负载均衡到多个控制平面节点的 FQDN。
  - 这样，Kubernetes 集群内的 kubelet 只需连接这个域名，**不需要知道具体的控制平面节点的 IP**。
- 示例：
  - 如果你有 3 台控制平面节点，`10.0.0.1, 10.0.0.2, 10.0.0.3`，那么你可以设置一个 VIP 例如 `10.0.0.100` 并将域名 `kubeapi.wang.org` 解析为 `10.0.0.100`。
  - 通过 **Keepalived** 和 **HAProxy**，可以将请求从 `10.0.0.100` 转发到 3 台控制平面节点中的任意一个。



4️⃣ **`--kubernetes-version=v${K8S_RELEASE_VERSION}`**

- **含义**：指定要安装的 Kubernetes 版本。

- **作用**：强制 kubeadm 使用特定版本的 Kubernetes 组件。

- 示例：

  ```bash
  --kubernetes-version=v1.30.2
  ```



5️⃣ **`--pod-network-cidr 10.244.0.0/16`**

- **含义**：设置 Pod 网络的 CIDR 地址段。
- 作用：
  - 在 Kubernetes 集群中，每个 Pod 都需要有一个唯一的 IP 地址。
  - `--pod-network-cidr` 指定了**Pod IP 地址段**。
  - 该 IP 地址段被 CNI（如 Flannel、Calico、Weave）使用，通常不与服务器的本地 IP 地址冲突。
- 注意事项：
  - Flannel 通常使用 `10.244.0.0/16`。
  - Calico 默认使用 `192.168.0.0/16`。
- 示例：
  - `--pod-network-cidr=10.244.0.0/16` 表示 Pod IP 地址的范围是 `10.244.0.0 - 10.244.255.255`。



6️⃣ **`--service-cidr 10.96.0.0/12`**

- **含义**：指定 Service 的虚拟 IP 地址段。

- 作用：

  - 在 Kubernetes 中，Service 是一种集群内的**虚拟 IP**，这些 IP 不与物理主机 IP 冲突。
  - 这个 IP 段由 kube-proxy 和 iptables 维护。

- 注意事项：

  - Service IP 只能在**集群内部访问**。
  - 通常不与物理网络 IP 段冲突。
  - 一般是 `10.96.0.0/12`，表示 `10.96.0.0 - 10.111.255.255` 这个范围。

- 示例：

  ```bash
  --service-cidr=10.96.0.0/12
  ```





7️⃣ **`--image-repository registry.aliyuncs.com/google_containers`**

- **含义**：指定 Kubernetes 组件镜像的拉取地址。

- 作用：

  - 由于国内无法直接访问 **Google 容器镜像仓库 (gcr.io)**，所以用阿里云的镜像源。
  - `registry.aliyuncs.com/google_containers` 是国内常用的镜像源，包含所有 Kubernetes 相关的镜像。

- 示例：

  ```bash
  --image-repository registry.aliyuncs.com/google_containers
  ```





8️⃣ **`--token-ttl=0`**

- **含义**：设置 kubeadm join 命令中 Token 的有效时间。

- 作用：

  - 默认的 token 过期时间是 24 小时。
  - 通过 `--token-ttl=0`，表示生成的 token**永不过期**。
  - 适用于长时间部署节点，或者需要一段时间内多次加入新节点的场景。

- 示例：

  ```bash
  --token-ttl=0
  ```





9️⃣ **`--upload-certs`**

- **含义**：将证书上传到集群中的控制平面节点。

- 作用：

  - 在高可用集群中，控制平面节点之间需要共享证书。
  - kubeadm 会将证书加密存储在 **Kubernetes Secret** 中。
  - 通过这个参数，**允许其他控制平面节点下载这些证书**。

- 示例：

  ```
  --upload-certs
  ```





🔟 **`--cri-socket=unix:///run/cri-dockerd.sock`**

- **含义**：指定 Kubelet 连接的 CRI（容器运行时接口）。

- 作用：

  - Kubernetes 支持多个 CRI，如 **containerd**、**cri-o** 和 **Docker**。
  - cri-dockerd 是一个专门的 Docker CRI 插件。
  - 此选项告诉 Kubernetes：**将 Kubelet 连接到 /run/cri-dockerd.sock**。

- 注意：

  - 如果未指定此选项，Kubelet 将尝试自动检测 CRI。
  - cri-dockerd 是用于从 Docker 转换到 Containerd 的临时解决方案。

- 示例：

  ```bash
  --cri-socket=unix:///run/cri-dockerd.sock
  ```





**总结**

| 选项                       | 含义                 | 示例                           |
| -------------------------- | -------------------- | ------------------------------ |
| `--control-plane-endpoint` | 控制平面的高可用入口 | `kubeapi.feng.org`             |
| `--kubernetes-version`     | 指定 Kubernetes 版本 | `v1.30.2`                      |
| `--pod-network-cidr`       | 指定 Pod IP 地址段   | `10.244.0.0/16`                |
| `--service-cidr`           | Service IP 地址段    | `10.96.0.0/12`                 |
| `--image-repository`       | 容器镜像仓库         | `registry.aliyuncs.com`        |
| `--token-ttl`              | kubeadm token 有效期 | `0` 表示永不过期               |
| `--upload-certs`           | 上传控制平面证书     | **启用证书共享**               |
| `--cri-socket`             | 容器运行时接口 (CRI) | `unix:///run/cri-dockerd.sock` |



如果运行出现问题，需要重置，执行如下命令

``````
kubeadm reset -f
``````



#### 将其他的master和worker主机加入集群



执行上述初始化命令后，得到如下结果

``````bash
############ 这部分是授权kubectl命令 #######################################################
o start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of the control-plane node running the following command on each as root:

############## 这部分是master节点加入集群的命令###############################

  kubeadm join kubeapi.wang.org:6443 --token jizd9o.tjfoyvdoisbklfi5 \
	--discovery-token-ca-cert-hash sha256:c27e15a7a39394b6d64e419b60df835f9dedb7b015a92c1d9285effa1fbea600 \
	--control-plane --certificate-key 9fa84696a800c6b995a9249972c1dd76735701e5ea2ae05191c9f612a0d1252c --cri-socket=unix:///run/cri-dockerd.sock # 后面追加 --cri-socket=unix:///run/cri-dockerd.sock

Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use
"kubeadm init phase upload-certs --upload-certs" to reload certs afterward.

Then you can join any number of worker nodes by running the following on each as root:

############## 这部分是worker节点加入集群的命令###############################

kubeadm join kubeapi.wang.org:6443 --token jizd9o.tjfoyvdoisbklfi5 \
	--discovery-token-ca-cert-hash sha256:c27e15a7a39394b6d64e419b60df835f9dedb7b015a92c1d9285effa1fbea600 --cri-socket=unix:///run/cri-dockerd.sock # 后面追加 --cri-socket=unix:///run/cri-dockerd.sock
``````



根据上述指令加master主机和其他worker主机加入集群



#### 安装网络插件flanny

``````bash
wget https://mirror.ghproxy.com/https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml

# 要确保docker可以拉取镜像，建议开代理
kubectl apply -f kube-flannel.yml
``````



#### 查看是否部署成功

``````bash
[root@ubuntu2204 ~]#kubectl get nodes
NAME      STATUS   ROLES           AGE   VERSION
master1   Ready    control-plane   97m   v1.30.8
master2   Ready    control-plane   94m   v1.30.8
master3   Ready    control-plane   93m   v1.30.8
node1     Ready    <none>          92m   v1.30.8
node2     Ready    <none>          92m   v1.30.8
node3     Ready    <none>          92m   v1.30.8

``````



#### 启用自动补全脚本

``````bash
# 临时补全命令
source <(kubectl completion bash)


# 用户永久补全，每次登录都生效
echo 'source <(kubectl completion bash)' >> ~/.bashrc
source ~/.bashrc
``````





## Kubernetes资源对象和Pod资源



**本章内容**

- **资源对象**
- **名称空间**
- **Pod资源**
- **Pod工作机制**



### 资源对象

#### Kubernetes常见资源对象

![alt text](images/image29.png)



#### Kubernetes中资源对象的分类



**独立存在的资源**

Kubernetes 系统将一切事物都称为资源对象, 相当于面向对象的思想 

有一些独立存在,即不依赖于其它对象存在的资源类型, Kubernetes 提供了单独的 API 资源，其**遵循  REST 风格**组织并管理这些资源对象

对这些API 资源类型支持使用标准的 HTTP 方法(POST,PUT,PATCH,DELETE 和 GET)对资源进行增、删、 改和查。



**不能独立存在的资源**

也有一些资源Kubernetes  中并没有提供对应独立的API资源类型,不能独立创建,需要依附其它资源的存 在, 比如: Label,emptyDir等



```ABAP
在 Kubernetes 系统中，资源代表了对象的集合，例如：Pod 资源可用于描述所有 Pod类型的对象。对 象实质是资源类型生成的实例。
```



 

**Kubernetes 的API  资源分为两种:**

- 内置API 资源: Kubernetes 安装后自身具有的自定义的API 资源: 
- 用户自定义的API,称为CRD(Custom Resource Definition),可以通过安装一些组件生成



**从资源的主要功能上Kubernetes 的资源对象分为**

- Workloads(工作负载)
- Service,LoadBalancing and Networking(服务发现和负载均衡)
- 存储和配置(Storage&Configuration)
- Cluster Admin(集群管理)
- Policies&Scheduling(策略和调度)
-  Metadata(元数据)



**K8S资源还可以按适用范围分为:名称空间级别、集群级别、元数据类型**

- **名称空间级别**
  - 仅在此名称中生效。举个例子，我们之前通过 kubeadm 去安装我们K8S 集群的时 候，他会默认把所有组件放到 kube-system 这个名称空间下去运行，然后我们可以通过命令 kubectl get pod 的时候会看到它获取不到，对应的我们系统一些 pod 的信息，原因是默认情况 下该命令什么都不加的话相当于是 kubectl get pod -n default ，但是我们的  K8S 本身组件他 是放在我们的 kube-system 名称空间下的，所有这种情况我们会发现，在  kube-system 名称空间 下的资源我们在其他名称空间中是看不见的。这就是典型的名称空间级别资源。



- **集群级别**
  - 比如、role 等等，这都是集群级别的资源，不管在什么名称空间下去定义，在其他的名 称空间下都能够看得到，其实他在定义的时候都没有去指定所谓的名称空间，也就意味着一旦经过 定义以后在全集群中都能够被可见以及调用，这种级别呢我们就把它集群级别下的名称空间，并且 把这种东西叫做集群级别的资源



- **元数据型**
  - 负责提供一种指标，源数据类型它不像我们的名称空间级别和集群级别，其实它也可以 归属在这两者之间，但是它又有自己的特点所以我们将他拿出来进行单独的分类。比如前面讲过的  HPA 他就是可以通过我们的 CPU 进行平滑扩展，他就是典型的源数据型。通过我们的指标进行操 作。



#### 资源及其在 API 中的组织形式

Kubernetes 利用标准的 **RESTful 术语**来描述其 API 概念

- **资源类型**：是指在 URL 中使用的名称，如 Pod、Namespace 和 Service 等，其 URL 格式 为"**/GROUP/VERSION/RESOURCE**"，示例：/apps/v1/deployment

- 所有资源类型都有一个对应的 JSON 表示格式：**kind(种类)**，在 K8s 中用户创建对象必须以 JSON格 式提交对象的配置信息
- 隶属于同一资源类型的对象组成的列表称为 **collection(集合)**，如 PodList
-   某种类型的单个实例称为**"resource"(资源)**或**"object"(对象)**，如运行的名为 pod-test 的 Pod 对象



**API群组**

Kubernetes 将 API 分割为多个逻辑组合，称为API 群组，不同的群组支持单独启用或禁用，并可以再次 分解。群组化管理的 API 使得其可以更轻松的进行扩展。当前 K8s 集群系统上的 API server 上的相关信 息可以使用 kubectl api-versions 获取。配置资源清单时会使用 API 群组

```bash
#显示API群组,结果格式为: GROUP_NAME/VERSOIN,同一个组可以有多版本并存
#GROUP_NAME：API群组名，如果省略表示属于core核心组
#VERSION:v1,经过验证的稳定版本，可以生产环境使用,如:apps/v1
#alpha:内测,可能包含错误，生产不建议使用
#beta: 公测，存在变动的可能或者潜在的问题，生产不建议使用,如:autoscaling/v2beta2
```

Kubernetes 的 API 以层级结构组织在一起

- Object：资源型对象，表现为 **http url中path**
- 非Object：非资源型对象，kubernetes特有，例如: /healthz



Object资源型对象对应的 API 群组可以归为以下两类：

- **核心群组(core group)：**

  -  在资源的配置信息 apiVersion 字段中引用时可以不用指定路径,如:"apiVersion: v1
  - **REST 路径为 /api/v1**

  ```bash
  # RESTful风格的URL格式 
  https://API_SERVER:HOST/api/v1/namespaces/<NS_NAME>/<RESOURCE_NANE>/<OBJECT_NAME>
  
  #default名称空间下的mypod的Pod资源，URL路径直接访问
  curl https://API_SERVER:HOST/api/vl/namespaces/default/pods/mypod
  ```

  扩展：**kubectl get --raw 作用详解**

  - **直接访问 Kubernetes API**

    - `kubectl get --raw` 不像 `kubectl get pods` 这样的命令会对数据做额外的处理
    - 它的效果和以下命令几乎一致：

    ```bash
    curl -k -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
      https://<API_SERVER>:6443/api/v1/namespaces/default/pods/myapp-7b94444f8d-66d4h
    ```

  - **返回的是完整的原始 JSON 格式的响应**

    - `kubectl get pods` 通常会输出表格数据：

    ```bash
    NAME                          READY   STATUS    RESTARTS   AGE
    myapp-7b94444f8d-66d4h        1/1     Running   0          10m
    ```

    - 但是 `kubectl get --raw` 返回的则是 **原始的 JSON 格式**，示例如下：

    ```json
    {
      "kind": "Pod",
      "apiVersion": "v1",
      "metadata": {
        "name": "myapp-7b94444f8d-66d4h",
        "namespace": "default",
        "uid": "12345678-1234-1234-1234-123456789abc",
        "creationTimestamp": "2024-12-15T10:00:00Z"
      },
      "spec": {
        "containers": [
          {
            "name": "myapp",
            "image": "nginx:1.26.0",
            "ports": [
              {
                "containerPort": 80,
                "protocol": "TCP"
              }
            ]
          }
        ]
      },
      "status": {
        "phase": "Running",
        "conditions": [
          {
            "type": "Initialized",
            "status": "True"
          },
          {
            "type": "Ready",
            "status": "True"
          },
          {
            "type": "ContainersReady",
            "status": "True"
          }
        ]
      }
    }
    
    ```

  - **常见使用场景**

    - **查看 Kubernetes 的所有API资源**

    ```bash
    kubectl get --raw="/apis"
    # 这会列出当前 Kubernetes 集群中可用的 API 版本和资源
    ```

    - **获取特定pod的详细信息**

    ```bash
    kubectl get --raw="/api/v1/namespaces/default/pods/myapp-7b94444f8d-66d4h"
    # 解释：返回这个 pod 的详细信息，比 kubectl get pod myapp-7b94444f8d-66d4h -o json 提供更多的API元数据信息。
    ```

    -  **获取 Kube-Proxy 的健康检查**

    ```bash
    kubectl get --raw="/healthz"
    # 返回字符串
    ```

    - **查看所有 Kubernetes 版本API**

    ```bash
    kubectl get --raw="/version"
    # 返回json数据
    ```

    - **访问 webhook 请求日志**

    ```bash
    kubectl get --raw="/logs"
    ```

- **命名的群组(named group)**

  - 即有名称的群组
  -  REST 路径为 `/apis/$GROUP_NAME/$VERSION` , 如 `/apis/apps/v1`

  ```bash
  https://API_SERVER:HOST/apis/GROUP_NANE/VERSION/namespaces/<NS_MTNE>/<RESOURCE_NAME>/<0B3ECT_NNE
  /apis/<GROUP_NAME>/<VERSION>/<NAMESPACE>/default/deployments/
  /apis/<GROUP_NAME>/<VERSION>/<NAMESPACE>/default/deployments/<PODNAME>
   
  #示例： 
  kubectl get --raw="/apis/apps/v1/namespaces/kube-system/deployments/coredns" | jq
  ```

  

#### 访问 Kubernetes REST API

```bash
# 这个TOKEN在后面学习创建SA的时候会学习如何得到
#TOKEN=$(echo ZXlKaGJHY2lw==|base64 -d)

#利用上面生成的TOEKN才能访问
curl -s  --cacert /etc/kubernetes/pki/ca.crt -H "Authorization: Bearer ${TOKEN}" https://kubeapi.wang.org:6443
```



#### 查看资源对象的命令

##### 查看资源类型

```bash
[root@ubuntu2204 ~]# kubectl api-resources 

NAME                                SHORTNAMES   APIVERSION                        NAMESPACED   KIND
bindings                                         v1                                true         Binding
componentstatuses                   cs           v1                                false        ComponentStatus
#configmaps                          cm           v1                                true         ConfigMap
#endpoints                           ep           v1                                true         Endpoints
events                              ev           v1                                true         Event
#limitranges                         limits       v1                                true         LimitRange
#namespaces                          ns           v1                                false        Namespace
#nodes                               no           v1                                false        Node
#persistentvolumeclaims              pvc          v1                                true         PersistentVolumeClaim
#persistentvolumes                   pv           v1                                false        PersistentVolume
#pods                                po           v1                                true         Pod
#podtemplates                                     v1                                true         PodTemplate
#replicationcontrollers              rc           v1                                true         ReplicationController
resourcequotas                      quota        v1                                true         ResourceQuota
#secrets                                          v1                                true         Secret
#serviceaccounts                     sa           v1                                true         ServiceAccount
#services                            svc          v1                                true         Service
mutatingwebhookconfigurations                    admissionregistration.k8s.io/v1   false        MutatingWebhookConfiguration
validatingadmissionpolicies                      admissionregistration.k8s.io/v1   false        ValidatingAdmissionPolicy
validatingadmissionpolicybindings                admissionregistration.k8s.io/v1   false        ValidatingAdmissionPolicyBinding
validatingwebhookconfigurations                  admissionregistration.k8s.io/v1   false        ValidatingWebhookConfiguration
customresourcedefinitions           crd,crds     apiextensions.k8s.io/v1           false        CustomResourceDefinition
apiservices                                      apiregistration.k8s.io/v1         false        APIService
controllerrevisions                              apps/v1                           true         ControllerRevision
#daemonsets                          ds           apps/v1                           true         DaemonSet
#deployments                         deploy       apps/v1                           true         Deployment
#replicasets                         rs           apps/v1                           true         ReplicaSet
#statefulsets                        sts          apps/v1                           true         StatefulSet
selfsubjectreviews                               authentication.k8s.io/v1          false        SelfSubjectReview
tokenreviews                                     authentication.k8s.io/v1          false        TokenReview
localsubjectaccessreviews                        authorization.k8s.io/v1           true         LocalSubjectAccessReview
selfsubjectaccessreviews                         authorization.k8s.io/v1           false        SelfSubjectAccessReview
selfsubjectrulesreviews                          authorization.k8s.io/v1           false        SelfSubjectRulesReview
subjectaccessreviews                             authorization.k8s.io/v1           false        SubjectAccessReview
horizontalpodautoscalers            hpa          autoscaling/v2                    true         HorizontalPodAutoscaler
#cronjobs                            cj           batch/v1                          true         CronJob
#jobs                                             batch/v1                          true         Job
certificatesigningrequests          csr          certificates.k8s.io/v1            false        CertificateSigningRequest
leases                                           coordination.k8s.io/v1            true         Lease
endpointslices                                   discovery.k8s.io/v1               true         EndpointSlice
events                              ev           events.k8s.io/v1                  true         Event
flowschemas                                      flowcontrol.apiserver.k8s.io/v1   false        FlowSchema
prioritylevelconfigurations                      flowcontrol.apiserver.k8s.io/v1   false        PriorityLevelConfiguration
ingressclasses                                   networking.k8s.io/v1              false        IngressClass
#ingresses                           ing          networking.k8s.io/v1              true         Ingress
networkpolicies                     netpol       networking.k8s.io/v1              true         NetworkPolicy
runtimeclasses                                   node.k8s.io/v1                    false        RuntimeClass
poddisruptionbudgets                pdb          policy/v1                         true         PodDisruptionBudget
#clusterrolebindings                              rbac.authorization.k8s.io/v1      false        #ClusterRoleBinding
#clusterroles                                     rbac.authorization.k8s.io/v1      false        ClusterRole
#rolebindings                                     rbac.authorization.k8s.io/v1      true         RoleBinding
#roles                                            rbac.authorization.k8s.io/v1      true         Role
priorityclasses                     pc           scheduling.k8s.io/v1              false        PriorityClass
csidrivers                                       storage.k8s.io/v1                 false        CSIDriver
csinodes                                         storage.k8s.io/v1                 false        CSINode
csistoragecapacities                             storage.k8s.io/v1                 true         CSIStorageCapacity
#storageclasses                      sc           storage.k8s.io/v1                 false        StorageClass
volumeattachments                                storage.k8s.io/v1                 false        VolumeAttachment
```



##### 查看所有资源

```bash
[root@ubuntu2204 ~]# kubectl get all -A

NAMESPACE      NAME                                  READY   STATUS    RESTARTS        AGE
default        pod/myapp-7b94444f8d-66d4h            1/1     Running   0               161m
default        pod/myapp-7b94444f8d-nctmp            1/1     Running   0               161m
default        pod/myapp-7b94444f8d-tnj2j            1/1     Running   0               161m
kube-flannel   pod/kube-flannel-ds-8c9x7             1/1     Running   0               3h42m
kube-flannel   pod/kube-flannel-ds-8xd9g             1/1     Running   0               3h42m
kube-flannel   pod/kube-flannel-ds-lgtbb             1/1     Running   0               3h42m
kube-flannel   pod/kube-flannel-ds-q2fvl             1/1     Running   0               3h42m
kube-flannel   pod/kube-flannel-ds-wdmsn             1/1     Running   0               3h42m
kube-flannel   pod/kube-flannel-ds-wfmst             1/1     Running   0               3h42m
kube-system    pod/coredns-cb4864fb5-4tsg8           1/1     Running   0               4h13m
kube-system    pod/coredns-cb4864fb5-kpzdd           1/1     Running   0               4h13m
kube-system    pod/etcd-master1                      1/1     Running   1 (3h45m ago)   4h13m
kube-system    pod/etcd-master2                      1/1     Running   1 (3h43m ago)   4h10m
kube-system    pod/etcd-master3                      1/1     Running   1 (3h43m ago)   4h8m
kube-system    pod/kube-apiserver-master1            1/1     Running   1 (3h45m ago)   4h13m
kube-system    pod/kube-apiserver-master2            1/1     Running   1 (3h43m ago)   4h10m
kube-system    pod/kube-apiserver-master3            1/1     Running   1               4h8m
kube-system    pod/kube-controller-manager-master1   1/1     Running   1 (3h45m ago)   4h13m
kube-system    pod/kube-controller-manager-master2   1/1     Running   1 (3h43m ago)   4h10m
kube-system    pod/kube-controller-manager-master3   1/1     Running   1               4h8m
kube-system    pod/kube-proxy-42n9v                  1/1     Running   1               4h8m
kube-system    pod/kube-proxy-4ckkx                  1/1     Running   1 (3h43m ago)   4h7m
kube-system    pod/kube-proxy-755mw                  1/1     Running   1 (3h45m ago)   4h13m
kube-system    pod/kube-proxy-c977c                  1/1     Running   1 (3h43m ago)   4h7m
kube-system    pod/kube-proxy-htdr6                  1/1     Running   1 (3h43m ago)   4h8m
kube-system    pod/kube-proxy-nxqr6                  1/1     Running   1 (3h43m ago)   4h10m
kube-system    pod/kube-scheduler-master1            1/1     Running   1 (3h45m ago)   4h13m
kube-system    pod/kube-scheduler-master2            1/1     Running   1 (3h43m ago)   4h10m
kube-system    pod/kube-scheduler-master3            1/1     Running   1 (3h43m ago)   4h8m


```



##### 查看CRD

```bash
[root@master1 ~]# kubectl get crd
NAME                                                  CREATED AT
bgpconfigurations.crd.projectcalico.org               2023-07-22T12:10:37Z             
bgpfilters.crd.projectcalico.org                      2023-07-22T12:10:37Z                  
bgppeers.crd.projectcalico.org                        2023-07-22T12:10:37Z                    
blockaffinities.crd.projectcalico.org                 2023-07-22T12:10:37Z            
caliconodestatuses.crd.projectcalico.org              2023-07-22T12:10:37Z
clusterinformations.crd.projectcalico.org             2023-07-22T12:10:37Z 
felixconfigurations.crd.projectcalico.org             2023-07-22T12:10:37Z
globalnetworkpolicies.crd.projectcalico.org           2023-07-22T12:10:37Z
globalnetworksets.crd.projectcalico.org               2023-07-22T12:10:37Z
hostendpoints.crd.projectcalico.org                   2023-07-22T12:10:37Z  
```



##### 查看指定API Group的资源

```bash
[root@ubuntu2204 ~]# kubectl api-resources --api-group apps
NAME                  SHORTNAMES   APIVERSION   NAMESPACED   KIND
controllerrevisions                apps/v1      true         ControllerRevision
daemonsets            ds           apps/v1      true         DaemonSet
deployments           deploy       apps/v1      true         Deployment
replicasets           rs           apps/v1      true         ReplicaSet
statefulsets          sts          apps/v1      true         StatefulSet
```



#### 用代理访问访问APIServer

```bash
# 前台启动一个代理
[root@master1 ~]#kubectl proxy --port=8081
Starting to serve on 127.0.0.1:8081

#在另一个终端执行下面
#使用 jq 命令(json 数据处理的命令行工具)处理结果：
[root@master1 ~]#curl -s 127.0.0.1:8081/api/  | jq .kind
"APIVersions"

# 查看版本
[root@master1 ~]#curl -s 127.0.0.1:8081/version  | jq 
{
  "major": "1",
  "minor": "30",
  "gitVersion": "v1.30.2",
  "gitCommit": "39683505b630ff2121012f3c5b16215a1449d5ed",
  "gitTreeState": "clean",
  "buildDate": "2024-06-11T20:21:00Z",
  "goVersion": "go1.22.4",
  "compiler": "gc",
  "platform": "linux/amd64"
}
```



### 资源清单格式

#### 资源配置清单介绍

资源配置清单的格式采用 Yaml 格式

第一级字段名一般包括: **apiVersion**、**kind**、**metadata**、**spec**、**status** 五个字段

字段名采有小驼峰命名法,而值一般采用大驼峰命令法



**第一级字段简介**

- apiVersion、kind 和 metadata 字段的功能基本相同
- spec 用于规定资源的期望状态，而资源的嵌套属性是有很大差别的。
- status字段则记录活动对象的当前状态，其要与 spec 中定义的状态相同，或者处于正转换为与其相同的 过程中。
- 用户可以使用 `kubectl get TYPE/NAME -o yaml/json` 命令来获取任何一个对象的yaml 或者 json 格式 的配置清单



**资源清单示例**

```yaml
# kubectl get namespace kube-system -o yaml
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: "2020-02-22T07:56:11Z"
  labels:
    kubernetes.io/metadata.name: kube-system
  name: kube-system
  resourceVersion: "7"
  uid: a176ab46-ab7b-4737-ab52-2e53ca1d1d46
spec:
  finalizers:- kubernetes
status:
  phase: Active
  
  
# kubectl get namespace kube-system -o json
{
 "apiVersion": "v1",
 "kind": "Namespace",
 "metadata": {
 "creationTimestamp": "2020-02-22T07:56:11Z",
 "labels": {
 "kubernetes.io/metadata.name": "kube-system"
        },
 "name": "kube-system",
 "resourceVersion": "7",
 "uid": "a176ab46-ab7b-4737-ab52-2e53ca1d1d46"
    },
 "spec": {
 "finalizers": [
 "kubernetes"
        ]
    },
 "status": {
 "phase": "Active"
    }
}
```



#### apiVersion和kind

apiVersion和kind 描述类型的元数据

- **apiVersion**：API版本,用于对同一资源对象的不同版本进行并行管理，主要有 alpha、betal、 stable
  - 格式：组名/版本
  - 查看命令：kubectl api-versions，可以看到当前共有27+个分组和版本
- **kind**：资源类型,kubernetes的专用资源对象
  - 查看命令： kubectl api-resources  [--api-group=]，可以看到当前共有50+种资源对象和对应的 APIVERSION 版本信息



#### metadata 嵌套字段

metadata 字段用于描述对象的元数据,即属性信息，其内嵌多个用于定义资源的元数据，如 **name** 和  **labels** 等。这些字段可以分为必选字段和可选字段



**必选字段：**

- **name**: 设定当前对象的名称，名称空间间级的资源在其所属的名称空间的同一类型中必须唯一
- **namespace**: 指定当前对象隶属的名称空间，默认值为 default，实现资源隔离
- **uid**: 当前对象的唯一标识符，用于区别"已删除"和"重新创建"的同一个名称的对象,系统可以自动生 成



**可选字段：**

- **labels**: 设定用于标识当前对象的标签，键值数据，格式：key1: value1 ,常用作标签选择器的挑选条件
- **annotation**: 非标识型键值数据，格式：key1: value1,用来作为挑选条件，用于 labels 的补充，不支持标签选择器的选择
- **resourceVersion**:当前对象的内部版本标识，用来让客户端确定对象的变动与否
- **generation**: 标识当前对象目标状态的代别
- **creationTimestamp**: 当前对象创建日期的时间戳
- **deletionTimestamp**: 当前对象删除日期的时间戳



####  spec 和 status 字段

定义资源配置清单时，spec 是必须的字段。用于描述对象的目标状态，也就是用户期望对象所表现出来的特征。

**spec 字段**

- Specification 规格字段
- 此字段对于不同的对象类型来说各不相同，具体字段含义及所接受的数据类型需要参照 Kubernets  API 手册中的说明进行获取。可通过命令  **kubectl explain KIND.spec** 获取具体帮助



**status 字段**

- 此字段记录对象的当前实际运行的状态，由 Kubernetes 系统负责更新，用户不能手动定义。
- Master 节点的 controller manager 通过相应的控制器组件动态管理并确保对象的实际转态匹配用 户所期望的状态。比如:Deployment 是一种描述集群中运行应用的资源对象，因此，创建  Deployment 类型对象时，需要为目标 Deployment 对象设定 spec，指定期望需要运行的 Pod 副 本数量、使用的标签选择器以及 Pod 模板等。在创建时，Kubernetes 相关组件读取待创建的  Deployment 对象的 spec以及系统上相应的活动对象的当前状态，必要时对活动的对象更新以确 保 status 字段吻合 spec 字段中期望的状态。
- **注意：**数据类的资源对象无spec, Status 字段，比如：configmaps，secrets ， endpoints 等



#### 使用命令生成清单文件

``````yaml
# 不执行，而是生产对应的清单文本内容输出到终端
kubectl create deployment myapp --image registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v1.0 --replicas 3 --dry-run=client -o yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: myapp
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: myapp
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v1.0
        name: myapp
        resources: {}
status: {}


# 将其输入到文件
kubectl create deployment myapp --image registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v1.0 --replicas 3 --dry-run=client -o yaml > myapp.yaml

# 得到资源清单后，可以根据需求进行更改
``````



#### 基于现有资源生成清单文件

```yaml
# 查看现有Services资源
[root@master1 ~]# kubectl get services
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP        7h4m
myapp        NodePort    10.98.161.155   <none>        80:31021/TCP   5h29m

# 基于myapp，输出它的资源清单文件
[root@master1 ~]# kubectl get services myapp -o yaml
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: "2024-12-15T12:03:41Z"
  labels:
    app: myapp
  name: myapp
  namespace: default
  resourceVersion: "13753"
  uid: e9d14260-ef75-4256-8887-200867c3d60a
spec:
  clusterIP: 10.98.161.155
  clusterIPs:
  - 10.98.161.155
  externalTrafficPolicy: Cluster
  internalTrafficPolicy: Cluster
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - name: 80-80
    nodePort: 31021
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: myapp
  sessionAffinity: None
  type: NodePort
status:
  loadBalancer: {}
```



#### 资源清单格式文档帮助Explain

```bash
[root@master1 ~]#kubectl explain pod
KIND:       Pod
VERSION:    v1

DESCRIPTION:
    Pod is a collection of containers that can run on a host. This resource is
    created by clients and scheduled onto hosts.
    
FIELDS:
  apiVersion	<string>
    APIVersion defines the versioned schema of this representation of an object.
    Servers should convert recognized schemas to the latest internal value, and
    may reject unrecognized values. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

  kind	<string>
    Kind is a string value representing the REST resource this object
    represents. Servers may infer this from the endpoint the client submits
    requests to. Cannot be updated. In CamelCase. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

  metadata	<ObjectMeta>
    Standard object's metadata. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

  spec	<PodSpec>
    Specification of the desired behavior of the pod. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

  status	<PodStatus>
    Most recently observed status of the pod. This data may not be up to date.
    Populated by the system. Read-only. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

# 递进查询
[root@master1 ~]#kubectl explain pod.spec
KIND:       Pod
VERSION:    v1

FIELD: spec <PodSpec>


DESCRIPTION:
    Specification of the desired behavior of the pod. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    PodSpec is a description of a pod.
    
FIELDS:
  activeDeadlineSeconds	<integer>
    Optional duration in seconds the pod may be active on the node relative to
    StartTime before the system will actively try to mark it failed and kill
    associated containers. Value must be a positive integer.

  affinity	<Affinity>
    If specified, the pod's scheduling constraints

  automountServiceAccountToken	<boolean>
    AutomountServiceAccountToken indicates whether a service account token
    should be automatically mounted.

  containers	<[]Container> -required-
    List of containers belonging to the pod. Containers cannot currently be
    added or removed. There must be at least one container in a Pod. Cannot be
    updated.

  dnsConfig	<PodDNSConfig>
    Specifies the DNS parameters of a pod. Parameters specified here will be
    merged to the generated DNS configuration based on DNSPolicy.
...
```





#### 资源对象的管理方式

kubectl 命令可分为三类命令：

- **指令式命令(imperative command)**

  - 指令式命令包括**kubectl run/expose/delete/ge**t等命令
  - 适合完成一次性的操作任务

  

- **指令式对象配置(imperative object configuration)**

  - 指令式对象配置管理包括**kubectl create/delete/get/replace/edit**等
  - 基于资源配置文件执行对象管理操作，但只能独立引用每个配置清单文件
  - **此方式没有幂等性,重复执行可能会出错,生产不推荐使用**

  

- **声明式对象配置(declarative object configration)**

  - 基于资源配置文件执行对象管理操作
  - 可直接引用目录下的所有配置清单文件，也可直接作用于单个配置文件
  - 资源对象的创建、删除及修改操作全部通过命令**kubectl apply/patch**等来完成，并且每次操作 时，提供给命令的配置信息都将保存于对象的注释信息(kubectl.kubernetes.io/last-applied configuration)中，

  

  ```bash
  kubectl apply -f /path/file -f .....    #加载指定文件
  kubectl apply -f /path                  #加载指定目录下的所有以.yaml,.yml,.json后缀的文件
  kubectl apply -f /path -f /path1/path2  # 不支持递归，所以如果目录下有子目录，需要多个-f分别加载
  kubectl apply -f URL                    #加载URL的文件
  ```

  



### 名称空间



#### 名称空间说明

![alt text](images\image30.png)



Kubernetes 的资源工作的有效范围分成两种级别:

- **集群级别**: 针对整个Kubernetes集群内都有效
  - 
- **名称空间级别**: 只针对指定名称空间内有效,而不属于任务名称空间



##### **名称空间的作用**

- 名称空间 Namespace 用于将集群分隔为多个隔离的逻辑分区以配置给不同的用户、租户、环境或者项目使用。
- 名称空间限定了资源对象工作在指定的名称范围内的作用域
- **注意: 名称空间本身是 Kubernetes 集群级别的资源**



##### **名称空间的使用场景**

- **环境管理**：需要在同一Kubernetes集群上隔离研发、预发和生产等一类的环境时，可以通过名称空间进行
- **隔离**：多个项目团队的不同产品线需要部署于同一Kubernetes集群时，可以使用名称空间进行隔离
- **资源控制**：名称空间可用作资源配额的承载单位，从而限制其内部所有应用可以使用的CPU/Memory/PV各自 的资源总和
  - 需要在产品线或团队等隔离目标上分配各自总体可用的系统资源时，可通过名称空间实现
- **权限控制**：基于RBAC鉴权体系，能够在名称空间级别进行权限配置
- **提高集群性能**：进行资源搜索时，名称空间有利于Kubernetes API缩小查找范围，从而对减少搜索延迟和提升性能 有一定的帮助





##### **名称空间分类**（**两类**）

- **系统级名称空间**
  - 由Kubernetes集群默认创建，主要用来隔离系统级的资源对象 所有的系统级名称空间均不能进行删除操作（即使删除也会自动重建） **除default外，其它三个系统级名称空间**不应该用作业务应用的部署目标
  - **default**：为任何名称空间级别的资源提供的默认的名称空间
  - **kuhe-system**：Kubernetes集群自身组件及其它系统级组件使用的名称空间，Kubernetes自身的 关键组件均部署在该名称空间中
  - **kube-public**：公众开放的名称空间，所有用户（包括Anonymous）都可以读取内部的资源,通常为空
  - **kube-node-lease**：节点租约资源所用的名称空间
    - 分布式系统通常使用“租约(Leqse)”机制来锁定共享资源并协调集群成员之间的活动 Kubernetes上的租约概念由API群组coordination.k8s.io群组下的Lease资源所承载，以支撑系统 级别的功能需求，例如节点心跳( node heartbeats)和组件级的领导选举等 Kubernetes集群的每个管理组件在该名称空间下都有一个与同名的Iease资源对象 
    - `~# kubectl -n kube-node-lease get lease`



- **自定义名称空间**
  - 由用户按需创建
  - 比如: 根据项目和场景, 分别创建对应不同的名称空间





#### 查看名称空间及资源对象

```bash
[root@master1 ~]#kubectl get ns
NAME              STATUS   AGE
default           Active   65m
kube-flannel      Active   63m
kube-node-lease   Active   65m
kube-public       Active   65m
kube-system  
Active   65m


[root@master1 ~]#kubectl get ns default -o yaml
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: "2024-12-16T05:34:09Z"
  labels:
    kubernetes.io/metadata.name: default
  name: default
  resourceVersion: "42"
  uid: b650835c-84e8-464a-84af-4955cb56285e
spec:
  finalizers:
  - kubernetes
status:
  phase: Active
  
  
# 查看指定信息
[root@master1 ~]#kubectl get ns default -o jsonpath={.metadata.name}
default

[root@master1 ~]#kubectl get ns default -o jsonpath={.apiVersion}
v1

# 查看默认名称下的资源
[root@master1 ~]# kubectl get all
NAME                         READY   STATUS    RESTARTS   AGE
pod/myapp-7b94444f8d-9xld5   1/1     Running   0          61m
pod/myapp-7b94444f8d-dhkdj   1/1     Running   0          61m
pod/myapp-7b94444f8d-ssp7z   1/1     Running   0          61m

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   69m

NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/myapp   3/3     3            3           61m

NAME                               DESIRED   CURRENT   READY   AGE
replicaset.apps/myapp-7b94444f8d   3         3         3       61m

# 查看指定名称空间的资源
[root@master1 ~]# kubectl get all -n kube-system 
NAME                                  READY   STATUS    RESTARTS   AGE
pod/coredns-cb4864fb5-5rbqf           1/1     Running   0          70m
pod/coredns-cb4864fb5-mzd84           1/1     Running   0          70m
pod/etcd-master1                      1/1     Running   0          70m
pod/kube-apiserver-master1            1/1     Running   0          70m
pod/kube-controller-manager-master1   1/1     Running   0          70m
pod/kube-proxy-h2kx8                  1/1     Running   0          68m
pod/kube-proxy-kklfd                  1/1     Running   0          68m
pod/kube-proxy-kmzqq                  1/1     Running   0          70m
pod/kube-proxy-vlvhj                  1/1     Running   0          69m
pod/kube-scheduler-master1            1/1     Running   0          70m

NAME               TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
service/kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   70m

NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/kube-proxy   4         4         4       4            4           kubernetes.io/os=linux   70m

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/coredns   2/2     2            2           70m

NAME                                DESIRED   CURRENT   READY   AGE
replicaset.apps/coredns-cb4864fb5   2         2         2       70m


```



#### 创建Namespace资源



##### **指令式命令创建**

使用指令式命令 `kubectl create` 可以直接创建名称空间，只需指定名称空间名称

```bash
[root@master1 ~]# kubectl create ns ns-mystical
namespace/ns-mystical created

[root@master1 ~]# kubectl get ns ns-mystical 
NAME          STATUS   AGE
ns-mystical   Active   8s
```

**注意**：实际生产中不建议使用指令式命令和配置，直接使用声明式就可以。



##### **指令式配置创建**

`kubectl create -f </path/to/namespace-obj.yaml `实现创建

此方式生产不建议使用,执行此命令需要指定的namespace不存在

```bash
[root@master1 ~]#vim namespace-test1.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: namespace-test1

# 创建
[root@master1 ~]#kubectl create -f namespace-test1.yaml 
namespace/namespace-test1 created

# 查看
[root@master1 ~]#kubectl get ns namespace-test1 
NAME              STATUS   AGE
namespace-test1   Active   8s
```



##### 声明式配置创建

Namespace 是 Kubernetes API 的标准资源类型之一，其配置主要有 kind、apiVolume、metadata 和 spec 等一级字段组成。使用 kubectl create/apply -f /path/to/namespace-obj.yaml 命令就可以 创建名称空间资源

```bash
[root@master1 ~]#vim namespace-test2.yaml 

[root@master1 ~]#cat namespace-test2.yaml 
apiVersion: v1
kind: Namespace
metadata:
  name: namespace-test2
  
[root@master1 ~]#kubectl apply -f namespace-test2.yaml 
namespace/namespace-test2 created

[root@master1 ~]#kubectl get namespaces namespace-test2 
NAME              STATUS   AGE
namespace-test2   Active   16s

# 使用命令生成声明式yaml文件
[root@master1 ~]# kubectl create ns stage --dry-run=client -o yaml > stage-ns.yaml
[root@master1 ~]# cat stage-ns.yaml 
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: stage
spec: {}
status: {}
```



#### 删除Namespace资源

注意: **删除 Namespace 会级联删除此名称空间的所有资源**,非常危险

```bash
[root@master1 ~]#kubectl delete namespaces namespace-test1 
namespace "namespace-test1" deleted

[root@master1 ~]#kubectl delete -f namespace-test2.yaml 
namespace "namespace-test2" deleted

# 在指定名称空间下创建资源
[root@master1 ~]#kubectl apply -f myapp.yaml -n ns-mystical 
deployment.apps/myapp created

# 查看指定名称空间(ns-mystical)下的指定资源(pod)
[root@master1 ~]#kubectl get pod -n ns-mystical 
NAME                     READY   STATUS    RESTARTS   AGE
myapp-7b94444f8d-6ms2c   1/1     Running   0          23s
myapp-7b94444f8d-c9g6n   1/1     Running   0          23s
myapp-7b94444f8d-l5bgb   1/1     Running   0          23s

# 删除指定名称空间
[root@master1 ~]#kubectl delete namespaces ns-mystical 
namespace "ns-mystical" deleted

# 所有此名称空间下的资源都被删除
[root@master1 ~]#kubectl get -n ns-mystical all
No resources found in ns-mystical namespace.
```





#### 删除指定名称空间的资源 

使用 kubectl 管理资源时，如果提供了名称空间选项，就表示此管理操作仅针对指定名称空间进行，而 删除 Namespace 资源则会级联删除其包含的所有其他资源对象

| 命令格式                        | 功能                                   |
| ------------------------------- | -------------------------------------- |
| kubectl delete TYPE RESOURCE -n | 删除指定名称空间内的指定资源           |
| kubectl delete TYPE --all -n    | 删除指定名称空间内的指定类型的所有资源 |
| kubectl delete all -n           | 删除指定名称空间内的所有资源           |
| kubectl delete all --all        | 删除所有名称空间中的所有资源           |



### Pod资源



#### Pod资源基础

Pod 是 Kubernetes API 中最常见最核心资源类型

**Pod 是一个或多个容器的集合**，因而也可称为容器集，但却是Kubernetes调度、部署和运行应用的原子单元

- 同一Pod内的所有容器都将运行于由Scheduler选定的同一个worker节点上
- 在同一个pod内的容器共享的**存储资源**、**网络协议栈**及容器的**运行控制策略**等
- 每个Pod中的容器依赖于一个特殊名为**pause容器**事先创建出可被各应用容器共享的**基础环境**，包括 Network、IPC和UTS名称空间共享给Pod中各个容器，PID名称空间也可以共享，但需要用户显式定 义,**Mount和User是不共享的**,每个容器有独立的Mount,User的名称空间


![alt text](images/image31.png)



Pod的组成形式有两种

- **单容器Pod**：除Pause容器外,仅含有一个容器
- **多容器Pod**：除Pause容器外，含有多个具有“超亲密”关系的容器，一般由主容器和辅助容器（比 如：**sidecar容器**）构成



**Pod资源分类**

- **自主式 Pod**
  - 由用户直接定义并提交给API Server创建的Pods
- **由Workload Controller管控的 Pod**
  - 比如: 由Deployment控制器管理的Pod
- **静态 Pod**
  - 由kubelet加载配置信息后，自动在对应的节点上创建的Pod
  - 用于实现Master节点上的系统组件API Server 、Controller-Manager 、Scheduler 和Etcd功能的 Pod
  - 相关配置存放在控制节点的 **`/etc/kubernetes/manifests`** 目录下



**总结：**

- Pod中最少有2个容器
- Pod = **Pause容器** + 业务容器



Pod的管理链

``````ABAP
# 自定义pod创建流程
kuebctl --> apiserver --> kubelet --> docker runc --> pod容器

# 在/etc/kubernetes/manifests目录下的yaml文件，不需要apiserver管理，会直接读取yaml文本执行创建pod

# 静态pod创建流程
/etc/kubernetes/mainfests目录下yaml文件 ---> kubelet --> docker runc --> ETCD | ApiServer Pod ...
``````



```bash
[root@master1 manifests]#ll /etc/kubernetes/manifests/
总计 24
drwxrwxr-x 2 root root 4096 12月 16 13:33 ./
drwxrwxr-x 4 root root 4096 12月 16 13:33 ../
-rw------- 1 root root 2408 12月 16 13:33 etcd.yaml
-rw------- 1 root root 4046 12月 16 13:33 kube-apiserver.yaml
-rw------- 1 root root 3567 12月 16 13:33 kube-controller-manager.yaml
-rw-r--r-- 1 root root    0 12月 10 20:09 .kubelet-keep
-rw------- 1 root root 1487 12月 16 13:33 kube-scheduler.yaml
```





#### 自主式Pod



##### 指令式命令创建Pod

通过kubectl 命令行工具指定选项创建 Pod，适合**临时性**工作

基本语法

```bash
kubectl run NAME --image=image [--port=port] [--replicas=replicas] 

kubectl run NAME --image=image [--env="key=value"] [--port=port] [--dryrun=server|client] [--overrides=inline-json] [--command] -- [COMMAND] [args...] [options]

#参数详解
--image='' #指定容器要运行的镜像
--port='' #设定容器暴露的端口
--dry-run=true #以模拟的方式来进行执行命令
--env=[] #执行的时候，向对象中传入一些变量
--labels='' #设定pod对象的标签
--limits='cpu=200m,memory=512Mi' #设定容器启动后的资源配置
--replicas=n #设定pod的副本数量,新版不再支持
--command=false     #设为true，将 -- 后面的字符串做为命令代替容器默认的启动命令，而非做为默
认启动命令的参数
-it            #打开交互终端
--rm           #即出即删除容器
--restart=Never #不会重启
```



示例

```bash
#初始化一个Pod对象，包含一个nginx容器
[root@master1 manifests]#kubectl run myapp-pod --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v1.0
pod/myapp-pod created

#创建Busybox的Pod,默认busybox没有前台进程,需要指定前台程序才能持继运行
[root@master1 manifests]#kubectl run busbox --image busybox:1.30 -- sleep 3600
pod/busbox created

[root@master1 manifests]#kubectl get pod
NAME                     READY   STATUS    RESTARTS   AGE
busbox                   1/1     Running   0          17s

# 进入容器
[root@master1 manifests]#kubectl exec -it busbox -- sh
/ # 

# 运行pod时定义一个变量
[root@master1 manifests]#kubectl run busybox --image busybox:1.30 --env="NAME=mystical" -- sleep 3600
pod/busybox created

[root@master1 manifests]#kubectl get pod
NAME                     READY   STATUS    RESTARTS   AGE
busybox                  1/1     Running   0          8s
myapp-7b94444f8d-9xld5   1/1     Running   0          133m
myapp-7b94444f8d-dhkdj   1/1     Running   0          133m
myapp-7b94444f8d-ssp7z   1/1     Running   0          133m
myapp-pod                1/1     Running   0          8m28s

[root@master1 manifests]#kubectl exec -it busybox -- sh
/ # echo $NAME
mystical
```



#### pod资源清单说明



##### yaml格式的Pod清单文件-极简版

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp2
  namespace: m58-namespace
spec:
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v1.0
    name: myapp2
```



##### yaml格式的Pod清单文件实例-完整版

```yaml
# yaml格式的Pod定义文件完整内容
apiVersion: v1
kind: Pod
metadata:
  name: string
  namespace: string
  labels:
    name: string
  annotations:
    name: string
spec:
  initContainers:
  - name: string
    image: string
    imagePullPolicy: Always  # Options: Always, Never, IfNotPresent
    command: 
      - string
    args: 
      - string
  containers:
  - name: string
    image: string
    imagePullPolicy: Always  # Options: Always, Never, IfNotPresent
    command: 
      - string
    args: 
      - string
    workingDir: string
    volumeMounts:
    - name: string
      mountPath: string
      readOnly: true  # Options: true, false
    ports:
    - name: string
      containerPort: 80  # Replace with the correct port
      hostPort: 80  # Replace with the correct port
      protocol: TCP  # Options: TCP, UDP, SCTP
    env:
    - name: string
      value: string
    resources:
      limits:
        cpu: "500m"  # Replace with actual limit
        memory: "128Mi"  # Replace with actual limit
      requests:
        cpu: "250m"  # Replace with actual request
        memory: "64Mi"  # Replace with actual request
    startupProbe:
      httpGet:
        path: /healthz
        port: 80  # Replace with actual port
    livenessProbe:
      exec:
        command: 
          - string
      httpGet:
        path: /healthz
        port: 80  # Replace with actual port
        host: localhost  # Replace with actual host
        scheme: HTTP  # Options: HTTP, HTTPS
        httpHeaders:
        - name: string
          value: string
      tcpSocket:
        port: 80  # Replace with actual port
      initialDelaySeconds: 10
      timeoutSeconds: 5
      periodSeconds: 10
      successThreshold: 1
      failureThreshold: 3
    securityContext:
      privileged: false  # Options: true, false
  restartPolicy: Always  # Options: Always, Never, OnFailure
  nodeSelector: 
    disktype: ssd  # Example node selector
  nodeName: string  # Replace with actual node name
  imagePullSecrets:
  - name: my-secret  # Replace with actual secret name
  hostNetwork: false  # Options: true, false
  volumes: 
  - name: empty-volume
    emptyDir: {}
  - name: host-path-volume
    hostPath:
      path: /data/volume  # Replace with actual path
  - name: secret-volume
    secret:
      secretName: string  # Replace with actual secret name
      items:     
      - key: string
        path: string
  - name: configmap-volume
    configMap:
      name: string  # Replace with actual ConfigMap name
      items:
      - key: string
        path: string
```



##### 更新Pod资源

```bash
# 方法1
# 导出配置
# kubectl get pods pod-test1 -o yaml pod-test1-update.yaml

# 编译导出的配置清单
[root@master1 ~]# vim myapp-pod-update.yaml 
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: "2024-12-16T07:47:09Z"
  labels:
    run: myapp-pod
  name: myapp-pod
  namespace: default
  resourceVersion: "13553"
  uid: 6e9fe649-9761-4d71-a7f9-9e8423e105b4
spec:
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:1.0  # 改为myapp:2.0
    imagePullPolicy: IfNotPresent
...

# 更新
kubectl replace -f myapp-pod-update.yaml # replace不建议使用，没有幂等性，建议apply

# 验证是否修改
[root@master1 ~]# kubectl describe -f myapp-pod-update.yaml
...
Events:
  Type    Reason     Age                  From               Message
  ----    ------     ----                 ----               -------
  Normal  Scheduled  48m                  default-scheduler  Successfully assigned default/myapp-pod to node1
  Normal  Pulled     48m                  kubelet            Container image "registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v1.0" already present on machine
  Normal  Pulling    5m23s                kubelet            Pulling image "registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v2.0"
  Normal  Pulled     5m12s                kubelet            Successfully pulled image "registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v2.0" in 10.467s (10.468s including waiting). Image size: 23012239 bytes.
  Normal  Killing    60s (x2 over 5m23s)  kubelet            Container myapp-pod definition changed, will be restarted
  Normal  Pulling    60s                  kubelet            Pulling image "registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v3.0"
  Normal  Created    43s (x3 over 48m)    kubelet            Created container myapp-pod
  Normal  Pulled     43s                  kubelet            Successfully pulled image "registry.cn-beijing.aliyuncs.com/wangxiaochun/myapp:v3.0" in 16.971s (16.971s including waiting). Image size: 23012239 bytes.
  Normal  Started    42s (x3 over 48m)    kubelet            Started container myapp-pod

```



##### 声明式对象管理方式

**创建 Pod 资源对象**

```bash
[root@master1 yaml]#kubectl apply -f pod-test1.yaml 
pod/pod-test1 created

[root@master1 yaml]#kubectl get -f pod-test1.yaml -o wide
NAME       READY   STATUS   RESTARTS   AGE   IP           NODE               
NOMINATED NODE   READINESS GATES
pod-test1   1/1     Running   0         5m8s   172.16.3.13   node1.wang.org   
<none>           <none>

[root@master1 ~]#curl 172.16.3.13 -I
HTTP/1.1 200 OK
Server: nginx/1.21.5
Date: Tue, 01 Mar 2022 04:32:32 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Tue, 28 Dec 2021 15:28:38 GMT
Connection: keep-alive
ETag: "61cb2d26-267"
Accept-Ranges: bytes
```



**更新应用版本**

```bash
# 更新对象的操作，可以直接在原有的资源清单文件上修改后再执行kubectl apply
# 生产环境下，建议使用，具有幂等性
[root@master1 yaml]#vim pod-test1.yaml
[root@master1 yaml]#cat pod-test1.yaml
apiVersion: v1
kind: Pod      
metadata:       
 name: pod-test1 
 labels:      
   app: test1  
   version: v1.0
spec:         
 containers:  
  - name: nginx-web01
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0 #修改此行
   
#应用更新
[root@master1 yaml]#kubectl apply -f pod-test1.yaml 
pod/pod-test1 configured
```



#### Pod查看状态

可以通过以下命令查看Pod 状态

```bash
kubectl get pod <pod_name> [(-o|--output=)json|yaml|jsonpath] [-n namespace]
kubectl describe pod <pod_name> [-n namespace]
```



范例

``````bash
#查看当前名称空间的所有pod
[root@master1 ~]# kubectl get pod

#查看所有空间的所有pod
[root@master1 ~]# kubectl get pod -A

#查看指定pod当前状态信息
[root@master1 yaml]# kubectl get -f pod-test1.yaml 
[root@master1 ~]# kubectl get pod pod-test1 
[root@master1 ~]# kubectl get po pod-test1 #支持缩写po
NAME       READY   STATUS   RESTARTS   AGE
pod-test1   1/1     Running   0         67s

#持续查看pod状态
# kubectl get pods pod-test1 -w

#查看扩展信息
[root@master1 ~]#kubectl get pod pod-test1 -o wide
NAME       READY   STATUS   RESTARTS   AGE   IP           NODE               
NOMINATED NODE   READINESS GATES
pod-test1   1/1     Running   0         88s   172.16.3.12   node1.wang.org   
<none>           <none>

#通过 -o yaml 的方式来进行查看yaml格式的详细信息
[root@master1 ~]#kubectl get pod pod-test -o yaml
apiVersion: v1
kind: Pod
metadata:
 annotations:
   kubectl.kubernetes.io/last-applied-configuration: |
......

#查看pod上面的label
[root@master1 ~]#kubectl get pod pod-test1 --show-labels
NAME       READY   STATUS   RESTARTS       AGE   LABELS
pod-test1   1/1     Running   7 (7h4m ago)   14d   app=test1,version=v2.0
``````



#### 查看Pod中指定容器应用的日志

```bash
kubectl logs [-f] (POD | TYPE/NAME) [-c CONTAINER] [options]
# 选项

-p 前一个已退出的容器的日志
--all-containers=true 所有容器
--tail=N 最后N个日志

# 示例
[root@master1 ~]#kubectl logs myapp-pod 
10.244.0.0 - - [16/Dec/2024:16:34:39 +0800] "GET / HTTP/1.1" 200 31 "-" "curl/7.81.0"

# 进入容器内执行操作
[root@master1 ~]#kubectl exec myapp-pod -- ps aux
PID   USER     TIME  COMMAND
    1 root      0:00 nginx: master process nginx -g daemon off;
    7 nginx     0:00 nginx: worker process
    8 root      0:00 ps aux
```



####  进入Pod 执行命令

```bash
kubectl exec (POD | TYPE/NAME) [-c CONTAINER] [flags] -- COMMAND [args...] [options]
```

范例

```bash
# 交互式执行
[root@master1 ~]#kubectl exec -it myapp-pod -- sh
/ # ps aux
PID   USER     TIME  COMMAND
    1 root      0:00 nginx: master process nginx -g daemon off;
    7 nginx     0:00 nginx: worker process
   14 root      0:00 sh
   20 root      0:00 ps aux
```



#### 删除 Pod

删除资源对象推荐使用指令式管理命令 `kubectl delete`

```bash
kubectl delete pod <pod_name> ... [--force --grace-period=0]
```



范例

```bash
#优雅删除
[root@master1 ~]#kubectl delete pod pod-test1

#立即删除
[root@master1 ~]#kubectl delete pod pod-test1 --force --grace-period=0
warning: Immediate deletion does not wait for confirmation that the running 
resource has been terminated. The resource may continue to run on the cluster 
indefinitely.
pod "pod-test1" force deleted

#删除多个资源
[root@master1 yaml]#kubectl delete -f pod-test1.yaml -f /data/kubernetes/yaml/pod-test2.yaml

#删除所有pod
[root@master1 ~]#kubectl get po|cut -d" " -f1 | tail -n +2 |xargs kubectl delete pod

#快速删除所有pod
[root@master1 ~]#kubectl get pod|awk 'NR!=1{print $1}'|xargs -i kubectl delete pod {} --force --grace-period=0
```



#### 创建定制的Pod

kubernets 支持多种定制 Pod 的实现方法

- 对于不同应用的Pod,重新定制对应的镜像
- 启动容器时指定env环境变量
- 启动容器的指定command和args
- 将配置信息基于卷资源对象，再将其加载到容器，比如：configMap和secret等



#####  利用环境变量`env`实现容器传参

在容器上嵌套使用env字段

- 每个环境变量需要通过`pod.spec.containers.env.name`给出指定的名称
- 传递的值则定义在`pod.spec.containers.env.value`字段上



示例：实现LAMP的应用wordpress

```bash
# mysql
[root@master1 lamp]# vim pod-mysql.yaml
[root@master1 lamp]# cat pod-mysql.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: mydb
  namespace: default
spec:
  containers:
  - name: mysql
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
    env:
    - name: MYSQL_ROOT_PASSWORD
      value: "654321"
    - name: MYSQL_DATABASE
      value: wordpress
    - name: MYSQL_USER
      value: wpuser
    - name: MYSQL_PASSWORD
      value: "123456
   
# 查看MySQL对应Pod的IP
[root@master1 lamp]#kubectl apply -f pod-mysql.yaml
pod/mydb created

[root@master1 lamp]#kubectl get pods mydb -o wide
NAME   READY   STATUS    RESTARTS   AGE     IP           NODE    NOMINATED NODE   READINESS GATES
mydb   1/1     Running   0          2m44s   10.244.2.6   node2   <none>           <none>


# wordpress
[root@master1 lamp]#vim pod-wordpress.yaml
[root@master1 lamp]#cat pod-wordpress.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: wordpress
  namespace: default
spec:
  hostNetwork: true
  containers:
  - name: wordpress
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache
    env:
    - name: WORDPRESS_DB_HOST
      value: 10.244.2.6
    - name: WORDPRESS_DB_NAME
      value: wordpress
    - name: WORDPRESS_DB_USER
      value: wpuser
    - name: WORDPRESS_DB_PASSWORD
      value: "123456"

[root@master1 lamp]#kubectl get pod -o wide
NAME                     READY   STATUS    RESTARTS      AGE     IP           NODE    NOMINATED NODE   READINESS GATES
myapp-7b94444f8d-9xld5   1/1     Running   0             4h16m   10.244.1.2   node1   <none>           <none>
myapp-7b94444f8d-dhkdj   1/1     Running   0             4h16m   10.244.2.2   node2   <none>           <none>
myapp-7b94444f8d-ssp7z   1/1     Running   0             4h16m   10.244.3.4   node3   <none>           <none>
myapp-pod                1/1     Running   2 (84m ago)   131m    10.244.1.5   node1   <none>           <none>
mydb                     1/1     Running   0             48m     10.244.2.6   node2   <none>           <none>
wordpress                1/1     Running   0             5m22s   10.0.0.202   node1   <none>           <none>
```

![alt text](images\image32.png)



##### 利用`command`和`args`字段传递容器的启动命令和参数

Pod配置中，spec.containers[].command字段能够在容器上指定替代镜像默认运行的应用程序，且可 同时使用spec.containers[].args字段进行参数传递，它们将覆盖镜像中的默认定义的参数。

- 若仅定义了command字段时，其值将覆盖镜像中定义的程序及参数。
- 若仅是定义了args字段，该字段值将作为参数传递给镜像中默认指定运行的应用程序
- **注意: args中使用环境变量,需要使用格式: $(环境变量名)**



**添加运行命令和参数**

```bash
[root@master1 yaml]#cat pod-with-cmd-and-args.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-cmd-and-args
spec:
  containers:
  - name: pod-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
    command: ['/bin/sh','-c']
    args: ['python3 /usr/local/bin/demo.py -p 8080']
    
[root@master1 yaml]#kubectl get pod -o wide
NAME                     READY   STATUS    RESTARTS      AGE   IP           NODE    NOMINATED NODE   READINESS GATES
myapp-7b94444f8d-66d4h   1/1     Running   1 (12m ago)   29h   10.244.4.4   node2   <none>           <none>
myapp-7b94444f8d-nctmp   1/1     Running   1 (12m ago)   29h   10.244.3.5   node1   <none>           <none>
myapp-7b94444f8d-tnj2j   1/1     Running   1 (12m ago)   29h   10.244.5.3   node3   <none>           <none>
pod-with-cmd-and-args    1/1     Running   1 (12m ago)   60m   10.244.3.4   node1   <none>           <none>

[root@master1 yaml]#curl 10.244.3.4:8080
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: pod-with-cmd-and-args, ServerIP: 10.244.3.4!
```



**添加运行命令，参数和环境变量**

```bash
[root@master1 yaml]#cat pod-with-cmd-and-args.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-cmd-and-args
spec:
  containers:
  - name: pod-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
    command: ['/bin/sh','-c']
    args: ['python3 /usr/local/bin/demo.py -p $port']
    env:
    - name: port
      value: "8888"
      
[root@master1 yaml]#kubectl get pod -o wide
NAME                     READY   STATUS    RESTARTS      AGE   IP           NODE    NOMINATED NODE   READINESS GATES
myapp-7b94444f8d-66d4h   1/1     Running   1 (29m ago)   29h   10.244.4.4   node2   <none>           <none>
myapp-7b94444f8d-nctmp   1/1     Running   1 (29m ago)   29h   10.244.3.5   node1   <none>           <none>
myapp-7b94444f8d-tnj2j   1/1     Running   1 (29m ago)   29h   10.244.5.3   node3   <none>           <none>
pod-with-cmd-and-args    1/1     Running   0             59s   10.244.5.4   node3   <none>           <none>
      
[root@master1 yaml]#curl 10.244.5.4:8888
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: pod-with-cmd-and-args, ServerIP: 10.244.5.4!
```

 

##### 使用宿主机网络实现容器的外部访问

默认容器使用私有的独立网段，无法从集群外直接访问，可以通过下面两种方式实现外部访问

- 让容器直接使用宿主机的网络地址，即容器使用host的网路模型
- 让容器通过宿主机的端口映射实现，即DNAT

注意：都要避免端口冲突



```bash
[root@master1 yaml]#cat pod-hostnetwork.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-hostnetwork-demo
spec:
  hostNetwork: true
  containers:
  - name: demo-env
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    env:
    - name: PORT
      value: "9999"
      
[root@master1 yaml]#kubectl apply -f pod-hostnetwork.yaml 
pod/pod-hostnetwork-demo created

[root@master1 yaml]#kubectl get pod -o wide
NAME                     READY   STATUS    RESTARTS      AGE     IP           NODE    NOMINATED NODE   READINESS GATES
myapp-7b94444f8d-66d4h   1/1     Running   1 (35m ago)   29h     10.244.4.4   node2   <none>           <none>
myapp-7b94444f8d-nctmp   1/1     Running   1 (35m ago)   29h     10.244.3.5   node1   <none>           <none>
myapp-7b94444f8d-tnj2j   1/1     Running   1 (35m ago)   29h     10.244.5.3   node3   <none>           <none>
pod-hostnetwork-demo     1/1     Running   0             21s     10.0.0.105   node2   <none>           <none>
pod-with-cmd-and-args    1/1     Running   0             7m33s   10.244.5.4   node3   <none>           <none>

[root@master1 yaml]#curl 10.0.0.105:9999
kubernetes pod-test v0.1!! ClientIP: 10.0.0.101, ServerName: node2, ServerIP: 10.0.0.105!
```



使用容器所在宿主机指定的端口

```bash
# 使用端口映射
[root@master1 yaml]#cat pod-hostport.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-hostport-demo
spec:
  containers:
  - name: demo-env
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    env:
    - name: PORT
      value: "9999"
    ports:                           # 使用宿主机指定端口
    - name: http                     # 不支持大写字母
      containerPort: 9999            # 使用上面变量相同的端口
      hostPort: 8888


# 本质上就是通过宿主机的DNAT策略实现
[root@master1 yaml]#ssh 10.0.0.104 iptables -vnL -t nat |grep DNAT|grep 8888
    1    60 DNAT       tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:8888 to:10.244.3.6:9999

[root@master1 yaml]#iptables --version
iptables v1.8.7 (nf_tables)

# 这里的 (nf_tables) 表示 iptables 是在 nftables 框架中实现的
# iptables 实际上是一个对 nftables 的封装
```





#### 临时容器

#####  了解临时容器

Pod 是 Kubernetes 应用程序的基本构建块。 由于 Pod 是一次性且可替换的，因此一旦 Pod 创建，就 无法将容器加入到 Pod 中。 取而代之的是，通常使用 Deployment 以受控的方式来删除并替换 Pod。

有时有必要检查现有 Pod 的状态。例如，对于难以复现的故障进行排查。 在这些场景中，可以在现有  Pod 中运行临时容器来检查其状态并运行任意命令。

Kubernetes v1.16推出临时容器, Kubernetes v1.25稳定可用, 就是在原有的Pod 上，添加一个**临时的 Container，这个Container可以包含我们排查问题所有的工具**, 比如: ip、ss、ps、pstree、top、kill、 top、jstat、jmap等







### Pod工作机制



#### Pod基本原理

![image-20241217182330834](D:\git_repository\cyber_security_learning\markdown_img\image-20241217182330834.png)

##### Pause容器

**什么是 pause 容器？**

- **pause 容器** 是每个 Pod 中的一个“基础”或“辅助”容器，作为 **“Pod的基础环境”**。
- **pause 容器的核心目的是**：
  1. 作为 Pod 中所有其他容器的“**根命名空间**”（包括网络、PID、IPC、用户命名空间等）。
  2. 提供一个**管理所有容器的父容器**。
  3. 充当**网络栈的宿主**，即将 Pod 的 IP 地址分配到 pause 容器。
  4. **防止孤儿进程**：pause 容器负责回收 Pod 中子进程（即僵尸进程），防止孤儿进程残留。
  5. **统一管理生命周期**：当 Pod 被销毁时，**所有与 pause 容器共享命名空间的容器**也会被销毁。



🟢 **pause 容器的主要作用**

| **作用**          | **描述**                                                     |
| ----------------- | ------------------------------------------------------------ |
| **网络命名空间**  | Pod 中的网络栈是 pause 容器的网络栈，所有其他容器与它共享 IP 地址、端口和网络命名空间。 |
| **PID 命名空间**  | Pod 内的所有容器与 pause 容器共享一个 PID 命名空间，Pod 内的进程能“看到”彼此的进程列表。 |
| **IPC 命名空间**  | 容器之间的进程通信（如信号、信号量）是通过 IPC 实现的，Pod 中的 IPC 命名空间由 pause 容器提供。 |
| **Volume 卷管理** | 如果 Pod 中有挂载卷，卷的路径通常先挂载到 pause 容器的文件系统中，其他容器共享这个路径。 |
| **僵尸进程回收**  | 如果 Pod 内的某个容器内的子进程退出，这个僵尸进程不会直接被宿主机的 init 进程 (PID 1) 回收，而是由 pause 容器回收。 |
| **父进程作用**    | pause 容器的 PID 始终是 Pod 中的第一个进程 (PID=1)，所有其他进程（即业务容器的进程）都是 pause 容器的“子进程”。 |





🟢 **实际的机制（深入剖析）**

- 1️⃣ 当 kubelet 启动一个 Pod 时：
  - **pause 容器首先启动**，这是 Pod 的第一个容器。
  - 启动 pause 容器的原因是：它会创建**PID 命名空间、网络命名空间、IPC 命名空间和 UTS 命名空间**。
  - pause 容器的 PID 在 Pod 命名空间中是 **1**，即**PID=1**。
- 2️⃣ 当其他业务容器启动时：
  - 业务容器不会从 pause 容器 fork() 出来，而是**containerd 或 dockerd** 启动的。
  - 业务容器和 pause 容器**共享 pause 容器的命名空间**（网络、IPC、PID、Volume 等），这就是“共享”命名空间的含义。
  - **从 PID 视角看**，所有业务容器中的进程都属于 pause 容器的子进程。



🟢 **为什么需要 pause 容器？**

- **统一命名空间**：
  - Pod 中的多个业务容器共享**网络命名空间**，这使得它们共享一个 IP 地址（Pod IP）。
  - 通过 pause 容器的 PID 1，所有业务容器可以共享同一个 PID 命名空间。
- **负责回收子进程**：
  - **回收僵尸进程**：如果业务容器内部的进程 (PID) 终止，会成为僵尸进程，系统的 init 进程通常负责回收僵尸进程。
  - 在 Pod 中，**pause 容器就是 Pod 中的 "init 进程"**，负责回收业务容器中的僵尸进程。
- **网络栈的基础**：
  - 通过 pause 容器的网络命名空间，Pod 中的每个业务容器共享一个 IP 地址和端口空间。



**🟢pod通信机制**

- Pod内多容器通信：容器件通信（容器模型）借助于pause容器实现
- 单节点内多Pod通信：主机间容器通信（host模型），利用kube-proxy实现
- 多节点内多Pod通信：跨主机网络解决方案（overlay模型），利用网络插件flannel，calico等实现



##### 静态Pod和动态Pod

基于控制的特性Pod 主要有两类：**静态pod**和**动态pod**

- 动态Pod

  - 之前创建管理的pod都是动态pod，也是应用最广泛的pod
  - 动态Pod 直接被集群中的API Server 进行管理

- 静态pod

  - 由特定节点上的kubelet进程来管理,对于**API Server 只能查看，而不能管理**。

  - 在本质上与动态pod没有区别，只是在于静态pod只能在特定的节点上运行

  - kubelet 默认会加载**/etc/kubernetes/manifests/*.yaml** 从而生成的静态Pod

  - 静态pod实现方式主要有两种：**配置文件**或者**http方式**。

    - 配置文件

      所谓的配置文件的方式，其实就是在特定的目录下存放我们定制好的资源对象文件，然后节点上的 kubelet服务周期性的检查该目录下的所有内容，对静态pod进行增删改查。其配置方式主要有两 步 

      1 定制kubelet服务定期检查配置目录 

      2 增删定制资源文件 

    - http方式

      1 准备http方式提供资源文件的web站点 

      2 工作节点的kubelet配置–manifest-url=<资源文件的url下载地址>

  ```bash
  # 查找静态文件配置路径的过程
  [root@master1 net.d]#systemctl status kubelet.service 
  ● kubelet.service - kubelet: The Kubernetes Node Agent
       Loaded: loaded (/lib/systemd/system/kubelet.service; enabled; vendor preset: enabled)
      Drop-In: /usr/lib/systemd/system/kubelet.service.d
               └─10-kubeadm.conf
       Active: active (running) since Tue 2024-12-17 14:20:02 CST; 6h ago
         Docs: https://kubernetes.io/docs/
     Main PID: 815 (kubelet)
        Tasks: 13 (limit: 2196)
       Memory: 68.4M
          CPU: 3min 13ms
       CGroup: /system.slice/kubelet.service
               └─815 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig
               
  # 基于上述的loaded (/lib/systemd/system/kubelet.service; enabled; vendor preset: enabled)
  [root@master1 net.d]#cat /lib/systemd/system/kubelet.service.d/10-kubeadm.conf 
  # Note: This dropin only works with kubeadm and kubelet v1.11+
  [Service]
  Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf"
  Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml"
  # This is a file that "kubeadm init" and "kubeadm join" generates at runtime, populating the KUBELET_KUBEADM_ARGS variable dynamically
  EnvironmentFile=-/var/lib/kubelet/kubeadm-flags.env
  # This is a file that the user can use for overrides of the kubelet args as a last resort. Preferably, the user should use
  # the .NodeRegistration.KubeletExtraArgs object in the configuration files instead. KUBELET_EXTRA_ARGS should be sourced from this file.
  EnvironmentFile=-/etc/default/kubelet
  ExecStart=
  ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS
  
  # 找到Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml"这样，说明kubelet的配置参数主要是在/var/lib/kubelet/config.yaml文件中定义
  
  [root@master1 net.d]#cat /var/lib/kubelet/config.yaml|grep static
  staticPodPath: /etc/kubernetes/manifests
  
  # 这个就是静态pod的专用目录
  
  ```



#### Pod管理机制

![image-20241217210820679](D:\git_repository\cyber_security_learning\markdown_img\image-20241217210820679.png)



#### Pod创建流程

客户端使用kubectl创建pod，需要先通知API Server，而kubectl能通知API Server是因为配置中，记录了API Server的地址

```bash
[root@master1 .kube]#grep server ~/.kube/config 
    server: https://master1.mystical.org:6443
    
# host中记录了master1.mystical.org对应的ip
[root@master1 .kube]#cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 ubuntu2204

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

10.0.0.201 master1 master1.mystical.org
10.0.0.202 node1 node1.mystical.org
10.0.0.203 node2 node2.mystical.org
10.0.0.204 node3 node3.mystical.org

```

##### 🌐 **1. 入口：kubectl 命令的发起**

**命令示例**：

```bash
kubectl run nginx --image=nginx --replicas=1
```

**操作过程**

1. kubectl 发起请求：

   - kubectl 将请求打包为一个 **HTTP REST 请求**，并发送到 **Kubernetes API Server**。
   - 通过 `kubectl` 命令，API Server 接收到**POST请求**，其中包含了 **Pod的定义信息**（YAML/JSON 格式的PodManifest）。

   

##### 📡 **2. API Server 处理请求**

**API Server的作用**：

1. 验证请求：

   - 进行身份验证（Authentication）和权限验证（Authorization）。
   - 例如，检查请求的用户是否具有创建Pod的权限。

   

2. 请求合法性校验：

   - 通过 **Admission Controllers** 进行一系列的规则检查（比如资源配额、Pod调度限制等）。
   - Admission Controller 可以拒绝不符合规范的Pod。

   

3. 对象序列化和持久化：

   - 检查请求的YAML/JSON定义是否符合 **Pod Schema**。
   - 如果检查通过，将其存储到 **etcd** 中。
   - 通过 `apiserver` 的 **etcd client** 将Pod信息序列化为二进制数据，并存储到etcd的**存储路径** `/registry/pods/{namespace}/{pod-name}` 中。

   

##### 📦 **3. etcd 存储 Pod 定义**

**etcd的作用**：

1. 数据存储：
   - etcd 存储的是**完整的Pod的定义**，如镜像、CPU/内存配额、环境变量等。
   - etcd 是一个分布式的键值存储，所有的K8s资源（Pod、Service、ConfigMap）都以路径的形式存储。
2. 数据变更触发通知：
   - etcd 作为一个**发布/订阅系统**，一旦新的Pod定义被存储，所有监听该路径的控制器（如**Controller-Manager** 和 **Scheduler**）都会被**Watch事件**触发。



##### ⚙️ **4. Scheduler 调度 Pod**

**Scheduler的作用**：

1. **监听Pod的变更**：
   - Scheduler 监听 `/registry/pods/` 目录的变更。
   - 监听到一个**未绑定Node的Pod**，即 `.spec.nodeName == null`，则启动调度。
2. **调度决策**：
   - Scheduler 会从所有**可用的Node中选择一个最优的Node**来运行这个Pod。
   - Scheduler会考虑以下因素：
     - **资源约束**：Node的CPU、内存是否足够。
     - **亲和性/反亲和性**：Pod的亲和性和反亲和性规则。
     - **污点和容忍度**：节点上是否有污点。
     - **节点健康状态**：节点是否Ready。
3. **写回调度结果**：
   - Scheduler 将调度的结果（`spec.nodeName: node01`）回写到 etcd，通知API Server。



##### 🔄 **5. Kubelet 监控 Pod 变更**

**Kubelet的作用**：

1. **监听 API Server 的事件**：
   - Kubelet 监听 `/registry/pods/{namespace}/{pod-name}` 目录的变更。
   - 一旦有变更，Kubelet会发现自己需要在本节点上**拉取一个新的Pod**。
2. **创建Pod沙箱（Pause容器）**：
   - Kubelet 使用 **container runtime (Docker/Containerd/CRI-O)** 创建一个**pause容器**。
   - pause 容器的作用：
     - **网络命名空间**：其他容器会和pause容器共享网络命名空间。
     - **PID命名空间**：共享进程命名空间。
     - **数据卷管理**：挂载Pod定义的卷到pause容器上，其他容器共享。
3. **创建Pod中的业务容器**：
   - **container runtime** 拉取镜像（如 nginx:latest），并在 pause 容器的**网络和PID命名空间中运行业务容器**。
   - 这个过程分为以下几个阶段：
     - **拉取镜像**：从**镜像仓库**中拉取镜像（docker hub、Harbor等）。
     - **解压镜像**：解压 tar 文件，加载容器文件系统。
     - **启动容器**：调用 `runc` 启动容器，和 pause 容器共享命名空间。



##### 📊 **6. 容器状态同步回 API Server**

**Kubelet的反馈机制**：

1. **Kubelet 汇报Pod状态**：
   - Pod 启动完成后，Kubelet 会将Pod的状态同步回API Server。
   - API Server将这些状态写入 etcd，状态路径是 `/registry/pods/{namespace}/{pod-name}`。
   - 用户可以通过 `kubectl get pods` 查看Pod的状态。
2. **容器健康检查和Liveness Probe**：
   - Kubelet 定期检查Pod的健康状态。
   - 如果容器的Liveness Probe失败，Kubelet会**重启容器**。



##### 流程图（可视化理解）

```scss
       kubectl run 
           │
           ▼
   ┌─────────────────┐
   │  API Server     │
   └─────────────────┘
           │  (身份验证、请求验证)
           ▼
   ┌─────────────────┐
   │  etcd 存储      │
   └─────────────────┘
           │
   (通知)  │   ┌─────────────────┐
           └─▶│ Scheduler 调度  │
               └─────────────────┘
                      │
               选择最佳节点
                      │
               ┌───────────┐
               │ etcd 存储 │
               └───────────┘
                      │
               (监听通知)
   ┌─────────────────┐
   │    Kubelet      │
   └─────────────────┘
      (在节点上启动Pod)

```



##### 🚀 **面试回答示例**

> **面试官问**：Kubernetes Pod 是如何创建的？ **回答思路**：

1. **kubectl run** 将YAML/JSON请求发到 **API Server**。
2. **API Server** 验证请求，将Pod定义写入 **etcd**。
3. **Scheduler** 监听到**etcd变更**，调度Pod到**最佳Node**。
4. **Kubelet** 监听到Pod定义，启动**Pause容器和业务容器**。
5. **Kubelet** 反馈Pod状态，用户可通过 `kubectl get pods` 查看状态。



##### 注意事项

1. **etcd 监听 API Server**：
   当用户通过 `kubectl` 创建、更新或删除 Pod 资源时，这些更改会存储到 **etcd**。
2. **API Server 监听 etcd**：
   **API Server 监听 etcd 中的变化**，并将变化通知 Kubelet 和 Controller Manager。
3. **Kubelet 监听 API Server**：
   Kubelet 通过 Watch API 从 API Server 获取其所在 Node 上的 Pod 列表，并在本地启动或终止相应的 Pod。

> 📝 **Kubelet 只能通过 API Server 来与 etcd 间接通信**。
> 这是为了确保所有数据的操作都由 API Server 统一控制和验证。





##### Pod创建流程自述（面试必背）



- 当使用 `kubectl apply -f pod.yaml` 时，kubectl 会将 YAML 文件中的**Kubernetes 资源对象**（Pod）转换为**JSON 格式的请求体**，并通过 **HTTP POST** 发送到 API Server
  - **kubectl 作为客户端**，会将 YAML 文件转换为**RESTful API 请求**，API Server 充当**服务端**。
  - 使用的是 **HTTP/2**，并且需要身份认证和权限控制（RBAC）。
  - API Server 会**先将 Pod 资源保存在内存中（Watch Cache）**，并异步写入 etcd。



- API Server通过gRPC与etcd通信，将Pod的数据持久化到etcd，**此时Pod的状态是Pending**，因为此时Pod还未被调度到某个节点



- Scheduler 通过 **watch 机制监听 API Server 中的 Pending Pods**。并通过预选过滤，优选打分，选择出最适合的节点，并将Pod通过POST请求binding到这个目标节点上



- API Server 将 Pod 的状态从 `Pending` 变为 `Scheduled`。并使用**PUT 请求** 更新 Pod 的状态，并同步到 etcd。同时**API Server 通过 Watch 机制将 Pod 变更事件推送给 Kubelet**。



- Kubelet 收到 API Server 发送的 Pod 数据后，Kubelet 使用**CRI（Container Runtime Interface）调用 containerd**。containerd 调用**runc**，创建 Pod 的 Linux 容器。Pod 进入**Running**状态。







#### Pod的生命周期



![image-20241218091558622](D:\git_repository\cyber_security_learning\markdown_img\image-20241218091558622.png)



- 创建指令送到apiserver
- 通知Schedule调度此请求到合适的节点
- **init容器**
  - 初始化容器（一次性容器，初始化结束，该容器就退出了），独立于主容器之外，即和主容器是隔离的
  - Pod可以拥有任意数量的init容器，init顺序执行，最后一个执行完成后，才启动主容器
  - init容器不支持探针检测功能
    - 它主要是为了主容器准备运行环境的功能，比如：给主容器准备配置文件，向主容器的存储写入数据，然后将存储卷挂载到主容器上，下载相关资源，监测主容器依赖服务等
- **启动后钩子PostStart（Post Start Hook）**: 与主容器同时启动
- 状态监测
- **Startup probe：启动探针**：启动探针用来探测这个服务是否起来的，如果探针检查失败，会认为该容器不健康，因此会重新启动容器，如果健康，就会进入下一步
  - 启动探针只检测容器是否启动，容器启动后，后续不再检查
- **Liveiness probe（存活探针）**：判断当前Pod是否处于存活状态，是Readiness存活的前提，对应READY状态的m/n的n值
- **Readiness Probe（就绪探针**）：判断当前Pod的主应用容器是否可以正常对外提供服务，只有Liveiness为存活，Readiness
  - Liveness probe和Readiness Probe持续容器终身，只要容器在启动，会不断地探测，如果容器出故障，可以进行一些操作
  - 三个探针就是用来检测容器健康性的



- Service关联Pod
- 接收用户请求





#### 关闭Pod流程



![image-20241218092215630](D:\git_repository\cyber_security_learning\markdown_img\image-20241218092215630.png)





Kubernetes 中的 **Pod 关闭流程**（Pod Termination）是一个**多阶段的有序过程**，其目的是在**优雅关闭（Graceful Termination）\**和\**强制删除（Force Deletion）\**之间取得平衡。这个流程涉及\**负载均衡器（Service 代理）、preStop 钩子、API Server、Kubelet、etcd、containerd 和 runc** 等多个组件的协作。



整个流程可分为**5 个主要阶段**：



##### 阶段 1：请求删除 Pod

**发起删除请求**：

- 通过 `kubectl delete pod <pod-name>`，kubectl 向 API Server 发起一个**DELETE 请求**。

- 这时，API Server 会**立即**将 Pod 的**状态标记为 Terminating**。

- API 请求示例：

  ```http
  DELETE /api/v1/namespaces/default/pods/nginx-pod
  ```

**体面终止期（graceful termination period）设置**：

- 当执行 `kubectl delete` 时，可以通过 `--grace-period=<seconds>` 指定**体面终止限期**。

- 如果未指定，默认为 30 秒。

- etcd 存储的状态：

  ```ABAP
  /registry/pods/default/nginx-pod
  {
    "status": {
      "phase": "Terminating"
    }
  }
  ```

**通知 Controller 和 Service**：

- API Server 通过**watch 机制**通知 **Controller Manager** 和 **Service 代理（例如 kube-proxy）**。
- **Service 代理（例如 kube-proxy）**会将 Pod 从 **Endpoints** 中删除，从而不再将流量路由到该 Pod





##### 阶段 2：通知 Kubelet

**Watch 机制通知 Kubelet**：

- API Server 向 Node 上的 Kubelet 发送一个**Pod 变更事件**，标识该 Pod 处于 **Terminating** 状态。

- watch URL：

  ```http
  GET /api/v1/nodes/<node-name>/pods?watch=true
  ```

**Kubelet 处理 Pod 变更**：

- Kubelet 在收到变更事件后，**检查 Pod 的体面终止限期（graceful termination period）**。
- Kubelet 确保 Pod 在**宽限期内停止运行**。
- **注意**：在此期间，Pod 可能仍在运行，直到 **preStop 钩子**和**容器被停止**



##### **阶段 3：执行 preStop 钩子和终止容器**

**执行 preStop 钩子**：

- 如果在 Pod 的 YAML 中定义了**preStop 钩子**，Kubelet 会**同步执行 preStop 钩子**。

- preStop 是**阻塞操作**，即在 preStop 钩子运行完成前，Pod 不会进入终止阶段。

- **！！preStop钩子和SIGTERM同步执行**

- 示例 Pod 定义：

  ```yaml
  lifecycle:
    preStop:
      exec:
        command: ["/bin/sh", "-c", "echo 'Goodbye, world!' > /tmp/goodbye.txt"]
  ```

**停止容器**：

- preStop 钩子执行完毕后，Kubelet 调用 **containerd** 和 **runc** 停止 Pod 中的容器。

- 通过调用 CRI gRPC，Kubelet 执行以下步骤：

  1. **停止信号**：发送**SIGTERM** 信号给 Pod 中的所有容器。
  2. **等待体面终止限期**：等待宽限期（默认 30 秒）内的终止。
  3. 执行 preStop 钩子
  4. **强制终止**：如果超时，Kubelet 会向容器发送**SIGKILL**，强制终止容器。

- 流程摘要：

  ```rust
  Kubelet --> containerd --> runc --> SIGTERM (宽限期)
  Kubelet --> containerd --> runc --> SIGKILL (强制杀死)
  ```



##### **阶段 4：移除 Pod Endpoints（从负载均衡中删除）**

**更新 Service Endpoints**：

- prestop钩子和Kubelet向Pod发送SIGTERM以及通过**Endpoints Controller**和**kube-proxy**将 Pod 从 Service 的 Endpoints 中移除。这三个操作同步执行

- 在体面终止限期的**开始时**，API Server 就会通过**Endpoints Controller**和**kube-proxy**将 Pod 从 Service 的 Endpoints 中移除。
- **原因**：即使 Pod 仍在运行，但为了防止发送到即将被终止的 Pod 的流量，提前将其从流量路径中删除。

**Service 负载均衡更新**：

- kube-proxy 监听 Endpoints 变更（**watch /api/v1/endpoints**）。
- kube-proxy 在 iptables 中**删除相关的规则**，以防止新流量发送到该 Pod。



##### 阶段 5：从 etcd 中删除 Pod

**Kubelet 向 API Server 发送删除请求**：

- 如果 Kubelet 发现 Pod 进程已完全终止（所有容器都已关闭），Kubelet 向 API Server 发送 **DELETE 请求**。

- API 请求示例：

  ```http
  DELETE /api/v1/namespaces/default/pods/nginx-pod
  ```

**API Server 通知 etcd 删除 Pod**：

- API Server 通过 gRPC 调用 etcd 删除与 Pod 相关的

  存储路径：

  ```http
  DELETE /registry/pods/default/nginx-pod
  ```

**从 etcd 中移除 Pod 对象**：

- Pod 对象从 etcd 中被物理删除，所有与之相关的**watch 监听器（Kubelet, Controller, Scheduler）**都会立即收到事件。



##### 总结



**Pod 关闭流程的状态变化**

| **阶段**   | **状态**      | **描述**                                    |
| ---------- | ------------- | ------------------------------------------- |
| **阶段 1** | `Running`     | Pod 处于正常运行状态                        |
| **阶段 2** | `Terminating` | `kubectl delete` 触发了删除事件             |
| **阶段 3** | `Terminating` | 体面终止限期内，preStop 钩子和 SIGTERM 执行 |
| **阶段 4** | `Terminating` | Pod 从 Service 的 Endpoints 中被删除        |
| **阶段 5** | **已删除**    | 体面终止限期结束，Pod 彻底被清除            |



**强制删除（Force Deletion）流程**

**当指定 `--grace-period=0` 时，流程的关键变化如下：**

| **组件**              | **行为变化**         | **解释**                                   |
| --------------------- | -------------------- | ------------------------------------------ |
| **体面终止**          | **跳过**             | 不执行宽限期，直接发出**SIGKILL**          |
| **preStop 钩子**      | **跳过**             | 不会执行 preStop 脚本                      |
| **Service Endpoints** | **立即删除**         | Pod 会立刻被从 Endpoints 中删除            |
| **Pod 终止状态**      | 立即终止             | API Server 将 Pod 立即标记为 `Terminating` |
| **Kubelet 删除**      | **立即发出 SIGKILL** | Kubelet 直接调用 SIGKILL                   |
| **Pod 删除**          | **立即删除**         | Kubelet 直接调用 API Server 删除           |





**关键总结**

1. **优雅终止**：
   - **宽限期**：体面终止限期内，Pod 从 Service 中被移除，接收 SIGTERM，并执行 preStop 钩子。
   - **状态变更**：Running → Terminating → 删除。
   - **删除过程**：当宽限期超时后，Pod 被 SIGKILL 终止，Kubelet 向 API Server 发送删除请求。
2. **强制删除**：
   - **直接跳过宽限期**，不执行 preStop 钩子，立即发送 SIGKILL。
   - **从负载均衡中删除**：立即将 Pod 从 Endpoints 中删除。





#### 设置终止宽限期

```bash
spec.terminationGracePeriod，默认为30s,此值为优雅终止宽限期

#删除命令：kubectl delete pod mypod --grace-period=5
#强制删除：kubectl delete pod mypod --grace-period=0 --force
```



范例

```bash
[root@master1 ~]#kubectl explain pod.spec.terminationGracePeriodSeconds
KIND:     Pod
VERSION: v1
FIELD:   terminationGracePeriodSeconds <integer>
DESCRIPTION:
     Optional duration in seconds the pod needs to terminate gracefully. May be
     decreased in delete request. Value must be non-negative integer. The value
     zero indicates stop immediately via the kill signal (no opportunity to shut
     down). If this value is nil, the default grace period will be used instead.
     The grace period is the duration in seconds after the processes running in
     the pod are sent a termination signal and the time when the processes are
     forcibly halted with a kill signal. Set this value longer than the expected
     cleanup time for your process. Defaults to 30 seconds.
```



示例

```yaml
spec:
 terminationGracePeriodSeconds: 3600  # Pod 级别设置，等价于--grace-period=3600
 containers:
  - name: test
   image: ...
   ports:
    - name: liveness-port
     containerPort: 8080
     hostPort: 8080
   livenessProbe:
     httpGet:
       path: /healthz
         port: liveness-port
       failureThreshold: 1
       periodSeconds: 60
        # 重载 Pod 级别的 terminationGracePeriodSeconds
       terminationGracePeriodSeconds: 60
       
# 解析上述两个terminationGracePeriodSeconds的含义与区别
# 第一个terminationGracePeriodSeconds：决定了Kubelet 在发送 SIGKILL 信号前的等待时间。 -- Pod级别
# 第二个terminationGracePeriodSeconds：在容器重启时生效。触发下列事件时，Kubelet会重启某个特定容器 -- 容器级别
# Liveness 探针失败。
# Kubelet 发现容器状态异常（例如 OOM、CrashLoopBackOff 等）。
# 容器的自我崩溃（containerd 发现容器进程退出）。

# 行为和信号流程：

# Kubelet 发现Liveness 探针失败或容器需要重启。
# Kubelet 向特定的容器发送 SIGTERM 信号。
# Kubelet 等待 terminationGracePeriodSeconds 秒，默认是 30 秒。
# 如果在宽限期内容器未退出，Kubelet 向容器发送 SIGKILL 信号。
# Kubelet 通过 CRI gRPC 请求 containerd 来删除和重启这个容器。
```



##### 特别说明

```ABAP
当 Kubernetes 删除一个 Pod 时，Kubelet 向容器发送 SIGTERM 信号的同时，执行 preStop 钩子。这两个动作是同时触发的。宽限期（grace period）从这两个操作开始时计时，这意味着 preStop 必须在宽限期内完成，否则 Kubelet 会在宽限期结束时直接向容器发送 SIGKILL，不论 preStop 是否完成。

preStop 触发的具体时间点
触发点
preStop 在Kubelet 发送 SIGTERM 的同时触发。
这两个操作（发送 SIGTERM 和 执行 preStop 钩子）是并行的，不依赖彼此。

如果 preStop 未能在宽限期内完成，Kubelet 仍会在宽限期结束后发送 SIGKILL，这会立即终止容器
如果 preStop 本身的逻辑依赖于较长时间的任务（如数据迁移、持久化操作），你需要确保 preStop 钩子在宽限期内完成。
```





#### 两种钩子PostStart和PreStop



根据上面Pod的启动流程，当容器中的进程启动前或者容器中的进程终止之前都会有一些额外的动作执 行，这是由kubelet所设置的，在这里，我们称之为 **pod hook。**



对于Pod的流程启动，主要有两种钩子：

- **postStart**：**容器创建完成后立即运行**，不保证一定会于容器中ENTRYPOINT之前运行,而Init  Container可以实现
- **preStop**：**容器终止操作之前立即运行**，在其完成前会阻塞删除容器的操作调用



##### Poststart钩子

```yaml
# cat pod-poststart.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-poststart
spec:
  containers:
    - name: busybox
      image: busybox:1.32.0
      lifecycle:
        postStart:
          exec:
            command: ["/bin/sh","-c","echo lifecycle poststart at $(date) > /tmp/poststart.log"]
      command: ['sh', '-c', 'echo The app is running at $(date) ! && sleep 3600']
      
# 查看pod执行      
#[root@master1 yaml]#kubectl logs pod-poststart
#The app is running at Wed Dec 18 03:34:41 UTC 2024 !

#[root@master1 yaml]#kubectl exec pod-poststart -- cat /tmp/poststart.log
#lifecycle poststart at Wed Dec 18 03:34:41 UTC 2024
```

```ABAP
基于上述现象，容器启动和PostStart钩子函数执行，几乎是同时的
```



##### Prestop钩子

**功能**：实现pod对象移除之前，需要做一些清理工作，比如:释放资源，解锁等

示例

```yaml
#由于默认情况下，删除的动作和日志我们都没有办法看到，那么我们这里采用一种间接的方法，在删除动作之前，给本地目录创建第一个文件，输入一些内容
# cat pod-prestop.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-prestop
spec:
  volumes:
  - name: vol-prestop
    hostPath:
      path: /tmp
  containers:
  - name: prestop-pod-container
    image: busybox:1.32.0
    volumeMounts:
    - name: vol-prestop
      mountPath: /tmp
    command: ['sh', '-c', 'echo The app is running at $(date) ! && sleep 3600']
    lifecycle:
      postStart:
        exec:
          command: ['/bin/sh', '-c', 'echo lifecycle poststart at $(date) > /tmp/poststart.log']
      preStop:
        exec:
          command: ['/bin/sh', '-c', 'echo lifecycle prestop at $(date) > /tmp/prestop.log']
```



#### Pod状态



##### Pod phase阶段（相位）

![image-20241218141357779](D:\git_repository\cyber_security_learning\markdown_img\image-20241218141357779.png)

| Value     | Description                                                  |
| --------- | ------------------------------------------------------------ |
| Pending   | Pod 已被 Kubernetes 集群接受，但一个或多个容器尚未设置并准备好运行。 这 包括 Pod 等待调度所花费的时间以及通过网络下载容器镜像所花费的时间。 |
| Running   | Pod 已经绑定到一个节点，并且所有的容器都已经创建。 至少有一个容器仍在运 行，或者正在启动或重新启动。 |
| Succeeded | Pod 中的所有容器都已成功终止，并且不会重新启动。             |
| Failed    | Pod 中的所有容器都已终止，并且至少有一个容器因故障而终止。 也就是说，容 器要么以非零状态退出，要么被系统终止。 |
| Unknown   | 由于某种原因，无法获取 Pod 的状态。 此阶段通常是由于与 Pod 应运行的节点通 信时出现错误而发生的。 |





##### Pod 的启动流程状态

| 流程状态        | 描述                              |
| --------------- | --------------------------------- |
| PodScheduled    | Pod被调度到某一个节点             |
| Ready           | 准备就绪，Pod可以处理请求         |
| Initialized     | Pod中所有初始init容器启动完毕     |
| Unschedulable   | 由于资源等限制，导致pod无法被调度 |
| ContainersReady | Pod中所有的容器都启动完毕了       |





##### Pod重启策略（面试题）



**注意：同一个 Pod 内所有容器只能使用统一的重启策略**



| 重启策略  | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| Always    | 无论退出码exit code是否为0，都要重启，即只要退出就重启，并且重启次数并没有限制，此为默认值 |
| OnFailure | 容器终止运行退出码exit code不为0时才重启,重启次数并没有限制  |
| Never     | 无论何种退出码exit code,Pod都不重启。主要针对Job和CronJob    |



示例：

```bash
[root@master1 tmp]#kubectl get pod myapp-pod -o yaml|grep restartPolicy
  restartPolicy: Always
```



#####  Pod 镜像拉取状态（面试题）

| 拉取策略     | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| Always       | 总是拉取新镜像，注意：如果**镜像的Tag为latest**，拉取策略为always或 ifNotPresent 都会重新拉取镜像 |
| IfNotPresent | 此为默认值，如果本地不存在的话，再拉取新镜像，例外情况:如果镜像的Tag为 latest，仍会重新拉取镜像 |
| Never        | 只使用本地的镜像，从不获取新镜像                             |



```bash
[root@master1 tmp]#kubectl get pod myapp-pod -o yaml|grep imagePullPolicy
    imagePullPolicy: IfNotPresent   # 默认值
```





##### Pod状态汇总

| 状态                       | 描述                                                         |
| -------------------------- | ------------------------------------------------------------ |
| Pending                    | APIserver已经创建该pod对象，但是kubelet启动容器之前，都处于Pending状态 |
| Running                    | Pod内所有的容器已创建，且**至少有一个容器处于运行状态**，正 在启动或重启状态 |
| Waiting                    | Pod 等待启动中                                               |
| Terminating                | Pod 正在删除，若超过终止宽限期仍无法删除，可以强制删除 kubectl delete pod  -n --grace-period=0 --force |
| Succeeded                  | 所有容器均成功执行退出，且不会再重启                         |
| Ready                      | Pod 已经准备好,可以提供服务                                  |
| Failed                     | Pod内所有容器都已退出，其中至少有一个容器退出失败            |
| CrashLookBackOff           | 曾经启动Pod成功，但是后来异常情况下，重启次数过多导致异常<br />**终止Pod退避算法**：第1次0秒立刻重启，第二次10秒后重启，第三次 20秒后重启, ... 第6次160秒后重启，第7次300秒后重启，如仍然 重启失败，则为 CrashLookBackOff状态 |
| Error                      | 因为集群配置、安全限制、资源等原因导致Pod 启动过程中发生 了错误 |
| Evicted                    | 集群节点系统**内存或硬盘资源不足**导致Pod出现异常            |
| Completed                  | 表示Pod已经执行完成,比如: **一次性的Job或周期性的CronJob**中 的Pod执行完成后,会显示此状态 |
| Unschedulable              | Pod 不能调度到节点,一般可能是因为没有合适的节点主机          |
| PodScheduled               | Pod 正在被调度过程,但此状态的时间很短                        |
| Initialized                | Pod中所有初始init容器启动完毕                                |
| ImagePullBackOff           | Pod对应的镜像拉取失败                                        |
| InvalidImageName           | 镜像名称无效导致镜像无法下载                                 |
| ImageInspectError          | 镜像检查错误，通常因为镜像不完整                             |
| ErrlmageNeverPull          | 拉取镜像因策略禁止错误，**镜像仓库权限拒绝或私有导致**       |
| RegistryUnavailable        | 镜像仓库服务不可用，比如:网络原因或仓库服务器宕机            |
| ErrImagePull               | 镜像拉取错误，可能是因为超时或拉取被强行终止                 |
| NetworkPluginNotReady      | 网络插件异常,会导致新建容器出错,但旧的容器不受影响           |
| NodeLost                   | Pod所在节点无法联系                                          |
| CreateContainerConfigError | 创建容器配置错误                                             |
| CreateContainerError       | 创建容器错误                                                 |
| RunContainerError          | 运行容器错误，比如:容器中没有PID为1的前台进程等原因          |
| ContainersNotInitialized   | 容器没有初始化完成                                           |
| ContainersNotReady         | 容器没有准备好                                               |
| ContainerCreating          | 容器正在创建过程中                                           |
| PodInitializing            | 容器正在初始化中                                             |
| DockerDaemonNotReady       | 节点的Docker服务异常                                         |
|                            |                                                              |



#### Pod 的健康状态监测



##### Pod的状态监控

实际上，我们需要一种可以及时的获取容器的各种运行状态数据，所以对于容器任务编排的环境下，他们都应该考虑到一种场景：主动的将容器运行的相关数据暴露出来 -- **数据暴露接口**。比如：包含大量 metric指标数据的API接口。



对于kubernetes内部的pod环境来说，常见的这些API接口有：

![image-20241218150953385](D:\git_repository\cyber_security_learning\markdown_img\image-20241218150953385.png)



```bash
process health #状态健康检测接口
readiness #容器可读状态的接口
liveness #容器存活状态的接口
metrics #监控指标接口
tracing #全链路监控的埋点(探针)接口
logs #容器日志接口
```





##### Pod 的健康性监控

Pod 通过**探针**要制实现Pod 健康性监控,当一旦检测出Pod故障时，会**重置Pod**或**将Pod从service后端 endpoint删除**，从而实现服务的高可用



**探针类型**

针对运行中的容器， kubelet 可以选择是否执行以下三种探针，以及如何针对探测结果作出反应



![image-20241218151223781](D:\git_repository\cyber_security_learning\markdown_img\image-20241218151223781.png)

**过程详解**



- 初始刚启动容器的时候，有个初始化时间（**InitialDelaySeconds for Startup Probe**该时间可以自己定义），然后在执行**Startup Probe** Execution
  - 这种可能使用的场景：java程序启动较慢，容器启动时间可能比较长，所以需要容器启动一段时间后，再使用**Startup Probe**进行探测，否则可能容器还未启动成功，Startup Probe就开始探测，会探测失败
  - 而Startup Probe**探测失败**的结果是容器会**立即重启**
  - **Startup Probe只探测一次，探测成功后，后续不会再探测**

- 容器启动成功后，后续会有两个探针Livness Probe和Readiness Probe，在两个探针之前，分别有两个等待时间，即
  - Livness Probe ----- initialDelaySeconds for Liveness Probe
  - Readiness Probe ----- initialDelaySeconds for Readiness Probe
- 如果Liveness Probe检测失败，会重启容器
- 如果Readiness Probe探测失败，不会重启容器，而是将容器从调度列表中移除
  - 用户通常是通过service来访问后端的Pod，如果Readiness Probe检测失败，会将其从Service的列表中移除，但是Pod不会重启
- 如果Liveness Probe检测成功后，会有一个等待的时间，即PeriodSeconds，然后会继续探测，也就是说后续会周期性探测，每过PeriodSeconds时间，会探测一次
- 如果Readiness Probe检测成功，也会有一个等待的事件，即PeriodSeconds，然后会继续探测



##### 配置探针

probe有很多配置字段，可以使用这些字段精确地控制启动，存活和就绪检测的行为

- `initialDelaySeconds`：容器启动后要等到多少秒后，才启动**启动**，**存活**，**就绪**探针，默认是0秒，最小值是0.
- `periodSeconds`：执行探测的时间间隔（单位是秒）。默认是10秒，最小值是1。
- `timeoutSeconds`：探测超时后，等待多少秒。默认值是1秒，最小值是1
- `successThreshold`：探针在失败后，被视为成功的最小连续成功数。默认值是1.存活和启动探测的这个值必须是1，最小值是1
- `failureThreshold`：当探测失败时，Kubernetes的重试次数。对存活探针而言。放弃就意味着重新启动容器
  - 对就绪探针而言，放弃意味着POd会被打上未就绪的标签。默认是3，最小值是1





![image-20241218151415616](D:\git_repository\cyber_security_learning\markdown_img\image-20241218151415616.png)

``````yaml
spec:
  containers:
  - name: string
    image: string
    livenessProbe:
      exec <Object>                    # 命令式探针
      httpGet <Object>                 # http GET类型的探针
      tcpSocket <Object>               # tcp Socket类型的探针
      initialDelaySeconds <integer>    # 发起初次探测请求前的延迟时长，默认为0，生产根据服务起哦多功能时长来设置，比如60s
      periodSeconds <integer>          # 每次探针请求间隔，即探测的周期，默认10s，如果Pod众多，可适当设长，比如60s
      timeoutSeconds <integer>         # 探测的超时时长，默认是1s
      successThreshold <integer>       # 连续成功几次才表示状态正常，默认值是1次，注意：liveness和startup只能是1
      failureThreshold <integer>       # 连续失败几次才表示状态异常，默认值是3次，即从成功变为失败的检查次数
``````



##### 实现探针的三种方式

对于Pod中多容器的场景，只有所有容器就绪，才认为Pod就绪

kubelet 定期执行LivenessProbe和ReadinessProbe探针来诊断Pod的健康状况，Pod探针的实现方式 有很多，常见的有如下三种：

| 监测的实现方式 | 解析                                                         |
| -------------- | ------------------------------------------------------------ |
| Exec           | 直接执行指定的命令，**根据**命令结果的**状态码$?判断是否成功**，成功则返回表示探测成功 |
| TCPSocket      | 根据相应TCP套接字连接建立状态判断,如果**端口能正常打开**，即成功 |
| HTTPGet        | 根据指定Http/Https服务URL的响应码结果判断，当**2xx, 3xx的响应码表示成功** |
| gRPC           | 使用 gRPC 执行一个远程过程调用。 目标应该实现 gRPC健康检查。 如果**响应的状态是 "SERVING"**，则认为诊断成功。 gRPC 探针是一个 Alpha 特性，只有在你启用 了 "GRPCContainerProbe" 特性门控时才能使用 |

![image-20241219155655923](D:\git_repository\cyber_security_learning\markdown_img\image-20241219155655923.png)

##### Exec方式案例

exec 其实就是尝试通过在容器内部来执行一个命令，看看能不能执行成功，如果成功，那么说明该对象 是正常的，否则就是失败的。

范例：startup probe

```yaml
# cat pod-startup-exec.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-startup-exec
  namespace: default
  labels:
    app: pod-startup-exec
spec:
  containers:
  - name: pod-startup-exec-container
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
    startupProbe:
      exec:
        command: ['/bin/sh', '-c', '["`$(curl -s 127.0.0.1/lives)" == "0k" ]']
      initialDelaySeconds: 60
      timeoutSeconds: 1
      periodSeconds: 5
      successThreshold: 1
      failureThreshold: 1
      
# 启动POd
kubectl apply -f pod-startup-exec.yaml

# 查看
[root@master1 yaml]#kubectl get pod 
NAME               READY   STATUS    RESTARTS      AGE
pod-startup-exec   0/1     Running   2 (12s ago)   3m28s

# 解析READY 0/1
# EADY = 当前“处于就绪(Ready)状态的容器数” / Pod 中的总容器数

# 这个pod里的容器里的程序是故意第一次启动会有一个延迟，超过1s,，因为timeoutSeconds: 1，因此会检测失败，unhealthy，导致重启
# 后续会循环重启

# 解决方案：将超时时间改为10
```



范例：livenessProbe

```yaml
# cat pod-liveness-exec-cmd.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-liveness-exec-cmd
  namespace: default
spec:
  containers:
  - name: pod-liveness-exec-cmd-container
    image: busybox:1.32.0
    imagePullPolicy: IfNotPresent
    command: ["/bin/sh", "-c", "touch /tmp/healthy; sleep 3; rm -f /tmp/healthy; sleep 3600"]
    livenessProbe:
      exec:
        command: ["test", "-e", "/tmp/healthy"]
      initialDelaySeconds: 1
      periodSeconds: 3
      
# 创建容器
kubectl apply -f pod-liveness-exec-cmd.yaml

# 实时监控，发现不断重启
[root@master1 yaml]#kubectl get pod pod-liveness-exec-cmd -w
NAME                    READY   STATUS    RESTARTS   AGE
pod-liveness-exec-cmd   1/1     Running   0          22s
pod-liveness-exec-cmd   1/1     Running   1 (1s ago)   55s
pod-liveness-exec-cmd   1/1     Running   2 (5s ago)   101s
pod-liveness-exec-cmd   1/1     Running   3 (1s ago)   2m19s
pod-liveness-exec-cmd   1/1     Running   4 (1s ago)   3m1s
pod-liveness-exec-cmd   1/1     Running   5 (0s ago)   3m42s
pod-liveness-exec-cmd   0/1     CrashLoopBackOff   5 (1s ago)   4m25s
pod-liveness-exec-cmd   1/1     Running            6 (85s ago)   5m49s
pod-liveness-exec-cmd   0/1     CrashLoopBackOff   6 (1s ago)    6m31s
pod-liveness-exec-cmd   1/1     Running            7 (2m50s ago)   9m20s
pod-liveness-exec-cmd   0/1     CrashLoopBackOff   7 (1s ago)      10m
pod-liveness-exec-cmd   1/1     Running            8 (5m5s ago)    15m
pod-liveness-exec-cmd   1/1     Running            9 (1s ago)      15m
pod-liveness-exec-cmd   0/1     CrashLoopBackOff   9 (1s ago)      16m
```



##### Tcpsocket方式案例

使用此配置， kubelet 将尝试在指定端口上打开容器的套接字。如果可以建立连接，容器被认为是健康 的，如果不能就认为是失败的，实际上就是**检查端口**。

对于 TCP 探测而言，kubelet 在节点上（不是在 Pod 里面）发起探测连接， 这意味着你不能在 host 参数上配置服务名称，因为 kubelet 不能解析服务名称。



**liveness的Tcpsocket探针**

```yaml
# cat pod-liveness-tcpsocket.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-liveness-tcpsocket
  namespace: default
spec:
  containers:
  - name: pod-liveness-tcpsocket-container
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
    ports:
    - name: http           # 给指定端口定义别名
      containerPort: 80
    securityContext:       # 添加特权，否则添加iptables规则会提示：getsockopt failed strangely: Operation not permitted
      capabilities:
        add:
        - NET_ADMIN
    livenessProbe:
      tcpSocket:
        port: http        # 引用上面端口的定义
      periodSeconds: 5
      initialDelaySeconds: 5
      
# 注意：由于此镜像应用对外暴露的端口是80端口，所以要探测80端口

# 模拟探测失败，添加防火墙规则，禁止探测
kubectl exec pod-liveness-tcpsocket -- iptables -A INPUT -p tcp --dport 80 -j REJECT

# 查看状态异常
kubectl describe pod pod-liveness-tcpsocket
...
Events:
  Type     Reason     Age               From               Message
  ----     ------     ----              ----               -------
  Normal   Scheduled  98s               default-scheduler  Successfully assigned default/pod-liveness-tcpsocket to node1
  Normal   Pulled     98s               kubelet            Container image "registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1" already present on machine
  Normal   Created    98s               kubelet            Created container pod-liveness-tcpsocket-container
  Normal   Started    97s               kubelet            Started container pod-liveness-tcpsocket-container
  Warning  Unhealthy  3s (x3 over 13s)  kubelet            Liveness probe failed: dial tcp 10.244.1.15:80: connect: connection refused
  Normal   Killing    3s                kubelet            Container pod-liveness-tcpsocket-container failed liveness probe, will be restarted
  
# 注意：livenessProbe探测失败，会重启容器，而重启容器并不是重新创建容器，因此内核相关功能无法重置，也就导致即便重启，防火墙规则仍然在，会导致探测失败，后续不断重启
```



**Readiness的Tcpsocket探针**

```yaml
# cat pod-readiness-tcpsocket.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-readiness-tcpsocket
  labels: 
    app: pod-readiness-tcpsocket
spec:
  containers:
  - name: pod-readiness-tcpsocket-container
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    readinessProbe:
      tcpSocket:
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 10
    livenessProbe:
      tcpSocket:
        port: 80
      initialDelaySeconds: 15
      periodSeconds: 20
---
apiVersion: v1
kind: Service
metadata:
  name: pod-readiness-tcpsocket-svc
spec:
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: pod-readiness-tcpsocket     # 指定上面Pod相同的标签
    
# 查看Service的IP    
[root@master1 yaml]# kubectl get svc
NAME                          TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes                    ClusterIP   10.96.0.1      <none>        443/TCP   25h
pod-readiness-tcpsocket-svc   ClusterIP   10.104.62.95   <none>        80/TCP    8s

# curl 10.104.62.95
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
...


# 将readniessProbe上的探测端口改为8080，因为没有打开8080端口，因此readinessProbe必然失败
# cat pod-readiness-tcpsocket.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-readiness-tcpsocket
  labels: 
    app: pod-readiness-tcpsocket
spec:
  containers:
  - name: pod-readiness-tcpsocket-container
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    readinessProbe:
      tcpSocket:
        port: 8080                 # 改为8080
      initialDelaySeconds: 5
      periodSeconds: 10
    livenessProbe:
      tcpSocket:
        port: 80
      initialDelaySeconds: 15
      periodSeconds: 20
---
apiVersion: v1
kind: Service
metadata:
  name: pod-readiness-tcpsocket-svc
spec:
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: pod-readiness-tcpsocket     # 指定上面Pod相同的标签
    
# 创建资源
[root@master1 yaml]#kubectl apply -f pod-readiness-tcpsocket.yaml 
pod/pod-readiness-tcpsocket created
service/pod-readiness-tcpsocket-svc created

# 查看状态
[root@master1 yaml]#kubectl get pod
NAME                      READY   STATUS    RESTARTS   AGE
pod-readiness-tcpsocket   0/1     Running   0          4s
pod-startup-exec          1/1     Running   0          3h26m

[root@master1 yaml]#kubectl describe pod pod-readiness-tcpsocket 
...
Events:
  Type     Reason     Age               From               Message
  ----     ------     ----              ----               -------
  Normal   Scheduled  25s               default-scheduler  Successfully assigned default/pod-readiness-tcpsocket to node1
  Normal   Pulled     24s               kubelet            Container image "registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0" already present on machine
  Normal   Created    24s               kubelet            Created container pod-readiness-tcpsocket-container
  Normal   Started    24s               kubelet            Started container pod-readiness-tcpsocket-container
  Warning  Unhealthy  4s (x2 over 14s)  kubelet            Readiness probe failed: dial tcp 10.244.1.17:8080: connect: connection refused

# 可以看到Readiness Probe失败
# 观察Service的ep
[root@master1 yaml]#kubectl get ep
NAME                          ENDPOINTS         AGE
kubernetes                    10.0.0.201:6443   25h
pod-readiness-tcpsocket-svc                     41s

# 由于readniessProbe探测失败，因此将Pod从service的endponits列表移除
```



##### HttpGet方式案例

HTTP 探测通过对容器内容开放的web服务，进行http方法的请求探测，如果**探测成功(状态码为2XX和 3XX)**，那么表示http服务是正常的，否则就是失败的。

HTTP Probes 允许针**对 httpGet 配置额外的字段**：

```yaml
#示例:
httpHeaders:
  - name: user_agent
    value: curl

# 其他字段
# host： 连接使用的主机名，默认是 Pod 的 IP。也可以在 HTTP 头中设置 “Host” 来代替。一般不配置此项
# scheme ： 用于设置连接主机的方式（HTTP 还是 HTTPS）。默认是 "HTTP"。一般不配置此项
# path： 访问 HTTP 服务的路径。默认值为 "/"。一般会配置此项
# port： 访问容器的端口号或者端口名。如果数字必须在 1～65535 之间。一般会配置此项
# httpHeaders：请求中自定义的 HTTP 头。HTTP 头字段允许重复。一般不配置此项
```



**Liveness的httpGet探针**

```yaml
# cat pod-liveness-http.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-liveness-http
spec:
  containers:
  - name: pod-liveness-http-container
    image: busybox:1.32.0
    ports:
    - name: http
      containerPort: 80
    livenessProbe:
      httpGet:
        port: http
        path: /index.html
      initialDelaySeconds: 1
      periodSeconds: 3

# 启用容器
kubectl apply -f pod-liveness-http.yaml
pod/pod-liveness-http created
```



 **Readiness 的 httpGet 探针**

通过readiness的属性，尝试判断资源对象是否准备好了相关服务，来接受用户请求。 如果readiness检测失败,相关的service会将此pod从Endpoints中移除,但不会重启pod 

```yaml
# cat pod-readiness-http.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-readiness-http
spec:
  containers:
  - name: pod-readiness-http-container
    image: busybox:1.32.0
    ports:
    - name: http
      containerPort: 80
    readinessProbe:
      httpGet:
        port: http
        path: /index.html
      initialDelaySeconds: 1
      periodSeconds: 3
      
# 创建容器
kubectl apply -f pod-readiness-http.yaml

#实时监控
[root@master1 ~]#kubectl get pod -w
NAME                 READY   STATUS             RESTARTS     AGE
pod-readiness-http   0/1     CrashLoopBackOff   1 (26s ago)   43s
pod-readiness-http   0/1     Completed          2 (32s ago)   49s
```





#### pod资源限制

kubernetes 可以支持在**容器级**及**namespace级**分别实现资源限制



Kubernetes 已经对Pod做了相应的资源配额设置，这些资源主要体现在：CPU和内存、存储，因为存储 在k8s中有专门的资源对象（PV,PVC）来进行管控，所以当前的pod资源限制，主要指的计算资源，即**CPU和内存。**



为了方便与k8s的其他单独的资源对象区分开来，一般将**CPU和内存**其称为**计算资源**。

如果运行的Pod使用的资源超过宿主机的最大可用资源,会导致**OOM**和**Pod驱逐**到其它宿主机



##### 可限制的资源单位

常见在容器级别的CPU和内存的限制



- **CPU**
  - 特点：是一种可压缩资源，cpu资源是支持抢占的
  - 单位：CPU的资源单位是CPU(Core)的数量,是一个绝对
  - 大小：在Kubernetes中通常以千分之一的CPU(Core)为最小单位，用毫 m 表示,即**一个CPU核心表示为1000m**
  - 经验：**一个资源占用不多的容器占用的CPU**通常在100~300m，即**0.1-0.3个CPU**
  - 注意：mi 代表是1024进制的



- **内存**
  - 特点：是不可压缩资源，当pod资源扩展的时候，如果node上资源不够，那么就会发生资源抢占， 或者OOM问题
  - 单位：内存的资源以字节数为单位，是一个绝对值
  - 大小：内存配额对于绝大多数容器来说很重要，在Kubernetes中通常以Mi,Gi为单位来分配。通常 分配置1G,2G,最多16G或32G
  - 注意：如果内存分配不足,可能会出现OOM现象（Java程序常见）



- **注意**
  - CPU属于可压缩（compressible）型资源，即资源额度可按需收缩
  - 内存（当前）则是不可压缩型资源，对其执行收缩操作可能会导致某种程度的问题，例如进程崩溃 等。



- **Extended Resources 扩展资源限制（常见：GPU资源）**
  - 所有不属于kubernetes.io域的资源,为扩展资源,如:"**nvidia.com/gpu**"
  - kubernetes 也支持针到扩展资源限制





##### 配额限制参数

Kubernetes中，对于每种资源的配额限定都需要两个参数：**Requests和Limits**

![image-20241218152631838](D:\git_repository\cyber_security_learning\markdown_img\image-20241218152631838.png)





- **资源需求Requests**
  - 业务运行时资源预留的最小使用量，即所需资源的**最低下限**，**该参数的值必须满足，若不满足，业务无法运行**。
  - 容器运行时可能用不到这些额度的资源，但用到时必须确保有相应数量的资源可用
  - 资源需求的定义会影响调度器的决策,只会将Pod调度至满足所有容器总的资源需求的节点
  - 当资源不足时，**实际使用的资源超出 Requests 的部分，可能会被回收**
  - **不能超过对应的limits值**
  - **不能超过物理节点可用分配的资源值**



- **资源限制 Limits**
  - 运行时资源允许使用最大可用量，即所需资源的最高上限，该参数的值不能被突破，超出该额度的资源使用请求通常会被拒绝
  - **该限制需要大于等于requests的值**，但系统在其某项资源紧张时，会从容器那里回收其使用的超出 其requests值的那部分
  - 针对内存而言,为防止上面回收情况的发生,一般**建议将内存的 Requests 和 Limits 设为相同**
  - 资源限制**Limit**的定义**不影响调度器的决策**
  - 不能低于对应的limits值
  - 可以超过物理节点可用分配的资源值
  - **提示:为保证性能,生产推荐Requests和Limits设置为相同的值**



##### k8s资源查看

要实现资源限制,需要先**安装metrics-server**

```bash
[root@master1 ~]# curl -LO https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

#默认文件需要修改才能工作,因为默认需要内部证书验证和镜像地址k8s.gcr.io所以修改
# vim components.yaml
spec:
      containers:
      - args:
        - --cert-dir=/tmp
        - --secure-port=10250
        - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
        - --kubelet-use-node-status-port
        - --metric-resolution=15s
        - --kubelet-insecure-tls
        #image: registry.cn-hangzhou.aliyuncs.com/google_containers/metricsserver:v0.7.1 # 可以添加国内源
        image: registry.k8s.io/metrics-server/metrics-server:v0.7.2
        imagePullPolicy: IfNotPresent
        livenessProbe:
          failureThreshold: 3
          httpGet:
            path: /livez
            port: https
            scheme: HTTPS
          periodSeconds: 10
        name: metrics-server
        ports:
        - containerPort: 10250
          name: https
          protocol: TCP
          
[root@master1 yaml]# kubectl apply -f components.yaml 
serviceaccount/metrics-server created
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created
clusterrole.rbac.authorization.k8s.io/system:metrics-server created
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created
service/metrics-server created
deployment.apps/metrics-server created
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created


root@master1 yaml]#kubectl get pod -n kube-system metrics-server-b79d5c976-hqrct 
NAME                             READY   STATUS    RESTARTS   AGE
metrics-server-b79d5c976-hqrct   1/1     Running   0          60s
[root@master1 yaml]#kubectl top node
NAME      CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
master1   62m          3%     910Mi           49%       
node1     30m          1%     669Mi           36%       
node2     20m          1%     927Mi           50%       
node3     27m          1%     715Mi           39% 
```



##### 资源限制实现

范例：limits和requests值大小

```yaml
# [root@master1 yaml]# cat pod-limit-request.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-limit-request
spec:
  containers:
  - name: pod-limit-request-container
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        memory: "500Mi"
        cpu: "250m"
      limits:
        memory: "500Mi"
        cpu: "250m"

```



##### 压力测试

```yaml
# cat pod-stress.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-stress
spec:
  containers:
  - name: pod-stress
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/stress-ng
    imagePullPolicy: IfNotPresent
    command: ["/usr/bin/stress-ng", "-c 2", "--metrics-brief"]
    resources:
      requests:
        memory: 128Mi
        cpu: 200m
      limits:
        memory: 256Mi
        cpu: 500m

# 查看
[root@master1 yaml]#kubectl exec pod-stress -- top
Mem: 1853284K used, 120644K free, 4744K shrd, 55064K buff, 832920K cached
CPU:  24% usr   0% sys   0% nic  74% idle   0% io   0% irq   0% sirq
Load average: 0.35 0.30 0.17 3/513 14
  PID  PPID USER     STAT   VSZ %VSZ CPU %CPU COMMAND
    8     1 root     R     6904   0%   1  13% {stress-ng-cpu} /usr/bin/stress-ng
    7     1 root     R     6904   0%   0  12% {stress-ng-cpu} /usr/bin/stress-ng
    1     0 root     S     6264   0%   1   0% /usr/bin/stress-ng -c 2 --metrics-
q   9     0 root     R     1520   0%   0   0% top
```





##### 基于Namespace级别的资源限制

在 **Kubernetes 中基于 Namespace 级别的资源限制**，我们通常使用 **ResourceQuota** 和 **LimitRange** 来实现对命名空间中资源的使用限制。



**资源限制的实现方式**

| **方式**          | **对象**       | **限制类型**                   | **典型限制内容**                             |
| ----------------- | -------------- | ------------------------------ | -------------------------------------------- |
| **ResourceQuota** | **Namespace**  | **命名空间级别的资源总量限制** | 限制 Namespace 中 Pod、CPU、内存、存储的总量 |
| **LimitRange**    | **Pod 和容器** | **单个 Pod/容器的资源限制**    | 限制每个 Pod/容器的 CPU 和内存的最小和最大值 |

------



**资源限制的工作机制**

**1️⃣ ResourceQuota (限制 Namespace 资源总量)**

- **作用范围**：
  限制整个 Namespace 中的资源总量，包括 Pod 数量、CPU、内存和存储。
- **常见的限制项目**：
  - Pod 总数 (`pods`)
  - 容器的总 CPU 请求 (`requests.cpu`) 和总限制 (`limits.cpu`)
  - 容器的总内存请求 (`requests.memory`) 和总限制 (`limits.memory`)
  - PersistentVolumeClaim (PVC) 的总存储使用量 (`requests.storage`)
- **典型场景**：
  限制一个项目团队在其 Namespace 中最多只能使用 10 个 Pod，CPU 总量不超过 10 核，内存总量不超过 32GiB。



**2️⃣ LimitRange (限制单个 Pod 和容器的资源)**

- **作用范围**：
  限制 **每个 Pod 或每个容器** 的 CPU 和内存的最大、最小值。
- **常见的限制项目**：
  - 容器的最小 CPU 请求 (`min.cpu`) 和最大限制 (`max.cpu`)
  - 容器的最小内存请求 (`min.memory`) 和最大限制 (`max.memory`)
- **典型场景**：
  每个 Pod 中的容器都必须请求最少 100m 的 CPU，但最多不能超过 2 核 CPU，最少 200Mi 的内存，最多不能超过 2GiB 的内存。



**ResourceQuota示例（命名空间的资源总量限制）**

限制 **整个命名空间中的 Pod 数量、CPU 和内存使用量**。

```yaml
# cat resource-quota.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: namespace-quota
  namespace: my-namespace
spec:
  hard:
    pods: "10"                    # 限制命名空间中最多有 10 个 Pod
    requests.cpu: "10"            # 所有 Pod 的 CPU 请求总和不能超过 10 核
    requests.memory: "32Gi"       # 所有 Pod 的内存请求总和不能超过 32Gi
    limits.cpu: "20"              # 所有 Pod 中 CPU 限制的总和不能超过 20 核
    limits.memory: "64Gi"         # 所有 Pod 中内存限制的总和不能超过 64Gi
    persistentvolumeclaims: "5"   # 限制 Namespace 中的 PVC 数量为 5 个
    requests.storage: "100Gi"     # 限制所有 PVC 请求的存储总量为 100Gi

```



**LimitRange示例（Pod和容器的资源限制）**

为 **单个 Pod 和容器** 限制其 CPU 和内存的最小值和最大值。

```yaml
cat limit-range.yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: container-limit-range
  namespace: my-namespace
spec:
  limits:
  - type: Pod                # 作用范围为POd
    max:                     # max：指定 Pod 总的 CPU 和内存上限，CPU 不能超过 2 核，内存不能超过 4Gi。
      cpu: "2"               # 每个 Pod 的最大 CPU 限制为 2 核
      memory: "4Gi"          # 每个 Pod 的最大内存限制为 4 GiB
    min:                     # min：指定 Pod 的最小资源请求，CPU 不低于 250m，内存不低于 128Mi。
      cpu: "250m"            # 每个 Pod 的最小 CPU 请求为 250m
      memory: "128Mi"        # 每个 Pod 的最小内存请求为 128Mi
  - type: Container          # type: Container：作用范围为 Pod 内的每个容器
    default:
      cpu: "500m"            # 每个容器的默认 CPU 请求为 500m
      memory: "512Mi"        # 每个容器的默认内存请求为 512Mi
    defaultRequest:
      cpu: "250m"            # 如果未指定请求，默认 CPU 请求为 250m
      memory: "256Mi"        # 如果未指定请求，默认内存请求为 256Mi
    max:
      cpu: "1"               # 每个容器的最大 CPU 限制为 1 核
      memory: "2Gi"          # 每个容器的最大内存限制为 2GiB
    min:
      cpu: "100m"            # 每个容器的最小 CPU 请求为 100m
      memory: "128Mi"        # 每个容器的最小内存请求为 128Mi

```





#### Pod安全

##### 资源安全属性

容器一般是基于6个命名空间实现资源的隔离，而一个 Pod 就是一个容器集合，包含多个容器

这个命名空间是按照下面方式来使用的：

- 内部的所有容器共享底层 pause容器的 UTS，Network 两个名称空间资源
- 可选共享命名空间：IPC，PID
- MNT和USER 两个命名空间默认没有共享,从而实现应用的隔离。



##### 容器安全上下文

pod在其生命周期中，涉及到多种场景(多容器的关联关系)，将这种相关的作用关系称为容器上下文，其 中有一些涉及到权限、限制等安全相关的内容，称其为安全上下文。

安全上下文是一组用于决定容器是如何创建和运行的约束条件，它们代表着创建和运行容器时使用的运行时参数。

它根据约束的作用范围主要包括三个级别：

- Pod级别：针对pod范围内的所有容器
- 容器级别：仅针对pod范围内的指定容器
- PSP级别：PodSecurityPolicy，全局级别的Pod安全策略，涉及到准入控制相关知识



Pod和容器的安全上下文设置主要包括以下几个方面

- 容器进程运行身份及资源访问权限
- Linux Capabilities
- 自主访问控制DAC
- seccomp：securecomputing mode，实现限制程序使用某些系统调用
- AppArmor：Application Armor 与SELinux类似，可以限制程序的功能，比如程序可以读、写或运 行哪些文件，是否可以打开端口等
- SELinux
- Privilege Mode
- Privilege Escalation 特权提升



##### 安全上下文相关属性

```bash
#Pod级安全上下文
~]#kubectl explain pod.spec.securityContext
#容器级安全上下文
~]#kubectl explain pod.spec.containers.securityContext
apiVersion: v1
kind: Pod
metadata: {…}
spec:
 securityContext:                        # Pod级别的安全上下文，对内部所有容器均有效
   runAsUser <integer>                   # 以指定的用户身份运行容器进程，默认由镜像中的USER指定
   runAsGroup <integer>                  # 以指定的用户组运行容器进程，默认使用的组随容器运行时
   supplementalGroups <[]integer>        # 为容器中1号进程的用户添加的附加组；
   fsGroup <integer>                     # 为容器中的1号进程附加的一个专用组，其功能类似于sgid
   runAsNonRoot <boolean>                # 是否以非root身份运行
   seLinuxOptions <Object>               # SELinux的相关配置
   sysctls <[]Object>                    # 应用到当前Pod上的名称或网络空间级别的sysctl参数设置列表
   windowsOptions <Object>               # Windows容器专用的设置
 containers:
  - name: …
   image: …
   securityContext:                      # 容器级别的安全上下文，仅生效于当前容器
     runAsUser <integer>                 # 以指定的用户身份运行容器进程
     runAsGroup <integer>                # 以指定的用户组运行容器进程
     runAsNonRoot <boolean>              # 是否以非root身份运行
     allowPrivilegeEscalation <boolean>  # 是否允许特权升级
     readOnlyRootFilesystem <boolean>    # 是否设置rootfs只读
     capabilities <Object>               # 于当前容器上添加（add）或删除（drop）的操作内核某些资源的能力
       add <[]string>                    # 添加由列表格式定义的各内核能力
       drop <[]string>                   # 移除由列表格式定义的各内核能力
     privileged <boolean>                # 是否运行为特权容器
     procMount <string>                  # 设置容器的procMount类型，默认为DefaultProcMount；
     readOnlyRootFilesystem <boolean>    # 是否将根文件系统设置为只读模式
     seLinuxOptions <Object>             # SELinux的相关配置
     windowsOptions <Object>             # windows容器专用的设置   
     
#注意：上面的属性仅是最常用的属性，而不是所有的属性
```



##### 资源策略

**用户级别**

默认Pod的容器进程是以root身份运行，可以通过下面属性指定其它用户

但此root用户只具有对容器内的相关资源比如文件系统等有管理权限，对于宿主机的内核不具有管理权 限，即是个**“伪"root用户**

相关的属性: 

- runAsUser
- runAsGroup



范例：默认root身份运行Pod内的进程

```yaml
# cat pod-test.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-test
spec:
  containers:
  - name: pod-test
  image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
  
# kubectl apply -f pod-test.yaml

# 查看用户
# kubectl exec pod-test -- id
uid=0(root) gid=0(root) 
groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)

# 注意：默认情况下一旦Pod创建好后，是不允许对用户归属权限进行任意修改的，所以需要修改的话，必须先关闭，再开启
```



范例：添加安全上下文属性实现**指定用户身份运行Pod内进程**

```yaml
# cat pod-securitycontext-runasuser.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-securitycontext-runasuser
  namespace: default
spec:
  containers:
  - name: pod-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
    env:
    - name: PORT
      value: "8080"
    securityContext:
      runasuser: 1001     # 指定运行身份
      runAsGroup: 1001
```



##### 资源能力

在 Linux 中，**root 用户（UID 0）** 默认拥有所有权限，但在容器化环境（如 Kubernetes）中，为了**安全性**，容器默认会剥夺部分 `root` 用户的特权，确保容器无法对宿主机造成威胁。

```bash
CAP_CHOWN                  #改变文件的所有者和所属组   
CAP_MKNOD                  #mknod()，创建设备文件  
CAP_NET_ADMIN              #网络管理权限
CAP_SYS_TIME               #更改系统的时钟
CAP_SYS_MODULE             #装载卸载内核模块
CAP_NET_BIND_SERVER：      #允许普通用户绑定1024以内的特权端口
CAP_SYS_ADMIN              #大部分的管理权限,基本相当于root权
```



范例：默认能力无法直接创建iptables规则

```yaml
# cat pod-securitycontext-capabailities.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-securitycontext-capabilities
  namespace: default
spec:
  containers:
  - name: pod-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
    command: ["/bin/sh", "-c"]
    args: ["/sbin/iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80 && /usr/bin/python3 /usr/local/bin/demo.py"]

# 注意：可以在容器内部通过command + args运行一个自定义的容器启动命令

# 创建资源
kubectl apply -f pod-securitycontext-capabilities.yaml

# 检查效果
kubectl get pod pod-securitycontext-capabilities
NAME                               READY   STATUS   RESTARTS     AGE
pod-securitycontext-capabilities   0/1     Error    2 (30s ago)   67s

[root@master1 ~]#kubectl logs pod-securitycontext-capabilities 
getsockopt failed strangely: Operation not permitted
#结果提示：当容器在启动的时候，默认是以linux系统普通用户启动的，所以普通用户是没有权限更改系统级别的内容的，所以导致我们更改命令权限失败
```



范例：通过添加add指令添加特权

```yaml
# cat pod-securitycontext-capabilities.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-securitycontext-capabilities
  namespace: default
spec:
  containers:
  - name: pod-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
    command: ["/bin/sh", "-c"]
    args: ["/sbin/iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80 && /usr/bin/python3 /usr/local/bin/demo.py"]
    # 添加下面三行
    securityContext:
      capailities:
        add: ['NET_ADMIN']
        
# 注意：add后面的权限能力使用单引号(''),也可以使用双引号("")
```



范例: 使用 drop 指令删除特权

```yaml
# cat pod-securitycontext-capabilities.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-securitycontext-capabilities
  namespace: default
spec:
  containers:
  - name: pod-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
    command: ["/bin/sh", "-c"]
    args: ["/sbin/iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80 && /usr/bin/python3 /usr/local/bin/demo.py"]
    securityContext:
      capabilities:
        add: ['NET_ADMIN']
        drop: ['CHOWN'] # 添加此行
        
# 应用配置
kubectl apply -f pod-securitycontext-capabilities.yaml

# 验证结果
#kubectl exec pod-securitycontext-capabilities   -- chown 1001:1001 /etc/hosts

#kubectl exec pod-securitycontext-capabilities   -- ls -l /etc/hosts
-rw-r--r--    1 root     root           228 Mar 17 07:22 /etc/hosts
#结果显示：文件权限不能随意的更改了
```



##### 添加特权模式：Privileged 模式

在某些场景下，如果需要容器具备**完全的 root 权限**，可以将容器运行在**特权模式**下：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: privileged-pod
spec:
  containers:
  - name: test-container
    image: nginx
    securityContext:
      privileged: true  # 运行在特权模式
```

**注意**：

- `privileged: true` 会授予容器 **所有 Linux 能力**，包括 `SYS_ADMIN`、`NET_ADMIN` 等。
- 特权模式可能会引发**安全风险**，应谨慎使用。



##### 内核参数

**Kubernetes 内核参数管理机制**

Kubernetes 通过 **`sysctl`** 来管理和修改内核参数。由于 `sysctl` 修改的是操作系统内核的全局配置，作用范围是整个 **Linux 命名空间**，因此：

- **Pod 内的所有容器共享相同的内核命名空间**。
- **无法针对单个容器** 修改独立的内核参数，因为同一 Pod 内的容器使用相同的 **Linux 内核命名空间**。



**为什么只能在 Pod 级别修改？**

**原因：命名空间的共享**

在 Kubernetes 中，Pod 是由一组容器组成的，它们共享以下资源：

- **内核命名空间（Kernel Namespace）**：sysctl 参数属于全局或命名空间级别。
- **网络命名空间（Net Namespace）**：Pod 级别的网络栈。
- **PID 命名空间**：Pod 内的所有进程共享 PID 空间。

**影响**

- 如果修改了一个 Pod 的内核参数，那么 Pod 内的所有容器都会受到影响。
- Kubernetes 没有为单个容器提供独立的内核命名空间，因此无法针对单个容器进行内核参数的修改。





**如何在 Pod 级别修改内核参数？**

Kubernetes 提供了 **`sysctl` 支持** 来设置 Pod 级别的内核参数，可以通过 `securityContext` 中的 **`sysctls` 字段** 进行配置。

**示例：Pod 级别修改内核参数**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sysctl-example
spec:
  securityContext:
    sysctls:                # Pod 级别的 sysctl 配置
    - name: net.core.somaxconn
      value: "1024"
    - name: net.ipv4.tcp_syncookies
      value: "1"
  containers:
  - name: nginx
    image: nginx
```

**解释**：

- **`securityContext.sysctls`**：在 Pod 级别设置内核参数。
- 修改的内核参数如 `net.core.somaxconn` 和 `net.ipv4.tcp_syncookies`，会作用于整个 Pod，而非单个容器。



**支持的 sysctl 参数**

Kubernetes 中的 sysctl 参数分为 **安全（safe）** 和 **不安全（unsafe）** 两类：

1. **安全参数**（Safe Sysctls）：

   - 这些参数作用范围限制在 Pod 的网络或 IPC 命名空间内。
   - 示例参数：
     - `net.ipv4.tcp_syncookies`
     - `net.ipv4.ip_unprivileged_port_start`
     - `net.core.somaxconn`
     - `net.ipv4.ping_group_range`

2. **不安全参数**（Unsafe Sysctls）：

   - 这些参数可能影响整个节点，可能会引发安全风险。

   - 需要在 kubelet 启动时添加参数启用：

     ```bash
     kubelet --allowed-unsafe-sysctls='kernel.*,net.*'
     ```





#### Pod服务质量QoS

#### 服务质量分类

QoS（服务质量等级）是作用在Pod上的一个配置

当Kubernetes创建一个Pod时，它就会给这个Pod分配一个QoS等级



QoS三个等级（图例）

![image-20241219100140277](D:\git_repository\cyber_security_learning\markdown_img\image-20241219100140277.png)





- 低优先级BestEffort：没有任何一个容器设置了requests或limits的属性。（最低优先级）
- 中优先级Burstable：Pod至少有一个容器设置了cpu或内存的requests和limits，且不相同

- 高优先级Guaranteed：Pod内的每个容器同时设置了CPU和内存的requests和limits  而且所有值 必须相等



**当主机出现OOM时,先删除服务质量为BestEffort的Pod，然后在删除Burstable，Quaranteed最后被删除**





#### Pod设计模式

##### 容器设计模式

基于容器的分布式系统中常用三类设计模式

- **单容器模式**：单一容器形式运行的应用,此模式应用最为广泛,相当于一个人
- **单节点多容器模式**：由强耦合的多个容器协同共生,容器之间关系密切,通常需要工作在同一个 worker主机上,相当于一个多成员的家庭,**Pod就是此模式的代表**
- **多节点多容器模式**：基于特定部署单元（ Pod）实现分布式算法,通常容器间需要跨网络通信,相当 于多个家庭此模式依赖于应用自身的实现, 例如: MySQL主从复制集群分布在不同节点的Pod





##### 单节点多容器模式



**注意:此处的节点指一个pod,而非worker节点主机**

一种跨容器的设计模式，目的是在**单个Pod之上**同时**运行多个共生关系的容器**，因而容器管理系统需要由将它们作为一个原子单位进行统一调度

**Pod概念就是这个设计模式的实现之一**

一个容器有多个容器,分为两类

- 主容器: 完成主要核心业务
- 辅助容器: 提供辅助功能,比如监控,内核优化,代理等



**单节点多容器模式的常见实现**

辅助容器跟据和主容器的关系,可以由下面几种模式

- **Init Container 模式**
  - Init Container模式只会出现在容器初始化阶段
  - Init容器负责以不同于主容器的生命周期来完成那些必要的初始化任务，包括在文件系统上设置必 要的特殊权限、数据库模式设置或为主应用程序提供初始数据等，但这些初始化逻辑无法包含在应 用程序的镜像文件中，或者出于安全原因，应用程序镜像没有执行初始化活动的权限等等
  - 一个Pod中可以同时定义多个Init容器
  - Init容器需要串行运行，且在**所有Init容器均正常终止后，才能运行主容器**
  - 注意: 此模式用`kubectl get pods` 显示一个Pod只有一个容器



- **Sidecar 模式**
  - Sidecar模式即边车(摩托车的挎斗)模式
  - Pod中的应用由主应用程序（通常是基于HTTP协议的应用程序）以及一个Sidecar的辅助容器组成 Sidecar做为辅助容器用于为主容器提供辅助服务以增强主容器的功能，是主应用程序是必不可少 的一部分，但却未必非得运行为应用的一部分,比如：服务网格的Envoy代理, filebeat 日志收
  - Sidecar容器可以对客户端和主容器之间的所有流量进行干预和监控 
  - 常见应用场景: 为主容器提供代理服务



- **Ambassador 模式**
  - Ambassador模式即大使模式,功能类似一国的大使
  - Pod中的应用由**主应用程序和一个Ambassador容器组成**
  - Ambassador辅助容器代表主容器发送网络请求至特定的外部环境中，因此可以将其视作主容器应 用的“大使”



- **Adapter 模式**
  - Adapter模式即适配器模式
  - Pod中的应用由主应用程序和一个Adapter容器组成，主要为从外部应用向主应用容器访问提供支 持，和Ambassador 模式方向相反
  - Adapter容器为主应用程序提供一致的接口，实现模块重用，支持主容器应用程序的标准化和规范 化输出以便于从外部服务进行访问
  - Adapter容器帮助主容器通信过程中的信息格式修正,将客户端的数据格式转换成主容器能够识别的 数据格式
  - 常见应用场景: 外部prometheus服务通过Adapter 模式的Exporter容器抓取nginx容器的日志,中间 Exporter需要转换两者之间的格式   



##### init模式案例

```yaml
# cat pod-init-container.yaml

apiVersion: v1
kind: Pod
metadata:
  name: pod-init-container
  namespace: default
spec:
  initContainers:
  - name: iptables-init
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/admin-box:v0.1
    imagePullPolicy: IfNotPresent
    command: ['/bin/bash', '-c']
    args: ['iptables -t nat -A -PREROUTING -p tcp --dport 8000 -j REDIRECT --to-port:80']
    securityContext:
      capabilities:
        add:
        - NET_ADMIN
  containers:
  - name: demo
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    ports:
    - name: http
      containerPort: 80
```



##### sidecar模式案例

```yaml
# cat pod-sidecar-test.yaml
apiServer: v1
kind: Pod
metadata:
  name: sidecar-test
spec:
  containers:
  - name: proxy
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/envoy-alpine:v1.14.1
    command: ['sh', '-c', 'sleep 5 && envoy -c /etc/envoy/envoy.yaml']
    lifecycle:
      postStart:
        exec:
          command: ["/bin/sh", "-c", "wget -O /etc/envoy/envoy.yaml http://www.wangxiaochun.com:8888/kubernetes/yaml/envoy.yaml"]
  - name: pod-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    env:
    - name: HOST
      value: "127.0.0.1"
    - name: PORT
      value: "8000"
```





## Kubernetes工作负载



**本章内容**

- **控制器原理**
- **标签和标签选择器**
- **Replica Set**
- **Deployment**
- **DaemonSet**
- **Job**
- **CronJob**



### 控制器原理

#### 资源对象

![image-20241220154542565](D:\git_repository\cyber_security_learning\markdown_img\image-20241220154542565.png)



对于Kubernetes 集群应用来说，所有的程序应用都是

- 运行在 **Pod 资源**对象里面
- 借助于**service资源**对象向外提供服务访问
- 借助于各种**存储资源对象**实现数据的可持久化
- 借助于各种**配置资源对象**实现配置属性、敏感信息的管理操作



#### 应用编排

在工作中为了完成大量的业务目标，首先会根据业务应用内部的关联关系，**把业务拆分成多个子任务**， 然后**对这些子任务进行顺序组合**，当子任务按照方案执行完毕后，就完成了业务目标。

任务编排实现就是对多个子任务的执行顺序进行确定的过程。

对于Kubernetes 来说:

- 对于**紧密相关**的多个子任务，把它们放到**同一个pod内部**
- 对于**非紧密关联**的多个任务，分别放到**不同的pod中**
- 然后借助于**endpoint+service**的方式实现彼此之间的相互调用

- 为了让这些纷乱繁杂的任务能够互相发现，通过集群的 **CoreDNS**组件实现服务注册发现功能。



对于Kubernetes场景中的应用任务，主要存在部署、扩容、缩容、更新、回滚等常见编排操作。

虽然基于pod的方式实现了应用任务的部署功能操作，但是对于自主式的pod来说，它并不能实现其他 的更多编排任务。

因此在Kubernetes集群的核心功能之上，有一群非常重要的组件专用于对pod实现所谓的任务编排功 能，这些组件统统将其称为**控制器Controller**。



**Kubernetes的声明式API**

- 用户能够以声明式定义资源对象的目标状态，即spec字段
- 由控制器代码（机器智能组件）负责确保实际状态，即**status字段与期望状态spec字段一致**
- 控制器相当于“人工智能机器人”，负责确保各项具体任务得以落地，而控制器通常由API的提供者负 责开发编写
- 用户需要做的是根据资源类型及其控制器提供的DSL（领域特定语言）进行声明式编程



**Kubernetes的控制器类型**

- Kubernetes内置控制器：
  - Kubernetes默认就提供的实现基础型、核心型的控制器
  - Controller Manager中内置提供了许多的控制器，例如Service Controller、DeploymentController等
  - 以kube-controller-manager组件的程序方式运行实现
- 第三方控制器
  - 实现高级控制器，通常需要借助于基础型控制器完成其功能
  - 例如Ingress插件ingress-nginx的Controller，网络插件Project Calico的Controller等
  - 通常以Pod形式托管运行于Kubernetes之上，而且这些Pod再由内置的控制器所控制



**控制器种类**

- 节点控制器(Node Controller): 负责在节点出现故障时进行通知和响应
- 任务控制器(Job controller): 监测代表一次性任务的 Job 对象，然后创建 Pods 来运行这些任务直至完成
- 端点控制器(Endpoints Controller): 填充端点(Endpoints)对象(即加入 Service 与 Pod)
- 服务帐户和令牌控制器(Service Account & Token Controllers): 为新的命名空间创建默认帐户和 API 访问令牌



**Kubernetes Controller的控制回路机制**

![image-20241220160056338](D:\git_repository\cyber_security_learning\markdown_img\image-20241220160056338.png)



- Controller根据Spec，控制Systems生成当前实际Status
- Controller借助于Sensor持续监视System的Spec和Status，在每一次控制回路中都会对二者进行 比较
- 确保System的Status不断逼近或完全等同Spec



#### Kubernetes Controller 流程

![image-20241220160149849](D:\git_repository\cyber_security_learning\markdown_img\image-20241220160149849.png)

- 用户向 APIserver中插入一个应用资源对象的请求
- 这个请求包含的数据形态中定义了该资源对象的 "期望"状态
- 数据经由 APIserver 保存到 ETCD 中
- kube-controller-manager 中的各种控制器会监视 Apiserver上与自己相关的资源对象的变动 比如 Pod Controller只负责Pod资源的控制，Service Controller只负责Service资源的控制等。
- 一旦API Server中的资源对象发生变动，对应的Controller执行相关的配置代码，到对应的node节 点上运行
- 该资源对象会在当前节点上，按照用户的"期望"进行运行
- 这些实体对象的运行状态称为 "实际状态"
- 即控制器的作用就是确保 "期望状态" 与 "实际状态" 相一致
- Controller将这些实际的资源对象状态，通过APIServer存储到ETCD的同一个数据条目的status的 字段中
- 资源对象在运行过程中，Controller 会循环的方式向 APIServer 监控 spec 和 status 的值是否一致
- 如果两个状态不一致，那么就指挥node节点的资源进行修改，保证两个状态一致
- 状态一致后，通过APIServer同步更新当前资源对象在ETCD上的数据



### 工作负载资源

工作负载是在 Kubernetes 上运行的应用程序。

为了减轻用户的使用负担，通常不需要用户直接管理每个 Pod 。 而是**使用负载资源来替用户管理 一组 Pod**。 这些负载资源通过对应的配置控制器来确保正确类型的、处于运行状态的 Pod 个数是正确 的，与用户所指定的状态相一致。

以编排Pod化运行的应用为核心的控制器，通常被统称为工作负载型控制器，用于管理与之同名的工作负载型资源类型的资源对象



**Kubernetes 提供若干种内置的工作负载资源：**

- **无状态应用编排**: Deployment 和 ReplicaSet （替换原来的资源 ReplicationController）。 Deployment 很适合用来管理你的集群上的无状态应用， Deployment 中的所有 Pod 都是相互等价的，并且在需要的时候被替换。
- **有状态应用编排**:StatefulSet 让你能够运行一个或者多个以某种方式跟踪应用状态的 Pod。 例如， 如果你的负载会将数据作持久存储，你可以运行一个 StatefulSet ，将每个 Pod 与某个 PersistentVolume 对应起来。你在 StatefulSet 中各个 Pod 内运行的代码可以将数据复制到 同一 StatefulSet 中的其它 Pod 中以提高整体的服务可靠性。
- **系统级应用**:DaemonSet 定义提供节点本地支撑设施的 Pod 。这些 Pod 可能对于你的集群的运维 是 非常重要的，例如作为网络链接的辅助工具或者作为网络 插件 的一部分等等。每次你向集群中 添加一个新节点时，如果该节点与某 DaemonSet 的规约匹配，则控制平面会为该 DaemonSet 调度一个 Pod 到该新节点上运行。
- **作业类应用:**Job 和 CronJob。 定义一些一直运行到结束并停止的任务。 Job 用来执行一次性任 务，而 CronJob 用来执行的根据时间规划反复运行的任务。



| 控制器                | 解析                                                         |
| --------------------- | ------------------------------------------------------------ |
| ReplicationController | 最早期的Pod控制器，目前已被废弃                              |
| RelicaSet             | 副本集，负责管理一个应用(Pod)的多个副本状态                  |
| Deployment            | 它不直接管理Pod，而是借助于ReplicaSet来管理Pod；最常用的无状态应用控制器 |
| DaemonSet             | 守护进程集，用于确保在每个节点仅运行某个应用的一个Pod副本。用于完成系统级任务 |
| Job                   | 有终止期限的一次性作业式任务，而非一直处于运行状态的服务进程 |
| CronJob               | 有终止期限的周期性作业式任务                                 |
| StatefulSet           | 功能类似于Deployment，但StatefulSet专用于编排有状态应用      |

注意：

- 当前主要 apps/v1 版本下的控制器
- 每个控制器对象也需要对应的controller来进行管理



#### **控制器和Pod**

- 控制器主要是通过管理pod来实现任务的编排效果
- 控制器是通过**标签或者标签选择器**找到pod
- 控制器对象仅负责确保API Server上有相应数量的符合标签选择器的Pod对象的定义
- Pod 对象的Status如何与Spec保持一致，则要由相应节点上的kubelet负责保证

![image-20241220162927417](D:\git_repository\cyber_security_learning\markdown_img\image-20241220162927417.png)



#### 节点控制器和Worker节点

![image-20241220163315449](D:\git_repository\cyber_security_learning\markdown_img\image-20241220163315449.png)

- 节点控制器**每间隔5秒检查一次** Worker 节点的状态
- 如果节点控制器没有收到来自Worker 节点的心跳，则将该Worker 节点被标记为**不可达**
- 如果该Worker节点被标记为不可达后,节点控制器再**等待40秒后**仍无法得到此节点的心跳,将该节点 标记为**无法访问**
- 如果该Worker 节点被标记为无法访问后,再**等待5分钟后,**还没有心跳, 节点控制器会**删除当前 Worker节点上面的所有pod,并在其它可用的Worker节点重建这些 pod**





### **标签和标签选择器**

#### 标签说明

Kubernetes通过标签来管理对应或者相关联的各种资源对象，**Label**是kubernetes中的核心概念之一。

Label 不是一个独立的API 资源类型,但Label对象可以关联到各种资源对象上

通过对Label的管理从而达到对相同Label的资源进行分组管理、分配、调度、配置、部署等。

标签Label 是可以附加在任何资源对象上的键值型元数据,即**Label本质上是一个key/value键值对**，其中 key与value由用户自己指定

key键标识由键前缀和键名组成,格式为 **[key_prefix/]key_name**



**`kubectl label`** 命令可管理对象的标签

创建：Label通常在资源对象定义时确定，也可以在对象创建后动态添加或者删除

一个资源对象可以定义多个Label，同一个Label 也可以关联多个资源对象上去



**常用标签使用场景：**

- 版本标签："release" : "stable"，"release" : "canary"，"release" : "beta"
- 环境标签："environment" : "dev"，"environment" : "qa"，"environment" : "prod"
- 应用标签："app" : "ui"，"app" : "as"，"app" : "pc"，"app" : "sc"
- 架构层级标签："tier" : "frontend"，"tier" : "backend", "tier" : "cache"
- 分区标签："partition" : "customerA"，"partition" : "customerB"
- 品控级别标签："track" : "daily"，"track" : "weekly"



#### 管理标签

关于label的创建操作主要有两种：

- 命令行方法
- yaml文件方法



#####  命令行方法

**管理标签：**

```bash
# 添加标签
kubectl label 资源类型 资源名称 label_name=label_value [label_name=label_value] ...

# 修改标签
kubectl label 资源类型 资源名称 label_name=label_value [label_name=label_value] ... --overwrite[=true]

# 删除标签
kubectl label 资源类型 资源名称 label_name- [label_name-] ...

# 参数说明
同时增加多个标签，只需要在后面多写几个就可以了，使用空格隔开
默认情况下，已存在的标签是不能修改的，使用 --overwrite=true 表示强制覆盖
label_name=label_value样式写成 label_name- 即表示删除label
```



**查看标签和指定标签的资源**

```bash
#查看所有标签
kubectl get 资源类型 [资源名称] --show-labels

#示例:
kubectl get pods --show-labels

#查看指定标签的资源
kubectl get pods -l label_name[=label_value]

# 参数：
-l #指定标签条件，获取指定资源对象，=表示匹配，!= 表示不匹配, 如果后面的选择标签有多个的话，使用逗号隔开

# 如果针对标签的值进行范围过滤的话，可以使用如下格式：
-l 'label_name in (value1, value2, value3, ...)'      #包括其中一个label
-l 'label_name notin (value1, value2, value3, ...)'   #不包括其中任何一个label
kube
#是否存在label的判断
-l 'label_name'    #存在label
-l '!label_name'   #不存在label,注意使用单引号.不支持双引号】
```



示例

```bash
# 添加标签
[root@master1 yaml]#kubectl label pod pod-startup-exec type=test
pod/pod-startup-exec labeled

# 查看标签
[root@master1 yaml]#kubectl get pod --show-labels 
NAME               READY   STATUS    RESTARTS   AGE     LABELS
pod-startup-exec   1/1     Running   0          5h51m   app=pod-startup-exec,type=test

# 修改标签
[root@master1 yaml]#kubectl label pod pod-startup-exec type=proc --overwrite
pod/pod-startup-exec labeled

# 查看标签
[root@master1 yaml]#kubectl get pod --show-labels 
NAME               READY   STATUS    RESTARTS   AGE     LABELS
pod-startup-exec   1/1     Running   0          5h52m   app=pod-startup-exec,type=proc

# 删除标签
[root@master1 yaml]#kubectl label pod pod-startup-exec type-
pod/pod-startup-exec unlabeled

# 查看标签
[root@master1 yaml]#kubectl get pod --show-labels 
NAME               READY   STATUS    RESTARTS   AGE     LABELS
pod-startup-exec   1/1     Running   0          5h53m   app=pod-startup-exec
```



##### yaml方法

资源对象 Label 不是一个独立的API资源，需要依附在某些资源对象上才可以

比如：依附在Pod，Service，Deployment 等对象上

初始化Pod资源对象应用时候，在资源对象的元数据metadata属性下添加一条Labels配置：

在特定的属性后面按照指定方式增加内容即可，格式如下：

```YAML
metadata:
  labels:
    key1: value1
    key2: value2
    ......
    
# 注意：labels复数
```



示例：

```yaml
# Label在之前的Pod的资源文件中定义,标签的内容是：app: nginx和 version: v1.20.0
# cat pod-label-nginx.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-label-nginx
  labels:
    app: nginx
    version: v1.20.0
spec:
  containers:
  - name: pod-label-nginx-container
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    
# 查看
[root@master1 yaml]#kubectl get pod --show-labels 
NAME              READY   STATUS    RESTARTS   AGE   LABELS
pod-label-nginx   1/1     Running   0          10s   app=nginx,version=v1.20.0

# 添加新label
[root@master1 yaml]# kubectl label pod pod-label-nginx arch=frontend role=proxy
pod/pod-label-nginx labeled

[root@master1 yaml]# kubectl get pod --show-labels 
NAME              READY   STATUS    RESTARTS   AGE    LABELS
pod-label-nginx   1/1     Running   0          111s   app=nginx,arch=frontend,role=proxy,version=v1.20.0

```



#### 标签选择器

Label附加到Kubernetes集群中的各种资源对象上，目的是对这些资源对象可以进行**后续的分组管理** 而分组管理的核心就是：**标签选择器Label Selector**。

可以通过Label Selector查询和筛选某些特定Label的资源对象，进而可以对他们进行相应的操作管理



**标签选择器的主要应用场景：**

监控具体的Pod、负载均衡调度、定向调度，常用于 Pod、Node等资源对象

**Label Selector**跟Label一样，不能单独定义，必须附加在一些资源对象的定义文件上。一般附加在RS， Deployment 和Service等资源定义文件中。

Label Selector使用时候有两种常见的标签选择算符表达式：**等值**和**集合**



##### 等值和不等值

```bash
# 等值
name = nginx                                   # 匹配所有具有标签name = nginx的资源对象
name == nginx                                  # 同上
name                                           # 表示匹配存在name标签的资源对象

# 不等值
!name                                          # 表示匹配不存在name标签的资源对象
name != nginx                                  # 匹配所有没有name标签或者标签name的值不等于nginx的资源对象

# 示例：pod调度到指定标签的Node节点上
apiVersion: v1
kind: Pod
metadata:
  name: cuda-test
spec:
  containers:
  - name: cuda-test
    image: "registry.k8s.io/cuda-vector-add:v0.1"
    resources:
      limits:
        nvidia.com/gpu: 1
  nodeSelector:
    acclerator: nvidia-tesla-p100
    
# 将所有的有app: myapp标签的pod管理在service下
apiVersion: v1
kind: Service
metadata:
  name: service-loadbalancer-lbaas
spec:
  type: LoadBalancer
  externalTrafficPolicy: Local
  selector:
    app: myapp
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
```



##### 集合

```bash
# 示例
env in (dev, test)                # 匹配所有具有标签 env = dev 或者 env = test的资源对象
name notin (frontend, backent)    # 匹配所有不具有标签name=frontend或者name=backend或者没有name标签的资源对象
```



后续Kubernetes 的集合表达式又增加了两种新的写法：匹配标签、匹配表达式



##### **匹配标签：matchLabels**

```bash
# 匹配标签
matchLabels:
  name: nginx
  app: myapp
  
# 当 matchLabels 中有多个标签时，它们之间的关系是逻辑与（AND）关系

#如下所示：
matchLabels:
 app: frontend
 environment: production
#那么只有那些标签中同时包含 app=frontend 和 environment=production 的资源才会被选中。
```



##### **匹配表达式 matchExpressions**

```bash
#匹配表达式：
   matchExpressions:
      - {key: name, operator: NotIn, values: [frontend]}
#当 matchExpressions 中包含多个标签表达式时，它们之间的关系是逻辑与（AND）关系。

#常见的operator操作属性值有：
   In、NotIn、Exists、NotExists等
   Exists和NotExist时，values必须为空，即 { key: environment, opetator: Exists,values:}
#注意：这些表达式一般应用在RS、RC、Deployment等其它管理对象中。

#示例
matchExpressions:
  - key: environment
    operator: In
    values:
      - production
      - staging
  - key: app
    operator: NotIn
    values:
      - test
#那么只有那些标签满足以下两个条件的资源才会被选中：
- 标签中 environment 的值是 production 或 staging
- 标签中 app 的值不是 test
```



#### 标签选择器操作方式

标签选择器两种方式

- 命令
- 文件



##### 命令方式

```bash
kubectl get TYPE -l SELECTOR1[,SELECTOR2,...]
kubectl get TYPE -l SELECTOR1 [-l SELECTOR2] ...

# 示例：
[root@master1 yaml]#kubectl get node -l ai
NAME    STATUS   ROLES    AGE    VERSION
node1   Ready    <none>   2d2h   v1.30.8
```



##### 配置文件

```yaml
# 基于等值，多个为与关系
selector:
  component: reids
  
# 基于集合
selector:
  matchLabels:
    component: redis
  matchExpressions:
    - key: tier            # 等价 - { key: tier, operator: In, values: [cache] }
      operator: In
      values: [cache]
    - key: environment     # 等价 - { key: environment, operator: NotIn, values: [dev] }
      operator: NotIn
      values: [dev]
```





### Replica Set

####  Replica Set 工作机制

Replica Set 是Pod 最常用的控制器

Replica Set 其实是定义了一个期望的场景，RS有以下特点：

负责编排无状态应用的基础控制器是ReplicaSet，定义编排一个无状态应用相应的资源类型主要的**三个关键属**性如下

- **replicas**：Pod期待的副本数量
- **selector**：筛选目标Pod的标签选择器,支持matchExpressions和matchLabels
- **template**：如果Pod数量不满足预期值，自动创建Pod时候用到的模板(template)，清单文件格式 和自主式Pod一样

意义：自动监控Pod运行的副本数目符合预期，保证Pod高可用的核心组件，常用于Pod的生命周期管理



**工作机制**

- 当通过"资源定义文件"定义好了一个RS资源对象，把它提交到Kubernetes集群
- Master节点上的Controller Manager组件就得到通知
- Controller Manager 根据 ReplicaSet Control Loop 管理 ReplicaSet Object
- 由该对象向API Server请求管理Pod对象(标签选择器选定的）
- 如果没有pod：以**Pod模板**向API Server请求创建Pod对象，由Scheduler调度并绑定至某节点，由相应节点kubelet负责运行
- 定期巡检系统中当前存活的Pod，并确保Pod实例数量刚到满足RC的期望值。
- 如果Pod数量大于RS定义的期望值，那么就杀死一些Pod
- 如果Pod数量小于RS定义的期望值，那么就创建一些Pod
- 所以通过RS资源对象，Kubernetes实现了业务应用集群的高可用性，大大减少了人工干预，提高了管理 的自动化。
- 如果后续想要扩充Pod副本的数量，可以直接修改replicas的值即可
- 当其中一个Node的Pod意外终止，根据RS的定义，Pod的期望值是2，所以会随机找一个Node结点重新 再创建一个新的Pod，来保证整个集群中始终存在两个Pod运行



![image-20241221153308297](D:\git_repository\cyber_security_learning\markdown_img\image-20241221153308297.png)



注意：

- 删除RS并不会影响通过该RS资源对象创建好的Pod。
- 如果要删除所有的Pod那么可以设置RS的replicas的值为0，然后更新该RS。
- 另外kubectl提供了stop和delete命令来一次性删除RS和RS控制的Pod。
- Pod提供的如果无状态服务，不会影响到客户的访问效果。



RS可以实现应用的部署，扩缩容和卸载，但一般很少单独使用，它**主要是被Deployment这个更高层的资源对象所使用**，从而形成了一整套Pod的创建、删除、更新的编排机制。



#### Replica Set 资源清单文件示例

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: ...                                   # ReplicaSet名称，生成的Pod名称以此处的ReplicaSet名称为前缀+随机字符
  namespace: ...
spec:
  minReadySeconds <integer>                   # Pod就绪后多少秒内，Pod任一容器无crash方可视为“就绪”
  replicas <integer>                          # 期望的Pod副本数，默认为1
  selector:                                   # 标签选择器，必须匹配template字段中Pod模版中的标签
    matchExpressions <[]Object>
    matchLabels <map[string]String>
  template:                                   # pod模版对象
    metadata:                                 # pod对象元数据
      labels:                                 # 由模版创建出的Pod对象所拥有的标签，必须要能够匹配前面定义的标签选择器
    spec:                                     # pod规范，格式同自主式Pod
```



#### 创建资源对象

```yaml
# cat controller-replicaset.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: controller-replicaset-test
spec:
  minReadySeconds: 0
  replicas: 3
  selector:
    matchLabels:
      app: rs-test
      release: stable
      version: v1.0
  template:
    metadata:
      labels:
        app: rs-test
        release: stable
        version: v1.0
    spec:
      containers:
      - name: rs-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
        
# 创建
kubectl apply -f controller-replicaset.yaml

# 查看
[root@master1 controller]#kubectl get rs
NAME                         DESIRED   CURRENT   READY   AGE
controller-replicaset-test   3         3         3       50s

[root@master1 controller]#kubectl get pod
NAME                               READY   STATUS    RESTARTS   AGE
controller-replicaset-test-27mmp   1/1     Running   0          57s
controller-replicaset-test-2hf65   1/1     Running   0          57s
controller-replicaset-test-jm29c   1/1     Running   0          57s
pod-label-nginx                    1/1     Running   0          78m
pod-label-nginx2                   1/1     Running   0          50m

```



#### 扩容和缩容

```yaml
# 扩容：调整Pod副本数量更多
# 方法1：修改清单文件
[root@master1 controller]#cat controller-replicaset.yaml 
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: controller-replicaset-test
spec:
  minReadySeconds: 0
  replicas: 4                                    # 修改这里，将其改为4
  selector:
    matchLabels:
      app: rs-test
      release: stable
      version: v1.0
  template:
    metadata:
      labels:
        app: rs-test
        release: stable
        version: v1.0
    spec:
      containers:
      - name: rs-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1

# 查看，数量变为4
[root@master1 controller]#kubectl get po
NAME                               READY   STATUS    RESTARTS   AGE
controller-replicaset-test-27mmp   1/1     Running   0          17m
controller-replicaset-test-2hf65   1/1     Running   0          17m
controller-replicaset-test-85dbn   1/1     Running   0          2m11s
controller-replicaset-test-jm29c   1/1     Running   0          17m


# 命令式，使用命令将其缩减为3个
[root@master1 controller]#kubectl scale --replicas=3 rs/controller-replicaset-test 
replicaset.apps/controller-replicaset-test scaled

# 查看
[root@master1 controller]#kubectl get po
NAME                               READY   STATUS    RESTARTS   AGE
controller-replicaset-test-27mmp   1/1     Running   0          18m
controller-replicaset-test-2hf65   1/1     Running   0          18m
controller-replicaset-test-jm29c   1/1     Running   0          18m
```



更新Pod镜像版本

```yaml
# 升级镜像版本
# 方法1：清单文件
cat controller-replicaset.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: controller-replicaset-test
spec:
  minReadySeconds: 0
  replicas: 6           # 修改此行，原pod版本不变，新pod的版本发生变化，更新为v0.2
  selector:
    matchLabels:
      app: rs-test
      release: stable
      version: v1.0
  template:
    metadata:
      labels:
        app: rs-test
        release: stable
        version: v1.0
    spec:
      containers:
      - name: rs-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2  # 修改此行
```



#### Replica Set 版本发布

##### 滚动发布

```yaml
# 准备service
# cat svc-controller-replicaset.yaml
apiVersion: v1
kind: Service
metadata:
  name: svc-replicaset
spec:
  type: ClusterIP
  selector:
    app: rs-test
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
    
# 准备旧版本的replicaset的清单文件
# cat controller-replicaset-1.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: replicaset-test
spec:
  minReadySeconds: 0
  replicas: 3
  selector:
    matchLabels:
      app: rs-test
      release: stable
      version: v0.1
  template:
    metadata:
      labels:
        app: rs-test
        release: stable
        version: v0.1
    spec:
      containers:
      - name: rs-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1

# 准备新版本的replicaset清单文件
# cat controller-replicaset-2.yaml
apiVersion: apps/v2
kind: ReplicaSet
metadata:
  name: replicaset-test-2
spec:
  minReadySeconds: 0
  replicas: 0                   # 注意此处为0
  selector:
    matchLabels:
      app: rs-test
      release: stable
      version: v0.2
  template:
    metadata:
      labels:
        app: rs-test
        release: stable
        version: v0.2
    spec:
      containers:
      - name: rs-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2

# 启动资源
kubectl apply -f svc-controller-replicaset.yaml
kubectl apply -f controller-replicaset-1.yaml
kubectl apply -f controller-replicaset-2.yaml

# 对旧版的RS缩容，对新版本的RS扩容
[root@master1 controller]# kubectl scale --replicas=2 rs/replicaset-test; kubectl scale --replicas=1 rs/replicaset-test-2
replicaset.apps/replicaset-test scaled
replicaset.apps/replicaset-test-2 scaled

# 观察结果
[root@master1 controller]#kubectl get pod --show-labels 
NAME                      READY   STATUS    RESTARTS      AGE   LABELS
pod-label-nginx           1/1     Running   1 (55m ago)   27h   app=nginx,version=v1.20.0
pod-label-nginx2          1/1     Running   1 (57m ago)   27h   app=nginx,version=v1.20.0
replicaset-test-2-ffh5j   1/1     Running   0             68s   app=rs-test,release=stable,version=v0.2
replicaset-test-2pbdk     1/1     Running   0             11m   app=rs-test,release=stable,version=v0.1
replicaset-test-v8967     1/1     Running   0             11m   app=rs-test,release=stable,version=v0.1


# 再次对旧版的RS缩容,对新版本的RS扩容
[root@master1 controller]#kubectl scale --replicas=1 rs/replicaset-test; kubectl scale --replicas=2 rs/replicaset-test-2
replicaset.apps/replicaset-test scaled
replicaset.apps/replicaset-test-2 scaled

#最后一次对旧版的RS缩容为0,对新版本的RS扩容到3
[root@master1 ~]#kubectl scale --replicas=0 rs/replicaset-test;kubectl scale -- replicas=3 rs/replicaset-test-2

# 上述手动实现滚动升级
```



##### 蓝绿发布

```yaml
# cat controller-replicaset-blue-green.yaml
apiVersion: v1
kind: Service
metadata:
  name: svc-replicaset-blue-green
spec:
  type: ClusterIP
  selector:
    app: rs-test
    ctr: rs-${DEPLOY}
    version: ${VERSION}
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
---
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: rs-${DEPLOY}
spec:
  minReadySeconds: 3
  replicas: 2
  selector:
    matchLabels:
      app: rs-test
      ctr: rs-${DEPLOY}
      version: ${VERSION}
  template:
    metadata:
      labels:
        app: rs-test
        ctr: rs-${DEPLOY}
        version: ${VERSION}
    spec:
      containers:
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:${VERSION}
        
        
# 开启蓝色发布旧版本
[root@master1 controller]#DEPLOY=blue VERSION=v0.1 envsubst < controller-replicaset-blue-green.yaml |kubectl apply -f -
service/svc-replicaset-blue-green created
replicaset.apps/rs-blue created


# 开启测试pod访问Service
[root@master1 controller]#kubectl run pod-$RANDOM --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/admin-box:v0.1 -it --rm --command -- /bin/bash
If you don't see a command prompt, try pressing enter.
root@pod-3326 /# 
root@pod-3326 /# curl svc-replicaset-blue-green
kubernetes pod-test v0.1!! ClientIP: 10.244.2.26, ServerName: rs-blue-qbmlm, ServerIP: 10.244.3.30!
root@pod-3326 /# curl svc-replicaset-blue-green
kubernetes pod-test v0.1!! ClientIP: 10.244.2.26, ServerName: rs-blue-6hkbt, ServerIP: 10.244.1.25!


# 切换至绿色版本
[root@master1 ~]#DEPLOY=green VERSION=v0.2 envsubst < ./yaml/controller/controller-replicaset-blue-green.yaml |kubectl apply -f -
service/svc-replicaset-blue-green configured
replicaset.apps/rs-green created

# 此时在测试pod上进行测试
root@pod-3326 /# curl svc-replicaset-blue-green
kubernetes pod-test v0.2!! ClientIP: 10.244.2.26, ServerName: rs-green-m5psl, ServerIP: 10.244.3.31!
root@pod-3326 /# curl svc-replicaset-blue-green
kubernetes pod-test v0.2!! ClientIP: 10.244.2.26, ServerName: rs-green-hlmxv, ServerIP: 10.244.1.26!

# 已成功切换至v0.2，此时当前k8s上有两套rs
[root@master1 controller]#kubectl get rs
NAME       DESIRED   CURRENT   READY   AGE
rs-blue    2         2         2       5m20s
rs-green   2         2         2       87s

# 上述就是蓝绿发
```



### Deployment

#### **Deployment工作机制**

**Deployment 介绍**

Deployment资源对象一般用于部署**无状态服务**,比如 java应用，Web等，这也是最常用的控制器

可以管理多个副本的Pod, 实现无缝迁移、自动扩容缩容、自动灾难恢复、一键回滚等功能

**Deployment相对于RC或RS的一个最大的升级是:支持滚动发布策略,其它功能几乎一样**

Deployment资源对象在内部使用Replica Set来实现Pod的自动化编排



**Deployment工作流程**

- 创建Deployment资源对象，自动生成对应的Replicas Set并完成Pod的自动管理，而无需人为显示创建 Replicas Set
- 检查Deployment对象状态，检查Pod自动管理效果
- 扩展Deployment资源对象，以应对应用业务的高可用





#### 资源对象 Deployment 和 Replica Set 关系

**Deployment 本质上是依赖并调用 Replica Set 的完成来基本的编排功能，并额外提供了滚动更新，回滚的功能**

- 先由Deployment 创建 Replica Set 资源对象并进行编排
- 再由Replica Set 创建并对 Pod 的编排
- Deployment是建立在ReplicaSet控制器上层的更高级的控制器
- Deployment 位于ReplicaSet更上面一层，基于ReplieaSet，提供了滚动更新、回滚等更为强大的 应用编排功能
- Deployment是 Replica Set 的编排工具，Deployment编排ReplicaSet，ReplicaSet编排Pod
- Replica Set的名称由Deployment名称-Template的Hash值生成
- **Deployment 并不直接管理 Pod**，必须间接的利用 Replica Set 来完成对Pod的编排
- 通常应该直接通过定义Deployment资源来编排Pod应用，而ReplicaSet无须显式配置





#### Deployment 的资源定义

Deployment的定义与Replica Set的定义类似，除了API声明与Kind类型有所区别，其他基本上都一样。

![image-20241222191629314](D:\git_repository\cyber_security_learning\markdown_img\image-20241222191629314.png)



**注意：Deployment对滚动更新多了一些更新策略的功能**

```yaml
apiVersion: apps/v1                 # API群组及版本
kind: Deployment                    # 资源类型特有标识
metadata: 
  name: <string>                    # 资源名称，在作用域中要唯一，生成Pod名称：Deployment + Pod模版Hash + 随机字符串
  namespace: <string>               # 名称空间：Deployment隶属名称空间级别
spec:
  minReadySeconds: <integer>
  replicas: <integer>
  selector: <object>
    matchLabels:
      app: <string>
  template: <object>
  revisionHistoryLimit: <integer>    # 滚动更新历史记录数量，默认为10，如果为0表示不保留历史数据
  strategy: <object>                 # 滚动更新策略
    type: <string>                   # 滚动更新类型，可用值有Recreate（删除所有旧POd再创建新Pod）和RollingUpdate     
    rollingUpdate: <Object>          # 滚动更新类型，专用于RollingUpdate类型，逐步更新，先创建新Pod再逐步删除旧Pod
      maxSurge: <string>             # 更新期间可比期望的POd数量能够多出的最大数量或比例
      maxUnavaiLabel: <String>       # 更新期间可比期望的Pod数量能够缺少的最大数量或比例
  progressDeadlineSeconds: <integer> # 滚动更新故障超时时长，默认为600秒
  paused: <boolean>                  # 是否暂停部署过程
```





#### Deployment实现



**命令行创建对象**

```bash
kubectl create deployment NAME --image=image -- [COMMAND] [args...] [options]
```



**示例**

```bash
# 创建命令
kubectl create deployment deployment-pod-test --image=wangxiaochun/pod-test:v0.1 --replicas=3

# 查看效果
[root@master1 controller]#kubectl get all
NAME                                       READY   STATUS    RESTARTS       AGE
pod/deployment-pod-test-587f5cfffb-btv2w   1/1     Running   0              36s
pod/deployment-pod-test-587f5cfffb-cbkrn   1/1     Running   0              36s
pod/deployment-pod-test-587f5cfffb-ctjvc   1/1     Running   0              36s
......

NAME                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/deployment-pod-test   3/3     3            3           36s

NAME                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/deployment-pod-test-587f5cfffb   3         3         3       36s

# 注意:创建deployment会自动创建相应的RS和POD
# RS的名称=deployment名称+template_hash值
# Pod的名称=deployment名称+replcaset_id+pod_id


# 使用命令查看资源对象格式
[root@master1 controller]# kubectl create deployment myapp --image registry.cn- beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas 3 --dry-run=client -o yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: myapp
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: myapp
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
        name: pod-test
        resources: {}
status: {}
```



**资源定义文件创建对象**

示例

```yaml
# cat controller-deployment-test.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-test
spec:
  replicas: 3
  selector: 
    matchLabels:
      app: rs-test
  template:
    metadata:
      labels:
        app: rs-test
    spec:
      containers:
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
        
# 启动资源清单
[root@master1 controller]#kubectl apply -f controller-deployment-test.yaml 
deployment.apps/deployment-test created

# 查看
[root@master1 controller]#kubectl get deploy
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
deployment-test   3/3     3            3           53s

# 自动生成rs
[root@master1 controller]#kubectl get rs
NAME                         DESIRED   CURRENT   READY   AGE
deployment-test-65495d86f9   3         3         3       95s

# 只要template模版内容变量，就会生成新的rs，因为hash值会变
[root@master1 controller]#cat controller-deployment-test.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-test
spec:
  replicas: 3
  selector: 
    matchLabels:
      app: rs-test
  template:
    metadata:
      labels:
        app: rs-test
    spec:
      containers:
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2        # 这里改为v0.2
      
# 查看：可以看到2个rs      
[root@master1 controller]#kubectl get rs
NAME                         DESIRED   CURRENT   READY   AGE
deployment-test-65495d86f9   0         0         0       10m
deployment-test-79f667698b   3         3         3       18s
```



![image-20241222202019431](D:\git_repository\cyber_security_learning\markdown_img\image-20241222202019431.png)





#### Deployment实现扩容缩容

**基于Deployment调整Pod有两种方法**

```bash
# 基于资源对象调整
kubectl scale  [--current-replicas=<当前副本数>] --replicas=<新副本数> deployment/deploy_name

# 基于资源文件调整
kubectl scale --replicas=<新副本数> -f deploy_name.yaml
```



示例

```bash
[root@master1 controller]#kubectl scale deployment deployment-test --replicas=5
deployment.apps/deployment-test scaled

[root@master1 controller]#kubectl get pod
NAME                               READY   STATUS    RESTARTS       AGE
deployment-test-65495d86f9-4sl7h   1/1     Running   0              2s
deployment-test-65495d86f9-kk28x   1/1     Running   0              3m33s
deployment-test-65495d86f9-qr2mr   1/1     Running   0              3m30s
deployment-test-65495d86f9-rfspr   1/1     Running   0              2s
deployment-test-65495d86f9-tl7sp   1/1     Running   0              3m32s
pod-label-nginx                    1/1     Running   1 (167m ago)   29h
pod-label-nginx2                   1/1     Running   1 (169m ago)   29h
```



#### Deployment动态更新回滚

##### 命令介绍

```bash
# 更新命令1
kubectl set SUBCOMMAND [options] 资源类型 资源名称
SUBCOMMAND：子命令，常用的子命令就是image

# 参数详解
--record=true       # 更改时，会将信息增加到历史记录中

#更新命令2：（用的很少）
kubectl patch (-f FILENAME | TYPE NAME) -p PATCH [options]

#参数详解：
--patch='' #设定对象属性内容

#回滚命令：
kubectl rollout SUBCOMMAND [options] 资源类型 资源名称

SUBCOMMAND 子命令：
history         #显示 rollout 历史,默认只保留最近的10个版本
pause           #标记resource为中止状态，配合resume可实现灰度发布，pause目前仅支持deployment,可配合kubectl set实现批量更新
restart         #重启一个 resource
resume          #继续一个停止的 resource
status          #显示 rollout 的状态
undo            #撤销上一次的 rollout
--revision=n    #查看指定版本的详细信息
--to-revision=0 #rollback至指定版本,默认为0,表示前一个版本
```



##### 案例：命令式更新和回滚

```bash
# 创建deployment
[root@master1 controller]# kubectl create deployment nginx --image registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.18.0
deployment.apps/nginx created


# 修改版本两种格式
#kubectl set image deployment/nginx nginx='registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0' --record=true

# 查看历史kubectl rollout history
[root@master1 controller]#kubectl rollout history deployment nginx
deployment.apps/nginx 
REVISION  CHANGE-CAUSE
1         <none>
2         kubectl set image deployment/nginx nginx=registry.cnbeijing.aliyuncs.com/wangxiaochun/nginx:1.20.0 --record=true

# 撤销/回退上次的更改：注意：只能回退一次
kubectl rollout undo deployment nginx

# 回退到指定版本
kubectl rollout undo --to-revision=2 deployment nginx
```



##### 案例: 基于声明清单文件实现升级和降级

```yaml
# cat controller-deployment-test.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-test
spec:
  replicas: 3
  selector:
    matchLabels:
      app: rs-test
  template:
    metadata:
      labels:
        app: rs-test
    spec:
      containers:
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2        # 直接改这里

# 完成升级
kubectl apply -f controller-deployment-test.yaml
```



##### 批量更新

默认只更改一次就会触发重新生成新Pod可能会影响业务的稳定,可以将多次批量更新合并为只触发一次 重新创建Pod,从而保证业务的稳定

```bash
# 暂停更新
kubectl rollout pause deployment pod-test

# 第一次更改
kubectl set image deployment pod-test pod-test=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2 --record

# 第二次更改
kubectl set resources deployment nginx --limits=cpu=200m,memory=128Mi --requests=cpu=100m,memory=64Mi


# 恢复批量更新
kubectl rollout resume deployment nginx
```





#### Deployment滚动更新策略

Deployment 控制器支持两种更新策略

- **重建式更新 recreate**
  - 当使用Recreate策略时，Deployment会直接**删除全部的旧的Pod**，然后创建新的Pod。
  - 这意味着在部署新版本时，整个应用会停止服务一段时间，直到所有旧的Pod都被删除并且新的 Pod被创建并运行起来。
  - 这可能会导致一段时间内的服务中断，因为旧版本的Pod被直接替换掉了。
  - **此方式可以防止端口冲突**

- **滚动式更新 rolling updates** 
  - 此为默认策略
  - RollingUpdate策略允许在部署新版本时逐步更新Pod。
  - 它会先创建新版本的Pod，然后逐步替换旧版本的Pod，直到所有Pod都已经更新为新版本。
  - 这种方式可以确保应用一直处于可用状态，因为在整个更新过程中，至少有一部分Pod一直在运行。
  - 逐批次更新Pod的方式，支持按百分比或具体的数量定义批次规模
  - 触发条件:
    - **podTemplate的hash码**变动，即仅podTemplate的配置变动才会导致hash码改变
    - replicas和selector的变更不会导致podTemplate的hash变动



**存在的问题**:必须以Pod为最小单位来调整规模比例，而无法实现流量路由比例的控制，比如: 共3个Pod 实现20%流量比例

要实现流量路由比例的控制，就需要使用更高级的工具比如: Ingress 才能实现



**属性解析**

```bash
kubectl explain deployment.spec.strategy

type <string> #主要有两种类型："Recreate"、"RollingUpdate-默认"
Recreate            #重建,先删除旧Pod,再创建新Pod,比如可以防止端口冲突

kubectl explain deployment.spec.strategy.rollingUpdate
rollingUpdate       <Object>
 maxSurge   <string>#更新时允许超过期望值的最大Pod数量或百分比,默认为25%,如果为0,表示先减,再加，此时maxUnavaible不能为0
 maxUnavailabel <string> #更新时允许最大多少个或百分比的Pod不可用,默认为25%,如果为0,表示先加后减，此时maxSurge不能为0
#如果maxSurge为正整数, maxUnavailabel为0,表示先添加新版本的Pod,再删除旧版本的Pod，即先加再减
#如果maxSurge为0, maxUnavaiLabel为正整数,表示先删除旧版本的Pod,再添加新版本的Pod，即先减再加
#如果maxSurge为100%，maxUnavaiLabel为100%，实现蓝绿发布，注意：资源要足够
```



| 属性            | 解析                                                         |
| --------------- | ------------------------------------------------------------ |
| minReadySeconds | Kubernetes在等待设置的时间后才进行升级<br />如果没有设置该值，Kubernetes会假设该容器启动起来后就提供服务了<br />如果没有设置该值，在某些情况下可能会造成服务不正常运行 |
| maxSurge        | 升级过程中Pod最多可比预期值多出的Pod数量，其值可以是0或正整数,或 者相对预期值的百分比<br />默认是25%<br />例如：maxSurage=1，replicas=5,则表示Kubernetes会先启动1一个新的 Pod后才删掉一个旧的POD，整个升级过程中最多会有5+1个Pod。 |
| maxUnavailabel  | 升级过程中最多有多少个Pod处于无法提供服务的状态<br />默认是25%<br />当maxSurge不为0时，该值也不能为0<br />例如：maxUnavaible=1，则表示Kubernetes整个升级过程中最多会有1个 POD处于无法服务的状态。 |



**资源清单文件基本样式**

```yaml
#基本属性样式：
minReadySeconds: 5
strategy:
 type: RollingUpdate
 rollingUpdate:
   maxSurge: 1
   maxUnavaiLabel: 1
```





##### 案例：定制滚动更新文件

```yaml
# cat controller-deployment-rollupdate.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-rolling-update
spec:
  replicas: 6
  selector:
    matchLabels:
      app: pod-test
  template:
    metadata:
      labels:
        app: pod-test
    spec:
      containers:
      - name: pod-rolling-update
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    minReadySeconds: 5
    strategy:
      type: RollingUpdate
      rollingUpdate:
        maxSurge: 1
        maxUnavailable: 1
# 属性解析
minReadySeconds: 5 #表示在更新的时候，需要先等待5秒，而不是一旦发生变化就滚动更新
maxSurge: 1 #定义了在更新期间允许超过期望数量的 Pod 实例,此处表示允许超过期望数量的一个额外的 Pod 实例。
maxUnavaiLabel: 1 #定义了在更新期间允许不可用的最大 Pod 数量。此处表示在更新期间允许最多一个 Pod 不可用。
```



##### 案例：金丝雀发布

```yaml
# cat controller-deployment-rollupdate-canary.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-rolling-update-canary
spec:
  replicas: 3
  selector:
    matchLabels:
      app: pod-test
  template:
    metadata:
      labels:
        app: pod-test
    spec:
      containers:
      - name: pod-rolling-update-canary
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1         # 先加后减
      maxUnavailable: 0
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: pod-test
  name: pod-test
spec:
  ports:
  - name: "80"
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: pod-test
  type: ClusterIP
 
 
# 启动资源清单
[root@master1 controller]#kubectl apply -f controller-deployment-rollupdate-canary.yaml 
deployment.apps/deployment-rolling-update-canary created
service/pod-test created

# 当前状态
[root@master1 controller]#kubectl get pod
NAME                                                READY   STATUS    RESTARTS        AGE
deployment-rolling-update-canary-6794cd6c97-6ljcw   1/1     Running   0               45s
deployment-rolling-update-canary-6794cd6c97-dmsgg   1/1     Running   0               45s
deployment-rolling-update-canary-6794cd6c97-xmjnh   1/1     Running   0               45s

# 升级版本
[root@master1 controller]#sed -i 's/pod-test:v0.1/pod-test:v0.2/' controller-deployment-rollupdate-canary.yaml

# 金丝雀发布
[root@master1 controller]#kubectl apply -f controller-deployment-rollupdate-canary.yaml && kubectl rollout pause deployment deployment-rolling-update-canary
deployment.apps/deployment-rolling-update-canary configured
service/pod-test unchanged
deployment.apps/deployment-rolling-update-canary paused
[root@master1 controller]#kubectl get pod
NAME                                                READY   STATUS    RESTARTS        AGE
deployment-rolling-update-canary-65687cb7cb-b9ghp   1/1     Running   0               4s
deployment-rolling-update-canary-6794cd6c97-6ljcw   1/1     Running   0               3m34s
deployment-rolling-update-canary-6794cd6c97-dmsgg   1/1     Running   0               3m34s
deployment-rolling-update-canary-6794cd6c97-xmjnh   1/1     Running   0               3m34s

# 更新
[root@master1 controller]#kubectl rollout status deployment deployment-rolling-update-canary 
Waiting for deployment "deployment-rolling-update-canary" rollout to finish: 1 out of 3 new replicas have been updated...

# 观察
[root@master1 ~]#while true;do curl 10.103.158.212; sleep 1;done
87cb7cb-b9ghp, ServerIP: 10.244.3.41!
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: deployment-rolling-update-canary-6794cd6c97-6ljcw, ServerIP: 10.244.3.40!
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: deployment-rolling-update-canary-6794cd6c97-6ljcw, ServerIP: 10.244.3.40!
kubernetes pod-test v0.2!! ClientIP: 10.244.0.0, ServerName: deployment-rolling-update-canary-65687cb7cb-b9ghp, ServerIP: 10.244.3.41!
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: deployment-rolling-update-canary-6794cd6c97-dmsgg, ServerIP: 10.244.2.32!
kubernetes pod-test v0.2!! ClientIP: 10.244.0.0, ServerName: deployment-rolling-update-canary-65687cb7cb-b9ghp, ServerIP: 10.244.3.41!
kubernetes pod-test v0.2!! ClientIP: 10.244.0.0, ServerName: deployment-rolling-update-canary-65687cb7cb-b9ghp, ServerIP: 10.244.3.41!
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: deployment-rolling-update-canary-6794cd6c97-6ljcw, ServerIP: 10.244.3.40!


# 确信没问题之后，继续完成一部分更新
[root@master1 controller]#kubectl rollout resume deployment deployment-rolling-update-canary && kubectl rollout pause deployment deployment-rolling-update-canary
deployment.apps/deployment-rolling-update-canary resumed
deployment.apps/deployment-rolling-update-canary paused
```



##### 案例：**模拟蓝绿发布**

```yaml
# cat controller-deployment-rollupdate-bluegreen.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-rolling-update-bluegreen
spec:
  replicas: 3
  selector:
    matchLabels:
      app: pod-test
  template:
    metadata:
      labels:
        app: pod-test
    spec:
      containers:
      - name: pod-rolling-update-bluegreen
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 100%
      maxUnavailable: 100%
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: pod-test
  name: pod-test
spec:
  ports:
  - name: "80"
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: pod-test
  type: ClusterIP
  
  
# 启动资源清单
[root@master1 controller]#kubectl apply -f controller-deployment-rollupdate-bluegreen.yaml 
deployment.apps/deployment-rolling-update-bluegreen created
service/pod-test unchanged

# 查看
[root@master1 controller]#kubectl get pod
NAME                                                   READY   STATUS    RESTARTS        AGE
deployment-rolling-update-bluegreen-854d466b88-d2fk4   1/1     Running   0               4s
deployment-rolling-update-bluegreen-854d466b88-dmpfg   1/1     Running   0               4s
deployment-rolling-update-bluegreen-854d466b88-nmkc4   1/1     Running   0               4s

# 修改版本
[root@master1 controller]#sed -i 's/pod-test:v0.1/pod-test:v0.2/' controller-deployment-rollupdate-bluegreen.yaml 

# 启动并观察结果
[root@master1 controller]#kubectl apply -f controller-deployment-rollupdate-bluegreen.yaml 
deployment.apps/deployment-rolling-update-bluegreen configured
service/pod-test unchanged

# 全部删除，全部换成新版本
[root@master1 controller]#kubectl get pod
NAME                                                   READY   STATUS        RESTARTS        AGE
deployment-rolling-update-bluegreen-5dcf45995c-6srwf   1/1     Running       0               6s
deployment-rolling-update-bluegreen-5dcf45995c-bmcr7   1/1     Running       0               6s
deployment-rolling-update-bluegreen-5dcf45995c-xr5ds   1/1     Running       0               6s
deployment-rolling-update-bluegreen-854d466b88-d2fk4   1/1     Terminating   0               115s
deployment-rolling-update-bluegreen-854d466b88-dmpfg   1/1     Terminating   0               115s
deployment-rolling-update-bluegreen-854d466b88-nmkc4   1/1     Terminating   0               115

# 回退
[root@master1 controller]#kubectl rollout undo deployment deployment-rolling-update-bluegreen 
deployment.apps/deployment-rolling-update-bluegreen rolled back

# 查看状态
[root@master1 controller]#kubectl get pod
NAME                                                   READY   STATUS        RESTARTS        AGE
deployment-rolling-update-bluegreen-5dcf45995c-6srwf   1/1     Terminating   0               70s
deployment-rolling-update-bluegreen-5dcf45995c-bmcr7   1/1     Terminating   0               70s
deployment-rolling-update-bluegreen-5dcf45995c-xr5ds   1/1     Terminating   0               70s
deployment-rolling-update-bluegreen-854d466b88-b2nmw   1/1     Running       0               2s
deployment-rolling-update-bluegreen-854d466b88-nvprx   1/1     Running       0               2s
deployment-rolling-update-bluegreen-854d466b88-rq7nw   1/1     Running       0               2s
```





### DaemonSet



![image-20241223092340014](D:\git_repository\cyber_security_learning\markdown_img\image-20241223092340014.png)



有些情况下，**需要在所有节点都运行一个Pod**，因为Node数量会变化，所以指定Pod的副本数就不合适 了

DaemonSet能够让所有（或者特定）的节点"精确的"运行同一个pod

当节点加入到kubernetes集群中，Pod会被DaemonSet 控制器调度到该节点上运行

当节点从Kubrenetes集群中被移除，被DaemonSet调度的pod也会被移除

如果删除DaemonSet，所有跟这个DaemonSet相关的pods都会被删除

在某种程度上，DaemonSet承担了RS的部分功能，它也能保证相关pods持续运行



**DaemonSet 的一些典型用法**

- 在每个节点上运行集群守护进程
- 在每个节点上运行日志收集守护进程
- 在每个节点上运行监控守护进程



**常用于后台支撑服务**

- Kubernetes集群的系统级应用: kube-proxy,flannel,calico
- 集群存储守护进程，如：ceph，glusterd
- 日志收集服务，如：fluentd，logstash
- 监控服务，如：Prometheus，collectd
- 暴露服务: 如: Ingress nginx



DaemonSet属性解析

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: <string>
  namespace: <string>
spec:
  minReadySeconds: <integer>
  selector: <object>
  template: <object>
  revisionHistoryLimit: <integer>
  updateStrategy: <object>          # 滚动更新策略
    type: <string>                  # 滚动更新类型，OnDelete(删除时更新，手动触发)和RollingUpdate(默认值，滚动更新)
    rollingUpdate: <object>
      maxSurge
      maxUnavailable: <string>
```



官方示例

```yaml
#https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/daemonset/
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
  labels:
    k8s-app: fluentd-logging
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      tolerations:
      # 这些容忍度设置是为了让该守护进程集在控制平面节点上运行
      # 如果你不希望自己的控制平面节点运行Pod，可以删除它们
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
```





**查看当前所有名称空间内的DaemonSet**

```bash
kubectl get ds -A    # -A表示所有名称空间
```



##### DaemonSet案例

```yaml
# cat controller-daemonset-test.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: controller-daemonset-test
spec:
  selector:
    matchLabels:
      app: pod-test
  template:
    metadata:
      labels:
        app: pod-test
    spec:
      # hostNetwork: true #使用宿主机的网络和端口,可以通过宿主机直接访问Pod,性能好,但要防止端口冲突
      #hostPID: true #直接使用宿主机的PID
      containers:
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1


# 查看，每个节点有一个
[root@master1 controller]#kubectl get pod -o wide
NAME                                                   READY   STATUS    RESTARTS      AGE   IP            NODE    NOMINATED NODE   READINESS GATES
controller-daemonset-test-hb2w4                        1/1     Running   0             16s   10.244.2.41   node2   <none>           <none>
controller-daemonset-test-q5zgl                        1/1     Running   0             16s   10.244.3.48   node3   <none>           <none>
controller-daemonset-test-wz55z                        1/1     Running   0             16s   10.244.1.43   node1   <none>           <none>

# daemonset对象也支持滚动更新
kubectl set image daemonsets controller-daemonset-test pod-test='wangxiaochun/pod-test:v0.2' --record=true && kubectl rollout status daemonset controller-daemonset-test

# 注意：daemonset对象不支持pause动作
```



##### 案例：: 在所有节点上部署监控软件prometheus采集指标数据

```yaml
# cat controller-daemonset-prometheus.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: daemonset-demo
  namespace: default
  labels:
    app: prometheus
    component: node-exporter
spec:
  selector:
    matchLabels:
      app: prometheus
      component: node-exporter
  template:
    metadata:
      name: prometheus-node-exporter
      labels:
        app: prometheus
        component: node-exporter
    spec:
      #tolerations:
      #- key: node-role.kubernetes.io/control-plane
      #  operator: Exists
      #  effect: NoSchedule
      #- key: node-role.kubernetes.io/master
      #  operator: Exists
      #  effect: NoSchedule
      containers:
      - image: prom/node-exporter:v1.2.2
        name: prometheus-node-exporter
        ports:
        - name: prom-node-exp
          containerPort: 9100
          #hostPort: 9100
        livenessProbe:
          tcpSocket:
            port: prom-node-exp
          initialDelaySeconds: 3
        readinessProbe:
          httpGet:
            path: '/metrics'
            port: prom-node-exp
            scheme: HTTP
          initialDelaySeconds: 5
      hostNetwork: true
      hostPID: true
```

![image-20241223104118377](D:\git_repository\cyber_security_learning\markdown_img\image-20241223104118377.png)



**案例：仅在指定标签的每个主机上运行一个Pod**

```bash
# 在指定的节点上打便签
[root@master1 yaml]#kubectl label node node1.wang.org node2.wang.org ds=true
node/node1.wang.org labeled
node/node2.wang.org labeled

[root@master1 yaml]#cat controller-daemonset-label-test.yaml 
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: controller-daemonset-label-test
spec:
  selector:
    matchLabels:
      app: pod-test
  template:
    metadata:
      labels:
        app: pod-test
    spec:
      nodeSelector:      # 使用节点标签选择器
        ds: "true"       #指定条件
      containers:
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
```





### Job



#### Job工作机制

在日常的工作中，经常会遇到临时执行一个任务，但是这个任务必须在某个时间点执行才可以

前面的Deployment和DaemonSet主要负责编排始终**持续运行的守护进程类的应用**，并不适合此场景

针对于这种场景，一般使用job的方式来完成任务。



**Job负责编排运行有结束时间的“一次性”任务**

- 控制器要确保Pod内的进程“正常（成功完成任务)”退出
- **非正常退出的Pod可以根据需要重启，并在重试指定的次数后终止**
- Job 可以是单次任务，也可以是在多个Pod分别各自运行一次，实现运行多次（次数通常固定)
- Job 支持同时创建及并行运行多个Pod以加快任务处理速度，Job控制器支持用户自定义其并行度



**关于job的执行主要有两种并行度的类型：**

- **串行 job**：即所有的job任务都在上一个job执行完毕后，再开始执行
- **并行 job**：如果存在多个 job，可以设定并行执行的 job 数量。



Job资源同样需要标签选择器和Pod模板，但它不需要指定replicas，且需要给定**completions**，即需要完成的作业次数，默认为1次

- Job资源会为其Pod对象自动添加“job-name=JOB_NAME”和“controller-uid=UID”标签，并使用标 签选择器完成对controller-uid标签的关联，因此，selector并非必选字段
- Pod的命名格式：$(job-name)-$(index)-$(random-string)，其中的$(index)字段取值与 completions和completionMode有关



**注意**：

- Job 资源是标准的API资源类型
- Job 资源所在群组为“batch/v1”
- Job 资源中，Pod的RestartPolicy的取值只能为**Never**或**OnFailure**



#### job属性解析

```yaml
apiVersion: batch/v1                   # API群组及版本
kind: Job
metadata:
  name: <string>             
  namespace: <string>                  # 名称空间：Job资源隶属名称空间级别
spec:
  selector: <object>                   # 标签选择器，必须匹配template字段中Pod模版中的标签
  suspend: <boolean>                   # 是否挂起当前Job的执行，挂起作业会重置StartTime字段的值
  template: <object>                   # Pod模版对象
  completions: <integer>               # 期望的成功完成的作业次数，成功运行结束的Pod数量，默认1次
  completionMode: <string>             # 追踪Pod完成模式，支持有序的Indexed和无序的NonIndexed（默认）两种
  ttlSecondsAfterFinished: <integer>   # Completed终止状态作业的生存时长，超时将被删除
  parallelism: <integer>               # 作业的最大并行度，默认为1
  backoffLimit: <integer>              # 将作业标记为Failed之前的重试次数，默认为6
  activeDeadlineSeconds: <integer>     # 作业启动后可处于活动状态的时长
```



**并行配置示例**

```yaml
#串行运行共5次任务
spec
  parallelism: 1
  completion: 5
 
#并行2个队列，总共运行6次任务
spec
  parallelism: 2
  completion: 6
```



#### Job案例

##### 示例：单个任务

```yaml
# cat controller-job-single.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: job-single
spec:
  template:
    metadata:
      name: job-single
    spec:
      restartPolicy: Never
      containers:
      - name: job-single
        image: busybox:1.30.0
        command: ["/bin/sh", "-c", "for i in `seq 10 -1 1`; do echo $i; sleep 2; done"]
# 属性解析：job重启策略只有两种，仅支持Never和OnFailure两种，不支持Always,否则的话就成死循环了

# 查看
[root@master1 loadBalancer]#kubectl logs job-single-t58q9 -f --timestamps=true
2024-12-23T03:08:42.128553849Z 10
2024-12-23T03:08:44.131895308Z 9
2024-12-23T03:08:46.132162071Z 8
2024-12-23T03:08:48.132344330Z 7
2024-12-23T03:08:50.132757393Z 6
2024-12-23T03:08:52.133286967Z 5
2024-12-23T03:08:54.133431930Z 4
2024-12-23T03:08:56.134113681Z 3
2024-12-23T03:08:58.134510385Z 2
2024-12-23T03:09:00.134875367Z 1

# 结果显示：job任务执行完毕后，状态是Completed
[root@master1 loadBalancer]#kubectl get pod
NAME                                                   READY   STATUS      RESTARTS       AGE
job-single-t58q9                                       0/1     Completed   0              13m

```



##### 示例：多个串行任务

```yaml
# cat controller-job-multi-serial.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: job-multi-serial
spec:
  completions: 5
  parallelism: 1              # parallelism为1表示串行
  # completionMode: Indexed
  template:
    spec:
      containers:
      - name: job-multi-serial
        image: busybox:1.30.0
        command: ["/bin/sh", "-c", "echo serial job; sleep 3"]
      restartPolicy: OnFailure

# 验证是否串行
# job_list=$(kubectl get pod |sort -k5 | awk '!/^NAME/{print $1}')
[root@master1 loadBalancer] # for i in $job_list ;do kubectl logs $i --timestamps;done
2024-12-23T03:36:53.978861730Z serial job
2024-12-23T03:37:19.492071239Z serial job
2024-12-23T03:37:12.968879900Z serial job
2024-12-23T03:37:06.853185566Z serial job
2024-12-23T03:37:00.775452672Z serial job
#结果显示：这些任务，确实是串行的方式来执行，由于涉及到任务本身是启动和删除，所以时间间隔要大于3s
```



##### 示例：并行任务

```yaml
# cat controller-job-multi-parallel.yaml 
apiVersion: batch/v1
kind: Job
metadata:
  name: job-multi-parallel
spec:
  completions: 6
  parallelism: 2   # #completions/parallelism 如果不能整除,最后一次为剩余的符务数
  ttlSecondsAfterFinished: 3600
  backoffLimit: 3
  activeDeadlineSeconds: 1200
  template:
    spec:
      containers:
      - name: job-multi-parallel
        image: busybox:1.30.0
        command: ["/bin/sh", "-c", "echo parallel job; sleep 3"]
      restartPolicy: OnFailure
      
[root@master1 loadBalancer] # kubectl apply -f controller-job-multi-parallel.yaml 
job.batch/job-multi-parallel created

# 查看Pod
[root@master1 loadBalancer] # kubectl get pod
NAME                       READY   STATUS      RESTARTS   AGE
job-multi-parallel-9mcfj   0/1     Completed   0          42s
job-multi-parallel-cmgjq   0/1     Completed   0          54s
job-multi-parallel-n9kc2   0/1     Completed   0          48s
job-multi-parallel-t7hrz   0/1     Completed   0          54s
job-multi-parallel-vzrrp   0/1     Completed   0          42s
job-multi-parallel-z2bsl   0/1     Completed   0          48s

# 验证结果
[root@master1 loadBalancer] # job_list=$(kubectl get pod |sort -k5 | awk '!/^NAME/{print $1}')
[root@master1 loadBalancer] # for i in $job_list ;do kubectl logs $i --timestamps;done
2024-12-23T03:45:54.982398422Z parallel job
2024-12-23T03:45:54.921097939Z parallel job
2024-12-23T03:45:48.912076981Z parallel job
2024-12-23T03:45:48.908837334Z parallel job
2024-12-23T03:45:42.743753059Z parallel job
2024-12-23T03:45:42.739638339Z parallel job
#结果显示：这6条任务确实是两两并行执行的
```



### CronJob

#### CronJob工作机制

![image-20241223114903445](D:\git_repository\cyber_security_learning\markdown_img\image-20241223114903445.png)



对于**周期性的定时任务**，kubernetes提供了 Cronjob控制器实现任务的编排

CronJob 建立在Job的功能之上，是更高层级的控制器

它以Job控制器完成单批次的任务编排，而后为这种Job作业提供需要运行的周期定义

CronJob其实就是在Job的基础上加上了时间调度，可以在给定的时间点启动一个Pod 来运行任务，也可 以周期性地在给定时间点启动Pod运行任务。

CronJob 被调用的时间是来自于controller-manager的时间,需要确保controller-manager准确

另外CronJob执行时,需要拉取镜像也需要一定的时间,所以可能会导致真正执行的时间不准确 对于没有指定时区的 CronJob，kube-controller-manager 基于本地时区解释排期表（Schedule）

**删除CronJob，同时会级联删除相关的Job和Pod**

一个CronJob对象其实就对应中crontab文件中的一行，它根据配置的时间格式周期性地运行一个Job， 格式和crontab也是相同的

注意：在CronJob中，通配符“?”和“*”的意义相同，它们都表示任何可用的有效值



**Cron 时间表语法**

```bash
# ┌───────────── 分钟 (0 - 59)
# │ ┌───────────── 小时 (0 - 23)
# │ │ ┌───────────── 月的某天 (1 - 31)
# │ │ │ ┌───────────── 月份 (1 - 12)
# │ │ │ │ ┌───────────── 周的某天 (0 - 6)（周日到周一；在某些系统上，7 也是星期日）
# │ │ │ │ │                         或者是 sun，mon，tue，web，thu，fri，sat
# │ │ │ │ │
# │ │ │ │ │
# * * * * *
```



| 输入                   | 描述                         | 相当于    |
| ---------------------- | ---------------------------- | --------- |
| @yearly (or @annually) | 每年 1 月 1 日的午夜运行一次 | 0 0 1 1 * |
| @monthly               | 每月第一天的午夜运行一次     | 0 0 1 * * |
| @weekly                | 每周的周日午夜运行一次       | 0 0 * * 0 |
| @daily (or @midnight)  | 每天午夜运行一次             | 0 0 * * * |
| @hourly                | 每小时的开始一次             | 0 * * * * |



#### CronJob属性解析

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: <string>
  namespace: <string>
spec:
  jobTemplate: <object>
    metadata: <object>
    spec: <object>
  schedule: <string>                   # 调度时间设定，必选字段，格式和Linux的cronjob相同
  concurrencyPolicy: <string>          # 多个Cronjob是否运行并发策略，可用值有Allow,Forbid和Replace
                                       # Allow 允许上一个CronJob没有完成，开始新的一个CronJob开始执行
                                       # Forbid 禁止在上一个CronJob还没完成，就开始新的任务
                                       # Replace 当上一个CronJob没有完成时，杀掉旧任务，用新的任务代替
  failedJobsHistoryLimit: <integer>    # 失败作业的历史记录数，默认为1，建议设置此值稍大一些，方便查看原因
  successfulDeadlineSeconds: <integer> # 成功作业的历史记录数，默认为3
  startingDeadlineSeconds: <integer>   # 因错过时间点而未执行的作业的可超期时长，仍可继续执行
  suspend: <boolean>                   # 是否挂起后续的作业，不影响当前的作业，默认为false
  

# 官方示例
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "* * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox:1.28
            imagePullPolicy: IfNotPresent
            command:
            - /bin/sh
            - -c
            - date; echo Hello from the kubernetes cluster
          restartPolicy: OnFailure
```



#### CronJob案例

##### 示例：单周期任务

```yaml
# cat controller-cronjob-simple.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: cronjob
spec:
  schedule: "*/2 * * * *"   # 每2分钟执行1次
  jobTemplate:
    spec:
      #parallelism: 2       # 两路并行
      #completions: 2
      template:
        spec:
          restartPolicy: OnFailure
          containers:
          - name: cronjob
            image: busybox:1.30.0
            command: ["/bin/sh", "-c", "echo Cron Job"]
            
# 启动
[root@master1 loadBalancer]#kubectl apply -f controller-cronjob-simple.yaml 
cronjob.batch/cronjob created

# 查看cronjob
[root@master1 loadBalancer]#kubectl get cronjobs.batch 
NAME      SCHEDULE      TIMEZONE   SUSPEND   ACTIVE   LAST SCHEDULE   AGE
cronjob   */2 * * * *   <none>     False     0        <none>          13s

# 可以观察到cronjob是周期性创建job
[root@master1 loadBalancer]#kubectl get job
NAME               STATUS     COMPLETIONS   DURATION   AGE
cronjob-28915564   Complete   1/1           3s         2m14s
cronjob-28915566   Complete   1/1           3s         14s

[root@master1 loadBalancer]#kubectl get pod
NAME                     READY   STATUS      RESTARTS   AGE
cronjob-28915564-zx5vh   0/1     Completed   0          2m50s
cronjob-28915566-trj2l   0/1     Completed   0          50s
```





## Kubernetes服务发现



**本章内容**

- **服务访问**
- **服务发现**
- **域名解析**
- **无头服务**





### 服务访问

Kubernetes集群提供了这样的一个资源对象Service，它定义了一组Pod的逻辑集合和一个用于访问它们 的入口策略

Service 可以**基于标签的方式**自动找到对应的pod应用，而无需关心pod的ip地址变化与否，从而实现了 类似负载均衡的效果

Service 本质上就是一个**四层的反向代理**，集群内和外的客户端可以通过如下流程最终实现访问Pod应用

```ABAP
集群内部Client --> service网络 --> Pod网络 --> 容器应用
集群外部Client --> 集群内节点网络 --> service网络 --> Pod网络 --> 容器应用

Kubernetes网络
Pod网络     ----  cni
Service网络 ----  kubeproxy
node网络    ----  宿主机网络
```



Service 资源在master端的Controller组件中，由 Service Controller 来进行统一管理。

service是Kubernetes里最核心的API资源对象之一，它是由coredns或者kube-dns组件提供的功能。

Service 是基于名称空间的资源



Kubernetes 的 Service定义了一个服务的访问入口地址，前端的应用Pod通过Service访问其背后一组有 Pod副本组成的集群实例，Service通过**Label Selector**访问指定的后端Pod，RC保证Service的服务能力和服务质量处于预期状态。



每个Pod都有一个专用的IP地址，加上Pod内部容器的Port端口，就组成了一个访问Pod专用的 EndPoint(Pod IP+Container Port)，从而实现了用户外部资源访问Pod内部应用的效果。

这个EndPoint资源在master端的Controller组件中，由EndPoint Controller 来进行统一管理。

当多个Pod组成了一个业务集群来提供外部服务，那么外部客户端怎么才能访问业务集群服务呢？

![image-20241223144004352](D:\git_repository\cyber_security_learning\markdown_img\image-20241223144004352.png)

根据Pod所处的Node场景，有两种情况：

- 所有Pod副本都在同一Node节点上：对于这种情况，将Node物理节点专用的IP，作为负载均衡器 的VIP，即可实现负载均衡后端服务的效果。
- 所有Pod副本不在同一Node节点上：Node节点的物理ip就没有办法作为负载均衡器的VIP了，这也 是更为常见的情况。



Kubernetes发明了一种设计，给Service分配一个全局唯一的虚拟ip地址--**cluster IP**，它不存在任何网络 设备上，Service通过内部的**标签选择器**，指定相应该Service的Pod资源，当请求发给cluster IP，后端 的Pod资源收到请求后，就会响应请求。

这种情况下，每个Service都有一个全局唯一通信地址，整个系统的内部服务间调用就变成了最基础的 TCP/IP网络通信问题。如果我们的集群内部的服务想要和外部的网络进行通信，可以有多种方法，比 如：

- NodePort类型，通过在所有节点上增加一个对外的端口，用于接入集群外部请求
- ingress类型，通过集群附加服务功能，将外部的域名流量转交到集群内部。



**Service 核心功能**

- 服务发现: 利用标签选择器，在同一个namespace中筛选符合的条件的Pod, 从面实现发现一组提供 了相同服务的Pod
- 负载均衡: Service作为流量入口和负载均衡器，其入口为ClusterIP, 这组筛选出的Pod的IP地址，将 作为该Service的后端服务器
- 名称解析: 利用Cluster DNS，为该组Pod所代表的服务提供一个名称, 在DNS中 对于每个Service， 自动生成一个A、PTR和SRV记录



```ABAP
[root@master1 loadBalancer]#kubectl get svc -A
NAMESPACE     NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
default       kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP                  4d1h
kube-system   kube-dns     ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   4d1h

# 使用10.96.0.1来访问api-server
# 使用10.96.0.10来访问dns，进行域名解析
# 因为在k8s中，core-dns和api-server都是以容器方式存在，本身地址不固定，因此需要借助service进行访问
```



#### Endpoints

当创建 Service资源的时候，最重要的就是为Service指定能够提供服务的标签选择器

Service Controller就会根据标签选择器会自动创建一个同名的**Endpoint**资源对象，Kubernetes新版中还增加了**endpointslices**资源

- Endpoint Controller使用Endpoint的标签选择器(继承自Service标签选择器)，筛选符合条件(包括 符合标签选择器条件和处于Ready 状态)的pod资源
- Endpoint Controller 将符合要求的pod资源绑定到Endpoint上，并告知给Service资源谁可以正常提供服务
- Service 会自动获取一个固定的 **cluster IP**向外提供由Endpoint提供的服务资源
- Service 其实就是为动态的一组 pod 资源对象提供一个固定的访问入口。即 Service实现了后端Pod 应用服务的发现功能 





![image-20241223151136366](D:\git_repository\cyber_security_learning\markdown_img\image-20241223151136366.png)



- 每创建一个Service ,自动创建一个和之同名的API 资源类型 Endpoints
- Endpoints负责维护由相关Service标签选择器匹配的Pod对象
- Endpoints对象上保存Service匹配到的所有Pod的IP和Port信息,称之为端点
- ETCD是K/V数据库, 而一个**Endpoints对象对应一个Key**,所有**后端Pod端点信息为其Value**
- 当一个Endpoints对象对应后端每个Pod的每次变动，都需更新整个Endpoints对象，并将新的 Endpoints对象重新保存至API Server和ETCD
- 此外还需要将该对象同步至每个节点的kube-proxy
- 在ETCD中的对象默认最大为1.5MB,一个Endpoints对象至多可以存储5000个左右的端点信息,这意 味着平均每端点占300KB



#### EndpointSlice

新版Kubernetes为什么需要引用EndpointSlice呢?

![image-20241223151352710](D:\git_repository\cyber_security_learning\markdown_img\image-20241223151352710.png)

- 基于Endpoints机制，即便只有一个Pod的IP等信息发生变动，就需要向集群中的每个节点上的 kube-proxy发送整个endpoints对象
- 比如: 一个由2000个节点组成的集群中，更新一个有5000个Pod IP占用1.5MB空间的Endpoints 对 象，就需要发送3GB的数据
  - 若以滚动更新机制，一次只升级更新一个Pod的信息，这将导致更新这个Endpoints对象需要发送 15T的数据
- EndpointSlice资源通过将Endpoints切分为多片来解决上述问题
- 自Kubernetes v1.16引入EndpointSlice
- 每个端点信息的变动，仅需要更新和发送一个**EndpontSlice对象**,而非整个Endpoints对象
- 每个EndpointSlice默认存储100个端点信息，不会超过 etcd对单个对象的存储限制
- 可在kube-controller-manager程序上使用 **--max-endpoints-per-slice** 选项进行配置
- EndpointSlice并未取代Endpoints，二者同时存在



```bash
# 查看endpoint和endpointslices
[root@master1 loadBalancer]#kubectl get endpointslices -A
NAMESPACE     NAME             ADDRESSTYPE   PORTS        ENDPOINTS                 AGE
default       kubernetes       IPv4          6443         10.0.0.201                4d2h
kube-system   kube-dns-5zfkl   IPv4          9153,53,53   10.244.2.40,10.244.2.38   4d2h
[root@master1 loadBalancer]#kubectl get ep -A
NAMESPACE     NAME         ENDPOINTS                                                  AGE
default       kubernetes   10.0.0.201:6443                                            4d2h
kube-system   kube-dns     10.244.2.38:53,10.244.2.40:53,10.244.2.38:53 + 3 more...   4d2h
```





#### Service访问过程

![image-20241223153657945](D:\git_repository\cyber_security_learning\markdown_img\image-20241223153657945.png)



#### endpoints扩展思路

```ABAP
可以手动创建endpoints，并将集群外资源加入endpoints的队列中，实现集群内的pod访问集群外资源的效果
```



#### Service 工作模型

一个Service对象最终体现为工作节点上的一些**iptables或ipvs规则**，这些规则是由kube-proxy进行实时生成和维护\



**针对某一特定服务，如何将集群中的每个节点都变成其均衡器：**

- 在每个节点上运行一个kube-proxy，由kube-proxy注册监视API Server的Service资源的创建、修 改和删除
- 将Service的定义，转为本地负载均衡功能的落地实现



**kube-proxy将请求代理至相应端点的实现方式有四种：**

- userspace（在kubernetes  v1.2以后淘汰）
- **iptables**： iptables工具，默认模式
- **ipvs**
- nftables: 从kubernetes-v1.29.0 之后版本支持,nft 工具
- kernelspace: 仅Windows使用



这些方法的目的是：kube-proxy如何确保service能在每个节点实现并正常工作

注意: 一个集群只能选择使用一种Mode，即集群中所有节点要使用相同的方式



#### Service和kube-proxy关联关系

![image-20241223160711007](D:\git_repository\cyber_security_learning\markdown_img\image-20241223160711007.png)

- Service作为一个独立的API资源对象，它会在API Service服务中定义出来的
- 在创建任何存在标签选择器的Service时，都会被自动创建一个同名的Endpoints资源，Endpoints  对象会使用Label Selector自动发现后端端点，并各端点的IP配置为可用地址列表的元素
- Service Controller 触发每个节点上的kube-proxy，由kube-proxy实时的转换为本地节点上面的 ipvs/iptables规则。
- 默认情况下，内核中的ipvs或iptables规则，仅仅是负责本地节点用户空间pod客户端发出请求时 的拦截或者转发规则
- 如果Pod客户端向Service发出请求,客户端向内核发出请求，根据ipvs或iptables规则，匹配目标 service
- 如果service匹配，会返回当前service随对应的后端endpoint有哪些
- iptables或ipvs会根据情况挑选一个合适的endpoint地址
  - 如果endpoint是本机上的，则会转发给本机的endpoint
  - 如果endpoint是其他主机上的，则转发给其他主机上的endpoint



#### Service类型

对于Kubernetes 可以实现内部服务的自由通信,也可以将平台内部的服务发布到外部环境

Service主要有四种类型，实现不同的网络通信功能

- ClusterIP
- NodePort
- LoadBalancer
- ExternalName



| 类型         | 解析                                                         |
| ------------ | ------------------------------------------------------------ |
| ClusterIP    | 此为Service的默认类型<br />为**集群内部的客户端访问**,包括节点和Pod等，**外部网络无法访问**<br />In client --> clusterIP: ServicePort (Service) --> PodIP: PodPort |
| NodePort     | 本质上**在ClusterIP模式基础上,再多加了一层端口映射的封装**,相当于增强版的 ClusterIP<br />通过NodeIP:NodePort对外部网络提供服务，默认**随机端口范围30000~32767**, 可指定为固定端口<br />NodePort是一个随机的端口，以防止端口冲突,在**所有安装kube-proxy的节点 上都会打开此相同的端口**<br />可通过访问ClusterIP实现集群内部访问,也可以通过NodeIP:NortPort的方式实 现从集群外部至内部的访问<br />Ex Client --> NodeIP:NodePort (Service) --> PodIP:PodPort |
| LoadBalancer | 基于NodePort基础之上**，使用集群外部的运营商负载均衡器方式实现对外提供** 服务,增强版的NodePort<br/>基于云运营商IaaS云创建一个Kubernetes云，云平台也支持LBaaS(Load Balance as a Service)产品服务<br/>Master借助cloud-manager向LBaaS的API请求动态创建软件LB,即支持和Kubernetes API Server 进行交互<br/>如果没有云服务,将无法获取EXTERNAL-IP,显示Pending状态,则降级为 NodePort类型<br/>Ex Client --> LB_IP:LB_PORT --> NodeIP:NodePort(Service)--> PodIP:PodPort |
| ExternalName | 当Kubernetes集群需要访问集群外部服务时，需要通过externalName**将外部主机引入到集群内部**<br />外部主机名以 DNS方式解析为一个 CNAME记录给Kubernetes集群的其他主机来使用<br />**这种Service既没有ClusterIP，也没有NodePort.而且依赖于内部的CoreDNS功能**<br />In client -->Cluster ServiceName --> CName --> External Service Name |





### ExternalIP

如果有外部 IP 能够路由到一个或多个集群节点上，则 Kubernetes 可以通过 externalIPs 将Service  公开出去。

当网络流量进入集群时，如果 externalIPs 作为目的 IP 地址和端口都与该 Service 匹配， Kubernetes  所配置的规则和路由会确保流量被路由到该 Service 的端点之一。

Service可通过使用节点上配置的辅助IP地址接入集群外部客户端流量

流量入口仅能是配置有该IP地址的节点，其它节点无效，因而此时在节点间无负载均衡的效果

external IP所在的节点故障后，该流量入口失效，除非将该IP地址转移配置到其它节点

定义 Service 时，你可以为任何服务类型externalIPs。

由于 externalIPs 是绑定在某一个节点上,而此节点存在单点问题,可以通过Keepalived等方式实现高可用

**高可用对外解决方案**

```ABAP
ExternalIP + VRRP Keepalived -----> Service -----> Pod
```



#### ExternalIP实现

```yaml
# 创建带externalIPs的service
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 80
  externalIPs:
    - 10.0.0.88   

# 查看
[root@master1 ExternalIP]#kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   4d4h
my-service   ClusterIP   10.108.156.228   10.0.0.88     80/TCP    60s

# 创建deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-test
spec:
  replicas: 3
  selector:
    matchLabels:
      app: rs-test
  template:
    metadata:
      labels:
        app: rs-test
        app.kubernetes.io/name: MyApp
    spec:
      containers:
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1


[root@master1 loadBalancer] #kubectl apply -f controller-deployment-test.yaml 
deployment.apps/deployment-test created

# 查看ep
[root@master1 loadBalancer]#kubectl get ep
NAME         ENDPOINTS                                      AGE
kubernetes   10.0.0.201:6443                                4d4h
my-service   10.244.1.88:80,10.244.2.44:80,10.244.3.99:80   11m

# 在其中一个节点上添加ip
ip a a 10.0.0.88 dev eth0:1

# 验证效果
[root@master1 ExternalIP]#curl 10.0.0.88
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: deployment-test-74b7f7d459-j4fx6, ServerIP: 10.244.2.44!
```



### Service管理



#### 创建 Service 方式说明

对于Service的创建有两种方法：

- 命令行方法
- YAML 文件方法



##### 命令行的方式

```bash
# 创建命令1：（单独创建一个service服务）
kubectl create service [flags] NAME [--tcp=port:targetPort] [--dry-run]

# flags参数详解：
clusterip   Create a ClusterIP service.将集群专用服务接口
nodeport     创建一个 NodePort service.将集群内部服务以端口形式对外提供
loadbalancer 创建一个 LoadBalancer service.主要针对公有云服务
externalname Create an ExternalName service.将集群外部服务引入集群内部

# 创建命令2：（针对一个已存在的deployment、pod、ReplicaSet等创建一个service）
kubectl expose (-f FILENAME | TYPE NAME) [--port=port] [--protocol=TCP|UDP|SCTP] [--target-port=number-or-name] [--name=name] [--external-ip=external-ip-of-service] [--type=type] [options]

# 参数详解
--port=''            #设定service对外的端口信息
--target-port=''     #设定容器的端口,默认和service的端口相同    
--type=''            #设定类型，支持四种：ClusterIP(默认), NodePort, LoadBalancer,ExternalName    
--cluster-ip=''      #设定对外的ClusterIP地址
--name=''            #创建service对外的svc名称

# 创建命令3：（创建自主式Pod时动创建Service）
kubectl run <Pod_name> --image 镜像 --expose --port <容器端口>

# 查看命令
kubectl get svc

# 删除service
kubectl delete svc <svc_name> [ -n <namespace>[] [--all]
```





##### 文件方式

语法解析

```yaml
apiVersion: v1
kind: Service
metadata:
  name: ...
  namespace: ...
  labels:
    key1: value1
    key2: value2
spec:
  type: <string>                    # service类型，默认为ClusterIP
  selector: <map[string]string>     # 指定用于过滤出service所代理的后端pod的标签，指支持等值类型的标签选择器
  ports:                            # Service的端口对象列表
  - name: <string>                  # 端口名称，需要保证唯一性
    protocol: <string>              # 协议，目前仅支持TCP、UDP和SCTP，默认为TCP
    port: <integer>                 # Service端口号
    targetPort: <string>            # 后端Pod的端口号或名称，名称需由Pod中的规范定义
    nodePort: <integer>             # 节点端口号，仅使用NodePort和LoadBalancerl类型，范围：30000-32768，建议系统分配
  - name: <string>
    ...
  clusterIP: <string>               # 指定Service的集群IP，建议不指定而由系统分配
  internalTrafficPolicy: <string>   # 内部流量策略处理方式，Local表示由当前节点处理，Cluster表示向集群范围调度，默认                                         Cluster
  externalTrafficPolicy: <string>   # 外部流量策略处理方式，默认为Cluster，当为Local时，表示由当前节点处理，性能好，但无                                       负载均衡功能，且可以看到客户端真实IP，Cluster表示向集群范围调度，和Local相反，基于                                       性能原因，生产更建议Local，此方式只支持type是NodePort和LoadBalancer类型或者                                         ExternalIps
  loadBalancerIP: <string>          # 外部负载均衡器使用的IP地址，仅适用于LoadBalancer，此字段未来可能删除
  externalName: <string>            # 外部服务名称，该名称将作为Service的DNS CNAME值
  externalIPs: <[]string>           # 群集中的节点将接受此服务的流量的IP地址列表。这些IP不由Kubernetes管理。用户负责确保                                       流量到达具有此 IP 的节点。常见的是不属于 Kubernetes 系统的外部负载均衡器，注意：                                       此IP和Type类型无关
```



#### ClusterIP Service实现

#####  单端口应用

```yaml
# 如果基于资源配置文件创建资源，依赖于后端pod的标签，才可以关联后端的资源
# 准备多个后端Pod对象
[root@master1 loadBalancer] # kubectl create deployment myweb --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas=3
deployment.apps/myweb created

# 查看效果
[root@master1 service] # kubectl get pod --show-labels 
NAME                     READY   STATUS    RESTARTS   AGE     LABELS
myweb-565cb68445-6c928   1/1     Running   0          5m49s   app=myweb,pod-template-hash=565cb68445
myweb-565cb68445-fc6xg   1/1     Running   0          5m49s   app=myweb,pod-template-hash=565cb68445
myweb-565cb68445-rsbs6   1/1     Running   0          5m49s   app=myweb,pod-template-hash=565cb68445


# 创建service对象
[root@master1 service] # vim service-clusterip-test.yaml
apiVersion: v1
kind: Service
metadata: 
  name: service-clusterip-test
spec:
  #type: ClusterIP            # 默认即为ClusterIP，此行可省略
  #clusterIP: 192.168.64.100  #可以手动指定IP，但一般都是系统自动指定而无需添加此行
  selector:
    app: myweb                # 引用上面deployment的名称，同时也是Pod的Lable中的app值
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80

[root@master1 service] # kubectl apply -f service-clusterip-test.yaml 
service/service-clusterip-test created

# 查看
[root@master1 service] # kubectl get svc
NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes               ClusterIP   10.96.0.1        <none>        443/TCP   4d7h
my-service               ClusterIP   10.108.156.228   10.0.0.88     80/TCP    158m
service-clusterip-test   ClusterIP   10.102.58.175    <none>        80/TCP    4s

# 测试
[root@master1 service]# curl 10.102.58.175
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: myweb-565cb68445-rsbs6, ServerIP: 10.244.1.89!

```



##### 多端口实现

有很多服务都会同时开启多个端口，典型的比如：tomcat三个端口，接下来实现创建多端口的Service

```yaml
# 创建多端口Service
[root@master1 service] # vim service-clusterip-multi-port.yaml
apiVersion: v1
kind: Service
metadata:
  name: service-clusterip-multi-port
spec:
  selector:
    app: myweb
  ports:
  - name: http
    protocol: TCP
    port: 80
  - name: https
    protocol: TCP
    port: 443
#关键点：只能有一个ports属性，多了会覆盖,每一个子port必须有一个name属性,由于service是基于标签的方式来管理pod的，所以必须有标签选择器 
```



#### NodePort Service实现

NodePort会在所有节点主机上，向外暴露一个指定或者随机的端口，供集群外部的应用能够访问

注意：nodePort 属性范围为 30000-32767，且type 类型只支持 NodePort或LoadBalancer

**注意: 此方式有安全风险，端口为非标端口,而且性能一般,生产一般较少使用**

**生产中建议使用Ingress方式向外暴露集群内的服务**



##### externaltrafficpolicy 的两种策略

![image-20241223203921088](D:\git_repository\cyber_security_learning\markdown_img\image-20241223203921088.png)

- **cluster模式**
  - 此为默认模式
  - 集群外的请求报文从某节点的NodePort进入，该节点的Service可以将请求流量调度到其他节点上的Pod，无需关心Pod在哪个节点上
  - **Kube-proxy转发外部请求时会替换掉报文的源IP和目标IP,相当于FULLNAT**
  - 返回时需要从原路返回,可能会产生跨节点的跃点转发流量
  - 此模式负载均衡效果好，因为无论容器实例怎么分布在多个节点上，它都会转发过去。
  - 但是由于多了一次转发，性能会损失
  - 如果是NodePort类型,Pod无法获取外部客户端真实客户端IP

![image-20241223204317595](D:\git_repository\cyber_security_learning\markdown_img\image-20241223204317595.png)



- **local模式**
  - 集群外的请求报文从某节点的NodePort进入,该节点的Service 只会将请求流量调度到当前节点上 的Pod
  - **外部请求流量只发给本机的Pod, Kube-proxy转发时只会替换掉报文的目标IP,即只实现DNAT**
  - 即：容器收到的报文，看到源IP地址还是用户的原有 IP  
  - 此模式的负载均衡效果不是很好，因为一旦容器实例分布在多个节点上，它只转发给本机，不产生 跨节点的跃点转发流量。
  - 但是少了一次转发，性能会相对好
  - 由于本机不会跨节点转发报文，所以要想对所有节点上的容器实现负载均衡，就需要借助外部的 Loadbalancer来实现
  - 因此使用Local 模式,一般会使用 LoadBalancer Service 类型结合 Loadbalancer 实现





##### nodePort实现

```yaml
[root@master1 service] # vim service-nodeport.yaml
apiVersion: v1
kind: Service
metadata:
  name: service-nodeport
spec:
  type: NodePort
  #externalTrafficPolicy: Local # 默认值为Cluster,如果是Local只能被当前运行Pod的节点处理流量，并>且可以获取客户端真实IP
  selector:
    app: myweb
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30066   # 指定固定端口(30000-32767)，使用NodePort类型且不指定nodeport，会自动分配随机端口向外暴露

[root@master1 service] # kubectl apply -f service-nodeport.yaml 
service/service-nodeport created

# 查看
[root@master1 service] # kubectl get svc
NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service-nodeport         NodePort    10.104.196.234   <none>        80:30066/TCP   33s

# 默认externalTrafficPolicy: Cluster，所以使用访问集群中任意一个物理节点的地址都可以，但是Pod上看不到真实客户端地址
[root@master1 service]#curl 10.0.0.202:30066
kubernetes pod-test v0.1!! ClientIP: 10.244.1.0, ServerName: myweb-565cb68445-6c928, ServerIP: 10.244.2.46!
[root@master1 service]#curl 10.0.0.202:30066
kubernetes pod-test v0.1!! ClientIP: 10.244.1.1, ServerName: myweb-565cb68445-rsbs6, ServerIP: 10.244.1.90!
[root@master1 service]#curl 10.0.0.202:30066
kubernetes pod-test v0.1!! ClientIP: 10.244.1.0, ServerName: myweb-565cb68445-fc6xg, ServerIP: 10.244.3.101!
[root@master1 

# 指定externalTrafficPolicy: Local，Pod能看到客户端真实IP，同时每个节点只能调度该节点上的Pod
[root@master1 service] #curl 10.0.0.202:30066
kubernetes pod-test v0.1!! ClientIP: 10.0.0.201, ServerName: myweb-565cb68445-rsbs6, ServerIP: 10.244.1.90!
[root@master1 service] #curl 10.0.0.202:30066
kubernetes pod-test v0.1!! ClientIP: 10.0.0.201, ServerName: myweb-565cb68445-rsbs6, ServerIP: 10.244.1.90!
[root@master1 service] #curl 10.0.0.202:30066
kubernetes pod-test v0.1!! ClientIP: 10.0.0.201, ServerName: myweb-565cb68445-rsbs6, ServerIP: 10.244.1.90!
[root@master1 service] #curl 10.0.0.203:30066
kubernetes pod-test v0.1!! ClientIP: 10.0.0.201, ServerName: myweb-565cb68445-6c928, ServerIP: 10.244.2.46!
[root@master1 service] #curl 10.0.0.203:30066
kubernetes pod-test v0.1!! ClientIP: 10.0.0.201, ServerName: myweb-565cb68445-6c928, ServerIP: 10.244.2.46!
[root@master1 service] #curl 10.0.0.203:30066
kubernetes pod-test v0.1!! ClientIP: 10.0.0.201, ServerName: myweb-565cb68445-6c928, ServerIP: 10.244.2.46!

# 将deploy缩容至1
[root@master1 service] #kubectl scale deployment myweb --replicas=1
deployment.apps/myweb scaled

# 查看
[root@master1 service]#kubectl get pod -o wide
NAME                     READY   STATUS    RESTARTS      AGE   IP             NODE    NOMINATED NODE   READINESS GATES
myweb-565cb68445-fc6xg   1/1     Running   1 (17m ago)   13h   10.244.3.101   node3   <none>           <none>

# 访问node1上的端口
[root@master1 service]#curl 10.0.0.202:30066
阻塞...
```



#### LoadBalancer Service实现

![image-20241224093229587](D:\git_repository\cyber_security_learning\markdown_img\image-20241224093229587.png)

只有Kubernetes集群是部署在一个LBaaS平台上且指供有一个集群外部的LB才适合使用LoadBalancer 

一般的公有云都提供了此功能,但可能会有费用产生

如果在一个非公用云的普通的Kubernetes集群上，创建了一个LoadBalancer类型的Service，一般情况 默认环境中是没有LBaaS的，所以会导致由于找不到指定的服务，状态会一直处于 Pending 状态

如果在私有云环境中使用 LoadBalancer Service，可以使用云原生的开源项目实现负载均衡器，比如 **OpenELB, MetalLB** 实现

Loadbalancer 可以获取用户访问的Service对应的Pod在哪个节点上,因此支持externaltrafficpolicy为 Local模式的流量转发



##### OpenElB实现LBaas服务



OpenELB 是一个开源的云原生负载均衡器实现

可以在基于裸金属服务器、边缘以及虚拟化的 Kubernetes 环境中使用 LoadBalancer 类型的 Service 对 外暴露服务。

OpenELB 项目最初由国内青云的 KubeSphere 社区发起，目前已作为 CNCF 沙箱项目加入 CNCF 基金 会，由 OpenELB 开源社区维护与支持。

官网: 

```ABAP
https://openelb.io/
https://github.com/openelb/openelb
```



OpenELB 也拥有两种主要工作模式：**Layer2** 模式和 **BGP** 模式。OpenELB 的 BGP 模式目前暂不支持 IPv6。

因为 OpenELB 是针对裸金属服务器设计的，因此如果是在云环境中部署，需要注意是否满足条件。

核心功能

- BGP模式和二层网络模式下的负载均衡
- ECMP路由和负载均衡
- IP地址池管理
- 基于CRD来管理BGP配置

**注意: 此应用可能不支持 Openstack 等云环境**



##### OpenELB 实现

部署和使用OpenELB

```bash
[root@master1 ~]#wget https://raw.githubusercontent.com/openelb/openelb/master/deploy/openelb.yaml

# 启用
[root@master1 openelb] #kubectl apply -f openelb.yaml 
namespace/openelb-system created
customresourcedefinition.apiextensions.k8s.io/bgpconfs.network.kubesphere.io created
customresourcedefinition.apiextensions.k8s.io/bgppeers.network.kubesphere.io created
customresourcedefinition.apiextensions.k8s.io/eips.network.kubesphere.io created
serviceaccount/openelb-admission created
serviceaccount/openelb-controller created
serviceaccount/openelb-speaker created
role.rbac.authorization.k8s.io/openelb-admission created
clusterrole.rbac.authorization.k8s.io/openelb-admission created
clusterrole.rbac.authorization.k8s.io/openelb-controller created
clusterrole.rbac.authorization.k8s.io/openelb-speaker created
rolebinding.rbac.authorization.k8s.io/openelb-admission created
clusterrolebinding.rbac.authorization.k8s.io/openelb-admission created
clusterrolebinding.rbac.authorization.k8s.io/openelb-controller created
clusterrolebinding.rbac.authorization.k8s.io/openelb-speaker created
secret/memberlist created
service/openelb-controller created
deployment.apps/openelb-controller created
daemonset.apps/openelb-speaker created
job.batch/openelb-admission-create created
job.batch/openelb-admission-patch created
validatingwebhookconfiguration.admissionregistration.k8s.io/openelb-admission created

# 查看创建的CRD自定义资源类型
[root@master1 openelb]#kubectl get crd
NAME                             CREATED AT
bgpconfs.network.kubesphere.io   2024-12-24T01:49:36Z
bgppeers.network.kubesphere.io   2024-12-24T01:49:36Z
eips.network.kubesphere.io       2024-12-24T01:49:36Z

# 确认openelb-manager Pod已经处于Running状态，且容器已经Ready
[root@master1 openelb]#kubectl get pods -n openelb-system 
NAME                                  READY   STATUS      RESTARTS   AGE
openelb-admission-create-r28c5        0/1     Completed   0          69s
openelb-admission-patch-h8g6n         0/1     Completed   2          69s
openelb-controller-7f8788f446-22j7d   1/1     Running     0          69s
openelb-speaker-f462b                 1/1     Running     0          69s
openelb-speaker-mzhpb                 1/1     Running     0          69s
openelb-speaker-phzd8                 1/1     Running     0          69s
openelb-speaker-tb2ms                 1/1     Running     0          69s

#创建了一个Eip资源对象，它提供了一个地址池给LoadBalancer Service使用
[root@master1 openelb] #vim service-loadbalancer-eip-pool.yaml
apiVersion: network.kubesphere.io/v1alpha2
kind: Eip
metadata:
  name: eip-pool
  annotations:
    eip.openelb.kubesphere.io/is-default-eip: "true" #指定当前EIP作为向LoadBalancer Server分片地>址时使用的默认的eip对象
spec:
  address: 10.0.0.10-10.0.0.50 #指定排除主机节点之外的地址范围，可以使用单个IP或者带有掩码长度的>网络地址
  protocol: layer2 #指定OpenELB模式，支持bgp,layer2和vip三种，默认bgp
  interface: eth0 #OpenELB侦听ARP或NDP请求时使用的网络接口名称，仅layer2模式下有效
  disable: false
  
  
# 创建资源
[root@master1 openelb]#kubectl apply -f service-loadbalancer-eip-pool.yaml 
eip.network.kubesphere.io/eip-pool created

# 查看结果
[root@master1 openelb]#kubectl get eip
NAME       CIDR                  USAGE   TOTAL
eip-pool   10.0.0.10-10.0.0.50           41

# 创建Deployment和LoadBalancer类型的Service，测试地址池是否能给Service分配LoadBalancerIP
[root@master1 openelb] #kubectl create deployment myapp --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas=3
deployment.apps/myapp created

[root@master1 openelb]#vim service-loadbalancer-lbaas.yaml
apiVersion: v1
kind: Service
metadata:
  name: service-loadbalancer-lbaas
spec:
  type: LoadBalancer
  externalTrafficPolicy: Local
  selector:
    app: myapp
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80

# 应用
[root@master1 openelb ]#kubectl apply -f service-loadbalancer-lbaas.yaml 
service/service-loadbalancer-lbaas created

# 查看service资源对象myapp是否自动获得了EXTERNAL IP，获取失败...
[root@master1 openelb]#kubectl get svc service-loadbalancer-lbaas 
NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service-loadbalancer-lbaas   LoadBalancer   10.97.215.163   <pending>     80:30214/TCP   8m41s
```





##### metalLB实现LBaaS服务



![image-20241224101508876](D:\git_repository\cyber_security_learning\markdown_img\image-20241224101508876.png)



官网

```ABAP
https://github.com/metallb/metallb
https://metallb.universe.tf/
```

MetalLB 是由 Google 开源提供

MetalLB 功能实现依赖于两种机制

- Address Allocation 地址分配：基于用户配置的地址池，为用户创建的LoadBalancer分配IP地址, 并配置在节点上
- External Announcement 对外公告：让集群外部的网络了解新分配的P地址，MetalLB使用ARP、 NDP或BGP实现



MetallB 可配置为在二层模式或BGP模式下运行

- 二层模式(ARP/NDP)
  - LoadBalancer IP地址配置在某一个节点上，并使用ARP(IPv4)或NDP(IPv6)对外公告
  - 拥有LoadBalancer IP 地址的节点将成为Service流量的惟一入口，并在节点故障时自动进行故障转 移
  - 并未真正实现负载均衡，存在性能瓶颈，且故障转移存在秒级的延迟
- BGP模式
  - 集群中的所有节点与本地网络中的BGP Router建立BGP对等会话，通告LoadBalancer IP，从而告知Router如何进行流量路由
  - 可以实现跨多个节点的真正意义上的负载均衡



**注意: 此应用可能不支持 Openstack 等云环境**



##### MetalLB 实现

```bash
# 部署MetalLB至Kubernetes集群
METALLB_VERSION='v0.14.7'
wget https://raw.githubusercontent.com/metallb/metallb/${METALLB_VERSION}/config/manifests/metallb-native.yaml

# 应用
[root@master1 metalLB]# kubectl apply -f metallb-native.yaml 
namespace/metallb-system created
customresourcedefinition.apiextensions.k8s.io/bfdprofiles.metallb.io created
customresourcedefinition.apiextensions.k8s.io/bgpadvertisements.metallb.io created
customresourcedefinition.apiextensions.k8s.io/bgppeers.metallb.io created
customresourcedefinition.apiextensions.k8s.io/communities.metallb.io created
customresourcedefinition.apiextensions.k8s.io/ipaddresspools.metallb.io created
customresourcedefinition.apiextensions.k8s.io/l2advertisements.metallb.io created
customresourcedefinition.apiextensions.k8s.io/servicel2statuses.metallb.io created
serviceaccount/controller created
serviceaccount/speaker created
role.rbac.authorization.k8s.io/controller created
role.rbac.authorization.k8s.io/pod-lister created
clusterrole.rbac.authorization.k8s.io/metallb-system:controller created
clusterrole.rbac.authorization.k8s.io/metallb-system:speaker created
rolebinding.rbac.authorization.k8s.io/controller created
rolebinding.rbac.authorization.k8s.io/pod-lister created
clusterrolebinding.rbac.authorization.k8s.io/metallb-system:controller created
clusterrolebinding.rbac.authorization.k8s.io/metallb-system:speaker created
configmap/metallb-excludel2 created
secret/metallb-webhook-cert created
service/metallb-webhook-service created
deployment.apps/controller created
daemonset.apps/speaker created
validatingwebhookconfiguration.admissionregistration.k8s.io/metallb-webhook-configuration created

# 查看CRD资源类型
[root@master1 metalLB]#kubectl get crd
NAME                           CREATED AT
bfdprofiles.metallb.io         2024-12-24T02:27:38Z
bgpadvertisements.metallb.io   2024-12-24T02:27:38Z
bgppeers.metallb.io            2024-12-24T02:27:38Z
communities.metallb.io         2024-12-24T02:27:38Z
ipaddresspools.metallb.io      2024-12-24T02:27:38Z
l2advertisements.metallb.io    2024-12-24T02:27:38Z
servicel2statuses.metallb.io   2024-12-24T02:27:38Z

# 创建地址池
# 注意: IPAddressPool 必须使用Kuberetes集群节点的IP地址段
[root@master1 metalLB]#vim service-metallb-IPAddressPool.yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: localip-pool
  namespace: metallb-system
spec:
  addresses:
  - 10.0.0.10-10.0.0.50
  autoAssign: true
  avoidBuggyIPs: true
  
# 应用
[root@master1 metalLB]#kubectl apply -f service-metallb-IPAddressPool.yaml
ipaddresspool.metallb.io/localip-pool created

# 创建二层公告机制
[root@master1 metalLB]#vim service-metallb-L2Advertisement.yaml
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: localip-pool-l2a
  namespace: metallb-system
spec:
  ipAddressPools:
  - localip-pool
  interfaces:
  - eth0 # 用于发送免费ARP公告

[root@master1 metalLB]#kubectl apply -f service-metallb-L2Advertisement.yaml 
l2advertisement.metallb.io/localip-pool-l2a created

# 创建Service和Deployment，测试地址池是否能给Service分配LoadBalancer IP
[root@master1 ~]#kubectl create deployment myapp --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas=3

[root@master1 metalLB]# vim service-loadbalancer-lbaas.yaml
apiVersion: v1
kind: Service
metadata:
  name: service-loadbalancer-lbaas
spec:
  type: LoadBalancer
  externalTrafficPolicy: Local
  selector:
    app: myapp
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
    
# 应用
[root@master1 metalLB]#kubectl apply -f service-loadbalancer-lbaas.yaml 
service/service-loadbalancer-lbaas created

# 查看
[root@master1 metalLB]#kubectl get svc service-loadbalancer-lbaas 
NAME                         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service-loadbalancer-lbaas   LoadBalancer   10.111.219.193   10.0.0.10     80:32248/TCP   7s

# 从外部访问测试
[root@master1 metalLB]#curl 10.0.0.10
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: myapp-547df679bb-57pnm, ServerIP: 10.244.2.51!
```



##### 实际生产环境

- 通常使用公有云提供的LBaaS，而不是这种开源的负载均衡器，MetalLB有Bug，在Local模式下，没有负载均衡效果
- 更多的是使用ingress进行对外暴露







#### ExternalName Service实现

Service 不仅可以实现Kubernetes集群内Pod应用之间的相互访问以及从集群外部访问集群中的Pod

还可以支持做为外部服务的代理实现集群中Pod访问集群外的服务

```ABAP
Pod --> Service_name --> External Name --> 外部DNS --> 外部服务IP
```



**Service代理Kubernetes外部应用的使用场景**

- 在生产环境中Pod 希望使用某个固定的名称而非IP地址进行访问集群外部的服务
- 使用Service指向另一个Namespace中或其它Kubernetes集群中的服务
- 某个项目正在迁移至Kubernetes集群，但是一部分服务仍然在集群外部，此时可以使用service代理至k8s集群外部的服务



**使用ExternalName Service实现代理外部服务（公网IP的服务）**

```bash
[root@master1 service]# vim service-externalname-web.yaml
apiVersion: v1
kind: Service
metadata:
  name: svc-externalname-web
  namespace: default
spec:
  type: ExternalName
  externalName: www.mysticalrecluse.com
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 0
  selector: {}

# 应用
[root@master1 service]#kubectl apply -f service-externalname-web.yaml 
service/svc-externalname-web created

# 查看
#注意: service没有Cluster-IP,即为无头服务Headless Service
[root@master1 service]#kubectl get svc
NAME                   TYPE           CLUSTER-IP   EXTERNAL-IP               PORT(S)   AGE
svc-externalname-web   ExternalName   <none>       www.mysticalrecluse.com   80/TCP    7s

# 创建一个测试pod，解析域名
[root@master1 service]# kubectl run pod-$RANDOM --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/admin-box:v0.1 -it --rm --command -- /bin/bash
If you don't see a command prompt, try pressing enter.
root@pod-18379 /# 
root@pod-18379 /# host svc-externalname-web
svc-externalname-web.default.svc.cluster.local is an alias for www.mysticalrecluse.com.
root@pod-18379 /# ping -c1 svc-externalname-web
PING svc-externalname-web (101.35.250.82): 56 data bytes
64 bytes from 101.35.250.82: seq=0 ttl=127 time=30.567 ms
```



**使用自建的Endpoint实现基于ClusterIP类型的Service代理集群外部服务**

- 手动创建一个Endpoints资源对象，直接把外部端点的IP地址，放入可用地址列表
- 额外创建一个不带selector的同名的Service对象

```bash
# 在k8s集群外安装redis
[root@master1 ~]#apt update && apt -y install redis
[root@master1 ~]#vim /etc/redis/redis.conf
bind 0.0.0.0
[root@master1 ~]#systemctl restart redis

[root@master1 service]# vim service-endpoints.yaml
apiVersion: v1
kind: Endpoints
metadata:
  name: service-redis  # 和下面的service必须同名
  namespace: default
subsets:
  - addresses:
    - ip: 10.0.0.131  # 外部服务的FQDN或IP
    ports:
    - name: reids
      port: 6379
      protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  name: service-redis  # 和上面的endpoints必须同名
  namespace: default
spec:
  type: ClusterIP
  clusterIP: "None"
  ports:
  - name: redis
    port: 6379
    protocol: TCP
    targetPort: 6379

  
# 应用
[root@master1 service]#kubectl apply -f service-endpoints.yaml 
endpoints/service-redis created
service/service-redis created

# 查看
[root@master1 service]#kubectl get svc
NAME                   TYPE           CLUSTER-IP   EXTERNAL-IP               PORT(S)    AGE
kubernetes             ClusterIP      10.96.0.1    <none>                    443/TCP    26m
service-redis          ClusterIP      None         <none>                    6379/TCP   38s

[root@master1 service]#kubectl get ep service-redis 
NAME            ENDPOINTS         AGE
service-redis   10.0.0.131:6379   76s

# 测试访问，使用service名做为域名，访问外部redis
[root@master1 service]#kubectl run pod-$RANDOM --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/admin-box:v0.1 -it --rm --command -- /bin/bash
If you don't see a command prompt, try pressing enter.
root@pod-28779 /# nc service-redis 6379
info
```





#### 会话粘滞

kubernetes的Service默认是按照轮询机制进行转发至后端的多个pod

如果用户请求有一定的会话要求，即希望同一个客户每次总是能访问同一个pod的时候，可以使用 service的**affinity机制**来实现

它能将同一个客户端的请求始终转发至同一个后端Pod对象，它是由**kube-proxy的ipvs机制**来实现的。

默认情况下，service所提供的会话粘性效果默认在**10800s(3小时)**后会重新调度,而且仅能基于客户端IP 进行识别，调度粒度较粗



**属性解析**

```yaml
# 属性信息
service.spec.sessionAffinity  # 定义粘性会话的类型，可为 None 和 ClientIP,默认值为None即不开启会话沾滞
service.spec.sessionAffinityConfig.clinetIP.timeoutSeconds # 配置会话保持时长，默认10800s，范围1-86400

# 配置格式
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800
```



**实现会话粘滞**

```yaml
# 创建deployment资源
[root@master1 service] # kubectl create deployment myweb --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas=3
deployment.apps/myweb created

[root@master1 service] # kubectl get pod
NAME                     READY   STATUS    RESTARTS   AGE
myweb-565cb68445-2sqx9   1/1     Running   0          3s
myweb-565cb68445-8z59d   1/1     Running   0          3s
myweb-565cb68445-nts2b   1/1     Running   0          3s

# 创建Service资源对象
[root@master1 service] # vim service-session.yaml
apiVersion: v1
kind: Service
metadata:
  name: service-session
spec:
  type: LoadBalancer
  ports:
  - port: 80
  selector:
    app: myweb
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 1800 # 默认值为10800，即3小时

# 应用
[root@master1 service]  #kubectl apply -f service-session.yaml 
service/service-session created

# 同一个客户端，多次访问都是调度到同一个Pod上
[root@master1 service] # curl 10.109.193.1
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: myweb-565cb68445-8z59d, ServerIP: 10.244.2.52!
[root@master1 service] # curl 10.109.193.1
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: myweb-565cb68445-8z59d, ServerIP: 10.244.2.52!
[root@master1 service] # curl 10.109.193.1
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: myweb-565cb68445-8z59d, ServerIP: 10.244.2.52!
```



#### ipvs模式

![image-20241224143822632](D:\git_repository\cyber_security_learning\markdown_img\image-20241224143822632.png)



ipvs会在每个节点上创建一个名为kube-ipvs0的虚拟接口，并将集群所有Service对象的ClusterIP和ExternalIP都配置在该接口； 所以每增加一个ClusterIP 或者ExternalIP，就相当于为 kube-ipvs0 关联 了一个地址罢了。

kube-proxy为每个service生成一个虚拟服务器( IPVS Virtual Server)的定义。



**基本流程：**

- 当前节点接收到外部流量后，如果该数据包是交给当前节点上的clusterIP，则会直接将数据包交给 kube-ipvs0，而这个接口是内核虚拟出来的，而kube-proxy定义的VS直接关联到kube-ipvs0上。
- 如果是本地节点pod发送的请求，基本上属于本地通信，效率是非常高的。
- 默认情况下，这里的ipvs使用的是nat转发模型，而且支持更多的后端调度算法。仅仅在涉及到源地址转 换的场景中，会涉及到极少量的iptables规则(应该不会超过20条)
- 对于Kubernetes来说，默认情况下，支持的规则是 iptables，可以通过多种方式对代理模式进行更改， 因为这些规则都是**基于kube-proxy**来定制的，所以，如果要更改代理模式的话，就需要调整kube-proxy 的属性。



**注意：Kubernetes-v1.29版本后，不再使用iptables，而使用nftables framework，工具使用nft  list ruleset 查看**



更改kube-proxy为IPVS模式方法说明

```bash
#方法1： 在集群创建的时候，修改kubeadm-init.yml 添加如下配置，此方法是生产中推荐
kubeadm config print init-defaults > kubeadm-init.yaml

# 在文件最后面添加一下几行
---
apiVersion: kubeproxy.config.Kubernetes.io/v1alpha1
kind: KubeProxyConfiguration
featureGates:
  SupportIPVSProxyMode: true
mode: ipvs

# 在初始阶段可能修改的参数
apiVersion: kubeadm.k8s.io/v1beta3
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: 192.168.0.100
  bindPort: 6443
nodeRegistration:
  criSocket: unix:///run/cri-dockerd.sock                  # 配置cri-dockerd插槽
  name: master1
  taints:
  - effect: NoSchedule
    key: node-role.kubernetes.io/control-plane

---
apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration
kubernetesVersion: "v1.30.2"
controlPlaneEndpoint: "master1.mystical.org:6443"            # 修改控制平面域名
networking:
  podSubnet: "10.244.0.0/16"                                 # 修改集群网路配置，pod网络
  serviceSubnet: "10.96.0.0/12"                              # service网络
imageRepository: registry.aliyuncs.com/google_containers     # 修改镜像仓库（如使用国内镜像）
apiServer:
  extraArgs:
    authorization-mode: Node,RBAC


# 更改好配置文件后，执行命令初始化
kubeadm init --config=kubeadm-init.yaml --token-ttl --upload-certs

# 验证集群状态
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# 看集群是否正常运行
kubectl get nodes
kubectl get pods -n kube-system


# 方法2：在测试环境中，临时修改一下configmap中proxy的基本属性，此方式在测试环境中推荐使用
[root@master1 ~] # kubectl edit cm  kube-proxy -n kube-system
...
mode: "ipvs"  #修改此行，默认为空”“表示iptables模式
...

# 更改后，需要稍等一会儿才能生效

# 如果想立即生效，需要重启所有的kube-proxy pod对象
[root@master1 ~]#kubectl get ds -n kube-system 
NAME         DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
kube-proxy   4         4         4       4            4           kubernetes.io/os=linux   5d1h

[root@master1 ~]#kubectl get pod -n kube-system -l k8s-app=kube-proxy
NAME               READY   STATUS    RESTARTS        AGE
kube-proxy-7fc2q   1/1     Running   5 (5h50m ago)   5d1h
kube-proxy-7slb9   1/1     Running   5 (5h49m ago)   5d1h
kube-proxy-n66cg   1/1     Running   5 (5h49m ago)   5d1h
kube-proxy-vkqh5   1/1     Running   5 (5h47m ago)   5d1h

# 重启pod
[root@master1 ~]#kubectl rollout restart daemonset -n kube-system kube-proxy 
daemonset.apps/kube-proxy restarted

# 重启方式2：删除原pod，使damonset自动重新创建
kubectl delete pod -n kube-system -l k8s-app=kube-proxy

# 安装ipvsadm查看效果
[root@master1 ~]#apt update && apt -y install ipvsadm
[root@master1 ~]#ipvsadm -Ln
IP Virtual Server version 1.2.1 (size=4096)
Prot LocalAddress:Port Scheduler Flags
  -> RemoteAddress:Port           Forward Weight ActiveConn InActConn
TCP  172.17.0.1:30433 rr persistent 1800
  -> 10.244.1.99:80               Masq    1      0          0         
  -> 10.244.2.52:80               Masq    1      0          0         
  -> 10.244.3.106:80              Masq    1      0          0         
TCP  10.0.0.201:30433 rr persistent 1800
  -> 10.244.1.99:80               Masq    1      0          0         
  -> 10.244.2.52:80               Masq    1      0          0         
  -> 10.244.3.106:80              Masq    1      0          0 
  ......
```



### 综合案例：Wordpress

```yaml
[root@master1 controller] # vim wordpress-mysql.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: demo
---
apiVersion: v1
kind: Service
metadata:
  name: wordpress
  namespace: demo
spec:
  type: LoadBalancer
  externalTrafficPolicy: Local
  selector:
    app: wordpress
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
  namespace: demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: wordpress
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache
        name: wordpress
        env:
        - name: WORDPRESS_DB_HOST
          value: mysql.demo.svc.cluster.local.
        - name: WORDPRESS_DB_USER
          value: wordpress
        - name: WORDPRESS_DB_PASSWORD
          value: "123456"
        - name: WORDPRESS_DB_NAME
          value: wordpress
---
apiVersion: v1
kind: Service
metadata:
  name: mysql
  namespace: demo
spec:
  ports:
  - port: 3306
    protocol: TCP
    targetPort: 3306
  selector:
    app: mysql

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
  namespace: demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
        name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: "123456"
        - name: MYSQL_DATABASE
          value: "wordpress"
        - name: MYSQL_USER
          value: wordpress
        - name: MYSQL_PASSWORD
          value: "123456"
          
# 查看svc
[root@master1 controller]#kubectl get svc -n demo 
NAME        TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)        AGE
mysql       ClusterIP      10.111.9.21   <none>        3306/TCP       23s
wordpress   LoadBalancer   10.97.65.76   10.0.0.11     80:30371/TCP   23s

# 浏览器访问
http://10.0.0.11/
```



![image-20241224154414207](D:\git_repository\cyber_security_learning\markdown_img\image-20241224154414207.png)









## Kubernetes域名解析

### 服务发现机制

在传统的系统部署中，服务运行在一个固定的已知的 IP 和端口上，如果一个服务需要调用另外一个服 务，可以通过地址直接调用

在Kubernetes 集群中，基于clusterip地址来访问每service是很不方便的

虽然通过配置DNS可以实现名称解析来访问，但是在Kubernetes集群中，服务实例的启动和销毁是很频 繁的，服务地址在动态的变化，所以传统的方式配置DNS解析记录就很不友好了。



将请求发送到动态变化的服务实例上，可以通过以下两个步骤来实现：

- **服务注册** — 创建服务实例后，主动将当前服务实例的信息，存储到一个集中式的服务管理中心。
- **服务发现** — 当A服务需要找未知的B服务时，先去服务管理中心查找B服务地址，然后根据该地址找到B服务



**Kubernetes主要有两种服务发现机制：**

- 环境变量
- DNS解析







### 环境变量

对于环境变量来说，它主要有两种实现方式

- **Kubernetes Service环境变量**

  - Kubernetes为每个Service资源生成包括以下形式的环境变量在内一系列环境变量
  - 在同一名称空间中后续创建的Pod对象都会自动拥有这些变量
  - 注意：此方式不支持Service的动态变化，即在创建Pod对象以后，Service的变化不会生成相关的 环境变量，生产此方式不太常见
  - Service相关环境变量形式如下

  ```bash
  {SVCNAME}_SERVICE_HOST {SVCNAME}_PORT
  
  # 比如：default名称空间创建名为test的Service，default名称空间下的每个Pod内部会被自动注入 和service相关的变量
  TEST_SERVICE_HOST=ClusterIP
  TEST_PORT=tcp://ClusterIP:80
  ```

  ```yaml
  # 注意：如果先创建Pod，然后关联到Service是不生效的
  # 一定要先创建Service，在创建Service下的pod资源类型或者deploy等，才会看到环境变量
  
  
  # 相关实验
  创建service
  [root@master1 controller]#kubectl create svc clusterip myweb --tcp=80:80
  service/myweb created
  
  # 创建相关svc下的deployment
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    labels:
      app: myweb                            # 必须是myweb,因为svc是myweb
    name: myweb
  spec:
    progressDeadlineSeconds: 600
    replicas: 3
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app: myweb
    template:
      metadata:
        labels:
          app: myweb
      spec:
        containers:
        - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
          imagePullPolicy: IfNotPresent
          name: pod-test
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
  
  # 应用
  [root@master1 controller] # kubectl apply -f myweb-deploy-test1.yaml
  deployment.apps/myweb created
  
  # 查看
  [root@master1 controller] # kubectl get pod
  NAME                     READY   STATUS        RESTARTS   AGE
  myweb-565cb68445-btlj8   1/1     Running       0          12s
  myweb-565cb68445-c8drb   1/1     Running       0          12s
  myweb-565cb68445-lj7bq   1/1     Running       0          12s
  
  [root@master1 controller] # kubectl get svc
  NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
  kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   4h59m
  myweb        ClusterIP   10.104.153.124   <none>        80/TCP    13m
  
  
  # 查看pod内的环境变量
  [root@master1 controller] # kubectl exec myweb-565cb68445-btlj8 -it -- /bin/sh
  [root@myweb-565cb68445-btlj8 /]# env
  KUBERNETES_SERVICE_PORT=443
  KUBERNETES_PORT=tcp://10.96.0.1:443
  HOSTNAME=myweb-565cb68445-btlj8
  MYWEB_SERVICE_HOST=10.104.153.124        # MYWEB_SERVICE_HOST
  SHLVL=1
  HOME=/root
  PS1=[\u@\h \w]\$ 
  MYWEB_SERVICE_PORT=80
  MYWEB_PORT=tcp://10.104.153.124:80       # MYWEB_PORT
  TERM=xterm
  MYWEB_PORT_80_TCP_ADDR=10.104.153.124
  KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
  MYWEB_SERVICE_PORT_80_80=80
  PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  MYWEB_PORT_80_TCP_PORT=80
  
  ```



### COREDNS

#### CoreDNS介绍

![image-20241224164000953](D:\git_repository\cyber_security_learning\markdown_img\image-20241224164000953.png)



专用于kubernetes集群中的服务注册和发现的解决方案就是KubeDNS。

kubeDNS自从Kubernetes诞生以来，其方案的具体实现方案前后经历了三代，分别是 SkyDNS、 KubeDNS、CoreDNS。

Kubernetes-v1.3之前使用SkyDNS, 之后到Kubernetes-v1.13之前使用KubeDNS,当前默认使用 **CoreDNS**

CoreDNS 是一个DNS服务器。Go实现，由于其灵活性，它可以在多种环境中使用。

CoreDNS 是一个云原生计算基金会毕业的项目。CoreDNS通过 Kubernetes 插件与 Kubernetes 集 成，或者通过etcd插件与etcd 集成,实现服务发现

**CoreDNS 官方网站**

```ABAP
https://coredns.io/
https://github.com/coredns/coredns
```





#### CoreDNS解析流程

CoreDNS 通过访问名为 kubernetes 的 Service,找到 API Server 进而连接到 ETCD, 从而实现 Kubernetess集群中的Service,Endpoint,Pod 等资源的查找

![image-20241224164328154](D:\git_repository\cyber_security_learning\markdown_img\image-20241224164328154.png)



- Client Pod **查询自身的/etc/resolv.conf** 指向的DNS服务器地址,此地址为kube-dns service的地址, 即将解析请求转发给名为 kube-dns的 service

  ```bash
  [root@master1 controller]#kubectl exec myweb-565cb68445-btlj8 -it -- /bin/sh
  [root@myweb-565cb68445-btlj8 /]# cat /etc/resolv.conf 
  nameserver 10.96.0.10      # COREDNS的svc地址
  search default.svc.cluster.local svc.cluster.local cluster.local wang.org
  options ndots:5
  ```

- kube-dns service会将请求转发到后端CoreDNS Pod,为了DNS的高可用,通常有两个CoreDNS Pod, 并位于kube-system名称空间

  ```bash
  [root@master1 controller]#kubectl get svc -n kube-system
  NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
  kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   5d3h
  ```

- Coredns Pod 根据Corefile的配置会连接到在default名称空间的名为kubernetes的service,而 kubernetes service对应的Endpoints为所有kube-apiserver:6443的地址

  ```bash
  [root@master1 controller]#kubectl get svc -n kube-system
  NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
  kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   5d3h
  
  [root@master1 controller]#kubectl get ep
  NAME         ENDPOINTS                                        AGE
  kubernetes   10.0.0.201:6443                                  5h17m
  ```

- kubernetes service 监视service IP的变动，维护DNS解析记录,并将变化发送至ETCD实现DNS记录 的存储

- CoreDNS查询到service name对应的IP后返回给客户端

- 如果查询的是外部域名，**CoreDNS无法解析，就转发给指定的域名服务器**，**一般是节点 上/etc/resolv.conf中的服务器解析**

  ```bash
  # 要使其生效，需要在更改coredns所在节点上的dns后，更新corednsPod
  [root@master1 controller]#kubectl rollout restart deployment -n kube-system coredns 
  deployment.apps/coredns restarted
  ```







#### CoreDNS域名解析

![image-20241224175717162](D:\git_repository\cyber_security_learning\markdown_img\image-20241224175717162.png)

Cluster DNS（CoreDNS）是Kubernetes集群的必备附件，负责为Kubernetes提供名称解析和服务发现

每个Service资源对象，在**CoreDNS上都会自动生成如下格式的名称，结合该名称会生成对应的一些不同 类型的DNS资源记录**

```bash
<service>.<ns>.svc.<zone>
<service>： #当前Service对象的名称
<ns>：      #当前Service对象所属的名称空间
<zone>：    #当前Kubernetes集群使用的域名后缀，默认为“cluster.local”pass
```

范例：kubeadm安装方式时查看默认Zone名称

```bash
[root@master1 ~]#kubeadm config print init-defaults |grep dns
dns: {}
  dnsDomain: cluster.local
```

CoreDNS会持续监视API Server上的Service资源对象的变动，并实时反映到相关的DNS资源记录中

Pod中各容器内部默认会在其 /etc/resolv.conf中，将nameserver指向CoreDNS相关的Service的 ClusterIP，默认为service网段的第10个IP，比如：10.96.0.10，其后面的Endpoint是coredns对应的 Pod的IP，此配置由kubelet创建Pod时根据指定的配置自动注入



范例：集群上的一个随机选择的Pod中的容器查看DNS客户端配置

```bash
[root@master1 ~]#kubectl exec myweb-5d78b4dcbd-6rgv4 -- cat /etc/resolv.conf
nameserver 10.96.0.10
search default.svc.cluster.local svc.cluster.local cluster.local wang.org
options ndots:5

#上述search参数中指定的DNS各搜索域，是以次序指定的几个域名后缀，它们各自的如下所示。
#<ns>.svc.<zone>：附带有特定名称空间的域名，例如default.svc.cluster.local
#svc. <zone>：附带了Kubernetes标识Service专用子域svc的域名，例如svc.cluster.local；
<zone>：集群本地域名，例如cluster.local。
#ndots:5，表示如果手工查询时候给的域名包含的点“.”不超过5个，那么进行DNS查找时将使用非完全限定
名称，即用search指定的域名补全
即 <手工输入域名> 或者 <手工输入域名>.<search 部分给定的域名后缀>
如果你查询的域名包含点数大于等于5，那么DNS查询，默认会使用绝对域名进行查询。
即 <手工输入域名>
```



#### Service 资源对应的DNS资源记录

基于DNS的服务发现，对于每个Service对象，都会具有以下3个类型的DNS资源记录**A/AAAA**，**PTR**和 **SRV**

- 根据ClusterIP的地址类型，为IPv4生成固定格式的 A记录，为IPv6生成AAAA记录

```bash
<service>.<ns>.svc.<zone>. <ttl> IN A <cluster-ip>
<service>.<ns>.svc.<zone>. <ttl> IN AAAA <cluster-ip>
#示例：
testapp.default.svc.cluster.local.
#注意：cluster.local 是默认zone名称，在初始化Kubernetes集群中，自己通过dnsDomain属性定制的。
```

- 对于每个给定的A记录或AAAA记录都要生成PTR记录，格式如下所示

```bash
<d>.<c>.<b>.<a>.in-addr.arpa. <ttl> IN PTR <service>.<ns>.svc.<zone>.
h4.h3.h2.h1.g4.g3.g2.g1.f4.f3.f2.f1.e4.e3.e2.e1.d4.d3.d2.d1.c4.c3.c2.c1.b4.b3.b2
.b1.a4.a3.a2.a1.ip6.arpa <ttl> IN PTR <service>.<ns>.svc.<zone>.
```

- 为每个定义了名称的端口生成一个SRV记录，未命名的端口号则不具有该记录

```bash
_<port_name>._<proto>.<service>.<ns>.svc.<zone>. <ttl> IN SRV <weight> 
<priority> <port-number> <service>.<ns>.svc.<zone>.
```





#### Pod的DNS解析策略和配置

Kubernetes支持在单个Pod资源规范上自定义DNS解析策略和配置，并组合生效

- **pod.spec.dnsPolicy**：解析策略
  - **Default**：从运行在的节点/etc/resolv.conf继承DNS名称解析相关的配置
  - **ClusterFirst**：**此为默认值**，优先使用集群内DNS服务上解析集群域内的名称，其他域名的解析则 交由从节点/etc/resolv.conf继承的名称服务器 即使用Default策略
  - **ClusterFirstWithHostNet**：专用于在设置了hostNetwork（使用宿主机的网络）的Pod对象上并不会使用节点网络的DNS，仍然使用的ClusterFirst策略
  - **None**：用于忽略Kubernetes集群的默认设定，而仅使用由dnsConfig自定义的配置
- **pod.spec.dnsConfig**：名称解析机制
  - **nameservers <[]string>**：DNS名称服务器列表，附加于由dnsPolicy生成的DNS名称服务器之后
  - **searches <[]string>**：DNS名称解析时的搜索域，附加由于dnsPolicy生成的搜索域之后
  - **options <[]Object>**：DNS解析选项列表，同dnsPolicy生成的解析选项合并成最终生效的定义



范例：dnsPolicy 的 None 的解析策略

```yaml
# cat service-pod-with-dnspolicy.yaml
apiVersion: v1
kind: Pod
metadata:
  name: service-pod-with-dnspolicy
  namespace: default
spec:
  containers:
  - name: demo
    image: wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
  dnsPolicy: None
  dnsConfig:
    nameservers:
    - 10.96.0.10
    - 180.76.76.76
    - 233.6.6.6
    searches:
    - svc.cluster.local
    - cluster.local
    - wang.org
    options:
    - name: ndots
      value: "5"  #意味着如果域名中只有5个或更少的点，则系统会尝试在其末尾添加搜索域。
```





#### CoreDNS配置

CoreDNS的配置都存储在名为**coredns的ConfigMap**对象中，该对象位于**kube-system**名称空间中

服务器配置段(Server Blocks)，用于定义负责解析的权威区域，配置段放置于其后的花括号{}中

服务器配置段也可以指定要监听的端口号,端口号之前需要使用一个冒号，默认为53



**配置解析**

```bash
# coredns的配置是存放在 configmap中
[root@master1 ~]#kubectl get cm -n kube-system
NAME                                                   DATA   AGE
coredns                                                1      5d20h

#查看配置内容
apiVersion: v1
data:
  Corefile: |
    .:53 {                               # 包括跟区域的所有区域对应的监听端口进行解析
        errors                           # 将错误信息进行输出
        health {                         # LivenessProbe检测，http://localhost:8080/health实现
           lameduck 5s
        }
        ready                            # readinessProbe检测，http://localhost:8181/ready coredns就绪返回200
        kubernetes cluster.local in-addr.arpa ip6.arpa {  # 基于Kubernetes的service名称进行查询返回查询结果
           pods insecure
           fallthrough in-addr.arpa ip6.arpa    # 如果in-addr.arpa ip6.arpa区域解析失败，交由后续的插件进行解析
           ttl 30
        }
        prometheus :9153                # 配置访问端口给Prometheus实现监控
        forward . /etc/resolv.conf {    # forward 转发配置，如果集群内部无法解析，交由宿主机的文件解析，也可为IP地址
           max_concurrent 1000          # 最大连接数，提高此值可以提高并发性
        }
        cache 30                        # 启用缓存，单位s
        loop                            # 检测发现环路时重建corendns对应的Pod显示CrashLoopBackOff状态而停止查询，比如CoreDNS直接将请求发给上游服务器，后者再将请求转发回CoreDNS
        reload                          # 检测Corefile是否变化，修改configmap会默认2M后自动加载
        loadbalance                     # 基于随机算法实现DNS查询记录负载均衡
    }

...
        # 对于企业内的dns解决方案，可以通过forward来实现，格式如下
        forward <域名> <转发至外部DNS的地址> {  # 转发配置，如果集群内部无法解析，交由宿主机文件或外部DNS的IP解析
            max_concurrent 最大连接配置
            except 排除域名
        }
        # 示例：转发域名解析至集群外的DNS服务器,"."点表示所有域名
        forward . 10.0.0.10 10.0.0.20 {
            prefer_udp                   # 优先使用UDP
        }
        #注意：如果仅仅对某个域名进行转发的话，只需要将 <域名> 部分设置为指定的域名即可。
        #生产中不推荐直接将 "." 的转发地址使用公网的dns地址，推荐在当前主机的/etc/resolv.conf中配置外网，实现间接效果
        
        # 添加特定主机的正向解析记录，类似于/etc/hosts文件功能
        hosts {
            192.168.10.100 www.example.com
            10.0.0.101 gitlab.example.org nfs.example.org
            10.0.0.102 jenkins.wang.org
            10.0.0.100 harbor.wang.org
            fallthrough
        }
```



范例: 不使用默认的转发策略，使用自定义的转发策略

```bash
# 修改配置文件
[root@master1 ~]#kubectl edit cm coredns -n kube-system 
configmap/coredns edited

# 修改之后重启CoreDNS
[root@master1 ~]#kubectl rollout restart -n kube-system deployment coredns 
deployment.apps/coredns restarted
```



### Headless Service

#### 无头服务机制

无头服务场景下，Kubernetes会将一个集群内部的所有Pod成员提供唯一的DNS域名来作为每个成员的 网络标识，集群内部成员之间使用域名通信，这个时候，就特别依赖service的selector属性配置了。



**广义上Headless Service，它们又可以为分两种情形**

- 有标签选择器，或者没有标签选择器,但有着与Service对象同名的Endpoint资源
  - Service的DNS名称直接解析为后端各就绪状态的Pod的IP地址
  - 调度功能也将由DNS完成
  - 各Pod IP相关PTR记录将解析至Pod名称，假设Pod IP为a.b.c.d，则其Pod名称为a-b-c-d...SVC.
  - 这种类型也就是狭义上的Headless Service
  - 主要应用于有状态服务的**statefulSet**资源对象

- 无标签选择器且也没有与Service对象同名的Endpoint资源
  - 用于集群外部 ExternalName 类型的Service
  - Service的DNS名称将会生成一条CNAME记录，对应值由Service对象上的spec.externalName字段指定

```ABAP
注意: headless service是一个四层调度，因为iptatbles/ipvs都是四层的
```



**主要的应用场景**

- ServiceName --> (label Selector，Pod) --> 所有Pod的IP地址，此方式又称为狭义的Headless  Service，主要应用在 **StatefulSet**
- ServiceName --> CName （**ExternalName**） --> ExternalService IP，此方式称为狭义的 External Service



**无头服务管理的域名是如下的格式：**

```bash
$(service_name).$(Kubernetes_namespace).svc.cluster.local
```



**DNS 解析记录**

```bash
#A记录
<a>-<b>-<c>-<d>.<service>.<ns>.svc.<zone> A PodIP

#PodIP的PTR反解析记录  
<d>.<c>.<b>.<a>.in-addr.arpa IN PTR <用横线分隔的PodIP>.<service>.<ns>.svc.<zone>

#关键点：
正向解析:svc_name的解析结果从常规Service的ClusterIP，转为解析成各个Pod的IP地址
反向解析:从常规的clusterip解析为service name，转为从podip到hostname, <a>-<b>-<c>-<d>.
<service>.<ns>.svc.<zone>
<hostname>指的是a-b-c-d格式，而非Pod自己的主机名；
```



**案例：: Headless Service**

```bash
# 命令行方式
[root@master1 ~]#kubectl create service clusterip service-headless-cmd --clusterip="None"

# 创建文件
[root@master1 headlessService]#vim service-headless.yaml
apiVersion: v1
kind: Service
metadata:
  name: service-headless
spec:
  selector:
    app: myweb
  clusterIP: "None"  #无头服务
  
# 应用
[root@master1 headlessService]#kubectl apply -f service-headless.yaml 
service/service-headless created

# 查看
[root@master1 headlessService]#kubectl exec myweb-565cb68445-btlj8 -- host service-headless
service-headless.default.svc.cluster.local has address 10.244.1.104
service-headless.default.svc.cluster.local has address 10.244.2.56
service-headless.default.svc.cluster.local has address 10.244.3.111
```







## Kubernetes数据存储





**本章内容**

- **存储机制**
- **emptyDir**
- **hostPath**
- **网络共享存储**
- **PV和PVC**
- **StorageClass**
- **CNS的存储方案OpenEBS**







### 数据存储



#### 存储机制

Container 中的文件在磁盘上是临时存放的，这给 Container 中运行的较重要的应用程序带来一些问题。

- 当容器崩溃时。 kubelet 可能会重新创建容器，可能会导致容器漂移至新的宿主机，容器会以干净的状态重建。导致数据丢失
- 在同一 Pod 中运行多个容器需要共享数据



Kubernetes 卷（Volume） 这一抽象概念能够解决这两个问题



Kubernetes 集群中的容器数据存储

![image-20241225142912632](D:\git_repository\cyber_security_learning\markdown_img\image-20241225142912632.png)





**Kubernetes支持的存储类型**

Kubernetes支持丰富的存储类型，可以分为树内和树外两种



**树内 In-Tree 存储卷插件**

| 类型         | 举例                                                         |
| ------------ | ------------------------------------------------------------ |
| 临时存储卷   | emptyDir                                                     |
| 本地数据卷   | hostPath、local                                              |
| 文件系统     | NFS、CephFS、GlusterFS、fastdfs、Cinder、gitRepo(DEPRECATED) |
| 块设备       | iSCSI、FC、rdb(块设备)、vSphereVolume                        |
| 存储平台     | Quobyte、PortworxVolume、StorageOS、ScaleIO                  |
| 云存储数据卷 | Aliyun OSS、Amazon S3、AWS Elastic Block Store、Google gcePersistentDisk等 |
| 特殊存储卷   | ConfigMap、Secret、DownwardAPI、Projectd、flocker            |



**树外 Out-of_Tree 存储卷插件**

经由**容器存储接口CSI**或**FlexVolume接口（已淘汰）**扩展出的外部的存储系统称为Out-of-Trec类的存储插件



- **CSI 插件**

  - Container Storage Interface 是当前Kubernetes社区推荐的插件实现方案
  - CSI 不仅支持Kubernetes平台存储插件接口，而且也作为云原生生态中容器存储接口的标准,公用 云对其有更好的支持
  - Kubernetes 支持 CSI 的接口方式实现更大范围的存储功能扩展,更为推荐使用

  ```bash
  https://github.com/container-storage-interface/spec/blob/master/spec.md
  ```

  

CSI 主要包含两个部分：**CSI Controller Server** 与 **CSI Node Server**，分别对应**Controller Server Pod**和 **Node Server Pod**



![image-20241225145234834](D:\git_repository\cyber_security_learning\markdown_img\image-20241225145234834.png)

- **Controller Server**
  - 也称为CSI Controller
  - 在集群中只需要部署一个 Controller Server，以 deployment 或者 StatefulSet 的形式运行
  - 主要负责与存储服务API通信完成后端存储的管理操作，比如 provision 和 attach 工作。



- **Node Server**
  - 也称为CSI Node 或 Node Plugin
  - 保证每一个节点会有一个 Pod 部署出来，负责在节点级别完成存储卷管理，和 CSI Controller 一起 完成 volume 的 mount 操作。
  - Node Server Pod 是个 DaemonSet，它会在每个节点上进行注册。
  - Kubelet 会直接通过 Socket 的方式直接和 CSI Node Server 进行通信、调用 Attach/Detach/Mount/Unmount 等。



![image-20241225145625234](D:\git_repository\cyber_security_learning\markdown_img\image-20241225145625234.png)





**CSI 插件包括以下两部分**

- **CSI-Plugin**:实现数据卷的挂载、卸载功能。
- **CSI-Provisioner**: 制备器（Provisioner）实现数据卷的自动创建管理能力，即驱动程序，比如: 支 持云盘、NAS等存储卷创建能力



**Kubernetes 存储架构**

存储的组件主要有：attach/detach controller、pv controller、volume manager、volume plugins、 scheduler

每个组件分工明确

![image-20241225150025215](D:\git_repository\cyber_security_learning\markdown_img\image-20241225150025215.png)

- **AD控制器**：负责存储设备的Attach/Detach操作
  - Attach：将设备附加到目标节点
  - Detach：将设备从目标节点上卸载
- **Volume Manager**：存储卷管理器，负责完成卷的Mount/Umount操作，以及设备的格式化操作等
- **PV Controller** ：负责PV/PVC的绑定、生命周期管理，以及存储卷的Provision/Delete操作
- **volume plugins**：包含k8s原生的和各厂商的的存储插件，扩展各种存储类型的卷管理能力
  - 原生的包括：emptydir、hostpath、csi等
  - 各厂商的包括：aws-ebs、azure等
- scheduler：实现Pod的调度，涉及到volume的调度。比如ebs、csi关于单node最大可attach磁盘 数量的predicate策略，scheduler的调度至哪个指定目标节点也会受到存储插件的影响





### Pod的存储卷Volume

Kubernetes 支持在Pod上创建不同类型的任意数量的卷来实现不同数据的存储



**单节点存储**

![image-20241225151327829](D:\git_repository\cyber_security_learning\markdown_img\image-20241225151327829.png)



**多节点存储**

![image-20241225151355422](D:\git_repository\cyber_security_learning\markdown_img\image-20241225151355422.png)



存储卷本质上表现为 Pod中**所有容器共享访问的目录**

而此目录的创建方式、使用的存储介质以及目录的初始内容是由Pod规范中声明的存储卷类型来源决定

**kubelet内置支持多种存储卷插件**，**存储卷是由各种存储插件(存储驱动)来提供存储服务**

存储卷插件(存储驱动)决定了支持的后端存储介质或存储服务，例如hostPath插件使用宿主机文件系 统，而nfs插件则对接指定的NFS存储服务等

Pod在规范中需要指定其包含的卷以及这些卷在容器中的挂载路径

**存储卷需要定义在指定的Pod之上**

有些卷本身的生命周期与Pod相同，但其后端的存储及相关数据的生命周期通常要取决于存储介质



存储卷可以分为：**临时卷和持久卷**

- **临时卷类型**的生命周期与 Pod 相同， 当 Pod 不再存在时，Kubernetes 也会销毁临时卷
- 持久卷可以比 Pod 的存活期长。当 Pod 不再存在时，Kubernetes 不会销毁持久卷。
- 但对于给定 Pod 中任何类型的卷，在容器重启期间数据都不会丢失。



#### Pod中卷的使用

- 一个Pod可以添加任意个卷
- 同一个Pod内每个容器可以在不同位置按需挂载Pod上的任意个卷，或者不挂载任何卷
- 同一个Pod上的某个卷，也可以同时被该Pod内的多个容器同时挂载，以共享数据
- 如果支持，多个Pod也可以通过卷接口访问同一个后端存储单元

![image-20241225155834088](D:\git_repository\cyber_security_learning\markdown_img\image-20241225155834088.png)



**存储卷的配置由两部分组成**

- 通过.spec.volumes字段定义在Pod之上的存储卷列表，它经由特定的存储卷插件并结合特定的存储供给方的访问接口进行定义
- 嵌套定义在容器的volumeMounts字段上的存储卷挂载列表，它只能挂载当前Pod对象中定义的存储卷



**Pod 内部容器使用存储卷有两步：**

- 在Pod上定义存储卷，并关联至目标存储服务上 **volumes**
  - **定义卷**
- 在需要用到存储卷的容器上，挂载其所属的Pod中pause的存储卷 **volumesMount**
  - **引用卷**



**容器引擎对共享式存储设备的支持类型：**

- **单路读写** - 多个容器内可以通过同一个中间容器对同一个存储设备进行读写操作
- **多路并行读写** - 多个容器内可以同时对同一个存储设备进行读写操作
- **多路只读** - 多个容器内可以同时对同一个存储设备进行只读操作



**Pod的卷资源对象属性**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: <string>
  namespace: <string>
spec:
  volumes:                       # 定义卷
  - name: <string>               # 存储卷名称标识，仅可使用DNS标签格式的字符，在当前Pod必须唯一
    VOL_TYPE: <Object>           # 存储卷插件及具体的目标存储供给方的相关配置
  containers:
  - name: ...
    image: ...
    volumeMounts:                # 挂载卷
    - name: <string>             # 要挂载的存储卷的名称，必须匹配存储卷列表中某项的定义
      mountPath: <string>        # 容器文件系统上的挂载点路径
      readOnly: <boolean>        # 是否挂载为只读模式，默认为"否"，即可读可写
      subPath: <string>          # 挂载存储卷上的一个子目录至指定挂载点
      subPathExpr: <string>      # 挂载有指定的模式匹配到的存储卷的文件或目录至挂载点
```





### emptyDir

一个emptyDir volume在pod被调度到某个Node时候自动创建的，无需指定宿主机上对应的目录。 适用于在一个**Pod中不同容器间的临时数据的共享**



**emptyDir 数据存放在宿主机的路径如下**

```bash
/var/lib/kubelet/pods/<pod_id>/volumes/kubernetes.io~empty-dir/<volume_name>/<FILE>

#注意：此目录随着Pod删除，也会随之删除，不能实现持久化

# 查看pod所在节点
[root@master1 pods]#kubectl get pods -o wide
NAME                     READY   STATUS    RESTARTS        AGE   IP             NODE    NOMINATED NODE   READINESS GATES
myweb-565cb68445-btlj8   1/1     Running   1 (7h25m ago)   24h   10.244.2.56    node2   <none>           <none>
myweb-565cb68445-c8drb   1/1     Running   1 (7h26m ago)   24h   10.244.1.104   node1   <none>           <none>
myweb-565cb68445-lj7bq   1/1     Running   1 (7h25m ago)   24h   10.244.3.111   node3   <none>           <none>

# 查看pod节点上emptyDir数据存放的路径
[root@master1 pods]#ssh 10.0.0.203 ls /var/lib/kubelet/pods/
242cc64b-4330-4c00-ba80-9228f2186367
4a737c21-36e2-413d-a53f-ce65b9b4698e
9fe61621-a076-4d35-add9-c329ca6b12db
eed8a3fa-73e0-4a1e-b897-4235d77cae66

# 查看对应的pod的uid
[root@master1 pods]#kubectl get pod myweb-565cb68445-btlj8 -o yaml|grep -i uid
    uid: 4db8879a-ee0d-48d3-8b7e-675581eb4fa2
  uid: eed8a3fa-73e0-4a1e-b897-4235d77cae66      # -------- 匹配上面的路径uid
```



**emptyDir 特点如下：**

- 此为**默认存储类型**
- 此方式只能临时存放数据，不能实现数据持久化
- 跟随Pod初始化而来，开始是空数据卷
- Pod 被删除，emptyDir对应的宿主机目录也被删除，当然目录内的数据随之永久消除
- emptyDir 数据卷介质种类跟当前主机的磁盘一样。
- emptyDir 主机可以为同一个Pod内多个容器共享
- emptyDir 容器数据的临时存储目录主要用于数据缓存和**同一个Pod内的多个容器共享使用**



**emptyDir属性解析**

```bash
kubectl explain pod.spec.volumes.emptyDir
    medium       # 指定媒介类型，主要有default和memory两种
                 # 默认情况下，emptyDir卷支持节点上的任何介质，SSD、磁盘或网络存储，具体取决于自身所在Node的环境
                 # 将字段设置为Memory，让K8S使用tmpfs，虽然tmpfs快，但是Pod重启时，数据会被清除，并且设置的大小会被计入                    # Container的内存限制当中
    sizeLimit    # 当前存储卷的空闲限制，默认值为nil表示不限制
    
kubectl explain pod.spec.containers.volumeMounts
    mountPath    # 挂载到容器中的路径,此目录会自动生成
    name         # 指定挂载的volumes名称
    readOnly     # 是否只读挂载
    subPath      # 是否挂载子目录的路径,默认不挂载子目录
```



**配置示例**

```yaml
# volume配置格式
volumes:
- name: volume_name
  emptyDir: {}
  
# volume使用格式
containers:
- volumeMounts:
  - name: volume_name
    mountPath: /path/to/container/  # 容器内路径


# 示例1
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir: {}
    
# 示例2：
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir:
      medium: Memory
      sizeLimit: 500Mi
```



范例：在一个Pod中定义多个容器通过emptyDir共享数据

```yaml
[root@master1 storage] # vim storage-emptydir-2.yaml
apiVersion: v1
kind: Pod
metadata:
  name: storage-emptydir
spec:
  volumes:
  - name: nginx-data
    emptyDir: {}
  containers:
  - name: storage-emptydir-nginx
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumeMounts:
    - name: nginx-data
      mountPath: /usr/share/nginx/html/
  - name: storage-emptydir-busybox
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/busybox:1.32.0
    volumeMounts:
    - name: nginx-data
      mountPath: /data/
    command:
    - "/bin/sh"
    - "-c"
    - "while true; do date > /data/index.html; sleep 1; done"

# 应用
[root@master1 storage]#kubectl apply -f storage-emptydir-2.yaml 
pod/storage-emptydir created

# 查看Pod
[root@master1 storage] # kubectl get pod -o wide
NAME                     READY   STATUS              RESTARTS      AGE   IP             NODE    NOMINATED NODE   READINESS GATES
myweb-565cb68445-btlj8   1/1     Running             1 (11h ago)   27h   10.244.2.56    node2   <none>           <none>
myweb-565cb68445-c8drb   1/1     Running             1 (11h ago)   27h   10.244.1.104   node1   <none>           <none>
myweb-565cb68445-lj7bq   1/1     Running             1 (11h ago)   27h   10.244.3.111   node3   <none>           <none>
storage-emptydir         0/2     ContainerCreating   0             9s    <none>         node2   <none>           <none>

# 查看Pod的网络IP
[root@master1 storage] # kubectl get pod -o wide
NAME                     READY   STATUS    RESTARTS      AGE   IP             NODE    NOMINATED NODE   READINESS GATES
myweb-565cb68445-btlj8   1/1     Running   1 (11h ago)   27h   10.244.2.56    node2   <none>           <none>
myweb-565cb68445-c8drb   1/1     Running   1 (11h ago)   27h   10.244.1.104   node1   <none>           <none>
myweb-565cb68445-lj7bq   1/1     Running   1 (11h ago)   27h   10.244.3.111   node3   <none>           <none>
storage-emptydir         2/2     Running   0             14s   10.244.2.59    node2   <none>           <none>

# 测试效果
[root@master1 storage] #curl 10.244.2.59
Wed Dec 25 12:05:05 UTC 2024
[root@master1 storage] #curl 10.244.2.59
Wed Dec 25 12:05:06 UTC 2024
[root@master1 storage] #curl 10.244.2.59
Wed Dec 25 12:05:07 UTC 2024
[root@master1 storage] #curl 10.244.2.59
Wed Dec 25 12:05:08 UTC 2024
[root@master1 storage] #curl 10.244.2.59
Wed Dec 25 12:05:08 UTC 2024
```









### hostPath

hostPath 可以将**宿主机上的目录**挂载到 Pod 中作为数据的存储目录



**hostPath 一般用在如下场景：**

- 容器应用程序中某些文件需要永久保存

- Pod删除，hostPath数据对应在宿主机文件不受影响,即hostPath的生命周期和Pod不同,而和节点相同
- **宿主机和容器的目录都会自动创建**
- 某些容器应用需要用到容器的自身的内部数据，可将宿主机的/var/lib/[docker|containerd]挂载到 Pod中



**hostPath 使用注意事项：**

- 不同宿主机的目录和文件内容不一定完全相同，所以Pod迁移前后的访问效果不一样
- 不适合Deployment这种分布式的资源，更适合于DaemonSet
- 宿主机的目录不属于独立的资源对象的资源，所以**对资源设置的资源配额限制对hostPath目录无效**



**配置属性**

```bash
# 配置属性
kubectl explain pod.spec.volumes.hostPath
path                         # 指定哪个宿主机的目录或文件被共享给Pod使用
type                         # 指定路径的类型，一共有7种，默认的类型是没有指定
     空字符串                 # 默认配置，在关联hostPath存储卷之前不进行任何检查，如果宿主机没有对应的目录，会自动创建
     DirectoryCreate         # 宿主机上不存在，创建此0755权限的空目录，属主属组均为kubelet
     Directory               # 必须存在，挂载已存在目录
     FileOrCreate            # 宿主机上不存在挂载文件，就创建0644权限的空文件，属主属组均为kubelet
     File                    # 必须存在文件
     Socket                  # 事先必须存在Socket文件路径
     CharDevice              # 事先必须存在的字符设备文件路径
     BlockDevice             # 事先必须存在的块设备文件路径
     
     
# 配置格式：
  volumes:
  - name: volume_name
    hostPath:
      path: /path/to/host
      
# 示例：
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
  spec:
    containers:
    - image: registry.k8s.io/test-webserver
      name: test-container
      volumeMounts:
      - mountPath: /test-pod
        name: test-volume
    volumes:
    - name: test-volume
      hostPath:
        path: /data           # 宿主机上目录位置
        type: Directory       # 此字段为可选
```



范例：使用你主机的时区配置

```yaml
[root@master1 storage] # vim storage-hostpath-timezone.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-hostpath-timezone
spec:
  volumes:
  - name: timezone
    hostPath:
      path: /etc/timezone        # 此文件是影响时区
      type: File
  - name: localtime              # 此文件挂载失败，不影响时区
    hostPath:
      path: /etc/localtime
      type: File
  containers:
  - name: c01
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    command: ["sh", "-c", "sleep 3600"]
  - name: c02
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    command: ["sh", "-c", "sleep 3600"]
    volumeMounts:
    - name: timezone
      mountPath: /etc/timezone    # 容器此为文件是普通文件， 挂载节点目录成功
    - name: localtime
      mountPath: /etc/localtime   # 容器此为文件是软连接， 挂载节点目录失败

# 应用
[root@master1 storage] # kubectl apply -f storage-hostpath-timezone.yaml 
pod/pod-hostpath-timezone created

# 查看Pod
[root@master1 storage]#kubectl get pod
NAME                     READY   STATUS    RESTARTS      AGE
pod-hostpath-timezone    2/2     Running   0             3s

# 测试效果
[root@master1 storage] # kubectl exec pod-hostpath-timezone -c c01 -- date
Wed Dec 25 13:19:40 UTC 2024
[root@master1 storage] # kubectl exec pod-hostpath-timezone -c c02 -- date
Wed Dec 25 21:19:46 CST 2024

[root@master1 storage] # kubectl exec pod-hostpath-timezone -c c01 -- cat /etc/timezone
Etc/UTC
[root@master1 storage] # kubectl exec pod-hostpath-timezone -c c02 -- cat /etc/timezone
Asia/Shanghai
```



**范例：实现NFS服务**

```yaml
[root@master1 storage ]# cat storage-nfs-server.yaml
---
apiVersion: v1
kind: Service
metadata:
  name: nfs-server
  labels:
    app: nfs-server
spec:
  type: ClusterIP
  selector: 
    app: nfs-server
  ports:
    - name: tcp-2049            # 未显示指定tartPort，默认和port一致
      port: 2049
      protocol: TCP
    - name: udp-111
      port: 111
      protocol: UDP
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nfs-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nfs-server
  template:
    metadata:
      name: nfs-server
      labels:
        app: nfs-server
    spec:
      nodeSelector:
        "kubernetes.io/os": linux
        "server": nfs
      containers:
      - name: nfs-server
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nfs-server-alpine:12
        env:
        - name: SHARED_DIRECTORY
          value: "/exports"
        volumeMounts:
        - mountPath: /exports
          name: nfs-vol
        securityContext:
          privileged: true
        ports:                       # 声明性说明，无直接功能，除非Service配置了targetPort匹配这些端口
        - name: tcp-2049
          containerPort: 2049
          protocol: TCP
        - name: udp-111
          containerPort: 111
          protocol: UDP
      volumes:
      - name: nfs-vol
        hostPath:
          path: /nfs-vol
          type: DirectoryOrCreate
```



### 网络共享存储

和传统的方式一样, 通过 NFS 网络文件系统可以实现Kubernetes数据的网络存储共享

使用NFS提供的共享目录存储数据时，需要在系统中部署一个NFS环境，通过volume的配置，实现pod 内的容器间共享NFS目录。



**属性解析**

```bash
# 配置属性
kubectl explain pod.spec.volumes.nfs
server                                     #指定nfs服务器的地址
path                                       #指定nfs服务器暴露的共享地址
readOnly                                   #是否只能读，默认false

#配置格式：
 volumes:
  - name: <卷名称>
   nfs:
     server: nfs_server_address           #指定NFS服务器地址
     path: "共享目录"                      #指定NFS共享目录
     readOnly: false                      #指定权限

# 示例
apiVersion: v1
kind: Pod
metadata:
 name: test-pd
spec:
 containers:
  - image: registry.k8s.io/test-webserver
   name: test-container
   volumeMounts:
    - mountPath: /my-nfs-data
     name: test-volume
 volumes:
  - name: test-volume
   nfs:
     server: my-nfs-server.example.com
     path: /my-nfs-volume
     readonly: true
```



范例：使用集群外的NFS存储

```bash
#NFS服务器软件安装,10.0.0.131
[root@nfs ~]#apt update && apt install -y nfs-kernel-server 或者 nfs-server

#配置共享目录
[root@nfs ~]#mkdir /nfs-data
[root@nfs ~]#echo '/nfs-data *(rw,all_squash,anonuid=0,anongid=0)' >> /etc/exports

#重启服务
[root@nfs ~]#exportfs -r
[root@nfs ~]#exportfs -v

# 在所有kubernetes的worker节点充当NFS客户端，都需要安装NFS客户端软件
[root@node1 ~]#apt update && apt -y install nfs-common 或者 nfs-client
[root@node2 ~]#apt update && apt -y install nfs-common 或者 nfs-client
[root@node3 ~]#apt update && apt -y install nfs-common 或者 nfs-client

#测试访问
[root@node1 ~]#showmount -e 10.0.0.131
Export list for 10.0.0.101:
/nfs-data *

#编写资源配置文件
[root@master1 storage]#cat storage-nfs-1.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: storage

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-nfs
  namespace: storage
  labels:
    app: nginx-nfs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-nfs
  template:
    metadata:
      labels:
        app: nginx-nfs
    spec:
      volumes:
      - name: html
        nfs:
          server: nfs.mystical.org
          path: /nfs-data/nginx
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
        name: nginx
        volumeMounts:
        - name: html
          mountPath: /usr/share/nginx/html
          
# 注意：nfs中的域名解析，使用的式Node上的DNS，而不是COREDNS，所以需要在Node节点上将DNS指向私有DNS
```



### **PV和PVC**

![image-20241228171426884](D:\git_repository\cyber_security_learning\markdown_img\image-20241228171426884.png)

#### PV Persistent Volume 定义

工作中的存储资源一般都是独立于Pod的，将之称为资源对象Persistent Volume(PV)，是由管理员设置的存储，它是kubernetes集群的一部分，PV 是 Volume 之类的卷插件，**但具有独立于使用 PV 的 Pod  的生命周期**



**Persistent Volume 跟 Volume类似，区别就是：**

- PV 是集群级别的资源，负责将存储空间引入到集群中，通常由管理员定义
- PV 就是Kubernetes集群中的网络存储，不属于Namespace、Node、Pod等资源，但可以被它们访问
- **PV 属于Kubernetes 整个集群,即可以被所有集群的Pod访问**
- **PV是独立的网络存储资源对象，有自己的生命周期**
- PV 支持很多种volume类型,PV对象可以有很多常见的类型：本地磁盘、NFS、分布式文件系统...



**PV持久卷的类型**

PV持久卷是用插件的形式来实现的。Kubernetes目前支持一下插件：

- **cephfs** - CephFS volume
- **csi** - 容器存储接口（CSI）
- **fc** - Fibre Channel（FC）存储
- **hostPath** - HostPath卷（仅供单节点测试使用，不适用于多节点集群；请尝试使用lcoal作为替代）
- **iscsi** = iSCSI（SCSI over IP）存储
- **local** - 节点上挂载的本地存储设备
- **nfs** - 网络文件系统（NFS）存储
- **rbd** - Rados块设备（RBD）卷



#### PVC Persistent Volume Claim定义

Persistent Volume Claim(PVC) 是一个网络存储服务的**请求**。

**PVC 属于名称空间级别的资源**，只能被同一个名称空间的Pod引用

由用户定义，用于在空闲的PV中申请使用符合过滤条件的PV之一，与选定的PV是“一对一”的关系

用户在Pod上**通过pvc插件**请求绑定使用定义好的PVC资源

Pod能够申请特定的CPU和MEM资源，但是Pod只能通过PVC到PV上请求一块独立大小的网络存储空 间，而PVC 可以动态的根据用户请求去申请PV资源，不仅仅涉及到存储空间，还有对应资源的访问模 式，对于真正使用存储的用户不需要关心底层的存储实现细节，只需要直接使用 PVC 即可。



#### Pod、PV、PVC 关系

![image-20241228172519330](D:\git_repository\cyber_security_learning\markdown_img\image-20241228172519330.png)



**前提：**

- 存储管理员配置各种类型的PV对象
- Pod、PVC 必须在同一个命名空间



**用户需要存储资源的时候：**

- 用户根据资源需求创建PVC，由PVC自动匹配(权限、容量)合适的PV对象
- PVC 允许用户按需指定期望的存储特性，并以之为条件，按特定的条件顺序进行PV的过滤 
  - VolumeMode → LabelSelector → StorageClassName → AccessMode → Size 
- 在Pod内部通过 PVC 将 PV 绑定到当前的空间，进行使用
- 如果用户不再使用存储资源，解绑 PVC 和 Pod 即可



**PV和PVC的生命周期**

![image-20241229204228667](D:\git_repository\cyber_security_learning\markdown_img\image-20241229204228667.png)





**PV和PVC的配置流程**

![image-20241229204254515](D:\git_repository\cyber_security_learning\markdown_img\image-20241229204254515.png)



- 用户创建了一个包含 PVC 的 Pod，该 PVC 要求使用动态存储卷
- Scheduler 根据 Pod 配置、节点状态、PV 配置等信息，把 Pod 调度到一个合适的 Worker 节点上
- PV 控制器 watch 到该 Pod 使用的 PVC 处于 Pending 状态，于是调用 Volume Plugin(in-tree)创 建存储卷，并创建 PV 对象(out-of-tree 由 External Provisioner 来处理)
- AD 控制器发现 Pod 和 PVC 处于待挂接状态，于是调用 Volume Plugin 挂接存储设备到目标 Worker 节点上
- 在 Worker 节点上，Kubelet 中的 Volume Manager 等待存储设备挂接完成，并通过 Volume  Plugin 将设备挂载到全局目录：**/var/lib/kubelet/pods/[pod_uid]/volumes/kubernetes.io~iscsi/[PVname] (以iscsi为例)**
- Kubelet 通过 Docker 启动 Pod 的 Containers，用 bind mount 方式将已挂载到本地全局目录的卷 映射到容器中



![image-20241229204525669](D:\git_repository\cyber_security_learning\markdown_img\image-20241229204525669.png)





#### PV和PVC管理

**PV的Provison 置备（创建）方法**

- **静态**：集群管理员预先手动创建一些 PV。它们带有可供群集用户使用的实际存储的细节
- **动态**：集群尝试根据用户请求动态地自动完成创建卷。此配置基于 StorageClasses：PVC 必须请 求存储类，并且管理员必须预先创建并配置该 StorageClasses才能进行动态创建。声明该类为空字 符串 ""， 可以有效地禁用其动态配置。



##### PV属性

```bash
# PV作为存储资源，主要包括存储能力，访问模式，存储类型，回收策略等关键信息，注意：PV的名称不支持大写
kubectl explain pv.spec
    capacity                            # 定义pv使用多少资源，仅限于空间的设定
    accessModes                         # 访问模式,支持单路读写，多路读写，多路只读，单Pod读写，可同时支持多种模式
    volumeMode                          # 文件系统或块设备,默认文件系统
    mountOptions                        # 挂载选项,比如:["ro", "soft"]    
    persistentVolumeReclaimPolicy       # 资源回收策略，主要三种Retain、Delete、Recycle 
    storageClassName                    # 存储类的名称,如果配置必须和PVC的storageClassName相同才能绑定
    
#注意:PersistentVolume 对象的名称必须是合法的 DNS 子域名

# 示例
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0003
  labels:
    release: "stable"    # 便签可以支持匹配过滤PVC
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow  # 必须和PVC相同
  mountOptions:
    - hard
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2  
```



##### PVC属性

```bash
#PVC属性信息,与所有空间都能使用的PV不一样，PVC是属于名称空间级别的资源对象，即只有特定的资源才能使用
kubectl explain pvc.spec
    accessModes            # 访问模式  
    resources              # 资源限制
    volumeMode             # 后端存储卷的模式,文件系统或块,默认为文件系统
    volumeName             # 指定绑定的卷(pv)的名称

kubectl explain pod.spec.volumes.persistentVolumeClaim
    claimName              # 定义pvc的名称,PersistentVolumeClaim 对象的名称必须是合法的 DNS 子域名
    readOnly               # 设定pvc是否只读
    storageClassName       # 存储类的名称,如果配置必须和PV的storageClassName相同才能绑定
    selector                # 标签选择器实现选择绑定PV
    
# storageClassName类
PVC可以通过为storageClassName属性设置StorageClass的名称来请求特定的存储类。只有所请求的类的PV的StorageClass值与PVC设置相同，才能绑定

# selector选择算符
PVC可以设置标签选择算符,来进一步过滤卷集合。只有标签与选择算符相匹配的卷能够绑定到PVC上。选择算符包含两个字段：

matchLabels - 卷必须包含带有此值的标签
 
matchExpressions - 通过设定键（key）、值列表和操作符（operator） 来构造的需求。合法的操作符
有 In、NotIn、Exists 和 DoesNotExist。
来自 matchLabels 和 matchExpressions 的所有需求都按逻辑与的方式组合在一起。 这些需求都必须被满足才被视为匹配。

# 示例：
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
  storageClassName: slow  # 必须和PV相同
  selector：
    matchLabels:
      release: "stable"
    matchExpressions:
    - {key: environment, operator: In, values: [dev]}
```





##### 属性进阶

**PV状态**

PV 有生命周期,自然也有自己特定的状态

注意：这个过程是单向过程，不能逆向

![image-20241229210212463](D:\git_repository\cyber_security_learning\markdown_img\image-20241229210212463.png)

| 状态       | 解析                                                  |
| ---------- | ----------------------------------------------------- |
| Availabled | 空闲状态，表示PV没有被其他PVC对象使用                 |
| Bound      | 绑定状态，表示PV已经被其他PVC对象使用                 |
| Released   | 未回收状态，表示PVC已经被删除了，但是资源还没有被回收 |
| Faild      | 资源回收失败                                          |



![image-20241229210316627](D:\git_repository\cyber_security_learning\markdown_img\image-20241229210316627.png)





**AccessMode 访问模式**

AccessModes 是用来对 PV 进行访问模式的设置，用于描述用户应用对存储资源的访问权限，访问权限包括

| 类型                   | 解析                                                         |
| ---------------------- | ------------------------------------------------------------ |
| ReadWriteOnce（RWO）   | 单节点读写,卷可以被一个节点以读写方式挂载。 <br />ReadWriteOnce 访问模式仍然可以在同一节点上运行的多个 Pod <br />访问该卷即不支持并行(非并发)写入 |
| ReadOnlyMany（ROX）    | 多节点只读                                                   |
| ReadWriteMany（RWX）   | 多节点读写                                                   |
| ReadWriteOncePod(RWOP) | 卷可以被单个 Pod 以读写方式挂载。 如果你想确保整个集群中只 有一个 Pod 可以读取或写入该 PVC， 请使用 ReadWriteOncePod 访问模式。单Pod读写,v1.22版以后才支 持,v1.29版stable可用 |



注意：

- 不同的后端存储支持不同的访问模式，所以要根据后端存储类型来设置访问模式。
- 一些 PV 可能支持多种访问模式，但是在挂载的时候只能使用一种访问模式，多种访问模式是不会 生效的



**PV资源回收策略**

PV 三种资源回收策略

当 Pod 结束 volume 后可以回收资源对象删除PVC，而绑定关系就不存在了，当绑定关系不存在后这个 PV需要怎么处理，而PersistentVolume 的回收策略告诉集群在存储卷声明释放后应如何处理该PV卷。 目前，volume 的处理策略有保留、回收或删除。

当PVC被删除后, Kubernetes 会自动生成一个recycler-for-的Pod实现回收工作,但Retain策 略除外

回收完成后,PV的状态变为Availabled,如果其它处于Pending状态的PVC和此PV条件匹配,则可以再次此 PV进行绑定

| 类型    | 解析                                                         |
| ------- | ------------------------------------------------------------ |
| Retain  | 保留PV和存储空间数据，后续数据的删除需要人工干预，**一般推荐使用此项**，对于**手动创建的PV此为默认值** |
| Delete  | 相关的存储实例PV和数据都一起删除。需要支持删除功能的存储才能实现，**动态存储 一般会默认采用此方式** |
| Recycle | **当前此项已废弃**，保留PV，但清空存储空间的数据，仅支持NFS和hostPath |



##### PV和PVC的使用流程

实现方法

- 准备存储
- 基于存储创建PV
- 根据需求创建PVC: PVC会根据capacity和accessModes及其它条件自动找到相匹配的PV进行绑定, 一个PVC对应一个PV
- 创建Pod
  - 在Pod中的 volumes 指定调用上面创建的 PVC 名称
  - 在Pod中的容器中的volumeMounts指定PVC挂载容器内的目录路径





##### 案例

**PV和PVC使用**

```yaml
[root@master1 storage] # cat storage-mysql-pv-pvc.yaml 
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 20Gi
  accessModes:
  - ReadWriteOnce
  hostPath:
    path: "/mnt/data"

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
spec:
  storageClassName: manual
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi

---
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  ports:
  - port: 3306
  selector:
    app: mysql
  clusterIP: None
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
spec:
  selector:
    matchLabels:
      app: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
        name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: "123456"
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-persistent-storage
        persistentVolumeClaim:
          claimName: mysql-pv-claim

# 安装mysql客户端
[root@master1 storage] #apt install -y mysql-client

# 通过svc域名，解析出mysql的pod的IP
[root@master1 storage]#nslookup mysql.default.svc.cluster.local 10.96.0.10
Server:		10.96.0.10
Address:	10.96.0.10#53

Name:	mysql.default.svc.cluster.local
Address: 10.244.2.73

# 测试访问
[root@master1 storage] # mysql -h10.244.2.73 -p123456 -uroot

# 查看Mysql的Pod所在主机
[root@master1 storage] # kubectl get pod -o wide
NAME                     READY   STATUS    RESTARTS   AGE     IP            NODE    NOMINATED NODE   READINESS GATES
mysql-7ffdfbdf6f-fsv6c   1/1     Running   0          7m34s   10.244.2.73   node2   <none>           <none>

# 查看node2节点的/mnt/data，自动创建/mnt/data目录
[root@node2 ~] # cd /mnt/data/
[root@node2 data]#ls
 auto.cnf        client-cert.pem      ib_logfile0     mysql.sock           sys
 binlog.000001   client-key.pem       ib_logfile1     performance_schema   undo_001
 binlog.000002  '#ib_16384_0.dblwr'   ibtmp1          private_key.pem      undo_002
 binlog.index   '#ib_16384_1.dblwr'  '#innodb_temp'   public_key.pem
 ca-key.pem      ib_buffer_pool       mysql           server-cert.pem
 ca.pem          ibdata1              mysql.ibd       server-key.pem
```



范例：以NFS类型创建一个3G大小的存储资源对象PV

```yaml
# 准备NFS共享存储
[root@master1 ~] #mkdir /nfs-data
[root@master1 ~] #apt -y install nfs-server
[root@master1 ~] #echo "/nfs-data *(rw,no_root_squash)" >> /etc/exports
[root@master1 ~] #exportfs -r
[root@master1 ~] #exportfs -v
/nfs-data     <world>
(rw,wdelay,no_root_squash,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_a
ll_squash)

#在所有worker节点安装nfs软件
[root@node1 ~] #apt -y install nfs-common

# 准备PV，定制一个具体空间大小的存储对象
[root@master1 ~] #cat storage-pv.yaml 
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-test
spec:
  capacity:
    storage: 3Gi
  accessModes:
    - ReadWriteOnce
    - ReadWriteMany
    - ReadOnlyMany
  nfs:
    path: /nfs-data
    server: nfs.mystical.org # 需要名称解析

# 应用
[root@master1 ~] #kubectl apply -f storage-pv.yaml
persistentvolume/pv-test created

# 查看
[root@master1 ~] #kubectl get pv
NAME     CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS     CLAIM   
STORAGECLASS   REASON   AGE
pv-test   3Gi       RWO,ROX,RWX   Retain           Available                   
                7s
# 结果显示：虽然我们在创建pv的时候没有指定回收策略，而其策略自动帮我们配置了Retain

# 准备PVC，定义一个资源对象，请求空间1Gi
[root@master1 ~] #cat storage-pvc.yaml 
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-test
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
#注意：请求的资源大小必须在 pv资源的范围内

[root@master1 ~] #kubectl apply -f storage-pvc.yaml

#结果显示：一旦启动pvc会自动去搜寻合适的可用的pv，然后绑定在一起
#如果pvc找不到对应的pv资源，状态会一直处于pending

# 准备Pod
[root@master1 ~] #cat storage-nginx-pvc.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: Pod-nginx
spec:
  volumes:
  - name: volume-nginx
    persistentVolumeClaim:
      claimName: pvc-test
  containers:
  - name: pvc-nginx-container
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumeMounts:
    - name: volume-nginx
      mountPath: "/usr/share/nginx/html"
      
#属性解析：
#spec.volumes 是针对pod资源申请的存储资源来说的，这里使用的主要是pvc的方式。
#spec.containers.volumeMounts 是针对pod资源对申请的存储资源的信息。将pvc挂载的容器目录 
```



**案例： PVC自动绑定相匹配的PV,PVC和 PV 是自动关联的，而且会匹配容量和权限**

```yaml
[root@master1 ~] # mkdir /nfs-data/data{1..3}
[root@master1 ~] # cat /etc/exports
/nfs-data *(rw,no_root_squash)

# PV清单文件
[root@master1 ~] # cat storage-multi-pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-nfs-1
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  persistentVolumeclaimPolicy: Retain
  nfs:
    path: "/nfs-data/data1"
    server: nfs.mystical.org
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-nfs-2
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
  - ReadOnlyMany
  persistentVolumeReclaimPolicy: Retain
  nfs:
    path: "/nfs-data/data2"
    server: nfs.mystical.org
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-nfs-3
spec:
  capacity:
    storage: 1Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  nfs:
    path: "/nfs-data/data3"
    server: nfs.mystical.org

# 应用
[root@master1 ~] # kubectl apply -f storage-multi-pv.yaml

# kubectl get pv
[root@master1 storage] # kubectl get pv
NAME       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
pv-nfs-1   5Gi        RWX            Retain           Available                          <unset>                          3s
pv-nfs-2   5Gi        ROX            Retain           Available                          <unset>                          2m13s
pv-nfs-3   1Gi        RWO            Retain           Available                          <unset>                          2m13s


# PVC清单文件
[root@master1 ~] # cat storage-multi-pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-demo-1
  namespace: default
spec:
  accessModes: ["ReadWriteMany"]
  volumeMode: Filesystem
  resources:
    requests:
      storage: 3Gi
    limits:
      storage: 10Gi
      
# 应用
[root@master1 storage] # kubectl apply -f storage-multi-pvc.yaml 
persistentvolumeclaim/pvc-demo-1 created

# 查看PVC
[root@master1 storage] # kubectl get pvc
NAME         STATUS   VOLUME     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
pvc-demo-1   Bound    pv-nfs-1   5Gi        RWX                           <unset>                 14s

# 自动绑定PVC至容器和权限都匹配的PV
[root@master1 storage]#kubectl get pv
NAME       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM                STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
pv-nfs-1   5Gi        RWX            Retain           Bound       default/pvc-demo-1                  <unset>                          3m7s
pv-nfs-2   5Gi        ROX            Retain           Available                                       <unset>                          5m17s
pv-nfs-3   1Gi        RWO            Retain           Available                                       <unset>                          5m17s
```



##### 强制删除

生产中，对于存储资源的释放，最好按照流程来，即先清空应用，然后在清空pvc，但是生产中，经常遇 到应用资源意外终止或者其他情况，导致我们的pvc资源没有使用，而且也没有清空

有多种方式解决，最常用的一种方式就是，在所有的应用pod中增加一个prestop的钩子函数，从而让我们的应用资源合理的清空

**而对于特殊的异常情况，我们还有另外一种策略，即强制清空,但是一般不推荐使用。**

```yaml
#对于这种无论何种方法都无法删除的时候，我们可以通过修改配置属性的方式，从记录中删除该信息
[root@master1 ~]#kubectl patch pv pv-nfs-1 -p '{"metadata":{"finalizers":null}}'
persistentvolume/pv-nfs-1 patched
```



##### subPath

上面范例中的nginx首页存放在/nfs-data的一级目录中，但是生产中，一个NFS共享资源通常是给多个应 用来使用的，比如需要定制每个app的分配单独的子目录存放首页资源，但是如果我们采用PV实现定制 的方式，就需要多个PV,此方式有些太繁琐了 

**可以通过subPath实现针对不同的应用对应子目录的挂载**

volumeMounts.subPath 属性可用于指定所引用的卷内的子路径，而不是其根路径。

下面例子展示了如何配置某包含 LAMP 堆栈（Linux Apache MySQL PHP）的 Pod 使用同一共享卷。 **此示例中的 subPath 配置不建议在生产环境中使用**。 PHP 应用的代码和相关数据映射到卷的 html 文 件夹，MySQL 数据库存储在卷的 mysql 文件夹中：

```yaml
[root@master1 storage] # cat storage-nginx-pvc-subdir.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-nginx-1
spec:
  volume:
  - name: nginx-volume
    persistentVolumeClaim:
      claimName: pvc-test
  containers:
  - name: nginx-pv
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumeMounts:
    - name: nginx-volume
      mountPath: "/usr/share/nginx/html"
      subPath: web1
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-nginx-2
spec:
  volumes:
  - name: nginx-volume
    persistentVolumeClaim:
      claimName: pvc-test
  containers:
  - name: nginx-flask
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumeMounts:
    - name: nginx-volume
      mountPath: "/usr/share/nginx/html"
      subPath: web2
```





### StorageClass

#### storageClass说明

对于 PV 和 PVC 的使用整个过程是比较繁琐的，不仅需要自己定义PV和PVC还需要将其与Pod进行关 联，而且对于PV和PVC的适配我们也要做好前提规划，而生产环境中，这种繁琐的事情是有悖于我们使 用kubernetes的原则的，而且这种方式在很大程度上并不能满足我们的需求，而且不同的应用程序对于 存储性能的要求可能也不尽相同，比如读写速度、并发性能等，比如我们有一个应用需要对存储的并发 度要求比较高，而另外一个应用对读写速度又要求比较高，特别是对于 StatefulSet 类型的应用简单的来 使用静态的 PV 就很不合适了，这种情况下就需要用到**动态 PV**。



Kubernetes 引入了一个**新的资源对象：StorageClass**，通过 StorageClass 的定义，管理员可以将存储资源定义为某种类型的资源，比如存储质量、快速存储、慢速存储等，为了满足不同用户的多种多样的 需求，用户根据 StorageClass 的描述就可以非常直观的知道各种存储资源的具体特性了，这样就可以根据应用的特性去申请合适的存储资源了。

所以,StorageClass提供了一种资源使用的描述方式，使得管理员能够描述提供的存储的服务质量和等级，进而做出不同级别的存储服务和后端策略。

StorageClass 用于定义不同的存储配置和属性，以供 PersistentVolume（PV）的动态创建和管理。它 为开发人员和管理员提供了一种在不同的存储提供商之间抽象出存储配置的方式。

**在 Kubernetes 中，StorageClass 是集群级别的资源，而不是名称空间级别。**

PVC和PV可以属于某个SC，也可以不属于任何SC,PVC只能够在同一个storageClass中过滤PV



**能建立绑定关系的PVC和PV一定满足如下条件：**

- 二者隶属于同个SC
- 二者都不属于任何SC



**StorageClass这个API对象可以自动创建PV的机制,即:Dynamic Provisioning**



**StorageClass对象会定义下面两部分内容:**

- PV的属性.比如,存储类型,Volume的大小等
- 创建这种PV需要用到的存储插件

提供以上两个信息,Kubernetes就能够根据用户提交的PVC,找到一个对应的StorageClass,之后 Kubernetes就会调用该StorageClass声明的存储插件,进而创建出需要的PV.



要使用 StorageClass，就得**安装对应的自动配置程序**，比如存储后端使用的是 nfs，那么就需要使用到 一个 nfs-client 的自动配置程序，也称为 Provisioner，这个程序使用已经配置好的 nfs 服务器，来自动 创建持久卷 PV。



#### storageClass API

每个 StorageClass 都包含 **provisioner** 、 **parameters** 和 **reclaimPolicy** 字段， 这些字段会在 StorageClass 需要动态制备 PersistentVolume 时会使用到。

StorageClass 对象的命名很重要，用户使用这个命名来请求生成一个特定的类。 当创建 StorageClass  对象时，管理员设置 StorageClass 对象的命名和其他参数。

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
reclaimPolicy: Retain
allowVolumeExpansion: true
mountOptions:
- debug
volumeBindingMode: Immediate | WaitForFirstConsumer（延迟绑定，只有Pod准备好才绑定）

# 管理员可以为没有申请绑定到特定StorageClass的PVC指定一个默认的存储类
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
  storageClassName: standard
  selector:
    matchLabels:
      release: "stable"
    matchExpressions:
      - {key: environment, operator: In, values: [dev]}
```



#### 存储制备器

每个 StorageClass 都有**一个制备器（Provisioner）**，用于提供存储驱动，用来决定使用哪个卷插件制备 PV。 **该字段必须指定**

| 卷插件         | 内置制备器 |                           配置示例                           |
| :------------- | :--------: | :----------------------------------------------------------: |
| AzureFile      |     ✓      | [Azure File](https://kubernetes.io/zh-cn/docs/concepts/storage/storage-classes/#azure-file) |
| CephFS         |     -      |                              -                               |
| FC             |     -      |                              -                               |
| FlexVolume     |     -      |                              -                               |
| iSCSI          |     -      |                              -                               |
| Local          |     -      | [Local](https://kubernetes.io/zh-cn/docs/concepts/storage/storage-classes/#local) |
| NFS            |     -      | [NFS](https://kubernetes.io/zh-cn/docs/concepts/storage/storage-classes/#nfs) |
| PortworxVolume |     ✓      | [Portworx Volume](https://kubernetes.io/zh-cn/docs/concepts/storage/storage-classes/#portworx-volume) |
| RBD            |     ✓      | [Ceph RBD](https://kubernetes.io/zh-cn/docs/concepts/storage/storage-classes/#ceph-rbd) |
| VsphereVolume  |     ✓      | [vSphere](https://kubernetes.io/zh-cn/docs/concepts/storage/storage-classes/#vsphere) |





#### Local Volume



#####  hostPath存在的问题

过去我们经常会通过hostPath volume让Pod能够使用本地存储，将Node文件系统中的文件或者目录挂 载到容器内，但是hostPath volume的使用是很难受的，并不适合在生产环境中使用。

- 由于集群内每个节点的差异化，要使用hostPath Volume，我们需要通过**NodeSelector**等方式进行精确调度，这种事情多了，你就会不耐烦了。

- 注意DirectoryOrCreate和FileOrCreate两种类型的hostPath，当Node上没有对应的 File/Directory时，你需要保**证kubelet有在 Node上Create File/Directory的权限**。
- 另外，如果Node上的文件或目录是由root创建的，挂载到容器内之后，你通常还要保证容器内进程有权限对该文件或者目录进行写入，比如你需要以root用户启动进程并运行于privileged容器， 或者你需要事先修改好Node上的文件权限配置。
- **Scheduler并不会考虑hostPath volume的大小，hostPath也不能申明需要的storagesize**，这样调度时存储的考虑，就需要人为检查并保证。



#####  Local PV 使用场景

Local Persistent Volume 并不适用于所有应用。它的适用范围非常固定，比如：高优先级的系统应用， 需要在多个不同节点上存储数据，而且对 I/O 要求较高。Kubernetes 直接使用宿主机的本地磁盘目录 ，来持久化存储容器的数据。它的**读写性能相比于大多数远程存储来说，要好得多，尤其是 SSD 盘**。

典型的应用包括：分布式数据存储比如 MongoDB，分布式文件系统比如 GlusterFS、Ceph 等，以及需 要在本地磁盘上进行大量数据缓存的分布式应用，其次使用 Local Persistent Volume 的应用必须具备 数据备份和恢复的能力，允许你把这些数据定时备份在其他位置。



#####  Local PV 的实现

LocalPV 的实现可以理解为我们前面使用的 hostpath 加上 nodeAffinity ，比如：在宿主机 NodeA 上 提前创建好目录 ，然后在定义 Pod 时添加 nodeAffinity=NodeA ，指定 Pod 在我们提前创建好目录的 主机上运行。但是**我们绝不应该把一个宿主机上的目录当作 PV 使用**，因为本地目录的磁盘随时都可能 被应用写满，甚至造成整个宿主机宕机。而且，不同的本地目录之间也缺乏哪怕最基础的 I/O 隔离机 制。所以，**一个 Local Persistent Volume 对应的存储介质，一定是一块额外挂载在宿主机的磁盘或者 块设备**（“额外” 的意思是，它不应该是宿主机根目录所使用的主硬盘）。这个原则，我们可以称为 “**一个 PV 一块盘**”。





#####  Local PV 和常规 PV 的区别

对于常规的 PV，Kubernetes 都是先调度 Pod 到某个节点上，然后再持久化 这台机器上的 Volume 目 录。而 Local PV，则需要运维人员提前准备好节点的磁盘。它们在不同节点上的挂载情况可以完全不 同，甚至有的节点可以没这种磁盘。所以调度器就必须能够知道所有节点与 Local Persistent Volume  对应的磁盘的关联关系，然后根据这个信息来调度 Pod。也就是在调度的时候考虑 Volume 分布。



k8s v1.10+以上的版本中推出local pv方案。Local volume 允许用户通过标准 PVC 接口以简单且可移植 的方式访问 node 节点的本地存储。 PV 的定义中需要包含描述节点亲和性的信息，k8s 系统则使用该信 息将容器调度到正确的 node 节点。

在 Kubernetes 中，HostPath 和 Local Volume 都可以用于将主机上的文件系统挂载到容器内部。虽然 它们有一些相似之处，但是它们之间也有一些重要的区别。

HostPath卷类型会直接挂载主机的文件系统到Pod中，这个文件系统可以是一个文件或者是一个目录。 当Pod被调度到一个节点上时，该节点上的文件系统就会被挂载到Pod中。这使得可以很容易地在容器 内部访问主机上的文件，例如主机上的日志或配置文件。但是，使用 HostPath 卷类型可能会存在安全 风险，因为容器可以访问主机上的所有文件和目录，包括其他容器的文件。

相比之下，Local Volume 卷类型只能将节点上的一个目录挂载到容器内部。当Pod被调度到一个节点上 时，Kubernetes 会为该节点创建一个唯一的目录，并将该目录挂载到 Pod 中。因为每个 Pod 只能访问 其本地的 Local Volume 目录，所以这种卷类型更加安全。但是，如果节点故障或被删除，Local  Volume 中的数据将会丢失。因此，使用 Local Volume 卷类型需要谨慎，需要确保有备份机制或持久化 存储。



**local Volume 默认不支持动态配置，只能用作静态创建的持久卷国。但可以采有第三方方案实现动态配置**

local 类型的PV是一种更高级的本地存储抽象，它可以**允许通过StorageClass来进行管理**。

与 hostPath 卷相比， local 卷能够以持久和可移植的方式使用，而无需手动将 Pod 调度到节点。

同样使用节点上的本地存储，但相比于 hostPath ， l**ocal Volume可以声明为动态供应，并且可以利 用节点标签（nodeAffinity）实现存储亲和性，确保Pod调度到包含所需数据的节点上**。而hostPath卷 在Pod重建后可能会调度至新的节点，而导致旧的数据无法使用



然而， local 卷仍然取决于底层节点的可用性，并不适合所有应用程序。 如果节点变得不健康，那么 local 卷也将变得不可被 Pod 访问。使用它的 Pod 将不能运行。 使用 local 卷的应用程序必须能够 容忍这种可用性的降低，以及因底层磁盘的耐用性特征而带来的潜在的数据丢失风险



##### 创建Local PV

下面是一个使用 local 卷和 nodeAffinity 的持久卷示例：

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage
provisioner: kubernetes.io/no-provisioner #表示该存储类不使用任何 provisioner，即不支持动态分配持久卷。这意味着管理员需要手动创建并管理持久卷。
volumeBindingMode: WaitForFirstConsumer #延迟绑定，只有Pod准备好才绑定PV至PVC，否则PVC处于Pending状态

---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: example-pv
spec:
  capacity:
    storage: 100Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete
  sotrageClassName: local-storage
  local:
    path: /mnt/disks/ssd1
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - example-node
```

使用 local 卷时，你需要设置 PersistentVolume 对象的 nodeAffinity 字段。 Kubernetes 调度器 使用 PersistentVolume 的 nodeAffinity 信息来将使用 local 卷的 Pod 调度到正确的节点。

使用 local 卷时，**建议创建一个 StorageClass 并将其 volumeBindingMode 设置为 WaitForFirstConsumer** 。要了解更多详细信息，请参考 local StorageClass 示例。 延迟卷绑定的操作 可以确保 Kubernetes 在为 PersistentVolumeClaim 作出绑定决策时，会评估 Pod 可能具有的其他节点 约束，例如：如节点资源需求、节点选择器、Pod 亲和性和 Pod 反亲和性。



**使用Local卷流程**

- 创建PV，使用 nodeAffinity 指定绑定的节点提供存储
- 创建 PVC，绑定PV的存储条件
- 创建Pod，引用前面的PVC和PV实现Local 存储



##### 案例：基于StorageClass实现Local卷

```yaml
#事先准备目标节点准备目录，对于本地存储Kubernetes 本身并不会自动创建路径，这是因为Kubernetes 不能控制节点上的本地存储，因此无法自动创建路径。
[root@node2 ~] # mkdir -p /data/www

#如果没有准备目录，会出现下面提示错误
[root@master1 yaml]#kubectl describe pod pod-sc-local-demo
Events:
 Type     Reason           Age               From               Message
  ----     ------            ----              ----               -------
 Warning FailedScheduling 2m2s             default-scheduler  0/4 nodes are 
available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/4 
nodes are available: 4 No preemption victims found for incoming pod..
 Normal   Scheduled         2m1s             default-scheduler Successfully 
assigned default/pod-sc-local-demo to node2.wang.org
 Warning FailedMount       56s (x8 over 2m) kubelet           
MountVolume.NewMounter initialization failed for volume "example-pv" : path 
"/data/www" does not exist

#准备清单文件, #kubernetes内置了Local的置备器，所以下面StorageClass资源可以不创建
[root@master1 yaml] # cat storage-sc-local-pv-pvc-pod.yaml
---
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: waitForFirstConsumer #延迟绑定，只有Pod启动后再绑定PV到Pod所在节点，否则PVC处于Pending状态

---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-sc-local
spec:
  capacity:
    storage: 100Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete
  storageClassName: local-storage
  local:
    path: /data/www/
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - node2.mystical.org
          
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-sc-local
spec:
  storageClassName: local-storage
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 100Mi

---
apiVersion: v1
kind: Pod
metadata:
  name: pod-sc-local-demo
spec:
  containers:
  - name: pod-sc-local-demo
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumeMounts:
    - name: pvc-sc-local
      mountPath: "/usr/share/nginx/html"
  restartPolicy: "Nerver"
  volumes:
  - name: pvc-sc-local
    persistentVolumeClaim:
      claimName: pvc-sc-local
      
#应用清单文件
[root@master1 yaml] # kubectl apply -f storage-sc-local-pv-pvc-pod.yaml
persistentvolume/pv-sc-local created
persistentvolumeclaim/pvc-sc-local created
pod/pod-sc-local-demo created

# 这里Pod的节点调度取决于PV定义的节点位置，是由于PV上定义了node2节点，因此Pod必然调度到node2节点
# 而hostPath是先确定Pod，然后在根据Pod调度到的节点来确定路径。
# 而且PV可以限定大小，而PV无法限定
```



#### NFS StorageClass

##### NFS的存储制备器方案

NFS 的自动配置程序 Provisioner 可以通过不同的项目实现,比如：

- **csi-driver-nfs**

  ```http
  https://github.com/kubernetes-csi/csi-driver-nfs
  ```

  

- **nfs-client-provisioner**

  - nfs-client-provisioner 是一个自动配置卷程序，它使用现有的和已配置的 NFS 服务器来支持通过 PVC动态配置 PV
  - nfs-client-provisioner **目前已经不提供更新**，nfs-client-provisioner 的 Github 仓库当前已经迁移 到 NFS-Subdir-External-Provisioner的仓库

  ```http
  https://github.com/kubernetes-retired/external-storage/tree/master/nfs-client
  https://github.com/kubernetes-sigs/sig-storage-lib-external-provisioner
  ```



- **NFS-Subdir-External-Provisioner（官方推荐）**

  - 此组件是由Kubernetes SIGs 社区开发,也是Kubernetes官方推荐实现
  - 是对 nfs-client-provisioner 组件的扩展

  ```http
  https://kubernetes.io/docs/concepts/storage/storage-classes/#nfs
  ```

  - NFS-Subdir-External-Provisioner 是一个自动配置卷程序，可以在 NFS 服务器上通过PVC动态创 建和配置 Kubernetes 持久卷
  - PV命名规则如下

  ```bash
  自动创建的 PV 以${namespace}-${pvcName}-${pvName} 命名格式创建在 NFS 服务器上的共享数据目录中
  当这个 PV 被回收后会以 archieved-${namespace}-${pvcName}-${pvName} 命名格式存在NFS 服务器中
  ```



- **NFS Ganesha server and external provisioner**

  ```http
  https://github.com/kubernetes-sigs/nfs-ganesha-server-and-external-provisioner
  ```

  - nfs-ganesha-server-and-external-provisioner 是 Kubernetes 1.14+ 的树外动态配置程序。 您可以使用它快速轻松地部署几乎可以在任何地方使用的共享存储。



##### 案例: 基于 nfs-subdir-external-provisione 创建 NFS 共享存储的 storageclass

部署相关文件

```http
https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner
https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner/tree/master/deploy
https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner?tab=readme-ov-file#manuall
```



创建NFS共享存储的storageclass步骤如下

- 创建 NFS 共享
- 创建 **Service Account** 并授予管控NFS provisioner在k8s集群中运行的权限
- 部署 NFS-Subdir-External-Provisioner 对应的 **Deployment**
- 创建 StorageClass 负责建立PVC并调用NFS provisioner进行预定的工作,并让PV与PVC建立联系
- 创建 PVC 时自动调用SC创建PV



**创建NFS服务**

```bash
[root@master1 ~] # apt update && apt -y install nfs-server
[root@master1 ~] # systemctl status nfs-server.service 
● nfs-server.service - NFS server and services
     Loaded: loaded (/lib/systemd/system/nfs-server.service; enabled; vendor 
preset: enabled)
     Active: active (exited) since Thu 2021-09-29 09:28:41 CST; 5min ago
   Main PID: 64029 (code=exited, status=0/SUCCESS)
     Tasks: 0 (limit: 2236)
     Memory: 0B
     CGroup: /system.slice/nfs-server.service
9月 29 09:28:40 master1.wang.org systemd[1]: Starting NFS server and services...
9月 29 09:28:41 master1.wang.org systemd[1]: Finished NFS server and services.


[root@master1 ~]#mkdir -pv /data/sc-nfs 
[root@master1 ~]#chown 777 /data/sc-nfs
[root@master1 ~]#vim /etc/exports
#授权worker节点的网段可以挂载
#/data/sc-nfs *(rw,no_root_squash,all_squash,anonuid=0,anongid=0) 
/data/sc-nfs *(rw,no_root_squash)

[root@master1 ~]#exportfs -r
[root@master1 ~]#exportfs -v
/data/sc-nfs <world>
(sync,wdelay,hide,no_subtree_check,anonuid=0,anongid=0,sec=sys,rw,secure,no_root_squash,all_squash)

#并在所有worker节点安装NFS客户端 
[root@nodeX ~]#apt update && apt -y install nfs-common 或者 nfs-client
```



**创建ServiceAccount并授权**

```yaml
[root@master1 yaml] # cat rbac.yaml 
# 创建独立的名称空间
apiVersion: v1
kind: Namespace
metadata:
  name: nfs-provisioner-demo
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: nfs-client-provisioner
  # replace with namespace where provisioner is deployed 根据业务需要修改此处名称空间
  namespace: nfs-provisioner-demo
  
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: nfs-client-provisioner-runner
rules:
  - apiGroups: [""]
    resources: ["nodes"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["persistentvolumes"]
    verbs: ["get", "list", "watch", "create", "delete"]
  - apiGroups: [""]
    resources: ["persistentvolumeclaims"]
    verbs: ["get", "list", "watch", "update"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["storageclasses"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["create", "update", "patch"]
  - apiGroups: [""]
    resources: ["services", "endpoints"]
    verbs: ["get", "list", "watch", "create", "update", "delete"]
    
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: run-nfs-client-provisioner
subjects:
  - kind: ServiceAccount
    name: nfs-client-provisioner
    # replace with namespace where provisioner is deployed
    namespace: nfs-provisioner-demo
roleRef:
  kind: ClusterRole
  name: nfs-client-provisioner-runner
  apiGroup: rbac.authorization.k8s.io
  
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: leader-locking-nfs-client-provisioner
  # replace with namespace where provisioner is deployed
  namespace: nfs-provisioner-demo
rules:
  - apiGroups: [""]
    resources: ["endpoints"]
    verbs: ["get", "list", "watch", "create", "update", "patch"]
    
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: leader-locking-nfs-client-provisioner
  # replace with namespace where provisioner is deployed
  namespace: nfs-provisioner-demo
subjects:
  - kind: ServiceAccount
    name: nfs-client-provisioner
    # replace with namespace where provisioner is deployed
    namespace: nfs-provisioner-demo
roleRef:
  kind: Role
  name: leader-locking-nfs-client-provisioner
  apiGroup: rbac.authorization.k8s.io


# 应用
[root@master1 yaml] # kubectl apply -f rbac.yaml
serviceaccount/nfs-client-provisioner created
clusterrole.rbac.authorization.k8s.io/nfs-client-provisioner-runner created
clusterrolebinding.rbac.authorization.k8s.io/run-nfs-client-provisioner created
role.rbac.authorization.k8s.io/leader-locking-nfs-client-provisioner created
rolebinding.rbac.authorization.k8s.io/leader-locking-nfs-client-provisioner created

# 查看系统用户
[root@master1 yaml]#kubectl get sa
NAME                     SECRETS   AGE
default                  0         34d
nfs-client-provisioner   0         9s
```



**部署 NFS-Subdir-External-Provisioner 对应的 Deployment**

```yaml
[root@master1 nsf-provisioner] #vim nfs-client-provisioner.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nfs-client-provisioner
  labels:
    app: nfs-client-provisioner
  namespace: nfs-provisioner-demo
spec:
  replicas: 1
  strategy:
    type: Recreate
  selector:
    matchLabels:
      app: nfs-client-provisioner
  template:
    metadata:
      labels:
        app: nfs-client-provisioner
    spec:
      serviceAccountName: nfs-client-provisioner
      containers:
      - name: nfs-client-provisioner     
        image: k8s.gcr.io/sig-storage/nfs-subdir-external-provisioner:v4.0.2 #此镜像国内可能无法访问
        imagePullPolicy: IfNotPresent
        volumeMounts:
        - name: nfs-client-root
          mountPath: /persistentvolumes
        env:
        - name: PROVISIONER_NAME
          value: k8s-sigs.io/nfs-subdir-external-provisioner # 名称确保与nfs-StorageClass.yaml文件中的provisioner名称保持一致
        - name: NFS_SERVER
          value: nfs.mystical.org
        - name: NFS_PATH
          value: /nfs-data/sc-nfs
      volumes:
      - name: nfs-client-root
        nfs:
          server: nfs.mystical.org
          path: /nfs-data/sc-nfs
          
# 应用
[root@master1 nsf-provisioner]#kubectl apply -f nfs-client-provisioner.yaml 
deployment.apps/nfs-client-provisioner created

# 查看
[root@master1 nsf-provisioner]#kubectl get pod -n nfs-provisioner-demo 
NAME                                      READY   STATUS    RESTARTS   AGE
nfs-client-provisioner-74d7c6bf46-kkpmd   1/1     Running   0          4m9s
```



**创建NFS资源的storageClass**

```yaml
[root@master1 nsf-provisioner] # vim nfs-storageClass.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: sc-nfs
  annotations:
    storageclass.kubernetes.io/is-default-class: "false" # 是否设置为默认的storageClass
provisioner:kubrovisioner # or choose another name, must match deployment's env PROVISIONER_NAME
parameters:
  archiveOnDelete: "true" # 设置为false时删除PVC不会保留数据，"true"则保留数据，基于安全原因建议设为"true"


# 应用
[root@master1 nsf-provisioner] # kubectl apply -f nfs-storageClass.yaml 
storageclass.storage.k8s.io/sc-nfs created

# 查看
[root@master1 nsf-provisioner]#kubectl get sc -n nfs-provisioner-demo 
NAME     PROVISIONER                                   RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
sc-nfs   k8s-sigs.io/nfs-subdir-external-provisioner   Delete          Immediate           false                  15s
```



**创建PVC**

```yaml
[root@master1 nsf-provisioner] # vim pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-nfs-sc
spec:
  storageClassName: sc-nfs # 需要和前面创建的storageClass名称相同
  accessModes: ["ReadWriteMany", "ReadOnlyMany"]
  resources:
    requests:
      storage: 100Mi


# 应用
[root@master1 nsf-provisioner] # kubectl apply -f pvc.yaml 
persistentvolumeclaim/pvc-nfs-sc created

# 查看pvc
[root@master1 nsf-provisioner] # kubectl get pvc
NAME         STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
pvc-nfs-sc   Bound    pvc-a77fd2d8-3f14-475c-8e81-b5c0b24c4358   100Mi      ROX,RWX        sc-nfs         <unset>                 9m46s

# 自动生成pv
[root@master1 nsf-provisioner]#kubectl get pv
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
pvc-a77fd2d8-3f14-475c-8e81-b5c0b24c4358   100Mi      ROX,RWX        Delete           Bound    default/pvc-nfs-sc   sc-nfs         <unset>                          10m


# 如果pv没有创建出来，可能的问题查看下rbac的权限，是否ServiceAccount给予的权限不够
# 可以通过logs命令查看，根据输出的日志进行排错
[root@master1 nsf-provisioner] # kubectl logs pod/nfs-client-provisioner-649b64df96-sb7sg -n nfs-provisioner-demo
```



**创建Pod**

```yaml
[root@master1 nsf-provisioner] # cat pod-test.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-nfs-sc-test
spec:
  containers:
  - name: pod-nfs-sc-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumeMounts:
    - name: nfs-pvc
      mountPath: "/usr/share/nginx/html/"
  restartPolicy: "Never"
  volumes:
  - name: nfs-pvc
    persistentVolumeClaim:
      claimName: pvc-nfs-sc

# 应用
[root@master1 nsf-provisioner] # kubectl apply -f pod-test.yaml                          
pod/pod-nfs-sc-test created

# 查看
[root@master1 nsf-provisioner] # kubectl get pod -o wide
NAME              READY   STATUS    RESTARTS   AGE   IP             NODE    NOMINATED NODE   READINESS GATES
pod-nfs-sc-test   1/1     Running   0          11s   10.244.1.125   node1   <none>           <none>

# curlIP
[root@master1 nsf-provisioner] # curl 10.244.1.125
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.20.0</center>
</body>
</html>

# 因为根目录下没有内容，因此返回403
# 在nfs目录下，添加index.html文件
[root@ubuntu2204 ~] # echo web1 > /nfs-data/sc-nfs/default-pvc-nfs-sc-pvc-a77fd2d8-3f14-475c-8e81-b5c0b24c4358/index.html

# 等一段时间后（有短时间的延迟），再次查看，
[root@master1 nsf-provisioner] # curl 10.244.1.125
web1
```







## Kubernetes配置管理



**文章内存**

- **配置说明**
- **ConfigMap**
- **Secret**
- **downwardAPI**
- **Projected**





### 配置说明

kubernetes提供了对 Pod 容器应用可以实现集中式的配置管理功能的相关资源：

- ConfigMap
- Secret
- downwardAPI
- Projected 



通过这些组件来实现向pod中的容器应用中注入配置信息的机制，从而避免了开发者参与

注意：**对于运行中容器的配置改变，还需要通过应用程序重载相关配置才能生效**





#### 配置组件简介

**configMap**

Configmap是Kubernetes集群中非常重要的一种配置管理资源对象。

借助于ConfigMap API可以向pod中的容器中注入配置信息。

ConfigMap不仅可以保存环境变量或命令行参数等属性，也可以用来保存整个配置文件或者JSON格式的 文件。

各种配置属性和数据以 k/v或嵌套k/v 样式 存在到Configmap中

注意：所有的配置信息都是**以明文的方式**来进行保存，实现资源配置的快速获取或者更新。



**Secret**

Kubernetes集群中，有一些配置属性信息是非常敏感的，所以这些信息在传递的过程中，是不希望其他人能够看到的

Kubernetes提供了一种加密场景中的配置管理资源对象Secret。

它在进行数据传输之前，会对数据进行编码，在数据获取的时候，会对数据进行解码。从而保证整个数 据传输过程的安全。

**注意：这些数据通常采用Base64机制保存，所以安全性一般**



**DownwardAPI**

downwardAPI 为运行在pod中的应用容器提供了一种反向引用。让容器中的应用程序了解所处pod或 Node的一些基础外部属性信息。

从严格意义上来说，downwardAPI不是存储卷，它自身就存在

相较于configmap、secret等资源对象需要创建后才能使用，而downwardAPI引用的是Pod自身的运行环境信息，这些信息在Pod启动的时候就存在



 **Projected**

一个 projected Volumes 投射卷可以将若干现有的卷源映射到同一个目录之上。







### ConfigMap



#### ConfigMap说明

Kubernetes提供了对pod中容器应用的集中配置管理组件：ConfigMap。

通过ConfigMap来实现向pod中的容器中注入配置信息的机制。

可以把configmap理解为Linux系统中的/etc目录，专门用来存储配置文件的目录

Kubernetes借助于ConfigMap对象实现了将配置信息从容器镜像中解耦，从而增强了工作负载的可移樟 性、使其配置更易于更改和管理并避免了将配置数据硬编码到Pod配置清单中

**ConfigMap不仅仅可以保存单个属性，也可以用来保存整个配置文件。**

从Kubernetes v1.19版本开始，ConfigMap和Secret支持使用**immutable字段**创建不可变实例，实现不 可变基础设施效果



##### 基本属性

```bash
# kubectl explain cm
    binaryData              # 二进制数据
    data                    # 文本数据，支持变量和文件
    immutable <boolean>     # 设为true，不能被修改只能删除，默认为nil可以随时被修改
    
#注意：基于data的方式传递信息的话，会在pod的容器内部生成一个单独的数据文件    
```



##### 数据配置的格式

```bash
#单行配置数据格式
属性名称key: 属性值value   #单行配置内容，一般保存变量，参数等
文件名：单行内容            #配置文件如果只有一行，也使用此方式，key为文件名，value为文件内容


#多行文件数据格式     
文件名称1: |     #注意：| 是"多行键值"的标识符
 文件内容行1    #内容大小不能超过1M
 文件内容行2
 ......
文件名称2: |     #注意：| 是"多行键值"的标识符
 文件内容行1    #内容大小不能超过1M
 文件内容行2
 ......
```

configmap资源类型的创建，与Kubernetes的其他很多资源对象的创建方式一样，主要涉及到两种方式：

- **命令行工具**：配置中有大量简单的键值对时建议使用
- **资源定义文件**：配置为大量文本内容时建议使用，此方式需要事先准备在资源清单元文件中加入配置文件内容





通常为了避免配置更新后没有生效的问题，可以在更新 ConfigMap 之后，手动重创建相关的 Pod 或者 Deployment

- 运维方式：可以通过 **重启** 或 **重建** 的方式 
  - 使用 kubectl rollout restart 命令来重启 Deployment 
  - 使用 kubectl delete pod 命令来删除 Pod，从而触发 Pod 的重启



#### ConfigMap创建和更新

##### 命令行创建方式

```bash
# 创建命令格式
kubectl create configmap NAME [--from-file=[key=]source] [--from-literal=key1=value1] [--dry-run=server|client|none] [-n <namespace>] [options]

# 参数详解：
--from-literal=key1=value1          #以设置键值对的方式实现变量配置数据
--from-env-file=/PATH/TO/FILE       #以环境变量专用文件的方式实现配置数据
--from-file=[key=]/PATH/TO/FILE     #以配置文件的方式创建配置文件数据，如不指定key，FILE名称为key名
--from-file=/PATH/TO/DIR            #以配置文件所在目录的方式创建配置文件数据

--dry-run=client -o yaml            #测试运行并显示cm内容


#查看configmap
kubectl create configmap <cm_name> -n <namespace> [-o yaml] --dry-run=client
kubectl get configmap <cm_name> -n <namespace>
kubectl describe configmap <cm_name> -n <namespace>


#删除configmap
kubectl delete configmap <cm_name> [-n <namespace>]
```



##### **命令行创建方式案例**



**范例：命令行创建基于key/value形式的变量配置**

```bash
# 在使用kubectl创建的时候，通过在命令行直接传递键值对创建
[root@master1 ~]#kubectl create configmap cm-test1 --from-literal=key1='value1' --from-literal=key2='value2'

# 查看
[root@master1 nsf-provisioner]#kubectl get cm
NAME               DATA   AGE
cm-test1           2      7s
kube-root-ca.crt   1      3d1h

# 查看yaml清单
[root@master1 nsf-provisioner]#kubectl get cm cm-test1 -o yaml
apiVersion: v1
data:
  key1: value1
  key2: value2
kind: ConfigMap
metadata:
  creationTimestamp: "2024-12-31T09:27:23Z"
  name: cm-test1
  namespace: default
  resourceVersion: "165446"
  uid: 8f831d4c-3b2d-4058-ae76-342c819f38a3

# 查看describe
[root@master1 nsf-provisioner]#kubectl describe cm cm-test1 
Name:         cm-test1
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
key1:
----
value1
key2:
----
value2

BinaryData
====

Events:  <none>

# 删除cm
[root@master1 nsf-provisioner]#kubectl delete cm cm-test1 
configmap "cm-test1" deleted
```



**范例: 命令行创建基于key/value形式的变量配置**

```bash
[root@master1 ~]# kubectl create configmap pod-test-config --from-literal=host="127.0.0.1" --from-literal=port="8888"
configmap/pod-test-config created

# 查看
[root@master1 ~]# kubectl get cm
NAME               DATA   AGE
kube-root-ca.crt   1      3d22h
pod-test-config    2      5s

# 输出清单
[root@master1 ~]# kubectl get cm pod-test-config -o yaml;
apiVersion: v1
data:
  host: 127.0.0.1
  port: "8888"
kind: ConfigMap
metadata:
  creationTimestamp: "2025-01-01T06:27:29Z"
  name: pod-test-config
  namespace: default
  resourceVersion: "197278"
  uid: 297b056b-8fa0-42e3-8394-93470a208147
```



**范例: 命令行创建基于环境变量文件的变量配置**

```bash
# 如果变量较多，使用上面方式一个个的设定环境变量太繁琐，可以全部添加到环境变量文件中然后基于它来创建CM
# 定制环境变量文件
[root@master1 conf.d]#cat env
key1=value1
key2=value2

# 注意：env文件中所有的配置项以“属性名=属性值”格式定制

# 将所有环境变量添加到configmap中
[root@master1 conf.d]# kubectl create configmap cm-test2 --from-env-file=./env 
configmap/cm-test2 created

# 查看清单文件
[root@master1 conf.d]# kubectl get cm cm-test2 -o yaml
apiVersion: v1
data:
  key1: value1
  key2: value2
kind: ConfigMap
metadata:
  creationTimestamp: "2025-01-01T06:32:42Z"
  name: cm-test2
  namespace: default
  resourceVersion: "197783"
  uid: e3a193ae-5093-4822-9c34-3b212fafc473

# 删除cm
[root@master1 conf.d]# kubectl delete cm pod-test-config 
configmap "pod-test-config" deleted
```



**范例：命令行创建基于配置文件的文件形式CM**

```bash
# 直接将多个配置文件创建为一个ConfigMap
[root@master1 ~]# ls conf.d/
app1.conf app2.conf app3.conf

[root@master1 ~]# cat conf.d/app1.conf
[app1]
config1

[root@master1 ~]# cat conf.d/app2.conf
[app2]
config2

#文件名自动成为key名
[root@master1 conf.d]#kubectl create configmap cm-test3 --from-file=./app1.conf --from-file=./app2.conf 
configmap/cm-test3 created

# 查看
[root@master1 conf.d]#kubectl get cm cm-test3 -o yaml
apiVersion: v1
data:
  app1.conf: |
    [app1]
    config1
  app2.conf: |
    [app2]
    config2
kind: ConfigMap
metadata:
  creationTimestamp: "2025-01-01T06:36:45Z"
  name: cm-test3
  namespace: default
  resourceVersion: "198174"
  uid: ee772063-dd7d-4ed5-acab-74423104695b
  
# 删除CM
[root@master1 conf.d]#kubectl delete cm cm-test3 
configmap "cm-test3" deleted
```



**范例: 命令行创建基于目录的CM**

```bash
[root@master1 conf.d]# ls
app1.conf  app2.conf  app3.conf

[root@master1 conf.d]#cat *
[app1]
config1
[app2]
config2
[app3]
config3

#直接将一个目录下的所有配置文件创建为一个ConfigMap
[root@master1 cm]#kubectl create cm cm-test4 --from-file=./conf.d/
configmap/cm-test4 created

#结果显示：多个文件之间，属性名是文件名，属性值是文件内容
[root@master1 cm]#kubectl get cm cm-test4 -o yaml;
apiVersion: v1
data:
  app1.conf: |
    [app1]
    config1
  app2.conf: |
    [app2]
    config2
  app3.conf: |
    [app3]
    config3
kind: ConfigMap
metadata:
  creationTimestamp: "2025-01-01T06:40:19Z"
  name: cm-test4
  namespace: default
  resourceVersion: "198521"
  uid: 4c83e7d6-b191-46a5-b0f4-a1c8b14f905a

# 删除CM
[root@master1 ~]#kubectl delete cm cm-test4
```



##### 资源清单文件创建方式

**资源清单文件命令格式说明**

```yaml
# 清单文件格式
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm_name
  namespace: default
data:
  key: value          # 配置信息如果只有一行，也使用此方式，使用卷挂载时，key即为文件名，value为文件内容
  文件名： |
    文件内容行1
    文件内容行2
    ......
# 注意：CM的清单文件没有spec信息，而是data

# 命令式：
kubectl create -f /path/file
# 声明式
kubectl apply -f /path/file
```

注意：此方式需要事先将配置文件的内容全部写入清单文件，而且配置文件的格式需要调整才能匹配， 所以很不方便，推荐如下方式解决

- 先在命令行执行时指定配置文件的方式创建 CM
- 通过 kubectl get cm  -o yaml > cm.yaml 方式导出资源清单文件
- 或者 kubectl create configmap NAME --dry-run=client -o yaml > cm.yaml 方式导出资源清单文件
- 最后调整和修改上面生成的 yaml资源清单文件



##### 资源清单文件创建方式案例

```yaml
# 资源定义文件
[root@master1 cm] # vim storage-configmap-test.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: config-test
data:
  author: wangxiaochun
  file.conf: |
    [class]
    linux
    go
    java
    
    
# 创建资源对象
[root@master1 cm] # kubectl apply -f storage-configmap-test.yaml 
configmap/config-test created

# 查看
[root@master1 cm] # kubectl describe cm config-test 
Name:         config-test
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
author:
----
wangxiaochun
file.conf:
----
[class]
linux
go
java


BinaryData
====

Events:  <none>

# 可以在线修改
[root@master1 cm] # kubectl edit cm config-test

# 删除
[root@master1 cm]#kubectl delete cm config-test 
configmap "config-test" deleted
```



**范例: 只读的configmap**

```yaml
[root@master1 cm] # vim storage-configmap-immutable-test.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-immutable-test
data:
  author: wangxiaochun
  file.conf: |
    [class]
    linux
    go
    java
immutable: true  # 只读

# 应用
[root@master1 cm]#kubectl apply -f storage-configmap-immutable-test.yaml 
configmap/cm-immutable-test created

# 查看
[root@master1 cm]#kubectl get cm cm-immutable-test 
NAME                DATA   AGE
cm-immutable-test   2      31s

# 在线修改configmap提示出错
[root@master1 cm]#kubectl edit cm cm-immutable-test 
error: configmaps "cm-immutable-test" is invalid

# 可以删除
[root@master1 cm]#kubectl delete cm cm-immutable-test 
configmap "cm-immutable-test" deleted
```



##### 在线更新configmap

注意：configmap虽然支持在线更新，但是configmap更新后可能不会对已有的Pod的应用生效，可能 还需要重建Pod才能生效

```bash
#创建 configmap
[root@master1 ~]#kubectl create cm cm-nginx-conf --from-file=nginx.conf

#修改configmap
#方法1,旧版中如果配置内容如果不大,多行内容可以显示在一行,但此方式不方便修改,但如果过大,此方式只
能显示大小,而非内容,所以不能修改,新版无此问题
[root@master1 ~]#kubectl edit cm cm-nginx-conf


#方法2
[root@master1 ~]#kubectl get cm cm-nginx-conf -o yaml > cm-config-conf.yaml
[root@master1 ~]#vim cm-config-conf.yaml
[root@master1 ~]#kubectl apply -f cm-config-conf.yaml


#方法3
#修改配置
[root@master1 ~]#vim nginx.conf
[root@master1 ~]#kubectl create cm cm-nginx-conf --from-file=nginx.conf --dry-run=client -oyaml |kubectl apply -f -
```



#### ConfigMap使用

**使用ConfigMap主要有两种方式：**

- 通过环境变量的方式直接传递pod
- 使用volume的方式挂载入到pod内的文件中



**注意：**

- ConfigMap必须在Pod之前创建
- 与ConfigMap在同一个namespace内的pod才能使用ConfigMap**，即ConfigMap不能跨命名空间调用。**
- ConfigMap通常存放的数据不要超过1M
- CM 可以支持实时更新，在原来的pod里面直接看到效果



#####  通过环境变量的方式直接传递 Pod

引用ConfigMap对象上特定的key，以**valueFrom**赋值给Pod上指定的环境变量

也可以在Pod上使用**envFrom**一次性导入ConfigMap对象上的所有的key-value,key(可以统一附加特定前 缀）即为环境变量,value自动成为相应的变量值

环境变量是容器启动时注入的，容器启动后变量的值不会随CM更改而发生变化,即一次性加载 configmap,除非删除容器重建



**方式1：env 对指定的变量一个一个赋值**

```bash
kubectl explain pod.spec.containers.env
    name          # 手工定制环境变量时，设置环境变量的名称，必选字段
    value         # 手工定制环境变量时，直接设置环境变量的属性值，不通过CM获取配置，可选字段
    valueFrom     # #手工定制环境变量时，设置环境变量的属性来源，可以支持从CM,Secret,downwordAPI获取

kubectl explain pod.spec.containers.env.valueFrom.configMapKeyRef
    name          # 引用指定的configmap
    key           # 引用指定的configmap中的具体哪个key
    optional      # 如果设置为false，标识该项是必选项，如果设置为true标识这个key是可选的。默认false

#此方式实现过程
1）容器中自定义环境变量名
2）根据CM的名称和Key名，找到对应的value
3) 再将value赋值给容器的环境变量
```



**方式2：envFrom 使用CM的所有变量实现对变量的批量赋值，此方式生产更为推荐**

```bash
kubectl explain pod.spec.containers.envFrom
    configMapRef     # ConfigMap对象中的所有Key
    secretKeyRef     # Secret对象中的所有Key
    prefix           # #为ConfigMap中的每个属性都添加前缀标识

#此方实现过程
1）容器中自定义环境变量名，并且和CM的key同名
2）找到指定的CM中所有Key名，将值批量直接赋值给容器中相同名称的变量
```



##### 使用volume的方式挂载入到pod内的文件中

在Pod上将 configMap对象引用为存储卷，而后整体由容器mount至某个目录下，key转为文件名， value即为相应的文件内容

在Pod上定义configMap卷时，仅引用其中的部分key，而后由容器mount至目录下

在容器上仅mount configMap卷上指定的key

容器中挂载的Volume数据可以**根据时间戳机制和ConfigMap 同步更新**，即configmap变更后会自动加载，但更新时间是不确定的，

所以一般建议当更新configmap的配置后，可以通过重新Pod使之生效，符合不可变基础设施的理念 

推荐滚动升级pod的方式来让ConfigMap内容变化生效



##### ConfigMap实战案例

**范例：env 变量**

```yaml
# 资源清单文件
[root@master1 cm] # vim storage-configmap-simple-env.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-nginx-config
data:
  port: "10086"  # 注意：只支持字符串，需要用引号引起来
  user: "www"
---
apiVersion: v1
kind: Pod
metadata:
  name: configmap-env-test
spec:
  containers:
  - name: configmap-env-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    env:
    - name: NGINX_HOST
      value: "10.0.0.100"  #直接变量赋值
    - name: NGINX_PORT
      valueFrom:
        configMapKeyRef:
          name: cm-nginx-config
          key: port
          optional: true
    - name: NGINX_USER
      valueFrom:
        configMapKeyRef:
          name: cm-nginx-config
          key: user
          optional: false
#配置解析：这里面我们可以使用两种方式在pod中传递变量

# 资源创建
[root@master1 cm] # kubectl apply -f storage-configmap-simple-env.yaml 
configmap/cm-nginx-config created
pod/configmap-env-test created

# 查看
[root@master1 cm] # kubectl get pod
NAME                 READY   STATUS    RESTARTS   AGE
configmap-env-test   1/1     Running   0          9s
[root@master1 cm] # kubectl get cm
NAME               DATA   AGE
cm-nginx-config    2      32s

# 验证变量
[root@master1 cm] # kubectl exec configmap-env-test -- env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=configmap-env-test
NGINX_HOST=10.0.0.100 
NGINX_PORT=10086   # ---------------------- ConfigMap传入变量
NGINX_USER=www     # ---------------------- ConfigMap传入变量
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
NGINX_VERSION=1.20.0
NJS_VERSION=0.5.3
PKG_RELEASE=1~buster
HOME=/root

# 资源删除
[root@master1 cm] # kubectl delete -f storage-configmap-simple-env.yaml 
configmap "cm-nginx-config" deleted
pod "configmap-env-test" deleted
```



**范例：env 变量**

```yaml
# 创建配置文件
[root@master1 cm] # vim storage-configmap-valueFrom-env.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-pod-test
  namespace: default
data:
  host: 0.0.0.0
  port: "8888"

---
apiVersion: v1
kind: Pod
metadata:
  name: configmap-env-demo
spec:
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    name: pod-test
    env:
    - name: HOST
      valueFrom:
        configMapKeyRef:
          name: cm-pod-test
          key: host
          optional: true  #true时,如果configmap中的key即使不存在,也不会导致容器无法初始

    - name: PORT
      valueFrom:
        configMapKeyRef:
          name: cm-pod-test
          key: port
          optional: false # false时，如果configmap中的key不存在，会导致容器无法初始化


# 应用
[root@master1 cm] # kubectl apply -f storage-configmap-valueFrom-env.yaml 
configmap/cm-pod-test created
pod/configmap-env-demo created

# 查看
[root@master1 cm] # kubectl exec configmap-env-demo -- env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=configmap-env-demo
HOST=0.0.0.0
PORT=8888
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
DEPLOYENV=Production
RELEASE=Stable
PS1=[\u@\h \w]\$ 
HOME=/root

# 删除资源
[root@master1 cm]#kubectl delete -f storage-configmap-valueFrom-env.yaml 
configmap "cm-pod-test" deleted
pod "configmap-env-demo" deleted
```



**范例：env 变量**

```yaml
# 清单文件
[root@master1 cm] # vim storage-configmap-simple-envargs.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-command-arg
data:
  time: "3600"
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-cm-command-arg
spec:
  containers:
  - name: pod-cm-command-arg-container
    image: busybox:1.32.0
    command: ["/bin/sh", "-c", "sleep ${SPECIAL_TIME}"]
    env:
    - name: SPECIAL_TIME
      valueFrom:
        configMapKeyRef:
          name: cm-command-arg
          key: time
    - name: NAME
      value: "wangxiaochun"
  restartPolicy: Never

# 应用
[root@master1 cm] # kubectl apply -f storage-configmap-simple-envargs.yaml 
configmap/cm-command-arg created
pod/pod-cm-command-arg created

# 查看
[root@master1 cm] # kubectl get pod
NAME                 READY   STATUS    RESTARTS   AGE
pod-cm-command-arg   1/1     Running   0          3s

[root@master1 cm] # kubectl exec pod-cm-command-arg -- ps aux
PID   USER     TIME  COMMAND
    1 root      0:00 sleep 3600
    8 root      0:00 ps aux

# 删除
[root@master1 cm]#kubectl delete -f storage-configmap-simple-envargs.yaml 
configmap "cm-command-arg" deleted
pod "pod-cm-command-arg" deleted
```



**范例：envFrom 批量导入所有变量**

```yaml
# 配置文件资源定义文件
[root@master1 cm] # vim storage-configmap-simple-envfrom.yaml
[root@master1 cm]#cat storage-configmap-simple-envfrom.yaml 
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-nginx
data:
  NGINX_PORT: "10086"
  NGINX_USER: "www"
---
apiVersion: v1
kind: Pod
metadata:
  name: configmap-envfrom-test
spec:
  containers:
  - name: configmap-envfrom-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    envFrom:
    - configMapRef:
        name: cm-nginx  # 所有变量从cm中读取
        
# 应用
[root@master1 cm] # kubectl apply -f storage-configmap-simple-envfrom.yaml 
configmap/cm-nginx unchanged
pod/configmap-envfrom-test created

# 查看
[root@master1 cm] # kubectl get pod
NAME                     READY   STATUS    RESTARTS   AGE
configmap-envfrom-test   1/1     Running   0          2s

[root@master1 cm] # kubectl exec configmap-envfrom-test -- env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=configmap-envfrom-test
NGINX_PORT=10086
NGINX_USER=www
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_PORT=443
NGINX_VERSION=1.20.0
NJS_VERSION=0.5.3
PKG_RELEASE=1~buster
HOME=/root

# 删除
[root@master1 cm]#kubectl delete -f storage-configmap-simple-envfrom.yaml 
configmap "cm-nginx" deleted
pod "configmap-envfrom-test" deleted
```



 **范例：volume 生成配置文件并更新生效**

```yaml
# configmap资源定义
[root@master1 cm] # vim storage-configmap-simple-volume.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-volume
data:
  author: wangxiaochun
  file.conf: |
    [app]
    config1
    config2

---
apiVersion: v1
kind: Pod
metadata:
  name: pod-volume-test
spec:
  volumes:
  - name: volume-config  # 指定卷名
    configMap:
      name: cm-volume    # 指定卷来自cm
  containers:
  - name: nginx
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumeMounts:
    - name: volume-config # 调用前面定义的卷名
      mountPath: /cmap/   # 指定Pod中的挂载点目录
      
# 应用
[root@master1 cm] # kubectl apply -f storage-configmap-simple-volume.yaml 
configmap/cm-volume created
pod/pod-volume-test created

# 查看
[root@master1 cm] # kubectl get pod
NAME              READY   STATUS    RESTARTS   AGE
pod-volume-test   1/1     Running   0          4s

[root@master1 cm] # kubectl exec pod-volume-test -- ls /cmap/
author
file.conf

# 进入容器查看
[root@master1 cm] # kubectl exec -it pod-volume-test -- sh
# cd /cmap     
# ls
author	file.conf
# ls -al
total 12
drwxrwxrwx 3 root root 4096 Jan  1 09:26 .
drwxr-xr-x 1 root root 4096 Jan  1 09:26 ..
drwxr-xr-x 2 root root 4096 Jan  1 09:26 ..2025_01_01_09_26_31.673800736
lrwxrwxrwx 1 root root   31 Jan  1 09:26 ..data -> ..2025_01_01_09_26_31.673800736
lrwxrwxrwx 1 root root   13 Jan  1 09:26 author -> ..data/author
lrwxrwxrwx 1 root root   16 Jan  1 09:26 file.conf -> ..data/file.conf
# cd ..2025*        
# ls
author	file.conf

# 结果显示：
# 这些文件虽然看起来是挂载在目录下，实际上，它是经过两层的软链接才能找到真正的挂载的文件，容器内挂载目录的生成的文件
# ..2025_01_01_09_26_31.673800736
# ..data -> ..2025_01_01_09_26_31.673800736
# author -> ..data/author
# file.conf -> ..data/file.conf
# 通过这种双层软连接的方式，只要容器支持重载技术，那么只需要更改配置文件就可以实现容器应用的变动

# 修改cm
[root@master1 cm] # kubectl edit cm cm-volume 
apiVersion: v1
data:
 author: wang  #修改此行
 file.conf: |
   [app]
   config1
   config2
   config3  #加此行
kind: ConfigMap
.....
configmap/cm-volume edited

# 等一会儿进入pod可以看到配置文件变化
[root@master1 cm] # kubectl exec -it pod-volume-test -- sh
# cd /cmap
# ls -al
total 12
drwxrwxrwx 3 root root 4096 Jan  1 09:33 .
drwxr-xr-x 1 root root 4096 Jan  1 09:26 ..
drwxr-xr-x 2 root root 4096 Jan  1 09:33 ..2025_01_01_09_33_42.2079151602
lrwxrwxrwx 1 root root   32 Jan  1 09:33 ..data -> ..2025_01_01_09_33_42.2079151602
lrwxrwxrwx 1 root root   13 Jan  1 09:26 author -> ..data/author
lrwxrwxrwx 1 root root   16 Jan  1 09:26 file.conf -> ..data/file.conf
# cat file.conf                     
[app]
config1
config2
config3
# exit

#删除
[root@master1 cm] # kubectl delete -f storage-configmap-simple-volume.yaml 
configmap "cm-volume" deleted
pod "pod-volume-test" deleted
```



**范例：volume 挂载全部内容**

```yaml
# 命令行创建CM，创建Nginx的配置信息
[root@master1 nginx.conf.d] # vim default.conf
server {
    listen 8080;
    server_name localhost;
    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
    }
    error_page 500 502 503 504 /50x.html;
    location /50x.html {
        root /usr/share/nginx/html;
    }
}

# 命令行创建CM
[root@master1 cm] # kubectl create configmap cm-nginx-conf-files --from-file=nginx.conf.d/
configmap/cm-nginx-conf-files created

# 查看
[root@master1 cm]#kubectl get cm
NAME                  DATA   AGE
cm-nginx-conf-files   1      87s

# 清单文件
[root@master1 cm] # vim storage-configmap-nginx-file.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-nginx-index
data:
  index.html: "Nginx Configmap Page!" # 单行内容生成configmap
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-nginx-conf-configmap
spec:
  volumes:
  - name: nginx-conf
    configMap:
      name: cm-nginx-conf-files
      optional: false
  - name: nginx-index
    configMap:
      name: cm-nginx-index
      optional: false
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: nginx
    volumeMounts:
    - name: nginx-conf
      mountPath: /etc/nginx/conf.d/
      readOnly: true
    - name: nginx-index
      mountPath: /usr/share/nginx/html/
      readOnly: true
      
      
# 应用
[root@master1 cm] # kubectl apply -f storage-configmap-nginx-file.yaml 
configmap/cm-nginx-index created
pod/pod-nginx-conf-configmap created

# 查看
[root@master1 cm] # kubectl get cm
NAME                  DATA   AGE
cm-nginx-conf-files   1      7m31s
cm-nginx-index        1      55s

# 测试效果
[root@master1 cm] # kubectl get pod -o wide
NAME                       READY   STATUS    RESTARTS   AGE   IP             NODE    NOMINATED NODE   READINESS GATES
pod-nginx-conf-configmap   1/1     Running   0          77s   10.244.3.138   node3   <none>           <none>

[root@master1 cm] # curl 10.244.3.138
curl: (7) Failed to connect to 10.244.3.138 port 80 after 0 ms: 拒绝连接

# 读取了configmap传入的配置文件
[root@master1 cm] # curl 10.244.3.138:8080
Nginx Configmap Page!

# 删除
[root@master1 cm] # kubectl delete -f storage-configmap-nginx-file.yaml 
configmap "cm-nginx-index" deleted
pod "pod-nginx-conf-configmap" deleted

[root@master1 cm] # kubectl delete cm cm-nginx-conf-files 
configmap "cm-nginx-conf-files" deleted
```



**范例：volume 挂载 CM 中部分文件**

```yaml
# 准备配置文件
[root@master1 nginx.conf.d] #ls
default.conf  myserver.conf  myserver-gzip.cfg  myserver-status.cfg

# 配置文件
[root@master1 cm] #cat nginx.conf.d/myserver.conf 
server {
    listen 8888;
    server_name www.wang.org;
    include /etc/nginx/conf.d/myserver-*.cfg
    location / {
        root /usr/share/nginx/html;
    }
}

# 子配置文件,注意:文件是以cfg为后缀,不能以conf文件后缀,会导致冲突
[root@master1 cm] # cat nginx.conf.d/myserver-gzip.cfg 
gzip on;
gzip_comp_level 5;
gzip_proxied     expired no-cache no-store private auth;
gzip_types text/plain text/css application/xml text/javascript;

[root@master1 cm] # cat nginx.conf.d/myserver-status.cfg 
location /nginx-status {
   stub_status on;
   access_log off;
}

# 创建cm
[root@master1 cm] # kubectl create cm cm-nginx-conf-files --from-file=nginx.conf.d/
configmap/cm-nginx-conf-files created

# 清单文件
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-nginx-index
data:
  index.html: "Nginx Sub Configmap Page\n"
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-cm-nginx-conf
spec:
  volumes:
  - name: nginx-conf
    configMap:
      name: cm-nginx-conf-files
      items:                            # 指定cm中的key
      - key: myserver.conf              # cm中的key名称
        path: myserver.conf             # Pod中的文件名
        mode: 0644                      # Pod中的文件权限
      - key: myserver-status.cfg
        path: myserver-status.cfg
        mode: 0644
      - key: myserver-gzip.cfg
        path: myserver-gzip.cfg
        mode: 0644
      optional: false
  - name: nginx-index
    configMap:
      name: cm-nginx-index
      optional: false
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: pod-cm-nginx-conf-container
    volumeMounts:
    - name: nginx-conf
      mountPath: /etc/nginx/conf.d/
      readOnly: true
    - name: nginx-index
      mountPath: /usr/share/nginx/html/
      readOnly: true

# 应用
[root@master1 cm] # kubectl apply -f storage-configmap-nginx-subfile.yaml 
configmap/cm-nginx-index created
pod/pod-cm-nginx-conf created

# 查看
[root@master1 cm]#kubectl exec pod-cm-nginx-conf -- ls /etc/nginx/conf.d
myserver-gzip.cfg
myserver-status.cfg
myserver.conf

# 查看资源
[root@master1 cm]#kubectl get cm cm-nginx-conf-files -o yaml
apiVersion: v1
data:
  default.conf: |
    server {
        listen 8080;
        server_name localhost;
        location / {
            root /usr/share/nginx/html;
            index index.html index.htm;
        }
        error_page 500 502 503 504 /50x.html;
        location /50x.html {
            root /usr/share/nginx/html;
        }
    }
  myserver-gzip.cfg: |
    gzip on;
    gzip_comp_level 5;
    gzip_proxied     expired no-cache no-store private auth;
    gzip_types text/plain text/css application/xml text/javascript;
  myserver-status.cfg: |+
    location /nginx-status {
       stub_status on;
       access_log off;
    }

  myserver.conf: |
    server {
        listen 8888;
        server_name www.wang.org;
        include /etc/nginx/conf.d/myserver-*.cfg;
        location / {
            root /usr/share/nginx/html;
        }
    }
kind: ConfigMap
metadata:
  creationTimestamp: "2025-01-01T10:54:52Z"
  name: cm-nginx-conf-files
  namespace: default
  resourceVersion: "224964"
  uid: 80862286-fb45-4dc2-ba8a-4d886f88e015
  
# 查看效果
[root@master1 cm] # curl 10.244.3.140:8888
Nginx Sub Configmap Page

# 删除资源
#删除资源
[root@master1 yaml] #kubectl delete -f storage-configmap-nginx-subfile.yaml
[root@master1 yaml] #kubectl delete cm cm-nginx-conf-files
```



**范例：volume 基于subpath实现挂载CM部分文件并修改配置文件名称**

```yaml
kubectl explain pod.spec.volumes.configMap.items

FIELDS:
   key <string> -required-
     key is the key to project.
     
   mode <integer>
     mode is Optional: mode bits used to set permissions on this file. Must be
     an octal value between 0000 and 0777 or a decimal value between 0 and 511.
     YAML accepts both octal and decimal values, JSON requires decimal values
     for mode bits. If not specified, the volume defaultMode will be used. This
     might be in conflict with other options that affect the file mode, like
     fsGroup, and the result can be other mode bits set.
     
   path <string> -required-
     path is the relative path of the file to map the key to. May not be an
     absolute path. May not contain the path element '..'. May not start with
     the string '..'.
     
kubectl explain pod.spec.containers.volumeMounts
FIELDS:
   mountPath <string> -required-
     Path within the container at which the volume should be mounted. Must not
     contain ':'.
     
   mountPropagation <string>
     mountPropagation determines how mounts are propagated from the host to
     container and the other way around. When not set, MountPropagationNone is
     used. This field is beta in 1.10.
     
   name <string> -required-
     This must match the Name of a Volume.
     
   readOnly <boolean>
     Mounted read-only if true, read-write otherwise (false or unspecified).
     Defaults to false.
     
   subPath <string>
     Path within the volume from which the container's volume should be mounted.
     Defaults to "" (volume's root).

   subPathExpr <string>
     Expanded path within the volume from which the container's volume should be
     mounted. Behaves similarly to SubPath but environment variable references
     $(VAR_NAME) are expanded using the container's environment. Defaults to ""
     (volume's root). SubPathExpr and SubPath are mutually exclusive
```

**范例**

```yaml
# 准备配置文件同上一样
[root@master1 cm] #ls nginx.conf.d/
default.conf  myserver.conf  myserver-gzip.cfg  myserver-status.cfg

# 将上面的配置文件都加入cm
[root@master1 cm] # kubectl create cm cm-nginx-conf-files --from-file=nginx.conf.d/
configmap/cm-nginx-conf-files created

# 清单文件
[root@master1 cm] # vim storage-configmap-nginx-usesubfile.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-nginx-index
data:
  index.html: "Nginx Use Sub Configmap Page\n"
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-cm-nginx-conf
spec:
  volumes:
  - name: nginx-conf
    configMap:
      name: cm-nginx-conf-files
      optional: false
  - name: nginx-index
    configMap:
      name: cm-nginx-index
      optional: false
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: pod-cm-nginx-conf-container
    volumeMounts:
    - name: nginx-conf
      mountPath: /etc/nginx/conf.d/myserver2.conf   # 修改生成的配置文件名
      subPath: myserver.conf                        # 指定nginx-conf中的特定文件，而非所有文件
      readOnly: true
    - name: nginx-conf
      mountPath: /etc/nginx/conf.d/myserver-gzip2.cfg   # 修改生成的配置文件名
      subPath: myserver-gzip.cfg                        # 指定nginx-conf中的特定文件，而非所有文件
      readOnly: true
    - name: nginx-index
      mountPath: /usr/share/nginx/html/
      readOnly: true


[root@master1 cm] # kubectl apply -f storage-configmap-nginx-usesubfile.yaml 
configmap/cm-nginx-index created
pod/pod-cm-nginx-conf created

[root@master1 cm] # kubectl get pod
NAME                READY   STATUS    RESTARTS   AGE
pod-cm-nginx-conf   1/1     Running   0          2s

[root@master1 cm] # kubectl get pod -o wide
NAME                READY   STATUS    RESTARTS   AGE   IP             NODE    NOMINATED NODE   READINESS GATES
pod-cm-nginx-conf   1/1     Running   0          15s   10.244.3.142   node3   <none>           <none>

[root@master1 cm] # kubectl exec pod-cm-nginx-conf -- ls /etc/nginx/conf.d
default.conf
myserver-gzip2.cfg
myserver2.conf

# 删除

```



**范例：volume 基于subPath 挂载CM 部分文件并保留原目录中的其它文件**

```yaml
# 查看容器内的文件列表
[root@master1 cm] # docker run --rm --name nginx wangxiaochun/nginx:1.20.0 ls /etc/nginx/
conf.d
fastcgi_params
mime.types
modules
nginx.conf
scgi_params
uwsgi_params

# 导出配置文件
[root@master1 cm] # docker run --rm --name nginx wangxiaochun/nginx:1.20.0 cat /etc/nginx/nginx.conf > nginx.conf

# 创建configmap
[root@master1 cm] # kubectl create cm cm-nginx-conf --from-file=nginx.conf
configmap/cm-nginx-conf created

# 查看配置内容
[root@master1 cm] # kubectl describe cm cm-nginx-conf 
Name:         cm-nginx-conf
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
nginx.conf:
----

user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}


BinaryData
====

Events:  <none>


# 准备配置文件
[root@master1 cm] # vim storage-configmap-subPath-nginx-1.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-cn-nginx-conf
spec:
  volumes:
  - name: volume-nginx-conf
    configMap:
      name: cm-nginx-conf
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: pod-cm-nginx-conf-container
    command: ["sh", "-c", "sleep 3600"]
    volumeMounts:
    - name: volume-nginx-conf
      mountPath: /etc/nginx/

# 应用
[root@master1 cm] # kubectl apply -f storage-configmap-subPath-nginx-1.yaml 
pod/pod-cn-nginx-conf created

# 查看
[root@master1 cm] # kubectl get pod
NAME                READY   STATUS    RESTARTS   AGE
pod-cn-nginx-conf   1/1     Running   0          3s

# 直接将整个目录覆盖了
[root@master1 cm] # kubectl exec pod-cn-nginx-conf -- ls /etc/nginx
nginx.conf

# 删除
[root@master1 cm] # kubectl delete -f storage-configmap-subPath-nginx-1.yaml 
pod "pod-cn-nginx-conf" deleted

# 修改清单文件
[root@master1 cm] # cat storage-configmap-subPath-nginx-2.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-cm-nginx-conf
spec:
  volumes:
  - name: volume-nginx-conf
    configMap:
      name: cm-nginx-conf
      items:
      - key: nginx.conf
        path: etc/nginx/nginx.conf       # 必须是相对路径，且和下面subPath路径相同
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: pod-cm-nginx-conf-container
    command: ["sh", "-c", "sleep 3600"]
    volumeMounts:
    - name: volume-nginx-conf
      mountPath: /etc/nginx/nginx.conf
      subPath: etc/nginx/nginx.conf     # 必须是相对路径，且和volumes的path路径相同
      
[root@master1 cm] # kubectl apply -f storage-configmap-subPath-nginx-2.yaml 
pod/pod-cm-nginx-conf created

[root@master1 cm] # kubectl get pod
NAME                READY   STATUS    RESTARTS   AGE
pod-cm-nginx-conf   1/1     Running   0          3s

[root@master1 cm] # kubectl exec -it pod-cm-nginx-conf -- ls /etc/nginx/
conf.d		mime.types  nginx.conf	 uwsgi_params
fastcgi_params	modules     scgi_params
```



**关于上面案例中，volumes.configMap.items.path相对路径补充说明：**

在 `ConfigMap` 中，`path` 是用来指定该键值对在 **`volume` 根目录下的相对路径**。

- **必须是相对路径的原因**： Kubernetes 的设计中，`ConfigMap` 的 `items` 是将键值对映射为文件，并存储到 `volume` 的临时文件目录中。这个目录是动态创建的，无法提前确定一个具体的绝对路径。因此，`path` 是相对于 **`volume` 的根目录** 的相对路径



**详细解释：它相对于谁的路径？**

**卷（`volume`）的根目录**：

- `ConfigMap` 数据被挂载到容器之前，Kubernetes 会将数据放在一个临时目录中，比如：

  ```js
  /var/lib/kubelet/pods/<pod-id>/volumes/kubernetes.io~configmap/<volume-name>/
  ```

- 在 `path` 中指定的路径是 **相对于这个临时目录** 的相对路径。

- 假设 `ConfigMap` 中有一条定义：

  ```yaml
  items:
    - key: nginx.conf
      path: etc/nginx/nginx.conf
  ```

- Kubernetes 会将键`nginx.conf`的值写入文件：

  ```js
  /var/lib/kubelet/pods/<pod-id>/volumes/kubernetes.io~configmap/<volume-name>/etc/nginx/nginx.conf
  ```

**挂载点的层次化设计:**

- `path` 是相对于 `volume` 内容的根路径，而不是容器内的 `mountPath`。
- 如果允许 `path` 是绝对路径（如 `/etc/nginx/nginx.conf`），则 Kubernetes 无法将它挂载到 `volume` 的临时目录中，因为这样会和文件系统结构冲突。



**`mountPath` 和 `subPath` 的关系**

- **`mountPath`**：是容器中挂载点的绝对路径，表示挂载点在容器文件系统中的位置。
- **`subPath`**：表示挂载点内部（`volume` 内部）的相对路径，它从 `volumes` 指定的资源（如 `ConfigMap` 或 `PersistentVolume`）的根目录开始。



**挂载路径的逻辑**

- `mountPath` 定义了容器中的文件/目录挂载位置，比如 `/etc/nginx/nginx.conf`。
- `subPath` 定义了在卷中选择具体的文件或路径，比如 `etc/nginx/nginx.conf`。
- **`subPath` 是相对于 `volumes` 挂载内容的路径，而不是 `mountPath` 的路径。**





### Secret



#### Secret介绍

![image-20250101212836061](D:\git_repository\cyber_security_learning\markdown_img\image-20250101212836061.png)

Secret 和 Configmap 相似，也可以提供配置数据，但主要用于为Pod提供敏感需要加密的信息

Secret 主要用于存储密码、证书私钥，SSH 密钥，OAuth令牌等敏感信息，这些敏感信息采用base64编 码保存，相对明文存储更安全

相比于直接将敏感数据配置在Pod的定义或者镜像中，Secret提供了更加安全的机制，将需要共享的数 据进行加密，防止数据泄露。

Secret的对象需要单独定义并创建，通常以数据卷的形式挂载到Pod中，Secret的数据将以文件的形式 保存，容器通过读取文件可以获取需要的数据

Secret volume是通过tmpfs（内存文件系统）实现的，所以**这种类型的volume不是永久存储的。**

**每个Secret的数据不能超过1MB**，支持通过资源限额控制每个名称空间的Secret的数量

**注意: Secret 属于名称空间级别，只能被同一个名称空间的Pod引用**



**Secret 分成以下常见大的分类**

| 类型            | 解析                                                         |
| --------------- | ------------------------------------------------------------ |
| generic         | 通用类型，基于**base64编码**用来存储密码，公钥等。<br />常见的子类型有： Opaque,kubernetes.io/service-account-token,kubernetes.io/basicauth,kubernetes.io/ssh-auth,bootstrap.kubernetes.io/token,kubernetes.io/rbd |
| tls             | 专门用于保存tls/ssl用到证书和配对的私钥,常见的子类型:kubernetes.io/tls |
| docker-registry | 专用于让kubelet启动Pod时从私有镜像仓库pull镜像时，首先认证到仓库Registry时使用 <br />常见的子类型:kubernetes.io/dockercfg,kubernetes.io/dockerconfigjson |



**Secret 细化为的子类型(Type)**

| 大类型          | Builtin Type                       | 说明                                        |
| --------------- | ---------------------------------- | ------------------------------------------- |
| generic         | opaque                             | arbitrary user-defined data                 |
| generic         | kubernetes.io/service-accounttoken | service account token                       |
| generic         | kubernetes.io/basic-auth           | credentials for basic authentication        |
| generic         | kubernetes.io/ssh-auth             | credentials for SSH authentication          |
| generic         | bootstrap.kubernetes.io/token      | bootstrap token data 初始化                 |
| tls             | kubernetes.io/tls                  | data for a TLS client or server             |
| docker-registry | kubernetes.io/dockerconfigjson     | serialized ~/ .docker/config.json file 新版 |
| docker-registry | kubernetes.io/dockercfg            | serialized -/ .dockercfg file 旧版          |



**注意：**

不同类型的Secret，在定义时支持使用的标准字段也有所不同

例如: ssh-auth类型的Secret应该使用ssh-privatekey，而basic-auth类型的Secret则需要使用 username和password等

另外也可能存在一些特殊的类型, 用于支撑第三方需求，例如: ceph的keyring信息使用的 kubernetes.io/rbd等



**Secret 创建方式**

- **手动创建**：用户自行创建的Secret 常用来存储用户私有的一些信息
- **自动创建**：集群自动创建的Secret 用来作为集群中各个组件之间通信的身份校验使用



**查看Secret**

```bash
[root@master1 cm]# kubectl get secrets -A
NAMESPACE     NAME                     TYPE                            DATA   AGE
kube-system   bootstrap-token-8loc6r   bootstrap.kubernetes.io/token   6      4d6h

[root@master1 cm]# kubectl get secrets -n kube-system  bootstrap-token-8loc6r -o yaml
apiVersion: v1
data:
  auth-extra-groups: c3lzdGVtOmJvb3RzdHJhcHBlcnM6a3ViZWFkbTpkZWZhdWx0LW5vZGUtdG9rZW4=
  description: VGhlIGRlZmF1bHQgYm9vdHN0cmFwIHRva2VuIGdlbmVyYXRlZCBieSAna3ViZWFkbSBpbml0Jy4=
  token-id: OGxvYzZy
  token-secret: cjFybWE3dzQ4eG1kdmJudA==
  usage-bootstrap-authentication: dHJ1ZQ==
  usage-bootstrap-signing: dHJ1ZQ==
kind: Secret
metadata:
  creationTimestamp: "2024-12-28T07:55:15Z"
  name: bootstrap-token-8loc6r
  namespace: kube-system
  resourceVersion: "215"
  uid: b50e2dd9-50e8-4f60-879f-89086ff35b2f
type: bootstrap.kubernetes.io/token

# basey64解码查看description具体数据
[root@master1 cm]#echo -n "VGhlIGRlZmF1bHQgYm9vdHN0cmFwIHRva2VuIGdlbmVyYXRlZCBieSAna3ViZWFkbSBpbml0Jy4="|base64 -d
The default bootstrap token generated by 'kubeadm init'.
```



#### Secret命令式创建



![image-20250101223713630](D:\git_repository\cyber_security_learning\markdown_img\image-20250101223713630.png)



**格式**

```bash
 kubectl create secret [flags] [options] [-n <namespace>]
```



**命令格式**

```bash
# generic类型
kubectl create secret generic NAME [--type=string] [--from-file=[key=]source] [--from-literal=key1=value1]

--from-literal=key1=value1       #以命令行设置键值对的环境变量方式配置数据
--from-env-file=/PATH/FILE       #以环境变量的专用文件的方式配置数据
--from-file=[key=]/PATH/FILE     #以配置文件的方式创建配置数据，如不指定key，FILE名称为key名
--from-file=/PATH/DIR            #以配置文件所在目录的方式创建配置数据

#该命令中的--type选项进行定义除了后面docker-registry和tls命令之外的其它子类型，有些类型有key的特定要求
#注意: 如果vaule中有特殊字符,比如:$,\,*,=,!等,需要用\进行转义或用单引号''引起来

#tls类型
kubectl create secret tls NAME --cert=/path/file --key=/path/file
#其保存cert文件内容的key名称不能指定自动为tls.crt，而保存private key的key不能指定自动tls.key

#docker-registry类型
#方式1:基于用户名和密码方式实现
kubectl create secret docker-registry NAME --docker-username=user --docker-password=password --docker-email=email [--docker-server=string] [--from-file=[key=]source]

#方式2:基于dockerconfig文件方式实现
kubectl create secret docker-registry KEYNAME --fromfile=.dockerconfigjson=path/to/.docker/config.json
#从已有的json格式的文件加载生成的就是dockerconfigjson类型，命令行直接生成的也是该类型
```



**范例**

```bash
# 创建generic类型
kubectl create secret generic my-secret-generic --from-file=/path/bar

kubectl create secret generic my-secret-generic --from-file=ssh-privatekey=~/.ssh/id_rsa --from-file=ssh-publickey=~/.ssh/id_rsa.pub

kubectl create secret generic my-secret-generic --from-literal=username=admin --from-literal=password=123456

kubectl create secret generic my-secret-generic --from-env-file=path/to/bar.env


# 创建tls类型
kubectl create secret tls my-secret-tls --cert=certs/wang.org.cert --key=certs/wang.org.key

#创建docker-registry类型
#参考示例：https://Kubernetesmeetup.github.io/docs/tasks/configure-podcontainer/pull-image-private-registry/
#基于私有仓库的用户名和密码
kubectl create secret docker-registry my-secret-docker-registry --docker-server=harbor.wang.org --docker-username=admin --docker-password=123456 --docker-email=29308620@qq.com

#先登录并认证到目标仓库server上，认证凭据自动保存在dockercfg文件中,基于dockerconfig文件实现
kubectl create secret docker-registry dockerharbor-auth --from-file=.dockerconfigjson=/root/.docker/config.json

kubectl create secret generic dockerharbor-auth --
type='kubernetes.io/dockerconfigjson' --from-file=.dockerconfigjson=/root/.docker/config.json
```





# 知识扩展



## Watch机制



**watch 本质上就是一个基于 HTTPS 的长连接请求**。在这个长连接中，**API Server 会向客户端主动推送资源变更事件**，但要注意的是，**客户端在发起 watch 请求后不会反复发送请求，后续的所有数据都是由 API Server 主动推送的**。



### HTTP/2实现

#### **1. 技术核心：HTTP/2 的特性**

Kubernetes 的 watch 机制依赖于**HTTP/2 协议**的**多路复用和流式数据传输**。和传统的 HTTP/1.1 不同，**HTTP/2 提供了持久的双向数据流**，这是实现“**一次请求，多次响应**”的核心。



##### **HTTP/2 的关键特性**

| **特性**            | **描述**                                   | **在 watch 中的作用**                                  |
| ------------------- | ------------------------------------------ | ------------------------------------------------------ |
| **多路复用**        | 单个 TCP 连接中允许多个流的并行交付        | 允许 kubelet 和 apiserver 通过单连接传输多个请求和响应 |
| **数据流 (Stream)** | 数据以流的形式发送，流 ID 用于标识数据段   | kube-apiserver 不断向 kubelet 发送流数据               |
| **流式响应**        | 不必等待请求完成，可以多次传输分段响应数据 | 在 watch 中，每次 Pod 变化都会立刻推送到客户端         |
| **长连接**          | 连接不关闭，维持客户端与服务端的长连接     | 客户端的 watch 请求一直保持连接，直到中断              |
| **头部压缩**        | HTTP 头的 HPACK 压缩，减少网络流量消耗     | kube-apiserver 的请求和响应的头部变小，减少延迟        |



##### **HTTP/2 是如何实现“请求-多次响应”的？**

1. **多路复用**：
   - 在 HTTP/2 中，客户端与服务端之间只建立一个 TCP 连接，但可以在该连接上同时处理多个 HTTP 请求。
   - watch 请求（`GET /api/v1/pods?watch=true`）**只占用一个 HTTP 流**，即使有其他请求（例如 List Pods）也不会影响 watch 流。
2. **数据流 (Stream)**：
   - HTTP/2 使用“**数据流**”的概念。
   - 当 kube-apiserver 监测到 Pod 变化时，**将变化的事件打包为一条消息**，推送到与客户端的流中。
   - **客户端监听到事件后可以立刻接收并处理，而不需要关闭或重新请求。**
3. **流式响应**：
   - 在 HTTP/1.1 中，响应数据必须等待请求完成后，才能完整返回。
   - 在 HTTP/2 中，服务端可以**一段一段地将数据发送回客户端**，这正是 Kubernetes 中 watch 机制的关键。
   - **每次 Pod 状态变化时，API Server 会将事件推送到客户端，客户端立即收到变化数据。**



#### **2. 在 Kubernetes 中的实现**

##### **Watch 请求**

``` 
GET /api/v1/pods?watch=true&resourceVersion=123456 HTTP/2
Host: kube-apiserver:6443
```

- **GET** 请求，路径是 `/api/v1/pods`，带有参数 `watch=true`。
- `resourceVersion=123456`：这表示客户端希望**从版本 123456 之后的事件开始监听**。
- 这是一个 HTTP/2 请求，它**不关闭连接**，相当于在 TCP 上创建一个**长连接**，并保持数据流。



##### **响应数据**

API Server 检测到 Pod 变化后，会不断地**流式传输**变更事件。

```json
jsonCopy code{
  "type": "ADDED",
  "object": {
    "metadata": {
      "name": "nginx-pod",
      "namespace": "default",
      "resourceVersion": "123457"
    },
    "status": {
      "phase": "Running"
    }
  }
}
{
  "type": "MODIFIED",
  "object": {
    "metadata": {
      "name": "nginx-pod",
      "namespace": "default",
      "resourceVersion": "123458"
    },
    "status": {
      "phase": "Terminating"
    }
  }
}
{
  "type": "DELETED",
  "object": {
    "metadata": {
      "name": "nginx-pod",
      "namespace": "default",
      "resourceVersion": "123459"
    }
  }
}
```

- 这些事件是**分段返回的 JSON 消息**。
- 每条事件都有一个**事件类型 (type)**，可以是 `ADDED`, `MODIFIED`, `DELETED`。
- **流式数据传输**：每个事件都是独立的 JSON 块，kubelet 立刻能读取这些数据，而不需要等待所有数据返回。
- **不关闭连接**：API Server **只会在连接断开时关闭流**，否则会持续发送数据。



#### **3. 这与 WebSocket 的对比**

| **特性**     | **HTTP/2**               | **WebSocket**              |
| ------------ | ------------------------ | -------------------------- |
| **连接类型** | HTTP/2 长连接，流式响应  | TCP 长连接，类似双工通信   |
| **协议层**   | TCP + HTTP/2             | TCP + WebSocket (ws://)    |
| **多路复用** | 支持                     | 不支持（一个请求一个通道） |
| **并发性**   | 高并发，多请求一个 TCP   | 需要多个 TCP 连接          |
| **数据传输** | 以**数据流**传输分段数据 | 以数据包/消息方式传输      |
| **使用场景** | Kubernetes watch、API流  | 聊天室、游戏等双工通信     |
| **网络效率** | 较高，资源利用率高       | 较高，适合双工通信         |



#### **4. 关键的网络协议特性**

| **网络协议/特性** | **HTTP/2** | **描述**                             |
| ----------------- | ---------- | ------------------------------------ |
| **TCP**           | 需要       | HTTP/2 是基于 TCP 传输的（TLS/SSL）  |
| **TLS/SSL**       | 必须       | 传输时使用 TLS 加密，增强数据安全    |
| **多路复用**      | 支持       | 单个 TCP 连接可传输多个 HTTP 请求    |
| **流控制**        | 支持       | 控制每个流的流量，避免某个流占满带宽 |
| **分段传输**      | 支持       | 不必等待所有数据，流式传输响应片段   |
| **头部压缩**      | 支持       | 使用 HPACK 压缩头部，减少带宽        |



#### **5. 关键问题解答**

1. **“一次请求，多次响应” 是怎么实现的？**

- 使用**HTTP/2 中的流式响应**。
- 通过在 HTTP/2 中维持一个**长连接**，服务端 API Server 会不断地将事件推送给客户端。
- 这些事件是一个个**分段的 JSON 数据块**，流式返回给客户端。
- **客户端只需要发起一次请求**，API Server 会主动推送资源的变化数据。



2. **watch 机制与传统的“轮询 (polling)” 有何不同？**

- **传统轮询**：客户端定期发送请求，获取全量资源列表，开销大，延迟高。
- **watch 机制**：客户端只发送一次请求，API Server 持续推送变更，实时性强，资源开销小。



3. **如果连接断开了怎么办？**

- 客户端会检测到断开，并自动重新发起 watch 请求。
- 如何避免丢失数据？
  - 客户端会使用最后的 `resourceVersion` 来恢复。
  - 如果 `resourceVersion` 太旧，API Server 会返回**HTTP 410 Gone**，这时客户端会触发**List + Watch**操作来重新同步数据。



#### **总结**

- **一次请求、多次响应**的关键在于**HTTP/2 的长连接和流式传输**。
- watch 使用的**HTTP/2 协议、流式响应、多路复用和长连接**技术，避免了客户端的重复请求，提升了性能。
- **不需要客户端反复请求**，一条请求，API Server 持续推送。
- **网络协议的支撑**：HTTP/2 流、长连接、TLS 加密和数据分段传输。





### 各组件在HTTP/2的角色

#### **1. 各组件在 HTTP/2 请求中的角色**

| **组件对**                 | **客户端 (Client)** | **服务端 (Server)** | **协议**   | **是否使用长连接** | **长连接的作用**                           |
| -------------------------- | ------------------- | ------------------- | ---------- | ------------------ | ------------------------------------------ |
| **Scheduler - API Server** | **Scheduler**       | **API Server**      | **HTTP/2** | 是                 | Scheduler 向 API Server 申请调度的资源更新 |
| **Kubelet - API Server**   | **Kubelet**         | **API Server**      | **HTTP/2** | 是                 | Kubelet 监听 Pod 变更 (watch)              |
| **API Server - etcd**      | **API Server**      | **etcd**            | **gRPC**   | 是                 | API Server 查询/更新 etcd 数据             |

------

#### **2. 角色解析**

##### **(1) Scheduler - API Server**

- **客户端**：Scheduler 是客户端。

- **服务端**：API Server 是服务端。

- **通信方式**：Scheduler 通过**HTTP/2 长连接**请求 API Server。

- **请求类型**：

  - Scheduler 向 API Server 发送请求，筛选出未绑定的 Pod。

  - 当 Scheduler 决定将 Pod 绑定到某个节点时，它会向 API Server 发送 **Bind API 请求**。

  - 请求示例：

    ```http
    POST /api/v1/namespaces/default/pods/<pod-name>/binding HTTP/2
    ```

- **长连接作用**：

  - 由于 Scheduler 不需要**watch**资源（不像 kubelet 监听 Pod 变更），所以 Scheduler 的长连接更多是为了**提高请求性能**，避免频繁建立和关闭 TCP 连接。
  - 当有多个调度请求时，长连接的**多路复用**特性显著提高了效率。



##### **(2) Kubelet - API Server**

- **客户端**：Kubelet 是客户端。

- **服务端**：API Server 是服务端。

- **通信方式**：**HTTP/2 长连接**，**watch 机制**。

- **请求类型**：

  - kubelet 监听特定的资源（如 Pods）：

    ```http
    GET /api/v1/nodes/<node-name>/pods?watch=true&resourceVersion=<RV> HTTP/2
    ```

  - 通过 watch 机制，Kubelet 可以**实时监听 Pod 的变化**（新增、修改、删除）。

  - watch 机制通过**流式响应**，API Server 在资源变更时，**主动推送变更事件**到 Kubelet。

- **长连接作用**：

  - Kubelet 只发送**一次请求**，API Server 保持长连接，推送资源变更事件。
  - 如果 watch 连接断开，Kubelet 会使用最后的 `resourceVersion` 重新发起 watch 请求。



##### **(3) API Server - etcd**

- **客户端**：API Server 是客户端。

- **服务端**：etcd 是服务端。

- **通信方式**：**gRPC 长连接**（HTTP/2）。

- **请求类型**：

  - 读操作：

    ```go
    etcdClient.Get(ctx, "/registry/pods/default/nginx-pod")
    ```

  - 写操作：

    ```go
    etcdClient.Put(ctx, "/registry/pods/default/nginx-pod", "<pod-data>")
    ```

- **长连接作用**：

  - gRPC 是基于 **HTTP/2** 的远程过程调用（RPC）框架。
  - **API Server 不会在每次请求时重新创建 TCP 连接**，而是维持一个**持久的 HTTP/2 连接**，这显著减少了 etcd 和 API Server 之间的网络开销。
  - **etcd 使用 MVCC（多版本并发控制）** 机制，每个变更都会生成一个**新的 revision**，API Server 使用这个 revision 来进行增量监听。



#### **3. HTTPS 证书的使用**

> **在 Kubernetes 中的 "三套证书" 是指：**

1. **ETCD 组件通信证书**（API Server ↔ ETCD）
2. **Kubernetes 组件之间的通信证书**（API Server、Scheduler、Kubelet、Controller Manager）
3. **外部用户的通信证书**（kubectl、外部 API 请求）



##### **(1) Scheduler - API Server**

- **证书类型**：**Kubernetes 组件内部通信证书**
- 证书说明：
  - Scheduler 需要与 API Server 进行 HTTPS 认证。
  - API Server 公开了**kube-apiserver.crt** 和 **kube-apiserver.key**。
  - Scheduler 使用 **kube-controller-manager.crt** 和 **kube-controller-manager.key** 来与 API Server 通信。
  - 这些证书存储在 **/etc/kubernetes/pki** 目录下。
  - 组件之间的**客户端证书**和**服务器证书**均由 **Kubernetes CA 证书**签名。



##### **(2) Kubelet - API Server**

- **证书类型**：**Kubernetes 组件内部通信证书**
- 证书说明：
  - Kubelet 需要与 API Server 通信以获取 Pod 信息。
  - Kubelet 证书：**kubelet.crt** 和 **kubelet.key**。
  - Kubelet 使用 **client-certificate-data** 和 **client-key-data** 进行客户端身份验证。
  - API Server 端的 **kube-apiserver.crt** 和 **kube-apiserver.key** 用于提供 HTTPS 连接的服务端证书。



##### **(3) API Server - etcd**

- **证书类型**：**ETCD 组件通信证书**

- 证书说明

  ：

  - API Server 作为**客户端**，etcd 作为**服务端**。
  - etcd 证书：**etcd-server.crt** 和 **etcd-server.key**。
  - API Server 作为客户端发起请求时，使用 **etcd-client.crt** 和 **etcd-client.key** 进行双向认证。
  - 这也是三套证书中**专门为 ETCD 组件通信生成的证书**。



##### **总结三套证书的作用**

| **证书类型**      | **通信场景**                    | **证书路径**               | **作用**                                  |
| ----------------- | ------------------------------- | -------------------------- | ----------------------------------------- |
| **ETCD 组件证书** | API Server ↔ etcd               | /etc/kubernetes/pki/etcd/  | etcd 和 API Server 之间的加密通信         |
| **K8s 组件证书**  | kubelet、Scheduler ↔ API Server | /etc/kubernetes/pki/       | Kubelet、Scheduler、API Server 之间的通信 |
| **用户 API 证书** | kubectl ↔ API Server            | /etc/kubernetes/admin.conf | 用户使用 kubectl 访问 API Server          |



#### **4. 关键总结**

1. **谁是客户端，谁是服务端？**
   - **Scheduler ↔ API Server**: Scheduler 是客户端，API Server 是服务端。
   - **Kubelet ↔ API Server**: Kubelet 是客户端，API Server 是服务端。
   - **API Server ↔ etcd**: API Server 是客户端，etcd 是服务端。
2. **长连接**
   - **Scheduler 和 API Server 之间**：HTTP/2 长连接。
   - **Kubelet 和 API Server 之间**：HTTP/2 长连接（watch 机制，推送变化事件）。
   - **API Server 和 etcd 之间**：gRPC（基于 HTTP/2 的长连接）。
3. **三套证书的使用**
   - **ETCD 证书**：API Server ↔ etcd 通信。
   - **Kubernetes 组件证书**：Scheduler、Kubelet、Controller Manager 与 API Server 之间的通信。
   - **用户 API 证书**：外部用户（如 kubectl）与 API Server 之间的通信。





## Controller Manager详解

控制器有很多种，但是里面的逻辑是一样的，都是thinkloop, 每一个Controller都是一个生产者，消费者模型，一边监控API Server的变化，API Server支持watchable,任何事件发生了变化，通过watch机制就会通知，controller manager中的生产者就会观测到这些变化，这些变化发生后，会有将其放入中心队列中，消费者从这里取数据，取出来之后去做配置，所以任何控制器都是生产者消费者模型

- Controller Manager是集群大脑，是确保整个集群动起来的关键；
- 作用是确保Kubernetes遵循声明式系统规范，确保系统的真实状态(Actual State)与用户定义的期望状态（Desired State）一致；
- Controller Manager是多个控制器的组合，每个Controller事实上都是一个Controll loop，负责侦听其管控的对象，当对象发生变更时完成配置；
- Controller配置失败通常会触发自动重试，整个集群会在控制器不断重试的机制下确保最终一致性（Eventual Consistency）



### 控制器工作流程

![image-20241220161159816](D:\git_repository\cyber_security_learning\markdown_img\image-20241220161159816.png)

Informer and lister Overview

- Informer: Informers are responsible for watching Kubernetes resources and reacting to changes(events).They efficiently monitor resouces state by subscribing to API events like `add`,`update`and`Delete`.These events are produced by the Kubernetes API Server whenever relevant objects changed

- Lister: Listers provide cached access to resources. Instead of directly querying the API server, they interact with a local cache that is populated by informers. This makes controllers more efficient by reducing the number of API requests needed to get the current state of objects

Event Handling with Informers

- Event Registration: Informers register event handlers to listen for changes(like add, update,delete)to resources. Whenerver an event occurs (e.g.,a Pod is added or deleted), the informer triggers the corresponding handler

- Key Extraction: The handler processes the event by extracting the key of the affected object, typically composed of its namespace and name. This key uniquely identifies the object in the cluster

Queue and Rate-Limited Queue

- Work Queues: when an event occurs, instead of processing it immediately, the object's key is placed into a rate-limited queue. the rate-limiting aspect helps prevent overwhelming the controllers with too many requests, especially if there are repeated failures. if a failure occurs, the item can be re-enqueued after a delay based on the rate-limiting policy

- Rate Limiting: Rate limiting is crucial for handing failures gracefully. If processing an event fails (e.g., due to a temporary error or unavailability of resources),the object is re-enqueued after a backoff period, allowing the controller to retry the operation without overloading the system.

Worker and Consumer Logic:

- Workers: On the other side of the queue, worker goroutines continuously dequeue and process these events.Each worker pull a key from the queue and reconclies the state of the corresponding object by querying its details using the lister and then performing the required actions to converge the cluster's state towards the desired configuration.
- Reconciliation Loop: The worker performs a reconciliation loop,which consists of checking the current state of the resource,comparing it to the desired state, and taking corrective action if there is a discrepancy.For instance, if a Pod should be running but isn't the controller will take steps to start it.

Error Handling and Retry

- If the processing of an event fails, the key is re-queued with a delay(rate limiting) so that the controller can retry later. This mechanism helps handle transient error without discarding events and ensures that all objects eventually converge to their desired state.

Producer-Consumer Model

- THis entire flow is a classic producer-consumer model:
  - Producers: The informers produce events and enqueue the affected objects'keys.
  - Consumers: Workers act as consumers, dequeueing keys, and processing them until the queue is empty.

- 注意：
  - Informer 监听的是当前状态的变化，通过处理 API Server 推送的事件，确保本地缓存中的数据始终与 Kubernetes 集群中的实际状态保持同步。
  - Lister 提供的是对当前状态的访问，但这个状态是从 informer 的缓存中获取的。它是为了减少频繁的 API 请求，提升访问性能。



### Informer的内部机制

![image-20241220161252961](D:\git_repository\cyber_security_learning\markdown_img\image-20241220161252961.png)



- kubernetes提供了一系列的项目，该项目叫code generator，（Kubernetes 提供了工具，如 code-generator，可以自动为你生成 Go 语言的客户端、informer、lister 和深度拷贝函数。这些工具能大大简化自定义控制器的开发。你只需专注于定义自定义资源的结构体，剩下的代码生成工作交由 code-generator 完成。）这个项目的作用就是你要定义任何Kubernetes对象，定义这些对象时，只需要去定义它的数据结构，这个数据结构一旦创建好，在API Server这边发布，你就可以通过api Server去访问这个数据

- Informer首先会提供一个list&watch机制（informer在启动后会发起一个长连接到API server，通常来讲，会在第一时间list一下，比如一个pod list&watch，它会把当前所有的podlist下来，然后回创建watch连接，那么api server上有哪些pod的变化，就会告诉informer）
  - API Server是一个标准的RESTfulAPI， 它提供了一个string，一个json格式的序列化数据，如果我们的程序要去消费这个序列化的数据，那么就要反序列化，（就是把这个字符串转换为一个个go对象，这里使用反射机制实现，反射机制回去解析api server中的key，每一个对象的定义，它都会有json_tag，通过json tag，我们就会知道，这个json的key,对应go语言中的哪个属性，通过这种反射机制，就把一个序列化的对象，转换为go的struct）
  - 后续有一个Delta buff，一个环状内存结构（任何时候都可以一直往里写），如果我的buffer满了，就会自动覆盖最老的数据的
  - 然后他会做一个通知，让informer来处理这些数据
  - informer会把这些反序列化好的数据，放入thread Safe Store里面，这里有indexer，会有索引，我们在未来要去访问这些Kubernete对象的时候，就不需要去api server去访问了，我们只需要对local store访问，减少对api server的访问，然后同时这个对象的变化会通过event发给event handler，然后将对应的key提取出来放入queue中，由另一边的woker将其取走进行处理


- 任何的控制器都应该使用shareinformer的freemoke，所有的对象只要用了shareinformer的freemoke，所有对象在客户端，比方你要写个控制器，在你控制器端，所有api server对象已经有一份本地的缓存了，由shareinformer保证本地缓存和apiserver中对象的版本一致性，所以当我们写控制器代码的时候，应该避免直接访问api server。读取任何对象都应该去local store去读取（Thread safe store），而不是直接去api server去读。一般来讲，只有更新一个对象的时候才会去apiserver中更新，要去调用api server. 

- 注意上述的local store指的是代码里，内存里的store不是本地的那个cache目录，那个地方只是去拉取一下当前支持的api，它不会存储对象，真实的对象是存在控制器的local store的




### 控制器的协同工作原理

![image-20241220161329298](D:\git_repository\cyber_security_learning\markdown_img\image-20241220161329298.png)

- 创建一个deployment的资源清单，使用kubectl在客户端创建后，发给API Server

```shell
kubectl apply -f myapp-deployment.yaml
```

- API Server对我进行认证（通过读本地配置文件，知道我是谁），然后鉴权，因为我用的是admin的身份去登录的，所以我是有创建deployment的权限的，然后我的deployment又是合法的，所以我得deployment对象被API Server接收，并存入etcd中
- `kube-controller-manager`里面有一个deployment controller，顾名思义，它感兴趣的对象是deployment，它回去根据资源清单的属性，去创建一个replicaset的对象

```shell
# 查看deployment对象
kubectl describe deployment myapp -n learn01
Name:                   myapp
Namespace:              learn01
CreationTimestamp:      Tue, 01 Oct 2024 16:02:31 +0800
Labels:                 app=myapp
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               app=myapp
Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=myapp
  Containers:
   pod-test2:
    Image:         registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    Port:          <none>
    Host Port:     <none>
    Environment:   <none>
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   myapp-7547f4df6 (3/3 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  6m31s  deployment-controller  Scaled up replica set myapp-7547f4df6 to 3
```

- `kube-controller-manager`里面又有ReplicaSet Controller，它也在监听API Server，然后它监听到需要创建3个pod，然后当前pod不存在，一次就需要它去创建这3个pod，然后这个pod的对象由replicaset发到API Server

```shell
[root@master201 iventory]#kubectl get replicaset -n learn01
NAME              DESIRED   CURRENT   READY   AGE
myapp-7547f4df6   3         3         3       7m37s
[root@master201 iventory]#kubectl describe replicaset -n learn01
Name:           myapp-7547f4df6
Namespace:      learn01
Selector:       app=myapp,pod-template-hash=7547f4df6
Labels:         app=myapp
                pod-template-hash=7547f4df6
Annotations:    deployment.kubernetes.io/desired-replicas: 3
                deployment.kubernetes.io/max-replicas: 4
                deployment.kubernetes.io/revision: 1
Controlled By:  Deployment/myapp
Replicas:       3 current / 3 desired
Pods Status:    3 Running / 0 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:  app=myapp
           pod-template-hash=7547f4df6
  Containers:
   pod-test2:
    Image:         registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    Port:          <none>
    Host Port:     <none>
    Environment:   <none>
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Events:
  Type    Reason            Age   From                   Message
  ----    ------            ----  ----                   -------
  Normal  SuccessfulCreate  8m5s  replicaset-controller  Created pod: myapp-7547f4df6-fr2hh
  Normal  SuccessfulCreate  8m5s  replicaset-controller  Created pod: myapp-7547f4df6-nkgnd
  Normal  SuccessfulCreate  8m5s  replicaset-controller  Created pod: myapp-7547f4df6-s74wv
```

- API Server将该POd对象固化下来，存入etcd
- Pod对象被创建下来后，在初始状态下，pod内的nodename属性是没有被写值的

```shell
kubectl get pod myapp-7547f4df6-fr2hh -n learn01 -o yaml|grep -i nodename
nodeName: node205.feng.org
```

- 这个时候由于nodename是空，此时调度器Scheduler就会去做调度，调度器在API Server上watch了没有调度过的(nodename为空)pod对象，以及当前节点的所有节点，然后根据调度策略，判断当前那个节点最适合这个pod，然后将这个节点和pod做绑定，并将结果写入API Server

- 写回到API Server后，节点上的kubelet会关注当前API Server中，跟我的节点相关的pod有哪些，该节点发生了一个pod绑定后，会被kubelet发现，就会去本地查当前运行的pod有没有这个pod，如果没有，就会进入create pod的流程，起pod，如果pod没有外挂存储，就会使用runtime拉起pod，并调用网络插件为pod setup网络，如果需要外挂存储，就需要使用csi，为这个pod挂载磁盘


- 如果我删除一个pod，此时依然会产生一个事件event，这个事件是pod delete事件，该事件被replicaset controller监听到，它的职责是里面的所有pod的数量也用户的期望的数量应该是一样的，我删除了一个，此时实际pod数量和期望数量不等，就会被replicaset监测到，此时为了确保一致，他就会去创建一个新的pod







## SRV记录详解

SRV（**Service Locator Record**）是 DNS 中的一种记录类型，用于**指定某个服务的主机名（hostname）和端口号（port number）**，以便客户端可以通过它找到指定服务的实例。它的**主要作用是支持基于服务的发现**，特别是在分布式系统中非常有用。



### SRV 记录的结构

SRV 记录的结构由以下几个部分组成：

```kotlin
_service._protocol.name TTL class SRV priority weight port target
```

| **字段**    | **含义**                                                     |
| ----------- | ------------------------------------------------------------ |
| `_service`  | 服务名称，以 `_` 开头。例如，`_http` 表示 HTTP 服务。        |
| `_protocol` | 使用的协议，例如 `_tcp` 表示 TCP 协议，`_udp` 表示 UDP 协议。 |
| `name`      | 服务的域名，表示此服务所属的域。例如，`service-test.default.svc.cluster.local`。 |
| `TTL`       | 记录的生存时间（Time To Live），以秒为单位，表示该记录在 DNS 缓存中的有效期。 |
| `class`     | 通常为 `IN`，表示 Internet 类别的记录。                      |
| `SRV`       | 表示该记录是 SRV 类型。                                      |
| `priority`  | 优先级，数值越小优先级越高，客户端应优先使用优先级较高的目标服务器。 |
| `weight`    | 权重，用于在同一优先级下的负载均衡。权重越高，该服务器被选中的概率越高。 |
| `port`      | 服务运行的端口号。例如，HTTP 通常是 `80`，HTTPS 是 `443`。   |
| `target`    | 服务对应的主机名（域名），指向提供此服务的主机（可以是 Service 的名称或 Pod 的 IP）。 |



### **SRV 记录的示例**

假设 Kubernetes 中有一个名为 `service-test` 的 **Service**，位于 `default` 命名空间，域名后缀为 `cluster.local`，其 IP 为 `10.97.72.1`，并提供 TCP 协议的 HTTP 服务，监听端口 `80`。对应的 SRV 记录如下：

```kotlin
_http._tcp.service-test.default.svc.cluster.local. 30 IN SRV 0 100 80 service-test.default.svc.cluster.local.
```



### SRV记录的作用和用途

**服务发现：**

- SRV 记录可以让客户端动态发现服务的主机名和端口，而无需硬编码。
- 在 Kubernetes 中，Service 的 SRV 记录用于客户端通过 DNS 查询找到相应的服务实例。

**负载均衡：**

- SRV 记录支持通过 **priority** 和 **weight** 字段实现简单的负载均衡。
- 同一优先级的服务实例按照权重分配流量，优先级较高的服务会被优先选择。

**动态分布式系统：**

- 在微服务架构或分布式系统中，服务的实例可能动态扩缩容。SRV 记录允许客户端根据 DNS 动态获取服务的最新信息。

**灵活性：**

- SRV 记录可以为服务定义多个实例，每个实例的优先级和权重可以灵活调整，从而实现更复杂的负载分配策略。
