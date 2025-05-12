# Kubernetes 排错案例

## 排错案例1

### 问题背景

#### **运行环境**

- **单 Master 节点**：即 **etcd、scheduler、controller-manager、apiserver** 都运行在 **单个 Master 节点**。
- **Kubernetes CNI**：Calico
- **Service 网络模式**：IPVS
- **关键组件**：etcd、kube-apiserver、kube-scheduler、kube-proxy、CNI（Calico）

#### **问题起因**

管理员为了修复 Kubernetes 集群访问异常，进行了以下操作：

1. **备份** 了 **3 天前的 etcd 数据**
2. **重启** 了 **Docker**
3. **恢复** 了 **3 天前的 etcd 数据**
4. **访问服务依然异常**

**错误点：**

- **etcd 数据回滚 3 天前**，意味着 **所有 Kubernetes 资源（Deployments、Services、Endpoints）都恢复到了 3 天前的状态**，这会导致资源版本（ResourceVersion）不匹配，甚至 pod 失效。



### 故障排查与修复

故障恢复过程分为 **三个核心阶段**：

1. **Deployment 资源版本不匹配**
2. **Iptables 丢失导致 Service 访问异常**
3. **CNI 连接异常导致 Pod 网络不可用**



#### 阶段 1：Deployment 资源版本不匹配

**问题表现**

- Pod 处于 **`Pending`** 状态
- **无法调度到节点**
- **删除 pod 后无法重建**
- **尝试删除 `kube-scheduler`，发现无法重新创建**
- **`kubectl rollout history` 发现 Deployment 版本不匹配**
- **`kube-apiserver` 日志中出现 reversion 版本不匹配**

**排查思路**

**检查调度器（Scheduler）**

- **删除 kube-scheduler Pod** 但未能自动重建
- **手动移除并恢复 `/etc/kubernetes/manifests/kube-scheduler.yaml`** 重新创建 `kube-scheduler`
  - 此时仍然无法调度pod，因此怀疑是在scheduler之前出现了问题，查看api-server的日志，发现有很多reversion版本不匹配的错误，应该是集群中的资源版本和etcd中的资源版本不匹配导致的

**检查 API Server**

- 使用 `kubectl logs -n kube-system kube-apiserver` 查看日志
- 发现 **资源版本不匹配**，说明 etcd 版本与 API Server 中的对象版本对不上

**检查 etcd 健康状况**

```bash
etcdctl endpoint health
etcdctl endpoint status --write-out=table
```

结果显示 etcd 正常

**查看 Deployment 版本**

```bash
kubectl rollout history deployment/<deployment_name>
```

**回滚 Deployment 版本（最终解决方案）**

```bash
kubectl rollout undo deployment/<deployment_name> --to-revision=<version>
```

**解决方案**

- 通过 **回滚 Deployment** 解决资源版本不匹配问题。
- **观察 Pod 重新创建情况，确保可以调度。**
- **Pod 运行后，检查访问是否恢复。**



#### 阶段 2：iptables 丢失导致 Service 访问异常

**问题表现**

- Service 无法访问
- `kubectl describe service` 发现 **没有 endpoints**
- `iptables-save` 发现 **丢失 Kubernetes 相关规则**
- `ipvsadm -l -n` 发现 **没有 Service 对应的 Pod IP**

**排查思路**

1. **检查 Service 是否存在**

   ```bash
   kubectl get svc -A
   ```

2. **检查 Endpoint 是否被正确分配**

   ```bash
   kubectl get endpoints -A
   ```

3. **检查 iptables 规则**

   ```bash
   iptables-save | grep KUBE
   ```

4. **检查 ipvs 规则**

   ```bash
   ipvsadm -l -n  # 发现service的cluster IP没有对应的pod IP
   ```

5. **检查 kube-proxy 日志**

   ```bash
   kubectl logs -n kube-system -l k8s-app=kube-proxy  # 并未发现任何异常
   ```

**解决方案**

- 发现 **iptables 规则丢失，重新初始化 kube-proxy**

  ```bash
  kubeadm init phase addon kube-proxy --kubeconfig ~/.kube/config --apiserver-advertise-address <api-server-ip>
  ```

