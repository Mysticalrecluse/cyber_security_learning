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
- CICD自动化脚本
```shell
#!/bin/bash

TIME=`date +%F_%s`

HOST_LIST="
10.0.0.128
10.0.0.138"


for i in $HOST_LIST; do
        ssh root@$i mkdir /opt/wheel/wheel-$TIME
        scp -r * root@$i:/opt/wheel/wheel-$TIME/
        ssh root@$i rm -rf /var/www/html
        ssh root@$i ln -s /opt/wheel/wheel-$TIME/ /var/www/html

done;
```

进阶脚本
```shell
#!/bin/bash

HOST_LIST="
10.0.0.128
10.0.0.138
"

APP=wheel
APP_PATH=/var/www/html
DATA_PATH=/opt/wheel
DATE=`date +%F_%H-%M-%S`

deploy () {
        for i in ${HOST_LIST}; do
                ssh root@$i "rm -f ${APP_PATH} && mkdir -pv ${DATA_PATH}/$(APP)-${DATE}"
                scp -f * root@$i:${DATA_PATH}/${APP}-${DATE}
                ssh root@$i "ln -sv $(DATA_PATH)/${APP}-${DATE} ${APP_PATH}"

        done
}


rollback() {
        for i in ($HOST_LIST); do
                CURRENT_VERISION=$(ssh root@$i "readlink $APP_PATH")
                CURRENT_VERISION=$(bashname ${CURRENT_VERISION})
                echo ${CURRENT_VERISION}
                PRE_VERISION=$(ssh root@$i "ls -l ${DATA_PATH} | grep -B1 ${CURRENT_VERISION}|head -n1")
                echo $PRE_VERISION
                ssh root@$1 "rm -f ${APP_PATH} && ln -sv ${DATA_PATH}/${PRE_VERISION} ${APP_PATH}"
        done
}
```

#### 创建凭证
- 基于用户密码进行凭证创建
- 基于ssh密钥进行凭证创建
  - 将gitlab的私钥上传到jenkins的凭证上


### 创建Java项目

#### 安装maven
```shell
apt install -y maven

# 查看mvn版本
mvn -v
```

#### 加速maven
- 加速方法1：修改maven配置文件
```shell
# /etc/maven/settings.xml
# 修改这里<mirrors>
<mirrors>
   <!-- mirror
    | Specifies a repository mirror site to use instead of a given repository. The repository that
    | this mirror serves has an ID that matches the mirrorOf element of this mirror. IDs are used
    | for inheritance and direct lookup purposes, and must be unique across the set of mirrors.
    |
   <mirror>
     <id>mirrorId</id>
     <mirrorOf>repositoryId</mirrorOf>
     <name>Human Readable Name for this Mirror.</name>
     <url>http://my.repository.com/repo/path</url>
   </mirror>
    -->
</mirrors>

# </miroor>后面添加为
    <mirror>
      <id>nexus-aliyun</id>
      <mirrorOf>*</mirrorOf>
      <name>Nexus aliyun</name>
      <url>http://maven.aliyun.com/nexus/content/groups/public</url>
    </mirror>
```

- 加速方法2：在项目内直接加速
```shell
# 修改pom.xml
# pom.xml里面通常放了打包的格式，依赖关系和依赖包
# 加速代码在最下面

  <!-- 配置阿里云仓库 -->
  <repositories>
    <repository>
        <id>aliyun-repos</id>
        <url>https://maven.aliyun.com/repository/public</url>
        <releases>
            <enabled>true</enabled>
        </releases>
        <snapshots>
            <enabled>false</enabled>
        </snapshots>
    </repository>
  </repositories>
  <pluginRepositories>
     <pluginRepository>
        <id>aliyun-repos</id>
        <url>https://maven.aliyun.com/repository/public</url>
        <releases>
            <enabled>true</enabled>
        </releases>
        <snapshots>
            <enabled>false</enabled>
        </snapshots>
     </pluginRepository>
  </pluginRepositories>
```

