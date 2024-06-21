# iptables

## iptables是什么

iptables是Netfilter的用户空间工具

```shell
┌──────────────────┐
│    User Space    │
│                  │
│    iptables      │
│    (管理工具)     │
└───────▲──────────┘
        │
        │
┌───────┴──────────┐
│    Kernel Space  │
│                  │
│     Netfilter    │
│   (数据包处理框架)│
└──────────────────┘
```
用户不能直接控制内核空间，因此需要有一个在用户空间的工具通过提供的API接口，对内核空间进行控制
这里这个工具就是iptables，Netfilter是内核空间的数据包处理框架，它提供一系列API接口，
在iptables上配置规则，iptables通过API接口将规则传递给内核空间的Netfilter（数据包处理框架），从而让用户在用户空间实现对内核空间网路数据包的控制


## Netfilter是什么

Netfilter是一个内核的数据包处理框架，他通过5个hook函数来对数据包进行处理，这些hook函数在网络栈的不同阶段被触发，通过对这些hook函数设置规则，来实现在不同阶段对数据包进行指定的操作

而这些规则由用户空间的iptables传递给Netfilter



## 关于Netfilter和iptables的概念和关系

Netfilter是内核的数据包处理框架，他通过5个hook点在数据包的不同处理阶段对其进行操作。

这5个hook点分别是
- PREROUTING
- INPUT
- FORWARD
- OUTPUT
- POSTROUTING


分别在数据包到达，输入，转发，输出和发送的阶段触发，
用户可以通过iptables在用户空间配置规则，这些规则定义了如何在各个钩子点处理这些数据包。这些规则通过iptables工具传递给Netfilter，并由Netfilter在适当的钩子点上应用


## 四表五链中，表是什么，作用是什么，链是什么，作用是什么

表是iptables中的逻辑结构，用于组织规则。
表（tables） 是逻辑上的分组，用于组织不同类型的规则

### 表与钩子的关系
每个钩子点可以引用多个表中的规则链，从而实现对数据包的多方面处理。例如：

- PREROUTING 钩子 
        - 可以引用 nat 表中的 PREROUTING 链来进行 DNAT 操作，
        - 也可以引用 mangle 表中的 PREROUTING 链来修改数据包属性。
- INPUT 钩子 
        - 可以引用 filter 表中的 INPUT 链来实现防火墙过滤，
        - 也可以引用 mangle 表中的 INPUT 链来修改包的某些属性。
- OUTPUT 钩子 
        - 可以引用 nat 表中的 OUTPUT 链来进行地址转换，
        - 也可以引用 filter 表中的 OUTPUT 链来实现流量控制。

### 为什么需要这些表？
- 灵活性：不同的表有不同的用途，组织不同类型的规则，使得规则的管理和查找更为高效。
- 功能区分：每个表专注于特定类型的数据包操作，比如 filter 表专注于允许或拒绝数据包，nat 表专注于地址转换。
- 优化：通过将规则分配到不同的表，可以减少规则匹配的复杂性，提高数据包处理的效率。


### 常用的表

- filter: 负责对数据包进行过滤
- nat： 主要负责数据包的网路地址转换，主要包括：SNAT，DNAT
- mangle：主要用于修改数据包的内容
- security: hatred-selinux 略



