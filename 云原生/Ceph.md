# 分布式存储概述









# Ceph 基础

Ceph是一个开源的分布式存储系统，同时支持对象存储、块设备、文件系统.

![image-20260513162050983](D:\git_repository\cyber_security_learning\markdown_img\image-20260513162050983.png)

ceph支持EB(1EB=1,000,000,000GB)十亿级别的数据存储，ceph把每一个待管理的数据流(文件等数据)切分为一到多个固定大小 (**默认4兆**) 的对象数据，并以其为原子单元(原子是构成元素的最小单元)完成数据的读写。

ceph的底层存储服务是由多个存储主机(host)组成的存储集群，该集群也被称之为 RADOS (reliable automatic distributed object store) 存储集群，即可靠的、自动化的、分布式的对象存储系统。

librados 是 RADOS 存储集群的 API，支持 C/C++/JAVA/python/ruby/php/go 等编程语言客户端。

<img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260513163313710.png" alt="image-20260513163313710" style="zoom:150%;" />

## Ceph 的发展史

Ceph 项目起源于2003年 Ceph 创始人 Sage Weil  (塞奇·威尔,生于1978年3月17日) 在加州大学圣克鲁兹分校（University of California，Santa Cruz,简称UC Santa Cruz 或 UCSC,位于加利福尼亚州）攻读博士期间的研究课题 ( Lustre 环境中的可扩展问题)。

Lustre 是一种平行分布式文件系统,早在1999年，由皮特·布拉姆 (Peter Braam) 创建的集群文件系统公司(Cluster File Systems Inc)开始研发,并于 2003 年发布Lustre 1.0 版本.

而 Ceph 的名称来源于学校的吉祥物香蕉色的蛞(kuò)蝓(yú)--Sammy,蛞(kuò)蝓(yú)是一种无壳的软体动物(类似于没有外壳的蜗牛、国内部分地区叫做鼻涕虫),

- 2007年 Sage Weil (塞奇·威尔)毕业后，Sage Weil 继续全职从事 Ceph 工作，
- 2010年3月19日，Linus Torvalds 将 Ceph 客户端合并到 
- 2010年5月16日 发布的Linux内核版本2.6.34,
- 2012年 Sage Weil 创建了 Inktank Storage 用于为 Ceph 提供专业服务和支持,
- 2014年 4月 Redhat 以1.75亿美元收购 inktank 公司并开源。

Ceph 意思是宠物章鱼(绰号)，而 ceph 把章鱼作为自己的吉祥物，并且 Ceph 也以章鱼作为自己的吉祥物，表达 Ceph 和章鱼一样对并行行为, Inktank 即墨鱼，也类似章鱼的一种海洋生物



## Ceph 的设计目标

Ceph的设计旨在实现以下目标：

- 每一组件皆可扩展
- 无单点故障
- 基于软件(而非专用设备)并且开源(无供应商锁定)
- 在现有的廉价硬件上运行
- 尽可能自动管理，减少用户干预

<img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260513164845947.png" alt="image-20260513164845947" style="zoom:150%;" />



## Ceph 的版本历史

Ceph的第一个版本是0.1,发布日期为2008年1月,多年来ceph的版本号一直采用递归更新的方式没变,直到2015年4月0.94.1(Hammer的第一个修正版)发布后,为了避免0.99(以及0.100或1.00),后期的命名方式发生了改变:

- `x.0.z-开发版`（给早期测试者和勇士们）
- `x.1.z-候选版`（用于测试集群、高手们）
- `x.2.z-稳定、修正版`（给用户们面向企业的稳定版）

x将从9算起，它代表 Infernalis (首字母I是英文单词中的第九个字母),这样第九个大版本的第一个开发版就是9.0.0,后续的开发版依次是 `9.0.0->9.0.1->9.0.2` 等,测试版本就是`9.1.0->9.1.1->9.1.2`,稳定版本就是 `9.2.0->9.2.1->9.2.2`.