#### maven编译java源码命令
```shell
mvn clean package -Dmaven.test.skep=true

# 使用mvn编译的java源码，中途下载的所有依赖包的默认路径是/root/.m2/repositry
# 该路径可以修改，配置文件为/etc/maven/setting.xml
  <!-- localRepository
   | The path to the local repository maven will use to store artifacts.
   |
   | Default: ${user.home}/.m2/repository
  <localRepository>/path/to/local/repo</localRepository>
  -->
```

#### 执行jar包并更改访问端口
```shell
java -jar target/spring-boot-helloworld-0.9.0-SNAPSHOT.jar --server.port=8888
```

#### 运行java程序脚本
```shell
APP_PATH=/data/spring-boot-helloworld

HOST_LIST="
10.0.0.200
10.0.0.201
"
#PORT=6666 6666为不安全端口，浏览器无法访问，只能用命令行访问
PORT=8888

mvn clean package -Dmaven.test.skip=true

for host in $HOST_LIST; do
        ssh root@$host killall -9 java &> /dev/null
        scp target/spring-boot-helloworld-*-SNAPSHOT.jar root@$host:${APP_PATH}/spring-boot-helloworld.jar
        #ssh root@$host "java -jar ${APP_PATH}/spring-boot-helloworld.jar --server.port=8888 &"
        ssh root@$host "nohup java -jar ${APP_PATH}/spring-boot-helloworld.jar --server.port=6666 &> /dev/null & "&
done
```

#### 部署War包实现CICD
```shell
# 先在待部署机器上安装tomcat
apt install -y tomcat9

# 在tomcat上，war包通常部署在/var/lib/tomcat/webapps目录下，和里面的ROOT目录同级
```

- 部署war包的脚本
```shell
#!/bin/bash

APP_PATH=/var/lib/tomcat9/webapps

HOST_LIST="
10.0.0.200
10.0.0.201
"
mvn clean package -Dmaven.test.skip=true

for host in $HOST_LIST; do
        ssh root@$host systemctl stop tomcat9
        scp target/hello-world-war-*.war root@$host:${APP_PATH}/hello.war
        ssh root@$host systemctl start tomcat9
done
```

#### 部署ruoyi系统

- 部署数据库
```shell
# 安装数据库
apt update && apt install -y mysql-server

# 将数据库端口开放，并在里面根据/RuoYi/ruoyi-admin/src/main/resources/application-druid.yaml中的数据，创建用户和数据库

create database <指定数据库>;
create user <user>@'%' identified by '123456';
grant all on <database>.* to <user>@'%';

# 将数据导入数据库
[root@python3 /repo/RuoYi] $mysql -u ry -p -h 10.0.0.3 ry < sql/quartz.sql 
[root@python3 /repo/RuoYi] $mysql -u ry -p -h 10.0.0.3 ry < sql/ry_20240112.sql 
```

- 写CICD运行脚本
```shell
#!/bin/bash

APP=ruoyi
APP_PATH=/data/ruoyi

HOST_LIST="
10.0.0.200
10.0.0.201
"
PORT=80

mvn clean package -Dmaven.test.skip=true

for host in $HOST_LIST; do
        ssh root@$host killall -9 java &> /dev/null
        scp ruoyi-admin/target/*.jar root@$host:${APP_PATH}/${APP}.jar
        ssh root@$host "nohup java -jar ${APP_PATH}/${APP}.jar --server.port=$PORT &> /dev/null & "&
done
```

- 在Jenkins上创建构建任务


### 创建Golang项目

#### 安装go编译器
```shell
apt install golang-go
```
#### 准备mysql和redis
```shell
# 安装mysql和redis
# 修改配置文件，开放端口，设置账户密码，mysql还需要配置权限
# 将git clone中的sql数据导入mysql的指定数据库中
# 设置DNS域名解析，使其与项目的配置文件中mysql和redis的host一致
```

