# 实验1：Gitlab部署

## GitLab 包安装

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
-  **Source**：源码安装，在GitLab没有提供适用的安装包的平台上（例如各类BSD系统）只能采用这种安装方式
-  **Docker**：Docker 容器化的极狐GitLab 软件包
-  **GitLab Operator**：Kubernetes Operator风格的部署模式
-  **Helm Chart**：用于在 Kubernetes 上安装极狐GitLab 及其所有组件的云原生 Helm chart
-  **GitLab Environment Toolkit（GET）**：自动化工具集，用于在主流的公有云（Azure、GCP和 AWS）上部署GitLab 



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

![image-20250206121909398](D:\git_repository\cyber_security_learning\markdown_img\image-20250206121909398-1755487531855-1.png)

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

![image-20250206125844241](D:\git_repository\cyber_security_learning\markdown_img\image-20250206125844241-1755487531856-2.png)



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



#### 在浏览器访问GitLab

在新版gitlab中第一次登录的界面发生变化,取消重设密码界面,需要直接输入用户和密码才能登录

**默认用户为root，其密码是随机生成**

![image-20250208154751291](D:\git_repository\cyber_security_learning\markdown_img\image-20250208154751291-1755487568776-5.png)

```bash
# 初始账号为root
# 初始密码为配置文件自行指定的密码
```

![image-20250208155656668](D:\git_repository\cyber_security_learning\markdown_img\image-20250208155656668-1755487568776-6.png)







## 基于 Kubernetes 安装 GitLab

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



![image-20250208125113586](D:\git_repository\cyber_security_learning\markdown_img\image-20250208125113586-1755487674940-9.png)

```bash
# 默认账号：root
# 初始密码：执行下列指令
[root@master1 ~]# kubectl get secret -n gitlab-system gitlab-gitlab-initial-root-password -o jsonpath="{.data.password}" | base64 --decode
mKycBGLxob511Rq2VopJ51URSWdphI7qVHass9t74LoZiglxdmMKSgrCUPkIAFS2	
```

![image-20250208125336856](D:\git_repository\cyber_security_learning\markdown_img\image-20250208125336856-1755487674940-10.png)

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

![image-20250208125839659](D:\git_repository\cyber_security_learning\markdown_img\image-20250208125839659-1755487674940-11.png)

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

![image-20250208130235955](D:\git_repository\cyber_security_learning\markdown_img\image-20250208130235955-1755487674940-12.png)



**在Kubernetes部署好GitLab后，查看资源情况**

![image-20250208133202056](D:\git_repository\cyber_security_learning\markdown_img\image-20250208133202056-1755487674940-14.png)



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

![image-20250208153458322](D:\git_repository\cyber_security_learning\markdown_img\image-20250208153458322-1755487674940-13.png)









# 实验2：GitLab 的数据备份和恢复



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





# 实验3：Gitlab实现HTTPS



itLab 如果用于不安全的网络，建议使用 https

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







# 实验4：Jenkins部署

## 安装前环境准备

**系统要求**

```http
https://www.jenkins.io/doc/administration/requirements/java/
```

最低推荐配置

- 256MB可用内存
- 1GB可用磁盘空间(作为一个Docker容器运行jenkins的话推荐10GB)

为小团队推荐的硬件配置

-  1GB+可用内存
-  50 GB+ 可用磁盘空间

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



## Jenkins 包安装

注意：新版jenkins_2.401.2启动很慢，可能需要20分钟才能启动成功

##### 二进制包安装 Jenkins

```http
https://mirrors.tuna.tsinghua.edu.cn/jenkins/debian-stable/
```

![image-20250216154954145](D:\git_repository\cyber_security_learning\markdown_img\image-20250216154954145-1755487937353-21.png)

安装过程

```bash
# 下载java17, Jenkins 2.492.1 版本需要 Java 17 或 21
# 选择版本下载并安装
[root@mystical /var/lib]# apt install -y openjdk-17-jdk

# 下载并安装jenkins_2.492.1_all.deb
[root@mystical ~]# wget https://mirrors.tuna.tsinghua.edu.cn/jenkins/debian-stable/jenkins_2.492.1_all.deb
[root@mystical ~]# dpkg -i jenkins_2.492.1_all.deb
```



## 基于 Kubernetes 部署 Jenkins

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



## 首次登录 Jenkins页面初始化

用浏览器访问： http://jenkins.mystical.org:8080/

默认内置用户admin，其密码为随机字符，可以从如下文件中查到密码

![image-20250212211710297](D:\git_repository\cyber_security_learning\markdown_img\image-20250212211710297-1755487937353-24.png)

```bash
# 查看密码
[root@master1 jenkins]#kubectl exec -it -n jenkins jenkins-5dd956745f-vmdjc -- /bin/bash
jenkins@jenkins-5dd956745f-vmdjc:~/secrets$ cd /var/jenkins_home/secrets/
jenkins@jenkins-5dd956745f-vmdjc:~/secrets$ cat initialAdminPassword 
8a5e445090f1412a89f857831a2258ae
```



**离线状态**

![image-20250216142300508](D:\git_repository\cyber_security_learning\markdown_img\image-20250216142300508-1755487937353-22.png)

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

![image-20250212212328405](D:\git_repository\cyber_security_learning\markdown_img\image-20250212212328405-1755487937353-25.png)

![image-20250212214309954](D:\git_repository\cyber_security_learning\markdown_img\image-20250212214309954-1755487937353-23.png)

**建议选择无**

![image-20250212214434396](D:\git_repository\cyber_security_learning\markdown_img\image-20250212214434396-1755487937353-28.png)

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

