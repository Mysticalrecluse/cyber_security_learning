## Kubernetes架构
Kubernetes主要分为master节点和Woker节点，其中Master节点为了高可用，至少3个
### Kubernetes组件
![alt text](images/image2.png)

Kubernetes组件分为三种
- Control Plane Components 控制平台组件(Master)
  - API Server
    - K8S内部通信的总入口
    - `API Server是Kubernetes集群中唯一能够与etcd通信的组件`
  - scheduler
  - controller-mananger
  - Etcd(集群状态存储系统，用于存储集群状态) - Node Components 节点组件
  - Kubelet
    - 接收从master节点发过来的指令(通过API Server)
    - 支持从API Server以配置清单形式接受Pod资源定义
    - 从指定本地目录中加载静态Pod清单`/etc/kubenetes/manifests`，并通过容器运行时创建、启动和监视容器
    - Kubelet会持续监视当前节点上的各Pod的健康状态，包括基于用户自定义的探针进行存活状态探测，并在任何Pod出现问题时将其重建为新实例
  - Container RUNTIME(容器运行时)
    - 从kubelet接收指令，去管理容器
  - Kube_Proxy(生成iptables规则)
    - 负载均衡：
      - kube-proxy 实现了对服务的负载均衡，将客户端的请求分发到对应的后端 Pod。
    - 服务发现：
      - kube-proxy 根据 Kubernetes API 服务器的更新，动态维护和更新集群内的网络规则，以确保服务 IP 地址和端口的正确性。
    - 网络规则管理:
      - kube-proxy 使用多种方式（如 iptables、IPVS）来管理集群节点上的网络规则，确保请求能够被正确转发
    - 它是Service资源的实现
      - 对内：ClusterIP：在集群内部访问。
      - 对外
        - NodePort
        - LoadBalancer
- Addons 附件(插件)
  - CoreDNS：


### Kubernetes组件间安全通信
Kubernetes集群中有三套CA机制
- etcd-ca ETCD集群内部的 TLS 通信
- kubernetes-ca kubernetes集群内部节点间的双向 TLS 通信(包括APIserver与Kubelet之间的安全通信，contruler和schedular之间的通信证书)
- front-proxy-ca Kubernetes集群与外部扩展服务简单双向 TLS 通信


### Kubernetes网络基础
#### 四种通信类型
- 同一Pod内的容器间通信
- 各Pod彼此间通信
- Pod与Service间的通信
- 集群外部的流量与Service之间的通信
#### 三种网络
- 节点网络（宿主机）
- Pod网络（Pod对象所属网络）
  - Pod之间的网络有CNI插件管理
- Service网络（ClusterIP,NodePort,LoadBalancer）
  - Service网络由Kubenetes分配和管理

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

### 基于kubeadm和docker安装k8s高可用集群
#### 基础系统环境设置
- 主机时间同步
- 防火墙设置
- 禁用swap
- 确保MAC地址及product_id的唯一性

#### 配置容器运行引擎
- 安装docker
- 配置cri-dockerd

#### 安装kubeadm，kubelet和kubectl

#### 初始化控制平面()

#### 配置命令行工具kubectl

#### 向集群添加master节点

#### 向集群添加worker节点

上述详情见ansible自动化脚本

### 基于containerd安装k8s高可用集群
#### 环境初始化，同上
#### 内核参数调整
```shell
# 方法1：安装docker，自动修改内核参数，并自动安装containerd
apt update && apt -y install docker.io

# 方法2：加载模块
modprobe overlay
modprobe br_netfilter

# 开机加载
cat <<EOF | tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

# 设置所需的sysctl参数，参数在重启后保持不变
cat <<EOF | tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward = 1
EOF

# 重启内核参数
sysctl --system
```
#### 安装containerd
```shell
apt install -y containerd

# 修改containerd配置
mkdir /etc/containerd
containerd config default > /etc/containerd/config.toml

# 将sandbox_image镜像源设置为阿里云google_containers镜像源
sed -i "s#registry.k8s.io/pause#registry.aliyuncs.com/google_containers/pause#g" /etc/containerd/config.toml

# 配置containerd cgroup 驱动程序systemd, ubuntu22.04较新内核必须修改，ubuntu20.04旧版内核不用改
sed -i 's#SystemdCgroup = false#SystemdCgroup = true#g' /etc/containerd/config.toml

# 镜像加速
vim /etc/containerd/config.toml
# 在行下面加行
[plugins."io.containerd.grpc.v1.cri".registry.mirrors]
       ###########################镜像加速###############################     
      #新版
  [plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]
    endpoint = ["https://docker.m.daocloud.io","https://docker.1panel.live"]

# 重启containerd
systemctl restart containerd
```

