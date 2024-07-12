# 容器技术入门概念
## 从进程开始

### 进程的概念
一旦“程序”被执行起来，它就从磁盘上的二进制文件，变成计算机内存中的数据，寄存器中的值，堆栈中的指令，被打开的文件，以及各种设备的状态信息的一个集合，像这样一个程序运行起来后的计算机执行环境的总和，就是进程

所以对于进程来说，它的静态表现就是程序，平常都安安静静地待在磁盘上，而一旦运行起来，它就变成了计算机里的数据和状态的总和，这就是它的动态表现

<span style="color:red;font-weight:700">容器技术的核心功能，就是通过约束和修改进程的动态表现，从而为其创造一个“边界”</span>

<span style="color:red;font-weight:700">对于Docker等大多数Linux容器来说，Cgroups技术是用来制造约束的主要手段，而Namespace技术则是用来修改进程视图的主要方法</span>

跟真实存在的虚拟机不同，在使用Docker的时候，并没有一个真正的“Docker容器”运行在宿主机里面。Docker项目帮助用户启动的，还是原来的应用进程，只不过创建这些进程时，Docker为他们加上了各种各样的Namespace参数
跟真实存在的虚拟机不同，在使用Docker的时候，并没有一个真正的“Docker容器”运行在宿主机里面。Docker项目帮助用户启动的，还是原来的应用进程，只不过创建这些进程时，Docker为他们加上了各种各样的Namespace参数

这时，这些进程就会觉得自己是各自PID Namespace里的第1号进程，只能看到各自Mount Namespace里挂载的目录和文件，只能访问到各自Network Namespace里的网络设备，就仿佛运行在一个个容器里面，与世隔绝。

## 隔离与限制
用户运行在容器里的应用进程，跟宿主机上的其他进程一样，都由宿主机操作系统统一管理，只不过这些被隔离的进程拥有额外设置过的Namespace参数。而Docker项目在这里扮演的角色，更多是旁路式的辅助和管理工作

### Docker项目比虚拟机更受欢迎的原因

容器化后的用户应用，却依然还是一个宿主机上的普通进程，这就意味着这些因为虚拟化而带来的性能损耗都是不存在的

另一方面，使用Namespace作为隔离手段的容器并不需要单独的Guest OS，这就使得容器额外的资源占用几乎可以忽略不计

#### 总结
所以说，`“敏捷”`和`“高性能”`是容器相较于虚拟机最大的优势,也是它能够在Paas这种更细粒度的资源管理平台上大行其道的重要原因

### 基于Linux Namespace的隔离机制的问题

!!`隔离的不彻底`!!
- 首先，既然容器只是运行在宿主机上的一种特殊的进程，那么多个容器之间使用的就还是同一个宿主机的操作系统内核
    - 尽管可以在容器里通过Mount Namespace单独挂载其他不同版本的操作系统文件，但是不能改变共享宿主机内核的事实，这意味着
      - 不能在Windows宿主机运行Linux容器
      - 低版本linux上不能运行高版本linux容器
      - 
- 其次，在Linux内核中，有很多资源和对象是不能被Namespace化的，最典型的例子就是`时间`

```
使用容器要考虑两个不能被隔离的资源：内核和时间
```

#### 针对隔离与性能之间平衡的解决方案

基于虚拟化或者独立内核技术的容器实现


### 容器的限制问题

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

#### Docker 使用 cgroups 的步骤

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

#### 容器是一个“单进程”模型

#### 容器的问题
众所周知，Linux 下的 /proc 目录存储的是记录当前内核运行状态的一系列特殊文件，用户可以通过访问这些文件，查看系统以及当前正在运行的进程的信息，比如 CPU 使用情况、内存占用率等，这些文件也是 top 指令查看系统信息的主要数据来源。但是，你如果在容器里执行 top 指令，就会发现，它显示的信息居然是宿主机的 CPU 和内存数据，而不是当前容器的数据。造成这个问题的原因就是，/proc 文件系统并不知道用户通过 Cgroups 给这个容器做了什么样的资源限制，即：/proc 文件系统不了解 Cgroups 限制的存在。


## 深入理解容器镜像
### 模拟容器文件系统的


### Docker项目的核心原理
为待创建的用户进程：
1. 启用Linux Namespace配置；
2. 设置指定的Cgroups参数
3. 切换进程的根目录（Change Root）


### Docker镜像
Docker在镜像的设计中，引入了层(layer)的概念，用户制作镜像的每一步操作，都会生成一个层，也就是一个增量rootfs

