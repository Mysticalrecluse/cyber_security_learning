# CICD



## 私有软件仓库GitLab

![image-20250206113905921](../markdown_img/image-20250206113905921.png)



GitLab 是一个基于Ruby on Rails构建用于仓库管理系统的开源项目，使用Git作为代码管理工具，提供 了Web界面进行访问公开的或者私有的项目

GitLab 特性

- 开源免费
- 可以作为 Git 代码仓库
- 提供了方便易用的 Web 管理界面
- 支持多租户
- 功能丰富
- 支持离线提交
- 安全性高, 可以对不同的用户设置不同的权限,并且支持不同用户只能访问特定的代码,实现代码部分可见



### GitLab 架构

Gitlab 是一个由很多应用组成复杂的系统

```http
https://panlw.github.io/15365441001781.html
```

![image-20250206114524326](../markdown_img/image-20250206114524326.png)



Gitlab的服务构成

- **Nginx**：静态web服务器
- **GitLab shell**：用于处理基于ssh会话的Git命令和修改authorized keys列表
- **gitlab-workhorse**：轻量级的反向代理服务器,它旨在充当智能反向代理，以帮助整个 GitLab 加速 
- **unicorn**：An HTTP server for Rack applications, GitLab Rails应用是托管在这个服务器上面的
- **Gitaly**：Git RPC service for handing all Git calls made by GitLab
-  **Puma (GitLab Rails)**：处理发往Web接口和API的请求
- **postgresql**：数据库
- **redis**：缓存数据库
- **sidekiq**：用于在后台执行队列任务（异步执行)
- **GitLab Exporter**：GitLab指标暴露器
- **Node Exporter**：节点指标暴露器
- **GitLab self-monitoring的多个组件**：Prometheus、Alertmanager、Grafana、Sentry和Jaeger
- **Inbound emails（SMPT）**：接收用于更新issue的邮件
- **Outbound email (SMTP)**：向用户发送邮件通知
- **LDAP Authentication**：LDAP认证集成
- **MinIO**：对象存储服务
- **Registry**：容器注册表，支持Image的push和pull操作
- **Runner**：执行GitLab的CI/CD作业



**Omnibus GitLab**

由于Gitlab 组件众多,各个组件的分别管理配置过于复杂,所以官方提供了 Omnibus GitLab 项目实现方便的管理 

Omnibus GitLab是基于Chef的应用编排工具，它基于Chef的cookbooks和recipes等组件自动化编排 GitLab的各组件，避免了用户复杂的配置过程

相关项目  https://gitlab.com/gitlab-org/omnibus-gitla

Omnibus GitLab architecture and components:  https://docs.gitlab.com/omnibus/architecture/

![image-20250206115900821](../markdown_img/image-20250206115900821.png)



管理各组件使用统一命令为**gitlab-ctl**，例如`gitlab-ctl reconfigure`或`gitlab-ctl restart`等能统—执行各组 件的重新配置及重启操作

此外还有一些各组件专用的命令，如:`gitlab-backup`,`gitlab-pgsql`,`gitlab-rails`和`gitlab-rake`等

提供统一配置模板文件, 用于为GitLab中的每个组件提供配置信息

在配置模板文件中对于每个组件配置参数格式为: `['']=`



### GitLab 包安装

GitLab 有两个版本：**EE商业版**和**CE社区版**，以下使用CE版



#### 安装方法

Gitlab 服务的安装文档

```http
https://docs.gitlab.com/ce/install/
```

安装方法说明

```http
https://docs.gitlab.com/ee/install/install_methods.html
```

-  **Linux 安装包**：官方的 deb/rpm 安装包（也被称作 Omnibus GitLab）包含极狐GitLab 和依赖的 组件，包括PostgreSQL、Redis 和 Sidekiq
- **Source**：源码安装，在GitLab没有提供适用的安装包的平台上（例如各类BSD系统）只能采用这种安装方式
- **Docker**：Docker 容器化的极狐GitLab 软件包
- **GitLab Operator**：Kubernetes Operator风格的部署模式
- **Helm Chart**：用于在 Kubernetes 上安装极狐GitLab 及其所有组件的云原生 Helm chart
- **GitLab Environment Toolkit（GET）**：自动化工具集，用于在主流的公有云（Azure、GCP和 AWS）上部署GitLab 



#### 安装 GitLab 要求

Gitlab硬件和软件的环境要求：

```http
https://docs.gitlab.com/ce/install/requirements.html
```

硬件配置要求较高：

- 测试环境：内存4G以上
- 生产环境：建议CPU2C以上，内存8G以上，磁盘10G以上配置，和用户数有关

```ABAP
注意:如果内存较低,可以会导致Gitlab有些服务无法启动,建议4G以上内存
```



#### 安装前准备

##### Ubuntu 系统环境安装前准备

配置ubuntu 仓库

配置阿里云或清华大学等国内镜像仓库实现加速

```bash
[root@ubuntu1804 ~]#vim /etc/apt/sources.list
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe
multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
debhttps://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
```



##### RHEL 系统环境安装前准备

基于最小化服务器安装，建议修改配置如下：

```bash
[root@centos ~]# wget -O /etc/yum.repos.d/epel.repo 
http://mirrors.aliyun.com/repo/epel-7.repo
[root@centos ~]# systemctl disable firewalld
[root@centos ~]# sed -i '/SELINUX/s/enforcing/disabled/' /etc/sysconfig/selinux
[root@centos ~]# hostnamectl set-hostname gitlab.example.com
[root@centos ~]# reboot
```



#### GitLab 安装

gitlab 安装有多种方式,下面选择包安装方式

**官方gitlab 包下载链接**

```http
https://packages.gitlab.com/gitlab
```

![image-20250206121909398](../markdown_img/image-20250206121909398.png)

**GitLab-CE 安装包官方下载地址**

```http
https://packages.gitlab.com/gitlab/gitlab-ce
```

**yum源清华大学下载地址：**

```http
https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/
```

范例：Ubuntu2204下载并安装 GitLab

```bash
# 在官方下载最新版本
[root@ubuntu2204 ~]#wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/ubuntu/jammy/gitlab-ce_17.6.4-ce.0_amd64.deb/download.deb

# Ubuntu 国内镜像下载 
[root@ubuntu2004 ~]#wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu/pool/jammy/main/g/gitlab-ce/gitlab-ce_17.8.1-ce.0_amd64.deb

# 安装
[root@ubuntu2204 ~]#apt install -y ./gitlab-ce_17.6.4-ce.0_amd64.deb
```

![image-20250206125844241](../markdown_img/image-20250206125844241.png)



#### 修改 GitLab 配置

##### gitlab相关的目录

```bash
/etc/gitlab         #配置文件目录，重要
/var/opt/gitlab     #数据目录,源代码就存放在此目录,重要
/var/log/gitlab     #日志目录 
/run/gitlab         #运行目录,存放很多的数据库文件
/opt/gitlab         #安装目录
```

##### gitlab 初始化配置

```bash
# 指定域名【必选】
[root@ubuntu1804 ~]#vim /etc/gitlab/gitlab.rb
[root@ubuntu1804 ~]#grep "^[a-Z]" /etc/gitlab/gitlab.rb
external_url 'http://gitlab.mystical.org'   

# 邮件通知设置【可选】
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.163.com"
gitlab_rails['smtp_port'] = 465
gitlab_rails['smtp_user_name'] = "15104600741@163.com"
gitlab_rails['smtp_password'] = "授权码"
gitlab_rails['smtp_domain'] = "163.com"
gitlab_rails['smtp_authentication'] = "login"
#gitlab_rails['smtp_enable_starttls_auto'] = true       # 二选一：该选项端口587
gitlab_rails['smtp_tls'] = true                         # 二选一：该选项端口465
gitlab_rails['smtp_pool'] = false

###! **Can be: 'none', 'peer', 'client_once', 'fail_if_no_peer_cert'**
###! Docs: http://api.rubyonrails.org/classes/ActionMailer/Base.html
gitlab_rails['smtp_openssl_verify_mode'] = 'none'
user['git_user_email'] = "15104600741@163.com"

# 修改nginx监听的端口【可选】
nginx['listen_port']=8080

# ssh协议端口，地址【可选】
gitlab_sshd['listen_address'] = '0.0.0.0:2222'
# 示例：ssh://git@gitlab.wang.org:2222/example/app.git

# 给root用户指定初始密码【必选】
#注意:密码至少8位并且复杂度要求才是有效密码
gitlab_ralis['initial_root_password'] = "zyf@123456"

# gitlab优化
# 关闭可能暂时不使用的功能，比如监控(测试环境下)
prometheus['enable'] = false
prometheus['monitor_kubernetes']=false
alertmanager['enable']=false
node_exporter['enable']=false
redis_exporter['enable']=false
postgres_exporter['enable']=false
gitlab_exporter['enable']= false
prometheus_monitoring['enable']=false
grafana['enable']=false

# 名称解析
[root@mystical ~]# vim /etc/hosts
```



#### 初始化和启动服务

执行配置reconfigure并启动服务：

```bash
#每次修改完配置文件都需要执行此操作
[root@ubuntu1804 ~]# gitlab-ctl reconfigure
```



#### 验证Gitlab启动完成

```bash
[root@mystical ~]# gitlab-ctl status
run: gitaly: (pid 15033) 17s; run: log: (pid 14586) 144s
run: gitlab-kas: (pid 14803) 130s; run: log: (pid 14814) 127s
run: gitlab-workhorse: (pid 15011) 19s; run: log: (pid 14946) 49s
run: logrotate: (pid 14502) 159s; run: log: (pid 14511) 156s
run: nginx: (pid 15025) 18s; run: log: (pid 14966) 44s
run: postgresql: (pid 14633) 136s; run: log: (pid 14644) 135s
run: puma: (pid 14866) 63s; run: log: (pid 14873) 62s
run: redis: (pid 14538) 153s; run: log: (pid 14548) 150s
run: sidekiq: (pid 14887) 57s; run: log: (pid 14904) 55s
```



#### Gitlab的常用命令

GitLab除了使用Web界面进行管理，还提供了各组件的统一命令为gitlab-ctl，此外还有一些各组件专用的命令，如gitlab-pgsql、 gitlab-rails和gitlab-rake等

```bash
#客户端命令行操作行
gitlab-ctl  
gitlab-ctl check-config #检查配置
gitlab-ctl show-config  #查看配置
gitlab-ctl reconfigure  #修改过配置后需要执行重新配置
gitlab-ctl stop         #停止gitlab
gitlab-ctl start        #启动gitlab
gitlab-ctl restart      #重启gitlab
gitlab-ctl status       #查看组件运行状态
gitlab-ctl tail         #查看所有日志
gitlab-ctl tail nginx   #查看某个组件的日志
gitlab-ctl service-list #列出服务

#其它命令
gitlab-rails #用于启动控制台进行特殊操作，如修改管理员密码、打开数据库控制台( gitlab-rails dbconsole)等
gitlab-psql #数据库命令行
gitlab-rake #数据备份恢复等数据操作
```

示例: 查看服务列表

```bash
[root@mystical ~]# gitlab-ctl service-list
gitaly*
gitlab-kas*
gitlab-workhorse*
logrotate*
nginx*
postgresql*
puma*
redis*
sidekiq*
```



#### 在浏览器访问GitLab

在新版gitlab中第一次登录的界面发生变化,取消重设密码界面,需要直接输入用户和密码才能登录

**默认用户为root，其密码是随机生成**

![image-20250208154751291](../markdown_img/image-20250208154751291.png)

```bash
# 初始账号为root
# 初始密码为配置文件自行指定的密码
```

![image-20250208155656668](../markdown_img/image-20250208155656668.png)





### 基于 Kubernetes 安装 GitLab

```http
https://docs.gitlab.com/operator/installation.html
```

注意：资源建议

```ABAP
master: 4核CPU + 4G内存
node1: 4核CPU + 6G内存
node1: 4核CPU + 6G内存
node1: 4核CPU + 6G内存

低于上述配置，可能会因为资源不足，导致服务异常
```

范例：注意相关镜像可能需要科学上网

```bash
# 提前安装cert-manager证书管理组件
# 官方cert-manager.yaml文件路径：https://github.com/cert-manager/cert-manager/releases/
# 根据需要，自行选定版本的cert-manager.yaml
# 示例以v1.17.0为例，此为20250208最新版 
[root@master1 ~]# wget https://www.mysticalrecluse.com/script/tools/cert-manager.yaml
[root@master1 ~]# kubectl apply -f cert-manager.yaml 

# 部署 GitLab Operator
# GL_OPERATOR_VERSION=1.9.1 
# PLATFORM=kubernetes
# 为gitlab创建名称空间
[root@master1 ~]# kubectl create namespace gitlab-system

# 创建动态置备的sc，并将其设置为default，这一步必须做，否则gitlab无法自动创建pv
# 创建sc，看Kubernetes数据存储相关教学，创建完sc后，使用下面指令，将其设置为默认
[root@master1 ~]# kubectl patch storageclass sc-nfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

# 设置完后查看sc状态
[root@master1 test]#kubectl get sc
NAME               PROVISIONER                                   RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
sc-nfs (default)   k8s-sigs.io/nfs-subdir-external-provisioner   Delete          Immediate           false                  27d


# gitlab operator的各版本yaml文件下载路径：
# https://gitlab.com/gitlab-org/cloud-native/gitlab-operator/-/releases
[root@master1 ~]# wget https://gitlab.com/api/v4/projects/18899486/packages/generic/gitlab-operator/1.9.1/gitlab-operator-kubernetes-1.9.1.yaml

# 启用operator
[root@master1 ~]# kubectl apply -f gitlab-operator-kubernetes-1.9.1.yaml

# 创建GitLab用户资源
[root@master1 ~]# cat mygitlab.yaml 
apiVersion: apps.gitlab.com/v1beta1
kind: GitLab
metadata:
  name: gitlab
spec:
  chart:
    # 使用下面链接查看version
    # https://gitlab.com/gitlab-org/cloud-native/gitlab-operator/-/blob/1.9.1/CHART_VERSIONS
    version: "8.8.1" 
    values:
      global:
        hosts:
          domain: "mygitlab.mystical.org"  # use a real domain here
        ingress:
          configureCertmanager: true
      certmanager-issuer:
        email: mysticalrecluse@gmail.com   # use your real email address here
        
# 启用gitlab
[root@master1 ~]# kubectl apply -f mygitlab.yaml -n gitlab-system

# 如果启动成功，查看状态如下
[root@master1 ~]#kubectl get gitlabs -n gitlab-system 
NAME     STATUS    VERSION
gitlab   Running   8.8.1

#  访问gitlab.mygitlab.mystical.org
```

```ABAP
注意：由于资源问题，服务可能因为就绪探针和生存探针，导致起不来，反复重启，建议将webservice和sidekiq的deployment的探针取消
注意：在取消探针前，记得将operator的controller-manager停掉，即将副本数量设为0即可
```



![image-20250208125113586](../markdown_img/image-20250208125113586.png)

```bash
# 默认账号：root
# 初始密码：执行下列指令
[root@master1 ~]# kubectl get secret -n gitlab-system gitlab-gitlab-initial-root-password -o jsonpath="{.data.password}" | base64 --decode
mKycBGLxob511Rq2VopJ51URSWdphI7qVHass9t74LoZiglxdmMKSgrCUPkIAFS2	
```

![image-20250208125336856](../markdown_img/image-20250208125336856.png)

```bash
# 查看所有的ingress
[root@master1 ~]#kubectl get ingress -n gitlab-system 
NAME                        CLASS          HOSTS                            ADDRESS     PORTS     AGE
gitlab-kas                  gitlab-nginx   kas.mygitlab.mystical.org        10.0.0.10   80, 443   3h9m
gitlab-minio                gitlab-nginx   minio.mygitlab.mystical.org      10.0.0.10   80, 443   3h26m
gitlab-registry             gitlab-nginx   registry.mygitlab.mystical.org   10.0.0.10   80, 443   3h9m
gitlab-webservice-default   gitlab-nginx   gitlab.mygitlab.mystical.org     10.0.0.10   80, 443   3h9m

# 尝试访问 minio.mygitlab.mystical.org
```

![image-20250208125839659](../markdown_img/image-20250208125839659.png)

```bash
# 查看minio的accesskey和secretkey
[root@master1 ~]#kubectl get secret -n gitlab-system gitlab-minio-secret -o yaml
apiVersion: v1
data:
  accesskey: RnJuZkYxd3hRUGN5WWtYdmt1NW1nWkg1VzNJQlhqTWk2ZGZzSzcyaUExYlF1V1I0Z044TTlZYXRFV3B2NUlacg==
  secretkey: T3hUZ1RJbk01UkttSWtLdzJsN25ZRjdaVjlXc3JEYVJaR1F4Y3F4UU5lMlFzWmZmY3J3eTF2N1IySHFSa2hYdw==
kind: Secret
metadata:
  creationTimestamp: "2025-02-08T01:29:09Z"
  labels:
    app: gitlab
    app.kubernetes.io/managed-by: gitlab-operator
    app.kubernetes.io/name: gitlab
    app.kubernetes.io/part-of: gitlab
    chart: gitlab-8.8.1
    heritage: Helm
    release: gitlab
  name: gitlab-minio-secret
  namespace: gitlab-system
  resourceVersion: "174778"
  uid: 9113c545-8eb0-40f3-af90-69817bf61837
type: Opaque

# base64解码
[root@master1 ~]#echo "RnJuZkYxd3hRUGN5WWtYdmt1NW1nWkg1VzNJQlhqTWk2ZGZzSzcyaUExYlF1V1I0Z044TTlZYXRFV3B2NUlacg=="|base64 -d
FrnfF1wxQPcyYkXvku5mgZH5W3IBXjMi6dfsK72iA1bQuWR4gN8M9YatEWpv5IZr
[root@master1 ~]#echo "T3hUZ1RJbk01UkttSWtLdzJsN25ZRjdaVjlXc3JEYVJaR1F4Y3F4UU5lMlFzWmZmY3J3eTF2N1IySHFSa2hYdw=="|base64 -d
OxTgTInM5RKmIkKw2l7nYF7ZV9WsrDaRZGQxcqxQNe2QsZffcrwy1v7R2HqRkhXw

# 使用解码后的key登录
```

![image-20250208130235955](../markdown_img/image-20250208130235955.png)



**在Kubernetes部署好GitLab后，查看资源情况**

![image-20250208133202056](../markdown_img/image-20250208133202056.png)



#### 配置邮件通知

**检查 `gitlab-rails-secret` 是否包含 SMTP 配置**

```bash
[root@master1 ~]# kubectl get secret gitlab-rails-secret -n gitlab-system -o yaml

# 如果 data: 下包含 smtp_address，说明 GitLab 已配置 SMTP
# 如果没有 smtp_address，则 GitLab 没有 SMTP 配置，需要手动添加
```



**在 `gitlab.yaml` 永久修改 `smtp_settings`**

**手动获取 `gitlab.yaml`**

```bash
[root@master1 ~]# kubectl get gitlab -n gitlab-system -o yaml > gitlab-latest.yaml
[root@master1 test]# cat gitlab-latest.yaml 
apiVersion: v1
items:
- apiVersion: apps.gitlab.com/v1beta1
  kind: GitLab
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"apps.gitlab.com/v1beta1","kind":"GitLab","metadata":{"annotations":{},"creationTimestamp":"2025-02-08T01:28:45Z","generation":2,"name":"gitlab","namespace":"gitlab-system","resourceVersion":"243958","uid":"ac00fa8b-c9ee-4df0-a666-3263366e5025"},"spec":{"chart":{"values":{"certmanager-issuer":{"email":"mysticalrecluse@gmail.com"},"global":{"hosts":{"domain":"mygitlab.mystical.org"},"ingress":{"configureCertmanager":true},"smtp":{"address":"smtp.163.com","authentication":"login","domain":"163.com","enabled":true,"openssl_verify_mode":"peer","password":{"key":"SMTP_PASSWORD","secret":"gitlab-smtp-secret"},"port":465,"starttls_auto":false,"tls":true,"user_name":"15104600741@163.com"}}},"version":"8.8.1"}},"status":{"conditions":[{"lastTransitionTime":"2025-02-08T07:07:10Z","message":"GitLab is initialized","observedGeneration":2,"reason":"Initialized","status":"True","type":"Initialized"},{"lastTransitionTime":"2025-02-08T07:07:10Z","message":"GitLab is running and available to accept requests","observedGeneration":2,"reason":"Available","status":"True","type":"Available"},{"lastTransitionTime":"2025-02-08T01:46:37Z","message":"GitLab is not currently upgrading","observedGeneration":2,"reason":"Upgrading","status":"False","type":"Upgrading"}],"phase":"Running","version":"8.8.1"}}
    creationTimestamp: "2025-02-08T07:13:15Z"
    generation: 1
    name: gitlab
    namespace: gitlab-system
    resourceVersion: "247693"
    uid: 1624d7c1-3786-47d8-beb7-1ccc1479e2de
  spec:
    chart:
      values:
        certmanager-issuer:
          email: mysticalrecluse@gmail.com
        global:
          hosts:
            domain: mygitlab.mystical.org
          ingress:
            configureCertmanager: true
          smtp:                                    # 从这里开始添加
            address: smtp.163.com
            authentication: login
            domain: 163.com
            enabled: true
            openssl_verify_mode: peer
            password:
              key: SMTP_PASSWORD
              secret: gitlab-smtp-secret
            port: 465
            starttls_auto: false
            tls: true
            user_name: 15104600741@163.com
          email:
            from: "15104600741@163.com"
            reply_to: "15104600741@163.com"      # 添加到这里
      version: 8.8.1
  status:
    conditions:
    - lastTransitionTime: "2025-02-08T07:18:57Z"
      message: GitLab is initialized
      observedGeneration: 1
      reason: Initialized
      status: "True"
      type: Initialized
    - lastTransitionTime: "2025-02-08T07:18:57Z"
      message: GitLab is running and available to accept requests
      observedGeneration: 1
      reason: Available
      status: "True"
      type: Available
    - lastTransitionTime: "2025-02-08T07:14:56Z"
      message: GitLab is not currently upgrading
      observedGeneration: 1
      reason: Upgrading
      status: "False"
      type: Upgrading
    phase: Running
    version: 8.8.1
kind: List
metadata:
  resourceVersion: ""

# 关键
# email.from 为 user_name 相同的邮箱
# reply_to 避免 Reply-To 触发 SMTP 检查
```



**创建secret存放邮箱授权码**

```bash
[root@master1 ~]# kubectl create secret generic gitlab-smtp-secret -n gitlab-system   --from-literal=SMTP_PASSWORD="<授权码>"
```



**应用新配置**

```bash
[root@master1 ~]# kubectl apply -f gitlab-latest.yaml
[root@master1 ~]# kubectl rollout restart deployment gitlab-webservice-default -n gitlab-system
```



<span style="color:tomato;font-weight:700">注意：由于某些原因，我将gitlab-controller-manager关闭了，手动接管整个服务，所以，上述所有的操作前提是gitlab-controller-manager是正常运行的，如果和我一样将其关闭，需执行下列操作，手动将smtp服务注入到configmap中</span>

```ABAP
# 手动修改 ConfigMap 来注入 smtp 配置

kubectl patch configmap -n gitlab-system gitlab-webservice-config --type='merge' -p \
'{"data":{"smtp.yml": "production:\n  enabled: true\n  address: \"smtp.163.com\"\n  port: 465\n  user_name: \"15104600741@163.com\"\n  password: \"你的SMTP密码\"\n  domain: \"163.com\"\n  authentication: \"login\"\n  tls: true\n  starttls_auto: false\n  openssl_verify_mode: \"peer\""}}'

# 让 ConfigMap 生效
kubectl rollout restart deployment -n gitlab-system gitlab-webservice
kubectl rollout restart deployment -n gitlab-system gitlab-sidekiq
kubectl rollout restart deployment -n gitlab-system gitlab-toolbox

# 测试是否生效
kubectl exec -it -n gitlab-system deployment/gitlab-toolbox -- gitlab-rails runner "Notify.test_email('3140394153@qq.com', 'Test Email', 'GitLab SMTP Config Test').deliver_now"

# 如果尤其开启operator的controller-manager会将上述配置覆盖掉，因此，上述方式仅适用于实验环境，在资源有限，正常gitlab无法再k8s上启动的情况下使用。
```



**测试邮件**

```bash
[root@master1 test]#kubectl exec -it -n gitlab-system deployment/gitlab-toolbox -- gitlab-rails runner "Notify.test_email('3140394153@qq.com', 'Test Email', 'GitLab SMTP Config Test').deliver_now"
Defaulted container "toolbox" out of: toolbox, certificates (init), configure (init)
WARNING: Active Record does not support composite primary key.

security_findings has composite primary key. Composite primary key is ignored.

# 成功
```

![image-20250208153458322](../markdown_img/image-20250208153458322.png)



### GitLab 基本配置

#### 首次登录 GitLab Web 界面修改密码

新版gitlab密码初始化官方帮助链接

```http
https://docs.gitlab.com/omnibus/installation/index.html
```

新版登录后,也需再次修改密码,注意:密码至少8位

![image-20250208155944241](../markdown_img/image-20250208155944241.png)

![image-20250208160007293](../markdown_img/image-20250208160007293.png)

![image-20250208160119946](../markdown_img/image-20250208160119946.png)





####  修改头像

登录gitlab后可能看到用户的头像不能正常显示,可以修改为自定义的头像

Kubernetes部署的GitLab有默认头像，可以正常显示

![image-20250208160335921](../markdown_img/image-20250208160335921.png)

![image-20250208160403884](../markdown_img/image-20250208160403884.png)

![image-20250208160416028](../markdown_img/image-20250208160416028.png)



#### 关闭账号注册功能

新版用户注册界面

![image-20250208160730934](../markdown_img/image-20250208160730934.png)

关闭注册功能,先用root用户登录

![image-20250208161042568](../markdown_img/image-20250208161042568.png)

![image-20250208161114717](../markdown_img/image-20250208161114717.png)

![image-20250208161128553](../markdown_img/image-20250208161128553.png)

在另一个浏览器登录

![image-20250208161240635](../markdown_img/image-20250208161240635.png)



#### 修改邮箱地址

![image-20250208161910920](../markdown_img/image-20250208161910920.png)

![image-20250208161934583](../markdown_img/image-20250208161934583.png)

此时指定邮箱会收到一封确认邮件

![image-20250208162052996](../markdown_img/image-20250208162052996.png)

![image-20250208162510672](../markdown_img/image-20250208162510672.png)



**修改个人资料的邮件地址**

![image-20250208162634481](../markdown_img/image-20250208162634481.png)

![image-20250208162749521](../markdown_img/image-20250208162749521.png)

![image-20250208162805076](../markdown_img/image-20250208162805076.png)

删除旧的邮箱

![image-20250208163033871](../markdown_img/image-20250208163033871.png)





### GitLab 用户和组管理

#### 用户管理

##### 创建用户

创建gitlab用户账户并登录

![image-20250208163328517](../markdown_img/image-20250208163328517.png)

![image-20250208163440555](../markdown_img/image-20250208163440555.png)

输入新的用户信息

![image-20250208172632118](../markdown_img/image-20250208172632118.png)

![image-20250208172650092](../markdown_img/image-20250208172650092.png)

为新建的用户设置密码

![image-20250208172749159](../markdown_img/image-20250208172749159.png)

![image-20250208172837815](../markdown_img/image-20250208172837815.png)

另找一个浏览器，以新建用户登录gitlab

![image-20250208172947464](../markdown_img/image-20250208172947464.png)

会提示更改密码，更改后重新登录

![image-20250208173100975](../markdown_img/image-20250208173100975.png)

![image-20250208173115793](../markdown_img/image-20250208173115793.png)

创建成功后，会给新账户的邮箱发送提示信息

![image-20250208173333212](../markdown_img/image-20250208173333212.png)



#### 更改语言

![image-20250208173512645](../markdown_img/image-20250208173512645.png)

![image-20250208173544945](../markdown_img/image-20250208173544945.png)

![image-20250208173644083](../markdown_img/image-20250208173644083.png)



#### 创建组

使用管理员root 或用户都可以创建group组

一个group组里面可以拥有多个project项目分支，可以将开发的用户添加到组里，再进行设置权限

如果gitlab使用者的组织规模较大,每一个group组可以分别对应一个组织,如:某个分公司或部门

如果gitlab使用者的组织规模较小, 每一个group组也可以对应一个项目或业务,即每一个不同的group组 对应同一个组织内部的不同的项目

不同的组中添加不同的开发人员帐号，即可实现对开发者实现权限的管理。

![image-20250208174433922](../markdown_img/image-20250208174433922.png)

![image-20250208174505641](../markdown_img/image-20250208174505641.png)

![image-20250208174702480](../markdown_img/image-20250208174702480.png)

- Private：只有加入组的用户能够访问
- Internal：只有注册到GItLab的用户能够访问
- Public：所有人都能访问

![image-20250208174820378](../markdown_img/image-20250208174820378.png)





### GitLab 项目管理

#### 创建新项目

项目project属于一个group组,即一般project对应一个项目中的功能模块或服务

注意: 此处在新建项目时先不进行初始化

![image-20250208175340783](../markdown_img/image-20250208175340783.png)

![image-20250208175905085](../markdown_img/image-20250208175905085.png)

注意: 此处在新建项目时先不进行初始化

![image-20250208180050971](../markdown_img/image-20250208180050971.png)

![image-20250211214500681](../markdown_img/image-20250211214500681.png)

命令行指引

您还可以按照以下说明从计算机中上传现有文件

##### Git 全局设置

```bash
# 在一台网络连通的虚拟机做客户端
# 如果客户端没有将ssh公钥上传到gitlab,则直接拉取仓库会报错
[root@master2 ~/project]$ git clone git@gitlab.mygitlab.mystical.org:devops/m62-hw.git
Cloning into 'm62-hw'...
The authenticity of host 'gitlab.mygitlab.mystical.org (172.22.200.11)' can't be established.
ED25519 key fingerprint is SHA256:aQ+Q4ELkyFWnqh88hcFvHIOKi4wUqsZqlyYCUhZ4kBI.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'gitlab.mygitlab.mystical.org' (ED25519) to the list of known hosts.
git@gitlab.mygitlab.mystical.org: Permission denied (publickey,keyboard-interactive).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

# 在客户端创建ssh
[root@master2 ~]$ ssh-keygen 
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Created directory '/root/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa
Your public key has been saved in /root/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:Ji2Lu3jg32JOYaxx1qbswtyYceLwYpeHXCwTt9MvGe4 root@master2.mystical.org
The key's randomart image is:
+---[RSA 3072]----+
|                 |
|                 |
|                 |
|   o o .         |
|  . X B S        |
|. +X.X B         |
| BoO@ + +        |
|..XO=+ + .       |
|..o*BooE.        |
+----[SHA256]-----+

# 输出公钥
[root@master2 ~]$ cat .ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDXFnbc/E3Hqp/slmeUIVUgkK/gyxFA0Gv5+bVa4h7qHPcYBmuR+ycza7y9Gu9KTqAWVI/1x5ihFODYmU7HxFu/L6FEbWSRidnwTChGZgfdVMR315zUmgSVahvi1QldRVZkvGe2t4p+xjkYtH78nKrd8ptkk/+FbYCTZjSN+0ThcVfSuPaY8U5xcLbPjMSYCqLuoTh3fvx/jAXDWASgohCmnmVyypdl/SHV2Wwo7bKKm17TYlviBmiZsXstAVP0kFd9t4lbAge2zGQF6rGpNTsSBORPg9JYK0J8TwKhx/3AxJUjBb5kz/IE7y72T30iyOO/J2Psy9l60eCH54xXHSDPBkZZIvR4YX6e97JE4SCglEtj7VitfWdTNV9qAL/BhbpQi5K9i34b6JjXnsbTTgiBPe+BxbjH3F29sbb0ViGNcTh/TITYshQdCy/i45SYjIF6Vs43EtEOO7DOLD1Vho74M7cvE+/o42oOmmkttqdZ19bu92ALeyEUeJQl+g6kEC0= root@master2.mystical.org

# 公钥贴在gitlab上，如下图
```

![image-20250212114256453](../markdown_img/image-20250212114256453.png)

![image-20250212114318304](../markdown_img/image-20250212114318304.png)

![image-20250212114345172](../markdown_img/image-20250212114345172.png)

![image-20250212114429246](../markdown_img/image-20250212114429246.png)

上传成功后，再在客户端clone仓库

```bash
# 成功将仓库clone了下来
[root@master2 ~/project]# git clone git@gitlab.mygitlab.mystical.org:devops/m62-hw.git
Cloning into 'm62-hw'...
warning: You appear to have cloned an empty repository.

# 查看
[root@master2 ~/project]# ls
m62-hw

# 配置这个项目的本地git身份
[root@master2 ~/project]# cd m62-hw
[root@master2 ~/project/m62-hw]# git config --local user.name Zhangyifeng
[root@master2 ~/project/m62-hw]# git config --local user.email "15104600741@163.com"

# 查看
[root@master2 ~/project/m62-hw]# git config --local --list
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=git@gitlab.mygitlab.mystical.org:devops/m62-hw.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
user.name=Zhangyifeng
user.email=15104600741@163.com

# 这里因为上述创建仓库，取消了仓库初始化，所以这里必须手动创建一个主分支
# clone的是未初始化的仓库的标志：warning: You appear to have cloned an empty repository

# 创建主分支
[root@master2 ~/project/m62-hw]# git switch --create main
Switched to a new branch 'main'

# 生成一个空文件，进行一次提交，将其推送到远程仓库
[root@master2 ~/project/m62-hw]# touch README.md
[root@master2 ~/project/m62-hw]# git add README.md 
[root@master2 ~/project/m62-hw]# git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   README.md

[root@master2 ~/project/m62-hw]# git commit -m'add README'
[main (root-commit) 06af66e] add README
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
 
# 方法1：这里提交文件到远程仓库
[root@master2 ~/project/m62-hw]# git push origin main 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 216 bytes | 216.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To gitlab.mygitlab.mystical.org:devops/m62-hw.git
 * [new branch]      main -> main

# 方法2：
# 在 git push --set-upstream origin main 中，--set-upstream（简写为 -u）的作用是 将本地分支与远程分支关联，这样以后可以直接使用 git push 和 git pull，而不必每次都指定远程仓库和分支名称。

[root@master2 ~/project/m62-hw]# git push --set-upstream origin main

# 后续再推送，和拉取可以直接使用git push 和 git pull, 否则每次要指定上传的仓库和分支，例如：git push origin main

# 刷新浏览器上的仓库，即可看到上传的文件
```

![image-20250212120213189](../markdown_img/image-20250212120213189.png)



#### 导入项目

新版需要开启导入旧项目到Gitlab功能才支持导入

![image-20250212120859168](../markdown_img/image-20250212120859168.png)

![image-20250212120912148](../markdown_img/image-20250212120912148.png)

![image-20250212134808015](../markdown_img/image-20250212134808015.png)

**向下拉，选择settings ---> General**

![image-20250212134859628](../markdown_img/image-20250212134859628.png)

![image-20250212134939323](../markdown_img/image-20250212134939323.png)

![image-20250212135031102](../markdown_img/image-20250212135031102.png)



**导入功能开启后，开始导入项目**

![image-20250212135140410](../markdown_img/image-20250212135140410.png)![image-20250212135156796](../markdown_img/image-20250212135156796.png)

![image-20250212135522664](../markdown_img/image-20250212135522664.png)

**等待一小会儿，导入成功后**

![image-20250212135704796](../markdown_img/image-20250212135704796.png)



#### 将用户添加到组或项目并指定角色

将用户添加到组或项目中,并指定不同的角色,可以获取不同的权限



**Gitlab用户在组里面有5种不同权限:**

- **Guest**: 可以创建issue、发表评论，不能读写版本库
- **Reporter:** 可以克隆代码，不能提交，QA、PM可以赋予这个权限
- **Developer**: 可以克隆代码、开发、提交、 push(非保护分支Protected branches)，普通开发可以 赋予这个权限
- **Maintainer**: 可以创建项目、添加tag、保护分支、添加项目成员、编辑项目，核心开发人员可以赋 予这个权限
- **Owner**: 可以设置项目访问权限Visibility Level、删除项目、迁移项目、管理组成员，开发组组长可 以赋予这个权限



##### 在组中添加用户并指定角色

**进入群组**

![image-20250212140719073](../markdown_img/image-20250212140719073.png)

![image-20250212140836588](../markdown_img/image-20250212140836588.png)

**邀请成员加入组中**

![image-20250212140935887](../markdown_img/image-20250212140935887.png)

![image-20250212141015706](../markdown_img/image-20250212141015706.png)

![image-20250212143102248](../markdown_img/image-20250212143102248.png)



#### 保护分支

默认 **master/main** 分支被保护,开发者角色无法对被保护的分支提交代码

也可以将其它分支进行保护,防止指定分支被破环

**进入你的 GitLab 项目**

![image-20250212153000705](../markdown_img/image-20250212153000705.png)

**进入 Repository 保护分支设置**

![image-20250212153031716](../markdown_img/image-20250212153031716.png)

![image-20250212153054048](../markdown_img/image-20250212153054048.png)



#### 合并分支

由于普通开发者无法直接提交代码至master分支，可以先创建其它分支如dev,再提交代码到dev分支，接下来申请将dev 分支合并至master分支。管理者收到请求,经过审核没有问题进行批准合并，最终实现 master 代码的更新。



当开发人员将代码在分支更新提交后，可以向管理员提交合并申请

```bash
# 模拟开发人员创建了一条分支，并提交代码
# 这里假设管理员创建的分支，当然开发人员在非特殊情况下，也有创建的分支的权限
[root@mystical ~/Zhangyifeng/devops/meta]# git checkout Zhangyifeng
[root@mystical ~/Zhangyifeng/devops/meta]# mkdir Zhangyifeng
[root@mystical ~/Zhangyifeng/devops/meta]# cd Zhangyifeng/
[root@mystical ~/Zhangyifeng/devops/meta/Zhangyifeng]# vim hello.sh

# 提交
[root@mystical ~/Zhangyifeng/devops/meta] $git add .
[root@mystical ~/Zhangyifeng/devops/meta] $git commit -m'add Zhangyifeng/hello'
[root@mystical ~/Zhangyifeng/devops/meta] $git push origin Zhangyifeng
```

![image-20250212154732613](../markdown_img/image-20250212154732613.png)

**点击合并申请**

![image-20250212154856668](../markdown_img/image-20250212154856668.png)

