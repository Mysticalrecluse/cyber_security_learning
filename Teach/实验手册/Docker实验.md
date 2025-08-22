# 实验1：Docker安装

## Ubuntu内置仓库安装

```bash
[root@mystical ~]# apt update && apt install -y docker.io

# 查看
[root@mystical ~]# docker info
Client:
 Version:    24.0.7
 Context:    default
 Debug Mode: false

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 24.0.7
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 ......
```





## 官方仓库安装

**阿里云官方仓库**

- 官方地址

```http
https://developer.aliyun.com/mirror/docker-ce?spm=a2c6h.13651102.0.0.57e31b11DDIh92
```

- 官方操作（可以看做是脚本运行）

```bash
# step 1: 安装必要的一些系统工具
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
# step 2: 安装GPG证书
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
# Step 3: 写入软件源信息
sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
# Step 4: 更新并安装Docker-CE
sudo apt-get -y update
sudo apt-get -y install docker-ce # 默认下载最新版

# 安装Docker-CE特定版本
sudo apt-get -y install docker-ce=[VERSION] docker-ce-cli=[VERSION]
```



## 二进制安装（离线）

本方法适用于无法上网或无法通过包安装方式安装的主机上安装docker

```bash
# 二进制安装下载路径
https://download.docker.com/linux/
https://mirrors.aliyun.com/docker-ce/linux/static/stable/x86_64/
```

示例：在CentOS上实现二进制安装docker

```bash
wget https://download.docker.com/linux/static/stable/x86_64/docker-19.03.5.tgz

# 解压到指定目录
tar xvf docker-19.03.5.tgz    

# 加入环境变量
cp docker/* /usr/bin/

# 创建 service文件
cat > /lib/systemd/system/docker.service <<-EOF
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target
[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues 
still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/bin/dockerd -H unix://var/run/docker.sock
ExecReload=/bin/kill -s HUP \$MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker 
containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s
[Install]
WantedBy=multi-user.target
EOF

# 重启
systemctl daemon-reload
systemctl enable --now docker   
```





## 脚本安装

- install_docker_offine.sh

```bash
#!/bin/bash
#
#********************************************************************
#Author:            wangxiaochun
#QQ:                29308620
#Date:              2022-10-14
#FileName:          install_docker_offline.sh
#URL:               http://www.wangxiaochun.com
#Description:       The test script
#Copyright (C):     2022 All rights reserved
#********************************************************************

#支持在线和离线安装

DOCKER_VERSION=26.1.4
#DOCKER_VERSION=26.0.0
#DOCKER_VERSION=24.0.7
#DOCKER_VERSION=24.0.5
#DOCKER_VERSION=23.0.3
#DOCKER_VERSION=20.10.19

URL=https://mirrors.tuna.tsinghua.edu.cn
#URL=https://mirrors.aliyun.com
#URL=https://download.docker.com

color () {
    RES_COL=60
    MOVE_TO_COL="echo -en \\033[${RES_COL}G"
    SETCOLOR_SUCCESS="echo -en \\033[1;32m"
    SETCOLOR_FAILURE="echo -en \\033[1;31m"
    SETCOLOR_WARNING="echo -en \\033[1;33m"
    SETCOLOR_NORMAL="echo -en \E[0m"
    echo -n "$1" && $MOVE_TO_COL
    echo -n "["
    if [ $2 = "success" -o $2 = "0" ] ;then
        ${SETCOLOR_SUCCESS}
        echo -n $"  OK  "    
    elif [ $2 = "failure" -o $2 = "1"  ] ;then 
        ${SETCOLOR_FAILURE}
        echo -n $"FAILED"
    else
        ${SETCOLOR_WARNING}
        echo -n $"WARNING"
    fi
    ${SETCOLOR_NORMAL}
    echo -n "]"
    echo 
}

prepare () {
    if [ ! -e docker-${DOCKER_VERSION}.tgz ];then
        #wget ${URL}/docker-ce/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
        wget ${URL}/docker-ce/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
    fi
    [ $? -ne 0  ] && { echo "文件下载失败"; exit; }
}

install_docker () {
    tar xf docker-${DOCKER_VERSION}.tgz -C /usr/local/
    cp /usr/local/docker/* /usr/local/bin/
    cat > /lib/systemd/system/docker.service <<-EOF
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target

[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/local/bin/dockerd -H unix://var/run/docker.sock
ExecReload=/bin/kill -s HUP \$MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s

[Install]
WantedBy=multi-user.target
EOF
    systemctl daemon-reload
}

config_docker () {
    mkdir -p /etc/docker
    tee /etc/docker/daemon.json <<-'EOF'
    {
      "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"]
     }
EOF
    #systemctl restart docker

}

start_docker (){
    systemctl enable --now docker
    docker version && color "Docker 安装成功" 0 ||  color "Docker 安装失败" 1
}


config_docker_completion () {
    wget -P /etc/bash_completion.d http://www.wangxiaochun.com:8888/testdir/docker/docker_completion 
    #source /etc/bash_completion.d/docker_completion
}


prepare

install_docker

config_docker

start_docker

config_docker_completion
```





