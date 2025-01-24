## Redis安装

### 包安装Redis
#### Ubuntu安装Redis
```shell
# 基于官方仓库包安装
# 官网下载地址
https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/

# Ubuntu
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update

# 安装前可以查看当前可安装版本
apt list redis -a

# 直接安装，默认安装最新版
sudo apt-get install redis

# 安装后查看版本
redis-cli -v
```

#### 红帽安装Redis（编译安装）
```shell
# 无官方仓库安装
# 编译安装
# 官方编译源码地址
https://download.redis.io/releases/

# redhat系列安装依赖包
yum -y install gcc make jemalloc-devel systemd-devel

# Ubuntu系列安装依赖包
apt update && apt -y install make gcc libjemalloc-dev libsystemd-dev

# 下载源码
wget https://download.redis.io/releases//redis-7.2.5.tar.gz

# 解压缩并且执行编译
tar -xzvf redis-stable.tar.gz
cd redis-stable

# 执行下面选项，支持systemd
make -j 2 [USE_SYSTEMD=yes] PREFIX=/apps/redis install

# 配置环境变量
echo 'PATH=/apps/redis/bin:$PATH' >> /etc/profile
. /etc/profile

# 也可以直接创建软连接，来配置环境变量
 ln -s /apps/redis/bin/* /usr/local/bin/

# 查看安装目录
[root@localhost /usr/local/src/redis-7.2.5] $ tree /apps/redis/
/apps/redis/
└── bin
    ├── redis-benchmark
    ├── redis-check-aof -> redis-server
    ├── redis-check-rdb -> redis-server
    ├── redis-cli
    ├── redis-sentinel -> redis-server
    └── redis-server

1 directory, 6 files

# 创建相关配置文件目录
mkdir -p /apps/redis/{etc,data,log,run}

# 默认配置文件有问题，需要修改
cp redis.conf /apps/redis/etc/

# 修改配置文件
#dir ./
dir /apps/redis/data   # 配置文件中定义数据目录

# logfile ""
logfilr "/apps/redis/log/redis6379.log"  # 配置日志文件

# pidfile /var/run/redis_6379.pid
pidfile /apps/redis/run/redis_6379.pid  # 配置pid路径

# 重启redis，使其可以读取配置文件
redis-server /apps/redis/etc/redis.conf

# 设置systemd服务
[root@localhost /usr/local/src/redis-7.2.5] $ cat /lib/systemd/system/redis.service 
[Unit]
Description=Redis persistent key-value database
After=network.target

[Service]
ExecStart=/apps/redis/bin/redis-server /apps/redis/etc/redis.conf --supervised systemd
ExecStop=/bin/kill -s QUIT $MAINPID
Type=notify
User=redis
Group=redis
RuntimeDirectory=redis
RuntimeDirectoryMode=0755
LimitNOFILE=1000000

[Install]
WantedBy=multi-user.target

# 创建redis账号
useradd -s /sbin/nologin -r redis
# 授权redis目录
chown -R redis.redis /apps/redis/

# 默认只能访问127.0.0.1本地访问，修改配置文件使其能够远程访问
#bind 127.0.0.1 -::1
bind 0.0.0.0

# 重启
```

### 基于启动时出现的三个告警的优化(面试重点)
#### memory overcommit优化
优化方法
```shell
# 设置内核参数
vm.overcommit_memory = 1  默认为0
# 如果是0，不允许超量承诺使用内存，推荐1
# 将参数写入sysctl
vim /etc/sysctl.conf
vm.overcommit_memory = 1

# 提交
sysctl -p
```

#### TCP backlog优化(全连接队列数量)
```shell
# 告警
WARNING： The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128
# somaxconn 全连接队列数量
# 新版默认4096,大于128，因此无此报警，但是老版本会存在 
```

#### Transparent Huge Pages (THP)透明大页优化
```shell
WARNING you have Transparent Huge Pages (THP) support enabled in your kernel

# 优化
# 建议禁用透明大页，否则会因为缓存页过大，导致延迟
# 新版默认没有开启，因此不告警，老版会默认开启，因此会报警
# 查看
cat /sys/kernel/mm/transparent_hugepage/enabled
[always] madvise never
# 建议设置成never
echo never > /sys/kernel/mm/transparent_hugepage/enabled
# 修改后必须重启redis
systemctl restart redis

# 建议将其添加到/etc/rc.local中，以便在重制后保留设置，禁用HTP后必须重启redis
vim /etc/rc.local
echo never > /sys/kernel/mm/transparent_hugepage/enabled
```

## Redis客户端
```shell
# redis添加了和安全相关的密码验证
# 开启密码验证
# 登录是直接输入验证信息
# redis只需要密码，无用户
redis-cli -a <password>

# 客户端直接访问
redis-cli a 123456 get class

# 查看redis信息分类
[root@localhost ~] $ redis-cli -a 123456 info|grep "^#"
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
# Server ------------- 服务端有关信息
# Clients ------------ 客户端有关信息
# Memory ------------- 内存有关信息
# Persistence -------- 持久化相关信息
# Stats -------------- 状态相关信息
# Replication -------- 复制
# CPU ---------------- CPU
# Modules ------------ 模块
# Errorstats --------- 错误状态
# Cluster ------------ 集群
# Keyspace ----------- 数据空间

# 只看部分信息
redis-cli -a 123456 info <信息类别，比如：server>
# 可以通过这里的信息，配置zabbix监控项
```

