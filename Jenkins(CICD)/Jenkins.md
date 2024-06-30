# DevOps之CICD服务器Jenkins

## Jenkins部署与基本配置
官方网站
```shell
https://www.jenkins.io/zh/
```

### 系统要求

最低推荐配置：
- 256MB可用内存
- 1GB可用磁盘空间(作为一个Docker容器运行Jenkins的话推荐10GB)
```shell
apt install openjdk-11-jdk
# 验证java版本
java -version
```

为小团队推荐的硬件配置
```shell
1GB+可用内存
50GB+可用磁盘空间
```

java软件配置
- Java8-无论是Java运行时环境(JRE)还是java开发工具包(JDK)都可以
- Jenkins requires java11 OR 17 since Jenkins 2.357 and LTS 236.1

```shell
# 关闭防火墙和SELINUX
# 设置语言环境，防止后期Jenkins汉化出问题
localectl set-locale LANG=en_US.UTF-8
```

### 包安装Jenkins
```shell
apt install -y ./jenkins_2.452.2_all.deb

# 查看初始密码
[root@jenkins ~] $cat /var/lib/jenkins/secrets/initialAdminPassword
1f03170af66445d09880191e5ed8fc86
```

### Jenkins数据

#### Jenkins核心数据目录
```shell
# 所有的数据默认放在, 该目录是jenkins的核心数据目录
# 备份jenkins的方法也是把它这个拷贝下来
/var/lib/jenkins
# 插件放在
/var/lib/jenkins/plugins
```

#### 执行器
系统管理（Manage Jenkins） -> 系统配置(System) -> 执行器数量（允许多个任务同时执行，执行器数量是允许任务的数量，建议和cpu核数一致）


#### Jenkins的环境变量

系统管理(Manage Jenkins) -> 系统信息 -> 环境变量（这些环境变量，可以在执行任务的时候引用，是属于jenkins的变量）

#### Jenkins的执行权限

默认是Jenkins账号执行，但是可能后续在执行任务的时候需要root权限

- 方法1
```shell
# 修改service文件，使其以root权限执行
# 此方法可行，但是安全角度不建议
vim /lib/systemd/system/jenkins.service

User=root
Group=root
```

- 方法2：
```shell
sudo # 使用sudo给jenkins授权
```

#### 以命令行的方式执行Jenkins
```shell
java -jar jenkins-cli.jar -s http://jenkins.wang.org:8080/<命令>

# 命令参考Jenkins的web页面
```


### Jenkins优化配置

#### SSH优化
方法1
```shell
# 修改ssh客户端配置
vim /etc/ssh/ssh_config

# StrictHostKeyChecking ask， 修改为no
StrictHostKeyChecking no

# 修改完后不会验证ssh公钥信息
```

方法2

系统管理 -> 全局安全配置
注意：需要安装Git或者Gitlab插件才能配置

配置Git Host Key Verification Configuration
选择：No verification

#### 性能优化

执行器数量和CPU数量尽量一致


### Jenkins优化配置

将核心数据目录备份打包即可

### Jenkins密码忘记后恢复

- 首先停止服务
```shell
systemctl stop jenkins
```

- 备份`config.xml`文件后修改
```shell
# 备份配置文件
cp /var/lib/jenkins/config.xml /tmp -a
# 修改配置文件
vim /var/lib/jenkins/config.xml

# 删除jenkins主目录中config.xml的如下内容
<useSecurity>true</useSecurity>
<authorizationStrategy class="hudson.security.FullControlOnceLoggedInAuthorizationStrategy">
  <denyAnonymousReadAccess>true</denyAnonymousReadAccess>
</authorizationStrategy>
<securityRealm class="hudson.security.HudsonPrivateSecurityRealm">
  <disableSignup>true</disableSignup>
  <enableCaptcha>false</enableCaptcha>
</securityRealm>

# 重启jenkins
systemctl start jenkins
```

- 输入域名，可以无需输入密码，直接进入系统
```shell
jenkins.wang.org:8080
```

- 进入 系统管理 -> 全局安全配置 -> 修改安全域
  - 安全域改为`Jenkins' own user database`
  - 授权策略改为`Logged-in users can do anything`

- 进入 系统管理 -> Users(用户) -> admin -> 设置 -> 修改新密码即可



## JenKins实现CICD

前期实验准备
- Gtilab服务器：10.0.0.3
- JenKins服务器：10.0.0.150
- 测试环境服务器：10.0.0.200
- 生产环境服务器：10.0.0.201


### 创建Freestyle风格的任务Job

#### 传统流程
- 开发人员将代码提交给Gitlab
- gitlab上的项目下载到目标服务器(Jenkins自动完成)
```shell
git clone 
```