# 实验2：Dockerfile 多阶段构建

## 多阶段构建Go语言程序镜像

**创建一个GO语言程序**

```go
# cat hello.go
package main

import (
   "fmt"
   "time"
)

func main() {
   for {
      fmt.Println("hello,world")
      time.Sleep(time.Second)
   }
}
```

**基于传统方式构建Golang应用**

```dockerfile
# cat Dockerfile
FROM golang:1.18-alpine
COPY hello.go /
# WORKDIR /
RUN cd / && go build hello.go
CMD ["/hello"]
```

**多阶段构建1:GO语言程序**

```dockerfile
# cp Dockerfile Dockerfile-v1.0
# vim Dockerfile
FROM golang:1.18-alpine as builder
COPY hello.go /opt
WORKDIR /opt
RUN go build hello.go

FROM alpine:3.15.0
#FROM scratch
COPY --from=builder /opt/hello /hello
#COPY --from=0 /opt/hello /hello
CMD ["/hello"]
```



## 多阶段构建C语言程序镜像

```dockerfile
ARG VERSION=3.20.0
FROM alpine:$VERSION
LABEL maintainer="mystical<mysticalrecluse@gmail.com>"

ENV NGINX_VERSION=1.26.1
ENV NGINX_DIR=/apps/nginx

ADD nginx-$NGINX_VERSION.tar.gz /usr/local/src

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/' /etc/apk/repositories && \
    apk update && apk --no-cache add gcc make libgcc libc-dev libcurl lib-utils pcre-dev zlib-dev libnfs pcre pcre2 net-tools curl pstree wget libevent libevent-dev iproute2 openssl-dev && \
    cd /usr/local/src/nginx-$NGINX_VERSION && \
    ./configure --prefix=${NGINX_VERSION} --user=nginx --group=nginx --with-http_ssl_module --with-http_v2_module --with-http_realip_module --with-http_stub_status_module --with-http_gzip_static_module --with-pcre --with-stream --with-stream_ssl_module --with-stream_realip_module && \
    make && make install && \
    rm -rf /usr/local/src/nginx-$NGINX_VERSION

COPY nginx.conf ${NGINX_DIR}/conf/nginx.conf

FROM alpine:$VERSION
ENV NGINX_DIR=/apps/nginx
COPY --from=0 ${NGINX_DIR}/ ${NGINX_DIR}/
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc/edu.cn/' /etc/apk/repositories \
    && apk update && apk --no-cache add tzdate pcre pcre2 \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && addgroup -g 888 -S nginx \
    && adduser -u 888 -G nginx -D -S -s /sbin/nologin nginx \
    && chown -R nginx.nginx ${NGINX_DIR}/ \
    # 在容器化环境中，推荐的做法是将应用程序的日志输出到标准输出和标准错误。容器运行时（如 Docker）会捕获这些日志并将它们存储在宿主机上。这样，日志就可以被宿主机上的日志收集和处理系统统一管理。
    && ln -sf /dev/stdout ${NGINX_DIR}/logs/access.log \
    && ln -sr /dev/stderr ${NGINX_DIR}/logs/error.log
EXPOSE 80 443
CMD ["nginx","-g","daemon off;"]
```