### 程序连接Redis



### 图形工具（略）


## Redis常用命令

### INFO

显示当前节点redis运行状态信息
```shell
127.0.0.1:6379 > info

# 只显示部分指定内容
127.0.0.1:6379 > info server
[root@localhost ~] $ redis-cli info server
# Server
redis_version:7.2.5
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:21e21aec7c77abc4
redis_mode:standalone
os:Linux 4.18.0-553.el8_10.x86_64 x86_64
arch_bits:64
monotonic_clock:POSIX clock_gettime
multiplexing_api:epoll
atomicvar_api:c11-builtin
gcc_version:8.5.0
process_id:12534
process_supervised:systemd
run_id:c7f7e3047678ce00c2f9daefe6f38bfe951cdad1
tcp_port:6379
server_time_usec:1719167505474756
uptime_in_seconds:930
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:7891473
executable:/apps/redis/bin/redis-server
config_file:/apps/redis/etc/redis.conf
io_threads_active:0
listener0:name=tcp,bind=0.0.0.0,port=6379
```

### Select 切换数据库

redis默认有16个数据库分别是0-15

使用Select+数据库编号，在数据库间进行切换

```shell
select 0
```

### Key * 

危险命令，可能会造成服务卡顿


### FLUSHDB
```shell
# 清空当前的数据库
flushdb

# 清空所有数据库
flushall

# 生产中建议修改配置使用rename-command禁用此命令
vim /apps/redis/etc/redis.conf
rename-command FLUSHALL ""  #flushdb和AOF功能冲突，需要设置appendonly no,不区分大小写
```

### SHOTDOWN
```shell
关闭redis服务，停止所有客户端连接
```

## Redis配置文件

```shell
bind 0.0.0.0 -::1  # 开启远程监听，默认127.0.0.1仅本地能访问
pidfile /var/.../*.pid  # 指定pid文件路径
databases <num>   # 默认16，可以自定义
tcp-backlog 511   # 指定全连接队列长度
```

### Redis配置文件优化（面试）
- `maxclients 10000` Redis最大连接的客户端数量，默认10000
   - 生产中可以适当调大，使其支持更多连接
   - 产生客户端连接的可能场景
     - 业务侧连接：应用程序（Web，后台服务）与Redis的连接
     - 用户侧连接：用户通常不会直接连接Redis，但是用户的操作会间接通过应用程序连接到Redis（例如：用户在网站上进行搜索，应用程序会向Redis查询缓存数据）
```扩展
通过对Redis指标进行监控`INFO clients`，发现连接数频繁达到maxclients限制,就需要考虑对其进行优化，防止影响业务
优化手段
1. 增加mxclients的数量，来允许更多的客户端连接
2. 使用连接池技术，复用一组连接，减少频繁创建和销毁连接的开销 从而更高效地使用连接资源
3. 负载均衡：使用Redis Cluster或多个Redis实例进行负载均衡，分散客户端连接到多实例
4. 优化应用程序的Redis连接策略（比如：设置timeout，让Redis自动关闭空闲时间超过指定秒数的连接，以减少连接数）
```
- `maxmemory <bytes>` 最大使用内存数,0表示不限制
   - 生产中可以限制一下，建议设置成当前物理内存的一半，注意：缓冲区不计算在maxmemory内，生产中如果不设置该项，可能导致OOM

- `memory-policy` 内存使用策略（当达到内存时，Redis如何处理要删除的内容）【面试可能会问】
   - allkeys-lru：在所有键中使用 LRU（Least Recently Used）算法进行淘汰。
      - 【使用场景】适用于一般缓存场景，优先淘汰最久未使用的键，确保最近使用的数据保留。
      - 可以有效利用内存，保持高命中率。
   - volatile-lru：在设置了过期时间的键中使用 LRU 算法进行淘汰。
      - 【使用场景】适用于只希望淘汰有过期时间的缓存数据，而保留永久性数据的场景
      - 能够在有限内存中优先保留永久性数据。
   - allkeys-lfu:在所有键中使用 LFU（Least Frequently Used）算法进行淘汰。
      - 【使用场景】适用于热点数据明显的场景，确保高频访问的数据保留
   - noeviction：当内存使用达到限制时，不会再接受新的写入请求，返回错误。
      - 【使用场景】适用于需要确保数据不会被自动删除的场景，比如缓存中存储了非常重要且不能丢失的数据。

## CONFIG命令实现动态修改配置【热加载】
### 设置客户端连接密码
```shell
# 设置连接密码
CONFIG SET requirepass 123456

# 查看连接密码
CONFIG GET requirepass
```

### 查看所有配置
```shell
CONFIG GET *
```

### 设置Redis使用的最大内存量
```shell
CONFIG SET maxmemory 1000000000，默认以字节为单位
```


## 慢查询
```shell
# 查询慢查询触发条件，即超过多久触发慢查询，默认以微秒为单位，默认10000us 10ms
CONFIG get slowlog-log-slower-than
```

