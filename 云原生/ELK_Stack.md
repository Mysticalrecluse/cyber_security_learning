# 	ELK概述

![image-20250119195308988](../markdown_img/image-20250119195308988.png)

## 什么是ELK

稍有一定规模的IT架构中，系统和应用的相关日志通常会分散在很多台不同的主机和相应的文件中

如果系统和应用出现异常和问题，相关的开发和运维人员想要排查原因，就要先登录到应用运行所相应的主机，找到上面的相关日志文件再进行查找和分析，所以非常不方便，此外还会涉及到权限和安全问题

而ELK的出现就很好的解决这一问题

ELK 是由一家 Elastic 公司开发的三个开源项目的首字母缩写，即是三个相关的项目组成的系统

这三个项目分别是：**Elasticsearch**、**Logstash** 和 **Kibana**。三个项目各有不同的功能

- **Elasticsearch** 是一个实时的全文搜索,存储库和分析引擎。
- **Logstash** 是数据处理的管道，能够同时从多个来源采集数据，转换数据，然后将数据发送到诸如 Elasticsearch 等存储库中。
- **Kibana** 则可以让用户在 Elasticsearch 中使用图形和图表对数据进行可视化。

之后又增加了许多新项目, 于是ELK从5.X版本后改名为Elastic Stack

目前 Elastic Stack 中除了Elasticsearch、Logstash 和 Kibana, 还包括一系列丰富的轻量型数据采集代 理，这些代理统称为 Beats，可用来向 Elasticsearch 发送数据。



**ELK stack的主要优点：**

- **功能强大**：Elasticsearch 是实时全文索引，具有强大的搜索功能
- **配置相对简单**：Elasticsearch 全部其于 JSON，Logstash使用模块化配置，Kibana的配置都比较简单。
- **检索性能高效**：基于优秀的设计，每次查询可以实时响应，即使百亿级数据的查询也能达到秒级响应。
- **集群线性扩展**：Elasticsearch 和 Logstash都可以灵活线性扩展
- **前端操作方便**：Kibana提供了比较美观UI前端，操作也比较简单



**EFK** 由**ElasticSearch**、**Fluentd**和**Kibana**三个开源工具组成。

**Fluentd**是一个实时开源的数据收集器,和logstash功能相似,这三款开源工具的组合为日志数据提供了分布式的实时搜集与分析的监控系统。



**Fluentd官网和文档:**

```http
https://www.fluentd.org/
https://docs.fluentd.org/
```



## Elasticsearch

### Elasticsearch 介绍

![image-20250119200330753](../markdown_img/image-20250119200330753.png)

**官方介绍**

```http
https://www.elastic.co/cn/elasticsearch
```



Elasticsearch 是一个分布式的免费开源搜索和分析引擎，适用于包括文本、数字、地理空间、结构化和 非结构化数据等在内的所有类型的数据。Elasticsearch 在 **Apache Lucene 的基础上开发**而成，由 Elasticsearch N.V.（即现在的 Elastic）于 2010 年首次发布。Elasticsearch 以其简单的 REST 风格 API、分布式特性、速度和可扩展性而闻名，是 Elastic Stack 的核心组件

Elasticsearch 支持数据的实时全文搜索搜索、支持分布式和高可用、提供API接口，可以处理大规模的 各种日志数据的处理，比如: Nginx、Tomcat、系统日志等功能。 

Elasticsearch **基于 Java 语言开发**，利用全文搜索引擎 Apache Lucene 实现



**为何使用 Elasticsearch？**

- **Elasticsearch 很快**。由于 Elasticsearch 是在 Apache Lucene 基础上构建而成的，所以在全文本搜索方面表现十分出色。Elasticsearch 同时还是一个近实时的搜索平台，这意味着从文档索引操作到文档变为可搜索状态之间的延时很短，一般只有一秒。因此，Elasticsearch 非常适用于对时间有严苛要求的用例，例如安全分析和基础设施监测。
- **Elasticsearch 具有分布式的本质特征。**Elasticsearch 中存储的文档分布在不同的容器中，这些容 器称为分片，可以进行复制以提供数据冗余副本，以防发生硬件故障。Elasticsearch 的分布式特性 使得它可以扩展至数百台（甚至数千台）服务器，并处理 PB 量级的数据。
- **Elasticsearch 包含一系列广泛的功能**。除了速度、可扩展性和弹性等优势以外，Elasticsearch 还 有大量强大的内置功能（例如数据汇总和索引生命周期管理），可以方便用户更加高效地存储和搜索数据。
- **Elastic Stack 简化了数据采集、可视化和报告过程。**通过与 Beats 和 Logstash 进行集成，用户能 够在向 Elasticsearch 中索引数据之前轻松地处理数据。同时，Kibana 不仅可针对 Elasticsearch  数据提供实时可视化，同时还提供 UI 以便用户快速访问应用程序性能监测 (APM)、日志和基础设 施指标等数据。



**Elasticsearch 在速度和可扩展性方面都表现出色，而且还能够索引多种类型的内容，可用于多种场景：**

- 应用程序搜索 
- 网站搜索 
- 企业搜索 
- 日志处理和分析 
- 基础设施指标和容器监测 
- 应用程序性能监测 
- 地理空间数据分析和可视化 
- 安全分析 
- 业务分析



### ELasticsearch原理

原始数据会从多个来源（包括日志、系统指标和网络应用程序）输入到 Elasticsearch 中。数据采集指在 Elasticsearch 中进行索引之前解析、标准化并充实这些原始数据的过程。这些数据在 Elasticsearch 中 索引完成之后，用户便可针对他们的数据运行复杂的查询，并使用聚合来检索自身数据的复杂汇总。在 Kibana 中，用户可以基于自己的数据创建强大的可视化，分享仪表板，并对 Elastic Stack 进行管理。

Elasticsearch 索引指**相互关联的文档集合**。Elasticsearch 会以 JSON 文档的形式存储数据。每个文档都会在一组键（字段或属性的名称）和它们对应的值（字符串、数字、布尔值、日期、数组、地理位置或 其他类型的数据）之间建立联系。

Elasticsearch 使用的是一种名为倒排索引的数据结构，这一结构的设计可以允许十分快速地进行全文本 搜索。倒排索引会列出在所有文档中出现的每个特有词汇，并且可以找到包含每个词汇的全部文档。

在索引过程中，Elasticsearch 会存储文档并构建倒排索引，这样用户便可以近乎实时地对文档数据进行 搜索。索引过程是在索引 API 中启动的，通过此 API 您既可向特定索引中添加 JSON 文档，也可更改特 定索引中的 JSON 文档



### 基本概念

**Near Realtime(NRT) 几乎实时**

Elasticsearch是一个几乎实时的搜索平台。意思是，从索引一个文档到这个文档可被搜索只需要一点点 的延迟，这个时间一般为毫秒级。



**Cluster 集群**

群集是一个或多个节点（服务器）的集合， 这些节点共同保存整个数据，并在所有节点上提供联合索引 和搜索功能。一个集群由一个唯一集群ID确定，并指定一个集群名（默认为“elasticsearch”）。该集群 名非常重要，因为节点可以通过这个集群名加入群集，一个节点只能是群集的一部分。

确保在不同的环境中不要使用相同的群集名称，否则可能会导致连接错误的群集节点。



**Node 节点**

节点是单个服务器实例，它是集群的一部分，可以存储数据，并参与群集的索引和搜索功能。就像一个 集群，节点的名称默认为一个随机的通用唯一标识符（UUID），确定在启动时分配给该节点。如果不希望默认，可以定义任何节点名。这个名字对管理很重要，目的是要确定网络服务器对应于ElasticSearch 群集节点。

我们可以通过集群名配置节点以连接特定的群集。默认情况下，每个节点设置加入名为“elasticSearch” 的集群。这意味着如果启动多个节点在网络上，假设他们能发现彼此都会自动形成和加入一个名为 “elasticsearch”的集群。

单个群集中，您可以拥有尽可能多的节点。此外，如果“elasticsearch”在同一个网络中，没有其他节 点正在运行，从单个节点的默认情况下会形成一个新的单节点名为"elasticsearch"的集群



**Index 索引** 

索引是**具有相似特性的文档集合**。例如，可以为客户数据提供索引，为产品目录建立另一个索引，以及 为订单数据建立另一个索引。索引由名称**（必须全部为小写）**标识，该名称用于在对其中的文档执行索 引、搜索、更新和删除操作时引用索引。在单个群集中，您可以定义尽可能多的索引。

```ABAP
注意: 索引名不支持大写字母
```



**Type 类型**

在索引中，可以定义一个或多个类型。类型是索引的逻辑类别/分区，其语义完全取决于您。一般来说， 类型定义为具有公共字段集的文档。例如，假设你运行一个博客平台，并将所有数据存储在一个索引 中。在这个索引中，您可以为用户数据定义一种类型，为博客数据定义另一种类型，以及为注释数据定 义另一类型。

Elasticsearch 版本对 type 概念的演变情况如下：

- 在 5.X 版本中，一个 index 下可以创建多个 type
- 在 6.X 版本中，一个 index 下只能存在一个 type
- 在 7.X 版本中，默认可以支持 type ,但可以禁用
- **在 8.X 版本中，直接就删除 type**,**即 index 不再支持 type**



**Document 文档**

文档是可以被索引的信息的基本单位。例如，您可以为单个客户提供一个文档，单个产品提供另一个文 档，以及单个订单提供另一个文档。本文件的表示形式为JSON（JavaScript Object Notation）格式，这 是一种非常普遍的互联网数据交换格式。

在索引/类型中，您可以存储尽可能多的文档。请注意，尽管文档物理驻留在索引中，**文档实际上必须索引**或分配到索引中的类型。



**Shards & Replicas 分片与副本**

索引可以存储大量的数据，这些数据可能超过单个节点的硬件限制。例如，十亿个文件占用磁盘空间 1TB的单指标可能不适合对单个节点的磁盘, 或者仅从单个节点的搜索请求服务可能太慢

为了解决这一问题，Elasticsearch提供细分指标分成多个块称为分片的能力。当创建一个索引，可以简 单地定义想要的分片数量。每个分片本身是一个全功能的、独立的“指数”，可以托管在集群中的任何节 点。

Shards分片的重要性主要体现在以下两个特征：

- 分片允许您水平拆分或缩放内容的大小
- 分片允许你分配和并行操作的碎片（可能在多个节点上）从而提高性能/吞吐量

在同一个集群网络或云环境上，故障是任何时候都会出现的，拥有一个故障转移机制以防分片和结点因 为某些原因离线或消失是非常有用的，并且被强烈推荐。为此，Elasticsearch允许你创建一个或多个拷 贝，索引分片进入所谓的副本或称作复制品的分片，简称Replicas。

注意：**ES的副本**指不包括主分片的其它副本,**即只包括备份**，这与Kafka是不同的

Replicas的重要性主要体现在以下两个特征：

- 副本为分片或节点失败提供了高可用性。需要注意的是，一个副本的分片不会分配在同一个节点作 为原始的或主分片，副本是从主分片那里复制过来的。
- 副本允许用户扩展你的搜索量或吞吐量，因为搜索可以在所有副本上并行执行。



**相关概念在关系型数据库和ElasticSearch中的对应关系**

| 关系型数据库    | Elasticsearch                                                |
| --------------- | ------------------------------------------------------------ |
| 数据库 Database | 索引 Index，支持全文检索                                     |
| 表 Table        | 类型 Type（废弃）                                            |
| 数据行 Row      | 文档 Document，但不需要固定结构，不同文档可以具有不同字段集合 |
| 数据列 Column   | 字段 Field                                                   |
| SQL语言         | DSL(domain specific language) 是Elasticsearch提供的JSON风格的请求语句， 用来操作ES实现CRUD |



## Logstash

```http
https://www.elastic.co/cn/what-is/elasticsearch
```

![image-20250119215819291](../markdown_img/image-20250119215819291.png)

Logstash 是 Elastic Stack 的核心产品之一，可用来对数据进行聚合和处理，并将数据发送到 Elasticsearch。

Logstash 是一个基于Java实现的开源的服务器端数据处理管道，允许您在将数据索引到 Elasticsearch 之前同时从多个来源采集数据，并对数据进行过滤和转换。

可以通过插件实现日志收集和转发，支持日志过滤，支持普通log、自定义json格式的日志解析。



## Kibana

Kibana 是一款适用于 Elasticsearch 的**基于Javascript语言**实现的数据可视化和管理工具，可以提供实时的直方图、线形图、饼状图和地图。Kibana 同时还包括诸如 Canvas 和 Elastic Maps 等高级应用程序； Canvas 允许用户基于自身数据创建定制的动态信息图表，而 Elastic Maps 则可用来对地理空间数据进行可视化。



**官方文档**

```http
https://www.elastic.co/cn/what-is/kibana
```



主要是通过接口调用elasticsearch的数据，并进行前端数据可视化的展现。

Kibana 与 Elasticsearch 和更广意义上的 Elastic Stack 紧密的集成在一起，这一点使其成为支持以下场 景的理想选择：

- 搜索、查看并可视化 Elasticsearch 中所索引的数据，并通过创建柱状图、饼图、表格、直方图和 地图对数据进行分析。仪表板视图能将这些可视化元素组织到一起，然后通过浏览器进行分享，以 提供对海量数据的实时分析视图，所支持的用例如下：
  - 日志处理和分析
  - 基础设施指标和容器监测
  - 应用程序性能监测 (APM) 
  - 地理空间数据分析和可视化
  - 安全分析
  - 业务分析 
- 借助网络界面来监测和管理 Elastic Stack 实例并确保实例的安全
- 针对基于 Elastic Stack 开发的内置解决方案（面向可观测性、安全和企业搜索应用程序），将其访 问权限集中到一起



## ELK应用场景

**运维主要应用场景：**

- 将分布在不同主机/容器的日志统一收集,并进行转换，通过集中的Web UI 进行查询和管理
- 通过查看汇总的日志,找到故障的根本原因
- Web 展示和报表功能
- 实现安全和事件等管理



**大数据运维主要应用场景：**

- 查询聚合, 大屏分析
- 预测告警, 网络指标，业务指标安全指标
- 日志查询，问题排查，基于API可以实现故障恢复和自愈
- 用户行为，性能,业务分析



## ELK应用架构

![image-20250119195308988](../markdown_img/image-20250119195308988.png)



##  其它方案

###  Fluentd 和 Fluent Bit

fluentd和fluent-bit都是有Treasure Data公司赞助开发的开源项目，这两个项目有很多相似之处

EFK：Elasticsearch，Fluentd，Fluent Bit，Kibana

ELK: Elasticsearch，Logstash，filebeat，Kibana



####  Fluentd

```http
https://www.fluentd.org/
```

![image-20250119220444011](../markdown_img/image-20250119220444011.png)

Fluentd 是开源社区中流行的日志收集工具，td-agent是其商业化版本，由Treasure Data公司维护，是本文选用的评测版本。

Fluentd 基于CRuby实现，并对性能表现关键的一些组件用C语言重新实现，整体性能不错。

Fluentd 作为一个很好的 Logstash 替代品，**Fluentd 是 DevOps 的最爱，特别是对于 Kubernetes 部 署，因为它具有丰富的插件库**。

Fluentd 与 Logstash 一样，它可以将数据结构化为 JSON，并涉及日志数据处理的所有方面：收集、解 析、缓冲和输出跨各种来源和目的地的数据



**优势**

- 支持许多日志源和目的地。
- 灵活、可扩展的解析选项，支持多种输入格式。
- 拥有庞大的生态系统，包括成百上千个插件,以及用Ruby自行编写插件的功能。
- 支持Apache 许可证，版本2.0
- 供应商中立（CNCF项目）
- 如果企业需要中立的供应商，Fluentd是不错的选择。它还经常与Kubernetes和容器化环境一起使 用。



**缺点**

- 解析前没有缓冲，可能会导致日志管道出现背压。
- 较于logstash，其插件支持相对少一些。



#### Fluent Bit

Fluent Bit 基于Fluentd体系结构和设计经验实现

Fluent Bit 不仅是一款日志收集工具，作数据流处理工具，并充当将日志数据转发到Fluentd的运送工具。

Fluent Bit 很适合在 Kubernetes集群等容器化环境中运行

Fluent Bit 很节省资源，因为它占用的空间很小。



**主要优势**

- 轻量级设计，内存占用量极小（通常不到1MB）
- 易于扩展的架构。
- 可插入式架构，有许多输入、过滤器和输出插件。
- 支持基于指标和基于日志的有效负载。
- 支持通过安全的连接将日志发送到存储后端。使用SQL，支持数据流处理。
- 支持Apache 许可证，版本2.0。供应商中立（CNCF项目）。
- Fluent Bit从众多日志源收集日志和指标,并将它们发送到不同的目的地
- Fluent Bit真正大放异彩的地方在于嵌入式、边缘及其他资源受限的环境，因为精简的运行时环境结合众多的输入/输出选项至关重要



**fluentd 和 fluent-bit 对比**

|          | fluentd                         | fluent-bit                                      |
| -------- | ------------------------------- | ----------------------------------------------- |
| 范围     | 容器/服务器                     | 容器/服务器                                     |
| 语言     | C和Ruby                         | C                                               |
| 大小     | 约40MB                          | 约450KB                                         |
| 性能     | 高性能                          | 高性能                                          |
| 依赖关系 | 作为Ruby Gem构建，主要依赖 gems | 除了一些安装编译插件（GCC、CMAKE）其它零 依赖。 |
| 插件支持 | 超过650个可用插件               | 大约35个可用插件                                |
| 许可证   | Apache许可证2.0版               | Apache许可证2.0版                               |

- Fluentd是日志收集器，处理器和聚合器。
- fluent-bit是一个日志收集器和处理器，因为它没有Fluentd等强大的聚合功能

两个项目相互补充，从而提供了完整的可靠轻量级日志解决方案，当然fluent-bit也可以独立完成日志收集。



### Loki

![image-20250119221835644](../markdown_img/image-20250119221835644.png)

```bash
#Loki文档网址：
https://grafana.com/docs/loki/latest/

#下载网址：
https://github.com/grafana/loki/releases
```

Loki 是由Grafana Labs团队开源的水平可扩展，高度可用的多租户日志聚合系统。基于 Go 语言开发

Loki 的设计具有很高的成本效益，并且易于操作

Loki 受到 Prometheus启发,也使用标签来作为索引，而不是对全文进行检索，通过这些标签既可以查询 日志的内容也可以查询到监控的数据签，极大地降低了日志索引的存储。



**典型的基于 Loki 的日志堆栈由 3 个组件组成：**

- **Loki** ：主服务器，负责摄取和存储日志以及处理查询。
- **Agent**：使用 Loki 一起分发的 Promtail 或者 Grafana 代理。通过代理抓取日志，通过添加标签将 日志转换为流，并通过 HTTP API 将流推送到 Loki。
- **Grafana**：用于 UI 展示，用于查询和显示日志数据。 您还可以使用 LogCLI 或直接使用 Loki API  从命令行查询日志。



**工作流程**

- 在应用程序服务器上安装promtail来收集日志然后发送给Loki存储
- 可以在Grafana UI界面通过添加Loki为数据源进行日志查询（如果Loki服务器性能不够，可以部署 多个Loki进行存储及查询）
- **作为一个日志系统不光只有查询分析日志的能力，还能对日志进行监控和报警。**



**与 ELK 比较优势**

- ELK虽然功能丰富，但规模复杂，资源占用高，很多功能往往用不上 
- loki 不对日志进行全文索引。通过存储压缩非结构化日志和索引元数据，Loki 操作起来会更简单， 更省成本。 
- 通过使用与 Prometheus 相同的标签记录流对日志进行索引和分组，这使得日志的扩展和操作效率 更高。 
- 安装部署简单快速，且受 Grafana 原生支持。 
- 适用于中小型规模的环境中



# Elasticsearch部署和管理

Elasticsearch 是一个分布式的免费开源搜索和分析引擎，适用于包括文本、数字、地理空间、结构化和 非结构化数据等在内的所有类型的数据



## Elasticsearch 安装说明

**官方文档**

```http
https://www.elastic.co/guide/en/elastic-stack/index.html
https://www.elastic.co/guide/en/elasticsearch/reference/master/install-elasticsearch.html
```



**部署方式**

- **包安装**
- **二进制安装** 
- **Docker 部署** 
- **Kubernetes 部署** 
- **Ansible 批量部署**



**ES支持操作系统版本和 Java 版本官方说明**

```http
https://www.elastic.co/cn/support/matrix
```

![image-20250119222614301](../markdown_img/image-20250119222614301.png)



## ELasticsearch安装前准备



###  安装前环境初始化

```bash
CPU 2C
内存4G或更多
操作系统: Ubuntu22.04,Ubuntu20.04,Ubuntu18.04,Rocky8.X,Centos 7.X
操作系统盘50G
主机名设置规则为nodeX.wang.org
生产环境建议准备单独的数据磁盘
```



####  主机名

```bash
#各服务器配置自己的主机名
[root@mystical ~]# hostnamectl set-hostname es-node1.mystical.org
```



#### 关闭防火墙和SELinux

关闭防所有服务器的防火墙和 SELinux

```bash
#RHEL系列的系统执行下以下配置
[root@es-node1 ~]# systemctl disable firewalld
[root@es-node1 ~]# systemctl disable NetworkManager
[root@es-node1 ~]# sed -i '/SELINUX/s/enforcing/disabled/' /etc/selinux/config
[root@es-node1 ~]# reboot

# Ubuntu
[root@es-node1 ~]# systemctl disable --now ufw
```



#### 各服务器配置本地域名解析

```bash
[root@es-node1 ~]# vim /etc/hosts
10.0.0.150 es-node1.mystical.org
10.0.0.151 es-node2.mystical.org
10.0.0.152 es-node3.mystical.org
```



#### 优化资源限制配置

**修改内核参数**

内核参数 `vm.max_map_count` 用于限制一个进程可以拥有的VMA(虚拟内存区域)的数量

使用默认系统配置，**二进制安装时会提示下面错误**，**包安装会自动修改此配置**

![image-20250119223514888](../markdown_img/image-20250119223514888.png)

```bash
#查看默认值
[root@ubuntu2204 ~]# sysctl -a |grep vm.max_map_count 
vm.max_map_count = 65530

[root@es-node1 ~]# sysctl -a |grep vm.max_map_count 
vm.max_map_count = 65530

#修改配置
[root@es-node1 ~]# echo "vm.max_map_count = 262144" >> /etc/sysctl.conf

#设置系统最大打开的文件描述符数
[root@es-node1 ~]# echo "fs.file-max = 1000000" >> /etc/sysctl.conf
[root@es-node1 ~]# sysctl -p 
vm.max_map_count = 262144

#Ubuntu22.04默认值已经满足要求
[root@ubuntu2204 ~]#sysctl fs.file-max
fs.file-max = 9223372036854775807
```



**范例: Ubuntu 基于包安装后会自动修改文件**

```bash
[root@node1 ~]#cat /usr/lib/sysctl.d/elasticsearch.conf
vm.max_map_count=262144
```



 **修改资源限制配置(可选)**

```bash
[root@es-node1 ~]#vi /etc/security/limits.conf
*               soft   core           unlimited
*               hard   core           unlimited
*               soft   nproc           1000000
*               hard   nproc           1000000
*               soft   nofile          1000000
*               hard   nofile          1000000
*               soft   memlock         32000
*               hard   memlock         32000
*               soft   msgqueue        8192000
*               hard   msgqueue        8192000
```



#### 关于JDK环境说明

```ABAP
1.x 2.x 5.x 6.x都没有集成JDK的安装包，也就是需要自己安装java环境
7.x 版本的安装包分为带JDK和不带JDK两种包，带JDK的包在安装时不需要再安装java，如果不带JDK的包
仍然需要自己去安装java
8.X 版本内置JDK，不再支持自行安装的JDK
```





## Elasticsearch 安装

### 包安装 Elasticsearch

#### 安装 Elasticsearch 包

下载链接

```ABAP
https://www.elastic.co/cn/downloads/elasticsearch
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/
```



![image-20250119224534985](../markdown_img/image-20250119224534985.png)



**范例：安装 elasticsearch-8**

```bash
#注意：是elasticsearch目录，不是enterprise-search目录
[root@ubuntu2204 ~]# wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/e/elasticsearch/elasticsearch-8.6.1-amd64.deb

[root@ubuntu2204 ~]# dpkg -i elasticsearch-8.6.1-amd64.deb
```



**安全验证**
8版本有安全验证，无法直接访问

```bash
--------------------------- Security autoconfiguration information ------------------------------

Authentication and authorization are enabled.
TLS for the transport and HTTP layers is enabled and configured.
# 服务启动后，必须使用这个密码才能访问
The generated password for the elastic built-in superuser is : zQWBLf_oPTQTVUE52Iam

If this node should join an existing cluster, you can reconfigure this with
'/usr/share/elasticsearch/bin/elasticsearch-reconfigure-node --enrollment-token <token-here>'
after creating an enrollment token on your existing cluster.

You can complete the following actions at any time:

Reset the password of the elastic built-in superuser with 
'/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic'.

Generate an enrollment token for Kibana instances with 
 '/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana'.

Generate an enrollment token for Elasticsearch nodes with 
'/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node'.

-------------------------------------------------------------------------------------------------
### NOT starting on installation, please execute the following statements to configure elasticsearch service to start automatically using systemd
 sudo systemctl daemon-reload
 sudo systemctl enable elasticsearch.service
### You can start elasticsearch service by executing
 sudo systemctl start elasticsearch.service
```



#### 启动Elasticsearch

```bash
systemctl enable --now elasticsearch

# elasticsearch中内置的java包安装路径
[root@ubuntu2204 ~]#/usr/share/elasticsearch/jdk/bin/java --version
openjdk 22.0.1 2024-04-16
OpenJDK Runtime Environment (build 22.0.1+8-16)
OpenJDK 64-Bit Server VM (build 22.0.1+8-16, mixed mode, sharing)
```



#### 直接运行Elasticsearch报错

```bash
# 直接访问报错，缺少证书
[root@ubuntu2204 ~]#curl https://10.0.0.121:9200
curl: (60) SSL certificate problem: self-signed certificate in certificate chain
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.

# 忽略证书也不行，401报错，需要认证
# 8.X版本特性
[root@ubuntu2204 ~]#curl https://10.0.0.121:9200 -k
{"error":{"root_cause":[{"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":["Basic realm=/"security/", charset=/"UTF-8/"","Bearer realm=/"security/"","ApiKey"]}}],"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":["Basic realm=/"security/", charset=/"UTF-8/"","Bearer realm=/"security/"","ApiKey"]}},"status":401}
```



#### 使用安装服务后生成的密码进行认证访问

```bash
[root@ubuntu2204 ~]#ES_PASSWD=zQWBLf_oPTQTVUE52Iam
# 访问成功
[root@ubuntu2204 ~]#curl -k -u "elastic:$ES_PASSWD" https://10.0.0.121:9200 -I 
HTTP/1.1 200 OK
X-elastic-product: Elasticsearch
content-type: application/json
content-length: 544

[root@ubuntu2204 ~]#curl -k -u "elastic:$ES_PASSWD" https://10.0.0.121:9200 
{
  "name" : "ubuntu2204.wang.org",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "FjrTC6U0TqS97R8CMAhtNQ",
  "version" : {
    "number" : "8.15.0",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "1a77947f34deddb41af25e6f0ddb8e830159c179",
    "build_date" : "2024-08-05T10:05:34.233336849Z",
    "build_snapshot" : false,
    "lucene_version" : "9.11.1",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```



#### 如果image忘记，重置生成新密码

```bash
# 方法1：生成随机密码
/usr/share/elasticsearch/bin/elasticsearch password -u elastic

# 方法2：交互式生成指定密码
/usr/share/elasticsearch/bin/elasticsearch-reset-password --username elastic -i
```



**该安全加固会对后续的产生影响**

在实际生产中，Elasticsearch会不可避免的和各种其他服务进行通信，这个过程中该认证会产生很多麻烦，所以在内网安全可到保证的情况下，建议把该安全加固取消



#### 取消安全认证

```bash
# 更改配置文件
vim /etc/elasticsearch/elasticsearch.yml

# 建议更改存放数据和日志的目录到单独的磁盘逻辑卷
# 使用逻辑卷方便以后扩容
path.data: /es/data
path.logs: /es/log

# 将xpack启用关闭
xpack.security.enabled: false

# 修改jvm.options文件
vim /etc/elasticsearch/jvm.options
# 调整JVM heap size，做实验可以将其调小，但是生产环境要保证足够
-Xms512m
-Xmx512m
# 后续优化es的启动，垃圾回收等也是在这里进行优化

# 直接访问
[root@ubuntu2204 ~]#curl 10.0.0.121:9200
{
  "name" : "ubuntu2204.wang.org",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "pcqcKf6YQ2yDJlxpmIrhNA",
  "version" : {
    "number" : "8.15.0",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "1a77947f34deddb41af25e6f0ddb8e830159c179",
    "build_date" : "2024-08-05T10:05:34.233336849Z",
    "build_snapshot" : false,
    "lucene_version" : "9.11.1",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```





### 二进制安装Elasticsearch