![image-20260513182134523](D:\git_repository\cyber_security_learning\markdown_img\image-20260513182134523.png)

到2017年底，Ceph项目都采取每年发布两个稳定版本的做法,从 Jewel 版到 Nautilus 之前，Ceph 经历过一段时间的每间隔9个月发布一个新版本,Nautilus 版本开始改为每年春季3月份发布一个稳定版本,并提供长达26个月左右的后期版本更新.

```http
https://docs.ceph.com/en/latest/releases/
```

![image-20260513182510938](D:\git_repository\cyber_security_learning\markdown_img\image-20260513182510938.png)



## 集群角色定义

![image-20260513190505133](D:\git_repository\cyber_security_learning\markdown_img\image-20260513190505133.png)

LIBRADOS、RADOSGW、RBD和CephFS统称为Ceph客户端接口。RADOSGW、RBD、CephFS是基于LIBRADOS提供的多编程语言接口开发的。

![image-20260513203320890](D:\git_repository\cyber_security_learning\markdown_img\image-20260513203320890.png)

一个ceph集群的技术组成部分：

- 若干的CephOSD（对象存储守护程序）
- 至少需要一个Ceph Monitors监视器（1,3,5,7...）
- 两个或以上的Ceph管理器 managers，运行Ceph文件系统客户端时
- 还需要高可用的Ceph Metadata Server(文件系统元数据服务器)。



### Monitor(ceph-mon) ceph 监视器

在一个主机上运行的一个守护进程，用于**维护集群状态映射**(maintains maps of the cluster state)，比如 ceph 集群中有多少存储池、每个存储池有多少PG以及存储池和 PG 的映射关系等，monitor map,manager map,the OSD map,the MDS map,and the CRUSH map，这些映射是 Ceph 守护程序相互协调所需的关键群集状态，此外监视器还负责**管理守护程序和客户端之间的身份验证**(认证使用 cephX 协议)。通常至少需要三个监视器才能实现冗余和高可用性。

```bat
MON 负责：“集群一致性元数据”，本质上是 “Ceph 的权威状态数据库”，可以类比于 Kubernetes 的 ETCD
```

MON 里的数据主要包含：

**OSDMap（最核心）**

例如：

```bat
哪些 OSD 存活
哪些 down
哪些 in/out
```

客户端必须先从 MON 获取：

```ABAP
OSDMap
```

才能知道：

```bat
object 应该写到哪个 OSD
```

**MONMap**：MON 自己的集群信息。

**CRUSHMap：**数据分布规则。

**auth（CephX）**：认证各种身份信息

**集群状态**



### Managers(ceph-mgr)的功能

在一个主机上运行的一个守护进程，Ceph Manager 守护程序（ceph-mgr）负责跟踪运行时指标和 Ceph 集群的当前状态，包括存储利用率，当前性能指标和系统负载。Ceph Manager守护程序还托管基于python的模块来管理和公开Ceph集群信息，包括基于 Web 的 Ceph 仪表板和 RESTAPI 。高可用性通常至少需要两个管理器。

```bat
MGR 负责：“集群运行时管理与观测”，它更像 “运维管理中心”
```

**MGR 主要做什么？**

- Dashboard
- Prometheus metrics
-  orchestrator
- REST API
- 自动管理模块

> MON 负责：集群“是什么状态”。即 “权威状态”； 
>
> MGR 负责：集群“怎么观察和管理”。即 “运维增强”；



### CephOSDs ( 对象存储守护程序 ceph-osd )

提供存储数据，操作系统上的一个磁盘就是一个OSD守护程序，OSD用于处理 ceph 集群数据复制，恢复，重新平衡，并通过检查其他CephOSD守护程序的心跳来向 Ceph 监视器和管理器提供一些监视信息。通常至少需要3个CephOSD才能实现冗余和高可用性。



### MDS(ceph元数据服务器ceph-mds)

代表 ceph 文件系统 ( NFS/CIFS ) 存储元数据，(即 Ceph 块设备和 Ceph 对象存储不使用 MDS)