![image-20250216145627814](D:\git_repository\cyber_security_learning\markdown_img\image-20250216145627814-1755487937353-26.png)



#### 配置 Jenkins URL

保存完成即可

![image-20250216145654161](D:\git_repository\cyber_security_learning\markdown_img\image-20250216145654161-1755487937353-27.png)

![image-20250216145826296](D:\git_repository\cyber_security_learning\markdown_img\image-20250216145826296-1755487937353-29.png)

![image-20250216145845607](D:\git_repository\cyber_security_learning\markdown_img\image-20250216145845607-1755487937353-30.png)







# 实验5：配置 Jenkins 结合 GitLab 实现自动化前端项目的部署和回滚



##  Jenkins 创建任务

![image-20250217164331078](D:\git_repository\cyber_security_learning\markdown_img\image-20250217164331078-1755488241484-41.png)





## 配置 Git 项目地址和凭证

![image-20250217164408642](D:\git_repository\cyber_security_learning\markdown_img\image-20250217164408642-1755488241484-42.png)



## 准备脚本并加入构建任务

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

![image-20250218091936057](D:\git_repository\cyber_security_learning\markdown_img\image-20250218091936057-1755488241484-48.png)

![image-20250218091957718](D:\git_repository\cyber_security_learning\markdown_img\image-20250218091957718-1755488241484-44.png)

查看控制台输出

![image-20250218092020644](D:\git_repository\cyber_security_learning\markdown_img\image-20250218092020644-1755488241484-43.png)



## 服务器验证数据

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

![image-20250218093456929](D:\git_repository\cyber_security_learning\markdown_img\image-20250218093456929-1755488241484-45.png)





## 修改代码再上传重新构建

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

![image-20250218100753510](D:\git_repository\cyber_security_learning\markdown_img\image-20250218100753510-1755488241484-46.png)





## 实现版本回滚任务

新建任务如下,实现回滚功能

![image-20250218101055995](D:\git_repository\cyber_security_learning\markdown_img\image-20250218101055995-1755488241484-47.png)

只修改构建的shell部分,其它不变

![image-20250218101215004](D:\git_repository\cyber_security_learning\markdown_img\image-20250218101215004-1755488241484-49.png)

![image-20250218101232842](D:\git_repository\cyber_security_learning\markdown_img\image-20250218101232842-1755488241484-51.png)

执行任务后,可以查看到 Web页面是否还原为上一个版本

![image-20250218102553543](D:\git_repository\cyber_security_learning\markdown_img\image-20250218102553543-1755488241484-50.png)







# 实验6：实现 Java 应用源码编译并部署



java 程序需要使用构建工具,如: maven,ant,gradle等进行构建打包才能部署,其中**maven**比较流行

以下以 maven 为例实现 Java 应用部署



## 自由风格的任务构建基于 Spring Boot 的 JAR 包部署 JAVA 项目

### Gitlab导入项目

项目链接

```http
https://gitee.com/lbtooth/helloworld-spring-boot
```

![image-20250218144012874](D:\git_repository\cyber_security_learning\markdown_img\image-20250218144012874-1755488420778-63.png)



### Jenkins 服务器上安装 maven 和配置镜像加速

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



### 准备相关脚本

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



### 创建 Jenkins 任务

![image-20250219154044944](D:\git_repository\cyber_security_learning\markdown_img\image-20250219154044944-1755488420778-66.png)

![image-20250219154128825](D:\git_repository\cyber_security_learning\markdown_img\image-20250219154128825-1755488420778-65.png)



### 构建并检查结果

![image-20250219160350420](D:\git_repository\cyber_security_learning\markdown_img\image-20250219160350420-1755488420778-64.png)

![image-20250219160416294](D:/git_repository/cyber_security_learning/markdown_img/image-20250219160416294.png)

![image-20250219160521103](D:\git_repository\cyber_security_learning\markdown_img\image-20250219160521103-1755488420778-67.png)

![image-20250219160540684](D:\git_repository\cyber_security_learning\markdown_img\image-20250219160540684-1755488420778-69.png)







## 自由风格的任务构建单体的 Java 应用到Tomcat服务

```ABAP
注意：此项目使用JDK-11，不支持JDK-17
```



### Gitlab仓库中准备 Java 代码

**在gitlab新建 java 项目**

```http
https://gitee.com/lbtooth/hello-world-war.git
```

**导入项目**

![image-20250221160046639](D:\git_repository\cyber_security_learning\markdown_img\image-20250221160046639-1755488420778-72.png)

![image-20250221160205323](D:/git_repository/cyber_security_learning/markdown_img/image-20250221160205323.png)





### 临时切换 java11 版本

```bash
[root@mystical /data/jenkins/script]# export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
[root@mystical /data/jenkins/script]# export PATH=$JAVA_HOME/bin:$PATH
```



### Server服务器上，安装tomcat

```bash
[root@mystical ~]# apt install -y tomcat9
```



### 准备相关脚本

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

![image-20250221180800840](D:\git_repository\cyber_security_learning\markdown_img\image-20250221180800840-1755488420778-70.png)



![image-20250221180822036](D:\git_repository\cyber_security_learning\markdown_img\image-20250221180822036-1755488420778-71.png)





### 执行构建后查看效果

![](D:\git_repository\cyber_security_learning\markdown_img\image-20250221180910711-1755488420778-73.png)

# 实验7：实现 Golang 应用源码编译并部署

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

![image-20250222095526522](D:\git_repository\cyber_security_learning\markdown_img\image-20250222095526522-1755488634190-89.png)

![image-20250222095606814](D:\git_repository\cyber_security_learning\markdown_img\image-20250222095606814-1755488634190-90.png)

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

