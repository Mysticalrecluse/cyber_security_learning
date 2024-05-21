### 网络防火墙
#### NAT网络转换原理

NAT: (Network Address Translation) 网络地址转换

局域网中的主机都是分配的私有IP地址，这些IP地址在互联网上是可不达到，局域网中的主机，在与互联网通讯时，要经过网络地址转换，去到互联网时，变成公网IP地址对外发送数据。服务器返回数据时，也是返回到这个公网地址，再经由网络地址转换返回给局域网中的主机。

一个局域网中的主机，想要访问互联网，在出口处，应该有一个公网可达的IP地址，应该能将局域网中的IP地址通过NAT转换成公网IP

NAT的分类
- SNAT (Source NAT) 
    - 源地址转换，修改请求报文中的源IP地址
- DNAT (Destination NAT)
    - 目标地址转换，修改响应报文中的目标IP地址
- PNAT (Port Nat)
    - 端口转换，IP地址和端口都进行转换


#### SNAT 实现源IP地址转换

SNAT：Source NAT: 源地址转换，基于nat表，工作在POSTROUTING链上。
具体是指将经过当前主机转发的请求报文的源IP地址转换成根据防火墙规则指定的IP地址

格式
```shell
iptables -t nat -A POSTROUTING -s LocalNet ! -d localNet -j SNAT --to-source ExtIP [--random]

# --to-source   转换成指定IP，或指定范围内的IP，端口可选
```

示例
```shell
iptables -t nat -A POSTROUTING -s 10.0.0.108 ! -d 10.0.0.108 -j SNAT --to-source 192.168.10.151
```

#### MASQUERADE 实现源IP地址转换

如果我们内网的出口设备上有固定IP，则直接指定--to-srouceIP，没有任何问题。但是如果是使用拨号上网，出口网络设备上的IP地址会发生变化，这种情况下，我们的出口IP不能写出固定的

这种场景下，我们需要使用MASQUERADE进行地址转换，MASOUERADE可以从主机网卡上自动获取IP地址作为出口IP地址

格式
```shell
iptables -t nat -A POSTROUTING -s localNET ! -d locatNet -j MASQUERADE [--to-ports port]     # MASQUEADE可以从主机网卡上自动获取 
```


#### DNAT 实现目标与IP地址转换

在内网换环境中，使用私有IP地址的设备需要与互联网进行时，需要借助出口设备将原内部IP地址转换成公网可达的IP地址可以再次隐藏

DNAT：Destination NAT, 目标地址转换，基于nat表，工作在PREROUTIe.

```shell
iptales -t nat -A PREPOUTING -d 192.168.10.123 -p tcp --dport 80 -j DNAT --to-destination 192.168.10.150:80
```

DNAT 只能将一条请求规则重定向到一台后端主机，无法实现负载均衡

#### REDIRECT 实现本机端口转换

REDIRECT：重定向，通过定义规则，将收到的数据包转发至同一主机的不同端口
REDIRECT 功能无需开启内核ip_forward转发

格式
```shell
iptables -t nat -A PREROUTING -d ExtIP -p tcp|udp -dport PORT -j REDIRECT --to-ports PORT
```

#### iptables中的自定义链

iptables中除了系统自带的五个链之外，还可以自定义链，来实现讲规则进行分组，重复调用的目的

自定义链添加规则之后，要作为系统链的target与之关联，才能起到作用

```shell
# 添加自定义链
iptables -t filter -N web_chain

# 修改自定义链的名称
iptables -t filter -E web_chain WEB_CHAIN

# 向自定义链添加规则
iptables -t filter -A WEB_CHAIN -p tcp -m multiport -dports 80,443 -j ACCEPT

# 将自定义链挂到系统链上
iptables -t filter -I INPUT 2 -J WEB_CHAIN
```

在使用单独的自定义链的情况下，如果需要修改，则只需要修改链上的具体规则，而不用修改自定义链与系统链的关联关系

```shell
# 单独修改自定义链的规则
iptables -t filter -R WEB_CHAIN 1 -p tcp -m multiport --dports 80,443,8080 -j ACCEPT

# 删除自定义链
iptables -t filter -X WEB_CHAIN

# 如果自定义链中还有规则，无法删除
```