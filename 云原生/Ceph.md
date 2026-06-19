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
- 较高的IOPS(Input/Output Operations Per Second,每秒可完成的读写次数):
  - 使用SSD/PCI-E SSD/NVMe硬盘提高存储集群数据以提高读写性能。

- 较大的存储空间
  - 使用单块2T/4T或更大容量的磁盘，提高单台服务器的总空间，节省服务器总数，降低 机柜使用量。

- 较快的网络吞吐
  - 使用10G、40G、100G或更快的光纤网络

- 更好的数据冗余
  - 数据可以以三副本机制分别保存到不同的主机，宕机2台也不会丢失数据。



#### 服务器硬件选型

http://docs.ceph.org.cn/start/hardware-recommendations/ #官方硬件推荐

 https://access.redhat.com/documentation/zh-cn/red_hat_ceph_storage/4/html/installation_guide/minimum-hardware-considerations-for-red-hat-ceph-storage_install #Red Hat Ceph Storage 的最低硬件

 https://documentation.suse.com/zh-cn/ses/7/html/ses-all/storage-bp-hwreq.html #suse 硬件要求和建议 

```ABAP
monitor、mgr、radosgw： 
4C8G~16G(小型，专用虚拟机)、
8C16G~32G(中型，专用虚拟机)、
16C~32C32G~64G(大 型/超大型，专用物理机)

MDS(相对配置更高一个等级)：
8C8G~16G(小型，专用虚拟机)、
16C16G~32G(中型，专用虚拟机)、
32C~64C64G~96G(大型、超大型，物理机)

OSD节点CPU
每个 OSD 进程至少有一个CPU核心或以上，比如服务器一共2颗CPU每个12核心24线程，那么服务器总计有48核心CPU，这样最多最多最多可以放48块磁盘。
(物理CPU数量*每颗CPU核心)/OSD磁盘数量 =X/每OSDCPU核心 >=1核心CPU
比如：(2颗*每颗24核心)/24OSD磁盘数量= 2/每OSDCPU核心 >=1核心CPU

OSD节点内存：
OSD硬盘空间在2T或以内的时候每个硬盘2G内存，4T的空间每个OSD磁盘4G内存，即大约每1T的磁盘空间(最少)分配1G的内存空间做数据读写缓存。
(总内存/OSD磁盘总空间)=X>1G内存
比如：(总内存128G/36T磁盘总空间 )=3G/每T >1G内存
```

Ceph OSD 要以下条件: 

1、目标磁盘不能有任何磁盘分区(例如不能有sdb1/sdc2)。 

2、目标磁盘不能有基于PV/LV创建的LVM。 

3、目标磁盘不能被挂载到当前文件系统的任何目录。 

4、目标磁盘不能包含文件系统(例如不能包含ext4/xfs)。 

5、目标磁盘不能包含CephBlueStoreOSD,会对磁盘进行全部擦除。 

6、目标磁盘大小必须大于5GB,Ceph会自动为小于5GB的磁盘指定权重0



#### 数据分类存储

是否存在访问量不高的业务备份数据(数据库备份、配置文件备份)和访问量比较高的业务数 据(静态文件、对象存储数据)都在ceph集群存储的场景，如果有的话可以分开不同的磁盘 存储。

- 备份数据：SAS7.2K/10K/15K硬盘
- 热点数据：SSD固态硬盘、M.2固态、PCI-E固态



#### ceph 集群规划图

![image-20260523143725511](D:\git_repository\cyber_security_learning\markdown_img\image-20260523143725511.png)



### 部署环境

四台服务器作为 ceph 集群 OSD 存储服务器，每台服务器支持两个网络，public网络针对客户端访问，cluster网络用于集群管理及数据同步，每台三块或以上的磁盘

| 主机名     | Nat网络   | 仅主机        | CPU/Mem | 数据盘            |
| ---------- | --------- | ------------- | ------- | ----------------- |
| ceph-node1 | 10.0.0.51 | 192.168.23.51 | 2C2G    | 1 \* 8T + 4 \* 4T |
| ceph-node2 | 10.0.0.52 | 192.168.23.52 | 2C2G    | 1 \* 8T + 4 \* 4T |
| ceph-node3 | 10.0.0.53 | 192.168.23.53 | 2C2G    | 1 \* 8T + 4 \* 4T |
| ceph-node4 | 10.0.0.54 | 192.168.23.54 | 2C2G    | 1 \* 8T + 4 \* 4T |

三台服务器作为 ceph 集群 Mon 监视服务器，每台服务器可以和 ceph 集群的 cluster 网络通信。

| 主机名    | Nat网络   | 仅主机        | CPU/Mem |
| --------- | --------- | ------------- | ------- |
| ceph-mon1 | 10.0.0.55 | 192.168.23.55 | 2C2G    |
| ceph-mon2 | 10.0.0.56 | 192.168.23.56 | 2C2G    |
| ceph-mon3 | 10.0.0.57 | 192.168.23.57 | 2C2G    |

两个ceph-mgr 管理服务器，可以和ceph集群的cluster网络通信。

| 主机名    | Nat网络   | 仅主机        | CPU/Mem |
| --------- | --------- | ------------- | ------- |
| ceph-mgr1 | 10.0.0.58 | 192.168.23.58 | 2C2G    |
| ceph-mgr2 | 10.0.0.59 | 192.168.23.59 | 2C2G    |

一个服务器用于部署ceph集群即安装Ceph-deploy，也可以和ceph-mgr等复用。

| 主机名      | Nat网络   | CPU/Mem |
| ----------- | --------- | ------- |
| ceph-deploy | 10.0.0.60 | 2C4G    |

创建一个普通用户，能够通过sudo执行特权命令，配置主机名解析，ceph 集群部署过程中需要对各主机配置不同的主机名，另外如果是 centos 系统则需要关闭各服务器的防火墙和 selinux。



**网络环境**

![image-20260523160037467](D:\git_repository\cyber_security_learning\markdown_img\image-20260523160037467.png)





###  系统环境初始化

- 时间同步(各服务器时间必须一致)
- 关闭selinux 和防火墙(如果是Centos)
- 配置主机域名解析或通过DNS解析

```bash
[root@ceph-node3 ~]# vim /etc/hosts
10.0.0.51 ceph-node1.mystical.org ceph-node1
10.0.0.52 ceph-node2.mystical.org ceph-node2
10.0.0.53 ceph-node3.mystical.org ceph-node3
10.0.0.54 ceph-node4.mystical.org ceph-node4
10.0.0.55 ceph-mon1.mystical.org  ceph-mon1
10.0.0.56 ceph-mon2.mystical.org  ceph-mon2
10.0.0.57 ceph-mon3.mystical.org  ceph-mon3
10.0.0.58 ceph-mgr1.mystical.org  ceph-mgr1
10.0.0.59 ceph-mgr2.mystical.org  ceph-mgr2
```





### 部署RADOS集群

```http
https://mirrors.aliyun.com/ceph/               # 阿里云镜像仓库
http://mirrors.163.com/ceph/                   # 网易镜像仓库
https://mirrors.tuna.tsinghua.edu.cn/ceph/     # 清华大学镜像源 
```



#### 仓库准备

各节点配置cephyum仓库

导入key文件

```bash
# 支持https 镜像仓库源
[root@ceph-node1 ~]# apt install -y apt-transport-https ca-certificates curl software-properties-common

# 导入key
[root@ceph-node1 ~]# wget -q -O- 'https://mirrors.tuna.tsinghua.edu.cn/ceph/keys/release.asc' | sudo apt-key add -

# Ubuntu2204 
# echo "deb https://mirrors.tuna.tsinghua.edu.cn/ceph/[ceph版本] [Ubuntu版本] main" >> /etc/apt/sources.list
[root@ceph-node1 ~]# echo "deb https://mirrors.tuna.tsinghua.edu.cn/ceph/debian-reef jammy main" >> /etc/apt/sources.list
[root@ceph-node1 ~]# apt update

# 更新后查看
[root@ceph-deploy ~]# apt-cache madison ceph
      # 确保有 18.2.x 版本的 ceph
      ceph | 18.2.8-1jammy | https://mirrors.tuna.tsinghua.edu.cn/ceph/debian-reef jammy/main amd64 Packages
      ceph | 17.2.9-0ubuntu0.22.04.3 | http://mirrors.aliyun.com/ubuntu jammy-updates/main amd64 Packages
      ceph | 17.2.9-0ubuntu0.22.04.2 | http://mirrors.aliyun.com/ubuntu jammy-security/main amd64 Packages
      ceph | 17.1.0-0ubuntu3 | http://mirrors.aliyun.com/ubuntu jammy/main amd64 Packages
```



