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


## Pod资源
### Pod资源分类
- 自主式Pod
- 由Workload Controller管控的Pod
- 静态Pod

### 自主式Pod支持三种方法创建
#### 指令式命令创建Pod
通过kubectl命令行工具指令选项创建Pod，适合临时工作
```shell
kubectl run NAME --image=image [--port=port]
# 这里--port仅是声明要暴露的端口

# 删除pod
kubectl delete pod NAME --grace-period=5
# 立即删除
kubectl delete pod NAME --grace-period=0 --force
```

### Pod资源清单说明
#### Pod资源清单必须存在的属性
- apiVersion
  - 这里指的是K8S API的版本，目前是基于V1的，可以通过`kubectl api-versions`查询

- kind
  - 这里指的是yaml文件定义的资源类型和橘色，比如我们创建一个Pod，他就是pod类型，如果创建的是一个deployment，就是deployment类型

- metadata
  - 元数据对象，固定值就写metadata，也就意味着，这个字段对象里面写的是他的一些元数据类型，这个对象类型主要有两个字段
    - metadata.name
    - metadata.namespace

- spec
  - 这里写的是spec对象的容器列表定义，是一个列表
    - 第一个主要元素name
    - 第二个主要元素image

## Pod生命周期
### init container
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  initContainers:
  - name: init-container-1
    image: busybox
    command: ['sh', '-c', 'echo Init Container 1; sleep 5']
  - name: init-container-2
    image: busybox
    command: ['sh', '-c', 'echo Init Container 2; sleep 5']
  containers:
  - name: app-container
    image: myapp:latest
    ports:
    - containerPort: 80
```

- 在Pod的生命周期内，首先启动Pause容器以提供基础环境，然后按顺序启动init Container执行初始化任务，最后启动业务容器以运行应用程序

### 两种钩子PostStart和PreStop
- 关于钩子函数的执行主要由两种方式
  - Exec，在钩子事件触发时，直接在当前容器中运行由用户定义的命令，用于执行一段特定的命令，不过要注意的是该命令消耗的资源会被计入容器
  - HTTP，在当前容器中向某URL发起HTTP请求

#### poststart示例
```yaml
[root@master1 yaml]#cat pod-poststart.yaml
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
```

PostStart钩子函数和主容器启动可以看作是同时进行

#### PreStop示例
```yaml
#由于默认情况下，删除的动作和日志我们都没有办法看到，那么我们这里采用一种间接的方法，在删除动作之前，给本地目录创建第一个文件，输入一些内容
[root@master1 yaml]#cat pod-prestop.yaml
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
         command: ['/bin/sh', '-c','echo lifecycle poststart at $(date) > /tmp/poststart.log']
```

```yaml
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
    image: buxybox-1.32.0
    volumeMounts:
    - name: vol-prestop
      mountPath: /tmp
    command: ['sh', '-c', 'echo The app is running at $(date) ! && sleep 3600']
    lifecycle:
      postStart:
        exec:
          command: ['/bin/sh', '-c', 'echo Lifecycle poststart at $(date)' > /tmp/poststart.log]
      preStop:
        exec:
          command: ['/bin/sh', '-c', 'echo Lifecycle poststart at $(date)' > /tmp/poststart.log]
```


## Pod资源限制
### 可限制资源单位
- CPU
  - 在Kubernetes中，通常以千分之一的CPU(core)为最小单元，用毫m表示，即一个CPU核心表示1000m
- 内存

### 资源限制实现
要实现资源限制，需要先安装metrics-server
```shell
curl -LO https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.7.1/components.yaml

# 默认文件需要修改
apiVersion: apps/v1
kind: Deployment
metadata:
labels:
  k8s-app: metrics-server
name: metrics-server
namespace: kube-system
spec:
selector:
  matchLabels:
  k8s-app: metrics-server
strategy:
  rollingUpdate:
  maxUnavailable: 0
template:
  metadata:
  labels:
    k8s-app: metrics-server
  spec:
  containers:
  - args:
    - --cert-dir=/tmp
    - --secure-port=4443
    - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
    - --kubelet-use-node-status-port
    - --metric-resolution=15s
    - --kubelet-insecure-tls   #添加本行和下面两行
    image: registry.cn-hangzhou.aliyuncs.com/google_containers/metrics-server:v0.7.1  # 或者开代理
 #image: registry.cn-hangzhou.aliyuncs.com/google_containers/metrics-server:v0.6.1
 #image: k8s.gcr.io/metrics-server/metrics-server:v0.6.1
 imagePullPolicy: IfNotPresent
 livenessProbe:

# 应用此文件
kubectl apply -f components.yaml
# 查看性能性能
kubectl top nodes
```

### 资源限制
```yaml
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
       memory: "200Mi"
       cpu: "500m"
     limits:
       memory: "200Mi"
       cpu: "500m"
```
提示：为保证性能，生产推荐Requests和Limits设置为相同的值
limit数值可以超过实际大小，但是requests不可以
- 如果requests的数值大小，没有任何节点可以满足，则调度器无法完成调度，则会卡在pending状态，详情可以查看pod创建流程

- 如果限制资源后，无法满足容器实际所需的资源大小，则会触发OOMkilled，在OOMKILLED和重启之间反复循环


#### LimitRange实现使用资源限制
后续有时间可以了解


## Pod安全

### 容器安全上下文
安全上下文是一组用于决定容器是如何创建和运行的约束条件，它们代表着创建和运行容器时使用的运行时参数

它根据约束的作用范围主要包括三个级别：
- Pod级别
  - 针对Pod范围内的所有容器
- 容器级别
  - 仅针对Pod范围内的指定容器
- PSP级别
  - PodSecurityPolicy，全局级别的Pod安全策略，涉及到准入控制相关的知识

### 资源策略
#### 用户级别
默认Pod容器进程是以root身份运行，可以通过下面属性指定其他用户
- runAsUser
- runAsGroup

默认情况下，一旦Pod创建好后，是不允许对用户归属权限进行任意修改的，所以需要修改的话，必须先关闭，在开启

添加安全上下文属性实现指定用户身份运行Pod内的进程
```yaml
[root@master1 yaml]#cat pod-securitycontext-runasuser.yaml 
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
     runAsUser: 1001     #指定运行身份
     runAsGroup: 1001
# 注意，普通用户无法监控特权端口0~1023
```
- 扩展知识
```shell
# 内核中有个参数可以控制特权端口的范围
sysclt -a | grep net.ipv4.ip_unprivileged_port_start
net.ipv4.ip_unprivileged_port_start=0
# 有的容器该参数默认为0，则即使是普通用户也能监控特权端口
```

#### 资源能力
Linux中相关的资源能力
```shell
CAP_CHOWN           # 改变文件的所有者和所属组
CAP_MKNOD           # mknod()，创建设备文件
CAP_NET_ADMIN       # 网络管理权限
CAP_SYS_TIME        # 更改系统的时钟
CAP_SYS_MODULE      # 装载卸载内核模块
CAP_NET_BIND_SERVER # 允许普通用户绑定1024以内的特权端口
CAP_SYS_ADMIN       # 大部分的管理权限，基本相当于root权限
```

可以在容器内部通过command+args运行一个自定义的容器启动命令
```yaml
# [root@master1 yaml]#cat pod-securitycontext-capabilities.yaml 
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
   command: ["/bin/sh","-c"]
   args: ["/sbin/iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80 && /usr/bin/python3 /usr/local/bin/demo.py"]