### Ceph的管理节点

- ceph的常用管理接口是一组命令行工具程序，例如rados、ceph、rbd等命令，ceph管理员可以从某个特定的ceph-mon节点执行管理操作
- 推荐使用部署专用的管理节点对ceph进行配置管理、升级与后期维护，方便后期权限管理，管理节点的权限只对管理人员开放，可以避免一些不必要的误操作的发生。





## 逻辑组织架构

### 基本概念

- **Pool**：存储池、存储数据的逻辑环境(不能直接对应OSD)、不同的业务可以使用不同的存储池隔离数据(类似于 K8S 的 namespace )，存储池的空间大小取决于底层的物理存储空间的大小。

- **PG(placementgroup)**：一个pool内部通常有多个PG存在，pool和PG都是抽象的逻辑概念，一个pool中有多少个PG可以通过公式进行粗略计算。

- **OSD(ObjectStorageDaemon,对象存储设备)**:每一块磁盘都是一个 osd，一个主机由一个或多个 osd 组成.

ceph 集群部署好之后,要先创建存储池并指定 PG 数量、才能向 ceph 写入数据，文件在向 ceph 保存之前要先进行一致性 hash 计算，计算后会把文件保存在某个对应的 PG 的，此文件一定属于某个 pool 的一个PG，在通过 PG 保存在 OSD 上。

<img src="D:\git_repository\cyber_security_learning\markdown_img\image-20260514093151799.png" alt="image-20260514093151799" style="zoom:150%;" />





存储服务的网络设备，通常不和业务混用，有单独的交换机和机柜，防止被业务影响。



### Ceph里的文件存储过程

以 CephFS 为例

CephFS 可以分为 Client侧 和 Server侧，而MDS是 Server侧 的组件 

```bat
echo "hello" > /mnt/cephfs/a.txt
```

- **第一步：Client 访问 MDS**：我要创建 /a.txt

- **第二步：MDS 创建 inode**

- **第三步：MDS 返回 layout 给 CephFS Client**

  - 例如：

    ```ini
    data pool = cephfs_data
    object_size = 4MB
    striping policy = xxx
    ```

    即告诉 Client：

    ```bat
    “你以后该怎么切 object”
    ```

- **第四步：CephFS Client 将 File 切分为 Object 并调用 librados 发给 RADOS 集群中具体的 OSD**

  - CephFS Client 从 MON 得到集群元数据后，根据 object -> PG -> CRUSH，计算 Primary OSD 和 Replica OSD Set
  - CephFS Client librados ，进而和 RADOS 的Primary OSD 建立网络通信

- **第五步：Primary OSD 同步副本**

- **第六步：BlueStore 落盘**

- **第七步：同步落盘后 (至少达到 min_size 要求)，将成功结果返回给Client**

#### 总结与补充：

```bat
MDS 管：这个文件应该怎么切、写哪里
Client 按 layout 执行：真正切 object、写 OSD
RADOS 管：object 最终落到哪些 PG/OSD
```

**CephFS layout 主要包含什么？**

```bat
pool        ：文件数据写入哪个 data pool
stripe_unit ：每个条带单元大小
stripe_count：一轮条带分布到几个 object
object_size ：单个 object 的最大大小
```

简单理解：

| 字段           | 作用                                            |
| -------------- | ----------------------------------------------- |
| `pool`         | 这个文件的数据 object 写到哪个 CephFS data pool |
| `object_size`  | 文件数据被切成多大的 object                     |
| `stripe_unit`  | 每次连续写入一个 object 的数据块大小            |
| `stripe_count` | 数据是否在多个 object 之间做条带化              |

##### 关于 Stripe 的理解

如果 “不条带化”，即最简单的情况（stripe_count=1）

假设：

```ini
object_size = 4MB
stripe_unit = 4MB
stripe_count = 1
```

文件：`12MB`，则 `CephFS Client` 直接

```bat
前4MB → object0
中4MB → object1
后4MB → object2
```

即：