官方文档

```http
https://www.elastic.co/guide/en/elasticsearch/reference/master/targz.html
```



#### 下载二进制文件

```http
https://www.elastic.co/cn/downloads/elasticsearch
```

![image-20250120180545468](../markdown_img/image-20250120180545468.png)



 **基于二进制包含JDK文件安装**

```bash
[root@es-node1 ~]# wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.15.0-linux-x86_64.tar.gz

[root@es-node1 ~]# ls
elasticsearch-8.15.0-linux-x86_64.tar.gz

# 解压至/usr/local
[root@es-node1 ~]# tar xf elasticsearch-8.15.0-linux-x86_64.tar.gz -C /usr/local/

# 创建软连接
[root@es-node1 ~]# ln -s /usr/local/elasticsearch-8.15.0/ /usr/local/elasticsearch
[root@es-node1 ~]# ls /usr/local/elasticsearch
bin  config  jdk  lib  LICENSE.txt  logs  modules  NOTICE.txt  plugins  README.asciidoc
```



**编辑服务配置文件（集群配置）**

```bash
# 关闭安全功能
[root@es-node1 /data/es-logs]# vim /usr/local/elasticsearch/config/elasticsearch.yml
# Enable security features
xpack.security.enabled: false

```



**修改ELK内存配置**

修改ELK内存配置，推荐使用宿主机物理内存的一半，最大不超过30G

```bash
[root@es-node1 ~]# vim /usr/local/elasticsearch/config/jvm.options
-Xms1g
-Xmx1g
```



**创建用户**

从ES7.X以后版不允许以root启动服务，需要委创建专用的用户

```bash
[root@es-node1 ~]# useradd -r elasticsearch
```



**目录权限更改**

在所有节点上创建数据和日志目录并修改目录权限为elasticsearchv

```bash
# 更改数据和日志目录
[root@es-node1 ~]# vim /usr/local/elasticsearch/config/elasticsearch.yml
path.data: /data/es-data
path.logs: /data/es-logs

[root@es-node1 /usr/local]# mkdir /data/es-{data,logs} -p
[root@es-node1 /usr/local]# chown -R elasticsearch.elasticsearch /data/

#修改elasticsearch安装目录权限
[root@es-node1 ~]# chown -R elasticsearch.elasticsearch /usr/local/elasticsearch/
```



**创建service文件**

```bash
[root@es-node2 ~]# vim /lib/systemd/system/elasticsearch.service
[Unit]
Description=Elasticsearch
Documentation=http://www.elastic.co
Wants=network-online.target
After=network-online.target

[Service]
RuntimeDirectory=elasticsearch
PrivateTmp=true
Environment=PID_DIR=/var/run/elasticsearch
WorkingDirectory=/usr/local/elasticsearch
User=elasticsearch
Group=elasticsearch
ExecStart=/usr/local/elasticsearch/bin/elasticsearch -p ${PID_DIR}/elasticsearch.pid --quiet
# StandardOutput is configured to redirect to journalctl since
# some error messages may be logged in standard output before
# elasticsearch logging system is initialized. Elasticsearch
# stores its logs in /var/log/elasticsearch and does not use
# journalctl by default. If you also want to enable journalctl
# logging, you can simply remove the "quiet" option from ExecStart.
# Specifies the maximum file descriptor number that can be opened by this process
LimitNOFILE=65535
# Specifies the maximum number of processes
LimitNPROC=4096
# Specifies the maximum size of virtual memory
LimitAS=infinity
# Specifies the maximum file size
LimitFSIZE=infinity
# Disable timeout logic and wait until process is stopped
TimeoutStopSec=0
# SIGTERM signal is used to stop the Java process
KillSignal=SIGTERM
# Send the signal only to the JVM rather than its control group
KillMode=process
# Java process is never killed
SendSIGKILL=no
# When a JVM receives a SIGTERM signal it exits with code 143
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target
```



**启动ELasticsearch服务**

在所有节点上配置并启动

```bash
[root@es-node1 ~]# echo 'PATH=/usr/local/elasticsearch/bin:$PATH' > /etc/profile.d/elasticsearch.sh
[root@es-node1 ~]# . /etc/profile.d/elasticsearch.sh
[root@es-node1 /usr/local]# systemctl start elasticsearch.service
[root@es-node1 /usr/local]# systemctl enable elasticsearch.service 
Created symlink /etc/systemd/system/multi-user.target.wants/elasticsearch.service → /lib/systemd/system/elasticsearch.service.
```



**验证端口监听成功**

```bash
[root@es-node1 /data/es-logs]# ss -nlt
State       Recv-Q      Send-Q                Local Address:Port           Peer Address:Port      Process   
LISTEN      0           4096                  127.0.0.53%lo:53                  0.0.0.0:*                   
LISTEN      0           128                       127.0.0.1:6010                0.0.0.0:*                   
LISTEN      0           128                         0.0.0.0:22                  0.0.0.0:*                   
LISTEN      0           4096             [::ffff:127.0.0.1]:9300                      *:*                   
LISTEN      0           4096                          [::1]:9300                   [::]:*                   
LISTEN      0           128                           [::1]:6010                   [::]:*                   
LISTEN      0           4096                              *:9200                      *:*                   
LISTEN      0           128                            [::]:22                     [::]:* 
```



**通过浏览器访问 Elasticsearch 服务端口**

```bash
[root@es-node1 /data/es-logs]# curl 10.0.0.150:9200
{
  "name" : "es-node1.mystical.org",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "5Igla64GQ8Ga5rBNDcQ8Zw",
  "version" : {
    "number" : "8.15.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "1a77947f34deddb41af25e6f0ddb8e830159c179",
    "build_date" : "2024-08-05T10:05:34.233336849Z",
    "build_snapshot" : false,
    "lucene_version" : "9.11.1",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```



### 多节点集群部署

#### 部署前准备

注意：此方式需要3G以上内存，否则会出现OOM报错

修改内核参数，默认无法启动，会出现下面错误提示

```ABAP
ERROR: [1] bootstrap checks failed
[1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```

```bash
[root@es-node1 ~]# echo vm.max_map_count=262144 >> /etc/sysctl.conf
[root@es-node1 ~]# sysctl -p
```



#### **服务端口解析**

```
9200端口：用于web访问
9300端口：用于集群内nodes之间通信
```



#### 集群配置

8.X 集群配置

```bash
#默认配置文件需要以下六行
[root@es-node1 ~]# vim /usr/local/elasticsearch/config/elasticsearch.yml 
cluster.name: my-application #指定集群名称，同一个集群内的所有节点相同
node.name: node-1            #修改此行，每个节点不同

# 集群模式必须修改此行，默认是127.0.0.1:9300,否则集群节点无法通过9300端口通信，每个节点相同
network.host: 0.0.0.0     
# 用于发现集群内节点地址
discovery.seed_hosts: ["10.0.0.150", "10.0.0.151", "10.0.0.152"] 
# 指定允许参与主节点选举的nodes
cluster.initial_master_nodes: ["10.0.0.150", "10.0.0.151", "10.0.0.152"]

# 下面这行和上面的相同，将其注释掉防止冲突
# cluster.initial_master_nodes: ["ubuntu2204.wang.org"]     #将此行注释

path.data: /data/es-data
path.logs: data/es-logs

# 改完后重启服务
[root@es-node1 /usr/local/elasticsearch]# systemctl restart elasticsearch

# 查看集群信息
[root@es-node1 /usr/local/elasticsearch/config]# curl 10.0.0.150:9200/_cat/nodes
10.0.0.152 34 96  3 0.30 0.18 0.20 cdfhilmrstw - node-3
10.0.0.150 33 72  7 0.28 0.19 0.10 cdfhilmrstw * node-1
10.0.0.151 41 96 27 0.79 0.25 0.12 cdfhilmrstw - node-2
```







## 优化ELK资源配置



### 开启bootstrap.memory_lock优化

**开启 bootstrap.memory_lock: true 可以优化性能，但会导致无法启动的错误解决方法**

注意：开启 `bootstrap.memory_lock: true` 需要足够的内存，建议4G以上，否则内存不足，启动会很失败或很慢

作用：用于在启动前给`Elasticsearch`预留充足的内存空间

```bash
# 开启此功能建议堆内存大小设置是总内存的一半，也就是内存充足的情况下使用
[root@es-node1 ~]# vim /etc/elasticsearch/elasticsearch.yml 
#开启此功能导8.X致集群模式无法启动,但单机模式可以启动
bootstrap.memory_lock: true

[root@es-node1 ~]# systemctl restart elasticsearch.service 
Job for elasticsearch.service failed because the control process exited with 
error code.
See "systemctl status elasticsearch.service" and "journalctl -xe" for details.

# #8.X致集群模式需要修改如下配置
#方法1：直接修改elasticsearch.service 
[root@es-node1 ~]# vim /lib/systemd/system/elasticsearch.service 
[Service]
#加下面一行
LimitMEMLOCK=infinity

# 更改后重启服务
[root@es-node2 /usr/local/elasticsearch]# systemctl daemon-reload 
[root@es-node2 /usr/local/elasticsearch]# systemctl restart elasticsearch.service
```



### 内存优化

**官方文档**

```http
https://www.elastic.co/guide/en/elasticsearch/reference/current/importantsettings.html#heap-size-settings
```



**推荐使用宿主机物理内存的一半，ES的heap内存最大不超过30G,26G是比较安全的**

```bash
堆大小应基于可用 RAM：
将 Xms 和 Xmx 设置为不超过总内存的 50%。 Elasticsearch 需要内存用于 JVM 堆以外的用途。 例如，Elasticsearch 使用堆外缓冲区来实现高效的网络通信，并依靠操作系统的文件系统缓存来高效地访问文件。 JVM 本身也需要一些内存。 Elasticsearch 使用比 Xmx 设置配置的限制更多的内存是正常的。在容器（例如 Docker）中运行时，总内存定义为容器可见的内存量，而不是主机上的总系统内存。将 Xms 和 Xmx 设置为不超过压缩普通对象指针 (oops) 的阈值。 确切的阈值会有所不同，但在大多数系统上 26GB 是安全的，在某些系统上可能高达 30GB。 要验证您是否低于阈值，请检查 Elasticsearch日志中的条目，如下所示：
```



#### **关于OOPS的说明**

```markdown
Managed pointers in the Java heap point to objects which are aligned on 8-byte address boundaries. Compressed oops represent managed pointers (in many but not all places in the JVM software) as 32-bit object offsets from the 64-bit Java heap base address.

Because they're object offsets rather than byte offsets, they can be used to address up to four billion objects (not bytes), or a heap size of up to about 32 gigabytes.

To use them, they must be scaled by a factor of 8 and added to the Java heap base address to find the object to which they refer. Object sizes using compressed oops are comparable to those in ILP32 mode.

Java 堆中的托管指针指向在 8 字节地址边界上对齐的对象。 压缩 oop 将托管指针（在 JVM 软件中的许多但不是所有地方）表示为相对于 64 位 Java 堆基地址的 32 位对象偏移量。
因为它们是对象偏移量而不是字节偏移量，所以它们可用于处理多达 40 亿个对象（不是字节），或高达约32GB的堆大小。
要使用它们，必须将它们缩放 8 倍并添加到 Java 堆基地址以找到它们所引用的对象。 使用压缩 oop 的对象大小与 ILP32 模式中的对象大小相当。
```



#### **关于 Heap 内存大小**

```markdown
虽然JVM可以处理大量的堆内存，但是将堆内存设置为过大的值可能导致以下问题：

堆内存分配的效率低。Java语言本身就是一种高级语言，这意味着需要更多的堆内存来存储对象。但是，当堆内存过大时，分配对象所需的时间也会相应增加，这可能会导致应用程序出现性能问题。

操作系统内存管理的限制。操作系统必须以页为单位进行内存管理。如果Java堆内存过大，则需要更多的页来管理堆内存。这可能会导致操作系统出现性能问题。

垃圾回收(Garbage Collection, GC)：JVM内存的一部分被用于存储对象，这些对象随着时间的推移可能不再需要。这些不再需要的对象被视为“垃圾”，需要由垃圾收集器清除，以释放内存空间。然而，执行GC会暂停所有的应用线程，这被称为 "Stop-the-World"（暂停世界）。这种暂停可能会影响应用的性能和响应时间。一般来说，如果堆内存非常庞大，GC需要检查和清理的对象数量会变得非常庞大，这会导致GC操作的时间变得非常漫长。

对象指针的大小：在某些JVM实现（例如Oracle的HotSpot），在堆（Heap）大小超过32GB之后，对象指针的表示将从32位压缩oops（Ordinary Object Pointers普通对象指针）转变为64位非压缩指针，这导致了内存使用的增加。如果内存设置接近或略超过32GB，实际上可能会因为此原因造成更多的内存消耗。因此，通常在32GB以下时，我们会使用32位压缩指针，而超过这个阈值时，除非有明确的需要，否则通常会选择保持在30GB左右以避免转为64位指针。

因此，建议将Java堆内存设置为合适的大小，以便在GC操作的同时与应用程序的性能之间进行平衡。通常情况下，堆内存应该设置为操作系统的物理内存的一半或三分之一。虽然这个数字可能会因系统配置和工作负载而有所变化，但是在32G的机器上，32G的堆空间已经超出了大部分Java应用程序的需求，因此更大的堆内存并不是必要的。

当然，根据具体的应用场景和需求，以及你使用的具体的JVM版本和垃圾收集器类型，这个30GB的规则并非绝对。比如ZGC和Shenandoah这类的低延迟垃圾回收器就可以处理大于30GB的堆内存，同时还能保持低停顿时间。
```



#### **内存优化建议**

为了保证性能，每个ES节点的JVM内存设置具体要根据 node 要存储的数据量来估算,建议符合下面约定

- 在内存和数据量有一个建议的比例：对于一般日志类文件，1G 内存能存储**48G~96GB**数据
- JVM 堆内存最大不要超过30GB
- 单个分片控制在30-50GB，太大查询会比较慢，索引恢复和更新时间越长；分片太小，会导致索引 碎片化越严重，性能也会下降

```bash
# 范例
#假设总数据量为1TB，3个node节点，1个副本；那么实际要存储的大小为2TB
每个节点需要存储的数据量为:2TB / 3 = 700GB，每个节点还需要预留20%的空间，所以每个node要存储大约 700*100/80=875GB 的数据；每个节点按照内存与存储数据的比率计算：875GB/48GB=18，即需要JVM内存为18GB,小于30GB
因为要尽量控制分片的大小为30GB；875GB/30GB=30个分片,即最多每个节点有30个分片

#思考：假设总数据量为2TB，3个node节点，1个副本呢？
```



#### **指定heap内存最小和最大内存限制**

```bash
#建议将heap内存设置为物理内存的一半且最小和最大设置一样大,但最大不能超过30G
[root@es-node1 ~]# vim /etc/elasticsearch/jvm.options 
-Xms30g
-Xmx30g

#每天产生1TB左右的数据量的建议服务器配置，还需要定期清理磁盘
16C 64G 6T硬盘 共3台服务器
```



#### **修改service文件，做优化配置**

```bash
[root@es-node1 ~]# vim /usr/lib/systemd/system/elasticsearch.service #修改内存限制
LimitNOFILE=1000000       #修改最大打开的文件数，默认值为65535
LimitNPROC=65535          #修改打开最大的进程数，默认值为4096
LimitMEMLOCK=infinity     #无限制使用内存，以前旧版需要修改，否则无法启动服务，8.X当前版本无需修改
```







## Elasticsearch插件

通过使用各种插件可以实现对 ES 集群的**状态监控**, **数据访问**, **管理配置**等功能



**ES集群状态：**

- **green 绿色状态**:表示集群各节点运行正常，而且没有丢失任何数据，各主分片和副本分片都运行正常
- **yellow 黄色状态:**表示由于某个节点宕机或者其他情况引起的，node节点无法连接、所有主分片都正常分配,有副本分片丢失，但是还没有丢失任何数据
- r**ed 红色状态:**表示由于某个节点宕机或者其他情况引起的主分片丢失及数据丢失,但仍可读取数据和存储



**监控下面两个条件都满足才是正常的状态**

- **集群状态为 green**
- **所有节点都启动**



### Head插件

Head 是一个 ES 在生产较为常用的插件，目前此插件更新较慢，还是2018年4月的版本



#### 浏览器安装插件

**离线安装**

先下载Head插件文件,再离线安装，支持Chrome 内核的各种浏览器，比如：edge，chrome

**注意：要打开开发者模式**

![image-20250120175237353](../markdown_img/image-20250120175237353.png)

```bash
# 下载Head插件安装包
https://www.mysticalrecluse.com/script/tools/ElasticSearch-Head-0.1.5_0.zip

# 解压后将文件夹导入浏览器
```

![image-20250120175807173](../markdown_img/image-20250120175807173.png)

![image-20250120175837414](../markdown_img/image-20250120175837414.png)

![image-20250120175856082](../markdown_img/image-20250120175856082.png)

**输入地址链接**

![image-20250120175956894](../markdown_img/image-20250120175956894.png)



### Cerebro插件

#### cerebro插件介绍

![image-20250121152023926](../markdown_img/image-20250121152023926.png)

Cerebro 是开源的 elasticsearch 集群 Web 管理程序，此工具应用也很广泛，此项目升级比 Head 频繁

当前最新版本为Apr 10, 2021发布的 v0.9.4

Cerebro v0.9.3 版本之前需要 java1.8 或者更高版本

Cerebro v0.9.4 版本更高版本需要 Java11



**github链接**

```http
https://github.com/lmenezes/cerebro
```

![image-20250121152207033](../markdown_img/image-20250121152207033.png)



#### 包安装

**注意：安装cerebro内存建议大于3G以上**

```bash
#依赖JDK
[root@ubuntu2004 ~]# apt update && apt -y install openjdk-11-jdk

# #下载包,官方提供了DEB和RPM包
[root@ubuntu2204 ~]# wget https://mirror.ghproxy.com/https://github.com/lmenezes/cerebro/releases/download/v0.9.4/cerebro_0.9.4_all.deb

#安装
[root@ubuntu2004 ~]# dpkg -i cerebro_0.9.4_all.deb

# 启动
[root@ubuntu2004 ~]# systemctl start cerebro.service 

# 修改配置文件
[root@ubuntu2004 ~]# vim /etc/cerebro/application.conf
data.path: "/var/lib/cerebro/cerebro.db" #取消此行注释
#data.path = "./cerebro.db" #注释此行，默认路径是/usr/share/cerebro/cerebro.db

#此目录自动生成
[root@ubuntu2204 ~]#l l -d /var/lib/cerebro
drwxr-xr-x 2 cerebro cerebro 4096  1月 21 15:52 /var/lib/cerebro/

# 重启服务
[root@ubuntu2204 ~]#systemctl restart cerebro.service

# 默认监听9000端口

# 访问浏览器：10.0.0.132:9000,并输入es集群IP连接
```

![image-20250121155806662](../markdown_img/image-20250121155806662.png)

![image-20250121155819105](../markdown_img/image-20250121155819105.png)





## ELasticsearch访问

Elasticsearch 支持各种语言使用 RESTful API 通过端口 9200 与之进行通信，可以用你习惯的 web 客户 端访问 Elasticsearch 



**可以用三种方式和 Elasticsearch进行交互**

- **curl 命令**和其它浏览器: 基于命令行,操作不方便
- **插件**: 在node节点上安装head,Cerebro 等插件,实现图形操作,查看数据方便
- **Kibana**: 需要java环境并配置,图形操作,显示格式丰富



### Shell命令

#### 查看ES集群状态

```bash
# 查看支持的指令
[root@mystical /es/log]# curl http://127.0.0.1:9200/_cat

#查看es集群状态，?v是详细显示 ?human是可阅读显示
[root@mystical /es/log]# curl http://127.0.0.1:9200/_cat/health
1737435286 04:54:46 my-es1 green 3 3 0 0 0 0 0 0 - 100.0%

[root@mystical /es/log]# curl 'http://127.0.0.1:9200/_cat/health?v'
epoch      timestamp cluster status node.total node.data shards pri relo init unassign pending_tasks max_task_wait_time active_shards_percent
1737435296 04:54:56  my-es1  green           3         3      0   0    0    0        0             0                  -                100.0%

[root@mystical /es/log]# curl 'http://127.0.0.1:9200/_cat/health?human'
1737435365 04:56:05 my-es1 green 3 3 0 0 0 0 0 0 - 100.0%

#查看集群分健康性,获取到的是一个json格式的返回值，那就可以通过python等工具对其中的信息进行分析
#注意：status 字段为green才是正常状态
[root@mystical /es/log]# curl http://127.0.0.1:9200/_cluster/health?pretty=true
{
  "cluster_name" : "my-es1",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 3,
  "number_of_data_nodes" : 3,
  "active_primary_shards" : 0,
  "active_shards" : 0,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 100.0
}

#查看所有的节点信息
[root@mystical /es/log]# curl 'http://127.0.0.1:9200/_cat/nodes?v'
ip         heap.percent ram.percent cpu load_1m load_5m load_15m node.role   master name
10.0.0.152           27          97   0    0.04    0.05     0.07 cdfhilmrstw *      es-node3
10.0.0.151           50          97   0    0.00    0.03     0.07 cdfhilmrstw -      es-node2
10.0.0.150           53          97   0    0.07    0.08     0.08 cdfhilmrstw -      es-node1


#列出所有的索引 以及每个索引的相关信息
[root@mystical /es/log]# curl 'http://127.0.0.1:9200/_cat/indices?v'
health status index uuid pri rep docs.count docs.deleted store.size pri.store.size dataset.size

# Master节点
[root@mystical /es/log]# curl 'http://127.0.0.1:9200/_cat/master?v'
id                     host       ip         node
zo37jquZSimiJTu7kCMjmA 10.0.0.152 10.0.0.152 es-node3

# 集群节点
[root@mystical /es/log]# curl 'http://127.0.0.1:9200/_cat/nodes?human'
10.0.0.152 31 97 0 0.02 0.04 0.07 cdfhilmrstw * es-node3
10.0.0.151 53 97 0 0.04 0.03 0.06 cdfhilmrstw - es-node2
10.0.0.150 56 97 0 0.03 0.07 0.08 cdfhilmrstw - es-node1
```



#### 创建和查看索引

```bash
#创建索引index1,简单输出
[root@mystical /es/log]# curl -XPUT '127.0.0.1:9200/index1'
{"acknowledged":true,"shards_acknowledged":true,"index":"index1"}

# 根据下图显示可以看出：没有分片（因为显示0），但是有一个副本（不包括原始数据自己，只计算副本数）
```

![image-20250121130543467](../markdown_img/image-20250121130543467.png)

```bash
# 关闭es-node1节点，再观察
[root@mystical /es/log]# systemctl stop elasticsearch.service

# 健康性变为黄色，然后主副本变为es-node3
# 即副本丢了，但是数据能正常访问，因此变黄
[root@es-node2 ~]# curl 127.0.0.1:9200/_cat/health?
1737436100 05:08:20 my-es1 yellow 2 2 1 1 0 0 1 0 - 50.0%
```

![image-20250121130731207](../markdown_img/image-20250121130731207.png)

```bash
# 过一段时间后，会在node2上重建副本，集群变为绿色
[root@es-node2 ~]# curl 127.0.0.1:9200/_cat/health?
1737436100 05:08:20 my-es1 green 2 2 2 1 0 0 0 0 - 100.0%
```

![image-20250121130959573](../markdown_img/image-20250121130959573.png)

```ABAP
颜色含义：
绿色：完全健康
黄色：副本丢了，数据没丢
红色：数据丢失
```

```bash
# 关闭es-node2节点，再观察
[root@mystical /es/log]# systemctl stop elasticsearch.service

# 因为少于半数以上可用，即3个节点的集群，关了两个，因此集群不可用，es无法访问
```

![image-20250121131436529](../markdown_img/image-20250121131436529.png)

```bash
#创建索引index2,格式化输出
[root@mystical /es/log]# curl -XPUT '127.0.0.1:9200/index2?pretty'
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "index2"
}

#查看所有索引
[root@mystical /es/log]# curl 'http://127.0.0.1:9200/_cat/indices?v'
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size dataset.size
green  open   index1 _uA6DC1BTy2gZdJPip6sGw   1   1          0            0       498b           249b         249b
green  open   index2 ThbaBIClSUazA8YQ33WqPQ   1   1          0            0       454b           227b         227b

# 查看索引格式化输出
[root@mystical /es/log]# curl 'http://127.0.0.1:9200/index1?pretty'
{
  "index1" : {
    "aliases" : { },
    "mappings" : { },
    "settings" : {
      "index" : {
        "routing" : {
          "allocation" : {
            "include" : {
              "_tier_preference" : "data_content"
            }
          }
        },
        "number_of_shards" : "1",            # 分片数
        "provided_name" : "index1",
        "creation_date" : "1737435726084",
        "number_of_replicas" : "1",          # 副本数（不含原数据）
        "uuid" : "_uA6DC1BTy2gZdJPip6sGw",
        "version" : {
          "created" : "8512000"
        }
      }
    }
  }
}

# 创建3个分片和2个副本的索引
[root@mystical /es/log]# curl -XPUT '127.0.0.1:9200/index3' -H 'Content-Type: application/json' -d '
{                     
  "settings": {
    "index": {
      "number_of_shards": 3,  
      "number_of_replicas": 2
   }                         
 }
}'
{"acknowledged":true,"shards_acknowledged":true,"index":"index3"}

```

![image-20250121132533883](../markdown_img/image-20250121132533883.png)

```bash
# 创建3分片，1副本（生产中建议分片数和节点数相同，实现负载均衡）
[root@mystical /es/log]# curl -XPUT '127.0.0.1:9200/index4' -H 'Content-Type: application/json' -d '
{                     
  "settings": {
    "index": {
      "number_of_shards": 3,  
      "number_of_replicas": 1
   }                         
 }
}'
{"acknowledged":true,"shards_acknowledged":true,"index":"index4"}

# ES自动将分片数据均匀的放在不同节点上，实现高可用
```

![image-20250121132811946](../markdown_img/image-20250121132811946.png)

```bash
# 关闭es-node2
[root@es-node2 ~]# systemctl stop elasticsearch.service

# 健康性检测为黄色，且无法恢复为绿色，因为index3索引副本缺失
[root@mystical /es/log]# curl 127.0.0.1:9200/_cat/health?
1737437626 05:33:46 my-es1 yellow 2 2 16 8 0 0 3 0 - 84.2%
```

![image-20250121133408182](../markdown_img/image-20250121133408182.png)

```bash
# 创建副本index5,3分片，0副本
[root@mystical /es/log]# curl -XPUT '127.0.0.1:9200/index5' -H 'Content-Type: application/json' -d '
{                     
  "settings": {
    "index": {
      "number_of_shards": 3,  
      "number_of_replicas": 0
   }                         
 }
}'
{"acknowledged":true,"shards_acknowledged":true,"index":"index5"}
```

![image-20250121133712189](../markdown_img/image-20250121133712189.png)

```bash
# 关闭es-node2，会造成index5的数据缺失，从而导致集群变为红色
[root@es-node2 ~]# systemctl stop elasticsearch.service 

# 查看健康性为红色
[root@mystical /es/log]# curl 127.0.0.1:9200/_cat/health?
1737437941 05:39:01 my-es1 red 2 2 15 10 0 0 7 0 - 68.2%
```

![image-20250121133936563](../markdown_img/image-20250121133936563.png)

```bash
# 启动es-node2
[root@es-node2 ~]# systemctl start elasticsearch.service

# 恢复es-node2后，查看索引信息
[root@es-node1 /es/log]# curl 127.0.0.1:9200/_cat/indices?
green open index3 VxDJ3o-JSSmHl4y3frw1eA 3 2 0 0 2.1kb 747b 747b
green open index4 oR__XrUQRf6TuNCHHlj6_g 3 1 0 0 1.4kb 747b 747b
green open index5 00PabrwhTcqyNLtB5xsy5A 3 0 0 0  747b 747b 747b
green open index1 _uA6DC1BTy2gZdJPip6sGw 1 1 0 0  498b 249b 249b
green open index2 ThbaBIClSUazA8YQ33WqPQ 1 1 0 0  498b 249b 249b

# 可以在对应节点上看到这些目录
[root@es-node1 /es/data/indices]# ls
00PabrwhTcqyNLtB5xsy5A  oR__XrUQRf6TuNCHHlj6_g  ThbaBIClSUazA8YQ33WqPQ  _uA6DC1BTy2gZdJPip6sGw  VxDJ3o-JSSmHl4y3frw1eA

[root@es-node2 ~]# ls /es/data/indices/
00PabrwhTcqyNLtB5xsy5A  oR__XrUQRf6TuNCHHlj6_g  _uA6DC1BTy2gZdJPip6sGw  VxDJ3o-JSSmHl4y3frw1eA

[root@es-node3 ~]# ls /es/data/indices/
00PabrwhTcqyNLtB5xsy5A  oR__XrUQRf6TuNCHHlj6_g  ThbaBIClSUazA8YQ33WqPQ  VxDJ3o-JSSmHl4y3frw1eA

#可以根据浏览器的图像界面进行对照，es-node2上没有index2, es-node3上没有index1
# 查看VxDJ3o-JSSmHl4y3frw1eA目录，即index3,即可看到3个副本目录
[root@es-node2 ~]# ls /es/data/indices/VxDJ3o-JSSmHl4y3frw1eA/
0  1  2  _state
```

