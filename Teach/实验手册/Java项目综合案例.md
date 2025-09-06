# Java项目综合案例



## 若依 RuoYi 单体服务项目构建案例



### 下载项目

```bash
# 下载资源
[root@ubuntu2204 ~]#git clone https://gitee.com/lbtooth/RuoYi.git

# 查看
[root@ubuntu2204 ~]#ls
bin  Dockerfile              kubernetes  pom.xml    ruoyi-admin   ruoyi-framework  ruoyi-quartz   ruoyi-system  ry.sh      ry.sh-java17
doc  Dockerfile-multi-stage  LICENSE     README.md  ruoyi-common  ruoyi-generator  ruoyi.service  ry.bat        ry.sh.bak  sql
```



### 准备数据库

```bash
# 安装和配置MySQL
[root@ubuntu2204 ~]#apt update && apt install -y mysql-server
[root@ubuntu2204 ~]#sed -i '/127.0.0.1/s/^/#/' /etc/mysql/mysql.conf.d/mysqld.cnf 
[root@ubuntu2204 ~]#systemctl restart mysql

# 查看数据库脚本
[root@ubuntu2204 ~]#ls sql/
quartz.sql  ruoyi.html  ruoyi.pdm  ry_20240112.sql

# 准备数据库表和数据及用户
[root@ubuntu2204 ~]# mysql
......
mysql> create database ry;                            # 创建数据库
Query OK, 1 row affected (0.01 sec)

mysql> create user ry@'%' identified by '123456';     # 创建用户
Query OK, 0 rows affected (0.01 sec)

mysql> grant all on ry.* to ry@'%';                   # 授权
Query OK, 0 rows affected (0.00 sec)

mysql> use ry                                         # 进入数据库
Database changed
mysql> source RuoYi/sql/ry_20240112.sql               # 导入数据
mysql> source RuoYi/sql/quartz.sql                    # 导入数据
mysql> show tables;                                   # 查看导入的数据表
+--------------------------+
| Tables_in_ry             |
+--------------------------+
| QRTZ_BLOB_TRIGGERS       |
| QRTZ_CALENDARS           |
| QRTZ_CRON_TRIGGERS       |
| QRTZ_FIRED_TRIGGERS      |
| QRTZ_JOB_DETAILS         |
| QRTZ_LOCKS               |
| QRTZ_PAUSED_TRIGGER_GRPS |
| QRTZ_SCHEDULER_STATE     |
| QRTZ_SIMPLE_TRIGGERS     |
| QRTZ_SIMPROP_TRIGGERS    |
| QRTZ_TRIGGERS            |
| gen_table                |
| gen_table_column         |
| sys_config               |
| sys_dept                 |
| sys_dict_data            |
| sys_dict_type            |
| sys_job                  |
| sys_job_log              |
| sys_logininfor           |
| sys_menu                 |
| sys_notice               |
| sys_oper_log             |
| sys_post                 |
| sys_role                 |
| sys_role_dept            |
| sys_role_menu            |
| sys_user                 |
| sys_user_online          |
| sys_user_post            |
| sys_user_role            |
+--------------------------+
31 rows in set (0.00 sec)
mysql> exit;                            # 退出

# 修改连接MySQL的配置
[root@ubuntu2204 ~]#cat RuoYi/ruoyi-admin/src/main/resources/application-druid.yml 
# 数据源配置
spring:
    datasource:
        type: com.alibaba.druid.pool.DruidDataSource
        driverClassName: com.mysql.cj.jdbc.Driver
        druid:
            # 主库数据源，修改数据名称和用户密码
            # 数据库地址：mysql.wang.org:3306
            # 用户名：ry
            # 密码：123456
            master:
                url: jdbc:mysql://mysql.wang.org:3306/ry?useUnicode=true&characterEncoding=utf8&zeroDateTimeBehavior=convertToNull&useSSL=true&serverTimezone=GMT%2B8
                username: ry
                password: 123456
```



### 域名解析

```bash
#注意:mysql.wang.org 需要通过/etc/hosts或DNS实现名称解析,这里的IP是MySQL所在的服务器IP
[root@ubuntu2204 ~]#cat /etc/hosts
10.0.0.201 mysql.wang.org 
```



### 构建Java项目

```bash
[root@ubuntu2204 ~]#apt update && apt -y install maven
[root@ubuntu2204 ~]#cd RuoYi/
[root@ubuntu2204 RuoYi]#mvn clean package -Dmaven.test.skip=true

# 运行
[root@ubuntu2204 RuoYi]#java -jar ruoyi-admin/target/ruoyi-admin.jar
......
16:25:41.400 [main] INFO  c.r.RuoYiApplication - [logStarted,61] - Started RuoYiApplication in 9.927 seconds (JVM running for 10.639)
(♥◠‿◠)ﾉﾞ  若依启动成功   ლ(´ڡ`ლ)ﾞ  
 .-------.       ____     __        
 |  _ _   \      \   \   /  /    
 | ( ' )  |       \  _. /  '       
 |(_ o _) /        _( )_ .'         
 | (_,_).' __  ___(_ o _)'          
 |  |\ \  |  ||   |(_,_)'         
 |  | \ `'   /|   `-'  /           
 |  |  \    /  \      /           
 ''-'   `'-'    `-..-'   
 
# 查看浏览器
```

![image-20250827162719212](../../markdown_img/image-20250827162719212.png)



### 使用Service方式管理服务

```bash
[root@ubuntu2204 ~]#cp RuoYi/ry.sh /srv/
[root@ubuntu2204 ~]#cp RuoYi/ruoyi-admin/target/ruoyi-admin.jar /srv
[root@ubuntu2204 ~]#ls /srv
ruoyi-admin.jar  ry.sh

# 修改官方脚本bug
[root@ubuntu2204 ~]#vim /srv/ry.sh
# JVM参数
# 将JVM_OPTS改为如下配置
JVM_OPTS="-Dname=$AppName  -Duser.timezone=Asia/Shanghai -Xms512m -Xmx1024m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m -XX:+HeapDumpOnOutOfMemoryError  -XX:+PrintGCDetails -XX:NewRatio=1 -XX:SurvivorRatio=30 -XX:+UseParallelGC -XX:+UseParallelOldGC"

 #创建service文件
[root@ubuntu2204 ~]#vim /lib/systemd/system/ruoyi.service
[Unit]
Description=Ruoyi
After=network.target

[Service]
Type=forking
ExecStart=/srv/ry.sh start
ExecStop=/srv/ry.sh stop
LimitNOFILE=10000

[Install]
WantedBy=multi-user.target

# 启用
[root@ubuntu2204 ~]#systemctl daemon-reload ;systemctl enable --now ruoyi

# 浏览器查看
```

![image-20250827164229887](../../markdown_img/image-20250827164229887.png)



### 登录访问

```bash
http://10.0.0.201/login

#默认用户名/密码
admin/admin123 
```

![image-20250827164411957](../../markdown_img/image-20250827164411957.png)

![image-20250827164442264](../../markdown_img/image-20250827164442264.png)





## 若依RuoYi单体服务基于容器化构建