#### 在所有主机安装kubeadm、kubelet和kubectl
后续同上, 详情见ansible自动化脚本


### 基于kubeasz安装二进制k8s高可用集群
#### 部署架构
- k8s主节点1
  - IP：10.0.0.131
  - 主机名：master1.feng.org
- k8s主节点2
  - IP：10.0.0.132
  - 主机名：master2.feng.org
- k8s主节点3
  - IP：10.0.0.133
  - 主机名：master3.feng.org
- k8s-workder-node1
  - IP：10.0.0.134
  - 主机名：node1.feng.org
- k8s-workder-nodej
  - IP：10.0.0.135
  - 主机名：node2.feng.org
- k8s-workder-node6
  - IP：10.0.0.136
  - 主机名：node3.feng.org
- ansible
  - 10.0.0.131

#### 下载kubeasz
```shell
# 下载ezdown脚本
export release=3.6.4
wget https://github.com/easzlab/kubeasz/releases/download/${release}/ezdown

# 加执行权限
chmod +x ezdown
./ezdown

# 下载相关文件到/etc/kubeasz
./ezdown -D

# 环境初始化
./ezdown -S

# 创建集群的初始配置信息，指定集群名称k8s-mycluster-01
dk ezctl new k8s-mycluster-01

# 修改/etc/kubeasz/clusters/k8s-mycluster-01/hosts文件

# 执行ansible，创建k8s集群
dk ezctl setup k8s-mycluster-01 all

```


## Kubernetes资源种类
查看kubernetes资源种类
```shell
kubectl api-resources
```

## Kubernetes与集群进行交互的主要方式
### RESTful API
#### 获取所有Pod
- 请求方法：GET
- 请求URL：`/api/v1/namespaces/{namespace}/pods`
- 示例
```shell
GET /api/v1/namespace/default/pods
```

#### 创建一个新的Pod
- 请求方法：POST
- 请求URL：`/api/v1/namespace/{namespace}/pods`
```shell
POST /api/v1/namespaces/default/pods
Content-Type: application/json

{
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
    "name": "my-pod"
  },
  "spec": {
    "containers": [
      {
        "name": "my-container",
        "image": "nginx",
        "ports": [
          {
            "containerPort": 80
          }
        ]
      }
    ]
  }
}
```

#### 删除一个Pod
- 请求方法：DELETE
- 请求URL：`/api/v1/namespace/{namespace}/pods/{name}`
```shell
DELETE /api/v1/namespaces/default/pods/my-pod
```

#### 更新一个Pod
- 请求方法：PUT
- 请求URL`/api/v1/namespace/{namespace}/pods/{name}`
- 示例：更新名为`my-pod`的Pod(注意，更新Pod通常使用的是`PATCH`请求，但这里以`PUT`为例)
```shell
PUT /api/v1/namespaces/default/pods/my-pod
Content-Type: application/json

{
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
    "name": "my-pod"
  },
  "spec": {
    "containers": [
      {
        "name": "my-container",
        "image": "nginx:latest",
        "ports": [
          {
            "containerPort": 80
          }
        ]
      }
    ]
  }
}

```

## Kubectl命令和资源管理
Kubectl的核心功能在于通过API Server操作Kubernetes的各种资源对象

### kubectl的命令格式
```shell
kubectl [command] [TYPE] [NAME] [flags]
```

#### 常用操作示例
```shell
# 创建一个名称空间
kubectl create namespace dev
# 创建一个deployment控制器管理下的Pod在命名空间dev下
kubectl create deployment demoapp --image="ikubernetes/demoapp:v1.0" -n dev
# 创建一个service网络
kubectl create service clusterip demoapp -tcp=80 -n dev

# 创建自主式Pod
kubectl run demoapp --image="ikubernetes/demoapp:v1.0"

kubectl run demoapp-$RANDOM --image="ikubernetes/demoapp:v1.0" --rm -it --command -- /bin/sh
# --command -- /bin/sh
# --command 选项表示将指定的命令作为容器的入口点（entrypoint）。
# -- 用于分隔选项和命令，确保 kubectl 能够正确识别命令部分，即使命令部分包含选项。
```

#### 查看资源对象`get`


#### 打印资源对象的详细信息
每个资源对象都有用户期望的状态(spec)和现有的实际状态(Status)两种状态信息

