# Docker
## 名称空间Namespace技术

namespace是Linux系统的底层概念。在Linux内核实现，即有一些不同类型的命名空间被部署在内核，各个`docker容器`运行在同一个`docker主进程`并且共用同一个宿主机系统内核，各docker容器运行在宿主机的用户空间，每个容器都有类似于虚拟机一样的相互隔离的运行空间，但是容器技术是`在一个进程内`实现运行指定服务的运行环境，并且还可以保护宿主机内核不受其他进程的干扰和影响，如文件系统空间，网络空间，进程空间等，目前主要通过以下技术实现容器运行空间的相互隔离

隔离类型
- MNT Namespace(mount)
  - 功能：提供磁盘挂载和文件系统的隔离能力
  - 系统调用参数：CLONE_NEWNS
- IPC Namespace(inter-Process Communication)
  - 功能：提供进程间通信的隔离能力，包括信号量，消息队列和共享内存
- UTS Namespace(UNIX Timesharing System)
  - 功能：提供内核，主机名和域名隔离能力
- PID Namespace(Process Identification)
  - 功能：提供进程隔离能力
- Net Namespace(network)
  - 功能：提供网络隔离能力，包括网络设备，网络栈，端口等
- User Namespace(user)
  - 功能：提供用户隔离能力，包括用户和组

## Control groups

Cgroups最主要的作用，就是限制一个进程组能够使用的资源上限，包括CPU，内存，磁盘，网络带宽等等。此外，还能够对进程进行优先级设置，资源的计量以及资源的控制（比如：将进程挂起和恢复等操作）


## 容器管理工具
![alt text](images/image7.png)
### nerdctl 
nerdctl是与Docker兼容的CLI for Containerd，其支持Compose

### docker


### ctr
ctr是由containerd提供的一个客户端工具

### podman
Podman即Pod Manager tool，从名称上可以看出和kubernets的pod的密切联系，

Podman是一个为Kubernetes而生的开源的容器管理工具，可在大多数Linux平台上使用，它是一种无守护程序的容器引擎，用于在Linux系统上开发，管理和运行任何符合Open Container Initiative(OCI)标准的容器和容器镜像。

### Podman和docker不同之处
- docker需要在系统上运行一个守护进程(docker daemon)，这会产生一定的开销，而podman不需要
- 启动容器的方式不同
  - Docker：
    - `docker cli`命令通过API跟`Docker Engine(引擎)`交互告诉它我想创建一个container
    - `Docker Engine`调用`OCI container runtime(runc)`来启动一个container。
    - 这代表container的process(进程)不会是`Docker CLI`的`child process`(子进程)，而是`Docker Engine`的`child process`
  - Podman:
    - 直接给OCI container runtime（runc）进行交互来创建container,所以`container process`直接是`podman`的`child process`

- docker在linux上作为守护进程运行扼杀了容器社区的创新。如果要更改容器的工作方式，则需要更改docker守护程序并将这些更改推送到上游
- 没有守护进程，容器基础结构更加模块化，更容易进行更改。podman的无守护进程架构更加灵活和安全

