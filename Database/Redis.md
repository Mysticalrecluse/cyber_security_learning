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
Descriptioin=Redis persistent key-value database
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
dirname  dump.rdb  # 默认叫dump.rdb
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
```