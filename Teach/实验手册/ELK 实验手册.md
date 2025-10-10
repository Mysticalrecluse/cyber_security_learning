# ELK 实验手册

## Elasticsearch部署和管理

Elasticsearch 是一个分布式的免费开源搜索和分析引擎，适用于包括文本、数字、地理空间、结构化和 非结构化数据等在内的所有类型的数据



### Elasticsearch 安装说明

**官方文档**

```http
https://www.elastic.co/guide/en/elastic-stack/index.html
https://www.elastic.co/guide/en/elasticsearch/reference/master/install-elasticsearch.html
```



**部署方式**

- **包安装**
- **二进制安装** 
- **Docker 部署** 
- **Kubernetes 部署** 
- **Ansible 批量部署**



**ES支持操作系统版本和 Java 版本官方说明**

```http
https://www.elastic.co/cn/support/matrix
```

![image-20250119222614301](D:\git_repository\cyber_security_learning\markdown_img\image-20250119222614301-1760090184682-1.png)



### ELasticsearch安装前准备



####  安装前环境初始化

```bash
CPU 2C
内存4G或更多
操作系统: Ubuntu22.04,Ubuntu20.04,Ubuntu18.04,Rocky8.X,Centos 7.X
操作系统盘50G
主机名设置规则为nodeX.wang.org
生产环境建议准备单独的数据磁盘
```



#####  主机名

```bash
#各服务器配置自己的主机名
[root@mystical ~]# hostnamectl set-hostname es-node1.mystical.org
```



##### 关闭防火墙和SELinux

关闭防所有服务器的防火墙和 SELinux

```bash
#RHEL系列的系统执行下以下配置
[root@es-node1 ~]# systemctl disable firewalld
[root@es-node1 ~]# systemctl disable NetworkManager
[root@es-node1 ~]# sed -i '/SELINUX/s/enforcing/disabled/' /etc/selinux/config
[root@es-node1 ~]# reboot

# Ubuntu
[root@es-node1 ~]# systemctl disable --now ufw
```



##### 各服务器配置本地域名解析

```bash
[root@es-node1 ~]# vim /etc/hosts
10.0.0.150 es-node1.mystical.org
10.0.0.151 es-node2.mystical.org
10.0.0.152 es-node3.mystical.org
```



##### 优化资源限制配置

**修改内核参数**

内核参数 `vm.max_map_count` 用于限制一个进程可以拥有的VMA(虚拟内存区域)的数量

使用默认系统配置，**二进制安装时会提示下面错误**，**包安装会自动修改此配置**

![image-20250119223514888](D:\git_repository\cyber_security_learning\markdown_img\image-20250119223514888-1760090184683-4.png)

```bash
#查看默认值
[root@ubuntu2204 ~]# sysctl -a |grep vm.max_map_count 
vm.max_map_count = 65530

[root@es-node1 ~]# sysctl -a |grep vm.max_map_count 
vm.max_map_count = 65530

#修改配置
[root@es-node1 ~]# echo "vm.max_map_count = 262144" >> /etc/sysctl.conf

#设置系统最大打开的文件描述符数
[root@es-node1 ~]# echo "fs.file-max = 1000000" >> /etc/sysctl.conf
[root@es-node1 ~]# sysctl -p 
vm.max_map_count = 262144

#Ubuntu22.04默认值已经满足要求
[root@ubuntu2204 ~]#sysctl fs.file-max
fs.file-max = 9223372036854775807
```



**范例: Ubuntu 基于包安装后会自动修改文件**

```bash
[root@node1 ~]#cat /usr/lib/sysctl.d/elasticsearch.conf
vm.max_map_count=262144
```



 **修改资源限制配置(可选)**

```bash
[root@es-node1 ~]#vi /etc/security/limits.conf
*               soft   core           unlimited
*               hard   core           unlimited
*               soft   nproc           1000000
*               hard   nproc           1000000
*               soft   nofile          1000000
*               hard   nofile          1000000
*               soft   memlock         32000
*               hard   memlock         32000
*               soft   msgqueue        8192000
*               hard   msgqueue        8192000
```



##### 关于JDK环境说明

```ABAP
1.x 2.x 5.x 6.x都没有集成JDK的安装包，也就是需要自己安装java环境
7.x 版本的安装包分为带JDK和不带JDK两种包，带JDK的包在安装时不需要再安装java，如果不带JDK的包
仍然需要自己去安装java
8.X 版本内置JDK，不再支持自行安装的JDK
```





### Elasticsearch 安装

#### 包安装 Elasticsearch

