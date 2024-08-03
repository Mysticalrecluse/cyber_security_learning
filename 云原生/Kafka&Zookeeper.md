# ZooKeeper
## Zookeeper解决的问题
- 实现了服务注册,服务发现
- 即实现了分布式服务管理

## Zookeeper的功能
- 实现了服务的命名服务
    - 即给每个服务取个名称进行存放，并对其进行对应的解析，解析成对应的地址，实现服务发现，服务注册

- Zookeeper内部可以看作是一个树状存储数据库
    - 在启动一个服务的时候，可以将自己的地址信息注册到Zookeeper的树状数据库中，在数据库中将每个服务的地址，端口号注册进Zookeeper(类比：port的启动的时候会将自己的地址和端口号注册进service的endpoint中)，
        - 后续有程序需要使用这个服务，就取Zookeeper中查询即可
        - Zookeeper做注册中心，需要在java程序中配置注册中心（Zookeeper）的地址
    - 然后zookeeper给每个服务取一个名称，通过名称借助数据库解析为对应的ip地址和端口
    - 同时Zookeeper也可以存放一些状态信息
    - Zookeeper也可以做配置中心

### 解决的问题
- 服务的地址端口预先不确定的情况下，如何实现服务间通讯

## 部署Zookeeper
### 包安装
```shell
[root@ubuntu2204 ~]#apt list zookeeper
正在列表... 完成
zookeeper/jammy-security,jammy-updates 3.4.13-6ubuntu4.1 all

apt -y install zookeeper

# 启动zookeeper
/usr/share/zookeeper/bin/zkServer.sh start
```

### 二进制安装
```shell
# 安装java环境
apt install -y openjdk-8-jdk
# 下载zookeeper
wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/current/apache-zookeeper-3.9.2-bin.tar.gz

# 解压并放入指定目录
tar xf apache-zookeeper-3.9.2-bin.tar.gz -C /usr/local/

# 将其放入PATH目录中
# vim /etc/profile
PATH=$PATH:/usr/local/zookeeper/bin/

# 加载
. /etc/profile

# 创建配置文件zoo.cfg
cd /usr/local/zookeeper/conf
cp zoo_sample.cfg zoo.cfg

# 启动zookeeper并查看状态
[root@ubuntu2204 conf]#zkServer.sh start
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
[root@ubuntu2204 conf]#zkServer.sh status
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: standalone  # 表示是单机模式，不是集群

# 查看zookeeper端口（2181以打开），本质上就是java程序
[root@ubuntu2204 conf]#ss -nltp
State      Recv-Q     Send-Q         Local Address:Port          Peer Address:Port    Process                                       
LISTEN     0          4096           127.0.0.53%lo:53                 0.0.0.0:*        users:(("systemd-resolve",pid=810,fd=14))    
LISTEN     0          128                  0.0.0.0:22                 0.0.0.0:*        users:(("sshd",pid=862,fd=3))                
LISTEN     0          50                         *:2181                     *:*        users:(("java",pid=16738,fd=77))             
LISTEN     0          50                         *:8080                     *:*        users:(("java",pid=16738,fd=69))             
LISTEN     0          50                         *:32785                    *:*        users:(("java",pid=16738,fd=68))             
LISTEN     0          128                     [::]:22                    [::]:*        users:(("sshd",pid=862,fd=4)) 
```
#### Zookeeper配置文件
```shell
# 可以更改配置使其暴露端口被Prometheus监控
cat /usr/local/zookeeper/conf/zoo.cfg
# The number of milliseconds of each tick
tickTime=2000
# The number of ticks that the initial 
# synchronization phase can take
initLimit=10
# The number of ticks that can pass between 
# sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just 
# example sakes.
dataDir=/tmp/zookeeper
# the port at which the clients will connect
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
#
# Be sure to read the maintenance section of the 
# administrator guide before turning on autopurge.
#
# https://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
#
# The number of snapshots to retain in dataDir
#autopurge.snapRetainCount=3
# Purge task interval in hours
# Set to "0" to disable auto purge feature
#autopurge.purgeInterval=1

## Metrics Providers
#
# https://prometheus.io Metrics Exporter
metricsProvider.className=org.apache.zookeeper.metrics.prometheus.PrometheusMetricsProvider
metricsProvider.httpHost=0.0.0.0
metricsProvider.httpPort=7000    # 打开7000端口
metricsProvider.exportJvmInfo=true
```
- 访问Prometheus指标
```shell
curl 127.0.0.1:7000/metrics
```
#### 前台执行Zookeeper(制作镜像时使用)
```shell
zkServer.sh start-foreground
```