# 实验3: 安装Docker Compose



## 方法1:通过 Compose plugin 形式安装

即通过docker 内置子命令实现, 此方式无需专门安装独立的 docker-compose 工具

注意：此方式需要配置官方仓库才支持，Ubuntu内置仓库没有此插件包

```bash
# Add Docker's official GPG key:
apt-get update
apt-get install ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

echo "GPG OVER"

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# 官方仓库配置好后，执行下面的指令
[root@ubuntu2204 ~]#apt install -y docker-compose-plugin

# 执行之后，查看docker
[root@ubuntu2204 ~]#docker
......
Management Commands:
  builder     Manage builds
  compose*    Docker Compose
  container   Manage containers
  context     Manage contexts
......
```



## 方法2: 在线直接从包仓库安装

此方法安装的版本较旧，不推荐使用

```bash
#ubuntu安装,此为默认版本
[root@ubuntu2204 ~]#apt list  docker-compose
正在列表... 完成
docker-compose/jammy 1.29.2-1 all
[root@ubuntu1804 ~]#apt -y install docker-compose
[root@ubuntu1804 ~]#docker-compose --version
docker-compose version 1.17.1, build unknown

#CentOS7安装，依赖EPEL源
[root@centos7 ~]#yum -y install docker-compose
[root@centos7 ~]#docker-compose --version
docker-compose version 1.18.0, buil 8dd22a9 
```



## 方法3: 离线安装，直接从github或国内镜像站下载安装对应版本

参看说明:   https://github.com/docker/compose/releases

此方法安装版本可方便指定，推荐方法，但网络下载较慢

```bash
[root@ubuntu1804 ~]#curl -L https://github.com/docker/compose/releases/download/1.25.3/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

#从国内镜像站下载
[root@ubuntu1804 ~]#curl -L https://get.daocloud.io/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

[root@ubuntu1804 ~]#chmod +x /usr/local/bin/docker-compose
[root@ubuntu1804 ~]#ldd /usr/local/bin/docker-compose
    不是动态可执行文件
```



## 方法4: 在线通过 pip安装

python-pip 包将安装一个 pip 的命令，pip 命令是一个python 安装包的安装工具，其类似于ubuntu 的 apt 或者 redhat 的yum，但是pip 只安装 python 相关的安装包，可以在多种操作系统安装和使用pip

此方式当前安装的版本较新，为docker_compose-1.25.3，推荐使用

```bash
Ubuntu:   
# apt  update 
# apt  install -y  python-pip 

CentOS:   
# yum install epel-release 
# yum install -y python-pip 
# pip install --upgrade pip 
```

基于python3 安装 docker-compose

```bash
#配置加速
[root@ubuntu2004 ~]#mkdir ~/.pip
[root@ubuntu2004 ~]#cat > ~/.pip/pip.conf <<-EOF
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
EOF

[root@ubuntu2004 ~]#apt -y install python3-pip
[root@ubuntu2004 ~]#pip3 install --upgrade pip

[root@ubuntu2004 ~]#pip3 install docker-compose
[root@ubuntu2004 ~]#docker-compose --version
docker-compose version 1.27.4, build unknown

#基于python2安装docker-compose
[root@ubuntu1804 ~]#apt -y install python-pip
[root@ubuntu1804 ~]#pip install docker-compose
[root@ubuntu1804 ~]#docker-compose --version
```





# 实验4：分布式仓库Harbor

#### 安装 Harbor

下载地址:   https://github.com/vmware/harbor/releases



##### 环境准备:  共四台主机

- 两台主机harbor服务器，地址:  10.0.0.101|102
- 两台主机harbor客户端上传和下载镜像

