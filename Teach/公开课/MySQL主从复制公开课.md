# 为什么需要主从复制







![image-20260415121301983](D:\git_repository\cyber_security_learning\markdown_img\image-20260415121301983.png)



**如果一个数据库：**

- 既要写，又要大量读
- 还不能停机
- 还要保证数据安全

怎么办？



## 三大核心场景

### 读写分离

![](D:\git_repository\cyber_security_learning\markdown_img\image-20260415135140675.png)



```bat
1. 减轻主库压力    2. 提高整体吞吐
```



### 高可用



![](D:\git_repository\cyber_security_learning\markdown_img\image-20260415135445206.png)

```bat
主库挂了 → 从库切换为主库
避免单点故障
```



### 数据备份 / 灾备



![image-20260417212420867](D:\git_repository\cyber_security_learning\markdown_img\image-20260417212420867.png)

```bat
避免备份过程中，影响主库性能，防止发生资源竞争。
```





# 主从复制完整流程（含实现机制)

## 复制原理图

![image-20260417213033154](D:\git_repository\cyber_security_learning\markdown_img\image-20260417213033154.png)

## 复制的流程



1. 从库开启主从复制（start slave），会创建⼀个 IO thread 来连接主库。
2. 主库接受到连接请求后，会创建⼀个 Binlog Dump thread 来响应它。
3. Binlog Dump Thread 会读取 binlog 里面的二进制日志事件
4. Binlog Dump Thread 将读取的事件发给 Slave IO Thread
5. Slave IO thread 接收到事件后，会将其写⼊到本地的 Relay log 中。
6. 从库的 SQL thread 实时监测replay log内容是否有更新，如果更新，会读取Relay log中的⼆进制⽇志事件，然后重放。



## 主从复制实现

### 搭建基本主从复制

#### 0. 前置准备

在准备好的两台虚拟机里分别安装MySQL

```bash
# 两台虚拟机分别部署MySQL
[root@mystical ~]# apt update && apt install -y mysql-server

# 安装后查看
[root@mystical ~]# mysql --version
mysql  Ver 8.0.45-0ubuntu0.24.04.1 for Linux on x86_64 ((Ubuntu))
```



MySQL配置文件并重启

```bash
# 主库配置
[root@mystical ~]# vim /etc/mysql/mysql.conf.d/mysqld.cnf
[mysqld]
log-bin = mysql-bin        // 开启 binlog。
server-id = 1              // 服务端ID。全局唯⼀。
bind-address = 0.0.0.0     // 开放端口

# 从库配置
[root@mystical ~]# vim /etc/mysql/mysql.conf.d/mysqld.cnf
[mysqld]
log-bin = mysql-bin        // 开启 binlog。
server-id = 2              // 服务端ID。全局唯⼀。
bind-address = 0.0.0.0     // 开放端口

# 重启服务使其生效
[root@mystical ~]# systemctl restart mysql

# 重启后查看
[root@mystical ~]# ss -ntlp
State          Recv-Q         Send-Q                 Local Address:Port                  Peer Address:Port         Process                                                          
LISTEN         0              4096                      127.0.0.54:53                         0.0.0.0:*             users:(("systemd-resolve",pid=640,fd=17))                       
LISTEN         0              151                          0.0.0.0:3306                       0.0.0.0:*             users:(("mysqld",pid=2882,fd=23))                               
LISTEN         0              70                         127.0.0.1:33060                      0.0.0.0:*             users:(("mysqld",pid=2882,fd=21))                               
LISTEN         0              4096                         0.0.0.0:22                         0.0.0.0:*             users:(("sshd",pid=1056,fd=3),("systemd",pid=1,fd=141))         
LISTEN         0              4096                   127.0.0.53%lo:53                         0.0.0.0:*             users:(("systemd-resolve",pid=640,fd=15))                       
LISTEN         0              4096                            [::]:22                            [::]:*             users:(("sshd",pid=1056,fd=4),("systemd",pid=1,fd=142))         

[root@mystical ~]# mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.45-0ubuntu0.24.04.1 (Ubuntu)

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show binary logs;
+------------------+-----------+-----------+
| Log_name         | File_size | Encrypted |
+------------------+-----------+-----------+
| mysql-bin.000001 |       157 | No        |
+------------------+-----------+-----------+
1 row in set (0.00 sec)
```



