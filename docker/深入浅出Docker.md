# 走进Docker
## Docker简介
### Docker公司

Docker公司位于旧金山，由法裔美籍开发者和企业家Solumon Hykes创立

Docker公司起初是一家名为dotcloud的Paas提供商

#### Docker出现的原因

dotCloud（早期的docker公司），其底层技术上，dotCloud平台利用Linux容器技术。为了方便`创建和管理`这些容器,dotCloud开发了一套内部工具，之后被命名为Docekr。Docker就这样诞生了

```
Tip:
"Docker"一词来自英国口语，意为码头工人(Docker Worker)，即从船上卸货的工人
```

### Docker运行时与编排引擎

多数技术人员在谈到Docker时，主要是指Docker引擎

Docker引擎是用于运行和编排容器的基础设施工具。

大多数其他Docker公司或第三方的产品都是围绕Docker引擎进行开发和集成的。Docker引擎位于中心，其他产品基于Docker引擎的核心功能进行集成（比如：K8S）


### Docker开源项目（Moby）

"Docker一词也会用于指代开源Docker项目。其中包含一系列可以从Docker官网下载和安装的工具（`比如Docker服务端和客户端`）

Docker项目在2017年于Austin举办的DockerCon上被正式命名为Moby项目

由于这次改名，GitHub上的docker/docker库也被转移到了moby/moby

#### Moby项目的目标

Moby项目的目标是基于开源的方式，发展成Docker上游，并将Docker拆分成更多的模块化组件。Moby项目托管于GitHub的Moby代码库，包括子项目和工具列表

核心的Docker引擎项目位于GitHub的moby/moby，但是引擎中的代码正在持续被拆分和模块化

多数项目及其工具都是基于Golang编写的

### 容器生态

Docker公司的一个核心哲学通常被称为"含电池，但可拆卸"(Batteries included but removable)

意思是许多Docker内置的组件都是可以替换为第三方的组件。

### 开放容器计划 OCI(The Open Container Initiative)

OCI是一个旨在对`容器基础架构中的基础组件`进行标准化的管理委员会

OCI发布了两份规范(标准)：镜像规范和运行时规范