```ini
object0 = 文件0~4MB
object1 = 文件4~8MB
object2 = 文件8~12MB
```

这是 **"最普通切片"** 没有 “条带化”

---

那什么是 “条带化”

现在：
```ini
stripe_unit = 1MB
stripe_count = 4
object_size = 4MB
```

这里意思变成：**“每1MB”** 切换一次 object。

---

**真正写入过程**

文件：

```bat
0MB ~ 8MB
```

现在不会：

```bat
连续 4MB 写一个 object
```

而是**轮流写**。

---

**真正条带化过程**

第一轮：

```bat
第1MB → object0
第2MB → object1
第3MB → object2
第4MB → object3
```

第二轮

```bat
第5MB → object0
第6MB → object1
第7MB → object2
第8MB → object3
```

于是最终：

```bat
object0:
  0~1MB
  4~5MB

object1:
  1~2MB
  5~6MB

object2:
  2~3MB
  6~7MB

object3:
  3~4MB
  7~8MB
```

这就是条带化（Stripe）。 最终目的是实现 **“多个OSD可同时读写”**。

---

### Ceph OSD 与 BlueStore

#### OSD 是什么？

OSD（Object Storage Daemon）是 Ceph 中：**真正负责存储 Object 数据的核心服务进程。**

Ceph 集群中的：

- 数据存储
- 副本同步
- Recovery
- Peering
- Scrub

等核心工作，几乎都由 OSD 完成。



#### OSD 的核心职责

OSD 不只是“存数据”。它本质上是 **“一个完整的分布式存储节点服务。”**

OSD 内部同时包含：

```bat
1. 分布式系统逻辑
2. 本地存储引擎
```



#### OSD 的整体架构

![image-20260514153240232](D:\git_repository\cyber_security_learning\markdown_img\image-20260514153240232.png)



#### OSD 的分布式系统职责

##### 1. 网络通信

OSD 通过：

```ABAP
Messenger(msgr2)
```

与：

- Client
- MON
- 其他 OSD

通信。例如：

```ABAP
Client → Primary OSD
Primary OSD → Replica OSD
```

##### 2. PG 管理

OSD 负责：**PG 的运行状态管理。**

例如：

```ABAP
active
clean
peering
degraded
recovering
```

##### 3. 副本同步

Primary OSD 负责：

```ABAP
写入副本
同步 Replica OSD
等待 ACK
```

##### 4. Recovery / Backfill

当：

- OSD Down
- 新增 OSD
- rebalance

发生时，负责：

```bat
PG 数据迁移
副本恢复
数据同步
```

##### 5. Scrub

OSD 定期校验：

```ABAP
副本数据一致性
checksum
metadata
```

##### 6. 事务系统（Transaction）

OSD 内部使用事务系统，保证：

```ABAP
object data + object metadata
```

一致提交。

---

#### BlueStore 是什么？

BlueStore 是 OSD 的本地存储引擎。它负责 object 如何真正落盘。

##### BlueStore 的核心思想

BlueStore 最大的特点：**绕过传统文件系统。**即**不使用**

```ABAP
ext4
xfs
VFS
```

##### 传统 FileStore 的问题

以前 Ceph 使用 FileStore 架构

```ABAP
OSD
 ↓
FileStore
 ↓
ext4/xfs
 ↓
Block Layer
 ↓
Disk
```

即：`Ceph Object -> Linux 文件`

这样会产生：

- inode 开销
- journal 开销
- fsync 开销
- page cache 开销

导致：**IO 路径过长。**

##### BlueStore 的改进

BlueStore 直接 管理裸块设备。即：

```ABAP
OSD
 ↓
BlueStore
 ↓
Block Device
 ↓
Disk
```

##### BlueStore 的整体结构

```bat
BlueStore
├── Allocator（空间分配器）
│
├── object data
│      ↓
│   BlockDevice(block)
│
└── metadata
       ├── RocksDB
       ├── BlueRocksEnv
       └── BlueFS
              ↓
          BlockDevice(block.db/wal)
```