```shell
# 查看kube-system名称空间中API Server相关Pod对象的资源配置清单，并输出为YAML格式
kubectl get pods kube-apiserver-k8s-master01.ilinux.io -o yaml -n kube-system

# 查看kube-system名称空间中拥有标签component=kube-apiserver的Pod对象的详细描述信息
kubectl describe pods -l component=kube-apiserver -n kube-system
```

#### 打印容器中的日志信息`logs`

```shell
kubectl logs ...
# -f，相当于tail -f，不多解释
```

#### 在容器中执行命令`exec`
```shell
kubectl exec kube-apiserver-master.ilinux.io -n kube-system -- ps
# 如果pod中有多个业务容器，可以用-c指定容器
```

#### 删除资源对象`delete`
```shell
# 删除Service资源对象
kubectl delete services demoapp-svc

# 删除名称空间内的某种类型对象--all
kubectl delete pods --all -n kube-public  # 如果没有--all，则是删除名称空间连同里面的所有对象

# 删除宽限期，默认30秒
kubectl delete pods demoapp --force --grance-period=0 # 立即删除
# 使用--now和--grace-period会覆盖默认宽限期
```

#### kubectl插件

显示所有kubectl插件，所有插件一定是以kubectl_开头
```shell
kubectl plugin list
```
插件管理：Krew(Krew自身也表现为kubectl的一个插件)

- 安装krew插件脚本
```shell
#!bin/bash
set -x; cd "$(mktemp) -d"

curl -fSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/krew.{gar.rz,yaml}"
tar zxvf krew.tar.gz
KREW=./krew-"$(uname | tr '[:upper:]' '[:lower:]')_amd64"

"$KREW" install --manifest=krew.yaml --archive=krew.tar.gz
"$KREW" update
```

## Kubernetes资源管理
### 工作负载型资源

### 发现与负载均衡 
#### ReplicationController(上一代无状态应用控制器，不建议使用)
- 用于确保每个Pod副本在任意时刻均能满足目标数量，即它用于保证每个容器或容器组总是运行并可访问
#### ReplicaSet
- 新一代ReplicationController，与ReplicationController唯一不同的：
  - 支持的标签选择器不同，不仅支持等值选择器，还支持基于集合的`选择器`

#### Deployment
- 用于管理无状态的持久化应用，例如HTTP服务等
- 用于为Pod和ReplicaSet提供声明式更新，是构建在ReplicaSet之上的更高级的控制器

#### StatefulSet
- 用于管理有状态的持久化应用
- 为每个Pod创建一个独有的持久性标识符，并确保各Pod间的`顺序性`

#### DaemonSet
- 用于确保每个节点都运行了某Pod的一个副本，包括后来新增的节点
- 常用于运行各类系统级守护进程

#### Job
- 用于管理运行完成后即可终止的任务，例如批处理作业任务；
- Job创建一个或多个Pod，并确保其符合目标数量，直到应用完成而终止
- `Cronjob`控制器对象，还能为Job型任务提供定期执行机制


### 发现与负载均衡
#### Service
- 用于为工作负载实例提供固定的访问入口及负载均衡服务
- 它把每个后端实例定义为`Endpoint`，简称ep

#### Ingress
- 为工作负载提供7层代理(HTTP/HTTPS)及负载均衡功能


### 配置与存储
#### ConfigMap
- 以环境变量或存储卷的方式，接入Pod资源的容器中，并可被多个同类的Pod共享引用
- 从而做到`一次修改，多处生效`

#### Secret
- 适用于存储敏感数据
- 例如：证书，私钥和密码等

#### CSI(存储)


### 集群型资源
- 用于定义集群自身的配置信息

#### 名称空间NameSpace

#### Node
- Kubernetes并不能直接管理工作节点
- 它把由管理员添加进来的任何形式的工作节点映射为一个Node资源对象(待理解)

#### Role
- 角色，隶属于名称空间，代表名称空间级别由规则组成的权限集合
- 可被`RoleBinding`引用

#### ClusterRole
- 集群角色，隶属于集群，由规则组成的权限集合
- 可被`RoleBinding`和`ClusterRoleBinding`引用

#### RoleBinding
- 用于将Role中的许可权限绑定在一个或一组用户上，从而完成用户授权
- 仅作用于名称空间级别

#### Clusterole
- 同上，但是是集群级别


### 元数据型资源
此类资源对象用于为集群内部其他资源对象配置其行为或特性

#### Pod模版

#### LimitRange