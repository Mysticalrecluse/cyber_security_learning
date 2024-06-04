## Zabbinx部署

## Zabbix核心功能
### 监控主机

### 监控服务

### 自定义监控项

客户端可以自定义监控项，在Zabbix Agent配置文件添加内容，格式如下
```shell
# cat /etc/zabbix/zabbix_agentd.conf
# cat /etc/zabbix/zabbix_agent2.conf
UserParameter=<key>,<shell command>
Include=/etc/zabbix/zabbix_agent.d/*.conf

# 或者创建独立的自定义文件
# cat /etc/zabbix/zabbix_agentd.d/*.conf
# cat /etc/zabbix/zabbix_agent2.d/*.conf

# 格式1：一般形式的自定义监控项
UserParamter=<key>,<shell command>
# 格式2：参数形式的自定义监控项
UserParamter=<key>[*],<shell command> $1 $2... 
```

示例
```shell
# vim /etc/zabbix/zabbix_agent.d/tcp.conf
UserParameter=tcp_listen,netstat -lant|grep -ci listen
UserParameter=tcp_time_wait,netstat -lant|grep -ci time_wait
UserParameter=establish,netstat -lant|grep -ci establish
```

测试监控项是否生效
```shell
zabbix_agentd -t tcp_listen
tcp_listen                 [t|7]
```

使用zabbix-get在监测端测试
```shell
zabbix_get -s 10.0.0.151 -k tcp_listen
```

zabbix-agentd后端配置好后

前端流程：
```shell
1. 创建模板
2. 给模板添加监控项
3. 在被监控主机上添加该模板
```