**发送成功后**

![image-20250212154923324](../markdown_img/image-20250212154923324.png)

**此时管理员的账号内，会出现合并请求**

![image-20250212155031130](../markdown_img/image-20250212155031130.png)

![image-20250212155105742](../markdown_img/image-20250212155105742.png)

**点击查看**

![image-20250212155146105](../markdown_img/image-20250212155146105.png)

**点击批准，即同意此次合并**

![image-20250212155249007](../markdown_img/image-20250212155249007.png)

**点击合并**

![image-20250212155458961](../markdown_img/image-20250212155458961.png)

**查看该项目，可以发现，代码已成功合并过来**

![image-20250212155611241](../markdown_img/image-20250212155611241.png)





### GitLab 的数据备份和恢复

数据备份和恢复官方帮助：

```http
https://docs.gitlab.com/ee/raketasks/backup_restore.html
```



#### 备份相关配置文件

```bash
/etc/gitlab/gitlab.rb
/etc/gitlab/gitlab-secrets.json #双因子验证等使用此文件
```



**备份配置文件命令**

```bash
gitlab-ctl backup-etc --backup-path <DIRECTORY>
#如果不指定--backup-path <DIRECTORY>，则默认备份至/etc/gitlab/config_backup/
```



#### 手动备份数据

不同版本的备份数据命令

```bash
# GitLab 12.2之后版本
gitlab-backup create

# GitLab 12.1之前版本
gitlab-rake gitlab:backup:create
```

备份相关配置

```bash
#默认在/etc/gitlab/gitlab.rb文件中指定备份路径，如果目录空间不足，可以修改新的目录
#注意：修改完配置需要执行gitlab-ctl reconfigure
# gitlab_rails['backup_path'] = "/var/opt/gitlab/backups"

#备份的文件权限，所有者和所属组为git
# gitlab_rails['backup_archive_permissions'] = 0644

#默认备份过期时长为7天，单位为s, 之后会被自动删除
# gitlab_rails['backup_keep_time'] = 604800
```



#### 执行恢复

恢复的前提条件

```ABAP
备份和恢复使用的版本要一致
还原相关配置文件后，执行gitlab-ctl reconfigure 
确保gitlab正在运行状态
```

新版恢复方法

```bash
#恢复前先停止两个服务
[root@ubuntu1804 ~]#gitlab-ctl stop puma
[root@ubuntu1804 ~]#gitlab-ctl stop sidekiq

#恢复时指定备份文件的时间部分，不需要指定文件的全名
[root@ubuntu1804 ~]#gitlab-backup restore BACKUP=备份文件名的时间部分_Gitlab版本

#示例
[root@ubuntu1804 ~]#gitlab-backup restore BACKUP=1583562898_2020_03_07_11.11.8
#Next, restore /etc/gitlab/gitlab-secrets.json if necessary, as previously mentioned.Reconfigure, restart and check GitLab:

[root@ubuntu1804 ~]#gitlab-ctl reconfigure
[root@ubuntu1804 ~]#gitlab-ctl restart

#后续检查可选做
[root@ubuntu1804 ~]#gitlab-rake gitlab:check SANITIZE=true
#In GitLab 13.1 and later, check database values can be decrypted especially if /etc/gitlab/gitlab-secrets.json was restored, or if a different server is the target for the restore.
[root@ubuntu1804 ~]#gitlab-rake gitlab:doctor:secrets

# 恢复成功后，将之前停止的两个服务启动
[root@ubuntu1804 ~]# gitlab-ctl start sidekiq
ok: run: sidekiq: (pid 16859) 0s
[root@ubuntu1804 ~]# gitlab-ctl start unicorn
ok: run: unicorn: (pid 16882) 1s

#或者执行下面也可以
[root@ubuntu1804 ~]# gitlab-ctl restart

# 恢复后，项目及用户信息都已还原
# 注意：可能需要等一段时间才能打开浏览器进行访问
```





### K8S 上 GitLab 的备份与恢复



#### GitLab Operator备份方法

GitLab Operator 采用 **Custom Resources (CRs)** 来管理 GitLab，而关键数据仍然存储在 **ConfigMaps、Secrets 和 Persistent Volumes (PVs)** 中。



#####  1. 备份 GitLab Operator 相关的 CRD 配置

GitLab Operator 主要使用 **GitLab Custom Resource（CR）** 来定义 GitLab 部署，因此备份这些 CR 是最重要的步骤之一

**执行以下命令，导出 GitLab Custom Resource**

```bash
[root@master1 backup]# kubectl get gitlab -n gitlab-system -o yaml > gitlab-cr-backup.yaml

# 如果你有多个 GitLab CR 实例：
kubectl get gitlab -A  # 查看所有 GitLab 实例
kubectl get gitlab <your-gitlab-instance-name> -n gitlab-system -o yaml > gitlab-cr-backup.yaml
```



**2. 备份 GitLab Operator 的 ConfigMaps 和 Secrets**

GitLab Operator 使用 K8S **ConfigMaps 和 Secrets** 来存储部分配置，如数据库、存储、认证信息等。因此，你需要分别备份它们。

**(1) 备份 ConfigMaps**

```bash
kubectl get cm -n gitlab-system -o yaml > gitlab-configmaps-backup.yaml
```

**(2) 备份 Secrets**

```bash
kubectl get secrets -n gitlab-system -o yaml > gitlab-secrets-backup.yaml
```

Secrets 里可能包含：

- GitLab 初始管理员密码
- 数据库密码
- TLS 证书



**3. 备份 GitLab 数据**

GitLab 的关键数据仍然存储在 **Persistent Volumes (PVs)**，包括

- Git 仓库（Gitaly）
- 数据库（PostgreSQL）
- Redis（缓存）
- 对象存储（MinIO 或 S3）

列出所有 GitLab 相关的 PVC：

```bash
kubectl get pvc -n gitlab-system
```

然后使用 `kubectl cp` 备份

```bash
kubectl cp gitlab-gitaly-0:/var/opt/gitlab /backup/gitlab-gitaly -n gitlab-system
kubectl cp gitlab-postgresql-0:/var/lib/postgresql /backup/gitlab-postgresql -n gitlab-system
kubectl cp gitlab-redis-master-0:/data /backup/gitlab-redis -n gitlab-system
```



**4. 备份 GitLab Operator 的 CRDs**

GitLab Operator 本身依赖 **Custom Resource Definitions（CRDs）**，在恢复环境时，你需要先恢复这些 CRD。

```bash
kubectl get crd | grep gitlab
kubectl get crd gitlabs.gitlab.com -o yaml > gitlab-crd-backup.yaml
```



**5. 使用 Velero 进行整站备份**

如果你的 GitLab 部署在 **生产环境**，建议使用 **Velero** 进行完整的 Kubernetes 资源和数据备份：

```bash
velero backup create gitlab-backup --include-namespaces gitlab-system --wait
```

恢复 GitLab

```bash
velero restore create --from-backup gitlab-backup
```

 🚀   **Velero 是最适合 Kubernetes 环境下 GitLab Operator 的完整备份和恢复方案**，适用于生产环境！ 🚀





### GitLab 迁移和升级

在生产中升级往往伴随着服务器的迁移,比如从本地机房迁移到云环境中,而实现升级

#### 迁移流程

- 在原 GitLab 主机上备份配置文件和数据
- 在目标主机上安装相同的版本的 GitLab 软件
- 还原配置和数据
- 本质上就是备份和恢复的过程



#### 升级流程

- 如果新主机，需要先安装原版本，并还原配置和数据
- 不能直接跳过中间的版本直接升级,选择最近的大版本进行升级
  - 比如:12.1想升级到13.0,先升级到12.X最高版,再升级到13.0.
- 下载新版本的安装包,直接安装包
- 安装包时可能会提示出错,原因是版本升级后有些配置项会过时,根据提示修改配置即可
- 重新配置: gitlab-ctl reconfigure
- 重启服务: gitlab-ctl restart



### 实现 Https

GitLab 如果用于不安全的网络，建议使用 https

```ABAP
注意：建议使用权威CA颁发的证书，自签名的证书需要加入信任,否则会导致后续git clone等操作失败
```

官方说明

```http
https://docs.gitlab.com/omnibus/settings/nginx.html#enable-https
```



#### 创建证书

```bash
[root@gitlab ~]# mkdir -p /etc/gitlab/ssl && cd /etc/gitlab/ssl
[root@gitlab ssl]# openssl genrsa -out gitlab.wang.org.key 2048
[root@gitlab ssl]# openssl req -days 3650 -x509 \
-sha256 -nodes -newkey rsa:2048 -subj "/C=CN/ST=beijing/L=beijing/O=wang/CN=gitlab.wang.org" -keyout gitlab.wang.org.key -out gitlab.wang.org.crt
```



#### 修改配置文件

```bash
[root@gitlab ~]# vim /etc/gitlab/gitlab.rb
external_url "https://gitlab.wang.org" #此项必须修改为https，必选项
nginx['enable'] = true  #可选
nginx['client_max_body_size'] = '1000m' #可选
nginx['redirect_http_to_https'] = true  #必选项，默认值为false，修改为true，实现http自动301跳转至https
nginx['redirect_http_to_https_port'] = 80 #可选,所有请求80的都跳转到443，默认值，可不改，保持注释状态
nginx['ssl_certificate'] ="/etc/gitlab/ssl/gitlab.wang.org.crt"   #必选项
nginx['ssl_certificate_key'] ="/etc/gitlab/ssl/gitlab.wang.org.key"   #必选项
nginx['ssl_ciphers'] = "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256" #可选
nginx['ssl_prefer_server_ciphers'] = "on"  #可选
nginx['ssl_protocols'] = "TLSv1.2"    #可选
nginx['ssl_session_cache'] = "shared:SSL:10m"   #可选
nginx['ssl_session_timeout'] = "1440m"    #可选
```



#### 重新初始化

```bash
[root@gitlab ~]# gitlab-ctl reconfigure
[root@gitlab ~]# gitlab-ctl restart
[root@gitlab ~]# gitlab-ctl status

#还登录原来的URL,会自动跳转到 https
```



#### 解决自签名证书的信任问题

```bash
# 在git的客户端主机上信任该证书
[root@ubuntu2204 ~]# scp gitlab-server:/etc/gitlab/ssl/gitlab.wang.org.crt

# 将证书加入信任文件
# Ubuntu
[root@ubuntu2204 ~]# cat gitlab.wang.org.crt >> /etc/ssl/certs/ca-certificate.crt

# Rocky
[root@rocky8 ~]# cat gitlab.wang.org.crt >> /etc/pki/tls/certs/ca-bundle.crt
```



### GitLab 忘记密码解决方案

官方说明

```http
https://docs.gitlab.com/ee/security/reset_user_password.html#reset-the-root-password
```



#### 进入数据库

```bash
[root@gitlab ~]#gitlab-rails console -e production

# 此步可能比较慢,需要等一段时间
--------------------------------------------------------------------------------
 Ruby:         ruby 2.7.5p203 (2021-11-24 revision f69aeb8314) [x86_64-linux]
 GitLab:       15.1.2 (ea7455c8292) FOSS
 GitLab Shell: 14.7.4
 PostgreSQL:   13.6
------------------------------------------------------------[ booted in 23.59s ]
Loading production environment (Rails 6.1.4.7)

# 找到root用户
# 方法1
irb(main):001:0> user = User.find_by_username 'root'
# 方法2
irb(main):001:0> user = User.where(id: 1).first
=> #<User id:1 @root>

# 重设密码
irb(main):002:0> user.password="wang@123"
=> "wang@123"
irb(main):003:0> user.password_confirmation="wang@123"
=> "wang@123"

# 保存
irb(main):004:0> user.save
=> true

# 退出控制台
irb(main):005:0> quit

#验证用新密码登录
```





## DevOps之CICD服务器Jenkins



- **Jenkins 介绍**
- **Jenkins 部署**
- **Jenkins 基本配置**
- **Jenkins 实现 CICD**
- **Jenkins 分布式**
- **Jenkins 流水线 Pipeline**
- **代码质量检测 SonarQube**



###  Jenkins 部署与基本配置

####  Jenkins 介绍

![image-20250212201154944](../markdown_img/image-20250212201154944.png)

官方文档

```http
https://www.jenkins.io/zh/doc/
```

Jenkins 是基于 **Java 开发**的一种开源的CI（Continuous integration持续集成）&CD (Continuous  Delivery持续交付，Continuous Deployment持续部署)工具

Jenkins 用于监控持续重复的工作，旨在提供一个开放易用的软件平台，使软件的持续集成变成可能。可用于自动化各种任务，如构建，测试和部署软件。

Jenkins 作为一个可扩展的自动化服务器，可以用作简单的 CI 服务器，或者变成任何项目的持续交付中 心。

Jenkins 只是一个调度平台,其本身并不能完成项目的构建部署

Jenkins **需要安装各种插件**,可能还需要编写Shell,python脚本等才能调用和集成众多的组件来实现复杂的构建部署功能

![image-20250212201712573](../markdown_img/image-20250212201712573.png)



**主要用途**

- 持续、自动地构建/测试软件项目
- 监控一些定时执行的任务

**Jenkins特点**

- 开源免费
- 跨平台，支持所有的平台
- master/slave支持分布式的build
- web形式的可视化的管理页面
- 安装配置简单
- 及时快速的提示和帮助
- 已有的1800+插件



**Jenkins官方介绍视频**

```http
https://v.qq.com/x/page/m0509xul0xk.html
```





### Jenkins 安装和启动

**Jenkins 的安装**

Jenkins 支持多种部署和运行方式

- 包安装
- JAVA 的 WAR 文件
- 容器运行

```http
https://www.jenkins.io/zh/doc/book/installing/
```





#### 安装前环境准备

**系统要求**

```http
https://www.jenkins.io/doc/administration/requirements/java/
```

最低推荐配置

- 256MB可用内存
- 1GB可用磁盘空间(作为一个Docker容器运行jenkins的话推荐10GB)

为小团队推荐的硬件配置

-  1GB+可用内存
- 50 GB+ 可用磁盘空间

JAVA 软件配置

- Java 8—无论是Java运行时环境（JRE）还是Java开发工具包（JDK）都可以
- Jenkins requires Java 11 or 17 since Jenkins 2.357 and LTS 2.361.1. 



**系统准备**

```bash
#关闭防火墙和SELinux
#设置语言环境，防止后期Jenkins汉化出问题
[root@jenkins ~]# localectl set-locale LANG=en_US.UTF-8
```



**Java 环境**

```http
https://www.jenkins.io/doc/book/platform-information/support-policy-java/
```

jenkins基于JAVA实现，安装jenkins前需要先安装 JDK

```bash
#安装openjdk
#新版要求安装JDK-11版
[root@ubuntu2004 ~]#apt update && apt -y install openjdk-11-jdk
[root@rocky8 ~]#yum -y install java-11-openjdk

#旧版安装JDK-8版
[root@ubuntu1804 ~]#apt update
[root@ubuntu1804 ~]#apt -y install openjdk-8-jdk
```



#### Jenkins 包安装

注意：新版jenkins_2.401.2启动很慢，可能需要20分钟才能启动成功

##### 二进制包安装 Jenkins

```http
https://mirrors.tuna.tsinghua.edu.cn/jenkins/debian-stable/
```

![image-20250216154954145](../markdown_img/image-20250216154954145.png)

安装过程

```bash
# 下载java17, Jenkins 2.492.1 版本需要 Java 17 或 21
# 选择版本下载并安装
[root@mystical /var/lib]# apt install -y openjdk-17-jdk

# 下载并安装jenkins_2.492.1_all.deb
[root@mystical ~]# wget https://mirrors.tuna.tsinghua.edu.cn/jenkins/debian-stable/jenkins_2.492.1_all.deb
[root@mystical ~]# dpkg -i jenkins_2.492.1_all.deb
```



#### 基于 Kubernetes 部署 Jenkins

##### **基于 Storage Class 实现持久化**

需要部署名称为sc-nfs的Storage class 和 提供loadBalancer的服务，如OpenELB

```yaml
[root@master1 jenkins] # cat jenkins-deployment-service-pvc-sc-rabc.yaml 
apiVersion: v1
kind: Namespace
metadata:
  name: jenkins
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: jenkins-pvc
  namespace: jenkins
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: sc-nfs
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: jenkins-master
  namespace: jenkins
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: jenkins-master
rules:
  - apiGroups: ["extensions", "apps"]
    resources: ["deployments"]
    verbs: ["create", "delete", "get", "list", "watch", "patch", "update"]
  - apiGroups: [""]
    resources: ["services"]
    verbs: ["create", "delete", "get", "list", "watch", "patch", "update"]
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["create","delete","get","list","patch","update","watch"]
  - apiGroups: [""]
    resources: ["pods/exec"]
    verbs: ["create","delete","get","list","patch","update","watch"]
  - apiGroups: [""]
    resources: ["pods/log"]
    verbs: ["get","list","watch"]
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: jenkins-master
roleRef:
  kind: ClusterRole
  name: jenkins-master
  apiGroup: rbac.authorization.k8s.io
subjects:
- kind: ServiceAccount
  name: jenkins-master
  namespace: jenkins
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jenkins
  namespace: jenkins
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jenkins
  template:
    metadata:
      labels:
        app: jenkins
    spec:
      serviceAccountName: jenkins-master
      containers:
      - name: jenkins
        image: jenkins/jenkins:lts
        ports:
        - containerPort: 8080
          name: web
          protocol: TCP
        - containerPort: 50000
          name: agent
          protocol: TCP
        volumeMounts:
        - name: jenkins-volume
          mountPath: /var/jenkins_home
      volumes:
      - name: jenkins-volume
        persistentVolumeClaim:
          claimName: jenkins-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: jenkins
  namespace: jenkins
spec:
  type: LoadBalancer
  ports:
  - name: http
    port: 8080
    targetPort: 8080
  - name: agent
    port: 50000
    targetPort: 50000
  selector:
    app: jenkins
```

**启动应用**

```bash
[root@master1 jenkins]#kubectl apply -f jenkins-deployment-service-pvc-sc-rabc.yaml 
namespace/jenkins unchanged
persistentvolumeclaim/jenkins-pvc unchanged
serviceaccount/jenkins-master unchanged
clusterrole.rbac.authorization.k8s.io/jenkins-master unchanged
clusterrolebinding.rbac.authorization.k8s.io/jenkins-master unchanged
deployment.apps/jenkins created
service/jenkins unchanged

# 查看
[root@master1 jenkins]#kubectl get all -n jenkins 
NAME                           READY   STATUS    RESTARTS   AGE
pod/jenkins-5dd956745f-vmdjc   1/1     Running   0          88s

NAME              TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                          AGE
service/jenkins   LoadBalancer   10.103.70.150   172.22.200.12   8080:32367/TCP,50000:31193/TCP   2m38s

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/jenkins   1/1     1            1           88s

NAME                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/jenkins-5dd956745f   1         1         1       88s

# 访问 172.22.200.12:8080
```



#### 首次登录 Jenkins页面初始化

用浏览器访问： http://jenkins.mystical.org:8080/

默认内置用户admin，其密码为随机字符，可以从如下文件中查到密码

![image-20250212211710297](../markdown_img/image-20250212211710297.png)

```bash
# 查看密码
[root@master1 jenkins]#kubectl exec -it -n jenkins jenkins-5dd956745f-vmdjc -- /bin/bash
jenkins@jenkins-5dd956745f-vmdjc:~/secrets$ cd /var/jenkins_home/secrets/
jenkins@jenkins-5dd956745f-vmdjc:~/secrets$ cat initialAdminPassword 
8a5e445090f1412a89f857831a2258ae
```



**离线状态**

![image-20250216142300508](../markdown_img/image-20250216142300508.png)

如果显示 jenkins 已离线 ，将`/var/lib/jenkins/hudson.model.UpdateCenter.xm`l文件中的更新检 查地址改成国内镜像地址,如清华大学地址，然后重启 jenkins 即可：

```http
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
https://mirrors.aliyun.com/jenkins/updates/update-center.json
https://jenkins-zh.gitee.io/update-center-mirror/tsinghua/update-center.json
```

**示例：解决离线问题**

```bash
[root@ubuntu1804 ~]#vim /var/lib/jenkins/hudson.model.UpdateCenter.xml
<?xml version='1.1' encoding='UTF-8'?>
<sites>
 <site>
   <id>default</id>
#修改此行为下面行 <url>https://updates.jenkins.io/update-center.json</url>
   <url>https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json</url>
 </site>
</sites>
```

**选择安装 Jenkins 插件**

![image-20250212212328405](../markdown_img/image-20250212212328405.png)

![image-20250212214309954](../markdown_img/image-20250212214309954.png)

**建议选择无**

![image-20250212214434396](../markdown_img/image-20250212214434396.png)

为了解决插件安装慢的解决方式 ，利用清华的jenkins源通过 Nginx 进行 rewrite 或者反向代理，如下：

```bash
#此方式只支持http
#在jenkins服务器上修改/etc/hosts 指向新安装的nginx服务器：10.0.0.102
[root@jenkins-ubuntu ~]#vim /etc/hosts
10.0.0.102 updates.jenkins-ci.org updates.jenkins.io

#在另一台主机安装nginx，并修改配置
[root@ubuntu1804 ~]#apt -y install nginx
[root@ubuntu1804 ~]#vim /etc/nginx/sites-enabled/default

#加下面行
location /download/plugins {
    proxy_set_header Host mirrors.tuna.tsinghua.edu.cn;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    rewrite /download/plugins(.*) /jenkins/plugins/$1 break;
    proxy_pass http://mirrors.tuna.tsinghua.edu.cn;
}
[root@ubuntu1804 ~]#systemctl restart nginx
```



#### 创建 Jenkins 管理员(可选)

用户信息保存在下面目录

```bash
[root@jenkins ~]#ls /var/lib/jenkins/users/
```

系统默认有一个管理员帐号admin,继续即可

![image-20250216145627814](../markdown_img/image-20250216145627814.png)



#### 配置 Jenkins URL

保存完成即可

![image-20250216145654161](../markdown_img/image-20250216145654161.png)

![image-20250216145826296](../markdown_img/image-20250216145826296.png)

![image-20250216145845607](../markdown_img/image-20250216145845607.png)





### Jenkins 基础配置

#### 修改管理员密码

登录后需要立即修改密码

![image-20250216165009188](../markdown_img/image-20250216165009188.png)



![image-20250216165123246](../markdown_img/image-20250216165123246.png)



####  Jenkins 管理工具

```http
https://www.jenkins.io/doc/book/managing/cli/
```

Jenkins 指供了Web 管理界面,也提供了命令行管理工具

![image-20250216165620201](../markdown_img/image-20250216165620201.png)

![image-20250216165930874](../markdown_img/image-20250216165930874.png)

![image-20250216170009582](../markdown_img/image-20250216170009582.png)



```bash
[root@mystical ~]# wget http://10.0.0.222:8080/jnlpJars/jenkins-cli.jar
--2025-02-16 08:55:05--  http://10.0.0.222:8080/jnlpJars/jenkins-cli.jar
Connecting to 10.0.0.222:8080... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3712826 (3.5M) [application/java-archive]
Saving to: ‘jenkins-cli.jar’

jenkins-cli.jar            100%[=======================================>]   3.54M  --.-KB/s    in 0.02s   

2025-02-16 08:55:05 (171 MB/s) - ‘jenkins-cli.jar’ saved [3712826/3712826]

# 查看用法和命令
[root@mystical ~]# java -jar jenkins-cli.jar -s http://admin:123456@10.0.0.222:8080/ -webSocket help

# 列出任务
[root@mystical ~]# java -jar jenkins-cli.jar -s http://admin:123456@10.0.0.222:8080/ -webSocket list-jobs

# 重启jenkins
[root@mystical ~]# java -jar jenkins-cli.jar -s http://admin:123456@10.0.0.222:8080/ -webSocket restart

# 列出插件
[root@mystical ~]# java -jar jenkins-cli.jar -s http://admin:Zyf646130..@10.0.0.222:8080/ -webSocket list-plugins
```



#### Jenkins 插件管理及安装

jenkins 本身的功能有限,但是插件丰富,大大扩展了jenkins的功能,当前已有1800+的插件.

要想使用jenkins实现生产需求,就必须安装相应的插件才能实现特定的功能

```http
https://plugins.jenkins.io/
```

![image-20250216173831151](../markdown_img/image-20250216173831151.png)



##### 插件安装目录

```bash
[root@mystical ~]# ls /var/lib/jenkins/plugins/
bouncycastle-api      instance-identity.jpi     javax-mail-api        localization-support.jpi
bouncycastle-api.jpi  javax-activation-api      javax-mail-api.jpi    localization-zh-cn
instance-identity     javax-activation-api.jpi  localization-support  localization-zh-cn.jpi
......
```



##### 插件管理

插件安装过程中，如果因为某种原因导致有安装失败的插件，没有关系，可以后期再单独安装



##### 安装中文插件

![image-20250216174401400](../markdown_img/image-20250216174401400.png)

![image-20250216174436831](../markdown_img/image-20250216174436831.png)

![image-20250216174522245](../markdown_img/image-20250216174522245.png)

![image-20250216174550469](../markdown_img/image-20250216174550469.png)



中文插件安装完后，重启服务

![image-20250216175013165](../markdown_img/image-20250216175013165.png)

![image-20250216174752117](../markdown_img/image-20250216174752117.png)





#### Jenkins 优化配置

通过优化配置,可以提高后续的效率,此为可选内容



##### ssh 优化

Jenkins 服务器做为一个CICD工具,后续会经常使用 ssh 协议连接远程主机,为方便连接,建议修改自动信 任远程主机,避免首次连接的人为输入yes的确认过程

**方法1**：注意:需要安装Git或者Gitlab插件才能配置

![image-20250216180547019](../markdown_img/image-20250216180547019.png)

![image-20250216175858108](../markdown_img/image-20250216175858108.png)

![image-20250216175929485](../markdown_img/image-20250216175929485.png)

![image-20250216180705878](../markdown_img/image-20250216180705878.png)

**方法2**：在 Jenkins 服务器修改 ssh的客户端配置文件

```bash
[root@jenkins ~]#vi /etc/ssh/ssh_config
 # StrictHostKeyChecking ask #修改此行如下面
   StrictHostKeyChecking no
 #修改客户端配置无需重启ssh服务
```



##### 性能优化

默认只能并行2个任务,建议根据CPU核心数,将执行器数量修改为CPU的核数

![image-20250216180950089](../markdown_img/image-20250216180950089.png)

![image-20250216181152343](../markdown_img/image-20250216181152343.png)

![image-20250216181230865](../markdown_img/image-20250216181230865.png)





#### Jenkins 的备份还原

Jenkins的相关数据都是放在主目录中, 将主目录备份即可实现Jenkins的备份,必要时用于还原

另外如果有相关脚本等,也需要进行备份

可以如下查看目录位置

![image-20250216181459569](../markdown_img/image-20250216181459569.png)

![image-20250216181524386](../markdown_img/image-20250216181524386.png)

jenkins 主目录包含以下文件和目录

```bash
*.xml                     # 需要备份
config-history            # 需要备份
fingerprints              # 需要备份
global-build-stats        # 需要备份
*.key*                    # 需要备份
jobs                      # jobs配置需要备份（config.xml, nextBuildNumber）, builds目录, builds目录（build logs                               等）根据需求而定
nodes                     # 需要备份
plugins                   # 需要备份 *.jpi及 *.hpi，可以不备份每个插件子目录，jenkins启动后会更新插件子目录
secrets                   # 需要备份
updates                   # 需要备份
userContent               # 用户上传内容，可以根据需要备份
users                     # 用户缓存信息，最好备份
logs                      # 插件logs，根据需要而定，可以不备份
monitoring                # 可以不备份，插件会实时生成监控数据
```



#### 找回忘记的密码

```bash
# 停止服务
[root@mystical ~]# systemctl stop jenkins

# 删除jenkins主目录中config.xml的如下内容
###########################################################

<useSecurity>true</useSecurity>
  <authorizationStrategy class="hudson.security.FullControlOnceLoggedInAuthorizationStrategy">
    <denyAnonymousReadAccess>true</denyAnonymousReadAccess>
  </authorizationStrategy>
  <securityRealm class="hudson.security.HudsonPrivateSecurityRealm">
    <disableSignup>true</disableSignup>
    <enableCaptcha>false</enableCaptcha>
  </securityRealm>

#################################################################
...

# 重启Jenkins
 systemctl start jenkins

#重新无需验证即可登录，修改安全配置为Jenkins's own user database(Jenkins专有用户数据库),保存后
```

![image-20250216182639752](../markdown_img/image-20250216182639752.png)

![image-20250216182713874](../markdown_img/image-20250216182713874.png)

![image-20250216182729955](../markdown_img/image-20250216182729955.png)

![image-20250216182817594](../markdown_img/image-20250216182817594.png)

系统管理”,发现此时出现“管理用户”

![image-20250216182946287](../markdown_img/image-20250216182946287.png)

![image-20250216183028939](../markdown_img/image-20250216183028939.png)

![image-20250216183059288](../markdown_img/image-20250216183059288.png)

![image-20250216183117733](../markdown_img/image-20250216183117733.png)

系统管理--- 全局安全配置 --- 授权策略 

将任何用户可以做任何事(没有任何限制) 修改为登录用户可以做任何事

![image-20250216183255050](../markdown_img/image-20250216183255050.png)





### Jenkins 实现 CICD



#### Jenkins 实现 CICD 说明

任务中构建将程序源码转换成一个可用的目标Target的过程，该过程可能会包括获取下载源码、解决依赖、编译和打包等环节

目标可以包括库、可执行文件及生成的脚本等，该类文件即是所谓的“制品”,它们通常应该存储于制品库,**Nexus就是著名的制品库服务**

程序员可以在本地进行构建，但基于有标准、统一构建环境的构建系统完成应用程序的构建，能有效确保制品质量

Jenkins虽然可以为构建服务器，但自身并未提供构建工具

Jenkins可以集成用户所需要的大部分主流构建工具来实现完整的构建过程

构建工具与源程序的编程语言及工程工具有密切关系,因而,在Jenkins服务器中具体需要安装和集成的构 建工具,取决于用户的实际需要

- Maven: Java
- Go:  Golang
- Gradle:  Java,Groovey和Kotlin等
- SBT: Scala
- Babel、Browserify、Weboack、Grunt及Gulp等: javascript



**Jenkins 架构**

![image-20250217104707079](../markdown_img/image-20250217104707079.png)

Jenkins根据业务场景的不同,提供了多种风格的任务，默认是自由风格任务，通过安装插件，还可以支持其它风格的插件



**Job 的风格分类**

- **自由风格freestyle**：支持实现各种开发语言的不同场景的风格，以Shell为主要技术，内部有各种灵活的配置属性，默认只有此类型

- **流水线 pipeline**：重点掌握的风格，使用专用语法
- **Maven 项目**：仅适用于 JAVA 项目





#### 创建 Freestyle 风格的任务 Job

##### Freestyle 风格任务说明

![image-20250217104958777](../markdown_img/image-20250217104958777.png)



自由风格的任务提供了下面的组成

- **通用配置**：当前任务的基本配置，历史记录、存储数据、认证、存储目录等

- **源码管理**：指定当前任务依赖的代码仓库地址(仓库的分支)
- **构建触发器**：在什么情况下，才会自动执行当前的任务
- **构建环境**：构建过程中，依赖的环境变量等
- **构建**：当前的代码构建操作，实现CICD核心步骤
- **构建后动作**：构建任务成功后，我们可以做的事情，发送邮件、提交代码标签、触发其他任务、等等



**构建状态**

```http
晴雨表主要是针对一个任务的整体执行成功比例来算的。80%成功表示太阳。
```

![image-20250217105645560](../markdown_img/image-20250217105645560.png)



##### 实现一个简单的 Freestyle 任务

注意：默认使用sh 的shell类型，可以使用#!/bin/bash 声明使用bash 的shell

![image-20250217110008874](../markdown_img/image-20250217110008874.png)



![image-20250217110057327](../markdown_img/image-20250217110057327.png)

![image-20250217110203690](../markdown_img/image-20250217110203690.png)

注意：默认 Freestyle 任务的Shell 使用 /bin/sh ，如果想使用 /bin/bash ，需要在最前面加shebang 机制

![image-20250217110438438](../markdown_img/image-20250217110438438.png)

保存后，立即构建

![image-20250217110509855](../markdown_img/image-20250217110509855.png)

查看控制台输出

![image-20250217110547061](../markdown_img/image-20250217110547061.png)

![返回首页](../markdown_img/image-20250217110620009.png)

返回首页，可以看到构建任务的晴雨表

![image-20250217110734652](../markdown_img/image-20250217110734652.png)

```bash
# 查看上述任务构建的文件
[root@master1 ~]#kubectl exec -n jenkins jenkins-58df579f8c-gq72v -- cat /var/jenkins_home/workspace/freestyle-demo1/test1.txt
demo1-test
```



为方便调试，在生产环境中更多的是在服务器上创建一个指定的Jenkins脚本的文件夹，使用 `bash -x XXX.sh` 来执行脚本

```bash
# /data目录以hostPath的方式挂载到pod上
[root@node1 jenkins]#mkdir -p /data/jenkins/

[root@node1 jenkins]#cat /data/jenkins/hello.sh 
#!/bin/bash
echo "Hello, World"
```

![image-20250217121026616](../markdown_img/image-20250217121026616.png)

构建后，查看控制台输出

![image-20250217121056528](../markdown_img/image-20250217121056528.png)



#####  Jenkins 构建的环境变量

 **Jenkins 环境变量说明**

构建时，Jenkins 支持使用变量,从而增强了任务的灵活性

环境变量有**内置**和**自定义**两种

在自由风格的的shell中可以使用`${VAR_NAME}`引用变量



**Pipeline 中引用全局环境**

- Jenkins内置的全局环境变量可被所有的pipeline引用，它们以“env.”为前缀
- 在pipeline中引用全局环境变量格式有三种：
  - `${env.<ENV_VAR_NAME>} `不支持在shell 中引用
  - `$env.<ENV_VAR_NAME> `不支持在shell 中引用
  - `${ENV_VAR_NAME}`     支持在shell 中引用



**Jenkins 内置环境变量**

```ABAP
注意：Jenkins的环境变量和root用户看到环境变量不完全相同
```



**查看Jenkins内置环境变量**

```http
http://172.22.200.12:8080/env-vars.html/
```

![image-20250217112015151](../markdown_img/image-20250217112015151.png)

```http
http://172.22.200.12:8080/manage/systemInfo
```

![image-20250217112105065](../markdown_img/image-20250217112105065.png)



**自定义环境变量**

变量的优先级顺序：

```ABAP
任务中的自定义的变量 > Jenkins 的自定义环境量 > Jenkins 内置的环境变量
```

**创建环境变量**

自定义变量可以在系统管理--配置系统--全局属性-- 环境变量 定义

注意：如果自定义环境变量与内置全局环境变量同名时，内置全局环境变量将被自定义环境变量覆盖

这可能会引起错误，必要时，可为自定义环境变量使用固定的前缀，例如“_ _”等

![image-20250217113700661](../markdown_img/image-20250217113700661.png)

![image-20250217113836606](../markdown_img/image-20250217113836606.png)

在作业中使用自定义的环境变量

![image-20250217113938728](../markdown_img/image-20250217113938728.png)

构建后查看

![image-20250217114012533](../markdown_img/image-20250217114012533.png)

####  Jenkins 结合 GitLab 实现代码下载

```HTTP
https://docs.gitlab.com/ee/integration/jenkins.html
```

##### GitLab 创建项目

```http
https://gitee.com/lbtooth/wheel_of_fortune.git
```

**导入项目**

![image-20250217114404742](../markdown_img/image-20250217114404742.png)

![image-20250217140837184](../markdown_img/image-20250217140837184.png)

![image-20250217140905835](../markdown_img/image-20250217140905835.png)

![image-20250217140934187](../markdown_img/image-20250217140934187.png)



##### Jenkins 安装和 Gitlab 相关的插件

只有安装GitLab插件,才能让Jenkins和GitLab相连

在管理插件中搜索需要插件 gitlab，其它依赖的插件会自动安装

![image-20250217150558897](../markdown_img/image-20250217150558897.png)



##### Jenkins 服务器创建访问GitLab的凭据

**Jenkins 凭证概述**

凭证就是认证到某个系统中的认证信息，用于提供对受限资源的访问; 

Jenkins所支持的凭证类型如下

- 用户名和密码(Username with password)
- SSH用户名和私钥对(SSH Username with private key)
- Github App
- Secret file: 需要保密的文本文件，保存有Token等信息
- Secret text:Token,串需要保密的文本，例如Github的API Token等
- Certificate
- 其它凭证类型还有二进制数据，或者更复杂形式的项目，例如OAuth凭证等;



**凭证的作用域**决定了它可用的目标范围

- **系统**:作用于Jenkins系统自身，仅可用于系统和后台任务，且一般用于连接到agent节点之上
- **全局**:作用于Jenkins上的所有任务，以确保任务的正常执行
- **用户**:作用于用户级别，仅生效于Jenkins中的线程代表该用户进行身份验证之时

```ABAP
注意: 在Jenkins内部，凭证被存放在JENKINS_ HOME目录下的secrets目录中，请务必确保该目录的访问权限进行了正确的设置
```



**添加基于用户名和密码类型的凭据**

如果基于http协议则无需实现ssh key 凭证,而选择添加gitlab用户名和密码的形式

如下图，表示对该连接没有连接权限，因为该仓库是私有仓库，因此需要账号密码或者ssh验证才能登录

![image-20250217152720707](../markdown_img/image-20250217152720707.png)



添加用户凭证，即访问gitlab的用户密码

![image-20250217152829054](../markdown_img/image-20250217152829054.png)

![image-20250217152845398](../markdown_img/image-20250217152845398.png)

![image-20250217153045186](../markdown_img/image-20250217153045186.png)

```http
服务器如果使用http连接，一旦gitlab上配置了https，则Jenkins上需要考虑服务器证书问题，因此建议用ssh连接
```



**关于 Git 的 SSL 证书验证解决方案**

```ABAP
详情见：知识扩展 -> Git相关用法补充 -> 绕过Git的SSL证书验证方法
```



**创建基于 ssh key 的凭据**

实现jenkins服务器到gitlab服务器的基于密钥的验证，可以让jenkins连接到gitlab执行操作，比如拉取代码