- **重启 kube-proxy**

  ```bash
  kubectl delete pod -n kube-system -l k8s-app=kube-proxy
  ```

- **重新创建 Service**

  ```bash
  kubectl delete svc <service-name>
  kubectl apply -f <service-yaml>
  ```

  

#### 阶段 3：CNI 连接异常

**问题表现**

- `kubectl describe pod <pod>` 显示 CNI 连接错误

  ```bash
  networkPlugin cni failed to set up pod "webhook-1" network: Get "https://[10.233.0.1]:443/api/v1/namespaces/volcano-system": dial tcp 10.233.0.1:443: i/o timeout
  ```

- **calico-node pod 处于非 Ready 状态**

- `telnet 10.233.0.1 443` 发现 API Server 无法访问

**排查思路**

- **检查 CNI 配置**

  ```bash
  # calico的/etc/cni/net.d/10-calico.conflist配置文件中定义了连接apiserver所需的kubeconfig文件
  cat /etc/cni/net.d/10-calico.conflist
  ```

- **检查 CNI 访问 API Server**

  ```bash
  # /etc/cni/net.d/calico-kubeconfig中就定义了连接apiserver所需的地址和端口
  cat /etc/cni/net.d/calico-kubeconfig
  ```

- **检查 calico-node 日志**

  ```bash
  kubectl logs -n kube-system -l k8s-app=calico-node
  ```

- **查看 API Server 地址**

  ```bash
  kubectl get endpoints -n default kubernetes
  ```

  

**解决方案**

- **修复 Calico CNI 配置**

  ```yaml
  - name: KUBERNETES_SERVICE_HOST
    value: <api-server-pod-ip>
  - name: KUBERNETES_SERVICE_PORT
    value: <api-server-pod-port>
  ```

- **删除并重新创建 calico-node**

  ```bash
  kubectl delete pod -n kube-system -l k8s-app=calico-node
  ```

- **确认 CNI 连接恢复**

  ```bash
  telnet 10.233.0.1 443
  ```



### 案例知识点补充

#### 为什么 etcd 数据回滚会导致资源版本不匹配？

在 Kubernetes 集群中，**所有的资源对象（如 Pod、Deployment、Service 等）都存储在 etcd**，并且这些资源都有一个**资源版本（Resource Version）**，用于标识该资源的当前状态。

当 **etcd 数据回滚** 时，会出现 **资源版本不匹配** 的问题，主要是因为

- etcd 版本回滚后，资源状态恢复到了过去的某个时间点，但 API Server 的状态仍然是当前时间点的资源。
- API Server 在处理资源变更时，依赖于 etcd 的递增版本号（revision）。如果 etcd 被回滚，这些 revision 可能会错乱，导致 API Server 无法正确同步资源
- **Controller Manager、Scheduler 依赖的资源版本（ResourceVersion）和 etcd 不匹配，可能导致调度失败、无法更新 Deployment、无法创建新 Pod。**



#### 什么是资源版本（Resource Version）？

**ResourceVersion** 是 Kubernetes API 中的一个字段，每个 Kubernetes 资源（如 Pod、Deployment）在 **etcd** 中存储时都会有一个 **版本号**。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
  namespace: default
  resourceVersion: "13579"  # 资源版本号
```

- 每次资源更新（增删改）时，resourceVersion 都会增加
- 当 API Server 查询资源时，会根据 resourceVersion 确保获取的是最新的状态。

**举例**

假设 etcd 存储了如下 Deployment 资源

```yaml
Deployment A:
  ResourceVersion: 1001
Deployment B:
  ResourceVersion: 1002