![image-20250121134718614](../markdown_img/image-20250121134718614.png)



#### 插入文档

```bash
#创建文档时不指定_id，会自动生成
#8.X版本后因为删除了type,所以索引操作：{index}/{type}/需要修改成PUT {index}/_doc/
#8.X版本之后
[root@mystical ~]# curl -XPOST http://127.0.0.1:9200/index1/_doc/ -H 'Content-Type: application/json' -d '{"name":"linux", "author": "wangxiaochun", "version": "1.0"}' 
{"_index":"index1","_id":"59Jsh5QBml4tClBPtQsJ","_version":1,"result":"created","_shards":{"total":2,"successful":2,"failed":0},"_seq_no":0,"_primary_term":2}

# 浏览器图形界面，可以看到刚才插入的数据，每个插入的文档都会随机分片一个编号，即id
```

![image-20250121135527505](../markdown_img/image-20250121135527505.png)

```bash
# 指定编号，插入文档（通常是系统分配）
[root@mystical ~]# 
[root@mystical ~]# curl -XPOST 'http://127.0.0.1:9200/index1/_doc/3?pretty' -H 'Content-Type: application/json' -d '{"name":"golang", "author": "zhang", "version": "1.0"}' 
{
  "_index" : "index1",
  "_id" : "3",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 2
}

# 查看浏览器，id为自己指定的3
```

![image-20250121135942316](../markdown_img/image-20250121135942316.png)



#### 查询文档

```bash
#查询索引的中所有文档
[root@mystical ~]# curl 'http://127.0.0.1:9200/index1/_search?pretty'
{
  "took" : 2,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "index1",
        "_id" : "59Jsh5QBml4tClBPtQsJ",
        "_score" : 1.0,
        "_source" : {
          "name" : "linux",
          "author" : "wangxiaochun",
          "version" : "1.0"
        }
      },
      {
        "_index" : "index1",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "golang",
          "author" : "zhang",
          "version" : "1.0"
        }
      }
    ]
  }
}

# 指定ID查询
#7.X版: curl -XGET ‘http://127.0.0.1:9200/{index}/{type}/{id}’
#8.X版: curl -XGET ‘http://127.0.0.1:9200/{index}/_/{id}’

#旧版本
[root@node1 ~]# curl 'http://127.0.0.1:9200/index1/book/3?pretty'

#新版本
[root@node1 ~]# curl 'http://127.0.0.1:9200/index1/_doc/3?pretty'
[root@mystical ~]# curl 'http://127.0.0.1:9200/index1/_doc/3?pretty'
{
  "_index" : "index1",
  "_id" : "3",
  "_version" : 1,
  "_seq_no" : 1,
  "_primary_term" : 2,
  "found" : true,
  "_source" : {
    "name" : "golang",
    "author" : "zhang",
    "version" : "1.0"
  }
}
```



#### 更新文档

```bash
#8.X
# 将index1的id为3的文档里的version: 1.0改为version: 2.0
[root@node1 ~]# curl -XPOST 'http://127.0.0.1:9200/index1/_doc/3' -H 'Content-Type: application/json' -d '{"version": "2.0","name":"golang","author": "zhang"}' 

# 查看
[root@mystical ~]# curl 'http://127.0.0.1:9200/index1/_doc/3?pretty'
{
  "_index" : "index1",
  "_id" : "3",
  "_version" : 2,
  "_seq_no" : 2,
  "_primary_term" : 2,
  "found" : true,
  "_source" : {
    "version" : "2.0",
    "name" : "golang",
    "author" : "zhang"
  }
}

# 7.X
[root@node1 ~]# curl -XPOST 'http://127.0.0.1:9200/index1/book/3' -H 'Content-Type: application/json' -d '{"version": "2.0","name":"golang","author": "zhang"}' 
```



#### 删除文档

```bash
#8.X版本
curl -XDELETE http://kibana服务器:9200/<索引名称>/_doc/<文档id>
#7.X版本前
curl -XDELETE http://kibana服务器:9200/<索引名称>/type/<文档id>
```

**范例：删除指定文档**

```bash
#8.X
[root@mystical ~]# curl -XDELETE 'http://127.0.0.1:9200/index1/_doc/3'
{"_index":"index1","_id":"3","_version":3,"result":"deleted","_shards":{"total":2,"successful":2,"failed":0},"_seq_no":3,"_primary_term":2}

# 确认已删除
[root@mystical ~]# curl 'http://127.0.0.1:9200/index1/_doc/3?pretty'
{
  "_index" : "index1",
  "_id" : "3",
  "found" : false
}

#7.X版本前
[root@node1 ~]#curl -XDELETE 'http://127.0.0.1:9200/index1/book/i8Q5TXsB1gLtFVg7vodl'
```



#### 删除索引

**范例：删除指定索引**

```bash
[root@mystical ~]# curl -XDELETE http://127.0.0.1:9200/index2
{"acknowledged":true}

#查看索引是否删除
[root@mystical ~]# curl 'http://127.0.0.1:9200/_cat/indices?pretty'
green open index3 VxDJ3o-JSSmHl4y3frw1eA 3 2 0 0  2.1kb 747b 747b
green open index4 oR__XrUQRf6TuNCHHlj6_g 3 1 0 0  1.4kb 747b 747b
green open index5 00PabrwhTcqyNLtB5xsy5A 3 0 0 0   747b 747b 747b
green open index1 _uA6DC1BTy2gZdJPip6sGw 1 1 1 1 24.3kb 15kb 15kb

#删除多个指定索引
curl -XDELETE 'http://127.0.0.1:9200/index_one,index_two

#删除通配符多个索引,需要设置action.destructive_requires_name: false
curl -XDELETE 'http://127.0.0.1:9200/index_*'
```

**范例：删除所有索引**

```bash
# 在集群所有节点上设置action.destructive_requires_name: false
[root@es-node1 ~]# vim /etc/elasticsearch/elasticsearch.yml
#最后加一行
#----------------------- END SECURITY AUTO CONFIGURATION ------------------------
-
action.destructive_requires_name: false

# 服务重启
[root@es-node1 ~]# systemctl restart elasticsearch

# 删除
[root@es-node1 ~]#curl -X DELETE "http://127.0.0.1:9200/*"

# 也可以不开启action.destructive_requires_name，使用循环进行批量删除
[root@es-node1 ~]# for i in `curl 'http://127.0.0.1:9200/_cat/indices?v'|awk 
'{print $3}'`;do curl -XDELETE http://127.0.0.1:9200/$i;done
```





## ELasticsearch集群工作原理

**官方说明**

```http
https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
```

单机节点 ES 存在单点可用性和性能问题,可以实现Elasticsearch多机的集群解决

Elasticsearch 支持集群模式

- 能够提高Elasticsearch可用性，即使部分节点停止服务，整个集群依然可以正常服务
- 能够增大Elasticsearch的性能和容量，如内存、磁盘，使得Elasticsearch集群可以支持PB级的数据



### ES 节点分类

Elasticsearch 集群的每个节点的角色有所不同,但都会保存集群状态Cluster State的相关的数据信息

- **节点信息**：每个节点名称和地址
- **索引信息**：所有索引的名称，配置等



**ES的节点有下面几种**

- **Master节点**

  - ES集群中只有一个 Master 节点，用于**控制**和**管理**整个集群的操作
  - Master 节点负责**增删索引**,**增删节点**,**分片shard的重新分配**
  - Master 主要维护**Cluster State**，包括节点名称,节点连接地址,索引名称和配置信息等
  - Master 接受集群状态的变化并推送给所有其它节点,集群中各节点都有一份完整的集群状态信息， 都由master node负责维护
  - Master 节点**不需要**涉及到**文档级别**的变更和搜索等操作
  - 协调创建索引请求或查询请求，将请求分发到相关的node上。
  - 当Cluster State有新数据产生后， Master 会将数据同步给其他 Node 节点
  - Master节点通过超过一半的节点投票选举产生的
  - 可以设置node.master: true 指定为是否参与Master节点选举, 默认true 

  ```ABAP
  指定node.master: false，可以让指定节点不参与选举，即不成为master节点
  ```

  

- **Data节点**
  - 存储数据的节点即为 data 节点
  - 当创建索引后，索引的数据会存储至某个数据节点
  - Data 节点消耗内存和磁盘IO的性能比较大
  - 配置node.data: true, 就是Data节点，默认为 true,**即默认所有节点都是 Data 节点类型**



- **Coordinating 节点(协调)**
  - 处理请求的节点即为 coordinating 节点，该节点类型为所有节点的默认角色，不能取消coordinating 节点主要将请求路由到正确的节点处理。比如创建索引的请求会由 coordinating 路由到 master 节点处理
  - 当配置 node.master:false、node.data:false 则只充当 Coordinating 节点
  - Coordinating 节点在 Cerebro 等插件中数据页面不会显示出来



- **Master-eligible 初始化时有资格选举Master的节点**
  - 集群初始化时有权利参于选举Master角色的节点
  - 只在集群第一次初始化时进行设置有效，后续配置无效
  - 由 cluster.initial_master_nodes 配置节点地址

```ABAP
node.master: true；                   指集群创建成功后，后续出现选举的话，谁有资格参与选举
cluster.initial_master_nodes: true    指初始化的时候，即第一次谁有资格参与选举，后续配置无效
```



### ES集群选举

ES集群的选举是由master-eligble（有资格充当的master节点）发起

当该节点发现当前节点不是master，并且该节点通过ZenDiscovery模块ping其他节点，如果发现超过 **mininum_master_nodes**个节点无法连接master时，就会发起新的选举

```ABAP
注意: 从 Elasticsearch 7.0 开始，minimum_master_nodes 被移除了，Elasticsearch 使用自动化机制来管理主节点的选举，不再需要手动设置此参数。
```

选举时,优先选举**ClusterStateVersion**最大的Node节点，如果ClusterStateVersion相同，则选举**Node  ID**最小的Node

```bash
# 查看ClusterStateVersion
[root@mystical ~]# curl -XGET "http://10.0.0.150:9200/_cluster/state/version?pretty"
{
  "cluster_name" : "my-es1",
  "cluster_uuid" : "sOJhWcLfRp6nqAJHZDsUBA",
  "version" : 221,                              # 221就是集群版本号
  "state_uuid" : "yVLaTIFxT5Wg_vbDsqD1lQ"
}
# lusterStateVersion 是集群状态的版本号，每当集群状态发生变更时（例如节点加入、索引创建、分片重新分配等），版本号都会递增。因此，这个版本号越大，说明是越早加入集群的，里面的数据越多


# 查看Node ID，id即为node id
[root@mystical ~]# curl -XGET "http://10.0.0.150:9200/_cat/nodes?v&h=ip,name,id"
ip         name     id
10.0.0.152 es-node3 zo37jquZSimiJTu7kCMjmA
10.0.0.151 es-node2 PxUqjPNwTaGnkHtpb-CFXQ
10.0.0.150 es-node1 0el3duwhQs6Ry1WsA-Xafg

# 查看Node ID，方法2
[root@mystical ~]# curl -XGET "http://10.0.0.150:9200/_cluster/state?pretty"|grep node_id|grep -Po "/".*/" : /".*/""
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 3459k    0 3459k    0     0  59.0M      0 --:--:-- --:--:-- --:--:-- 59.2M
"node_id" : "zo37jquZSimiJTu7kCMjmA"
"node_id" : "PxUqjPNwTaGnkHtpb-CFXQ"
"node_id" : "0el3duwhQs6Ry1WsA-Xafg"
"node_id" : "0el3duwhQs6Ry1WsA-Xafg"
"node_id" : "PxUqjPNwTaGnkHtpb-CFXQ"
"node_id" : "zo37jquZSimiJTu7kCMjmA"
```

**ClusterStateVersion**是集群的状态版本号，每一次集群选举ClusterStateVersion都会更新，因此最大的 ClusterStateVersion是与原有集群数据最接近或者是相同的，这样就尽可能的避免数据丢失。

**Node的ID**是在第一次服务启动时随机生成的，直接选用最小ID的Node，主要是为了选举的稳定性，尽量少出现选举不出来的问题。

**每个集群中只有一个Master节点**

```ABAP
每个集群中损坏的节点不能超过集群一半以上,否则集群将无法提供服务
```





### ES 集群 Shard 和 Replication

####  分片 Shard

ES 中存储的数据可能会很大,有时会达到PB级别，单节点的容量和性能可以无法满足

基于容量和性能等原因,可以将一个索引数据分割成多个小的分片

再将每个分片分布至不同的节点,从而实现数据的分布存储,实现性能和容量的水平扩展

在读取时,可以实现多节点的并行读取,提升性能

除此之外,如果一个分片的主机宕机,也不影响其它节点分片的读取

横向扩展即增加服务器，当有新的Node节点加入到集群中时，集群会动态的重新进行均匀分配和负载

```ABAP
例如原来有两个Node节点，每个节点上有3个分片，即共6个分片,如果再添加一个node节点到集群中，
集群会动态的将此6个分片分配到这三个节点上，最终每个节点上有2个分片。
```



#### 副本 Replication

将一个索引分成多个数据分片,仍然存在数据的单点问题,可以对每一个分片进行复制生成副本,即备份,实现数据的高可用

ES的分片分为主分片（primary shard）和副本分片（复制replica shard），而且通常分布在不同节点 

**主分片实现数据读写,副本分片只支持读**

在索引中的每个分片只有一个主分片,而对应的副本分片可以有多个,一个副本本质上就是一个主分片的备份

每个分片的主分片在创建索引时自动指定且后续不能人为更改



#### 默认分片配置

默认情况下，elasticsearch将分片相关的配置从配置文件中的属性移除了，可以借助于一个默认的模板接口将索引的分片属性更改成我们想要的分片效果

```bash
# 默认5分片和1副本
[root@mystical ~]# curl -XPUT 'http://127.0.0.1:9200/_template/template_http_request_record' -H 'Content-Type: application/json' -d '{"index_patterns": ["*"],"settings": {"number_of_shards": 5,"number_of_replicas": 1}}'

{"acknowledged":true}

#属性解析：
接口地址：_template/template_http_request_record
索引类型：index_patterns
分片数量：number_of_shards
副本数量：number_of_replicas
```





#### 数据同步机制

Elasticsearch主要依赖 **Zen Discovery 协议**来管理集群中节点的加入和离开，以及选举主节点（master  node）。

Zen Discovery是Elasticsearch自带的一个协议，不依赖于任何外部服务。

然而，Elasticsearch对于一致性的处理与传统的一致性协议（如Raft或Paxos）有所不同。它采取了一 种“**最终一致性**”（eventual consistency）的模型。

每个索引在Elasticsearch中被分成多个分片（shard），每个分片都有一个主分片和零个或多个副本分片。

主分片负责处理所有的写操作，并将写操作复制到其副本分片。当主分片失败时，一个副本分片会被提升为新的主分片。

Elasticsearch为了提高写操作的性能，允许在主分片写入数据后立即确认写操作，而不需要等待数据被所有副本分片确认写入。这就意味着，在某些情况下，主分片可能会确认写操作成功，而实际上副本分片还没有完全写入数据。这就可能导致数据在短时间内在主分片和副本分片之间不一致。然而，一旦所 有副本分片都确认写入了数据，那么系统就会达到“最终一致性”。

为了保证搜索的准确性，Elasticsearch还引入了一个**"refresh"机制**，每隔一定时间（默认为1秒）将最新的数据加载到内存中，使其可以被搜索到。这个过程是在主分片和所有副本分片上独立进行的，所以可能存在在短时间内搜索结果在不同分片之间有些许不一致的情况，但随着时间的推移，所有分片上的数据都会达到一致状态。

综上所述，Elasticsearch通过Zen Discovery协议管理节点和选举，通过主分片和副本分片的机制保证数 据的最终一致性，并通过"refresh"机制保证数据的搜索准确性。



### 集群故障转移

故障转移指的是，当集群中有节点发生故障时，ES集群会进行自动修复

![image-20250121175601325](../markdown_img/image-20250121175601325.png)

如上图，假设由3个节点的ES集群组成,有一个索引index_mystical，三个主分片，三个副本分片，如果其中一个节点宕机

**ES集群的故障转移流程如下**

- **重新选举**
  - 假设当前Master节点 node3 节点宕机,同时也导致 node3 的原有的P1和R2分片丢失
  - node1 和 node2 发现 Master节点 node3 无法响应
  - 过一段时间后会重新发起 master 选举
  - 比如这次选择 node2 为 新 master 节点；此时集群状态变为yellow 状态
  - 其实无论选举出的新Master节点是哪个节点，都不影响后续的分片的重新分布结果

![image-20250121175830942](../markdown_img/image-20250121175830942.png)

- **主分片调整**
  - 新的Master节点 node2 发现在原来在node3上的主分片 P1 丢失
  - 将 node1 上的 R1 提升为主分片
  - 此时所有的主分片都正常分配，但1和2分片没有副本分片
  - 集群状态变为 Yellow状态
- **副本分片调整**
  - node1 将 P1 和 node2上的P2 主分片重新生成新的副本分片 R1、R2，此时集群状态变为 Green

![image-20250121175932581](../markdown_img/image-20250121175932581.png)

- 后续修复好node3节点后，Master 不会重新选举，但会自动将各个分片重新均匀分配
  - 保证主分片尽可能分布在每个节点上
  - 副本分片也尽可能分布不同的节点上
  - 重新分配的过程需要一段时间才能完成

![image-20250121180438208](../markdown_img/image-20250121180438208.png)

```ABAP
一定是主分片将数据复制给副本分片，所以没有主分片的数据，要现将副本分片提升为主分片
```



### ES文档路由

#### ES 文档路由原理

ES文档是分布式存储，当在ES集群访问或存储一个文档时，由下面的算法决定此**文档到底存放在哪个主分片中**,再结合**集群状态**找到存放此主分片的节点主机

```bash
shard = hash(routing) % number_of_primary_shards
hash                     #哈希算法可以保证将数据均匀分散在分片中
routing                  #用于指定用于hash计算的一个可变参数，默认是文档id，也可以自定义
number_of_primary_shards #主分片数
#注意：该算法与主分片数相关，一旦确定后便不能更改主分片，因为主分片数的变化会导致所有分片需要重新分配

```

```ABAP
先根据哈希/主分片数计算出要存放到几号分片中，存放到主分片后，再将数据复制到副本分片中
```



![image-20250121181107339](../markdown_img/image-20250121181107339.png)

可以发送请求到集群中的任一节点。每个节点都知道集群中任一文档位置， 每个节点都有能力接收请求, 再接将请求转发到真正存储数据的节点上



#### ES 文档创建删除流程

![image-20250121181541492](../markdown_img/image-20250121181541492.png)

- 客户端向集群中某个节点 Node1 发送**新建索引文档**或者**删除索引文档**请求
- Node1节点使用文档的 _id 通过上面的算法确定文档属于分片 0 
- 因为分片 0 的主分片目前被分配在 Node3 上,请求会被转发到 Node3
- Node3 在主分片上面执行创建或删除请求
- Node3 执行如果成功，它将请求并行转发到 Node1 和 Node2 的副本分片上
- Node3 将向协调节点Node1 报告成功
- 协调节点Node1 客户端报告成功。



#### **ES 文档读取流程**

可以从主分片或者从其它任意副本分片读取文档 ，读取流程如下图所示 ：

![image-20250121181827402](../markdown_img/image-20250121181827402.png)

- 客户端向集群中某个节点 Node1 发送读取请求
- 节点使用文档的 _id 来确定文档属于分片 0 。分片 0 的主副本分片存在于所有的三个节点上
- 在处理读取请求时，协调节点在每次请求的时候都会通过轮询所有的主副本分片来达到负载均衡， 此次它将请求转发到 Node2 
- Node2 将文档返回给 Node1 ，然后将文档返回给客户端



## Elasticsearch 集群扩容和缩容

### 集群扩容

新加入两个节点node4和node5，变为Data节点

·在两个新节点安装 ES，并配置文件如下

```bash
[root@mystical ~]# vim /usr/local/elasticsearch/config/elasticsearch.yml
cluster.name: ELK-Cluster #和原集群名称相同

#当前节点在集群内的节点名称，同一集群中每个节点要确保此名称唯一
node.name: es-node4  #第二个新节点为es-node5

#集群监听端口对应的IP，默认是127.0.0.1:9300
network.host: 0.0.0.0

#指定任意集群节点即可
discovery.seed_hosts: ["10.0.0.150","10.0.0.151","10.0.0.152"]

#集群初始化时指定希望哪些节点可以被选举为 master,只在初始化时使用,新加节点到已有集群时此项可不配置
#cluster.initial_master_nodes: ["10.0.0.101","10.0.0.102","10.0.0.103"]
#cluster.initial_master_nodes: ["ubuntu2204.wang.org"] 


# 以下配置（选配）
# ELasticsearch8.x开始，使用新方式直接节点角色
# 如果是master节点
node.roles: [master]

# 如果是Data节点
node.roles: [data]

# 如果节点同时是 Master 和 Data 节点：
node.roles: [master, data]

# 如果节点是 Coordinating-only 节点（不存储数据也不当选主节点，仅用于查询分发）
#如果改为路由节点，需要先执行/usr/share/elasticsearch/bin/elasticsearch-node repurpose 清理数据
node.roles: []

# ELasticsearch7.x
#如果不参与主节点选举设为false,默认值为true
node.master: false

#存储数据,默认值为true,此值为false则不存储数据而成为一个路由节点
#如果将原有的true改为false,需要先执行/usr/share/elasticsearch/bin/elasticsearch-node repurpose 清理数据

node.data: true

# 注意jvm优化和内核参数调整
vm.max_map_count = 262144
fs.file-max = 1000000

# 没问题的话重启服务
[root@mystical /es/log]# systemctl restart elasticsearch.service
```

![image-20250121203409221](../markdown_img/image-20250121203409221.png)



### 集群缩容

从集群中删除两个节点node4和node5，在两个节点按一定的顺序逐个停止服务，即可自动退出集群

注意：停止服务前，要观察索引的情况，按一定顺序关机，防止数据丢失

```ABAP
就是要注意：同一个节点上，不能有相同的分片
停服务的时候，要注意保证先把该节点上独有的分片，复制到其他集群节点上后，在删除该节点
```

```bash
[root@mystical /es/log]# systemctl stop elasticsearch.service
```

![image-20250121204518014](../markdown_img/image-20250121204518014.png)

```ABAP
以上述图片为例，绝不能同时通知node3和node5，否则就会出现分片1丢失的问题，如果确定要将node3和node5移出集群
要先将node5移出，等待分片1，备份到es-node1后，再移出node3
```



## ElasticSearch应用



### 创建、查询、删除索引

这里我们可以使用Kibana的开发工具对Elasticsearch进行操作，选择“DevTools”开发工具：

![image-20250506110317866](../markdown_img/image-20250506110317866.png)

![image-20250506110358258](../markdown_img/image-20250506110358258.png)



#### 创建索引

![image-20250506111325697](../markdown_img/image-20250506111325697.png)

```http
PUT /kubernetes
{
  "settings": {
    "index": {
      "number_of_shards": "2",
      "number_of_replicas": "0"
    }
  }
}
```

![image-20250506111411157](../markdown_img/image-20250506111411157.png)

查看Cerebro,可以都看到刚才创建的索引

![image-20250506111529328](../markdown_img/image-20250506111529328.png)

**创建带副本的索引**

```http
PUT /nat
{
  "settings": {
    "index": {
      "number_of_shards": "4",
      "number_of_replicas": "1"
    }
  }
}
```

![image-20250506111856591](../markdown_img/image-20250506111856591.png)

#### 查询索引

```http
GET /_cat/indices
```

![image-20250506112445291](../markdown_img/image-20250506112445291.png)

#### 删除索引

```http
DELETE /nat
```

![image-20250506112756466](D:\git_repository\cyber_security_learning\markdown_img\image-20250506112756466.png)



### 插入数据

```http
URL规则：POST /{索引}/{类型}/{id}
```

插入数据（指定id）

```http
POST /kubernetes/user/1
{
  "id": 1,
  "name": "mystical",
  "age": 20,
  "sex": "male"
}
```

![image-20250506133639103](../markdown_img/image-20250506133639103.png)

插入数据（不指定id）

```http
POST /kubernetes/user
{
  "id": 2,
  "name": "kobe",
  "age": 32,
  "sex": "male"
}
```

![image-20250506134431505](../markdown_img/image-20250506134431505.png)



### 查询数据

#### **查询全部数据**

```http
GET /kubernetes/user/_search
```

![image-20250506134753923](../markdown_img/image-20250506134753923.png)



#### 根据id指定查询

```http
GET /kubernetes/user/1
```

![image-20250506135013924](../markdown_img/image-20250506135013924.png)



#### 根据关键字查询数据

```http
GET /kubernetes/user/_search?q=name:kobe
```

![image-20250506135312947](../markdown_img/image-20250506135312947.png)



### 更新数据

在Elasticsearch中，文档数据是不可修改的，但是可以通过覆盖的方式进行更新

更新一条数据的所有信息

```http
PUT /kubernetes/user/1
{
  "id":1,
  "name":"susan",
  "age":24,,
  "sex":"female"
}
```

![image-20250506135825945](../markdown_img/image-20250506135825945.png)

可以看到数据已经被覆盖了。问题来了，可以局部更新吗？可以的，前面不是说，文档数据不能更新吗？其实是这样的：在内部，依然会查询到这个文档数据，然后进行覆盖操作，步骤如下：

- 从旧文档中检索JSON
- 修改它
- 删除就旧文档
- 索引新文档



#### 局部更新

```http
POST /kubernetes/user/1/_update
{
  "doc":{
    "age":33
  }
}
```

![image-20250506140507255](../markdown_img/image-20250506140507255.png)



### 删除数据

在Elasticsearch中，删除文档数据，只需要发起DELETE请求即可，不用额外的参数

**删除一条存在的数据**

```http
DELETE /kubernetes/user/1
```

![image-20250506141031657](../markdown_img/image-20250506141031657.png)



### DSL搜索

Elasticsearch提供丰富且灵活的查询语句叫DSL查询（Query DSL），它允许你构建更加复杂，强大的查询。DSL以JSON请求的形式出现



#### **示例1：查询名字是kobe的用户**

```http
POST /kubernetes/user/_search
{
  "query":{
    "match":{   # match精确匹配，只是查询的一种
      "name":"kobe"
    }
  }
}
```

![image-20250506142417995](../markdown_img/image-20250506142417995.png)



#### **示例2：查询年龄大于30岁的男性用户**

```http
生成数据,当索引不存在的时候，创建数据的时候会自动创建索引
POST /test/user/1
{
  "id":1,
  "name":"curry",
  "age":37,
  "sex":"male"
}

POST /test/user/2
{
  "id":2,
  "name":"susan",
  "age":26,
  "sex":"female"
}

POST /test/user/3
{
  "id":3,
  "name":"kobe",
  "age":22,
  "sex":"male"
}
```

![image-20250506143221752](../markdown_img/image-20250506143221752.png)

**查询**

```http
POST /test/user/_search
{
  "query":{
    "bool":{
      "filter":{
        "range":{
          "age":{
            "gt":30
          }
        }
      },
      "must":{
        "match":{
          "sex":"male"
        }
      }
    }
  }
}
```

![image-20250506143922574](../markdown_img/image-20250506143922574.png)

##### 补充：`filter` 和 `must` 都是`bool`查询（`bool query`）的一部分，用于组合多个查询条件，但它们的行为和用途有明显区别

**`must`**

- **语义**：必须匹配（相当于逻辑 AND）。
- **作用**：文档必须匹配 `must` 中的所有子查询，才能被返回。
- **评分**：`must` 参与文档的**相关性评分（_score）**，即文档匹配得好坏会影响其得分排序。

**`filter`**

- **语义**：过滤匹配。
- **作用**：文档必须满足 `filter` 条件才能被返回。
- **评分**：`filter` **不参与评分**，只是一个纯过滤器，适合用在不需要打分的场景（比如范围过滤、精确值过滤）。
- **性能**：因为不打分，**性能更好**，会被 Elasticsearch 缓存优化。



**何时用 `filter`？何时用 `must`？**

| 场景                       | 用 `must` | 用 `filter` |
| -------------------------- | --------- | ----------- |
| 需要全文搜索、相关性排序   | ✅ 是      | ❌ 否        |
| 精确值匹配（状态、标签等） | ❌ 否      | ✅ 是        |
| 范围查询（时间、年龄等）   | ❌ 否      | ✅ 是        |
| 影响结果排序               | ✅ 是      | ❌ 否        |
| 想要缓存以加快性能         | ❌ 否      | ✅ 是        |



**打分的含义**

在 Elasticsearch 中，“打分”是指对每个**匹配的文档**根据其**与查询条件的相关性**进行评分，称为 `_score`。这个评分决定了**搜索结果的排序顺序**，更相关的文档会排在更前面。



**为什么要打分？**