### Zookeeper集群部署
- 因为选举机制，半数以上可用，所以建议奇数个节点
- Zookeeper的选举基于ZAB协议（原子广播协议）
  - Zab(Zookeeper Atomic Broadcast原子广播)：强一致性协议
- 集群中节点数越多，写性能越差，读性能越好


#### 集群角色
- 领导者(Leader)
  - 负责处理写入请求的，事务请求的唯一调度和处理者，负责进行投票发起和决议，更新系统状态

- 跟随者(Follower)
  - 接收客户请求并向客户端返回结果，在选Leader中参与投票

- 观察者(Observer)
  - 转交客户端写请求给leader节点，和同步leader状态和Follower唯一区别就是不参与Leader投票，也不参与写操作的“过半写成功”策略
  - 它的作用类似于专用于Zookeeper集群的反向代理

- 学习者(Learner)
  - 和leader进行状态同步的节点统称Learner，包括Follower和Observer

- 客户端(Client)
  - 请求发起者

#### 选举ID
- ZXID(zookeeper transaction id): 每个改变Zookeeper状态的操作都会自动生成一个对应的zxid。ZXID最大的节点优先选为Leader
  - ZXID大说明该节点的数据是最新的，ZXID可以理解为事务ID
- myid: 服务器的唯一标识(SID)，通过配置myid文件指定，集群中唯一，当ZXID一样时，myid大的节点优先选为Leader


### 协议说明（重要）
在分布式系统中，有多种协议被设计来解决一致性问题，Paxos、Raft、ZAB等分布式算法经常会被称作是“强一致性”的分布式共识协议

#### ZAB(Zookeeper Atomic Broadcast 原子广播)
Zab协议是由Apache Zookeeper项目提出的一种原子广播协议，是为分布式协调服务Zookeeper专门设计的一种支持崩溃恢复的原子广播协议。在Zookeeper中，主要依赖ZAB协议来实现分布式数据一致性，基于该协议，Zookeeper实现了一种主备模式的系统架构来保持集群中各个副本之间的数据一致性

#### Raft
Raft是一个为分布式系统提供一致性的算法。与Paxos相比，Raft的主要目标是提供一种更加易于理解和实现的一致性算法。Raft通过选举算法确保了分布式系统中的领导者唯一性所有的写操作都通过领导者完成，这样就可以确保所有的复制节点上的数据一致性，一些知名的分布式系统，如：kafka,etcd,nacos和Consul，都采用了Raft算法

#### Zookeeper集群部署实现

```shell
# 在三台机器上安装Zookeeper

# 当所有的机器都准备好Zookeeper之后，准备配置文件
# 配置文件的最后添加
# 将路径指向指定的myid所在路径
dataDir=/usr/local/zookeeper/data
# 格式：server.MyID服务器唯一编号=服务器IP:Leader和Follower的数据同步端口(只有leader才会打开)：Leader和Follower选举端口(L和F都有)
server.1=10.0.0.131:2888:3888
server.2=10.0.0.132:2888:3888
server.3=10.0.0.133:2888:3888

# 如果添加节点，只需要在所有节点上添加新节点的上面形式的配置行，在新节点创建myid文件，并重启所有节点服务即可

# 将配置文件同步到其他机器
scp /usr/local/zookeeper/conf/zoo.cfg 10.0.0.132:/usr/local/zookeeper/conf/
scp /usr/local/zookeeper/conf/zoo.cfg 10.0.0.133:/usr/local/zookeeper/conf/
```

- 在各个节点生成ID文件
```shell
echo 1 > /usr/local/zookeeper/data/myid
echo 2 > /usr/local/zookeeper/data/myid
echo 3 > /usr/local/zookeeper/data/myid
```

- 各服务启动Zookeeper
```shell
zkServer.sh start   # 三台机器都启动

# node1
[root@ubuntu2204 conf]#zkServer.sh status
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: follower

# node2
[root@ubuntu2204 zookeeper]#zkServer.sh status
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: leader

# node3
[root@ubuntu2204 data]#zkServer.sh status
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: follower
```

