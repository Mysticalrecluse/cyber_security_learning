## Kubernetes架构
Kubernetes主要分为master节点和Woker节点，其中Master节点为了高可用，至少3个
### Kubernetes组件
![alt text](images/image2.png)

Kubernetes组件分为三种
- Control Plane Components 控制平台组件(Master)
  - API Server
    - K8S内部通信的总入口
  - scheduler
  - controller-mananger
  - Etcd
- Node Components 节点组件
  - Kubelet
    - 接收从master节点发过来的指令(通过API Server)
  - Container RUNTIME(容器运行时)
    - 从kubelet接收指令，去管理容器
  - Kube_Proxy(生辰iptables规则)
    - kube-proxy 负责为 Kubernetes 服务实现负载均衡。它拦截访问服务的网络请求，并将请求转发到该服务的后端 Pod 上。
    - 它为每个服务创建一组网络规则，这些规则用于将外部或内部流量分发到与服务相关联的 Pod 上，实现负载均衡。
- Addons 附件(插件)


### Kubernetes组件间安全通信
Kubernetes集群中有三套CA机制
- etcd-ca ETCD集群内部的 TLS 通信
- kubernetes-ca kubernetes集群内部节点间的双向 TLS 通信
- front-proxy-ca Kubernetes集群与外部扩展服务简单双向 TLS 通信

### Kubernetes版本

1.24版本之后，Kubernetes不再直接支持Docker

### Kubernetes扩展接口

- 容器运行时接口(CRI：Container Runtime Interface)
  - 从Kubernetes1.5开始，CRI成为Kubernetes与容器运行时交互的标准接口，使得Kubernetes可以与各种容器运行时进行通信，从而增加了灵活性和可移植性
  - Kubernetes对于容器的解决方案，只是预留了网络接口，只要符合CNI标准的接口方案都可用
- 容器网络接口CNI(Container Network Interface)
  - Kubernetes对于网络的解决方案，只是预留了网络接口，只要符合CNI标准的解决方案都可以用
- 容器存储接口CSI：Container Storage Interface
  - Kubernetes对于存储的解决方案，只是预留了存储接口，只要符合CSI标准的解决方案都可以使用此接口，非必须

![alt text](images/image3.png)

## Kubernetes安装
- K8S集群主节点1
  - IP: 10.0.0.201
  - 主机名：master1.feng.org
- K8S集群主节点2
  - IP: 10.0.0.202
  - 主机名：master2.feng.org
- K8S集群主节点3
  - IP: 10.0.0.203
  - 主机名：master3.feng.org
- K8S集群工作节点1
  - IP: 10.0.0.204
  - 主机名：node1.feng.org
- K8S集群工作节点2
  - IP: 10.0.0.205
  - 主机名：node2.feng.org
- K8S集群工作节点3
  - IP: 10.0.0.206
  - 主机名：node3.feng.org


- 负载均衡haproxy
  - IP: 10.0.0.3
  - 主机名：ha1.feng.org
- 负载均衡haproxy2
  - IP: 10.0.0.13
  - 主机名：ha2.feng.org