### 开启慢查询
```shell
# 在配置文件中开启慢查询
vim /etc/redis.conf
slowlog-log-slower-than 1    # 指定超过1us的即为慢查询，默认10000un，即10ms
slowlog-max-len 1024         # 指定只保存最近的1024条慢记录，默认为128

slowlog-max-len # 默认128

# 查看慢查询指令
SLOWLOG LEN     # 查询慢的指令数量
SLOWLOG GET     # 查询所有
SLOWLOG GET [n] # 查n个查询指令

# 示例
27.0.0.1:6379> slowlog len
(integer) 2
127.0.0.1:6379> slowlog get
1) 1) (integer) 1
   2) (integer) 1719170693     # 第2）行表示执行命令的时间戳
   3) (integer) 13             # 第3）行表示每条指令的执行时长
   4) 1) "set"
      2) "name"
      3) "zhangyifeng"
   5) "127.0.0.1:44390"
   6) ""
2) 1) (integer) 0
   2) (integer) 1719170672
   3) (integer) 14
   4) 1) "config"
      2) "set"
      3) "slowlog-log-slower-than"
      4) "10"
```

## Redis持久化

Redis是基于内存型的NoSQL和MySQL是不同的，使用内存进行数据保存
如果想实现数据的持久化，Redis也可以支持内存数据保存到硬盘

Redis支持两种数据持久化保存方法
- RDB：Redis DataBase （全量）
- AOF：AppendOnlyFile （增量）



### RDB工作原理

RDB会尝试将内存中的所有数据全部存到硬盘上，存储路径有配置文件中的dir指定
```shell
vim /apps/redis/etc/redis.conf
dir /apps/redis/data  # 定义rdb存储的路径
# 指定文件名
dirname  dump.rdb  # 默认叫dump.rdb，dump.rdb为二进制文件
```

#### 手动触发备份
```shell
# 手动触发备份
# 方法1：同步，同步期间会占用线程，慎重使用，因为redis是单线程
SAVE
# 方法2：后台备份，会生成一个独立的子进程用来在后台运行
BGSAVE  
# 持久化备份信息
rdb_bgsave_in_progress:0 # 0表示备份完了，1表示没备份完了

# redis启动时，会自动从dump.rdb文件中加载数据
```
注意：备份的重点：异地备份，比如：拷贝到远程主机

实际工作中可能出现的问题：
1. 备份的时候，可能无法判断备份的数据是新文件还是旧文件，因为在备份时，会产生一个tump.rdb的临时文件，当备份完成后，才会替代原备份文件
此时，备份数据后同时拷贝到远程主机可能无法保证拷贝的是新文件还是旧文件，即文件是否备份完成

解决方案：写个脚本，循环判断`rdb_bgsave_in_progress`是否为0，当值为0，表示备份完成，再进行异地拷贝
```shell
# 判断是否备份完成
until [ $result -eq 0] ; do
    sleep 1
    result = `redis-cli -a $PASS --no-auth-warning info Persistence | awk -F: '/rdb_bgsave_in_progress/{print $2}'`
done

# 备份完成后，后续可以使用scp进行异地拷贝
```

2. 写个计划任务，每个小时备份一次数据
```shell
0 * * * * redis-cli -a 123456 bgsave
```


#### 自动触发备份
```shell
# redis自动触发备份，使用save策略
save <seconds> <changes> [<seconds> <changes>...]

# 查看策略
config get save
# 默认 save 3600 1 300 100 60 10000
# 老版本必须分行写
# 老版本示例
save 3600 1
save 300 100
save 60 10000
```


### AOF
#### AOF工作原理 
AOF即AppendOnlyFile，采用COW机制
AOF可以指定不同的保存策略，默认为每秒执行一次fsync，按照操作的顺序地将变更命令追加至指定的AOF日志文件尾部
在第一次启动AOF功能时，会做一次完全备份，后续将执行增量备份，相当于完全数据备份+增量变化
如果同时启用RDB和AOF，进行恢复时，默认AOF文件优先级高于RDB文件，即会使用AOF文件进行恢复

注意：AOF模式默认是关闭的，第一次开启AOF后，并重启服务生效后，会因为AOF的优先级高于RDB，而AOF默认没有数据文件存在，从而导致所有数据丢失

正确启用AOF功能，防止数据丢失
```shell
# 热加载启用AOF
redis-cli -a 123456
config set appendonly yes  # 自动触发AOF重写，会自动备份所有数据到AOF文件
# 生成appendonly.aof

# 然后再在配置文件中开启AOF
vim /etc/redis.conf
appendonly yes
```

#### AOF相关配置
```shell
appendfilename "appendonly.aof"  #文本文件AOF的文件名，存放在dir指令指定的目录中
appenddirname "appendonlydir"    #7.X 版指定目录名称

# AOF的持久化策略配置
appendfsync everysec  
#no表示由操作系统保证数据同步到磁盘,Linux的默认fsync策略是30秒，最多会丢失30s的数据
#always表示每次写入都执行fsync，以保证数据同步到磁盘,安全性高,性能较差
#everysec表示每秒执行一次fsync，可能会导致丢失这1s数据,此为默认值,也生产建议值

# rewrite相关
no-appendfsync-on-rewrite yes
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
aof-load-truncated yes
```



#### AOF启动后的文件解析

