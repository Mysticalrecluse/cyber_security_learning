# 考前架构整理

## DNS主从


- 主DNS服务器
  - 软件安装


  - 更改DNS配置文件
  - 更改/etc/bind/named.conf.default-zones
  - 创建区域数据库文件
  - 增加数据库模板
    - TTL_TIME
    - DNS_VERSION
    - DNS_Master_IP
    - DNS_Slave_IP
    - Web1_IP
  - 增加DNS远程开启和关闭脚本

- 从DNS服务器
  - 创建slaves文件夹并更改权限
  - 修改apparmor.d/usr.sbin.named
  - 重新加载apparmor
  - 

## 