![image-20250222100121501](D:\git_repository\cyber_security_learning\markdown_img\image-20250222100121501-1755488634190-94.png)

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

![image-20250222101223993](D:\git_repository\cyber_security_learning\markdown_img\image-20250222101223993-1755488634190-91.png)

![image-20250222101342798](D:\git_repository\cyber_security_learning\markdown_img\image-20250222101342798-1755488634190-96.png)

![image-20250222101352413](D:\git_repository\cyber_security_learning\markdown_img\image-20250222101352413-1755488634190-92.png)

![image-20250222101411136](D:\git_repository\cyber_security_learning\markdown_img\image-20250222101411136-1755488634190-93.png)



![image-20250222102425510](D:\git_repository\cyber_security_learning\markdown_img\image-20250222102425510-1755488634190-95.png)

![image-20250222103225178](D:\git_repository\cyber_security_learning\markdown_img\image-20250222103225178.png)







# 实验8：集成 Ansible 的任务构建

#### 

![image-20250222103330422](D:\git_repository\cyber_security_learning\markdown_img\image-20250222103330422-1755488871284-105.png)



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

![image-20250222104213568](D:\git_repository\cyber_security_learning\markdown_img\image-20250222104213568-1755488871284-106.png)

安装插件后，添加了ansible的构建步骤

![image-20250222104602641](D:\git_repository\cyber_security_learning\markdown_img\image-20250222104602641-1755488871284-109.png)

##### 使用 Ansible Ad-Hoc 实现任务

![image-20250222105143430](D:\git_repository\cyber_security_learning\markdown_img\image-20250222105143430-1755488871284-121.png)



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

![image-20250222112353806](D:\git_repository\cyber_security_learning\markdown_img\image-20250222112353806-1755488871284-107.png)



**保存构建后**

![image-20250222112422185](D:\git_repository\cyber_security_learning\markdown_img\image-20250222112422185-1755488871284-108.png)



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

![image-20250222130005269](D:\git_repository\cyber_security_learning\markdown_img\image-20250222130005269-1755488871284-110.png)

![image-20250222130242957](D:\git_repository\cyber_security_learning\markdown_img\image-20250222130242957-1755488871284-111.png)

![image-20250222130030705](D:\git_repository\cyber_security_learning\markdown_img\image-20250222130030705-1755488871284-112.png)

![image-20250222130816616](D:\git_repository\cyber_security_learning\markdown_img\image-20250222130816616-1755488871284-113.png)



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

![image-20250222133953392](D:\git_repository\cyber_security_learning\markdown_img\image-20250222133953392-1755488871284-114.png)

**添加第二个选项参数**

![image-20250222134023497](D:\git_repository\cyber_security_learning\markdown_img\image-20250222134023497-1755488871284-115.png)

![image-20250222134253048](D:\git_repository\cyber_security_learning\markdown_img\image-20250222134253048-1755488871284-116.png)

**点"高级"添加ansible的变量,添加Ansible Playbook的变量**

![image-20250222134411643](D:\git_repository\cyber_security_learning\markdown_img\image-20250222134411643-1755488871284-117.png)

![image-20250222134558674](D:\git_repository\cyber_security_learning\markdown_img\image-20250222134558674-1755488871284-118.png)

- key 是 ansible里定义的变量名
- Value 是 Jenkins 里的变量名
- 然后通过选项可以指定value的值

![image-20250222135414424](D:\git_repository\cyber_security_learning\markdown_img\image-20250222135414424-1755488871284-119.png)

![image-20250222135350536](D:\git_repository\cyber_security_learning\markdown_img\image-20250222135350536-1755488871284-120.png)





# 实验9：实现邮件通知

## 使用 mailer 实现邮件通知

Mailer 和 Email Extension 插件都可以实现邮件通知功能

###### 准备告警邮箱配置

生成邮箱登录授权码，可以使用QQ或163邮箱等

###### mailer 插件实现邮件告警

**安装mailer插件**

先安装mailer插件后才可以显示和配置发件配置信息

注意: 安装 Gitlab插件会因为依赖关系自动安装mailer插件

![image-20250222141016139](D:\git_repository\cyber_security_learning\markdown_img\image-20250222141016139-1755488937052-139.png)

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

![image-20250222141544314](D:\git_repository\cyber_security_learning\markdown_img\image-20250222141544314-1755488937052-140.png)

![image-20250222141959867](D:\git_repository\cyber_security_learning\markdown_img\image-20250222141959867-1755488937052-141.png)



###### 配置任务的构建后通知

```ABAP
注意:Jenkins-2.426.2选中和不选中效果一样
```

选中“每次不稳定的构建都发送邮件通知”，表示只有失败构建时才会发邮件通知

如果不选中，表示当失败或者从失败变为成功切换时都会通知，但总是成功不会通知

Recipients 支持多个收信人的邮件地址，空格隔开即可

![image-20250222142436740](D:\git_repository\cyber_security_learning\markdown_img\image-20250222142436740-1755488937052-144.png)

![image-20250222142405512](D:\git_repository\cyber_security_learning\markdown_img\image-20250222142405512-1755488937052-142.png)

###### 执行任务验证结果

默认“每次不稳定的构建都发送邮件通知”选中，表示当任务执行失败时才会收邮件

不选中”每次不稳定的构建都发送邮件通知“，表示当失败或者从失败变为成功切换时都会通知，但总是 成功不会通知

![image-20250222142609139](D:\git_repository\cyber_security_learning\markdown_img\image-20250222142609139-1755488937052-143.png)