注意：

- 修改 server-id ⽆需重启实例，开启 binlog，需重启实例。
- 在 MySQL 8.0 之前，binlog 默认是关闭的，不显式设置 log-bin，则不会开启。
- 而在 MySQL 8.0 中，binlog是默认开启的，如果要关闭binlog，必须设置 skip_log_bin 或 disable_log_bin。



选择其中一台作为MySQL主库，在主库导入一些数据模拟主库正常运行的情况

```sql
# 创建测试库和表
CREATE DATABASE repl_test;
USE repl_test;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# 插入一些基础数据
INSERT INTO users (name, age) VALUES
('Alice', 25),
('Bob', 30),
('Charlie', 28),
('David', 35),
('Eve', 22);

# 写一个无限循环+可控停止的函数
DELIMITER $$

CREATE PROCEDURE insert_loop()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE TRUE DO
        INSERT INTO users(name, age) VALUES(CONCAT('loop_', i), i+20);
        SET i = i + 1;
        DO SLEEP(0.5);  -- 控制写入速度（很关键）
    END WHILE;
END$$

DELIMITER ;

CALL insert_loop();
```



#### 1. 主库上创建复制用户

```sql
CREATE USER 'repl'@'10.0.0.%' IDENTIFIED BY '123456';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'10.0.0.%';
```

从库上进行登录测试

```bash
[root@mystical ~]# mysql -h 10.0.0.101 -urepl -p123456
```



#### 2. 备份

创建备份的用户，并生成登录文件

```sql
CREATE USER 'backup'@'10.0.0.%' IDENTIFIED BY '123456';
GRANT SELECT, RELOAD, LOCK TABLES, PROCESS, SHOW VIEW, EVENT, REPLICATION CLIENT ON *.* TO 'backup'@'10.0.0.%';

# 生成登录文件
mysql_config_editor set --login-path=backup --host=10.0.0.101 --user=backup --passworod

# 查看
[root@mystical /var/lib/mysql/test]# ll /root/.mylogin.cnf 
-rw------- 1 root root 152 Feb 27 15:40 /root/.mylogin.cnf
[root@mystical /var/lib/mysql/test]# mysql_config_editor print --login-path=backup
[backup]
user = "backup"
password = *****
host = "10.0.0.101"
```

以 mysqldump 为例。备份集通过 scp 远程拷⻉到从库上。

```sql
[root@mystical ~]# mysqldump --login-path=backup --single-transaction --source-data=2 -E -R --triggers --databases repl_test > full.backup.sql
[root@mystical ~]# scp full.backup.sql 10.0.0.102:
```



#### 3. 基于主库的备份恢复从库

```bash
[root@mystical ~]# mysql < full.backup.sql
```



#### 4. 建立主从复制

获取位置点信息

```bash
[root@mystical ~]# grep -m 1 "CHANGE MASTER TO" full.backup.sql
-- CHANGE MASTER TO MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=235580;
```

执行 CHANGE MASTER TO 语句。

```sql
# 主库上查看复制用户的认证插件
mysql> select user,host,plugin from mysql.user;
+------------------+-----------+-----------------------+
| user             | host      | plugin                |
+------------------+-----------+-----------------------+
| backup           | 10.0.0.%  | caching_sha2_password |
| repl             | 10.0.0.%  | caching_sha2_password |
| debian-sys-maint | localhost | caching_sha2_password |
| mysql.infoschema | localhost | caching_sha2_password |
| mysql.session    | localhost | caching_sha2_password |
| mysql.sys        | localhost | caching_sha2_password |
| root             | localhost | auth_socket           |
+------------------+-----------+-----------------------+
7 rows in set (0.00 sec)

# 从库上执行
mysql> CHANGE MASTER TO
    ->  MASTER_HOST='10.0.0.101',
    ->  MASTER_USER='repl',
    ->  MASTER_PASSWORD='123456',
    ->  MASTER_LOG_FILE='mysql-bin.000001',
    ->  MASTER_LOG_POS=235580,
    ->  GET_MASTER_PUBLIC_KEY = 1;
Query OK, 0 rows affected, 9 warnings (0.01 sec)
```

