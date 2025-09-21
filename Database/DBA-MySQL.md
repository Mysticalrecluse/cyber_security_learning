# MySQL安装

## 官方文档解读

```http
https://dev.mysql.com/doc/refman/8.0/en/
```

![image-20250919093959919](D:\git_repository\cyber_security_learning\markdown_img\image-20250919093959919.png)



## 下载页面解读

```http
mysql.com/downloads/
```

![image-20250919094240399](D:\git_repository\cyber_security_learning\markdown_img\image-20250919094240399.png)

```http
dev.mysql.com/downloads/
```

![image-20250919094410923](D:\git_repository\cyber_security_learning\markdown_img\image-20250919094410923.png)

![image-20250919094626407](D:\git_repository\cyber_security_learning\markdown_img\image-20250919094626407.png)

```bat
建议使用LTS版本，不建议使用Innovation版本
如上图，建议使用8.4.6LTS，或者8.0.43
```

![image-20250919095030288](D:\git_repository\cyber_security_learning\markdown_img\image-20250919095030288.png)

```bat
# 查看glibc版本
[root@devops-custom ~]# ldd --version
ldd (Ubuntu GLIBC 2.35-0ubuntu3.10) 2.35
Copyright (C) 2022 自由软件基金会。
这是一个自由软件；请见源代码的授权条款。本软件不含任何没有担保；甚至不保证适销性
或者适合某些特殊目的。
由 Roland McGrath 和 Ulrich Drepper 编写。
```



### 补充 ldd 命令详解

`ldd` 用来**显示一个可执行文件或共享库在运行时会加载哪些共享库**，以及这些库被解析到的**实际路径**与**装载基址**。最常用于：

- 诊断 “`libXXX.so: cannot open shared object file: No such file or directory`”
- 确认程序需要的 **glibc/其他库版本**
- 检查 RPATH/RUNPATH/`LD_LIBRARY_PATH` 等搜索路径生效情况
- 找“没用上的直连依赖”（瘦身镜像/包）



#### 基本用法与输出解读

```bash
[root@devops-custom ~]# ldd /bin/ls
        linux-vdso.so.1 (0x00007ffcb3f81000)
        libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1 (0x00007f370577d000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f3705554000)
        libpcre2-8.so.0 => /lib/x86_64-linux-gnu/libpcre2-8.so.0 (0x00007f37054bd000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f37057df000)
```

常见情形：

- `xxx.so => /path/to/xxx.so (0x...)`：找到了，并显示装载地址。
- `xxx.so => not found`：没找到（最常见的出错原因）。
- `statically linked` / `not a dynamic executable`：静态链接或非ELF动态文件，`ldd` 不适用。



#### 常用参数

```bat
ldd --version            # 同时大致反映系统 glibc 版本
ldd -v                   # verbose，显示符号版本需求等
ldd -u /path/prog        # 列出“未使用的直连依赖”
ldd -d / -r              # 解析并报告数据/函数重定位问题（更严格）
```



#### 安全警告

多数 glibc 系统上，`ldd` 不是简单的“离线解析器”，它通常通过**设置环境变量**（如 `LD_TRACE_LOADED_OBJECTS=1`）让**动态链接器**加载目标文件，并打印依赖；在某些情况下它会**实际执行目标**的一部分装载流程。
 👉 **不要对不可信的二进制文件运行 `ldd`**（可能触发其恶意初始化代码）。
 要做**纯静态分析**，改用：

```bat
readelf -dW /path/prog            # 看 NEEDED/RPATH/RUNPATH
objdump -p /path/prog | grep NEEDED
```





## MySQL二进制安装