![image-20250222142745234](D:\git_repository\cyber_security_learning\markdown_img\image-20250222142745234-1755488937052-145.png)





## 使用 Email Extension 插件实现邮件通知

Email Extension 插件比Mailer插件的功能更加丰富

说明

```http
https://www.jenkins.io/doc/pipeline/steps/email-ext/#emailext-extended-email
https://plugins.jenkins.io/email-ext
```

######  安装插件 Email Extension

![image-20250222143038988](D:\git_repository\cyber_security_learning\markdown_img\image-20250222143038988-1755488937052-146.png)

###### 配置 Email Extension

系统管理-- 系统配置 -- Jenkins Location -- 系统管理员邮件地址

```ABAP
注意：此处必须配置发件人邮箱和下面Extended E-mail Notification 的一致
```

![image-20250222143959169](D:\git_repository\cyber_security_learning\markdown_img\image-20250222143959169-1755488937052-147.png)

**添加认证**

![image-20250222144241480](D:\git_repository\cyber_security_learning\markdown_img\image-20250222144241480-1755488937052-148.png)



![image-20250222144355710](D:\git_repository\cyber_security_learning\markdown_img\image-20250222144355710-1755488937052-150.png)

**设置各种邮件通知的触发器条件**

![image-20250222144551934](D:\git_repository\cyber_security_learning\markdown_img\image-20250222144551934-1755488937052-149.png)

![image-20250222144632526](D:\git_repository\cyber_security_learning\markdown_img\image-20250222144632526-1755488937052-151.png)

###### 在任务中使用邮件通知

**在构建后操作选择**

![image-20250222144807957](D:\git_repository\cyber_security_learning\markdown_img\image-20250222144807957-1755488937052-152.png)

**![image-20250222144952098](D:\git_repository\cyber_security_learning\markdown_img\image-20250222144952098-1755488937052-154.png)**

**默认只有失败才会发送通知，修改为总是发送给收件人Always**

![image-20250222145209521](D:\git_repository\cyber_security_learning\markdown_img\image-20250222145209521-1755488937052-155.png)

![image-20250222145257796](D:\git_repository\cyber_security_learning\markdown_img\image-20250222145257796-1755488937052-153.png)

**执行构建后，收到邮件**

![image-20250222145338071](D:\git_repository\cyber_security_learning\markdown_img\image-20250222145338071.png)



# 实验10：自动化构建

- **周期性定时构建**
- **Webhook 触发构建**



## 定时和 SCM 构建

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

![image-20250222151941655](D:\git_repository\cyber_security_learning\markdown_img\image-20250222151941655-1755489161350-175.png)



![image-20250222152043085](D:\git_repository\cyber_security_learning\markdown_img\image-20250222152043085-1755489161349-173.png)

```ABAP
注意：SCM任务会在左侧多出一个“Git 轮询日志”，可以看到轮询的记录信息
观察Git 轮询日志可以看到当有变化时才会构建,否则不会执行构建
```

![image-20250222152228871](D:\git_repository\cyber_security_learning\markdown_img\image-20250222152228871-1755489161350-178.png)





## 构建 Webhook 触发器

构建触发器(webhook)，也称为钩子，**实际上是一个HTTP回调**，其用于在开发人员向gitlab提交代码后 能够触发jenkins自动执行代码构建操作。

**常见场景:**

只有在开发人员向develop分支提交代码的时候会自动触发代码构建和部署至测试环境，而向主分支提 交的代码不会自动构建，需要运维人员手动部署代码到生产环境。

![image-20250222152502473](D:\git_repository\cyber_security_learning\markdown_img\image-20250222152502473-1755489161350-176.png)

**多种方式实现 Webhook 触发构建**

- 触发远程构建: 此方式无需安装插件
- Build when a change is pushed to GitLab. GitLab webhook URL: 需要安装Gitlab插件
- Generic Webhook Trigger : 需要安装 Generic Webhook Trigger Plugin 插件



###### **触发远程构建**

Jenkins配置构建 Webhook 触发器

![image-20250222155325828](D:\git_repository\cyber_security_learning\markdown_img\image-20250222155325828-1755489161350-174.png)

这里的触发路径为

```bash
JENKINS_URL/job/trigger1-demo1/build?token=TOKEN_NAME 或者 /buildWithParameters?token=TOKEN_NAME

# 其中JENKINS_URL的值为http://172.22.200.222:8080/
# 所以拼出来的最终URL为

http://172.22.200.222:8080/job/trigger1-demo1/build?token=123456
```

![image-20250222155601674](D:\git_repository\cyber_security_learning\markdown_img\image-20250222155601674-1755489161350-177.png)

![image-20250222155348764](D:\git_repository\cyber_security_learning\markdown_img\image-20250222155348764-1755489161350-179.png)

保存后，访问`http://172.22.200.222:8080/job/trigger1-demo1/build?token=123456`

```bash
#如果执行正常，则无任何显示
[root@mystical /tmp]# curl http://172.22.200.222:8080/job/trigger1-demo1/build?token=12345

# 触发构建
```

```ABAP
注意：这里之所以直接成功，是因为测试的服务器和Jenkins所在服务器，打通了ssh验证
```



![image-20250222160244159](D:\git_repository\cyber_security_learning\markdown_img\image-20250222160244159-1755489161350-180.png)

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

![image-20250222161429574](D:\git_repository\cyber_security_learning\markdown_img\image-20250222161429574-1755489161350-181.png)



![image-20250222161444100](D:\git_repository\cyber_security_learning\markdown_img\image-20250222161444100-1755489161350-182.png)

![image-20250222161526818](D:\git_repository\cyber_security_learning\markdown_img\image-20250222161526818-1755489161350-183.png)

