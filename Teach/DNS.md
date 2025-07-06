# DNS
## DNS总体思路和目的
### DNS的主要思路
- 分层的，基于域的命名机制，即层次化命名
    - 解决：一个平面命名的重名问题，以及名称更有意义了
- 分布式数据库维护
    - 解决1：可靠性问题：单点故障
    - 解决2：扩展性问题：通信容量
    - 解决3：维护问题：远距离集中式数据库


### DNS的主要目的
- 实现主机名 --> IP地址的转换 (A)
- 其他目的
    - 主机别名到规范名称的转换（CNAME）
        - 规范名称是为了便于管理
        - 别名是为了用户访问
    - 负载均衡（CNAME+A）
```shell
www    CNAME    websrv
websrv    A      10.0.0.6
websrv    A      10.0.0.7
# 此时用户访问www，流量会被均摊到6,7两台服务器上，从而实现服务器性能的提升
```


## DNS域名结构
- DNS采用层次树状结构的命名方法
- 最上面是根域(13个)（10个美国，2个欧洲，1个日本）
- 树叶到根表示主机名
- 树干到根表示域名


## DNS查询方式
- 迭代查询
  - DNS 服务器另外一种查询方式为迭代查询，DNS 服务器会向客户机提供其他能够解析查询请求的DNS服务器地址，当客户机发送查询请求时，DNS 服务器并不直接回复查询结果，而是告诉客户机另一台DNS 服务器地址，客户机再向这台DNS 服务器提交请求，依次循环直到返回查询的结果为止。
- 递归查询
  - 递归查询是一种DNS 服务器的查询模式，在该模式下DNS 服务器接收到客户机请求，必须使用一个准确的查询结果回复客户机。如果DNS 服务器本地没有存储查询DNS 信息，那么该服务器会询问其他服务器，并将返回的查询结果提交给客户机。

## DNS记录
- DNS本身可以看做：保存资源记录(RR)的分布式数据库

### RR格式
```shell
# RR格式
name ttl class type value
```

### 常用Type
- 记录类型：A，AAAA，PTR， SOA， NS， CNAME， MX
- Type=A
  - Name为主机
  - Value为Ip地址

- Type=CNAME
  - Name为规范名称的别名
  - value为规范名称

- Type=NS
  - Name域名（如foo.com）
  - Value为该域名的权威服务器主机名

- SOA：Start Of Authority（权威），起始授权记录：一个区域解析库有且仅有一个SOA记录，必须位于解析库的第一条记录
- A：Internet Addresses：作用：FQDN -> IP
- AAAA: FQDN -> IPv6
- PTR: IP -> FQDN
- NS：NAME Service，专用于标明当前区域的DNS服务
- CNAME：Canonical Name，别名记录
- MX：邮件交换器
- TXT：对域名进行标识和说明的一种方式

## 实际案例
```shell
$TTL 3600
@   IN  SOA  ns-1234.awsdns-56.org. awsdns-hostmaster.amazon.com. (
            2023090601 ; Serial
            7200        ; Refresh
            900         ; Retry
            1209600     ; Expire
            86400 )     ; Minimum TTL

; Name servers
@   IN  NS   ns-1234.awsdns-56.org.
@   IN  NS   ns-5678.awsdns-12.co.uk.
@   IN  NS   ns-9101.awsdns-23.net.
@   IN  NS   ns-1122.awsdns-34.com.

; A records for name servers
ns-1234.awsdns-56.org.   IN  A    192.0.2.11
ns-5678.awsdns-12.co.uk. IN  A    192.0.2.12
ns-9101.awsdns-23.net.   IN  A    192.0.2.13
ns-1122.awsdns-34.com.   IN  A    192.0.2.14

; A records for other hosts
@               IN  A    192.0.2.1      ; example.com
www             IN  A    192.0.2.2      ; www.example.com
api             IN  A    192.0.2.3      ; api.example.com

; CNAME records
ftp             IN  CNAME www.example.com. ; ftp.example.com points to www.example.com

; MX records
@               IN  MX   10 mail.example.com. ; Mail server with priority 10

; TXT records
@               IN  TXT  "v=spf1 a mx -all" ; SPF record for email validation
```

## 权威DNS服务器(SOA)
```shell
cat feng.org.zone
$TTL 86400

@ IN SOA master.ns1 mysticalrecluse.gmail.com (129 1h 10m 1D 12h)

@ NS master.ns1   # 表示对于这个域名，master.ns1 是负责回答 DNS 查询的服务器之一
@ NS slave.ns2
sub NS ns3

slave.ns2 A 10.0.0.123
master.ns1 A 10.0.0.121
ns3 A 10.0.0.124

www A 10.0.0.122
```

```shell
$TTL 86400
# 一个小时做一次拉取操作，如果失败了10分钟后重试，当从服务器和主服务器无法同步，一天之后，从主将无法对外提供服务，最后一个参数：错误结果缓存时间
@ IN SOA ns1.magedu.org admin.magedu.org (123, 1h, 10m, 1D, 12h)
ns1.magedu.org IN A 10.0.0.8

#： ns1.magedu.org: 表示当前维护magedu.org这个域的服务器的名称（我是谁）

#： 后面需要补一个
ns1.magedu.org IN A 10.0.0.33  # 我在哪

# admin.magedu.org: 域名服务器的管理员邮箱，指代admin@magedu.org

# 123: 该数据库版本名称
# 1h: 每隔一个小时从服务器从主服务器拉取数据，（是否更新的判断是版本号）
# 10m: 如果同步失败，则每10分钟重新尝试一次
# 1D：如果1天以上都无法实现同步，则从服务器数据失效
# 12h: 错误访问记录的缓存有效期，即如果用户查找一个不存在数据库中的域名，则定一个缓存有效期，12个小时内，用户如果继续访问，则直接返回该记录不存在。（否定答案的TTL值 ）
```
- 主服务器和从服务器之间一般有两种操作：一种是推push，一种是拉pull
  - 主服务器数据变了，主动把数据推送给从服务器
  - 从服务器定时从主服务器 拉取数据，查看是否更新