##### BlueStore 的各组件详解

###### Allocator（空间分配器）

Allocator 负责 **管理块设备空间。**例如：

```ABAP
哪些区域空闲
哪些区域已占用
```

工作过程：

当 `写 object abc` 时，Allocator 决定：`写到 BlockDevice 哪个 offset`，例如：

```ABAP
offset=100MB
len=4MB
```

###### object data

真正的 **“用户 Object 数据。”**

例如：

```ABAP
4MB object 内容
```

这些数据：直接写入 BlockDevice。

###### RocksDB

RocksDB 是 BlueStore 的元数据库。它负责 **保存 Object metadata**。例如：
```ABAP
object abc
→ offset=100MB
→ length=4MB
→ checksum=xxx
```

RocksDB 保存的内容

例如：

- object offset
- object extent
- omap
- checksum
- attr
- allocation metadata

###### BlueFS

BlueFS 是 Ceph 自己实现的小型文件系统。

**为什么需要 BlueFS？**

因为 RocksDB 需要文件系统接口。但 BlueStore 又不使用 `ext4/xfs`。于是 Ceph 自己实现 BlueFS 专门给 RocksDB 使用。

###### BlueRocksEnv

BlueRocksEnv 是 RocksDB 的 BlueFS 的适配层。

因为 RocksDB 原本认为自己运行在普通文件系统之上。BlueRocksEnv 负责做 `RocksDB API -> BlueFS API` 的转换。

###### BlockDevice

BlockDevice 是真正的 “块设备”。例如：

```ABAP
/dev/sdb
/dev/nvme0n1
```

**BlueStore 常见设备**

- block
  - 主数据盘：`object data`
- block.db
  - RocksDB 元数据盘。通常：放 SSD/NVMe。
- block.wal
  - WAL 日志盘



##### BlueStore 的写入流程

**第一步：OSD 收到 object 写请求**

例如：

```ABAP
object abc
```

**第二步：事务系统创建 transaction**

OSD生成：

```ABAP
transaction
```

**第三步：Allocator 分配空间**

例如：

```ABAP
offset=100MB
```

**第四步：object data 写 BlockDevice**

直接写：

```ABAP
/dev/sdb
```

对应 offset。

**第五步：metadata 写 RocksDB**

例如：

```ABAP
abc → offset=100MB
```

**第六步：RocksDB 通过 BlueFS 落盘**

```ABAP
RocksDB
 ↓
BlueRocksEnv
 ↓
BlueFS
 ↓
block.db / wal
```

**第七步：事务 commit**

事务完成

**第八步：OSD 返回 ACK**

---

#### Ceph CRUSH 算法简介

**Controllers replication under scalable hashing** 可控的、可复制的、可伸缩的一致性 hash 算法。

Ceph使用 CURSH 算法来存放和管理数据，它是 Ceph 的智能数据分发机制。Ceph 使用 CRUSH 算法来准确计算数据应该被保存到哪里，以及应该从哪里读取和保存元数据

不同的是 CRUSH 按需计算出元数据，因此它就消除了对中心式的服务器／网关的需求,它使得 Ceph 客户端能够计算出元数据，该过程也称为CRUSH查找，然后和OSD直接通信。

**详情待定**



---

# 部署 Ceph 集群

## 部署方式

ceph-deploy：https://github.com/ceph/ceph-deploy#python
是一个 ceph 官方维护的基于 ceph-deploy 命令行部署 ceph 集群的工具，基于 ssh 执行可以 sudo 权限的 shell 命令以及一些 python 脚本实现 ceph 集群的部署和管理维护。
Ceph-deploy 只用于部署和管理 ceph 集群，客户端需要访问 ceph，需要部署客户端工具。

### 服务器准备

构建可靠的、低成本的、可扩展的、与业务紧密结合使用的高性能分布式存储系统。

#### Ceph分布式存储集群规划原则/目标

- 较低的 TCO (Total Cost of Ownership,总拥有成本):
  - 使用廉价的X86服务器。