#### 创建 ceph 集群部署用户cephadmin

推荐使用指定的普通用户部署和运行 ceph 集群，普通用户只要能以非交互方式执行 sudo 命令执行一些特权命令即可，新版的 ceph-deploy 可以指定包含 root 的在内只要可以执 行 sudo 命令的用户，不过仍然推荐使用普通用户，

**ceph集群安装完成后会自动创建 ceph 用户(ceph集群默认会使用ceph用户运行各服务进程,如ceph-osd等)，因此推荐 使用除了 ceph 用户之外的比如 cephuser、cephadmin 这样的普通用户去部署和 管理 ceph 集群。**

> cephadmin 仅用于通过ceph-deploy部署和管理 ceph集群的时候使用，比如首次初始 化集群和部署集群、添加节点、删除节点等， ceph 集群在node节点、mgr等节点会使用 ceph 用户启动服务进程。



**在包含ceph-deploy节点的存储节点、mon节点和mgr节点等创建cephadmin用户**。

```bash
# 仅在部署节点：ceph-deploy 创建即可
# Ubuntu
[root@ceph-deploy ~]# groupadd -r -g 2088 cephadmin && useradd -r -m -s /bin/bash -u 2088 -g 2088 cephadmin && echo cephadmin:123456 | chpasswd

# Centos
[root@ceph-deploy ~]# groupadd cephadmin -g 2088 && useradd -u 2088 -g 2088 cephadmin && echo "123456" | passwd --stdin cephadmin
```



**各服务器允许cephadmin用户以sudo执行特权命令**：

```bash
[root@ceph-deploy ~]# echo "cephadmin ALL=(ALL)    NOPASSWD: ALL" >> /etc/sudoers
```



#### **配置免秘钥登录**	

在ceph-deploy 节点配置秘钥分发，允许cephadmin用户以非交互的方式登录到各ceph node/mon/mgr 节点进行集群部署及管理操作，即在ceph-deploy节点生成秘钥对，然后分发公钥到各被管理节点

```bat
cephadmin@ceph-deploy:~$ ssh root@10.0.0.51
cephadmin@ceph-deploy:~$ ssh-copy-id 127.0.0.1

cephadmin@ceph-deploy:~$ for i in {52..60} ;do scp -r .ssh root@10.0.0.${i}: ;done
cephadmin@ceph-deploy:~$ for i in {52..60} ;do scp -r .ssh cephadmin@10.0.0.${i}: ;done
```



#### **配置主机名解析**

```bash
[root@ceph-deploy ~]# cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 mystical

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

10.0.0.51 ceph-node1.mystical.org ceph-node1
10.0.0.52 ceph-node2.mystical.org ceph-node2
10.0.0.53 ceph-node3.mystical.org ceph-node3
10.0.0.54 ceph-node4.mystical.org ceph-node4
10.0.0.55 ceph-mon1.mystical.org  ceph-mon1
10.0.0.56 ceph-mon2.mystical.org  ceph-mon2
10.0.0.57 ceph-mon3.mystical.org  ceph-mon3
10.0.0.58 ceph-mgr1.mystical.org  ceph-mgr1
10.0.0.59 ceph-mgr2.mystical.org  ceph-mgr2
10.0.0.60 ceph-deploy.mystical.org  ceph-deploy
```



#### **安装 Ceph 部署工具**

在ceph部署服务器安装部署工具ceph-deploy

```bash
# Ubuntu2004/2204
cephadmin@ceph-deploy:~$ sudo apt install python2
cephadmin@ceph-deploy:~$ sudo curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1863k  100 1863k    0     0  2546k      0 --:--:-- --:--:-- --:--:-- 2545k

cephadmin@ceph-deploy:~$ sudo pip2 install ceph-deploy
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
Collecting ceph-deploy
  Downloading ceph-deploy-2.0.1.tar.gz (115 kB)
     |████████████████████████████████| 115 kB 644 kB/s 
Requirement already satisfied: setuptools in /usr/local/lib/python2.7/dist-packages (from ceph-deploy) (44.1.1)
Building wheels for collected packages: ceph-deploy
  Building wheel for ceph-deploy (setup.py) ... done
  Created wheel for ceph-deploy: filename=ceph_deploy-2.0.1-py2-none-any.whl size=164051 sha256=1b5f7635c5a254f704632f499740ffeb04f1823c680b8daeeb98d3f11371a2e3
  Stored in directory: /root/.cache/pip/wheels/8a/ee/43/0104e60a63fc7c2151ff055a0b099a8b854b89b98c5198c3c9
Successfully built ceph-deploy
Installing collected packages: ceph-deploy
Successfully installed ceph-deploy-2.0.1       # 装完之后要求 ceph-deploy版本2.0.1即可

# 测试命令是否能执行
cephadmin@ceph-deploy:~$ ceph-deploy --help

# CentOS
[cephadmin@ceph-deploy ~]$ sudo yum install ceph-deploy python-setuptools python2-subprocess3
```



#### **初始化 mon 节点**

在管理节点初始化mon节点

```bash
cephadmin@ceph-deploy:~$ mkdir ceph-cluster    # 保存当前集群的初始化配置信息
cephadmin@ceph-deploy:~$ cd ceph-cluster
```

**ceph-deploy 命令详解**

```bash
$ ceph-deploy--help

# new: 开始部署一个新的 ceph 存储集群，并生成 CLUSTER.conf 集群配置文件和 keyring 认证文件。
# install: 在远程主机上安装ceph相关的软件包, 可以通过--release指定安装的版本。
# rgw：管理 RGW 守护程序(RADOSGW,对象存储网关)。
# mgr：管理 MGR 守护程序(ceph-mgr,Ceph Manager DaemonCeph管理器守护程序)。
# mds：管理 MDS 守护程序(CephMetadataServer，ceph源数据服务器)。
# mon：管理 MON 守护程序(ceph-mon,ceph监视器)。
# gatherkeys：从指定获取提供新节点的验证keys，这些keys会在添加新的MON/OSD/MD加入的时候使用。
# disk：管理远程主机磁盘。
# osd：在远程主机准备数据磁盘，即将指定远程主机的指定磁盘添加到ceph集群作为osd使用。
# repo： 远程主机仓库管理。
# admin：推送 ceph 集群配置文件和 client.admin 认证文件到远程主机。
# config：将 ceph.conf 配置文件推送到远程主机或从远程主机拷贝
# uninstall：从远端主机删除安装包。
# purgedata：从/var/lib/ceph 删除 ceph 数据,会删除/etc/ceph 下的内容。
# purge: 删除远端主机的安装包和所有数据。
# forgetkeys：从本地主机删除所有的验证keyring, 包括client.admin,monitor, bootstrap 等认证文件。
# pkg： 管理远端主机的安装包。
# calamari：安装并配置一个calamari web节点，calamari是一个web 监控平台。
```

初始化mon节点过程如下:

```bash
# Ubuntu 各服务器需要单独安装Python2
[root@ceph-node1 ~]# apt install python2.7 -y
[root@ceph-node1 ~]# ln -sv /usr/bin/python2.7 /usr/bin/python2

# 集群初始化，加入mon节点
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy new --cluster-network 192.168.23.0/24 --public-network 10.0.0.0/24 ceph-mon1
[ceph_deploy.conf][DEBUG ] found configuration file at: /home/cephadmin/.cephdeploy.conf
[ceph_deploy.cli][INFO  ] Invoked (2.0.1): /usr/local/bin/ceph-deploy new --cluster-network 192.168.23.0/24 --public-network 10.0.0.0/24 ceph-mon1
[ceph_deploy.cli][INFO  ] ceph-deploy options:
[ceph_deploy.cli][INFO  ]  username                      : None
[ceph_deploy.cli][INFO  ]  verbose                       : False
[ceph_deploy.cli][INFO  ]  overwrite_conf                : False
[ceph_deploy.cli][INFO  ]  quiet                         : False
[ceph_deploy.cli][INFO  ]  cd_conf                       : <ceph_deploy.conf.cephdeploy.Conf instance at 0x7f44324ed550>
[ceph_deploy.cli][INFO  ]  cluster                       : ceph
[ceph_deploy.cli][INFO  ]  ssh_copykey                   : True
[ceph_deploy.cli][INFO  ]  mon                           : ['ceph-mon1']
[ceph_deploy.cli][INFO  ]  func                          : <function new at 0x7f44318d0ad0>
[ceph_deploy.cli][INFO  ]  public_network                : 10.0.0.0/24
[ceph_deploy.cli][INFO  ]  ceph_conf                     : None
[ceph_deploy.cli][INFO  ]  cluster_network               : 192.168.23.0/24
[ceph_deploy.cli][INFO  ]  default_release               : False
[ceph_deploy.cli][INFO  ]  fsid                          : None
[ceph_deploy.new][DEBUG ] Creating new cluster named ceph
[ceph_deploy.new][INFO  ] making sure passwordless SSH succeeds
[ceph-mon1][DEBUG ] connected to host: ceph-deploy.mystical.org 
[ceph-mon1][INFO  ] Running command: ssh -CT -o BatchMode=yes ceph-mon1
[ceph_deploy.new][WARNIN] could not connect via SSH
[ceph_deploy.new][INFO  ] will connect again with password prompt
The authenticity of host 'ceph-mon1 (10.0.0.55)' can't be established.
ED25519 key fingerprint is SHA256:SCqNIBsqP4p0k3RgAhUXZOvIA8vcNO10/BEZcueB1C4.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:1: [hashed name]
    ~/.ssh/known_hosts:4: [hashed name]
    ~/.ssh/known_hosts:5: [hashed name]
    ~/.ssh/known_hosts:6: [hashed name]
    ~/.ssh/known_hosts:7: [hashed name]
    ~/.ssh/known_hosts:8: [hashed name]
    ~/.ssh/known_hosts:9: [hashed name]
    ~/.ssh/known_hosts:10: [hashed name]
    (3 additional names omitted)
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes      # 首次需要输入yes
Warning: Permanently added 'ceph-mon1' (ED25519) to the list of known hosts.
[ceph-mon1][DEBUG ] connected to host: ceph-mon1 
[ceph-mon1][DEBUG ] detect platform information from remote host
[ceph-mon1][DEBUG ] detect machine type
[ceph_deploy.new][INFO  ] adding public keys to authorized_keys
[ceph-mon1][DEBUG ] append contents to file
[ceph-mon1][DEBUG ] connection detected need for sudo
[ceph-mon1][DEBUG ] connected to host: ceph-mon1 
[ceph-mon1][DEBUG ] detect platform information from remote host
[ceph-mon1][DEBUG ] detect machine type
[ceph-mon1][DEBUG ] find the location of an executable
[ceph-mon1][INFO  ] Running command: sudo /bin/ip link show
[ceph-mon1][INFO  ] Running command: sudo /bin/ip addr show
[ceph-mon1][DEBUG ] IP addresses found: [u'192.168.23.55', u'10.0.0.55']
[ceph_deploy.new][DEBUG ] Resolving host ceph-mon1
[ceph_deploy.new][DEBUG ] Monitor ceph-mon1 at 10.0.0.55
[ceph_deploy.new][DEBUG ] Monitor initial members are ['ceph-mon1']
[ceph_deploy.new][DEBUG ] Monitor addrs are [u'10.0.0.55']
[ceph_deploy.new][DEBUG ] Creating a random mon key...
[ceph_deploy.new][DEBUG ] Writing monitor keyring to ceph.mon.keyring...
[ceph_deploy.new][DEBUG ] Writing initial config to ceph.conf...

# 查看生成的文件
cephadmin@ceph-deploy:~/ceph-cluster$ ll
total 20
drwxrwxr-x 2 cephadmin cephadmin 4096 May 23 13:36 ./
drwxr-x--- 5 cephadmin cephadmin 4096 May 23 12:51 ../
-rw-rw-r-- 1 cephadmin cephadmin 3896 May 23 13:36 ceph-deploy-ceph.log    # 初始化日志
-rw-rw-r-- 1 cephadmin cephadmin  259 May 23 13:36 ceph.conf               # 自动生成的配置文件
-rw------- 1 cephadmin cephadmin   73 May 23 13:36 ceph.mon.keyring        # 用于 ceph mon节点内部通讯认证的秘钥环文件

# 查看 ceph.conf
cephadmin@ceph-deploy:~/ceph-cluster$ cat ceph.conf 
[global]
fsid = f1df489b-7d99-4877-9d84-6326834b74a2    # 自动生成集群id
public_network = 10.0.0.0/24
cluster_network = 192.168.23.0/24
mon_initial_members = ceph-mon1
mon_host = 10.0.0.55
auth_cluster_required = cephx
auth_service_required = cephx
auth_client_required = cephx

# 查看 ceph.mon.keyring -> ceph 的认证文件
cephadmin@ceph-deploy:~/ceph-cluster$ cat ceph.mon.keyring 
[mon.]
key = AQBurRFqAAAAABAAarkV7hsJ8cI8nt5A6QI4KA==
caps mon = allow *    # 表示对 mon 有所有权限

# 此时仅仅生成配置文件，并没有拉起 mon 进程
```



#### **初始化node 节点**

```bash
# 在远程服务器装包
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy install --no-adjust-repos --nogpgcheck ceph-node1 ceph-node2 ceph-node3 ceph-node4
```

```ABAP
# 因为远程服务器必须走代理，才能绕过IP被清华源黑名单的问题，当时解决方案如下
cat >/etc/apt/apt.conf.d/95proxy <<'EOF'
Acquire::http::Proxy "http://代理IP:代理端口/";
Acquire::https::Proxy "http://代理IP:代理端口/";
EOF

# 远程执行期间，有问题的源要注释掉，否则会打断执行
```



#### **安装 ceph-mon 服务**

在各 mon 节点按照组件 ceph-mon ,并通初始化 mon 节点，mon 节点 HA 还可以后期横向扩容。

```bash
# Ubuntu
# 检查
[root@ceph-mon1 ~]# apt-cache madison ceph-mon
  ceph-mon | 18.2.8-1jammy | https://mirrors.tuna.tsinghua.edu.cn/ceph/debian-reef jammy/main amd64 Packages
  ceph-mon | 17.2.9-0ubuntu0.22.04.3 | http://mirrors.aliyun.com/ubuntu jammy-updates/main amd64 Packages
  ceph-mon | 17.2.9-0ubuntu0.22.04.2 | http://mirrors.aliyun.com/ubuntu jammy-security/main amd64 Packages
  ceph-mon | 17.1.0-0ubuntu3 | http://mirrors.aliyun.com/ubuntu jammy/main amd64 Packages
  
# 安装
[root@ceph-mon1 ~]# apt install ceph-mon -y
[root@ceph-mon2 ~]# apt install ceph-mon -y
[root@ceph-mon3 ~]# apt install ceph-mon -y

# CentOS 安装
[root@ceph-mon1 ~]# yum install ceph-mon -y
```



#### **ceph 集群添加 ceph-mon 服务**

```bash
# 初始化 mon 服务器
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy mon create-initial

# 初始化之后会发现当前仅初始化了 10.0.0.55，也就是 ceph-mon1
# 原因在于，我们在 ceph.conf 只指定了ceph-mon1
cephadmin@ceph-deploy:~/ceph-cluster$ cat ceph.conf 
[global]
fsid = f1df489b-7d99-4877-9d84-6326834b74a2
public_network = 10.0.0.0/24
cluster_network = 192.168.23.0/24
mon_initial_members = ceph-mon1   # 这里可以写多个，比如：ceph-mon1,ceph-mon2...，然后下面的地址也需要补全
mon_host = 10.0.0.55              # 比如：10.0.0.55,10.0.0.56，此时则可以同时初始化多个 mon ，这里不加，后期也可以对mon做扩容
auth_cluster_required = cephx
auth_service_required = cephx
auth_client_required = cephx

# 查看生成的文件
cephadmin@ceph-deploy:~/ceph-cluster$ ll
total 336
drwxrwxr-x 2 cephadmin cephadmin   4096 May 23 14:17 ./
drwxr-x--- 5 cephadmin cephadmin   4096 May 23 12:51 ../
-rw-rw-r-- 1 cephadmin cephadmin 301864 May 23 14:17 ceph-deploy-ceph.log
-rw------- 1 cephadmin cephadmin    113 May 23 14:17 ceph.bootstrap-mds.keyring    # MDS 加入集群时使用的 bootstrap 认证 keyring
-rw------- 1 cephadmin cephadmin    113 May 23 14:17 ceph.bootstrap-mgr.keyring    # MGR 加入集群时使用的 bootstrap 认证 keyring
-rw------- 1 cephadmin cephadmin    113 May 23 14:17 ceph.bootstrap-osd.keyring    # OSD 加入集群时使用的 bootstrap 认证 keyring
-rw------- 1 cephadmin cephadmin    113 May 23 14:17 ceph.bootstrap-rgw.keyring    # RGW 对象网关加入集群时使用的 bootstrap 认证 keyring
-rw------- 1 cephadmin cephadmin    151 May 23 14:17 ceph.client.admin.keyring     # Ceph 集群管理员客户端身份认证文件（拥有最高权限）
-rw-rw-r-- 1 cephadmin cephadmin    259 May 23 13:36 ceph.conf
-rw------- 1 cephadmin cephadmin     73 May 23 13:36 ceph.mon.keyring              # MON 集群初始化与 monitor 身份认证使用的 keyring
```