![image-20250205223819316](D:\git_repository\cyber_security_learning\markdown_img\image-20250205223819316-1755485801360-1.png)

##### 安装 docker

使用脚本安装，脚本内容如下

```bash
#!/bin/bash
#
#********************************************************************
#Author:            wangxiaochun
#QQ:                29308620
#Date:              2022-10-14
#FileName:          install_docker_offline.sh
#URL:               http://www.wangxiaochun.com
#Description:       The test script
#Copyright (C):     2022 All rights reserved
#********************************************************************

#支持在线和离线安装

DOCKER_VERSION=26.1.4
#DOCKER_VERSION=26.0.0
#DOCKER_VERSION=24.0.7
#DOCKER_VERSION=24.0.5
#DOCKER_VERSION=23.0.3
#DOCKER_VERSION=20.10.19

URL=https://mirrors.tuna.tsinghua.edu.cn
#URL=https://mirrors.aliyun.com
#URL=https://download.docker.com

color () {
    RES_COL=60
    MOVE_TO_COL="echo -en \\033[${RES_COL}G"
    SETCOLOR_SUCCESS="echo -en \\033[1;32m"
    SETCOLOR_FAILURE="echo -en \\033[1;31m"
    SETCOLOR_WARNING="echo -en \\033[1;33m"
    SETCOLOR_NORMAL="echo -en \E[0m"
    echo -n "$1" && $MOVE_TO_COL
    echo -n "["
    if [ $2 = "success" -o $2 = "0" ] ;then
        ${SETCOLOR_SUCCESS}
        echo -n $"  OK  "    
    elif [ $2 = "failure" -o $2 = "1"  ] ;then 
        ${SETCOLOR_FAILURE}
        echo -n $"FAILED"
    else
        ${SETCOLOR_WARNING}
        echo -n $"WARNING"
    fi
    ${SETCOLOR_NORMAL}
    echo -n "]"
    echo 
}

prepare () {
    if [ ! -e docker-${DOCKER_VERSION}.tgz ];then
        #wget ${URL}/docker-ce/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
        wget ${URL}/docker-ce/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
    fi
    [ $? -ne 0  ] && { echo "文件下载失败"; exit; }
}

install_docker () {
    tar xf docker-${DOCKER_VERSION}.tgz -C /usr/local/
    cp /usr/local/docker/* /usr/local/bin/
    cat > /lib/systemd/system/docker.service <<-EOF
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target

[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/local/bin/dockerd -H unix://var/run/docker.sock
ExecReload=/bin/kill -s HUP \$MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s

[Install]
WantedBy=multi-user.target
EOF
    systemctl daemon-reload
}

config_docker () {
    mkdir -p /etc/docker
    tee /etc/docker/daemon.json <<-'EOF'
    {
      "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"]
     }
EOF
    #systemctl restart docker

}

start_docker (){
    systemctl enable --now docker
    docker version && color "Docker 安装成功" 0 ||  color "Docker 安装失败" 1
}


config_docker_completion () {
    wget -P /etc/bash_completion.d http://www.wangxiaochun.com:8888/testdir/docker/docker_completion 
    #source /etc/bash_completion.d/docker_completion
}


prepare

install_docker

config_docker

start_docker

config_docker_completion
```



##### 先安装docker compose

```bash
# Add Docker's official GPG key:
apt-get update
apt-get install ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

echo "GPG OVER"

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# 官方仓库配置好后，执行下面的指令
[root@ubuntu2204 ~]#apt install -y docker-compose-plugin
```



##### 下载Harbor安装包并解压缩

```bash
[root@ubuntu2204 ~]#wget https://github.com/goharbor/harbor/releases/download/v2.12.2/harbor-offline-installer-v2.12.2.tgz

[root@ubuntu2204 ~]#mkdir /apps
[root@ubuntu2204 ~]#tar xvf harbor-offline-installer-v2.12.2.tgz -C /apps/
harbor/harbor.v2.12.2.tar.gz
harbor/prepare
harbor/LICENSE
harbor/install.sh
harbor/common.sh
harbor/harbor.yml.tmpl
```