##### 安装 Elasticsearch 包

下载链接

```ABAP
https://www.elastic.co/cn/downloads/elasticsearch
https://mirrors.tuna.tsinghua.edu.cn/elasticstack/
```



![image-20250119224534985](D:\git_repository\cyber_security_learning\markdown_img\image-20250119224534985-1760090184683-2.png)



**范例：安装 elasticsearch-8**

```bash
#注意：是elasticsearch目录，不是enterprise-search目录
[root@ubuntu2204 ~]# wget https://mirrors.tuna.tsinghua.edu.cn/elasticstack/8.x/apt/pool/main/e/elasticsearch/elasticsearch-8.6.1-amd64.deb

[root@ubuntu2204 ~]# dpkg -i elasticsearch-8.6.1-amd64.deb
```



**安全验证**
8版本有安全验证，无法直接访问

```bash
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



##### 启动Elasticsearch

```bash
systemctl enable --now elasticsearch

# elasticsearch中内置的java包安装路径
[root@ubuntu2204 ~]#/usr/share/elasticsearch/jdk/bin/java --version
openjdk 22.0.1 2024-04-16
OpenJDK Runtime Environment (build 22.0.1+8-16)
OpenJDK 64-Bit Server VM (build 22.0.1+8-16, mixed mode, sharing)
```



##### 直接运行Elasticsearch报错

```bash
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
{"error":{"root_cause":[{"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":["Basic realm=/"security/", charset=/"UTF-8/"","Bearer realm=/"security/"","ApiKey"]}}],"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":["Basic realm=/"security/", charset=/"UTF-8/"","Bearer realm=/"security/"","ApiKey"]}},"status":401}
```



##### 使用安装服务后生成的密码进行认证访问

```bash
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



##### 如果image忘记，重置生成新密码

```bash
# 方法1：生成随机密码
/usr/share/elasticsearch/bin/elasticsearch password -u elastic

# 方法2：交互式生成指定密码
/usr/share/elasticsearch/bin/elasticsearch-reset-password --username elastic -i
```



**该安全加固会对后续的产生影响**

在实际生产中，Elasticsearch会不可避免的和各种其他服务进行通信，这个过程中该认证会产生很多麻烦，所以在内网安全可到保证的情况下，建议把该安全加固取消



##### 取消安全认证

```bash
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
# 调整JVM heap size，做实验可以将其调小，但是生产环境要保证足够
-Xms512m
-Xmx512m
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





#### 二进制安装Elasticsearch

官方文档

```http
https://www.elastic.co/guide/en/elasticsearch/reference/master/targz.html
```



##### 下载二进制文件

```http
https://www.elastic.co/cn/downloads/elasticsearch
```

![image-20250120180545468](D:\git_repository\cyber_security_learning\markdown_img\image-20250120180545468-1760090184683-3.png)



 **基于二进制包含JDK文件安装**

```bash
[root@es-node1 ~]# wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.15.0-linux-x86_64.tar.gz

[root@es-node1 ~]# ls
elasticsearch-8.15.0-linux-x86_64.tar.gz

# 解压至/usr/local
[root@es-node1 ~]# tar xf elasticsearch-8.15.0-linux-x86_64.tar.gz -C /usr/local/

# 创建软连接
[root@es-node1 ~]# ln -s /usr/local/elasticsearch-8.15.0/ /usr/local/elasticsearch
[root@es-node1 ~]# ls /usr/local/elasticsearch
bin  config  jdk  lib  LICENSE.txt  logs  modules  NOTICE.txt  plugins  README.asciidoc
```



**编辑服务配置文件（集群配置）**

```bash
# 关闭安全功能
[root@es-node1 /data/es-logs]# vim /usr/local/elasticsearch/config/elasticsearch.yml
# Enable security features
xpack.security.enabled: false

```



**修改ELK内存配置**

修改ELK内存配置，推荐使用宿主机物理内存的一半，最大不超过30G

```bash
[root@es-node1 ~]# vim /usr/local/elasticsearch/config/jvm.options
-Xms1g
-Xmx1g
```



**创建用户**

从ES7.X以后版不允许以root启动服务，需要委创建专用的用户

```bash
[root@es-node1 ~]# useradd -r elasticsearch
```



**目录权限更改**

在所有节点上创建数据和日志目录并修改目录权限为elasticsearchv

```bash
# 更改数据和日志目录
[root@es-node1 ~]# vim /usr/local/elasticsearch/config/elasticsearch.yml
path.data: /data/es-data
path.logs: /data/es-logs