```

通过add添加特权
```yaml
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
   command: ["/bin/sh","-c"]
   args: ["/sbin/iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT -
-to-port 80 && /usr/bin/python3 /usr/local/bin/demo.py"]
#添加下面三行
   securityContext:
     capabilities:
       add: ['NET_ADMIN']
       drop: ['CHOWN']

# 注意add后面的权限能力使用单引号('')，也可以使用双引号("")
# drop可以删除特权
```

#### Pod中的内核参数
Pod安全上下文级别默认只支持为数不多的内核安全参数
```shell
net.ipv4.ip_local_port_range
net.ipv4.ip_unprivileged_port_start
net.ipv4.tcp_syncookies
kernel.shm_rmid_forced
```

上面的几个内核参数可以在Pod内部的容器名称空间的内核级别进行调整，被视为安全参数
但其他的绝大部分参数不支持直接修改，被视为不安全参数
如果想对其他不安全内核参数修改，必须要所在的node节点上修改kubelet的配置
```shell
KUBELET_EXTRA_ARGS='--allowed-unsafe-sysctls=net.core.somaxconn,net.ipv4.ip_nonlocal_bind'
```
示例
```yaml
apiVersion: v1
kind: Pod
metadata:
 name: pod-sysctl
spec:
 securityContext:
   sysctls:
      - name: kernel.shm_rmid_forced
       value: "1"
      - name: net.ipv4.ip_unprivileged_port_start
       value: "60"
    # - name: net.core.somaxconn
    #   value: "6666"
 containers:
  - name: pod-sysctl
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   securityContext:
     runAsUser: 1001
     runAsGroup: 1001
```


#### 特权
添加privileged特权
```yaml
apiVersion: v1
kind: Pod
metadata:
 name: pod-privileged-demo
spec:
 initContainers:  
  - name: set-sysctl
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/admin-box:v0.1
   command: ["sysctl","-w","vm.max_map_count=6666666"]
   securityContext:         #添加特权
     privileged: true
 containers:
  - name: pod-privileged-demo
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
```

#### 服务质量分类
QoS(服务质量等级)是作用在Pod上的一个配置
当Kubernetes创建一个Pod时，它就会给这个Pod分配一个Qos等级
- 低优先级BestEffort：没有任何一个容器设置了requests或limits属性(最低优先级)
- 中优先级Burstable: Pod至少有一个容器设置了CPU或内存的requests和limits，且不相同
- 高优先级Guaranteed：Pod内的每一个容器同时设置了CPU和内存的requests和limits，而且所有值必须相等

当主机出现OOM时，先删除服务质量低的, 服务质量高的最后删除


## 单节点多容器模式
### Init Container模式
```yaml
#通过init模式实现iptables规则的端口重定向
[root@master1 yaml]#cat pod-init-container.yaml 
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
   command: ['/bin/sh','-c']
   args: ['iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80']
   securityContext:
capabilities:
       add:
        - NET_ADMIN
 containers:
  - name: demo
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   imagePullPolicy: IfNotPresent
   ports:
    - name: http
     containerPort: 80
```

### sideCar模式
在一个pod内启动两个容器，访问B容器的时候，都需要经过A容器，只有通过A处理后的数据才会发送给B容器。
在整个过程中，A容器就是B容器应用的代理服务器
```yaml
apiVersion: v1
kind: Pod
metadata:
 name: sidecar-test
spec:
 containers:
  - name: proxy
   image: envoyproxy/envoy-alpine:v1.14.1
   command: ['sh', '-c', 'sleep 5 && envoy -c /etc/envoy/envoy.yaml']
   lifecycle:
     postStart:
       exec:
         command: ["/bin/sh","-c","wget -O /etc/envoy/envoy.yaml 
http://www.wangxiaochun.com/kubernetes/yaml/envoy.yaml"]
  - name: pod-test
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   env:
    - name: HOST
     value: "127.0.0.1"
    - name: PORT
     value: "8080"
```
这里设计云原生的envoy组件，有时间可以学习下


## Pod健康性检查

### Pod中的健康检查流程
- 初始启动容器的时候，有一个初始化时间（InitialDelaySeconds，可自定义，如5s）
- 5s后启动第一个探针，`Startup Probe`，初始化时间是为了确保程序已经运行，因为有些程序启动可能较慢，`Startup Probe`一般在服务启动后探测
- Startup Probe如果探测失败，容器将立即重启
- Startup Probe探测成功后，进入下一阶段，此时Startup Probe将不会再执行
- 在该阶段初始也会有一个`InitalDelaySceonds for Livness Probe`和`InitalDelaySceonds for Readiness Probe`即启动后续探针的等待时间
- 后续有两个探针：Livness Probe和Readiness Probe
- 如果Livness检测失败，则重启Pod
- 如果Readiness检查失败，Pod不会重启，而是会将其从SerVice资源的端点控制器中的调度列表移除，待后续检查成功，在将其从调度列表恢复


### Pod健康性检查的方法
- Exec探测方法
- TCPSocket探测方法
- HTTPGET探测方法
- gRPC探测方法

### 探针案例
#### Exec方式案例

```yaml
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
       command: ['/bin/sh', '-c', '[ "$(curl -s 127.0.0.1/livez)" == "OK" ]']
     initialDelaySeconds: 60
     timeoutSeconds: 1
     periodSeconds: 5
     successThreshold: 1
     failureThreshold: 1
```

```yaml
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
   command: ["/bin/sh","-c","touch /tmp/healthy; sleep 3; rm -f 
/tmp/healthy;sleep 3600"]
   livenessProbe:
     exec:
       command: ["test", "-e","/tmp/healthy"]
     initialDelaySeconds: 1
     periodSeconds: 3
```

#### Tcpsocket方式案例
使用此配置，kubelet将尝试在指定端口上打开容器的套接字，如果可以建立连接，则容器被认为是健康的，如果不能则认为是失败的，其实就是在检查端口是否开启
```yaml
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
    - name: http           #给指定端口定义别名
     containerPort: 80
   securityContext:  #添加特权，否则添加iptables规则会提示：getsockopt failed strangely: Operation not permitted
     capabilities:
       add:
        - NET_ADMIN
   livenessProbe:
     tcpSocket:
       port: http        #引用上面端口的定义
     periodSeconds: 5
     initialDelaySeconds: 5
#注意：由于此镜像应用对外暴露的端口是80端口，所以要探测80端口
```

Readness的Tcpsocket探针
```yaml
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
   app: pod-readiness-tcpsocket  #指定上面Pod相同的标签
```


#### HTTPGET方式案例
HTTP探测通过对容器内容开放的Web服务，进行http方法的请求探测，如果探测成功（即响应码为2XX,3XX），否则就失败

HTTP Probes允许针对httpGet配置额外的字段
```shell
host：连接使用的主机名，默认是 Pod 的 IP。也可以在 HTTP 头中设置 “Host” 来代替。一般不配置此
项
scheme ：用于设置连接主机的方式（HTTP 还是 HTTPS）。默认是 "HTTP"。一般不配置此项
path：访问 HTTP 服务的路径。默认值为 "/"。一般会配置此项
port：访问容器的端口号或者端口名。如果数字必须在 1～65535 之间。一般会配置此项
httpHeaders：请求中自定义的 HTTP 头。HTTP 头字段允许重复。一般不配置此项
```
```yaml
# [root@master1 yaml]#cat pod-liveness-http.yaml 
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
       port: http    #或者指定80，如果非标准端口可以指定端口号
       path: /index.html
     initialDelaySeconds: 1
     periodSeconds: 3
```

## 工作负载
### 工作负载资源分类
- 无状态应用编配
  - Deployment
  - ReplicaSet
- 有状态应用编排
  - StatefulSet
- 系统级应用
  - DaemonSet
- 工作类应用
  - Job
  - CronJOb

### 标签（键值对）
#### 查看标签
```shell
kubectl pod --show-labels
kubectl <资源类型> --show-labels
```
#### 添加标签
```shell
# kubectl label <资源对象> <对象名称> <key1> <value1> <key2> <value2>...
kubectl label pod myapp class=m58 title=k8s
```

#### 更改原有标签
```shell
kubectl label pod myapp class=m59 title=k8s --overwrite=true
```

#### 删除标签
```shell
kubectl label 资源类型 资源名称 label_name- [label_name]-...
kubectl label pod myapp title-
```

#### Yaml方法
```yaml
metadata:
  labels:
    key1: value1
    key2: value2
    ...
# 注意：labels复数
```

### 标签选择器 Label Selector
Label附加到Kubernetes集群中的各种资源对象上，目的是对这些资源对象可以进行后续的分组管理
而分组管理的核心就是：`标签选择器Label Selector`

#### 等值匹配
```shell
# 等值
name = nginx
name == nginx
name            # 表示匹配存在name标签的资源对象

# 不等值
！name          # 表示匹配不存在name标签的资源对象
name != nginx   # 匹配所有没有name标签或者标签name的值不等于nginx的资源对象
```

应用示例
```yaml
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
   accelerator: nvidia-tesla-p100
```

应用示例2
```yaml
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

#### 集合匹配
```shell
# 集合匹配相当于“或”
#示例：
env in (dev, test)        #匹配所有具有标签 env = dev 或者 env = test 的资源对象
name notin (frontend,backent)    #匹配所有不具有标签name=frontend或者name=backend或者没有name标签的资源对象
```

#### 匹配标签matchLabels
```shell
#匹配标签：
   matchLabels:
     name: nginx
     app: myapp
#当 matchLabels 中有多个标签时，它们之间的关系是逻辑与（AND）关系
#如下所示：
matchLabels:
 app: frontend
 environment: production
#那么只有那些标签中同时包含 app=frontend 和 environment=production 的资源才会被选中。
```
#### 匹配表达式
```shell
#匹配表达式：
   matchExpressions:
      - {key: name, operator: NotIn, values: [frontend]}
#当 matchExpressions 中包含多个标签表达式时，它们之间的关系是逻辑与（AND）关系
#常见的operator操作属性值有：
   In、NotIn、Exists、NotExists等
   Exists和NotExist时，values必须为空，即 { key: environment, opetator: Exists,values:}
#注意：这些表达式一般应用在RS、RC、Deployment等其它管理对象中。
```

```yaml
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

### 标签选择器操作方式
- 命令
- 文件

#### 命令方式
```shell
#多个SELECTOR表示并且的关系
kubectl get TYPE -l SELECTOR1[,SELECTOR2,...]
kubectl get TYPE -l SELECTOR1 [-l SELECTOR2] ...
#额外针对指定的每一个标签单独一列来显示对应的值
kubectl get TYPE -L label_name
```