##### 编辑 harbor 配置文件

```bash
[root@ubuntu2204 harbor]#cd /apps/harbor
[root@ubuntu2204 harbor]#cp harbor.yml.tmpl harbor.yml
[root@ubuntu2204 harbor]#vim harbor.yml
# 更改配置文件的主机名，这里为了实验简单，故而使用ip
# hostname: harbor.mystical.org
hostname: 10.0.0.100

# 将https注视掉
#https:
  # https port for harbor, default is 443
#  port: 443
  # The path of cert and key files for nginx
#  certificate: /your/certificate/path
#  private_key: /your/private/key/path

# 更改harbor的登录密码
harbor_admin_password: 123456

# 更改数据目录
# The default data volume
data_volume: /data/harbor

[root@ubuntu2204 harbor]#ls
common.sh  harbor.v2.12.2.tar.gz  harbor.yml  harbor.yml.tmpl  install.sh  LICENSE  prepare

# 使用prepare拉取镜像并生成配置文件
[root@ubuntu2204 harbor]#./prepare 

# 使用install.sh
[root@ubuntu2204 harbor]#./install.sh 

# 查看
[root@ubuntu2204 harbor]#docker compose ps
NAME                IMAGE                                 COMMAND                   SERVICE       CREATED          STATUS                             PORTS
harbor-core         goharbor/harbor-core:v2.12.2          "/harbor/entrypoint.…"   core          26 seconds ago   Up 19 seconds (health: starting)   
harbor-db           goharbor/harbor-db:v2.12.2            "/docker-entrypoint.…"   postgresql    26 seconds ago   Up 20 seconds (health: starting)   
harbor-jobservice   goharbor/harbor-jobservice:v2.12.2    "/harbor/entrypoint.…"   jobservice    26 seconds ago   Up 9 seconds (health: starting)    
harbor-log          goharbor/harbor-log:v2.12.2           "/bin/sh -c /usr/loc…"   log           26 seconds ago   Up 24 seconds (health: starting)   127.0.0.1:1514->10514/tcp
harbor-portal       goharbor/harbor-portal:v2.12.2        "nginx -g 'daemon of…"   portal        26 seconds ago   Up 20 seconds (health: starting)   
nginx               goharbor/nginx-photon:v2.12.2         "nginx -g 'daemon of…"   proxy         26 seconds ago   Up 18 seconds (health: starting)   0.0.0.0:80->8080/tcp, [::]:80->8080/tcp
redis               goharbor/redis-photon:v2.12.2         "redis-server /etc/r…"   redis         26 seconds ago   Up 21 seconds (health: starting)   
registry            goharbor/registry-photon:v2.12.2      "/home/harbor/entryp…"   registry      26 seconds ago   Up 20 seconds (health: starting)   
registryctl         goharbor/harbor-registryctl:v2.12.2   "/home/harbor/start.…"   registryctl   26 seconds ago   Up 20 seconds (health: starting) 
```



##### 实现开机自动启动 harbor

旧版 Harbor 开机不会自动启动，可以创建 service 文件实现

新版 Harbor 默认开机自动，比如：harbor-v2.9.1

```bash
[root@harbor ~]#vim /lib/systemd/system/harbor.service
[Unit]
Description=Harbor
After=docker.service systemd-networkd.service systemd-resolved.service
Requires=docker.service
Documentation=http://github.com/vmware/harbor

[Service]
Type=simple
Restart=on-failure
RestartSec=5
ExecStart=/usr/bin/docker-compose -f  /apps/harbor/docker-compose.yml up
ExecStop=/usr/bin/docker-compose -f /apps/harbor/docker-compose.yml down

[Install]
WantedBy=multi-user.target

[root@harbor ~]#systemctl daemon-reload 
[root@harbor ~]#systemctl enable harbor
```



#### 登录 harbor 主机网站

用浏览器访问:   http://10.0.0.100/