- NS：通过NS记录，判断当前数据库中，有哪些主从服务器
  - 对NS记录而言，任何一个ns记录后面的服务器名称，都应该在后续有一个A记录
```shell
@ IN NS ns1       # 主服务器 
@ IN NS ns2       # 从服务器
ns1 IN NS ip_addr
ns2 IN NS ip_addr
```

## 子域服务器
```shell
$TTL 86400

@ IN SOA sub.feng.org mysticalrecluse.gmail.com (12 1h 10m 1D 12h)

@ NS sub.feng.org 

sub.feng.org A 10.0.0.124

test A 10.0.0.122
```

#### 全局转发
- 对非本机所负责解析区域的请求，全转发给指定的服务器
- 在全局配置块中实现：
```shell
Options {
  forward first| only;
  forwarders { ip; };
}
# first 表示如果转发给的DNS服务器上没有需要的记录，则自己去互联网查询
# only 表示如果转发给的DNS服务器上没有需要的记录，直接返回失败，自己本身不去查询
```

#### 特定区域转发
- 仅转发特定的区域请求，比全局转发优先级高
```shell
zone "ZONE_NAME" IN {
  type forward;
  forward first | only;
  forwarders { ip; };
}
```

### 反解析
```shell
# vim /etc/bind/named.conf.default.zones
zone "0.0.10.in-addr.arpa" {
        type master;
        file "/etc/bind/db.0.0.10.in-addr.arpa";
};

# vim /etc/bind/db.0.0.10.in-addr.arpa
$TTL 86400
@ IN SOA ptr mysticalrecluse.gmail.com (223 1H 10m 1D 12h)
@ NS ptr
ptr A 10.0.0.101
10 PTR www.fengxx.com.

# 测试 dig -x 10.0.0.10 @10.0.0.101
```

## CDN



![image-20250630091204881](../markdown_img\image-20250630091204881.png)

如图所示，Origin Server（源站）是指业务服务器所在的原始站点。如果没有经过 CDN 加速，那么全球用户在下载资源时，需要与该源站进行网络交互。如果使用了 CDN 加速，用户的请求就可以通过距离自己地理位置较近的 CDN Server 来处理。因为 CDN 服务器分布在全球各地，所以用户请求的路径就会大大缩短，进而提升性能。



想要实现就近调度，CDN 就要解决这样几个问题：



- 怎样让用户本来去 Origin Server 的请求，转移到 CDN Server 上？	

  > CNAME

- 怎么找到用户地理位置较近的 CDN Server 的？

- CDN Server 上的资源是怎么来的？



DNS 的解析结果可以是 CNAME，用来将一个原始的域名映射到另一个域名。所以我们只需修改原始域名的 DNS 结果为 CNAME CDN 加速域名，原始域名的请求就会被转发到 CDN 加速域名，从而实现流量的重新定向。

所以，只需要将访问源站用的原始域名 CNAME 到 CDN 的加速域名，后续的流量调度就会交由 CDN 处理了

![image-20250630091618510](D:\git_repository\cyber_security_learning\markdown_img\image-20250630091618510.png)









- 客户端请求
  - 客户端（例如，浏览器）发送请求到服务器上的资源，比如一个网页或图像

- 请求到达CDN
  - CDN（内容分发网络）作为中间层，通常会在请求到达源站之前进行处理。
  - 客户端的请求会被转发到就近的 CDN 节点（即最接近客户端的 CDN 服务器）。
  ```shell
  www.example.com. IN CNAME example.cdnprovider.com.
  ```

- CDN 节点处理
  - CDN 节点缓存检查: CDN 节点会首先检查自己是否缓存了客户端请求的资源。如果资源已经存在于 CDN 的缓存中，CDN 会直接从缓存中响应客户端请求。
  - 如果资源在缓存中: CDN 节点将直接将缓存的资源返回给客户端，避免了对源站的额外请求，这样可以减少延迟和减轻源站的负担。
  - 如果资源不在缓存中: CDN 节点需要从源站拉取资源。

- 请求转发到源站
  - 从CDN到源站: 如果 CDN 节点没有缓存请求的资源，它会将请求转发到源站服务器（原始服务器），即资源的真正来源地
  
- 源站响应
  - 源站获取资源: 源站接收到来自 CDN 节点的请求后，将响应请求并将资源发送回 CDN 节点。
  - 缓存资源: 在将资源发送回客户端之前，CDN 节点会将资源存储到自己的缓存中，以便未来的请求可以更快地处理。

- 资源返回客户端
  - 从CDN返回: CDN 节点将从源站获取的资源返回给客户端，同时缓存这些资源以供将来使用。

### 配置CDN的实际情况
作为域名所有者，你通常不需要直接配置 CDN 域名的 A 记录，因为这些记录是由 CDN 提供商管理的。你只需要确保你的自定义域名的 CNAME 记录正确指向 CDN 提供商的域名。

CDN 提供商管理 DNS: CDN 提供商会负责管理其域名的 A 记录，确保 CDN 节点的 IP 地址是最新的。这些 IP 地址的更新和管理通常都是透明的，对于使用 CDN 的用户来说，CDN 提供商会自动处理。
