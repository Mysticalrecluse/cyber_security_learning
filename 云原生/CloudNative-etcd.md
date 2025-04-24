## CloudNative—etcd

### etcd简介

- etcd是CoreOS团队于2013年6月发起的开源项目，它的目标是构建一个高可用的分布式键值（key-value）数据库。etcd内部采用raft协议作为一致性算法，etcd基于Go语言实现
- 官方网站：http://etcd.io
- github地址：https://github.com/etcd-io/etcd
- 官方硬件推荐：https://etcd.io/docs/v3.5/op-guide/hardware/
- 官方文档：https://etcd.io/docs/v3.5/op-guide/maintenance



![image-20250409120720107](../markdown_img/image-20250409120720107.png)



**etcd具有下面这些属性**

- 完全复制：集群中的每个节点都可以使用完整的存档
- 高可用性：Etcd可用于避免硬件的单点故障或网络问题
- 一致性：每次读取都会返回跨多主机的最新写入
- 简单：包括一个定义良好，面向用户的API（gRPC）
- 安全：实现了带有可选的客户端证书身份验证的自动化TLS
- 快速：每秒10000次写入基准速度
- 可靠：使用Raft算法实现了存储的合理分布Etcd的工作原理



**etcd的service文件**

```bash
[root@k8s-10-0-0-206 ~]#cat /etc/systemd/system/etcd.service
[Unit]
Description=Etcd Server
After=network.target
After=network-online.target
Wants=network-online.target
Documentation=https://github.com/coreos

[Service]
Type=notify
WorkingDirectory=/var/lib/etcd
# etcd没有配置文件，直接传递参数
ExecStart=/usr/local/bin/etcd \
  --name=etcd-10.0.0.206 \        # etcd基于当前节点名称识别节点，因此etcd集群的每个节点名称不能一样
  --cert-file=/etc/kubernetes/ssl/etcd.pem \
  --key-file=/etc/kubernetes/ssl/etcd-key.pem \
  --peer-cert-file=/etc/kubernetes/ssl/etcd.pem \
  --peer-key-file=/etc/kubernetes/ssl/etcd-key.pem \
  --trusted-ca-file=/etc/kubernetes/ssl/ca.pem \
  --peer-trusted-ca-file=/etc/kubernetes/ssl/ca.pem \
  --initial-advertise-peer-urls=https://10.0.0.206:2380 \   # 通告自己的集群端口
  --listen-peer-urls=https://10.0.0.206:2380 \              # 集群之间的通信端口
  --listen-client-urls=https://10.0.0.206:2379,http://127.0.0.1:2379 \   # 客户端访问地址
  --advertise-client-urls=https://10.0.0.206:2379 \                      # 通告自己的客户端端口
  --initial-cluster-token=etcd-cluster-0 \               # 创建集群使用的token，一个集群内的节点保持一致
  --initial-cluster=etcd-10.0.0.206=https://10.0.0.206:2380,etcd-10.0.0.207=https://10.0.0.207:2380,etcd-10.0.0.208=https://10.0.0.208:2380 \                     # 集群所有的节点信息，节点间会进行健康性检测
  --initial-cluster-state=new \                # 新建集群的时候的值为new，如果是已经存在的集群为existing
  --data-dir=/var/lib/etcd \                   # 数据目录路径
  --wal-dir= \
  --snapshot-count=50000 \
  --auto-compaction-retention=1 \
  --auto-compaction-mode=periodic \
  --max-request-bytes=10485760 \
  --quota-backend-bytes=8589934592
Restart=always
RestartSec=15
LimitNOFILE=65536
OOMScoreAdjust=-999

[Install]
WantedBy=multi-user.target
```



### etcd选举

