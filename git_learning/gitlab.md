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
#### 限制注册

![alt text](images/gitlab1.png)

#### 创建账号

首页 -> 创建群组 -> 该群组一般是项目名或部门名，主要用来分类

首页 -> 添加人员 -> 填写资料后 -> 提交

管理中心 -> 用户 -> 找到刚才添加的用户 -> 编辑 -> 添加用户密码


#### 开启导入项目的功能

管理中心 -> 通用 -> 设置 -> 导入导出 -> 勾选后点击保存