```bash
[root@mystical ~]# tree /apps/
/apps/
└── redis
    └── data
        ├── appendonlydir
        │   ├── appendonly.aof.1.base.rdb
        │   ├── appendonly.aof.1.incr.aof
        │   └── appendonly.aof.manifest
        └── dump.rdb
        
# 查看
[root@mystical ~]# ll /apps/redis/data/appendonlydir/
total 16
drwxr-x--- 2 redis redis 4096 Jan 15 09:59 ./
drwxr-xr-x 3 redis redis 4096 Jan 15 09:59 ../
-rw-rw---- 1 redis redis   88 Jan 15 09:59 appendonly.aof.1.base.rdb
-rw-r----- 1 redis redis    0 Jan 15 09:59 appendonly.aof.1.incr.aof
-rw-r----- 1 redis redis   88 Jan 15 09:59 appendonly.aof.manifest
```



**`appendonly.aof.1.base.rdb`**

- **作用：**
  - 这是一个 RDB 格式的文件，代表 AOF 的基础快照。Redis 在某个时间点上创建该文件以保存当前数据集的完整状态。
  - 当 Redis 启用混合持久化（AOF + RDB 混合模式）时，这个文件用于存储初始的数据库状态。
  - 在恢复过程中，Redis 首先加载此文件，然后再应用增量 AOF 文件的命令来还原完整数据集。
- **特性：**
  - 文件内容是二进制格式，与标准 RDB 文件类似。
  - 在 AOF 重写过程中，Redis 会生成或更新该文件。

------

**`appendonly.aof.1.incr.aof`**

- **作用：**
  - 这是增量 AOF 文件，存储了自 `appendonly.aof.1.base.rdb` 生成之后的写入命令。
  - 文件以 AOF 格式（命令行形式）记录 Redis 的写操作。
  - 在恢复时，Redis 会按顺序应用这些写命令到基础 RDB 快照上，确保数据的完整性。
- **特性：**
  - 文件可能非常小（例如为 0 字节），如果没有写入操作或刚完成了 AOF 重写。
  - 每次新的写操作会追加到此文件中。

------

**`appendonly.aof.manifest`**

- **作用：**

  - 这是 AOF 文件的元数据清单，描述了 Redis 如何组合使用上述文件来恢复数据。
  - 文件内容列出了所有参与恢复的数据文件（基础 RDB 和增量 AOF 文件）及其顺序。

- **内容示例：**

  ```
  txtCopy codefile appendonly.aof.1.base.rdb
  file appendonly.aof.1.incr.aof
  ```

  - **`file`** 表示要加载的文件。
  - 加载顺序从上到下，Redis 会先加载 `base.rdb`，然后应用 `incr.aof`。

------

**工作流程**

1. Redis 在启动时，首先读取 `appendonly.aof.manifest` 文件。
2. 按照清单文件的顺序加载 `appendonly.aof.1.base.rdb` 快照。
3. 应用 `appendonly.aof.1.incr.aof` 中的命令以还原增量数据。
4. 恢复完成后，Redis 开始正常运行。

------

**为什么分为多个文件？**

- 提高性能：
  - RDB 格式文件的生成效率高，减少了单一大型 AOF 文件的写入开销。
- 提高恢复效率：
  - 加载 RDB 文件速度比逐行解析 AOF 文件快得多。
- 简化管理：
  - 将基础数据与增量数据分开，可以更灵活地进行文件操作（如压缩或备份）。



### AOF日志格式

```shell
# set testkey testvalue的日志格式
*3                  # 这个3意味着当前命令有3个部分
$3                  # 每部分都是有“$+数字”
set                 # 
$7
testkey
$9
testvalue
```

#### AOF重写（清理）
将一些重复的，可以合并的，过期的数据重新写入一个新的AOF文件，从而节约AOF备份占用的硬盘空间，也能加速恢复过程，可以手动执行`bgwriteaof`触发AOF，第一次开启AOF功能，或定义自动rewrite策略

#### AOF rewrite过程

1. 首先执行指令`bgwriteaof`
2. 指令发送给父进程
3. 父进程fork一个子进程
4. 初始阶段，主进程和子进程共享内存空间，但该内存空间对于子进程是只读的，子进程基于此进行数据读取，重写并保存到新的文件
5. 如果有新的数据写入主进程，且该数据在之前已存在，则主进程复制该数据所在的内存页 ，并在复制的内存页上更改此数据，并保存到aof_buf
6. 同时主进程将数据拷贝一份到aof_rewrite_buf，等待数据重写后，追加到新生成的aof文件中
7. 当数据重写结束，子进程给主进程一个信号，然后将新的aof替代就得aof，然后子进程释放

#### 手动触发AOF
```shell
redis-cli -a 123456 bgrewriteof ; pstree -p | grep redis; ll /apps/redis/data/appendondir/

vim /apps/redis/etc/redis.conf
auth-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
```

## 消息队列

### 生产者消费者模式

生产者消费者模式下，多个消费者同时监听一个频道(redis用队列实现)，但是生产者产生的一个消息只能被最先抢到消费的一个消费者消费一次，队列中的消息由可以多个生产者写入，也可以由不同的消费者取出进行消费处理，此模式应用广泛

#### 生产者生成消息
```shell
LPUSH channel1 message1
LPUSH channel1 message2
LPUSH channel1 message3
LPUSH channel1 message4
LPUSH channel1 message5
```

#### 获取所有消息
```shell
LRANGE channel1 0 -1
message5
message4
message3
message2
message1
```


#### 消费者消费消息
```shell
RPOP channel1  
# message1
RPOP channel1
# message2
RPOP channel1
# message3
RPOP channel1
# message4
RPOP channel1
# message5
```