打分的目的是为了：

- **排序搜索结果**：让更“相关”的内容排在前面。
- **体现匹配程度**：不是简单的“是否匹配”，而是“匹配得有多好”。

**举例说明**

假设你搜索

```json
{
  "query": {
    "match": {
      "message": "error"
    }
  }
}
```

如果有两个文档：

- 文档 A：`"message": "critical error occurred while processing"`
- 文档 B：`"message": "everything is fine, no issue"`

虽然两个都包含了关键词 "error"，但**文档 A 更相关**，它的 `_score` 会更高，因此它排在前面。

**`_score` 在哪里体现？**

在查询结果中，每个文档会带一个 `_score` 字段，例如：

```json
{
  "_index": "log",
  "_id": "1",
  "_score": 2.354,
  "_source": {
    "message": "critical error occurred"
  }
}
```

**什么时候不需要打分？**

不需要打分的场景一般是：

- 过滤（`filter`）：
  - 比如 `status = "active"`、`age > 18` 这类查询只是决定**是否符合条件**，不需要参与排序。
  - 使用 `filter` 会提升性能，因为 Elasticsearch 可以**跳过打分计算**并启用缓存。



#### 示例3：过滤name为kobe和curry的数据

```http
POST /test/user/_search
{
  "query":{
    "match":{
      "name": "kobe curry"
    }
  }
}
```

![image-20250506145354026](../markdown_img/image-20250506145354026.png)



## Elasticsearch核心概念

### 文档

在Elasticsearch中，文档以JSON格式存储，可以是复杂的结构，如

```http
# 查看文档
GET /test/_doc/1
{
  "_index":"test",
  "_type":"_doc",
  "_id":"1",
  "_version":1,
  "_seq_no":0,
  "primary_term":1,
  "found":true
  "_source":{
    "id":1,
    "name":"curry",
    "age":37,
    "sex":"male"
  }
}
```

一个文档不只有数据。它还包含了元数据（metadata）。三个必须得元数据节点是

- `_index`: 文档存储的地方
- `_type`：文档代表的对象的类
- `_id`：文档的唯一标识



### 查询响应

在响应的数据中，如果我们不需要全部的字段，可以指定某些需要的字段进行返回。通过添加`_source`实现。

```http
GET /test/user/1?_source=id,name
```

![image-20250506151541090](../markdown_img/image-20250506151541090.png)

如不需要返回元数据，仅仅返回原始数据，可以这样：

```http
GET /test/user/1/_source
```

![image-20250506151759982](../markdown_img/image-20250506151759982.png)

如果不需要返回元数据，还想获取指定字段的数据时，可以这样：

```http
GET /test/user/1/_source?_source=id,name
```

![image-20250506152041242](../markdown_img/image-20250506152041242.png)



### 判断文档是否存在

如果我们需要判断文档是否存在，而不是查询文档内容，那么可以执行如下操作

```http
HEAD /test/user/1
```

![image-20250506152314474](../markdown_img/image-20250506152314474.png)

当文档不存在时判断：

![image-20250506152458350](../markdown_img/image-20250506152458350.png)



### 批量操作

在某些情况下可以通过批量操作减少网络请求。如：批量查询，批量插入数据

**批量查询**

```http
POST /test/user/_mget
{
  "ids": ["1","2"]
}
```

![image-20250506152754895](../markdown_img/image-20250506152754895.png)

如果某一条数据不存在，不影响整体响应，需要通过found的值进行判断是否查询到数据。如果found值为false则表示该数据不存在

```http
POST /test/user/_mget
{
  "ids":["10","2"]
}
```

![image-20250506154149265](../markdown_img/image-20250506154149265.png)



**`_bulk`操作**

在Elasticsearch中，支持批量插入，修改，删除操作，都是通过`_bulk`的**api**完成的

请求格式如下

```http
{ action: { metadata }}
{ request body }
{ action: { metadata }}
{ request body }
......
```

**批量插入数据**

```http
POST /test/user/_bulk
{"create":{"_index":"test","_type":"user","_id":2001}}
{"id":2001,"name","name1","age":20,"sex":"male"}
{"create":{"_index":"test","_type":"user","_id":2002}}
{"id":2002,"name","name2","age":21,"sex":"male"}
{"create":{"_index":"test","_type":"user","_id":2003}}
{"id":2003,"name","name3","age":22,"sex":"male"}
{"create":{"_index":"test","_type":"user","_id":2004}}
{"id":2004,"name","name4","age":23,"sex":"male"}
```

![image-20250506155034674](../markdown_img/image-20250506155034674.png)

**批量删除**

```http
POST /test/user/_bulk?pretty
{"delete":{"_index":"test","_type":"user","_id":2001}}
{"delete":{"_index":"test","_type":"user","_id":2002}}
{"delete":{"_index":"test","_type":"user","_id":2003}}
{"delete":{"_index":"test","_type":"user","_id":2004}}
```

![image-20250506160353212](../markdown_img/image-20250506160353212.png)



### 分页查询

要执行Elasticsearch的分页查询，你需要使用from和size参数来指定结果集的起始位置和数量

- **size: **分页的结果数，默认10
- **from: **跳过开始的结果数，默认0

例如：如果你想每页显示5个结果，那请求如下

```http
GET /_search?size=5
```

**应用案例**

示例1：跳过第1个数据拿第2个数据，一页最多显示5个结果

```http
GET /test/user/_search?size=5&from=1
```

![image-20250506161118808](../markdown_img/image-20250506161118808.png)

示例2：数据分页。每页5条数据，查看第2页数据

```http
GET /test/user/_search
{
  "from":5,
  "size":5,
  "query":{
    "match_all": {}
  }
}
```

在上述示例中，我们指定了从结果集中的第5个文档开始获取5个文档。match_all查询是一个简单的查询类型，它会返回索引中的全部文档



### 映射

前面创建的索引以及插入数据，都是由Elasticsearch进行自动判断类型，有些时候我们是需要进行明确字段类型的，否则，自动判断的类型和实际需要时不相符的

**自动判断的规则如下**

| JSON type                       | Field type  |
| ------------------------------- | ----------- |
| Boolean: `true` or `false`      | "`boolean`" |
| Whole number: 123               | "long"      |
| Floating point: 123.45          | "double"    |
| String valid data: "2014-09-15" | "date"      |
| String: "foo bar"               | "string"    |

上述表格的意思是，如果你输入的是true或者false，就会被定义为"boolean"类型；如果输入的是123，会被定义为"long"类型。......



Elasticsearch中支持的类型如下：字符串类型，数字类型，浮点类型，布尔类型，date类型

| 类型           | 表示的数据类型                  |
| -------------- | ------------------------------- |
| String         | `string`, `text`, `keyword`     |
| Whole number   | `byte`,`short`,`integer`,`long` |
| Floating point | `float`,`double`                |
| Boolean        | `boolean`                       |
| Date           | `date`                          |

- String类型在Elasticsearch旧版本中使用较多，从Elasticsearch5.0开始不再支持String，由`text`和`keyword类型`代替
- **text类型**：text类型用于索引长文本或字符串数据。当你使用text类型时，Elasticsearch会对文本进行分词，并根据分词后的结果建立倒排索引。这使得我们**可以对文本进行全文搜索，找到包含特定词汇的文档**。text类型适合于需要进行全文搜索的字段。在聚合时，text类型会将字段的每个独立词汇作为聚合的独立项
- **keyword类型: **适用于索引结构化的字段，比如email地址，主机名，状态码，标签。如果字段需要进行过滤（比如查找已发布博客中status属性为published的文章）、排序、聚合。keyword类型的字段**只能通过精确值搜索到**



**创建明确类型的索引**

```http
PUT /itcast?include_type_name=true     #itcast是索引名
{
  "settings":{
    "index":{
      "number_of_shards: "2",
      "number_of_replicas: "0"
    }
  }
  "mappings":{
    "person":{
      "properties":{
        "name":{
          "type":"text"
        },
        "age":{
          "type":"integer"
        },
        "mail":{
          "type":"keyword"
        },
        "hobby":{
          "type":"text"
        }
      }
    }
  }
}
```

![image-20250506170243621](../markdown_img/image-20250506170243621.png)

**查询映射**

```http
GET /itcast/_mapping
```

![image-20250506170423476](../markdown_img/image-20250506170423476.png)



### 结构化查询

在Elasticsearch中，可以使用结构化查询来检索和过滤数据。结构化查询的语法是基于Elasticsearch的查询DSL（领域特定语言）的

#### term查询

**term**主要用于精确匹配哪些值，比如数字，日期，布尔值或字符串

```http
{"term":{"age":26}}
{"term":{"date":"2014-09-01"}}
{"term":{"public":true}}
{"term":{"tag":"full_text"}}
```

示例1：精确匹配`age=20`的数据

```http
POST /itcast/person/_search
{
  "query":{
    "term":{
      "age":20
    }
  }
}
```

#### terms查询

terms和term有点类似，但terms允许指定多个匹配条件。如果某个字段指定了多个值，那么文档需要一起去做匹配

```http
{
  "terms":{
    "tag":[
      "search",
      "full_text",
      "nosql"
    ]
  }
}
```

示例

```http
POST /itcast/person/_search
{
  "query": {
    "terms": {
      "age": [
        20,
        21,
        22
      ]
    }
  }
}
```

#### 范围查询

根据范围条件查询指定字段的值。range过滤允许我们按照指定范围查找一批数据

```http
{
  "range":{
    "age":{
      "gte":20,
      "lt":30
    }
  }
}
```

范围操作符包含：

- **gt**：大于
- **gte**：大于等于
- **lt**：小于
- **lte**：小于等于

示例：查询年龄在20~30之间的数据

```http
POST /itcast/person/_search
{
  "query":{
    "range":{
      "age":{
        "gte":20,
        "lte":30
      }
    }
  }
}
```

#### 存在查询

检查指令字段是否存在。`exists`查询可以用于查找文档中是否包含指定字段

示例：查找拥有age字段的数据

```http
POST /itcast/person/_search
{
  "query":{
    "exists":{
      "field":"age"
    }
  }
}
```

#### 匹配查询

根据特定字段匹配查询文档。match查询是一个标准查询，不管你需要全文本查询还是精确查询基本上都用到它

注意：match可以做精确匹配和模糊匹配使用（keyword不支持模糊查询）

示例：匹配查询name中有"张"的数据

```http
POST /itcast/person/_search
{
  "query":{
    "match":{
      "name":"张"
    }
  }
}
```

#### 布尔查询

组合多个查询条件进行复合查询。bool查询可以用来合并多个条件查询结果的布尔逻辑，它包含一些操作符

```bash
must           # 多个查询条件的完全匹配，相当于and
must_not       # 多个查询条件的相反匹配，相当于not
should         # 至少有一个查询条件匹配，相当于or
```

示例1：查找喜欢足球的，不喜欢音乐的

```http
POST /itcast/person/_search
{
  "query":{
    "bool":{
      "must":{
        "match":{
          "hobby":"足球"
        }
      }，
      "must_not":{
        "match":{
          "hobby":"音乐"
        }
      }
    }
  }
}
```





# Beats收集数据

Beats 是一个免费且开放的平台，集合了多种单一用途数据采集器。它们从成百上千或成千上万台机器 和系统向 Logstash 或 Elasticsearch 发送数据

虽然利用 logstash 就可以收集日志，功能强大，但由于 Logtash 是基于Java实现，需要在采集日志的主 机上安装JAVA环境

logstash运行时最少也会需要额外的500M的以上的内存，会消耗比较多的内存和磁盘空间，

可以采有基于Go开发的 Beat 工具代替 Logstash 收集日志，部署更为方便，而且只占用10M左右的内 存空间及更小的磁盘空间。



![image-20250121205310305](../markdown_img/image-20250121205310305.png)

**官方链接**

```http
https://www.elastic.co/cn/beats/
```

**Github 链接**

```http
https://github.com/elastic/beats
```

**下载链接**

```http
https://www.elastic.co/cn/downloads/beats
```



**Beats 是一些工具集,包括以下,其中 filebeat 应用最为广泛**

![image-20250121205605253](../markdown_img/image-20250121205605253.png)

注意: Beats 版本要和 Elasticsearch 相同的版本，否则可能会出错



## 利用Metricbeat监控性能相关指标

Metricbeat 可以收集指标数据，比如系统运行状态、CPU、内存利用率等。

生产中一般用 zabbix 等专门的监控系统实现此功能

官方配置说明

```http
https://www.elastic.co/guide/en/beats/metricbeat/current/configuring-howto-metricbeat.html
```



### 下载 metricbeat 并安装

**下载链接**

```http
https://www.elastic.co/cn/downloads/beats/metricbeat
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/m/metricbeat/
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/7.x/apt/pool/main/m/metricbeat/
```

**创建2个需要被采集日志的主机**

```bash
# 10.0.0.153 -- web01
[root@mystical ~]# hostnamectl set-hostname web01
# 10.0.0.154 -- web02
[root@mystical ~]# hostnamectl set-hostname web02
```

**范例**

```bash
# 下载
[root@web01 ~]# wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/m/metricbeat/metricbeat-8.15.0-amd64.deb

# 安装
[root@web01 ~]# dpkg -i metricbeat-8.15.0-amd64.deb
```



### 修改配置

```bash
[root@web01 ~]# vim /etc/metricbeat/metricbeat.yml
# 可选
#setup.kibana:
#   host: "10.0.0.101:5601" #指向kabana服务器地址和端口，非必须项，即使不设置Kibana也可以通过ES获取Metrics信息

# 必改
# ---------------------------- Elasticsearch Output ----------------------------
output.elasticsearch:
  # Array of hosts to connect to.
  hosts: ["10.0.0.150", "10.0.0.151", "10.0.0.152"]     #指向任意一个ELK集群节点即可
```



### 启动服务

```bash
[root@web01 ~]# systemctl enable --now metricbeat.service
```



### Cerebro插件查看索引

新版`.ds-metricbeat-<时间>-<版本>`

![image-20250121215017651](../markdown_img/image-20250121215017651.png)



### 通过 Kibana 查看收集的性能指标

**8.X版本界面**

![image-20250121215242609](../markdown_img/image-20250121215242609.png)



## 利用 Heartbeat 监控

heartbeat 用来定时探测服务是否正常运行。支持也支持TLS、身份验证和代理

官方heartbeat配置文档

```http
https://www.elastic.co/guide/en/beats/heartbeat/current/configuring-howto-heartbeat.htm
```



### 下载并安装

**下载链接**

```http
https://www.elastic.co/cn/downloads/beats/heartbeat
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/h/heartbeat-elastic/
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/7.x/apt/pool/main/h/heartbeat-elastic/
```

```bash
# 新版8.X
[root@web01 ~]# wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/h/heartbeat-elastic/heartbeat-8.15.0-amd64.deb

# 安装
[root@web01 ~]# dpkg -i heartbeat-8.15.0-amd64.deb

#准备需要监控的服务httpd
[root@web01 ~]# apt -y install apache2
```



### **修改配置**

**官方参考**

```bash
# https://www.elastic.co/guide/en/beats/heartbeat/current/configuration-heartbeat-options.html

# 官方示例 heartbeat.yml
heartbeat.monitors:
- type: icmp
 id: ping-myhost
 name: My Host Ping
 hosts: ["myhost"]
 schedule: '*/5 * * * * * *'  #相当于'@every 5s'; 秒 分 时 日 月 周 年
- type: tcp
 id: myhost-tcp-echo
 name: My Host TCP Echo
 hosts: ["myhost:777"]  # default TCP Echo Protocol
 check.send: "Check"
 check.receive: "Check"
 schedule: '@every 5s'
- type: http
 id: service-status
 name: Service Status
  service.name: my-apm-service-name
 hosts: ["http://localhost:80/service/status"]
 check.response.status: [200] #默认值
 schedule: '@every 5s'
heartbeat.scheduler:
 limit: 10
```

**时间格式: 注意可以支持秒级精度**

```ABAP
https://github.com/gorhill/cronexpr#implementation
Field name     Mandatory?   Allowed values   Allowed special characters
----------     ----------   --------------   --------------------------
Seconds        No           0-59             * / , -
Minutes        Yes          0-59             * / , -
Hours          Yes          0-23             * / , -
Day of month   Yes          1-31             * / , - L W
Month          Yes          1-12 or JAN-DEC  * / , -
Day of week    Yes          0-6 or SUN-SAT   * / , - L #
Year           No           1970–2099        * / , -
```

**范例**

```bash
[root@web01 ~]# vim /etc/heartbeat/heartbeat.yml
# Configure monitors inline
heartbeat.monitors:

# 添加下面5行，用于监控TCP
- type: tcp
  id: myhost-tcp-echo
  name: My Host TCP Echo
  hosts: ["10.0.0.154:80"]  # default TCP Echo Protocol
  schedule: '@every 5s'

# 添加下面5行，用于监控ICMP
- type: icmp
  id: ping-myhost
  name: My Host Ping
  hosts: ["10.0.0.154"]
  schedule: '*/5 * * * * * *'

- type: http
  # Set enabled to true (or delete the following line) to enable this monitor
  enabled: true       # 修改此行false为true
  # ID used to uniquely identify this monitor in Elasticsearch even if the config changes
  id: my-monitor
  # Human readable display name for this service in Uptime UI and elsewhere
  name: My Monitor
  # List of URLs to query
  urls: ["http://10.0.0.154"]
  # Configure task schedule
  schedule: '@every 10s'
  # Total test connection and data exchange timeout
  #timeout: 16s
  # Name of corresponding APM service, if Elastic APM is in use for the monitored service
  
#-------------------------- Elasticsearch output ------------------------------
output.elasticsearch:
  # Array of hosts to connect to.
 hosts: ["10.0.0.151:9200"]  #修改此行，指向ELK集群服务器地址和端口

# ======================= Elasticsearch template setting =======================

setup.template.settings:
  index.number_of_shards: 3         # 修改分片数量，因为集群有3个节点，因此改为3
  index.codec: best_compression
  #_source.enabled: false
```



### 启动服务

```bash
[root@web01 ~]# systemctl start heartbeat-elastic.service
```



### cerebro插件查看索引

![image-20250121222236027](../markdown_img/image-20250121222236027.png)



### 通过 Kibana 查看收集的性能指标

```ABAP
Observability---运行时间---监测 Uptime Monitors
如果没有，可以刷新后在观察
```



![image-20250121222503550](../markdown_img/image-20250121222503550.png)

```bash
# 在被观测节点安装nginx，打开80端口
[root@web02 ~]# apt install -y nginx
```

![image-20250121223146570](../markdown_img/image-20250121223146570.png)





## 利用 Filebeat 收集日志

**Filebeat** 是用于转发和集中日志数据的轻量级传送程序。作为服务器上的代理安装，Filebeat监视您指定的日志文件或位置，收集日志事件，并将它们转发到**Elasticsearch**或**Logstash**进行索引。

Logstash 也可以直接收集日志,但需要安装JDK并且会占用至少 500M 以上的内存

生产一般使用filebeat代替logstash, 基于go开发,部署方便,重要的是只需要10M多内存,比较节约资源.

filebeat 支持从日志文件,Syslog,Redis,Docker,TCP,UDP,标准输入等读取数据,对数据做简单处理，再输出至Elasticsearch,logstash,Redis,Kafka等



**Filebeat的工作方式如下：**

- 启动Filebeat时，它将启动一个或多个输入源，这些输入将在为日志数据指定的位置中查找。
- 对于Filebeat所找到的每个日志，Filebeat都会启动收集器**harvester**进程。
- 每个收集器harvester都读取一个日志以获取新内容，并将新日志数据发送到**libbeat**
- **libbeat**会汇总事件并将汇总的数据发送到为Filebeat配置的输出



**Filebeat 官方说明**

```http
https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-overview.html
https://www.elastic.co/guide/en/beats/filebeat/current/configuring-howto-filebeat.htm
```

![image-20250122091225320](../markdown_img/image-20250122091225320.png)

**输入和输出官方说明**

```http
https://www.elastic.co/guide/en/beats/filebeat/current/configuration-filebeat-options.html
https://www.elastic.co/guide/en/beats/filebeat/current/configuring-output.html
```

**注意: Filebeat 支持多个输入,但不支持同时有多个输出，如果多输出，会报错如下**

```ABAP
Exiting: error unpacking config data: more than one namespace configured 
accessing 'output' (source:'/etc/filebeat/stdout_file.yml')
```



### 安装 Filebeat 和配置说明

**安装说明**

```http
https://www.elastic.co/guide/en/beats/filebeat/current/setup-repositories.html
https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html
https://www.elastic.co/guide/en/beats/filebeat/current/running-on-kubernetes.html
```

**下载链接**

```http
https://www.elastic.co/cn/downloads/beats/filebeat
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/f/filebeat/
```



#### 安装Filebeat

**范例：包安装**

```bash
# 8.X版本下载
[root@web01 ~]# wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/f/filebeat/filebeat-8.15.0-amd64.deb

# 安装
[root@web01 ~]# dpkg -i filebeat-8.15.0-amd64.deb

#默认没有启动
[root@web01 ~]# systemctl enable --now filebeat

#先停止服务,方便后续调试
[root@web01 ~]# systemctl stop filebeat
```





#### Filebeat配置

**配置官方说明**

```http
https://www.elastic.co/guide/en/beats/filebeat/current/configuring-howto-filebeat.html
https://www.elastic.co/guide/en/beats/filebeat/8.3/configuration-general-options.htm
```

**filebeat默认二进制路径**

```bash
[root@web02 ~]# ls /usr/share/filebeat/bin/filebeat
/usr/share/filebeat/bin/filebeat
```





### 从STDIN读取再输出STDOUT

#### 创建配置

范例：解析文本，不能解析json格式文本

```bash
[root@web02 ~/filebeat]# vim stdin.yaml
filebeat.inputs:
- type: stdin
  enabled: true
  #tags: ["stdin-tags","myapp"] #添加新字段名tags，可以用于判断不同类型的输入，实现不同的输出
  fields:
    status_code: "200"  #添加新字段名fields.status_code，可以用于判断不同类型的输入，实现不同的输出
    author: "wangxiaochun"
#output.console:
#  pretty: true
#  enable: true
output.console:
  pretty: true
  enable: true
  
# 语法检查，注意：stdin.yml的相对路径是相对于/etc/filebeat的路径，而不是当前路径
[root@web02 ~/filebeat]# filebeat test config -c /root/filebeat/stdin.yaml 
Config OK
```



#### 执行读取

```bash
#从指定文件中读取配置
#-e 表示Log to stderr and disable syslog/file output
[root@web02 ~/filebeat]# filebeat -e -c /root/filebeat/stdin.yaml

# 实际为了测试，也可以不加-e
[root@web02 ~/filebeat]# filebeat -c /root/filebeat/stdin.yaml
# 在屏幕输入hello
hello, world
{
  "@timestamp": "2025-01-22T01:54:00.288Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "_doc",
    "version": "8.15.0"
  },
  "log": {
    "file": {
      "path": ""
    },
    "offset": 0
  },
  "message": "hello,world",
  "input": {
    "type": "stdin"
  },
  "ecs": {
    "version": "8.0.0"
  },
  "host": {
    "name": "web02"
  },
  "agent": {
    "version": "8.15.0",
    "ephemeral_id": "795036a9-d582-42c1-9d6f-8866fd53a612",
    "id": "d5fc8381-c364-4164-9cd2-75d9b006ad80",
    "name": "web02",
    "type": "filebeat"
  }
}

# 输入json格式数据
{"name" : "wangxiaochun", "age" : "18", "phone" : "0123456789"}
{
  "@timestamp": "2025-01-22T01:55:23.995Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "_doc",
    "version": "8.15.0"
  },
  "message": "{/"name/" : /"wangxiaochun/", /"age/" : /"18/", /"phone/" : /"0123456789/"}", # 没有解析json数据
  "input": {
    "type": "stdin"
  },
  "host": {
    "name": "web02"
  },
  "agent": {
    "name": "web02",
    "type": "filebeat",
    "version": "8.15.0",
    "ephemeral_id": "795036a9-d582-42c1-9d6f-8866fd53a612",
    "id": "d5fc8381-c364-4164-9cd2-75d9b006ad80"
  },
  "ecs": {
    "version": "8.0.0"
  },
  "log": {
    "offset": 0,
    "file": {
      "path": ""
    }
  }
}
```



#### 解析Json格式文本

```bash
[root@web02 /etc/filebeat]# cat test.yaml 
filebeat.inputs:
- type: stdin
  enable: true
  json.keys_under_root: true  # 解析json

output.console:
  pretty: true
  enable: true
  
# 测试
[root@web02 /etc/filebeat]# filebeat -c test.yaml 
# 测试非json数据
hello,world
{
  "@timestamp": "2025-01-22T02:02:54.093Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "_doc",
    "version": "8.15.0"
  },
  "ecs": {
    "version": "8.0.0"
  },
  "host": {
    "name": "web02"
  },
  "agent": {
    "ephemeral_id": "0f302cae-f141-466b-b479-358fd3dd1124",
    "id": "d5fc8381-c364-4164-9cd2-75d9b006ad80",
    "name": "web02",
    "type": "filebeat",
    "version": "8.15.0"
  },
  "message": "hello,world",    # 非json，不解析
  "log": {
    "offset": 0,
    "file": {
      "path": ""
    }
  },
  "json": {},
  "input": {
    "type": "stdin"
  }
}

# 测试json数据
{"name" : "mystical", "age" : "18", "phone" : "0123456789"}
{
  "@timestamp": "2025-01-22T02:03:53.363Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "_doc",
    "version": "8.15.0"
  },
  "age": "18",         # json格式，被解析，并且不会生成message字段
  "input": {
    "type": "stdin"
  },
  "ecs": {
    "version": "8.0.0"
  },
  "host": {
    "name": "web02"
  },
  "agent": {
    "ephemeral_id": "0f302cae-f141-466b-b479-358fd3dd1124",
    "id": "d5fc8381-c364-4164-9cd2-75d9b006ad80",
    "name": "web02",
    "type": "filebeat",
    "version": "8.15.0"
  },
  "log": {
    "offset": 0,
    "file": {
      "path": ""
    }
  },
  "phone": "0123456789",    # json格式，被解析
  "name": "mystical"        # json格式，被解析
}
```



#### 加自定义字段

作用：用于将日志信息分类使用

```bash
[root@web02 /etc/filebeat]# cat test.yaml 
filebeat.inputs:
- type: stdin
  enable: true
  json.keys_under_root: true      # 解析json
  tags: ["stdin-tags", "myapp"]   # 添加新字段名tags，可以用于判断不同类型的输入，实现不同的输出
  fields:
    status_code: "200"            # 添加新字段名fields.status_code，可以用于判断不同类型的输入，实现不同的输出
    author: "mystical"

output.console:
  pretty: true
  enable: true

# 测试
{
  "@timestamp": "2025-01-22T02:11:06.580Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "_doc",
    "version": "8.15.0"
  },
  "log": {
    "offset": 0,
    "file": {
      "path": ""
    }
  },
  "name": "mystical",
  "age": "18",
  "phone": "0123456789",
  "tags": [
    "stdin-tags",
    "myapp"
  ],
  "input": {
    "type": "stdin"
  },
  "fields": {
    "status_code": "200",
    "author": "mystical"
  },
  "ecs": {
    "version": "8.0.0"
  },
  "host": {
    "name": "web02"
  },
  "agent": {
    "ephemeral_id": "5671e9ac-918f-48df-a13a-c034d6175b82",
    "id": "d5fc8381-c364-4164-9cd2-75d9b006ad80",
    "name": "web02",
    "type": "filebeat",
    "version": "8.15.0"
  }
}

```



### 从STDIN读取再输出FILE

#### 创建配置

```bash
[root@web02 ~]# cat /etc/filebeat/stdout_file.yaml 
filebeat.inputs:
- type: stdin
  enable: true
  json.keys_under_root: true

output.file:
  path: "/tmp"
  filename: "filebeat.log"
```



#### 执行读取

```bash
[root@web02 ~]# filebeat -c stdout_file.yaml
#输入如下Json格式信息，再回车后输出如下
{"name" : "mystical", "age" : "18", "phone" : "0123456789"}

# 查看
[root@web02 /tmp]# ls
filebeat.log-20250122.ndjson    # 自动生成

[root@web02 /tmp]# cat filebeat.log-20250122.ndjson |jq
{
  "@timestamp": "2025-01-22T02:20:07.524Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "_doc",
    "version": "8.15.0"
  },
  "age": "18",
  "phone": "0123456789",
  "input": {
    "type": "stdin"
  },
  "host": {
    "name": "web02"
  },
  "agent": {
    "type": "filebeat",
    "version": "8.15.0",
    "ephemeral_id": "eeb00a90-67ca-49df-b1ac-31ea3c781c38",
    "id": "d5fc8381-c364-4164-9cd2-75d9b006ad80",
    "name": "web02"
  },
  "ecs": {
    "version": "8.0.0"
  },
  "log": {
    "file": {
      "path": ""
    },
    "offset": 0
  },
  "name": "mystical"
}
```



### 从FILE读取再输出至STDIN

```http
https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-log.html
```