```

- 之后某个 Pod 进行了 `kubectl apply`，Deployment A 的 `ResourceVersion` 变成 `1003`
- 但是如果 **回滚 etcd 数据**（例如回到 `resourceVersion: 1001`），那么



#### etcd 资源版本如何影响 Kubernetes？

etcd **存储的所有 Kubernetes 资源**，例如：

- **Deployments**
- **Pods**
- **Services**
- **ConfigMaps**
- **Secrets**
- **DaemonSets**

这些资源都有一个 **resourceVersion**，用于跟踪变更。

当 etcd 发生回滚，可能会导致：

1. **Pod 无法调度**
   - **Scheduler 依赖于 API Server 获取最新的 Pod 版本**，如果 API Server 发现 etcd 版本比自己低，调度器可能无法正常工作。
   - `kubectl get pods` 可能会出现旧版本的 Pod，但无法更新或调度新的 Pod。
2. **Deployment/DaemonSet 失效**
   - `kubectl rollout history deployment/<deployment_name>` 可能会显示旧版本，而新的 Pod 可能因为资源版本不匹配而无法创建。
3. **Service 找不到 Endpoints**
   - `kubectl get endpoints` 可能会出现为空的情况，因为 etcd 里的 Service 可能丢失了最新的 Endpoint 绑定信息。
4. **API Server 无法正确查询资源**
   - `kubectl get pods` 可能出现 **"resource version too old"** 错误。



#### 为什么 etcd 回滚后，API Server 可能会报错？

**因为 API Server 和 etcd 之间的通信基于资源版本的递增**，当 etcd 发生回滚时，API Server 仍然记得之前的较高版本的 resourceVersion，但 etcd 里存储的是旧数据，导致 API Server 发现：

- 之前存在 `resourceVersion: 1050` 的资源
- 但 etcd 里现在只有 `resourceVersion: 1000`
- 于是 **API Server 认为数据不一致，可能会拒绝更新或出现错误**

**💡 解决方案：** 如果 etcd 回滚了数据，并且 Kubernetes 组件出现问题，可能的修复方式：

- **完全重启 API Server**

  ```bash
  systemctl restart kube-apiserver
  ```

  

- **检查 etcd 数据一致性**

  ```bash
  etcdctl endpoint health
  etcdctl endpoint status --write-out=table
  ```

- **手动回滚 Deployment 到正确版本**

  ```bash
  kubectl rollout history deployment/<deployment_name>
  kubectl rollout undo deployment/<deployment_name> --to-revision=<version>
  ```

- **删除并重建 pod**

  ```bash
  kubectl delete pod --all -n default
  ```

- **如果问题严重，考虑重新初始化 etcd**

  ```bash
  kubeadm init phase etcd
  ```

  **重新初始化 etcd**（例如 `kubeadm init phase etcd`），那么 **etcd 的数据通常会被清空**，集群中的所有资源（Pods、Deployments、Services、ConfigMaps 等）都会丢失。**这类似于全新部署 etcd。**





## 排错案例2

### 问题背景

**部署metrics-server出现报错**

```bash
[root@master1]$ kubectl get pod -A
NAMESPACE     NAME                                       READY   STATUS    RESTARTS   AGE
kube-system   calico-kube-controllers-864cf7ff46-khgtl   1/1     Running   0          10h
kube-system   calico-node-6nvz5                          1/1     Running   0          10h
kube-system   calico-node-jbvpb                          1/1     Running   0          10h
kube-system   calico-node-jvz7j                          1/1     Running   0          10h
kube-system   calico-node-w9xvw                          1/1     Running   0          10h
kube-system   coredns-76fccbbb6b-95jsl                   1/1     Running   0          11h
kube-system   coredns-76fccbbb6b-p8cbc                   1/1     Running   0          11h
kube-system   etcd-master1                               1/1     Running   1          11h
kube-system   kube-apiserver-master1                     1/1     Running   1          11h
kube-system   kube-controller-manager-master1            1/1     Running   1          11h
kube-system   kube-proxy-cpn54                           1/1     Running   0          11h
kube-system   kube-proxy-gvhmb                           1/1     Running   0          11h
kube-system   kube-proxy-hwnjv                           1/1     Running   0          11h
kube-system   kube-proxy-tknzn                           1/1     Running   0          11h
kube-system   kube-scheduler-master1                     1/1     Running   1          11h
kube-system   metrics-server-5488b6568-f9pbx             0/1     Running   0          31m  # 这里始终显示0/1
```



### 故障排查与修复

```bash
# 查看pod的日志和状态
[root@master1]$ kubectl describe pod -n kube-system metrics-server-5488b6568-f9pbx 
Events:
  Type     Reason     Age                  From               Message
  ----     ------     ----                 ----               -------
  Normal   Scheduled  3m55s                default-scheduler  Successfully assigned kube-system/metrics-server-5488b6568-f9pbx to work1.mystical.org
  Normal   Pulling    3m54s                kubelet            Pulling image "harbor.magedu.mysticalrecluse.com/k8simage/metrics-server:v0.7.2"
  Normal   Pulled     3m53s                kubelet            Successfully pulled image "harbor.magedu.mysticalrecluse.com/k8simage/metrics-server:v0.7.2" in 1.366s (1.366s including waiting). Image size: 19493207 bytes.
  Normal   Created    3m53s                kubelet            Created container: metrics-server
  Normal   Started    3m53s                kubelet            Started container metrics-server
  Warning  Unhealthy  3s (x23 over 3m30s)  kubelet            Readiness probe failed: HTTP probe failed with statuscode: 500
  