### 发布者订阅者模式

#### 订阅者订阅频道
```shell
SUBSCRIBE channel01 # 订阅者实现订阅指定频道，之后发布的消息才能收到
```

#### 发布者发布消息
```shell
PUBLISH channel01 message1 # 发布者发布信息到指定频道
# 发布者发布的消息，所有订阅者都能收到
```

#### 可以同时发布多个频道的信息，支持通配符
```shell
PUBLISH channel01 channel02 channel*
```

#### 取消订阅
```shell
unsubscribe channel01
```

## Redis高可用与集群

### Redis主从复制

主从复制特点
- 一个master可以有多个slave
- 一个slave只能有一个master
- 数据流向是从master到slave单向的
- master可读可写
- slave只读

### 主从复制实现
当master出现故障后，可以自动提升一个slave节点变成新的master，因此Redis Slave需要设置和master`相同的连接密码`
此外当一个Slave提升为新的master的时候，需要通过持久化实现数据的恢复

#### 启用主从同步
Redis Server 默认为master节点，如果要配置从节点，需要指定master服务器的IP，端口以及链接密码
```shell
# 新版Reids，从节点
REPLICAOF MASTER_IP PORT

# 旧版将被淘汰
SLAVEOF MASTERIP PORT

# 指明主节点密码
CONFIG SET masterauth <masterpass>

# 集群中，建议所有主节点，从节点，都设置相同的requirepass和masterauth

# 配置好后，查看身份
role
redis-cli -a 123456 role

# 查看同步状态
redis-cli -a 123456 info replication
master_sync_in_progress: 0    # 0表示同步完成，1表示同步中，还未完成

# 所有从节点默认只读

# 从节点从主从状态变为独立节点
REPLICAOF NO ONE  # 临时取消，要永久生效修改配置文件
```

### 主从复制优化

#### 主从复制过程

Redis主从复制分为全量同步和增量同步

主节点重启会导致`全量同步`, 从节点重启会导致`增量同步`

复制过程详解
- 主从节点建立连接，验证身份后，从节点向主节点发送PSYNC(2.8版本之前是SYNC)命令
- 主节点向从节点发送FULLRESYNC命令，包括master_replid(runID)和offset
- 从节点保存主节点信息
- 主节点执行BGSAVE保持RDB文件，同时记录新的记录到buffer中
- 主节点发送RDB文件给从节点
- 主节点将新收到的buffer中的记录发送至从节点
- 从节点删除本机的旧数据
- 从节点加载RDB
- 从节点同步主节点的buffer信息

全量复制发生在下面情况
- 从节点首次连接主节点
- 从节点的复制偏移量不在复制挤压缓冲区内
- 从节点无法连接主节点超过一定时间
- replicid变了，即主节点重启过，之后一定发生全量复制


#### 主从复制优化
- 第一次全量复制不可避免，后续的全量复制可以利用小主节点（内存小），业务低峰时进行全量
- 节点RUN_ID不匹配，主节点重启会导致RUN_ID变化，从而触发全量备份，可以利用config动态修改配置
- 复制积压缓冲区不足，当主节点生成的新数据大于缓冲区大小，从节点恢复和主节点连接后，会导致全量复制，解决方法将`repl-backlog-size`调大

#### 避免复制风暴
- 单主节点复制风暴
   - 当主节点重启，多节点复制
   - 解决方法：更换复制拓扑，可以换成级联复制，这样只有一个从节点全量复制，后面的都是增量复制

- 单机器多实例复制风暴
   - 机器宕机后，大量全量复制
   - 解决方法：主节点分散多机器
   - Redis建议小内存，多实例o

#### 多实例实现方法

- /bin目录二进制文件共用
- 其他的数据，日志，配置，pid文件以及service文件都复制，每个实例复制一份
- 还可以使用docker，更简单，直接使用多容器


#### 主从同步优化配置

Redis在2.8版本之前没有提供增量部分复制的功能，当网络闪断或者slave Redis重启之后会导致主从之间的全量同步，即从2.8版本开始增加了部分复制功能

```shell
repl-diskless-sync no  # 是否使用无盘方式进行同步RDB文件，默认为no（编译安装为yes），no表示不使用无盘，需要将RDB文件保存到磁盘后再发送给slave，yes表示使用无盘，即RDB无需保存到本地磁盘，而是直接通过网络发送给slave

repl-disless-sync-delay 5 # 无盘时复制的服务器等待的延迟时间

repl-ping-slave-preiod 10 # slave向master发送ping指令的时间间隔，默认为10s

repl-timeout 60   # 指定ping连接超时时间，超过此值无法连接，master_link_status显示为down状态，并记录错误日志

repl-disable-tcp-nodelay no # 是否启动TCP_NODELAY
# 设置成yes，则redis会合并多个小的tcp包打包成一个大包再发送，此方式可以节省带宽，但会造成同步延迟时长增加，导致master与slave短期不一致，设置成no，则master会立即同步数据

repl-backlog-size 1mb  # 建议此值是设置的足够大，如果此值太小，会造成全量复制

repl-backlog-ttl 3600 # 指定多长时间后如果没有slave连接到master，则backlog的内存数据将会过期，如果值为0，表示永不过期

slave-priority 100 # slave参与选择新的master的优选级，此整数值越小，优先级越高。如果值为0，表示slave永远不会被选为master节点

min-replicas-to-write 1 # 指定master的可用salve不能少于个数，如果少于此值，master将无法重写执行操作，默认值为0，生产建议波动1.5
```