```bat
# 下载资源
[root@ubuntu2204 ~]# cd /usr/local/src
[root@ubuntu2204 src]# wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.43-linux-glibc2.28-x86_64.tar.xz
[root@ubuntu2204 src]# wget https://dev.mysql.com/get/Downloads/MySQL-8.4/mysql-8.4.6-linux-glibc2.28-x86_64.tar.xz

# 解压
[root@ubuntu2204 src]# tar xf mysql-8.0.43-linux-glibc2.28-x86_64.tar.xz

# 创建软链接
[root@ubuntu2204 src]# ln -s /usr/local/src/mysql-8.0.43-linux-glibc2.28-x86_64 /usr/local/mysql8.0

# MySQL初始配置文件
[root@ubuntu2204 mysql8.0]# mkdir {log,data,etc}
[root@ubuntu2204 mysql8.0]# vim etc/my.cnf
[client]
socket = /usr/local/mysql8.0/data/mysql.sock

[mysqld]
basedir = /usr/local/mysql8.0
datadir = /usr/local/mysql8.0/data
user = mysql
port = 3306
socket = /usr/local/mysql8.0/data/mysql.sock
log_error = /usr/local/mysql8.0/log/mysqld.err
log_timestamps = system

log-bin = mysql-bin
server-id = 1

# mysql初始化
[root@ubuntu2204 mysql8.0]# /usr/local/mysql8.0/bin/mysqld --defaults-file=/usr/local/mysql8.0/etc/my.cnf --initialize

# 查看表空间
[root@ubuntu2204 mysql8.0]#ls data/
 auto.cnf          client-key.pem       ibdata1         mysql-bin.000001     private_key.pem   sys
 ca-key.pem       '#ib_16384_0.dblwr'  '#innodb_redo'   mysql-bin.index      public_key.pem    undo_001
 ca.pem           '#ib_16384_1.dblwr'  '#innodb_temp'   mysql.ibd            server-cert.pem   undo_002
 client-cert.pem   ib_buffer_pool       mysql           performance_schema   server-key.pem
 
# 查看日志，会生成初始密码
[root@ubuntu2204 mysql8.0]#cat log/mysqld.err 
2025-09-19T11:10:48.915632+08:00 0 [System] [MY-013169] [Server] /usr/local/mysql8.0/bin/mysqld (mysqld 8.0.43) initializing of server in progress as process 1481
2025-09-19T11:10:48.925270+08:00 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2025-09-19T11:10:49.390455+08:00 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2025-09-19T11:10:52.190679+08:00 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: .3DH53oww,e+

# 初始化成功后，启动实例
[root@ubuntu2204 mysql8.0]#/usr/local/mysql8.0/bin/mysqld_safe --defaults-file=/usr/local/mysql8.0/etc/my.cnf &

# 查看端口
[root@ubuntu2204 mysql8.0]#ss -nlt
State          Recv-Q         Send-Q     Local Address:Port       Peer Address:Port         Process         
LISTEN         0              4096       127.0.0.53%lo:53         0.0.0.0:*    
LISTEN         0              128        0.0.0.0:22               0.0.0.0:*     
LISTEN         0              70         *:33060                  *:*     
LISTEN         0              151        *:3306                   *:*     
LISTEN         0              128        [::]:22                  [::]:*

# 查看进程
[root@ubuntu2204 mysql8.0]#ps aux|grep mysql
root        1550  0.0  0.0   2888  1728 pts/1    S    11:14   0:00 /bin/sh /usr/local/mysql8.0/bin/mysqld_safe --defaults-file=/usr/local/mysql8.0/etc/my.cnf
mysql       1725  0.7 10.0 1755120 399752 pts/1  Sl   11:14   0:01 /usr/local/mysql8.0/bin/mysqld --defaults-file=/usr/local/mysql8.0/etc/my.cnf --basedir=/usr/local/mysql8.0 --datadir=/usr/local/mysql8.0/data --plugin-dir=/usr/local/mysql8.0/lib/plugin --user=mysql --log-error=/usr/local/mysql8.0/log/mysqld.err --pid-file=ubuntu2204.wang.org.pid --socket=/usr/local/mysql8.0/data/mysql.sock --port=3306

# 使用客户端登录mysql
[root@ubuntu2204 mysql8.0]#/usr/local/mysql8.0/bin/mysql -uroot -S /usr/local/mysql8.0/data/mysql.sock -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.43

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# 使用alert user设置密码,这里设置空密码，RPM包安装的话，因为密码策略插件的原因，无法设置空密码
mysql> alter user user() identified by '';
Query OK, 0 rows affected (0.00 sec)
```



### 如何定位实例启动失败原因

1. 查看错误日志

