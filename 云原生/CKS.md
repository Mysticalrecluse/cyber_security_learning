# CKS

```ABAP
注意：模拟环境里的题目，要按照顺序，从第 1 题往后做。如果先做后面的，可能会导致异常，无法一遍练习完 16 道题
```



## 1.修复kubelet和etcd不安全问题



### 考题

```ABAP
你必须连接到正确的主机，不这样做可能会导致零分。
[candidate@base] $ ssh cks001091

Context
针对 kubeadm 创建的 cluster 运行 CIS 基准测试工具时，发现了多个必须立即解决的问题。

Task
通过配置修复所有问题并重新启动受影响的组件以确保新的设置生效。

修复针对 kubelet 发现的所有以下违规行为：
1.1.1 确保将 anonymous-auth 参数设置为 false                    FAIL
1.1.2 确保 --authorization-mode 参数未设置为 AlwaysAllow        FAIL
注意：尽可能使用 Webhook 身份验证/授权。

修复针对 etcd 发现的所有以下违规行为：
2.1.1 确保 --client-cert-auth 参数设置为 true                   FAIL

模拟环境里，初始化这道题的脚本为 kubelet-etcd.sh
```



### 解答

**【1】 按照题目要求，在 base 节点上执行，切换到题目要求节点** 

考试时务必先按照题目要求，ssh 到对应节点做题。做完后，务必要 exit 退回到 candidate@base 初始节点。 

因为这道题需要切到 root 下操作，所以需要执行 sudo -i 从普通用户 candidate 切到 root。所以退出时，要执行 2 次 exit。

```bash
# 确保在 candidate@base:~$下，再执行切换集群的命令
candidate@base:~$ ssh master01
candidate@master01:~$ sudo -i

# 请先执行如下脚本，初始化这道题的模拟环境配置。实际考试时，不需要执行的。
# 脚本在/root 目录下
# 执行脚本后，集群可能会异常。你按照题目要求，即按照答案的方法修改正确，集群就恢复了。这道题考查的就是，按照题目要求修复好集群。
root@master01:~# sh kubelet-etcd.sh
请稍等1分钟，正在初始化这道题的环境配置。
Please wait for 1 minutes, the environment configuration for this question is being initialized.
```



**【2】 修改 kubelet**

```bash
#注意 vim 文件后，要先输入 :set paste 回车，防止 yaml 文件空格错序，然后再输入 i 回车，开始编辑文件。
root@master01:~# vim /var/lib/kubelet/config.yaml 
apiVersion: kubelet.config.k8s.io/v1beta1
authentication:
  anonymous:       # 在 anonymous 下，注意这两个 enabled 千万不要搞混，anonymous 应该为 false，webhook 应该为 true。
    enabled: false # 将true改为false，禁止匿名连接
# Webhook 模式核心原理
# 当 API Server 收到用户请求时，它会将这个请求打包为一个 SubjectAccessReview 请求，发送到你指定的 Webhook 服务，由外部服务决定是否允许这个请求。权限判断逻辑可以自定义
  webhook:
    cacheTTL: 0s
    enabled: true  # 改为true，webhook
  x509:
    clientCAFile: /etc/kubernetes/pki/ca.crt
authorization:
  mode: Webhook   # 原AlwaysAllow改为Webhook,W注意大写
  webhook:
    cacheAuthorizedTTL: 0s
    cacheUnauthorizedTTL: 0s
......
``
```

**【3】 修改 etcd**

```bash
root@master01:~# vim /etc/kubernetes/manifests/etcd.yaml
......
spec:
  containers:
  - command:
    - etcd
    - --advertise-client-urls=https://11.0.1.111:2379
    - --cert-file=/etc/kubernetes/pki/etcd/server.crt
    - --client-cert-auth=true  # 这里改为true
......
```

**【4】 编辑完后重新加载配置文件，并重启 kubelet**

```bash
root@master01:~# systemctl daemon-reload 
root@master01:~# systemctl restart kubelet.service
```