- etcd基于Raft算法进行集群角色选举，使用Raft的还有consul，InfluxDB，Kafka等
- [Raft协议详解](CloudNative-Kubernetes.md##Raft协议)



### etcd配置优化

```bash
# rquests size limit (请求的最大字节数，默认一个key最大1.5Mib，官方最大不要超过10Mib)
--max-request-bytes=10485760 

# storage size limit (磁盘存储空间大小限制，默认为2G，此值超过8G启动会有警告信息)
# 因为etcd存储的通常都是集群的元数据，因此占用磁盘大小不大，但是磁盘IO很高
--quota-backend-bytes=8589934592

# 集群碎片整理，时间长了可以做一下，提升性能
# 早期
ETCDCTL_API=3 /usr/local/bin/etcdctl defrag --cluster --endpoints=https://10.0.0.206:2379 --cacert=/etc/kubernetes/ssl/ca.pem --cert=/etc/kubernetes/ssl/etcd.pem --key=/etc/kubernetes/ssl/etcd-key.pem

# 现在基本都是使用v3，以前可能有使用v2的，因此需要声明v3，现在默认都是v3，所以不需要声明
[root@k8s-10-0-0-206 ~]#/usr/local/bin/etcdctl defrag --cluster --endpoints=https://10.0.0.206:2379 --cacert=/etc/kubernetes/ssl/ca.pem --cert=/etc/kubernetes/ssl/etcd.pem --key=/etc/kubernetes/ssl/etcd-key.pem
Finished defragmenting etcd member[https://10.0.0.207:2379]
Finished defragmenting etcd member[https://10.0.0.206:2379]
Finished defragmenting etcd member[https://10.0.0.208:2379]

```



### etcd操作

#### etcd成员列表

```bash
[root@k8s-10-0-0-206 ~]#export NODE_IPS="10.0.0.206 10.0.0.207 10.0.0.208"

[root@k8s-10-0-0-206 ~]#ETCDCTL_API=3 /usr/local/bin/etcdctl --write-out=table member list --endpoints=https://10.0.0.206:2379 --cacert=/etc/kubernetes/ssl/ca.pem --cert=/etc/kubernetes/ssl/etcd.pem --key=/etc/kubernetes/ssl/etcd-key.pem
+------------------+---------+-----------------+-------------------------+-------------------------+------------+
|        ID        | STATUS  |      NAME       |       PEER ADDRS        |      CLIENT ADDRS       | IS LEARNER |
+------------------+---------+-----------------+-------------------------+-------------------------+------------+
| 2323451019f6428d | started | etcd-10.0.0.207 | https://10.0.0.207:2380 | https://10.0.0.207:2379 |      false |
| 23d31ba59ca79fa0 | started | etcd-10.0.0.206 | https://10.0.0.206:2380 | https://10.0.0.206:2379 |      false |
| 7a42012c95def99e | started | etcd-10.0.0.208 | https://10.0.0.208:2380 | https://10.0.0.208:2379 |      false |
+------------------+---------+-----------------+-------------------------+-------------------------+------------+
```



#### etcd验证节点心跳状态

```bash
[root@k8s-10-0-0-207 ~]#for ip in ${NODE_IPS}; do ETCDCTL_API=3 /usr/local/bin/etcdctl --endpoints=https://${ip}:2379 --cacert=/etc/kubernetes/ssl/ca.pem --cert=/etc/kubernetes/ssl/etcd.pem --key=/etc/kubernetes/ssl/etcd-key.pem endpoint health; done
https://10.0.0.206:2379 is healthy: successfully committed proposal: took = 68.505353ms
https://10.0.0.207:2379 is healthy: successfully committed proposal: took = 101.925588ms
https://10.0.0.208:2379 is healthy: successfully committed proposal: took = 109.962263ms
```



#### etcd查看详细信息

```bash
[root@k8s-10-0-0-207 ~]#for ip in ${NODE_IPS}; do ETCDCTL_API=3 /usr/local/bin/etcdctl --write-out=table endpoint status --endpoints=https://${ip}:2379 --cacert=/etc/kubernetes/ssl/ca.pem --cert=/etc/kubernetes/ssl/etcd.pem --key=/etc/kubernetes/ssl/etcd-key.pem; done
+-------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|        ENDPOINT         |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+-------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
| https://10.0.0.206:2379 | 23d31ba59ca79fa0 |  3.5.12 |  2.2 MB |     false |      false |         4 |     144353 |             144353 |        |
+-------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
+-------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|        ENDPOINT         |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+-------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
| https://10.0.0.207:2379 | 2323451019f6428d |  3.5.12 |  2.2 MB |      true |      false |         4 |     144354 |             144354 |        |
+-------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
+-------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|        ENDPOINT         |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+-------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
| https://10.0.0.208:2379 | 7a42012c95def99e |  3.5.12 |  2.2 MB |     false |      false |         4 |     144354 |             144354 |        |
+-------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+

```



#### 查看etcd数据

```bash
# 以路径的方式所有key信息
ETCD_API=3 etcdctl get / --prefix --keys-only  

# 查看pod信息：
[root@k8s-10-0-0-207 ~]#ETCD_API=3 etcdctl get / --prefix --keys-only|grep pod
/calico/ipam/v2/handle/k8s-pod-network.bff6832b73978900eea1e2cb579bbd2efaee3e114030af52c8a68e27b879e7be
/calico/resources/v3/projectcalico.org/profiles/ksa.kube-system.horizontal-pod-autoscaler
/calico/resources/v3/projectcalico.org/profiles/ksa.kube-system.pod-garbage-collector
/registry/clusterrolebindings/system:controller:horizontal-pod-autoscaler
/registry/clusterrolebindings/system:controller:pod-garbage-collector
/registry/clusterroles/system:controller:horizontal-pod-autoscaler
/registry/clusterroles/system:controller:pod-garbage-collector
/registry/poddisruptionbudgets/kube-system/calico-kube-controllers
/registry/pods/kube-system/calico-kube-controllers-cdf8978d8-d2xmc
/registry/pods/kube-system/calico-node-57htk
/registry/pods/kube-system/calico-node-5hmhr
/registry/pods/kube-system/calico-node-79jxn
/registry/pods/kube-system/calico-node-gs4xt
/registry/pods/kube-system/calico-node-j25th
/registry/pods/kube-system/calico-node-slntd
/registry/pods/kube-system/coredns-55c868d7f5-d76zv
/registry/serviceaccounts/kube-system/horizontal-pod-autoscaler
/registry/serviceaccounts/kube-system/pod-garbage-collector

# namespace信息
[root@k8s-10-0-0-207 ~]#ETCD_API=3 etcdctl get / --prefix --keys-only|grep namespaces
/registry/namespaces/default
/registry/namespaces/kube-node-lease
/registry/namespaces/kube-public
/registry/namespaces/kube-system

# 查看deployment控制器信息
[root@k8s-10-0-0-207 ~]#ETCD_API=3 etcdctl get / --prefix --keys-only|grep deployment
/calico/resources/v3/projectcalico.org/profiles/ksa.kube-system.deployment-controller
/registry/clusterrolebindings/system:controller:deployment-controller
/registry/clusterroles/system:controller:deployment-controller
/registry/deployments/kube-system/calico-kube-controllers
/registry/deployments/kube-system/coredns
/registry/serviceaccounts/kube-system/deployment-controller

# 查看calico组件信息
[root@k8s-10-0-0-207 ~]#ETCD_API=3 etcdctl get / --prefix --keys-only|grep calico
/calico/ipam/v2/assignment/ipv4/block/10.200.129.0-26
/calico/ipam/v2/assignment/ipv4/block/10.200.171.0-26
/calico/ipam/v2/assignment/ipv4/block/10.200.184.64-26
/calico/ipam/v2/assignment/ipv4/block/10.200.222.0-26
/calico/ipam/v2/assignment/ipv4/block/10.200.37.192-26
/calico/ipam/v2/assignment/ipv4/block/10.200.49.0-26
/calico/ipam/v2/config
......

# 查看key的值，内容可能存在乱码，需要工具（auger）进行解码，将etcd编码的数据重新排列
# 下载
[root@k8s-10-0-0-207 ~]# wget https://github.com/etcd-io/auger/releases/download/v1.0.3/auger_1.0.3_linux_amd64.tar.gz
[root@k8s-10-0-0-206 ~]#tar xf auger_1.0.3_linux_amd64.tar.gz 
[root@k8s-10-0-0-206 ~]#mv auger augerctl /usr/local/bin

# 相当于kubectl get pod -n kube-system calico-node-57htk -o yaml
[root@k8s-10-0-0-206 ~]#etcdctl get /registry/pods/kube-system/calico-node-57htk|auger decode
```



#### etcd增删改查

```bash
# 添加数据
[root@k8s-10-0-0-206 ~]# etcdctl put /name "tom"
OK

# 查询数据
[root@k8s-10-0-0-206 ~]#etcdctl get /name
/name
tom

# 修改数据，重新put，将值覆盖掉
[root@k8s-10-0-0-206 ~]#etcdctl put /name curry
OK
[root@k8s-10-0-0-206 ~]#etcdctl get /name
/name
curry

# 删除数据
[root@k8s-10-0-0-206 ~]#etcdctl del /name
1
```



#### etcd数据watch机制

基于不断监看数据，发生变化就主动触发通知客户端，Etcd v3 的watch机制支持watch某个固定的key，也支持watch一个范围

```bash
# 在etcd1 上watch一个key，没有此key也可以执行watch，后期可以再创建
[root@k8s-10-0-0-206 ~]#etcdctl watch /data

# 在etcd2 修改数据，验证etcd1是否发生数据变化
[root@k8s-10-0-0-207 ~]#etcdctl put /data "data v1"
OK

# 观察etcd1
[root@k8s-10-0-0-206 ~]#etcdctl watch /data
PUT
/data
data v1

[root@k8s-10-0-0-207 ~]#etcdctl put /data "data v2"
OK

[root@k8s-10-0-0-206 ~]#etcdctl watch /data
PUT
/data
data v1
PUT
/data
data v2
```



#### Kubernetes 上 Watch机制示例

```bash
# kuber-scheduler会watch /registry/pods，/registry/nodes，/registry/bindings
# 在etcd1 watch /registry/pods
[root@k8s-10-0-0-206 ~]#etcdctl watch --prefix /registry/pods

# 创建一个pod
[root@master-01 pod]#kubectl apply -f myapp.yaml 
pod/alpine3 created

# 观察刚刚watch的路径
[root@k8s-10-0-0-206 ~]#etcdctl watch --prefix /registry/pods
PUT
/registry/pods/default/alpine3
k8s
......

# 删除刚刚创建的pod->alpine3
# 查看etcd的key
[root@k8s-10-0-0-207 ~]#etcdctl get / --prefix --keys-only |grep events
/registry/apiregistration.k8s.io/apiservices/v1.events.k8s.io
/registry/events/default/alpine3.1834a7d6ad5491c5
/registry/events/default/alpine3.1834a7d6ffc8fbb9
/registry/events/default/alpine3.1834a7d86aa93aa4
/registry/events/default/alpine3.1834a7d8788b8e49
/registry/events/default/alpine3.1834a7d88764f93d
/registry/events/default/alpine3.1834a7dbe6982b44
/registry/events/default/alpine3.1834a7eec882ed84
/registry/events/default/alpine3.1834a7ef13aa3e3e
/registry/events/default/alpine3.1834a7f05f0ef84e
/registry/events/default/alpine3.1834a7f0616b646a
/registry/events/default/alpine3.1834a7f06d7c3b22
/registry/events/default/alpine3.1834a7f0f67862de

# 为什么 /registry/events/default/alpine3.* 有这么多条目？
# 你创建 Pod alpine3 后，Kubernetes 控制平面（尤其是 kubelet 和 controller-manager）会对该 Pod 的生命周期过程不断记录事件，例如：Scheduled，Pulling image，Created container，Started container......
# 每条事件都会单独作为一个对象写入 etcd，路径就是：/registry/events/{namespace}/{pod-name}.{event-uuid}
# 所以会看到很多条/registry/events/default/alpine3.XXXXXXX

# 那我把 Pod 删除了，为什么这些事件还在？
# 事件资源（events.k8s.io）是 非绑定生命周期资源（non-owner reference），即使 Pod 被删除，事件并不会马上被清理掉。

# 事件的保留策略如下：
# 类型: CoreV1 Event   ---->  默认保留时间 ~1 小时左右（1h）
# 类型: Events.k8s.io/v1   ---->  默认也大约 1 小时，具体取决于 GC 策略

# 这些事件由 event 控制器定期清理，或者由组件（如 kube-controller-manager）后台垃圾回收。
# 你可以通过以下方式验证其 TTL：kubectl get events --all-namespaces --output=wide
# 你也可以 watch /registry/events 的变化，过一会它们会自动从 etcd 中清除。

# kube-proxy会 watch /registry/services/specs/
# 如果想要观察到这个路径下的变化要关掉所有节点上的kube-proxy，否则刚删除数据变化，就会被kube-proxy消费掉
```



### etcd-v3-API版本数据备份与恢复

**WAL**是write ahead log（预写日志）的缩写，顾名思义，也就是在执行真正的写操作之前先写一个日志，预写日志（详情可以看补充：raft协议详解）

**WAL**：存放预写式日志，最大的作用是记录了整个数据变化的全部历程。在etcd中，所有数据的修改在提交前，都要先写入到WAL中。



#### V3版本备份数据

```bash
ETCDCTL_API=3 etcdctl snapshot save snapshot.db

# 示例
[root@k8s-10-0-0-206 ~]#etcdctl snapshot save /tmp/etcd.db
{"level":"info","ts":"2025-04-09T21:43:15.766559+0800","caller":"snapshot/v3_snapshot.go:65","msg":"created temporary db file","path":"/tmp/etcd.db.part"}
{"level":"info","ts":"2025-04-09T21:43:15.776496+0800","logger":"client","caller":"v3@v3.5.12/maintenance.go:212","msg":"opened snapshot stream; downloading"}
{"level":"info","ts":"2025-04-09T21:43:15.776865+0800","caller":"snapshot/v3_snapshot.go:73","msg":"fetching snapshot","endpoint":"127.0.0.1:2379"}
{"level":"info","ts":"2025-04-09T21:43:15.998158+0800","logger":"client","caller":"v3@v3.5.12/maintenance.go:220","msg":"completed snapshot read; closing"}
{"level":"info","ts":"2025-04-09T21:43:16.006574+0800","caller":"snapshot/v3_snapshot.go:88","msg":"fetched snapshot","endpoint":"127.0.0.1:2379","size":"2.3 MB","took":"now"}
{"level":"info","ts":"2025-04-09T21:43:16.007478+0800","caller":"snapshot/v3_snapshot.go:97","msg":"saved","path":"/tmp/etcd.db"}
Snapshot saved at /tmp/etcd.db

# 查看
[root@k8s-10-0-0-206 ~]#ls /tmp/
etcd.db

# 如果后期etcd集群数据损坏，可以使用这个etcd.db，将数据恢复
```



#### V3版本恢复数据

```bash
# 将数据恢复到一个新的不存在的目录中，单机恢复
# 恢复数据指定的数据目录必须是新的
ETCDCTL_API=3 etcdctl snapshot restore snapshot.db --data-dir=/opt/etcd-testdir

# 实际生产中数据恢复
# 注意：集群恢复必须加下面的参数，否则恢复的是单机状态！！！
ETCDCTL_API=3 /usr/local/bin/etcdctl snapshot restore snapshot.db \
--name etcd-{{ inventory_hostname }} \    # 这里必须加etcd的name，下面的参数可以通过etcd.service查看
--initial-cluster {{ ETCD_NODES }} \
--initial-cluster-token etcd-cluster-0 \
--initial-advertise-peer-urls https://{{ inventory_hostname }}:2380

# 恢复数据至etcd数据目录
cp -rf /etc/_backup/etcd-{{ inventory_hostnamme }}.etcd/member {{ ETCD_DATA_DIR }}/

# 重启etcd数据目录
systemctl restart etcd.service
```



#### 自动备份数据

```bash
[root@k8s-10-0-0-206 ~]# mkdir /data/etcd-backup-dir/ -p
[root@k8s-10-0-0-206 ~]# cat etcd-backup.sh
#!/bin/bash
source /etc/profile
DATE=`data +%Y-%m-%d_%H-%M-%S`
ETCDCTL_API=3 /usr/local/bin/etcdctl snapshot save /data/etcd-backup-dir/etcd-snapshot-${DATE}.db
```



#### 使用kubeasz备份恢复集群数据

```bash
# ./ezctl backup <集群名>
[root@haproxy1 ~]#./ezctl backup k8s-cluster1

# 查看备份的数据
[root@haproxy1 kubeasz]#ls clusters/k8s-cluster1/backup/
snapshot_202504092210.db  snapshot.db

# 恢复指定版本/日期的备份文件
# 方法1：修改ansible
[root@haproxy1 kubeasz]# vim ./roles/cluster-restore/defaults/main.yaml
# 指定需要恢复的 etcd 数据备份，默认使用最近的一次备份
# 在ansible 控制端查看备份目录：/etc/kubeasz/clusters/_cluster_name_/backup
db_to_restore: "snapshot.db"    # 改这里

# 方法2：将指定版本/日期备份文件覆盖snapshot.db
[root@haproxy1 kubeasz]# cd  clusters/k8s-cluster1/backup/ && cp snapshot_XXXX.db snapshot.db

# 恢复数据
# 恢复数据的时候，会关闭master上的apiserver禁止写入
[root@haproxy1 kubeasz]# ./ezctl restore k8s-cluster1

# 注意！！！：执行恢复前查看
[root@haproxy1 kubeasz]#cat roles/cluster-restore/tasks/main.yml 
- name: 停止ectd 服务
  service: name=etcd state=stopped

- name: 清除etcd 数据目录
  file: name={{ ETCD_DATA_DIR }}/member state=absent

- name: 清理上次备份恢复数据
  file: name=/etcd_backup state=absent

- name: 生成备份目录
  file: name=/etcd_backup state=directory

- name: 准备指定的备份etcd 数据
  copy:
    src: "{{ cluster_dir }}/backup/{{ db_to_restore }}"
    dest: "/etcd_backup/snapshot.db"

- name: etcd 数据恢复
  shell: "cd /etcd_backup && \
	ETCDCTL_API=3 {{ bin_dir }}/etcdctl snapshot restore snapshot.db \   # 下面必须加参数，否则会出现bug
	--name etcd-{{ inventory_hostname }} \
	--initial-cluster {{ ETCD_NODES }} \
	--initial-cluster-token etcd-cluster-0 \
	--initial-advertise-peer-urls https://{{ inventory_hostname }}:2380"

- name: 恢复数据至etcd 数据目录
  shell: "cp -rf /etcd_backup/etcd-{{ inventory_hostname }}.etcd/member {{ ETCD_DATA_DIR }}/"

- name: 重启etcd 服务
  service: name=etcd state=restarted

- name: 以轮询的方式等待服务同步完成
  shell: "systemctl is-active etcd.service"
  register: etcd_status
  until: '"active" in etcd_status.stdout'
  retries: 8
  delay: 8
```



#### ETCD数据恢复流程

当etcd集群宕机数量超过集群总节点一半以上的时候（如总数为三台宕机两台），就会导致整个集群宕机，后期需要恢复数据

- 恢复服务器系统
- 重新部署ETCD集群
- 停止kube-apisever/controller-manager/scheduler/kubelet/kube-proxy
- 停止ETCD集群
- 各ETCD节点恢复同一份备份数据
- 启动各节点并验证ETCD集群
- 启动kube-apisever/controller-manager/scheduler/kubelet/kube-proxy
- 验证k8s master状态及pod数据



### ETCD集群节点添加与删除

- add-etcd
- del-etcd