### Reddis哨兵(Sentinel)

#### Redis哨兵实现故障转移的原理

#### Sentinel中的三个定时任务
- 每10秒每个sentinel对master和slave执行info
   - 发现slave节点
   - 确认主从关系
- 每2秒每个sentinel通过master节点的channel交换信息(pub/sub)
   - 通过sentinel_:hello频道交互
   - 交互对节点的“看法”和自身信息
- 每1秒每个sentinel和其他sentinel和redis执行ping

#### 哨兵实现
sentinel配置

Sentinel实际上是一个特殊的redis服务器，有些redis指令支持，但很多指令并不支持，默认监听在26379/tcp端口
哨兵服务可以和redis服务器分开部署，但为了节约成本一般会部署在一起

```shell
# 哨兵的本质是redis-server的软连接
# 基于包安装的sentinel
apt install -y redis-sentinel  # 配置文件sentinel.conf在/etc/目录下

# 基于编译安装
直接解压后，里面有sentinel.conf，拷贝到指定etc/目录下

# 修改哨兵的配置文件
bind 0.0.0.0
port 26379
daemonize yes
pidfile "redis-sentinel.pid"
logfile "sentinel_26379.log"
dir "/tmp"  # 工作目录

sentinel monitor mymaster 10.0.0.108 6379 2
# mymaster是集群的名称，此行指定当前mymaster集群中master服务器的地址和端口
# 2为法定人数限制(quorum)，即有几个sentinel认为master down了就进行故障转移，一般此值是所有sentinel节点的一半以上的整数值
# 是master的ODOWN客观下线依据

sentinel auth-pass mymaster 123456
# mymaster集群中master的密码，注意此行要在上面行的下面，注意，要求这组redis主从复制所有节点的密码相同

sentinel down-after-milliseconds mymaster 30000
# 判断mymaster集群中所有节点的主观下线(SDOWN)时间，单位：毫秒，建议3000

sentinel parallel-syncs master 1
# 发生故障转移后，可以同时向新master同步数据的slave的数量，数字越小说明总同步时间越长，但可以减轻新master的负载压力

sentinel failover-timeout mymaster 180000
# 所有slaves指向新的master所需要的超时时间，单位：毫秒

sentinel deny-scripts-reconfig yes # 禁止修改脚本
```

#### Sentinel运维

在Sentinel主机手动触发故障切换
```shell
sentinel failover <mastername>
```

可以通过调整优先级数值`replica-priority`来指定故障切换时，优先切换的从节点

#### python上对于哨兵模式的使用
```python
import redis
from redis.sentinel import Sentinel

# 连接哨兵服务器(主机名也可以用域名)
# 因为故障转移，所以主节点的ip并不固定，所以通过哨兵来确认当前哪个ip是主节点
sentinel = sentinel ([('10.0.0.206', 26379),
                     ('10.0.0.204', 26379),
                     ('10.0.0.203', 26379)
                     ], socket_timeout=0.5)

redis_auth_pass='123456'

# mymaster是运维人员配置哨兵模式的的数据库名称，实际名称按照个人部署决定
# 获取主服务地址
master=sentinel.discover_master('mymaster')
print(master)

# 获取从服务器地址
slave=sentinel.discover_slaves('mymaster')
print(slave)

 



# 获取从服务器进行读取（默认是round-roubin）
slave=sentinel.slave_for('mymaster', socket_timeout=0.5,password=redis_auth_pass, db=0)
r_ret = slave.get('name')
print(r_ret)
```

#### 哨兵机制总结

哨兵机制大抵涉及3个问题
- 主库真的挂了吗
- 该选择哪个从库作为主库
- 怎么把新主库的相关信息通知给从库和客户端


上述问题对应着哨兵的三个任务
- 监控
  - 哨兵进程在运行时，周期性给所有主从库发送ping命令，检测它们是否在线
  - 判断主库是否在线的机制：
    - 哨兵采用多实例组成的集群模式进行部署，即哨兵集群
    - 通过多个哨兵共同判断，当主观下线的数量超过了n/2时，则判定为客观下线
- 选主
  - 当主库挂了之后，哨兵需要从很多个从库里，`按照一定的规则`，选择一个从库实例，把它作为主库
  - 选择新主的过程“筛选+打分”
    - 筛选：按照`一定`的筛选条件，把不符合条件的从库去掉
      - 从库正常在线，且网络连接状态良好
        - 判断网络连接状态不好的依据：在`down-after-milliseconds`毫秒内，发生断连的次数超过10次
    - 打分：按照`一定`的规则，给剩下的从库逐个打分,将得分最高的从库选为新主库
      - 按照三个规则，依次进行三轮打分
        - 第一轮：`优先级`最高的从库得分高，如果优先级相同，则进入第二轮打分
        - 第二轮：`和旧主库同步程度最接近的得分高`
          - 在主从库同步的过程中，主库会用`master_repl_offset`记录当前的最新写操作在repl_backlog_buffer中的位置
          - 从库使用`slave_repl_offset`记录当前的复制进度
          - `slave_repl_offset`和`master_repl_offset`最接近的则判断得分高，如果同步程度相同，则进入第三轮打分
        - 第三轮：从库ID号小的打分高