# 查看日志
[root@master1]$ kubectl logs -n kube-system metrics-server-5488b6568-f9pbx 
......
\"https://10.2.1.151:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.151 because it doesn't contain any IP SANs" node="master1"
E0502 06:13:50.939933       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.198:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.198 because it doesn't contain any IP SANs" node="work3.mystical.org"
E0502 06:13:50.951533       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.238:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.238 because it doesn't contain any IP SANs" node="work2.mystical.org"
E0502 06:13:50.954955       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.106:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.106 because it doesn't contain any IP SANs" node="work1.mystical.org"
I0502 06:13:51.035049       1 shared_informer.go:318] Caches are synced for client-ca::kube-system::extension-apiserver-authentication::requestheader-client-ca-file
I0502 06:13:51.035167       1 shared_informer.go:318] Caches are synced for RequestHeaderAuthRequestController
I0502 06:13:51.035240       1 shared_informer.go:318] Caches are synced for client-ca::kube-system::extension-apiserver-authentication::client-ca-file
E0502 06:14:05.938933       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.238:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.238 because it doesn't contain any IP SANs" node="work2.mystical.org"
E0502 06:14:05.943590       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.106:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.106 because it doesn't contain any IP SANs" node="work1.mystical.org"
```

说明你的 Kubernetes 集群中 **kubelet 的 TLS 证书**没有包含对应节点的 IP 或主机名（SAN 字段缺失），所以 `metrics-server` 或 `scraper` 无法通过 HTTPS 成功拉取节点指标。



#### 错误解释（核心问题）

Kubernetes 的 `kubelet` 启动了一个 HTTPS 服务在 `10250` 端口（暴露 `/metrics/resource` 等）：

- 该服务使用的是 `/var/lib/kubelet/pki/kubelet.crt` 证书；
- 这个证书由 `kubelet` 启动时自动请求签发（Bootstrapping）；
- **但你的集群没有配置正确的 SAN 签发策略**，导致：

> 所有节点的 kubelet 证书只包含了 `CN=kubelet`，**没有 IP 或主机名 SAN**



### 解决方案

#### 方案一：无需重装，使用 `kubelet-serving` CSR 动态重签证书（推荐）

Kubelet 会自动创建一个 `kubelet-serving` 的 CSR 请求（CertificateSigningRequest），你可以手动批准：

**查看CSR请求**

```bash
[root@master1]$ kubectl get csr
No resources found
```

❌ `No resources found`，说明 kubelet 没有发出新的证书签名请求（CSR）

**这通常有两个原因**

- 原因 1：Kubelet 没有配置自动向 API 申请证书（client 和 serving）
  - 默认 kubeadm 初始化的 kubelet 会自动申请两种证书：
    - **client 证书**：用于 kubelet 自己连 API server
    - **serving 证书**：用于其他组件访问 kubelet 的 10250 端口
  - 但你当前可能没有启用 serving 证书自动申请功能。



**检查 kubelet 配置**

查看 `/var/lib/kubelet/config.yaml` 中有没有：

```bash
serverTLSBootstrap: true
```

如果 **缺失或为 false**，则 kubelet 不会自动申请 serving 证书。



#### 解决步骤（启用 serverTLSBootstrap）

**第一步：编辑 kubelet 配置文件**

```bash
# 编辑kubelet配置文件
[root@master1]$ vim /var/lib/kubelet/config.yaml
......
serverTLSBootstrap: true    # 添加或修改这行
```

保存后退出。



**第二步：重启 kubelet**

```bash
[root@master1]$ systemctl restart kubelet.service
```



**第三步：查看并批准 CSR**

```bash
[root@master1]$ kubectl get csr
NAME        AGE   SIGNERNAME                      REQUESTOR             REQUESTEDDURATION   CONDITION
csr-jbphr   8s    kubernetes.io/kubelet-serving   system:node:master1   <none>              Pending