其中， 

- MASTER_HOST：主库的主机信息。 
- MASTER_PORT：主库端⼝，不指定，则默认为3306。 
- MASTER_USER：复制⽤户。 
- MASTER_PASSWORD：复制⽤户的密码。 
- MASTER_LOG_FILE，MASTER_LOG_POS：从库 IO 线程启动时，它应该从主库的哪个 binlog（由 MASTER_LOG_FILE 确定）的哪个位置点（由 MASTER_LOG_POS 确定）开始读取 binlog。 

> 注意，如果是 MySQL 8.0，且复制用户的密码认证插件是 caching_sha2_password，才需要设置 GET_MASTER_PUBLIC_KEY = 1 （这个认证插件默认不允许明文传密码，需要用公钥加密传输密码）。使用的是 mysql_native_password 密码认证插件的就不需要。



#### 5. 开启主从复制

从库上执行

```sql
mysql> start slave;
Query OK, 0 rows affected, 1 warning (0.05 sec)

mysql> show slave status\G
*************************** 1. row ***************************
               Slave_IO_State: Waiting for source to send event
                  Master_Host: 10.0.0.104
                  Master_User: repl
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000001
          Read_Master_Log_Pos: 917164
               Relay_Log_File: mystical-relay-bin.000003
                Relay_Log_Pos: 12837
        Relay_Master_Log_File: mysql-bin.000001
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: 
          Replicate_Ignore_DB: 
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0
                   Last_Error: 
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 917164
              Relay_Log_Space: 682292
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 0
               Last_SQL_Error: 
  Replicate_Ignore_Server_Ids: 
             Master_Server_Id: 2
                  Master_UUID: b998bad7-3c6e-11f1-b212-005056287d06
             Master_Info_File: mysql.slave_master_info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Replica has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind: 
      Last_IO_Error_Timestamp: 
     Last_SQL_Error_Timestamp: 
               Master_SSL_Crl: 
           Master_SSL_Crlpath: 
           Retrieved_Gtid_Set: 
            Executed_Gtid_Set: 
                Auto_Position: 0
         Replicate_Rewrite_DB: 
                 Channel_Name: 
           Master_TLS_Version: 
       Master_public_key_path: 
        Get_master_public_key: 1
            Network_Namespace: 
1 row in set, 1 warning (0.00 sec)
```

重点关注两列的输出： Slave_IO_Running 和 Slave_SQL_Running，两个均为”Yes“代表主从复制搭建成功。



在主库上执行 show processlist 命令

```sql
mysql> show processlist;
+----+-----------------+------------------+-----------+-------------+------+-----------------------------------------------------------------+------------------+
| Id | User            | Host             | db        | Command     | Time | State                                                           | Info             |
+----+-----------------+------------------+-----------+-------------+------+-----------------------------------------------------------------+------------------+
|  5 | event_scheduler | localhost        | NULL      | Daemon      | 5465 | Waiting on empty queue                                          | NULL             |
| 20 | repl            | 10.0.0.105:59542 | NULL      | Binlog Dump | 3899 | Source has sent all binlog to replica; waiting for more updates | NULL             |
| 22 | root            | localhost        | repl_test | Query       |    0 | init                                                            | show processlist |
+----+-----------------+------------------+-----------+-------------+------+-----------------------------------------------------------------+------------------+
3 rows in set, 1 warning (0.00 sec)
```

Id 为 20 的连接对应的即是 Binlog Dump thread。



从库上执行 show processlist 命令

