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



## 认识Docker

- 基于Linux内核的**Cgroup**，**Namespace**，以及**Union FS**等技术，对进程进行封装隔离，属于操作系统层面的虚拟化技术，由于隔离的进程独立于宿主和其他的隔离的进程，因此也称其为容器



- 最初实现是基于**LXC**，从0.7以后开始去除LXC,，转而使用自行开发的**Libcontainer**，从1.11开始，则进一步演进为使用**Runc**和**Containerd**。



- Docker在容器的基础上，进行了进一步封装，从文件系统、网络互联到进程隔离等等，极大的简化了容器的创建和维护，使得Docker技术比虚拟机技术更为轻便、快捷。





### 为什么要用Docker



![image-20250103094450293](D:\git_repository\cyber_security_learning\markdown_img\image-20250103094450293.png)



- **更高效地利用系统资源**

  ```ABAP
  相对于虚拟机还说，虚拟机是要虚拟操作系统，而操作系统本身是有开销的，通常一开机几百M内存就没了。
  容器技术基于Linux Kernel的Namespace和CGroup技术，它共享host的Kernel，它不需要额外占用很多资源来模拟操作系统
  从整体来看，企业的所有资源是给应用使用的，容器最终是跑应用的，所以它整体的资源利用率是高的
  ```

  

- **更快速的启动速度**

  ```ABAP
  正因为容器不需要模拟一个操作系统，因此它没有操作系统的启动时间，它没有boot，所以它启动更快
  ```

  

- **一致的运行环境**

  ```ABAP
  又因为它有Namespace这个技术，有了OverlayFS这个技术，使得这个容器可以构建成镜像，可以被分发到不同环境
  当你运行这个镜像，本质上是把这个镜像重放了一遍，所以在测试环境能够运行的程序，在其他环境一定也能运行
  因为容器在运行的时候，里面提供了一个完全封装掉，跟外面隔离的环境，既然是隔离环境，它就仿佛是一个箱子，这个箱子在这里打开和别的地方打开它里面的东西一定是一样的，它自身能够提供一致的运行环境
  ```

  

- **持续交付和部署**

  ```ABAP
  有了一致性的运行环境，就很容易迁移。而有了一致性运行环境的特性，持续交付和持续部署就很简单了。持续部署无非就是将这个盒子在不同的房间打开一遍，这就是持续部署
  ```

  

- **更轻松地迁移**

- **更轻松地维护和扩展**





### Docker三大技术



- **NameSpace**
- **Cgroup**
- **OverlayFS**



#### NameSpace

跟真实存在的虚拟机不同，在使用Docker的时候，并没有一个真正的“Docker容器”运行在宿主机里面。Docker项目帮助用户启动的，还是原来的应用进程，只不过创建这些进程时，Docker为他们加上了各种各样的Namespace参数

这时，这些进程就会觉得自己是各自PID Namespace里的第1号进程，只能看到各自Mount Namespace里挂载的目录和文件，只能访问到各自Network Namespace里的网络设备，就仿佛运行在一个个容器里面，与世隔绝。

- Linux Namespace是一种Linux Kernel提供的资源隔离方案
  - 系统可以为进程分配不同的Namespace
  - 并保证不同的Namespace资源独立分配，进程彼此隔离，即不同的Namespace下的进程互不干扰

##### Linux内核代码中Namespace的实现

```C
// 进程数据结构
struct task_struct {
    ...
    /* namesapce */
    struct nsproxy *nsproxy;
    ...
}

// Namespace数据结构
struct nsproxy {
    atomic_t count;
    struct uts_namespace *uts_ns;
    struct ipc_namespace *ipc_ns;
    struct mnt_namespace *mnt_ns;
    struct pid_namespace *pid_ns_for_children;
    struct net_namespace *net_ns;
}
```



##### Linux对Namespace操作的方法

一个进程是如何分Namespace的？

- 首先第一个进程(systemd)，pid为1的进程，它会被分配一个默认的Namespace

- 当init进程要起其他进程的时候，fork或者clone

  - clone(在clone的时候是可以指定新的Namespace的)

    - 在创建新进程的系统调用时，可以通过flags参数指定新建的Namespace类型：

    ```C
    // CLONE_NEWCGROUPS / CLONE_NEWPIC / CLONE_NEWNET / CLONE_NEWNS / CLONE_NEWPID / CLONE_NEWUSER / CLONE_NEWUTS
    int clone(int(*fn)(void*), void*child_stack, int flags, void *arg)
    ```

  - setns

    - 该系统调用可以让调用进程加入某个已经存在的Namespace中

    ```C
    int setns(int fd, int nstype)
    ```

  - unshare

    - 该系统调用可以将调用进程移动到新的Namespace下：

    ```C
    int unshare(int flags)
    ```



##### PID Namespace

- 不同用户的进程就是通过Pid Namespace隔离开的，且不同Namespace中可以有相同pid
- 有了Pid Namespace，每个namespace中的Pid能相互隔离
- pid namespace的意义
  - 一个主机可能有上千个进程，很难管理，但是使用namespace隔离开后，管理上更清晰
  - 进程将彼此隔离，则A进程无法杀死B进程，因为不同namespace下，进程相互看不到



##### Network Namespace

- 网络隔离是通过net namespace实现的，每个net namespace有独立的network devices, ip address, IP routing tables, /proc/net目录
  - 实现了微服务中，给每个服务分配自己的IP，实现服务间通信
- Docker默认采用veth的方式，将container中的虚拟网卡同host上的一个docker bridge：docker0连接在一起



##### IPC namespace

- Container中，进程交互还是采用Linux常见的进程间交互方法，包括常见的信号量，消息队列和共享内存
- container的进程间交互实际上还是host上具有相同pid namespace中的进程间交互，因此需要在IPC资源申请时加入namespace信息-每个IPC资源有一个唯一的32位ID



##### mnt namespace

- mnt namespace允许不同namespace的进程看到的文件结构不同，这样每个namespace中的进程所看到的文件目录就被隔离开了



##### uts namespace

UTS("UNIX Time-sharing System")namespace允许每个Container拥有独立的Hostname和domain name，使其在网络上可以被视作一个独立的节点而非Host上一个进程



##### user namespace

每个Container可以有不同的user和group id，也就是说可以在Container内部用container内部的用户执行程序而非Host上的用户



##### 关于Namespace的常用操作

- 查看当前系统的namespace

```shell
# 相当于list当前主机的namespace
lsns -t <type>
```

- 查看某进程的namespace

```shell
ls -la /用于Pod的环境准备，准备网络栈和存储卷的基础容器proc/<pid>/ns/

# 示例
[root@ubuntu2204 ~]#ls -la /proc/827/ns
总计 0
dr-x--x--x 2 root root 0  8月  6 10:17 .
dr-xr-xr-x 9 root root 0  8月  6 10:16 ..
lrwxrwxrwx 1 root root 0  8月  6 10:17 cgroup -> 'cgroup:[4026531835]'
lrwxrwxrwx 1 root root 0  8月  6 10:17 ipc -> 'ipc:[4026531839]'
lrwxrwxrwx 1 root root 0  8月  6 10:17 mnt -> 'mnt:[4026531841]'
lrwxrwxrwx 1 root root 0  8月  6 10:17 net -> 'net:[4026531840]'
lrwxrwxrwx 1 root root 0  8月  6 10:17 pid -> 'pid:[4026531836]'
lrwxrwxrwx 1 root root 0  8月  6 10:22 pid_for_children -> 'pid:[4026531836]'
lrwxrwxrwx 1 root root 0  8月  6 10:17 time -> 'time:[4026531834]'
lrwxrwxrwx 1 root root 0  8月  6 10:22 time_for_children -> 'time:[4026531834]'
lrwxrwxrwx 1 root root 0  8月  6 10:17 user -> 'user:[4026531837]'
lrwxrwxrwx 1 root root 0  8月  6 10:17 uts -> 'uts:[4026531838]'
```

- 进入某namespace运行命令（非常常用）
  - 当需要对docker容器进行调试，由于容器本身很小，没有调试工具，因此需要使用`nsenter`从主机进入该容器进行调试

```shell
 nsenter -t <pid> -n ip addr

# 第一步先去查容器id
docker ps|grep <container_name>

# 第二步通过docker inspect 去查找该容器在宿主机的Pid
docker inspect <docker_id> | grep -i pid

# 第三步使用nsenter进入该pid的net namespace
nsenter -t <pid> -n ip addr
```

- unshare，将进程移入新的ns

```shell
# 此时sleep 120这个进程会在新的ns中执行
unshare -fn sleep 120

# 使用ps查看sleep 120的pid
[root@ubuntu2204 ~]#ps -ef|grep sleep
root        3533    1024  0 10:47 pts/0    00:00:00 unshare -fn sleep 120
root        3534    3533  0 10:47 pts/0    00:00:00 sleep 120
root        3536    3446  0 10:47 pts/1    00:00:00 grep --color=auto sleep

# 使用nsenter就可以看到这个进程的网路是独立的
# 但是此时网络插件帮该进程去配ip
# docker中，由网络插件，默认bridge去给docker的容器也就是进程配置一个网络ip
[root@ubuntu2204 ~]#nsenter -t 3533 -n ip a
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

# 文件系统也是独立的
[root@ubuntu2204 ~]#nsenter -t 3533 -m ls
bin   dev  home  lib32  libx32      media  opt   root  sbin  swap.img  tmp  var
boot  etc  lib   lib64  lost+found  mnt    proc  run   srv   sys       usr# 查看sleep 120的pid
ps aux|grep sleep    # pid为
```



#### Cgroup

虽然容器内的第1号进程在“障眼法”的干扰下只能看到容器里的情况，但是宿主机上，它作为第100号进程与其他所有进程之间依然是平等竞争关系。

而Linux Cgroups就是Linux内核中用来为进程设置资源限制的一个重要功能

Linux Cgruops的全称是Linux Contrlo Group。它最主要的作用，就是限制一个进程组能够使用的资源上限，包括CPU，内存，磁盘，网络带宽等
此外，Cgoups还能够对进程进行优先级设置，审计，以及将进程挂起和恢复等操作

<span style="color:red;font-weight:699">在 Linux 中，Cgroups 给用户暴露出来的操作接口是文件系统，即它以文件和目录的方式组织在操作系统的 /sys/fs/cgroup 路径下</span>

Ubuntu22.04采用的是cgroup v2，在cgroup v2创建一个控制组

```shell
cd /sys/fs/cgroup
mkdir container
# 创建的这个container的目录，就是一个控制组，操作系统会在这个新创建的container目录下，自动生成该子系统对应的资源限制文件
cgroup.controllers      cgroup.subtree_control  cpuset.cpus.effective  cpu.weight.nice  memory.events.local  memory.stat
cgroup.events           cgroup.threads          cpuset.cpus.partition  io.max           memory.high          memory.swap.current
cgroup.freeze           cgroup.type             cpuset.mems            io.pressure      memory.low           memory.swap.events
cgroup.kill             cpu.idle                cpuset.mems.effective  io.prio.class    memory.max           memory.swap.high
cgroup.max.depth        cpu.max                 cpu.stat               io.stat          memory.min           memory.swap.max
cgroup.max.descendants  cpu.max.burst           cpu.uclamp.max         io.weight        memory.numa_stat     pids.current
cgroup.procs            cpu.pressure            cpu.uclamp.min         memory.current   memory.oom.group     pids.events
cgroup.stat             cpuset.cpus             cpu.weight             memory.events    memory.pressure      pids.max
```

`cpu.max` 文件

- 功能：
  - cpu.max 文件用于设置 CPU 的最大使用时间配额和周期，类似于 cgroup v1 中的 cpu.cfs_quota_us 和 cpu.cfs_period_us。
- 格式：cpu.max 文件的内容格式为 max_quota period，其中：
  - max_quota 表示 CPU 时间的最大配额（以微秒为单位）。
  - period 表示分配的周期（以微秒为单位）。
  - 如果 max_quota 设置为 max，表示没有限制（即与 cgroup v1 中的 -1 类似）。

```shell
# 默认max
[root@ubuntu2204 container]#cat cpu.max
max 100000

# 执行下列指令，控制每 100 ms 的时间里，被该控制组限制的进程只能使用 20 ms 的 CPU 时间，
# 也就是说这个进程只能使用到 20% 的 CPU 带宽。
echo 20000 100000 > cpu.max  # 单位是纳秒，1000纳秒=1毫秒
# 运行下列指令
# 它执行了一个死循环，可以把计算机的 CPU 吃到 100%
# 根据它的输出，我们可以看到这个脚本在后台运行的进程号（PID）是 226
$ while : ; do : ; done &
[1] 226

# 使用top查看可以看到进程号226的程序将CPU打满
```

`cgroup.procs`

- cgroup.procs：在 cgroup v2 中，cgroup.procs 文件用于管理控制组中的进程和线程，与 cgroup v1 中的 tasks 文件功能相同

```shell
echo 226 > cgroup.procs

# 将226进程加入控制组，，此时上面的限制生效，该进程的CPU使用被控制到20%
```

除CPU外，Cgroups的每个文件都有其独有的资源限制能力

Linux Cgroups的设计还是比较易用的，简单粗暴地理解，就是一个子系统目录加上一组资源限制文件的组合。对于Docker等linux容器项目来说，它们只需要为每个容器创建一个控制组（即创建一个新目录），然后在启动容器进程之后，把这个进程的PID填写到对应的控制组的cgroup.procs中就可以了



##### **Docker 使用 cgroups-v1 的步骤**

- 创建控制组目录

  - 当 Docker 启动一个新的容器时，它会在 /sys/fs/cgroup 下创建一个新的控制组目录。这可以用于 CPU、内存、设备访问等各类资源的控制。例如，为某个容器创建一个新的控制组目录

  ```shell
  sudo mkdir /sys/fs/cgroup/cpu/docker/container_id
  sudo mkdir /sys/fs/cgroup/memory/docker/container_id
  # 其他资源类型的控制组目录
  ```

- 配置控制组资源限制

  - 在新的控制组目录中，可以配置资源限制。例如，限制 CPU 和内存使用

  ```shell
  # 设置 CPU 使用配额
  echo "50000 100000" > /sys/fs/cgroup/cpu/docker/container_id/cpu.max
  
  # 设置内存限制
  echo "500M" > /sys/fs/cgroup/memory/docker/container_id/memory.max
  ```

- 启动容器进程

  - 启动容器进程。假设启动的容器进程的 PID 是 12345。

- 将容器进程的 PID 添加到控制组

  - 将容器进程PID写入控制组的cgroup.procs

  ```shell
  echo 12345 > /sys/fs/cgroup/cpu/docker/container_id/cgroup.procs
  echo 12345 > /sys/fs/cgroup/memory/docker/container_id/cgroup.procs
  # 其他资源类型的控制组
  ```



##### 在Cgroups-v2中docker路径

如果 Docker 使用了 `systemd` 驱动，Cgroup 文件路径可能类似于：

```ABAP
/sys/fs/cgroup/system.slice/docker-<container-id>.scope/
```



#### Union FS

- 将不同目录挂载到同一个虚拟文件系统下(unite several directories into a single virtual filesystem的文件系统)
- 支持为每一个成员目录(类似Git Branch)设定readonly、readwrite和whiteout-able权限
- 文件系统分层，对readonly权限的branch可以逻辑上进行修改(增量地，不影响readonly部分的)
- 通常Union FS有两个用途，一方面可以将多个disk挂到同一个目录下，另一个更常用的就是将一个readonly的branch和一个writeable的branch联合在一起

##### Docker的文件系统

典型的Linux文件系统组成

- Bootfs(boot file system)
  - Bootloader - 引导加载kernel
  - Kernel - 当kernel被加载到内存中后umount bootfs
- rootfs(root file system)
  - /dev, /proc, /bin, /etc等标准目录和文件
  - 对于不同的Linux发行版，bootfs基本是一致的，但rootfs会有差别

Docker没有bootfs，它复用主机的Kernel
Docker有自己的rootfs，该rootfs有容器驱动加载出来

##### Docker启动

Linux

- 在启动后，首先将rootfs设置为readonly，进行一系列检查，然后将其切换为"readwrite"供用户使用

Docker

- 初始化时也是将rootfs以readonly方式加载并检查，然后接下来利用union mount的方式将一个readwrite文件系统挂载在readonly的rootfs之上
- 并且允许再次将下层的FS(file system)设定为readonly并向上叠加
- 这样一组readonly和一个writeable的结构构成一个container的运行时态，每一个FS被称为FS层

##### 特点1：写操作

由于镜像具有共享特性，所以对容器可写层的操作需要依赖存储驱动提供的写时复制和用时分配机制，以此来支持对容器可写层的修改，进而提高对存储和内存资源的利用率

- 写时复制
  - 写时复制，即Copy-on-Write。一个镜像可以被多个容器使用，但是不需要在内存和磁盘上做多个拷贝。
  - 在需要对镜像提供的文件进行修改时，该文件会从镜像的文件系统被复制到容器的可写层的文件系统进行修改，而镜像里面的文件不会改变。不同容器对文件的修改都相互独立，互不影响

- 用时分配
  - 按需分配空间，而非提前分配，即当一个文件被创建出来后，才会分配空间

##### OverlayFS文件系统练习

```shell
mkdir upper lower merged work
echo "from lower" > lower/in_lower.txt
echo "from upper" > upper/in_upper.txt
echo "from lower" > lower/in_both.txt
echo "from upper" > upper/in_both.txt

mount -t overlay overlay -o lowerdir=`pwd`/lower,upperdir=`pwd`/upper,workdir=`pwd`/work `pwd`/merged

# upperdir 是最上层的可写层，而 lowerdir 是只读层。当多个层次中存在相同的文件时，优先展示 upperdir 中的版本
cat merged/in_both.txt
from upper

# 在merged层添加一个文件
[root@mystical ~/test/merged]# echo aaa > a.txt

# 查看upper目录和lower目录
[root@mystical ~/test/upper]# ls
a.txt  in_both.txt  in_upper.txt
[root@mystical ~/test/lower]# ls
in_both.txt  in_lower.txt

# 结论1：对 merged 目录的任何写入操作，都会发生在 upperdir，而 lowerdir 仍然是只读的
# 结论2：果 merged 目录中的文件来自 lowerdir，修改它时会触发 "copy-up" 机制，将文件复制到 upperdir，然后再修改（COW 机制）
```

##### Docker文件系统的本质

就是一次次的`mount -t overlay overlay -o <下层>,<上层> <合并>`
通过这种方式，确保进程所需要的所有依赖和配置都在我的隔离环境中，这样迁移到其他环境中，才能完整的replay出来



##### Union FS的优点

```ABAP
1. 多个容器共享相同的 lowerdir，这是 Docker 的层存储机制（Layered Storage）。
2. 每个容器都有自己的 upperdir，存放容器的修改和新增文件，确保容器间互不影响。
3. 如果容器修改 lowerdir 的文件，会触发 "copy-up" 机制，将文件复制到 upperdir，然后容器修改 upperdir 中的文件。
4. lowerdir 仅在 docker rmi 镜像时才会真正删除，而不是删除容器时就消失。

Docker 的存储机制极大地提高了存储效率，让多个容器共享基础镜像层，同时保持隔离性。
```



### Docker组件及其关系



#### Docker组件

- **Docker Client**
- **Dockerd**
- **Containerd**
- **Containerd-shim**
- **Runc**





#### Docker组件详解



##### Dockerd (Docker Daemon)

- 负责接收和解析来自 Docker 客户端（`docker` CLI 或 API）的请求
- 是 Docker 的核心守护进程，主要负责
  - 容器生命周期管理
  - 网络和存储的管理
  - 与其他组件（如 `containerd`）的通信



##### Containerd

- 是一个高性能的容器运行时守护进程，用于管理容器生命周期
- 收 `dockerd` 的请求后，负责更底层的操作，比如
  - 拉取和管理容器镜像。
  - 创建和删除容器。
  - 处理容器的运行状态。
  - 与 `runc` 交互来创建和管理容器的具体运行环境。



##### Containerd-shim

- **了解****`containerd-shim`**
  - **`containerd-shim` 是 `containerd` 的一部分**，它由 `containerd` 创建和管理，用于处理容器的生命周期及相关操作

- **作用**

  - 它`containerd-shim` 是 `containerd` 的一个独立进程，为每个运行的容器提供隔离层
    - 通过 `containerd-shim`，每个容器都可以独立运行，无需依赖 `dockerd`。

- **启动 `containerd-shim`**

  - 当 `containerd` 接收到创建容器的请求时，会启动一个新的 `containerd-shim` 进程。
  - 每个容器都会对应一个独立的 `containerd-shim`。

- **主要职责**

  - **管理生命周期**: 通过与运行时（如 `runc`）交互，控制容器的创建、启动、停止等。
  - **标准输入/输出处理**: 处理容器的 `stdin`、`stdout`、`stderr` 管道。
  - **信号转发**: 将主机的信号（如 `SIGTERM`）转发给容器的主进程
  - **资源监控**: 通过与 cgroup 的交互，监控和限制容器的资源使用

- **关于独立进程的解读**

  - 容器的生命周期独立于 `containerd`：
    - 如果 `containerd` 崩溃或重启，容器不会受影响。
    - 通过 `containerd-shim`，每个容器都有一个进程在管理它。
  - 提供更细粒度的进程管理：
    - 每个容器的 `containerd-shim` 是一个独立的进程，确保容器进程隔离，不受其他容器影响。

- **与 `runc` 的关系**:

  - `containerd-shim` 是 `containerd` 与运行时（如 `runc`）之间的**桥梁**。

  - 它调用 `runc` 来实际执行容器创建、运行、暂停等操作。



##### runc

- 是一个轻量级工具，用于按照 OCI（Open Container Initiative）标准创建和运行容器
- 主要职责：
  - 使用 Linux 内核的 **`namespace`** 和 **`cgroup`** 功能隔离容器。
  - 执行容器进程的初始化





#### 工作流程拆解



**创建容器**

1. **`docker` CLI**:

   - 用户通过 `docker` CLI 发起容器创建请求（如 `docker run`）。

   - CLI 将请求发送到 `dockerd`。

2. **`dockerd`**:

   - 接收请求后，解析用户的需求（如镜像名、资源限制等）。

   - 将请求转发给 `containerd`。

3. **`containerd`**:

   - 拉取镜像（如果镜像尚未本地存在）。

   - 创建容器相关的**元数据**。

   - 调用 `runc` 来设置容器的运行环境。

3. **`runc`**:

   - 使用 Linux 的 **`namespace`** 隔离文件系统、进程、网络等资源。

   - 使用 **`cgroup`** 控制容器的 CPU、内存、磁盘等资源使用。

   - 启动容器进程。

   

```ABAP
docker CLI --> dockerd --> containerd --> containerd-shim --> runc
```





### 容器标准



#### **Open Container Initiative（OCI）**

**Open Container Initiative (OCI)** 是由 **Linux Foundation** 于 2015 年创建的一个开放治理结构，旨在为容器格式和运行时制定开放的行业标准。**OCI 的目标是解决容器生态系统中存在的兼容性和可移植性问题**，推动不同容器平台之间的互操作性。



**OCI 成立的背景**

在 OCI 成立之前，容器技术缺乏统一的标准，具体表现为：

- 各大平台（如 Docker、CoreOS rkt 等）使用不同的镜像格式和运行时实现，导致工具之间无法兼容。

- 开发者在一个平台上构建的容器，可能无法在其他平台无缝运行。

为了解决这些问题，Docker 将其 **容器运行时规范**（libcontainer）和 **镜像格式规范** 捐献给 OCI，成为该组织的奠基。





#### OCI 的核心规范



OCI 目前有三个主要规范：

1. **OCI 运行时规范 (Runtime Specification)：**

   - 定义文件系统包如何解压至硬盘
   - 定义容器的运行方式。
   - 描述容器的配置文件格式和生命周期。
   - 涉及低层实现细节，如 Linux 的 namespaces（命名空间）、cgroups（控制组）、文件系统和挂载点。
   - 实现：
     - **runc** 是 OCI 运行时规范的参考实现，也是许多容器引擎使用的核心组件。
     - Runc依托于Namespace和Cgroup技术（这两个技术和Docker没有任何关系）

2. **OCI 镜像规范 (Image Specification)：**

   - 标准化容器镜像的格式。
   - 描述镜像的打包、分发和分层结构。
   - 确保不同容器引擎和镜像仓库之间的兼容性。
   - 实现：
     - Docker、Podman 和 Buildah 等工具均遵循 OCI 镜像规范。

   ```ABAP
   Docker的创举：基于OverlayFS，把以前虚拟机镜像这种整个二进制包揉在一起的模式，通过Dockerfile这种分层的方式，使得容器变得更有调理；容器镜像分为很多层，每一层分发的时候，可以去并行分发，而且每一层有自己的checksum，当checksum一致（也就是没发生变化）的时候，它是认缓存的
   
   比如有一个2G的镜像，分了10层，只有最上面的几M是你的增量（也就是每次更新版本，变更在几兆），当你docker pull的时候，如果本地已经有老版本的，当你Pull新版本的时候，会直接利用缓存，而只Pull更新的几兆。
   
   通过上述方式，巧妙的解决了业界一直头痛的问题，也就是应用如何分发的问题，在最大程度上做到了复用
   多个容器可以共享相同的镜像层，而不需要为每个容器单独存储一份镜像
   ```

   

3. **OCI 分发规范 (Distribution Specification)：**

   - 定义容器镜像及其工件的分发方式。
   - 提供标准 API 用于镜像的发现、拉取和推送。
   - 基于 Docker 的 Registry HTTP API V2。





### Docker安装

#### Ubuntu内置仓库安装

```bash
[root@mystical ~]# apt update && apt install -y docker.io

# 查看
[root@mystical ~]# docker info
Client:
 Version:    24.0.7
 Context:    default
 Debug Mode: false

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 24.0.7
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 
 runc version: 
 init version: 
 Security Options:
  apparmor
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 5.15.0-102-generic
 Operating System: Ubuntu 22.04.3 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 2
 Total Memory: 1.883GiB
 Name: mystical
 ID: ca263d13-ae96-4c86-bba5-be8480d1ea64
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false
```



#### 官方仓库安装

**阿里云官方仓库**

- 官方地址

```http
https://developer.aliyun.com/mirror/docker-ce?spm=a2c6h.13651102.0.0.57e31b11DDIh92
```

- 官方操作（可以看做是脚本运行）

```bash
# step 1: 安装必要的一些系统工具
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
# step 2: 安装GPG证书
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
# Step 3: 写入软件源信息
sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
# Step 4: 更新并安装Docker-CE
sudo apt-get -y update
sudo apt-get -y install docker-ce # 默认下载最新版

# 安装Docker-CE特定版本
sudo apt-get -y install docker-ce=[VERSION] docker-ce-cli=[VERSION]
```



#### 二进制安装（离线）

本方法适用于无法上网或无法通过包安装方式安装的主机上安装docker

```bash
# 二进制安装下载路径
https://download.docker.com/linux/
https://mirrors.aliyun.com/docker-ce/linux/static/stable/x86_64/
```

示例：在CentOS上实现二进制安装docker

```bash
wget https://download.docker.com/linux/static/stable/x86_64/docker-19.03.5.tgz

# 解压到指定目录
tar xvf docker-19.03.5.tgz    

# 加入环境变量
cp docker/* /usr/bin/

# 创建 service文件
cat > /lib/systemd/system/docker.service <<-EOF
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target
[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues 
still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/bin/dockerd -H unix://var/run/docker.sock
ExecReload=/bin/kill -s HUP \$MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker 
containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s
[Install]
WantedBy=multi-user.target
EOF

# 重启
systemctl daemon-reload
systemctl enable --now docker   
```



#### 脚本安装

- install_docker_offine.sh

```bash
#!/bin/bash
#
#********************************************************************
#Author:            wangxiaochun
#QQ:                29308620
#Date:              2022-10-14
#FileName:          install_docker_offline.sh
#URL:               http://www.wangxiaochun.com
#Description:       The test script
#Copyright (C):     2022 All rights reserved
#********************************************************************

#支持在线和离线安装

DOCKER_VERSION=26.1.4
#DOCKER_VERSION=26.0.0
#DOCKER_VERSION=24.0.7
#DOCKER_VERSION=24.0.5
#DOCKER_VERSION=23.0.3
#DOCKER_VERSION=20.10.19

URL=https://mirrors.tuna.tsinghua.edu.cn
#URL=https://mirrors.aliyun.com
#URL=https://download.docker.com

color () {
    RES_COL=60
    MOVE_TO_COL="echo -en \\033[${RES_COL}G"
    SETCOLOR_SUCCESS="echo -en \\033[1;32m"
    SETCOLOR_FAILURE="echo -en \\033[1;31m"
    SETCOLOR_WARNING="echo -en \\033[1;33m"
    SETCOLOR_NORMAL="echo -en \E[0m"
    echo -n "$1" && $MOVE_TO_COL
    echo -n "["
    if [ $2 = "success" -o $2 = "0" ] ;then
        ${SETCOLOR_SUCCESS}
        echo -n $"  OK  "    
    elif [ $2 = "failure" -o $2 = "1"  ] ;then 
        ${SETCOLOR_FAILURE}
        echo -n $"FAILED"
    else
        ${SETCOLOR_WARNING}
        echo -n $"WARNING"
    fi
    ${SETCOLOR_NORMAL}
    echo -n "]"
    echo 
}

prepare () {
    if [ ! -e docker-${DOCKER_VERSION}.tgz ];then
        #wget ${URL}/docker-ce/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
        wget ${URL}/docker-ce/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
    fi
    [ $? -ne 0  ] && { echo "文件下载失败"; exit; }
}

install_docker () {
    tar xf docker-${DOCKER_VERSION}.tgz -C /usr/local/
    cp /usr/local/docker/* /usr/local/bin/
    cat > /lib/systemd/system/docker.service <<-EOF
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target

[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/local/bin/dockerd -H unix://var/run/docker.sock
ExecReload=/bin/kill -s HUP \$MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s

[Install]
WantedBy=multi-user.target
EOF
    systemctl daemon-reload
}

config_docker () {
    mkdir -p /etc/docker
    tee /etc/docker/daemon.json <<-'EOF'
    {
      "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"]
     }
EOF
    #systemctl restart docker

}

start_docker (){
    systemctl enable --now docker
    docker version && color "Docker 安装成功" 0 ||  color "Docker 安装失败" 1
}


config_docker_completion () {
    wget -P /etc/bash_completion.d http://www.wangxiaochun.com:8888/testdir/docker/docker_completion 
    #source /etc/bash_completion.d/docker_completion
}


prepare

install_docker

config_docker

start_docker

config_docker_completion
```



#### Docker卸载

```bash
apt purge docker-ce
rm -rf /var/lib/docker
```



#### 停止Docker服务

```bash
# 仅停止docker.service，暂停后会被自动激活
systemctl stop docker.service

# 想停止该服务，还需停止docker.socket
systemctl stop docker.service docker.socket
```





### Docker配置优化

#### 优化方法1：用空间足够的高速磁盘用来存放docker的相关数据

```shell
# 在/etc/docker/目录下创建配置文件daemon.json(该文件默认不存在，需要自己创建)
vim /etc/docker/daemon.json

# daemon.json
{
  #指定docker数据目录,新版24.0.0不支持，
  # 实现：修改service文件
  # ExecStart=/usr/bin/dockerd --data-root=/data/docker
  "graph": "/data/docker",  
}
```

#### 优化方法2：从自建仓库下载镜像

```shell
# 查看docker信息
docker info

# 默认不信任外部仓库
···
Insecure Registries:
  127.0.0.0/8
···

# 需要在配置文件中添加信任的仓库
vim /etc/docker/daemon.json
{
  "insecure-registries": ["harbor.wang.org","172.18.0.253"]
}

# 添加后重启
systemctl restart docker

# 再次查看docker信息
docker info
···
Insecure Registries:
  harbor.wang.org
  172.18.0.253
  127.0.0.0/8
```

#### 优化方法3：调整允许最多同时下载docker镜像的数量（使其性能更好）

```shell
vim /etc/docker/daemon.json
{
  # 允许最多同时下载docker镜像的数量
  "max-concurrent-downloads": 10,
  # 最大允许同时上传多少个
  "max-concurrent-uploads": 5
}
```

#### 优化方法4：对容器中生成的日志进行约束

```shell
vim /etc/docker/daemon.json
{
  # 防止容器的日志过大，撑满磁盘
  "log-opts": {
    # 指定容器日志文件的最大值
    "max-size": "300m",
    # 指定容器日志文件的个数
    # 循环写入日志文件
    # 即一个日志满，会写入第二个
    "max-file": "2"
  }
}
```

#### 优化方法5：镜像加速，加快镜像下载速度

```shell
# docker网站被墙的情况下，该加速无效
vim /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://registry.docker-cn.com",
    "http://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn",
    "https://si7y70hh.mirror.aliyuncs.com/"
  ]
}
```

#### 扩展：docker远程连接

```shell
systemctl cat docker

...
# -H 指定客户端和服务端通信的媒介
# docker客户端通过该socket文件发送指令
# docker服务端通过该socket通过该文件接收指令
# for containers run by docker
ExecStart=/usr/bin/dockerd -H unix://var/run/docker.sock  --data-root=/data/docker
ExecReload=/bin/kill -s HUP $MAINPID
...
# 但是这只能保证同主机间的通信
# 如果客户端和服务器端不再同一主机
# 比如在10.0.0.101的客户端，去访问10.0.0.100的docker服务端，需要打开远程连接
# 方法：在dockerd的守护进程上开启远程连接
# -H,--host=
# tcp://host:port,
# 默认2375端口（不加密），加密：2376
# unix://path/to/socket
# fd://* or fd://socketfd
```

#### 远程连接的实现方法1

**方法1：修改service文件**

```shell
vim /lib/systemd/system/docker.service
# 后面加一行 -H tcp://0.0.0.0:2375
ExecStart=/usr/bin/dockerd -H unix://var/run/docker.sock  --data-root=/data/docker -H tcp://0.0.0.0:2375
```

**问题：当虚拟机的全局环境变量开启代理，该虚拟机远程连接其他机器的docker服务端失效**

```shell
cat .bashrc
...
export http_proxy=http://10.0.0.1:10809
export https_proxy=http://10.0.0.1:10809
export ftp_proxy=ftp://10.0.0.1:10809
```

此时运行`docker -H 10.0.0.208 version`失败

原因：Docker 客户端直接连接：Docker 客户端连接 Docker 守护进程通常通过直接 TCP 连接 (tcp://) 而不是 HTTP(S) 代理。代理的设置会导致 Docker 客户端尝试通过代理去连接，而代理并不支持这种直接 TCP 连接，从而导致连接失败。

**解决方案**

```shell
export http_proxy=http://10.0.0.1:10809
export https_proxy=http://10.0.0.1:10809
export ftp_proxy=ftp://10.0.0.1:10809
export NO_PROXY="10.0.0.208"
```

指定连接10.0.0.208的通信不走代理即可

#### 远程连接的实现方法2（更安全）

通过ssh远程连接

```shell
docker -H ssh://root@10.0.0.206 version
```

实现ssh远程连接的前提

- 打通key验证

```shell
# 生成密钥私钥对
ssh-keygen

# 将公钥拷贝到指定服务器
ssh-copy-id root@10.0.0.206
```


#### 优化方法6：重启docker不影响容器运行

```shell
vim /etc/docker/daemon.json

{
  # docker.service重启，不影响容器的运行
  "live-restore": true
}
```

#### 优化方法7：修改默认 `docker0` 网络的网段

```bash
# 编辑或创建 Docker 配置文件
sudo mkdir -p /etc/docker
sudo vi /etc/docker/daemon.json

# 添加或修改 bip 选项
{
  "bip": "192.168.100.1/24"
}

# 重启Docker
sudo systemctl restart docker

# 验证新的 docker0 网段
ip a show docker0
```

#### 优化方法8：添加代理

```bash
# 核心代码
PROXY_SERVER_IP=10.0.0.1
PROXY_PORT=10808
[ -d /etc/systemd/system/docker.service.d ] || mkdir -p /etc/systemd/system/docker.service.d
cat >> /etc/systemd/system/docker.service.d/http-proxy.conf <<EOF
[Service]
Environment="HTTP_PROXY=http://${PROXY_SERVER_IP}:${PROXY_PORT}/"
Environment="HTTPS_PROXY=http://${PROXY_SERVER_IP}:${PROXY_PORT}/"
# 如果有本地镜像仓，不走代理，可以把镜像仓的IP或者域名写在这里
Environment="NO_PROXY=127.0.0.0/8,172.17.0.0/16,10.0.0.0/24,10.244.0.0/16,192.168.0.0/16,wang.org,cluster.local"
EOF
systemctl daemon-reload
systemctl restart docker.service
```





## Docker命令

### Docker镜像管理

#### 镜像结构和原理

镜像即创建容器的模版，含有启动容器所需要的文件系统及所需要的内容，因此镜像主要用于方便和快速的创建并启动容器

镜像含里面是一层层的文件系统,叫做 **Union FS（联合文件系统）**,联合文件系统，可以将几层目录挂载 到一起（就像千层饼，洋葱头，俄罗斯套娃一样），形成一个虚拟文件系统,虚拟文件系统的目录结构就像普通 linux 的目录结构一样，镜像通过这些文件再加上宿主机的内核共同提供了一个 linux 的虚拟环境，每一层文件系统叫做一层 layer，联合文件系统可以对每一层文件系统设置三种权限，**只读 （readonly）、读写（readwrite）和写出（whiteout-able）**，但是镜像中每一层文件系统都是只读的, 构建镜像的时候，从一个最基本的操作系统开始，每个构建提交的操作都相当于做一层的修改，增加了 一层文件系统，一层层往上叠加，上层的修改会覆盖底层该位置的可见性，这也很容易理解，就像上层 把底层遮住了一样，当使用镜像的时候，我们只会看到一个完全的整体，不知道里面有几层,实际上也不需要知道里面有几层，结构如下:

![image-20250201215931873](D:\git_repository\cyber_security_learning\markdown_img\image-20250201215931873.png)

一个典型的 Linux文件系统由 **bootfs** 和 **rootfs** 两部分组成

bootfs(boot file system) 主要包含bootloader和kernel，bootloader主要用于引导加载 kernel，Linux 刚启动时会加载bootfs文件系统,当boot加载完成后,kernel 被加载到内存中后接管系统的控制权,bootfs 会被 umount 掉

rootfs (root file system) 包含的就是典型 Linux 系统中的/dev，/proc，/bin，/etc 等标准目录和文件， 不同的 linux 发行版（如 ubuntu 和 CentOS ) 主要在 rootfs 这一层会有所区别。

一般的镜像通常都比较小，官方提供的Ubuntu镜像只有60MB多点，而 CentOS 基础镜像也只有200MB 左右，一些其他版本的镜像甚至只有几MB，比如:  busybox 才1.22MB，alpine镜像也只有5M左右。镜像直接调用宿主机的内核，镜像中只提供 rootfs，也就是只需要包括最基本的命令,配置文件和程序库等相关文件就可以了。



#### 查看镜像

范例:  查看镜像的分层结构

```bash
[root@ubuntu2204 ~]# docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
af302e5c37e9: Pull complete 
207b812743af: Pull complete 
841e383b441e: Pull complete 
0256c04a8d84: Pull complete 
38e992d287c5: Pull complete 
9e9aab598f58: Pull complete 
4de87b37f4ad: Pull complete 
Digest: sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206a
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest

# 查看镜像分层历史
[root@ubuntu2204 docker-entrypoint.d]#docker image  history nginx
IMAGE          CREATED        CREATED BY                                       SIZE      COMMENT
9bea9f2796e2   2 months ago   CMD ["nginx" "-g" "daemon off;"]                 0B        buildkit.dockerfile.v0
<missing>      2 months ago   STOPSIGNAL SIGQUIT                               0B        buildkit.dockerfile.v0
<missing>      2 months ago   EXPOSE map[80/tcp:{}]                            0B        buildkit.dockerfile.v0
<missing>      2 months ago   ENTRYPOINT ["/docker-entrypoint.sh"]             0B        buildkit.dockerfile.v0
<missing>      2 months ago   COPY 30-tune-worker-processes.sh /docker-ent…   4.62kB    buildkit.dockerfile.v0
<missing>      2 months ago   COPY 20-envsubst-on-templates.sh /docker-ent…   3.02kB    buildkit.dockerfile.v0
<missing>      2 months ago   COPY 15-local-resolvers.envsh /docker-entryp…   389B      buildkit.dockerfile.v0
<missing>      2 months ago   COPY 10-listen-on-ipv6-by-default.sh /docker…   2.12kB    buildkit.dockerfile.v0
<missing>      2 months ago   COPY docker-entrypoint.sh / # buildkit           1.62kB    buildkit.dockerfile.v0
<missing>      2 months ago   RUN /bin/sh -c set -x     && groupadd --syst…   117MB     buildkit.dockerfile.v0
<missing>      2 months ago   ENV DYNPKG_RELEASE=1~bookworm                    0B        buildkit.dockerfile.v0
<missing>      2 months ago   ENV PKG_RELEASE=1~bookworm                       0B        buildkit.dockerfile.v0
<missing>      2 months ago   ENV NJS_RELEASE=1~bookworm                       0B        buildkit.dockerfile.v0
<missing>      2 months ago   ENV NJS_VERSION=0.8.7                            0B        buildkit.dockerfile.v0
<missing>      2 months ago   ENV NGINX_VERSION=1.27.3                         0B        buildkit.dockerfile.v0
<missing>      2 months ago   LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0
<missing>      2 months ago   # debian.sh --arch 'amd64' out/ 'bookworm' '…   74.8MB    debuerreotype 0.15

[root@ubuntu2204 ~]#docker inspect nginx
[
    {
        "Id": "sha256:9bea9f2796e236cb18c2b3ad561ff29f655d1001f9ec7247a0bc5e08d25652a1",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206a"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2024-11-26T18:42:08Z",
        "DockerVersion": "",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.27.3",
                "NJS_VERSION=0.8.7",
                "NJS_RELEASE=1~bookworm",
                "PKG_RELEASE=1~bookworm",
                "DYNPKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 191717838,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/1249b5e460970bc0669325f672f717926c587d2c90e5fb83acd0e8b2a7f2ac5a/diff:/var/lib/docker/overlay2/9656448c1b2636d76bd98557faad6c8caf5a0d1ad84f2e5bead8b6347fc7ad77/diff:/var/lib/docker/overlay2/0dde63244c35f47fdb37dc8d59c6675c71d522910ae5caa9539a622f2598b634/diff:/var/lib/docker/overlay2/5e09fb9bb9e90097695a35f40ae7ac5e30d97ef9d899f550d435b8cf6bf5aa74/diff:/var/lib/docker/overlay2/1c7db90446e2df6c7a062ed3519d0c42ac36d6ec04cd8d1eb1090a796c4ea76c/diff:/var/lib/docker/overlay2/7c5ef05f1f440ea899031a98ee13da160e10cf1446e6abc4c26d12b99b2ce59e/diff",
                "MergedDir": "/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/merged",
                "UpperDir": "/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/diff",
                "WorkDir": "/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:f5fe472da25334617e6e6467c7ebce41e0ae5580e5bd0ecbf0d573bacd560ecb",
                "sha256:88ebb510d2fb3ed50f4268455a38443074cad5c6957f6d2cd0126c899a159e6e",
                "sha256:9431321431991c4e64246007e04602160bca8984439ff96461fb992072dd49af",
                "sha256:32c977818204dc910140b3b7abcad06a6613dd1f511ce8f33626a364a3bb68b6",
                "sha256:541cf9cf006d6c9920e5897bf63a4dce0ae1a8388bc82bfa1abedc48b8eb1de9",
                "sha256:58045dd06e5b2c1220ab200c36b450ce3adbfd3fa0f8e3c2c17ffaf7f2906455",
                "sha256:b57b5eac2941c7c1f1f5bc2391123e553d0082eb8e1c6675101aab47a11b26ee"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
```



#### 搜索镜像

官方网站进行镜像的搜索

```http
http://hub.docker.com
http://dockerhub.com
https://hub-stage.docker.com
```

![image-20250201223443278](D:\git_repository\cyber_security_learning\markdown_img\image-20250201223443278.png)

![image-20250201223610265](D:\git_repository\cyber_security_learning\markdown_img\image-20250201223610265.png)

在官方的docker 仓库中搜索指定名称的docker镜像，也会有很多三方镜像。



##### docker search命令详解

格式如下

```bash
Usage:  docker search [OPTIONS] TERM

options:
    -f, --filter filter   Filter output based on conditions provided
        --format string   Pretty-print search using a Go template
        --limit int       Max number of search results (default 25)
        --no-trunc        Don't truncate output
# 说明: 
# OFFICIAL:  官方
# AUTOMATED:  使用第三方docker服务来帮助编译镜像，可以在互联网上面直接拉取到镜像，减少了繁琐的编译过程
```

范例

```bash
[root@ubuntu2204 ~]#docker search alpine
NAME                DESCRIPTION                                      STARS     OFFICIAL
alpine              A minimal Docker image based on Alpine Linux…   11172     [OK]
alpine/git          A  simple git container running in alpine li…   239       
alpine/socat        Run socat command in alpine container            105       
alpine/helm         Auto-trigger docker build for kubernetes hel…   68        
alpine/k8s          Kubernetes toolbox for EKS (kubectl, helm, i…   58 
...
```

范例:  选择性的查找镜像

```bash
#搜索点赞100个以上的镜像
[root@ubuntu2204 ~]#docker  search --filter=stars=100 centos
NAME             DESCRIPTION                                 STARS     OFFICIAL
centos           DEPRECATED; The official build of CentOS.   7763      [OK]
centos/systemd   systemd enabled base container.             115 
```



#### **alpine 介绍**

![image-20250201225805763](D:\git_repository\cyber_security_learning\markdown_img\image-20250201225805763.png)

Alpine 操作系统是一个面向安全的轻型 Linux 发行版。它不同于通常 Linux 发行版，Alpine 采用了  musl libc 和 busybox 以减小系统的体积和运行时资源消耗，但功能上比 busybox 又完善的多，因此得 到开源社区越来越多的青睐。在保持瘦身的同时，Alpine 还提供了自己的**包管理工具 apk**，可以通过 https://pkgs.alpinelinux.org/packages 网站上查询包信息，也可以直接通过 apk 命令直接查询和安装各 种软件。

Alpine 由非商业组织维护的，支持广泛场景的 Linux发行版，它特别为资深/重度Linux用户而优化，关 注安全，性能和资源效能。Alpine 镜像可以适用于更多常用场景，并且是一个优秀的可以适用于生产的 基础系统/环境

Alpine Docker 镜像也继承了 Alpine Linux 发行版的这些优势。相比于其他 Docker 镜像，它的容量非常小，仅仅只有 5 MB 左右（对比 Ubuntu 系列镜像接近 200 MB），且拥有非常友好的包管理机制。 官方镜像来自 docker-alpine 项目

目前 Docker 官方已开始推荐使用 Alpine 替代之前的 Ubuntu 做为基础镜像环境。这样会带来多个好 处。包括镜像下载速度加快，镜像安全性提高，主机之间的切换更方便，占用更少磁盘空间等。

下表是官方镜像的大小比较: 

```bash
REPOSITORY          TAG           IMAGE ID          VIRTUAL SIZE
 busybox            latest        beae173ccac6      1.24MB
 alpine             latest        4e38e38c8ce0      4.799 MB
 debian             latest        4d6ce913b130      84.98 MB 
 ubuntu             latest        b39b81afc8ca      188.3 MB
 centos             latest        8efe422e6104      210 MB
```

- Alpine 官网:   https://www.alpinelinux.org/
- Alpine 官方仓库:   https://github.com/alpinelinux 
- Alpine 官方镜像:   https://hub.docker.com/_/alpine/
- Alpine 官方镜像仓库:   https://github.com/gliderlabs/docker-alpine
- Alpine 阿里云的镜像仓库:   https://mirrors.aliyun.com/alpine/



alpine管理软件

```bash
# 下载apline
[root@ubuntu2204 ~]#docker pull alpine
Using default tag: latest
latest: Pulling from library/alpine
1f3e46996e29: Pull complete 
Digest: sha256:56fa17d2a7e7f168a043a2712e63aed1f8543aeafdcee47c58dcffe38ed51099
Status: Downloaded newer image for alpine:latest
docker.io/library/alpine:latest

# 查看软件源文件
[root@ubuntu2204 ~]# docker run --name myapline --rm alpine cat /etc/apk/repositories
https://dl-cdn.alpinelinux.org/alpine/v3.21/main
https://dl-cdn.alpinelinux.org/alpine/v3.21/community

# 默认是国外源，替换为中科大的源
[root@ubuntu2204 ~]#sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/' /etc/apk/repositories

#修改源替换成阿里源，将里面 dl-cdn.alpinelinux.org 的 改成 mirrors.aliyun.com
vi /etc/apk/repositories
https://mirrors.ustc.edu.cn/alpine/v3.16/main
https://mirrors.ustc.edu.cn/alpine/v3.16/community

http://mirrors.aliyun.com/alpine/v3.8/main/
http://mirrors.aliyun.com/alpine/v3.8/community/

#更新源
apk update = apt update

#安装软件
apk add vim = apt install vim

#删除软件
apk del openssh openntp vim = apt remove openssh 

#安装常见软件
apk update && apk --no-cache add bash curl telnet  wget net-tools pstree  zip unzip 

#安装常用编译工具
apk update && apk --no-cache add gcc make curl zip unzip net-tools pstree wget libgcc libc-dev libcurl libc-utils pcre-dev zlib-dev  libnfs  pcre pcre2 libevent libevent-dev iproute2 

#修改时区
apk update && apk --no-cache add tzdata  && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
```



#### 下载镜像

从 docker 仓库将镜像下载到本地，命令格式如下

```bash
docker pull [OPTIONS] NAME[:TAG|@DIGEST]

Options:
    -a, --all-tags                 Download all tagged images in the repository
        --disable-content-trust    Skip image verification (default true)
        --platform string          Set platform if server is multi-platform capable
    -q, --quiet                    Suppress verbose output
    
# NAME: 是镜像名,一般的形式  仓库服务器:端口/项目名称/镜像名称
# :TAG: 即版本号,如果不指定:TAG,则下载最新版镜像
```

镜像下载说明

```bash
[root@ubuntu1804 ~]#docker pull hello-world
Using default tag: latest #默认下载最新版本
latest: Pulling from library/hello-world
1b930d010525: Pull complete  #分层下载
Digest: sha256:9572f7cdcee8591948c2963463447a53466950b3fc15a247fcad1917ca215a2f
#摘要
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest  #下载的完整地址
```

镜像下载保存的路径:  

```http
/var/lib/docker/overlay2/OverlayFS目录ID（Layer ID）
```

注意:  镜像下载完成后，会自动解压缩，比官网显示的可能会大很多，如:   centos8.1.1911下载时只有 70MB，下载完后显示237MB

下载镜像 alpine,busybox等镜像,查看下载的存放目录

```bash
# 你可以使用以下命令找到 镜像的底层 Layer ID
[root@ubuntu2204 docker-entrypoint.d]#docker inspect --format='{{.GraphDriver.Data.LowerDir}}' nginx
/var/lib/docker/overlay2/1249b5e460970bc0669325f672f717926c587d2c90e5fb83acd0e8b2a7f2ac5a/diff:/var/lib/docker/overlay2/9656448c1b2636d76bd98557faad6c8caf5a0d1ad84f2e5bead8b6347fc7ad77/diff:/var/lib/docker/overlay2/0dde63244c35f47fdb37dc8d59c6675c71d522910ae5caa9539a622f2598b634/diff:/var/lib/docker/overlay2/5e09fb9bb9e90097695a35f40ae7ac5e30d97ef9d899f550d435b8cf6bf5aa74/diff:/var/lib/docker/overlay2/1c7db90446e2df6c7a062ed3519d0c42ac36d6ec04cd8d1eb1090a796c4ea76c/diff:/var/lib/docker/overlay2/7c5ef05f1f440ea899031a98ee13da160e10cf1446e6abc4c26d12b99b2ce59e/diff

# 可以直接查看 镜像的最高层（顶层）
[root@ubuntu2204 docker-entrypoint.d]#docker inspect --format='{{.GraphDriver.Data.UpperDir}}' nginx
/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/diff

# 实际目录内容
[root@ubuntu2204 overlay2]#pwd
/var/lib/docker/overlay2
[root@ubuntu2204 overlay2]#ls
0dde63244c35f47fdb37dc8d59c6675c71d522910ae5caa9539a622f2598b634
1249b5e460970bc0669325f672f717926c587d2c90e5fb83acd0e8b2a7f2ac5a
1c7db90446e2df6c7a062ed3519d0c42ac36d6ec04cd8d1eb1090a796c4ea76c
3de5cf009108cf7c0aab9084cfdd7a5121ea9d1c791797da7dd54c1cc6d91efd
5e09fb9bb9e90097695a35f40ae7ac5e30d97ef9d899f550d435b8cf6bf5aa74
7c5ef05f1f440ea899031a98ee13da160e10cf1446e6abc4c26d12b99b2ce59e
9656448c1b2636d76bd98557faad6c8caf5a0d1ad84f2e5bead8b6347fc7ad77
e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13
l   
# l目录的作用
# 用于管理和优化 Docker 存储层， 
# 里面的文件是 Layer ID 的短哈希，链接到真实 overlay2 目录
# Docker 通过 l/ 目录优化镜像层的访问速度，减少存储开销
```



##### 镜像加速配置和优化

docker 镜像官方的下载站点是:   https://hub.docker.com/

![image-20250202113930676](D:\git_repository\cyber_security_learning\markdown_img\image-20250202113930676.png)

从国内下载官方的镜像站点有时候会很慢，因此可以更改docker配置文件添加一个加速器，可以通过加 速器达到加速下载镜像的目的

国内有许多公司都提供了docker 加速镜像，比如:  阿里云，腾讯云，网易云，以下以阿里云为例

![image-20250202120049008](D:\git_repository\cyber_security_learning\markdown_img\image-20250202120049008.png)

##### **Docker 镜像加速配置**

```bash
1. 安装／升级Docker客户端
推荐安装1.10.0以上版本的Docker客户端，参考文档 docker-ce

2. 配置镜像加速器
修改daemon配置文件/etc/docker/daemon.json来使用加速器

mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
 "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn","http://hub mirror.c.163.com/","https://si7y70hh.mirror.aliyuncs.com"],
 "live-restore": true,      #docker服务重启,不会重启容器,
 "graph": "/data/docker"，  #指定docker数据目录
 "insecure-registries": ["harbor.wang.org"]
}
EOF

#网易云:  http://hub-mirror.c.163.com/
#中科大:  https://docker.mirrors.ustc.edu.cn
#腾讯云:  https://mirror.ccs.tencentyun.com
#七牛云:  https://reg-mirror.qiniu.com

systemctl daemon-reload
systemctl restart docker
```

范例： 镜像加速器

```bash
[root@ubuntu1804 ~]vim /etc/docker/daemon.json
{
   # 设置 Docker 镜像加速器（Registry Mirrors），加速从 Docker Hub 拉取镜像。
   "registry-mirrors" : [
   "http://registry.docker-cn.com",
   "http://docker.mirrors.ustc.edu.cn",
   "http://hub-mirror.c.163.com"
  ],
   # 允许 Docker 访问不安全（未启用 HTTPS）的私有镜像仓库。
   "insecure-registries" : [
   "registry.docker-cn.com",
   "docker.mirrors.ustc.edu.cn"
  ],
 "debug" : true,
 "experimental" : true
}
```



#### 查看本地镜像

docker images 可以查看下载至本地的镜像

```http
https://docs.docker.com/engine/reference/commandline/images/
```

格式

```bash
# docker images 和 docker image ls 等价
docker images [OPTIONS] [REPOSITORY[:TAG]]
docker image ls [OPTIONS] [REPOSITORY[:TAG]]

#常用选项: 
-q, --quiet            # Only show numeric IDs       
-a, --all              # Show all images (default hides intermediate images)     
    --digests          # Show digests
    --no-trunc         # Don't truncate output(显示完整的image ID)
-f, --filter filter    # Filter output based on conditions provided
    --format string    # Pretty-print images using a Go template
```

执行结果的显示信息说明:  

```bash
REPOSITORY          #镜像所属的仓库名称 
TAG                 #镜像版本号（标识符），默认为latest        
IMAGE ID            #镜像唯一ID标识,如果ID相同,说明是同一个镜像有多个名称   
CREATED             #镜像在仓库中被创建时间   
VIRTUAL SIZE        #镜像的大小
```

docker images --format命令用于指定在输出中显示映像信息的格式。格式字符串由多个占位符组成， 每个占位符代表映像的特定属性。

```bash
#常用的格式占位符：
{{.Repository}}：映像的仓库名称。
{{.Tag}}：映像的标签。
{{.ID}}：映像的ID。
{{.Digest}}：映像的摘要值
{{.CreatedAt}}：映像的创建时间
{{.Size}}：映像的大小。

#示例，括号内首字母大写
docker images --format "{{.Repository}}\t{{.Tag}}\t{{.Size}}"
docker images --format "{{.CreatedAt}}\t{{.Repository}}:{{.Tag}}" | sort -k 1 -r
```

查看dangling状态的镜像

dangling images表示TAG为none的镜像

```bash
[root@ubuntu2204 l]#docker images  -f dangling=true
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
<none>       <none>    c012b71a41fc   2 months ago   701MB
```





##### 补充：出现dangling状态的原因

```bash
# 重现dangling状态的容器
# 重现方法1：
# 拉取一个镜像，eg:wordpress
[root@ubuntu2204 l]#docker pull wordpress

# 使用该镜像创建一个容器
[root@ubuntu2204 l]#docker run -d -p 80:80 -name mywordpress wordpress
d6facffb0290702f0a83d3798b3de7d4f6fad59ec378be8d172d8da0e7dead1c

# 查看创建的容器
[root@ubuntu2204 l]#docker ps
CONTAINER ID   IMAGE       COMMAND                   CREATED         STATUS        PORTS                               NAMES
d6facffb0290   wordpress   "docker-entrypoint.s…"   3 seconds ago   Up 1 second   0.0.0.0:80->80/tcp, :::80->80/tcp   mywordpress

# 在容器运行的状态下，强行删除镜像
[root@ubuntu2204 l]#docker rmi -f wordpress:latest
Untagged: wordpress:latest
Untagged: wordpress@sha256:b60e01ce06202c836b46d54cb3eceba3a6f30950491e6805ce17d840ff6943c0

# 查看镜像，之前的wordpress镜像，变成了dangling状态的镜像
[root@ubuntu2204 l]#docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
alpine       latest    b0c9d60fc5e3   3 weeks ago    7.83MB
nginx        latest    9bea9f2796e2   2 months ago   192MB
<none>       <none>    c012b71a41fc   2 months ago   701MB

# 恢复该镜像
[root@ubuntu2204 l]#docker tag c012b71a41fc wordpress:latest
[root@ubuntu2204 l]#docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
alpine       latest    b0c9d60fc5e3   3 weeks ago    7.83MB
nginx        latest    9bea9f2796e2   2 months ago   192MB
wordpress    latest    c012b71a41fc   2 months ago   701MB

# 重现方法2：
# Docker save 使用IMAGE ID导出，在导入后的镜像没有REPOSITORY和TAG,显示为<none>
[root@ubuntu2204 images]#docker save `docker images -qa` -o mynone.tar

# 将生成的tar包，将其传到另一个机器上
[root@ubuntu2204 images]#scp mynone.tar 10.0.0.101:

# 然后导入docker
[root@ubuntu2204 ~]#docker load -i mynone.tar 

# 查看镜像
[root@ubuntu2204 ~]#docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
<none>       <none>    b0c9d60fc5e3   3 weeks ago    7.83MB
<none>       <none>    9bea9f2796e2   2 months ago   192MB
<none>       <none>    c012b71a41fc   2 months ago   701MB
```



##### 查看指定镜像的详细信息

```bash
# docker inspect <镜像名:Tags>
[root@ubuntu2204 l]#docker inspect nginx:latest
[
    {
        "Id": "sha256:9bea9f2796e236cb18c2b3ad561ff29f655d1001f9ec7247a0bc5e08d25652a1",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206a"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2024-11-26T18:42:08Z",
        "DockerVersion": "",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.27.3",
                "NJS_VERSION=0.8.7",
                "NJS_RELEASE=1~bookworm",
                "PKG_RELEASE=1~bookworm",
                "DYNPKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 191717838,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/1249b5e460970bc0669325f672f717926c587d2c90e5fb83acd0e8b2a7f2ac5a/diff:/var/lib/docker/overlay2/9656448c1b2636d76bd98557faad6c8caf5a0d1ad84f2e5bead8b6347fc7ad77/diff:/var/lib/docker/overlay2/0dde63244c35f47fdb37dc8d59c6675c71d522910ae5caa9539a622f2598b634/diff:/var/lib/docker/overlay2/5e09fb9bb9e90097695a35f40ae7ac5e30d97ef9d899f550d435b8cf6bf5aa74/diff:/var/lib/docker/overlay2/1c7db90446e2df6c7a062ed3519d0c42ac36d6ec04cd8d1eb1090a796c4ea76c/diff:/var/lib/docker/overlay2/7c5ef05f1f440ea899031a98ee13da160e10cf1446e6abc4c26d12b99b2ce59e/diff",
                "MergedDir": "/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/merged",
                "UpperDir": "/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/diff",
                "WorkDir": "/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:f5fe472da25334617e6e6467c7ebce41e0ae5580e5bd0ecbf0d573bacd560ecb",
                "sha256:88ebb510d2fb3ed50f4268455a38443074cad5c6957f6d2cd0126c899a159e6e",
                "sha256:9431321431991c4e64246007e04602160bca8984439ff96461fb992072dd49af",
                "sha256:32c977818204dc910140b3b7abcad06a6613dd1f511ce8f33626a364a3bb68b6",
                "sha256:541cf9cf006d6c9920e5897bf63a4dce0ae1a8388bc82bfa1abedc48b8eb1de9",
                "sha256:58045dd06e5b2c1220ab200c36b450ce3adbfd3fa0f8e3c2c17ffaf7f2906455",
                "sha256:b57b5eac2941c7c1f1f5bc2391123e553d0082eb8e1c6675101aab47a11b26ee"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
```



#### 镜像导出

利用docker save命令可以将从本地镜像导出为一个打包 tar文件，然后复制到其他服务器进行导入使用

注意：镜像导出支持多个镜像导出

格式

```bash
docker save [OPTIONS] IMAGE [IMAGE...]
选项: 
-o, --output string   Write to a file, instead of STDOUT

# 说明
Docker save 使用IMAGE ID导出，在导入后的镜像没有REPOSITORY和TAG,显示为<none>
```

常见用法

```bash
#导出为tar格式
docker save -o /path/file.tar IMAGE1 IMAGE2 ...
docker save IMAGE1 IMAGE2 ... > /path/file.tar

#导出为压缩格式
docker save IMAGE1 IMAGE2 ... | gzip > /path/file.tar.gz
```

范例

```bash
# 导出所有镜像至不同的文件中
[root@centos8 ~]#docker images | awk 'NR!=1{print $1,$2}' | while read repo tag ;do docker save $repo:$tag -o ~/images/$repo-$tag.tar ;done

[root@ubuntu2204 images]#ls
alpine-latest.tar  nginx-latest.tar  wordpress-latest.tar
```

导出所有镜像到一个打包文件

```bash
#方法1: 使用image ID导出镜像,在导入后的镜像没有REPOSITORY和TAG,显示为<none>
[root@ubuntu1804 ~]#docker save `docker images -qa` -o all.tar

#方法2:将所有镜像导入到一个文件中,此方法导入后可以看REPOSITORY和TAG
[root@ubuntu1804 ~]#docker save `docker images | awk 'NR!=1{print $1":"$2}'` -o all.tar

#方法3:将所有镜像导入到一个文件中,此方法导入后可以看REPOSITORY和TAG
[root@centos8 ~]#docker image save `docker image ls --format "{{.Repository}}:{{.Tag}}"` -o all.tar
 [root@centos8 ~]#docker image save `docker image ls --format "{{.Repository}}:{{.Tag}}"` | gzip > all.tar.gz
```



#### 镜像导入

利用docker load命令可以将镜像导出的打包或压缩文件再导入

注意：镜像导入只能支持单个镜像导入，不支持多个镜像导入

格式

```bash
docker load [OPTIONS]

#选项
-i, --input string    # Read from tar archive file, instead of STDIN
-q, --quiet           # Suppress the load output
```

常见用法

```bash
docker load -i /path/file.tar
docker load < /path/file.tar.gz
```

镜像导入

```bash
[root@centos7 ~]# docker load -i /data/myimages.tar
#或者
[root@centos7 ~]# docker load < /data/myimages.tar
```



#### 删除镜像

docker rmi 命令可以删除本地镜像

格式

```bash
docker rmi [OPTIONS] IMAGE [IMAGE...]
docker image rm [OPTIONS] IMAGE [IMAGE...]

 #选项:
 -f, --force     # Force removal of the image
 --no-prune      # Do not delete untagged parents
```



#### 清理dangling状态的镜像

dangling images表示TAG为None的镜像

```bash
#dangling images表示TAG为<none>的镜像	
# 查看所有dangling状态的镜像
[root@ubuntu2204 ~]#docker images -q -f dangling=true

# 删除
[root@ubuntu2204 ~]#docker rmi -f `docker images -q -f dangling=true`
```

 清除dangling和不再使用的镜像

```bash
[root@ubuntu1804 ~]#docker image prune -a -f
```



#### 镜像打标签

docker tag 可以给镜像打标签，类似于起别名,但通常要遵守一定的命名规范,才可以上传到指定的仓库

格式

```bash
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

# TARGET_IMAGE[:TAG]格式一般形式
# 仓库主机FQDN或IP[:端口]/项目名(或用户名)/image名字:版本
# TAG默认为latest
```





### 容器操作命令

#### 容器生命周期

![image-20250202145303954](D:\git_repository\cyber_security_learning\markdown_img\image-20250202145303954.png)



#### 启动容器用法

命令格式

```bash
docker run [选项]  [镜像名]  [shell命令] [参数]

#选项:  
-i, --interactive   # Keep STDIN open even if not attached，通常和-t一起使用
-t, --tty           # 分配pseudo-TTY，通常和-i一起使用,注意对应的容器必须运行shell才支持进入
-d, --detach        # Run container in background and print container ID,台后运行，默认前台
--name string       # Assign a name to the container
--h, --hostname string  # Container host name
--rm                # Automatically remove the container when it exits
-p, --publish list  # Publish a container's port(s) to the host
-P, --publish-all   # Publish all exposed ports to random ports
--dns list          # Set custom DNS servers
--entrypoint string # Overwrite the default ENTRYPOINT of the image
--restart policy    # 后续详解
--privileged        # Give extended privileges to container
-e, --env=[]        # Set environment variables
--env-file=[]       # Read in a line delimited file of environment variables
--sysctl net.ipv4.ip_unprivileged_port_start=0 #指定容器的内核参数,但不修改宿主机内核
--ulimit ulimit     #指定ulimit限制配置，比如： --ulimit nofile=10240:10240

[shell命令] [参数]   #使用指定的命令和参数，替换容器默认的命令 
```



##### 详解--restart的四种policy

```bash
# no: 默认策略，不会自动重启容器
docker run --name mycontainer --restart no myimage

# no-failure[:max-retries]: 如果容器因错误退出（非零退出码），则重启容器，可以选择性地指定最大重启次数
docker run --name mycontainer --restart on-failure:5 myimage

# always：无论容器因何原因停止，都会重启容器。如果手动停止容器，只有在Docker守护进程重启或手动重启容器时才会重新启动(这里意味容器因错误退出可能导致无限重启，所以建议在这里配置一个监控项并设置报警或者触发器，以防止容器重现重启导致的负载上升)
docker run --name mycontainer --restart always myimage

# unless-stopped：类似于always，但如果容器被手动停止，则不会在Docker守护进程重启后重新启动
docker run --name mycontainer --restart unless-stopped myimage

# always和unless-stopped都可以实现开机自启，不同点在于，如果手动停止容器后，重启docker进程，比如systemctl restart docker,此时always会重启容器，而unless-stopped不会
```

```ABAP
一个容器要持续运行，条件：在镜像中有一个持续运行并以前台方式运行的进程作为容器启动的默认程序
- 持续运行
- 启动程序以前台方式运行
```

注意: 容器启动后,如果容器内没有前台运行的进程,将自动退出停止



##### 从容器中退出

```bash
# 使用-it进入容器，然后使用exit退出
[root@ubuntu2204 ~]#docker run -it --name myapline alpine
/ # exit

# exit之后，容器是Exited状态
[root@ubuntu2204 ~]#docker ps -a
CONTAINER ID   IMAGE       COMMAND                   CREATED         STATUS                      PORTS                               NAMES
c66494c6babc   alpine      "/bin/sh"                 6 minutes ago   Exited (0) 26 seconds ago                                       myapline

# 使用staret和attach重新进入容器
[root@ubuntu2204 ~]#docker start myapline 
myapline
[root@ubuntu2204 ~]#docker attach myapline 
/ # #同时按三个键:ctrl+p+q

# #用同时按三个键ctrl+p+q退出后容器不会停止
[root@ubuntu2204 ~]#docker ps
CONTAINER ID   IMAGE       COMMAND                   CREATED         STATUS              PORTS                               NAMES
c66494c6babc   alpine      "/bin/sh"                 8 minutes ago   Up About a minute                                       myapline
```



##### 一次性运行容器，退出后立即删除，用于测试

```bash
[root@ubuntu2204 ~]#docker run --rm alpine cat /etc/resolv.conf
# Generated by Docker Engine.
# This file can be edited; Docker Engine will not make further changes once it
# has been modified.

nameserver 180.76.76.76
nameserver 223.6.6.6
search wang.org

# Based on host file: '/run/systemd/resolve/resolv.conf' (legacy)
# Overrides: []
```



#####  设置容器内的主机名

```bash
[root@ubuntu2204 ~]#docker run --rm -h a1.mystical.org alpine hostname
a1.mystical.org
```



##### 使用--privileged 让容器获取 root 权限

```bash
[root@ubuntu2204 ~]#docker run -it --name myubuntu ubuntu:22.04
root@2f482ba39e27:/# sysctl -w net.ipv4.ip_forward=1
sysctl: setting key "net.ipv4.ip_forward", ignoring: Read-only file system

# 提权为root权限
[root@ubuntu2204 ~]#docker run -it --name myubuntu --privileged ubuntu:22.04
root@51b83f476575:/# sysctl -w net.ipv4.ip_forward=1
net.ipv4.ip_forward = 1
```



##### 修改容器的内核参数

```bash
[root@ubuntu2204 ~]#docker run --name mynginx  --sysctl net.ipv4.icmp_echo_ignore_all=1 -d nginx 
01d3b844929590d6b0469e77ec1f6b8c4f54ce88c1baab6decaacbd2eadf4eca

# 进入容器查看
[root@ubuntu2204 ~]#docker exec -it mynginx /bin/bash
root@01d3b8449295:/# cat /proc/sys/net/ipv4/icmp_echo_ignore_all 
1

# 容器外不受影响
[root@ubuntu2204 /]#cat /proc/sys/net/ipv4/icmp_echo_ignore_all
0
```



##### 限制容器内部的资源使用

Docker 支持多个 `ulimit` 限制项，以下是常见的限制资源及其作用：

| 选项      | 作用                                                | 示例                        |
| --------- | --------------------------------------------------- | --------------------------- |
| `nofile`  | 限制 **最大文件描述符数（打开的文件数量）**         | `--ulimit nofile=1024:2048` |
| `nproc`   | 限制 **最大进程数**                                 | `--ulimit nproc=50`         |
| `memlock` | 限制 **进程可锁定的最大内存量（防止锁住过多内存）** | `--ulimit memlock=64M:64M`  |
| `stack`   | 限制 **线程栈大小**                                 | `--ulimit stack=8M:16M`     |
| `cpus`    | 限制 **CPU 数**                                     | `--ulimit cpus=1`           |
| `fsize`   | 限制 **最大文件大小**                               | `--ulimit fsize=100M`       |
| `core`    | 限制 **Core Dump 文件大小**                         | `--ulimit core=0`           |
| `rtprio`  | 限制 **实时调度优先级**                             | `--ulimit rtprio=10`        |

**`--ulimit` 具体使用示例**

**限制容器的最大打开文件数**

**场景：** 防止单个容器打开太多文件句柄，导致宿主机资源耗尽。

```bash
docker run -d --ulimit nofile=1024:2048 nginx
```

- `1024`：软限制（Soft Limit，警告但允许超出）。

- `2048`：硬限制（Hard Limit，不能超过此值）。

验证限制是否生效

```bash
docker exec -it <container_id> bash
ulimit -n   # 1024，表示容器最多可以打开 1024 个文件。
```



**限制容器最大进程数**

**场景：** 防止容器内创建 **过多进程**，导致宿主机 **负载过高**。

```bash
# 最大允许 100 个进程。
docker run -d --ulimit nproc=100 ubuntu
```

**验证限制**

```bash
docker exec -it <container_id> bash
ulimit -u
```



**限制容器的 CPU 使用**

**场景：** 使用 `--cpus` 限制 CPU 数，防止高 CPU 负载影响其他进程。

```bash
# 限制容器最多使用 1 个 CPU 核心
docker run -d --cpus=1 ubuntu
```



**限制容器的内存锁定**

**场景：** 防止容器锁定大量内存，影响宿主机的正常运行。

```bash
# 限制容器内最大可锁定内存量为 64M
docker run -d --ulimit memlock=64M:64M ubuntu
```

 **验证内存锁定**

```bash
docker exec -it <container_id> bash
ulimit -l
```



#### 查看容器信息

##### 显示当前存在容器

格式

```bash
docker ps [OPTIONS]
docker container ls [OPTIONS]

# 选项
-a, --all            # Show all containers (default shows just running)
-q, --quiet          # Only display numeric IDs
-s, --size           # Display total file sizes
-f, --filter filter  # Filter output based on conditions provided
-l, --latest         # Show the latest created container (includes all states)
-n, --last int       # Show n last created containers (includes all states) (default -1)
    --format         # 按格式输出信息           
```

docker ps --format 命令中，你可以使用不同的占位符来指定要在输出中显示的容器信息。

```bash
#以下是一些常用的占位符：
{{.ID}}          # 容器的ID。
{{.Image}}       # 容器使用的映像名称。
{{.Command}}     # 容器的启动命令。
{{.CreatedAt}}   # 容器的创建时间。
{{.RunningFor}}  # 容器运行的时间。
{{.Ports}}       # 容器的端口映射信息。
{{.Status}}      # 容器的状态。
{{.Size}}        # 容器的大小。
{{.Names}}       # 容器的名称。
{{.Label}}       # 容器的标签。

# 示例
[root@ubuntu2204 /]#docker ps --format "{{.ID}}\t{{.Image}}\t{{.Status}}"
01d3b8449295	nginx	    Up 2 hours
2bc478010524	wordpress	Up 3 hours
```

 显示指定状态的容器

```bash
# 查看退出状态的容器
[root@ubuntu2204 /]#docker ps -f "status=exited"
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# 查看运行中的容器
[root@ubuntu2204 /]#docker ps -f "status=running"
CONTAINER ID   IMAGE       COMMAND                   CREATED       STATUS       PORTS                               NAMES
01d3b8449295   nginx       "/docker-entrypoint.…"   2 hours ago   Up 2 hours   80/tcp                              mynginx
2bc478010524   wordpress   "docker-entrypoint.s…"   3 hours ago   Up 3 hours   0.0.0.0:80->80/tcp, :::80->80/tcp   mywordpres
```



##### 查看容器内的进程

```bash
docker top CONTAINER [ps OPTIONS]
```

示例

```bash
[root@ubuntu2204 /]#docker top mynginx 
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                3146                3126                0                   20:01               ?                   00:00:00            nginx: master process nginx -g daemon off;
systemd+            3192                3146                0                   20:01               ?                   00:00:00            nginx: worker process
systemd+            3193                3146                0                   20:01               ?                   00:00:00            nginx: worker process
root                3261                3126                0                   20:02               pts/0               00:00:00            /bin/bash
```



##### 查看容器资源使用情况

```bash
docker stats [OPTIONS] [CONTAINER...]

Display a live stream of container(s) resource usage statistics
 
# options
-a, --all             # Show all containers (default shows just running)
    --format string   # Pretty-print images using a Go template
    --no-stream       # Disable streaming stats and only pull the first result
    --no-trunc        # Do not truncate output
```

示例

```bash
[root@ubuntu2204 /]#docker stats --no-stream mynginx
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O       BLOCK I/O         PIDS
01d3b8449295   mynginx   0.00%     5.312MiB / 3.785GiB   0.14%     1.29kB / 0B   16.3MB / 24.6kB   4
```



##### 查看容器的详细信息

**docker inspect** 可以查看docker各种对象的详细信息,包括:镜像,容器,网络等

```bash
docker inspect [OPTIONS] NAME|ID [NAME|ID...]

# Options:
-f, --format string   # Format the output using the given Go template
-s, --size            # Display total file sizes if the type is container
```

示例

```bash
# 全部查看
[root@ubuntu2204 /]#docker inspect mynginx

# 选择性查看
[root@ubuntu2204 /]#docker inspect -f "{{.State.Status}}" mynginx
running

[root@ubuntu2204 /]#docker inspect -f "{{.NetworkSettings.Networks.bridge.IPAddress}}" mynginx
172.17.0.3

[root@ubuntu2204 /]#docker inspect -f "{{.Created}}" mynginx
2025-02-02T12:01:25.168043364Z
```



#### 删除容器

docker rm 可以删除容器，即使容器正在运行当中，也可以被强制删除掉

格式

```bash
docker rm [OPTIONS] CONTAINER [CONTAINER...]
docker container rm [OPTIONS] CONTAINER [CONTAINER...]

# 选项:  
-f, --force     # Force the removal of a running container (uses SIGKILL)
-v, --volumes   # Remove the volumes associated with the container

# 删除停止的容器
docker container prune [OPTIONS]

# 选项：
--filter filter   # Provide filter values (e.g. 'until=<timestamp>')
-f, --force       # Do not prompt for confirmation
```

示例

```bash
# 正在运行的容器，要先停止再删除
[root@ubuntu2204 /]#docker stop mynginx 
mynginx
[root@ubuntu2204 /]#docker rm mynginx 
mynginx

# 强行删除运行中的容器
[root@ubuntu2204 /]#docker rm -f mywordpress 
mywordpress

# 删除所有停止的容器
[root@ubuntu1804 ~]#docker rm `docker ps -qf status=exited`
[root@ubuntu1804 ~]#docker ps -f status=exited -q  | xargs docker rm -f
[root@ubuntu1804 ~]#docker container prune  -f 
```



#### 容器的启动和停止

格式

```ABAP
docker start|stop|restart|pause|unpause 容器ID|容器name
```

批量正常启动或关闭所有容器

```ABAP
docker start $(docker ps -a -q)  
docker stop $(docker ps -a -q) 
```

##### 补充：stop和pause的区别

**✅ `docker pause` vs `docker stop`**

| **操作**       | **作用**         | **进程是否终止** | **是否释放 CPU 资源** | **是否释放内存** |
| -------------- | ---------------- | ---------------- | --------------------- | ---------------- |
| `docker pause` | **暂停**容器进程 | ❌ 进程保留       | ✅ CPU 停止使用        | ❌ 仍占用内存     |
| `docker stop`  | **停止**容器     | ✅ 进程终止       | ✅ CPU 释放            | ✅ 释放内存       |



✅ **`docker pause` 的工作原理**

Docker 使用 **`cgroup freezer`** 机制来暂停容器

- **`FREEZE` 状态**：所有进程被挂起，CPU 不再调度该容器的进程。
- **`THAW` 状态**（恢复）：`docker unpause` 解除暂停，恢复进程调度。

示例

```bash
# 暂停一个运行中的容器
[root@ubuntu2204 /]# docker run -d --name mynginx nginx
[root@ubuntu2204 /]# docker pause mynginx

# 此时容器不会继续执行任务，但不会被销毁。
# 检查容器状态,STATUS 显示 (Paused)，表示该容器已暂停
[root@ubuntu2204 /]# docker ps
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS                NAMES
f3b1d0a98d0b   nginx   "nginx"   2 mins    Up 2 mins (Paused)    mynginx

# 解除暂停
[root@ubuntu2204 /]# docker unpause mynginx
```



#### 给正在运行的容器发信号

docker kill  可以给容器发信号,默认号SIGKILL,即9信号

**`docker kill` 的本质是** **从容器外部向容器内的 `PID 1` 进程发送信号**

格式

```bash
docker kill [OPTIONS] CONTAINER [CONTAINER...]

#选项:
-s, --signal string   Signal to send to the container (default "KILL")
```

示例

```bash
[root@ubuntu2204 /]#docker run -d -p 80:80 --name mynginx nginx
6c009fc597dbc1535e0f0affc3562a80f21f50126a76979caaad0f6390941325

[root@ubuntu2204 /]#docker ps
CONTAINER ID   IMAGE     COMMAND                   CREATED         STATUS         PORTS                               NAMES
6c009fc597db   nginx     "/docker-entrypoint.…"   6 seconds ago   Up 4 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   mynginx

[root@ubuntu2204 /]#docker kill 6c009fc597db
6c009fc597db

[root@ubuntu2204 /]#docker ps -a
CONTAINER ID   IMAGE     COMMAND                   CREATED          STATUS                        PORTS     NAMES
6c009fc597db   nginx     "/docker-entrypoint.…"   40 seconds ago   Exited (137) 21 seconds ago             mynginx
```



#### 进入正在运行的容器

注意：容器只有正在运行状态时，才能进入

##### 使用attach命令

docker attach 容器名，attach 类似于vnc，操作会在同一个容器的多个会话界面同步显示，所有使用此方式进入容器的操作都是同步显示的，且使用exit退出后容器自动关闭，**不推荐使用**，需要进入到有shell环境的容器

格式: 

```ABAP
docker attach [OPTIONS] CONTAINER
```

示例

```bash
# 启动一个alpine容器
[root@ubuntu2204 ~]#docker run -it --name myalpine alpine

# ctrl + q + p 退出
# 查看状态
[root@ubuntu2204 ~]#docker ps
CONTAINER ID   IMAGE     COMMAND     CREATED          STATUS          PORTS     NAMES
16ee7828079d   alpine    "/bin/sh"   17 seconds ago   Up 15 seconds             myalpine

# attach进入容器
[root@ubuntu2204 ~]#docker attach myalpine

# 在另一个会话中，也使用attach进入容器
[root@ubuntu2204 /]#docker attach myalpine

# 在任意会话中，执行ls
[root@ubuntu2204 /]#docker attach myalpine
/ # ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr

# 两个会话同时都会出现ls的执行结果
/ # exit

# exit退出，两个会话同时退出
```



##### 使用exec命令

在运行中的容器启动新进程,可以执行单次命令，以及进入容器

测试环境使用此方式，**使用exit退出,但容器还在运行**，此为推荐方式

格式

```bash
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

# 常用选项
-d, --detach           # Detached mode: run command in the background
-e, --env list         # Set environment variables
-i, --interactive      # Keep STDIN open even if not attached
-t, --tty              # Allocate a pseudo-TTY

#常见用法
docker exec -it 容器ID sh|bash
```



#### 暴露容器端口

##### 暴露所有容器端口

容器启动后,默认处于预定义的NAT网络中,所以外部网络的主机无法直接访问容器中网络服务

docker run -P  可以将事先容器预定义的所有端口映射宿主机的网卡的随机端口，默认从32768开始

使用随机端口时,当停止容器后再启动可能会导致端口发生变化

```bash
-P , --publish-all= true | false默认为false

#示例:
docker run -P docker.io/nginx  #映射容器所有暴露端口至随机本地端口
```

**docker port 可以查看容器的端口映射关系**

格式

```ABAP
docker port CONTAINER [PRIVATE_PORT[/PROTO]]
```

范例

```bash
[root@ubuntu2204 ~]#docker run -d --name mynginx -P nginx
7c9191c1b96a1609535a3622b7c528818270587d09e5edd98d410e414472730d

[root@ubuntu2204 ~]#docker port mynginx
80/tcp -> 0.0.0.0:32769
80/tcp -> [::]:32769

# 更改index.html文件
[root@ubuntu2204 ~]#echo hello > index.html
[root@ubuntu2204 ~]#docker cp index.html mynginx:/usr/share/nginx/html/
Successfully copied 2.05kB to mynginx:/usr/share/nginx/html/

# 测试
[root@ubuntu2204 ~]#curl 127.1:32769
hello
```

**端口映射的本质就是利用NAT技术实现的**

```bash
# 查看宿主机防火墙
[root@ubuntu2204 ~]#iptables -t nat -vnL|grep 32769
    0     0 DNAT       tcp  --  !docker0 *       0.0.0.0/0            0.0.0.0/0            tcp dpt:32769 to:172.17.0.2:80
```



##### 指定端口映射

docker run -p 可以将容器的预定义的指定端口映射到宿主机的相应端口

注意:  多个容器映射到宿主机的端口不能冲突，但容器内使用的端口可以相同 

方式1:  容器80端口映射宿主机本地随机端口

```bash
docker run  -p 80 --name nginx-test-port1 nginx
```

方式2:  容器80端口映射到宿主机本地端口81

```bash
docker run  -p 81:80 --name nginx-test-port2 nginx
```

方式3:  宿主机本地IP:宿主机本地端口:容器端口

```bash
docker run  -p 10.0.0.100:82:80 --name nginx-test-port3 docker.io/nginx
```

方式4:  宿主机本地IP:宿主机本地随机端口:容器端口，默认从32768开始

```bash
docker run -p 10.0.0.100::80 --name nginx-test-port4 docker.io/nginx
```

方式5:  宿主机本机ip:宿主机本地端口:容器端口/协议，默认为tcp协议

```bash
docker run  -p 10.0.0.100:83:80/udp --name nginx-test-port5 docker.io/nginx
```

方式6:  一次性映射多个端口+协议

```bash
docker run  -p 8080:80/tcp -p 8443:443/tcp -p 53:53/udp --name nginx-test-port6 nginx
```

**实战案例: 修改已经创建的容器的端口映射关系**

```bash
# 创建一个nginx容器，并暴露本机80端口
[root@ubuntu2204 ~]#docker run -d -p 80:80 --name mynginx nginx
a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8

# 查看状态
[root@ubuntu2204 a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8]#docker port mynginx
80/tcp -> 0.0.0.0:80
80/tcp -> [::]:80

# 查看完整的容器ID
[root@ubuntu2204 ~]#docker inspect mynginx|grep -i 'id'
        "Id": "a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8",
        
# 进入容器数据目录，找到元数据文件，并修改
[root@ubuntu2204 ~]#cd /var/lib/docker/containers/a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8

# stop停止容器
[root@ubuntu2204 a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8]# docker stop mynginx
mynginx
# 查看该目录下的文件
[root@ubuntu2204 a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8]# ls
a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8-json.log  hostconfig.json  mounts
checkpoints                                                                hostname         resolv.conf
config.v2.json                                                             hosts            resolv.conf.hash

# 查看hostconfig.json
[root@ubuntu2204 a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8]# cat hostconfig.json |jq
{
  "Binds": null,
  "ContainerIDFile": "",
  "LogConfig": {
    "Type": "json-file",
    "Config": {}
  },
  "NetworkMode": "bridge",
  "PortBindings": {
    "80/tcp": [
      {
        "HostIp": "",
        "HostPort": "80"   # 这里改为8000
      }
    ]
  },
  "RestartPolicy": {
    "Name": "no",
    "MaximumRetryCount": 0
  },
  ......
  
# 修改完端口后，重启docker服务
[root@ubuntu2204 a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8]# systemctl restart docker
[root@ubuntu2204 a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8]# docker start mynginx
mynginx

# 再次查看，已修改端口号
[root@ubuntu2204 a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8]#docker port mynginx
80/tcp -> 0.0.0.0:8000
80/tcp -> [::]:8000
```



#### 查看容器的日志

docker logs 可以查看容器中运行的进程在控制台的标准输出和标准错误，一般对应是日志信息

docker 日志是存放在宿主机的 `/var/lib/docker/containers//-json.log`文 件中

```bash
# 查看image_ID
[root@ubuntu2204 ~]#docker inspect mynginx|grep -i 'id'
        "Id": "a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8",

# 进入该目录下，查看<id>_json.log
[root@ubuntu2204 ~]#ls /var/lib/docker/containers/a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8
a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8-json.log  hostconfig.json  mounts
checkpoints                                                                hostname         resolv.conf
config.v2.json                                                             hosts            resolv.conf.hash

# 查看该日志文件
[root@ubuntu2204 ~]# cat /var/lib/docker/containers/a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8/a38b2ad1e33c2574da35edc7d284b43b4963389e79510d04cc23e277ee402ac8-json.log 
```

格式

```bash
docker logs [OPTIONS] CONTAINER

# 选项
--details        # Show extra details provided to logs
-f, --follow     # Follow log output
--since string   # Show logs since timestamp (e.g.2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes)
--tail string    # Number of lines to show from the end of the logs (default "all")
-t, --timestamps # Show timestamps
--until string   # Show logs before a timestamp (e.g. 2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes)
```

示例：持续查看nginx访问日志

```bash
# 在10.0.0.100上持续查看mynginx容器的日志
[root@ubuntu2204 ~]#docker logs -f mynginx

# 在10.0.0.101上访问
[root@ubuntu2204 ~]#curl 10.0.0.100:8000

# 在10.0.0.100上的日志显示
10.0.0.101 - - [03/Feb/2025:02:52:08 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/7.81.0" "-"
```



#### 传递运行命令

容器需要有一个前台运行的进程才能保持容器的运行，可以在构建镜像的时候指定容器启动时运行的前 台命令，也可以通过启动容器时传递运行参数实现

容器里的PID为1的守护进程的实现方式

- 服务类:  如:  Nginx，Tomcat，Apache ，但服务不能停
- 命令类:  如:  tail -f  /etc/hosts ，主要用于测试环境，注意:  不要tail -f <服务访问日志>  会产生不必要的磁盘IO

示例

```bash
[root@ubuntu2204 ~]# docker run -d --name myalpine alpine tail -f /etc/hosts
8796b4458f633823a5eaaafee8876eb5079a790268a0c8a3270d7b01b38916e7

# 此时查看，容器处于运行中状态
[root@ubuntu2204 ~]# docker ps
CONTAINER ID   IMAGE     COMMAND                   CREATED          STATUS          PORTS                                   NAMES
8796b4458f63   alpine    "tail -f /etc/hosts"      3 seconds ago    Up 2 seconds                                            myalpine
```



#### 容器内部的hosts文件

容器会自动将容器的ID加入自已的/etc/hosts文件中，并解析成容器的IP

示例

```bash
[root@ubuntu2204 ~]#docker exec myalpine cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.3	8796b4458f63    #默认会将实例的ID 添加到自己的hosts文件

[root@ubuntu2204 ~]#docker exec myalpine ping 8796b4458f63
PING 8796b4458f63 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.079 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.135 ms
......
```

修改容器的 hosts文件

```bash
[root@ubuntu2204 ~]#docker run -it --rm --add-host www.mystical.com:6.6.6.6 --add-host www.mystical.org:8.8.8.8 alpine
/ # cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
6.6.6.6	www.mystical.com
8.8.8.8	www.mystical.org
172.17.0.4	d332cdde61b8
```



#### 指定容器 DNS

容器的dns服务器，默认采用宿主机的dns 地址，可以用下面方式指定其它的DNS地址

- 修改宿主机的DNS地址址配置
- 在容器启动时加选项 `--dns=x.x.x.x`
- 在/etc/docker/daemon.json 文件中指定

范例:  容器的DNS默认从宿主机的DNS获取

```bash
# 查看宿主机DNS
[root@ubuntu2204 ~]#resolvectl status
......
Link 2 (eth0)
    Current Scopes: DNS
         Protocols: +DefaultRoute +LLMNR -mDNS -DNSOverTLS DNSSEC=no/unsupported
Current DNS Server: 180.76.76.76
       DNS Servers: 180.76.76.76 223.6.6.6
        DNS Domain: wang.org

# 查看容器内DNS
[root@ubuntu2204 ~]# docker run --rm  alpine cat /etc/resolv.conf
# Generated by Docker Engine.
# This file can be edited; Docker Engine will not make further changes once it
# has been modified.

nameserver 180.76.76.76
nameserver 223.6.6.6
search wang.org
......
```

示例：指定DNS地址

```bash
[root@ubuntu2204 ~]#docker run --rm --dns 1.1.1.1 --dns 8.8.8.8 alpine cat /etc/resolv.conf
# Generated by Docker Engine.
# This file can be edited; Docker Engine will not make further changes once it
# has been modified.

nameserver 1.1.1.1
nameserver 8.8.8.8
```

示例：指定domain名

```bash
[root@ubuntu2204 ~]#docker run --rm --dns 1.1.1.1 --dns 8.8.8.8 --dns-search a.com --dns-search b.com  alpine cat /etc/resolv.conf
......
nameserver 1.1.1.1
nameserver 8.8.8.8
search a.com b.com
......
```

示例：配置文件指定DNS和搜索domain名

```bash
[root@ubuntu1804 ~]#vim /etc/docker/daemon.json 
[root@ubuntu1804 ~]#cat /etc/docker/daemon.json 
{
 "storage-driver": "overlay2",
 "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"],
 "dns" : [  "114.114.114.114", "119.29.29.29"],
 "dns-search": [ "magedu.com", "wang.org"]
}
 
[root@ubuntu1804 ~]#systemctl restart docker
[root@ubuntu1804 ~]#docker run -it --rm   centos bash
[root@7a2d8fac6f6b /]# cat /etc/resolv.conf 
search magedu.com wang.org
nameserver 114.114.114.114
nameserver 119.29.29.29
[root@7a2d8fac6f6b /]# exit
exit
 
#用--dns指定优先级更高
[root@ubuntu1804 ~]#docker run -it --rm  --dns 8.8.8.8 --dns 8.8.4.4 centos bash
[root@80ffe3547b87 /]# cat /etc/resolv.conf 
search magedu.com wang.org
nameserver 8.8.8.8
nameserver 8.8.4.4
[root@80ffe3547b87 /]# exit
exit
```



#### 容器内和宿主机之间复制文件

不论容器的状态是否运行，复制都可以实现

```bash
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH
docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH

# 选项
-a, --archive        # Archive mode (copy all uid/gid information)
-L, --follow-link    # Always follow symbol link in SRC_PATH
```

范例： 复制容器的文件至宿主机

```bash
[root@ubuntu2004 ~]#docker run -it --name b1  busybox sh
[root@ubuntu2004 ~]#docker cp  b1:/bin/busybox /usr/local/bin/
[root@ubuntu2004 ~]#busybox ls
```

示例

```bash
[root@ubuntu1804 ~]#docker run -itd centos
1311fe67e6708dac71c01f7d1752a6dcb5e85c2f1fa4ac2efcef9edfe4fb6bb5
[root@ubuntu1804 ~]#docker ps
......

#将容器内文件复制到宿主机
[root@ubuntu1804 ~]#docker cp -a 1311:/etc/centos-release .
[root@ubuntu1804 ~]#cat centos-release 
CentOS Linux release 8.1.1911 (Core) 

#将宿主机文件复制到容器内
[root@ubuntu1804 ~]#docker cp /etc/issue  1311:/root/
[root@ubuntu1804 ~]#docker exec 1311 cat /root/issue
Ubuntu 18.04.1 LTS \n \l
```



#### 传递环境变量

有些容器运行时，需要传递变量，可以使用 -e <参数> 或 --env-file <参数文件> 实现

范例:  传递变量创建MySQL

```bash
#MySQL容器运行时需要指定root的口令
[root@ubuntu1804 ~]#docker run --name mysql-test1 -v /data/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=wordpress -e MYSQL_USER=wpuser -e MYSQL_PASSWORD=123456 -d -p 3306:3306 mysql:5.7.30

# 使用文件传递变量
[root@ubuntu1804 ~]#docker run --name mysql-test2 -v /root/mysql/:/etc/mysql/conf.d -v /data/mysql2:/var/lib/mysql --env-file=env.list -d -p 3307:3306 mysql:5.7.30

[root@ubuntu1804 ~]#cat mysql/mysql-test.cnf 
[mysqld]
server-id=100
log-bin=mysql-bin

[root@ubuntu1804 ~]#cat env.list 
MYSQL_ROOT_PASSWORD=123456
MYSQL_DATABASE=wordpress
MYSQL_USER=wpuser
MYSQL_PASSWORD=wppass
```



#### 清除不再使用的数据

```bash
#dangling images表示TAG为<none>的镜像
[root@ubuntu2204 ~]#docker system prune
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache

Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B

# 清除不再使用的镜像
[root@ubuntu1804 ~]#docker system  prune -f -a

# 查看docker的系统信息
[root@ubuntu2204 ~]#docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          4         2         903.4MB   778.6MB (86%)
Containers      2         2         1.095kB   0B (0%)
Local Volumes   3         0         222.8MB   222.8MB (100%)
Build Cache     0         0         0B        0B
```



#### 导出和导出容器文件系统

docker export 和  docker save 都可以用于将 Docker 的容器/镜像导出到本地文件系统，但是它们 用途和效果是不同的：

**docker export**：此命令是用于将一个运行的或者停止的容器的文件系统导出为一个 tar 归档文件。需 要注意的是， docker export 不会包含该容器的历史（也就是每个层的变更），并且也不会包含容器 的环境变量、元数据和其他相关的配置信息。这意味着如果你导入一个用  docker export 导出的 tar  文件并运行，你得到的将是一个新的、干净的容器，没有之前容器的运行历史和配置。

**docker save**：此命令用于将一个或多个镜像导出为一个 tar 归档文件。与  docker export 不同， docker save 会完整地保存镜像的所有内容，包括每一层的变更、所有的元数据、所有的标签等。这 意味着如果你导入一个用  docker save 导出的 tar 文件并运行，你得到的将是一个与原镜像完全一样 的新镜像，包括所有的历史和配置。

总结来说， docker export 是用来导出容器的文件系统，而  docker save 是用来导出镜像的全部内容。

```bash
[root@ubuntu2204 ~]#docker export mynginx -o nginx.tar
[root@ubuntu2204 ~]#tar tvf nginx.tar |head
-rwxr-xr-x 0/0               0 2025-02-03 10:30 .dockerenv
lrwxrwxrwx 0/0               0 2025-01-13 08:00 bin -> usr/bin
drwxr-xr-x 0/0               0 2024-12-31 18:25 boot/
drwxr-xr-x 0/0               0 2025-02-03 10:30 dev/
-rwxr-xr-x 0/0               0 2025-02-03 10:30 dev/console
drwxr-xr-x 0/0               0 2025-02-03 10:30 dev/pts/
drwxr-xr-x 0/0               0 2025-02-03 10:30 dev/shm/
drwxr-xr-x 0/0               0 2025-01-14 10:21 docker-entrypoint.d/
-rwxr-xr-x 0/0            2125 2025-01-14 10:20 docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
-rwxr-xr-x 0/0             389 2025-01-14 10:20 docker-entrypoint.d/15-local-resolvers.envsh

# 将容器文件传到另一个服务器上
[root@ubuntu2204 ~]#scp nginx.tar 10.0.0.101:

#import 实现将容器文件生成镜像
[root@ubuntu2204 ~]#docker import nginx.tar nginx:test
sha256:0f9c43c5b5e9b819099236ac75442b1da5399e810a862503b790f53d7eb52db1
[root@ubuntu2204 ~]#docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
nginx        test      0f9c43c5b5e9   7 seconds ago   190MB
```





## Docker镜像制作

### Docker 镜像说明

#### Docker 镜像中有没有内核

从镜像大小上面来说，一个比较小的镜像只有1MB多点或几MB，镜像在被启动为容器后将直接使用宿主机的内核，因此使制作的镜像更小,而镜像本身则只提供相应的rootfs，即系统正常运行所必须的用户空间的文件系统，比如: /dev/，/proc，/bin，/etc等目录，容器当中/boot目录是空的，而/boot当中保存的就是与内核相关的文件和目录。 



#### 为什么没有内核

由于容器启动和运行过程中通常不会直接调用物理硬件，所以也不会涉及到硬件驱动，因此也无需容器内拥有自已的内核和驱动,而是直接使用了宿主机的内核，而如果使用虚拟机技术，对应每个虚拟机都有自已独立的内核



#### 容器中的程序后台运行会导致此容器启动后立即退出

当容器启动时，它会运行一个指定的初始化主进程，通常是容器的PID 1。如果这个主进程退出或停止， 容器也会相应地退出和停止。

在Docker容器中的初始化进程可以被Dockerfile中的ENTRYPOINT或CMD指令所指明；也可以被docker  run命令的启动参数所覆盖。

如果主进程以后台方式（即通过在命令后加上&符号）运行，因为容器认为主进程已经完成，它就会停止整个容器

Docker容器如果希望启动后能持续运行,就必须有一个能**前台持续运行**的进程，如果在容器中启动传统的服务，如:httpd,php-fpm等均为后台进程模式运行,就导致 docker 在前台没有运行的应用,这样的容器启动后会立即退出。所以一般会将服务程序以前台方式运行，对于有一些可能不知道怎么实现前台运行的 程序,只需要在你启动的该程序之后添加类似于 tail ，top 这种可以前台运行的程序即可. 比较常用的方 法，如  tail  -f  /etc/hosts 。

范例:  

```bash
#httpd
ENTRYPOINT [ "/usr/sbin/apache2" ]  
CMD ["-D", "FOREGROUND"] 

#nginx
ENTRYPOINT [ "/usr/sbin/nginx", "-g", "daemon off;" ] 

#用脚本运行容器
c基于容器手动制作镜像步骤at run_haproxy.sh 
#!/bin/bash
haproxy -f /etc/haproxy/haproxy.cfg
tail -f /etc/hosts

tail -n1 Dockerfile 
CMD ["run_haproxy.sh"]
```



### 将现有容器通过 docker commit 手动构建镜像

#### 基于容器手动制作镜像步骤

**docker commit 格式**

```bash
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]

# 选项
-a, --author string    # Author (e.g., "John Hannibal Smith <hannibal@ateam.com>")
-c, --change list      # Apply Dockerfile instruction to the created image
-m, --message string   # Commit message
-p, --pause            # Pause container during commit (default true)

#说明:
制作镜像和CONTAINER状态无关,停止状态也可以制作镜像
如果没有指定[REPOSITORY[:TAG]],REPOSITORY和TAG都为<none>
提交的时候标记TAG号:  生产当中常用，后期可以根据TAG标记创建不同版本的镜像以及创建不同版本的容器
```

**基于容器手动制作镜像步骤具体如下:**

- 下载一个系统的官方基础镜像，如:  CentOS 或 Ubuntu 
- 基于基础镜像启动一个容器,并进入到容器  
- 在容器里面做配置操作
  - 安装基础命令
  - 配置运行环境
  - 安装服务和配置服务
  - 放业务程序代码
- 提交为一个新镜像  docker commit
- 基于自己的的镜像创建容器并测试访问



#### 实战案例: 基于 busybox 制作 httpd 镜像

```bash
[root@ubuntu2204 ~]#docker run -it --name b1 busybox
Unable to find image 'busybox:latest' locally
latest: Pulling from library/busybox
9c0abc9c5bd3: Pull complete 
Digest: sha256:a5d0ce49aa801d475da48f8cb163c354ab95cab073cd3c138bd458fc8257fbf1
Status: Downloaded newer image for busybox:latest
/ # mkdir /data/html -p
/ # echo httpd website in busybox > /data/html/index.html
/ # httpd --help
BusyBox v1.37.0 (2024-09-26 21:31:42 UTC) multi-call binary.

Usage: httpd [-ifv[v]] [-c CONFFILE] [-p [IP:]PORT] [-u USER[:GRP]] [-r REALM] [-h HOME]
or httpd -d/-e/-m STRING

Listen for incoming HTTP requests

	-i		Inetd mode
	-f		Run in foreground
	-v[v]		Verbose
	-p [IP:]PORT	Bind to IP:PORT (default *:80)
	-u USER[:GRP]	Set uid/gid after binding to port
	-r REALM	Authentication Realm for Basic Authentication
	-h HOME		Home directory (default .)
	-c FILE		Configuration file (default {/etc,HOME}/httpd.conf)
	-m STRING	MD5 crypt STRING
	-e STRING	HTML encode STRING
	-d STRING	URL decode STRING
/ # exit

# 使用commit从编辑好的容器上，生成镜像
[root@ubuntu2204 ~]#docker commit -a "wang<root@wangxiaochun.com>" -c 'CMD /bin/httpd -fv -h /data/html' -c "EXPOSE 80" b1 httpd-busybox:v1.0
sha256:14fc46128d53349a2feb401cdf108c3584bc89f1b57260e9ebb8ce5f301f6572

# 查看
[root@ubuntu2204 ~]#docker images
REPOSITORY      TAG       IMAGE ID       CREATED         SIZE
httpd-busybox   v1.0      14fc46128d53   9 seconds ago   4.27MB

# 运行生成的镜像，进行测试
[root@ubuntu2204 ~]#docker run  -d -P --name httpd01 httpd-busybox:v1.0 
f7dbd52b05d67f5427f187845c5c06e5b9ebbb890742e20a444b58e9ca5ae147

[root@ubuntu2204 ~]#docker port httpd01 
80/tcp -> 0.0.0.0:32768
80/tcp -> [::]:32768

# 测试
[root@ubuntu2204 ~]#curl 127.1:32768
httpd website in busybox

# 查看进程
[root@ubuntu2204 ~]#docker exec -it httpd01 sh
/ # pstree -p
httpd(1)
/ # ps aux
PID   USER     TIME  COMMAND
    1 root      0:00 /bin/httpd -fv -h /data/html
    8 root      0:00 sh
   15 root      0:00 ps aux
```



#### 实战案例: 基于官方镜像生成的容器制作 tomcat 镜像

##### 下载官方的tomcat镜像并运行

```bash
[root@ubuntu2204 ~]#docker run -d -p 8080:8080 tomcat
Unable to find image 'tomcat:latest' locally
latest: Pulling from library/tomcat
de44b265507a: Pull complete 
dde9ea9bd15b: Pull complete 
8e785af5c591: Pull complete 
a612cb0b0ff4: Pull complete 
9a1e83616f3e: Pull complete 
fd0eb1230e44: Pull complete 
4f4fb700ef54: Pull complete 
11282d08385c: Pull complete 
Digest: sha256:c147f0e1141b7b389077d94aed5abb5108793bf1f763f3de3210043145f9637e
Status: Downloaded newer image for tomcat:latest
75a5bc77769bc7228aa9cc5136b1fd1b075db9aa873c9006b0d1c09dc4596084

# 测试
[root@ubuntu2204 ~]#curl -I 127.0.0.1:8080
HTTP/1.1 404 
Content-Type: text/html;charset=utf-8
Content-Language: en
Content-Length: 682
Date: Mon, 03 Feb 2025 06:10:37 GMT
```



##### **修改容器**

```bash
[root@ubuntu2204 ~]#docker ps
CONTAINER ID   IMAGE                COMMAND                   CREATED              STATUS              PORTS                                       NAMES
75a5bc77769b   tomcat               "catalina.sh run"         About a minute ago   Up About a minute   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   objective_goldwasser

# 进入tomcat的容器
[root@ubuntu2204 ~]#docker exec -it 75a5bc bash
root@75a5bc77769b:/usr/local/tomcat# ls
bin           conf             filtered-KEYS  LICENSE  native-jni-lib  README.md      RUNNING.txt  upstream-KEYS  webapps.dist
BUILDING.txt  CONTRIBUTING.md  lib            logs     NOTICE          RELEASE-NOTES  temp         webapps        work
root@75a5bc77769b:/usr/local/tomcat# cp -a webapps.dist/* webapps/
root@75a5bc77769b:/usr/local/tomcat# ls webapps/
docs  examples  host-manager  manager  ROOT
root@75a5bc77769b:/usr/local/tomcat# exit
exit

# 测试，返回200,成功
[root@ubuntu2204 ~]#curl -I 127.1:8080
HTTP/1.1 200 
Content-Type: text/html;charset=UTF-8
Date: Mon, 03 Feb 2025 06:13:21 GMT
```



##### 提交新镜像

```bash
[root@ubuntu2204 ~]#docker commit -m "add webapps app" -a "mystical" 75a5bc tomcat:9.0.37-v1
sha256:d11deed49556ed73a36d305e7a1edd2748f2c352024220a77a0f3ed6c7e92209
[root@ubuntu2204 ~]#docker images
REPOSITORY      TAG         IMAGE ID       CREATED          SIZE
tomcat          9.0.37-v1   d11deed49556   3 seconds ago    484MB

#查看
[root@ubuntu2204 ~]#docker history tomcat:9.0.37-v1 
IMAGE          CREATED          CREATED BY                                       SIZE      COMMENT
d11deed49556   46 seconds ago   catalina.sh run                                  5.37MB    add webapps app
9a15eef1e849   3 weeks ago      CMD ["catalina.sh" "run"]                        0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      ENTRYPOINT []                                    0B        buildkit.dockerfile.v0
<missing>      3 weeks ago      EXPOSE map[8080/tcp:{}]                          0B        buildkit.dockerfile.v0 #删除当前的容器
......

#删除当前的容器
[root@ubuntu2204 ~]#docker rm -f `docker ps -aq`
75a5bc77769b
```



##### 利用新镜像启动容器

```bash
[root@ubuntu2204 ~]#docker run  -d -p 8080:8080 --name tomcat tomcat:9.0.37-v1
b18c27f2e7621f94aea988f2d9dac6610c17a11fda1077c8b5af88601b6e3c6f

# 访问10.0.0.100:8080
```

![image-20250203143803373](D:\git_repository\cyber_security_learning\markdown_img\image-20250203143803373.png)



#### 实战案例: 基于Ubuntu的基础镜像利用 apt 安装手动制作 nginx 的镜像

##### 启动Ubuntu基础镜像并实现相关的配置

```bash
[root@ubuntu2204 ~]#docker run -it -p 80 --name nginx_ubuntu ubuntu bash
root@bd4982935c9c:/# sed -i 's/cn.archive.ubuntu.com/mirrors.ustc.edu.cn/' /etc/apt/sources.list
root@bd4982935c9c:/# apt update && apt install -y nginx

# 下载nginx，查看
root@bd4982935c9c:/# nginx -v
nginx version: nginx/1.24.0 (Ubuntu)
# 查看页面所在路径
root@bd4982935c9c:/# grep root /etc/nginx/sites-enabled/default 
	root /var/www/html;
	# deny access to .htaccess files, if Apache's document root
#	root /var/www/example.com;
root@bd4982935c9c:/#  echo Nginx Website in Docker >  /var/www/html/index.html
root@bd4982935c9c:/# cat /etc/os-release  
PRETTY_NAME="Ubuntu 24.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
root@bd4982935c9c:/# exit
```

##### 提交为镜像

```bash
[root@ubuntu2204 ~]#docker commit -a 'mystical' -m 'nginx-ubuntu:24.04' nginx_ubuntu nginx_ubuntu24.04:v1.24.0
sha256:9a761128ce8059e821abac7f5efe6d0d684948d30790f6a8869c679977b8dc4f
[root@ubuntu2204 ~]#docker images
REPOSITORY          TAG         IMAGE ID       CREATED          SIZE
nginx_ubuntu24.04   v1.24.0     9a761128ce80   6 seconds ago    132MB
```

##### 从制作的新镜像启动容器并测试访问

```bash
[root@ubuntu2204 ~]#docker run -d -p 80 --name nginx-web nginx_ubuntu24.04:v1.24.0 nginx -g 'daemon off;'
ba7793edf56740afd16d5ba458200d58ccdefabffade91f74904a7c767ff408a

# 查看
[root@ubuntu2204 ~]#docker ps
CONTAINER ID   IMAGE                       COMMAND                   CREATED         STATUS         PORTS                                       NAMES
ba7793edf567   nginx_ubuntu24.04:v1.24.0   "nginx -g 'daemon of…"   3 seconds ago   Up 2 seconds   0.0.0.0:32771->80/tcp, :::32771->80/tcp     nginx-web

# 访问容器测试
[root@ubuntu2204 ~]#curl 10.0.0.100:32771
Nginx Website in Docker
```



### 利用 DockerFile 文件执行 docker build 自动构建镜像

#### Dockerfile 使用详解

DockerFile 是一种被Docker程序解释执行的脚本，由一条条的命令组成的，每条命令对应linux下面的 一条命令，Docker程序将这些DockerFile指令再翻译成真正的linux命令，其有自己的书写方式和支持的命令，Docker程序读取DockerFile并根据指令生成Docker镜像，相比手动制作镜像的方式，DockerFile 更能直观的展示镜像是怎么产生的，有了DockerFile，当后期有额外的需求时，只要在之前的 DockerFile添加或者修改响应的命令即可重新生成新的Docker镜像，避免了重复手动制作镜像的麻烦,类似与shell脚本一样,可以方便高效的制作镜像

Docker守护程序 Dockerfile 逐一运行指令，如有必要，将每个指令的结果提交到新镜像，然后最终输出新镜像的ID。

Docker守护程序将自动清理之前发送的上下

请注意，每条指令都是独立运行的，并会导致创建新镜像，比如影响。

Docker将尽可能重用中间镜像层（缓存），以显著加速 docker build 命令的执行过程，这由 cache 控制台输出中的消息指示



#### Dockerfile文件的制作镜像的分层结构

![image-20250203164411302](D:\git_repository\cyber_security_learning\markdown_img\image-20250203164411302.png)

![image-20250203164458843](D:\git_repository\cyber_security_learning\markdown_img\image-20250203164458843.png)



#### 生产环境的最佳实践

在实际生产环境中，为了**便于管理、维护和扩展**，Dockerfile 及其相关资源通常按照 **业务类型、系统类型、服务角色** 进行分类，确保团队可以高效协作，方便 CI/CD 部署。

**生产环境一般按照以下方式进行组织**：

```bash
/data/dockerfiles/
├── base_images/            # 存放基础镜像 Dockerfile
│   ├── centos/             # 基于 CentOS 生成的基础镜像
│   │   ├── Dockerfile
│   │   ├── entrypoint.sh
│   │   └── sources.list
│   ├── ubuntu/             # 基于 Ubuntu 生成的基础镜像
│   │   ├── Dockerfile
│   │   ├── entrypoint.sh
│   │   └── sources.list
│   ├── alpine/             # 轻量级 Alpine
│   │   ├── Dockerfile
│   │   ├── entrypoint.sh
│   │   └── sources.list
│   └── debian/             # Debian
│       ├── Dockerfile
│       ├── entrypoint.sh
│       └── sources.list
│
├── app_images/             # 存放具体应用的 Dockerfile
│   ├── web/                # Web 相关服务
│   │   ├── nginx/
│   │   │   ├── Dockerfile
│   │   │   ├── nginx.conf
│   │   │   ├── default.conf
│   │   │   ├── certs/      # SSL 证书存放
│   │   │   │   ├── server.crt
│   │   │   │   ├── server.key
│   │   │   └── html/       # 静态资源
│   │   │       ├── index.html
│   │   │       ├── styles.css
│   │   │       └── script.js
│   │   ├── apache/
│   │   │   ├── Dockerfile
│   │   │   ├── httpd.conf
│   │   │   ├── modules.conf
│   │   │   └── logs/
│   │   ├── tomcat/
│   │   │   ├── Dockerfile
│   │   │   ├── tomcat-users.xml
│   │   │   ├── webapps/
│   │   │   └── logs/
│   │   ├── jdk/
│   │   │   ├── Dockerfile
│   │   │   ├── java.policy
│   │   │   └── jvm.options
│   │   ├── nodejs/
│   │   │   ├── Dockerfile
│   │   │   ├── package.json
│   │   │   ├── index.js
│   │   │   └── node_modules/
│   │   ├── php/
│   │   │   ├── Dockerfile
│   │   │   ├── php.ini
│   │   │   ├── www.conf
│   │   │   └── fpm.conf
│   │   ├── python/
│   │   │   ├── Dockerfile
│   │   │   ├── requirements.txt
│   │   │   ├── app.py
│   │   │   └── wsgi.py
│
├── db_images/              # 数据库相关镜像
│   ├── mysql/
│   │   ├── Dockerfile
│   │   ├── my.cnf
│   │   ├── init.sql
│   │   ├── data/
│   │   ├── backup/
│   │   └── logs/
│   ├── redis/
│   │   ├── Dockerfile
│   │   ├── redis.conf
│   │   ├── data/
│   │   ├── backup/
│   │   ├── logs/
│   │   └── redis_init.sh
│   ├── postgres/
│   │   ├── Dockerfile
│   │   ├── postgresql.conf
│   │   ├── pg_hba.conf
│   │   ├── init.sql
│   │   ├── data/
│   │   ├── backup/
│   │   ├── logs/
│
└── tools/                   # 其他工具相关
    ├── logstash/
    ├── filebeat/
    ├── elasticsearch/
    ├── kafka/
```



##### 按照功能划分目录

- `base_images/` 存放基础镜像，避免重复构建。
- `app_images/` 存放应用，如 `nginx`, `tomcat`, `nodejs`。
- `db_images/` 存放数据库，如 `mysql`, `redis`。
- `tools/` 存放监控、日志工具，如 `logstash`, `filebeat`。



##### Dockerfile 结构清晰

- **基础镜像**
- **复制配置**
- **复制静态资源**
- **暴露端口**
- **启动命令**



##### 所有配置文件（如 `nginx.conf`）都单独存放

- **不写死在 Dockerfile 里**，而是使用 `COPY` 复制。



##### 使用 `.dockerignore`

`.dockerignore` 用于排除构建 Docker 镜像时不需要的文件和目录，优化构建速度，减少镜像体积，提高安全性。

`.dockerignore` 语法

`.dockerignore` 语法类似 `.gitignore`，支持：

| 语法       | 作用                                     |
| ---------- | ---------------------------------------- |
| `file`     | 忽略 `file` 文件                         |
| `dir/`     | 忽略 `dir` 目录（包含子目录）            |
| `*.log`    | 忽略所有 `.log` 结尾的文件               |
| `!file`    | **强制包含** `file`，即使上面已忽略      |
| `**/temp/` | 忽略所有 `temp` 目录，无论在哪个子目录中 |

示例：优化 `Python` Flask 应用

```bash
# 适用于： Python、Flask、Django 等项目。
[root@ubuntu2204 dockerfile]#vim .dockerignore
__pycache__/        # 排除 Python 编译缓存
*.pyc               # 排除 Python 生成的 .pyc 文件。
*.pyo
.env                # 排除环境变量文件，防止 .env 泄露
.vscode/            # 排除 IDE 配置。
.idea/              # 排除 IDE 配置。
logs/
```



##### 日志和数据存储持久化

`logs/` 目录绑定宿主机，避免日志丢失

```bash
docker run -d -v /data/logs/nginx:/var/log/nginx nginx
```





#### Dockerfile 文件格式

Dockerfile 是一个有特定语法格式的文本文件

dockerfile 官方说明:   https://docs.docker.com/engine/reference/builder

Dockerfile 文件说明

- 每一行以Dockerfile的指令开头，指令不区分大小写，但是惯例使用大写
- 使用 # 开始作为注释
- 每一行只支持一条指令，每条指令可以携带多个参数
- 指令按文件的顺序从上至下进行执行
- 每个指令的执行会生成一个新的镜像层，为了减少分层和镜像大小，尽可能将多条指令合并成一条 指令
- 制作镜像一般可能需要反复多次，每次执行dockfile都按顺序执行，从头开始，已经执行过的指令 已经缓存，不需要再执行，如果后续有一行新的指令没执行过，其往后的指令将会重新执行，所以 为加速镜像制作，将最常变化的内容放下dockerfile的文件的后面



#### Dockerfile 相关指令

| Instruction              | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| **ADD**                  | Add local or remote files and directories.                 |
| **ARG**                  | Use build-time variables.                                  |
| **CMD**                  | Specify default commands.                                  |
| **COPY**                 | Copy files and directories.                                |
| **ENTRYPOINT**           | Specify default executable.                                |
| **ENV**                  | Set environment variables.                                 |
| **EXPOSE**               | Describe which ports your application is listening on      |
| **FROM**                 | Create a new build stage from a base image.                |
| **HEALTHCHECK**          | Check a container's health on startup                      |
| **LABEL**                | Add metadata to an image.                                  |
| **MAINTAINER（已废弃）** | Specify the author of an image                             |
| **ONBUILD**              | Specify instructions for when the image is used in a build |
| **RUN**                  | Execute build commands.                                    |
| **SHELL**                | Specify the system call signal for exiting a container.    |
| **USER**                 | Set user and group ID.                                     |
| **VOLUME**               | Create volume mounts.                                      |
| **WORKDIR**              | Change working directory                                   |



##### FROM: 指定基础镜像

定制镜像，需要先有一个基础镜像，在这个基础镜像上进行定制。

**FROM** 就是指定基础镜像，此指令通常必需放在Dockerfile文件第一个非注释行。后续的指令都是运行 于此基准镜像所提供的运行环境

基础镜像可以是任何可用镜像文件，默认情况下，docker build会在docker主机上查找指定的镜像文 件，在其不存在时，则会从Docker Hub Registry上拉取所需的镜像文件.如果找不到指定的镜像文件， docker build会返回一个错误信息

**格式**

```bash
FROM [--platform=<platform>] <image> [AS <name>]
FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]

# 说明
--platform=<platform> 可选  # 指定目标 CPU 架构（如 linux/amd64 或 linux/arm64）。
image                      # 基础镜像名称（如 ubuntu、nginx）。
tag：可选，                 # 指定版本（如 :latest、:20.04）。
digest：可选                # 指定精确的 SHA256 哈希值，确保镜像的一致性。
AS <name>（可选）           # 用于多阶段构建，命名阶段。

# 推荐实践
开发环境：可以用 FROM ubuntu（默认 latest）。
生产环境：推荐用 FROM ubuntu:20.04 或 FROM ubuntu@sha256:xxx 确保版本一致。
跨架构支持：用 --platform=linux/arm64 指定架构。
```

```ABAP
使用 digest 可确保每次构建的镜像一致性，更适用于生产环境！
```



**说明: 关于scratch 镜像**

```bash
FROM scratch
参考链接:
https://hub.docker.com/_/scratch?tab=description
https://docs.docker.com/develop/develop-images/baseimages/
该镜像是一个空的镜像，可以用于构建busybox等超小镜像，可以说是真正的从零开始构建属于自己的镜像
该镜像在构建基础镜像（例如debian和busybox）或超最小镜像（仅包含一个二进制文件及其所需内容，例
如:hello-world）的上下文中最有用。
```



##### LABEL: 指定镜像元数据

可以指定镜像元数据，如:  镜像作者等

```bash
LABEL <key>=<value> <key>=<value> <key>=<value> ...
```

范例:

```bash
LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
LABEL version="1.0"
LABEL description="This text illustrates \
that label-values can span multiple lines."
```

一个镜像可以有多个label ,还可以写在一行中,即多标签写法,可以减少镜像的层数

多标签写法

```bash
#一行格式
LABEL multi.label1="value1" multi.label2="value2" other="value3"

#多行格式
LABEL multi.label1="value1" \
      multi.label2="value2" \
      other="value3"
```

docker inspect 命令可以查看LABEL

```bash
"Labels": {
 "com.example.vendor": "ACME Incorporated"
 "com.example.label-with-value": "foo",
 "version": "1.0",
 "description": "This text illustrates that label-values can span multiple lines.",
 "multi.label1": "value1",
 "multi.label2": "value2",
 "other": "value3"
},
```



##### MAINTAINER: 指定维护者信息(已废弃)

此指令已过时，用LABEL代替

```bash
MAINTAINER wangxiaochun <root@wangxiaochun.com>
#用LABEL代替
LABEL maintainer="wangxiaochun <root@wangxiaochun.com>"
```



##### RUN: 执行 shell 命令

**RUN** 指令用来在**构建镜像阶段**需要执行 FROM 指定镜像所支持的Shell命令。

通常各种基础镜像一般都支持丰富的shell命令

注意:  RUN 可以写多个，每一个RUN指令都会建立一个镜像层，所以尽可能合并成一条指令,比如将多个 shell命令通过 && 连接一起成为在一条指令

```ABAP
每个RUN都是独立运行的,和前一个RUN无关
```

格式

```bash
#shell 格式: 相当于 /bin/sh -c  <命令>  此种形式支持环境变量
RUN <命令> 

#如果想使用其它shell,可以用SHELL指令指定不同的shell
SHELL ["/bin/bash", "-c"]
RUN <命令> 

#exec 格式: 此种形式不支持环境变量,注意:是双引号,不能是单引号
RUN ["executable","param1","param2"...] 

#exec格式可以指定其它shell
RUN ["/bin/bash","-c","echo hello wang"]
```

**关于 shell 和 exec 形式**

- **Shell解释**
  - **Shell形式**：命令通过Shell解释，这意味着可以使用Shell特性，例如环境变量替换、管道和重定向。
  - **Exec形式**：命令直接执行，不经过Shell。因此，没有Shell特性支持。
- **可移植性和安全性**
  - **Shell形式**：由于依赖Shell解释，可能会受到Shell注入攻击或其他Shell相关的问题
  - **Exec形式**：更安全和可移植，因为命令直接执行，不依赖Shell。
- **性能**
  - **Shell形式**：需要额外启动一个Shell进程，可能略有性能开销
  - **Exec形式**：直接执行命令，通常更高效。
- **复杂命令**
  - **Shell形式**：适合编写复杂的命令或使用Shell特性的场景
  - **Exec形式**：适合简单的命令或不需要Shell功能的场景

范例

```bash
RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
RUN ["/bin/bash", "-c", "echo hello world"]
RUN yum -y install epel-release \
      && yum -y install nginx \
      && rm -rf /usr/share/nginx/html/*
      && echo "<h1> docker test nginx </h1>" > /usr/share/nginx/html/index.html
```

 多个前后RUN命令独立无关和shell命令不同

```bash
#world.txt并不存放在/app内
RUN cd /app
RUN echo "hello" > world.txt

#下面写法可以实现关联关系
RUN cd /app &&  echo "hello" > world.txt
```



##### ENV: 设置环境变量

ENV 可以定义环境变量和值，会被后续指令(如:ENV,ADD,COPY,RUN等)通过$KEY或${KEY}进行引用， 并在容器运行时保持

```bash
#变量赋值格式1
ENV <key> <value>   #此格式只能对一个key赋值,<key>之后的所有内容均会被视作其<value>的组成部分

#变量赋值格式2
ENV <key1>=<value1> <key2>=<value2> \  #此格式可以支持多个key赋值,定义多个变量建议使用,减少镜像层
    <key3>=<value3> ...
    
#如果<value>中包含空格，可以以反斜线\进行转义，也可通过对<value>加引号进行标识;另外，反斜线也可用于续行    
    
#只使用一次变量
RUN <key>=<value> <command>
 
#引用变量
RUN $key .....
```

如果运行容器时如果需要修改变量,可以执行下面通过基于 exec 机制实现

注意: 下面方式只影响容器运行时环境,而不影响构建镜像的过程,即只能覆盖docker run时的环境变量,而 不会影响docker build时环境变量的值

```bash
docker run -e|--env <key>=<value>
 
#说明
-e, --env list              # Set environment variables
    --env-file filename     # Read in a file of environment variables
```

示例:  两种格式功能相同
```bash
#格式1
 ENV myName="John Doe" myDog=Rex\ The\ Dog \
     myCat=fluffy
     
#格式2
ENV myName John Doe
ENV myDog Rex The  Dog
ENV myCat fluffy
```

示例

```dockerfile
[root@ubuntu2204 alpine]# cat dockerfile 
FROM alpine
LABEL AUTH=mystical
ENV NAME=mystical ID=1
RUN touch /$ID.txt
CMD echo $NAME > $ID.txt && tail -f /etc/hosts	
```

```bash
# 根据dockerfile，创建镜像
[root@ubuntu2204 alpine]#docker build -t alpine-test:vp0.1 .

# 使用新镜像创建容器，并指定环境变量
[root@ubuntu2204 alpine]#docker run -d  -e NAME=mage -e ID=12 alpine-test:vp0.1
a3b6fda28b05d603a3ad5a86b0234444e42c96bd85ee099349a169923f14b7bf

# 查看结果
[root@ubuntu2204 alpine]#docker exec -it laughing_bassi /bin/sh
/ # ls
1.txt   bin     etc     lib     mnt     proc    run     srv     tmp     var
12.txt  dev     home    media   opt     root    sbin    sys     usr
/ # cat 12.txt 
mage
/ # exit

# 上述结果可以看出，RUN执行在dockerfile -> images 这个阶段
# CMD执行在images -> containers 这个阶段
```



##### COPY: 复制文本

复制本地宿主机的到容器中的 

```BASH
COPY [--chown=<user>:<group>] <src>... <dest>
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"] #路径中有空白字符时,建议使用此格式
```

说明: 

- 可以是多个,可以使用通配符，通配符规则满足Go的filepath.Match 规则
  - filepath.Match 参考链接:  https://golang.org/pkg/path/filepath/#Match
- 必须是build上下文中的相对路径(为 Dockerfile 所在目录的相对路径），不能是其父目录中的文件
- 如果是目录，则其内部文件或子目录会被递归复制，但**目录自身不会被复制**
- 如果指定了多个, 或在中使用了通配符，则必须是一个目录，且**必须以 / 结尾**
- 可以是绝对路径或者是 WORKDIR 指定的相对路径
- 使用 COPY 指令，源文件的各种元数据都会保留。比如读、写、执行权限、文件变更时间等
- 如果事先不存在，它将会被自动创建，这包括其父目录路径,即**递归创建目录** 

示例

```dockerfile
COPY hom* /mydir/    
COPY hom?.txt /mydir/
```



##### ADD: 复制和解包文件

该命令可认为是增强版的COPY，不仅支持COPY，还**支持自动解压缩**。可以将复制指定的到容器中的

```dockerfile
ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>",... "<dest>"] 
```

说明

- `<src>`可以是Dockerfile所在目录的一个相对路径；也可是一个 URL；还可是一个 tar 文件（自动解压）
- `<dest>`可以是绝对路径或者是 WORKDIR 指定的相对路径
- 如果`<src>`是目录，只复制目录中的内容，而**非目录本身**
- 如果`<src>`是一个 URL ，下载后的文件权限自动设置为 600
- 如果`<src>`为URL且`<dest>`不以/结尾，则`<src>`指定的文件将被下载并直接被创建为`<dest>`,如果以 / 结尾，则文件名URL指定 的文件将被直接下载并保存为`<dest>`/`< filename>`
- 如果`<src>`是一个本地文件系统上的打包文件,如: gz, bz2 ,xz ，它将被解包 ，其行为类似于"tar -x"命令, 但是**通过URL获取到的tar文件将不会自动展开**
- 如果`<src>`有多个，或其间接或直接使用了通配符，则`<dest>`必须是一个以/结尾的目录路径;如果不以/结尾，则 其被视作一个普通文件，`<src>`的内容将被直接写入到 `<dest>`

范例

```dockerfile
ADD test relativeDir/            # adds "test" to `WORKDIR`/relativeDir/
ADD test /absoluteDir/           # adds "test" to /absoluteDir/
ADD --chown=55:mygroup files* /somedir/
ADD --chown=bin files* /somedir/
ADD --chown=1 files* /somedir/
ADD --chown=10:11 files* /somedir/
ADD ubuntu-xenial-core-cloudimg-amd64-root.tar.gz/
```



##### CMD: 容器启动命令

![image-20250204163700600](D:\git_repository\cyber_security_learning\markdown_img\image-20250204163700600.png)

一个容器中通常需要一个持续运行的业务主进程

CMD 用来指定启动容器时默认执行的一个初始命令

如果容器内没有一个持续运行的前台进程,容器会停止

- 如果docker run没有指定任何的执行命令或者dockerfile里面也没有ENTRYPOINT命令，那么开启 容器时就会使用执行CMD指定的默认的命令
- RUN 命令是在构建镜像时执行的命令
- 每个 Dockerfile 只能有一条 CMD 命令。如指定了多条，只有最后一条被执行
- 如果用户启动容器时用 docker run xxx 指定运行的命令，则会覆盖 CMD 指定的命令

格式

```dockerfile
#格式1:使用exec形式，推荐方式，第一个参数必须是命令的全路径,此种形式不支持环境变量,注意:是双引号,不能是单引号
CMD ["executable","param1","param2"] 

#格式2:shell形式,默认/bin/sh 中执行，提供给需要交互的应用；此种形式支持环境变量,相当于执行 
/bin/sh -c "command param1 param2"
CMD command param1 param2 

#指定不同的shell
SHELL ["/bin/bash", "-c"]
CMD command param1 param2

#格式3:使用exec形式,提供给 ENTRYPOINT 命令的充当其参数
CMD ["param1","param2"]
```

示例

```dockerfile
CMD ["nginx", "-g", "daemon off;"]
```

示例：使用CMD构建可传参脚本

```dockerfile
FROM nginx:1.26.1-alpine-3.20.0-2024-06-14
ENV SERVER=m58.wang,org
RUN mkdir /data/html -p
COPY start.sh /usr/local/bin/
CMD ["start.sh"]
```

```bash
vim start.sh
#!/bin/bash

mkdir -p /usr/local/nginx/conf/conf.d/
cat > /usr/local/nginx/conf/conf.d/wang.org.conf
server {
   listen 80;
   server_name ${SERVER};
   location / {
      root /data/html;
   }
}
EOF
echo $SERVER > /data/html/index.html
nginx -g "daemon off;"
```

```bash
# 启动容器
docker run -p 80:80 -e SERVER=m59 --rm --name nginx01 nginx-mx:1.27
```



##### ENTRYPOINT: 入口点

ENTRYPOINT和CMD的区别

- ENTRYPOINT后面的指令会追加，作为前面指令的参数
- CMD后面如果有后续输入，则会替换之前设置的指令
- 如果ENTRYPOINT和CMD共存，则CMD的值看作是ENTRYPOINT的参数

ENTRYPOINT和CMD之间配合使用

- ENTRYPOINT负责执行环境初始化
- CMD作为容器启动的默认进程

示例

```dockerfile
CMD ["nginx","-g","daemon off;"]
ENTRYPOINT ["start.sh"]
```

```bash
# vim start.sh
# 环境初始化后面追加CMD指令
# exec的功能是使用指令命令，替换当前进程
...
exec "$@"
```

```ABAP
可以通过docker run --entrypoint string 参数在运行时替换,注意string不要加空格

```



##### SHELL: 指定 Shell 类型

```dockerfile
SHELL ["executable", "parameters"]
```

该指令允许默认 shell 用于 shell 形式的要覆盖的命令。

Linux 上的默认 shell 是  `["/bin/sh", "-c"]`

该指令可以多次出现。每条指令都覆盖所有先前的指令，并影响所有后续指令。



##### ARG: 构建参数

`ARG`是唯一允许写在`FROM`之前的指令

ARG指令在build 阶段指定变量

和ENV不同的是，容器运行时并不存在ARG定义的环境变量

```dockerfile
ARG <name>[=<default value>]
```

如果和ENV同名，ENV覆盖ARG变量

```ABAP
可以用  docker build --build-arg <参数名>=<值> 来覆盖
```

示例

```dockerfile
#FROM指令支持ARG指令放在第一个FROM之前声明变量
ARG CODE_VERSION=latest
FROM base:${CODE_VERSION}
CMD  /code/run-app

FROM extras:${CODE_VERSION}
CMD  /code/run-extras

#在FROM之前声明的ARG在构建阶段之外，所以它不能在FROM之后的任何指令中使用。 要使用在第一个FROM之前声明的ARG的默认值，请在构建阶段内使用没有值的ARG指

ARG VERSION=latest
FROM busybox:$VERSION
ARG VERSION
RUN echo $VERSION > image_version
```



##### VOLUME: 匿名卷

在容器中创建一个可以从本地主机或其他容器挂载的挂载点，一般用来存放数据库和需要保持的数据 等，默认会将宿主机上的目录挂载至VOLUME 指令指定的容器目录。即使容器后期被删除，此宿主机的目录仍会保留，从而实现容器数据的持久保存。

宿主机目录为

```ABAP
/var/lib/docker/volumes/<volume_id>/_data
```

语法:

```html
VOLUME <容器内路径>
VOLUME ["<容器内路径1>", "<容器内路径2>"...]

注意: 
<容器内路径>如果在容器内不存在,在创建容器时会自动创建
<容器内路径>如果是存在的,同时目录内有内容,将会把此目录的内容复制到宿主机的实际目录
```

注意:

- Dockerfile中的VOLUME实现的是匿名数据卷,无法指定宿主机路径和容器目录的挂载关系
- 通过`docker rm -fv <容器ID> `可以删除容器的同时删除VOLUME指定的卷

示例： 在容器创建两个/data/ ,/data2的挂载点

```dockerfile
VOLUME [ "/data1","/data2" ] 
```



##### EXPOSE: 暴露端口

指定服务端的容器需要对外暴露(监听)的端口号，以实现容器与外部通信。

EXPOSE **仅仅是声明容器打算使用什么端口**而已,并不会真正暴露端口,即不会自动在宿主进行端口映射

因此，在启动容器时需要通过 -P 或 -p ，Docker 主机才会真正分配一个端口转发到指定暴露的端口才可使用

注意: 即使 Dockerfile 没有 EXPOSE 端口指令,也可以通过`docker run -p ` 临时暴露容器内程序真正监听的端口,所以EXPOSE 相当于指定默认的暴露端口,可以通过`docker run -P` 进行真正暴露

 格式

```dockerfile
EXPOSE <port>[/ <protocol>] [<port>[/ <protocol>] ..]
    
#说明
<protocol>用于指定传输层协议，可为tcp或udp二者之一，默认为TCP协议
```

示例

```dockerfile
EXPOSE 80 443
EXPOSE 11211/udp 11211/tcp
```



##### WORKDIR: 指定工作目录

为后续的 RUN、CMD、ENTRYPOINT 指令配置工作目录，当容器运行后，进入容器内WORKDIR指定的 默认目录

WORKDIR 指定工作目录（或称当前目录），以后各层的当前目录就被改为指定的目录，如该目录不存 在，WORKDIR 会自行创建

```ABAP
注意: 在RUN可以生效,在CMD、ENTRYPOINT可能会有问题
```

示例

```dockerfile
#两次RUN独立运行,不在同一个目录
RUN cd /app 
RUN echo "hello" > world.txt

#如果想实现相同目录
RUN cd /app && echo "hello" > world.txt

#可以使用WORKDIR
WORKDIR /app
RUN echo "hello" > world.tx 
```

可以使用多个 WORKDIR 指令，后续命令如果参数是相对路径，则会基于之前命令指定的路径。例如

```dockerfile
WORKDIR /a
WORKDIR b
WORKDIR c
RUN pwd
#则最终路径为 /a/b/c
```



##### ONBUILD: 子镜像引用父镜像的指令

可以用来配置当构建当前镜像的子镜像时，会自动触发执行的指令,但在当前镜像构建时,并不会执行,即 延迟到子镜像构建时才执行

```dockerfile
ONBUILD [INSTRUCTION]
```

例如，Dockerfile 使用如下的内容创建了镜像 image-A。

```dockerfile
...
ONBUILD ADD http://www.magedu.com/wp-content/uploads/2017/09/logo.png /data/
ONBUILD RUN /usr/local/bin/python-build --dir /app/src...
```

如果基于 image-A 创建新的镜像image-B时，新的Dockerfile中使用 FROM image-A指定基础镜像时， 会自动执行ONBUILD 指令内容，等价于在后面添加了两条指令。

```dockerfile
FROM image-A

#Automatically run the following
ADD http://www.magedu.com/wp-content/uploads/2017/09/logo.png /data
RUN /usr/local/bin/python-build --dir /app/src
```

说明

- 尽管任何指令都可注册成为触发器指令，但ONBUILD不能自我能套，且不会触发`FROM`和 `MAINTAINER`指令
- 使用 `ONBUILD` 指令的镜像，推荐在标签中注明，例如  `ruby:1.9-onbuild`



#####  USER: 指定当前用户

指定运行容器的用户名或 UID，在后续dockerfile中的 RUN ，CMD和ENTRYPOINT指令时使用此用户

当服务不需要管理员权限时，可以通过该命令指定运行用户

这个用户必须是事先建立好的，否则无法切换

如果没有指定 USER,**默认是 root 身份执行**

```html
USER <user>[:<group>] 
USER <UID>[:<GID>]
```

示例

```dockerfile
RUN groupadd -r mysql && useradd -r -g mysql mysql
USER mysql
```



##### HEALTHCHECK: 健康检查

检查容器的健康性

```bash
HEALTHCHECK [选项] CMD <命令> #设置检查容器健康状况的命令,如果命令执行失败,则返回1,即unhealthy
HEALTHCHECK NONE #如果基础镜像有健康检查指令，使用这行可以屏蔽掉其健康检查指令

HEALTHCHECK 支持下列选项: 
--interval=<间隔>             #两次健康检查的间隔，默认为 30 秒
--timeout=<时长>              #健康检查命令运行超时时间，如果超过这个时间，本次健康检查就被视为失败，默认 30 秒
--retries=<次数>              #当连续失败指定次数后，则将容器状态视为 unhealthy，默认3次 
--start-period=<FDURATION>   #容器启动后多久进行健康性检查，default: 0s

#检查结果返回值:
0  #success    the container is healthy and ready for use
1  #unhealthy   the container is not working correctly
2  #reserved   do not use this exit code
```

示例

```dockerfile
FROM nginx
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
HEALTHCHECK --interval=5s --timeout=3s CMD curl -fs http://localhost/ 
```



#### 多阶段构建

多阶段构建可以帮助你在构建阶段使用大型的构建工具和依赖项,但是在最终阶段只包含运行时所需的内容。

利用多阶段构建,可以大大减小镜像的大小,但要**注意相关依赖文件都要复制到新构建中**才能正常运行容器

多阶段构建比较适用于静态编译的程序，比如：**Golang**

另外在Dockerfile文件中删除文件，也不会让镜像变小，也可以利用多阶段构建缩小镜像



##### 实战案例：编译一个Go语言的镜像

**创建一个GO语言程序**

```go
# cat hello.go
package main

import (
   "fmt"
   "time"
)

func main() {
   for {
      fmt.Println("hello,world")
      time.Sleep(time.Second)
   }
}
```

**基于传统方式构建Golang应用**

```dockerfile
# cat Dockerfile
FROM golang:1.18-alpine
COPY hello.go /
# WORKDIR /
RUN cd / && go build hello.go
CMD ["/hello"]
```

**多阶段构建1:GO语言程序**

```dockerfile
# cp Dockerfile Dockerfile-v1.0
# vim Dockerfile
FROM golang:1.18-alpine as builder
COPY hello.go /opt
WORKDIR /opt
RUN go build hello.go

FROM alpine:3.15.0
#FROM scratch
COPY --from=builder /opt/hello /hello
#COPY --from=0 /opt/hello /hello
CMD ["/hello"]
```



##### 多阶段构建2：C语言程序

```dockerfile
ARG VERSION=3.20.0
FROM alpine:$VERSION
LABEL maintainer="mystical<mysticalrecluse@gmail.com>"

ENV NGINX_VERSION=1.26.1
ENV NGINX_DIR=/apps/nginx

ADD nginx-$NGINX_VERSION.tar.gz /usr/local/src

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/' /etc/apk/repositories && \
    apk update && apk --no-cache add gcc make libgcc libc-dev libcurl lib-utils pcre-dev zlib-dev libnfs pcre pcre2 net-tools curl pstree wget libevent libevent-dev iproute2 openssl-dev && \
    cd /usr/local/src/nginx-$NGINX_VERSION && \
    ./configure --prefix=${NGINX_VERSION} --user=nginx --group=nginx --with-http_ssl_module --with-http_v2_module --with-http_realip_module --with-http_stub_status_module --with-http_gzip_static_module --with-pcre --with-stream --with-stream_ssl_module --with-stream_realip_module && \
    make && make install && \
    rm -rf /usr/local/src/nginx-$NGINX_VERSION

COPY nginx.conf ${NGINX_DIR}/conf/nginx.conf

FROM alpine:$VERSION
ENV NGINX_DIR=/apps/nginx
COPY --from=0 ${NGINX_DIR}/ ${NGINX_DIR}/
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc/edu.cn/' /etc/apk/repositories \
    && apk update && apk --no-cache add tzdate pcre pcre2 \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && addgroup -g 888 -S nginx \
    && adduser -u 888 -G nginx -D -S -s /sbin/nologin nginx \
    && chown -R nginx.nginx ${NGINX_DIR}/ \
    # 在容器化环境中，推荐的做法是将应用程序的日志输出到标准输出和标准错误。容器运行时（如 Docker）会捕获这些日志并将它们存储在宿主机上。这样，日志就可以被宿主机上的日志收集和处理系统统一管理。
    && ln -sf /dev/stdout ${NGINX_DIR}/logs/access.log \
    && ln -sr /dev/stderr ${NGINX_DIR}/logs/error.log
EXPOSE 80 443
CMD ["nginx","-g","daemon off;"]
```





## 容器数据管理

![image-20250204192226502](D:\git_repository\cyber_security_learning\markdown_img\image-20250204192226502.png)



Docker镜像由多个只读层叠加而成，启动容器时，Docker会加载只读镜像层并在镜像栈顶部添加一个读写层

如果运行中的容器修改了现有的一个已经存在的文件，那该文件将会从读写层下面的只读层复制到读写层，该文件的只读版本仍然存在，只是已经被读写层中该文件的副本所隐藏，此即“写时复制(COW copy  on write)"机制

如果将正在运行中的容器修改生成了新的数据，那么新产生的数据将会被复制到读写层，进行持久化保 存，这个读写层也就是容器的工作目录，也为写时复制(COW) 机制

COW机制节约空间,但会导致性低下,虽然关闭重启容器,数据不受影响,但会随着容器的删除,其对应的可写 层也会随之而删除,即数据也会丢失.如果容器需要持久保存数据,并不影响性能可以用**数据卷技术实现**



### 容器的数据管理介绍

Docker镜像是分层设计的，**镜像层是只读的**，通过镜像启动的**容器添加了一层可读写**的文件系统，用户 写入的数据都保存在这一层中。



#### Docker容器的分层

当 Docker 使用 `overlay2` 作为存储驱动时，每个容器的文件系统结构类似如下

```bash
/var/lib/docker/overlay2/<container-id>/
├── lowerdir   # 只读层（基础镜像）
├── upperdir   # 可写层（当前容器的变化）
├── workdir    # 临时目录（合并时的工作目录）
└── merged     # 容器实际看到的文件系统（挂载点）
```

查看

```bash
[root@ubuntu2204 alpine]#docker inspect nginx
......
"GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/1249b5e460970bc0669325f672f717926c587d2c90e5fb83acd0e8b2a7f2ac5a/diff:/var/lib/docker/overlay2/9656448c1b2636d76bd98557faad6c8caf5a0d1ad84f2e5bead8b6347fc7ad77/diff:/var/lib/docker/overlay2/0dde63244c35f47fdb37dc8d59c6675c71d522910ae5caa9539a622f2598b634/diff:/var/lib/docker/overlay2/5e09fb9bb9e90097695a35f40ae7ac5e30d97ef9d899f550d435b8cf6bf5aa74/diff:/var/lib/docker/overlay2/1c7db90446e2df6c7a062ed3519d0c42ac36d6ec04cd8d1eb1090a796c4ea76c/diff:/var/lib/docker/overlay2/7c5ef05f1f440ea899031a98ee13da160e10cf1446e6abc4c26d12b99b2ce59e/diff",
                "MergedDir": "/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/merged",
                "UpperDir": "/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/diff",
                "WorkDir": "/var/lib/docker/overlay2/e24c38f35989f4ad2a6680b0a7e14c149c050fb757e76d8b34a035198a173e13/work"
            },
            "Name": "overlay2"
        },
......

#删除容器后，所有容器数据目录都随之而删除
```



#### 容器数据持久保存方式

如果要将写入到容器的数据永久保存，则需要将容器中的数据保存到宿主机的指定目录

Docker 提供了多种方法将宿主机的文件系统挂载到容器内，包括以下几种主要方式：

**卷（Volume）**

- 这是 Docker 推荐的挂载方式。卷是完全由 Docker 管理的文件目录，可以在容器之间共享和重用。在创建卷时，Docker 创建了一个目录在宿主机上，然后将这个目录挂载到容器内。卷的主要优点是你可以使用 Docker CLI 或 Docker API 来备份、迁移或者恢复卷，而无需关心卷在宿主机上的具体位置。

**绑定挂载（Bind Mount）**

- 这种方式可以将宿主机上的任意文件或目录挂载到容器内。与卷不同，绑定挂载依赖于宿主机的文件系统结构。
- 因此，如果你在 Docker CLI 或 Docker API 中使用绑定挂载，你需要知道宿主机上的文件或目录的具体路径。
- 另外，由于绑定挂载可以访问宿主机上的任意文件和目录，使用这种方式可能会有一定的安全风险。

**tmpfs 挂载**

- tmpfs 挂载不与宿主机上的任何文件或目录相关联，而是将一个临时文件系统挂载到容器的某个目录下。这种方式的主要优点是它提供了一个高速且安全的挂载方式，因为 **tmpfs 挂载通常驻留在宿主机的内存**中，且在**容器停止后会被自动删除**。
- tmpfs 挂载是临时的，只存留在容器宿主机的内存中。当容器停止时，tmpfs 挂载文件路径将被删除，在那里写入的文件不会被持久化。



#### tmpfs 挂载

```bash
[root@ubuntu2204 ~]#docker run -d --tmpfs /data --name test wangxiaochun/pod-test:v0.1
[root@ubuntu2204 ~]#docker exec -it test sh
[root@931b40b1ae29 /]# df /data
Filesystem           1K-blocks      Used   Available Use% Mounted on 
tmpfs                4046088        0      4046088   0%   /data

#宿主机内存空间
[root@ubuntu2204 ~]#free -hh
               total        used        free      shared  buff/cache   available
内存：          1.9Gi       401Mi        82Mi       1.0Mi   1.4Gi       1.3Gi
交换：          2.0Gi        20Mi        2.0Gi
      
[root@931b40b1ae29 /]# dd if=/dev/zero of=/data/test.img bs=1M count=500
100+0 records in
100+0 records out
[root@931b40b1ae29 /]# ls  -lh /data/test.img
-rw-r--r--    1 root     root     500.0M Aug 28 05:52 /data/test.img

#宿主机内存消耗了500M
 [root@ubuntu2204 ~]#free -h
               total        used        free      shared  buff/cache   available
内存：          1.9Gi       385Mi        65Mi       490Mi   1.4Gi       860Mi

[root@931b40b1ae29 /]# exit

#停止容器重启动
[root@ubuntu2204 ~]#docker stop test
 test
 
#宿主机内存释放前面占用的500M
[root@ubuntu2204 ~]#free -hh
               total        used        free      shared  buff/cache   available
内存：          1.9Gi       377Mi       560Mi       0.0Ki  990Mi         1.3Gi
交换：          2.0Gi        21Mi       2.0Gi

[root@ubuntu2204 ~]#docker start test
test
      
#查看文件已经不存在
[root@ubuntu2204 ~]#docker exec -it test ls /data
[root@ubuntu2204 ~]#
```



#### 数据卷(data volume)

##### 数据卷特点和使用

数据卷实际上就是宿主机上的目录或者是文件，可以被直接mount到容器当中使用 

实际生成环境中，需要针对不同类型的服务、不同类型的数据存储要求做相应的规划，最终保证服务的可扩展性、稳定性以及数据的安全性

**数据卷使用场景**

- 数据库
- 日志输出
- 静态web页面
- 应用配置文件
- 多容器间目录或文件共享

**数据卷的特点**

- 数据卷是目录或者文件，并且可以在多个容器之间共同使用,实现容器之间共享和重用
- 对数据卷更改数据在所有容器里面会立即更新
- 数据卷的数据可以持久保存，即使删除使用使用该容器卷的容器也不影响。
- 在容器里面的写入数据不会影响到镜像本身,即数据卷的变化不会影响镜像的更新
- 依赖于宿主机目录，宿主机出问题，上面容器会受影响，当宿主机较多时，不方便统一管理
- 匿名和命名数据卷在容器启动时初始化，如果容器使用的镜像在挂载点包含了数据，会拷贝到新初始化的数据卷中

**数据卷分类**

- 启动容器时，可以指定使用数据卷实现容器数据的持久化,数据卷有三种
  - 指定宿主机目录或文件（**绑定挂载**）: 指定宿主机的具体路径和容器路径的挂载关系，此方式不会创建数据卷
  - **匿名卷**:  不指定数据名称,只指定容器内目录路径充当挂载点,docker自动指定宿主机的路径进行挂载，此方式会创建匿名数据卷,Dockerfile中VOLUME指定的卷即为此种
  - **命名卷**:  指定数据卷的名称和容器路径的挂载关系，此方式会创建命名数据卷



##### 数据卷使用方法

`docker run` 命令的以下格式可以实现数据卷

```bash
-v, --volume=[host-src:]container-dest[:<options>]

# options
ro          # 从容器内对此数据卷是只读，不写此项默认为可读可写
rw          # 从容器内对此数据卷可读可写,此为默认值
host-src    # 宿主机目录如果不存在,会自动创建
```

**方式1: 绑定挂载（Bind Mount）**

```bash
#指定宿主机目录或文件格式: 
-v <宿主机绝对路径的目录或文件>:<容器目录或文件>[:ro]  #将宿主机目录挂载容器目录，两个目录都可自动创建

#注意：如果初始容器中有旧数据，将被宿主机目录覆盖
#注意:如果挂载文件,必须指定文件的相对或绝对路径,否则会将文件名当成命名卷
```

**方式2: 匿名卷**

```bash
#匿名卷,只指定容器内路径,没有指定宿主机路径信息,宿主机自动生成/var/lib/docker/volumes/<卷ID>/_data目录,并挂载至容器指定路径
#注意：如果初始容器中有旧数据，将被复制到宿主机数据卷目录
-v <容器内路径>

#示例:
docker run --name nginx -v /etc/nginx nginx
```

**方式3: 命名卷**

```bash
#命名卷将固定的存放在/var/lib/docker/volumes/<卷名>/_data
#注意：如果初始容器中有旧数据，将被复制到宿主机数据卷目录

-v <卷名>:<容器目录路径>

#可以通过以下命令事先创建,如可没有事先创建卷名,docker run时也会自动创建卷
docker volume  create <卷名>

#示例:
docker volume  create vol1  #也可以事先不创建
docker run -d  -p 80:80 --name nginx01 -v vol1:/usr/share/nginx/html  nginx
```

**docker rm 的 -v 选项可以删除容器时，同时删除相关联的匿名卷**

```bash
-v, --volumes      # Remove the volumes associated with the container
```

**管理数据卷命令**

```bash
docker volume COMMAND

Commands:
  create      Create a volume
  inspect     Display detailed information on one or more volumes
  ls          List volumes
  prune       Remove all unused local volumes
  rm          Remove one or more volumes
```

**关于匿名数据卷和命名数据卷**

```ABAP
命名卷就是有名字的卷，使用 docker volume create <卷名> 形式创建并命名的卷；而匿名卷就是没名字的卷，一般是 docker run -v /data 这种不指定卷名的时候所产生，或者 Dockerfile 里面的定义直接使用的。

有名字的卷，在用过一次后，以后挂载容器的时候还可以使用，因为有名字可以指定。所以一般需要保存的数据使用命名卷保存。
而匿名卷则是随着容器建立而建立，随着容器消亡而淹没于卷列表中（对于 docker run 匿名卷不会被自动删除）。 因此匿名卷只存放无关紧要的临时数据，随着容器消亡，这些数据将失去存在的意义。

Dockerfile中指定VOLUME为匿名数据卷,其目的只是为了将某个路径确定为卷。

按照最佳实践的要求，不应该在容器存储层内进行数据写入操作，所有写入应该使用卷。如果定制镜像的时候，就可以确定某些目录会发生频繁大量的读写操作，那么为了避免在运行时由于用户疏忽而忘记指定卷，导致容器发生存储层写入的问题，就可以在 Dockerfile 中使用 VOLUME 来指定某些目录为匿名卷。这样即使用户忘记了指定卷，也不会产生不良的后果

这个设置可以在运行时覆盖。通过 docker run 的 -v 参数或者 docker-compose.yml 的 volumes指定。使用命名卷的好处是可以复用，其它容器可以通过这个命名数据卷的名字来指定挂载，共享其内容（不过要注意并发访问的竞争问题）。

比如，Dockerfile 中说 VOLUME /data，那么如果直接 docker run，其 /data 就会被挂载为匿名卷，向 /data 写入的操作不会写入到容器存储层，而是写入到了匿名卷中。但是如果运行时 docker run -v mydata:/data，这就覆盖了 /data 的挂载设置，要求将 /data 挂载到名为 mydata 的命名卷中。所以说 Dockerfile 中的 VOLUME 实际上是一层保险，确保镜像运行可以更好的遵循最佳实践，不向容器存储层内进行写入操作。

数据卷默认可能会保存于 /var/lib/docker/volumes，不过一般不需要、也不应该访问这个位置。
```





## 容器网络管理

### 浅谈容器网络

**这个被隔离的容器进程，该如何跟其他 Network Namespace 里的容器进程进行交互呢？**

为了理解这个问题，你其实可以把每一个容器看做一台主机，它们都有一套独立的“网络栈”。

如果你想要实现两台主机之间的通信，最直接的办法，就是把它们用一根网线连接起来；而如果你想要实现多台主机之间的通信，那就需要**用网线，把它们连接在一台交换机上**。

在 Linux 中，能够起到虚拟交换机作用的网络设备，是**网桥（Bridge）**。它是一个**工作在数据链路层（Data Link）的设备**，主要功能是**根据 MAC 地址学习来将数据包转发到网桥的不同端口（Port）上**。

而为了实现上述目的，Docker 项目会默认在宿主机上创建一个名叫 docker0 的网桥，凡是连接在 docker0 网桥上的容器，就可以通过它来进行通信。

可是，我们又该如何把这些容器“连接”到 docker0 网桥上呢？

这时候，我们就需要使用一种名叫**Veth Pair**的虚拟设备了。

**Veth Pair 设备**的特点是：它被创建出来后，总是以两张虚拟网卡（Veth Peer）的形式成对出现的。并且，**从其中一个“网卡”发出的数据包，可以直接出现在与它对应的另一张“网卡”上**，哪怕这两个“网卡”在不同的 Network Namespace 里。

这就使得 Veth Pair 常常被用作连接不同 Network Namespace 的“网线”。

```bash
# 拉取一个测试镜像
[root@mystical ~]# docker pull ubuntu

# 启动两个容器
[root@mystical ~]# docker run -d --name myubuntu ubuntu sleep 3600
[root@mystical ~]# docker run -d --name myubuntu2 ubuntu sleep 3600

# 查看IP
[root@mystical ~]# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:1b:11:2e brd ff:ff:ff:ff:ff:ff
    altname enp2s1
    altname ens33
    inet 10.0.0.150/24 brd 10.0.0.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe1b:112e/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:65:02:5c:d1 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:65ff:fe02:5cd1/64 scope link 
       valid_lft forever preferred_lft forever
5: vethebb1471@if4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether e6:f4:5f:1b:1c:82 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::e4f4:5fff:fe1b:1c82/64 scope link 
       valid_lft forever preferred_lft forever
7: veth753a3ed@if6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether 4a:0d:31:f2:1f:3c brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::480d:31ff:fef2:1f3c/64 scope link 
       valid_lft forever preferred_lft foreve
       
      
# 查看网桥
[root@mystical ~]# brctl show
bridge name	bridge id		STP enabled	interfaces
docker0		8000.024265025cd1	no		veth753a3ed
							            vethebb1471

# 查看容器内的网络
[root@mystical ~]# docker inspect myubuntu|grep -i pid
            "Pid": 3940,
            "PidMode": "",
            "PidsLimit": null,
            
[root@mystical ~]# nsenter -t 3940 -n ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
4: eth0@if5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
       
[root@mystical ~]# docker inspect myubuntu2|grep -i pid
            "Pid": 4030,
            "PidMode": "",
            "PidsLimit": null,
[root@mystical ~]# nsenter -t 4030 -n ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
6: eth0@if7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.3/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever

```



基于上述的`brctl show`可以看出，`veth753a3ed `和 `vethebb1471`都“插”在docker0网桥上

此时`myubuntu`和`myubuntu2`这两个容器进行通信，其中原理如下

- 当在`myubuntu`容器里访问`myubuntu2`容器的IP地址（比如：`ping 172.17.0.3`）的时候，这个目的IP地址会匹配到myubuntu容器里的第二条路由规则，可以看到，这条路由规则的**网关（Gateway）是 0.0.0.0**，这就意味着这是一条直连规则，即：凡是匹配到这条规则的 IP 包，应该经过本机的 eth0 网卡，通过二层网络直接发往目的主机。

  ```bash
  [root@mystical ~]# nsenter -t 4030 -n route -n
  Kernel IP routing table
  Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
  0.0.0.0         172.17.0.1      0.0.0.0         UG    0      0        0 eth0
  172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 eth0
  ```

  

- 而要通过二层网络到达 `myubuntu2` 容器，就需要有 `172.17.0.3` 这个 IP 地址对应的 MAC 地址。所以 `myubuntu` 容器的网络协议栈，就需要通过 eth0 网卡发送一个 ARP 广播，来通过 IP 地址查找对应的 MAC 地址



- 前面提到过，这个 eth0 网卡，是一个 Veth Pair，它的一端在这个 nginx-1 容器的 Network Namespace 里，而另一端则位于宿主机上（Host Namespace），并且被“插”在了宿主机的 docker0 网桥上。

  - 一旦一张虚拟网卡被“插”在网桥上，它就会变成该网桥的“从设备”。从设备会被“剥夺”调用网络协议栈处理数据包的资格，从而“降级”成为网桥上的一个端口。而这个端口唯一的作用，就是接收流入的数据包，然后把这些数据包的“生杀大权”（比如转发或者丢弃），全部交给对应的网桥。
  - 所以，在收到这些 ARP 请求之后，docker0 网桥就会扮演二层交换机的角色，把 ARP 广播转发到其他被“插”在 docker0 上的虚拟网卡上。这样，同样连接在 docker0 上的 nginx-2 容器的网络协议栈就会收到这个 ARP 请求，从而将 172.17.0.3 所对应的 MAC 地址回复给`myubuntu`容器

  

- 有了这个目的 MAC 地址，`myubuntu` 容器的 eth0 网卡就可以将数据包发出去。



- 而根据 Veth Pair 设备的原理，这个数据包会立刻出现在宿主机上的 `vethebb1471` 虚拟网卡上。不过，此时这个 `vethebb1471` 网卡的网络协议栈的资格已经被“剥夺”，所以这个数据包就直接流入到了 docker0 网桥里。



- docker0 处理转发的过程，则继续扮演二层交换机的角色。此时，docker0 网桥根据数据包的目的 MAC 地址（也就是 `ubuntu2` 容器的 MAC 地址），在它的 CAM 表（即交换机通过 MAC 地址学习维护的端口和 MAC 地址的对应表）里查到对应的端口（Port）为：vethb4963f3，然后把数据包发往这个端口。

  ```bash
  [root@mystical ~]# brctl showmacs docker0
  port no	mac addr		is local?	ageing timer
    2	4a:0d:31:f2:1f:3c	yes		   0.00
    2	4a:0d:31:f2:1f:3c	yes		   0.00
    1	e6:f4:5f:1b:1c:82	yes		   0.00
    1	e6:f4:5f:1b:1c:82	yes		   0.00
    
  [root@mystical ~]# ip a
  ......
  5: vethebb1471@if4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default 
      link/ether e6:f4:5f:1b:1c:82 brd ff:ff:ff:ff:ff:ff link-netnsid 0
      inet6 fe80::e4f4:5fff:fe1b:1c82/64 scope link 
         valid_lft forever preferred_lft forever
  7: veth753a3ed@if6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default 
      link/ether 4a:0d:31:f2:1f:3c brd ff:ff:ff:ff:ff:ff link-netnsid 1
      inet6 fe80::480d:31ff:fef2:1f3c/64 scope link 
         valid_lft forever preferred_lft forever
  ```



- 而这个端口，正是 `ubuntu2` 容器“插”在 docker0 网桥上的另一块虚拟网卡，当然，它也是一个 Veth Pair 设备。这样，数据包就进入到了 `ubuntu2` 容器的 Network Namespace 里。



![image-20250116152542027](D:\git_repository\cyber_security_learning\markdown_img\image-20250116152542027.png)



```ABAP
在实际的数据传递时，上述数据的传递过程在网络协议栈的不同层次，都有 Linux 内核 Netfilter 参与其中
以通过打开 iptables 的 TRACE 功能查看到数据包的传输过程
# 在宿主机上执行
$ iptables -t raw -A OUTPUT -p icmp -j TRACE
$ iptables -t raw -A PREROUTING -p icmp -j TRACE

less /var/log/syslog
Jan 16 06:42:16 mystical kernel: [ 7105.605200] eth0: renamed from vetha24fcee
Jan 16 06:42:16 mystical systemd-networkd[838]: veth753a3ed: Gained carrier
Jan 16 06:42:16 mystical kernel: [ 7105.615808] IPv6: ADDRCONF(NETDEV_CHANGE): veth753a3ed: link becomes ready
Jan 16 06:42:16 mystical kernel: [ 7105.615858] docker0: port 2(veth753a3ed) entered blocking state
Jan 16 06:42:16 mystical kernel: [ 7105.615860] docker0: port 2(veth753a3ed) entered forwarding state
```



当容器试图连接到另外一个宿主机时，比如：`ping 10.0.0.151`，最终到达 10.168.0.3 对应的宿主机上。当然，这个过程的实现要求这两台宿主机本身是连通的。这个过程的示意图，如下所示：

![image-20250116153904758](D:\git_repository\cyber_security_learning\markdown_img\image-20250116153904758.png)

这里当容器内的数据包从容器的 `eth0` 到达宿主机的 `eth0` 时，**Linux 内核在某种程度上扮演了路由器的角色**，处理了数据包的转发。



**容器到宿主机的数据转发过程**

- **容器内的 `eth0` 发送数据包：**

  - 数据包从容器内的应用程序发出，经过容器的虚拟网络接口（`eth0`）。
  - `eth0` 是容器内部的虚拟网络设备，通常连接到宿主机的虚拟接口（如 `vethXXX`）。

- **通过虚拟接口进入宿主机：**

  - 容器的 `eth0` 另一端是宿主机上的 `vethXXX` 设备。
  - `vethXXX` 是一个虚拟以太网设备，与容器的 `eth0` 成对，数据包通过它进入宿主机网络栈

- **宿主机的 `docker0` 网桥处理数据包：**

  - 宿主机的 `docker0` 是一个 Linux 桥接设备，扮演了二层交换机的角色。
  - 如果目标是同一宿主机内的其他容器，`docker0` 会根据 MAC 地址表（CAM 表）将数据包转发到对应的容器。

- **从 `docker0` 网桥到宿主机的 `eth0`（外部网络）：**

  - 如果数据包的目标地址不是容器，而是外部网络（如互联网），则会通过 NAT 和路由规则转发到宿主机的 `eth0` 接口。

- **宿主机执行 NAT 转换：**

  - 在默认的 Docker 设置中，宿主机为容器提供 NAT 转换，将容器的源地址（如 `172.17.x.x`）转换为宿主机的 IP 地址。
  - 这是通过 `iptables` 的 `POSTROUTING` 链实现的。

  ```bash
  [root@mystical ~]# iptables -t nat -vnL
  Chain POSTROUTING (policy ACCEPT 0 packets, 0 bytes)
   pkts bytes target     prot opt in     out     source               destination         
      3   252 MASQUERADE  all  --  *      !docker0  172.17.0.0/16        0.0.0.0/0 
      
  # MASQUERADE 是一种特殊的 NAT 操作，会修改匹配数据包的源地址，使其看起来像是从宿主机的出口 IP 地址发出。
  # out --> !docker0 : !docker0 表示数据包的出口接口不是 docker0，即不处理通过 docker0 网桥发送的数据包。
  # source (源地址)：172.17.0.0/16 表示匹配容器子网（docker0 默认创建的子网）。
  # destination (目标地址)：0.0.0.0/0 表示匹配所有目标地址（发送到任意外部网络）
  ```

- **隔离与转发：**

  - 内核中的网桥（如 `docker0`）和虚拟以太网设备负责在容器和宿主机之间转发数据包，同时维护隔离。

  ```ABAP
  当容器访问外部（或另一个宿主机）时，数据包不需要在 docker0 网桥上处理。
  容器直接通过宿主机的出口网卡发出。
  ```

  - 在宿主机查看追踪表，看SNAT信息

  ```bash
  root@mystical ~]# nsenter -t 5234 -n curl 10.0.0.151
  hello
  [root@mystical ~]# conntrack -L
  tcp      6 113 TIME_WAIT src=172.17.0.3 dst=10.0.0.151 sport=51906 dport=80 src=10.0.0.151 dst=10.0.0.150 sport=80 dport=51906 [ASSURED] mark=0 use=1
  tcp      6 96 TIME_WAIT src=172.17.0.3 dst=10.0.0.151 sport=42030 dport=80 src=10.0.0.151 dst=10.0.0.150 sport=80 dport=42030 [ASSURED] mark=0 use=1
  ```

  

### 容器网络通信

#### 容器间通信

##### 同一个宿主机的不同容器可相互通信

默认情况下

- 同一个宿主机的不同容器之间可以相互通信

```bash
dockerd --icc Enable inter-container communication (default true)
--icc=false  #此配置可以禁止同一个宿主机的容器之间通
```

- 不同宿主机之间的容器IP地址重复，默认不能相互通信

范例:  同一个宿主机的容器之间访问

```bash
# 查看当前容器
[root@ubuntu2204 alpine]#docker ps
CONTAINER ID   IMAGE               COMMAND                   CREATED         STATUS         PORTS                               NAMES
05376bf09814   nginx               "/docker-entrypoint.…"   5 seconds ago   Up 4 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   mynginx
a3b6fda28b05   alpine-test:vp0.1   "/bin/sh -c 'echo $N…"   13 hours ago    Up 13 hours                                        laughing_bassi

# 查看容器的ip
root@ubuntu2204 alpine]#docker inspect mynginx|grep -i pid
            "Pid": 5063,
            "PidMode": "",
            "PidsLimit": null,
[root@ubuntu2204 alpine]#nsenter -t 5063 -n ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
38: eth0@if39: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.3/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
       
[root@ubuntu2204 alpine]#docker exec laughing_bassi ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
36: eth0@if37: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever

# 两容器相互通信
[root@ubuntu2204 alpine]#docker exec laughing_bassi ping 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.347 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.206 ms
```



##### 禁止同一个宿主机的不同容器间通信

范例: 同一个宿主机不同容器间禁止通信

```bash
#dockerd 的 --icc=false 选项可以禁止同一个宿主机的不同容器间通信
[root@ubuntu1804 ~]#vim /lib/systemd/system/docker.service
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --icc=false
[root@ubuntu1804 ~]#systemctl daemon-reload
[root@ubuntu1804 ~]#systemctl restart docker

#创建两个容器,测试无法通信
#添加--icc选项，本质上就是修改iptables规则 -A FORWARD -i docker0 -o docker0 -j ACCEPT修改为DROP
[root@ubuntu2204 ~]#iptables -S > icc.txt
[root@ubuntu2204 ~]#diff icc.txt no_icc.txt 
13c13
< -A FORWARD -i docker0 -o docker0 -j DROP--
> -A FORWARD -i docker0 -o docker0 -j ACCEPT
```



#### 修改默认docker0网桥的网络配置

默认docker后会自动生成一个docker0的网桥,使用的IP是172.17.0.1/16,可能和宿主机的网段发生冲突, 可以将其修改为其它网段的地址,避免冲突

范例: 将docker0的IP修改为指定IP

```bash
#方法1
[root@ubuntu1804 ~]#vim /etc/docker/daemon.json 
[root@ubuntu1804 ~]#cat /etc/docker/daemon.json
{
 "bip": "192.168.100.1/24",
 "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"]
}

# 方法2
[root@ubuntu1804 ~]#vim /lib/systemd/system/docker.service
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --bip=192.168.100.1/24 
[root@ubuntu1804 ~]#systemctl daemon-reload 
[root@ubuntu1804 ~]#systemctl restart docker.service

#注意两种方法不可混用,否则将无法启动docker服务
```



#### 修改默认网络设置使用自定义网桥

新建容器默认使用docker0的网络配置,可以修改默认指向自定义的网桥网络

范例:  用自定义的网桥代替默认的docker0

```bash
[root@ubuntu2204 alpine]#ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:50:56:22:42:a6 brd ff:ff:ff:ff:ff:ff
    altname enp2s1
    altname ens33
    inet 10.0.0.100/24 brd 10.0.0.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:fe22:42a6/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:6f:a2:16:cf brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:6fff:fea2:16cf/64 scope link 
       valid_lft forever preferred_lft forever

[root@ubuntu2204 alpine]#apt -y install bridge-utils
[root@ubuntu2204 alpine]#brctl addbr br0

#给网桥添加IP，用于给容器分配置IP，如果不指定IP，会自动向后续网段，默认是172.18.0.0/16
[root@ubuntu2204 alpine]#ip a a 192.168.100.1/24 dev br0
[root@ubuntu2204 alpine]#brctl show
bridge name	bridge id		STP enabled	interfaces
br0		8000.0a2400beff3d	no		
docker0		8000.02426fa216cf	no		vethac3c076
							            vethd7a2ac6
							        
[root@ubuntu2204 alpine]#ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:50:56:22:42:a6 brd ff:ff:ff:ff:ff:ff
    altname enp2s1
    altname ens33
    inet 10.0.0.100/24 brd 10.0.0.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:fe22:42a6/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:6f:a2:16:cf brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:6fff:fea2:16cf/64 scope link 
       valid_lft forever preferred_lft forever
40: br0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 0a:24:00:be:ff:3d brd ff:ff:ff:ff:ff:ff
    inet 192.168.100.1/24 scope global br0
       valid_lft forever preferred_lft forever

[root@ubuntu2204 alpine]#vim /lib/systemd/system/docker.service 
ExecStart=/usr/local/bin/dockerd -H unix://var/run/docker.sock -b br0

[root@ubuntu2204 alpine]#systemctl daemon-reload 
[root@ubuntu2204 alpine]#systemctl restart docker
[root@ubuntu2204 alpine]#ps -ef |grep dockerd
root        5693       1  0 23:50 ?        00:00:00 /usr/local/bin/dockerd -H unix://var/run/docker.sock -b br0

# 启动容器，查看新容器的ip
[root@ubuntu2204 alpine]#docker run -d --name=mynginx2 nginx
c03848a8d6b01a655268a1d7224e26a74049c606a1624c08ad8ee75024c6244d
[root@ubuntu2204 alpine]#docker inspect mynginx2 |grep -i pid
            "Pid": 5914,
            "PidMode": "",
            "PidsLimit": null,
[root@ubuntu2204 alpine]#nsenter -t 5914 -n ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
41: eth0@if42: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:c0:a8:64:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.100.2/24 brd 192.168.100.255 scope global eth0
       valid_lft forever preferred_lft forever

```



### 容器名称互联

新建容器时，docker会自动分配容器名称，容器ID和IP地址，导致容器名称，容器ID和IP都不固定，那 么如何区分不同的容器，实现和确定目标容器的通信呢？解决方案是**给容器起个固定的名称**，容器之间通过固定名称实现确定目标的通信

有两种固定名称: 

- 容器名称
- 容器名称的别名

注意:  两种方式都最少需要两个容器才能实现



#### 通过容器名称互联

##### 容器名称介绍

即在同一个宿主机上的容器之间可以通过自定义的容器名称相互访问，比如:  一个业务前端静态页面是使用nginx，动态页面使用的是tomcat，另外还需要负载均衡调度器，如:  haproxy 对请求调度至nginx 和tomcat的容器，由于容器在启动的时候其内部IP地址是DHCP 随机分配的，而给容器起个固定的名 称，则是相对比较固定的，因此比较适用于此场景

**注意: 如果被引用的容器地址变化,必须重启当前容器才能生效**



##### 容器名称实现

`docker run` 创建容器，可使用`--link`选项实现容器名称的引用，其本质就是在容器内的`/etc/hosts`中添加`--link`后指定的容器的IP和主机名的对应关系，从而实现名称解析

```bash
--link list                                      #Add link to another container 

格式:  
docker run --name <容器名称>                      #先创建指定名称的容器                  
docker run --link <目标通信的容器ID或容器名称>       #再创建容器时引用上面容器的名称   
```

```bash
[root@ubuntu2204 ~]#docker run -d --name myalpine1 alpine tail -f /etc/hosts
ba9112e5d111d9d7a6d42e147e03247f5606ef44afffd49a388af85ac2150e96

[root@ubuntu2204 ~]#docker ps
CONTAINER ID   IMAGE     COMMAND                CREATED         STATUS         PORTS     NAMES
ba9112e5d111   alpine    "tail -f /etc/hosts"   6 seconds ago   Up 4 seconds             myalpine1

[root@ubuntu2204 ~]#docker exec myalpine1 cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.2	ba9112e5d111

[root@ubuntu2204 ~]#docker run -d --link myalpine1 --name myalpine2 alpine tail -f /etc/hosts
cbd192e95d68ac5aea14c5ae3a0c4d6d8cf9aca98588133583efd9db47bc1709

[root@ubuntu2204 ~]#docker exec myalpine2 cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.2	myalpine1 ba9112e5d111       # 本质是在hosts添加了一条解析
172.17.0.3	cbd192e95d68
[root@ubuntu2204 ~]#docker exec myalpine2 ping myalpine1
PING myalpine1 (172.17.0.2): 56 data bytes
64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.310 ms
64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.209 ms
```

```ABAP
注意：--link 指定容器名后，如果容器后期重启，可能会由于ip更改导致报错，示例如下
```

```bash
# 删除之前的myalpine1
[root@ubuntu2204 ~]#docker rm -f myalpine1
myalpine1

# 创建一个test容器，目的是占住之前myalpine1的ip，使新创建的myalpine1的ip发生变化
[root@ubuntu2204 ~]#docker run -d --name test1 alpine tail -f /etc/hosts
8f451cf032df9180e6d42cee7f999b09f6e462c448bff3ea6142498fac43f657

[root@ubuntu2204 ~]#docker run -d --name myalpine1 alpine tail -f /etc/hosts
218caa62e2f89e4febc9a4e932b6f05d14ca3fadf1ceccaa498b7fe51de9bb33

# 查看新创建的myalpine1的ip
root@ubuntu2204 ~]#docker exec myalpine1 ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
10: eth0@if11: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:ac:11:00:04 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.4/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever

# 然后查看原myalpine2则会发现报错
[root@ubuntu2204 ~]#docker exec myalpine2 cat /etc/hosts
Error response from daemon: Cannot link to a non running container: /myalpine1 AS /myalpine2/myalpine1

# 进入其名称空间查看hosts文件
[root@ubuntu2204 ~]#docker inspect myalpine2 | grep -i pid
            "Pid": 1758,
            "PidMode": "",
            "PidsLimit": null,
[root@ubuntu2204 ~]#nsenter -t 1758 -m cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.2	myalpine1 ba9112e5d111
172.17.0.3	cbd192e95d68

# 原纪录并未动态变化，导致域名解析不匹配，所以发生报错
```



#### 通过自定义容器别名互联

##### 容器别名介绍

自定义的容器名称可能后期会发生变化，那么一旦名称发生变化，容器内程序之间也必须要随之发生变化，比如:程序通过固定的容器名称进行服务调用，但是容器名称发生变化之后再使用之前的名称肯定是无法成功调用，每次都进行更改的话又比较麻烦，因此可以使用自定义别名的方式解决，即容器名称可以随意更改，只要不更改别名即可



##### 容器别名实现

命令格式

```bash
docker run --name <容器名称>                                                       
#先创建指定名称的容器
docker run --name <容器名称> --link <目标容器名称>:"<容器别名1>  <容器别名2> ..."       
#给上面创建的容器起别名,来创建新容器
```

作用

```ABAP
当配置文件写死的时候，不需要更改容器名，只需要在创建容器的时候指定该容器名的别名和配置文件中引用的名称一致即可
```

示例

```bash
[root@ubuntu2204 ~]# dokcer run -d -name mysql123 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=wordpress -e MYSQL_USER=wordpress -e MYSQL_PASSWORD=123456 mysql:8.0.29-oracle

# 由于配置文件写死，链接的mysql的host是mysql，但是上面的容器的name是mysql123,因此可以使用别名解决
[root@ubuntu2204 ~]# docker run -p 80:80 --name wordpress --link mysql123:mysql -e WORDPRESS_DB_HOST=mysql -e WORDPRESS_DB_NAME=wordpress -e WORDPRESS_DB_USER=wordpress -e WORDPRESS_DB_PASSWORD=123456 -d wordpress:php8.2-apache
```



### Docker 网络连接模式

#### 网络模式介绍

**Docker 的网络支持5种网络模式:** 

- **none**
- **host**
- **bridge**
- **container**
- **network-name**



查看默认的网络模式有三个

```bash	
[root@ubuntu2204 ~]#docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
d22f3b149636   bridge    bridge    local
70cb08699f16   host      host      local
233da050125d   none      null      local
```



####  网络模式指定

默认新建的容器使用Bridge模式，创建容器时，docker run 命令使用以下选项指定网络模式

```bash
docker run --network <mode>
docker run --net=<mode>

<mode>:  可是以下值
none
bridge
host
container:<容器名或容器ID>
<自定义网络名称>
```



#### Bridge网络模式

本模式是docker的默认模式，即不指定任何模式就是bridge模式，也是使用比较多的模式，此模式创建的容器会为每一个容器分配自己的网络 IP 等信息，并将容器连接到一个虚拟网桥与外界通信

可以和外部网络之间进行通信，通过**SNAT**访问外网，使用**DNAT**可以让容器被外部主机访问，所以此模式也称为NAT模式

此模式宿主机需要启动`ip_forward`功能

bridge网络模式特点

- 网络资源隔离:  不同宿主机的容器无法直接通信，各自使用独立网络
- 无需手动配置:  容器默认自动获取172.17.0.0/16的IP地址，此地址可以修改
- 可访问外网:  利用宿主机的物理网卡，SNAT连接外网
- 外部主机无法直接访问容器:  可以通过配置DNAT接受外网的访问(暴露端口的本质就是DNAT)
- 低性能较低:  因为可通过NAT，网络转换带来更的损耗
- 端口管理繁琐:  每个容器必须手动指定唯一的端口，容器产生端口冲容





#### Host 模式

如果指定host模式启动的容器，那么新创建的容器不会创建自己的虚拟网卡，而是直接使用宿主机的网卡和IP地址，因此在容器里面查看到的IP信息就是宿主机的信息，访问容器的时候直接使用宿主机IP+容器端口即可，不过容器内除网络以外的其它资源，如:  文件系统、系统进程等仍然和宿主机保持隔离

此模式由于直接使用宿主机的网络无需转换，网络性能最高，但是各容器内使用的端口不能相同，适用于运行容器端口比较固定的业务

Host 网络模式特点: 

- 使用参数 `--network host` 指定
- 共享宿主机网络
- 各容器网络无隔离
- 网络性能无损耗
- 网络故障排除相对简单
- 容易产生端口冲突
- 网络资源无法分别统计
- 不支持端口映射

示例

```bash
[root@ubuntu2204 ~]#docker run --network host --name myalpine1 -d alpine tail -f /etc/hosts
9e2e18708d7c8b060f36e008b1f491d40be22a4d4186ab43c8e2fc1f935740ff

# 和宿主机公用一个网络
[root@ubuntu2204 ~]#docker exec myalpine1 ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP qlen 1000
    link/ether 00:50:56:22:42:a6 brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.100/24 brd 10.0.0.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:fe22:42a6/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN 
    link/ether 02:42:e5:0f:48:0e brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:e5ff:fe0f:480e/64 scope link 
       valid_lft forever preferred_lft forever
```

```ABAP
注意：host模式下端口映射无法实现
```



#### None 模式

在使用 none 模式后，Docker 容器不会进行任何网络配置，没有网卡、没有IP也没有路由，因此默认无 法与外界通信，需要手动添加网卡配置IP等，所以极少使用

none 模式特点

- 使用参数 `--network none` 指定
- 默认无网络功能，无法和外部通信
- 无法实现端口映射
- 适用于测试环境

范例:  启动none模式的容器

```bash
[root@ubuntu2204 ~]#docker run --network none -d --name myalpine2 alpine tail -f /etc/hosts
58ce25d229297c9d35a2dfdda97b3ef2ddadb5f60729b27d660fa78147fcd6ed
[root@ubuntu2204 ~]#docker exec myalpine2 ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
```



#### Container 模式

使用此模式创建的容器**需指定和一个已经存在的容器共享一个网络**，而不是和宿主机共享网络，新创建的容器不会创建自己的网卡也不会配置自己的IP，而是和一个被指定的已经存在的容器共享IP和端口范 围，因此这个容器的端口不能和被指定容器的端口冲突，除了网络之外的文件系统、进程信息等仍然保持相互隔离，两个容器的进程可以通过lo网卡进行通信

Container 模式特点

- 使用参数 `–-network container`:名称 或 ID 指定
- 与宿主机网络空间隔离
- 空器间共享网络空间,直接使用对方的网络
- 第一个容器的网络可能是bridge，或none，或者host，而第二个容器模式依赖于第一个容器，它们共享网络
- 如果第一个容器停止，将导致无法创建第二个容器
- 第二个容器可以直接使用127.0.0.1访问第一个容器
- 适合频繁的容器间的网络通信
- 默认不支持端口映射，较少使用

范例： 通过容器模式实现 wordpress

```bash
#方法1
[root@ubuntu2004 ~]#docker run -d  -p 80:80 --name wordpress -v /data/wordpress:/var/www/html --restart=always  wordpress:php7.4-apache

[root@ubuntu2004 ~]#docker run --network container:wordpress -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=wordpress -e MYSQL_USER=wordpress -e MYSQL_PASSWORD=123456 --name mysql -d  -v /data/mysql:/var/lib/mysql --restart=always mysql:8.0.29-oracle

#方法2
#MySQL提前为wordpress暴露端口
[root@ubuntu2004 ~]#docker run -d  -p 80:80 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=wordpress -e MYSQL_USER=wordpress -e MYSQL_PASSWORD=123456 --name mysql  --restart=always mysql:8.0.29-oracle

[root@ubuntu2004 ~]#docker run -d  --network container:mysql  --name wordpress --restart=always  wordpress:php7.4-apache

#注意：数据库主机地址为127.0.0.1或wordpress容器的IP，不支持localhost
```



####  自定义网络模式

除了以上的网络模式，也可以自定义网络，使用自定义的网段地址，网关等信息

可以使用自定义网络模式,实现不同集群应用的独立网络管理,而互不影响,而且在网一个网络内,可以直接利用容器名相互访问，非常便利

**注意: 自定义网络内的容器可以直接通过容器名进行相互的访问,而无需使用 --link**



##### 自定义网络实现

```bash
[root@ubuntu1804 ~]#docker network  --help
Usage:  docker network COMMAND
Manage networks

Commands:
    connect     Connect a container to a network
    create      Create a network
    disconnect  Disconnect a container from a network
    inspect     Display detailed information on one or more networks
    ls          List networks
    prune       Remove all unused networks
    rm          Remove one or more networks
```

创建自定义网络: 

```bash
docker network create -d <mode> --subnet <CIDR> --gateway <网关> <自定义网络名称>

#注意mode不支持host和none,默认是bridge模式
-d <mode> 可省略，默认为bridg
```

查看自定义网络信息

```bash
docker network inspect <自定义网络名称或网络ID>
```

引用自定义网络

```bash
docker run --network  <自定义网络名称> <镜像名称>
docker run --net  <自定义网络名称> --ip <指定静态IP> <镜像名称>
#注意：静态IP只支持自定义网络模型

#指定自定义网络中的容器的别名
docker run --network  <自定义网络名称> --network-alias list  <镜像名称>
```

删除自定义网络

```bash
doccker network rm <自定义网络名称或网络ID>
```

示例

```bash
# 创建两个自定义网络
[root@ubuntu2204 ~]#docker network create --subnet 172.31.0.0/16 net1
a4e6f84b267cba0e0c138baa921841c1d724bb9e423cdcf87da87f6cdab1e36d

[root@ubuntu2204 ~]#docker network create --subnet 172.32.0.0/16 net2
5e34d958aed1d9a8f9b19f0d600e3f5dcdf10494acff91c24668f9a937785b76

# 两个自定义网络，各自创建一个容器
[root@ubuntu2204 ~]#docker run --network net1 -d --name myalpine alpine tail -f /etc/hosts
1c354d82d663fac1a1cc3c4132f9b4f43ad9194033729ef060a9f195b748d11e
[root@ubuntu2204 ~]#docker run --network net2 -d --name myalpine2 alpine tail -f /etc/hosts
18af7a7b9d593e921ac7cb1825c19e18def43aa78b53d4c2468c5cfbe99e0821

# 查看
[root@ubuntu2204 ~]#docker exec myalpine ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
23: eth0@if24: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:ac:1f:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.31.0.2/16 brd 172.31.255.255 scope global eth0
       valid_lft forever preferred_lft forever
[root@ubuntu2204 ~]#docker exec myalpine2 ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
25: eth0@if26: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:ac:20:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.32.0.2/16 brd 172.32.255.255 scope global eth0
       valid_lft forever preferred_lft forever
       
# 两个容器之间不通
[root@ubuntu2204 ~]#docker exec myalpine ping 172.32.0.2
PING 172.32.0.2 (172.32.0.2): 56 data bytes

# 在net1再创建一个容器
[root@ubuntu2204 ~]#docker run --network net1 -d --name myalpine3 alpine tail -f /etc/hosts
105b37d1da5c39ea9a625343c1727496613592a979afdc36a3823839a7a75ec2

# 通网络的容器可以直接使用容器名称进行通信，无需使用--link
[root@ubuntu2204 ~]#docker exec myalpine3 ping myalpine
PING myalpine (172.31.0.2): 56 data bytes
64 bytes from 172.31.0.2: seq=0 ttl=64 time=0.267 ms
64 bytes from 172.31.0.2: seq=1 ttl=64 time=0.343 ms
64 bytes from 172.31.0.2: seq=2 ttl=64 time=4.989 ms
```

```bash
# 不同自定义网络之间容器不通的本质原因是因为iptablesc策略
[root@ubuntu2204 ~]#iptables -vnL 
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain FORWARD (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
  189 15876 DOCKER-USER  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
  189 15876 DOCKER-ISOLATION-STAGE-1  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     all  --  *      br-5e34d958aed1  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
    0     0 DOCKER     all  --  *      br-5e34d958aed1  0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     all  --  br-5e34d958aed1 !br-5e34d958aed1  0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     all  --  br-5e34d958aed1 br-5e34d958aed1  0.0.0.0/0            0.0.0.0/0           
  107  8988 ACCEPT     all  --  *      br-a4e6f84b267c  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
    1    84 DOCKER     all  --  *      br-a4e6f84b267c  0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     all  --  br-a4e6f84b267c !br-a4e6f84b267c  0.0.0.0/0            0.0.0.0/0           
    1    84 ACCEPT     all  --  br-a4e6f84b267c br-a4e6f84b267c  0.0.0.0/0            0.0.0.0/0           
 6677  561K ACCEPT     all  --  *      docker0  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
    3   252 DOCKER     all  --  *      docker0  0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     all  --  docker0 !docker0  0.0.0.0/0            0.0.0.0/0           
    3   252 ACCEPT     all  --  docker0 docker0  0.0.0.0/0            0.0.0.0/0           

Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain DOCKER (3 references)
 pkts bytes target     prot opt in     out     source               destination         

Chain DOCKER-ISOLATION-STAGE-1 (1 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DOCKER-ISOLATION-STAGE-2  all  --  br-5e34d958aed1 !br-5e34d958aed1  0.0.0.0/0            0.0.0.0/0           
   81  6804 DOCKER-ISOLATION-STAGE-2  all  --  br-a4e6f84b267c !br-a4e6f84b267c  0.0.0.0/0            0.0.0.0/0           
    0     0 DOCKER-ISOLATION-STAGE-2  all  --  docker0 !docker0  0.0.0.0/0            0.0.0.0/0           
 6788  570K RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain DOCKER-ISOLATION-STAGE-2 (3 references)
 pkts bytes target     prot opt in     out     source               destination         
   81  6804 DROP       all  --  *      br-5e34d958aed1  0.0.0.0/0            0.0.0.0/0           
    0     0 DROP       all  --  *      br-a4e6f84b267c  0.0.0.0/0            0.0.0.0/0           
    0     0 DROP       all  --  *      docker0  0.0.0.0/0            0.0.0.0/0           
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain DOCKER-USER (1 references)
 pkts bytes target     prot opt in     out     source               destination         
 6869  577K RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0
```

更改`iptables`规则使不同网络之间的容器可以通信

```bash
[root@ubuntu2204 ~]#iptables -I DOCKER-ISOLATION-STAGE-2  -j ACCEPT
[root@ubuntu2204 ~]#docker exec myalpine ping 172.32.0.2
PING 172.32.0.2 (172.32.0.2): 56 data bytes
64 bytes from 172.32.0.2: seq=0 ttl=63 time=0.953 ms
64 bytes from 172.32.0.2: seq=1 ttl=63 time=0.144 ms
```





## Docker Compose单机编排

### Docker Compose 介绍

![image-20250205141018844](D:\git_repository\cyber_security_learning\markdown_img\image-20250205141018844.png)

当在宿主机启动较多的容器时候，如果都是手动操作会觉得比较麻烦而且容易出错，此时推荐使用  docker 单机编排工具 docker-compose

docker-compose 是 docker 容器的一种单机编排服务，docker-compose 是一个管理多个容器的工具，比如:  可以解决容器之间的依赖关系，就像启动一个nginx 前端服务的时候会调用后端的 tomcat， 那就得先启动tomcat，但是启动tomcat 容器还需要依赖数据库，那就还得先启动数据库，docker compose 可以用来解决这样的嵌套依赖关系，并且可以替代docker命令对容器进行创建、启动和停止等手工的操作

因此，如果说docker命令就像linux的命令，docker-compose.yml 文件就像shell脚本，可以自动的执行容器批量操作，从而实现自动化的容器管理，或者说docker命令相当于ansible命令，那么docker  compose文件，就相当于ansible-playbook的yaml文件

docker-compose 项目是Docker 官方的开源项目，负责实现对Docker 容器集群的快速编排，docker compose 将所管理的容器分为三层，分别是工程（project），服务（service）以及容器（container）

github地址:   https://github.com/docker/compose

官方地址:   https://docs.docker.com/compose/



### 安装和准备

#### 安装 Docker Compose

##### 方法1：通过 Compose plugin 形式安装

即通过docker 内置子命令实现, 此方式无需专门安装独立的 docker-compose 工具

注意：此方式需要配置官方仓库才支持，Ubuntu内置仓库没有此插件包

```bash
# Add Docker's official GPG key:
apt-get update
apt-get install ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

echo "GPG OVER"

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# 官方仓库配置好后，执行下面的指令
[root@ubuntu2204 ~]#apt install -y docker-compose-plugin

# 执行之后，查看docker
[root@ubuntu2204 ~]#docker
......
Management Commands:
  builder     Manage builds
  compose*    Docker Compose
  container   Manage containers
  context     Manage contexts
......
```



##### 方法2: 在线直接从包仓库安装

此方法安装的版本较旧，不推荐使用

```bash
#ubuntu安装,此为默认版本
[root@ubuntu2204 ~]#apt list  docker-compose
正在列表... 完成
docker-compose/jammy 1.29.2-1 all
[root@ubuntu1804 ~]#apt -y install docker-compose
[root@ubuntu1804 ~]#docker-compose --version
docker-compose version 1.17.1, build unknown

#CentOS7安装，依赖EPEL源
[root@centos7 ~]#yum -y install docker-compose
[root@centos7 ~]#docker-compose --version
docker-compose version 1.18.0, buil 8dd22a9 
```



##### 方法3: 离线安装，直接从github或国内镜像站下载安装对应版本

参看说明:   https://github.com/docker/compose/releases

此方法安装版本可方便指定，推荐方法，但网络下载较慢

```bash
[root@ubuntu1804 ~]#curl -L https://github.com/docker/compose/releases/download/1.25.3/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

#从国内镜像站下载
[root@ubuntu1804 ~]#curl -L https://get.daocloud.io/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

[root@ubuntu1804 ~]#chmod +x /usr/local/bin/docker-compose
[root@ubuntu1804 ~]#ldd /usr/local/bin/docker-compose
    不是动态可执行文件
```



##### 方法4: 在线通过 pip安装

python-pip 包将安装一个 pip 的命令，pip 命令是一个python 安装包的安装工具，其类似于ubuntu 的 apt 或者 redhat 的yum，但是pip 只安装 python 相关的安装包，可以在多种操作系统安装和使用pip

此方式当前安装的版本较新，为docker_compose-1.25.3，推荐使用

```bash
Ubuntu:   
# apt  update 
# apt  install -y  python-pip 

CentOS:   
# yum install epel-release 
# yum install -y python-pip 
# pip install --upgrade pip 
```

基于python3 安装 docker-compose

```bash
#配置加速
[root@ubuntu2004 ~]#mkdir ~/.pip
[root@ubuntu2004 ~]#cat > ~/.pip/pip.conf <<-EOF
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
EOF

[root@ubuntu2004 ~]#apt -y install python3-pip
[root@ubuntu2004 ~]#pip3 install --upgrade pip

[root@ubuntu2004 ~]#pip3 install docker-compose
[root@ubuntu2004 ~]#docker-compose --version
docker-compose version 1.27.4, build unknown

#基于python2安装docker-compose
[root@ubuntu1804 ~]#apt -y install python-pip
[root@ubuntu1804 ~]#pip install docker-compose
[root@ubuntu1804 ~]#docker-compose --version
```



### Compose 文件

docker-compose命令默认于当前⽬目录中搜索docker-compose.yaml配置文件，除了了version以外，该 ⽂ 文件主要由三个顶级参数组成：**services**、**networks**和**volumes**

- **serivces**：用于定义组成每个服务的容器的相关配置，相关配置项类似于传递给docker container create命令的相关参数；每个服务启动的容器实例可能不止⼀个，而每个容器依赖的镜像要么通过 二级指令image指定位置直接获取，要么由二级指令build指定的Dockerfile临时构建；另外，服务中可内嵌networks指令引用顶级指令networks中定义的网络，以及内嵌volumes引用顶级指令 volumes中定义的存储卷。
- **networks**：用于定义容器网络，相关配置项类似于传递给docker network create命令的相关参数；
- **volumes**：用于定义容器器存储卷，相关配置项类似于传递给docker volume create命令的相关参数；



#### Services的常用指令

##### build

用于定义构建镜像的相关配置，它自身可以直接以上下文路径为参数，例如“build ./dir”即为于当前目录 下的dir子目录中搜索Dockerfile配置文件。不过，也可以使用二级参数context来完成此类功能。它常用的二级参数如下：

- **context**：包含Dockerfile的目录的路路径，或者是git仓库的url；相对路径通常意味着以docker compose.yaml文件所在的目录为起始目录

```yaml
# context 指定构建镜像的上下文路径，即 Docker 构建的工作目录
version: '3.8'
services:
  app:
    build:
      context: ./app  # Dockerfile 存放在 ./app 目录
    ports:
      - "8080:80"
# 运行 docker-compose up 时，docker-compose 会将 app 目录作为上下文发送给 Docker 守护进程。
```

- **dockerfile**：备用的Dockerfile文件，此指令依赖于context指令；

```yaml
# dockerfile 用于指定要使用的 Dockerfile 文件名（默认是 Dockerfile）
version: '3.8'
services:
  app:
    build:
      context: ./app
      dockerfile: Dockerfile.prod
    ports:
      - "8080:80"
# dockerfile: Dockerfile.prod 指定使用 app 目录中的 Dockerfile.prod 文件，而不是默认的 Dockerfile。
# 适用于同一目录下有多个 Dockerfile 的情况，比如开发和生产环境分开。
```

- **args**：构建参数，常用于向Dockerfile中由ARG指令定义的构建参数传值；

```dockerfile
# ./app/dockerfile
FROM python:3.9
ARG APP_ENV=development
ENV APP_ENV=${APP_ENV}
RUN echo "Building for environment: ${APP_ENV}"
```

```yaml
version: '3.8'
services:
  app:
    build:
      context: ./app
      args:
        APP_ENV: production

# args 将 APP_ENV 设置为 production，覆盖 Dockerfile 中的默认值 development。
# 构建时会输出：Building for environment: production。
```

- **cache_from**：解析缓存时使用的镜像列表，由3.2版本引入；

```yaml
# Docker 使用缓存来避免重复构建相同的步骤
# cache_from 允许指定已存在的镜像作为缓存来源
version: '3.8'
services:
  app:
    build:
      context: ./app
      cache_from:
        - myregistry.com/myapp:cache

# cache_from 指定镜像 myregistry.com/myapp:cache 作为缓存
# 如果该镜像中有匹配的构建步骤，Docker 会跳过这些步骤，从而加速构建
```

- **labels**：向镜像添加元数据的标签，由3.3版本引入；

```yaml
version: '3.8'
services:
  app:
    build:
      context: ./app
      labels:
        com.example.version: "1.0.0"
        com.example.author: "Your Name"
        
# 可以通过 docker inspect 查看这些标签
```

- **target**：基于多阶段镜像构建方式构建镜像时指定目标阶段，由3.4版本引入；

```dockerfile
FROM node:16 AS build
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

```yaml
version: '3.8'
services:
  app:
    build:
      context: .
      target: build

# target: build 指定只构建 Dockerfile 中的 build 阶段，而不包含 nginx 阶段
# 常用于调试构建过程，或仅构建特定阶段
```

**综合示例**

```yaml
version: '3.8'
services:
  app:
    build:
      context: ./app
      dockerfile: Dockerfile.prod
      args:
        APP_ENV: production
      cache_from:
        - myregistry.com/myapp:cache
      labels:
        com.example.version: "1.0.0"
        com.example.author: "Your Name"
      target: build
    ports:
      - "8080:80"
```

##### command和entrypoint

基于镜像启动容器器时，command指定的命令覆盖镜像上默认的由CMD定义要运行的命令，而 entrypoint指定的命令则覆盖镜像上由ENTRYPOINT定义要运行的命令，二者命令格式分别同 Dockerfile的CMD和ENTRYPOINT。

##### cap_add和cap_drop

用于调整容器器操作内核的权利与能力，cap_add用于添加容器运行时可用的能力，而cap_drop则相反。 群集模式（swarm）会忽略此参数。

```yaml
```



#### Compose的网络配置



#### Volumes的常用指令



### docker-compose 命令行

docker-compose命令用于构建和管理Compose文件定义的服务等对象，命令的语法格式：

```bash
docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]
```

其中的-f选项用于指定使用Compose配置文件，默认为当前目录下的docker-compose.yaml，但也可以使用多个-f选项同时指定多个配置文件，运行时，Compose会将它们合并为一个配置，并按照文件的顺序构建配置，后续的文件将覆盖并添加到前面的文件中。另外，每个配置都应该有一个项目名称，也可以使用-p选项指定项目名称。未指定时，Compose将使用当前目录的名称。下面是命令的简明使用帮助。

```bash
# 启动compose
docker-compose -f file up

# 关闭并删除容器
docker-compose -f file down

# 检查compose语法
docker-compose -f file config -q

# 查看镜像
docker-compose -f file images

# 查看容器
docker-compose -f file ps
```





## 仓库管理

### 分布式仓库 Harbor

#### Harbor 介绍和架构

![image-20250205223045296](D:\git_repository\cyber_security_learning\markdown_img\image-20250205223045296.png)

Harbor (港口,海港) 是一个用于存储和分发Docker镜像的企业级Registry服务器，由VMware开源，其通过添加一些企业必需的功能特性，例如安全、标识和管理等，扩展了开源 Docker Distribution。作为一 个企业级私有Registry服务器，Harbor 提供了更好的性能和安全。提升用户使用Registry构建和运行环境传输镜像的效率。Harbor支持安装在多个Registry节点的镜像资源复制，镜像全部保存在私有  Registry 中， 确保数据和知识产权在公司内部网络中管控，另外，Harbor也提供了高级的安全特性，诸如用户管理，访问控制和活动审计等

vmware 官方开源服务:   https://vmware.github.io/

harbor 官方 github 地址:   https://github.com/vmware/harbor 

harbor 官方网址:  https://goharbor.io/

harbor 官方文档:   https://goharbor.io/docs/

github文档:  :   https://github.com/goharbor/harbor/tree/master/docs



#### Harbor 功能官方介绍

- 基于角色的访问控制:  用户与Docker镜像仓库通过“项目”进行组织管理，一个用户可以对多个镜像 仓库在同一命名空间（project）里有不同的权限
- 镜像复制:  镜像可在多个Registry实例中复制（同步）。尤其适合于负载均衡，高可用，混合云和 多云的场景
- 图形化用户界面:  用户可以通过浏览器来浏览，检索当前Docker镜像仓库，管理项目和命名空间
- AD/LDAP 支:  Harbor可以集成企业内部已有的AD/LDAP，用于鉴权认证管理
- 审计管理:  所有针对镜像仓库的操作都可以被记录追溯，用于审计管理
- 国际化:  已拥有英文、中文、德文、日文和俄文的本地化版本。更多的语言将会添加进来
- RESTful API:  提供给管理员对于Harbor更多的操控, 使得与其它管理软件集成变得更容易
- 部署简单:  提供在线和离线两种安装工具， 也可以安装到vSphere平台(OVA方式)虚拟设备



#### 安装 Harbor

下载地址:   https://github.com/vmware/harbor/releases



##### 环境准备:  共四台主机

- 两台主机harbor服务器，地址:  10.0.0.101|102
- 两台主机harbor客户端上传和下载镜像

![image-20250205223819316](D:\git_repository\cyber_security_learning\markdown_img\image-20250205223819316.png)

##### 安装 docker

使用脚本安装，脚本内容如下

```bash
#!/bin/bash
#
#********************************************************************
#Author:            wangxiaochun
#QQ:                29308620
#Date:              2022-10-14
#FileName:          install_docker_offline.sh
#URL:               http://www.wangxiaochun.com
#Description:       The test script
#Copyright (C):     2022 All rights reserved
#********************************************************************

#支持在线和离线安装

DOCKER_VERSION=26.1.4
#DOCKER_VERSION=26.0.0
#DOCKER_VERSION=24.0.7
#DOCKER_VERSION=24.0.5
#DOCKER_VERSION=23.0.3
#DOCKER_VERSION=20.10.19

URL=https://mirrors.tuna.tsinghua.edu.cn
#URL=https://mirrors.aliyun.com
#URL=https://download.docker.com

color () {
    RES_COL=60
    MOVE_TO_COL="echo -en \\033[${RES_COL}G"
    SETCOLOR_SUCCESS="echo -en \\033[1;32m"
    SETCOLOR_FAILURE="echo -en \\033[1;31m"
    SETCOLOR_WARNING="echo -en \\033[1;33m"
    SETCOLOR_NORMAL="echo -en \E[0m"
    echo -n "$1" && $MOVE_TO_COL
    echo -n "["
    if [ $2 = "success" -o $2 = "0" ] ;then
        ${SETCOLOR_SUCCESS}
        echo -n $"  OK  "    
    elif [ $2 = "failure" -o $2 = "1"  ] ;then 
        ${SETCOLOR_FAILURE}
        echo -n $"FAILED"
    else
        ${SETCOLOR_WARNING}
        echo -n $"WARNING"
    fi
    ${SETCOLOR_NORMAL}
    echo -n "]"
    echo 
}

prepare () {
    if [ ! -e docker-${DOCKER_VERSION}.tgz ];then
        #wget ${URL}/docker-ce/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
        wget ${URL}/docker-ce/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
    fi
    [ $? -ne 0  ] && { echo "文件下载失败"; exit; }
}

install_docker () {
    tar xf docker-${DOCKER_VERSION}.tgz -C /usr/local/
    cp /usr/local/docker/* /usr/local/bin/
    cat > /lib/systemd/system/docker.service <<-EOF
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target

[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/local/bin/dockerd -H unix://var/run/docker.sock
ExecReload=/bin/kill -s HUP \$MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s

[Install]
WantedBy=multi-user.target
EOF
    systemctl daemon-reload
}

config_docker () {
    mkdir -p /etc/docker
    tee /etc/docker/daemon.json <<-'EOF'
    {
      "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"]
     }
EOF
    #systemctl restart docker

}

start_docker (){
    systemctl enable --now docker
    docker version && color "Docker 安装成功" 0 ||  color "Docker 安装失败" 1
}


config_docker_completion () {
    wget -P /etc/bash_completion.d http://www.wangxiaochun.com:8888/testdir/docker/docker_completion 
    #source /etc/bash_completion.d/docker_completion
}


prepare

install_docker

config_docker

start_docker

config_docker_completion
```



##### 先安装docker compose

```bash
# Add Docker's official GPG key:
apt-get update
apt-get install ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

echo "GPG OVER"

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# 官方仓库配置好后，执行下面的指令
[root@ubuntu2204 ~]#apt install -y docker-compose-plugin
```



##### 下载Harbor安装包并解压缩

```bash
[root@ubuntu2204 ~]#wget https://github.com/goharbor/harbor/releases/download/v2.12.2/harbor-offline-installer-v2.12.2.tgz

[root@ubuntu2204 ~]#mkdir /apps
[root@ubuntu2204 ~]#tar xvf harbor-offline-installer-v2.12.2.tgz -C /apps/
harbor/harbor.v2.12.2.tar.gz
harbor/prepare
harbor/LICENSE
harbor/install.sh
harbor/common.sh
harbor/harbor.yml.tmpl
```



##### 编辑 harbor 配置文件

```bash
[root@ubuntu2204 harbor]#cd /apps/harbor
[root@ubuntu2204 harbor]#cp harbor.yml.tmpl harbor.yml
[root@ubuntu2204 harbor]#vim harbor.yml
# 更改配置文件的主机名，这里为了实验简单，故而使用ip
# hostname: harbor.mystical.org
hostname: 10.0.0.100

# 将https注视掉
#https:
  # https port for harbor, default is 443
#  port: 443
  # The path of cert and key files for nginx
#  certificate: /your/certificate/path
#  private_key: /your/private/key/path

# 更改harbor的登录密码
harbor_admin_password: 123456

# 更改数据目录
# The default data volume
data_volume: /data/harbor

[root@ubuntu2204 harbor]#ls
common.sh  harbor.v2.12.2.tar.gz  harbor.yml  harbor.yml.tmpl  install.sh  LICENSE  prepare

# 使用prepare拉取镜像并生成配置文件
[root@ubuntu2204 harbor]#./prepare 

# 使用install.sh
[root@ubuntu2204 harbor]#./install.sh 

# 查看
[root@ubuntu2204 harbor]#docker compose ps
NAME                IMAGE                                 COMMAND                   SERVICE       CREATED          STATUS                             PORTS
harbor-core         goharbor/harbor-core:v2.12.2          "/harbor/entrypoint.…"   core          26 seconds ago   Up 19 seconds (health: starting)   
harbor-db           goharbor/harbor-db:v2.12.2            "/docker-entrypoint.…"   postgresql    26 seconds ago   Up 20 seconds (health: starting)   
harbor-jobservice   goharbor/harbor-jobservice:v2.12.2    "/harbor/entrypoint.…"   jobservice    26 seconds ago   Up 9 seconds (health: starting)    
harbor-log          goharbor/harbor-log:v2.12.2           "/bin/sh -c /usr/loc…"   log           26 seconds ago   Up 24 seconds (health: starting)   127.0.0.1:1514->10514/tcp
harbor-portal       goharbor/harbor-portal:v2.12.2        "nginx -g 'daemon of…"   portal        26 seconds ago   Up 20 seconds (health: starting)   
nginx               goharbor/nginx-photon:v2.12.2         "nginx -g 'daemon of…"   proxy         26 seconds ago   Up 18 seconds (health: starting)   0.0.0.0:80->8080/tcp, [::]:80->8080/tcp
redis               goharbor/redis-photon:v2.12.2         "redis-server /etc/r…"   redis         26 seconds ago   Up 21 seconds (health: starting)   
registry            goharbor/registry-photon:v2.12.2      "/home/harbor/entryp…"   registry      26 seconds ago   Up 20 seconds (health: starting)   
registryctl         goharbor/harbor-registryctl:v2.12.2   "/home/harbor/start.…"   registryctl   26 seconds ago   Up 20 seconds (health: starting) 
```



##### 实现开机自动启动 harbor

旧版 Harbor 开机不会自动启动，可以创建 service 文件实现

新版 Harbor 默认开机自动，比如：harbor-v2.9.1

```bash
[root@harbor ~]#vim /lib/systemd/system/harbor.service
[Unit]
Description=Harbor
After=docker.service systemd-networkd.service systemd-resolved.service
Requires=docker.service
Documentation=http://github.com/vmware/harbor

[Service]
Type=simple
Restart=on-failure
RestartSec=5
ExecStart=/usr/bin/docker-compose -f  /apps/harbor/docker-compose.yml up
ExecStop=/usr/bin/docker-compose -f /apps/harbor/docker-compose.yml down

[Install]
WantedBy=multi-user.target

[root@harbor ~]#systemctl daemon-reload 
[root@harbor ~]#systemctl enable harbor
```



#### 登录 harbor 主机网站

用浏览器访问:   http://10.0.0.100/

- 用户名:  admin
- 密码:  即前面harbor.yml中指定的密码

![image-20250205230259130](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230259130.png)

![image-20250205230320523](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230320523.png)



### 使用单主机 Harbor

#### 建立项目

**harbor上必须先建立项目，才能上传镜像**

![image-20250205230642513](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230642513.png)

![image-20250205230713546](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230713546.png)

![image-20250205230806935](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230806935.png)



#### 创建用户和项目授权

##### 创建用户

![image-20250205230911713](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230911713.png)

![image-20250205230956394](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230956394.png)

![image-20250205231026855](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231026855.png)



##### 在项目内对用户授权

进入对应的项目，，注意：至少是开发者以上才能上传镜像

![image-20250205231233881](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231233881.png)

![image-20250205231314266](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231314266.png)

![image-20250205231342108](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231342108.png)



#### 命令行登录 Harbor

查看推送地址与相关命令

![image-20250205231933464](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231933464.png)

```bash
# 推送镜像前，要将镜像改名
# docker tag SOURCE_IMAGE[:TAG] 10.0.0.100/example/REPOSITORY[:TAG]
[root@ubuntu2204 ~]#docker tag nginx:latest 10.0.0.100/example/nginx:latest

# 目前推送会报错
# 首先默认会使用https推送，但是我们这边使用http，所以需要将host加入Insecure Registries中
# 这里不安全的仓库，指的就是使用http，而不是https
[root@ubuntu2204 ~]#cat /etc/docker/daemon.json 
{
   "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"],
   "insecure-registries": ["harbor.mystical.org", "10.0.0.100"]
}

# 重启docker服务
[root@ubuntu2204 ~]#systemctl restart docker

# 查看
[root@ubuntu2204 ~]#docker info
......
 Insecure Registries:
  10.0.0.100
  harbor.mystical.org
  127.0.0.0/8
......

# 推送镜像前，要登录harbor
[root@ubuntu2204 ~]#docker login 10.0.0.100
Username: zhangyifeng
Password: 
# 只需登录一次，登录信息会记录在config.json文件中，无需反复登录
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

# 推送镜像
[root@ubuntu2204 ~]#docker push 10.0.0.100/example/nginx:latest 
The push refers to repository [10.0.0.100/example/nginx]
e2eb04df0bda: Pushed 
1b78ffef68d1: Pushed 
16649054d94a: Pushed 
a280e15d559d: Pushed 
0b2dafd61482: Pushed 
2cdcaebcf23c: Pushed 
7914c8f600f5: Pushed 
latest: digest: sha256:0b2c307c84395005578e9e35ee4bc6c00387cd4573e8098d656245895dc1f7d5 size: 1778

# 浏览器查看
```

![image-20250205232824550](D:\git_repository\cyber_security_learning\markdown_img\image-20250205232824550.png)

```bash
# 在10.0.0.100查看harbor数据目录
[root@ubuntu2204 harbor]#du -sh /data/harbor
119M	/data/harbor

# 在其他服务器上拉去harbor上的镜像
# 将其加入insecure-registries
[root@ubuntu2204 ~]#cat /etc/docker/daemon.json 
{
   "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"],
   "insecure-registries": ["harbor.mystical.org", "10.0.0.100"]
}

# 重启docker服务
[root@ubuntu2204 ~]#systemctl restart docker

# 拉取镜像
[root@ubuntu2204 ~]#docker pull 10.0.0.100/example/nginx:latest
latest: Pulling from example/nginx
d2eb42b4a5eb: Pull complete 
ee083de5ceda: Pull complete 
5afd6583b29c: Pull complete 
8c2914db26a3: Pull complete 
1e8aefce6919: Pull complete 
a982d09283a6: Pull complete 
ab571a6216e3: Pull complete 
Digest: sha256:0b2c307c84395005578e9e35ee4bc6c00387cd4573e8098d656245895dc1f7d5
Status: Downloaded newer image for 10.0.0.100/example/nginx:latest
10.0.0.100/example/nginx:latest
```





### 实现 Harbor 高可用

![image-20250205235448305](D:\git_repository\cyber_security_learning\markdown_img\image-20250205235448305.png)

Harbor支持基于策略的Docker镜像复制功能，这类似于MySQL的主从同步，其可以实现不同的数据中 心、不同的运行环境之间同步镜像，并提供友好的管理界面，大大简化了实际运维中的镜像管理工作， 已经有用很多互联网公司使用harbor搭建内网docker仓库的案例，并且还有实现了双向复制功能



#### 安装第二台 harbor主机

在第二台主机上安装部署好harbor，并登录系统

![image-20250205235601361](D:\git_repository\cyber_security_learning\markdown_img\image-20250205235601361.png)



#### 第二台harbor上新建项目

参考第一台harbor服务器的项目名称，在第二台harbor服务器上新建与之同名的项目

![image-20250205235735134](D:\git_repository\cyber_security_learning\markdown_img\image-20250205235735134.png)

![image-20250206000014158](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000014158.png)



#### 在源主机上新建目标

注意：有镜像的，将要传递镜像给目的主机的服务器为源主机，该实验中为10.0.0.100

![image-20250206000235404](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000235404.png)

![image-20250206000400238](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000400238.png)

![image-20250206000425158](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000425158.png)

![image-20250206000450030](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000450030.png)



#### 复制管理

![image-20250206000618204](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000618204.png)

![image-20250206000746061](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000746061.png)

![image-20250206000830129](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000830129.png)



#### 初始手动触发复制

![image-20250206000924963](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000924963.png)

![image-20250206000934456](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000934456.png)

![image-20250206000947520](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000947520.png)

![image-20250206001009365](D:\git_repository\cyber_security_learning\markdown_img\image-20250206001009365.png)



#### 在目标服务器上查看

![image-20250206001104394](D:\git_repository\cyber_security_learning\markdown_img\image-20250206001104394.png)



#### 在镜像上传至源服务器，观察目标服务器

```bash
[root@ubuntu2204 ~]#docker pull alpine
Using default tag: latest
latest: Pulling from library/alpine
1f3e46996e29: Pull complete 
Digest: sha256:56fa17d2a7e7f168a043a2712e63aed1f8543aeafdcee47c58dcffe38ed51099
Status: Downloaded newer image for alpine:latest
docker.io/library/alpine:latest

[root@ubuntu2204 ~]#docker tag alpine:latest 10.0.0.100/example/alpine:latest
[root@ubuntu2204 ~]#docker push 10.0.0.100/example/alpine:latest
The push refers to repository [10.0.0.100/example/alpine]
a0904247e36a: Pushed 
latest: digest: sha256:c10f729849a3b03cbf222e2220245dd44c39a06d444aa32cc30a35c4c1aba59d size: 527
```

**查看源harbor**

![image-20250206001436193](D:\git_repository\cyber_security_learning\markdown_img\image-20250206001436193.png)

**查看目标服务器**

![image-20250206001508918](D:\git_repository\cyber_security_learning\markdown_img\image-20250206001508918.png)



#### 反向再做一遍，实现双向复制







# CICD



## 私有软件仓库 GitLab

![image-20250206113905921](D:\git_repository\cyber_security_learning\markdown_img\image-20250206113905921.png)



GitLab 是一个基于Ruby on Rails构建用于仓库管理系统的开源项目，使用Git作为代码管理工具，提供 了Web界面进行访问公开的或者私有的项目

GitLab 特性

- 开源免费
- 可以作为 Git 代码仓库
- 提供了方便易用的 Web 管理界面
- 支持多租户
- 功能丰富
- 支持离线提交
- 安全性高, 可以对不同的用户设置不同的权限,并且支持不同用户只能访问特定的代码,实现代码部分可见



### GitLab 架构

Gitlab 是一个由很多应用组成复杂的系统

```http
https://panlw.github.io/15365441001781.html
```

![image-20250206114524326](D:\git_repository\cyber_security_learning\markdown_img\image-20250206114524326.png)



Gitlab的服务构成

- **Nginx**：静态web服务器
- **GitLab shell**：用于处理基于ssh会话的Git命令和修改authorized keys列表
- **gitlab-workhorse**：轻量级的反向代理服务器,它旨在充当智能反向代理，以帮助整个 GitLab 加速 
- **unicorn**：An HTTP server for Rack applications, GitLab Rails应用是托管在这个服务器上面的
- **Gitaly**：Git RPC service for handing all Git calls made by GitLab
-  **Puma (GitLab Rails)**：处理发往Web接口和API的请求
- **postgresql**：数据库
- **redis**：缓存数据库
- **sidekiq**：用于在后台执行队列任务（异步执行)
- **GitLab Exporter**：GitLab指标暴露器
- **Node Exporter**：节点指标暴露器
- **GitLab self-monitoring的多个组件**：Prometheus、Alertmanager、Grafana、Sentry和Jaeger
- **Inbound emails（SMPT）**：接收用于更新issue的邮件
- **Outbound email (SMTP)**：向用户发送邮件通知
- **LDAP Authentication**：LDAP认证集成
- **MinIO**：对象存储服务
- **Registry**：容器注册表，支持Image的push和pull操作
- **Runner**：执行GitLab的CI/CD作业



**Omnibus GitLab**

由于Gitlab 组件众多,各个组件的分别管理配置过于复杂,所以官方提供了 Omnibus GitLab 项目实现方便的管理 

Omnibus GitLab是基于Chef的应用编排工具，它基于Chef的cookbooks和recipes等组件自动化编排 GitLab的各组件，避免了用户复杂的配置过程

相关项目  https://gitlab.com/gitlab-org/omnibus-gitla

Omnibus GitLab architecture and components:  https://docs.gitlab.com/omnibus/architecture/

![image-20250206115900821](D:\git_repository\cyber_security_learning\markdown_img\image-20250206115900821.png)



管理各组件使用统一命令为**gitlab-ctl**，例如`gitlab-ctl reconfigure`或`gitlab-ctl restart`等能统—执行各组 件的重新配置及重启操作

此外还有一些各组件专用的命令，如:`gitlab-backup`,`gitlab-pgsql`,`gitlab-rails`和`gitlab-rake`等

提供统一配置模板文件, 用于为GitLab中的每个组件提供配置信息

在配置模板文件中对于每个组件配置参数格式为: `['']=`



### GitLab 包安装

GitLab 有两个版本：**EE商业版**和**CE社区版**，以下使用CE版



#### 安装方法

Gitlab 服务的安装文档

```http
https://docs.gitlab.com/ce/install/
```

安装方法说明

```http
https://docs.gitlab.com/ee/install/install_methods.html
```

-  **Linux 安装包**：官方的 deb/rpm 安装包（也被称作 Omnibus GitLab）包含极狐GitLab 和依赖的 组件，包括PostgreSQL、Redis 和 Sidekiq
- **Source**：源码安装，在GitLab没有提供适用的安装包的平台上（例如各类BSD系统）只能采用这种安装方式
- **Docker**：Docker 容器化的极狐GitLab 软件包
- **GitLab Operator**：Kubernetes Operator风格的部署模式
- **Helm Chart**：用于在 Kubernetes 上安装极狐GitLab 及其所有组件的云原生 Helm chart
- **GitLab Environment Toolkit（GET）**：自动化工具集，用于在主流的公有云（Azure、GCP和 AWS）上部署GitLab 



#### 安装 GitLab 要求

Gitlab硬件和软件的环境要求：

```http
https://docs.gitlab.com/ce/install/requirements.html
```

硬件配置要求较高：

- 测试环境：内存4G以上
- 生产环境：建议CPU2C以上，内存8G以上，磁盘10G以上配置，和用户数有关

```ABAP
注意:如果内存较低,可以会导致Gitlab有些服务无法启动,建议4G以上内存
```



#### 安装前准备

##### Ubuntu 系统环境安装前准备

配置ubuntu 仓库

配置阿里云或清华大学等国内镜像仓库实现加速

```bash
[root@ubuntu1804 ~]#vim /etc/apt/sources.list
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe
multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
debhttps://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
```



##### RHEL 系统环境安装前准备

基于最小化服务器安装，建议修改配置如下：

```bash
[root@centos ~]# wget -O /etc/yum.repos.d/epel.repo 
http://mirrors.aliyun.com/repo/epel-7.repo
[root@centos ~]# systemctl disable firewalld
[root@centos ~]# sed -i '/SELINUX/s/enforcing/disabled/' /etc/sysconfig/selinux
[root@centos ~]# hostnamectl set-hostname gitlab.example.com
[root@centos ~]# reboot
```



#### GitLab 安装

gitlab 安装有多种方式,下面选择包安装方式

**官方gitlab 包下载链接**

```http
https://packages.gitlab.com/gitlab
```

![image-20250206121909398](D:\git_repository\cyber_security_learning\markdown_img\image-20250206121909398.png)

**GitLab-CE 安装包官方下载地址**

```http
https://packages.gitlab.com/gitlab/gitlab-ce
```

**yum源清华大学下载地址：**

```http
https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/
```

范例：Ubuntu2204下载并安装 GitLab

```bash
# 在官方下载最新版本
[root@ubuntu2204 ~]#wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/ubuntu/jammy/gitlab-ce_17.6.4-ce.0_amd64.deb/download.deb

# Ubuntu 国内镜像下载 
[root@ubuntu2004 ~]#wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu/pool/jammy/main/g/gitlab-ce/gitlab-ce_17.8.1-ce.0_amd64.deb

# 安装
[root@ubuntu2204 ~]#apt install -y ./gitlab-ce_17.6.4-ce.0_amd64.deb
```

![image-20250206125844241](D:\git_repository\cyber_security_learning\markdown_img\image-20250206125844241.png)



#### 修改 GitLab 配置

##### gitlab相关的目录

```bash
/etc/gitlab         #配置文件目录，重要
/var/opt/gitlab     #数据目录,源代码就存放在此目录,重要
/var/log/gitlab     #日志目录 
/run/gitlab         #运行目录,存放很多的数据库文件
/opt/gitlab         #安装目录
```

##### gitlab 初始化配置

```bash
# 指定域名【必选】
[root@ubuntu1804 ~]#vim /etc/gitlab/gitlab.rb
[root@ubuntu1804 ~]#grep "^[a-Z]" /etc/gitlab/gitlab.rb
external_url 'http://gitlab.mystical.org'   

# 邮件通知设置【可选】
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.163.com"
gitlab_rails['smtp_port'] = 465
gitlab_rails['smtp_user_name'] = "15104600741@163.com"
gitlab_rails['smtp_password'] = "授权码"
gitlab_rails['smtp_domain'] = "163.com"
gitlab_rails['smtp_authentication'] = "login"
#gitlab_rails['smtp_enable_starttls_auto'] = true       # 二选一：该选项端口587
gitlab_rails['smtp_tls'] = true                         # 二选一：该选项端口465
gitlab_rails['smtp_pool'] = false

###! **Can be: 'none', 'peer', 'client_once', 'fail_if_no_peer_cert'**
###! Docs: http://api.rubyonrails.org/classes/ActionMailer/Base.html
gitlab_rails['smtp_openssl_verify_mode'] = 'none'
user['git_user_email'] = "15104600741@163.com"

# 修改nginx监听的端口【可选】
nginx['listen_port']=8080

# ssh协议端口，地址【可选】
gitlab_sshd['listen_address'] = '0.0.0.0:2222'
# 示例：ssh://git@gitlab.wang.org:2222/example/app.git

# 给root用户指定初始密码【必选】
#注意:密码至少8位并且复杂度要求才是有效密码
gitlab_ralis['initial_root_password'] = "zyf@123456"

# gitlab优化
# 关闭可能暂时不使用的功能，比如监控(测试环境下)
prometheus['enable'] = false
prometheus['monitor_kubernetes']=false
alertmanager['enable']=false
node_exporter['enable']=false
redis_exporter['enable']=false
postgres_exporter['enable']=false
gitlab_exporter['enable']= false
prometheus_monitoring['enable']=false
grafana['enable']=false

# 名称解析
[root@mystical ~]# vim /etc/hosts
```



#### 初始化和启动服务

执行配置reconfigure并启动服务：

```bash
#每次修改完配置文件都需要执行此操作
[root@ubuntu1804 ~]# gitlab-ctl reconfigure
```



#### 验证Gitlab启动完成

```bash
[root@mystical ~]# gitlab-ctl status
run: gitaly: (pid 15033) 17s; run: log: (pid 14586) 144s
run: gitlab-kas: (pid 14803) 130s; run: log: (pid 14814) 127s
run: gitlab-workhorse: (pid 15011) 19s; run: log: (pid 14946) 49s
run: logrotate: (pid 14502) 159s; run: log: (pid 14511) 156s
run: nginx: (pid 15025) 18s; run: log: (pid 14966) 44s
run: postgresql: (pid 14633) 136s; run: log: (pid 14644) 135s
run: puma: (pid 14866) 63s; run: log: (pid 14873) 62s
run: redis: (pid 14538) 153s; run: log: (pid 14548) 150s
run: sidekiq: (pid 14887) 57s; run: log: (pid 14904) 55s
```



#### Gitlab的常用命令

GitLab除了使用Web界面进行管理，还提供了各组件的统一命令为gitlab-ctl，此外还有一些各组件专用的命令，如gitlab-pgsql、 gitlab-rails和gitlab-rake等

```bash
#客户端命令行操作行
gitlab-ctl  
gitlab-ctl check-config #检查配置
gitlab-ctl show-config  #查看配置
gitlab-ctl reconfigure  #修改过配置后需要执行重新配置
gitlab-ctl stop         #停止gitlab
gitlab-ctl start        #启动gitlab
gitlab-ctl restart      #重启gitlab
gitlab-ctl status       #查看组件运行状态
gitlab-ctl tail         #查看所有日志
gitlab-ctl tail nginx   #查看某个组件的日志
gitlab-ctl service-list #列出服务

#其它命令
gitlab-rails #用于启动控制台进行特殊操作，如修改管理员密码、打开数据库控制台( gitlab-rails dbconsole)等
gitlab-psql #数据库命令行
gitlab-rake #数据备份恢复等数据操作
```

示例: 查看服务列表

```bash
[root@mystical ~]# gitlab-ctl service-list
gitaly*
gitlab-kas*
gitlab-workhorse*
logrotate*
nginx*
postgresql*
puma*
redis*
sidekiq*
```



#### 在浏览器访问GitLab

在新版gitlab中第一次登录的界面发生变化,取消重设密码界面,需要直接输入用户和密码才能登录

**默认用户为root，其密码是随机生成**

![image-20250208154751291](D:\git_repository\cyber_security_learning\markdown_img\image-20250208154751291.png)

```bash
# 初始账号为root
# 初始密码为配置文件自行指定的密码
```

![image-20250208155656668](D:\git_repository\cyber_security_learning\markdown_img\image-20250208155656668.png)





### 基于 Kubernetes 安装 GitLab

```http
https://docs.gitlab.com/operator/installation.html
```

注意：资源建议

```ABAP
master: 4核CPU + 4G内存
node1: 4核CPU + 6G内存
node1: 4核CPU + 6G内存
node1: 4核CPU + 6G内存

低于上述配置，可能会因为资源不足，导致服务异常
```

范例：注意相关镜像可能需要科学上网

```bash
# 提前安装cert-manager证书管理组件
# 官方cert-manager.yaml文件路径：https://github.com/cert-manager/cert-manager/releases/
# 根据需要，自行选定版本的cert-manager.yaml
# 示例以v1.17.0为例，此为20250208最新版 
[root@master1 ~]# wget https://www.mysticalrecluse.com/script/tools/cert-manager.yaml
[root@master1 ~]# kubectl apply -f cert-manager.yaml 

# 部署 GitLab Operator
# GL_OPERATOR_VERSION=1.9.1 
# PLATFORM=kubernetes
# 为gitlab创建名称空间
[root@master1 ~]# kubectl create namespace gitlab-system

# 创建动态置备的sc，并将其设置为default，这一步必须做，否则gitlab无法自动创建pv
# 创建sc，看Kubernetes数据存储相关教学，创建完sc后，使用下面指令，将其设置为默认
[root@master1 ~]# kubectl patch storageclass sc-nfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

# 设置完后查看sc状态
[root@master1 test]#kubectl get sc
NAME               PROVISIONER                                   RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
sc-nfs (default)   k8s-sigs.io/nfs-subdir-external-provisioner   Delete          Immediate           false                  27d


# gitlab operator的各版本yaml文件下载路径：
# https://gitlab.com/gitlab-org/cloud-native/gitlab-operator/-/releases
[root@master1 ~]# wget https://gitlab.com/api/v4/projects/18899486/packages/generic/gitlab-operator/1.9.1/gitlab-operator-kubernetes-1.9.1.yaml

# 启用operator
[root@master1 ~]# kubectl apply -f gitlab-operator-kubernetes-1.9.1.yaml

# 创建GitLab用户资源
[root@master1 ~]# cat mygitlab.yaml 
apiVersion: apps.gitlab.com/v1beta1
kind: GitLab
metadata:
  name: gitlab
spec:
  chart:
    # 使用下面链接查看version
    # https://gitlab.com/gitlab-org/cloud-native/gitlab-operator/-/blob/1.9.1/CHART_VERSIONS
    version: "8.8.1" 
    values:
      global:
        hosts:
          domain: "mygitlab.mystical.org"  # use a real domain here
        ingress:
          configureCertmanager: true
      certmanager-issuer:
        email: mysticalrecluse@gmail.com   # use your real email address here
        
# 启用gitlab
[root@master1 ~]# kubectl apply -f mygitlab.yaml -n gitlab-system

# 如果启动成功，查看状态如下
[root@master1 ~]#kubectl get gitlabs -n gitlab-system 
NAME     STATUS    VERSION
gitlab   Running   8.8.1

#  访问gitlab.mygitlab.mystical.org
```

```ABAP
注意：由于资源问题，服务可能因为就绪探针和生存探针，导致起不来，反复重启，建议将webservice和sidekiq的deployment的探针取消
注意：在取消探针前，记得将operator的controller-manager停掉，即将副本数量设为0即可
```



![image-20250208125113586](D:\git_repository\cyber_security_learning\markdown_img\image-20250208125113586.png)

```bash
# 默认账号：root
# 初始密码：执行下列指令
[root@master1 ~]# kubectl get secret -n gitlab-system gitlab-gitlab-initial-root-password -o jsonpath="{.data.password}" | base64 --decode
mKycBGLxob511Rq2VopJ51URSWdphI7qVHass9t74LoZiglxdmMKSgrCUPkIAFS2	
```

![image-20250208125336856](D:\git_repository\cyber_security_learning\markdown_img\image-20250208125336856.png)

```bash
# 查看所有的ingress
[root@master1 ~]#kubectl get ingress -n gitlab-system 
NAME                        CLASS          HOSTS                            ADDRESS     PORTS     AGE
gitlab-kas                  gitlab-nginx   kas.mygitlab.mystical.org        10.0.0.10   80, 443   3h9m
gitlab-minio                gitlab-nginx   minio.mygitlab.mystical.org      10.0.0.10   80, 443   3h26m
gitlab-registry             gitlab-nginx   registry.mygitlab.mystical.org   10.0.0.10   80, 443   3h9m
gitlab-webservice-default   gitlab-nginx   gitlab.mygitlab.mystical.org     10.0.0.10   80, 443   3h9m

# 尝试访问 minio.mygitlab.mystical.org
```

![image-20250208125839659](D:\git_repository\cyber_security_learning\markdown_img\image-20250208125839659.png)

```bash
# 查看minio的accesskey和secretkey
[root@master1 ~]#kubectl get secret -n gitlab-system gitlab-minio-secret -o yaml
apiVersion: v1
data:
  accesskey: RnJuZkYxd3hRUGN5WWtYdmt1NW1nWkg1VzNJQlhqTWk2ZGZzSzcyaUExYlF1V1I0Z044TTlZYXRFV3B2NUlacg==
  secretkey: T3hUZ1RJbk01UkttSWtLdzJsN25ZRjdaVjlXc3JEYVJaR1F4Y3F4UU5lMlFzWmZmY3J3eTF2N1IySHFSa2hYdw==
kind: Secret
metadata:
  creationTimestamp: "2025-02-08T01:29:09Z"
  labels:
    app: gitlab
    app.kubernetes.io/managed-by: gitlab-operator
    app.kubernetes.io/name: gitlab
    app.kubernetes.io/part-of: gitlab
    chart: gitlab-8.8.1
    heritage: Helm
    release: gitlab
  name: gitlab-minio-secret
  namespace: gitlab-system
  resourceVersion: "174778"
  uid: 9113c545-8eb0-40f3-af90-69817bf61837
type: Opaque

# base64解码
[root@master1 ~]#echo "RnJuZkYxd3hRUGN5WWtYdmt1NW1nWkg1VzNJQlhqTWk2ZGZzSzcyaUExYlF1V1I0Z044TTlZYXRFV3B2NUlacg=="|base64 -d
FrnfF1wxQPcyYkXvku5mgZH5W3IBXjMi6dfsK72iA1bQuWR4gN8M9YatEWpv5IZr
[root@master1 ~]#echo "T3hUZ1RJbk01UkttSWtLdzJsN25ZRjdaVjlXc3JEYVJaR1F4Y3F4UU5lMlFzWmZmY3J3eTF2N1IySHFSa2hYdw=="|base64 -d
OxTgTInM5RKmIkKw2l7nYF7ZV9WsrDaRZGQxcqxQNe2QsZffcrwy1v7R2HqRkhXw

# 使用解码后的key登录
```

![image-20250208130235955](D:\git_repository\cyber_security_learning\markdown_img\image-20250208130235955.png)



**在Kubernetes部署好GitLab后，查看资源情况**

![image-20250208133202056](D:\git_repository\cyber_security_learning\markdown_img\image-20250208133202056.png)



#### 配置邮件通知

**检查 `gitlab-rails-secret` 是否包含 SMTP 配置**

```bash
[root@master1 ~]# kubectl get secret gitlab-rails-secret -n gitlab-system -o yaml

# 如果 data: 下包含 smtp_address，说明 GitLab 已配置 SMTP
# 如果没有 smtp_address，则 GitLab 没有 SMTP 配置，需要手动添加
```



**在 `gitlab.yaml` 永久修改 `smtp_settings`**

**手动获取 `gitlab.yaml`**

```bash
[root@master1 ~]# kubectl get gitlab -n gitlab-system -o yaml > gitlab-latest.yaml
[root@master1 test]# cat gitlab-latest.yaml 
apiVersion: v1
items:
- apiVersion: apps.gitlab.com/v1beta1
  kind: GitLab
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"apps.gitlab.com/v1beta1","kind":"GitLab","metadata":{"annotations":{},"creationTimestamp":"2025-02-08T01:28:45Z","generation":2,"name":"gitlab","namespace":"gitlab-system","resourceVersion":"243958","uid":"ac00fa8b-c9ee-4df0-a666-3263366e5025"},"spec":{"chart":{"values":{"certmanager-issuer":{"email":"mysticalrecluse@gmail.com"},"global":{"hosts":{"domain":"mygitlab.mystical.org"},"ingress":{"configureCertmanager":true},"smtp":{"address":"smtp.163.com","authentication":"login","domain":"163.com","enabled":true,"openssl_verify_mode":"peer","password":{"key":"SMTP_PASSWORD","secret":"gitlab-smtp-secret"},"port":465,"starttls_auto":false,"tls":true,"user_name":"15104600741@163.com"}}},"version":"8.8.1"}},"status":{"conditions":[{"lastTransitionTime":"2025-02-08T07:07:10Z","message":"GitLab is initialized","observedGeneration":2,"reason":"Initialized","status":"True","type":"Initialized"},{"lastTransitionTime":"2025-02-08T07:07:10Z","message":"GitLab is running and available to accept requests","observedGeneration":2,"reason":"Available","status":"True","type":"Available"},{"lastTransitionTime":"2025-02-08T01:46:37Z","message":"GitLab is not currently upgrading","observedGeneration":2,"reason":"Upgrading","status":"False","type":"Upgrading"}],"phase":"Running","version":"8.8.1"}}
    creationTimestamp: "2025-02-08T07:13:15Z"
    generation: 1
    name: gitlab
    namespace: gitlab-system
    resourceVersion: "247693"
    uid: 1624d7c1-3786-47d8-beb7-1ccc1479e2de
  spec:
    chart:
      values:
        certmanager-issuer:
          email: mysticalrecluse@gmail.com
        global:
          hosts:
            domain: mygitlab.mystical.org
          ingress:
            configureCertmanager: true
          smtp:                                    # 从这里开始添加
            address: smtp.163.com
            authentication: login
            domain: 163.com
            enabled: true
            openssl_verify_mode: peer
            password:
              key: SMTP_PASSWORD
              secret: gitlab-smtp-secret
            port: 465
            starttls_auto: false
            tls: true
            user_name: 15104600741@163.com
          email:
            from: "15104600741@163.com"
            reply_to: "15104600741@163.com"      # 添加到这里
      version: 8.8.1
  status:
    conditions:
    - lastTransitionTime: "2025-02-08T07:18:57Z"
      message: GitLab is initialized
      observedGeneration: 1
      reason: Initialized
      status: "True"
      type: Initialized
    - lastTransitionTime: "2025-02-08T07:18:57Z"
      message: GitLab is running and available to accept requests
      observedGeneration: 1
      reason: Available
      status: "True"
      type: Available
    - lastTransitionTime: "2025-02-08T07:14:56Z"
      message: GitLab is not currently upgrading
      observedGeneration: 1
      reason: Upgrading
      status: "False"
      type: Upgrading
    phase: Running
    version: 8.8.1
kind: List
metadata:
  resourceVersion: ""

# 关键
# email.from 为 user_name 相同的邮箱
# reply_to 避免 Reply-To 触发 SMTP 检查
```



**创建secret存放邮箱授权码**

```bash
[root@master1 ~]# kubectl create secret generic gitlab-smtp-secret -n gitlab-system   --from-literal=SMTP_PASSWORD="<授权码>"
```



**应用新配置**

```bash
[root@master1 ~]# kubectl apply -f gitlab-latest.yaml
[root@master1 ~]# kubectl rollout restart deployment gitlab-webservice-default -n gitlab-system
```



<span style="color:tomato;font-weight:700">注意：由于某些原因，我将gitlab-controller-manager关闭了，手动接管整个服务，所以，上述所有的操作前提是gitlab-controller-manager是正常运行的，如果和我一样将其关闭，需执行下列操作，手动将smtp服务注入到configmap中</span>

```ABAP
# 手动修改 ConfigMap 来注入 smtp 配置

kubectl patch configmap -n gitlab-system gitlab-webservice-config --type='merge' -p \
'{"data":{"smtp.yml": "production:\n  enabled: true\n  address: \"smtp.163.com\"\n  port: 465\n  user_name: \"15104600741@163.com\"\n  password: \"你的SMTP密码\"\n  domain: \"163.com\"\n  authentication: \"login\"\n  tls: true\n  starttls_auto: false\n  openssl_verify_mode: \"peer\""}}'

# 让 ConfigMap 生效
kubectl rollout restart deployment -n gitlab-system gitlab-webservice
kubectl rollout restart deployment -n gitlab-system gitlab-sidekiq
kubectl rollout restart deployment -n gitlab-system gitlab-toolbox

# 测试是否生效
kubectl exec -it -n gitlab-system deployment/gitlab-toolbox -- gitlab-rails runner "Notify.test_email('3140394153@qq.com', 'Test Email', 'GitLab SMTP Config Test').deliver_now"

# 如果尤其开启operator的controller-manager会将上述配置覆盖掉，因此，上述方式仅适用于实验环境，在资源有限，正常gitlab无法再k8s上启动的情况下使用。
```



**测试邮件**

```bash
[root@master1 test]#kubectl exec -it -n gitlab-system deployment/gitlab-toolbox -- gitlab-rails runner "Notify.test_email('3140394153@qq.com', 'Test Email', 'GitLab SMTP Config Test').deliver_now"
Defaulted container "toolbox" out of: toolbox, certificates (init), configure (init)
WARNING: Active Record does not support composite primary key.

security_findings has composite primary key. Composite primary key is ignored.

# 成功
```

![image-20250208153458322](D:\git_repository\cyber_security_learning\markdown_img\image-20250208153458322.png)



### GitLab 基本配置

#### 首次登录 GitLab Web 界面修改密码

新版gitlab密码初始化官方帮助链接

```http
https://docs.gitlab.com/omnibus/installation/index.html
```

新版登录后,也需再次修改密码,注意:密码至少8位

![image-20250208155944241](D:\git_repository\cyber_security_learning\markdown_img\image-20250208155944241.png)

![image-20250208160007293](D:\git_repository\cyber_security_learning\markdown_img\image-20250208160007293.png)

![image-20250208160119946](D:\git_repository\cyber_security_learning\markdown_img\image-20250208160119946.png)





####  修改头像

登录gitlab后可能看到用户的头像不能正常显示,可以修改为自定义的头像

Kubernetes部署的GitLab有默认头像，可以正常显示

![image-20250208160335921](D:\git_repository\cyber_security_learning\markdown_img\image-20250208160335921.png)

![image-20250208160403884](D:\git_repository\cyber_security_learning\markdown_img\image-20250208160403884.png)

![image-20250208160416028](D:\git_repository\cyber_security_learning\markdown_img\image-20250208160416028.png)



#### 关闭账号注册功能

新版用户注册界面

![image-20250208160730934](D:\git_repository\cyber_security_learning\markdown_img\image-20250208160730934.png)

关闭注册功能,先用root用户登录

![image-20250208161042568](D:\git_repository\cyber_security_learning\markdown_img\image-20250208161042568.png)

![image-20250208161114717](D:\git_repository\cyber_security_learning\markdown_img\image-20250208161114717.png)

![image-20250208161128553](D:\git_repository\cyber_security_learning\markdown_img\image-20250208161128553.png)

在另一个浏览器登录

![image-20250208161240635](D:\git_repository\cyber_security_learning\markdown_img\image-20250208161240635.png)



#### 修改邮箱地址

![image-20250208161910920](D:\git_repository\cyber_security_learning\markdown_img\image-20250208161910920.png)

![image-20250208161934583](D:\git_repository\cyber_security_learning\markdown_img\image-20250208161934583.png)

此时指定邮箱会收到一封确认邮件

![image-20250208162052996](D:\git_repository\cyber_security_learning\markdown_img\image-20250208162052996.png)

![image-20250208162510672](D:\git_repository\cyber_security_learning\markdown_img\image-20250208162510672.png)



**修改个人资料的邮件地址**

![image-20250208162634481](D:\git_repository\cyber_security_learning\markdown_img\image-20250208162634481.png)

![image-20250208162749521](D:\git_repository\cyber_security_learning\markdown_img\image-20250208162749521.png)

![image-20250208162805076](D:\git_repository\cyber_security_learning\markdown_img\image-20250208162805076.png)

删除旧的邮箱

![image-20250208163033871](D:\git_repository\cyber_security_learning\markdown_img\image-20250208163033871.png)





### GitLab 用户和组管理

#### 用户管理

##### 创建用户

创建gitlab用户账户并登录

![image-20250208163328517](D:\git_repository\cyber_security_learning\markdown_img\image-20250208163328517.png)

![image-20250208163440555](D:\git_repository\cyber_security_learning\markdown_img\image-20250208163440555.png)

输入新的用户信息

![image-20250208172632118](D:\git_repository\cyber_security_learning\markdown_img\image-20250208172632118.png)

![image-20250208172650092](D:\git_repository\cyber_security_learning\markdown_img\image-20250208172650092.png)

为新建的用户设置密码

![image-20250208172749159](D:\git_repository\cyber_security_learning\markdown_img\image-20250208172749159.png)

![image-20250208172837815](D:\git_repository\cyber_security_learning\markdown_img\image-20250208172837815.png)

另找一个浏览器，以新建用户登录gitlab

![image-20250208172947464](D:\git_repository\cyber_security_learning\markdown_img\image-20250208172947464.png)

会提示更改密码，更改后重新登录

![image-20250208173100975](D:\git_repository\cyber_security_learning\markdown_img\image-20250208173100975.png)

![image-20250208173115793](D:\git_repository\cyber_security_learning\markdown_img\image-20250208173115793.png)

创建成功后，会给新账户的邮箱发送提示信息

![image-20250208173333212](D:\git_repository\cyber_security_learning\markdown_img\image-20250208173333212.png)



#### 更改语言

![image-20250208173512645](D:\git_repository\cyber_security_learning\markdown_img\image-20250208173512645.png)

![image-20250208173544945](D:\git_repository\cyber_security_learning\markdown_img\image-20250208173544945.png)

![image-20250208173644083](D:\git_repository\cyber_security_learning\markdown_img\image-20250208173644083.png)



#### 创建组

使用管理员root 或用户都可以创建group组

一个group组里面可以拥有多个project项目分支，可以将开发的用户添加到组里，再进行设置权限

如果gitlab使用者的组织规模较大,每一个group组可以分别对应一个组织,如:某个分公司或部门

如果gitlab使用者的组织规模较小, 每一个group组也可以对应一个项目或业务,即每一个不同的group组 对应同一个组织内部的不同的项目

不同的组中添加不同的开发人员帐号，即可实现对开发者实现权限的管理。

![image-20250208174433922](D:\git_repository\cyber_security_learning\markdown_img\image-20250208174433922.png)

![image-20250208174505641](D:\git_repository\cyber_security_learning\markdown_img\image-20250208174505641.png)

![image-20250208174702480](D:\git_repository\cyber_security_learning\markdown_img\image-20250208174702480.png)

- Private：只有加入组的用户能够访问
- Internal：只有注册到GItLab的用户能够访问
- Public：所有人都能访问

![image-20250208174820378](D:\git_repository\cyber_security_learning\markdown_img\image-20250208174820378.png)





### GitLab 项目管理

#### 创建新项目

项目project属于一个group组,即一般project对应一个项目中的功能模块或服务

注意: 此处在新建项目时先不进行初始化

![image-20250208175340783](D:\git_repository\cyber_security_learning\markdown_img\image-20250208175340783.png)

![image-20250208175905085](D:\git_repository\cyber_security_learning\markdown_img\image-20250208175905085.png)

注意: 此处在新建项目时先不进行初始化

![image-20250208180050971](D:\git_repository\cyber_security_learning\markdown_img\image-20250208180050971.png)

![image-20250211214500681](D:\git_repository\cyber_security_learning\markdown_img\image-20250211214500681.png)

命令行指引

您还可以按照以下说明从计算机中上传现有文件

##### Git 全局设置

```bash
# 在一台网络连通的虚拟机做客户端
# 如果客户端没有将ssh公钥上传到gitlab,则直接拉取仓库会报错
[root@master2 ~/project]$ git clone git@gitlab.mygitlab.mystical.org:devops/m62-hw.git
Cloning into 'm62-hw'...
The authenticity of host 'gitlab.mygitlab.mystical.org (172.22.200.11)' can't be established.
ED25519 key fingerprint is SHA256:aQ+Q4ELkyFWnqh88hcFvHIOKi4wUqsZqlyYCUhZ4kBI.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'gitlab.mygitlab.mystical.org' (ED25519) to the list of known hosts.
git@gitlab.mygitlab.mystical.org: Permission denied (publickey,keyboard-interactive).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

# 在客户端创建ssh
[root@master2 ~]$ ssh-keygen 
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Created directory '/root/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa
Your public key has been saved in /root/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:Ji2Lu3jg32JOYaxx1qbswtyYceLwYpeHXCwTt9MvGe4 root@master2.mystical.org
The key's randomart image is:
+---[RSA 3072]----+
|                 |
|                 |
|                 |
|   o o .         |
|  . X B S        |
|. +X.X B         |
| BoO@ + +        |
|..XO=+ + .       |
|..o*BooE.        |
+----[SHA256]-----+

# 输出公钥
[root@master2 ~]$ cat .ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDXFnbc/E3Hqp/slmeUIVUgkK/gyxFA0Gv5+bVa4h7qHPcYBmuR+ycza7y9Gu9KTqAWVI/1x5ihFODYmU7HxFu/L6FEbWSRidnwTChGZgfdVMR315zUmgSVahvi1QldRVZkvGe2t4p+xjkYtH78nKrd8ptkk/+FbYCTZjSN+0ThcVfSuPaY8U5xcLbPjMSYCqLuoTh3fvx/jAXDWASgohCmnmVyypdl/SHV2Wwo7bKKm17TYlviBmiZsXstAVP0kFd9t4lbAge2zGQF6rGpNTsSBORPg9JYK0J8TwKhx/3AxJUjBb5kz/IE7y72T30iyOO/J2Psy9l60eCH54xXHSDPBkZZIvR4YX6e97JE4SCglEtj7VitfWdTNV9qAL/BhbpQi5K9i34b6JjXnsbTTgiBPe+BxbjH3F29sbb0ViGNcTh/TITYshQdCy/i45SYjIF6Vs43EtEOO7DOLD1Vho74M7cvE+/o42oOmmkttqdZ19bu92ALeyEUeJQl+g6kEC0= root@master2.mystical.org

# 公钥贴在gitlab上，如下图
```

![image-20250212114256453](D:\git_repository\cyber_security_learning\markdown_img\image-20250212114256453.png)

![image-20250212114318304](D:\git_repository\cyber_security_learning\markdown_img\image-20250212114318304.png)

![image-20250212114345172](D:\git_repository\cyber_security_learning\markdown_img\image-20250212114345172.png)

![image-20250212114429246](D:\git_repository\cyber_security_learning\markdown_img\image-20250212114429246.png)

上传成功后，再在客户端clone仓库

```bash
# 成功将仓库clone了下来
[root@master2 ~/project]# git clone git@gitlab.mygitlab.mystical.org:devops/m62-hw.git
Cloning into 'm62-hw'...
warning: You appear to have cloned an empty repository.

# 查看
[root@master2 ~/project]# ls
m62-hw

# 配置这个项目的本地git身份
[root@master2 ~/project]# cd m62-hw
[root@master2 ~/project/m62-hw]# git config --local user.name Zhangyifeng
[root@master2 ~/project/m62-hw]# git config --local user.email "15104600741@163.com"

# 查看
[root@master2 ~/project/m62-hw]# git config --local --list
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=git@gitlab.mygitlab.mystical.org:devops/m62-hw.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
user.name=Zhangyifeng
user.email=15104600741@163.com

# 这里因为上述创建仓库，取消了仓库初始化，所以这里必须手动创建一个主分支
# clone的是未初始化的仓库的标志：warning: You appear to have cloned an empty repository

# 创建主分支
[root@master2 ~/project/m62-hw]# git switch --create main
Switched to a new branch 'main'

# 生成一个空文件，进行一次提交，将其推送到远程仓库
[root@master2 ~/project/m62-hw]# touch README.md
[root@master2 ~/project/m62-hw]# git add README.md 
[root@master2 ~/project/m62-hw]# git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   README.md

[root@master2 ~/project/m62-hw]# git commit -m'add README'
[main (root-commit) 06af66e] add README
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
 
# 方法1：这里提交文件到远程仓库
[root@master2 ~/project/m62-hw]# git push origin main 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 216 bytes | 216.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To gitlab.mygitlab.mystical.org:devops/m62-hw.git
 * [new branch]      main -> main

# 方法2：
# 在 git push --set-upstream origin main 中，--set-upstream（简写为 -u）的作用是 将本地分支与远程分支关联，这样以后可以直接使用 git push 和 git pull，而不必每次都指定远程仓库和分支名称。

[root@master2 ~/project/m62-hw]# git push --set-upstream origin main

# 后续再推送，和拉取可以直接使用git push 和 git pull, 否则每次要指定上传的仓库和分支，例如：git push origin main

# 刷新浏览器上的仓库，即可看到上传的文件
```

![image-20250212120213189](D:\git_repository\cyber_security_learning\markdown_img\image-20250212120213189.png)



#### 导入项目

新版需要开启导入旧项目到Gitlab功能才支持导入

![image-20250212120859168](D:\git_repository\cyber_security_learning\markdown_img\image-20250212120859168.png)

![image-20250212120912148](D:\git_repository\cyber_security_learning\markdown_img\image-20250212120912148.png)

![image-20250212134808015](D:\git_repository\cyber_security_learning\markdown_img\image-20250212134808015.png)

**向下拉，选择settings ---> General**

![image-20250212134859628](D:\git_repository\cyber_security_learning\markdown_img\image-20250212134859628.png)

![image-20250212134939323](D:\git_repository\cyber_security_learning\markdown_img\image-20250212134939323.png)

![image-20250212135031102](D:\git_repository\cyber_security_learning\markdown_img\image-20250212135031102.png)



**导入功能开启后，开始导入项目**

![image-20250212135140410](D:\git_repository\cyber_security_learning\markdown_img\image-20250212135140410.png)![image-20250212135156796](D:\git_repository\cyber_security_learning\markdown_img\image-20250212135156796.png)

![image-20250212135522664](D:\git_repository\cyber_security_learning\markdown_img\image-20250212135522664.png)

**等待一小会儿，导入成功后**

![image-20250212135704796](D:\git_repository\cyber_security_learning\markdown_img\image-20250212135704796.png)



#### 将用户添加到组或项目并指定角色

将用户添加到组或项目中,并指定不同的角色,可以获取不同的权限



**Gitlab用户在组里面有5种不同权限:**

- **Guest**: 可以创建issue、发表评论，不能读写版本库
- **Reporter:** 可以克隆代码，不能提交，QA、PM可以赋予这个权限
- **Developer**: 可以克隆代码、开发、提交、 push(非保护分支Protected branches)，普通开发可以 赋予这个权限
- **Maintainer**: 可以创建项目、添加tag、保护分支、添加项目成员、编辑项目，核心开发人员可以赋 予这个权限
- **Owner**: 可以设置项目访问权限Visibility Level、删除项目、迁移项目、管理组成员，开发组组长可 以赋予这个权限



##### 在组中添加用户并指定角色

**进入群组**

![image-20250212140719073](D:\git_repository\cyber_security_learning\markdown_img\image-20250212140719073.png)

![image-20250212140836588](D:\git_repository\cyber_security_learning\markdown_img\image-20250212140836588.png)

**邀请成员加入组中**

![image-20250212140935887](D:\git_repository\cyber_security_learning\markdown_img\image-20250212140935887.png)

![image-20250212141015706](D:\git_repository\cyber_security_learning\markdown_img\image-20250212141015706.png)

![image-20250212143102248](D:\git_repository\cyber_security_learning\markdown_img\image-20250212143102248.png)



#### 保护分支

默认 **master/main** 分支被保护,开发者角色无法对被保护的分支提交代码

也可以将其它分支进行保护,防止指定分支被破环

**进入你的 GitLab 项目**

![image-20250212153000705](D:\git_repository\cyber_security_learning\markdown_img\image-20250212153000705.png)

**进入 Repository 保护分支设置**

![image-20250212153031716](D:\git_repository\cyber_security_learning\markdown_img\image-20250212153031716.png)

![image-20250212153054048](D:\git_repository\cyber_security_learning\markdown_img\image-20250212153054048.png)



#### 合并分支

由于普通开发者无法直接提交代码至master分支，可以先创建其它分支如dev,再提交代码到dev分支，接下来申请将dev 分支合并至master分支。管理者收到请求,经过审核没有问题进行批准合并，最终实现 master 代码的更新。



当开发人员将代码在分支更新提交后，可以向管理员提交合并申请

```bash
# 模拟开发人员创建了一条分支，并提交代码
# 这里假设管理员创建的分支，当然开发人员在非特殊情况下，也有创建的分支的权限
[root@mystical ~/Zhangyifeng/devops/meta]# git checkout Zhangyifeng
[root@mystical ~/Zhangyifeng/devops/meta]# mkdir Zhangyifeng
[root@mystical ~/Zhangyifeng/devops/meta]# cd Zhangyifeng/
[root@mystical ~/Zhangyifeng/devops/meta/Zhangyifeng]# vim hello.sh

# 提交
[root@mystical ~/Zhangyifeng/devops/meta] $git add .
[root@mystical ~/Zhangyifeng/devops/meta] $git commit -m'add Zhangyifeng/hello'
[root@mystical ~/Zhangyifeng/devops/meta] $git push origin Zhangyifeng
```

![image-20250212154732613](D:\git_repository\cyber_security_learning\markdown_img\image-20250212154732613.png)

**点击合并申请**

![image-20250212154856668](D:\git_repository\cyber_security_learning\markdown_img\image-20250212154856668.png)

**发送成功后**

![image-20250212154923324](D:\git_repository\cyber_security_learning\markdown_img\image-20250212154923324.png)

**此时管理员的账号内，会出现合并请求**

![image-20250212155031130](D:\git_repository\cyber_security_learning\markdown_img\image-20250212155031130.png)

![image-20250212155105742](D:\git_repository\cyber_security_learning\markdown_img\image-20250212155105742.png)

**点击查看**

![image-20250212155146105](D:\git_repository\cyber_security_learning\markdown_img\image-20250212155146105.png)

**点击批准，即同意此次合并**

![image-20250212155249007](D:\git_repository\cyber_security_learning\markdown_img\image-20250212155249007.png)

**点击合并**

![image-20250212155458961](D:\git_repository\cyber_security_learning\markdown_img\image-20250212155458961.png)

**查看该项目，可以发现，代码已成功合并过来**

![image-20250212155611241](D:\git_repository\cyber_security_learning\markdown_img\image-20250212155611241.png)





### GitLab 的数据备份和恢复

数据备份和恢复官方帮助：

```http
https://docs.gitlab.com/ee/raketasks/backup_restore.html
```



#### 备份相关配置文件

```bash
/etc/gitlab/gitlab.rb
/etc/gitlab/gitlab-secrets.json #双因子验证等使用此文件
```



**备份配置文件命令**

```bash
gitlab-ctl backup-etc --backup-path <DIRECTORY>
#如果不指定--backup-path <DIRECTORY>，则默认备份至/etc/gitlab/config_backup/
```



#### 手动备份数据

不同版本的备份数据命令

```bash
# GitLab 12.2之后版本
gitlab-backup create

# GitLab 12.1之前版本
gitlab-rake gitlab:backup:create
```

备份相关配置

```bash
#默认在/etc/gitlab/gitlab.rb文件中指定备份路径，如果目录空间不足，可以修改新的目录
#注意：修改完配置需要执行gitlab-ctl reconfigure
# gitlab_rails['backup_path'] = "/var/opt/gitlab/backups"

#备份的文件权限，所有者和所属组为git
# gitlab_rails['backup_archive_permissions'] = 0644

#默认备份过期时长为7天，单位为s, 之后会被自动删除
# gitlab_rails['backup_keep_time'] = 604800
```



#### 执行恢复

恢复的前提条件

```ABAP
备份和恢复使用的版本要一致
还原相关配置文件后，执行gitlab-ctl reconfigure 
确保gitlab正在运行状态
```

新版恢复方法

```bash
#恢复前先停止两个服务
[root@ubuntu1804 ~]#gitlab-ctl stop puma
[root@ubuntu1804 ~]#gitlab-ctl stop sidekiq

#恢复时指定备份文件的时间部分，不需要指定文件的全名
[root@ubuntu1804 ~]#gitlab-backup restore BACKUP=备份文件名的时间部分_Gitlab版本

#示例
[root@ubuntu1804 ~]#gitlab-backup restore BACKUP=1583562898_2020_03_07_11.11.8
#Next, restore /etc/gitlab/gitlab-secrets.json if necessary, as previously mentioned.Reconfigure, restart and check GitLab:

[root@ubuntu1804 ~]#gitlab-ctl reconfigure
[root@ubuntu1804 ~]#gitlab-ctl restart

#后续检查可选做
[root@ubuntu1804 ~]#gitlab-rake gitlab:check SANITIZE=true
#In GitLab 13.1 and later, check database values can be decrypted especially if /etc/gitlab/gitlab-secrets.json was restored, or if a different server is the target for the restore.
[root@ubuntu1804 ~]#gitlab-rake gitlab:doctor:secrets

# 恢复成功后，将之前停止的两个服务启动
[root@ubuntu1804 ~]# gitlab-ctl start sidekiq
ok: run: sidekiq: (pid 16859) 0s
[root@ubuntu1804 ~]# gitlab-ctl start unicorn
ok: run: unicorn: (pid 16882) 1s

#或者执行下面也可以
[root@ubuntu1804 ~]# gitlab-ctl restart

# 恢复后，项目及用户信息都已还原
# 注意：可能需要等一段时间才能打开浏览器进行访问
```





### K8S 上 GitLab 的备份与恢复



#### GitLab Operator备份方法

GitLab Operator 采用 **Custom Resources (CRs)** 来管理 GitLab，而关键数据仍然存储在 **ConfigMaps、Secrets 和 Persistent Volumes (PVs)** 中。



#####  1. 备份 GitLab Operator 相关的 CRD 配置

GitLab Operator 主要使用 **GitLab Custom Resource（CR）** 来定义 GitLab 部署，因此备份这些 CR 是最重要的步骤之一

**执行以下命令，导出 GitLab Custom Resource**

```bash
[root@master1 backup]# kubectl get gitlab -n gitlab-system -o yaml > gitlab-cr-backup.yaml

# 如果你有多个 GitLab CR 实例：
kubectl get gitlab -A  # 查看所有 GitLab 实例
kubectl get gitlab <your-gitlab-instance-name> -n gitlab-system -o yaml > gitlab-cr-backup.yaml
```



**2. 备份 GitLab Operator 的 ConfigMaps 和 Secrets**

GitLab Operator 使用 K8S **ConfigMaps 和 Secrets** 来存储部分配置，如数据库、存储、认证信息等。因此，你需要分别备份它们。

**(1) 备份 ConfigMaps**

```bash
kubectl get cm -n gitlab-system -o yaml > gitlab-configmaps-backup.yaml
```

**(2) 备份 Secrets**

```bash
kubectl get secrets -n gitlab-system -o yaml > gitlab-secrets-backup.yaml
```

Secrets 里可能包含：

- GitLab 初始管理员密码
- 数据库密码
- TLS 证书



**3. 备份 GitLab 数据**

GitLab 的关键数据仍然存储在 **Persistent Volumes (PVs)**，包括

- Git 仓库（Gitaly）
- 数据库（PostgreSQL）
- Redis（缓存）
- 对象存储（MinIO 或 S3）

列出所有 GitLab 相关的 PVC：

```bash
kubectl get pvc -n gitlab-system
```

然后使用 `kubectl cp` 备份

```bash
kubectl cp gitlab-gitaly-0:/var/opt/gitlab /backup/gitlab-gitaly -n gitlab-system
kubectl cp gitlab-postgresql-0:/var/lib/postgresql /backup/gitlab-postgresql -n gitlab-system
kubectl cp gitlab-redis-master-0:/data /backup/gitlab-redis -n gitlab-system
```



**4. 备份 GitLab Operator 的 CRDs**

GitLab Operator 本身依赖 **Custom Resource Definitions（CRDs）**，在恢复环境时，你需要先恢复这些 CRD。

```bash
kubectl get crd | grep gitlab
kubectl get crd gitlabs.gitlab.com -o yaml > gitlab-crd-backup.yaml
```



**5. 使用 Velero 进行整站备份**

如果你的 GitLab 部署在 **生产环境**，建议使用 **Velero** 进行完整的 Kubernetes 资源和数据备份：

```bash
velero backup create gitlab-backup --include-namespaces gitlab-system --wait
```

恢复 GitLab

```bash
velero restore create --from-backup gitlab-backup
```

 🚀   **Velero 是最适合 Kubernetes 环境下 GitLab Operator 的完整备份和恢复方案**，适用于生产环境！ 🚀





### GitLab 迁移和升级

在生产中升级往往伴随着服务器的迁移,比如从本地机房迁移到云环境中,而实现升级

#### 迁移流程

- 在原 GitLab 主机上备份配置文件和数据
- 在目标主机上安装相同的版本的 GitLab 软件
- 还原配置和数据
- 本质上就是备份和恢复的过程



#### 升级流程

- 如果新主机，需要先安装原版本，并还原配置和数据
- 不能直接跳过中间的版本直接升级,选择最近的大版本进行升级
  - 比如:12.1想升级到13.0,先升级到12.X最高版,再升级到13.0.
- 下载新版本的安装包,直接安装包
- 安装包时可能会提示出错,原因是版本升级后有些配置项会过时,根据提示修改配置即可
- 重新配置: gitlab-ctl reconfigure
- 重启服务: gitlab-ctl restart



### 实现 Https

GitLab 如果用于不安全的网络，建议使用 https

```ABAP
注意：建议使用权威CA颁发的证书，自签名的证书需要加入信任,否则会导致后续git clone等操作失败
```

官方说明

```http
https://docs.gitlab.com/omnibus/settings/nginx.html#enable-https
```



#### 创建证书

```bash
[root@gitlab ~]# mkdir -p /etc/gitlab/ssl && cd /etc/gitlab/ssl
[root@gitlab ssl]# openssl genrsa -out gitlab.wang.org.key 2048
[root@gitlab ssl]# openssl req -days 3650 -x509 \
-sha256 -nodes -newkey rsa:2048 -subj "/C=CN/ST=beijing/L=beijing/O=wang/CN=gitlab.wang.org" -keyout gitlab.wang.org.key -out gitlab.wang.org.crt
```



#### 修改配置文件

```bash
[root@gitlab ~]# vim /etc/gitlab/gitlab.rb
external_url "https://gitlab.wang.org" #此项必须修改为https，必选项
nginx['enable'] = true  #可选
nginx['client_max_body_size'] = '1000m' #可选
nginx['redirect_http_to_https'] = true  #必选项，默认值为false，修改为true，实现http自动301跳转至https
nginx['redirect_http_to_https_port'] = 80 #可选,所有请求80的都跳转到443，默认值，可不改，保持注释状态
nginx['ssl_certificate'] ="/etc/gitlab/ssl/gitlab.wang.org.crt"   #必选项
nginx['ssl_certificate_key'] ="/etc/gitlab/ssl/gitlab.wang.org.key"   #必选项
nginx['ssl_ciphers'] = "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256" #可选
nginx['ssl_prefer_server_ciphers'] = "on"  #可选
nginx['ssl_protocols'] = "TLSv1.2"    #可选
nginx['ssl_session_cache'] = "shared:SSL:10m"   #可选
nginx['ssl_session_timeout'] = "1440m"    #可选
```



#### 重新初始化

```bash
[root@gitlab ~]# gitlab-ctl reconfigure
[root@gitlab ~]# gitlab-ctl restart
[root@gitlab ~]# gitlab-ctl status

#还登录原来的URL,会自动跳转到 https
```



#### 解决自签名证书的信任问题

```bash
# 在git的客户端主机上信任该证书
[root@ubuntu2204 ~]# scp gitlab-server:/etc/gitlab/ssl/gitlab.wang.org.crt

# 将证书加入信任文件
# Ubuntu
[root@ubuntu2204 ~]# cat gitlab.wang.org.crt >> /etc/ssl/certs/ca-certificate.crt

# Rocky
[root@rocky8 ~]# cat gitlab.wang.org.crt >> /etc/pki/tls/certs/ca-bundle.crt
```



### GitLab 忘记密码解决方案

官方说明

```http
https://docs.gitlab.com/ee/security/reset_user_password.html#reset-the-root-password
```



#### 进入数据库

```bash
[root@gitlab ~]#gitlab-rails console -e production

# 此步可能比较慢,需要等一段时间
--------------------------------------------------------------------------------
 Ruby:         ruby 2.7.5p203 (2021-11-24 revision f69aeb8314) [x86_64-linux]
 GitLab:       15.1.2 (ea7455c8292) FOSS
 GitLab Shell: 14.7.4
 PostgreSQL:   13.6
------------------------------------------------------------[ booted in 23.59s ]
Loading production environment (Rails 6.1.4.7)

# 找到root用户
# 方法1
irb(main):001:0> user = User.find_by_username 'root'
# 方法2
irb(main):001:0> user = User.where(id: 1).first
=> #<User id:1 @root>

# 重设密码
irb(main):002:0> user.password="wang@123"
=> "wang@123"
irb(main):003:0> user.password_confirmation="wang@123"
=> "wang@123"

# 保存
irb(main):004:0> user.save
=> true

# 退出控制台
irb(main):005:0> quit

#验证用新密码登录
```





## DevOps 之 CICD 服务器 Jenkins



- **Jenkins 介绍**
- **Jenkins 部署**
- **Jenkins 基本配置**
- **Jenkins 实现 CICD**
- **Jenkins 分布式**
- **Jenkins 流水线 Pipeline**
- **代码质量检测 SonarQube**



###  Jenkins 部署与基本配置

####  Jenkins 介绍

![image-20250212201154944](D:\git_repository\cyber_security_learning\markdown_img\image-20250212201154944.png)

官方文档

```http
https://www.jenkins.io/zh/doc/
```

Jenkins 是基于 **Java 开发**的一种开源的CI（Continuous integration持续集成）&CD (Continuous  Delivery持续交付，Continuous Deployment持续部署)工具

Jenkins 用于监控持续重复的工作，旨在提供一个开放易用的软件平台，使软件的持续集成变成可能。可用于自动化各种任务，如构建，测试和部署软件。

Jenkins 作为一个可扩展的自动化服务器，可以用作简单的 CI 服务器，或者变成任何项目的持续交付中 心。

Jenkins 只是一个调度平台,其本身并不能完成项目的构建部署

Jenkins **需要安装各种插件**,可能还需要编写Shell,python脚本等才能调用和集成众多的组件来实现复杂的构建部署功能

![image-20250212201712573](D:\git_repository\cyber_security_learning\markdown_img\image-20250212201712573.png)



**主要用途**

- 持续、自动地构建/测试软件项目
- 监控一些定时执行的任务

**Jenkins特点**

- 开源免费
- 跨平台，支持所有的平台
- master/slave支持分布式的build
- web形式的可视化的管理页面
- 安装配置简单
- 及时快速的提示和帮助
- 已有的1800+插件



**Jenkins官方介绍视频**

```http
https://v.qq.com/x/page/m0509xul0xk.html
```





### Jenkins 安装和启动

**Jenkins 的安装**

Jenkins 支持多种部署和运行方式

- 包安装
- JAVA 的 WAR 文件
- 容器运行

```http
https://www.jenkins.io/zh/doc/book/installing/
```





#### 安装前环境准备

**系统要求**

```http
https://www.jenkins.io/doc/administration/requirements/java/
```

最低推荐配置

- 256MB可用内存
- 1GB可用磁盘空间(作为一个Docker容器运行jenkins的话推荐10GB)

为小团队推荐的硬件配置

-  1GB+可用内存
- 50 GB+ 可用磁盘空间

JAVA 软件配置

- Java 8—无论是Java运行时环境（JRE）还是Java开发工具包（JDK）都可以
- Jenkins requires Java 11 or 17 since Jenkins 2.357 and LTS 2.361.1. 



**系统准备**

```bash
#关闭防火墙和SELinux
#设置语言环境，防止后期Jenkins汉化出问题
[root@jenkins ~]# localectl set-locale LANG=en_US.UTF-8
```



**Java 环境**

```http
https://www.jenkins.io/doc/book/platform-information/support-policy-java/
```

jenkins基于JAVA实现，安装jenkins前需要先安装 JDK

```bash
#安装openjdk
#新版要求安装JDK-11版
[root@ubuntu2004 ~]#apt update && apt -y install openjdk-11-jdk
[root@rocky8 ~]#yum -y install java-11-openjdk

#旧版安装JDK-8版
[root@ubuntu1804 ~]#apt update
[root@ubuntu1804 ~]#apt -y install openjdk-8-jdk
```



#### Jenkins 包安装

注意：新版jenkins_2.401.2启动很慢，可能需要20分钟才能启动成功

##### 二进制包安装 Jenkins

```http
https://mirrors.tuna.tsinghua.edu.cn/jenkins/debian-stable/
```

![image-20250216154954145](D:\git_repository\cyber_security_learning\markdown_img\image-20250216154954145.png)

安装过程

```bash
# 下载java17, Jenkins 2.492.1 版本需要 Java 17 或 21
# 选择版本下载并安装
[root@mystical /var/lib]# apt install -y openjdk-17-jdk

# 下载并安装jenkins_2.492.1_all.deb
[root@mystical ~]# wget https://mirrors.tuna.tsinghua.edu.cn/jenkins/debian-stable/jenkins_2.492.1_all.deb
[root@mystical ~]# dpkg -i jenkins_2.492.1_all.deb
```



#### 基于 Kubernetes 部署 Jenkins

##### **基于 Storage Class 实现持久化**

需要部署名称为sc-nfs的Storage class 和 提供loadBalancer的服务，如OpenELB

```yaml
[root@master1 jenkins] # cat jenkins-deployment-service-pvc-sc-rabc.yaml 
apiVersion: v1
kind: Namespace
metadata:
  name: jenkins
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: jenkins-pvc
  namespace: jenkins
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: sc-nfs
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: jenkins-master
  namespace: jenkins
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: jenkins-master
rules:
  - apiGroups: ["extensions", "apps"]
    resources: ["deployments"]
    verbs: ["create", "delete", "get", "list", "watch", "patch", "update"]
  - apiGroups: [""]
    resources: ["services"]
    verbs: ["create", "delete", "get", "list", "watch", "patch", "update"]
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["create","delete","get","list","patch","update","watch"]
  - apiGroups: [""]
    resources: ["pods/exec"]
    verbs: ["create","delete","get","list","patch","update","watch"]
  - apiGroups: [""]
    resources: ["pods/log"]
    verbs: ["get","list","watch"]
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: jenkins-master
roleRef:
  kind: ClusterRole
  name: jenkins-master
  apiGroup: rbac.authorization.k8s.io
subjects:
- kind: ServiceAccount
  name: jenkins-master
  namespace: jenkins
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jenkins
  namespace: jenkins
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jenkins
  template:
    metadata:
      labels:
        app: jenkins
    spec:
      serviceAccountName: jenkins-master
      containers:
      - name: jenkins
        image: jenkins/jenkins:lts
        ports:
        - containerPort: 8080
          name: web
          protocol: TCP
        - containerPort: 50000
          name: agent
          protocol: TCP
        volumeMounts:
        - name: jenkins-volume
          mountPath: /var/jenkins_home
      volumes:
      - name: jenkins-volume
        persistentVolumeClaim:
          claimName: jenkins-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: jenkins
  namespace: jenkins
spec:
  type: LoadBalancer
  ports:
  - name: http
    port: 8080
    targetPort: 8080
  - name: agent
    port: 50000
    targetPort: 50000
  selector:
    app: jenkins
```

**启动应用**

```bash
[root@master1 jenkins]#kubectl apply -f jenkins-deployment-service-pvc-sc-rabc.yaml 
namespace/jenkins unchanged
persistentvolumeclaim/jenkins-pvc unchanged
serviceaccount/jenkins-master unchanged
clusterrole.rbac.authorization.k8s.io/jenkins-master unchanged
clusterrolebinding.rbac.authorization.k8s.io/jenkins-master unchanged
deployment.apps/jenkins created
service/jenkins unchanged

# 查看
[root@master1 jenkins]#kubectl get all -n jenkins 
NAME                           READY   STATUS    RESTARTS   AGE
pod/jenkins-5dd956745f-vmdjc   1/1     Running   0          88s

NAME              TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                          AGE
service/jenkins   LoadBalancer   10.103.70.150   172.22.200.12   8080:32367/TCP,50000:31193/TCP   2m38s

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/jenkins   1/1     1            1           88s

NAME                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/jenkins-5dd956745f   1         1         1       88s

# 访问 172.22.200.12:8080
```



#### 首次登录 Jenkins页面初始化

用浏览器访问： http://jenkins.mystical.org:8080/

默认内置用户admin，其密码为随机字符，可以从如下文件中查到密码

![image-20250212211710297](D:\git_repository\cyber_security_learning\markdown_img\image-20250212211710297.png)

```bash
# 查看密码
[root@master1 jenkins]#kubectl exec -it -n jenkins jenkins-5dd956745f-vmdjc -- /bin/bash
jenkins@jenkins-5dd956745f-vmdjc:~/secrets$ cd /var/jenkins_home/secrets/
jenkins@jenkins-5dd956745f-vmdjc:~/secrets$ cat initialAdminPassword 
8a5e445090f1412a89f857831a2258ae
```



**离线状态**

![image-20250216142300508](D:\git_repository\cyber_security_learning\markdown_img\image-20250216142300508.png)

如果显示 jenkins 已离线 ，将`/var/lib/jenkins/hudson.model.UpdateCenter.xm`l文件中的更新检 查地址改成国内镜像地址,如清华大学地址，然后重启 jenkins 即可：

```http
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
https://mirrors.aliyun.com/jenkins/updates/update-center.json
https://jenkins-zh.gitee.io/update-center-mirror/tsinghua/update-center.json
```

**示例：解决离线问题**

```bash
[root@ubuntu1804 ~]#vim /var/lib/jenkins/hudson.model.UpdateCenter.xml
<?xml version='1.1' encoding='UTF-8'?>
<sites>
 <site>
   <id>default</id>
#修改此行为下面行 <url>https://updates.jenkins.io/update-center.json</url>
   <url>https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json</url>
 </site>
</sites>
```

**选择安装 Jenkins 插件**

![image-20250212212328405](D:\git_repository\cyber_security_learning\markdown_img\image-20250212212328405.png)

![image-20250212214309954](D:\git_repository\cyber_security_learning\markdown_img\image-20250212214309954.png)

**建议选择无**

![image-20250212214434396](D:\git_repository\cyber_security_learning\markdown_img\image-20250212214434396.png)

为了解决插件安装慢的解决方式 ，利用清华的jenkins源通过 Nginx 进行 rewrite 或者反向代理，如下：

```bash
#此方式只支持http
#在jenkins服务器上修改/etc/hosts 指向新安装的nginx服务器：10.0.0.102
[root@jenkins-ubuntu ~]#vim /etc/hosts
10.0.0.102 updates.jenkins-ci.org updates.jenkins.io

#在另一台主机安装nginx，并修改配置
[root@ubuntu1804 ~]#apt -y install nginx
[root@ubuntu1804 ~]#vim /etc/nginx/sites-enabled/default

#加下面行
location /download/plugins {
    proxy_set_header Host mirrors.tuna.tsinghua.edu.cn;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    rewrite /download/plugins(.*) /jenkins/plugins/$1 break;
    proxy_pass http://mirrors.tuna.tsinghua.edu.cn;
}
[root@ubuntu1804 ~]#systemctl restart nginx
```



#### 创建 Jenkins 管理员(可选)

用户信息保存在下面目录

```bash
[root@jenkins ~]#ls /var/lib/jenkins/users/
```

系统默认有一个管理员帐号admin,继续即可

![image-20250216145627814](D:\git_repository\cyber_security_learning\markdown_img\image-20250216145627814.png)



#### 配置 Jenkins URL

保存完成即可

![image-20250216145654161](D:\git_repository\cyber_security_learning\markdown_img\image-20250216145654161.png)

![image-20250216145826296](D:\git_repository\cyber_security_learning\markdown_img\image-20250216145826296.png)

![image-20250216145845607](D:\git_repository\cyber_security_learning\markdown_img\image-20250216145845607.png)





### Jenkins 基础配置

#### 修改管理员密码

登录后需要立即修改密码

![image-20250216165009188](D:\git_repository\cyber_security_learning\markdown_img\image-20250216165009188.png)



![image-20250216165123246](D:\git_repository\cyber_security_learning\markdown_img\image-20250216165123246.png)



####  Jenkins 管理工具

```http
https://www.jenkins.io/doc/book/managing/cli/
```

Jenkins 指供了Web 管理界面,也提供了命令行管理工具

![image-20250216165620201](D:\git_repository\cyber_security_learning\markdown_img\image-20250216165620201.png)

![image-20250216165930874](D:\git_repository\cyber_security_learning\markdown_img\image-20250216165930874.png)

![image-20250216170009582](D:\git_repository\cyber_security_learning\markdown_img\image-20250216170009582.png)



```bash
[root@mystical ~]# wget http://10.0.0.222:8080/jnlpJars/jenkins-cli.jar
--2025-02-16 08:55:05--  http://10.0.0.222:8080/jnlpJars/jenkins-cli.jar
Connecting to 10.0.0.222:8080... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3712826 (3.5M) [application/java-archive]
Saving to: ‘jenkins-cli.jar’

jenkins-cli.jar            100%[=======================================>]   3.54M  --.-KB/s    in 0.02s   

2025-02-16 08:55:05 (171 MB/s) - ‘jenkins-cli.jar’ saved [3712826/3712826]

# 查看用法和命令
[root@mystical ~]# java -jar jenkins-cli.jar -s http://admin:123456@10.0.0.222:8080/ -webSocket help

# 列出任务
[root@mystical ~]# java -jar jenkins-cli.jar -s http://admin:123456@10.0.0.222:8080/ -webSocket list-jobs

# 重启jenkins
[root@mystical ~]# java -jar jenkins-cli.jar -s http://admin:123456@10.0.0.222:8080/ -webSocket restart

# 列出插件
[root@mystical ~]# java -jar jenkins-cli.jar -s http://admin:Zyf646130..@10.0.0.222:8080/ -webSocket list-plugins
```



#### Jenkins 插件管理及安装

jenkins 本身的功能有限,但是插件丰富,大大扩展了jenkins的功能,当前已有1800+的插件.

要想使用jenkins实现生产需求,就必须安装相应的插件才能实现特定的功能

```http
https://plugins.jenkins.io/
```

![image-20250216173831151](D:\git_repository\cyber_security_learning\markdown_img\image-20250216173831151.png)



##### 插件安装目录

```bash
[root@mystical ~]# ls /var/lib/jenkins/plugins/
bouncycastle-api      instance-identity.jpi     javax-mail-api        localization-support.jpi
bouncycastle-api.jpi  javax-activation-api      javax-mail-api.jpi    localization-zh-cn
instance-identity     javax-activation-api.jpi  localization-support  localization-zh-cn.jpi
......
```



##### 插件管理

插件安装过程中，如果因为某种原因导致有安装失败的插件，没有关系，可以后期再单独安装



##### 安装中文插件

![image-20250216174401400](D:\git_repository\cyber_security_learning\markdown_img\image-20250216174401400.png)

![image-20250216174436831](D:\git_repository\cyber_security_learning\markdown_img\image-20250216174436831.png)

![image-20250216174522245](D:\git_repository\cyber_security_learning\markdown_img\image-20250216174522245.png)

![image-20250216174550469](D:\git_repository\cyber_security_learning\markdown_img\image-20250216174550469.png)



中文插件安装完后，重启服务

![image-20250216175013165](D:\git_repository\cyber_security_learning\markdown_img\image-20250216175013165.png)

![image-20250216174752117](D:\git_repository\cyber_security_learning\markdown_img\image-20250216174752117.png)





#### Jenkins 优化配置

通过优化配置,可以提高后续的效率,此为可选内容



##### ssh 优化

Jenkins 服务器做为一个CICD工具,后续会经常使用 ssh 协议连接远程主机,为方便连接,建议修改自动信 任远程主机,避免首次连接的人为输入yes的确认过程

**方法1**：注意:需要安装Git或者Gitlab插件才能配置

![image-20250216180547019](D:\git_repository\cyber_security_learning\markdown_img\image-20250216180547019.png)

![image-20250216175858108](D:\git_repository\cyber_security_learning\markdown_img\image-20250216175858108.png)

![image-20250216175929485](D:\git_repository\cyber_security_learning\markdown_img\image-20250216175929485.png)

![image-20250216180705878](D:\git_repository\cyber_security_learning\markdown_img\image-20250216180705878.png)

**方法2**：在 Jenkins 服务器修改 ssh的客户端配置文件

```bash
[root@jenkins ~]#vi /etc/ssh/ssh_config
 # StrictHostKeyChecking ask #修改此行如下面
   StrictHostKeyChecking no
 #修改客户端配置无需重启ssh服务
```



##### 性能优化

默认只能并行2个任务,建议根据CPU核心数,将执行器数量修改为CPU的核数

![image-20250216180950089](D:\git_repository\cyber_security_learning\markdown_img\image-20250216180950089.png)

![image-20250216181152343](D:\git_repository\cyber_security_learning\markdown_img\image-20250216181152343.png)

![image-20250216181230865](D:\git_repository\cyber_security_learning\markdown_img\image-20250216181230865.png)





#### Jenkins 的备份还原

Jenkins的相关数据都是放在主目录中, 将主目录备份即可实现Jenkins的备份,必要时用于还原

另外如果有相关脚本等,也需要进行备份

可以如下查看目录位置

![image-20250216181459569](D:\git_repository\cyber_security_learning\markdown_img\image-20250216181459569.png)

![image-20250216181524386](D:\git_repository\cyber_security_learning\markdown_img\image-20250216181524386.png)

jenkins 主目录包含以下文件和目录

```bash
*.xml                     # 需要备份
config-history            # 需要备份
fingerprints              # 需要备份
global-build-stats        # 需要备份
*.key*                    # 需要备份
jobs                      # jobs配置需要备份（config.xml, nextBuildNumber）, builds目录, builds目录（build logs                               等）根据需求而定
nodes                     # 需要备份
plugins                   # 需要备份 *.jpi及 *.hpi，可以不备份每个插件子目录，jenkins启动后会更新插件子目录
secrets                   # 需要备份
updates                   # 需要备份
userContent               # 用户上传内容，可以根据需要备份
users                     # 用户缓存信息，最好备份
logs                      # 插件logs，根据需要而定，可以不备份
monitoring                # 可以不备份，插件会实时生成监控数据
```



#### 找回忘记的密码

```bash
# 停止服务
[root@mystical ~]# systemctl stop jenkins

# 删除jenkins主目录中config.xml的如下内容
###########################################################

<useSecurity>true</useSecurity>
  <authorizationStrategy class="hudson.security.FullControlOnceLoggedInAuthorizationStrategy">
    <denyAnonymousReadAccess>true</denyAnonymousReadAccess>
  </authorizationStrategy>
  <securityRealm class="hudson.security.HudsonPrivateSecurityRealm">
    <disableSignup>true</disableSignup>
    <enableCaptcha>false</enableCaptcha>
  </securityRealm>

#################################################################
...

# 重启Jenkins
 systemctl start jenkins

#重新无需验证即可登录，修改安全配置为Jenkins's own user database(Jenkins专有用户数据库),保存后
```

![image-20250216182639752](D:\git_repository\cyber_security_learning\markdown_img\image-20250216182639752.png)

![image-20250216182713874](D:\git_repository\cyber_security_learning\markdown_img\image-20250216182713874.png)

![image-20250216182729955](D:\git_repository\cyber_security_learning\markdown_img\image-20250216182729955.png)

![image-20250216182817594](D:\git_repository\cyber_security_learning\markdown_img\image-20250216182817594.png)

系统管理”,发现此时出现“管理用户”

![image-20250216182946287](D:\git_repository\cyber_security_learning\markdown_img\image-20250216182946287.png)

![image-20250216183028939](D:\git_repository\cyber_security_learning\markdown_img\image-20250216183028939.png)

![image-20250216183059288](D:\git_repository\cyber_security_learning\markdown_img\image-20250216183059288.png)

![image-20250216183117733](D:\git_repository\cyber_security_learning\markdown_img\image-20250216183117733.png)

系统管理--- 全局安全配置 --- 授权策略 

将任何用户可以做任何事(没有任何限制) 修改为登录用户可以做任何事

![image-20250216183255050](D:\git_repository\cyber_security_learning\markdown_img\image-20250216183255050.png)





### Jenkins 实现 CICD



#### Jenkins 实现 CICD 说明

任务中构建将程序源码转换成一个可用的目标Target的过程，该过程可能会包括获取下载源码、解决依赖、编译和打包等环节

目标可以包括库、可执行文件及生成的脚本等，该类文件即是所谓的“制品”,它们通常应该存储于制品库,**Nexus就是著名的制品库服务**

程序员可以在本地进行构建，但基于有标准、统一构建环境的构建系统完成应用程序的构建，能有效确保制品质量

Jenkins虽然可以为构建服务器，但自身并未提供构建工具

Jenkins可以集成用户所需要的大部分主流构建工具来实现完整的构建过程

构建工具与源程序的编程语言及工程工具有密切关系,因而,在Jenkins服务器中具体需要安装和集成的构 建工具,取决于用户的实际需要

- Maven: Java
- Go:  Golang
- Gradle:  Java,Groovey和Kotlin等
- SBT: Scala
- Babel、Browserify、Weboack、Grunt及Gulp等: javascript



**Jenkins 架构**

![image-20250217104707079](D:\git_repository\cyber_security_learning\markdown_img\image-20250217104707079.png)

Jenkins根据业务场景的不同,提供了多种风格的任务，默认是自由风格任务，通过安装插件，还可以支持其它风格的插件



**Job 的风格分类**

- **自由风格freestyle**：支持实现各种开发语言的不同场景的风格，以Shell为主要技术，内部有各种灵活的配置属性，默认只有此类型

- **流水线 pipeline**：重点掌握的风格，使用专用语法
- **Maven 项目**：仅适用于 JAVA 项目





#### 创建 Freestyle 风格的任务 Job

##### Freestyle 风格任务说明

![image-20250217104958777](D:\git_repository\cyber_security_learning\markdown_img\image-20250217104958777.png)



自由风格的任务提供了下面的组成

- **通用配置**：当前任务的基本配置，历史记录、存储数据、认证、存储目录等

- **源码管理**：指定当前任务依赖的代码仓库地址(仓库的分支)
- **构建触发器**：在什么情况下，才会自动执行当前的任务
- **构建环境**：构建过程中，依赖的环境变量等
- **构建**：当前的代码构建操作，实现CICD核心步骤
- **构建后动作**：构建任务成功后，我们可以做的事情，发送邮件、提交代码标签、触发其他任务、等等



**构建状态**

```http
晴雨表主要是针对一个任务的整体执行成功比例来算的。80%成功表示太阳。
```

![image-20250217105645560](D:\git_repository\cyber_security_learning\markdown_img\image-20250217105645560.png)



##### 实现一个简单的 Freestyle 任务

注意：默认使用sh 的shell类型，可以使用#!/bin/bash 声明使用bash 的shell

![image-20250217110008874](D:\git_repository\cyber_security_learning\markdown_img\image-20250217110008874.png)



![image-20250217110057327](D:\git_repository\cyber_security_learning\markdown_img\image-20250217110057327.png)

![image-20250217110203690](D:\git_repository\cyber_security_learning\markdown_img\image-20250217110203690.png)

注意：默认 Freestyle 任务的Shell 使用 /bin/sh ，如果想使用 /bin/bash ，需要在最前面加shebang 机制

![image-20250217110438438](D:\git_repository\cyber_security_learning\markdown_img\image-20250217110438438.png)

保存后，立即构建

![image-20250217110509855](D:\git_repository\cyber_security_learning\markdown_img\image-20250217110509855.png)

查看控制台输出

![image-20250217110547061](D:\git_repository\cyber_security_learning\markdown_img\image-20250217110547061.png)

![返回首页](D:\git_repository\cyber_security_learning\markdown_img\image-20250217110620009.png)

返回首页，可以看到构建任务的晴雨表

![image-20250217110734652](D:\git_repository\cyber_security_learning\markdown_img\image-20250217110734652.png)

```bash
# 查看上述任务构建的文件
[root@master1 ~]#kubectl exec -n jenkins jenkins-58df579f8c-gq72v -- cat /var/jenkins_home/workspace/freestyle-demo1/test1.txt
demo1-test
```



为方便调试，在生产环境中更多的是在服务器上创建一个指定的Jenkins脚本的文件夹，使用 `bash -x XXX.sh` 来执行脚本

```bash
# /data目录以hostPath的方式挂载到pod上
[root@node1 jenkins]#mkdir -p /data/jenkins/

[root@node1 jenkins]#cat /data/jenkins/hello.sh 
#!/bin/bash
echo "Hello, World"
```

![image-20250217121026616](D:\git_repository\cyber_security_learning\markdown_img\image-20250217121026616.png)

构建后，查看控制台输出

![image-20250217121056528](D:\git_repository\cyber_security_learning\markdown_img\image-20250217121056528.png)



#####  Jenkins 构建的环境变量

 **Jenkins 环境变量说明**

构建时，Jenkins 支持使用变量,从而增强了任务的灵活性

环境变量有**内置**和**自定义**两种

在自由风格的的shell中可以使用`${VAR_NAME}`引用变量



**Pipeline 中引用全局环境**

- Jenkins内置的全局环境变量可被所有的pipeline引用，它们以“env.”为前缀
- 在pipeline中引用全局环境变量格式有三种：
  - `${env.<ENV_VAR_NAME>} `不支持在shell 中引用
  - `$env.<ENV_VAR_NAME> `不支持在shell 中引用
  - `${ENV_VAR_NAME}`     支持在shell 中引用



**Jenkins 内置环境变量**

```ABAP
注意：Jenkins的环境变量和root用户看到环境变量不完全相同
```



**查看Jenkins内置环境变量**

```http
http://172.22.200.12:8080/env-vars.html/
```

![image-20250217112015151](D:\git_repository\cyber_security_learning\markdown_img\image-20250217112015151.png)

```http
http://172.22.200.12:8080/manage/systemInfo
```

![image-20250217112105065](D:\git_repository\cyber_security_learning\markdown_img\image-20250217112105065.png)



**自定义环境变量**

变量的优先级顺序：

```ABAP
任务中的自定义的变量 > Jenkins 的自定义环境量 > Jenkins 内置的环境变量
```

**创建环境变量**

自定义变量可以在系统管理--配置系统--全局属性-- 环境变量 定义

注意：如果自定义环境变量与内置全局环境变量同名时，内置全局环境变量将被自定义环境变量覆盖

这可能会引起错误，必要时，可为自定义环境变量使用固定的前缀，例如“_ _”等

![image-20250217113700661](D:\git_repository\cyber_security_learning\markdown_img\image-20250217113700661.png)

![image-20250217113836606](D:\git_repository\cyber_security_learning\markdown_img\image-20250217113836606.png)

在作业中使用自定义的环境变量

![image-20250217113938728](D:\git_repository\cyber_security_learning\markdown_img\image-20250217113938728.png)

构建后查看

![image-20250217114012533](D:\git_repository\cyber_security_learning\markdown_img\image-20250217114012533.png)

####  Jenkins 结合 GitLab 实现代码下载

```HTTP
https://docs.gitlab.com/ee/integration/jenkins.html
```

##### GitLab 创建项目

```http
https://gitee.com/lbtooth/wheel_of_fortune.git
```

**导入项目**

![image-20250217114404742](D:\git_repository\cyber_security_learning\markdown_img\image-20250217114404742.png)

![image-20250217140837184](D:\git_repository\cyber_security_learning\markdown_img\image-20250217140837184.png)

![image-20250217140905835](D:\git_repository\cyber_security_learning\markdown_img\image-20250217140905835.png)

![image-20250217140934187](D:\git_repository\cyber_security_learning\markdown_img\image-20250217140934187.png)



##### Jenkins 安装和 Gitlab 相关的插件

只有安装GitLab插件,才能让Jenkins和GitLab相连

在管理插件中搜索需要插件 gitlab，其它依赖的插件会自动安装

![image-20250217150558897](D:\git_repository\cyber_security_learning\markdown_img\image-20250217150558897.png)



##### Jenkins 服务器创建访问GitLab的凭据

**Jenkins 凭证概述**

凭证就是认证到某个系统中的认证信息，用于提供对受限资源的访问; 

Jenkins所支持的凭证类型如下

- 用户名和密码(Username with password)
- SSH用户名和私钥对(SSH Username with private key)
- Github App
- Secret file: 需要保密的文本文件，保存有Token等信息
- Secret text:Token,串需要保密的文本，例如Github的API Token等
- Certificate
- 其它凭证类型还有二进制数据，或者更复杂形式的项目，例如OAuth凭证等;



**凭证的作用域**决定了它可用的目标范围

- **系统**:作用于Jenkins系统自身，仅可用于系统和后台任务，且一般用于连接到agent节点之上
- **全局**:作用于Jenkins上的所有任务，以确保任务的正常执行
- **用户**:作用于用户级别，仅生效于Jenkins中的线程代表该用户进行身份验证之时

```ABAP
注意: 在Jenkins内部，凭证被存放在JENKINS_ HOME目录下的secrets目录中，请务必确保该目录的访问权限进行了正确的设置
```



**添加基于用户名和密码类型的凭据**

如果基于http协议则无需实现ssh key 凭证,而选择添加gitlab用户名和密码的形式

如下图，表示对该连接没有连接权限，因为该仓库是私有仓库，因此需要账号密码或者ssh验证才能登录

![image-20250217152720707](D:\git_repository\cyber_security_learning\markdown_img\image-20250217152720707.png)



添加用户凭证，即访问gitlab的用户密码

![image-20250217152829054](D:\git_repository\cyber_security_learning\markdown_img\image-20250217152829054.png)

![image-20250217152845398](D:\git_repository\cyber_security_learning\markdown_img\image-20250217152845398.png)

![image-20250217153045186](D:\git_repository\cyber_security_learning\markdown_img\image-20250217153045186.png)

```http
服务器如果使用http连接，一旦gitlab上配置了https，则Jenkins上需要考虑服务器证书问题，因此建议用ssh连接
```



**关于 Git 的 SSL 证书验证解决方案**

```ABAP
详情见：知识扩展 -> Git相关用法补充 -> 绕过Git的SSL证书验证方法
```



**创建基于 ssh key 的凭据**

实现jenkins服务器到gitlab服务器的基于密钥的验证，可以让jenkins连接到gitlab执行操作，比如拉取代码

```ABAP
注意：ssh key的凭据可以基于jenkins用户或任意主机的其它任何用户的公钥私钥对都可以，但都需要在gitlab将此用户的公钥public key 和在gitlab主机上与gitlab的用户进行关联，并将私钥private key在jenkins创建为SSH Username with private key类型的凭据

总结：gitlab上指定用户上传的公钥和jenkins上的凭据（私钥）匹配即可
```



 **在 Jenkins 服务器上生成 ssh key**

```bash
# 在jenkins的主机上创建公私钥对
# [root@node1 data]# ssh-keygen

# 生成公私钥对后，将公钥上传gitlab
```

![image-20250217161748213](D:\git_repository\cyber_security_learning\markdown_img\image-20250217161748213.png)

然后将私钥上传到jenkins的凭据中

**注意**：此处的 username 只是注释性功能，理论上可以随便填写，只要确保此处private key和在 gitlab上关联的公钥是一对即可

![image-20250217161823375](D:\git_repository\cyber_security_learning\markdown_img\image-20250217161823375.png)

![image-20250217162058432](D:\git_repository\cyber_security_learning\markdown_img\image-20250217162058432.png)

保存后，没有报错，即表示jenkins有权限拉去gitlab的代码

![image-20250217162144524](D:\git_repository\cyber_security_learning\markdown_img\image-20250217162144524.png)



```ABAP
如果ssh连接方法出现下面报错，是因为Jenkins以Jenkins用户身份运行，首次连接Gitlab服务器会弹出未知主机的 警告，需要添加信任
```

![image-20250217163035747](D:\git_repository\cyber_security_learning\markdown_img\image-20250217163035747.png)

**解决方法**

```ABAP
参考：DevOps之CICD服务器Jenkins -> Jenkins基础配置 -> Jenmins优化配置 -> ssh优化
```



git仓库连接成功后选择要拉取的分支

![image-20250217163550403](D:\git_repository\cyber_security_learning\markdown_img\image-20250217163550403.png)

直接保存构建，代码即可拉取到 Jenkins 服务器上

![image-20250217163705311](D:\git_repository\cyber_security_learning\markdown_img\image-20250217163705311.png)

![image-20250217163826379](D:\git_repository\cyber_security_learning\markdown_img\image-20250217163826379.png)

查看Jenkins工作目录下代码是否拉取成功

```bash
jenkins@jenkins-578dc9ccf4-nk8g4:~/workspace/freestyle-wheel-demo1# ls
images	index.html  js
```





#### 配置 Jenkins 结合 GitLab 实现自动化前端项目的部署和回滚



#####  Jenkins 创建任务

![image-20250217164331078](D:\git_repository\cyber_security_learning\markdown_img\image-20250217164331078.png)



##### 配置 Git 项目地址和凭证

![image-20250217164408642](D:\git_repository\cyber_security_learning\markdown_img\image-20250217164408642.png)

##### 准备脚本并加入构建任务

```bash
[root@node1 jenkins]#cat wheel-html-gitlab-deploy-rollback.sh 
#!/bin/bash
#
#********************************************************************
#Author:            mystical
#QQ:                29308620
#Date:              2025-02-17
#FileName:          wheel-html-gitlab-deploy-rollback.sh
#URL:               http://www.mysticalrecluse.com
#Description:       The test script
#Copyright (C):     2025 All rights reserved
#********************************************************************

HOST_LIST="
172.22.200.101
172.22.200.102
"

APP=wheel
APP_PATH=/var/www/html
DATA_PATH=/opt
DATE=$(date +%F_%H-%M-%S)

deploy() {
    for i in ${HOST_LIST}; do
        ssh root@$i "rm -rf ${APP_PATH} && mkdir -pv ${DATA_PATH}/${APP}-${DATE}"
        scp -r * root@$i:${DATA_PATH}/${APP}-${DATE}
        ssh root@$i "ln -sv ${DATA_PATH}/${APP}-${DATE} ${APP_PATH}"
    done
}

rollback() {
    for i in ${HOST_LIST}; do
        CURRENT_VERSION=$(ssh root@$i "readlink $APP_PATH")
        CURRENT_VERSION=$(basename ${CURRENT_VERSION})
        echo ${CURRENT_VERSION}
        PRE_VERSION=$(ssh root@$i "ls -l ${DATA_PATH} | grep -B1 ${CURRENT_VERSION}|head -n1")
        echo $PRE_VERSION
        PRE_VERSION=$(echo $PRE_VERSION|awk '{print $NF}')
        ssh root@$i "rm -rf ${APP_PATH} && ln -sv ${DATA_PATH}/${PRE_VERSION} ${APP_PATH}"
    done
}

case $1 in
deploy)
    deploy
    ;;
rollback)
    rollback
    ;;
*)
    exit
    ;;
esac
```

![image-20250218091936057](D:\git_repository\cyber_security_learning\markdown_img\image-20250218091936057.png)

![image-20250218091957718](D:\git_repository\cyber_security_learning\markdown_img\image-20250218091957718.png)

查看控制台输出

![image-20250218092020644](D:\git_repository\cyber_security_learning\markdown_img\image-20250218092020644.png)

##### 服务器验证数据

```bash
[root@mystical /opt]# ll
total 28
drwxr-xr-x  7 root root 4096 Feb 17 14:41 ./
drwxr-xr-x 19 root root 4096 Apr 17  2024 ../
drwxr-xr-x  2 root root 4096 Feb 17 06:48 wheel/
drwxr-xr-x  4 root root 4096 Feb 17 11:01 wheel-2025-02-17_11-01-21/
drwxr-xr-x  4 root root 4096 Feb 17 14:29 wheel-2025-02-17_14-29-20/
drwxr-xr-x  4 root root 4096 Feb 17 14:30 wheel-2025-02-17_14-30-50/
drwxr-xr-x  4 root root 4096 Feb 17 14:41 wheel-2025-02-17_14-41-47/

[root@mystical /opt] $ll /var/www/html
lrwxrwxrwx 1 root root 30 Feb 17 14:41 /var/www/html -> /opt/wheel-2025-02-17_14-41-47/
```

**访问`172.22.200.101`和`172.22.200.102`**

![image-20250218093456929](D:\git_repository\cyber_security_learning\markdown_img\image-20250218093456929.png)



##### 修改代码再上传重新构建

```bash
# 取消ssl验证
[root@mystical ~]# git config --global http.sslVerify false

# 拉取代码
[root@mystical ~]# git clone http://gitlab.mygitlab.mystical.org/devops/wheel_of_fortune.git

# 修改代码后重新上传
[root@mystical ~]# vim index.html
[root@mystical ~]# git add .
[root@mystical ~]# git commit -m'change 500w'
[root@mystical ~]# git push origin master 
```

重新执行任务，可以看到如下修改

![image-20250218100753510](D:\git_repository\cyber_security_learning\markdown_img\image-20250218100753510.png)



##### 实现版本回滚任务

新建任务如下,实现回滚功能

![image-20250218101055995](D:\git_repository\cyber_security_learning\markdown_img\image-20250218101055995.png)

只修改构建的shell部分,其它不变

![image-20250218101215004](D:\git_repository\cyber_security_learning\markdown_img\image-20250218101215004.png)

![image-20250218101232842](D:\git_repository\cyber_security_learning\markdown_img\image-20250218101232842.png)

执行任务后,可以查看到 Web页面是否还原为上一个版本

![image-20250218102553543](D:\git_repository\cyber_security_learning\markdown_img\image-20250218102553543.png)



#### 参数化构建

jenkins支持参数化构建，类似于脚本中的参数，可以实现灵活的构建任务

Jenkins 支持多种参数类型,比如:Boolean,Choice选项,字符串,Multi_line字符串,文件类型等



##### 参数类型说明

参数化构建的目标在于为流水线提供基于参数值的灵活构建机制，从而让一个流水线的定义可以适用于多种需求情形

- 其功能与引用方式与环境变量类似
- 在触发作业运行之时，需要向各参数赋值
- 参数在使用时实际上也表现为变量，可以通过变量的调用方式使用参数
- 注意: 参数化功能无需安装插件即可支持

**常用的参数类型**

![image-20250218103626204](D:\git_repository\cyber_security_learning\markdown_img\image-20250218103626204.png)



##### 创建包含各种类型参数的任务

###### 布尔值参数Boolean  Parameter

![image-20250218104051835](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104051835.png)

![image-20250218104102212](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104102212.png)

![image-20250218104113979](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104113979.png)

![image-20250218104124076](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104124076.png)

构建后，查看控制台输出

![image-20250218104159641](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104159641.png)



###### 选项参数Choice  Parameter

![image-20250218104646702](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104646702.png)

![image-20250218104700098](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104700098.png)

![image-20250218104712039](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104712039.png)

可以选择指定的参数值

![image-20250218104750056](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104750056.png)

点击Build构建后，查看控制台输出

![image-20250218104847954](D:\git_repository\cyber_security_learning\markdown_img\image-20250218104847954.png)

###### 字符参数 String Parameter

![image-20250218105208649](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105208649.png)

![image-20250218105224135](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105224135.png)



![image-20250218105244529](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105244529.png)

![image-20250218105255321](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105255321.png)

可以更改后，提交构建，查看控制台效果

![image-20250218105344473](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105344473.png)

![image-20250218105402461](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105402461.png)

###### 文本参数Multi-line String  Parameter

![image-20250218105601062](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105601062.png)

![image-20250218105615340](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105615340.png)

![image-20250218105627520](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105627520.png)

更改后，提交构建，查看控制台输出（**换行被空格替代，所有文本在一行输出**）

![image-20250218105743516](D:\git_repository\cyber_security_learning\markdown_img\image-20250218105743516.png)

**如果想要保留多行，需要将变量用双引号引起来**

![image-20250218110358635](D:\git_repository\cyber_security_learning\markdown_img\image-20250218110358635.png)

![image-20250218110419179](D:\git_repository\cyber_security_learning\markdown_img\image-20250218110419179.png)



#####  选项参数实现不同分支的部署

###### 查看当前分支

```bash
# 查看当前分支
[root@mystical ~/project/testproject]# git branch -v
  devel ef9119b add v2 devel
* main  2b25da9 create index v1

# 查看main分支日志
[root@mystical ~/project/testproject]# git log
commit 2b25da926eaaac186a7c2dbdfa339fb02cacc36d (HEAD -> main, origin/main)
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 05:05:16 2025 +0000

    create index v1

commit e092f325efc674a587453905234dd6095cc3fd88
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 03:25:56 2025 +0000

    add README

# 查看devel分支日志
[root@mystical ~/project/testproject]# git checkout devel 
Switched to branch 'devel'
[root@mystical ~/project/testproject]# git log
commit ef9119b63d267ddd0b4e2cbd4b3f92e557e9d759 (HEAD -> devel, origin/devel)
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 05:07:14 2025 +0000

    add v2 devel

commit 2b25da926eaaac186a7c2dbdfa339fb02cacc36d (origin/main, main)
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 05:05:16 2025 +0000

    create index v1

commit e092f325efc674a587453905234dd6095cc3fd88
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 03:25:56 2025 +0000

    add README
```

###### 准备构建脚本

```bash
[root@node1 jenkins]#cat deploy.sh 
#!/bin/bash
#
#********************************************************************
#Author:            mystical
#QQ:                29308620
#Date:              2025-02-18
#FileName:          deploy.sh
#URL:               http://www.mysticalrecluse.com
#Description:       The test script
#Copyright (C):     2025 All rights reserved
#********************************************************************

BRANCH=$1

ls /data/git &> /dev/null || mkdir -pv /data/git
cd /data/git && rm -rf testproject
git clone -b $BRANCH git@gitlab.mygitlab.mystical.org:devops/testproject.git
cd testproject

case $BRANCH in
main)
    scp -r * root@172.22.200.101:/var/www/html/
    ;;
devel)
    scp -r * root@172.22.200.102:/var/www/html/
    ;;
*)
    echo $BRANCH is error
    ;;
esac
```

###### 新建任务，并配置参数化构建

![image-20250218135016459](D:\git_repository\cyber_security_learning\markdown_img\image-20250218135016459.png)

![image-20250218135044179](D:\git_repository\cyber_security_learning\markdown_img\image-20250218135044179.png)

分别执行main分支和devel分支

![image-20250218135122352](D:\git_repository\cyber_security_learning\markdown_img\image-20250218135122352.png)

###### 查看效果

![image-20250218135820662](D:\git_repository\cyber_security_learning\markdown_img\image-20250218135820662.png)

![image-20250218135735134](D:\git_repository\cyber_security_learning\markdown_img\image-20250218135735134.png)

![image-20250218135754886](D:\git_repository\cyber_security_learning\markdown_img\image-20250218135754886.png)



![image-20250218135829123](D:\git_repository\cyber_security_learning\markdown_img\image-20250218135829123.png)



![image-20250218135856630](D:\git_repository\cyber_security_learning\markdown_img\image-20250218135856630.png)

#### 利用 Git Parameter 插件实现拉取指定版本

##### 创建多个tag，并同步到仓库

```bash
# 查看当前git日志
[root@mystical ~/project/wheel_of_fortune]# git log
commit a03647ff47edf0b0ca1289473ff013b057ddeeee
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 02:21:48 2025 +0000

    change 3002

commit 26551d643447ebebf0eab4a5a40905e9bab82ebc
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 02:04:56 2025 +0000

    change 500w

commit 46b0c7a08624cae2d1f96fdbf20434b1b68362cf
Author: mystical <mysticalrecluse@gmail.com>
Date:   Mon Feb 17 14:41:13 2025 +0000

    change 100w

commit 730984d25d3b79610f7cc113c5c9d1c2b340cdbb
Author: yangchao <chao.yang@bridgetek.cn>
Date:   Wed Aug 8 19:48:30 2018 +0800

# 给每个阶段打上标签
[root@mystical ~/project/wheel_of_fortune]# git tag v1.0 730984d25d3b79610
[root@mystical ~/project/wheel_of_fortune]# git tag v2.0 46b0c7a08624cae2
[root@mystical ~/project/wheel_of_fortune]# git tag v3.0 26551d643447ebeb
[root@mystical ~/project/wheel_of_fortune]# git tag v4.0 a03647ff47edf0b0c

# 同步tags到仓库
git push origin --tags
```



##### 安装 Git Parameter 插件

![image-20250218141614844](D:\git_repository\cyber_security_learning\markdown_img\image-20250218141614844.png)



##### 创建任务

![image-20250218141824687](D:\git_repository\cyber_security_learning\markdown_img\image-20250218141824687.png)

![image-20250218142143511](D:\git_repository\cyber_security_learning\markdown_img\image-20250218142143511.png)

![image-20250218142309665](D:\git_repository\cyber_security_learning\markdown_img\image-20250218142309665.png)

![image-20250218142644353](D:\git_repository\cyber_security_learning\markdown_img\image-20250218142644353.png)

![image-20250218142715442](D:\git_repository\cyber_security_learning\markdown_img\image-20250218142715442.png)

##### 选择指定tag，构建测试后观察效果

![image-20250218142804116](D:\git_repository\cyber_security_learning\markdown_img\image-20250218142804116.png)

![image-20250218142856390](D:\git_repository\cyber_security_learning\markdown_img\image-20250218142856390.png)

![image-20250218143043448](D:\git_repository\cyber_security_learning\markdown_img\image-20250218143043448.png)

![](D:\git_repository\cyber_security_learning\markdown_img\image-20250218142952407.png)





#### 实现 Java 应用源码编译并部署

java 程序需要使用构建工具,如: maven,ant,gradle等进行构建打包才能部署,其中**maven**比较流行

以下以 maven 为例实现 Java 应用部署



##### 自由风格的任务构建基于 Spring Boot 的 JAR 包部署 JAVA 项目

###### Gitlab导入项目

项目链接

```http
https://gitee.com/lbtooth/helloworld-spring-boot
```

![image-20250218144012874](D:\git_repository\cyber_security_learning\markdown_img\image-20250218144012874.png)



###### Jenkins 服务器上安装 maven 和配置镜像加速

```bash
[root@jenkins ~]#apt update && apt  -y install maven

# 配置镜像加速，全局配置
[root@mystical ~]# vim /etc/maven/settings.xml
......
    <mirror>
         <id>nexus-aliyun</id>
         <mirrorOf>*</mirrorOf>
         <name>Nexus aliyun</name>
         <url>http://maven.aliyun.com/nexus/content/groups/public</url>
    </mirror>
</mirrors>

# 也可以配置项目级别的加速
[root@mystical ~/project/helloworld-spring-boot]# vim pom.xml
##############################################
......
    <!-- 配置阿里云仓库 -->
    <repositories>
        <repository>
            <id>aliyun-repos</id>
            <url>https://maven.aliyun.com/repository/public</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>
......
###########################################
```



###### 准备相关脚本

```bash
#!/bin/bash

APP_PATH=/data/spring-boot-helloworld

HOST_LIST="
172.22.200.101
172.22.200.102
"

mvn clean package -Dmaven.test.skip=true

for host in $HOST_LIST; do
	ssh root@$host killall -9 java &> /dev/null
	scp target/helloworld-spring-boot-*-SNAPSHOT.jar root@$host:${APP_PATH}/spring-boot-helloworld.jar
	ssh root@$host "nohup java -jar ${APP_PATH}/spring-boot-helloworld.jar --server.port=8888 &>/dev/null &"&
done
```



###### 创建 Jenkins 任务

![image-20250219154044944](D:\git_repository\cyber_security_learning\markdown_img\image-20250219154044944.png)

![image-20250219154128825](D:\git_repository\cyber_security_learning\markdown_img\image-20250219154128825.png)



###### 构建并检查结果

![image-20250219160350420](D:\git_repository\cyber_security_learning\markdown_img\image-20250219160350420.png)

![image-20250219160416294](D:\git_repository\cyber_security_learning\markdown_img\image-20250219160416294.png)

![image-20250219160521103](D:\git_repository\cyber_security_learning\markdown_img\image-20250219160521103.png)

![image-20250219160540684](D:\git_repository\cyber_security_learning\markdown_img\image-20250219160540684.png)





##### Maven 风格的任务构建基于WAR包运行 Tomcat服务器 JAVA

```ABAP
注意：此项目使用JDK-11，不支持JDK-8
```









# Prometheus





# Skywalking



# 微服务



## ZooKeeper

![image-20250123173725567](D:\git_repository\cyber_security_learning\markdown_img\image-20250123173725567.png)



### Zookeeper解决的问题

- 实现了服务注册,服务发现
- 即实现了分布式服务管理



### Zookeeper的功能

- 实现了服务的**命名服务**

  - 即给每个服务取个名称进行存放，并对其进行对应的解析，解析成对应的地址，实现服务发现，服务注册

- Zookeeper内部可以看作是一个树状存储数据库

  - 在启动一个服务的时候，可以将自己的地址信息注册到Zookeeper的树状数据库中，在数据库中将每个服务的地址，端口号注册进Zookeeper(类比：pod的启动的时候会将自己的地址和端口号注册进service的endpoint中)，
    - 后续有程序需要使用这个服务，就取Zookeeper中查询即可
    - Zookeeper做注册中心，需要在java程序中配置注册中心（Zookeeper）的地址
  - 然后zookeeper给每个服务取一个名称，通过名称借助数据库解析为对应的ip地址和端口
  - 同时Zookeeper也可以存放一些状态信息
  - Zookeeper也可以做配置中心

  

#### 解决的问题

- 服务的地址端口预先不确定的情况下，如何实现服务间通讯



### 单机部署Zookeeper

#### 包安装

```bash
[root@ubuntu2204 ~]#apt list zookeeper
正在列表... 完成
zookeeper/jammy-security,jammy-updates 3.4.13-6ubuntu4.1 all

apt -y install zookeeper

# 启动zookeeper
/usr/share/zookeeper/bin/zkServer.sh start
```



#### 二进制安装

```bash
# 安装java环境
apt install -y openjdk-11-jdk
# 下载zookeeper
wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/current/apache-zookeeper-3.9.3-bin.tar.gz

# 解压并放入指定目录
tar xf apache-zookeeper-3.9.2-bin.tar.gz -C /usr/local/

# 将其放入PATH目录中
# vim /etc/profile
PATH=$PATH:/usr/local/zookeeper/bin/

# 加载
. /etc/profile

# 创建配置文件zoo.cfg
cd /usr/local/zookeeper/conf
cp zoo_sample.cfg zoo.cfg

# 启动zookeeper并查看状态
[root@ubuntu2204 conf]#zkServer.sh start
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
[root@ubuntu2204 conf]#zkServer.sh status
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: standalone  # 表示是单机模式，不是集群

# 查看zookeeper端口（2181以打开），本质上就是java程序
[root@ubuntu2204 conf]#ss -nltp
State      Recv-Q     Send-Q         Local Address:Port          Peer Address:Port    Process                                       
LISTEN     0          4096           127.0.0.53%lo:53                 0.0.0.0:*        users:(("systemd-resolve",pid=810,fd=14))    
LISTEN     0          128                  0.0.0.0:22                 0.0.0.0:*        users:(("sshd",pid=862,fd=3))                
LISTEN     0          50                         *:2181                     *:*        users:(("java",pid=16738,fd=77))             
LISTEN     0          50                         *:8080                     *:*        users:(("java",pid=16738,fd=69))             
LISTEN     0          50                         *:32785                    *:*        users:(("java",pid=16738,fd=68))             
LISTEN     0          128                     [::]:22                    [::]:*        users:(("sshd",pid=862,fd=4)) 
```



#### Zookeeper配置文件

```bash
# 可以更改配置使其暴露端口被Prometheus监控
cat /usr/local/zookeeper/conf/zoo.cfg
# The number of milliseconds of each tick
tickTime=2000  # 滴答时间，是后续时间的基本单位
# The number of ticks that the initial 
# synchronization phase can take
initLimit=10   # 因为滴答时间是2000毫秒，也就是2秒，因此这里initlimit的时间是20s
# The number of ticks that can pass between 
# sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just 
# example sakes.
dataDir=/tmp/zookeeper        # 指定数据目录，这里不建议使用tmp目录，因为tmp目录下的数据无法持久化
# the port at which the clients will connect
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
#
# Be sure to read the maintenance section of the 
# administrator guide before turning on autopurge.
#
# https://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
#
# The number of snapshots to retain in dataDir
#autopurge.snapRetainCount=3    # 只保留最近的3个版本的镜像文件
# Purge task interval in hours
# Set to "0" to disable auto purge feature
#autopurge.purgeInterval=1    # 自动数据清理

## Metrics Providers
#
# https://prometheus.io Metrics Exporter
metricsProvider.className=org.apache.zookeeper.metrics.prometheus.PrometheusMetricsProvider
metricsProvider.httpHost=0.0.0.0
metricsProvider.httpPort=7000    # 打开7000端口
metricsProvider.exportJvmInfo=true
```



**访问Prometheus指标**

```bash
curl 127.0.0.1:7000/metrics
```



#### 前台执行Zookeeper(制作镜像时使用)

```bash
zkServer.sh start-foreground
```

**注意**

```http
如果配置service，zkServer.sh和systemctl不要混用，否则无法启用
```



#### Service文件

```bash
cat > /lib/systemd/system/zookeeper.service <<EOF
[Unit]
Description=zookeeper.service
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/zookeeper/bin/zkServer.sh start
ExecStop=/usr/local/zookeeper/bin/zkServer.sh stop
ExecReload=/usr/local/zookeeper/bin/zkServer.sh restart

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload

systemctl enable --now zookeeper.service
```



### Zookeeper集群部署

- 因为选举机制，半数以上可用，所以建议奇数个节点
- Zookeeper的选举基于ZAB协议（原子广播协议）
  - Zab(Zookeeper Atomic Broadcast原子广播)：强一致性协议
- 集群中节点数越多，写性能越差，读性能越好



#### 集群角色

- 领导者(Leader)
  - 负责处理写入请求的，事务请求的唯一调度和处理者，负责进行投票发起和决议，更新系统状态

- 跟随者(Follower)
  - 接收客户请求并向客户端返回结果，在选Leader中参与投票

- 观察者(Observer)
  - 转交客户端写请求给leader节点，和同步leader状态和Follower唯一区别就是不参与Leader投票，也不参与写操作的“过半写成功”策略
  - 它的作用类似于专用于Zookeeper集群的反向代理

- 学习者(Learner)
  - 和leader进行状态同步的节点统称Learner，包括Follower和Observer

- 客户端(Client)
  - 请求发起者

#### 选举ID

- ZXID(zookeeper transaction id): 每个改变Zookeeper状态的操作都会自动生成一个对应的zxid。ZXID最大的节点优先选为Leader
  - ZXID大说明该节点的数据是最新的，ZXID可以理解为事务ID
- myid: 服务器的唯一标识(SID)，通过配置myid文件指定，集群中唯一，当ZXID一样时，myid大的节点优先选为Leader



#### 协议说明（重要）

在分布式系统中，有多种协议被设计来解决一致性问题，Paxos、Raft、ZAB等分布式算法经常会被称作是“强一致性”的分布式共识协议

**ZAB(Zookeeper Atomic Broadcast 原子广播)**

Zab协议是由Apache Zookeeper项目提出的一种原子广播协议，是为分布式协调服务Zookeeper专门设计的一种支持崩溃恢复的原子广播协议。在Zookeeper中，主要依赖ZAB协议来实现分布式数据一致性，基于该协议，Zookeeper实现了一种主备模式的系统架构来保持集群中各个副本之间的数据一致性

**Raft**

Raft是一个为分布式系统提供一致性的算法。与Paxos相比，Raft的主要目标是提供一种更加易于理解和实现的一致性算法。Raft通过选举算法确保了分布式系统中的领导者唯一性所有的写操作都通过领导者完成，这样就可以确保所有的复制节点上的数据一致性，一些知名的分布式系统，如：kafka,etcd,nacos和Consul，都采用了Raft算法



#### Zookeeper集群部署实现

```bash
# 在三台机器上安装Zookeeper

# 当所有的机器都准备好Zookeeper之后，准备配置文件
# 配置文件的最后添加
# 将路径指向指定的myid所在路径
dataDir=/usr/local/zookeeper/data
# 格式：server.MyID服务器唯一编号=服务器IP:Leader和Follower的数据同步端口(只有leader才会打开)：Leader和Follower选举端口(L和F都有)
server.1=10.0.0.131:2888:3888
server.2=10.0.0.132:2888:3888
server.3=10.0.0.133:2888:3888

# 2888是集群中节点之间数据的同步，通过2888
# 3888是选举端口

# 如果添加节点，只需要在所有节点上添加新节点的上面形式的配置行，在新节点创建myid文件，并重启所有节点服务即可

# 将配置文件同步到其他机器
scp /usr/local/zookeeper/conf/zoo.cfg 10.0.0.132:/usr/local/zookeeper/conf/
scp /usr/local/zookeeper/conf/zoo.cfg 10.0.0.133:/usr/local/zookeeper/conf/
```

**在各个节点生成ID文件**

```bash
echo 1 > /usr/local/zookeeper/data/myid
echo 2 > /usr/local/zookeeper/data/myid
echo 3 > /usr/local/zookeeper/data/myid
```

**各服务启动Zookeeper**

```bash
zkServer.sh start   # 三台机器都启动

# node1
[root@ubuntu2204 conf]#zkServer.sh status
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: follower

# node2
[root@ubuntu2204 zookeeper]#zkServer.sh status
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: leader

# node3
[root@ubuntu2204 data]#zkServer.sh status
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: follower
```



### ZooKeeper客户端访问

#### 命令行客户端访问ZooKeeper

```bash
# 使用命令行访问
# 如果不写ip:port，默认本机
zkCli.sh -server 10.0.0.131:2181

[zk: 10.0.0.132:2181(CONNECTED) 1] ls /
[zookeeper]

# 查看zookeeper集群数据
[zk: 10.0.0.132:2181(CONNECTED) 4] ls /zookeeper 
[config, quota]
[zk: 10.0.0.132:2181(CONNECTED) 5] ls /zookeeper/config 
[]
[zk: 10.0.0.132:2181(CONNECTED) 6] get /zookeeper/config 
server.1=10.0.0.131:2888:3888:participant
server.2=10.0.0.132:2888:3888:participant
server.3=10.0.0.133:2888:3888:participant
version=0

# 在zookeeper中创建子目录create,以及在文件中添加数据set
# zookeeper中，目录即是目录也是可以保存数据的文件
[zk: 10.0.0.132:2181(CONNECTED) 7] ls /
[zookeeper]
[zk: 10.0.0.132:2181(CONNECTED) 8] create /myapp1
Created /myapp1
[zk: 10.0.0.132:2181(CONNECTED) 9] ls /
[myapp1, zookeeper]
[zk: 10.0.0.132:2181(CONNECTED) 10] set /myapp1 M58
[zk: 10.0.0.132:2181(CONNECTED) 11] get /myaap1
Node does not exist: /myaap1
[zk: 10.0.0.132:2181(CONNECTED) 12] get /myapp1
M58
```



#### nc访问Zookeeper

Zookeeper支持某些特定的四字命令字母与其交互，它们大多是查询命令，用来获取ZooKeeper服务的当前状态和相关信息

**常用命令列表**

```bash
conf #输出相关服务配置的详细信息
cons #列出所有连接到服务器的客户端的完全的连接/会话的详细信息
envi #输出关于服务环境的详细信息
dump #列出未经处理的会话和临时节点
stat #查看哪个节点被选择作为Follower或者Leader
ruok #测试是否启动了该Server，若回复imok表示已经启动
mntr #输出一些运行时信息
reqs #列出未经处理的请求
wchs #列出服务器watch的简要信息
wchc #通过session列出服务器watch的详细信息
wchp #通过路径列出服务器watch的详细信息
```

**命令安全限制**

```bash
# 默认情况下，这些4字命令有可能会被拒绝，提示如下报错
xxxx is not executed because it is not in the whitelist.

#解决办法:在 zoo.cfg文件中添加如下配置,如果是集群需要在所有节点上添加下面配置
# vim conf/zoo.cfg
4lw.commands.whitelist=*

#在服务状态查看命令中有很多存在隐患的命令，为了避免生产中的安全隐患，要对这些"危险"命令进行一些安全限制，只需要编辑服务的zoo.cfg文件即可

# vim conf/zoo.cfg
4lw.commands.whitelist=conf,stat,ruok,isro
```



### 图形化客户端Zoolnspector

#### Linux客户端

**编译zooinspector**

注意：此软件因年代久远，仅支持JAVA-8，且不支持Ubuntu20.04但支持Ubuntu22.04和Rocky8

```bash
#Ubuntu22.04编译
apt update && apt -y install openjdk-8-jdk
apt update && apt -y install maven

# 添加阿里云加速
vim /etc/maven/settings.xml 
<mirrors>
   <!--阿里云镜像-->
   <mirror>
       <id>nexus-aliyun</id>
       <mirrorOf>*</mirrorOf>
       <name>Nexus aliyun</name>
       <url>http://maven.aliyun.com/nexus/content/groups/public</url>
   </mirror>                                                                                               
</mirrors>

# 下载zooInspector
git clone https://mirror.ghproxy.com/https://github.com/zzhang5/zooinspector.git

cd zooinspector/
mvn clean package -Dmaven.test.skip=true

# 授权
chmod +x zooinspector-pkg/bin/zooinspector.sh

# windows宿主机上开启Xmanager

# Linux定义环境变量
export DISPLAY=10.0.0.1:0.0

# 运行
./zooinspector-pkg/bin/zooinspector.sh
```



## Kafka

### 消息队列简介

#### MQ定义

```http
#阿里云消息队列
https://www.aliyun.com/product/ons?spm=5176.234368.h2v3icoap.427.2620db25lcHi1Q&amp;aly_as=Tz_Lue_o
```

在分布式场景中，相对于大量的用户请求来说，内部的功能主机之间、功能模块之间等，数据传递的数据量是无法想象的，因为一个用户请求，会涉及到各种内部的业务逻辑跳转等操作。那么，在大量用户的业务场景中，如何保证所有的内部业务逻辑请求都处于稳定而且快捷的 数据传递呢? 消息队列(Message Queue)技术可以满足此需求

消息队列（Message Queue，简称 MQ）是构建分布式互联网应用的基础设施，通过 MQ 实现的松耦合架构设计可以提高系统可用性以及可扩展性，是适用于现代应用的最佳设计方案。

消息队列是一种异步的服务间通信方式，适用于无服务器和微服务架构。消息在被处理和删除之前一直存储在队列上。每条消息仅可被一位用户处理一次。消息队列可被用于分离重量级处理、缓冲或批处理工作以及缓解高峰期工作负载。



#### MQ 使用场合

消息队列作为高并发系统的核心组件之一，能够帮助业务系统结构提升开发效率和系统稳定性

**消息队列主要有以下应用场景**

- **削峰填谷**
  - 诸如电商业务中的秒杀、抢红包、企业开门红等大型活动时皆会带来较高的流量脉冲，或因没做相应的保护而导致系统超负荷甚至崩溃，或因限制太过导致请求大量失败而影响用户体验，消息队列可提供削峰填谷的服务来解决该问题。
- **异步解耦**
  - 交易系统作为淘宝等电商的最核心的系统，每笔交易订单数据的产生会引起几百个下游业务系统的关注，包括物流、购物车、积分、流计算分析等等，整体业务系统庞大而且复杂，消息队列可实现异步通信和应用解耦，确保主站业务的连续性。

- **顺序收发**
  - 细数日常中需要保证顺序的应用场景非常多，例如证券交易过程时间优先原则，交易系统中的订单创建、支付、退款等流程，航班中的旅客登机消息处理等等。与先进先出FIFO（First In First Out）原理类似，消息队列提供的顺序消息即保证消息FIFO。

- **分布式事务一致性**
  - 交易系统、支付红包等场景需要确保数据的最终一致性，大量引入消息队列的分布式事务，既可以实现系统之间的解耦，又可以保证最终的数据一致性。

- **大数据分析**
  - 数据在“流动”中产生价值，传统数据分析大多是基于批量计算模型，而无法做到实时的数据分析，利用消息队列与流式计算引擎相结合，可以很方便的实现业务数据的实时分析。

- **分布式缓存同步**
  - 电商的大促，各个分会场琳琅满目的商品需要实时感知价格变化，大量并发访问数据库导致会场页面响应时间长，集中式缓存因带宽瓶颈，限制了商品变更的访问流量，通过消息队列构建分布式缓存，实时通知商品数据的变化

- **蓄流压测**
  - 线上有些链路不方便做压力测试，可以通过堆积一定量消息再放开来压测




#### 主流MQ

目前主流的消息队列软件有 **Kafka**、**RabbitMQ**、ActiveMQ、**RocketMQ**等，还有相对小众的消息队列软件如ZeroMQ、Apache Qpid 



### Kafka介绍

![image-20250124113709879](D:\git_repository\cyber_security_learning\markdown_img\image-20250124113709879.png)

Kafka 被称为下一代分布式消息系统，由 **Scala 和 Java编写**，是非营利性组织ASF(Apache Software Foundation)基金会中的一个开源项 目，比如:HTTP Server、Tomcat、Hadoop、ActiveMQ等开源软件都属于 Apache基金会的开源软件，类似的消息系统还有RabbitMQ、 ActiveMQ、ZeroMQ。

Kafka用于构建实时数据管道和流应用程序。 它具有水平可伸缩性，容错性，快速性，可在数千家组织中同时投入生产协同工作。



### Kafka 特点和优势

![image-20250124114136074](D:\git_repository\cyber_security_learning\markdown_img\image-20250124114136074.png)

**特点**

- **分布式**: 支持分布式多主机部署实现
- **分区**: 一个消息.可以拆分出多个，分别存储在多个位置
- **多副本**: 防止信息丢失，可以多来几个备份
- **多订阅者**: 可以有很多应用连接kafka
- **Zookeeper**: 早期版本的Kafka依赖于zookeeper， **2021年**4月19日**Kafka 2.8.0**正式发布，此版本包括了很多重要改动，最主要的是 kafka通过自我管理的仲裁来替代ZooKeeper，即Kafka**将不再需要ZooKeeper！**



**优势**

- Kafka 通过 O(1)的磁盘数据结构提供消息的持久化，这种结构对于即使数以 TB 级别以上的消息存储也能够保持长时间的稳定性能。
- **高吞吐量**：即使是非常普通的硬件Kafka也可以支持每秒数百万的消息。支持通过Kafka 服务器分区消息。
- **分布式**： Kafka 基于分布式集群实现高可用的容错机制，可以实现自动的故障转移
- **顺序保证**：在大多数使用场景下，数据处理的顺序都很重要。大部分消息队列本来就是排序的，并且能保证数据会按照特定的顺序来处理。 Kafka保证一个Partiton内的消息的有序性（分区间数据是无序的，如果对数据的顺序有要求，应将在创建主题时将分区数partitions设置为1）
- 支持 Hadoop 并行数据加载
- 通常用于大数据场合,传递单条消息比较大，而Rabbitmq 消息主要是传输业务的指令数据,单条数据较小



### Kafka角色和流程

####  Kafka概念![image-20250127092542394](D:\git_repository\cyber_security_learning\markdown_img\image-20250127092542394.png)



**Producer**：Producer即生产者，消息的产生者，是消息的入口。负责发布消息到Kafka broker

**Consumer**：消费者，用于消费消息，即处理消息

**Broker**：Broker是kafka实例，每个服务器上可以有一个或多个kafka的实例，假设每个broker对应一台服务器。每个kafka集群内的broker 都有一个不重复的编号，如: broker-0、broker-1等…...

**Controller**：是整个 Kafka 集群的管理者角色，任何集群范围内的状态变更都需要通过 Controller 进行，在整个集群中是个单点的服务，可以通过选举协议进行故障转移，负责集群范围内的一些关键操作：主题的新建和删除，主题分区的新建、重新分配，Broker 的加入、退出， 触发分区 Leader 选举等，每个 Broker 里都有一个 Controller 实例，多个 Broker 的集群同时最多只有一个 Controller 可以对外提供集群管理服务，Controller 可以在 Broker 之间进行故障转移，Kafka 集群管理的工作主要是由 Controller 来完成的，而 Controller 又通过监听  Zookeeper 节点的变动来进行监听集群变化事件，Controller 进行集群管理需要保存集群元数据，监听集群状态变化情况并进行处理，以及 处理集群中修改集群元数据的请求，这些主要都是**利用 Zookeeper 来实现**

**Topic** ：消息的主题，可以理解为消息的分类，一个Topic相当于数据库中的一张表,一条消息相当于关系数据库的一条记录，或者一个Topic 相当于Redis中列表数据类型的一个Key，一条消息即为列表中的一个元素。kafka的数据就保存在topic。在每个broker上都可以创建多个 topic。  虽然一个 topic的消息保存于一个或多个broker 上同一个目录内, 物理上不同 topic 的消息分开存储在不同的文件夹，但用户只需指定消息的 topic即可生产或消费数据而不必关心数据存于何处，topic 在逻辑上对record(记录、日志)进行分组保存，消费者需要订阅相应的topic 才能 消费topic中的消息。

**Consumer group**: 每个consumer 属于一个特定的consumer group（可为每个consumer 指定 group name，若不指定 group name 则 属于默认的group），同一topic的一条消息只能被同一个consumer group 内的一个consumer 消费，类似于一对一的单播机制，但多个 consumer group 可同时消费这一消息，类似于一对多的多播机制，默认消费组的多个消费者是共享消息。**（同一组内的consumer是生产者消费者模式，即抢占模式，不同组内的consumer是发布者订阅者模式，可以同时订阅同一个消息）**

**Partition** ：是物理上的概念，每个 topic 分割为一个或多个partition，即一个topic切分为多份, 当创建 topic 时可指定 partition 数量， partition的表现形式就是一个一个的文件夹,该文件夹下存储该partition的数据和索引文件，分区的作用还可以实现负载均衡，提高kafka的吞吐量。同一个topic在不同的分区的数据是不重复的,一般Partition数不要超过节点数，注意同一个partition数据是有顺序的，但不同的 partition则是无序的。（**即分片**）

**Replication**: 同样数据的副本，包括leader和follower的副本数,基本于数据安全,建议至少2个,是Kafka的高可靠性的保障，和ES的副本有所 不同，**Kafka中的副(leader+follower）数包括主分片数,而ES中的副本数(follower)不包括主分片数**

为了实现数据的高可用，比如将分区 0 的数据分散到不同的kafka 节点，每一个分区都有一个 broker 作为 Leader 和一个 broker 作为 Follower，类似于ES中的主分片和副本分片，

假设分区为 3, 即分三个分区0-2，副本为3，即每个分区都有一个 leader，再加两个follower，分区 0 的leader为服务器A，则服务器 B 和服 务器 C 为 A 的follower，而分区 1 的leader为服务器B，则服务器 A 和C 为服务器B 的follower，而分区 2 的leader 为C，则服务器A 和 B 为 C 的follower。

**AR**： Assigned Replicas，分区中的所有副本的统称，包括leader和 follower，AR= lSR+ OSR

**lSR**：ln Sync Replicas，所有与leader副本保持同步的副本 follower和leader本身组成的集合，包括leader和 follower，是AR的子集

**OSR**：out-of-Sync Replied，所有与leader副本同步不能同步的 follower的集合，是AR的子集

![image-20250127105623929](D:\git_repository\cyber_security_learning\markdown_img\image-20250127105623929.png)



#### Kafka 工作机制

Apache Kafka的选举机制涉及到其使用的分区复制模式（partition replication）。

每个Kafka Topic 的分区都有一个领导者（leader）和零个或多个追随者（follower）。

领导者负责所有客户端请求的读写操作，而追随者则复制领导者的数据(kafka2.4新版本后，也支持读)

**Kafka的领导者选举过程发生在以下情况中：**

- 当新的分区创建时，Kafka选择ISR（In-Sync Replica）列表中的第一个副本作为领导者。
- 当领导者失败或无法与ZooKeeper通信时，会重新选举新的领导者。这个过程被称为领导者故障转移（leader failover）



**Kafka领导者选举的详细步骤**

-  当领导者发生故障，ZooKeeper将会检测到它的会话过期。
-  ZooKeeper接着将通知所有的副本进行领导者选举。
- 副本们会查看它们在ZooKeeper中存储的元数据并确定新的领导者，选择规则是选取副本集合（ISR）中最新的副本。
- 一旦新的领导者被选出，ZooKeeper将通知所有的副本更新它们的元数据。

**注意**：Kafka 2.8.0版本开始，增加了KRaft（KRaft是Kafka Raft协议模式的简称）模式，这个模式下Kafka不再需要ZooKeeper，而是使用内 置的Raft协议来进行元数据的管理和领导者选举。Raft协议是一种为分布式系统提供一致性的算法，它更易于理解和实施，同时也保证了系 统的可用性和数据的一致性。

![image-20250127110415730](D:\git_repository\cyber_security_learning\markdown_img\image-20250127110415730.png)

Apache Kafka可以配置为提供**强一致性**的语义，但这是以牺牲一定的性能为代价的

在Kafka中，数据被分布在各个分区上，每个分区都有一个领导者（leader）和若干个追随者（follower）。领导者负责处理所有读写请求， 而追随者则复制领导者的数据。这种设计确保了数据的高可用性和容错性

然而，为了保证高性能和低延迟，Kafka允许领导者在数据还未被所有的追随者复制之前就将写操作确认为成功。这就带来了一种可能的情况，即在领导者确认写操作成功后、新数据还未被所有追随者复制完成之前，领导者发生故障，此时新数据可能会丢失，从而造成一致性问题。

要实现强一致性，你需要将Kafka的 **min.insync.replicas** 参数设置为大于1，这样可以确保至少有N个副本确认数据写入才认为写操作成 功。并且需要设置 acks 为 all 或者-1，表示领导者需要等待所有的ISR（In-Sync Replicas）确认接收到消息后，才向生产者返回ack。这 样，即使领导者发生故障，由于至少有一个追随者已经复制了数据，新的领导者仍然可以提供所有的数据，从而保证了强一致性。

总的来说，Kafka可以配置为提供强一致性，但这可能会影响其性能和吞吐量。在实际使用中，你需要根据自己的业务需求在一致性和性能 之间进行权衡



### Kafka 部署

#### Kafka 部署说明

**kafka 版本选择**

kafka 基于scala语言实现,所以使用kafka需要指定scala的相应的版本.kafka 为多个版本的Scala构建。这仅在使用 Scala 时才重要，并且希望为使用的相同Scala 版本构建一个版本。否则，任何版本都可以

**kafka下载链接**

```http
http://kafka.apache.org/downloads
```

 **kafka版本格式**

```ABAP
kafka_<scala 版本>_<kafka 版本>
#示例:kafka_2.13-2.7.0.tgz
```

 scala 语言官网:  https://www.scala-lang.org/

scale 与 java关系: https://baike.baidu.com/item/Scala/2462287?fr=aladdin

**官方文档**

```http
http://kafka.apache.org/quickstart
```



#### 单机部署

##### 单机部署Kafka 脚本

```bash
#!/bin/bash
#
#********************************************************************
#Author:            mystical
#QQ:                29308620
#Date:              2020-06-03
#FileName:          install_kafka_single_node.sh
#URL:               http://www.wangxiaochun.com
#Description:       The test script
#Copyright (C):     2020 All rights reserved
#********************************************************************
 
 #支持在线和离线安装安装
 
KAFKA_VERSION=3.8.0
#KAFKA_VERSION=3.5.1
#KAFKA_VERSION=3.5.0
#KAFKA_VERSION=3.4.0
#KAFKA_VERSION=3.3.2
#KAFKA_VERSION=3.2.0
#KAFKA_VERSION=-3.0.0
SCALA_VERSION=2.13
 KAFKA_URL="https://mirrors.tuna.tsinghua.edu.cn/apache/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"
#KAFKA_URL="https://mirrors.tuna.tsinghua.edu.cn/apache/kafka/2.8.1/kafka_2.13-2.8.1.tgz"
#KAFKA_URL="https://mirrors.tuna.tsinghua.edu.cn/apache/kafka/2.7.1/kafka_2.13-2.7.1.tgz"

KAFKA_INSTALL_DIR=/usr/local/kafka
HOST=`hostname -I|awk '{print $1}'`
.  /etc/os-release

color () {
    RES_COL=60
    MOVE_TO_COL="echo -en \\033[${RES_COL}G"
    SETCOLOR_SUCCESS="echo -en \\033[1;32m"
    SETCOLOR_FAILURE="echo -en \\033[1;31m"
    SETCOLOR_WARNING="echo -en \\033[1;33m"
    SETCOLOR_NORMAL="echo -en \E[0m"
    echo -n "$1" && $MOVE_TO_COL
    echo -n "["
    if [ $2 = "success" -o $2 = "0" ] ;then
        ${SETCOLOR_SUCCESS}
        echo -n $"  OK  "    
    elif [ $2 = "failure" -o $2 = "1"  ] ;then 
        ${SETCOLOR_FAILURE}
        echo -n $"FAILED"
    else
        ${SETCOLOR_WARNING}
        echo -n $"WARNING"
    fi
    ${SETCOLOR_NORMAL}
    echo -n "]"
    echo 
}

env () {
    echo $HOST `hostname` >> /etc/hosts
}

install_jdk() {
    java -version &>/dev/null && { color "JDK 已安装!" 1 ; return;  }
    if command -v yum &>/dev/null ; then
        yum -y install java-1.8.0-openjdk-devel || { color "安装JDK失败!" 1; exit 1; }
    elif command -v apt &>/dev/null ; then
        apt update
        #apt install openjdk-11-jdk -y || { color "安装JDK失败!" 1; exit 1; } 
        apt install openjdk-8-jdk -y || { color "安装JDK失败!" 1; exit 1; } 
    else
        color "不支持当前操作系统!" 1
        exit 1
    fi
    java -version && { color "安装 JDK 完成!" 0 ; } || { color "安装JDK失败!" 1; exit 1; } 
}

install_zookeeper() {
    cat > ${KAFKA_INSTALL_DIR}/bin/zookeeper-startup.sh <<EOF
#!/bin/bash
nohup ${KAFKA_INSTALL_DIR}/bin/zookeeper-server-start.sh ${KAFKA_INSTALL_DIR}/config/zookeeper.properties  &
EOF
    chmod +x ${KAFKA_INSTALL_DIR}/bin/zookeeper-startup.sh
    cat > /lib/systemd/system/zookeeper.service <<EOF
[Unit]
Description=zookeeper.service
After=network.target
[Service]
Type=forking
ExecStart=${KAFKA_INSTALL_DIR}/bin/zookeeper-startup.sh
ExecStop=${KAFKA_INSTALL_DIR}/bin/zookeeper-server-stop.sh 
[Install]
WantedBy=multi-user.target
EOF
    systemctl daemon-reload
    systemctl enable --now  zookeeper.service
    systemctl is-active zookeeper.service
    if [ $? -eq 0 ] ;then 
        color "zookeeper 安装成功!" 0  
    else 
        color "zookeeper 安装失败!" 1
        exit 1
    fi  
}

install_kafka(){
    if [ ! -f kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz ];then
        wget -P /usr/local/src/  --no-check-certificate $KAFKA_URL  || { color  "下载失败!" 1 ;exit ; }
    fi
    tar xf /usr/local/src/${KAFKA_URL##*/}  -C /usr/local/
    ln -s /usr/local/kafka_${SCALA_VERSION}-${KAFKA_VERSION}  ${KAFKA_INSTALL_DIR}
    install_zookeeper
    echo PATH=${KAFKA_INSTALL_DIR}/bin:'$PATH' >> /etc/profile
    cat > ${KAFKA_INSTALL_DIR}/bin/kafka-startup.sh <<EOF
#!/bin/bash
nohup ${KAFKA_INSTALL_DIR}/bin/kafka-server-start.sh  ${KAFKA_INSTALL_DIR}/config/server.properties &
EOF
    chmod +x ${KAFKA_INSTALL_DIR}/bin/kafka-startup.sh
    cat > /lib/systemd/system/kafka.service <<EOF
[Unit]                                                                          
Description=Apache kafka
After=network.target
[Service]
Type=forking
ExecStart=${KAFKA_INSTALL_DIR}/bin/kafka-startup.sh
ExecStop=/bin/kill  -TERM \${MAINPID}
Restart=always
RestartSec=20
[Install]
WantedBy=multi-user.target
EOF
    systemctl daemon-reload
    systemctl enable --now kafka.service
    #kafka-server-start.sh -daemon ${KAFKA_INSTALL_DIR}/config/server.properties 
    systemctl is-active kafka.service
    if [ $? -eq 0 ] ;then 
        color "kafka 安装成功!" 0  
    else 
        color "kafka 安装失败!" 1
        exit 1
    fi    
}

env 
install_jdk
install_kafka
```

```bash
#Ubuntu22.04编译
apt update && apt -y install openjdk-8-jdk
apt update && apt -y install maven

# 添加阿里云加速
vim /etc/maven/settings.xml 
<mirrors>
   <!--阿里云镜像-->
   <mirror>
       <id>nexus-aliyun</id>
       <mirrorOf>*</mirrorOf>
       <name>Nexus aliyun</name>
       <url>http://maven.aliyun.com/nexus/content/groups/public</url>
   </mirror>                                                                                               
</mirrors>

# 下载zooInspector
git clone https://mirror.ghproxy.com/https://github.com/zzhang5/zooinspector.git

cd zooinspector/
mvn clean package -Dmaven.test.skip=true

# 授权
chmod +x zooinspector-pkg/bin/zooinspector.sh

# windows宿主机上开启Xmanager

# Linux定义环境变量
export DISPLAY=10.0.0.1:0.0

# 运行
./zooinspector-pkg/bin/zooinspector.sh
```

![image-20250127125130187](D:\git_repository\cyber_security_learning\markdown_img\image-20250127125130187.png)



#### 集群部署

##### 环境准备

**主机名解析**

注意：每个kafka节点的主机名称解析需要提前准备，否则会导致失败

```bash
#修改每个kafka节点的主机名
[root@ubuntu2204 ~]#hostnamectl hostname node1
[root@ubuntu2204 ~]#hostnamectl hostname node2
[root@ubuntu2204 ~]#hostnamectl hostname node3

#在所有kafka节点上实现主机名称解析
[root@ubuntu2204 ~]#cat /etc/hosts
10.0.0.101 node1
10.0.0.102 node2
10.0.0.103 node3
```

**安装JDK**

```bash
# 所有节点安装jdk，因为zookeeper是java程序
[root@node1 ~]# apt update && apt install openjdk-8-jdk -y
[root@node2 ~]# apt update && apt install openjdk-8-jdk -y
[root@node3 ~]# apt update && apt install openjdk-8-jdk -y
```

##### **安装 ZooKeeper**

注意:如果使用kafka自带的zookeeper，需要修改配置文件

```bash
# 集群所有节点执行下面操作
# 下载kafka
[root@node1 ~]# wget -P /usr/local/src https://mirrors.tuna.tsinghua.edu.cn/apache/kafka/3.8.0/kafka_2.13-3.8.0.tgz

# 解压
[root@node1 src]# tar xf /usr/local/src/kafka_2.13-3.8.0.tgz -C /usr/local/

# 创建软链接
[root@node1 local]# ln -s /usr/local/kafka_2.13-3.8.0/ /usr/local/kafka

#注意如果使用kafka自带的zookeeper，需要修改配置文件
[root@node1 ~]#vim /usr/local/kafka/config/zookeeper.properties
# 更改数据目录
dataDir=/usr/local/kafka/data
#添加三行时间相关配置
tickTime=2000
# The number of ticks that the initial 
# synchronization phase can take
initLimit=10
# The number of ticks that can pass between 
# sending a request and getting an acknowledgement
syncLimit=5
#添加下面集群配置
 
server.1=10.0.0.101:2888:3888
server.2=10.0.0.102:2888:3888
server.3=10.0.0.103:2888:3888

# 同步到其他节点
[root@node1 config]#scp zookeeper.properties 10.0.0.102:/usr/local/kafka/config/zookeeper.properties
zookeeper.properties 
[root@node1 config]#scp zookeeper.properties 10.0.0.103:/usr/local/kafka/config/zookeeper.properties
zookeeper.properties 

# 创建目录
[root@node1 kafka]# mkdir data
[root@node2 kafka]# mkdir data
[root@node3 kafka]# mkdir data

# 每个节点配置myid
[root@node1 data]# echo 1 > /usr/local/kafka/data/myid
[root@node2 data]# echo 2 > /usr/local/kafka/data/myid
[root@node3 data]# echo 3 > /usr/local/kafka/data/myid

# 创建启动文件
[root@node1 ~]# cat > /usr/local/kafka/bin/zookeeper-startup.sh <<EOF
#!/bin/bash
nohup /usr/local/kafka/bin/zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties &
EOF
[root@node1 ~]# chmod +x /usr/local/kafka/bin/zookeeper-startup.sh

# 将二进制执行文件同步到其他节点
[root@node1 ~]# rsync -a /usr/local/kafka/bin/zookeeper-startup.sh 10.0.0.102:/usr/local/kafka/bin/
[root@node1 ~]# rsync -a /usr/local/kafka/bin/zookeeper-startup.sh 10.0.0.103:/usr/local/kafka/bin/

# 创建service文件
[root@node1 ~]# cat > /lib/systemd/system/zookeeper.service<<EOF
[Unit]
Description=zookeeper.service
After=network.target
[Service]
Type=forking
ExecStart=/usr/local/kafka/bin/zookeeper-startup.sh
ExecStop=/usr/local/kafka/bin/zookeeper-server-stop.sh 
[Install]
WantedBy=multi-user.target
EOF

# 将service文件同步到其他节点
[root@node1 ~]# scp /lib/systemd/system/zookeeper.service 10.0.0.102:/lib/systemd/system/
[root@node1 ~]# scp /lib/systemd/system/zookeeper.service 10.0.0.103:/lib/systemd/system/

# 所有节点启动服务
[root@node1 bin]#systemctl daemon-reload 
[root@node1 bin]#systemctl restart zookeeper.service 
```



##### 各节点部署Kafka

**配置文件说明**

```bash
#配置文件 ./conf/server.properties内容说明

############################# Server Basics###############################

# broker的id，值为整数，且必须唯一，在一个集群中不能重复，此行必须修改
broker.id=1

############################# Socket ServerSettings ######################

# kafka监听端口，默认9092
listeners=PLAINTEXT://10.0.0.101:9092 #指定当前主机的IP做为监听地址,注意:不支持0.0.0.0

# 处理网络请求的线程数量，默认为3个
num.network.threads=3

# 执行磁盘IO操作的线程数量，默认为8个
num.io.threads=8

# socket服务发送数据的缓冲区大小，默认100KB
socket.send.buffer.bytes=102400

# socket服务接受数据的缓冲区大小，默认100KB
socket.receive.buffer.bytes=102400

# socket服务所能接受的一个请求的最大大小，默认为100M
socket.request.max.bytes=104857600

############################# Log Basics###################################

# kafka存储消息数据的目录
log.dirs=../data

# 每个topic默认的partition
num.partitions=1

# 设置副本数量为3,当Leader的Replication故障，会进行故障自动转移。
default.replication.factor=3

# 在启动时恢复数据和关闭时刷新数据时每个数据目录的线程数量
num.recovery.threads.per.data.dir=1

############################# Log FlushPolicy #############################
# 消息刷新到磁盘中的消息条数阈值
log.flush.interval.messages=10000

# 消息刷新到磁盘中的最大时间间隔1s,单位是ms
log.flush.interval.ms=1000

############################# Log RetentionPolicy #########################
# 日志保留小时数，超时会自动删除，默认为7天
log.retention.hours=168

# 日志保留大小，超出大小会自动删除，默认为1G
#log.retention.bytes=1073741824

# 日志分片策略，单个日志文件的大小最大为1G，超出后则创建一个新的日志文件
log.segment.bytes=1073741824

# 每隔多长时间检测数据是否达到删除条件,300s
log.retention.check.interval.ms=300000

############################# Zookeeper ####################################
# Zookeeper连接信息，如果是zookeeper集群，则以逗号隔开，此行必须修改
zookeeper.connect=10.0.0.101:2181,10.0.0.102:2181,10.0.0.103:2181

# 连接zookeeper的超时时间,6s
zookeeper.connection.timeout.ms=6000

# 是否允许删除topic，默认为false，topic只会标记为marked for deletion
delete.topic.enable=true
```

**部署Kafka**

```bash
#配置PATH变量
[root@node1 ~]# echo 'PATH=/usr/local/kafka/bin:$PATH' > /etc/profile.d/kafka.sh
[root@node1 ~]# . /etc/profile.d/kafka.sh

#修改配置文件
[root@node1 ~]# vim /usr/local/kafka/config/server.properties
broker.id=1 #每个broker在集群中每个节点的正整数唯一标识，此值保存在log.dirs下的meta.properties文件，修改此行
listeners=PLAINTEXT://10.0.0.101:9092 #指定当前主机的IP做为监听地址,注意:不支持0.0.0.0
log.dirs=/usr/local/kafka/data #kakfa用于保存数据的目录，所有的消息都会存储在该目录当中，修改此行
num.partitions=3 #设置创建新的topic时默认分区数量,建议和kafka的节点数量一致
default.replication.factor=3 #指定默认的副本数为3，可以实现故障的自动转移
log.retention.hours=168 #设置kafka中消息保留时间，默认为168小时即7天
zookeeper.connect=10.0.0.101:2181,10.0.0.102:2181,10.0.0.103:2181 #指定连接的zk的地址,zk中存储了broker的元数据信息，修改此行
zookeeper.connection.timeout.ms=6000 #设置连接zookeeper的超时时间，单位为ms,默认6秒钟

#准备数据目录,安装zookeeper的时候应该创建过
[root@node1 ~]#mkdir /usr/local/kafka/data

# 先同步配置文件，后对其进行修改
[root@node1 ~]#scp /usr/local/kafka/config/server.properties 10.0.0.102:/usr/local/kafka/config
[root@node1 ~]#scp /usr/local/kafka/config/server.properties 10.0.0.103:/usr/local/kafka/config

#修改第2个节点配置
[root@node2 ~]#vim /usr/local/kafka/config/server.properties
broker.id=2 #每个broker 在集群中的唯一标识，正整数。
listeners=PLAINTEXT://10.0.0.102:9092 #指定当前主机的IP做为监听地址,注意:不支持0.0.0.0

#修改第3个节点配置
[root@node3 ~]#vim /usr/local/kafka/config/server.properties
broker.id=3  #每个broker 在集群中的唯一标识，正整数。
listeners=PLAINTEXT://10.0.0.103:9092 #指定当前主机的IP做为监听地址,注意:不支持0.0.0.0

#可以调整内存
[root@node1 ~]#vim /usr/local/kafka/bin/kafka-server-start.sh
......
if[ " x$KAFKA_HEAP_OPTS"="x"] ; then
    export KAFKA_HEAP_OPTS=" -Xmx1G -Xms1G"  
fi
......
```



##### 准备Kafka的service文件

```bash
[root@node1 bin]# cat /lib/systemd/system/kafka.service
[Unit]                                                                          
Description=Apache kafka
After=network.target
[Service]
Type=forking
ExecStart=/usr/local/kafka/bin/kafka-startup.sh
ExecStop=/bin/kill  -TERM \${MAINPID}
Restart=always
RestartSec=20
[Install]
WantedBy=multi-user.target

# 同步service文件，并重启服务
[root@node1 bin]# scp /lib/systemd/system/kafka.service 10.0.0.102:/lib/systemd/system/  
[root@node1 bin]# scp /lib/systemd/system/kafka.service 10.0.0.103:/lib/systemd/system/

# 所有节点上重启服务
[root@node1 bin]# systemctl daemon-reload 
[root@node1 bin]# systemctl restart kafka

# 查看zooInspector
```

![image-20250127182115277](D:\git_repository\cyber_security_learning\markdown_img\image-20250127182115277.png)

**注意**

```ABAP
如果有服务器加入集群失败，可以将data和logs目录里的内容删掉，重启
！！！记住，两个目录的内容都要删掉
```



### Kafka 读写数据

参考文档

```http
http://kafka.apache.org/quickstart
```

常见命令

```bash
kafka-topics.sh             #消息的管理命令           
kafka-console-producer.sh   #生产者的模拟命令
kafka-console-consumer.sh   #消费者的模拟命令
```



#### 创建Topic

创建topic名为 mystical，partitions(分区)为3，replication(每个分区的副本数/每个分区的分区因子)为 2

```bash
#新版命令,通过--bootstrap-server指定kafka的地址
[root@node1 ~]# /usr/local/kafka/bin/kafka-topics.sh --create --topic mystical --bootstrap-server 10.0.0.101:9092 --partitions 3 --replication-factor 2

#旧版命令，通过--zookeeper指定zookeeper的地址
[root@node1 ~]# /usr/local/kafka/bin/kafka-topics.sh --create --zookeeper 10.0.0.101:2181,10.0.0.102:2181,10.0.0.103:2181 --partitions 3 --replication-factor 2 --topic mystical

#在各节点上观察生成的相关数据
[root@node1 ~]# ls /usr/local/kafka/data
cleaner-offset-checkpoint    meta.properties  mystical-0  recovery-point-offset-checkpoint  version-2
log-start-offset-checkpoint  myid             mystical-1  replication-offset-checkpoint

[root@node2 bin]# ls /usr/local/kafka/data
cleaner-offset-checkpoint    meta.properties  mystical-1  recovery-point-offset-checkpoint  version-2
log-start-offset-checkpoint  myid             mystical-2  replication-offset-checkpoint

[root@node3 ~]#ls /usr/local/kafka/data/
cleaner-offset-checkpoint    meta.properties  mystical-0  recovery-point-offset-checkpoint  version-2
log-start-offset-checkpoint  myid             mystical-2  replication-offset-checkpoint
```



#### 获取所有 Topic

```bash
#新版命令
[root@node1 ~]# /usr/local/kafka/bin/kafka-topics.sh --list --bootstrap-server 10.0.0.101:9092

#旧版命令
[root@node1 ~]# /usr/local/kafka/bin/kafka-topics.sh --list --zookeeper 10.0.0.101:2181,10.0.0.102:2181,10.0.0.103:2181
```

![image-20250127194747818](D:\git_repository\cyber_security_learning\markdown_img\image-20250127194747818.png)



####  查看 Topic 详情

状态说明：mystical 有三个分区分别为0、1、2，分区0的leader是3 （broker.id），分区 0 有2 个副本，并且状态都为 lsr（ln-sync，表示可 以参加选举成为 leader）

```bash
# 新版命令
[root@node1 data]# /usr/local/kafka/bin/kafka-topics.sh --describe --bootstrap-server 10.0.0.101:9092  --topic mystical
[2025-01-27 19:50:51,936] WARN [AdminClient clientId=adminclient-1] The DescribeTopicPartitions API is not supported, using Metadata API to describe topics. (org.apache.kafka.clients.admin.KafkaAdminClient)
Topic: mystical	TopicId: 1xuTntXbTfO9ewL3SRfhRw	PartitionCount: 3	ReplicationFactor: 2	Configs: 
	Topic: mystical	Partition: 0	Leader: 1	Replicas: 1,3	Isr: 1,3	Elr: N/A	LastKnownElr: N/A
	Topic: mystical	Partition: 1	Leader: 2	Replicas: 2,1	Isr: 2,1	Elr: N/A	LastKnownElr: N/A
	Topic: mystical	Partition: 2	Leader: 3	Replicas: 3,2	Isr: 3,2	Elr: N/A	LastKnownElr: N/A
	
#旧版命令
[root@node1 ~]# /usr/local/kafka/bin/kafka-topics.sh --describe --zookeeper 10.0.0.101:2181,10.0.0.102:2181,10.0.0.103:2181 --topic wang
```



#### 生产 Topic

kafka-console-producer.sh 格式

```bash
#发送消息命令格式:
[root@node1 ~]# kafka-console-producer.sh --broker-list <kafkaIP1>:<端口>,<kafkaIP2>:<端口> --topic <topic名称> --producer property group.id=<组名>
```

范例

```bash
#交互式输入消息,按Ctrl+C退出
[root@node1 ~]# /usr/local/kafka/bin/kafka-console-producer.sh --broker-list 10.0.0.101:9092,10.0.0.102:9092,10.0.0.103:9092 --topic mystical
>message1
>message2
>message3
>
 #或者下面方式
[root@node1 ~]#/usr/local/kafka/bin/kafka-console-producer.sh --topic mystical --bootstrap-server 10.0.0.101:9092
```



#### 消费 Topic

kafka-console-consumer.sh 格式

```bash
# 接收消息命令格式:
[root@node1 ~]# kafka-console-consumer.sh --bootstrap-server <host>:<post> --topic <topic名称> --from-beginning --consumer-property group.id=<组名称>
```

注意：

- 生产者先生产消息，消费者后续启动，也能收到之前生产的消息
- 同一个消息在同一个group内的消费者只有被一个消费者消费，比如：共100条消息，在一个group内有A，B两个消费者，其中A消费 50条，B消费另外的50条消息。从而实现负载均衡，不同group内的消费者则可以同时消费同一个消息
- `--from-beginning` 表示消费前发布的消息也能收到，默认只能收到消费后发布的新消息

范例

```bash
#交互式持续接收消息,按Ctrl+C退出
[root@node1 ~]#/usr/local/kafka/bin/kafka-console-consumer.sh --topic wang --bootstrap-server 10.0.0.102:9092 --from-beginning
message1
message3
message2

#一个消息同时只能被同一个组内一个消费者消费（单播机制），实现负载均衡，而不同组可以同时消费同一个消息（多播机制）
# 其中如果不指定组，则消费者算作是默认组中，而默认组中的消费者，共享消息
[root@node2 ~]#/usr/local/kafka/bin/kafka-console-consumer.sh --topic wang --bootstrap-server 10.0.0.102:9092 --from-beginning --consumer-property group.id=group1

[root@node2 ~]#/usr/local/kafka/bin/kafka-console-consumer.sh --topic wang --bootstrap-server 10.0.0.102:9092 --from-beginning --consumer-property group.id=group1
```



#### 删除 Topic

```bash
#注意：需要修改配置文件server.properties中的delete.topic.enable=true并重启
#新版本
[root@node3 ~]#/usr/local/kafka/bin/kafka-topics.sh --delete --bootstrap-server 10.0.0.101:9092,10.0.0.102:9092,10.0.0.103:9092 --topic wang

#旧版本
[root@node3 ~]#/usr/local/kafka/bin/kafka-topics.sh --delete --zookeeper 10.0.0.101:2181,10.0.0.102:2181,10.0.0.103:2181 --topic wang
Topic wang is marked for deletion.
Note: This will have no impact if delete.topic.enable is not set to true.
```



### 消息积压

消息积压是指在消息传递系统中，积累了大量未被处理或未被消费的消息

Kafka 消息积压可能由多种原因引起，以下是一些可能的原因：

- **消费者处理速度慢**： 如果消费者处理消息的速度不足以跟上生产者的速度，就会导致消息积压。这可能是因为消费者逻辑复杂、消费 者数量不足、消费者宕机或者网络延迟等原因引起的。
-  **消费者宕机**： 如果某个消费者宕机，其负责处理的分区将没有消费者来消费消息，导致消息在该分区上积压
- **网络问题**： 网络故障可能导致生产者和消费者之间的通信延迟或中断，从而影响消息的传递速度
- **硬件资源不足**： Kafka 集群所在的机器，包括生产者、消费者和 Broker 所在的机器，可能由于 CPU、内存或磁盘等资源不足，导致消息处理速度变慢
-  **分区不均匀**： 如果某些分区的负载比其他分区更高，可能导致这些分区上的消息积压。这可能是由于分区数量设置不合理、数据分布 不均匀等原因引起的
- **生产者速度过快**： 如果生产者生产消息的速度过快，而消费者无法及时处理，就会导致消息积压
- **配置不当**： Kafka 的一些配置参数，如副本数、分区数、消费者数量等，需要根据实际情况进行合理的配置。如果配置不当，可能导致 消息积压问题。
- **异常情况**： 突发性的异常情况，如硬件故障、网络故障、软件 bug 等，都可能导致消息积压



Kafka 消息积压可能的解决方案

- **增加消费者数量**：如果消费者处理速度不足导致消息积压，可以增加消费者的数量来提高处理速度。
- **扩展Kafka集群**：如果消息积压是由于Kafka集群的吞吐量达到极限导致的，考虑扩展Kafka集群的规模来增加其处理能力。
- **数据分区**：合理划分数据分区可以提高并行处理能力，从而减少消息积压。
- **数据清理**：定期清理过期的数据和日志文件，以释放磁盘空间并提高性能。
- **优化消费者代码**：检查消费者代码，确保它们是高效的。可能存在一些性能瓶颈或不必要的延迟。
- **调整Kafka配置**：根据需要调整Kafka的配置参数，例如增加分区数量、调整副本数量、调整日志清理策略等。
- **监控和警报**：设置监控系统，及时发现消息积压问题并发送警报。这样可以在问题出现之前采取行动。
- **故障排除**：检查系统日志，查找可能的问题源，并采取相应的措施解决问题。



kafka 要发现消息积压，可以考虑以下方法

- **监控工具**： Kafka 提供了一些监控工具，例如 Kafka Manager、Burrow、Kafka Offset Monitor 等。这些工具可以帮助你监控每个分区的偏移量（offset）和消费者组的状态。通过检查偏移量的增长速度，你可以判断是否有消息积压
- **Consumer Lag**： Consumer Lag 是指消费者组相对于生产者的消息偏移量的差异。通过监控 Consumer Lag，你可以了解消费者是 否跟上了生产者的速度。如果 Consumer Lag 增长较快，可能表示消息积压
- **Kafka Logs 目录**： Kafka 的每个分区都有一个日志目录，其中包含了该分区的消息数据。可以检查每个分区的日志目录，查看是否有 大量的未消费的消息
- **Kafka Broker Metrics**： Kafka 提供了一系列的 broker metrics，包括消息入队速率、出队速率等。通过监控这些指标，可以了解 Kafka 集群的负载状况
- **操作系统资源**： 如果 Kafka 所在的机器资源不足，可能导致消息积压。监控 CPU、内存、磁盘等系统资源，确保它们没有达到极限
- **警报系统**： 设置警报系统，当某些指标达到预定的阈值时触发警报，通知运维人员或相关团队及时处理



通过Kafka提供的工具查看格式：

```bash
#发现当前消费的offset和最后一条的offset差距很大,说明有大量的数据积压
kafka-consumer-groups.sh --bootstrap-server {kafka连接地址} --describe --group {消费组} | --all-groups
```

范例

```bash
#模拟生产者生产大量消息
[root@ubuntu2204 ~]#( while true; do echo $i;let i++;done ) | kafka-console-producer.sh --broker-list 
10.0.0.101:9092,10.0.0.102:9092,10.0.0.103:9092 --topic mystical

#下面命令查看消费组中每个Topic的堆积消息数。“LAG”表示每个Topic的总堆积数
[root@ubuntu2204 ~]#kafka-consumer-groups.sh --bootstrap-server 10.0.0.101:9092 --describe --all-groups
```



### Kafka工具

#### 图形工具 Offset Explorer (Kafka Tool)

![image-20250130220201790](D:\git_repository\cyber_security_learning\markdown_img\image-20250130220201790.png)

Offset Explorer ，旧称Kafka Tool，工具是一个 GUI 应用程序，用于管理和使用 Apache Kafka 群集。它提供了一个直观的 UI，允许人们快速查看 Kafka 群集中的对象以及存储在群集主题中的消息。它包含面向开发人员和管理员的功能。一些关键功能包括

- 快速查看您的所有 Kafka 集群，包括其经纪人、主题和消费者
- 查看分区中邮件的内容并添加新邮件
- 查看消费者的偏移量，包括阿帕奇风暴卡夫卡喷口消费者
- 以漂亮的打印格式显示 JSON和 XML 消息
- 添加和删除主题以及其他管理功能
- 将单个邮件从分区保存到本地硬盘驱动器
- 编写自己的插件，允许您查看自定义数据格式
- Kafka 工具在Windows、Linux 和 Mac 操作系统上运行



下载链接

```http
https://www.kafkatool.com/download.html
```

![image-20250130220548021](D:\git_repository\cyber_security_learning\markdown_img\image-20250130220548021.png)

下载安装后，直接连接（有代理的注意代理网络）

![image-20250131102147694](D:\git_repository\cyber_security_learning\markdown_img\image-20250131102147694.png)



### Kafka监控项

| Kafka集群 |                      |                                        |         |
| --------- | -------------------- | -------------------------------------- | ------- |
| 序号      | 指标别名             | 指标含义解释                           | 单位    |
| 1         | Partitions总数       | 集群中所有节点Partition数之和          | 个      |
| 2         | 未复制分区总数       | 集群中所有节点未复制分区数之和         | 个      |
| 3         | 离线分区总数         | 集群中所有节点离线分区数之和           | 个      |
| 4         | Controller存活数     | 集群中Controller存活的数量             | 个      |
| 5         | 失败请求（生产者）   | 集群中所有节点生产者失败请求的速率之和 | 次/s    |
| 6         | 失败请求（消费者）   | 集群中所有节点消费者失败请求的速率     | 次/s    |
| 7         | 生产者流量           | 集群中所有节点生产者流量之和           | Bytes/s |
| 8         | 消费者流量           | 集群中所有节点消费者流量之和           | Bytes/s |
| 9         | 生产者QPS            | 集群中所有节点生产者QPS之和            | 次/s    |
| 10        | 消费者QPS            | 集群中所有节点消费者QPS之和            | 次/s    |
| 11        | 存活节点数           | 集群中存活的节点数量                   | 个      |
| 12        | 每秒流入消息数       | 集群中所有节点流入消息数之和           | 个/s    |
| 13        | 最大CPU利用率        | 集群中所有节点CPU利用率最大值          |         |
| 14        | 最大内存利用率       | 集群中所有节点内存利用率最大值         |         |
| 15        | 最大Heap区利用率     | 集群中所有节点堆内存利用率最大值       |         |
| 16        | 最大Non-Heap区利用率 | 集群中所有节点非堆内存利用率最大值     |         |
| 17        | 最大Minor GC次数     | 集群中所有节点每分钟Minor GC次数最大值 |         |
| 18        | 最大Major GC次数     | 集群中所有节点每分钟Major GC次数最大值 |         |
| 19        | 最大Minor GC时间     | 集群中所有节点每分钟Minor GC时间       |         |
| 20        | 最大Major GC时间     | 集群中所有节点每分钟Major GC时间       |         |



### Kafka常见面试题

#### 说说kafka是怎样选举的

- 当新的分区创建时，Kafka选择ISR(In-Sync Replica)列表中的第一个副本作为领导者

- 当领导者发生故障

  - ZooKeeper将会检测到它的`会话过期`

  ```
  当Kafka broker启动时，会与Zookeeper建立一个会话，并定期发送心跳信号，保持会话的活跃状态
  Kafka broker会定期发送心跳到Zookeeper，告诉它自己还活着
  如果因为网路原因，broker故障等原因，Zookeeper在一定时间内（通常是几秒到几分钟的超时时间）没有收到broker的心跳信号，就会认为这个broker已经失效，称之为会话过期
  ```

  - Zookeeper会将该broker标记为失效，并通知其他相关组件
  - 如果失效的是某个分区的leader，Zookeeper会触发leader选举机制，从该分区的其他副本中选出一个新的leader

  ```java
  // Zookeeper维护了每个分区的ISR列表，该列表包含当前处于同步状态的副本
  // /brokers/topics/example-topic/partitions/0/state
  {
    "controller_epoch": 1,
    "leader": 1,
    "version": 1,
    "leader_epoch": 1,
    "isr": [1, 2, 3]
  }
  
  /brokers/topics/example-topic/partitions/1/state
  {
    "controller_epoch": 1,
    "leader": 2,
    "version": 1,
    "leader_epoch": 1,
    "isr": [2, 1, 3]
  }
  
  /brokers/topics/example-topic/partitions/2/state
  {
    "controller_epoch": 1,
    "leader": 3,
    "version": 1,
    "leader_epoch": 1,
    "isr": [3, 1, 2]
  }
  //从ISR列表中选择brokerID最小的副本作为新的leader
  List<Integer> isr = getIsrForPartition(partitionId);
  int newLeader = Collections.min(isr);  // 选择 ID 最小的副本作为新的 leader
  updatePartitionLeader(partitionId, newLeader);
  ```

  - Zookeeper会将新的leader信息通知Kafka集群中的其他brokers和相关消费者，让它们更新leader信息，继续处理消息

#### 说一下同步投递和重复消费

- 同步投递
  - 同步投递是Kafka中实现消息可靠性的重要机制, 但这种方式可能增加延迟和资源消耗，适用于对消息传递要求严格的场景
  - 其具体实现细节如下
    - 生产者先从集群获取分区的leader
      - 生产者初始化的时候，会连接到Kafka集群的一个或多个broker(通常称为bootstrap servers)
      - 生产者会向这些broker请求集群元数据信息，包括主题的分区信息和每个分区的leader副本
      - broker收到请求后会返回主题的分区信息，包括每个分区的leader副本和ISR列表
      - 生产者将这些元数据缓存到本地，以便在发送消息时快速查找每个分区的leader信息
    - 生产者将消息发送给leader副本
    - leader副本将消息写入本地日志文件
    - leader副本将消息传递给ISR列表中的所有follower副本
    - 每个follower副本将消息写入自己的本地日志文件
    - 每个foolower副本在成功写入消息后，发送确认给leader副本
    - 当leader副本收到所有ISR副本的确认后，向生产者发送确认消息
    - 生产者在接受到副本的确认后，才认为消息已成功发送

```shell
# acks配置
acks=0: 生产者不会等待任何确认。消息发送后立即返回。这种方式最快，但风险最大，因为消息可能丢失
acks=1: 生产者会等待leader副本确认消息写入日志后才返回，提供了一定可靠性，但是如果leader副本在消息传递给follower之前发生故障，消息可能会丢失。
acks=all(或-1): 生产者会等待所有ISRI(同步副本)确认消息写入后才返回。提供最高的可靠性（即同步投递）

# 关于同步投递的性能优化建议
为了在保证数据可靠性的同时优化性能，可以考虑以下建议：

配置优化：

调整 retries 和 retry.backoff.ms 参数，以适应实际的网络和系统状况，减少消息发送失败的重试次数。
配置 linger.ms 和 batch.size，通过批量发送消息来提高吞吐量。
集群扩展：

根据订单数据的量和并发要求，适当扩展 Kafka 集群，增加 broker 的数量和分区的数量，以提高系统的处理能力。
监控和调优：

通过监控 Kafka 集群的运行状态，及时发现和解决性能瓶颈和故障。
定期调优 Kafka 集群的配置，优化网络和存储性能，以适应不断增长的数据量和并发要求。
```

- 重复消费
  - 重复消费指消费者多次读取同一条信息。
  - 理解重复消费的前提知识
    - 偏移量(Offset)：偏移量是一个分区内每条消息的唯一标识，表示消息在分区日志中的位置，消费者通过偏移量来跟踪已消费的消费位置
    - 消费者可以从分区的起始偏移量(最早的消息)，或末尾偏移量开始消费
    - 偏移量主要由消费者管理，Kafka提供了机制来存储和检索偏移量，但具体的管理和提交由消费者负责
    - 消费者会定期调用`poll`方法，从Kafka中获取消息
    - 消费者维护它自己的消费进度，通过偏移量来跟踪它已经消费到哪条信息
    - 每次消费者拉取消息时，它会告诉Kafka从哪个偏移量开始读取消息，Kafka根据这个便宜量返回相应的消息
    - 消费者可以自动提交偏移量（由Kafka自动管理）或手动提交偏移量(由开发人员显式管理)
  - 重复消费的实现
    - 消费者使用自动提交偏移量，自动提交每5秒会将消费者的偏移量提交给Kafka，如果消费者处理消息的时候过长(或者消费者在处理完消息之前崩溃或重启)，超过这个时间，那么下次就会发生重复消费
  - 解决方法
    - 建议使用手动提交偏移量
    - 设计一些幂等性操作
    - 使用事务



## RabbitMQ

### RabbitMQ介绍

![image-20250117100208552](D:\git_repository\cyber_security_learning\markdown_img\image-20250117100208552.png)



**官网**

```http
https://www.rabbitmq.com/
```



RabbitMQ 基于 Erlang 语言开发，Erlang 语言由爱立信 Ericson 开发设计

Erlang语言在高并发,分布式编程和故障恢复方面表现优异，因此在电信领域被广泛使用



**Erlang版本和RabbitMQ版本的对应**

```http
https://www.rabbitmq.com/which-erlang.html
https://www.rabbitmq.com/docs/which-erlang
```



**RabbitMQ优势**

- 基于Erlang 语言开发，具有高并发优点、支持分布式
- 具有消息确认机制、消息持久化机制，消息可靠性和集群可靠性高、简单易用、运行稳定、跨平台、多语言
- 自带图形 Web 管理功能
- 开源



### RabbitMQ架构

![image-20250117100723696](D:\git_repository\cyber_security_learning\markdown_img\image-20250117100723696.png)



**Message:** 消息，消息是不具名的，它由消息头和消息体组成。消息体是不透明的，而消息头则由一系列的可选属性组成，这些属性包括 routing-key（路由键）、priority（相对于其他消息的优先权）、delivery-mode（指出该消息可能需要持久性存储）等。

**Publisher:** 消息的生产者，就是一个向交换器发布消息的客户端应用程序。

**Consumer:** 消息的消费者，表示一个从消息队列中取得消息的客户端应用程序。

**Broker:** 接收和分发消息的应用，表示消息队列服务器实体。**RabbitMQ Server 就是Message Broker。**

**Virtual host:** 为了支持多租户和安全原因，当多个不同的用户使用同一个RabbitMQ Server时，可以先划分出多个 vhost，每个用户使用独 立的vhost创建exchange／queue 等。每一个虚拟主机表示一批交换器、消息队列和相关对象的集合。虚拟主机是共享相同的身份认证和加 密环境的独立服务器域。每个 vhost 本质上就是一个 mini 版的 RabbitMQ 服务器，拥有自己的队列、交换器、绑定和权限机制。vhost 是 AMQP 概念的基础，必须在连接时指定，RabbitMQ 默认的 vhost 是 / 。

**Exchange:** 交换器，用来接收生产者发送的消息并将这些消息路由给服务器中的队列。message 到达 broker 会由Exchange 根据分发规 则，匹配查询表中的路由信息，分发消息到队列中。常用的类型：direct (point to poing 点对点),topic (publish subscribe发布者订阅者) 和 fanout (multicast多播)等

**Queue:** 消息队列，用来保存消息直到发送给消费者。它是消息的容器，也是消息的终点。一个消息可投入一个或多个队列。消息一直在队 列里面，等待消费者连接到这个队列将其取走。

**Binding:** 绑定，用于消息队列和交换器之间的关联。一个绑定就是基于路由键将交换器和消息队列连接起来的路由规则，所以可以将交换器 理解成一个由绑定构成的路由表。exchange 和 queue 之间的虚拟连接，binding 中可以包含 routing key。Binding 信息被保存到 exchange 中的查询表中，用于message 的分发依据。

**Connection:** 网络连接，比如一个TCP连接。publisher／consumer 和 broker 之间的TCP 连接。**（类似ssh的会话，每个会话独占一个TCP连接）**

**Channel:** 信道，多路复用连接中的一条独立的双向数据流通道。信道是建立在真实的TCP连接内部的虚拟连接，AMQP 命令都是通过信道 发出去的，不管是发布消息、订阅队列还是接收消息，这些动作都是通过信道完成。因为对于操作系统来说建立和销毁 TCP 都是非常昂贵的 开销，所以引入了信道的概念，以复用一条 TCP 连接。Channel 是在 connection内部建立的逻辑连接，如果应用程序支持多线程，通常每 个 thread创建单独的channel 进行通讯，AMQP method 包含了channel id 帮助客户端和messagebroker极大减少了操作系统建立TCP  connection 的开销**（类比ssh的隧道，一个会话可以有多个隧道，多个隧道共用一个TCP连接）**



### RabbitMQ 生产者消费者

![image-20250117101848248](D:\git_repository\cyber_security_learning\markdown_img\image-20250117101848248.png)



- 生产者发送消息到 broker server（RabbitMQ）
- 在 Broker 内部，用户创建Exchange／Queue，通过 Binding 规则将两者联系在一起
- Exchange 分发消息，根据类型／binding 的不同分发策略有区别
- 消息最后来到Queue 中，等待消费者取走。





### RabbitMQ 单机部署



#### 基于Docker部署RabbitMQ

```bash
[root@mystical ~]# docker run -d --name rabbitmq-single-node --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
Unable to find image 'rabbitmq:3-management' locally
3-management: Pulling from library/rabbitmq
de44b265507a: Pull complete 
609d1f44794c: Pull complete 
93bc35f205f7: Pull complete 
ae78677340ad: Pull complete 
f4546f4074da: Pull complete 
25a4431bdb90: Pull complete 
d18e4e86d7da: Pull complete 
fb48d524e912: Pull complete 
e7dfc1785660: Pull complete 
eb2c807d46cb: Pull complete 
Digest: sha256:29ded394fc8639f891e0c80fac7b8f594bb8edaa83e15dc8c5795ef8d6c15f6a
Status: Downloaded newer image for rabbitmq:3-management
765260f64c9d5bbd63a0e4f1ff466876a0fdcbf1f8a5e27e6c553adbe3998033


# 查看
[root@mystical ~]# docker ps
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS         PORTS                                                                                                                                                 NAMES
765260f64c9d   rabbitmq:3-management   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp, :::5672->5672/tcp, 15671/tcp, 15691-15692/tcp, 25672/tcp, 0.0.0.0:15672->15672/tcp, :::15672->15672/tcp   rabbitmq

# 访问浏览器：http://IP:15672
# 默认用户密码都是guest/guest
# 5672端口：客户端访问
# 15672端口：web访问
```



![image-20250117103535991](D:\git_repository\cyber_security_learning\markdown_img\image-20250117103535991.png)

![image-20250117103607691](D:\git_repository\cyber_security_learning\markdown_img\image-20250117103607691.png)







#### 基于包方式在Ubuntu 安装单机版 RabbitMQ

##### 主机名解析（可选）

早期版本安装必须做主机名解析,否则无法启动RabbitMQ服务,并且后续不能再修改主机名

**注意**: 当前版本不再有此限制

在当前MQ 服务器配置本地主机名解析

```bash
[root@mystical ~]# hostnamectl set-hostname rabbitmq.mystical.org

[root@mystical ~]# vim /etc/hosts
10.0.0.151 rabbitmq.mystical.org rabbitmq
```



##### 系统内置仓库安装

```bash
[root@mystical ~]# apt list |grep -i rabbitmq

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

kamailio-rabbitmq-modules/jammy 5.5.4-1 amd64
libanyevent-rabbitmq-perl/jammy 1.22~dfsg-1 all
libmojo-rabbitmq-client-perl/jammy 0.3.1-2 all
libmono-messaging-rabbitmq4.0-cil/jammy 6.8.0.105+dfsg-3.2 all
libmono-rabbitmq4.0-cil/jammy 6.8.0.105+dfsg-3.2 all
librabbitmq-client-java/jammy 5.0.0-1.1 all
librabbitmq-dev/jammy 0.10.0-1ubuntu2 amd64
librabbitmq4/jammy 0.10.0-1ubuntu2 amd64
nagios-plugins-rabbitmq/jammy 1:1.2.0-2.2ubuntu1 all
puppet-module-puppetlabs-rabbitmq/jammy 8.5.0-7 all
rabbitmq-server/jammy-updates 3.9.27-0ubuntu0.1 all

[root@mystical ~]# apt install -y rabbitmq-server
```



##### 官方仓库脚本包安装指定较新版本

```http
https://www.rabbitmq.com/docs/install-debian#apt-quick-start-cloudsmith
```





![image-20250117104808492](D:\git_repository\cyber_security_learning\markdown_img\image-20250117104808492.png)



```bash
# Ubuntu2204

#!/bin/sh

sudo apt update && apt-get install curl gnupg apt-transport-https -y

## Team RabbitMQ's main signing key
curl -1sLf "https://keys.openpgp.org/vks/v1/by-fingerprint/0A9AF2115F4687BD29803A206B73A36E6026DFCA" | sudo gpg --dearmor | sudo tee /usr/share/keyrings/com.rabbitmq.team.gpg > /dev/null

## Community mirror of Cloudsmith: modern Erlang repository
curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg > /dev/null

## Community mirror of Cloudsmith: RabbitMQ repository
curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.9F4587F226208342.gpg > /dev/null

## Add apt repositories maintained by Team RabbitMQ
sudo tee /etc/apt/sources.list.d/rabbitmq.list <<EOF
## Provides modern Erlang/OTP releases
##
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.rabbitmq.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.rabbitmq.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main

# another mirror for redundancy
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.rabbitmq.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.rabbitmq.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main

## Provides RabbitMQ
##
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.rabbitmq.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.rabbitmq.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main

# another mirror for redundancy
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.rabbitmq.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.rabbitmq.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
EOF

## Update package indices
sudo apt-get update -y

## Install Erlang packages
sudo apt-get install -y erlang-base \
                        erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets \
                        erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key \
                        erlang-runtime-tools erlang-snmp erlang-ssl \
                        erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl

## Install rabbitmq-server and its dependencies
sudo apt-get install rabbitmq-server -y --fix-missing
```





#### 二进制安装RabbitMQ

**通用二进制安装官方说明**

```http
https://www.rabbitmq.com/install-generic-unix.html
```



**RabbitMQ版本和Erlang版本对应要求**

```http
https://www.rabbitmq.com/which-erlang.html
```



**RabbitMQ和Erlang各版本二进制tar包下载**

```bash
# RabbitMQ:
https://github.com/rabbitmq/rabbitmq-server

# Erlang:
https://github.com/erlang/otp/releases
```





**范例：二进制安装一键安装脚本**

```bash
#!/bin/bash

RABBITMQ_VERSION=3.13.7
OPT_VERSION=26.2.5.1
INSTALL_DIR="/usr/local/rabbitmq"

SRC_DIR=`pwd`
CPUS=`grep -c processor /proc/cpuinfo`
GREEN="echo -e \E[32;1m"
END="\E[0m"
HOST=`hostname -I|awk '{print $1}'`

. /etc/os-release

color () {
    RES_COL=60
    MOVE_TO_COL="echo -en \\033[${RES_COL}G"
    SETCOLOR_SUCCESS="echo -en \\033[1;32m"
    SETCOLOR_FAILURE="echo -en \\033[1;31m"
    SETCOLOR_WARNING="echo -en \\033[1;33m"
    SETCOLOR_NORMAL="echo -en \E[0m"
    echo -n "$1" && $MOVE_TO_COL
    echo -n "["
    if [ $2 = "success" -o $2 = "0" ] ;then
        ${SETCOLOR_SUCCESS}
        echo -n $" OK "    
    elif [ $2 = "failure" -o $2 = "1" ] ;then
        ${SETCOLOR_FAILURE}
        echo -n $"FAILED"
    else
        ${SETCOLOR_WARNING}
        echo -n $"WARNING"
    fi
    ${SETCOLOR_NORMAL}
    echo -n "]"
    echo
}

install_erlang() {

   apt update
   apt -y install gcc build-essential make ncurses-dev libssl-dev libncurses5-dev libwxgtk3.0-gtk3-dev libalien-wxwidgets-perl pkg-config default-jdk unixodbc unixodbc-dev g++ xsltproc fop libxml2-utils socat || { color "安装相关包失败!" 1;exit; }
   [ -e otp_src_${OPT_VERSION}.tar.gz ] || { color "otp-src-${OPT_VERSION}.tar.gz 文件不存在!" 1;wget https://mirror.ghproxy.com/https://github.com/erlang/otp/releases/download/OTP-${OPT_VERSION}/otp_src_${OPT_VERSION}.tar.gz ; }
   tar xf otp_src_${OPT_VERSION}.tar.gz -C /usr/local
    cd /usr/local/otp_src_${OPT_VERSION}
   ./configure --prefix=/apps/erlang \
            --enable-kernel-poll \
            --enable-threads \
            --enable-smp-support \
            --enable-dirty-schedulers \
            --with-ssl=/usr \
            --enable-dynamic-ssl-lib \
            --enable-sharing-of-heap \
            --enable-hipe \
            --enable-escript
    make -j $CPUS && make install 
    echo 'PATH=/apps/erlang/bin:$PATH' >> /etc/profile
    ln -s /apps/erlang/bin/* /usr/bin/
}

install_rabbitmq() {
    cd $SRC_DIR
   [ -e rabbitmq-server-generic-unix-${RABBITMQ_VERSION}.tar.xz ] || { color "rabbitmq-server-genericunix-${RABBITMQ_VERSION}.tar.xz 文件不存在!" 1;wget https://mirror.ghproxy.com/https://github.com/rabbitmq/rabbitmq-server/releases/download/v${RABBITMQ_VERSION}/rabbitmq-server-generic-unix-${RABBITMQ_VERSION}.tar.xz; }
   tar xf rabbitmq-server-generic-unix-${RABBITMQ_VERSION}.tar.xz -C /usr/local/
   [ -e `dirname ${INSTALL_DIR}` ] || mkdir `dirname ${INSTALL_DIR}`
    ln -s /usr/local/rabbitmq_server-${RABBITMQ_VERSION}  ${INSTALL_DIR}
    ln -s ${INSTALL_DIR}/sbin/* /usr/sbin/
    useradd -r -m rabbitmq
    chown -R rabbitmq.rabbitmq ${INSTALL_DIR}/
    
    cat > /lib/systemd/system/rabbitmq-server.service <<EOF
# systemd unit example
[Unit]
Description=RabbitMQ broker
After=network.target epmd@0.0.0.0.socket
Wants=network.target epmd@0.0.0.0.socket
[Service]
Type=notify
User=rabbitmq
Group=rabbitmq
UMask=0027
NotifyAccess=all
TimeoutStartSec=600
# To override LimitNOFILE, create the following file:
#
# /etc/systemd/system/rabbitmq-server.service.d/limits.conf
#
# with the following content:
#
# [Service]
# LimitNOFILE=65536
LimitNOFILE=32768
# The following setting will automatically restart RabbitMQ
# in the event of a failure. systemd service restarts are not a
# replacement for service monitoring. Please see
# https://www.rabbitmq.com/monitoring.html
Restart=on-failure
RestartSec=10
#WorkingDirectory=/var/lib/rabbitmq
ExecStart=${INSTALL_DIR}/sbin/rabbitmq-server
ExecStop=${INSTALL_DIR}/sbin/rabbitmqctl shutdown
# See rabbitmq/rabbitmq-server-release#51
SuccessExitStatus=69
[Install]
WantedBy=multi-user.target
EOF
   systemctl daemon-reload
   systemctl enable rabbitmq-server.service
}

config_rabbitmq(){
    rabbitmq-plugins enable rabbitmq_management
    echo  "loopback_users = none" > ${INSTALL_DIR}/etc/rabbitmq/rabbitmq.conf 
    systemctl restart rabbitmq-server.service
}

start_rabbitmq() { 
   systemctl is-active rabbitmq-server.service    
    if [ $?  -eq 0 ];then  
        echo
       color "RabbitMQ安装完成!" 0
        echo "-------------------------------------------------------------------"
        echo -e "访问链接: \c"
        ${GREEN}"http://${HOST}:15672/"${END}
        echo -e "用户和密码: \c"
 ${GREEN}"guest/guest"${END}
    else
       color "RabbitMQ安装失败!" 1
        exit
    fi
}


install_erlang
install_rabbitmq
config_rabbitmq
start_rabbitmq
```



### RabbitMQ管理

#### 启用远程登录Web管理页面

##### RabbitMQ 插件管理说明

**官方文档：**

```http
https://www.rabbitmq.com/management.html
```



**端口说明：**

```bash
5672   #客户端访问的端口
15672  #web 管理端口,默认没有打开,需要启用插件
25672  #集群状态通信端口
```



##### 安装Web管理插件rabbitmq_management

```bash
# 添加web管理插件
[root@mystical /apps/erlang/bin]# rabbitmq-plugins enable rabbitmq_management
Enabling plugins on node rabbit@mystical:
rabbitmq_management
The following plugins have been configured:
  rabbitmq_management
  rabbitmq_management_agent
  rabbitmq_web_dispatch
Applying plugin configuration to rabbit@mystical...
The following plugins have been enabled:
  rabbitmq_management
  rabbitmq_management_agent
  rabbitmq_web_dispatch

set 3 plugins.
Offline change; changes will take effect at broker restart.

# 重启服务
[root@mystical /apps/erlang/bin]# systemctl restart rabbitmq-server.service

# 可以看到15762/tcp端口打开
[root@mystical /apps/erlang/bin]# ss -nlt
State       Recv-Q      Send-Q             Local Address:Port              Peer Address:Port      Process   
LISTEN      0           1024                     0.0.0.0:15672                  0.0.0.0:*                   
LISTEN      0           4096                     0.0.0.0:4369                   0.0.0.0:*                   
LISTEN      0           128                      0.0.0.0:22                     0.0.0.0:*                   
LISTEN      0           128                      0.0.0.0:25672                  0.0.0.0:*                   
LISTEN      0           4096                     127.0.0.53%lo:53               0.0.0.0:*    

#开启插件本质修改了如下文件
[root@mq-server ~]#cat /etc/rabbitmg/enabled plugins
[rabbitmg management]

# 注意: rabbitmq 从 3.3.0 开始禁止使用guest/guest 权限通过除localhost外的访问，直接访问报错
# 因此需要开启用户 guest 远程登录功能
```



#####  开启用户 guest 远程登录功能

```bash
[root@mystical ~]# ls /etc/rabbitmq/
enabled_plugins

#创建配置文件开启远程登录功能
[root@mystical ~]# echo "loopback_users = none" > /etc/rabbitmq/rabbitmq.conf 
[root@mystical ~]# systemctl restart rabbitmq-server.service

#如果多台主机需要打开远程Web访问功能，可以将两个文件同步到其它主机
[root@mq-server ~]#scp /etc/rabbitmq/* 10.0.0.101:/etc/rabbitmq/
root@10.0.0.101's password: 
enabled_plugins                                                  100%   23    55.1KB/s   00:00    
rabbitmq.conf                                                    100%   22    34.6KB/s   00:00 

#再次用户guest远程登录验证
```

![image-20250117173542516](D:\git_repository\cyber_security_learning\markdown_img\image-20250117173542516.png)



#### 修改guest密码

![image-20250117173638076](D:\git_repository\cyber_security_learning\markdown_img\image-20250117173638076.png)



![image-20250117173740711](D:\git_repository\cyber_security_learning\markdown_img\image-20250117173740711.png)

![image-20250117173838985](D:\git_repository\cyber_security_learning\markdown_img\image-20250117173838985.png)



#### 创建新用户

上面可以设置guest用户远程登录,但基于安全起见建议创建新的管理用户

```bash
# 查看用户
[root@mystical ~]# rabbitmqctl list_users
Listing users ...
user	tags
guest	[administrator]

# 可能出现的报错
[root@mystical ~]# rabbitmqctl cluster_status
Error: unable to perform an operation on node 'rabbit@mystical'. Please see diagnostics information and suggestions below.

# 出错原因：Erlang Cookie不一致 或者 host主机名和节点名称不一致
# 解决方案：
# 包安装：确保两个文件内容一致
cat /var/lib/rabbitmq/.erlang.cookie
cat ~/.erlang.cookie

# 编译安装，确保下面两个文件内容一致
[root@mystical ~]# find / -name '.erlang.cookie'
/home/rabbitmq/.erlang.cookie
/root/.erlang.cookie

[root@mystical ~]# cp /home/rabbitmq/.erlang.cookie ~/.erlang.cookie

# 重启服务
[root@mystical ~]# systemctl restart rabbitmq-server.service 
```

#### 管理用户

```bash
# 创建用户
[root@mystical ~]# rabbitmqctl add_user admin 123456
Adding user "admin" ...
Done. Don't forget to grant the user permissions to some virtual hosts! See 'rabbitmqctl help set_permissions' to learn more.

# 查看用户
[root@mystical ~]# rabbitmqctl list_users
Listing users ...
user	tags
admin	[]
guest	[administrator]

# 修改密码
[root@mystical ~]# rabbitmqctl change_password admin 646130
Changing password for user "admin" ...

# 加入管理员角色，可以登录Web管理页面进行管理，但仍然无法访问virtual hosts,需要授权才可以
[root@mystical ~]# rabbitmqctl set_user_tags admin administrator
Setting tags for user "admin" to [administrator] ...

# 查看
[root@mystical ~]# rabbitmqctl list_users
Listing users ...
user	tags
admin	[administrator]
guest	[administrator]

# 设置vhost权限，格式如下
rabbitmqctl [--node <node>] [--longnames] [--quiet] set_permissions [--vhost <vhost>] <username> <conf> 
<write> <read>

# 设置对vhost “/” 给admin用户授予:configure配置，write写，read读的权限，“.*”表示正则表达式的任意字符串
# 默认vhost为 "/"

# 示例
[root@mystical ~]# rabbitmqctl set_permissions [--vhost /] admin ".*" ".*" ".*"
Setting permissions for user "admin" in vhost "/" ...

# 验证权限
[root@mystical ~]# rabbitmqctl list_user_permissions admin
Listing permissions for user "admin" ...
vhost	configure	write	read
/	.*	.*	.*

# 给指定vhost设置权限
```

#### 删除用户

```bash
[root@mq-server ~]#rabbitmqctl list_users
Listing users ...
user tags
admin [administrator]
wang [administrator]
guest [administrator]

[root@mq-server ~]#rabbitmqctl delete_user wang
Deleting user "wang" ...
```



#### 创建vhost

![image-20250118092128743](D:\git_repository\cyber_security_learning\markdown_img\image-20250118092128743.png)

![image-20250118092621666](D:\git_repository\cyber_security_learning\markdown_img\image-20250118092621666.png)



**命令行操作vhost**

```bash
[root@mystical ~]# rabbitmqctl 
......
Virtual hosts:

   add_vhost                                     Creates a virtual host
   clear_vhost_limits                            Clears virtual host limits
   delete_vhost                                  Deletes a virtual host
   list_vhost_limits                             Displays configured virtual host limits
   reconcile_vhosts                              Makes sure all virtual hosts were initialized on all                                                        reachable cluster nodes
   restart_vhost                                 Restarts a failed vhost data stores and queues
   set_vhost_limits                              Sets virtual host limits
   set_vhost_tags                                Sets virtual host tags
   trace_off                                     
   trace_on                                      
   update_vhost_metadata                         Updates metadata (tags, description, default queue type) a                                                  virtual host

......
```



#### 创建Queue

**Queue类似于Kafka的Topic，后续可以向里面写入数据**

![image-20250118093126680](D:\git_repository\cyber_security_learning\markdown_img\image-20250118093126680.png)



**Durability字段解析**

- **Durable**：

  - 队列是持久化的。

  - 即使 RabbitMQ 服务重启，队列仍然会保留。

  - 队列的元数据存储在磁盘上，而不是仅保存在内存中。

- **Transient**：

  - 队列是非持久化的。

  - 当 RabbitMQ 服务重启时，队列会被删除。

  - 队列的元数据仅存储在内存中。

- **Durable 参数的作用**

  - `Durable` 参数是在声明队列时指定的，其主要目的是控制队列是否在 RabbitMQ 服务重启后保留。

  - **设置 Durable 为 true**：
    - 队列的元数据会被存储到磁盘。
    - 在服务重启后，队列依然存在。

  - **设置 Durable 为 false**：
    - 队列仅存在于内存中。
    - 如果 RabbitMQ 服务重启，队列会丢失。

- **消息持久化 vs 队列持久化**
  - 需要注意的是，**队列的持久化**（通过 `Durable` 参数设置）和**消息的持久化**是两个不同的概念：
  - **队列持久化**：
    - 队列的元数据存储到磁盘。
    - 通过声明队列时设置 `Durable=true`。
  - **消息持久化**：
    - 消息存储到磁盘。
    - 需要在消息发布时，将消息的 `delivery_mode` 属性设置为 2（持久化）。
  - **持久化队列不等于持久化消息**：
    - 即使队列是持久化的，如果消息没有设置持久化属性，服务重启后消息仍然会丢失。
    - 反之，若队列是非持久化的，即使消息设置了持久化，服务重启后消息也会丢失。

```ABAP
生产环境通常会设置队列为持久化（Durable=true），并确保消息的 delivery_mode=2，以实现高可靠性数据传输。
```







### Python客户端访问RabbitMQ

#### 生产者（producter）

队列消息的产生者，负责生产消息，并将消息传入队列

```bash
[root@mystical ~]# apt install -y python3 python3-pip

# 加速配置
[root@mystical ~]# python3 -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
Writing to /root/.config/pip/pip.conf

# 下载pika模块
[root@mystical ~]# pip3 install pika
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting pika
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/f9/f3/f412836ec714d36f0f4ab581b84c491e3f42c6b5b97a6c6ed1817f3c16d0/pika-1.3.2-py3-none-any.whl (155 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.4/155.4 KB 7.4 MB/s eta 0:00:00
Installing collected packages: pika
Successfully installed pika-1.3.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```

```python
import pika
import json

username = 'guest'
password = 'guest'
host = '127.0.0.1'
port = 5672

def publish_messages():
   credentials = pika.PlainCredentials(username, password)
   connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, virtual_host='/', 
credentials=credentials))
   channel = connection.channel()
    
   queue_name = 'new_test'
   channel.queue_declare(queue=queue_name)
    
   for i in range(10):
       message = json.dumps({'OrderId': f"1000{i}"})
       channel.basic_publish(exchange='', routing_key=queue_name, body=message)
       print(message)
        
   connection.close()

if __name__ == "__main__":
   publish_messages()
```

```bash
# 运行脚本
[root@mystical ~]# python3 rabbitmq_product.py 
{"OrderId": "10000"}
{"OrderId": "10001"}
{"OrderId": "10002"}
{"OrderId": "10003"}
{"OrderId": "10004"}
{"OrderId": "10005"}
{"OrderId": "10006"}
{"OrderId": "10007"}
{"OrderId": "10008"}
{"OrderId": "10009"}
```

![image-20250118095737801](D:\git_repository\cyber_security_learning\markdown_img\image-20250118095737801.png)



#### 消费者（consumer）

```python
import pika

# Define MQ parameters
username = 'guest'
password = '123456'
host = '10.0.0.150'
port = 5672

def consume_messages():
   credentials = pika.PlainCredentials(username, password)
   connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, virtual_host='/', credentials=credentials))
   channel = connection.channel()

   channel.queue_declare(queue='new_test', durable=False)
    
   def callback(ch, method, properties, body):
       print(body.decode())
       ch.basic_ack(delivery_tag=method.delivery_tag)
    
   channel.basic_consume(queue='new_test', on_message_callback=callback, auto_ack=False)

   channel.start_consuming()
    
if __name__ == "__main__":
   consume_messages()
```



**查看队列和删除**

```bash
# 查看队列
[root@mystical ~]# rabbitmqctl list_queues
Timeout: 60.0 seconds ...
Listing queues for vhost / ...
name	messages
new_test	0
rabbit-test 10
test	0

# 删除队列
[root@mystical ~]# rabbitmqctl delete_queue new_test
Deleting queue 'new_test' on vhost '/' ...
Queue was successfully deleted with 0 ready messages

#清空队列
[root@mystical ~]# rabbitmqctl purge_queue rabbit-test
Purging queue 'rabbit-test' in vhost '/' ...

# 再次查看
[root@mq-server ~]#rabbitmqctl list_queues
Timeout: 60.0 seconds ...
Listing queues for vhost / ...
name messages
rabbit-test 0
```



### RabbitMQ集群部署

#### RabbitMQ集群模式

RabbitMQ集群模式分为两种:普通和镜像模式

- **普通集群模式：**
  - 创建好RabbitMQ集群之后的默认模式
  - queue 创建之后，如果没有其它policy，消息实体只存在于其中一个节点
  - 假设 A、B 两个 Rabbitmq节点仅有相同的元数据，即队列结构，但队列的数据仅保存有一份，即创建该队列的rabbitmq节点（A 节 点）
  - 当消息进入 A 节点的 Queue 中后，consumer 从 B节点拉取时，RabbitMQ 会临时在 A、B 间进行消息传输，把 A中的消息实体取出 并经过 B 发送给consumer，所以 consumer可以连接每一个节点，从中取消息
  - 该模式存在一个问题就是当 A 节点故障后，B节点无法取到A 节点中还未消费的消息实体。可能会丢失数据
  - **缺点： 没有数据高可用**
  - **优点：多个节点可以实现负载均衡**



- **镜像集群模式：** 
  - 把需要的队列做成镜像队列，存在于多个节点，属于 RabbitMQ 的 HA方案（镜像模式是在普通模式的基础上，增加一些镜像策略）
  - 该模式解决了普通模式中的数据丢失问题，其实质和普通模式不同之处在于，消息实体会主动在镜像节点间同步，而不是在consumer 取数据时临时拉取
  - 该模式带来的副作用也很明显，除了降低系统性能外，如果镜像队列数量过多，加之大量的消息进入，集群内部的网络带宽将会被这种 同步通讯大大消耗掉，所以在对可靠性要求较高的场合中适用
  - 一个队列想做成镜像队列，需要先设置policy， 然后客户端创建队列的时候，rabbitmq集群根据“队列名称”自动设置是普通集群模式或 镜像队列
  - **优点：此模式因数据有冗余,比较常用**
  - **缺点：性能不佳**



- **集群中两种节点类型:**
  - 内存节点：只将数据保存到内存
  - 磁盘节点：保存数据到内存和磁盘。

```ABAP
内存节点执行效率比磁盘节点要高，集群中只需要一个磁盘节点来保存数据就可以
如果集群中只有内存节点，那么不能全部停止它们，否则所有数据消息在服务器全部停机之后都会丢失。
```



 **推荐设计架构**

在一个rabbitmq 集群里，有 3 台或以上机器，其中 1台使用磁盘模式，其它节点使用内存模式，内存节点访问速度更快，由于磁盘IO相对 较慢，因此可作为数据备份使用。



#### 安装RabbitMQ集群

##### 环境准备

集群节点之间通信依赖主机名，每个节点需要有唯一的主机名

集群环境准备三台服务器，不同节点需要指定的主机名

```bash
[root@ubuntu1804 ~]#hostnamectl set-hostname node1.wang.org
[root@ubuntu1804 ~]#hostnamectl set-hostname node2.wang.org
[root@ubuntu1804 ~]#hostnamectl set-hostname node3.wang.org

[root@node1 ~]#cat >> /etc/hosts <<EOF
10.0.0.101 node1.wang.org node1
10.0.0.102 node2.wang.org node2
10.0.0.103 node3.wang.org node3
EOF

[root@node1 ~]#scp /etc/hosts node2:/etc/hosts
[root@node1 ~]#scp /etc/hosts node3:/etc/hosts
```



##### 各节点分别安装RabbitMQ并启用Web管理

```bash
# 下载rabbitmq
[root@node1 ~]# wget https://www.mysticalrecluse.com/script/tools/rabbitmq-server-generic-unix-3.13.7.tar.xz
[root@node1 ~]# wget https://www.mysticalrecluse.com/script/tools/otp_src_26.2.5.1.tar.gz

# 下载RabbitMQ安装脚本
[root@node1 ~]# wget https://www.mysticalrecluse.com/script/Shell/install_rabbitmq.sh

# 访问IP:15672,验证各个节点都可以用guest/guest登录
```

![image-20250118115201944](D:\git_repository\cyber_security_learning\markdown_img\image-20250118115201944.png)



##### 同步 cookie 文件

RabbitMQ 的集群是依赖于 erlang 的集群来工作的，所以必须先构建起 erlang的集群环境

而 Erlang 的集群中各节点是通过一个 magic cookie来实现的

这个 cookie 存放在 `/var/lib/rabbitmq/.erlang.cookie` 中，编译安装是在`/home/rabbitmq/.erlang.cookie`

文件是 400的权限,所以必须保证各节点cookie 保持一致，否则节点之间就无法通信。

```bash
[root@node1 ~]# ll /home/rabbitmq/.erlang.cookie 
-r-------- 1 rabbitmq rabbitmq 20 Jan 18 00:00 /home/rabbitmq/.erlang.cookie

[root@node1 ~]# cat /home/rabbitmq/.erlang.cookie 
QQYNWDZEONWPFROEDSFM

[root@node1 ~]# scp /home/rabbitmq/.erlang.cookie node2:/home/rabbitmq/.erlang.cookie
.erlang.cookie                                                               100%   20    61.7KB/s   00:00    
[root@node1 ~]# scp /home/rabbitmq/.erlang.cookie node3:/home/rabbitmq/.erlang.cookie
.erlang.cookie                                                               100%   20    54.2KB/s   00:00 

# 重启服务生效
[root@node1 ~]# systemctl restart rabbitmq-server.service
[root@node2 ~]# systemctl restart rabbitmq-server.service
[root@node3 ~]# systemctl restart rabbitmq-server.service
```



##### 创建集群

```bash
# 在 node2,node3 节点执行以下命令作为内存节点添加到 node1 所在集群
# 将 node2 加入集群
[root@node2 ~]# rabbitmqctl stop_app                    # 停止app服务
Stopping rabbit application on node rabbit@node2 ...

[root@node2 ~]# rabbitmqctl reset                       # 清空元数据
Resetting node rabbit@node2 ...

#将node2添加到集群当中，并成为内存节点，不加--ram 默认是磁盘节点,此步依赖于/etc/hosts的名称解析
[root@node2 ~]# rabbitmqctl join_cluster rabbit@node1 --ram
Clustering node rabbit@node2 with rabbit@node1

# 启动app服务
[root@node3 ~]# rabbitmqctl start_app
Starting node rabbit@node3 ...

# 将 node3 加入集群
[root@node3 ~]# rabbitmqctl stop_app
Stopping rabbit application on node rabbit@node3 ...

[root@node3 ~]# rabbitmqctl reset
Resetting node rabbit@node3 ...

[root@node3 ~]# rabbitmqctl join_cluster rabbit@node1 --ram
Clustering node rabbit@node3 with rabbit@node1

[root@node3 ~]# rabbitmqctl start_app
Starting node rabbit@node3 ...
```

![image-20250118120333681](D:\git_repository\cyber_security_learning\markdown_img\image-20250118120333681.png)



##### 将集群设置为镜像模式

创建的集群默认为普通模式,没有冗余性,可以修改为镜像模式

```bash
# 命令说明
rabbitmqctl set_policy [-p Vhost] Name Pattern Definition [Priority]

# 参数说明
-p Vhost                # 可选参数，针对指定vhost下的queue进行设置
Name                    # policy的名称
Pattern                 # queue的匹配模式(正则表达式)
Definition              # 镜像定义，包括三个部分ha-mode, ha-params, ha-sync-mode
ha-mode                 #指明镜像队列的模式，有效值为 all/exactly/nodes
all                     # 表示在集群中所有的节点上进行镜像
exactly                 # 表示在指定个数的节点上进行镜像，节点的个数由ha-params指定
nodes                   # 表示在指定的节点上进行镜像，节点名称通过ha-params指定
ha-params               # ha-mode模式需要用到的参数
ha-sync-mode            # 进行队列中消息的同步方式，有效值为automatic和manual
priority                # 可选参数，policy的优先级
```

默认模式为普通模式,无数据冗余功能,可以通过设置镜像模式,实现集群的高可用性功能

```bash
#在任意一个节点执行一次下面操作即可
[root@node1 ~]# rabbitmqctl set_policy ha-all "^" '{"ha-mode":"all"}'
Setting policy "ha-all" for pattern "^" to "{"ha-mode":"all"}" with priority "0" for vhost "/" ...

# 查看
[root@node1 ~]# rabbitmqctl list_policies
Listing policies for vhost "/" ...
vhost	name	pattern	apply-to	definition	priority
/	ha-all	^	all	{"ha-mode":"all"}	0
```



##### 验证镜像模式

```bash
#在任意节点创建用户并设置权限,会自动同步至其它节点
[root@node1 ~]# rabbitmqctl add_user mystical 123456
Adding user "mystical" ...
Done. Don't forget to grant the user permissions to some virtual hosts! See 'rabbitmqctl help set_permissions' to learn more.

[root@node1 ~]# rabbitmqctl set_user_tags mystical administrator
Setting tags for user "mystical" to [administrator] ...

[root@node1 ~]# rabbitmqctl set_permissions mystical ".*" ".*" ".*" 
Setting permissions for user "mystical" in vhost "/" ...

[root@node1 ~]# rabbitmqctl list_users
Listing users ...
user	tags
mystical	[administrator]
guest	[administrator]

# 在任何其他节点上查看用户信息
[root@node2 ~]# rabbitmqctl list_users
Listing users ...
user	tags
mystical	[administrator]
guest	    [administrator]
```





## MINIO



**内容概述**

- **MINIO 介绍**
- **MINIO 部署**
- **MINIO 使用**
- **MINIO 故障恢复**
- **MINIO 扩容和缩容**
- **MINIO 备份和还原**
- **MINIO 监控**



### MINIO介绍

![image-20250118123718005](D:\git_repository\cyber_security_learning\markdown_img\image-20250118123718005.png)

MinIO 是GlusterFS创始人之一Anand Babu Periasamy发布的新的开源项目。

MinlO 是一个**用 GoLang 语言开发**的基于 **GNU AGPL v3** 开源协议的对象存储服务(Object Storage  Service, OSS)

对象存储服务是一种海量、安全、低成本、高可靠的云存储服务，适合存放任意类型的文件。

对象存储服务支持容量和处理能力弹性扩展，多种存储类型供选择，全面优化存储成本。

MinlO **兼容亚马逊S3云存储服务接口**，非常适合于存储大容量非结构化的数据，例如:图片、视频、日志 文件、备份数据和容器/虚拟机镜像等

MinlO 支持的一个对象文件可以是任意大小，从几kb到最大5T不等

MinlO 是一个非常轻量的服务， 可以很简单的和其他应用的结合,也支持各种操作系统,比 如:Linux,Windows,Mac等

**对于中小型企业的对象存储**，如果不选择公有云存储，那么Minio是个不错的选择

MinIO 除了直接作为对象存储使用,还可以作为云上对象存储服务的网关层，无缝对接到Amazon S3、 MicroSoft Azure。



**MINIO特点**

- MinIO 提供高性能、与S3 兼容的对象存储系统，让你自己能够构建自己的云储存服务。
- MinIO 使用和部署非常简单，可以让您在最快的时间内实现下载到生产环境的部署。
- MinIO 读写性能优异,高性能MinIO 是世界上最快的对象存储，没有之一。在 32 个 NVMe 驱动器节点和 100Gbe 网络上发布的 GET/PUT 结果超过 325 GiB/秒和 165 GiB/秒
- MinIO 支持的对象文件小到几kb到最大5T,并实现了数据的高可用
- MinIO 原生支持 Kubernetes，它可用于每个独立的公共云、每个 Kubernetes 发行版、私有云和 边缘的对象存储套件
- MinIO 是软件定义的，不需要购买其他任何硬件，在 GNU AGPL v3 下是 100% 开源的



**MINIO性能**

```ABAP
节点越多，性能越好
```

![image-20250118152114187](D:\git_repository\cyber_security_learning\markdown_img\image-20250118152114187.png)



### MINIO工作机制

#### MINIO相关术语

- **0bject 对象**
  - 存储到Minio的基本对象,如文件、字节流等任意数据
- **Bucket 桶**
  - 用来存储Object的逻辑空间。
  - 每个Bucket之间的数据是相互隔离的。
  - 对于客户端而言，就相当于一个存放文件的顶层文件夹，用于实现不同资源的分类存储
  - 通常一个项目或同一类资源可以对应于一个Bucket
- **Drive 驱动器**
  - 即存储数据的磁盘,**一个Drive通常对应一块物理磁盘**或者一个独立目录
  - **在MinIO启动时，以参数的方式传入**
  - Minio 中所有的对象数据都会存储在Drive里
- **Set 存储集**
  - 一组Drive的集合,即一组相关的磁盘的集合
  - 分布式部署时,MinIO会根据集群规模自动划分一个或多个Set，每个Set中的Drive分布在不同位置。
  - 一个对象存储在一个Set上
  - 一个集群划分为多个Set
  - 一个Set包含的Drive数量是固定的， 默认由系统根据集群规模自动计算得出
  - 一个Set中的Drive尽可能分布在不同的节点上



####  纠删码EC（Erasure Code）

分布式存储，很关键的点在于数据的可靠性，即保证数据的完整,不丢失，不损坏。只有在可靠性实现的 前提下，才有了追求一-致性、高可用、高性能的基础。而对于在存储领域，一 般对于保证数据可靠性的 方法主要有两类，一类是**冗余法**，一 类是**校验法**。



- **冗余法**
  - 冗余法即对存储的数据进行副本备份，当数据出现丢失，损坏，即可使用备份内容进行恢复，而副 本备份的多少，决定了数据可靠性的高低。这其中会有成本的考量，副本数据越多，数据越可靠， 但需要的设备就越多，成本就越高。可靠性是允许丢失其中一份数据。
  - 当前有很多分布式系统采用此种方式实现，如：ELasticsearch的索引副本，Kafka的副本，Redis 的集群，MySQL的主从模式，Hadoop的多副本的文件系统
- **校验法**
  - 校验法即通过校验码的数学计算的方式，对出现丢失、损坏的数据可以实现**校验**和**还原**两个功能
  - 通过对数据进行校验和( checksum )进行计算，可以检查数据是否完整，有无损坏或更改，在数据 传输和保存时经常用到，如TCP协议
  - 恢复还原，通过对数据结合校验码进行数学计算，还原丢失或损坏的数据，可以在保证数据可靠的 前提下，降低冗余，如单机硬盘存储中的RAID技术，纠删码(Erasure Code)技术等。
  - **MinlO采用的就是纠删码技术**



MinIO 纠删码EC (Erasure Code) 是一种数据冗余和可用性功能，允许具有多个驱动器的 MinIO 部署即 时自动重建对象，即使群集中丢失了多个驱动器或节点。 纠删码提供了**对象级修复**

Minio使用纠删码erasure code 和校验和checksum来保护数据免受硬件故障和无声数据损坏。即便您 丢失一 半数量(N/2) 的硬盘,您仍然可以恢复数据

纠删码是一种恢复铁和损坏数据的数学算法，Minio采用Reed-Solomon code将对象拆分成N/2数据和 N/2奇偶校验块。

```ABAP
当损坏总磁盘数的一半磁盘时,只能读取而不能上传新的文件,只要保证正常磁盘数大于等n/2+1时,就可以支持写入新数据
```

这就意味着如果是12块盘，一个对象会被分成6个数据块、6个奇偶校验块，你可以失任意6块盘(不管其 是存放的数据块还是奇偶校验块)，你仍可以从剩下的盘中的数据进行恢复

```ABAP
实现纠删码 EC 至少需要4块磁盘以上
```

纠删码是可以通过数学计算,实现数据冗余,功能上类似于RAID技术,当磁盘损坏时,可以通过计算把丢失的 数据进行还原，它可以将n份原始数据,增加m份数据,并能通过n+m份中的任意n份数据,还原为原始数 据。即如果有**任意小于等于m份**的数据失效,仍然能通过剩下的数据还原出来。



#### MinIO 工作流程

![image-20250118155634053](D:\git_repository\cyber_security_learning\markdown_img\image-20250118155634053.png)

### MINIO部署



 **部署模式**

- **单机单硬盘**
- **单机多硬盘**
- **多机多硬盘**



**部署方法**

- **包安装**
- **二进制安装**
- **Docker容器化安装**
- **基于Kubernetes部署**



#### 单机部署

minio server的standalone模式，即单机模式，所有管理的磁盘都在一个主机上。

该启动模式一般仅用于实验环境、测试环境、开发环境的验证和学习使用。

在standalone模式下，还可以分为**non-erasure code mode**和**erasure code mode(纠删码)**。

- **non-erasure code mode**
  - 当minio server 运行时只传入一个本地磁盘参数。即为 non-erasure code mode
  - 在此启动模式下，对于每一份对象数据， minio直接存储这份数据，不会建立副本，也不会启用纠删码机制。
  - 因此,这种模式无论是服务实例还是磁盘都是”单点"，无任何高可用保障，磁盘损坏就意味着数据丢失。
- **erasure code mode**
  - 此模式需要为minio server实例传入多个本地磁盘参数。
  - 一旦遇到多于一 个磁盘的参数， minio server会自动启用erasure code mode.
  - erasure code对磁盘的个数是有要求的，至少4个磁盘, 如不满足要求，实例启动将失败。
  - erasure code启用后，要求传给minio server的endpoint(standalone模式下，即本地磁盘上的目录)至少为4个。



##### 包安装

**Debian/Ubuntu包安装**

```bash
# 下载deb包
[root@mystical ~]# wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20230829230735.0.0_amd64.deb -O minio.deb

# 安装
[root@mystical ~]# dqkg -i minio.deb

# 查看
[root@mystical ~]# which minio
/usr/local/bin/minio

[root@mystical ~]# minio -v
minio version RELEASE.2023-08-29T23-07-35Z (commit-id=07b1281046c8934c47184d1b56c78995ef960f7d)
Runtime: go1.19.12 linux/amd64
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl-3.0.html>
Copyright: 2015-2023 MinIO, Inc.

# 查看service文件
[root@mystical ~]# grep -Ev "#|^$" /lib/systemd/system/minio.service
[Unit]
Description=MinIO
Documentation=https://docs.min.io
Wants=network-online.target
After=network-online.target
AssertFileIsExecutable=/usr/local/bin/minio
[Service]
Type=notify
WorkingDirectory=/usr/local
User=minio-user
Group=minio-user
ProtectProc=invisible
EnvironmentFile=-/etc/default/minio
ExecStartPre=/bin/bash -c "if [ -z \"${MINIO_VOLUMES}\" ]; then echo \"Variable MINIO_VOLUMES not set in /etc/default/minio\"; exit 1; fi"
ExecStart=/usr/local/bin/minio server $MINIO_OPTS $MINIO_VOLUMES
Restart=always
LimitNOFILE=1048576
TasksMax=infinity
TimeoutStopSec=infinity
SendSIGKILL=no
[Install]
WantedBy=multi-user.target

# 需自行创建用户
[root@mystical ~]# groupadd -r minio-user
[root@mystical ~]# useradd -M -r -s /sbin/nologin -g minio-user minio-user

# 准备多个数据目录,minio数据目录不允许和根文件系统在一起，注意：新版允许
[root@mystical ~]# mkdir -p /data

# 在现有卷组中，切10G逻辑卷
[root@mystical ~]# lvcreate -n minio -L 10G ubuntu-vg 
  Logical volume "minio" created.
  
# 给新逻辑卷创建文件系统
[root@mystical ~]# mkfs.ext4 /dev/ubuntu-vg/minio 
mke2fs 1.46.5 (30-Dec-2021)
Creating filesystem with 2621440 4k blocks and 655360 inodes
Filesystem UUID: 956b6bf3-8709-4c30-a8e1-97eda95cba2a
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done 

# 配置持久化
[root@mystical ~]# echo /dev/ubuntu-vg/minio /data ext4 defaults 0 0 >> /etc/fstab

# 挂载
[root@mystical ~]# mount -a

[root@mystical ~]# mkdir -p /data/minio{1..4} 
[root@mystical ~]# chown -R minio-user.minio-user /data/
[root@mystical ~]# ll -d /data/minio{1..4}
drwxr-xr-x 2 minio-user minio-user 4096 Jan 18 08:22 /data/minio1/
drwxr-xr-x 2 minio-user minio-user 4096 Jan 18 08:22 /data/minio2/
drwxr-xr-x 2 minio-user minio-user 4096 Jan 18 08:22 /data/minio3/
drwxr-xr-x 2 minio-user minio-user 4096 Jan 18 08:22 /data/minio4/

# 创建初始化参数（注意在实验时将注释去掉，防止干扰）
[root@mystical ~]# cat > /etc/default/minio <<EOF
> MINIO_ROOT_USER=admin                #默认minioadmin
MINIO_ROOT_PASSWORD=12345678           #默认minioadmin
MINIO_VOLUMES="/data/minio{1...4}"     #必选项
MINIO_OPTS='--console-address :9001'   #默认端口随机端口
> EOF

# 开机自启服务并启动minio
[root@mystical ~]# systemctl enable --now minio.service 

#登录 http://10.0.0.100:9001/ 用户名密码:admin/12345678 
```

![image-20250118163000487](D:\git_repository\cyber_security_learning\markdown_img\image-20250118163000487.png)

![image-20250118163045830](D:\git_repository\cyber_security_learning\markdown_img\image-20250118163045830.png)



**红帽系统包安装**

```bash
# 下载rpm包
[root@localhost ~]# wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio-20230829230735.0.0.x86_64.rpm -O minio.rpm

# 安装
[root@localhost ~]# yum install -y ./minio.rpm 

# 应用
[root@localhost ~]# mkdir ~/minio
[root@localhost ~]# minio server ~/minio --console-address :9090

#默认用户和密码
#RootUser: minioadmin 
#RootPass: minioadmin 
```



![image-20250118163714513](D:\git_repository\cyber_security_learning\markdown_img\image-20250118163714513.png)



![image-20250118163758269](D:\git_repository\cyber_security_learning\markdown_img\image-20250118163758269.png)





##### 二进制表示部署

```bash
# 官方下载网站
https://dl.min.io/server/minio/release/linux-amd64/

# 下载二进制文件
[root@mystical ~]# wget https://dl.min.io/server/minio/release/linux-amd64/minio

# 添加到PATH路径并添加执行权限
[root@mystical ~]# install minio /usr/local/bin

# 准备数据目录，建议此目录为逻辑卷，方便后期动态扩容
[root@mystical /data/minio]# lvcreate -n minio -L 10G ubuntu-vg
[root@mystical /data/minio]# mkdir -p /data
[root@mystical /data/minio]# mkfs.ext4 /dev/ubuntu-vg/minio 
[root@mystical /data/minio]# echo /dev/ubuntu-vg/minio /data ext4 defaults 0 0 >> /etc/fstab
[root@mystical /data/minio]# mount -a
# 实际生产中，4个目录对应4块独立硬盘，这里仅做模拟
[root@mystical /data/minio]# mkdir -p /data/minio{1..4}
[root@mystical /data/minio]# chown -R minio.minio /data/

# 创建用户
[root@mystical ~]# useradd -s /sbin/nologin -r minio

# 给目录授权
[root@mystical ~]# chown -R minio.minio /data/minio/

# 创建service文件，新版对密码强度有要求，不要用弱密码
[root@mystical /data/minio]# cat /lib/systemd/system/minio.service
[Unit]
Description=Minio
After=systemd-networkd.service systemd-resolved.service
Documentation=https://min.io
[Service]
Type=notify
Environment=MINIO_ROOT_USER=admin MINIO_ROOT_PASSWORD=Zyf123456
ExecStart=/usr/local/bin/minio server /data/minio{1...4} --console-address ":9999"
Restart=on-failure
User=minio
Group=minio
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
[Install]
WantedBy=multi-user.target

[root@mystical /data/minio]# systemctl enable --now minio

# 访问10.0.0.151:9999
```

![image-20250118181523507](D:\git_repository\cyber_security_learning\markdown_img\image-20250118181523507.png)





#### 分布式集群部署



![image-20250118182057118](D:\git_repository\cyber_security_learning\markdown_img\image-20250118182057118.png)



**分布式Minio优势**

- **数据保护**
  - 分布式Minio采用纠删码来防范多个节点宕机和位衰减bit rot。
  - 分布式Minio至少需要4个硬盘，使用分布式Minio 会自动引入纠删码功能
- **高可用**
  - 单机Minio服务存在单点故障，相反，如果是一个有N块硬盘的分布式Minio,只要有N/2硬盘在线， 数据就是安全的。不过你需要至少有N/2+1个硬盘来创建新的对象。
  - 例如，一个16节点Minio集群，每个节点16块硬盘，就算8台服务器宕机，这个集群仍然可读的， 不过需要9台服务器才能写数据。
- **性能**
  - 多个节点负载均衡，提升性能
- **一致性**
  - Minio在分布式和单机模式下，所有读写操作都严格遵守read-after-write一致性模型。



**分布式Minio实现条件**

- 在所有节点运行同样的命令启动一个分布式Minio实例，只需要把硬盘位置做为参数传给minio  server命令即可
- 分布式Minio中的所有节点需要有同样的环境变量MINIO_ACCESS_KEY和MINIO_SECRET_KEY，才 能建立分布式集群
  - 注意：新版本使用环境变量 **MINIO_ROOT_USER**和**MINIO_ROOT_PASSWORD**
- 分布式Minio使用的磁盘里必须是干净的，里面没有数据
- 分布式Minio里的节点时间差不能超过3秒，可以使用NTP来保证时间一致



**分布式Minio注意事项**

- minio服务器多块数据磁盘需申请独立的磁盘，在物理底层要相互独立避免遇到磁盘io竞争，导致 minio性能直线下降,如果性能下降严重，数据量大时甚至会导致集群不可用
- minio数据磁盘最大不超过2T,如果使用lvm逻辑卷，逻辑卷大小也不要超过2T，过大的磁盘或文件 系统会导致后期IO延迟较高导致minio性能降
- minio集群共M节点每个节点N块数据磁盘，磁盘只要存活M*N/2，minio集群数据就是安全的，在 节点数剩余M/2+1时节点可以正常读写
- 如果使用lvm方式扩展集群容量，请在部署阶段minio数据目录就使用lvm。
- 如果需要备份minio集群数据，请准备存放minio集群所有对象数据的空间容量
  - 比如: 一个2T/盘*4块/节点*8节点=64T的集群所有容量的一半存储空间即32T服务器，配置内存 CPU配置不需要太高
- 如果网络环境允许请把minio集群节点配置双网卡，节点通信网络与客户端访问网络分开避免网络瓶颈
- 配置反向代理实现MinIO的负载均衡, 可以使用云服务SLB或者2台haproxy/nginx结合keepalived 实现高可用
- minio系统中不要安装消耗IO较高的应用,比如:updatedb程序，如安装请排除扫描minio数据目录, 否则可以会导致磁盘io延迟过高，会导致cpu负载过高，从而降低minio性能



**二进制安装MinIO 实现3节点4磁盘的分布式集群部署**

```bash
#准备三台主机,在所有节点上做好名称解析
[root@minio1 ~]# cat /etc/hosts
10.0.0.150 minio1.mystical.org minio1
10.0.0.151 minio2.mystical.org minio2
10.0.0.152 minio3.mystical.org minio3

# 在所有节点下载二进制程序
[root@minio1 ~]# wget https://dl.min.io/server/minio/release/linux-amd64/minio
[root@minio1 ~]# install minio /usr/local/bin/minio

#在所有节点上准备数据目录和用户
[root@minio1 ~]# lvcreate -n minio -L 10G ubuntu-vg
[root@minio1 ~]# mkfs.ext4 /dev/ubuntu-vg/minio
[root@minio1 ~]# echo /dev/ubuntu-vg/minio /data/ ext4 defaults 0 0 >> /etc/fstab
[root@minio1 ~]# mkdir -p /data
[root@minio1 ~]# mkdir -p /data/minio{1..4}
[root@minio1 ~]# useradd -r -s /sbin/nologin minio
[root@minio1 ~]# chown -R minio. /data

# 在所有节点上准备环境变量
[root@minio3 ~]# cat > /etc/default/minio <<EOF
> MINIO_ROOT_USER=admin
MINIO_ROOT_PASSWORD=12345678
MINIO_VOLUMES='http://minio{1...3}.mystical.org:9000/data/minio{1...4}'
MINIO_OPTS='--console-address :9001'
MINIO_PROMETHEUS_AUTH_TYPE="public"
> EOF


#在所有节点上创建service文件
[root@minio1 ~]# vim/lib/systemd/system/minio.service
[Unit]
Description=MinIO
Documentation=https://docs.min.io
Wants=network-noline.target
After=network-noline.target

[Service]
WorkingDirectory=/usr/local
User=minio
Group=minio
EnvironmentFile=-/etc/default/minio
ExecStartPre=/bin/bash -c "if [ -z \"${MINIO_VOLUMES}\" ]; then echo \"Variable MINIO_VOLUMES not set in /etc/default/minio\"; exit 1; fi"
ExecStart=/usr/local/bin/minio server $MINIO_OPTS $MINIO_VOLUMES
Restart=always
LimitNOFILE=1048576
TasksMax=infinity

[Install]
WantedBy=multi-user.target


# 在所有节点启动服务
#浏览器访问 http://minio{1..3}.wang.org:9000/ 用户名密码:admin/12345678
```

![image-20250118212508562](D:\git_repository\cyber_security_learning\markdown_img\image-20250118212508562.png)



**配置反向代理，通过haproxy或nginx实现minio的反向代理**

```bash
#配置反向代理,通过Haproxy或者Nginx实现minio的反向代理
#Haproxy配置
[root@mystical ~]# apt update && apt -y instapt update && apt -y install haproxy

[root@mystical ~]# vim /etc/haproxy/haproxy.cfg
...
listen stats
   mode http
   bind 0.0.0.0:9999
   stats enable
   log global
   stats uri /haproxy-status
   stats auth admin:123456
listen minio
   bind 10.0.0.100:9000
   mode http
   log global
   server 10.0.0.101 10.0.0.101:9000 check inter 3000 fall 2 rise 5
   server 10.0.0.102 10.0.0.102:9000 check inter 3000 fall 2 rise 5
   server 10.0.0.103 10.0.0.103:9000 check inter 3000 fall 2 rise 5
listen minio_console
   bind 10.0.0.100:9001
   mode http
   log global
   server 10.0.0.101 10.0.0.101:9001 check inter 3000 fall 2 rise 5
   server 10.0.0.102 10.0.0.102:9001 check inter 3000 fall 2 rise 5
   server 10.0.0.103 10.0.0.103:9001 check inter 3000 fall 2 rise 5

# 重启haproxy
[root@mystical ~]# systemctl restart haproxy.service

# 访问10.0.0.100:9000
```

![image-20250118214910766](D:\git_repository\cyber_security_learning\markdown_img\image-20250118214910766.png)









​                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

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
wget https://mirror.ghproxy.com/https://github.com/Mirantis/cri-dockerd/releases/download/v0.3.14/cri-dockerd_0.3.14.3-0.ubuntu-jammy_amd64.deb

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
[root@master1 controller] # kubectl apply -f controller-deployment-rollupdate-canary.yaml 
deployment.apps/deployment-rolling-update-canary created
service/pod-test created

# 当前状态
[root@master1 controller] # kubectl get pod
NAME                                                READY   STATUS    RESTARTS        AGE
deployment-rolling-update-canary-6794cd6c97-6ljcw   1/1     Running   0               45s
deployment-rolling-update-canary-6794cd6c97-dmsgg   1/1     Running   0               45s
deployment-rolling-update-canary-6794cd6c97-xmjnh   1/1     Running   0               45s

# 升级版本
[root@master1 controller]#sed -i 's/pod-test:v0.1/pod-test:v0.2/' controller-deployment-rollupdate-canary.yaml

# 金丝雀发布
[root@master1 controller] # kubectl apply -f controller-deployment-rollupdate-canary.yaml && kubectl rollout pause deployment deployment-rolling-update-canary
deployment.apps/deployment-rolling-update-canary configured
service/pod-test unchanged
deployment.apps/deployment-rolling-update-canary paused
[root@master1 controller] # kubectl get pod
NAME                                                READY   STATUS    RESTARTS        AGE
deployment-rolling-update-canary-65687cb7cb-b9ghp   1/1     Running   0               4s
deployment-rolling-update-canary-6794cd6c97-6ljcw   1/1     Running   0               3m34s
deployment-rolling-update-canary-6794cd6c97-dmsgg   1/1     Running   0               3m34s
deployment-rolling-update-canary-6794cd6c97-xmjnh   1/1     Running   0               3m34s

# 更新
[root@master1 controller] # kubectl rollout status deployment deployment-rolling-update-canary 
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
[root@master1 controller] # kubectl rollout resume deployment deployment-rolling-update-canary && kubectl rollout pause deployment deployment-rolling-update-canary
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
  #externalTrafficPolicy: Local # 默认值为Cluster,如果是Local只能被当前运行Pod的节点处理流量，并且可以获取客户端真实IP
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

```ABAP
插件的定义和执行是按照配置文件的顺序进行解析的，并且 CoreDNS 会对第一个匹配的 forward 插件进行处理。一旦匹配成功，就不会继续处理后续的 forward 插件。

如果匹配后无法解析该域名，CoreDNS 将返回 NXDOMAIN 或 SERVFAIL。
如果希望前面无法解析的情况下，继续尝试后续的配置，可以在配置中添加fallthrough

# 示例：
forward wang.org 10.0.0.200 {
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
provisioner: k8s-sigs.io/nfs-subdir-external-provisioner # or choose another name, must match deployment's env PROVISIONER_NAME
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





#### Secret声明式创建

Secret 数据存放在data或stringData字段,其中**data字段中的Key/value必须使用base64编码存放**,而 stringData使用明文存放

Secret 资源的元数据：除了name, namespace之外，常用的还有labels, annotations

- annotation的名称遵循类似于labels的名称命名格式，但其数据长度不受限制
- 它不能用于被标签选择器作为筛选条件；但常用于为那些仍处于Beta阶段的应用程序提供临时的配置接口
- 管理命令：kubectl annotate TYPE/NAME KEY=VALUE

```bash
[root@master1 ~]#kubectl explain secret
KIND:       Secret
VERSION:    v1

DESCRIPTION:
    Secret holds secret data of a certain type. The total bytes of the values in
    the Data field must be less than MaxSecretSize bytes.
    
FIELDS:
  apiVersion	<string>
    APIVersion defines the versioned schema of this representation of an object.
    Servers should convert recognized schemas to the latest internal value, and
    may reject unrecognized values. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

  data	<map[string]string>
    Data contains the secret data. Each key must consist of alphanumeric
    characters, '-', '_' or '.'. The serialized form of the secret data is a
    base64 encoded string, representing the arbitrary (possibly non-string) data
    value here. Described in https://tools.ietf.org/html/rfc4648#section-4

  immutable	<boolean>
    Immutable, if set to true, ensures that data stored in the Secret cannot be
    updated (only object metadata can be modified). If not set to true, the
    field can be modified at any time. Defaulted to nil.

  kind	<string>
    Kind is a string value representing the REST resource this object
    represents. Servers may infer this from the endpoint the client submits
    requests to. Cannot be updated. In CamelCase. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

  metadata	<ObjectMeta>
    Standard object's metadata. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

  stringData	<map[string]string>
    stringData allows specifying non-binary secret data in string form. It is
    provided as a write-only input field for convenience. All keys and values
    are merged into the data field on write, overwriting any existing values.
    The stringData field is never output when reading from the API.

  type	<string>
    Used to facilitate programmatic handling of secret data. More info:
    https://kubernetes.io/docs/concepts/configuration/secret/#secret-types

```





#### Secret引用

Secret资源在Pod中引用的方式有三种

- **环境变量**
  - 引用Secret对象上特定的key，以valueFrom赋值给Pod上指定的环境变量
  - 在Pod上使用envFrom一次性导入Secret对象上的所有key-value，key(也可以统一附加特定前缀） 即为环境变量名,value自动成 为相应的变量值
  - 注意：容器很可能会将环境变量打印到日志中,基于安全考虑**不建议以环境变量方式引用Secret中的敏感数据**
- **secret卷**
  - 在Pod上将Secret对象引用为存储卷，而后整体由容器mount至某个目录下,其中key名称转为文件 名，value的值转为相应的文件内容
  - 在Pod上定义Secret卷时，也可以仅引用其中的指定的部分key，而后由容器mount至目录下
- **拉取镜像**
  - 在Pod 上使用 imagePullSecrets 拉取私有仓库镜像使用
  - Pod引用Secret的方式：pods.spec.imagePullSecrets





#### Generic 案例

generic 主要用于实现用户名和密码的加密保存

注意: generic加密保存要注意换行问题 `\n `

```bash
#generic类型
kubectl create secret generic NAME [--type=string] [--from-file=[key=]source] [--from-literal=key1=value1]

--from-literal=key1=value1        #以命令行设置键值对的方式配置数据
--from-env-file=/PATH/TO/FILE       #以环境变量专用文件的方式配置数据
--from-file=[key=]/PATH/TO/FILE #以配置文件的方式创建配置数据，如不指定key，FILE名称为key名
--from-file=/PATH/TO/DIR        #以配置文件所在目录的方式创建配置数据

#该命令中的--type选项进行定义除了后面docker-registry和tls命令之外的其它子类型，有些类型有key的特定要求
#注意: 如果vaule中有特殊字符,比如:$,\,*,=,!等,需要用\进行转义或用单引号''引起来
```



##### 范例：命令式创建 generic

```bash
# 命令式创建
[root@master1 ~]# kubectl create secret generic secret-mysql-root --from-literal=username=root --f
rom-literal=password=123456
secret/secret-mysql-root created

# 查看
[root@master1 ~]# kubectl get secrets 
NAME                TYPE     DATA   AGE
secret-mysql-root   Opaque   2      6s

# 查看Generic使用Base64编码
[root@master1 ~]# kubectl get secrets secret-mysql-root -o yaml
apiVersion: v1
data:
  password: MTIzNDU2
  username: cm9vdA==
kind: Secret
metadata:
  creationTimestamp: "2025-01-02T01:19:55Z"
  name: secret-mysql-root
  namespace: default
  resourceVersion: "247070"
  uid: 5e668e52-7990-47ec-93b6-a412649c5417
type: Opaque

# 解码
[root@master1 ~]# echo -n "MTIzNDU2" | base64 -d
123456
[root@master1 ~]# echo -n "cm9vdA==" | base64 -d
root

# 删除
[root@master1 ~]# kubectl delete secrets secret-mysql-root 
secret "secret-mysql-root" deleted
```



##### 范例：stringData明文数据

```yaml
# 清单文件
[root@master1 secret] # vim storage-secret-opaque-stringData.yaml
apiVersion: v1
kind: Secret
metadata:
  name: secret-stringdata
  namespace: default
type: opaque
stringData:                  # stringData表示明文存放数据，data表示必须以base64编码存放
  user: 'admin'
  password: '123456'


# 应用
[root@master1 secret] # kubectl apply -f storage-secret-opaque-stringData.yaml 
secret/secret-stringdata created

# 查看
[root@master1 secret] # kubectl get secrets 
NAME                TYPE     DATA   AGE
secret-stringdata   opaque   2      5s

# 查看
[root@master1 secret] # kubectl get secrets secret-stringdata -o yaml
apiVersion: v1
data:
  password: MTIzNDU2
  user: YWRtaW4=
kind: Secret
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","kind":"Secret","metadata":{"annotations":{},"name":"secret-stringdata","namespace":"default"},"stringData":{"password":"123456","user":"admin"},"type":"opaque"}
  creationTimestamp: "2025-01-02T01:27:51Z"
  name: secret-stringdata
  namespace: default
  resourceVersion: "247832"
  uid: 58fa1297-3800-4c02-bfd7-b9a63212f1e3
type: opaque

# 删除
[root@master1 secret] # kubectl delete -f storage-secret-opaque-stringData.yaml 
secret "secret-stringdata" deleted
```



#####  范例: Secret 通过环境变量为提供MySQL环境初始化的密码信息

```yaml
# MySQL容器支持MYSQL_ROOT_PASSWORD变量存放密码,使用环境变量创建MySQL容器
[root@master1 secret] # docker run --name mysql_test -e MYSQL_ROOT_PASSWORD=123456 -d mysql:8.0

# 登录验证
[root@master1 secret] # docker exec mysql_test mysql -uroot -h127.0.0.1 -p123456 -e status
mysql: [Warning] Using a password on the command line interface can be insecure.
--------------
mysql  Ver 8.0.40 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:		8
Current database:	
Current user:		root@127.0.0.1
SSL:			Cipher in use is TLS_AES_256_GCM_SHA384
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		8.0.40 MySQL Community Server - GPL
Protocol version:	10
Connection:		127.0.0.1 via TCP/IP
Server characterset:	utf8mb4
Db     characterset:	utf8mb4
Client characterset:	latin1
Conn.  characterset:	latin1
TCP port:		3306
Uptime:			48 sec

Threads: 2  Questions: 5  Slow queries: 0  Opens: 119  Flush tables: 3  Open tables: 38  Queries per second avg: 0.104
--------------

# 生成密码的base64编码
[root@master1 secret] # echo -n root|base64
cm9vdA==
[root@master1 secret] # echo -n 123456|base64
MTIzNDU2

# 清单文件，secret 通过环境为提供MySQL环境初始化的密码信息，但很不安全
[root@master1 secret]#cat storage-secret-mysql-init.yaml 
apiVersion: v1
kind: Secret
metadata:
  name: secret-mysql
type: kubernetes.io/basic-auth
# type: Opaque  # 也可以用Opaque类型
data:
  username: cm9vdA==
  password: MTIzNDU2
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-secret-mysql-init
spec:
  containers:
  - name: mysql
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
    env:
    - name: MYSQL_ROOT_PASSWORD
      valueFrom:
        secretKeyRef:
          name: secret-mysql   # 引用指定的secret
          key: password        # 引用指定的secret中对应的key
          optional: false      # 必须存在

# 应用
[root@master1 secret] # kubectl apply -f storage-secret-mysql-init.yaml 
secret/secret-mysql created
pod/pod-secret-mysql-init created

# 查看结果
[root@master1 secret] # kubectl get secrets 
NAME           TYPE                       DATA   AGE
secret-mysql   kubernetes.io/basic-auth   2      28s

[root@master1 secret] # kubectl get pod
NAME                    READY   STATUS    RESTARTS      AGE
pod-secret-mysql-init   1/1     Running   0             47s

# 可以通过环境变量查看到密码，很不安全
[root@master1 secret]#kubectl exec pod-secret-mysql-init -- env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=pod-secret-mysql-init # -------------- secret变量
MYSQL_ROOT_PASSWORD=123456     # -------------- secret变量
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
GOSU_VERSION=1.14
MYSQL_MAJOR=8.0
MYSQL_VERSION=8.0.29-1.el8
MYSQL_SHELL_VERSION=8.0.29-1.el8
HOME=/root

# 验证密码登录MySQL
[root@master1 secret] # kubectl exec pod-secret-mysql-init -- mysql -uroot -p123456 -e status
mysql: [Warning] Using a password on the command line interface can be insecure.
--------------
mysql  Ver 8.0.29 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:		8
Current database:	
Current user:		root@localhost
SSL:			Not in use
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		8.0.29 MySQL Community Server - GPL
Protocol version:	10
Connection:		Localhost via UNIX socket
Server characterset:	utf8mb4
Db     characterset:	utf8mb4
Client characterset:	latin1
Conn.  characterset:	latin1
UNIX socket:		/var/run/mysqld/mysqld.sock
Uptime:			2 min 27 sec

Threads: 2  Questions: 5  Slow queries: 0  Opens: 117  Flush tables: 3  Open tables: 36  Queries per second avg: 0.034
--------------

# 更改密码
[root@master1 yaml] # echo -n 654321 | base64 
NjU0MzIx

[root@master1 yaml] # vim storage-secret-mysql-init.yaml
data:
 username: cm9vdAo=
 password: NjU0MzIx   #修改密码
 
# 重新应用
[root@master1 secret] # kubectl apply -f storage-secret-mysql-init.yaml 
secret/secret-mysql configured
pod/pod-secret-mysql-init unchanged

# 查看是否变化
[root@master1 secret] # kubectl get secrets secret-mysql -o yaml
apiVersion: v1
data:
  password: NjU0MzIx        # 成功更新
  username: cm9vdA==
kind: Secret
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","data":{"password":"NjU0MzIx","username":"cm9vdA=="},"kind":"Secret","metadata":{"annotations":{},"name":"secret-mysql","namespace":"default"},"type":"kubernetes.io/basic-auth"}
  creationTimestamp: "2025-01-02T01:40:21Z"
  name: secret-mysql
  namespace: default
  resourceVersion: "249464"
  uid: 1ba61d4f-41d6-4f3a-989d-4f572ec08734
type: kubernetes.io/basic-auth

# Pod内变量没有自动更新
[root@master1 secret] # kubectl exec pod-secret-mysql-init -- env|grep PASSWORD
MYSQL_ROOT_PASSWORD=123456

# 删除Pod重建
[root@master1 secret] # kubectl delete pod pod-secret-mysql-init 
pod "pod-secret-mysql-init" deleted

[root@master1 secret] # kubectl apply -f storage-secret-mysql-init.yaml 
secret/secret-mysql unchanged
pod/pod-secret-mysql-init created

# Pod内变量更新成功
[root@master1 secret] # kubectl exec pod-secret-mysql-init -- env|grep PASSWORD
MYSQL_ROOT_PASSWORD=654321

# 清理环境
[root@master1 secret] # kubectl delete -f storage-secret-mysql-init.yaml 
secret "secret-mysql" deleted
pod "pod-secret-mysql-init" deleted
```



##### 范例: 通过卷调用 secret

```yaml
# 清单文件
[root@master1 secret] # cat storage-secret-test-pod.yaml 
apiVersion: v1
kind: Secret
metadata:
  name: secret-test
type: kubernetes.io/basic-auth
data:
  username: YWRtaW4=
  password: cGFzc3dvcmQ=

# 说明：
#type类型指定为 Opaque 或者 kubernetes.io/basic-auth,username和password是加密的信息
#资源定义文件时，与命令行创建secret的--from-literal=username=admin 效果是一样的,但命令行的变量无需加密

---
# 调用secret的清单文件
apiVersion: v1
kind: Pod
metadata:
  name: pod-secret-volume
spec:
  volumes:
  - name: secret
    secret:
      secretName: secret-test    # 指定secret的名称
  containers:
  - name: secret-test-container
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumeMounts:
    - name: secret
      mountPath: /secret/
      readOnly: true

# 创建资源
[root@master1 secret] # kubectl apply -f  storage-secret-test-pod.yaml 
secret/secret-test unchanged
pod/pod-secret-volume created

# 查看
[root@master1 secret] # kubectl get secrets 
NAME          TYPE                       DATA   AGE
secret-test   kubernetes.io/basic-auth   2      56s

# 验证
[root@master1 secret]#kubectl exec pod-secret-volume  -- ls /secret
password
username

# 在Pod运行的宿主机上可以看到secret对应的文件
[root@node2 ~] # find /var/lib/kubelet -name password
/var/lib/kubelet/pods/0439bb26-fdfc-4769-9cc9-d47c718fb301/volumes/kubernetes.io~secret/secret/password

[root@node2 ~] # cat /var/lib/kubelet/pods/0439bb26-fdfc-4769-9cc9-d47c718fb301/volumes/kubernetes.io~secret/secret/password
password

# 清理环境
[root@master1 secret] # kubectl delete -f storage-secret-test-pod.yaml 
secret "secret-test" deleted
pod "pod-secret-volume" deleted
```



##### 范例: 为 Service Account 创建 Secret

```yaml
#k8s-v1.24版本后,创建SA不会自动创建secret,需要手动创建secret
[root@master1 secret] # cat storage-secret-sa.yaml 
apiVersion: v1
kind: ServiceAccount
metadata:
  name: testsa
---
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: testsa-secret
  namespace: default
  annotations:
    kubernetes.io/service-account.name: "testsa"

# 查看
[root@master1 secret] # kubectl get secrets,sa
NAME                   TYPE                                  DATA   AGE
secret/testsa-secret   kubernetes.io/service-account-token   3      29s

NAME                     SECRETS   AGE
serviceaccount/default   0         4d18h
serviceaccount/testsa    0         29s

# 查看对应token
[root@master1 secret] # kubectl get secrets testsa-secret -o yaml
apiVersion: v1
data:
  ca.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURCVENDQWUyZ0F3SUJBZ0lJZHhKUmVsbVJDVlF3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TkRFeU1qZ3dOelV3TURWYUZ3MHpOREV5TWpZd056VTFNRFZhTUJVeApFekFSQmdOVkJBTVRDbXQxWW1WeWJtVjBaWE13Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLCkFvSUJBUUMrdG9oRDcwaUhEVzNxeFhPeVlsaFpveER0bUZFSTRjTk93K0RySDZFcFVxaVdSUDM0TmwxSzNuR3kKdlRJM3BlRkJtQnF4cXFSSGhCV3M3QUNHTUNFM3VJTHdpN21WTTBrOXJrTW9XeDBIL0draTFyQUJRRXhCS0xyUgp3MTJTdE1QNTFKMHJKaUpxU1I3SElCQ1N5b2NSTzFmYmZNY0VQKzRvK2ZLaWxybHZtTVZIS08vb1czSlJBSXA1CjNkSTBlZUNHTytIN1FFV0RDUlZwek10emtRUGg5L2hMM0t2eEVtSFRtcGt5N2NLNFVoc3c5ZVBrOTVxTmgybnoKUExKd0laNTBpRkh0M05VclRjVUJwTUlpN2VKZEZ0T0ZCTXEraEdvLzJRZlIzUTZ1dmpLdFdrTk9tcFcwRmRaYwpvbHlwbjFmZjdUUEFMVFc4eWdlSGIwRnhIR1R6QWdNQkFBR2pXVEJYTUE0R0ExVWREd0VCL3dRRUF3SUNwREFQCkJnTlZIUk1CQWY4RUJUQURBUUgvTUIwR0ExVWREZ1FXQkJTWGtXOGRYRVVpanlhRThiZGFRU1pxd2k5UVFUQVYKQmdOVkhSRUVEakFNZ2dwcmRXSmxjbTVsZEdWek1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQ0FkTTQ3RHNHUApla2VUQXRXdTFFc3NJVlJJWUZ4bzZhNzBPZG8rOGxyQ2xVdjc1SzRHbkxxc3ByaFA5Y2dPN0JZbXpxb0xNazR2Cmwyem1VOFlqbXYrblVpaWVFMkcyekh6dFNZRXZ2RHBoL1FUajl0Yk1LYmpqenRQYWlNTE9RUXB6bXNXR2FIYzIKUTMrMnZlYzNFY3JneTJidCtUOWNDUE9za0ZZemlNTzZaMEVtNXdtRkgxbk9CRkdCSWpwVUJUZmV5TURkMjNwNwp6THB5M0RUMkNTVWkva2NOeWpOd0tZczhTTmNwRjYyc1VCS2h1eUdidG8rSEo2Q3J6UmFTb3hRcW9BeHdtRUl6CjhYZHhnbEFaSm5tY0F2L0lKVW1HOGVTRFhYMTZNdDBsSm5XT0JzTHJXU08rN1BwWkR0UFlnaG5rVGgweHNmNHUKODEydFFWelpnYjFsCi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K
  namespace: ZGVmYXVsdA==
  token: ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNkltdERURWRTV0VwNFozbGpTamxMWlhsTFRrTjZMWE5EZUZsQmJsaE5OR1paY1hSelowTkhjelUzVURnaWZRLmV5SnBjM01pT2lKcmRXSmxjbTVsZEdWekwzTmxjblpwWTJWaFkyTnZkVzUwSWl3aWEzVmlaWEp1WlhSbGN5NXBieTl6WlhKMmFXTmxZV05qYjNWdWRDOXVZVzFsYzNCaFkyVWlPaUprWldaaGRXeDBJaXdpYTNWaVpYSnVaWFJsY3k1cGJ5OXpaWEoyYVdObFlXTmpiM1Z1ZEM5elpXTnlaWFF1Ym1GdFpTSTZJblJsYzNSellTMXpaV055WlhRaUxDSnJkV0psY201bGRHVnpMbWx2TDNObGNuWnBZMlZoWTJOdmRXNTBMM05sY25acFkyVXRZV05qYjNWdWRDNXVZVzFsSWpvaWRHVnpkSE5oSWl3aWEzVmlaWEp1WlhSbGN5NXBieTl6WlhKMmFXTmxZV05qYjNWdWRDOXpaWEoyYVdObExXRmpZMjkxYm5RdWRXbGtJam9pTURNNVpUZGpNalF0TXpkaVpTMDBNamt4TFRneE9HTXRNemxqWWpKaFkyVmhOekkySWl3aWMzVmlJam9pYzNsemRHVnRPbk5sY25acFkyVmhZMk52ZFc1ME9tUmxabUYxYkhRNmRHVnpkSE5oSW4wLkI3SFQtQWx5MWt2Wk1TTGFfSTREWHBGM0lkZ2JVaHJXWkczZXBQdVprcTQtWkpfcGN5MTJabkVCTUttLVRTbTFwNWhrQ3gzQm5NQzJ6QmF0VHJIRmp5TkhQSWRuZFJwMk9NMzZHeHNKOGNna0tOU21FMVg3bmM4R2w0ZkxYcDJXSWdUQVN2ZWFVOFI3UWFlZWhXaXdpNzNLNjVpMjNqNEtFYW9YRHhyS2hmb1RIWkdhVG5hVFdTTFZPNW5aRTBZNjg4VnVvem9rcEtrX21Qa1RteUpYUFhPanJKTGNBbHNkSGw2enVhaklJSlkyOGhUQTdCR2NyRnRGSzN3Nm1SLUdTSWpra2pzUmRkQW1mR1lsSVhlci1UMkItZ2Z0eWVaeElvM214OVJzRWhNdzY0Z2V6LUh6NmR6cC1JUVNqMHZwNmtHME1pbTR0WDdRZHpiOWhZaWNtQQ==
kind: Secret
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","kind":"Secret","metadata":{"annotations":{"kubernetes.io/service-account.name":"testsa"},"name":"testsa-secret","namespace":"default"},"type":"kubernetes.io/service-account-token"}
    kubernetes.io/service-account.name: testsa
    kubernetes.io/service-account.uid: 039e7c24-37be-4291-818c-39cb2acea726
  creationTimestamp: "2025-01-02T02:16:03Z"
  name: testsa-secret
  namespace: default
  resourceVersion: "252537"
  uid: 61a2410e-06eb-4222-ba61-df9a4589db5e
type: kubernetes.io/service-account-token

# 获取上面的Token值并解码生成变量TOKEN
[root@master1 secret]#TOKEN=$(echo ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNkltdERURWRTV0VwNFozbGpTamxMWlhsTFRrTjZMWE5EZUZsQmJsaE5OR1paY1hSelowTkhjelUzVURnaWZRLmV5SnBjM01pT2lKcmRXSmxjbTVsZEdWekwzTmxjblpwWTJWaFkyTnZkVzUwSWl3aWEzVmlaWEp1WlhSbGN5NXBieTl6WlhKMmFXTmxZV05qYjNWdWRDOXVZVzFsYzNCaFkyVWlPaUprWldaaGRXeDBJaXdpYTNWaVpYSnVaWFJsY3k1cGJ5OXpaWEoyYVdObFlXTmpiM1Z1ZEM5elpXTnlaWFF1Ym1GdFpTSTZJblJsYzNSellTMXpaV055WlhRaUxDSnJkV0psY201bGRHVnpMbWx2TDNObGNuWnBZMlZoWTJOdmRXNTBMM05sY25acFkyVXRZV05qYjNWdWRDNXVZVzFsSWpvaWRHVnpkSE5oSWl3aWEzVmlaWEp1WlhSbGN5NXBieTl6WlhKMmFXTmxZV05qYjNWdWRDOXpaWEoyYVdObExXRmpZMjkxYm5RdWRXbGtJam9pTURNNVpUZGpNalF0TXpkaVpTMDBNamt4TFRneE9HTXRNemxqWWpKaFkyVmhOekkySWl3aWMzVmlJam9pYzNsemRHVnRPbk5sY25acFkyVmhZMk52ZFc1ME9tUmxabUYxYkhRNmRHVnpkSE5oSW4wLkI3SFQtQWx5MWt2Wk1TTGFfSTREWHBGM0lkZ2JVaHJXWkczZXBQdVprcTQtWkpfcGN5MTJabkVCTUttLVRTbTFwNWhrQ3gzQm5NQzJ6QmF0VHJIRmp5TkhQSWRuZFJwMk9NMzZHeHNKOGNna0tOU21FMVg3bmM4R2w0ZkxYcDJXSWdUQVN2ZWFVOFI3UWFlZWhXaXdpNzNLNjVpMjNqNEtFYW9YRHhyS2hmb1RIWkdhVG5hVFdTTFZPNW5aRTBZNjg4VnVvem9rcEtrX21Qa1RteUpYUFhPanJKTGNBbHNkSGw2enVhaklJSlkyOGhUQTdCR2NyRnRGSzN3Nm1SLUdTSWpra2pzUmRkQW1mR1lsSVhlci1UMkItZ2Z0eWVaeElvM214OVJzRWhNdzY0Z2V6LUh6NmR6cC1JUVNqMHZwNmtHME1pbTR0WDdRZHpiOWhZaWNtQQ==|base64 -d)

# 使用上面TOKEN访问，验证用户身份，但权限不足
[root@master1 secret] # curl -s --cacert /etc/kubernetes/pki/ca.crt -H "Authorization:Bearer ${TOKEN}" https://10.0.0.201:6443 
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "forbidden: User \"system:serviceaccount:default:testsa\" cannot get path \"/\"",
  "reason": "Forbidden",
  "details": {},
  "code": 403
}

# 删除
[root@master1 secret] # kubectl delete -f storage-secret-sa.yaml 
serviceaccount "testsa" deleted
```



#### TLS案例

TLS 类型的 Secret 主要用于对**https场景**的证书和密钥文件来进行加密传输

```bash
#tls类型格式
kubectl create secret tls NAME --cert=/path/file --key=/path/file

#注意：
#保存cert文件内容的key名称不能指定，自动为tls.crt，卷挂载后生成的文件名也为tls.crt
#保存private key文件内容的key不能指定,自动为tls.key，卷挂载后生成的文件名也为tls.key

```

![image-20250102102801681](D:\git_repository\cyber_security_learning\markdown_img\image-20250102102801681.png)



下面案例实现一个基于https 的nginx的web服务

#####  创建 TLS 证书文件

```bash
# 生成私钥
[root@master1 tls]# openssl genrsa -out nginx-certs/mystical.org.key 2048

# 生成自签证书
[root@master1 tls]# openssl req -new -x509 -key nginx-certs/mystical.org.key -days 3650 -out nginx-certs/mystical.org.crt -subj /C=CN/ST=Beijing/L=Beijing/O=DevOps/CN=www.mystical.org
#注意：CN指向的域名必须是nginx配置中使用的域名信息

# 查看文件
[root@master1 tls]# ls nginx-certs/
mystical.org.crt  mystical.org.key
```



##### 基于 TLS 证书文件创建对应的 Secret

```yaml
[root@master1 tls] # kubectl create secret tls secret-nginx-ssl --cert=nginx-certs/mystical.org.crt  --key=nginx-certs/mystical.org.key 
secret/secret-nginx-ssl created

# 查看结果
[root@master1 tls] # kubectl get secrets 
NAME               TYPE                DATA   AGE
secret-nginx-ssl   kubernetes.io/tls   2      23s

# 查看内容
[root@master1 tls]#kubectl get secrets secret-nginx-ssl -o yaml
apiVersion: v1
data:
  tls.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURtekNDQW9PZ0F3SUJBZ0lVTjJtZHRnQU1obHNvdlRhbkxaK2F5M29oNW9jd0RRWUpLb1pJaHZjTkFRRUwKQlFBd1hURUxNQWtHQTFVRUJoTUNRMDR4RURBT0JnTlZCQWdNQjBKbGFXcHBibWN4RURBT0JnTlZCQWNNQjBKbAphV3BwYm1jeER6QU5CZ05WQkFvTUJrUmxkazl3Y3pFWk1CY0dBMVVFQXd3UWQzZDNMbTE1YzNScFkyRnNMbTl5Clp6QWVGdzB5TlRBeE1ESXdNak14TlRsYUZ3MHpOREV5TXpFd01qTXhOVGxhTUYweEN6QUpCZ05WQkFZVEFrTk8KTVJBd0RnWURWUVFJREFkQ1pXbHFhVzVuTVJBd0RnWURWUVFIREFkQ1pXbHFhVzVuTVE4d0RRWURWUVFLREFaRQpaWFpQY0hNeEdUQVhCZ05WQkFNTUVIZDNkeTV0ZVhOMGFXTmhiQzV2Y21jd2dnRWlNQTBHQ1NxR1NJYjNEUUVCCkFRVUFBNElCRHdBd2dnRUtBb0lCQVFEaVVZUjVacFoxY2NML0wydVNTZTB0aU5RMVpCVzRFaHN2YVdweHJTbncKeENac3NWb0pnbzV3eExmeTV6dTY1QmFLOTJsR29xbWRUWFYxbG54UTJERWQ0S3JXVmNDQnhlaHNDRGx1bVZUVgpIRGF0QkFpeWtzRWd4bmszNzdma2FHbGtKSmp0dWlCalRNdlNFUnlMYWlWbGI4Y1BjWDFyNzdNNXJMQ3lhdkZDCm5yM21JWWxYQi9POE42N21zdHI3TlNVNkN4ZFgzVkdXVzdRYzFLVFJ4SGhmQ1o0aHd3RTBFOFNZeHZuTTRsUkIKNitidThZbEpsb0JUZGFOQko3NkpaOE5CbzJpcEc0VTZSMmhMNEVPdnkyOGJBOWlCdisyc2RmM3NzQ0F3U1pqUgpab1RoTlQyaXU2cG5sTXR5Nzg5WmFpSTBPMThWZ2hVQ0swYU4zRmRnTE9VN0FnTUJBQUdqVXpCUk1CMEdBMVVkCkRnUVdCQlRGTGhreDFCQTJEMHNTUG1jVnhPNktDSWF0b3pBZkJnTlZIU01FR0RBV2dCVEZMaGt4MUJBMkQwc1MKUG1jVnhPNktDSWF0b3pBUEJnTlZIUk1CQWY4RUJUQURBUUgvTUEwR0NTcUdTSWIzRFFFQkN3VUFBNElCQVFDZwoxTmhtZlcrOTRHTFBuNXE4QlFqcXpzL1ZSSlBGMTNYbXBDVTREczJFdm5ya0JXb0NRYXJlSmdiUjZzMi82R1dKCjVud0Ewbjd4VnBiYk1UV2U0bVdrd3N0STJPRXJhYnhlQml2NVdBeGF5ZzMzOXQ3WkhCQkJpdzFqZU14d28yNm4KMnlJUFkxU0dYMVdoY2RqL21FNVQyZnRYb3RLUHFrUk5lNFBpdDdXRlBEOUlWd3FJdWM3Q3QwSjFDaFpQVWZONgpxdGhaTUd4S2RQbVc4TnZaeU5GUDV6Q2JheXVXQmJFZjc0WE9tQ0Jqa0x4a0NIcHFkTjRwVkhQb3QxUkxRQ3pkCjlhWCsyUS9XMWdkS3pGMzNucnJLSTMzd3Jpclo3UVp5QjVBaHplOUxwMFBiQjRlTFkyUzgvRkxiaWhSZm90SEMKREJaQzltckFsNWNHK0pIeE42OFoKLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
  tls.key: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRRGlVWVI1WnBaMWNjTC8KTDJ1U1NlMHRpTlExWkJXNEVoc3ZhV3B4clNud3hDWnNzVm9KZ281d3hMZnk1enU2NUJhSzkybEdvcW1kVFhWMQpsbnhRMkRFZDRLcldWY0NCeGVoc0NEbHVtVlRWSERhdEJBaXlrc0VneG5rMzc3ZmthR2xrSkpqdHVpQmpUTXZTCkVSeUxhaVZsYjhjUGNYMXI3N001ckxDeWF2RkNucjNtSVlsWEIvTzhONjdtc3RyN05TVTZDeGRYM1ZHV1c3UWMKMUtUUnhIaGZDWjRod3dFMEU4U1l4dm5NNGxSQjYrYnU4WWxKbG9CVGRhTkJKNzZKWjhOQm8yaXBHNFU2UjJoTAo0RU92eTI4YkE5aUJ2KzJzZGYzc3NDQXdTWmpSWm9UaE5UMml1NnBubE10eTc4OVphaUkwTzE4VmdoVUNLMGFOCjNGZGdMT1U3QWdNQkFBRUNnZ0VBQ3Bvb3NML3FadGhzVUU4VTVOYXd2K21CT00vQS9XSzFGNmRYdjJQamdKak4KSWdTOFErWWVyU1ZuWnFveXovZTFIMC9RTHo1dk5XUWhEMS84TlQ5WTF3ajZNb05Ka0VBZUQzTGloSTRMVXRaNQpCZW1YOTJHaVNZVHl2YzVDN2t0K2tISHZJTWZrNTRkUlR4SFNlcXpVMFZLSFgrK3E5cWovMjVaUzlYREd4UE9iClFzQW5KejYrb2syVDhwMWNNZXZqSUZUWkIrbk8vYmhQWkZUZHAwalZ5WWhsMHkvRXk2Z2pEQ1pBaEM3UFFZck4KQ2lLZWpSL2ZpQ1NUaURkSXJ0Y2JoQmlCL2xVZWhyd3JldnpvOWhFcnBWb3daeThhRHVERVkxL0ZWTVRsMUc0agppTWhMcUxSYkFFZ1R6T1pNYUY4TU5KNTR4KzZURFAxTldxcUFDYkt1VFFLQmdRRHdydGR2cmVHOTJmTWVNT3RHCnhhdFpZUDZWd2laYU0zbmJIN1B3UkxXMkVjODlaMjRLVnJhUGt6bjhWOC8ySTNBTVVhRElxeTlvb0ZWNThzeEoKc044VWcxdzZObTZQR043UWFEUUR3ZWRxbGtxSzFzK0dXWFVZWXVjUmM2eE5ESm5EZHlKRmJPc05ubzdCNlRabAppWGhtdVJ6NWl0V1RrWVg4YldkVkpRdkwvUUtCZ1FEd3VLYlEvS3A2NUs2aXJVM3dXZzJlK0RIUlZUZWwrV1F4Cm9JbUJVODFkNUVMVzFUNHdOZSs4WWxoVmJwR0lMeTczeWo3a2xBY2VsMlJJM3JqK0xtd05iNFZPN05LTkc1VkwKNW5tdW4wcUlocUNya1ZOL2hWcUovK1h1eFJtMWpmYlRROURCSHl6WVJJVjBKU3QvV2tmUnFTeFE2Wk5zTXlZawp0RTYwZVQ3UGx3S0JnUUNtYVMwNTRXN2d0bzQ3UkxXWUpGb2FIVTlKT29rTCt1VjVGVTF6aGY1aG1hVEJudjdkCmxTRDYybC9RVXVMT0c2aUFTL3d3WXZRUGtqUW5jakcvamRSZ09ZY09GTTZTa0M2V3lFV1doMzQ3R3hrRk1Bc2kKcUQybkU5TVNKUGx2K0pOa0s3MzlaSmFNdnlHVGYyMEYvV3ZMRXBpdkRVZ29sUWlnQlFEYVJSZ0gvUUtCZ0d1dgp6MENTcDVsT2tDbEtLaUdweDRva01mVVprRWw1cGE3bHlGM0lwWWlwUXBWazArc3hWY3dLbXNXdEx3R2pTZm1qCnlqcnJWYndEc2VNL2I3YVdBZFNJM1RRUGthbDZlM0YyNjF5SStnalZZUzhmVmlFb0FQYlhPWDkxUVNrTkZ5d3YKbkVXb3NxRVZGalo5SWxaWWh1UnVMOXNLZ3Q3V2l1dkVsYWo2ekhTRkFvR0JBSTFaZnFiK2VpVkhDU0JBaHN5bgpiYzRRazlHNmxoaXByYnZlQXRTUjRsWnFXeWlXdmpvZU5WZWVJVk14Wm1XVUtEZ29ZZDNPNC96RFpmYm9PNCtqCk1QWk40RzhrYS9IcWNKRFl0N3pzRXJ5WU5QVnVNSmsyTzhMcXAxbzBwdVM2cUFoaDVXVjJ1c1UvNXZKZDY0emcKa05ENWk5S3E3b250YzRHdVVvWTRpeGdLCi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0K
kind: Secret
metadata:
  creationTimestamp: "2025-01-02T02:35:26Z"
  name: secret-nginx-ssl
  namespace: default
  resourceVersion: "254403"
  uid: e4c5eeac-23a3-4412-8f7e-c07dbf5dc837
type: kubernetes.io/tls
```



准备Nginx配置文件

```bash
# nginx主配置文件 myserver.conf
[root@master1 tls]#vim myserver.conf
server {
    listen 80;
    server_name www.mystical.org;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name www.mystical.org;
    
     ssl_certificate /etc/nginx/certs/tls.crt; 
     ssl_certificate_key /etc/nginx/certs/tls.key;
     ssl_session_timeout 5m;
     ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; 
     ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; 
     ssl_prefer_server_ciphers on;
     include /etc/nginx/conf.d/myserver-*.cfg;

     location / {
         root /usr/share/nginx/html;
     }
}

# nginx的压缩配置文件:myserver-gzip.cfg
[root@master1 tls]#vim myserver-gzip.cfg
gzip on;
gzip_comp_level 5;
gzip_proxied     expired no-cache no-store private auth;
gzip_types text/plain text/css application/xml text/javascript;


# nginx的状态页配置文件myserver-status.cfg
[root@master1 tls]#vim myserver-status.cfg
location /status {
   stub_status on;
   access_log off;
}
```



#####  创建配置文件对应的 Configmap

```bash
# 查看配置文件
[root@master1 tls]# ls nginx-ssl-conf.d/
myserver.conf  myserver-gzip.cfg  myserver-status.cfg

# 创建cm
[root@master1 tls]# kubectl create configmap cm-nginx-ssl-conf --from-file=nginx-ssl-conf.d/
configmap/cm-nginx-ssl-conf created

# 查看
[root@master1 tls]# kubectl get cm
NAME                DATA   AGE
cm-nginx-ssl-conf   3      42s
kube-root-ca.crt    1      4d18h
```



##### 创建引用Secret和configmap资源配置文件

```yaml
# 创建资源配置文件
[root@master1 tls] # cat storage-secret-nginx-ssl.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: pod-nginx-ssl
  namespace: default
spec:
  volumes:
  - name: nginx-certs
    secret:
      secretName: secret-nginx-ssl
  - name: nginx-confs
    configMap:
      name: cm-nginx-ssl-conf
      optional: false
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: nginx-ssl-server
    volumeMounts:
    - name: nginx-certs
      mountPath: /etc/nginx/certs/  # 其保存cert文件自动命名为tls.crt，而private key文件会自动命名为tls.key
      readOnly: true
    - name: nginx-confs
      mountPath: /etc/nginx/conf.d/
      readOnly: true


# 应用
[root@master1 tls] # kubectl apply -f storage-secret-nginx-ssl.yaml 
pod/pod-nginx-ssl created

# 验证结果
[root@master1 tls] # kubectl get pod pod-nginx-ssl -o wide
NAME            READY   STATUS    RESTARTS   AGE   IP             NODE    NOMINATED NODE   READINESS GATES
pod-nginx-ssl   1/1     Running   0          24s   10.244.3.150   node3   <none>           <none>

# 查看生成的证书文件，表示为关联时间戳目录下的两个双层软链接文件tls.crt和tls.key,保存证书的原始文件,而非base64格式
[root@master1 tls] # kubectl exec -it pod-nginx-ssl -- ls -l /etc/nginx/certs/
total 0
lrwxrwxrwx 1 root root 14 Jan  2 02:47 tls.crt -> ..data/tls.crt
lrwxrwxrwx 1 root root 14 Jan  2 02:47 tls.key -> ..data/tls.key

# 访问Pod
[root@master1 tls]#curl -H'host: www.mystical.org' http://10.244.3.150 -I
HTTP/1.1 301 Moved Permanently
Server: nginx/1.20.0
Date: Thu, 02 Jan 2025 02:59:02 GMT
Content-Type: text/html
Content-Length: 169
Connection: keep-alive
Location: https://www.mystical.org/

[root@master1 tls] # curl 10.244.3.150 -kL
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
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

# 清理环境
[root@master1 tls] # kubectl delete -f storage-secret-nginx-ssl.yaml 
pod "pod-nginx-ssl" deleted
[root@master1 tls] # kubectl delete cm cm-nginx-ssl-conf 
configmap "cm-nginx-ssl-conf" deleted
[root@master1 tls] # kubectl delete secrets tls secret-nginx-ssl 
secret "secret-nginx-ssl" deleted
```



#### Docker-registry案例

有时Docker的仓库是私有的,如果想下载镜像,就需要在下载镜像的主机上登录仓库并认证后才能实现

但是在Kubernetes集群使用私有仓库镜像就比较繁琐,因为运行Pod 的宿主机并不固定,如果在每个 worker节点登录验证显然是不方便的

dockercfg及dockerconfigjson类型的Secret 适用于实现让kubelet从私有Image Registry中下载容器镜像

其引用定义在pod.spec.imagePullSecrets字段上的列表,即支持多个docker-registry类型的Secret,从上至下逐个进行匹配



**创建此种secret 可以通过下面方式实现**

**方法1: 通过命令创建**

```bash
kubectl create secret docker-registry KEYNAME --docker-server=DOCKER_REGISTRY_SERVER --docker-username=DOCKER_USER --docker-password=DOCKER_PASSWORD --docker-email=EMAIL
```



**方式二: 通过docker认证文件创建**

```bash
# 先登录并认证到目标仓库server上，认证凭据自动保存在~/.docker/config.json文件中
docker login --username=DOCKER_USER DOCKER_REGISTRY_SERVER

#基于config.json文件生成secret
kubectl create secret docker-registry KEYNAME --from-file=.dockerconfigjson=path/to/.docker/config.json

kubectl create secret generic KEYNAME --type='kubernetes.io/dockerconfigjson' --from-file=.dockerconfigjson=/root/.docker/config.json

# 示例
kubectl create secret docker-registry my-secret --from-file=.dockerconfigjson=path/to/.docker/config.json

kubectl create secret generic dockerharbor-auth --
type='kubernetes.io/dockerconfigjson' --from-file=.dockerconfigjson=/root/.docker/config.json
```





##### 通过命令创建私有仓库登录认证信息



**安装并创建Harbor的私有仓库和项目**

```bash
# 下载harbor的包
wget https://www.mysticalrecluse.com/script/tools/harbor-offline-installer-v2.11.0.tgz
# 使用脚本下载并部署harbor
wget https://www.mysticalrecluse.com/script/Shell/install_harbor.sh
bash install_harbor.sh
......
Harbor 安装完成

Harbor安装完成!                                            [  OK  ]
-------------------------------------------------------------------
请访问链接: http://10.0.0.131/
用户和密码: admin/123456
```

![image-20250102141543930](D:\git_repository\cyber_security_learning\markdown_img\image-20250102141543930.png)



##### 创建Harbor用户

![image-20250102141832106](D:\git_repository\cyber_security_learning\markdown_img\image-20250102141832106.png)



##### 给library项目添加成员

![image-20250102141948806](D:\git_repository\cyber_security_learning\markdown_img\image-20250102141948806.png)



##### 将harbor的域名解析添加到域名服务器上

```bash
[root@ubuntu2204 ~]#cat /etc/bind/db.mystical.org 
$TTL 86400

@ IN  SOA dns1 msticalrecluse.gmail.com (123 12H 10M 3D 1D)

  IN  NS dns1

dns1 A 10.0.0.131
harbor A 10.0.0.131
feng A 11.11.11.11
nfs A 10.0.0.131

# 之前在CoreDNS上已经指定了转发的DNS服务器为10.0.0.131
# 随便创建一个Pod测试
[root@master1 yaml]# kubectl apply -f myapp.yaml 
deployment.apps/myapp created

# 成功解析
[root@master1 yaml]#kubectl exec myapp-7b94444f8d-7zqjv -- ping harbor.mystical.org
PING harbor.mystical.org. (10.0.0.131): 56 data bytes
64 bytes from 10.0.0.131: seq=0 ttl=63 time=0.755 ms
64 bytes from 10.0.0.131: seq=1 ttl=63 time=0.190 ms

# 更改harbor的yaml文件，指定域名访问
[root@ubuntu2204 ~]#vim /usr/local/harbor/harbor.yml
hostname: harbor.mystical.org  # ---这里更改为指定域名，后续使用域名访问harbor

# 使用prepare重新生成脚本
[root@ubuntu2204 harbor]# ls
common     docker-compose.yml     harbor.yml       install.sh  prepare
common.sh  harbor.v2.11.0.tar.gz  harbor.yml.tmpl  LICENSE
[root@ubuntu2204 harbor]# ./prepare 
prepare base dir is set to /usr/local/harbor
WARNING:root:WARNING: HTTP protocol is insecure. Harbor will deprecate http protocol in the future. Please make sure to upgrade to https
Clearing the configuration file: /config/nginx/nginx.conf
Clearing the configuration file: /config/registryctl/config.yml
Clearing the configuration file: /config/registryctl/env
Clearing the configuration file: /config/db/env
Clearing the configuration file: /config/log/rsyslog_docker.conf
Clearing the configuration file: /config/log/logrotate.conf
Clearing the configuration file: /config/registry/config.yml
Clearing the configuration file: /config/registry/root.crt
Clearing the configuration file: /config/registry/passwd
Clearing the configuration file: /config/core/env
Clearing the configuration file: /config/core/app.conf
Clearing the configuration file: /config/portal/nginx.conf
Clearing the configuration file: /config/jobservice/config.yml
Clearing the configuration file: /config/jobservice/env
Generated configuration file: /config/portal/nginx.conf
Generated configuration file: /config/log/logrotate.conf
Generated configuration file: /config/log/rsyslog_docker.conf
Generated configuration file: /config/nginx/nginx.conf
Generated configuration file: /config/core/env
Generated configuration file: /config/core/app.conf
Generated configuration file: /config/registry/config.yml
Generated configuration file: /config/registryctl/env
Generated configuration file: /config/registryctl/config.yml
Generated configuration file: /config/db/env
Generated configuration file: /config/jobservice/env
Generated configuration file: /config/jobservice/config.yml
loaded secret from file: /data/secret/keys/secretkey
Generated configuration file: /compose_location/docker-compose.yml
Clean up the input dir

# 删除之前的docker compose起的harbor，重新创建harbor
[root@ubuntu2204 harbor]# docker-compose down
Stopping harbor-jobservice ... done
Stopping nginx             ... done
Stopping harbor-core       ... done
Stopping redis             ... done
Stopping harbor-db         ... done
Stopping harbor-portal     ... done
Stopping registry          ... done
Stopping registryctl       ... done
Stopping harbor-log        ... done
Removing harbor-jobservice ... done
Removing nginx             ... done
Removing harbor-core       ... done
Removing redis             ... done
Removing harbor-db         ... done
Removing harbor-portal     ... done
Removing registry          ... done
Removing registryctl       ... done
Removing harbor-log        ... done
Removing network harbor_harbor

# 重新使用service启动harbor
[root@ubuntu2204 harbor]# systemctl start harbor.service 
```



##### 更改宿主机上的host文件后，使用域名登录harbor

![image-20250102145733724](D:\git_repository\cyber_security_learning\markdown_img\image-20250102145733724.png)



##### 使docker信任harbor，修改所有节点上的docker配置

```bash
# 修改所有集群节点的Docker配置支持私有仓库
[root@node1 ~]# vim /etc/docker/daemon.json 
{
      "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"],
      "insecure-registries": ["harbor.mystical.org"], # 添加此行
      "no-proxy": "127.0.0.0/8,172.17.0.0/16,10.0.0.0/24,10.244.0.0/16,192.168.0.0/16,wang.org,cluster.local,harbor.mystical.org" # 如果配了代理，在代理中将harbor.mystical.org排除，也就是添加harbor.mystical.org在noproxy字段
     }

# 更改代理配置，修改 /etc/systemd/system/docker.service.d/http-proxy.conf 文件
[root@node1 ~]# vim /etc/systemd/system/docker.service.d/http-proxy.conf
[Service]
Environment="NO_PROXY=127.0.0.0/8,172.17.0.0/16,10.0.0.0/24,10.244.0.0/16,192.168.0.0/16,wang.org,cluster.local,harbor.mystical.org" # 修改这行


# 重启docker
[root@node1 ~]#systemctl daemon-reload
[root@node1 ~]# systemctl restart docker

# 查看
[root@node1 ~]#docker info
......
 HTTP Proxy: http://10.0.0.1:10809/
 HTTPS Proxy: http://10.0.0.1:10809/
 # 在noproxy中添加harbor.mystical.org
 No Proxy: 127.0.0.0/8,172.17.0.0/16,10.0.0.0/24,10.244.0.0/16,192.168.0.0/16,wang.org,cluster.local,harbor.mystical.org
 Experimental: false
 # 添加信任
 Insecure Registries:
  harbor.mystical.org
  127.0.0.0/8
 Registry Mirrors:
  https://si7y70hh.mirror.aliyuncs.com/
 Live Restore Enabled: false
 Product License: Community Engine


# 登录测试
[root@node1 ~]# docker login harbor.mystical.org -u mystical -p 'Zyf646130..'
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```



##### 使用命令行方式创建docker-registry类型的secret

```bash
[root@master1 yaml]# kubectl create secret docker-registry harbor-docker-registry-secret --docker-server=harbor.mystical.org --docker-username=mystical --docker-password=Zyf646130..
secret/harbor-docker-registry-secret created

# 查看
[root@master1 yaml]# kubectl get secret
NAME                            TYPE                             DATA   AGE
harbor-docker-registry-secret   kubernetes.io/dockerconfigjson   1      21s

```



##### 使用admin账号，创建一个私有项目example，并添加成员mystical

![image-20250102153457019](D:\git_repository\cyber_security_learning\markdown_img\image-20250102153457019.png)

![image-20250102153558659](D:\git_repository\cyber_security_learning\markdown_img\image-20250102153558659.png)



##### 在node节点测试私有仓能否上传下载镜像

```bash
# 登录
[root@node3 ~]#docker login harbor.mystical.org -u mystical -p 'Zyf646130..'
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

# 查看docker镜像，选一个上传到harbor仓库
[root@node3 ~]#docker images

# 更改镜像tag名称
[root@node3 ~]#docker tag registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0 harbor.mystical.org/example/nginx:1.20.0

# 上传成功
[root@node3 ~]#docker push harbor.mystical.org/example/nginx:1.20.0
The push refers to repository [harbor.mystical.org/example/nginx]
272bc57d3405: Pushed 
f7141923aaa3: Pushed 
9b63e6289fbe: Pushed 
a2f4f809e04e: Pushed 
1839f9962bd8: Pushed 
02c055ef67f5: Pushed 
1.20.0: digest: sha256:598057a5c482d2fb42092fd6f4ba35ea4cc86c41f5db8bb68d1ab92c4c40db98 size: 1570
```



##### 使用创建的secret让k8s从私有仓中拉取镜像

```bash
[root@master1 yaml]#cat storage-secret-docker-registry-harbor.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-harbor-docker-registry-secret
spec:
  replicas: 3
  selector:
    matchLabels:
      app: pod-test-harbor-docker-registry-secret
  template:
    metadata:
      labels:
        app: pod-test-harbor-docker-registry-secret
    spec:
      containers:
      - name: pod-test-harbor-docker-registry-secret
        image: harbor.mystical.org/example/nginx:1.20.0
      imagePullSecrets:
      - name: harbor-docker-registry-secret  # 指定docker-registry类型的secret，如果有多个会逐个验证

# 应用
[root@master1 yaml]# kubectl apply -f storage-secret-docker-registry-harbor.yaml 
deployment.apps/deployment-harbor-docker-registry-secret created

# 查看
[root@master1 yaml]#kubectl get pod -o wide
NAME                                                       READY   STATUS    RESTARTS      AGE   IP             NODE    NOMINATED NODE   READINESS GATES
deployment-harbor-docker-registry-secret-97787d89c-fbw8v   1/1     Running   0             22s   10.244.1.143   node1   <none>           <none>
deployment-harbor-docker-registry-secret-97787d89c-plcdx   1/1     Running   0             22s   10.244.2.88    node2   <none>           <none>
deployment-harbor-docker-registry-secret-97787d89c-tgzmx   1/1     Running   0             22s   10.244.3.154   node3   <none>           <none>
myapp-7b94444f8d-7zqjv                                     1/1     Running   2 (20m ago)   88m   10.244.2.86    node2   <none>           <none>
myapp-7b94444f8d-9x8xk                                     1/1     Running   1 (20m ago)   88m   10.244.3.152   node3   <none>           <none>
myapp-7b94444f8d-dh7jd                                     1/1     Running   4 (28m ago)   88m   10.244.1.140   node1   <none>           <none>
```





### downwardAPI

#### dockerwardAPI介绍

在Kubernetes中 可以基于一种 downwardAPI 的对象，**将宿主机相关的信息以存储卷的样式加载到pod内部**。

相较于configmap、secret等资源对象需要创建后才能使用，downwardAPI 不是存储卷，无需人为创 建，它自身一直就存在。

downwardAPI 不是一种独立的API资源类型，只是一种引用Pod自身的运行环境信息

downwardAPI 包括Pod的metadata,spect或status字段值，将这些信息注入到容器内部的方式

downwardAPI 为运行在pod中的应用容器提供了一种反向引用。让容器中的应用程序了解所处pod或 Node的一些基础属性信息。



![image-20250102155831373](D:\git_repository\cyber_security_learning\markdown_img\image-20250102155831373.png)



不过，**通常只有常量类型的属性**才能够通过环境变量注入到容器中，毕竟，在进程启动完成后无法再向 其告知变量值的变动，于是，环境变量也就不支持中途的更新操作。



**DownwardAPI提供了两种方式用于将 Pod 的信息注入到容器内部**

- **环境变量**：用于单个变量，可以将 Pod 信息和容器信息直接注入容器内部
- **Volume挂载**：将 Pod 信息生成为文件，再挂载到容器内部中



类似于ConfigMap或Secret资源，容器能够在环境变量中**valueFrom字段**中基于**两个字段**来引用其所属 Pod对象的元数据信息

- **fieldRef**：引用常规性的元数据
- **resourceFieldRef**：引用和资源限制和资源请求相关的元数据



**Downward API fields injected via the fieldRef field**

| Field                       | Description                                                  | Allowed in env | Allowed in volume |
| --------------------------- | ------------------------------------------------------------ | -------------- | ----------------- |
| metadata.name               | The pod’s name.                                              | Yes            | Yes               |
| metadata.namespace          | The pod’s namespace.                                         | Yes            | Yes               |
| metadata.uid                | The pod’s UID.                                               | Yes            | Yes               |
| metadata.labels             | All the pod’s labels, one label per line, formatted as key=” value” . | No             | Yes               |
| metadata.labels['key']      | The value of the specified label.                            | Yes            | Yes               |
| metadata.annotations        | All the pod’s annotations, one per line, formatted as key=” value” . | No             | Yes               |
| metadata.annotations['key'] | The value of the specified annotation.                       | Yes            | Yes               |
| spec.nodeName               | The name of the worker node the pod runs on.                 | Yes            | No                |
| spec.serviceAccountName     | The name of the pod’s service account.                       | Yes            | No                |
| status.podIP                | The pod’s IP address                                         | Yes            | No                |
| status.hostIP               | The worker node’s IP address.                                | Yes            | No                |



**Table 9.6 Downward API resource fields injected via the resourceFieldRef field**

| Resource field             | Description                                | Allowed in env | Allowed in vol |
| -------------------------- | ------------------------------------------ | -------------- | -------------- |
| requests.cpu               | The container’s CPU request.               | Yes            | Yes            |
| requests.memory            | The container’s memory request.            | Yes            | Yes            |
| requests.ephemeral-storage | The container’s ephemeral storage request. | Yes            | Yes            |
| limits.cpu                 | The container’s CPU limit.                 | Yes            | Yes            |
| limits.memory              | The container’s memory limit.              | Yes            | Yes            |
| limits.ephemeral-storage   | The container’s ephemeral storage limit.   | Yes            | Yes            |



#### downwardAPI案例

##### 范例：获取基本的变量信息通过变量方式引用

```yaml
# 定制的资源对象
[root@master1 yaml] # vim storage-downwardapi-env-test.yaml
apiVersion: v1
kind: Pod
metadata:
  name: downwardapi-env-test
  labels:
    app: downwardapi-env
spec:
  containers:
  - name: downwardapi-env-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    resources:
      requests:
        memory: "32Mi"
        cpu: "250m"
      limits:
        memory: "64Mi"
        cpu: "500m"
    env:
    - name: THIS_POD_NAME
      valueFrom:
        fieldRef:                 
          fieldPath: metadata.name 
          # "fieldPath"指定的是 Pod 的某些元数据字段的路径，它告诉 Kubernetes 要从 Pod 的哪些部分提取值。
    - name: THIS_POD_NAMESPACE
      valueFrom:
        fieldRef:
          fieldPath: metadata.namespace
    - name: THIS_APP_LABEL
      valueFrom:
        fieldRef:
          fieldPath: metadata.labels['app']
    - name: THIS_CPU_LIMIT
      valueFrom:
        resourceFieldRef:
          resource: limits.cpu
    - name: THIS_MEM_REQUEST
      valueFrom:
        resourceFieldRef:
          resource: requests.memory
          divisor: 1Mi
    - name: VAR_REF
      value: $(THIS_POD_NAMESPACE).wang.org  # 变量引用格式:$(VAR_NAME)


[root@master1 yaml] # kubectl apply -f storage-downwardapi-env-test.yaml 
pod/downwardapi-env-test created

[root@master1 yaml] # kubectl get pod
NAME                   READY   STATUS    RESTARTS   AGE
downwardapi-env-test   1/1     Running   0          2m36s

# 查看环境变量
[root@master1 yaml] # kubectl exec -it downwardapi-env-test -- env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=downwardapi-env-test
TERM=xterm
THIS_APP_LABEL=downwardapi-env
THIS_CPU_LIMIT=1
THIS_MEM_REQUEST=32
VAR_REF=default.wang.org
THIS_POD_NAME=downwardapi-env-test
THIS_POD_NAMESPACE=default
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
DEPLOYENV=Production
RELEASE=Stable
PS1=[\u@\h \w]\$ 
HOME=/root

# 删除
[root@master1 yaml]#kubectl delete pod downwardapi-env-test 
pod "downwardapi-env-test" deleted
```



##### 范例：存储卷方式使用

```yaml
[root@master1 yaml] # vim storage-downwardapi-volume-test.yaml
apiVersion: v1
kind: Pod
metadata:
  name: downwardapi-volume-test
  labels:
    zone: Beijing
    rack: zhongguancun
    app: redis-master
  annotations:
    region: Asia-China
spec:
  volumes:
  - name: podinfo
    downwardAPI:
      defaultMode: 0420  # 文件权限，默认0644
      items:
      - fieldRef:
          fieldPath: metadata.namespace
        path: pod_namespace
      - fieldRef:
          fieldPath: metadata.labels
        path: pod_labels
      - fieldRef:
          fieldPath: metadata.annotations
        path: pod_annotations
      - resourceFieldRef:
          containerName: downwardapi-volume-test
          resource: limits.cpu
        path: "cpu_limit"
      - resourceFieldRef:
          containerName: downwardapi-volume-test
          resource: requests.memory
          divisor: "1Mi"              # 将资源值进行整除操作，从而将资源值转换为以指定单位为基准的整数值。
        path: "mem_request"
  containers:
  - name: downwardapi-volume-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    resources:
      requests:
        memory: "32Mi"
        cpu: "250m"
      limits:
        memory: "64Mi"
        cpu: "500m"
    volumeMounts:
    - name: podinfo
      mountPath: /etc/podinfo
      readOnly: false

# 应用
[root@master1 yaml] # kubectl apply -f storage-downwardapi-volume-test.yaml 
pod/downwardapi-volume-test created

# 查看
[root@master1 yaml]#kubectl get pod
NAME                      READY   STATUS    RESTARTS   AGE
downwardapi-volume-test   1/1     Running   0          3s

# 查看容器内挂载的文件及其内容
[root@master1 yaml] # kubectl exec downwardapi-volume-test -- ls /etc/podinfo -l
total 0
lrwxrwxrwx    1 root     root            16 Jan  2 09:31 cpu_limit -> ..data/cpu_limit
lrwxrwxrwx    1 root     root            18 Jan  2 09:31 mem_request -> ..data/mem_request
lrwxrwxrwx    1 root     root            22 Jan  2 09:31 pod_annotations -> ..data/pod_annotations
lrwxrwxrwx    1 root     root            17 Jan  2 09:31 pod_labels -> ..data/pod_labels
lrwxrwxrwx    1 root     root            20 Jan  2 09:31 pod_namespace -> ..data/pod_namespace

[root@master1 yaml] # kubectl exec downwardapi-volume-test -- cat /etc/podinfo/pod_labels
app="redis-master"
rack="zhongguancun"
zone="Beijing"

# 删除
[root@master1 yaml] # kubectl delete pod downwardapi-volume-test 
pod "downwardapi-volume-test" deleted
```





### Projected

#### Projected说明

之前的CM,Secret等卷资源在Pod内的一个目录同时只能挂载一个卷，而我们有时希望在一个目录内生成 来自多个卷的多个文件

**Projected volumes 是一种特殊的卷类型，支持同时投射多个卷至同一个挂载点**

Projected 不是一个独立的API 资源类型，但其可以引用现有的configmap、secret资源对象，或 downwardAPI中的元数据信息

此类的卷一般用于为容器提供预先定义好的数据

![image-20250102174640664](D:\git_repository\cyber_security_learning\markdown_img\image-20250102174640664.png)



**Projected Volume仅支持对如下四种类型的卷（数据源）进行投射操作**

- **Secret**：投射Secret对象
- **ConfigMap**：投射ConfgMap对象
- **DownwardAPI**：投射Pod元数据
- **ServiceAccountToken**：投射ServiceAccountToken



#### Projected案例

##### 范例：Example configuration with a secret, a downwardAPI, and a configMap

```yaml
# 资源清单文件
[root@master1 yaml] # vim storage-projected-demo.yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
  namespace: default
data:
  username: d2FuZ3hpYW9jaHVu
type: Opaque
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: myconfigmap
  namespace: default
data:
  myconfig: Hello, Myconfig
---
apiVersion: v1
kind: Pod
metadata:
  name: projected-volume-demo
spec:
  containers:
  - name: container-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    volumeMounts:
    - name: all-in-one
      mountPath: "/projected-volume"
      readOnly: true
  volumes:
  - name: all-in-one
    projected:
      sources:
      - secret:
          name: mysecret
          items:
          - key: username
            path: my-group/my-username
      - downwardAPI:
          items:
          - path: "labels"
            fieldRef:
              fieldPath: metadata.labels
          - path: "cpu_limit"
            resourceFieldRef:
              containerName: container-test
              resource: limits.cpu
      - configMap:
          name: myconfigmap
          items:
          - key: myconfig
            path: my-group/my-config

# 应用
[root@master1 yaml] # kubectl apply -f storage-projected-demo.yaml 
secret/mysecret unchanged
configmap/myconfigmap unchanged
pod/projected-volume-demo created

# 查看
[root@master1 yaml] # kubectl get pod
NAME                    READY   STATUS    RESTARTS   AGE
projected-volume-demo   1/1     Running   0          7s

# 查看挂载文件
[root@master1 yaml] # kubectl exec projected-volume-demo -- ls /projected-volume -l
total 0
lrwxrwxrwx    1 root     root            16 Jan  2 10:03 cpu_limit -> ..data/cpu_limit
lrwxrwxrwx    1 root     root            13 Jan  2 10:03 labels -> ..data/labels
lrwxrwxrwx    1 root     root            15 Jan  2 10:03 my-group -> ..data/my-group

[root@master1 yaml] # kubectl exec projected-volume-demo -- ls /projected-volume/my-group/  -l
total 8
-rw-r--r--    1 root     root            15 Jan  2 10:03 my-config
-rw-r--r--    1 root     root            12 Jan  2 10:03 my-username

```



### 综合案例：使用持久卷部署WordPress和MySQL

在kubernetes部署 wordpress，要满足以下要求：

- 部署一个独立的nginx Pod实例，为wordpress提供反向代理；同时提供https和http虚拟主机，其中发往http的请求都重定向给https；以ConfigMap和Secret提供必要的配置
- 独立部署两个wordpress Pod实例，它们使用NFS StorageClass 存储卷存储用户上传的图片或文 件等数据；以ConfigMap和Secret提供必要的配置
- 部署一个MySQL数据库；以ConfigMap和Secret提供必要的配置
- service 暴露 nginx的服务，然后以反向代理的方式进行访问
- 动态的蓝绿发布和滚动发布
  - 对于wordpress 来说，没有本质的区别
  - nginx的更新，依赖configmap和secret的内容



**简单版：无nginx反向代理**

```yaml
# 提前准备好动态置备程序的Pod，sa
# 提前准备名为sc-nfs的storageClass
[root@master1 yaml] # kubectl get sc
NAME     PROVISIONER                                   RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
sc-nfs   k8s-sigs.io/nfs-subdir-external-provisioner   Delete          Immediate           false                  2d8h

[root@master1 nsf-provisioner] # kubectl get pod -n nfs-provisioner-demo 
NAME                                      READY   STATUS    RESTARTS   AGE
nfs-client-provisioner-649b64df96-tq8hq   1/1     Running   0          7m29s

[root@master1 nsf-provisioner] # kubectl get sa -n nfs-provisioner-demo 
NAME                     SECRETS   AGE
default                  0         8m27s
nfs-client-provisioner   0         8m27s

# 清单文件
[root@master1 yaml] # cat mysql-wordpress-persistent-volume.yaml 
apiVersion: v1
kind: Secret
metadata:
  name: mysql-pass
type: kubernetes.io/basic-auth
data:
  password: MTIzNDU2

---
apiVersion: v1
kind: Service
metadata:
  name: wordpress-mysql
  labels: 
    app: wordpress
spec:
  ports:
  - port: 3306
  selector:
    app: wordpress
    tier: mysql
  clusterIP: None

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
  labels:
    app: wordpress
spec:
  storageClassName: sc-nfs
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress-mysql
  labels:
    app: wordpress
spec:
  selector:
    matchLabels:
      app: wordpress
      tier: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
        tier: mysql
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
        name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        - name: MYSQL_DATABASE
          value: wordpress
        - name: MYSQL_USER
          value: wordpress
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        ports:  # ports 本身不对容器的端口监听产生实际作用，只是一个声明。但是，它在 Kubernetes 资源协作、文档化、以及某些工具中，间接具有重要意义。
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-persistent-storage
        persistentVolumeClaim:
          claimName: mysql-pv-claim
---
apiVersion: v1
kind: Service
metadata:
  name: wordpress
  labels:
    app: wordpress
spec:
  ports:
  - port: 80
  selector:
    app: wordpress
    tier: frontend
  type: LoadBalancer
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: wp-pv-claim
  labels:
    app: wordpress
spec:
  storageClassName: sc-nfs
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
  labels:
    app: wordpress
spec:
  selector:
    matchLabels:
      app: wordpress
      tier: frontend
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
        tier: frontend
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache
        name: wordpress
        env:
        - name: WORDPRESS_DB_HOST
          value: wordpress-mysql
        - name: WORDPRESS_DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        - name: WORDPRESS_DB_USER
          value: wordpress
        ports:
        - containerPort: 80
          name: wordpress
        volumeMounts:
        - name: wordpress-persistent-storage
          mountPath: /var/www/html
      volumes:
      - name: wordpress-persistent-storage
        persistentVolumeClaim:
          claimName: wp-pv-claim

#应用
[root@master1 yaml] # kubectl apply -f mysql-wordpress-persistent-volume.yaml 
secret/mysql-pass created
service/wordpress-mysql created
persistentvolumeclaim/mysql-pv-claim created
deployment.apps/wordpress-mysql created
service/wordpress created
persistentvolumeclaim/wp-pv-claim created
deployment.apps/wordpress created

# 查看
[root@master1 yaml] # kubectl get svc
NAME              TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes        ClusterIP      10.96.0.1      <none>        443/TCP        5d4h
wordpress         LoadBalancer   10.102.38.58   <pending>     80:31889/TCP   31s
wordpress-mysql   ClusterIP      None           <none>        3306/TCP       31s

# 浏览器访问10.0.0.202:31889
```



![image-20250102204154945](D:\git_repository\cyber_security_learning\markdown_img\image-20250102204154945.png)





**进阶：完全按要求配置**

![image-20250103172728642](D:\git_repository\cyber_security_learning\markdown_img\image-20250103172728642.png)



```yaml
# 目录结构
[root@master1 lnmp] # ls
mysql  nginx  nginx.conf.d  plugin  wordpress

[root@master1 lnmp] # tree .
.
├── mysql
│   ├── lnmp-mysql.yaml
│   └── service-mysql.yaml
├── nginx
│   ├── lnmp-nginx-deloyment.yaml
│   ├── service-nginx.yaml
│   └── tls
│       ├── mystical.org.crt
│       └── mystical.org.key
├── nginx.conf.d
│   └── wordpress.mystical.org.conf
├── plugin
│   ├── metalLB
│   │   ├── metallb-native.yaml
│   │   ├── service-metallb-IPAddressPool.yaml
│   │   └── service-metallb-L2Advertisement.yaml
│   └── nfc-sc
│       ├── nfs-client-provisioner.yaml
│       ├── nfs-storageClass.yaml
│       └── rbac.yaml
└── wordpress
    ├── lnmp-wordpress.yaml
    ├── service-wordpress-loadbalancer.yaml
    └── service-wordpress.yaml


# 插件清单 -- MetalLB
[root@master1 lnmp] # METALLB_VERSION='v0.14.7'
[root@master1 lnmp] # wget https://raw.githubusercontent.com/metallb/metallb/${METALLB_VERSION}/config/manifests/metallb-native.yaml

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

# 应用
[root@master1 metalLB] # kubectl apply -f service-metallb-L2Advertisement.yaml 
l2advertisement.metallb.io/localip-pool-l2a created

####################################################################################################

# 存储制备器
[root@master1 nfc-sc]#cat rbac.yaml 
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
[root@master1 nfc-sc] # kubectl apply -f rbac.yaml

[root@master1 nfc-sc] # cat nfs-client-provisioner.yaml 
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
[root@master1 nfc-sc] # kubectl apply -f nfs-client-provisioner.yaml

[root@master1 nfc-sc] # cat nfs-storageClass.yaml 
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: sc-nfs
  annotations:
    storageclass.kubernetes.io/is-default-class: "false" # 是否设置为默认的storageClass
provisioner: k8s-sigs.io/nfs-subdir-external-provisioner # or choose another name, must match deployment's env PROVISIONER_NAME
parameters:
  archiveOnDelete: "true"

# 应用
[root@master1 nfc-sc] # kubectl apply -f nfs-storageClass.yaml 

####################################################################################################

# MySQL清单资源
[root@master1 lnmp] # cat mysql/lnmp-mysql.yaml 
apiVersion: v1
kind: Secret
metadata:
  name: mysql-pass
type: kubernetes.io/basic-auth
data:
  password: MTIzNDU2

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
  labels:
    app: wordpress
spec:
  storageClassName: sc-nfs
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress-mysql
  labels:
    app: wordpress
spec:
  selector:
    matchLabels:
      app: wordpress
      tier: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
        tier: mysql
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
        name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        - name: MYSQL_DATABASE
          value: wordpress
        - name: MYSQL_USER
          value: wordpress
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
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

# 应用
[root@master1 nfc-sc] # kubectl apply -f mysql/lnmp-mysql.yaml

[root@master1 lnmp] # cat mysql/service-mysql.yaml 
apiVersion: v1
kind: Service
metadata:
  name: wordpress-mysql
  labels:
    app: wordpress
spec:
  ports:
  - port: 3306
  selector:
    app: wordpress
    tier: mysql
  clusterIP: None

# 应用
[root@master1 nfc-sc] # kubectl apply -f mysql/service-mysql.yaml 

######################################################################################################

# wordpress资源清单
[root@master1 lnmp] # cat wordpress/lnmp-wordpress.yaml 
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: wp-pv-claim
  labels:
    app: wordpress
spec:
  storageClassName: sc-nfs
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
  labels:
    app: wordpress
spec:
  replicas: 2
  selector:
    matchLabels:
      app: wordpress
      tier: frontend
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
        tier: frontend
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache
        name: wordpress
        env:
        - name: WORDPRESS_DB_HOST
          value: wordpress-mysql
        - name: WORDPRESS_DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        - name: WORDPRESS_DB_USER
          value: wordpress
        ports:
        - containerPort: 80
          name: wordpress
        volumeMounts:
        - name: wordpress-persistent-storage
          mountPath: /var/www/html
      volumes:
      - name: wordpress-persistent-storage
        persistentVolumeClaim:
          claimName: wp-pv-claim
          
# 应用
[root@master1 nfc-sc] # kubectl apply -f wordpress/lnmp-wordpress.yaml

[root@master1 lnmp] # cat wordpress/service-wordpress.yaml 
apiVersion: v1
kind: Service
metadata:
  name: wordpress
  labels:
    app: wordpress
spec:
  ports:
  - port: 80
  selector:
    app: wordpress
    tier: frontend
  clusterIP: None

# 应用
[root@master1 nfc-sc] # kubectl apply -f wordpress/service-wordpress.yaml
#########################################################################################################

# nginx资源清单
# nginx配置文件
[root@master1 lnmp] # cat nginx.conf.d/wordpress.mystical.org.conf 
server {
    listen 80;
    server_name wordpress.mystical.org;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name www.mystical.org;
    
    ssl_certificate /etc/nginx/certs/tls.crt; 
    ssl_certificate_key /etc/nginx/certs/tls.key;
    ssl_session_timeout 5m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; 
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; 
    ssl_prefer_server_ciphers on;
    include /etc/nginx/conf.d/myserver-*.cfg;

    location / {
        proxy_pass http://wordpress;                       # wordpress的svc名称
        proxy_set_header Host $host;                       # 必须写，将用户的hosts传给wordpress
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}


# 生成cm
[root@master1 lnmp] #kubectl create cm cm-nginx-conf --from-file=./wordpress.mystical.org.conf

# nginx的deployment
[root@master1 lnmp] # cat nginx/lnmp-nginx-deloyment.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: lnmp-nginx-deploy
  labels:
    app: wordpress
spec:
  replicas: 2
  selector:
    matchLabels:
      app: wordpress
      tier: nginx
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
        tier: nginx
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
        name: nginx
        env:
        - name: UPSTREAM_URL
          value: "http://wordpress"
        volumeMounts:
        - name: nginx-config-volume
          mountPath: /etc/nginx/conf.d
        - name: nginx-certs
          mountPath: /etc/nginx/certs/
      volumes:
      - name: nginx-config-volume
        configMap:
          name: cm-nginx-conf
      - name: nginx-certs
        secret:
          secretName: secret-nginx-ssl

# 应用
[root@master1 nfc-sc] # kubectl apply -f nginx/lnmp-nginx-deloyment.yaml 

# nginx对外的Service
[root@master1 lnmp] # cat nginx/service-nginx.yaml 
apiVersion: v1
kind: Service
metadata:
  name: server-nodeport-nginx
spec:
  type: LoadBalancer
  selector:
    app: wordpress
    tier: nginx
  ports:                         # 注意暴露两个端口
  - name: https
    protocol: TCP
    port: 443  
    targetPort: 443
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80

# 应用
[root@master1 nfc-sc] # kubectl apply -f nginx/service-nginx.yaml
```







## Kubernetes流量调度-Ingress



**本章内容**

- **Ingress原理**
- **Ingress-nginx安装和配置**
- **Ingress-nginx实现**
- **Ingress-nginx 实现蓝绿和灰度发布**





### Ingress原理

Ingress本质就是**七层代理**, 所以可以基于http/https的方式，将集群外部的流量统一的引入到集群内部

通过一个统一的流量入口，避免将集群内部大量的端口直接暴露给外部

Ingress 可为 Service 提供外部可访问的 URL、负载均衡流量、终止 SSL/TLS，以及基于名称的虚拟托管。 Ingress 控制器 通常负责通过负载均衡器来实现 Ingress，尽管它也可以配置边缘路由器或其他前 端来帮助处理流量。

Ingress 不会公开任意端口或协议。 将 HTTP 和 HTTPS 以外的服务公开到 Internet 时，通常使用 Service.Type=NodePort 或 Service.Type=LoadBalancer 类型的 Service。

Ingress这种利用应用层协议来进行流量的负载均衡效果，它可以实现让用户通过域名来访问相应的 service就可以了，无需关心Node IP及Port是什么，避免了信息的泄露。



**ingress 主要包含两个组件Ingress API和Ingress Controller**

ingress 其具备了动态更新并加载新配置的特性。而且ingress本身是不具备实现集群内外流量通信的功能的，这个功能是通过 controller来实现的。**Ingress Controller本身是运行于集群中的Pod资源对象**

| 组件               | 解析                                                         |
| ------------------ | ------------------------------------------------------------ |
| Ingress API        | Kubernetes上的标准API资源类型之一 仅定义了抽象路由配置信息，只是元数据，需要由相应的控制器动态加载 将代理配置抽象成一个Ingress对象，每个服务对应一个yaml配置文件 负责以k8s标准的资源格式定义流量调度、路由等规则 属于名称空间级资源,完成将同一个名空间的service资源进行暴露 |
| Ingress Controller | 七层反向代理服务程序 需要监视（watch）API Server上 Ingress资源的变动，并生成具体应用的自身的配 置文件格式，即将新加入的Ingress转化成反向代理的配置文件并动态加载使之生效，最终并据此完成流量转发 <br />Ingress Controller非为内置的控制器，需要额外自行部署 <br />通常以Pod形式运行于Kubernetes集群之上 一般应该由专用的LB Service负责为其接入集群外部流量 |



**因为ingress Controller是以pod的方式部署的,所以需要解决如下问题**

- ingress的pod如何引入外部流量
  - 通过一个专用的service 即可实现
- 如何实现ingress的Pod的流量负载均衡
  - 关于pod负载均衡的流量，直接通过deployment/daemonset等controller转发给后端pod即可。
- 后端应用的 Pod 很多，如何找到要转发的目标？
  - 通过k8s的service对所有的pod进行分组管理，再用controller内部的负载均衡配置，找到对应的目标。
  - 即后端应用的Pod对应的service 只是起到服务发现Pod的功能，而从外部访问应用的Pod的流量转发过程中不需要再经过此service 



#### Ingress 访问过程

- 从外部流量调度到kubernetes中Ingress service，有多种实现方案，比如使用节点网络中的 EXTERNAL-IP或者NodePort方式
- 从service调度到ingress-controller
- ingress-controller根据ingress Pod 中的定义，比如虚拟主机或者后端的url
- 根据虚拟主机名直接调度到后端的一组应用pod中



![image-20250104101257362](D:\git_repository\cyber_security_learning\markdown_img\image-20250104101257362.png)

注意：

- 整个流程中涉及到了两处service内容
- service ingress-nginx 是帮助 ingress controller Pod 接入外部流量的
- **后端的服务对应的service**只起到帮助 ingress controller Pod 找到具体的服务的Pod，即**只用于服务发现** ，而**流量不需要经过后端服务的Service**，直接从ingress controller Pod转到至具体的Pod
- 虚线表示service对后端的应用进行分组，实线表示ingress实际的访问流向







###  Ingress controller 常见的解决方案

对于Ingress controller的软件实现，其实没有特殊的要求，只要能够实现七层的负载均衡功能效果即可

Ingress controller 支持由任何具有反向代理功能的程序实现，如Nginx、Traefik、Envoy、HAProxy、 Vulcand等

Kubernetes支持同时部署二个或以上的数量的Ingress Controller

**Ingress资源配置指定Ingress Controller类型的方法**

- 专用的**annotation**：kubernetes.io/ingress.class，老版本用法
- Ingress资源的spec的专有字段：**ingressClassName**，引用的IngressClass是一种特定的资源类 型，此方式v1.18版本起使用，新版本推荐





### Ingress-nginx Controller 安装和配置

![image-20250104103640034](D:\git_repository\cyber_security_learning\markdown_img\image-20250104103640034.png)

#### 基于YAML部署

基于kubectl apply 部署

```bash
#获取配置文件,可能需要科学上网才能下载
https://kubernetes.github.io/ingress-nginx/deploy/

# 新版
[root@master1 ~]#wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.1/deploy/static/provider/cloud/deploy.yaml

[root@master1 ~]#wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

[root@master1 ~]#wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.0/deploy/static/provider/cloud/deploy.yaml

# 查看资源
[root@master1 ~]#cat deploy-v1.11.1.yaml |grep "^kind"
kind: Namespace
kind: ServiceAccount
kind: ServiceAccount
kind: Role
kind: Role
kind: ClusterRole
kind: ClusterRole
kind: RoleBinding
kind: RoleBinding
kind: ClusterRoleBinding
kind: ClusterRoleBinding
kind: ConfigMap
kind: Service
kind: Service
kind: Deployment
kind: Job
kind: Job
kind: IngressClass
kind: ValidatingWebhookConfiguration

# 编辑deploy-v1.11.1.yaml
# 1）默认镜像可能需要翻墙，需要修改基础镜像（共改3处，其中2处相同）
[root@master1 ~]#vim deploy.yaml
        # image: registry.k8s.io/ingress-nginx/controller:v1.11.1@sha256:e6439a12b52076965928e83b7b56aae6731231677b01e81818bce7fa5c60161a
          image: registry.cn-hangzhou.aliyuncs.com/google_containers/nginx-ingress-controller:v1.11.1
        # image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.4.1@sha256:36d05b4077fb8e3d13663702fa337f124675ba8667cbd949c03a8e8ea6fa4366  
          image: registry.cn-hangzhou.aliyuncs.com/google_containers/kube-webhook-certgen:v20230407
        # image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.4.1@sha256:36d05b4077fb8e3d13663702fa337f124675ba8667cbd949c03a8e8ea6fa4366  
          image: registry.cn-hangzhou.aliyuncs.com/google_containers/kube-webhook-certgen:v20230407
          
#2）开放外部访问入口地址
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
    app.kubernetes.io/version: 1.11.1
  name: ingress-nginx-controller
  namespace: ingress-nginx
  annotations:                       # 添加如下三行，用于支持Prometheus监控，可选
    prometheus.io/scrape: "true"
    prometheus.io/port: "10254"
spec:
  externalTrafficPolicy: Local
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - appProtocol: http
    name: http
    port: 80
    protocol: TCP
    targetPort: http
  - appProtocol: https
    name: https
    port: 443
    protocol: TCP
    targetPort: https
  selector:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
  type: LoadBalancer             # 这里使用LoadBalancer，因此需要部署MetalLB
  
#3）默认ingress-nginx-controller只有一个Pod副本的,
#方法1: 指定2个副本实现高可用（此步可选）
  name: ingress-nginx-controller
  namespace: ingress-nginx
spec:
  replicas: 2  # 添加副本数
  
# 配置MetalLB
[root@master1 metalLB]#kubectl apply -f metallb-native.yaml 
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

[root@master1 metalLB]#kubectl apply -f service-metallb-IPAddressPool.yaml 
ipaddresspool.metallb.io/localip-pool created

[root@master1 metalLB]#kubectl apply -f service-metallb-L2Advertisement.yaml 
l2advertisement.metallb.io/localip-pool-l2a created

# 应用Ingress-nginx资源配置文件
[root@master1 ~]#kubectl apply -f deploy-v1.11.1.yaml 
namespace/ingress-nginx created
serviceaccount/ingress-nginx created
serviceaccount/ingress-nginx-admission created
role.rbac.authorization.k8s.io/ingress-nginx created
role.rbac.authorization.k8s.io/ingress-nginx-admission created
clusterrole.rbac.authorization.k8s.io/ingress-nginx created
clusterrole.rbac.authorization.k8s.io/ingress-nginx-admission created
rolebinding.rbac.authorization.k8s.io/ingress-nginx created
rolebinding.rbac.authorization.k8s.io/ingress-nginx-admission created
clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx created
clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx-admission created
configmap/ingress-nginx-controller created
service/ingress-nginx-controller created
service/ingress-nginx-controller-admission created
deployment.apps/ingress-nginx-controller created
job.batch/ingress-nginx-admission-create created
job.batch/ingress-nginx-admission-patch created
ingressclass.networking.k8s.io/nginx created
validatingwebhookconfiguration.admissionregistration.k8s.io/ingress-nginx-admission created

# 查看
[root@master1 ~]# kubectl get all -n ingress-nginx 
NAME                                        READY   STATUS      RESTARTS   AGE
pod/ingress-nginx-admission-create-lx764    0/1     Completed   0          91s
pod/ingress-nginx-admission-patch-vqttt     0/1     Completed   1          91s
pod/ingress-nginx-controller-666487-9cvb7   1/1     Running     0          91s
pod/ingress-nginx-controller-666487-z24f8   1/1     Running     0          91s

NAME                                         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/ingress-nginx-controller             LoadBalancer   10.100.252.99    10.0.0.10     80:30529/TCP,443:31050/TCP   91s
service/ingress-nginx-controller-admission   ClusterIP      10.110.228.129   <none>        443/TCP                      91s

NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/ingress-nginx-controller   2/2     2            2           91s

NAME                                              DESIRED   CURRENT   READY   AGE
replicaset.apps/ingress-nginx-controller-666487   2         2         2       91s

NAME                                       STATUS     COMPLETIONS   DURATION   AGE
job.batch/ingress-nginx-admission-create   Complete   1/1           20s        91s
job.batch/ingress-nginx-admission-patch    Complete   1/1           22s        91s

```



### Ingress命令式实现

#### 命令式实现说明

```bash
# 类比nginx反向代理配置文件
http {
    upstream service_name {
        server xxxx: port
        server xxxx: port
    }
    server {
        listen 80;
        server_name domain;
        location /url {
            proxy_pass http://upstream_name;
        }
    }
}

# 创建Ingress命令
kubectl create ingress NAME --rule=domain/url=service:port[, tls[=secret]] [option]

# 常用option
--annotation=[]  # 注解信息：格式"annotation=value"
--rule=[]        # 代理规则，格式"host/path=service:port[,tls=secretname]",,注意:rule中外部域名要在所有的名称空间唯一
--class=''       # 此Ingress适配的Ingress Class Controller

# 基于URI方式代理不同应用的请求时，后端应用的URI若与代理时使用的URI不同，则需要启用URL Rewrite完成URI的重写
# Ingress-Nginx支持使用“annotation nginx.ingress.kubernetes.io/rewrite-target”注解进行
```



#### 命令式实现案例

**准备环境实现两个service应用 pod-test1和pod-test2**

```bash
# 准备后端的应用pod-test v0.1和相应的service
[root@master1 ~]# kubectl create deployment pod-test1 --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas=3
deployment.apps/pod-test1 created

[root@master1 ~]# kubectl create service clusterip pod-test1 --tcp=80:80
service/pod-test1 created

# 准备后端的应用pod-test v0.2和相应的service
[root@master1 ~]# kubectl create deployment pod-test2 --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2 --replicas=3
deployment.apps/pod-test2 created

[root@master1 ~]#kubectl create service clusterip pod-test2 --tcp=80:80
service/pod-test2 created

[root@master1 ~]#kubectl get ep
NAME         ENDPOINTS                                         AGE
kubernetes   10.0.0.201:6443                                   4h47m
pod-test1    10.244.1.159:80,10.244.2.107:80,10.244.3.173:80   3m10s
pod-test2    10.244.1.160:80,10.244.2.108:80,10.244.3.174:80   13s
```



##### 单域名单URL

**实现单域名不支持子URL**

范例：命令式实现单域名不支持子URL，子URL无法访问，返回404

```bash
#路径精确匹配,对于发往www.wang.org的请求，代理至service/pod-test1，其它的URL则无法代理
[root@master1 ~]# kubectl create ingress demo-ingress --rule="www.mystical.org/=pod-test1:80" --class=nginx -o yaml --dry-run=client
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  creationTimestamp: null
  name: demo-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test1
            port:
              number: 80
        path: /
        pathType: Exact    # #表示精确匹配，--rule="www.wang.org/*=pod-test1:80",则为prefix
status:
  loadBalancer: {}

# 创建
[root@master1 ~]#kubectl create ingress demo-ingress --rule="www.mystical.org/=pod-test1:80" --class=nginx
ingress.networking.k8s.io/demo-ingress created

# 查看生成的yaml文件
[root@master1 ~]#kubectl get ingress demo-ingress -o yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  creationTimestamp: "2025-01-04T06:37:06Z"
  generation: 1
  name: demo-ingress
  namespace: default
  resourceVersion: "30734"
  uid: a87cc2f4-3755-45fd-ab85-36a800869698
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test1
            port:
              number: 80
        path: /
        pathType: Exact
status:
  loadBalancer: {}


# 查看ingress资源
[root@master1 ~]#kubectl get ingress
NAME           CLASS   HOSTS              ADDRESS     PORTS   AGE
demo-ingress   nginx   www.mystical.org   10.0.0.10   80      2m37s


# 查看ingress-nginx-controller对应的Pod中Nginx配置文件的变化
[root@master1 ~]# kubectl exec -it -n ingress-nginx ingress-nginx-controller-666487-9cvb7  -- grep mystical.org /etc/nginx/nginx.conf
	## start server www.mystical.org
		server_name www.mystical.org ;
	## end server www.mystical.org


# 集群外访问
[root@master1 ~]#curl -H"host: www.mystical.org" http://10.0.0.10
kubernetes pod-test v0.1!! ClientIP: 10.244.1.158, ServerName: pod-test1-cd487559d-pmf2j, ServerIP: 10.244.3.173!
[root@master1 ~]#curl -H"host: www.mystical.org" http://10.0.0.10
kubernetes pod-test v0.1!! ClientIP: 10.244.1.158, ServerName: pod-test1-cd487559d-v6pl7, ServerIP: 10.244.1.159!


# 访问子URL失败，原因是只发布了www.wang.org的根目录，其它URL没有发布
[root@master1 ~]#curl -H"host: www.mystical.org" http://10.0.0.10/hostname
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>


#清理
[root@master1 ~]#kubectl delete ingress demo-ingress 
ingress.networking.k8s.io "demo-ingress" deleted
```



**实现单域名支持子URL**

```bash
#添加/*，支持子URL，如果有URL则转发至Pod对应相同的URL
[root@master1 ~]# kubectl create ingress demo-ingress --class=nginx --rule="www.mystical.org/*=pod-test1:80" -o yaml --dry-run=client
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  creationTimestamp: null
  name: demo-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test1
            port:
              number: 80
        path: /
        pathType: Prefix
status:
  loadBalancer: {}


# 创建
[root@master1 ~]#kubectl create ingress demo-ingress --rule="www.mystical.org/*=pod-test1:80" --class=nginx
ingress.networking.k8s.io/demo-ingress created

# 查看
[root@master1 ~]#kubectl get ingress
NAME           CLASS   HOSTS              ADDRESS   PORTS   AGE
demo-ingress   nginx   www.mystical.org             80      5s

# 测试访问，且支持子URL
[root@master1 ~]#curl -H"host: www.mystical.org" 10.0.0.10/hostname
ServerName: pod-test1-cd487559d-gs725

# 清理
[root@master1 ~]#kubectl delete ingress demo-ingress 
ingress.networking.k8s.io "demo-ingress" deleted
```



##### 单域名多URL

![image-20250104152617359](D:\git_repository\cyber_security_learning\markdown_img\image-20250104152617359.png)

在同一个FQDN下通过不同的URL完成不同应用间的流量分发



**单域名多URL不支持子URL**

范例: 命令式实现单域名多URL，不支持子URL，如果子URL访问，也全部转发至后端Pod的根路径 / 

```bash
#路径精确匹配,对于发往www.wang.org/v1和www.wang.org/v2的请求，分别代理至service/pod-test1和service/pod-test2的对应的子URL
[root@master1 ~]# kubectl create ingress demo-ingress1 --rule="www.mystical.org/v1=pod-test1:80" --rule="www.mystical.org/v2=pod-test2:80" --class=nginx
ingress.networking.k8s.io/demo-ingress1 created

# 集群外访问失败，原因是后端服务没有对应的/v1这样的子URL资源
[root@master1 ~]# curl -H"host: www.mystical.org" 10.0.0.10/v1/
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>
[root@mas

[root@master1 ~]# curl -H"host: www.mystical.org" 10.0.0.10/v2/
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>

# 路径精确匹配,对于发往www.wang.org/v1和/v2的请求，分别代理至service/pod-test1和service/pod-test2的根
[root@master1 ~]# kubectl create ingress demo-ingress1 --rule="www.mystical.org/v1=pod-test1:80" --rule="www.mystical.org/v2=pod-test2:80" --class=nginx --annotation nginx.ingress.kubernetes.io/rewrite-target="/"

# --annotation nginx.ingress.kubernetes.io/rewrite-target="/" 表示代理至后端服务的根/，而非默认代理至后端服务的子URL/v1和/v2

# 查看对应的yaml文件
[root@master1 ~]# kubectl get ingress demo-ingress1 -o yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
  creationTimestamp: "2025-01-04T07:49:12Z"
  generation: 1
  name: demo-ingress1
  namespace: default
  resourceVersion: "38353"
  uid: 822e0bb2-0ae3-4b17-acc2-13db0bfe5499
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test1
            port:
              number: 80
        path: /v1
        pathType: Exact
      - backend:
          service:
            name: pod-test2
            port:
              number: 80
        path: /v2
        pathType: Exact
status:
  loadBalancer:
    ingress:
    - ip: 10.0.0.10


# 测试
[root@master1 ~]#curl -H"host: www.mystical.org" 10.0.0.10/v2/
kubernetes pod-test v0.2!! ClientIP: 10.244.3.172, ServerName: pod-test2-6fb54b5db8-jkvjx, ServerIP: 10.244.1.160!
[root@master1 ~]#curl -H"host: www.mystical.org" 10.0.0.10/v1
kubernetes pod-test v0.1!! ClientIP: 10.244.1.158, ServerName: pod-test1-cd487559d-pmf2j, ServerIP: 10.244.3.173!

# 如果有URL，则访问的资源仍然是根目录，不支持对应的子URL
[root@master1 ~]#curl -H"host: www.mystical.org" 10.0.0.10/v1/hostname
kubernetes pod-test v0.1!! ClientIP: 10.244.1.158, ServerName: pod-test1-cd487559d-v6pl7, ServerIP: 10.244.1.159!

# 清理
[root@master1 ~]#kubectl delete ingress demo-ingress1 
ingress.networking.k8s.io "demo-ingress1" deleted
```



**单域名多URL支持子URL**

范例：命令式实现单域名多URL，支持子URL

```bash
# 使用URI的前缀匹配，而非精确匹配，且基于正则表达式模式进行url rewrite
[root@master1 ~]# kubectl create ingress demo-ingress2 --rule='www.mystical.org/v1(/|$)(.*)=pod-test1:80' --rule='www.mystical.org/v2(/|$)(.*)=pod-test2:80' --class=nginx --annotation nginx.ingress.kubernetes.io/rewrite-target='/$2'
Warning: path /v1(/|$)(.*) cannot be used with pathType Exact
Warning: path /v2(/|$)(.*) cannot be used with pathType Exact
ingress.networking.k8s.io/demo-ingress2 created


# 查看
[root@master1 ~]#kubectl get ingress
NAME            CLASS   HOSTS              ADDRESS     PORTS   AGE
demo-ingress2   nginx   www.mystical.org   10.0.0.10   80      75s


# 查看yaml文件
[root@master1 ~]# kubectl get ingress demo-ingress2 -o yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
  creationTimestamp: "2025-01-04T07:58:21Z"
  generation: 1
  name: demo-ingress2
  namespace: default
  resourceVersion: "39303"
  uid: de4a2bb8-e2aa-4458-ba39-3660dc46ed5f
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test1
            port:
              number: 80
        path: /v1(/|$)(.*)
        pathType: Exact
      - backend:
          service:
            name: pod-test2
            port:
              number: 80
        path: /v2(/|$)(.*)
        pathType: Exact
status:
  loadBalancer:
    ingress:
    - ip: 10.0.0.10


# 测试
[root@master1 ~]# curl -H"host: www.mystical.org" 10.0.0.10/v1/hostname
ServerName: pod-test1-cd487559d-v6pl7
[root@master1 ~]# curl -H"host: www.mystical.org" 10.0.0.10/v2/hostname
ServerName: pod-test2-6fb54b5db8-p6bwc
 
# 清理
[root@master1 ~]# kubectl delete ingress demo-ingress2 
ingress.networking.k8s.io "demo-ingress2" deleted
```



##### 多域名

![image-20250104160408264](D:\git_repository\cyber_security_learning\markdown_img\image-20250104160408264.png)



范例：命令式实现基于主机头的多虚拟主机

```bash
# 环境准备：
# 基于FQDN名称代理不同应用的请求时，需要事先准备好多个域名，且确保对这些域名的解析能够达到Igress Controller

# 对test1.wang.org的请求代理至service/pod-test1，对test2.wang.org请求代理至service/pod-test2
[root@master1 ~]# kubectl create ingress demo-ingress3 --rule="test1.mystical.org/*=pod-test1:80" --rule="test2.mystical.org/*=pod-test2:80" --class=nginx
ingress.networking.k8s.io/demo-ingress3 created


# 查看
[root@master1 ~]# kubectl get ingress
NAME            CLASS   HOSTS                                  ADDRESS   PORTS   AGE
demo-ingress3   nginx   test1.mystical.org,test2.mytical.org             80      25s

[root@master1 ~]# kubectl get ingress demo-ingress3 -o yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  creationTimestamp: "2025-01-04T08:11:21Z"
  generation: 1
  name: demo-ingress3
  namespace: default
  resourceVersion: "40668"
  uid: af274e94-7c95-4ee3-9dd3-4da09fcd0937
spec:
  ingressClassName: nginx
  rules:
  - host: test1.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test1
            port:
              number: 80
        path: /
        pathType: Prefix
  - host: test2.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test2
            port:
              number: 80
        path: /
        pathType: Prefix
status:
  loadBalancer:
    ingress:
    - ip: 10.0.0.10


# 测试
[root@master1 ~]#curl -H'host: test1.mystical.org' 10.0.0.10
kubernetes pod-test v0.1!! ClientIP: 10.244.3.172, ServerName: pod-test1-cd487559d-gs725, ServerIP: 10.244.2.107!

[root@master1 ~]#curl -H'host: test2.mystical.org' 10.0.0.10
kubernetes pod-test v0.2!! ClientIP: 10.244.1.158, ServerName: pod-test2-6fb54b5db8-jkvjx, ServerIP: 10.244.1.160!

# 清理
[root@master1 ~]#kubectl delete ingress demo-ingress3 
ingress.networking.k8s.io "demo-ingress3" deleted
```



##### HTTPS

范例：命令式实现HTTPS

```bash
# 基于TLS的Ingress要求事先准备好专用的“kubernetes.io/tls”类型的Secret资源对象
[root@master1 tls]#ls
mystical.org.crt  mystical.org.key

#创建Secret
[root@master1 tls]#kubectl create secret tls tls-mystical --cert=./mystical.org.crt --key=./mystical.org.key 
secret/tls-mystical created

# 查看
[root@master1 tls]#kubectl get secrets
NAME           TYPE                DATA   AGE
tls-mystical   kubernetes.io/tls   2      45s

#创建虚拟主机代理规则，同时将该主机定义为TLS类型，默认HTTP自动跳转至HTTPS
[root@master1 tls]#kubectl create ingress tls-demo-ingress --rule='www.mystical.org/*=pod-test1:80, tls=tls-mystical' --class=nginx
ingress.networking.k8s.io/tls-demo-ingress created

# 注意：启用tls后，该域名下的所有URI默认为强制将http请求利用308跳转至https，若不希望使用该跳转功能，可以使用如下注解选项
--annotation nginx.ingress.kubernetes.io/ssl-redirect=false，即如下形式
[root@master1 ~]# kubectl create ingress tls-demo-ingress -- rule='www.wang.org/*=pod-test1:80,tls=tls-wang' --class=nginx --annotation nginx.ingress.kubernetes.io/ssl-redirect=false

# 查看
[root@master1 tls]#kubectl get ingress tls-demo-ingress -o yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  creationTimestamp: "2025-01-04T08:47:00Z"
  generation: 1
  name: tls-demo-ingress
  namespace: default
  resourceVersion: "44442"
  uid: 42e90245-143b-4f74-a128-8216da28b839
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test1
            port:
              number: 80
        path: /
        pathType: Prefix
  tls:
  - hosts:
    - www.mystical.org
    secretName: tls-mystical
status:
  loadBalancer:
    ingress:
    - ip: 10.0.0.10


#集群外客户端测试访问
https://www.mystical.org/
```



![image-20250104165007749](D:\git_repository\cyber_security_learning\markdown_img\image-20250104165007749.png)





##### 证书更新

HTTPS 的证书的有效期一般为1年,到期前需要提前更新证书

```bash
#重新颁发证书
[root@master1 ~]# (umask 077; openssl genrsa -out wang.key 2048)
[root@master1 ~]# openssl req -new -x509 -key wang.key -out wang.crt -subj /C=CN/ST=Beijing/L=Beijing/O=SRE/CN=www.wang.org -days 3650

# 方法1：
#在线修改证书配置,需要提前先将新证书文件用base64编码并删除换行符
[root@master1 ~]# cat wang.crt |base64 | tr -d '\n' 
[root@master1 ~]# cat wang.key |base64 | tr -d '\n'

#上面生成的内容替换下面命令的内容,立即生效
[root@master1 ~]# kubectl edit secrets tls-wang 

# 方法2：
#方法2
#删除旧证书配置
[root@master1 ~]#kubectl delete secrets tls-wang 

#创建新证书配置
[root@master1 ~]# kubectl create secret tls tls-wang --cert=./wang.crt --key=./wang.key
```



### Ingress声明式实现

#### 声明式实现说明

基于命令方式格式功能有限，且不利于后续的重复使用，**工作中更多的使用声明式实现Ingress**

在实际的工作中，可能会基于域名访问,也可能会基于不同的功能服务以子路径的方式来进行访问，以及 与https相关的访问。



**配置文件解析**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: <string>
  annotations:                                 # 资源注解，v1beta1使用下面的注解来指定要解析该资源的控制器类型
    kubernetes.io/ingress.class: <string>      # 适配的Ingress控制器类别，便于多ingress组件场景下，挑选针对的类型
  namespace: <string>
spec:
  rules: <[]object>                            # Ingress规则列表，也就是http转发时候用到的 url关键字
  - host: <string>                             # 虚拟主机的FQDN，支持"*"前缀通配，不支持IP，不支持指定端口
    http: <object>
      paths: <[]object>                        # 虚拟主机PATH定义的列表，由path和backend组成
      - path: <string>                         # 流量匹配的HTTP PATH，必须以/开头
        pathType: <string>                     # 支持Exact、Prefix和ImplementationSpecific, 必须
        backend: <object>                      # 匹配到的流量转发到的目标后端
          resource: <object>                   # 引用的同一名称空间下的资源，与下面两个字段互斥
          service: <object>                    # 关联的后端Service对象
            name: <string>                     # 后端Service的名称
            port: <string>                     # 后端Service上的端口对象
              name: <string>                   # 端口名称
              number: <integer>                # 端口号
  tls: <[]Object>                              # TLS配置，用于指定上rules中定义的哪些host需要工作https模式
  - hosts: <[]string>                          # 使用同一组证书的主机名称列表
    secretName: <string>                       # 保存于数字证书和私钥信息的Secret资源名称，用于主机认证
  backend: <Object>                            # 默认backend的定义，可嵌套字段及使用格式跟rules字段中的相同
  ingressClassName: <string>                   # ingress类名称，用于指定适配的控制器，类似于注解的功能，未来代替                                                        annotations
```



#### 声明式实现案例

##### 单域名案例

![image-20250104171513550](D:\git_repository\cyber_security_learning\markdown_img\image-20250104171513550.png)

范例 : 单域名支持子URL

```yaml
# 准备后端服务所需资源
[root@master1 ingress] # cat ingress-deployment-svc.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-test
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
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
          name: http
---
apiVersion: v1
kind: Service
metadata:
  name: deployment-service
spec:
  selector:
    app: pod-test
  ports:
  - name: http
    port: 80
    targetPort: 80
    
# 应用
[root@master1 yaml] # kubectl apply -f ingress-deployment-svc.yaml 
deployment.apps/deployment-test created

# 自定义创建ingress资源文件
[root@master1 ingress] # vim ingress-http-test.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-test
  #annotations:
  #  kubernetes.io/ingress.class: "nginx"
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: deployment-service
            port:
              number: 80

# 查看ingress
[root@master1 ingress] # kubectl get ingress
NAME           CLASS   HOSTS              ADDRESS     PORTS   AGE
ingress-test   nginx   www.mystical.org   10.0.0.10   80      2m12s

# 测试
# 这里的客户端显示的是ingress的Pod的IP，而不是真实的客户端IP
[root@master1 ingress] # curl -H"host: www.mystical.org" 10.0.0.10
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: deployment-test-5cc5b8d4cd-bzbnm, ServerIP: 10.244.2.112!
[root@master1 ingress] # curl -H"host: www.mystical.org" 10.0.0.10
kubernetes pod-test v0.1!! ClientIP: 10.244.1.164, ServerName: deployment-test-5cc5b8d4cd-qv78g, ServerIP: 10.244.3.177!

# 清理删除
[root@master1 ingress]#kubectl delete -f ingress-http-test.yaml 
ingress.networking.k8s.io "ingress-test" deleted
```



##### 获取真实客户端IP

```yaml
# 环境准备，直接使用上述环境即可
[root@master1 ingress] # kubectl create deployment myapp --image registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
deployment.apps/myapp created

[root@master1 ingress] # kubectl create svc clusterip myapp --tcp 80
service/myapp created

# Ingress配置
[root@master1 ingress] # cat ingress-http-real-ip.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-myapp
  annotations:
    nginx.ingress.kubernetes.io/enable-real-ip: "true" # 允许IP透传，此为默认值
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: myapp
            port:
              number: 80
        path: /
        pathType: Prefix
        
# 查看ingress-nginx的pod里的配置
[root@master1 ingress] # kubectl exec -n ingress-nginx ingress-nginx-controller-666487-9cvb7 -- nginx -T|grep 'proxy_set_header X-Forwarded-For'
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
			proxy_set_header X-Forwarded-For        $remote_addr;
			proxy_set_header X-Forwarded-For        $remote_addr;
			
# 从集群外访问 
[root@ubuntu2204 ~] # curl www.mystical.org
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...

# 查看日志信息
[root@master1 ingress] # kubectl logs myapp-56cc856b4-k9hjv 
10.244.3.178 - - [06/Jan/2025:06:28:39 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0" "10.0.0.132"
10.244.3.178 - - [06/Jan/2025:06:28:42 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0" "10.0.0.132"
```



##### 单域名多URL案例

范例：环境准备两个HTTP应用

```yaml
# 如果前面的资源已删除，重新应用上面小节的资源文件生成deployment和对应的SVC
#访问 www.wang.org/flask的时候，返回flask的结果
#访问 www.wang.org/nginx的时候，返回nginx的结果

[root@master1 ingress] # cat ingress-deployment-svc.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-test
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
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
          name: http
---
apiVersion: v1
kind: Service
metadata:
  name: deployment-service
spec:
  selector:
    app: pod-test
  ports:
  - name: http
    port: 80
    targetPort: 80


# 应用
[root@master1 ingress] # kubectl apply -f ingress-deployment-svc.yaml 
deployment.apps/deployment-test created
service/deployment-service created

# 在添加一个nginx的服务，定义资源文件
[root@master1 ingress] # cat ingress-deployment-nginx.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-test
  template:
    metadata:
      labels:
        app: nginx-test
    spec:
      containers:
      - name: nginx-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
          name: nginx

---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx-test
  ports:
  - name: nginx
    port: 80
    targetPort: 80
    
# 应用
[root@master1 ingress] # kubectl apply -f ingress-deployment-nginx.yaml 
deployment.apps/deployment-nginx created
service/nginx-service created

# 查看
[root@master1 ingress] # kubectl get deployments,svc
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/deployment-nginx   3/3     3            3           113s
deployment.apps/deployment-test    3/3     3            3           10m
deployment.apps/myapp              1/1     1            1           21m

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/deployment-service   ClusterIP   10.105.47.74     <none>        80/TCP    10m
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP   2d5h
service/myapp                ClusterIP   10.102.162.246   <none>        80/TCP    21m
service/nginx-service        ClusterIP   10.102.157.212   <none>        80/TCP    113s
```



**单域名多URL不支持子URL**

```yaml
# 清单文件
[root@master1 ingress] # cat ingress-http-mul-url.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-mul-url
  annotations:
#    kubenetes.io/ingress.class: "nginx"   # 新版k8s好像不支持注解的用法
    nginx.ingress.kubernetes.io/rewrite-target: / # 默认会转发给后端时会带URL，添加此行，表示转发时删除后面的URL
spec:
  ingressClassName: nginx  # 新版建议使用此项指定controller类型
  rules:
  - host: www.mystical.org
    http:
      paths:
      - path: /flask
        pathType: Prefix # 表示以/flask为开始即可
        backend:
          service:
            name: deployment-service  # 指定对应Service的名称
            port:
              name: http
      - path: /nginx
        pathType: Prefix
        backend:
          service:
            name: nginx-service
            port:
              name: nginx

# 应用
[root@master1 ingress] # kubectl apply -f ingress-http-mul-url.yaml 
ingress.networking.k8s.io/ingress-mul-url created

# 查看
[root@master1 ingress] # kubectl get ingress
NAME              CLASS   HOSTS              ADDRESS     PORTS   AGE
ingress-mul-url   nginx   www.mystical.org   10.0.0.10   80      5s

# 测试
[root@ubuntu2204 ~] # curl www.mystical.org/flask
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: deployment-test-5cc5b8d4cd-nrv8t, ServerIP: 10.244.1.166!

[root@ubuntu2204 ~] # curl www.mystical.org/nginx
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
......

#注意事项：
#默认转给后端服务时会将url也同时转发，而后端服务有可能不存在此URL，所以需要在后端url转发的时候，取消转发关键字。
#方法就是，在annotation中添加一个重写的规则nginx.ingress.kubernetes.io/rewrite-target: / 即所有的请求把ingress匹配到的url关键字清除掉

```



**单域名多URL支持子URL**

```yaml
# 准备后端的应用pod-test v0.1和相应的service
[root@master1 ~]# kubectl create deployment pod-test1 --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas=3
deployment.apps/pod-test1 created

[root@master1 ~]# kubectl create service clusterip pod-test1 --tcp=80:80
service/pod-test1 created

# 准备后端的应用pod-test v0.2和相应的service
[root@master1 ~]# kubectl create deployment pod-test2 --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2 --replicas=3
deployment.apps/pod-test2 created

[root@master1 ~]#kubectl create service clusterip pod-test2 --tcp=80:80
service/pod-test2 created

[root@master1 ~]#kubectl get ep
NAME         ENDPOINTS                                         AGE
kubernetes   10.0.0.201:6443                                   4h47m
pod-test1    10.244.1.159:80,10.244.2.107:80,10.244.3.173:80   3m10s
pod-test2    10.244.1.160:80,10.244.2.108:80,10.244.3.174:80   13s


# 资源文件
[root@master1 ingress] # cat ingress-http-mul-suburl.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2  # 正则表达式
  name: ingress-http-mul-suburl
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test1
            port:
              number: 80
        path: /v1(/|$)(.*)
        pathType: Exact
      - backend:
          service:
            name: pod-test2
            port:
              number: 80
        path: /v2(/|$)(.*)
        pathType: Exact

# 应用
[root@master1 ingress] # kubectl apply -f ingress-http-mul-suburl.yaml 
Warning: path /v1(/|$)(.*) cannot be used with pathType Exact
Warning: path /v2(/|$)(.*) cannot be used with pathType Exact
ingress.networking.k8s.io/ingress-http-mul-suburl created

# 查看
[root@master1 ingress] # kubectl get ingress
NAME                      CLASS   HOSTS              ADDRESS     PORTS   AGE
ingress-http-mul-suburl   nginx   www.mystical.org   10.0.0.10   80      9s

# 测试
[root@ubuntu2204 ~]#curl www.mystical.org/v1/hostname
ServerName: pod-test1-cd487559d-wfvhs
[root@ubuntu2204 ~]#curl www.mystical.org/v2/hostname
ServerName: pod-test2-6fb54b5db8-mmrjm
```



##### 多域名案例

```yaml
# 访问flask.mystical.org/的时候，返回flask的结果
# 访问flask.mystical.org/的时候，返回nginx的结果
[root@master1 ingress] # kubectl apply -f ingress-deployment-nginx.yaml 
deployment.apps/deployment-nginx created
service/nginx-service created

[root@master1 ingress] # kubectl apply -f ingress-deployment-svc.yaml
deployment.apps/deployment-test created
service/deployment-service created

# 编辑Ingress资源定义文件
[root@master1 ingress]#cat ingress-http-mul-host.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-mul-url
  annotations:
    nginx.ingress.kubernetes.io/use-regex: "true"           # 指定后面rules定义的path使用的正则表达式
    nginx.ingress.kubernetes.io/proxy-body-size: "100m"     # 客户端上传文件最大值，默认1m
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "60" # 后端服务器的连接超时的时间，默认值为5s
    nginx.ingress.kubernetes.io/proxy-send-timeout: "120"   # 后端服务器数据回传超时时间，即规定时间之内后端服务器必须传完所有的数据，默认值为60s
    nginx.ingress.kubernetes.io/proxy-read-timeout: "120"   # 后端服务器响应的超时时间，默认60s
    #nginx.ingress.kubernetes.io/app-root: /index.html      #指定默认页面文件
spec:
  ingressClassName: nginx                                   # 新版建议使用此项指定controllerl类型
  rules:
  - host: flask.mystical.org
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: deployment-service
            port:
              name: http                                  # 匹配service中的端口 name: http
  - host: nginx.mystical.org
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx-service
            port:
              name: nginx

# 应用
[root@master1 ingress] # kubectl apply -f ingress-http-mul-host.yaml 
ingress.networking.k8s.io/ingress-mul-url created

# 查看
[root@master1 ingress]#kubectl get ingress
NAME              CLASS   HOSTS                                   ADDRESS     PORTS   AGE
ingress-mul-url   nginx   flask.mystical.org,nginx.mystical.org   10.0.0.10   80      65s

# 测试
[root@ubuntu2204 ~] # curl flask.mystical.org
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: deployment-test-5cc5b8d4cd-69cgm, ServerIP: 10.244.3.184!

[root@ubuntu2204 ~] # curl nginx.mystical.org
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>

#清理环境
[root@master1 ingress] # kubectl delete -f ingress-http-mul-host.yaml 
ingress.networking.k8s.io "ingress-mul-url" deleted

[root@master1 ingress] # kubectl delete -f ingress-deployment-svc.yaml 
deployment.apps "deployment-test" deleted
service "deployment-service" deleted

[root@master1 ingress] # kubectl delete -f ingress-deployment-nginx.yaml 
deployment.apps "deployment-nginx" deleted
service "nginx-service" deleted
```



#####  HTTPS 案例

```yaml
# 准备好证书相关的secret
[root@master1 ingress] # kubectl get secret
NAME           TYPE                DATA   AGE
tls-mystical   kubernetes.io/tls   2      47h

# 准备好后面的deployment和service
[root@master1 ingress] # kubectl apply -f ingress-deployment-svc.yaml 
deployment.apps/deployment-test created
service/deployment-service created

# 定义资源配置文件，实现HTTP自动跳转至HTTPS
[root@master1 ingress]#cat ingress-http-tls-test.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-test
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: deployment-service
            port:
              number: 80
# - host: m.mystical.org
# ...

# https证书配置
  tls:
  - hosts:
    - www.mystical.org
    secretName: tls-mystical
 #- hosts:                                             # 多个域名分别对应不同的证书
 #  - m.mystical.org
 #  secretName: ingress-tls-m


# 应用
[root@master1 ingress] # kubectl apply -f ingress-http-tls-test.yaml 
ingress.networking.k8s.io/ingress-test created

# 查看
[root@master1 ingress] # kubectl get ingress
NAME           CLASS   HOSTS              ADDRESS     PORTS     AGE
ingress-test   nginx   www.mystical.org   10.0.0.10   80, 443   2m11s


# 测试
[root@ubuntu2204 ~] # curl www.mystical.org -Lk
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: deployment-test-5cc5b8d4cd-ww8fc, ServerIP: 10.244.3.185!
[root@ubuntu2204 ~] # curl www.mystical.org -Lk
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: deployment-test-5cc5b8d4cd-lkf2v, ServerIP: 10.244.2.119!
```





### Ingress Nginx 实现蓝绿BlueGreen 和灰度Canary 发布



####  Ingress Nginx 进行BlueGreen 和 Canary 灰度发布说明



Service 虽然支持流量分配,但是**只支持基于Pod的数量或比例实现**,而**不支持基于Header,cookie,权重等** 更为清确的流量发配策略

**Ingress-Nginx支持配置Ingress Annotations来实现不同场景下的灰度发布和测试**，它能够满足金丝雀 发布、蓝绿部署与A/B测试等不同的业务场景

**注意**：Ingress-Nginx 只能支持南北向的流量发布，而东西向流量的发布可以利用工作负载型如 deployment的更新策略或者服务网格技术实现



**Ingress Nginx的流量发布机制**



![image-20250106163000499](D:\git_repository\cyber_security_learning\markdown_img\image-20250106163000499.png)



- **蓝绿**：
  - production: 100%, canary: 0%
  - production: 0%, canary: 100% --> Canary变成后面的Production
- **金丝雀Canary**：
  - **流量比例化切分**: 逐渐调整
  - **流量识别，将特定的流量分发给Canary**：
    - By-Header：基于特定的标头识别
      -  Header 值默认：只有Always 或 Nerver 两种值 
      - Header 值自定义 
      - Header 值可以基于正则表达式Pattern进行匹配
    - By-Cookie: 基于Cookie识别



**基于Ingress Nginx的Canary规则**

Ingress Nginx 的 Annotations支持的Canary规则， Annotations 和 Label 相似也是保存资源对象上的 元数据，但不能被标签选择器选择，且没有Label的名称最长63个字符的限制



- **nginx.ingress.kubernetes.io/canary-weight**：
  - 基于服务权重进行流量切分，适用于蓝绿或灰度发布，权重范围0 - 100按百分比将请求路由到 Canary Ingress中指定的服务
  - 权重为 0 意味着该金丝雀规则不会向Canary入口的服务发送任何请求
  - 权重为100意味着所有请求都将被发送到 Canary 入口

- **nginx.ingress.kubernetes.io/canary-by-cookie**：
  - 基于 cookie 的流量切分，适用于灰度发布与 A/B 测试
  - cookie 的值设置为 always 时，它将被路由到Canary入口
  - cookie 的值设置为 never 时，请求不会被发送到Canary入口
  - 对于任何其他值，将忽略 cookie 并将请求与其他金丝雀规则进行优先级的比较，默认转发给旧版 本











**规则的应用次序**

- Canary规则会按特定的次序进行评估
- 优先级从低到高顺序：**canary -weight- -> canary-by-cookie --> canary-by-header** 





#### 实战案例

##### 范例：初始环境准备新旧两个版本应用

```yaml
# 准备新旧版本对应的各自独立的两套deployment和service
[root@master1 project-caray] # cat deploy-pod-test-v1.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: pod-test
  name: pod-test-v1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pod-test
      version: v0.1
  strategy: {}
  template:
    metadata:
      labels:
        app: pod-test
        version: v0.1
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
        name: pod-test

---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: pod-test
  name: pod-test-v1
spec:
  ports:
  - name: http-80
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: pod-test
    version: v0.1
  type: ClusterIP

[root@master1 project-caray] # cat deploy-pod-test-v2.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: pod-test
  name: pod-test-v2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pod-test
      version: v0.2
  strategy: {}
  template:
    metadata:
      labels:
        app: pod-test
        version: v0.2
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2
        name: pod-test

---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: pod-test
  name: pod-test-v2
spec:
  ports:
  - name: http-80
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: pod-test
    version: v0.2
  type: ClusterIP


# 部署新旧两个版本
[root@master1 project-caray] # kubectl apply -f deploy-pod-test-v1.yaml 
deployment.apps/pod-test-v1 created
service/pod-test-v1 created

[root@master1 project-caray] # kubectl apply -f deploy-pod-test-v2.yaml 
deployment.apps/pod-test-v2 created
service/pod-test-v2 created

# 测试
[root@master1 project-caray] # kubectl get svc
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes    ClusterIP   10.96.0.1       <none>        443/TCP   2d7h
pod-test-v1   ClusterIP   10.99.14.10     <none>        80/TCP    84s
pod-test-v2   ClusterIP   10.96.114.114   <none>        80/TCP    81s

[root@master1 project-caray] # curl 10.99.14.10
kubernetes pod-test v0.1!! ClientIP: 10.244.0.0, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!

[root@master1 project-caray] # curl 10.96.114.114
kubernetes pod-test v0.2!! ClientIP: 10.244.0.0, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
```



##### 范例：蓝绿发布

```yaml
# 创建Ingress，使其对应旧版本应用
[root@master1 project-caray] # cat ingress-blue-green.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-blue-green
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test-v1
            port:
              number: 80 
        path: /
        pathType: Prefix

# 查看
[root@master1 project-caray] # kubectl get ingress
NAME                 CLASS   HOSTS              ADDRESS     PORTS   AGE
ingress-blue-green   nginx   www.mystical.org   10.0.0.10   80      54s

# 测试
[root@ubuntu2204 ~] # curl www.mystical.org
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!

# 修改Ingress切换成v0.2版本
[root@master1 project-caray]#cat ingress-blue-green.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-blue-green
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test-v2              # 修改Service版本
            port:
              number: 80 
        path: /
        pathType: Prefix

# 应用
[root@master1 project-caray] # kubectl apply -f ingress-blue-green.yaml 
ingress.networking.k8s.io/ingress-blue-green configured

# 测试
[root@ubuntu2204 ~] # curl www.mystical.org
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
```





##### 范例：基于权重的金丝雀发布

```yaml
# 清单文件
[root@master1 project-caray] # cat canary-by-weight.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "10"  # 指定使用金丝雀新版占用百分比
  name: pod-test-canary-by-weight
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test-v2
            port:
              number: 80
        path: /
        pathType: Prefix

# 应用
[root@master1 project-caray] # kubectl apply -f canary-by-weight.yaml 
ingress.networking.k8s.io/pod-test-canary-by-weight created

# 集群外客户端访问，观察新旧版本的比例
[root@ubuntu2204 ~]#while true; do curl www.mystical.org; sleep 1; done
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!

# 调整weight权重为90
[root@master1 project-caray]# cat canary-by-weight.yaml 
......
    nginx.ingress.kubernetes.io/canary-weight: "90"
    ......
    
# 观察比例变化
[root@ubuntu2204 ~] # while true; do curl www.mystical.org; sleep 1; done
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!

# 清理
[root@master1 project-caray] # kubectl delete -f canary-by-weight.yaml 
ingress.networking.k8s.io "pod-test-canary-by-weight" deleted
```



##### 范例：基于Cookie实现金丝雀发布

```yaml
# 清单文件
[root@master1 project-caray] # cat canary-by-cookie.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-cookie: "vip_user"  # cookie中vip_user=always时才用金丝雀发布下面新版本
  name: pod-test-canary-by-cookie
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test-v2
            port:
              number: 80
        path: /
        pathType: Prefix

# 应用
[root@master1 project-caray] # kubectl apply -f canary-by-cookie.yaml 
ingress.networking.k8s.io/pod-test-canary-by-cookie created

# 外部正常访问
[root@ubuntu2204 ~] # while true; do curl www.mystical.org; sleep 1; done
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!

# 将Cookie上面添加：vip_user=always，测试成功
[root@ubuntu2204 ~]#while true; do curl -b "vip_user=always" www.mystical.org; sleep 1; done
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!

# 清理

```



##### 范例：基于请求Header固定值的金丝雀发布

```yaml
# 清单文件
[root@master1 project-caray ]# cat canary-by-header.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-header: "X-Canary" # X-Canary首部字段值为always时才使用金丝雀发布下面新版本,否则为旧版本
  name: pod-test-canary-by-header
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test-v2
            port:
              number: 80
        path: /
        pathType: Prefix
        
# 应用
[root@master1 project-caray] # kubectl apply -f canary-by-header.yaml 
ingress.networking.k8s.io/pod-test-canary-by-header created

# 测试
[root@ubuntu2204 ~]#while true; do curl www.mystical.org; sleep 1; done
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!
kubernetes pod-test v0.1!! ClientIP: 10.244.3.178, ServerName: pod-test-v1-5b856c4b5b-g9ltz, ServerIP: 10.244.1.173!

# 添加header，实现版本切换
[root@ubuntu2204 ~]#while true; do curl -H "X-Canary: always" www.mystical.org; sleep 1; done
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!

# 清理

```



##### 范例: 基于请求 Header 精确匹配指定值的金丝雀发布

```yaml
# 清单
[root@master1 project-caray] # cat canary-by-header-value.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-header: "IsVIP"
    nginx.ingress.kubernetes.io/canary-by-header-value: "true" #IsVIP首部字段的值为true就使用金丝雀发布下面新版本,否则为旧版本
  name: pod-test-canary-by-header-value
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test-v2
            port: 
              number: 80
        path: /
        pathType: Prefix


# 应用
[root@master1 project-caray] # kubectl apply -f canary-by-header-value.yaml 
ingress.networking.k8s.io/pod-test-canary-by-header-value created

# 测试
[root@ubuntu2204 ~] # while true; do curl -H "IsVIP: true" www.mystical.org; sleep 1; done
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!

# 清理
[root@master1 project-caray] # kubectl delete -f canary-by-header-value.yaml 
ingress.networking.k8s.io "pod-test-canary-by-header-value" deleted
```



##### 范例：基于请求 Header 正则表达式模式匹配的指定值的金丝雀发布

```yaml
# 清单文件
[root@master1 project-caray] # cat canary-by-header-pattern.yaml 
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-header: "username"
    nginx.ingress.kubernetes.io/canary-by-header-pattern: "(vip|VIP)_.*" #首部字段的值为username且正则表达式匹配时使用新版，否则使用旧版
  name: pod-test-canary-by-header-pattern
spec:
  ingressClassName: nginx
  rules:
  - host: www.mystical.org
    http:
      paths:
      - backend:
          service:
            name: pod-test-v2
            port: 
              number: 80
        path: /
        pathType: Prefix

# 应用
[root@master1 project-caray] # kubectl apply -f canary-by-header-pattern.yaml 
ingress.networking.k8s.io/pod-test-canary-by-header-pattern created

# 集群外客户端访问
[root@ubuntu2204 ~]#while true; do curl -H "username: vip_user" www.mystical.org; sleep 1; done
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!

# 换个username的值，可以匹配正则，因此仍是新版
[root@ubuntu2204 ~]#while true; do curl -H "username: VIP_man" www.mystical.org; sleep 1; done
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!
kubernetes pod-test v0.2!! ClientIP: 10.244.3.178, ServerName: pod-test-v2-54df7d7958-c427f, ServerIP: 10.244.3.186!

# 清理
[root@master1 project-caray] # kubectl delete -f canary-by-header-pattern.yaml 
ingress.networking.k8s.io "pod-test-canary-by-header-pattern" deleted
```





## Kubernetes安全机制



**本章内容**

- **安全体系**
- **认证机制**
- **授权机制**
- **准入机制**





### 安全体系



**用户访问Kubernetes业务应用的流程**

- 无需api_server认证
  - 用户 --> Service(ingress-nginx) --> ingress(controller) --> service --> pod
- 基于api_server认证
  - 管理Kubernetes平台上各种应用现象

对于Kubernetes平台来说，几乎所有的操作基本上都是通过kube apiserver这个组件进行的，该组件提供HTTP RESTful形式的API集群内外客户端调用

对于Kubernetes集群的部署样式主要由两种：http形式和https形式

采用Kubernetes部署的形式默认对外是基于https的方式，而内部组件的通信是基于http方式

而Kubernetes的认证授权机制仅仅存在于https形式的api访问中，也就是说，如果客户端使用HTTP连接到kube-apiserver,那么是不会进行认证授权的，这样即增加了安全性，也不至于太复杂

Kubelet和kubeapi类似，提供一个简单的REST API服务，也监听一些TCP的套接字

- 10250：具有所有节点上Pod管理权限的读写端口，应谨慎管理，Kubelet管理的端口
- 10255：仅提供只读操作，是REST API的子集，新版不再使用
- 10248：是本地healthz端点使用的端口，Kubelet管理的端口

```bash
[root@master1 project-caray]# ss -ntlp|grep kubelet
LISTEN 0      4096       127.0.0.1:10248      0.0.0.0:*    users:(("kubelet",pid=1256,fd=17))       
LISTEN 0      4096               *:10250            *:*    users:(("kubelet",pid=1256,fd=14))  
```



#### 安全基本流程

![image-20250106182043977](D:\git_repository\cyber_security_learning\markdown_img\image-20250106182043977.png)



- 认证 Authentication
- 授权 Authorization
- 准入控制 Admission contro



此安全机制在一定程度上提高安全性，不过更多是资源管理方面的作用。

认证,授权和准入控制功能都是以**插件化的方式**来实现的，这样可以最大化的用户自定义灵活性。



| 步骤                 | 解析                                                         |
| -------------------- | ------------------------------------------------------------ |
| 认证(Authn)          | 对用户进行身份认证，只允许被许可的用户才能进入集群内部，认证失败返回 401。<br />遵循“或”逻辑,且任何一个插件核验成功后都将不再进行后续的插件验证<br />前面的插件检查失败,则检查下一个插件,如里都不成功,才失败,或以匿名身份访 问 |
| 授权(Authz)          | 不同用户获取不同的资源操作权限，比如普通用户、超级用户等。权限不足返 回403<br />鉴权过程遵循“或”逻辑，且任何一个插件对操作的许可授权后都将不再进行后 续的插件验证<br />如果都未许可,则拒绝请求 |
| 准入控制 (Admission) | 用户认证、授权之后，当进行一些写操作的时候，需要遵循的一些限制的要 求,比如资源限制<br />内容合规性检查，遵循“与”逻辑，且无论成败，每次操作都要经由所有插件检 验,最后统一返回结果<br />只对写操作进行合规性检查，在授权范围内，对用户的某些命令或者操作进行 进一步的限制<br />分为两类: validaing 校验(合规性,资源默认和最大和最小限制)和 mutating 变 更(补全,默认值填充) |



![image-20250106182813464](D:\git_repository\cyber_security_learning\markdown_img\image-20250106182813464.png)



### 认证机制

主要涉及到**用户帐号UA**和**服务帐号SA**的认证内容



#### 认证机制说明

所有 Kubernetes 集群都有**两类用户**：由 Kubernetes 管理的**服务账号**和**普通用户**。

在 Kubernetes 中，**subject** 是指一个对象或实体，该对象或实体可以**是用户、服务帐户、组或其他可识别的实体**。它在授权策略中用于标识哪些实体被允许或被拒绝访问资源。简而言之，**subject 就是需要被授权访问资源的实体**。认证用户即属于Subject



在Kubernetes集群中定义了**两种类型的subject资源的认证用户**：

| 用户种类        | 解析                                                         |
| --------------- | ------------------------------------------------------------ |
| User Account    | 用户账户，指非Pod类的客户端访问API Server时使用的身份标识，一般是现实中的 “人”<br />API Server没有为这类账户提供保存其信息的资源类型，**相关的信息通常保存于外部的文件或认证系统中**,由外部独立服务进行管理，所以用户不能通过集群内部的 API 来 进行管理。<br />身份核验操作可由API Server进行，也可能是由外部身份认证服务完成 作用域为整个集群级别,常见的管理方式，如： openssl等 |
| Service Account | ervice Accounts（SA）在 Kubernetes 中是一种内建的、与 Pod 关联的账号类型。 它们主要是为了在Pod中运行的进程提供一个身份标识，以便访问 Kubernetes API 通过Kubernetes API 来管理的用户帐号，适用于集群中Pod内的进程访问API Server 时使用的身份信息，需要通过 API 来完成权限认证<br />API Server使用ServiceAccount类型的资源对象来保存该类账号<br />认证到API Server的认证信息称为**Service Account Token**，它们**保存于同名的专用类型的Secret对象中**<br />在集群内部进行权限操作，都需要使用到 ServiceAccount<br />**namespace 别级的资源类型,即帐号隶属于名称空间,但可以授予集群级别的权限** |
| 匿名用 户       | 不能被识别为Service Account，也不能被识别为User Account的用户，即“匿名用户" |

尽管无法通过 API 调用来添加普通用户， Kubernetes 仍然认为**能够提供**由集群的证书机构签名的**合法证书**的**用户**是**通过身份认证的用户**。 基于这样的配置**，Kubernetes 使用证书中的 'subject' 的通用名称** （Common Name）**字段** （例如，"/CN=bob"）**来确定用户名**。 接下来，**基于角色访问控制**（RBAC） 子系统会**确定用户是否有权针对某资源执行特定的操作**。



##### 用户组

在kubernetes集群中，为了更方便的对某一类用户帐号UA进行方便管理，一般会通过用户组的方式来进行管理

注意: Kubernetes 不支持将一个SA服务帐户加入一个指定的组中,但是可以通过RBAC机制创建一个授权 的角色,再将服务帐户和角色绑定实现。

Kubernetes常见的内置用户组有以下四类：

| 用户组                              | 解析                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| system:unauthenticated              | 未能通过任何一个授权插件检验的账号的所有未通过认证测试的用户 统一隶属的用户组 |
| system:authenticated                | 认证成功后的用户自动加入的一个专用组，用于快捷引用所有正常通 过认证的用户账号 |
| system:serviceaccounts              | 所有名称空间中的所有ServiceAccount对象                       |
| system:serviceaccounts: <namespace> | 特定名称空间内所有的ServiceAccount对象                       |

Kubernetes本身并没有对用户或用户组的内建概念或实体。

在**Kubernetes中**，**用户和组是在身份提供者**（如OpenID Connect，Active Directory等）**中创建和管理 的**，**而不是在Kubernetes集群自身中创建**。所以，无法直接在Kubernetes中创建组。

在Kubernetes中，用户和用户组主要在**认证 (Authentication)** 和**授权 (Authorization)** 环节中发挥作用。

**这就意味着在Kubernetes中没有直接的方式去查看用户或用户组**

如果想要查看当前Kubernetes集群中的用户和用户组，通常需要查看的是**外部身份提供商的设置**或**Kubeconfig文件**。同时，您可以查看在Kubernetes中定义的RBAC策略，以理解哪些用户和用户组有 权访问特定资源。

在Kubernetes中，**服务帐户(ServiceAccount)**默认会被放入两个组之一： **system:serviceaccounts （**表示集群中的所有服务帐户）和 **system:serviceaccounts: `<namespace>`**（表示给定命名空间中的所有服务帐户）。这些是内置的组。



**范例：查看用户组`system:master`的权限**

```bash
#所有的k8s集群资源操作，其实都是通过node节点上的kubelet和master节点上的apiserver之间的通信实现，而在kubernetes的认证目录中有其专用的通信认证证书 apiserver-kubelet-client.crt，可以通过该文件来检查一下这两者之间是一个怎样的关系。

# 新版
[root@master1 pki]#openssl x509 -in /etc/kubernetes/pki/apiserver-kubelet-client.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 8841619138675744303 (0x7ab3bdc300101e2f)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = kubernetes
        Validity
            Not Before: Jan  4 01:39:06 2025 GMT
            Not After : Jan  4 01:44:06 2026 GMT
            # 下面Organization的值为kubeadm: cluster-admins，意思是将该用户加入组cluster-admins中
            # 下面有为什么cluster-admins有所有权限
        Subject: O = kubeadm:cluster-admins, CN = kube-apiserver-kubelet-client
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                ......
                
# 查看集群角色权限
[root@master1 pki]#kubectl get clusterrole cluster-admin -o yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  creationTimestamp: "2025-01-04T01:44:14Z"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: cluster-admin     # 给集群角色cluster-admin全部权限，下面都是*，就表示授予所有权限
  resourceVersion: "74"
  uid: 7defd096-536a-4bd1-890c-e496d1c5f35e
rules:
- apiGroups:
  - '*'
  resources:
  - '*'
  verbs:
  - '*'
- nonResourceURLs:
  - '*'
  verbs:
  - '*'

# 查看role角色cluster-admin同名的clusterrolebinding，分配权限给kubeadm:cluster-admins组
[root@master1 pki]# kubectl get clusterrolebinding kubeadm:cluster-admins -o yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  creationTimestamp: "2025-01-04T01:44:15Z"
  name: kubeadm:cluster-admins
  resourceVersion: "204"
  uid: c0010b58-45ce-4d63-a0b4-e1a1632f3977
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin   # 将这个拥有全部权限的角色，赋予下面的组kubeadm:cluster-admins
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: kubeadm:cluster-admins   # 因此这里这个组cluster-admins有全部权限

```



##### 认证插件

Kubernetes 通过身份认证插件利用**客户端证书**、**持有者令牌（Bearer Token）**或**身份认证代理 （Proxy）** 来认证 API 请求的身份。

kubernetes提供了多种认证方式，可以同时使用一种或多种认证方式，只要通过任何一个成功即被认作 是认证通过。即或关系



**常见的认证方式如下：**

| 认证方式            | 解析                                                         |
| ------------------- | ------------------------------------------------------------ |
| X509 客户端证书认证 | TLS双向认证，客户端持有数字证书,API Server信任客户端证书的颁发者.即服务器客户 端互相验证<br />**信任的CA**需要在kube-apiserver启动时,通过**--client-ca-file选项指定**.<br />证书中的Subject中的 **CN(CommonName)即被识别为用户名**，而**O（Organization） 被识别为组名**<br />对于这种客户的账号，k8s是无法管理的。为了使用这个方案，api-server需要用-- client-ca-file、--tls-private-key-file、--tls-cert-file选项来开启。<br />kubeadm部署的Kubernetes集群，默认使用 **/etc/kubernetes/pki/ca.crt** 进行客户端认证,此文件是kubeadm为Kubernetes各组件间颁发数字证书的**根CA** |
| 令牌认证 (Token)    | 在节点数量非常多的时候，大量手动配置TLS认证比较麻烦，可以**通过在api-server开 启 experimental-bootstrap-token-auth 特性**，**通过对客户端的和k8s平台预先定义的 token信息进行匹配**，**认证通过后，自动为节点颁发证书**，可以大大减轻工作量，而且 应用场景非常广。<br />包括: Service Account 令牌,静态令牌文件,Bootstrap令牌,OIDC(OpenID Connect)令 牌,Webhook 令牌 等 |
| 代理认证            | 一般借助于中间代理的方式来进行统用的认证方式，样式不固定     |
| 匿名                | 无法认证的其它请求                                           |



**API Server启用的身份认证机制**

- 基于认证插件支持多种认证方式，而相应认证插件的启用需要经由kube-apiserver上的专用选项完成
- kubeadm 部署的集群默认启用的认证机制包括如下几种
  - X509客户端证书认证
  - Bootstrap令牌认证
  - 前端代理身份认证 front-proxy
  - Service Account 令牌
- 注意：API Server并不保证各认证插件的生效次序与定义的次序相同



**范例: 查看API Server 的认证机制**

```bash
#在Master节查看认证机制
[root@master1 pki] # cat /etc/kubernetes/manifests/kube-apiserver.yaml 
apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 10.0.0.201:6443
  creationTimestamp: null
  labels:
    component: kube-apiserver
    tier: control-plane
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
  - command:
    - kube-apiserver
    - --advertise-address=10.0.0.201
    - --allow-privileged=true
    - --authorization-mode=Node,RBAC
    - --client-ca-file=/etc/kubernetes/pki/ca.crt             # x509客户端认证，此CA颁发的证书对应的用户是合法用户
    - --enable-admission-plugins=NodeRestriction
    - --enable-bootstrap-token-auth=true                      # Bootstrap 令牌认证
    - --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt
    - --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt
    - --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key
    - --etcd-servers=https://127.0.0.1:2379
    - --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt
    - --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
    - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
    - --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt     # 身份认证代理
    - --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key      # 身份认证代理
    - --requestheader-allowed-names=front-proxy-client                        # 身份认证代理
    - --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt   # 身份认证代理
    - --requestheader-extra-headers-prefix=X-Remote-Extra-                    # 身份认证代理
    - --requestheader-group-headers=X-Remote-Group                            # 身份认证代理
    - --requestheader-username-headers=X-Remote-User                          # 身份认证代理
    - --secure-port=6443
    - --service-account-issuer=https://kubernetes.default.svc.cluster.local   # SA认证
    - --service-account-key-file=/etc/kubernetes/pki/sa.pub                   # SA认证
    - --service-account-signing-key-file=/etc/kubernetes/pki/sa.key           # SA认证
    - --service-cluster-ip-range=10.96.0.0/12
    - --tls-cert-file=/etc/kubernetes/pki/apiserver.crt
    - --tls-private-key-file=/etc/kubernetes/pki/apiserver.key
    image: registry.aliyuncs.com/google_containers/kube-apiserver:v1.30.2
    imagePullPolicy: IfNotPresent
    livenessProbe:
      failureThreshold: 8
      httpGet:
        host: 10.0.0.201
        path: /livez
        port: 6443
        scheme: HTTPS
      initialDelaySeconds: 10
      periodSeconds: 10
      timeoutSeconds: 15
    name: kube-apiserver
    readinessProbe:
      failureThreshold: 3
      httpGet:
        host: 10.0.0.201
        path: /readyz
        port: 6443
        scheme: HTTPS
      periodSeconds: 1
      timeoutSeconds: 15
    resources:
      requests:
        cpu: 250m
    startupProbe:
      failureThreshold: 24
      httpGet:
        host: 10.0.0.201
        path: /livez
        port: 6443
        scheme: HTTPS
      initialDelaySeconds: 10
      periodSeconds: 10
      timeoutSeconds: 15
    volumeMounts:
    - mountPath: /etc/ssl/certs
      name: ca-certs
      readOnly: true
    - mountPath: /etc/ca-certificates
      name: etc-ca-certificates
      readOnly: true
    - mountPath: /etc/pki
      name: etc-pki
      readOnly: true
    - mountPath: /etc/kubernetes/pki
      name: k8s-certs
      readOnly: true
    - mountPath: /usr/local/share/ca-certificates
      name: usr-local-share-ca-certificates
      readOnly: true
    - mountPath: /usr/share/ca-certificates
      name: usr-share-ca-certificates
      readOnly: true
  hostNetwork: true
  priority: 2000001000
  priorityClassName: system-node-critical
  securityContext:
    seccompProfile:
      type: RuntimeDefault
  volumes:
  - hostPath:
      path: /etc/ssl/certs
      type: DirectoryOrCreate
    name: ca-certs
  - hostPath:
      path: /etc/ca-certificates
      type: DirectoryOrCreate
    name: etc-ca-certificates
  - hostPath:
      path: /etc/pki
      type: DirectoryOrCreate
    name: etc-pki
  - hostPath:
      path: /etc/kubernetes/pki
      type: DirectoryOrCreate
    name: k8s-certs
  - hostPath:
      path: /usr/local/share/ca-certificates
      type: DirectoryOrCreate
    name: usr-local-share-ca-certificates
  - hostPath:
      path: /usr/share/ca-certificates
      type: DirectoryOrCreate
    name: usr-share-ca-certificates
status: {}
```



**Kubelet启用的身份认证机制**

- kubelet的REST API端点默认通过TCP协议的10250端口提供，支持管理操作

| Kubelet API | 功能简介                   |
| ----------- | -------------------------- |
| /pods       | 列出当前kubelet节点上的Pod |
| /run        | 在一个容器内运行指定的命令 |
| /exec       | 在一个容器内运行指定的命令 |
| /configz    | 设置Kubelet的配置文件参数  |
| /debug      | 调试信息                   |

- 需要对客户端身份进行认证
- 启用的身份认证:webhook,x509客户端证书认证
  - 注意：建议显式禁用匿名用户
- API Server是该API端点的客户端，因此，kubelet需要在验证客户端身份时信任给API Server颁发数字证书的CA



**范例：查看Kubelet的认证机制**

```yaml
#在每个worker节点查看
[root@node1 pki] # cat /var/lib/kubelet/config.yaml 
apiVersion: kubelet.config.k8s.io/v1beta1
authentication:
  anonymous:
    enabled: false                             # 匿名认证，true为允许匿名访问，但是权限不足
  webhook:
    cacheTTL: 0s                               # webhook认证
    enabled: true
  x509:
    clientCAFile: /etc/kubernetes/pki/ca.crt   # 证书认证
authorization:
  mode: Webhook
  webhook:
    cacheAuthorizedTTL: 0s
    cacheUnauthorizedTTL: 0s
cgroupDriver: systemd
clusterDNS:
- 10.96.0.10
clusterDomain: cluster.local
containerRuntimeEndpoint: ""
cpuManagerReconcilePeriod: 0s
evictionPressureTransitionPeriod: 0s
fileCheckFrequency: 0s
healthzBindAddress: 127.0.0.1
healthzPort: 10248
httpCheckFrequency: 0s
imageMaximumGCAge: 0s
imageMinimumGCAge: 0s
kind: KubeletConfiguration
logging:
  flushFrequency: 0
  options:
    json:
      infoBufferSize: "0"
    text:
      infoBufferSize: "0"
  verbosity: 0
memorySwap: {}
nodeStatusReportFrequency: 0s
nodeStatusUpdateFrequency: 0s
resolvConf: /run/systemd/resolve/resolv.conf
rotateCertificates: true
runtimeRequestTimeout: 0s
shutdownGracePeriod: 0s
shutdownGracePeriodCriticalPods: 0s
staticPodPath: /etc/kubernetes/manifests
streamingConnectionIdleTimeout: 0s
syncFrequency: 0s
volumeStatsAggPeriod: 0s

#如果修改,不建议修改/var/lib/kubelet/config.yaml配置文件,而通过修改对应的configmap实现
[root@master1 pki]#kubectl get -n kube-system cm kubelet-config -o yaml
apiVersion: v1
data:
  kubelet: |
    apiVersion: kubelet.config.k8s.io/v1beta1
    authentication:
      anonymous:
        enabled: false
      webhook:
        cacheTTL: 0s
        enabled: true
      x509:
        clientCAFile: /etc/kubernetes/pki/ca.crt
    authorization:
      mode: Webhook
      webhook:
        cacheAuthorizedTTL: 0s
        cacheUnauthorizedTTL: 0s
    cgroupDriver: systemd
    clusterDNS:
    - 10.96.0.10
    clusterDomain: cluster.local
    containerRuntimeEndpoint: ""
    cpuManagerReconcilePeriod: 0s
    evictionPressureTransitionPeriod: 0s
    fileCheckFrequency: 0s
    healthzBindAddress: 127.0.0.1
    healthzPort: 10248
    httpCheckFrequency: 0s
    imageMaximumGCAge: 0s
    imageMinimumGCAge: 0s
    kind: KubeletConfiguration
    logging:
      flushFrequency: 0
      options:
        json:
          infoBufferSize: "0"
        text:
          infoBufferSize: "0"
      verbosity: 0
    memorySwap: {}
    nodeStatusReportFrequency: 0s
    nodeStatusUpdateFrequency: 0s
    resolvConf: /run/systemd/resolve/resolv.conf
    rotateCertificates: true
    runtimeRequestTimeout: 0s
    shutdownGracePeriod: 0s
    shutdownGracePeriodCriticalPods: 0s
    staticPodPath: /etc/kubernetes/manifests
    streamingConnectionIdleTimeout: 0s
    syncFrequency: 0s
    volumeStatsAggPeriod: 0s
kind: ConfigMap
metadata:
  annotations:
    kubeadm.kubernetes.io/component-config.hash: sha256:14a463ee2caafeaa2b6d58bb8c225fb8e9e4509ed1a77d8c55a943bc7d89f7ac
  creationTimestamp: "2025-01-04T01:44:15Z"
  name: kubelet-config
  namespace: kube-system
  resourceVersion: "208"
  uid: 4e74f407-d431-4379-9a22-4cd5b9f64916
```



#### X509客户端认证

Kubernetes集群中的X509客户端认证依赖于PKI证书体系,有如下三套CA证书系统

![image-20250107194258441](D:\git_repository\cyber_security_learning\markdown_img\image-20250107194258441.png)

kubeadm部署Kubernetes集群时会自动生成所需要的证书，它们位于**/etc/kubernetes/pki**自录下

| 文件                                     | Default CN               | 说明                           |
| ---------------------------------------- | ------------------------ | ------------------------------ |
| ca.crt,ca.key                            | kubernetes-ca            | Kubernetes general CA          |
| etcd/ca.crt,etcd/ca.key                  | etcd-ca                  | For all etcd-related functions |
| front-proxy-ca.crt,front-proxyca.crt.key | kubernetes-frontproxy-ca | For the front-end proxy        |



**案例**

#####  **创建基于X509客户端普通的用户证书**

```ABAP
原理：客户端，无论是使用kubectl还是curl，和apiServer通信，客户端使用的证书是apiServer服务端上有的ca证书生成的，所以客户端使用的证书可以被服务端信任，就这么简单，哈哈哈
```



```bash
# 查看到以下内容，表示默认kubernetes的CA签发的证书，都是k8s客户端的用户
[root@master1 kubelet]#grep '\-\-client-ca-file' /etc/kubernetes/manifests/kube-apiserver.yaml 
    - --client-ca-file=/etc/kubernetes/pki/ca.crt

# #在master节点创建test用户证书
[root@master1 ~]#mkdir pki
[root@master1 pki]#(umask 077; openssl genrsa -out pki/mystical.key 4096)
[root@master1 pki]#ls pki/
mystical.key

# 生成证书申请,加入ops组只具有普通权限
[root@master1 pki]# openssl req -new -key ./mystical.key -out ./mystical.csr -subj "/CN=mystical/O=ops"
[root@master1 pki]# ls
mystical.csr  mystical.key

#使用kubernetes-ca颁发证书
[root@master1 pki]#openssl x509 -req -days 3650 -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -in ./mystical.csr -out ./mystical.crt
Certificate request self-signature ok
subject=CN = mystical, O = ops

# 复制证书文件到worker节点
[root@master1 ~]#scp -r pki/ 10.0.0.202:
mystical.key                                        100% 3272     1.7MB/s   00:00    
mystical.csr                                        100% 1602     2.4MB/s   00:00    
mystical.crt                                        100% 1359     2.0MB/s   00:00 

#在worker节点使用kubectl访问，正常是没有权限的
[root@node1 pki]#kubectl get pod
E0107 20:00:19.853410  205917 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused

# 使用刚创建的证书进行访问，显示的是无权限，而不是拒绝访问，是Forbidden
[root@node1 ~]#kubectl get pod --server=https://10.0.0.201:6443 --client-certificate=pki/mystical.crt --client-key=pki/mystical.key --certificate-authority=/etc/kubernetes/pki/ca.crt
Error from server (Forbidden): pods is forbidden: User "mystical" cannot list resource "pods" in API group "" in the namespace "default"

# 或者下面选项忽略证书校验也可以
[root@node1 ~]#kubectl get pod --server=https://10.0.0.201:6443 --client-certificate=pki/mystical.crt --client-key=pki/mystical.key --insecure-skip-tls-verify=true
Error from server (Forbidden): pods is forbidden: User "mystical" cannot list resource "pods" in API group "" in the namespace "default"

# 通过curl使用证书访问，仍是权限不足
[root@node1 ~]#curl --cert pki/mystical.crt --key pki/mystical.key --key-type PEM --cacert /etc/kubernetes/pki/ca.crt https://10.0.0.201:6443
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "forbidden: User \"mystical\" cannot get path \"/\"",
  "reason": "Forbidden",
  "details": {},
  "code": 403
}
```



##### 创建基于X509客户端管理员的用户证书

```bash
# 创建管理员用户admin证书
[root@master1 pki]#(umask 077; openssl genrsa -out ./admin.key 4096)

[root@master1 pki]#ls
admin.key  mystical.crt  mystical.csr  mystical.key

# 生成证书申请文件，注意：加入system:masters组成System组才具有管理权限
# 新版
[root@master1 pki]#openssl req -new -key ./admin.key -out ./admin.csr -subj "/CN=admin/O=kubeadm:cluster-admins"

[root@master1 pki]#ls
admin.csr  admin.key  mystical.crt  mystical.csr  mystical.key

#查看到system:masters组被授权ClusterRole角色,具有集群的管理权限
#新版
[root@master1 pki]#kubectl get clusterrolebindings.rbac.authorization.k8s.io kubeadm:cluster-admins -o yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  creationTimestamp: "2025-01-04T01:44:15Z"
  name: kubeadm:cluster-admins
  resourceVersion: "204"
  uid: c0010b58-45ce-4d63-a0b4-e1a1632f3977
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin            # 该角色被赋予了所有权限
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: kubeadm:cluster-admins   # 组
  
# 使用kubernetes-ca颁发证书
[root@master1 pki]#openssl x509 -req -days 3650 -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -in ./admin.csr -out ./admin.crt
Certificate request self-signature ok
subject=CN = admin, O = kubeadm:cluster-admins

[root@master1 pki]#ls
admin.crt  admin.csr  admin.key  mystical.crt  mystical.csr  mystical.key

# 传给worker节点
[root@master1 ~]#scp -r pki/ 10.0.0.202:

# work节点使用证书访问测试
[root@node1 ~]#kubectl get ns -s https://10.0.0.201:6443 --certificate-authority=/etc/kubernetes/pki/ca.crt --client-certificate=pki/admin.crt --client-key=pki/admin.key
NAME              STATUS   AGE
default           Active   3d11h
ingress-nginx     Active   3d9h
kube-flannel      Active   3d11h
kube-node-lease   Active   3d11h
kube-public       Active   3d11h
kube-system       Active   3d11h
metallb-system    Active   3d9h

# curl命令使用证书访问
[root@node1 ~]#curl --cert pki/wang.crt --key pki/wang.key --key-type PEM --cacert /etc/kubernetes/pki/ca.crt https://10.0.0.201:6443/api
{
  "kind": "APIVersions",
  "versions": [
    "v1"
  ],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.0.0.201:6443"
    }
  ]

#注意：如果在master节点执行会出现下面提示错
[root@master1 ~]#kubectl get ns -s https://10.0.0.201:6443 --certificate-authority=/etc/kubernetes/pki/ca.crt --client-certificate=pki/wang.crt --client-key=pki/wang.key
Error in configuration: 
* client-cert-data and client-cert are both specified for kubernetes-admin. client-cert-data will override.
* client-key-data and client-key are both specified for kubernetes-admin; client-key-data will override

#提示错误的原因:$HOME/.kube/config文件还有其它用户身份，解决方法如下
[root@master1 ~]# mv ~/.kube/config /tmp

#再次执行成功
[root@master1 ~]#]#kubectl get ns -s https://10.0.0.201:6443 --certificate-authority=/etc/kubernetes/pki/ca.crt --client-certificate=pki/wang.crt --client-key=pki/wang.key
pod-test-6d8c97ff75-qt8zq   1/1     Running   1 (10h ago)   2d
pod-test-6d8c97ff75-rhwkv   1/1     Running   1 (10h ago)   2d
pod-test-6d8c97ff75-tmtl9   1/1     Running   1 (10h ago)   2d
```



##### 方法2：使用kubernetes资源接管CSR证书申请文件

```bash
# 创建私钥
[root@master1 ~]#openssl genrsa -out test2.key 2048

# 创建证书申请
[root@master1 pki]#openssl req -new -key test2.key -out test2.csr -subj "/CN=test2/O=devops"

# 查看证书信息
[root@master1 pki]#cat test2.csr|base64 |tr -d "\n"
LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1pqQ0NBVTRDQVFBd0lURU9NQXdHQTFVRUF3d0ZkR1Z6ZERJeER6QU5CZ05WQkFvTUJtUmxkbTl3Y3pDQwpBU0l3RFFZSktvWklodmNOQVFFQkJRQURnZ0VQQURDQ0FRb0NnZ0VCQUpoSUFOUzlra2x4ZFVxZjlqanRWZ2VnCm1ibkk1TUFYTjNJMU9WakZpQjd0UlhURzZuQngwOHFjM1lBc0NYcmQ5NFExYlVKbUNJR3Fyd0xVU1N4ZURJRlQKcEwreWR1QjlWdkN2MEhXbHFPbE9FcjNlUGtsV3pheUJpNUhqbUJYYlZrNUpsMlk2L1NZTkdzLzFhZWFFMk1FZApwSlAydTJFSDdqMFVvYVhSNlNVV1hwLzFGYjhkRXAvR2VaM29taFFKaC9uM0dvKzhCSlV5MStVRlF3b1VMMEtKCm05R2tKbnFPUkR4OTQ0RVptRmxKOFg1bXFFbHhkUUg3TGtRcXhpTkY4TitJUmZtdXplVVp6VncrbzFzRGo3STMKY2JrZCsrTGVVVmJkbC9VZThlUlphdHVZTzJZQy9TMk85S2loTWZONXR2K0ZnNjl1Ylc5RkhIK1g2L25XS3JjQwpBd0VBQWFBQU1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQXFyVlVLR3VWaHdxdjRuZnBsQVV3T0NaSkFNemcwCm5tMVpNYnFUeGM4ZE1BZFFBQTJOcTVOOEhMQzJ4NFhQeDdlUlFGL2hVSUh5SE0wZUNCcTVlV1htTlRlbERkdTUKWTVja1hkbjJOZmVVd0lJMmtNcGxyMXlxam9nTXc3QTIzemVYdHB6R29PbkxvZ1ZkV3Z0c1ludmNIS0hHSUVnWApSRUwwdDRtY0d2UkMrMFFRVjVEd1pBb2FTdnE0d3pzdllQSktFUmNSdzBNT2dzVGZ2ZXBlMW1mWVNYUCtMRUswCkVHYVVaY0tuY3FpTFFLdzY2SzVyU1ZMa25VMDBhcktIUGlvWWNyb0pRYktWN0w5ekMrblFtNHRYNFJDWFRPd2UKZ1QrdFVxTEZHK1hwNDlSUWNvblZhU0tZWjgzVnlHa2lPMjZqWUpOWHJUSUFPYmsrQ1ZJajJQMngKLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tCg==


[root@master1 pki]#cat security-certificaterequests-test2.yaml 
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: test2
spec:
  # request: XXXX...
  requests: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1pqQ0NBVTRDQVFBd0lURU9NQXdHQTFVRUF3d0ZkR1Z6ZERJeER6QU5CZ05WQkFvTUJtUmxkbTl3Y3pDQwpBU0l3RFFZSktvWklodmNOQVFFQkJRQURnZ0VQQURDQ0FRb0NnZ0VCQUpoSUFOUzlra2x4ZFVxZjlqanRWZ2VnCm1ibkk1TUFYTjNJMU9WakZpQjd0UlhURzZuQngwOHFjM1lBc0NYcmQ5NFExYlVKbUNJR3Fyd0xVU1N4ZURJRlQKcEwreWR1QjlWdkN2MEhXbHFPbE9FcjNlUGtsV3pheUJpNUhqbUJYYlZrNUpsMlk2L1NZTkdzLzFhZWFFMk1FZApwSlAydTJFSDdqMFVvYVhSNlNVV1hwLzFGYjhkRXAvR2VaM29taFFKaC9uM0dvKzhCSlV5MStVRlF3b1VMMEtKCm05R2tKbnFPUkR4OTQ0RVptRmxKOFg1bXFFbHhkUUg3TGtRcXhpTkY4TitJUmZtdXplVVp6VncrbzFzRGo3STMKY2JrZCsrTGVVVmJkbC9VZThlUlphdHVZTzJZQy9TMk85S2loTWZONXR2K0ZnNjl1Ylc5RkhIK1g2L25XS3JjQwpBd0VBQWFBQU1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQXFyVlVLR3VWaHdxdjRuZnBsQVV3T0NaSkFNemcwCm5tMVpNYnFUeGM4ZE1BZFFBQTJOcTVOOEhMQzJ4NFhQeDdlUlFGL2hVSUh5SE0wZUNCcTVlV1htTlRlbERkdTUKWTVja1hkbjJOZmVVd0lJMmtNcGxyMXlxam9nTXc3QTIzemVYdHB6R29PbkxvZ1ZkV3Z0c1ludmNIS0hHSUVnWApSRUwwdDRtY0d2UkMrMFFRVjVEd1pBb2FTdnE0d3pzdllQSktFUmNSdzBNT2dzVGZ2ZXBlMW1mWVNYUCtMRUswCkVHYVVaY0tuY3FpTFFLdzY2SzVyU1ZMa25VMDBhcktIUGlvWWNyb0pRYktWN0w5ekMrblFtNHRYNFJDWFRPd2UKZ1QrdFVxTEZHK1hwNDlSUWNvblZhU0tZWjgzVnlHa2lPMjZqWUpOWHJUSUFPYmsrQ1ZJajJQMngKLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tCg==
  signerName: kubernetes.io/kube-apiserver-client
  expirationSeconds: 8640000
  usages:
  - client auth

# 生成CSR资源对象
[root@master1 pki]#kubectl apply -f security-certificaterequests-test2.yaml 
certificatesigningrequest.certificates.k8s.io/test2 created

# 查看
[root@master1 pki]#kubectl get csr
NAME    AGE    SIGNERNAME                            REQUESTOR          REQUESTEDDURATION   CONDITION
test2   119s   kubernetes.io/kube-apiserver-client   kubernetes-admin   100d                Pending

# 以kubernetes管理员身份，颁发证书
[root@master1 pki]# kubectl certificate approve test2
certificatesigningrequest.certificates.k8s.io/test2 approved

# 查看状态已颁发
[root@master1 pki]#kubectl get csr
NAME    AGE    SIGNERNAME                            REQUESTOR          REQUESTEDDURATION   CONDITION
test2   3m4s   kubernetes.io/kube-apiserver-client   kubernetes-admin   100d                Approved,Issued

# 获取证书
[root@master1 pki]#kubectl get csr test2 -o jsonpath={.status.certificate}|base64 -d > test2.crt

[root@master1 pki]#cat test2.crt 
-----BEGIN CERTIFICATE-----
MIIDBzCCAe+gAwIBAgIRAMjOBLtzoxNSnwuFWP0q0awwDQYJKoZIhvcNAQELBQAw
FTETMBEGA1UEAxMKa3ViZXJuZXRlczAeFw0yNTAxMDcxNDMxNDVaFw0yNTA0MTcx
NDMxNDVaMCExDzANBgNVBAoTBmRldm9wczEOMAwGA1UEAxMFdGVzdDIwggEiMA0G
CSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCYSADUvZJJcXVKn/Y47VYHoJm5yOTA
FzdyNTlYxYge7UV0xupwcdPKnN2ALAl63feENW1CZgiBqq8C1EksXgyBU6S/snbg
fVbwr9B1pajpThK93j5JVs2sgYuR45gV21ZOSZdmOv0mDRrP9WnmhNjBHaST9rth
B+49FKGl0eklFl6f9RW/HRKfxnmd6JoUCYf59xqPvASVMtflBUMKFC9CiZvRpCZ6
jkQ8feOBGZhZSfF+ZqhJcXUB+y5EKsYjRfDfiEX5rs3lGc1cPqNbA4+yN3G5Hfvi
3lFW3Zf1HvHkWWrbmDtmAv0tjvSooTHzebb/hYOvbm1vRRx/l+v51iq3AgMBAAGj
RjBEMBMGA1UdJQQMMAoGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgw
FoAU1qvukPDcEq9gVsqNRan7GdWoTHswDQYJKoZIhvcNAQELBQADggEBAAenQ8eL
1+eOA7hpwuNcEZJs+OCn2CUFtYWQ+SHQQ0yhcfACcxXzXt7XagShKC4ZmP0oeAwq
YBgoFSGiJKetDhFLVdvN/ZeUsXoplg017QgfQZ0N3kOqhwkKeIPlY0dAB5S2v1Nb
CvMk/gyXqTGqGB57bVXYZUEHZ3G5xAB2mmskNa38tBykOFrhQfL7BB7rCD9HUZDE
QGbgyZxi7Oio8MDc7wEsG85GyE6FWyE+2ad6SLOLtB7pLvGltencMF2q0JWhqFzv
oWJ7T9b93TS5Xj2yQNg2zIDhZlNi8Wr9qdC0Qe2Kbr/Ose7I9M8gtmmUaNxj0UY/
ZMZO1382+baf02Q=
-----END CERTIFICATE-----

[root@master1 pki]#openssl x509 -in test2.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            c8:ce:04:bb:73:a3:13:52:9f:0b:85:58:fd:2a:d1:ac
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = kubernetes
        Validity
            Not Before: Jan  7 14:31:45 2025 GMT
            Not After : Apr 17 14:31:45 2025 GMT
        Subject: O = devops, CN = test2

# 后续使用这个证书可以正常访问，按上述方法
```





#### 令牌认证

#####  常见的令牌认证

- **引导令牌**

  - kubeadm创建集群初始化环境时，自动创建好的一次性令牌，用于其他节点加入到集群环境中

  ```bash
  kubeadm join kubeapi.wang.org:6443 --token jizd9o.tjfoyvdoisbklfi5 \
  	--discovery-token-ca-cert-hash sha256:c27e15a7a39394b6d64e419b60df835f9dedb7b015a92c1d9285effa1fbea600 \  # 这里就是引导令牌
  	--control-plane --certificate-key 9fa84696a800c6b995a9249972c1dd76735701e5ea2ae05191c9f612a0d1252c --cri-socket=unix:///run/cri-dockerd.sock # 后面追加 --cri-socket=unix:///run/cri-dockerd.sock
  ```

  

- **静态令牌**
  - 将用户和令牌存放于**文本文件**中,并启动API Server进程时加载此文件，该文件内容会由API Server缓存于内存中
  - 由kube-apiserver在启动时通过--token-auth-file选项加载,**默认没有加载此选项**
  - 加载完成后的文件变动，仅能通过重启程序进行重载，因此，相关的令牌会长期有效
  - 客户端在HTTP请求中，通过“**Authorization Bearer TOKEN**”标头附带令牌令牌以完成认证
  - 比如在使用kubelet的时候，需要依赖的token文件



- **静态密码**
  - 存储于API Server进程可直接加载到的文件中保存的账户和密码令牌，该文件内容会由API Server 缓存于内存中
  - 比如在使用kubelet的时候，需要依赖的.kube/config文件



- **Service Account 令牌**
  - 此令牌专用于ServiceAccount
  - 用于将Pod认证到API Server 上，以支持集群内的进程与API Server通信
  - 该认证方式将由kube-apiserver程序内置直接启用它借助于经过签名的Bearer Token来验证请求
  - 签名时使用的密钥可以由--service-account-key-file选项指定，也可以默认使用API Server的tls私钥
  - Kubernetes可使用ServiceAccount准入控制器自动为Pod关联ServiceAccount



- **OIDC令牌**
  - OIDC 就是 OpenID Connect，是一种动态令牌,主要应用于集成第三方认证的一种集中式认证方式
  - 比如: KeyCloak,通常遵循OAuth 2协议。尤其是第三方云服务商的认证



- **Webhook令牌**
  - 常应用于触发第三方的动作时候的一些认证机制，主要侧重于http协议场景。





##### 静态令牌认证实现

- **静态令牌认证的配置说明**

  - 令牌信息保存于**格式为CSV**的文本文件，每行定义一个用户，由“**令牌、用户名、用户ID和所属的用户组**”四个字段组成，用户组为可选字段

  ```ABAP
  格式: token, user, uid, "group1, group2, ......"
  ```

  - 由kube-apiserver在启动时通过--token-auth-file选项加载
  - 加载完成后如果再有文件变动，需要通过重启kube-apiserver进行重载
  - 可在客户端在HTTP请求中，通过“Authorization Bearer TOKEN”标头附带令牌令牌以完成认证



- **静态令牌认证配置过程**

  - 生成token，命令：echo "$(openssl rand -hex 3).$(openssl rand -hex 8)"

  ```bash
  echo "$(openssl rand -hex 3).$(openssl rand -hex 8)"  # 3和8表示的字节数，整体意思是3个字节的16进制显示的随机数
  ```

  - 生成static token文件
  - 配置kube-apiserver加载该静态令牌文件以启用相应的认证功能
  - 测试命令

  ```bash
  #方法1
  curl -k -H "Authorization: Bearer $TOKEN"
  https://API_SERVER:6443/api/v1/namespaces/default/pods/
  
  #方法2
  kubectl --insecure-skip-tls-verify  --token=$TOKEN -s
  https://kubeapi.wang.org:6443 get pod
  
  #说明： TOKEN表示上面用户生成的token 
  ```



**范例: 基于静态token令牌向API Server添加认证用户**

```bash
#在所有Master节点上配置下面过程,如果只有一个Master节点配置,只能连接此Master节点测试
#准备Token文件存放的独立目录
[root@master1 ~]#mkdir /etc/kubernetes/auth

# 创建静态令牌文件并添加用户信息
[root@master1 auth]#echo "$(openssl rand -hex 3).$(openssl rand -hex 8),wang,1001,ops" > /etc/kubernetes/auth/token.csv
[root@master1 auth]#echo "$(openssl rand -hex 3).$(openssl rand -hex 8),test,1002,dev" >> /etc/kubernetes/auth/token.csv

# 查看
[root@master1 auth]#cat /etc/kubernetes/auth/token.csv 
1ec32a.838c37d29a7c43b6,wang,1001,ops
fd3e78.2a0395a1c58fb561,test,1002,dev

#先备份配置文件，注意：不要将备份文件放在原目录下；
[root@master1 backup]#cp /etc/kubernetes/manifests/kube-apiserver.yaml .

#直接修改原文件
[root@master1 ~]#vim /etc/kubernetes/manifests/kube-apiserver.yaml 
......
  - command:
    - kube-apiserver
    - --advertise-address=10.0.0.200
    - --allow-privileged=true
    - --authorization-mode=Node,RBAC
    - --client-ca-file=/etc/kubernetes/pki/ca.crt
    - --token-auth-file=/etc/kubernetes/auth/token.csv  #指定前面创建文件的路径
.....
   volumeMounts:
   ......
    - mountPath: /etc/kubernetes/auth                   #添加三行,实现数据卷的挂载配
置
     name: static-auth-token
     readOnly: true
 hostNetwork: true
......
 volumes:
 .......
  - hostPath:                                           #添加三行数据卷定义
     path: /etc/kubernetes/auth
     type: DirectoryOrCreate
   name: static-auth-token
   
# 上面文件修改后,Kubernetes会自动重启名为kube-apiserver-master1.wang.org的Pod,可能需要等一会儿才能启动成功
# apiServer重启期间可能报错，访问可能报错，需等待
[root@master1 backup]# kubectl get pod -n kube-system kube-apiserver
The connection to the server master1.mystical.org:6443 was refused - did you specify the right host or port?


# 一段时间后，重启成功
[root@master1 backup]#kubectl get pod -n kube-system kube-apiserver-master1 
NAME                     READY   STATUS    RESTARTS   AGE
kube-apiserver-master1   1/1     Running   0          2m54s


#查看容器是否加载了token.csv文件
[root@master1 backup]# docker ps |grep api
a8e08a3f681f   56ce0fd9fb53                                        "kube-apiserver --ad…"   33 seconds ago   Up 32 seconds             k8s_kube-apiserver_kube-apiserver-master1_kube-system_a940e438a9aff369d80b49179ee0f235_0
a90cdbbf53f0   registry.aliyuncs.com/google_containers/pause:3.9   "/pause"                  33 seconds ago   Up 32 seconds             k8s_POD_kube-apiserver-master1_kube-system_a940e438a9aff369d80b49179ee0f235_0

[root@master1 backup]# docker inspect a8e08a3f681f |grep -n token.csv
11:            "--token-auth-file=/etc/kubernetes/auth/token.csv",
302:                "--token-auth-file=/etc/kubernetes/auth/token.csv",


#验证方法1:使用上面任意用户的token访问,提示用户wang被禁止访问，说明用户验证成功，只是权限不足
#注意:如果只是修改一下master节点的配置,只能连接此节点测试,示例: "https://修改配置的master节点:6443/api/....."

[root@master1 backup]#TOKEN="1ec32a.838c37d29a7c43b6";curl -k -H"Authorization: Bearer $TOKEN" https://10.0.0.201:6443/api/v1/namespaces/default/pods/
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "pods is forbidden: User \"wang\" cannot list resource \"pods\" in API group \"\" in the namespace \"default\"",
  "reason": "Forbidden",
  "details": {
    "kind": "pods"
  },
  "code": 403

# 验证方法2:在worker节点执行,提示用户wang被禁止访问，说明用户验证成功，只是权限不足
#注意:如果只是修改一下master节点的配置,只能连接此节点测试,示例: -s "https://修改配置的master节点:6443"

[root@node1 ~]#TOKEN="1ec32a.838c37d29a7c43b6";kubectl -s "https://10.0.0.201:6443" --token="$TOKEN" --insecure-skip-tls-verify=true get pod
Error from server (Forbidden): pods is forbidden: User "wang" cannot list resource "pods" in API group "" in the namespace "default"


# 使用错误Token访问，观察结果
[root@master1 backup]#TOKEN="1ec32a.838c37d29a7c43b5";curl -k -H"Authorization: Bearer $TOKEN" https://10.0.0.201:6443/api/v1/namespaces/default/pods/
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "Unauthorized",
  "reason": "Unauthorized",
  "code": 401


#不使用Token访问，观察结果，即匿名访问
[root@master1 backup]##curl -k https://10.0.0.201:6443/api/v1/namespaces/default/pods/{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "pods is forbidden: User \"system:anonymous\" cannot list resource \"pods\" in API group \"\" in the namespace \"default\"",
  "reason": "Forbidden",
  "details": {
    "kind": "pods"
  },
  "code": 403
}
```



#### Kubeconfig管理

kubeconfig 是YAML格式的文件，用于存储身份认证信息，以便于客户端加载并认证接入到API Server

kubeconfig 保存有认证到一或多个Kubernetes集群的相关配置信息，并允许管理员按需在各配置间灵活切换



##### Kubeconfig 文件格式

Kubeconfig包括如下信息

![image-20250108105650248](D:\git_repository\cyber_security_learning\markdown_img\image-20250108105650248.png)



- **clusters**：每个Kubernetes集群的信息，包括集群对应访问端点（API Server）的地址
- **users**：认证到API Server的用户的身份凭据列表
- **contexts**：将每一个user同可认证到的cluster建立关联关系的上下文列表
- **current-context**：当前默认使用的context



**客户端程序kubectl 加载的kubeconfig文件的途径及从高到低优先级次序**



- --kubeconfig选项,只支持一个文件
- KUBECONFIG环境变量：其值是包含有kubeconfig文件的列表,支持多个文件,用冒号隔离
- 默认路径：$HOME/.kube/config



**默认 /etc/kubernetes/*.conf 的文件都属于 Kubeconfig 文件**

```bash
[root@master1 backup]# ls /etc/kubernetes/*.conf
/etc/kubernetes/admin.conf               /etc/kubernetes/scheduler.conf
/etc/kubernetes/controller-manager.conf  /etc/kubernetes/super-admin.conf
/etc/kubernetes/kubelet.conf

[root@master1 backup]#grep "^[a-z]" /etc/kubernetes/*.conf
/etc/kubernetes/admin.conf: apiVersion: v1
/etc/kubernetes/admin.conf: clusters:
/etc/kubernetes/admin.conf: contexts:
/etc/kubernetes/admin.conf: current-context: kubernetes-admin@kubernetes
/etc/kubernetes/admin.conf: kind: Config
/etc/kubernetes/admin.conf: preferences: {}
/etc/kubernetes/admin.conf: users:

/etc/kubernetes/controller-manager.conf: apiVersion: v1
/etc/kubernetes/controller-manager.conf: clusters:
/etc/kubernetes/controller-manager.conf: contexts:
/etc/kubernetes/controller-manager.conf: current-context: system:kube-controller-manager@kubernetes
/etc/kubernetes/controller-manager.conf: kind: Config
/etc/kubernetes/controller-manager.conf: preferences: {}
/etc/kubernetes/controller-manager.conf: users:

/etc/kubernetes/kubelet.conf: apiVersion: v1
/etc/kubernetes/kubelet.conf: clusters:
/etc/kubernetes/kubelet.conf: contexts:
/etc/kubernetes/kubelet.conf: current-context: system:node:master1@kubernetes
/etc/kubernetes/kubelet.conf: kind: Config
/etc/kubernetes/kubelet.conf: preferences: {}
/etc/kubernetes/kubelet.conf: users:

/etc/kubernetes/scheduler.conf: apiVersion: v1
/etc/kubernetes/scheduler.conf: clusters:
/etc/kubernetes/scheduler.conf: contexts:
/etc/kubernetes/scheduler.conf: current-context: system:kube-scheduler@kubernetes
/etc/kubernetes/scheduler.conf: kind: Config
/etc/kubernetes/scheduler.conf: preferences: {}
/etc/kubernetes/scheduler.conf: users:

/etc/kubernetes/super-admin.conf: apiVersion: v1
/etc/kubernetes/super-admin.conf: clusters:
/etc/kubernetes/super-admin.conf: contexts:
/etc/kubernetes/super-admin.conf: current-context: kubernetes-super-admin@kubernetes
/etc/kubernetes/super-admin.conf: kind: Config
/etc/kubernetes/super-admin.conf: preferences: {}
/etc/kubernetes/super-admin.conf: users:
```



**利用kubeconfig实现集群外主机访问集群资源**

```bash
#在集群外节点安装kubectl工具
#方法1
[root@ubuntu2204 ~]# curl -s https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add -
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
OK

[root@ubuntu2204 ~]# cat << EOF > /etc/apt/sources.list.d/kubernetes.list
> deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
> EOF

# 查看
[root@ubuntu2204 ~]# cat /etc/apt/sources.list.d/kubernetes.list 
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main

# 更新元数据并安装
[root@ubuntu2204 ~]# apt update &> /dev/null && apt install -y kubectl &> /dev/null


# 方法2：直接将master节点的kubectl程序文件复制到集群外节点
[root@ubuntu2204 ~]#scp master1.wang.org:/usr/bin/kubectl /usr/local/bin/
[root@ubuntu2204 ~]#ls -l /usr/local/bin/
total 46904
-rwxr-xr-x 1 root root 48029696 Jul  6 14:23 kubectl
[root@ubuntu2204 ~]#ldd /usr/local/bin/kubectl 
 not a dynamic executable


# 将主节点的./kube/config传递到集群外节点
[root@master1 ~]# scp .kube/config 10.0.0.131:

# 在集群外节点配置hosts文件使其能够解析config中的apiServer地址的域名
echo "10.0.0.201 mater1.mystical.org" >> /etc/hosts

# 执行kubectl测试是否能够访问集群
[root@ubuntu2204 ~]# kubectl get nodes --kubeconfig=./config
NAME      STATUS   ROLES           AGE    VERSION
master1   Ready    control-plane   4d1h   v1.30.8
node1     Ready    <none>          4d1h   v1.30.8
node2     Ready    <none>          4d1h   v1.30.8
node3     Ready    <none>          4d1h   v1.30.8
```





##### Kubeconfig创建和管理



kubectl config 命令可以创建和管理kubeconfig文件

扩展工具: **kubectx** 和 **kubens**

**kubectx** is a tool to switch between contexts (clusters) on kubectl faster.

**kubens** is a tool to switch between Kubernetes namespaces (and configure them for kubectl) easily.



**kubectl config 命令用法**

```bash
#kubernetes 配置文件管理
[root@master1 ~]#kubectl config -h
Modify kubeconfig files using subcommands like "kubectl config set
current-context my-context".

 The loading order follows these rules:
 
 # 配置文件的基本信息
    1 使用 --kubeconfig 参数管理某个指定的配置文件路径
    2 该文件可以使用 $KUBECONFIG 变量来管理
    3 其他情况下，配置文件指的就是 ${HOME}/.kube/config 
   优先级： 1 > 2 > 3

  1.  If the --kubeconfig flag is set, then only that file is loaded. The flag
may only be set once and no merging takes place.

  2.  If $KUBECONFIG environment variable is set, then it is used as a list of
paths (normal path delimiting rules for your system). These paths are merged.
When a value is modified, it is modified in the file that defines the stanza.
When a value is created, it is created in the first file that exists. If no
files in the chain exist, then it creates the last file in the list.

  3.  Otherwise, ${HOME}/.kube/config is used and no merging takes place.


Available Commands:
  current-context   Display the current-context
  delete-cluster    从 kubeconfig 中删除指定的集群
  delete-context    从 kubeconfig 中删除指定的上下文
  delete-user       Delete the specified user from the kubeconfig
  get-clusters      显示在 kubeconfig 中定义的集群
  get-contexts      描述一个或多个上下文
  get-users         Display users defined in the kubeconfig
  rename-context    Rename a context from the kubeconfig file
  set               Set an individual value in a kubeconfig file
  set-cluster       Set a cluster entry in kubeconfig
  set-context       Set a context entry in kubeconfig
  set-credentials   Set a user entry in kubeconfig
  unset             Unset an individual value in a kubeconfig file
  use-context       Set the current-context in a kubeconfig file
  view              显示合并的 kubeconfig 配置或一个指定的 kubeconfig 文件

Usage:
  kubectl config SUBCOMMAND [options]

# 集群相关
  delete-cluster
  set-cluster
  get-clusters
  
# 用户相关
  set-credentials
  get-users
  delete-user
  
# 上下文相关
  delete-context
  get-contexts
  set-context
  rename-context
  
# current-context相关子命令
  user-context
  current-context

# 查看
  view
  
#结果显示：对于一个用户账号，至少包含三部分：
1.用户条目-credentials 设定具体的user account名称
2.集群-cluster 设定该user account所工作的区域
3.上下文环境-context 设定用户和集群的关系
```



**创建和使用kubeconfig流程**

```bash
# 1) 在kubeconfig中添加集群信息
# 需指定3个重要信息
# 1. Kubernetes集群的CA证书信息
# 2. apiServer的IP地址
# 3. 指定生成的config文件所在路径
[root@node1 ~]# kubectl config set-cluster mykube --embed-certs=true --certificate-authority=/etc/kubernetes/pki/ca.crt --server="https://10.0.0.201:6443" --kubeconfig=$HOME/.kube/mykube.conf
Cluster "mykube" set.

# 查看文件
[root@node1 ~]#ls .kube/
cache  mykube.conf

[root@node1 ~]#cat .kube/mykube.conf 
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURCVENDQWUyZ0F3SUJBZ0lJRmQ2UW5LYmkzK2t3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TlRBeE1EUXdNVE01TURaYUZ3MHpOVEF4TURJd01UUTBNRFphTUJVeApFekFSQmdOVkJBTVRDbXQxWW1WeWJtVjBaWE13Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLCkFvSUJBUURObjZibnVuWVZkV1kvQ1JPczVIaGE0TE8zYk81dEtZRlNOMnNYQ2pERXYyM0VWRTVDTE9qMmJlblkKRUt4YUcrdHR2UFJqWWpQUkZCWldjOFFJcmdQc2gzWHI4YzRHNFVMU1grdkJhdEdhVFhpSU9DQXNSRUxRcUExcgpXajkvZ0hrZlRvQlRCY2J5M0xEbms5RFJ3SXR4SXJYSTFxUUJLL2VLRmNFOVlBaG93YkpBK2I3TTJ3SHlPdFg2CmVnV09WVWRDQjRzN05qZHAvYytDamJXeStUYTBmbDQ4RVM4VHFFY3kxUXMvYXMybjAxOFdJei80TExDazFYSmwKTFdDRlJrOE5BOTVIcVZQbkRmVWVLK3RaSXpBS0dFbVpuM290RXNPdHgzanJBV2ZxbjV5UzVDVEZFZlRBU2FpWApFL3k4eFZrSzREQi8xNlFGSXM1cVBVSzVSMkhYQWdNQkFBR2pXVEJYTUE0R0ExVWREd0VCL3dRRUF3SUNwREFQCkJnTlZIUk1CQWY4RUJUQURBUUgvTUIwR0ExVWREZ1FXQkJUV3ErNlE4TndTcjJCV3lvMUZxZnNaMWFoTWV6QVYKQmdOVkhSRUVEakFNZ2dwcmRXSmxjbTVsZEdWek1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQzRLOHRLaktMQQpUMWJaV1NHTmlGZStEVGRKZEx0NlEyRkdaTUdCT3Yyc04ybXhJZDJzMW1rSHFCbEJzQ1JEcDdpRXdwVE1EcWtjCjlJdWEzcG1hdDAxMWJZMVZmNUF6aktiVVYzYlplSXJUWWkrSEtZWThCWnZ2WTVUcDJOdTBOUjk5NkJjSE5zRWsKdlhCSS9JcmlOd0swUHZqRTNVeGFlMUx4T2MvcjdyZWI5bVZQSTlXYWorVDY3KzZZS3BhTHBYWXQ0dGFMWDFBOQpiU1lGekdFVzZqRFpJSG9hSDFxTDNXcGRud2VMcThldjRCV0dmdURHNUltY0tibHUrT3crNjRUZ05taC9oNk9CClVFa0FDQThqQVR4R2g4eEtQZFBtRHFNbEdET0kvOXVkc2U2b1E2QW40c1k2RldTb2NUYjEyWU1TUDVjbkhVa0sKTERhR0tWRUhmUFllCi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K
    server: https://10.0.0.201:6443         # apiServer地址
  name: mykube
contexts: null
current-context: ""
kind: Config
preferences: {}
users: null

# 2) 在kubeconfig中添加用户凭证
# 方式1：X509数字证书认证
[root@node1 ~]# kubectl config set-credentials wang --embed-certs=true --client-certificate=pki/wang.crt --client-key=pki/wang.key --kubeconfig=$HOME/.kube/mykube.conf
User "wang" set.

# 查看
[root@node1 ~]#cat .kube/mykube.conf 
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURCVENDQWUyZ0F3SUJBZ0lJRmQ2UW5LYmkzK2t3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TlRBeE1EUXdNVE01TURaYUZ3MHpOVEF4TURJd01UUTBNRFphTUJVeApFekFSQmdOVkJBTVRDbXQxWW1WeWJtVjBaWE13Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLCkFvSUJBUURObjZibnVuWVZkV1kvQ1JPczVIaGE0TE8zYk81dEtZRlNOMnNYQ2pERXYyM0VWRTVDTE9qMmJlblkKRUt4YUcrdHR2UFJqWWpQUkZCWldjOFFJcmdQc2gzWHI4YzRHNFVMU1grdkJhdEdhVFhpSU9DQXNSRUxRcUExcgpXajkvZ0hrZlRvQlRCY2J5M0xEbms5RFJ3SXR4SXJYSTFxUUJLL2VLRmNFOVlBaG93YkpBK2I3TTJ3SHlPdFg2CmVnV09WVWRDQjRzN05qZHAvYytDamJXeStUYTBmbDQ4RVM4VHFFY3kxUXMvYXMybjAxOFdJei80TExDazFYSmwKTFdDRlJrOE5BOTVIcVZQbkRmVWVLK3RaSXpBS0dFbVpuM290RXNPdHgzanJBV2ZxbjV5UzVDVEZFZlRBU2FpWApFL3k4eFZrSzREQi8xNlFGSXM1cVBVSzVSMkhYQWdNQkFBR2pXVEJYTUE0R0ExVWREd0VCL3dRRUF3SUNwREFQCkJnTlZIUk1CQWY4RUJUQURBUUgvTUIwR0ExVWREZ1FXQkJUV3ErNlE4TndTcjJCV3lvMUZxZnNaMWFoTWV6QVYKQmdOVkhSRUVEakFNZ2dwcmRXSmxjbTVsZEdWek1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQzRLOHRLaktMQQpUMWJaV1NHTmlGZStEVGRKZEx0NlEyRkdaTUdCT3Yyc04ybXhJZDJzMW1rSHFCbEJzQ1JEcDdpRXdwVE1EcWtjCjlJdWEzcG1hdDAxMWJZMVZmNUF6aktiVVYzYlplSXJUWWkrSEtZWThCWnZ2WTVUcDJOdTBOUjk5NkJjSE5zRWsKdlhCSS9JcmlOd0swUHZqRTNVeGFlMUx4T2MvcjdyZWI5bVZQSTlXYWorVDY3KzZZS3BhTHBYWXQ0dGFMWDFBOQpiU1lGekdFVzZqRFpJSG9hSDFxTDNXcGRud2VMcThldjRCV0dmdURHNUltY0tibHUrT3crNjRUZ05taC9oNk9CClVFa0FDQThqQVR4R2g4eEtQZFBtRHFNbEdET0kvOXVkc2U2b1E2QW40c1k2RldTb2NUYjEyWU1TUDVjbkhVa0sKTERhR0tWRUhmUFllCi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K
    server: https://10.0.0.201:6443
  name: mykube
contexts: null
current-context: ""
kind: Config
preferences: {}
users:
- name: wang
  user:
    client-certificate-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUR6RENDQXJRQ0ZGY3lqanV6VXpFUmVXcVV4MkNmVkpYcDJSTFhNQTBHQ1NxR1NJYjNEUUVCQ3dVQU1CVXgKRXpBUkJnTlZCQU1UQ210MVltVnlibVYwWlhNd0hoY05NalV3TVRBM01UTXdNakU1V2hjTk16VXdNVEExTVRNdwpNakU1V2pBd01RMHdDd1lEVlFRRERBUjNZVzVuTVI4d0hRWURWUVFLREJacmRXSmxZV1J0T21Oc2RYTjBaWEl0CllXUnRhVzV6TUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUFyaDVoL1NOWDdSZHEKem04UzB1UUUwKzFRNkI3dklmQm5QK0xWbWkvS0crVHB5N0YwKzM1K2dsNy80NCsvc1RmcFR1SlNEYVh6VTVydwpOd3NyNlNqV2o3NVlYOCtBSVlja0VWVVNwS3hwUkJ0ZDJjbENUanF3bTVHZ21EUk1Ca1ptNzl1S1NmdmZKZnZqCjF5M3U1Q0lhTmNjZWJia29TdUZXeUtxWHQwcEM5WTFDTWhpV0FoNjFJRVU5UFZjSURqK0JoNjNSNS8yOXJSZHEKTk52ZlNuYUY0c2dVL09wRTZXd3lMdUQ4aVhLdFBMeUExa0tpbE5RaWlsS0NFbm13RmxLNVk5N3EwQU45RElRbgpmbStleGhDTnRwdHhvU3R6OXE1aHM2QWUvK041azBKZDQ1Q0dUZm5NbzMvYjE4SDdxSGlvaVlvUXNEaitlWkt3Ck9ua3A0YmVDZXAyZGZxNDlKcG1FOGprY0FUd2NtMFJoVFlUbG5IZ1crZWczSjV3SkRhT2RGRlVUQ29rOUhIS0kKMy9UMzVwdnZaNWRLcXJKYjJHajdFT210bUp5MGowQ2YvaVB1QkxBK0lwbm12NGg3TmFjaDAwb0p2LytBV3pUegpHOGRTcWhHMWR1ekFNOG9uZlBiU292Y0ZaYmZmSUhPSEpydlVxdkF1Y25aanNCQnFTbmt0d2U3L05hbWU0WDk5ClVZVU9TNVBHVGdBWG1WaUEyb1NpOWxaSnB4czVBZkhwUllKenpQRlFNZnFxS2o1VUhaV0ZzSW5JR25rTm5XcEkKNWtRcWZMUFNvSGVVQmp2TytqU3pLSnZyeTBJTGtyZmgzRHN0THlYV3kyK0pnaFQrUFprT0J5RnZma1VBVlpKRgpsUUtuN0czZlZXYmxDeUdOU0NjaHB0Z3FnNmxBVjBzQ0F3RUFBVEFOQmdrcWhraUc5dzBCQVFzRkFBT0NBUUVBCkpRdGRsblQvRm5PRklDeFY3NDFJNHRRT1dROEhWdVU4Y1F6eDV2b3FtZmU1OStZbUJxT2FPMjcxS0c2akVGMEsKTzM4RmNLVEltTGRhaHdXRkNWSkROV1B4cmFtM2FxUHoveXkxd0VXMkY1c0lSZ004VzAwc0tzTnNpMlR3MjJZawpiQ0NkUWYrZnhLTkh4TXJpS2FoYXYvNXFkWHA5elRkUFRLU1E2U0tTQm9Jd2NCYk1lTWZPWU1WZDdoSmJBdHFMCkh5ZmNOMkdHMW9LSjhMRDBrU1FHa1h2eEZQNFR6WThUenlEcnVFN0laMkJ3V0s1VFdlWXFXUTVXNjBNMnFMYncKLzlBMHJsMFhEM0hHZStpVkd3UWdYWXkxaWhhOUZaSUpTb3lVLzJhd2MvU3pENkFTWkFGNGpLOXZxa29iTHdjdgpQdTQzUmJicFl2WXJPNU9qakxWdm13PT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
    client-key-data: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUpRZ0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQ1N3d2dna29BZ0VBQW9JQ0FRQ3VIbUg5STFmdEYyck8KYnhMUzVBVFQ3VkRvSHU4aDhHYy80dFdhTDhvYjVPbkxzWFQ3Zm42Q1h2L2pqNyt4TitsTzRsSU5wZk5UbXZBMwpDeXZwS05hUHZsaGZ6NEFoaHlRUlZSS2tyR2xFRzEzWnlVSk9PckNia2FDWU5Fd0dSbWJ2MjRwSis5OGwrK1BYCkxlN2tJaG8xeHg1dHVTaEs0VmJJcXBlM1NrTDFqVUl5R0pZQ0hyVWdSVDA5VndnT1A0R0hyZEhuL2IydEYybzAKMjk5S2RvWGl5QlQ4NmtUcGJESXU0UHlKY3EwOHZJRFdRcUtVMUNLS1VvSVNlYkFXVXJsajN1clFBMzBNaENkKwpiNTdHRUkyMm0zR2hLM1Aycm1Hem9CNy80M21UUWwzamtJWk4rY3lqZjl2WHdmdW9lS2lKaWhDd09QNTVrckE2CmVTbmh0NEo2bloxK3JqMG1tWVR5T1J3QlBCeWJSR0ZOaE9XY2VCYjU2RGNubkFrTm81MFVWUk1LaVQwY2NvamYKOVBmbW0rOW5sMHFxc2x2WWFQc1E2YTJZbkxTUFFKLytJKzRFc0Q0aW1lYS9pSHMxcHlIVFNnbS8vNEJiTlBNYgp4MUtxRWJWMjdNQXp5aWQ4OXRLaTl3Vmx0OThnYzRjbXU5U3E4QzV5ZG1Pd0VHcEtlUzNCN3Y4MXFaN2hmMzFSCmhRNUxrOFpPQUJlWldJRGFoS0wyVmttbkd6a0I4ZWxGZ25QTThWQXgrcW9xUGxRZGxZV3dpY2dhZVEyZGFram0KUkNwOHM5S2dkNVFHTzg3Nk5MTW9tK3ZMUWd1U3QrSGNPeTB2SmRiTGI0bUNGUDQ5bVE0SElXOStSUUJWa2tXVgpBcWZzYmQ5Vlp1VUxJWTFJSnlHbTJDcURxVUJYU3dJREFRQUJBb0lDQUE1Qm9waE5hb2VaSVQraHpKTEQ1TGxOCmR4QnFaLzRKWndyT0VkczhDbnBhTmVKZHQweFlRUmQvbThnUUh3dnRuZ2E5ZFNaMDdnVnNiRHExaVhUZnlTR2YKM2pDS0Z0Mm42UVlhUnhxQW0yWGVMOE1EUFpDV01adXJRdER6aHo0RVNhMWQ5bWEwWHNNSGF0SlZpbmZYYXZuNApRYitPSjRScUN1Y0hRTURiTGJ4WlFwQkRmeFRSV3RjM2xCb1BwRE0yYys2ZUJzL044TmZaVVBMZkJkdGM5UDFxCmtIMWMyU09ibmtoRVY2a1JZS25XYlY0ZHVwNGcrR3NHOG10ODF6UWN0ZDA5aFZCZTJNQkxtY2c2YjIrY0wxNUMKUC8ySVIwaHRZc2FJVjhGdjZLWnNDcS8xUjJuZkNDaGk4YWNxMU9Zb2F2UkgvN0hPR05mdmNNcDQzVHNFQVlUUgovcjVGSDVMQ2xCNlJDK2VaU29GNURvYU5MY25xZGFkV3FTcW0rYml2ZS85WGszMHF0TERQL0o4WGQ2Y1BXQjZZCjVUd2JOWmVnOHlPb0t4a0d6NDJMYzJ1UlV2VlR3bXJOVEdtVlNnUkZEdE5BeWZlbGNkOEtLank4VVpOSTJ1cTcKK3ZoenJsbVBPRnlHU2RFSEFFajBrbXVXM2xpUGRTNXRBOEJPUVlCQVVuVWRiVUVaSjdsSFpGdDNwYURoYVJuQwp0V2hqU3ZmZ0diS0ZzeldmOXlhRzZFYVhFMEgzQUJaSTBxcWhyeVdmQlhMb1YzY0lYbHNsbzFhanhLcmhSK0JVCjVKbUlyQlhiczh6VEFxbFZ6V2daK1ExL1JoSnkrUy95amtuZkhmMFUyOC9ZNkxyN1RIS0MyQTlnTW5RcnlRRjYKVDY2SkROcVdST1BaYjhlaS9nRFJBb0lCQVFESDFObUxnczdUdXB6dkhvN3ZYdkRnb3JWcGJkZ2l6WWNrejN6Zwp4a0lqTUNERkpVdmE1dTZ3ZEJZL1RUNlpPUDlTSXRxWlBEMjhJYmhySStPZkxlQzVJT2owbXFtSGdRSW94b3pvCmVleVdSNVdYWlpyUHVieVlrbCt2Sk1jNTRNRUp4ZHdPeHR2TkIzMkkwMXlhOVh0RmNkeVFLMWhEdG5kb0pseG8KY2NOaGczcjVRTmxNY1UxY3RHK2NzL2RrQWlSQTZ4OXRkcGdzWWFrVVVLdjlPUTB4VFpDTVN0R3U3VlNobC9MWgorRTdSbnFVQ3RkWU05dzRTRzNVQ2FtazNobENmUXAwb2RQZGg1eUJ6K0w5elk5OFdDOUZrWjFZeEp6L1FqbXVjClhxTVZ5ZGFrTTdCSHJWUFA4K0xLTjlmb2NaU0FpamJ5bGUxZ3kxZlJta1RQM1RoUEFvSUJBUURmRDFYYUIxbEsKd2ZvMCtlS2tiRDFadWRlU29DdkFkWW80ZEswY0wzRVY2TUxycmNmdFVWWGxVUW9EOTZHcVpaZlZodjFtTzg2bQpuRUF5UTg1SG91aG1EZy9teU9DRUVFMWxiVmpPTkl0c2ZxQ1JGNVBOSTZCc0NXTHpKS1pVUGtKOGhBRzdQbWxkCm02UTA3Z2wwb2VVUlRDVmZ3dXZycFdkd09SREUvSUxPbzI4aXFxNGRsNUNOWVpvUE91bDJYK3U4V2RkOHhUZk0KVFFJWlZwMm1OMTU0VnlDR29HUmxIVytzQ1k5QXgzZzNIUTI3Yjgzc2kvRzMyeTVSVmduWjNWeXdmRHRQazdaUApiUkYzMWpiUlNwU20xb3R4anJYamJzOUliWGg5eUZZbm4vSU5rZC90SVg3Sml5QTQ3RXN1MUtXTVVwVXNuQ2VVCkUvMDlLS3NiNkxaRkFvSUJBR2FadWF5dzErTE1FT0dSVGhCSExlUVlobzZBTUpZRjh0cUtrZktTdU1oNllJajQKa2s3dGZTWXFKSFlTQWc4SHZjZjlUMEdZTlpaUHRmR0V0czAyOEFmOWhyNTRYb3pOUnorS1dqVE96Uk9INDUyZApOSFJ0U0JFS0xvaXRtSUQyRGdjbmlNb3BmaGR5UGhrdmRIKzNoTGh1TXJIdkgxMTg1U2diY2h6S05HZnY2d2JwCkxlamF6NzdHZ2Z2eVJ4WVpKMllSa3N4UU5PZXNxUFJlUzBBenQ3dFZ1TjdmVjNPNk5WYld2b0Q5eGZKSXd5NTIKRUZZTnp6S3EyRlFLTU1XcWQrQ2RnaldRZ0tmSzFOWFdwTzNwSEZTa2NybGJlVnk1YTBGNHJuWFYvV1FsZ3NoQwpKY05Ya2czV2lkNEwrQlpIb3Rpd25tL0ZYT0R5NXI4ZXR6QUd4RzhDZ2dFQUUvNFo0Y3JhMC9xQzVKQ3BJYmVaCjRCcnFHWGhGczZCVlhTNEgvZ2k2aUE0dXVsVC9JR1F6NExQY3cvSkVDVFBGNGh1UlJzS0JpU2xrRDUxSU5kK0MKR1BPVnRVZTM1OTVXTVlzVmRKWDlFU0pnWGVEUkhJZmU3eEFBVUc2dWdjcDZ4eEpGM1hTQW1TVkVHSUpsVXBEWQpLUzY4QXRORHRnRkRQaW0vT1FpdzZMaDVVNUFjdndaQXJJdGM5WlNBTEYzNGtRODBZemlDQWN1OUxtdzNBUmpoClhNUGlaRzZuMFBCTWZBejNUQVVVMzB1NVdWMXlCWXVkaEs4ZWZhZktoajV5K2xhSU1sKzQ3WEdIS1VpSDdVWlUKQUlnbVEyMVpIQ05vYk1OekUwTUxoYzJ1TWswcTF1UXpxdmpQVUlyTlNrdEE4MHpMbGc0QTlpSzhoZWpKUFYwawpTUUtDQVFFQWxuWlMzR2NrTTBjRlJibm9VUmp4M2VEUFhrZldEUis0c29FUk9OTndLRnVLaDRRU3M0SGVONTIwCjlBOXlxald5NTVRNUJSamhaNHprOWhMdEVPTERsL3BSQWUxbjNGNmtxZGJocG5XTk9iOWhFRnFRWGJZdmY4bk8KRzdWbkwra0FqUDhXbHAwMERudEtzT0VvVUpGYWRMK3AxdDIrSnlCOXlhUmJjRUFneWxIM1ZUN3hpdUg1NFUwMwpCZ1hqQ0ZhMll0Mjg0L0FkWkRGMWx3c1E3alpUSFAxa3pSbVphYmhKemZCa3ZYTGtVL0JRZ0Q4amtzTFVmN2tICmVYTDFMbVJGTUwxejgxYjRXZE42RXBEUXNFckNWdGYzdnByMGFaRzFlcmZ4U2E1VWs4b3lWYnlvL0sxTHIremIKaytOc2wyQ1dtOUd5UWtSd3BZd0VkNk13MFNDcXR3PT0KLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLQo=
    
# 查看证书
[root@node1 ~]#echo "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUR6RENDQXJRQ0ZGY3lqanV6VXpFUmVXcVV4MkNmVkpYcDJSTFhNQTBHQ1NxR1NJYjNEUUVCQ3dVQU1CVXgKRXpBUkJnTlZCQU1UQ210MVltVnlibVYwWlhNd0hoY05NalV3TVRBM01UTXdNakU1V2hjTk16VXdNVEExTVRNdwpNakU1V2pBd01RMHdDd1lEVlFRRERBUjNZVzVuTVI4d0hRWURWUVFLREJacmRXSmxZV1J0T21Oc2RYTjBaWEl0CllXUnRhVzV6TUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUFyaDVoL1NOWDdSZHEKem04UzB1UUUwKzFRNkI3dklmQm5QK0xWbWkvS0crVHB5N0YwKzM1K2dsNy80NCsvc1RmcFR1SlNEYVh6VTVydwpOd3NyNlNqV2o3NVlYOCtBSVlja0VWVVNwS3hwUkJ0ZDJjbENUanF3bTVHZ21EUk1Ca1ptNzl1S1NmdmZKZnZqCjF5M3U1Q0lhTmNjZWJia29TdUZXeUtxWHQwcEM5WTFDTWhpV0FoNjFJRVU5UFZjSURqK0JoNjNSNS8yOXJSZHEKTk52ZlNuYUY0c2dVL09wRTZXd3lMdUQ4aVhLdFBMeUExa0tpbE5RaWlsS0NFbm13RmxLNVk5N3EwQU45RElRbgpmbStleGhDTnRwdHhvU3R6OXE1aHM2QWUvK041azBKZDQ1Q0dUZm5NbzMvYjE4SDdxSGlvaVlvUXNEaitlWkt3Ck9ua3A0YmVDZXAyZGZxNDlKcG1FOGprY0FUd2NtMFJoVFlUbG5IZ1crZWczSjV3SkRhT2RGRlVUQ29rOUhIS0kKMy9UMzVwdnZaNWRLcXJKYjJHajdFT210bUp5MGowQ2YvaVB1QkxBK0lwbm12NGg3TmFjaDAwb0p2LytBV3pUegpHOGRTcWhHMWR1ekFNOG9uZlBiU292Y0ZaYmZmSUhPSEpydlVxdkF1Y25aanNCQnFTbmt0d2U3L05hbWU0WDk5ClVZVU9TNVBHVGdBWG1WaUEyb1NpOWxaSnB4czVBZkhwUllKenpQRlFNZnFxS2o1VUhaV0ZzSW5JR25rTm5XcEkKNWtRcWZMUFNvSGVVQmp2TytqU3pLSnZyeTBJTGtyZmgzRHN0THlYV3kyK0pnaFQrUFprT0J5RnZma1VBVlpKRgpsUUtuN0czZlZXYmxDeUdOU0NjaHB0Z3FnNmxBVjBzQ0F3RUFBVEFOQmdrcWhraUc5dzBCQVFzRkFBT0NBUUVBCkpRdGRsblQvRm5PRklDeFY3NDFJNHRRT1dROEhWdVU4Y1F6eDV2b3FtZmU1OStZbUJxT2FPMjcxS0c2akVGMEsKTzM4RmNLVEltTGRhaHdXRkNWSkROV1B4cmFtM2FxUHoveXkxd0VXMkY1c0lSZ004VzAwc0tzTnNpMlR3MjJZawpiQ0NkUWYrZnhLTkh4TXJpS2FoYXYvNXFkWHA5elRkUFRLU1E2U0tTQm9Jd2NCYk1lTWZPWU1WZDdoSmJBdHFMCkh5ZmNOMkdHMW9LSjhMRDBrU1FHa1h2eEZQNFR6WThUenlEcnVFN0laMkJ3V0s1VFdlWXFXUTVXNjBNMnFMYncKLzlBMHJsMFhEM0hHZStpVkd3UWdYWXkxaWhhOUZaSUpTb3lVLzJhd2MvU3pENkFTWkFGNGpLOXZxa29iTHdjdgpQdTQzUmJicFl2WXJPNU9qakxWdm13PT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=" |base64 -d|openssl x509 -noout -text
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number:
            57:32:8e:3b:b3:53:31:11:79:6a:94:c7:60:9f:54:95:e9:d9:12:d7
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = kubernetes
        Validity
            Not Before: Jan  7 13:02:19 2025 GMT
            Not After : Jan  5 13:02:19 2035 GMT
        Subject: CN = wang, O = kubeadm:cluster-admins    # 管理员组
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (4096 bit)
                Modulus:
                ......
                
# 方法2：静态令牌认证
kubectl config set-credentials wang --token="xxxxxxx" -- kubeconfig=$HOME/.kube/mykube.conf

# 3) 在kubeconfig中添加context,实现集群和用户关联
[root@node1 ~]# kubectl config set-context wang@mykube --cluster=mykube --user=wang --kubeconfig=$HOME/.kube/mykube.conf
Context "wang@mykube" created.

# 使用指定的context访问集群
[root@node1 ~]#kubectl get ns --context="wang@mykube"  --kubeconfig=.kube/mykube.conf
NAME              STATUS   AGE
default           Active   4d2h
ingress-nginx     Active   4d
kube-flannel      Active   4d2h
kube-node-lease   Active   4d2h
kube-public       Active   4d2h
kube-system       Active   4d2h
metallb-system    Active   4d

# 设置默认context
[root@node1 ~]#kubectl config use-context wang@mykube --kubeconfig=.kube/mykube.conf
Switched to context "wang@mykube".

# 查看
[root@node1 ~]#kubectl get nodes --kubeconfig=.kube/mykube.conf
NAME      STATUS   ROLES           AGE    VERSION
master1   Ready    control-plane   4d2h   v1.30.8
node1     Ready    <none>          4d2h   v1.30.8
node2     Ready    <none>          4d2h   v1.30.8
node3     Ready    <none>          4d2h   v1.30.8

# 查看kubeconfig内容
[root@node1 ~]#kubectl config view --kubeconfig=.kube/mykube.conf --raw


# 使用kubeconfig总结
1)kubectl get pods --kubeconfig=$HOME/.kube/mykube.conf
2)export KUBECONFIG="$HOME/.kube/mykube.conf"; kubectl get pods 
3)kubectl get pods 
```



**查看默认的kubeconfig配置内容**

```bash
# 查看默认的配置文件内容
[root@master1 ~]# kubectl config view
apiVersion: v1
clusters:                                                  # 集群列表
- cluster:
    certificate-authority-data: DATA+OMITTED               # 证书认证方式
    server: https://master1.mystical.org:6443              # api_server的地址
  name: kubernetes                                         # 当前集群名称
contexts:                                                  # 上下文列表，一般指的是多集群间用户的切换所需的环境属性
- context:
    cluster: kubernetes                                    # 集群名称：kubernetes
    user: kubernetes-admin                                 # 使用kubernetes-admin用户来访问集群kubernetes
  name: kubernetes-admin@kubernetes                        # 该context的名称标准写法
current-context: kubernetes-admin@kubernetes               # 当前正在使用的上下文的名称
kind: Config
preferences: {}
users:                                                     # 用户列表
- name: kubernetes-admin                                   # 用户名称
  user:                                                    # 用户自己认证属性
    client-certificate-data: DATA+OMITTED                  # 客户端证书
    client-key-data: DATA+OMITTED                          # 客户端私钥

# 结果总结
# 一个config主要包含了三部分内容：users、clusters、contexts，每个部分都有两部分组成：
# name和user|cluster|context
# 对于cluster，对外的地址-server 和 基本的认证方式-certificate-authority-data
# 对于context，连接到的集群-cluster 和 连接集群的用户-user
# 对于user，连接集群的认证方式-client-certificate-data 和 私钥信息-client-key-data
# current-context表明我们是处于哪一个环境中。
```



##### 合并多个kubeconfig文件

客户端能够通过多种途径获取到kubeconfig文件时，将遵循如下优先级顺序进行文件合并

- 设置了**--kubeconfig参数**时，则仅使用指定的文件，且不进行合并；该参数只能使用一次，即**不支持多个文件合并**
- 若设置了**KUBECONFIG环境变量**，则**可以指定用冒号分隔的多个文件**，**进行合并处理规则**
  - 忽略不存在的文件
  - 遇到内容无法反序列化的文件时，将生成错误信息
  - 文件列表中，第一个设定了特定值或映射键(map key)的文件是为生效文件，即**第一个文件优先生效**
    - 修改某个映射键的值时，将修改列表中第一个出现该键的文件中的内容
    - 创建一个键时，其将保存于列表中的第一个文件中
    - 若列表中指定的文件均不存在时，则自动创建列表中的最后一个文件
- 将使用默认的${HOME}/**.kube/config**，且**不进行合并**

```ABAP
以上说明: 只有KUBECONFIG变量一种方式才支持合并多个kubeconfig文件
```



**利用KUBECONFIG变量合并多个文件**

```bash
# 设置环境变量
[root@node1 ~]#export KUBECONFIG="/root/.kube/config:/root/.kube/mykube.conf"

# 查看
[root@node1 ~]#kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://master1.mystical.org:6443
  name: kubernetes
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://10.0.0.201:6443
  name: mykube
contexts:
- context:
    cluster: kubernetes
    user: kubernetes-admin
  name: kubernetes-admin@kubernetes
- context:
    cluster: mykube
    user: wang
  name: wang@mykube
current-context: kubernetes-admin@kubernetes           # 默认左边的文件生效
kind: Config
preferences: {}
users:
- name: kubernetes-admin
  user:
    client-certificate-data: DATA+OMITTED
    client-key-data: DATA+OMITTED
- name: wang
  user:
    client-certificate-data: DATA+OMITTED
    client-key-data: DATA+OMITTED
    
    
#使用当前context身份kubernetes-admin@kubernetes访问
[root@node1 ~]# kubectl get nodes
NAME      STATUS   ROLES           AGE    VERSION
master1   Ready    control-plane   4d4h   v1.30.8
node1     Ready    <none>          4d4h   v1.30.8
node2     Ready    <none>          4d4h   v1.30.8
node3     Ready    <none>          4d4h   v1.30.8
```



#### User Account 综合案例



##### UA创建流程

以基于X509的客户端为例,用户认证的创建流程

**创建证书**

- 创建私钥文件
  - 对于用户名和用户组需要提前规划好，如果用户多权限集中的情况下，一定要规划好用户组信息
- 基于私钥文件创建证书签名请求
  - 要基于我们自建的私钥来创建签证请求文件
- 基于私钥和签名请求生成证书文件
  - 因为生成的证书要应用在kubernetes环境中，所以必须由kubernetes的全局证书来认证



**创建user**

- 基于证书文件在k8s上创建用户 credentials

  ```bash
  kubectl config set-credentials wang --embed-certs=true --client-certificate=pki/wang.crt --client-key=pki/wang.key --kubeconfig=$HOME/.kube/mykube.conf
  ```



**创建Cluster**

- 创建工作区域-cluster

  - 所谓的工作区域是用户的工作场景，必须定制好，一个cluster可以被多个用户使用

  ```bash
  kubectl config set-cluster mykube --embed-certs=true --certificate-authority=/etc/kubernetes/pki/ca.crt --server="https://10.0.0.201:6443" --kubeconfig=$HOME/.kube/mykube.conf
  ```

  

**关联 user 和 cluster**

- 将cluster和user关联起来-context

- 关联的作用就是，将用户和区域整合在一起，使用资源的时候便于调用

  ```bash
  kubectl config set-context wang@mykube --cluster=mykube --user=wang --kubeconfig=$HOME/.kube/mykube.conf
  ```

  

**验证用户**

- 因为前面只做了认证，而用户的操作涉及到资源权限，这部分是需要结合授权机制才能进行
- 默认情况下，如果另外的没有授权, 基于创建好的文件来获取资源是被forbidden的





#####  创建私钥文件

```bash
# 给用户feng创建一个私钥，命名成：feng.key（无加密）
[root@master1 ~]# (umask 077; openssl genrsa -out pki/feng.key 2048)

#命令解析：
#    genrsa 该子命令用于生成RSA私钥，不会生成公钥，因为公钥提取自私钥
#    -out filename 生成的私钥保存至filename文件，若未指定输出文件，则为标准输出
#    -numbits 指定私钥的长度，默认1024，该项必须为命令行的最后一项参数

# 查看
[root@master1 ~]# ls pki/
admin.crt  feng.key      mystical.key                             test2.csr  wang.csr
admin.csr  mystical.crt  security-certificaterequests-test2.yaml  test2.key  wang.key
admin.key  mystical.csr  test2.crt 
```



#####  签名请求

```bash
# 用刚创建的私钥创建一个证书签名请求文件：feng.csr
[root@master1 ~]#openssl req -new -key pki/feng.key -out feng.csr -subj "/CN=feng/O=kubeadm:cluster-admins"

#参数说明：
    -new 生成证书请求文件
    -key   指定已有的秘钥文件生成签名请求，必须与-new配合使用
    -out 输出证书文件名称
    -subj 输入证书拥有者信息，这里指定 CN 以及 O 的值，/表示内容分隔
           CN以及O的值对于kubernetes很重要，因为kubernetes会从证书这两个值对应获取相关信息：
       "CN"：Common Name，用于从证书中提取该字段作为请求的用户名 (User Name)；浏览器使用该字段验证网站是否合法；
       "O"： Organization，用于分组认证
# 注意： 用户是feng,组是kubeadm:cluster-admins

# 查看
[root@master1 ~]#ls pki/
admin.crt  feng.csr      mystical.csr                             test2.crt  wang.crt
admin.csr  feng.key      mystical.key                             test2.csr  wang.csr
admin.key  mystical.crt  security-certificaterequests-test2.yaml  test2.key  wang.key
#结果显示：*.key 是私钥，*.csr是签名请求文件
```



##### **生成证书**

刚才的私钥和认证并没有被Kubernetes集群纳入到管理体系，需要基于kubeadm集群的CA相关证书来 进行认证

CA相关文件位于/etc/kubernetes/pki/目录下面，利用该目录下面的ca.crt和ca.key两个文件来批准上面 的证书请求

```bash
[root@master1 ~]# cd /etc/kubernetes/pki
[root@master1 pki]#openssl x509 -req -CA ./ca.crt -CAkey ./ca.key -CAcreateserial -in /root/pki/feng.csr -out /root/pki/feng.crt  -days 365 
Certificate request self-signature ok
subject=CN = feng, O = kubeadm:cluster-admins


#参数说明：
    -req                 产生证书签发申请命令
    -in                  指定需要签名的请求文件
    -CA                  指定CA证书文件
    -CAkey               指定CA证书的秘钥文件
    -CAcreateserial      生成唯一的证书序列号
    -x509                表示输出一个X509格式的证书
    -days                指定证书过期时间为365天
    -out                 输出证书文件
    
# 检查文件效果[root@master1 pki]# ls /root/pki/
admin.crt  feng.csr      mystical.key                             test2.key
admin.csr  feng.key      security-certificaterequests-test2.yaml  wang.crt
admin.key  mystical.crt  test2.crt                                wang.csr
feng.crt   mystical.csr  test2.csr                                wang.key
#结果显示：*.crt就是最终生成的签证证书

# 查看证书信息
[root@master1 pki]#openssl x509 -in /root/pki/feng.crt -noout -text
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number:
            08:b6:f7:4d:94:a6:7f:15:ed:18:36:29:c0:4b:1a:d0:85:1c:de:f9
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = kubernetes
        Validity
            Not Before: Jan  8 06:38:55 2025 GMT
            Not After : Jan  8 06:38:55 2026 GMT
        Subject: CN = feng, O = kubeadm:cluster-admins
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                ......
#结果显示：Issuer: 表示是哪个CA机构帮我们认证的,我们关注的重点在于Subject内容中的请求用户所属的组信息
```



##### 创建Kubernetes用户

```bash
#创建用户信息
[root@master1 pki]# kubectl config set-credentials feng --client-certificate=/root/pki/feng.crt --client-key=/root/pki/feng.key --embed-certs=true --kubeconfig=/tmp/feng.conf
User "feng" set.

#参数详解：
set-credentials                          #子命令的作用就是给kubeconfig认证文件创建一个用户条目
--client-certificate=path/to/certfile    #指定用户的签证证书文件
--client-key=path/to/keyfile             #指定用户的私钥文件
--embed-certs=true                       #在kubeconfig中为用户条目嵌入客户端证书/密钥，默认值是false
--kubeconfig=/path/other_config.file     #表示将属性信息单独输出到一个文件，如不指定，默认存放在 ~/.kube/config文件中

# 查看生成文件
[root@master1 pki]#cat /tmp/feng.conf
apiVersion: v1
clusters: null
contexts: null
current-context: ""
kind: Config
preferences: {}
users:
- name: feng
  user:
......

# 查看效果
kubect
[root@master1 pki]# kubectl config view --kubeconfig=/tmp/feng.conf 
apiVersion: v1
clusters: null
contexts: null
current-context: ""
kind: Config
preferences: {}
users:
- name: feng
  user:
    client-certificate-data: DATA+OMITTED
    client-key-data: DATA+OMITTED
```



##### 创建集群

```bash
#创建一个新的集群mycluster
[root@master1 pki]# kubectl config set-cluster fengcluster --server="https://10.0.0.201:6443" --certificate-authority=./ca.crt --embed-certs=true --kubeconfig=/tmp/feng.conf 
Cluster "fengcluster" set.

#参数详解：
--server=cluster_api_server
--certificate-authority=path/to/certificate/authority
--embed-certs=true  #默认为false,会将证书文件路径存入kubeconfig文件中,true时会将证书内容存入kubdconfig文件中
#注意：这里使用到的证书必须是kubernetes的ca证书

# 检查效果
[root@master1 pki]#kubectl config view --kubeconfig=/tmp/feng.conf
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://10.0.0.201:6443
  name: fengcluster
contexts: null
current-context: ""
kind: Config
preferences: {}
users:
- name: feng
  user:
    client-certificate-data: DATA+OMITTED
    client-key-data: DATA+OMITTED
```



##### 关联用户和集群

所谓关联实际上就是设置用户能在哪个集群的使用

```bash
#配置上下文信息
[root@master1 pki]#kubectl config set-context feng@fengcluster --cluster=fengcluster --user=feng --kubeconfig=/tmp/feng.conf 
Context "feng@fengcluster" created.

#属性详解
--cluster=cluster_nickname     # 关联的集群名称
--user=user_nickname           # 关联的用户名称
--namespace=namespace          # 可以设置该生效的命名空间

#最终效果
[root@master1 pki]#kubectl config view --kubeconfig=/tmp/feng.conf
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://10.0.0.201:6443
  name: fengcluster
contexts:
- context:
    cluster: fengcluster
    user: feng
  name: feng@fengcluster
current-context: ""
kind: Config
preferences: {}
users:
- name: feng
  user:
    client-certificate-data: DATA+OMITTED
    client-key-data: DATA+OMITTED
```



##### 验证效果

```bash
#根据刚才的信息显示，current-context的信息是空，那么切换上下文
#更改上下文
[root@master1 pki]# kubectl config use-context feng@fengcluster --kubeconfig=/tmp/feng.conf 
Switched to context "feng@fengcluster".

# 验证访问
[root@master1 pki]#kubectl get nodes --kubeconfig=/tmp/feng.conf 
NAME      STATUS   ROLES           AGE    VERSION
master1   Ready    control-plane   4d5h   v1.30.8
node1     Ready    <none>          4d5h   v1.30.8
node2     Ready    <none>          4d5h   v1.30.8
node3     Ready    <none>          4d5h   v1.30.8
```





#### Service Account 管理

#####  Service Account 基础

**Service Account 功能**

- Kubernetes原生（kubernetes-native）应用托管运行于Kubernetes之上，通常需要直接与API  Server进行交互以获取必要的信息
- API Server同样需要对这类来自于Pod资源中客户端程序进行身份验证，Service Account也就是设计专用于这类场景的账号
- ServiceAccount是API Server支持的标准资源类型之一





**ServiceAccont：标准的API资源类型**

- 基于资源对象保存ServiceAccount的数据
- 认证信息保存于ServiceAccount对象专用的Secret中
- 隶属名称空间级别，专供集群上的Pod中的进程访问API Server时使用
- 需要用到特殊权限时，可为Pod指定要使用的自定义ServiceAccount资源对象





**在Pod上使用Service Account**

- 自动设定：Service Account通常由API Server自动创建并通过 ServiceAccount准入控制器自动关 联到集群中创建的每个Pod上

  - K8S自动为每个Pod注入一个 ServiceAccount 及配套的令牌

  ```bash
  # 默认叫default，每个名称空间都有一个名为default的sa，该sa权限很小
  [root@master1 pki]#kubectl get sa -A |grep default
  default           default                                       0         4d5h
  ingress-nginx     default                                       0         4d3h
  kube-flannel      default                                       0         4d5h
  kube-node-lease   default                                       0         4d5h
  kube-public       default                                       0         4d5h
  kube-system       default                                       0         4d5h
  metallb-system    default                                       0         4d3h
  ```

- 自定义：在Pod规范上，使用serviceAccountName指定要使用的特定ServiceAccount

- Pod中的字段imagePullSecrets，可为Pod提供从私有image registry获取时使用的认证凭据

  ```bash
  imagePullSecrets:
        - name: harbor-docker-registry-secret  # 指定docker-registry类型的secret，如果有多个会逐个验证
  ```

  



**为Pod提供向私有image registry提供认证凭据的方法**

- pods.spec.imagePullSecrets: 直接调用的方式

- pods.spec.serviceAccountName指定使用的特有ServiceAccount，而后在ServiceAccount资源对象上，使用serviceaccounts.imagePullSecrets 指定 secret ,此为间接调用的方式

  ```ABAP
  pod使用ServiceAccount，该SA上设置imagePullSecrets，从而实现Pod能够从私有仓拉镜像的权限
  ```



**Kubernetes基于三个组件完成Pod上service account的自动化**

- ServiceAccount Admission Controller
- Token Controller
- ServiceAccount Controller



在每个名称空间中，会自动生成(由ServiceAccount准入控制器负责)一个名称为default的 ServiceAccount，并默认将其自动分配给该空间下的每个Pod共享使用。

```bash
[root@master1 pki]#kubectl get sa -A |grep default
default           default                                       0         4d5h
ingress-nginx     default                                       0         4d3h
kube-flannel      default                                       0         4d5h
kube-node-lease   default                                       0         4d5h
kube-public       default                                       0         4d5h
kube-system       default                                       0         4d5h
metallb-system    default                                       0         4d3h
```

认证令牌保存于该名称空间下的一个Secret对象中，该对象中共有三个信息：namespace、ca.crt、 token



**SA 就是集群内部资源操作的账号**

- 每个命名空间自动生成一个名称为default的sa用户
- 每个命名空间可以有很多sa
- sa内部是secrets类型的token



**ServiceAccount使用专用的Secret类型存储相关的敏感信息**

- 类型标识为“kubernetes.io/serviceaccount”
- data 字段有三个固定的属性字段，名称分别为
  - ca.crt：Kubernetes CA的数字证书
  - namespace：该ServiceAccount可适用的名称空间
  - token：认证到API Server的令牌



**Pod用sa上附加的认证凭据：**

- **Secret卷**：Kubernetes-v1.23版本之前,被挂载至一个固定路径`/var/run/secrets/kubernetes.io/serviceaccount`

  - 在该路径下将会存在三个文件
    - ca.crt：kubernetes root ca的证书
    - namesapce：生效的名称空间
    - token：认证令牌

- **Projected卷**：Kubernetes-v1.24版本以后, 同样映射到固定路径`/var/run/secrets/kubernetes.io/serviceaccount/`

  - serviceAccountToken：用于ServiceAccount的Token信息提供给Pod，同样为token文件
  - configMap/kube-root-ca.crt：将kubernetes root ca自身的证书提供给Pod，同样为ca.crt
  - downwardAPI: metadata.namespace，用于限制该SA可生效的名称空间，同样为 namespace文件

  ```bash
  [root@master1 yaml]#kubectl exec -it myapp-7b94444f8d-hws2b -- /bin/sh
  / # cd /var/run/secrets/kubernetes.io/serviceaccount/
  /var/run/secrets/kubernetes.io/serviceaccount # ls
  ca.crt     namespace  token
  /var/run/secrets/kubernetes.io/serviceaccount # ls -l
  total 0
  lrwxrwxrwx    1 root     root            13 Jan  8 16:11 ca.crt -> ..data/ca.crt
  lrwxrwxrwx    1 root     root            16 Jan  8 16:11 namespace -> ..data/namespace
  lrwxrwxrwx    1 root     root            12 Jan  8 16:11 token -> ..data/token
  /var/run/secrets/kubernetes.io/serviceaccount # ls -la
  total 4
  drwxrwxrwt    3 root     root           140 Jan  8 16:11 .
  drwxr-xr-x    3 root     root          4096 Jan  8 16:11 ..
  drwxr-xr-x    2 root     root           100 Jan  8 16:11 ..2025_01_08_08_11_17.4084613224
  lrwxrwxrwx    1 root     root            32 Jan  8 16:11 ..data -> ..2025_01_08_08_11_17.4084613224
  lrwxrwxrwx    1 root     root            13 Jan  8 16:11 ca.crt -> ..data/ca.crt
  lrwxrwxrwx    1 root     root            16 Jan  8 16:11 namespace -> ..data/namespace
  lrwxrwxrwx    1 root     root            12 Jan  8 16:11 token -> ..data/token
  ```

  

**ServiceAccount Admission Controller负责完成Pod上的ServiceAccount的自动化**

- 为每个名称空间生成一个默认的default **ServiceAccount及其**依赖到的**Secret对象**
- 为未定义serviceAccountName的Pod资源自动附加名称空间下的serviceaccounts/default
- 为定义了serviceAccountName的Pod资源检查其引用的目标对象是否存在



每个serviceaccount，被API Server认证为**`“system:serviceaccount:NAMESPACE:SA”`**

ServiceAccount用到的token，也可以为被创建为kubeconfig文件，从而被kubectl等其它客户端引用；

```BASH
kubectl config set-cluster myk8s --server=https://kubernetes.default -certificate-authority=ca.crt
kubectl config set-credentials user --token={serviceaccount_token}
kubectl config set-context user@myk8s --cluster=myk8s
kubectl config set-context user@myk8s --user=user
kubectl config use-context user@myk8s
```





**默认认证示例**

```bash
#在k8s环境中创建任意一个pod的时候，它都会自动创建一个属性信息：
# 新版情况
[root@master1 yaml]#kubectl get pod myapp-7b94444f8d-hws2b -o yaml
...
 volumes:
  - name: kube-api-access-6ffvs
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
...

# 默认的sa:default权限很小
# 验证default权限
[root@master1 yaml]#kubectl cp myapp-7b94444f8d-hws2b:var/run/secrets/kubernetes.io/serviceaccount/..data/token token

# 查看token文件
[root@master1 yaml]#cat token 
eyJhbGciOiJSUzI1NiIsImtpZCI6IjVyZ2VtUUFRUk0zdnhNVUpRRHlqcUxCUGRVOGhqbFRTMDlCdEZTNmpSbE0ifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzY3ODU5ODc1LCJpYXQiOjE3MzYzMjM4NzUsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiMTlhMzMzZjQtZWJjMi00MDYxLWFkNTYtZGZjZWFiZmY2ZmNmIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwibm9kZSI6eyJuYW1lIjoibm9kZTEiLCJ1aWQiOiJmN2NkYjk5Yy1iYjQ5LTQ0N2MtOTQ4MS1jMzZjMTNhNWU3NTMifSwicG9kIjp7Im5hbWUiOiJteWFwcC03Yjk0NDQ0ZjhkLWh3czJiIiwidWlkIjoiZGEyYTk1MTctZTM1Mi00N2RlLWJiMDEtOGU1NDUwYmUzOTkxIn0sInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJkZWZhdWx0IiwidWlkIjoiMDIyNjYxODItNzRlYS00NWRjLWIwZDctNmY3NDQ5ZjlhZTExIn0sIndhcm5hZnRlciI6MTczNjMyNzQ4Mn0sIm5iZiI6MTczNjMyMzg3NSwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6ZGVmYXVsdCJ9.HERqhyZGaNj5juZWrfCJBJvoAGRfiHyzjqKyv8lNpwoBhH86ujnD4ql_f4thXY2lsM_1YCLrjtGssFLD7blaO4Ln91ekJLm-uMOvFZQKjCXwMxuLNNviC-OzqHrSmzoXyEqCaNGa5yJkjmpxbdXOk_zn0nu_HSkqk_qaegxYt9sDW_alQcWIsBtec2oN4CSnwUDTt_X7QvWceib5_2oKIgZlZXDpFViT9K2KtT3SxWUUFeFXGCLd7CaEGVckO1GhDI35oUobLZ2RjWrtoBsHYRzLa-zQhI43t9zpu7I1ss0bylFFOTdQkf7RtJzitpC1LKN70qYOf4GIlF4i2fqOIA

# 将这个token解码
# SA 的 Token 是 JWT 格式，并非简单的 Base64 编码数据，因此直接用 Base64 解码可能失败。
# JWT 的格式：{Header}.{Payload}.{Signature}

# 解密方法如下
[root@master1 yaml]#cat token |cut -d '.' -f1 | base64 -d |jq
{
  "alg": "RS256",
  "kid": "5rgemQAQRM3vxMUJQDyjqLBPdU8hjlTS09BtFS6jRlM"
}

[root@master1 yaml]#cat token |cut -d '.' -f2 | base64 -d |jq
{
  "aud": [
    "https://kubernetes.default.svc.cluster.local"
  ],
  "exp": 1767859875,
  "iat": 1736323875,
  "iss": "https://kubernetes.default.svc.cluster.local",
  "jti": "19a333f4-ebc2-4061-ad56-dfceabff6fcf",
  "kubernetes.io": {
    "namespace": "default",
    "node": {
      "name": "node1",
      "uid": "f7cdb99c-bb49-447c-9481-c36c13a5e753"
    },
    "pod": {
      "name": "myapp-7b94444f8d-hws2b",
      "uid": "da2a9517-e352-47de-bb01-8e5450be3991"
    },
    "serviceaccount": {
      "name": "default",
      "uid": "02266182-74ea-45dc-b0d7-6f7449f9ae11"
    },
    "warnafter": 1736327482
  },
  "nbf": 1736323875,
  "sub": "system:serviceaccount:default:default"
}

# 默认的default的Sa权限过小
[root@ubuntu2204 ~]#kubectl get pod --insecure-skip-tls-verify -s https://10.0.0.201:6443 --token `cat token`
Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:default" cannot list resource "pods" in API group "" in the namespace "default"
```



**sa资源属性**

```bash
apiVersion: v1                           # ServiceAccount所属的API群组及版本
kind: ServiceAccount                     # 资源类型标识
metadata:
  name <string>                          # 资源名称
  namespace <string>                     # ServiceAccount是名称空间级别的资源
automountServiceAccountToken <boolean>   # 是否让Pod自动挂载API令牌
secrets <[]Object>                       # 以该SA运行的Pod所要使用的Secret对象组成的列表
  apiVersion <string>                    # 引用的Secret对象所属的API群组及版本，可省略
  kind <string>                          # 引用的资源的类型，这里是指Secret，可省略
  name <string>                          # 引用的Secret对象的名称，通常仅给出该字段即可
  namespace <string>                     # 引用的Secret对象所属的名称空间
  uid <string>                           # 引用的Secret对象的标识符；
imagePullSecrets <[]Object>              # 引用的用于下载Pod中容器镜像的Secret对象列表
  name <string>                          # docker-registry类型的Secret资源的名称
```





#### 创建和使用SA账号

##### 创建方法

```bash
# 命令格式
[root@master1 yaml]# kubectl create serviceaccount NAME [--dry-run] [options]
#作用：创建一个"服务账号"

#参数详解
--dry-run=false                  # 模拟创建模式
--generator='serviceaccount/v1'  # 设定api版本信息
-o, --output=''                  # 设定输出信息格式，常见的有：json|yaml|name|template|...
--save-config=false              # 保存配置信息
--template=''                    # 设定配置模板文件

#文件格式:
apiVersion: v1
kind: ServiceAccount
metadata:
  name: <SA名称>

#创建SA资源文件的简单方法
[root@master1 yaml]# kubectl create serviceaccount mysa --dry-run -o yaml
apiVersion: v1
kind: ServiceAccount
metadata:
 name: mysa
```



**范例: 创建SA及其对应的Token**

```yaml
# 清单文件
[root@master1 sa] # cat security-sa-admin.yaml 
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin

---
# v1.24版之后添加下面内容手动创建secret
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: admin-secret
  annotations:
    kubernetes.io/service-account.name: "admin"

---
apiVersion: v1
kind: Pod
metadata:
  name: pod-sa-admin
spec:
  containers:
  - name: pod-sa-admin
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagePullPolicy: IfNotPresent
  serviceAccountName: admin
  
# 应用
[root@master1 sa] # kubectl apply -f security-sa-admin.yaml 
serviceaccount/admin created
secret/admin-secret created
pod/pod-sa-admin created

# 查看
[root@master1 sa] # kubectl describe sa admin 
Name:                admin
Namespace:           default
Labels:              <none>
Annotations:         <none>
Image pull secrets:  <none>
Mountable secrets:   <none>
Tokens:              admin-secret
Events:              <none>
```





### 授权机制

k8s集群默认的认证插件有 **Node** 和 **RBAC**，其他的都是使用大量的证书来进行的

如果没有鉴权方式允许,则默认为拒绝



**配置方法**

- 在kube-apiserver上使用 --authorization-mode 选项进行定义
- 多个模块彼此间以逗号分隔

```bash
[root@master1 sa]#cat /etc/kubernetes/manifests/kube-apiserver.yaml 
apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 10.0.0.201:6443
  creationTimestamp: null
  labels:
    component: kube-apiserver
    tier: control-plane
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
  - command:
    - kube-apiserver
    - --advertise-address=10.0.0.201
    - --allow-privileged=true
    - --authorization-mode=Node,RBAC       # 这里进行定义
    - --client-ca-file=/etc/kubernetes/pki/ca.crt
    - --token-auth-file=/etc/kubernetes/auth/token.csv
    - --enable-admission-plugins=NodeRestriction
    - --enable-bootstrap-token-auth=true
    ......
```



![image-20250108193615349](D:\git_repository\cyber_security_learning\markdown_img\image-20250108193615349.png)





####  RBAC 机制



##### RBAC基础概念

- **实体（Entity）**：在RBAC也称为**Subject**，通常指的是**User**、**Group** 或者 **ServiceAccount**,即对哪些人进行授权
- **资源（Resource）**：在RBAC中也称为**Object**，指代Subject期望操作的目标，例如**Secret、Pod及 Service对象**等
  - 仅限于/api/v1/ 或 /apis/// 开始的路径
  - 其它路径对应的端点均被视作“非资源类请求（Non-Resource Requests）”，例如: /healthz  端点
- **动作（Actions）**：Subject可以于Object上有权限执行的特定操作，具体的可用动作取决于Kubernetes的定义
  - **Object**
    - 读操作：get、list、watch等
    - 写操作：create、update、patch、delete、deletecollection等
  - **非Object**: 仅支持get操作
- **规则Rules**: 是一组属于不同 API Group 资源上的操作的权限集合,即资源Resource和动作Actions 的组合的授权规则
- **角色（Role）**：承载资源操作权限的容器,包含一组权限的规则,只有允许没有拒绝权限
- **Role：**名称空间级别，生效范围为其所属的名称空间
  - **ClusterRole：**集群级别，生效范围为整个集群
- **角色绑定（Role Binding）**：将角色关联至实体上，它能够将角色具体的操作权限赋予给实体,即将角色上的权限授予给账号，标准的资源类型
- **RoleBinding:** 绑定在名称空间级别,即只授权拥有指定名称空间范围的权限 
  - **ClusterRoleBinding:** 绑定在集群级别,即授权拥有集群范围中所有名称空间的权限





#####  RBAC 授权机制

 **角色和角色绑定**

授权指的是将某些subject对象赋予执行某些资源动作的权限。有时候会将其称为Group(权限组)，有两 部分组成：角色（组名）和角色绑定(组关联)。

简单来说：**授权为用户授予某种角色**

| 组 成    | 解析                                                         |
| -------- | ------------------------------------------------------------ |
| 角色     | 其实是附加在某些资源上的一系列权限的集合，对于k8s来说，它主要有两类：**Role和 clusterRole**<br />其中Role主要是作用于namespace，而clusterRole主要作用于多个namespace，它们之间 是一对多的关系。<br />为了将权限应用和具体权限列表分开描述，一般称权限列表为规则-rules |
| 角色绑定 | 将之前定义的Subject和对应的权限组关联在一起，表示某个Subject具 有执行某个资源的一系列动作权限。<br />它主要涉及到两个RoleBinding和 ClusterRoleBinding。 |



![image-20250108195742108](D:\git_repository\cyber_security_learning\markdown_img\image-20250108195742108.png)



**角色Role分类：**

- **ClusterRole：**集群范围内的资源的操作权限的集合,存在于所有名称空间
- **Role：**名称空间范围内资源操作的权限的集合,只存在于特定的名称空间



**角色绑定 RoleBinding 分类**

- **ClusterRoleBinding**：集群范围内的角色绑定,即分配给集群中所有名称空间相应的权限
- **RoleBinding**：名称空间范围内的角色绑定,,即只分配给指定名称空间相应的权限



##### 角色和角色绑定组合

![image-20250108201908367](D:\git_repository\cyber_security_learning\markdown_img\image-20250108201908367.png)



- namespace 级别
- cluster 级别
- 混合级别



**namespace级别组合**

| 术语        | 解析                                                         |
| ----------- | ------------------------------------------------------------ |
| rules       |                                                              |
| role        | 名称空间级别，生效范围为其所属的名称空间<br />表示在一个namespace中基于rules使用资源的权限，属于集群内部的 API 资源， 主要涉及到操作和对象 |
| RoleBinding | 将Subject关联至Role,授权给Subject可以在RoleBinding所在的名称空间使用指定 资源的role角色权限<br />也可以将Subject使用RoleBinding关联至ClusterRole上，**该角色赋予到Subject的 权限也会降级到RoleBinding所属的Namespace范围之内** |

```ABAP
注意: 在名称空间级授权时,必须要保证ServiceAccounts (SA) and RoleBindings 都在同个名称空间下
```



**cluster级别组合**

| 术语               | 解析                                                         |
| ------------------ | ------------------------------------------------------------ |
| ClusterRole        | 定义集群范围内的资源操作权限集合，包括集群级别及名称空间级别的资源对象<br />表示在一个cluster中基于rules使用资源的权限，属于集群内部的 API 资 源，一个cluster有多个namespace即有多个role |
| ClusterRoleBinding | 将Subject关联至ClusterRole，授权给Subject可以在集群中使用指定资源 的ClusterRole角色权限<br />即将实体（User、Group或ServiceAccount）关联至ClusterRole |



**混合级别组合**

| 术语        | 解析                                                         |
| ----------- | ------------------------------------------------------------ |
| ClusterRole | 定义集群范围内的资源操作权限集合，包括集群级别及名称空间级别的资源对象 表示在一个cluster中基于rules使用资源的权限，属于集群内部的 API 资源，一个 cluster有多个namespace即有多个role |
| RoleBinding | 将Subject基于RoleBinding与ClusterRole绑定在一起，表示Subject可以使用所有 namespace中指定资源的role角色，从而避免了多次role和user的RoleBinding。 同样的操作，站在ClusterRole的角度，我们可以理解为，用户得到的权限仅是 ClusterRole的权限在Rolebinding所属的名称空间上的一个子集，也就是所谓 的"权限降级" |



**RoleBinding 绑定 ClusterRole 的场景和原因**

**场景1：限定集群级权限在特定命名空间中**

- `ClusterRole` 通常定义集群级别的权限，但某些情况下，你可能希望将这些集群级权限限制到一个特定的命名空间。
- 通过 `RoleBinding` 绑定 `ClusterRole`，你可以有效地**将集群级的操作权限仅应用于某个命名空间**。

**示例：**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: admin-binding
  namespace: my-namespace
subjects:
- kind: User
  name: alice
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: admin
  apiGroup: rbac.authorization.k8s.io
```

- 里的 `admin` 是一个集群级别的角色（`ClusterRole`），但通过 `RoleBinding` 将其权限限制在 `my-namespace` 命名空间中。



**用途**

- 限制用户（如开发人员）在特定命名空间中的操作权限，防止其对集群其他部分造成影响。



**场景2：重用 ClusterRole**

- 有时集群管理员可能已经定义了一些通用的 `ClusterRole`，如 `view`、`edit`、`admin`，这些角色可以覆盖很多场景。
- 为了避免重新创建一个相同规则的 `Role`，可以直接通过 `RoleBinding` 绑定已有的 `ClusterRole`。



**示例：**

- 为了避免重新创建一个相同规则的 `Role`，可以直接通过 `RoleBinding` 绑定已有的 `ClusterRole`。
- 这样可以减少管理复杂度，并重用已有的权限模型。



##### 默认的ClusterRole及ClusterRoleBinding

启用RBAC鉴权模块时，API Server会自动创建一组ClusterRole和ClusterRoleBinding对象

- 多数都以“system:”为前缀，也有几个面向用户的ClusterRole未使用该前缀，如cluster-admin、 admin等
- 它们都默认使用“kubernetes.io/bootstrapping: rbac-defaults”这一标签



**默认的ClusterRole大体可以分为如下5个类别**

- **API发现相关的角色**
  - 包括system:basic-user、system:discovery和system:public-info-viewer
- **面向用户的角色**
  - 包括cluster-admin、admin、edit和view
- **核心组件专用的角色**
  - 包括system:kube-scheduler、system:volume-scheduler、system:kube-controller-manager、 system:node和system:node-proxier等
- **其它组件专用的角色**
  - 包括system:kube-dns、system:node-bootstrapper、system:node-problem-detector和 system:monitoring等
- **内置控制器专用的角色**





**用于交互式用户授权目的的常见角色**

```bash
# 查看cluster-admin
#可以通过clusterrole 资源来查看cluster-admin的所有权限信息
[root@master1 sa]# kubectl get clusterrole cluster-admin  -o yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  creationTimestamp: "2025-01-04T01:44:14Z"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: cluster-admin
  resourceVersion: "74"
  uid: 7defd096-536a-4bd1-890c-e496d1c5f35e
rules:
- apiGroups:
  - '*'
  resources:
  - '*'
  verbs:
  - '*'
- nonResourceURLs:
  - '*'
  verbs:
  - '*'

#查看role角色cluster-admin同名的clusterrolebinding
[root@master1 sa]# kubectl get clusterrolebinding cluster-admin -o yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  creationTimestamp: "2025-01-04T01:44:14Z"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: cluster-admin
  resourceVersion: "138"
  uid: 969955ea-19c0-4590-836c-68652f9deb73
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: system:masters    #对组system:masters进行角色绑定

# 查看admin
[root@master1 sa]#kubectl get clusterrole admin  -o yaml
aggregationRule:
  clusterRoleSelectors:
  - matchLabels:
      rbac.authorization.k8s.io/aggregate-to-admin: "true"
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  creationTimestamp: "2025-01-04T01:44:14Z"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: admin
  resourceVersion: "355"
  uid: 74c723db-9eac-4c11-89eb-172f8c98ec7b
rules:
- apiGroups:
  - ""          # ""（空字符串）表示默认的 Core API 组，即属于 Kubernetes 核心 API 的资源
  resources:
  - pods/attach
  - pods/exec
  - pods/portforward
  - pods/proxy
  - secrets
  - services/proxy
  verbs:
  - get
  - list
  - watch
......

# 重启apiServer的方法
# 删掉当前的API Server Pod，kubelet 会自动重新创建
kubectl delete pod kube-apiserver-<node-name> -n kube-system
```





#### Role 和 RoleBinding 组合实现



##### 创建Role

**属性解析**

```bash
#因为角色由于级别不一样，作用的范围也不同，Role的属性，可以使用 kubectl explain role 的方式来查看
[root@master1 ~]#kubectl explain role.rules
apiVersion <string>
kind <string>
metadata     <Object>
rules       <[]Object>
  apiGroups   <[]string>
  nonResourceURLs     <[]string>
  resourceNames       <[]string>
  resources   <[]string>
  verbs       <[]string> -required-
  
#结果显示：
对于role来说，其核心的内容主要是rules的权限规则
在这么多rules属性中，最重要的是verbs就是权限条目，而且所有的属性都是可以以列表的形式累加存在

#命令式命令
kubectl create role NAME --verb=verb --resource=resource.group/subresource [--resource-name=resourcename]
verb：#允许在资源上使用的操作（verb）列表
resources.group/subresource：#操作可施加的目标资源类型或子资源列表
resourcename：#特定的资源对象列表，可选

# 示例
# 创建一个对所有pod,service,deployment具有get,list权限的role的资源定义文件格式
[root@master1 ~]# kubectl create role pods-viewer --verb=get,list --resource=pods,services,deployments --dry-run -o yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: pods-viewer            
rules:                          
- apiGroups:                 
  - ""
  resources:
  - pods
  - services
  verbs:
  - get
  - list
- apiGroups:
  - apps
  resources:
  - deployments
  verbs:
  - get
  - list

#结果显示：
#role必备的rules主要有三部分组成：apiGroup、resources、verbs
apiGroups #设定包含资源的api组，如果是多个，表示只要属于api组范围中的任意资源都可以操作
resources #位于apiGroup范围中的某些具体的资源对象
verbs #针对具体资源对象的一些具体操作
```



##### 角色绑定rolebinding

RoleBinding 或者 ClusterRoleBinding 可绑定角色到某主体（Subject） 上。 主体可以是组，用户或者 服务账户。

Kubernetes 用字符串来表示用户名。 

- 用户名可以是普通的用户名，像 "alice"；
- 邮件风格的名 称，如 "bob@example.com"， 
- 以字符串形式表达的数字 ID。



**注意：**

前缀 system: 是 Kubernetes 系统保留的，所以你**要确保所配置的用户名或者组名不能出现上述 system: 前缀**。除了对前缀的限制之外，RBAC 鉴权系统不对用户名格式作任何要求。

服务账户（ServiceAccount） 的用户名前缀为 system:serviceaccount:，属于前缀为 system:serviceaccounts: 的用户组。

- **system:serviceaccount**: （单数）是用于服务账户用户名的前缀
- **system:serviceaccounts**: （复数）是用于服务账户组名的前缀



**RoleBinding 示例**

下面示例是 RoleBinding 中的片段，仅展示其 subjects 的部分



**对于名称为 alice@example.com 的用户：**

```yaml
subjects:
- kind: User
  name: "alice@example.com"
  apiGroup: rbac.authorization.k8s.io
```



**对于名称为 frontend-admins 的用户组：**

```yaml
subjects:
- kind: Group
  name: "frontend-admins"
  apiGroup: rbac.authorization.k8s.io

```



**对于 kube-system 名字空间中的默认服务账户：**

```yaml
subjects:
- kind: ServiceAccount
  name: default
  namespace: kube-system
```



**对于 "qa" 名称空间中的所有服务账户：**

```yaml
subjects:
- kind: Group
  name: system:serviceaccounts:qa
  apiGroup: rbac.authorization.k8s.io
```



**对于在任何名字空间中的服务账户：**

```yaml
subjects:
- kind: Group
  name: system:serviceaccounts
  apiGroup: rbac.authorization.k8s.io
```



**对于所有已经过身份认证的用户：**

```yaml
subjects:
- kind: Group
  name: system:authenticated
  apiGroup: rbac.authorization.k8s.io
```



**对于所有未通过身份认证的用户：**

```yaml
subjects:
- kind: Group
  name: system:unauthenticated
  apiGroup: rbac.authorization.k8s.io
```



**对于所有用户：**

```yaml
subjects:
- kind: Group
  name: system:authenticated
  apiGroup: rbac.authorization.k8s.io
- kind: Group
  name: system:unauthenticated
  apiGroup: rbac.authorization.k8s.io
```

**注意**

```ABAP
RoleBinding 的权限作用范围仅限于其所在的命名空间。即使绑定的角色（Role）定义了可以操作某些资源的权限，这些权限也只能在 RoleBinding 所在的命名空间内生效。
```





##### UA绑定

**用户绑定属性简介**

```bash
#查看rolebinding的属性信息
[root@master1 ~]# kubectl explain rolebinding
apiVersion        <string>
kind              <string>
metadata          <Object>
roleRef           <Object> -required
subjects          <[]Object>

#结果显示：对于角色绑定来说，主要涉及到两点：subject和对应的role权限列表，其中roleRef是必选项。

#命令式命令：
kubectl create rolebinding NAME --clusterrole=NAME|--role=NAME [--user=username] [--group=groupname] [--namespace=namespace_name]

#可以绑定到Role，也可以绑定到ClusterRole，后者会将ClusterRole的权限缩减至当前名称空间之内
#Subject可以是User、Group或者ServiceAccount

#示例：将用户tom绑定至角色pods-viewer之上,注意：pods-viewer和tom-attachto-pods-viewer都要求在default名称空间中
kubectl create rolebinding tom-attachto-pods-viewer --role=pods-viewer --user=tom --namespace=default
#而后可测试tom用户是否可读取default名称空间内的pods资源，以及其它资源
```



**范例: 配置文件**

```yaml
# 准备一个role资源文件，允许用户操作Deployment，Pod，RS的所有权限
[root@master1 sa] # cat security-role-myrole.yaml 
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: myrole
rules:
- apiGroups: ["", "extensions", "apps"]
  resources: ["pods", "deployments", "replicasets"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
  
  
# 以pod-sa-admin或者wang的subject来与myrole进行一次模拟绑定查看属性效果
[root@master1 ~]#kubectl create rolebinding test-myrole --role=myrole --user=test -o yaml --dry-run
W0109 22:24:54.445293  235536 helpers.go:703] --dry-run is deprecated and can be replaced with --dry-run=client.
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  creationTimestamp: null
  name: test-myrole
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: myrole
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: test


# 创建kubeconfig文件
[root@master1 sa] # kubectl config set-cluster mykube --embed-certs=true --certificate-authority=/etc/kubernetes/pki/ca.crt --server="https://10.0.0.201:6443" --kubeconfig=$HOME/.kube/mykube.conf
Cluster "mykube" set.

[root@master1 sa] # kubectl config set-credentials test --token="fd3e78.2a0395a1c58fb561" --kubeconfig=$HOME/.kube/mykube.conf
User "test" set.

[root@master1 sa] # kubectl config set-context test@mykube --cluster=mykube --user=test --kubeconfig=$HOME/.kube/mykube.conf 
Context "test@mykube" created.
[root@master1 sa]#

# 使用被授权的test账号进行测试
# default下的pod资源可以访问
[root@master1 sa] # kubectl get pod --context=test@mykube --kubeconfig=$HOME/.kube/mykube.conf
NAME           READY   STATUS    RESTARTS        AGE
pod-sa-admin   1/1     Running   2 (3h33m ago)   2d21h

# default下的secrets资源没有权限访问
[root@master1 sa]#kubectl get secrets --context=test@mykube --kubeconfig=$HOME/.kube/mykube.conf
Error from server (Forbidden): secrets is forbidden: User "test" cannot list resource "secrets" in API group "" in the namespace "default"

# 其他名称空间的pod资源也没有权限访问
[root@master1 sa]#kubectl get pod -n kube-system --context=test@mykube --kubeconfig=$HOME/.kube/mykube.conf
Error from server (Forbidden): pods is forbidden: User "test" cannot list resource "pods" in API group "" in the namespace "kube-system"
```



##### SA绑定

SA可以跨名称空间进行授权，比如:名称空间A的SA帐号可以授权给名称空间B的权限，甚至对所有名称空间授权



**命令格式**

```bash
# 查看sa的角色绑定格式
kubectl create rolebinding NAME --role=NAME [--serviceaccount=namespace:serviceaccoutname] [--namespace=namespace_name]

# 注意：在基于服务账号进行关联的时候，需要关注一下该SA所属的namespace信息。
```



**范例**

```bash
# 自建的sa是admin而且是属于default空间，先将admin和myrole进行绑定，查看一下效果
[root@master1 sa] # kubectl create rolebinding myrolebinding1 --role=myrole --serviceaccount=default:admin
rolebinding.rbac.authorization.k8s.io/myrolebinding1 created

# 查看效果
[root@master1 sa]#kubectl describe rolebinding myrolebinding1 
Name:         myrolebinding1
Labels:       <none>
Annotations:  <none>
Role:
  Kind:  Role
  Name:  myrole
Subjects:
  Kind            Name   Namespace
  ----            ----   ---------
  ServiceAccount  admin  default
```



##### 综合案例

**实现Jenkins的权限**

运行Kubernetes上的Jenkins，为能够动态创建jenkins-slave相关的Pod，需要对运行该Pod对应的ServiceAccount进行认证和授权

```yaml
# 创建Role
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: jenkins-master
  namespace: jenkins
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]
  - apiGroups: [""]
    resources: ["pods/exec"]
    verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["watch"]
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]

---
# 创建SA
apiVersion: v1
kind: ServiceAccount
metadata:
  name: jenkins-master
  namespace: jenkins

---
# 角色绑定
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: jenkins-master
  namespace: jenkins
roleRef:
  kind: Role
  name: jenkins-master
  apiGroup: rbac.authorization.k8s.io
subjects:
- kind: ServiceAccount
  name: jenkins-master
  namespace: jenkins     # 这里指定SA是jenkins名称空间下的SA，因为SA是名称空间级别的资源
```



#### ClusterRole和ClusterRoleBinding组合实现

cluster级别的实践主要涉及到clusterRole和ClusterRoleBinding之间的操作，即可以操作**集群内所有 namespace空间的资源**。



##### 创建Clusterrole

```bash
# kubectl explain clusterrole
aggregationRule     <Object>   #可以实现role的嵌套关系
apiVersion <string>
kind <string>
metadata     <Object>
rules        <[]Object>
  apiGroups           <[]string>
  nonResourceURLs     <[]string>
  resourceNames       <[]string>
  resources           <[]string>
  verbs               <[]string> -required-
  
#结果显示：clusterrole相对于role的属性多了一个集中控制器的属性aggregationRule，而这是一个可选的属性


# 查看一个简单的配置格式
[root@master1 sa]#kubectl create clusterrole myclusterrole --verb=get,list --resource=pods -o yaml --dry-run=client
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  creationTimestamp: null
  name: myclusterrole
rules:
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - get
  - list
#结果显示：单从模板的资源配置样式来说，其配置信息与role的配置信息几乎一样
```



**`aggregationRule` 的含义和用法**

在 Kubernetes 中，`aggregationRule` 是 `ClusterRole` 的一个属性，它允许实现**角色的嵌套关系**。通过 `aggregationRule`，你可以动态组合多个 `ClusterRole` 的权限，使得一个 `ClusterRole` 可以聚合其他角色的权限。



**`aggregationRule` 的结构**

- **`clusterRoleSelectors`**：这是 `aggregationRule` 的核心字段，用于指定一个 LabelSelector，通过匹配其他 `ClusterRole` 的标签来聚合其权限。

  - 结构示例

  ```yaml
  aggregationRule:
    clusterRoleSelectors:
    - matchLabels:
        rbac.example.com/aggregate-to-admin: "true"
    - matchLabels:
        rbac.example.com/aggregate-to-edit: "true"
  ```

  

**`aggregationRule` 的用法**

- **动态聚合角色权限**
  - `aggregationRule` 允许将其他 `ClusterRole` 的规则动态地组合到当前角色中。
  - 如果某个 `ClusterRole` 的标签匹配了 `aggregationRule` 中的 `clusterRoleSelectors`，它的权限会自动添加到定义了 `aggregationRule` 的角色中。



**详细示例**

- **场景:** 假设我们希望创建一个名为 `super-admin` 的角色，该角色需要聚合两个子角色的权限
  - 一个角色 `read-only`，只能对资源执行只读操作。
  - 一个角色 `edit`，可以编辑资源。

- **子角色定义**：

  - **`read-only` ClusterRole**

  ```YAML
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    name: read-only
    labels:
      rbac.example.com/aggregate-to-super-admin: "true"
  rules:
  - apiGroups: [""]
    resources: ["pods", "services"]
    verbs: ["get", "list"]
  ```

  - **`edit` ClusterRole**

  ```yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    name: edit
    labels:
      rbac.example.com/aggregate-to-super-admin: "true"
  rules:
  - apiGroups: [""]
    resources: ["pods", "services"]
    verbs: ["get", "list", "create", "update", "delete"]
  ```

- **聚合角色定义**

  - 使用 `aggregationRule` 动态聚合这两个角色：

  ```yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    name: super-admin
  aggregationRule:
    clusterRoleSelectors:
    - matchLabels:
        rbac.example.com/aggregate-to-super-admin: "true"
  ```

  - **聚合结果**
    - `super-admin` 角色自动继承了 `read-only` 和 `edit` 的规则。
    - 不需要手动写规则，只要某个角色被打上 `rbac.example.com/aggregate-to-super-admin: "true"` 标签，它的权限就会动态添加到 `super-admin` 中。



**`aggregationRule` 的优势**

- **动态聚合权限**：
  - 无需手动维护组合角色的权限规则，只需给子角色打上特定的标签即可
- **模块化和复用**：
  - 子角色可以单独使用，也可以通过聚合规则组合成更大的权限集，便于复用。
- **简化管理**
  - 当需要扩展权限时，只需创建新角色并添加对应的标签，主聚合角色会自动更新权限



**`aggregationRule` 注意事项**

- **只适用于 `ClusterRole`**：
  - 目前 `aggregationRule` 仅能用于聚合 `ClusterRole`，不能用于 `Role`。
- **动态更新**：
  - 如果修改了某个子角色的规则或标签，聚合角色会动态更新，无需重新创建。
- **标签管理**：
  - 子角色需要正确配置标签，确保能被聚合规则选择到。





##### 角色绑定Clusterrolebinding

```bash
# 命令格式
kubectl create clusterrolebinding NAME --clusterrole=NAME [--user=username] [--group=groupname]
[--serviceaccount=namespace:serviceaccountname] [--dry-run=server|client|none] [options]

#属性解析:对于clusterrolebinding来说，仅仅允许集群角色进行和其进行绑定，对于普通的role来说就无效了

#将wang用户和myclasterrole进行角色绑定，查看资源配置效果
[root@master1 sa]#kubectl create clusterrolebinding myclusterrolebinding --clusterrole=myclusterrole --user=test --dry-run=client -o yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  creationTimestamp: null
  name: myclusterrolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: myclusterrole
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: test

#属性解析：这里的属性配置与我们之前的role和rolebinding的方法几乎一样,区别就是kind和--clusterrole的不同
```



##### 案例: 实现 Prometheus 的权限

将Prometheus部署运行于Kubernetes之上并监控集群时，需要使用专用的ServiceAccount运行该Pod 并认证和授权到API Server

```yaml
[root@master1 sa] # vim clusterrolebinding-prometheus.yaml
# ClusterRole
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRole
metadata:
  name: prometheus
rules:
- apiGroups: [""]
  resources:
  - nodes
  - nodes/proxy
  - services
  - endpoints
  - pods
  verbs: ["get", "list", "watch"]
- apiGroups:
  - extensions
  resources:
  - ingresses
  verbs: ["get", "list", "watch"]
- nonResourceURLs: ["/metrics"]
  verbs: ["get"]

---
# 创建SA
apiVersion: v1 
kind: ServiceAccount
metadata:
  name: prometheus
  namespace: prom

---
# ClusterRoleBinding
apiVersion: rbac.authoriaztion.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: prometheus
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: prometheus
subjects:
- kind: ServiceAccount
  name: prometheus
  namespace: prom
```



#### ClusterRole和RoleBingding混合组合实现



##### 实现对指定多个名称空间的资源设置特定权限

实现对指定多个名称空间的资源设置特定权限的方法，但需要组合使用 **`RoleBinding`** 和 **`ClusterRole`**

**实现思路**

- 创建一个 `ClusterRole`
  - `ClusterRole` 是集群级别的角色，可以指定资源的操作权限，但不绑定到任何特定名称空间。
- 在目标名称空间中创建多个 `RoleBinding`
  - 每个 `RoleBinding` 将该 `ClusterRole` 绑定到指定的名称空间和对应的用户或服务账户



**示例配置**：假设需要在 `namespace1` 和 `namespace2` 中，赋予 `UserA` 对 `pods` 和 `services` 资源的只读权限。

- **创建 `ClusterRole`**

  ```yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    name: readonly-pods-services
  rules:
  - apiGroups: [""]
    resources:
    - pods
    - services
    verbs:
    - get
    - list
    - watch
  ```

- **为 `namespace1` 创建 `RoleBinding`**

  ```yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: RoleBinding
  metadata:
    name: readonly-access
    namespace: namespace1  # 绑定到 namespace1
  subjects:
  - kind: User
    name: UserA  # 授予权限的用户
    apiGroup: rbac.authorization.k8s.io
  roleRef:
    kind: ClusterRole
    name: readonly-pods-services  # 引用上面定义的 ClusterRole
    apiGroup: rbac.authorization.k8s.io
  ```

- **为 `namespace2` 创建 `RoleBinding`**

  ```yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: RoleBinding
  metadata:
    name: readonly-access
    namespace: namespace2  # 绑定到 namespace2
  subjects:
  - kind: User
    name: UserA  # 授予权限的用户
    apiGroup: rbac.authorization.k8s.io
  roleRef:
    kind: ClusterRole
    name: readonly-pods-services  # 引用上面定义的 ClusterRole
    apiGroup: rbac.authorization.k8s.io
  ```



**工作原理**

- `ClusterRole` 定义了对资源的具体权限，但不限定作用范围
- `RoleBinding` 将该 `ClusterRole` 的权限限定在指定的名称空间中，并指定用户或服务账户。
- 每个 `RoleBinding` 只在其所在的名称空间中生效，因此可以通过在多个名称空间中创建 `RoleBinding`，实现对特定多个名称空间的资源进行权限控制。



### 图形化面板

#### kuboard

```ABAP
官网：https://kuboard.cn/install/v3/install.html
```

![image-20250111162025438](D:\git_repository\cyber_security_learning\markdown_img\image-20250111162025438.png)



##### 以Docker方式在集群外部署

```bash
sudo docker run -d \
  --restart=unless-stopped \
  --name=kuboard \
  -p 80:80/tcp \
  -p 10081:10081/tcp \
  -e KUBOARD_ENDPOINT="http://内网IP:80" \
  -e KUBOARD_AGENT_SERVER_TCP_PORT="10081" \
  -v /root/kuboard-data:/data \
  eipwork/kuboard:v3
  # 也可以使用镜像 swr.cn-east-2.myhuaweicloud.com/kuboard/kuboard:v3 ，可以更快地完成镜像下载。
  # 请不要使用 127.0.0.1 或者 localhost 作为内网 IP \
  # Kuboard 不需要和 K8S 在同一个网段，Kuboard Agent 甚至可以通过代理访问 Kuboard Server \

```





##### 基于Kubernetes集群中部署

**使用StorageClass持久化**

```yaml
[root@master1 nfc-sc] # cat rbac.yaml 
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


[root@master1 nfc-sc] # cat nfs-client-provisioner.yaml 
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


[root@master1 nfc-sc] # cat nfs-storageClass.yaml 
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: sc-nfs
  annotations:
    storageclass.kubernetes.io/is-default-class: "false" # 是否设置为默认的storageClass
provisioner: k8s-sigs.io/nfs-subdir-external-provisioner # or choose another name, must match deployment's env PROVISIONER_NAME
parameters:
  archiveOnDelete: "true"   # 即使删除PVC，依然会保留数据
```



**获取部署 Kuboard 所需的 YAML 文件**

```bash
curl -o kuboard-v3.yaml https://addons.kuboard.cn/kuboard/kuboard-v3-storage-class.yaml
```



**编辑 `kuboard-v3.yaml` 文件中的配置，该部署文件中，有两处配置必须修改**

```bash
# KUBOARD_ENDPOINT
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: kuboard-v3-config
  namespace: kuboard
data:
  # 关于如下参数的解释，请参考文档 https://kuboard.cn/install/v3/install-built-in.html
  # [common]
  KUBOARD_ENDPOINT: 'http://your-node-ip-address:30080' # 这里改为自己指定的域名，后续用ingress暴露，所以不用写端口
 #KUBOARD_ENDPOINT: 'http://kuboard.mystical.org'
  KUBOARD_AGENT_SERVER_UDP_PORT: '30081'
  KUBOARD_AGENT_SERVER_TCP_PORT: '30081'

# storageClassName
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      # 请填写一个有效的 StorageClass name
      storageClassName: please-provide-a-valid-StorageClass-name-here
      #storageClassName: sc-nfs
      accessModes: [ "ReadWriteMany" ]
      resources:
        requests:
          storage: 5Gi

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: kuboard-data-pvc
  namespace: kuboard   # 这里官方没有加名称空间，但是PVC是名称空间资源，这里需要加上
spec:
  # 请填写一个有效的 StorageClass name
  storageClassName:  please-provide-a-valid-StorageClass-name-here
  #storageClassName: sc-nfs
  accessModes:
    - ReadWriteOnce
    
    
# 上述官方文件修改后，应用
[root@master1 ~] # kubectl apply -f kuboard-v3.yaml 
namespace/kuboard created
configmap/kuboard-v3-config created
statefulset.apps/kuboard-etcd created
persistentvolumeclaim/kuboard-data-pvc created
service/kuboard-etcd created
deployment.apps/kuboard-v3 created
service/kuboard-v3 created


# 添加ingress，要提前部署ingress-nginx
[root@ubuntu2204 ~]# kubectl create ingress kuboard-ingress --rule=kuboard.mystical.org/*=kuboard-v3:80 --class nginx -n kuboard -o yaml --dry-run=client > kuboard-ingress.yaml

[root@ubuntu2204 ~]#kubectl apply -f kuboard-ingress.yaml 
ingress.networking.k8s.io/kuboard-ingress created

[root@ubuntu2204 ~]#kubectl get ingress -n kuboard
NAME              CLASS   HOSTS                  ADDRESS     PORTS   AGE
kuboard-ingress   nginx   kuboard.mystical.org   10.0.0.10   80      21s

# 在宿主机解析域名后在浏览器访问kuboard.mystical.org
# 默认用户名：admin
# 默认密码：Kuboard123
```

![image-20250111203856817](D:\git_repository\cyber_security_learning\markdown_img\image-20250111203856817.png)

![image-20250112195241195](D:\git_repository\cyber_security_learning\markdown_img\image-20250112195241195.png)



#### KubeSphere

```ABAP
官网：https://www.kubesphere.io/zh/docs/v3.4/installing-on-linux/introduction/multioverview/
```



![image-20250111162716226](D:\git_repository\cyber_security_learning\markdown_img\image-20250111162716226.png)



确保您的机器满足安装的前提条件之后，可以按照以下步骤安装 KubeSphere。

```bash
kubectl apply -f https://github.com/kubesphere/ks-installer/releases/download/v3.4.1/kubesphere-installer.yaml

# 在该文件指定存储，或者配置好默认存储
kubectl apply -f https://github.com/kubesphere/ks-installer/releases/download/v3.4.1/cluster-configuration.yaml
```

检查安装日志：

```bash
kubectl logs -n kubesphere-system $(kubectl get pod -n kubesphere-system -l 'app in (ks-install, ks-installer)' -o jsonpath='{.items[0].metadata.name}') -f
```

使用 `kubectl get pod --all-namespaces` 查看所有 Pod 是否在 KubeSphere 的相关命名空间中正常运行。如果是，请通过以下命令检查控制台的端口（默认为 `30880`）：

```bash
kubectl get svc/ks-console -n kubesphere-system
```

确保在安全组中打开了端口 `30880`，并通过 NodePort `(IP:30880)` 使用默认帐户和密码 `(admin/P@88w0rd)` 访问 Web 控制台



执行下列命令

```bash
[root@master1 kubesphere]#kubectl logs -n kubesphere-system $(kubectl get pod -n kubesphere-system -l 'app in (ks-install, ks-installer)' -o jsonpath='{.items[0].metadata.name}') -f

# 显示下方
......
**************************************************
Collecting installation results ...
#####################################################
###              Welcome to KubeSphere!           ###
#####################################################

Console: http://172.22.201.124:30880
Account: admin
Password: P@88w0rd
NOTES：
  1. After you log into the console, please check the
     monitoring status of service components in
     "Cluster Management". If any service is not
     ready, please wait patiently until all components 
     are up and running.
  2. Please change the default password after login.

#####################################################
https://kubesphere.io             2025-02-11 13:35:25
#####################################################

```

访问http://172.22.201.124:30880

![image-20250211135114480](D:\git_repository\cyber_security_learning\markdown_img\image-20250211135114480.png)

![image-20250211135302152](D:\git_repository\cyber_security_learning\markdown_img\image-20250211135302152.png)



## Kubernetes有状态服务管理





## Kubernetes包管理Helm





## Kubernetes网络剖析

在Docker模块的**`浅谈容器网络`**中，介绍了宿主机中的容器间通信是通过docker0作为网桥，将宿主机内的容器都连在这个网桥上。

那么Kubernetes中，不同节点间的容器进行通信，是不是可以**通过软件的方式，创建一个整个集群“公用”的网桥，然后把集群里的所有容器都连接到这个网桥上，不就可以相互通信了吗?**

这样一来，我们整个集群里的容器网络就会类似于下图所示的样子：

![image-20250116155827857](D:\git_repository\cyber_security_learning\markdown_img\image-20250116155827857.png)

可以看到，构建这种容器网络的核心在于：我们需要在已有的宿主机网络上，再**通过软件构建一个覆盖在已有宿主机网络之上的、可以把所有容器连通在一起的虚拟网络**。所以，这种技术就被称为：**Overlay Network（覆盖网络）**。





### 深入了解容器跨主机网络



#### Flannel概述

Flannel 项目是 CoreOS 公司主推的容器网络方案。事实上，Flannel 项目本身只是一个框架，真正为我们提供容器网络功能的，是 Flannel 的后端实现。目前，Flannel 支持三种后端实现，分别是：

- **VXLAN**
- **host-gw**
- **UDP**



这三种不同的后端实现，正代表了三种容器跨主网络的主流实现方法



##### UDP模式的跨主网络实现原理（已废弃）

假设有两台宿主机

- 宿主机 Node 1 上有一个容器 container-1，它的 IP 地址是 10.244.2.20，对应的 docker0 网桥的地址是：172.17.0.1/16
- 宿主机 Node 2 上有一个容器 container-2，它的 IP 地址是 10.244.3.27，对应的 docker0 网桥的地址是：172.17.0.1/16



**让 container-1 访问 container-2**



container-1 容器里的进程发起的 IP 包，其源地址就是 10.244.2.20，目的地址就是 10.244.3.27。由于目的地址 10.244.3.27 并不在 Node 1 的 docker0 网桥的网段里，所以这个 IP 包会被交给默认路由规则，通过容器的网关进入 docker0 网桥（如果是同一台宿主机上的容器间通信，走的是直连规则），从而出现在宿主机上。



这时候，这个 IP 包的下一个目的地，就取决于宿主机上的路由规则了。此时，Flannel 已经在宿主机上创建出了一系列的路由规则，以 Node 1 为例，如下所示：

```bash
[root@node1 ~]# route -n
内核 IP 路由表
目标            网关            子网掩码        标志  跃点   引用  使用 接口
0.0.0.0         10.0.0.2        0.0.0.0         UG    0      0        0 eth0
10.0.0.0        0.0.0.0         255.255.255.0   U     0      0        0 eth0
10.244.0.0      10.244.0.0      255.255.255.0   UG    0      0        0 flannel.1 # 命中，并进入flannel1.1设备
10.244.1.0      0.0.0.0         255.255.255.0   U     0      0        0 cni0
10.244.2.0      10.244.2.0      255.255.255.0   UG    0      0        0 flannel.1
10.244.3.0      10.244.3.0      255.255.255.0   UG    0      0        0 flannel.1   
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
```

由于我们的 IP 包的目的地址是10.244.3.27，它匹配不到本机 docker0 网桥对应的 172.17.0.1/16 网段，只能匹配到第三条、也就是 10.244.0.0/16 对应的这条路由规则，从而进入到一个叫作 flannel1.1 的设备中。



 **flannel1.1 设备是一个TUN设备（Tunnel 设备）。**

```ABAP
在 Linux 中，TUN 设备是一种工作在三层（Network Layer）的虚拟网络设备。TUN 设备的功能非常简单，即：在操作系统内核和用户应用程序之间传递 IP 包。
```



当操作系统将一个 IP 包发送给 flannel0 设备之后，flannel0 就会把这个 IP 包，交给创建这个设备的应用程序，也就是 Flannel 进程。这是一个从内核态（Linux 操作系统）向用户态（Flannel 进程）的流动方向。

```ABAP
Container1-eth0 ---> 根据路由 ---> flannel1.1 ---> flanneld进程处理
```



反之，如果 Flannel 进程向 flannel0 设备发送了一个 IP 包，那么这个 IP 包就会出现在宿主机网络栈中，然后根据宿主机的路由表进行下一步处理。这是一个从用户态向内核态的流动方向。

当 IP 包从容器经过 docker0 出现在宿主机，然后又根据路由表进入 flannel0 设备后，宿主机上的 flanneld 进程（Flannel 项目在每个宿主机上的主进程），就会收到这个 IP 包。然后，flanneld 看到了这个 IP 包的目的地址，是 10.244.3.27，就把它发送给了 Node 2 宿主机。



**flanneld 又是如何知道这个 IP 地址对应的容器，是运行在 Node 2 上的呢？**



 Flannel 项目里一个非常重要的概念：子网（Subnet）。

事实上，在由 Flannel 管理的容器网络里，一台宿主机上的所有容器，都属于该宿主机被分配的一个“子网”。在我们的例子中，Node 1 的子网是 100.96.1.0/24，container-1 的 IP 地址是 100.96.1.2。Node 2 的子网是 100.96.2.0/24，container-2 的 IP 地址是 100.96.2.3。

而这些子网与宿主机的对应关系，正是保存在 Etcd 当中，如下所示：

```bash
$ etcdctl ls /coreos.com/network/subnets
/coreos.com/network/subnets/100.96.1.0-24
/coreos.com/network/subnets/100.96.2.0-24
/coreos.com/network/subnets/100.96.3.0-24
```



**注意：****如果 `--kube-subnet-mgr` 参数存在**，说明 Flannel 使用 Kubernetes API 而非 etcd 存储数据。

```bash
[root@master1 net.d]#kubectl -n kube-flannel describe daemonsets.apps kube-flannel-ds |grep -P "\-\-kube-subnet-mgr"
      --kube-subnet-mgr  # 说明Flannel使用的Kubernetes API

```



在Kubernetes API模式下，Flannel的子网分配信息存储在每个节点上的Annotation中，可以通过一下命令查看

```bash
[root@master1 ~]#kubectl get nodes -o json | jq '.items[] | {name: .metadata.name, podCIDR: .spec.podCIDR, flannelSubnet: .metadata.annotations["flannel.alpha.coreos.com/subnet"]}'
{
  "name": "master1",
  "podCIDR": "10.244.0.0/24",
  "flannelSubnet": null
}
{
  "name": "node1",
  "podCIDR": "10.244.1.0/24",
  "flannelSubnet": null
}
{
  "name": "node2",
  "podCIDR": "10.244.2.0/24",
  "flannelSubnet": null
}
{
  "name": "node3",
  "podCIDR": "10.244.3.0/24",
  "flannelSubnet": null
}
```



所以，flanneld 进程在处理由 flannel0 传入的 IP 包时，就可以根据目的 IP 的地址（比如 100.96.2.3），匹配到对应的子网（比如 100.96.2.0/24），从 Etcd 中找到这个子网对应的宿主机的 IP 地址



**当container-1发起对container-2的访问请求时，数据包的通信过程如下**

- container-1发出一个IP包，源地址为`10.244.2.20`，目的地址为`10.244.3.27`
- 这个IP包首先到达Node 1的docker0网桥**（这里进行一次判断）**。由于目的地址`10.244.3.37`不在docker0网桥的网段内，所以这个IP包会被转发给默认路由**。(此时进行第一次用户态和内核态的切换)**
- 根据Node 1上的路由规则，这个IP包会被送往一个名为flannel0的设备。flannel0是一个TUN设备，它在三层网络上工作。
- flannel0设备会将这个IP包交给用户态的flanneld进程处理。**(此时进行第二次用户态和内核态的切换)**
- flanneld进程通过查询Etcd（或者**Kubernetes API**），得知目的IP地址10.244.3.27所在的子网对应的宿主机是Node 2，其IP地址为`10.0.0.202`。
- flanneld将原始的IP包封装在一个UDP包里，然后发送给Node 2的8285端口（flanneld默认监听的端口）。**(此时进行三次用户态和内核态的切换)**
- 当这个UDP包到达Node 2后，会被Node 2上的flanneld进程接收和解包，还原出原始的IP包。**(此时另一台主机进行一次用户态和内核态的切换)**
- Node 2的flanneld将还原出的IP包交给本机的flannel0设备。**(此时另一台主机进行二次用户态和内核态的切换)**
- flannel0设备将IP包转发给docker0网桥。
- docker0网桥根据目的IP地址，将包转发给container-2。**(此时另一台主机进行三次用户态和内核态的切换)**



**UDP封装与解封装过程**

- **封装过程包括以下步骤**

  - flanneld首先检查数据包的目的IP地址，确定目标容器所在的宿主机
  - flanneld然后创建一个新的UDP数据包。这个UDP数据包的源IP地址是当前宿主机的IP地址，目的IP地址是目标容器所在宿主机的IP地址。UDP端口通常是8285。
  - 原始的IP数据包被放入这个UDP数据包的负载部分。
  - flanneld将封装好的UDP数据包交给宿主机的网络栈，由宿主机的网络栈负责将这个UDP包发送出去。

  

- **拆解UDP解封装过程**

  - 目标宿主机的网络栈接收到UDP包，发现目的端口是8285，于是将这个包交给监听在8285端口的flanneld进程。
  - flanneld进程接收到UDP包后，从UDP包的负载中提取出原始的IP数据包
  - flanneld将提取出的原始IP包写入本机的flannel0设备。
  - Linux内核接收到这个IP包，根据路由规则将其转发给docker0网桥。
  - docker0网桥根据IP包的目的地址，将包转发给目标容器。





**UDP网络模式性能问题在实际应用中的表现可能如下:**

- **较高的网络延迟**: 由于每个数据包都需要经过多次处理和状态切换，网络延迟会显著增加。
- **CPU使用率升高**: 频繁的状态切换和数据拷贝会消耗大量的CPU资源。
- **吞吐量受限**: 由于单个flanneld进程需要处理所有流量，在高并发情况下可能会成为瓶颈。
- **内存带宽压力**: 多次数据拷贝会增加内存带宽的使用。
- **网络效率降低**: UDP封装增加了数据包大小，降低了网络的有效载荷比例。



正是由于这些性能问题，UDP模式在实际生产环境中很少被使用。 相比之下，VXLAN模式通过在内核态实现封装和解封装，大大减少了用户态和内核态的切换，同时也减少了数据拷贝的次数，因此能够提供更好的性能



##### VXLAN网络模式剖析

VXLAN，即 Virtual Extensible LAN（虚拟可扩展局域网），是 Linux 内核本身就支持的一种网络虚似化技术。所以说，VXLAN 可以完全在内核态实现上述封装和解封装的工作，从而通过与前面相似的“隧道”机制，构建出覆盖网络（Overlay Network）。













## Kubernetes网络插件详解



**Kubernetes网络** 

- **Node网络**
  - 各Node是否在同一网段（子网）会影响可以使用的Pod的网络模型
- **Service网络**
  - 由集群自行管理（Kube proxy）
- **Pod网络**
  - 只提供了CNI，具体实现交给第三方
  - Flanny
    - 默认网段：10.244.0.0/16
  - Calico
    - 默认网段：192.168.0.0/16
  - Cilium
    - 默认网段：192.168.0.0/16



**将容器接入到网络中**

- 首先要有虚拟网络接口提供给容器，即向容器**注入虚拟网络接口**（创建Pod时）
- 为Pod**准备好专有网络**（由网络插件负责）
- 将Pod容器的网络接口连入到Pod网络（创建Pod时）
- 为该Pod的网络接口提供IP地址（启动Pod时，关闭Pod释放IP地址）

```ABAP
除了准备Pod网络是在部署网络插件时一次性提供好的之外，后续的注入接口，配置地址等，都和Pod自身的生命周期相关，而和网络插件无关
```



**真正给Pod分配地址的程序，是位于每个节点上都有一个节点范围的地址的维护程序，而不是整个集群范围的**

- 这个程序通常在节点范围内维护一个地址池，并从该地址池中分配 IP 地址给新创建的 Pod。这种设计体现了 Kubernetes 网络的去中心化特点。



**详细解释**

- **节点范围的地址池**
  - 每个节点上的 CNI 插件负责**从节点范围内的地址池**中为 Pod 分配 IP 地址。
  - 每个节点通常会分配一个**子网范围的地址池**，这个地址池是由网络插件在初始化时分配的。例如，节点 A 的地址池可能是 `10.244.1.0/24`，节点 B 的地址池可能是 `10.244.2.0/24`。
  - Pod 的 IP 地址是从该子网中分配的，比如节点 A 上的 Pod IP 可能是 `10.244.1.2`，而节点 B 上的 Pod IP 可能是 `10.244.2.3`。
- **本地分配与全局通信**
  - 分配 IP 的过程是本地化的，网络插件在每个节点上独立运行，不需要与整个集群的控制平面直接通信。
  - 分配完成后，Kubernetes 的控制平面（API Server 等）会知道每个 Pod 的 IP 地址，以便进行网络通信的路由设置。
- **去中心化的优势**
  - 去中心化分配降低了中心节点的负载，因为 IP 地址的分配和管理是分布式的。
  - 即使集群规模扩大，由于地址分配是每个节点独立完成的，分配速度不会显著受到影响





**如何避免每个节点上独立的网络地址分配程序所分配的IP在不同节点上不相互冲突**

整个Kubernetes有很多个节点，通常在节点上维护节点上Pod地址的是节点级的插件，叫**IPAM插件**（IP Addresses Manager）

**Flanny解决方案**

- 为每个节点分配一个子网
- 总的子网是10.244.0.0/16，将其再做子网划分，默认使用**24bits**掩码
- 因此，每个节点的子网是0-255，而整个Kubernetes集群**最多能管理256个节点**
- 每个节点上的**可用地址为254个**（256-2）

```ABAP
默认情况下，Kubernetes为每个节点最多调度运行的Pod数量为110个
```



**Calico解决方案**

- 总的子网是192.168.0.0/16
- 默认使用**26bits**掩码，进行子网划分



## Kubernetes调度框架











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





## K8S中安全机制的证书体系



### Kubelet 和 apiServer之间通信

Kubernetes 中 **kubelet 和 API Server 之间的通信**确实很好地体现了 Kubernetes **双向 TLS（mTLS，Mutual TLS）**的加密机制。这种机制通过双向验证确保了通信的安全性和身份的可信性。



#### Kubernetes 双向 TLS 通信的工作机制

**双向 TLS 加密：**

- 双向 TLS 意味着：
  - **客户端（kubelet）验证服务端（API Server）的身份**。
  - **服务端（API Server）验证客户端（kubelet）的身份**。
- 这种双向认证确保了双方都是可信任的，并防止了中间人攻击（MitM）。



**涉及的证书：**

- **kubelet 的客户端证书** 

  ```bash
  [root@node1 pki]# ls /var/lib/kubelet/pki/kubelet-client-current.pem
  
  [root@node1 pki]# openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -text -noout
  Certificate:
      Data:
          Version: 3 (0x2)
          Serial Number:
              f4:4c:9d:a8:f2:82:e8:fd:07:5a:3b:64:57:45:ed:cc
          Signature Algorithm: sha256WithRSAEncryption
          Issuer: CN = kubernetes            # 上级CA
          Validity
              Not Before: Jan  4 01:40:29 2025 GMT
              Not After : Jan  4 01:40:29 2026 GMT
          Subject: O = system:nodes, CN = system:node:node1
          Subject Public Key Info:
              Public Key Algorithm: id-ecPublicKey
              ......
  ```

  - kubelet 用于向 API Server 证明自己的身份。

- **API Server 的服务端证书**

  ```bash
  /etc/kubernetes/pki/apiserver.crt
  
  [root@master1 pki]#openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout
  Certificate:
      Data:
          Version: 3 (0x2)
          Serial Number: 8495257128868470889 (0x75e5375951cf6069)
          Signature Algorithm: sha256WithRSAEncryption
          Issuer: CN = kubernetes            # 上级CA
          Validity
              Not Before: Jan  4 01:39:06 2025 GMT
              Not After : Jan  4 01:44:06 2026 GMT
          Subject: CN = kube-apiserver
          Subject Public Key Info:
          ......
  ```

  - API Server 用于向 kubelet 证明自己的身份。

- **CA 证书**

  ```bash
  /etc/kubernetes/pki/ca.crt
  
  [root@node1 pki]# openssl x509 -in ca.crt -text -noout
  Certificate:
      Data:
          Version: 3 (0x2)
          Serial Number: 1575855922115436521 (0x15de909ca6e2dfe9)
          Signature Algorithm: sha256WithRSAEncryption
          Issuer: CN = kubernetes            # 上级CA
          Validity
              Not Before: Jan  4 01:39:06 2025 GMT
              Not After : Jan  2 01:44:06 2035 GMT
          Subject: CN = kubernetes          # 上级CA一致，因此是自签证书
          Subject Public Key Info:
          ......
  ```

  - kubelet 和 API Server 都通过该 CA 证书验证对方的证书是否合法。



**通信过程：**

- kubelet 连接到 API Server：
  1. kubelet 发起 HTTPS 请求，并发送自己的客户端证书和私钥。
  2. API Server 验证 kubelet 的客户端证书是否由可信 CA 签发。
  3. 验证通过后，API Server 确认 kubelet 是一个可信的客户端。

- API Server 返回响应：
  1. API Server 返回自己的服务端证书。
  2. kubelet 使用本地的 CA 证书验证 API Server 的服务端证书。
  3. 验证通过后，kubelet 确认 API Server 是可信的服务端。

- 最终，双向 TLS 验证完成，通信建立。





### Kubectl 和 apiServer之间通信

`Kubectl` 是 Kubernetes 的命令行工具，用于与集群的 API Server 通信。它是用户和 Kubernetes 集群之间的桥梁，所有对集群的操作都是通过 `kubectl` 发出的请求实现的。以下是 `kubectl` 和 API Server 之间通信的详细讲解：



#### 通信的基础概念

**kubectl 的工作原理：**

- `kubectl` 通过 **REST API** 与 API Server 通信。
- `kubectl` 使用配置文件（通常是 **`~/.kube/config`**）来确定需要连接的 API Server 的地址、认证信息、命名空间等。



**API Server 的职责**

- API Server 是 Kubernetes 控制平面的核心组件。
- 它接收 `kubectl` 发出的 REST 请求，验证、授权请求，并将其路由到相应的控制器或 etcd 存储。



**使用的协议**

- `kubectl` 和 API Server 的通信使用 **HTTPS** 协议。
- 通信通过 **双向 TLS（mTLS）** 认证进行加密和身份验证。



#### 通信过程详解

**加载配置文件**

- `kubectl` 在运行时，会读取默认的 `~/.kube/config` 文件，加载以下信息：
  - **API Server 的地址：** 如 `https://<api-server-ip>:6443`。
  - **认证信息：** 包括客户端证书、密钥、或 Bearer Token。
  - **命名空间：** 如果未指定，默认是 `default`。
  - **上下文：** 用于选择当前集群的配置。



**认证与授权**

- **认证：**
  - `kubectl` 提供客户端证书或 Token 给 API Server。
  - API Server 使用 CA 证书（如 `/etc/kubernetes/pki/ca.crt`）验证客户端证书的合法性
  - 若验证成功，API Server 识别用户身份
- **授权**
  - API Server 根据用户身份和RBAC（Role-Based Access Control）策略，检查用户是否有权限执行该操作。

- **请求的具体处理**
  - 请求可以是 `kubectl get pods`、`kubectl apply -f deployment.yaml` 等。
  - API Server 处理流程：
    - **解析请求：** 根据请求路径和方法（如 GET、POST、DELETE）判断操作目标和类型。
    - **验证请求：** 检查请求体格式是否正确。
    - **路由请求：** 将请求转发给对应的控制器或组件（如 Scheduler、Controller Manager）。
    - **返回响应：** 返回操作结果或数据（如 Pod 列表）。
- **传输安全性**
  - 通信使用 **TLS 加密**，防止数据被窃听或篡改。
  - 双向 TLS 确保：
    - **API Server 的身份：** `kubectl` 使用 CA 证书验证 API Server 的服务端证书。
    - **kubectl 的身份：** API Server 使用 CA 验证 `kubectl` 的客户端证书。



#### 双向 TLS 实现细节

**kubectl 客户端证书：**

- 通常存储在 `~/.kube/config` 文件中，指向以下字段：
  - `client-certificate`：客户端证书路径。
  - `client-key`：客户端私钥路径。
  - `certificate-authority`：CA 证书路径，用于验证 API Server 的服务端证书。



**API Server 服务端证书：**

- 存储在 `/etc/kubernetes/pki/apiserver.crt`。
- 配置在 API Server 的启动参数中，用于对外提供 HTTPS 服务。



**交互过程**

- `kubectl` 使用自己的客户端证书与 API Server 握手，证明身份。
- API Server 使用服务端证书提供 HTTPS 服务，`kubectl` 验证其身份



#### 通信示例

**kubectl 命令：**

```bash
kubectl get pods
```

**完整通信流程：**

- **kubectl 发起请求：**
  - 请求地址：从配置文件中读取，如 `https://<api-server-ip>:6443/api/v1/pods`。
  - 请求方法：`GET`。
  - 附带认证信息（客户端证书或 Token）。
- **API Server 验证身份：**
  - 验证 `kubectl` 提供的客户端证书是否由可信 CA 签发。
  - 根据 RBAC 权限检查用户是否有 `list pods` 的权限。

- **API Server 执行操作：**
  - 查询 etcd 数据库中的 Pod 信息。
  - 格式化查询结果为 JSON。
- **API Server 返回结果：**
  - 将 JSON 数据通过 HTTPS 返回给 `kubectl`。
  - `kubectl` 格式化并在终端显示结果。



#### 配置文件示例

**`~/.kube/config` 文件：**

```yaml
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority: /etc/kubernetes/pki/ca.crt # CA 证书路径，用于验证 API Server 的服务端证书。
    server: https://<api-server-ip>:6443
  name: kubernetes
users:
- name: admin
  user:
    client-certificate: /etc/kubernetes/pki/admin.crt   # 客户端证书路径
    client-key: /etc/kubernetes/pki/admin.key
contexts:
- context:
    cluster: kubernetes
    user: admin
  name: admin@kubernetes
current-context: admin@kubernetes

```



## 实际生产中的服务版本



| 中间件        | 版本       | 是否依赖其他中间件 | 依赖中间件  | 是否支持容器化 | 是否支持Ubuntu |
| ------------- | ---------- | ------------------ | ----------- | -------------- | -------------- |
| rabbitmq      | 3.7.27     | 否                 |             | 是             | 是             |
| redis         | 5.0.14     | 否                 |             | 是             | 是             |
| nacos         | 1.4.2      | 是                 | mysql.nginx | 是             | 是             |
| tomcat        | 8.5.65     | 否                 |             | 是             | 是             |
| kafka         | 2.13_2.6.0 | 是                 | zookeeper   | 是             | 是             |
| zookeeper     | 3.8.0      | 否                 |             | 是             | 是             |
| elasticsearch | 7.10.2     | 否                 |             | 是             | 是             |
| tengine       | 2.3.3      | 否                 |             | 是             | 是             |



| 软件名称   | 软件版本        | 使用类型  | 备注         |
| ---------- | --------------- | --------- | ------------ |
| JDK/JRE    | 1.8             | 平台      | Java         |
| CEPH       | 13.2.10         | 平台/业务 | 分布式存储   |
| DOCKER     | 20.10.7         | 平台      | 镜像容器     |
| K8S        | 1.18.19         | 平台      | 容器编排     |
| KUBESPHERE | 3.1.0           | 平台      | 可视化容器   |
| HARBOR     | 2.2.0-ecobal116 | 平台      | 镜像仓库     |
| ZOOKEEPER  | 3.4.5           | 平台      | 分布式服务   |
| KAFKA      | 2.2.2           | 业务      | 队列         |
| REDIS      | 6.2.4           | 业务      | 缓存库       |
| ORACLE     | 12C及以上       | 业务      | 数据库       |
| NACOS      | 2.0.3           | 平台      | 服务配置     |
| SFTP       | /               | 业务      | 文件         |
| NGINX      | 1.18.0          | 业务      | 服务代理     |
| XX_JOB     | /               | 业务      | 任务调度平台 |



## BGP协议





## Git 相关用法补充

### 绕过 Git 的 SSL 证书验证方法



#### 临时禁用 SSL 验证（仅当前命令）

```bash
# 这个方法 仅对当前命令生效，不会影响其他 Git 操作
GIT_SSL_NO_VERIFY=true git clone http://gitlab.mygitlab.mystical.org/devops/meta.git
```



#### 全局禁用 Git SSL 证书验证

```bash
# 这会对 所有 Git 操作 关闭 SSL 验证，但并不推荐，因为可能会让你对 MITM（中间人攻击）更脆弱
git config --global http.sslVerify false
```



#### 仅对特定 GitLab 域名禁用 SSL 验证

```bash
# 只想对 gitlab.mygitlab.mystical.org 禁用 SSL 验证
git config --global http."http://gitlab.mygitlab.mystical.org".sslVerify false
```



#### 为 GitLab 添加自签证书

如果你的 GitLab 使用了自签名证书，推荐把它的 CA 证书添加到系统或 Git 的 CA 证书列表，而不是禁用 SSL 验证

**获取 GitLab 证书**

```bash
openssl s_client -showcerts -connect gitlab.mygitlab.mystical.org:443 < /dev/null | openssl x509 -outform PEM > gitlab-cert.pem
```

**把证书加入 Git 信任**

```bash
git config --global http.sslCAInfo ~/gitlab-cert.pem
```







## Kubernetes GPU 集群部署

### **最小部署方案**

| 角色                      | 机器数量 | 规格建议                                       | 说明                                |
| ------------------------- | -------- | ---------------------------------------------- | ----------------------------------- |
| **Master 节点（控制面）** | 1 台     | `ecs.c6.large`（2 vCPU 4 GiB RAM）             | 运行 K8s 控制面，不需要 GPU         |
| **GPU Worker 节点**       | 2 台     | `ecs.sgn7i-vws-m2s.xlarge`（4 vCPU 8 GiB RAM） | 运行 AI 计算任务，支持 K8s GPU 调度 |

------



### **更推荐的生产模拟方案**

如果你想要 **更接近生产环境**，建议：

- 选择 **独占型 GPU 实例**，如 `ecs.gn6e-c12g1.2xlarge`（Tesla T4 GPU）
- 增加 **多 GPU Worker 节点**，模拟实际 K8s GPU 负载均衡调度
- 使用 **阿里云 ACK（托管 K8s）**，简化管理