filebeat 会将每个文件的读取数据的相关信息记录在`/var/lib/filebeat/registry/filebeat/log.json`文件中,可以实现日志采集的持续性,而不会重复采集

- 当日志文件大小发生变化时，filebeat会接着上一次记录的位置继续向下读取新的内容
- 当日志文件大小没有变化，但是内容发生变化，filebeat会将文件的全部内容重新读取一遍



#### 创建配置

```bash
[root@web02 ~]# cat /etc/filebeat/file.yaml  
filebeat.inputs:
- type: log
  enable: true
  json.keys_under_root: true
  paths:
  #- /var/log/syslog
  - /var/log/test.log

output.console:
  pretty: true
  enable: true
```



#### 执行读取

```bash
[root@web02 /var/log]# echo '{"name" : "mystical", "age" : "20", "phone" : "0123456789"}' >> test.log

[root@web02 ~]# filebeat -c file.yaml
{
  "@timestamp": "2025-01-22T02:34:22.273Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "_doc",
    "version": "8.15.0"
  },
  "host": {
    "name": "web02"
  },
  "agent": {
    "name": "web02",
    "type": "filebeat",
    "version": "8.15.0",
    "ephemeral_id": "ad623318-8939-4f9c-887b-8fa18bcf1cf6",
    "id": "d5fc8381-c364-4164-9cd2-75d9b006ad80"
  },
  "name": "mystical",
  "age": "20",
  "phone": "0123456789",
  "log": {
    "offset": 240,
    "file": {
      "path": "/var/log/test.log"
    }
  },
  "input": {
    "type": "log"
  },
  "ecs": {
    "version": "8.0.0"
  }
}

# filebeat 会将每个文件的读取数据的相关信息记录在/var/lib/filebeat/registry/filebeat/log.json文件中,可以实现日志采集的持续性,而不会重复采集
[root@web02 /var/log]# ls /var/lib/filebeat/registry/filebeat/log.json 
/var/lib/filebeat/registry/filebeat/log.json
```



#### 不同的文件生成不同的fields

```bash
# 示例1
[root@web02 ~]# cat /etc/filebeat/test_field.yaml 
filebeat.inputs:
- type: log
  paths:
  - /var/log/app1
  json.keys_under_root: true
  tags: ["app1_tag"]
  fields:
    type: "app1"

- type: log
  paths:
  - /var/log/app2
  json.keys_under_root: true
  tags: ["app2_tag"]
  field:
    type: "app2"

output.console:
  pretty: true
  
# 示例2：
[root@web02 ~]# cat /etc/filebeat/file_console.yaml
filebeat.inputs:
- type: log
  paths:
  - /var/log/syslog
  json.keys_under_root: true
  tags: ["syslog"]
  fields:
    type: "syslog"

- type: log
  paths:
  - /var/log/test.log
  json.keys_under_root: true
  tags: ["testlog"]
  fields:
    type: "testlog"

output.console:
  pretty: true
```



### 利用 Filebeat 收集系统日志到 ELasticsearch

**官方说明**

```http
https://www.elastic.co/guide/en/beats/filebeat/current/elasticsearch-output.html
```

**Filebeat收集的日志在Elasticsearch中默认生成的索引名称为**

```bash
#8.X新版
.ds-filebeat-<版本>-<时间>-<ID>
#旧版
filebeat-<版本>-<时间>-<ID>
```



#### 修改配置

```bash
# 方法1
# 先备份文件
[root@web02 /etc/filebeat]# cp /etc/filebeat/filebeat.yml{,.bak}
[root@web02 /etc/filebeat]# cat /etc/filebeat/filebeat.yml
# 删除所有原内容，只添加下面内容
filebeat.inputs:
- type: log
  json.keys_under_root: true
  enabled: true                   # 开启日志
  paths:
  - /var/log/syslog                    # 指定收集的日志

output.elasticsearch:
  hosts: ["10.0.0.150:9200", "10.0.0.151:9200", "10.0.0.152:9200"] # 指定ELK集群任意节点地址和端口，多个端口容错

# 启动服务
[root@web02 /etc/filebeat]# systemctl enable --now filebeat
```



#### 插件查看索引

**通过cerebro查看收集的日志信息**

![image-20250122110443183](../markdown_img/image-20250122110443183.png)

**通过Kibana查看收集的日志信息 (8.X版本 — 数据视图；7.X版本 — 索引模式)**

![image-20250122112341415](../markdown_img/image-20250122112341415.png)

![image-20250122112453394](../markdown_img/image-20250122112453394.png)

![image-20250122112633883](../markdown_img/image-20250122112633883.png)

![image-20250122112751286](../markdown_img/image-20250122112751286.png)

![image-20250122112810615](../markdown_img/image-20250122112810615.png)

```bash
# 测试
[root@web02 /var/log]# logger "This is a test log"

# 在Kibana中搜索查询
```

![image-20250122112933908](../markdown_img/image-20250122112933908.png)

![image-20250122113345402](../markdown_img/image-20250122113345402.png)

![image-20250122113358029](../markdown_img/image-20250122113358029.png)



###  自定义索引名称收集日志到 ELasticsearch

#### 修改配置

自定义索引名称收集所有系统日志到 ELasticsearch

```bash
# 原本的索引名为：.ds-filebeat-8.15.0-2025.01.22-000001

[root@web01 ~]# cat /etc/filebeat/filebeat.yml 
# 删除所有原内容，只添加下面内容
filebeat.inputs:
- type: log
  json.keys_under_root: true
  enabled: true                        # 开启日志
  paths:
  - /var/log/syslog                    # 指定收集的日志

output.elasticsearch:
  hosts: ["10.0.0.150:9200", "10.0.0.151:9200", "10.0.0.152:9200"]  # 指定ELK集群任意节点地址和端口，多个端口容错
  index: "mystical-%{[agent.version]}-%{+yyyy.MM.dd}"               # 自定义索引名称，8.X的索引为.ds-mystical，agent.version是filebeat添加的元数据
# 8.X，即使更改了索引名，最前面也会被强制添加.ds-*
# 7.X以前不会被强制添加.ds-

# 要改索引名，下面三行必须添加，如果不添加下面三行会报错
setup.ilm.enable: false               # 关闭索引生命周期ilm功能，默认开启时索引名称只能为filebeat-*，自定义索引名必须修改为false
setup.template.name: "mystical"       # 定义模板名称,要自定义索引名称,必须指定此项,否则无法启动
setup.template.pattern: "mystical-*"  # 定义模板的匹配索引名称,要自定义索引名称,必须指定此项,否则无法启动

# 指定分片和副本
setup.template.settings:
  index.number_of_shards: 3
  index.number_of_replicas: 1

# 重启服务
[root@web01 ~]# systemctl restart filebeat.service
```



**使用cerebro插件查看**

![image-20250122115259861](../markdown_img/image-20250122115259861.png)



**使用Kibana数据视图查看**

![image-20250122120537111](../markdown_img/image-20250122120537111.png)

![image-20250122120513796](../markdown_img/image-20250122120513796.png)



### 利用 tags 收集 Nginx的 Json 格式访问日志和错误日志到 Elasticsearch 不同的索引

**官方文档**

```http
https://www.elastic.co/guide/en/beats/filebeat/7.6/filebeat-input-log.html
https://www.elastic.co/guide/en/beats/filebeat/7.6/redis-output.html
```

生产环境中经常需要获取Web访问用户的信息，比如:访问网站的PV、UV、状态码、用户来自哪个地区，访问时间等

可以通过收集的Nginx的J访问日志实现

默认Nginx的每一次访问生成的访问日志是一行文本,ES没办法直接提取有效信息,不利于后续针对特定信息的分析

可以将Nginx访问日志转换为JSON格式解决这一问题



#### 安装 nginx 配置访问日志使用 Json 格式

```bash
#安装Nginx
[root@web02 ~]# apt update && apt -y install nginx

#修改nginx访问日志为Json格式
[root@web02 ~]# vim /etc/nginx/nginx.conf
......
log_format access_json '{"@timestamp":"$time_iso8601",'
        '"host":"$server_addr",'
        '"clientip":"$remote_addr",'
        '"size":$body_bytes_sent,'
        '"responsetime":$request_time,'
        '"upstreamtime":"$upstream_response_time",'
        '"upstreamhost":"$upstream_addr",'
	    '"http_host":"$host",'
        '"uri":"$uri",'
        '"domain":"$host",'
        '"xff":"$http_x_forwarded_for",'
        '"referer":"$http_referer",'
        '"tcp_xff":"$proxy_protocol_addr",'
        '"http_user_agent":"$http_user_agent",'
        '"status":"$status"}';

	access_log /var/log/nginx/access_json.log access_json;
	error_log /var/log/nginx/error.log;

# 查看
[root@web02 ~]# ll /var/log/nginx/access*
-rw-r--r-- 1 root     root   4975 Jan 22 05:59 /var/log/nginx/access_json.log
-rw-r----- 1 www-data adm    204  Jan 22 05:58 error.log
```



#### 修改Filebeat配置文件

```bash
#要收集多台nginx服务器日志到同名的ES的索引中,只要filebeat的配置都使用如下相同的配置即可
#可以ES中通过filebeat输出中自动添加agent_name字段中记录的每个主机的主机名(要确保每个主机的主机名不同)来区分日志来自于哪个主机
[root@web02 ~]# cat /etc/filebeat/filebeat.yml
# 删除所有原内容，只添加下面内容
filebeat.inputs:
- type: log
  json.keys_under_root: true
  json.overwrite_keys: true       # 设为ture，使用json格式日志中自定义的key替代默认的message，此项可选
  enabled: true                   # 开启日志
  paths:
  - /var/log/nginx/access_json.log
  tags: ["nginx-access"]          # 指定tag，用于分类

- type: log
  enabled: true
  paths:
  - /var/log/nginx/error.log
  tags: ["nginx-error"]

output.elasticsearch:
  hosts: ["10.0.0.150:9200", "10.0.0.151:9200", "10.0.0.152:9200"] # 指定ELK集群任意节点地址和端口，多个端口容错
  indices:
  - index: "nginx-access-%{[agent.version]}-%{+yyy.MM.dd}"
    when.contains:
      tags: "nginx-access"    # 如果日志中有access的tag，就记录到nginx-access的索引中
  - index: "nginx-error-%{[agent.version]}-%{+yyy.MM.dd}"
    when.contains:
      tags: "nginx-error"    # 如果日志中有error的tag，就记录到nginx-error的索引中



# 要改索引名，下面三行必须添加，如果不添加下面三行会报错
setup.ilm.enable: false               # 关闭索引生命周期ilm功能，默认开启时索引名称只能为filebeat-*，自定义索引名必须修改为false
setup.template.name: "nginx"       # 定义模板名称,要自定义索引名称,必须指定此项,否则无法启动
setup.template.pattern: "nginx-*"  # 定义模板的匹配索引名称,要自定义索引名称,必须指定此项,否则无法启动

# 指定分片和副本
setup.template.settings:
  index.number_of_shards: 3
  index.number_of_replicas: 1

```



#### **Cerebro插件查看索引**

![image-20250122141031491](../markdown_img/image-20250122141031491.png)



#### 使用Kibana查看索引

![image-20250122141316537](../markdown_img/image-20250122141316537.png)

![image-20250122141357867](../markdown_img/image-20250122141357867.png)



### 利用 fields 收集 Nginx的同一个访问日志中不同响应码的行到 Elasticsearch 不同的索引

#### 修改Filebeat配置文件

```bash
[root@web02 ~]# cat /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  json.keys_under_root: true
  json.overwrite_keys: true       # 设为ture，使用json格式日志中自定义的key替代默认的message，此项可选
  enabled: true
  paths:
  - /var/log/nginx/access_json.log
  # 可以选出日志中，指定行的数据
  include_lines: ['404']        # 文件中包含404的行
  # exclude_lines: ['']         # 排除包含关键字的值
  # exclude_files: ['.gz$']     # 排除文件名包含关键字的日志文件
  fields:
    status_code: "404"

- type: log
  json.keys_under_root: true
  json.overwrite_keys: true       # 设为ture，使用json格式日志中自定义的key替代默认的message，此项可选
  enabled: true
  paths:
  - /var/log/nginx/access_json.log
  include_lines: ['200']
  fields:
    status_code: "200"

- type: log
  json.keys_under_root: true
  json.overwrite_keys: true       # 设为ture，使用json格式日志中自定义的key替代默认的message，此项可选
  enabled: true
  paths:
  - /var/log/nginx/access_json.log
  include_lines: ['304']
  fields:
    status_code: "304"

output.elasticsearch:
  hosts: ["10.0.0.150:9200", "10.0.0.151:9200", "10.0.0.152:9200"]
  indices:
  - index: "myapp-error-404-%{+yyy.MM.dd}"
    when.equals:
      fields.status_code: "404"
  - index: "myapp-error-200-%{+yyy.MM.dd}"
    when.equals:
      fields.status_code: "200"
  - index: "myapp-error-304-%{+yyy.MM.dd}"
    when.equals:
      fields.status_code: "304"


setup.ilm.enable: false
setup.template.name: "myapp"
setup.template.pattern: "myapp-*"

setup.template.settings:
  index.number_of_shards: 3
  index.number_of_replicas: 1
  
# 重启服务
[root@web02 ~]# systemctl restart filebeat.service 
```



#### **Cerebro插件查看索引**

![image-20250122144529051](../markdown_img/image-20250122144529051.png)



#### 使用Kibana查看索引

![image-20250122144835128](../markdown_img/image-20250122144835128.png)



### 利用 Filebeat 收集 Tomat 的 Json 格式的访问日志和错误日志到 Elasticsearch

#### 安装 Tomcat 并配置使用 Json 格式的访问日志

```bash
# 安装Tomcat,可以包安装或者二进制安装
[root@web01 ~]# apt update && apt install -y tomcat9

# 包安装默认日志路径
[root@web01 /var/log/tomcat9]# ls /var/log/tomcat9/
catalina.2025-01-23.log  catalina.out  localhost.2025-01-23.log  localhost_access_log.2025-01-23.txt

# 修改Tomcat的访问日志为json格式
[root@web01 /var/log/tomcat9]# vim /etc/tomcat9/server.xml
......
<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
               prefix="localhost_access_log" suffix=".txt"
               # 注意pattern内的日志格式是一行，不要换行
               pattern="{&quot;clientip&quot;:&quot;%h&quot;,&quot;ClientUser&quot;:&quot;%l&quot;,&quot;authenticated&quot;:&quot;%u&quot;,&quot;AccessTime&quot;:&quot;%t&quot;,&quot;method&quot;:&quot;%r&quot;,&quot;status&quot;:&quot;%s&quot;,&quot;SendBytes&quot;:&quot;%b&quot;,&quot;Query?string&quot;:&quot;%q&quot;,&quot;partner&quot;:&quot;%{Referer}i&quot;,&quot;AgentVersion&quot;:&quot;%{User-Agent}i&quot;}" />

      </Host>
    </Engine>
  </Service>
</Server>

[root@web01 /var/log/tomcat9]# systemctl restart tomcat9

# 访问tomcat的页面，可以看到如下的json格式日志
[root@web01 /var/log/tomcat9]# tail -f /var/log/tomcat9/localhost_access_log.2025-01-23.txt 
{"clientip":"10.0.0.151","ClientUser":"-","authenticated":"-","AccessTime":"[23/Jan/2025:06:43:41 +0000]","method":"GET / HTTP/1.1","status":"200","SendBytes":"1895","Query?string":"","partner":"-","AgentVersion":"curl/7.81.0"}
```



#### 修改Filebeat配置文件

```bash
[root@web01 /var/log/tomcat9]# cat /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/tomcat9/localhost_access_log.*
  json.keys_under_root: true 
  json.overwrite_keys: false
  tags: ["tomcat-access"]

- type: log
  enabled: true
  paths:
  - /var/log/tomcat9/catalina.*.log
  tags: ["tomcat-error"]

output.elasticsearch:
  hosts: ["10.0.0.150:9200", "10.0.0.151:9200", "10.0.0.152:9200"]
  indices:
  - index: "tomcat-access-%{[agent.version]}-%{+yyy.MM.dd}"
    when.contains:
      tags: "tomcat-access"
  - index: "tomcat-error-%{[agent.version]}-%{+yyy.MM.dd}"
    when.contains:
      tags: "tomcat-error"

setup.ilm.enabled: false
setup.template.name: "tomcat"
setup.template.pattern: "tomcat-*"

# 重启filebeat服务
[root@web01 /var/log/tomcat9]# systemctl restart filebeat.service 
```



#### 插件查看索引

![image-20250123145535819](../markdown_img/image-20250123145535819.png)

![image-20250123145814580](../markdown_img/image-20250123145814580.png)

![image-20250123145854123](../markdown_img/image-20250123145854123.png)

![image-20250123150017701](../markdown_img/image-20250123150017701.png)





### 利用 Filebeat 收集 Tomat 的多行错误日志到 Elasticsearch

#### Tomcat 错误日志解析

Tomcat 是 Java 应用,当只出现一个错误时,会显示很多行的错误日志,如下所示

```bash
#包安装
[root@ubuntu2004 ~]#tail -f /var/log/tomcat9/catalina.2021-12-03.log
.....
03-Dec-2022 20:58:24.379 警告 [Thread-2] 
org.apache.catalina.loader.WebappClassLoaderBase.clearReferencesObjectStreamClas
sCaches 无法清除web应用程序[ROOT]的ObjectStreamClass$缓存中的软引用
 java.lang.ClassCastException: class java.io.ObjectStreamClass$Caches$1
cannot be cast to class java.util.Map (java.io.ObjectStreamClass$Caches$1 and 
java.util.Map are in module java.base of loader 'bootstrap')
 at 
org.apache.catalina.loader.WebappClassLoaderBase.clearCache(WebappClassLoaderBas
e.java:2325)
 at 
org.apache.catalina.loader.WebappClassLoaderBase.clearReferencesObjectStreamClas
sCaches(WebappClassLoaderBase.java:2300)
 at 
org.apache.catalina.loader.WebappClassLoaderBase.clearReferences(WebappClassLoad
erBase.java:1669)
 at 
org.apache.catalina.loader.WebappClassLoaderBase.stop(WebappClassLoaderBase.java
:1597)
...
```

Java 应用的一个错误导致生成的多行日志其实是同一个事件的日志的内容

而ES默认是根据每一行来区别不同的日志,就会导致一个错误对应多行错误信息会生成很多行的ES文档记 录

可以将一个错误对应的多个行合并成一个ES的文档记录来解决此问题



**官方文档**

```http
https://www.elastic.co/guide/en/beats/filebeat/current/multiline-examples.html
https://www.elastic.co/guide/en/beats/filebeat/7.0/multiline-examples.html
```



![image-20250123151144386](../markdown_img/image-20250123151144386.png)

#### 修改Filebeat文件

```bash
[root@web01 /var/log/tomcat9]# cat /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/tomcat9/localhost_access_log.*
  json.keys_under_root: true 
  json.overwrite_keys: false
  tags: ["tomcat-access"]

- type: log
  enabled: true
  paths:
  - /var/log/tomcat9/catalina.*.log
  tags: ["tomcat-error"]
  multiline.type: pattern            # 此为默认值，可省略
  multiline.pattern: '^[0-3][0-9]'   # 此正则表达式匹配以两位，或者为'^/d{2}',因为要匹配以日期开头
  multiline.negate: true             # negate否定无效
  multiline.match: after
  multiline.max_lines: 5000          # 默认只合并5000行，指定最大合并5000行

output.elasticsearch:
  hosts: ["10.0.0.150:9200", "10.0.0.151:9200", "10.0.0.152:9200"]
  indices:
  - index: "tomcat-access-%{[agent.version]}-%{+yyy.MM.dd}"
    when.contains:
      tags: "tomcat-access"
  - index: "tomcat-error-%{[agent.version]}-%{+yyy.MM.dd}"
    when.contains:
      tags: "tomcat-error"

setup.ilm.enabled: false
setup.template.name: "tomcat"
setup.template.pattern: "tomcat-*"

# 重启filebeat服务
[root@web01 /var/log/tomcat9]# systemctl restart filebeat.service 
```



### 利用 Filebeat 收集 Nginx 日志到 Redis

将 filebeat收集的日志,发送至Redis 格式如下

```yaml
output.redis:
  hosts: ["localhost:6379"]
  password: "my_password"
  key: "filebeat"
  db: 0
  timeout: 5
```



#### 安装 Nginx 配置访问日志使用 Json格式

 ```bash
 [root@web01 ~]#cat /etc/nginx/nginx.conf	
     ##
 	# Logging Settings
 	##
     log_format access_json '{"@timestamp":"$time_iso8601",'
     '"host":"$server_addr",'
     '"clientip":"$remote_addr",'
     '"size":$body_bytes_sent,'
     '"responsetime":$request_time,'
     '"upstreamtime":"$upstream_response_time",'
     '"upstreamhost":"$upstream_addr",'
     '"http_host":"$host",'
     '"uri":"$uri",'
     '"domain":"$host",'
     '"xff":"$http_x_forwarded_for",'
     '"referer":"$http_referer",'
     '"tcp_xff":"$proxy_protocol_addr",'
     '"http_user_agent":"$http_user_agent",'
     '"status":"$status"}';
 
 	access_log /var/log/nginx/access_json.log access_json;
 	error_log /var/log/nginx/error.log;
 	
 [root@web01 ~]#nginx -s reload
 ```



#### 安装和配置 Redis

```bash
[root@web01 ~]# apt install -y redis
[root@web01 ~]# sed -i.bak '/^bind.*/c bind 0.0.0.0'  /etc/redis/redis.conf
[root@web01 ~]# systemctl restart  redis
```



#### 修改 Filebeat 配置文件

```bash
[root@web01 ~]# cat /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/nginx/access_json.log
  json.keys_under_root: true
  json.overwrite_keys: true
  tags: ["nginx-access"]

- type: log
  enabled: true
  paths:
  - /var/log/nginx/error.log
  tags: ["nginx-error"]

output.redis:
  hosts: ["10.0.0.104:6379"]
  key: "filebeat"
```



#### 查看redis验证

```bash
[root@web01 ~]#redis-cli
127.0.0.1:6379> keys *
1) "filebeat"
127.0.0.1:6379> type filebeat
list
127.0.0.1:6379> lindex filebeat 0
"{/"@timestamp/":/"2025-01-28T09:11:15.000Z/",/"@metadata/":{/"beat/":/"filebeat/",/"type/":/"_doc/",/"version/":/"8.15.0/"},/"tags/":[/"nginx-access/"],/"upstreamhost/":/"-/",/"log/":{/"offset/":0,/"file/":{/"path/":/"/var/log/nginx/access_json.log/"}},/"uri/":/"/index.nginx-debian.html/",/"xff/":/"-/",/"referer/":/"-/",/"tcp_xff/":/"-/",/"host/":{/"name/":/"web01/"},/"clientip/":/"10.0.0.102/",/"ecs/":{/"version/":/"8.0.0/"},/"agent/":{/"name/":/"web01/",/"type/":/"filebeat/",/"version/":/"8.15.0/",/"ephemeral_id/":/"0d736cd1-4ceb-46f5-9589-30b0b03cf642/",/"id/":/"52dc5551-3312-4428-9923-914dfa240323/"},/"status/":/"200/",/"http_host/":/"10.0.0.104/",/"domain/":/"10.0.0.104/",/"http_user_agent/":/"curl/7.81.0/",/"size/":612,/"upstreamtime/":/"-/",/"responsetime/":0,/"input/":{/"type/":/"log/"}}"
127.0.0.1:6379> exit
```



### 从标准输入读取再输出至 Kafka

#### 编辑 filebeat.yml

```bash
[root@ubuntu2204 ~]#cat /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: stdin
  enabled: true

output.kafka:
  hosts: ["10.0.0.105:9092"]
  topic: mystical
  partition.round_robin:
    reachable_only: true
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000000
```

#### 输出测试

```bash
# 输出测试
[root@ubuntu2204 ~]# filebeat
hello, world
hello,python

# 从Kafka消费消息
[root@ubuntu2204 ~]# /usr/local/kafka/bin/kafka-console-consumer.sh --topic mystical --bootstrap-server 10.0.0.105:9092 --from-beginning
{"@timestamp":"2025-01-28T09:45:41.199Z","@metadata":{"beat":"filebeat","type":"_doc","version":"8.15.0"},"log":{"offset":0,"file":{"path":""}},"message":"hello, world","input":{"type":"stdin"},"ecs":{"version":"8.0.0"},"host":{"name":"ubuntu2204.wang.org"},"agent":{"name":"ubuntu2204.wang.org","type":"filebeat","version":"8.15.0","ephemeral_id":"f3bfa984-a8e4-4a11-b4c8-dbc1184582a2","id":"2e53b66f-23b4-4f30-80a6-7de2d388006e"}}
{"@timestamp":"2025-01-28T09:46:54.507Z","@metadata":{"beat":"filebeat","type":"_doc","version":"8.15.0"},"host":{"name":"ubuntu2204.wang.org"},"agent":{"ephemeral_id":"f3bfa984-a8e4-4a11-b4c8-dbc1184582a2","id":"2e53b66f-23b4-4f30-80a6-7de2d388006e","name":"ubuntu2204.wang.org","type":"filebeat","version":"8.15.0"},"log":{"offset":0,"file":{"path":""}},"message":"hello,python","input":{"type":"stdin"},"ecs":{"version":"8.0.0"}}
```



### 从标准输入读取再输出至 Logstash

#### 编辑filebeat.yml

```bash
[root@elk-web1 ~]#vim /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: stdin
  enabled: true
  
output.logstash:
  hosts: ["10.0.0.104:5044","10.0.0.105:5044"]
  index: filebeat  
  loadbalance: true     #默认为false,只随机输出至一个可用的logstash,设为true,则输出至全部logstash
  worker: 1             #线程数量        
  compression_level: 3  #压缩比
```





# Logstash过滤

## Logstash 介绍

![image-20250128175852633](../markdown_img/image-20250128175852633.png)

Logstash 是免费且开放的**服务器端数据处理管道**，能够从多个来源采集数据，转换数据，然后将数据发送到您最喜欢的一个或多个“存储库”中

Logstash 是整个ELK中拥有最丰富插件的一个组件,而且支持可以水平伸缩

Logstash 基于 **Java** 和 **Ruby** 语言开发

Logstash  官网:

```http
https://www.elastic.co/cn/logstash/
```

 Logstash 官方说明

```http
https://www.elastic.co/guide/en/logstash/current/index.html
https://www.elastic.co/guide/en/logstash/7.6/index.html
```



**Logstash 架构**

- 输入 Input：用于日志收集,常见插件: Stdin、File、Kafka、Redis、Filebeat、Http
- 过滤 Filter：日志过滤和转换,常用插件: grok、date、geoip、mutate、useragent
- 输出 Output：将过滤转换过的日志输出, 常见插件: File,Stdout,Elasticsearch,MySQL,Redis,Kafka



**Logstash 和 Filebeat 比较**

- Logstash 功能更丰富,可以支持直接将非Josn 格式的日志统一转换为Json格式,且支持多目标输出, 和filebeat相比有更为强大的过滤转换功能
- Logstash 资源消耗更多,不适合在每个需要收集日志的主机上安装



## Logstash 安装

安装要求

```http
https://www.elastic.co/guide/en/logstash/current/getting-started-with-logstash.html
```

安装方法

```http
https://www.elastic.co/guide/en/logstash/current/installing-logstash.html
```

可以支持下面安装方法

- 二进制
- 包安装
- Docker容器



### 环境准备安装 Java 环境

注意: 8.X版本之后的logstash包已经内置了JDK无需安装

新版 Logstash 要求 JAVA 要求 11和17 

```http
https://www.elastic.co/guide/en/logstash/current/getting-started-with-logstash.html
```



###  Ubuntu 环境准备

```bash
#8.X要求安装JDK11或17,新版logstash包已经内置了JDK无需安装
[root@logstash ~]#apt update && apt -y install openjdk-17-jdk
[root@logstash ~]#apt update && apt -y install openjdk-11-jdk

#7.X 要求安装JDK8
[root@logstash ~]#apt -y install openjdk-8-jdk
```



### CentOS 环境准备

关闭防火墙和 SELinux

```bash
[root@logstash ~]# systemctl disable --now firewalld
 [root@logstash ~]# sed -i '/SELINUX/s/enforcing/disabled/' /etc/selinux/config
 [root@logstash ~]# setenforce 0
```

安装 Java 环境

```bash
#安装oracle 的JDK
[root@logstash ~]# yum install jdk-8u121-linux-x64.rpm
[root@logstash ~]# java -version
java version "1.8.0_121"
Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)

#或者安装OpenJDK
[root@logstash ~]# yum -y install java-1.8.0-openjdk
[root@logstash ~]# java -version
openjdk version "1.8.0_302"
OpenJDK Runtime Environment (build 1.8.0_302-b08)
OpenJDK 64-Bit Server VM (build 25.302-b08, mixed mode)
```



### 包安装 Logstash

注意:  Logstash 版本要和 Elasticsearch 相同的版本，否则可能会出错

Logstash 官方下载链接:

```http
https://www.elastic.co/cn/downloads/logstash
https://www.elastic.co/cn/downloads/past-releases#logstash
```