修改完成后，等待 5 分钟，再检查一下所有 pod，确保模拟环境里除了 clever-cactus 和 ingress-nginx 之外，其他 pod 都 Running 的。 <span style='color:red'>强烈建议，考试时，先做下一道题，后面再回来切集群，并检查。</span>

**【5】别忘记，做完后，退回到 base 节点，这样下一道题才能继续切节点。**

```bash
# 退出 root 用户，退回到 candidate 用户下
exit
# 退出 cks001091 节点，返回到 candidate@base 用户和节点下
exit
```

<span style='color:red'>做下一题之前，确保除了 clever-cactus 和 ingress-nginx 之外，其他 pod 都 Running 的</span>>，特别是 kube-apiserver-master01 也正常。（考试时，只要确保这个 apiserver 是正常的）

模拟环境里，tigera-operator 和 calico-apiserver 和 calico-system 这几个 pod 可能需要比较长的时间才能恢复到 Running 状态，此时只要确保其他 pod 已恢复 Running（除了 clever-cactus 和 ingress-nginx），就可以继续做题了。



## 2. TLS Secret



### 考题

```ABAP
你必须连接到正确的主机。不这样做可能导致零分
[candidate@base] $ ssh cks000040

Context
您必须使用存储在 TLS Secret 中的 SSL 文件，来保护 Web 服务器的安全访问。

Task
在 clever-cactus namespace 中为名为 clever-cactus 的现有 Deployment 创建名为 clever-cactus 的 TLS Secret 。

使用以下 SSL 文件：
证书 /home/candidate/ca-cert/web.k8s.local.crt
密钥 /home/candidate/ca-cert/web.k8s.local.key

Deployment 已配置为使用 TLS Secret。
请勿修改现有的 Deployment。
```



### 解答

**【1】 按照题目要求，在 base 节点上执行，切换到题目要求节点** 

考试时务必先按照题目要求，ssh 到对应节点做题。做完后，务必要 exit 退回到 candidate@base 初始节点。

```bash
# 确保在 candidate@base:~$下，再执行切换集群的命令
candidate@base:~$ ssh master01
```

**【2】 将生成的 TLS 证书和密钥存储到 K8S 的 Secret 对象中**

<mark><span style="color:red">特别注意，--cert 和--key 后面，要写绝对路径。不要要写 ~/ca-cert/web.k8s.local.crt 这种形式，会报错。</span></mark>

```bash
candidate@master01:~$ kubectl -n clever-cactus create secret tls clever-cactus --cert=/home/candidate/ca-cert/web.k8s.local.crt --key=/home/candidate/ca-cert/web.k8s.local.key
secret/clever-cactus created

# 查看创建的Secret
candidate@master01:~$ kubectl -n clever-cactus get secrets 
NAME            TYPE                DATA   AGE
clever-cactus   kubernetes.io/tls   2      13s

# 等 3 分钟左右，再次检查 deployment，显示 1/1 即表示正常了
candidate@master01:~$ kubectl -n clever-cactus get pod
NAME                             READY   STATUS    RESTARTS   AGE
clever-cactus-8445cd87c8-pgzjf   1/1     Running   0          32d
```

**【3】别忘记，做完后，退回到 base 节点，这样下一道题才能继续切节点。**

```bash
# 退出 cks000040 节点，返回到 candidate@base 用户和节点下
candidate@master01:~$ exit
```



## Dockerfile 安装最佳实践



### 考题

```ABAP
你必须连接到正确的主机。不这样做可能导致零分。
[candidate@base] $ ssh cks001095

Task
分析和编辑给定的 Dockerfile /cks/docker/Dockerfile
并修复在文件中拥有的突出的安全/最佳实践问题的一个指令。

分析和编辑给定的清单文件 /cks/docker/deployment.yaml ，
并修复在文件中拥有突出的安全/最佳实践问题的一个字段。

注意：请勿添加或删除配置设置；只需修改现有的配置设置让以上两个配置设置都不再有安全/最佳实践问题。

注意：如果您需要非特权用户来执行任何项目，请使用用户 ID 65535 的用户 nobody 。
```