### ZooKeeper客户端访问
#### 命令行客户端访问ZooKeeper
```shell
# 使用命令行访问
# 如果不写ip:port，默认本机
zkCli.sh -server 10.0.0.131:2181

[zk: 10.0.0.132:2181(CONNECTED) 1] ls /
[zookeeper]

# 查看zookeeper集群数据
[zk: 10.0.0.132:2181(CONNECTED) 4] ls /zookeeper 
[config, quota]
[zk: 10.0.0.132:2181(CONNECTED) 5] ls /zookeeper/config 
[]
[zk: 10.0.0.132:2181(CONNECTED) 6] get /zookeeper/config 
server.1=10.0.0.131:2888:3888:participant
server.2=10.0.0.132:2888:3888:participant
server.3=10.0.0.133:2888:3888:participant
version=0

# 在zookeeper中创建子目录create,以及在文件中添加数据set
# zookeeper中，目录即是目录也是可以保存数据的文件
[zk: 10.0.0.132:2181(CONNECTED) 7] ls /
[zookeeper]
[zk: 10.0.0.132:2181(CONNECTED) 8] create /myapp1
Created /myapp1
[zk: 10.0.0.132:2181(CONNECTED) 9] ls /
[myapp1, zookeeper]
[zk: 10.0.0.132:2181(CONNECTED) 10] set /myapp1 M58
[zk: 10.0.0.132:2181(CONNECTED) 11] get /myaap1
Node does not exist: /myaap1
[zk: 10.0.0.132:2181(CONNECTED) 12] get /myapp1
M58
```

#### nc访问Zookeeper
Zookeeper支持某些特定的四字命令字母与其交互，它们大多是查询命令，用来获取ZooKeeper服务的当前状态和相关信息

- 常用命令列表
```shell
conf #输出相关服务配置的详细信息
cons #列出所有连接到服务器的客户端的完全的连接/会话的详细信息
envi #输出关于服务环境的详细信息
dump #列出未经处理的会话和临时节点
stat #查看哪个节点被选择作为Follower或者Leader
ruok #测试是否启动了该Server，若回复imok表示已经启动
mntr #输出一些运行时信息
reqs #列出未经处理的请求
wchs #列出服务器watch的简要信息
wchc #通过session列出服务器watch的详细信息
wchp #通过路径列出服务器watch的详细信息
```

- 命令安全限制
```shell
# 默认情况下，这些4字命令有可能会被拒绝，提示如下报错
xxxx is not executed because it is not in the whitelist.

#解决办法:在 zoo.cfg文件中添加如下配置,如果是集群需要在所有节点上添加下面配置
# vim conf/zoo.cfg
4lw.commands.whitelist=*

#在服务状态查看命令中有很多存在隐患的命令，为了避免生产中的安全隐患，要对这些"危险"命令进行一些安全限制，只需要编辑服务的zoo.cfg文件即可

# vim conf/zoo.cfg
4lw.commands.whitelist=conf,stat,ruok,isro
```

### 图形化客户端Zoolnspector
#### Linux客户端
- 编译zooinspector
  - 注意：此软件因年代久远，仅支持JAVA-8，且不支持Ubuntu20.04但支持Ubuntu22.04和Rocky8
```shell
#Ubuntu22.04编译
apt update && apt -y install openjdk-8-jdk
apt update && pat -y install maven

# 添加阿里云加速
vim /etc/maven/settings.xml 
<mirrors>
   <!--阿里云镜像-->
   <mirror>
       <id>nexus-aliyun</id>
       <mirrorOf>*</mirrorOf>
       <name>Nexus aliyun</name>
       <url>http://maven.aliyun.com/nexus/content/groups/public</url>
   </mirror>                                                                                               
</mirrors>

# 下载zooInspector
git clone https://mirror.ghproxy.com/https://github.com/zzhang5/zooinspector.git

cd zooinspector/
mvn clean package -Dmaven.test.skip=true

# 授权
chmod +x zooinspector-pkg/bin/zooinspector.sh

# 运行
./zooinspector-pkg/bin/zooinspector.sh
```

# Kafka
## 消息队列简介
略
### 消息对接解决的问题
- 消息队列主要用于解决服务间访问

### 消息队列主要应用场景
- 削峰填谷
- 异步解耦
- 顺序收发
- 分布式事务一致性
- 大数据分析
- 分布式缓存同步
- 蓄流压测

### Kafka特点和优势
- 特点：
  - 分布式：支持分布式多主机部署实现
  - 分区：一个消息，可以拆分出多个，分别存储在多个位置
  - 多副本：防止信息丢失，可以多来几个副本
  - 多订阅者：可以有很多应用连接Kafka
  - Zookeeper：早期版本的Kafka依赖于Zookeeper

- 优势：
  - Kafka通过O(1)的磁盘数据结构(顺序写入)提供消息的持久化，这种结构对于即使数以 TB 级别以上的消息存储也能够保持长时间的稳定性能。
  - 高吞吐量：即使是非常普通的硬件Kafka也可以支持每秒数百万的消息。支持通过Kafka 服务器分区消息。
  - 分布式： Kafka 基于分布式集群实现高可用的容错机制，可以实现自动的故障转移
  - 顺序保证：在大多数使用场景下，数据处理的顺序都很重要。大部分消息队列本来就是排序的，并且能保证数据会按照特定的顺序来处理。 Kafka保证一个Partiton内的消息的有序性（分区间数据是无序的，如果对数据的顺序有要求，应将在创建主题时将分区数partitions设置为1）
  - 支持Hadoop并行数据加载
  - 通常用于大数据场合,传递单条消息比较大，而Rabbitmq 消息主要是传输业务的指令数据,单条数据较小