镜像网站下载链接

```http
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/
```



### Ubuntu 安装 Logstash

范例：8.X版本的包安装

```bash
[root@logstash ~]# wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/l/logstash/logstash-8.6.1-amd64.deb
[root@logstash ~]# dpkg -i logstash-8.6.1-amd64.deb
[root@logstash ~]# systemctl enable --now logstash.service
```



### RHEL系列安装 Logstash

范例: 包安装

```bash
[root@logstash ~]# wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/7.x/yum/7.6.2/logstash-7.6.2.rpm
[root@logstash ~]# yum install logstash-7.6.2.rpm
[root@logstash ~]# chown logstash.logstash /usr/share/logstash/data/queue –R #权限更改为logstash用户和组，否则启动的时候日志报错
```



### 修改 Logstash 配置(可选)

```bash
#默认配置可以不做修改
[root@logstash ~]#vim /etc/logstash/logstash.yml
[root@logstash ~]#grep -Ev '#|^$' /etc/logstash/logstash.yml
node.name: logstash-node01
pipeline.workers: 2
pipeline.batch.size: 1000      #批量从IPNPUT读取的消息个数，可以根据ES的性能做性能优化
pipeline.batch.delay: 5        #处理下一个事件前的最长等待时长，以毫秒ms为单位,可以根据ES的性能做性能优化
path.data: /var/lib/logstash   #默认值
path.logs: /var/log/logstash   #默认值

#内存优化
[root@logstash ~]# vim /etc/logstash/jvm.options
-Xms1g
-Xmx1g

#Logstash默认以logstash用户运行,如果logstash需要收集本机的日志,可能会有权限问题,可以修改为root
[root@logstash ~]#vim /lib/systemd/system/logstash.service
[Service]
User=root
Group=root

#查看子配置文件路径:/etc/logstash/conf.d/*.conf
[root@logstash ~]#cat /etc/logstash/pipelines.yml 
# This file is where you define your pipelines. You can define multiple.
# For more information on multiple pipelines, see the documentation:
# https://www.elastic.co/guide/en/logstash/current/multiple-pipelines.html
- pipeline.id: main
  path.config: "/etc/logstash/conf.d/*.conf"

[root@logstash ~]#systemctl daemon-reload && systemctl restart logstash
```



## Logstash 使用

**查看帮助**

```bash
[root@logstash1 ~]#/usr/share/logstash/bin/logstash --help

#常用选项
-e 指定配置内容
-f 指定配置文件，支持绝对路径，如果用相对路径，是相对于/usr/share/logstash/的路径
-t 语法检查
-r 修改配置文件后自动加载生效,注意:有时候修改配置还需要重新启动生效

#服务方式启动,由于默认没有配置文件,所以7.X无法启动，8.X可以启动
[root@logstash ~]#systemctl start logstash
```



**各种插件帮助**

```http
https://www.elastic.co/guide/en/logstash/current/index.html
```



**列出所有插件**

```bash
[root@logstash1 ~]#/usr/share/logstash/bin/logstash-plugin list
```

 

**Github logstash插件链接**

```http
https://github.com/logstash-plugins
```



### Logstash 输入 Input 插件

官方链接

```http
https://www.elastic.co/guide/en/logstash/7.6/input-plugins.html
```



#### 标准输入

codec 用于输入数据的编解码器，默认值为plain表示单行字符串，若设置为json，表示按照json方式解析

范例: 交互式实现标准输入

```bash
#标准输入和输出,codec => rubydebug指输出格式，是默认值，可以省略，也支持设为json，以json格式输出
[root@logstash1 ~]#/usr/share/logstash/bin/logstash -e 'input { stdin{} } output { stdout{} }'
# 输入
hello,python  
# 输出
{
          "host" => {
        "hostname" => "logstash1"
    },
       "message" => "hello,python",
    "@timestamp" => 2025-01-28T10:55:14.459186056Z,
      "@version" => "1",
         "event" => {
        "original" => "hello,python"
    }
}

# 输入json格式的数据
{ "name" : "mystical", "age" : "18"}
# 输出：未解析json格式
{
          "host" => {
        "hostname" => "logstash1"
    },
       "message" => "{ /"name/" : /"mystical/", /"age/" : /"18/"}",
    "@timestamp" => 2025-01-28T10:57:46.303054636Z,
      "@version" => "1",
         "event" => {
        "original" => "{ /"name/" : /"mystical/", /"age/" : /"18/"}"
    }
}

# 解析json格式数据，code => rubydebug为默认选项，可以省略
[root@logstash1 ~]#/usr/share/logstash/bin/logstash -e 'input { stdin{ codec => json } } output { stdout{ codec => rubydebug } }'
# 输入json格式数据
{ "name": "mystical", "age": "18", "gender": "men" }

# 输出时，会解析json数据
{
           "age" => "18",
    "@timestamp" => 2025-01-28T11:31:34.453097351Z,
         "event" => {
        "original" => "{ /"name/": /"mystical/", /"age/": /"18/", /"gender/": /"men/" }/n"
    },
          "name" => "mystical",
      "@version" => "1",
        "gender" => "men",
          "host" => {
        "hostname" => "logstash1"
    }
}

# 输入非json数据，会提示解析失败，并存放message字段
hello,python
[WARN ] 2025-01-28 19:37:16.620 [[main]<stdin] jsonlines - JSON parse error, original data now in message field {:message=>"Unrecognized token 'hello': was expecting (JSON String, Number, Array, Object or token 'null', 'true' or 'false')/n at [Source: (String)/"hello,python/"; line: 1, column: 6]", :exception=>LogStash::Json::ParserError, :data=>"hello,python"}
{
    "@timestamp" => 2025-01-28T11:37:16.626204699Z,
         "event" => {
        "original" => "hello,python/n"
    },
      "@version" => "1",
       "message" => "hello,python",
          "tags" => [
        [0] "_jsonparsefailure"
    ],
          "host" => {
        "hostname" => "logstash1"
    }
}

#添加tag和type
/usr/share/logstash/bin/logstash  -e 'input { stdin{  tags => "stdin_tag"  type => "stdin_type" codec => json }  } output { stdout{  }}'

# 输入json数据
{ "name":"mystical", "age":"18","position":"sg"}

# 输出，其中type是键值对，而tags是一个列表
{
      "position" => "sg",
          "tags" => [
        [0] "stdin_tag"
    ],
          "name" => "mystical",
    "@timestamp" => 2025-01-28T11:40:08.725851262Z,
      "@version" => "1",
         "event" => {
        "original" => "{ /"name/":/"mystical/", /"age/":/"18/",/"position/":/"sg/"}/n"
    },
          "type" => "stdin_type",
           "age" => "18",
          "host" => {
        "hostname" => "logstash1"
    }
}

```

以配置文件实现标准输入

```bash
[root@logstash1 conf.d]#cat stdin_to_stdout.conf 
input {
    stdin {
        type => "stdin_type"
        tags => "stdin_tag"
        codec => "json"
    }
}

output {
    stdout {
        codec => "rubydebug" # 默认值
    }
}

# 执行
[root@logstash1 conf.d]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/stdin_to_stdout.conf
# 输入json格式数据
{"name":"mystical", "age":"18"}

# 输出
{
          "name" => "mystical",
      "@version" => "1",
         "event" => {
        "original" => "{/"name/":/"mystical/", /"age/":/"18/"}/n"
    },
    "@timestamp" => 2025-01-28T12:05:22.790372226Z,
          "type" => "stdin_type",
          "tags" => [
        [0] "stdin_tag"
    ],
           "age" => "18",
          "host" => {
        "hostname" => "logstash1"
    }
}
```





#### 从文件输入

Logstash 会记录每个文件的读取位置,下次自动从此位置继续向后读取

每个文件的读取位置记录在下面对应的文件中（此文件包括文件的 inode号, 大小等信息）

```bash
#新版：8.11.1
/usr/share/logstash/data/plugins/inputs/file/.sincedb_f5fdf6ea0ea92860c6a6b2b354bfcbbc

#旧版
/var/lib/logstash/plugins/inputs/file/.sincedb_xxxx
```

范例:

```bash
[root@logstash1 conf.d]#cat file_to_stdout.conf 
input {
    file {
        path => "/tmp/wang.*"
        type => "wanglog"                     # 添加自定义的type字段,可以用于条件判断,和filebeat中tag功能相似
        exclude => "*.txt"                    # 排除不采集数据的文件，使用通配符glob匹配语法
        start_position => "beginning"         # 第一次从头开始读取文件,可以取值为:beginning和end,默认为end,即只从最后尾部读取日志
        stat_interval => "3"                  # 定时检查文件是否更新，默认1s
        codec => json                         # 如果文件是Json格式,需要指定此项才能解析,如果不是Json格式而添加此行也不会影响结果
    }
    
    file {
        path => "/var/log/syslog"
        type => "syslog"
        start_position => "beginning"
        stat_interval => "3"
    }

}

output {
    stdout {
        codec => rubydebug
    }
}

# 测试
[root@logstash1 conf.d]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/file_to_stdout.conf 
```



#### 从 Http 请求买取数据

```bash
[root@logstash ~]# cat /etc/logstash/conf.d/http_to_stdout.conf
input {
    http {
        port => 6666
        codec => json
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 测试
[root@ubuntu2204 ~]# curl -XPOST -d "This is a test data" 10.0.0.106:6666
ok

# 在10.0.0.106的logstash收到请求体内容
[root@logstash1 conf.d]# /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/http_to_stdout.conf 
{
           "url" => {
          "path" => "/",
          "port" => 6666,
        "domain" => "10.0.0.106"
    },
      "@version" => "1",
    "@timestamp" => 2025-01-28T13:07:47.020281752Z,
          "tags" => [
        [0] "_jsonparsefailure"
    ],
          "http" => {
        "version" => "HTTP/1.1",
         "method" => "POST",
        "request" => {
                 "body" => {
                "bytes" => "19"
            },
            "mime_type" => "application/x-www-form-urlencoded"
        }
    },
       "message" => "This is a test data",
    "user_agent" => {
        "original" => "curl/7.81.0"
    },
          "host" => {
        "ip" => "10.0.0.105"
    }
}

# 默认可以解析json数据
[root@ubuntu2204 ~]#curl -XPOST -d '{"name":"mystcal", "age":"18"}' 10.0.0.106:6666
ok

# 在10.0.0.106的logstash收到请求体内容 
# json数据成功被解析
{
           "url" => {
          "path" => "/",
          "port" => 6666,
        "domain" => "10.0.0.106"
    },
      "@version" => "1",
    "@timestamp" => 2025-01-28T13:14:24.742440563Z,
          "name" => "mystcal",
         "event" => {
        "original" => "{/"name/":/"mystcal/", /"age/":/"18/"}"
    },
          "http" => {
        "version" => "HTTP/1.1",
         "method" => "POST",
        "request" => {
                 "body" => {
                "bytes" => "30"
            },
            "mime_type" => "application/x-www-form-urlencoded"
        }
    },
    "user_agent" => {
        "original" => "curl/7.81.0"
    },
           "age" => "18",
          "host" => {
        "ip" => "10.0.0.105"
    }
}
```



####  从 Filebeat 读取数据

```bash
#filebeat配置
[root@elk-web1 ~]# vim /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: log
  enabled: true                            #开启日志 
  paths:
  - /var/log/nginx/access_json.log         #指定收集的日志文件     
  json.keys_under_root: true
  tags: ["nginx-access"]
  
- type: log
  enabled: true            
  paths:
  - /var/log/syslog                       #指定收集的日志文件        
  fields:
    logtype: "syslog"                     #添加自定义字段logtype

#output.console:
#  pretty: true
#  enable: true

output.logstash:
  hosts: ["10.0.0.106:5044"]             #指定Logstash服务器的地址和端口
  

# Logstash配置
[root@logstash ~]# cat /etc/logstash/conf.d/filebeat_to_stdout.conf
input {
    beats {
       port => 5044
    }
 }
 
output {
    stdout {
        codec => rubydebug
    }
}

# 测试
[root@web01 ~]#systemctl restart filebeat.service 
# 访问filebeat所在机器上的nginx
[root@node3 local]#curl 10.0.0.104

# filebeat将nginx产生的日志传给logstash
[root@logstash1 conf.d]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/filebeat_to_stdout.conf
{
       "upstreamtime" => "-",
            "referer" => "-",
                "ecs" => {
        "version" => "8.0.0"
    },
       "upstreamhost" => "-",
            "tcp_xff" => "-",
          "http_host" => "10.0.0.104",
         "@timestamp" => 2025-01-28T13:33:34.565Z,
           "@version" => "1",
    "http_user_agent" => "curl/7.81.0",
                "log" => {
          "file" => {
            "path" => "/var/log/nginx/access_json.log"
        },
        "offset" => 322
    },
              "agent" => {
        "ephemeral_id" => "ceca0e07-f91a-42b3-b064-b8a11cb1e96c",
                  "id" => "52dc5551-3312-4428-9923-914dfa240323",
                "name" => "web01",
                "type" => "filebeat",
             "version" => "8.15.0"
    },
           "clientip" => "10.0.0.102",
               "host" => {
        "name" => "web01"
    },
              "input" => {
        "type" => "log"
    },
                "xff" => "-",
                "uri" => "/index.nginx-debian.html",
               "tags" => [
        [0] "nginx-access",
        [1] "beats_input_raw_event"
    ],
               "size" => 612,
             "domain" => "10.0.0.104",
       "responsetime" => 0,
             "status" => "200"
}

```



####  从 Redis 中读取数据

支持由多个 Logstash 从 Redis 读取日志,提高性能

Logstash 从 Redis 收集完数据后,将删除对应的列表Key

```bash
# 初始在redis所在服务器上，即10.0.0.104，有三条数据
[root@web01 ~]#redis-cli -a 123456 -h 10.0.0.104
10.0.0.104:6379> llen filebeat
(integer) 3

# 编辑logstash配置文件
[root@logstash1 conf.d] #cat redis_to_stdout.conf 
input {
    redis {
        host => '10.0.0.104'
        port => "6379"
        password => "123456"
        db => "0"
        data_type => 'list'
        key => "filebeat"
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 启动logstash，会输出redis的key-filebeat里的数据
[root@logstash1 conf.d]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/redis_to_stdout.conf
...

# 再次查看redis，数据被取走了
[root@web01 ~]#redis-cli -a 123456 -h 10.0.0.104
10.0.0.104:6379> llen filebeat
(integer) 0
```



#### Filebeat -> Redis -> Logstatsh

```bash
# filebeat配置
[root@web01 ~]#cat /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/nginx/access_json.log
  json.keys_under_root: true
  json.overwrite_keys: true
  tags: ["nginx-access"]

- type: log
  enabled: true
  paths:
  - /var/log/nginx/error.log
  tags: ["nginx-error"]

output.redis:
  hosts: ["10.0.0.104:6379"]
  key: "filebeat"
  password: "123456"
  
#logstatsh配置
[root@logstash1 ~]#cat /etc/logstash/conf.d/redis_to_stdout.conf 
input {
    redis {
        host => '10.0.0.104'
        port => "6379"
        password => "123456"
        db => "0"
        data_type => 'list'
        key => "filebeat"
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 测试
# 使用10.0.0.100访问10.0.0.104上的nginx
[root@node1 config]#curl 10.0.0.104

# 在10.0.0.106，也就是logstash的服务器上，收到消息
[root@logstash1 conf.d]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/redis_to_stdout.conf 
{
              "input" => {
        "type" => "log"
    },
               "tags" => [
        [0] "nginx-access"
    ],
              "event" => {
        "original" => "{/"@timestamp/":/"2025-01-28T14:47:32.000Z/",/"@metadata/":{/"beat/":/"filebeat/",/"type/":/"_doc/",/"version/":/"8.15.0/"},/"upstreamtime/":/"-/",/"xff/":/"-/",/"host/":{/"name/":/"web01/"},/"http_host/":/"10.0.0.104/",/"input/":{/"type/":/"log/"},/"status/":/"200/",/"responsetime/":0,/"upstreamhost/":/"-/",/"tags/":[/"nginx-access/"],/"log/":{/"offset/":966,/"file/":{/"path/":/"/var/log/nginx/access_json.log/"}},/"domain/":/"10.0.0.104/",/"tcp_xff/":/"-/",/"size/":612,/"uri/":/"/index.nginx-debian.html/",/"referer/":/"-/",/"clientip/":/"10.0.0.100/",/"http_user_agent/":/"curl/7.81.0/",/"ecs/":{/"version/":/"8.0.0/"},/"agent/":{/"ephemeral_id/":/"9afd9c68-255e-4e55-b734-8a78298a26e2/",/"id/":/"52dc5551-3312-4428-9923-914dfa240323/",/"name/":/"web01/",/"type/":/"filebeat/",/"version/":/"8.15.0/"}}"
    },
          "http_host" => "10.0.0.104",
           "@version" => "1",
       "upstreamhost" => "-",
            "referer" => "-",
                "xff" => "-",
            "tcp_xff" => "-",
         "@timestamp" => 2025-01-28T14:47:32.000Z,
               "host" => {
        "name" => "web01"
    },
       "responsetime" => 0,
           "clientip" => "10.0.0.100",
               "size" => 612,
       "upstreamtime" => "-",
             "domain" => "10.0.0.104",
                "log" => {
          "file" => {
            "path" => "/var/log/nginx/access_json.log"
        },
        "offset" => 966
    },
    "http_user_agent" => "curl/7.81.0",
                "ecs" => {
        "version" => "8.0.0"
    },
             "status" => "200",
                "uri" => "/index.nginx-debian.html",
              "agent" => {
        "ephemeral_id" => "9afd9c68-255e-4e55-b734-8a78298a26e2",
                  "id" => "52dc5551-3312-4428-9923-914dfa240323",
                "name" => "web01",
                "type" => "filebeat",
             "version" => "8.15.0"
    }
}
```



#### 从 Kafka 中读取数据

```bash
#logstash会读取kafka最新生成的消息数据，原有的消息不会读取
[root@logstash ~]#cat /etc/logstash/conf.d/kakfa_to_stdout.conf
input {
    kafka {
        bootstrap_servers => "10.0.0.201:9092,10.0.0.202:9092,10.0.0.203:9092"
        group_id => "logstash" #多个logstash的group_id如果不同，将实现消息共享（发布者/订阅者模式），如果相同（建议使用），则消息独占（生产者/消费者模式）
        topics => ["nginx-accesslog","nginx-errorlog"]
        codec => "json"
        consumer_threads => 8
    }
}

output {
    stdout {
        codec => rubydebug
    }
}
```



#### Filebeat -> Kafka -> Logstash

```bash
# 注意：Kafka开放端口，默认仅本机可以访问
[root@ubuntu2204 ~]#vim /usr/local/kafka/config/server.properties
listeners=PLAINTEXT://0.0.0.0:9092
advertised.listeners=PLAINTEXT://10.0.0.105:9092

# 重启Kafka，重启的时候，注意Kafka等待一段时间，才会开放端口，耐心等待
[root@ubuntu2204 ~]#systemctl restart kafka

# kafka创建nginx-access和nginx-error的topic
[root@ubuntu2204 ~]#/usr/local/kafka/bin/kafka-topics.sh --create --topic nginx-access --bootstrap-server 10.0.0.105:9092
[root@ubuntu2204 ~]#/usr/local/kafka/bin/kafka-topics.sh --create --topic nginx-error --bootstrap-server 10.0.0.105:9092

# filebeat编辑
[root@web01 filebeat]#cat /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: log
  json.keys_under_root: true
  json.overwrite_keys: true       # 设为ture，使用json格式日志中自定义的key替代默认的message，此项可选
  enabled: true                   # 开启日志
  paths:
  - /var/log/nginx/access_json.log
  fields:
    log_type: nginx-access
  fields_under_root: true

- type: log
  enabled: true
  paths:
  - /var/log/nginx/error.log
  fields:
    log_type: nginx-error
  fields_under_root: true

output.kafka:
  # 配置 Kafka 的连接信息
  hosts: ["10.0.0.105:9092"]  # 替换为你的 Kafka broker 地址
  topic: '%{[log_type]}'  # 动态设置 topic，使用 log_type 字段
  partition.round_robin:
    reachable_only: true  # 仅将消息发送到可用分区
  required_acks: 1        # 消息发送成功时的确认级别
  compression: gzip       # 启用数据压缩（可选）
  max_message_bytes: 1000000  # 最大消息大小（根据 Kafka 配置调整

# 重启filebeat
[root@web01 filebeat]#systemctl restart filebeat.service 

# 编辑logstash
[root@logstash1 ~]#cat /etc/logstash/conf.d/kafka_to_stdout.conf 
input {
    kafka {
        bootstrap_servers => "10.0.0.105:9092"
        group_id => "logstash" #多个logstash的group_id如果不同，将实现消息共享（发布者/订阅者模式），如果相同（建议使用），则消息独占（生产者/消费者模式）
        topics => ["nginx-access","nginx-error"]
        codec => "json"
        consumer_threads => 8
    }
 }


output {
    stdout {
        codec => rubydebug
    }
}
```



#### 从syslog输入数据

```bash
# 配合rsyslog使用
# 在rsyslog配置文件中添加：*.*  @10.0.0.105（514是默认端口，可以不写）
[root@logstash1 conf.d]#cat syslog_to_stdout.conf 
input {
    syslog {
        host => "0.0.0.0"
        port => "514"       # 指定监听的UDP/TCP端口，注意普通用户无法监听特权端口（0-1024）
        type => "haproxy"
    }
}

output {
    stdout {
        codec => rubydebug
    }
}
```



#### 从TCP/UDP协会输入数据

```bash
[root@logstash1 conf.d]#cat tcp_to_stdout.conf 
input {
    tcp {
        port => "9527"
        host => "0.0.0.0"
        type => "tcplog"
        codec => json
        mode => "server"
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 启用
[root@logstash1 conf.d]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/tcp_to_stdout.conf 

# 远程服务器使用nc连接
nc 10.0.0.106 9527
hello, test

# logstash上显示
{
          "tags" => [
        [0] "_jsonparsefailure"
    ],
       "message" => "hello, test",
      "@version" => "1",
          "type" => "tcplog",
    "@timestamp" => 2025-01-29T00:43:41.440597604Z
}
```



### Logstash 过滤 Filter 插件

数据从源传输到存储库的过程中，Logstash 过滤器能够解析各个事件，识别已命名的字段以构建结构， 并将它们转换成通用格式，以便进行更强大的分析和实现商业价值。

Logstash 能够动态地转换和解析数据，不受格式或复杂度的影响

常见的 Filter 插件:

- 利用 **Grok** 从非结构化数据中转化为结构数据
- 利用 GEOIP 根据 IP 地址找出对应的地理位置坐标
- 利用 useragent 从请求中分析操作系统、设备类型
- 利用 Mutate 从请求中整理字段



**官方链接**

```http
https://www.elastic.co/guide/en/logstash/current/filter-plugins.html
https://www.elastic.co/guide/en/logstash/7.6/filter-plugins.html
```



#### Grok 插件

Grok  是一个过滤器插件，可帮助用户描述日志格式的结构。有超过200种 grok模式抽象概念，如IPv6 地址，UNIX路径和月份名称。

为了将日志行与格式匹配, 生产环境常需要将非结构化的数据解析成 json 结构化数据格式

Grok 可以解析任意文本并把它结构化。因此 Grok 是**将非结构化的日志数据解析为可查询的结构化数据**的好方法。

Grok 非常适合将syslog 日志、apache 和其他 web 服务器日志、MySQL 日志等日志格式转换为JSON格 式。

**比如下面行**

```bash
2016-09-19T18:19:00 [8.8.8.8:prd] DEBUG this is an example log message
```

使用  Grok 插件可以基于正则表达式技术利用其内置的正则表达式的别名来表示和匹配上面的日志,如下效果

```bash
%{TIMESTAMP_ISO8601:timestamp} /[%{IPV4:ip};%{WORD:environment}/] %{LOGLEVEL:log_level} %{GREEDYDATA:message}
```

最终转换为以下格式

```json
{
  "timestamp": "2016-09-19T18:19:00",
  "ip": "8.8.8.8",
  "environment": "prd",
  "log_level": "DEBUG",
  "message": "this is an example log message"
}
```

**参考网站**

```http
# 可以直接问CHATGPT
```

示例

```bash
# 编辑logstash
[root@logstash1 conf.d]#cat tcp_to_stdout.conf 
input {
    tcp {
        port => "9527"
        host => "0.0.0.0"
        type => "tcplog"
        codec => json
        mode => "server"
    }
}


filter {
    grok {
        match => {
            # TIME匹配的值，作为timestamp这个健的值，WORD的值，作为log_level这个健的值...
            "message" => "%{YEAR}/%{MONTHNUM}/%{MONTHDAY} %{TIME:timestamp} /[%{WORD:log_level}/] %{NUMBER:pid1}#%{NUMBER:pid2}: %{GREEDYDATA:message}"
        }
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 在另一个服务器上使用nc连接10.0.0.106,即logstash所在服务器的9527端口
[root@web01 ~]#nc 10.0.0.106 9527
2025/01/28 15:03:26 [notice] 2299#2299: using inherited sockets from "6;7;"

# 在logstash所在服务器上启动logstash，然后等待数据输出
# -r 表示可以动态加载logstash的配置文件
[root@logstash1 conf.d]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/tcp_to_stdout.conf -r
{
          "tags" => [
        [0] "_jsonparsefailure"
    ],
          "pid2" => "2299",
     "timestamp" => "15:03:26",
     "log_level" => "notice",
       "message" => [
        [0] "2025/01/28 15:03:26 [notice] 2299#2299: using inherited sockets from /"6;7;/"",
        [1] "using inherited sockets from /"6;7;/""
    ],
      "@version" => "1",
    "@timestamp" => 2025-01-29T10:28:23.098915063Z,
          "type" => "tcplog",
          "pid1" => "2299"
}
```



##### 在 Grok 中使用自定义正则表达式

Grok 允许你用 `(?<字段名>正则表达式)` 的形式定义自定义字段匹配规则。例如

示例日志

```bash
192.168.1.100 - - [28/Jan/2025:15:03:26 +0000] "GET /index.html HTTP/1.1" 200 1024
```

使用自定义正则

```bash
# 这里 (?<request>.*?) 中.*? 表示非贪婪匹配
(?<client_ip>/d+/./d+/./d+/./d+) - - /[(?<timestamp>/d{2}/[A-Za-z]+//d{4}:/d{2}:/d{2}:/d{2} [+/-]/d{4})/] "(?<method>/w+) (?<request>.*?) HTTP/(?<http_version>/d+/./d+)" (?<status>/d{3}) (?<bytes>/d+)
```

解析结果

```json
{
  "client_ip": "192.168.1.100",
  "timestamp": "28/Jan/2025:15:03:26 +0000",
  "method": "GET",
  "request": "/index.html",
  "http_version": "1.1",
  "status": "200",
  "bytes": "1024"
}
```



##### 在 Logstash 中使用自定义正则

如果 Grok 预定义的模式不能满足需求，你可以直接在 `logstash.conf` 中使用自定义正则表达式。

示例：解析 Nginx error.log

```bash
2025/01/28 15:03:26 [error] 2299#2299: failed to open file "/var/log/nginx/access.log"
```

logstash Grok配置

```bash
filter {
  grok {
    match => {
      "message" => "(?<year>/d{4})/(?<month>/d{2})/(?<day>/d{2}) (?<time>/d{2}:/d{2}:/d{2}) /[(?<log_level>/w+)/] (?<pid1>/d+)#(?<pid2>/d+): (?<message>.*)"
    }
  }
  
  # 字段合并
  mutate {
    add_field => { "full_timestamp" => "%{year}-%{month}-%{day} %{time}" }
  }

  date {
    match => [ "full_timestamp", "yyyy-MM-dd HH:mm:ss" ]
    target => "@timestamp"
    timezone => "UTC"
  }
}

```

解析结果

```bash
{
  "@timestamp": "2025-01-28T15:03:26.000Z",
  "log_level": "error",
  "pid1": "2299",
  "pid2": "2299",
  "message": "failed to open file /"/var/log/nginx/access.log/""
}
```



##### 结合 Grok 和 自定义正则

你还可以在 Grok 规则中混合使用 Grok 预定义模式和自定义正则。

```bash
grok {
  match => { "message" => "%{YEAR}/%{MONTHNUM}/%{MONTHDAY} (?<time>/d{2}:/d{2}:/d{2}) /[%{WORD:log_level}/] (?<pid1>/d+)#(?<pid2>/d+): (?<message>.*)" }
}
```



##### 使用 `patterns_dir` 定义自定义 Grok 规则

如果你需要经常使用自定义模式，可以将它们存入 `patterns_dir` 目录，然后在 Grok 过滤器中引用。

- 创建自定义 Grok 规则文件

```bash
mkdir -p /etc/logstash/patterns
vi /etc/logstash/patterns/nginx
```

- 在 `nginx` 文件中定义模式

```bash
NGINX_ERROR_LOG %{YEAR}/%{MONTHNUM}/%{MONTHDAY} %{TIME} /[%{WORD:log_level}/] %{NUMBER:pid1}#%{NUMBER:pid2}: %{GREEDYDATA:message}
```