#### Go语言项目构建脚本模板
```shell
#!/bin/bash

APP=ginweb
APP_PATH=/data
DATE=`date +%F_%H-%M-%S`
HOST_LIST="
10.0.0.200
10.0.0.201
"
build () {
        #go env 可以查看到下面变量信息，如下环境变量不支持相对路径，只支持绝对路径
        #root用户运行脚本
        #export GOCACHE="/root/.cache/go-build"
        #export GOPATH="/root/go"
        #Jenkins用户运行脚本
        export GOCACHE="/var/lib/jenkins/.cache/go-build"
        export GOPATH="/var/lib/jenkins/go"
        #go env -w GOPROXY=https://goproxy.cn,direct
        export GOPROXY="https://goproxy.cn,direct"
        (GO_ENABLED=0 go build -o ${APP})
}

deploy () {
        for host in $HOST_LIST; do
                ssh root@$host "mkdir -p $APP_PATH/${APP}-${DATE}"
                scp -r * root@$host:$APP_PATH/${APP}-${DATE}/
                ssh root@$host "killall -0 ${APP} &> /dev/null && killall -9 ${APP}; rm -f ${APP_PATH}/${APP} && \
                        ln -s ${APP_PATH}/${APP}-${DATE} ${APP_PATH}/${APP}; \
                        cd ${APP_PATH}/${APP}/ && nohup ./${APP} &> /dev/null" &
        done
}

build

deploy
```


### 集成Ansible的任务构建

#### 安装Ansible环境
```shell
apt update && apt -y install ansible

# Ubuntu22.04默认没有配置文件，可以手动创建一个空文件，使用默认值即可
mkdir -p /etc/ansible && touch /etc/ansible/ansible.cfg

# 也可以使用init命令，创建一个初始化配置文件
# 生成配置文件
ansible-config init -t all -disabled > /etc/ansible/ansible.cfg

# 在hosts配置文件中指定以root身份连接对方，并jenkis对root的ssh验证
# 默认以账户当前身份运行
vim hosts
[webservers]
10.0.0.200 ansible_ssh_user=root
10.0.0.201
```

#### 在Jenkins上安装ansible插件
- 插件名就叫`ansible`

#### 使用Ansible Playbook基于参数化实现任务测试和生产多套不同环境的部署



#### 使用Ansible Playbook实现向Playbook中传参功能

- 编写playbook文件
```yaml
- hosts: "{{ ansible_hosts }}"  # 指ansible变量，后面在Jenkins中对其赋值
  remote_user: root

  tests:
  - name: excute cmd
    shell:
      cmd: hostname -I
    register: result
  
  - name: show result
    debug:
      msg: "{{ result }}"
```

- 创建主机清单文件
```shell
cat /etc/ansible/hosts_test
[webservers]
10.0.0.104

[appservers]
10.0.0.106

cat /etc/ansible/hosts_test
[webservers]
10.0.0.105

[appservers]
10.0.0.107
```

- 创建Ansible Playbook的任务
![alt text](images\image1.png)
![alt text](images\image2.png)


## 构建后通知


### 邮件通知 

Mailer和Email Extension插件都可以实现邮件通知功能

#### 邮箱配置

- Manage Jenkins -> System -> (往下翻)系统管理员邮件地址

- 授权码位置：在上面系统管理员邮件地址下方（比较远的地方，要往下翻,接近最底下的地方）`邮件通知`
  - SMTP服务器：
  - 用户默认邮件后缀(eg：@qq.com)
  - 高级里面填写信息
    - 用户名：即发出邮箱
    - 密码：授权码
    - SMTP端口：（加密端口465，不加密25）
  - 可以发一个测试邮箱试试

#### 在构建后操作中，选择邮件通知


#### Email Extension

具体填写方式，详情见ppt


### 微信通知

具体填写方式，详情见ppt

### 钉钉通知

具体填写方式，详情见ppt

##  自动化构建
### 定时和SCM构建