```bash
# 此时直接使用新创建的用户名密码，就能触发
[root@master1 ~]#curl http://mystical:123456@172.22.200.222:8080/job/trigger1-demo1/build?token=123456

# 但是账号密码直接触发并不安全，因此建议使用API token
```



**创建 API Token**

使用刚刚创建的新用户登录Jenkins

![image-20250222162230718](D:\git_repository\cyber_security_learning\markdown_img\image-20250222162230718-1755489161350-198.png)

![image-20250222162332664](D:\git_repository\cyber_security_learning\markdown_img\image-20250222162332664-1755489161350-184.png)

![image-20250222162345984](D:\git_repository\cyber_security_learning\markdown_img\image-20250222162345984-1755489161350-185.png)

![image-20250222162441576](D:\git_repository\cyber_security_learning\markdown_img\image-20250222162441576-1755489161350-186.png)

点击生成，得到一串随机的令牌

![image-20250222162529528](D:\git_repository\cyber_security_learning\markdown_img\image-20250222162529528-1755489161350-187.png)

后续即可使用该API Token进行访问

```bash
[root@master1 ~]#curl http://mystical:1128f339f008e400621c665a474c529973@172.22.200.222:8080/job/trigger1-demo1/build?token=123456
```



**GitLab 配置 Webhook**

以幸运大转盘的前端项目为准备环境，在上面配置远程构建

![image-20250222163707479](D:\git_repository\cyber_security_learning\markdown_img\image-20250222163707479-1755489161350-188.png)

在 GitLab 上配置 Webhook

![image-20250222163804202](D:\git_repository\cyber_security_learning\markdown_img\image-20250222163804202-1755489161350-189.png)

![image-20250222171422210](D:\git_repository\cyber_security_learning\markdown_img\image-20250222171422210-1755489161350-190.png)

**执行测试**

![image-20250222171457017](D:\git_repository\cyber_security_learning\markdown_img\image-20250222171457017-1755489161350-191.png)

```ABAP
添加webhook后，执行测试，会显示报错：Hook execution failed: URL is blocked: Requests to the local network are not allowed 

原因：Gitlab 需要打开外发请求，而默认是关闭的
```

![image-20250222171306327](D:\git_repository\cyber_security_learning\markdown_img\image-20250222171306327-1755489161350-192.png)

**手动打开外发请求**

![image-20250222170843855](D:\git_repository\cyber_security_learning\markdown_img\image-20250222170843855-1755489161350-193.png)

![image-20250222170947507](D:\git_repository\cyber_security_learning\markdown_img\image-20250222170947507-1755489161350-196.png)

**打开外发请求后，再执行测试**

![image-20250222171659375](D:\git_repository\cyber_security_learning\markdown_img\image-20250222171659375-1755489161350-194.png)

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

![image-20250222174525613](D:\git_repository\cyber_security_learning\markdown_img\image-20250222174525613-1755489161350-195.png)

![image-20250222174550740](D:\git_repository\cyber_security_learning\markdown_img\image-20250222174550740-1755489161350-197.png)







# 实验11：建前后多个项目关联自动触发任务执行

用于多个 Job 相互关联，需要同行执行多个job的场景,比如:如果job1后希望自动构建job2

**可以用两种方法实现**

- 在前面任务中利用构建后操作关联后续任务
- 在后面任务中利用构建触发器关联前面任务

```ABAP
注意：
上面两种方法,都需要在前面任务执行后才能自动关联执行后续任务
不要实现任务的环路，会导致死循环
```



## 在前面任务里配置构建后操作

在先执行的任务中配置构建后操作实现

###### 创建构建后操作

在第一个要执行的任务,指定构建后操作,添加第二个任务

要构建的项目可以填写多个项目名，之间用逗号分隔即可



**创建3个job**

![image-20250222180103160](D:\git_repository\cyber_security_learning\markdown_img\image-20250222180103160-1755489270953-225.png)

![image-20250222180137405](D:\git_repository\cyber_security_learning\markdown_img\image-20250222180137405-1755489270953-230.png)

![image-20250222180157020](D:\git_repository\cyber_security_learning\markdown_img\image-20250222180157020-1755489270953-226.png)



**在 job1 配置构建后操作**

![image-20250222223134385](D:\git_repository\cyber_security_learning\markdown_img\image-20250222223134385-1755489270953-228.png)![image-20250222223205571](D:\git_repository\cyber_security_learning\markdown_img\image-20250222223205571-1755489270953-227.png)

![image-20250222223233455](D:\git_repository\cyber_security_learning\markdown_img\image-20250222223233455-1755489270953-229.png)



## **在后面构建的任务里创建**

###### 在后续构建的任务里利用构建触发器实现

在后面的 job 配置如下

在构建触发器---Build after other project are built --- 关注的项目 --- 输入前面的 job,如果有多个job 用 逗号分隔

![image-20250222224326137](D:\git_repository\cyber_security_learning\markdown_img\image-20250222224326137-1755489270953-231.png)                                                                                                                                                                                                                                                                                                

![image-20250222224423262](D:\git_repository\cyber_security_learning\markdown_img\image-20250222224423262-1755489270953-233.png)

![image-20250222224657104](D:\git_repository\cyber_security_learning\markdown_img\image-20250222224657104-1755489270953-232.png)





## Blue Ocean 插件实现可视化

![image-20250222224922418](D:\git_repository\cyber_security_learning\markdown_img\image-20250222224922418-1755489308952-243.png)

Blue Ocean 插件可以实现更加漂亮的可视化界面,并且可以对指定的步骤进行重启等操作