```ABAP
注意：ssh key的凭据可以基于jenkins用户或任意主机的其它任何用户的公钥私钥对都可以，但都需要在gitlab将此用户的公钥public key 和在gitlab主机上与gitlab的用户进行关联，并将私钥private key在jenkins创建为SSH Username with private key类型的凭据

总结：gitlab上指定用户上传的公钥和jenkins上的凭据（私钥）匹配即可
```



 **在 Jenkins 服务器上生成 ssh key**

```bash
# 在jenkins的主机上创建公私钥对
# [root@node1 data]# ssh-keygen

# 生成公私钥对后，将公钥上传gitlab
```

![image-20250217161748213](../markdown_img/image-20250217161748213.png)

然后将私钥上传到jenkins的凭据中

**注意**：此处的 username 只是注释性功能，理论上可以随便填写，只要确保此处private key和在 gitlab上关联的公钥是一对即可

![image-20250217161823375](../markdown_img/image-20250217161823375.png)

![image-20250217162058432](../markdown_img/image-20250217162058432.png)

保存后，没有报错，即表示jenkins有权限拉去gitlab的代码

![image-20250217162144524](../markdown_img/image-20250217162144524.png)



```ABAP
如果ssh连接方法出现下面报错，是因为Jenkins以Jenkins用户身份运行，首次连接Gitlab服务器会弹出未知主机的 警告，需要添加信任
```

![image-20250217163035747](../markdown_img/image-20250217163035747.png)

**解决方法**

```ABAP
参考：DevOps之CICD服务器Jenkins -> Jenkins基础配置 -> Jenmins优化配置 -> ssh优化
```



git仓库连接成功后选择要拉取的分支

![image-20250217163550403](../markdown_img/image-20250217163550403.png)

直接保存构建，代码即可拉取到 Jenkins 服务器上

![image-20250217163705311](../markdown_img/image-20250217163705311.png)

![image-20250217163826379](../markdown_img/image-20250217163826379.png)

查看Jenkins工作目录下代码是否拉取成功

```bash
jenkins@jenkins-578dc9ccf4-nk8g4:~/workspace/freestyle-wheel-demo1# ls
images	index.html  js
```





#### 配置 Jenkins 结合 GitLab 实现自动化前端项目的部署和回滚



#####  Jenkins 创建任务

![image-20250217164331078](../markdown_img/image-20250217164331078.png)



##### 配置 Git 项目地址和凭证

![image-20250217164408642](../markdown_img/image-20250217164408642.png)

##### 准备脚本并加入构建任务

```bash
[root@node1 jenkins]#cat wheel-html-gitlab-deploy-rollback.sh 
#!/bin/bash
#
#********************************************************************
#Author:            mystical
#QQ:                29308620
#Date:              2025-02-17
#FileName:          wheel-html-gitlab-deploy-rollback.sh
#URL:               http://www.mysticalrecluse.com
#Description:       The test script
#Copyright (C):     2025 All rights reserved
#********************************************************************

HOST_LIST="
172.22.200.101
172.22.200.102
"

APP=wheel
APP_PATH=/var/www/html
DATA_PATH=/opt
DATE=$(date +%F_%H-%M-%S)

deploy() {
    for i in ${HOST_LIST}; do
        ssh root@$i "rm -rf ${APP_PATH} && mkdir -pv ${DATA_PATH}/${APP}-${DATE}"
        scp -r * root@$i:${DATA_PATH}/${APP}-${DATE}
        ssh root@$i "ln -sv ${DATA_PATH}/${APP}-${DATE} ${APP_PATH}"
    done
}

rollback() {
    for i in ${HOST_LIST}; do
        CURRENT_VERSION=$(ssh root@$i "readlink $APP_PATH")
        CURRENT_VERSION=$(basename ${CURRENT_VERSION})
        echo ${CURRENT_VERSION}
        PRE_VERSION=$(ssh root@$i "ls -l ${DATA_PATH} | grep -B1 ${CURRENT_VERSION}|head -n1")
        echo $PRE_VERSION
        PRE_VERSION=$(echo $PRE_VERSION|awk '{print $NF}')
        ssh root@$i "rm -rf ${APP_PATH} && ln -sv ${DATA_PATH}/${PRE_VERSION} ${APP_PATH}"
    done
}

case $1 in
deploy)
    deploy
    ;;
rollback)
    rollback
    ;;
*)
    exit
    ;;
esac
```

![image-20250218091936057](../markdown_img/image-20250218091936057.png)

![image-20250218091957718](../markdown_img/image-20250218091957718.png)

查看控制台输出

![image-20250218092020644](../markdown_img/image-20250218092020644.png)

##### 服务器验证数据

```bash
[root@mystical /opt]# ll
total 28
drwxr-xr-x  7 root root 4096 Feb 17 14:41 ./
drwxr-xr-x 19 root root 4096 Apr 17  2024 ../
drwxr-xr-x  2 root root 4096 Feb 17 06:48 wheel/
drwxr-xr-x  4 root root 4096 Feb 17 11:01 wheel-2025-02-17_11-01-21/
drwxr-xr-x  4 root root 4096 Feb 17 14:29 wheel-2025-02-17_14-29-20/
drwxr-xr-x  4 root root 4096 Feb 17 14:30 wheel-2025-02-17_14-30-50/
drwxr-xr-x  4 root root 4096 Feb 17 14:41 wheel-2025-02-17_14-41-47/

[root@mystical /opt] $ll /var/www/html
lrwxrwxrwx 1 root root 30 Feb 17 14:41 /var/www/html -> /opt/wheel-2025-02-17_14-41-47/
```

**访问`172.22.200.101`和`172.22.200.102`**

![image-20250218093456929](../markdown_img/image-20250218093456929.png)



##### 修改代码再上传重新构建

```bash
# 取消ssl验证
[root@mystical ~]# git config --global http.sslVerify false

# 拉取代码
[root@mystical ~]# git clone http://gitlab.mygitlab.mystical.org/devops/wheel_of_fortune.git

# 修改代码后重新上传
[root@mystical ~]# vim index.html
[root@mystical ~]# git add .
[root@mystical ~]# git commit -m'change 500w'
[root@mystical ~]# git push origin master 
```

重新执行任务，可以看到如下修改

![image-20250218100753510](../markdown_img/image-20250218100753510.png)



##### 实现版本回滚任务

新建任务如下,实现回滚功能

![image-20250218101055995](../markdown_img/image-20250218101055995.png)

只修改构建的shell部分,其它不变

![image-20250218101215004](../markdown_img/image-20250218101215004.png)

![image-20250218101232842](../markdown_img/image-20250218101232842.png)

执行任务后,可以查看到 Web页面是否还原为上一个版本

![image-20250218102553543](../markdown_img/image-20250218102553543.png)



#### 参数化构建

jenkins支持参数化构建，类似于脚本中的参数，可以实现灵活的构建任务

Jenkins 支持多种参数类型,比如:Boolean,Choice选项,字符串,Multi_line字符串,文件类型等



##### 参数类型说明

参数化构建的目标在于为流水线提供基于参数值的灵活构建机制，从而让一个流水线的定义可以适用于多种需求情形

- 其功能与引用方式与环境变量类似
- 在触发作业运行之时，需要向各参数赋值
- 参数在使用时实际上也表现为变量，可以通过变量的调用方式使用参数
- 注意: 参数化功能无需安装插件即可支持

**常用的参数类型**

![image-20250218103626204](../markdown_img/image-20250218103626204.png)



##### 创建包含各种类型参数的任务

###### 布尔值参数Boolean  Parameter

![image-20250218104051835](../markdown_img/image-20250218104051835.png)

![image-20250218104102212](../markdown_img/image-20250218104102212.png)

![image-20250218104113979](../markdown_img/image-20250218104113979.png)

![image-20250218104124076](../markdown_img/image-20250218104124076.png)

构建后，查看控制台输出

![image-20250218104159641](../markdown_img/image-20250218104159641.png)



###### 选项参数Choice  Parameter

![image-20250218104646702](../markdown_img/image-20250218104646702.png)

![image-20250218104700098](../markdown_img/image-20250218104700098.png)

![image-20250218104712039](../markdown_img/image-20250218104712039.png)

可以选择指定的参数值

![image-20250218104750056](../markdown_img/image-20250218104750056.png)

点击Build构建后，查看控制台输出

![image-20250218104847954](../markdown_img/image-20250218104847954.png)

###### 字符参数 String Parameter

![image-20250218105208649](../markdown_img/image-20250218105208649.png)

![image-20250218105224135](../markdown_img/image-20250218105224135.png)



![image-20250218105244529](../markdown_img/image-20250218105244529.png)

![image-20250218105255321](../markdown_img/image-20250218105255321.png)

可以更改后，提交构建，查看控制台效果

![image-20250218105344473](../markdown_img/image-20250218105344473.png)

![image-20250218105402461](../markdown_img/image-20250218105402461.png)

###### 文本参数Multi-line String  Parameter

![image-20250218105601062](../markdown_img/image-20250218105601062.png)

![image-20250218105615340](../markdown_img/image-20250218105615340.png)

![image-20250218105627520](../markdown_img/image-20250218105627520.png)

更改后，提交构建，查看控制台输出（**换行被空格替代，所有文本在一行输出**）

![image-20250218105743516](../markdown_img/image-20250218105743516.png)

**如果想要保留多行，需要将变量用双引号引起来**

![image-20250218110358635](../markdown_img/image-20250218110358635.png)

![image-20250218110419179](../markdown_img/image-20250218110419179.png)



#####  选项参数实现不同分支的部署

###### 查看当前分支

```bash
# 查看当前分支
[root@mystical ~/project/testproject]# git branch -v
  devel ef9119b add v2 devel
* main  2b25da9 create index v1

# 查看main分支日志
[root@mystical ~/project/testproject]# git log
commit 2b25da926eaaac186a7c2dbdfa339fb02cacc36d (HEAD -> main, origin/main)
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 05:05:16 2025 +0000

    create index v1

commit e092f325efc674a587453905234dd6095cc3fd88
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 03:25:56 2025 +0000

    add README

# 查看devel分支日志
[root@mystical ~/project/testproject]# git checkout devel 
Switched to branch 'devel'
[root@mystical ~/project/testproject]# git log
commit ef9119b63d267ddd0b4e2cbd4b3f92e557e9d759 (HEAD -> devel, origin/devel)
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 05:07:14 2025 +0000

    add v2 devel

commit 2b25da926eaaac186a7c2dbdfa339fb02cacc36d (origin/main, main)
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 05:05:16 2025 +0000

    create index v1

commit e092f325efc674a587453905234dd6095cc3fd88
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 03:25:56 2025 +0000

    add README
```

###### 准备构建脚本

```bash
[root@node1 jenkins]#cat deploy.sh 
#!/bin/bash
#
#********************************************************************
#Author:            mystical
#QQ:                29308620
#Date:              2025-02-18
#FileName:          deploy.sh
#URL:               http://www.mysticalrecluse.com
#Description:       The test script
#Copyright (C):     2025 All rights reserved
#********************************************************************

BRANCH=$1

ls /data/git &> /dev/null || mkdir -pv /data/git
cd /data/git && rm -rf testproject
git clone -b $BRANCH git@gitlab.mygitlab.mystical.org:devops/testproject.git
cd testproject

case $BRANCH in
main)
    scp -r * root@172.22.200.101:/var/www/html/
    ;;
devel)
    scp -r * root@172.22.200.102:/var/www/html/
    ;;
*)
    echo $BRANCH is error
    ;;
esac
```

###### 新建任务，并配置参数化构建

![image-20250218135016459](../markdown_img/image-20250218135016459.png)

![image-20250218135044179](../markdown_img/image-20250218135044179.png)

分别执行main分支和devel分支

![image-20250218135122352](../markdown_img/image-20250218135122352.png)

###### 查看效果

![image-20250218135820662](../markdown_img/image-20250218135820662.png)

![image-20250218135735134](../markdown_img/image-20250218135735134.png)

![image-20250218135754886](../markdown_img/image-20250218135754886.png)



![image-20250218135829123](../markdown_img/image-20250218135829123.png)



![image-20250218135856630](../markdown_img/image-20250218135856630.png)

#### 利用 Git Parameter 插件实现拉取指定版本

##### 创建多个tag，并同步到仓库

```bash
# 查看当前git日志
[root@mystical ~/project/wheel_of_fortune]# git log
commit a03647ff47edf0b0ca1289473ff013b057ddeeee
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 02:21:48 2025 +0000

    change 3002

commit 26551d643447ebebf0eab4a5a40905e9bab82ebc
Author: mystical <mysticalrecluse@gmail.com>
Date:   Tue Feb 18 02:04:56 2025 +0000

    change 500w

commit 46b0c7a08624cae2d1f96fdbf20434b1b68362cf
Author: mystical <mysticalrecluse@gmail.com>
Date:   Mon Feb 17 14:41:13 2025 +0000

    change 100w

commit 730984d25d3b79610f7cc113c5c9d1c2b340cdbb
Author: yangchao <chao.yang@bridgetek.cn>
Date:   Wed Aug 8 19:48:30 2018 +0800

# 给每个阶段打上标签
[root@mystical ~/project/wheel_of_fortune]# git tag v1.0 730984d25d3b79610
[root@mystical ~/project/wheel_of_fortune]# git tag v2.0 46b0c7a08624cae2
[root@mystical ~/project/wheel_of_fortune]# git tag v3.0 26551d643447ebeb
[root@mystical ~/project/wheel_of_fortune]# git tag v4.0 a03647ff47edf0b0c

# 同步tags到仓库
git push origin --tags
```



##### 安装 Git Parameter 插件

![image-20250218141614844](../markdown_img/image-20250218141614844.png)



##### 创建任务

![image-20250218141824687](../markdown_img/image-20250218141824687.png)

![image-20250218142143511](../markdown_img/image-20250218142143511.png)

![image-20250218142309665](../markdown_img/image-20250218142309665.png)

![image-20250218142644353](../markdown_img/image-20250218142644353.png)

![image-20250218142715442](../markdown_img/image-20250218142715442.png)

##### 选择指定tag，构建测试后观察效果

![image-20250218142804116](../markdown_img/image-20250218142804116.png)

![image-20250218142856390](../markdown_img/image-20250218142856390.png)

![image-20250218143043448](../markdown_img/image-20250218143043448.png)

![](../markdown_img/image-20250218142952407.png)





#### 实现 Java 应用源码编译并部署

java 程序需要使用构建工具,如: maven,ant,gradle等进行构建打包才能部署,其中**maven**比较流行

以下以 maven 为例实现 Java 应用部署



##### 自由风格的任务构建基于 Spring Boot 的 JAR 包部署 JAVA 项目

###### Gitlab导入项目

项目链接

```http
https://gitee.com/lbtooth/helloworld-spring-boot
```

![image-20250218144012874](../markdown_img/image-20250218144012874.png)



###### Jenkins 服务器上安装 maven 和配置镜像加速

```bash
[root@jenkins ~]#apt update && apt  -y install maven

# 配置镜像加速，全局配置
[root@mystical ~]# vim /etc/maven/settings.xml
......
    <mirror>
         <id>nexus-aliyun</id>
         <mirrorOf>*</mirrorOf>
         <name>Nexus aliyun</name>
         <url>http://maven.aliyun.com/nexus/content/groups/public</url>
    </mirror>
</mirrors>

# 也可以配置项目级别的加速
[root@mystical ~/project/helloworld-spring-boot]# vim pom.xml
##############################################
......
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
......
###########################################
```



###### 准备相关脚本

```bash
#!/bin/bash

APP_PATH=/data/spring-boot-helloworld

HOST_LIST="
172.22.200.101
172.22.200.102
"

mvn clean package -Dmaven.test.skip=true

for host in $HOST_LIST; do
	ssh root@$host killall -9 java &> /dev/null
	scp target/helloworld-spring-boot-*-SNAPSHOT.jar root@$host:${APP_PATH}/spring-boot-helloworld.jar
	ssh root@$host "nohup java -jar ${APP_PATH}/spring-boot-helloworld.jar --server.port=8888 &>/dev/null &"&
done
```



###### 创建 Jenkins 任务

![image-20250219154044944](../markdown_img/image-20250219154044944.png)

![image-20250219154128825](../markdown_img/image-20250219154128825.png)



###### 构建并检查结果

![image-20250219160350420](../markdown_img/image-20250219160350420.png)

![image-20250219160416294](../markdown_img/image-20250219160416294.png)

![image-20250219160521103](../markdown_img/image-20250219160521103.png)

![image-20250219160540684](../markdown_img/image-20250219160540684.png)





##### 自由风格的任务构建单体的 Java 应用到Tomcat服务

```ABAP
注意：此项目使用JDK-11，不支持JDK-17
```

###### Gitlab仓库中准备 Java 代码

**在gitlab新建 java 项目**

```http
https://gitee.com/lbtooth/hello-world-war.git
```

**导入项目**

![image-20250221160046639](../markdown_img/image-20250221160046639.png)

![image-20250221160205323](../markdown_img/image-20250221160205323.png)





###### 临时切换 java11 版本

```bash
[root@mystical /data/jenkins/script]# export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
[root@mystical /data/jenkins/script]# export PATH=$JAVA_HOME/bin:$PATH
```

###### Server服务器上，安装tomcat

```bash
[root@mystical ~]# apt install -y tomcat9
```

###### 准备相关脚本

```bash
[root@mystical /data/jenkins/script]# cat hello-world-war.sh 
#!/bin/bash

APP_PATH=/var/lib/tomcat9/webapps

HOST_LIST="
    172.22.200.101
    172.22.200.102
"
mvn clean package -Dmaven.test.skip=true

for host in $HOST_LIST; do
	ssh root@$host systemctl stop tomcat9
	scp target/hello-world-war-*.war root@$host:${APP_PATH}/hello.war
	ssh root@$host systemctl start tomcat9
done
```

![image-20250221180800840](../markdown_img/image-20250221180800840.png)



![image-20250221180822036](../markdown_img/image-20250221180822036.png)



###### 执行构建后查看效果

![](../markdown_img/image-20250221180910711.png)

![image-20250221180923368](../markdown_img/image-20250221180923368.png)

#### 实现 Golang 应用源码编译并部署

##### 在Jenkins 安装 Golang 环境

```bash
#基于仓库安装
[root@ubuntu2004 ~]#apt update && apt -y install golang
[root@ubuntu2004 ~]#go version
go version go1.18.1 linux/amd64	

#或者从官网下载指定版本自行安装
```



##### 准备 Golang 源代码和数据库环境

###### 项目1：ginweb 项目

```http
https://gitee.com/lbtooth/ginweb.git
```

范例：准备数据库环境
````bash
# 下载源码进行修改
[root@ubuntu2204 ~]#git clone https://gitee.com/lbtooth/ginweb.git
[root@ubuntu2204 ~]#cd  ginweb

# 查看构建说明
[root@mystical ~/project/ginweb] $cat README.md 
# Golang 的 Web 测试项目
```
https://gitee.com/lbtooth/ginweb
```

## 1. 安装前环境准备
### 参看和修改文件 conf/ginweb.ini
### 安装 MySQL和Redis,按如下配置用户和密码
```sh
[mysql]
host = "127.0.0.1"
port = 3306
databases = "ginweb"
user = "ginweb"
passwd = "123456"

[redis]
host = "127.0.0.1"
port = 6379
passwd = "123456"
```

## 2. 链接访问
## http://localhost:8888

## 3. 默认登录用户/密码
## admin/123456

# 基于上述构架说明，对ginweb.ini文件进行修改
[root@mystical ~/project/ginweb] $cat conf/ginweb.ini 

[mysql]
host = "172.22.200.111"
port = 3306
databases = "ginweb"
user = "ginweb"
passwd = "123456"

[redis]
host = "172.22.200.111"
port = 6379
passwd = "123456"

# 准备MySQL和Redis
[root@ubuntu2204 ~]# apt update && apt -y install mysql-server redis 

# 修改MySQL配置
[root@mystical ~]# vim /etc/mysql/mysql.conf.d/mysqld.cnf
#bind-address           = 127.0.0.1
#mysqlx-bind-address    = 127.0.0.1
[root@mystical ~]# systemctl restart mysql

# 配置MySQL环境
[root@mystical ~]# mysql
mysql> create database ginweb;
Query OK, 1 row affected (0.01 sec)

mysql> create user ginweb@'172.22.200.%' identified by '123456';
Query OK, 0 rows affected (0.00 sec)

mysql> grant all on ginweb.* to ginweb@'172.22.200.%';
Query OK, 0 rows affected (0.00 sec)

# 导入表结构
[root@mystical ~/project/ginweb]# mysql -uginweb -p123456 -h 172.22.200.111 ginweb < ginweb.sql 
mysql: [Warning] Using a password on the command line interface can be insecure.

# 准备redis
[root@mystical ~]# vim /etc/redis/redis.conf
bind 0.0.0.0
requirepass 123456
[root@mystical ~]# systemctl restart redis
````



##### Gitlab创建项目

创建空白项目，并将之前的更改后的ginweb项目上传至创建好的项目中

![image-20250222095526522](../markdown_img/image-20250222095526522.png)

![image-20250222095606814](../markdown_img/image-20250222095606814.png)

```bash
# 删除之前的remote的地址，将之前拉下来的项目的remote值改为刚创建的gitlab仓库的地址
[root@mystical ~/project/ginweb]# git remote remove origin
[root@mystical ~/project/ginweb]# git remote add origin https://gitlab.mygitlab.mystical.org/devops/ginweb.git
[root@mystical ~/project/ginweb]# git push origin master

# 将更改后的记录上传
[root@mystical ~/project/ginweb]# git add .
[root@mystical ~/project/ginweb]# git commit -m'update'
[master ab22ba5] update
 1 file changed, 2 insertions(+), 2 deletions(-)

```

![image-20250222100121501](../markdown_img/image-20250222100121501.png)

##### 相关脚本

```bash
[root@mystical /data/jenkins/script]# cat ginweb.sh 
#!/bin/bash

APP=ginweb
APP_PATH=/data
DATE=`date +%F_%H-%M-%S`
HOST_LIST="
172.22.200.101
172.22.200.102
"

build() {
    export GOCACHE="/var/lib/jenkins/.cache/go-build"
    export GOPATH="/var/lib/jenkins/go"
    export GOPROXY="https://goproxy.cn,direct"
    CGO_ENABLED=0 go build -o ${APP}
}

deploy() {
    for host in $HOST_LIST;do
	    ssh root@$host "mkdir -p $APP_PATH/${APP}-${DATE}"
	    scp -r * root@$host:$APP_PATH/${APP}-${DATE}/
	    ssh root@$host "killall -0 ${APP} &> /dev/null && killall -9 ${APP}; rm -rf ${APP_PATH}/${APP} && \
		ln -s ${APP_PATH}/${APP}-${DATE} ${APP_PATH}/${APP}; \
		cd ${APP_PATH}/${APP}/ && nohup ./${APP}&>/dev/null" &
    done
}

build
deploy
```



##### 创建 Jenkins 自由风格的任务

![image-20250222101223993](../markdown_img/image-20250222101223993.png)

![image-20250222101342798](../markdown_img/image-20250222101342798.png)

![image-20250222101352413](../markdown_img/image-20250222101352413.png)

![image-20250222101411136](../markdown_img/image-20250222101411136.png)



![image-20250222102425510](../markdown_img/image-20250222102425510.png)

![image-20250222103225178](../markdown_img/image-20250222103225178.png)





#### 集成 Ansible 的任务构建

![image-20250222103330422](../markdown_img/image-20250222103330422.png)



##### 安装 Ansible 环境

```bash
[root@mystical ~]# wget https://www.mysticalrecluse.com/script/Shell/install_ansible.sh
[root@mystical ~]# bash install_ansible.sh 

# 准备主机清单文件
[root@mystical ~]# cat /etc/ansible/hosts
[webservers]
172.22.200.101 ansible_ssh_user=root

[appservers]
172.22.200.102 ansible_ssh_user=root

# 因为Jenkins服务是以jenkins用户身份运行，所以需要实现Jenkins用户到被控制端的免密码验证
[root@jenkins ~]#su - jenkins
jenkins@jenkins:~$ ssh-keygen
jenkins@jenkins:~$ ssh-copy-id root@10.0.0.202
jenkins@jenkins:~$ ssh-copy-id root@10.0.0.203

# 连接测试
[root@mystical ~]# su - jenkins
jenkins@mystical:~$ ansible all -u root -m ping
172.22.200.102 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
172.22.200.101 | SUCCESS => {
    "changed": false,
    "ping": "pong"
```



##### 安装 Ansible 插件（可能需要科学）

![image-20250222104213568](../markdown_img/image-20250222104213568.png)

安装插件后，添加了ansible的构建步骤

![image-20250222104602641](../markdown_img/image-20250222104602641.png)

##### 使用 Ansible Ad-Hoc 实现任务

![image-20250222105143430](../markdown_img/image-20250222105143430.png)



**查看结果**

```bash
# 在172.22.200.101上查看结果
[root@mystical /tmp] $cat /tmp/hello.txt 
hello
```



##### 使用 Ansible Playbook 实现任务

###### **准备 Playbook文件**

```bash
[root@mystical /data/jenkins/ansible]# cat test.yaml 
- hosts: webservers
  remote_user: root

  tasks:
  - name: excute cmd
    shell:
      cmd: hostname -I
    register: result

  - name: show result
    debug:
      msg: "{{ result }}"
```



###### 创建任务

![image-20250222112353806](../markdown_img/image-20250222112353806.png)



**保存构建后**

![image-20250222112422185](../markdown_img/image-20250222112422185.png)



#####  使用 Ansible Playbook 基于参数化实现任务测试和生产多套 不同环境的部署

上面的任务是固定的,不灵活,利用参数在同一个任务就可以灵活实现测试和生产多套不同环境的部署



###### 准备playbook文件

```bash
[root@mystical /data/jenkins/ansible]# cat test.yaml 
- hosts: webservers
  remote_user: root

  tasks:
  - name: excute cmd
    shell:
      cmd: hostname -I
    register: result

  - name: show result
    debug:
      msg: "{{ result }}"
```

###### 准备两个不同环境的主机清单文件

```bash
[root@mystical /etc/ansible]# cat hosts_test 
[webservers]
172.22.200.101
[root@mystical /etc/ansible]# cat hosts_product 
[webservers]
172.22.200.102
```

###### 创建参数化任务

![image-20250222130005269](../markdown_img/image-20250222130005269.png)

![image-20250222130242957](../markdown_img/image-20250222130242957.png)

![image-20250222130030705](../markdown_img/image-20250222130030705.png)

![image-20250222130816616](../markdown_img/image-20250222130816616.png)



##### 使用 Ansible Playbook 实现向 Playbook 中传参功能

###### 编写Playbook文件

```bash
[root@mystical /data/jenkins/ansible]# cat test-vars.yaml 
- hosts: "{{ ansible_hosts }}"
  remote_user: root

  tasks:
  - name: excute cmd
    shell:
      cmd: hostname -I
    register: result

  - name: show result
    debug:
      msg: "{{ result }}"
```

###### 创建主机清单文件

```bash
[root@mystical /data/jenkins/ansible]# cat /etc/ansible/hosts_test 
[webservers]
172.22.200.101

[appservers]
172.22.200.102

[root@mystical /data/jenkins/ansible]# cat /etc/ansible/hosts_product 
[webservers]
172.22.200.222

[webservers]
172.22.200.111
```

###### 创建 Ansible Playbook 的任务

**创建任务,添加第一个选项参数**

![image-20250222133953392](../markdown_img/image-20250222133953392.png)

**添加第二个选项参数**

![image-20250222134023497](../markdown_img/image-20250222134023497.png)

![image-20250222134253048](../markdown_img/image-20250222134253048.png)

**点"高级"添加ansible的变量,添加Ansible Playbook的变量**

![image-20250222134411643](../markdown_img/image-20250222134411643.png)

![image-20250222134558674](../markdown_img/image-20250222134558674.png)

- key 是 ansible里定义的变量名
- Value 是 Jenkins 里的变量名
- 然后通过选项可以指定value的值

![image-20250222135414424](../markdown_img/image-20250222135414424.png)

![image-20250222135350536](../markdown_img/image-20250222135350536.png)





#### 构建后通知

Jenkins通知可以将任务的执行状态、事件或信息推送给相关用户，这些通常发生在pipeline的“构建后处理(post-processing)”时期

Email是 Jenkins 内置支持的通知方式，它也能够通过 webhook 扩展支持其它的即时通信媒介，例如:钉钉,Slack等



##### 使用 mailer 实现邮件通知

Mailer 和 Email Extension 插件都可以实现邮件通知功能

###### 准备告警邮箱配置

生成邮箱登录授权码，可以使用QQ或163邮箱等

###### mailer 插件实现邮件告警

**安装mailer插件**

先安装mailer插件后才可以显示和配置发件配置信息

注意: 安装 Gitlab插件会因为依赖关系自动安装mailer插件

![image-20250222141016139](../markdown_img/image-20250222141016139.png)

**配置 Jenkins管理员邮箱**

```ABAP
注意:必须指定系统管理员邮件地址才能实现邮件通知
```

Jenkins—系统管理—系统设置

```ABAP
注意：系统管理员邮件地址，必须和下面SMTP的用户名相同
注意:必须安装插件才能出现下面的SMTP配置
```

配置邮件通知信息如下:

- 用户名必须要和上面的系统管理员邮件地址相同
- 用户默认邮件后缀，可为空
- 启用"使用SSL协议"
- SMTP 端口可以为空,默认为465
- Reply-To Address 可以为空

![image-20250222141544314](../markdown_img/image-20250222141544314.png)

![image-20250222141959867](../markdown_img/image-20250222141959867.png)



###### 配置任务的构建后通知

```ABAP
注意:Jenkins-2.426.2选中和不选中效果一样
```

选中“每次不稳定的构建都发送邮件通知”，表示只有失败构建时才会发邮件通知

如果不选中，表示当失败或者从失败变为成功切换时都会通知，但总是成功不会通知

Recipients 支持多个收信人的邮件地址，空格隔开即可

![image-20250222142436740](../markdown_img/image-20250222142436740.png)

![image-20250222142405512](../markdown_img/image-20250222142405512.png)

###### 执行任务验证结果

默认“每次不稳定的构建都发送邮件通知”选中，表示当任务执行失败时才会收邮件

不选中”每次不稳定的构建都发送邮件通知“，表示当失败或者从失败变为成功切换时都会通知，但总是 成功不会通知

![image-20250222142609139](../markdown_img/image-20250222142609139.png)

![image-20250222142745234](../markdown_img/image-20250222142745234.png)





##### 使用 Email Extension 插件实现邮件通知

Email Extension 插件比Mailer插件的功能更加丰富

说明

```http
https://www.jenkins.io/doc/pipeline/steps/email-ext/#emailext-extended-email
https://plugins.jenkins.io/email-ext
```

######  安装插件 Email Extension

![image-20250222143038988](../markdown_img/image-20250222143038988.png)

###### 配置 Email Extension

系统管理-- 系统配置 -- Jenkins Location -- 系统管理员邮件地址

```ABAP
注意：此处必须配置发件人邮箱和下面Extended E-mail Notification 的一致
```

![image-20250222143959169](../markdown_img/image-20250222143959169.png)

**添加认证**

![image-20250222144241480](../markdown_img/image-20250222144241480.png)



![image-20250222144355710](../markdown_img/image-20250222144355710.png)

**设置各种邮件通知的触发器条件**

![image-20250222144551934](../markdown_img/image-20250222144551934.png)

![image-20250222144632526](../markdown_img/image-20250222144632526.png)

###### 在任务中使用邮件通知

**在构建后操作选择**

![image-20250222144807957](../markdown_img/image-20250222144807957.png)

**![image-20250222144952098](../markdown_img/image-20250222144952098.png)**

**默认只有失败才会发送通知，修改为总是发送给收件人Always**

![image-20250222145209521](../markdown_img/image-20250222145209521.png)

![image-20250222145257796](../markdown_img/image-20250222145257796.png)

**执行构建后，收到邮件**

![image-20250222145338071](../markdown_img/image-20250222145338071.png)





#### 自动化构建

- **周期性定时构建**
- **Webhook 触发构建**



##### 定时和 SCM 构建

周期性构建这是—-种基于 cron 类型的构建机制．按照预定义的时间周期性启动作务

对于期望能够基于代码变更进行触的CI场景来说，周期性构建并非其最佳选项，但对于有些类型的住务,它却也能够**通过精心编排的周期性构建来避免资源冲突**;



周期性构建分为**定时构建**和**轮询构建**

- **定时构建**: 按时间周期性的触发构建
- **轮询SCM(Source Code Management):**  指的是定期到代码仓库检查代码是否有变更，存在代码变更时就运行pipeline;为了能够从CI中得到更多的收益，轮询操作越频繁越好;显然，这会给SCM带去无谓的压力,所以构建的触发由SCM负责通知Jenkins最为理想;但在外部的SCM无法通知到局域网中的Jenkins时，可以采轮询SCM方式倒也不失为一种选择



**Jenkins cron语法遵循Unix cron语法的定义,但在细节上略有差别**

一项cron的定义包含由空白字符或Tab分隔的5个字段，用于定义周期性的时间点

H 符号可用于任何字段,且它能够在一个时间范围内对项目名称进行散列值计算出一个唯一的偏移量，以避免所有配置相同cron值的项目在同一时间启动;比如:**triggers { cron(H(0,30)) }**，表示每小时的前半小 时的某一分钟进行构建



###### 关于Jenkins Cron 语法中 H 用法详解

在 **Jenkins 的 Pipeline 或定时任务** (**Build periodically** or **Poll SCM**) 里，**H** 代表 **哈希散列（Hash-based）** 时间调度，而 **不是固定的数字**。

它的作用是**自动计算一个分布均匀的时间点**，以 **避免多个任务同时触发，导致服务器高负载**。



**H 的作用**

- 让 Jenkins 自动计算一个任务执行时间
- 基于 Job 名称的 Hash 值生成随机时间
- 避免所有任务在同一时间点执行



**H 的用法示例**

**✅ 1. `H * * * *`（每小时执行一次，但具体时间随机）**

```bash
H * * * *   # Jenkins 会在 0-59 之间随机选择一个固定的分钟数，每次触发都在相同的分钟数执行（对同一任务而言）。

# Jenkins 自动分配一个分钟数（0-59 之间），确保任务不会集中在同一时刻执行。
```

例如：某个 Job 可能被分配到 `23` 分钟，则它每小时执行一次，时间可能是：

```bash
10:23, 11:23, 12:23, 13:23, 14:23 ...
```

✅ **2. `H H(0-7) * * *`（每天凌晨 0-7 点某个时间运行一次）**

```bash
H H(0-7) * * *  # 例如可能是 02:34、05:21、06:45

# Jenkins 会在 0-7 小时之间选择一个固定时间，保证不同任务不会全部集中在 00:00。
```

✅ **3. `H/15 * * * *`（每 15 分钟执行一次）**

```bash
H/15 * * * *  # 例如可能是 07,22,37,52 分钟执行

# 避免所有任务固定在 00,15,30,45 分钟执行，减少服务器负载高峰
```

✅ **4. `H(0-30) 12 * * *`（每天 12:00-12:30 之间执行）**

```bash
H(0-30) 12 * * *  # 例如可能是 12:07、12:19、12:26

# 确保任务在 12:00-12:30 之间随机选择一个时间点
```



###### 定时构建示例

![image-20250222151941655](../markdown_img/image-20250222151941655.png)



![image-20250222152043085](../markdown_img/image-20250222152043085.png)

```ABAP
注意：SCM任务会在左侧多出一个“Git 轮询日志”，可以看到轮询的记录信息
观察Git 轮询日志可以看到当有变化时才会构建,否则不会执行构建
```

![image-20250222152228871](../markdown_img/image-20250222152228871.png)





##### 构建 Webhook 触发器

构建触发器(webhook)，也称为钩子，**实际上是一个HTTP回调**，其用于在开发人员向gitlab提交代码后 能够触发jenkins自动执行代码构建操作。

**常见场景:**

只有在开发人员向develop分支提交代码的时候会自动触发代码构建和部署至测试环境，而向主分支提 交的代码不会自动构建，需要运维人员手动部署代码到生产环境。

![image-20250222152502473](../markdown_img/image-20250222152502473.png)

**多种方式实现 Webhook 触发构建**

- 触发远程构建: 此方式无需安装插件
- Build when a change is pushed to GitLab. GitLab webhook URL: 需要安装Gitlab插件
- Generic Webhook Trigger : 需要安装 Generic Webhook Trigger Plugin 插件



###### **触发远程构建**

Jenkins配置构建 Webhook 触发器

![image-20250222155325828](../markdown_img/image-20250222155325828.png)

这里的触发路径为

```bash
JENKINS_URL/job/trigger1-demo1/build?token=TOKEN_NAME 或者 /buildWithParameters?token=TOKEN_NAME

# 其中JENKINS_URL的值为http://172.22.200.222:8080/
# 所以拼出来的最终URL为

http://172.22.200.222:8080/job/trigger1-demo1/build?token=123456
```

![image-20250222155601674](../markdown_img/image-20250222155601674.png)

![image-20250222155348764](../markdown_img/image-20250222155348764.png)

保存后，访问`http://172.22.200.222:8080/job/trigger1-demo1/build?token=123456`

```bash
#如果执行正常，则无任何显示
[root@mystical /tmp]# curl http://172.22.200.222:8080/job/trigger1-demo1/build?token=12345

# 触发构建
```

```ABAP
注意：这里之所以直接成功，是因为测试的服务器和Jenkins所在服务器，打通了ssh验证
```



![image-20250222160244159](../markdown_img/image-20250222160244159.png)

  ```ABAP
  如果在没有和Jenkins进行任何验证的机器上执行curl http://172.22.200.222:8080/job/trigger1-demo1/build?token=12345
  则会报如下错误
  ```

```bash
[root@master1 ~]#curl http://172.22.200.222:8080/job/trigger1-demo1/build?token=12345
<html><head><meta http-equiv='refresh' content='1;url=/login?from=%2Fjob%2Ftrigger1-demo1%2Fbuild%3Ftoken%3D12345'/><script id='redirect' data-redirect-url='/login?from=%2Fjob%2Ftrigger1-demo1%2Fbuild%3Ftoken%3D12345' src='/static/44b48e24/scripts/redirect.js'></script></head><body style='background-color:white; color:white;'>
Authentication required
<!--
-->
</body></html> 

# 请求返回的 HTML 提示 Authentication required，说明 Jenkins 要求身份验证
```