- 通知
  - 哨兵会把新主库的连接信息发给其他从库。让它们执行replicaof命令，和新主库建立来连接，并进行数据复制
  - 哨兵把新主库的连接信息通知给客户端，让它们把请求操作发到新主库上


### 哨兵集群的组成和运行机制

#### 哨兵集群间建立通信的原理
哨兵实例之间可以相互发现，归功于Redis提供的`pub/sub`，也就是`发布订阅机制`

- 哨兵先和主库建立联系（在配置项上`sentinel monitor mymaster 10.0.0.206 6379 2`）
- 建立了联系就可以在主库上发布消息，比如`发布它自己的连接信息（IP和端口号）`
- 也可以从主库订阅消息，获得其他哨兵发布的连接信息。
- 也就是说先在主库上订阅相同的频道，然后发布信息，每个哨兵都能收到这个频道上的消息，也就得到了彼此的IP地址和端口号
- 这个频道就是`__sentinel__:hello`
- 在这个频道得到彼此的IP和端口号后就可以互相通过网络进行通信，比如：`对主库有没有下线进行判断和协商`

#### 哨兵如何的到从库的信息

- 哨兵向主库发送INFO命令来完成，主库会接受到INFO命令后，将从库列表返回
- 接着，哨兵可以根据从库列表中的连接信息，和每个从库建立连接，并在这个连接上持续对从库进行监控
```shell
[root@ubuntu2204 redis]#redis-cli -a 123456 info replication
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
# Replication
role:master
connected_slaves:2
# 可以拿到从库的IP和端口号
slave0:ip=10.0.0.203,port=6379,state=online,offset=2939656,lag=0
slave1:ip=10.0.0.206,port=6379,state=online,offset=2939656,lag=0
master_replid:b3ce242dd27e5f5703da2f9a17b28e840cfc3110
master_replid2:693d43b96e9ee68f710fe8cff04597b26be466cf
master_repl_offset:2939656
second_repl_offset:7491
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1891081
repl_backlog_histlen:1048576
```

#### 哨兵如何和客户端建立连接（告诉客户端当前主库的信息）

每个哨兵实例也提供`PUB/SUB`机制，客户端可以从哨兵订阅消息，从而得到需要的信息。

哨兵提供的信息订阅频道有很多，不同的频道包含了主从库切换过程中的不同关键事件
```shell
相关频道
# 主库下线事件
+sdown (实例进入“主观下线状态”)
-sdown (实例退出“主观下线”状态)
+odown (实例进入“客观下线”状态)
-odown (实例退出“客观下线”状态)
# 从库重新配置事件
+slave-reconf-sent (哨兵发送SLAVEOF命令重新配置从库)
+slave-reconf-inprog (从库配置了新主库，但尚未进行同步)
+slave-reconf-done (从库配置了新主库，且和新主库完成同步)
# 新主库切换
+switch-master (主库地址发生变化)
```

可以在客户端通过订阅来观察所有事件的频道发布的信息


## Redis Cluster
解决主从架构的单节点性能瓶颈问题，实现负载均衡

### 集群Cluster架构的缺陷
- 不支持换库，即Redis有默认有16个数据库，但是集群模式下，只能用一个，不能切换
- 不支持同时对多个值赋值，即以下用法不支持，会报错
```shell
mset a 1 b 2 c 3
# 在Cluster模式下会报错
```

### Redis Cluster架构

Redis Cluster需要至少3个master节点才能实现，slave节点数量不限，当然一般每个master都至少对应一个slave节点

#### 数据分区：虚拟槽分区

Redis Cluster设置0~16383的槽，每个槽映射一个数据子集，通过hash函数，将数据存放在不同的槽位中，每个集群的节点保存一部分的槽

每个Key存储时，先经过算法函数CRC16(key)得到一个整数，然后整数与16384取余，得到槽的数值，然后找到对应的节点，将数据存放入对应的槽中

CRC16算法
```shell
CRC（循环冗余检测算法）是一种错误检测码，通过一系列数学运算生成一个检验值（校验码）。
校验码满足确定性，即确保相同的输入始终产生相同的输出，以此进行数据的验证
```

#### 集群通信



### Redis Cluster集群实现
- 6台设备上所有配置文件初始相同，全部开启集群模式
```shell
# 每个节点修改redis配置，必须开启cluster功能的参数
# 手动修改配置文件
vim /etc/redis/redis.conf
bind 0.0.0.0
requirepass 123456
masterauth 123456
cluster-enabled yes # 取消此行注释，必须开启集群，开启后，redis进程会有cluster标识
cluster-config-file nodes-6379.conf # 取消此行注释，此为集群状态数据文件，记录主从关系及slot范围信息，由redis cluster集群自动创建和维护
cluster-require-full-coverage no # 默认值为yes，设为no可以防止一个节点不可用导致的整个cluster不可用（如果是yes的话，在集群中，只要有一组主从不可用，则整个集群停止服务）
```