#### 验证 mon节点

验证在 mon 定节点已经自动安装并启动了 ceph-mon 服务，并且后期在 ceph-deploy 节点初始化目录会生成一些 `bootstrap ceph mds/mgr/osd/rgw` 等服务的 keyring 认证文件，这些初始化文件拥有对 ceph 集群的最高权限，所以一定要保存好。

```bash
# 在 ceph-mon1 机器上查看 mon 进程
[root@ceph-mon1 ~]# ps aux|grep ceph
ceph        8971  0.0  0.6  17176 12464 ?        Ss   14:17   0:00 /usr/bin/python3 /usr/bin/ceph-crash
ceph        8972  0.0  2.2 266956 45392 ?        Ssl  14:17   0:00 /usr/bin/ceph-mon -f --cluster ceph --id ceph-mon1 --setuser ceph --setgroup ceph
root        9260  0.0  0.1   4020  2000 pts/1    S+   14:21   0:00 grep --color=auto ceph
```



#### 分发 admin 秘钥

在 ceph-deploy 节点把配置文件和 admin 密钥拷贝至 Ceph 集群需要执行 ceph 管理命令的节点，从而不需要后期通过 ceph 命令对 ceph 集群进行管理配置的时候每次都需要指定 ceph-mon 节点地址和 ceph.client.admin.keyring 文件,另外各 ceph-mon 节点也需要同步 ceph 的集群配置文件与认证文件。

如果在ceph-deploy节点管理集群

```bash
# 先装ceph common -> 想在哪个节点管理ceph集群，就要按照ceph common，有点像kubectl
cephadmin@ceph-deploy:~/ceph-cluster$ sudo apt install ceph-common -y

[root@ceph-node1 ~]# apt install ceph-common -y       # node节点初始化时已经安装了，无需手动再次安装
[root@ceph-node2 ~]# apt install ceph-common -y
[root@ceph-node3 ~]# apt install ceph-common -y
[root@ceph-node4 ~]# apt install ceph-common -y

# 将 admin 认证文件推送到 node 节点
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy admin ceph-node1 ceph-node2 ceph-node3 ceph-node4
[ceph_deploy.conf][DEBUG ] found configuration file at: /home/cephadmin/.cephdeploy.conf
[ceph_deploy.cli][INFO  ] Invoked (2.0.1): /usr/local/bin/ceph-deploy admin ceph-node1 ceph-node2 ceph-node3 ceph-node4
[ceph_deploy.cli][INFO  ] ceph-deploy options:
[ceph_deploy.cli][INFO  ]  username                      : None
[ceph_deploy.cli][INFO  ]  verbose                       : False
[ceph_deploy.cli][INFO  ]  overwrite_conf                : False
[ceph_deploy.cli][INFO  ]  quiet                         : False
[ceph_deploy.cli][INFO  ]  cd_conf                       : <ceph_deploy.conf.cephdeploy.Conf instance at 0x7f482cdea500>
[ceph_deploy.cli][INFO  ]  cluster                       : ceph
[ceph_deploy.cli][INFO  ]  client                        : ['ceph-node1', 'ceph-node2', 'ceph-node3', 'ceph-node4']
[ceph_deploy.cli][INFO  ]  func                          : <function admin at 0x7f482ceb9a50>
[ceph_deploy.cli][INFO  ]  ceph_conf                     : None
[ceph_deploy.cli][INFO  ]  default_release               : False
[ceph_deploy.admin][DEBUG ] Pushing admin keys and conf to ceph-node1
[ceph-node1][DEBUG ] connection detected need for sudo
[ceph-node1][DEBUG ] connected to host: ceph-node1 
[ceph-node1][DEBUG ] detect platform information from remote host
[ceph-node1][DEBUG ] detect machine type
[ceph-node1][DEBUG ] write cluster configuration to /etc/ceph/{cluster}.conf
[ceph_deploy.admin][DEBUG ] Pushing admin keys and conf to ceph-node2
[ceph-node2][DEBUG ] connection detected need for sudo
[ceph-node2][DEBUG ] connected to host: ceph-node2 
[ceph-node2][DEBUG ] detect platform information from remote host
[ceph-node2][DEBUG ] detect machine type
[ceph-node2][DEBUG ] write cluster configuration to /etc/ceph/{cluster}.conf
[ceph_deploy.admin][DEBUG ] Pushing admin keys and conf to ceph-node3
[ceph-node3][DEBUG ] connection detected need for sudo
[ceph-node3][DEBUG ] connected to host: ceph-node3 
[ceph-node3][DEBUG ] detect platform information from remote host
[ceph-node3][DEBUG ] detect machine type
[ceph-node3][DEBUG ] write cluster configuration to /etc/ceph/{cluster}.conf
[ceph_deploy.admin][DEBUG ] Pushing admin keys and conf to ceph-node4
[ceph-node4][DEBUG ] connection detected need for sudo
[ceph-node4][DEBUG ] connected to host: ceph-node4 
[ceph-node4][DEBUG ] detect platform information from remote host
[ceph-node4][DEBUG ] detect machine type
[ceph-node4][DEBUG ] write cluster configuration to /etc/ceph/{cluster}.conf

# 给部署节点 deploy 自己推送下admin，认证文件
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy admin ceph-deploy
[ceph_deploy.conf][DEBUG ] found configuration file at: /home/cephadmin/.cephdeploy.conf
[ceph_deploy.cli][INFO  ] Invoked (2.0.1): /usr/local/bin/ceph-deploy admin ceph-deploy
[ceph_deploy.cli][INFO  ] ceph-deploy options:
[ceph_deploy.cli][INFO  ]  username                      : None
[ceph_deploy.cli][INFO  ]  verbose                       : False
[ceph_deploy.cli][INFO  ]  overwrite_conf                : False
[ceph_deploy.cli][INFO  ]  quiet                         : False
[ceph_deploy.cli][INFO  ]  cd_conf                       : <ceph_deploy.conf.cephdeploy.Conf instance at 0x7f4798977500>
[ceph_deploy.cli][INFO  ]  cluster                       : ceph
[ceph_deploy.cli][INFO  ]  client                        : ['ceph-deploy']
[ceph_deploy.cli][INFO  ]  func                          : <function admin at 0x7f4798a46a50>
[ceph_deploy.cli][INFO  ]  ceph_conf                     : None
[ceph_deploy.cli][INFO  ]  default_release               : False
[ceph_deploy.admin][DEBUG ] Pushing admin keys and conf to ceph-deploy
[ceph-deploy][DEBUG ] connection detected need for sudo
[ceph-deploy][DEBUG ] connected to host: ceph-deploy 
[ceph-deploy][DEBUG ] detect platform information from remote host
[ceph-deploy][DEBUG ] detect machine type
[ceph-deploy][DEBUG ] write cluster configuration to /etc/ceph/{cluster}.conf

# 此时 /etc/ceph 下就会有admin 的认证文件，但此时 ceph 客户端仍无法使用，可以看到文件的属主属组都是root
# 普通用户无法访问
cephadmin@ceph-deploy:~/ceph-cluster$ ll /etc/ceph/
total 20
drwxr-xr-x  2 root root 4096 May 23 14:43 ./
drwxr-xr-x 83 root root 4096 May 23 14:38 ../
-rw-------  1 root root  151 May 23 14:43 ceph.client.admin.keyring
-rw-r--r--  1 root root  259 May 23 14:43 ceph.conf
-rw-r--r--  1 root root   92 Mar 11 23:37 rbdmap
-rw-------  1 root root    0 May 23 14:43 tmp_rhozp

# 为了解决这个问题，可以使用acl -> 访问权限控制
cephadmin@ceph-deploy:~/ceph-cluster$ sudo apt install -y acl
[root@ceph-node1 ~]# apt install acl -y 
[root@ceph-node2 ~]# apt install acl -y 
[root@ceph-node3 ~]# apt install acl -y 
[root@ceph-node4 ~]# apt install acl -y 

cephadmin@ceph-deploy:~/ceph-cluster$ sudo setfacl -m u:cephadmin:rw /etc/ceph/ceph.client.admin.keyring
[root@ceph-node1 ~]# setfacl -m u:cephadmin:rw /etc/ceph/ceph.client.admin.keyring
[root@ceph-node2 ~]# setfacl -m u:cephadmin:rw /etc/ceph/ceph.client.admin.keyring
[root@ceph-node3 ~]# setfacl -m u:cephadmin:rw /etc/ceph/ceph.client.admin.keyring
[root@ceph-node4 ~]# setfacl -m u:cephadmin:rw /etc/ceph/ceph.client.admin.keyring

# 验证，发现成功执行
cephadmin@ceph-deploy:~/ceph-cluster$ ceph -s
  cluster:
    id:     f1df489b-7d99-4877-9d84-6326834b74a2
    health: HEALTH_WARN
            mon is allowing insecure global_id reclaim
 
  services:
    mon: 1 daemons, quorum ceph-mon1 (age 32m)
    mgr: no daemons active
    osd: 0 osds: 0 up, 0 in
 
  data:
    pools:   0 pools, 0 pgs
    objects: 0 objects, 0 B
    usage:   0 B used, 0 B / 0 B avail
    pgs:  
```