**解决方案**

**方法1：使用 API Token 进行认证**

Jenkins **默认不允许匿名构建**，需要 **API Token** 进行身份认证。

1️⃣ 获取 API Token

创建一个自定义用户

![image-20250222161429574](../markdown_img/image-20250222161429574.png)



![image-20250222161444100](../markdown_img/image-20250222161444100.png)

![image-20250222161526818](../markdown_img/image-20250222161526818.png)

```bash
# 此时直接使用新创建的用户名密码，就能触发
[root@master1 ~]#curl http://mystical:123456@172.22.200.222:8080/job/trigger1-demo1/build?token=123456

# 但是账号密码直接触发并不安全，因此建议使用API token
```



**创建 API Token**

使用刚刚创建的新用户登录Jenkins

![image-20250222162230718](../markdown_img/image-20250222162230718.png)

![image-20250222162332664](../markdown_img/image-20250222162332664.png)

![image-20250222162345984](../markdown_img/image-20250222162345984.png)

![image-20250222162441576](../markdown_img/image-20250222162441576.png)

点击生成，得到一串随机的令牌

![image-20250222162529528](../markdown_img/image-20250222162529528.png)

后续即可使用该API Token进行访问

```bash
[root@master1 ~]#curl http://mystical:1128f339f008e400621c665a474c529973@172.22.200.222:8080/job/trigger1-demo1/build?token=123456
```



**GitLab 配置 Webhook**

以幸运大转盘的前端项目为准备环境，在上面配置远程构建

![image-20250222163707479](../markdown_img/image-20250222163707479.png)

在 GitLab 上配置 Webhook

![image-20250222163804202](../markdown_img/image-20250222163804202.png)

![image-20250222171422210](../markdown_img/image-20250222171422210.png)

**执行测试**

![image-20250222171457017](../markdown_img/image-20250222171457017.png)

```ABAP
添加webhook后，执行测试，会显示报错：Hook execution failed: URL is blocked: Requests to the local network are not allowed 

原因：Gitlab 需要打开外发请求，而默认是关闭的
```

![image-20250222171306327](../markdown_img/image-20250222171306327.png)

**手动打开外发请求**

![image-20250222170843855](../markdown_img/image-20250222170843855.png)

![image-20250222170947507](../markdown_img/image-20250222170947507.png)

**打开外发请求后，再执行测试**

![image-20250222171659375](../markdown_img/image-20250222171659375.png)

```bash
# 修改git仓库的代码，上传，并提交tag
[root@mystical ~/project/wheel_of_fortune] $vim index.html 
[root@mystical ~/project/wheel_of_fortune] $git add .
[root@mystical ~/project/wheel_of_fortune] $git commit -m'5w -> 8w'
[root@mystical ~/project/wheel_of_fortune] $git push origin master
[root@mystical ~/project/wheel_of_fortune] $git log --oneline 
50250e0 (HEAD -> master, origin/master, origin/HEAD) 5w -> 8w
865e96c (tag: v8.0) +5w
3880368 (tag: v7.0) 50w
1bd276e (tag: v6.0) +200w
75cbf7a (tag: v5.0) + 400w
39cc771 500w
5fdc3cd -300w,-500w
a03647f (tag: v4.0) change 3002
26551d6 (tag: v3.0) change 500w
46b0c7a (tag: v2.0) change 100w
730984d (tag: v1.0) 幸运大转盘演示demo
[root@mystical ~/project/wheel_of_fortune] $git tag v9.0 50250e0
[root@mystical ~/project/wheel_of_fortune] $git push --tags

# 提交tags即可触发构建
```

![image-20250222174525613](../markdown_img/image-20250222174525613.png)

![image-20250222174550740](../markdown_img/image-20250222174550740.png)





#### 构建前后多个项目关联自动触发任务执行

用于多个 Job 相互关联，需要同行执行多个job的场景,比如:如果job1后希望自动构建job2

**可以用两种方法实现**

- 在前面任务中利用构建后操作关联后续任务
- 在后面任务中利用构建触发器关联前面任务

```ABAP
注意：
上面两种方法,都需要在前面任务执行后才能自动关联执行后续任务
不要实现任务的环路，会导致死循环
```



##### 在前面任务里配置构建后操作

在先执行的任务中配置构建后操作实现

###### 创建构建后操作

在第一个要执行的任务,指定构建后操作,添加第二个任务

要构建的项目可以填写多个项目名，之间用逗号分隔即可



**创建3个job**

![image-20250222180103160](../markdown_img/image-20250222180103160.png)

![image-20250222180137405](../markdown_img/image-20250222180137405.png)

![image-20250222180157020](../markdown_img/image-20250222180157020.png)



**在 job1 配置构建后操作**

![image-20250222223134385](../markdown_img/image-20250222223134385.png)![image-20250222223205571](../markdown_img/image-20250222223205571.png)

![image-20250222223233455](../markdown_img/image-20250222223233455.png)



##### **在后面构建的任务里创建**

###### 在后续构建的任务里利用构建触发器实现

在后面的 job 配置如下

在构建触发器---Build after other project are built --- 关注的项目 --- 输入前面的 job,如果有多个job 用 逗号分隔

![image-20250222224326137](../markdown_img/image-20250222224326137.png)                                                                                                                                                                                                                                                                                                

![image-20250222224423262](../markdown_img/image-20250222224423262.png)

![image-20250222224657104](../markdown_img/image-20250222224657104.png)



#### Blue Ocean 插件实现可视化

![image-20250222224922418](../markdown_img/image-20250222224922418.png)

Blue Ocean 插件可以实现更加漂亮的可视化界面,并且可以对指定的步骤进行重启等操作



##### 安装 Blue Ocean 插件

注意: 安装完插件,需要重启Jenkins才能生效

![image-20250223132907470](../markdown_img/image-20250223132907470.png)

![image-20250223133616278](../markdown_img/image-20250223133616278.png)



![image-20250223133645332](../markdown_img/image-20250223133645332.png)

![image-20250223133711823](../markdown_img/image-20250223133711823.png)

![image-20250223133735240](../markdown_img/image-20250223133735240.png)





#### 实现容器化的 Docker 任务

##### Jenkins 支持 Docker 说明

![image-20250223133933079](../markdown_img/image-20250223133933079.png)



当前越来越多的组织以容器形式运行应用, 应用交付形式统一为**Container Image**

交付的Container Image由Registry存储和分发,应用以容器化形式由Docker，Kubernetes进行编排运行

jenkins的多款插件都能实现容器镜像Image构建和推送

- docker-build-step
- Docker
- CloudBees Docker Build and Publish
- **Docker Pipeline Plugin**：这个插件允许在Jenkins Pipeline中使用Docker来构建、发布和管理容 器。它提供了一组用于在Pipeline脚本中执行Docker相关操作的步骤。
- **Docker Slaves Plugin**：这个插件允许Jenkins使用Docker容器作为构建代理（agent）。它可以动态地启动和停止Docker容器来扩展Jenkins的构建能力



##### 案例： 实现自由风格任务实现 Docker 镜像制作并运行

###### 在harbor.mystical.org主机上安装Harbor

```ABAP
略
```

###### 在目标主机安装 Docker，并且信任harbor

```bash
# 在Jenkins主机及应用主机上安装Docker
[root@mystical ~]# apt update && apt -y install docker.io

# 配置docker/daemon.json
[root@mystical ~]# cat /etc/docker/daemon.json 
{
  "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"],
  "insecure-registries": ["harbor.mystical.org"]
}

# 重启docker
[root@mystical ~]# systemctl restart docker

# 在Jenkins主机上，将jenkins用户加入docker组
# 如果不加的话，默认使用jenkins的身份，访问socket文件，但是docker.sock的其它没有读写权限，所以权限不足
[root@mystical ~]# ll /var/run/docker.sock 
srw-rw---- 1 root docker 0 Feb 23 08:13 /var/run/docker.sock=

[root@mystical ~]# usermod -aG docker jenkins
[root@mystical ~]# id jenkins
uid=114(jenkins) gid=119(jenkins) groups=119(jenkins),120(docker)

# 需要重启Jenkins，上面的权限才能生效
[root@mystical ~]# systemctl restart jenkins

#在Jenkins主机用jenkins用户登录harbor
# Jenkins和应用服务器都要先登录Harbor
[root@mystical ~]# su - jenkins
jenkins@mystical:~$ docker login harbor.mystical.org -u admin -p 123456
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
WARNING! Your password will be stored unencrypted in /var/lib/jenkins/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
jenkins@mystical:~$ cat .docker/config.json 
{
	"auths": {
		"harbor.mystical.org": {
			"auth": "YWRtaW46MTIzNDU2"
		}
	}
}
```

###### 在 Gitlab 准备项目

![image-20250223163022686](../markdown_img/image-20250223163022686.png)

###### 在 Jenkins 创建自由风格任务

![image-20250223173110146](../markdown_img/image-20250223173110146.png)

![image-20250223163303219](../markdown_img/image-20250223163303219.png)

![image-20250223173127646](../markdown_img/image-20250223173127646.png)



###### 脚本示例

```bash
[root@mystical /data/jenkins/script]# cat spring-boot-hello-docker.sh 
#!/bin/bash

REGISTRY=172.22.200.223
PORT=8888

HOSTS="
172.22.200.101
172.22.200.102
"

mvn clean package -Dmaven.test.skip=true

docker build -t ${REGISTRY}/myk8s/myapp:$TAG .
docker push ${REGISTRY}/myk8s/myapp:$TAG

for i in $HOSTS; do
	ssh root@$i docker rm -f myapp
	ssh root@$i docker run -d -p ${PORT}:8888 --restart always --name myapp ${REGISTRY}/myk8s/myapp:$TAG
done
```

###### 执行任务

![image-20250223173254371](../markdown_img/image-20250223173254371.png)

![image-20250223173307915](../markdown_img/image-20250223173307915.png)

![image-20250223173322383](../markdown_img/image-20250223173322383.png)



##### 案例: 基于 Docker 插件实现自由风格任务实现 Docker 镜像 制作

![image-20250223173417986](../markdown_img/image-20250223173417986.png)

###### 安装插件 docker-build-step

![image-20250223174752040](../markdown_img/image-20250223174752040.png)

###### 在Jenkins 安装Docker并配置 Docker 插件

```bash
# 在Jenkins主机及应用主机上安装Docker
[root@mystical ~]# apt update && apt -y install docker.io

# 配置docker/daemon.json
[root@mystical ~]# cat /etc/docker/daemon.json 
{
  "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"],
  "insecure-registries": ["harbor.mystical.org"]
}

# 重启docker
[root@mystical ~]# systemctl restart docker

# 在Jenkins主机上，将jenkins用户加入docker组
# 如果不加的话，默认使用jenkins的身份，访问socket文件，但是docker.sock的其它没有读写权限，所以权限不足
[root@mystical ~]# ll /var/run/docker.sock 
srw-rw---- 1 root docker 0 Feb 23 08:13 /var/run/docker.sock=

[root@mystical ~]# usermod -aG docker jenkins
[root@mystical ~]# id jenkins
uid=114(jenkins) gid=119(jenkins) groups=119(jenkins),120(docker)

# 需要重启Jenkins，上面的权限才能生效
[root@mystical ~]# systemctl restart jenkins

#在Jenkins主机用jenkins用户登录harbor
# Jenkins和应用服务器都要先登录Harbor
[root@mystical ~]# su - jenkins
jenkins@mystical:~$ docker login harbor.mystical.org -u admin -p 123456
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
WARNING! Your password will be stored unencrypted in /var/lib/jenkins/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
jenkins@mystical:~$ cat .docker/config.json 
{
	"auths": {
		"harbor.mystical.org": {
			"auth": "YWRtaW46MTIzNDU2"
		}
	}
}
```

######  本地 Docker Engine

```ABAP
系统管理-- 系统配置 -- Docker Builder -- Docker URL (支持本地和远程)
```

```bash
#本地Docker Engine
unix:///var/run/docker.sock

# 注意：Jenkins-2.246.2 版本不支持sock文件，会出现下面错误提示，只支持：unix://localhost:2375 形式
unix://localhost:2375   

#远程Docker Engine
tcp://10.0.0.101:2375
```

![image-20250223175454021](../markdown_img/image-20250223175454021.png)

###### 在 Jenkins 创建连接 Harbor 的凭证

![image-20250223175853800](../markdown_img/image-20250223175853800.png)



![image-20250223175930893](../markdown_img/image-20250223175930893.png)

![image-20250223175940433](../markdown_img/image-20250223175940433.png)

![image-20250223180125307](../markdown_img/image-20250223180125307.png)

###### 创建自由风格的 spring-boot-helloworld 项目的任务

![image-20250223180245096](../markdown_img/image-20250223180245096.png)

![image-20250223180429539](../markdown_img/image-20250223180429539.png)



![image-20250223180635122](../markdown_img/image-20250223180635122.png)

![image-20250223180645491](../markdown_img/image-20250223180645491.png)



![image-20250223180906669](../markdown_img/image-20250223180906669.png)



![image-20250223181140733](../markdown_img/image-20250223181140733.png)

![image-20250223181559168](../markdown_img/image-20250223181559168.png)

![image-20250223205825975](../markdown_img/image-20250223205825975.png)





#### 集成 Kubernetes

```http
https://www.jenkins.io/doc/book/scaling/scaling-jenkins-on-kubernetes/
```

在部署在Kubernetes集群外的Jenkins中执行Kubernetes集群的管理任务有以下两种方式



##### 方法1: 基于 kubeconfig 实现

流程说明

- 在Jenkins服务器安装kubectl工具，可以通过复制kubectl 二进制程序文件到Jenkins服务器 的/usr/local/bin下实现

- 将Kubernetes集群中的master节点的上的/etc/kubernetes/admin.conf 复制到Jenkins服务器 ~jenkins/.kube/config
- 修改权限： chmod 644 ~jenkins/.kube/config
- 编写shell,调用kubectl apply -f 执行集群管理操作





#### 推送构建状态信息至GitLab

Jenkins也能将流水线上的构建状态结果通过Webhook推送至GitILab进行显示，这需要配置**GitLab  Connection**



##### 在Gitlab创建用户的Access Token

在GitLab上，以仓库所关联的**用户登录--编辑个人资料--访问令牌 --- 生成Access Token**，并选择可访问 的API





### Jenkins 高级功能

#### Jenkins 分布式

Jenkins 分布式即将 Jenkins 的任务进行分布式处理

##### Jenkins 分布式说明

![image-20250225094809066](../markdown_img/image-20250225094809066.png)

在众多 Job 的场景下，单台 Jenkins Master 同时执行代码 clone、编译、打包及构建，其性能可能会出现瓶颈从而会影响代码部署效率

Jenkins官方提供了 Jenkins 分布式构建，将众多job分散运行到不同的 Jenkins slave节点，大幅提高并行job的处理能力。除此之外,还可以针对不同的开发环境分配至不同的Slave实现编译部署

比如:Java程序分配至Slave1,Go程序的编译分配给Slave2,Nodejs程序分配给Slave3

在 Jenkins 2 中，节点是一个基础概念，代表了任何可以执行 Jenkins 任务的系统

采用 master/agent 架构，因而其节点可划分主节点(master)和代理节点(agent)两种类型,，代理节点也 被称为从节点(slave)

主节点负责提供UI、处理HTTP请求及管理构建环境等，而代理节点则主要负责执行构建任务

- **主节点Master/Controller**

  Jenkins的一个部署实例的核心控制系统，它能够完全访问所有Jenkins配置的选项和任务（job)列 表，而且，若不存在其他代理节点，主节点也是默认的任务执行节点

- **代理节点Slave/Agent**

  在早先版本的Jenkins中，代理节点 (agent)也被称为从节点(slave),它代表着所有的非主节点 这类节点由主节点管理，按需分配或指定执行特定的任务，例如不同的构建任务或测试脚本式流水线中,节点特指一个运行代理节点的系统,而在声明式流水线中,它则是分配的一个作为代理节点的特定节点

- **执行器（Executor)**

  简单来说，Executor只是节点或代理节点用于执行任务的一个糟位

Executor的数量定义了该节点可以执行的并发任务量，一个节点上可以有任务数量的糟位，但也允行管理员按节点资源定义合适的数量

在主节点将任务分配给特定节点时，该节点上必须有可用的Executor来立即执行该任务,否则、只能等到有空闲槽位可用



##### 节点标签 Label

Jenkins中的标签(tag)指的是节点上的标识符，而后可由pipeline中的agent指令等进行过滤和选择节点执行

当Agent节点较多时，基于方便管理的目的，通常应该给这些节点添加能够体现其某种特性或功能的标签，以便于在构建任务中能基于标签过滤出符合条件的agent来

一个 Agent 上可添加多个标签,一个标签也可以添加至多个 Agent, 可以在作业中通过标签表达式实现 Agent的过滤

标签名称不允许使用空白字符，也不允许使用标签表达式中预留的关键字，例如: !、&、|、<、>、) 和 （ 等

**常用的标签纬度有如下几个**

- 操作系统类型: Linux、Windows、MacOS
- 操作系统位数: 32bit、64bit
- 集成的工具链: jdk、Go、Python、Nodejs等

**标签表达式（label expressions）支持如下操作符**

- !expression：表达式条件取反

- a && b：表达式间“与” 关系

- a || b：表达式间“或” 关系

- a -> b：表示如果满足a表达式，则同时必须满足b表达式,但是如果不满足a,则不要求满足b,等同于 “!a || b“

  示例: linux -> x64，意味着，如果操作系统为linux，则它也必须是x64的系统环境，如果不是 linux，则无要求必须是x64

- a<->b：表示两个条件要么同时满足，要么同时都不满足，即等同于 “a && b || !a && !b”

- (expression)：表达式分组，常在需要改变操作符间的优先级顺序时使用



#####  Jenkins Master 与 Agent之间的通信方式

![image-20250225100627746](../markdown_img/image-20250225100627746.png)



- **Launch agent via SSH**

  - SSH连接, Agent端是SSH Server端

  - **此方式需要安装SSH Build Agents插件**

  - **方式1**

    - 在Jenkins Agent节点运行ssh服务,接收Master的远程连接
    - 在Controller端保存认证信息为Credential,可以口令认证和密钥认证
    - 运行者身份：普通用户jenkins，/home/jenkins/agent目录，作为Agent端的工作目录

    ```ABAP
    Controller ssh client --> Agent ssh server
    ```

  - **方式2**

    - 通过基于 jenkins/ssh-agent 镜像的容器运行
    - 此方式只支持密钥认证
    - 使用ssh-keygen生成一对密钥，并将公钥通过环境变量传递给 ssh-agent容器
    - 将私钥保存为 Jenkins上的凭据

- **Launch agent by connecting it to the controller**

  - 注意：此方式中文翻译为**通过 Java Web 启动代理**

  - 基于JNLP-HTTP 协议连接器实现

  - 在agent上以手动或系统服务的方式经由JNLP协议触发双向连接的建立

  - 要求：Controller端额外提供一个套接字以接收连接请求，默认使用tcp协议的**50000端口**，也支持使用随机端口（安全，可能会对服务端在防火墙开放该端口造成困扰），也可以使用websocket， 基于默认8080端口建立集群通信连接

    ```ABAP
    Controller jnlp server <-- Agent jnlp client 

- **Launch agent via execution of command on the controller**
  - 在Controller上远程运行命令启动Agent
  - 在Master 上以远程运行命令的方式启动Agent,需要ssh服务



##### Agent分类

Agent 可以分为静态和动态两种

- **静态Agent**

  - 固定的持续运行的Agent,即使没有任务,也需要启动Agent
  - 以daemon形式运行的Jenkins
  - 每个Agent可以存在多个Executor，具体的数量应该根据Agent所在主机的系统资源来设定
  - (1) Linux Jenkins (2) Windows Jenkins (3) Jenkins Container 方式
  - 注意：很多的构建步骤，有可能会通过运行shell命令进行，则必须要确保在Container内部有所调用的可用shell命令

- **动态Agent**

  按需动态创建和删除 Agent ,当无任务执行时,删除Agent

  可以基于Docker 和 Kubernetes 实现

  - Docker Plugin 
    - 在基于配置好的Docker Host上，按需要创建以容器方式运行的 Agent
    - 需要事先配置好容器模板
  - Kubernetes Plugin
    - 基于配置好的Kubernetes集群环境，按需要创建以Pod方式运行Agent，需要事先配置Pod模板
    - 由Controller按Job的运行需要临时创建Agent，Agent数量可以动态伸缩, 且Job运行结束后会 删除Agent
    - 可以把每个Agent视作一个动态的Executor
    - 依赖的环境：云，支持由Jenkins Controller通过API调用
    - 而 Jenkins 自身既可以部署在k8s上，也完全可以运行在k8s外



##### 基于 SSH 协议实现 Jenkins 分布式

![image-20250225105514984](../markdown_img/image-20250225105514984.png)

###### Slave 节点安装 Java 等环境确保和 Master 环境一致

```bash
# 准备两台agent服务器
# 172.22.200.224
# 172.22.200.225

# 配置hostname
[root@mystical ~]# hostnamectl set-hostname agent1
[root@mystical ~]# hostnamectl set-hostname agent2

```



###### Master节点安装插件

安装 **SSH Build Agents** 插件，实现 ssh 连接代理

![image-20250225112619786](../markdown_img/image-20250225112619786.png)



###### 添加 Master 访问 Slave 认证凭据

用于 Master 连接 Slave 节点的凭据

可以是用户密码的凭据,也可以配置Master节点到Slave节点SSH key 验证

以root 身份连接 Agent

如果已经实现ssh key 验证，下面可以不配置

![image-20250225112948156](../markdown_img/image-20250225112948156.png)

![image-20250225113016078](../markdown_img/image-20250225113016078.png)

![image-20250225113056030](../markdown_img/image-20250225113626670.png)

​		

###### 添加 Agent 节点

![image-20250225113800566](../markdown_img/image-20250225113800566.png)

![image-20250225113817218](../markdown_img/image-20250225113817218.png)

![image-20250225113847599](../markdown_img/image-20250225113847599.png)

![image-20250225114035874](D:\git_repository\cyber_security_learning\markdown_img\image-20250225114035874.png)

![image-20250225114501906](../markdown_img/image-20250225114501906.png)

**agent 创建失败**

![image-20250225114631657](../markdown_img/image-20250225114631657.png)

**查看原因**

![image-20250225114738113](../markdown_img/image-20250225114738113.png)

![image-20250225114746411](../markdown_img/image-20250225114746411.png)

通过日志可以看出，这里报错是因为，agent所在主机上没有安装java

```bash
# 注意：agent上安装的java版本和master上的java版本一致
[root@agent1 ~]# apt update && apt install -y openjdk-17-jdk
[root@agent2 ~]# apt update && apt install -y openjdk-17-jdk
```

重新连接一下agent

![image-20250225115402542](../markdown_img/image-20250225115402542.png)

**成功同步**

![image-20250225120030718](../markdown_img/image-20250225120030718.png)

查看 agent1上的进程，可以看到启用了一个 java 服务

```bash
[root@agent1 ~]# ps aux|grep java
root        6189  3.4  2.9 3619940 118364 ?      Ssl  04:00   0:03 java -jar remoting.jar -workDir /var/lib/jenkins -jar-cache /var/lib/jenkins/remoting/jarCache
```



###### 建立后续的其它节点

重复上面的过程,建立其它的从节点

**小技巧:** 可以将复制Slave1节点的/root/.ssh目录到Slave2,从而可以省略 Slave2到其它主机的 Ssh key验证过程

![image-20250225121438278](../markdown_img/image-20250225121438278.png)

![image-20250225121513853](../markdown_img/image-20250225121513853.png)

稍微更下配置和标签后，创建

![image-20250225121609219](../markdown_img/image-20250225121609219.png)

将全局安全配置中的Git Host Key Verification Configuration 选为 No verification，否则，agent 上的 ssh 初次连接 gitlab 会要求验证，要求输入yes。

![image-20250225132143105](../markdown_img/image-20250225132143105.png)

将脚本文件从 master 服务器拷贝到 agent 服务器上，路径建议一致

```bash
[root@mystical /data/jenkins/script]# scp spring-boot-helloworld.sh 172.22.200.224:/data/jenkis/script/
```



打通 agent 服务器和待部署的服务器的 ssh 验证并在 agent 上安装 mvn

```bash
[root@mystical /data/jenkins/script]# apt install -y maven
```





###### 测试 SSH Agent

创建一个 freestyle 风格的任务

![image-20250225130935891](../markdown_img/image-20250225130935891.png)



通过标签选择用来构建的 agent 节点

![image-20250225131142758](../markdown_img/image-20250225131150390.png)

![image-20250225131514543](../markdown_img/image-20250225131514543.png)

![image-20250225134157097](../markdown_img/image-20250225134157097.png)

![image-20250225135745320](../markdown_img/image-20250225135745320.png)

![image-20250225144853905](../markdown_img/image-20250225144853905.png)





##### 基于 JNLP 协议的 Java Web 启动代理

此方式无需安装插件，即可实现

###### 全局安全配置

使用随机端口

![image-20250225145552793](../markdown_img/image-20250225145552793.png)

或者指定为固定端口

![image-20250225145659642](../markdown_img/image-20250225145659642.png)



###### 创建代理Agent节点

![image-20250225145829581](../markdown_img/image-20250225145829581.png)

![](../markdown_img/image-20250225150157433.png)

![image-20250225150257221](../markdown_img/image-20250225150257221.png)

![image-20250225150337369](../markdown_img/image-20250225150337369.png)

**在 agent 执行**

```bash
[root@mystical ~] $cat agent.sh 
#!/bin/bash

curl -sO http://172.22.200.222:8080/jnlpJars/agent.jar

nohup java -jar agent.jar -url http://172.22.200.222:8080/ -secret 0b6331c711be920d01fb247872fd7a110225eaa90fb78a2dbbcaa92e793d6b36 -name "agent1-jnlp" -webSocket -workDir "/var/lib/jenkins" &>/dev/null &

[root@mystical ~] $bash agent.sh
```

```bash
# 查看连接情况
[root@agent1 ~]# ss -nt
State Recv-Q Send-Q            Local Address:Port               Peer Address:Port  Process 
ESTAB 0      52               172.22.200.224:22                 172.22.100.1:57059         
ESTAB 0      0       [::ffff:172.22.200.224]:37614   [::ffff:172.22.200.222]:8080 

# 可以看出连接的master的8080端口
# 原因是：-webSocket 让 Jenkins Agent 直接通过 HTTP/HTTPS 连接 到 http://172.22.200.222:8080/。
# 这意味着 不会使用 TCP 50000 端口，而是 HTTP 端口（8080） 进行 WebSocket 连接。

# 如果想要连接master的50000端口，可以去掉 -webSocket 选项，并确保 Master 已启用 JNLP 端口。
```

✅**后续的创建与构建任务与基于 ssh 协议实现 Jenkins 分布式相同**



##### 基于Docker 的动态Agent

###### 准备 Docker Engine 主机

准备一台新的主机，安装 Docker Engine 此主机上运行Agent容器

```bash
[root@ubuntu2204 ~]# apt update && apt -y install docker.io

#如果需要远程 Docker 连接,需要修配下面配置
[root@ubuntu2204 ~]#vim /lib/systemd/system/docker.service
[Service]
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375 --
containerd=/run/containerd/containerd.sock

# 重启服务
[root@agent1 ~]# systemctl daemon-reload 
[root@agent1 ~]# systemctl restart docker

# 查看
[root@agent1 ~]# ss -nlt
State     Recv-Q    Send-Q       Local Address:Port        Peer Address:Port    Process    
LISTEN    0         128                0.0.0.0:22               0.0.0.0:*                  
LISTEN    0         128              127.0.0.1:6010             0.0.0.0:*                  
LISTEN    0         4096         127.0.0.53%lo:53               0.0.0.0:*                  
LISTEN    0         4096             127.0.0.1:36127            0.0.0.0:*                  
LISTEN    0         128                   [::]:22                  [::]:*                  
LISTEN    0         4096                     *:2375                   *:*                  
LISTEN    0         128                  [::1]:6010                [::]:* 
```



###### Jenkins 上安装Docker插件

![image-20250225153235825](../markdown_img/image-20250225153235825.png)





###### 创建 Cloud

![image-20250225153542704](../markdown_img/image-20250225153542704.png)

![image-20250225153558551](../markdown_img/image-20250225153558551.png)

![image-20250225153652356](../markdown_img/image-20250225153652356.png)

###### Docker Cloud Details 配置指定连接Docker的方式

**远程方式**

![image-20250225154819035](../markdown_img/image-20250225154819035.png)



###### 添加 Docker Agent templates

![image-20250225155053687](../markdown_img/image-20250225155053687.png)

```bash
# 在agent上将官方的agent镜像拉下来，可能需要科学上网
[root@agent1 ~]# docker pull jenkins/inbound-agent:alpine-jdk11
```

![image-20250225155918739](../markdown_img/image-20250225155918739.png)

![image-20250225155955353](../markdown_img/image-20250225155955353.png)



###### 测试构建任务

![image-20250225160328457](../markdown_img/image-20250225160328457.png)

![image-20250225160511512](../markdown_img/image-20250225160511512.png)

![image-20250225160521762](../markdown_img/image-20250225160521762.png)

因为镜像中没有 mvn 工具，因此这里使用 echo 做测试

![image-20250225160840603](../markdown_img/image-20250225160840603.png)

![image-20250225162110851](../markdown_img/image-20250225162110851.png)

![image-20250225162121841](../markdown_img/image-20250225162121841.png)

构建任务结束后，刚创建的 agent 容器会释放掉

```ABAP
注意：master节点上java的版本必须和agent服务器上的镜像的java版本一致！！！
```

查看日志，在临时容器中运行的构建任务

![image-20250225162439065](../markdown_img/image-20250225162439065.png)





#### Jenkins 视图

视图可用于归档job进行分组显示，比如将一个业务的视图放在一个视图显示，安装完成插件之后将会有 一个+号用于创建视图，支持三种视图，其中列表视图使用较多。

![image-20250225175518295](../markdown_img/image-20250225175518295.png)



##### 列表视图

列表视图使用场景比较多，用于将同一个业务的job保存至一个列表视图进行分类管理，即不同业务的 job放在不同的列表视图中。

###### 创建新的视图

![image-20250225175518295](../markdown_img/image-20250225175518295.png)

![image-20250225180129210](../markdown_img/image-20250225180129210.png)

根据正则表达式筛选 job

![image-20250225180354561](../markdown_img/image-20250225180354561.png)

![image-20250225180416085](../markdown_img/image-20250225180416085.png)



##### Pipeline 视图

Pipeline 视图可以显示任务之间的上下游关系，而非Pipeline风格的任务

###### **安装 build pipeline 插件**

安装 build pipeline 插件，可以在原来“列表视图”和“我的视图”上面增加“Build Pipeline View”

![image-20250225181032403](../markdown_img/image-20250225181032403.png)

![image-20250225181204020](../markdown_img/image-20250225181204020.png)



###### **创建 pipeline 视图**

![image-20250225181531392](../markdown_img/image-20250225181531392.png)

![image-20250225181548405](../markdown_img/image-20250225181548405.png)

![image-20250225181723709](../markdown_img/image-20250225181723709.png)



![image-20250225181821639](../markdown_img/image-20250225181821639.png)



##### 我的视图

我的视图会显示当前账户有权限访问的job，因此需要提前划分好权限。

###### **创建我的视图**

创建后点保存，就会直接看到当前账户有权限的 job

![image-20250225182225582](../markdown_img/image-20250225182225582.png)

###### **最终状态**

![image-20250225182346033](D:\git_repository\cyber_security_learning\markdown_img\image-20250225182346033.png)





#### Jenkins 权限管理

默认 jenkins 用户可以执行所有操作和管理所有 job

为了更好的分层控制，可以实现基于角色的权限管理，先创建角色和用户，给角色授权，然后把用户管理到角色。

**查看默认的权限设置**

![image-20250225182718275](../markdown_img/image-20250225182718275.png)



##### 创建新用户

默认所有jenkins用户都具有管理权限

Jenkins—系统管理—管理用户— 新建用户

![image-20250225182949163](../markdown_img/image-20250225182949163.png)

![image-20250225183001303](../markdown_img/image-20250225183001303.png)

![image-20250225183120371](../markdown_img/image-20250225183120371.png)



##### 安装角色权限相关的插件

搜索 **Role-based Authorization Strategy** 可以找到下面插件

![image-20250225183301564](../markdown_img/image-20250225183301564.png)

##### 更改认证方式

Jenkins—系统管理—全局安全配置 

默认创建的用户登录后可以做任何操作，取决于默认的认证授权方式。将其更改为**Role-Based Strategy**

![image-20250225183542060](../markdown_img/image-20250225183542060.png)

更改为 Role-Based Strategy 之后，zhangyifeng 这个账号在没有授权前，无任何权限

![image-20250225183919201](../markdown_img/image-20250225183919201.png)



##### 创建全局角色

Jenkins—系统管理--Manage and Assign Roles

![image-20250225183722239](../markdown_img/image-20250225183722239.png)



###### 添加一个只读权限的角色

![image-20250225184303747](../markdown_img/image-20250225184303747.png)

##### 将用户关联到全局角色

![image-20250225184430237](../markdown_img/image-20250225184430237.png)

![image-20250225184805684](../markdown_img/image-20250225184805684.png)

![image-20250225184819500](../markdown_img/image-20250225184819500.png)

![image-20250225184833071](../markdown_img/image-20250225184833071.png)

绑定权限后，查看 zhangyifeng 这个账号，具有了基本的读权限

![image-20250225184943179](../markdown_img/image-20250225184943179.png)





##### 创建项目(任务)角色

项目角色分配权限, 用于控制用户能看到哪些项目，并且有什么样的权限

项目角色使用pattern正则表达式,用于匹配相关的项目名称

比如: pattern 设为正则表达式`testproject.*` 表示所有`testproject`开头的job

![image-20250225185342406](../markdown_img/image-20250225185342406.png)

选择针对任务的权限，即用户可以对任务做怎样的操作

比如：用户只能对任务进行执行，但是不允许其修改任务

![image-20250225185605965](../markdown_img/image-20250225185605965.png)

为了让用户 zhangyifeng 只有指定 job 的读权限，因此，一定要将全局角色里的读权限取消

![image-20250225185914011](../markdown_img/image-20250225185914011.png)



将该项目角色与 zhangyifeng 这个账号绑定

![image-20250225185725767](../markdown_img/image-20250225185725767.png)

保存后，查看 zhangyifeng 用户的账号

![image-20250225185939072](../markdown_img/image-20250225185939072.png)



### Jenkins Pipeline

#### Pipeline 介绍

流水线生产，又叫流水生产流水作业，指劳动对象按一定的工艺路线和统一的生产速度，连续不断地通过各个工作地，按顺序地进行加工并生产出产品的一种生产组织形式。它是对象专业化组织形式的进一步发展，是劳动分工较细、生产效率较高的一种生产组织形式。亨利.福特(Henry Ford)于1913年在密歇根州的 Highland Park，建立的生产系统

![image-20250225191601613](../markdown_img/image-20250225191601613.png)

所谓的 Pipeline 流水线，其实就是将之前的一个任务或者一个脚本就做完的工作，用 Pipeline 语法划分 为多个子任务然后分别执行，两者实现的最终效果是一样的，但是由于原始任务划分为多个子任务之 后，以流水线的方式来执行，那么就可以随时查看任意子任务的执行效果，即使在某个阶段出现问题， 我们也可以随时直接定位问题的发生点，大大提高项目的效率,即模块化完成复杂任务的思想体现

Pipeline 是帮助 Jenkins 实现CI到CD转变的重要角色，是运行在 jenkins 2.X 版本的核心插件，简单来说 Pipeline就是一套运行于 Jenkins上的工作流框架，将原本独立运行于单个或者多个节点的任务连接起来，实现单个任务难以完成的复杂发布流程，从而实现单个任务很难实现的复杂流程编排和任务可视化

**官方帮助**

```http
https://www.jenkins.io/zh/doc/book/pipeline/
https://www.jenkins.io/doc/book/pipeline/
https://www.jenkins.io/2.0/
```

Pipeline基于**Groovy DSL(领域特定语言Domain Specific Language )**实现，任何发布流程都可以表述为 一段Groovy脚本。

Groovy是一种基于JVM虚拟机的敏捷开发语言，它结合了Python、Ruby和Smalltalk的许多强大的特性，Groovy 是用Java写的 , Groovy语法与Java语法类似

Groovy 代码不仅能够与 Java 代码很好地结合，也能用于扩展现有代码。由于其运行在 JVM 上的特性， Groovy也可以使用其他非Java语言编写的库

```http
Groovy官网:http://www.groovy-lang.org/learn.html
Groovy语法:http://groovy-lang.org/syntax.html
```



#### Pipeline 优势

![image-20250225191956307](../markdown_img/image-20250225191956307.png)

**一致性**: Pipeline 用统一语法的代码的方式实现各个CICD的阶段的任务，不仅可以被纳入版本控制，还 可以通过编辑代码实现目标效果

**直观性**: 构建过程中每一步都可以直接的图形化显示输出,比如每个阶段的执行时间,直观友好,pipeline  帮助我们快速的定位哪个阶段的任务出现错误

**可持续性**：Jenkins的重启或者中断后不影响已经执行的pipeline Job

**支持暂停**：Pipeline可以选择停止并等待人工输入或批准后再继续执行

**支持回放**: 如果失败,可以使用回放,进行临时性的修改 job ,再调试执行,如果成功,再真正修改任务即可

**可扩展**：通过Groovy的编程更容易的扩展插件

**并行执行**：通过Groovy脚本可以实现step，stage间的并行执行，和更复杂的相互依赖关系

**多功能**：支持复杂CD要求，包括fork/join子进程，条件判断，循环和并行执行工作的能力



#### Pipeline 语法

##### Pipeline 语法介绍和结构

官方文档

```http
https://www.jenkins.io/zh/doc/book/pipeline/syntax/
http://www.jenkins.io/doc/book/pipeline/syntax/
http://www.jenkins.io/doc/pipeline/steps/
#支持docker
https://www.jenkins.io/doc/book/pipeline/docker/
```

当前 Jenkins 2.X 支持两种语法的流水线： **脚本式（命令式）和声明式**

- **脚本式Scripted Pipeline语法**
  - 此语法是 Jenkins最先支持pipeline语法，采用命令式风格，直接在流水线脚本中定义逻辑和程序流程
- **声明式Declarative Pipeline语法**
  - 后来CloudBees公司为Jenkins引入的一种“流水线即代码”的pipeline语法
  - 它允许用户在pipeline的定义中将更多的精力关注于期望pipeline的状态和输出之上，而非实现逻辑

声明式和脚本化的流水线从根本上是不同的。 声明式流水线的是 Jenkins 流水线更新一些的特性:

- 相比脚本化的流水线语法，它提供更丰富的语法特性
- 是为了使编写和读取流水线代码更容易而设计的



##### Pipeline 的基本结构

📌 **pipeline**

流水线的**最外层结构**，代表整条pipeline，包含着pipeline的完整逻辑;是声明式流水线语法的关健特征

📌 **node 和 agent**

用于定义任务在哪里执行

每个node都是一个 Jenkins 节点，可以是 Jenkins master也可以是 Jenkins agent，node是执行 step的具体服务器。

node 代码块也是脚本式pipeline语法的关健特性,声明式pipeline使用 agent 关健字

📌 **stages**

用于包含所有stage的定义

📌 **stage**

属于 stages 的子语句块

指定 stage 的名称, 用于定义每个阶段 stage 的主要任务

一个pipeline可以划分为若干个stage，每个stage都是一个完整的操作，比如: clone代码、代码编 译、代码测试和代码部署，阶段是一个逻辑分组，可以跨多个node执行。

📌 **steps**

属于stage的子语句块

每个阶段stage中定义完成该阶段功能所需要经历的一系列步骤

步骤 steps 是jenkins pipeline最基本的操作单元，从在服务器创建目录到构建容器镜像，由各类 Jenkins 插件提供实现，例如： sh “make”

能够把这些步骤steps 同该stage中的其它定义（如环境的定义,Post 等）分隔开

📌 **post**

用在stage 代码块（和steps 同级）或整个pipeline执行完成后的附加步骤，此指令非必须项



##### 脚本式流水线语法

```http
https://www.jenkins.io/zh/doc/book/pipeline/
```

```groovy
node {
    stage('Source') {
        // git clone
    }
    stage('Build') {
        // mvn
    }
    stage('Test') {
        // mvn test
    }
    stage('Deploy') {
        // scp
        // java-jar
    }
}
# 特点：最外层是node {}
```



##### 声明式流水线语法

声明式流水线是在"Pipeline plugin"的2.5版本添加到 Jenkins 流水线的 ，它在流水线子系统之上提供了 一种更简单，更常见的语法。

所有有效的声明式流水线必须包含在一个 pipeline 块中, 比如:

```groovy
pipeline {
   /* insert Declarative Pipeline here */
}
```

官方说明

```http
https://www.jenkins.io/zh/doc/book/pipeline/syntax/
```

###### Pipeline 的基本结构

pipeline的定义有一个明确的、必须遵循的结构，它由一些directive和section组成，每一个section又可 包含其它的section、directive和step，以及一些condlition的定义

**Section**:用于将那些在某个时间点需要一同运行的条目(item）组织在一起

- **agent section**:指定负责运行代码的节点
  - 在pipeline代码块的顶部，必须要有一个agent来指定“默认”的执行节点
  - 而一个stage的顶部也可以有一个agent的定义，用来指定负责运行该stage中的代码的节点
- **stages section**:组织一到多个stage
- **steps section**:组织一至多个DSL格式的步骤
- **post section**:在stage或整个pipeline的尾部封装--些需要被执行的步骤或者检验条件

**Directive(指令)**︰负责完成特定功能的语句或代码块，如environment、tools、triggers、input和when 等

**Steps** : steps本身就是一个标识特定section的名称，其内部可以使用任何合法的DSL语句，例如git、 sh、 bat和echo等



###### Pipeline 的声明式语法要点

steps内部的命令，每一条单独的命令都在**当前任务的工作目录下执行**。

即使A命令切换到了一个新的目录，接下来的B命令并不会在对应的新目录中执行，而是在当前任务6的工作目录下执行。如果非要在切换后的目录下执行命令B，那么采用she11中的&&符号将多条命 令拼接在一起即可。

默认情况下，不支持shell里面的复杂语法，因为**groovy有自己的条件表达式**

如果jenkins的工作目录下存在同名目录，则获取失败

```groovy
pipeline {
    agent any 
    environment{
        url='http://www.wangxiaochun.com'
    }
    stages {
        stage('Source') {
            steps {
                // 
                echo "Access ${url}"
            }
        }
        stage('Build') { 
            steps {
                // 
            }
        }
        stage('Test') { 
            steps {
                // 
            }
        }
        stage('Deploy') { 
            steps {
                // 
            }
        }
    }
}
// 特点：最外层是 pipeline {} 
```



#### 生产级别的 Jenkins Pipeline 框架

一个 **生产级别（Production Ready）** 的 Jenkins Pipeline 应该包括：

**Job 配置（`properties([])`）**

- **参数化构建**
- **并发控制**
- **构建历史管理**
- **自动触发**

**Pipeline 主体**

- **Agent（Jenkins 节点调度）**
- **环境变量**
- **多个阶段（`stages`）**
- **错误处理（异常捕获）**
- **并行执行**
- **构建后操作（`post {}`）**



##### 生产级 Jenkins Pipeline 示例

```groovy
// 1️⃣ 【Job 配置】参数化构建 + 触发策略
properties([
    parameters([
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Git branch to build'),
        choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'], description: 'Deployment Environment'),
        booleanParam(name: 'SKIP_TESTS', defaultValue: false, description: 'Skip running tests')
    ]),
    disableConcurrentBuilds(), // 禁止并发执行
    buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '5')), // 仅保留最近 10 次构建
    pipelineTriggers([
        cron('H 12 * * 1-5') // 每天中午12点触发（周一到周五）
    ])
])