##### 安装 Blue Ocean 插件

注意: 安装完插件,需要重启Jenkins才能生效

![image-20250223132907470](D:\git_repository\cyber_security_learning\markdown_img\image-20250223132907470-1755489308952-245.png)

![image-20250223133616278](D:\git_repository\cyber_security_learning\markdown_img\image-20250223133616278-1755489308952-247.png)



![image-20250223133645332](D:\git_repository\cyber_security_learning\markdown_img\image-20250223133645332-1755489308952-246.png)

![image-20250223133711823](D:\git_repository\cyber_security_learning\markdown_img\image-20250223133711823-1755489308952-244.png)

![image-20250223133735240](D:\git_repository\cyber_security_learning\markdown_img\image-20250223133735240-1755489308952-248.png)







# 实验12：基于 Docker 插件实现自由风格任务实现 Docker 镜像制作

![image-20250223173417986](D:\git_repository\cyber_security_learning\markdown_img\image-20250223173417986-1755489427346-255.png)

## 安装插件 docker-build-step

![image-20250223174752040](D:\git_repository\cyber_security_learning\markdown_img\image-20250223174752040-1755489427346-256.png)





## 在Jenkins 安装Docker并配置 Docker 插件

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



##  本地 Docker Engine

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

![image-20250223175454021](D:\git_repository\cyber_security_learning\markdown_img\image-20250223175454021-1755489427346-258.png)





## 在 Jenkins 创建连接 Harbor 的凭证

![image-20250223175853800](D:\git_repository\cyber_security_learning\markdown_img\image-20250223175853800-1755489427346-260.png)



![image-20250223175930893](D:\git_repository\cyber_security_learning\markdown_img\image-20250223175930893-1755489427346-257.png)

![image-20250223175940433](D:\git_repository\cyber_security_learning\markdown_img\image-20250223175940433-1755489427346-261.png)

![image-20250223180125307](D:\git_repository\cyber_security_learning\markdown_img\image-20250223180125307-1755489427346-259.png)





## 创建自由风格的 spring-boot-helloworld 项目的任务

![image-20250223180245096](D:\git_repository\cyber_security_learning\markdown_img\image-20250223180245096-1755489427346-262.png)

![image-20250223180429539](D:\git_repository\cyber_security_learning\markdown_img\image-20250223180429539-1755489427346-263.png)



![image-20250223180635122](D:\git_repository\cyber_security_learning\markdown_img\image-20250223180635122-1755489427346-264.png)

![image-20250223180645491](D:\git_repository\cyber_security_learning\markdown_img\image-20250223180645491-1755489427346-265.png)



![image-20250223180906669](D:\git_repository\cyber_security_learning\markdown_img\image-20250223180906669-1755489427346-267.png)



![image-20250223181140733](D:\git_repository\cyber_security_learning\markdown_img\image-20250223181140733-1755489427346-266.png)

![image-20250223181559168](D:\git_repository\cyber_security_learning\markdown_img\image-20250223181559168-1755489427346-269.png)

![image-20250223205825975](D:\git_repository\cyber_security_learning\markdown_img\image-20250223205825975-1755489427346-268.png)







# 实验13：基于 SSH 协议实现 Jenkins 分布式

![image-20250225105514984](D:\git_repository\cyber_security_learning\markdown_img\image-20250225105514984-1755489543919-285.png)

## Slave 节点安装 Java 等环境确保和 Master 环境一致

```bash
# 准备两台agent服务器
# 172.22.200.224
# 172.22.200.225

# 配置hostname
[root@mystical ~]# hostnamectl set-hostname agent1
[root@mystical ~]# hostnamectl set-hostname agent2

```



## Master节点安装插件

安装 **SSH Build Agents** 插件，实现 ssh 连接代理

![image-20250225112619786](D:\git_repository\cyber_security_learning\markdown_img\image-20250225112619786-1755489543919-288.png)



## 添加 Master 访问 Slave 认证凭据

用于 Master 连接 Slave 节点的凭据

可以是用户密码的凭据,也可以配置Master节点到Slave节点SSH key 验证

以root 身份连接 Agent

如果已经实现ssh key 验证，下面可以不配置

![image-20250225112948156](D:\git_repository\cyber_security_learning\markdown_img\image-20250225112948156-1755489543919-286.png)

![image-20250225113016078](D:\git_repository\cyber_security_learning\markdown_img\image-20250225113016078-1755489543919-292.png)

![image-20250225113056030](D:\git_repository\cyber_security_learning\markdown_img\image-20250225113626670-1755489543919-287.png)

​		

## 添加 Agent 节点

![image-20250225113800566](D:\git_repository\cyber_security_learning\markdown_img\image-20250225113800566-1755489543919-289.png)

![image-20250225113817218](D:\git_repository\cyber_security_learning\markdown_img\image-20250225113817218-1755489543919-290.png)

![image-20250225113847599](D:\git_repository\cyber_security_learning\markdown_img\image-20250225113847599-1755489543919-291.png)

![image-20250225114035874](D:\git_repository\cyber_security_learning\markdown_img\image-20250225114035874.png)

![image-20250225114501906](D:\git_repository\cyber_security_learning\markdown_img\image-20250225114501906-1755489543919-293.png)

**agent 创建失败**

![image-20250225114631657](D:\git_repository\cyber_security_learning\markdown_img\image-20250225114631657-1755489543919-294.png)

**查看原因**

![image-20250225114738113](D:\git_repository\cyber_security_learning\markdown_img\image-20250225114738113-1755489543919-296.png)

![image-20250225114746411](D:\git_repository\cyber_security_learning\markdown_img\image-20250225114746411-1755489543919-295.png)