2. 通过 mysqld 启动

   ```bash
   # /usr/local/mysql8.0/bin/mysqld --defaults-file=my.cnf &
   ```

3. 只指定几个必要的参数启动

   ```bat
   # /usr/local/mysql8.0/bin/mysqld --no-defaults --basedir=/usr/local/mysql8.0 --datadir=/data/mysql8.0/data/ --user=mysql
   ```

如果还是不行，可以通过 strace 查看 MySQL 启动过程中的系统调用情况





## MySQL源码编译安装

```http
dev.mysql.com/downloads/mysql/
```

![image-20250919115932558](D:\git_repository\cyber_security_learning\markdown_img\image-20250919115932558.png)

```bat
# cd /usr/local/src
# wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-boost-8.0.43.tar.gz
# yum install -y cmake3 gcc gcc-c++ glibc ncurses-devel openssl-devel libaio-devel
# apt install -y pkg-config libtirpc-dev rpcsvc-proto build-essential libncurses-dev libssl-dev libaio-dev zlib1g-dev cmake gcc g++ libc6 
# tar xf mysql-boost-8.0.43.tar.gz
# cd mysql-8.0.43/
# mkdir build
# cd build
# cmake3 /usr/local/src/mysql-8.0.43/ -DWITH_BOOST=/usr/local/src/mysql-8.0.43/boost/boost_1_77_0 -DENABLE_DOWNLOADS=1 -DBUILD_CONFIG=mysql_release

# make

# make install
```

源码编译支持的选项：https://dev.mysql.com/doc/refman/8.0/en/source-configuration-options.html



## systemd管理服务

创建 systemd 服务配置文件

```bash
[root@ubuntu2204 mysql8.0]#cat /lib/systemd/system/mysql.service 
[Unit]
Description=MySQL Server
Documentation=man:mysqld(8)
Documentation=http://dev.mysql.com/doc/refman/en/using-systemd.html
After=network.target
After=syslog.target

[Install]
WantedBy=multi-user.target

[Service]
User=mysql
Group=mysql

Type=forking

PIDFile=/usr/local/mysql8.0/data/mysqld.pid

# Disable service start and stop timeout logic of systemd for mysqld service.
TimeoutSec=0

# Start main service
ExecStart=/usr/local/mysql8.0/bin/mysqld --defaults-file=/usr/local/mysql8.0/etc/my.cnf --pid-file=/usr/local/mysql8.0/data/mysqld.pid --daemonize $MYSQLD_OPTS

# Use this to switch malloc implementation
#EnvironmentFile=~/etc/sysconfig/mysql

# Sets open_files_limit

LimitNOFILE=65535

Restart=on-failure

RestartPreventExitStatus=1

PrivateTmp=false
```



## MySQL8.0 配置文件参数模版 (线上配置)