# 当前是pending状态，手动批准证书请求
[root@master1]$ kubectl certificate approve csr-jbphr
certificatesigningrequest.certificates.k8s.io/csr-jbphr approved

# 再次查看
[root@master1]$ kubectl get csr
NAME        AGE    SIGNERNAME                      REQUESTOR             REQUESTEDDURATION   CONDITION
csr-jbphr   111s   kubernetes.io/kubelet-serving   system:node:master1   <none>              Approved,Issued
```

**Kubelet 会自动替换自己的证书，稍等几分钟 `metrics-server` 会恢复正常抓取**。



**查看最终的效果**

```bash
[root@master1]$ kubectl get pod -A
NAMESPACE     NAME                                       READY   STATUS    RESTARTS   AGE
kube-system   calico-kube-controllers-864cf7ff46-khgtl   1/1     Running   0          10h
kube-system   calico-node-6nvz5                          1/1     Running   0          10h
kube-system   calico-node-jbvpb                          1/1     Running   0          10h
kube-system   calico-node-jvz7j                          1/1     Running   0          10h
kube-system   calico-node-w9xvw                          1/1     Running   0          10h
kube-system   coredns-76fccbbb6b-95jsl                   1/1     Running   0          11h
kube-system   coredns-76fccbbb6b-p8cbc                   1/1     Running   0          11h
kube-system   etcd-master1                               1/1     Running   1          11h
kube-system   kube-apiserver-master1                     1/1     Running   1          11h
kube-system   kube-controller-manager-master1            1/1     Running   1          11h
kube-system   kube-proxy-cpn54                           1/1     Running   0          11h
kube-system   kube-proxy-gvhmb                           1/1     Running   0          11h
kube-system   kube-proxy-hwnjv                           1/1     Running   0          11h
kube-system   kube-proxy-tknzn                           1/1     Running   0          11h
kube-system   kube-scheduler-master1                     1/1     Running   1          11h
kube-system   metrics-server-5488b6568-f9pbx             1/1     Running   0          32m

# 测试
[root@master1]$ kubectl top pod -A
NAMESPACE     NAME                              CPU(cores)   MEMORY(bytes)   
kube-system   calico-node-6nvz5                 25m          120Mi           
kube-system   etcd-master1                      21m          46Mi            
kube-system   kube-apiserver-master1            51m          255Mi           
kube-system   kube-controller-manager-master1   18m          49Mi            
kube-system   kube-proxy-hwnjv                  10m          17Mi            
kube-system   kube-scheduler-master1            12m          22Mi 
```



## 排错案例3

### 问题背景

worker节点加入kubernetes集群，使用负载均衡器的IP，而不是直接使用master节点IP，但是导致join加入集群的时候阻塞在初始化阶段

| 行为                              | 结果                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| `curl -k https://10.2.1.139:6443` | ✅ 返回 403，说明 **TLS 成功握手 + 请求被 kube-apiserver 接收 + 匿名用户被拒绝** |
| `kubeadm join 10.2.1.139:6443`    | ❌ 阻塞在 preflight，说明 **连接建立但请求未成功返回（或验证失败）** |

#### 问题起因

 kube-apiserver 返回证书中未包含该 SNI，导致 kubeadm TLS 验证失败卡死。



#### 知识点补充：SNI 是怎么参与 `kubeadm join` 的？

- `kubeadm join` 使用 HTTPS+TLS 和 apiserver 通信；
- 它会发起带有 SNI 的 TLS Client Hello；
- **如果 kube-apiserver 返回的证书中不包含这个 SNI（如 VIP 或 HAProxy IP），就会被 TLS 客户端验证失败！**



**所以：如果你 kubeadm init 时没有指定 SNI / SAN（如 HAProxy 的 IP），那么返回的证书只包含：**

