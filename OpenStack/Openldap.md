# Openldap 简介

## OpenLDAP 到底是什么？

OpenLDAP：是 LDAP 协议的开源实现。与之关系类似的有：

```ABAP
HTTP 协议
    ↓
Nginx / Apache
```

LDAP：

```ABAP
LDAP 协议
    ↓
OpenLDAP
```





# Docker 部署 Openldap

## 环境准备

- Rocky 9
- docker

在 Rocky 9 中准备 Docker 环境

```bash
# 删除 podman-docker（建议）
[root@ldap /etc/yum.repos.d]# dnf remove -y podman-docker

# 安装基础工具
[root@ldap /etc/yum.repos.d]# dnf install -y yum-utils device-mapper-persistent-data lvm2

# 添加阿里云 Docker Repo
[root@ldap /etc/yum.repos.d]# yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
添加仓库自：https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 安装Docker CE
[root@ldap /etc/yum.repos.d]# yum makecache && dnf install -y docker-ce docker-ce-cli containerd.io

# 启动 Docker
[root@ldap /etc/yum.repos.d]# systemctl enable --now docker
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /usr/lib/systemd/system/docker.service.

# 验证
[root@ldap /etc/yum.repos.d]# systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: disabled)
    Drop-In: /etc/systemd/system/docker.service.d
             └─http-proxy.conf
     Active: active (running) since Mon 2026-05-11 15:00:30 CST; 18s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 6866 (dockerd)
      Tasks: 8
     Memory: 29.3M
        CPU: 219ms
     CGroup: /system.slice/docker.service
             └─6866 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.s>
5月 11 15:00:29 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:29.835252102+08>
5月 11 15:00:29 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:29.839941491+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.106675947+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.116124991+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.116210291+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.119178151+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.119965464+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.128860351+08>
5月 11 15:00:30 ldap.mystical.org dockerd[6866]: time="2026-05-11T15:00:30.128948954+08>
5月 11 15:00:30 ldap.mystical.org systemd[1]: Started Docker Application Container Engi>

# 下载代理脚本
[root@ldap ~]# wget https://www.mysticalrecluse.com/script/Shell/set_docker_proxy.sh

# 启动脚本
# 记得根据自己的实际情况，修改脚本
[root@ldap ~]# bash set_docker_proxy.sh start
Docker 服务代理配置完成!                                   [  OK  ]

# 取消环境变量
[root@ldap ~]# env|grep DOCKER
DOCKER_HOST=unix:///run/podman/podman.sock
[root@ldap ~]# unset DOCKER_HOST
```



## 部署 Openldap

```bash
[root@ldap ~]# docker pull osixia/openldap
[root@ldap ~]# docker pull osixia/phpldapadmin

[root@ldap ~]# docker run -d \
-p 389:389 \
-p 636:636 \
-v /usr/local/ldap:/usr/local/ldap \
-v /opt/ldap:/var/lib/ldap \
-v /opt/slapd.d:/etc/ldap/slapd.d \
-e LDAP_ORGANISATION="mystical" \
-e LDAP_DOMAIN="mystical.org" \
-e LDAP_ADMIN_PASSWORD="123456" \
--name openldap \
--hostname ldap.mystical.com \
osixia/openldap

[root@ldap ~]# docker run -p 80:80 --privileged -d \
--name ldapweb --env PHPLDAPADMIN_HTTPS=false \
--env PHPLDAPADMIN_LDAP_HOSTS=192.168.100.210 \
osixia/phpldapadmin
```

浏览器访问 80 端口查看

![image-20260511151919822](D:\git_repository\cyber_security_learning\markdown_img\image-20260511151919822.png)

## Openldap 基础知识