#### 部署 MGR 节点

mgr 节点需要读取ceph的配置文件，即/etc/ceph目录中的配置文件

```bash
# 初始化 ceph-mgr 节点
[root@ceph-mgr1 ~]# apt install ceph-mgr -y
[root@ceph-mgr2 ~]# apt install ceph-mgr -y

# 将ceph-mgr1加入集群
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy mgr create ceph-mgr1

# 稍等几秒后查看
cephadmin@ceph-deploy:~/ceph-cluster$ ceph -s
  cluster:
    id:     f1df489b-7d99-4877-9d84-6326834b74a2
    health: HEALTH_WARN
            mon is allowing insecure global_id reclaim
 
  services:
    mon: 1 daemons, quorum ceph-mon1 (age 49m)
    mgr: ceph-mgr1(active, since 6s)              # 要保证这里至少有一个active的mgr
    osd: 0 osds: 0 up, 0 in
 
  data:
    pools:   0 pools, 0 pgs
    objects: 0 objects, 0 B
    usage:   0 B used, 0 B / 0 B avail
    pgs: 
```



#### 验证 ceph-mgr 节点

```bash
[root@ceph-mgr1 ~]# ps -ef | grep ceph
ceph       12536       1  0 15:06 ?        00:00:00 /usr/bin/python3 /usr/bin/ceph-crash
ceph       12538       1  3 15:06 ?        00:00:05 /usr/bin/ceph-mgr -f --cluster ceph --id ceph-mgr1 --setuser ceph --setgroup ceph
root       12693    1604  0 15:09 pts/2    00:00:00 grep --color=auto ceph
```



#### 初始化存储节点

OSD 节点安装运行环境：

```bash
# node节点：Ubuntu 2004、2204 系统单独安装 ceph-volume，否则无法初始化
[root@ceph-node1 ~]# apt install -y ceph-volume
[root@ceph-node2 ~]# apt install -y ceph-volume
[root@ceph-node3 ~]# apt install -y ceph-volume
[root@ceph-node4 ~]# apt install -y ceph-volume

# 安装后会有一个 ceph-volume 的命令，用于擦除管理磁盘。
# 但是不需要我们手动使用，程序会自动调用这个命令。
[root@ceph-node4 ~]# which ceph-volume
/usr/sbin/ceph-volume
```

```bash
# 擦除磁盘之前通过 deploy 节点对 node 节点执行安装 ceph 基本运行环境
# 之前进行 node 节点初始化的时候，已经安装过了，这里不用再次安装
# 之前的初始化没有指定版本，但默认最新版本，所以没啥影响。
# 下面的命令可以手动指定版本，通过 --release <版本>
cephadmin@ceph-deploy:~$ ceph-deploy install --release reef ceph-node1
cephadmin@ceph-deploy:~$ ceph-deploy install --release reef ceph-node2
cephadmin@ceph-deploy:~$ ceph-deploy install --release reef ceph-node3
cephadmin@ceph-deploy:~$ ceph-deploy install --release reef ceph-node4

# 列出 ceph node 节点磁盘
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk list ceph-node1
[ceph_deploy.conf][DEBUG ] found configuration file at: /home/cephadmin/.cephdeploy.conf[ceph_deploy.cli][INFO  ] Invoked (2.0.1): /usr/local/bin/ceph-deploy disk list ceph-node1
[ceph_deploy.cli][INFO  ] ceph-deploy options:
[ceph_deploy.cli][INFO  ]  username                      : None
[ceph_deploy.cli][INFO  ]  verbose                       : False
[ceph_deploy.cli][INFO  ]  debug                         : False
[ceph_deploy.cli][INFO  ]  overwrite_conf                : False
[ceph_deploy.cli][INFO  ]  subcommand                    : list
[ceph_deploy.cli][INFO  ]  quiet                         : False
[ceph_deploy.cli][INFO  ]  cd_conf                       : <ceph_deploy.conf.cephdeploy.Conf instance at 0x7f3830ff8cd0>
[ceph_deploy.cli][INFO  ]  cluster                       : ceph
[ceph_deploy.cli][INFO  ]  host                          : ['ceph-node1']
[ceph_deploy.cli][INFO  ]  func                          : <function disk at 0x7f38310632d0>
[ceph_deploy.cli][INFO  ]  ceph_conf                     : None
[ceph_deploy.cli][INFO  ]  default_release               : False
[ceph-node1][DEBUG ] connection detected need for sudo
[ceph-node1][DEBUG ] connected to host: ceph-node1 
[ceph-node1][DEBUG ] detect platform information from remote host
[ceph-node1][DEBUG ] detect machine type
[ceph-node1][DEBUG ] find the location of an executable
[ceph-node1][INFO  ] Running command: sudo fdisk -l
[ceph-node1][INFO  ] Disk /dev/nvme0n1: 200 GiB, 214748364800 bytes, 419430400 sectors
[ceph-node1][INFO  ] Disk /dev/nvme0n2: 4 TiB, 4398046511104 bytes, 8589934592 sectors
[ceph-node1][INFO  ] Disk /dev/nvme0n3: 4 TiB, 4398046511104 bytes, 8589934592 sectors
[ceph-node1][INFO  ] Disk /dev/nvme0n4: 4 TiB, 4398046511104 bytes, 8589934592 sectors
[ceph-node1][INFO  ] Disk /dev/nvme0n5: 4 TiB, 4398046511104 bytes, 8589934592 sectors
[ceph-node1][INFO  ] Disk /dev/sda: 8 TiB, 8796093022208 bytes, 17179869184 sectors
[ceph-node1][INFO  ] Disk /dev/mapper/ubuntu--vg-ubuntu--lv: 99 GiB, 106296246272 bytes, 207609856 sectors
```

使用 ceph-deploy disk zap 擦除各 ceph node 的 ceph 数据磁盘：

ceph-node1、ceph-node2、ceph-node3 的存储节点磁盘擦除过程如下：

```bash
# 擦除 ceph-node1
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node1 /dev/nvme0n2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node1 /dev/nvme0n3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node1 /dev/nvme0n4
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node1 /dev/nvme0n5
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node1 /dev/sda

# 擦除 ceph-node2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node2 /dev/nvme0n2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node2 /dev/nvme0n3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node2 /dev/nvme0n4
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node2 /dev/nvme0n5
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node2 /dev/sda

# 擦除 ceph-node3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node3 /dev/nvme0n2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node3 /dev/nvme0n3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node3 /dev/nvme0n4
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node3 /dev/nvme0n5
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node3 /dev/sda

# 擦除 ceph-node4
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node4 /dev/nvme0n2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node4 /dev/nvme0n3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node4 /dev/nvme0n4
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node4 /dev/nvme0n5
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy disk zap ceph-node4 /dev/sda
```



#### 添加 OSD

**数据分类保持方式**

- Data：即ceph保存的对象数据
- Block: rocks DB 数据即元数据
- block-wal：数据库的 wal 日志



**添加 OSD**