// 2️⃣ 【Pipeline 主体】
pipeline {
    // 【Agent 指定】动态分配 Agent
    agent { label params.DEPLOY_ENV == 'prod' ? 'prod-node' : 'dev-node' }

    // 【环境变量】
    environment {
        DOCKER_IMAGE = "my-app:${params.BRANCH_NAME}"
        WORKSPACE_DIR = "${env.WORKSPACE}"
    }

    // 3️⃣ 【Stages 阶段】
    stages {
        // 代码拉取
        stage('Checkout Code') {
            steps {
                script {
                    echo "Checking out branch: ${params.BRANCH_NAME}"
                    git branch: params.BRANCH_NAME, url: 'https://github.com/my-org/my-app.git'
                }
            }
        }

        // 并行编译 & 测试
        stage('Build & Test') {
            parallel {
                stage('Build') {
                    steps {
                        script {
                            sh 'mvn clean package -DskipTests=${params.SKIP_TESTS}'
                        }
                    }
                }
                stage('Unit Tests') {
                    when {
                        expression { return !params.SKIP_TESTS }
                    }
                    steps {
                        script {
                            sh 'mvn test'
                        }
                    }
                }
            }
        }

        // Docker 打包 & 推送
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }

        // 部署到目标环境
        stage('Deploy') {
            steps {
                script {
                    if (params.DEPLOY_ENV == 'prod') {
                        sh "kubectl apply -f k8s/prod-deployment.yaml"
                    } else {
                        sh "kubectl apply -f k8s/dev-deployment.yaml"
                    }
                }
            }
        }
    }

    // 4️⃣ 【后置处理】
    post {
        always {
            script {
                echo "Cleaning up workspace"
                cleanWs()  // 清理工作目录
            }
        }
        success {
            script {
                echo "Pipeline execution successful!"
            }
        }
        failure {
            script {
                echo "Pipeline execution failed! Sending alert..."
                sh 'curl -X POST -H "Content-Type: application/json" -d \'{"text": "Jenkins Build Failed!"}\' https://chat.mycompany.com/api/webhook'
            }
        }
    }
}
```



###### 代码详细解析

**1️⃣ `properties([])`（Job 配置）**

| 配置项                                | 作用                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| **`parameters([])`**                  | 允许用户选择 `BRANCH_NAME`（Git 分支）、`DEPLOY_ENV`（环境）、`SKIP_TESTS`（是否跳过测试） |
| **`disableConcurrentBuilds()`**       | 禁止同时运行多个相同 Job，防止资源冲突                       |
| **`buildDiscarder(logRotator(...))`** | 仅保留最近 10 次构建，节省 Jenkins 服务器存储                |
| **`pipelineTriggers([cron(...)])`**   | 每天 12:00 自动触发任务                                      |

------

**2️⃣ `pipeline {}`（Pipeline 主体）**

- **`agent { label params.DEPLOY_ENV == 'prod' ? 'prod-node' : 'dev-node' }`**
  - 动态选择 `prod-node`（生产环境）或 `dev-node`（开发环境）。
- **`environment {}`**
  - 设置环境变量，如 `DOCKER_IMAGE`（Docker 镜像名称）。

------

**3️⃣ `stages {}`（主要阶段）**

| 阶段                   | 作用                                            |
| ---------------------- | ----------------------------------------------- |
| **Checkout Code**      | 拉取 Git 代码，指定分支 `BRANCH_NAME`           |
| **Build & Test**       | 并行执行 `Maven` 构建和单元测试（可以跳过测试） |
| **Build Docker Image** | 构建并推送 Docker 镜像                          |
| **Deploy**             | 部署到 `Kubernetes`，区分 `dev/prod`            |

------

**4️⃣ `post {}`（后置处理）**

| 触发条件         | 处理                                                |
| ---------------- | --------------------------------------------------- |
| **`always {}`**  | **无论成功或失败，都执行** `cleanWs()` 清理工作目录 |
| **`success {}`** | **成功时打印 "Pipeline execution successful!"**     |
| **`failure {}`** | **失败时调用 Webhook 发送报警通知**                 |

------



##### **生产级别 Pipeline 设计要点**

1. **参数化构建**
   - 让用户选择 **分支、部署环境、测试选项**，增强灵活性。
2. **动态 Agent 选择**
   - **生产环境 & 开发环境** 使用不同的 Jenkins Agent。
3. **并行执行**
   - `Build` & `Test` **并行执行**，减少等待时间。
4. **自动触发**
   - `pipelineTriggers([cron('H 12 * * 1-5')])` **每天 12:00 触发**。
5. **构建后清理**
   - **清理工作目录**，避免磁盘空间不足。
6. **错误处理**
   - **失败时发送通知**，自动报警。







#### Pipeline 常见指令



##### properties([])  详解

在 **Jenkins Declarative Pipeline** 中，`properties([])` **用于设置 Job 的属性（Job Properties）**，包括：

- **参数化构建**（`parameters`）
- **触发策略**（`triggers`）
- **禁用并发执行**（`disableConcurrentBuilds`）
- **保留构建历史**（`buildDiscarder`）
- **流水线选项**（`pipelineTriggers`）



###### `properties([])` 用法扩展

1️⃣ **`parameters([])`：参数化构建**

**多个参数示例**

```groovy
properties([
    parameters([
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Git branch to build'),
        choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'], description: 'Deployment Environment'),
        booleanParam(name: 'SKIP_TESTS', defaultValue: false, description: 'Skip running tests')
    ])
])
```

📌 **作用**

- **`BRANCH_NAME`**：用户可以输入 Git 分支名，默认为 `main`
- **`DEPLOY_ENV`**：用户可以选择 `dev/staging/prod` 环境
- **`SKIP_TESTS`**：用户可以选择是否跳过测试

**2️⃣ `disableConcurrentBuilds()`：禁止并发执行**

```groovy
properties([
    disableConcurrentBuilds()
])
```

📌 **作用**

- **避免多个构建同时运行**
- 适用于 **资源敏感的 Job**，如部署任务

3️⃣ **`buildDiscarder()`：控制构建历史**

```groovy
properties([
    buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '5'))
])
```

📌 **作用**

- **仅保留最近 10 次构建记录**
- **仅保留最近 5 次构建的制品（Artifacts）**
- **节省 Jenkins 磁盘空间**

4️⃣ **`pipelineTriggers()`：自动触发构建**

```groovy
properties([
    pipelineTriggers([
        cron('H 12 * * 1-5') // 每天中午12点触发（周一到周五）
    ])
])
```

📌 **作用**

- **定时触发构建**
- `H 12 * * 1-5` 表示 **工作日（周一到周五）中午 12 点执行**



 **结合多个 `properties([])` 用法**

```groovy
properties([
    parameters([
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Git branch to build'),
        choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'], description: 'Deployment Environment')
    ]),
    disableConcurrentBuilds(),
    buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '5')),
    pipelineTriggers([
        cron('H 12 * * 1-5')
    ])
])
```



**结论**

| **功能**       | **用法**                    | **说明**              |
| -------------- | --------------------------- | --------------------- |
| **参数化构建** | `parameters([])`            | 允许用户输入参数      |
| **禁用并发**   | `disableConcurrentBuilds()` | 避免多个构建同时运行  |
| **保留历史**   | `buildDiscarder()`          | 控制 Jenkins 记录数量 |
| **定时构建**   | `pipelineTriggers([])`      | 使用 `cron` 触发构建  |

🚀 **`properties([])` 主要用于** **参数化构建、触发策略、并发控制、历史清理**，是 Jenkins 高级 CI/CD 任务的核心配置！ 🚀



##### Agent 用法详解

- **any**: 任何可用节点**（不推荐）**

- **none**: 用于pipeline顶端时表示不定义默认的agent，每个stage就需要单独指定

- **label { label ""}**: 具有指定的标签的节点均为可用节点

  ✅ **示例1：指定 Label 运行**

  ``` groovy
  pipeline {
      agent {
          label 'linux-agent'
      }
      stages {
          stage('Build') {
              steps {
                  echo 'Running on a specific agent with label: linux-agent'
              }
          }
      }
  }
  ```

  **📌 解释**

  - **`agent { label 'linux-agent' }`** ：表示 **Pipeline 只能在** `linux-agent` **这个 Label 的 Jenkins Agent 运行**。
  - **如果没有匹配的 Agent**，Jenkins 会等待**直到有符合 Label 的 Agent 可用**。

  ✅ **示例 2：动态分配 Label**

  1️⃣ **场景1：简单示例**

  ```groovy
  def myLabel = 'docker-node'
  
  pipeline {
      agent {
          label myLabel    // 直接写 myLabel，Jenkins 自动解析为 "docker-node"
      }
      stages {
          stage('Build') {
              steps {
                  echo "Running on agent: ${myLabel}"   // 这里用 ${myLabel} 是因为它在字符串中
              }
          }
      }
  }
  ```

  2️⃣ **场景 2：不同任务运行在不同环境**

  比如 **开发环境、测试环境、生产环境** 需要不同的 `Jenkins Agent`

  ```groovy
  def myLabel = env.BUILD_ENV == "prod" ? "prod-agent" : "dev-agent"
  
  pipeline {
      agent { label myLabel }
      stages {
          stage('Build') {
              steps {
                  echo "Running on agent: ${myLabel}"
              }
          }
      }
  }
  ```

  **📌 解释**

  - `env.BUILD_ENV` 是 Jenkins 环境变量，决定当前 Job 运行在哪个环境。
  - 如果 `BUILD_ENV=prod`，则 Job 运行在 `prod-agent`。
  - 如果 `BUILD_ENV=dev`，则 Job 运行在 `dev-agent`。

  3️⃣ **场景 3：多个 Agent 负载均衡**

  如果 Jenkins 有 **多个 `docker-node` Agent**，可以动态选择其中一个

  ```groovy
  def agents = ['docker-node-1', 'docker-node-2', 'docker-node-3']
  def myLabel = agents[new Random().nextInt(agents.size())]  // 随机选一个
  
  pipeline {
      agent { label myLabel }
      stages {
          stage('Build') {
              steps {
                  echo "Running on agent: ${myLabel}"
              }
          }
      }
  }
  ```

  **📌 解释**

  - **定义多个 Agent Label**，比如 `docker-node-1`, `docker-node-2`, `docker-node-3`。
  - **使用 `Random().nextInt(agents.size())` 随机选择一个 Agent** 进行构建，防止某个 Agent 负载过高。
  - 适用于 **并行构建、负载均衡调度任务**



###### agent { docker "image-name" } 详解

- **docker**:  在指定的容器中运行pipeline或stage代码，该容器动态创建并运行于预配置的可运行容器 的node上，或能够匹配到指定label的node上;可用参数如下 `image`、`label`、`args`、`rgistryUrl` 和 `rcgistryCredentialsId`

  📌 **`agent { docker "image-name" }` 详解**

  在 **Jenkins Declarative Pipeline** 中，`agent { docker "image-name" }` **表示在 Docker 容器内运行 Pipeline 任务**，而不是在物理/虚拟机的 Jenkins Agent 上执行。

  ✅ **适用于**

  - **隔离构建环境**（每次运行任务时使用干净的 Docker 容器）
  - **无需在 Jenkins Agent 上安装依赖**（如 Java、Maven、Node.js）
  - **支持动态拉取 Docker 镜像**（自动从 Docker Hub 或私有仓库拉取）

  **1️⃣ 基本用法**

  ```groovy
  pipeline {
      agent {
          docker 'maven:3.8.5' // 在 Maven Docker 容器中运行
      }
      stages {
          stage('Build') {
              steps {
                  sh 'mvn --version' // 运行 Maven 命令
              }
          }
      }
  }
  ```

  📌 **执行过程**

  1. **Jenkins 在 Agent 节点拉取 `maven:3.8.5` Docker 镜像**（如果本地不存在）。
  2. **在该 Docker 容器中运行所有 Pipeline 任务**。
  3. **执行 `mvn --version`，检查 Maven 版本**。
  4. **任务完成后，容器被销毁**

  2️⃣ **使用 `docker { image "..." args "-u root" }`**

  如果需要**修改容器用户或加参数**

  ```groovy
  pipeline {
      agent {
          docker { 
              image 'node:18' 
              args '-u root'  // 以 root 用户运行
          }
      }
      stages {
          stage('Node.js Version') {
              steps {
                  sh 'node -v'
              }
          }
      }
  }
  ```

  📌 **执行过程**

  - `image 'node:18'` → 运行 Node.js 18 的容器
  - `args '-u root'` → **确保容器以 `root` 用户运行**
  - `sh 'node -v'` → **在 Docker 容器内运行 `node -v`**

  3️⃣ **绑定宿主机目录**

  如果 Jenkins Agent 需要访问宿主机上的代码或目录

  ```groovy
  pipeline {
      agent {
          docker {
              image 'python:3.10'
              args '-v /var/lib/jenkins/workspace:/workspace'
          }
      }
      stages {
          stage('Run Python Script') {
              steps {
                  sh 'python /workspace/script.py'
              }
          }
      }
  }
  ```

  📌 **作用**

  - `-v /var/lib/jenkins/workspace:/workspace` → **挂载宿主机目录**
  - **容器内可访问 Jenkins `workspace` 目录**
  - **在容器里执行 `/workspace/script.py`**

  4️⃣ `**agent { docker { image "..." reuseNode true } }**`

  **默认情况下，每个 stage 运行完后，Jenkins 会销毁 Docker 容器。**
  如果希望 **整个 Pipeline 运行在同一个容器里**，可以使用 `reuseNode true`：

  ```groovy
  pipeline {
      agent {
          docker {
              image 'golang:1.19'
              reuseNode true  // 复用 Docker 容器
          }
      }
      stages {
          stage('Build') {
              steps {
                  sh 'go build -o myapp'
              }
          }
          stage('Test') {
              steps {
                  sh './myapp --test'
              }
          }
      }
  }
  ```

  📌 **作用**

  - `reuseNode true` **保证 `Build` 和 `Test` 阶段在同一个容器里运行**。
  - 如果没有 `reuseNode true`，`Test` 阶段会运行在新的容器里，导致 `Build` 生成的 `myapp` 文件丢失。

  5️⃣ **在 `dockerfile` 里构建镜像**

  如果 Jenkins **需要基于 `Dockerfile` 构建自定义镜像**：

  ```groovy
  pipeline {
      agent {
          dockerfile {
              filename 'Dockerfile'  // 指定 Dockerfile 文件
              dir 'docker'  // Dockerfile 目录
          }
      }
      stages {
          stage('Build') {
              steps {
                  sh 'echo "Running inside custom Docker image"'
              }
          }
      }
  }
  ```

  📌 **作用**

  - **Jenkins 先基于 `docker/Dockerfile` 构建镜像**
  - **然后使用该镜像运行 Pipeline**
  - 适用于 **项目需要自定义 Docker 环境的情况**

  **📌 `agent { docker "..." }` vs `agent any`**

  | 配置方式                       | 运行环境                             | 适用场景                                 |
  | ------------------------------ | ------------------------------------ | ---------------------------------------- |
  | **`agent any`**                | **直接运行在 Jenkins Agent 机器上**  | 适用于 **已有 Jenkins 环境，依赖已安装** |
  | **`agent { docker "image" }`** | **运行在指定 Docker 容器里**         | 适用于 **需要隔离环境，动态拉取依赖**    |
  | **`agent { dockerfile {} }`**  | **基于 `Dockerfile` 构建自定义环境** | 适用于 **自定义 CI/CD 运行环境**         |



###### `agent { kubernetes "" }` 详解

在 **Jenkins Pipeline** 中，`agent { kubernetes "" }` 用于在 Kubernetes 集群中 **动态分配 Jenkins Agent**，使得构建任务在 Kubernetes Pod 内执行，而不是直接在 Jenkins 主机或固定的 Agent 上。

1️⃣ **基本用法**

```groovy
pipeline {
    agent {
        kubernetes {
            yaml """
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: jnlp
                image: jenkins/inbound-agent:latest
                args: ['$(JENKINS_SECRET)', '$(JENKINS_NAME)']
              - name: builder
                image: maven:3.8.5
                command:
                - cat
                tty: true
            """
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
}
```

📌 **作用**

- **在 Kubernetes 内动态创建 Pod 作为 Jenkins Agent**
- `jnlp` 容器用于连接 Jenkins Master
- `builder` 容器（Maven）用于执行构建任务
- **任务完成后，Pod 自动销毁**

2️⃣ **`agent { kubernetes "" }` 主要参数**

| **参数**           | **作用**                                        |
| ------------------ | ----------------------------------------------- |
| `yaml`             | **定义 Kubernetes Pod 规格**，可以直接嵌入 YAML |
| `defaultContainer` | 指定默认运行构建任务的容器（非 `jnlp`）         |
| `inheritFrom`      | 继承已有的 Pod 模板                             |
| `customWorkspace`  | 设置工作目录                                    |
| `idleMinutes`      | Pod 任务完成后，等待多少分钟再销毁              |
| `serviceAccount`   | 运行 Pod 的 Kubernetes Service Account          |
| `cloud`            | 指定 Kubernetes Cloud 名称（Jenkins 配置中）    |

**3️⃣ 完整示例**

```groovy
pipeline {
    agent {
        kubernetes {
            yaml """
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                some-label: some-value
            spec:
              containers:
              - name: maven
                image: maven:3.8.5
                command: ['sleep']
                args: ['99d']
              - name: golang
                image: golang:1.19
                command: ['sleep']
                args: ['99d']
            """
            defaultContainer 'maven'
        }
    }
    stages {
        stage('Build Java') {
            steps {
                container('maven') {
                    sh 'mvn clean package'
                }
            }
        }
        stage('Build Go') {
            steps {
                container('golang') {
                    sh 'go build -o app'
                }
            }
        }
    }
}
```

📌 **作用**

- **Pod 里有多个容器（`maven`、`golang`）**
- **使用 `defaultContainer 'maven'`**，默认在 Maven 容器里执行
- **使用 `container('golang')` 指定在 Golang 容器里执行**

4️⃣ **`inheritFrom` 继承已有的 Pod 模板**

```groovy
pipeline {
    agent {
        kubernetes {
            inheritFrom 'maven-template'
        }
    }
    stages {
        stage('Compile') {
            steps {
                sh 'mvn clean compile'
            }
        }
    }
}
```

📌 **作用**

- **`inheritFrom 'maven-template'` 继承已有的 Pod 模板**
- **减少 YAML 配置重复**

5️⃣ **自定义工作目录**

```groovy
pipeline {
    agent {
        kubernetes {
            yaml """
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: nodejs
                image: node:18
                command: ['sleep']
                args: ['99d']
            """
            defaultContainer 'nodejs'
            customWorkspace '/home/jenkins/workspace'
        }
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }
    }
}
```

📌 **作用**

- **在 `nodejs` 容器里执行任务**
- **工作目录改为 `/home/jenkins/workspace`**

6️⃣ **设定 Pod 自动销毁时间**

```groovy
pipeline {
    agent {
        kubernetes {
            yaml """
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: builder
                image: ubuntu
                command: ['sleep']
                args: ['99d']
            """
            idleMinutes 2
        }
    }
    stages {
        stage('Run') {
            steps {
                sh 'echo "Building project"'
            }
        }
    }
}
```

📌 **作用**

- **Pod 任务完成后，等待 2 分钟再销毁**
- **适用于高频任务，减少 Pod 创建开销**

7️⃣ **使用 Service Account 运行 Pod**

```groovy
pipeline {
    agent {
        kubernetes {
            yaml """
            apiVersion: v1
            kind: Pod
            spec:
              serviceAccountName: jenkins-agent
              containers:
              - name: build
                image: ubuntu
                command: ['sleep']
                args: ['99d']
            """
        }
    }
    stages {
        stage('Run') {
            steps {
                sh 'whoami'
            }
        }
    }
}
```

📌 **作用**

- **`serviceAccountName: jenkins-agent` 指定 Service Account**
- **Pod 运行时拥有 K8s 访问权限**

8️⃣ **结合 `cloud` 指定 Kubernetes Cloud**

```groovy
pipeline {
    agent {
        kubernetes {
            cloud 'kubernetes'
            yaml """
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: builder
                image: ubuntu
                command: ['sleep']
                args: ['99d']
            """
        }
    }
    stages {
        stage('Run') {
            steps {
                sh 'echo "Building inside Kubernetes"'
            }
        }
    }
}
```

📌 **作用**

- **`cloud 'kubernetes'` 指定 Jenkins 配置的 K8s Cloud**
- **适用于多 Kubernetes 环境**



##### stages 和 stage 详细讲解

在 **Jenkins Pipeline** 中，`stages` 是一个 **包含多个 `stage` 的块**，而 `stage` 是 **具体的一个阶段**。通常 **`stages` 用于定义整个流水线的多个阶段，而 `stage` 用于描述流水线中的单个步骤**。

```ABAP
在一个 pipeline {} 块内，stages {} 只能出现一次！
```

###### 1️⃣`stages` 和 `stage` 的用法

 基本 `stages` 和 `stage` 示例

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building project..."'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying to production..."'
            }
        }
    }
}
```

📌 **解释**

- **`stages`** 里面包含了 **3 个 `stage`**
- **每个 `stage` 代表流水线的一个步骤**
- **按顺序执行：构建 → 测试 → 部署**

###### 2️⃣ `stage` 的高级用法

`stage` 中嵌套 `parallel`（并行执行）

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Tests') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'echo "Running unit tests..."'
                    }
                }
                stage('Integration Tests') {
                    steps {
                        sh 'echo "Running integration tests..."'
                    }
                }
            }
        }
    }
}
```

📌 **解释**

- **`stage('Parallel Tests')` 里使用 `parallel`**
- **`Unit Tests` 和 `Integration Tests` 并行执行**
- **适用于测试场景，提高执行速度**



##### stage 和 steps 详解

每个 `stage` **可以包含多个 `steps`**，但所有 `steps` 必须位于 **`steps {}` 代码块内**。**如果要执行多个 `steps`，只需在 `steps {}` 内写多个命令**。

```ABAP
多个steps指的是steps{ }这个代码块内有多个
Jenkins steps 是流水线的最小执行单元
```

###### **1️⃣ `stage` 里多个 `steps` 示例**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Step 1: Cleaning workspace..."
                sh 'rm -rf target/'
                
                echo "Step 2: Compiling source code..."
                sh 'mvn clean compile'
                
                echo "Step 3: Packaging..."
                sh 'mvn package'
            }
        }
    }
}
// 上述pipeline，共有6个steps
```

📌 **解释**

- **`echo` 和 `sh` 命令都是 `steps`**
- **多个 `steps` 可以连续执行**
- **Jenkins 依次执行：清理 → 编译 → 打包**

###### 2️⃣ `stage` 里包含多个 `steps` 和 `script`

**如果需要使用变量或者复杂逻辑，使用 `script {}`**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    def version = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    echo "Building version: ${version}"
                }
                sh 'mvn clean package'
            }
        }
    }
}
```

📌 **解释**

- **`script {}` 用于定义变量**
- **然后 `sh` 命令执行打包**

###### 3️⃣ `stage` 里多个 `steps` 并行执行

如果 **多个 `steps` 需要并行执行**，使用 `parallel`：

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Tests') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'echo Running unit tests...'
                        sh './run_unit_tests.sh'
                    }
                }
                stage('Integration Tests') {
                    steps {
                        sh 'echo Running integration tests...'
                        sh './run_integration_tests.sh'
                    }
                }
            }
        }
    }
}
```

📌 **解释**

- **`parallel {}` 使 `Unit Tests` 和 `Integration Tests` 并行执行**
- **适用于大规模测试，减少构建时间**

###### 4️⃣ `stage` 里多个 `steps` 结合 `when` 条件

**可以根据条件执行 `steps`**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}
```

📌 **解释**

- **如果是 `main` 分支，才执行 `Deploy`**
- **`when` 可以配合多个 `steps` 使用**

###### 5️⃣ `stage` 里多个 `steps` 结合 `retry`

如果某个 `steps` 可能失败，可以用 `retry`

```groovy
pipeline {
    agent any
    stages {
        stage('Download Dependencies') {
            steps {
                retry(3) {
                    sh 'mvn dependency:resolve'
                }
            }
        }
    }
}
```

📌 **解释**

- **如果 `mvn dependency:resolve` 失败，最多重试 3 次**

###### 6️⃣ 结论

✅ **`stage` 里可以包含多个 `steps`**
✅ **多个 `steps` 必须在 `steps {}` 里**
✅ **`script {}` 用于变量和复杂逻辑**
✅ **`parallel {}` 让多个 `stage` 并行**
✅ **`when {}` 让 `steps` 按条件执行**

🚀 **最终，`stage` 里可以有多个 `steps`，可以串行、并行、条件执行，满足各种 CI/CD 需求！** 🚀



##### post section 详解

在 **Jenkins Pipeline** 中，`post {}` 允许你在 **Pipeline 运行结束后执行额外的步骤**，比如：

- **发送通知**
- **清理工作空间**
- **存档构建产物**
- **在失败时触发回滚**

###### 1️⃣ `post {}` 的基本用法

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
    post {
        always {
            echo "Pipeline completed, executing cleanup steps..."
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
        unstable {
            echo "Pipeline is unstable!"
        }
        changed {
            echo "Pipeline status changed from previous run!"
        }
    }
}
```

📌 **解析**

- **`always {}`** → **无论成功/失败都会执行**
- **`success {}`** → **只在成功时执行**
- **`failure {}`** → **失败时执行**
- **`unstable {}`** → **测试失败但构建成功（不稳定状态）执行**
- **`changed {}`** → **如果当前运行结果与上次不同，则执行**

###### 2️⃣ `post {}` 主要选项

| **选项**   | **触发条件**                                       | **适用场景**               |
| ---------- | -------------------------------------------------- | -------------------------- |
| `always`   | **任何情况下**都会执行                             | **清理资源、记录日志**     |
| `success`  | **Pipeline 成功完成时**执行                        | **通知成功、存储构建产物** |
| `failure`  | **Pipeline 失败时**执行                            | **发送警报、回滚**         |
| `unstable` | **Pipeline 状态是 Unstable（测试失败但构建成功）** | **标记不稳定任务**         |
| `changed`  | **如果当前运行结果与上一次不同**                   | **通知变化，如失败后成功** |

###### 3️⃣ `post {}` 的高级用法

