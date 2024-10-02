# Elasticsearch部署和管理
## Elasticsearch安装前准备
### 安装前环境初始化
```shell
CPU 2C
内存 4G以上
操作系统 Linux主流版本
系统盘 50G
主机名设置规则：nodeX.feng.org
生产环境建议准备单独的数据磁盘（比如Minio）
```

### 主机名
```shell
# 各服务器配置自己的主机名
hostnamectl set-hostname es-node1.wang.org
```

### 关闭防火墙和SELinux
```shell
systemctl disable firewalld
systemctl disable NetworkManager
sed -i '/SELINUX/s/enforcing/disabled/' /etc/selinux/config
reboot
```

### 服务器配置本地域名解析(集群)
```shell
vim /etc/hosts
10.0.0.121 es-node1.feng.org
10.0.0.122 es-node2.feng.org
10.0.0.123 es-node3.feng.org
```

### 优化资源限制配置
#### 修改内核参数
内核参数`vm.max_map_count`用于限制一个进程可以拥有的VMA(虚拟内存区域)的数量
```shell
# 查看默认值
sysctl -a | grep vm.max_map_count
# 输出结果：vm.max_map_count = 65530

# 修改配置
echo "vm.max_map_count = 262144" >> /etc/sysctl.conf

# 设置系统最大打开的文件描述符
fs.file-max = 9223372036854775807 （Ubuntu2204默认值）
fs.file-max=XXXX(默认已满足要求)
```

### 安装Java环境（可选）
- 7.X以前需要自行安装Java
- 7.X版本分带JDK和不带JDK两种
- 8.X版本内置Java，不再支持自行安装的JDK

## 单机版ES安装
### 包安装
```shell
# 下载deb包或者rpm包
# 在官方或者国内源
wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/e/elasticsearch/elasticsearch-8.15.0-amd64.deb

# 安装
dpkg -i elasticsearch-8.15.0-amd64.deb
```
### 安全验证
8版本有安全验证，无法直接访问
```shell
--------------------------- Security autoconfiguration information ------------------------------

Authentication and authorization are enabled.
TLS for the transport and HTTP layers is enabled and configured.
# 服务启动后，必须使用这个密码才能访问
The generated password for the elastic built-in superuser is : zQWBLf_oPTQTVUE52Iam

If this node should join an existing cluster, you can reconfigure this with
'/usr/share/elasticsearch/bin/elasticsearch-reconfigure-node --enrollment-token <token-here>'
after creating an enrollment token on your existing cluster.

You can complete the following actions at any time:

Reset the password of the elastic built-in superuser with 
'/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic'.

Generate an enrollment token for Kibana instances with 
 '/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana'.

Generate an enrollment token for Elasticsearch nodes with 
'/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node'.

-------------------------------------------------------------------------------------------------
### NOT starting on installation, please execute the following statements to configure elasticsearch service to start automatically using systemd
 sudo systemctl daemon-reload
 sudo systemctl enable elasticsearch.service
### You can start elasticsearch service by executing
 sudo systemctl start elasticsearch.service
```

### 启动Elasticsearch
```shell
systemctl enable --now elasticsearch

# elasticsearch中内置的java包安装路径
[root@ubuntu2204 ~]#/usr/share/elasticsearch/jdk/bin/java --version
openjdk 22.0.1 2024-04-16
OpenJDK Runtime Environment (build 22.0.1+8-16)
OpenJDK 64-Bit Server VM (build 22.0.1+8-16, mixed mode, sharing)
```

### 直接运行Elasticsearch报错
```shell
# 直接访问报错，缺少证书
[root@ubuntu2204 ~]#curl https://10.0.0.121:9200
curl: (60) SSL certificate problem: self-signed certificate in certificate chain
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.

# 忽略证书也不行，401报错，需要认证
# 8.X版本特性
[root@ubuntu2204 ~]#curl https://10.0.0.121:9200 -k
{"error":{"root_cause":[{"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":["Basic realm=\"security\", charset=\"UTF-8\"","Bearer realm=\"security\"","ApiKey"]}}],"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":["Basic realm=\"security\", charset=\"UTF-8\"","Bearer realm=\"security\"","ApiKey"]}},"status":401}
```

### 使用安装服务后生成的密码进行认证访问
```shell
[root@ubuntu2204 ~]#ES_PASSWD=zQWBLf_oPTQTVUE52Iam
# 访问成功
[root@ubuntu2204 ~]#curl -k -u "elastic:$ES_PASSWD" https://10.0.0.121:9200 -I 
HTTP/1.1 200 OK
X-elastic-product: Elasticsearch
content-type: application/json
content-length: 544

[root@ubuntu2204 ~]#curl -k -u "elastic:$ES_PASSWD" https://10.0.0.121:9200 
{
  "name" : "ubuntu2204.wang.org",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "FjrTC6U0TqS97R8CMAhtNQ",
  "version" : {
    "number" : "8.15.0",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "1a77947f34deddb41af25e6f0ddb8e830159c179",
    "build_date" : "2024-08-05T10:05:34.233336849Z",
    "build_snapshot" : false,
    "lucene_version" : "9.11.1",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

#### 如果image忘记，重置生成新密码
```shell
# 方法1：生成随机密码
/usr/share/elasticsearch/bin/elasticsearch password -u elastic

# 方法2：生成指定密码
/usr/share/elasticsearch/bin/elasticsearch-reset-password --username elastic -i
```

#### 该安全加固会对后续的产生影响
- 在实际生产中，Elasticsearch会不可避免的和各种其他服务进行通信，这个过程中该认证会产生很多麻烦，所以在内网安全可到保证的情况下，建议把该安全加固取消


### 取消安全认证
```shell
# 更改配置文件
vim /etc/elasticsearch/elasticsearch.yml

# 建议更改存放数据和日志的目录到单独的磁盘逻辑卷
# 使用逻辑卷方便以后扩容
path.data: /es/data
path.logs: /es/log

# 将xpack启用关闭
xpack.security.enabled: false

# 修改jvm.options文件
vim /etc/elasticsearch/jvm.options
# 调整JVM heap size
-Xms512m
-Xms512m