- 在 `logstash.conf` 中引用模式

```bash
filter {
  grok {
    patterns_dir => ["/etc/logstash/patterns"]
    match => { "message" => "%{NGINX_ERROR_LOG}" }
  }
}
```



#### GeoIP 插件

geoip 根据 ip 地址提供的对应地域信息，比如:经纬度,国家,城市名等,以方便进行地理数据分析

```bash
# 查看IP地理位置数据库的路径
[root@logstash1 vendor]#dpkg -L logstash|grep mmdb
/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-filter-geoip-7.2.12-java/vendor/GeoLite2-ASN.mmdb
/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-filter-geoip-7.2.12-java/vendor/GeoLite2-City.mmdb   # 用这个
```

示例

```bash
[root@logstash1 vendor]#cat /etc/logstash/conf.d/tcp_to_stdout.conf 
input {
    tcp {
        port => "9527"
        host => "0.0.0.0"
        type => "tcplog"
        codec => json
        mode => "server"
    }
}


filter {
    grok {
        match => {
            "message" => "%{IPORHOST:client_ip} %{DATA:ident} %{DATA:user} /[%{HTTPDATE:timestamp}/] /"%{WORD:method} %{URIPATHPARAM:request} HTTP/%{NUMBER:http_version}/" %{NUMBER:status} %{NUMBER:bytes}" }
        }
    
    date {
        match => ["timestamp", "UNIX", "dd/MMM/yyyy:HH:mm:ss Z"]
        target => "@timestamp"        
        timezone => "Asia/Shanghai"
       }
    useragent {
        source => "message"
        target => "useragent"
      }

    geoip {
        # 新版的database字段必须添加
        database => "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-filter-geoip-7.2.12-java/vendor/GeoLite2-City.mmdb"
        # 8.x添加经纬度字段，用于后期画地图使用
        add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lon]}"]
        add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lat]}"]
        source => "client_ip"
        target => "geoip"
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 在nc所在服务器上输入日志信息，输入的日志信息的IP必须是公网IP
[root@web01 ~]#nc 10.0.0.106 9527
162.142.125.221 - - [15/Mar/2024:15:49:41 +0800] "GET / HTTP/1.1" 403 146 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)

# logstash上显示
{
           "bytes" => "146",
           "ident" => "-",
            "tags" => [
        [0] "_jsonparsefailure"
    ],
          "method" => "GET",
         "message" => "162.142.125.221 - - [15/Mar/2024:15:49:41 +0800] /"GET / HTTP/1.1/" 403 146 /"-/" /"Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)/"",
       "useragent" => {
            "os" => {
            "name" => "Other",
            "full" => "Other"
        },
        "device" => {
            "name" => "Other"
        },
          "name" => "Other"
    },
       "timestamp" => "15/Mar/2024:15:49:41 +0800",
       "client_ip" => "162.142.125.221",
           "geoip" => {
                "geo" => {
                    "location" => {
                "lon" => -97.822,
                "lat" => 37.751
            },
              "continent_code" => "NA",
                "country_name" => "United States",
            "country_iso_code" => "US",
                    "timezone" => "America/Chicago"
        },
                 "ip" => "162.142.125.221",
        # 这个是添加的字段，用于画图时使用的经纬度
        "coordinates" => [
            [0] "-97.822",
            [1] "37.751"
        ]
    },
      "@timestamp" => 2024-03-15T07:49:41.000Z,
        "@version" => "1",
            "type" => "tcplog",
            "user" => "-",
         "request" => "/",
    "http_version" => "1.1",
          "status" => "403"
}
```

只显示指定的geoip的字段信息

```bash
[root@logstash1 ~]#cat /etc/logstash/conf.d/tcp_to_stdout.conf 
input {
    tcp {
        port => "9527"
        host => "0.0.0.0"
        type => "tcplog"
        codec => json
        mode => "server"
    }
}


filter {
    grok {
        match => {
            "message" => "%{IPORHOST:client_ip} %{DATA:ident} %{DATA:user} /[%{HTTPDATE:timestamp}/] /"%{WORD:method} %{URIPATHPARAM:request} HTTP/%{NUMBER:http_version}/" %{NUMBER:status} %{NUMBER:bytes}" }
        }
    
    date {
        match => ["timestamp", "UNIX", "dd/MMM/yyyy:HH:mm:ss Z"]
        target => "@timestamp"        
        timezone => "Asia/Shanghai"
       }
    useragent {
        source => "message"
        target => "useragent"
      }

    geoip {
        database => "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-filter-geoip-7.2.12-java/vendor/GeoLite2-City.mmdb"
        add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lon]}"]
        add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lat]}"]
        source => "client_ip"
        target => "geoip"
        # 以上面提取clientip字段为源，获取地域信息，并指定只保留显示的字段
        fields => ["continent_code", "region_name", "city_name", "timezone", "longitude", "latitude"]
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 使用nc连接logstash服务器，并输入日志信息
[root@web01 ~]#nc 10.0.0.106 9527
118.123.105.92 - - [15/Mar/2024:11:33:18 +0800] "GET /favicon.ico HTTP/1.1" 404 548 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4 240.111 Safari/537.36"

# logstash服务器显示
[root@logstash1 ~]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/tcp_to_stdout.conf -r
{
            "tags" => [
        [0] "_jsonparsefailure"
    ],
      "@timestamp" => 2024-03-15T03:33:18.000Z,
       "timestamp" => "15/Mar/2024:11:33:18 +0800",
       "client_ip" => "118.123.105.92",
          "method" => "GET",
         "message" => "118.123.105.92 - - [15/Mar/2024:11:33:18 +0800] /"GET /favicon.ico HTTP/1.1/" 404 548 /"-/" /"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4 240.111 Safari/537.36/"",
    "http_version" => "1.1",
           "ident" => "-",
       "useragent" => {
          "name" => "favicon",
            "os" => {
            "name" => "Linux",
            "full" => "Linux"
        },
        "device" => {
            "name" => "Spider"
        }
    },
        "@version" => "1",
         "request" => "/favicon.ico",
            "type" => "tcplog",
            "user" => "-",
          "status" => "404",
           "geoip" => {
        "coordinates" => [
            [0] "104.0667",
            [1] "30.6667"
        ],
        
        # geo只显示指定字段
                "geo" => {
              "country_name" => "China",
            "continent_code" => "AS",
                  "location" => {
                "lat" => 30.6667,
                "lon" => 104.0667
            },
              "region_name" => "Sichuan",
                  "timezone" => "Asia/Shanghai"
        }
    },
           "bytes" => "548"
}

```

更新数据库地理位置

早期直接下载,现在必须注册登录后,在用户帐户页面下载

官网链接

```http
https://www.maxmind.com/en/home
```

![image-20250131145820821](../markdown_img/image-20250131145820821.png)

注册账号

![image-20250131145932129](../markdown_img/image-20250131145932129.png)

注册成功后，登录账户即可下载最新的数据

![image-20250131150023119](../markdown_img/image-20250131150023119.png)



![image-20250131150053981](../markdown_img/image-20250131150053981.png)



#### Date 插件

Date插件可以将日志中的指定的日期字符串对应的源字段生成新的目标字段

然后替换@timestamp 字段(此字段默认为当前写入logstash的时间而非日志本身的时间)或指定的其他字段

```bash
match         # 类型为数组，用于指定需要使用的源字段名和对应的时间格式
target        # 类型为字符串，用于指定生成的目标字段名，默认是 @timestamp
timezone      # 类型为字符串，用于指定时区域
```

官方说明

```http
https://www.elastic.co/guide/en/logstash/current/plugins-filters-date.html
```

时区格式参考

```http
http://joda-time.sourceforge.net/timezones.html
```

利用源字段timestamp生成新的字段名access_time

```bash
[root@logstash1 conf.d]# vim tcp_to_stdout.conf 
input {
    tcp {
        port => "9527"
        host => "0.0.0.0"
        type => "tcplog"
        codec => json
        mode => "server"
    }
}


filter {
    grok {
        match => {
            "message" => "%{IPORHOST:client_ip} %{DATA:ident} %{DATA:user} /[%{HTTPDATE:timestamp}/] /"%{WORD:method} %{URIPATHPARAM:request} HTTP/%{NUMBER:http_version}/" %{NUMBER:status} %{NUMBER:bytes}" }
        }
        
    #解析源字段timestamp的date日期格式: 14/Jul/2020:15:07:27 +0800
    date {
        match => ["timestamp", "dd/MMM/yyyy:HH:mm:ss Z" ] # 这里的时间格式必须和timestamp的实际格式匹配
        target => "access_time"         #将时间写入新生成的access_time字段，源字段仍保留
        #target => "@timestamp"         #将时间覆盖原有的@timestamp字段
        timezone => "Asia/Shanghai"
       }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 在另一台设备上nc 10.0.0.106 9527然后输入nginx的日志
[root@web01 ~]#nc 10.0.0.106 9527
10.0.0.102 - - [29/Jan/2025:22:55:08 +0800] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"

# 在logstash上会显示
{
           "bytes" => "612",
           "ident" => "-",
            "tags" => [
        [0] "_jsonparsefailure"
    ],
          "method" => "GET",
         "message" => "10.0.0.102 - - [29/Jan/2025:22:55:08 +0800] /"GET / HTTP/1.1/" 200 612 /"-/" /"curl/7.81.0/"",
       "timestamp" => "29/Jan/2025:22:55:08 +0800",
       "client_ip" => "10.0.0.102",
     "access_time" => 2025-01-29T14:55:08.000Z,          # 会将时间写入指定字段
      "@timestamp" => 2025-01-29T15:10:39.724041888Z,
        "@version" => "1",
            "type" => "tcplog",
            "user" => "-",
         "request" => "/",
    "http_version" => "1.1",
          "status" => "200"
}

# 如果target是@timestamp，则显示如下
{
           "bytes" => "612",
           "ident" => "-",
            "tags" => [
        [0] "_jsonparsefailure"
    ],
          "method" => "GET",
         "message" => "10.0.0.102 - - [29/Jan/2025:22:55:08 +0800] /"GET / HTTP/1.1/" 200 612 /"-/" /"curl/7.81.0/"",
       "timestamp" => "29/Jan/2025:22:55:08 +0800",
       "client_ip" => "10.0.0.102",
      "@timestamp" => 2025-01-29T14:55:08.000Z,        # @timestamp和timestamp相同
        "@version" => "1",
            "type" => "tcplog",
            "user" => "-",
         "request" => "/",
    "http_version" => "1.1",
          "status" => "200"
}
```



#### Useragent 插件

useragent 插件可以根据请求中的 user-agent 字段，解析出浏览器设备、操作系统等信息, 以方便后续的分析使用

```bash
[root@logstash ~]#cat /etc/logstash/conf.d/http_grok_useragent_stdout.conf
input {
    http {
        port => 6666
    }
}

filter {
    #将nginx日志格式化为json格式
    grok {
        match => {
            "message" => "%{IPORHOST:client_ip} %{DATA:ident} %{DATA:user} /[%{HTTPDATE:timestamp}/] /"%{WORD:method} %{URIPATHPARAM:request} HTTP/%{NUMBER:http_version}/" %{NUMBER:status} %{NUMBER:bytes}" }
        }
    }
    #解析date日期如: 10/Dec/2020:10:40:10 +0800
    date {
        match => ["timestamp", "dd/MMM/yyyy:HH:mm:ss Z" ]
        target => "@timestamp"
        #target => "access_time"
        timezone => "Asia/Shanghai"
    }
    #提取agent字段，进行解析
    useragent {
        #source => "agent"                    #7,X指定从哪个字段获取数据
        source => "message"                   #8.X指定从哪个字段获取数据
        #source => "[user_agent][original]"   #8.X指定从哪个字段获取数据,直接分析日志文件，curl或insomnia此方式不成功
        #source => "[user_agent][original][1]" #8.X指定从哪个字段获取数据，如果利用insomnia此方式不成功工具发送http请求，需要加[1]
        target => "useragent" #指定生成新的字典类型的字段的名称，包括os，device等内容
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# logstash上显示
{
           "bytes" => "396",
           "ident" => "-",
            "tags" => [
        [0] "_jsonparsefailure"
    ],
          "method" => "GET",
         "message" => "10.0.0.1 - - [29/Jan/2025:23:43:47 +0800] /"GET / HTTP/1.1/" 200 396 /"-/" /"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0/"",
       "useragent" => {
        "version" => "132.0.0.0",
             "os" => {
            "version" => "10",
               "name" => "Windows",
               "full" => "Windows 10"
        },
         "device" => {
            "name" => "Other"
        },
           "name" => "Edge"
    },
       "timestamp" => "29/Jan/2025:23:43:47 +0800",
       "client_ip" => "10.0.0.1",
      "@timestamp" => 2025-01-29T15:43:47.000Z,
        "@version" => "1",
            "type" => "tcplog",
            "user" => "-",
         "request" => "/",
    "http_version" => "1.1",
          "status" => "200"
}
```



#### Mutate 插件

官方链接

```http
https://www.elastic.co/guide/en/logstash/master/plugins-filters-mutate.html https://www.elastic.co/guide/en/logstash/7.6/plugins-filters-mutate.html
```

 Mutate 插件主要是对字段进行、类型转换、删除、替换、更新等操作,可以使用以下函数

```bash
remove_field   #删除字段
split          #字符串切割,相当于awk取列
add_field      #添加字段    
convert        #字符串替换
gsub           #类型转换，支持的数据类型：integer，integer_eu，float，float_eu，string，boolean 
rename         #字符串改名
lowercase      #转换字符串为小写 
```



##### remove_field 删除字段

```bash
[root@logstash1 ~]#cat /etc/logstash/conf.d/tcp_to_stdout.conf
input {
    tcp {
        port => "9527"
        host => "0.0.0.0"
        type => "tcplog"
        codec => json
        mode => "server"
    }
}


filter {
    grok {
        match => {
            "message" => "%{IPORHOST:client_ip} %{DATA:ident} %{DATA:user} /[%{HTTPDATE:timestamp}/] /"%{WORD:method} %{URIPATHPARAM:request} HTTP/%{NUMBER:http_version}/" %{NUMBER:status} %{NUMBER:bytes}" }
        }
    
    date {
        match => ["timestamp", "UNIX", "dd/MMM/yyyy:HH:mm:ss Z"]
        target => "@timestamp"        
        timezone => "Asia/Shanghai"
       }
    useragent {
        source => "message"
        target => "useragent"
      }

    geoip {
        database => "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-filter-geoip-7.2.12-java/vendor/GeoLite2-City.mmdb"
        add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lon]}"]
        add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lat]}"]
        source => "client_ip"
        target => "geoip"
        fields => ["continent_code", "country_name", "region_name", "timezone", "longitude", "latitude"]
    }
    # 删除指定字段
    mutate {
        remove_field => ["timestamp", "message"]
    }
}

output {
    stdout {
        codec => rubydebug
    }
}


# 使用nc连接logstash服务器，并输入日志信息
[root@web01 ~]#nc 10.0.0.106 9527
118.123.105.92 - - [15/Mar/2024:11:33:18 +0800] "GET /favicon.ico HTTP/1.1" 404 548 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4 240.111 Safari/537.36"

# logstash服务器显示
# 原来的timestamp和message都被删除了
{
            "tags" => [
        [0] "_jsonparsefailure"
    ],
      "@timestamp" => 2024-03-15T03:33:18.000Z,
          "method" => "GET",
       "client_ip" => "118.123.105.92",
    "http_version" => "1.1",
           "ident" => "-",
       "useragent" => {
          "name" => "favicon",
            "os" => {
            "name" => "Linux",
            "full" => "Linux"
        },
        "device" => {
            "name" => "Spider"
        }
    },
        "@version" => "1",
         "request" => "/favicon.ico",
            "type" => "tcplog",
            "user" => "-",
          "status" => "404",
           "geoip" => {
        "coordinates" => [
            [0] "104.0667",
            [1] "30.6667"
        ],
                "geo" => {
              "country_name" => "China",
            "continent_code" => "AS",
                  "location" => {
                "lat" => 30.6667,
                "lon" => 104.0667
            },
               "region_name" => "Sichuan",
                  "timezone" => "Asia/Shanghai"
        }
    },
           "bytes" => "548"
}
```



##### Split 切割

mutate 中的 split 字符串切割，指定字符做为分隔符，切割的结果用于生成新的列表元素

示例：1000|提交订单|2020-01-08 09:10:21

```bash
[root@logstash1 conf.d]#vim http_to_stdout.conf 
input {
    http {
        port => 6666
        codec => json
    }
}

filter {
    mutate {
        split => {"message" => "|"}
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 启动logstash
[root@logstash1 ~]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/http_to_stdout.conf -r

# 在另一台服务器上使用curl，携带请求体，访问10.0.0.106:6666
[root@web01 ~]#curl -XPOST -d '1000|提交订单|2020-01-08 09:10:21' http://10.0.0.106:6666
ok

# 在logstash服务器上显示
{
           "url" => {
          "path" => "/",
          "port" => 6666,
        "domain" => "10.0.0.106"
    },
      "@version" => "1",
    "@timestamp" => 2025-01-30T01:40:02.101039609Z,
    "user_agent" => {
        "original" => "curl/7.81.0"
    },
       "message" => [
        [0] "1000",
        [1] "提交订单",
        [2] "2020-01-08 09:10:21"
    ],
          "tags" => [
        [0] "_jsonparsefailure"
    ],
          "host" => {
        "ip" => "10.0.0.104"
    },
          "http" => {
        "version" => "HTTP/1.1",
         "method" => "POST",
        "request" => {
            "mime_type" => "application/x-www-form-urlencoded",
                 "body" => {
                "bytes" => "37"
            }
        }
    }
}
```



##### add_field 添加字段

用指定源字段添加新的字段，添加完成后源字段还存在

```bash
[root@logstash1 conf.d]#vim http_to_stdout.conf 
input {
    http {
        port => 6666
        codec => json
    }
}

filter {
    mutate {
        split => {"message" => "|"}
        # 添加字段，将message的列表的第0个元素添加字段名user_id...
        add_field => {
            "user_id" => "%{[message][0]}"
            "action" => "%{[message][1]}"
            "time" => "%{[message][2]}"
        }
        # 添加字段做索引名
        # add_field => {"[@metadata][target_index]" => "app-%{+YYY.MM.dd}"}
        # 删除无用字段
        remove_field => ["headers", "message"]
    }
}

output {
    stdout {
        codec => rubydebug
    }
}
```



##### convert 转换

mutate 中的 convert 可以实现数据类型的转换。 支持转换integer、float、string等类型

```bash
[root@logstash1 conf.d]#vim http_to_stdout.conf
input {
    http {
        port => 6666
        codec => json
    }
}

filter {
    mutate {
        split => {"message" => "|"}
        add_field => {
            "user_id" => "%{[message][0]}"
            "action" => "%{[message][1]}"
            "time" => "%{[message][2]}"
        }

        remove_field => ["headers", "message"]
        # 数据类型转换
        convert => {
            "user_id" => "integer"
            "action" => "string"
            "time" => "string"
        }
    }
}

output {
    stdout {
        codec => rubydebug
    }
}
```



##### gsub 替换

gsub 实现字符串的替换

```bash
filter {
    mutate {
        gsub=>["message","/n", " "] #将message字段中的换行替换为空格
    }
}
```



#### 条件判断

Filter 语句块中支持 if 条件判断功能

```bash
# vim /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/nginx/access.log
  tags: ["access"]
  
- type: log
  enabled: true
  paths:
  - /var/log/nginx/error.log
  tags: ["error"]
  
- type: log
  enabled: true
  paths:- /var/log/syslog
  tags: ["system"]
  
output.logstash:
  hosts: ["10.0.0.104:5044","10.0.0.105:5044"]
  #loadbalance: true        #负载均衡
  #worker: 2 #number of hosts * workers #开启多进程
  
# vim /etc/logstash/conf.d/filebeat_logstash_es.conf 
input {
    beats {
        port => 5044
    }
}

filter {
    if "access" in [tags][0] {
        mutate {
            add_field => {"target_index" => "access-%{+YYYY.MM.dd}"}
        }
    }
    else if "error" in [tags][0] {
        mutate {
            add_field => {"target_index" => "error-%{+YYYY.MM.dd}"}
        }
    }
    else if "system" in [tags][0] {
        mutate {
            add_field => {"target_index" => "system-%{+YYYY.MM.dd}"}
        }
    }

}

output {
    elasticsearch {
        hosts => ["10.0.0.100:9200", "10.0.0.101:9200", "10.0.0.102:9200"]
        index => "%{[target_index]}"
        template_overwrite => true   # 覆盖索引模版
    }
}
```

范例2：

```bash
# vim /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  enable: true
  paths:
  - /var/log/nginx/access/log
  fields:
    project: test-access
    env: test

output.logstash:
  hosts: ["10.0.0.104:5044", "10.0.0.105:5044"]
  
# vim /etc/logstash/conf.d/filebeat_logstash_es.conf 
input {
    beats {
        port => 5044
    }
    file {
        path => "/tmp/mystical.log"
        type => mysticallog   # 自定义类型，可用于条件判断
        start_position => "beginning"
        stat_interval => "3"
    }
}

output {
    if [fields][env] == "test" {
        elasticsearch {
            hosts => ["10.0.0.100:9200","10.0.0.101:9200","10.0.0.102:9200"]
            index => "test-nginx-%{+YYYY.MM.dd}"
        }
    }
    if [type] == "mysticallog" {
        stdout {
            codec => rubydebug
        }
    }
}
```



### Logstash 输出 Output插件

官方链接

```http
https://www.elastic.co/guide/en/logstash/7.6/output-plugins.html
```



#### Stdout 插件

stdout 插件将数据输出到屏幕终端，主要用于调试

```bash
output {
    stdout {
        codec => rubydebug
    }
}
```



#### File 插件

输出到文件，可以将分散在多个文件的数据统一存放到一个文件

示例: 将所有 web 机器的日志收集到一个文件中，从而方便统一管理

```bash
[root@ubuntu2204 ~]#cat /etc/logstash/conf.d/stdin_file.conf
input {
    stdin {}
}
output {
    stdout {
        codec => rubydebug
    }
    file {
        path => "/var/log/test.log"
    }
}
```



#### Elasticsearch 插件

官方说明

```http
https://www.elastic.co/guide/en/logstash/7.6/plugins-outputs-elasticsearch.html
```

索引的时间格式说明

```http
https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html
```

当日志量较小时，可以按月或周生成索引，当日志量比较大时，会按天生成索引，以方便后续按天删除

```bash
output {
    elasticsearch {
        hosts => ["10.0.0.100:9200", "10.0.0.101:9200", "10.0.0.102:9200"]  # 一般写ES中data节点地址
        index => "app-%{+YYYY.MM.dd}"               # 指定索引名称，建议加时间，按天建立索引
        # index => "%{[@metadata][target_index]}"   # 使用字段[metadata][target_index]值做为索引名
        template_overwrite => true                  # 覆盖索引模版，此项可选，默认值为false
    }
}
```

```ABAP
注意: 索引名必须为小写
```



#### Redis 插件

Logstash 支持将日志转发至 Redis

官方链接：

```http
https://www.elastic.co/guide/en/logstash/7.6/plugins-outputs-redis.html
```

范例

```bash
[root@logstash ~]#cat /etc/logstash/conf.d/file_to_redis.conf
input {
    file {
        path => "/var/log/nginx/access/log"
        type => 'nginx-accesslog'
        start_postion => "beginning"
        start_interval => "3"
        codec => json
    }
    stdin { }
}
output {
    if [type] == 'nginx-accesslog' {
        redis {
            host => 'Redis_IP'
            port => "6379"
            password => "123456"
            db => "0"
            data_type => 'list'
            key => "nginx-accesslog"
        }
    }
    stdout {
        codec => rubydebug
    }
}
```



#### Kafka 插件

Logstash 支持将日志转发至 Kafka

官方链接：

```http
https://www.elastic.co/guide/en/logstash/7.6/plugins-outputs-kafka.html
```

范例

```bash
[root@logstash ~]#cat /etc/logstash/conf.d/file_to_kafka.conf
input {
    file {
        path => "/var/log/nginx/access.log"
        type => 'nginx-accesslog'
        start_position => "beginning"
        start_interval => "3"
        codec => json
    }
    file {
        path => "/var/log/nginx/error.log"
        type => "nginx-errorlog"
        start_position => "beginning"
        start_interval => "3"
    }
}

output {
    # stdout {}
    if [type] == 'nginx-accesslog' {
        kafka {
           bootstrap_server => '10.0.0.105:9092,10.0.0.107:9092,10.0.0.108:9092'
           topic_id => 'nginx-accesslog'
           codec => 'json'   # 如果是Json格式，需要标识的字段
        }
    }
    if [type] == 'nginx-errorlog' {
        kafka {
           bootstrap_server => '10.0.0.105:9092,10.0.0.107:9092,10.0.0.108:9092'
           topic_id => 'nginx-errorlog'
           codec => 'json'  # 为了保留logstash添加的字段,比如:type字段,也需要指定json格式,否则会丢失logstash添加的字段
        }
    }
}
```





### Logstash 实战案例

#### 收集应用特定格式的日志输出至 Elasticsearch 并利用 Kibana 展示

![image-20250130105839369](../markdown_img/image-20250130105839369.png)

##### 应用日志收集项目说明

应用的日志格式如下

```bash
[root@web01 ~]#tail -n 10 mall_app.log 
[INFO] 2018-06-30 23:59:29 [www.mall.com] - DAU|2467|浏览页面|2018-06-30 05:41:24
[INFO] 2018-06-30 23:59:33 [www.mall.com] - DAU|2231|领取优惠券|2018-06-30 12:09:03
[INFO] 2018-06-30 23:59:35 [www.mall.com] - DAU|1808|提交订单|2018-06-30 04:48:33
[INFO] 2018-06-30 23:59:39 [www.mall.com] - DAU|3385|加入收藏|2018-06-30 15:32:12
[INFO] 2018-06-30 23:59:40 [www.mall.com] - DAU|937|评论商品|2018-06-30 08:10:35
[INFO] 2018-06-30 23:59:44 [www.mall.com] - DAU|6446|搜索|2018-06-30 12:55:40
[INFO] 2018-06-30 23:59:45 [www.mall.com] - DAU|4208|搜索|2018-06-30 06:43:24
[INFO] 2018-06-30 23:59:48 [www.mall.com] - DAU|76|查看订单|2018-06-30 09:50:37
[INFO] 2018-06-30 23:59:52 [www.mall.com] - DAU|2538|加入收藏|2018-06-30 06:58:41
[INFO] 2018-06-30 23:59:55 [www.mall.com] - DAU|9008|加入收藏|2018-06-30 13:56:26
```

将日志收集利用 Logstash 进行格式转换后发给 Elasticsearch,并利用Kibana展示



##### 实现过程

**配置filebeat**

```bash
[root@web01 ~]# cat /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/mall_app.log

output.logstash:
  hosts: ["10.0.0.106:6666"]
```

**配置 Logstash**

```bash
[root@logstash1 conf.d]#cat app_filebeat_fileter_es.conf 
input {
    beats {
        port => 6666
    }
}

filter {
    mutate {
        split => {"message" => "|"}
        add_field => {
            "user_id" => "%{[message][1]}"
            "action" => "%{[message][2]}"
            "time" => "%{[message][3]}"
        }

        remove_field => ["message"]
    
        convert => {
            "user_id" => "integer"
            "action" => "string"
            "time" => "string"
        }
    }

    date {
        match => ["time", "yyyy-MM-dd HH:mm:ss"]
        target => "@timestamp"
        timezone => "Asia/Shanghai"
    }
}

output {
    stdout {
        codec => rubydebug
    }
    elasticsearch {
        hosts => ["10.0.0.100:9200", "10.0.0.101:9200", "10.0.0.102:9200"]
        index => "mall-app-%{+YYYY.MM.dd}"
        template_overwrite => true
    }
}

 #启动，观察结果
 [root@logstash ~]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/app_filebeat_filter_es.conf -r
......
{
       "user_id" => "9008",
         "event" => {
        "original" => "[INFO] 2018-06-30 23:59:55 [www.mall.com] - DAU|9008|加入收藏|2018-06-30 13:56:26"
    },
         "input" => {
        "type" => "log"
    },
    "@timestamp" => 2018-06-30T05:56:26.000Z,
          "host" => {
        "name" => "web01"
    },
        "action" => "加入收藏",
          "time" => "2018-06-30 13:56:26",
      "@version" => "1",
           "log" => {
          "file" => {
            "path" => "/var/log/mall_app.log"
        },
        "offset" => 14313461
    },
           "ecs" => {
        "version" => "8.0.0"
    },
          "tags" => [
        [0] "beats_input_codec_plain_applied"
    ],
         "agent" => {
                  "id" => "52dc5551-3312-4428-9923-914dfa240323",
                "name" => "web01",
                "type" => "filebeat",
        "ephemeral_id" => "b4b84c1c-0e89-4c0c-bbfa-0921204f1a5f",
             "version" => "8.15.0"
    }
}
```

 **插件查看索引**

![image-20250130112114322](../markdown_img/image-20250130112114322.png)