```bash
# ceph-node1
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node1 --data /dev/nvme0n2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node1 --data /dev/nvme0n3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node1 --data /dev/nvme0n4
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node1 --data /dev/nvme0n5

# ceph-node2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node2 --data /dev/nvme0n2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node2 --data /dev/nvme0n3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node2 --data /dev/nvme0n4
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node2 --data /dev/nvme0n5

# ceph-node3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node3 --data /dev/nvme0n2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node3 --data /dev/nvme0n3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node3 --data /dev/nvme0n4
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node3 --data /dev/nvme0n5

# ceph-node2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node4 --data /dev/nvme0n2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node4 --data /dev/nvme0n3
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node4 --data /dev/nvme0n4
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy osd create ceph-node4 --data /dev/nvme0n5

# 添加后查看
cephadmin@ceph-deploy:~/ceph-cluster$ ceph -s
  cluster:
    id:     f1df489b-7d99-4877-9d84-6326834b74a2
    health: HEALTH_WARN
            mon is allowing insecure global_id reclaim
            Slow OSD heartbeats on back (longest 1241.772ms)
            Slow OSD heartbeats on front (longest 1243.733ms)
 
  services:
    mon: 1 daemons, quorum ceph-mon1 (age 70m)
    mgr: ceph-mgr1(active, since 69m)
    osd: 16 osds: 16 up (since 60s), 16 in (since 72s)  # 16个OSD添加成功
 
  data:
    pools:   1 pools, 1 pgs
    objects: 2 objects, 577 KiB
    usage:   441 MiB used, 64 TiB / 64 TiB avail
    pgs:     1 active+clean
    
# 到 ceph-node 节点查看
[root@ceph-node1 ~]# ps aux|grep osd
ceph       27324  0.4  4.2 961776 83320 ?        Ssl  11:17   0:04 /usr/bin/ceph-osd -f --cluster ceph --id 0 --setuser ceph --setgroup ceph
ceph       28970  0.4  4.0 961780 80416 ?        Ssl  11:20   0:04 /usr/bin/ceph-osd -f --cluster ceph --id 1 --setuser ceph --setgroup ceph
ceph       30595  0.8  4.2 961776 83076 ?        Ssl  11:20   0:07 /usr/bin/ceph-osd -f --cluster ceph --id 2 --setuser ceph --setgroup ceph
ceph       32234  0.7  4.0 961776 79136 ?        Ssl  11:21   0:05 /usr/bin/ceph-osd -f --cluster ceph --id 3 --setuser ceph --setgroup ceph
root       32807  0.0  0.1   4024  2104 pts/0    S+   11:34   0:00 grep --color=auto osd
```

```bash
# 可以看到osd之间会进行相互的心跳检测
[root@ceph-node1 ~]# netstat -ntalp
......
tcp        0      0 10.0.0.51:55878         10.0.0.52:6806          ESTABLISHED 32234/ceph-osd      
tcp        0      0 10.0.0.51:6810          10.0.0.54:45706         ESTABLISHED 30595/ceph-osd      
tcp        0      0 10.0.0.51:6806          10.0.0.54:34164         ESTABLISHED 28970/ceph-osd      
tcp        0      0 192.168.23.51:59522     192.168.23.54:6808      ESTABLISHED 30595/ceph-osd      
tcp        0      0 192.168.23.51:46760     192.168.23.52:6804      ESTABLISHED 27324/ceph-osd      
tcp        0      0 192.168.23.51:6808      192.168.23.52:57594     ESTABLISHED 30595/ceph-osd      
tcp        0      0 192.168.23.51:6808      192.168.23.52:51472     ESTABLISHED 30595/ceph-osd      
tcp        0      0 10.0.0.51:6802          10.0.0.53:49176         ESTABLISHED 27324/ceph-osd      
tcp        0      0 192.168.23.51:6802      192.168.23.54:39074     ESTABLISHED 27324/ceph-osd      
tcp        0      0 192.168.23.51:6808      192.168.23.53:48008     ESTABLISHED 30595/ceph-osd      
tcp        0      0 10.0.0.51:52398         10.0.0.51:6810          ESTABLISHED 28970/ceph-osd      
tcp        0      0 10.0.0.51:6814          10.0.0.51:60268         ESTABLISHED 32234/ceph-osd      
tcp        0      0 10.0.0.51:6810          10.0.0.54:50824         ESTABLISHED 30595/ceph-osd      
tcp        0      0 192.168.23.51:6808      192.168.23.51:60740     ESTABLISHED 30595/ceph-osd      
tcp        0      0 192.168.23.51:6808      192.168.23.52:54236     ESTABLISHED 30595/ceph-osd      
tcp        0      0 192.168.23.51:60214     192.168.23.53:6800      ESTABLISHED 30595/ceph-osd      
```

去掉 mon 的非安全认证

```bash
# 默认是允许 mon 进行非安全认证访问的
# 可以把这个关掉
cephadmin@ceph-deploy:~/ceph-cluster$ ceph config set mon auth_allow_insecure_global_id_reclaim false

# 查看
cephadmin@ceph-deploy:~/ceph-cluster$ ceph -s
  cluster:
    id:     f1df489b-7d99-4877-9d84-6326834b74a2
    health: HEALTH_WARN     # 最好的状态是 HEALTH_OK
            Slow OSD heartbeats on back (longest 1241.772ms)
            Slow OSD heartbeats on front (longest 1243.733ms)
 
  services:
    mon: 1 daemons, quorum ceph-mon1 (age 79m)
    mgr: ceph-mgr1(active, since 78m)
    osd: 16 osds: 16 up (since 10m), 16 in (since 10m)
 
  data:
    pools:   1 pools, 1 pgs
    objects: 2 objects, 577 KiB
    usage:   441 MiB used, 64 TiB / 64 TiB avail
    pgs:     1 active+clean
    
# 查看 osd 的状态
[root@ceph-node2 ~]# ceph osd tree
ID  CLASS  WEIGHT    TYPE NAME            STATUS  REWEIGHT  PRI-AFF
-1         64.00000  root default                                  
-3         16.00000      host ceph-node1                           
 0    ssd   4.00000          osd.0            up   1.00000  1.00000
 1    ssd   4.00000          osd.1            up   1.00000  1.00000
 2    ssd   4.00000          osd.2            up   1.00000  1.00000
 3    ssd   4.00000          osd.3            up   1.00000  1.00000
-5         16.00000      host ceph-node2                           
 4    ssd   4.00000          osd.4            up   1.00000  1.00000
 5    ssd   4.00000          osd.5            up   1.00000  1.00000
 6    ssd   4.00000          osd.6            up   1.00000  1.00000
 7    ssd   4.00000          osd.7            up   1.00000  1.00000
-7         16.00000      host ceph-node3                           
 8    ssd   4.00000          osd.8            up   1.00000  1.00000
 9    ssd   4.00000          osd.9            up   1.00000  1.00000
10    ssd   4.00000          osd.10           up   1.00000  1.00000
11    ssd   4.00000          osd.11           up   1.00000  1.00000
-9         16.00000      host ceph-node4                           
12    ssd   4.00000          osd.12           up   1.00000  1.00000
13    ssd   4.00000          osd.13           up   1.00000  1.00000
14    ssd   4.00000          osd.14           up   1.00000  1.00000
15    ssd   4.00000          osd.15           up   1.00000  1.00000
```



#### 从 RADOS 移除OSD

Ceph 集群中的一个 OSD 是一个 node 节点的服务进程且对应于一个物理磁盘设备，是一个专用的守护进程。在某 OSD 设备出现故障，或管理员出于管理之需确实要移除特定的 OSD 设备时，需要先停止相关的守护进程，而后再进行移除操作。对于 Luminous 及其之后的版 本来说，停止和移除命令的格式分别如下所示：

```bash
# 停用设备，此时 mon 会将该 osd 提出集群，数据后续不会再调度过去
ceph osd out {osd-num}

# 停止进程
systemctl stop ceph-osd@{osd-num}

# 移除设备
ceph osd purge {id} --yes-i-really-mean-it
```

不过，对于 **Luminous 之前的版本**来说，管理员需要依次手动执行如下步骤删除OSD设备

```bash
# 于 CRUSH 运行图中移除设备：
ceph osd crush remove {name}

# 移除 OSD 的认证 key
ceph auth del osd.{osd-num}

# 最后移除 OSD 设备
ceph osd rm {osd-num}
```



#### 测试上传与下载数据

存取数据时，客户端必须首先连接至 RADOS 集群上某存储池，然后根据对象名称由相关的 CRUSH 规则完成数据对象寻址。于是，为了测试集群的数据存取功能，这里首先创建一个用于测试的存储池 mypool，并设定其 PG 数量为 32 个。



创建 pool 存储池