```ini
[client]
socket = /usr/local/mysql8.0/data/mysql.sock

[mysql]
# 关闭 mysql 客户端的“自动补全（auto-rehash）”功能
# auto-rehash 是什么？
# mysql 命令行里按 Tab 能补全 库/表/列 名。为做到这一点，客户端在：
# 启动连接时，和/或
# 你执行 USE db; 切换数据库时
# 会去服务器拉取元数据（库、表、列清单）并“建索引”（rehash）。库很多或网络慢时，这个过程会明显卡顿。
# 关掉它有什么效果？
# no-auto-rehash = 不再自动拉取元数据 → 启动、切库更快；
# 代价：Tab 不再补全表/列名（关键字仍可补全）；
# 需要时你可以手动补一次：在 mysql 提示符里执行 rehash，随后再用 Tab。

# 什么时候建议关？
# 连接线上实例、库/表数量大、或者网络延迟高时；
# 登录只为执行已知命令，不依赖交互补全时。
no-auto-rehash

[mysqld]
# General
user = mysql
port = 3306
basedir = /usr/local/mysql8.0
datadir = /usr/local/mysql8.0/data
socket = /usr/local/mysql8.0/data/mysql.sock
pid_file = /usr/local/mysql8.0/data/mysql.pid
character_set_server = utf8mb4
# 事务隔离级别
transaction_isolation = READ-COMMITTED 
# 建议开启严格模式
sql_mode = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'
log_error = /usr/local/mysql8.0/log/mysqld.err
default_time_zone = '+8:00'
log_timestamps = system
temdir = /usr/local/mysql8.0/tmp
secure_file_priv = /usr/local/mysql8.0/tmp

#Slow log
slow_query_log = ON
long_query_time = 0.5
slow_query_log_file = /usr/local/mysql8.0/slowlog/slog.log

# Connection
back_log = 2048
max_connections = 500
max_connect_errors = 10000
interactive_timeout = 1800
wait_timeout = 1800
thread_cache_size = 128
max_allowed_packet = 1G
skip_name_resolve = ON

# Session
read_buffer_size = 2M
read_rnd_buffer_size = 4M
sort_buffer_size = 4M
join_buffer_size = 4M

# InnoDB
innodb_buffer_pool_size = 6144M
innodb_buffer_pool_instances = 4
innodb_log_file_size = 512M
innodb_log_files_in_group = 2
innodb_log_buffer_size = 16M
innodb_flush_log_at_trx_commit = 1
innodb_undo_tablespaces = 2
innodb_max_undo_log_size = 1024M
innodb_undo_log_truncate = 1
innodb_page_cleaners = 8
innodb_io_capacity = 200
innodb_io_capacity_max = 500
innodb_data_file_path = ibdata1:1G:autoextend
innodb_flush_method = O_DIRECT
innodb_purge_threads = 4
innodb_antoinc_lock_mode = 2
innodb_buffer_pool_load_at_startup = 1
innodb_buffer_pool_dump_at_shutdown = 1
innodb_read_io_threads = 8
innodb_write_io_threads = 8
innodb_flush_neighbors = 1
innodb_checksum_algorithm = crc32
innodb_strick_mode = ON
innodb_print_all_deadlocks = ON
innodb_numa_interleave = ON
innodb_open_files = 65535
innodb_adaptive_hash_index = OFF

# Replication
server_id = 528884
log_bin = /usr/local/mysql8.0/binlog/mysql-bin
relay_log = /usr/local/mysql8.0/relaylog/relay-bin
sync_binlog = 1
binlog_format = ROW
master_info_repository = TABLE
relay_log_info_repository = TABLE
relay_log_recovery = ON
log_slave_updates = ON
binlog_expire_logs_seconds = 604800
slave_rows_search_algorithms = 'INDEX_SCAN,HASH_SCAN'
skip_slave_start = ON
slave_net_timeout = 60
binlog_error_action = ABORT_SERVER
super_read_only = ON

# Semi-Sync Replication
plugin_load = 'validate_password.so;semisync_master.so;semisync_slave.so'
rpl_semi_sync_master_enabled = ON
rpl_semi_sync_slave_enabled = ON
rpl_semi_sync_master_timeout = 1000

# GTID
gtid_mode = ON
enforce_gtid_consistency = ON
binlog_gtid_simple_recovery = ON

# Multithreaded Replication
slave-parallel-type = LOGICAL_CLOCK
slave-parallel-workers = 8
slave_preserver_commit_order = ON
transaction_write_set_extraction = XXHASH64
binlog_transaction_dependency_tracking = WRITESET_SESSION
binlog_transaction_dependency_history_size = 25000

# others
open_files_limit = 65535
max_heap_table_size = 32M
tmp_table_size = 32M
table_open_cache = 65535
table_definition_cache = 65535
table_open_cache_instances = 64
```



### 上述参数含义

**back_log = 2048**

- **作用**：控制 MySQL 监听套接字的 **等待队列长度**（`listen(back_log)`），也就是当客户端瞬时并发建连很多，而 mysqld 还没来得及 `accept()` 时，能在内核队列里**排队**的连接请求数。
- **影响**：建连高峰期可减少 “connect timeout/ECONNREFUSED”。
- **前提**：受内核上限限制，Linux 至少需要
  - `net.core.somaxconn >= 2048`
  - `net.ipv4.tcp_max_syn_backlog` 也要相应加大（SYN 队列）
- **排错/自检**：若仍有大量失败连接，`ss -lnt` 看监听，`dmesg`/监控看 SYN backlog drops；必要时配合负载均衡器的连接速率限制。