# 后续优化es的启动，垃圾回收等也是在这里进行优化
# 直接访问
[root@ubuntu2204 ~]#curl 10.0.0.121:9200
{
  "name" : "ubuntu2204.wang.org",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "pcqcKf6YQ2yDJlxpmIrhNA",
  "version" : {
    "number" : "8.15.0",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "1a77947f34deddb41af25e6f0ddb8e830159c179",
    "build_date" : "2024-08-05T10:05:34.233336849Z",
    "build_snapshot" : false,
    "lucene_version" : "9.11.1",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

### 使用RESTFUL API对其进行访问
```shell
[root@ubuntu2204 ~]#curl 10.0.0.121:9200/_cat?
=^.^=
/_cat/allocation
/_cat/shards
/_cat/shards/{index}
/_cat/master
/_cat/nodes
/_cat/tasks
/_cat/indices
/_cat/indices/{index}
/_cat/segments
/_cat/segments/{index}
/_cat/count
/_cat/count/{index}
/_cat/recovery
/_cat/recovery/{index}
/_cat/health
/_cat/pending_tasks
/_cat/aliases
/_cat/aliases/{alias}
/_cat/thread_pool
/_cat/thread_pool/{thread_pools}
/_cat/plugins
/_cat/fielddata
/_cat/fielddata/{fields}
/_cat/nodeattrs
/_cat/repositories
/_cat/snapshots/{repository}
/_cat/templates
/_cat/component_templates/_cat/ml/anomaly_detectors
/_cat/ml/anomaly_detectors/{job_id}
/_cat/ml/datafeeds
/_cat/ml/datafeeds/{datafeed_id}
/_cat/ml/trained_models
/_cat/ml/trained_models/{model_id}
/_cat/ml/data_frame/analytics
/_cat/ml/data_frame/analytics/{id}
/_cat/transforms
/_cat/transforms/{transform_id}
```

#### 查看健康性health
```shell
curl 10.0.0.121:9200/_cat/health
1723534586 07:36:26 elasticsearch green 1 1 0 0 0 0 0 0 - 100.0%
```

## Elasticsearch插件
### elasticsearch-head
```shell
# 该插件以被谷歌下架，所以放到了自己的网站上
https://www.mysticalrecluse.com/script/tools/ElasticSearch-Head-0.1.5_0.zip
```

### es-client
- 可以在微软或谷歌商店下载

### cerebro
```shell
# 需要java环境，要先安装java
apt update && openjdk-11-jdk

# 下载cerebro
https://github.com/lmenezes/cerebro/releases
https://github.com/lmenezes/cerebro/releases/download/v0.9.4/cerebro_0.9.4_all.deb

# 更改配置文件，指定有权限的数据库地址
# Path of local database file
data.path: "/var/lib/cerebro/cerebro.db"
#data.path = "./cerebro.db"

# 启动cerebro.service
systemctl start cerebro

# 用浏览器打开(默认9000端口)
10.0.0.132:9000
# 并连接：http://10.0.0.121:9200
```


### 二进制安装
#### 下载二进制包
```shell
# 官网下载
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.15.0-linux-x86_64.tar.gz

# 解压缩到指定目录
tar xf elasticsearch-8.15.0-linux-x86_64.tar.gz -C /usr/local/

# 创建软连接
ln -s /usr/local/elasticsearch-8.15.0/ /usr/local/elasticsearch
```

#### 编辑服务配置文件
```shell
# 创建数据目录
mkdir -pv /es/{data,log}
# 修改配置文件，比如关闭xpath,更改数据，日志路径
vim /usr/local/elasticsearch/config/elasticsearch.yml

# 建议更改存放数据和日志的目录到单独的磁盘逻辑卷
# 使用逻辑卷方便以后扩容
path.data: /es/data
path.logs: /es/log

# 更改ELK内存配置
# vim /usr/local/elasticsearch/jvm.options
-Xms2g
-Xmx2g
```

#### 创建用户
```shell
# 从ES7.X以后不允许以root启动服务，需要创建专用的用户
在所有节点上创建用户
useradd -r elasticsearch
```

#### 目录权限更改
```shell
# 在所有节点上创建数据和目录并修改目录权限为elasticsearch
chown -R elasticsearch.elasticsearch /es

# 修改elasticsearch的安装目录权限
chown -R elasticsearch.elasticsearch /usr/local/elasticsearch/

# 启动后才会出现xpack的选项，将其改为false再重启
vim /usr/local/elasticsearch/config/elasticsearch.yml
```

#### 启动Elasticsearch
```shell
echo 'PATH=/usr/local/elasticsearch/bin:$PATH' > /etc/profile.d/elasticsearch.sh
``` 

#### 创建service文件
```shell
cat /lib/systemd/system/elasticsearch.service
[Unit]
Description=Elasticsearch
Documentation=http://www.elastic.co
Wants=network-online.target
After=nework-online.target

[Service]
RuntimeDirectory=elasticsearch
PrivateTmp=true
Environment=PID_DIR=/var/run/elasticsearch

WorkingDirectory=/usr/local/elasticsearch

User=elasticsearch
Group=elasticsearch

ExecStart=/usr/local/elasticsearch/bin/elasticsearch -p ${PID_DIR}/elasticsearch.pid --quiet

LimitNOFILE=65535
LimitNPROC=4096

TimeoutStopSec=0
KillMode=process
KillSignal=SIGTERM
SendSIGKILL=no
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target
```

## 集群部署
```shell
# 修改每个主机的hostname
hostnamectl set-hostname es-node1
hostnamectl set-hostname es-node2
hostnamectl set-hostname es-node3

# 修改堆内存
# 理论上java程序的堆内存建议设置成程序的一半，但是建议不要超过30G
# 超过30G反而可能影响性能
vim /usr/local/elasticsearch/jvm.options
-Xms2g
-Xmx2g
```

### 性能提升
```shell
vim /usr/local/elasticsearch/elasticsearch.yml

# 内存优化
bootstrap.memroy_lock: true   #将内存空间给程序预留好，不需要临时申请内存
# 开启此功能8.X，集群模式可能无法启动，但是单机模式可以启动
# 存在缺点：如果强制预留空间，但是机器的内存空间不够，会导致服务无法启动，为了解决这个问题，可以在service文件增加参数
# 方法1：直接修改elasticsearch.service
[Service]
LimitMEMLOCK=infinity

systemctl daemon-reload

# 方法2：新建文件
systemctl edit elasticsearch
### Anything between here and the comment below will become the new contents of the file
# 加下面两行，注意加载中间的位置
[Service]
LimitMEMLOCK=infinity
```

### 修改集群配置
```shell
# vim /usr/local/elasticsearch/config/elasticsearch.yml
# 同一集群内的Clustername名称要一致
# Use a descriptive name for your cluster:

cluster.name: my-application

# 写上自己的node名
node.name: node-1

# 集群模式下，开放9300端口，实现集群间的相互通信
# address here to expose this node on the network:
#
network.host: 0.0.0.0

# 添加集群内节点
# --------------------------------- Discovery ----------------------------------
#
# Pass an initial list of hosts to perform discovery when this node is started:
# The default list of hosts is ["127.0.0.1", "[::1]"]
#
discovery.seed_hosts: ["10.0.0.121", "10.0.0.122", "10.0.0.123"]

# 选择参与选举的节点
# Bootstrap the cluster using an initial set of master-eligible nodes:
#
cluster.initial_master_nodes: ["10.0.0.121", "10.0.0.122", "10.0.0.123"]

# 最下面也有一个选择参与节点的选项，将其注释掉，防止和之前的冲突

#cluster.initial_master_nodes: ["ubuntu2204.wang.org"]

```

## Elasticsearch 访问
Elasticsearch支持各种语言使用RESTful API通过端口9200与之进行通信
可以用三种方式和Elasticsearch进行交互
- curl命令和其他浏览器：基于命令行，操作不方便
- 插件：在node节点上安装head, Celebro等插件，实现图形操作，查看数据方便
- Kibnan：需要java环境并配置图形操作，显示格式丰富

### 使用curl访问
#### 查看集群状态
```shell
# 查看集群节点
[root@es-node2 config]#curl 10.0.0.121:9200/_cat/nodes
10.0.0.121 57 96 0 0.00 0.00 0.00 cdfhilmrstw * node-1
10.0.0.123 63 97 0 0.00 0.00 0.00 cdfhilmrstw - node-3
10.0.0.122 31 97 0 0.00 0.01 0.00 cdfhilmrstw - node-2

# 查看集群健康性
[root@es-node2 config]#curl 10.0.0.121:9200/_cat/health
1723792483 07:14:43 my-application green 3 3 0 0 0 0 0 0 - 100.0%
```

#### 创建和查看索引
```shell
# 创建索引index1，简单输出
[root@es-node2 config]#curl -XPUT '10.0.0.121:9200/index1'
{"acknowledged":true,"shards_acknowledged":true,"index":"index1"}

# 默认有1个副本，加上主切片，则共两个
# 如果将10.0.0.121上面的服务关闭,只剩一个切片(副本)，则健康性变黄色

# 过一段时间，自动在node3上同步一个副本，保证副本数量，则健康性再次变为绿色
[root@es-node1 config]#curl 10.0.0.122:9200/_cat/health
1723793050 07:24:10 my-application green 2 2 2 1 0 0 0 0 - 100.0%
```
#### 创建索引
```shell
# 创建副本的时候指定副本数和分片数
# 下面数量：3个分片，3个副本
curl -XPUT '10.0.0.121:9200/index2' -H 'Content-Type: application/json' -d '
{
    "settings": {
        "index": {
            "number_of_shards": 3, 
            "number_of_replicas": 2
        }
    }
}'
{"acknowledged":true,"shards_acknowledged":true,"index":"index2"}

# 查看分片在不同节点的分布
[root@es-node1 data]#curl 10.0.0.121:9200/_cat/indices
green open index2 XwSLR-0FSEyZcT4mXjH3yg 3 2 0 0 2.1kb 747b 747b
green open index1 dOPGBm9XSQuLMbdLiDvnQg 1 1 0 0  498b 249b 249b
```

#### 健康状态总结
- 绿色：表示完全健康
- 黄色：数据还在，副本数量缺失
- 红色：数据缺失

#### 插入文档
```shell
# 创建文档时不指定_id，会自动生成
# 8.x版本后因为删除了type，所以索引操作：{index}/{type}/需要修改成PUT {index}/_doc/
# index1是索引数据库，book是type

# 7.x版本之前
curl -XPOST http://127.0.0.1:9200/index1/book/ -H 'Content-Type: application/json' -d '{"name":"linux", "author":"wangxiaochun","version":"1.0"}'

# 8.x版本之后
curl -XPOST http://10.0.0.121:9200/index1/_doc/ -H 'Content-Type: application/json' -d '{"name":"linux", "author":"zhangyifeng", "version":"1.0"}'
{"_index":"index1","_id":"k8QsWpEBTrkwRwkc1TwS","_version":1,"result":"created","_shards":{"total":2,"successful":2,"failed":0},"_seq_no":0,"_primary_term":1}
```
- 插入文档时，指定_id
```shell
[root@es-node1 data]#curl -XPOST 'http://10.0.0.121:9200/index1/_doc/1?pretty' -H 'Content-Type: application/json' -d '{"name":"golang", "author":"yanbingcheng", "version":"1.0"}'
{
  "_index" : "index1",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "_seq_no" : 2,
  "_primary_term" : 1
}
```

#### 查询文档
```shell
# 查询索引中的所有文档
curl 'http://10.0.0.121:9200/index1/_search?pretty'
```

#### 删除文档
```shell
# 8.x版本
curl -XDELETE 'http://10.0.0.121:9200/<索引名称>/_doc/<文档id>'

# 7.x版本之前
curl -XDELETE 'http://10.0.0.121:9200/<索引名称>/type/<文档id>'
```

#### 删除索引
```shell
curl -XDELETE 'http://10.0.0.121:9200/index2'

# 查看索引是否删除
curl 'http://10.0.0.121:9200/_cat/indices?pretty'
#green open index2 XwSLR-0FSEyZcT4mXjH3yg 3 2 0 0  2.1kb   747b   747b
#green open index1 dOPGBm9XSQuLMbdLiDvnQg 1 1 2 1 35.3kb 15.1kb 15.1kb

# 删除多个索引
curl -XDELETE 'http://10.0.0.121:9200/index_one,index_two'

# 使用通配符删除多个索引，
# 需要设置action.destructive_require_name:false
curl -XDELETE 'http://10.0.0.121:9200/index_*'
```


## Elasticsearch集群工作原理
### ES节点分类
Elasticsearch集群的每个节点的角色有所不同，但都会保存集群状态`Cluster State`的相关的数据信息
- 节点信息：每个节点名称和地址
- 索引信息：所有索引的名称，配置等

#### Master节点
- ES集群只有一个Mster节点，用于控制和管理整个集群的操作
- Master节点负责增删索引，增删节点，分片shared的重新分配
- `Cluster State`主要由Master节点维护，主要包括
  - 节点名称
  - 节点连接地址
  - 索引名称
  - 配置信息等
- Master接收集群状态的变化，并推送给所有其他节点，集群中各节点都有一份完整的集群状态信息，都有master node负责维护
- 当Cluster State有新数据产生后，Master会将数据同步给其他Node节点
- Master节点通过超过一半的节点投票选举产生的
- 可以设置`node.master:true`指定为后续是否参与Master节点选举，默认true

#### Data节点
- 存储数据的节点即为data节点
- 当创建索引后，索引的数据会存储至某个数据节点
- Data节点消耗内存和磁盘IO的性能比较大
- 配置`node.data:true`就是Data节点，默认为true，即默认所有节点都是Data节点类型

#### Coordinating节点（调节）
- 处理请求的节点，即为coordinating节点，该节点类型为所有节点的默认角色，不能取消
- coordinating节点主要讲请求路由到正确的节点护理，比如创建索引的请求会由coordinating路由到master节点处理
- 当配置`node.master:false、node.data:false`则只充当Coordinating节点
- Coordinating节点在Cerrebro等插件中数据页面不会显示

#### Master-eligible（初始化时参与选举）
- 初始化时有资格选举Master的节点
- 只在集群第一次初始化时进行设置有效，后续配置无效
- 由cluster.initial_master_nodes配置节点地址


### ES集群选举
- ES集群的选举是由master-eligible（有资格充当的master节点）发起
- 选举时，优先选举`ClusterStateVersion`最大的Node节点
- 如果`ClusterStateVersion`相同，则选举Node ID最小的Node


### ES集群分片Shard和副本Replication
#### 分片
实现负载均衡

#### 副本
实现高可用

#### 默认分片配置
默认情况下，Elasticsearch将分片相关的配置从配置文件中的属性移除了，可以借助于一个默认的模版接口将索引的分片属性更改成我们想要的分片效果
```shell
# 配置5分片和1副本
curl -XPUT 'http://10.0.0.121:9200/_template/template_http_request' -H 'Content-Type: application/json' -d {"index_patterns":["*"], "settings": {"number_of_shards": 5, "number_of_replicas": 1}}'
```

#### 数据同步机制
Elasticsearch主要依赖Zen Discovery协议来管理集群中节点的加入和离开，以及选举主节点(master node)。
Zen Discovery是Elasticsearch自带一个协议，不依赖于任何外部服务。

#### 集群故障转移


## ES文档路由
### ES文档路由原理
ES文档是分布式存储，当在ES集群访问或存储一个文件时，由下面的算法决定此文档到底存放在哪个主分片中，再结合集群状态找到存放此主分片的节点主机

```shell
shard = hash(routing) % number_of_primary_shards
hash                      # 哈希算法可以保证将数据均匀分散在分片中
routing                   # 用于指定hash计算的一个可变参数，默认是文档id，也可以自定义
number_of_primary_shards  # 主分片数

# 注意：该算法与主分片数相关，一旦确定后便不能更改主分片，因为主分片的变化会导致所有分片需要重新分配
```
- 可以发送请求到集群中的任一节点，每个节点都知道集群中任意文档的位置，每个节点都有能力接收请求，再将请求转发到真正存储数据的节点上

### ES文档创建删除流程
- 客户端向集群中某个节点Node1发送新建索引文档或者删除索引文档请求
- Node1节点使用文档的_id，通过上面的算法确定文档属于分片0
- 因为分片0的主分片目前被分配在Node3上面，请求会被转发到Node3
- Node3在主分片上面执行创建或删除请求
- Node3执行如果成功，它将请求并行转发到Node1和Node2的副本分片上
- Node3将向协调节点Node1报告成功
- 协调节点Node1客户端报告成功


### ES文档读取流程
- 客户端向集群中某一节点Node1发送读取请求
- 节点使用文档的_id来确定文档属于分片0。分片0的主副本分片存在于所有的三个节点上
- 在处理读取请求时，协调节点在每次请求的时候都会通过轮询所有的主副本分片来达到负载均衡，此次它将请求转发到Node2
- Node2将文档返回给Node1，然后将文档返回给客户端

### Elasticsearch集群扩容和缩容
#### 集群扩容
新加入两个节点node4和node5，变为Data节点
在两个新节点安装ES，并配置文件如下
```shell
vim /etc/elasticsearch/elasticsearch.yml
cluster.name: ELK-Cluster # 和原集群名称相同  

# 当前节点在集群内的集群名称，同一集群中每个节点要确保此名称唯一
node.name: es-node4 # 第二个新节点为es-node5

# 集群监听端口对应的IP，默认是127.0.0.1:9300
network.host:0.0.0.0

# 指定任意集群节点即可
discovery.seed_hosts: ["10.0.0.121", "10.0.0.122", "10.0.0.123"]

# 集群初始化时指定希望哪些节点可以被选举为master，只在初始化时使用，新加节点到已有集群时此项可不配置
# cluster.initial_master_nodes: ["10.0.0.101","10.0.0.102","10.0.0.103"]
# cluster.initial_master_nodes: ["ubuntu2204.wang.org"]

# 如果不参与主节点选举设为false，默认值为true
node.master: false

# 存储数据，默认值为true，此值为false则不存储数据而成为一个路由节点
# 如果将原有的true改为false，需要先执行/usr/share/elasticsearch/bin/elasticsearch-node repurpose 清理数据
node.data:true
systemctl restart elasticsearch
```

#### 集群缩容
从集群中删除两个节点node4和node5，在两个节点按一定的顺序逐个停止服务，即可自动退出集群
注意：停止服务前，要观察索引的情况，按一定顺序关机，防止数据丢失
```shell
systemctl stop elasticsearch
```

# Beats收集数据
## 利用Filebeat收集数据
Filebeat是用于转发和集中日志数据的轻量级传送程序。作为服务器上的代理安装，Filebeat监视您指定的日志文件或位置，收集日志文件或位置，收集日志事件，并将它们转发到Elasticsearch或logstash进行索引

生产中收集数据一般使用Filebeat，Filebeat基于go开发，部署方便，重要的是只需要10M多内存，比较节约资源

Filebeat支持从日志文件，Syslog,Redis,Docker,TCP,UDP,标准输入等读取数据，对数据做简单处理，再输出至Elasticsearch，logstash,Redis,Kafka等

### filebeat工作方式
- 启动filebeat时，它将启动一个或多个输入源，这些输入源将在为日志数据指定的位置中查找
- 对于FIlebeat所找到的每个日志，FIlebeat都会启动收集器`harvester`进程
- 每个收集器harvester都读取一个日志以获取新内容，并将新日志数据发送到`libbeat`
- libbeat会汇总事件并将汇总的数据发送到FIlebeat配置的输出

```
注意：FIlebeat支持多个输入，但不支持同时有多个输出，如果多输出，会报错如下
```

### filebeat安装和配置
```shell
# 下载deb安装包
wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/apt/8.x/pool/main/f/filebeat/filebeat-8.15.0-amd64.deb

# 安装
dpkg -i filebeat-8.15.0-amd64.deb

# 安装后的二进制文件路径
/usr/share/filebeat/bin/filebeat

# filebeat命令，使用-c制定读取的配置文件路径

# -e将日志信息发送到标准错误（直接在文件打印），禁止输出到文件
```

### 从标准输入读取-输出至标准输出
```yaml
filebeat.inputs:
- type: stdin
  enabled: true
  # tags: ["stdin-tags","myapp"] #添加新字段名tags,可用于判断不同类型的输入，实现不同的输出
  fields:
    status_code: "200"
    author: "Zhangyifeng"

output.console:
  pretty: true
  enable: true
```
- 语法检查，注意：`stdin.yaml`的相对路径是相对于/etc/filebeat的，丼，而不是当前路径
```shell
[root@ubuntu2204 filebeat]#filebeat test config -c stdin.yml
Config OK
```

#### 执行读取
解析文本，不能解析json格式文本
```shell
# 从指定文件中读取配置
# -e表示Log to stderr and disable syslog/file output
filebeat -e -c /etc/filebeat/stdin.yml

# 输入json格式的数据
{"name":"Zhangyifeng","age":"18"}
# 生成如下数据
{
  "@timestamp": "2024-08-17T09:45:04.413Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "_doc",
    "version": "8.15.0"
  },
  "log": {
    "file": {
      "path": ""
    },
    "offset": 0
  },
  "message": "{\"name\":\"Zhangyifeng\",\"age\":\"18\"}",
  "input": {
    "type": "stdin"
  },
  "fields": {
    "author": "Zhangyifeng",
    "status_code": "200"
  },
  "ecs": {
    "version": "8.0.0"
  },
  "host": {
    "name": "ubuntu2204.wang.org"
  },
  "agent": {
    "ephemeral_id": "7eb051ab-63d9-4703-996b-c51e0465df2c",
    "id": "c5789874-a476-450b-a8c0-c2d55bdd95aa",
    "name": "ubuntu2204.wang.org",
    "type": "filebeat",
    "version": "8.15.0"
  }
}

# 按照上面stdin.yaml的配置运行，即使发送json格式的数据，filebeat也不会解析json
```
- 使`stdin.yml`配置能够解析json
```yaml
filebeat.inputs:
- type: stdin
  json.keys_under_root: true  #解析json
  enabled: true
  # tags: ["stdin-tags","myapp"] #添加新字段名tags,可用于判断不同类型的输入，实现不同的输出
  fields:
    status_code: "200"
    author: "Zhangyifeng"

output.console:
  pretty: true
  enable: true
```
- 在终端标准输入json数据
```shell
# 输入 {"name":"Zhangyifeng","age":"18"}
#
{
  "@timestamp": "2024-08-17T09:50:55.435Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "_doc",
    "version": "8.15.0"
  },
  "name": "Zhangyifeng",
  "input": {
    "type": "stdin"
  },
  "fields": {
    "author": "Zhangyifeng",
    "status_code": "200"
  },
  "ecs": {
    "version": "8.0.0"
  },
  "host": {
    "name": "ubuntu2204.wang.org"
  },
  "agent": {
    "version": "8.15.0",
    "ephemeral_id": "c2c9bc3b-e0a2-4c02-a01d-b5d801f04504",
    "id": "c5789874-a476-450b-a8c0-c2d55bdd95aa",
    "name": "ubuntu2204.wang.org",
    "type": "filebeat"
  },
  "log": {
    "offset": 0,
    "file": {
      "path": ""
    }
  },
  "age": "18"
}
```
### 将采集的信息输出到文件中
```yaml
# vim /etc/filbeate/stdfile.yml
filebeat.inputs:
- type: stdin
  enabled: true
  json.key_under_root: true
output.file:
  path: "/tmp"
  filename: "filebeat.log"
```

### 从文件读取在输出至标准输出
filebeat会将每个文件的读取数据的相关记录在`/var/lib/filebeat/registry/filebeat/log.json`文件中，可以实现日志采集的持续性，而不会重复采集
- 当日志文件大小发生变化时，filebeat会接着上一次记录的位置继续向下读取新的内容
- 当日志文件大小不变，但是内容发生变化时，filebeat会将文件的内容重新读取一遍
```yaml
# vim /etc/filebeat/file.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
  # 这里可以放多个文件，本身就是一个列表
  - /var/log/test.log
  - /var/log/syslog
output.console:
  pretty: true
  enable: true
```

### 不同的文件生成不同fields
用不同field标识不同文件来自不同的数据源
```yaml
filebeat.inputs:
- type: log
  paths:
    - /var/log/app1.log
  json.keys_under_root: true
  tags: ["app1_tag"]
  field:
    type: "app1"
- type: log
  paths:
    - /var/log/app2.log
  json.keys_under_root: true
  tags: ["app2_tag"]
  field:
    type: "app2"
output.console:
  pretty: true
```
### 利用filebeat收集系统日志到Elasticsearch
filebeat收集的系统日志到Elasticsearch
```shell
# 8.x版本
.ds-filebeat-<版本>-<时间>-<ID>
# 旧版
filebeat-<版本>-<时间>-<ID>
```

#### 修改配置
不使用-c指定配置文件，filebeat默认读取`/etc/filebeat/filebeat.yml`
```shell
# 方法1
# 先备份文件
cp /etc/filebeat/filebeat.yml{,.bak}
# 编辑
vim /etc/filebeat/filebeat.yml
# 删除所有原有内容，只添加下面内容
filebeat.inputs:
- type: log
  json.keys_under_root: true
  enabled: true       # 开启日志
  paths:
  - /var/log/syslog        # 指定收集的日志文件

#--------- Elasticsearch output ------------
output.elasticsearch:
  hosts: ["10.0.0.121:9200","10.0.0.122:9200","10.0.0.123:9200"]

# 方法2
# 修改syslog.conf
vim /etc/resyslog.conf
*.* /var/log/system.log

# 编辑filebeat配置文件
filebeat.inputs:
- type: log
  json.keys_under_root: true
  enabled: true       # 开启日志
  paths:
  - /var/log/system.log       # 指定收集的日志文件

#--------- Elasticsearch output ------------
output.elasticsearch:
  hosts: ["10.0.0.121:9200","10.0.0.122:9200","10.0.0.123:9200"]
```

### 自定义索引名称收集日志到ELasticsearch
#### 修改配置
```yaml
# vim /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  json.keys_under_root: true
  enabled: true
  paths:
  - /var/log/system.log
  include_lines: ['sshd','failed','password'] # 只过滤指定包含关键字的日志
# include_lines: ['^ERR', '^WARN'] # 可以使用正则表达式
# exclude_lines: ['Debug']         # 排除包含关键字的日志
# exclude_lines: ['.gz$']         # 排除包含关键字的日志, 使用正则
output.elasticsearch:
  hosts: ["10.0.0.121:9200","10.0.0.122:9200","10.0.0.123:9200"]
  index: "wang-%{[agent.version]-%{+yyyy,MM,dd}" #自定义索引名称
# 注意：如果自定义索引名称，没有添加下面三行的配置会导致filebeat无法启动

setup.ilm.enabled: false  # 关闭索引生命周期ilm功能，默认开启时索引名称只能为filebeat-*,自定义索引名必须修改为false
setup.template.name: "wang" # 定义模版名称，要自定义索引名，必须指定此项，否则无法启动
setup.template.pattern: "wang-*" #定义模版的匹配索引名称，要自定义索引名称，必须指定此项，否则无法启动
setup.template.settings:
  index.number_of_shards: 3
  index.number_of_replicas: 3
  # 默认情况下filebeat写入ES的索引分片为1，副本为1
```

上面修改自定义索引名的`agent.version`实际是内置可用字段，在Kibana中可见
![alt text](images\image7.png)

- 即使修改了自定义索引名，索引名前缀仍然是`.ds-XXXXX`
- 在filebeat上修改索引名意义不大，实际生产中通常是filebeat将日志发给logstash或者kafka等消息队列，从而在后续修改索引名


### 利用tags收集Nginx的JSON格式访问日志和错误日志到ELasticsearch不同的索引
```shell
# 安装nginx
apt update && apt install -y nginx

# 修改Nginx访问日志为json格式
# vim /etc/nginx/nginx.conf
    # Logging Settings
    ##
    log_format access_json '{"@timestamp":"$time_iso8601",'
        '"host":"$server_addr",'
        '"clientip":"$remote_addr",'
        '"size":"$body_bytes_sent",'
        '"responsetime":"$request_time",'
        '"upstreamtime":"$upstream_response_time",'
        '"upstreamhost":"$upstream_addr",'
        '"http_host":"$host",'
        '"uri":"$uri",'
        '"domain":"$host",'
        '"xff":"$http_x_forwarded_for",'
        '"referer":"$http_referer",'
        '"tcp_xff":"$proxy_protocol_addr",'
        '"http_user_agent":"$http_user_agent",'
        '"status":"$status"}';

#   access_log /var/log/nginx/access.log;
# 将access_log 指定存储文件和格式
    access_log /var/log/nginx/access_json.log access_json;

# 检测nginx配置文件是否正确
[root@ubuntu2204 nginx]#nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
# 正确则重新加载配置
[root@ubuntu2204 nginx]#nginx -s reload

# 安装filebeat并修改配置文件
# vim /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  json.keys_under_root: true
  enabled: true
  paths:
  - /var/log/nginx/access_json.log
  tags: ["nginx-access"]

- type: log
  enabled: true
  paths:
    - /var/log/nginx/error.log
  tags: ["nginx-error"]
#----------------------------------------
output.elasticsearch:
  hosts: ["10.0.0.121:9200","10.0.0.122:9200","10.0.0.123:9200"] # 指定ELK集群任意节点和端口，多个地址容错
  indices:
    - index: "nginx-access-%{[agent.version]}-%{+yyy.MM.dd}"
      when.contains:
        tags: "nginx-access"  # 如果日志中有access的tag，就记录到nginx-access的索引中
    - index: "nginx-error-%{[agent.version]}-%{+yyy.MM.dd}"
      when.contains:
        tags: "nginx-error"  #如果日志中有error的tag，就记录到nginx-error的索引中

# 自定义索引，必须加下面三行
setup.ilm.enabled: false
setup.template.name: "nginx"
setup.template.pattern: "nginx-*"
```
### 利用field字段收集Nginx的同一个访问日志中不同响应码的行到ELasticsearch不同的索引
```shell
# cat /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/nginx/access.log
  include_lines: ['404'] # 文件中包含404的行
  # exclude_lines:[]   # 还可以排除，[]中可以使用正则
  field:
    status_code: "404"
- type: log
  enabled: true
  paths:
    - /var/log/nginx/access.log
  include_lines: ['200']
  field:
    status_code: "200"
- type: log
  enabled: true
  paths:
    - /var/log/nginx/access.log
  include_lines: ['304']
  field:
    status_code: "304"

# 输出到es的配置 - 通过when语句进行字段的条件判断
output.elasticsearch:
  hosts: ["http://10.0.0.121:9200"]
  indices:
    -index: "myapp-error-404-%{+yyyy.MM.dd}"
    when.equals:
      fields.status_code: "404"
    -index: "myapp-error-200-%{+yyyy.MM.dd}"
    when.equals:
      fields.status_code: "200"
    -index: "myapp-error-304-%{+yyyy.MM.dd}"
    when.equals:
      fields.status_code: "304"

# 设定定制索引名称的配置
setup.ilm.enabled: false

# 设定定制索引名称的配置格式1
setup.template:
  enabled: true  # 默认值，可选
  name: "myapp"
  pattern: "myapp-*"

# 设定定制索引名称的配置格式2
setup.template.name: "myapp"
setup.template.pattern: "myapp-*"
```

### 利用Filebeat收集Tomcat的Json格式的访问日志和错误日志到ELasticsearch
#### 安装Tomcat并配置使用Json格式的访问日志
```shell
# 安装tomcat，可以包安装或者二进制安装
apt update && apt -y install tomcat9 tomcat9-admin

# 修改tomcat的访问日志为json格式
# 路径为包安装的默认路径
# vim /etc/tomcat9/server.xml
<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" prefix="localhost_access_log" suffix=".txt"
########################添加下面行,注意是一行,不要换行################################
pattern="
{&quot;clientip&quot;:&quot;%h&quot;,&quot;ClientUser&quot;:&quot;%l&quot;,&quot;authenticated&quot;:&quot;%u&quot;,&quot;AccessTime&quot;:&quot;%t&quot;,&quot;method&quot;:&quot;%r&quot;,&quot;status&quot;:&quot;%s&quot;,&quot;SendBytes&quot;:&quot;%b&quot;,&quot;Query?string&quot;:&quot;%q&quot;,&quot;partner&quot;:&quot;%{Referer}i&quot;,&quot;AgentVersion&quot;:&quot;%{User-Agent}i&quot;}"/>
################################################################################
     </Host>
   </Engine>
 </Service>
</Server>

# 重启tomcat服务
systemctl restart tomcat9

# 访问几次tomcat页面，然后查看json格式日志
tail -n1 /var/log/tomcat9/localhost_access_log.2023-07-10.txt 
```

#### 修改Filebeat配置文件
```shell
# cat /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/tomcat9/localhost_access_log.* # 包安装路径
  json.keys_under_root: true # 默认False会将json数据存储至message，改为true则会独立message外存储
  json.overwrite_keys: false # 设为true,覆盖默认的message字段，使用自定义json格式中的key
  tags: ["tomcat-access"]

- type: log
  enabled: true
  paths:
    - /var/log/tomcat9/catalina.*.log
  tags: ["tomcat-error"]

output.elasticsearch:
  hosts: ["10.0.0.121:9200"]
  indices:
    - index: "tomcat-access-%{[agent.version]}-%{+yyyy.MM.dd}"
     when.contains:
       tags: "tomcat-access"
    - index: "tomcat-error-%{[agent.version]}-%{+yyyy.MM.dd}"
     when.contains:
       tags: "tomcat-error"
  
setup.ilm.enabled: false
setup.template.name: "tomcat"
setup.template.pattern: "tomcat-*"
```

### 利用Filebeat收集Tomcat的多行错误日志到ELasticsearch(多行合并)
#### 将一个错误对应的多个行合并成一个ES的文档记录来解决此问题
![alt text](images\image8.png)

#### 修改Filebeat配置文件
```shell
[root@elk-web1 ~]#cat /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
 enabled: true
 paths:
    #- /usr/local/tomcat/logs/localhost_access_log.* #二进制安装
    - /var/log/tomcat9/localhost_access_log.* #包安装
 json.keys_under_root: true
 json.overwrite_keys: false
 tags: ["tomcat-access"]
- type: log
 enabled: true
 paths:
    #- /usr/local/tomcat/logs/catalina.*.log #二进制安装
   /var/log/tomcat9/catalina.*.log #包安装
 tags: ["tomcat-error"]
 multiline.type: pattern            #此为默认值,可省略
 multiline.pattern: '^[0-3][0-9]-'  #正则表达式匹配以两位,或者为'^\d{2}'
 multiline.negate: true             #negate否定无效
 multiline.match: after
 multiline.max_lines: 5000          #默认只合并500行,指定最大合并5000行
  
output.elasticsearch:
 hosts: ["10.0.0.101:9200"]      
 indices:
    - index: "tomcat-access-%{[agent.version]}-%{+yyy.MM.dd}"
     when.contains:
       tags: "tomcat-access"
    - index: "tomcat-error-%{[agent.version]}-%{+yyy.MM.dd}"
     when.contains:
       tags: "tomcat-error"
  
setup.ilm.enabled: false
setup.template.name: "tomcat"
setup.template.pattern: "tomcat-*
```

### 利用Filebeat收集Nginx日志到Redis
将filebeat收集的日志，发送至Redis格式如下
```shell
output.redis:
 hosts: ["localhost:6379"]
 password: "my_password"
 key: "filebeat"
 db: 0
 timeout: 5
```

#### 安装Nginx配置访问日志使用Json格式
```shell
# 安装nginx
apt update && apt install -y nginx

# 修改Nginx访问日志为json格式
# vim /etc/nginx/nginx.conf
    # Logging Settings
    ##
    log_format access_json '{"@timestamp":"$time_iso8601",'
        '"host":"$server_addr",'
        '"clientip":"$remote_addr",'
        '"size":"$body_bytes_sent",'
        '"responsetime":"$request_time",'
        '"upstreamtime":"$upstream_response_time",'
        '"upstreamhost":"$upstream_addr",'
        '"http_host":"$host",'
        '"uri":"$uri",'
        '"domain":"$host",'
        '"xff":"$http_x_forwarded_for",'
        '"referer":"$http_referer",'
        '"tcp_xff":"$proxy_protocol_addr",'
        '"http_user_agent":"$http_user_agent",'
        '"status":"$status"}';

#   access_log /var/log/nginx/access.log;
# 将access_log 指定存储文件和格式
    access_log /var/log/nginx/access_json.log access_json;

# 检测nginx配置文件是否正确
[root@ubuntu2204 nginx]#nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
# 正确则重新加载配置
[root@ubuntu2204 nginx]#nginx -s reload
```

#### 安装和配置redis
```shell
apt install -y redis
sed -i.bak '/^bind.*/c bind 0.0.0.0' /etc/redis/redis.conf
systemctl restart redis
```

#### 修改Filebeat配置文件
```shell
# vim /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
     - /var/log/nginx/access_json.log
  json.keys_under_root: true #默认False会将json数据存储至message，改为true则会独立message外存储
  json.overwrite_keys: true  #设为true,覆盖默认的message字段，使用自定义json格式中的key
  tags: ["nginx-access"]
  
- type: log
  enabled: true
  paths:
     - /var/log/nginx/error.log
  tags: ["nginx-error"]

output.redis:
  hosts: ["10.0.0.104:6379"]
  key: "filebeat"
  #password: "123456"
  #db: 0
  
systemctl restart filebeat.service
```
### 从标准输入读取再输出至Kafka
```shell
#vim /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: stdin
  enabled: true
  
output.kafka:
  hosts: ["10.0.0.201:9092", "10.0.0.202:9092", "10.0.0.203:9092"]
  topic: filebeat-log       #指定kafka的topic
  partition.round_robin:
    reachable_only: true    #true表示只发布到可用的分区，false 时表示所有分区，如果一个节点down，会block
  required_acks: 1          #如果为0，错误消息可能会丢失，1等待写入主分区（默认），-1等待写入副本分区
  compression: gzip  
  max_message_bytes: 1000000 #每条消息最大长度，以字节为单位，如果超过将丢弃
  
#查看kafka是否收到数据
/usr/local/kafka/bin/kafka-topics.sh --list --bootstrap-server 10.0.0.201:9092 
/usr/local/kafka/bin/kafka-console-consumer.sh --topic filebeat-log --bootstrap-server 10.0.0.201:9092 --from-beginning
```

### 从标准输入读取在输出至Logstash
```shell
# vim /etc/filebeat/filebeat.yml 
filebeat.inputs:
- type: stdin
  enabled: true
  
output.logstash:
  hosts: ["10.0.0.104:5044","10.0.0.105:5044"]
  index: filebeat  
  loadbalance: true    #默认为false,只随机输出至一个可用的logstash,设为true,则输出至全部logstash
  worker: 1     #线程数量
  compression_level: 3 #压缩比
```

# Logstash过滤
## Logstash介绍
- Logstash是免费且开放的服务器端数据处理管道，能从多个来源采集数据，转换数据，然后将数据发送到您最喜欢的一个或多个“存储库”中
- Logstash是整个ELK中拥有最丰富插件的一个组件，而且支持可以水平伸缩
- Logstash基于Java和Ruby语言开发

### Logstash架构
- 输入input：用于日志收集，常见插件：Stdin、File、Kafka、Redis、Filebeat、Http
- 过滤Filter：日志过滤和转换，常见插件：grok、date、geoip、mutate、useragent
- 输出Output：将过滤转换过的日志输出：常见插件：File、Stdout、ELasticsearch、MySQL、Redis、Kafka

### Logstash和Filebeat比较
- Logstash功能更丰富，可以支持直接将非json格式的日志统一转换为json格式，且支持多目标输出，和filterbeat相比有更为强大的过滤功能
- Logstash:资源消耗更多，不适合在每个需要收集日志的主机上安装

## Logstash安装
```shell
# 下载
wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/l/logstash/logstash-8.15.0-amd64.deb

# 安装
dpkg -i logstash-8.15.0-amd64.deb

# 查看Logstash命令选项
/usr/share/logstash/bin/logstash --help

# 可以加入环境变量，方便后续使用
ln -s /usr/share/logstash/bin/logstash /usr/local/bin/logstash

# 常用选项
-e      # 指定配置内容
-f      # 指定配置文件，支持绝对路径，如果使用相对路径，是相对于/usr/share/logstash/的路径
-t      # 语法检测
-r      # 修改配置文件后自动加载生效，注意：有时修改配置需要重启生效

# 启动Logstash服务
systemctl start Logstash

# 查看Logstash插件
/usr/share/logstash/bin/logstash-plugin list
```

## Logstash输入INPUT插件
### 标准输入
codec用于输入数据的编码器，默认值为plain表示单行字符串，若设置为json，表示按照json方式解析
```shell
# 标准输入和输出,codec => rubydebug指输出格式，是默认值，可以省略，也支持设为json
logstash -e 'input { stdin{} } output { stdout{}}'
# 输入
hello-m60 
# 输出
{
      "@version" => "1",
          "host" => {
        "hostname" => "ubuntu2204.wang.org"
    },
       "message" => "hello-m60",
         "event" => {
        "original" => "hello-m60"
    },
    "@timestamp" => 2024-08-18T11:52:47.083150335Z
}

# 指定输入信息为json格式
logstash -e 'input { stdin{ codec => json } } output { stdout{ codec => rubydebug}}'

# 输入
{"name":"wang","age":"19","gender":"male"} # 输入json格式
# 输出
{
      "@version" => "1",
         "event" => {
        "original" => "{\"name\":\"wang\",\"age\":\"19\",\"gender\":\"male\"}\n"
    },
    "@timestamp" => 2024-08-18T12:00:24.394923833Z,
          "name" => "wang",
        "gender" => "male",
           "age" => "19",
          "host" => {
        "hostname" => "ubuntu2204.wang.org"
    }
}

# 添加tag和type
logstash -e 'input { stdin{ tags => "stdin_tag" type => "stdin_type" codec => json } } output { stdout{ }}'

# 输入hello,world
{
       "message" => "hello,word",
          "tags" => [
        [0] "_jsonparsefailure",
        [1] "stdin_tag"
    ],
    "@timestamp" => 2024-08-18T12:05:32.620434360Z,
      "@version" => "1",
         "event" => {
        "original" => "hello,word\n"
    },
          "host" => {
        "hostname" => "ubuntu2204.wang.org"
    },
          "type" => "stdin_type"
}

# 输入json{"name":"wang"}
{
          "tags" => [
        [0] "stdin_tag"
    ],
          "name" => "wang",
      "@version" => "1",
    "@timestamp" => 2024-08-18T12:06:24.098709557Z,
         "event" => {
        "original" => "{\"name\":\"wang\"}\n"
    },
          "host" => {
        "hostname" => "ubuntu2204.wang.org"
    },
          "type" => "stdin_type"
}
```

### 从文件输入
Logstash会记录每个文件的读取位置，下次自动从此位置继续向后读取

- 每个文件的读取位置记录在下面对应的文件中
```shell
#新版：8.11.1
/usr/share/logstash/data/plugins/inputs/file/.sincedb_XXXX

# 旧版
/var/lib/logstash/plugins/inputs/file/.sincedb_XXX
# 此文件包括文件的inode号，大小等信息
```

#### 修改配置文件
```shell
cat /etc/logstash/conf.d/file_to_stdout.conf
# 内容如下
input {
    file {
        path => "/tmp/wang.*"
        type => "wanglog"              # 添加自定义的type字段，可以用于条件判断，和filebeat中tag功能相似
        exclude => "*.txt"             # 排除不采集数据的文件，使用通配符glob匹配语法
        start_position => "beginning"  # 第一次从头开始读取文件，可以取值为:beginning和end，默认为end，即只从最后尾部读取日志
        stat_interval => "3"           # 定义检查文件是否更新，默认1s
        codec => json                  # 如果文件是json格式，需要指定此项才能解析，如果不是Json格式而添加此行也不会影响结果
    }
    file {
        path => "/var/log/syslog"
        type => "syslog"
        start_position => "beginning"
        stat_interval => "3"
    }
}

output {
    stdout {
        codec => rubydebug
    }
}

# 语法检查
#语法检查,配置文件路径默认查找/usr/share/logstash/，文件放在此路径下时可省略
/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/stdin_to_stdout.conf -t

# 执行logstash,选项-r表示动态加载 
/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/stdin_to_stdout.conf -r
```

### 从Http请求获取数据
```shell
# cat /etc/logstash/conf.d/http_to_stdout.conf
input {
   http {
       port => 6666
       codec => json
   }
}
output {
   stdout {
       codec => rubydebug
   }
}
/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/http_to_stdout.conf -r

# 提交字符串
curl -XPOST -d'test log message' http://logstash.wang.org:6666

# 输出
{
    "user_agent" => {
        "original" => "curl/7.81.0"
    },
       "message" => "test log message",
          "tags" => [
        [0] "_jsonparsefailure"
    ],
    "@timestamp" => 2024-08-18T13:03:15.124956933Z,
          "http" => {
         "method" => "POST",
        "request" => {
                 "body" => {
                "bytes" => "16"
            },
            "mime_type" => "application/x-www-form-urlencoded"
        },
        "version" => "HTTP/1.1"
    },
           "url" => {
        "domain" => "localhost",
          "port" => 6666,
          "path" => "/"
    },
      "@version" => "1",
          "host" => {
        "ip" => "127.0.0.1"
    }
}

# 提交json格式数据，可以自动解析
curl -XPOST -d'{ "name":"wang","age": "18","gender":"male"}' http://logstash.wang.org:6666
```
#### 使用第三方图形工具，提交http数据
- 比如：burp

### 从filebeat读取数据
```yaml
# filebeat配置
# vim /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
  - /var/log/nginx/access_json.log
  json.keys_under_root: true
  tags: ["nginx-access"]
- type: log
  enabled: true
  paths:
  - /var/log/syslog        # 指定收集的日志文件
  field:
    logtype: "syslog"      # 添加自定义字段logtype

output.logstash:
  host: ["10.0.0.126:5044"]  # 指定Logstash服务器的地址和端口

# Logstash配置
# cat /etc/logstash/conf.d/filebeat_to_stdout.conf
input {
    beats {
        port => 5044
    }
}

output {
    stdout {
        code => rubydebug
    }
}
```

### 从Redis读取日志
```shell
# cat /etc/logstash/conf.d/redis_to_stdout.conf
input {
 redis {
 host => 'Redis_IP'
 port => "6379"
 password => "123456"
 db => "0"
 data_type => 'list'
 key => "nginx-accesslog"
 }
}
output {
   stdout {
       codec => rubydebug
   }
}

/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/redis_to_stdout.conf -r
```

### 从Kafka中读取日志
```shell
# cat /etc/logstash/conf.d/kafka_to_stdout.conf
input {
   kafka {
       bootstrap_servers => "10.0.0.201:9092,10.0.0.202:9092,10.0.0.203:9092"
       group_id => "logstash" #多个logstash的group_id如果不同，将实现消息共享（发布者/订阅者模式），如果相同（建议使用），则消息独占（生产者/消费者模式）
       topics => ["nginx-accesslog","nginx-errorlog"]
       codec => "json"
       consumer_threads => 8
   }
}

output {
   stdout {
       codec => rubydebug
   }
}

# 加载配置
/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/kakfa_to_stdout.conf -r
```

### 从syslog输入数据
```shell
# cat /etc/logstash/conf.d/haproxy-syslog-to-es.conf
input {
    syslog {
        host => "0.0.0.0"
        port => "514"           # 指定监听的UDP/TCP端口，注意普通用户无法监听此端口，因为此端口是特权端口
        type => "haproxy"
    }
}
```

#### 普通用户监听特权端口的方案
1. 修改内核参数
```shell
# 修改 net.ipv4.ip_unprivileged_port_start = 1024
# 改为
net.ipv4.ip_unprivileged_port_start = 0  #表示所有端口都是非特权端口
```
2. 使用iptables转发，将特权端口转发到非特权端口
3. 使用setcap命令进行授权
4. sudo授权

#### 补充
- 如果logstash收集本机上面的文件也需要root权限，因此建议修改`service`文件，使其直接以root身份运行

### 从TCP/UDP协议输入数据
```shell
cat /etc/logstash/conf.d/tcp-to-es.conf
input {
    tcp {
        port => "9527"
        host => "0.0.0.0"
        type => "tcplog"   # 用于判断输出
        codec => "json"
        mode => "server"   # 默认值，可省略

    }
}

output {
    stdout {
        codec => rubydebug
    }
}
```

## Logstash过滤filter插件
数据从源传输到存储库的过程中，Logstash过滤器能够解析各个事件，识别已命名的字段以构建结构，并将它们转换成通用格式，以便进行更强大的分析和实现商业价值

Logstash能够动态地转换和解析数据，不受格式或复杂度的影响

常见的Filter插件：
- 利用Grok从非结构化数据中转化为结构数据
- 利用GEOIP根据IP地址找出对应的地理位置坐标
- 利用useragent从请求中分析操作系统，设备类型
- 利用Mutate从请求中整理字段
- Date插件可以将日志中的指定的日期字符串对应的源字段生成新的目标字段

### Grok插件
#### Grok插件介绍
为了将日志行与格式匹配。生产环境常需要将非结构化的数据结构解析成json结构化数据格式
Grok可以解析任意文本并把它们结构化。因此Grok是将非结构化的日志数据解析为可查询的结构化数据的好方法
Grok非常适合将syslog日志、apache和其他web服务器日志、MySQL日志等日志格式转换为JSON格式

比如下面行：
```shell
2016-09-19T18:19:00 [8.8.8.8:prd] DEBUG this is an example log message
```
使用Grok插件可以基于正则表达式技术利用其内置的正则表达式别名来表示和匹配上面的日志，如下效果
```shell
%{TIMESTAMP_ISO8601:timestamp} \[%{IPV4:ip};%{WORD:environment}\] %{LOGLEVEL:log_level} %{GREEDYDATA:message}
```
最终转换为如下形式
```shell
{
  "timestamp": "2016-09-19T18:19:00",
  "ip": "8.8.8.8",
  "environment": "prd",
  "log_level": "DEBUG",
  "message": "this is an example log message"
}
```

Grok的匹配格式可以使用AI工具进行查询，而后直接在配置文件中使用

#### 示例：使用grok pattern将Nginx日志格式转换为JSON格式
```shell
# vim /etc/logstash/conf.d/http_grok_stdout.conf
input {
    http {
        port => 6666
    }
}

filter {
    # 将nginx日志格式化为JSON格式
    grok {
        match => {
            "message" => "%{COMBINEDAPACHELOG}" #将message字段转换为指定的JSON格式
        }
    }    
}

output {
    stdout {
        codec => rebydebug
    }
}

# 执行
logstash -f /etc/logstash/conf.d/http_grok_stdout.conf
```

### GeoIP插件
geoip根据ip地址提供的对应地域信息，比如：经纬度，国家，城市名等，以方便进行地理数据分析
```shell
# vim /etc/logstash/conf.d/http_geoip_stdout.conf
input {
    http {
        port => 6666
        codec => "json"
    }
}

filter {
    #将nginx日志格式化为json格式
    grok {
        match => {
            "message" => "%{COMBINEDAPACHELOG}" 
        }
    }
    # 以上面提取clientip字段为源，获取地域信息
    geoip {
        # source => "clientip"        # 7.x版本指定源IP的所在字段
        source => "[source][address]" # 8.x版本变化，结合grok插件
        target => "geoip"
    }
}

output {
    stdout {
        codec => rubydebug
    }
}
```

#### 只显示指定的geoip的字段信息
```shell
#cat /etc/logstash/conf.d/http_geoip_field_stdout.conf

input {
    http {
        port =>6666
   }
}
filter {
    #将nginx日志格式化为json格式
    grok {
        match => {
            "message" => "%{COMBINEDAPACHELOG}"
       }
   }
    #以上面提取clientip字段为源,获取地域信息,并指定只保留显示的字段
    geoip {
        #source => "clientip"           #7.X版本
        source => "[source][address]"   #8.X版本变化
        target => "geoip"
        fields => ["continent_code","country_name","city_name","timezone", "longitude","latitude"]
   }
}
output {
    stdout {
        codec => rubydebug
   }
}
```

### Date插件



# Kibana图形展示
## 安装并配置Kibana
### 下载链接
```shell
# 官方链接
https://www.elastic.co/cn/downloads/kibana
https://www.elastic.co/cn/downloads/past-releases#kibana

# 清华源下载链接
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/apt/8.x/pool/main/k/kibana/kibana-8.15.0-amd64.deb
```

### 安装并配置
```shell
# 安装
dpkg -i kibana-8.15.0-amd64.deb

# 修改配置
vim /etc/kibana/kibana.yml

# 修改监听地址，使其所有主机都能访问
# To allow connections from remote users, set this parameter to a non-loopback address.
server.host: "0.0.0.0"

# 指定ES地址
# The URLs of the Elasticsearch instances to use for all your queries.
elasticsearch.hosts: ["http://10.0.0.121:9200","http://10.0.0.122:9200","http://10.0.0.123:9200"]

# 如果开启了Xpack，则需要验证
#elasticsearch.username: "kibana_system"
#elasticsearch.password: "pass"

# 开启中文界面
# Supported languages are the following: English (default) "en", Chinese "zh-CN", Japanese "ja-JP", French "fr-FR".
i18n.locale: "zh-CN"

# 保存配置后开启服务
systemctl start kibana.service
```

### 使用Kibana查看索引
```shell
10.0.0.132:5601 --> Management --> Stack Management --> 索引管理
```


### 数据视图（7版本之前叫索引模式）
```shell
10.0.0.132:5601 --> Management --> Stack Management --> 数据视图 --> 创建数据视图
```
