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