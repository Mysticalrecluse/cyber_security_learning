## kubernetes架构
kubernetes主要分为master节点和woker节点，其中master节点为了高可用，至少3个
### kubernetes组件
![alt text](images/image2.png)

kubernetes组件分为三种
- control plane components 控制平台组件(master)
  - api server
    - k8s内部通信的总入口
    - `api server是kubernetes集群中唯一能够与etcd通信的组件`
  - scheduler
  - controller-mananger
  - etcd(集群状态存储系统，用于存储集群状态) - node components 节点组件
  - kubelet
    - 接收从master节点发过来的指令(通过api server)
    - 支持从api server以配置清单形式接受pod资源定义
    - 从指定本地目录中加载静态pod清单`/etc/kubenetes/manifests`，并通过容器运行时创建、启动和监视容器
    - kubelet会持续监视当前节点上的各pod的健康状态，包括基于用户自定义的探针进行存活状态探测，并在任何pod出现问题时将其重建为新实例
  - container runtime(容器运行时)
    - 从kubelet接收指令，去管理容器
  - kube_proxy(生成iptables规则)
    - 负载均衡：
      - kube-proxy 实现了对服务的负载均衡，将客户端的请求分发到对应的后端 pod。
    - 服务发现：
      - kube-proxy 根据 kubernetes api 服务器的更新，动态维护和更新集群内的网络规则，以确保服务 ip 地址和端口的正确性。
    - 网络规则管理:
      - kube-proxy 使用多种方式（如 iptables、ipvs）来管理集群节点上的网络规则，确保请求能够被正确转发
    - 它是service资源的实现
      - 对内：clusterip：在集群内部访问。
      - 对外
        - nodeport
        - loadbalancer
- addons 附件(插件)
  - coredns：


### kubernetes组件间安全通信
kubernetes集群中有三套ca机制
- etcd-ca etcd集群内部的 tls 通信
- kubernetes-ca kubernetes集群内部节点间的双向 tls 通信(包括apiserver与kubelet之间的安全通信，contruler和schedular之间的通信证书)
- front-proxy-ca kubernetes集群与外部扩展服务简单双向 tls 通信


### kubernetes网络基础
#### 四种通信类型
- 同一pod内的容器间通信
- 各pod彼此间通信
- pod与service间的通信
- 集群外部的流量与service之间的通信
#### 三种网络
- 节点网络（宿主机）
- pod网络（pod对象所属网络）
  - pod之间的网络有cni插件管理
- service网络（clusterip,nodeport,loadbalancer）
  - service网络由kubenetes分配和管理

### kubernetes版本

1.24版本之后，kubernetes不再直接支持docker

### kubernetes扩展接口

- 容器运行时接口(cri：container runtime interface)
  - 从kubernetes1.5开始，cri成为kubernetes与容器运行时交互的标准接口，使得kubernetes可以与各种容器运行时进行通信，从而增加了灵活性和可移植性
  - kubernetes对于容器的解决方案，只是预留了网络接口，只要符合cni标准的接口方案都可用
- 容器网络接口cni(container network interface)
  - kubernetes对于网络的解决方案，只是预留了网络接口，只要符合cni标准的解决方案都可以用
- 容器存储接口csi：container storage interface
  - kubernetes对于存储的解决方案，只是预留了存储接口，只要符合csi标准的解决方案都可以使用此接口，非必须

![alt text](images/image3.png)

## kubernetes安装
- k8s集群主节点1
  - ip: 10.0.0.201
  - 主机名：master1.feng.org
- k8s集群主节点2
  - ip: 10.0.0.202
  - 主机名：master2.feng.org
- k8s集群主节点3
  - ip: 10.0.0.203
  - 主机名：master3.feng.org
- k8s集群工作节点1
  - ip: 10.0.0.204
  - 主机名：node1.feng.org
- k8s集群工作节点2
  - ip: 10.0.0.205
  - 主机名：node2.feng.org
- k8s集群工作节点3
  - ip: 10.0.0.206
  - 主机名：node3.feng.org


- 负载均衡haproxy
  - ip: 10.0.0.3
  - 主机名：ha1.feng.org
- 负载均衡haproxy2
  - ip: 10.0.0.13
  - 主机名：ha2.feng.org

### 基于kubeadm和docker安装k8s高可用集群
#### 基础系统环境设置
- 主机时间同步
- 防火墙设置
- 禁用swap
- 确保mac地址及product_id的唯一性

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
cat <<eof | tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
eof

# 设置所需的sysctl参数，参数在重启后保持不变
cat <<eof | tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward = 1
eof

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
sed -i 's#systemdcgroup = false#systemdcgroup = true#g' /etc/containerd/config.toml

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
  - ip：10.0.0.131
  - 主机名：master1.feng.org
- k8s主节点2
  - ip：10.0.0.132
  - 主机名：master2.feng.org
- k8s主节点3
  - ip：10.0.0.133
  - 主机名：master3.feng.org
- k8s-workder-node1
  - ip：10.0.0.134
  - 主机名：node1.feng.org
- k8s-workder-nodej
  - ip：10.0.0.135
  - 主机名：node2.feng.org
- k8s-workder-node6
  - ip：10.0.0.136
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
./ezdown -d

# 环境初始化
./ezdown -s

# 创建集群的初始配置信息，指定集群名称k8s-mycluster-01
dk ezctl new k8s-mycluster-01

# 修改/etc/kubeasz/clusters/k8s-mycluster-01/hosts文件

# 执行ansible，创建k8s集群
dk ezctl setup k8s-mycluster-01 all

```


## kubernetes资源种类
查看kubernetes资源种类
```shell
kubectl api-resources
```

## kubernetes与集群进行交互的主要方式
### restful api
#### 获取所有pod
- 请求方法：get
- 请求url：`/api/v1/namespaces/{namespace}/pods`
- 示例
```shell
get /api/v1/namespace/default/pods
```

#### 创建一个新的pod
- 请求方法：post
- 请求url：`/api/v1/namespace/{namespace}/pods`
```shell
post /api/v1/namespaces/default/pods
content-type: application/json

{
  "apiversion": "v1",
  "kind": "pod",
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
            "containerport": 80
          }
        ]
      }
    ]
  }
}
```

#### 删除一个pod
- 请求方法：delete
- 请求url：`/api/v1/namespace/{namespace}/pods/{name}`
```shell
delete /api/v1/namespaces/default/pods/my-pod
```

#### 更新一个pod
- 请求方法：put
- 请求url`/api/v1/namespace/{namespace}/pods/{name}`
- 示例：更新名为`my-pod`的pod(注意，更新pod通常使用的是`patch`请求，但这里以`put`为例)
```shell
put /api/v1/namespaces/default/pods/my-pod
content-type: application/json

{
  "apiversion": "v1",
  "kind": "pod",
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
            "containerport": 80
          }
        ]
      }
    ]
  }
}

```

## kubectl命令和资源管理
kubectl的核心功能在于通过api server操作kubernetes的各种资源对象

### kubectl的命令格式
```shell
kubectl [command] [type] [name] [flags]
```

#### 常用操作示例
```shell
# 创建一个名称空间
kubectl create namespace dev
# 创建一个deployment控制器管理下的pod在命名空间dev下
kubectl create deployment demoapp --image="ikubernetes/demoapp:v1.0" -n dev
# 创建一个service网络
kubectl create service clusterip demoapp -tcp=80 -n dev

# 创建自主式pod
kubectl run demoapp --image="ikubernetes/demoapp:v1.0"

kubectl run demoapp-$random --image="ikubernetes/demoapp:v1.0" --rm -it --command -- /bin/sh
# --command -- /bin/sh
# --command 选项表示将指定的命令作为容器的入口点（entrypoint）。
# -- 用于分隔选项和命令，确保 kubectl 能够正确识别命令部分，即使命令部分包含选项。
```

#### 查看资源对象`get`


#### 打印资源对象的详细信息
每个资源对象都有用户期望的状态(spec)和现有的实际状态(status)两种状态信息

```shell
# 查看kube-system名称空间中api server相关pod对象的资源配置清单，并输出为yaml格式
kubectl get pods kube-apiserver-k8s-master01.ilinux.io -o yaml -n kube-system

# 查看kube-system名称空间中拥有标签component=kube-apiserver的pod对象的详细描述信息
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
# 删除service资源对象
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
插件管理：krew(krew自身也表现为kubectl的一个插件)

- 安装krew插件脚本
```shell
#!bin/bash
set -x; cd "$(mktemp) -d"

curl -fslo "https://github.com/kubernetes-sigs/krew/releases/latest/download/krew.{gar.rz,yaml}"
tar zxvf krew.tar.gz
krew=./krew-"$(uname | tr '[:upper:]' '[:lower:]')_amd64"

"$krew" install --manifest=krew.yaml --archive=krew.tar.gz
"$krew" update
```

## kubernetes资源管理
### 工作负载型资源

### 发现与负载均衡 
#### replicationcontroller(上一代无状态应用控制器，不建议使用)
- 用于确保每个pod副本在任意时刻均能满足目标数量，即它用于保证每个容器或容器组总是运行并可访问
#### replicaset
- 新一代replicationcontroller，与replicationcontroller唯一不同的：
  - 支持的标签选择器不同，不仅支持等值选择器，还支持基于集合的`选择器`

#### deployment
- 用于管理无状态的持久化应用，例如http服务等
- 用于为pod和replicaset提供声明式更新，是构建在replicaset之上的更高级的控制器

#### statefulset
- 用于管理有状态的持久化应用
- 为每个pod创建一个独有的持久性标识符，并确保各pod间的`顺序性`

#### daemonset
- 用于确保每个节点都运行了某pod的一个副本，包括后来新增的节点
- 常用于运行各类系统级守护进程

#### job
- 用于管理运行完成后即可终止的任务，例如批处理作业任务；
- job创建一个或多个pod，并确保其符合目标数量，直到应用完成而终止
- `cronjob`控制器对象，还能为job型任务提供定期执行机制


### 发现与负载均衡
#### service
- 用于为工作负载实例提供固定的访问入口及负载均衡服务
- 它把每个后端实例定义为`endpoint`，简称ep

#### ingress
- 为工作负载提供7层代理(http/https)及负载均衡功能


### 配置与存储
#### configmap
- 以环境变量或存储卷的方式，接入pod资源的容器中，并可被多个同类的pod共享引用
- 从而做到`一次修改，多处生效`

#### secret
- 适用于存储敏感数据
- 例如：证书，私钥和密码等

#### csi(存储)


### 集群型资源
- 用于定义集群自身的配置信息

#### 名称空间namespace

#### node
- kubernetes并不能直接管理工作节点
- 它把由管理员添加进来的任何形式的工作节点映射为一个node资源对象(待理解)

#### role
- 角色，隶属于名称空间，代表名称空间级别由规则组成的权限集合
- 可被`rolebinding`引用

#### clusterrole
- 集群角色，隶属于集群，由规则组成的权限集合
- 可被`rolebinding`和`clusterrolebinding`引用

#### rolebinding
- 用于将role中的许可权限绑定在一个或一组用户上，从而完成用户授权
- 仅作用于名称空间级别

#### clusterole
- 同上，但是是集群级别


### 元数据型资源
此类资源对象用于为集群内部其他资源对象配置其行为或特性

#### pod模版

#### limitrange


## pod资源
### pod资源分类
- 自主式pod
- 由workload controller管控的pod
- 静态pod

### 自主式pod支持三种方法创建
#### 指令式命令创建pod
通过kubectl命令行工具指令选项创建pod，适合临时工作
```shell
kubectl run name --image=image [--port=port]
# 这里--port仅是声明要暴露的端口

# 删除pod
kubectl delete pod name --grace-period=5
# 立即删除
kubectl delete pod name --grace-period=0 --force
```

### pod资源清单说明
#### pod资源清单必须存在的属性
- apiversion
  - 这里指的是k8s api的版本，目前是基于v1的，可以通过`kubectl api-versions`查询

- kind
  - 这里指的是yaml文件定义的资源类型和橘色，比如我们创建一个pod，他就是pod类型，如果创建的是一个deployment，就是deployment类型

- metadata
  - 元数据对象，固定值就写metadata，也就意味着，这个字段对象里面写的是他的一些元数据类型，这个对象类型主要有两个字段
    - metadata.name
    - metadata.namespace

- spec
  - 这里写的是spec对象的容器列表定义，是一个列表
    - 第一个主要元素name
    - 第二个主要元素image

## pod生命周期
### init container
```yaml
apiversion: v1
kind: pod
metadata:
  name: example-pod
spec:
  initcontainers:
  - name: init-container-1
    image: busybox
    command: ['sh', '-c', 'echo init container 1; sleep 5']
  - name: init-container-2
    image: busybox
    command: ['sh', '-c', 'echo init container 2; sleep 5']
  containers:
  - name: app-container
    image: myapp:latest
    ports:
    - containerport: 80
```

- 在pod的生命周期内，首先启动pause容器以提供基础环境，然后按顺序启动init container执行初始化任务，最后启动业务容器以运行应用程序

### 两种钩子poststart和prestop
- 关于钩子函数的执行主要由两种方式
  - exec，在钩子事件触发时，直接在当前容器中运行由用户定义的命令，用于执行一段特定的命令，不过要注意的是该命令消耗的资源会被计入容器
  - http，在当前容器中向某url发起http请求

#### poststart示例
```yaml
[root@master1 yaml]#cat pod-poststart.yaml
apiversion: v1
kind: pod
metadata:
 name: pod-poststart
spec:
 containers:
  - name: busybox
   image: busybox:1.32.0
   lifecycle:
     poststart:
       exec:
         command: ["/bin/sh","-c","echo lifecycle poststart at $(date) > /tmp/poststart.log"]
   command: ['sh', '-c', 'echo the app is running at $(date) ! && sleep 3600']
```

poststart钩子函数和主容器启动可以看作是同时进行

#### prestop示例
```yaml
#由于默认情况下，删除的动作和日志我们都没有办法看到，那么我们这里采用一种间接的方法，在删除动作之前，给本地目录创建第一个文件，输入一些内容
[root@master1 yaml]#cat pod-prestop.yaml
apiversion: v1
kind: pod
metadata:
 name: pod-prestop
spec:
 volumes:
  - name: vol-prestop
   hostpath:
     path: /tmp
 containers:
  - name: prestop-pod-container
   image: busybox:1.32.0
   volumemounts:
    - name: vol-prestop
     mountpath: /tmp
   command: ['sh', '-c', 'echo the app is running at $(date) ! && sleep 3600']
   lifecycle:
     poststart:
       exec:
         command: ['/bin/sh', '-c','echo lifecycle poststart at $(date) > /tmp/poststart.log']
```

```yaml
apiversion: v1
kind: pod
metadata:
  name: pod-prestop
spec:
  volumes:
  - name: vol-prestop
    hostpath:
      path: /tmp
  containers:
  - name: prestop-pod-container
    image: buxybox-1.32.0
    volumemounts:
    - name: vol-prestop
      mountpath: /tmp
    command: ['sh', '-c', 'echo the app is running at $(date) ! && sleep 3600']
    lifecycle:
      poststart:
        exec:
          command: ['/bin/sh', '-c', 'echo lifecycle poststart at $(date)' > /tmp/poststart.log]
      prestop:
        exec:
          command: ['/bin/sh', '-c', 'echo lifecycle poststart at $(date)' > /tmp/poststart.log]
```


## pod资源限制
### 可限制资源单位
- cpu
  - 在kubernetes中，通常以千分之一的cpu(core)为最小单元，用毫m表示，即一个cpu核心表示1000m
- 内存

### 资源限制实现
要实现资源限制，需要先安装metrics-server
```shell
curl -lo https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.7.1/components.yaml

# 默认文件需要修改
apiversion: apps/v1
kind: deployment
metadata:
labels:
  k8s-app: metrics-server
name: metrics-server
namespace: kube-system
spec:
selector:
  matchlabels:
  k8s-app: metrics-server
strategy:
  rollingupdate:
  maxunavailable: 0
template:
  metadata:
  labels:
    k8s-app: metrics-server
  spec:
  containers:
  - args:
    - --cert-dir=/tmp
    - --secure-port=4443
    - --kubelet-preferred-address-types=internalip,externalip,hostname
    - --kubelet-use-node-status-port
    - --metric-resolution=15s
    - --kubelet-insecure-tls   #添加本行和下面两行
    image: registry.cn-hangzhou.aliyuncs.com/google_containers/metrics-server:v0.7.1  # 或者开代理
 #image: registry.cn-hangzhou.aliyuncs.com/google_containers/metrics-server:v0.6.1
 #image: k8s.gcr.io/metrics-server/metrics-server:v0.6.1
 imagepullpolicy: ifnotpresent
 livenessprobe:

# 应用此文件
kubectl apply -f components.yaml
# 查看性能性能
kubectl top nodes
```

### 资源限制
```yaml
apiversion: v1
kind: pod
metadata:
 name: pod-limit-request
spec:
 containers:
  - name: pod-limit-request-container
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
   imagepullpolicy: ifnotpresent
   resources:
     requests:
       memory: "200mi"
       cpu: "500m"
     limits:
       memory: "200mi"
       cpu: "500m"
```
提示：为保证性能，生产推荐requests和limits设置为相同的值
limit数值可以超过实际大小，但是requests不可以
- 如果requests的数值大小，没有任何节点可以满足，则调度器无法完成调度，则会卡在pending状态，详情可以查看pod创建流程

- 如果限制资源后，无法满足容器实际所需的资源大小，则会触发oomkilled，在oomkilled和重启之间反复循环


#### limitrange实现使用资源限制
后续有时间可以了解


## pod安全

### 容器安全上下文
安全上下文是一组用于决定容器是如何创建和运行的约束条件，它们代表着创建和运行容器时使用的运行时参数

它根据约束的作用范围主要包括三个级别：
- pod级别
  - 针对pod范围内的所有容器
- 容器级别
  - 仅针对pod范围内的指定容器
- psp级别
  - podsecuritypolicy，全局级别的pod安全策略，涉及到准入控制相关的知识

### 资源策略
#### 用户级别
默认pod容器进程是以root身份运行，可以通过下面属性指定其他用户
- runasuser
- runasgroup

默认情况下，一旦pod创建好后，是不允许对用户归属权限进行任意修改的，所以需要修改的话，必须先关闭，在开启

添加安全上下文属性实现指定用户身份运行pod内的进程
```yaml
[root@master1 yaml]#cat pod-securitycontext-runasuser.yaml 
apiversion: v1
kind: pod
metadata:
 name: pod-securitycontext-runasuser
 namespace: default
spec:
 containers:
  - name: pod-test
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   imagepullpolicy: ifnotpresent
   env:
    - name: port
     value: "8080"
   securitycontext:
     runasuser: 1001     #指定运行身份
     runasgroup: 1001
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
linux中相关的资源能力
```shell
cap_chown           # 改变文件的所有者和所属组
cap_mknod           # mknod()，创建设备文件
cap_net_admin       # 网络管理权限
cap_sys_time        # 更改系统的时钟
cap_sys_module      # 装载卸载内核模块
cap_net_bind_server # 允许普通用户绑定1024以内的特权端口
cap_sys_admin       # 大部分的管理权限，基本相当于root权限
```

可以在容器内部通过command+args运行一个自定义的容器启动命令
```yaml
# [root@master1 yaml]#cat pod-securitycontext-capabilities.yaml 
apiversion: v1
kind: pod
metadata:
 name: pod-securitycontext-capabilities
 namespace: default
spec:
 containers:
  - name: pod-test
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   imagepullpolicy: ifnotpresent
   command: ["/bin/sh","-c"]
   args: ["/sbin/iptables -t nat -a prerouting -p tcp --dport 8080 -j redirect --to-port 80 && /usr/bin/python3 /usr/local/bin/demo.py"]
```

通过add添加特权
```yaml
apiversion: v1
kind: pod
metadata:
 name: pod-securitycontext-capabilities
 namespace: default