- 在将所有节点加入同一个集群中
```shell
# 下面命令在集群节点或任意节点执行皆可，命令redis-cli的选项，
# --cluster-relicas 1表示每个master对应一个slave节点，注意，所以节点数据必须清空
redis-cli -a 123456 --cluster create 10.0.0.8:6379 10.0.0.18:6379 10.0.0.28:6379 10.0.0.38:6379 10.0.0.48:6379 10.0.0.58:6379 --cluster-replicas 1
# 前面的是主节点，后面的是从节点，1表示一对一
# 后面输入yes，自动分槽位

# -c 表示自动查找该key应该存到哪个槽位，然后存过去
# 因为每次写入数据，都可能定位到新的节点，都会涉及查询后保存，所以性能肯定比单机差
# 但是如果用户量很大的话，多个设备整体的效率是要高过单机的
redis-cli -a 123456 -c

# 查看集群中具体节点状态
redis-cli -a 123456 --cluster info 10.0.0.38:6379
```

#### 使用python操作集群
```python
# 配置python加速
python3 -m pip config set global.index-url https://mirrors.aliyun..com/pypi/simple
python3 -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# pip3 install redis-py-cluster

from rediscluster import RedisCluster
startup_nodes = [
   {"host":"10.0.0.200","port":6379},
   {"host":"10.0.0.201","port":6379},
   {"host":"10.0.0.202","port":6379},
   {"host":"10.0.0.203","port":6379},
   {"host":"10.0.0.204","port":6379},
   {"host":"10.0.0.205","port":6379},
]

redis_conn = RedisCluster(startup_nodes=startup_nodes,password='123456',decode_responses=True)

for i in range(0,10000):
   redis_conn.set('key'+str(i),'value'+str(i))
   print('key'+str(i)+':',redis_conn.get('key'+str(i)))
```

注意：Cluster集群模式下，从节点仅做备份，读写都从主节点进行

#### 集群操作
```shell
# 查询单个槽位上的数据,查询有几个key
redis-cli -a 123456 cluster countkeysinslot [num]
```


#### 集群数据偏斜问题
```shell
# 查询大key
redis-cli -a 123456 --bigkeys
# 如果多个节点上的槽位中的数据很不平衡，可以使用命令重新分配
# 执行自动的槽位重新平衡分布，会影响客户端访问，慎用
redis-cli -a 123456 --cluster rebalance 10.0.0.8:6379
```


## Redis Cluster管理

### 集群扩容

增加Redis新节点，需要与之前的Redis node版本和配置一致，然后分别再启动两台Redis node，应为一主一从。

#### 添加新master节点到集群
使用以下命令添加新节点，要添加的新redis节点IP和端口添加到已有的集群中任意节点的IP端口
```shell
# 该命令可以再任意机器上执行
redis-cli -a 123456 --cluster add-node new_host:newport existing_host:existing_port [--slave --master-id <arg>]
# new_host:new_port             指定新添加的主机IP和端口
# existing_host:existing_port   指定已有的集群中任意节点的IP和端口

# 移动槽位
redis-cli -a 123456 --cluster reshard <当前任意集群节点>:6379
.... 
[OK] All 16384 slots covered
How many slots do you want to move (from 1 to 16384)? 4096
What is the receiving node ID? <填写新加入节点的node ID>
Please enter all the source node IDs
   Type 'all' to use all the nodes as source nodes for the hash slots
   Type 'done' once you entered all the source nodes ID.
Source node #1: all  （从所有设备上将槽位匀给新加入的设备）
...
# 敲yes开始挪动槽位
```

把从节点加进来
```shell
redis-cli a 123456 --cluster add-node <新加节点IP:端口> <任意集群节点IP:端口> --cluster-slave --cluster-master-id <主节点node ID>
```

#### 集群节点缩容
```shell
redis-cli -a 123456 --cluster reshard <当前任意集群节点>:6379
[OK] All 16384 slots covered
How many slots do you want to move (from 1 to 16384)? 1365
What is the receiving node ID? <要接收的node ID>
Please enter all the source node IDs
   Type 'all' to use all the nodes as source nodes for the hash slots
   Type 'done' once you entered all the source nodes ID.
Source node #1: <要退出的node ID>
Source node #2: done
...
# 确认yes
...

# 分批将所有的槽点都分给集群其他node之后，此时该节点中的槽位清空
# 节点清空后将其踢出集群
redis-cli -a 123456 --cluster del-node <任意集群节点的IP>:b379 <删除的节点IP>
```
#### 导入现有数据到集群

- 迁移前基础环境准别
```shell
# 集群中所有节点关闭保护模式，清空密码
# 1. 关闭保护模式，2. 清空密码
redis-cli -a 123456 config set protected-mode no
# 在所有节点(源节点和集群节点)关闭各redis密码认证
redis-cli -a 123456 --no-auth-warning CONFIG SET requirepass ""
```

- 执行数据导入操作（这个任务慎重，尽量交给别人干）
```shell
redis-cli --cluster import <集群任意节点服务器IP:Port> --cluster-from <外部Redis node-IP:Port> --cluster-copy --cluster-replace
# 只使用cluster-copy，则要导入集群中的key不能存在
# 如果集群中已有同样的key，如果需要替换，可以--cluster-copy --cluster-replace联用，这样集群中的key就会被替换为外部数据
```

- 还原安全配置
```shell
# 动态修改
# 在所有节点（源节点和集群节点）还原redis密码认证
redis-cli -p 6379 --no-auth-warning CONFIG SET requirepass "123456"

# 还原配置protected-mode
redis-cli -a 123456 config set protected-mode yes
```