**`post {}` 发送通知**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
    post {
        failure {
            mail to: 'devops@example.com',
                 subject: "Jenkins Pipeline Failed: ${env.JOB_NAME}",
                 body: "Check the logs at ${env.BUILD_URL}"
        }
    }
}
```

📌 **作用**

- **如果 Pipeline 失败，发送邮件**
- **邮件内容包含 Job 名称和日志链接**

**`post {}` 清理工作空间**

```groovy
post {
    always {
        cleanWs() // 清理 Jenkins 工作目录
    }
}
```

📌 **作用**

- **无论成功还是失败，都删除工作目录**
- **避免磁盘占用过多**

**`post {}` 存档构建产物**

```groovy
post {
    success {
        archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
    }
}
```

 📌 **作用**

- **在构建成功时存档 `.jar`**
- **`fingerprint: true` 用于追踪构建产物**

**`post {}` 触发回滚**

```groovy
post {
    failure {
        sh 'kubectl rollout undo deployment my-app'
    }
}
```

**`post {}` 结合 `changed`（监测状态变化）**

```groovy
post {
    changed {
        echo "Pipeline result changed from previous run!"
    }
}
```

📌 **作用**

- **只有当本次构建状态与上次不同（如成功→失败）才执行**

###### 4️⃣ `post {}` 里的 `steps` 只能直接写命令

❌ **错误示例（`post {}` 里不能再写 `stages {}`）**

```groovy
post {
    always {
        stages {
            stage('Cleanup') { // ❌ 不能这样写
                steps {
                    sh 'rm -rf workspace/'
                }
            }
        }
    }
}
```

✅ **正确示例**

```groovy
post {
    always {
        sh 'rm -rf workspace/'
    }
}
```

📌 **解析**

- **`post {}` 里只能直接写 `steps {}` 或 `sh`**
- **不能再嵌套 `stages {}`**



##### Jenkins Pipeline支持常用指令

###### echo 命令

**输出信息**

```groovy
echo "Building"
```

###### sh 命令

`sh` 是 **Shell Script（Bash）执行器**，用于在 Linux 环境执行 Shell 命令。它是 `steps` 语法的一部分，在 **Declarative Pipeline 和 Scripted Pipeline** 中都可以使用。

**1️⃣ `sh` 命令的基本用法**

```groovy
pipeline {
    agent any
    stages {
        stage('Run Shell Command') {
            steps {
                sh 'echo "Hello, Jenkins!"'
            }
        }
    }
}
```

📌 **解析**

- **执行 Shell 命令 `echo "Hello, Jenkins!"`**
- **适用于 Linux 环境**
- **如果是 Windows 需要用 `bat '命令'`**

**2️⃣ `sh` 语法详解**

**🔹单行命令**

```groovy
sh 'ls -l'
```

📌 **作用**

- **执行 `ls -l`**
- **列出当前工作目录的文件**

**🔹 多行命令**

```groovy
sh '''
echo "Step 1: Cleaning workspace..."
rm -rf target/

echo "Step 2: Compiling source code..."
mvn clean compile

echo "Step 3: Packaging..."
mvn package
'''
```

📌 **作用**

- **使用 `'''`（三引号）编写多行 Shell 脚本**
- **每一行命令按顺序执行**

**🔹 sh 获取命令输出**

```groovy
pipeline {
    agent any
    stages {
        stage('Get Git Commit Hash') {
            steps {
                script {
                    def commit = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    echo "Latest Commit Hash: ${commit}"
                }
            }
        }
    }
}
```

📌 **作用**

- **`returnStdout: true` 获取 Shell 输出**
- **`trim()` 去除换行符**
- **`echo` 输出 Git 提交哈希**

**🔹 sh 获取命令执行状态**

```groovy
pipeline {
    agent any
    stages {
        stage('Check File Exists') {
            steps {
                script {
                    def status = sh(script: '[ -f /etc/passwd ]', returnStatus: true)
                    if (status == 0) {
                        echo "File exists!"
                    } else {
                        echo "File not found!"
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **`returnStatus: true` 获取 Shell 命令的退出码**
- **`status == 0` 代表命令成功**
- **适用于 `if` 语句判断**

**3️⃣ `sh` 执行外部脚本**

**🔹 运行外部 Shell 脚本**

```groovy
sh 'bash /path/to/script.sh'
```

📌 **作用**

- **执行 `/path/to/script.sh`**
- **适用于复杂逻辑脚本**

**🔹 运行 Python 脚本**

```groovy
sh 'python3 /path/to/script.py'
```

📌 **作用**

- **调用 Python 运行 `script.py`**
- **可以在 CI/CD 任务中使用**

**🔹 运行 Groovy 脚本**

```groovy
sh 'groovy /path/to/script.groovy'
```

📌 **作用**

- **执行 Groovy 脚本**
- **适用于 Jenkins 复杂逻辑**

**4️⃣ `sh` 的错误处理**

**🔹 失败时不中断 Pipeline**

```groovy
sh 'rm -rf /nonexistent/file || true'
```

📌 **作用**

- **如果 `rm` 命令失败，不会终止 Pipeline**
- **适用于非关键性任务**

**🔹 使用 `try-catch` 捕获错误**

```groovy
pipeline {
    agent any
    stages {
        stage('Safe Execution') {
            steps {
                script {
                    try {
                        sh 'exit 1' // 模拟失败
                    } catch (Exception e) {
                        echo "Command failed, but we handled it."
                    }
                }
            }
        }
    }
}
```

 **作用**

- **使用 `try-catch` 捕获 `sh` 执行错误**
- **避免 Pipeline 直接失败**

**5️⃣ `sh` 结合 `timeout`**

```groovy
timeout(time: 30, unit: 'SECONDS') {
    sh 'long_running_script.sh'
}
```

📌 **作用**

- **如果 `long_running_script.sh` 超过 30 秒没执行完，Jenkins 强制终止**
- **防止构建卡住**

**6️⃣ `sh` 结合 `retry`**

```groovy
retry(3) {
    sh 'curl -o data.txt http://example.com/file'
}
```

📌 **作用**

- **如果 `curl` 失败，最多重试 3 次**
- **适用于网络请求**

**7️⃣ `sh` 结合 `parallel`（并行执行）**

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Execution') {
            parallel {
                stage('Task 1') {
                    steps {
                        sh 'echo "Running task 1..."'
                    }
                }
                stage('Task 2') {
                    steps {
                        sh 'echo "Running task 2..."'
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **`sh` 命令在 `parallel` 里并行执行**
- **提高任务执行效率**

**8️⃣ `sh` 结合 `environment`**

```groovy
pipeline {
    agent any
    environment {
        API_KEY = '123456'
    }
    stages {
        stage('Use Environment Variable') {
            steps {
                sh 'echo "API_KEY is $API_KEY"'
            }
        }
    }
}
```

📌 **作用**

- **使用 `environment {}` 传递环境变量**
- **`sh` 里可以引用 `$API_KEY`**



###### sh 补充

`sh ''` 和 `sh(script: '')` **在功能上是等价的**，但 `sh(script: '')` 主要用于 **显示参数**，适用于**返回值处理和增强可读性**。

**1️⃣ `sh ''` 和 `sh(script: '')` 的区别**

| **写法**             | **是否等价** | **适用场景**                            |
| -------------------- | ------------ | --------------------------------------- |
| `sh '命令'`          | ✅ 等价       | **执行 Shell 命令**                     |
| `sh(script: '命令')` | ✅ 等价       | **适用于 returnStdout 和 returnStatus** |

✅ **示例**

```groovy
sh 'echo "Hello, Jenkins!"'   // ✅ 正常执行
sh(script: 'echo "Hello, Jenkins!"') // ✅ 等价，作用相同
```

**2️⃣ `sh(script: '命令')` 适用于返回值获取**

🔹`returnStdout: true` **获取命令输出**

✅ **标准写法**

```groovy
pipeline {
    agent any
    stages {
        stage('Get Git Commit Hash') {
            steps {
                script {
                    def commit = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    echo "Latest Commit Hash: ${commit}"
                }
            }
        }
    }
}
```

📌 **解析**

- **`sh(script: '命令', returnStdout: true)` 用于获取命令输出**
- **适用于 Shell 命令返回值处理**
- **`trim()` 去除换行符**

**🔹 `returnStatus: true` 获取命令执行状态**

✅ **示例**

```groovy
pipeline {
    agent any
    stages {
        stage('Check File Exists') {
            steps {
                script {
                    def status = sh(script: '[ -f /etc/passwd ]', returnStatus: true)
                    if (status == 0) {
                        echo "File exists!"
                    } else {
                        echo "File not found!"
                    }
                }
            }
        }
    }
}
```

📌 **解析**

- **`returnStatus: true` 返回 Shell 命令的退出码**
- **适用于 `if` 语句判断**

**3️⃣ 结论**

| **写法**                                 | **适用场景**            | **是否等价**                     |
| ---------------------------------------- | ----------------------- | -------------------------------- |
| `sh '命令'`                              | **直接执行 Shell 命令** | ✅ 等价                           |
| `sh(script: '命令')`                     | **增强可读性**          | ✅ 等价                           |
| `sh(script: '命令', returnStdout: true)` | **获取 Shell 输出**     | ❌ 不等价，`sh ''` 默认不返回值   |
| `sh(script: '命令', returnStatus: true)` | **获取 Shell 退出状态** | ❌ 不等价，`sh ''` 默认不返回状态 |

🚀 **最终：**

- **`sh ''` 和 `sh(script: '')` 是等价的**
- **但 `returnStdout` 和 `returnStatus` 只能在 `sh(script: '')` 中使用**
- **推荐使用 `sh(script: '')` 以增强可读性！** 🚀



###### git 命令

在 **Jenkins Pipeline** 中，`git` 命令用于 **拉取 Git 仓库的代码**，并且可以 **指定分支、凭据、Git URL** 以及 **管理 Submodules**。

**1️⃣ `git` 命令的基本用法**

**🔹 方式 1：最简单的 Git 拉取**

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/user/repository.git'
            }
        }
    }
}
```

📌 **作用**

- **拉取 Git 仓库** `https://github.com/user/repository.git`
- **默认拉取 `master` 分支**
- **适用于公开仓库**

**🔹 方式 2：指定分支**

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'dev', url: 'https://github.com/user/repository.git'
            }
        }
    }
}
```

📌 **作用**

- **拉取 `dev` 分支**
- **适用于多分支开发**

**2️⃣ `git` 命令的高级用法**

**🔹指定 Git 凭据（私有仓库）**

如果 **Git 仓库是私有的**，需要 **使用 Jenkins 的 Credentials（凭据管理）**

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout Private Repo') {
            steps {
                // git-credentials 是在jenkins里创建的凭证的名称，因此在使用前需要先在jenkins创建凭证
                git credentialsId: 'git-credentials', branch: 'main', url: 'git@github.com:user/repository.git'
            }
        }
    }
}
```

📌 **作用**

- **使用 Jenkins 存储的 `git-credentials` 登录 Git**
- **适用于 GitHub、GitLab、Bitbucket 私有仓库**
- **Git URL 需要使用 `SSH`（`git@github.com:user/repository.git`）或 `HTTPS`（`https://github.com/user/repository.git`）**

**🔹 checkout` 命令（更灵活）**

✅ **`checkout` 提供更多控制**

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    userRemoteConfigs: [[url: 'https://github.com/user/repository.git']]
                ])
            }
        }
    }
}
```

📌 **作用**

- **`checkout` 允许更灵活的 Git 选项**
- **适用于更复杂的 Git 操作**`

**3️⃣ `git` 结合 `pollSCM`（定时拉取）**

如果希望 **Jenkins 监听 Git 代码变更，并自动触发构建**：

```groovy
pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')  // 每 5 分钟检查一次 Git 是否有更新
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/user/repository.git'
            }
        }
    }
}
```

📌 **作用**

- **每 5 分钟检查 Git 是否有新代码**
- **如果有新代码，自动触发构建**

**4️⃣ `git` 结合 `webhook`（GitLab/GitHub 触发）**

Jenkins 也可以使用 **GitLab 或 GitHub Webhook** 自动触发：**

```groovy
pipeline {
    agent any
    triggers {
        gitlabPush()  // GitLab Webhook 触发
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://gitlab.com/user/repository.git'
            }
        }
    }
}
```

📌 **作用**

- **使用 `gitlabPush()` 监听 GitLab Webhook**
- **GitHub 需要使用 `Generic Webhook Plugin`**

**5️⃣ `git` 结合 `sh` 获取更多信息**

 🔹**获取当前 Git 分支**

```groovy
pipeline {
    agent any
    stages {
        stage('Get Branch') {
            steps {
                script {
                    def branch = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                    echo "Current Branch: ${branch}"
                }
            }
        }
    }
}

```

📌 **作用**

- **获取当前分支名称**
- **适用于动态判断分支**

**🔹 获取 Git 提交哈希**

```groovy
pipeline {
    agent any
    stages {
        stage('Get Commit Hash') {
            steps {
                script {
                    def commit = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    echo "Latest Commit: ${commit}"
                }
            }
        }
    }
}
```

📌 **作用**

- **获取最新提交哈希**
- **适用于版本管理**

**🔹 获取 Git 提交日志**

```groovy
pipeline {
    agent any
    stages {
        stage('Get Git Logs') {
            steps {
                script {
                    def logs = sh(script: 'git log -1 --pretty=format:"%h - %an: %s"', returnStdout: true).trim()
                    echo "Last Commit: ${logs}"
                }
            }
        }
    }
}
```

📌 **作用**

- **获取最近一次 Git 提交日志**
- **适用于自动生成 Release Notes**



###### trigger 命令

**1️⃣ `trigger` 的主要类型**

| **类型**             | **作用**              | **示例**                 |
| -------------------- | --------------------- | ------------------------ |
| **`pollSCM`**        | 监听 Git 代码变更     | `pollSCM('H/5 * * * *')` |
| **`cron`**           | 定时触发              | `cron('H 12 * * 1-5')`   |
| **`upstream`**       | 监听其他 Job 构建完成 | `upstream('JobA')`       |
| **`genericTrigger`** | 监听 Webhook 触发     | `genericTrigger(...)`    |

**2️⃣ `pollSCM`（基于 Git 变更触发）**

Jenkins **定期检查 Git 仓库是否有变更**，如果有新提交，自动触发构建。

```groovy
pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')  // 每 5 分钟检查一次 Git 是否有更新
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/user/repository.git'
            }
        }
    }
}
```

📌 **解析**

- **每 5 分钟检查 Git 是否有新代码**
- **适用于 CI/CD 持续集成**
- **但不会立即触发（存在一定延迟）**

**3️⃣ `cron`（定时构建）**

Jenkins **可以像 Linux `cron` 一样定时触发构建**

```groovy
pipeline {
    agent any
    triggers {
        cron('H 12 * * 1-5')  // 每周一到周五中午 12 点运行
    }
    stages {
        stage('Build') {
            steps {
                echo "Running scheduled build..."
            }
        }
    }
}
```

📌 **解析**

- **定时每天中午 12 点运行**
- **`H` 代表随机分配分钟，避免多个 Job 同时触发**
- **适用于夜间构建、定期清理任务**

**4️⃣ `upstream`（监听其他 Job 触发）**

Jenkins **可以在某个 Job 运行完成后，自动触发另一个 Job**。

```groovy
pipeline {
    agent any
    triggers {
        upstream('JobA')
    }
    stages {
        stage('Deploy') {
            steps {
                echo "Deploying after JobA finishes..."
            }
        }
    }
}
```

📌 **解析**

- **当 `JobA` 运行完成后，`JobB` 会被自动触发**
- **适用于多级流水线（如 Build → Deploy）**

**5️⃣ `genericTrigger`（监听 Webhook 触发）**

```ABAP
后续详解！！！
```



**6️⃣`genericTrigger` 结合 `curl` 测试**

```bash
curl -X POST http://JENKINS_URL/generic-webhook-trigger/invoke?token=mySecretToken \
     -H "Content-Type: application/json" \
     -d '{"ref": "refs/heads/main", "repository": {"full_name": "user/repository"}}'
```

📌 **作用**

- **模拟 GitLab / GitHub Webhook 触发**

**7️⃣`triggers` 总结**

| **触发方式**     | **适用场景**                      | **是否推荐** |
| ---------------- | --------------------------------- | ------------ |
| `pollSCM`        | **定期检查 Git 代码变更**         | ❌（有延迟）  |
| `cron`           | **定时构建**                      | ✅            |
| `upstream`       | **监听其他 Job**                  | ✅            |
| `genericTrigger` | **Webhook 触发（GitLab/GitHub）** | ✅✅✅          |



###### genericTrigger 详解

`genericTrigger` 是 **Jenkins Pipeline** 提供的一种 **Webhook 触发机制**，通常用于 **监听 GitLab、GitHub、Bitbucket Webhook** 或 **其他外部服务的 HTTP 事件**，在满足特定条件时触发 Jenkins 构建。

**1️⃣ `genericTrigger` 基本语法**

```groovy
pipeline {
    agent any
    triggers {
        genericTrigger(
            genericVariables: [
                [key: 'branch', value: '$.ref'],  
                [key: 'repository', value: '$.repository.full_name']
            ],
            token: 'mySecretToken',
            printContributedVariables: true,
            printPostContent: true
        )
    }
    stages {
        stage('Print Webhook Data') {
            steps {
                echo "Branch: ${env.branch}"
                echo "Repository: ${env.repository}"
            }
        }
    }
}
```

📌 **作用**

- **监听 Webhook 请求**
- **解析 Webhook JSON 数据**
- **存储 Webhook 变量（`branch`、`repository`）**
- **Jenkins 只在 Webhook 触发时运行**

**2️⃣ `genericTrigger` 主要参数**

| **参数**                    | **作用**                                     | **示例值**                      |
| --------------------------- | -------------------------------------------- | ------------------------------- |
| `token`                     | Webhook 认证令牌                             | `'mySecretToken'`               |
| `genericVariables`          | **Webhook JSON 解析变量**                    | `key: 'branch', value: '$.ref'` |
| `printContributedVariables` | **打印解析后的变量**                         | `true / false`                  |
| `printPostContent`          | **打印 Webhook 的原始 JSON**                 | `true / false`                  |
| `regexpFilterText`          | **定义过滤条件的原始文本**                   | `'$branchName'`                 |
| `regexpFilterExpression`    | **用于匹配 `regexpFilterText` 的正则表达式** | `'refs/heads/main'`             |
| `causeString`               | **构建原因描述**                             | `'Triggered by Webhook'`        |

**3️⃣ `genericTrigger` 参数详解**

**🔹 `token`（Webhook 认证令牌）**

```groovy
token: 'mySecretToken'
```

📌 **作用**

- **防止恶意 Webhook 请求**
- **GitLab/GitHub 需要在 Webhook 配置 `Secret Token`**
- **URL 示例**

```http
http://JENKINS_URL/generic-webhook-trigger/invoke?token=mySecretToken
```

**🔹 genericVariables`（解析 Webhook JSON）**

```groovy
genericVariables: [
    [key: 'branch', value: '$.ref'],  
    [key: 'repository', value: '$.repository.full_name']
]
```

📌 **作用**

- **解析 Webhook 的 JSON 数据**
- **`key` 是 Jenkins 环境变量名**
- **`value` 是 JSON 路径**
- **示例 Webhook JSON**

```bash
{
  "ref": "refs/heads/main",
  "repository": {
      "full_name": "user/repository"
  }
}
```

- **解析后**

```bash
env.branch = "refs/heads/main"
env.repository = "user/repository"
```

**🔹  `printContributedVariables`（打印 Webhook 变量）**

```groovy
printContributedVariables: true
```

📌 **作用**

- **构建时在 Jenkins Console 显示 `genericVariables` 解析出的变量**
- **用于调试 Webhook 变量**

**🔹  `printPostContent`（打印 Webhook 原始 JSON）**

```groovy
printPostContent: true
```

📌 **作用**

- **在 Jenkins Console 打印 Webhook 发送的原始 JSON**
- **适用于调试 Webhook**

**🔹 `regexpFilterText` 和 `regexpFilterExpression`（基于正则过滤 Webhook 事件）**

```groovy
regexpFilterText: '$branch',
regexpFilterExpression: 'refs/heads/main'
```

📌 **作用**

- **`regexpFilterText` 设定要匹配的文本**
- **`regexpFilterExpression` 设定正则匹配规则**
- **只有 `refs/heads/main` 触发构建，其他分支不触发**



**🔹 `causeString`（构建原因）**

```groovy
causeString: 'Triggered by Webhook from GitLab'
```

📌 **作用**

- **在 Jenkins 构建记录中显示触发原因**



**4️⃣ `genericTrigger` 高级示例**

🔹**监听 GitLab Webhook**

```groovy
pipeline {
    agent any
    triggers {
        genericTrigger(
            genericVariables: [
                [key: 'branch', value: '$.ref'],
                [key: 'commit_message', value: '$.commits[0].message'],
                [key: 'commit_author', value: '$.commits[0].author.name']
            ],
            token: 'myGitLabToken',
            printContributedVariables: true,
            printPostContent: true,
            regexpFilterText: '$branch',
            regexpFilterExpression: 'refs/heads/main'
        )
    }
    stages {
        stage('Checkout Code') {
            steps {
                echo "Branch: ${env.branch}"
                echo "Commit Message: ${env.commit_message}"
                echo "Commit Author: ${env.commit_author}"
                git branch: "${env.branch}", url: "https://gitlab.com/user/repository.git"
            }
        }
    }
}
```

📌 **作用**

- **监听 GitLab Webhook**
- **解析 `branch`、`commit_message`、`commit_author`**
- **只允许 `main` 分支触发构建**



**🔹 监听 GitHub Webhook**

```groovy
pipeline {
    agent any
    triggers {
        genericTrigger(
            genericVariables: [
                [key: 'branch', value: '$.ref'],
                [key: 'repo', value: '$.repository.full_name'],
                [key: 'pusher', value: '$.pusher.name']
            ],
            token: 'myGitHubToken',
            printContributedVariables: true,
            printPostContent: true
        )
    }
    stages {
        stage('Build') {
            steps {
                echo "Repository: ${env.repo}"
                echo "Branch: ${env.branch}"
                echo "Pushed by: ${env.pusher}"
            }
        }
    }
}
```

📌 **作用**

- **监听 GitHub Webhook**
- **解析 `branch`、`repo`、`pusher`**
- **适用于 CI/CD 触发**



**5️⃣ Webhook 配置**
**🔹 GitLab Webhook**

- **GitLab → 项目 → Settings → Webhooks**

- **URL**

```http
http://JENKINS_URL/generic-webhook-trigger/invoke?token=myGitLabToken
```

- **Secret Token**：`myGitLabToken`

- **触发事件**：选择 `Push events`

- **保存 Webhook**



**🔹 GitHub Webhook**

- **GitHub → Settings → Webhooks**
- **Payload URL**

```http
http://JENKINS_URL/generic-webhook-trigger/invoke?token=myGitHubToken
```

- **Content Type**：选择 `application/json`
- **触发事件**：选择 `Push event`
- **保存 Webhook**



###### environment 命令

在 **Jenkins Pipeline** 中，`environment {}` 用于 **定义环境变量**，这些变量可以在 **整个 Pipeline** 或 **单个 `stage`** 中使用。

- **可以设置静态变量**
- **可以访问 Jenkins `credentials()` 凭据**
- **可以通过 `sh`、`echo` 读取**

**1️⃣ `environment {}` 基本用法**

**🔹  全局环境变量（作用于整个 Pipeline）**

```groovy
pipeline {
    agent any
    environment {
        PROJECT_NAME = 'MyApp'
        BUILD_NUMBER = "${env.BUILD_ID}"  // 使用 Jenkins 预定义变量
    }
    stages {
        stage('Build') {
            steps {
                echo "Project: ${PROJECT_NAME}"
                echo "Build Number: ${BUILD_NUMBER}"
            }
        }
    }
}
```

📌 **解析**

- **`PROJECT_NAME = 'MyApp'`** → 静态变量
- **`${env.BUILD_ID}`** → 访问 Jenkins 内置环境变量
- **整个 Pipeline 都可以使用 `PROJECT_NAME` 和 `BUILD_NUMBER`**



**🔹 局部环境变量（仅作用于 `stage`）**

```groovy
pipeline {
    agent any
    stages {
        stage('Test') {
            environment {
                TEST_ENV = 'Testing'
            }
            steps {
                echo "Current Stage: ${TEST_ENV}"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying... but cannot access TEST_ENV"
            }
        }
    }
}
```

📌 **解析**

- **`TEST_ENV` 仅在 `Test` 阶段可用**
- **`Deploy` 阶段无法访问 `TEST_ENV`**



**2️⃣ `environment {}` 结合 `credentials()` 访问 Jenkins 凭据**

Jenkins **支持存储敏感信息（如 API Key、SSH 密钥）**，可以通过 `credentials()` 访问它们

**🔹 访问 Jenkins Secret Text**

**enkins 管理界面** → **Manage Credentials** → 添加一个 Secret Text：

- **ID**: `GIT_ACCESS_TOKEN`
- **值**: `ghp_xxx123456789`

然后在 `environment {}` 中使用：

```groovy
pipeline {
    agent any
    environment {
        GIT_TOKEN = credentials('GIT_ACCESS_TOKEN')
    }
    stages {
        stage('Clone Repo') {
            steps {
                sh 'git clone https://$GIT_TOKEN@github.com/user/repository.git'
            }
        }
    }
}
```

📌 **解析**

- **`credentials('GIT_ACCESS_TOKEN')` 读取 Jenkins Secret Text**
- **`$GIT_TOKEN` 在 Shell 里可用**
- **避免直接暴露 Token**



**🔹 访问 Jenkins 用户名/密码**

如果你存储的是 **用户名+密码**（如 Docker Hub 登录凭据）：

1. **Jenkins → Manage Credentials** → 添加 `Username with Password` 类型：
   - **ID**: `DOCKER_CREDENTIALS`
   - **Username**: `docker_user`
   - **Password**: `docker_password`
2. **在 `environment {}` 里访问**

```groovy
pipeline {
    agent any
    environment {
        DOCKER_AUTH = credentials('DOCKER_CREDENTIALS')
    }
    stages {
        stage('Login to Docker') {
            steps {
                sh 'echo "$DOCKER_AUTH" | docker login -u docker_user --password-stdin'
            }
        }
    }
}
```

📌 **解析**

- **`credentials('DOCKER_CREDENTIALS')` 访问 Jenkins 存储的 Docker 账号**
- **在 `sh` 里用 `--password-stdin` 方式登录**

如果 Git 需要 **SSH 认证**：

1. **Jenkins → Manage Credentials** → 添加 `SSH Private Key`：
   - **ID**: `GIT_SSH_KEY`
   - **存储 Git SSH 私钥**
2. **Pipeline 访问 SSH 密钥**

🔹 访问 SSH 密钥

```groovy
pipeline {
    agent any
    environment {
        SSH_KEY = credentials('GIT_SSH_KEY')
    }
    stages {
        stage('Setup SSH') {
            steps {
                sh '''
                echo "$SSH_KEY" > ~/.ssh/id_rsa
                chmod 600 ~/.ssh/id_rsa
                ssh -T git@github.com
                '''
            }
        }
    }
}
```

📌 **解析**

- **`credentials('GIT_SSH_KEY')` 访问存储的 SSH Key**
- **`echo` 将 Key 写入 `~/.ssh/id_rsa`**
- **用 SSH 方式拉取 Git 代码**



**3️⃣ `environment {}` 结合 `withEnv()`**

可以使用 `withEnv()` **临时设置环境变量**

```groovy
pipeline {
    agent any
    stages {
        stage('Dynamic Env') {
            steps {
                script {
                    withEnv(['BUILD_MODE=release']) {
                        sh 'echo "Build mode is $BUILD_MODE"'
                    }
                }
            }
        }
    }
}
```

📌 **解析**

- **`withEnv()` 只在 `script` 代码块中有效**
- **适用于临时变量**



**4️⃣ `environment {}` 结合 `sh`**

```groovy
pipeline {
    agent any
    environment {
        JAVA_HOME = '/usr/lib/jvm/java-11-openjdk'
        PATH = '/usr/lib/jvm/java-11-openjdk/bin:$PATH'
    }
    stages {
        stage('Check Java Version') {
            steps {
                sh 'echo "Java Home: $JAVA_HOME"'
                sh 'java -version'
            }
        }
    }
}
```

📌 **解析**

- **设置 `JAVA_HOME` 和 `PATH`**
- **Shell 里可以直接使用**



###### env 命令

**1️⃣ `env` 访问 Jenkins 预定义变量**

Jenkins 预设了一些环境变量，`env` 允许我们访问

```groovy
pipeline {
    agent any
    stages {
        stage('Print Jenkins Vars') {
            steps {
                echo "Job Name: ${env.JOB_NAME}"
                echo "Build Number: ${env.BUILD_NUMBER}"
                echo "Build URL: ${env.BUILD_URL}"
            }
        }
    }
}
```

📌 **常见 `env` 变量**

| **变量**           | **说明**                   | **示例值**                         |
| ------------------ | -------------------------- | ---------------------------------- |
| `env.JOB_NAME`     | **Jenkins Job 名称**       | `MyProject`                        |
| `env.BUILD_NUMBER` | **当前构建号**             | `42`                               |
| `env.BUILD_URL`    | **当前构建的 Jenkins URL** | `http://jenkins/job/MyProject/42/` |
| `env.WORKSPACE`    | **Jenkins 工作目录**       | `/var/jenkins/workspace/MyProject` |



**2️⃣ `env` 访问 `environment {}` 定义的变量**

```groovy
pipeline {
    agent any
    environment {
        MY_VAR = 'Hello'
    }
    stages {
        stage('Check Env') {
            steps {
                echo "MY_VAR: ${env.MY_VAR}"
            }
        }
    }
}
```

📌 **作用**

- **`environment {}` 里的变量，也能用 `env.MY_VAR` 访问**



**3️⃣`env` 允许修改变量**

```groovy
pipeline {
    agent any
    stages {
        stage('Modify Env') {
            steps {
                script {
                    env.BUILD_MODE = 'release'
                }
                echo "Build mode is now: ${env.BUILD_MODE}"
            }
        }
    }
}
```

📌 **作用**

- **在 `script {}` 里，`env.BUILD_MODE` 可以修改**
- **不像 `environment {}` 那样是只读的**



**4️⃣ `environment {}` vs `env` 用法对比**

| **方式**         | **作用范围**                                                 | **是否可修改**                      | **支持 `credentials()`**     | **适用场景**                  |
| ---------------- | ------------------------------------------------------------ | ----------------------------------- | ---------------------------- | ----------------------------- |
| `environment {}` | **全局（整个 Pipeline）或局部（某个 `stage`）**              | ❌ **只读（不能在 `steps` 里修改）** | ✅ **支持 `credentials()`**   | **设置 CI/CD 变量、访问凭据** |
| `env`            | **Jenkins 内置环境变量**（可在 `script {}` 或 `steps` 里使用） | ✅ **可动态修改**                    | ❌ **不支持 `credentials()`** | **获取/修改 Jenkins 变量**    |



**5️⃣ `env` 和 `environment {}` 结合使用**

```groovy
pipeline {
    agent any
    environment {
        APP_ENV = 'staging'
    }
    stages {
        stage('Modify Environment') {
            steps {
                script {
                    env.APP_ENV = 'production'
                }
                echo "APP_ENV is now: ${env.APP_ENV}"
            }
        }
    }
}
```

📌 **解析**

- **`environment {}` 里 `APP_ENV = 'staging'`**
- **在 `script {}` 里修改 `env.APP_ENV = 'production'`**
- **最终 `APP_ENV` 变为 `production`**



###### tools 命令

在 **Jenkins Pipeline** 中，`tools {}` 主要用于 **自动安装和管理构建工具**（如 JDK、Maven、Gradle、Node.js、Go 等）。

**1️⃣ `tools {}` 的基本用法**

🔹 `tools {}` 用于指定构建工具

```groovy
pipeline {
    agent any
    tools {
        jdk 'JDK11'
        maven 'Maven3'
    }
    stages {
        stage('Check Tools') {
            steps {
                sh 'java -version'
                sh 'mvn -version'
            }
        }
    }
}
```

📌 **作用**

- **`tools {}` 指定 JDK 和 Maven 版本**
- **Jenkins 会自动安装 `JDK11` 和 `Maven3` 并配置环境变量**
- **`sh 'java -version'` 和 `sh 'mvn -version'` 确保环境正确**

**2️⃣ `tools {}` 支持的构建工具**

| **工具**    | **关键字** | **示例值**         |
| ----------- | ---------- | ------------------ |
| **JDK**     | `jdk`      | `jdk 'JDK11'`      |
| **Maven**   | `maven`    | `maven 'Maven3'`   |
| **Gradle**  | `gradle`   | `gradle 'Gradle6'` |
| **Node.js** | `nodejs`   | `nodejs 'Node16'`  |
| **Go**      | `go`       | `go 'Go1.18'`      |

📌 **这些工具名称（如 `JDK11`、`Maven3`）必须在**
`Manage Jenkins` → `Global Tool Configuration` 里**提前配置**。

**3️⃣ `tools {}` 详细示例**

**🔹 指定 JDK 和 Maven**

```groovy
pipeline {
    agent any
    tools {
        jdk 'JDK11'
        maven 'Maven3'
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
}
```

📌 **作用**

- **自动安装 `JDK11` 和 `Maven3`**
- **构建 Java 项目**

**🔹 指定 Go**

**4️⃣ `tools {}` vs `environment {}`**

| **方式**             | **作用**                   | **示例**                                    |
| -------------------- | -------------------------- | ------------------------------------------- |
| **`tools {}`**       | **自动安装和配置构建工具** | `tools { maven 'Maven3' }`                  |
| **`environment {}`** | **手动设置环境变量**       | `environment { JAVA_HOME = '/opt/java11' }` |

✅ `tools {}` **更方便，因为 Jenkins 自动配置环境变量**
✅ `environment {}` **适用于手动配置环境，如 `PATH`**

**5️⃣ `tools {}` 结合 `environment {}`**

如果需要同时 **安装工具** 和 **手动修改环境变量**：

```groovy
pipeline {
    agent any
    tools {
        jdk 'JDK11'
        maven 'Maven3'
    }
    environment {
        MAVEN_OPTS = '-Xmx1024m'
    }
    stages {
        stage('Build') {
            steps {
                sh 'java -version'
                sh 'mvn clean package'
            }
        }
    }
}
```

📌 **作用**

- **安装 JDK 和 Maven**
- **设置 `MAVEN_OPTS` 变量**

**6️⃣ 如何在 Jenkins 配置 `tools`**

1. **进入 Jenkins 管理页面**
2. **点击 `Manage Jenkins` → `Global Tool Configuration`**
3. **找到对应工具（如 `JDK`, `Maven`, `Gradle`, `NodeJS`）**
4. **点击 `Add` 添加版本**
5. **设置 `Name`（如 `JDK11`, `Maven3`）**
6. **点击 `Save`**

📌 **必须在 `Global Tool Configuration` 里配置，Pipeline 才能使用**。



###### parameters 命令（参数化构建）

在 **Jenkins Pipeline** 中，`parameters {}` 用于 **定义可选的用户输入参数**，这些参数可以在 **构建时由用户提供**，然后在 Pipeline 中使用。

- **支持多种参数类型（String、Boolean、Choice、Password、File 等）**
- **可以在 Pipeline 代码中通过 `params.PARAM_NAME` 访问**
- **适用于动态构建，如选择分支、环境、版本等**



**1️⃣ `parameters {}` 基本用法**

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'APP_ENV', defaultValue: 'staging', description: '环境变量')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: '是否运行测试')
    }
    stages {
        stage('Print Parameters') {
            steps {
                echo "Environment: ${params.APP_ENV}"
                echo "Run Tests: ${params.RUN_TESTS}"
            }
        }
    }
}
```

📌 **作用**

- **定义 `APP_ENV` 字符串参数**
- **定义 `RUN_TESTS` 布尔参数**
- **构建时用户可以自定义参数**

**2️⃣ `parameters {}` 支持的参数类型**

| **参数类型**   | **示例**                                                     | **作用**                 |
| -------------- | ------------------------------------------------------------ | ------------------------ |
| `string`       | `string(name: 'BRANCH', defaultValue: 'main', description: 'Git 分支')` | **字符串输入**           |
| `booleanParam` | `booleanParam(name: 'DEBUG', defaultValue: false, description: '启用调试')` | **布尔值（true/false）** |
| `choice`       | `choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'], description: '部署环境')` | **下拉菜单**             |
| `password`     | `password(name: 'SECRET', description: '请输入密码')`        | **隐藏输入**             |
| `file`         | `file(name: 'UPLOAD_FILE', description: '上传配置文件')`     | **文件上传**             |
| `text`         | `text(name: 'RELEASE_NOTES', description: '输入发布说明')`   | **多行文本输入**         |

**3️⃣ `string`（字符串参数）**

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'GIT_BRANCH', defaultValue: 'main', description: '选择 Git 分支')
    }
    stages {
        stage('Checkout') {
            steps {
                echo "Pulling branch: ${params.GIT_BRANCH}"
                git branch: "${params.GIT_BRANCH}", url: 'https://github.com/user/repository.git'
            }
        }
    }
}
```

📌 **作用**

- **用户可以输入 `GIT_BRANCH`**
- **动态拉取不同分支**

**4️⃣ `booleanParam`（布尔参数）**

```groovy
pipeline {
    agent any
    parameters {
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: '是否运行测试')
    }
    stages {
        stage('Test') {
            when {
                expression { params.RUN_TESTS == true }
            }
            steps {
                echo "Running tests..."
                sh 'pytest'
            }
        }
    }
}
```

📌 **作用**

- **用户可选择是否运行测试**
- **`when {}` 控制执行逻辑**

**5️⃣ `choice`（下拉选项）**

```groovy
pipeline {
    agent any
    parameters {
        choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'], description: '选择部署环境')
    }
    stages {
        stage('Deploy') {
            steps {
                echo "Deploying to ${params.DEPLOY_ENV} environment"
                sh "./deploy.sh ${params.DEPLOY_ENV}"
            }
        }
    }
}
```

📌 **作用**

- **用户可选择 `dev`、`staging`、`prod`**
- **适用于环境选择**

**6️⃣ `password`（隐藏输入）**

```groovy
pipeline {
    agent any
    parameters {
        password(name: 'DEPLOY_KEY', description: '输入部署密钥')
    }
    stages {
        stage('Use Password') {
            steps {
                withCredentials([string(credentialsId: 'DEPLOY_KEY', variable: 'SECRET')]) {
                    sh 'echo "Using secret key: $SECRET"'
                }
            }
        }
    }
}
```

📌 **作用**

- **`password` 保护敏感信息**
- **结合 `withCredentials()` 使用**

7️⃣**`text`（多行文本输入）**

```groovy
pipeline {
    agent any
    parameters {
        text(name: 'RELEASE_NOTES', description: '输入发布说明')
    }
    stages {
        stage('Show Notes') {
            steps {
                echo "Release Notes: ${params.RELEASE_NOTES}"
            }
        }
    }
}
```

📌 **作用**

- **用户输入多行文本**
- **适用于发布说明、变更日志**

**8️⃣结合 `environment {}` 使用**

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'BUILD_ENV', defaultValue: 'dev', description: '构建环境')
    }
    environment {
        ENV_NAME = "${params.BUILD_ENV}"
    }
    stages {
        stage('Print Env') {
            steps {
                echo "Environment: ${ENV_NAME}"
            }
        }
    }
}
```

📌 **作用**

- **将 `params.BUILD_ENV` 赋值给环境变量**

**1️⃣0️⃣ `parameters {}` vs `environment {}` vs `env`**

| **方式**         | **作用**             | **是否可修改**       | **访问方式**        |
| ---------------- | -------------------- | -------------------- | ------------------- |
| `parameters {}`  | **定义用户输入参数** | ❌ **构建后不可修改** | `params.PARAM_NAME` |
| `environment {}` | **定义环境变量**     | ❌ **构建后不可修改** | `${ENV_NAME}`       |
| `env`            | **Jenkins 内置变量** | ✅ **可动态修改**     | `env.BUILD_NUMBER`  |



###### options 命令

在 **Jenkins Pipeline** 中，`options {}` **用于设置 Pipeline 级别的行为**，比如：

- **构建超时**
- **并发控制**
- **跳过 SCM 轮询**
- **禁用构建撤销**
- **限制日志大小**
- **自定义 Job 失败策略**

**1️⃣ `options {}` 基本用法**

```groovy
pipeline {
    agent any
    options {
        timeout(time: 30, unit: 'MINUTES')  // 超时 30 分钟
        buildDiscarder(logRotator(numToKeepStr: '10'))  // 仅保留最近 10 次构建
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..."
            }
        }
    }
}
```

📌 **作用**

- **设置超时（30 分钟）**
- **保留最近 10 次构建**
- **适用于控制 CI/CD 任务的行为**

**2️⃣ `options {}` 可用的选项**

| **选项**                  | **作用**                        | **示例**                                         |
| ------------------------- | ------------------------------- | ------------------------------------------------ |
| `timeout`                 | **设置构建超时时间**            | `timeout(time: 30, unit: 'MINUTES')`             |
| `buildDiscarder`          | **控制构建记录的保留策略**      | `buildDiscarder(logRotator(numToKeepStr: '10'))` |
| `disableConcurrentBuilds` | **禁止 Job 并发执行**           | `disableConcurrentBuilds()`                      |
| `skipDefaultCheckout`     | **跳过默认的 SCM 拉取**         | `skipDefaultCheckout()`                          |
| `disableResume`           | **禁用流水线恢复**              | `disableResume()`                                |
| `preserveStashes`         | **构建结束后保留 stash 文件**   | `preserveStashes()`                              |
| `quietPeriod`             | **设置 Job 触发后延迟时间**     | `quietPeriod(10)`                                |
| `retry`                   | **设置失败重试次数**            | `retry(3)`                                       |
| `timestamps`              | **在日志中加上时间戳**          | `timestamps()`                                   |
| `parallelsAlwaysFailFast` | **并行 `stage` 失败时立刻终止** | `parallelsAlwaysFailFast()`                      |

**3️⃣ `timeout`（设置超时时间）**

```groovy
pipeline {
    agent any
    options {
        timeout(time: 30, unit: 'MINUTES')
    }
    stages {
        stage('Long Running Task') {
            steps {
                sh 'sleep 2000'
            }
        }
    }
}
```

 **作用**

- **如果 `sleep 2000` 超过 30 分钟，Jenkins 自动终止任务**
- **适用于防止任务无限等待**

**4️⃣ `buildDiscarder`（控制构建历史）**

```groovy
pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '5'))
    }
    stages {
        stage('Build') {
            steps {
                echo "Build in progress..."
            }
        }
    }
}
```

📌 **作用**

- **仅保留最近 10 次构建**
- **仅保留最近 5 个构建的制品**
- **适用于控制磁盘占用**

**5️⃣ `disableConcurrentBuilds`（禁止并发构建）**

```groovy
pipeline {
    agent any
    options {
        disableConcurrentBuilds()
    }
    stages {
        stage('Critical Stage') {
            steps {
                sh 'echo "Running critical stage"'
                sleep 30
            }
        }
    }
}
```

📌 **作用**

- **防止同一个 Job 在多个线程里并行执行**
- **如果 Job 在运行，新的触发会等待**

**6️⃣ `skipDefaultCheckout`（跳过默认 SCM 拉取）**

```groovy
pipeline {
    agent any
    options {
        skipDefaultCheckout()
    }
    stages {
        stage('Checkout Manually') {
            steps {
                git branch: 'main', url: 'https://github.com/user/repository.git'
            }
        }
    }
}
```

**7️⃣ `disableResume`（禁止流水线恢复）**

```groovy
pipeline {
    agent any
    options {
        disableResume()
    }
    stages {
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
            }
        }
    }
}
```

📌 **作用**

- **如果 Jenkins 重启，流水线不会自动恢复**
- **适用于防止半途而废的构建自动继续**

**8️⃣ `preserveStashes`（保留 stash 文件）**

```groovy
pipeline {
    agent any
    options {
        preserveStashes()
    }
    stages {
        stage('Build') {
            steps {
                stash name: 'build-output', includes: '**/target/*.jar'
            }
        }
    }
}
```

📌 **作用**

- **即使构建完成，`stash` 文件不会被删除**
- **适用于多 Job 共享数据**

**9️⃣ `quietPeriod`（触发延迟）**

```groovy
pipeline {
    agent any
    options {
        quietPeriod(10)
    }
    stages {
        stage('Build') {
            steps {
                echo "Job triggered after 10 seconds delay"
            }
        }
    }
}
```

1️⃣0️⃣ `retry`（失败自动重试）

```groovy
pipeline {
    agent any
    options {
        retry(3)
    }
    stages {
        stage('Unstable Step') {
            steps {
                sh 'exit 1' // 失败
            }
        }
    }
}
```

📌 **作用**

- **失败时最多重试 3 次**
- **适用于网络请求等不稳定任务**

**1️⃣1️⃣ `timestamps`（日志加时间戳）**

```groovy
pipeline {
    agent any
    options {
        timestamps()
    }
    stages {
        stage('Log Output') {
            steps {
                sh 'echo "This log has timestamps"'
            }
        }
    }
}
```

**1️⃣2️⃣ `parallelsAlwaysFailFast`（并行任务失败即终止）**

```groovy
pipeline {
    agent any
    options {
        parallelsAlwaysFailFast()
    }
    stages {
        stage('Parallel Jobs') {
            parallel {
                stage('Job 1') {
                    steps {
                        sh 'exit 1'
                    }
                }
                stage('Job 2') {
                    steps {
                        sh 'echo "Job 2 running..."'
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **如果 `Job 1` 失败，整个 `parallel` 立即终止**
- **适用于避免浪费资源**

**1️⃣3️⃣ 结论**

✅ **`options {}` 用于控制 Jenkins Pipeline 行为**
✅ **可用于超时、并发、日志、失败策略等**
✅ **适用于优化 CI/CD 任务的运行方式**

🚀 **最终，`options {}` 让 Jenkins 更灵活，避免不必要的失败和资源浪费！** 🚀



###### input 命令

在 **Jenkins Pipeline** 中，`input {}` 允许 **在流水线的某个 `stage` 暂停执行，等待人工审批**。

- **可以收集用户输入（例如文本、选项、密码）**
- **适用于审批发布、人工选择环境**
- **支持 `timeout`，防止长时间挂起**

**1️⃣ `input {}` 基本用法**

```groovy
pipeline {
    agent any
    stages {
        stage('Deploy Approval') {
            steps {
                script {
                    input "是否批准部署到生产环境？"
                }
                echo "部署被批准，继续执行..."
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying application..."'
            }
        }
    }
}
```

📌 **作用**

- **Pipeline 在 `input` 处暂停**
- **需要用户手动点击 “Proceed”**
- **用户批准后，继续执行 `Deploy`**

**2️⃣ `input {}` 详细语法**

```groovy
input(
    message: '请输入发布环境',
    parameters: [
        string(name: 'VERSION', defaultValue: '1.0.0', description: '请输入版本号'),
        choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'], description: '选择环境'),
        booleanParam(name: 'CONFIRM', defaultValue: true, description: '是否确认发布')
    ]
)
```

📌 **作用**

- **等待用户输入**
- **提供 `string`、`choice`、`booleanParam` 参数**
- **用户提交后，Pipeline 继续执行**

**3️⃣ `input {}` 结合 `params` 读取输入**

```groovy
pipeline {
    agent any
    stages {
        stage('User Input') {
            steps {
                script {
                    def userInput = input(
                        message: '请输入部署参数',
                        parameters: [
                            string(name: 'APP_VERSION', defaultValue: '1.0.0', description: '版本号'),
                            choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'], description: '选择环境')
                        ]
                    )
                    echo "用户输入的版本号: ${userInput.APP_VERSION}"
                    echo "部署环境: ${userInput.DEPLOY_ENV}"
                }
            }
        }
    }
}
```

📌 **作用**

- **用户输入 `APP_VERSION` 和 `DEPLOY_ENV`**
- **在 `script {}` 里读取 `userInput.APP_VERSION` 和 `userInput.DEPLOY_ENV`**
- **适用于动态发布**

**4️⃣ `input {}` 结合 `timeout`（超时自动取消）**

```groovy
pipeline {
    agent any
    stages {
        stage('Approval with Timeout') {
            steps {
                script {
                    try {
                        timeout(time: 60, unit: 'SECONDS') {
                            input "请在 60 秒内批准发布"
                        }
                    } catch (err) {
                        echo "超时未批准，取消发布"
                        currentBuild.result = 'ABORTED'
                        error("超时取消")
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **等待 60 秒，超时后自动取消**
- **`catch (err)` 捕获超时错误**
- **`currentBuild.result = 'ABORTED'` 设置 Jenkins 状态**

**5️⃣ `input {}` 结合 `when {}`（条件触发）**

```groovy
pipeline {
    agent any
    stages {
        stage('Deploy Approval') {
            when {
                branch 'main'  // 只有 main 分支才需要审批
            }
            steps {
                input "请确认是否部署到生产环境？"
            }
        }
    }
}
```

📌 **作用**

- **只有 `main` 分支才需要 `input` 审批**
- **适用于 CI/CD 多分支策略**

**6️⃣ `input {}` 结合 `approver`（指定审批人）**

```groovy
pipeline {
    agent any
    stages {
        stage('Manager Approval') {
            steps {
                input(
                    message: '请审批发布',
                    submitter: 'admin,devops'
                )
            }
        }
    }
}
```

📌 **作用**

- **只有 `admin` 和 `devops` 组用户可以批准**
- **适用于企业级权限管理**

**7️⃣ `input {}` 结合 `password`（敏感输入）**

```groovy
pipeline {
    agent any
    stages {
        stage('User Authentication') {
            steps {
                script {
                    def authInput = input(
                        message: '请输入管理员密码',
                        parameters: [
                            password(name: 'ADMIN_PASS', description: '管理员密码')
                        ]
                    )
                    echo "密码已输入"
                }
            }
        }
    }
}
```

📌 **作用**

- **用户输入密码**
- **适用于 `admin` 级别的敏感操作**

**8️⃣ `input {}` 结合 `parallel`（并行等待）**

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Approvals') {
            parallel {
                stage('Dev Approval') {
                    steps {
                        input "开发团队审批"
                    }
                }
                stage('QA Approval') {
                    steps {
                        input "QA 团队审批"
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **开发和 QA 团队可以分别审批**
- **并行执行，不相互影响**





###### `input` 在 `parallel` 并行审批的行为详解

**1️⃣ `input` 执行逻辑**

| **阶段**         | **执行行为**                                   |
| ---------------- | ---------------------------------------------- |
| `Dev Approval`   | **弹出开发团队审批窗口，阻塞等待手动批准**     |
| `QA Approval`    | **同时弹出 QA 团队审批窗口，阻塞等待手动批准** |
| **开发审批通过** | **QA 仍然在等待审批**                          |
| **QA 通过审批**  | **Pipeline 继续执行**                          |

**2️⃣ `input` 在 Jenkins UI 中的表现**

- **Jenkins 会在 Web UI 提示 "等待用户输入"**
- **点击 "Proceed" 按钮才能继续**
- **如果 `parallel`，两个 `input` 会同时等待**

```bash
[Pipeline] input
等待用户输入: "开发团队审批"
[Pipeline] input
等待用户输入: "QA 团队审批"
```

📌 **如果开发团队批准，QA 仍然会继续等待**

**3️⃣ `input` 结合 `timeout`（超时自动取消）**

如果审批超时，自动取消：

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Approvals') {
            parallel {
                stage('Dev Approval') {
                    steps {
                        script {
                            try {
                                timeout(time: 60, unit: 'SECONDS') {
                                    input "开发团队审批"
                                }
                            } catch (Exception e) {
                                echo "开发团队未审批，自动取消"
                                currentBuild.result = 'ABORTED'
                                error("开发审批超时")
                            }
                        }
                    }
                }
                stage('QA Approval') {
                    steps {
                        script {
                            try {
                                timeout(time: 60, unit: 'SECONDS') {
                                    input "QA 团队审批"
                                }
                            } catch (Exception e) {
                                echo "QA 团队未审批，自动取消"
                                currentBuild.result = 'ABORTED'
                                error("QA 审批超时")
                            }
                        }
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **如果 60 秒内未审批，自动取消**
- **`try-catch` 捕获超时错误**
- **`currentBuild.result = 'ABORTED'` 让 Jenkins 显示取消状态**

**4️⃣ `input` 结合 `submitter`（限制审批人）**

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Approvals') {
            parallel {
                stage('Dev Approval') {
                    steps {
                        input(
                            message: "开发团队审批",
                            submitter: "dev,admin"
                        )
                    }
                }
                stage('QA Approval') {
                    steps {
                        input(
                            message: "QA 团队审批",
                            submitter: "qa,admin"
                        )
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **只有 `dev` 和 `admin` 组用户可以审批 `Dev Approval`**
- **只有 `qa` 和 `admin` 组用户可以审批 `QA Approval`**
- **适用于权限管理**

**6️⃣ `input` 结合 `parameters`（输入参数）**

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Approvals') {
            parallel {
                stage('Dev Approval') {
                    steps {
                        script {
                            def devInput = input(
                                message: "开发团队审批",
                                parameters: [string(name: 'RELEASE_NOTES', description: '输入发布说明')]
                            )
                            echo "开发团队输入的发布说明: ${devInput.RELEASE_NOTES}"
                        }
                    }
                }
                stage('QA Approval') {
                    steps {
                        script {
                            def qaInput = input(
                                message: "QA 团队审批",
                                parameters: [choice(name: 'TEST_RESULT', choices: ['Pass', 'Fail'], description: '测试结果')]
                            )
                            echo "QA 审批结果: ${qaInput.TEST_RESULT}"
                        }
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **开发团队可以输入 `RELEASE_NOTES`（发布说明）**
- **QA 团队可以选择 `Pass/Fail`**
- **可以存入变量 `devInput.RELEASE_NOTES` 和 `qaInput.TEST_RESULT`**

**7️⃣ `input` 结合 `emailext`（发送审批提醒邮件）**

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Approvals') {
            parallel {
                stage('Dev Approval') {
                    steps {
                        script {
                            // 发送邮件通知开发团队
                            emailext subject: "请审批: 开发团队审批请求",
                                     body: "请访问 Jenkins 审批任务: ${env.BUILD_URL}",
                                     to: "dev-team@example.com"

                            // 等待开发团队审批
                            input "开发团队审批"
                        }
                    }
                }
                stage('QA Approval') {
                    steps {
                        script {
                            // 发送邮件通知 QA 团队
                            emailext subject: "请审批: QA 团队审批请求",
                                     body: "请访问 Jenkins 审批任务: ${env.BUILD_URL}",
                                     to: "qa-team@example.com"

                            // 等待 QA 团队审批
                            input "QA 团队审批"
                        }
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **在 `input` 之前发送邮件**
- **邮件正文包含 Jenkins 审批 URL**
- **`env.BUILD_URL` 自动生成 Jenkins 任务链接**
- **开发团队 & QA 团队分别收到邮件后，进入 Jenkins 审批**

**8️⃣ `input` 结合 `timeout`（超时提醒审批人）**

如果 30 分钟后仍未审批，发送邮件提醒：

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Approvals') {
            parallel {
                stage('Dev Approval') {
                    steps {
                        script {
                            // 发送初始审批邮件
                            emailext subject: "请审批: 开发团队审批请求",
                                     body: "请访问 Jenkins 审批任务: ${env.BUILD_URL}",
                                     to: "dev-team@example.com"

                            try {
                                timeout(time: 30, unit: 'MINUTES') {
                                    input "开发团队审批"
                                }
                            } catch (Exception e) {
                                // 发送超时提醒邮件
                                emailext subject: "⚠️ 开发团队审批超时",
                                         body: "任务等待 30 分钟未审批，请尽快处理: ${env.BUILD_URL}",
                                         to: "dev-team@example.com"

                                echo "开发团队未审批，取消任务"
                                currentBuild.result = 'ABORTED'
                                error("开发审批超时")
                            }
                        }
                    }
                }
                stage('QA Approval') {
                    steps {
                        script {
                            // 发送初始审批邮件
                            emailext subject: "请审批: QA 团队审批请求",
                                     body: "请访问 Jenkins 审批任务: ${env.BUILD_URL}",
                                     to: "qa-team@example.com"

                            try {
                                timeout(time: 30, unit: 'MINUTES') {
                                    input "QA 团队审批"
                                }
                            } catch (Exception e) {
                                // 发送超时提醒邮件
                                emailext subject: "⚠️ QA 团队审批超时",
                                         body: "任务等待 30 分钟未审批，请尽快处理: ${env.BUILD_URL}",
                                         to: "qa-team@example.com"

                                echo "QA 团队未审批，取消任务"
                                currentBuild.result = 'ABORTED'
                                error("QA 审批超时")
                            }
                        }
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **30 分钟未审批，自动取消**
- **发送超时提醒邮件**
- **`currentBuild.result = 'ABORTED'` 让 Jenkins 显示取消状态**
- **`error("审批超时")` 让流水线终止**

**9️⃣ `input` 结合 `submitter`（仅特定人员可审批）**

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Approvals') {
            parallel {
                stage('Dev Approval') {
                    steps {
                        input(
                            message: "开发团队审批",
                            submitter: "dev,admin"
                        )
                    }
                }
                stage('QA Approval') {
                    steps {
                        input(
                            message: "QA 团队审批",
                            submitter: "qa,admin"
                        )
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **只有 `dev` 和 `admin` 组用户可以审批 `Dev Approval`**
- **只有 `qa` 和 `admin` 组用户可以审批 `QA Approval`**
- **适用于权限管理**

**1️⃣0️⃣ `input` 结合 `parameters`（输入参数）**

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Approvals') {
            parallel {
                stage('Dev Approval') {
                    steps {
                        script {
                            // 发送邮件通知开发团队
                            emailext subject: "请审批: 开发团队审批请求",
                                     body: "请访问 Jenkins 审批任务: ${env.BUILD_URL}",
                                     to: "dev-team@example.com"

                            // 等待开发团队审批
                            input "开发团队审批"
                        }
                    }
                }
                stage('QA Approval') {
                    steps {
                        script {
                            // 发送邮件通知 QA 团队
                            emailext subject: "请审批: QA 团队审批请求",
                                     body: "请访问 Jenkins 审批任务: ${env.BUILD_URL}",
                                     to: "qa-team@example.com"

                            // 等待 QA 团队审批
                            input "QA 团队审批"
                        }
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **审批人可以输入备注**
- **`params.APPROVAL_COMMENT` 记录审批理由**

**1️⃣1️⃣ `input` 结合 `Slack`（审批提醒）**

```ABAP
Slack 类似于钉钉，它们都是团队协作和即时通讯工具，但 Slack 更侧重于 开发者和 DevOps 场景，而钉钉更适合 企业内部办公。
Slack 是 DevOps 团队最常用的协作工具之一！

可以 与 Jenkins、GitHub、Kubernetes、Prometheus 轻松集成
比 Email 更适合即时通知
与 GitHub Actions、GitLab CI/CD 兼容

✅ Slack 不是开源的，但提供 API 和 Webhook 集成
✅ Slack 提供免费版，适用于小团队
✅ 如果需要完整功能（无限消息、更多 App），需要付费
✅ 开源替代品包括 Mattermost、Rocket.Chat、Zulip
✅ Slack 适用于 DevOps、CI/CD 自动化通知

🚀 最终，Slack 适用于技术团队，但如果需要开源免费版本，建议使用 Mattermost 或 Rocket.Chat！ 🚀
```

除了邮件，还可以 **在 Slack 发送提醒**：

```groovy
pipeline {
    agent any
    stages {
        stage('Approval') {
            steps {
                script {
                    slackSend channel: '#deployments',
                              message: "⚠️ 请审批 Jenkins 任务: ${env.BUILD_URL}"

                    input "请经理审批"
                }
            }
        }
    }
}
```

📌 **作用**

- **在 Slack 频道 `#deployments` 发送提醒**
- **审批人可以点击 `env.BUILD_URL` 进入 Jenkins**



###### emailext 命令

```ABAP
使用 emailext 需要提前在 Jenkins 安装 Email Extension Plugin（邮件扩展插件），否则 emailext 不能正常工作
```

1️⃣**`emailext` 需要安装的插件**

| **插件名称**               | **作用**                                  | **下载方式**                        |
| -------------------------- | ----------------------------------------- | ----------------------------------- |
| **Email Extension Plugin** | 允许 Jenkins 使用 `emailext` 发送邮件     | 在 Jenkins 插件管理里安装           |
| **Mailer Plugin**          | 处理 Jenkins 邮件发送功能（基础邮件支持） | Jenkins 默认预装，`emailext` 依赖它 |

📌 **注意**

- **`Email Extension Plugin` 依赖 `Mailer Plugin`，需要同时安装**
- **确保 Jenkins 服务器可以连接 SMTP 邮件服务器（如 Gmail、企业邮箱）**

**2️⃣配置 Jenkins SMTP 邮件服务器 （上面有详细的配置方法，并且配有插图）**

安装插件后，需要 **配置邮件服务器**，否则 `emailext` 不能发送邮件。

**🔹 配置 SMTP**

- **进入 Jenkins `Manage Jenkins`**

- **点击 `Configure System`**

- **找到 `Extended E-mail Notification`**

- **填写 SMTP 服务器信息**

  - **SMTP Server**（示例：`smtp.example.com`）

  - **User Name**（示例：`jenkins@example.com`）

  - **Password**（SMTP 邮箱密码）

  - **Use SMTP Authentication**（✅ 勾选）

  - **SMTP Port**

    **（常见端口：**

    - **`465`（SSL 加密）**
    - **`587`（TLS 加密）**

- **Reply-To Address**（示例：`noreply@example.com`）

1. **测试邮件**
   - **填写 `Test E-mail recipient`**
   - **点击 `Test configuration`**

📌 **示例：Gmail SMTP 配置**

```bash
SMTP Server: smtp.gmail.com
User Name: your-email@gmail.com
Password: your-app-password
Use SSL: ✅
SMTP Port: 465
```

📌 **如果 Gmail SMTP 被阻止**

- **使用 Gmail "应用专用密码"**
- **开启 "允许不安全应用访问"**

**3️⃣测试 `emailext` 是否正常**

安装插件并配置 SMTP 服务器后，可以使用 **Pipeline 代码测试 `emailext`**

```groovy
pipeline {
    agent any
    stages {
        stage('Send Email') {
            steps {
                emailext(
                    subject: "Jenkins 测试邮件",
                    body: "Jenkins 服务器邮件通知测试成功！",
                    to: "user@example.com"
                )
            }
        }
    }
}
```

**4️⃣`emailext` 的基本语法**

```groovy
emailext(
    subject: '邮件主题',
    body: '邮件正文',
    to: 'user@example.com'
)
```

📌 **作用**

- `subject` → 邮件的 **主题**
- `body` → 邮件的 **正文**
- `to` → **接收人**（多个邮件用 `,` 分隔）

**5️⃣ `emailext` 发送 Jenkins 构建通知**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
    post {
        success {
            emailext(
                subject: "✅ Jenkins 构建成功 - ${env.JOB_NAME}",
                body: "Jenkins 构建成功！请查看详情: ${env.BUILD_URL}",
                to: "dev-team@example.com"
            )
        }
        failure {
            emailext(
                subject: "❌ Jenkins 构建失败 - ${env.JOB_NAME}",
                body: "Jenkins 构建失败！请查看日志: ${env.BUILD_URL}",
                to: "dev-team@example.com"
            )
        }
    }
}
```

📌 **作用**

- **构建成功时，发送 `✅ 成功` 邮件**
- **构建失败时，发送 `❌ 失败` 邮件**
- **邮件内容包含 Jenkins 构建 URL**
- **适用于 CI/CD 监控**

**6️⃣ `emailext` 主要参数**

| **参数**             | **作用**   | **示例**                |
| -------------------- | ---------- | ----------------------- |
| `to`                 | 邮件接收人 | `"user@example.com"`    |
| `cc`                 | 抄送       | `"manager@example.com"` |
| `bcc`                | 密送       | `"admin@example.com"`   |
| `subject`            | 邮件主题   | `"构建通知"`            |
| `body`               | 邮件正文   | `"Jenkins 任务完成"`    |
| `from`               | 发送人     | `"jenkins@example.com"` |
| `replyTo`            | 回复地址   | `"noreply@example.com"` |
| `attachmentsPattern` | 附件       | `"logs/*.txt"`          |
| `mimeType`           | 邮件类型   | `"text/html"`           |

------

**7️⃣ `emailext` 发送 HTML 格式邮件**

```groovy
emailext(
    subject: "✅ 构建成功 - ${env.JOB_NAME}",
    body: """
        <html>
            <body>
                <h2>构建成功 🎉</h2>
                <p>任务名称: ${env.JOB_NAME}</p>
                <p>构建详情: <a href='${env.BUILD_URL}'>查看 Jenkins</a></p>
            </body>
        </html>
    """,
    mimeType: 'text/html',
    to: "dev-team@example.com"
)
```

📌 **作用**

- **支持 HTML 格式**
- **邮件正文带超链接**
- **适用于更美观的邮件通知**

**8️⃣`emailext` 发送带附件的邮件**

```groovy
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
        }
    }
    post {
        always {
            emailext(
                subject: "📝 测试报告 - ${env.JOB_NAME}",
                body: "请查收最新测试报告。",
                to: "qa-team@example.com",
                attachmentsPattern: "results.xml"
            )
        }
    }
}
```

📌 **作用**

- **邮件附带 `results.xml` 测试报告**
- **适用于 CI/CD 测试通知**

**9️⃣ `emailext` 结合 `input` 发送审批邮件**

```groovy
pipeline {
    agent any
    stages {
        stage('Approval') {
            steps {
                script {
                    emailext(
                        subject: "⚠️ 请审批 Jenkins 任务 - ${env.JOB_NAME}",
                        body: "请访问 Jenkins 进行审批: ${env.BUILD_URL}",
                        to: "manager@example.com"
                    )
                    input "请审批"
                }
            }
        }
    }
}
```

📌 **作用**

- **邮件通知审批人**
- **Jenkins 暂停等待审批**
- **适用于手动审批流程**

**1️⃣0️⃣ `emailext` 结合 `timeout` 发送超时提醒**

```groovy
pipeline {
    agent any
    stages {
        stage('Approval') {
            steps {
                script {
                    emailext(
                        subject: "⚠️ 请审批 Jenkins 任务 - ${env.JOB_NAME}",
                        body: "请访问 Jenkins 进行审批: ${env.BUILD_URL}",
                        to: "manager@example.com"
                    )
                    try {
                        timeout(time: 30, unit: 'MINUTES') {
                            input "请审批"
                        }
                    } catch (Exception e) {
                        emailext(
                            subject: "⚠️ 审批超时 - ${env.JOB_NAME}",
                            body: "审批超时，任务已取消。",
                            to: "manager@example.com"
                        )
                        error("审批超时")
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **发送审批通知**
- **30 分钟未审批，发送超时提醒**
- **适用于 CI/CD 审批流程**

**1️⃣1️⃣ `emailext` 结合 `try-catch` 处理异常**

```groovy
pipeline {
    agent any
    stages {
        stage('Approval') {
            steps {
                script {
                    emailext(
                        subject: "⚠️ 请审批 Jenkins 任务 - ${env.JOB_NAME}",
                        body: "请访问 Jenkins 进行审批: ${env.BUILD_URL}",
                        to: "manager@example.com"
                    )
                    try {
                        timeout(time: 30, unit: 'MINUTES') {
                            input "请审批"
                        }
                    } catch (Exception e) {
                        emailext(
                            subject: "⚠️ 审批超时 - ${env.JOB_NAME}",
                            body: "审批超时，任务已取消。",
                            to: "manager@example.com"
                        )
                        error("审批超时")
                    }
                }
            }
        }
    }
}
```

📌 **作用**

- **发送审批通知**
- **30 分钟未审批，发送超时提醒**
- **适用于 CI/CD 审批流程**

**1️⃣2️⃣`emailext` 结合 `triggerRemoteJob`（远程触发任务后通知)**

```groovy
pipeline {
    agent any
    stages {
        stage('Trigger Remote Job') {
            steps {
                sh 'curl -X POST http://jenkins.example.com/job/RemoteJob/build?token=secret-token'
                emailext(
                    subject: "🚀 远程任务已触发 - ${env.JOB_NAME}",
                    body: "Jenkins 远程任务已启动，请查看进度。",
                    to: "dev-team@example.com"
                )
            }
        }
    }
}
```



###### when 命令

**1️⃣ `when {}` 基本语法**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            when {
                expression { return true }  // ✅ 如果返回 true，执行该 stage
            }
            steps {
                echo "正在执行 Build 任务..."
            }
        }
    }
}
```

📌 **作用**

- **如果 `expression { return true }`，则 `Build` 阶段会执行**
- **可以使用条件控制 `stage` 是否运行**

**2️⃣ `when` 支持的条件类型**

| **条件类型**  | **作用**                              | **示例**                                                     |
| ------------- | ------------------------------------- | ------------------------------------------------------------ |
| `branch`      | 仅在特定 Git 分支执行                 | `branch 'main'`                                              |
| `environment` | 仅在特定环境变量匹配时执行            | `environment name: 'DEPLOY_ENV', value: 'prod'`              |
| `equals`      | 仅在参数等于指定值时执行              | `equals expected: 'yes', actual: params.DEPLOY`              |
| `expression`  | 使用 Groovy 逻辑控制                  | `expression { env.BUILD_NUMBER.toInteger() % 2 == 0 }`       |
| `not`         | 取反逻辑                              | `not { branch 'dev' }`                                       |
| `anyOf`       | 逻辑 OR（多个条件任意匹配）           | `anyOf { branch 'main'; branch 'dev' }`                      |
| `allOf`       | 逻辑 AND（所有条件必须匹配）          | `allOf { branch 'main'; environment name: 'DEPLOY', value: 'yes' }` |
| `buildingTag` | 仅在构建 Git Tag 时执行               | `buildingTag()`                                              |
| `changelog`   | 仅在 Git 提交信息包含某些关键字时执行 | `changelog 'fix                                              |
| `changeset`   | 仅在文件发生特定变化时执行            | `changeset pattern: 'src/**'`                                |

**3️⃣ `when { branch 'main' }`（根据分支执行）**

```groovy
pipeline {
    agent any
    stages {
        stage('Deploy to Production') {
            when {
                branch 'main'  // ✅ 仅在 main 分支执行
            }
            steps {
                echo "🚀 部署到生产环境"
            }
        }
    }
}
```

📌 **作用**

- **只有在 `main` 分支时，`Deploy to Production` 才会执行**
- **适用于 CI/CD 分支控制**

**4️⃣ `when { environment name: 'DEPLOY_ENV', value: 'prod' }`（根据环境变量执行）**

```groovy
pipeline {
    agent any
    stages {
        stage('Deploy to Production') {
            when {
                environment name: 'DEPLOY_ENV', value: 'prod'
            }
            steps {
                echo "🚀 部署到生产环境"
            }
        }
    }
}
```

📌 **作用**

- **如果 `DEPLOY_ENV=prod`，则执行 `Deploy to Production`**
- **适用于不同环境的 CI/CD 部署**

**5️⃣ `when { equals expected: 'yes', actual: params.DEPLOY }`（根据参数执行）**

```groovy
pipeline {
    agent any
    parameters {
        choice(name: 'DEPLOY', choices: ['yes', 'no'], description: '是否部署？')
    }
    stages {
        stage('Deploy') {
            when {
                equals expected: 'yes', actual: params.DEPLOY  // ✅ 仅当参数值为 yes 时执行
            }
            steps {
                echo "🚀 正在部署..."
            }
        }
    }
}
```

📌 **作用**

- **当用户在 Jenkins 构建时选择 `DEPLOY=yes`，才会执行 `Deploy`**
- **适用于手动控制部署**

**6️⃣ `when { expression { condition } }`（使用表达式）**

```groovy
pipeline {
    agent any
    stages {
        stage('Even Build') {
            when {
                expression { env.BUILD_NUMBER.toInteger() % 2 == 0 }  // ✅ 仅在偶数构建号时执行
            }
            steps {
                echo "当前构建号: ${env.BUILD_NUMBER}，是偶数，执行任务"
            }
        }
    }
}
```

📌 **作用**

- **只有 `BUILD_NUMBER` 为偶数时才执行**
- **适用于动态控制 `stage` 何时执行**

**7️⃣ `when { not { condition } }`（取反）**

```groovy
pipeline {
    agent any
    stages {
        stage('Skip on Dev Branch') {
            when {
                not { branch 'dev' }  // ❌ `dev` 分支不会执行
            }
            steps {
                echo "🚀 不是 dev 分支，执行任务"
            }
        }
    }
}
```

📌 **作用**

- **如果当前分支不是 `dev`，则执行**
- **适用于跳过特定分支**

**8️⃣ `when { anyOf { condition1; condition2 } }`（多个条件 OR）**

```groovy
pipeline {
    agent any
    stages {
        stage('Run on Main or Dev') {
            when {
                anyOf {
                    branch 'main'
                    branch 'dev'
                }
            }
            steps {
                echo "当前分支是 main 或 dev，执行任务"
            }
        }
    }
}
```

📌 **作用**

- **如果分支是 `main` 或 `dev`，则执行**
- **适用于多个分支的 CI/CD 流程**

**✅ 9️⃣ `when { allOf { condition1; condition2 } }`（多个条件 AND）**

```groovy
pipeline {
    agent any
    stages {
        stage('Deploy') {
            when {
                allOf {
                    branch 'main'
                    environment name: 'DEPLOY', value: 'yes'
                }
            }
            steps {
                echo "🚀 生产环境部署已启动"
            }
        }
    }
}
```

📌 **作用**

- **当 `branch='main'` 且 `DEPLOY=yes` 时才执行**
- **适用于复杂的 CI/CD 逻辑**

**✅ 1️⃣0️⃣ `when { buildingTag() }`（仅在构建 Git Tag 时执行）**

```groovy
pipeline {
    agent any
    stages {
        stage('Release Build') {
            when {
                buildingTag()
            }
            steps {
                echo "📦 这是一个发布版本，正在执行 Release 任务..."
            }
        }
    }
}
```

📌 **作用**

- **仅在 Git Tag 构建时执行**
- **适用于自动发布版本**

**1️⃣1️⃣ `when { changelog 'fix|hotfix' }`（检查 Git 提交信息）**

```groovy
pipeline {
    agent any
    stages {
        stage('Run on Fixes') {
            when {
                changelog 'fix|hotfix'
            }
            steps {
                echo "🚀 代码提交信息包含 'fix' 或 'hotfix'，执行任务"
            }
        }
    }
}
```

📌 **作用**

- **如果 Git 提交信息包含 `"fix"` 或 `"hotfix"`，则执行**
- **适用于 Bug 修复的自动测试**



##### Jenkins pipeline 进阶

###### pipeline中函数的使用

**1️⃣ `Declarative Pipeline` 里如何定义和调用函数**

在 **Declarative Pipeline（声明式流水线）** 里，函数必须 **放在 `script {}` 代码块里**：

```groovy
pipeline {
    agent any
    stages {
        stage('Test Function') {
            steps {
                script {
                    def result = multiplyNumbers(5, 10)
                    echo "计算结果: ${result}"
                }
            }
        }
    }
}

// 自定义函数
def multiplyNumbers(a, b) {
    return a * b
}
```

📌 **解析**

- **定义 `multiplyNumbers(a, b)` 函数，返回 `a \* b`**
- **在 `script {}` 代码块中调用 `multiplyNumbers(5, 10)`**
- **输出 `计算结果: 50`**



2️⃣**Jenkins Pipeline 支持返回值的函数**

```groovy
pipeline {
    agent any
    stages {
        stage('Generate ID') {
            steps {
                script {
                    def uniqueId = generateUniqueId()
                    echo "生成的唯一 ID: ${uniqueId}"
                }
            }
        }
    }
}

// 生成唯一 ID 的函数
def generateUniqueId() {
    return UUID.randomUUID().toString()
}
```

📌 **解析**

- **`generateUniqueId()` 生成 UUID**
- **返回值可以在 `script {}` 里使用**
- **适用于构建唯一标识符**



**3️⃣Jenkins Pipeline 里的函数可以调用 `sh` 命令**

```groovy
pipeline {
    agent any
    stages {
        stage('Check Disk Space') {
            steps {
                script {
                    def freeSpace = checkDiskSpace()
                    echo "磁盘剩余空间: ${freeSpace}"
                }
            }
        }
    }
}

// 运行 `df -h` 命令并返回磁盘剩余空间
def checkDiskSpace() {
    return sh(script: "df -h | grep '/dev/sda1' | awk '{print \$4}'", returnStdout: true).trim()
}
```

📌 **解析**

- **`sh(script: ..., returnStdout: true)`** → 运行 Shell 命令并返回结果
- **`.trim()`** → 去除换行符
- **可以在 `script {}` 里使用返回值**



**4️⃣Jenkins Pipeline 里的函数可以嵌套**

```groovy
pipeline {
    agent any
    stages {
        stage('Process Data') {
            steps {
                script {
                    def numbers = [1, 2, 3, 4, 5]
                    def squaredNumbers = processList(numbers, squareNumber)
                    echo "平方结果: ${squaredNumbers}"
                }
            }
        }
    }
}

// 处理列表数据
def processList(list, closure) {
    return list.collect { closure(it) }
}

// 计算平方
def squareNumber(num) {
    return num * num
}

```

📌 **解析**

- **`processList(numbers, squareNumber)`** → 传递函数 `squareNumber` 作为参数
- **`squareNumber(num)`** → 计算平方
- **`collect { closure(it) }`** → 遍历 `list`，对每个元素执行 `closure` 函数



**5️⃣Jenkins Pipeline 里的函数可以调用 `parallel` 并行执行**

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Tasks') {
            steps {
                script {
                    def tasks = [
                        "Task 1": { runTask("任务 1") },
                        "Task 2": { runTask("任务 2") }
                    ]
                    parallel tasks
                }
            }
        }
    }
}

// 定义任务
def runTask(name) {
    echo "正在执行: ${name}"
    sh "sleep 2"
}
```

📌 **解析**

- **`parallel tasks`** 并行执行 `Task 1` 和 `Task 2`
- **`runTask(name)`** 运行 Shell 命令
- **适用于并行测试、并行构建**



###### stage 函数

**可以将某个 `stage` 定义为函数**，然后在 Pipeline 里调用它，实现 **代码复用** 和 **减少冗余**。

在 **Jenkins Pipeline（Declarative & Scripted）** 中，你可以：

- **把 `stage` 的逻辑封装到函数**
- **在 `script {}` 代码块中调用该函数**
- **根据不同参数执行不同 `stage`**

**1️⃣ 基本用法：将 `stage` 逻辑封装为函数**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    buildProject()  // ✅ 调用封装的构建函数
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    runTests()  // ✅ 调用封装的测试函数
                }
            }
        }
    }
}

// ✅ 封装 `stage` 逻辑到函数
def buildProject() {
    echo "开始构建项目..."
    sh 'mvn clean package'
}

def runTests() {
    echo "执行单元测试..."
    sh 'pytest tests/'
}
```

📌 **解析**

- **`def buildProject()`** → 定义 `Build` 阶段的构建逻辑
- **`def runTests()`** → 定义 `Test` 阶段的测试逻辑
- **`script { buildProject() }`** → 在 `stage` 里调用封装的函数
- **这样可以复用 `buildProject()` 和 `runTests()`，提高可维护性**

**2️⃣ 使用参数让 `stage` 变得动态**

你可以定义一个 **通用的 `stage` 函数**，然后 **根据参数动态执行不同的阶段**

```groovy
pipeline {
    agent any
    stages {
        stage('Dynamic Build') {
            steps {
                script {
                    executeStage('Build', 'mvn clean package')
                }
            }
        }
        stage('Dynamic Test') {
            steps {
                script {
                    executeStage('Test', 'pytest tests/')
                }
            }
        }
    }
}

// ✅ 定义通用 `stage` 函数
def executeStage(stageName, command) {
    echo "开始执行阶段: ${stageName}"
    sh command
}
```

📌 **解析**

- **`executeStage(stageName, command)`** → 一个通用 `stage` 逻辑
- **不同 `stage` 传入不同的 `command`**
- **减少重复代码，Pipeline 变得更灵活**

**3️⃣ 并行 `stage` 封装为函数**

如果你的 CI/CD 任务有多个 **并行 `stage`**，你可以把它们封装到 **函数**

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Tasks') {
            steps {
                script {
                    def tasks = [
                        "Build": { executeStage("Build", "mvn clean package") },
                        "Test": { executeStage("Test", "pytest tests/") },
                        "Deploy": { executeStage("Deploy", "./deploy.sh") }
                    ]
                    parallel tasks  // ✅ 并行执行多个 `stage`
                }
            }
        }
    }
}

// ✅ 定义通用 `stage` 函数
def executeStage(stageName, command) {
    echo "开始执行: ${stageName}"
    sh command
}
```

📌 **解析**

- **`parallel tasks`** → 并行执行 `Build`、`Test`、`Deploy`
- **封装 `executeStage(stageName, command)`**
- **动态控制 `stage` 逻辑**

**4️⃣ `post` 处理 `stage` 失败**

你可以封装 **错误处理逻辑**，当某个 `stage` 失败时执行 `post`：

```groovy
pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                script {
                    try {
                        executeStage("Deploy", "./deploy.sh")
                    } catch (Exception e) {
                        handleFailure("Deploy", e)
                    }
                }
            }
        }
    }
}

// ✅ 封装通用 `stage` 函数
def executeStage(stageName, command) {
    echo "开始执行: ${stageName}"
    sh command
}

// ✅ 失败处理函数
def handleFailure(stageName, error) {
    echo "❌ 阶段 ${stageName} 失败，错误信息: ${error}"
    emailext(
        subject: "❌ ${stageName} 失败",
        body: "请检查 Jenkins 任务: ${env.BUILD_URL}",
        to: "dev-team@example.com"
    )
}
```

**5️⃣ 组合多个 `stage` 为一个函数**

```groovy
pipeline {
    agent any
    stages {
        stage('Build & Test') {
            steps {
                script {
                    buildAndTest()  // ✅ 组合多个阶段的函数
                }
            }
        }
    }
}

// ✅ 组合 `Build` 和 `Test`
def buildAndTest() {
    echo "开始构建..."
    sh 'mvn clean package'

    echo "开始测试..."
    sh 'pytest tests/'
}
```

📌 **解析**

- **`buildAndTest()` 封装 `Build` 和 `Test`**
- **只需要调用 `buildAndTest()`，减少重复代码**

**6️⃣ 结合 `input` 和 `timeout` 进行审批**

```groovy
pipeline {
    agent any
    stages {
        stage('Deploy Approval') {
            steps {
                script {
                    approvalRequired('生产环境')
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    executeStage('Deploy', './deploy.sh')
                }
            }
        }
    }
}

// ✅ 审批函数
def approvalRequired(env) {
    try {
        timeout(time: 30, unit: 'MINUTES') {
            input "请批准部署到 ${env} 环境"
        }
    } catch (Exception e) {
        echo "审批超时，取消部署"
        currentBuild.result = 'ABORTED'
        error("审批超时")
    }
}

// ✅ 通用 `stage` 执行函数
def executeStage(stageName, command) {
    echo "开始执行: ${stageName}"
    sh command
}
```

📌 **解析**

- **`approvalRequired('生产环境')` 处理审批**
- **`executeStage('Deploy', './deploy.sh')` 部署**
- **30 分钟未审批，自动取消**



###### 多文件共享函数

1️⃣在 `shared.groovy` **里定义通用函数**

如果 **多个 `Jenkinsfile` 需要共享相同的函数**，建议使用 **共享库（Shared Library）**。

**🔹 第一步：创建 `vars/shared.groovy`**

在 Jenkins 服务器上，创建 **共享库目录**：

```bash
mkdir -p /var/lib/jenkins/shared-library/vars
cd /var/lib/jenkins/shared-library/vars
```

**创建 `shared.groovy`**

```groovy
// vars/shared.groovy
def buildAndDeploy(String projectName, String buildCmd, String deployScript) {
    echo "🚀 开始构建 ${projectName}"
    sh buildCmd
    echo "🚀 开始部署 ${projectName}"
    sh deployScript
}

// 让 `shared.groovy` 能被外部调用
return this
```

📌 **作用**

- **定义 `buildAndDeploy()`**
- **所有 `Jenkinsfile` 可以加载 `shared.groovy` 并调用 `buildAndDeploy()`**
- **`return this` 让 `shared.groovy` 能被加载**



**🔹 第二步：在 Jenkins 配置共享库**

1. **进入 `Jenkins` 管理后台**
2. **点击 `Manage Jenkins`**
3. **点击 `Global Pipeline Libraries`**
4. 点击 `Add`
   - **Library name:** `shared-library`
   - **Default version:** `master`（如果使用 Git）
   - **Retrieval method:** `Modern SCM`
   - **Git repository URL:** `https://github.com/your-org/jenkins-shared-library.git`
   - **Load implicitly:** ✅ **勾选（自动加载）**

📌 **这样，所有 Jenkins 任务都能用 `shared.groovy` 里的函数！**



**🔹 第三步：在 `Jenkinsfile` 里引用 `shared.groovy`**

```groovy
@Library('shared-library') _

pipeline {
    agent any
    stages {
        stage('Project A - Build & Deploy') {
            steps {
                script {
                    shared.buildAndDeploy('Project A', 'mvn clean package', 'deploy-A.sh')
                }
            }
        }
        stage('Project B - Build & Deploy') {
            steps {
                script {
                    shared.buildAndDeploy('Project B', 'npm install && npm run build', 'deploy-B.sh')
                }
            }
        }
    }
}
```

📌 **作用**

- **使用 `@Library('shared-library') _` 加载共享库**
- **使用 `shared.buildAndDeploy()` 调用 `shared.groovy` 里的函数**
- **多个 `Jenkinsfile` 共享同一套 `buildAndDeploy()` 逻辑**



**2️⃣ 方案 3：直接从 Git 远程加载共享函数**

如果你的共享函数存储在 **远程 Git 仓库**，可以直接加载

```groovy
@Library('github.com/your-org/jenkins-shared-library') _

pipeline {
    agent any
    stages {
        stage('Project A - Build & Deploy') {
            steps {
                script {
                    shared.buildAndDeploy('Project A', 'mvn clean package', 'deploy-A.sh')
                }
            }
        }
    }
}
```

📌 **作用**

- **从 GitHub / GitLab / 企业 Git 直接加载共享库**
- **避免 Jenkins 服务器本地存储代码**



#### 实现一个简单 Pipeline Job

##### 安装 Pipeline 插件

安装 **Pipeline** 和 **Pipeline Stage View** 插件



##### 创建 Pipeline Job

![image-20250227211812589](../markdown_img/image-20250227211812589.png)



##### 测试简单 Pipeline Job 运行

Pipeline 测试代码

```groovy
pipeline {
    agent any
    stages {
        stage('获取代码') {
            steps {
                echo '获取代码'
            }
    }
        stage('构建代码') {
            steps {
                echo '构建项目代码'
            }
        }
        stage('代码测试') {
            steps {
                echo '测试项目功能'
            }
        }
        stage('项目部署') {
                steps {
                    echo '部署项目'
                }
        }
    }
}
```

 Jenkins Web 界面配置

![image-20250227212308189](../markdown_img/image-20250227212308189.png)



##### 执行 Pipeline Job

任务执行结果在阶段视图中以方块的形式显示

- 一次构建用一行方块来表示,其中每个方块代表流水线中的一个stage
- 每个方块都代表了一个特定阶段的一次执行结果

**块颜色的意义**

- 蓝色条纹:stage 运行中
- 白色: stage尚未执行
- 红色条纹:state执行失败
- 绿色:stage执行成功
- 浅红色:stage 执行成动，但是下游的某个stage出现失败

![image-20250227212550509](../markdown_img/image-20250227212550509.png)



如果安装Blue Ocean 插件,可以下看如下的显示效果

![image-20250227212709806](../markdown_img/image-20250227212709806.png)

![image-20250227212729211](D:\git_repository\cyber_security_learning\markdown_img\image-20250227212729211.png)

#### 自动生成拉取代码的 Pipeline 脚本

![image-20250227213053118](../markdown_img/image-20250227213053118.png)

![image-20250227213159445](../markdown_img/image-20250227213159445.png)

![image-20250227213243882](../markdown_img/image-20250227213243882.png)

![image-20250227220601973](../markdown_img/image-20250227220601973.png)

![image-20250227220656449](D:\git_repository\cyber_security_learning\markdown_img\image-20250227220656449.png)

![image-20250227220724455](../markdown_img/image-20250227220724455.png)



###### 验证结果

![image-20250227221014115](../markdown_img/image-20250227221014115.png)



![image-20250227221123245](../markdown_img/image-20250227221123245.png)

Jenkins 服务器验证 clone 代码数据是否成功

```bash
# 从 gitlab 拉下来的代码
[root@mystical /var/lib/jenkins/workspace/pipeline-demo1]# ls
deploy      Dockerfile-multistages  pom.xml    sonar-project.properties
Dockerfile  Jenkinsfile             README.md  src
```



#### 流水线步骤

Pipeline Job中的流水线步骤可以分解显示每个步骤的执行状态

![image-20250227223633213](../markdown_img/image-20250227223633213.png)



![image-20250227225030445](../markdown_img/image-20250227225030445.png)



#### 回放 Replay

对于错误的构建任务，Jenkins提供了一种称为“回放”的机制，它允许用户无须改变已保存的原有代码的基础上进行试验和调试

回放为用户提供了一种在原有代码基础上修改代码并再次触发pipeline的功能，以便于在正式提交代码 之前进行一次变更的快速快速验证并查看效果；

点击构建菜单中的“回放”，会弹出编辑窗口，并允许用户任意临时修改程序，而后点击“运行”按钮来验证变更效果

Jenkins会在回放窗口中运行编辑后的代码，并保存一次全新的构建记录，但原始代码依然保持从前的状态

因此，回放操作能帮用户验证变更，但真正的变更依然需要用户手动更新pipeline的代码完成

![image-20250228091750460](../markdown_img/image-20250228091750460.png)

![image-20250228091837372](../markdown_img/image-20250228091837372.png)



##### `Replay` 适合哪些场景？

| **场景**                    | **是否适用 `Replay`？** | **原因**                            |
| --------------------------- | ----------------------- | ----------------------------------- |
| **测试 `Jenkinsfile` 语法** | ✅ **适用**              | `Replay` 可用于调试 Pipeline 代码   |
| **调试 CI/CD 逻辑**         | ✅ **适用**              | 适合测试 `when`、`input` 等逻辑     |
| **测试 `sh` 命令是否正确**  | ⚠️ **部分适用**          | `Replay` 可能不会真正执行 `sh` 命令 |
| **真正的 CI/CD 部署**       | ❌ **不适用**            | `Replay` 不会修改生产环境           |
| **回滚代码**                | ❌ **不适用**            | `Replay` 只是临时修改，不影响 Git   |

📌 **如果只是测试 `Jenkinsfile` 语法，`Replay` 很有用，但它不能替代真正的构建部署。**



**`Replay` 与 `Build Now` 的区别**

| **功能**               | **Replay（回放）** | **Build Now（立即构建）**  |
| ---------------------- | ------------------ | -------------------------- |
| **修改 `Jenkinsfile`** | ✅ **可以临时修改** | ❌ **不修改 `Jenkinsfile`** |
| **影响 Git 代码**      | ❌ **不会影响**     | ❌ **不会影响**             |
| **实际执行部署**       | ❌ **不会真正执行** | ✅ **会真正执行**           |
| **适合调试**           | ✅ **适合**         | ❌ **不适合**               |
| **适合生产部署**       | ❌ **不适合**       | ✅ **适合**                 |

📌 **如果你只是调试 Jenkinsfile 代码，可以用 `Replay`；但如果你要真正构建或部署，必须使用 `Build Now`**





#### 从指定阶段重新运行

```ABAP
注意：声明式Pipeline 语法才支持
```

![image-20250228092402507](../markdown_img/image-20250228092402507.png)

![image-20250228092513974](../markdown_img/image-20250228092513974.png)







### 代码质量检测 SonarQube

#### 代码测试工具 SonarQube 简介

![image-20250228093214079](D:\git_repository\cyber_security_learning\markdown_img\image-20250228093214079.png)

SonarQube  是一个开源平台，用于管理源代码的质量

Sonar 不只是一个质量数据报告工具，更是**代码质量管理平台**。

支持的语言包括：Java、Go、Python、PHP、C、C++C#、C#、JavaScripts、Scala、HTML、 PL/SQL、Swift、Ruby等29种语言。

![image-20250228093339366](D:\git_repository\cyber_security_learning\markdown_img\image-20250228093339366.png)

SonarQube是一种自动代码审查工具，用于检测代码中的错误漏洞和代码异味，它集成到现有的工作流 程,以便在项目分支和拉取(PR)请求之间进行连续的代码检查

SonarQube 支持多种插件,实现和 Jenkins 等 CICD 工具的集成



**主要特点**

- 代码覆盖：通过单元测试，将会显示哪行代码被选中
- 改善编码规则
- 搜寻编码规则：按照名字，插件，激活级别和类别进行查询
- 项目搜寻：按照项目的名字进行查询
- 对比数据：比较同一张表中的任何测量的趋势

```http
官方网站：
http://www.sonarqube.org/ 
下载地址：
https://www.sonarqube.org/downloads/
Github 地址: 
https://github.com/SonarSource/sonarqube
```



#### 七个维度检测代码质量

- **可维护性（maintainability）**

  所谓“代码易维护”就是指，在不破坏原有代码设计、不引入新的 bug 的情况下，能够快速地修改或者添 加代码。

- **可读性（readability）**

  在编写代码的时候，时刻要考虑到代码是否易读、易理解。除此之外，代码的可读性在非常大程度上会 影响代码的可维护性。

  看代码是否符合编码规范、命名是否达意、注释是否详尽、函数是否长短合适、模块划分是否清晰、是 否符合高内聚低耦合等等。

  code review 是一个很好的测验代码可读性的手段

-  **可扩展性（extensibility）**

  表示代码应对未来需求变化的能力。跟可读性一样，代码是否易扩展也很大程度上决定代码是否易维 护.

  代码的可扩展性表示，在不修改或少量修改原有代码的情况下，通过扩展的方式添加新的功能代码

-  **灵活性（flexibility）**

  如果一段代码易扩展、易复用或者易用，都可以称这段代码写得比较灵活

-  **简洁性（simplicity）**

   KISS ( Keep It Simple, Stupid)原则:尽量保持代码简单。代码简单、逻辑清晰，也就意味着易读、易维 护.

- **可复用性（reusability）**

  代码的可复用性可以简单地理解为，尽量减少重复代码的编写，复用已有的代码

- **可测试性（testability）**

  代码可测试性的好坏，能从侧面上非常准确地反应代码质量的好坏。代码的可测试性差，比较难写单元 测试，那基本上就能说明代码设计得有问题



#### 架构和集成

官方说明

```http
https://docs.sonarqube.org/8.9/architecture/architecture-integration/
https://docs.sonarqube.org/7.9/architecture/architecture-integration/
```

##### SonarQube 架构

**基于C/S结构**

SonarQube 四个主要组件

![image-20250228095849358](../markdown_img/image-20250228095849358.png)

-  SonarQube Server 包括三个主要部分
  - **Web Server**: UI 界面
  - **Search Server** :为UI提供搜索功能,基于 ElasticSearch 实现
  - **Compute Engine Server**：处理代码分析报告,并将之存储到 SonarQube Database
- **SonarQube Database**: 负责存储 SonarQube 的配置，以及项目的质量快照等
- **SonarQube Plugin**: 可以在 SonarQube Server 安装丰富的插件，实现支持各种开发语言、SCM、 集成、身份验证和治理等功能
- **Code analysis Scanners**: 代码扫描器,是SonarQube Server的客户端, 将代码扫描后得出报告提交 给 SonarQube Serve



##### SonarQube 生态集成

Sonar有两种使用方式：插件和客户端。

Sonar的插件名称为 sonarlint,实现支持多种开发工具的IDE的插件安装

![image-20250228102814644](D:\git_repository\cyber_security_learning\markdown_img\image-20250228102814644.png)





##### SonarQube 版本说明

SonarQube 分为: **社区版**,**开发版**,**企业版**和**数据中心版**

其中只有社区版是开源免费的

![image-20250228110002250](../markdown_img/image-20250228110002250.png)



**SonarQube 分两种版本: LTS 和非 LTS 版**

SonarQube 的 LTS (Long Term Support长期支持版本) 在其约 18 个月的生命周期内提供组织稳定性和 错误修复。

LTS 新版称为LTA Long Term Active version

生产建议使用 LTS 版

官方LTS版本说明

```http
https://www.sonarqube.org/downloads/lts/
```

各种版本下载

```http
https://www.sonarsource.com/products/sonarqube/downloads/historical-downloads/
https://www.sonarqube.org/downloads/
```

![image-20250228110426522](../markdown_img/image-20250228110426522.png)



#### 安装环境准备

##### 硬件要求

官方说明

```http
https://docs.sonarqube.org/latest/requirements/prerequisites-and-overview/
https://docs.sonarqube.org/8.9/requirements/requirements/
https://docs.sonarqube.org/7.9/requirements/requirements/
```

**硬件需求**

- 小型应用至少需要2GB的RAM
- 磁盘空间取决于SonarQube分析的代码量
- 必须安装在读写性能较好的磁盘, 存储数据的目录中包含ElasticSearch的索引,服务器启动并运行 时，将会在该索引上进行大是I/O操作
- 不支持32位操作系统



##### 系统内核优化

```http
https://docs.sonarqube.org/latest/requirements/prerequisites-and-overview/
```

**新版要求**

- `vm.max_map_count` is greater than or equal to 524288
- `fs.file-max` is greater than or equal to 131072
- the user running SonarQube can open at least 131072 file descriptors
- the user running SonarQube can open at least 8192 threads

You can set them dynamically for the current session by running the following commands as  root :

```bash
# mv.max_map_count 用于限制一个进程可以拥有的VMA(虚拟内存区域)的数量
sysctl -w vm.max_map_count=524288

# 设置系统最大打开的文件描述符数
sysctl -w fs.file-max=131072

# 每个用户可以打开的文件描述符数
ulimit -n 131072

# 每个用户可以打开的线程数
ulimit -u 8192
```

**持久化配置**

```bash
[root@mystical ~]# vim /etc/sysctl.conf
vm.max_map_count=524288
fs.file-max=131072

# 更改limits.conf之后，退出当前会话，重新进入
[root@mystical ~]# vim /etc/security/limits.conf
sonarqube  -  nofile  131072
sonarqube  -  nproc  8192
root  -  nofile  131072
root  -  nproc  8192
```



###### 知识点补充

**1️⃣ `nofile`（最大打开文件数）**

```bash
sonarqube  -  nofile  65536
```

📌 **作用**

- **`nofile` 指定用户能同时打开的最大文件描述符数量**

- 文件描述符（File Descriptor，FD）

   包括：

  - 打开的普通文件
  - 网络连接（Socket）
  - 管道（Pipe）

📌 **示例**

```bash
ulimit -n  # 查看当前用户的 `nofile` 限制
65536
```

📌 **影响**

- **如果 `nofile` 太小（如默认 `1024`），SonarQube 可能会报 `Too many open files` 错误**
- **提高 `nofile` 可以提升高并发时的性能**

**2️⃣ `nproc`（最大进程数）**

```bash
sonarqube  -  nproc  4096
```

📌 **作用**

- **`nproc` 指定用户可创建的最大进程数**
- **防止单个用户创建过多进程，导致系统资源耗尽**

📌 **示例**

```bash
ulimit -u  # 查看当前用户的 `nproc` 限制
4096
```

📌 **影响**

- **如果 `nproc` 过小（如默认 `1024`），SonarQube 可能无法正常启动**
- **增加 `nproc` 允许 SonarQube 运行更多线程，提高性能**

**3️⃣ `limits.conf` 详解**

`/etc/security/limits.conf` 用于**配置 Linux 资源限制**，格式：

```bash
<用户名>  <类型>  <限制项>  <值>
```

| **字段**        | **含义**                            | **示例**                          |
| --------------- | ----------------------------------- | --------------------------------- |
| **`sonarqube`** | 用户名                              | `sonarqube` 进程生效              |
| **`-`**         | `soft`（软限制）或 `hard`（硬限制） | `-` 代表同时设置 `soft` 和 `hard` |
| **`nofile`**    | 文件描述符限制                      | `65536`                           |
| **`nproc`**     | 进程数限制                          | `4096`                            |



**旧版要求** 

按官网说明修改配置

```http
https://docs.sonarqube.org/7.9/requirements/requirements/
```



##### 数据库环境依赖说明

SonarQube 7.9 以上版本的数据库要求

```http
https://docs.sonarqube.org/7.9/requirements/requirements/
```

注意：SonarQube 7.9 不再支持MySQL，可以选择安装 PostgreSQL

**官方如下说明**: 7.9.x 版本不再支持MySQL



#####  Java 环境依赖说明

SonarQube 9.9 以上版本的 java 环境要求

![image-20250228120802157](../markdown_img/image-20250228120802157.png)



**范例：安装 openjdk-17-jdk**

```bash
#Ubuntu安装java
[root@SonarQube-Server ~]#apt update && apt -y install openjdk-17-jdk
#RHEL系统安装java
[root@SonarQube-Server ~]#yum -y install java-17-openjdk
 
[root@mystical ~]$ java --version
openjdk 17.0.14 2025-01-21
OpenJDK Runtime Environment (build 17.0.14+7-Ubuntu-122.04.1)
OpenJDK 64-Bit Server VM (build 17.0.14+7-Ubuntu-122.04.1, mixed mode, sharing)
```



##### **创建SonarQube用户**

```bash
#使用普通账户启动sonarqube,因为sonarqube内置了ES，所以不允许能root启动
#Ubuntu使用useradd创建用户时默认使用/bin/sh,并且不创建家目录
[root@SonarQube-Server ~]# useradd -s /bin/bash -m sonarqube
```



#### 安装 SonarQube 服务器

##### 数据库准备

###### 安装和配置 PostgreSQL 数据库

```http
https://docs.sonarsource.com/sonarqube/latest/requirements/prerequisites-and-overview/
```

![image-20250228141609596](../markdown_img/image-20250228141609596.png)

##### 安装和配置 PostgreSQL

```bash
[root@mystical ~]# apt install -y postgresql

# 安装时自动生成用户postgres
[root@mystical ~]# id postgres 
uid=114(postgres) gid=120(postgres) groups=120(postgres),119(ssl-cert)

# 默认监听在127.0.0.1的5432端口，需要修改监听地址
[root@mystical ~]# ss -nltp|grep post
LISTEN 0      244        127.0.0.1:5432      0.0.0.0:*    users:(("postgres",pid=8400,fd=5)) 

#修改监听地址支持远程连接（如果sonarqube和PostgreSQL在同一台主机，可不做修改）
[root@mystical ~]#  vim /etc/postgresql/14/main/pg_hba.conf
host    all             all              0.0.0.0/0              scram-sha-256   # 旧版改为md5
[root@mystical /etc/postgresql/14/main]# vim postgresql.conf
listen_addresses = '*' 或者 '0.0.0.0'

# 重启 postgresql
[root@mystical ~]# systemctl restart postgresql
[root@mystical /etc/postgresql/14/main]$ ss -nltp|grep 5432
LISTEN 0      244          0.0.0.0:5432      0.0.0.0:*    users:(("postgres",pid=8805,fd=5))       
LISTEN 0      244             [::]:5432         [::]:*    users:(("postgres",pid=8805,fd=6))
```

说明: /etc/postgresql/1X/main/pg_hba.conf

```ABAP
格式:TYPE  DATABASE        USER            ADDRESS                 
METHOD
METHOD有如下值可选
md5： 执行MD5身份验证以验证用户的密码。
peer：从操作系统获取客户端的操作系统用户名，并检查它是否与请求的数据库用户名匹配。这仅适用于本地连接。
trust：允许无条件连接，允许任何PostgreSQL用户身份登录，而无需密码或任何其他身份验证。
reject：拒绝任何条件连接，这对于从组中“过滤掉”某些主机非常有用。
scram-sha-256：执行SCRAM-SHA-256身份验证以验证用户的密码。
password：要提供未加密的密码以进行身份••验证。由于密码是通过网络以明文形式发送的，因此不应在不受信任的网络上使用。
gss：使用GSSAPI对用户进行身份验证，这仅适用于TCP / IP连接。
sspi：使用SSPI对用户进行身份验证，这仅适用于Windows。
ident：通过联系客户端上的ident服务器获取客户端的操作系统用户名，并检查它是否与请求的数据库用户名匹配。 Ident身份验证只能用于TCP/IP连接。为本地连接指定时，将使用对等身份验证。
ldap：使用LDAP服务器进行身份验证。
radius：使用RADIUS服务器进行身份验证。
cert：使用SSL客户端证书进行身份验证。
pam：使用操作系统提供的可插入身份验证模块（PAM）服务进行身份验证。
bsd：使用操作系统提供的BSD身份验证服务进行身份验证。
```

##### 创建数据库和用户授权

```bash
#使用postgres用户登录（PostgresSQL安装后会自动创建postgres用户）
[root@mystical /etc/postgresql/14/main]# su - postgres

#登录postgresql数据库
postgres@mystical:~$ psql -U postgres
psql (14.15 (Ubuntu 14.15-0ubuntu0.22.04.1))
Type "help" for help.

#安全起见,修改数据库管理员postgres用户的密码,可选
postgres=# ALTER USER postgres WITH ENCRYPTED PASSWORD '123456';
ALTER ROLE

#创建用户和数据库并授权
postgres=# CREATE USER sonarqube WITH ENCRYPTED PASSWORD '123456';
CREATE ROLE
postgres=# CREATE DATABASE sonarqube OWNER sonarqube;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE sonarqube TO sonarqube;
GRANT
#前面如果已经指定数据库的OWNER,则可以不执行下面命令,可选
postgres=# ALTER DATABASE sonarqube OWNER TO sonarqube; 
ALTER DATABASE

#查看数据库是否创建,相当于MySQL中 show databases;
postgres=# \l
                                   List of databases
   Name    |   Owner   | Encoding |   Collate   |    Ctype    |    Access privileges    
-----------+-----------+----------+-------------+-------------+-------------------------
 postgres  | postgres  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 sonarqube | sonarqube | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/sonarqube          +
           |           |          |             |             | sonarqube=CTc/sonarqube
 template0 | postgres  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres            +
           |           |          |             |             | postgres=CTc/postgres
 template1 | postgres  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres            +
           |           |          |             |             | postgres=CTc/postgres
(4 rows)

#退出数据库连接
postgres=# \q
```



##### 下载 SonarQube 和修改配置文件

###### **下载解压缩**

下载链接

```http
https://www.sonarqube.org/downloads/
```

![image-20250228143857745](D:\git_repository\cyber_security_learning\markdown_img\image-20250228143857745.png)

```bash
# 9.9.8版下载
[root@mystical ~]# wget -P /usr/local/src https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.9.8.100196.zip

# 解压
[root@mystical ~]# unzip /usr/local/src/sonarqube-9.9.8.100196.zip

# 新版
[root@mystical ~]# unzip /usr/local/src/sonarqube-9.9.8.100196.zip
[root@mystical ~]# ln -s /usr/local/src/sonarqube-9.9.8.100196 /usr/local/sonarqube

# 查看
[root@mystical /usr/local]# ls /usr/local/sonarqube
bin   COPYING  dependency-license.json  extensions  logs  web
conf  data     elasticsearch            lib         temp

# 设置属性
[root@mystical /usr/local]# chown -R sonarqube.sonarqube /usr/local/sonarqube/
```



##### 设置 SonarQube 连接数据库

```bash
#修改SonarQube配置用于连接postgresql数据库
[root@SonarQube-Server ~]#vim /usr/local/sonarqube/conf/sonar.properties 
#修改连接postgresql数据库的账号和密码,和前面的配置必须匹配
sonar.jdbc.username=sonarqube
sonar.jdbc.password=123456

#修改数据库相关的信息，这里必须和此前配置的postgresql内容相匹配，其中localhost为DB服务器的地址，而sonarqube为数据库名称
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
# 默认配置如下：
##sonar.jdbc.url=jdbc:oracle:thin:@localhost:1521/XE

#设置 SonarQube 的提供的 Web Server监听的地址和端口,可选
sonar.web.host=0.0.0.0 #此为默认值,可不做修改
sonar.web.port=9000    #此为默认值,可不做修改

#按需要修改SonarQube存储数据的目录位置，以下两个目录为相对路径，相对于sonarqube的安装目录，也可以使用绝对路径
sonar.path.data=data  #默认值,可不做修改
sonar.path.temp=temp  #默认值,可不做修改
```



##### 启动 SonarQube

注意:SonarQube 需要调用 Elasticsearch，而且默认需要使用普通用户启动，如果以root启动会报错

范例: 以sonarqube用户身份启动

```bash
[root@SonarQube-Server ~]#su - sonarqube -c '/usr/local/sonarqube/bin/linux-x86-64/sonar.sh  start'
```



##### 创建 service 文件

官网参考

```http
https://docs.sonarsource.com/sonarqube/latest/setup-and-upgrade/configure-and-operate-a-server/operating-the-server/
https://docs.sonarqube.org/8.9/setup/operate-server/
https://docs.sonarqube.org/7.9/setup/operate-server/
```

范例: 创建 service 文件

```bash
# 创建service文件
[root@SonarQube-Server ~]#vim  /etc/systemd/system/sonarqube.service
[Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=simple
User=sonarqube
Group=sonarqube
PermissionsStartOnly=true
ExecStart=/usr/bin/nohup /usr/bin/java -Xms32m -Xmx32m -Djava.net.preferIPv4Stack=true -jar /usr/local/sonarqube/lib/sonar-application-9.9.8.100196.jar
#ExecStart=/usr/bin/nohup /usr/bin/java -Xms32m -Xmx32m-Djava.net.preferIPv4Stack=true -jar  /usr/local/sonarqube/lib/sonar-application-7.9.6.jar
StandardOutput=syslog
LimitNOFILE=65536
LimitNPROC=4096
TimeoutStartSec=5
Restart=always

[Install]
WantedBy=multi-user.target

[root@mystical ~]# systemctl daemon-reload 
[root@mystical ~]# systemctl enable --now sonarqube.service 
Created symlink /etc/systemd/system/multi-user.target.wants/sonarqube.service → /etc/systemd/system/sonarqube.service.
[root@mystical ~]# systemctl status sonarqube.service
```



#### 登录到 Web 界面

用浏览器访问地址：` http://SonarQube服务器IP:9000`

```ABAP
新版默认必须登录,不支持匿名访问
默认用户名和密码都是 admin
```

![image-20250228151954515](../markdown_img/image-20250228151954515.png)

首次登录必须修改admin用户的密码

```ABAP
注意: 新密码不能使用原密码
```

![image-20250228152203063](../markdown_img/image-20250228152203063.png)

![image-20250228152313536](../markdown_img/image-20250228152313536.png)



#### 管理 SonarQube 服务器

##### 安装中文支持

**查看本地已安装插件**

插件本地路径用于安装相关插件,比如: 中文插件,用于分析不同开发语言的对应的插件

```bash
#初始此目录没有插件文件 
[root@SonarQube-Server ~]#ll /usr/local/sonarqube/extensions/plugins/
total 12
drwxr-xr-x 2 sonarqube sonarqube 4096 Jul 27 06:27 ./
drwxr-xr-x 5 sonarqube sonarqube 4096 Oct 24 09:59 ../
-rw-r--r-- 1 sonarqube sonarqube  737 Jul 27 06:27 README.txt
```

**安装中文语言插件**

`administration- Marketplace`，在后面的搜索框搜索插件chinese，然后点install安装：

**新版需要先理解风险,才能安装插件**

![image-20250228153146191](../markdown_img/image-20250228153146191.png)

![image-20250228153345226](../markdown_img/image-20250228153345226.png)

![image-20250228153552581](../markdown_img/image-20250228153552581.png)

![image-20250228153749887](../markdown_img/image-20250228153749887.png)

![image-20250228153940307](../markdown_img/image-20250228153940307.png)

安装完后,点 `Restart Server`

![image-20250228154942053](D:\git_repository\cyber_security_learning\markdown_img\image-20250228154942053.png)

重新登陆

![image-20250228155042113](../markdown_img/image-20250228155042113.png)

查看到多了一个插件文件

```bash
[root@mystical /usr/local/sonarqube]# ls extensions/plugins/
README.txt  sonar-l10n-zh-plugin-9.9.jar
```

查看安装的插件

![image-20250228155244376](../markdown_img/image-20250228155244376.png)



##### 权限管理

###### 允许匿名访问

新版默认取消了匿名用户访问,可以在下面配置中打开匿名访问即关闭认证

![image-20250228161321999](../markdown_img/image-20250228161321999.png)

![image-20250228161350624](../markdown_img/image-20250228161350624.png)

关闭开关并保存

![image-20250228161457795](../markdown_img/image-20250228161457795.png)

![image-20250228161840387](../markdown_img/image-20250228161840387.png)



###### 不允许匿名访问

如果不允许匿名访问,就需要给 Jenkins 创建访问sonarqube 所使用的用户的访问令牌

可以创建新用户或使用默认的admin用户

**新建用户并授权**

- 在SonarQube上创建用户账号（不建议使用admin账号）

  配置 →权限 →用户

- 为用户账号赋予相应的权限，例如执行分析和置备项目

  配置 →权限 →全局权限



###### **对 admin用户创建token**

![image-20250228162629071](../markdown_img/image-20250228162629071.png)

![image-20250228162919620](../markdown_img/image-20250228162919620.png)

![image-20250228162948298](../markdown_img/image-20250228162948298.png)



###### **创建新用户并授权**

![image-20250228163657917](../markdown_img/image-20250228163657917.png)

![image-20250228163854919](../markdown_img/image-20250228163854919.png)

生成令牌 token

![image-20250228163948961](../markdown_img/image-20250228163948961.png)

![image-20250228164049850](../markdown_img/image-20250228164049850.png)

```ABAP
token: squ_7defee030c19a5bb79053067e5efeee7aacbb5c6
```

 给Jenkins用户授权

![image-20250228164403462](../markdown_img/image-20250228164403462.png)

使用 jenkins 用户登陆

![image-20250228164744963](../markdown_img/image-20250228164744963.png)



#### 部署代码扫描器 sonar-scanner

sonar-scanner 是基于Java 实现的客户端工具，负责扫描源代码，并提交结果给Sonarqube Server

官方文档

```http
https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/
```

![image-20250228165558325](../markdown_img/image-20250228165558325.png)

##### 在 Jenkins 服务器部署和配置 sonar-scanner

sonarqube 通过调用扫描器sonar-scanner进行代码质量分析，即扫描器的具体工作就是扫描代码

###### sonar-scanner 安装方法1：手动下载安装

新版下载链接

```http
https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/
```

![image-20250228170052006](../markdown_img/image-20250228170052006.png)

###### 下载并配置

通过这个配置，告知扫描器，将扫描的内容发给指定的服务端

```bash
# 因为是要扫描Jenkins拉取的代码，因此sonar scanner部署在Jenkins所在服务器上
[root@mystical ~]# wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-7.0.2.4839-linux-x64.zip

# 解压
[root@mystical /usr/local]# unzip sonar-scanner-cli-7.0.2.4839-linux-x64.zip -d /usr/local/
[root@mystical /usr/local]# ln -s /usr/local/sonar-scanner-7.0.2.4839-linux-x64 /usr/local/sonar-scanner

# 查看版本，内置java，无需单独安装java
[root@mystical /usr/local]# /usr/local/sonar-scanner/jre/bin/java --version
openjdk 17.0.13 2024-10-15
OpenJDK Runtime Environment Temurin-17.0.13+11 (build 17.0.13+11)
OpenJDK 64-Bit Server VM Temurin-17.0.13+11 (build 17.0.13+11, mixed mode, sharing)

# 配置sonar-scanner连接sonarqube服务器
[root@mystical /usr/local]# vim /usr/local/sonar-scanner/conf/sonar-scanner.properties
sonar.host.url=http://172.22.200.103:9000
sonar.sourceEncoding=UTF-8 
# sonar.login=jenkins
# sonar.password=123456
# 密码方式未来会淘汰
# 建议使用Token方式
sonar.login=squ_7defee030c19a5bb79053067e5efeee7aacbb5c6
```



#### 准备测试代码和配置文件

 sonar-scanner 扫描的代码需要提前在项目的根目录下准备名称为sonar-project.properties的文件，内容如下

```bash
# must be unique in a given SonarQube instance,此为必须项
sonar.projectKey=my:project   # 这一项唯一的表示了scanner扫描的是哪个项目，此项必须唯一

# --- optional properties --

# defaults to project key
#sonar.projectName=My project
# defaults to 'not provided'
#sonar.projectVersion=1.0

# Path is relative to the sonar-project.properties file. Defaults to .
#sonar.sources=.

# Encoding of the source code. Default is default system encoding
#sonar.sourceEncoding=UTF-8
```

测试代码下载

```bash
[root@mystical ~]# wget https://www.mysticalrecluse.com/script/tools/sonar-examples-master.zip
[root@mystical ~]# unzip sonar-examples-master.zip -d /opt/

# 目录下是很多语言的sonarqube的测试代码
# 在包含sonar-project.properties的同级目录下，直接执行sonar-scanner
[root@mystical /opt/sonar-examples-master/projects/languages/php/php-sonar-runner]# ls
README.md  sonar-project.properties  src  validation.txt
[root@mystical /opt/sonar-examples-master/projects/languages/php/php-sonar-runner]# /usr/local/sonar-scanner/bin/sonar-scanner

# 执行后，将结果发给sonarqube服务端，观察服务端
```

![image-20250228205931497](../markdown_img/image-20250228205931497.png)

```bash
# 也可以不使用sonar-project.properties文件的值，而是直接在命令行赋值
[root@jenkins spring-boot-helloWorld]#sonar-scanner -Dsonar.projectName=myapp -Dsonar.projectKey=myapp 

# 执行后，观察服务端结果，项目名称是自定义的myapp，作为了一个新项目。
```

![image-20250228210612819](../markdown_img/image-20250228210612819.png)

点击进入项目，可以发现有25个异味

![image-20250228210737781](../markdown_img/image-20250228210737781.png)

查看异味具体内容

![image-20250228210833199](../markdown_img/image-20250228210833199.png)

![image-20250228210919616](../markdown_img/image-20250228210919616.png)

##### 扫描 Java 项目

```ABAP
扫描 java 项目和其他语言有所不同，不能只指定sonar.projectKey，还必须额外指定sonar.java.binaries的值
```

**示例**

```bash
[root@mystical ~/project/helloworld-spring-boot]# /usr/local/sonar-scanner/bin/sonar-scanner -Dsonar.projectName=helloworld -Dsonar.projectKey=helloworld -Dsonar.java.binaries=./

# 执行后，查看server端的项目
```

![image-20250228212229579](../markdown_img/image-20250228212229579.png)



#### SonarQube 质量阈

质量阙是一组预定义的评估条件

代码质量扫描结果可满足这组条件时,项目才会被标记为“passed”

管理员也可以在SonarQube上按需自定义并调用质量阈



##### 新建质量域

![image-20250228212758934](../markdown_img/image-20250228212758934.png)

![image-20250228212851004](../markdown_img/image-20250228212851004.png)

解锁编辑后，即可自定义质量域条件

![image-20250228213034795](../markdown_img/image-20250228213034795.png)

解锁后，为了测试（让代码检测失败），添加一个条件

![image-20250228213307530](../markdown_img/image-20250228213307530.png)

![image-20250228214426061](../markdown_img/image-20250228214426061.png)

将test条件作为默认的质量域使其生效

![image-20250228213715330](../markdown_img/image-20250228213715330.png)

再次提交代码测试

```bash
[root@mystical ~/project/helloworld-spring-boot]# /usr/local/sonar-scanner/bin/sonar-scanner -Dsonar.projectName=helloworld -Dsonar.projectKey=helloworld -Dsonar.java.binaries=./

# 代码检测结果，如下查看server端项目
```

![image-20250228214601350](../markdown_img/image-20250228214601350.png)



#### Jenkins 和 SonarQube 集成实现代码扫描

##### Jenkins 和 SonarQube 集成说明

![image-20250228222134414](../markdown_img/image-20250228222134414.png)

Jenkins借助于SonarQube Scanner插件将SonarQube提供的代码质量检查能力集成到pipeline上,从而确保质量阈检查失败时，能够避免继续进行后续的操作，例如发布等

**通常的流程如下**

- Jenkins Pipeline启动
- SonarQube Scanner分析代码,并将报告发送至SonarQubeServe
- SonarQube Server分析代码检测的结果是否符合预定义的质量阈
- SonarQube Server将通过(passed)或者失败（failed)的结果发送回Jenkins上的SonarQube  Scanner插件暴露的 Webhook
- 质量阈相关的阶段成功通过或可选地失败时Jenkins pipeline继续后面的Stage,否则pipeline将终止 4.6.2 SonarQube 质量阈



####  案例: 基于 PipeLine 实现 JAVA项目集成 SonarQube 代码检测通知 Jenkins(推荐)

![image-20250301221807591](../markdown_img/image-20250301221807591.png)