通过日志可以看出，这里报错是因为，agent所在主机上没有安装java

```bash
# 注意：agent上安装的java版本和master上的java版本一致
[root@agent1 ~]# apt update && apt install -y openjdk-17-jdk
[root@agent2 ~]# apt update && apt install -y openjdk-17-jdk
```

重新连接一下agent

![image-20250225115402542](D:\git_repository\cyber_security_learning\markdown_img\image-20250225115402542-1755489543919-297.png)

**成功同步**

![image-20250225120030718](D:\git_repository\cyber_security_learning\markdown_img\image-20250225120030718-1755489543919-301.png)

查看 agent1上的进程，可以看到启用了一个 java 服务

```bash
[root@agent1 ~]# ps aux|grep java
root        6189  3.4  2.9 3619940 118364 ?      Ssl  04:00   0:03 java -jar remoting.jar -workDir /var/lib/jenkins -jar-cache /var/lib/jenkins/remoting/jarCache
```



## 建立后续的其它节点

重复上面的过程,建立其它的从节点

**小技巧:** 可以将复制Slave1节点的/root/.ssh目录到Slave2,从而可以省略 Slave2到其它主机的 Ssh key验证过程

![image-20250225121438278](D:\git_repository\cyber_security_learning\markdown_img\image-20250225121438278-1755489543919-298.png)

![image-20250225121513853](D:\git_repository\cyber_security_learning\markdown_img\image-20250225121513853-1755489543919-299.png)

稍微更下配置和标签后，创建

![image-20250225121609219](D:\git_repository\cyber_security_learning\markdown_img\image-20250225121609219-1755489543919-300.png)

将全局安全配置中的Git Host Key Verification Configuration 选为 No verification，否则，agent 上的 ssh 初次连接 gitlab 会要求验证，要求输入yes。

![image-20250225132143105](D:\git_repository\cyber_security_learning\markdown_img\image-20250225132143105-1755489543919-302.png)

将脚本文件从 master 服务器拷贝到 agent 服务器上，路径建议一致

```bash
[root@mystical /data/jenkins/script]# scp spring-boot-helloworld.sh 172.22.200.224:/data/jenkis/script/
```



打通 agent 服务器和待部署的服务器的 ssh 验证并在 agent 上安装 mvn

```bash
[root@mystical /data/jenkins/script]# apt install -y maven
```





## 测试 SSH Agent

创建一个 freestyle 风格的任务

![image-20250225130935891](D:\git_repository\cyber_security_learning\markdown_img\image-20250225130935891-1755489543919-303.png)



通过标签选择用来构建的 agent 节点

![image-20250225131142758](D:\git_repository\cyber_security_learning\markdown_img\image-20250225131150390-1755489543919-304.png)

![image-20250225131514543](D:\git_repository\cyber_security_learning\markdown_img\image-20250225131514543-1755489543919-305.png)

![image-20250225134157097](D:\git_repository\cyber_security_learning\markdown_img\image-20250225134157097-1755489543919-306.png)

![image-20250225135745320](D:\git_repository\cyber_security_learning\markdown_img\image-20250225135745320-1755489543919-307.png)

![image-20250225144853905](D:\git_repository\cyber_security_learning\markdown_img\image-20250225144853905-1755489543919-308.png)







# 实验14：基于 JNLP 协议的 Java Web 启动代理

此方式无需安装插件，即可实现

## 全局安全配置

使用随机端口

![image-20250225145552793](D:\git_repository\cyber_security_learning\markdown_img\image-20250225145552793-1755489721906-333.png)

或者指定为固定端口

![image-20250225145659642](D:\git_repository\cyber_security_learning\markdown_img\image-20250225145659642-1755489721906-335.png)



## 创建代理Agent节点

![image-20250225145829581](D:\git_repository\cyber_security_learning\markdown_img\image-20250225145829581-1755489721906-334.png)

![](D:\git_repository\cyber_security_learning\markdown_img\image-20250225150157433-1755489721906-338.png)

![image-20250225150257221](D:\git_repository\cyber_security_learning\markdown_img\image-20250225150257221-1755489721906-337.png)

![image-20250225150337369](D:\git_repository\cyber_security_learning\markdown_img\image-20250225150337369-1755489721906-336.png)

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





# 实验15：配置基于Docker 的动态Agent

## 准备 Docker Engine 主机

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



## Jenkins 上安装Docker插件

![image-20250225153235825](D:\git_repository\cyber_security_learning\markdown_img\image-20250225153235825-1755489783274-345.png)





## 创建 Cloud

![image-20250225153542704](D:\git_repository\cyber_security_learning\markdown_img\image-20250225153542704-1755489783274-348.png)

![image-20250225153558551](D:\git_repository\cyber_security_learning\markdown_img\image-20250225153558551-1755489783274-347.png)

![image-20250225153652356](D:\git_repository\cyber_security_learning\markdown_img\image-20250225153652356-1755489783274-349.png)

## Docker Cloud Details 配置指定连接Docker的方式

**远程方式**

![image-20250225154819035](D:\git_repository\cyber_security_learning\markdown_img\image-20250225154819035-1755489783274-346.png)



## 添加 Docker Agent templates

![image-20250225155053687](D:\git_repository\cyber_security_learning\markdown_img\image-20250225155053687-1755489783274-350.png)

```bash
# 在agent上将官方的agent镜像拉下来，可能需要科学上网
[root@agent1 ~]# docker pull jenkins/inbound-agent:alpine-jdk11
```

![image-20250225155918739](D:\git_repository\cyber_security_learning\markdown_img\image-20250225155918739-1755489783274-351.png)

