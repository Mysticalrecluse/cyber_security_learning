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

表是iptables中的逻辑结构，用于组织规则。不同的表通过对不同的钩子点的不同规则进行整合，实现不同的用户和功能