```sql
mysql> show processlist;
+----+-----------------+-----------------+------+---------+------+----------------------------------------------------------+------------------+
| Id | User            | Host            | db   | Command | Time | State                                                    | Info             |
+----+-----------------+-----------------+------+---------+------+----------------------------------------------------------+------------------+
|  5 | event_scheduler | localhost       | NULL | Daemon  | 4782 | Waiting on empty queue                                   | NULL             |
|  9 | system user     | connecting host | NULL | Connect | 4772 | Waiting for source to send event                         | NULL             |
| 10 | system user     |                 | NULL | Query   | 4024 | Replica has read all relay log; waiting for more updates | NULL             |
| 11 | system user     |                 | NULL | Query   | 4024 | Waiting for an event from Coordinator                    | NULL             |
| 12 | system user     |                 | NULL | Query   | 4856 | Waiting for an event from Coordinator                    | NULL             |
| 13 | system user     |                 | NULL | Connect | 4772 | Waiting for an event from Coordinator                    | NULL             |
| 14 | system user     |                 | NULL | Connect | 4772 | Waiting for an event from Coordinator                    | NULL             |
| 15 | root            | localhost       | NULL | Query   |    0 | init                                                     | show processlist |
+----+-----------------+-----------------+------+---------+------+----------------------------------------------------------+------------------+
8 rows in set, 1 warning (0.00 sec)

```

9 是 IO 线程，10 是协调线程，11-14 是 SQL 线程



## 查看复制用户的密码

```sql
mysql> select * from mysql.slave_master_info\G
*************************** 1. row ***************************
                Number_of_lines: 33
                Master_log_name: mysql-bin.000001
                 Master_log_pos: 865234
                           Host: 10.0.0.104
                      User_name: repl
                  User_password: 123456
                           Port: 3306
                  Connect_retry: 60
                    Enabled_ssl: 0
                         Ssl_ca: 
                     Ssl_capath: 
                       Ssl_cert: 
                     Ssl_cipher: 
                        Ssl_key: 
         Ssl_verify_server_cert: 0
                      Heartbeat: 30
                           Bind: 
             Ignored_server_ids: 0
                           Uuid: b998bad7-3c6e-11f1-b212-005056287d06
                    Retry_count: 86400
                        Ssl_crl: 
                    Ssl_crlpath: 
          Enabled_auto_position: 0
                   Channel_name: 
                    Tls_version: 
                Public_key_path: 
                 Get_public_key: 1
              Network_namespace: 
   Master_compression_algorithm: uncompressed
  Master_zstd_compression_level: 3
               Tls_ciphersuites: NULL
Source_connection_auto_failover: 0
                      Gtid_only: 0
1 row in set (0.00 sec)
```



## 查看从库重放信息

```sql
mysql> select * from mysql.slave_relay_log_info\G
*************************** 1. row ***************************
                             Number_of_lines: 14
                              Relay_log_name: ./mystical-relay-bin.000003
                               Relay_log_pos: 12837
                             Master_log_name: mysql-bin.000001
                              Master_log_pos: 917164
                                   Sql_delay: 0
                           Number_of_workers: 4
                                          Id: 1
                                Channel_name: 
                   Privilege_checks_username: NULL
                   Privilege_checks_hostname: NULL
                          Require_row_format: 0
             Require_table_primary_key_check: STREAM
 Assign_gtids_to_anonymous_transactions_type: OFF
Assign_gtids_to_anonymous_transactions_value: 
1 row in set (0.00 sec)
```

relay_log_info 表记录的是从库 SQL线程执行的“精确进度”，是主从复制中判断数据同步位置和进行故障切换的重要依据。



# 数据一致性问题分析

## 一致性相关定义

**什么是一致性**

在主从复制中，数据一致性指的是：**主库和从库在同一时间点上，数据是否相同。**

> 关键在于 “同一时间点”

问题：如果主库写入成功，从库查不到，这算不一致吗？

> 要看查询时间

**强一致性**：主库写完 --> 从库必须立刻可见（MySQL默认做不到）

**最终一致性**：主库写完 --> 过一段时间从库一致（MySQL默认实现）

**什么是一致性问题**：当从库数据与主库在 **预期时间内** 不一致时，就称为数据一致性问题。



## 为什么 MySQL 主从一定存在一致性问题

一致性问题一定存在的原因：**主从复制是异步的**

主库提交事务：

- 写 binlog（持久化）
- 从库 IO线程拉取 binlog
- 写入 relay log
- SQL 线程执行

> 由于主从复制是基于 binlog 的异步日志传输与重放机制，从事务提交到从库执行完成之间存在多个阶段，因此天然存在数据不一致窗口。



