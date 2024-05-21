## MySQL安装

### 包管理器进行安装
```shell
# 下载mysql源的配置文件
# Ubuntu
https://dev.mysql.com/downloads/repo/apt/
# Rokcy
https://dev.mysql.com/downloads/repo/apt/

# 以Rokcy为例，下载mysql
yum list "mysql*"

yum install -y mysql-server
```


### 二进制包安装

这里的二进制包是指已经编译完成，以压缩包提供下载的文件，下载到本地之后释放到自定义目录，在进行配置即可

范例：Rocky中安装mysql8.0
```shell
# 安装依赖
yum -y install libaio numactl-libs ncurses-compat-libs

# 创建用户和组
groupadd -r mysql
useradd -r -g mysql -s /sbin/nologin mysql

# 下载二进制包
wget https://dev.mysql.com/get/Downloads/MySQL-8.4/mysql-8.4.0-linux-glibc2.28-x86_64.tar.xz

# 解压至指定目录，这个目录只能写 /usr/local
tar xf mysql-8.4.0-linux-glibc2.28-x86_64.tar.xz -C /usr/local/

cd /usr/local

ln -s mysql-8.4.0-linux-glibc2.28-x86_64/ mysql

chown -R root.root mysql/

# 创建环境变量
echo 'PATH=/usr/local/mysql/bin:$PATH' > /etc/profile.d/mysql.sh
. /etc/profile.d/mysql.sh

# 创建主配置文件
vim /etc/my.cnf
[mysqld]
datadir=/data/mysql
skip_name_resolve=1
socket=/data/mysql/mysql.sock
log-error=/data/mysql/mysql.log
pid-file=/data/mysql/mysql.pid

[client]
socket=/data/mysql/mysql.sock

# 初始化，本地root用户空密码
# 如果使用--initlalize选项会生成随机密码，要去/data/mysql/mysql.log中查看
mysqld --initialize-insecure --user=mysql --datadir=/data/mysql

# 加启动脚本
cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld
chkconfig --add mysqld

# 启动服务
systemctl start mysqld
```

## MySQL多实例

### MySQL多实例配置方案
```shell
# 安装mariadb-server
yum install -y mariadb-server

# 创建相关目录
mkdir -pv -/mysql/{3306,3307,3308}/{data,etc,socket,log,bin,pid}

chown -R mysql.mysql /mysql/

# 生成3个实例的初始数据
mysql_install_db --user=mysql --data=/mysql/3306/data
mysql_install_db --user=mysql --data=/mysql/3307/data
mysql_install_db --user=mysql --data=/mysql/3308/data

# 创建3个配置文件
vim /mysql/3306/etc/my.cnf
[mysqld]
port=3306
datadir=/mysql/3306/data
socket=/mysql/3306/socket/mysql.sock
log-error=/mysql/3306/log/mysql.log
pid-file=/mysql/3306/pid/mysql.pid

sed 's/3306/3307/' /mysql/3306/etc/my.cnf > /mysql/3307/etc/my.cnf
sed 's/3306/3308/' /mysql/3306/etc/my.cnf > /mysql/3308/etc/my.cnf

配置启动脚本

```

## MySQL的组成和常用工具