- `CN = kube-apiserver`
- `SubjectAltName: DNS: kube-apiserver, IP: 10.2.1.151`（master IP）

> 当你使用 `curl -k` 可以绕过 TLS 校验（`-k` 跳过 SNI 验证），但 `kubeadm join` 不会这么做，它是严格验证的。



#### 对SNI内容缺失的验证

你可以手动查看 kube-apiserver 证书内容：

```bash
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout | grep -A1 "Subject Alternative Name"
```

如果输出中没有包含 `10.2.1.139` 或 `10.2.0.100`（你用于 join 的地址）：

```bash
X509v3 Subject Alternative Name:
    DNS:kubernetes, IP Address:10.2.1.151
```

那就说明了——**join 时使用的 IP 不在 SAN 中 → TLS 验证失败卡住**



### 故障排查与修复

初始化的时候在 `kubeadm init` 配置中添加 SNI/SAN

创建一个 `kubeadm-config.yaml`：

```yaml
apiVersion: kubeadm.k8s.io/v1beta3
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: 10.2.1.151
  bindPort: 6443

---
apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration
apiServer:
  certSANs:
    - "10.2.1.151"
    - "10.2.1.139"     # HAProxy真实IP
    - "10.2.0.100"     # VIP
    - "127.0.0.1"
    - "kubernetes"
    - "kubernetes.default"
```

然后使用：

```bash
kubeadm init --config kubeadm-config.yaml
```

这将生成包含多个 IP 的 SAN 证书，支持后续任意地址 join。



**⚠️ 如果集群已部署，可以重新生成 apiserver 证书，不必全部重装（使用 `kubeadm alpha certs` 工具）**。



## 排错案例4

### 问题背景

由于apiserver证书过期，导致apiserver反复崩溃



### 故障排查与修复

```bash
[root@master01 ~]# nerdctl logs <CONTAINER ID> --namespace k8s.io
# 发现是证书过去导致错误
```



#### 修复方法1：使用 `kubeadm` 自动重新生成证书（推荐）

如果你是通过 `kubeadm` 部署的集群，可以使用以下命令自动续期：

```bash
[root@master01 ~]# kubeadm certs renew all
```

然后重启 `kubelet`，apiserver 会重新加载新证书：

```bash
[root@master01 ~]# systemctl restart kubelet
```

注意：此命令默认使用 `/etc/kubernetes/pki/ca.crt` 和 `ca.key` 来签发新证书，默认有效期为 1 年。



#### 修复方法2：自定义生成有效期更长的新证书

如果你希望有效期不是 1 年，可以手动生成： 

**生成私钥（如果没有）**

```bash
[root@master01 ~]# openssl genrsa -out apiserver.key 2048
```

**创建证书请求（CSR）**

创建 `apiserver-csr.conf` 文件：

```ini
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
CN = kube-apiserver

[v3_req]
keyUsage = keyEncipherment, dataEncipherment, digitalSignature
extendedKeyUsage = serverAuth, clientAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = kubernetes
DNS.2 = kubernetes.default
DNS.3 = kubernetes.default.svc
DNS.4 = kubernetes.default.svc.cluster.local
IP.1 = 10.96.0.1
IP.2 = 127.0.0.1
IP.3 = <你的API Server IP或VIP>
```

**生成 CSR 文件**

```bash
[root@master01 ~]# openssl req -new -key apiserver.key -out apiserver.csr -config apiserver-csr.conf
```

**使用集群的 CA 签发证书，有效期自定义（如 10 年）**

```bash
openssl x509 -req -in apiserver.csr -CA /etc/kubernetes/pki/ca.crt \
  -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial \
  -out apiserver.crt -days 3650 -extensions v3_req -extfile apiserver-csr.conf
```

**替换证书后重启 kubelet**

```bash
cp apiserver.crt /etc/kubernetes/pki/
cp apiserver.key /etc/kubernetes/pki/
systemctl restart kubelet
```



## 排错案例5

### 问题背景

在部署了metrics-server之后，执行`kubectl top node`，返回如下

