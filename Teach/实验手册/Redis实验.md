# 实验1：Redis安装部署



## 包安装Redis

### Ubuntu安装Redis

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

## 红帽安装Redis（编译安装）

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

## 基于启动时出现的三个告警的优化(面试重点)

### memory overcommit优化

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



### TCP backlog优化(全连接队列数量)

```shell
# 告警
WARNING： The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128
# somaxconn 全连接队列数量
# 新版默认4096,大于128，因此无此报警，但是老版本会存在 
```



### Transparent Huge Pages (THP)透明大页优化

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

# 建议将其添加到/etc/rc.local中，以便在重制后保留设置，禁用THP后必须重启redis
vim /etc/rc.local
echo never > /sys/kernel/mm/transparent_hugepage/enabled
```





# 实验2：Redis主从复制

```bash
# 集群中，建议所有主节点，从节点，都设置相同的requirepass和masterauth
[root@ubuntu2204 redis6379]#vim /apps/redis6379/etc/redis.conf
masterauth 123456
requirepass 123456

# 从节点配置
[root@ubuntu2204 ~]#vim /apps/redis6379/etc/redis.conf
replicaof 10.0.0.203 6379

# 重启后查看从服务器身份
[root@ubuntu2204 ~]#systemctl restart redis
[root@ubuntu2204 ~]#redis-cli -a 123456 role
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
1) "slave"
2) "10.0.0.203"
3) (integer) 6379
4) "connected"
5) (integer) 28

# 查看主服务器身份
[root@ubuntu2204 redis6379]#redis-cli -a 123456 role
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
1) "master"
2) (integer) 182
3) 1) 1) "10.0.0.202"
      2) "6379"
      3) "182"
```





# 实验3：Redis哨兵

```bash
# 3台服务器
# 主服务器：10.0.0.203
# 从服务器：10.0.0.202
# 从服务器：10.0.0.204

# 在三台服务器配置redis
[root@ubuntu2204 ~]# curl -fsSL https://www.mysticalrecluse.com/script/Shell/install_redis_binary.sh | bash

# 配置10.0.0.203主服务器
[root@ubuntu2204 etc]# vim /apps/redis6379/etc/redis.conf
masterauth 123456
requirepass 123456
bind 0.0.0.0

# 配置10.0.0.202主服务器
[root@ubuntu2204 etc]# vim /apps/redis6379/etc/redis.conf
masterauth 123456
requirepass 123456
bind 0.0.0.0
replicaof 10.0.0.203 6379

# 配置10.0.0.204主服务器
[root@ubuntu2204 etc]# vim /apps/redis6379/etc/redis.conf
masterauth 123456
requirepass 123456
bind 0.0.0.0
replicaof 10.0.0.203 6379


# 在 10.0.0.203 服务器配置sentinel
# 将sentinel.conf文件拷贝到etc/目录下
[root@ubuntu2204 ~]#cp /usr/local/src/redis-7.2.5/sentinel.conf /apps/redis6379/etc/

# 修改哨兵配置文件
[root@ubuntu2204 ~]#vim /apps/redis6379/etc/sentinel.conf 
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

# 将配置文件复制到其他所有哨兵所在服务器上
[root@ubuntu2204 ~]#scp /apps/redis6379/etc/sentinel.conf 10.0.0.202:/apps/redis6379/etc/
[root@ubuntu2204 ~]#scp /apps/redis6379/etc/sentinel.conf 10.0.0.204:/apps/redis6379/etc/

# 创建service文件接管redis-sentinel
[root@ubuntu2204 redis6379]#vim /lib/systemd/system/redis-sentinel.service
[Unit]
Description=Redis Sentinel
After=network.target
[Service]
Type=notify
ExecStart=/apps/redis6379/bin/redis-sentinel /apps/redis6379/etc/sentinel.conf --supervised systemd
ExecStop=/bin/kill -s QUIT $MAINPID
User=redis
Group=redis
RuntimeDirectory=redis
Mode=0755
[Install]
WantedBy=multi-user.target

# 将service文件复制到其他所有哨兵所在服务器上
[root@ubuntu2204 redis6379]#scp /lib/systemd/system/redis-sentinel.service 10.0.0.202:/lib/systemd/system/
[root@ubuntu2204 redis6379]#scp /lib/systemd/system/redis-sentinel.service 10.0.0.204:/lib/systemd/system/

# 记得将配置文件和数据目录添加权限
[root@ubuntu2204 redis6379]#mkdir /apps/redis6379/tmp
[root@ubuntu2204 redis6379]#chown redis:redis /apps/redis6379/tmp/
[root@ubuntu2204 redis6379]#chown redis:redis /apps/redis6379/etc/sentinel.conf

# 启动哨兵
[root@ubuntu2204 redis6379]#systemctl start redis-sentinel
[root@ubuntu2204 redis6379]#systemctl start redis-sentinel
[root@ubuntu2204 redis6379]#systemctl start redis-sentinel
```







# 实验4：Redis Cluster

准备6台Redis服务器

```bash
# 主服务器 10.0.0.202
# 主服务器 10.0.0.203
# 主服务器 10.0.0.204
# 从服务器 10.0.0.205
# 从服务器 10.0.0.206
# 从服务器 10.0.0.207
# 每天服务器上，都安装Redis
[root@ubuntu2204 ~]# curl -fsSL https://www.mysticalrecluse.com/script/Shell/install_redis_binary.sh | bash
```





6台设备上所有配置文件初始相同，全部开启集群模式

```bash
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

在将所有节点加入同一个集群中

```bash
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