主从复制中的一致性问题，可以分为两类：：

- 复制层一致性问题（主从之间）
  - 由于日志传输和执行过程产生的问题
- 事务层一致性问题（主库内部）
  - 由于事务提交过程中 binlog 与数据不一致导致的问题。

> 主从复制能够保证一致性的前提，是主库生成的 binlog 本身是正确的；如果 binlog 与主库数据不一致，那么整个复制体系将失去基础，必然导致主从数据不一致



## 复制过程中产生的问题

### 1. 延迟一致性（最常见）

#### 现象

- 主库插入数据成功
- 从库查不到主库刚插入的数据



#### 原因

在主从复制期间，写binlog，从库 IO线程拉取binlog，从库写入relay log，还是从库 SQL 线程的执行，都会产生延迟，这也就意味着，主库写入，到从库重复一定存在时间差。（简单来说，主库在写日记，而从库在抄日记，抄一定比写慢）。

因此延迟一致性并不是一个bug，而是主从复制的特性。我们在生产中做的，不是消除它，而是控制它，绕开它。



#### 解决方案

##### 1. 读写分离规避

**应用代码控制（最常见）**

如果是写后读，则走主库，否则走从库。

```python
if is_write_operation:
    use_master()
elif is_read_after_write:
    use_master()
else:
    use_slave()
```



##### 2. 缓存兜底

伪代码示例：

```python
# 写操作
def update_user(user_id, new_name):
    # 1. 更新主库
    db.execute("UPDATE users SET name=%s WHERE id=%s", [new_name, user_id])

    # 2. 查询主库最新数据
    user = db.query_one("SELECT id, name, age FROM users WHERE id=%s", [user_id])

    # 3. 写入 Redis，设置短 TTL
    redis.setex(f"user:{user_id}", 5, json.dumps(user))  # 在主从延迟窗口（5秒）内，用 Redis 保证读到最新值
    

# 读操作
def get_user(user_id):
    # 1. 先查 Redis
    val = redis.get(f"user:{user_id}")
    if val:
        return json.loads(val)

    # 2. Redis 没有，再查数据库
    # 普通情况下这里可以查从库
    user = slave_db.query_one("SELECT id, name, age FROM users WHERE id=%s", [user_id])
    return user
```

> 在主从复制延迟场景下，常见的规避方案有两种：
>  一种是业务侧在写后短时间内强制读主库，优点是简单可靠（适合并发不高，但对一致性要求高的场景）；
>  另一种是引入 Redis 作为最新值缓存层，优点是减少主库读压力（适用于读流量大，热点数据多，写后短时间内会被频繁读取的场景）。
>  前者偏“简单稳妥”，后者偏“高性能优化”。



##### 3. 提升复制速度

- 方法1：开启并行复制

  ```sql
  slave_parallel_workers = 4
  ```

- 方法2：减少大事务

- 方法3：提升IO / 网络



##### 4. 监控延迟

```sql
# 通过
SHOW REPLICA STATUS\G
# 查看
Seconds_Bebind_Master
```

生产中一旦超过阈值，则触发告警。



### 2. 主从切换导致的数据丢失

主从切换导致的数据丢失，是指**主库已经对客户端返回“写成功”**，但这些数据**还没有同步并执行到从库**，这时如果主库故障并把从库提升为新主库，那么这部分未同步的数据就会永久丢失。

这个定义里有两个关键词：

- 主库已经返回成功
- 从库还没追上

> 对客户端来说写成功了，但对整个主从体系来说，这条数据还不安全。



#### 经典丢数据场景

**场景1：主库突然宕机**

1. 用户下单
2. 主库写入订单成功，并返回“下单成功”
3. 这条 binlog 还没同步到从库
4. 主库突然断电
5. 从库被提升为新主
6. 用户订单在新主库里不存在

> 此时结果：用户看到下单成功，但订单没了。



**场景2：自动故障切换过快**

比如高可用系统误判主库故障，快速把从库升主：**主库只是网络抖动，但自动切换已出发，从库还没追平**，结果：

- 旧主上最后几笔写入没同步过去
- 新主已经开始对外提供服务
- 最后几笔数据丢失

