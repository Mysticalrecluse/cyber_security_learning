# - 课程目标



- 熟悉 OpenStack 架构，熟悉每个组件的作用和基础配置
- 能够独立完成 OpenStack 集群的部署和外部服务的对接
- 能够根据公司的实际需求设计出符合环境的 OpenStack 集群架构



# 课程目录



- OpenStack 简介
- OpenStack 环境搭建
- Keystone 服务详解
- Placement 服务详解
- Ceph 分布式存储介绍
- Cephadm 搭建 Ceph 集群
- Ceph 核心技术和组件介绍
- Ceph 集群存储服务配置
- Glance 服务详解
- Clinder 服务详解
- Neutron 服务详解
- Nova 服务详解
- 高可用集群搭建和配置
- 其他常用服务介绍
  - Skyline
  - Octavia
  - Trove



# OpenStack 简介



## 虚拟化技术的演进



## CPU运行级别

### CPU 运行级别是什么？

CPU 运行级别，本质上是 **CPU 为了保护系统安全，把代码（机器指令）分成不同权限等级来执行**。

例如：

```asm
mov eax, 1
cli            ; 关闭中断（特权指令）
hlt            ; 停机（特权指令）
out 0x64, al   ; I/O 操作（特权指令）
```

>  CPU判断权限，是在执行这些指令的时候判断的。



在 x86 架构里，经典权限等级叫 **Ring**，一共有 4 个：

```bat
Ring 0：最高权限
Ring 1
Ring 2
Ring 3：最低权限
```

最常见的是：

```bat
Ring 0：操作系统内核
Ring 3：普通用户程序
```

Ring 1 和 Ring 2 在现代主流操作系统里基本很少用。



### 为什么要有 CPU 运行级别？

因为一台机器上运行很多程序，不能让普通应用随便操作硬件。

比如普通程序如果能直接执行这些操作：

```bat
修改页表
直接操作磁盘控制器
关闭中断
修改 CPU 控制寄存器
直接访问任意物理内存
```

那系统就乱套了。

所以 CPU 规定：

```bat
普通应用程序运行在 Ring 3
操作系统内核运行在 Ring 0
```

普通程序想访问硬件，必须通过 **系统调用** 进入内核。

示例：

```bat
用户程序 read()
    ↓ 系统调用
Linux 内核
    ↓ 驱动程序
磁盘 / 网卡 / 文件系统
```



### Ring 0 和 Ring 3 的核心区别

#### Ring 0：内核态

Ring 0 代码可以执行特权指令。

示例：
```bat
管理内存
管理进程
管理中断
管理页表
访问硬件设备
执行 I/O 指令
```

Linux 内核就是运行在 Ring 0。

#### Ring 3：用户态

Ring 3 代码权限低，不能直接操作硬件。

普通程序如：

```bat
nginx
mysql
redis
java 程序
python 程序
shell 命令
```

通常都运行在 Ring 3。

如果它们需要访问硬件，需要通过系统调用：

```bat
用户态程序
    ↓ syscall
内核态
    ↓ 驱动
硬件
```



### 虚拟化为什么和 CPU 运行级别有关？

正常情况下，一台物理机只有一个操作系统内核运行在 Ring 0。

```bat
App          Ring 3
OS Kernel    Ring 0
Hardware
```

但是虚拟化要做什么？它要在一台物理机上运行多个操作系统。

例如：

```bat
物理机上运行：
- VM1：CentOS
- VM2：Ubuntu
- VM3：Windows
```

每个虚拟机里的操作系统都以为自己是“真正的操作系统”，都想运行在 Ring 0。

那么问题来了：

```bat
真正的 Ring 0 只能由谁占？
```

如果 Guest OS 也直接运行在 Ring 0，那它就可能直接控制物理硬件，破坏宿主机和其他虚拟机。

所以虚拟化的核心问题就是：

```bat
如何让 Guest OS 以为自己在 Ring 0，但实际上不能真正控制物理硬件？
```



### 传统 x86 虚拟化的困难

早期 x86 架构有个问题：不是所有敏感指令（特权指令）都会触发异常。

理想情况下，如果 Guest OS 执行特权指令：

```bat
修改页表
操作中断
访问设备
```

CPU 应该立刻陷入 **Hypervisor**，由 Hypervisor 接管。这叫：

```bat
trap and emulate
陷入并模拟
trap = 陷入 Hypervisor
emulate = 由 Hypervisor 模拟执行
```

但是早期 x86 有些指令在低权限下执行时，不会正常 trap，而是静默失败或行为异常。这导致早期 x86 不太适合直接做传统全虚拟化。

所以后来出现了三种方案：

```bat
1. 软件全虚拟化
2. 半虚拟化
3. 硬件支持的全虚拟化
```





#### 补充：Hypervisor 是什么？

Hypervisor = “比操作系统更高一层的控制者”，它的职责是：

- 控制 CPU / 内存 / 设备
- 设备虚拟化
- 并把这些资源“分配”给多个虚拟机
- 隔离不同虚拟机

直观理解 Hypervisor：

正常情况下：

```bat
App
↓
OS（Linux）  ← 控制硬件
↓
Hardware
```

虚拟化之后：

```bat
VM里的App
↓
VM里的OS（Guest OS）
↓
Hypervisor（真正控制硬件）
↓
Hardware
```

关键点：

- Guest OS 以为自己在控制硬件
- 实际上是 Hypervisor 在控制

> Hypervisor 是“类别”，不是“单一程序”。就像操作系统（OS）不是一个程序，而是一类系统（Linux、Windows、FreeBSD…）



##### 常见的 Hypervisor 举例

举例之前，我们先将虚拟化场景分为两种情况



**情况1：Type-1 Hypervisor（裸机型）**

例如：

- Xen
- ESXi

结构：

```bat
Guest OS
↓
Hypervisor
↓
Hardware
```

> 这时候你可以说：Hypervisor 在“资源控制”这件事上，确实类似内核



**情况2：Type-2 / KVM**

结构是：

```bat
QEMU（用户态）
↓
Linux Kernel（+ KVM 模块）
↓
Hardware
```

> 关键点来了：KVM 不是一个独立的 Hypervisor，它是 Linux 内核的一部分。



对于上述两种架构来说：

**Type-1（裸机型）的常见 Hypervisor**

- VMware ESXi
- Xen
- Hyper-V（本质接近）



**Type-2 / KVM（你最重要）**

- KVM（Linux 内核模块）
- VirtualBox
- VMware Workstation

> 从这种角度可以说：KVM 是一种 Hypervisor 的实现
>
> 但这里有一个坑在于，完整的虚拟化系统不全是由KVM解决的，KVM仅仅是处理内核模块，而用户态是由QEMU处理的



**KVM（内核态）**

负责：

- CPU 虚拟化（VM Entry / Exit）
- 内存虚拟化（EPT）
- vCPU 调度接口



**QEMU（用户态）**

负责：

- 设备模拟（磁盘 / 网卡）
- 虚拟机进程管理
- 镜像加载
- BIOS/固件



所以更准确的说：

```bat
KVM 提供“虚拟 CPU + 内存能力”
QEMU 提供“虚拟设备 + 虚拟机外壳”
```



## 虚拟化层级



### 软件全虚拟化

软件全虚拟化就是：

```bat
不修改 Guest OS
完全靠虚拟化软件模拟一台完整计算机
```

Guest OS 不知道自己运行在虚拟机里。

例如：

```bat
Guest OS 以为自己在操作真实 CPU、内存、磁盘、网卡
实际上这些都是虚拟化软件模拟出来的
```



**典型代表**

早期 VMware 就大量使用软件全虚拟化技术。



**它怎么解决 Ring 0 问题？**

因为 Hypervisor 需要掌握最高权限，所以一般让 Hypervisor 占据真正的 Ring 0。Guest OS 不能真正运行在 Ring 0，只能被放到较低权限级别。

可以理解为：

```bat
Guest App       Ring 3
Guest Kernel    Ring 1 / 受限环境
Hypervisor      Ring 0
Hardware
```

但是 Guest OS 以为自己在 Ring 0。当 Guest OS 执行敏感指令时，虚拟化软件通过：

- 二进制翻译
- 动态指令替换
- 陷入模拟

把危险操作拦截下来。



**二进制翻译是什么意思？**

比如 Guest OS 原本想执行：

```bat
直接修改 CPU 控制寄存器
```

虚拟化软件不能让它直接执行，于是提前把这段指令翻译成安全代码：

```bat
Guest 原始指令
    ↓
Hypervisor 改写后的安全指令
    ↓
由 Hypervisor 模拟执行
```

所以软件全虚拟化的核心是：

```bat
Guest OS 不用改
Hypervisor 很辛苦
性能开销较大
```



### 半虚拟化

半虚拟化就是：

```bat
修改 Guest OS，让它知道自己运行在虚拟机里
```

Guest OS 不再假装自己可以直接控制硬件，而是主动调用 Hypervisor 提供的接口。

这个接口叫：

```bat
hypercalls 超级调用
```

类似于普通程序调用系统调用：

```bat
普通程序 → syscall → OS Kernel
Guest OS → hypercall → Hypervisor
```





### 硬件支持的全虚拟化

硬件支持的全虚拟化就是：

```bat
CPU 本身增加虚拟化能力
让 Guest OS 可以更自然地运行
```

典型技术：

```bat
Intel VT-x
AMD-V
```

Linux KVM 就依赖这些 CPU 虚拟化扩展。



#### **它解决了什么问题？**

它解决了早期 x86 不好虚拟化的问题。

CPU 新增了专门的虚拟化运行模式，让 Hypervisor 和 Guest OS 可以分层运行。

Intel 里常见说法是：

```bat
VMX root mode
VMX non-root mode
```

可以简单理解为：

```bat
Hypervisor 运行在 VMX root mode
Guest OS 运行在 VMX non-root mode
```

注意：这里不要简单理解为 Guest OS 只是 Ring 1。

在硬件虚拟化下，Guest OS 可以认为自己运行在 Ring 0，但这个 Ring 0 是受 VMX non-root 限制的。



#### 硬件虚拟化下的运行级别关系

传统没有虚拟化时：

```bat
App             Ring 3
OS Kernel       Ring 0
Hardware
```

硬件虚拟化后：

```bat
Guest App       Guest Ring 3
Guest Kernel    Guest Ring 0
--------------------------------
Hypervisor      VMX root mode
Hardware
```

关键点是：

```bat
Guest Kernel 可以运行在自己的 Ring 0
但它处于 VMX non-root mode
真正能控制物理硬件的是 Hypervisor
```

所以可以理解为 CPU 又加了一层更高的控制权。

以前只有：

```bat
Ring 0 > Ring 3
```

现在变成：

```bat
VMX root mode > VMX non-root mode
```

在 VMX non-root mode 里面，Guest OS 还可以有自己的 Ring 0 和 Ring 3。



#### VM Exit 和 VM Entry

硬件虚拟化最核心的机制是：

```
VM Exit
VM Entry
```

**1. VM Entry**

Hypervisor 把 CPU 切换进虚拟机执行 Guest OS。

```bat
Hypervisor
    ↓ VM Entry
Guest OS 开始运行
```

**2. VM Exit**

Guest OS 执行某些敏感操作时，CPU 自动退出虚拟机，回到 Hypervisor。

```bat
Guest OS 执行敏感操作
    ↓ CPU 触发 VM Exit
Hypervisor 接管处理
```

例如：

```bat
访问特殊寄存器
处理中断
访问某些 I/O 端口
操作页表
访问虚拟设备
```





在硬件支持的全虚拟化中，CPU 实际有两层权限体系：

第一层（虚拟化层）

```bat
VMX root mode       ← Hypervisor
VMX non-root mode   ← Guest（包括 Guest Ring0 和 Ring3）
```

第二层（Guest 内部）

```bat
Guest Ring0（Guest Kernel）
Guest Ring3（Guest App）
```

关键结论

```bat
Guest Ring0 虽然是“0”，但它在 VMX non-root 模式下，所以它不是真正的最高权限。
```

当 Guest OS 执行到受控区域后，在越界时会被 CPU 强制交给 Hypervisor 处理。



**举例说明：**

场景：Guest 内核写磁盘

Guest 里：

```bata
write()
→ Guest Kernel
→ 虚拟磁盘设备
```

实际发生了：

```bat
1. Guest Kernel 写设备寄存器（MMIO）
2. CPU 检测到：这是受控区域
3. 触发 VM Exit
4. 切到 Hypervisor（KVM）
5. KVM → QEMU 模拟磁盘
6. 写入宿主机文件
7. VM Entry 回 Guest
```

这里关键：

```bat
Guest 没有“调用 Hypervisor”，而是被拦截。
```



### 半虚拟化与硬件支持的全虚拟化区别

半虚拟化依赖 Guest OS 主动通过 hypercall 与 Hypervisor 协作，属于**软件层面的显式调用机制**；

而硬件支持的全虚拟化依赖 CPU 的虚拟化扩展（如 VT-x/AMD-V），当 Guest 执行受控操作或发生特定事件时，由 CPU 自动触发 VM Exit，将控制权切换到 Hypervisor，属于**硬件级别的强制切换机制**（Guest 并不知情）。



### 三种虚拟化方式对比

| 类型             | Guest OS 是否需要修改 | 依赖硬件虚拟化  | 性能 | 代表                      |
| ---------------- | --------------------- | --------------- | ---- | ------------------------- |
| 软件全虚拟化     | 不需要                | 不依赖          | 较低 | 早期 VMware               |
| 半虚拟化         | 需要                  | 不一定          | 较高 | Xen PV                    |
| 硬件支持全虚拟化 | 不需要                | 需要 VT-x/AMD-V | 高   | KVM、现代 VMware、Xen HVM |



### 它们和 CPU 运行级别的核心关联

可以总结成一句话：

```
虚拟化的本质问题之一，就是谁能占据真正的最高 CPU 权限。
```

**软件全虚拟化**

```bat
Hypervisor 占 Ring 0
Guest OS 被降权运行
危险指令靠软件翻译和模拟
```

**半虚拟化**

```bat
Hypervisor 占 Ring 0
Guest OS 被修改后主动调用 Hypervisor
减少危险指令直接执行
```

**硬件支持全虚拟化**

```bat
CPU 增加 VMX root / non-root 模式
Guest OS 可以在虚拟环境里运行自己的 Ring 0
Hypervisor 仍然拥有最终控制权
```





## KVM的出现

### KVM简史

2007年，KVM 最初由以色列的公司 Qumranet 开发，在 2007 年 2 月被正式合入 Linux 2.6.20 版本的内核中，随着内核一起发行。

2008年，2008 年 9 月红帽公司收购了 Qumranel，开始在 RHEL 中使用 KVM 替换 Xen，从 RHEL6 开始，KVM 成为默认的虚拟化引擎。

### KVM架构

KVM依赖于CPU提供的硬件虚拟化功能，因此必须在具备 Intel-VT 和 AMD-VT 功能的 X86 平台上运行，它的核心组件包括：

- 内核模块 kvm.ko（根据平台可能是 kvm-intel.ko 或 kvm-amd.ko）
- qemu-kvm，提供设备模拟功能；
- Libvirt，开源虚拟化管理工具。

<img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260501231338500.png" alt="image-20260501231338500" style="zoom:150%;" />



### KVM 的优势

和其他虚拟化产品相比，KVM 主要具备下面几个优势：

- 开源免费
- 强大的技术支持，跟随Linux 内核一起发行，RedHat 提供商业支持
- 性能强大，配置简单



## OpenStack 的出现

### OpenStack 简介

随着虚拟化技术的快速发展，各大公司都陆续推出了自己的虚拟化产品，同时期国内实际上已经有很多云服务厂商基于 KVM 开发出了自己的云服务并推出了自己的商业化产品，例如当时国内比较有名的云厂商西部数码，他们的产品就是在 KVM 之上开发出的一套虚拟机管理系统对外提供云资源的售卖。

在 2010 年，RackSpace 公司和美国国家航空航天局（NASA）合作，RackSpace 公司贡献出了自己的云文件平台代码，NASA 贡献出了自己的 Nebula 平台代码，以 Apache 许可证开源了 OpenStack。

此后随着 OpenStack 的快速迭代，除了少数自研的厂家，国内外的云服务厂商都陆陆续续切换到了 OpenStack 平台上。



### OpenStack 组件

随着 OpenStack 的快速发展，OpenStack 的各大服务组件陆续成熟，形成以 6 大组件为核心，其他组件为附加的格局。

6 大核心组件是：

- 认证组件 Keystone
- 计算组件 Nova
- 网络组件 Neutron
- 存储组件 Cinder
- 镜像组件 Glance
- 面板组件 Horizon



附加组件则是根据自己公司实际需要来采用，例如：

- 计量和监控组件 Telemetry
- 编排组件 Heat
- 物理机管理 Ironic
- 等等



### OpenStack 架构

OpenStack 几大组件协作基础架构图如下所示：

<img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260501232920577.png" alt="image-20260501232920577" style="zoom:150%;" />

当前 Swift 也就是给 Glance 提供后端存储的服务，已经被淘汰了。



### OpenStack 简史

**2010年**

RackSpace 公司和美国国家航空航天局（NASA）合作，RackSpace 公司贡献出了自己的云文件平台代码，NASA 贡献出了自己的 Nebula 平台代码，以 Apache 许可证开源了 OpenStack。
 OpenStack 第一个版本 Austin，以美国得克萨斯州 Texas 首府命名，第一个版本只有 Swift 和 Nova 两个组件；



**2011年**

2月，发布第二个版本 Bexar，新增了 Glance 组件提供镜像服务；
4月，发布第三个版本 Cactus，提高稳定性，同时 Ubuntu 宣布全面支持 OpenStack；
9月，发布第四个版本 Diablo，OpenStack 社区计划发行节奏为每半年一次；



**2012年**

4月，发布第五个版本 Essex，新增了 Horizon 和 Keystone 组件。Debian 7.0 宣布集成 Essex，红帽公司宣布集成 Essex 并发布了包含 OpenStack 的第一个预览版
9月，发布第六个版本 Folsom，同时将 Nova 项目中的网络模块和块存储模块剥离，成立新的核心项目 Quantum 和 Cinder；

**2013年**

4月，发布第7个版本 Grizzly，红帽公司宣布在它的商业化版本中提供对 OpenStack 的全面商业化支持；
10月，发布第8个版本 Havana，提出集成项目的概念，并集成 Ceilometer 和 Heat 这两个组件；



## Openstack 的组件命名风格

OpenStack 的组件命名，其实很多都带有一种：

**“宇宙 / 天文 / 工业” 命名风格**

比如：

- Nova（新星）→ 计算
- Neutron（中子）→ 网络
- Keystone（拱心石）→ 认证
- Glance（快速一瞥）→ 镜像
- Horizon（地平线）→ Dashboard
- Ceilometer（高度计）→ 监控
- Heat（热量）→ 编排

- Cinder（余烬）-> 存储



### 为什么存储组件叫 Cinder？

因为：

Cinder 指的是：

```ABAP
燃烧后剩下的炽热煤渣
```

例如：

- 火炉里的余烬
- 燃烧后的矿渣
- 仍然发热的块状物

OpenStack 社区当时给它起这个名字：

是为了呼应 Nova

因为：

Nova = 恒星爆发

而：

Cinder = **恒星燃烧后的残骸/余烬**

有一种：**“天体燃烧后的物质”** 这种意境。

但更深层一点：

Cinder 本质负责：

“持久化块存储”

也就是：

- VM 关闭后
- 数据仍然存在

类似：**火焰熄灭后仍存在的余烬**



其实你会发现：

**OpenStack 早期社区很“理想主义工程师文化”**

命名：

- 文艺
- 工程感
- 科幻感
- Unix Hacker 风格

比较浓。

不像现在很多云产品：

```ABAP
CloudBlockStorageService
```

这种企业化命名。



### Glance 为什么叫 Glance？

glance 的英文意思：

```ABAP
一瞥
快速浏览
扫一眼
```

而：

Glance 是 OpenStack 的镜像服务

它负责：

- 管理镜像
- 查询镜像
- 获取镜像元数据
- 给 Nova 提供镜像下载

例如：

```ABAP
ubuntu.qcow2
centos.qcow2
```

为什么叫 “Glance”？因为镜像本质上是：“系统模板”

而用户通常：

- 浏览镜像
- 选择镜像
- 快速查看镜像信息

像：**看商品列表** 一样。

所以，“一眼看过去”，这个感觉很贴切。

还有更深一层：Nova 创建虚拟机时：

实际上会：

```ABAP
向 Glance 查询镜像
```

这个动作很像：

```ABAP
“看一眼镜像仓库”
```

因此：Glance 更强调：“镜像目录与发现”

而不是：镜像存储本身



### Neutron 为什么叫 Neutron（中子）？

这个更有意思。neutron 是什么？

物理里的：中子

特点：

- 不带电
- 存在于原子核
- 参与维持结构稳定
- 是粒子间的重要组成部分



#### 为什么网络组件叫 Neutron？

因为：网络本质上“连接一切”

OpenStack 里：

- VM
- Router
- DHCP
- Floating IP
- VXLAN
- SDN

全部都靠：网络把它们组织起来。而中子（Neutron）在物理世界也是：**“维持原子结构的重要粒子”**

所以：OpenStack 网络组件用了

```ABAP
Neutron
```

表达：**“云平台中的连接核心”**，还有一个更现实的原因最早 OpenStack 网络组件不叫 Neutron。叫 Quantum

后来因为 Quantum 名字商标冲突，于是改名 Neutron。



#### 为什么继续走粒子命名？

因为：Quantum（量子）本来就是 微观粒子世界 于是改成：Neutron（中子）

还能保持：

- 物理学风格
- 科幻风格
- 粒子体系风格

社区就接受了。所以：Quantum → Neutron 其实是 “被迫改名但尽量保留原气质” 。

你会发现 OpenStack 整体很像：“宇宙工程学”

- Nova
  - 新星爆发 → 计算资源爆发

- Neutron
  - 连接粒子结构 → 网络连接

- Cinder 
  - 燃烧后的余烬 → 持久存储

- Swift
  - 快速流动 → 对象存储

- Horizon
  - 地平线 → 用户看到的平台入口

- Keystone
  - 拱心石 → 所有服务认证核心

- Heat
  - 热量/能量 → 编排引擎

- Ceilometer
  - 高度计 → 监控计量

所以：OpenStack 的命名体系，本质是一种 “科幻工程师文化”

这个在：

- Linux
- BSD
- OpenStack
- 早期 Docker
- Ceph

这些项目里其实都挺常见。



## 重点：图解虚拟化

![image-20260528144245013](D:\git_repository\cyber_security_learning\markdown_img\image-20260528144245013.png)

### Openstack虚拟机完整启动流程

```ABAP
openstack server create vm1
```

![image-20260528145110180](D:\git_repository\cyber_security_learning\markdown_img\image-20260528145110180.png)



# OpenStack 部署

## 前期准备

- 控制节点（4核8G，双网卡，一个能通外网，一个内网能连通，硬盘50G）
- 计算节点（4核8G，双网卡，一个能通外网，一个内网能连通，计算节点需要比控制节点多两个300G的硬盘，也就是一共3块硬盘，一块50G，两块300G）

- 两个网卡设计为：一个Bridge，一个Host-only

- 部署版本：**2023.2 Bobcat** OpenStack
- 操作系统：**Rocky9 / Ubuntu2204**

```bat
注意：
Rocky 9 可以稳定学习和部署 OpenStack，但 Rocky 10 目前太新，生态兼容性还不成熟；相比 Ubuntu 的 Cloud Archive 强绑定版本，Rocky/RHEL 系由于企业生态更保守，版本兼容问题通常没那么激进，但仍然需要关注 OpenStack 对应的 RDO/Kolla-Ansible 支持情况。

Ubuntu与OpenStack的版本对应关系
Ubuntu版本	 推荐OpenStack版本
22.04	      Bobcat / Antelope / Caracal
24.04	      Caracal（默认） / Dalmatian

否则容易出现：
- 依赖冲突
- 包不兼容
- RabbitMQ/Ceph版本问题
```





### 准备数据库密码

```bash
# 生成16位随机密码的指令
[root@computer1 ~]# openssl rand -base64 24 | tr -dc 'A-Za-z0-9@#%+=' | head -c 16; echo
```

| 组件                  | 密码             | 备注          |
| --------------------- | ---------------- | ------------- |
| 集群管理员            | JzycczIrOmPZsa8u | 用户admin     |
| 数据库mariadb         | ceSCVcUTyFaSdy9o | 用户root      |
| 消息队列 rabbitmq     | xN4UFkpayBbNH1zS | 用户openstack |
| keystone数据库        | KOLTUX8tNP81uWtN | 用户keystone  |
| placement数据库       | lvIB6W1DtVT1X3IQ | 用户placement |
| placement用户         | ROaTaWKNcTjjqDkF |               |
| glance数据库          | P4Sh2ixq24gSsvRn | 用户glance    |
| glance用户            | WqddBWi6QXbMMXjk |               |
| cinder数据库          | 7t0u7vVSeiHs+3OT | 用户cinder    |
| cinder用户            | bDtsOxVMlh9Nr7IL |               |
| neutron数据库         | KBifilr+NxW+jVDC | 用户neutron   |
| neutron用户           | JwqzZOmggKXUJDvO |               |
| metadata proxy secret | uj19FdS9DIGklYED |               |
| nova数据库            | zHs5DOM4S+2OhJN8 | 用户nova      |
| nova用户              | ac5RpUjzywMqhuqZ |               |



### 配置主机名

```bash
[root@controller1 ~]# hostnamectl set-hostname gz-controller1.mystical.org
[root@computer1 ~]# hostnamectl set-hostname gz-computer1.mystical.org
```



### 配置域名解析

```bash
# controller1节点配置
[root@controller1 ~]# vim /etc/hosts
192.168.100.200 gz-controller1.mystical.org gz-controller1
192.168.100.201 gz-computer1.mystical.org gz-computer1

# # computer1节点配置
[root@controller1 ~]# vim /etc/hosts
192.168.100.200 gz-controller1.mystical.org gz-controller1
192.168.100.201 gz-computer1.mystical.org gz-computer1
```





### 安装时间同步服务 Chrony

```bash
[root@controller ~]# yum makecache && yum install -y chrony
[root@computer1 ~]# yum makecache && yum install -y chrony

# 查看
[root@controller ~]# systemctl status chronyd
● chrony.service - chrony, an NTP client/server
     Loaded: loaded (/usr/lib/systemd/system/chrony.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-05-06 02:11:30 UTC; 39min ago
       Docs: man:chronyd(8)
             man:chronyc(1)
             man:chrony.conf(5)
   Main PID: 35008 (chronyd)
      Tasks: 2 (limit: 9377)
     Memory: 1.4M (peak: 2.4M)
        CPU: 172ms
     CGroup: /system.slice/chrony.service
             ├─35008 /usr/sbin/chronyd -F 1
             └─35009 /usr/sbin/chronyd -F 1

May 06 02:11:30 controller systemd[1]: Starting chrony.service - chrony, an NTP client/>
May 06 02:11:30 controller chronyd[35008]: chronyd version 4.5 starting (+CMDMON +NTP +>
May 06 02:11:30 controller chronyd[35008]: Loaded 0 symmetric keys
May 06 02:11:30 controller chronyd[35008]: Frequency 12.114 +/- 0.602 ppm read from /va>
May 06 02:11:30 controller chronyd[35008]: Using right/UTC timezone to obtain leap seco>May 06 02:11:30 controller chronyd[35008]: Loaded seccomp filter (level 1)
May 06 02:12:04 controller chronyd[35008]: Selected source 139.199.214.202 (0.ubuntu.po>
May 06 02:12:04 controller chronyd[35008]: System clock TAI offset set to 37 seconds

# 新版 chrony 默认不再配置 allow，是因为默认更偏客户端模式。对于小规模或云环境，所有机器直接同步公网 NTP 完全可行；但在中大型生产环境中，通常仍会部署内网统一 NTP 时间源，以降低公网依赖和时间漂移。

# 更改主节点配置，使其允许从节点连接
[root@controller ~]# vim /etc/chrony/chrony.conf
# 最下方添加
allow 192.168.0.0/16

# 更改从节点配置
[root@computer1 ~]# vim /etc/chrony/chrony.conf
pool 192.168.100.200        iburst maxsources 4
#pool ntp.ubuntu.com        iburst maxsources 4
#pool 0.ubuntu.pool.ntp.org iburst maxsources 1
#pool 1.ubuntu.pool.ntp.org iburst maxsources 1
#pool 2.ubuntu.pool.ntp.org iburst maxsources 2

# 查看
[root@computer1 ~]# chronyc
chrony version 4.5
Copyright (C) 1997-2003, 2007, 2009-2023 Richard P. Curnow and others
chrony comes with ABSOLUTELY NO WARRANTY.  This is free software, and
you are welcome to redistribute it under certain conditions.  See the
GNU General Public License version 2 for details.

chronyc> sourcestats 
Name/IP Address            NP  NR  Span  Frequency  Freq Skew  Offset  Std Dev
==============================================================================
192.168.100.200             5   3    70     -2.615    119.630    -37us   368us
chronyc> exit
```



### 关闭防火墙

```bash
# Ubuntu 关闭防火墙
[root@controller ~]# systemctl disable --now ufw
[root@computer1 ~]# systemctl disable --now ufw

# 注意：Rocky 的话需要关闭SELINUX
[root@computer1 ~]# systemctl disable --now firewalld
[root@computer1 ~]# setenforce 0
[root@computer1 ~]# cat /etc/selinux/config 
SELINUX=disabled
```



## OpenStack实验环境基础包安装

```bash
# 下载Openstack源
[root@computer1 ~]# yum install -y centos-release-openstack-bobcat

# 替换国内源
[root@computer1 ~]# sed -i 's/metalink=/#metalink=/g' /etc/yum.repos.d/CentOS-OpenStack-bobcat.repo 
[root@computer1 ~]# sed -i 's/#baseurl=/baseurl=/g' /etc/yum.repos.d/CentOS-OpenStack-bobcat.repo 

# 安装Openstack客户端
[root@computer1 ~]# yum install -y python-openstackclient

# 查看
[root@controller1 ~]# openstack --version
openstack 6.3.0

# 安装数据库组件
[root@controller1 ~]# yum install mariadb mariadb-server python3-PyMySQL -y

# 启动数据库
[root@controller1 ~]# systemctl start mariadb

# 查看状态
[root@controller1 ~]# systemctl status mariadb
● mariadb.service - MariaDB 10.5 database server
     Loaded: loaded (/usr/lib/systemd/system/mariadb.service; disabled; preset: disable>     Active: active (running) since Wed 2026-05-06 12:14:01 CST; 21s ago
       Docs: man:mariadbd(8)
             https://mariadb.com/kb/en/library/systemd/
    Process: 5227 ExecStartPre=/usr/libexec/mariadb-check-socket (code=exited, status=0>    Process: 5249 ExecStartPre=/usr/libexec/mariadb-prepare-db-dir mariadb.service (cod>    Process: 5355 ExecStartPost=/usr/libexec/mariadb-check-upgrade (code=exited, status>   Main PID: 5336 (mariadbd)
     Status: "Taking your SQL requests now..."
      Tasks: 18 (limit: 48716)
     Memory: 83.1M
        CPU: 236ms
     CGroup: /system.slice/mariadb.service
             └─5336 /usr/libexec/mariadbd --basedir=/usr

5月 06 12:14:01 controller1 mariadb-prepare-db-dir[5288]: The second is mysql@localhost>
5月 06 12:14:01 controller1 mariadb-prepare-db-dir[5288]: you need to be the system 'my>
5月 06 12:14:01 controller1 mariadb-prepare-db-dir[5288]: After connecting you can set >
5月 06 12:14:01 controller1 mariadb-prepare-db-dir[5288]: able to connect as any of the>
5月 06 12:14:01 controller1 mariadb-prepare-db-dir[5288]: See the MariaDB Knowledgebase>
5月 06 12:14:01 controller1 mariadb-prepare-db-dir[5288]: Please report any problems at>
5月 06 12:14:01 controller1 mariadb-prepare-db-dir[5288]: The latest information about >
5月 06 12:14:01 controller1 mariadb-prepare-db-dir[5288]: Consider joining MariaDB's st>
5月 06 12:14:01 controller1 mariadb-prepare-db-dir[5288]: https://mariadb.org/get-invol>
5月 06 12:14:01 controller1 systemd[1]: Started MariaDB 10.5 database server.

# MySQL初始化
[root@controller1 ~]# mysql_secure_installation

NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!

In order to log into MariaDB to secure it, we'll need the current
password for the root user. If you've just installed MariaDB, and
haven't set the root password yet, you should just press enter here.

# 当前密码：<空>，因此直接回车
Enter current password for root (enter for none): 
OK, successfully used password, moving on...

Setting the root password or using the unix_socket ensures that nobody
can log into the MariaDB root user without the proper authorisation.

You already have your root account protected, so you can safely answer 'n'.

# 不使用 unix_socket 认证
# 这里我们使用密码认证
Switch to unix_socket authentication [Y/n] n
 ... skipping.

You already have your root account protected, so you can safely answer 'n'.

# 修改root密码，使用上述表格的密码
Change the root password? [Y/n] y
New password: 
Re-enter new password: 
Password updated successfully!
Reloading privilege tables..
 ... Success!


By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

# 移除匿名用户，直接回车
Remove anonymous users? [Y/n] 
 ... Success!

Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

# 禁止root远程登录，直接回车
Disallow root login remotely? [Y/n] 
 ... Success!

By default, MariaDB comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.

# 移除测试表
Remove test database and access to it? [Y/n] 
 - Dropping test database...
 ... Success!
 - Removing privileges on test database...
 ... Success!

Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

# 重新加载权限表
Reload privilege tables now? [Y/n] 
 ... Success!

Cleaning up...

All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

Thanks for using MariaDB!

# 修改数据库配置
# 增加最大连接数配置
[root@controller1 ~]# vim /etc/my.cnf
[mysqld]
max_connection = 1024

# 安装消息队列
[root@controller1 ~]# yum install rabbitmq-server -y

# 启动并设置为开机自启
[root@controller1 ~]# systemctl enable --now rabbitmq-server

# 查看
[root@controller1 ~]# systemctl status rabbitmq-server

# 添加 rabbitmq 用户
[root@controller1 ~]# rabbitmqctl add_user openstack xN4UFkpayBbNH1zS
Adding user "openstack" ...
Done. Don't forget to grant the user permissions to some virtual hosts! See 'rabbitmqctl help set_permissions' to learn more.

# 给 openstack 用户设置权限
[root@controller1 ~]# rabbitmqctl set_user_tags openstack administrator
Setting tags for user "openstack" to [administrator] ...

# 设置路有权限
[root@controller1 ~]# rabbitmqctl set_permissions -p "/" openstack ".*" ".*" ".*"
Setting permissions for user "openstack" in vhost "/" ...

# 查看权限设置
[root@controller1 ~]# rabbitmqctl list_users
Listing users ...
user    tags
openstack       [administrator]
guest   [administrator]

# 安装 memcached
# 用于openstack 存储后端 token
[root@controller1 ~]# yum install -y memcached python3-memcached

# 需改配置
[root@gz-controller1 ~]# cat /etc/sysconfig/memcached 
PORT="11211"
USER="memcached"
MAXCONN="1024"
CACHESIZE="512"     # 这里改成512
OPTIONS="-l 127.0.0.1,::1,gz-controller1"  # 监听在gz-controller1域名上

# 启动并启用开机自启
[root@gz-controller1 ~]# systemctl enable --now memcached
Created symlink /etc/systemd/system/multi-user.target.wants/memcached.service → /usr/lib/systemd/system/memcached.service.

# 登录并创建8个数据库
[root@gz-controller1 ~]# mysql -u root -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 10.5.29-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> create database keystone default character set utf8;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> create database placement default character set utf8;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> create database glance default character set utf8;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> create database neutron default character set utf8;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> create database cinder default character set utf8;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> create database nova default character set utf8;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> create database nova_api default character set utf8;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> create database nova_cell0 default character set utf8;
Query OK, 1 row affected (0.000 sec)  

MariaDB [(none)]> grant all privileges on keystone.* to keystone@'192.168.100.%' identified by 'KOLTUX8tNP81uWtN';
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> grant all privileges on glance.* to glance@'localhost' identified by 'P4Sh2ixq24gSsvRn';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> grant all privileges on glance.* to glance@'192.168.100.%' identified by 'P4Sh2ixq24gSsvRn';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> grant all privileges on cinder.* to cinder@'192.168.100.%' identified by '7t0u7vVSeiHs+3OT';
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> grant all privileges on cinder.* to cinder@'localhost' identified by '7t0u7vVSeiHs+3OT';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> grant all privileges on neutron.* to 'neutron'@'localhost' identified by 'KBifilr+NxW+jVDC';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> grant all privileges on neutron.* to 'neutron'@'192.168.100.%' identified by 'KBifilr+NxW+jVDC';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> grant all privileges on nova_api.* to 'nova'@'localhost' identified by 'zHs5DOM4S+2OhJN8';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> grant all privileges on nova_api.* to 'nova'@'192.168.100.%' identified by 'zHs5DOM4S+2OhJN8';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> grant all privileges on nova.* to 'nova'@'localhost' identified by 'zHs5DOM4S+2OhJN8';
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> grant all privileges on nova.* to 'nova'@'192.168.100.%' identified by 'zHs5DOM4S+2OhJN8';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> grant all privileges on nova_cell0.* to 'nova'@'localhost' identified by 'zHs5DOM4S+2OhJN8';
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> grant all privileges on nova_cell0.* to 'nova'@'192.168.100.%' identified by 'zHs5DOM4S+2OhJN8';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> flush privileges;
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> grant all privileges on keystone.* to keystone@'localhost' identified by 'KOLTUX8tNP81uWtN';
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> grant all privileges on placement.* to placement@'192.168.100.%' identified by 'lvIB6W1DtVT1X3IQ';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> grant all privileges on placement.* to placement@'localhost' identified by 'lvIB6W1DtVT1X3IQ';
Query OK, 0 rows affected (0.000 sec)
```



## OpenStack控制节点安装和配置

```bash
# 控制节点打开crb仓库，因为OpenStack部分组件依赖于crb仓库的服务
[root@gz-computer1 ~]# vim /etc/yum.repos.d/rocky.repo
[crb]
name=Rocky Linux $releasever - CRB
#mirrorlist=https://mirrors.rockylinux.org/mirrorlist?arch=$basearch&repo=CRB-$releasever$rltype
baseurl=https://mirrors.aliyun.com/rockylinux/$releasever/CRB/$basearch/os/
gpgcheck=1
enabled=1
countme=1
metadata_expire=6h
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-9

[root@gz-computer1 ~]# yum makecache

# 安装 OpenStack 所有组件的软件包
[root@gz-computer1 ~]# yum install -y openstack-keystone httpd mod_wsgi openstack-placement-api openstack-glance openstack-cinder openstack-neutron openstack-neutron-ml2 openstack-neutron-linuxbridge openstack-nova openstack-dashboard
```



### Keystone配置

OpenStack 中 Keystone 是认证服务，负责分发 token。这里的 token 本质上是 “登录后的身份凭证”

#### Token 在 HTTP 里长什么样？

openstack API 请求：

```http
X-Auth-Token: gAAAAAB...
```

这个 X-Auth-Token 就是 Keystone 发的 Token。

而 Keystone 用来存放 Token 的后端服务就是 memcached

```bash
# 打开 keystone 的配置文件 /etc/keystone/keystone.conf，需要修改的配置如下所示
[root@gz-controller1 ~]# vim /etc/keystone/keystone.conf 
[database]
#...
# 数据库+驱动://连接地址
# 连接地址 = 账号:密码@主机名/数据库名称
connection = mysql+pymysql://keystone:glrKEib48VYPZBjO@controller/keystone
#...
[cache]
# 指定后端存放token的连接池
backend = oslo_cache.memcache_pool
enabled = true
memcache_servers = localhost:11211

# 根据 Keystone 当前版本的数据库迁移脚本，在 MySQL/MariaDB 中创建或升级 Keystone 所需要的表结构。
[root@gz-controller1 ~]# keystone-manage db_sync
2026-05-06 17:53:44.517 24793 INFO alembic.runtime.migration [-] Context impl MySQLImpl.2026-05-06 17:53:44.517 24793 INFO alembic.runtime.migration [-] Will assume non-transactional DDL.
2026-05-06 17:53:44.524 24793 INFO alembic.runtime.migration [-] Running upgrade  -> 27e647c0fad4, Initial version.
2026-05-06 17:53:44.637 24793 INFO alembic.runtime.migration [-] Running upgrade 27e647c0fad4 -> e25ffa003242, Initial no-op Yoga contract migration.
2026-05-06 17:53:44.640 24793 INFO alembic.runtime.migration [-] Running upgrade e25ffa003242 -> 99de3849d860, Fix incorrect constraints.
2026-05-06 17:53:44.652 24793 INFO alembic.runtime.migration [-] Running upgrade 99de3849d860 -> c88cdce8f248, Remove duplicate constraints.
2026-05-06 17:53:44.655 24793 INFO alembic.runtime.migration [-] Running upgrade 27e647c0fad4 -> 29e87d24a316, Initial no-op Yoga expand migration.
2026-05-06 17:53:44.655 24793 INFO alembic.runtime.migration [-] Running upgrade 29e87d24a316 -> b4f8b3f584e0, Fix incorrect constraints.
2026-05-06 17:53:44.657 24793 INFO alembic.runtime.migration [-] Running upgrade b4f8b3f584e0 -> 11c3b243b4cb, Remove service_provider.relay_state_prefix server default.

# 查看生成的表
[root@gz-controller1 ~]# mysql -ukeystone -p 
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 5
Server version: 10.5.29-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use keystone
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [keystone]> show tables;
+------------------------------------+
| Tables_in_keystone                 |
+------------------------------------+
| access_rule                        |
| access_token                       |
| alembic_version                    |
| application_credential             |
| application_credential_access_rule |
| application_credential_role        |
| assignment                         |
| config_register                    |
| consumer                           |
| credential                         |
| endpoint                           |
| endpoint_group                     |
| expiring_user_group_membership     |
| federated_user                     |
| federation_protocol                |
| group                              |
| id_mapping                         |
| identity_provider                  |
| idp_remote_ids                     |
| implied_role                       |
| limit                              |
| local_user                         |
| mapping                            |
| nonlocal_user                      |
| password                           |
| policy                             |
| policy_association                 |
| project                            |
| project_endpoint                   |
| project_endpoint_group             |
| project_option                     |
| project_tag                        |
| region                             |
| registered_limit                   |
| request_token                      |
| revocation_event                   |
| role                               |
| role_option                        |
| sensitive_config                   |
| service                            |
| service_provider                   |
| system_assignment                  |
| token                              |
| trust                              |
| trust_role                         |
| user                               |
| user_group_membership              |
| user_option                        |
| whitelisted_config                 |
+------------------------------------+
49 rows in set (0.000 sec)

# 初始化fernet 密钥仓库，这个命令会生成对认证令牌进行加密解密的密钥
[root@gz-controller1 ~]# keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone
2026-05-06 18:01:47.872 25153 INFO keystone.common.utils [-] /etc/keystone/fernet-keys/ does not appear to exist; attempting to create it
2026-05-06 18:01:47.873 25153 INFO keystone.common.fernet_utils [-] Created a new temporary key: /etc/keystone/fernet-keys/0.tmp
2026-05-06 18:01:47.874 25153 INFO keystone.common.fernet_utils [-] Become a valid new key: /etc/keystone/fernet-keys/0
2026-05-06 18:01:47.875 25153 INFO keystone.common.fernet_utils [-] Starting key rotation with 1 key files: ['/etc/keystone/fernet-keys/0']
2026-05-06 18:01:47.876 25153 INFO keystone.common.fernet_utils [-] Created a new temporary key: /etc/keystone/fernet-keys/0.tmp
2026-05-06 18:01:47.877 25153 INFO keystone.common.fernet_utils [-] Current primary key is: 0
2026-05-06 18:01:47.877 25153 INFO keystone.common.fernet_utils [-] Next primary key will be: 1
2026-05-06 18:01:47.877 25153 INFO keystone.common.fernet_utils [-] Promoted key 0 to be the primary: 1
2026-05-06 18:01:47.878 25153 INFO keystone.common.fernet_utils [-] Become a valid new key: /etc/keystone/fernet-keys/0

[root@gz-controller1 ~]# keystone-manage credential_setup --keystone-user keystone --keystone-group keystone
2026-05-06 18:02:11.768 25161 INFO keystone.common.utils [-] /etc/keystone/credential-keys/ does not appear to exist; attempting to create it
2026-05-06 18:02:11.769 25161 INFO keystone.common.fernet_utils [-] Created a new temporary key: /etc/keystone/credential-keys/0.tmp
2026-05-06 18:02:11.770 25161 INFO keystone.common.fernet_utils [-] Become a valid new key: /etc/keystone/credential-keys/0
2026-05-06 18:02:11.771 25161 INFO keystone.common.fernet_utils [-] Starting key rotation with 1 key files: ['/etc/keystone/credential-keys/0']
2026-05-06 18:02:11.771 25161 INFO keystone.common.fernet_utils [-] Created a new temporary key: /etc/keystone/credential-keys/0.tmp
2026-05-06 18:02:11.772 25161 INFO keystone.common.fernet_utils [-] Current primary key is: 0
2026-05-06 18:02:11.774 25161 INFO keystone.common.fernet_utils [-] Next primary key will be: 1
2026-05-06 18:02:11.774 25161 INFO keystone.common.fernet_utils [-] Promoted key 0 to be the primary: 1
2026-05-06 18:02:11.774 25161 INFO keystone.common.fernet_utils [-] Become a valid new key: /etc/keystone/credential-keys/0

# 上面两个命令的作用分别是：为fernet token设置密钥仓库和授权收据（auth receipts），默认仓库路径是/etc/keystone/fernet-keys。这个命令也会创建一个主密钥用于创建和校验fernet 令牌和授权收据。

# 设置管理员密码变量，这个管理员也是后面登录openstack管理界面的管理员。查上面表格
[root@gz-controller1 ~]# export ADMIN_PASS=JzycczIrOmPZsa8u

# 初始化鉴权服务
# 这个初始化命令会创建默认的地域RegionOne、默认的域Default、默认用户admin、默认角色admin、默认用户admin和默认角色admin的关系绑定、设置keystone组件的服务端点。
[root@gz-controller1 ~]# keystone-manage bootstrap --bootstrap-password $ADMIN_PASS \
--bootstrap-admin-url http://gz-controller1:5000/v3/ \
--bootstrap-internal-url http://gz-controller1:5000/v3/ \
--bootstrap-public-url http://gz-controller1:5000/v3/ \
--bootstrap-region-id RegionOne
2026-05-06 18:06:57.671 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created domain default
2026-05-06 18:06:57.694 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created project admin
2026-05-06 18:06:57.703 25361 WARNING keystone.common.password_hashing [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Truncating password to algorithm specific maximum length 72 characters.: keystone.exception.UserNotFound: Could not find user: admin.2026-05-06 18:06:57.928 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created user admin
2026-05-06 18:06:57.934 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created role reader
2026-05-06 18:06:57.944 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created role member
2026-05-06 18:06:57.956 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created implied role where 388b8748f462477695843031667eff1c implies 5f71422b24ca48ab9baf83ce0b40b621
2026-05-06 18:06:57.965 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created role manager
2026-05-06 18:06:57.978 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created implied role where 174fd42cecd14980aad55bcb4228735c implies 388b8748f462477695843031667eff1c
2026-05-06 18:06:58.006 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created role admin
2026-05-06 18:06:58.022 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created implied role where 3200c78c1cf04462bbea8a882f33cd5b implies 174fd42cecd14980aad55bcb4228735c
2026-05-06 18:06:58.030 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created role service
2026-05-06 18:06:58.032 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Granted role admin on project admin to user admin.
2026-05-06 18:06:58.034 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Granted role admin on the system to user admin.
2026-05-06 18:06:58.037 25361 WARNING py.warnings [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] /usr/lib/python3.9/site-packages/pycadf/identifier.py:71: UserWarning: Invalid uuid: RegionOne. To ensure interoperability, identifiers should be a valid uuid.
  warnings.warn(('Invalid uuid: %s. To ensure interoperability, '

2026-05-06 18:06:58.038 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created region RegionOne
2026-05-06 18:06:58.062 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created public endpoint http://gz-controller1:5000/v3/
2026-05-06 18:06:58.066 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created internal endpoint http://gz-controller1:5000/v3/
2026-05-06 18:06:58.073 25361 INFO keystone.cmd.bootstrap [None req-c24186f5-7b6e-4481-8228-e7137b56c286 - - - - - -] Created admin endpoint http://gz-controller1:5000/v3/

# 配置 apache 服务器
[root@gz-controller1 ~]# vim /etc/httpd/conf/httpd.conf
ServerName gz-controller1:80
Listen gz-controller1:80

# 创建软链接并修改配置
[root@gz-controller1 ~]# ln -s /usr/share/keystone/wsgi-keystone.conf /etc/httpd/conf.d/
[root@gz-controller1 ~]# vim /etc/httpd/conf.d/wsgi-keystone.conf
Listen gz-controller1:5000

# 修改完之后，启动并开启开机自启httpd服务
[root@gz-controller1 ~]# systemctl enable --now httpd

# 在控制节点创建admin用的授权文件
[root@gz-controller1 ~]# vim admin-openrc 
export OS_USERNAME=admin
export OS_PASSWORD=JzycczIrOmPZsa8u
export OS_PROJECT_NAME=admin
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
export OS_AUTH_URL=http://gz-controller1:5000/v3
export OS_REGION_NAME=RegionOne
export OS_IDENTITY_API_VERSION=3

# 这个文件里指定的环境变量含义分别是：
# OS_USERNAME，认证使用的用户名，默认是admin，即集群管理员账号；
# OS_PASSWORD，管理员admin的密码；
# OS_PROJECT_NAME，项目名称，默认admin
# OS_USER_DOMAIN_NAME，用户所在域名称，默认Default
# OS_PROJECT_DOMAIN_NAME，项目所在域名称，默认Default
# OS_AUTH_URL，认证的keystone连接URL；
# OS_REGION_NAME，地域名称，默认RegionOne；
# OS_IDENTITY_API_VERSION，认证的API版本，默认是v3版本。
```

至此，keystone 组件就按照完毕了。执行下面命令来验证

```bash
[root@gz-controller1 ~]# source admin-openrc
[root@gz-controller1 ~]# openstack user list
+----------------------------------+-------+
| ID                               | Name  |
+----------------------------------+-------+
| ff1850b740aa4cc3bde9d038adbffe54 | admin |
+----------------------------------+-------+
```

如果openstack用户能够看到实际的用户信息，说明配置正确。



### 创建 service 项目

```bash
[root@gz-controller1 ~]# openstack project create --domain default --description "Service project" service
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| description | Service project                  |
| domain_id   | default                          |
| enabled     | True                             |
| id          | e62a640e1b1a4a3e8f3c9e010728b4f9 |
| is_domain   | False                            |
| name        | service                          |
| options     | {}                               |
| parent_id   | default                          |
| tags        | []                               |
+-------------+----------------------------------+
```

这个service项目需要给后面的几个组件使用，到这里keystone组件配置完毕。



### Placement 配置

#### 创建 placement 用户

在openstack集群内，创建placement用户

```bash
[root@gz-controller1 ~]# openstack user create --domain default --password-prompt placement
User Password:           # 这里使用的是placement用户的密码
Repeat User Password:
+---------------------+----------------------------------+
| Field               | Value                            |
+---------------------+----------------------------------+
| domain_id           | default                          |
| enabled             | True                             |
| id                  | 3ff42198d9164355bf47aa7a7ecd499b |
| name                | placement                        |
| options             | {}                               |
| password_expires_at | None                             |
+---------------------+----------------------------------+
```



#### 绑定角色

将placement用户绑定到admin角色

```bash
[root@gz-controller1 ~]# openstack role add --project service --user placement admin
```

这个命令执行成功后没有任何输出。



#### 创建 placement 服务

在集群中创建placement服务，对应的命令是：

```bash
[root@gz-controller1 ~]# openstack service create --name placement --description "Placement API" placement
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| description | Placement API                    |
| enabled     | True                             |
| id          | 1aca8eb44f264a5a9590c74dfbff7225 |
| name        | placement                        |
| type        | placement                        |
+-------------+----------------------------------+
```



#### 创建服务访问端点

创建placement服务的访问端点

```bash
[root@gz-controller1 ~]# openstack endpoint create --region RegionOne placement public http://gz-controller1:8778
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | 2c1bec45d1e24500b0ad7e6a6392e8da |
| interface    | public                           |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 1aca8eb44f264a5a9590c74dfbff7225 |
| service_name | placement                        |
| service_type | placement                        |
| url          | http://gz-controller1:8778       |
+--------------+----------------------------------+

[root@gz-controller1 ~]# openstack endpoint create --region RegionOne placement internal http://gz-controller1:8778
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | 4f3b1434524f4a37aa44772ddd9850f3 |
| interface    | internal                         |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 1aca8eb44f264a5a9590c74dfbff7225 |
| service_name | placement                        |
| service_type | placement                        |
| url          | http://gz-controller1:8778       |
+--------------+----------------------------------+

[root@gz-controller1 ~]# openstack endpoint create --region RegionOne placement admin http://gz-controller1:8778
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | 291891f3d150427abfb40d701f2d91af |
| interface    | admin                            |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 1aca8eb44f264a5a9590c74dfbff7225 |
| service_name | placement                        |
| service_type | placement                        |
| url          | http://gz-controller1:8778       |
+--------------+----------------------------------+
```



#### 修改配置文件

打开控制节点上的/etc/placement/placement.conf文件

```bash
[root@gz-controller1 ~]# cat /etc/placement/placement.conf |grep -Pv "^#|^$"
[api]
#...
auth_strategy = keystone

[keystone_authtoken]
www_authenticate_uri = http://gz-controller1:5000
auth_url = http://gz-controller1:5000/v3
auth_version = v3
service_token_roles = service
service_token_roles_required = true
memcached_servers = gz-controller1:11211
auth_type = password
project_domain_name = Default
user_domain_name = Default
project_name = service
username = placement
password = ROaTaWKNcTjjqDkF
[oslo_middleware]
[oslo_policy]
[placement]

[placement_database]
connection = mysql+pymysql://placement:lvIB6W1DtVT1X3IQ@gz-controller1/placement
```



#### 初始化数据库

配置完成后，开始初始化placement组件的数据库

```bash
[root@gz-controller1 ~]# su -s /bin/sh -c "placement-manage db sync" placement
```

数据库初始化完成后，会在/etc/httpd/conf.d/目录下 生成一个00-placement-api.conf文件，里面是placement的虚拟机主机，打开这个文件，将里面的监 听地址改为下面的样子

```bash
[root@gz-controller1 ~]# vim /etc/httpd/conf.d/00-placement-api.conf
Listen gz-controller1:8778

<VirtualHost *:8778>
# ......
  <Directory /usr/bin>
    Require all denied
    <Files "placement-api">
      <RequireAll>
        Require all granted
        Require not env blockAccess
      </RequireAll>
    </Files>
  </Directory>
</VirtualHost>
```

这是2.2和2.4版本的httpd的差异，添加这段内容，httpd才能正常调用/usr/bin/placement-api命令， placement-api才能在httpd2.4版本上正常工作。重启httpd服务

```bash
[root@gz-controller1 ~]# systemctl restart httpd
```

到这里placement服务就安装完毕。



#### 转换默认策略文件格式

从Wallaby版本开始，Placement组件的策略文件从json格式改为yaml格式，但是安装程序并没有帮我们自动转换，需要我们手动来处理一下，转换的命令是：

```bash
[root@gz-controller1 ~]# oslopolicy-convert-json-to-yaml --namespace placement \
--policy-file /etc/placement/policy.json \
--output-file /etc/placement/policy.yaml
mv /etc/placement/policy.json /etc/placement/policy.json.bak
```

转换完成后，下面的服务检查就能顺利通过。



#### placement服务校验

执行下面的命令来校验placement服务是否正常工作

```bash
[root@gz-controller1 ~]# placement-status upgrade check
+-------------------------------------------+
| Upgrade Check Results                     |
+-------------------------------------------+
| Check: Missing Root Provider IDs          |
| Result: Success                           |
| Details: None                             |
+-------------------------------------------+
| Check: Incomplete Consumers               |
| Result: Success                           |
| Details: None                             |
+-------------------------------------------+
| Check: Policy File JSON to YAML Migration |
| Result: Success                           |
| Details: None                             |
+-------------------------------------------+
```

然后检查命令执行结果：

```bash
[root@gz-controller1 ~]# echo $?
0
```



### Glance配置

#### 创建glance用户

数据创建完成后，在openstack集群里创建glance相关的用户

```bash
[root@gz-controller1 ~]# openstack user create --domain default --password-prompt glance
User Password:
Repeat User Password:
+---------------------+----------------------------------+
| Field               | Value                            |
+---------------------+----------------------------------+
| domain_id           | default                          |
| enabled             | True                             |
| id                  | 1a139355a8e446f7903107c381d12c06 |
| name                | glance                           |
| options             | {}                               |
| password_expires_at | None                             |
+---------------------+----------------------------------+
```



#### 绑定角色

需要将glance用户绑定到admin角色

```bash
[root@gz-controller1 ~]# openstack role add --project service --user glance admin
```



#### 创建glance 服务入口

```bash
[root@gz-controller1 ~]# openstack service create --name glance --description "OpenStack Image" image
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| description | OpenStack Image                  |
| enabled     | True                             |
| id          | 93de37d2c5c1415ab19e7e8a833ddc3e |
| name        | glance                           |
| type        | image                            |
+-------------+----------------------------------+
```



#### 创建服务访问端点

```bash
# public入口
[root@gz-controller1 ~]# openstack endpoint create --region RegionOne image public http://gz-controller1:9292
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | e6cffed9f2ae46be977c388c4a0f2a9d |
| interface    | public                           |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 93de37d2c5c1415ab19e7e8a833ddc3e |
| service_name | glance                           |
| service_type | image                            |
| url          | http://gz-controller1:9292       |
+--------------+----------------------------------+

# internal入口
[root@gz-controller1 ~]# openstack endpoint create --region RegionOne image internal http://gz-controller1:9292
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | f718732cde204cabbe05a91fb7633426 |
| interface    | internal                         |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 93de37d2c5c1415ab19e7e8a833ddc3e |
| service_name | glance                           |
| service_type | image                            |
| url          | http://gz-controller1:9292       |
+--------------+----------------------------------+

# admin入口
[root@gz-controller1 ~]# openstack endpoint create --region RegionOne image admin http://gz-controller1:9292
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | 880a2d67fb514cd7971bc8b86560bce0 |
| interface    | admin                            |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 93de37d2c5c1415ab19e7e8a833ddc3e |
| service_name | glance                           |
| service_type | image                            |
| url          | http://gz-controller1:9292       |
+--------------+----------------------------------+
```



#### 修改配置文件

```bash
[root@gz-controller1 ~]# vim /etc/glance/glance-api.conf
# 修改绑定地址和glance数据库连接信息
[DEFAULT]
# ......
bind_host = gz-controller1
# ......

[database]
connection = mysql+pymysql://glance:P4Sh2ixq24gSsvRn@gz-controller1/glance

[glance_store]
stores = file,http
default_store = file
filesystem_store_datadir = /var/lib/glance/images

[keystone_authtoken]
www_authenticate_uri = http://gz-controller1:5000
auth_version = v3
auth_url = http://gz-controller1:5000/v3
memcached_servers = controller:11211
service_token_roles = service
service_token_roles_required = True
auth_type = password
project_domain_name = Default
user_domain_name = Default
project_name = service
username = glance
password = WqddBWi6QXbMMXjk

[paste_deploy]
flavor = keystone
```

这里使用操作系统本地文件路径作为镜像的存储位置，即镜像文件会放到控制节点的磁盘上存储。后面生产环境中会将它和Ceph对接，存储到后端Ceph集群中。



#### 初始化数据库

执行下面的命令初始化glance组件所需数据库

```bash
[root@gz-controller1 ~]# su -s /bin/sh -c "glance-manage db_sync" glance
```

最后看到下面这样的字样，说明同步成功

```bash
......
2026-05-06 23:22:28.451 39350 INFO alembic.runtime.migration [-] Context impl MySQLImpl.
2026-05-06 23:22:28.451 39350 INFO alembic.runtime.migration [-] Will assume non-transactional DDL.
Database is synced successfully.
```



#### 启动glance-api服务

执行下面的命令启动glance-api服务并设置开机自启动：

```bash
[root@gz-controller1 ~]# systemctl enable --now openstack-glance-api.service
Created symlink /etc/systemd/system/multi-user.target.wants/openstack-glance-api.service → /usr/lib/systemd/system/openstack-glance-api.service.
```

然后可以执行下面的命令验证

```bash
[root@gz-controller1 ~]# source admin-openrc
[root@gz-controller1 ~]# openstack image list
```

如果没有报错，说明glance-api可以正常查询。



#### 镜像创建测试

下载了一个云镜像到服务器上，用于创建镜像测试

云镜像网站

```http
https://cloud-images.ubuntu.com/jammy/current/
```

![image-20260508131011595](D:\git_repository\cyber_security_learning\markdown_img\image-20260508131011595.png)

```bash
# 上传镜像到家目录
[root@gz-controller1 ~]# wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img

# 查看
[root@gz-controller1 ~]# ls
admin-openrc  anaconda-ks.cfg  jammy-server-cloudimg-amd64.img

# 上传镜像
[root@gz-controller1 ~]# openstack image create "ubuntu-22.04" \
  --file /root/jammy-server-cloudimg-amd64.img \
  --disk-format qcow2 \
  --container-format bare \
  --public
  
# 修改镜像，添加登录用户
[root@gz-controller1 ~]# LIBGUESTFS_BACKEND=direct virt-customize -a jammy-server-cloudimg-amd64.img --run-command 'useradd -m -s /bin/bash testuser' --run-command 'echo "testuser:123456" | chpasswd' --run-command 'usermod -aG sudo testuser' --run-command 'echo "testuser ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-testuser' --run-command 'chmod 440 /etc/sudoers.d/90-testuser'

# 上传镜像
[root@gz-controller1 ~]# openstack image create ubuntu-22.04-testuser   --disk-format qcow2   --container-format bare   --file jammy-server-cloudimg-amd64.img --public
```

创建成功，且镜像状态正常，说明glance-api正常工作：

```bash
[root@gz-controller1 ~]# openstack image list
```

到这里glance组件安装完毕。

补充：修改 Rocky9 

```bash
export LIBGUESTFS_BACKEND_SETTINGS=force_tcg export LIBGUESTFS_BACKEND=direct virt-customize -a /var/lib/libvirt/images/Rocky-9-GenericCloud.latest.x86_64.qcow2 --run-command 'useradd -m -s /bin/bash magedu || true' --run-command 'echo "magedu:123456" | chpasswd' --run-command 'usermod -aG wheel magedu' --run-command 'echo "magedu ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-magedu' --run-command 'chmod 440 /etc/sudoers.d/90-magedu' --run-command 'sed -ri "s/^#?PasswordAuthentication.*/PasswordAuthentication yes/" /etc/ssh/sshd_config'sshd_config'
```





### Cinder配置

#### 创建cinder用户

执行下面的命令在OpenStack集群中创建cinder用户

```bash
[root@gz-controller1 ~]# openstack user create --domain default --password-prompt cinder
User Password:
Repeat User Password:
+---------------------+----------------------------------+
| Field               | Value                            |
+---------------------+----------------------------------+
| domain_id           | default                          |
| enabled             | True                             |
| id                  | 03229ea157cc4630af6dd2243473cf77 |
| name                | cinder                           |
| options             | {}                               |
| password_expires_at | None                             |
+---------------------+----------------------------------+
```



#### 绑定角色

将cinder用户和admin角色绑定

```bash
[root@gz-controller1 ~]# openstack role add --project service --user cinder admin
```



#### 创建cinder服务

创建v3版本的cinder服务

```bash
[root@gz-controller1 ~]# openstack service create --name cinderv3 --description "OpenStack Block Storage" volumev3
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| description | OpenStack Block Storage          |
| enabled     | True                             |
| id          | bffe1998e23347e3869fe9e10f8f7d71 |
| name        | cinderv3                         |
| type        | volumev3                         |
+-------------+----------------------------------+
```



#### 创建服务端点

依次创建cinder的服务端端点：

```bash
[root@gz-controller1 ~]# openstack endpoint create --region RegionOne volumev3 public http://gz-controller1:8776/v3/%\(project_id\)s
+--------------+----------------------------------------------+
| Field        | Value                                        |
+--------------+----------------------------------------------+
| enabled      | True                                         |
| id           | 12344e19845342dc91155bcf1905131c             |
| interface    | public                                       |
| region       | RegionOne                                    |
| region_id    | RegionOne                                    |
| service_id   | bffe1998e23347e3869fe9e10f8f7d71             |
| service_name | cinderv3                                     |
| service_type | volumev3                                     |
| url          | http://gz-controller1:8776/v3/%(project_id)s |
+--------------+----------------------------------------------+

[root@gz-controller1 ~]# openstack endpoint create --region RegionOne volumev3 internal http://gz-controller1:8776/v3/%\(project_id\)s
+--------------+----------------------------------------------+
| Field        | Value                                        |
+--------------+----------------------------------------------+
| enabled      | True                                         |
| id           | 0684789652f841b690f2079e15fac738             |
| interface    | internal                                     |
| region       | RegionOne                                    |
| region_id    | RegionOne                                    |
| service_id   | bffe1998e23347e3869fe9e10f8f7d71             |
| service_name | cinderv3                                     |
| service_type | volumev3                                     |
| url          | http://gz-controller1:8776/v3/%(project_id)s |
+--------------+----------------------------------------------+

[root@gz-controller1 ~]# openstack endpoint create --region RegionOne volumev3 admin http://gz-controller1:8776/v3/%\(project_id\)s
+--------------+----------------------------------------------+
| Field        | Value                                        |
+--------------+----------------------------------------------+
| enabled      | True                                         |
| id           | 245a5afcf8ae40e29a831c76bb960285             |
| interface    | admin                                        |
| region       | RegionOne                                    |
| region_id    | RegionOne                                    |
| service_id   | bffe1998e23347e3869fe9e10f8f7d71             |
| service_name | cinderv3                                     |
| service_type | volumev3                                     |
| url          | http://gz-controller1:8776/v3/%(project_id)s |
+--------------+----------------------------------------------+
```

下面的操作需要注意，cinder的服务有4种：

- openstack-cinder-api，负责核心接口
- openstack-cinder-scheduler，负责调度，选择合适的节点接受调度任务
- openstack-cinder-volume，负责调度卷驱动创建实际的存储卷
- openstack-cinder-backup，负责卷快照任务

如果控制节点和计算节点是分离的，那么在控制节点上只需要启动前两个服务，在计算节点上只需要启动后两个服务。同时，计算节点和控制节点的配置因为安装的服务不同是有差异的。



#### 修改配置文件

打开/etc/cinder/cinder.conf文件，控制节点需要修改的配置如下所示

```bash
[root@gz-controller1 ~]# vim /etc/cinder/cinder.conf
[DEFAULT]
auth_strategy = keystone
glance_api_servers = http://gz-controller1:9292
my_ip = 192.168.100.200
osapi_volume_listen = $my_ip
transport_url = rabbit://openstack:xN4UFkpayBbNH1zS@gz-controller1

[database]
connection = mysql+pymysql://cinder:7t0u7vVSeiHs+3OT@gz-controller1/cinder

[keystone_authtoken]
www_authenticate_uri = http://gz-controller1:5000
auth_version = v3
auth_url = http://gz-controller1:5000
memcached_servers = localhost:11211
auth_type = password
project_domain_name = default
user_domain_name = default
project_name = service
username = cinder
password = bDtsOxVMlh9Nr7IL

[oslo_concurrency]
lock_path = /var/lib/cinder/tmp
```

配置修改好后，保存退出继续下面的操作



#### 初始化数据库

初始化cinder数据库，创建所需的表结构

```bash
[root@gz-controller1 ~]# su -s /bin/sh -c "cinder-manage db sync" cinder
```



#### 启动服务

在控制节点上只需要启动这两个服务即可

```bash
[root@gz-controller1 ~]# systemctl enable --now openstack-cinder-api.service openstack-cinder-scheduler.service
Created symlink /etc/systemd/system/multi-user.target.wants/openstack-cinder-api.service → /usr/lib/systemd/system/openstack-cinder-api.service.
Created symlink /etc/systemd/system/multi-user.target.wants/openstack-cinder-scheduler.service → /usr/lib/systemd/system/openstack-cinder-scheduler.service.
```

启动成功后，执行命令测试：

```bash
[root@gz-controller1 ~]# cinder list
+----+--------+------+------+----------------+-------------+----------+-------------+
| ID | Status | Name | Size | Consumes Quota | Volume Type | Bootable | Attached to |
+----+--------+------+------+----------------+-------------+----------+-------------+
+----+--------+------+------+----------------+-------------+----------+-------------+
```

有报错说明哪里配置有问题，需要检查配置信息。因为目前只搭建好了cinder-api和cinder-scheduler 服务，还没有搭建cinder-volume和cinder-backup服务，因此还无法测试卷创建和快照备份。到后面计算节点配置完成后，我们就可以测试。



#### 补充内容

数据卷在挂载到server实例上面之后，会存在一个挂载关系，这个挂载关系也是在数据库里进行管理的，主要有5个命令进行管理，分别是：

- cinder attachment-list，列出所有挂载关系。
- cinder attachment-show attach_id，显示挂载关系细节
- cinder attachment-delete attach_id，删除一个挂载关系
- cinder attachment-create 创建挂载关系
- cinder attachment-update 升级挂载关系。

后面两个命令使用的参数复杂一点。要根据具体的情况来确定，一般都是在网页上直接挂载磁盘到虚 拟机上或者从虚拟机上卸载磁盘，只有在网页上无法操作时，才需要使用到这几个命令来处理。



### Neutron配置

#### 创建neutron用户

创建neutron用户的命令是

```bash
[root@gz-controller1 ~]# openstack user create --domain default --password-prompt neutron
User Password:
Repeat User Password:
+---------------------+----------------------------------+
| Field               | Value                            |
+---------------------+----------------------------------+
| domain_id           | default                          |
| enabled             | True                             |
| id                  | 630d2d4dcad841a3b38badcc3d4c9906 |
| name                | neutron                          |
| options             | {}                               |
| password_expires_at | None                             |
+---------------------+----------------------------------+
```



#### 绑定角色

绑定neutron用户到admin角色，命令是

```bash
[root@gz-controller1 ~]# openstack role add --project service --user neutron admin
```



#### 创建neutron服务

在集群内创建neutron网络服务，命令是

```bash
[root@gz-controller1 ~]# openstack service create --name neutron --description "OpenStack Networking" network
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| description | OpenStack Networking             |
| enabled     | True                             |
| id          | 6d7d9097530d4910841db48b08590ee3 |
| name        | neutron                          |
| type        | network                          |
+-------------+----------------------------------+
```



#### 创建服务访问端点

创建neutron服务的3个端点

```bash
[root@gz-controller1 ~]# openstack endpoint create --region RegionOne network public http://gz-controller1:9696
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | fbdda6eb58dd40cf9174039a583eca16 |
| interface    | public                           |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 6d7d9097530d4910841db48b08590ee3 |
| service_name | neutron                          |
| service_type | network                          |
| url          | http://gz-controller1:9696       |
+--------------+----------------------------------+
[root@gz-controller1 ~]# openstack endpoint create --region RegionOne network internal http://gz-controller1:9696
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | 7bce5cf1b3fb4f99ba7860b20fc05754 |
| interface    | internal                         |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 6d7d9097530d4910841db48b08590ee3 |
| service_name | neutron                          |
| service_type | network                          |
| url          | http://gz-controller1:9696       |
+--------------+----------------------------------+
[root@gz-controller1 ~]# openstack endpoint create --region RegionOne network admin http://gz-controller1:9696
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | 7d010ce1f6cf4372914029e5382949cf |
| interface    | admin                            |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 6d7d9097530d4910841db48b08590ee3 |
| service_name | neutron                          |
| service_type | network                          |
| url          | http://gz-controller1:9696       |
+--------------+----------------------------------+
```



#### 修改neutron配置

使用provider网络，即单纯的二层网络，打开/etc/neutron/neutron.conf配置文件，需要新增或修改 的配置有

```bash
[root@gz-controller1 ~]# vim /etc/neutron/neutron.conf
[DEFAULT]
core_plugin = ml2
service_plugins =
notify_nova_on_port_status_changes = true
notify_nova_on_port_data_changes = true
transport_url = rabbit://openstack:xN4UFkpayBbNH1zS@gz-controller1
auth_strategy = keystone

[database]
connection = mysql+pymysql://neutron:KBifilr+NxW+jVDC@gz-controller1/neutron

[keystone_authtoken]
www_authenticate_uri = http://gz-controller1:5000
auth_url = http://gz-controller1:5000/v3
memcached_servers = localhost:11211
auth_type = password
project_domain_name = default
user_domain_name = default
project_name = service
username = neutron
password = JwqzZOmggKXUJDvO

[experimental]
linuxbridge = true

[oslo_concurrency]
lock_path = /var/lib/neutron/tmp
```

新增了一个linuxbridge =true的配置，因为在新版本的Neutron中，使用linuxbridge实现基础网络变成 了一个实验特性。(默认主流使用ovs/ovn，linuxbridge比较老，但是有部分老版本的 OpenStack 仍在维护使用，因此这里添加上去)



#### nova相关的配置

Neutron服务需要和Nova服务进行交互，因此需要在配置文件最后添加Nova组件的配置：

```bash
[nova]
auth_url = http://gz-controller1:5000
auth_type = password
project_domain_name = default
user_domain_name = default
region_name = RegionOne
project_name = service
username = nova
password = ac5RpUjzywMqhuqZ
```

neutron.conf文件修改完毕后，保存退出。



#### ML2配置

修改ML2配置文件，打开 /etc/neutron/plugins/ml2/ml2_conf.ini，需要新增的配置有：

```bash
[ml2]
type_drivers = flat,vlan
tenant_network_types =
mechanism_drivers = linuxbridge
extension_drivers = port_security

[ml2_type_flat]
flat_networks = provider

[securitygroup]
enable_ipset = true
```

这个配置表示只支持flat和vlan类型的网络，具体的网络类型和差异会在后面Neutron组件里详细讲解。



#### linux agent配置文件

打开 /etc/neutron/plugins/ml2/linuxbridge_agent.ini，需要新增的配置是：

```bash
[root@gz-controller1 ~]# vim /etc/neutron/plugins/ml2/linuxbridge_agent.ini
[linux_bridge]
physical_interface_mappings = provider:eth1    # 这里填自己机器的第二块网卡名

[vxlan]
enable_vxlan = false

[securitygroup]
enable_security_group = true
firewall_driver = neutron.agent.linux.iptables_firewall.IptablesFirewallDriver
```

provider后面是控制节点上虚拟机网络的接口地址，**根据实际情况来填写，因为每个人虚拟机上第二块 网卡的名称都可能不一样ss**。针对这个配置文件，centos7系统还需要新建一个模块加载配置

```bash
[root@gz-controller1 ~]# vim /etc/modules-load.d/neutron.conf
br_netfilter
```

为了能够开机自启动br_netfilter模块，还需要手动加载一下：

```bash
[root@gz-controller1 ~]# modprobe br_netfilter
```

然后往/etc/sysctl.conf文件里添加下面3行：

```bash
[root@gz-controller1 ~]# vim /etc/sysctl.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1

# 使其生效
[root@gz-controller1 ~]# sysctl -p
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
```



#### 配置 dhcp agent

打开文件路径/etc/neutron/dhcp_agent.ini，把下面三行添加到[default]下方:

```bash
[root@gz-controller1 ~]# vim /etc/neutron/dhcp_agent.ini
[DEFAULT]
interface_driver = linuxbridge
dhcp_driver = neutron.agent.linux.dhcp.Dnsmasq
enable_isolated_metadata = true
```

启用enabled_isolated_metadata=true，会自动在dhcp发的数据里增加一条路由：

```bash
169.254.169.254 gateway_ip xxx xx
```



#### 配置 metadata agent（元数据服务器）

打开文件/etc/neutron/metadata_agent.ini文件，在[DEFAULT]下面添加下面两行配置：

```bash
[root@gz-controller1 ~]# vim /etc/neutron/metadata_agent.ini 
[DEFAULT]
nova_metadata_host = gz-controller1
metadata_proxy_shared_secret = uj19FdS9DIGklYED
```

同时这两行必须写入到/etc/neutron/neutron.conf文件的[DEFAULT]位置，否则neutronmetadata-agent获取不到这个配置。



#### 创建配置文件软链接

创建ml2文件的软链接：

```bash
[root@gz-controller1 ~]# ln -s /etc/neutron/plugins/ml2/ml2_conf.ini /etc/neutron/plugin.ini
```



#### 初始化数据库

初始化neutron组件的数据库，命令是

```bash
[root@gz-controller1 ~]# su -s /bin/sh -c "neutron-db-manage --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head" neutron
```

最后看到下面的字样，说明数据库初始化成功：

```bash
INFO  [alembic.runtime.migration] Running upgrade 2e0d7a8a1586 -> 5c85685d616d
  确定|OK
```



#### 启动服务

设置网络服务开机自启并启动网络服务

```bash
[root@gz-controller1 ~]# systemctl enable --now neutron-server.service neutron-linuxbridge-agent.service neutron-dhcp-agent.service neutron-metadata-agent.service
Created symlink /etc/systemd/system/multi-user.target.wants/neutron-server.service → /usr/lib/systemd/system/neutron-server.service.
Created symlink /etc/systemd/system/multi-user.target.wants/neutron-linuxbridge-agent.service → /usr/lib/systemd/system/neutron-linuxbridge-agent.service.
Created symlink /etc/systemd/system/multi-user.target.wants/neutron-dhcp-agent.service → /usr/lib/systemd/system/neutron-dhcp-agent.service.
Created symlink /etc/systemd/system/multi-user.target.wants/neutron-metadata-agent.service → /usr/lib/systemd/system/neutron-metadata-agent.service.
```

确认服务正常了以后再配置开机自启动，否则会一直报错，导致多次重启失败后无法重启。需要执行下面的命令重设状态后才能重新启动

```bash
systemctl reset-failed neutron-server
```

上面的服务是neutron-server，其他的服务如果也出现这种状态，用同样的命令执行即可



#### 验证

使用下面的命令验证：

```bash
[root@gz-controller1 ~]# openstack port list
```

如果能正常执行，说明没问题，如果报错说明有问题。



#### 创建provider 网络

在控制节点上，初始化环境变量

```bash
[root@gz-controller1 ~]# source admin-openrc
```



然后创建一个虚拟网络：

```bash
[root@gz-controller1 ~]# openstack network create --share --provider-physical-network provider --provider-network-type flat flat_net
+---------------------------+--------------------------------------+
| Field                     | Value                                |
+---------------------------+--------------------------------------+
| admin_state_up            | UP                                   |
| availability_zone_hints   |                                      |
| availability_zones        |                                      |
| created_at                | 2026-05-06T16:34:42Z                 |
| description               |                                      |
| dns_domain                | None                                 |
| id                        | f43422a8-ec14-454f-89c0-d9956036f4e3 |
| ipv4_address_scope        | None                                 |
| ipv6_address_scope        | None                                 |
| is_default                | None                                 |
| is_vlan_transparent       | None                                 |
| mtu                       | 1500                                 |
| name                      | flat_net                             |
| port_security_enabled     | True                                 |
| project_id                | 546fb5e605354a52bc5fcdec78a0db9b     |
| provider:network_type     | flat                                 |
| provider:physical_network | provider                             |
| provider:segmentation_id  | None                                 |
| qos_policy_id             | None                                 |
| revision_number           | 1                                    |
| router:external           | Internal                             |
| segments                  | None                                 |
| shared                    | True                                 |
| status                    | ACTIVE                               |
| subnets                   |                                      |
| tags                      |                                      |
| tenant_id                 | 546fb5e605354a52bc5fcdec78a0db9b     |
| updated_at                | 2026-05-06T16:34:42Z                 |
+---------------------------+--------------------------------------+
```



#### 创建一个子网

网络创建好以后，在网络下面创建一个子网用于给虚拟机分配IP地址

```bash
[root@gz-controller1 ~]# openstack subnet create --network flat_net --allocation-pool start=192.168.116.150,end=192.168.116.253 --dns-nameserver=192.168.116.2 --gateway=192.168.116.2 --subnet-range=192.168.116.0/24 flat_subnet
+----------------------+--------------------------------------+
| Field                | Value                                |
+----------------------+--------------------------------------+
| allocation_pools     | 192.168.116.150-192.168.116.253      |
| cidr                 | 192.168.116.0/24                     |
| created_at           | 2026-05-06T16:35:51Z                 |
| description          |                                      |
| dns_nameservers      | 192.168.116.2                        |
| dns_publish_fixed_ip | None                                 |
| enable_dhcp          | True                                 |
| gateway_ip           | 192.168.116.2                        |
| host_routes          |                                      |
| id                   | d962442a-938c-4ac6-a665-9ed043b1360b |
| ip_version           | 4                                    |
| ipv6_address_mode    | None                                 |
| ipv6_ra_mode         | None                                 |
| name                 | flat_subnet                          |
| network_id           | f43422a8-ec14-454f-89c0-d9956036f4e3 |
| project_id           | 546fb5e605354a52bc5fcdec78a0db9b     |
| revision_number      | 0                                    |
| segment_id           | None                                 |
| service_types        |                                      |
| subnetpool_id        | None                                 |
| tags                 |                                      |
| updated_at           | 2026-05-06T16:35:51Z                 |
+----------------------+--------------------------------------+
```

这个命令创建的ip地址池范围是192.168.116.150到192.168.116.254，dns地址和网关地址都是 192.168.116.2

然后在网络里也可以看到对应子网的信息：

```bash
[root@gz-controller1 ~]# openstack network list
+--------------------------------------+----------+--------------------------------------+
| ID                                   | Name     | Subnets                              |
+--------------------------------------+----------+--------------------------------------+
| f43422a8-ec14-454f-89c0-d9956036f4e3 | flat_net | d962442a-938c-4ac6-a665-9ed043b1360b |
+--------------------------------------+----------+--------------------------------------+
```

这个网络是否能用，得等到nova配置完成后，创建虚拟机来测试就知道了。



### Nova配置

#### 创建nova用户

```bash
[root@gz-controller1 ~]# openstack user create --domain default --password-prompt nova
User Password:
Repeat User Password:
+---------------------+----------------------------------+
| Field               | Value                            |
+---------------------+----------------------------------+
| domain_id           | default                          |
| enabled             | True                             |
| id                  | b282d168b687415eb637ed5215214061 |
| name                | nova                             |
| options             | {}                               |
| password_expires_at | None                             |
+---------------------+----------------------------------+
```



#### 绑定角色

将用户nova和admin角色绑定

```bash
[root@gz-controller1 ~]# openstack role add --project service --user nova admin
[root@gz-controller1 ~]# openstack role add --project service --user nova service
```

nova需要和两个角色绑定，第一个角色admin是用来具备服务管理权限，第二个角色service，是用来 调用其他服务时使用。



#### 创建nova服务

```bash
[root@gz-controller1 ~]# openstack service create --name nova --description "OpenStack Compute" compute
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| description | OpenStack Compute                |
| enabled     | True                             |
| id          | 8c2923a3f8024d35b496e778c59031ee |
| name        | nova                             |
| type        | compute                          |
+-------------+----------------------------------+
```



#### 创建服务访问端点

依次创建nova服务的3个访问端点：

```bash
[root@gz-controller1 ~]# openstack endpoint create --region RegionOne compute public http://gz-controller1:8774/v2.1
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | 00db217b9ed04381858ec7501f58fb9c |
| interface    | public                           |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 8c2923a3f8024d35b496e778c59031ee |
| service_name | nova                             |
| service_type | compute                          |
| url          | http://gz-controller1:8774/v2.1  |
+--------------+----------------------------------+

[root@gz-controller1 ~]# openstack endpoint create --region RegionOne compute internal http://gz-controller1:8774/v2.1
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | 8ed86ec8a7e14bc59507526332ae38d9 |
| interface    | internal                         |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 8c2923a3f8024d35b496e778c59031ee |
| service_name | nova                             |
| service_type | compute                          |
| url          | http://gz-controller1:8774/v2.1  |
+--------------+----------------------------------+

[root@gz-controller1 ~]# openstack endpoint create --region RegionOne compute admin http://gz-controller1:8774/v2.1
+--------------+----------------------------------+
| Field        | Value                            |
+--------------+----------------------------------+
| enabled      | True                             |
| id           | 3658dfddb69d47dcb2976348eb13e021 |
| interface    | admin                            |
| region       | RegionOne                        |
| region_id    | RegionOne                        |
| service_id   | 8c2923a3f8024d35b496e778c59031ee |
| service_name | nova                             |
| service_type | compute                          |
| url          | http://gz-controller1:8774/v2.1  |
+--------------+----------------------------------+
```



#### 修改配置文件

需要修改的配置文件是/etc/nova/nova.conf，需要修改的配置内容如下所示

```bash
[root@gz-controller1 ~]# vim /etc/nova/nova.conf
[DEFAULT]
enabled_apis = osapi_compute,metadata
my_ip=192.168.100.200
metadata_host=$my_ip
firewall_driver=nova.virt.firewall.NoopFirewallDriver
transport_url=rabbit://openstack:xN4UFkpayBbNH1zS@gz-controller1
log_dir = /var/log/nova
lock_path = /var/lock/nova
state_path = /var/lib/nova

[api]
auth_strategy=keystone

[api_database]
connection=mysql+pymysql://nova:zHs5DOM4S+2OhJN8@gz-controller1/nova_api

[cinder]
catalog_info=volumev3::internalURL
os_region_name=RegionOne
auth_type=password
auth_url=http://gz-controller1:5000
project_name=service
project_domain_name=default
username=cinder
user_domain_name=default
password=bDtsOxVMlh9Nr7IL

[database]
connection=mysql+pymysql://nova:zHs5DOM4S+2OhJN8@gz-controller1/nova

[glance]
api_servers=http://gz-controller1:9292

[keystone_authtoken]
www_authenticate_uri=http://gz-controller1:5000/
auth_url=http://gz-controller1:5000
memcached_servers=gz-controller1:11211
auth_type=password
project_domain_name = Default
user_domain_name = Default
project_name = service
username = nova
password = ac5RpUjzywMqhuqZ 

[placement]
auth_type=password
auth_url=http://gz-controller1:5000/v3
project_name=service
project_domain_name=default
username=placement
user_domain_name=default
password=ROaTaWKNcTjjqDkF
region_name=RegionOne

[service_user]
send_service_user_token = true
auth_url = http://gz-controller1:5000/identity
auth_strategy = keystone
auth_type = password
project_domain_name = Default
project_name = service
user_domain_name = Default
username = nova
password = ac5RpUjzywMqhuqZ

[vnc]
enabled=true
server_listen=$my_ip
server_proxyclient_address=$my_ip
novncproxy_host=gz-controller1

[neutron]
auth_type = password
auth_url = http://gz-controller1:5000
project_domain_name = default
user_domain_name = default
region_name = RegionOne
project_name = service
username = neutron
password = JwqzZOmggKXUJDvO
service_metadata_proxy = true
metadata_proxy_shared_secret = uj19FdS9DIGklYED
```

这里的metadata_proxy_shared_secret配置项对应的值需要和neutron组件中的一样，否则nova和 neutron组件之间通信会失败。



#### 初始化数据库

首先初始化 nova-api 数据库

```bash
[root@gz-controller1 ~]# su -s /bin/sh -c "nova-manage api_db sync" nova
```

注册 cell0 数据库：

```bash
[root@gz-controller1 ~]# su -s /bin/sh -c "nova-manage cell_v2 map_cell0" nova
```

创建cell1 cell

```bash
[root@gz-controller1 ~]# su -s /bin/sh -c "nova-manage cell_v2 create_cell --name=cell1 --verbose" nova
--transport-url not provided in the command line, using the value [DEFAULT]/transport_url from the configuration file
--database_connection not provided in the command line, using the value [database]/connection from the configuration file
55fadf3c-08c3-4417-8989-89d44032b6e1
```

初始化nova数据库：

```bash
[root@gz-controller1 ~]# su -s /bin/sh -c "nova-manage db sync" nova
```

这个命令执行时可能会看到部分警告信息，可以不用管它。

验证cell0和cell1正确注册命令：

```bash
[root@gz-controller1 ~]# su -s /bin/sh -c "nova-manage cell_v2 list_cells" nova
+-------+--------------------------------------+----------------------------------------+-----------------------------------------------------+----------+
|  名称 |                 UUID                 |             Transport URL              |                      数据库连接                     | Disabled |
+-------+--------------------------------------+----------------------------------------+-----------------------------------------------------+----------+
| cell0 | 00000000-0000-0000-0000-000000000000 |                 none:/                 | mysql+pymysql://nova:****@gz-controller1/nova_cell0 |  False   |
| cell1 | 55fadf3c-08c3-4417-8989-89d44032b6e1 | rabbit://openstack:****@gz-controller1 |    mysql+pymysql://nova:****@gz-controller1/nova    |  False   |
+-------+--------------------------------------+----------------------------------------+-----------------------------------------------------+----------+
```



#### 启动服务

```bash
# 启动并开机自启
[root@gz-controller1 ~]# systemctl enable --now \
openstack-nova-api.service \
openstack-nova-scheduler.service \
openstack-nova-conductor.service \
openstack-nova-novncproxy.service
Created symlink /etc/systemd/system/multi-user.target.wants/openstack-nova-api.service → /usr/lib/systemd/system/openstack-nova-api.service.
Created symlink /etc/systemd/system/multi-user.target.wants/openstack-nova-scheduler.service → /usr/lib/systemd/system/openstack-nova-scheduler.service.
Created symlink /etc/systemd/system/multi-user.target.wants/openstack-nova-conductor.service → /usr/lib/systemd/system/openstack-nova-conductor.service.
Created symlink /etc/systemd/system/multi-user.target.wants/openstack-nova-novncproxy.service → /usr/lib/systemd/system/openstack-nova-novncproxy.service.
```



#### nova服务测试

执行下面的命令测试nova服务是否正常

```bash
[root@gz-controller1 ~]# nova list
nova CLI is deprecated and will be removed in a future release
+----+------+--------+------------+-------------+----------+
| ID | Name | Status | Task State | Power State | Networks |
+----+------+--------+------------+-------------+----------+
+----+------+--------+------------+-------------+----------+
```



### Horizon面板配置

#### 修改horizon django配置

先打开配置文件/etc/openstack-dashboard/local_settings，依次修改下面的配置：

```bash
[root@gz-controller1 ~]# vim /etc/openstack-dashboard/local_settings
# 配置允许以哪个域名或ip访问这个地址
ALLOWED_HOSTS = ['gz-controller1.mystical.org','gz-controller1']

# 配置主机名和鉴权服务地址
OPENSTACK_HOST = "gz-controller1.mystical.org"
OPENSTACK_KEYSTONE_URL = "http://%s:5000/v3" % OPENSTACK_HOST

# 配置memcached作为缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'gz-controller1:11211',
    },
}

# session存储引擎
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# 设置各个组件的API接口版本
OPENSTACK_API_VERSIONS = {
    "identity": 3,
    "image": 2,
    "volume": 3,
}

# 设置keystone用户的默认域和默认角色
WEBROOT='/dashboard'
OPENSTACK_KEYSTONE_MULTIDOMAIN_SUPPORT = True
OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = "Default"
OPENSTACK_KEYSTONE_DEFAULT_ROLE = "admin"

TIME_ZONE = "Asia/Shanghai"
```



#### 修改horizon httpd配置文件

```bash
# 改成如下配置即可
[root@gz-controller1 ~]# cat /etc/httpd/conf.d/openstack-dashboard.conf 
WSGIDaemonProcess dashboard
WSGIProcessGroup dashboard
WSGISocketPrefix run/wsgi
WSGIApplicationGroup %{GLOBAL}

#WSGIScriptAlias /dashboard /usr/share/openstack-dashboard/openstack_dashboard/wsgi/django.wsgi


WSGIScriptAlias /dashboard /usr/share/openstack-dashboard/openstack_dashboard/wsgi.py
Alias /dashboard/static /usr/share/openstack-dashboard/static

<Directory /usr/share/openstack-dashboard/openstack_dashboard>
  Options All
  AllowOverride All
  Require all granted
</Directory>

<Directory /usr/share/openstack-dashboard/static>
  Options All
  AllowOverride All
  Require all granted
</Directory>
```



#### 启动服务

```bash
[root@gz-controller1 ~]# systemctl restart httpd memcached
```



#### 在浏览器查看

![image-20260507014106996](D:\git_repository\cyber_security_learning\markdown_img\image-20260507014106996.png)

登录后

![image-20260507014127339](D:\git_repository\cyber_security_learning\markdown_img\image-20260507014127339.png)







## OpenStack 计算节点配置

计算机节点因为只需要负责创建虚拟机并和控制节点进行交互，因此需要安装的组件比控制节点要少得多，主要有：

- Neutron，负责虚拟机网络
- Cinder，负责虚拟机存储
- Nova，负责虚拟机管理



### 基础配置

#### 检查虚拟化支持

确认计算节点支持硬件虚拟化

```bash
# 检查是否开启虚拟化支持
[root@gz-computer1 ~]# egrep -c '(vmx|svm)' /proc/cpuinfo
8
```

如果是值是0，说明不支持硬件虚拟化，如果不是0，则支持。



#### 防火墙和selinux

确认所有节点的firewalld都是关闭状态，selinux都是disable状态。



#### OpenStack基础包安装

依次执行下面的4条命令，在节点上配置一下OpenStack Bobcat版本yum 源：

```bash
[root@gz-computer1 ~]# yum install centos-release-openstack-bobcat -y
[root@gz-computer1 ~]# sed -i 's/metalink=/#metalink=/g' /etc/yum.repos.d/CentOS-OpenStack-bobcat.repo
[root@gz-computer1 ~]# sed -i 's/#baseurl=/baseurl=/g' /etc/yum.repos.d/CentOS-OpenStack-bobcat.repo
```



### 网络配置

#### 安装包

neutron在计算节点上安装的包和服务端略有区别，如下所示：

```bash
[root@gz-computer1 ~]# yum install openstack-neutron-linuxbridge conntrack-tools -y
```



#### 修改配置文件

先打开配置文件/etc/neutron/neutron.conf，需要修改的配置如下所示：

```bash
[root@gz-computer1 ~]# vim /etc/neutron/neutron.conf
[DEFAULT]
transport_url = rabbit://openstack:xN4UFkpayBbNH1zS@gz-controller1
auth_strategy = keystone

[database]
connection = mysql+pymyqsl@neutron:KBifilr+NxW+jVDC@gz-controller1/neutron

[experimental]
linuxbridge = true

[keystone_authtoken]
www_authenticate_uri = http://gz-controller1:5000
auth_url = http://gz-controller1:5000
memcached_servers = gz-controller1:11211
service_token_roles = service
service_token_roles_required = true
auth_type = password
project_domain_name = default
user_domain_name = default
project_name = service
username = neutron
password = JwqzZOmggKXUJDvO

[oslo_concurrency]
lock_path = /var/lib/neutron/tmp
```

按照provider network的方式来配置，因为前面neutron服务端也是按照这个模式来配置的。再打开/etc/neutron/plugins/ml2/linuxbridge_agent.ini文件，添加或者修改配置到下面的样子：

```bash
[root@gz-computer1 ~]# vim /etc/neutron/plugins/ml2/linuxbridge_agent.ini
[linux_bridge]
physical_interface_mappings = provider:eth1

[securitygroup]
enable_security_group = true
firewall_driver = neutron.agent.linux.iptables_firewall.IptablesFirewallDriver

[vxlan]
enable_vxlan = false
```

节点上还需要配置br_netfilter模块开机自启动，步骤如下：

```bash
# 编辑/etc/modules-load.d/neutron.conf文件
[root@gz-computer1 ~]# vim /etc/modules-load.d/neutron.conf
br_netfilter

# 这个文件是为了配置br_netfilter模块开机自启动的。还需要手动加载一下
[root@gz-computer1 ~]# modprobe br_netfilter

# 验证
[root@gz-computer1 ~]# lsmod | grep br_netfilter
br_netfilter           36864  0
bridge                409600  1 br_netfilter

# 修改/etc/sysctl.conf文件，添加下面三行
[root@gz-computer1 ~]# vim /etc/sysctl.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1

# 加载配置
[root@gz-computer1 ~]# sysctl -p
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
```



#### 启动网络服务

最后启动网络组件对应的服务

```bash
[root@gz-computer1 ~]# systemctl enable --now neutron-linuxbridge-agent
Created symlink /etc/systemd/system/multi-user.target.wants/neutron-linuxbridge-agent.service → /usr/lib/systemd/system/neutron-linuxbridge-agent.service.
```

启动完成后，记得检查一下linuxbridge-agent服务的状态，确认是running状态后才能设置enable



### 存储配置

计算节点支持使用多种类型的后端，例如直接使用物理机上的磁盘，或者使用网络存储。本次测试环境使用的是本地磁盘上的lvm卷，此时对于虚拟机来说需要两个独立的lvm卷，一个给Nova使用，用于存放虚拟机系统盘，一个给Cinder使用，用于存放虚拟机数据盘。因此本次计算节点使用两块300G的 磁盘`/dev/sdb`和`/dev/sdc`，首先来创建LVM后端需要的vg，命令依次如下。



#### 安装包

安装存储配置所需要的包，命令如下：

```bash
[root@gz-computer1 ~]# yum install openstack-cinder targetcli python-keystone -y
```



#### 创建vg

先创建pv，本次配置里因为nova和cinder都需要对接后端的LVM，将盘 nvme0n1 和 nvme0n3 分别创建pv

```bash
[root@gz-computer1 ~]# pvcreate /dev/nvme0n2
  Physical volume "/dev/nvme0n2" successfully created.
  
[root@gz-computer1 ~]# pvcreate /dev/nvme0n3
  Physical volume "/dev/nvme0n3" successfully created.
```

再创建nova和cinder使用的vg，命令是：

```bash
[root@gz-computer1 ~]# vgcreate nova-volumes /dev/nvme0n2 
  Volume group "nova-volumes" successfully created
  
[root@gz-computer1 ~]# vgcreate cinder-volumes /dev/nvme0n3 
  Volume group "cinder-volumes" successfully created
  
# 查看
[root@gz-computer1 ~]# vgs
  VG             #PV #LV #SN Attr   VSize    VFree   
  cinder-volumes   1   0   0 wz--n- <300.00g <300.00g
  nova-volumes     1   0   0 wz--n- <300.00g <300.00g
  rl_bogon         1   3   0 wz--n- <199.00g       0 
```

要注意，这里的nova-volumes和cinder-volumes是vg的名称，下面要用到.



#### 修改lvm配置

打开/etc/lvm/lvm.conf文件，在devices部分添加下面的过滤器：

```bash
[root@gz-computer1 ~]# vim /etc/lvm/lvm.conf
global_filter = [ "a|/dev/nvme0n*|", "r/.*/" ]
```

这个过滤器的意思是，a即accept，表示只接受物理磁盘作为后端存储卷。r即reject，.*是通配符， 即/dev/目录下的所有其他设备都不接受作为后端存储卷。 同时不要使用官方文档上介绍的filter过滤器，因为这个过滤器因为功能问题已经被废弃，需要使用现 在的global_filter。



#### 修改 cinder 配置

打开/etc/cinder/cinder.conf文件，在这个文件里新增下面的配置（如果有重复的，则以实际配置文件 为准）：

```bash
[root@gz-computer1 ~]# vim /etc/cinder/cinder.conf
[DEFAULT]
backup_ceph_user = cinder-backup2
backup_driver = cinder.backup.drivers.ceph.CephBackupDriver
transport_url = rabbit://openstack:xN4UFkpayBbNH1zS@gz-controller1
auth_strategy = keystone
glance_api_servers = http://gz-controller1:9292
enabled_backends = lvm

[database]
connection = mysql+pymysql://cinder:7t0u7vVSeiHs+3OT@gz-controller1/cinder

[keystone_authtoken]
www_authenticate_uri = http://gz-controller1:5000
auth_url = http://gz-controller1:5000
memcached_servers = gz-controller1:11211
auth_type = password
project_domain_name = default
user_domain_name = default
project_name = service
username = cinder
password = bDtsOxVMlh9Nr7IL

[lvm]
target_helper = lioadm
target_protocol = iscsi
target_ip_address = 192.168.100.201
volume_backend_name = LVM
volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver
volume_group = cinder-volumes
volumes_dir = $state_path/volumes
```



cinder-backup备份配置目前支持的后端存储有：

- Ceph，块存储
- GCS，对象存储
- glusterfs，文件存储
- Swift，对象存储

在上面的示例中使用的是Ceph后端存储，因此还需要另外两个文件ceph.conf和ceph.client.cinderbackup2.keyring。具体的细节会在后面cinder一节中详细介绍。



#### 启动服务

```bash
# 启动lvm服务
[root@gz-computer1 ~]# systemctl enable --now lvm2-lvmpolld.service 
The unit files have no installation config (WantedBy=, RequiredBy=, Also=,
Alias= settings in the [Install] section, and DefaultInstance= for template
units). This means they are not meant to be enabled or disabled using systemctl.
 
Possible reasons for having this kind of units are:
• A unit may be statically enabled by being symlinked from another unit's
  .wants/ or .requires/ directory.
• A unit's purpose may be to act as a helper for some other unit which has
  a requirement dependency on it.
• A unit may be started when needed via activation (socket, path, timer,
  D-Bus, udev, scripted systemctl call, ...).
• In case of template units, the unit is meant to be enabled with some
  instance name specified.
  
[root@gz-computer1 ~]# systemctl enable --now openstack-cinder-volume.service 
Created symlink /etc/systemd/system/multi-user.target.wants/openstack-cinder-volume.service → /usr/lib/systemd/system/openstack-cinder-volume.service.
```

这个时候存储就相当于有了一个对应的agent节点了。



### 计算配置

#### 安装包

在CentOS 9.x发行版中，libvirt改为模块化安装和管理方式，先安装计算服务所需要的libvirt模块包和 openstack-nova-compute包，命令是：

```bash
[root@gz-computer1 ~]# yum install libvirt openstack-nova-compute -y
# 安装 virtio 模拟 GPU(这里目前未测试，使用vga更稳)
[root@gz-computer1 ~]# yum install -y qemu-kvm-device-display-virtio-gpu
[root@gz-computer1 ~]# yum install -y qemu-kvm-device-display-virtio-gpu-pci
```



#### 修改配置信息

打开/etc/nova/nova.conf文件，修改的内容如下：

```bash
[root@gz-computer1 ~]# vim /etc/nova/nova.conf
[DEFAULT]
my_ip=192.168.100.201
enabled_apis=osapi_compute,metadata
transport_url = rabbit://openstack:xN4UFkpayBbNH1zS@gz-controller1
compute_driver=libvirt.LibvirtDriver
log_dir = /var/log/nova
state_path = /var/lib/nova

[api]
auth_strategy=keystone

[cinder]
catalog_info=volumev3::internalURL
os_region_name=RegionOne
auth_type=password
auth_url=http://gz-controller1:5000
project_domain_name=Default
user_domain_name=Default
username=cinder
password=bDtsOxVMlh9Nr7IL

[glance]
api_servers=http://gz-controller1:9292

[keystone]
www_authenticate_uri=http://gz-controller1:5000
auth_url=http://gz-controller1:5000
memcached_servers=controller:11211
auth_type=password
project_domain_name = default
user_domain_name = default
project_name = service
username = nova
password = ac5RpUjzywMqhuqZ

[libvirt]
#virt_type=kvm
virt_type=qemu
cpu_mode=none
video_type=vga
snapshot_image_format=qcow2
images_type=lvm
images_volume_group=nova-volumes

[neutron]
auth_url = http://gz-controller1:5000
region_name = RegionOne
project_domain_name = default
user_domain_name = default
project_name = service
auth_type = password
username = neutron
password = JwqzZOmggKXUJDvO

[placement]
auth_url = http://gz-controller1:5000/v3
region_name = RegionOne
project_domain_name = Default
user_domain_name = default
project_name = service
auth_type=password
username = placement
password = ROaTaWKNcTjjqDkF

[oslo_concurrency]
lock_path=/var/lib/nova/tmp

[vnc]
enabled=true
server_listen=$my_ip
server_proxyclient_address = $my_ip
novncproxy_base_url=http://gz-controller1:6080/vnc_auto.html
novncproxy_host=$my_ip
```

在 flavor 和 image 添加属性

```bash
# 创建 flavor
[root@gz-computer1 ~]# openstack flavor create \
--id 1 \
--vcpus 1 \
--ram 1024 \
--disk 20 \
1c1g20g
+----------------------------+---------+
| Field                      | Value   |
+----------------------------+---------+
| OS-FLV-DISABLED:disabled   | False   |
| OS-FLV-EXT-DATA:ephemeral  | 0       |
| description                | None    |
| disk                       | 20      |
| id                         | 1       |
| name                       | 1c1g20g |
| os-flavor-access:is_public | True    |
| properties                 |         |
| ram                        | 1024    |
| rxtx_factor                | 1.0     |
| swap                       | 0       |
| vcpus                      | 1       |
+----------------------------+---------+
[root@gz-controller1 ~]# openstack flavor set --property hw:video_model=vga 1c1g20g
[root@gz-controller1 ~]# openstack image set --property hw_video_model=vga ubuntu-22.04
```



#### 启动服务

上面说过libvirt是模块化包，因此启动方式发生了一些变化，先启动libvirtd进程，

```bash
# 启动模块化守护进程，命令依次是：
for drv in qemu interface network nodedev nwfilter secret storage;
do
    systemctl unmask virt${drv}d.service;
    systemctl unmask virt${drv}d{,-ro,-admin}.socket;
    systemctl enable virt${drv}d.service;
    systemctl enable virt${drv}d{,-ro,-admin}.socket;
done

Created symlink /etc/systemd/system/multi-user.target.wants/virtinterfaced.service → /usr/lib/systemd/system/virtinterfaced.service.
Created symlink /etc/systemd/system/multi-user.target.wants/virtnetworkd.service → /usr/lib/systemd/system/virtnetworkd.service.
Created symlink /etc/systemd/system/multi-user.target.wants/virtnodedevd.service → /usr/lib/systemd/system/virtnodedevd.service.
Created symlink /etc/systemd/system/multi-user.target.wants/virtnwfilterd.service → /usr/lib/systemd/system/virtnwfilterd.service.
Created symlink /etc/systemd/system/multi-user.target.wants/virtsecretd.service → /usr/lib/systemd/system/virtsecretd.service.
Created symlink /etc/systemd/system/multi-user.target.wants/virtstoraged.service → /usr/lib/systemd/system/virtstoraged.service.

# 然后启用模块化进程的套接字：
for drv in qemu network nodedev nwfilter secret storage;
do
    systemctl start virt${drv}d{,-ro,-admin}.socket;
done

# 最后启动计算服务：
[root@gz-computer1 ~]# systemctl enable --now openstack-nova-compute.service
Created symlink /etc/systemd/system/multi-user.target.wants/openstack-nova-compute.service → /usr/lib/systemd/system/openstack-nova-compute.service.
```

到这里，计算节点就配置完毕了，剩下的是在控制节点上的操作。目前只有通过这种方式才能在 RHEL9上正常加载virtio驱动。



#### 添加nova节点到cell数据库

在控制节点查看新增的nova计算节点状态，命令是：

```bash
[root@gz-controller1 ~]# source admin-openrc 
[root@gz-controller1 ~]# openstack compute service list --service nova-compute
+--------------------------------------+--------------+---------------------------+------+---------+-------+----------------------------+
| ID                                   | Binary       | Host                      | Zone | Status  | State | Updated At                 |
+--------------------------------------+--------------+---------------------------+------+---------+-------+----------------------------+
| 1bd02060-13c2-4563-9ff3-6c39ab936aab | nova-compute | gz-computer1.mystical.org | nova | enabled | up    | 2026-05-08T03:48:45.000000 |
+--------------------------------------+--------------+---------------------------+------+---------+-------+----------------------------+
```

正常情况下此时就可以看到计算节点的信息，执行下面命令发现计算节点主机（注册该计算节点到系统中）

```bash
[root@gz-controller1 ~]#  su -s /bin/sh -c "nova-manage cell_v2 discover_hosts --verbose" nova
Found 2 cell mappings.
Skipping cell0 since it does not contain hosts.
Getting computes from cell 'cell1': 55fadf3c-08c3-4417-8989-89d44032b6e1
Checking host mapping for compute host 'gz-computer1.mystical.org': 4f05bb1e-5a64-45f6-85b0-ce96c45b57b6
Creating host mapping for compute host 'gz-computer1.mystical.org': 4f05bb1e-5a64-45f6-85b0-ce96c45b57b6
Found 1 unmapped computes in cell: 55fadf3c-08c3-4417-8989-89d44032b6e1
```

说明注册成功，这个时候就可以尝试创建并启动虚拟机了。

此时在浏览器的 Web UI 应该能看到计算节点

#### ![image-20260508115552185](D:\git_repository\cyber_security_learning\markdown_img\image-20260508115552185.png)创建实例测试

先创建实例类型

![image-20260508120137079](D:\git_repository\cyber_security_learning\markdown_img\image-20260508120137079.png)

检查下之前创建的镜像

![image-20260508120256154](D:\git_repository\cyber_security_learning\markdown_img\image-20260508120256154.png)

查看之前测试的时候创建的网络

![image-20260508120343021](D:\git_repository\cyber_security_learning\markdown_img\image-20260508120343021.png)

创建实例

![image-20260508120507998](D:\git_repository\cyber_security_learning\markdown_img\image-20260508120507998.png)

![image-20260508120543894](D:\git_repository\cyber_security_learning\markdown_img\image-20260508120543894.png)

![image-20260508120717335](D:\git_repository\cyber_security_learning\markdown_img\image-20260508120717335.png)

![image-20260508120754412](D:\git_repository\cyber_security_learning\markdown_img\image-20260508120754412.png)

![image-20260508120834670](D:\git_repository\cyber_security_learning\markdown_img\image-20260508120834670.png)

![image-20260508120913270](D:\git_repository\cyber_security_learning\markdown_img\image-20260508120913270.png)

创建过程中，可以通过日志查看是否有问题

```bash
[root@gz-computer1 ~]# tail -f /var/log/nova/nova-conductor.log 
2026-05-08 11:35:43.764 35043 ERROR oslo_service.service 
2026-05-08 11:35:44.720 2105 INFO oslo_service.service [None req-d5337f90-1905-4ce2-8035-9c9b58f8931b - - - - - -] Child 35001 exited with status 1
......

[root@gz-computer1 ~]# grep -i "ERROR\|CRITICAL\|Traceback\|AccessRefused\|OperationalError" /var/log/nova/nova-conductor.log | tail -n 80
2026-05-08 11:35:42.752 35002 ERROR oslo_service.service   File "/usr/lib/python3.9/site-packages/kombu/connection.py", line 877, in _connection_factory
......
```



# OpenStack 认证服务 Keystone

首先来介绍OpenStack里的第一个核心组件，在企业内部任何一个核心系统都离不开认证和授权，而 Keystone就是OpenStack里用来提供认证和授权服务的组件，主要负责OpenStack中用户的身份认 证、令牌管理、提供OpenStack内部资源的服务目录和访问端点。提供基于角色的权限控制方式，也 就是我们常说的RBAC权限控制。

在之前搭建实验环境的时候，在安装配置各个组件之前我们都需要先创建每个组件的用户，把它绑定 到管理员角色，然后创建服务自身以及服务的访问端点（public、internal、admin共3个）。这个过程就是SOA架构中的服务发现和注册，各个组件的用户、角色、端点等资源都是由Keystone来进行管理的，下面我们来深入研究Keystone的基本架构，以及它的是怎样完成这样的管理工作的。



Keystone 建议教学大纲

```bat
1. Keystone 架构与运行机制
2. Keystone 核心资源模型
   - Domain
   - Project
   - User / Group
   - Role

3. Keystone Endpoint 与 Service Catalog
4. Keystone Token 机制
5. Fernet Token 与 Key Rotation
6. Keystone 认证授权完整流程
7. Keystone Policy 与权限控制
8. Keystone Middleware 工作机制
9. Keystone 高可用与多 Region
```



## Keystone 架构与运行机制

### 什么是 Keystone

Keystone 是 OpenStack 的 Identity Service（身份服务），即 **OpenStack IAM 中心**。

Keystone 负责：

- 用户认证（Authentication）
- Token 签发
- 用户/项目管理
- Role Assignment
- Service Catalog
- Endpoint 管理

```bat
它本质上是 OpenStack 的统一身份认证中心
```



> Keystone 本质上是一个运行在 WSGI 架构上的 **Python Web Application**



### Keystone 整体架构（核心）

```bat
HTTP Request
    ↓
Apache httpd
    ↓
mod_wsgi
    ↓
keystone-wsgi-public
    ↓
Keystone Python Application
    ↓
Keystone 源码
    ↓
Token / User / Policy / Catalog
```

mod_wsgi 是 Apache 的 **Python WSGI 模块**。它允许 Apache 直接加载 **Python WSGI Application。**

```bat
mod_wsgi 是 Apache 的 WSGI 模块，
用于在 Apache httpd 中嵌入 Python Interpreter，
并加载和运行 Python WSGI Application，
从而使 Apache 能够处理 Keystone 这样的 Python Web API 服务。

教学版：
mod_wsgi 可以理解为 Apache 的 Python 运行桥梁，
它让 Apache 能够加载并运行 Keystone 这样的 Python WSGI Web 应用。
真正执行 Python 代码的是 Python Interpreter，
而 mod_wsgi 的作用是让 Apache 能够加载并运行 Python WSGI Web Application。
```



#### keystone-wsgi-public 是什么

它不是完整 Keystone 程序。而是 WSGI 入口脚本（Entry Point）。

示例：

```python
from keystone.server.wsgi import initialize_public_application

application = initialize_public_application()
```

它的作用是**创建 Keystone WSGI Application 对象（application）。**



#### Openstack Keystone RPM包

Keystone 源码位于：

```ABAP
/usr/lib/python3*/site-packages/keystone/
```

OpenStack 使用 RPM 分层打包。

 OpenStack Keystone 通常拆成：

| RPM包              | 作用         |
| ------------------ | ------------ |
| openstack-keystone | 服务层       |
| python3-keystone   | Python源码层 |



##### openstack-keystone 包负责什么

```bash
# 查看 openstack-keystone 包里的内容
[root@gz-controller1 /etc/httpd/conf.d]# rpm -ql openstack-keystone
\/etc/keystone
/etc/keystone/default_catalog.templates
/etc/keystone/keystone.conf
/etc/keystone/logging.conf
/etc/keystone/policy.d
/etc/keystone/policy.json
/etc/keystone/sso_callback_template.html
/etc/logrotate.d/openstack-keystone
/usr/bin/keystone-manage
/usr/bin/keystone-status
/usr/bin/keystone-wsgi-admin
/usr/bin/keystone-wsgi-public
/usr/bin/openstack-keystone-sample-data
/usr/lib/sysctl.d/openstack-keystone.conf
/usr/share/doc/openstack-keystone
/usr/share/doc/openstack-keystone/README.rst
/usr/share/keystone
/usr/share/keystone/keystone-dist.conf
/usr/share/keystone/keystone-schema.json
/usr/share/keystone/keystone-schema.yaml
/usr/share/keystone/sample_data.sh
/usr/share/keystone/wsgi-keystone.conf
/usr/share/licenses/openstack-keystone
/usr/share/licenses/openstack-keystone/LICENSE
/usr/share/man/man1/keystone-manage.1.gz
/var/lib/keystone
/var/log/keystone
/var/log/keystone/keystone.log
```

它主要负责：

- WSGI入口
- 配置文件
- Apache配置
- 日志目录
- 管理工具



真正源码来自 python3-keystone，该包是因为依赖关系，在下载 openstack-keystone包的时候自动安装的

```bash
[root@gz-controller1 /etc/httpd/conf.d]# yum deplist openstack-keystone
上次元数据过期检查：1:41:27 前，执行于 2026年05月09日 星期六 14时30分31秒。
package: openstack-keystone-1:24.0.0-1.el9s.noarch
  dependency: /bin/sh
   provider: bash-5.1.8-9.el9.x86_64
  dependency: /usr/bin/bash
   provider: bash-5.1.8-9.el9.x86_64
  dependency: /usr/bin/python3
   provider: python3-3.9.25-3.el9_7.3.x86_64
   provider: python3-3.9.25-3.el9_7.3.i686
  dependency: python3-keystone = 1:24.0.0-1.el9s
   provider: python3-keystone-1:24.0.0-1.el9s.noarch
  dependency: shadow-utils
   provider: shadow-utils-2:4.9-15.el9.x86_64

# 查看python3-keystone包里的内容
[root@gz-controller1 /etc/httpd/conf.d]# rpm -ql python3-keystone
/usr/lib/python3.9/site-packages/keystone
/usr/lib/python3.9/site-packages/keystone-24.0.0.dist-info
/usr/lib/python3.9/site-packages/keystone-24.0.0.dist-info/AUTHORS
/usr/lib/python3.9/site-packages/keystone-24.0.0.dist-info/INSTALLER
/usr/lib/python3.9/site-packages/keystone-24.0.0.dist-info/LICENSE
/usr/lib/python3.9/site-packages/keystone-24.0.0.dist-info/METADATA
......
```



### 完整 Keystone 启动链路（核心）

```bat
yum install openstack-keystone
    ↓
自动安装 python3-keystone
    ↓
Python源码进入 site-packages
    ↓
Apache 启动
    ↓
mod_wsgi 加载 keystone-wsgi-public
    ↓
keystone-wsgi-public import keystone.server.wsgi
    ↓
initialize_public_application()
    ↓
创建 Keystone WSGI Application
    ↓
开始处理 HTTP API 请求
```



### Keystone 本质总结

```bat
Apache + mod_wsgi 承载的 Python WSGI Web 应用。
```







## KeyStone 体系结构

### KeyStone 体系核心概念

- 地域（region）和可用区（available zone，简称az）
- 域（domain）和项目（Project）
- 用户（User）、用户组（Group）和角色（Role）
- 策略（Policy）
- 服务（Service），例如nova、cinder、glance等和端点（Endpoint）
- 令牌（Token）和凭据（Credentials）



#### Region（地域）

**OpenStack 中的 Region**

在 OpenStack 的底层实现中：Region 本质上是 Keystone 对 Service Endpoint 的逻辑分类管理机制，用于区分不同 OpenStack 服务集合。

Keystone 用 Region 来区分：这一组 API Endpoint 属于哪一套云环境

```bat
RegionOne
 ├── nova endpoint
 ├── glance endpoint
 ├── neutron endpoint
```

它主要用于：

- Service Catalog 分类
- 多云区域管理
- Endpoint 隔离

本质上属于：逻辑管理域，而不是物理机房概念



**公有云中的 Region**

在公有云产品设计中：Region 通常被定义为 “地域”

```bat
一个 Region ≈ 一个大型数据中心区域
```

例如：

| 云厂商 | Region    |
| ------ | --------- |
| AWS    | us-east-1 |
| 阿里云 | 华东1     |
| 腾讯云 | 广州      |
| 华为云 | 北京四    |

这些 Region 往往对应真实的数据中心区域，并具备：

- 网络隔离
- 电力隔离
- 容灾隔离

等能力。因此：公有云中的 Region 通常具有物理地理意义。



**Openstack的多Region意义**

OpenStack 的多 Region，本质上就是：“多个 OpenStack 服务区域，共享同一个 Keystone 认证体系” 以进一步理解成：

```bat
多个 OpenStack 云环境
被一个 Keystone 统一管理。
```

整体架构

```bat
                Keystone
                    │
        ┌───────────┴───────────┐
        │                       │
   RegionOne               RegionTwo
   (广州)                     (上海)
        │                       │
   nova/glance            nova/glance
   neutron/cinder         neutron/cinder (多个小OpenStack)
```



#### Availability Zone（AZ，可用区）

##### 什么是 Availability Zone（AZ）

Availability Zone（AZ，可用区）是 OpenStack 中的一种 "对计算资源进行分组管理。"

AZ 的核心作用：是让 Nova Scheduler 在创建虚拟机时，决定实例应该调度到哪些计算节点。

> AZ 是对 Compute Node 的逻辑资源分组。



##### AZ 解决什么问题

AZ 主要解决：

| 场景     | 作用     |
| -------- | -------- |
| 多机房   | 故障隔离 |
| GPU资源  | 资源隔离 |
| SSD资源  | 性能隔离 |
| 不同业务 | 调度隔离 |
| 运维管理 | 资源分类 |



##### AZ 与 Region 的区别

**Region** 管理的是：“使用哪一套 OpenStack 服务（Endpoint）”，也就是访问哪一个云区域。

例如：

```bat
RegionOne -> 广州云
RegionTwo -> 上海云
```

每个 Region 通常都有

- 自己的 Nova
- 自己的 Neutron
- 自己的 Glance

这些云服务。

因此：Region 决定使用哪一套 OpenStack 云服务，AZ 决定实例调度到哪些计算节点资源池。

> Region 和 AZ 是完全不同维度的概念。
>
> Region 是对 OpenStack 云服务区域的划分，而 AZ 是对计算节点资源池的划分。









#### 服务（Service）和端点（Endpoint）

服务就是OpenStack集群中各个组件能够提供的能力，例如Cinder组件提供的存储、neutron组件提供的网络， glance组件提供的镜像、keystone组件提供的认证，nova组件提供的虚拟机管理等能力。所有的服务都需要先在 Keystone里注册，组成服务清单目录（catalog），供其他服务查询，然后其他服务才能进行调用。例如Nova服务依 赖于镜像、存储、网络等基本服务，那么它在创建虚拟机时，就会先去keystone查询可以使用的服务，如果服务清单目录有，就向对应的服务请求所需要的资源。

 Endpoint（服务端点）可以理解为 “服务的访问地址”，本质上：

```bat
Endpoint = API 服务入口地址
```

例如：

| 服务    | Endpoint              |
| ------- | --------------------- |
| Nova    | http://10.0.0.10:8774 |
| Glance  | http://10.0.0.11:9292 |
| Neutron | http://10.0.0.12:9696 |

这些地址：就是 OpenStack 各组件真正提供 API 的地方。



##### 为什么 OpenStack 需要 Endpoint

因为 OpenStack 本质上是 “一堆微服务”

例如：

| 组件     | 功能   |
| -------- | ------ |
| Keystone | 认证   |
| Nova     | 计算   |
| Neutron  | 网络   |
| Glance   | 镜像   |
| Cinder   | 块存储 |

这些服务：

- 地址不同
- 端口不同
- 节点不同

所以用户登录后必须知道各个组件的访问地址，这个时候 “Keystone” 就负责告诉客户端： “这些服务的访问地址是什么”。



##### Keystone Service Catalog

这里是核心。当用户认证成功后，Keystone 不只是返回 Token。还会返回 “Service Catalog（服务目录）”，里面记录了：有哪些服务 和 每个服务在哪。

示例：

```bat
{
  "service": "nova",
  "region": "RegionOne",
  "endpoint": "http://10.0.0.10:8774/v2.1"
}
```

客户端（例如：Horizon、OpenStack CLI、Terraform、SDK）等都会根据 Service catalog 去访问对应 API



##### Endpoint 在 Keystone 里怎么存

OpenStack 里 Endpoint 是 Keystone 数据库中的资源。

```bash
# 查看
[root@gz-controller1 ~]# openstack endpoint list
+----------------------------------+-----------+--------------+--------------+---------+-----------+----------------------------------------------+
| ID                               | Region    | Service Name | Service Type | Enabled | Interface | URL                                          |
+----------------------------------+-----------+--------------+--------------+---------+-----------+----------------------------------------------+
| 00db217b9ed04381858ec7501f58fb9c | RegionOne | nova         | compute      | True    | public    | http://gz-controller1:8774/v2.1              |
| 0684789652f841b690f2079e15fac738 | RegionOne | cinderv3     | volumev3     | True    | internal  | http://gz-controller1:8776/v3/%(project_id)s |
| 12344e19845342dc91155bcf1905131c | RegionOne | cinderv3     | volumev3     | True    | public    | http://gz-controller1:8776/v3/%(project_id)s |
| 245a5afcf8ae40e29a831c76bb960285 | RegionOne | cinderv3     | volumev3     | True    | admin     | http://gz-controller1:8776/v3/%(project_id)s |
| 291891f3d150427abfb40d701f2d91af | RegionOne | placement    | placement    | True    | admin     | http://gz-controller1:8778                   |
| 2c1bec45d1e24500b0ad7e6a6392e8da | RegionOne | placement    | placement    | True    | public    | http://gz-controller1:8778                   |
| 3076e1720f6443dc9e0ecd98f8a2e3fb | RegionOne | keystone     | identity     | True    | admin     | http://gz-controller1:5000/v3/               |
| 3658dfddb69d47dcb2976348eb13e021 | RegionOne | nova         | compute      | True    | admin     | http://gz-controller1:8774/v2.1              |
| 4f3b1434524f4a37aa44772ddd9850f3 | RegionOne | placement    | placement    | True    | internal  | http://gz-controller1:8778                   |
| 646d835290d540d185287fc5494f2ced | RegionOne | keystone     | identity     | True    | internal  | http://gz-controller1:5000/v3/               |
| 7bce5cf1b3fb4f99ba7860b20fc05754 | RegionOne | neutron      | network      | True    | internal  | http://gz-controller1:9696                   |
| 7d010ce1f6cf4372914029e5382949cf | RegionOne | neutron      | network      | True    | admin     | http://gz-controller1:9696                   |
| 880a2d67fb514cd7971bc8b86560bce0 | RegionOne | glance       | image        | True    | admin     | http://gz-controller1:9292                   |
| 8ed86ec8a7e14bc59507526332ae38d9 | RegionOne | nova         | compute      | True    | internal  | http://gz-controller1:8774/v2.1              |
| ba23b370774f45c5a8c8b52666cd5ccf | RegionOne | keystone     | identity     | True    | public    | http://gz-controller1:5000/v3/               |
| e6cffed9f2ae46be977c388c4a0f2a9d | RegionOne | glance       | image        | True    | public    | http://gz-controller1:9292                   |
| f718732cde204cabbe05a91fb7633426 | RegionOne | glance       | image        | True    | internal  | http://gz-controller1:9292                   |
| fbdda6eb58dd40cf9174039a583eca16 | RegionOne | neutron      | network      | True    | public    | http://gz-controller1:9696                   |
+----------------------------------+-----------+--------------+--------------+---------+-----------+----------------------------------------------+
```

```bat
Nova 的 Endpoint = Nova API 地址
Glance 的 Endpoint = Glance API 地址
```



##### Region 和 Endpoint 的关系图

```bat
Keystone
│
├── RegionOne
│     ├── Nova Endpoint
│     │      └── http://gz:8774
│     │
│     ├── Glance Endpoint
│            └── http://gz:9292
│
├── RegionTwo
      ├── Nova Endpoint
      │      └── http://sh:8774
      │
      ├── Glance Endpoint
             └── http://sh:9292
```



##### 补充：OpenStack Interface（接口类型）详解

###### 什么是 Interface（接口类型）

在 OpenStack 中 “Interface” 是 Keystone Endpoint（服务端点）的一种分类方式。它用于区分同一个 OpenStack 服务应该通过哪种方式被访问

例如：

- 给普通用户访问
- 给 OpenStack 内部组件访问
- 给管理员访问



###### Interface 的本质

Interface本质上是 “同一个服务的不同访问入口分类”。

例如：同一个 Nova API，可以同时拥有：

| Interface | URL                          |
| --------- | ---------------------------- |
| public    | https://api.example.com:8774 |
| internal  | http://10.0.0.10:8774        |
| admin     | http://172.16.0.10:8774      |

虽然 URL不同，但最终访问的仍然是同一个 nova-api 服务。



###### OpenStack 中的三种 Interface

OpenStack 默认提供：

| Interface | 作用         |
| --------- | ------------ |
| public    | 公共访问接口 |
| internal  | 内部通信接口 |
| admin     | 管理接口     |



###### public Interface（公网接口）

**1. 作用**

用于：

- 普通用户
- 外部系统
- Horizon
- OpenStack CLI

访问 OpenStack。

**2. 常见特点**

 通常：

- 暴露公网
- 经过 HTTPS
- 经过 SLB / Nginx
- 配置 WAF
- 配置限流

**3. 示例**

```http
https://openstack.company.com:8774
```

**4. 典型场景**

```bash
openstack server create
```

CLI 通常会访问 “compute + public endpoint”



###### internal Interface（内部接口）

**1. 作用**

用于：OpenStack 内部组件之间通信。

例如：

- Nova 调 Neutron
- Cinder 调 Glance
- Scheduler 调 Placement

**2. 常见特点**

通常：

- 使用管理网络
- 不开放公网
- 延迟低
- 更安全

**3. 示例**

```http
http://10.0.0.10:8774
```

**4. 典型场景**

例如：

```bat
nova-compute -> 访问 neutron API
```

此时通常会走 “internal endpoint”，而不是公网。



###### admin Interface（管理接口）

**1. 作用**

用于：

- 管理员
- 运维
- 后台管理系统

执行管理操作。

**2. 常见特点**

通常：

- 只允许管理网访问
- VPN/堡垒机访问
- 不开放公网

**3. 示例**

```http
http://172.16.0.10:8774
```

**4. 常见用途**

例如：

- 修改配额
- 删除实例
- 管理租户
- 运维审计



###### Interface 的真正价值

Interface的核心价值：是 “**访问路径分层”**



###### 生产中的典型网络划分

真实生产环境：
```bat
公网
│
├── public endpoint
│
管理网络
│
├── internal endpoint
│
运维网络
│
├── admin endpoint
```









## OpenStack IAM 与 Keystone 认证授权体系详解 — 从 Domain 到 Fernet Token 的完整实现机制



**本章目标**

系统掌握 OpenStack 的：

- 身份认证体系（Authentication）
- 权限授权体系（Authorization）
- 多租户体系（Multi-Tenancy）
- Token 机制
- Keystone 工作原理
- Policy 权限控制机制

并彻底理解：OpenStack 为什么能实现 “统一认证 + 分布式权限控制”



### 什么是 IAM

IAM 全称：`Identity and Access Management`，即：**身份与访问管理系统。**

IAM 核心解决：

| 问题         | 示例             |
| ------------ | ---------------- |
| 你是谁       | 用户认证         |
| 你属于谁     | Domain / Project |
| 你是什么身份 | Role             |
| 你能做什么   | Policy           |
| 如何证明自己 | Credentials      |
| 如何访问服务 | Token            |



### OpenStack IAM 核心组件

在 OpenStack 中 IAM 由 KeyStone 实现。

Keystone 负责：

| 功能         | 说明               |
| ------------ | ------------------ |
| 用户认证     | Authentication     |
| Token 签发   | Token Issue        |
| 身份管理     | User / Group       |
| 多租户管理   | Project / Domain   |
| 服务目录管理 | Endpoint / Catalog |
| 权限身份管理 | Role Assignment    |



### OpenStack IAM 总体架构（核心）

```bat
Credentials
    │
    ▼
Keystone
    │
    ├── User
    ├── Group
    ├── Project
    ├── Role
    ├── Token
    └── Service Catalog
    │
    ▼
Nova / Neutron / Cinder
    │
    ▼
Policy
    │
    ▼
Allow / Deny
```



### Domain（域）

#### Domain 是什么

Domain 是 KeyStone 中的顶层组织隔离边界。

用于隔离：

- 用户
- 用户组
- 项目



#### Domain 示例

```bat
Domain: company-a
├── User: zhangsan
├── Group: dev-team
└── Project: ecommerce-prod
```



#### Domian 的作用

用于：

- 多公司隔离
- 多客户隔离
- 多组织隔离



#### 查看 Domain

```bash
[root@gz-controller1 ~]# openstack domain list
+---------+---------+---------+--------------------+
| ID      | Name    | Enabled | Description        |
+---------+---------+---------+--------------------+
| default | Default | True    | The default domain |
+---------+---------+---------+--------------------+
```



### Project（项目）

#### Project 是什么

Project 以前叫 `Tenant`，现在统一称：`Project`。它是 **OpenStack 的资源租户空间**。

Project 的本质是

```bat
Project = 资源边界
```



#### Project 管理什么

Project 下通常包含：

- VM
- Network
- Volume
- Security Group
- Floating IP

等资源。



#### Project 的作用

| 功能       | 说明              |
| ---------- | ----------------- |
| 资源归属   | VM属于哪个项目    |
| 资源隔离   | 不同项目互相隔离  |
| 配额管理   | CPU/内存/磁盘限制 |
| 权限作用域 | Role Assignment   |



#### Project 示例

```bat
Project: ecommerce-prod
├── web01            # 实例
├── mysql01          # 实例
├── prod-network     # 网络资源
└── prod-volume      # 存储资源
```



#### 查看 Project

```bat
[root@gz-controller1 ~]# openstack project list
+----------------------------------+---------+
| ID                               | Name    |
+----------------------------------+---------+
| 546fb5e605354a52bc5fcdec78a0db9b | admin   |
| e62a640e1b1a4a3e8f3c9e010728b4f9 | service |
+----------------------------------+---------+
```



### User（用户）

#### User 是什么

User 表示操作者身份，本质上：

```bat
user = 谁在操作
```

User 属于 Domain 下的资源

添加  User

```bash
[root@gz-controller1 ~]# openstack user create --domain default zhangsan
No password was supplied, authentication will fail when a user does not have a password.
+---------------------+----------------------------------+
| Field               | Value                            |
+---------------------+----------------------------------+
| domain_id           | default                          |
| enabled             | True                             |
| id                  | 15c4ee48734c459cbffce401016f2491 |
| name                | zhangsan                         |
| options             | {}                               |
| password_expires_at | None                             |
+---------------------+----------------------------------+
```

查看 User

```bash
[root@gz-controller1 ~]# openstack user list
+----------------------------------+-----------+
| ID                               | Name      |
+----------------------------------+-----------+
| 15c4ee48734c459cbffce401016f2491 | zhangsan  |
| ff1850b740aa4cc3bde9d038adbffe54 | admin     |
| 3ff42198d9164355bf47aa7a7ecd499b | placement |
| 1a139355a8e446f7903107c381d12c06 | glance    |
| 03229ea157cc4630af6dd2243473cf77 | cinder    |
| 630d2d4dcad841a3b38badcc3d4c9906 | neutron   |
| b282d168b687415eb637ed5215214061 | nova      |
+----------------------------------+-----------+
```



### Group（用户组）

Group 是用户集合，用于批量授权。

**示例**

```bat
Group: dev-team
├── zhangsan
├── lisi
└── wangwu
```



#### Group 的作用示例

```bat
dev-team -> Project:dev -> Role:member
```

则组内所有用户自动获得：

```bat
dev 项目的 member 权限
```



#### 查看 Group

```bash
[root@gz-controller1 ~]# openstack group list
```



### Role（角色）

Role 是**权限身份标签**

例如：

| Role   | 含义     |
| ------ | -------- |
| admin  | 管理员   |
| member | 普通成员 |
| reader | 只读用户 |



#### Role 是全局资源（重点）

Role 通常不属于某个 Domain 或 Project。他是 **Keystone 全局对象**。

**查看 Role**

```bash
[root@gz-controller1 ~]# openstack role list
+----------------------------------+---------+
| ID                               | Name    |
+----------------------------------+---------+
| 174fd42cecd14980aad55bcb4228735c | manager |
| 3200c78c1cf04462bbea8a882f33cd5b | admin   |
| 388b8748f462477695843031667eff1c | member  |
| 4e7c726cd79040778263003e73e33449 | service |
| 5f71422b24ca48ab9baf83ce0b40b621 | reader  |
+----------------------------------+---------
```



### Role Assignment（核心）

Keystone 权限模型不是 `User -> Role` 而是 User 在某个 Project 中拥有某个 Role

即：`(User, Project, Role)` 三元组关系。

**示例**

| User     | Project | Role   |
| -------- | ------- | ------ |
| zhangsan | dev     | admin  |
| zhangsan | prod    | reader |

表示：

```bat
zhangsan 在 dev 是管理员，
zhangsan 在 prod 只能查看。
```



**查看授权关系**

```bash
[root@gz-controller1 ~]# openstack role assignment list --names
+---------+-------------------+-------+-----------------+--------+--------+-----------+
| Role    | User              | Group | Project         | Domain | System | Inherited |
+---------+-------------------+-------+-----------------+--------+--------+-----------+
| admin   | cinder@Default    |       | service@Default |        |        | False     |
| admin   | glance@Default    |       | service@Default |        |        | False     |
| admin   | placement@Default |       | service@Default |        |        | False     |
| admin   | neutron@Default   |       | service@Default |        |        | False     |
| admin   | nova@Default      |       | service@Default |        |        | False     |
| service | nova@Default      |       | service@Default |        |        | False     |
| admin   | admin@Default     |       | admin@Default   |        |        | False     |
| admin   | admin@Default     |       |                 |        | all    | False     |
+---------+-------------------+-------+-----------------+--------+--------+-----------+
```



**授权用户的命令**

```bash
[root@gz-controller1 ~]# openstack role add --project demo --user zhangsan admin
```



### Credentials（认证凭据）

Credentials是向 Keystone 证明身份的材料。



**常见 Credentials**

| 类型                   | 示例             |
| ---------------------- | ---------------- |
| 用户名密码             | admin / password |
| Application Credential | app credential   |
| Token                  | Token 换 Token   |
| LDAP                   | 外部认证         |
| Access Key             | EC2风格认证      |



**最常见形式**

```bash
# 用户名密码，以环境变量的形式存在
export OS_USERNAME=admin
export OS_PASSWORD=123456
export OS_PROJECT_NAME=admin
```



### Token（令牌）

Token 是 Keystone 签发的：临时访问凭证。

Token 的本质是 “加密后的身份上下文”，Token中通常包含：

- user_id
- project_id
- roles
- expires
- audit_id

等信息。



**Token 示例**

```bash
[root@gz-controller1 ~]# openstack token issue 
+------------+----------------------------------------------------------------------------------------------------------------+
| Field      | Value                                                                                                           
+------------+-----------------------------------------------------------------------------------------------------------------+
| expires    | 2026-05-09T03:57:44+0000                                                                                        |
| id         | gAAAAABp_qKoxoaHwY5YLmSmMY9lGJPRx92f8kFEcOhehFBfXmddIjpRm4CHq_N2eQ51CbBVwRCDQOR6xIMG7QNtqf_0axExTUtFosDm0KDvvYPOCGmFbuS2AWhWEqYLq7lgzkrAKLMsB80LlVIbyLyo_CqX56fArrHOR5306HSj2Aj1gfvsV0A |
|
| project_id | 546fb5e605354a52bc5fcdec78a0db9b                                                                                 |
| user_id    | ff1850b740aa4cc3bde9d038adbffe54                                                                                |
+------------+---------------------------------------------------------------------------------------------------------------+

# 根据上述输出，Token值是id: gAAAAABp_qKoxoaHwY5YLmSmMY9lGJPRx92f8kFEcOhehFBfXmddIjpRm4CHq_N2eQ51CbBVwRCDQOR6xIMG7QNtqf_0axExTUtFosDm0KDvvYPOCGmFbuS2AWhWEqYLq7lgzkrAKLMsB80LlVIbyLyo_CqX56fArrHOR5306HSj2Aj1gfvsV0A
```



#### 现代 OpenStack 使用 Fernet Token

现代 OpenStack 默认使用 Fernet Token。

##### Fernet Token 本质

```bat
身份上下文
↓
msgpack序列化
↓
Fernet加密
↓
Base64编码
```



##### Fernet Token 优势

| 优势   | 说明       |
| ------ | ---------- |
| 无状态 | 无需数据库 |
| 高性能 | 本地验证   |
| 高扩展 | 适合大型云 |
| 高安全 | AES + HMAC |



##### Fernet Key

Key 的作用是

- Token 加密
- Token 解密
- Token 验签

> 所有 Controller 都必须能验证 / 解密 Token。因此多 Controller 必须同步 Key



##### Key的位置

```bash
[root@gz-controller1 ~]# ls /etc/keystone/fernet-keys/
0  1
```



##### Fernet Key 类型和轮替

Fernet使用3种类型的 fernet 密钥，存放在 `/etc/keystone/fernet-keys` 目录下，密钥文件名称使用数字命名，最大的数字中包含当前主密钥（primary key），用来生成新的token并加密已有的 fernet token。 

- **0 包含暂存密钥**，并一直是数字0，这里的密钥会在下一次密钥轮替的时候被提升为主密钥;
- 1和2，包含**次密钥**（secondary key）
- 3，包含主密钥（primary key），这个数字在密钥轮替时会增加，**最大的数字总是作为主密钥提供**。



![image-20260510151613949](D:\git_repository\cyber_security_learning\markdown_img\image-20260510151613949.png)

```bash
# 轮替 Fernet Key 演示
[root@gz-controller1 ~]# ls /etc/keystone/fernet-keys/
0  1

[root@gz-controller1 ~]# keystone-manage fernet_rotate --keystone-user keystone --keystone-group keystone
2026-05-10 15:33:51.031 77406 INFO keystone.common.fernet_utils [-] Starting key rotation with 2 key files: ['/etc/keystone/fernet-keys/1', '/etc/keystone/fernet-keys/0']
2026-05-10 15:33:51.034 77406 INFO keystone.common.fernet_utils [-] Created a new temporary key: /etc/keystone/fernet-keys/0.tmp
2026-05-10 15:33:51.034 77406 INFO keystone.common.fernet_utils [-] Current primary key is: 1
2026-05-10 15:33:51.034 77406 INFO keystone.common.fernet_utils [-] Next primary key will be: 2
2026-05-10 15:33:51.035 77406 INFO keystone.common.fernet_utils [-] Promoted key 0 to be the primary: 2
2026-05-10 15:33:51.035 77406 INFO keystone.common.fernet_utils [-] Become a valid new key: /etc/keystone/fernet-keys/0

# 再次查看
[root@gz-controller1 ~]# ls /etc/keystone/fernet-keys/
0  1  2
```



 



##### Token 解密实验

```bash
#更新Token
[root@gz-controller1 ~]# openstack token issue 
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field      | Value                                                                                                                                                                                   |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| expires    | 2026-05-09T03:57:44+0000                                                                                                                                                                |
| id         | gAAAAABp_qKoxoaHwY5YLmSmMY9lGJPRx92f8kFEcOhehFBfXmddIjpRm4CHq_N2eQ51CbBVwRCDQOR6xIMG7QNtqf_0axExTUtFosDm0KDvvYPOCGmFbuS2AWhWEqYLq7lgzkrAKLMsB80LlVIbyLyo_CqX56fArrHOR5306HSj2Aj1gfvsV0A |
| project_id | 546fb5e605354a52bc5fcdec78a0db9b                                                                                                                                                        |
| user_id    | ff1850b740aa4cc3bde9d038adbffe54                                                                                                                                                        |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

```python
# 使用脚本解密token，Python脚本内容如下
[root@gz-controller1 ~]# cat decrypt2.py 
from cryptography.fernet import Fernet, InvalidToken
import os
import msgpack

token = os.popen("openstack token issue -f value -c id").read().strip()

missing_padding = len(token) % 4
if missing_padding:
    token += "=" * (4 - missing_padding)

key_dir = "/etc/keystone/fernet-keys"

for key_name in sorted(os.listdir(key_dir)):
    key_path = os.path.join(key_dir, key_name)

    with open(key_path, "rb") as f:
        key = f.read().strip()

    try:
        fernet = Fernet(key)
        plaintext = fernet.decrypt(token.encode())

        print(f"[+] 使用 key {key_name} 解密成功")
        print("\n[+] 原始 payload:")
        print(plaintext)

        print("\n[+] msgpack 解析结果:")
        data = msgpack.unpackb(plaintext, raw=False)
        print(data)

        break

    except InvalidToken:
        print(f"[-] key {key_name} 解密失败")
```

执行脚本

```bash
[root@gz-controller1 ~]# python3 decrypt2.py 
[-] key 0 解密失败
[+] 使用 key 1 解密成功

[+] 原始 payload:
b'\x96\x02\x92\xc3\xc4\x10\xff\x18P\xb7@\xaaL\xc3\xbd\xe9\xd08\xad\xbf\xfeT\x02\x92\xc3\xc4\x10To\xb5\xe6\x055JR\xbc_\xcd\xecx\xa0\xdb\x9b\xcbA\xda\x7f\xac/\xc0\x00\x00\x91\xc4\x10\xfc^\xe8j=\x08B \x98)?\xef\x12P\x17\xfe'

[+] msgpack 解析结果:
[2, [True, b'\xff\x18P\xb7@\xaaL\xc3\xbd\xe9\xd08\xad\xbf\xfeT'], 2, [True, b'To\xb5\xe6\x055JR\xbc_\xcd\xecx\xa0\xdb\x9b'], 1778299071.0, [b'\xfc^\xe8j=\x08B \x98)?\xef\x12P\x17\xfe']]
```

成功得到解密后的结果

```json
[
  2,
  [True, b'\xff\x18P...'],
  2,
  [True, b'To\xb5...'],
  1778298961.0,
  [b"c@\xcc..."]
]
```

大致对应

```bat
[
  user_id 类型/版本,
  user_id 的二进制压缩形式,
  project_id 类型/版本,
  project_id 的二进制压缩形式,
  expires_at 过期时间戳,
  audit_ids
]
```

`b'\xff\x18P...'`这部分字符不是乱码，而是**UUID 的二进制压缩形式**。Keystone 没有直接存：`ff1850b740aa4cc3bde9d038adbffe54`‘。而是把这个 32 位十六进制 UUID 压成 16 字节 bytes，节省 Token 长度。

使用脚本继续把它转成人能读懂的UUID:

```python
[root@gz-controller1 ~]# cat zh.py 
import uuid

user_id = uuid.UUID(bytes=b'\xff\x18P\xb7@\xaaL\xc3\xbd\xe9\xd08\xad\xbf\xfeT')
project_id = uuid.UUID(bytes=b'To\xb5\xe6\x055JR\xbc_\xcd\xecx\xa0\xdb\x9b')

print(user_id.hex)
print(project_id.hex)
```

执行后对比

```bash
[root@gz-controller1 ~]# python3 zh.py 
ff1850b740aa4cc3bde9d038adbffe54
546fb5e605354a52bc5fcdec78a0db9b
```

查看结果可以发现，输出结果正好是 project_id 和 user_id。进而证明 Token 里是携带信息的。









### Policy（权限策略）

Policy 是真正的权限规则。

```bat
Policy 的本质 -> API 权限判断规则
```

权限并不是 keystone 判断的。而是：

| 服务    | 权限判断 |
| ------- | -------- |
| Nova    | VM       |
| Neutron | 网络     |
| Cinder  | 存储     |

这些组件根据 Policy 决定 Allow / Deny。



#### Policy 示例

```ini
"os_compute_api:servers:create": "role:member"
```

表示：member 可以创建 VM



#### 现代 Policy 机制（重点）

现代 OpenStack 已经开始默认策略内置到代码。

**默认配置查看**

```bash
# 导出 nova 的 policy 文件
[root@gz-computer1 ~]# oslopolicy-policy-generator \
--namespace nova \
--output-file nova-policy.yaml
WARNING:oslo_policy.policy:JSON formatted policy_file support is deprecated since Victoria release. You need to use YAML format which will be default in future. You can use ``oslopolicy-convert-json-to-yaml`` tool to convert existing JSON-formatted policy file to YAML-formatted in backward compatible way: https://docs.openstack.org/oslo.policy/latest/cli/oslopolicy-convert-json-to-yaml.html.
WARNING:oslo_policy.policy:JSON formatted policy_file support is deprecated since Victoria release. You need to use YAML format which will be default in future. You can use ``oslopolicy-convert-json-to-yaml`` tool to convert existing JSON-formatted policy file to YAML-formatted in backward compatible way: https://docs.openstack.org/oslo.policy/latest/cli/oslopolicy-convert-json-to-yaml.html.

# 查看
[root@gz-computer1 ~]# ls
anaconda-ks.cfg  nova-policy.yaml

# 查看导出的文件
[root@gz-computer1 ~]# cat nova-policy.yaml 
"context_is_admin": "role:admin"
"admin_or_owner": "is_admin:True or project_id:%(project_id)s"
"admin_api": "is_admin:True"
"project_member_api": "role:member and project_id:%(project_id)s"
"project_reader_api": "role:reader and project_id:%(project_id)s"
"project_member_or_admin": "rule:project_member_api or rule:context_is_admin"
"project_reader_or_admin": "rule:project_reader_api or rule:context_is_admin
......
```

观察 Policy 文件

```bash
[root@gz-computer1 ~]# cat /etc/nova/policy.json 
{
}
```

可以看到 Policy 文件是空的。



**最终生效策略：**

运行时 Nova 会对 `默认策略` 和 `Policy.json 中的自定义项` 进行合并（merge）。



### OpenStack IAM 的完整真实工作流

**1. 用户提交 Credentials**

例如：

```
username/password
```

给：

```
Keystone
```

**2. Keystone 认证成功**

查询：

- User
- Project
- Role Assignment

**3. Keystone 签发 Fernet Token**

Token 中：

包含：

- user_id
- project_id
- roles
- expires
- service catalog

等信息。

**4. 用户访问 Nova API**

携带：

```
X-Auth-Token
```

**5. Keystone Middleware 校验 Token**

完成：

- 验签
- 检查过期
- 解密
- msgpack解析

**6. Middleware 构造 Context**

例如：

```
context.user_id
context.project_id
context.roles
```

**7. Nova 执行 Policy**

例如：

```
role:member
```

是否允许：

```
servers:create
```

**8. Allow / Deny**

**9. 返回 HTTP 状态码**

| 状态码 | 含义       |
| ------ | ---------- |
| 200    | 成功       |
| 201    | 创建成功   |
| 401    | 未认证     |
| 403    | 无权限     |
| 404    | 资源不存在 |

**总结**

```bat
用户使用 OpenStack Client 首先向 Keystone 提交 Credentials（用户名密码等认证凭据）。

Keystone 对用户进行认证，并查询：
- User
- Project
- Role Assignment

认证成功后，Keystone 会签发 Fernet Token，
并在认证响应中返回 Token 与 Service Catalog。

Service Catalog 中包含 Nova、Neutron、Cinder、Glance 等 OpenStack 服务的 Endpoint 信息，
客户端根据 Region 与 Interface 选择对应服务的访问地址。

随后，OpenStack Client 携带 Token 直接访问对应 OpenStack 服务，例如 Nova API。

OpenStack 服务中的 Keystone Middleware 会对 Token 进行：
- 验签
- 有效期检查
- 解密
- 解析

并从中获取：
- user_id
- project_id
- roles
- expires
- audit_id

等身份上下文信息。

Middleware 随后构造 Request Context，
并将其传递给 Nova、Neutron、Cinder 等具体服务。

然后，各 OpenStack 服务根据自身 Policy 规则，
结合 Request Context 中的身份信息，
判断当前请求是否具备执行对应 API 操作的权限。

如果权限校验通过，则执行操作并返回成功状态；
如果 Token 无效或已过期，则返回 401 Unauthorized；
如果 Token 有效但权限不足，则返回 403 Forbidden。
```





## Keystone Middleware 工作机制

### 什么是 Keystone Middleware

Keystone Middleware 是 OpenStack 中**统一认证中间件（Authentication Middleware）**。

> 它的本质是：一个被各 OpenStack API 服务共享使用的 **Python 中间件库**。

Keystone Middleware：

主要负责：

- 提取 Token
- Token Cache 检查
- 必要时调用 Keystone，接收 Keystone 返回的 token_data
- 构造 Request Context



#### Keystone Middleware 的本质

Keystone Middleware 是 Python Middleware Library。通常安装后位于：

```ABAP
/usr/lib/python3*/site-packages/keystonemiddleware/
```



#### Keystone 与 Middleware 的关系

| 组件                | 职责                                 |
| ------------------- | ------------------------------------ |
| Keystone            | 签发并验证身份（Token）              |
| Keystone Middleware | 接受token_data并构造 Request context |
| Nova/Neutron/Cinder | 执行业务逻辑                         |
| Policy              | 决定是否允许操作                     |



#### 完整认证链路（核心）

```bat
Client 携带 Token 访问 Nova
↓
Nova 内部的 keystonemiddleware 先查 token 缓存
↓
缓存命中：直接使用缓存中的 token 验证结果
↓
缓存未命中/过期：keystonemiddleware 调用 Keystone 的 Token Validate API
↓
Keystone 负责解密/校验 Fernet Token，并返回 token_data
↓
Middleware 把 token_data 转换成环境变量/Request Context
↓
Nova 再根据 Policy 做权限判断
```

OpenStack 官方对 `auth_token` middleware 的描述就是：它通过向 auth service 验证 token 来确认客户端请求有效，并收集/转发 token 中的身份信息。 Keystone 文档也明确说 Fernet Token 的加解密 key 应该只由 Identity service 持有。



#### Openstack 各组件什么时候会和 Keystone 通信？

主要是这几类情况。

##### 1. Token 缓存没有命中

第一次用某个 Token 访问 Nova 时，Nova 侧的 keystonemiddleware 本地还没有这个 Token 的验证结果。

于是它会请求 Keystone：

```bat
请帮我验证这个 Token 是否有效，
并返回 user/project/roles 等身份信息。
```

Keystone 校验成功后，把 token_data 返回给 middleware，middleware 再缓存一段时间。



##### 2. token_cache_time 过期

例如：

```ini
[keystone_authtoken]
token_cache_time = 300
```

含义是：同一个 Token 的验证结果缓存 300 秒。Red Hat 配置说明也把它描述为“为了避免过度验证 token，middleware 会缓存已见过的 token 一段可配置时间”。

所以：

```bat
300 秒内：
Nova middleware 直接使用缓存结果

300 秒后：
下一次请求到来时，Nova middleware 重新找 Keystone 验证 Token
```

这个时候会和 Keystone 通信。



##### 3. Token 无法解析/验证

注意：在标准架构里，**不是 Nova 自己解析 Fernet Token**，而是 Keystone 解析。

所以如果 middleware 把 Token 发给 Keystone 后，Keystone 发现：

```bat
Token 格式不对
签名不对
Token 被篡改
Token 已过期
Fernet Key 不匹配
```

Keystone 会返回失败，Nova 最终返回 401。

这里不是 Nova 去 Keystone “重新申请 key”。Fernet Key 不会通过 API 自动下发给 Nova。Key 是 Keystone 侧的核心密钥，标准要求只有 Identity service 持有。



##### 4. 组件服务用户需要认证

Nova、Neutron、Cinder 这些组件自己也有服务用户，例如：

```ini
[keystone_authtoken]
auth_url = http://controller:5000
project_name = service
username = nova
password = NOVA_PASS
```

这些配置不是普通用户的账号，而是组件自己的 service user。

Middleware 或组件在需要访问 Keystone 验证用户 Token 时，必须证明：

```bat
我是合法的 nova 服务
我有资格向 Keystone 查询/验证 Token
```

所以它会使用 `username=nova`、`password=NOVA_PASS` 这类服务凭据与 Keystone 通信。



##### 5. Token 吊销/缓存安全相关场景

`token_cache_time` 越长，性能越好，但吊销感知越慢。OpenStack 性能文档也提到：增加 `token_cache_time` 可以提升性能，降低它可以更快响应 token revocation 事件，从而提高安全性。

举例：
```ini
token_cache_time = 300
```

如果某个 Token 已经被验证并缓存，管理员随后禁用了用户，那么在缓存过期前，组件可能仍然使用旧缓存。

如果你把它改小：

```ini
token_cache_time = 30
```

那么组件更频繁向 Keystone 重新验证 Token，吊销/禁用的感知会更快，但 Keystone 压力更大。



##### 把几种场景串成例子

**场景 1：正常第一次访问**

```bat
Client → Nova：X-Auth-Token: gAAAA...
Nova middleware：缓存没有
Nova middleware → Keystone：请验证这个 token
Keystone：解密 Fernet Token，检查 expires，返回 token_data
Nova middleware：缓存 token_data
Nova：根据 Context + Policy 判断权限
```

**场景 2：缓存期内再次访问**

```bat
Client → Nova：同一个 Token
Nova middleware：缓存命中
Nova middleware：不访问 Keystone
Nova：直接使用缓存身份上下文做 Policy 判断
```

**场景 3：缓存过期后再次访问**

```bat
Client → Nova：同一个 Token
Nova middleware：缓存过期
Nova middleware → Keystone：重新验证 Token
Keystone：返回新的验证结果或拒绝
```

**场景 4：Token 被篡改**

```bat
Client → Nova：伪造/篡改 Token
Nova middleware → Keystone：验证 Token
Keystone：验签失败 / 解密失败
Nova：返回 401 Unauthorized
```

**场景 5：权限不足**

```bat
Token 有效
Keystone 返回 user/project/roles
Nova Policy 判断该 role 不能执行 API
Nova：返回 403 Forbidden
```



#### 总结

```bat
keystonemiddleware 是各 OpenStack API 服务内部使用的 Python 认证中间件。

它会缓存 Token 验证结果。

缓存命中时，不访问 Keystone；
缓存未命中或缓存过期时，会调用 Keystone 验证 Token。

Fernet Token 的加解密密钥通常只由 Keystone 持有，
Nova/Neutron/Cinder 不会向 Keystone 动态申请 Fernet Key。

Keystone 验证 Token 后返回身份上下文，
Middleware 再把这些信息交给具体组件用于 Policy 权限判断。
```

![image-20260510011020548](D:\git_repository\cyber_security_learning\markdown_img\image-20260510011020548.png)





## keystone 管理命令

### 签发令牌

```ABAP
openstack token issue
```

`openstack token issue` 是 OpenStack 中最常用的认证测试命令之一。

它的核心作用：向 Keystone（身份认证服务）申请一个 Token，并显示当前认证结果。

你可以把它理解成：“我拿用户名、密码、项目这些信息，去 Keystone 登录一次，看看认证是否成功。”



#### 他到底干了什么？

当你执行：

```ABAP
openstack token issue
```

实际上背后发生的是：

```bat
OpenStack Client
        ↓
读取环境变量（OS_USERNAME 等）
        ↓
向 Keystone 发起认证请求
        ↓
Keystone 验证：
- 用户是否存在
- 密码是否正确
- project 是否存在
- 用户是否属于该 project
        ↓
认证成功后：
生成 Token
        ↓
返回 token + 用户信息 + project 信息
```

`openstack token issue` 默认输出里不会直接明确写：`scoped token` 还是 `unscoped token`

但实际上：它生成的大多数都是 Scoped Token（有范围 Token）。只是 OpenStack Client 没直接把这个词打印出来。



##### 什么叫 Scoped / Unscoped Token？

这是 Keystone 认证体系里的核心概念。

**1. Unscoped Token（无范围 Token）**

只有：`你是谁`，没有：`“你属于哪个 project”`，也没有 `“你在什么租户里操作”`

相当于：**“登录成功了，但还没进入任何项目”**



**2. Scoped Token（有范围 Token）**

不仅知道：

```ABAP
你是谁
```

还知道：

```ABAP
你在哪个 project，你有什么权限
```

例如：

```ABAP
admin project
service project
demo project
```



##### 为什么 OpenStack 大多数命令都需要 Scoped Token？

因为 OpenStack 资源都是：**Project（租户）隔离的**

例如：

- VM
- 网络
- Volume
- Floating IP

都属于某个 project。所以：

```bat
[root@gz-controller1 ~]# openstack server list
```

必须知道：

```bat
你要看哪个 project 的虚拟机
```

因此：**Nova / Neutron 基本都要求 Scoped Token**



##### 如何判断 `openstack token issue` 返回的是 Scoped Token？

关键看：

```ABAP
project_id
project_name
```

示例：

```bat
[root@gz-controller1 ~]# openstack token issue 
+------------+----------------------------------+
| Field      | Value                            |
+------------+----------------------------------+
| expires    | 2026-05-10T10:30:00+0000        |
| id         | gAAAAABo...                     |
| project_id | 8f1b0d...                       |
| user_id    | 7a2c...                         |
+------------+----------------------------------+
```

这里：

```ABAP
project_id
```

已经说明：这是 Scoped Token。因为：Token 已经绑定到某个 Project。

OpenStack CLI 默认就会自动申请 Scoped Token，当你配置了：

```ABAP
export OS_PROJECT_NAME=admin
```

所以

```bat
Client 自动申请：“admin project 范围内的 token”
```



##### Keystone 设计 Unscoped Token 的意义

因为有些用户：**属于多个 Project**。因此 Keystone 需要先确定 “你是谁”，再让你选择 “你要进入哪个 project”。于是流程变成：

```bat
用户名密码
↓
获取 Unscoped Token
↓
选择 project
↓
换 Scoped Token
```

示例：

老版本 v2 的 Horizon（OpenStack Web界面），网页登录使用用户名和密码，先获取 **Unscoped Token** 然后如果你属于多个项目：弹出 project 选择，再换 Scoped Token。

但是在新版本的 Horizon 的实际行为是

```bat
登录时：
直接获取默认项目的 Scoped Token

切换项目时：
重新获取新的 Scoped Token
```

因此 Unscoped Token 在现在的实际生产中用的比较少，常见于：

- Keystone IAM 开发
- 多租户门户系统
- Keystone API 调试等





#### 最常见用途（生产里天天用）

**1. 验证 OpenStack 是否能正常认证（最重要）**

```bash
source admin-openrc
openstack token issue
```

如果成功：则说明：

- Keystone 正常
- 数据库正常
- 用户存在
- 密码正确
- API 正常
- endpoint 正常
- 环境变量正常

这其实是 **“OpenStack 是否活着”的第一检测命令**



#### 它会读取哪些环境变量？

```bat
[root@gz-controller1 ~]# cat admin-openrc 
export OS_USERNAME=admin
export OS_PASSWORD=JzycczIrOmPZsa8u
export OS_PROJECT_NAME=admin
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
export OS_AUTH_URL=http://gz-controller1:5000/v3
export OS_REGION_NAME=RegionOne
export OS_IDENTITY_API_VERSION=3

[root@gz-controller1 ~]# openstack token issue 
+------------+----------------------------------+
| Field      | Value                            |
+------------+----------------------------------+
| expires    | 2026-05-10T10:30:00+0000        |
| id         | gAAAAABo...                     |
| project_id | 8f1b0d...                       |
| user_id    | 7a2c...                         |
+------------+----------------------------------+
```

所以使用 openstack 命令前，需要先执行：

```bat
[root@gz-controller1 ~]# source admin-openrc 
```

本质是：给 openstack client 提供认证信息



#### 令牌签发本质与案例演示

Openstack 令牌签发的本质是 HTTP 的 API 请求。



##### 使用用户名和密码构建一个无范围令牌签发请求

无范围令牌签发请求脚本如下：

```bash
curl -i \
  -H "Content-Type: application/json" \
  -d '
{
  "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "default" },
          "password": "JzycczIrOmPZsa8u"
        }
      }
    }
  }
}' \
"http://gz-controller1:5000/v3/auth/tokens" ; echo
```

返回结果：

```bash
HTTP/1.1 201 CREATED
Date: Mon, 11 May 2026 03:10:36 GMT
Server: Apache/2.4.62 (Rocky Linux) mod_wsgi/4.7.1 Python/3.9
Content-Length: 312
X-Subject-Token: gAAAAABqAUisCWLypKfJImanJbVOPxlK1YNZKNQk_YItjsUGPsTwfmmZdEH71qgkL2Z8Dy54YtU-VUuhUvQy11i48ZLBnfhczaM9x9n_5dXmla6sb-759T2e80tzoUMI92UzfYZ-1DDTIWOGe137yRGIGNXdhMqwlg
Vary: X-Auth-Token
x-openstack-request-id: req-b8beaca9-7299-4772-a897-a9241e0736bc
Content-Type: application/json

{"token": {"methods": ["password"], "user": {"domain": {"id": "default", "name": "Default"}, "id": "ff1850b740aa4cc3bde9d038adbffe54", "name": "admin", "password_expires_at": null}, "audit_ids": ["I3fMWMXjSNyJoL0gebwmgQ"], "expires_at": "2026-05-11T04:10:36.000000Z", "issued_at": "2026-05-11T03:10:36.000000Z"}}
```

实际的token id是放在X-Subject-Token头部字段里的，下面的是token的各种基本属性信息，比我们通过openstack token issue命令看到的更详细。



##### 使用用户名和密码构建项目级别令牌签发请求

```bash
curl -i \
  -H "Content-Type: application/json" \
  -d '
{
  "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "default" },
          "password": "JzycczIrOmPZsa8u"
        }
      }
    },
    "scope": {
      "project": {
        "name": "admin",
        "domain": { "id": "default" }
      }
    }
  }
}' \
"http://gz-controller1:5000/v3/auth/tokens" ; echo
```

返回结果：

```bat
HTTP/1.1 201 CREATED
Date: Mon, 11 May 2026 03:14:43 GMT
Server: Apache/2.4.62 (Rocky Linux) mod_wsgi/4.7.1 Python/3.9
Content-Length: 4203
X-Subject-Token: gAAAAABqAUmkNu2wXA0dSFnyc57RllZyYdr2O5O1he7obIcFIRSAkFOEvBwBEbshCM81ZfBn9zusPz_SxnwR_QLXfRkpViGIrI6wfZKjkFl9pKmlrUoe_sQgOY4EJC9zHVexNXhgUwfhKKs2zxPqTGwMGEc8jfYbqLCm2bp9KJ4TUOJ57G86UDI
Vary: X-Auth-Token
x-openstack-request-id: req-217dc3cc-01aa-449d-b729-25bf01046b91
Content-Type: application/json

{"token": {"methods": ["password"], "user": {"domain": {"id": "default", "name": "Default"}, "id": "ff1850b740aa4cc3bde9d038adbffe54", "name": "admin", "password_expires_at": null}, "audit_ids": ["whEWBlHxRHOfZ144HxJMrA"], "expires_at": "2026-05-11T04:14:44.000000Z", "issued_at": "2026-05-11T03:14:44.000000Z", "project": {"domain": {"id": "default", "name": "Default"}, "id": "546fb5e605354a52bc5fcdec78a0db9b", "name": "admin"}, "is_domain": false, "roles": [{"id": "388b8748f462477695843031667eff1c", "name": "member"}, {"id": "174fd42cecd14980aad55bcb4228735c", "name": "manager"}, {"id": "3200c78c1cf04462bbea8a882f33cd5b", "name": "admin"}, {"id": "5f71422b24ca48ab9baf83ce0b40b621", "name": "reader"}], "catalog": [{"endpoints": [{"id": "291891f3d150427abfb40d701f2d91af", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:8778", "region": "RegionOne"}, {"id": "2c1bec45d1e24500b0ad7e6a6392e8da", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:8778", "region": "RegionOne"}, {"id": "4f3b1434524f4a37aa44772ddd9850f3", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:8778", "region": "RegionOne"}], "id": "1aca8eb44f264a5a9590c74dfbff7225", "type": "placement", "name": "placement"}, {"endpoints": [{"id": "7bce5cf1b3fb4f99ba7860b20fc05754", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:9696", "region": "RegionOne"}, {"id": "7d010ce1f6cf4372914029e5382949cf", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:9696", "region": "RegionOne"}, {"id": "fbdda6eb58dd40cf9174039a583eca16", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:9696", "region": "RegionOne"}], "id": "6d7d9097530d4910841db48b08590ee3", "type": "network", "name": "neutron"}, {"endpoints": [{"id": "3076e1720f6443dc9e0ecd98f8a2e3fb", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:5000/v3/", "region": "RegionOne"}, {"id": "646d835290d540d185287fc5494f2ced", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:5000/v3/", "region": "RegionOne"}, {"id": "ba23b370774f45c5a8c8b52666cd5ccf", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:5000/v3/", "region": "RegionOne"}], "id": "82604998ff624d7db05715ea04a1f810", "type": "identity", "name": "keystone"}, {"endpoints": [{"id": "00db217b9ed04381858ec7501f58fb9c", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:8774/v2.1", "region": "RegionOne"}, {"id": "3658dfddb69d47dcb2976348eb13e021", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:8774/v2.1", "region": "RegionOne"}, {"id": "8ed86ec8a7e14bc59507526332ae38d9", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:8774/v2.1", "region": "RegionOne"}], "id": "8c2923a3f8024d35b496e778c59031ee", "type": "compute", "name": "nova"}, {"endpoints": [{"id": "880a2d67fb514cd7971bc8b86560bce0", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:9292", "region": "RegionOne"}, {"id": "e6cffed9f2ae46be977c388c4a0f2a9d", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:9292", "region": "RegionOne"}, {"id": "f718732cde204cabbe05a91fb7633426", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:9292", "region": "RegionOne"}], "id": "93de37d2c5c1415ab19e7e8a833ddc3e", "type": "image", "name": "glance"}, {"endpoints": [{"id": "0684789652f841b690f2079e15fac738", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:8776/v3/546fb5e605354a52bc5fcdec78a0db9b", "region": "RegionOne"}, {"id": "12344e19845342dc91155bcf1905131c", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:8776/v3/546fb5e605354a52bc5fcdec78a0db9b", "region": "RegionOne"}, {"id": "245a5afcf8ae40e29a831c76bb960285", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:8776/v3/546fb5e605354a52bc5fcdec78a0db9b", "region": "RegionOne"}], "id": "bffe1998e23347e3869fe9e10f8f7d71", "type": "volumev3", "name": "cinderv3"}]}}
```

可以看出，返回结果多出了 roles 和 catalog 的信息。



##### 使用用户名和密码构建域级别令牌签发请求

```bat
curl -i \
  -H "Content-Type: application/json" \
  -d '
{
  "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "default" },
          "password": "JzycczIrOmPZsa8u"
        }
      }
    },
    "scope": {
      "domain": {
        "id": "default"
      }
    }
  }
}' \
"http://gz-controller1:5000/v3/auth/tokens" ; echo
```

返回结果：

```bat
HTTP/1.1 401 UNAUTHORIZED
Date: Mon, 11 May 2026 03:17:14 GMT
Server: Apache/2.4.62 (Rocky Linux) mod_wsgi/4.7.1 Python/3.9
WWW-Authenticate: Keystone uri="http://gz-controller1:5000/v3"
Content-Length: 109
Vary: X-Auth-Token
x-openstack-request-id: req-59d21ec1-2f9c-4185-85fc-c9913f433903
Content-Type: application/json

{"error":{"code":401,"message":"The request you have made requires authentication.","title":"Unauthorized"}}
```

申请项目级 Token 成功，但是申请域级别 Token 返回 401 失败的原因是因为 `admin` 用户在 `admin` 项目上有角色授权，之前执行过

```ABAP
openstack role add --project admin --user admin admin
```

但是 `admin` 用户在 `default` 这个 domain 上并没有角色授权，因此在请求 **Domain Scoped Token** 的时候，Keystone 会认为：

```bat
你这个用户身份是真的，但你没有 default domain 的操作权限
```

所以返回:

```ABAP
401 Unauthorized
```

查看权限

```bat
[root@gz-controller1 ~]# openstack role assignment list --user admin --names
+-------+---------------+-------+---------------+--------+--------+-----------+
| Role  | User          | Group | Project       | Domain | System | Inherited |
+-------+---------------+-------+---------------+--------+--------+-----------+
| admin | admin@Default |       | test@Default  |        |        | False     |
| admin | admin@Default |       | admin@Default |        |        | False     |
| admin | admin@Default |       |               |        | all    | False     |
+-------+---------------+-------+---------------+--------+--------+-----------+
```

可以看到 Domain 确实为空，即 admin 用户确实没有域级别的授权。

因此只要我们添加域级别的授权，就能得到正确的 域级别的 token。

```bash
[root@gz-controller1 ~]# openstack role add \
  --user admin \
  --user-domain default \
  --domain default \
  admin
  
# 查看 admin 权限
+-------+---------------+-------+---------------+---------+--------+-----------+
| Role  | User          | Group | Project       | Domain  | System | Inherited |
+-------+---------------+-------+---------------+---------+--------+-----------+
| admin | admin@Default |       | test@Default  |         |        | False     |
| admin | admin@Default |       | admin@Default |         |        | False     |
| admin | admin@Default |       |               | Default |        | False     |
| admin | admin@Default |       |               |         | all    | False     |
+-------+---------------+-------+---------------+---------+--------+-----------+
```

申请域级别令牌再次尝试

```bat
[root@gz-controller1 ~]# curl -i   -H "Content-Type: application/json"   -d '
{
  "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "default" },
          "password": "JzycczIrOmPZsa8u"
        }
      }
    },
    "scope": {
      "domain": {
        "id": "default"
      }
    }
  }
}' "http://gz-controller1:5000/v3/auth/tokens" ; echo
```

返回

```bat
HTTP/1.1 201 CREATED
Date: Mon, 11 May 2026 03:19:59 GMT
Server: Apache/2.4.62 (Rocky Linux) mod_wsgi/4.7.1 Python/3.9
Content-Length: 3545
X-Subject-Token: gAAAAABqAUrgXbf1oUuyUGlgjhXcucwPmVSVK_0lqq9egx5vg22y4zfvhy0Exhuc0pUOVfb0Hn7ljpwIikFuUz-spZp2qnxPjTbR6g_wkGMVKiMAmOEauDJi7isPW1FS9W9qYLczlcPfkVtipoTnmXZe8RgEnjUQlw
Vary: X-Auth-Token
x-openstack-request-id: req-d31b5d61-47a3-4d02-ae50-e8eceb463cf2
Content-Type: application/json

{"token": {"methods": ["password"], "user": {"domain": {"id": "default", "name": "Default"}, "id": "ff1850b740aa4cc3bde9d038adbffe54", "name": "admin", "password_expires_at": null}, "audit_ids": ["JlLg0pgfRBGF5cHPGqzZ_w"], "expires_at": "2026-05-11T04:20:00.000000Z", "issued_at": "2026-05-11T03:20:00.000000Z", "domain": {"id": "default", "name": "Default"}, "roles": [{"id": "388b8748f462477695843031667eff1c", "name": "member"}, {"id": "3200c78c1cf04462bbea8a882f33cd5b", "name": "admin"}, {"id": "174fd42cecd14980aad55bcb4228735c", "name": "manager"}, {"id": "5f71422b24ca48ab9baf83ce0b40b621", "name": "reader"}], "catalog": [{"endpoints": [{"id": "291891f3d150427abfb40d701f2d91af", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:8778", "region": "RegionOne"}, {"id": "2c1bec45d1e24500b0ad7e6a6392e8da", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:8778", "region": "RegionOne"}, {"id": "4f3b1434524f4a37aa44772ddd9850f3", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:8778", "region": "RegionOne"}], "id": "1aca8eb44f264a5a9590c74dfbff7225", "type": "placement", "name": "placement"}, {"endpoints": [{"id": "7bce5cf1b3fb4f99ba7860b20fc05754", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:9696", "region": "RegionOne"}, {"id": "7d010ce1f6cf4372914029e5382949cf", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:9696", "region": "RegionOne"}, {"id": "fbdda6eb58dd40cf9174039a583eca16", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:9696", "region": "RegionOne"}], "id": "6d7d9097530d4910841db48b08590ee3", "type": "network", "name": "neutron"}, {"endpoints": [{"id": "3076e1720f6443dc9e0ecd98f8a2e3fb", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:5000/v3/", "region": "RegionOne"}, {"id": "646d835290d540d185287fc5494f2ced", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:5000/v3/", "region": "RegionOne"}, {"id": "ba23b370774f45c5a8c8b52666cd5ccf", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:5000/v3/", "region": "RegionOne"}], "id": "82604998ff624d7db05715ea04a1f810", "type": "identity", "name": "keystone"}, {"endpoints": [{"id": "00db217b9ed04381858ec7501f58fb9c", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:8774/v2.1", "region": "RegionOne"}, {"id": "3658dfddb69d47dcb2976348eb13e021", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:8774/v2.1", "region": "RegionOne"}, {"id": "8ed86ec8a7e14bc59507526332ae38d9", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:8774/v2.1", "region": "RegionOne"}], "id": "8c2923a3f8024d35b496e778c59031ee", "type": "compute", "name": "nova"}, {"endpoints": [{"id": "880a2d67fb514cd7971bc8b86560bce0", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:9292", "region": "RegionOne"}, {"id": "e6cffed9f2ae46be977c388c4a0f2a9d", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:9292", "region": "RegionOne"}, {"id": "f718732cde204cabbe05a91fb7633426", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:9292", "region": "RegionOne"}], "id": "93de37d2c5c1415ab19e7e8a833ddc3e", "type": "image", "name": "glance"}, {"endpoints": [], "id": "bffe1998e23347e3869fe9e10f8f7d71", "type": "volumev3", "name": "cinderv3"}]}}
```



##### 使用无范围令牌构建一个有范围令牌签发请求

下面的示例脚本使用一个无范围的token请求一个有范围token：

```bash
#!/bin/bash

OS_TOKEN=gAAAAABqAUmkNu2wXA0dSFnyc57RllZyYdr2O5O1he7obIcFIRSAkFOEvBwBEbshCM81ZfBn9zusPz_SxnwR_QLXfRkpViGIrI6wfZKjkFl9pKmlrUoe_sQgOY4EJC9zHVexNXhgUwfhKKs2zxPqTGwMGEc8jfYbqLCm2bp9KJ4TUOJ57G86UDI

curl -i \
  -H "Content-Type: application/json" \
  -d '
{
  "auth": {
    "identity": {
      "methods": ["token"],
      "token": {
        "id": "'"$OS_TOKEN"'"
      }
    },
    "scope": {
      "project": {
        "name": "admin",
        "domain": {"id": "default"}
      }
    }
  }
}' \
"http://gz-controller1:5000/v3/auth/tokens" ; echo
```

返回结果：

```bat
HTTP/1.1 201 CREATED
Date: Mon, 11 May 2026 03:32:37 GMT
Server: Apache/2.4.62 (Rocky Linux) mod_wsgi/4.7.1 Python/3.9
Content-Length: 4238
X-Subject-Token: gAAAAABqAU3Vxe8ATKFkEDyzEXrFCYeKF_UixLdrUVivXZtGrtEHfbCjch9vcdpZTJ9RqBDBBZN3142cYu3v9LKe0vkxs5Gv2ExoA1UNWACn4nUI7oASYCgkHVjwgqTqzTts8Slq25y0Q_Vaf7miMwidoTGyRwsg1liXZ8QANy-uvejM4mCVIQ1mYNRzqIeMcSIh1Bx_Migi
Vary: X-Auth-Token
x-openstack-request-id: req-da6ab982-0e4d-486f-b608-4491e2ae14da
Content-Type: application/json

{"token": {"methods": ["token", "password"], "user": {"domain": {"id": "default", "name": "Default"}, "id": "ff1850b740aa4cc3bde9d038adbffe54", "name": "admin", "password_expires_at": null}, "audit_ids": ["DSPPZ-qdTS22Jnnc82yS5A", "whEWBlHxRHOfZ144HxJMrA"], "expires_at": "2026-05-11T04:14:44.000000Z", "issued_at": "2026-05-11T03:32:37.000000Z", "project": {"domain": {"id": "default", "name": "Default"}, "id": "546fb5e605354a52bc5fcdec78a0db9b", "name": "admin"}, "is_domain": false, "roles": [{"id": "5f71422b24ca48ab9baf83ce0b40b621", "name": "reader"}, {"id": "3200c78c1cf04462bbea8a882f33cd5b", "name": "admin"}, {"id": "388b8748f462477695843031667eff1c", "name": "member"}, {"id": "174fd42cecd14980aad55bcb4228735c", "name": "manager"}], "catalog": [{"endpoints": [{"id": "291891f3d150427abfb40d701f2d91af", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:8778", "region": "RegionOne"}, {"id": "2c1bec45d1e24500b0ad7e6a6392e8da", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:8778", "region": "RegionOne"}, {"id": "4f3b1434524f4a37aa44772ddd9850f3", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:8778", "region": "RegionOne"}], "id": "1aca8eb44f264a5a9590c74dfbff7225", "type": "placement", "name": "placement"}, {"endpoints": [{"id": "7bce5cf1b3fb4f99ba7860b20fc05754", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:9696", "region": "RegionOne"}, {"id": "7d010ce1f6cf4372914029e5382949cf", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:9696", "region": "RegionOne"}, {"id": "fbdda6eb58dd40cf9174039a583eca16", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:9696", "region": "RegionOne"}], "id": "6d7d9097530d4910841db48b08590ee3", "type": "network", "name": "neutron"}, {"endpoints": [{"id": "3076e1720f6443dc9e0ecd98f8a2e3fb", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:5000/v3/", "region": "RegionOne"}, {"id": "646d835290d540d185287fc5494f2ced", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:5000/v3/", "region": "RegionOne"}, {"id": "ba23b370774f45c5a8c8b52666cd5ccf", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:5000/v3/", "region": "RegionOne"}], "id": "82604998ff624d7db05715ea04a1f810", "type": "identity", "name": "keystone"}, {"endpoints": [{"id": "00db217b9ed04381858ec7501f58fb9c", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:8774/v2.1", "region": "RegionOne"}, {"id": "3658dfddb69d47dcb2976348eb13e021", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:8774/v2.1", "region": "RegionOne"}, {"id": "8ed86ec8a7e14bc59507526332ae38d9", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:8774/v2.1", "region": "RegionOne"}], "id": "8c2923a3f8024d35b496e778c59031ee", "type": "compute", "name": "nova"}, {"endpoints": [{"id": "880a2d67fb514cd7971bc8b86560bce0", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:9292", "region": "RegionOne"}, {"id": "e6cffed9f2ae46be977c388c4a0f2a9d", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:9292", "region": "RegionOne"}, {"id": "f718732cde204cabbe05a91fb7633426", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:9292", "region": "RegionOne"}], "id": "93de37d2c5c1415ab19e7e8a833ddc3e", "type": "image", "name": "glance"}, {"endpoints": [{"id": "0684789652f841b690f2079e15fac738", "interface": "internal", "region_id": "RegionOne", "url": "http://gz-controller1:8776/v3/546fb5e605354a52bc5fcdec78a0db9b", "region": "RegionOne"}, {"id": "12344e19845342dc91155bcf1905131c", "interface": "public", "region_id": "RegionOne", "url": "http://gz-controller1:8776/v3/546fb5e605354a52bc5fcdec78a0db9b", "region": "RegionOne"}, {"id": "245a5afcf8ae40e29a831c76bb960285", "interface": "admin", "region_id": "RegionOne", "url": "http://gz-controller1:8776/v3/546fb5e605354a52bc5fcdec78a0db9b", "region": "RegionOne"}], "id": "bffe1998e23347e3869fe9e10f8f7d71", "type": "volumev3", "name": "cinderv3"}]}}
```



### 撤销令牌

要撤销令牌直接可以直接使用openstack的子命令，用法是：

```ABAP
 openstack token revoke <token-id>
```

这个命令只能撤销已存在的令牌，且必须知道令牌ID，且执行成功后没有任何返回信息。当然也可以 通过curl直接构建删除token的请求，示例用法如下：

```bat
curl -i -X DELETE \
-H "X-Auth-Token: $OS_TOKEN" \
-H "X-Subject-Token: $OS_TOKEN" \
"http://localhost:5000/v3/auth/tokens"
```

实际使用时，把里面的OS_TOKEN变量替换为实际的token id即可。 示例返回请求如下所示：

```bat
HTTP/1.1 204 NO CONTENT
2 Date: Wed, 22 Nov 2023 14:59:46 GMT
3 Server: Apache/2.4.6 (CentOS) mod_wsgi/3.4 Python/2.7.5
4 Vary: X-Auth-Token
5 x-openstack-request-id: req-89d4a065-dad5-463c-b2bf-2d6aedd921df
6 Content-Type: text/plain; charset=UTF-8
```

撤销后验证

下面是一个使用curl请求访问keystone 群组信息的API请求，

```bat
OS_TOKEN=gAAAAABmHIjK2hlPy0oJzsfaEGfrbGQpsart9I3DojLrqoOHyrWl2xLKshbyM6mHSIYZnWq
kuQJwoCIZvflk0KHp297zyaXKqNvMKRxvNyAY8eC0e2Jlu8uTRb46JG2O41fw7bSKRiwHZenOTpIPseiuFSOSl9shcKwGVoIrArsbJb4kcBBpQDkAFltwU00Uvll
gaesddEt
curl -i \
-H "Content-Type: application/json" \
-H "X-Auth-Token: $OS_TOKEN" \
"http://gz-controller:5000/v3/groups" ; echo
```

在token是有效的请求下，返回结果如下：

```bat
{"groups": [], "links": {"next": null, "self": "http://gzcontroller:5000/v3/groups", "previous": null}}
```

在令牌撤销以后，相同的脚本执行结果如下：

```bat
{"error":{"code":401,"message":"The request you have made requires authentication.","title":"Unauthorized"}}
```

说明令牌已经被撤销失效。



## Keystone 实战

### 实战内容1：Keystone对接LDAP

在实际公司内部部署OpenStack的时候，我们一般会把keystone组件和公司的LDAP对接，实现统一的 权限认证和管理。根据下面的步骤来配置一个keystone和LDAP服务器的对接示例。



#### 测试 LDAP 服务器搭建

##### 前提条件

准备好一台安装好docker的linux服务器，如果资源有限，也可以在当前已有的机器上部署，后面需要注意避免端口冲突。我这里准备的机器ip地址是`192.168.100.210`，主机名是ldap.mystical.org

在 Rocky 9 中准备 Docker 环境

```bash
# 删除 podman-docker（建议）
[root@ldap /etc/yum.repos.d]# dnf remove -y podman-docker

# 安装基础工具
[root@ldap /etc/yum.repos.d]# dnf install -y yum-utils device-mapper-persistent-data lvm2

# 添加阿里云 Docker Repo
[root@ldap /etc/yum.repos.d]# yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
添加仓库自：https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 安装Docker CE
[root@ldap /etc/yum.repos.d]# yum makecache && dnf install -y docker-ce docker-ce-cli containerd.io

# 启动 Docker
[root@ldap /etc/yum.repos.d]# systemctl enable --now docker
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /usr/lib/systemd/system/docker.service.

# 验证
[root@ldap /etc/yum.repos.d]# systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: disabled)
    Drop-In: /etc/systemd/system/docker.service.d
             └─http-proxy.conf
     Active: active (running) since Mon 2026-05-11 15:00:30 CST; 18s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 6866 (dockerd)
      Tasks: 8
     Memory: 29.3M
        CPU: 219ms
     CGroup: /system.slice/docker.service
             └─6866 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.s>
5月 11 15:00:29 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:29.835252102+08>
5月 11 15:00:29 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:29.839941491+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.106675947+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.116124991+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.116210291+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.119178151+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.119965464+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.128860351+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.128948954+08>
5月 11 15:00:30 ldap.mystical.org systemd[1]: Started Docker Application Container Engi>

# 下载代理脚本
[root@ldap ~]# wget https://www.mysticalrecluse.com/script/Shell/set_docker_proxy.sh

# 启动脚本
# 记得根据自己的实际情况，修改脚本
[root@ldap ~]# bash set_docker_proxy.sh start
Docker 服务代理配置完成!                                   [  OK  ]

# 取消环境变量
[root@ldap ~]# env|grep DOCKER
DOCKER_HOST=unix:///run/podman/podman.sock
[root@ldap ~]# unset DOCKER_HOST
```



##### 配置LDAP服务端

如果你自己的环境中有现成的LDAP服务器配置，那么可以跳过这个步骤。

因为这里只是为了测试目的，我们这里直接使用docker来搭建一个测试使用的LDAP服务器，执行下面的命令拉取LDAP服务器所需的镜像：

```bash
[root@ldap ~]# docker pull osixia/openldap
[root@ldap ~]# docker pull osixia/phpldapadmin
```

先部署LDAP服务，启动容器的命令是：

```bash
[root@ldap ~]# docker run -d \
-p 389:389 \
-p 636:636 \
-v /usr/local/ldap:/usr/local/ldap \
-v /opt/ldap:/var/lib/ldap \
-v /opt/slapd.d:/etc/ldap/slapd.d \
-e LDAP_ORGANISATION="mystical" \
-e LDAP_DOMAIN="mystical.org" \
-e LDAP_ADMIN_PASSWORD="123456" \
--name openldap \
--hostname ldap.mystical.com \
osixia/openldap
```

面配置中，你自己实验时，需要把里面的主机名、域名、组织名称都换成你自己对应的配置参数。



##### PHPLdapAdmin Web管理工具配置

phpldapadmin是一个提供ldap Web管理页面的工具，现在也可以直接通过容器来部署，之前镜像已经拉取到本地，直接使用下面的命令来启动即可：

```bash
[root@ldap ~]# docker run -p 80:80 --privileged -d \
--name ldapweb --env PHPLDAPADMIN_HTTPS=false \
--env PHPLDAPADMIN_LDAP_HOSTS=192.168.100.210 \
osixia/phpldapadmin
```

启动成功后，直接访问这台机器的80端口即可，对应页面如下所示：

![image-20260511151919822](D:\git_repository\cyber_security_learning\markdown_img\image-20260511151919822.png)

点击页面左侧login登录，默认的登录账号是 `cn=admin,dc=mystical,dc=org`，默认密码就是启动ldap 服务端时在环境变量里指定的密码 `123456`。登录后完成LDAP组织配置，我们需要在myhuihui.com这个域下添 加两个OU，分别是groups和users，添加完成后如下所示：

![image-20260511152901152](D:\git_repository\cyber_security_learning\markdown_img\image-20260511152901152.png)



### 实战内容2： keystone多地域配置





### 实战内容3：Keystone MFA多因子认证

















# OpenStack 资源大脑 Placement

Placement是OpenStack中用来进行资源管理的组件，是N版本开始从Nova组件中剥离出来的项目。之 前在Nova中是用来寻找符合条件的主机，独立出来以后，它的目标变成了寻找合适资源。例如Nova用 来开启虚拟机的主机资源，Neutron用来创建虚拟网络的资源等等。 现在它的API是用来追踪资源供应商（Resource Provider，例如计算节点、存储池等）的清单 （Inventory）和使用率（Usage），以及不同的资源类别。例如可以查看计算节点上的CPU和内存使 用情况，外部存储池的使用情况等。



## Placement体系结构

### Placement里的核心概念

#### 资源提供商（Resource Provider）

提供云计算所需资源的各种设备或者部件，例如计算节点，可以提供Nova 开启虚拟机所需的CPU、内存、硬盘等资源；显卡可以提供GPU运算资源等。



#### 资源类（Resource Class）

表示资源的类型，例如CPU、内存、GPU、磁盘等等；



#### 资源提供商聚合（Resource Provider Aggregate）

把众多具有相同特性或者相同用途的资源提供商分组，例如 一组具备高带宽网卡的机器分为一类、一组安装了高性能显卡的主机分为一类等等；



#### 资源特征（Resource Trait）

用来描述和区分资源提供商的特性



#### 资源提供商清单（Resource Provider Inventory）

指的是资源提供商的总资源清单，详细列出每种资源的总 量，例如分配时的最大、最小单位等分配粒度信息。



#### 资源使用率（Resource Usage）

清单用于记录设备的总资源清单和分配特性，而使用率则记录目前的资源消耗 情况，让用户可以了解每个资源提供商上还可以使用的资源数量。



#### 资源分配（Resource Allocation）

指的是期望从某个Resource Provider上获得的资源类型和数量每个资源分配 都是相对于单个资源提供商而言的，每个资源分配请求的资源数量时资源提供商所拥有资源的子集。



## Placment 资源管理

Placement服务因为从N版本才开始分离出来，因此最开始默认只提供了api接口供其他服务进行资源的查询，没有提供对应的CLI命令，因此社区为了方便用户查询placement管理的资源信息，为它开发了 一个命令行工具osc-placement，这个命令行工具没有自己的命令，它更像是一个插件，给openstack 添加了子命令resource、allocation等。我们先安装配置好这个命令，然后再来研究它的使用方式。



### CLI命令安装

osc-placement这个命令插件在Rockylinux9上可以直接通过dnf命令来安装，命令是：

```ABAP
dnf install python3-osc-placement
```

安装的版本是4.2.0，安装完成后openstack就多了resource、aggregate、f这样几个子命令。但是这 个版本的命令默认使用的是Placement 1.0版本的API接口，而实际使用时需要最低1.20版本的接口，因 此在使用之前，我们还需要在admin-rc文件中添加下面一行：

```ABAP
export OS_PLACEMENT_API_VERSION=1.20
```

然后重新执行source admin-rc.sh让环境变量生效，下面我们就可以通过这几个子命令来查看整个集群 内的资源基本情况。



### Placement资源分类

资源分类指的是Placement里把资源节点能够提供的资源分成了对应的类别，例如计算节点一般可以提 供CPU、内存，安装了计算显卡的节点可以提供GPU资源等，管理资源分类对应的子命令是：

```ABAP
openstack resource class [list|show|create|delete|set]
```

各个子命令的作用分别是：

- list，列出现有的所有资源类
- show，显示某个资源类的详细信息；
- create，创建一个自定义的资源类别；
- delete，删除某个资源类别；
- set，创建或者校验已有的单个资源类，和create命令不一样的是，create命令在资源类存在时会失败。而set命令 不会。同时这个命令要求placement 的API版本大于1.7，即我们当前的1.10版本可以正常使用。



示例输出如下：

```bash
[root@gz-controller1 ~]# openstack resource class list
+----------------------------------------+
| name                                   |
+----------------------------------------+
| VCPU                                   |
| MEMORY_MB                              |
| DISK_GB                                |
| PCI_DEVICE                             |
| SRIOV_NET_VF                           |
| NUMA_SOCKET                            |
| NUMA_CORE                              |
| NUMA_THREAD                            |
| NUMA_MEMORY_MB                         |
| IPV4_ADDRESS                           |
| VGPU                                   |
| VGPU_DISPLAY_HEAD                      |
| NET_BW_EGR_KILOBIT_PER_SEC             |
| NET_BW_IGR_KILOBIT_PER_SEC             |
| PCPU                                   |
| MEM_ENCRYPTION_CONTEXT                 |
| FPGA                                   |
| PGPU                                   |
| NET_PACKET_RATE_KILOPACKET_PER_SEC     |
| NET_PACKET_RATE_EGR_KILOPACKET_PER_SEC |
| NET_PACKET_RATE_IGR_KILOPACKET_PER_SEC |
+----------------------------------------+
```



### Placement资源供应商

资源供应商指的就是提供资源的节点，对应的管理子命令是：

```ABAP
openstack resource provider [list|create|delete|set|show]
```

管理子命令的用法和资源类的用法一样。

示例输出如下：

```bash
[root@gz-controller1 ~]# openstack resource provider list
+--------------------------------------+---------------------------+------------+--------------------------------------+----------------------+
| uuid                                 | name                      | generation | root_provider_uuid                   | parent_provider_uuid |
+--------------------------------------+---------------------------+------------+--------------------------------------+----------------------+
| 4f05bb1e-5a64-45f6-85b0-ce96c45b57b6 | gz-computer1.mystical.org |         20 | 4f05bb1e-5a64-45f6-85b0-ce96c45b57b6 | None                 |
+--------------------------------------+---------------------------+------------+--------------------------------------+----------------------+
```

除了对资源供应商本身的管理外，基于资源供应商，还有另外几个下级概念，分别是：





# OpenStack 镜像服务 Glance

Glance是为OpenStack提供虚拟机镜像管理的组件，在搭建起来的 OpenStack 集群中，我们在创建虚拟机的时候需要指定使用的镜像，例如CentOS还是Ubuntu。然后在虚拟机创建的过程中，Nova就会向 Glance 服务申请镜像。Glance服务自己负责管理镜像的存储，会告诉虚拟机在哪里可以获取镜像， 然后Nova服务就到指定地址去读取镜像并启动虚拟机。



## Glance体系结构

Glance 只负责镜像管理工作，镜像存储工作由后端的存储组件负责，Glance只负责对接后端的存储。 因此Glance可以认为是OpenStack几大核心组件中最简单的组件。Glance的体系结构如下所示：

![image-20260527162542699](D:\git_repository\cyber_security_learning\markdown_img\image-20260527162542699.png)

从图上可以看到整个架构比较简单，glance-api负责接收镜像相关的请求，然后调用glance-registry服 务进行镜像相关的CRUD操作，glance-api还可以直接调用后端存储进行镜像的读写操作。但这里的图片中大家可以看到，glance-api到glance-registry，然后到db这里用的是虚线，这里的原因是从S版本开始，glance-registry 组件被废弃了，它的功能直接集成到了glance-api组件里。因此在S之前的版本中，我们还可以看到 glance-registry 这个组件，之后的版本中就没有了，例如我们在前面使用rpm包 署Train版本时，就没有启动这个组件，但是我们的虚拟机创建过程中还是可以正常获取到镜像信息。 Glance组件里的store模块实现了一个存储框架，可以对接多种后端存储，例如S3、Swift、Ceph、本 地文件系统等，然后向glance-api提供一个统一镜像读写接口。



## Glance存储配置

根据上面的架构图我们知道，glance组件只有两块配置，分别是：

- 数据库配置，一般是设置数据库的连接信息，包括地址、端口、账号密码等；

- 存储配置，根据存储类型会有不同的配置信息，下面会详细介绍。

```bash
# 分发 keyring 到 /etc/ceph
[root@gz-controller1 ~]# mkdir /etc/ceph
mkdir: 无法创建目录 “/etc/ceph”: 文件已存在
[root@gz-controller1 ~]# cp ceph.conf ceph.client.glance.keyring /etc/ceph/
[root@gz-controller1 ~]# ls /etc/ceph/
ceph.client.glance.keyring  ceph.conf

# ceph 集群查看 pool
[root@rl-ceph1 ~]# ceph osd lspools
1 .mgr
2 volumes
3 images                           # 提前创建好了存放image的pool
4 backups
5 vms
6 rbd
7 .rgw.root
8 default.rgw.log
9 default.rgw.control
10 default.rgw.meta
11 default.rgw.buckets.index
12 default.rgw.buckets.data

# 修改 glance API
[root@gz-controller1 ~]# vim /etc/glance/glance-api.conf 
[DEFAULT]
enabled_backends = ceph_rbd:rbd
log_dir = /var/log/glance

[glance_store]
default_backend = ceph_rbd

[ceph_rbd]
rbd_store_user = glance
rbd_store_pool = images

[oslo_reports]
log_dir = /var/log/glance    # 方便后期调试

# 删除之前的镜像
[root@gz-controller1 ~]# openstack image list
+--------------------------------------+-----------------------+--------+
| ID                                   | Name                  | Status |
+--------------------------------------+-----------------------+--------+
| cccc88b8-ff50-4bb2-a30c-d60cb261233d | cirros                | active |
| 6e6efb5b-eb7d-4c20-9da2-a53760300274 | ubuntu-22.04-testuser | active |
| 242d37eb-c2c6-4070-a1a6-6febec2bd511 | ubuntu-22.04-update   | active |
| 9703d1ce-3bf3-4444-8dc7-67717ab4b539 | ubuntu-22.04-v2       | active |
+--------------------------------------+-----------------------+--------+
[root@gz-controller1 ~]# openstack image delete 9703d1ce-3bf3-4444-8dc7-67717ab4b539
[root@gz-controller1 ~]# openstack image delete 242d37eb-c2c6-4070-a1a6-6febec2bd511
[root@gz-controller1 ~]# openstack image delete 6e6efb5b-eb7d-4c20-9da2-a53760300274
[root@gz-controller1 ~]# openstack image delete cccc88b8-ff50-4bb2-a30c-d60cb261233d

# 安装 python 的 rbd/rados 绑定库
[root@gz-controller1 ~]# dnf config-manager --set-enabled crb
[root@gz-controller1 ~]# dnf install -y epel-release
[root@gz-controller1 ~]# dnf clean all
[root@gz-controller1 ~]# dnf makecache
[root@gz-controller1 ~]# dnf install -y python3-rados python3-rbd --nobest

# 或者安装ceph-common 也可以
[root@gz-controller1 ~]# dnf install -y ceph-common

# 重启镜像
[root@gz-controller1 ~]# systemctl restart openstack-glance-api.service

# 查看日志，没有任何报错
[root@gz-controller1 ~]# tail -f /var/log/glance/glance-api.log 
2026-05-27 17:19:01.999 150307 INFO glance.async_ [-] Threadpool model set to 'EventletThreadPoolModel'
2026-05-27 17:19:05.317 150307 INFO glance.common.wsgi [-] Starting 4 workers
2026-05-27 17:19:05.328 150307 INFO glance.common.wsgi [-] Started child 150346
2026-05-27 17:19:05.337 150346 INFO eventlet.wsgi.server [-] (150346) wsgi starting up on http://10.2.100.200:9292
2026-05-27 17:19:05.344 150307 INFO glance.common.wsgi [-] Started child 150347
2026-05-27 17:19:05.351 150347 INFO eventlet.wsgi.server [-] (150347) wsgi starting up on http://10.2.100.200:9292
2026-05-27 17:19:05.355 150307 INFO glance.common.wsgi [-] Started child 150348
2026-05-27 17:19:05.362 150348 INFO eventlet.wsgi.server [-] (150348) wsgi starting up on http://10.2.100.200:9292
2026-05-27 17:19:05.369 150307 INFO glance.common.wsgi [-] Started child 150349
2026-05-27 17:19:05.383 150349 INFO eventlet.wsgi.server [-] (150349) wsgi starting up on http://10.2.100.200:9292

# 上传镜像测试
[root@gz-controller1 ~]# openstack image create "ubuntu-22.04-testuser" \
  --file /root/jammy-server-cloudimg-amd64.img \
  --disk-format qcow2 \
  --container-format bare \
  --public

[root@gz-controller1 ~]# openstack image create "cirror-0.6.2"   --file /root/cirros-0.6.2-x86_64-disk.img  --disk-format qcow2   --container-format bare   --public

# 去 ceph 上查看
[root@rl-ceph1 ~]# rbd ls -p images
1bd67a7d-c848-4bb6-8704-56109be6f8f1
82b11e39-5b11-4483-98c8-1651f1a9898d
```



## Glance 镜像管理命令

```bash
openstack image create               # 创建一个新镜像
openstack image list                 # 列出当前用户可以查看的所有镜像
openstack image delete               # 删除一个镜像，后面跟镜像id
openstack image show                 # 显式一个镜像的详情信息
openstack image save                 # 把 Glance 中的镜像导出并保存到本地
openstack image set/unset            # 给镜像设置属性或取消属性
openstack image add project          # 把项目和镜像关联起来
openstack image member list          # 显示这个镜像关联的项目数量
openstack image remove project       # 从镜像上移除某个项目的关联
```



## 镜像文件制作工具 Diskimage-builder

Diskimage-builder 是 OpenStack 生态里的：

```ABAP
“云镜像自动化构建引擎”
```

核心用途：

- 自动生成 qcow2/raw 镜像
- 构建 OpenStack Cloud Image
- 自动化生成 Kubernetes/OpenStack/Ceph 节点镜像
- CI/CD 镜像流水线
- 裸金属/Ironic deploy image



### DIB 安装

```bash
# Rocky / CentOS
[root@gz-controller1 ~]# dnf install -y python3-pip qemu-img qemu-kvm gi
[root@gz-controller1 ~]# pip3 install diskimage-builder

# 验证
[root@gz-controller1 ~]# disk-image-create --version
3.42.0

# Ubuntu
apt update
apt install -y python3-pip qemu-utils debootstrap git
pip3 install diskimage-builder
```



### 基本命令格式

```ABAP
disk-image-create [elements...] -o 镜像名
```

示例：
```bash
# 创建一个Ubuntu镜像
[root@gz-controller1 ~]# disk-image-create ubuntu vm cloud-init -o ubuntu2204

# 查看
[root@gz-controller1 ~]# ll -h ubuntu2204.qcow2 
-rw-r--r-- 1 root root 1.3G  5月 27 20:32 ubuntu2204.qcow2
```







# OpenStack 存储服务 Cinder

Cinder是 OpenStack 中为虚拟机提供虚拟硬盘服务的组件，在早期也是Nova中的一个组件，但是从F版本开始被剥离出来作为单独的项目存在。在OpenStack里面，Nova 组件和 Cinder 组件都可以创建存储卷，在之前搭建虚拟机的时候中我们也实际操作过，Nova 组件和 Cinder 组件都使用本地的LVM存储卷来提供存储服务。

Nova组件通常是创建虚拟机的系统盘，单个系统盘容量一般比较小，通常在50-100G左右，整个大小是在创建实例规格的时候定义的。而实际提供数据存储的盘则由Cinder服务提供，一般会把Cinder对 接多种后端，来提供不同性能水平的数据盘，通常是IOPS的大小差异，并发写入的带宽差异等。例如 下面的公有云磁盘性能差异：

![image-20260527203440263](D:\git_repository\cyber_security_learning\markdown_img\image-20260527203440263.png)

Cinder服务可以实现存储卷的创建、挂载、卸载、快照（snapshot）全生命周期管理。



## Cinder体系结构

Cinder的各个组件之间的体系架构如下图所示：

![image-20260527203535773](D:\git_repository\cyber_security_learning\markdown_img\image-20260527203535773.png)

控制节点：

- Cinder-API
- Cinder-Scheduler
- Cinder-backup

计算节点：

- Cinder-volume



从上面图里可以看到，cinder-api 负责接收用户请求，例如创建存储卷、获取存储卷信息、删除存储卷、创建快照等。然后调用后端不同的组件来完成用户请求，例如调用 Cinder-scheduler 来处理存储卷的创建、删除、扩缩容等操作。调用 cinder-backup 组件完成存储卷备份的管理工作，例如创建备份、 备份恢复、备份删除这些基本操作，cinder-backup 组件后端也是需要对接外部存储。

cinder-volume 组件是用来管理本地硬盘资源或者网络存储资源到宿主机的映射，一般是安装在提供物理硬盘存储的计算节点或者专门的存储节点上。

cinde r默认使用 lvm 作为后端存储，这样就可以直接使用存储节点上的物理磁盘，就像我们在之前第一章的计算节点上创建的lvm，先在物理磁盘上创建pv，然后创建vg，cinder在接收到存储盘创建请求的时候，到vg上去划分对应大小的空间创建lv，并在lv上创建虚拟机数据盘所需的文件系统， 例如ext4， xfs等，创建好后挂载到虚拟机上使用。

如果使用的是网络存储，例如Ceph，它会通过Ceph集群的配置信息和认证文件，到Ceph集群上对应存储池中（通常是volumes）创建一个rbd文件，然后将这个rbd文件挂载为虚拟机所在宿主机上的物理磁盘，最后再把这个物理磁盘挂载到虚拟机里使用。

这两种存储各有各的优势，例如 lvm 存储可以直接利用物理磁盘，因此性能更加优异，对于一些需要高性能的需求来说，使用这种类型的存储比较合适。但是磁盘是固定在物理服务器上，当物理服务器宕机时，数据也不能即时取出。

使用Ceph存储，当物理服务器宕机的时候，我们只需要把rbd文件挂载到新的宿主机上，并在这个新的宿主机直接启动虚拟机，数据就回来了。 因此灵活性更好，但是相对lvm存储来说，性能就比不上了。 对于云服务来说，数据安全性和灵活性一般比性能更重要，这也是为什么网络存储在云服务中使用这 么广泛的原因



## Cinder的调度策略

当使用lvm存储，cinder-scheduler 这个组件就会根据实际的请求去选择合适的存储节点，它会经过过滤和权重两个流程选择出最合适的存储节点。基本流程像下面示例图演示的那样，对这个流程只需要了解即可，因为实际私有云部署中，使用lvm存储的情况比较少见，大部分还是以云存储居多。



### 过滤器和权重器

cinder 选择合适的存储节点是通过过滤器（Filters）和权重器（weigher）两层工具来实现。 首先使用过滤器从所有后端存储节点中选择出符合条件的多个节点，然后通过权重计算，依次计算出 每个节点的权重值，最后选择权重最高的那个节点来创建存储卷。

在Cinder的配置文件中，默认的过滤器配置是：

```ABAP
scheduler_default_filters = AvailabilityZoneFilter,CapacityFilter,CapabilitiesFilter
```

即默认有3个过滤器，分别是

- 可用区过滤器，通过可用区来过滤；
- 容量过滤器，通过存储节点可用存储容量来过滤；
- 兼容性过滤器，存储类型是是否满足实例或存储卷的要求来过滤；

同样在配置文件中，默认的权重器配置是：

```ABAP
scheduler_default_weighers = CapacityWeigher
```

这个配置计算权重，是根据存储节点上剩余的磁盘空间容量来计算的，剩余的磁盘空间容量越大，权重值越高。

实际上 Cinder 的配置中还可以使用其他的过滤器和权重器，但是就像上面说的那样，现在的 OpenStack集群在生产上部署时，以网络存储为主，基本上不使用本地存储，因此这两者我们不需要过多的去了解，当真正要用到的时候再去查看官方文档即可。



### cinder-volume

在上面基本流程中说到，cinder-volume是存储节点上实际负责调度的组件，它会对接后端的存储硬盘，并根据请求里的参数创建出对应大小的数据卷，并将这个数据卷映射到虚拟机上，给虚拟机使用。实际配置如下：





### 多存储卷配置

如果后端可以提供多种类型的存储卷，例如普通性能的SSD和高性能的SSD，像上面图中看到的，我 们在公有云上购买虚拟机的时候，都会有这样的选项，而在OpenStack上我们自己配置的时候，也可以实现。

```bash
# ceph 上的演示
[root@rl-ceph1 ~]# ceph osd tree
ID  CLASS  WEIGHT   TYPE NAME          STATUS  REWEIGHT  PRI-AFF
-1         0.87918  root default                                
-3         0.29306      host rl-ceph1                           
 2         0.09769          osd.2          up   1.00000  1.00000
 0    ssd  0.09769          osd.0          up   1.00000  1.00000
 1    ssd  0.09769          osd.1          up   1.00000  1.00000
-5         0.29306      host rl-ceph2                           
 3    ssd  0.09769          osd.3          up   1.00000  1.00000
 4    ssd  0.09769          osd.4          up   1.00000  1.00000
 5    ssd  0.09769          osd.5          up   1.00000  1.00000
-7         0.29306      host rl-ceph3                           
 6    ssd  0.09769          osd.6          up   1.00000  1.00000
 7    ssd  0.09769          osd.7          up   1.00000  1.00000
 8    ssd  0.09769          osd.8          up   1.00000  1.00000
 
 # 修改class
[root@rl-ceph1 ~]# ceph osd crush rm-device-class osd.2
done removing class of osd(s): 2
[root@rl-ceph1 ~]# ceph osd crush rm-device-class osd.5
done removing class of osd(s): 5
[root@rl-ceph1 ~]# ceph osd crush rm-device-class osd.8
done removing class of osd(s): 8

# 查看
[root@rl-ceph1 ~]# ceph osd tree
ID  CLASS  WEIGHT   TYPE NAME          STATUS  REWEIGHT  PRI-AFF
-1         0.87918  root default                                
-3         0.29306      host rl-ceph1                           
 2         0.09769          osd.2          up   1.00000  1.00000
 0    ssd  0.09769          osd.0          up   1.00000  1.00000
 1    ssd  0.09769          osd.1          up   1.00000  1.00000
-5         0.29306      host rl-ceph2                           
 5         0.09769          osd.5          up   1.00000  1.00000
 3    ssd  0.09769          osd.3          up   1.00000  1.00000
 4    ssd  0.09769          osd.4          up   1.00000  1.00000
-7         0.29306      host rl-ceph3                           
 8         0.09769          osd.8          up   1.00000  1.00000
 6    ssd  0.09769          osd.6          up   1.00000  1.00000
 7    ssd  0.09769          osd.7          up   1.00000  1.00000
 
 # 添加新标记
[root@rl-ceph1 ~]# ceph osd crush set-device-class hdd osd.2
set osd(s) 2 to class 'hdd'
[root@rl-ceph1 ~]# ceph osd crush set-device-class hdd osd.5
set osd(s) 5 to class 'hdd'
[root@rl-ceph1 ~]# ceph osd crush set-device-class hdd osd.8
set osd(s) 8 to class 'hdd'

# 查看
[root@rl-ceph1 ~]# ceph osd tree
ID  CLASS  WEIGHT   TYPE NAME          STATUS  REWEIGHT  PRI-AFF
-1         0.87918  root default                                
-3         0.29306      host rl-ceph1                           
 2    hdd  0.09769          osd.2          up   1.00000  1.00000
 0    ssd  0.09769          osd.0          up   1.00000  1.00000
 1    ssd  0.09769          osd.1          up   1.00000  1.00000
-5         0.29306      host rl-ceph2                           
 5    hdd  0.09769          osd.5          up   1.00000  1.00000
 3    ssd  0.09769          osd.3          up   1.00000  1.00000
 4    ssd  0.09769          osd.4          up   1.00000  1.00000
-7         0.29306      host rl-ceph3                           
 8    hdd  0.09769          osd.8          up   1.00000  1.00000
 6    ssd  0.09769          osd.6          up   1.00000  1.00000
 7    ssd  0.09769          osd.7          up   1.00000  1.00000
 
 # 基于新标记创建规则
[root@rl-ceph1 ~]# ceph osd crush rule create-replicated replicated_ssd default host ssd
[root@rl-ceph1 ~]# ceph osd crush rule create-replicated replicated_hdd default host hdd
 
# 查看
[root@rl-ceph1 ~]# ceph osd crush rule ls
replicated_rule
replicated_ssd
replicated_hdd

# 创建使用指定规则的存储池
[root@rl-ceph1 ~]# ceph osd pool create ssd-pool 64 64 replicated replicated_ssd
pool 'ssd-pool' created
[root@rl-ceph1 ~]# ceph osd pool create hdd-pool 64 64 replicated replicated_hdd
pool 'hdd-pool' created

# 将其初始化为rbd
[root@rl-ceph1 ~]# rbd pool init ssd-pool
[root@rl-ceph1 ~]# rbd pool init hdd-pool

# 赋予 client_cinder 新创建的存储池的权限
[root@rl-ceph1 ~]# ceph auth caps client.cinder \
mon 'profile rbd' \
osd 'profile rbd pool=hdd-pool, profile rbd pool=ssd-pool' \
mgr 'profile rbd pool=hdd-pool, profile rbd pool=ssd-pool'
updated caps for client.cinder
```



#### 准备工作

先在存储节点上安装好ceph-common工具，因为nova需要利用这个工具里提供的命令来挂载ceph 存 储到虚拟机上，安装命令是：

```bash
[root@gz-computer1 ~]# dnf install -y ceph-common 

# 注意如果出现问题，可以下面的操作解决依赖问题
[root@gz-computer1 ~]# dnf config-manager --set-enabled crb
[root@gz-computer1 ~]# dnf install -y epel-release
[root@gz-computer1 ~]# dnf clean all
[root@gz-computer1 ~]# dnf makecache
[root@gz-computer1 ~]# dnf install -y ceph-common 
```

然后在Ceph节点上获取cinder用户keyring文件的一个临时副本：

```bash
[root@rl-ceph1 ~]# ceph auth get-key client.cinder|ssh 10.2.100.200 tee client.cinder.key
AQDAFhVqP0SXHRAA67sChuGqAmVEYuhVWj7Lyg==
[root@rl-ceph1 ~]# ceph auth get-key client.cinder|ssh 10.2.100.201 tee client.cinder.key
AQDAFhVqP0SXHRAA67sChuGqAmVEYuhVWj7Lyg==

# 到openstack节点查看
[root@gz-controller1 ~]# ls client.cinder.key 
client.cinder.key
[root@gz-controller1 ~]# cat client.cinder.key 
AQDAFhVqP0SXHRAA67sChuGqAmVEYuhVWj7Lyg==
[root@gz-computer1 ~]# ls client.cinder.key
client.cinder.key
[root@gz-computer1 ~]# cat client.cinder.key
AQDAFhVqP0SXHRAA67sChuGqAmVEYuhVWj7Lyg==
```

这个命令会把这个副本密钥文件client.cinder.key发送到计算节点上。



#### secret 创建

在获取到 cinder 用户的 keyring 文件副本后，我们要使用它在计算节点上创建一个虚拟机使用的secret， 虚拟机需要通过它和 Ceph 集群进行认证。

首先使用uuidgen生成一个uuid，生成的uuid如下所示：

```bash
# 在计算节点创建uuid
[root@gz-computer1 ~]# uuidgen 
3dbee1a1-a44b-4d39-94ce-b9cea6e31f3c

# 在计算节点上创建一个secret.yml文件
[root@gz-computer1 ~]# cat secret.xml 
<secret ephemeral='no' private='no'>
  <uuid>3dbee1a1-a44b-4d39-94ce-b9cea6e31f3c</uuid>
  <usage type='ceph'>
    <name>client.cinder secret</name>
  </usage>
</secret>

# 指明这个secret的用途是Ceph，名称里标明这个Secret所属用户，然后执行下面的命令定义一个 secret：
[root@gz-computer1 ~]# virsh secret-define --file secret.xml
生成 secret 3dbee1a1-a44b-4d39-94ce-b9cea6e31f3c

# 然后我们将它的值设置为 cinder 用户 keyring 文件里key对应的值：
# 这步把 Cephx key 保存到 libvirt secret 里了
[root@gz-computer1 ~]# virsh secret-set-value --secret 3dbee1a1-a44b-4d39-94ce-b9cea6e31f3c --base64 $(cat client.cinder.key) && rm client.cinder.key secret.xml
错误： 将 secret 值作为命令行参数传递是不安全的！  # 警告，不算错误，可以无视
secret 值设定

rm：是否删除普通文件 'client.cinder.key'？y
rm：是否删除普通文件 'secret.xml'？y

# 验证查看
[root@gz-computer1 ~]# virsh secret-list
 UUID                                   用量
-------------------------------------------------------------------
 3dbee1a1-a44b-4d39-94ce-b9cea6e31f3c   ceph client.cinder secret
```

这里的操作实际上就是把uuid和认证文件的key绑定到一起。（实际测试过程中的uuid值可能不一样，替换为你自己的uuid值即可。）



#### 整个通信过程详解

**1. QEMU 启动**

```bash
# libvirt 生成：
<auth username='cinder'>
  <secret uuid='xxxx'/>
</auth>
```

**2. QEMU 向 libvirt 要 secret**

```ABAP
“把 UUID 对应的密码给我”
```

**3. libvirt 返回真正 key**

```ABAP
AQBxxxxxxxx==
```

**4. librbd 使用 key 登录 Ceph**

然后：

```ABAP
librbd
 ↓
MON认证
 ↓
拿到OSDMap
 ↓
访问OSD
```





#### 配置文件修改

假设后端的Ceph存储给我们提供了两种类型的存储池，

- 第一种是基于普通的HDD磁盘
- 第二种是基于纯SSD构建

存储团队那边给我们提供了存储池的名称分别是volumes和volumes-ssd，那么在Cinder的配置文件里

需要增加或者修改的配置就是

```bash
[root@gz-computer1 ~]# vim /etc/cinder/cinder.conf 
[DEFAULT]
# 这里 volumes-hdd 和 volumes-ssd 是与backend section 对应
enabled_backends = lvm,volumes-hdd,volumes-ssd

[keystone_authtoken]
service_token_roles = service
service_token_roles_required = true

[service_user]

send_service_user_token = True
project_domain_name = Default

project_name = service
user_domain_name = Default
username = cinder
password = bDtsOxVMlh9Nr7IL
auth_url = http://gz-controller1:5000
auth_type = password
auth_strategy = keystone

[volumes-hdd]   # 这个就是backend section
volume_driver = cinder.volume.drivers.rbd.RBDDriver
volume_backend_name = volumes-hdd  # 这里要与后面的指定后端的命令里的property对应
rbd_pool = hdd-pool
rbd_ceph_conf = /etc/ceph/ceph.conf
rados_connect_timeout = 5
rbd_keyring_conf = /etc/ceph/ceph.client.cinder.keyring
rbd_user = cinder
rbd_secret_uuid = 3dbee1a1-a44b-4d39-94ce-b9cea6e31f3c
report_discard_supported = True

[volumes-ssd]
volume_driver = cinder.volume.drivers.rbd.RBDDriver
volume_backend_name = volumes-ssd
rbd_pool = ssd-pool   # 指定存储池
rbd_ceph_conf = /etc/ceph/ceph.conf
rbd_keyring_conf = /etc/ceph/ceph.client.cinder.keyring
rados_connect_timeout = 5
rbd_user = cinder    # 这里省略了，完整是client.cinder，会自动补全。
rbd_secret_uuid = 3dbee1a1-a44b-4d39-94ce-b9cea6e31f3c
report_discard_supported = True
```

配置说明：

- keystone_authtoken和service_user部分的配置是新版本中，为了区分普通用户和服务组件用户新增的安全措施配置，如果缺少这两部分的配置，会导致后面创建卷或者挂载卷都会报错；
- 如果两个存储池使用的用户名不一样，那么就需要创建两个不同的secret。示例里一样，因此一个就够了
- 如果后端是两个不一样的Ceph集群，那么keyring文件名要避免冲突，需要使用 rbd_keyring_conf配置来分别指定不同的认证文件名称。

配置好以后重启后端存储服务

```bash
[root@gz-computer1 ~]# systemctl restart openstack-cinder-volume

# 重启完成后，就能看到对应的后端服务了：
[root@gz-controller1 ~]# openstack volume service list
+------------------+---------------------------------------+------+---------+-------+----------------------------+
| Binary           | Host                                  | Zone | Status  | State | Updated At                 |
+------------------+---------------------------------------+------+---------+-------+----------------------------+
| cinder-scheduler | gz-controller1.mystical.org           | nova | enabled | up    | 2026-05-27T15:37:44.000000 |
| cinder-volume    | gz-computer1.mystical.org@lvm         | nova | enabled | up    | 2026-05-27T15:37:26.000000 |
| cinder-volume    | gz-computer1.mystical.org@volumes-hdd | nova | enabled | up    | 2026-05-27T15:37:48.000000 |
| cinder-volume    | gz-computer1.mystical.org@volumes-ssd | nova | enabled | up    | 2026-05-27T15:37:48.000000 |
+------------------+---------------------------------------+------+---------+-------+----------------------------+
```



#### nova组件新增配置

通用的keystone_authtoken和service_user部分的配置也需要在nova组件中添加，示例如下：

```bash
[root@gz-computer1 ~]# vim /etc/nova/nova.conf 
[keystone_authtoken]
service_token_roles = service
service_token_roles_required = true

[service_user]

send_service_user_token = True
project_domain_name = Default

project_name = service
user_domain_name = Default
username = nova
password = ac5RpUjzywMqhuqZ
auth_url = http://gz-controller1:5000
auth_type = password
auth_strategy = keystone

# 配置完成后，重启nova服务
[root@gz-computer1 ~]# systemctl restart openstack-nova-compu
```



#### 卷类型创建

服务都正常后，我们需要手动创建一个卷类型，和后端的存储关联到一起，创建卷类型的命令是：

```bash
[root@gz-controller1 ~]# openstack volume type create --public  --description "ceph hdd rbd pool" ceph-hdd
+-------------+--------------------------------------+
| Field       | Value                                |
+-------------+--------------------------------------+
| description | ceph hdd rbd pool                    |
| id          | 61d8b042-188d-44b6-a22d-5581bbc58152 |
| is_public   | True                                 |
| name        | ceph-hdd                             |
+-------------+--------------------------------------+

[root@gz-controller1 ~]# openstack volume type set --property volume_backend_name="volumes-hdd" ceph-hdd

[root@gz-controller1 ~]# openstack volume type create --public  --description "ceph ssd 
rbd pool" ceph-ssd
+-------------+--------------------------------------+
| Field       | Value                                |
+-------------+--------------------------------------+
| description | ceph ssd rbd pool                    |
| id          | 687b494b-d88d-45eb-8d30-5b8a0aa5a465 |
| is_public   | True                                 |
| name        | ceph-ssd                             |
+-------------+--------------------------------------+

[root@gz-controller1 ~]# openstack volume type set --property volume_backend_name="volumes-ssd" ceph-ssd
```



## Cinder 备份还原组件配置

Cinder中目前提供了两种备份还原机制，分别是：

- 快照（snapshot）
- 备份（backup）



### 快照

快照记录的是块存储某个时间点的状态，创建的速度非常快。在之前 Ceph 集群 RBD 块存储相关操作中，我们有介绍过 RBD 块存储创建快照以及恢复快照的相关操作。实际上Cinder对接的多种存储后端都支持快照的创建和恢复，包括我们集群最开始部署时使用的LVM卷。

默认情况下使用时需要遵循下面的规则：

- 打快照时，卷需要是可用状态（available），实际上当前支持强制打快照，但存在数据不一致的风险；
- 快照创建后，它关联的卷不能直接删除，需要删除对应的快照后才能删除卷；
- 卷文件故障时，快照也无法正常使用；

快照不需要额外的配置，只要后端的存储设备支持快照功能，即可正常使用。



#### 快照的使用

在使用快照之前，我们需要有一个可用的数据卷，我这边创建的是test1虚拟机上的卷，如下所示：

```bash
[root@gz-controller1 ~]# openstack volume list
+--------------------------------------+----------+-----------+------+-------------------------------+
| ID                                   | Name     | Status    | Size | Attached to                   |
+--------------------------------------+----------+-----------+------+-------------------------------+
| b0d13acb-fda7-493f-8963-e98a27d582d4 |          | in-use    |   10 | Attached to test on /dev/vdb  |
| bddfe61c-7b74-43be-a1a8-bf71bc05119b | test-hdd | available |   10 |                               |
+--------------------------------------+----------+-----------+------+-------------------------------+
```



#### 创建快照

针对某个卷创建快照的常用命令格式是：

```ABAP
openstack volume snapshot create --volume volume_name \
    --force --description description \
    <snapshot-name>
  
# --volume volume_name，后面跟上要创建快照的卷id或者卷名称，通常使用卷id，避免名称冲突；
# --force，可以对已经挂载到实例上的卷创建快照；
# --description，快照描述信息；
# snapshot-name，快照名称
```

示例：

```bash
[root@gz-controller1 ~]# openstack volume snapshot create --volume b0d13acb-fda7-493f-8963-e98a27d582d4 --force --description test snapshot-test1
+-------------+--------------------------------------+
| Field       | Value                                |
+-------------+--------------------------------------+
| created_at  | 2026-05-28T01:14:17.622493           |
| description | test                                 |
| id          | 92d2fab3-729c-4f93-b764-d06e2c4a8968 |
| name        | snapshot-test1                       |
| properties  |                                      |
| size        | 10                                   |
| status      | creating                             |
| updated_at  | None                                 |
| volume_id   | b0d13acb-fda7-493f-8963-e98a27d582d4 |
+-------------+--------------------------------------+
```

在前端页面查看

![image-20260528091529799](D:\git_repository\cyber_security_learning\markdown_img\image-20260528091529799.png)



#### 恢复快照

使用快照恢复数据的流程是：

- 使用快照创建新卷；
- 挂载新卷；

现在我们模拟删除卷里的文件，并从快照里恢复。虚拟机上挂载好的卷如下所示：

```bash
# 删除原有卷上到文件
# 然后通过快照创建新卷
[root@gz-controller1 ~]# openstack volume create --snapshot snapshot-test1 snapshot-test1
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| attachments         | []                                   |
| availability_zone   | nova                                 |
| bootable            | false                                |
| consistencygroup_id | None                                 |
| created_at          | 2026-05-28T01:20:57.992044           |
| description         | None                                 |
| encrypted           | False                                |
| id                  | 59719aba-a68b-4cf2-b7f8-1f054cc389f6 |
| migration_status    | None                                 |
| multiattach         | False                                |
| name                | snapshot-test1                       |
| properties          |                                      |
| replication_status  | None                                 |
| size                | 10                                   |
| snapshot_id         | 92d2fab3-729c-4f93-b764-d06e2c4a8968 |
| source_volid        | None                                 |
| status              | creating                             |
| type                | ceph-ssd                             |
| updated_at          | None                                 |
| user_id             | 27cbb482ca6045ef87c6122545f8a0bd     |
+---------------------+--------------------------------------+
```

![image-20260528092259923](D:\git_repository\cyber_security_learning\markdown_img\image-20260528092259923.png)

然后像普通卷一样挂载到实例上，就可以看到它里面的数据了。但是挂载之前建议先把之前删除数据的卷卸载掉，否则会因为两个磁盘上的文件系统拥有相同的UUID导致挂载冲突，如下所示：

![image-20260528092420847](D:\git_repository\cyber_security_learning\markdown_img\image-20260528092420847.png)

可以看到两个设备拥有相同的UUID，挂载/dev/vdc时，会报错

```bash
mount /dev/vdc /mnt
[14246.600362] XFS (vdc): Filesystem has duplicate UUID eeea1b54-eb30-4400-b7a9-c38db105ef19 - can't mount
mount: wrong fs type, bad option, bad superblock on /dev/vdc, 
       missing codepage or helper program, or other error 
       In some cases useful info is found in syslog - try 
       dmesg | tail or so. 
```

可以通过修改它的UUID解决这个问题

```bash
# 为设备重新生成uuid
# ext4文件系统
# 如果出现问题可以强制 fsck
# e2fsck -f /dev/vdc，过程如果被问到fix? yes/no，直接 y
e2fsck -f /dev/vdc
tune2fs -U random /dev/sdb1
# xfs文件系统
xfs_admin -U generate /dev/vdc
```

![image-20260528093137456](D:\git_repository\cyber_security_learning\markdown_img\image-20260528093137456.png)



#### 删除快照

删除快照的命令格式是：

```ABAP
openstack volume snapshot delete [snapshot_id|snapshot_name]
```

例如我们要删除上面创建的快照vdb-snap1，则命令是:

```bash
[root@gz-controller1 ~]# openstack volume snapshot delete snapshot-test1
```

删除成功后没有任何返回信息。



### 备份

备份的着重点是完整备份卷文件的数据，因此它的创建实际比较长。在**备份之前，需要把卷卸载**，避免出现数据不一致的情况。备份完成后，即使对应的卷出现故障，也可以从备份中直接会恢复。 在之前搭建Cinder服务的时候，我们有提到过Cinder-backup组件的后端只能对接网络存储服务，不支持本地存储，目前支持的网络存储有：`Ceph`、`Swift`、`Glusterfs`、`GCS`，等等组件，因此在搭建好了Ceph存储以后，我们来尝试也把它对接到Ceph存储。



#### 备份配置

在计算节点上打开`/etc/cinder/cinder.conf`配置文件，添加下面的配置：

```bash
[root@gz-computer1 ~]# vim /etc/cinder/cinder.conf
[DEFAULT]
backup_ceph_conf=/etc/ceph/ceph.conf
backup_ceph_user=cinder-backup
backup_ceph_chunk_size=134217728
backup_ceph_pool=backups
backup_ceph_stripe_unit=0
backup_ceph_stripe_count=0
restore_discard_excess_bytes=true
backup_driver=cinder.backup.drivers.ceph.CephBackupDriver
```

对于部署cinder-backup服务的节点需要下面3个配置文件：

- /etc/ceph/ceph.conf
- /etc/cinder/ceph.client.cinder.keyring
- /etc/cinder/ceph.client.cinderbackup.keyring

```bash
# 查看
[root@gz-computer1 ~]# ls /etc/ceph/
ceph.client.admin.keyring         ceph.client.glance.keyring  rbdmap
ceph.client.cinder-backup.keyring  ceph.client.nova.keyring
ceph.client.cinder.keyring        ceph.conf
```

而且需要把两个keyring文件的用户和群组都改为cinder，避免权限问题。添加好以后，重启cinder组件 服务，命令是：

```bash
# 修改权限
[root@gz-computer1 ~]# chown cinder:cinder /etc/ceph/ceph.client.cinder*

# 重启服务
[root@gz-computer1 ~]# systemctl restart openstack-cinder-api openstack-cinder-scheduler openstack-cinder-backup

# 查看backup服务状态，正常状态如下
[root@gz-computer1 ~]# openstack volume service list
+------------------+---------------------------------------+------+---------+-------+----------------------------+
| Binary           | Host                                  | Zone | Status  | State | Updated At                 |
+------------------+---------------------------------------+------+---------+-------+----------------------------+
| cinder-scheduler | gz-controller1.mystical.org           | nova | enabled | up    | 2026-05-28T01:45:02.000000 |
| cinder-volume    | gz-computer1.mystical.org@lvm         | nova | enabled | up    | 2026-05-28T01:45:00.000000 |
| cinder-volume    | gz-computer1.mystical.org@volumes-hdd | nova | enabled | up    | 2026-05-28T01:45:00.000000 |
| cinder-volume    | gz-computer1.mystical.org@volumes-ssd | nova | enabled | up    | 2026-05-28T01:45:06.000000 |
| cinder-scheduler | gz-computer1.mystical.org             | nova | enabled | up    | 2026-05-28T01:45:05.000000 |
| cinder-backup    | gz-computer1.mystical.org             | nova | enabled | up    | 2026-05-28T01:44:16.000000 |
+------------------+---------------------------------------+------+---------+-------+----------------------------+

# 查看显示当前存储卷
[root@gz-computer1 ~]# openstack volume list
+--------------------------------------+----------------+-----------+------+-------------------------------+
| ID                                   | Name           | Status    | Size | Attached to                   |
+--------------------------------------+----------------+-----------+------+-------------------------------+
| 59719aba-a68b-4cf2-b7f8-1f054cc389f6 | snapshot-test1 | in-use    |   10 | Attached to test on /dev/vdc  |
| b0d13acb-fda7-493f-8963-e98a27d582d4 |                | in-use    |   10 | Attached to test on /dev/vdb  |
| bddfe61c-7b74-43be-a1a8-bf71bc05119b | test-hdd       | available |   10 |                               |
+--------------------------------------+----------------+-----------+------+-------------------------------+
```

为什么比cinder组件多一个keyring文件，原因是cinder-backup它需要到cinder组件的存储池volumes去 读取原来的文件，并写入到新的备份存储池backups中。



#### 备份和恢复

##### 创建备份

创建存储卷备份，命令格式是：

```ABAP
openstack volume backup create --name name --description description \
     --force --snapshot <volume>
```

参数说明：

- `--name name`，后面跟上备份名称；
- `--description description`，备份描述信息
- `--force`，对正常使用的卷强制创建备份，对于读写频繁的卷建议卸载后再使用；
- `--snapshot snapshot`，对卷的某个快照创建备份
- `<volume>`，卷名称或id，一般建议使用id，避免名称冲突；

针对上面的测试卷创建快照的命令就是：

```bash
# 备份之前，先卸载快照
umount /data

# 备份
[root@gz-computer1 ~]# openstack volume backup create --name vdc-bak --description 'vdc 磁盘快照' --force 59719aba-a68b-4cf2-b7f8-1f054cc389f6
+-----------+--------------------------------------+
| Field     | Value                                |
+-----------+--------------------------------------+
| id        | df2ef769-a700-4a38-9474-e00d12a2e0fb |
| name      | vdc-bak                              |
| volume_id | 59719aba-a68b-4cf2-b7f8-1f054cc389f6 |
+-----------+--------------------------------------+

# 创建成功后，查看
[root@gz-computer1 /etc/ceph]# openstack volume backup list
+--------------------------------------+---------+--------------+-----------+------+
| ID                                   | Name    | Description  | Status    | Size |
+--------------------------------------+---------+--------------+-----------+------+
| bf65d00d-647a-4ec5-8f51-849fc73033f9 | vdc-bak | vdc 磁盘快照 | available |   10 |
+--------------------------------------+---------+--------------+-----------+------+
```



##### 备份恢复

现在我们在挂载的虚拟机上删除卷中的数据，然后从卷备份中恢复，恢复命令是：

```bash
# 从 test vm 上卸载
[root@gz-computer1 /etc/ceph]# openstack server remove volume test 59719aba-a68b-4cf2-b7f8-1f054cc389f6

# 状态从 in-use 变为 available
[root@gz-computer1 /etc/ceph]# openstack volume list
+--------------------------------------+----------------+-----------+------+-------------------------------+
| ID                                   | Name           | Status    | Size | Attached to                   |
+--------------------------------------+----------------+-----------+------+-------------------------------+
| 59719aba-a68b-4cf2-b7f8-1f054cc389f6 | snapshot-test1 | available |   10 |                               |
| b0d13acb-fda7-493f-8963-e98a27d582d4 |                | in-use    |   10 | Attached to test on /dev/vdb  |
| bddfe61c-7b74-43be-a1a8-bf71bc05119b | test-hdd       | available |   10 |                               |
+--------------------------------------+----------------+-----------+------+-------------------------------+

# 恢复
[root@gz-computer1 /etc/ceph]# cinder backup-restore --volume 59719aba-a68b-4cf2-b7f8-1f054cc389f6 bf65d00d-647a-4ec5-8f51-849fc73033f9
+-------------+--------------------------------------+
| Property    | Value                                |
+-------------+--------------------------------------+
| backup_id   | bf65d00d-647a-4ec5-8f51-849fc73033f9 |
| volume_id   | 59719aba-a68b-4cf2-b7f8-1f054cc389f6 |
| volume_name | snapshot-test1                       |
+-------------+--------------------------------------+

# 再重新挂到 vm 上
```

![image-20260528105923954](D:\git_repository\cyber_security_learning\markdown_img\image-20260528105923954.png)

![image-20260528110006351](D:\git_repository\cyber_security_learning\markdown_img\image-20260528110006351.png)

![image-20260528110028521](D:\git_repository\cyber_security_learning\markdown_img\image-20260528110028521.png)

![image-20260528110158338](D:\git_repository\cyber_security_learning\markdown_img\image-20260528110158338.png)

连接 test 实例后，挂载到目录，查看发现数据恢复。完美！



##### 备份删除

删除备份使用下面的命令：

```bash
[root@gz-computer1 /etc/ceph]# openstack volume backup delete bf65d00d-647a-4ec5-8f51-849fc73033f9
```



# Openstack 网络服务 Neutron

Neutron是用来管理OpenStack集群中的网络资源，是虚拟化中三个核心资源（计算、网络、存储）之 一，也是最复杂的模块之一，这个模块我们需要花上大半天的时间去理解。和其他类型的资源一样， 网络资源虚拟化也是由Linux上的基础组件慢慢搭建而成的，下面我们先来看LInux虚拟网络。

需要准备3个环境：

- 使用 linuxbridge 做 agent 的网络
- 使用 ovs 做 agent 的网络
- 使用 ovn 做 agent 的网络

需要搞懂下面这些逻辑：

- 同宿主机之间的虚拟机通信方式
- 不同宿主机之间的通信方式



## 网络基础知识

在看具体的虚拟网络实现之前，我们先看下网络架构的发展历史。



### 二层网络模型

在最早期入行的时候，整个公司就是用的一张大二层网络，网络架构看起来就像下面这样：

![image-20260528112036268](D:\git_repository\cyber_security_learning\markdown_img\image-20260528112036268.png)

这样的二层网络非常简单，也比较好维护，一个办公室里就是一个傻瓜式交换机把所有电脑连起来。 然后所有傻瓜式交换机上联到一个带路由功能的三层交换机，然后接到运营商的光猫，实现全公司的人上网。

这种网络虽然简单，但是使用起来也有很多麻烦。尤其是中毒或者乱插线的时候，一不小心插个环 路，整个公司的网络就断了。因此随着技术发展，就出现了虚拟机局域网VLAN。



### VLAN

虚拟局域网简单点说，就是分组，把同一个部门的几台电脑编为一个组，分配一个VLAN ID，然后在这些电脑连接的交换机端口上进行编号，俗称打tag，每个端口定义只有这个组里的数据包可以通过， 这样就形成了一个个逻辑局域网。像下面示意图里看到的样子。

![image-20260528112220658](D:\git_repository\cyber_security_learning\markdown_img\image-20260528112220658.png)

三台蓝色标识的电脑是一个VLAN，两台黄色的电脑是一个VLAN，在三层交换机上可以添加VLAN之间不同的路由，这样不同的VLAN之间就可以互相通信。 这样做的好处就是，当一个局域网里出现环路或者因为中毒出现广播风暴时，只会影响它这一个VLAN 里的电脑，对其他的电脑没有太大影响，能够把问题控制在较小的范围内，大大减轻了网工的工作难度。

在传统的VLAN技术中，标准的 VLAN 编号最大是4096，也就是说最多只能划分四千多个虚拟局域网， 对于一些中小型公司来说，完全够用了。但是随着虚拟化技术的出现和云计算的快速发展，在大规模网络中 VLAN 就不再适用了。

在云计算出现后，大家可以直接去公有云上购买虚拟机来直接使用，不同的用户之间，你需要实现网络隔离，不同的业务之间，基于安全因素也需要实现网络隔离。

同时随着硬件技术的发展，在单台服务器上就可以承载几十上百台虚拟机，一个大型数据中心中的虚拟机数量甚至能达到几十上百万，4000多个 VLAN 远远无法满足实际的生产需要。基于这样的现状，就出现了现在使用的各种叠加（Overlay）网络，常见的主要有 VxLAN、GRE 等。



### VxLAN

VxLAN（Virtual eXtensible Local Area Network，虚拟可扩展局域网），采用MAC in UDP封装方式， 是基于3层网络进行扩展的一种虚拟化技术，因此在Linux系统上创建虚拟的VxLAN设备的时候也会同 步创建一个UDP 套接字（Socket）。

对比上面的7层网络模型我们可以知道，VxLAN的数据包传输是在4层，它的数据包格式如下所示:

![image-20260528112612290](D:\git_repository\cyber_security_learning\markdown_img\image-20260528112612290.png)

中间负责对虚拟机数据进行封装并添加VxLAN头部的设备被称为VTEP端点。

VxLAN 设备创建的 UDP 套接字会向内核注册对 UDP 包的处理，这个 UDP 套接字还绑定了VxLAN 处理数据包的回调函数。当有数据包进来的时候，网络协议栈发现有对应的 UDP 套接字监听，就会把对应的 数据包转交给这个 UDP 套接字指定的回调函数来处理，这个过程是直接在内核里完成，并没有上层程序参与，因此我们在计算节点或者控制节点上，能看到有监听对应的端口，但是找不到实际的进程， 如下所示：

```bash
[root@rl-ceph1 ~]#
[root@gz-controller1 ~]# ss -tunlp|grep 4789
udp        0      0 0.0.0.0:8472            0.0.0.0:*

[root@gz-controller1 ~]# ss -tunlp|grep 8472
udp        0      0 0.0.0.0:4789            0.0.0.0:* 
udp6       0      0 :::4789                 :::*  
```

linuxbridge 实现的 VxLAN 设备默认监听的端口是8472，OVS 实现的 VxLAN 设备默认监听的端口是 4789。



## Linux 网络虚拟化

虚拟机的虚拟网络最终都是要配置到宿主机上的，因此我们需要先理解Linux上的虚拟机网络机制。先来看下普通的物理网络结构，物理服务器一般都会先连接到二层物理交换机上，二层物理交换机将流量汇聚以后连接到具有路由交换功能的三层交换机上，像下面图中演示的那样

![image-20260528113246714](D:\git_repository\cyber_security_learning\markdown_img\image-20260528113246714.png)

那么当虚拟化技术引入后，就可以在一台物理机上虚拟出多个虚拟机，这些虚拟机都有自己的网络， 那么它的虚拟网络结构看起来就是下面这样：

![image-20260528113325719](D:\git_repository\cyber_security_learning\markdown_img\image-20260528113325719.png)

相同网段的虚拟机连接到同一个虚拟交换机上，而虚拟交换机直接连接到我们的物理网卡上，负责把流量送出宿主机。那么要实现上面图中的虚拟网络，我们必须要实现虚拟机的网卡和它连接的虚拟交换机，下面来看下具体的实现。



### 虚拟网卡

#### TAP设备

TAP/TUN 是内核实现的一对虚拟网络设备，TAP 设备在二层网络上工作，而 TUN 设备则在三层网络上工作，Linux内核通过 TAP/TUN 设备向绑定该设备的用户空间程序发送数据，反过来用户空间程序向 TAP/TUN设备发送数据，就像向实际的物理网卡发送数据一样，因此基于 TAP 设备驱动就可以实现虚拟网卡的功能。

![image-20260528114500803](D:\git_repository\cyber_security_learning\markdown_img\image-20260528114500803.png)

我们知道虚拟机在计算节点上就是用户空间的一个kvm程序，虚拟机中的每个虚拟网卡（vNIC）都会和hypervisor（kvm）中的一个TAP设备相连。因此正常情况下你创建一个虚拟机，就会在计算节点上创建一个tap设备。如下所示：

```bash
# 查看在测试集群中的虚拟机
root@gz-computer1 ~]# virsh list
 Id   名称                状态
--------------------------------
 1    instance-0000000a   运行
 
# 对应的 tab 设备
[root@gz-computer1 ~]# ip a|grep tap
6: tap6005ff20-d7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master brq497bf174-ea state UNKNOWN group default qlen 1000
```

当创建一个 TAP 设备时，在Linux设备文件目录下会生成一个对应的字符设备文件，TAP设备在系统中的配置路径是：

```bash
[root@gz-computer1 ~]# ls /sys/devices/virtual/net
brq497bf174-ea  lo  tap6005ff20-d7  virbr0

[root@gz-computer1 ~]# ls /sys/devices/virtual/net/tap6005ff20-d7/
addr_assign_type    dormant            name_assign_type      speed
address             duplex             napi_defer_hard_irqs  statistics
addr_len            flags              netdev_group          subsystem
broadcast           gro_flush_timeout  operstate             testing
brport              group              owner                 threaded
carrier             ifalias            phys_port_id          tun_flags
carrier_changes     ifindex            phys_port_name        tx_queue_len
carrier_down_count  iflink             phys_switch_id        type
carrier_up_count    link_mode          power                 uevent
dev_id              master             proto_down            upper_brq497bf174-ea
```

用户空间程序可以像打开普通文件一样对这里的 tap文件进行读写。

当对这个 TAP 设备执行写入操作时，Linux网络子系统就会认为TAP设备接收到了数据，并请求内核接收它，然后根据对应的网络规则来处理数据包。

当外界数据进入到物理网卡，然后由虚拟网桥进行数据转发，根据数据包的目的mac地址发送到对应的TAP设备中。

用户程序执行读请求时，相当于向内核查询TAP设备上是否有数据需要被发送，如果有，取到用户程序里，完成TAP设备的数据发送功能。

用户空间程序通过系统的read/write系统调用，和本机进行网络通信。基本流程如下所示：

![image-20260528115151851](D:\git_repository\cyber_security_learning\markdown_img\image-20260528115151851.png)

虚拟机中的虚拟网卡到 TAP 设备的关联是由 KVM 来实现的，KVM 把他们关联到一起以后，虚拟机的网卡就具备了Mac地址等基本属性，就能够接收外部的数据包，就像是有了一块真正的网卡一样。



每跑一个Openstack VM，就会有一个 KVM 进程

```bash
[root@gz-computer1 ~]# virsh list
 Id   名称                状态
--------------------------------
 1    instance-0000000a   运行
 
# 查看 KVM 进程
[root@gz-computer1 ~]# ps aux|grep kvm
qemu        2954  9.1  3.1 5130060 504584 ?      Sl   09:08  24:47 /usr/libexec/qemu-kvm -name guest=instance-0000000a,debug-threads=on -S -object {"qom-type":"secret","id":"masterKey0","format":"raw","file":"/var/lib/libvirt/qemu/domain-1-instance-0000000a/master-key.aes"} -machine pc-i440fx-rhel7.6.0,usb=off,dump-guest-core=off,memory-backend=pc.ram,acpi=on -accel tcg -cpu qemu64 -m size=1048576k -object {"qom-type":"memory-backend-ram","id":"pc.ram","size":1073741824} -overcommit mem-lock=off -smp 1,sockets=1,dies=1,clusters=1,cores=1,threads=1 -uuid 7908a465-6b8f-41f3-9463-f34911d75524 -smbios type=1,manufacturer=RDO,product=OpenStack Compute,version=28.3.0-1.el9s,serial=7908a465-6b8f-41f3-9463-f34911d75524,uuid=7908a465-6b8f-41f3-9463-f34911d75524,family=Virtual Machine -no-user-config -nodefaults -chardev socket,id=charmonitor,fd=26,server=on,wait=off -mon chardev=charmonitor,id=monitor,mode=control -rtc base=utc -no-shutdown -boot strict=on -device {"driver":"piix3-usb-uhci","id":"usb","bus":"pci.0","addr":"0x1.0x2"} -blockdev {"driver":"host_device","filename":"/dev/nova-volumes/7908a465-6b8f-41f3-9463-f34911d75524_disk","aio":"native","node-name":"libvirt-2-storage","read-only":false,"cache":{"direct":true,"no-flush":false}} -device {"driver":"virtio-blk-pci","bus":"pci.0","addr":"0x4","drive":"libvirt-2-storage","id":"virtio-disk0","bootindex":1,"write-cache":"on"} -object {"qom-type":"secret","id":"libvirt-1-storage-auth-secret0","data":"jfYnRA6CbrlxsTd+oiGaQWCl7Wwicv3QHS14tPgckUY=","keyid":"masterKey0","iv":"GzJ50Rc+V1KPdIHmHu8Qww==","format":"base64"} -blockdev {"driver":"rbd","pool":"ssd-pool","image":"volume-b0d13acb-fda7-493f-8963-e98a27d582d4","server":[{"host":"10.2.100.220","port":"6789"},{"host":"10.2.100.221","port":"6789"},{"host":"10.2.100.222","port":"6789"}],"user":"cinder","auth-client-required":["cephx","none"],"key-secret":"libvirt-1-storage-auth-secret0","node-name":"libvirt-1-storage","read-only":false,"discard":"unmap","cache":{"direct":true,"no-flush":false}} -device {"driver":"virtio-blk-pci","bus":"pci.0","addr":"0x5","drive":"libvirt-1-storage","id":"virtio-disk1","write-cache":"on","serial":"b0d13acb-fda7-493f-8963-e98a27d582d4"} 

# 这里可以看到 fd 是 28，可以通过 ls -l /proc/2954/fd 查看到
-netdev {"type":"tap","fd":"28","id":"hostnet0"} 

# 这里的mac地址和 Guest OS 的 eth0 的网卡 mac 地址一致
-device {"driver":"virtio-net-pci","host_mtu":1500,"netdev":"hostnet0","id":"net0","mac":"fa:16:3e:82:f8:72","bus":"pci.0","addr":"0x3"} -add-fd set=0,fd=27,opaque=serial0-log -chardev pty,id=charserial0,logfile=/dev/fdset/0,logappend=on -device {"driver":"isa-serial","chardev":"charserial0","id":"serial0","index":0} -device {"driver":"usb-tablet","id":"input0","bus":"usb.0","port":"1"} -device {"driver":"usb-kbd","id":"input1","bus":"usb.0","port":"2"} -audiodev {"id":"audio1","driver":"none"} -vnc 10.2.100.201:0,audiodev=audio1 -device {"driver":"virtio-vga","id":"video0","max_outputs":1,"bus":"pci.0","addr":"0x2"} -device {"driver":"virtio-balloon-pci","id":"balloon0","bus":"pci.0","addr":"0x6"} -object {"qom-type":"rng-random","id":"objrng0","filename":"/dev/urandom"} -device {"driver":"virtio-rng-pci","rng":"objrng0","id":"rng0","bus":"pci.0","addr":"0x7"} -device {"driver":"vmcoreinfo"} -sandbox on,obsolete=deny,elevateprivileges=deny,spawn=deny,resourcecontrol=deny -msg timestamp=on
```

解析: 为什么 Guest OS 网卡的 MAC 地址与 TAP 网卡的 MAC 地址不一致

```bat
# 真正的数据模型是：
Guest OS
   ↓
virtio-net 驱动
   ↓
虚拟 PCI 网卡
   ↓
QEMU
   ↓
TAP fd
   ↓
Linux 网络栈

TAP 并不是对端机器，而更像是一个注入 Linux 网络栈的入口

# 整个通讯流程是：
1. Guest 发包： SRC MAC = fa:16:3e:82:f8:72；DST MAC = xx:xx:xx 生成 Ethernet Frame
2. 然后 Guest 驱动 -> virtio ring -> QEMU （QEMU 拿到完整 Ethernet Frame）

# 上述步骤2补充讲述
Guest 驱动负责 “把数据放进共享内存队列”
virtio ring 负责 “Guest 和 QEMU 之间的共享队列”

3. QEMU 从共享内存读取 Ethernet Frame，通过 write(tap_fd, ethernet_frame) 将其发给 TAP，此时 TAP 收到数据，然后给到网络协议栈，最后到物理网卡

# 查看 tap 和 实例对应关系
[root@gz-computer1 ~]# virsh list
 Id   名称                状态
--------------------------------
 1    instance-0000000a   运行
 
[root@gz-computer1 ~]# virsh dumpxml instance-0000000a
......
<interface type='bridge'>
      <mac address='fa:16:3e:82:f8:72'/>
      <source bridge='brq497bf174-ea'/>
      <target dev='tap6005ff20-d7'/>   # tap网卡名
      <model type='virtio'/>
      <driver name='qemu'/>
      <mtu size='1500'/>
      <alias name='net0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
    </interface>
......

# 查看网桥上连接的tap设备
# tap6005ff20-d 关联到了brq497bf174-ea网桥上
[root@gz-computer1 ~]# bridge link show
6: tap6005ff20-d7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master brq497bf174-ea state forwarding priority 32 cost 100 

# 使用 nmcli conn 查看
[root@gz-computer1 ~]# nmcli conn
NAME            UUID                                  TYPE      DEVICE         
eth0            c4b0c225-e51d-31e9-926e-a3421cd8e220  ethernet  eth0           
eth1            5eb4da26-5d1d-30a5-8747-80181ed055fa  ethernet  eth1           
lo              991d2e8e-5adf-448a-86cf-dffdfa10442a  loopback  lo             
brq497bf174-ea  9b946720-b1ca-4b0d-857d-3dac0d9966af  bridge    brq497bf174-ea 
tap6005ff20-d7  8954c582-259d-4472-b376-bc11759f5274  tun       tap6005ff20-d7 
virbr0          70eaa828-4746-4f91-94f3-de28477f884b  bridge    virbr0 
```



##### TAP设备的管理

在 Linux 中，TAP 设备的管理都是通过 ip 命令来实现的，主要有以下这些部分。



###### TAP 设备的创建

```bash
[root@gz-computer1 ~]# ip tuntap add tap0 mode tapc
```

这个命令会创建一个叫做tap0的TAP设备，因为TAP设备属于二层设备，会自动给它分配一个MAC地址（MAC 是Openstack Neutron 分配的）。在 Rocky Linux 9 上，添加的 tap 设备会自动被绑定到网桥上。



###### 查看TAP设备的信息

要查看创建好的TAP设备的信息，使用命令：

```bash
[root@gz-computer1 ~]# ip addr show tap0
7: tap0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 2e:1d:b4:71:32:6a brd ff:ff:ff:ff:ff:ff
```



###### 绑定MAC地址到TAP设备

TAP设备属于二层设备，一般会需要绑定一个MAC地址，如果不想使用默认的MAC地址，可以使用下面的命令给它换一个：

```bash
[root@gz-computer1 ~]# ip link set dev tap0 address 00:11:22:33:44:55
[root@gz-computer1 ~]# ip addr show tap0
7: tap0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
```



###### 启动 TAP 设备

当TAP设备配置好以后，就可以启用它，命令是：

```bash
[root@gz-computer1 ~]# ip link set tap0 up

# 显示UP，但是实际还是DOWN的状态
[root@gz-computer1 ~]# ip addr show tap0
7: tap0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
```



###### 绑定IP地址

tap设备可以绑定IP地址，但是实际上并没有什么作用。

```bash
[root@gz-computer1 ~]# ip addr add 192.168.1.2/24 dev tap0
[root@gz-computer1 ~]# ip addr show tap0
7: tap0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.2/24 scope global tap0
       valid_lft forever preferred_lft forever
```

直接绑IP地址的时候，导致网卡断开，无法连接，原因是因为tap设备只是一个二层设备，绑定IP地址无意义



###### 删除TAP设备

```bash
[root@gz-computer1 ~]# ip tuntap del dev tap0 mode tap
```



#### TUN设备

TAP设备是工作在二层的，而TUN设备是工作在三层的。创建的TAP设备可以绑定MAC地址，不能绑 定IP地址，而TUN设备上不支持绑定MAC地址，只能绑定IP地址，是用来实现点对点通信的，和TAP 设备实际上没多大关系，例如常用的OpenVPN软件即使通过tun设备实现内网之间互通的。而我们 Neutron组件里的Overlay类型的网络，也是通过tun设备实现不同节点之间的网络互通，稍后在overlay 网络部分会详细介绍。



#### Veth设备



## Neutron架构

网络资源模型就是 Neutron 管理的资源对象，例如网络（Network）、子网（Subnet）、路由器 （router）等。要想掌握 Neutron 组件，就必须要对这些基本的网络概念有一定的基本了解。

网络也被称为二层网络，所有接入到同一个二层网络的设备，互相之间通信时，二层交换机会根据 mac 地址来确定每个设备的位置，而我们通常所说的主机IP地址，则属于三层网络的概念，也就是 Neutron里的子网，在二层网络中划分子网，子网中才能配置IP地址范围、网关、DNS这些基本信息， 在创建虚拟机的时候，给虚拟机选择一个子网，虚拟机就能分配一个子网范围内的IP地址。

不同子网之间的虚拟机互相通信，就到了三层路由交换的层面了，这个时候我们就需要路由器或者具备路由功能的交换机来实现对应的功能。Neutron组件有提供软件实现的路由器，但是通常性能较弱， 在实际生产中不会使用，Neutron里目前支持的二层网络类型有：

- flat，最普通的二层网络，不支持网络隔离，所有虚拟机都处于同一个广播域。目前已经不推荐使用。
- VLAN，支持虚拟网络隔离，在中小型企业使用的比较多，配置也比较简单，一般和物理交换机搭配使用。
- VxLAN，通过三层网络UDP协议的封装实现对虚拟网络的扩展，因此每个节点需要有一 个独立的IP地址可以互相访问，最多可以实现1600万个虚拟机网络。
- GENEVE，通用虚拟网络封装，和VxLAN类似，通过UDP协议来通信

在熟悉了这些基本概念以后，我们就需要考虑一个问题，怎么把Neutron里的网络、子网的概念和现实 中物理设备上的网络概念对应起来，下面我们就看实际的网络实现模型。



## Neutron软件架构

### Neutron 插件

#### ML2 插件

ML2 插件是目前 Neutron 组件中的核心插件，核心插件的作用是负责管理和维护网络、子网、端口这些核心资源的状态信息，ML2的完整框架如下所示

ML2插件对接的是网络类型管理器和网络组件管理器，通过这种机制，把网络类型和底层具体实现网络的组件分开，并通过驱动的方式进行管理。

网络拓扑类型就是我们之前提到的Flat、VLAN、VxLAN这些，由不同的类型驱动实现这种网络类型的具体配置和参数，并且由网络类型管理器来负责管理，向ML2插件提供统一的管理接口。目前支持的网络类型驱动有：

- Flat类型驱动
- VLAN类型驱动，这种类型的驱动在配置时，需要指定物理网络的名称，即物理网络接口。同时还需要指定这个网络VLAN ID范围，对应外部物理网络支持的VLAN范围
- 隧道（Tunnel）类型驱动，VxLAN和GRE都是属于隧道类型网络

网络组件指的是具体实现这些二层网络的组件，在之前我们提到了常用的有 linuxbridge 和 OpenvSwitch，以及后面可能会应用越来越广泛的OVN组件。网络组件由组件管理器负责管理，并向 ML2 插件提供一个统一的管理接口。



#### 服务插件

ML2插件是负责管理和实现二层网络的，在二层网络上实现的服务，则由服务插件来实现。目前常用的主要有两个，分别是：

- 负载均衡，负载均衡用于在虚拟机实例之间提供负载均衡服务，也被称为LBaaS。但是后面已经独立成一个单独的项目Octavia，在后面的第10节常用的其他服务中，会详细讲解。



#### Neutron代理

ML2插件主要是管理虚拟网络资源，确认他们的状态信息。具体的网络设置则是由对应的代理插件完成的，目前常用的代理插件有：

- **linuxbridge-agent**，实现具体的虚拟网络，支持flat、VLAN、VXLAN网络
- **ovs-agent**，实现具体的虚拟网络，支持flat、VLAN、VXLAN、GRE等网络
- **dhcp-agent**，提供 DHCP 功能，给虚拟机分发 IP 地址，参与虚拟机获取元数据信息流程；
- **metadata-agent**，参与虚拟机获取元数据信息流程
- **l3-agent**，提供路由组件和浮动IP功能。

组件具体的功能演示请查看实战内容：

- 7.1 实战1：测试环境二层网络添加VLAN、三层网络和VxLAN网络支持
- 7.2 实战2：neutron+ovs网络配置





### 虚拟交换机



## linuxbridge实现

linuxbridge目前只支持flat、VLAN和VXLAN类型的网络，因此它可以实现这三种网络模型，具体实现 架构如下所示：

### 网络节点和计算节点Flat网络模型linuxbridge实现

![image-20260528175628590](D:\git_repository\cyber_security_learning\markdown_img\image-20260528175628590.png)





### 网络节点和计算节点VLAN网络模型linuxbridge实现

![image-20260528175657539](D:\git_repository\cyber_security_learning\markdown_img\image-20260528175657539.png)

#### 添加对于 VLAN 的支持

```bash
# 在控制节点配置
# 修改 ml2 配置
[root@gz-controller1 ~]# vim /etc/neutron/plugins/ml2/ml2_conf.ini
[ml2_type_vlan]
network_vlan_ranges = provider

# 更新数据库
[root@gz-controller1 ~]# su -s /bin/sh -c "neutron-db-manage --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head" neutron
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
  正在对 neutron 运行 upgrade...
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
  确定
  
# 重启 neutron-server
[root@gz-controller1 ~]# systemctl restart neutron-server

# 创建一个VLAN类型的网络
[root@gz-controller1 ~]# openstack network create --share --provider-physical-network provider --provider-network-type vlan --provider-segment 2 vlan_network
+---------------------------+--------------------------------------+
| Field                     | Value                                |
+---------------------------+--------------------------------------+
| admin_state_up            | UP                                   |
| availability_zone_hints   |                                      |
| availability_zones        |                                      |
| created_at                | 2026-05-28T14:38:13Z                 |
| description               |                                      |
| dns_domain                | None                                 |
| id                        | 05d9e583-db0d-4f5c-b8d8-6f8764e644b2 |
| ipv4_address_scope        | None                                 |
| ipv6_address_scope        | None                                 |
| is_default                | None                                 |
| is_vlan_transparent       | None                                 |
| mtu                       | 1500                                 |
| name                      | vlan_network                         |
| port_security_enabled     | True                                 |
| project_id                | 91dfd3026f58437cbff8e9526f31823c     |
| provider:network_type     | vlan                                 |
| provider:physical_network | provider                             |
| provider:segmentation_id  | 2                                    |
| qos_policy_id             | None                                 |
| revision_number           | 1                                    |
| router:external           | Internal                             |
| segments                  | None                                 |
| shared                    | True                                 |
| status                    | ACTIVE                               |
| subnets                   |                                      |
| tags                      |                                      |
| tenant_id                 | 91dfd3026f58437cbff8e9526f31823c     |
| updated_at                | 2026-05-28T14:38:13Z                 |
+---------------------------+--------------------------------------+

# 上面创建了一个vlan id=2的vlan网络，名称是vlan_network，在这个网络里创建一个子网：
[root@gz-controller1 ~]# openstack subnet create --subnet-range 192.168.100.0/24 --gateway 192.168.100.1 --network vlan_network --allocation-pool start=192.168.100.2,end=192.168.100.254 --dns-nameserver 192.168.31.1 vlan-100
+----------------------+--------------------------------------+
| Field                | Value                                |
+----------------------+--------------------------------------+
| allocation_pools     | 192.168.100.2-192.168.100.254        |
| cidr                 | 192.168.100.0/24                     |
| created_at           | 2026-05-28T14:39:20Z                 |
| description          |                                      |
| dns_nameservers      | 192.168.31.1                         |
| dns_publish_fixed_ip | None                                 |
| enable_dhcp          | True                                 |
| gateway_ip           | 192.168.100.1                        |
| host_routes          |                                      |
| id                   | 03d9ee4f-3caf-4431-82d1-26d8bdfa664c |
| ip_version           | 4                                    |
| ipv6_address_mode    | None                                 |
| ipv6_ra_mode         | None                                 |
| name                 | vlan-100                             |
| network_id           | 05d9e583-db0d-4f5c-b8d8-6f8764e644b2 |
| project_id           | 91dfd3026f58437cbff8e9526f31823c     |
| revision_number      | 0                                    |
| segment_id           | None                                 |
| service_types        |                                      |
| subnetpool_id        | None                                 |
| tags                 |                                      |
| updated_at           | 2026-05-28T14:39:20Z                 |
+----------------------+--------------------------------------+
```

查看WEB UI，注意是管理员 -> 网络

![image-20260528224417868](D:\git_repository\cyber_security_learning\markdown_img\image-20260528224417868.png)





### 网络节点和计算节点VXLAN网络模型linuxbridge实现

![image-20260528175754973](D:\git_repository\cyber_security_learning\markdown_img\image-20260528175754973.png)



#### 添加三层网络支持

在上面的二层网络中添加了 VLAN 支持后，我们可以看到需要外部的物理交换机支持，能够处理带有 VLAN ID的二层数据包才能够实现内部虚拟机连接外网。因此对于一些小型企业来说，可能不具备这种能力，例如他们只有不能划分VLAN的傻瓜式二层交换机，同时二层网络也无法提供绑定浮动 IP 的能力。

那么我们可以在 Neutron 上添加三层网络支持，能够自己定义软件实现的Router，来实现虚拟机上外网的服务，根据下面的步骤来配置

##### 控制节点修改

```bash
# server配置文件修改
[root@gz-controller1 ~]# vim /etc/neutron/neutron.conf 
[DEFAULT]
# 添加
service_plugins = router
allow_overlapping_ips = True

# ml2插件配置修改
# 在flat和vlan网络里都添加了外部网络的名称external
[root@gz-controller1 ~]# vim /etc/neutron/plugins/ml2/ml2_conf.ini 
[ml2]
type_drivers = flat,vlan,vxlan

[ml2_type_flat]
flat_networks = provider,external

[ml2_type_vlan]
network_vlan_ranges = provider,external

# linuxbridge agent 配置修改
# 增加了外部网络和关联的网卡，因为我们这里两台机器只能通过管理网络对外通信，因此外部网络必须要和管理网络网卡eth0关联。
[root@gz-controller1 ~]# vim /etc/neutron/plugins/ml2/linuxbridge_agent.ini
[linux_bridge]
physical_interface_mappings = provider:eth1,external:eth0

# L3 agent配置修改
[root@gz-controller1 ~]# vim /etc/neutron/l3_agent.ini
interface_driver = linuxbridge

# 指定实现L3 agent的组件是linuxbridge，所有配置修改完成后重启neutron所有组件服务
    [root@gz-controller1 ~]# systemctl restart neutron-server neutron-linuxbridge-agent neutron-dhcp-agent neutron-metadata-agent neutron-l3-agent

# 查看 L3 agent 状态
[root@gz-controller1 ~]# openstack network agent list
+--------------------------------------+--------------------+-----------------------------+-------------------+-------+-------+---------------------------+
| ID                                   | Agent Type         | Host                        | Availability Zone | Alive | State | Binary                    |
+--------------------------------------+--------------------+-----------------------------+-------------------+-------+-------+---------------------------+
| 0b429046-1184-43fc-adb3-271d69323880 | Linux bridge agent | gz-controller1.mystical.org | None              | :-)   | UP    | neutron-linuxbridge-agent |
| 19521016-b7e7-4c6b-a0b0-194fc0266684 | L3 agent           | gz-controller1.mystical.org | nova              | :-)   | UP    | neutron-l3-agent          |
| 2e3081bb-f210-4c11-8b5f-3430b08fb758 | Metadata agent     | gz-controller1.mystical.org | None              | :-)   | UP    | neutron-metadata-agent    |
| 80bb0ec7-a216-4607-8cb1-09c2fa71ff22 | Linux bridge agent | gz-computer1.mystical.org   | None              | :-)   | UP    | neutron-linuxbridge-agent |
| ba655414-014a-43f9-9b6a-c81015a4da89 | DHCP agent         | gz-controller1.mystical.org | nova              | :-)   | UP    | neutron-dhcp-agent        |
+--------------------------------------+--------------------+-----------------------------+-------------------+-------+-------+---------------------------+
```



##### 计算节点修改

因为L3 agent的配置只需要更改控制节点组件，计算节点不需要修改任何配置。



##### 验证

**创建外部网络**

在我们的实验环境中，外部网络就是我们的管理网络，可以上外网，因此被称为外部网络。然后再配 置一个router，将外部网络和我们OpenStack集群内部的网络关联到一起，这样我们内网里的虚拟机就可以通过这个router上外网了。

创建外部网络的命令是：

```bash
[root@gz-controller1 ~]# openstack network create --share --external --provider-physical-network external --provider-network-type flat external_network
+---------------------------+--------------------------------------+
| Field                     | Value                                |
+---------------------------+--------------------------------------+
| admin_state_up            | UP                                   |
| availability_zone_hints   |                                      |
| availability_zones        |                                      |
| created_at                | 2026-05-28T15:57:00Z                 |
| description               |                                      |
| dns_domain                | None                                 |
| id                        | 54c80d26-f182-43f7-8b09-65ddd154c4f5 |
| ipv4_address_scope        | None                                 |
| ipv6_address_scope        | None                                 |
| is_default                | False                                |
| is_vlan_transparent       | None                                 |
| mtu                       | 1500                                 |
| name                      | external_network                     |
| port_security_enabled     | True                                 |
| project_id                | 91dfd3026f58437cbff8e9526f31823c     |
| provider:network_type     | flat                                 |
| provider:physical_network | external                             |
| provider:segmentation_id  | None                                 |
| qos_policy_id             | None                                 |
| revision_number           | 1                                    |
| router:external           | External                             |
| segments                  | None                                 |
| shared                    | True                                 |
| status                    | ACTIVE                               |
| subnets                   |                                      |
| tags                      |                                      |
| tenant_id                 | 91dfd3026f58437cbff8e9526f31823c     |
| updated_at                | 2026-05-28T15:57:00Z                 |
+---------------------------+--------------------------------------+
```

上面的命令中的参数解释：

- `--external` 指定网络是外部的，
- `--provider-phyical-network external` 指定使用 external 标签指定的网络，根据linuxbridge agent配置文件里的映射关系我们知道，这个标签指定的网络是走eth0端口出去。

- `--provider-network-type flat`，我们的测试环境管理网络就是家里路由器dhcp分发的网 络，默认就是一个flat类型网络，没有vlan。



**创建子网**

然后在这个外部网络里创建一个子网：

```bash
# 查看 public 网卡网关
[root@gz-controller1 ~]# ip route
default via 10.2.84.1 dev eth0 proto static metric 100 
10.2.0.0/16 dev eth0 proto kernel scope link src 10.2.100.200 metric 100 
192.168.23.0/24 dev brq497bf174-ea proto kernel scope link src 192.168.23.151 
192.168.23.0/24 dev eth1 proto kernel scope link src 192.168.23.151 metric 101

[root@gz-controller1 ~]# openstack subnet create --network external_network     --no-dhcp --gateway 10.2.84.1     --dns-nameserver 114.114.114.114     --subnet-range=10.2.0.0/16     external_subnet
+----------------------+-------------------------------------------+
| Field                | Value                                     |
+----------------------+-------------------------------------------+
| allocation_pools     | 10.2.84.2-10.2.255.254,10.2.0.1-10.2.84.0 |
| cidr                 | 10.2.0.0/16                               |
| created_at           | 2026-05-28T16:07:54Z                      |
| description          |                                           |
| dns_nameservers      | 114.114.114.114                           |
| dns_publish_fixed_ip | None                                      |
| enable_dhcp          | False                                     |
| gateway_ip           | 10.2.84.1                                 |
| host_routes          |                                           |
| id                   | ba9d86f3-2790-414d-9bdc-81b1c47bd409      |
| ip_version           | 4                                         |
| ipv6_address_mode    | None                                      |
| ipv6_ra_mode         | None                                      |
| name                 | external_subnet                           |
| network_id           | 54c80d26-f182-43f7-8b09-65ddd154c4f5      |
| project_id           | 91dfd3026f58437cbff8e9526f31823c          |
| revision_number      | 0                                         |
| segment_id           | None                                      |
| service_types        |                                           |
| subnetpool_id        | None                                      |
| tags                 |                                           |
| updated_at           | 2026-05-28T16:07:54Z                      |
+----------------------+-------------------------------------------+
```

命令行参数解释：

- `--network external_netowrk`，这个子网所属的网络
- `--no-dhcp`，因为外部子网不需要分发IP地址，只提供一个外部网络的基本信息，因此禁 用dhcp功能；
- `--dns-nameserver` 外部网络dns
- `--gateway`，外部网络网关
- `--subnet-range` 外网网络范围

最后在子网上创建一个和Router连接的端口，命令是

```bash
[root@gz-controller1 ~]# openstack port create --network external_network --fixed-ip subnet=external_subnet,ip-address=10.2.100.254 --project admin external_port
+-------------------------+-----------------------------------------------------------------------------+
| Field                   | Value                                                                       |
+-------------------------+-----------------------------------------------------------------------------+
| admin_state_up          | UP                                                                          |
| allowed_address_pairs   |                                                                             |
| binding_host_id         |                                                                             |
| binding_profile         |                                                                             |
| binding_vif_details     |                                                                             |
| binding_vif_type        | unbound                                                                     |
| binding_vnic_type       | normal                                                                      |
| created_at              | 2026-05-28T16:10:38Z                                                        |
| data_plane_status       | None                                                                        |
| description             |                                                                             |
| device_id               |                                                                             |
| device_owner            |                                                                             |
| device_profile          | None                                                                        |
| dns_assignment          | None                                                                        |
| dns_domain              | None                                                                        |
| dns_name                | None                                                                        |
| extra_dhcp_opts         |                                                                             |
| fixed_ips               | ip_address='10.2.100.254', subnet_id='ba9d86f3-2790-414d-9bdc-81b1c47bd409' |
| id                      | 919415cb-97bd-41b2-acee-ac32ef8a33ad                                        |
| ip_allocation           | None                                                                        |
| mac_address             | fa:16:3e:53:26:62                                                           |
| name                    | external_port                                                               |
| network_id              | 54c80d26-f182-43f7-8b09-65ddd154c4f5                                        |
| numa_affinity_policy    | None                                                                        |
| port_security_enabled   | True                                                                        |
| project_id              | 91dfd3026f58437cbff8e9526f31823c                                            |
| propagate_uplink_status | None                                                                        |
| qos_network_policy_id   | None                                                                        |
| qos_policy_id           | None                                                                        |
| resource_request        | None                                                                        |
| revision_number         | 1                                                                           |
| security_group_ids      | 6546f149-7c4b-4057-bc5c-ba73e2019c7b                                        |
| status                  | DOWN                                                                        |
| tags                    |                                                                             |
| trunk_details           | None                                                                        |
| updated_at              | 2026-05-28T16:10:39Z                                                        |
+-------------------------+-----------------------------------------------------------------------------+
```

外部网络、子网和端口创建好以后，就可以把它和router关联起来了



**创建一个 router**

外部网络创建好以后，我们就可以创建一个router来把外部网络和内部网络关联到一起，创建router的 命令是：

```bash
[root@gz-controller1 ~]# openstack router create --project admin --description "connect external network and openstack subnet" external_router
+-------------------------+-----------------------------------------------+
| Field                   | Value                                         |
+-------------------------+-----------------------------------------------+
| admin_state_up          | UP                                            |
| availability_zone_hints |                                               |
| availability_zones      |                                               |
| created_at              | 2026-05-28T16:11:59Z                          |
| description             | connect external network and openstack subnet |
| distributed             | False                                         |
| enable_ndp_proxy        | None                                          |
| external_gateway_info   | null                                          |
| flavor_id               | None                                          |
| ha                      | False                                         |
| id                      | 4a8c1907-8174-4e67-a6e4-5d0ca12be5c5          |
| name                    | external_router                               |
| project_id              | 91dfd3026f58437cbff8e9526f31823c              |
| revision_number         | 1                                             |
| routes                  |                                               |
| status                  | ACTIVE                                        |
| tags                    |                                               |
| tenant_id               | 91dfd3026f58437cbff8e9526f31823c              |
| updated_at              | 2026-05-28T16:11:59Z                          |
+-------------------------+-----------------------------------------------+
```

router创建好以后，先把它和外网端口绑定：

```bash
[root@gz-controller1 ~]# openstack router add port external_router external_port
```

绑定成功后，再把要连接外网的子网和 router 关联起来，我们这里先关联第一次创建的 flat 网络里的子网flat_subnet，命令是：

```bash
[root@gz-controller1 ~]# openstack router add subnet external_router flat_subnet
```



补充：解决 linuxbridage拿不到IP的问题

```bash
# 查看 Neutron Port ID
[root@gz-computer1 ~]# openstack port list --server ecs1
+--------------------------------------+------+-------------------+--------------------------------------------------------------------------------+--------+
| ID                                   | Name | MAC Address       | Fixed IP Addresses                                                             | Status |
+--------------------------------------+------+-------------------+--------------------------------------------------------------------------------+--------+
| 63b914e6-303a-4b30-8e39-e11296b4a8f7 |      | fa:16:3e:d0:d9:c4 | ip_address='192.168.116.209', subnet_id='d1deb5fd-7c57-4823-b4e3-fc622c0757e5' | ACTIVE |
+--------------------------------------+------+-------------------+--------------------------------------------------------------------------------+--------+

# 关闭 OpenStack 对这个虚拟机网卡的“网络安全保护”
[root@gz-computer1 ~]# openstack port set --no-security-group 63b914e6-303a-4b30-8e39-e11296b4a8f7
[root@gz-computer1 ~]# openstack port set --disable-port-security 63b914e6-303a-4b30-8e39-e11296b4a8f7
```

> 或者不关闭网络安全保护，自行配置 yaml 文件，netplan apply 也可以，但是要注意 IP 要一致。





我们通过 linuxbridge 实现了 flat、VLAN 和 VXLAN 类型网络，但是因为 linuxbridge 自身的缺陷， 在实际生产中慢慢被 OVS 代替，因此我们在了解 linuxbridge实现的基础上，也需要掌握 OVS 这个工具的配置。下面我们通过 OVS 来实现 linuxbridge 实现的各种网络，将测试环境的 linuxbridge 配置全部更换为OVS的配置。











## OVS 实现

Open vSwitch也简称ovs，后面都直接使用ovs这个简称。它是一个企业级别的虚拟交换机软件，使用 C 语言开发，从上面的虚拟网桥概念中我们知道，它就是用来连接虚拟机、虚拟网卡以及物理机网卡的一个中间设备。

为什么Linux系统上有了原生的 linux bridge 组件，我们还需要另外实现 ovs 呢？这是因为 linux bridge 它只实现了网络接入和交换功能。但是在实际生产环境上物理交换机具备的功能，例如网络隔离 VLAN、 流量监控、流量控制、数据包分析、流量优化等必备需求在 linux bridge 上都无法满足，虚拟机之间的网络对于管理员来说是一个无法管理的盲区，因此才有了这样具备这些功能的 ovs 出现

同时OpenvSwitch还可以通过隧道技术，将所有计算节点上的ovs实例连接到一起，形成一个分布式的虚拟交换机，让整个集群中不同计算节点上的虚拟机之间都可以互联互通，也就是我们俗称的 SDN （Software Definition Network）技术，常见的应用场景就是Neutron里的VxLAN技术。

所有的OpenvSwitch 实例还支持上层的SDN控制器来进行管理，在一些大企业内部有专门的SDN硬件 控制器来管理OpenStack集群内部的网络。



### OVS 软件架构

OVS使用的各个组件之间的关系图如下所示：

![image-20260529102327033](D:\git_repository\cyber_security_learning\markdown_img\image-20260529102327033.png)

从这个架构图中可以看到，核心组件主要有4个：

- **ovs-vswitchd**，负责和外界各种管理命令交互的主进程
- **ovsdb-server**，负责和主进程交互并操作数据库的组件；
- **ovsdb**，负责存储虚拟网络内部各种逻辑设备的主数据库；
- **OpenvSwitch Kernel Module**，OpenvSwitch内核模块，实现OVS基本功能；



剩下的都是围绕着这几个核心组件的各种管理命令或者管理组件：

- ovs-ofctl，是通过OpenFlow协议和OVS创建的OpenFlow交换机交互的工具；

- sFlow Monitor，通过sFlow协议监控网络的工具；
- ovs-dpctl，负责管理和监控OVS中的datapath；
- ovs-appctl，负责和OVS主进程交互的组件；
- ovs-vsctl，负责配置管理的组件，例如网桥配置、端口配置等；
- ovsdb-client，负责和ovsdb-server交互，查询数据库、更新配置、获取统计信息等；
- ovsdb-tool，用于管理和操作OVS数据库，通常用于一些高级操作，例如数据库迁移和模式修改等；



### 切换 OVS 前期准备

清理资源，关闭Linuxbridge，为切换OVS做准备

```bash
# 如果有浮动IP，解除绑定，并删除计算实例，建议删除网络资源，后续重建

# 删除计算实例后查看，确认返回为空
[root@gz-controller1 ~]# openstack server list

# 查看剩余 Port，Port 是 Neutron 的一个逻辑对象。可以理解为“虚拟网卡对象”，返回为空 
[root@gz-controller1 ~]# openstack port list

# 查看网络，返回为空
[root@gz-controller1 ~]# openstack network list

# 查看网桥成员（停掉neutron-linuxbridge-agent，Neutron不会主动帮你清理已经创建好的Linux Bridge）
[root@gz-controller1 ~]# bridge link
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master brq54c80d26-f1 state forwarding priority 32 cost 2 
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master brq497bf174-ea state forwarding priority 32 cost 2 
7: eth1.2@eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master brq05d9e583-db state forwarding priority 32 cost 2 

# 经过确认，上述 Port 中没有 device_owner=compute:nova
# 关闭 neutron-linuxbridge-agent，并安装 neutron-openvswitch-agent
# 控制节点和计算节点都执行下列操作
[root@gz-controller1 ~]# systemctl disable --now neutron-linuxbridge-agent
Removed "/etc/systemd/system/multi-user.target.wants/neutron-linuxbridge-agent.servige-agent.serv
[root@gz-computer1 ~]# systemctl disable --now neutron-linuxbridge-agent
Removed "/etc/systemd/system/multi-user.target.wants/neutron-linuxbridge-agent.service".

# 当前情况是网卡上没IP，IP在网桥上
# 无论是 Linux Bridge 还是 OVS，只要物理网卡加入交换机（Bridge）成为 Port，IP 就应该配置在 Bridge 上，而不是配置在物理网卡上。
# 加入 OVS 的 eth0 相当于交换机的一个端口，而br-ex才是交换机本身。（IP不应在端口上，而应在交换机本身上）
# 第一步：把 IP 挂回 eth0
[root@gz-controller1 ~]# ip addr add 192.168.116.150/24 dev eth0
[root@gz-controller1 ~]# ip link set eth0 up

# 删除网桥上的IP
[root@gz-controller1 ~]# ip addr flush dev brq54c80d26-f1

# 解除绑定：
[root@gz-controller1 ~]# ip link set eth0 nomaster

# 删桥：
[root@gz-controller1 ~]# ip link set brq54c80d26-f1 down
[root@gz-controller1 ~]# brctl delbr brq54c80d26-f1

# eth1 和 eth0 原理相同

# 安装 openstack-neutron-openvswitch
[root@gz-controller1 ~]# dnf install -y openstack-neutron-openvswitch
[root@gz-computer1 ~]# dnf install -y openstack-neutron-openvswitch

# 启动
[root@gz-controller1 ~]# systemctl enable --now openvswitch.service 
Created symlink /etc/systemd/system/multi-user.target.wants/openvswitch.service → /usr/lib/systemd/system/openvswitch.service.
[root@gz-computer1 ~]# systemctl enable --now openvswitch.service
Created symlink /etc/systemd/system/multi-user.target.wants/openvswitch.service → /usr/lib/systemd/system/openvswitch.service.
```

> 最终切换后，IP 应该在 br-ex 上，而不是 eth0 上。就好像 IP 一定是在交换机上，而不会配在交换机的某个端口上。



### 二层网络+Router配置

为了实现Router可以正常连接外网，需要给专门为 Router 额外增加一个专用的可以连接外部网络的网卡，不需要配置IP地址，我这里控制节点上新增的网卡名称是ens20。



#### 准备工作

在进行底层组件切换之前，删除集群中之前创建的实例、网络和路由组件，避免底层使用OVS实现 后，之前创建的实例、网络和路由无法处理。



#### 控制节点

**server 配置文件修改**

server端配置文件neutron.con中默认已经启用了ml2和router组件，不需要再做任何修改。



**ml2插件配置文件修改**

打开ml2插件配置文件 `/etc/neutron/plugins/ml2/ml2_conf.ini` 文件，配置文件修改后如下所示：

```bash
[root@gz-controller1 ~]# vim /etc/neutron/plugins/ml2/ml2_conf.ini
[ml2]
type_drivers = flat,vlan,vxlan
tenant_network_types =
mechanism_drivers = openvswitch             # 其实最终只改这里
extension_drivers = port_security


[ml2_type_flat]
flat_networks = provider,external

[ml2_type_vlan]
network_vlan_ranges = provider,external

[securitygroup] 
enable_ipset = true

# 修改好后更新数据库
[root@gz-controller1 ~]# su -s /bin/sh -c "neutron-db-manage --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head" neutron
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
  正在对 neutron 运行 upgrade...
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
  确定
```



**配置 OVS**

```bash
[root@gz-controller1 ~]# vim /etc/neutron/plugins/ml2/openvswitch_agent.ini
[ovs]
bridge_mappings = provider:br-eth,external:br-ex  #指定了两个网桥，br-eth是内部二层网络互通使用的网桥，br-ex是外部网络使用的网桥。

[securitygroup]
firewall_driver = iptables_hybrid
```



**添加 OVS 需要的网桥**

上面配置文件中配置了provider网络对应的设备是br-eth网桥，external网络对应的物理设备是br-ex网 桥，下面需要手动创建它：

```bash
[root@gz-controller1 ~]# ovs-vsctl add-br br-eth
[root@gz-controller1 ~]# ovs-vsctl add-br br-ex

# 查看
[root@gz-controller1 ~]# nmcli device
DEVICE          TYPE         STATE         CONNECTION     
brq497bf174-ea  bridge       连接（外部）  brq497bf174-ea 
brq54c80d26-f1  bridge       连接（外部）  brq54c80d26-f1 
lo              loopback     连接（外部）  lo             
brq05d9e583-db  bridge       连接（外部）  brq05d9e583-db 
eth0            ethernet     连接（外部）  eth0           
eth1.2          vlan         连接（外部）  eth1.2         
eth1            ethernet     未托管        --             
tap9db44907-f1  ethernet     未托管        --             
tapbb3ac461-a8  ethernet     未托管        --             
tapbfe54a50-6a  ethernet     未托管        --             
tapc28dbb91-3b  ethernet     未托管        --             
br-eth          openvswitch  未托管        --             
br-ex           openvswitch  未托管        --             
ovs-system      openvswitch  未托管        -- 

# 把 br-eth 网桥和虚拟机网络网卡 eth1 绑定、把 br-ex 网桥和专用的外部网卡 eth0 绑定
[root@gz-controller1 ~]# ovs-vsctl add-port br-eth eth1
[root@gz-controller1 ~]# ovs-vsctl add-port br-ex eth0
```



**dhcp agent配置文件修改**

```bash
# 将接口驱动替换为openvswitch
[root@gz-controller1 ~]# vim /etc/neutron/dhcp_agent.ini
[DEFAULT]
interface_driver = openvswitch
dhcp_driver = neutron.agent.linux.dhcp.Dnsmasq
enable_isolated_metadata = True
force_metadata = True
```



**metadata agent 配置文件修改**

正常情况下不需要修改 metadata agent 配置，因为里面保存的只是 nova metata 主机的IP地址和认证 secret 信息。



**L3 agent 配置修改**

```bash
[root@gz-controller1 /etc/neutron]# vim l3_agent.ini 
[default]
interface_driver = openvswitch
```



**服务配置**

然后重启其余的服务，命令是：

```bash
[root@gz-controller1 /etc/neutron]# systemctl restart neutron-server neutron-dhcp-agent neutron-metadata-agent neutron-l3-agent neutron-openvswitch-agent
```



#### 计算节点

**OVS 包安装和配置**

上文已经安装好了 OVS，接下来对配置文件进行编辑

```bash
[root@gz-computer1 ~]# vim /etc/neutron/plugins/ml2/openvswitch_agent.ini 
[ovs]
bridge_mappings = provider:br-eth

[securitygroup]
firewall_driver = iptables_hybrid:

# 添加 br-eth 网桥，并关联 eth1
[root@gz-computer1 ~]# ovs-vsctl add-br br-eth

# 删除网桥上的IP
[root@gz-computer1 ~]# ip addr flush dev brq497bf174-ea

# 解除绑定：
[root@gz-computer1 ~]# ip link set eth1 nomaster

# 删桥：
[root@gz-computer1 ~]# ip link set brq497bf174-ea down
[root@gz-computer1 ~]# brctl delbr brq497bf174-ea

# 把br-eth网桥和虚拟机网络网卡eth1绑定
[root@gz-computer1 ~]# ovs-vsctl add-port br-eth eth1

# 启动 OVS agent
[root@gz-computer1 ~]# systemctl enable neutron-openvswitch-agent

# 验证所有 agent 状态
[root@gz-controller1 ~]# openstack network agent list
+--------------------------------------+--------------------+-----------------------------+-------------------+-------+-------+---------------------------+
| ID                                   | Agent Type         | Host                        | Availability Zone | Alive | State | Binary                    |
+--------------------------------------+--------------------+-----------------------------+-------------------+-------+-------+---------------------------+
| 0b429046-1184-43fc-adb3-271d69323880 | Linux bridge agent | gz-controller1.mystical.org | None              | XXX   | UP    | neutron-linuxbridge-agent |
| 19521016-b7e7-4c6b-a0b0-194fc0266684 | L3 agent           | gz-controller1.mystical.org | nova              | :-)   | UP    | neutron-l3-agent          |
| 2e3081bb-f210-4c11-8b5f-3430b08fb758 | Metadata agent     | gz-controller1.mystical.org | None              | :-)   | UP    | neutron-metadata-agent    |
| 80bb0ec7-a216-4607-8cb1-09c2fa71ff22 | Linux bridge agent | gz-computer1.mystical.org   | None              | XXX   | UP    | neutron-linuxbridge-agent |
| 9e0aa906-8cd7-4fe1-85c2-f62d37032116 | Open vSwitch agent | gz-controller1.mystical.org | None              | :-)   | UP    | neutron-openvswitch-agent |
| ba655414-014a-43f9-9b6a-c81015a4da89 | DHCP agent         | gz-controller1.mystical.org | nova              | :-)   | UP    | neutron-dhcp-agent        |
| ed6e741a-dba2-4020-833d-d879ed30e860 | Open vSwitch agent | gz-computer1.mystical.org   | None              | :-)   | UP    | neutron-openvswitch-agent |
+--------------------------------------+--------------------+-----------------------------+-------------------+-------+-------+---------------------------+
```

可以看到除了linuxbridge agent以外，其他agent的Alive字段都是笑脸，说明配置正常。



#### 创建外部网络

![image-20260530002948880](D:\git_repository\cyber_security_learning\markdown_img\image-20260530002948880.png)

![image-20260530003019822](D:\git_repository\cyber_security_learning\markdown_img\image-20260530003019822.png)

![image-20260530003147080](D:\git_repository\cyber_security_learning\markdown_img\image-20260530003147080.png)

![image-20260530003205668](D:\git_repository\cyber_security_learning\markdown_img\image-20260530003205668.png)



#### 创建内网子网







# 存储服务 Ceph

## Ceph 发展简史

加州大学圣克鲁斯分校最早创建研究项目：

- 2004 年 Sage Weil 编写第一行代码；
- 2006 年，正式开源 Ceph 代码；
- 2010 年，Ceph 客户端工具合入内核；
- 2012 年，完成和 Openstack 的集成；
- 2014 年，红帽收购 Inktank；



## Ceph 存储使用场景

Ceph是一个开源的、高扩展性的软件定义存储，所谓的软件定义存储我理解的是由通用硬件组成，通 过软件来调整部署结构，可以提供多种访问接口，满足多种业务场景的存储产品。这种类别的产品可 以使用通用硬件，也就是普通x86架构服务器，甚至自己组装的电脑都可以。相对于传统的专业硬件产品，像硬件Raid、商业NAS、SAN存储等，在相同规格容量下它的成本大大下降。这也让它的应用场 景变得越来越广泛，甚至有很多公司基于Ceph开发出了自己的商业产品，例如XSKY，但是发展到现 在，商业产品和社区产品相比已经有了比较大的区别。 目前Ceph常见的应用场景主要有：

- 私有云平台存储，例如OpenStack和kubernetes上使用的块存储和对象存储等；
- 企业内部私有文件库，例如和网盘软件NextCloud、Seafile等结合，实现企业内部资料 存储和共享，一般用的是Ceph里的对象存储或者文件存储功能；
- 音视频、图片文件存储，常用的是Ceph里的对象存储；
- AI大模型存储，用于存储大模型所需的大量训练数据，一般是块存储或者对象存储。
- 大数据分析，例如安全公司用来存储病毒库、扫描样本等，一般是对象存储或者文件存 储；

可以看到，在实际的业务场景中，Ceph的使用还是非常广泛的。

> Ceph 生产中最少最少三个节点，一个数据三个副本，也就是如果我有60T的存储，能用的只有20T，考虑到通常85%-90%扩容，因此预计能用的也就18T



### 需要考虑的问题

Ceph的应用场景多种多样，但是在实际的生产上应用来说，还有很多实际的问题需要考虑。

最常见的问题就是它适合的公司规模，在实际的实践过程中，我们认为Ceph目前只适合于中大型公 司，对于小型公司来说，Ceph的配置、使用、维护等方面都不是特别友好。

首先从配置上来说，Ceph设计时就考虑是分布式架构的软件，因此它在生产上使用最少需要3台机器 才能搭建一个可以有效保障数据安全的集群。对于一台正规的生产服务器配上十来块大容量硬盘，单台成本都需要2万元以上。

其次，如果想要更好的性能，目前推荐的配置都需要万兆网卡、PCI-E接口的固态硬盘用作日志盘加 速。更别说在高性能场景中使用的全闪存固态硬盘配置，成本远远不是一般的小公司能够承受的。 最后，在实际使用时，你还需要额外准备一些用来替换的备件，便于在Ceph集群出估值时能够及时进行更换，对于经常维护Ceph集群的同学们来说，运行两年以上的Ceph集群，更换硬盘可以说是家常便饭。

因此在做资源评估时，需要考虑你们的业务场景是否需要这样大规模的集群，以及你们的业务是否能够满足这样的集群消耗。



## Ceph 集群架构简介



<img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260512113832184.png" alt="image-20260512113832184" style="zoom:150%;" />



可以简单划分为4个层次，分别是：

- 应用层，即实际使用Ceph存储的业务层，例如使用S3对象存储的各种web客户端、使用 块存储的虚拟机和容器，挂载CephFS当作存储盘使用的windows服务器等等；
- 接口层，即Ceph集群对外提供的调用接口，就是Ceph的3大存储接口：对象存储网关、RBD块存储和CephFS文件存储；
- RADOS层，向上提供对接接口层，向下对接存储组件，实现数据接收和分发的核心层，实际上由多种组件和规则构成，在后面会详细讲解。
- 存储层，由多台主机上的多个OSD组件构成，组合在一起形成一个超大的分布式存储。



### RADOS层的实现

上面说到RADOS层是Ceph集群业务层次中负责承上启下的核心层，它的实际实现机制如下所示：

<img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260512142021465.png" alt="image-20260512142021465" style="zoom:150%;" />

RADOS的全称是Reliable Autonomic Distributed Object Store，即可靠的自主分布式对象存储。这个层面实现的核心库主要用来操作Ceph集群里的对象，它是整个Ceph集群的基石。

在它的基础上开发出了librados库，提供了对外访问集群对象的接口，块存储和对象存储都是在 librados库的基础上开发出来的，客户端app或者其他需要使用对象存储和块存储的组件在把数据写入到对象存储网关或者块存储服务端时，都会调用底层的librados把对象文件或者块文件分割成4m一个 小文件，然后由RADOS存储到底层的OSD上。

 CephFS则是直接通过它自己的两个组件调用RADOS库，实现了普通文件到Ceph存储对象文件的转换，具体的转换细节在后面的存储服务中会详细讲解。



### 部署架构

生产上实际进行Ceph集群部署时，常用的部署架构如下所示：

<img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260512142435280.png" alt="image-20260512142435280" style="zoom:150%;" />

对于现在部署的小规模的集群来说（<100T），一般只有3-5个节点。每台节点上部署10-16块盘，每块盘10-16T容量，可以部署出一个100-250T容量范围的3副本集群。

MON、MGR、MDS、RGW都属于接口层的组件，OSD属于存储层的组件。对于小集群来说，MON、 MGR、MDS和RGW这些组件通常都是和OSD组件部署在一起，有足够的机器时才会分开部署来分散业务压力。

集群一般会使用2套网络，一套对外服务的网络，一套集群内部私有网络。集群内部私有网络用于各个节点之间的数据同步，而对外服务网络则是实际的业务流量经过的网络。对于现在的集群来说，在条件允许的情况下，两套网络尽量都使用万兆及以上的网络（10G+）。

主要原因在于现在的单块存储磁盘容量太大，假设单块磁盘只存储了8T数据，那么当这块盘的故障时，要把它上面的数据转移到其他节点上所需的时间就是8*1024G/1*3600 ≈ 2.28h，这个恢复时间对 于一个低频率使用的业务集群来说还可以接受，而如果是一个千兆网络，则所需的时间要提升一个数量级，远远超出了能够接受的范围。



### Ceph 版本号和名称对应关系

最近几个主要发行版的名称和版本对应关系如下：

 <img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260512142804963.png" alt="image-20260512142804963" style="zoom:150%;" />



Ceph的主版本大概是一年左右发一个大版本，每个大版本的维护时间是2年左右。Ceph社区的版本命 名策略是：x.y.z，x表示主版本号，y表示次版本号，z表示补丁版本号。通常y的值有0、1、2三个，代 表的含义是：

- 0，开发版本，类似其他软件里的alpha版本，主要给开发人员和早期测试人员使用，用 于早期测试；
- 1，候选版本，类似其他软件里的beta版本，给开发任意和测试任意搭建测试集群使 用；
- 2，稳定或者bug修复版本，可以给终端用户使用，部署在生产环境；

一般学习的时候我们会选择较新的LTS版本，例如本次课程文件整理的时候，较新的LTS版本是Reef 18.2.2版本。

因为后续要介绍的几个OpenStack主要组件都需要和Ceph集群对接，因此我们需要搭建一个用于测试 目的的Ceph集群，用来演示和OpenStack几大组件的对接，以及Ceph集群的学习。



## 前置条件

### 硬件条件

本次搭建我们准备3台2c4g的RockyLinux 9.2虚拟机，每台虚拟机除了系统盘50g以外，还单独配置了3 块100G的数据盘，整个集群的总容量是3*3*100g=900g的磁盘空间，用来和OpenStack集群进行对接使用。使用了两块网卡ens18和ens19，ens18配置了外网IP地址，用于提供Ceph集群对外访问接口。 ens19配置集群内部IP地址，用于Ceph集群内部通信。

首先安装好三台虚拟机，都使用最小化安装。我这边三台机器IP地址和主机名分别是：

- 10.2.100.220 rl-ceph1.mystical.com ceph1
- 10.2.100.221 rl-ceph2.mystical.com ceph2
- 10.2.100.222 rl-ceph3.mystical.com ceph3

将IP地址和主机名对应关系写到/etc/hosts文件里。

节点硬盘信息如下：

```bash
[root@rl-ceph1 ~]# lsblk
NAME              MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sr0                11:0    1  10.2G  0 rom  
nvme0n1           259:0    0   200G  0 disk 
├─nvme0n1p1       259:1    0     1G  0 part /boot
└─nvme0n1p2       259:2    0   199G  0 part 
  ├─rl_bogon-root 253:0    0    70G  0 lvm  /
  ├─rl_bogon-swap 253:1    0   3.9G  0 lvm  [SWAP]
  └─rl_bogon-home 253:2    0 125.1G  0 lvm  /home
nvme0n2           259:3    0   100G  0 disk 
nvme0n3           259:4    0   100G  0 disk 
nvme0n4           259:5    0   100G  0 disk
```

网卡配置如下：

- ceph1
  - eth0: 10.2.100.220
  - eth1: 192.168.23.134
- ceph2
  - eth0: 10.2.100.221
  - eth1: 192.168.23.135
- ceph3
  - eth0: 10.2.100.222
  - eth1: 192.168.23.136



### 软件条件

操作系统说明：本次搭建Ceph集群使用的是官方提供的cephadm工具，它也是一个容器化部署的工 具，因此它只要求操作系统上具备以下组件：

- Python3
- Systemd
- Podman 或者 Docker
- NTP 校时服务
- LVM2

因此使用CentOS8、CentOS9、RockyLinux8、RockyLinux9、Fedora系列发行版均可以正常部署，本 次测试集群使用的是RockLinux9.2.操作系统安装好后，完成以下基础配置：

- 关闭防火墙
- 关闭SELINUX
- 设置好主机名
- 配置好校时服务
- 安装好docker-ce



### cephadm命令配置

当前置条件都配置好了以后，就可以开始配置cephadm这个命令行工具了，在RockyLinux9上，自带了 Ceph的yum源，因此可以直接安装，我们本次安装的是Q版本的Ceph，对应的命令就是：

```bat
[root@rl-ceph1 ~]# dnf install centos-release-ceph-reef -y
[root@rl-ceph1 ~]# dnf install cephadm -y
[root@rl-ceph1 ~]# dnf install epel-release -y
[root@rl-ceph1 ~]# dnf install ceph-common -y
```

等命令执行完成后，cephadm和ceph命令行工具就安装好了，cephadm命令行工具是用来做Ceph集群 节点管理的，而ceph命令行工具是用来做集群内部组件和服务管理的。安装完成后，确认两者的版本 一样：

```bat
[root@rl-ceph1 ~]# ceph --version
ceph version 18.2.8 (efac5a54607c13fa50d4822e50242b86e6e446df) reef (stable)
[root@rl-ceph1 ~]# cephadm version
cephadm version 18.2.8 (efac5a54607c13fa50d4822e50242b86e6e446df) reef (stable)
```



## 集群配置

### 集群初始化

集群配置时，默认会先使用 cephadm bootstrap 命令初始化出第一个集群节点，然后在第一个集群节点 的基础上扩展出剩下的节点，完成整个集群的构建。初始化过程中cephadm会下载一个ceph的docker 镜像到本地，这个镜像比较大有1.2G，因此为了加快后续节点的启动和部署，可以直接下载我这边导 出的镜像直接导入到各个节点即可，这样初始化和后续节点的启动过程就会省掉镜像的下载流程。

初始化命令：

```bat
[root@rl-ceph1 ~]# cephadm --docker bootstrap --mon-ip 10.2.100.220 \
--allow-fqdn-hostname \
--cluster-network 192.168.23.0/24 \
--allow-overwrite
```

参数解释：

- `--docker`，使用docker作为底层存储引擎，默认是podman，注意这个参数是 `cephadm` 命令的参数；
- `--mon-ip` mon-ip通常指的是第一台机器的对外通信IP地址
- `--allow-fqdn-hostname`，当主机配置了完整主机名的时候需要这个参数，例如我们这里 的 `r1-ceph1.mystical.com`
- `--cluster-network 192.168.32.0/24`，设置集群内部组件通信的网络，后面一般是跟上一 个网段地址，程序会自动查找每个节点上对应网段的IP地址。
- `--allow-overwrite`，允许覆盖/etc/ceph目录下旧的配置；



这个命令会执行很多操作，包括：

- 在mon-ip机器上创建出新集群的一个monitor进程和mgr进程，即一个最小化集群所需的基本服务；
- 生成一对SSH密钥，把公钥写入root用户的~/.ssh/authorized_keys文件 和/etc/ceph/ceph.pub文件，方便传输到其他节点；
- 创建一个集群的最小化配置到/etc/ceph/ceph.conf文件中；
- 创建一个client.admin用户的管理密钥到/etc/ceph/ceph.client.admin.keyring文件中；
- 给第mon-ip指定的主机添加一个_admin标签，表示它是一个管理节点（通常只有管理节点才有ceph.conf和ceph.client.admin.keyring文件）

集群初始化完毕后，会提示你创建好了web访问地址和账号密码，示例如下：

```bat
Creating initial admin user...
Fetching dashboard port number...
Ceph Dashboard is now available at:

URL: https://rl-ceph1.mystical.com:8443/
User: admin
Password: 5f7zi4pkqj
```

还可以使用ceph -s命令查看集群的基本状态，正常示例如下：

```bat
[root@rl-ceph1 ~]# ceph -s
  cluster:
    id:     91a1bf62-4ddd-11f1-8646-0050562f55be
    health: HEALTH_WARN
            OSD count 0 < osd_pool_default_size 3
 
  services:
    mon: 2 daemons, quorum rl-ceph1,rl-ceph2 (age 5m)
    mgr: rl-ceph1.xbofcm(active, since 35m), standbys: rl-ceph2.ylkqld
    osd: 0 osds: 0 up, 0 in
 
  data:
    pools:   0 pools, 0 pgs
    objects: 0 objects, 0 B
    usage:   0 B used, 0 B / 0 B avail
    pgs:    
```

当前集群的状态因为只有一个节点，还不太正常。添加新节点让它变成一个正常工作的集群。 后面的节点添加和osd添加操作除了可以使用命令行进行外，也可以直接在web界面上添加。



### 添加新节点

cephadm工具和web界面的管理命令都是通过ssh远程到其他节点上去执行后续的步骤命令，因此我们 需要先配置好第一个节点到其他节点的免密登录：

```bash
cp /etc/ceph/ceph.pub /etc/ceph/.pub
ssh-copy-id -i /etc/ceph/ rl-ceph2.mystical.com
ssh-copy-id -i /etc/ceph/ rl-ceph3.mystical.com
```



#### 命令行添加

```bat
[root@rl-ceph1 ~]# ceph orch host add rl-ceph2.mystical.com 10.2.100.221
Added host 'rl-ceph2.mystical.com' with addr '192.168.100.221'
[root@rl-ceph1 ~]# ceph orch host ls
HOST                   ADDR             LABELS  STATUS  
rl-ceph1.mystical.com  192.168.100.220  _admin          
rl-ceph2.mystical.com  192.168.100.221                  
2 hosts in cluster
```

配置好免密登录后，继续后面的操作。

注意：

```bash
# 如果之前重新生成过新的 ceph 的ssh密钥对，集群内需要重新注册
[root@rl-ceph1 ~]# ceph config-key set mgr/cephadm/ssh_identity_key -i /etc/ceph/ceph
set mgr/cephadm/ssh_identity_key
[root@rl-ceph1 ~]# ceph config-key set mgr/cephadm/ssh_identity_pub -i /etc/ceph/ceph.pub
set mgr/cephadm/ssh_identity_pub
```





#### web界面添加

打开集群初始化完成后给出的登录地址，并输入账号密码登录

如果忘记密码，可以更新密码

```bash
[root@rl-ceph1 ~]# echo 'NewPassword123' > /tmp/ceph_pass
[root@rl-ceph1 ~]# ceph dashboard ac-user-set-password admin -i /tmp/ceph_pass
{"username": "admin", "password": "$2b$12$EfexWH.gQRShe5jkLklgAODfr2Y0E9bMpqO5VR7bXI0kWD4BFh2aG", "roles": ["administrator"], "name": null, "email": null, "lastUpdate": 1778585240, "enabled": true, "pwdExpirationDate": null, "pwdUpdateRequired": false}
```

登录后，会看到下面的页面：

```http
https://rl-ceph1.mystical.com:8443/
```

![image-20260512193359699](D:\git_repository\cyber_security_learning\markdown_img\image-20260512193359699.png)

输入第3台机器的主机名和IP地址，点击Add Host按钮添加主机，然后等它自动添加完成即可。如果发现它有自动添加一个_no_schedule标签，点击左上角的编辑按钮，把这个标签去掉。

```bat
# 查看ceph 状态，可以看到健康告警
# 因为 osd 数量少于集群最小数量
[root@rl-ceph1 ~]# ceph -s
  cluster:
    id:     91a1bf62-4ddd-11f1-8646-0050562f55be
    health: HEALTH_WARN
            OSD count 0 < osd_pool_default_size 3
 
  services:
    mon: 3 daemons, quorum rl-ceph1,rl-ceph2,rl-ceph3 (age 33m)
    mgr: rl-ceph1.xbofcm(active, since 3h), standbys: rl-ceph2.ylkqld
    osd: 0 osds: 0 up, 0 in
 
  data:
    pools:   0 pools, 0 pgs
    objects: 0 objects, 0 B
    usage:   0 B used, 0 B / 0 B avail
    pgs: 
```



## 添加osd

OSD就是实际负责数据存储的组件，在实际的生产环境中，通常就是我们的单个数据盘。我们的环境 中每个机器有3个数据盘，对应的盘符分别是sdb/sdc/sdd，我们使用ceph命令可以直接看到这些硬盘，如下所示：

```bat
[root@rl-ceph1 ~]# ceph orch device ls
HOST                   PATH          TYPE  DEVICE ID                                             SIZE  AVAILABLE  REFRESHED  REJECT REASONS    
rl-ceph1.mystical.com  /dev/nvme0n2  ssd   VMware_Virtual_NVMe_Disk_VMware_NVME_0000             100G  Yes        21m ago                      
rl-ceph1.mystical.com  /dev/nvme0n3  ssd   VMware_Virtual_NVMe_Disk_VMware_NVME_0000             100G  Yes        21m ago                      
rl-ceph1.mystical.com  /dev/nvme0n4  ssd   VMware_Virtual_NVMe_Disk_VMware_NVME_0000             100G  Yes        21m ago                      
rl-ceph1.mystical.com  /dev/sr0      hdd   VMware_Virtual_IDE_CDROM_Drive_10000000000000000001  10.1G  No         21m ago    Has a FileSystem  
rl-ceph2.mystical.com  /dev/nvme0n2  ssd   VMware_Virtual_NVMe_Disk_VMware_NVME_0000             100G  Yes        21m ago                      
rl-ceph2.mystical.com  /dev/nvme0n3  ssd   VMware_Virtual_NVMe_Disk_VMware_NVME_0000             100G  Yes        21m ago                      
rl-ceph2.mystical.com  /dev/nvme0n4  ssd   VMware_Virtual_NVMe_Disk_VMware_NVME_0000             100G  Yes        21m ago                      
rl-ceph2.mystical.com  /dev/sr0      hdd   VMware_Virtual_IDE_CDROM_Drive_10000000000000000001  10.1G  No         21m ago    Has a FileSystem  
rl-ceph3.mystical.com  /dev/nvme0n2  ssd   VMware_Virtual_NVMe_Disk_VMware_NVME_0000             100G  Yes        21m ago                      
rl-ceph3.mystical.com  /dev/nvme0n3  ssd   VMware_Virtual_NVMe_Disk_VMware_NVME_0000             100G  Yes        21m ago                      
rl-ceph3.mystical.com  /dev/nvme0n4  ssd   VMware_Virtual_NVMe_Disk_VMware_NVME_0000             100G  Yes        21m ago                      
rl-ceph3.mystical.com  /dev/sr0      hdd   VMware_Virtual_IDE_CDROM_Drive_10000000000000000001  10.1G  No         21m ago    Has a FileSystem  
```

把主机上的硬盘添加为集群中的OSD的命令是：

```bat
ceph orch apply osd --all-available-devices
```

这个命令会一次把所有的硬盘全部加入到集群中，比较适合硬盘比较多的情况，但是这个命令会因为 每个节点上程序执行速度的差异，导致OSD的编号完全混乱。因此在实际的生产中，为了方便管理起见，通常会按顺序添加，即按下面的命令依次执行：

```bat
[root@rl-ceph1 ~]# ceph orch daemon add osd rl-ceph1.mystical.com:/dev/nvme0n2
Created osd(s) 0 on host 'rl-ceph1.mystical.com'
[root@rl-ceph1 ~]# ceph orch daemon add osd rl-ceph1.mystical.com:/dev/nvme0n3
Created osd(s) 1 on host 'rl-ceph1.mystical.com'
[root@rl-ceph1 ~]# ceph orch daemon add osd rl-ceph1.mystical.com:/dev/nvme0n4
Created osd(s) 2 on host 'rl-ceph1.mystical.com'
[root@rl-ceph1 ~]# ceph orch daemon add osd rl-ceph2.mystical.com:/dev/nvme0n2
Created osd(s) 3 on host 'rl-ceph2.mystical.com'
[root@rl-ceph1 ~]# ceph orch daemon add osd rl-ceph2.mystical.com:/dev/nvme0n3
Created osd(s) 4 on host 'rl-ceph2.mystical.com'
[root@rl-ceph1 ~]# ceph orch daemon add osd rl-ceph2.mystical.com:/dev/nvme0n4
Created osd(s) 5 on host 'rl-ceph2.mystical.com'
[root@rl-ceph1 ~]# ceph orch daemon add osd rl-ceph3.mystical.com:/dev/nvme0n2
Created osd(s) 6 on host 'rl-ceph3.mystical.com'
[root@rl-ceph1 ~]# ceph orch daemon add osd rl-ceph3.mystical.com:/dev/nvme0n3
Created osd(s) 7 on host 'rl-ceph3.mystical.com'
[root@rl-ceph1 ~]# ceph orch daemon add osd rl-ceph3.mystical.com:/dev/nvme0n4
Created osd(s) 8 on host 'rl-ceph3.mystical.com'
```

```bash
# 如果之前机器上有旧集群，需要删除旧集群，zap旧的osd
# 在当前机器执行，仅能擦除当前机器的osd
[root@rl-ceph3 ~]# cephadm rm-cluster --force --zap-osds --fsid 91a1bf62-4ddd-11f1-8646-0050562f55be
Deleting cluster with fsid: 91a1bf62-4ddd-11f1-8646-0050562f55be
Using ceph image with id 'c7a6fb3e0c59' and tag '<none>' created on 2026-03-13 16:58:30 +0000 UTC
quay.io/ceph/ceph@sha256:239258a155b151a2190eb4b0795c8def30bb862af1f0c0513ea53f1a54d33a9d
Zapping /dev/nvme0n2...
Zapping /dev/nvme0n3...
Zapping /dev/nvme0n4...
```



这样添加的osd就会按照主机、磁盘的顺序依次编号，添加完毕后，查看集群状态，

```bat
[root@rl-ceph1 ~]# ceph -s
  cluster:
    id:     91a1bf62-4ddd-11f1-8646-0050562f55be
    health: HEALTH_OK
 
  services:
    mon: 3 daemons, quorum rl-ceph1,rl-ceph2,rl-ceph3 (age 76m)
    mgr: rl-ceph1.xbofcm(active, since 4h), standbys: rl-ceph2.ylkqld
    osd: 9 osds: 9 up (since 15m), 9 in (since 16m)
 
  data:
    pools:   1 pools, 1 pgs
    objects: 2 objects, 449 KiB
    usage:   243 MiB used, 900 GiB / 900 GiB avail
    pgs:     1 active+clean
```

确认是health_ok状态就可以执行后面的对接配置操作了。



## Ceph集群和OpenStack集群对接配置

Ceph集群搭建好以后，为了和OpenStack对接正常，我们需要在Ceph集群这边完成一些基础配置，包括：

- 存储池的创建，存储池名称和作用分别是
  - vms，Nova组件存放虚拟机系统盘；
  - volumes，Cinder组件存放虚拟机数据盘；
  - backups，Cinder-backup组件存放备份数据；
  - images，Glance组件存放镜像数据；
- 账号配置，Ceph集群连接时需要认证的keyring文件，因此我们需要把每个组件使用的认证账号和权限都配置好，需要创建的账号有：
  - client.cinder
  - client.cinder-backup
  - client.glance



### 创建存储池

创建4个存储池的命令分别是：

```bat
[root@rl-ceph1 ~]# ceph osd pool create volumes
pool 'volumes' created
[root@rl-ceph1 ~]# ceph osd pool create images
pool 'images' created
[root@rl-ceph1 ~]# ceph osd pool create backups
pool 'backups' created
[root@rl-ceph1 ~]# ceph osd pool create vms
pool 'vms' created
```

创建好了以后还有对存储池进行初始化，默认初始化为 **RBD 类型**的存储池：

```bat
[root@rl-ceph1 ~]# rbd pool init volumes
[root@rl-ceph1 ~]# rbd pool init images
[root@rl-ceph1 ~]# rbd pool init backups
[root@rl-ceph1 ~]# rbd pool init vms
```

初始化完毕后，配置所需的账号和权限。



### 账号权限配置

4个账号和相关联的存储池权限配置命令是：

```bat
# glance 用来访问镜像
[root@rl-ceph1 ~]#  ceph auth get-or-create client.glance mon 'profile rbd' osd 'profile rbd pool=images' mgr 'profile rbd pool=images'

# 这个返回的密钥匙是客户端和ceph集群通信使用的共享密钥
[client.glance]
        key = AQCSFhVqPYmVMBAAcLLzyeWsaLAu1ySh7lhA7g==

# cinder 用来存储数据盘
[root@rl-ceph1 ~]# ceph auth get-or-create client.cinder mon 'profile rbd' osd 'profile rbd pool=volumes, profile rbd pool=vms, profile rbd-read-only pool=images' mgr 'profile rbd pool=volumes, profile rbd pool=vms'
[client.cinder]
        key = AQDAFhVqP0SXHRAA67sChuGqAmVEYuhVWj7Lyg==

# cinder backup 做快照备份
[root@rl-ceph1 ~]# ceph auth get-or-create client.cinder-backup mon 'profile rbd' osd 'profile rbd pool=backups' mgr 'profile rbd pool=backups'
[client.cinder-backup]
        key = AQDbFhVqzPSaFhAA7Rx6bAOB/kF1/Ntkj8jZYw==

# nova，用来做nova的系统盘
[root@rl-ceph1 ~]# ceph auth get-or-create client.nova mon 'profile rbd' osd 'profile rbd pool=vms, profile rbd-read-only pool=images' mgr 'profile rbd pool=vms'
[client.nova]
        key = AQDiFhVqwAdwJRAARmSDuZQm5vdg0oF7Kg0zpw==
```

上述生成的共享密钥，后续会发到openstack集群，供Openstack集群使用



如果需要单独创建nova用户的账号，则命令是：

```bash
ceph auth get-or-create client.nova mon 'profile rbd' osd 'profile rbd pool=vms,
profile rbd-read-only pool=images' mgr 'profile rbd pool=vms'
```

查看创建好的账号信息：

```bash
[root@rl-ceph1 ~]# ceph auth list
```

示例输出账号信息如下所示：

```bash
......
client.glance
        key: AQAWMANqibNpChAAeFNtepMZtlaguBydZiyBoA==
        caps: [mgr] profile rbd pool=images
        caps: [mon] profile rbd
        caps: [osd] profile rbd pool=images
client.nova
        key: AQBWMANqyP/6AhAAgYTIVpQgX8dztIYq10mVPg==
        caps: [mgr] profile rbd pool=vms
        caps: [mon] profile rbd
        caps: [osd] profile rbd pool=vms, profile rbd-read-only pool=images
......
```

将账号认证信息导出为keyring文件：

```bash
[root@rl-ceph1 ~]# ceph auth get-or-create client.glance | sudo tee /etc/ceph/ceph.client.glance.keyring
[client.glance]
        key = AQCSFhVqPYmVMBAAcLLzyeWsaLAu1ySh7lhA7g==
[root@rl-ceph1 ~]# ceph auth get-or-create client.cinder | sudo tee /etc/ceph/ceph.client.cinder.keyring
[client.cinder]
        key = AQDAFhVqP0SXHRAA67sChuGqAmVEYuhVWj7Lyg==
[root@rl-ceph1 ~]# ceph auth get-or-create client.nova | sudo tee /etc/ceph/ceph.client.nova.keyring
[client.nova]
        key = AQDiFhVqwAdwJRAARmSDuZQm5vdg0oF7Kg0zpw==
[root@rl-ceph1 ~]# ceph auth get-or-create client.cinder-backup | sudo tee /etc/ceph/ceph.client.cinderbackup.keyring
[client.cinder-backup]
        key = AQDbFhVqzPSaFhAA7Rx6bAOB/kF1/Ntkj8jZYw==
```

这3个命令执行完毕后，就会把client.glance、client.cinder和client.cinder-backup用户的认证文件保存 到/etc/ceph目录下，如下所示：

```bash
[root@rl-ceph1 ~]# ls /etc/ceph
ceph.client.admin.keyring         ceph.client.glance.keyring  ceph.pub
ceph.client.cinderbackup.keyring  ceph.client.nova.keyring    rbdmap
ceph.client.cinder.keyring        ceph.conf
```

然后就可以把这4个keyring文件上传到需要用到它的OpenStack节点上。

```bash
[root@rl-ceph1 ~]# scp /etc/ceph/ceph.conf 10.2.100.200:~/
root@10.2.100.200's password: 
ceph.conf                                             100%  271    86.0KB/s   00:00  
[root@rl-ceph1 ~]# scp /etc/ceph/ceph.*.keyring 10.2.100.200:~/
root@10.2.100.200's password: 
# 生产中 admin.keyring这个文件不要传过去，因为admin权限很高，可以操作整个集群，不安全
ceph.client.admin.keyring                   100%  151    44.7KB/s   00:00    
ceph.client.cinderbackup.keyring            100%   71    21.0KB/s   00:00    
ceph.client.cinder.keyring                  100%   64    26.8KB/s   00:00    
ceph.client.glance.keyring                  100%   64    21.8KB/s   00:00    
ceph.client.nova.keyring                    100%   62    22.0KB/s   00:00 

# 查看 ceph.client.admin.keyring 
[root@rl-ceph1 ~]# cat /etc/ceph/ceph.client.admin.keyring 
[client.admin]
        key = AQBA9BRqVoPUJhAAan2F/wZYtXPuthcffZkUCw==
        caps mds = "allow *"
        caps mgr = "allow *"
        caps mon = "allow *"
        caps osd = "allow *"
        
# 查看当前创建好的存储池
[root@rl-ceph1 ~]# ceph osd pool ls
.mgr
volumes
images
backups
vms
```

> 对于存储数据的集群来说，授权一定要谨慎！！！
>
> 支持和 Openstack 对接的操作就完成了，总结：1. 创建并初始化存储池，2.创建账号权限配置





## Ceph 集群认证

### cephx认证开关

Ceph集群认证使用的是cephx协议，对应的认证开关是在/etc/ceph/ceph.conf文件中，示例文件内容如下所示：

```ini
[global]
fsid = 5beba824-df4a-43fc-b87c-1048d1bceb23
mon_initial_members = ceph01, ceph02, ceph03
mon_host = 192.168.21.160,192.168.21.161,192.168.21.162
# 下面是默认值，正常是缺省
auth_cluster_required = cephx
auth_service_required = cephx
auth_client_required = cephx
```

如果要禁用它，需要设置：

```ini
auth_cluster_required = none
auth_service_required = none
auth_client_required = none
```

修改完成后重启集群组件让配置生效，一般情况下建议不要随便禁用。当开关打开了以后，就可以使用ceph自带的认证和鉴权子系统了。



### cephx认证类型

哪些场景下会需要用到 Ceph 的认证和鉴权？主要有下面这些场景：

- 使用命令行和Ceph集群交互
- 使用客户端和Ceph集群交互

这些场景中都必须带上认证和鉴权相关的信息。

默认使用一个包含 sercret key 的 keyring（共享密钥）文件，集群搭建好以后，第一次执行的命令一般都是：

```bat
[root@rl-ceph1 ~]# ceph -s
  cluster:
    id:     91a1bf62-4ddd-11f1-8646-0050562f55be
    health: HEALTH_OK
 
  services:
    mon: 3 daemons, quorum rl-ceph1,rl-ceph2,rl-ceph3 (age 2h)
    mgr: rl-ceph1.xbofcm(active, since 5h), standbys: rl-ceph2.ylkqld
    osd: 9 osds: 9 up (since 105m), 9 in (since 105m)
 
  data:
    pools:   5 pools, 129 pgs
    objects: 10 objects, 449 KiB
    usage:   256 MiB used, 900 GiB / 900 GiB avail
    pgs:     129 active+clean
```

来查看Ceph集群的状态，它在后端实际上执行的命令是：

```bat
# 这里 ceph -s 省略了 -n client.admin --keyring=/etc/ceph/ceph.client.admin.keyring
[root@rl-ceph1 ~]# ceph -n client.admin --keyring=/etc/ceph/ceph.client.admin.keyring -s  cluster:
    id:     91a1bf62-4ddd-11f1-8646-0050562f55be
    health: HEALTH_OK
 
  services:
    mon: 3 daemons, quorum rl-ceph1,rl-ceph2,rl-ceph3 (age 2h)
    mgr: rl-ceph1.xbofcm(active, since 5h), standbys: rl-ceph2.ylkqld
    osd: 9 osds: 9 up (since 105m), 9 in (since 105m)
 
  data:
    pools:   5 pools, 129 pgs
    objects: 10 objects, 449 KiB
    usage:   256 MiB used, 900 GiB / 900 GiB avail
    pgs:     129 active+clean
```

默认使用用户 `client.admin` 和 `/etc/ceph/` 下的`ceph.client.admin.keyring` 文件。

而Ceph中使用到用户认证的位置主要场景有：

- Ceph集群内外部交互，使用**`cephx认证`**；
- RGW对象网关认证，**`对象网关自带认证系统` 和 `cephx结合授权`**；
- CephFS用户认证，**`文件系统路径` + `cephx结合授权`**；

cephx认证和鉴权是最基本的功能，后面两种场景需要结合实际应用来组合授权，因此我们先来了解 cephx 认证和鉴权，熟悉了以后再去学习后面两种场景。



### CephX里至少有三类 “密钥”

#### 第一种：Client Secret（长期共享密钥）

例如：

```ABAP
ceph auth get client.admin
```

看到：

```ini
[client.admin]
key = AQBxxxxx==
```

这个：

```ABAP
就是 client.admin 的长期 secret key
```

它保存在：

- MON auth DB
- 客户端 keyring

双方都有



#### 第二种：Service Secret（服务密钥）

Service Secret 是 CephX 内部用于服务认证与 ticket 签发/校验的长期共享密钥，由 Ceph 认证体系维护，供 MON、OSD、MDS 等服务使用。

该服务密钥由 MON 主导管理，是 Ceph 内部服务间（OSD、MON、MDS）共享的secret

主要作用：“签发 ticket 的依据”



#### 第三种：session key

在客户端和 Ceph 内部组件（例如：OSD）认证成功后，客户端和 OSD 之间

```ABAP
不会一直用长期secret
```

否则：

```ABAP
长期密钥泄漏风险大
```

所以：

```ABAP
MON 会生成临时 session key
```

用于：

```ABAP
后续消息签名/加密
```



### ceph集群认证流程

#### 第一阶段：客户端认证

**第一步：客户端发起认证**

客户端：

```ABAP
我是 client.admin
```

发送：

```ABAP
entity name
supported auth methods
```

给 MON。

**第二步：MON 返回 challenge**

MON:

```ABAP
证明你真有 secret key
```

发送：

```ABAP
随机 challenge
```

**第三步：客户端使用 secret key 计算响应**

客户端本地：

```ABAP
使用 keyring 中的 secret key
```

对 challenge 做：

```ABAP
HMAC/hash
```

返回给 MON。

注意：

```ABAP
真正的 secret key 不会直接发送
```

**第四步：MON 校验**

MON 本地也保存：

```ABAP
client.admin 的 secret key
```

MON：

```ABAP
自己计算 challenge 的hash
```

如果一致：

```ABAP
说明客户端确实拥有 secret key
```

认证通过。



#### 第二阶段：MON生成 session key

例如：

```ABAP
SK = abc123
```



#### 第三阶段：MON做两件事

**第五步：将 session key 发给客户端**

```ABAP
使用 client secret 加密：
这里是 SK
```

客户端：

```ABAP
解密得到 SK
```

**第六步：MON 将包含 session key 的 ticket 返回给客户端”**

ticket 内：

```ABAP
client=client.admin
caps=...
session_key=abc123
expire=...
```

ticket：

```ABAP
ticket 使用 service secret 进行签名或认证保护，使 OSD/MDS 能验证 ticket 确实由 MON 签发。
```



#### 第四阶段：客户端访问 OSD

客户端：

```ABAP
这是我的 ticket
```

OSD：

```ABAP
验证 ticket
```

验证通过：

```ABAP
从 ticket 中取出 session key
```

于是：

```ABAP
OSD 也知道了 abc123
```



**最终**

Client 和 OSD 通过 MON 安全协商了共同 Session key，后续客户端使用 Session Key 和 OSD 进行通信。

![image-20260512234908944](D:\git_repository\cyber_security_learning\markdown_img\image-20260512234908944.png)

### ceph 用户配置和管理

从上面的流程中可以看出，cephx认证是**基于用户**来实现的。在Ceph中基于用户认证，需要先在集群中创建一个用户，然后给该用户授予特定的权限或者所有的权限，然后该用户才能执行相应的操作， 例如连接集群，读取或写入数据等。因此要了解cephx认证，我们就需要先学习ceph集群的用户管理。 用户管理功能是Ceph集群管理员具备的能力，一般就是admin用户才有权限进行这个操作，包括用户的创建、更新和删除。



#### 用户查看

在Ceph集群中的用户不单单指实际的**运维人员**，还包括**集群组件**和**Ceph客户端**。会为每一个实际用户、组件或客户端配置一个单独的认证帐号，然后给每个帐号关联集群中不同组件的权限。 查看集群内部所有认证用户的命令是

```bat
[root@rl-ceph1 ~]# ceph auth ls
osd.0
        key: AQCzHQNq0di/DRAADA0Y/SipM1HQSvqkBiRSug==
        caps: [mgr] allow profile osd
        caps: [mon] allow profile osd
        caps: [osd] allow *
osd.1
        key: AQDKHQNqaFekAxAArH74xUdzCDWh/P9dPIFomA==
        caps: [mgr] allow profile osd
        caps: [mon] allow profile osd
        caps: [osd] allow *
......
```

在上面的示例输出中，有多种类型的用户，例如：

- `osd.0`，表示 `osd` 组件用户；
- `client.admin`，表示客户端用户；
- `client.bootstrap-*`，表示初始化集群时使用的用户；
- `client.ceph-exporter.*`，`client.crash.*`，`mgr` 里管理的不同模块使用的用户；
- `mgr.*`，表示 `mgr` 组件用户；

总体上来说，集群里的用户分为2类，分别是：

- **组件用户**，直接以组件类型开头的，例如 `osd.1`，`mgr.node1`，是组件用来和集群内其他 组件进行交互的用户。
- **客户端用户**，以 `client.xxx` 格式命名的用户。一般是用于客户端连接集群或运维人员用来管理集群时使用。

从上面还可以看到，每个用户都有一个key，这个就是共享密钥。每个用户上还配置了不同的caps，对应的就是不同的权限这个后面会详细讲解。



#### 获取单个用户信息

获取当用户信息使用命令格式是：

```bat
ceph auth get TYPE.ID
ceph auth export TYPE.ID
```

TYPE表示的是用户类型，例如cient、osd、mgr等，ID指的是组件的编号或者用户的名称。

使用示例如下：

```bat
[root@rl-ceph1 ~]# ceph auth get client.admin
[client.admin]
        key = AQCg5gJq9+PTORAAxaC30XrVjjtcmgq270Nsmw==
        caps mds = "allow *"
        caps mgr = "allow *"
        caps mon = "allow *"
        caps osd = "allow *"
```



#### 添加用户

添加一个用户操作会创建下面3个信息：

- **用户名**，格式是TYPE.ID，例如client.user
- **secret key**，用户的密钥，用来连接集群时用于认证
- **权限信息**，里面配置的是不同组件的权限；

目前有多个命令都可以用来添加用户，包括：

- `ceph auth add`，**最标准的添加用户方式**，会生成上面所说的3个信息，如果用户已存在时会报错
- `ceph auth get-or-create`，**最方便创建用户的方式**，会返回格式化后包含用户名称、key 的keyring文件信息，可以使用-o filename选项将返回信息保存为keyring文件
- `ceph auth get-or-create-key`，这是最方便创建用户并返回key（只有key）的命令，这个 命令可以用来创建客户端认证使用的secret文件。使用-o filename选项将结果保存为 secret文件。



创建用户时的一些基本规则：

- 至少有 `monitor` 的读权限
- 至少有 `OSD` 的读写和执行权限，才能查看 `pool` 里的数据以及向 `pool` 里写入数据
- `OSD` 的权限限制在某个**特定的 `pool`**，不限制用户能够访问的 `pool`，用户会具有 `OSD` 上所有 `pool` 的访问权限。

创建用户示例如下：

```bash
ceph auth add client.john mon 'allow r' osd 'allow r pool=liverpool'
ceph auth get-or-create client.paul mon 'allow r' osd 'allow r pool=liverpool'

# client.afei可以读取并向存储池vms中写入数据
ceph auth get-or-create client.afei mon 'allow r' osd 'allow rwx pool=vmx'

# 创建用户george并把认证信息保存在keyring文件中
ceph auth get-or-create client.george mon 'allow r' osd 'allow rw pool=liverpool' -o 
george.keyring
ceph auth get-or-create-key client.ringo mon 'allow r' osd 'allow rw pool=liverpool' 
o ringo.key
```

示例：

```bash
[root@rl-ceph1 /etc/ceph]# ceph auth get-or-create client.afei mon 'profile rbd' osd 'profile rbd pool=vms' -o /etc/ceph/ceph.client.afei.keyring
[root@rl-ceph1 /etc/ceph]# ll
总用量 40
-rw------- 1 root root 419  5月 26 09:37 ceph
-rw------- 1 root root 151  5月 26 09:51 ceph.client.admin.keyring
-rw-r--r-- 1 root root  62  5月 26 14:57 ceph.client.afei.keyring
-rw-r--r-- 1 root root  71  5月 26 11:54 ceph.client.cinderbackup.keyring
-rw-r--r-- 1 root root  64  5月 26 11:53 ceph.client.cinder.keyring
-rw-r--r-- 1 root root  64  5月 26 11:53 ceph.client.glance.keyring
-rw-r--r-- 1 root root  62  5月 26 11:53 ceph.client.nova.keyring
-rw-r--r-- 1 root root 271  5月 26 09:57 ceph.conf
-rw-r--r-- 1 root root 108  5月 26 09:37 ceph.pub
-rw-r--r-- 1 root root  92  3月 24 00:28 rbdmap

[root@rl-ceph1 /etc/ceph]# cat ceph.client.afei.keyring 
[client.afei]
        key = AQADRBVqSNi9EhAAZjy6QuSF2W/vRfq03TZShg==
        
[root@rl-ceph1 /etc/ceph]# rbd -p vms -n client.afei create demo-img --size 1024

# 查看image
[root@rl-ceph1 /etc/ceph]# rbd ls vms
demo-img

# 查看详细信息
[root@rl-ceph1 /etc/ceph]# rbd info vms/demo-img
rbd image 'demo-img':
        size 1 GiB in 256 objects
        order 22 (4 MiB objects)
        snapshot_count: 0
        id: 39e489952d95
        block_name_prefix: rbd_data.39e489952d95
        format: 2
        features: layering, exclusive-lock, object-map, fast-diff, deep-flatten
        op_features: 
        flags: 
        create_timestamp: Tue May 26 14:58:09 2026
        access_timestamp: Tue May 26 14:58:09 2026
        modify_timestamp: Tue May 26 14:58:09 2026
```





#### 删除用户

删除用户使用子命令：

```bash
ceph auth rm/del TYPE.ID
```

示例如下：

```bash
ceph auth rm/del client.user
```



#### 打印用户Key

使用子命令

```bash
ceph auth print-key {TYPE}.{ID}
```

如下所示：

```bash
[root@rl-ceph1 ~]# ceph auth print-key client.admin
AQBA9BRqVoPUJhAAan2F/wZYtXPuthcffZkUCw==
```

例如在挂载文件系统的时候需要使用key，那么就可以使用这个命令来避免暴露key到bash的历史记录 中，示例如下所示：

```bash
# “使用 CephX 用户认证，把 CephFS 挂载到 Linux”
# mount -t ceph ：挂载一个 Ceph 文件系统（CephFS），即文件系统类型 = ceph
# serverhost:/ ：Ceph MON 地址 + CephFS 根目录
# mountpoint：挂载到本地哪个目录 eg：/mnt/cephfs
# -o：使用哪个 CephX 用户认证，name=client.user中client可以不写，内核客户端会自动补全
mount -t ceph serverhost:/ mountpoint -o name=client.user,secret=`ceph auth print-key client.user`
mount -t ceph serverhost:/ mountpoint -o name=client.user,secretfile=/etc/ceph/client.user

# 示例：
mount -t ceph \
10.0.0.11:6789:/ \
/mnt/cephfs \
-o name=admin,secretfile=/etc/ceph/admin.secret
```





### ceph 权限配置和管理

下面我们来介绍用户权限的格式，以及认证权限信息的配置流程。\

#### caps 详解

在权限信息里我们看到，有多行caps开头的权限信息，caps是capabilities的缩写，即拥有的能力。这 个字段里定义的是用户到mon、osd、mgr、mds这些集群核心组件的访问能力。还可以定义对资源池 的访问能力。这个字段的定义基本格式是：

```bash
caps {daemon-type} = '{cap-spec}[, {cap-spec} ...]'

# daemon-type，即组件的类型，不同组件类型后面的cap-spec对应的值也不一样。集群内目前可以配置的组件类型有：mon、osd、mgr、mds

# mon：指的是对monitor组件的访问权限。对于mon，有两种配置格式：
# mon 'allow {access-spec} [network {network/prefix}]' （格式1）
# mon 'allow profile {name}'（格式2）

# 第一种格式里 access-spec 是允许哪些权限，network是用来限制哪些客户端能够访问。参数解释如下：
# access-spec，允许的权限，对应的值有：
# * | all | r | w | x，
# *和all表示所有权限，rwx分别表示可读、可写和可执行权限。对于 mon，一般是 * 或 r

# network [network/prefix]，表示通过ip或网段来限制，例如
# network 192.168.1.120，表示只允许这个用户通过192.168.1.120来访问monitor，通过这种方式可以限制客户端的来源。
# network 192.168.1.0/24，表示只允许这个用户通过192.168.1.0/24这个网段来访问。

# 第二种格式是使用默认的模板来配置权限
# profile 宏并不是“配置文件里的对象”，而是 Ceph 源码内部硬编码（hardcode）的 capability 模板
# 因此不支持查看，修改和自定义，只能通过查看源码和修改源码的方式更改内置的权限宏。

# -------------------------------------------------------------------------------------------------------------------------

# osd：指的是针对osd进程的访问权限，对于osd，也有两种配置格式：
# osd 'allow {access-spec} [{match-spec}] [network {network/prefix}]'
# osd 'profile {name} [pool={pool-name} [namespace={namespace-name}]] [network {network/prefix}]

# 第一种格式是允许对osd进程的读写等权限，可以通过network来限制客户端访问。参数解释如下：
# access-spec，允许的权限，对应的值有：
# * | all | [r][w][x]，osd级别限制
# [class-read] [class-write]， 是class操作类型限制，即在class上只能进行读、写操作。
# class-read，给用户调用类读取方法的能力，x的子集
# class-write，给用户调用类写入方法的能力，x的子集
# 后续记得补充

# 示例：
[osd.0]
        key = AQBC/xRqL25sHRAAZJn82eLEaNz1WGGbix2hrg==
        caps mgr = "allow profile osd"
        caps mon = "allow profile osd"
        caps osd = "allow *"
```

ceph 内置 capability 宏（即内置“标准权限模板”）

```http
https://docs.ceph.com/en/latest/rados/operations/user-management/?utm_source=chatgpt.com#profile-capabilities
```



#### 修改用户权限

修改用户权限使用的子命令是：

```ABAP
ceph auth caps
```

设置了新权限，就会覆盖旧的权限。要查看当前的权限可以使用上面介绍的获取用户信息命令ceph auth get，要添加权限，那么你也必须指定目前已有的权限。格式如下：

```bash
ceph auth caps USERTYPE.USERID 
    {daemon} 'allow [r|w|x|*|...] [pool={pool-name}] [namespace={namespace-name}]' \
    [{daemon} 'allow [r|w|x|*|...] [pool={pool-name}] [namespace={namespace-name}]']
```

示例如下：

```bash
ceph auth get client.john
ceph auth caps client.john mon 'allow r' osd 'allow rw pool=liverpool'
ceph auth caps client.paul mon 'allow rw' osd 'allow rwx pool=liverpool'
ceph auth caps client.brian-manager mon 'allow *' osd 'allow *'
```



#### 多用户keyring文件管理







## Ceph 组件介绍

### Monitor 节点

Monitor节点上会运行着一个 ceph-mon 进程，这个进程负责维护 cluster map，map里面包含整个集群的拓扑图。因此客户端只需要连接到任意一个Monitor节点就能够知道整个集群的架构，包括每个节点的信息。

在monitor节点上保存着每个组件的map，包括OSD map、MON map、MDS map、PG map和 CRUSH map等，这些map合在一起被统称为Cluster Map，Monitor节点并不保存实际的业务数据。 查看各种map的命令：

```bash
ceph mon dump
ceph osd dump
ceph pg dump
ceph mgr dump
ceph mds dump
ceph osd getcrushmap -o crushmap                # 从集群中导出编码后的crushmap信息
crushtool -d clushmap -o decrushmap.txt         # 把crushmap文件文件解码为普通的txt文件
```

示例：

```bash
# mon dump
[root@rl-ceph1 /etc/ceph]# ceph mon dump
epoch 3                                                             # 版本
fsid 67c41f82-58a0-11f1-9541-0050562f55be                           # 集群id
last_changed 2026-05-26T01:56:31.306287+0000                        # 最后一次变更时间
created 2026-05-26T01:15:46.399373+0000                             # 集群创建时间
min_mon_release 18 (reef)                                           # ceph 版本
election_strategy: 1
0: [v2:10.2.100.220:3300/0,v1:10.2.100.220:6789/0] mon.rl-ceph1     # 通信端口
1: [v2:10.2.100.221:3300/0,v1:10.2.100.221:6789/0] mon.rl-ceph2
2: [v2:10.2.100.222:3300/0,v1:10.2.100.222:6789/0] mon.rl-ceph3
dumped monmap epoch 3

# osd dump
[root@rl-ceph1 /etc/ceph]# ceph osd dump
epoch 98
fsid 67c41f82-58a0-11f1-9541-0050562f55be
created 2026-05-26T01:15:52.058907+0000
modified 2026-05-26T03:40:03.486553+0000
flags sortbitwise,recovery_deletes,purged_snapdirs,pglog_hardlimit
crush_version 19
# ceph 维护常看的信息（磁盘告警）
full_ratio 0.95                             
backfillfull_ratio 0.9
nearfull_ratio 0.85
require_min_compat_client luminous
min_compat_client luminous
require_osd_release reef
stretch_mode_enabled false
pool 1 '.mgr' replicated size 3 min_size 2 crush_rule 0 object_hash rjenkins pg_num 1 pgp_num 1 autoscale_mode on last_change 22 flags hashpspool stripe_width 0 pg_num_max 32 pg_num_min 1 application mgr read_balance_score 9.09
pool 2 'volumes' replicated size 3 min_size 2 crush_rule 0 object_hash rjenkins pg_num 32 pgp_num 32 autoscale_mode on last_change 84 lfor 0/0/76 flags hashpspool,selfmanaged_snaps stripe_width 0 application rbd read_balance_score 1.69
pool 3 'images' replicated size 3 min_size 2 crush_rule 0 object_hash rjenkins pg_num 32 pgp_num 32 autoscale_mode on last_change 90 lfor 0/0/76 flags hashpspool,selfmanaged_snaps stripe_width 0 application rbd read_balance_score 1.69pool 4 'backups' replicated size 3 min_size 2 crush_rule 0 object_hash rjenkins pg_num 32 pgp_num 32 autoscale_mode on last_change 94 lfor 0/0/78 flags hashpspool,selfmanaged_snaps stripe_width 0 application rbd read_balance_score 1.41
pool 5 'vms' replicated size 3 min_size 2 crush_rule 0 object_hash rjenkins pg_num 32 pgp_num 32 autoscale_mode on last_change 97 lfor 0/0/78 flags hashpspool,selfmanaged_snaps stripe_width 0 application rbd read_balance_score 1.69
max_osd 9
osd.0 up   in  weight 1 up_from 9 up_thru 80 down_at 0 last_clean_interval [0,0) [v2:10.2.100.220:6800/2225215016,v1:10.2.100.220:6801/2225215016] [v2:192.168.23.154:6800/2225215016,v1:192.168.23.154:6801/2225215016] exists,up 0c1c19f4-a613-4c18-a9f1-c2b8686dbddb
osd.1 up   in  weight 1 up_from 14 up_thru 86 down_at 0 last_clean_interval [0,0) [v2:10.2.100.220:6804/1850992905,v1:10.2.100.220:6805/1850992905] [v2:192.168.23.154:6804/1850992905,v1:192.168.23.154:6805/1850992905] exists,up 22b1e278-9367-42fc-a720-da13a4c9292d
osd.2 up   in  weight 1 up_from 19 up_thru 86 down_at 0 last_clean_interval [0,0) [v2:10.2.100.220:6808/3851126219,v1:10.2.100.220:6809/3851126219] [v2:192.168.23.154:6808/3851126219,v1:192.168.23.154:6809/3851126219] exists,up cfc4980e-0216-4f76-92a1-332069bb8de7
osd.3 up   in  weight 1 up_from 26 up_thru 80 down_at 0 last_clean_interval [0,0) [v2:10.2.100.221:6802/2976503068,v1:10.2.100.221:6803/2976503068] [v2:192.168.23.155:6800/2976503068,v1:192.168.23.155:6801/2976503068] exists,up 0a70ab75-f6aa-4491-9f1e-dbd99454704f
osd.4 up   in  weight 1 up_from 34 up_thru 80 down_at 0 last_clean_interval [0,0) [v2:10.2.100.221:6806/847166279,v1:10.2.100.221:6807/847166279] [v2:192.168.23.155:6804/847166279,v1:192.168.23.155:6805/847166279] exists,up 29999eec-585a-4234-84d5-af49eee575b4
osd.5 up   in  weight 1 up_from 39 up_thru 80 down_at 0 last_clean_interval [0,0) [v2:10.2.100.221:6810/1071284141,v1:10.2.100.221:6811/1071284141] [v2:192.168.23.155:6808/1071284141,v1:192.168.23.155:6809/1071284141] exists,up 4f6631e9-6dac-4465-a4bc-0d7f070fc45f
osd.6 up   in  weight 1 up_from 46 up_thru 86 down_at 0 last_clean_interval [0,0) [v2:10.2.100.222:6800/3163201805,v1:10.2.100.222:6801/3163201805] [v2:192.168.23.156:6800/3163201805,v1:192.168.23.156:6801/3163201805] exists,up 4763657a-b3c7-4dac-a7d4-0ffc08ebb56e
osd.7 up   in  weight 1 up_from 54 up_thru 80 down_at 0 last_clean_interval [0,0) [v2:10.2.100.222:6804/2791226569,v1:10.2.100.222:6805/2791226569] [v2:192.168.23.156:6804/2791226569,v1:192.168.23.156:6805/2791226569] exists,up 0ef88062-5430-43ec-8b86-523888a98552
osd.8 up   in  weight 1 up_from 60 up_thru 86 down_at 0 last_clean_interval [0,0) [v2:10.2.100.222:6808/4277774054,v1:10.2.100.222:6809/4277774054] [v2:192.168.23.156:6808/4277774054,v1:192.168.23.156:6809/4277774054] exists,up 33c304da-7414-44ec-8a8e-90bd052028fc
pg_upmap_items 4.7 [1,2]
pg_upmap_items 4.9 [6,8]
pg_upmap_items 4.f [1,2]
pg_upmap_items 4.10 [6,7]
pg_upmap_items 4.14 [1,2]
pg_upmap_items 4.1c [1,2]
pg_upmap_items 4.1f [6,8]
blocklist 10.2.100.220:0/3602759610 expires 2026-05-27T01:51:30.361091+0000
blocklist 10.2.100.220:6801/2386278797 expires 2026-05-27T01:51:30.361091+0000blocklist 10.2.100.220:6800/2386278797 expires 2026-05-27T01:51:30.361091+0000blocklist 10.2.100.220:0/426896390 expires 2026-05-27T01:51:30.361091+0000
blocklist 10.2.100.220:6801/1553684386 expires 2026-05-27T01:19:52.766332+0000blocklist 10.2.100.220:6800/1553684386 expires 2026-05-27T01:19:52.766332+0000blocklist 10.2.100.220:6801/1449263673 expires 2026-05-27T01:18:29.553533+0000blocklist 10.2.100.220:0/694715175 expires 2026-05-27T01:19:52.766332+0000
blocklist 10.2.100.220:6801/1005904402 expires 2026-05-27T01:17:12.510347+0000blocklist 10.2.100.220:0/676695144 expires 2026-05-27T01:17:12.510347+0000
blocklist 10.2.100.220:0/2492596507 expires 2026-05-27T01:18:29.553533+0000
blocklist 10.2.100.220:6800/1005904402 expires 2026-05-27T01:17:12.510347+0000blocklist 10.2.100.220:0/3238812792 expires 2026-05-27T01:17:12.510347+0000
blocklist 10.2.100.220:0/2809494165 expires 2026-05-27T01:17:12.510347+0000
blocklist 10.2.100.220:6800/1449263673 expires 2026-05-27T01:18:29.553533+0000blocklist 10.2.100.220:0/3618146719 expires 2026-05-27T01:19:52.766332+0000
blocklist 10.2.100.220:0/3454032269 expires 2026-05-27T01:18:29.553533+0000
blocklist 10.2.100.220:0/1793604516 expires 2026-05-27T01:51:30.361091+0000
blocklist 10.2.100.220:0/2527633849 expires 2026-05-27T01:18:29.553533+0000
blocklist 10.2.100.220:0/1621904928 expires 2026-05-27T01:19:52.766332+0000
```





这些map中最重要的是crushmap，因为这个crushmap决定了你写入集群的数据写入的具体位置。在后面的归置组一节会详细讲解这个map的作用和管理方式。

在生产集群中，通常会有奇数个Monitor节点，例如3，5，7个。原因是高可用架构中，需要通过投票来选举出Leader节点。而选举投票机制中，都会要求大于半数以上的节点处于可用状态才能正常选举投票的流程。例如有5个Monitor节点，则必须要有5/2，即最少3个节点处于可用状态，才能正常选举出 Leader 节点。如果少于3个Monitor节点在工作，则可以认为集群处于故障状态。

这种选举机制通常是为了避免脑裂的出现，在大规模的分布式集群中，一般都可能会把一部分服务部署在另外的机柜或者机房中，因此当两个机柜或者两个机房之间的网络断开时，就会分成两个部分：

![image-20260526151742280](D:\git_repository\cyber_security_learning\markdown_img\image-20260526151742280.png)

如上图所示，如果两个机柜中都各自有2个节点，那么都不满足选举条件，整个集群全部宕机。



### Manager 节点

Manager 组件通常和 Monitor 组件在同一个台机器上部署，Ceph Manager 组件负责从集群中收集其他组件的状态信息并通过它自带的各种模块来进行展示。例如最常见的 Ceph dashboard 模块以及 Prometheus 模块，前者用来管理和展示整个 Ceph 集群各个组件的状态信息，还可以对整个集群进行管理。Prometheus模块则是从每个节点上运行的 node-exporter 组件中收集数据并通过 Grafana 进行展 示。整体架构图如下所示：

![image-20260526151927975](D:\git_repository\cyber_security_learning\markdown_img\image-20260526151927975.png)

除了我们介绍的dashboard 和 Prometheus模块以外，它还提供了REST API接口，可以让用户自己对接外部平台或者通过脚本来控制集群。



#### 常用模块介绍

##### dashboard

dashboard 模块是从 L 版本开始一起发行的，最开始只是一个用来查看 Ceph 集群运行信息以及集群性能数据的 Web 页面，并没有任何管理功能。但是随着版本的迭代，越来越多的用户需要基于 web 的管理能力，通过 Web 页面可以让用户更简单地管理 Ceph 集群。因此社区根据用户的需求，在之前版本的基础 上开发出了新的 Ceph Dashboard 模块。它提供了以下特性：

- 多用户和角色管理
- SSO单点登录
- SSL/TLS支持
- 审计，可以配置为在设计日志里记录所有PUT、POST、DELETE API请求。
- I18N，即国际化支持



**Ceph Dashboard具备以下管理能力：**

- **内嵌 Grafana 面板**：在 Ceph 面板中内嵌了 Grafana 面板，用来展示 Prometheus 模块收集的集群指标；
- **集群日志**：显示最近更新的集群事件和审计日志文件。可以通过优先级、日期和关键字等过滤日志。
- **主机**：显示了集群所有主机列表以及它们上面的存储设备，运行了哪些服务，以及安装 了哪个版本的Ceph
- **性能计数器**：显示每个运行的服务相关的统计指标详情
- **监视器（mon）**：显示所有的Mon组件，它们的投票状态以及打开的会话。
- **配置编辑**：显示所有可用的配置选项，描述信息、类型、默认和当前的配置值， CRUSH规则、配额等等信息；
- **池（Pool）**：显示Ceph存储池以及它们的详情（例如应用类型、pg自动缩放，pg、副 本数量、EC配置，CRUSH规则、配额等）
- **OSD**：显示OSD以及它们的状态、使用率指标以及详情信息（例如OSD map）、元数 据、性能计数器等。标记OSD的up/down/out状态，清除或者调整OSD权重，执行scrub 操作，修改scrub相关的配置选项，选择配置模板来调整回填事件的级别。列出OSD关 联的设备，设置和修改OSD的设备类别，通过设备类别对OSD进行显示或者排序。在新 的设备或者主机上部署OSD。
- **设备管理**：列出被编排器感知到的所有主机，列出主机上的所有驱动设备以及它们的熟悉，显示驱动盘设备健康预测和SMART数据，闪烁对应的LED等。
- **iSCSI**
- **RBD**：列出所有 RBD 镜像以及它们的属性（大小、对象、特性），创建、复制、修改和删除RBD镜像以及管理RBD名称空间。在全局、单池、或者单镜像级别定义多种 I/O 或 带宽限制。创建、删除和回滚选定镜像的快照，保护/取消保护快照避免修改，复制或克 隆快照，拍扁克隆的快照。
- **RBD 镜像**：启用和配置 RBD 镜像到一个远程的 Ceph 集群，列出活动的进程和它们的状态、存储池和RBD镜像，包括同步进程；
- **对象网关**：列出所有活动的对象网关以及它们的性能计数器，显示和管理（添加/编辑/ 删除）对象网关用户和它们的详情（例如配额、认证密钥等）以及用户的存储桶和存储 桶详情（例如所有者、配额、版本、多因子认证等）。
- **NFS**：管理通过 NFS Ganesha 和 CephFS 文件系统、RGW S3 存储桶实现的NFS。
- **Ceph Manager 模块**：启用或者禁用Ceph Manager模块，管理模块相关的配置设置。



**dashboard模块配置命令**

内置的 dashboard 模块实际上是一个完整的 HTTP 服务器，能够实现多种配置，包括：

- 用户和角色管理
- 证书管理
- 单点登录配置

等等功能，非常强大。我们这里记录几个常用的操作。



**显式当前角色**

```bash
[root@rl-ceph1 /etc/ceph]# ceph dashboard ac-role-show
["administrator", "read-only", "block-manager", "rgw-manager", "cluster-manager", "pool-manager", "cephfs-manager", "ganesha-manager"]
```

**显式用户信息**

```bash
[root@rl-ceph1 /etc/ceph]# ceph dashboard ac-user-show admin
{"username": "admin", "password": "$2b$12$65jPiA2qlra8EeW.3Gt1f.vLqQmSUgESMv4dKl/qDWM12/7/7Ifk6", "roles": ["administrator"], "name": null, "email": null, "lastUpdate": 1779759781, "enabled": true, "pwdExpirationDate": null, "pwdUpdateRequired": false}
```

**创建新用户并绑定角色**

```bash
ceph dashboard ac-user-create afei read-only afei afei@magedu.com -i password.txt 
```

也可以通过面板创建，操作更简单

![image-20260526155744609](D:\git_repository\cyber_security_learning\markdown_img\image-20260526155744609.png)

![image-20260526155757156](D:\git_repository\cyber_security_learning\markdown_img\image-20260526155757156.png)



##### Prometheus

这个模块提供了一个 Prometheus exporte r来传递从 ceph-mgr 里收集的各种性能计数器数据。并通过一 个 http 页面展示所有收集到的指标数据，访问效果如下所示：

```http
http://10.2.100.221:9283/metrics
```

![image-20260526160322574](D:\git_repository\cyber_security_learning\markdown_img\image-20260526160322574.png)



#### 模块管理

##### 查看模块

使用下面的命令可以查看当前集群中所有模块，以及它们对应的状态：

```bash
[root@rl-ceph1 /etc/ceph]# ceph mgr module ls
MODULE                              
balancer              on (always on)
crash                 on (always on)
devicehealth          on (always on)
orchestrator          on (always on)
pg_autoscaler         on (always on)
progress              on (always on)
rbd_support           on (always on)
status                on (always on)
telemetry             on (always on)
volumes               on (always on)
cephadm               on            
dashboard             on            
iostat                on            
nfs                   on            
prometheus            on            
restful               on            
alerts                -             
diskprediction_local  -             
influx                -             
insights              -             
k8sevents             -             
localpool             -             
mds_autoscaler        -             
mirroring             -
......
```

模块状态说明：

- （always on）表示这个模块需要一直开启保证集群正常工作，可以强制关闭。
- on，表示模块处于开启状态，可以正常关闭
- -，表示模块处于关闭状态，需要手动开启；



##### 启动模块

启用模块使用的命令格式是：

```bash
ceph mgr module enable <module-name>
```

例如要启用告警模块alerts，对应的命令就是：

```bash
ceph mgr module enable alerts
```



**查看模块对外服务地址**

部分模块在启用后可以通过指定地址访问，例如我们的 dashboard 模块，mgr也提供了命令来查看所有模块的暴露地址，命令是：

```bash
[root@rl-ceph1 /etc/ceph]# ceph mgr services
{
    "dashboard": "https://10.2.100.221:8443/",
    "prometheus": "http://10.2.100.221:9283/"
}
```



**关闭模块**

关闭模块使用的命令格式是：

```bash
ceph mgr module disable <module-name>
```

用法和打开模块一样，正常情况下只能关闭状态为 on 的模块，不能关闭 always-on 状态的模块。



### OSD 节点

OSD 节点上运行的是 ceph-osd 进程，这个进程负责检查它自己的状态以及其他 OSD 的状态，并且把这 些状态向 MON 节点报告。同时 ceph-osd 进程的任务还包括：

- 接收读写请求
- 接收或转移故障PG数据；
- 检测或发送心跳信息；
- PG 数据清洗 scrub;



#### osd 状态和权重

执行ceph -s命令时，可以看到OSD节点的大致状态，如下所示：

```bash
[root@rl-ceph1 /etc/ceph]# ceph -s
  cluster:
    id:     67c41f82-58a0-11f1-9541-0050562f55be
    health: HEALTH_OK
 
  services:
    mon: 3 daemons, quorum rl-ceph1,rl-ceph2,rl-ceph3 (age 6h)
    mgr: rl-ceph2.mdvjav(active, since 6h), standbys: rl-ceph1.rekvwd
    osd: 9 osds: 9 up (since 5h), 9 in (since 5h)
 
  data:
    pools:   5 pools, 129 pgs
    objects: 14 objects, 449 KiB
    usage:   264 MiB used, 900 GiB / 900 GiB avail
    pgs:     129 active+clean
```

例如上面的示例输出中，可以看到集群中9个OSD节点是up和in的状态，都是正常状态。OSD对应的状态一般有4中：

- **in/out**，表示OSD进程是否正常对外提供服务，标记为out，表示该OSD节点无法对外提 供服务
- **up/down**，表示OSD进程是否正常运行，标记为down，表示ceph-osd进程已停止。

在Reef版本中，目前只有3个命令可以来修改 OSD 的这几种状态，分别是：

```bash
ceph osd down id
ceph osd up id
ceph osd out id
```

OSD 的状态变化会直接导致整个集群的 map 发生变化，进而可能会导致数据发生迁移，因此在正常情况下，不要使用这几个命令来调整 OSD 的状态。

在使用命令ceph osd tree查看集群OSD的状态时，可以看到如下信息：

```bash
[root@rl-ceph1 /etc/ceph]# ceph osd tree
ID  CLASS  WEIGHT   TYPE NAME          STATUS  REWEIGHT  PRI-AFF
-1         0.87918  root default                                
-3         0.29306      host rl-ceph1                           
 0    ssd  0.09769          osd.0          up   1.00000  1.00000
 1    ssd  0.09769          osd.1          up   1.00000  1.00000
 2    ssd  0.09769          osd.2          up   1.00000  1.00000
-5         0.29306      host rl-ceph2                           
 3    ssd  0.09769          osd.3          up   1.00000  1.00000
 4    ssd  0.09769          osd.4          up   1.00000  1.00000
 5    ssd  0.09769          osd.5          up   1.00000  1.00000
-7         0.29306      host rl-ceph3                           
 6    ssd  0.09769          osd.6          up   1.00000  1.00000
 7    ssd  0.09769          osd.7          up   1.00000  1.00000
 8    ssd  0.09769          osd.8          up   1.00000  1.00000
```

在上面的示例输出中，是本次测试集群的几个OSD节点的信息。从输出中我们可以看到两个关键字：

- WEIGHT
- REWEIGHT

这两个关键字对应的是OSD节点能够存储的数据量。WEIGHT是和OSD底层存储设备的容量直接相 关，1T容量对应的值是1，我们使用的测试盘都是100G一个，去掉日志存储部分使用的容量，还有 97.69G，对应值就是0.09769。

而 REWEIGHT 的值则是这个 OSD 底层设备容量能够使用的比例，默认是1，表示100%。通常在数据分布不均衡的时候需要调节这个值的大小。数据不均衡指的是同一个集群中，整个集群的平均使用率在 70%，但是部分OSD使用率超过85%，而另外一部分在30-70%之间，说明数据在不同的OSD节点之间并不是均匀分布的，就会导致部分OSD使用率超过告警比例，集群状态变为HEALTH_WARN状态，这 个时候就可以通过调整这个 REWEIGHT 的值来调整OSD中存储的数据比例。

调整权重的命令格式是：

```bash
ceph osd reweight <id|osd.id> <weight:float>
```

示例如下

```bash
# REWEIGHT 的取值范围：0.0 ~ 1.0
[root@rl-ceph1 /etc/ceph]# ceph osd reweight osd.0 0.95
reweighted osd.0 to 0.95 (f333)
```

调整完成后，查看集群OSD节点状态如下所示：

```bash
[root@rl-ceph1 /etc/ceph]# ceph osd tree
ID  CLASS  WEIGHT   TYPE NAME          STATUS  REWEIGHT  PRI-AFF
-1         0.87918  root default                                
-3         0.29306      host rl-ceph1                           
 0    ssd  0.09769          osd.0          up   0.95000  1.00000
 1    ssd  0.09769          osd.1          up   1.00000  1.00000
 2    ssd  0.09769          osd.2          up   1.00000  1.00000
-5         0.29306      host rl-ceph2                           
 3    ssd  0.09769          osd.3          up   1.00000  1.00000
 4    ssd  0.09769          osd.4          up   1.00000  1.00000
 5    ssd  0.09769          osd.5          up   1.00000  1.00000
-7         0.29306      host rl-ceph3                           
 6    ssd  0.09769          osd.6          up   1.00000  1.00000
 7    ssd  0.09769          osd.7          up   1.00000  1.00000
 8    ssd  0.09769          osd.8          up   1.00000  1.00000
```

可以看到OSD.0的权重变成了0.95.

**osd 使用率查看**

```bash
# 之前创建了1G的image，但是并未挂载使用，因此只写入了部分元数据，此时显式USED:36KiB.
# RBD 的核心机制之一：Thin Provisioning（薄置备）
[root@rl-ceph1 /etc/ceph]# ceph df
--- RAW STORAGE ---
CLASS     SIZE    AVAIL     USED  RAW USED  %RAW USED
ssd    900 GiB  900 GiB  264 MiB   264 MiB       0.03
TOTAL  900 GiB  900 GiB  264 MiB   264 MiB       0.03
 
--- POOLS ---
POOL     ID  PGS   STORED  OBJECTS     USED  %USED  MAX AVAIL
.mgr      1    1  897 KiB        2  2.6 MiB      0    285 GiB
volumes   2   32     19 B        2   12 KiB      0    285 GiB
images    3   32     19 B        2   12 KiB      0    285 GiB
backups   4   32     19 B        2   12 KiB      0    285 GiB
vms       5   32    133 B        6   36 KiB      0    285 GiB

[root@rl-ceph1 /etc/ceph]# ceph osd df
ID  CLASS  WEIGHT   REWEIGHT  SIZE     RAW USE  DATA     OMAP    META     AVAIL    %USE  VAR   PGS  STATUS
 0    ssd  0.09769   1.00000  100 GiB   27 MiB  1.1 MiB   1 KiB   26 MiB  100 GiB  0.03  0.93   44      up
 1    ssd  0.09769   1.00000  100 GiB   27 MiB  1.1 MiB   1 KiB   26 MiB  100 GiB  0.03  0.93   51      up
 2    ssd  0.09769   1.00000  100 GiB   32 MiB  1.5 MiB   1 KiB   30 MiB  100 GiB  0.03  1.09   34      up
 3    ssd  0.09769   1.00000  100 GiB   32 MiB  1.5 MiB   1 KiB   30 MiB  100 GiB  0.03  1.09   41      up
 4    ssd  0.09769   1.00000  100 GiB   27 MiB  1.1 MiB   1 KiB   26 MiB  100 GiB  0.03  0.93   46      up
 5    ssd  0.09769   1.00000  100 GiB   27 MiB  1.1 MiB   1 KiB   26 MiB  100 GiB  0.03  0.93   42      up
 6    ssd  0.09769   1.00000  100 GiB   31 MiB  1.1 MiB   1 KiB   30 MiB  100 GiB  0.03  1.07   43      up
 7    ssd  0.09769   1.00000  100 GiB   28 MiB  1.5 MiB   1 KiB   26 MiB  100 GiB  0.03  0.95   44      up
 8    ssd  0.09769   1.00000  100 GiB   31 MiB  1.1 MiB   1 KiB   30 MiB  100 GiB  0.03  1.07   42      up
                       TOTAL  900 GiB  264 MiB   11 MiB  14 KiB  253 MiB  900 GiB  0.03                   
MIN/MAX VAR: 0.93/1.09  STDDEV: 0.00
```



#### OSD 心跳检测

心跳机制是 Ceph 集群用来保证集群状态和维护节点状态的一种重要机制，OSD节点之间默认情况下每隔6s（实际会增加一个随机时间来降低集群网络并发）给其他 OSD 节点发送一条心跳信息，并期待接收到其他节点的响应消息。

![image-20260526163130207](D:\git_repository\cyber_security_learning\markdown_img\image-20260526163130207.png)

在多次没有接收到其他 OSD 节点的消息，或者接收这个 OSD 节点消息超时（20s），就会向 MON 上报 这个 OSD 节点的状态，当 MON 接收到多个 OSD 上报某个 OSD 节点无法响应心跳请求或者响应超时时， 就会把这个 OSD 标记为 out 状态。流程图如下所示：

![image-20260526163222560](D:\git_repository\cyber_security_learning\markdown_img\image-20260526163222560.png)



#### OSD 后端存储 FileStore 和 BlueStore

![image-20260526163250313](D:\git_repository\cyber_security_learning\markdown_img\image-20260526163250313.png)

FileStore和BlueStore都是Ceph使用的存储后端，FileStore是直接在文件系统里存储切分后的单个小对 象文件，通常使用XFS、EXT4等常见的文件系统格式，每个对象文件都是文件系统里单个独立的小文 件。FileStore使用日志来处理写入操作和保证数据的一致性。但是基于日志的特性，也是它的缺点， 在文件规模非常大的时候，每次写入文件都会有多次日志记录，而日志操作实际上也是磁盘IO操作， 因此会导致非常高的IO读写频率，同时基于文件系统的存储方式，数据延迟较高。 BlueStore是社区开发出来的新存储后端，用来解决FileStore里的各种弊端，例如过高的IO读写和较高 的数据读写延迟等问题。

BlueStore直接在块设备（可以是裸设备，也可以是LVM）上存储数据，绕过了文件系统层，使用 RocksDB作为键值对存储和leveldb来存储小对象，Ceph里使用键值对存储来管理元数据。BlueStore 还自带数据压缩和校验能力。因此从L版本开始，BlueStore 就成为了 Ceph 的默认后端存储。 对于 BlueStore 来说，默认需要有 3 个存储，分别是：

- 存储文件数据的主存储；
- 存储文件元数据（在RocksDB中）的db存储（可选）
- 存储内部日志（RocksDB write-ahead log，简写为WAL）的WAL存储（可选）；

在生产上使用时，通常会把db存储和WAL存储放到小容量的高性能固态磁盘上，因为这两者都是高IO 读写操作，在高性能固态磁盘上，可以极大的提升这两者的读写速度，能够有效地降低IO读写时延。



### MDS 节点

MDS节点是在部署了CephFS组件后才会启用的一类节点，主要用来管理文件的元数据信息，包括文件创建时间、修改时间、最后访问时间、所有者等。通过这个组件和其他组件的组合才能向外提供文件存储服务。整体架构如下所示：

![image-20260527092819982](D:\git_repository\cyber_security_learning\markdown_img\image-20260527092819982.png)



CephFS 的客户端在挂载了 CephFS 卷以后，就会同时访问Ceph集群Mon、OSD 和 MDS 组件，Mon 负责认证，OSD 负责读写实际的文件数据，MDS 则负责向客户端提供文件的属性信息，以及组织构建目录结构，并提供文件、目录相关操作支持，例如查看文件属性，切换目录等等。



### RGW 节点



### Ceph CRUSH 算法介绍

CRUSH（Controlled Repliation Under Scalable Hashing，可扩展哈希下的受控复制）算法是一种基于伪随机控制数据分布、复制的算法，在Ceph集群中的作用是用来控制客户端写入的数据实际保存的位置。

Ceph是一种大规模分布式存储系统，大规模的 Ceph 集群可以拥有 EB 级别的数据和几百上千台存储设备。在这样大规模的存储系统中，在设计时必须要考虑到数据的平衡分布、负载、系统扩展和硬件容错等问题，而CRUSH算法就是为解决这些问题而设计的。

在大规模存储系统中，CRUSH必须面对这些常见的场景或者问题：

- 集群系统中任何一方需要可以通过 CURSH 算法计算出独立对象文件的位置；
- 故障域隔离，不能因为一台主机故障导致所有数据副本丢失；
- 负载均衡，数据需要均匀分布在不同的存储节点，避免出现部分节点容量和性能空闲， 而另外的部分性能超载的情况
- 大型存储系统在动态变化，例如节点扩缩容，硬件故障导致节点失联，这些情况都会导致集群结构发生变化，因此需要把这种变化产生的影响控制在最小。

![image-20260527093356828](D:\git_repository\cyber_security_learning\markdown_img\image-20260527093356828.png)



#### 对象到PG的映射

Ceph客户端把实际的文件（块文件、普通文件）写入到Ceph集群之前，会把文件进行切分，切换后会获得N个具有整个集群唯一OID（Object ID）的小对象文件。OID是线性映射生成的，由文件的元数据、数据片的序号连接组成。此时需要把每个对象文件映射到 PG 中，包含两个步骤:

- Ceph集群指定的 hash 函数计算对象文件 OID 的 hash 值；
- 使用hash值对PG数量值N进行取余操作，获得PG ID；

在 Ceph 集群中，每个存储池中PG的数量都是N（N通常是2的整数幂，例如512，1024等），因此当 hash 值和N进行取余运算的结果都是 [0, N-1] 之间的值，刚好对应的就是每个 PG 的编号。在对象文件数量非常庞大的时候，根据概率论，可以认为对象文件数据是均匀分布在所有的 PG 上。



#### PG到OSD的映射

PG是一个逻辑结构，简单点来看，它的作用就是把所有的对象文件均匀地分成 N 份，它自身并不会保存数据，实际的对象文件数据是存放在 OSD 管理的底层设备上，因此我们还需要计算出 PG 到 OSD 的映 射关系，这个映射流程是由 CRUSH 算法来完成的。

把 PG ID 作为参数输入，返回的PG所在存储池副本数量的 OSD 集合。例如这个 PG 所在存储池是3副本，则会返回3个OSD集合，集合中的第一个OSD被称为主OSD，另外两个被称为从OSD。 这个OSD集合会受到两个因素影响：

- 当前集群状态，当集群中发生硬件数量变化时，Cluster Map也会发生变化，进而导致计 算结果不一致；
- 存储策略规则，例如指定同一个PG的3个副本需要位于不同的机柜甚至机房内，那么计算结果也可能会发生变化

在实际的生产环境中，通常存储策略规则在集群搭建时就会大致固定下来，因此主要的影响因素是集 群中的硬件状态。

当集群的硬件状态发生变化时，例如某个OSD的底层硬盘故障，导致这个OSD无法正常工作，这个时候有数据副本存在这个OSD上的PG就会因为Cluster Map的变化重新计算出新的OSD集合，并复制一 份新的数据到其他OSD上去。

从上面的两个映射流程中我们可以看到，CRUSH算法主要的作用是在**第二步映射**过程中起作用。



#### 存储池Pool和PG

存储池和PG一样，也是一个逻辑概念。Ceph集群使用存储池来做业务划分，每个业务都会分配一个单独的存储池。例如我们在和OpenStack对接配置时创建的存储池images、volumes和vms，分别用来保存虚拟机的镜像文件、数据盘和系统盘。

当这些镜像文件、数据盘文件和系统盘文件经过Ceph客户端写入Ceph集群时，都会切分为单个的小文 件。我们上面说到PG是一个逻辑概念，主要的作用是把存储池里的所有对象文件近似均匀的分成N 份，这样数据就能近似均匀的存放到每一个OSD上。

通过存储池（Pool）和PG这样两个逻辑概念，实现了业务主要的归集和分类，下面我们来看看实际的存储过程。

在使用执行我们需要先创建存储池，创建存储池的命令格式是：

```bash
osd pool create <pool> [<pg_num:int>] [<pgp_num:int>] \
    [<pool_type:replicated|erasure>] \
    [<erasure_code_profile>] [<rule>] \
    [<expected_num_objects:int>] [<size:int>] \
    [<pg_num_min:int>] [<pg_num_max:int>] \
    [<autoscale_mode:on|off|warn>] [--bulk] \
    [<target_size_bytes:int>] \
    [<target_size_ratio:float>] [--yes-i-really-mean-it]
```

创建时需要指定的常用配置包括：

- `pg_num`，`pgp_num`，即 PG 和 PGP 的数量
- `pool_type`，即存储池类型，有两种，分别是：
  - replicated，副本类型
  - erasure，纠删码类型，还可以通过 `erasure_code_profile` 配置指定纠删码配置文件；
- rule，使用的CRUSH规则；
- `pg_num_min`，`pg_num_max`，pg正常服务所需的最小和最大副本数，默认是2和3；
- `autoscale_mode`，是否开启pg数量自动调整功能，默认开启，生产上建议关闭；



#### PG和PGP

在上面配置中，我们看到了PG和PGP两个配置项，PG我们说过是归置组，用来把对象文件进行分组存放。那么PGP又是做什么用的呢？

在 PG 创建完成后，会计算出 PG 到 OSD 的映射关系，而这个映射关系就是PGP来表示的。社区里经常用的一个例子是，在酒店里吃饭时服务员告诉你吃饭的位置在10号包厢（OSD.10），当你走进10号包 厢的时候发现先来的人已经把位子坐满了，这个时候你就需要喊服务员帮你加个椅子，等椅子加好以后你才会正式入座。

PG和PGP的关系是一样的，它俩通常是一对一的关系，当PG创建出来后，还需要指定同等数量的 PGP，然后才会找到真正的OSD，并往里面写入数据。

> 注意：上面的PGP的解释并不算好，PGP实际属于历史包袱，现在的新版 Ceph 会自动保持（pg_num = pgp_num），官方已经不建议人为分离。
>
> 因为现代 Ceph 的 peering、backfill、recovery 已经成熟了很多，没必要再手工控制。 
>
> PGP 本质上是：Ceph 早期为了降低扩容时的数据迁移风暴，而引入的一种“延迟PG参与数据分布”的机制。
>
> 代价是：短期负载不均衡。



##### PG 状态

在实际的生产集群中，PG会因为集群的组件动态变化而出现多种不同的状态。如下所示：

![image-20260527102804678](D:\git_repository\cyber_security_learning\markdown_img\image-20260527102804678.png)

常见的状态有：

- **active + clean**，表示PG处于健康状态；
- **degraded + undersized**，降级状态，多副本时如果某个保存PG副本的OSD故障，则PG 会进入这个状态，此时另外的副本还可以正常读写；
- **peered**，PG副本数量小于pg_num_min时，就会出现该状态，此时PG无法正常读写， 无法响应外部IO请求；
- **remapped**，PG副本因为OSD故障小于pg_num_max时，会把副本映射到新的OSD上， 会出现该状态；
- **wait_backfill/backfilling**，重新映射完成后，pg就会进入到wait_backfill，等待新的OSD 从其他副本拷贝数据，OSD开始拷贝数据后，就会进入到backfilling状态。
- **stale+recovery**，故障OSD重新上线后发现自己的某个PG数据较为陈旧时，会从其他副 本恢复最新的数据，这个过程中这个pg的状态就是recovery；
- **scrub/deep**，OSD上正在对这个PG做数据清洗，OSD会检查不同节点上pg副本数据的 一致性，类似文件系统的fsck命令。这个操作分为轻量扫描和深度扫描，前者只会扫描 元数据，而后者会不光扫描元数据，还会扫描所有实际的文件，速度较慢，且对集群性 能有影响。因此一般会把这个操作配置为业务不繁忙的时候进行。
- **down+peering**，集群出现严重故障导致三个副本数据全部丢失时会出现。



##### 恢复速度调整

pg在进行故障恢复时，会进行频繁的数据读写，会消耗较多的网络带宽和CPU资源，因此生产上会配 置两套网络，让故障恢复在单独的cluster_network中进行，避免对业务造成较大影响。除此之外，还 可以调整pg的恢复配置，调整并发恢复的PG数量，避免对业务造成影响。或者在业务不繁忙的时候调 大恢复并发数，加快业务恢复速度。

查看默认配置：
```bash
[root@rl-ceph1 ~]# ceph-conf --show-config | egrep "osd_recovery_max_active|osd_recovery_op_priority|osd_max_backfills"
osd_max_backfills = 1
osd_recovery_max_active = 0
osd_recovery_max_active_hdd = 3
osd_recovery_max_active_ssd = 10
osd_recovery_op_priority = 3
```

调整并发数量：

```bash
[root@rl-ceph1 ~]# ceph tell 'osd.*' injectargs --osd-max-backfills=2 --osd-recovery-max-active=6
[root@rl-ceph1 ~]# ceph tell 'osd.*' injectargs --osd-max-backfills=3 --osd-recovery-max-active=9
```





#### 副本和纠删码

存储池存储类型有**副本**和**纠删码**两种方式，副本方式很好理解，2个副本数据就存两份，3个副本数据 就存三份，副本类型也是生产上最常用的存储类型，它可以有效地保证数据的安全性（3副本最多可以 丢失2个副本）和性能（3个副本可以同时读取）。

纠删码（Erase Coding，EC）是一种编码容错技术，最早应用在通信行业。基本原理是把传输的数据分段，并加上几个校验数据。同时让各段数据之间互相关联，这样即使传输过程中丢失部分数据，也 可以通过算法把完整的信息计算出来。

纠删码由 k 个数据块和 m 个校验块组成，k表示原始文件被切分的数据块数量，m是根据数据块计算出来的校验块，当小于m个块损坏时，整体数据块可以通过计算剩余块上的数据得到，不会出现数据丢失的情况。

纠删码的优势是它占用的空间要小于副本规则，例如100G的数据盘，3副本时需要占用的实际存储空间就是300G，而4+3类型的纠删码，可以容忍2个块丢失，实际占用的空间是((4+3)/4)*100=175G，比 2副本的空间还要少。但是纠删码类型的劣势是，当有数据块丢失时，它需要读取所有剩余的数据块来进行计算，因此会带来极大的CPU资源和网络资源开销，对于需要高并发实时读写的集群来说，纠删码就不太适用。同时它还需要额外的插件支持，因此它的应用场景主要在于一些读写不频繁的冷备场景。两者的存储方式对比如下：



![image-20260527101923367](D:\git_repository\cyber_security_learning\markdown_img\image-20260527101923367.png)



#### Crush规则

最后来看存储池里的 CRUSH 规则，CRUSH 规则是用来定义 PG 数据存放到 OSD 上的规则。Ceph 集群默认使用的是副本规则 replicated_rule，这个规则的内容如下所示：

```bash
# 查看当前默认规则
[root@rl-ceph1 ~]# ceph osd crush rule ls
replicated_rule

# 输出规则查看
[root@rl-ceph1 ~]# ceph osd crush rule dump replicated_rule
{
    "rule_id": 0,
    "rule_name": "replicated_rule",
    "type": 1,
    "steps": [
        {
            "op": "take",
            "item": -1,
            "item_name": "default"
        },
        {
            "op": "chooseleaf_firstn",
            "num": 0,
            "type": "host"
        },
        {
            "op": "emit"
        }
    ]
}
```

这个规则的含义分别是：

- 第一步，选择default入口，即默认的；
- 第二步，在default入口里选择host，即在选定的主机上选择任意一个OSD；
- 第三步，返回选择的结果;



##### 添加一个新规则

先往测试集群每个节点上添加一个 SSD 磁盘，如果是虚拟机上添加的磁盘，默认都识别为 hdd，可以通 过下面的命令修改：

```bash
# 删除指定 OSD 的磁盘类型
[root@rl-ceph1 ~]# ceph osd crush rm-device-class osd.$OSD

# 给没有磁盘类型的 OSD 设置新的类型
[root@rl-ceph1 ~]# ceph osd crush set-device-class ssd osd.$OSD
```

使用时把$OSD替换为实际的osd id。替换完成后的效果如下：

<img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260527104525888.png" alt="image-20260527104525888" style="zoom:67%;" />

每个节点上都可以看到一个ssd磁盘。来定义一个新的规则：

```bash
# ceph osd crush rule create-replicated <rule-name> <root> <failure-domain> <device-class>
[root@rl-ceph1 ~]# ceph osd crush rule create-replicated replicated_ssd default host ssd

# root：CRUSH树的名称
# failure-domain：故障域
# device-class：设备类
```

查看创建成功的规则

```bash
[root@rl-ceph1 ~]# ceph osd crush rule ls 
replicated_rule 
replicated_ssd
```

创建新的存储池使用新规则

```bash
[root@rl-ceph1 ~]# ceph osd pool create ssd-pool 32 32 replicated replicated_ssd
```

往存储池里写入一个文件来进行测试：

```bash
ceph osd map ssd-pool test
```



## Ceph 块存储服务

### 块设备的使用

KRBD（Kernel RADOS Block Device，内核RADOS块设备）是通过内核中的 RBD 模块实现对后端RBD存储的访问，因此一般在使用之前需要先加载rbd模块，命令是：

```bash
```

#### 创建存储池并初始化

```bash
[root@rl-ceph1 ~]# ceph osd pool create rbd 32
pool 'rbd' created
[root@rl-ceph1 ~]# rbd pool init rbd
```

#### 创建块文件

```bash
[root@rl-ceph1 ~]# rbd create demo-img --size 2048

# 查看，默认查看 pool = rbd
[root@rl-ceph1 ~]# rbd ls
demo-img

[root@rl-ceph1 ~]# rbd ls -p rbd
demo-img

# 查看块文件详情
# 从输出信息可以看到这个块设备切分的最小分片就是4MiB，这个块文件的前缀是 `rbd_data.3adaae2f6209`
[root@rl-ceph1 ~]# rbd info demo-img
rbd image 'demo-img':
        size 2 GiB in 512 objects
        order 22 (4 MiB objects)
        snapshot_count: 0
        id: 3adaae2f6209
        block_name_prefix: rbd_data.3adaae2f6209
        format: 2
        # exclusive-lock 排它锁，即一旦一个系统挂载了这个块，其他系统只能以只读的形式挂载
        features: layering, exclusive-lock, object-map, fast-diff, deep-flatten
        op_features: 
        flags: 
        create_timestamp: Wed May 27 11:11:02 2026
        access_timestamp: Wed May 27 11:11:02 2026
        modify_timestamp: Wed May 27 11:11:02 2026
        
# 查看块文件的对象文件信息
# demo-img 本质上是：大量对象 + 元数据对象共同组成的一个“逻辑块设备”
[root@rl-ceph1 ~]# rados ls -p rbd
rbd_directory                           # 整个 pool 的 image 目录
rbd_info                                # pool级别信息
rbd_object_map.3adaae2f6209             # demo-img对象
rbd_trash                               # 整个 pool 的回收站
rbd_header.3adaae2f6209                 # demo-img对象
rbd_id.demo-img                         # demo-img对象
```



#### 扩缩容

```bash
# 缩小块文件大小为2G
[root@rl-ceph1 ~]# rbd resize --size 1024 demo-img --allow-shrink
Resizing image: 100% complete...done.

# 扩大块文件到4G
[root@rl-ceph1 ~]# rbd resize --size 4096 demo-img
Resizing image: 100% com
```



#### 映射

格式：

```ABAP
rbd map {pool-name}/{image-name} --id {user-nme}
```

- pool-name，存储池名称，默认rbd；
- image-name，镜像名称；
- --id user-name，用户名，默认client.admin



```bash
# 把块文件映射到本机上
[root@rl-ceph1 ~]# rbd map rbd/demo-img 
/dev/rbd0

# 查看
[root@rl-ceph1 ~]# rbd showmapped
id  pool  namespace  image     snap  device   
0   rbd              demo-img  -     /dev/rbd0
```

此时就可以把/dev/rbd0当作一个普通的块设备来挂载使用，可以在它上面创建文件系统， 然后读写文件。

```bash
# 格式化文件系统
[root@rl-ceph1 ~]# mkfs.xfs /dev/rbd0 
meta-data=/dev/rbd0              isize=512    agcount=8, agsize=131072 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1    bigtime=1 inobtcount=1 nrext64=0
data     =                       bsize=4096   blocks=1048576, imaxpct=25
         =                       sunit=16     swidth=16 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=16384, version=2
         =                       sectsz=512   sunit=16 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
Discarding blocks...Done.

# 挂载
[root@rl-ceph1 ~]# mount /dev/rbd0 /mnt

# 在 /mnt 创建 50M 文件
[root@rl-ceph1 ~]# dd if=/dev/zero of=/mnt/test.file bs=1M count=50
记录了50+0 的读入
记录了50+0 的写出
52428800字节（52 MB，50 MiB）已复制，0.0535007 s，980 MB/s

# 查看
[root@rl-ceph1 ~]# ls /mnt
test.file

# 使用 rados 查看对象
[root@rl-ceph1 ~]# rados ls -p rbd
rbd_data.3adaae2f6209.0000000000000180
rbd_data.3adaae2f6209.000000000000000c
rbd_data.3adaae2f6209.0000000000000100
rbd_directory
rbd_data.3adaae2f6209.000000000000000b
rbd_info
rbd_data.3adaae2f6209.00000000000003ff
rbd_data.3adaae2f6209.000000000000000a
rbd_data.3adaae2f6209.0000000000000300
rbd_data.3adaae2f6209.0000000000000280
rbd_data.3adaae2f6209.0000000000000003
rbd_data.3adaae2f6209.0000000000000000
rbd_data.3adaae2f6209.0000000000000200
rbd_object_map.3adaae2f6209
rbd_data.3adaae2f6209.0000000000000001
rbd_data.3adaae2f6209.0000000000000004
rbd_data.3adaae2f6209.0000000000000005
rbd_trash
rbd_data.3adaae2f6209.0000000000000007
rbd_data.3adaae2f6209.0000000000000380
rbd_data.3adaae2f6209.0000000000000008
rbd_data.3adaae2f6209.0000000000000002
rbd_data.3adaae2f6209.0000000000000006
rbd_header.3adaae2f6209
rbd_data.3adaae2f6209.0000000000000080
rbd_data.3adaae2f6209.0000000000000009
rbd_id.demo-img
```



#### 取消块设备映射

命令：格式

```ABAP
rbd unmap /dev/rbd/{pool-name}/{image-name}
```



#### 块文件快照

```bash
# 创建快照
[root@rl-ceph1 ~]# rbd snap create demo-img --snap demo-snap1
Creating snap: 100% complete...done.

# 查看快照文件
[root@rl-ceph1 ~]# rbd ls demo-img -p rbd
demo-img

[root@rl-ceph1 ~]# rbd snap ls demo-img
SNAPID  NAME        SIZE   PROTECTED  TIMESTAMP               
     4  demo-snap1  4 GiB             Wed May 27 12:07:14 2026
     
# 删除之前创建的文件
[root@rl-ceph1 ~]# rm -rf /mnt/test.file 

# 快照回滚
# 注意：执行这个操作的时候，块文件必须处于空闲状态，需要解除挂载
# 解除挂载
[root@rl-ceph1 ~]# umount /mnt

# unmap
[root@rl-ceph1 ~]# rbd unmap /dev/rbd0

# 回滚
[root@rl-ceph1 ~]# rbd snap rollback rbd/demo-img@demo-snap1
Rolling back to snapshot: 100% complete...don 


# 挂回去观察回滚后的数据恢复情况
[root@rl-ceph1 ~]# rbd map demo-img
/dev/rbd0

# 重新挂载后查看，数据成功恢复
[root@rl-ceph1 ~]# mount /dev/rbd0 /mnt
[root@rl-ceph1 ~]# ls /mnt/
test.file
```



#### 快照保护

```bash
# 对快照demo-snap1进行保护
[root@rl-ceph1 ~]# rbd snap protect demo-img --snap demo-snap1

# 查看可以发现，PROJECT 这里是 yes
[root@rl-ceph1 ~]# rbd snap ls demo-img
SNAPID  NAME        SIZE   PROTECTED  TIMESTAMP               
     4  demo-snap1  4 GiB  yes        Wed May 27 12:07:14 2026
     
# 此时删除快照会报错
[root@rl-ceph1 ~]# rbd snap rm demo-img --snap demo-snap1
2026-05-27T13:34:40.474+0800 7f3440fe4640 -1 librbd::Operations: snapshot is protected
Removing snap: 0% complete...failed.
rbd: snapshot 'demo-snap1' is protected from removal.

# 解除保护
[root@rl-ceph1 ~]# rbd snap unprotect demo-img --snap demo-snap1

# 再次查看
[root@rl-ceph1 ~]# rbd snap ls demo-img
SNAPID  NAME        SIZE   PROTECTED  TIMESTAMP               
     4  demo-snap1  4 GiB             Wed May 27 12:07:14 2026
```



#### 快照文件克隆

```bash
# 创建快照的克隆
# 创建克隆之前需要对快照进行保护，否则创建克隆时会报错。
[root@rl-ceph1 ~]# rbd snap protect demo-img --snap demo-snap1
[root@rl-ceph1 ~]# rbd clone demo-img --snap demo-snap1 demo-clone

# 查看
[root@rl-ceph1 ~]# rbd ls
demo-clone
demo-img
```



#### 导入导出

```BASH
# 导入镜像
[root@rl-ceph1 ~]# rbd export demo-img ./demo-img
Exporting image: 100% complete...done.

# 查看
[root@rl-ceph1 ~]# ls
anaconda-ks.cfg  ceph-info.txt  demo-img  set_docker_proxy.sh

# 导入镜像到存储池
[root@rl-ceph1 ~]# rbd import demo-img rbd/demo-img2
Importing image: 100% complete...done.

# 查看
[root@rl-ceph1 ~]# rbd ls
demo-clone
demo-img
demo-i
```



#### 删除块文件

```bash
[root@rl-ceph1 ~]# rbd rm demo-img2
Removing image: 100% complete...done.

[root@rl-ceph1 ~]# rbd ls
demo-clone
demo-img
```



## Ceph 对象存储服务

### 功能架构

实际生产上部署对象网关服务时，会同时部署多个节点，然后在前端使用负载均衡组件进行反向代 理，来实现业务请求的负载均衡和组件的高可用。实际架构如下所示：



### 逻辑架构

对象网关服务中，是使用用户来进行资源管理的，名称空间下可以创建多个用户，每个用户可以创建多个存储桶，然后使用用户名和认证密钥往不同的存储桶中上传文件。逻辑架构如下所示：

![image-20260527134658433](D:\git_repository\cyber_security_learning\markdown_img\image-20260527134658433.png)



### 文件切分

用户在客户端上认证完成后，通过客户端上传数据时，数据会自动被切片，切分为一个512KB的头数 据分片、若干个4MB的数据分片、不足4MB的尾数据分片。根据命名规则，每个数据分片都有全局唯 一的命名，并根据CEPH的数据分布规则选择存放到不同的OSD。其中，head分片还负责存储对象的 所有属性信息和后续数据分片的索引信息。

RGW接收客户端上传的对象数据，首先在内存中缓存head分片数据及对象属性信息，然后将后续分片 数据并行存储到不同OSD，并在内存中记录各个分片的索引信息，最后存储head分片数据，同时将对 象的属性和分片数据索引等元数据信息存储到head分片文件的扩展属性中。

head分片的名称就是对象的名称，用户访问对象时，RGW根据请求访问的对象名称读取head分片数 据及元数据信息，根据记录的元数据信息并行读取对象的全部分片数据并按序返回给客户端。

![image-20260527153357051](D:\git_repository\cyber_security_learning\markdown_img\image-20260527153357051.png)



### 对象网关服务部署

```bash
# 添加rgw组件的命令是
[root@rl-ceph1 ~]# ceph orch host label add rl-ceph1.mystical.com rgw
Added label rgw to host rl-ceph1.mystical.com
[root@rl-ceph1 ~]# ceph orch host label add rl-ceph2.mystical.com rgw
Added label rgw to host rl-ceph2.mystical.com
[root@rl-ceph1 ~]# ceph orch host label add rl-ceph3.mystical.com rgw
Added label rgw to host rl-ceph3.mystical.com

# 上面命令将3台主机分别打上rgw标签，然后执行下面命令，将rgw服务部署到带有rgw标签的主机上：
[root@rl-ceph1 ~]# ceph orch apply rgw  rpa '--placement=label:rgw'
Scheduled rgw.rpa update...

# 查看
[root@rl-ceph1 ~]# ss -ntlp|grep -P  '80 '
LISTEN 0      4096          0.0.0.0:80        0.0.0.0:*    users:(("radosgw",pid=435058,fd=52))     
LISTEN 0      4096             [::]:80           [::]:*    users:(("radosgw",pid=435058,fd=53))  
```

默认情况下，所有rgw服务都会启动并监听在主机的80端口上。



### 配置账号

RGW 服务配置成功以后，需要创建一个对象存储用户，命令是  

```bash
# 会返回access_key和secret_key，记录下来后面使用
[root@rl-ceph1 ~]# radosgw-admin user create --uid=mystical --display-name="mystical" --email=mystical@magedu.com
{
    "user_id": "mystical",
    "display_name": "mystical",
    "email": "mystical@magedu.com",
    "suspended": 0,
    "max_buckets": 1000,
    "subusers": [],
    "keys": [
        {
            "user": "mystical",
            "access_key": "ENDJKZ3OQX05SL9L0GFB",
            "secret_key": "jjDzknquAU9l9DNz4jeNl0fafO3KL3xz7ZCkVJFu"
        }
    ],
    "swift_keys": [],
    "caps": [],
    "op_mask": "read, write, delete",
    "default_placement": "",
    "default_storage_class": "",
    "placement_tags": [],
    "bucket_quota": {
        "enabled": false,
        "check_on_raw": false,
        "max_size": -1,
        "max_size_kb": 0,
        "max_objects": -1
    },
    "user_quota": {
        "enabled": false,
        "check_on_raw": false,
        "max_size": -1,
        "max_size_kb": 0,
        "max_objects": -1
    },
    "temp_url_keys": [],
    "type": "rgw",
    "mfa_ids": []
}
```



### 对接测试

使用s3cmd工具来测试对象存储的功能，首先安装它：

```bash
# 安装 s3cmd
[root@rl-ceph1 ~]# dnf install -y python3-pip
[root@rl-ceph1 ~]# pip install s3cmd

# 配置s3cmd工具：
[root@rl-ceph1 ~]# s3cmd --configure
```

根据提示依次输入各个配置项，在这个过程输入出错也没有关系，在输入过程结束后，它会提示你将 配置保存到~/.s3cfg文件中。保存好以后，可以通过修改这个配置文件来修改配置。几个关键配置项有：

```bash
# 其他值填默认值或者空，否则可能报错
[root@rl-ceph1 ~]# vim .s3cfg 
...
access_key = ENDJKZ3OQX05SL9L0GFB
host_base = http://rl-ceph1.mystical.com
host_bucket = http://rl-ceph1.mystical.com/%(bucket)s
secret_key = jjDzknquAU9l9DNz4jeNl0fafO3KL3xz7ZCkVJFu
signature_v2 = True
...
```

上面几个配置项的作用分别是：

- 配置认证
- 配置对象存储连接地址
- 配置对象存储bucket地址基本格式
- 配置认证
- 配置认证签名版本，Ceph目前只支持V2版本。

配置好以后执行命令：

```bash
[root@rl-ceph1 ~]# s3cmd mb s3://test
Bucket 's3://test/' created
```

来创建一个test存储桶查看是否可以正常执行，确认可以正常执行，说明s3对象存储对接正常可以直接 使用。



### 上传测试

```bash
# 创建测试文件
[root@rl-ceph1 ~]# echo "hello ceph rgw" > test.txt

# 上传
[root@rl-ceph1 ~]# s3cmd put test.txt s3://test
upload: 'test.txt' -> 's3://test/test.txt'  [1 of 1]
 15 of 15   100% in    2s     5.09 B/s  done
 
# 查看 bucket 里的文件
[root@rl-ceph1 ~]# s3cmd ls s3://test
2026-05-27 07:59           15  s3://test/test.txt

# 下载文件
[root@rl-ceph1 ~]# s3cmd get s3://test/test.txt
download: 's3://test/test.txt' -> './test.txt'  [1 of 1]
 15 of 15   100% in    0s   288.23 B/s  done
 
# 查看
[root@rl-ceph1 ~]# ls
anaconda-ks.cfg  ceph-info.txt  demo-img  set_docker_proxy.sh  test.txt

# 删除 bucket 里的文件
[root@rl-ceph1 ~]# s3cmd del s3://test/test.txt
delete: 's3://test/test.txt'

# 查看所有 bucket
[root@rl-ceph1 ~]# s3cmd ls
2026-05-27 07:51  s3://test
```





# 混合云组网

## 架构

### ECS

```ABAP
公网:
123.56.7.248

WireGuard:
172.16.0.1
```



### Ubuntu Gateway

```ABAP
WireGuard:
172.16.0.2

桥接网络
10.2.0.105
```



### Openstack VM

```ABAP
float IP
10.10.60.131

内网IP
10.100.0.11 (用不到)
```



## 部署过程

### 1. 两边安装 WireGuard

#### ECS（Rocky）

```bash
dnf install epel-release -y
dnf install wireguard-tools -y
```

#### Ubuntu Gateway

```bash
apt update
apt install wireguard -y
```



### 2. 生成密钥

两边都执行：

```bash
wg genkey | tee privatekey | wg pubkey > publickey
```

查看：

```bash
cat privatekey
cat publickey
```



### 3. 配置 ECS

```bash
[root@crmeb ~]# cat /etc/wireguard/wg0.conf 
[Interface]
Address = 172.16.0.1/24
ListenPort = 51820
PrivateKey = <ECS私钥>

[Peer]
PublicKey = <Ubuntu公钥>
AllowedIPs = 172.16.0.2/32,10.100.0.0/16,10.10.0.0/16    # 这里一定要加浮动IP的网段：10.10.0.0/16
```



### 4. 配置 Ubuntu Gateway

```bash
[root@mystical ~]# cat /etc/wireguard/wg0.conf 
[Interface]
Address = 172.16.0.2/24
PrivateKey = <Ubuntu私钥>

PostUp = sysctl -w net.ipv4.ip_forward=1
PostUp = iptables -t nat -A POSTROUTING -d 10.100.0.0/16 -j MASQUERADE
PostDown = iptables -t nat -D POSTROUTING -d 10.100.0.0/16 -j MASQUERADE

[Peer]
PublicKey = <ECS公钥>
Endpoint = 123.56.7.248:51820
AllowedIPs = 172.16.0.1/32
PersistentKeepalive = 25
```



### 5. ECS 开防火墙

阿里云安全组：

放行：

```ABAP
UDP 51820
```

Linux

```bash
# 关闭防火墙
# Rocky
systemctl disable --now firewalld

# ubuntu
systemctl disable --now ufw
```



### 6. 启动

两边：

```bash
systemctl enable wg-quick@wg0
systemctl start wg-quick@wg0
```



### 7. ECS 增加路由（核心）

```bash
ip route add 10.100.0.0/16 via 172.16.0.2 dev wg0
ip route add 10.10.60.131/32 via 172.16.0.2 dev wg0
```



#### Ubuntu Gateway

```bash
# 添加防火墙规则
iptables -t nat -A POSTROUTING \
-d 10.10.60.131 \
-j MASQUERADE
```



### 8. 最终测试

```bash
# ECS 上进行测试
[root@crmeb ~]# ping 10.10.60.131
```





# 课程前部分结构

```bat
虚拟化技术体系
├── 1. CPU 运行级别与特权指令
│   ├── Ring 0 / Ring 3
│   ├── 用户态与内核态
│   ├── 特权指令
│   └── 系统调用
│
├── 2. 虚拟化为什么需要接管最高权限
│   ├── Guest OS 也想运行在 Ring 0
│   ├── Hypervisor 必须控制硬件
│   └── 特权指令拦截问题
│
├── 3. 虚拟化实现方式
│   ├── 软件全虚拟化
│   ├── 半虚拟化
│   └── 硬件支持的全虚拟化
│
├── 4. KVM 的实现位置
│   ├── VT-x / AMD-V
│   ├── VM Entry / VM Exit
│   ├── QEMU 与 KVM 分工
│   └── libvirt 管理接口
│
└── 5. OpenStack 的定位
    ├── OpenStack 不是 Hypervisor
    ├── Nova 管理虚拟机
    ├── 底层对接 libvirt
    └── 常见后端是 KVM
```

