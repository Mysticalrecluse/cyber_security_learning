# JumpServer

## JumpServer安装

### 基于Docker部署

#### 前置条件

- 使用外置MySQL数据库和Redis
    - 外置数据库要求MariaDB版本大于等于10.6
    - 外置Redis要求Redis版本大于等于6.2

- 建议内存8G左右

#### 部署Mysql容器

将宿主机的设置好的配置文件挂载至MySQL容器
```shell
# 默认MySQL8.0的验证插件是caching_sha2_password, 不符合要求，需要修改mysql_native_password
cat mysqld.cnf
[mysqld]
default_authentication_plugin=mysql_native_password
```

启动mysql容器
```shell
#jumpserver-v3.4.3基于MySQL8.0
docker run -d -p 3306:3306 --name mysql --restart always \
-e MYSQL_ROOT_PASSWORD=123456 \
-e MYSQL_DATABASE=jumpserver  \
-e MYSQL_USER=jumpserver      \
-e MYSQL_PASSWORD=123456      \
-v /data/mysql:/var/lib/mysql \
-v ./mysqld.cnf:/etc/mysql/conf.d/mysqld.cnf \
mysql:8.0.29-oracle
```

#### 部署redis
```shell
docker run -d -p 6379:6379 --name redis --restart always redis:7.2.5 redis-server --requirepass 123456
```

#### 部署jumpserver

```shell
docker pull jumpserver/jms_all:v3.10.11
```

```shell
 docker run --name jms_all -d \-p 80:80 \-p 2222:2222 \-p 30000-30100:30000-30100 \-e SECRET_KEY=xeqKd4FW2Yn0xZ8w7eKxLJN0ponWOwj5tolgoR8c2TlbIB9rsw \-e BOOTSTRAP_TOKEN=mGNRiYinwrbfv8dg3iFIuex2 \-e LOG_LEVEL=ERROR \-e DB_HOST=10.0.0.168 \-e DB_PORT=3306 \-e DB_USER=jumpserver \-e DB_PASSWORD=123456 \-e DB_NAME=jumpserver \-e REDIS_HOST=10.0.0.168 \-e REDIS_PORT=6379 \-e REDIS_PASSWORD=123456 \--privileged=true \-v /opt/jumpserver/core/data:/opt/jumpserver/data \-v /opt/jumpserver/koko/data:/opt/koko/data \-v /opt/jumpserver/lion/data:/opt/lion/data \-v /opt/jumpserver/core/data:/opt/jumpserver/data \-v /opt/jumpserver/koko/data:/opt/koko/data \-v /opt/jumpserver/lion/data:/opt/lion/data \-v /opt/jumpserver/kael/data:/opt/kael/data \-v /opt/jumpserver/chen/data:/opt/chen/data \-v /opt/jumpserver/web/log:/var/log/nginx \
jumpserver/jms_all:v3.10.11
```