> 这类问题在自动化切换场景下很常见。



#### 解决方案

**1. 使用半同步复制**

```bat
至少一个从库收到 binlog 才返回成功
```



**2. 合理故障检测（避免误切换）**

```bat
检测到主库异常 → 等几秒确认
```





### 3. 执行错误导致的不一致

执行错误导致的不一致，是指主库已经正常执行并写入 binlog，但从库在重放 relay log 时执行失败，导致复制中断，后续数据无法继续同步，从而造成主从数据不一致。

```bat
这里需要注意的点：
主库没问题
问题出在从库 “执行” 这一步
```

也就是说：

- 主库：事务提交成功，binlog 正常
- 从库：拿到了日志，但是执行不下去

于是复制链断了。



#### 典型现象

从库执行：

```sql
SHOW REPLICA STATUS\G
```

你会看到：

```sql
Replica_IO_Running: Yes
Replica_SQL_Running: No
```

这就说明：

- IO线程还在拉日志
- 但 SQL线程停了

进一步看：

```sql
Last_SQL_Error
```

这里就能看到具体错误原因。



#### 常见原因

**1. 非确定性语句引发的执行差异**

比如 statement 模式下：

```sql
UPDATE t SET score = RAND();
```

或者：

```sql
INSERT INTO t VALUES (NOW());
```

主从执行结果可能不一样，进一步可能触发冲突或逻辑错误。



**2. DDL 导致的中断**

比如：

- 主库执行 `ALTER TABLE`
- 从库执行太慢
- 或中间结构已经不一致

就可能导致后面的 DML 无法继续。

DDL 是复制里非常危险的一类操作。



#### 生产案例讲解