spec:
 containers:
  - name: pod-test
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   imagepullpolicy: ifnotpresent
   command: ["/bin/sh","-c"]
   args: ["/sbin/iptables -t nat -a prerouting -p tcp --dport 8080 -j redirect -
-to-port 80 && /usr/bin/python3 /usr/local/bin/demo.py"]
#添加下面三行
   securitycontext:
     capabilities:
       add: ['net_admin']
       drop: ['chown']

# 注意add后面的权限能力使用单引号('')，也可以使用双引号("")
# drop可以删除特权
```

#### pod中的内核参数
pod安全上下文级别默认只支持为数不多的内核安全参数
```shell
net.ipv4.ip_local_port_range
net.ipv4.ip_unprivileged_port_start
net.ipv4.tcp_syncookies
kernel.shm_rmid_forced
```

上面的几个内核参数可以在pod内部的容器名称空间的内核级别进行调整，被视为安全参数
但其他的绝大部分参数不支持直接修改，被视为不安全参数
如果想对其他不安全内核参数修改，必须要所在的node节点上修改kubelet的配置
```shell
kubelet_extra_args='--allowed-unsafe-sysctls=net.core.somaxconn,net.ipv4.ip_nonlocal_bind'
```
示例
```yaml
apiversion: v1
kind: pod
metadata:
 name: pod-sysctl
spec:
 securitycontext:
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
   securitycontext:
     runasuser: 1001
     runasgroup: 1001
```


#### 特权
添加privileged特权
```yaml
apiversion: v1
kind: pod
metadata:
 name: pod-privileged-demo
spec:
 initcontainers:  
  - name: set-sysctl
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/admin-box:v0.1
   command: ["sysctl","-w","vm.max_map_count=6666666"]
   securitycontext:         #添加特权
     privileged: true
 containers:
  - name: pod-privileged-demo
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
```

#### 服务质量分类
qos(服务质量等级)是作用在pod上的一个配置
当kubernetes创建一个pod时，它就会给这个pod分配一个qos等级
- 低优先级besteffort：没有任何一个容器设置了requests或limits属性(最低优先级)
- 中优先级burstable: pod至少有一个容器设置了cpu或内存的requests和limits，且不相同
- 高优先级guaranteed：pod内的每一个容器同时设置了cpu和内存的requests和limits，而且所有值必须相等

当主机出现oom时，先删除服务质量低的, 服务质量高的最后删除


## 单节点多容器模式
### init container模式
```yaml
#通过init模式实现iptables规则的端口重定向
[root@master1 yaml]#cat pod-init-container.yaml 
apiversion: v1
kind: pod
metadata:
 name: pod-init-container
 namespace: default
spec:
 initcontainers:
  - name: iptables-init
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/admin-box:v0.1
   imagepullpolicy: ifnotpresent
   command: ['/bin/sh','-c']
   args: ['iptables -t nat -a prerouting -p tcp --dport 8080 -j redirect --to-port 80']
   securitycontext:
capabilities:
       add:
        - net_admin
 containers:
  - name: demo
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   imagepullpolicy: ifnotpresent
   ports:
    - name: http
     containerport: 80
```

### sidecar模式
在一个pod内启动两个容器，访问b容器的时候，都需要经过a容器，只有通过a处理后的数据才会发送给b容器。
在整个过程中，a容器就是b容器应用的代理服务器
```yaml
apiversion: v1
kind: pod
metadata:
 name: sidecar-test
spec:
 containers:
  - name: proxy
   image: envoyproxy/envoy-alpine:v1.14.1
   command: ['sh', '-c', 'sleep 5 && envoy -c /etc/envoy/envoy.yaml']
   lifecycle:
     poststart:
       exec:
         command: ["/bin/sh","-c","wget -o /etc/envoy/envoy.yaml 
http://www.wangxiaochun.com/kubernetes/yaml/envoy.yaml"]
  - name: pod-test
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   env:
    - name: host
     value: "127.0.0.1"
    - name: port
     value: "8080"
```
这里设计云原生的envoy组件，有时间可以学习下


## pod健康性检查

### pod中的健康检查流程
- 初始启动容器的时候，有一个初始化时间（initialdelayseconds，可自定义，如5s）
- 5s后启动第一个探针，`startup probe`，初始化时间是为了确保程序已经运行，因为有些程序启动可能较慢，`startup probe`一般在服务启动后探测
- startup probe如果探测失败，容器将立即重启
- startup probe探测成功后，进入下一阶段，此时startup probe将不会再执行
- 在该阶段初始也会有一个`initaldelaysceonds for livness probe`和`initaldelaysceonds for readiness probe`即启动后续探针的等待时间
- 后续有两个探针：livness probe和readiness probe
- 如果livness检测失败，则重启pod
- 如果readiness检查失败，pod不会重启，而是会将其从service资源的端点控制器中的调度列表移除，待后续检查成功，在将其从调度列表恢复


### pod健康性检查的方法
- exec探测方法
- tcpsocket探测方法
- httpget探测方法
- grpc探测方法

### 探针案例
#### exec方式案例

```yaml
apiversion: v1
kind: pod
metadata:
 name: pod-startup-exec
 namespace: default
 labels:
   app: pod-startup-exec
spec:
 containers:
  - name: pod-startup-exec-container
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   imagepullpolicy: ifnotpresent
   startupprobe:
     exec:
       command: ['/bin/sh', '-c', '[ "$(curl -s 127.0.0.1/livez)" == "ok" ]']
     initialdelayseconds: 60
     timeoutseconds: 1
     periodseconds: 5
     successthreshold: 1
     failurethreshold: 1
```

```yaml
apiversion: v1
kind: pod
metadata:
 name: pod-liveness-exec-cmd
 namespace: default
spec:
 containers:
  - name: pod-liveness-exec-cmd-container
   image: busybox:1.32.0
   imagepullpolicy: ifnotpresent
   command: ["/bin/sh","-c","touch /tmp/healthy; sleep 3; rm -f 
/tmp/healthy;sleep 3600"]
   livenessprobe:
     exec:
       command: ["test", "-e","/tmp/healthy"]
     initialdelayseconds: 1
     periodseconds: 3
```

#### tcpsocket方式案例
使用此配置，kubelet将尝试在指定端口上打开容器的套接字，如果可以建立连接，则容器被认为是健康的，如果不能则认为是失败的，其实就是在检查端口是否开启
```yaml
apiversion: v1
kind: pod
metadata:
name: pod-liveness-tcpsocket
 namespace: default
spec:
 containers:
  - name: pod-liveness-tcpsocket-container
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   imagepullpolicy: ifnotpresent
   ports:
    - name: http           #给指定端口定义别名
     containerport: 80
   securitycontext:  #添加特权，否则添加iptables规则会提示：getsockopt failed strangely: operation not permitted
     capabilities:
       add:
        - net_admin
   livenessprobe:
     tcpsocket:
       port: http        #引用上面端口的定义
     periodseconds: 5
     initialdelayseconds: 5
#注意：由于此镜像应用对外暴露的端口是80端口，所以要探测80端口
```

readness的tcpsocket探针
```yaml
apiversion: v1
kind: pod
metadata:
 name: pod-readiness-tcpsocket
 labels:
   app: pod-readiness-tcpsocket
spec:
 containers:
  - name: pod-readiness-tcpsocket-container
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
   readinessprobe:
     tcpsocket:
       port: 80
     initialdelayseconds: 5
     periodseconds: 10
   livenessprobe:
     tcpsocket:
       port: 80
     initialdelayseconds: 15
     periodseconds: 20
---
apiversion: v1
kind: service
metadata:
 name: pod-readiness-tcpsocket-svc
spec:
 ports:
  - name: http
   port: 80
   protocol: tcp
   targetport: 80
 selector:
   app: pod-readiness-tcpsocket  #指定上面pod相同的标签
```


#### httpget方式案例
http探测通过对容器内容开放的web服务，进行http方法的请求探测，如果探测成功（即响应码为2xx,3xx），否则就失败

http probes允许针对httpget配置额外的字段
```shell
host：连接使用的主机名，默认是 pod 的 ip。也可以在 http 头中设置 “host” 来代替。一般不配置此
项
scheme ：用于设置连接主机的方式（http 还是 https）。默认是 "http"。一般不配置此项
path：访问 http 服务的路径。默认值为 "/"。一般会配置此项
port：访问容器的端口号或者端口名。如果数字必须在 1～65535 之间。一般会配置此项
httpheaders：请求中自定义的 http 头。http 头字段允许重复。一般不配置此项
```
```yaml
# [root@master1 yaml]#cat pod-liveness-http.yaml 
apiversion: v1
kind: pod
metadata:
 name: pod-liveness-http
spec:
 containers:
  - name: pod-liveness-http-container
   image: busybox:1.32.0
   ports:
    - name: http
     containerport: 80
   livenessprobe:
     httpget:
       port: http    #或者指定80，如果非标准端口可以指定端口号
       path: /index.html
     initialdelayseconds: 1
     periodseconds: 3
```

## 工作负载
### 工作负载资源分类
- 无状态应用编配
  - deployment
  - replicaset
- 有状态应用编排
  - statefulset
- 系统级应用
  - daemonset
- 工作类应用
  - job
  - cronjob

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

#### yaml方法
```yaml
metadata:
  labels:
    key1: value1
    key2: value2
    ...
# 注意：labels复数
```

### 标签选择器 label selector
label附加到kubernetes集群中的各种资源对象上，目的是对这些资源对象可以进行后续的分组管理
而分组管理的核心就是：`标签选择器label selector`

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
apiversion: v1
kind: pod
metadata:
 name: cuda-test
spec:
 containers:
 - name: cuda-test
     image: "registry.k8s.io/cuda-vector-add:v0.1"
     resources:
       limits:
         nvidia.com/gpu: 1
 nodeselector:
   accelerator: nvidia-tesla-p100
```

应用示例2
```yaml
apiversion: v1
kind: service
metadata:
 name: service-loadbalancer-lbaas
spec:
 type: loadbalancer
 externaltrafficpolicy: local
 selector:
   app: myapp
 ports:
  - name: http
   protocol: tcp
   port: 80
   targetport: 80
```

#### 集合匹配
```shell
# 集合匹配相当于“或”
#示例：
env in (dev, test)        #匹配所有具有标签 env = dev 或者 env = test 的资源对象
name notin (frontend,backent)    #匹配所有不具有标签name=frontend或者name=backend或者没有name标签的资源对象
```

#### 匹配标签matchlabels
```shell
#匹配标签：
   matchlabels:
     name: nginx
     app: myapp
#当 matchlabels 中有多个标签时，它们之间的关系是逻辑与（and）关系
#如下所示：
matchlabels:
 app: frontend
 environment: production
#那么只有那些标签中同时包含 app=frontend 和 environment=production 的资源才会被选中。
```
#### 匹配表达式
```shell
#匹配表达式：
   matchexpressions:
      - {key: name, operator: notin, values: [frontend]}
#当 matchexpressions 中包含多个标签表达式时，它们之间的关系是逻辑与（and）关系
#常见的operator操作属性值有：
   in、notin、exists、notexists等
   exists和notexist时，values必须为空，即 { key: environment, opetator: exists,values:}
#注意：这些表达式一般应用在rs、rc、deployment等其它管理对象中。
```

```yaml
matchexpressions:
  - key: environment
   operator: in
   values:
      - production
      - staging
  - key: app
   operator: notin
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
#多个selector表示并且的关系
kubectl get type -l selector1[,selector2,...]
kubectl get type -l selector1 [-l selector2] ...
#额外针对指定的每一个标签单独一列来显示对应的值
kubectl get type -l label_name
```

### replica set 工作机制(rs)
#### 查看资源清单写法
```shell
kubectl explain 资源类型
```

#### replica set基础管理replica set资源清单示例
```yaml
apiversion: apps/v1
kind: replicaset   # 注意大小写
metadata:
  name: _
  namespace: _
spec:
  minreadyseconds <int>
  replicas <int>
  selector:
    matchexpression <[]object>
    matchlabels <map[string]string>
  template:
    metadata:
      labels:   # 这个地方定义具体pod的标签一定要和selector标签选择器规则匹配
    spec:
    ...
```

```yaml
apiversion: apps/v1
kind: replicaset
metadata:
  name: controller-replicaset-test
spec:
  minreadyseconds: 0
  replicas: 3    # 修改此行
  selector:
    matchlabels:
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
        images: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
```

#### replicaset扩容和缩容
```shell
# 方法1：修改yaml文件中replicas的参数

# 方法2：
kubectl scale replicaset controller-replicaset-test --replicas 2
```

#### 更新镜像版本
```yaml
apiversion: apps/v1
kind: replicaset
metadata:
  name: controller-replicaset-test
spec:
  minreadyseconds: 0
  replicas: 3    # 修改此行
  selector:
    matchlabels:
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
        images: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2 #修改此行
```

必须要手动将旧的删除后，再重新创建才能更新成功
虽然镜像模版信息更新了，但是pod并没有升级镜像，rs不支持自动更新

#### 蓝绿发布示例
```yaml
apiversion: v1
kind: service
metadata:
  name: svc-replicaset-blue-green
spec:
  type: clusterip
  selector:
    app: rs-test
    ctr: rs-${deploy}
    version: ${version}
  ports:
  - name: http
    port: 80
    protocol: tcp
    targetport: 80
---
apiversion: apps/v1
kind: replicaset
metadata:
  name: rs-${deploy}
spec:
  minreadyseconds: 3
  replicas: 2
  selector:
    matchlabels:
      app: rs-test
      ctr: rs-${deploy}
      version: ${version}
  template:
    metadata:
      labels:
        spp: rs-test
        ctr: rs-${deploy}
        version: ${version}
    spec:
      containers:
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:${version}
```
```shell
# 访问
deploy=blue version=v0.1 envsubst < controller-replicaset-blue-green.yaml|kubectl apply -f -
# envsubst命令
用环境变量的值替换掉标准输入的内容
root@master101:~/mypod# name=feng envsubst
i'm $name
i'm feng
```


### deployment

deployment相对于rs的一个最大升级是：支持滚动发布策略，其他功能几乎一样

#### 创建deployment
```shell
kubectl create deployment myapp --image registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas 3 --dry-run=client -o yaml

root@master101:~/mypod# kubectl create deployment myapp --image registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas 3 --dry-run=client -o yaml
apiversion: apps/v1
kind: deployment
metadata:
  creationtimestamp: null
  labels:
    app: myapp
  name: myapp
spec:
  replicas: 3
  selector:
    matchlabels:
      app: myapp
  strategy: {}
  template:
    metadata:
      creationtimestamp: null
      labels:
        app: myapp
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
        name: pod-test
        resources: {}
status: {}
# 同replicaset基本一致
```
```shell
# 查看标签
root@master101:~/mypod# kubectl get pod --show-labels
name                               ready   status    restarts   age     labels
controller-replicaset-test-64x48   1/1     running   0          96m     app=rs-test,release=stable,version=v1.0
controller-replicaset-test-jc5h4   1/1     running   0          105m    app=rs-test,release=stable,version=v1.0
controller-replicaset-test-sngj8   1/1     running   0          96m     app=rs-test,release=stable,version=v1.0
controller-replicaset-test-xjlft   1/1     running   0          96m     app=rs-test,release=stable,version=v1.0
controller-replicaset-test-zjx9b   1/1     running   0          105m    app=rs-test,release=stable,version=v1.0
myapp-547df679bb-9p82b             1/1     running   0          77s     app=myapp,pod-template-hash=547df679bb
myapp-547df679bb-cwknj             1/1     running   0          6m11s   app=myapp,pod-template-hash=547df679bb
myapp-547df679bb-djpkh             1/1     running   0          6m11s   app=myapp,pod-template-hash=547df679bb
myapp-547df679bb-ftxlg             1/1     running   0          6m11s   app=myapp,pod-template-hash=547df679bb
myapp-547df679bb-ssdk5             1/1     running   0          77s     app=myapp,pod-template-hash=547df679bb
```

#### deployment扩容与缩容
```shell
# 基于资源对象调整
kubectl scale --current-replicas=<新副本数>] --replicas=[副本数] deployment /deploy_name

# 基于文件调整
kubectl scale --replicas=<新副本数> -f deploy_name.yaml
```

deployment创建后的名称组成为name+rs_name_随机字符串

#### deployment动态更新和回滚
```shell
# 更新命令
kubectl set subcommand [options] 资源类型 资源名称
# 示例
kubectl set image deployment/myapp pod-test=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2 --record=true

# 参数详情
--record=true      # 更改时，将会信息转增到历史

# 查看版本更新状态和历史
kubectl rollout history deployment myapp

# 撤销回退上次的更改，注意只能回退一次
kubectl rollout undo deployment myapp

# 回退到指定历史
kubectl rollout undo --to-revision=2 deployment myapp
```

#### 批量更新
```shell
# 多次更新合并为一次更新
# 暂停更新
kubectl rollout pause deployment pod-test

# 第一次更新
kubectl set image deployment/myapp pod-test=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2 --record=true

# 第二次修改
kubectl set resources deployment/myapp -c pod-test --limits=cpu=200m,memory=128mi --requests=cpu=200m,memory=128mi

# 此时还没有更新

# 恢复批量更新
kubectl rollout resume deployment myapp
```

#### deployment实现滚动更新策略
金丝雀发布示例
```yaml
apiversion: apps/v1
kind: deployment
metadata:
  name: deployment-rolling-update-canary
spec:
  replicas: 3
  selector:
    matchlabels:
      app: pod-test
  template:
    metadata:
      labels:
        app: pod-test
    spec:
      containers:
      - name: pod-rolling-update-canary
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
  strategy:  # 更新策略
    type: rollingupdate
    # 滚动更新类型，可用值有recreate（删除所有旧pod再创建新pod）和rollingupdate
    rollingupdate:
      maxsurge: 1     # 先加后减
      maxunavaliable: 0
---
apiversion: v1
kind: service
metadata:
  labels:
    app: pod-test
  name: pod-test
spec:
  ports:
  - name: "80"
    port: 80
    protocol: tcp
    targetport: 80
  selector:
    app: pod-test
  tyep: clusterip
```

滚动发布
```shell
# 发布
kubectl apply -f controller-deployment-rollupdate-canary.yaml

# 版本升级
sed -i 's/pod-test:v0.1/pod-test:v0.2/' controller-deployment-rollupdate-canary.yaml

# 滚动发布
kubectl apply -f controller-deployment-rollupdate-canary.yaml && kubectl rollout pause deployment deployment-rolling-update-canary`

# 如果确认没问题继续更新
kubectl rollout resume deployment deployment-rolling-udpate-canary && kubectl rollout pause deployment deployment-rolling-update-canary
```

### daemon工作机制
#### 扩展：污点容忍度
```yaml
...
  tolerations:
  - operator: exists
```

#### 注意daemonset对象不支持pause动作（暂停更新）

#### daemonset案例-node-exporter
```yaml
apiversion: apps/v1
kind: daemonset
metadata:
  name: daemonset-demo
  namespace: default
  labels:
    app: prometheus
    component: node-exporter
spec:
  selector:
    matchlabels:
      app: prometheus
      componennt: node-exporter
  template:
    metadata:
      name: prometheus-node-exporter
      labels:
        app: prometheus-node-exporter
        component: node-exporter
    spec:
      # 污点容忍度
      #tolerations:
      #- key: node-role.kubernetes.io/control-plane
      #  operator: exists
      #  effect: noschedule
      #- key: node-role.kubernetes.io/master
      #  operator: exists
      #  effect: noschedule
      containers:
      - image: prom/node-exporter:v1.2.2
        name: prometheus-node-exporter
        ports:
        - name: prom-node-exp
          containerport: 9100
          # hostport: 9100, 和hostnetwork二选一即可，要吗只保露节点端口，要吗直接使用节点网络
        livenessprobe:
          tcpsocket:
            port: prom-node-exp
          initialdelayseconds: 3
        readinessprobe:
          httpget:
            path: '/metrics'
            port: prom-node-exp
            scheme: http
          initialdelayseconds: 5
      hostnetwork: true
      hostpid: true
```

#### 仅在指定标签的每个主机上运行一个pod
```shell
# 贴标签
kubectl label node node1.wang.org node2.wang.org ai=true
# 查看标签
kubectl get nodes --show-lables
```

```yaml
apiversion: apps/v1
kind: daemonset
metadata:
  name: controler-daemonset-label-test
spec:
  selector:
    matchlabels:
      ai: "true"
  template:
    metadata:
      labels:
        app: pod-test
    spec:
      nodeselector:
        ai: "true"
      container:
      - name: pod-test
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v1.0
```

#### 滚动更新
```yaml
...
  updatestrategy:
    rollingupdate:
      maxsurge: 0
      maxunavaiable: 1
    type: rollingupdate  #pod自动更新
```

### job工作机制
job负责编排运行有结束时间的“一次性”任务
- 控制器要确保pod内的进程“正常（成功完成任务）”退出
- 非正常退出的pod可以根据需要重启，并在重试指定的次数后终止
- job可以是单次任务，也可以是在多个pod分别各自运行一次，实现运行多次（次数通常固定）
- job支持同时创建及并行运行多个pod以加快任务处理速度，job控制器支持用户自定义其并行度

关于job的执行主要有两种并行度的类型：
- 串行job：即所有job任务都在上一个job执行完成后，再开始执行
- 并行job：如果存在多个job，可以设定并行执行的job数量

job资源同样需要标签选择器和po的模版，但它不需要指定replicas，且需要给定completions，即需要完成的作业次数，默认为1次
- job资源会为其pod对象自行添加"job-name=job_name"和"controller-uid=uid"标签，并使用标签选择器完成对controller-uid标签的关联，因此，selector并非必选字段
- pod的命名格式：$(job-name)-$(index)-$(random-string)，其中的$(index)字段取值与completion和completionmode有关

注意
- job资源是标准api资源类型
- job资源所在群组为"batch/v1"
- job资源中，pod的restartpolicy的取值只能为never和onfailure

#### job属性解析
```shell
apiversion: batch/v1               # api群组及版本
kind: job                          # 资源类型特有标识
metadata：
  name <string>                    # 资源名称，在作用域中要唯一
  namespace <string>               # 名称空间，job资源隶属名称空间级别
spec:
  selector <object>                # 标签选择器，必须匹配template字段中pod模版中的标签
  suspend <boolean>                # 是否挂起当前job的执行，挂起作业会重置starttime字段的值
  template
  completions <int>                # 期望的完成作业次数，成功运行结束的pod数量
  completionmode <string>          # 追踪pod完成模式，支持有序的index和无序的noindexed (默认)
  ttlsecondsafterfinished          # completed终止状态作业的生存时长，超时将被删除
  parallelism <int>                # 作业的最大并行度：默认为1
  backofflimit <int>               # 将作业标记为failed之前的重试次数，默认为6
  activedeadlineseconds <int>      # 作业启动后可处于活动状态的时长
```

#### 并行配置示例
```yaml
# 串行运行共5次任务
spec:
  parallelism: 1
  completion: 5

# 并行2个队列，总共运行6次任务，也就是说并行运行3次即可
spec:
  parallelism: 2
  completion: 6
```

#### 多个串行任务示例
```yaml
apiversion: batch/v1
kind: job
metadata:
  name: job-multi-serial
spec:
  completions: 5
  parallelism: 1
  #completionmode: indexed
  template:
    spec:
      containers:
      - name: job-multi-serial
        image: busybox:1.30.0
        command: ["/bin/sh", "echo serial job; sleep 3"]
        restartpolicy: onfailure
```

#### 并行任务
```yaml
apiversion: batch/v1
kind: job
metadata:
  name: job-multi-parallel
spec:
  completions: 6
  parallelism: 2
  ttlsecondsafterfinished: 3600
  backofflimit: 3
  activedeadlineseconds: 1200 2
  ttlsecondsafterfinished: 3600
  backofflimit: 3
  activedeadlineseconds: 1200 
  template:
    spec:
      containers:
      - name: job-multi-parallel
        image: busybox:1.30.0
        command: ["/bin/sh","-c","echo parallel job; sleep 3"]
      restartpolicy: onfailure
```
- 扩展资料activedeadlineseconds
```shell
开始计时：
当 job 被创建时，kubernetes 开始计时 activedeadlineseconds。
超过时间限制：

如果 job 的所有 pod 在 1200 秒内没有完成，无论当前有多少 pod 仍在运行，kubernetes 会终止所有 pod。
状态更新：

job 的状态会被标记为 failed，并附带一个消息，说明 job 超过了 activedeadlineseconds。
```
- 扩展资料backofflimit
- 测试backofflimit参数
```yaml
apiversion: batch/v1
kind: job
metadata:
  name: example-job
spec:
  backofflimit: 4  # 最多重试 4 次
  template:
    metadata:
      name: example-job-pod
    spec:
      containers:
      - name: example
        image: busybox
        command: ["sh", "-c", "exit 1"]
      restartpolicy: never
```
```shell
初始创建：
kubernetes 创建一个 pod 来执行 job。
pod 执行 exit 1 命令，返回失败状态。
重试：

kubernetes 根据 backofflimit 开始重试。
每次重试后，kubernetes 会根据指数退避算法（exponential backoff）增加重试间隔时间。
超过限制：

如果 job 的 pod 连续失败 4 次（包括初始创建），kubernetes 将停止重试，并将 job 的状态标记为 failed。
状态更新：

job 的状态会更新为 failed，并附带一个消息，说明 job 因重试次数超过 backofflimit 而失败
```

### cronjob工作机制
- cronjob案例
```yaml
apiversin: batch/v1
kind: cronjob
metadata:
  name: cronjob
spec:
  schedule: "*/2 * * * *" #每2分钟执行1次
  jobtemplate:
    spec:
      #parallelism: 2
      #completions: 2
      template:
        spec:
          restartpolicy: onfailure
          containers:
          - name: cronjob
            image: busybox:1.30.0
            command: ["/bin/sh","-c","echo cron job"]
```

## 服务发现 service

- service只能做四层代理
- ingress有七层负载能力  

### service核心能力
- 服务发现：利用标签选择器，在同一个namespace中筛选符合的条件的pod，从而实现发现一组提供了相同服务的pod
- 负载均衡：service作为流量入口和负载均衡器，其入口为clusterip，这组筛选出的pod的ip地址，将作为该service的后端服务器
- 名称解析：利用cluster dns，为该组pod所代表的服务提供一个名称，在dns中对于每个service，自动生成一个a、ptr和srv记录

### endpoints
当创建service资源的时候，最重要的就是service指定能够提供服务的标签选择器

service controller就会根据标签选择器会自动创建一个同名的endpoint资源对象，kubernetes新版中还增加了endpointerslices资源
- endpoint controller使用endpoint的标签选择器（继承自service标签选择器），筛选符合条件（包括符合标签选择器条件和处于ready状态）的pod资源
- endpint controller将符合要求的pod资源绑定到endpoint上，并告知给service资源谁可以正常提供服务
- service会自动获取一个固定的cluster ip向外提供由endpoint提供的服务资源
- service其实就是为动态的一组pod资源对象提供一个固定的访问入口。即service实现了后端pod应用服务发现的发现功能

- 每创建一个service，自动创建一个与之同名的api资源类型endpoints
- endpoints负载维护由相关service标签选择器匹配的pod对象
- endpoints对象上保存service匹配到的所有pod的ip和port信息，称之为端点
- etcd是k/v数据库，而一个endpoints对象对应一个key，所有后端pod端点信息为其value
- 当一个endpoints对象对应后端每个pod的每次变动，都需更新整个endpoints对象，并将新的endpoints对象重新保存至api server和etcd
- 此外还需要将该对象同步至每个节点的kube-proxy
- 在etcd中的对象默认最大为1.5mb，一个endpoints对象至多可以存储5000个左右的端点信息，这意味着平均每个端点占300kb

### endpointslice
- 基于endpoints机制，即便只有一个pod的ip等信息发生变动，就需要向集群中的每个节点上的kube-proxy发送整个endpoints对象
- 比如: 一个由2000个节点组成的集群中，更新一个有5000个pod ip占用1.5mb空间的endpoints 对象，就需要发送3gb的数据若以滚动更新机制，一次只升级更新一个pod的信息，这将导致更新这个endpoints对象需要发送15t的数据
- endpointslice资源通过将endpoints切片为多片来解决上述问题
- 自kubernetesv1.16引入endpointslice
- 每个endpointslice默认存储100个端点信息，不会超过etcd对单个对象的存储限制
- 可在kube-controller-manager程序上使用 --max-endpoints-per-slice选项进行配置
- endpointslice并未取代endpoints，二者同时存在


### endpoint实战示例 
通过手动创建 kubernetes endpoints 并将其与外部服务器的地址关联，从而使集群内的 pod 可以访问集群外部的服务器服务

- 创建一个 service：
  - 首先，创建一个 kubernetes service，但不指定任何 selector，这样 kubernetes 不会自动创建对应的 endpoints。

- 手动创建 endpoints：
  - 手动创建一个 endpoints 对象，其中包含外部服务器的 ip 地址和端口。

创建一个没有selector的service服务，没有selector,因此也不会为它自动创建endpoint
```shell
apiversion: v1
kind: service
metadata:
  name: external-service
  namespace: default
spec:
  ports:
  - port: 80
    targetport: 80
```

手动创建endpoint
```shell
apiversion: v1
kind: endpoints
metadata:
  name: external-service
  namespace: default
subsets:
  - addresses:
      - ip: 192.168.1.100   # 外部服务器的 ip 地址
    ports:
      - port: 80            # 外部服务器的端口
```

执行资源清单
```shell
kubectl apply -f external-service.yaml
kubectl apply -f external-endpoints.yaml

# 现在，集群内的 pod 可以通过 external-service service 的 dns 名称来访问外部服务器的服务。
curl http://external-service.default.svc.cluster.local
```

### service服务的执行过程

运维（写一个资源清单） ----> api server ------> etcd数据库
api serser同时 ----> service controller ----> api server
----> kube-proxy -----> iptables/ipvs/nftables


### service类型(四种)

- cluterip
- nodeport
- loadbalancer
- exteralname


### service类型之clusterip

此为service的默认类型
为集群内部的客户端访问，包括节点和pod等，外部网络无法访问

### clusterip实现
```shell
# 在命令行中，clusterip name很重要，这个name必须和pod的app:~标签一致，否则匹配不到pod
kubectl create service clusterip name [--tcp=<port>:<targetrport>] [--dry-run=server|client|none] [options]

# 示例
kubectl create service myapp --tcp 88:80 --dry-run=client -o yaml
```

### service类型之nodeport

本质上就是把port的端口暴露给宿主机的端口
nodeport = pod:port --> node:port
- 这里的node可以是任意节点，因为集群中所有节点都有kube-proxy，都能实现调度，但是本地local更快
- 默认随机端口范围30000-32767，可指定为固定端口 

#### nodeport实现
```yaml
apiversion: v1
kind: service
metadata:
  name: myapp-service-nodeport
spec:
  ports:
  - name: 80-80
    port: 80
    protocol: tcp
    targetport: 80
  selector:
    app: myapp
  type: nodeport
```
指定暴露端口
```yaml
apiversion: v1
kind: service
metadata:
  name: myapp-service-nodeport
spec:
  ports:
  - name: 80-80
    port: 80
    protocol: tcp
    targetport: 80
    nodeport: 32000   # 指定暴露端口
  selector:
    app: myapp
  type: nodeport
```
#### 资源清单解析
端口映射详解
- service 内部端口 (port: 80):
  - 这是 service 对外提供的端口，客户端（例如其他 pods）可以通过这个端口访问 service。

- 目标端口 (targetport: 80):
  - 这是 service 选择器匹配到的 pod 上的端口。service 将请求转发到这个端口上的 pod。也就是说，当请求到达 service 的 80 端口时，它将转发到 pod 的 80 端口。
  nodeport (nodeport: 32000):

这是在每个节点上暴露的端口，用于将外部流量路由到 service。外部客户端可以通过节点的 ip 地址和 32000 端口来访问 service，kubernetes 将这个流量转发到 service 的 80 端口，然后再转发到 pod 的 80 端口。

端口映射总结
外部流量访问: 外部客户端可以通过访问节点的 ip 地址和 32000 端口（例如 http://<node-ip>:32000）来访问你的 service。

内部流量处理: kubernetes 将这些请求转发到 service 的 80 端口，然后再转发到与 service 选择器匹配的 pod 的 80 端口。


#### 内部流程策略
```yaml
apiversion: v1
kind: service
metadata:
  name: myapp-service-nodeport
spec:
  ports:
  - name: 80-80
    port: 80
    protocol: tcp
    targetport: 80
    nodeport: 32000   # 指定暴露端口
  selector:
    app: myapp
  type: nodeport
  internaltrafficpolicy: # 内部流程策略处理方式，local表示由当前节点处理，cluster表示向集群范围调度，默认cluster
  externaltrafficpolicy: # 外部流程策略处理方式，默认cluster，当为local时，表示由当前节点处理，性能较好，但无负载均衡功能，且可以看到真实客户ip，cluster表示向集群范围调度，和local相反，基于性能原因，生产更建议local
  # 此方式仅支持type是nodeport和loadblance
```

外部流量策略本质
- cluster：本质是fullnat
- local：本质是dnat

### service类型之loadbalancer

#### loadbalancer类型实现

loadbalancer类型默认无法获取loadbalancerip

```yaml
# 清单文件
# cat service-loadbalancer.yaml
apiversion: v1
kind: service
metadata:
  name: service-loadbalancer
spec:
  type: load balancer
  externaltrafficpolicy: local
  selector:
    app: myweb
  ports:
  - name: http
    protocol: tcp
    port: 80
    targetport: 80
    # loadbalancerip: 6.6.6.6 #指定地址后，还需要连接云服务商的lbaas服务才能真正获得此地址，否则为pending状态
```

注意：loadbalancer本身是一个增强的nodeport类型的service

使用openelb实现loadbalancer
```shell
# 国内镜像地址
# 青云项目
image: registry.cn-beijing.aliyuncs.com/wangxiaochun/ingress-nginx-kube-webhook-certgen:v1.1.1
image: registry.cn-beijing.aliyuncs.com/wangxiaochun.kubesphere/openelb.v0.5.1

# 谷歌项目：metallb实现
metallb_version='v0.14.7'
wget https://mirror.ghproxy.com/https://raw.githubusercontent.com/metallb/metallb/${metallb_version}/config/manifests/metallb-native.yaml

# 直接执行
kubectl apply -f metallb-native.yaml

#指定ip地址池
[root@master1 yaml]#cat service-metallb-ipaddresspool.yaml 
apiversion: metallb.io/v1beta1
kind: ipaddresspool
metadata:
 name: localip-pool
 namespace: metallb-system
spec:
 addresses:
  - 10.0.0.10-10.0.0.50
 autoassign: true
 avoidbuggyips: true
  
[root@master1 yaml]#cat service-metallb-l2advertisement.yaml 
apiversion: metallb.io/v1beta1
kind: l2advertisement
metadata:
 name: localip-pool-l2a
 namespace: metallb-system
spec:
 ipaddresspools:
  - localip-pool
 interfaces:
  - eth0

# 执行
kubectl apply -f service-metallb-ipaddresspool.yaml -f service-metallb-l2advertisement.yaml

# 创建deployment和loadbalancer类型的service，测试地址池是否能给service分配loadbalancer ip
kubectl create deployment myapp --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas=3

# 创建service
[root@master1 yaml]#cat service-loadbalancer-lbaas.yaml 
apiversion: v1
kind: service
metadata:
 name: service-loadbalancer-lbaas
spec:
 type: loadbalancer
 externaltrafficpolicy: local
 selector:
   app: myapp
 ports:
  - name: http
   protocol: tcp
   port: 80
   targetport: 80
```

### externallps
如果当前底层没有laas服务，也没有lbaas服务，但是想直接通过众所周知的服务端口地址来进行访问，可以通过externallps实现

在任意主机上，配置一个地址
```shell
# 这里模拟外网ip，必须被宿主机能够访问，而且与kubernetes的集群pod网段不一样
ip a a 10.0.0.66 dev eth0 label 0:1

#配置清单文件
[root@master1 yaml]#cat service-loadbalancer-externalip.yml 
apiversion: v1
kind: service
metadata:
 name: service-loadbalancer-externalip
spec:
 type: loadbalancer
 ports:
  - port: 80
 selector:
   app: myweb
 externalips:
  - 10.0.0.66
#注意：这里的externalips对于使用哪种service类型无关

# 这里创建nodeport，然后加externalips是一样的
```

### service类型之externalname
externalname实现
```yaml
# vim service-externalname-redis.yaml
kind: service
apiversion: v1
metadata:
 name: svc-externalname-web
 namespace: default
spec:
 type: externalname
 externalname: www.wangxiaochun.com   #外部服务的fqdn,不支持ip
 # 使用外部dns的同时需要修改coredns
 ports:                               #以下行都可选
  - protocol: tcp
   port: 80
   targetport: 8888                    #外部服务端口
   nodeport: 0
 selector: {}                         #没有标签选择器，表示不关联任何pod
```

pod域名固定写法：`service名+namespace名+svc.cluster.local`

- cluster.local是在安装k8s的时候指定的
- 查看方法`kubectl cluster-info dump|grep cluster.local`
- 访问：`curl sev-externalname-web.default.svc.cluster.local:8888`


#### 使用自建的endpoint实现基于clusterip类型的service代理集群外部服务
- 手动创建一个endpoints资源对象，直接把外部端点的ip地址，放入可用地址列表
- 额外创建一个不带selector的同名的service对象

```yaml
# vim service-endpoints.yaml
---
kind: endpoints
apiversion: v1
metadata:
  name: service-redis
  namespace: default
subsets:
  - addresses:
    - ip: 10.0.0.101    # 外部服务的fqdn或ip
  # - ip: 10.0.0.102   可以有多个外部主机
    ports:
      - name: redis
        port: 6379
        protocol: tcp
---
apiversion: v1
kind: service
metadata:
  name: service-redis  # 和上面的endpoints必须同名, 后续靠域名访问，即service-redis
  namespace: default
spec:
  type: clusterip
  # clusterip: "none"
  ports:
    - name: redis
      port: 6379
      protocol: tcp
      targetport: 6379
```

### 会话粘滞
```shell
# 创建一个clusterip
kubectl create svc clusterip myapp --tcp 80:80
```
默认没有开启会话粘滞
```yaml
kubectl create deployment myweb --image=wangxiaochun/pod-test:v0.1 --replicas=3

# cat service-test.yaml
kind: service
apiversion: v1
metadata:
  name: service-test
spec:
  selector:
    app: myweb
  ports:
  - name: http
    protocol: tcp
    port: 80
    targetport: 80
```

实现会话粘滞
```yaml
# cat service-session.yaml
apiversion: v1
kind: service
metadata:
  name: service-session
spec:
  type: loadbalancer
  ports:
  - port: 80
  selector:
    app: myweb
  sessionaffinity: clientip  # 客户端ip的亲缘性，实现1800s内的会话保持
  sessionaffinityconfig:
    clientip:
      timeoutseconds: 1800
```

### ipvs
#### 查看当前模式
```shell
#查看当前模式
[root@master1 ~]#curl 127.0.0.1:10249/proxymode
iptables
```

#### 更改模式
更改kube-proxy为ipvs模式方法说明
```shell
#方法1： 在集群创建的时候，修改kubeadm-init.yml 添加如下配置，此方法是生产中推荐
[root@master1 ~]#kubeadm config print init-defaults > kubeadm-init.yaml
#在文件最后面添加以下几行
[root@master1 ~]#vim kubeadm-init.yaml
---
apiversion: kubeproxy.config.kubernetes.io/v1alpha1
kind: kubeproxyconfiguration
featuregates:
 supportipvsproxymode: true
mode: ipvs

#方法2：在测试环境中，临时修改一下configmap中proxy的基本属性，此方式在测试环境中推荐使用
root@master1:~# kubectl edit configmap kube-proxy -n kube-system
 ...
   mode: "ipvs"  #修改此行，默认为空”“表示iptables模式

#所有的规则都是 ipvs本身的调度规则，可以在node节点上查看效果(master也可以)
ipvsadm -ln
# 保存后立即生效，但是pod需要删除重新生成
```

## 使用k8s实现wordpress架构
### 创建wordpress的service网络
```shell
kubectl create svc loadbalancer wordpress --tcp 80:80 --dry-run=client -o yaml > wordpress-mysql-svc-deployment.yaml
```

### 创建deployment类型编排的wordpress
```shell
kubectl create deployment wordpress --image registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache--dry-run=client -o yaml >> wordpress-mysql-svc-deployment.yaml kubectl cre
```

### 创建mysql的service网络
```shell
kubectl create svc clusterip mysql --tcp 3306:3306 --dry-run=client -o yaml > wordpress-mysql-svc-deployment.yaml
```

### 创建mysql的deployment类型
```shell
kubectl create deployment mysql --image registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle --dry-run=client -o yaml >> wordpress-mysql-svc-deployment.yaml 
```

### 在最开始定义一个名称空间，整理yaml文件如下
```yaml
apiversion: v1
kind: namespace
metadata:
  name: wordpress
---
apiversion: v1
kind: service
metadata:
  labels:
    app: wordpress
  name: wordpress
spec:
  ports:
  - name: 80-80
    port: 80
    protocol: tcp
    targetport: 80
  selector:
    app: wordpress
  type: loadbalancer

---
apiversion: apps/v1
kind: deployment
metadata:
  labels:
    app: wordpress
  name: wordpress
spec:
  progressdeadlineseconds: 600
  replicas: 1
  revisionhistorylimit: 10
  selector:
    matchlabels:
      app: wordpress
    type: rollingupdate
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache--dry-run=client
        imagepullpolicy: ifnotpresent
        name: wordpress

---

apiversion: v1
kind: service
metadata:
  creationtimestamp: null
  labels:
    app: mysql
  name: mysql
spec:
  ports:
  - name: 3306-3306
    port: 3306
    protocol: tcp
    targetport: 3306
  selector:
    app: mysql
  type: clusterip

---
apiversion: apps/v1
kind: deployment
metadata:
  labels:
    app: mysql
  name: mysql
spec:
  replicas: 1
  selector:
    matchlabels:
      app: mysql
  template:
    metadata:
      creationtimestamp: null
      labels:
        app: mysql
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
        name: mysql
```

### 在执行资源清单的时候，指定一开始创建的namespace，并记得把环境变量写上
```yaml
apiversion: v1
kind: namespace
metadata:
  name: wordpress
---
apiversion: v1
kind: service
metadata:
  labels:
    app: wordpress
  name: wordpress
spec:
  ports:
  - name: 80-80
    port: 80
    protocol: tcp
    targetport: 80
  selector:
    app: wordpress
  type: loadbalancer

---
apiversion: apps/v1
kind: deployment
metadata:
  labels:
    app: wordpress
  name: wordpress
spec:
  replicas: 1
  selector:
    matchlabels:
      app: wordpress
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache
        imagepullpolicy: ifnotpresent
        name: wordpress
        env:
        - name: wordpress_db_host
          value: mysql.wordpress.svc.cluster.local.
        - name: wordpress_db_user
          value: wordpress
        - name: wordpress_db_password
          value: "123456"
        - name: wordpress_db_name
          value: wordpress

---
apiversion: v1
kind: service
metadata:
  labels:
    app: mysql
  name: mysql
spec:
  ports:
  - name: 3306-3306
    port: 3306
    protocol: tcp
    targetport: 3306
  selector:
    app: mysql
  type: clusterip
---
apiversion: apps/v1
kind: deployment
metadata:
  name: mysql
spec:
  replicas: 1
  selector:
    matchlabels:
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
        - name: mysql_root_password
          value: "123456"
        - name: mysql_database
          value: "wordpress"
        - name: mysql_user
          value: wordpress
        - name: mysql_password
          value: "123456"
```
### 启用资源清单
```shell
kubectl apply -f wordpress-mysql-svc-deployment.yaml -n wordpress 
```
## coredns
### coredns解析流程
- client pod查询自身的/etc/resolv.conf文件中指向的dns服务器地址，此地址为kube-dns service的地址，即将解析请求转发给名为kube-dns的service

- kube-dns service会将请求转发到后端coredns pod，为了dns的高可用，通常有两个coredns pod，并位于kube-system名称空间

- coredns pod根据corefile的配置会连接到在default名称空间的名为kubernetes的service，而kubernetes service对应的endpoints为所有kube-apiserver:6443的地址

- kubernetes service监视service ip的变动，维护dns解析记录，并将变化发送至etcd实现dns记录的存储

- coredns查询到service name对应的ip后返回给客户端

- 如果查询的是外部域名，coredns无法解析，就转发给指定的域名服务器，一般是宿主机节点上/etc/resolv.conf的服务器解析


### 查看pod内部的域名解析
```shell
# 进入容器内部
[root@master201 ~]#kubectl exec -it myapp-547df679bb-5hk2w -- sh
[root@myapp-547df679bb-5hk2w /]# host kubernetes.default
kubernetes.default.svc.cluster.local has address 10.96.0.1
[root@myapp-547df679bb-5hk2w /]# cat /etc/resolv.conf 
# 执行coredns的service ip
nameserver 10.96.0.10
search default.svc.cluster.local svc.cluster.local cluster.local
# ndots:5 表示点少于5个的时候，补search后面的后缀，超过5个不补
options ndots:5
# 如果coredns查不到，则使用宿主机的resolv.conf上的域名服务器进行查询
[root@myapp-547df679bb-5hk2w /]# host www.baidu.com
www.baidu.com has address 220.181.38.149
www.baidu.com has address 220.181.38.150
www.baidu.com has ipv6 address 240e:83:205:58:0:ff:b09f:36bf
www.baidu.com has ipv6 address 240e:83:205:5a:0:ff:b05f:346b
www.baidu.com is an alias for www.a.shifen.com.
```

### 基于二进制kubernetes集群中的coredns部署
```shell
# 下载coredns的yaml文件
wget -o coredns.yaml https://raw.githubusercontent.com/coredns/deployment/master/kubernetes/coredns.yaml.sed

# 修改
apiversion: v1
kind: serviceaccount
metadata:
name: coredns
 namespace: kube-system
---
apiversion: rbac.authorization.k8s.io/v1
kind: clusterrole
metadata:
 labels:
   kubernetes.io/bootstrapping: rbac-defaults
 name: system:coredns
rules:
  - apigroups:
    - ""
   resources:
    - endpoints
    - services
    - pods
    - namespaces
   verbs:
    - list
    - watch
  - apigroups:
    - discovery.k8s.io
   resources:
    - endpointslices
   verbs:
    - list
    - watch
---
apiversion: rbac.authorization.k8s.io/v1
kind: clusterrolebinding
metadata:
 annotations:
   rbac.authorization.kubernetes.io/autoupdate: "true"
 labels:
   kubernetes.io/bootstrapping: rbac-defaults
 name: system:coredns
roleref:
 apigroup: rbac.authorization.k8s.io
 kind: clusterrole
 name: system:coredns
subjects:
- kind: serviceaccount
 name: coredns
 namespace: kube-system
---
apiversion: v1
kind: configmap
metadata:
 name: coredns
 namespace: kube-system
data:
 corefile: |
   .:53 {
       errors
       health {
         lameduck 5s
       }
       ready
#此处cluster_domain修改cluster.local,reverse_cidrs 修改为 in-addr.arpa ip6.arpa
       kubernetes cluster_domain reverse_cidrs {  
         fallthrough in-addr.arpa ip6.arpa
       }
       prometheus :9153
       forward . upstreamnameserver {     #此处upstreamnameserver修改为/etc/resolv.conf
         max_concurrent 1000
       }
       cache 30
       loop
       reload
       loadbalance
   }stubdomains
---
apiversion: apps/v1
kind: deployment
metadata:
 name: coredns
 namespace: kube-system
 labels:
   k8s-app: kube-dns
   kubernetes.io/name: "coredns"
spec:
  # replicas: not specified here:
  # 1. default is 1.
  # 2. will be tuned in real time if dns horizontal auto-scaling is turned on.
 replicas: 2                   #添加此行为多副本,默认为1
 strategy:
   type: rollingupdate
   rollingupdate:
     maxunavailable: 1
 selector:
   matchlabels:
     k8s-app: kube-dns
 template:
   metadata:
     labels:
       k8s-app: kube-dns
   spec:
     priorityclassname: system-cluster-critical
     serviceaccountname: coredns
     tolerations:
        - key: "criticaladdonsonly"
         operator: "exists"
     nodeselector:
       kubernetes.io/os: linux
     affinity:
         podantiaffinity:
           requiredduringschedulingignoredduringexecution:
           - labelselector:
               matchexpressions:
               - key: k8s-app
                 operator: in
                 values: ["kube-dns"]
             topologykey: kubernetes.io/hostname
     containers:
  - name: coredns
       image: coredns/coredns:1.9.4
       imagepullpolicy: ifnotpresent
       resources:
         limits:
           memory: 170mi  #此处的资源限制修改为合适的值,比如:4096mi
         requests:
           cpu: 100m      #此处的资源限制修改为合适的值
           memory: 70mi   #此处的资源限制修改为合适的值
       args: [ "-conf", "/etc/coredns/corefile" ]
       volumemounts:
        - name: config-volume
         mountpath: /etc/coredns
         readonly: true
       ports:
        - containerport: 53
         name: dns
         protocol: udp
        - containerport: 53
         name: dns-tcp
         protocol: tcp
        - containerport: 9153
         name: metrics
         protocol: tcp
       securitycontext:
         allowprivilegeescalation: false
         capabilities:
           add:
            - net_bind_service
           drop:
            - all
         readonlyrootfilesystem: true
       livenessprobe:
         httpget:
           path: /health
           port: 8080
           scheme: http
         initialdelayseconds: 60
         timeoutseconds: 5
         successthreshold: 1
         failurethreshold: 5
       readinessprobe:
         httpget:
           path: /ready
           port: 8181
           scheme: http
     dnspolicy: default
     volumes:
        - name: config-volume
         configmap:
           name: coredns
           items:
            - key: corefile
             path: corefile
---
apiversion: v1
kind: service
metadata:
name: kube-dns
 namespace: kube-system
 annotations:
   prometheus.io/port: "9153"
   prometheus.io/scrape: "true"
 labels:
   k8s-app: kube-dns
   kubernetes.io/cluster-service: "true"
   kubernetes.io/name: "coredns"
spec:
 selector:
   k8s-app: kube-dns
 clusterip: cluster_dns_ip  #修改此处为kube-dns svc的地址,比如:10.96.0.10,可通过查看pod的/etc/resolv.conf 获取
 ports:
  - name: dns
   port: 53
   protocol: udp
  - name: dns-tcp
   port: 53
   protocol: tcp
  - name: metrics
   port: 9153
   protocol: tcp
```
```shell
#修改上面文件内容汇总
[root@master1 ~]#vim coredns.yaml
cluster_domain: cluster.local
reverse_cidrs: in-addr.arpa ip6.arpa
upstreamnameserver: /etc/resolv.conf
cluster_dns_ip: 10.96.0.2
#应用创建coredns的pod
[root@master1 ~]#kubectl apply -f coredns.yaml
```

### coredns工作机制
每个service资源对象，在coredns上都会自动生成如下格式的名称，结合该名称会生成对应的一些不同类型的dns资源记录
```shell
<service>.<ns>.svc.<zone>
<service>： #当前service对象的名称
<ns>：      #当前service对象所属的名称空间
<zone>：    #当前kubernetes集群使用的域名后缀，默认为“cluster.local” ，用 kubeadm init --service-dns-domain 指定
```

kuberadm安装方式时查看默认zone名称
```shell
[root@master1 ~]#kubeadm config print init-defaults |grep dns
dns: {}
dnsdomain: cluster.local
```

### coredns的配置策略
kubernetes支持单个pod资源规范上自定义dns解析策略和配置，并组合生效
- pod.spec.dnspolicy: 解析策略
- pod.spec.dnsconfig: 名称解析机制

#### pod.spec.dnspolicy策略
- default： 从运行在宿主机节点/etc/resolv.conf继承dns名称解析相关的配置
- clusterfirst: 
  - 此为默认值，优先使用集群内dns服务上的即系集群域内的名称，其他域名解析则交由宿主机节点/etc/resolv.conf的名称服务器
- clusterfirstwithhostnet:
  - 在容器使用宿主机网络的情况下，仍然使用clustfirst策略
- none
  - 用于忽略kubernetes集群的默认设定，仅使用由dnsconfig自定义的配置
  

#### pod.spec.dnsconfig
- nameservers <[]string>：dns名称服务器列表，附加于由dnspolicy生成的dns名称服务器之后
- searches <[]string>：dns名称解析时的搜索域，附加由于dnspolicy生成的搜索域之后
- options <[]object>：dns解析选项列表，同dnspolicy生成的解析选项合并成最终生效的定义

### 创建pod并修改coredns配置
相当于指定pod的专有dns解析方式（很不方便）
```shell
[root@master1 yaml]#cat service-pod-with-dnspolicy.yaml 
apiversion: v1
kind: pod
metadata:
 name: service-pod-with-dnspolicy
 namespace: default
spec:
 containers:
  - name: demo
   image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
   imagepullpolicy: ifnotpresent
 dnspolicy: none
 dnsconfig:         # 修改dns配置
   nameservers:
    - 10.96.0.10
    - 180.76.76.76
    - 223.6.6.6
   searches: 
    - svc.cluster.local
    - cluster.local
    - wang.org
   options:
    - name: ndots
     value: "5"    #意味着如果域名中只有5个或更少的点，则系统会尝试在其末尾添加搜索域。
```


### coredns配置
```shell
#coredns的配置是存放在 configmap中
[root@master1 ~]#kubectl get cm -n kube-system
name                                 data   age
coredns                              1     27d
.....

[root@master1 ~]#kubectl get cm coredns -n kube-system -o yaml
apiversion: v1
data:
 corefile: |
   .:53 {
errors
       health {
           lameduck 5s
       }
       ready
       kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
           ttl 30
       }
       prometheus :9153
       forward . /etc/resolv.conf {
           max_concurrent 1000
       }
       cache 30
       loop
       reload
       loadbalance
   }
kind: configmap
metadata:
 creationtimestamp: "2021-03-04t15:36:36z"
 name: coredns
 namespace: kube-system
 resourceversion: "219"
 uid: d6307d21-8c84-4302-9b95-a8058188333e
```

![alt text](images\image4.png)

不使用默认的转发策略，使用自定义的转发策略
```shell
#修改配置文件
root@master1:~# kubectl edit cm coredns -n kube-system
...
       rewrite name myapp.wang.org myapp.default.svc.cluster.local #将集群外的域名
重写为集群内的域名再进行解析
       kubernetes cluster.local in-addr.arpa ip6.arpa
       forward . /etc/resolv.conf {
           max_concurrent 1000
           except www.baidu.com.                    #排除www.baidu.com，不进行解析，
注意：最后面的点
       }
       hosts {                                     #添加三行，实现指定域名的解析,此优
先级比forward高
           10.0.0.100 harbor.cluster.local harbor.wang.org
           10.0.0.101 nfs.wang.org
           fallthrough
       }
       ...
#注意：多个dns地址间用空格隔开,排除的域名最好在末尾添加 “.”，对于之前的旧版本来说可能会出现无法查询的现象
#重建coredns，加快dns配置信息生效
[root@master1 ~]#kubectl delete pod -l kubernetes-app=kube-dns -n kube-system
```

## headless service 

### 无头服务使用场景

#### 有标签选择器，或者没有标签选择器但是有与service同名的endpoint资源
主要应用于有状态服务的stateful资源对象

#### 无标签选择器且也没有与service对象同名的endpoint资源
主要用于集群外部externalname类型的service

#### 无头服务管理域名格式
```shell
$(service_name).$(kubernetes_namespace).svc.cluster.local
```

#### 案例
```shell
# 无头服务标志就是clusterip为none
kubectl create service clusterip service-headless-cmd --clusterip="none"
```

## 存储管理
存储卷的配置由两部分组成
- 通过spec.volumes字段定义在pod之上的存储卷列表，它经由特定的存储插件并结合特定的存储供给方的接口进行定义
- 嵌套定义在容器的`volumemounts`字段上的存储卷挂载列表，它只能挂载当前pod对象中定义的存储卷

pod内部容器使用存储卷有两步
- 在pod上定义存储卷，并关联至目标存储服务上volumes
- 在需要用到存储卷的容器上，挂载其其所属的pod中pause的存储卷volumesmount

pod的卷资源对象属性
```yaml
apiversion: v1
kind: pod
metadata:
  name: <string>
  namespace: <string>
spec:
  volumes:                     # 定义卷, spec.volumes
  - name: <string>             # 卷名
  vol_type <object>            # 类型
  containers:
  - name:
    image:
    volumemounts:               # 引用卷, spec.containers.volumemounts
      - name: <string>          # 引用卷名
        mountpath: <string>
        readonly: <bool>
        subpath: <string>
        subpathexpr: <string>
```
### emptydir

emptydir 数据存放在宿主机路径如下
```shell
/var/lib/kubelet/pods/pod_id/volumes/kubernetes.io~empty-dir/<volume_name>/<file>
# 此目录随着pod的删除，也会随之删除，不能实现持久化
```

#### emptydir特点
- 此为默认存储类型
- 此方式只能临时存放数据，不能实现数据持久化
- 跟随pod初始化而来，开始是空数据卷
- pod被删除，emptydir对应的宿主机目录也被删除，当然目录内的数据随之永久消除 
- emptydir主机可以为同一个pod内多个内容共享
- emptydir容器数据的临时存储目录主要用于数据缓存和同一个pod内的多个容器共享使用

#### emptydir属性解析
```shell
kubectl explain pod.spec.volumes.emptydir
    medium      # 指定媒介类型，主要由default和memory
    sizelimit   # 当前存储卷的空间限额，默认值为nil表示不限制

kubectl explain pod.spec.containers.volumemounts
    mountpath   # 挂载到容器中的路径，此目录会自动生成
    name        # 指定挂载的volumes名称
    readonly    # 是否只读挂载
```

#### 示例
```yaml
# cat storage-emptydir-2.yaml
apiversion: v1
kind: pod
metadata:
  name: storage-emptydir
spec:
  volumes:
  - name: nginx-data
    emptydir: {}
  containers:
  - name: storage-emptydir-nginx
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumemounts:
    - name: nginx-data
      mountpath: /usr/share/nginx/html/
  - name: storage-emptydir-busybox
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/busybox:1.32.0
    volumemounts:
    - name: nginx-data
      mountpath: /data/
    command:
    - "/bin/sh"
    - "-c"
    - "while true; do date > /data/index.html; sleep 1; done"
```

### hostpath
hostpath可以将宿主机上的目录挂载到pod中作为数据的存储目录

#### hostpath的使用场景
- 容器应用程序中某些文件需要永久保存
- pod删除，hostpath数据对应在宿主机文件不受影响，即hostpath的生命周期和pod不同，而和节点相同
- 宿主机和容器的目录都会自动加载 (目录自动生成)
- 某些容器应用需要用到容器自身的内部数据，可将宿主机的/var/lib/[docker|containerd]挂载到pod中

#### hostpath使用注意事项
- 不同宿主机的目录和文件不一定完全相同，所以pod迁移前后的访问效果不一样
- 不适合deployment这种分布式资源，更适合daemonset
- 宿主机的目录不属于独立的资源对象的资源，所以对资源设置的资源配额限制对hostpath目录无效

#### 配置属性
```shell
# 配置属性
kubectl explain pod.spec.volumes.hostpath
path  # 指定哪个宿主机的目录或文件将共享给pod使用
type  # 指定路径的类型，一共有7种，
     空字符串  # 默认配置，在关联hostpath存储卷之前不进行任何检查，如果宿主机没有对应的目录，会自动创建
     directoryorcreate   # 宿主机上不存在，创建此755权限的空目录，属主属组均为kubelet
     directory  # 必须存在，挂载已存在的目录
     fileorcreate #宿主机上不存在挂载文件，就创建0644权限的空文件，属主属组同为kubelet
     file         # 必须存在的文件
     socket       # 事先必须存在socket文件路径
     chardevice   # 事先必须存在字符设备文件路径
     blockdevice  # 事先必须存在的块设备文件路径
```

#### 示例
```yaml
apiversion: v1
kind: pod
metadata:
  name: test-pod
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumemounts:
    - mountpath: /test-pod
      name: test-volume
  volumes:
  - name: test-volume
    hostpath:
      path: /data
      type: directory
```

#### 实现redis数据持久化
```yaml
apiversion: v1
kind: pod
metadata:
  name: hostpath-redis
spec:
  nodename: node.wang.org    # 指定运行在指定worker主机上
  volumes:
  - name: redis-backup
    hostpath:
      path: /backup/redis
  containers:
    - name: hostpath-redis
      image: redis:6.2.5
      volumemounts:
      - name: redis-backup
        mountpath: /data
```


### 网络存储共享

#### 实现nfs的网络共享存储

使用nfs提供的共享目录存储数据时，需要在系统中部署一个nfs环境，通过volume的配置，实现pod的容器间共享nfs目录

属性解析
```shell
# 配置属性
kubectl explain pod.spec.volumes.nfs
server         # 指定nfs服务器的地址
path           # 指定nfs服务器暴露的共享地址
readonly       # 是否只读，默认false

# 配置格式
  volumes:
  - name: <卷名>
    nfs:
      server: nfs_server_address
      path: "共享目录"
      readonly: false

# 注意：要求kubernetes所有集群都必须支持nfs客户端命令，所有节点都必须执行 apt -y install nfs-common
```

示例
```yaml
apiversion: v1
kind: pod
metadata:
  name: test-pod
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumemounts:
      - mountpath: /my-nfs-data
        name: test-volume
  volumes:
  - name: test-volume
    nfs:
      server: my-nfs-server.example.com
      path: /my-nfs-volume
      readonly: true
```

#### 案例
使用集群外的nfs存储
```shell
# nfs服务器软件安装
apt update && apt install -y nfs-kernel-server 或者 nfs-server

# 配置共享目录
mkdir /nfs-data
echo '/nfs-data *(rw,all_squash,anonuid=0,anongid=0)' >> /etc/exports

# 重启服务
exportfs -r
# 查看nfs
exportfs -v
```

资源清单
```yaml
apiversion: v1
kind: pod
metadata:
  name: volumes-nfs
spec:
  volumes:
  - name: redisdatapath
    nfs:
      server: nfs.feng.org
      path: /data/nfs/redis
  containers:
  - name: redis
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/redis:6.2.5
    volumemounts:
    - name: redisdatapath
      mountpath: /data
```

更改dns设置，转发只指定dns服务器
```shell
kubectl edit cm coredns -n kube-system
```
```yaml
apiversion: v1
data:
  corefile: |
    .:53 {
        errors
        health {
           lameduck 5s
        }
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
           ttl 30
        }
        prometheus :9153
        # 添加转发
        forward . 10.0.0.129 {
           max_concurrent 1000
        }
        cache 30
        loop
        reload
        loadbalance
    }
kind: configmap
metadata:
  creationtimestamp: "2024-07-15t05:08:40z"
  name: coredns
  namespace: kube-system
  resourceversion: "599520"
  uid: e766f12b-6f34-4acc-be90-65130bc4ee69
```

### pv和pvc
pvc负责提出需求
pv负责提供解决方案
客户(pod)提出pvc的需求，pvc根据需求匹配pv（解决方案）来达到存储目的

pv(persistent volume)
- 工作中的存储资源一般都独立于pod的，将之称为资源对象pv，是由管理员设置的存储，它是kubernetes集群的一部分，pv是volume之类的卷插件，但是具有独立于pv的pod的生命周期

pv与volume的区别
- pv是集群级别的资源，负责将存储空间引入到集群中，通常有管理员定义
- pv就是kubernetes集群中的网络存储，不属于namespace，node，pod等资源，但可以被他们访问
- pv有自己独立的生命周期

#### pv和pvc的配置流程

- 集群管理员创建一个存储解决方案（比如nfs）
- 管理员创建一个pv，pv定义了一个存储的具体实现，保留使用多大存储，哪种模式等
- 用户提出pvc
- 如果pvc能够匹配到合适的pv，则实现绑定
- 用户创建一个pod并使用卷关联pvc 

#### pv的两种解决方案
- 静态
  - 集群管理员预先手动创建一些pv。它们有可供集群用户使用的实际存储细节

- 动态
  - 集群尝试根据用户请求动态地自动完成创建卷，此配置基于storageclass；pvc必须请求存储类，并且管理员必须预先创建并配置该storageclass才能进行动态创建
  - 声明该类为""（空字符），可以有效地禁用其动态配置

#### pv属性
```shell
# pv 作为存储资源，主要包括存储能力，访问模式，存储类型，回收策略等关键信息
kubectl explain pv.spec
    capacity(容量)        # 定义pv使用多少资源，仅限于空间的设定
    accessmodes          # 访问模式，支持单路读写，多路读写，单路只读，多路只读，可同时支持多种模式
    volumemode            # 文件系统或块设备，默认文件系统·
    mountoptions          # 挂载选项：比如["ro","soft"]
    persistentvolumereclaimpolicy  # 资源回收策略，主要三种retain,delete,recycle
    存储类型               # 每种存储类型的样式的属性名称都是专有的
    storageclassname      # 存储类的名称，如果配置必须和pvc的storageclass一致

# 示例
# pv在意存储细节，需明确具体实现
apiversion: v1
kind: persistentvolume
matadata:
  name: pv0003
  labels:
    release: "stable"    # 便签可以支持匹配过滤pvc
spec：
  capacity:
    storage: 5gi
  volumemode: filesystem
  accessmodes:
    - readwriteonce
  persistentvolumereclaimpolicy: recycle
  storageclassname: slow   # 必须和pvc匹配
  mountoptions:
    - hard
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2
```

#### pvc属性
```shell
pvc属性信息，与所有空间都能使用的pv不一样，pvc是属于名称空间级别的资源对象，即只有特定的资源才能使用
kubectl explain pvc.spec
    accessmodes     # 访问模式
    resources       # 资源限制
    volumemode      # 后端存储卷的模式，文件系统或块，默认为文件系统
    volumename      # 指定绑定的卷(pv)的名称

kubectl explain pods.spec.volumes.persistentvolumeclaim
    claimname
    readonly       # 设定pvc是否只读
    storageclassname    # 存储类的名称，如果配置必须和pv的storageclassname相同才能绑定
    selector            # 标签选择器实现选择绑定pv
    # selector 选择算符
    # pvc可以设置标签选择算符，来进一步过滤集合，只有标签与选择算符相匹配的卷能够绑定到pvc上。选择算符包含两个字段
    matchlabels - 卷必须包含带有此值的标签
    matchexpressionis - 通过设定键(key)、值列表和操作符(operator)来构造的需求。合法的操作符有in、notin、exists和doesnotexists
```

- 示例
```yaml
apiversion: v1
kind: persistentvolumeclaim
metadata:
  name: myclaim
spec:
  accessmodes:
    - readwriteonce
  volumemode: filesystem
  resources:
    request:
      storage: 8gi
  storageclassname: slow  # 必须和pv相同
  selector:
    matchlabels:
      release: "stable"
    matchexpressions
      - {kye: environment, operator: in, values: [dev]}
```


### 属性进阶
#### pv状态(面试重点)
create pv ---> pending ---> avaliable ---> bound ---> released ---> delete
create pv ---> pending ---> avaliable ---> bound ---> released ---> faild

状态解析：
- availabled:
  - 空闲状态，表示pv没有被其他pvc对象使用
- bound：
  - 绑定状态，表示pv已经被其他pvc对象使用
- release
  - 未回收状态，表示pvc已经被删除了，但资源还没有被回收
- faild
  - 资源回收失败

create pvc ---> pending ---> bound ---> delete

#### accessmode 访问模式

- readwriteonde(rwo)
  - 单节点读写，卷可以被`一个节点`以读写方式挂载
  - readwriteonce访问模式仍然可以在同一节点上运行的多个pod,访问该卷即不支持并行写入（非并发）
- readonlymany(rox)
  - 多节点只读
- readwritemany(rwx)
  - 多节点读写
- readwriteoncepod(rwop)
  - 卷可以被单个pod以读写方式挂载
  - 如果你想确保整个集群中只有一个pod可以读取或写入该pvc，请使用rwop访问模式

#### pv资源回收策略
当pod结束volume后可以回收资源对象，删除pvc，而绑定关系就不要存在了，当绑定关系不存在后，这个pv如何处理，这里pc的回收策略告诉集群在存储卷声明释放后应如何处理该pv卷。目前，volume的处理策略有`保留`，`回收`和`删除`

- retain
  - 保留pv和存储空间数据，后续数据的删除需要人工干预，一般推荐使用此项，对于手动创建的pv，此为默认值
- delete
  - 相关的存储实例pv和数据都一起删除，需要支持删除功能的存储才能实现，动态存储一般会默认采用此方式
- recycle
  - 已废弃

#### pv和pvc使用流程
实现方法
- 准备存储
- 基于存储创建pv
- 根据需求创建pvc
  - pvc会根据capacity和accessmode及其它条件自动找到相匹配的pv进行绑定，一个pvc对应一个pv
- 创建pod
  - 在pod的volumes指定调用上面创建pvc的名称
  - 在pod中的容器中的volumemounts指定pvc挂载容器内的目录路径

#### pv和pvc使用案例
```yaml
# 创建service网络, 无头服务
apiversion: v1
kind: service
metadata:
  name: mysql
spec:
  ports:
  - port: 3306
  selector:
    app: mysql
  clusterip: none   # 只能用域名访问：mysql.default.svc.cluster.lical
---
# 创建deployment
apiversion: apps/v1
kind: deployment
metadata:
  name: mysql
spec:
  selector:
    matchlabels:
      app: mysql
  strategy:
    type: recreate
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - image: mysql:8.0
        name: mysql
        env:
          # 实际中使用secret
        - name: mysql_root_password
          value: password
        ports:
        - containerport: 3306
          name: mysql
        volumemounts:
        - name: mysql-persistent-storage
          mountpath: /var/lib/mysql
      volumes:
      - name: mysql-persistent-storage
        persistentvolumeclaim:
          claimname: mysql-pv-claim
---
apiversion: v1
kind: persistentvolume
metadata:
  name: mysql-pv-volume
  labels:
    type: local
spec:
  storageclassname: manual
  capacity:
    storage: 20gi
  accessmodes:
    - readwriteonce
  hostpath:            # 用的本地存储
    path: "/mnt/data"
---
apiversion: v1
kind: persistentvolumeclaim
metadata:
  name: mysql-pv-claim
spec:
  storageclassname: manual
  accessmodes:
    - readwriteonce
  resources:
    requests:
      storage: 20gi
```

#### 以nfs类型创建一个3g大小的存储资源对象pv
```yaml
# 准备nfs共享存储
# 在所有worker节点安装nfs软件
# 准备pv，定制一个具体空间大小的存储对象
apiversion: v1
kind: persistentvolume
metadata:
  name: pv-test
spec:
  capacity:
    storage: 3gi
  accessmodes:
    - readwriteonce
    - readwritemany
    - readonlymany
  nfs:
    path: /nfs-data
    server: nfs.wang.org  # 需要域名解
```

#### subpath

`volumemounts.subpath`属性可用于指定所引用的卷内的子路径，而不是其根路径
```yaml
apiversion: v1
kind: pod
metadata:
  name: my-lamp-site
spec:
  containers:
  - name: mysql
    image: mysql:8.0
    env:
    - name: mysql_root_password
      value: "rootpasswd"
    volumemounts:
    - mountpath: /var/lib/mysql
      name: site-data
      subpath: mysql
  - name: php
    image: php:8.1-apache
    volumemounts:
    - mountpath: /var/www/html
      name: site-data
      subpath: html      # 假设pv的指定路径是/data/nfs
                         # 则该挂载路径是/data/nfs/html
  volumes:
  - name: site-data
    persistentvolumeclaim:
      claimname: my-lamp-site-data
```

### storageclass

#### 基于storageclass的动态置备

- 在kubernetes中，storageclass是集群级别的资源，而不是名称空间级别

storageclass对象会定义下面两部分内容
- pv的属性，比如存储类型，volume的大小等
- 创建这种pv需要用到的存储插件

提供以上两个信息，kubernetes就能够根据用户提交的pvc，找到一个对应的storageclass，之后kubernetes就会调用该storageclass声明的存储插件，进而创建出需要的pv

要使用storageclass，就得安装对应的自动配置程序，比如存储后端使用的是nfs，那么就需要使用到一个nfs-client的自动配置程序，也称为provisioner，这个程序使用已经配置好的nfs服务器，来自动创建持久卷pv


storageclass api

每个sorageclass都包含`provisioner`,`parameters`和`reclaimpolicy`字段，这些字段会在storageclass需要动态置备persistentvolume时会使用到。
storageclass对象的命名很重要，用户使用这个命名来请求生成一个特定的类。当创建storageclass对象时，管理员设置storageclass对象的命名和其他参数

```yaml
apiversion: storage.k8s.io/v1
kind: storageclass
metadata:
  name: standard
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
reclaimpolicy: retain
allowvolumeexpansion: true
mountoptions:
  - debug
volumebindingmode: immediate | waitforfirstconsumer
# immediate pod创建后立即绑定pv和pvc
# waitforfirstconsumer pod准备好后，根据pod的情况再创建pv和pvc

# 管理员可以为没有申请绑定到特定storageclass的pvc指定一个默认的存储类
apiversion: v1
kind: persistentvolumeclaim
metadata:
  name: myclaim
spec:
  accessmodes:
    - readwriteonce
  volumemode: filesystem
  resources:
    requests:
      storage: 8gi
  storageclassname: standard
  selector:
    matchlabels:
      release: "stable"
    matchexpressions:
      - {key: environment, operator: in, values: [dev]}
```

存储制备器
- 每个storageclass都有一个制备器（provisioner），用于提供存储驱动，用来决定使用哪个卷插件制备pv。该字段必须指定

#### nfs的制备器解决方案

kubernetes不包含内部nfs驱动。需要使用外部驱动创建storageclass
- nfs ganesha服务器和外部驱动
- nfs subdir外部驱动
```shell
# kubernetes-sigs k8s兴趣小组
https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner
```

### local volume

#### hostpath存在的问题
- 由于集群内每个节点的差异化，要使用hostpath volume，我们需要通过nodeseletor等方式进行精确调度，这种事情多了，你就会不耐放，暴躁，疯狂，啊啊啊啊啊啊啊！！！
- 注意directoryorcreate和fileorcreate两种类型的hostpath，当node上没有对应的file/directory时，你需要保证kubelet有在node上create file/directory的权限
- scheduler并不会考虑hostpath volume的大小，hostpath也不能申明需要的storagesize，这样调度时存储的考虑，就需要人为检查并保证

#### local pv使用场景
local persistent volume它的使用范围非常固定
- 高优先级的系统应用
  - 需要在多个不同节点上存储数据
  - 对i.o要求较高
  - 比如：
    - 分布式数据存储mongodb
    - 分布式文件系统ceph
- 其次，使用local persistent volume的应用必须具备数据备份和恢复的能力，允许你把这些数据定时备份在其他位置

#### local pv和hostpath的区别
常规的pv(hostpath)是先调度pod到某个节点，然后在持久化这台机器上的volume目录
- 也就是说挂载的实际目录是在确定pod调度到某节点之后，再决定的，实际挂载目录依赖于pod调度到的节点

local pv允许用户通过标准pvc接口以简单可移植的方式访问node节点的本地存储。
- pv的定义中需要包含描述节点亲和性的信息，k8s系统则使用该信息将容器调度到正确的node节点
- local类型的pv是一种更高级的本地存储抽象，它可以允许通过storageclass来进行管理
- 与`hostpath`相比，`local volume`可以声明为动态供应，并且可以利用节点标签(nodeaffinity)实现存储亲和性，确保pod调度到包含所需数据的节点上。而`hostpath`卷在pod重建后可能会调度至新的节点，而导致旧的数据无法使用。

- 总结：local pv因为是抽象成一种pv资源对象，因此可以限制大小，且可以挂载到指定节点

#### local pv的风险
`local`卷仍然取决于底层节点的可用性，并不适合所有应用的程序。如果节点变得不健康，那么`local`卷也将变得不可被pod访问。使用它的pod将不能运行。使用local卷的应用程序必须能够容忍这种可用性的降低，以及因底层磁盘的耐用性特征而带来的潜在的数据丢失风险

#### local卷的创建
```yaml
apiversion: storage.k8s.io/v1
kind: storageclass
metadata:
  name: local-storage
# 表示存储类不使用任何provisioner，即不支持动态分配持久卷。这意味着管理员需要手动创建并管理持久卷
provisioner: kubernetes.io/no-provisioner
volumebindingmode: waitforfirstconsumer  # 延迟绑定
---
apiversion: v1
kind: persistentvolume
metadata:
  name: example-pv
spec:
  capacity:
    storage: 100gi
  volumemode: filesystem
  accessmodes:
  - readwriteonce
  persistentvolumereclaimpolicy: delete
  storageclassname: local-storage
  local:
    # 实现准备目标节点目录，对于本地存储kubernetes本身不会自动创建路径
    # 因为kubernetes不能控制节点上的本地存储，因此无法自动创建
    path: /mnt/disks/ssd1
  nodeaffinity:
    required:
      nodeselectorterms:
      - matchexpressions:
        - key: kubernetes.io/hostname
          operator: in
          values:
          - example-node
```
- 使用`local`卷时，需要设置persistentvolume对象的nodeaffinity字段。kubernetes调度器使用persistentvolume的nodeaffinity信息来将使用`local`卷的pod调度到正确的节点。
- 使用`local`卷时，建议创建一个storageclass并将其`volumebindingmode`设置为`waitforfirstconsumer`。      

使用local卷的流程
- 创建pv，使用nodeaffinity指定绑定的节点提供存储
- 创建pvc，绑定pv的存储条件
- 创建pod，引用前面的pvc和pv实现local存储

```yaml
apiversion: storage.k8s.io/v1
kind: storageclass
metadata:
  name: local-storage
provisioner: kubernetes.io/no-provisioner
volumebindingmode: waitforfirstconsumer 
# 延迟绑定，只有pod启动后再绑定pv到pod所在节点，否则pvc处于pending状态
---
apiversion: v1
kind: persistentvolume
metadata:
  name: pv-sc-local
spec:
  capacity:
    storage: 100gi
  volumemode: filesystem
  accessmodes:
  - readwriteonce
  persistentvolumereclaimpolicy: delete
  storageclassname: local-storage
  local:
    path: /data/www/
  nodeaffinity:
    required:
      nodeselectorterms:
      - matchexpressions:
        - key: kubernetes.io/hostname
          operator: in
          values:
          - node2.wang.org
---
apiversion: v1
kind: persistentvolumeclaim
metadata:
  name: pvc-sc-local
spec:
  storageclassname: local-storage
  accessmodes: ["readwriteoncde"]
  resources:
    requests:
      storage: 100mi
---
apiversion: v1
kind: pod
metadata:
  name: pod-sc-local-demo
spec:
  containers:
  - name: pod-sc-local-demo
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx.1.20.0
    volumemounts:
      - name: pvc-sc-local
        mountpath: "/usr/share/nginx/html/"
  restartpolicy: "never"
  volumes:
    - name: pvc-sc-local
      persistentvolumeclaim:
        claimname: pvc-scp-local
```

### nfs的存储制备器方案
#### 基于nfs-subdir-external-provisione创建nfs共享存储的storageclass

创建nfs共享存储的storageclass步骤如下
- 创建nfs共享
- 创建service account并授予管控nfs provisioner在k8s集群中运行的权限
- 部署nfs-subdir-external-provisioner对应的deployment
- 创建storageclass负责建立pvc并调用nfs provisioner进行预定的工作，并让pv与pvc建立联系
- 创建pvc时自动调用sc创建pc

在nfs服务器上增加一个规则
```shell
# vim /etc/exports
/data/sc-nfs *(rw,no_root_squash)

# 创建该目录
mkdir -p /data/sc-nfs
# 添加权限
chmod 777 /data/sc-nfs
# 加载配置
exportfs -r
```

创建serviceaccount并授权
```shell
# ls
namespace.yaml
nfs-client-provisioner.yaml 
nfs-storageclass.yaml 
rbac.yaml
```

创建一个名称空间（生产环境中，独立项目建议单独创建一个名称空间中）
```yaml
# cat namespace.yaml
apiversion: v1
kind: namespace
metadata:
  name: sc-nfs
```

创建serviceaccount（rbac）,创建账号并授权
```yaml
# cat rbac.yaml
apiversion: v1
kind: serviceaccount   # 账号
metadata:
  name: nfs-client-provisioner
  namespace: sc-nfs
---
apiversion: rbac.authorization.k8s.io/v1
kind: clusterrole   # 权限
metadata:
  name: nfs-client-provisioner-runner
rules:
  - apigroups: [""]
    resources: ["nodes"]
    verbs: ["get","list","watch"]
  - apigroups: [""]
    resources: ["persistentvolumes"]
    verbs: ["get","list","watch","create","delete"]
  - apigroups: [""]
    resources: ["persistentvolumeclaims"]
    verbs: ["get","list","watch","update"]
  - apigroups: ["storage.k8s.io"]
    resources: ["storageclasses"]
    verbs: ["get","list","watch"]
  - apigroups: [""]
    resources: ["events"]
    verbs: ["create","update","patch"]
---
apiversion: rbac.authorization.k8s.io/v1
kind: clusterrolebinding
metadata:
  name: run-nfs-client-provisioner
subjects:
  - kind: serviceaccount
    name: nfs-client-provisioner
    namespace: sc-nfs
roleref:
  kind: clusterrole
  name: nfs-client-provisioner-runner   # 将权限关联给账号使用
  apigroup: rbac.authorization.k8s.io
---
apiversion: rbac.authorization.k8s.io/v1
kind: role
metadata:
  name: leader-locking-nfs-client-provisioner
  namespace: sc-nfs
rules:
  - apigroups: [""]
    resources: ["endpoints"]
    verbs: ["get","list","watch","create","update","patch"]
---
apiversion: rbac.authorization.k8s.io/v1
kind: rolebinding
metadata:
  name: leader-locking-nfs-client-provisioner
  namespace: sc-nfs
subjects:
  - kind: serviceaccount
    name: nfs-client-provisioner
    namespace: sc-nfs
roleref:
  kind: role
  name: leader-locking-nfs-client-provisioner  # 将权限关联给账号使用
  apigroup: rbac.authorization.k8s.io
```

部署nfs-subdir-external-provisioner对应的deployment
这个镜像就是提供nfs制备器的应用程序
```yaml
# cat nfs-client-provisioner.yaml
apiversion: apps/v1
kind: deployment
metadata:
  name: nfs-client-provisioner
  labels:
    app: nfs-client-provisioner
  # replace with namespace where provisioner is deployed
  #namespace: default
  namespace: sc-nfs
spec:
  replicas: 1
  strategy:
    type: recreate
  selector:
    matchlabels:
      app: nfs-client-provisioner
  template:
    metadata:
      labels:
        app: nfs-client-provisioner
    spec:
      serviceaccountname: nfs-client-provisioner
      containers:
        - name: nfs-client-provisioner
          image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nfs-subdir-external-provisioner:v4.0.2
          #image: wangxiaochun/nfs-subdir-external-provisioner:v4.0.2
          #image: k8s.gcr.io/sig-storage/nfs-subdir-external-provisioner:v4.0.2
          imagepullpolicy: ifnotpresent
          volumemounts:
            - name: nfs-client-root
              mountpath: /persistentvolumes
          env:
            - name: provisioner_name
              value: k8s-sigs.io/nfs-subdir-external-provisioner #名称确保与 nfs-storageclass.yaml文件中的provisioner名称保持一致
            - name: nfs_server
              value: nfs.feng.org # nfs server_ip 
            - name: nfs_path
              value: /data/sc-nfs  # nfs 共享目录
      volumes:
        - name: nfs-client-root
          nfs:
            server: nfs.feng.org  # nfs server_ip 
            path: /data/sc-nfs  # nfs 共享目录
```

创建storageclass用来引用制备器
```yaml
#cat nfs-storageclass.yaml
apiversion: storage.k8s.io/v1
kind: storageclass
metadata:
  name: sc-nfs 
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"  # 是否设置为默认的storageclass
provisioner: k8s-sigs.io/nfs-subdir-external-provisioner # or choose another name, must match deployment's env provisioner_name'
parameters:
  archiveondelete: "true" # 设置为"false"时删除pvc不会保留数据,"true"则保留数据
```
后续只要使用storageclass创建pvc，就会自动创建pv

测试用例
```yaml
# cat pvc.yaml
apiversion: v1
kind: persistentvolumeclaim
metadata:
  name: pvc-nfs-sc
spec:
  storageclassname: sc-nfs
  accessmodes: ["readwritemany","readonlymany"]
  resources:
    requests:
      storage: 100mi
```
```yaml
# cat pod-test.yaml
apiversion: v1
kind: pod
metadata:
  name: pod-nfs-sc-test
spec:
  containers:
  - name: pod-nfs-sc-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    volumemounts:
      - name: nfs-pvc
        mountpath: "/usr/share/nginx/html/"
  restartpolicy: "never"
  volumes:
    - name: nfs-pvc
      persistentvolumeclaim:
        claimname: pvc-nfs-sc  #指定前面创建的pvc名称
```

## 配置管理
### configmap
kubernetes提供了对pod中容器应用的集中配置管理组件：configmap
通过configmap来实现向pod中的容器中注入配置信息的机制
可以把configmap理解为linux系统中的/etc/目录，专门用来存储配置文件的目录

configmap不仅仅可以保存单个属性，也可以用来保存整个配置文件
虽然configmap可以对各种应用程序提供定制配置服务，但是一般不用它来替代专门的配置文件

从kubernetesv1.19版本开始，configmap和secret支持使用immutable字段创建不可变实例，实现不可变基础设施效果

注意：configmap属于名称空间级别，只能被同一个名称空间的pod引用


#### configmap基本属性
```shell
kubectl explain cm
    binarydata           # 二进制数据
    data                 # 文件数据，支持变量和文件
    immutable <boolean>  # 设为true，不能被修改只能删除，默认为nil可以随时被修改
# 注意：基于data的方式传递信息的话，会在pod容器内部生成一个单独的数据文件
```

#### 数据配置格式
```shell
# 单行配置数据格式
属性名称key: 属性值value       # 单行配置内容，一般保存变量，参数等
文件: 单行内容                 # 配置文件如果只有一行，也使用此方式，key为文件名，value为内容

# 多行文件数据格式
文件名称1: |                   # 注意：|是多行键值的标识符
    文件内容1                  # 内容大小不能超过1m
    文件内容2
    ...
文件名称2: |                   # 注意：|是多行键值的标识符
    文件内容1                  # 内容大小不能超过1m
    文件内容2
    ...

# 一般多行文件数据格式不需要自己写，可以直接生成
```

### configmap创建和更新
#### 命令行创建方式
```shell
kubectl create configmap name [--from-file=[key=]source] [--from-literal=key1=value1] [--dry-run=server|client|none] [-n namespace] [option]

# 参数详解：
--from-literal=key1=value1             # 以设置键值对的方式实现变量配置数据
--from-env-file=/path/to/file          # 以环境变量专用文件的方式实现配置数据
--from-file=[key=]/path/to/file        # 以配置文件的方式创建配置文件数据，如不指定key，file名称为key名,key表示后续在pod中生成的文件名，file表示当前文件名
--from-file=/path/to/dir               # 以配置文件所在目录的方式创建文件数据

--dry-run=client -o yaml               # 测试运行并显示cm内容以yaml格式

# 查看configmap
kubectl create configmap <cm_name> -n <namesapce> [-o yaml] --dry-run=client
kubectl get configmap <cm_name> -n <namespace>
kubectl describe configmap <cm_name> -n <namespace>

# 删除configmap
kubectl delete configmap <cm_name> [-n <namespace>]
```


#### 命令行创建方式案例
命令行创建基于key/value形式的变量配置
```shell
root@master101:~# kubectl create cm cm-test1 --from-literal=key1=value1 --from-literal=key2=value2
configmap/cm-test1 created
root@master101:~# kubectl get cm
name               data   age
cm-test1           2      12s
kube-root-ca.crt   1      8d

root@master101:~# kubectl get cm cm-test1 -o yaml
apiversion: v1
data:
  key1: value1                  # 如果键是数字，必须加双引号或单引号
  key2: value2
kind: configmap
metadata:
  creationtimestamp: "2024-07-25t17:33:52z"
  name: cm-test1
  namespace: default
  resourceversion: "40963"
  uid: 7970123b-44ab-4c8c-8100-12570464f5c3
```

#### 命令行创建多个配置文件
```shell
root@master101:~# kubectl create cm cm-test2 --from-file=conf/app1.conf --from-file=conf/app2.conf --dry-run=client -o yaml
apiversion: v1
data:
  app1.conf: |
    server {
        listen 80；
        server_name web.wang.org;
        root /data/web01;
    }
  app2.conf: |
    server {
        listen 88；
        server_name web.wang.org;
        root /data/web02;
    }
kind: configmap
metadata:
  creationtimestamp: null
  name: cm-test2
```

#### 资源清单文件格式
一般不会手写，建议直接生成后修改，即可使用


### configmap使用
使用configmap主要有两种方式
- 通过环境变量的方式直接传递pod
- 使用volume的方式挂载到pod内的文件中

注意
- configmap必须在pod之前创建
- 与configmap在同一个namespace的pod才能使用configmap，即configmap不能跨命名空间调用
- configmap通常存放的数据不要超过1m(从性能方面考虑)
- cm支持实时更新，在原来的pod里面直接看到效果

#### 通过环境变量的方式直接传递pod
方式1：env对指定的变量一个一个赋值
```shell
kubectl explain pod.spec.containers.env
    name         # 手工定制环境变量，设置环境变量的名称，必选字段
    value        # 手工定制环境变量时，直接设置环境变量的属性值，不通过cm获取配置，可选字段
    valuefrom    # 手工定制环境变量时，设置环境变量来源，可以支持cm，secret，downwordapi获取

kubectl explain pod.spec.containers.env.valuefrom.configmapkeyref
    name         # 引用指定的configmap
    key          # 引用指定的configmap中的具体哪个key
    optional     # 如果设置为false，标识该项是必选项，如果设置为true，标识这个key是可选项
```

方式2：envfrom使用cm的所有变量实现对变量的批量赋值，此方式生产更为推荐
```shell
kubectl explain pod.spec.containers.envfrom
    configmapref    # configmap对象中的所有key
    secretkeyref    # secret对象中的所有key
    prefix          # 为configmap中的每个属性都添加前缀标记
```
#### configmap-env变量案例
```yaml
apiversion: v1
kind: configmap
metadata:
  name: cm-nginx-config
data:
  port: "10086"
  user: "www"
---
apiversion: v1
kind: pod
metadata:
  name: configmap-env-test
spec:
  containers:
  - name: configmap-env-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx.1.20.0
    env:
    - name: nginx_host
      value: "10.0.0.100"  # 直接变量赋值
    - name: nginx_port
      valuefrom:
        configmapkeyref:
          name: cm-nginx-config
          key: port
          optional: true  # 表可选项
    - name: nginx_user
      valuefrom:
        configmapkeyref:
          name: cm-nginx-config
          key: user
          optional: false  #表必选项
```

#### 范例：envfrom批量导入所有变量
```yaml
# cat storage-configure-simple-envfrom.yaml
apiversion: v1
kind: configmap
metadata:
  name: cm-nginx
data:
  nginx_port: "10086"
  nginx_user: "www"
---
apiversion: v1
kind: pod
metadate:
  name: configmaq-envfrom-test
spec:
  containers:
  - name: configmap-envfrom-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    envfrom:
    - configmapref:
        name: cm-nginx   # 所有变量从cm中读取
        ...
```
#### 使用volume的方式挂载到pod内的文件中
#### 范例：volume生成配置文件并更新生效
```yaml
apiversion: v1
kind: configmap
metadata:
  name: cm-volume
data:
  author: wangxiaochun
  file.conf: |
    [app]
    config1
    cnnfig2
---
apiversion: v1
kind: pod
metadata:
  name: pod-volume-test
spec:
  volumes:
    - name: volume-config
    configmap:
      name: cm-volume
  containers:
    - name: nginx
      image: regsitry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
      volumemounts:
      - name: volume-config   # 调用前面定义的卷面
        mountpath: /cmap/     # 指定pod中的挂载目录
```

在线修改configmap中的值，pod内的配置文件也会变，本质是因为configmap挂载的配置文件本质上是一个双层软连接，
```shell
file.conf -> ..data/file.conf
..data/file.conf -> ..<timetemp> # 该时间戳就是configmap的生成时间，configmap一变，这个时间戳文件也会变，里面的内容就也会变
```
#### kubectl cp命令
```shell
kubectl cp pod-volume-test:/etc/nginx/nginx.conf ./nginx.conf
```

#### volume挂载cm中部分文件
```shell
# 准备配置文件
ls nginx-conf.d/
default.conf myserver.conf myserver-gzip.cfg myserver-status.cfg

# 配置文件
[root@master1 ~]#cat nginx-conf.d/myserver.conf 
server {
   listen 8888;
   server_name www.wang.org;
   include /etc/nginx/conf.d/myserver-*.cfg;
   location / {
       root /usr/share/nginx/html;
   }
}

#子配置文件,注意:文件是以cfg为后缀,不能以conf文件后缀,会导致冲突
[root@master1 ~]#cat nginx-conf.d/myserver-gzip.cfg 
gzip on;
gzip_comp_level 5;
gzip_proxied     expired no-cache no-store private auth;
gzip_types text/plain text/css application/xml text/javascript;
[root@master1 ~]#cat nginx-conf.d/myserver-status.cfg 
location /nginx-status {
   stub_status on;
   access_log off;
}

# 创建cm
kubectl create cm cm-nginx-conf-files --from-file=nginx-conf.d/

# 清单文件
cat storage-configmap-nginx-subfile.yaml
```
```yaml
apiversion: v1
kind: configmap
metadata:
  name: cm-nginx-index
data:
  index.html: "nginx sub configmap page!\n"
---
apiversion: v1
kind: pod
metadata:
  name: pod-cm-nginx-conf
spec:
  volumes:
  - name: nginx-conf
    configmap:
      name: cm-nginx-conf-files
      items:                        # 指定cm中的key
      - key: myserver.conf          # cm中key的名称
        path: myserver.conf         # pod中的文件名
        mode: 0644                  # pod中的文件权限
      - key: myserver-status.cfg
        path: myserver-status.cfg
        mode: 0644
      - key: myserver-gzip.cfg
        path: myserver-gzip.cfg
        mode: 0644
      optional: false
  - name: nginx-index
    configmap:
      name: cm-nginx-index
      optional: false
  containers:
  - image:  registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: pod-cm-nginx-conf-container
    volumemounts:
    - name: nginx-conf
      mountpath: /etc/nginx/conf.d/
      readonly: true
    - name: nginx-index
      mountpath: /usr/share/nginx/html/
      readonly: true
```


#### volume基于subpath实现挂载cm部分文件并修改配置文件名称
```yaml
apiversion: v1
kind: configmap
metadata:
  name: cm-nginx-index
data:
  index.html: "nginx sub configmap page!\n"
---
apiversion: v1
kind: pod
metadata:
  name: pod-cm-nginx-conf
spec:
  volumes:
  - name: nginx-conf
    configmap:
      name: cm-nginx-conf-files
      optional: false
  - name: nginx-index
    configmap:
      name: cm-nginx-index
      optional: false
  containers:
  - image:  registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: pod-cm-nginx-conf-container
    volumemounts:
    - name: nginx-conf
      mountpath: /etc/nginx/conf.d/myserver2.conf   # 修改生成的配置文件名
      subpath: myserver.conf     # 指定nginx-conf中的特定文件，而非所有文件
      readonly: true
    - name: nginx-conf
      mountpath: /etc/nginx/conf.d/myserver-gzip2.cfg
      subpath: myserver-gzip.cfg
      readonly: true
    - name: nginx-index
      mountpath: /usr/share/nginx/html/
      readonly: true
```

#### volume基于subpath挂载cm部分文件并保留原目录中的其他文件
```yaml
apiversion: v1
kind: pod
metadata:
  name: pod-cm-nginx-conf
spec:
  volumes:
  - name: volume-nginx-conf
    configmap:
      name: cm-nginx-conf
      items:
      - key: nginx.conf
        path: etc/nginx/nginx.conf  # 必须是相对路径，且和下面subpath路径相同
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: pod-cm-nginx-conf-conftainer
    command: ["sh","-c","sleep 3600"]
    volumemounts:
    - name: volume-nginx-conf
      mountpath: /etc/nginx/nginx.conf
      subpath: etc/nginx/nginx.conf
```

### secret
#### secret分类
- generic
  - opaque
  - kubernetes.io/service-account-token
  - kubernetes.io/ssh-auth
  - kubernetes.io/basic-auth
  - bootstrap.kubernetes.io/token
- tls
  - kubernetes.io/tls
- docker-registry
  - kubernetes.io/dockerconfigjson
  - kubernetes.io/dockercfg

#### secret创建方式
- 手动创建：用户执行创建的secret常用来存储用户私有的一些信息
- 自动创建：集群自动创建的secret用来作为集群中各个组件之间的通信的身份校验使用

#### secret命令式创建
```shell
# generic类型
kubectl create secret generic name [--type=string] [--from-file=[key=]source] [--from-literal=key1=value1]

# --from-literal=key1=value1   以命令行设置键值对的环境变量方式配置数据
# --from-env-file=/path/file   以环境变量的专用文件的方式配置数据
# --from-file=[key=]/path/file 以配置文件的方式创建配置数据
# --from-file=/path/file       以配置文件所在目录的方式创建配置数据

# 该命令中的--type选项进行定义除了后面docker-registry和tls命令之外的其他子类型，有些类型有key的特定要求

# tls命令
kubectl create secret tls name --cert=/path/file --key=/path/file
# 其保存cert文件内容的key名称不能指定自动为tls.crt,而保持private key的key不能指定自动为tls.key

# docker-registry类型
# 方式1：基于用户名和密码方式实现
kubectl create secret docker-registry name --docker-username=user --docker-password=password --docker-email=email [--docker-server=string] [--from-file=[key=]source]

# 方式2：基于dockerconfig文件方式实现
kubectl create secret docker-registry keyname --from-file=.dockerconfigjson=path/to/.docker/config.json
```

#### secret引用
secret资源在pod中引用的方式有三种
- 环境变量
- secret卷
- 拉取镜像

#### generic案例
```shell
# 命令式创建
kubectl create secret generic secret-mysql-root --from-literal=username=root --from-literal=password=123456

#
[root@master201 nginx]#kubectl get secrets
name                type     data   age
secret-mysql-root   opaque   2      3s
[root@master201 nginx]#kubectl describe secrets secret-mysql-root 
name:         secret-mysql-root
namespace:    default
labels:       <none>
annotations:  <none>

type:  opaque

data
====
password:  6 bytes
user:      4 bytes 

# 账号密码被base64编码
[root@master201 nginx]#kubectl get secrets secret-mysql-root -o yaml
apiversion: v1
data:
  password: mtizndu2
  user: cm9vda==
kind: secret
metadata:
  creationtimestamp: "2024-07-28t06:25:33z"
  name: secret-mysql-root
  namespace: default
  resourceversion: "737849"
  uid: f438d3be-8755-4bb5-8870-7277256a907f
type: opaque
[root@master201 nginx]#echo mtizndu2 | base64 -d
123456
```

#### stringdata明文数据
```shell
cat storage-secret-opaque-stringdata.yaml
apiversion: v1
kind: secret
metadata:
  name: secret-stringdata
  namespace: default
type: opaque
# stringdata表示明文存放数据，data表示必须以base64编码存放
stringdata:
  user: 'admin'
  password: 'password'
```

#### secret引用实例
```yaml
apiversion: v1
kind: secret
metadata:
  name: secret-mysql
  type: kubernetes.io/basic-auth
data:
  username: cm9vdao=      # key名称：username
  password: mtizndu2      # key名称：password
---
apiversion: v1
kind: pod
metadata:
  name: pod-secret-mysql-init
spec:
  containers:
  - name: mysql
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
    env:
    - name: mysql_root_password
      valuefrom:
        secretkeyref:
          name: secret-mysql      # 引用指定的secret
          key: password           # 引用指定的secret中对应的key
          optional: false         # 必须存在
```

#### 通过卷调用secret
```yaml
# 清单文件
# cat storage-secret-test-pod.yaml
apiversion: v1
kind: secret
metadata:
  name: secret-test
type: kubernetes.io/basic-auth
data:
  username: ywrtaw4=
  password: cgfzc3dvcmq=
# 使用命令行的时候，命令行变量无需加密，但是清单的命令必须加密
---
# 调用secret的清单文件
apiversion: v1
kind: pod
metadata:
  name: secret
spec:
  volumes:
  - name: secret
    secret:
      secretname: secret-test   # 指定secret的名称
  containers:
    - name: secret-test-container
      image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
      volumemounts:
      - name: secret
        mountpath: /secret/
        readonly: true
```

### tls
tls类型的secret主要用于对https场景的证书和密钥文件来进行加密传输
```shell
# tls类型格式
kubectl create secret tls name --cert=/path/file --key=/path/file

# 注意：
# 保存cert文件内容的key名称不能指定，自动为tls.crt,卷挂载后生成的文件名也为tls.crt
# 保持private key文件内容的key不能指定，自动为tls.key,卷挂载后生成的文件名也为tls.key
```

#### tls案例
创建tls证书文件
```shell
# 生成私钥
openssl genrsa -out nginx-certs/www.wang.org.key 2048

# 生成自签名证书
openssl req -new -x509 -key nginx-certs/www.wang.org.key -days 3650 -out nginx-certs/wang.org.crt -subj/c=cn/st=beijing/l=beijing/o=devops/cn=www.wang.org
# 注意：cn指向的域名必须是nginx配置中使用的域名信息

# 创建tls类型的secret
kubectl create secret tls secret-nginx-ssl --cert=nginx-crets/www.wang.org.crt --key=nginx-certs/www.wang.org.key
```

准备nginx配置文件
```shell
# nginx主配置文件 myserver.conf
cat > myserver.conf
server {
    listen 80;
    server_name www.wang.org;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name www.wang.org;

    ssl_certificate /etc/nginx/certs/tls.crt;
    ssl_certificate_key /etc/nginx/certs/tls.key;

    ssl_session_timeout 5m;

    ssl_protocols tlsv1 tlsv1.1 tlsv1.2;

    ssl_ciphers ecdhe-rsa-aes128-gcm-sha256:high:!anull:!md5:!rc4:!dhe; 
    ssl_prefer_server_ciphers on;

    include /etc/nginx/conf.d/myserver-*.cfg;

    location / {
       root /usr/share/nginx/html;
    }
}

# nginx的压缩配置文件：myserver-gzip.cfg
cat > myserver-gzip.cfg
gzip on;
gzip_comp_level 5;
gzip_proxied     expired no-cache no-store private auth;
gzip_types text/plain text/css application/xml text/javascript;

# nginx的状态页配置文件myserver-status.cfg
cat > myserver-status.cfg
location /status {
   stub_status on;
   access_log off;
}
```

创建配置文件对应的configmap
```shell
kubectl create configmap cm-nginx-ssl-conf --from-file=nginx-ssl-conf.d/
```

创建引用secret和configmap资源配置文件
```yaml
# 创建资源配置文件
# cat storage-secret-nginx-ssl.yaml
apiversion: v1
kind: pod
metadata:
  name: pod-nginx-ssl
  namespace: default
spec:
  volumes:
  - name: nginx-certs
    secret:
      secretname: secret-nginx-ssl
  - name: nginx-confs
    configmap:
      name: cm-nginx-ssl-conf
      optional: false
  containers:
  - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
    name: nginx-ssl-server
    volumemounts:
    - name: nginx-certs
      mountpath: /etc/nginx/certs/
      readonly: true
    - name: nginx-confs
      mountpath: /etc/nginx/conf.d/
      readonly: true
```

### docker-registry
#### secret实现docker私有仓库
方法1：通过命令创建
```shell
kubectl create secret docker-registry keyname --docker-server=docker_registry_server --docker-username=docker_user --docker-password=docker_password --docker-email=email
```

#### 注意事项总结
- 将harbor的域名加入到docker-daemon.json的非安全组中
- 将dns指向harbor域名所在dns或者直接写hosts文件
- 建议将harbor.yaml中的hostname改为域名

### downwardapi
downwardapi不是一种独立的api资源类型，只是一种引用pod自身的运行环境信息
downwardapi包括pod的metadata，spec或status字段值，将这些信息注入到容器内部的方式

downwardapi提供了两种方式用于将pod的信息注入到容器内部
- 环境变量：用于单个变量，可以将pod信息和容器信息直接注入容器内部
- volume挂载：将pod信息生成为文件，再挂载到容器内部中

#### downwardapi案例
获取基本的变量信息通过变量方式引用
```yaml
# cat storage-downwardapi-env-test.yaml
apiversion: v1
kind: pod
metadata:
  name: downwardapi-env-test
  labels:
    app: downwardapi-env
spec:
  containers:
    - name: downwardapi-env-test
      image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
      resource:
        requests:
          memory: "32mi"
          cpu: "250m"
        limits:
          memory: "64mi"
          cpu: "500m"
      env:
        - name: this_pod_name
          valuefrom:
            fieldref:
              fieldpath: metadata.name
        - name: this_pod_namespace
          valuefrom:
            fieldref:
              fieldpath: metadata.namespace
        - name: this_app_label
          valuefrom:
            fieldref:
              fieldpath: metadata.labels['app']
        - name: this_cpu_limit
          valuefrom:
            resourcefieldref:
              resource: limits.cpu
        - name: this_mem_request
          value.from
            resourcefieldref:
              resource: requests.memory
              divisor: 1mi
        - name: var_ref
          value: $(this_pod_namespace).wang.org  # 变量引用格式：$(var_name)
```

存储卷方式使用
```yaml
# cat storage-downwardapi-volume-test.yaml
apiversion: v1
kind: pod
metadata:
  name: downwardapi-volume-test
  labels:
    zone: beijing
    rack: zhongguancun
    app: redis-master
  annotations:
    region: asia-china
spec:
  volumes:
  - name: podinfo
    downwardapi:
      defaultmode: 0420  #文件权限，默认0644
      items:
      - fieldref:
          fieldpath: metadata.namespace
        path: pod_namespace
      - fieldref:
          fieldpath: metadata.labels
        path: pod_labels
      - fieldref:
          fieldpath: metadata.annotations
        path: pod_annotations
      - resourcefieldref:
          containername: downwardapi-volume-test
          resource: limits.cpu
        path: "cpu_limit"
      - resourcefieldref:
          containername: downwardapi-volume-test
          resource: requests.memory
          divisor: "1mi"
        path: "mem_request"
  containers:
    - name: downwardapi-volume-test
      image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
      resources:
        requests:
          memory: "32mi"
          cpu: "250m"
        limits:
          memory: "64mi"
          cpu: "500m"
      volumemounts:
      - name: podinfo
        mountpath: /etc/podinfo
        readonly: false
# 属性解析：defaultmode 表示挂载文件后，文件的权限限制，items定制自己的一些名称
#应用资源对象
[root@master1 ~]#kubectl apply -f storage-downwardapi-volume-test.yaml

#查看效果
[root@master1 ~]#kubectl get pod
name                     ready   status   restarts   age
downwardapi-volume-test   1/1     running   0         2s

[root@master1 ~]#kubectl exec -it downwardapi-volume-test -- ls /etc/podinfo/
cpu_limit       pod_annotations pod_namespace
mem_request     pod_labels
```

### projected
之前的cm，secret等卷资源在pod内的一个目录同时只能挂载一个卷，而我们有时希望在一个目录内生成来自多个卷的多个文件
projected volumes是一种特殊的卷类型，支持同时投射多个卷至同一个挂载点

projected volume仅支持对如下四种类型的卷（数据源）进行投射操作
- secret：投射secret对象
- configmap：投射configmap对象
- downwardapi：投射pod元数据
- serviceaccounttoken: 投射serviceaccounttoken

#### projected案例
```yaml
cat storage-projected-demo.yaml
apiversion: v1
data:
  username: d2fuz3hpyw9jahvu
kind: secret
metadata:
  name: mysecret
  namespace: default
type: opaque
---
apiversion: v1
data:
  myconfig: hello,myconfig
kind: configmap
metadata:
  name: myconfigmap
  namespace: default
---
apiversion: v1
kind: pod
metadata:
  name: projected-volume-demo
spec:
  containers:
  - name: container-test
    image: registry.cn-beijing.aliyuncs.com/wangxiaochunpod-test:v0.1
    volumemounts:
    - name: all-in-one
      mountpath: "/projected-volume"
      readonly: true
  volumes:
  - name: all-in-one
    projected:
      sources:
      - secret:
          name: mysecret
          items:
            - key: username
              path: my-group/my-username
      - downwardapi:
          items:
            - path: "labels"
              fieldref:
                fieldpath: metadata.labels
            - path: "cpu_limit"
              resourcefieldref:
                containername: container-test
                resource: limits.cpu
      - configmap:
          name: myconfigmap
          items:
            - key: myconfig
              path: my-group/my-config
```

#### projected案例2
```yaml
apiversion: v1
kind: pod
metadata:
 name: volume-test
spec:
 containers:
  - name: container-test
   image: busybox:1.28
   volumemounts:
    - name: all-in-one
     mountpath: "/projected-volume"
     readonly: true
 volumes:
  - name: all-in-one
   projected:
     sources:
      - secret:
         name: mysecret
         items:
            - key: username
             path: my-group/my-username
      - secret:
         name: mysecret2
         items:
            - key: password
             path: my-group/my-password
             mode: 511
```

## kubernetes流量调度ingress
### ingress原理
ingress主要包含两个组件ingress api和ingress controller
ingress其具备了动态更新并加载新配置的特性。而且ingress本身是不具备实现集群内外流量通信的功能的，这个功能是通过controller来实现的。ingress controller本身是运行于集群中的pod资源对象

ingress不会公开任意端口或协议，将http和https以外的服务公开到internet时，通常使用`service.type=nodeport`或`service.type=loadblancer`类型的service

#### ingress访问过程
- 从外部流量调度到kubernetes中ingress service，有多中实现方案，比如使用节点网络中的externalip或者nodeport方式
- 从service调度到ingress-controller
- ingress-controller根据ingress pod中的定义，比如虚拟主机或者后端的url
- 根据虚拟主机名直接调度到后端的一组应用pod中

注意：
- 整个流程中涉及了两处service内容
- service ingress-nginx是帮助ingress controller pod接入外部流量的
- 后端的服务对应的service只起到帮助ingress controller pod找到具体的服务的pod，即只用于服务发现(即通过标签选择器，查询后端的endpoint内的ip，端口数据)，而流量不需要经过后端服务的service，直接从ingress controller pod转到具体的pod
- 后端service负责服务发现，然后有ingress直接访问后端的pod

总结：
- ingress ---> 查询 --->  Service(endpoint[ip:port]) ingress通过查询service，得到后端的待访问pod的Socket数据
- ingress根据socket直接访问后端的pod，此时不需要经过Service


#### ingress controller常见的解决方案
ingress资源配置指定ingress controller类型的方法
- 专用的annotation：kubernetes.io/ingress.class(旧)
- ingress资源的spec的专有字段：ingressclassname，引用的ingressclass是一种特定的资源类型(新)

### 基于yaml mainifests部署ingress-nginx
```shell
# 获取配置文件
wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.1/deploy/static/provider/cloud/deploy.yaml

# 下载后，修改镜像地址
#image: registry.k8s.io/ingress-nginx/controller:v1.11.1@sha256:XXXX
image: registry.cn-hangzhou.aliyuncs.com/google_containers/nginx-ingress-controller:v1.11.1

# image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.4.1@sha256:XXX
# 有两个地方引用这个镜像，都需要改成阿里云的
image: registry.cn-hangzhou.aliyuncs.com/google_containers/kube-webhook-certgen:v1.4.1

# 该yaml文件中，有一个资源是name: ingress-nginx-controller（kind: Service）
# 该资源的作用：负责客户端请求使用该service文件找到ingress-nginx-controller的pod,该service不用改，默认为LoadBalancer,前提是装MetaLB，来提供IP池

# 建立多副本
# 方法1就是将deployment添加replicas=2
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app...
    ...
spec:
  replicas: 2    # 高可用

# 方法2：可以修改为DaemonSet提高性能（此步可选）

# 添加prometheus的检测端口
metadata:
  ...
  name: ingress-nginx-controller
  namespace: ingress-nginx
  annotations:                      # 添加如下三行，用于支持promethe监控，可选
    prometheus.io/scrape: "true"
    prometheus.io/port: "10254"
spec: 
  externalTrafficPolicy: Cluster   # 默认为Local, 如果service是LoadBalancer不用改，可以继续使用Local，已获得更好的性能
  
```

### ingress命令式实现
```shell
# 创建ingress的命令
kubectl create ingress name --rule=host/path=service:port[,tls[-secret]] [options]

# 常用选项
-- annotation=[]  # 注解信息，格式"annotation=value"
-- rule=[]        # 代理规则，注意：rule中外部域名要在所有名称空间唯一
-- class=''       # 此ingress适配的ingress class controller

# 基于uri方式代理不同应用的请求时，后端应用的uri若与代理时使用的uri不同，则需要启用url rewrite完成uri的重写
```

#### 准备后续实验中需要的service服务及后端pod
```shell
# 准备deployment
kubectl create deployment myapp1 --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas=3

# 创建对应的service
kubectl create service clusterip myapp1 --tcp=80:80
```

#### 使用ingress将集群暴露出去
```shell
# 单域名不支持子url
kubectl create ingress ingress-myapp1 --rule=myapp1.feng.org/=myapp1:80 --class=nginx
g
[root@master201 ingress-nginx]#kubectl get ingress
name             class    hosts             address   ports   age
ingress-myapp1   <none>   myapp1.feng.org             80      8s
```

#### 支持子路径
```shell
# 要想支持子路径，后面加*
kubectl create ingress ingress-myapp1 --rule=myapp1.feng.org/*=myapp1:80 --class=nginx
```

#### 单域名多url(不支持子url)
```shell
# 准备第二套deployment和service
kubectl create deployment myapp2 --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2 --replicas=3

kubectl create svc clusterip myapp2 --tcp=80:80

# 实现单域名多url, 这种方法会报错
# 因为域名上/v1，后端的service也会/v1，但是后端service没有/v1这个url
kubectl create ingress ingress-myapp --rule=myapp.feng.org/v1=myapp1:80 --rule=myapp.feng.org/v2=myapp2:80 --class=nginx
# 报错
[root@ubuntu2204 ~]#curl -h"host: myapp.feng.org" 10.0.0.12/v2
<!doctype html public "-//w3c//dtd html 3.2 final//en">
<title>404 not found</title>
<h1>not found</h1>
<p>the requested url was not found on the server. if you entered the url manually please check your spelling and try again.</p>

# 解决方案，加一个注解，表示重写后端的请求转发转到后端的根上
kubectl create ingress ingress-myapp --rule=myapp.feng.org/v1=myapp1:80 --rule=myapp.feng.org/v2=myapp2:80 --class=nginx --annotation nginx.ingress.kubernetes.io/rewrite-target="/"

```

#### 单域名多url支持子url
```shell
kubectl create ingress demo-ingress2 --rule='myapp.feng.org/v1(/|$)(.*)=myapp1:80' --rule='myapp.feng.org/v2(/|$)(.*)=myapp2:80' --class=nginx --annotation nginx.ingress.kubernetes.io/rewrite-target='/$2'
```

#### 多域名多url支持子url
```shell
kubectl create ingress ingress-myapp --rule="myapp1.feng.org/*=myapp1:80" --rule="myapp2.feng.org/*=myapp2:80" --class=nginx
```

### ingress实现https
#### 命令式实现https
```shell
# 基于tls的ingress要求事先准备专用的"kubernetes.io/tls"类型的secret资源对象
(umask 077; openssl genrsa -out feng.key 2048)

# 生成证书
openssl req -new -x509 -key feng.key -out feng.crt -subj /c=cn/st=beijing/o=sre/cn=www.feng.org -days 365

# 创建secret
kubectl create secret tls tls-feng --cert=./feng.crt --key=./feng.key

# 创建虚拟主机代理规则，同时将主机定义为tls类型，默认http自动跳转至https
kubectl create ingress tls-feng-ingress --rule='www.feng.org/*=myapp1:80,tls=tls-feng' --class=nginx

# 注意：启用tls后，该域名下的所有uri默认为强制将http请求利用308跳转至https，若不希望使用跳转功能，可以使用如下注解选项
--annotation nginx.ingress.kubernetes.io/ssl=redirect=false
# 即如下所示
kubectl create ingress tls-feng-ingress --rule='www.feng.org/*=myapp1:80,tls=tls-feng' --class=nginx --annotation nginx.ingress.kubernetes.io/ssl-redirect=false
```

#### 证书更新
https的证书的有效期一般为1年，到期前需要提前更新证书
```shell
# 重新颁发证书
(umask 077; openssl genrsa -out feng.key 2048)

# 生成证书
openssl req -new -x509 -key feng.key -out feng.crt -subj /c=cn/st=beijing/o=sre/cn=www.feng.org -days 365

# 方法1：
# 在线修改证书配置，需要提前先将新证书文件用base64编码并删除换行符
cat feng.crt|base64 | tr -d '\n'
cat feng.key|base64 | tr -d '\n'
# 上述生成的内容其他换下面命令的内容，立即生效
kubectl edit secrets tls-wang

# 方法2
# 删除旧证书配置
kubectl delete secrets tls-wang
# 创建新证书配置
kubectl create secret tls tls-feng --cert=./feng.crt --key=./feng.key
```

#### 获取客户端真实ip
```yaml
apiversion: networking.k8s.io/v1
kind: ingress
metadata:
  generation: 1
  name: ingress-myapp
  namespace: default
  annotations:
    nginx.ingress.kubernetes.io/enable-real-ip: "true"  # 允许ip透传
spec:
  ingressclassname: nginx
  rules:
  - host: www.wang.org
    http:
      paths:
      - backend:
          service:
            name: myapp
            port:
              number: 80
        path: /
        pathtype: prefix
```

### 案例：ingress nginx实现蓝绿发布
```yaml
# cat ingress-pod-test.yaml
apiversion: networking.k8s.io/v1
kind: ingress
metadata:
  name: pod-test
  #annotations:
  #  kubernetes.io/ingress.class: nginx
spec:
  ingressclassname: nginx  # 建议使用新版写法
  rules:
  - host: www.feng.org
    http:
      paths:
      - backend:
          service:
            name: myapp1      #myapp2  切换这里直接变更发布, 指向所需切换版本的svc
            port:
              number: 80
        path: /
        pathtype: prefix
```

### 案例：ingress nginx实现金丝雀（灰度）发布

ingress nginx的annotation支持的canary规则，annotation和label相似，也是保存资源对象上的元数据，但不能被标签选择器选择，且没有labels的名称最长63个字符的限制

- nginx.ingress.kubernetes.io/canary-weight
  - 基于服务权重进行流量切分，适用于蓝绿或灰度发布，权重范围0-100按百分比将请求路由到canary ingress中指定的服务
  - 权重为0意味着该金丝雀规则不会向canary入口的服务发送任何请求
  - 权重为100意味着所有请求都将被发送到canary入口

- nginx.ingress.kubernetes.io/canary-by-cookie:
  - 基于cookie的流量切分，适用于灰度发布与a/b测试
  - cookie值设置为always时，它将被路由到canary入口
  - cookie值设置为never时，请求不会被发送到canary入口
  - 对于任何其它值，将忽略cookie并将请求与其他金丝雀规则进行优先级比较

- nginx.ingress.kubernetes.io/canary-by-header
  - 基于该annotation中指定request header进行流量切分，适用于灰度发布以及a/b测试
  - 在请求报文中，若存在该header且其值为always时，请求将被发送到canary版本，注意always大小写敏感
  - 若存在该header且其值为never，请求将不会被发送至canary版本
  - 若存在该header且其值为其他任意值，将忽略该annotation指定的header，并按优先级将请求与其他金丝雀规则相比较
  - 若不存在header时，请求将不会被发送到canary
  
- nginx.ingress.kubernetes.io/canary-by-header-value
  - 基于该annotation中指定的request header的值进行流量切分，header名称则由前一个annotation(nginx.ingress.kubernetes.io/canary-by-header)进行指定
  - 请求报文中存在指定的header，且其值与该annotation的值匹配时，它将被路由到canary版本
  - 对于其他任何值，将忽略该annotation

- nginx.ingress.kubernetes.io/canary-by-header-pattern
  - 同canary-by-header-value的功能类似，但该annotation基于正则表达式匹配request header的值
  - 若该annotation与canary-by-header-value同时存在，则该annotation被忽略

#### 规则应用次序
- 优先级从低到高：canary-weight -> canary-by-cookie -> canary-by-header

#### 实战案例(前期准备)
- 初始环境，准备新旧两个版本应用及ingress
```shell
# 准备deployment
kubectl create deployment myapp1 --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1 --replicas=3

# 创建对应的service
kubectl create service clusterip myapp1 --tcp=80:80

# 准备第二套deployment和service
kubectl create deployment myapp2 --image=registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.2 --replicas=3

kubectl create svc clusterip myapp2 --tcp=80:80
```

- 创建ingress对应旧版本的应用
```yaml
# cat ingress-pod-test.yaml
apiversion: networking.k8s.io/v1
kind: ingress
metadata:
  name: pod-test
spec:
  ingressclassname: nginx
  rules:
  - host: www.feng.org
    http:
      paths:
      - backend:
          service:
            name: myapp1
            port:
              number: 80
        path: /
        pathtype: prefix
```

- 循环测试
```shell
[root@ubuntu2204 ~]#while true; do curl -h'host:www.feng.org' 10.0.0.12;sleep 1;done
kubernetes pod-test v0.1!! clientip: 10.244.5.62, servername: myapp1-57c65fd549-xkqsm, serverip: 10.244.4.85!
kubernetes pod-test v0.1!! clientip: 10.244.5.62, servername: myapp1-57c65fd549-xxp4k, serverip: 10.244.3.62!
kubernetes pod-test v0.1!! clientip: 10.244.5.62, servername: myapp1-57c65fd549-v6fbm, serverip: 10.244.5.58!
kubernetes pod-test v0.1!! clientip: 10.244.5.62, servername: myapp1-57c65fd549-xkqsm, serverip: 10.244.4.85!
kubernetes pod-test v0.1!! clientip: 10.244.5.62, servername: myapp1-57c65fd549-xxp4k, serverip: 10.244.3.62!
kubernetes pod-test v0.1!! clientip: 10.244.5.62, servername: myapp1-57c65fd549-xxp4k, serverip: 10.244.3.62!
kubernetes pod-test v0.1!! clientip: 10.244.5.62, servername: myapp1-57c65fd549-v6fbm, serverip: 10.244.5.58!
kubernetes pod-test v0.1!! clientip: 10.244.5.62, servername: myapp1-57c65fd549-v6fbm, serverip: 10.244.5.58!
```

#### 范例：基于权重的金丝雀发布
```yaml
# cat canary-by-weight.yaml
apiversion: networking.k8s.io/v1
kind: ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "30" # 通过更改比例，逐级发布
  name: pod-test-canary-by-weight
spec:
  ingressclassname: nginx
  rules:
  - host: www.feng.org
    http:
      paths:
      - backend:
          service:
            name: myapp2
            port:
              number: 80
        path: /
        pathtype: prefix
```

#### 范例：基于cookie实现金丝雀发布
```yaml
# cat canary-by-cookie.yaml
apiversion: networking.k8s.io/v1
kind: ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-cookie: "vip_user" # cookie中vip_user=always时才用金丝雀发布下面新版本
  name: pod-test-canary-by-cookie
spec:
  ingressclassname: nginx
  rules:
  - host: www.feng.org
    http:
      paths:
      - backend:
          service:
            name: myapp2
            port:
              number: 80
        path: /
        pathtype: prefix
```

- 验证是否成功
```shell
[root@ubuntu2204 ~]#while true; do curl -h'host:www.feng.org' -b"vip_user=always" 10.0.0.12;sleep 1;done
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sfwpt, serverip: 10.244.4.81!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-vjmxc, serverip: 10.244.5.60!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sfwpt, serverip: 10.244.4.81!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sctbx, serverip: 10.244.3.59!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-vjmxc, serverip: 10.244.5.60!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sctbx, serverip: 10.244.3.59!
```

#### 范例：基于请求header固定值的金丝雀发布
```yaml
# cat canary-by-header.yaml
apiversion: networking.k8s.io/v1
kind: ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-header: "x-canary" # x-canary首部字段为always时才使用金丝雀发布下面新版本，否则为旧版
  name: pod-test-canary-by-header
spec:
  ingressclassname: nginx
  rules:
  - host: www.feng.org
    http:
      paths:
      - backend:
          service:
            name: myapp2
            port:
              number: 80
        path: /
        pathtype: prefix
```

- 验证结果
```shell
[root@ubuntu2204 ~]#while true; do curl -h'host:www.feng.org' -h"x-canary: always" 10.0.0.12;sleep 1;done
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sctbx, serverip: 10.244.3.59!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sfwpt, serverip: 10.244.4.81!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sctbx, serverip: 10.244.3.59!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-vjmxc, serverip: 10.244.5.60!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sfwpt, serverip: 10.244.4.81!
```

#### 范例：基于请求header精确匹配指定值的金丝雀发布
```yaml
# cat > canary-by-header-value.yaml
apiversion: networking.k8s.io/v1
kind: ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-header: "isvip"
    nginx.ingress.kubernetes.io/canary-by-header-value: "true" # isvip首部字段的值为true就是用金丝雀发布新版，否则旧版
  name: pod-test-canary-by-header-value
spec:
  ingressclassname: nginx
  rules:
  - host: www.feng.org
    http:
      paths:
      - backend:
          service:
            name: pod-test-v2
            port:
              number: 80
        path: /
        pathtype: prefix
```

- 验证结果
```shell
[root@ubuntu2204 ~]#while true; do curl -h'host:www.feng.org' -h"isvip: true" 10.0.0.12;sleep 1;done
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-vjmxc, serverip: 10.244.5.60!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sfwpt, serverip: 10.244.4.81!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sctbx, serverip: 10.244.3.59!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sfwpt, serverip: 10.244.4.81!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-vjmxc, serverip: 10.244.5.60!
```

#### 范例：基于请求header正则表达式模式匹配的指定值的金丝雀发布
```yaml
# cat canary-by-header-pattern.yaml
apiversion: networking.k8s.io/v1
kind: ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-header: "username"
    nginx.ingress.kubernetes.io/canary-by-header-pattern: "(vip|vip)_.*"
    # 首部字段有username且正则匹配时，用新版，否则用旧版
  name: pod-test-canary-by-header-pattern
spec:
  ingressclassname: nginx
  rules:
  - host: www.feng.org
    http:
      paths:
      - backend:
          service:
            name: myapp2
            port:
              number: 80
        path: /
        pathtype: prefix
```

- 验证结果
```shell
[root@ubuntu2204 ~]#while true; do curl -h'host:www.feng.org' -h"username: vip_hahaha" 10.0.0.12;sleep 1;done
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sctbx, serverip: 10.244.3.59!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-vjmxc, serverip: 10.244.5.60!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-vjmxc, serverip: 10.244.5.60!
kubernetes pod-test v0.2!! clientip: 10.244.5.62, servername: myapp2-79c9d694f5-sfwpt, serverip: 10.244.4.81!`
```


## kubernetes安全机制
### 安全体系
用户访问Kubernetes业务应用的流程
- 无需api_server认证
  - 用户 --> Service(ingress-nginx) --> ingress(controller) --> service --> pod
- 基于api_server认证
  - 管理Kubernetes平台上各种应用现象

对于Kubernetes平台来说，几乎所有的操作基本上都是通过kube apiserver这个组件进行的，该组件提供HTTP RESTful形式的API集群内外客户端调用

对于Kubernetes集群的部署样式主要由两种：http形式和https形式

采用Kubernetes部署的形式默认对外是基于https的方式，而内部组件的通信是基于http方式

而Kubernetes的认证授权机制仅仅存在于https形式的api访问中，也就是说，如果客户端使用HTTP连接到kube-apiserver,那么是不会进行认证授权的，这样即增加了安全性，也不至于太复杂

Kubelet和kubeapi类似，提供一个简单的REST API服务，也监听一些TCP的套接字
- 10250：具有所有节点上Pod管理权限的读写端口，应谨慎管理
- 10255：仅提供只读操作，是REST API的子集，新版不再使用
- 10248：是本地healthz端点使用的端口

#### 安全基本流程
![alt text](images\image9.png)

kubernetes主要有两种用户
- User Account：普通人类用户(交互模式)
- Service Account: 集群内部的Pod用户(服务进程)

### kubernetes中的用户
#### user account(ua)
kubernetes并不包含用来代替普通用户账号ua的对象。普通用户的信息无法通过api调用添加到集群中

尽管无法通过 api 调用来添加普通用户， kubernetes 仍然认为能够提供由集群的证书机构签名的合法证书的用户是通过身份认证的用户。 基于这样的配置，kubernetes 使用证书中的 'subject' 的通用名称（common name）字段 （例如，"/cn=bob"）来确定用户名。 接下来，基于角色访问控制（rbac）子系统会确定用户是否有权针对某资源执行特定的操作。

#### 用户组
kubernetes中没有直接的方式去查看用户或用户组
对于用户组，kubernetes rbac可以使用“group”字段来限定对某些资源的访问。例如，您可能有一个rolebinding或clusterrolebinding，其subjects字段包括一个特定的group，这就意味着这个绑定是对应的用户组
- 示例
```shell
kubectl get clusterrolebindings.rbac.authorization.k8s.io kubeadm:cluster-admins -o yaml
apiversion: rbac.authorization.k8s.io/v1
kind: clusterrolebinding
metadata:
  creationtimestamp: "2024-07-15t05:08:32z"
  name: kubeadm:cluster-admins
  resourceversion: "217"
  uid: e83fa8a5-7f9b-4e4a-a293-9e9a7216ce62
roleref:
  apigroup: rbac.authorization.k8s.io
  kind: clusterrole
  name: cluster-admin #经该权限绑定到cluster-admins组上
subjects:
- apigroup: rbac.authorization.k8s.io
  kind: group    # subject中使用group类型表示组
  name: kubeadm:cluster-admins
```
- 查看cluster-admin权限
```yaml
# [root@master201 pki]#kubectl get clusterrole cluster-admin -o yaml
apiversion: rbac.authorization.k8s.io/v1
kind: clusterrole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  creationtimestamp: "2024-07-15t05:08:27z"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: cluster-admin
  resourceversion: "69"
  uid: 0713e60a-f683-4589-ba64-44b19a2faac0
rules:
- apigroups:
  - '*'
  resources:
  - '*'
  verbs:
  - '*'
- nonresourceurls:
  - '*'
  verbs:
  - '*'
```
- 证书上使用o(organization)表示组
```shell
# /etc/kubernetes/pki/apiserver-kubelet-client.crt
openssl x509 -in apiserver-kubelet-client.crt -text -noout
certificate:
    data:
        version: 3 (0x2)
        serial number: 914152039183806867 (0xcafb86fae3ff193)
        signature algorithm: sha256withrsaencryption
        issuer: cn = kubernetes
        validity
            not before: jul 15 05:03:13 2024 gmt
            not after : jul 15 05:08:14 2025 gmt
            # o表示组
        subject: o = kubeadm:cluster-admins, cn = kube-apiserver-kubelet-client
        subject public key info:
            public key algorithm: rsaencryption
                public-key: (2048 bit)
                modulus:
                    00:db:eb:ed:5a:06:11:6b:31:3c:d7:80:f8:d4:58:
                    12:ac:54:96:b3:20:70:3b:ba:5e:6c:0b:20:9b:d8:
                    66:bf:02:ba:d1:e2:27:6e:d9:0c:53:bf:cc:19:82:
                    6d:83:fc:74:64:b5:b8:ef:4c:18:cd:ac:d9:4c:20:
                    ...
```

### 认证机制-认证插件

#### kubelet启用身份认证
- kubelet的rest api端点默认通过tcp协议的10250端口提供，支持管理操作
- kubectl api
  - /pods
    - 列出当前kubelet节点上的pid
  - /run
    - 在一个容器内运行指定的命令
  - /exec
    - 在一个容器内运行指定的命令
  - /configz
    - 设置kubelet的配置文件参数
  - /debug
    - 调试信息
```shell
# 没有权限，需要验证后才能访问
[root@master201 pki]#curl -k https://127.0.0.1:10250/pods
unauthorized
```

- 查看kubelet的认证机制
```shell
#在每个worker节点查看
[root@node1 ~]#cat /var/lib/kubelet/config.yaml
apiversion: kubelet.config.k8s.io/v1beta1
authentication:
 anonymous:
   enabled: false      #匿名认证，true为允许匿名访问，但是权限不足
 webhook:
...

# 更改configmap，但是不能直接激活，需要删除kubelet的pod并重启
[root@master1 ~]#kubectl get cm -n kube-system|grep kubelet
kubelet-config                                         1      37h
```

#### x509客户端认证
- 案例：创建基于x509客户端普通的用户证书
```shell
# 查看到以下内容，表示默认kubernetes的ca签发的证书，都是k8s客户端的用户
[root@master201 pki]#grep '\-\-client-ca-file' /etc/kubernetes/manifests/kube-apiserver.yaml 
    - --client-ca-file=/etc/kubernetes/pki/ca.crt

# 在master节点创建test用户证书
# 创建test私钥
mkdir pki
(umask 077; openssl genrsa -out pki/test.key 4096)

# 生成证书申请文件，加入ops组只具有普通权限
openssl req -new -key pki/test.key -out pki/test.csr -subj "/cn=test/o=ops"

# 使用kubernetes-ca颁发证书
openssl x509 -req -days 3650 -ca /etc/kubernetes/pki/ca.crt -cakey /etc/kubernetes/pki/ca.key -cacreateserial -in pki/test.csr -out pki/test.crt

# 复制证书文件到worker节点
scp -r pki/ node1

# 指定apiserver地址和证书信息等信息，执行可以看到已识别用户test,但无权访问资源
kubectl get pod --server=https://kubeapi.feng.org:6443 --client-certificate=pki/test.crt --client-key=pki/test.key --certificate-authority=/etc/kubernetes/pki/ca.crt
error from server (forbidden): pods is forbidden: user "test" cannot list resource "pods" in api group "" in the namespace "default"
```

- 案例：创建x509客户端管理员的用户证书，并使用此证书访问kubernetes集群
```shell
# 创建管理员用户feng的证书
(umask 077; openssl genrsa -out pki/feng.key 4096)

# 生成证书申请文件，注意，加入system:masters组或kubeadm:cluster-admins组才具有管理权限
openssl req -new -key pki/feng.key -out pki/feng.csr -subj "/CN=feng/O=kubeadm:cluster-admins"

# 使用kubernetes-ca颁发证书
openssl x509 -req -days 3650 -ca /etc/kubernetes/pki/ca.crt -cakey /etc/kubernetes/pki/ca.key -cacreateserial -in pki/feng.csr -out pki/feng.crt

# 使用该证书执行kubectl指令
[root@node204 pki]#kubectl get pod --server=https://kubeapi.feng.org:6443 --client-certificate=./feng.crt --client-key=./feng.key --certificate-authority=/etc/kubernetes/pki/ca.crt
name                      ready   status    restarts        age
configmap-env-test2       1/1     running   4 (6h21m ago)   2d4h
myapp1-57c65fd549-v6fbm   1/1     running   2 (6h21m ago)   41h
myapp1-57c65fd549-xkqsm   1/1     running   2 (6h21m ago)   41h
myapp1-57c65fd549-xxp4k   1/1     running   2 (6h21m ago)   41h
myapp2-79c9d694f5-sctbx   1/1     running   1 (6h21m ago)   18h
myapp2-79c9d694f5-sfwpt   1/1     running   1 (6h21m ago)   18h
myapp2-79c9d694f5-vjmxc   1/1     running   1 (6h21m ago)   18h
pod-cm-nginx-conf         1/1     running   4 (6h21m ago)   2d4h
pod-nginx-ssl             1/1     running   4 (6h21m ago)   2d
pod-secret-volume         1/1     running   4 (6h21m ago)   2d1h
```

#### 静态令牌认证
静态令牌认证的配置说明
- 令牌信息保存于格式为csv的文本文件，每行定义一个用户，由“令牌，用户名，用户id和所属的用户组”四个字段组成，用户组为可选字段
```shell
格式：token,user,uid,"group1,group2..."
```
- 由kube-apiserver在启动时通过--token-auth-file选项加载
- 加载完成后如果再由文件变动，需要通过重启kube-apiserver进行重载
- 可在客户端在http请求中，通过“authorization bearer token”标头附带令牌以完成认证

静态令牌认证的配置过程
- 生成token，命令：`echo "$(openssl rand -hex 3).$(openssl rand -hex 8)"`
```shell
echo "$(openssl rand -hex 3).$(openssl rand -hex 8)"
```
- 生成static token文件
- 配置kube-apiserver加载该静态令牌文件以启用相应的认证功能
- 测试命令
```shell
# 方法1：
curl -k -h "authorization: bearer $token" https://api_server:6443/api/v1/namespace/default/pods/

# 方法2
kubectl --insecure-skip-tls-verify --token=$token -s https://kubeapi.feng.org:6443 get pod
```

范例：基于静态token令牌向api server添加认证用户
```shell
# 在所有master节点上配置下面过程，如果只有一个master节点配置，只能连接此master节点测试
# 准备token文件存放的独立目录
mkdir /etc/kubernetes/auth

# 创建静态令牌文件并添加用户信息
echo "$(openssl rand -hex 3).$(openssl rand -hex 8),feng,1001,ops" > /etc/kubernetes/auth/token.csv
echo "$(openssl rand -hex 3).$(openssl rand -hex 8),test,1002,dev" >> /etc/kubernetes/auth/token.csv

# 先备份配置文件，注意，不要将备份文件放在原目录下
cp /etc/kubernetes/manifests/kube-apiserver.yaml /tmp/

# 修改kube-apiserver.yaml, 共改三处
[root@master1 ~]#vim /etc/kubernetes/manifests/kube-apiserver.yaml 
......
  - command:
    - kube-apiserver
    - --advertise-address=10.0.0.200
    - --allow-privileged=true
    - --authorization-mode=node,rbac
    - --client-ca-file=/etc/kubernetes/pki/ca.crt
    - --token-auth-file=/etc/kubernetes/auth/token.csv  #指定前面创建文件的路径
.....
   volumemounts:
   ......
    - mountpath: /etc/kubernetes/auth                   #添加三行,实现数据卷的挂载配
置
     name: static-auth-token
     readonly: true
 hostnetwork: true
......
 volumes:
 .......
  - hostpath:                                           #添加三行数据卷定义
     path: /etc/kubernetes/auth
     type: directoryorcreate
   name: static-auth-token
#上面文件修改后,kubernetes会自动重启名为kube-apiserver-master1.wang.org的pod,可能需要等一会儿才能启动成功
[root@master201 auth]#kubectl get pod -n kube-system kube-apiserver-master201.feng.org 
name                                ready   status    restarts   age
kube-apiserver-master201.feng.org   1/1     running   0          3m43s

# 验证
token="cfbf31.2b7641894ef09341";curl -k -h "authorization: bearer $token" https://kubeapi.feng.org:6443/api/v1/namespaces/default/pods/

# 验证2
token="cfbf31.2b7641894ef09341";kubectl -s "https://kubeapi.feng.org:6443" --token="$token" --insecure-skip-tls-verify=true get pod -n kube-system
```

### kubeconfig管理
```shell
ll /etc/kubernetes/admin.conf
.kube/config  # 初始创建集群时由admin.conf复制得到
```
#### 管理Kubernetes集群所需信息
1. kube-api-server地址
2. 用户验证信息

需要准备一个文件，用来管理多个集群的访问，该文件就是Kubeconfig

#### kubeconfig文件格式
```yaml
clusters:
- cluster:
  name:
...

users:
- name:
  user:
...

contexts:
- context:
    cluster:
    user:
  name:
...

current-context: user@cluster
```
- cluster: 每个kubernetes集群的信息，包括集群对应访问端点(api server)的地址
- users: 认证到api server的用户的身份凭据列表
- contexts：将每个user同可认证的cluster建立关联关系的上下文列表
- current-context: 当前默认使用的context
  

客户端程序kubectl加载的kubeconfig文件的途径及从高到低优先级次序
- `--kubeconfig`选项，只支持一个文件
- kubeconfig环境变量：其值是包含有kubeconfig文件的列表，支持多个文件，用冒号隔离
- 默认路径：$home/.kube/config

#### kubeconfig创建和管理
`kubectl config`命令可以创建和管理kubeconfig文件

kubectl config简述
```shell
# 结果显示：对于一个用户账号，至少包含三部分
1. 用户条目-credentials 设定具体的user account名称
2. 集群-cluster 设定该user account所工作的区域
3. 上下文环境-context 设定用户和集群的关系
```

在集群外节点安装kubectl工具
```shell
#在集群外节点安装kubectl工具
#方法1
curl -s https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add -

cat << eof > /etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
eof

cat /etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main

apt update &> /dev/null
apt install -y kubectl

# 方法2
scp /usr/bin/kubectl 10.0.0.129:/usr/local/bin/
```

创建和使用kubeconfig流程
```shell
# 1. 在kubeconfig中添加集群信息
kubectl config set-cluster mykube --embed-certs=true --certificate-authority=/etc/kubernetes/pki/ca.crt --server="https://kubeapi.feng.org:6443" --kubeconfig=$home/.kube/mykube.conf

# 2. 在kubeconfig中添加用户凭证
# 方式1: x509数字证书认证
kubectl config set-credentials feng --embed-certs=true --client-certificate=./feng.crt --client-key=./feng.key --kubeconfig=$home/.kube/mykube.conf

# 方式2：静态令牌凭证
kubectl config set-credentials feng --token="xxxx" --kubeconfig=$home/.kube/mykube.conf

# 3. 在kubeconfig中添加context，实现集群和用户关联
kubectl config set-context feng@mykube --cluster=mykube --user=feng --kubeconfig=$home/.kube/mykube.conf

# 测试
kubectl --context='feng@mykube' get pods --kubeconfig=$home/.kube/mykube.conf

# 设置默认context
kubectl config use-context feng@mykube --kubeconfig=$home/.kube/mykube.conf

# 查看kubeconfig内容
kubectl config view --kubeconfig=$home/.kube/mykube.conf --raw

# 使用kubeconfig内容
1. kubectl get pods --kubeconfig=$home/.kube/mykube.conf
# 使用环境变量可以同时使多个文件生效，注意文件顺序，左边优先生效
# export kubeconfig="$home/.kube/kubeusers.conf:/etc/kubernetes/admin.conf"
2. export kubeconfig="$home/.kube/mykube.conf"; kubectl get pods
3. kubectl get pods # 将生成的文件改名为config，并放入默认路径
```

### service account管理
serviceaccount
- 基于资源对象保持serviceaccount的数据
- 认证信息保存于serviceaccount对象专用的secret中(v1.23版本前会自动创建和sa同名的secret，之后需要手动创建secret)
- 隶属于名称空间级别，专供集群上的pod中的进程访问api server时使用
- 需要用到特殊权限时，可为pod指定要使用的自定义serviceaccount资源对象
- 每个命名空间自动生成一个名称为default的sa用户
- 每个命名空间可以有很多sa
- sa内部有secret类型的token

在pod上使用service account
- 自动设定
  - service account通常有api server自动创建并通过serviceaccount准入控制器自动关联到集群中创建的每个pod上
  - kubernetes会自动为每个名称空间创建一个名为default的sa账号，并作为默认pod使用的sa账号
  - k8s自动为每个pod注入一个同一个名称空间名为default的serviceaccount及配套的令牌
  - default的sa账号权限有限，无法实行kubernetes管理性任务
- 自定义
  - 在pod规范上，使用serviceaccountname指定要使用的特定serviceaccount
- pod中的字段spec.imagepullsecrets
  - 可为pod提供从私有image registry获取时使用的docker-registry类型的secret的认证凭证
  - 为pod提供向私有image registry提供认证凭据的方法
    - pods.spec.imagepullsecrets: 直接调用的方式
    - pods.spec.serviceaccountname之地都给你使用的特有serviceaccount,而后在serviceaccount资源对象上，使用serviceaccounts.imagepullsecrets指定secret，此为间接调用的方式
- kubernetes基于三个组件完成pod上service account的自动化
  - serviceaccont admission controller
  - token controller
  - serviceaccount controller

- serviceaccount和token
  - serviceaccount使用专用的secret对象(kubernetesv1.23)存储相关的敏感信息
  - secret对象的类型标识为“kubernetes.io/serviceaccount”
  - 该secret对象会自动附带认证到apiserver用到的token，也称为serviceaccounttoken
  - 特殊场景：若需要一个永不过期的token，可手动创建serviceaccount专用类型的secret，并将其关联到serviceaccount上

#### 创建pod时，自动生成的token
```shell
# 进入pod内查看
kubectl exec -it demoapp-59768b6f4f-86tkt -- /bin/sh
cd /var/run/secrets/kubernetes.io/serviceaccount/

# ls -al
ls -al
total 4
drwxrwxrwt    3 root     root           140 Aug 27 05:41 .
drwxr-xr-x    3 root     root          4096 Aug 27 00:51 ..
drwxr-xr-x    2 root     root           100 Aug 27 05:41 ..2024_08_27_05_41_16.4288045796
lrwxrwxrwx    1 root     root            32 Aug 27 05:41 ..data -> ..2024_08_27_05_41_16.4288045796
lrwxrwxrwx    1 root     root            13 Aug 27 00:50 ca.crt -> ..data/ca.crt
lrwxrwxrwx    1 root     root            16 Aug 27 00:50 namespace -> ..data/namespace
lrwxrwxrwx    1 root     root            12 Aug 27 00:50 token -> ..data/token

# 查看pod的yaml清单中对secret的定义与挂载
kubectl get pod demoapp-59768b6f4f-86tkt -o yaml
...
# 关于serviceAccounttoken的挂载
volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-q9tz4
      readOnly: true
# 卷定义
  volumes:
  - name: kube-api-access-q9tz4
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

# pod内的文件情况
# cd /var/run/secrets/kubernetes.io/serviceaccount
[root@demoapp-59768b6f4f-86tkt /var/run/secrets/kubernetes.io/serviceaccount]# ls
ca.crt     namespace  token
```

#### 创建和使用sa账号
```shell
# 命令格式
# kubectl create seviceaccount name [--dry-run] [options]

# 文件格式
apiversion: v1
kind: serviceaccount
metadata:
  name: <sa名称>
  namespace: <名称空间名称>
```


#### 应用sa
在pod资源中一个属性专门来设置该资源属于哪个sa管理
```shell
kubectl explain pod.spec.serviceaccountname 
```

验证sa
```shell
#方法1:在集群节点上执行
kubectl --insecure-skip-tls-verify  --token=$token -s
https://kubeapi.wang.org:6443 get pod
#方法2:在集群节点上执行
curl -s -h "authorization: bearer $token"  --cacert /etc/kubernetes/pki/ca.crt 
https://api_server:6443/api/v1/namespaces/default/pods/
#方法3:在pod内执行下面命令
curl --cacert /etc/kubernetes/pki/ca.crt -h "authorization: bearer ${token}"
https://kubernetes.default/api/v1/pod/namespaces/{namespace}
```

对应sa创建对应的token
```yaml
# 清单文件
# cat yaml/security-sa-admin.yaml
apiversion: v1
kind: serviceaccount
metadata:
  name: admin
---
# v1.24版之后添加下面内容手动创建secret
apiversion: v1
kind: secret
type: kubernetes.io/service-account-token
metadata:
  name: admin-secret
  annotations:
    kubernetes.io/service-account.name: "admin"
---
apiversion: v1
kind: pod
metadata:
  name: pod-sa-admin
spec:
  containers:
  - name: pod-sa-admin
    image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
    imagepullpolicy: ifnotpresent
  serviceaccountname: admin #使用sa
```

为sa账号创建kubeconfig
```yaml
# 创建sa并获取token
apiversion: v1
kind: serviceaccount
metadata:
  name: admin
---
# v1.24版本之后添加下面内容手动创建secret
apiversion: v1
kind: secret
type: kubernetes.io/service-account-token
metadata:
  name: admin-secret
  annotations:
    kubernetes.io/service-account.name: "admin`"
```
```shell
kubectl apply -f yaml/security-sa-admin.yaml

# 获取sa账号的token
# 方法1
kubeadmin_token=$(kubectl get secret admin-secret -n default -o jsonpath='{.data.token}' | base64 -d) 
# 方法2:
kubectl describe secrets admin-service | awk '/^token/(pring $12)'

# 设置用户信息
kubectl config set-credentials kubeadmin --toke=$kubeadmin_token --kubeconfig=/root/kubeadmin.conf

# 设置集群信息
kubectl config set-cluster kubernetes --certificate-authority=/etc/kubernetes/pki/ca.crt --serve="https://kubeapi.feng.ory:6443" --embed-certs=true --kubeconfig=/root/kubeadmin.conf

# 设置上下文信息context
kubectl config set-context kubeadmin@kubernetes --cluster=kubernetes --user=kubeadmin --kubeconfig=/root/kubeadmin.conf

# 指定默认context
kubectl config use-context kubeadmin@kubernetes --kubeconfig=/root/kubeadmin.conf

# 验证kubeconfig,权限不足
kubectl get pod --kubeconfig=/root/kubeadmin.conf`
```

### 授权机制-rbac机制
#### rbac基础概念
- 实体(entity): 在rbac也称为subject，通常指的是user、group或者serviceaccount，即对哪些人进行授权
- 资源(resource): 在rbac中也称为object，指代subject期望操作的目标，例如secret、pod及service对象等
  - 仅限于/api/v1 或 /apis/group/version/开始的路径
  - 其他路径对应的端点均被视为“非资源类请求”，例如/healthz端点
- 动作(action):
  - object
    - 读操作：get,list,watch
    - 写操作：create, update, patch, delete, deletecollection等
- 规则(rules): resource + action
- 角色：规则的集合
  - role: 名称空间级别
  - clusterrole: 集群级别
- 角色绑定（role binding）
  - rolebinding
  - clusterrolebinding

#### 查看默认role和clusterrole
```shell
kubectl get role -a
kubectl get clusterrole
```

查看超级管理员cluster-admin格式
```yaml
#  kubectl get clusterrole cluster-admin -o yaml
apiversion: rbac.authorization.k8s.io/v1
kind: clusterrole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  creationtimestamp: "2024-07-16t18:17:02z"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: cluster-admin
  resourceversion: "78"
  uid: b35abec6-afb3-4e69-83b7-f04b291ec626
rules:   # 规则
- apigroups:  # 分组
  - '*'
  resources:   # 分组下的资源
  - '*'
  verbs:      # 动作：读(get,list,watch), 写（create,delete,update,patch...）
  - '*'
- nonresourceurls:
  - '*'
  verbs:
  - '*'
```

#### clusterrole和clusterrolebinding组合实现
```shell
kubectl create clusterrolebinding name --clusterrole=name [--user=username] [--group=groupname] [--serviceaccount=namespace:serviceaccountname]

# 示例，view系统自带clusterrole
kubectl create clusterrolebinding admin-default-view --clusterrole=view --serviceaccount=default:admin
```

#### clusterrolebinding清单格式
```yaml
apiversion: rbac.authorization.k8s.io/v1
kind: clusterrolebinding
metadata:
  name: feng-edit
roleref: # 关联的规则
  apigroup: rbac.authorization.k8s.io
  kind: clusterrole
  name: edit
subjects: # 关联的对象
- apigroup: rbac.authorization.k8s.io
  kind: user
  name: feng
```

#### role和rolebinding组合实现
```shell
kubectl create rolebinding name --clusterrole=name|--role=name [--user=usernmae] [--group=gruopname] [--serviceaccount=namespace:serviceaccountname]
```
#### role和clusterrole的命令行操作方法
```shell
# role
kubectl create role name --verb=verb --resource=resource.group/subresource [--resource-name=resourcename]
[--dry-run=server|client|none] [options]

# cluserrole
kubectl create clusterrole name --verb=verb --resource=resource.group [--resource-name=resourcename]
[--dry-run=server|client|none] [options]`
```


## dashboard
### 官方dashboard
```shell
wget https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml
```

### kuborad



## kubernetes有状态服务管理

### statefulset工作机制
#### statefulset特定
- 每个pod都有稳定、唯一的网络访问标识
- 每个pod彼此间的通信基于headless service实现
- statefulset控制的pod副本启动、扩展、删除、更新等操作都是有顺序的
- statefulset里的每个pod存储的数据不同，所以采用专用的稳定独立的持久化存储卷，用于存储pod的状态数据

#### statefulset对用pod的网络标识
- 每个statefulset对象对应于一个专用的headless service对象
- 使用headless service给每一个statefulset控制的pod提供一个唯一的dns域名来作为每个成员的网络标识
- 每个pod都有一个从0开始，从小到大的序号的名称，创建和扩容时序号从小到大，删除，缩容和更新镜像时，从大到小
- 通过clusterdns解析为pod的地址，从而实现集群内部成员之间使用域名通信
```shell
$(statefulset_name)-$(orederid).$(headless_service_name).$(namespace_name).svc.cluster.local

# 示例
mysql-0.mysql.wordpress.svc.cluster.local
mysql-1.mysql.wordpress.svc.cluster.local
mysql-2.mysql.wordpress.svc.cluster.local
```

#### statefulset的pod管理策略pod management policy
定义创建，删除及扩缩容等管理操作期间，在pod副本上的创建两种模式
- `orderedready`
  - 创建或扩容时，顺次完成各pod副本的创建，且要求只有前一个pod转为ready状态后，才能进行后一个pod副本的创建
  - 删除或缩容时，逆序，依次完成相关pod副本的终止
- `parallel`
  - 各pod副本的创建或删除操作不存在顺序方面的要求，可同时进行

#### statefulset的存储方式
- 基于podtemplate定义pod模版
- 在podtemplate上使用volumetemplate为各pod副本动态置备persistentvolume
- 因为每个pod存储的状态数据不尽相同，所以在创建每一个pod副本时绑定至专有的固定的pvc
- pvc的名称遵循特定的格式，从而能够与statefulset控制器对象的pod副本建立紧密的关联关系
- 支持从静态置备或动态置备的pv中完成绑定
- 删除pod(例如缩容)，并不会一并删除相关的pvc

#### statefulset组件
- headless service
  - 一般的pod名称是随机的，而为了statefulset的唯一性，所以借用headless service通过唯一的“网络标识”来直接指定的pod应用，所以它要求我们的dns环境完好
  - 当一个statefulset挂掉，新创建的statefulset会被赋予跟原来的pod一样的名字，通过这个名字来匹配到原来的存储，实现了状态的保存

- volumeclaimtemplate
  - 有状态中的副本数据是不一样的，如果用共享存储的话，会导致多副本间 的数据被覆盖，为了statefulset数据持久化，需要将pod和其申请的数据卷隔离开，每一种pod都有其独立的对应的数据卷配置模版，来满足该要求


### statefulset配置
- 注意：statefulset除了需要定义自身的标签选择器和pod模版等属性字段，statefulset必须要配置一个专用的headless service，而且还可能要根据需要，编写代码完成扩容，缩容等功能所依赖的操作
```yaml
# 格式
apiversion: apps/v1
kind: statefulset
metadata:
  name <string>                         # 资源名称，在作用域中要唯一
  namespace <string>                    # 名称空间：statefulset隶属名称空间级别
spec:
  replicas: <integer>                   # 期望的pod副本数，默认为1
  selector: <object>                    # 标签选择器，须匹配pod模版中的标签
  template: <object>                    # pod模版对象，必选字段
  revisioinhistorylimit: <integer>      # 滚动更新历史记录数量，默认为10
  updatestrategy: <object>              # 滚动更新策略
    type: <string>                      # ondelete和rollingupdate
    rollingupdate: <object>             # 滚动更新参数，只有在手动删除旧pod后才会触发更新
      maxunavailable: <integer>         # 更新期间可比期望的pod数量缺少的数量或比例
      partition: <integer>              # 分区值，表示只更新大于等于此索引值的pod，默认为0，一般用于金丝雀场景，更新和缩容都是索引号的pod从大到小进行
  servicename: <string>                 # 相关的headless service的名称，必选字段
    apiversion: <string>
    kind: <string>                      # pvc资源类型表示，可省略
    metadata: <object>                  # 卷申请模版元数据
    spec: <object>
  podmanagementpolicy <string>          # pod管理策略，默认orderedready表示顺序创建并逆序删除，“parallel”表示并行模式
  volumeclaimtemplates: <[]object>      # 指定pvc的模版，存储卷申请模版，实现数据持久化
  - metadata:
      name: <string>                    # 生成的pvc名称格式为<volumeclaimtemplates>.<statefulset>-<orderid>
    spec:
      accessmodes: ["readwriteonce"]
      storageclassname: "sc-nfs"        # 如果有动态置备的storageclass，可以指定名称
      resources:
        requests:
          storage: 1gi
```

范例：简单statefulset
```yaml
# cat statefulset-demo.yaml
apiversion: v1
kind: service
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: http
  clusterip: none
  selector:
    app: nginx
---
apiversion: apps/v1
kind: statefulset
metadata:
  name: web
spec:
  servicename: "nginx"
  replicas: 2
  selector:
    matchlabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/pod-test:v0.1
        ports:
        - containerport: 80
          name: http
```

#### statefulset扩缩容
```shell
kubectl scale sts <sts_name> --replicas <num>

# 示例
kubectl scale sts web --replicas 5
```

#### statefulset简单案例
- 准备nfs服务
  - 建议直接搭建nfs动态置备
- service资源
```yaml
# 准备headless服务
apiversion: v1
kind: service
metadata:
  name: statefulset-headless
spec:
  ports:
  - port: 80
  clusterip: none
  selector:
    app: myapp-pod
```

- 创建statefulset资源
```yaml
apiversion: apps/v1
kind: statefulset
metadata:
  name: myapp
spec:
  servicename: statefulset-headless
  replicas: 3
  selector:
    matchlabels:
      app: myapp-pod
  template:
    metadata:
      labels:
        app: myapp-pod
    spec:
      containers:
      - name: myapp
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/nginx:1.20.0
        volumemounts:
        - name: myappdata
          mountpath: /usr/share/nginx/html
  volumeclaimtemplates:
  - metadata:
      name: myappdata
    spec:
      accessmodes: [ "readwriteonce" ]
      storageclassname: "sc-nfs"
      resources:
        requests:
          storage: 1gi
```

#### 案例：mysql主从复制集群
- 准备nfs服务（推荐动态置备）
- 创建configmap
```yaml
# cat statefulset-mysql-configmap.yaml
apiversion: v1
kind: configmap
metadata:
  name: mysql
  labels:
    app: mysql
    app.kubernetes.io/name: mysql
data:
  primary.cnf: |
    [mysqld]
    log-bin    
  replica.cnf: |
    [mysqld]
    super-read-only  
```

- 创建service
```yaml
# cat statefulset-mysql-svc.yaml
# 为statefulset成员提供稳定的dns表项的无头服务(headless service)
# 主节点的对应的service
apiversion: v1
kind: service
metadata:
  name: mysql
  labels:
    app: mysql
    app.kubernetes.io/name: mysql
spec:
  ports:
  - name: mysql
    port: 3306
  clusterip: none
  selector:
    app: mysql
---
# 用于连接到任一mysql实例执行读操作的客户端服务
# 对于写操作，必须连接到主服务器：mysql-0.mysql
# 从节点的对应的service，注意：此处无需无头服务
# 下面的service可以不创建，直接使用无头服务mysql也可以
apiversion: v1
kind: service
metadata:
  name: mysql-read
  labels:
    app: mysql
    app.kubernetes.io/name: mysql
spec:
  ports:
  - name: mysql
    port: 3306
  selector:
    app: mysql
```
- 创建statefulset
```yaml
# cat statefulset-mysql-statefulset.yaml
apiversion: apps/v1
kind: statefulset
metadata:
  name: mysql
spec:
  selector:
    matchlabels:
      app: mysql
      app.kubernetes.io/name: mysql
  servicename: mysql
  replicas: 3
  template:
    metadata:
      labels:
        app: mysql
        app.kubernetes.io/name: mysql
    spec:
      initcontainers:
      - name: init-mysql
        #image: mysql:5.7
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:5.7
        command:
        - bash
        - "-c"
        - |
          set -ex
          # 基于 pod 序号生成 mysql 服务器的 id。
          [[ $hostname =~ -([0-9]+)$ ]] || exit 1
          ordinal=${bash_rematch[1]}
          echo [mysqld] > /mnt/conf.d/server-id.cnf
          # 添加偏移量以避免使用 server-id=0 这一保留值。
          echo server-id=$((100 + $ordinal)) >> /mnt/conf.d/server-id.cnf
          # 将合适的 conf.d 文件从 config-map 复制到 emptydir。
          if [[ $ordinal -eq 0 ]]; then
            cp /mnt/config-map/primary.cnf /mnt/conf.d/
          else
            cp /mnt/config-map/replica.cnf /mnt/conf.d/
           fi          
        volumemounts:
        - name: conf
          mountpath: /mnt/conf.d
        - name: config-map
          mountpath: /mnt/config-map
      - name: clone-mysql
        #image: gcr.io/google-samples/xtrabackup:1.0
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/xtrabackup:1.0
        command:
        - bash
        - "-c"
        - |
          set -ex
          # 如果已有数据，则跳过克隆。
          [[ -d /var/lib/mysql/mysql ]] && exit 0
          # 跳过主实例（序号索引 0）的克隆。
          [[ `hostname` =~ -([0-9]+)$ ]] || exit 1
          ordinal=${bash_rematch[1]}
          [[ $ordinal -eq 0 ]] && exit 0
          # 从原来的对等节点克隆数据。
          ncat --recv-only mysql-$(($ordinal-1)).mysql 3307 | xbstream -x -c /var/lib/mysql
          # 准备备份。
          xtrabackup --prepare --target-dir=/var/lib/mysql          
        volumemounts:
        - name: data
          mountpath: /var/lib/mysql
          subpath: mysql
        - name: conf
          mountpath: /etc/mysql/conf.d
      containers:
      - name: mysql
        #image: mysql:5.7
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:5.7        
        env:
        - name: mysql_allow_empty_password
          value: "1"
        ports:
        - name: mysql
          containerport: 3306
        volumemounts:
        - name: data
          mountpath: /var/lib/mysql
          subpath: mysql
        - name: conf
          mountpath: /etc/mysql/conf.d
        resources:
          requests:
            cpu: 500m
            memory: 1gi
        livenessprobe:
          exec:
            command: ["mysqladmin", "ping"]
          initialdelayseconds: 30
          periodseconds: 10
          timeoutseconds: 5
        readinessprobe:
          exec:
            # 检查我们是否可以通过 tcp 执行查询（skip-networking 是关闭的）。
            command: ["mysql", "-h", "127.0.0.1", "-e", "select 1"]
          initialdelayseconds: 5
          periodseconds: 2
          timeoutseconds: 1
      - name: xtrabackup
        #image: gcr.io/google-samples/xtrabackup:1.0
        image: registry.cn-beijing.aliyuncs.com/wangxiaochun/xtrabackup:1.0
        ports:
        - name: xtrabackup
          containerport: 3307
        command:
        - bash
        - "-c"
        - |
          set -ex
          cd /var/lib/mysql
          # 确定克隆数据的 binlog 位置（如果有的话）。
          if [[ -f xtrabackup_slave_info && "x$(<xtrabackup_slave_info)" != "x" ]]; then
            # xtrabackup 已经生成了部分的 “change master to” 查询
            # 因为从一个现有副本进行克隆。(需要删除末尾的分号!)
            cat xtrabackup_slave_info | sed -e 's/;$//g' > change_master_to.sql.in
            # 在这里要忽略 xtrabackup_binlog_info （它是没用的）。
            rm -f xtrabackup_slave_info xtrabackup_binlog_info
          elif [[ -f xtrabackup_binlog_info ]]; then
            # 直接从主实例进行克隆。解析 binlog 位置。
            [[ `cat xtrabackup_binlog_info` =~ ^(.*?)[[:space:]]+(.*?)$ ]] || exit 1
            rm -f xtrabackup_binlog_info xtrabackup_slave_info
            echo "change master to master_log_file='${bash_rematch[1]}',\
                  master_log_pos=${bash_rematch[2]}" > change_master_to.sql.in
          fi
          # 检查是否需要通过启动复制来完成克隆。
          if [[ -f change_master_to.sql.in ]]; then
            echo "waiting for mysqld to be ready (accepting connections)"
            until mysql -h 127.0.0.1 -e "select 1"; do sleep 1; done
            echo "initializing replication from clone position"
            mysql -h 127.0.0.1 \
                  -e "$(<change_master_to.sql.in), \
                          master_host='mysql-0.mysql', \
                          master_user='root', \
                          master_password='', \
                          master_connect_retry=10; \
                        start slave;" || exit 1
            # 如果容器重新启动，最多尝试一次。
            mv change_master_to.sql.in change_master_to.sql.orig
          fi
          # 当对等点请求时，启动服务器发送备份。
          exec ncat --listen --keep-open --send-only --max-conns=1 3307 -c \
            "xtrabackup --backup --slave-info --stream=xbstream --host=127.0.0.1 --user=root"          
        volumemounts:
        - name: data
          mountpath: /var/lib/mysql
          subpath: mysql
        - name: conf
          mountpath: /etc/mysql/conf.d
        resources:
          requests:
            cpu: 100m
            memory: 100mi
      volumes:
      - name: conf
        emptydir: {}
      - name: config-map
        configmap:
          name: mysql
  volumeclaimtemplates:
  - metadata:
      name: data
    spec:
      accessmodes: ["readwriteonce"]
      storageclassname: "sc-nfs"  #如果使用storageclass,启用此行
      resources:
        requests:
          storage: 10gi
```

测试
```shell
# 部署一个测试节点
kubectl run client-test-$random --image registry.cn-beijing.aliyuncs.com/wangxiaochun/ubuntu:22.04 --restart=never --rm -it --command -- /bin/bash
```

## crd定制资源
扩展kubernetes api常用方法
- 二次开发api server源码，适合在添加新的核心类型时采用
- 开发自定义api server并聚合至主api server，富于弹性但代码工作量大
- 使用crd（custom resource definition）自定义资源类型，易用但限制较多，对应的控制器还需自行开发

### crd资源清单实现
```yaml
# cat crd-user.yaml
apiversion: apiextensions.k8s.io/v1
kind: customreasourcedefinition
metadata:
  name: users.auth.democrd.io
spec:
  group: auth.democrd.io            #定义该资源属于哪个组
  names:
    kind: user
    plural: users  # 复数
    singular: user # 单数
    shortnames:    # 缩写
    - u
  scope: namespaced    # 表明该资源是名称空间级的资源
  version:
  - served: true
    storage: true
    name: vlalpha1
    schema:
      openapiv3schema:
        type: object
        properties:
          spec:
            type:
            properties:
              userid:
                type: integer
                minimum: 1
                maximum: 65535
              groups:
                type: array
                items:
                  type: string
              email:
                type: string
              password:
                type: string
                format: password
            required: ["userid","groups"]
```

## operator
### operator应用网站
```shell
https://operatorhub.io
```

### operator安装部署流程
```shell
# 安装operator
# 创建(一些)crd
kubectl create -f 
https://download.elastic.co/downloads/eck/2.12.1/crds.yaml`

# 查看创建的相关crd
kubectl get crd --sort-by='{.metadata.creationtimestamp}'|tail

# 安装operator相关rbac规则
kubectl apply -f 
https://download.elastic.co/downloads/eck/2.12.1/operator.yaml

# 在elastic-system，名称空间查看相关资源
kubectl get all -n elastic-system
```

### 部署elasticsearch
```shell
# 准备业务的名称空间
kubectl create ns demo

# 准备elasticsearch-cluster清单文件
apiversion: elasticsearch.k8s.elastic.co/v1
kind: elasticsearch
metadata:
 name: my-es-cluster
  #namespace: elastic-system
 namespace: demo
spec:
  #version: 8.13.2
 version: 8.14.0
 nodesets:
  - name: default
   count: 3                  #3个节点的集群
   config:
      node.store.allow_mmap: false
   volumeclaimtemplates:
    - metadata:
       name: elasticsearch-data
     spec:
       accessmodes: ["readwriteonce"] 
       resources:
         requests:
           storage: 2gi
       storageclassname: sc-nfs     #需要提前准备sc-nfs的storageclass
# 注意：节点内存需要4g以
```

- 执行清单文件
```shell
kubectl apply -f operator-elasticsearch-cluster.yaml
```

## kubernetes包管理器helm
### helm相关概念
- helm: helm的客户端工具，负责和api server通信
  - 和kubectl类似，也是kubernetes api server的命令行客户端工具
  - 支持kubeconfig认证文件

- chart：打包文件，将所有相关的资源清单文件yaml的打包文件

- release: 表示基于chart部署的一个实例。通过chart部署的应用都会生成一个唯一的release

- repository：chart包存放的仓库，相当于apt和yum仓库

### helm3和helm2的变化
- tiller服务器被废弃，仅保留helm客户端，helm通过kubeconfig认证到api server
- release可以在不同名称空间重用
- 支持将chart推送到docker镜像仓库
- helm3默认使用secret来存储发行信息，提供了更高的安全性
  - helm2默认使用configmaps存储发行信息
- 不再需要requirements.yaml,依赖关系式直接在chart.yaml中定义

### chart仓库
用于实现chart包的集中存储和分发，类似于docker仓库harbor

chart仓库
- 官方仓库：`https://artifacthub.io`
- 微软仓库：推荐使用，`http://mirror.azure.cn/kubernetes/charts/`
- 阿里云仓库：`http://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts`
- harbor仓库：新版支持基于oci://协议， 将chart存放在公共的docker镜像仓库

### helm部署应用流程
- 安装helm工具
- 查找合适的chart仓库
- 配置chart仓库
- 定位chart
- 通过向chart中模版文件中字符串赋值完成其实例化，即模版渲染，实例化的结果可以部署到目标kubernetes上（模版字符串的定制方式三种）
  - 默认使用chart中的value.yaml中定义的默认值
  - 直接在helm install的命令行，通过--set选项进行
  - 自定义values.yaml，由helm install -f values.yaml命令加载文件

### helm二进制安装
```shell
#在kubernetes的管理节点部署
[root@master1 ~]#wget https://get.helm.sh/helm-v3.12.0-linux-amd64.tar.gz
[root@master1 ~]#tar xf helm-v3.12.0-linux-amd64.tar.gz -c /usr/local/
[root@master1 ~]#ls /usr/local/linux-amd64/
helm license readme.md
[root@master1 ~]#ln -s /usr/local/linux-amd64/helm /usr/local/bin/
```

```shell
# 查看helm版本
helm version
```

### helm命令用
```shell
# 仓库管理
helm repo list    #列出已添加的仓库
helm repo add [repo_name] [url]   # 添加远程仓库并命名，如下所示
# 添加仓库示例
helm repo add bitnami https://charts.bitnami.com/bitnami
# 添加harbor仓库
helm repo add myharbor https://harbor.wangxiaochun.com/charrepo/myweb --username admin --password 123456

# 删除仓库
helm repo remove [repo1 [repo2...]]

# 更新仓库
helm repo update   相当于apt update

# 从artifacthub网站搜索，无需配置本地仓库，相当于docker search
helm search hub [keyword]

# 从本地仓库搜索，需要配置本地仓库才能搜索，相当于apt search
helm search repo [keyword]

# 查看chart信息
helm show chart [chart]

# 拉取chart到本地
helm pull repo/chartname   # 下载charts到当前目录，表现为tgz文件，默认最新版本

# 新版路径支持oci
helm pull oci://

# 下载指定版本的chart包并解压
helm pull myrepo/myapp --version 1.2.3 --untar

# 安装
helm install [name] [chart] [--version <string>] # 安装指定版本的chart
helm install [chart] --generate-name             # 自动生成 release_name
helm install --set key1=value1 --set key2=value2 release_name chart... #指定属性实现定制配置
helm install -f value.yaml release_name chart...   # 引用文件实现定制配置
helm install --debug --dry-run release_name chart   # 调试并不执行，可以查看到执行的渲染结果

# 删除
helm uninstall release_name    # 卸载release

# 查看release
helm list     # 列出安装的release
helm status release_name       # 查看release状态
helm get values release_name -n namespace > values.yaml

# 查看release的生成的资源清单文件
helm get manifest release_name -n namespace

# 升级和回滚
helm upgrade release_name chart --set key=newvalue
helm upgrade release_name chart -f mychart/values.yaml

# release回滚到指定版本，如果不指定版本，默认回滚至上一个版本
helm rollback release_name [revision]

# 查看历史
helm history release_name

# 打包
helm package mychart/  # 将指定目录的chart打包为.tgz到当前目录下
```

helm install说明
```shell
#安装的chart有六种形式
1. by chart reference: helm install mymaria example/mariadb  #在线安装,先通过helm 
repo add添加仓库，才能在线安装
2. by path to a packaged chart: helm install myweb ./nginx-1.2.3.tgz  #离线安装
3. by path to an unpacked chart directory: helm install myweb ./nginx #离线安装
4. by absolute url: helm install myweb https://example.com/charts/nginx-1.2.3.tgz #在线安装
5. by chart reference and repo url: helm install --repo https://example.com/charts/ myweb nginx #在线安装
6. by oci registries: helm install myweb --version 1.2.3 oci://example.com/charts/nginx #在线安装。
```

### 案例：部署mysql(单机版)
- 查看chart包的参数变量
```shell
helm show values bitnami/mysql --version 11.1.14 > values.yaml

# 去掉注释
grep -v "#" values.yaml 

# 安装时必须指定存储卷，否则会处于pending状态
helm install mysql bitnami/mysql --version 11.1.14 --set primary.persistence.storageclass=sc-nfs
```

### 案例：部署mysql主从复制
```shell
helm install mysql \
    --set auth.rootpassword='p@ssw0rd' \
    --set global.storageclass=sc-nfs \
    --set auth.database=wordpress \
    --set auth.username=wordpress \
    --set auth.password='p@ssw0rd' \
    --set architecture=replication \
    --set secondary.replicacount=1 \
    --set auth.replicationpassword='p@ssw0rd' \
   bitnami/mysql \
    -n wordpress --create-namespace
```

### 案例：部署wordpress
```shell
helm install wordpress \
    --version 21.0.10 \
    --set mariadb.enabled=false \
    --set externaldatabase.host=mysql-primary.wordpress.svc.cluster.local \
    --set externaldatabase.user=wordpress \
    --set externaldatabase.password='p@ssw0rd' \
    --set externaldatabase.database=wordpress \
    --set externaldatabase.port=3306 \
    --set wordpressusername=admin \
    --set wordpresspassword='p@ssw0rd' \
    --set persistence.storageclass=sc-nfs \
    --set ingress.enabled=true \
    --set ingress.ingressclassname=nginx \
    --set ingress.hostname=wordpress.wang.org \
    --set ingress.pathtype=prefix \
    --set wordpressusername=admin \
    --set wordpresspassword='p@ssw0rd' \
    ./wordpress-21.0.10.tgz \
    -n wordpress --create-namespace
```

### 自定义chart
#### helm chart
```shell
mychart/
  chart.yaml
  values.yaml
  charts/
  templates/
  ...
```

- `chart.yaml`文件
  - 必选项
  - 包含了该chart的描述，你可以从模版中访问它
  - `helm show chart [chart]`查看到即此文件内容

- `templates/`目录
  - 必选项
  - 包括了各种资源清单的模版文件。比如：`deployment,service,ingress,configmap`
  - 可以是固定内容的文本，也可以包含了一些变量，函数等模版语法
  - 当helm评估chart时，会通过模版渲染引擎将所有文件发送到`templates/`目录中。然后收集模版的结果并发送给kubernetes。

- `values.yaml`文件
  - 可选项
  - 如果`templates/`目录下文件都是固定格式，此文件无需创建
  - 如果`templates`目录中包含变量时，可以通过此文件提供变量的默认值
  - 这些值可以在用户执行`helm install`或`helm upgrade`时被覆盖
  - `helm show values [chart]`查看到即此文件内容
  
- `charts/`目录
  - 可选项
  - 可以包含依赖的其他的chart，称之为子chart


#### 常用内置对象
- release对象
```shell
# 描述应用发布自身的一些信息
.release.name      #release 的名称
,release.namespace #release 的命名空间
.release.revision  #获取此次修订的版本号。初次安装时为1，每次升级或回滚都会递增
.release.service   #获取渲染当前模板的服务名称。一般都是 helm
.release.isinstall #如果当前操作是安装，该值为 true
.release.isupgrade #如果当前操作是升级或回滚，该值为true
.release.time      #chart发布时间

#引用
{{ .release.name }}
```
- values对象
```shell
# 变量赋值
key1: value1
info:
 key2: value2

# 变量引用
#注意: 大写字母v
{{ .value.key1 }}
{{ .value.info.key2 }}

```
- chart对象
- capabilities对象
- template对象


## 补充
### 客户端负载均衡
这里把apiserver看作一个数据库，无论是scheduler还是controller，又或者worker节点的kebulet都可以看作是api server的客户端，它们从中监听到数据，并对其进行增删改查。
- scheduler负责监听api server上的pod状态，任何时候有pod出现，并且pod又没有与某个节点建立绑定关系，那么scheduler就负责给它调度，从众多的节点找到一个最佳适配
- 这里kebulet也监视api server,监视上面与自己相关的pod信息,scheduler把某一个pod调度到当前节点，当前节点就要从api server中把pod的配置读出来到本地，根据配置的需要创建并启动容器
- kubeproxy负责监视api server上的service上的创建，一旦有service被创建，service就会根据标签选择器挑选出pod，跟service关联的pod信息都挑选出来被填充到service的定义当中，都保存在api server上，随后kubeproxy就会发现该service，也知道该service关联到哪些pod上，kubeproxy将service的定义读出来，转换成当前节点内核当中的iptables规则


#### 以wordpress和mysql举例
wordpress访问mysql，首先要访问mysql的service地址，mysql的service记录在api server上，此时wordpress和mysql两个节点上的各自的kubeproxy，各自都通过apiserver，将service定义转换为内核中的iptables规则


### 把容器接入网络中
1. 给容器提供虚拟网络接口 (创建pod时)
2. 为pod准备好网络；由网络插件负责（在部署集群的时候，选择的子网应与网络插件的默认配置一致）
  - flannel: 10.244.0.0/16
  - calico: 192.168.0.0/16
  - cilium: 192.168.0.0/16
3. 将该容器的网络接口接口pod网络(创建pod时)
4. 为该pod的网络接口提供一个ip地址（启动pod时）

注意：pod停止，他此前使用的地址是存储在api server中，当再次重启时，很可能将pod再次使用

#### 网络插件在如何保证创建pod时，在不同节点创建的pod的网络ip不冲突
真正分配地址的程序是位于每一个节点上都有一个节点范围的地址维护程序，而不是整个集群范围的,(节点级插件ipam插件)

ipam本质上网络插件flannel或者calic等网络插件中的一个组件或者进程之一

#### ipam插件(节点级地址分配插件的统称)
- host-local
- dhcp

#### 解决节点级插件分配网络地址时，地址冲突的方法
为每一个节点，分一个子网
- 以flannel为例
  - 10.244.0.0/24
  - 10.244.1.0/24
  - 10.244.2.0/24
  - ...

- 每个节点上的可用地址是254个，全0和全1不算，通常来讲，全0代表网络地址，全1代表广播地址
- 默认情况下k8s最多运行pod数量为110个

#### calico默认子网掩码26位
calico：192.168.0.0/16 --> 做子网划分，默认使用26bit掩码，即10bit做子网划分，6位bit做地址, 因此子网数量是1024个，每个子网的可用地址是62


### 不同节点上的pod的通信方式
重点：kubernetes要求pod之间，无论是否在同一节点上，必须能够`直接通信`

#### pod网络通信的常见方式：2种
第一种：underlay（底层网络）路由模型
第二种：overlay（叠加网络）隧道模型


#### 详细解读
见云原生学习导图--> 《不同节点的pod间通信过程》

#### 网络插件可实现其中的一种或多种模型
- flannel:
  - vxlan
  - 路由模型（通过查询中央库生成路由表）
  - 混合模型
    - 自动识别，如果节点间跨路由，使用隧道模型，不跨路由使用混合模型

- calico:
  - ipip(默认ipip隧道)、vxlan
  - 路由模型(通过bgp学习生成路由表)
  - 混合模型
    - ipip + 路由模型
    - vxlan + 路由模型

- cilium
  - vxlan/geneve
  - 路由模型：（bgp协议）
    - 但是原生不支持，需要组合第三方插件提供bgp协议的功能（比如kube-router）
  - cilium底层通过ebpf完成，是在网卡驱动中完成报文的转发，路由等，因此性能更好

在云端部署k8s最好的网络插件就是云端提供商自己的网络插件

### 总结
#### kubernetes将pod网络功能通过cni委托给了外部的插件，主要解决4个问题
- 同一pod容器间的通信(container to container) --- 共享同一网络名称空间
- pod间的通信(pod to pod) --- 由插件解决
- service到pod的通信 --- 利用节点内核完成
- 集群外部与service之间的通信 

#### cni网络插件基础
- cni（容器网络接口），它是容器引擎与遵循该规范网络插件的中间层，专用于为容器配置网路子系统
- 目前的cni规范主要由netplugin(网络插件)和ipam两个插件api组成
  - 网络插件也成main插件，主要负责创建/删除网络以及向网络添加/删除容器
    - 它专注于连通容器与容器之间以及容器与宿主机之间的通信，同容器相关网路设备通常都由该类插件所创建，例如：brige、ipvlan、macvlan、loopback、ptp、veth以及vlan等虚拟设备·
  - ipam，该类插件负责创建/删除地址池以及分片/回收容器的ip地址
    - 目前，该类型插件的实现主要有host-local和dhcp两个，前一个基于预置的地址范围进行地址分配，而后一个通过dhcp协议获取地址

#### 配置容器网络接口的常用方法
不同的容器虚拟化网络解决方案中为pod的网络名称空间创建虚拟接口设备的方式也会有所不同，目前，较为主流的实现方式有虚拟以太网设备（veth）、多路复用及硬件交换三种
- veth设备：
  - 创建一个网桥，并为每个容器创建一对虚拟以太网接口（veth），一个接入容器内部，另一个留置于根名称空间内添加为linux内核桥接功能或openvswitch（ovs）网桥的从设备
  - 节点的内核上有一个模块，就叫veth模块，它允许针对该模块创建一对虚拟以太网网卡
  - flannel使用的方法
- 多路复用：
  - 多路复用可以由一个中间网络设备组成，它暴露多个虚拟接口，使用数据包转发规则来控制每个数据包转到的目标接口
  - calico使用功能的方法
  - 将底层物理网卡借助于软件，虚拟出多块网卡，每一块网卡给一个pod使用，因此每个pod就好像直接使用这块网卡，只不过这块网卡被分成了n份，每个人只得到其中一份，这样一来，容器内部的进程生成的报文，要封装驱动的时候是直接送给物理网卡出去的，要想实现这个功能，需要隔离内部的多个pod，目前的话通常是把他们放到vlan中，所以这个vlan要么是在ip层实现，要么是在mac层实现，在mac层实现意味着每一个网卡每个pod内的网卡都有独立的mac地址，而且和物理网卡的mac地址不同，这样的就会出一个问题，就是数据发给物理网卡的时候，mac地址都是物理网卡的地址，而不是pod1,pod2等虚拟mac地址的地址，因此无法通过mac地址和他们通信，解决这个问题的方法就是使用网卡的混杂模式，使其物理网卡可以接受不是自己mac地址的数据包，又因为什么mac地址的包都接受，所以非常容易引发arp地址欺骗攻击，因此macvlan不建议使用，而使用ipvlan，所有pod持有的虚拟网卡，mac地址共享物理网卡的mac，但各自的ip地址是不一样的，但是无论是ipvlan还是macvlan，前提都是内核支持这些模块，由于ubuntu内核版本较新，因此容器时代，大家更愿意使用ubuntu，而不是内核比较老的centos，因此容器技术时代，红帽沦落到卖身了，卖给了ibm
- 硬件交换
  - 现今市面上有相当数量的nic都支持单根i/o虚拟化（sr-iov）（single root-iovirtual单根虚拟化），他是创建虚拟设备的一种实现方式，每个虚拟设备自身表现为一个独立的pci设备，并有着自己的vlan及硬件强制关联的qos；sr-iov提供了接近硬件级别的性能




### 主流网络插件
网络插件要实现两大核心功能：
1. 网络插件(pod间通信)
2. 支撑k8s中的著名的api：network policy，本质上就是定义iptables规则，从而实现哪些pod和哪些pod能通信，哪些和哪些不能通信
3. 链路加密

#### 对比 
flannel不支持网路策略，calico和cilium都支持



### flannel网路插件
#### flannel支持的后端
- flanneld
  - flannel在每个主机上运行一个名为flanneld的二进制代理程序
  - 该程序负责从预留的网络中按照指定或默认的掩码长度来为当前节点申请分配一个子网，并将网络配置、已分配的子网或辅助数据存储于kubernetesapi或etcd之中

- flannel使用称为后端(backend)的容器网络机制转发跨节点的pod报文，它目前支持的主流backend如下
  - vxlan
    - 使用linux内核中的vxlan模块封装隧道报文，以叠加网络模型支持跨节点的pod间互联互通
    - 额外支持直接路由(direct routing)模式，该模式下位于同二层网络内的节点之上的pod间通信可通过路由模式直接发送，而跨网络的节点之上的pod间通信仍要使用vxlan隧道转发
    - vxlan后端模式中，flannel监听于8472/udp发送封装的数据包
  - host-gw
    - 类似于vxlan中的直接路由模式，但不支持跨网络的节点，因此这种方式强制要求各节点本身必须在同一个二层网络中，不太适用于较大的网络规模
    - 有着较好的转发性能，且易于设定，推荐对报文转发性能要求较高的场景使用
  - udp
    - 使用常规udp报文封装完成隧道转发，性能较前两种方式低很多，它仅应该用在不支持前两种后端的环境中使用
    - udp后端模式中，flannel监听于8286、udp转发封装的报文
```shell
# kuberadm init指令
k8s_release_version=1.30.2 && 
kubeadm init --control-plane-endpoint kubeapi.feng.org --kubernetes-version=v${k8s_release_version} 
--pod-network-cidr 10.244.0.0/16   # 此处指定pod间通信的网段，和后续网络插件要保持一致
--service-cidr 10.96.0.0/12 
--image-repository registry.aliyuncs.com/google_containers 
--token-ttl=0 # 生成工作节点接入集群所需的token，该值是token的过期时间(默认24h)
--upload-certs  # 将第一个主节点上生成的ca的相关信息，做成一个secrets放到kube-system名称空间下，其他主节点加入该集群后，将ca相关信息同步过去
--cri-socket=unix:///run/cri-dockerd.sock

# --upload-certs示例
[root@master1 ~]#kubectl get secrets -n kube-system
name                     type                            data   age
bootstrap-token-4oei1o   bootstrap.kubernetes.io/token   6      17h
```
```shell
vim kube-flannel.yaml   # 加载flannel的资源清单文件
...
data:
...
net-conf.json: |
{
    "network": "10.244.0.0/16",
    "enablenftables": false, # 是否使用nstables，false表示使用iptables
    "backend": {
        "type": "vxlan"   #这个插件工作于哪个模型   #这个插件工作于哪个模型   #这个插件工作于哪个模型   #这个插件工作于哪个模型
        # 每个节点都会创建一个名为flannel.1的接口，即为隧道报文出入口，根据图例，报文通过隧道出入口进行封装和解封装
    }
}
```
部署完后
```shell
kubectl apply -f kube-flannel.yaml

# 在每个节点的目录下会生成一个配置文件
ls /etc/cni/net.d/
> 10-flannel.conflit  # 会有一个配置文件，用于配置flannel插件的程序的配置文件，而不是整个插件配置的时候基于哪个模型的配置文件

ls /opt/cni/bin/
> 二进制程序插件放在这里
```

#### 验证该网路插件基于隧道模型建立跨节点间的pod间通信
```shell
route -n
[root@master1 ~]#route -n
内核 ip 路由表
目标            网关            子网掩码        标志  跃点   引用  使用 接口
0.0.0.0         10.0.0.2        0.0.0.0         ug    0      0        0 eth0
10.0.0.0        0.0.0.0         255.255.255.0   u     0      0        0 eth0
10.244.0.0      0.0.0.0         255.255.255.0   u     0      0        0 cni0
10.244.1.0      10.244.1.0      255.255.255.0   ug    0      0        0 flannel.1  # flannel是隧道出入口,报文只有经由隧道出入口，才会进行报文的封装与解封装
10.244.2.0      10.244.2.0      255.255.255.0   ug    0      0        0 flannel.1
10.244.3.0      10.244.3.0      255.255.255.0   ug    0      0        0 flannel.1
172.17.0.0      0.0.0.0         255.255.0.0     u     0      0        0 docker0

4: flannel.1: <broadcast,multicast,up,lower_up> mtu 1450 qdisc noqueue state unknown group default 
# 该接口的mtu为1450， 因为隧道模式前面要封装udp首部和ip首部和mac地址首部
    link/ether ca:12:49:6e:3b:b2 brd ff:ff:ff:ff:ff:ff
    inet 10.244.0.0/32 scope global flannel.1
       valid_lft forever preferred_lft forever
    inet6 fe80::c812:49ff:fe6e:3bb2/64 scope link 
       valid_lft forever preferred_lft forever

# 在每个节点上
# 10.244.1.0被flannel.1拿走了
# 10.244.1.1被cni0拿走了
```
- 创建一个3副本的deployment
```shell
kubectl create deployment demoapp --image=ikubernetes/demoapp:v2.1 --replicas=3

# 在worker节点上
[root@worker1 etc]#ip a
1: lo: <loopback,up,lower_up> mtu 65536 qdisc noqueue state unknown group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <broadcast,multicast,up,lower_up> mtu 1500 qdisc fq_codel state up group default qlen 1000
    link/ether 00:50:56:21:35:5c brd ff:ff:ff:ff:ff:ff
    altname enp2s1
    altname ens33
    inet 10.0.0.122/24 brd 10.0.0.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:fe21:355c/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <no-carrier,broadcast,multicast,up> mtu 1500 qdisc noqueue state down group default 
    link/ether 02:42:0c:91:3c:bd brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
4: flannel.1: <broadcast,multicast,up,lower_up> mtu 1450 qdisc noqueue state unknown group default 
    link/ether fa:ca:d2:07:4c:b0 brd ff:ff:ff:ff:ff:ff
    inet 10.244.1.0/32 scope global flannel.1
       valid_lft forever preferred_lft forever
    inet6 fe80::f8ca:d2ff:fe07:4cb0/64 scope link 
       valid_lft forever preferred_lft forever
5: cni0: <broadcast,multicast,up,lower_up> mtu 1450 qdisc noqueue state up group default qlen 1000
    link/ether a2:0c:4a:b3:15:90 brd ff:ff:ff:ff:ff:ff
    inet 10.244.1.1/24 brd 10.244.1.255 scope global cni0
       valid_lft forever preferred_lft forever
    inet6 fe80::a00c:4aff:feb3:1590/64 scope link 
       valid_lft forever preferred_lft forever
# 会生成veth-pair
7: vethc235fb28@if2: <broadcast,multicast,up,lower_up> mtu 1450 qdisc noqueue master cni0 state up group default 
    link/ether d2:36:76:96:58:c6 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::d036:76ff:fe96:58c6/64 scope link 
       valid_lft forever preferred_lft forever

# 可以进入网络名称空间看多对端的网络
# 查看方法1
[root@worker1 etc]#nsenter -t 244156 -n ip addr
1: lo: <loopback,up,lower_up> mtu 65536 qdisc noqueue state unknown group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0@if7: <broadcast,multicast,up,lower_up> mtu 1450 qdisc noqueue state up group default 
    link/ether 9a:ac:84:08:63:5c brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.244.1.3/24 brd 10.244.1.255 scope global eth0
       valid_lft forever preferred_lft forever

# 留在宿主机一段的接口插在名为cni0的虚拟交换机（虚拟网桥）上
[root@worker1 etc]#brctl show
bridge name	bridge id		stp enabled	interfaces
cni0		8000.a20c4ab31590	no		vethc235fb28
docker0		8000.02420c913cbd	no	

# pod内的路由表的默认网关是cni0
[root@worker1 etc]#nsenter -t 244156 -n route -n
内核 ip 路由表
目标            网关            子网掩码        标志  跃点   引用  使用 接口
0.0.0.0         10.244.1.1      0.0.0.0         ug    0      0        0 eth0
10.244.0.0      10.244.1.1      255.255.0.0     ug    0      0        0 eth0
10.244.1.0      0.0.0.0         255.255.255.0   u     0      0        0 eth0
```
```shell
# 使用10.0.0.122上的pod访问10.0.0.123上的pod
# 并使用tcpdump在10.0.0.122的物理网卡接口eth0上抓包观察
# 进入pod1内，进行curl访问
kubectl exec  -it demoapp-59768b6f4f-8pzmc -- /bin/sh

curl 10.244.2.2
> demoapp by ikubernetes! app version: v2.0, client ip: 10.244.1.3, server name: demoapp-59768b6f4f-xvrw2, server ip: 10.244.2.2 ~

tcpdump -i eth0 -nn host 10.0.0.123

# 查看观察到数据包的外部封装了10.0.0.122:59662 -> 10.0.0.123:8472
# ip层上外层使用node地址封装内部的pod地址
# 同时udp报文上，使用的是8472端口
21:03:09.214331 ip 10.0.0.122.59662 > 10.0.0.123.8472: otv, flags [i] (0x08), overlay 0, instance 1
ip 10.244.1.3.48784 > 10.244.2.2.80: flags [.], ack 304, win 505, options [nop,nop,ts val 3686178909 ecr 3653720387], length 0
21:03:09.214506 ip 10.0.0.122.59662 > 10.0.0.123.8472: otv, flags [i] (0x08), overlay 0, instance 1
ip 10.244.1.3.48784 > 10.244.2.2.80: flags [f.], seq 74, ack 304, win 505, options [nop,nop,ts val 3686178909 ecr 3653720387], length 0
```

- 路由表代表了报文流入流出的位置，对分析报文走向非常重要

#### 路由模型 host-gw
```shell
net-conf.json:|
{
  "network":"10.244.0.0/16",
  "backend":{
    "type":"host-gw"
  }
}
```
- 所有配置信息放在`kube-flannel-cfg`configmap资源类型中
```shell
[root@master1 ~]#kubectl get cm -n kube-flannel
name               data   age
kube-flannel-cfg   2      22h
kube-root-ca.crt   1      22h

# 更改该configmap
kubectl get cm kube-flannel-cfg -o yaml -n kube-flannel > /tmp/kube-flannel-cfg.yaml

vim /tmp/kube-flannel-cfg.yaml

apiversion: v1
data:
  cni-conf.json: |
    {
      "name": "cbr0",
      "cniversion": "0.3.1",
      "plugins": [
        {
          "type": "flannel",
          "delegate": {
            "hairpinmode": true,
            "isdefaultgateway": true
          }
        },
        {
          "type": "portmap",
          "capabilities": {
            "portmappings": true
          }
        }
      ]
    }
  net-conf.json: |
    {
      "network": "10.244.0.0/16",
      "enablenftables": false,
      "backend": {
        "type": "host-gw"
      }
    }
kind: configmap
metadata:
  labels:
    app: flannel
    k8s-app: flannel
    tier: node
  name: kube-flannel-cfg
  namespace: kube-flannel

# 如果等他自动加载会有一个延时，或者需要手动管理
# 加载新配置
kubectl get ds -n kube-flannel

[root@master1 ~]#kubectl get ds -n kube-flannel
name              desired   current   ready   up-to-date   available   node selector   age
kube-flannel-ds   4         4         4       4            4           <none>          22h

kubectl rollout restart daemonset kube-flannel-ds -n kube-flannel

# 查看变更
[root@master1 ~]#kubectl get pods -n kube-flannel
name                    ready   status    restarts   age
kube-flannel-ds-99jlk   1/1     running   0          32s
kube-flannel-ds-srsgc   1/1     running   0          42s
kube-flannel-ds-zc6vj   1/1     running   0          27s
kube-flannel-ds-zctjq   1/1     running   0          37s

# 查看worker节点上的路由表的变化
# 可以看到隧道出入口不见了，网关指向node节点
[root@worker1 etc]#route -n
内核 ip 路由表
目标            网关            子网掩码        标志  跃点   引用  使用 接口
0.0.0.0         10.0.0.2        0.0.0.0         ug    0      0        0 eth0
10.0.0.0        0.0.0.0         255.255.255.0   u     0      0        0 eth0
10.244.0.0      10.0.0.121      255.255.255.0   ug    0      0        0 eth0
10.244.1.0      0.0.0.0         255.255.255.0   u     0      0        0 cni0
10.244.2.0      10.0.0.123      255.255.255.0   ug    0      0        0 eth0
10.244.3.0      10.0.0.124      255.255.255.0   ug    0      0        0 eth0
172.17.0.0      0.0.0.0         255.255.0.0     u     0      0        0 docker0
```

### calico网络插件
三种模式
- 隧道模式：
  - ipip（默认模式），只在报文外增加ip首部字段，不会加udp首部和帧首部
  - vxlan
- 路由模式
  - 基于bgp协议学习生成路由表(不像flannel需要查询中央数据库)
  - 限制：节点不能跨子网
- 混乱模式
  - ipip + bgp
  - vxlan + bgp

#### calico简介
- calico被称作是纯三层网络插件，为什么
  - 对比flannel，flannel使用的是虚拟网路接口是veth-pair，一段连接容器pod，另一端连接虚拟网桥cni0上，同一节点上的两个pod通信，可以直接通过网桥cni0进行通信，而网桥是二层设备，因此这里是基于二层网络的通信
  - 而calico一样使用veth-pair（虚拟以太网接口对），一端注入到pod内部，另一端驻留在节点上，不会添加到某虚拟网桥上，而是直接保留在宿主机上，因此同一节点上的两个pod通信，相当于两个pod被内核链接起来，而内核相当于路由设备，因此同节点间的pod通信需要路由，因为没有网桥了，所以要指网关，最起码要指下一跳的地址，因此必须在通信前生成路由表条目
  - 就因为哪怕是同一节点的pod要通信，也必须需要路由表进行路由，所以是纯三层网络

- calico把每个节点都当做虚拟路由器(vrouter)，把每个节点上的pod都当做是“节点路由器”后的一个终端设备并为其分配一个ip地址

- 各节点路由器通过bgp(border gateway protocol)协议学习生成路由规则，从而实现不同节点上pod间的互联互通

- calico在每一个计算节点利用linux内核实现了一个高效的vrouter（虚拟路由器）进行报文转发，而每个vrouter通过bgp协议负责把自身所属的节点上的运行的pod资源的ip地址信息基于节点的agent程序(felix)直接由vrouter生成路由规则向整个calico网络内传播


#### calico系统组件
概括来说，calico主要由felix、orchestrator、etcd、bird和bgprouterreflector等组件组成
- `felix`: calico agent，运行于每个节点，主要负责维护虚拟接口设备和路由信息
- `orchestrator plugin`：编排系统（比如k8s，openstack等）用于将calico整合进行系统中的插件，例如k8s的cni
- etcd：持久存储calico数据的存储管理系统
- bird：负责分发路由信息的bgp客户端
- bgp route reflector：bgp路由反射器，可选组件，用于较大规模的网络场景

集群中每个节点会运行一个calico-node的pod，每个pod里有两个容器
- felix
  - felix负责维持路由表(route tables)
  - 同时felix还负责根据定义的网络策略，生成iptables规则
  - 因为每个节点都有，因此应该是使用daemonset编排
- bird

calico-kube-controller: 用来支撑network-policy这样的api，这是一个控制器集，里面包含很多controller
因为calico自定义了很多crd资源类型的实现
- policy-controller
- ns-controller
- sa-controller
- pod-controller
- node-controller

calico datastore：所有的数据都存储在这里
- felix从这里读取资源定义，从而生成对应的iptables规则
- calico datastore在api-server中

typha：从api-server中把calico相关数据读出来，并缓存下来，由它向fliex提供数据，从而减轻了api-server的负载
- 通常在50个节点以上的时候使用

bgprouterreflector（路由反射器）
- 用来减少每个节点间的bgp路由信息交换而产生的大量连接，而是统一连接到路由反射器，然后通过反射器与其他节点通信，从而实现交换路由信息
- 通常建议超过100个节点，启用`bgprouterreflector`


#### calico下的pod网络接口
- calico网络插件如何为pod配置网络接口
  - 为每个pod创建一组`veth_pair`，一端注入pod网络名称空间，另一端驻留在宿主机上
    - pod内的一端，通常名称格式为"eth0@ifn"，其中的n是驻留在宿主机上的另一端的ip link编号
    - 驻留宿主机的一端，名称格式为`calixxxxx@ifn`，其中的11位x是经由函数计算生成，而n则是注入到pod网络名称空间中的对端的ip link编号
  
  - pod网络名称空间中，会生成独特的默认路由，将网关指向169.254.1.1
    - `169.254.1.1`该地址是不可用地址，表示没网关，但是这里宿主机做了一个特有设定，及下面的arp proxy功能
  ```shell
  destination    gateway      genmask         flags ... use iface
  0.0.0.0        169.254.1.1  0.0.0.0         ug        eth0
  169.254.1.1    0.0.0.0      255.255.255.255 uh        eth0
  ```

  - 宿主机为每个cali接口都开启了arp proxy的功能，从而让宿主机扮演网关设备，并以自己的mac地址为应答对端pod中发出的所有arp请求
  ```shell
  arp proxy的关键配置：/proc/sys/net/ipv4/conf/dev/proxy_arp
  # 即pod上的网络报文发送到169.254.1.1的这个不可用地址时，可能使用arp代理，从而使用该节点上的物理网卡mac地址进行响应
  ```

- 同一节点上的pod间通信依赖于为每个pod单独配置的路由规则
```shell
destination    gateway  genmask         ... use iface
192.168.252.1  0.0.0.0  255.255.255.255     cali76d294abd03
192.168.252.2  0.0.0.0  255.255.255.255     cali8a8c7a2100c
```

- 不同节点上的pod间通信，则由calico的路由模式决定


#### native routing模式
bird默认使用tcp的179端口

- 报文的流向：pod ---> eth0（容器内接口）---> calixx ---> enp1s0

- 难以使用路由模式的常见场景
  - 集群节点跨越多个子网或路由器，这些路由器依赖目标ip来确定目标主机
  - 对入站数据包强制执行源地址和目标地址核验
  - 阻止所有bgp报文的网络环境(比如公有云端的网络可能已经使用bgp虚拟过一次了，无法再使用bgp)

#### ipip隧道
- 适用性好，尤其是跨多子网的网络环境
- 存在额外开销，mtu一般要设置为1480
- ipip模式同样需要使用bgp协议，以完成路由分发

- 难以使用该模式的常见场景
  - 禁止使用ipip协议的环境，例如：azure
  - 阻止所有bgp报文的网络环境

- 报文的流向：pod --> eth0 --> calixx --> tunl0 --> enp1s0

#### vxlan隧道模式
- 完全不依赖于bgp，开销较之ipip略大(mtu为1450)，但功能更为强大
- 默认使用udp的4789端口
- vxlan隧道出入口：vxlan.calico
- 报文流向：pod --> eth0 --> calixxx --> vxlan.calico --> enp1so



#### 部署calico插件
- 部署方式：
  - operator：由专用的operator和crd管理
  - manifest：基于配置清单进行部署
    - 将kubernetes api作为存储，节点数小于等于50
    - 将kubernetes api作为存储，节点数大于50；重点在于启用typha
    - 使用专用的etcd数据存储，不推荐 

- 部署前要关注的几项配置
  - 选用的pod cidr及子网掩码长度
    - 默认为192.168.0.0/16
    - 可修改
  ```shell
  env:
  - name: calico_ipv4pool_cidr
    value: "192.168.0.0/16"
  - name: calico_ipv4pool_block_size
    value: "24"  # 默认26位
  ```

- 选用的路由模式
  - always, never, cross-subnet
  ```shell
  env:
  # 默认ipip:always，且ipip和vxlan只能二选一
  - name: calico_ipv4pool_ipip
    value: "always"
  - name: calico_ipv4pool_vxlan
    value: "never"
  - name: calico_ipv6pool_vxlan
    value: "never"
  ```

- ipip和vxlan的mtu
  - 默认由configmap/calico-config提供配置
  
- bgp要是用的ip地址
```shell
env:
- name: ip
  value: "autodetect"
  # 选择bgp通过哪个接口将子网信息同步给其他节点
  # autodetect是自动探测
  # 如果探测错了，需要手动进行更改，手动更改的前提是标准化接口名称等
```

#### ippool crd
ippool的作用
- calico可用于为pod配置ip地址的地址池
- 配置路由模式
- 支持在同一集群上配置使用多个地址池
  - 可通过annotation配置默认的ippool
  - 可通过nodeselector限定其使用到的目标节点
- 需要预留一小段地址时，可通过ipreservation crd进行定义
```yaml
apiversion: crd.projectcalico.org/v1
kind: ippool
metadata:
  name: ...
spec:
  alloweduses: <[]string> #支持的使用场景，可选项有tunnel和workload
  blocksize: <integer> # 使用的子网掩码长度，ipv4默认为26，ipv6默认为122
  cidr: <string>  # 使用的cidr
  ipipmode: <string>   # ipip的启用模式，默认为never
  natoutgoing: <boolean>   # 目标地址不在本地cidr范围内时，是否启用snat
  vxlanmode: <string>   # vxlan的启用模式，默认为never
  nodeselector: <string>  # 地址池适用到的目标节点，此为节点的标签选择器
  disablebgpexport: <boolean>  # 是否禁止bgp传播本地址池内的相关路由
  disabled: <boolean> # 是否禁用本地址池
```

#### calico部署
- 重置kubeadm
```shell
kubeadm reset -f 

# 清除网路插件和残留数据
rm -rf /etc/cni/net.d
rm -rf $home/.kube

rm -rf /var/lib/cni
```
- 主节点执行kubeadm初始化
```shell
k8s_release_version=1.30.2 && kubeadm init --control-plane-endpoint kubeapi.feng.org --kubernetes-version=v${k8s_release_version} --pod-network-cidr 192.168.0.0/16 --service-cidr 10.96.0.0/12 --image-repository registry.aliyuncs.com/google_containers --token-ttl=0 --upload-certs --cri-socket=unix:///run/cri-dockerd.sock

# worker节点加入主节点
kubeadm join kubeapi.feng.org:6443 --token se55ec.bu2rwnwjz13os7ss \
--discovery-token-ca-cert-hash sha256:0b6211893138164398ebcb2b17661178e03010dc662ffeccc52843751a68ef91 --cri-socket=unix:///run/cri-dockerd.sock
```

- 下载calico的yaml文件
```shell
curl https://raw.githubusercontent.com/projectcalico/calico/v3.28.1/manifests/calico.yaml -o

# 编辑修改calico.yaml
# 选用的pod cidr及子网掩码长度  
- name: calico_ipv4pool_cidr
  vlaue: "192.168.0.0/16"
  name: calico_ipv4pool_block_size
  values: "24"

# 选用的路由模式：always, never, cross-subnet
env:
- name: calico_ipv4pool_ipip
  value: "always"
- name: calico_ipv4pool_vxlan
  value: "never"
- name: calico_ipv6pool_vxlan
  value: "never"
```

- 执行calico的yaml
```shell
kubectl apply -f calico.yaml

# 下载calicoctl
curl -l https://github.com/projectcalico/calico/releases/download/v3.28.1/calicoctl-linux-amd64 -o calicoctl

# 授权并加入path变量
chmod +x ./calicoctl
mv calicoctl /usr/local/bin

# 使用calicoctl查看node状态
[root@master1 ~]#calicoctl get node -o wide
name               asn       ipv4            ipv6   
master1.feng.org   (64512)   10.0.0.121/24          
worker1.feng.org   (64512)   10.0.0.122/24          
worker2.feng.org   (64512)   10.0.0.123/24          
worker3.feng.org   (64512)   10.0.0.124/24 
```

#### 路由模式分析
- ipip模式
  - ipip的隧道在隧道出入口处，抓不到封装的包，必须在物理网卡处才能看到封装成节点报文的包

#### calico切换模式
```shell
kubectl get ippool default-ipv4-ippool -o yaml > ippool.yaml

vim ippool.yaml

apiversion: crd.projectcalico.org/v1
kind: ippool
metadata:
  annotations:
    projectcalico.org/metadata: '{"creationtimestamp":"2024-08-25t11:47:34z"}'
  creationtimestamp: "2024-08-25t11:47:34z"
  generation: 1
  name: default-ipv4-ippool
  resourceversion: "1521"
  uid: 2a607e35-fdcd-4bf9-affc-86ef119e86ad
spec:
  alloweduses:
  - workload
  - tunnel
  blocksize: 24
  cidr: 192.168.0.0/16
  ipipmode: never    # 将其改为never，当ipip和vxlan都是never时，则成功切换成路由模式
  natoutgoing: true
  nodeselector: all()
  vxlanmode: never

# 在从节点查看路由表
# 隧道节点已经没了
内核 IP 路由表
目标            网关            子网掩码        标志  跃点   引用  使用 接口
0.0.0.0         10.0.0.2        0.0.0.0         UG    0      0        0 eth0
10.0.0.0        0.0.0.0         255.255.255.0   U     0      0        0 eth0
10.244.0.0      10.0.0.121      255.255.255.0   UG    0      0        0 eth0
10.244.1.0      10.0.0.122      255.255.255.0   UG    0      0        0 eth0
10.244.2.0      10.0.0.123      255.255.255.0   UG    0      0        0 eth0
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
192.168.163.0   10.0.0.123      255.255.255.0   UG    0      0        0 eth0
192.168.210.0   0.0.0.0         255.255.255.0   U     0      0        0 *
192.168.210.2   0.0.0.0         255.255.255.255 UH    0      0        0 cali1b10d3456be
192.168.222.0   10.0.0.122      255.255.255.0   UG    0      0        0 eth0
192.168.247.0   10.0.0.121      255.255.255.0   UG    0      0        0 eth0

# 切换混合模式
vim ippool.yaml

apiversion: crd.projectcalico.org/v1
kind: ippool
metadata:
  annotations:
    projectcalico.org/metadata: '{"creationtimestamp":"2024-08-25t11:47:34z"}'
  creationtimestamp: "2024-08-25t11:47:34z"
  generation: 1
  name: default-ipv4-ippool
  resourceversion: "1521"
  uid: 2a607e35-fdcd-4bf9-affc-86ef119e86ad
spec:
  alloweduses:
  - workload
  - tunnel
  blocksize: 24
  cidr: 192.168.0.0/16
  ipipmode: CrossSubnet    # 注意Cross和Subnet之间没有横杠
  natoutgoing: true
  nodeselector: all()
  vxlanmode: never

```

#### BGP Peering
- Calico在各节点间基于BGP传播路由信息
  - BGP是路由器交换路由信息的标准路由协议
    - iBGP：Interior Border Gateway Protocola, 负责在同一AS(自治系统,每个自治系统有自己的自治系统号)内的BGP路由器间传播路由，它通过递归方式进行路径选择
    - eBGP：Exterior Border Gateway Protocol，用于在不同AS间传播BGP路由，它基于hop-by-hop机制进行路径选择
  - 每个路由器都存在一到多个BGP Peer（对等端）
  - Calico Node能够基于BGP协议将物理路由器作为BGP Peer

- BGP的常用拓扑
  - Full-mesh
    - 启用BGP时，Calico默认在所有节点间建立一个AS(64512)，并基于iBGP为它们创建full-mesh连接
    - 该模式较适用于集群规模较小(100个节点以内)的场景
  - Route Reflectors
    - 在大规模的iBGP场景中，BGP route reflectors能显著降低每个节点需要维护的BGP Peer的数量
    - 可选择几个节点作为BGP RR,并在这些RR之间建立full-mesh拓扑
    - 其他节点只需要同这些RR之间建立Peer连接即可
  - ToR(Top of Rack)
    - 节点直接同机柜栈顶的L3交换机建立Peer连接，并禁用默认的full-mesh模式
    - Calico也能够完全支持eBGP机制，从而允许用户灵活构建出需要的网络拓扑

#### 配置Route Reflector模式
- 在100个节点规模以上的Calico集群环境中，为提升iBGP的效率，通常应该建立Router Reflector
- 配置步骤
  - 禁用默认的Full-mesh拓扑
  - 在选定的RR节点上添加专用的节点标签
  - 配置集群节点同RR节点建立BGP会话

- 创建BGPConfiguration对象，禁用默认的full-mesh拓扑
```yaml
apiVersion: crd.projectcalico.org/v1
kind: BGPConfiguration
metadata:
  name: default
spec:
  logSeverityScreen: Info
  # 是否启用full-mesh模式，默认为true
  nodeToNodeMeshEnabled: false
  nodeMeshMaxRestartTime: 120s
  # 使用的自治系统号，默认为64512
  asNumber: 65009
  # BGP要对外通告的Service CIDR
  ServiceClusterIPs:
  - cidr: 10.96.0.0/12
```


#### NetWork Policy



### 存储卷OpenEBS
#### Kubernetes存储架构
- 存储卷的具体的管理操作由相关的控制器向卷插件发起调用请求来完成
  - AD控制器：负责存储设备的Attach/Detach操作
    - Attach：将设备附加到目标节点
    - Detach：将设备从目标节点上拆除
  - 存储卷管理器：负责完成卷的Mount/Umount操作，以及设备的格式化操作等
  - PV控制器：负责PV/PVC的绑定，生命周期管理，以及存储卷的Provision/Delete操作

- Scheduler：特定调度插件的调度决策会受到目标节点上的存储卷的影响

#### Out-of-Tree存储
- CSI简介
  - 容器存储接口规范，与平台无关
  - 驱动程序组件
    - CSI Controller：负责与存储服务的API通信从而完成后端存储的管理操作
    - Node Plugin：也称为CSI Node, 负责在节点级别完成存储卷的管理

#### CSI存储组件和部署架构
- CSI Controller：由Statefulset控制器对象编排于运行，副本量需设置为1，以保证只会该存储服务单个CSI Controller实例；
- Node Plugin：由DaemonSet控制器对象编排运行，以确保每个节点精确运行一个相关的Pod副本

#### CAS(Container Attached Storage)简介
- 容器附加存储(Container Attached Storage)
  - Kubernetes的卷通常是基于外部文件系统或块存储实现，这种存储方案称为共享存储(Shared Storage)
  - CAS则是将存储系统自身部署为Kubernetes集群上的一种较新的存储解决方案
    - 存储系统自身(包括存储控制器)在Kubernetes上以容器化微服务的方式运行
    - 使得工作负载更易于移植，且更容器根据应用程序的需求改动使用的存储
    - 通常基于工作负载或者按集群部署，因此消除了共享存储的跨工作负载甚至是跨集群的爆炸半径
  - 存储在CAS中的数据可以直接从集群内的容器访问，从而能显著减少读写时间
  - OpenEBS是CAS存储机制的著名实现之一，由CNCF孵化
- 基于CAS的存储解决方案，通常包含两大组件
  - 控制平面
    - 负责配置卷以及其他同存储相关的任务
    - 由存储控制器，存储策略以及如何配置数据平面指令组成
  - 数据平面
    - 接收并执行来自控制平面的有关如何保存和访问容器信息的指令
    - 主要组件是实现池化存储的存储引擎，这类引擎本质上负责输入/输出卷路径
    - OpenEBS支持存储引擎包括Mayastor，cStor，Jiva和OpenEBS，LocalPV等


#### 补充：将节点上的pod排空
```shell
kubectl drain
```