```bash
# 创建名为 mypool 的存储池，设置PG=32,PGP=32
# 即逻辑上 PG 的数量是32，而实际参与数据分布的 PG 数量也是32
cephadmin@ceph-deploy:~/ceph-cluster$ ceph osd pool create mypool 32 32
pool 'mypool' created

# 验证PG 与 PGP 组合
# PG 2.0~2.1f -> <pool_id>.<pg_index>
# pool_id 只会递增，不会复用
ceph pg ls-by-pool mypool | awk '{print $1,$2,$15}' 
cephadmin@ceph-deploy:~/ceph-cluster$ ceph pg ls-by-pool mypool | awk '{print $1,$2,$15}'
PG OBJECTS UP
2.0 0 [7,10,3]p7
2.1 0 [14,0,8]p14
2.2 0 [5,1,14]p5
2.3 0 [14,5,9]p14
2.4 0 [1,10,15]p1
2.5 0 [8,0,4]p8
2.6 0 [1,8,14]p1
2.7 0 [6,13,2]p6
2.8 0 [12,9,0]p12
2.9 0 [1,7,14]p1
2.a 0 [11,3,15]p11
2.b 0 [8,7,12]p8
2.c 0 [11,0,5]p11
2.d 0 [9,13,3]p9
2.e 0 [2,9,13]p2
2.f 0 [8,13,4]p8
2.10 0 [15,8,0]p15
2.11 0 [15,6,1]p15
2.12 0 [10,3,7]p10
2.13 0 [15,4,3]p15
2.14 0 [6,9,12]p6
2.15 0 [14,1,8]p14
2.16 0 [5,11,12]p5
2.17 0 [6,13,2]p6
2.18 0 [12,9,0]p12
2.19 0 [1,7,14]p1
2.1a 0 [11,3,15]p11
2.1b 0 [8,7,12]p8
2.1c 0 [11,0,5]p11
2.1d 0 [9,13,3]p9
2.1e 0 [2,9,13]p2
2.1f 0 [8,13,4]p8
  
* NOTE: afterwards

# 查看集群中的pool
# .mgr 是 MGR 内部数据存储池，里面存了 dashboard 信息，mgr module 状态等信息
# ceph 本质是 “Ceph 集群控制面客户端”
cephadmin@ceph-deploy:~/ceph-cluster$ ceph osd pool ls
.mgr
mypool

# rados 本质是 “RADOS 对象存储客户端”，直接操作对象 object
cephadmin@ceph-deploy:~/ceph-cluster$ rados lspools
.mgr
mypool

# 查看ceph状态
cephadmin@ceph-deploy:~/ceph-cluster$ ceph -s
  cluster:
    id:     f1df489b-7d99-4877-9d84-6326834b74a2
    health: HEALTH_WARN
            # 此时pool没有初始化完成，此时既不是块也不是文件存储也不是对象存储，但不影响后续测试
            1 pool(s) do not have an application enabled  
 
  services:
    mon: 1 daemons, quorum ceph-mon1 (age 3h)
    mgr: ceph-mgr1(active, since 3h)
    osd: 16 osds: 16 up (since 2h), 16 in (since 2h)
 
  data:
    pools:   2 pools, 33 pgs
    objects: 2 objects, 577 KiB
    usage:   450 MiB used, 64 TiB / 64 TiB avail
    pgs:     33.333% pgs unknown
             21.212% pgs not active
             15 active+clean
             11 unknown
             7  creating+peering
```

当前的ceph环境还没还没有部署使用块存储和文件系统使用ceph，也没有使用对象存储 的客户端，但是ceph的rados命令可以实现访问ceph对象存储的功能：

```bash
# 上传文件
# #把 messages 文件上传到 mypool 并指定对象id为 msg1
cephadmin@ceph-deploy:~/ceph-cluster$ rados put msg1 /var/log/lastlog --pool=mypool

# 列出文件
cephadmin@ceph-deploy:~/ceph-cluster$ rados ls --pool=mypool
msg1

# 查看文件信息
# 表示文件放在了存储池id为3的 c833d430 的 PG 上，10为当前PG的id,2.10表示数据是在id为2的存储池当中id为10的PG中存储
# 在线的OSD编号 15,13,10，主OSD为5，活动的OSD15,13,10，三个OSD表示数据放一共3个副本，PG中的OSD是ceph的 crush 算法计算出三份数据保存在哪些OSD
cephadmin@ceph-deploy:~/ceph-cluster$ ceph osd map mypool msg1
osdmap e128 pool 'mypool' (3) object 'msg1' -> pg 3.c833d430 (3.10) -> up ([12,9,5], p12) acting ([12,9,5], p12)

# 下载文件
ephadmin@ceph-deploy:~/ceph-cluster$ sudo rados get msg1 --pool=mypool /opt/my.txt

# 查看
cephadmin@ceph-deploy:~/ceph-cluster$ ls /opt
my.txt

# 修改文件，就是重新上传
cephadmin@ceph-deploy:~/ceph-cluster$ sudo rados put msg1 /etc/passwd --pool=mypool	

# 再次下载验证
cephadmin@ceph-deploy:~/ceph-cluster$ sudo rados get msg1 --pool=mypool /opt/2.txt
cephadmin@ceph-deploy:~/ceph-cluster$ tail /opt/2.txt 
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:107:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
mystical:x:1000:1000:mystical:/home/mystical:/bin/bash
cephadmin:x:2088:2088::/home/cephadmin:/bin/bash
ceph:x:64045:64045:Ceph storage service:/var/lib/ceph:/usr/sbin/nologin

# 删除文件
cephadmin@ceph-deploy:~/ceph-cluster$ sudo rados rm msg1 --pool=mypool
cephadmin@ceph-deploy:~/ceph-cluster$ rados ls --pool=mypool
```

删除 pool

```bash
# 默认是不能直接删的,需要开启允许删除 pool
cephadmin@ceph-deploy:~/ceph-cluster$ ceph config set mon mon_allow_pool_delete true

# 删除 pool
# 这里写两次 mypool，第二个 mypool 的目的是防止误删确认。
ceph osd pool delete mypool mypool --yes-i-really-really-mean-it
```



## 扩展 ceph 集群实现高可用

主要是扩展ceph集群的mon节点以及mgr节点，以实现集群高可用。

### 扩展 ceph-mon 节点

Ceph-mon 是原生具备自选举以实现高可用机制的 ceph 服务，节点数量通常是奇数。

```bash
# 在 mon 节点安装 ceph-mon
# Ubuntu
[root@ceph-mon2 ~]# apt install -y ceph-mon
[root@ceph-mon3 ~]# apt install -y ceph-mon

# Centos
[root@ceph-mon2 ~]# yum install -y ceph-mon

# 然后使用 ceph-deploy mon add 添加 mon2 和 mon3 到集群
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy mon add ceph-mon2
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy mon add ceph-mon3
```

