# Nacos介绍和架构
主要解决Java框架的微服务中的服务发现服务注册问题
主要解决2个问题
- Nacos服务注册集群
- Nacos配置中心集群


## Nacos核心功能
- 服务发现和服务健康监测
  - Nacos支持基于DNS和基于RPC的服务发现，服务提供者使用`原生SDK`、`OpenAPI`或一个`独立的Agent TODO`注册Service后，服务消费者可以使用`DNS TODO`或`HTTP&API`查找和发现服务。
  - Nacos提供对服务的实时的健康检测，阻止向不健康的主机或服务实例发送请求。Nacos支持传输层(PING或TCP)和应用程(如HTTP、MySQL、用户自定义)的健康检查。对于复杂的云环境和网络拓扑环境中(如VPC、边缘网络等)服务的健康检查，Nacos提供了agent上报模式和服务端主动检测2种健康检查模式。Nacos还提供了统一的健康检查仪表盘，帮助根据健康状态管理服务的可用性及流量

- 动态配置

- 动态DNS服务

- 服务及其元数据管理
Nacos能让您从微服务平台建设的视角管理数据中心的所有服务及元数据、包括管理服务的描述、生命周期、服务的静态依赖分析、服务的健康状态，服务的流量管理，路由及安全策略、服务的SLA以及最首要的metrics统计数据

## Nacos注册中心工作机制
### 服务提供者分类
- 临时实例：服务提供者主动向nacos发送心跳监测，如果一段时间后，nacos无法收到心跳，则删除此实例
- 非临时实例：nacos主动定时监测此类实例，如果提供者实例异常，则并不会删除只是标记此实例异常，等待此实例恢复

### 服务消费者
- 消费者定时向nacos注册中心Pull拉去提供者信息，并加以缓存
- 如果提供者有变化，nacos会主动向消费者PUSH推送消息通知，Eureka不支持主动PUSH

### 集群模式
- Nacos默认使用AP(Availability和Partition tolerance)模式，存在非临时实例，会采用CP(Consistency和Partition tolerance)模式
- Eurka采用AP模式

### 集群数据一致性实现
- CP模式基于Raft
- AP模式基于阿里的Distro（基于Gossip和Eureka协议优化而来）最终一致性的AP分布式协议

## Nacos部署
部署前准备好java环境
```shell
apt update && apt install -y openjdk-8-jdk
```
### Nacos单机部署
```shell
# 下载二进制包
wget https://github.com/alibaba/nacos/releases/download/2.4.0.1/nacos-server-2.4.0.1.tar.gz

# 解压至指定目录
tar xf nacos-server-2.4.0.1.tar.gz -C /usr/local/

# 修改配置，可选
vim /usr/local/nacos/conf/application.properties

# 添加PATH变量中，可选
echo 'PATH=/usr/local/nacos/bin:$PATH' >> /etc/profile
```

#### 启动和关闭服务器
```shell
# 启动服务
bash startup.sh -m standalone
```
```shell
# 将服务交给systemd管理
[root@ubuntu2204 ~]#systemctl cat nacos.service 
# /lib/systemd/system/nacos.service
[Unit]
Description=nacos.service
After=network.target

[Service]
Type=forking
#Environment=
ExecStart=/usr/local/nacos/bin/startup.sh -m standalone
ExecStop=/usr/local/nacos/bin/shutdown.sh

[Install]
WantedBy=multi-user.target

# 启用systmed
systemctl daemon-reload
systemctl restart nacos
```

#### 关闭服务
```shell
sh shutdown.sh
```


#### 服务注册&发现和配置管理
```shell
# 服务注册
# 固定格式：curl -x POST 'http://127.0.0.1:8848/nacos/v1/ns/instance?serviceName=
# 临时注册，过段时间就没了
curl -X POST 'http://127.0.0.1:8848/nacos/v1/ns/instance?serviceName=nacos.wang.serviceName&ip=1.2.3.4&port=8080'

# 服务发现
curl -X GET 'http://127.0.0.1:8848/nacos/v1/ns/instance/list?serviceName=nacos.wang.serviceName'

# 发布配置
curl -X POST "http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=nacos.cfg.dataId&group=test&content=HelloWorld"

# 获取配置
curl -X GET "http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=nacos.cfg.dataId&group=test"

# 范例：生成配置
curl --location --request POST 'http://127.0.0.1:8848/nacos/v1/cs/config?import=true&namespace=pulic' --form 'policy=OVERWRITE' --form 'file=@"/PATH/ZIP_FILE"'
```

#### Nacos中的名称空间
- Nacos中的名称空间和K8S中的差不多，都是为了实现服务分组，服务隔离的作用