有一张订单表：

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10,2)
);
```

**线上变更（问题开始）**

开发要加一个字段：

```sql
# 主库执行
ALTER TABLE orders ADD COLUMN status VARCHAR(20);
```

**主库情况**

```bat
ALTER TABLE 成功
→ 写入 binlog
→ 返回成功
```

**从库情况**

从库开始执行这个 DDL：

```sql
SQL线程执行 ALTER TABLE
```

但问题来了：

**问题1：表很大（千万级数据）**

```sql
ALTER TABLE 是重建表（copy）
→ 执行时间很长（几十秒 / 几分钟）
```

从库

```sql
SQL线程被DDL占住
```

**问题2：这段时间主库还在写**

主库继续执行：

```sql
INSERT INTO orders VALUES (...);
UPDATE orders SET amount=... WHERE id=...
```

binlog 持续产生

但从库：

```bat
DDL还没执行完 → 后续DML全部“堆积”
```

**问题升级（真正事故点）**

**有人手工干预（最常见）**

运维看到从库卡住：

```bat
延迟越来越大
```

一旦运维误判，以为是 SQL 线程异常，打算重启 SQL 线程

```sql
STOP REPLICA;
START REPLICA;
```

或者：

```bat
kill 掉 SQL线程
```

**后续就会发生一系列错误**

DDL没执行完就被中断

```bat
表结构：半完成状态
```

复制链断裂

```sql
Replica_SQL_Running = No
```

后续 DML 全部报错
```sql
Unknown column
Column count mismatch
```

复制彻底中断



#### 生产中如何避免

**建议使用在线DDL工具（最重要）**

不直接用

```sql
ALTER TABLE
```

使用在线DDL（pt-osc / gh-ost）时：

```bat
写操作不会因为“新字段”而阻塞
```

> 原因是：整个变更过程不是在原表上做，而是在“影子表（ghost table）”上完成的





### 4. 非确定性操作导致不一致（高级）

#### 案例

```sql
INSERT INTO t VALUES (NOW());
```

或：

```sql
UPDATE t SET value = RAND();
```



#### 问题

 主库执行和从库执行：

```bat
时间不同 / 随机数不同
```

最终导致数据不一致



#### 解决方案

```bat
使用 ROW 格式 binlog（推荐）
```





## 主库自身事务提交不一致导致的问题

### 问题场景

事务提交过程中崩溃：

```bat
数据写入成功，但 binlog 没写
```

或者：

```bat
binlog 写了，但数据没落盘
```



**导致结果**

主从直接不一致

```bat
主库数据 ≠ 从库数据
```

> 从库是靠 binlog 同步的，如果 binlog 和 数据不一致，整个复制体系就崩了。



```bat
MySQL 是否有机制来保证 binlog 和数据一定一致呢？
答案是有，使用的就是两阶段提交（2PC）机制，
它解决的是：“事务提交时，binlog 和数据必须同时成功或同时失败”
```





# 2PC两阶段提交机制

## 一条事务从请求到复制的完整顺序（2PC 的完整逻辑流程图）



![image-20260420211740208](D:\git_repository\cyber_security_learning\markdown_img\image-20260420211740208.png)



### 第 1 步：客户端发送 SQL

```bat
client -> mysqld
```

MySQL Server 层接收 SQL，开始一个事务（显式 BEGIN 或隐式）。



### 第 2 步：执行阶段（InnoDB 层）

```sql
UPDATE account SET money=200 WHERE id=1;
```

InnoDB 做三件事：

1. 修改 Buffer Pool （位于 MySQL 用户态内存）中的数据页（内存）
2. 生成 undo 记录（用于回滚 + MVCC）
3. 生成 redo 记录（用于崩溃恢复）
4. 生成 binlog event（row event / statement），写入 binlog cache（内存）

此时：

- 数据页在内存被修改
- redo 在 redo buffer
- 还没真正持久化
- binlog event 在 binlog cache



### 第 3 步：进入提交阶段（关键）

当执行：

```css
COMMIT;
```

真正复杂的事情开始了。

为了保证 redo 和 binlog 一致，MySQL 做 2PC。



#### 阶段一：Prepare 阶段（InnoDB）

1. InnoDB 写 redo（包含 prepare 标记）
2. 根据 `innodb_flush_log_at_trx_commit` 决定是否 fsync

```bat
innodb_flush_log_at_trx_commit 不控制“系统何时发生 write/fsync”，但它控制“commit 时是否必须执行这些动作并等待完成”。
```

此时：

- InnoDB 说：“我准备好了。”

但事务还不能算真正提交。



#### 阶段二：写 binlog（Server 层）

1. Server 层写 binlog 事件
2. 根据 `sync_binlog` 决定是否 fsync

此时：

- binlog 持久化完成
- 复制系统可以看到这条事务



#### 阶段三：Commit 阶段（InnoDB）

- InnoDB 写 redo commit 标记
- 事务真正完成
- 返回给客户端“提交成功”



### 第 4 步：复制流程

从库：

1. IO 线程拉取 binlog
2. 写入 relay log
3. SQL 线程重放
4. 从库执行事务



## 宕机在 6 个不同时间点的完整恢复结果推演

下面用最经典的一笔事务来推：

```sql
BEGIN;
UPDATE account SET money = money - 200 WHERE id=1;
COMMIT;
```

并假设这是一个 **InnoDB 表 + binlog 开启** 的典型主库。



### 时间线总览（你先把这 6 个点记住）

把提交路径抽象成这些动作（按发生顺序）：

1. **执行更新**：改 Buffer Pool，写 undo，写 redo（update 的 redo，未提交）
2. **进入提交**：写 redo 的 **prepare** 记录
3. **写 binlog event**（含 XID）到 binlog buffer/文件（未必 fsync）
4. **fsync binlog**（binlog 真正落盘持久化）
5. **写 redo 的 commit** 记录
6. **fsync redo**（取决于 `innodb_flush_log_at_trx_commit`）

> 2PC 协调的“提交判据”是：**redo prepare + binlog XID（事务提交标识）**。



### 推演规则

重启恢复时：

- InnoDB 扫描 **redo 物理文件**，找 `PREPARED` 的事务（带 XID）
- 对每个 prepared XID 去查 **binlog 物理文件**里是否有对应 XID
  - 找到 → **提交**
  - 找不到 → **回滚**

> 所以你只要在每个宕机点判断：**redo 有没有 prepare？binlog 有没有 XID？**就能推出结果。



### 6 个宕机点逐个推（拔电推演）

#### 宕机点 1：执行更新过程中（还没 prepare）

**当时可能发生：**

- Buffer Pool 页被改了（脏页）
- undo 已生成（部分或全部）
- redo（更新相关）可能写入了 log buffer，甚至部分写进 redo 文件

**宕机后重启：**

- redo 里：**没有 prepare**
- binlog 里：**没有 XID**
- InnoDB crash recovery：最多把“未完成的页修改”用 redo/undo 修正到一致状态，但事务视角是 **未提交**

> 最终结果：**回滚（事务不生效）**

示例：如果数据库 crash 后重启：

```c
redo log 有 prepare
binlog 没 commit
```

MySQL 会：rollback 这个事务。

启动日志会看到：

```c
InnoDB: Transaction 123 in prepared state
InnoDB: Rolling back trx 123
```



#### 宕机点 2：redo 已写 prepare（prepare 落到 redo 文件）但 binlog 还没写

**当时发生：**

- redo 文件里已经有：`PREPARE(XID=123)`
- binlog 文件里还没有这笔事务

**宕机后重启：**

- redo：**有 prepare**
- binlog：**无 XID**

恢复判断：prepared 但没 binlog → 说明 server 还没承诺复制/持久化

> 最终结果：**回滚**



#### 宕机点 3：binlog 已写入文件（可能在 page cache）但还没 fsync

**当时发生：**

- redo：有 prepare
- binlog：事件可能已经 write() 出去，但只是 OS page cache，**没 fsync**

**宕机后重启：**  

这里分两种现实情况（这也是最有价值的点）：

- **3A：只是 mysqld 崩溃（OS 没崩）**
   page cache 还在，binlog 文件可能包含 XID
   → redo 有 prepare + binlog 有 XID → **提交**
- **3B：机器掉电/OS 崩溃**
   page cache 丢了，binlog 可能没有这笔 XID
   → redo 有 prepare + binlog 无 XID → **回滚**

最终结果（最保守、也是数据库承诺的）：**回滚**

> 因为没有 fsync 的 binlog，不能当作 “存在”。



#### 宕机点 4：binlog 已 fsync 成功，但 redo 还没写 commit

**当时发生：**

- redo：有 prepare
- binlog：**XID 已经持久化**
- redo commit：还没来得及写/刷

**宕机后重启：**

- redo：扫描到 prepared(XID=123)
- 查 binlog：找到 XID=123

恢复判断：redo prepared + binlog XID 存在 → InnoDB 必须把它补成 committed

最终结果：**提交（会在恢复过程中完成提交）**

> 这就是 2PC 的“关键保证”：**一旦 binlog fsync 了，这笔事务就必须最终提交**，否则复制会乱。



#### 宕机点 5：redo 已写 commit（但可能没 fsync）

**当时发生：**

- redo：有 prepare + commit（至少写进 redo 文件或 buffer）
- binlog：已 fsync（通常在它前面）
- 可能还没把 redo fsync（取决于参数）

**宕机后重启：**

- redo：通常能看到 commit（若已进文件）
- 即使只看到 prepare，也能在 binlog 里找到 XID

> 最终结果：**提交**



#### 宕机点 6：一切都完成（redo commit 也 fsync 了）

**当时发生：**

- redo：commit 持久化
- binlog：持久化

**宕机后重启：**  毫无悬念。

✅ 最终结果：**提交**



| 宕机点                   | redo(prepare) | binlog(XID) | 重启结论                               |
| ------------------------ | ------------- | ----------- | -------------------------------------- |
| 1 执行中未 prepare       | ❌             | ❌           | 回滚                                   |
| 2 已 prepare 未写 binlog | ✅             | ❌           | 回滚                                   |
| 3 写了 binlog 未 fsync   | ✅             | ⚠ 不确定    | **掉电：回滚**；仅 mysqld 崩：可能提交 |
| 4 binlog fsync 后宕机    | ✅             | ✅           | **提交**（恢复时补 commit）            |
| 5 redo commit 后宕机     | ✅             | ✅           | 提交                                   |
| 6 全部持久化后宕机       | ✅             | ✅           | 提交                                   |





# Group Commit 与性能优化













# 总结与设计思想