- 用户名:  admin
- 密码:  即前面harbor.yml中指定的密码

![image-20250205230259130](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230259130-1755485801360-2.png)

![image-20250205230320523](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230320523-1755485801360-4.png)



### 使用单主机Harbor

#### 建立项目

**harbor上必须先建立项目，才能上传镜像**

![image-20250205230642513](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230642513-1755485801360-6.png)

![image-20250205230713546](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230713546-1755485801360-3.png)

![image-20250205230806935](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230806935-1755485801360-5.png)



#### 创建用户和项目授权

##### 创建用户

![image-20250205230911713](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230911713-1755485801360-8.png)

![image-20250205230956394](D:\git_repository\cyber_security_learning\markdown_img\image-20250205230956394-1755485801360-7.png)

![image-20250205231026855](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231026855-1755485801360-9.png)



##### 在项目内对用户授权

进入对应的项目，，注意：至少是开发者以上才能上传镜像

![image-20250205231233881](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231233881-1755485801360-10.png)

![image-20250205231314266](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231314266-1755485801360-11.png)

![image-20250205231342108](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231342108-1755485801360-12.png)



#### 命令行登录 Harbor

查看推送地址与相关命令

![image-20250205231933464](D:\git_repository\cyber_security_learning\markdown_img\image-20250205231933464-1755485801360-13.png)

```bash
# 推送镜像前，要将镜像改名
# docker tag SOURCE_IMAGE[:TAG] 10.0.0.100/example/REPOSITORY[:TAG]
[root@ubuntu2204 ~]#docker tag nginx:latest 10.0.0.100/example/nginx:latest

# 目前推送会报错
# 首先默认会使用https推送，但是我们这边使用http，所以需要将host加入Insecure Registries中
# 这里不安全的仓库，指的就是使用http，而不是https
[root@ubuntu2204 ~]#cat /etc/docker/daemon.json 
{
   "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"],
   "insecure-registries": ["harbor.mystical.org", "10.0.0.100"]
}

# 重启docker服务
[root@ubuntu2204 ~]#systemctl restart docker

# 查看
[root@ubuntu2204 ~]#docker info
......
 Insecure Registries:
  10.0.0.100
  harbor.mystical.org
  127.0.0.0/8
......

# 推送镜像前，要登录harbor
[root@ubuntu2204 ~]#docker login 10.0.0.100
Username: zhangyifeng
Password: 
# 只需登录一次，登录信息会记录在config.json文件中，无需反复登录
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

# 推送镜像
[root@ubuntu2204 ~]#docker push 10.0.0.100/example/nginx:latest 
The push refers to repository [10.0.0.100/example/nginx]
e2eb04df0bda: Pushed 
1b78ffef68d1: Pushed 
16649054d94a: Pushed 
a280e15d559d: Pushed 
0b2dafd61482: Pushed 
2cdcaebcf23c: Pushed 
7914c8f600f5: Pushed 
latest: digest: sha256:0b2c307c84395005578e9e35ee4bc6c00387cd4573e8098d656245895dc1f7d5 size: 1778

# 浏览器查看
```

![image-20250205232824550](D:\git_repository\cyber_security_learning\markdown_img\image-20250205232824550-1755485801360-14.png)

```bash
# 在10.0.0.100查看harbor数据目录
[root@ubuntu2204 harbor]#du -sh /data/harbor
119M	/data/harbor

# 在其他服务器上拉去harbor上的镜像
# 将其加入insecure-registries
[root@ubuntu2204 ~]#cat /etc/docker/daemon.json 
{
   "registry-mirrors": ["https://si7y70hh.mirror.aliyuncs.com"],
   "insecure-registries": ["harbor.mystical.org", "10.0.0.100"]
}

# 重启docker服务
[root@ubuntu2204 ~]#systemctl restart docker

# 拉取镜像
[root@ubuntu2204 ~]#docker pull 10.0.0.100/example/nginx:latest
latest: Pulling from example/nginx
d2eb42b4a5eb: Pull complete 
ee083de5ceda: Pull complete 
5afd6583b29c: Pull complete 
8c2914db26a3: Pull complete 
1e8aefce6919: Pull complete 
a982d09283a6: Pull complete 
ab571a6216e3: Pull complete 
Digest: sha256:0b2c307c84395005578e9e35ee4bc6c00387cd4573e8098d656245895dc1f7d5
Status: Downloaded newer image for 10.0.0.100/example/nginx:latest
10.0.0.100/example/nginx:latest
```