#### 定时构建
Jenkins cron语法遵循Unix cron语法，但在细节上略有不同
一样是分时日月周，但是，多一个H属性
H符号可用于任何字段，且它能够在一个时间范围内对项目名称进行散列值计算出一个唯一的偏移量，以避免所有配置相同cron值的项目在同一时间启动，比如
```shell
# H可以看做一个随机值
triggers{ cron(H(0,30) * * * * )} #表示每小时的前半小时的某一分钟进行构建

# 示例2
H H(0-7) * * *  # 表示每天0-7点任意一个小时内的任意时间点执行一次

# 对比说明
H/2 * * * *：基于作业哈希值选择的起始时间，然后每 2 分钟执行一次。
*/2 * * * *：从每小时的 0 分钟开始，每 2 分钟执行一次。
```

![alt text](images\image3.png)
![alt text](images\image4.png)

#### SCM构建

![alt text](images\image5.png)

### Webhook触发构建

一共三种方法
#### 触发远程构建（无需装插件）

![alt text](images\image6.png)
根据上图需构建的weburl为
```shell
JENKINS_URL/job/freestyle-ansible/build?token=TOKEN_NAME
# JENKINS_URL可以在system中查看
TOKEN_NAME即为自定义的令牌，相当于密码

# 构造之后的webbook的url为
http://jenkins.wang.org:8080/job/freestyle-ansible/build?token=123456

# 此时构造的这个url还是有问题，因为没有用户权限，可以为这个链接专门创建一个用户
# 然后将用户的账号密码写在上面
http://jenkins:123456@jenkins.wang.org:8080/job/freestyle-ansible/build?token=123456

# 但是这种还是有问题，账号密码明文暴露了，因此基于此Jenkinsz账号生成一个令牌，使用该令牌
```
![alt text](images\image7.png)
![alt text](images\image8.png)
使用Jenkins账号，生产一个随机令牌，框中的随机值无所谓，都可以
后续可以使用这个令牌替换`123456`这个密码，最终构建的URL如下
```shell
http://jenkins:1124cb6c571b1b58c240e42be739acbe6c@feng.jenkins.org:8080/job/freestyle-wheel-demo1/build?token=123456
```

- 生成了Webhook后，配合Gitlab实现通过Gitlab的行为触发
![alt text](images\image9.png)
![alt text](images\image10.png)

tip: 此时webhook还无法在gitlab创建成功，在创建gitlab的webhook之前，还需要修改

在添加Webhook之前必须先打开外发请求
管理中心 -> 设置 -> 网络 -> 外发请求（勾选）
![alt text](images\image11.png)
所有信息写在URL框即可，，第一种方法不用写Secret令牌
![alt text](images\image12.png)

#### Gitlab Webhook URL（插件）构建
- 需要先安装Gitlab插件
![alt text](images\image13.png)
![alt text](images\image14.png)
![alt text](images\image15.png)

将生成的连接和令牌直接填写在Gitlab的Webhook上即可


#### Generic Webhook Trigger 构建

略

### 多个项目间的关联构建

#### 将一个项目关联到另一个项目之后
![alt text](images\image16.png)

#### 将一个项目关联到另一个项目之前

![alt text](images\image17.png)


### Blue Ocean



## 实现容器化Docker任务

### 可能遇到的问题1：

#### 权限问题
```shell
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock
# 运行docker是使用jenkins用户，但是在通过docker.sock进行通信时，使用docker.sock会有权限问题，
srw-rw---- 1 root docker 0 Jul  3 13:01 /var/run/docker.sock=

# 解决方案：
将jenkins用户加入docker组中
usermod -aG docker jenkins
# 改完记得重启
systemctl restart jenkins
```

#### 镜像推不上去
```shell
unauthorized: unauthorized to access repository: library/spring boot-helloworld, action:push: unauthorized to access repository: /library/spring-boot/helloworld,

# 出现原因
docker login的认证信息，之前是在root用户下，但是，自动化构建中使用的是jenkins用户
```


#### 注意实现
```shell
# 生产机器和测试机器上记得将添加harbor域名到不信任主机
```




