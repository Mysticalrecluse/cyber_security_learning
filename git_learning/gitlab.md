# GitLab安装
## 安装方法
gitlab服务的安装方法
```
https://docs.gitlab.com/ce/install/
```

安装方法说明
```
https://docs.gitlab.com/ce/install
```

### 包安装

#### 配置官方仓库

- 配置好域名解析
```shell
# 下载deb安装包
https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu/pool/jammy/main/g/gitlab-ce/gitlab-ce_17.1.1-ce.0_amd64.deb

# 安装
apt install -y ./gitlab-ce_17.1.1-ce.0_amd64.deb

# 更改/etc/gitlab/gitlab.rb配置文件
# 该组件是gitlab所有组件统一的配置文件
external_url 'http://feng.gitlab.org' # 更改为自定义的域名

# 修改完配置文件，执行此操作
gitlab-ctl reconfigure

# 查看gitlab服务进程，状态
gitlab-ctl statusroot@ubuntu2204:~# gitlab-ctl status
run: alertmanager: (pid 30490) 30s; run: log: (pid 30214) 103s
run: gitaly: (pid 30453) 33s; run: log: (pid 29701) 338s
run: gitlab-exporter: (pid 30463) 33s; run: log: (pid 30139) 121s
run: gitlab-kas: (pid 29920) 319s; run: log: (pid 29939) 316s
run: gitlab-workhorse: (pid 30418) 34s; run: log: (pid 30063) 138s
run: logrotate: (pid 29614) 356s; run: log: (pid 29626) 352s
run: nginx: (pid 30435) 34s; run: log: (pid 30080) 132s
run: node-exporter: (pid 30447) 33s; run: log: (pid 30127) 125s
run: postgres-exporter: (pid 30499) 29s; run: log: (pid 30236) 97s
run: postgresql: (pid 29747) 325s; run: log: (pid 29761) 323s
run: prometheus: (pid 30474) 32s; run: log: (pid 30186) 109s
run: puma: (pid 29990) 153s; run: log: (pid 29997) 152s
run: redis: (pid 29653) 349s; run: log: (pid 29663) 345s
run: redis-exporter: (pid 30466) 32s; run: log: (pid 30163) 115s
run: sidekiq: (pid 30006) 147s; run: log: (pid 30019) 144s

# 初始化后，用户名是root，密码：在/etc/gitlab/initial_root_password
```

## Gitlab用法
### 限制注册

![alt text](images/gitlab1.png)

### 创建账号

首页 -> 创建群组 -> 该群组一般是项目名或部门名，主要用来分类

首页 -> 添加人员 -> 填写资料后 -> 提交

管理中心 -> 用户 -> 找到刚才添加的用户 -> 编辑 -> 添加用户密码


### 开启导入项目的功能

管理中心 -> 通用 -> 设置 -> 导入导出 -> 勾选后点击保存

### 保护分支

默认master分支被保护，开发者角色无法对被保护的分支提交代码
也可以将其他分支进行保护，防止指定分支被破坏

进入项目 -> 设置 -> 仓库 -> 受保护分支

### 分支提交后申请合并

由管理员确认后合并

### 基于ssh免密登录

```shell
# 创建密钥对
ssh-keygen

# 然后将公钥复制到gitlab上
```

## 手动备份数据

```shell
# Gitlab 12.2之后的版本
gitlab-backup create

# Gitlab 12.1之前的版本
gitlab-rake gitlab:bakcup:create

# 默认备份路径
[root@python3 /repo/golang] $cd /var/opt/gitlab/backups/
[root@python3 /var/opt/gitlab/backups] $ls
1719724369_2024_06_30_17.1.0_gitlab_backup.tar
```

### 使用备份数据还原
```shell
# 备份前先停止两个服务
gitlab-ctl stop puma
gitlab-ctl stop sidekiq

# 然后还原
gitlab-backup restore BACKUP=1719724369_2024_06_30_17.1.0

# 重新启动
gitlab-ctl reconfigure
gitlab-ctl restart
```

### Gitlab的迁移和升级

#### 迁移流程
- 在原Gitlab主机上备份配置文件和数据
- 在目标主机上安装相同版本的gitlab软件
- 还原配置和数据
- 本质上就是数据的备份和恢复过程

#### 升级流程
- 如果新主机，需要先安装原版本，并还原配置和数据
- 不能直接跳过中间的版本直接升级，先选择最近的大版本进行升级
  - 比如：12.1向升级到13.0,要先升级到12.X最高版，然后再升级到13.0
- 下载新版本安装包，直接安装
- 安装时如果报错，根据提示修改配置
- 重新配置：`gitlab-ctl reconfigure`
- 重启服务：`gitlab-ctl restart`


### 实现Https
注意：建议使用权威CA颁发的证书，自签名的证书需要加入信任，否则会导致后续git clone等操作失败

```shell
# 创建证书
mkdir -p /etc/gitlab/ssl && cd /etc/gitlab/ssl
openssl genrsa -out gitlab.wang.org.key 2048
openssl req -days 3650 -x509 \
-sha256 -nodes -newkey rsa:2048 -subj "/C=CN/ST=beijing/L=beijing/O=wang/CN=gitlab.wang.org" -keyout gitlab.wang.org.key -out gitlab.wang.org.crt

# 修改配置文件如下内容
vim /etc/gitlab/gitlab/rb

external_url "https://gitlab.wang.org"  # 此项必须修改为https,必选项
nginx['redirect_http_to_https'] = true  # 必选项，默认值false，修改为true，实现http自动301调整至https
nginx['ssl_certificate'] = "/etc/gitlab/ssl/gitlab.wang.org.crt" # 必选项
nginx['ssl_certificate_key'] = '/etc/gitlab/ssl/gitlab.wang.org.key' # 必须项


# 重新初始化
gitlab-ctl reconfigure
gitlab-ctl restart
gitlab-ctl status
```

#### 将证书加入信任
```shell
# 在使用git客户端的主机上信任自签证书
scp gitlab-server:/etc/gitlab/ssl/gitlab.wang.org.crt

# Ubuntu证书路径
cat gitlab.wang.org.crt >> /etc/ssl/certs/ca-certificate.crt
# 红帽系统证书路径
cat gitlab.wang.org.crt >> /etc/pki/tls/certs/ca-bundle.crt
```

### 忘记gitlab密码
```shell
# 此步骤可能比较慢，需要等待以一段时间
gitlab-rails console -e production

# 输入下面指令
# 方法1：
user = User.find_by_username'root'
=> #<User id:1 @root>
irb(main):002:0> user.password="wang@123"
irb(main):003:0> user.password.confirmation="wang@123"

# 保存
irb(main):004:0> user.save
=> true

# 退出控制台
quit
```

面试对于找回密码的大体回答
```shell
进入控制台 -> 找到root用户名 -> 输两遍自定义密码即可
```