#### 单机模式支持MySQL
```shell
# 安装数据库
apt update && apt -y install mysql-server

# 给nacos创建数据库，账号，并授权
create database nacos;
create user nacos@'127.0.0.1' identified with mysql_native_password by '123456';
grant all on nacos.* to nacos@'127.0.0.1';

# 将数据文件导入数据库
mysql -unacos -p123456 -h127.0.0.1 nacos < /usr/local/nacos/conf/mysql-schema.sql

# 修改配置，让其使用数据库存放数据
vim /usr/local/nacos/conf/application.properties
```

#### 开启鉴权
```shell
# 生成token的值，至少32位，否则无法启动
openssl rand -base64 32

# 修改配置文件，共四行内容
vim /usr/local/nacos/conf/application.properties
nacos.core.auth.enabled=true    # 修改此行为true
nacos.core.auth.server.identity.key=wang
nacos.core.auth.server.identity.value=wang
nacos.core.auth.plugin.nacos.token.secret.key=XXX # 前面生成的token
```

### Nacos集群部署
#### 部署MySQL做为数据源
```shell
# 安装数据库
apt update && apt install -y mysql-server

# 改为可远程访问
sed -i '/127.0.0.1/s/^/#/' /etc/mysql/mysql.conf.d/mysqld.cnf

# 按单机配置，将mysql账号，授权和数据库配置好
```

#### 在三台机器上安装nacos

#### 配置集群配置文件
在nacos的解压目录nacos/conf目录下，有配置文件cluster.conf，请每行配置成ip:port
```shell
vim /usr/local/nacos/conf/cluster.conf
#ip:port
10.0.0.131:8848
10.0.0.132:8848
10.0.0.133:8848

# 所有节点同步配置
for i in {132..133} ; do scp /usr/local/nacos/conf/cluster.conf 10.0.0.$i: ; done

# 修改配置文件，将mysql选项打开，并将地址改为远程mysql的地址，同上，注意地址

# 更改service文件，将-m standalone去掉
# 重启
systemctl daemon-reload
systemctl restart nacos
```

#### 配置haproxy负载均衡
```shell
#修改内核参数
[root@ubuntu2204 ~]#echo net.ipv4.ip_nonlocal_bind = 1 >> /etc/sysctl.conf
[root@ubuntu2204 ~]#sysctl -p
#在两台服务器上安装配置haproxy实现负载均衡反向代理和高可用
[root@ubuntu2204 ~]#apt update && apt -y install haproxy 
[root@ubuntu2204 ~]#vim /etc/haproxy/haproxy.cfg
#添加下面行
listen stats
   mode http
   bind 0.0.0.0:9999
   stats enable
   log global
   stats uri     /haproxy-status
   stats auth   admin:123456
listen nacos-8848
    #mode tcp
   bind 10.0.0.100:8848
   server nacos01 10.0.0.201:8848 check
   server nacos02 10.0.0.202:8848 check
   server nacos03 10.0.0.203:8848 check
    
listen nacos-9848
   mode tcp
   bind 10.0.0.100:9848
   server nacos01 10.0.0.101:9848 check
   server nacos02 10.0.0.102:9848 check
   server nacos03 10.0.0.103:9848 check
    
    
[root@ubuntu2204 ~]#systemctl reload haproxy
#在两台服务器上安装配置keepalived实现高可用
[root@ubuntu2204 ~]#apt update && apt -y install keepalived
#/usr/share/doc/keepalived/samples/keepalived.conf.sample
#/usr/share/doc/keepalived/samples/keepalived.conf.vrrp.localcheck
#参考上面文件修改配置文件
[root@ubuntu2204 ~]#vim /etc/keepalived/keepalived.conf 
! Configuration File for keepalived
global_defs {
   router_id ka1           #另一台主机上为ka2
}
vrrp_script chk_haproxy {
       script "killall -0 haproxy"     # cheaper than pidof
       interval 1
       weight -30
}

vrrp_instance VI_1 {
   interface eth0
   virtual_router_id 66
   state MASTER              #另一台主机上为BACKUP
   priority 100              #另一台主机上为80
   advert_int 1
   authentication {
       auth_type PASS
       auth_pass 123456
   }
   virtual_ipaddress {
        10.0.0.100/24 dev eth0 label eth0:1
   }
   track_script {
       chk_haproxy 
   }
}
[root@ubuntu2204 ~]#systemctl restart keepalived
#浏览器访问haproxy的管理页,用户名/密码:admin/123456
http://10.0.0.100:9999/haproxy-status
```

### Nacos实战案例



# Sentinel
主要解决限流限速，流量控制的问题




# Seata
主要解决分布式事务的问题