![image-20250225155955353](D:\git_repository\cyber_security_learning\markdown_img\image-20250225155955353-1755489783274-352.png)



## 测试构建任务

![image-20250225160328457](D:\git_repository\cyber_security_learning\markdown_img\image-20250225160328457-1755489783274-353.png)

![image-20250225160511512](D:\git_repository\cyber_security_learning\markdown_img\image-20250225160511512-1755489783274-354.png)

![image-20250225160521762](D:\git_repository\cyber_security_learning\markdown_img\image-20250225160521762-1755489783274-355.png)

因为镜像中没有 mvn 工具，因此这里使用 echo 做测试

![image-20250225160840603](D:\git_repository\cyber_security_learning\markdown_img\image-20250225160840603-1755489783274-356.png)

![image-20250225162110851](D:\git_repository\cyber_security_learning\markdown_img\image-20250225162110851-1755489783274-357.png)

![image-20250225162121841](D:\git_repository\cyber_security_learning\markdown_img\image-20250225162121841-1755489783274-358.png)

构建任务结束后，刚创建的 agent 容器会释放掉

```ABAP
注意：master节点上java的版本必须和agent服务器上的镜像的java版本一致！！！
```

查看日志，在临时容器中运行的构建任务

![image-20250225162439065](D:\git_repository\cyber_security_learning\markdown_img\image-20250225162439065.png)





# 实验16：实现一个简单 Pipeline Job

##### 安装 Pipeline 插件

安装 **Pipeline** 和 **Pipeline Stage View** 插件



##### 创建 Pipeline Job

![image-20250227211812589](D:\git_repository\cyber_security_learning\markdown_img\image-20250227211812589-1755489946215-373.png)



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

![image-20250227212308189](D:\git_repository\cyber_security_learning\markdown_img\image-20250227212308189-1755489946215-375.png)



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

![image-20250227212550509](D:\git_repository\cyber_security_learning\markdown_img\image-20250227212550509-1755489946215-376.png)



如果安装Blue Ocean 插件,可以下看如下的显示效果

![image-20250227212709806](D:\git_repository\cyber_security_learning\markdown_img\image-20250227212709806-1755489946215-374.png)

![image-20250227212729211](D:\git_repository\cyber_security_learning\markdown_img\image-20250227212729211.png)

# 实验17：部署代码测试工具 SonarQube 



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

![image-20250228120802157](D:\git_repository\cyber_security_learning\markdown_img\image-20250228120802157-1755490214253-385.png)



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

![image-20250228141609596](D:\git_repository\cyber_security_learning\markdown_img\image-20250228141609596-1755490214253-381.png)

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

![image-20250228151954515](D:\git_repository\cyber_security_learning\markdown_img\image-20250228151954515-1755490214253-382.png)

首次登录必须修改admin用户的密码

```ABAP
注意: 新密码不能使用原密码
```

![image-20250228152203063](D:\git_repository\cyber_security_learning\markdown_img\image-20250228152203063-1755490214253-384.png)

![image-20250228152313536](D:\git_repository\cyber_security_learning\markdown_img\image-20250228152313536-1755490214253-383.png)





# 实验18：在 Jenkins 服务器部署代码扫描器 sonar-scanner

## 部署代码扫描器 sonar-scanner

sonar-scanner 是基于Java 实现的客户端工具，负责扫描源代码，并提交结果给Sonarqube Server

官方文档

```http
https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/
```

![image-20250228165558325](D:\git_repository\cyber_security_learning\markdown_img\image-20250228165558325-1755490674014-391.png)



## 在 Jenkins 服务器部署和配置 sonar-scanner

sonarqube 通过调用扫描器sonar-scanner进行代码质量分析，即扫描器的具体工作就是扫描代码

###### sonar-scanner 安装方法1：手动下载安装

新版下载链接

```http
https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/
```

![image-20250228170052006](D:\git_repository\cyber_security_learning\markdown_img\image-20250228170052006-1755490674014-393.png)

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

![image-20250228205931497](D:\git_repository\cyber_security_learning\markdown_img\image-20250228205931497-1755490674014-395.png)

```bash
# 也可以不使用sonar-project.properties文件的值，而是直接在命令行赋值
[root@jenkins spring-boot-helloWorld]#sonar-scanner -Dsonar.projectName=myapp -Dsonar.projectKey=myapp 

# 执行后，观察服务端结果，项目名称是自定义的myapp，作为了一个新项目。
```

![image-20250228210612819](D:\git_repository\cyber_security_learning\markdown_img\image-20250228210612819-1755490674014-397.png)

点击进入项目，可以发现有25个异味

![image-20250228210737781](D:\git_repository\cyber_security_learning\markdown_img\image-20250228210737781-1755490674014-394.png)

查看异味具体内容

![image-20250228210833199](D:\git_repository\cyber_security_learning\markdown_img\image-20250228210833199-1755490674014-392.png)

![image-20250228210919616](D:\git_repository\cyber_security_learning\markdown_img\image-20250228210919616-1755490674014-396.png)

##### 扫描 Java 项目

```ABAP
扫描 java 项目和其他语言有所不同，不能只指定sonar.projectKey，还必须额外指定sonar.java.binaries的值
```

**示例**

```bash
[root@mystical ~/project/helloworld-spring-boot]# /usr/local/sonar-scanner/bin/sonar-scanner -Dsonar.projectName=helloworld -Dsonar.projectKey=helloworld -Dsonar.java.binaries=./

# 执行后，查看server端的项目
```

![image-20250228212229579](D:\git_repository\cyber_security_learning\markdown_img\image-20250228212229579-1755490674014-398.png)