[root@es-node1 /usr/local]# mkdir /data/es-{data,logs} -p
[root@es-node1 /usr/local]# chown -R elasticsearch.elasticsearch /data/

#修改elasticsearch安装目录权限
[root@es-node1 ~]# chown -R elasticsearch.elasticsearch /usr/local/elasticsearch/
```



**创建service文件**

```bash
[root@es-node2 ~]# vim /lib/systemd/system/elasticsearch.service
[Unit]
Description=Elasticsearch
Documentation=http://www.elastic.co
Wants=network-online.target
After=network-online.target

[Service]
RuntimeDirectory=elasticsearch
PrivateTmp=true
Environment=PID_DIR=/var/run/elasticsearch
WorkingDirectory=/usr/local/elasticsearch
User=elasticsearch
Group=elasticsearch
ExecStart=/usr/local/elasticsearch/bin/elasticsearch -p ${PID_DIR}/elasticsearch.pid --quiet
# StandardOutput is configured to redirect to journalctl since
# some error messages may be logged in standard output before
# elasticsearch logging system is initialized. Elasticsearch
# stores its logs in /var/log/elasticsearch and does not use
# journalctl by default. If you also want to enable journalctl
# logging, you can simply remove the "quiet" option from ExecStart.
# Specifies the maximum file descriptor number that can be opened by this process
LimitNOFILE=65535
# Specifies the maximum number of processes
LimitNPROC=4096
# Specifies the maximum size of virtual memory
LimitAS=infinity
# Specifies the maximum file size
LimitFSIZE=infinity
# Disable timeout logic and wait until process is stopped
TimeoutStopSec=0
# SIGTERM signal is used to stop the Java process
KillSignal=SIGTERM
# Send the signal only to the JVM rather than its control group
KillMode=process
# Java process is never killed
SendSIGKILL=no
# When a JVM receives a SIGTERM signal it exits with code 143
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target
```



**启动ELasticsearch服务**

在所有节点上配置并启动

```bash
[root@es-node1 ~]# echo 'PATH=/usr/local/elasticsearch/bin:$PATH' > /etc/profile.d/elasticsearch.sh
[root@es-node1 ~]# . /etc/profile.d/elasticsearch.sh
[root@es-node1 /usr/local]# systemctl start elasticsearch.service
[root@es-node1 /usr/local]# systemctl enable elasticsearch.service 
Created symlink /etc/systemd/system/multi-user.target.wants/elasticsearch.service → /lib/systemd/system/elasticsearch.service.
```



**验证端口监听成功**

```bash
[root@es-node1 /data/es-logs]# ss -nlt
State       Recv-Q      Send-Q                Local Address:Port           Peer Address:Port      Process   
LISTEN      0           4096                  127.0.0.53%lo:53                  0.0.0.0:*                   
LISTEN      0           128                       127.0.0.1:6010                0.0.0.0:*                   
LISTEN      0           128                         0.0.0.0:22                  0.0.0.0:*                   
LISTEN      0           4096             [::ffff:127.0.0.1]:9300                      *:*                   
LISTEN      0           4096                          [::1]:9300                   [::]:*                   
LISTEN      0           128                           [::1]:6010                   [::]:*                   
LISTEN      0           4096                              *:9200                      *:*                   
LISTEN      0           128                            [::]:22                     [::]:* 
```



**通过浏览器访问 Elasticsearch 服务端口**

```bash
[root@es-node1 /data/es-logs]# curl 10.0.0.150:9200
{
  "name" : "es-node1.mystical.org",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "5Igla64GQ8Ga5rBNDcQ8Zw",
  "version" : {
    "number" : "8.15.0",
    "build_flavor" : "default",
    "build_type" : "tar",
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



#### 多节点集群部署

##### 部署前准备

注意：此方式需要3G以上内存，否则会出现OOM报错

修改内核参数，默认无法启动，会出现下面错误提示

```ABAP
ERROR: [1] bootstrap checks failed
[1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```

```bash
[root@es-node1 ~]# echo vm.max_map_count=262144 >> /etc/sysctl.conf
[root@es-node1 ~]# sysctl -p
```



##### **服务端口解析**

```
9200端口：用于web访问
9300端口：用于集群内nodes之间通信
```



##### 集群配置

8.X 集群配置

```bash
#默认配置文件需要以下六行
[root@es-node1 ~]# vim /usr/local/elasticsearch/config/elasticsearch.yml 
cluster.name: my-application #指定集群名称，同一个集群内的所有节点相同
node.name: node-1            #修改此行，每个节点不同

# 集群模式必须修改此行，默认是127.0.0.1:9300,否则集群节点无法通过9300端口通信，每个节点相同
network.host: 0.0.0.0     
# 用于发现集群内节点地址
discovery.seed_hosts: ["10.0.0.150", "10.0.0.151", "10.0.0.152"] 
# 指定允许参与主节点选举的nodes
cluster.initial_master_nodes: ["10.0.0.150", "10.0.0.151", "10.0.0.152"]

# 下面这行和上面的相同，将其注释掉防止冲突
# cluster.initial_master_nodes: ["ubuntu2204.wang.org"]     #将此行注释

path.data: /data/es-data
path.logs: data/es-logs

# 改完后重启服务
[root@es-node1 /usr/local/elasticsearch]# systemctl restart elasticsearch

# 查看集群信息
[root@es-node1 /usr/local/elasticsearch/config]# curl 10.0.0.150:9200/_cat/nodes
10.0.0.152 34 96  3 0.30 0.18 0.20 cdfhilmrstw - node-3
10.0.0.150 33 72  7 0.28 0.19 0.10 cdfhilmrstw * node-1
10.0.0.151 41 96 27 0.79 0.25 0.12 cdfhilmrstw - node-2
```







## 优化ELK资源配置



### 开启bootstrap.memory_lock优化

**开启 bootstrap.memory_lock: true 可以优化性能，但会导致无法启动的错误解决方法**

注意：开启 `bootstrap.memory_lock: true` 需要足够的内存，建议4G以上，否则内存不足，启动会很失败或很慢

作用：用于在启动前给`Elasticsearch`预留充足的内存空间

```bash
# 开启此功能建议堆内存大小设置是总内存的一半，也就是内存充足的情况下使用
[root@es-node1 ~]# vim /etc/elasticsearch/elasticsearch.yml 
#开启此功能导8.X致集群模式无法启动,但单机模式可以启动
bootstrap.memory_lock: true

[root@es-node1 ~]# systemctl restart elasticsearch.service 
Job for elasticsearch.service failed because the control process exited with 
error code.
See "systemctl status elasticsearch.service" and "journalctl -xe" for details.

# #8.X致集群模式需要修改如下配置
#方法1：直接修改elasticsearch.service 
[root@es-node1 ~]# vim /lib/systemd/system/elasticsearch.service 
[Service]
#加下面一行
LimitMEMLOCK=infinity

# 更改后重启服务
[root@es-node2 /usr/local/elasticsearch]# systemctl daemon-reload 
[root@es-node2 /usr/local/elasticsearch]# systemctl restart elasticsearch.service
```



### 内存优化

**官方文档**

```http
https://www.elastic.co/guide/en/elasticsearch/reference/current/importantsettings.html#heap-size-settings
```



**推荐使用宿主机物理内存的一半，ES的heap内存最大不超过30G,26G是比较安全的**

```bash
堆大小应基于可用 RAM：
将 Xms 和 Xmx 设置为不超过总内存的 50%。 Elasticsearch 需要内存用于 JVM 堆以外的用途。 例如，Elasticsearch 使用堆外缓冲区来实现高效的网络通信，并依靠操作系统的文件系统缓存来高效地访问文件。 JVM 本身也需要一些内存。 Elasticsearch 使用比 Xmx 设置配置的限制更多的内存是正常的。在容器（例如 Docker）中运行时，总内存定义为容器可见的内存量，而不是主机上的总系统内存。将 Xms 和 Xmx 设置为不超过压缩普通对象指针 (oops) 的阈值。 确切的阈值会有所不同，但在大多数系统上 26GB 是安全的，在某些系统上可能高达 30GB。 要验证您是否低于阈值，请检查 Elasticsearch日志中的条目，如下所示：
```



#### **关于OOPS的说明**

```markdown
Managed pointers in the Java heap point to objects which are aligned on 8-byte address boundaries. Compressed oops represent managed pointers (in many but not all places in the JVM software) as 32-bit object offsets from the 64-bit Java heap base address.

Because they're object offsets rather than byte offsets, they can be used to address up to four billion objects (not bytes), or a heap size of up to about 32 gigabytes.

To use them, they must be scaled by a factor of 8 and added to the Java heap base address to find the object to which they refer. Object sizes using compressed oops are comparable to those in ILP32 mode.

Java 堆中的托管指针指向在 8 字节地址边界上对齐的对象。 压缩 oop 将托管指针（在 JVM 软件中的许多但不是所有地方）表示为相对于 64 位 Java 堆基地址的 32 位对象偏移量。
因为它们是对象偏移量而不是字节偏移量，所以它们可用于处理多达 40 亿个对象（不是字节），或高达约32GB的堆大小。
要使用它们，必须将它们缩放 8 倍并添加到 Java 堆基地址以找到它们所引用的对象。 使用压缩 oop 的对象大小与 ILP32 模式中的对象大小相当。
```



#### **关于 Heap 内存大小**

```markdown
虽然JVM可以处理大量的堆内存，但是将堆内存设置为过大的值可能导致以下问题：

堆内存分配的效率低。Java语言本身就是一种高级语言，这意味着需要更多的堆内存来存储对象。但是，当堆内存过大时，分配对象所需的时间也会相应增加，这可能会导致应用程序出现性能问题。

操作系统内存管理的限制。操作系统必须以页为单位进行内存管理。如果Java堆内存过大，则需要更多的页来管理堆内存。这可能会导致操作系统出现性能问题。

垃圾回收(Garbage Collection, GC)：JVM内存的一部分被用于存储对象，这些对象随着时间的推移可能不再需要。这些不再需要的对象被视为“垃圾”，需要由垃圾收集器清除，以释放内存空间。然而，执行GC会暂停所有的应用线程，这被称为 "Stop-the-World"（暂停世界）。这种暂停可能会影响应用的性能和响应时间。一般来说，如果堆内存非常庞大，GC需要检查和清理的对象数量会变得非常庞大，这会导致GC操作的时间变得非常漫长。

对象指针的大小：在某些JVM实现（例如Oracle的HotSpot），在堆（Heap）大小超过32GB之后，对象指针的表示将从32位压缩oops（Ordinary Object Pointers普通对象指针）转变为64位非压缩指针，这导致了内存使用的增加。如果内存设置接近或略超过32GB，实际上可能会因为此原因造成更多的内存消耗。因此，通常在32GB以下时，我们会使用32位压缩指针，而超过这个阈值时，除非有明确的需要，否则通常会选择保持在30GB左右以避免转为64位指针。

因此，建议将Java堆内存设置为合适的大小，以便在GC操作的同时与应用程序的性能之间进行平衡。通常情况下，堆内存应该设置为操作系统的物理内存的一半或三分之一。虽然这个数字可能会因系统配置和工作负载而有所变化，但是在32G的机器上，32G的堆空间已经超出了大部分Java应用程序的需求，因此更大的堆内存并不是必要的。

当然，根据具体的应用场景和需求，以及你使用的具体的JVM版本和垃圾收集器类型，这个30GB的规则并非绝对。比如ZGC和Shenandoah这类的低延迟垃圾回收器就可以处理大于30GB的堆内存，同时还能保持低停顿时间。
```



#### **内存优化建议**

为了保证性能，每个ES节点的JVM内存设置具体要根据 node 要存储的数据量来估算,建议符合下面约定

- 在内存和数据量有一个建议的比例：对于一般日志类文件，1G 内存能存储**48G~96GB**数据
- JVM 堆内存最大不要超过30GB
- 单个分片控制在30-50GB，太大查询会比较慢，索引恢复和更新时间越长；分片太小，会导致索引 碎片化越严重，性能也会下降

```bash
# 范例
#假设总数据量为1TB，3个node节点，1个副本；那么实际要存储的大小为2TB
每个节点需要存储的数据量为:2TB / 3 = 700GB，每个节点还需要预留20%的空间，所以每个node要存储大约 700*100/80=875GB 的数据；每个节点按照内存与存储数据的比率计算：875GB/48GB=18，即需要JVM内存为18GB,小于30GB
因为要尽量控制分片的大小为30GB；875GB/30GB=30个分片,即最多每个节点有30个分片

#思考：假设总数据量为2TB，3个node节点，1个副本呢？
```



#### **指定heap内存最小和最大内存限制**

```bash
#建议将heap内存设置为物理内存的一半且最小和最大设置一样大,但最大不能超过30G
[root@es-node1 ~]# vim /etc/elasticsearch/jvm.options 
-Xms30g
-Xmx30g

#每天产生1TB左右的数据量的建议服务器配置，还需要定期清理磁盘
16C 64G 6T硬盘 共3台服务器
```



#### **修改service文件，做优化配置**

```bash
[root@es-node1 ~]# vim /usr/lib/systemd/system/elasticsearch.service #修改内存限制
LimitNOFILE=1000000       #修改最大打开的文件数，默认值为65535
LimitNPROC=65535          #修改打开最大的进程数，默认值为4096
LimitMEMLOCK=infinity     #无限制使用内存，以前旧版需要修改，否则无法启动服务，8.X当前版本无需修改
```