```bash
[root@master1]# kubectl top node
NAME                 CPU(cores)   CPU(%)      MEMORY(bytes)   MEMORY(%)   
master1              232m         5%          1611Mi          13%         
work1.mystical.org   <unknown>    <unknown>   <unknown>       <unknown>   
work2.mystical.org   <unknown>    <unknown>   <unknown>       <unknown>   
work3.mystical.org   <unknown>    <unknown>   <unknown>       <unknown>   
```

可以看出所有的worker节点的信息无法采集



查看metrics-server日志结果如下

```bash
[root@master1]# kubectl -n kube-system edit deployments.apps metrics-server
......
E0504 07:28:05.953674       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.198:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.198 because it doesn't contain any IP SANs" node="work3.mystical.org"
E0504 07:28:20.938137       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.106:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.106 because it doesn't contain any IP SANs" node="work1.mystical.org"
E0504 07:28:20.939317       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.238:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.238 because it doesn't contain any IP SANs" node="work2.mystical.org"
E0504 07:28:20.950004       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.198:10250/metrics/resource\": tls: failed to verify certificate: x509: cannot validate certificate for 10.2.1.198 because it doesn't contain any IP SANs" node="work3.mystical.org"
E0504 07:28:35.936570       1 scraper.go:149] "Failed to scrape node" err="Get \"https://10.2.1.198:10250/metrics/reso
```



### 故障排查与修复

#### **推荐方法（最常用）**

编辑 metrics-server 的 Deployment，**加上 `--kubelet-insecure-tls` 参数**：

```yaml
[root@master1] # kubectl -n kube-system edit deployment metrics-server
containers:
- name: metrics-server
  args:
    - --kubelet-insecure-tls      # 添加这行
    - --kubelet-preferred-address-types=InternalIP,Hostname

# 修改后，重启kubelet
[root@master1] # systemctl restart kubelet
```



#### **进阶方法（安全性高，但复杂）**：

1. 为每个 node 生成 kubelet 的证书，**且必须在 SAN 里包含每个节点的 IP**；
2. kubelet 启动时指定该证书；
3. metrics-server 信任这些证书；
4. 重新部署集群或手动更新 kubelet 的 cert。

一般生产环境中为了省事都走第一个方案，**只加 `--kubelet-insecure-tls`**。



##### **全流程步骤（适用于每个 Worker 节点）**

⚠️ 操作前 **备份证书**，确保掌握节点重启和 kubelet 日志排查能力。

**第一步：编辑 kubelet 配置文件**

编辑或创建 `/var/lib/kubelet/config.yaml` 中，加入：

```yaml
tlsCertFile: /var/lib/kubelet/pki/kubelet.crt
tlsPrivateKeyFile: /var/lib/kubelet/pki/kubelet.key
```

**第二步：生成自定义 kubelet 证书（以 `10.2.1.198` 为例）**

创建 OpenSSL 配置（`kubelet-openssl.cnf`）：

```ini
[ req ]
distinguished_name = req_distinguished_name
x509_extensions = v3_req
prompt = no

[ req_distinguished_name ]
CN = system:node:work3.mystical.org
O = system:nodes

[ v3_req ]
basicConstraints = critical,CA:FALSE
keyUsage = critical,digitalSignature,keyEncipherment
extendedKeyUsage = serverAuth,clientAuth
subjectAltName = @alt_names

[ alt_names ]
IP.1 = 10.2.1.198
DNS.1 = work3.mystical.org
```

你需要为每个节点更换 `CN` 和 `IP/DNS`

生成私钥和证书签署请求：

```bash
openssl genrsa -out kubelet.key 2048

openssl req -new -key kubelet.key -out kubelet.csr \
  -config kubelet-openssl.cnf
```

使用集群 CA 签名生成证书：

```bash
openssl x509 -req -in kubelet.csr -CA /etc/kubernetes/pki/ca.crt \
  -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial \
  -out kubelet.crt -days 365 -extensions v3_req \
  -extfile kubelet-openssl.cnf
```

**第三步：放置证书并重启 kubelet**

```bash
mkdir -p /var/lib/kubelet/pki/
cp kubelet.crt kubelet.key /var/lib/kubelet/pki/

systemctl restart kubelet
```

**第四步：确认 Node 正常 & metrics-server 不再报 SAN 错误**

- `kubectl get node`
- `kubectl top node`
- `kubectl logs -n kube-system deploy/metrics-server`