```bash 
# 查看 mon 的当前状态
cephadmin@ceph-deploy:~/ceph-cluster$ ceph quorum_status --format json-pretty

{
    "election_epoch": 14,
    "quorum": [
        0,
        1,
        2
    ],
    "quorum_names": [
        "ceph-mon1",
        "ceph-mon2",
        "ceph-mon3"
    ],
    "quorum_leader_name": "ceph-mon1",
    "quorum_age": 140,
    "features": {
        "quorum_con": "4540138322906710015",
        "quorum_mon": [
            "kraken",
            "luminous",
            "mimic",
            "osdmap-prune",
            "nautilus",
            "octopus",
            "pacific",
            "elector-pinging",
            "quincy",
            "reef"
        ]
    },
    "monmap": {
        "epoch": 3,
        "fsid": "f1df489b-7d99-4877-9d84-6326834b74a2",
        "modified": "2026-05-24T14:32:25.441504Z",
        "created": "2026-05-23T14:17:16.996415Z",
        "min_mon_release": 18,
        "min_mon_release_name": "reef",
        "election_strategy": 1,
        "disallowed_leaders": "",
        "stretch_mode": false,
        "tiebreaker_mon": "",
        "removed_ranks": "",
        "features": {
            "persistent": [
                "kraken",
                "luminous",
                "mimic",
                "osdmap-prune",
                "nautilus",
                "octopus",
                "pacific",
                "elector-pinging",
                "quincy",
                "reef"
            ],
            "optional": []
        },
        "mons": [
            {
                "rank": 0,
                "name": "ceph-mon1",
                "public_addrs": {
                    "addrvec": [
                        {
                            "type": "v2",
                            "addr": "10.0.0.55:3300",
                            "nonce": 0
                        },
                        {
                            "type": "v1",
                            "addr": "10.0.0.55:6789",
                            "nonce": 0
                        }
                    ]
                },
                "addr": "10.0.0.55:6789/0",
                "public_addr": "10.0.0.55:6789/0",
                "priority": 0,
                "weight": 0,
                "crush_location": "{}"
            },
            {
                "rank": 1,
                "name": "ceph-mon2",
                "public_addrs": {
                    "addrvec": [
                        {
                            "type": "v2",
                            "addr": "10.0.0.56:3300",
                            "nonce": 0
                        },
                        {
                            "type": "v1",
                            "addr": "10.0.0.56:6789",
                            "nonce": 0
                        }
                    ]
                },
                "addr": "10.0.0.56:6789/0",
                "public_addr": "10.0.0.56:6789/0",
                "priority": 0,
                "weight": 0,
                "crush_location": "{}"
            },
            {
                "rank": 2,
                "name": "ceph-mon3",
                "public_addrs": {
                    "addrvec": [
                        {
                            "type": "v2",
                            "addr": "10.0.0.57:3300",
                            "nonce": 0
                        },
                        {
                            "type": "v1",
                            "addr": "10.0.0.57:6789",
                            "nonce": 0
                        }
                    ]
                },
                "addr": "10.0.0.57:6789/0",
                "public_addr": "10.0.0.57:6789/0",
                "priority": 0,
                "weight": 0,
                "crush_location": "{}"
            }
        ]
    }
}

# 验证 ceph-mon 状态
cephadmin@ceph-deploy:~/ceph-cluster$ ceph -s
  cluster:
    id:     f1df489b-7d99-4877-9d84-6326834b74a2
    health: HEALTH_WARN
            1 pool(s) do not have an application enabled
 
  services:
    mon: 3 daemons, quorum ceph-mon1,ceph-mon2,ceph-mon3 (age 37s)  # 这里显示3个ceph-mon
    mgr: ceph-mgr1(active, since 4h)
    osd: 16 osds: 16 up (since 3h), 16 in (since 3h)
 
  data:
    pools:   2 pools, 33 pgs
    objects: 2 objects, 577 KiB
    usage:   504 MiB used, 64 TiB / 64 TiB avail
    pgs:     33 active+clean
    
# 修改 ceph.conf 文件，将其重新分发给 ceph-node 节点
cephadmin@ceph-deploy:~/ceph-cluster$ cat ceph.conf 
[global]
fsid = f1df489b-7d99-4877-9d84-6326834b74a2
public_network = 10.0.0.0/24
cluster_network = 192.168.23.0/24
mon_initial_members = ceph-mon1,ceph-mon2,ceph-mon3    # 增加新添加的ceph-mon2,ceph-mon3
mon_host = 10.0.0.55,10.0.0.56,10.0.0.57               # 添加ceph-mon2和ceph-mon3的public iP
auth_cluster_required = cephx
auth_service_required = cephx
auth_client_required = cephx  

# 重新推送给 ceph-node，ceph-mon，ceph-mgr，注意覆盖旧文件
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy --overwrite-conf admin ceph-node1 ceph-node2 ceph-node3 ceph-node4
```



### 扩展 MGR 节点

```bash
# 在 mgr 节点安装
[root@ceph-mgr2 ~]# apt install ceph-mgr -y

# 添加
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy mgr create ceph-mgr2

# 同步配置文件到 ceph-mon，ceph-mgr 节点
cephadmin@ceph-deploy:~/ceph-cluster$ ceph-deploy --overwrite-conf admin ceph-mon1 ceph-mon2 ceph-mon3 ceph-mgr1 ceph-mgr2

# 验证 mgr 节点状态
cephadmin@ceph-deploy:~/ceph-cluster$ ceph -s
  cluster:
    id:     f1df489b-7d99-4877-9d84-6326834b74a2
    health: HEALTH_WARN
            1 pool(s) do not have an application enabled
 
  services:
    mon: 3 daemons, quorum ceph-mon1,ceph-mon2,ceph-mon3 (age 5m)
    mgr: ceph-mgr1(active, since 4h), standbys: ceph-mgr2         # 这里能看到 ceph-mgr2
    osd: 16 osds: 16 up (since 3h), 16 in (since 3h)
 
  data:
    pools:   2 pools, 33 pgs
    objects: 2 objects, 577 KiB
    usage:   504 MiB used, 64 TiB / 64 TiB avail
    pgs:     33 active+clean
```





# Ceph 集群应用基础

ceph 的集群应用

![image-20260524223929973](D:\git_repository\cyber_security_learning\markdown_img\image-20260524223929973.png)



## 块存储（RDB）基础

RBD(RADOS Block Devices)即为块存储设备，RBD可以为KVM、vmware等虚拟化技术和云服务（如OpenStack、kubernetes）提供高性能和无限可扩展性的存储后端，客户端基于 librbd 库即可将 RADOS 存储集群用作块设备，不过，用于 rbd 的存储池需要事先启用 rbd 功能并进行初始化。例如，下面的命令创建一个名为 myrbd1的存储池，并在启用 rbd 功能后对其进行初始化



### 创建 RBD

具体 RBD使用会在第六章详细介绍

```bash
# 创建存储池命令格式
# ceph osd pool create <poolname> pg_num pgp_num {replicated|erasure}

# 创建存储池,指定pg和pgp的数量，pgp是对存在于pg的数据进行组合存储，pgp通常等于pg的值
cephadmin@ceph-deploy:~/ceph-cluster$ ceph osd pool create myrbd1 64 64
pool 'myrbd1' created

# 对存储池启用 RBD功能
cephadmin@ceph-deploy:~/ceph-cluster$ ceph osd pool application enable myrbd1 rbd
enabled application 'rbd' on pool 'myrbd1'

# 通过 RBD 命令对存储池初始化
cephadmin@ceph-deploy:~/ceph-cluster$ rbd pool init -p myrbd1
```



### 创建并验证 img

不过，rbd存储池并不能直接用于块设备，而是需要事先在其中按需创建映像（image）， 并把映像文件作为块设备使用，rbd命令可用于创建、查看及删除块设备相在的映像 （image），以及克隆映像、创建快照、将映像回滚到快照和查看快照等管理操作，例如， 下面的命令能够创建一个名为myimg1的映像：

```bash
# 创建 image
cephadmin@ceph-deploy:~/ceph-cluster$ rbd create myimg1 --size 5G --pool myrbd1
cephadmin@ceph-deploy:~/ceph-cluster$ rbd create myimg2 --size 3G --pool myrbd1 --image-format 2 --image-feature layering

# 列出指定 pool 中所有的 img
cephadmin@ceph-deploy:~/ceph-cluster$ rbd ls --pool myrbd1
myimg1
myimg2

# 查看 img 的特性
cephadmin@ceph-deploy:~/ceph-cluster$ rbd --image myimg1 --pool myrbd1 info
rbd image 'myimg1':
        size 5 GiB in 1280 objects
        order 22 (4 MiB objects)
        snapshot_count: 0
        id: 3990ff239741
        block_name_prefix: rbd_data.3990ff239741
        format: 2
        # 如果不指定特性，默认会有很多默认特性，部分内核版本较低的操作系统，可能因为内核不支持，导致无法挂载
        features: layering, exclusive-lock, object-map, fast-diff, deep-flatten   
        op_features: 
        flags: 
        create_timestamp: Sun May 24 15:06:41 2026
        access_timestamp: Sun May 24 15:06:41 2026
        modify_timestamp: Sun May 24 15:06:41 2026
        
cephadmin@ceph-deploy:~/ceph-cluster$ rbd --image myimg2 --pool myrbd1 info
rbd image 'myimg2':
        size 3 GiB in 768 objects
        order 22 (4 MiB objects)
        snapshot_count: 0
        id: 3999163b2cc1
        block_name_prefix: rbd_data.3999163b2cc1
        format: 2
        features: layering
        op_features: 
        flags: 
        create_timestamp: Sun May 24 15:07:14 2026
        access_timestamp: Sun May 24 15:07:14 2026
        modify_timestamp: Sun May 24 15:07:14 2026
```



### 客户端使用块存储

```bash
# 当前 ceph 状态
cephadmin@ceph-deploy:~/ceph-cluster$ ceph df
--- RAW STORAGE ---
CLASS    SIZE   AVAIL     USED  RAW USED  %RAW USED
ssd    64 TiB  64 TiB  454 MiB   454 MiB          0
TOTAL  64 TiB  64 TiB  454 MiB   454 MiB          0
 
--- POOLS ---
POOL    ID  PGS   STORED  OBJECTS     USED  %USED  MAX AVAIL
.mgr     1    1  2.3 MiB        2  6.8 MiB      0     20 TiB       # 这里是除以3副本后的容量，即64/3
myrbd1   4   64    405 B        8   48 KiB      0     20 TiB
```



#### 在客户端安装 ceph-common

```bash
```