注意：因为是历史数据，所以需要选择正确的时间段

![image-20250130112234029](../markdown_img/image-20250130112234029.png)



##### Kibana 展示

![image-20250130112342396](../markdown_img/image-20250130112342396.png)

![image-20250130112412257](../markdown_img/image-20250130112412257.png)

![image-20250130112438271](../markdown_img/image-20250130112438271.png)

![image-20250130112459217](../markdown_img/image-20250130112459217.png)

![image-20250130112521022](../markdown_img/image-20250130112521022.png)

![image-20250130112535573](../markdown_img/image-20250130112535573.png)

![image-20250130112557741](../markdown_img/image-20250130112557741.png)

![image-20250130112631559](../markdown_img/image-20250130112631559.png)

![image-20250130112652545](../markdown_img/image-20250130112652545.png)

![image-20250130112720311](../markdown_img/image-20250130112720311.png)



![image-20250130112804067](../markdown_img/image-20250130112804067.png)

![image-20250130112821255](../markdown_img/image-20250130112821255.png)

![image-20250130112919146](../markdown_img/image-20250130112919146.png)

后续根据上述方法，创建云图

![image-20250130113028284](../markdown_img/image-20250130113028284.png)

点击共享，可以将大屏共享到指定链接或者自己的html网站中

![image-20250130113117733](../markdown_img/image-20250130113117733.png)



# Kibana图形显示

## kibana介绍

Kibana 是一款开源的数据分析和可视化平台，它是 Elastic Stack 成员之一，设计用于和 Elasticsearch  协作,可以使用 Kibana 对 Elasticsearch 索引中的数据进行搜索、查看、交互操作,您可以很方便的利用 图表、表格及地图对数据进行多元化的分析和呈现。

Kibana 可以使大数据通俗易懂。基于浏览器的界面便于您快速创建和分享动态数据仪表板来追踪 Elasticsearch 的实时数据变化。

**Kibana 基于 TypeScript 语言开发**

Kibana 官方下载链接:

```http
https://www.elastic.co/cn/downloads/kibana
https://www.elastic.co/cn/downloads/past-releases#kibana
```

镜像网站下载链接

```http
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/
```



## 安装并配置 Kibana

可以通过包或者二进制的方式进行安装,可以安装在独立服务器,或者也可以和elasticsearch的主机安装在 一起

注意: Kibana的版本要和 Elasticsearch 相同的版本，否则可能会出错

官方说明：

```http
https://github.com/elastic/kibana
```

![image-20250121160534071](../markdown_img/image-20250121160534071.png)



### 包安装

基于性能原因，建议将Kibana安装到独立节点上，而非和ES节点复用

下载链接

```http
https://www.elastic.co/cn/downloads/kibana
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/
```



#### Ubuntu安装

```bash
[root@ubuntu2204 ~]#https://artifacts.elastic.co/downloads/kibana/kibana-8.6.1-amd64.deb

[root@ubuntu2204 ~]#wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/k/kibana/kibana-8.15.0-amd64.deb

[root@es-node1 ~]#wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/7.x/apt/pool/main/k/kibana/kibana-7.6.2-amd64.deb

[root@ubuntu2204 ~]# dpkg -i kibana-8.15.0-amd64.deb
```



#### CentOS安装

```bash
[root@es-node1 ~]#wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/7.x/yum/7.6.2/kibana-7.6.2-x86_64.rpm

[root@es-node1 ~]#yum localinstall kibana-7.6.2-x86_64.rpm
```



### 修改配置

```bash
[root@es-node1 ~]#vim /etc/kibana/kibana.yml 
[root@es-node1 ~]#grep "^[a-Z]" /etc/kibana/kibana.yml 

server.port: 5601  #监听端口,此为默认值
server.host: "0.0.0.0" #修改此行的监听地址,默认为localhost，即：127.0.0.1:5601

#修改此行,指向ES任意服务器地址或多个节点地址实现容错,默认为localhost
elasticsearch.hosts: 
["http://10.0.0.101:9200","http://10.0.0.102:9200","http://10.0.0.103:9200"] 

i18n.locale: "zh-CN"   #修改此行,使用"zh-CN"显示中文界面,默认英文

#8.X版本新添加配置,默认被注释,会显示下面提示
server.publicBaseUrl: "http://kibana.mystical.org"
```



#### 启动Kibana服务并验证

```bash
#默认没有开机自动启动，需要自行设置
[root@es-node1 ~]#systemctl enable --now kibana

# 查看端口
[root@ubuntu2204 ~]#ss -nlt
State       Recv-Q      Send-Q            Local Address:Port             Peer Address:Port      Process                           
LISTEN      0           511                     0.0.0.0:5601                  0.0.0.0:* 

# 在宿主机上添加hosts文件信息，然后浏览器登录：http://kibana.mystical.org:5601/
```

![image-20250121163026440](../markdown_img/image-20250121163026440.png)

**点击自己浏览**

![image-20250121163437711](../markdown_img/image-20250121163437711.png)

![image-20250121163608191](../markdown_img/image-20250121163608191.png)

![image-20250121163643228](../markdown_img/image-20250121163643228.png)

![image-20250121163717772](../markdown_img/image-20250121163717772.png)

**安装并连接Kibana后，Kibana会自动生成很多元数据索引，可以使用cerebro进行观看**

![image-20250121163907063](../markdown_img/image-20250121163907063.png)





# ELK综合实战案例

## Filebeat 收集Nginx日志并写入 Kafka 缓存发送至 Elasticsearch

### 环境准备

![image-20250130215315585](../markdown_img/image-20250130215315585.png)


```bash
#三台ES集群
10.0.0.100
10.0.0.101
10.0.0.102

#logstash
10.0.0.106 logstash1
10.0.0.107 logstash2

# kafka准备的单机
10.0.0.105
10.0.0.107
10.0.0.108

# filebeat和nginx
10.0.0.104
```

![image-20250131144641023](../markdown_img/image-20250131144641023.png)

### Filebeat 收集 Nginx 的访问和错误日志并发送至 kafka

```bash
[root@web01 nginx]#cat /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/nginx/mystical.access.log
  tags: ["nginx-access"]

- type: log
  enable: true
  paths:
  - /var/log/nginx/mystical.error.log
  tags: ["nginx-error"]

output.kafka:
  hosts: ["10.0.0.105:9092", "10.0.0.107:9092", "10.0.0.108:9092"]
  topic: nginx-log
  partition.round_robin:
    reachable_only: true
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000000
  
# 重启加载filebeat服务
[root@web01 ~]#systemctl restart filebeat.service 
```

查看kafka中的数据

![image-20250131103038074](../markdown_img/image-20250131103038074.png)



### 配置 Logstash 读取 Kafka 日志发送到 Elasticsearch

```bash
[root@logstash1 conf.d]#cat kafka-to-es.conf 
input {
    kafka {
        bootstrap_servers => "10.0.0.105:9092, 10.0.0.107:9092, 10.0.0.108:9092"
        topics => "nginx-log"
        consumer_threads => "3"
        codec => "json"
    }
}

filter {
    if "nginx-access" in [tags] {
            grok {
                match => {
                    "message" => "%{IPORHOST:client_ip} %{DATA:ident} %{DATA:user} /[%{HTTPDATE:timestamp}/] (?:%{QS:request}|%{DATA:raw_request}) %{NUMBER:status} %{NUMBER:bytes} %{QS:referer} %{QS:user_agent}"

                }
            }
            
            date {
                match => ["timestamp", "UNIX", "dd/MMM/yyyy:HH:mm:ss Z"]
                target => "@timestamp"        
                timezone => "Asia/Shanghai"
               }
            useragent {
                source => "message"
                target => "useragent"
              }
        
            geoip {
                database => "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-filter-geoip-7.2.12-java/vendor/GeoLite2-City.mmdb"
                add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lon]}"]
                add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lat]}"]
                source => "client_ip"
                target => "geoip"
                fields => ["continent_code", "country_name", "region_name", "timezone", "longitude", "latitude"]
            }
        
            mutate {
                remove_field => ["timestamp", "message"]
                convert => [ "[geoip][coordinates]", "float"]
            }
        

    } else if "nginx-error" in [tags] {
            grok {
                match => { 
                    "message" => "%{YEAR:year}/%{MONTHNUM:month}/%{MONTHDAY:day} %{TIME:time} /[%{WORD:log_level}/] %{NUMBER:pid}#%{NUMBER:worker_id}: /*%{NUMBER:request_id} %{WORD:action}/(/) /"%{DATA:file_path}/" %{WORD:status} /(%{NUMBER:error_code}: %{DATA:error_message}/), client: %{IP:client_ip}, server: %{DATA:server_name}, request: /"%{WORD:method} %{DATA:request_uri} HTTP/%{NUMBER:http_version}/", host: /"%{DATA:host}/""
                }
            }
            
        
            geoip {
                database => "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-filter-geoip-7.2.12-java/vendor/GeoLite2-City.mmdb"
                add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lon]}"]
                add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lat]}"]
                source => "client_ip"
                target => "geoip"
                fields => ["continent_code", "country_name", "region_name", "timezone", "longitude", "latitude"]
            }
        
            mutate {
                add_field => { "full_timestamp" => "%{year}-%{month}-%{day} %{time}" }
                remove_field => ["year", "message", "month", "day", "time"]
                convert => [ "[geoip][coordinates]", "float"]
          }
        
            date {
                match => [ "full_timestamp", "yyyy-MM-dd HH:mm:ss" ]
                target => "@timestamp"
                timezone => "Asia/Shanghai"
            }

    }
}

output {
    stdout {
        codec => rubydebug
    }
    
    if "nginx-access" in [tags] {
        elasticsearch {
            hosts => ["10.0.0.100:9200", "10.0.0.101:9200", "10.0.0.102:9200"]
            index => "logstash-kafka-nginx-accesslog-%{+YYYY.MM.dd}"
            template_overwrite => true
        }
    } else if "nginx-error" in [tags] {
        elasticsearch {
            hosts => ["10.0.0.100:9200", "10.0.0.101:9200", "10.0.0.102:9200"]
            index => "logstash-kafka-nginx-errorlog-%{+YYYY.MM.dd}"
            template_overwrite => true
        }
    }

}

# 启动logstash

```

也可以根据Kafka的图形工具，观察消息积压状况

![image-20250131144938030](../markdown_img/image-20250131144938030.png)

观察Kabana上的索引是否生成，如果有，说明elasticsearch成功接收数据

![image-20250131145127613](../markdown_img/image-20250131145127613.png)

创建视图

![image-20250131151836675](../markdown_img/image-20250131151836675.png)

![image-20250131151909764](../markdown_img/image-20250131151909764.png)

查看Discover，并做好调试

![image-20250131152050448](../markdown_img/image-20250131152050448.png)

![image-20250131152200659](../markdown_img/image-20250131152200659.png)

### Kibana 创建地图数据

对于区域地图、坐标地图、Coordinate Map之类的图形展示，新版的Kibana已经将其整合到了一个统 一的功能模块 Map.

通过左侧边栏的 analytics的Maps中来创建图形

```ABAP
ES8 要求地图数据类型geo_point类型，在logstash的地址信息的格式使用mutate（支持的数据类型：
integer，integer_eu，float，float_eu，string，boolean）可以转换成 float类型而不支持geo_point类
型，所以需要转换一下logstash在传递信息到es时候的模板信息，将地址信息转换成geo_point类型即可
```

解决方案：

- 获取模板
- 修改模板
- 使用模板



在开发工具执行下面指令，获取模版设置，复制mappings块中的所有内容

```bash
# 查看生成的索引信息
GET /logstash-kafka-nginx-accesslog-2022.03.02

#复制mappings开始的行到settings行之前结束,并最后再加一个 }
```

![image-20250131152645703](../markdown_img/image-20250131152645703.png)

![image-20250131152816851](../markdown_img/image-20250131152816851.png)

![image-20250131153228759](../markdown_img/image-20250131153228759.png)

![image-20250131153255307](../markdown_img/image-20250131153255307.png)

执行下面操作生成索引模板，将上面的mappings部分内容复制到下面，只修改"coordinates": {  "type":  "geo_point" } 部分

```bash
PUT /_template/template_nginx_accesslog
{
  "index_patterns" : [
    "logstash-kafka-nginx-accesslog-*" 
  ],
  "order" : 0,
  "aliases" : { },
  "mappings" {
  ...
   "geoip": {
          "properties": {
            "coordinates": {
              "type": "geo_point"    # 这里把类型改为geo_point
            },
  ......
  
} # 最后补一个 }
```

![image-20250131162509928](../markdown_img/image-20250131162509928.png)

查看生成的索引模板

![image-20250131162852511](../markdown_img/image-20250131162852511.png)

必须先删除旧有索引重新生成数据才能生

![image-20250131163151654](../markdown_img/image-20250131163151654.png)

重新生成数据，确认类型是否更改

![image-20250131165421406](../markdown_img/image-20250131165421406.png)

修改好数据类型后，重新导入数据，生成地图

![image-20250131165537145](../markdown_img/image-20250131165537145.png)

![image-20250131165644298](../markdown_img/image-20250131165644298.png)

![image-20250131165708987](../markdown_img/image-20250131165708987.png)

![image-20250131165838774](../markdown_img/image-20250131165838774.png)

![image-20250131165907568](../markdown_img/image-20250131165907568.png)

![image-20250131170134325](../markdown_img/image-20250131170134325.png)





## Logstash收集日志写入 MySQL 数据库

ES中的日志后续会被删除,但有些重要数据,比如状态码、客户端IP、客户端浏览器版本等，后期可以会按月或年做数据统计等,因此需要持久保存

可以将重要数据写入数据库达到持久保存目的

![image-20250131205922262](../markdown_img/image-20250131205922262.png)



###  安装 MySQL 数据库

```bash
[root@ubuntu2204 ~]#apt update && apt install -y mysql-server
# 查看端口
[root@ubuntu2204 ~]#ss -nlt    
LISTEN        0              70                         127.0.0.1:33060                      0.0.0.0:*      
LISTEN        0              151                        127.0.0.1:3306                       0.0.0.0:* 

# 公开端口
[root@ubuntu2204 ~]#sed -i  '/127.0.0.1/s/^/#/' /etc/mysql/mysql.conf.d/mysqld.cnf 
[root@ubuntu2204 ~]#systemctl restart mysql

# 再次查看端口
LISTEN        0              70                                 *:33060                            *:*       
LISTEN        0              151                                *:3306                             *:*   
```



### 创建库和表并授权用户登录

```bash
[root@ubuntu2204 ~]#mysql
mysql> create database elk;
Query OK, 1 row affected (0.02 sec)

mysql> create user elk@"10.0.0.%" identified by '123456';
Query OK, 0 rows affected (0.03 sec)

mysql> grant all privileges on elk.* to elk@"10.0.0.%";
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

#创建表,字段对应需要保存的数据字段
mysql> use elk;
Database changed

mysql> create table elklog (clientip varchar(39),bytes int,uri varchar(256),status char(3));
Query OK, 0 rows affected, 1 warning (0.03 sec)

# 查看创建的表
mysql> desc elklog;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| clientip     | varchar(39)  | YES  |     | NULL    |       |
| bytes        | int          | YES  |     | NULL    |       |
| uri          | varchar(256) | YES  |     | NULL    |       |
| status       | char(3)      | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
4 rows in set (0.01 sec)
```



###  测试用户从 Logstash 主机远程登录(可选)

```bash
[root@logstash1 ~]#mysql -uelk -h10.0.0.109 -p123456 -e "show databases";
mysql: [Warning] Using a password on the command line interface can be insecure.
+--------------------+
| Database           |
+--------------------+
| elk                |
| information_schema |
| performance_schema |
+--------------------+
```



### Logstash 配置 mysql-connector-java 包

MySQL Connector/J是MySQL官方JDBC驱动程序，JDBC（Java Data Base Connectivity,java数据库连接）是一种用于执行SQL语句的Java API，可以为多种关系数据库提供统一访问，它由一组用Java语言编 写的类和接口组成。

官方下载地址

```http
https://dev.mysql.com/downloads/connector/
```

![image-20250131220452111](../markdown_img/image-20250131220452111.png)

选择合适的版本

![image-20250131221154737](../markdown_img/image-20250131221154737.png)

![image-20250131221312513](../markdown_img/image-20250131221312513.png)

Ubuntu22.04 安装 mysql-connector

```bash
[root@logstash1 ~]#wget https://downloads.mysql.com/archives/get/p/3/file/mysql-connector-j_8.0.33-1ubuntu22.10_all.deb


# 安装
[root@logstash1 ~]#dpkg -i mysql-connector-j_8.0.33-1ubuntu22.10_all.deb 
正在选中未选择的软件包 mysql-connector-j。
(正在读取数据库 ... 系统当前共安装有 124632 个文件和目录。)
准备解压 mysql-connector-j_8.0.33-1ubuntu22.10_all.deb  ...
正在解压 mysql-connector-j (8.0.33-1ubuntu22.10) ...
正在设置 mysql-connector-j (8.0.33-1ubuntu22.10) ...

# 查看mysql-connector-j的jar包所在路径
[root@logstash1 ~]#dpkg -L mysql-connector-j
/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/mysql-connector-j
/usr/share/doc/mysql-connector-j/CHANGES.gz
/usr/share/doc/mysql-connector-j/INFO_BIN
/usr/share/doc/mysql-connector-j/INFO_SRC
/usr/share/doc/mysql-connector-j/LICENSE.gz
/usr/share/doc/mysql-connector-j/README
/usr/share/doc/mysql-connector-j/changelog.Debian.gz
/usr/share/doc/mysql-connector-j/copyright
/usr/share/java
/usr/share/java/mysql-connector-j-8.0.33.jar
/usr/share/java/mysql-connector-java-8.0.33.jar

# 查看
[root@logstash1 ~]#ll /usr/share/java/mysql-connector-j-8.0.33.jar /usr/share/java/mysql-connector-java-8.0.33.jar
-rw-r--r-- 1 root root 2481543  3月  8  2023 /usr/share/java/mysql-connector-j-8.0.33.jar
lrwxrwxrwx 1 root root      28  3月  8  2023 /usr/share/java/mysql-connector-java-8.0.33.jar -> mysql-connector-j-8.0.33.jar

# 复制jar文件到logstash指定的目录下
[root@logstash1 ~]#mkdir -p  /usr/share/logstash/vendor/jar/jdbc
[root@logstash1 ~]#cp /usr/share/java/mysql-connector-j-8.0.33.jar /usr/share/logstash/vendor/jar/jdbc/

# 此步可选
[root@logstash1 ~]#chown -R logstash.logstash /usr/share/logstash/vendor/jar/
[root@logstash1 ~]#ll  /usr/share/logstash/vendor/jar/jdbc/ -h
总计 2.4M
drwxr-xr-x 2 logstash logstash 4.0K  1月 31 22:17 ./
drwxr-xr-x 3 logstash logstash 4.0K  1月 31 22:16 ../
-rw-r--r-- 1 logstash logstash 2.4M  1月 31 22:17 mysql-connector-j-8.0.33.jar
```



### 安装logstash-output-jdbc插件

```bash
#查看安装拆插件,默认只有input-jdbc插件,需要安装output-jdbc插件
[root@logstash1 ~]#/usr/share/logstash/bin/logstash-plugin list|grep jdbc
......
logstash-integration-jdbc
├── logstash-input-jdbc
├── logstash-filter-jdbc_streaming
└── logstash-filter-jdbc_static
 
#在线安装output-jdbc插件,可能会等较长时间,20240524花10分钟
# 建议开代理翻墙下载
# 选做
[root@logstash1 ~]#vim .bashrc
export http_proxy=http://10.0.0.1:10809
export https_proxy=http://10.0.0.1:10809

# 开始下载
[root@logstash1 ~]#/usr/share/logstash/bin/logstash-plugin install  logstash-output-jdbc
Using bundled JDK: /usr/share/logstash/jdk
Validating logstash-output-jdbc
Resolving mixin dependencies
Installing logstash-output-jdbc
Installation successful

#离线安装方法
#如果无法在线安装,可以先从已经安装的主机导出插件,再导入
#导出插件
[root@ubuntu2204 ~]#/usr/share/logstash/bin/logstash-plugin prepare-offline-pack logstash-output-jdbc
Using bundled JDK: /usr/share/logstash/jdk
Offline package created at: /usr/share/logstash/logstash-offline-plugins-8.6.1.zip

 You can install it with this command `bin/logstash-plugin install file:///usr/share/logstash/logstash-offline-plugins-8.6.1.zip`

#离线导入插件
[root@ubuntu2204 ~]#/usr/share/logstash/bin/logstash-plugin install file:///usr/share/logstash/logstash-offline-plugins-8.6.1.zip
Using bundled JDK: /usr/share/logstash/jdk
Installing file: /usr/share/logstash/logstash-offline-plugins-8.6.1.zip
Resolving dependencies..................................
Install successful

#检查插件安装成功
[root@logstash1 ~]#/usr/share/logstash/bin/logstash-plugin list|grep jdbc
logstash-integration-jdbc
 ├── logstash-input-jdbc
 ├── logstash-filter-jdbc_streaming
 └── logstash-filter-jdbc_static
logstash-output-jdbc

#删除插件
[root@logstash1 ~]#/usr/share/logstash/bin/logstash-plugin remove logstash-output-jdbc
```



### 配置 Filebeat 配置文件

```bash
[root@web01 ~]#cat /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/nginx/mystical.access.log
  tags: ["nginx-access"]

- type: log
  enable: true
  paths:
  - /var/log/nginx/mystical.error.log
  tags: ["nginx-error"]

output.kafka:
  hosts: ["10.0.0.105:9092", "10.0.0.107:9092", "10.0.0.108:9092"]
  topic: nginx-log
  partition.round_robin:
    reachable_only: true
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000000
```



### 配置 Logstash 将日志写入数据库

```bash
[root@logstash1 conf.d]#cat kafka-to-es.conf 
input {
    kafka {
        bootstrap_servers => "10.0.0.105:9092, 10.0.0.107:9092, 10.0.0.108:9092"
        topics => "nginx-log"
        consumer_threads => "3"
        codec => "json"
    }
}

filter {
    if "nginx-access" in [tags] {

            grok {
                match => {
                    "message" => "%{IPORHOST:client_ip} %{DATA:ident} %{DATA:user} /[%{HTTPDATE:timestamp}/] (?:%{QS:request}|%{DATA:raw_request}) %{NUMBER:status} %{NUMBER:bytes} %{QS:referer} %{QS:user_agent}"

                }
            }
            
            date {
                match => ["timestamp", "UNIX", "dd/MMM/yyyy:HH:mm:ss Z"]
                target => "@timestamp"        
                timezone => "Asia/Shanghai"
               }
            useragent {
                source => "message"
                target => "useragent"
              }
        
            geoip {
                database => "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-filter-geoip-7.2.12-java/vendor/GeoLite2-City.mmdb"
                add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lon]}"]
                add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lat]}"]
                source => "client_ip"
                target => "geoip"
                fields => ["continent_code", "country_name", "region_name", "timezone", "longitude", "latitude"]
            }
        
            mutate {
                remove_field => ["timestamp", "message"]
                convert => [ "[geoip][coordinates]", "float"]
            }
        

    } else if "nginx-error" in [tags] {
            grok {
                match => { 
                    "message" => "%{YEAR:year}/%{MONTHNUM:month}/%{MONTHDAY:day} %{TIME:time} /[%{WORD:log_level}/] %{NUMBER:pid}#%{NUMBER:worker_id}: /*%{NUMBER:request_id} %{WORD:action}/(/) /"%{DATA:file_path}/" %{WORD:status} /(%{NUMBER:error_code}: %{DATA:error_message}/), client: %{IP:client_ip}, server: %{DATA:server_name}, request: /"%{WORD:method} %{DATA:request_uri} HTTP/%{NUMBER:http_version}/", host: /"%{DATA:host}/""
                }
            }
            
        
            geoip {
                database => "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-filter-geoip-7.2.12-java/vendor/GeoLite2-City.mmdb"
                add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lon]}"]
                add_field => ["[geoip][coordinates]", "%{[geoip][geo][location][lat]}"]
                source => "client_ip"
                target => "geoip"
                fields => ["continent_code", "country_name", "region_name", "timezone", "longitude", "latitude"]
            }
        
            mutate {
                add_field => { "full_timestamp" => "%{year}-%{month}-%{day} %{time}" }
                remove_field => ["year", "message", "month", "day", "time"]
                convert => [ "[geoip][coordinates]", "float"]
          }
        
            date {
                match => [ "full_timestamp", "yyyy-MM-dd HH:mm:ss" ]
                target => "@timestamp"
                timezone => "Asia/Shanghai"
            }

    }
}

output {
    stdout {
        codec => rubydebug
    }
    
    if "nginx-access" in [tags] {
        elasticsearch {
            hosts => ["10.0.0.100:9200", "10.0.0.101:9200", "10.0.0.102:9200"]
            index => "logstash-kafka-nginx-accesslog-%{+YYYY.MM.dd}"
            template_overwrite => true
        }
 
        jdbc {
            connection_string => "jdbc:mysql://10.0.0.109/elk?user=elk&password=123456&useUnicode=true&characterEncoding=UTF8"
            statement => ["INSERT INTO elklog (clientip,bytes,uri,status) VALUES(?,?,?,?)","client_ip","bytes","request","status"]
    }
      

    } else if "nginx-error" in [tags] {
        elasticsearch {
            hosts => ["10.0.0.100:9200", "10.0.0.101:9200", "10.0.0.102:9200"]
            index => "logstash-kafka-nginx-errorlog-%{+YYYY.MM.dd}"
            template_overwrite => true
        }
    }

}
```



### 检查 Logstash 配置并重启服务

```bash
[root@logstash1 ~]#/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/kafka-to-es.conf -t
[root@logstash1 ~]#systemctl restart logstash.service
```



### 访问 Nginx 产生日志

```bash
# 为方便测试，手动追加数据至日志文件
[root@web01 nginx]#cat mysql.test.log >> mystical.access.log
```



### 验证数据库是否写入数据

```bash
mysql> select * from elklog;
+-----------------+-------+------------------------------------------------------------------------------+--------+
| clientip        | bytes | uri                                                                          | status |
+-----------------+-------+------------------------------------------------------------------------------+--------+
| 178.20.42.24    |     5 | "GET / HTTP/1.1"                                                             | 301    |
| 109.205.213.198 |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 40.77.167.181   |   134 | "GET /robots.txt HTTP/2.0"                                                   | 200    |
| 220.196.160.146 |     0 | "GET / HTTP/2.0"                                                             | 301    |
| 185.196.220.253 |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 101.35.250.82   |    31 | "POST /wp-cron.php?doing_wp_cron=1738280215.6015350818634033203125 HTTP/1.1" | 200    |
| 54.36.149.15    | 12380 | "GET /computer-composition-principles/ HTTP/2.0"                             | 200    |
| 182.44.9.147    |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 220.196.160.83  |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 54.36.148.212   | 14113 | "GET /tag/base/ HTTP/2.0"                                                    | 200    |
| 66.249.75.44    |   145 | "GET /robots.txt HTTP/1.1"                                                   | 200    |
| 146.19.24.168   |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 185.242.226.155 | 18498 | "GET / HTTP/1.1"                                                             | 200    |
| 46.19.143.58    |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 180.101.245.252 |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 66.249.69.102   |     5 | "GET /robots.txt HTTP/1.1"                                                   | 301    |
| 120.237.87.26   |   145 | "GET /robots.txt HTTP/1.1"                                                   | 200    |
| 178.20.42.24    | 76858 | "GET / HTTP/1.1"                                                             | 200    |
| 51.254.49.101   |     5 | "GET / HTTP/1.1"                                                             | 301    |
| 37.19.223.24    |     0 | "GET / HTTP/1.0"                                                             | 301    |
| 220.196.160.144 |     5 | "GET / HTTP/1.1"                                                             | 301    |
| 59.83.208.105   |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 195.3.223.55    |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 220.196.160.65  |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 85.208.96.196   |   145 | "GET /robots.txt HTTP/1.1"                                                   | 200    |
| 51.195.148.211  |  3818 | "POST /wp-login.php HTTP/1.1"                                                | 200    |
| 59.83.208.107   | 18492 | "GET / HTTP/2.0"                                                             | 200    |
| 51.8.102.58     |   134 | "GET /robots.txt HTTP/2.0"                                                   | 200    |
| 66.249.75.44    | 18497 | "GET / HTTP/1.1"                                                             | 200    |
| 220.196.160.53  | 18498 | "GET / HTTP/2.0"                                                             | 200    |
| 31.202.47.201   |   162 | "GET / HTTP/1.1"                                                             | 301    |
| 182.44.9.147    | 18508 | "GET / HTTP/1.1"                                                             | 200    |
| 101.35.250.82   |    31 | "POST /wp-cron.php?doing_wp_cron=1738283189.4807469844818115234375 HTTP/1.1" | 200    |
| 66.249.69.100   |     5 | "GET / HTTP/1.1"                                                             | 301    |
+-----------------+-------+------------------------------------------------------------------------------+--------+
34 rows in set (0.00 sec)
```