### 深入理解kafkaz在实际应用中的作用（电商侧）

#### Kafka 实现异步解耦的优势
- 高吞吐量和低延迟：
  - Kafka 能够处理大量的消息，支持高吞吐量和低延迟的数据传输。
  - 在电商平台中，可以同时处理大量订单、用户行为等数据流，确保系统的高性能。

- 持久化存储：
  - Kafka 会将消息持久化到磁盘，确保消息不会丢失。
  - 即使系统故障或重启，消息仍然能够被可靠地恢复。

- 可扩展性：
  - Kafka 允许横向扩展，可以通过增加更多的 broker 来提升系统的处理能力。
  - 生产者和消费者都可以独立扩展，适应不断增长的数据量和业务需求。

- 高可用性：
  - Kafka 通过分区和副本机制，确保高可用性和数据冗余。
  - 即使某个节点出现故障，其他副本可以继续提供服务。

#### 对比示例：使用和不使用 Kafka
使用 Kafka 的示例
如前所述，使用 Kafka 的生产者和消费者程序如下：
- 生产者程序
```python
from kafka import KafkaProducer
import json

# 创建 Kafka 生产者
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 发送订单消息
order = {'orderId': '12345', 'amount': 100}
producer.send('order-topic', value=order)
producer.flush()  # 确保消息被发送
producer.close()
```

- 消费者程序
```python
from kafka import KafkaConsumer
import json

# 创建 Kafka 消费者
consumer = KafkaConsumer(
    'order-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='order-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# 消费订单消息
for message in consumer:
    order = message.value
    print(f"Received order: {order}")
    # 处理订单逻辑
```

不使用 Kafka 的示例
假设不使用 Kafka，而是直接通过 REST API 或数据库传递订单信息
- 生产者程序（通过 REST API 直接发送订单）：
```python
import requests
import json

order = {'orderId': '12345', 'amount': 100}
response = requests.post('http://localhost:5000/orders', json=order)

if response.status_code == 200:
    print("Order sent successfully")
else:
    print("Failed to send order")

```
- 消费者程序
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def receive_order():
    order = request.get_json()
    print(f"Received order: {order}")
    # 处理订单逻辑
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5000)
```
对比分析
- 同步 vs 异步：
  - 不使用 Kafka 的方案是同步通信，生产者必须等待消费者处理完请求后才能继续。这样会导致生产者阻塞，特别是在高并发场景下，系统响应变慢。
  - 使用 Kafka 的方案是异步通信，生产者发送消息后立即返回，不需要等待消费者处理，能够提高系统的并发处理能力。

- 解耦：
  - 不使用 Kafka 时，生产者和消费者直接通信，耦合度高，彼此依赖较大。系统扩展和维护困难。
  - 使用 Kafka 时，生产者和消费者通过 Kafka 进行解耦，彼此独立，系统更具灵活性和扩展性。

- 可靠性和持久化：
  - 不使用 Kafka 时，生产者和消费者直接通信，可能存在消息丢失风险，特别是在系统故障或网络不稳定时。
  - 使用 Kafka 时，消息持久化存储，系统故障时仍能恢复数据，确保消息可靠传递。

- 扩展性：
  - 不使用 Kafka 时，生产者和消费者直接通信，扩展系统时需要同时扩展生产者和消费者，复杂度高。
  - 使用 Kafka 时，可以独立扩展生产者和消费者，增加 Kafka broker 来提升系统的处理能力。

- 高可用性：
  - 不使用 Kafka 时，系统依赖单个服务，故障时无法提供服务。
  - 使用 Kafka 时，通过分区和副本机制，确保高可用性，即使某个节点故障，其他副本可以继续服务。

综上所述，Kafka 在电商系统中提供了高效、可靠、可扩展的消息处理能力，解决了同步通信带来的阻塞问题，降低了系统耦合度，提升了系统的可靠性和扩展性。


## Kafka的集群部署
Kafka的版本说明
```shell
kafka_<scala 版本>_<scala 版本>
```

```shell
# 下载Kafka
# Kafka4.0之后不再支持Zookeeper
# Kafka包里集成了Zookeeper，不需要自己单装Zookeeper
wget https://mirrors.tuna.tsinghua.edu.cn/apache/kafka/3.8.0/kafka_2.13-3.8.0.tgz
```