### 实现Harbor高可用

![image-20250205235448305](D:\git_repository\cyber_security_learning\markdown_img\image-20250205235448305-1755485801360-15.png)

Harbor支持基于策略的Docker镜像复制功能，这类似于MySQL的主从同步，其可以实现不同的数据中 心、不同的运行环境之间同步镜像，并提供友好的管理界面，大大简化了实际运维中的镜像管理工作， 已经有用很多互联网公司使用harbor搭建内网docker仓库的案例，并且还有实现了双向复制功能



#### 安装第二台 harbor主机

在第二台主机上安装部署好harbor，并登录系统

![image-20250205235601361](D:\git_repository\cyber_security_learning\markdown_img\image-20250205235601361-1755485801360-16.png)



#### 第二台harbor上新建项目

参考第一台harbor服务器的项目名称，在第二台harbor服务器上新建与之同名的项目

![image-20250205235735134](D:\git_repository\cyber_security_learning\markdown_img\image-20250205235735134-1755485801360-17.png)

![image-20250206000014158](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000014158-1755485801360-18.png)



#### 在源主机上新建目标

注意：有镜像的，将要传递镜像给目的主机的服务器为源主机，该实验中为10.0.0.100

![image-20250206000235404](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000235404-1755485801360-19.png)

![image-20250206000400238](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000400238-1755485801360-20.png)

![image-20250206000425158](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000425158-1755485801360-21.png)

![image-20250206000450030](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000450030-1755485801360-22.png)



#### 复制管理

![image-20250206000618204](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000618204-1755485801360-23.png)

![image-20250206000746061](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000746061-1755485801360-24.png)

![image-20250206000830129](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000830129-1755485801360-25.png)



#### 初始手动触发复制

![image-20250206000924963](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000924963-1755485801360-26.png)

![image-20250206000934456](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000934456-1755485801360-27.png)

![image-20250206000947520](D:\git_repository\cyber_security_learning\markdown_img\image-20250206000947520-1755485801360-28.png)

![image-20250206001009365](D:\git_repository\cyber_security_learning\markdown_img\image-20250206001009365-1755485801360-29.png)



#### 在目标服务器上查看

![image-20250206001104394](D:\git_repository\cyber_security_learning\markdown_img\image-20250206001104394-1755485801360-30.png)



#### 在镜像上传至源服务器，观察目标服务器

```bash
[root@ubuntu2204 ~]#docker pull alpine
Using default tag: latest
latest: Pulling from library/alpine
1f3e46996e29: Pull complete 
Digest: sha256:56fa17d2a7e7f168a043a2712e63aed1f8543aeafdcee47c58dcffe38ed51099
Status: Downloaded newer image for alpine:latest
docker.io/library/alpine:latest

[root@ubuntu2204 ~]#docker tag alpine:latest 10.0.0.100/example/alpine:latest
[root@ubuntu2204 ~]#docker push 10.0.0.100/example/alpine:latest
The push refers to repository [10.0.0.100/example/alpine]
a0904247e36a: Pushed 
latest: digest: sha256:c10f729849a3b03cbf222e2220245dd44c39a06d444aa32cc30a35c4c1aba59d size: 527
```

**查看源harbor**

![image-20250206001436193](D:\git_repository\cyber_security_learning\markdown_img\image-20250206001436193-1755485801360-31.png)

**查看目标服务器**

![image-20250206001508918](D:\git_repository\cyber_security_learning\markdown_img\image-20250206001508918-1755485801360-32.png)



#### 反向再做一遍，实现双向复制