**max_connections = 500**

- **作用**：允许的**同时连接数上限**。超出时返回 *Too many connections*。

- **代价**：每个连接都要占用线程与一批会话缓冲区（如 `thread_stack`、`net_buffer_length`，在执行排序/连接时还会临时分配 `sort_buffer_size`、`join_buffer_size` 等）。

- **建议**：不要盲目拉很大。粗略估算**基线内存**（0.5–2MB/连接）×并发，再预留执行期峰值；更大的并发请配合**连接池**（应用或中间件）与**线程池**（MySQL 企业版/Percona Thread Pool）。

- **观测**：

  ```
  SHOW GLOBAL STATUS LIKE 'Threads_connected';
  SHOW GLOBAL STATUS LIKE 'Max_used_connections';
  ```



**max_connect_errors = 10000**

- **作用**：来自**同一主机**的**连续连接失败**（如握手中断、半开等）达到此阈值后，**暂时封禁**该主机（防止恶意/异常反复尝试）。
- **解封**：`FLUSH HOSTS;` 或 mysqld 重启。
- **注意**：设得很大基本等于放宽保护；在易抖动网络或大量短连失败环境可适当提高，但不建议无限大。



**interactive_timeout = 1800，wait_timeout = 1800**

- **作用**：**空闲连接超时**（秒）。

  - 对**交互式连接**（客户端设置了 `CLIENT_INTERACTIVE` 标志，如 `mysql` 命令行的交互模式），会话的 `wait_timeout` **初始化**为 `interactive_timeout`。
  - 对**非交互连接**（大多数应用/驱动），会话的 `wait_timeout` **初始化**为全局 `wait_timeout`。

- **效果**：空闲超过 30 分钟自动断开，回收资源。

- **实践**：对使用**连接池**的应用，要与应用池的**闲置回收时间**匹配，否则容易出现“服务端先断、应用池复用死连接”的问题（报 `MySQL server has gone away`）。多数驱动有“连接存活/心跳”选项。

- **查看会话值**：

  ```
  SHOW VARIABLES LIKE 'wait_timeout';
  SHOW VARIABLES LIKE 'interactive_timeout';
  ```



**thread_cache_size = 128**

- **作用**：完成请求后，服务端线程不销毁、放入**线程缓存**，新连接可复用，避免频繁的线程创建/销毁开销。

- **调优方法**：观察 `Threads_created` 增长速度，如果在稳定负载下仍增长很快，说明缓存偏小；逐步增大。

  ```
  SHOW GLOBAL STATUS LIKE 'Threads_created';
  SHOW GLOBAL STATUS LIKE 'Connections';
  ```

  一般让 `Threads_created`/运行时间（秒）远小于 1 比较理想。

- **经验**：并发峰值几百时，`64~256` 常见；太大也无益（占用少量内存）。



**max_allowed_packet = 1G**

- **作用**：服务器允许接收的**单个通信包**的最大大小（同时也限制结果集/语句中单条记录的编码后大小）。
- **为什么设大**：需要传/收大 BLOB/TEXT、批量插入、或复制通道上存在大事务/行时需要更高上限。
- **代价与风险**：这是**上限**，连接在需要时会把网络缓冲**增长到这个大小**，极端情况下消耗大量内存；同时也可能放大“超大包”带来的 DoS 风险。
- **建议**：按业务最大值+余量设置（如 64M/256M），确有需要再到 1G；复制链路两端的相关上限需一致或更高（如 `replica` 侧也要同步设置）。



**skip_name_resolve = ON**

- **作用**：**禁用 DNS 反查**，只用 IP 做认证匹配，避免连接握手阶段因 DNS 慢/坏而阻塞。
- **影响**：`mysql.user` 中 **以主机名写的账号**（如 `'u'@'app01.mydomain'`）将不匹配，必须改用 IP/网段（如 `'u'@'10.0.%'`、`'u'@'%'`）。
- **变更方式**：启动参数/配置文件项，**需要重启** mysqld 生效。
- **常见收益**：显著降低登录抖动与 “Host 'x' is not allowed to connect to this MySQL server” 等因 DNS 引起的问题。







