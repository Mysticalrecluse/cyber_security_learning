## 实际生产案例—业务迁移

### 业务容器化案例之一业务规划及镜像分层构建

![image-20250419122548232](../markdown_img/image-20250419122548232.png)

![image-20250419122822891](../markdown_img/image-20250419122822891.png)



这种“分层复用 + 规范化构建”的镜像架构设计，有非常多的 **实际好处**，尤其适合企业级、DevOps 规范的环境



#### 优势解析

1️⃣ **镜像分层复用，显著提升构建效率**

- 所有镜像基于官方镜像（如 Ubuntu/CentOS）开始统一构建。
- 再抽象出 “**统一基础镜像**”（如含基础工具、配置、安全组件等），让所有业务镜像构建基于它。
- **Python、JDK8/11、Go、Nginx** 等构建环境只需要构建一次，多个项目复用：
  - 比如：JDK11 + spring基础镜像 → 多个 Spring 项目共享。
  - 镜像构建时 **Docker 分层缓存生效**，只改业务代码就不会重建基础镜像。



2️⃣ **构建链清晰、依赖收敛**

- 你可以通过 Dockerfile `FROM` 路径清楚追踪到每个镜像的祖先镜像。
- 这有利于：
  - 安全漏洞统一扫描和修复。
  - 依赖升级时统一更新底层镜像，不用挨个处理上层服务。



3️⃣ **快速发布与部署**

- Harbor 镜像仓库缓存所有镜像层，在 Kubernetes 节点拉取时：
  - 如果某层镜像已有（如基础层），只需要拉取最上层改动部分 → 加快拉取速度。
- 节省带宽和时间，尤其适用于 CI/CD 高频构建。



4️⃣ **分工协作更清晰**

- 运维/平台团队维护基础镜像（比如 JDK、Python、Nginx 层）。
- 开发团队只负责业务镜像的 `Dockerfile`，关注服务逻辑即可。



5️⃣ **对接 CI/CD 更高效**

- CI 只需 build 最上层镜像即可，构建链条短、速度快。
- 支持 “多阶段构建” 和 “镜像瘦身”



#### 构建底层镜像

```bash
[root@worker-01 centos]# ls
build-command.sh  CentOS-repo.repo  Dockerfile  filebeat-7.6.2-x86_64.rpm

[root@worker-01 centos]#cat Dockerfile 
#自定义Centos 基础镜像
FROM harbor.mysticalrecluse.com/myserver/centos:7.9.2009 
MAINTAINER Mystical mysticalrecluse@gmail.com

ADD filebeat-7.6.2-x86_64.rpm /tmp
RUN rm -rf /etc/yum.repos.d/
ADD CentOS-repo.repo /etc/yum.repos.d/
RUN yum makecache && yum install -y /tmp/filebeat-7.6.2-x86_64.rpm vim wget tree  lrzsz gcc gcc-c++ automake pcre pcre-devel zlib zlib-devel openssl openssl-devel iproute net-tools iotop &&  rm -rf /etc/localtime /tmp/filebeat-7.6.2-x86_64.rpm && ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && useradd  www -u 2020 && useradd nginx -u 2021

[root@worker-01 centos]#cat build-command.sh 
#!/bin/bash
nerdctl build -t  harbor.mysticalrecluse.com/baseimages/mystical-centos-base:7.9.2009 .

nerdctl push harbor.mysticalrecluse.com/baseimages/mystical-centos-base:7.9.2009

# 执行脚本，构建镜像并上传harbor
[root@worker-01 centos]#bash build-command.sh
```



### 业务容器化案例之二Nginx+Tomcat+NFS实现动静分离

![image-20250419160043736](../markdown_img/image-20250419160043736.png)



#### 公共镜像构建

```bash
# 记得提前配置好nfs的动态置备
[root@worker-01 pub-images]# ls
jdk-1.8.212  nginx-base  nginx-base-wordpress  tomcat-base-8.5.43

[root@worker-01 pub-images]#cd jdk-1.8.212/

[root@worker-01 jdk-1.8.212]#ls
build-command.sh  Dockerfile  jdk-8u212-linux-x64.tar.gz  profile

[root@worker-01 jdk-1.8.212]#cat Dockerfile 
#JDK Base Image
FROM harbor.mysticalrecluse.com/baseimages/mystical-centos-base:7.9.2009

MAINTAINER Mystical "mysticalrecluse@gmail.com"


ADD jdk-8u212-linux-x64.tar.gz /usr/local/src/
RUN ln -sv /usr/local/src/jdk1.8.0_212 /usr/local/jdk
ADD profile /etc/profile


ENV JAVA_HOME /usr/local/jdk
ENV JRE_HOME $JAVA_HOME/jre
ENV CLASSPATH $JAVA_HOME/lib/:$JRE_HOME/lib/
ENV PATH $PATH:$JAVA_HOME/bin

[root@worker-01 jdk-1.8.212]#cat build-command.sh 
#!/bin/bash
nerdctl build -t harbor.mysticalrecluse.com/pub-images/jdk-base:v8.212  .
sleep 1
nerdctl push harbor.mysticalrecluse.com/pub-images/jdk-base:v8.212

# 在另一个主机上，测试镜像的java是否正确
[root@master-01 ~]#ssh haproxy1
[root@haproxy1 ~]#docker login harbor.mysticalrecluse.com
Authenticating with existing credentials...
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

[root@haproxy1 ~]#docker pull  harbor.mysticalrecluse.com/pub-images/jdk-base:v8.212
[root@haproxy1 ~]#docker run -it --rm harbor.mysticalrecluse.com/pub-images/jdk-base:v8.212 bash
# 检查java环境是否正常
[root@6674b5290219 /]# java -version
java version "1.8.0_212"
Java(TM) SE Runtime Environment (build 1.8.0_212-b10)
Java HotSpot(TM) 64-Bit Server VM (build 25.212-b10, mixed mode)

# 检查用户是否成功创建
[root@6674b5290219 /]# id nginx
uid=2021(nginx) gid=2021(nginx) groups=2021(nginx)

# 在jdk镜像的基础上，构建tomcat镜像
[root@worker-01 tomcat-base-8.5.43]#ls
apache-tomcat-8.5.43.tar.gz  build-command.sh  Dockerfile

[root@worker-01 tomcat-base-8.5.43]#cat Dockerfile 
#Tomcat 8.5.43基础镜像
FROM harbor.mysticalrecluse.com/pub-images/jdk-base:v8.212

MAINTAINER mystical "mysticalrecluse@gmail.com"

RUN mkdir /apps /data/tomcat/webapps /data/tomcat/logs -pv 
ADD apache-tomcat-8.5.43.tar.gz  /apps
RUN useradd tomcat -u 2022 && ln -sv /apps/apache-tomcat-8.5.43 /apps/tomcat && chown -R tomcat.tomcat /apps /data -R

[root@worker-01 tomcat-base-8.5.43]#cat build-command.sh 
#!/bin/bash
nerdctl build -t harbor.mysticalrecluse.com/pub-images/tomcat-base:v8.5.43  .
sleep 3
nerdctl push  harbor.mysticalrecluse.com/pub-images/tomcat-base:v8.5.43

# 检查tomcat镜像是否正常
[root@haproxy1 ~]#docker run -it --rm -p 8080:8080 harbor.mysticalrecluse.com/pub-images/tomcat-base:v8.5.43 bash
[root@2290a2e9187e /]# cd /apps/tomcat/
[root@2290a2e9187e tomcat]# bash bin/catalina.sh start
[root@2290a2e9187e tomcat]# ss -nlt
State       Recv-Q Send-Q Local Address:Port               Peer Address:Port              
LISTEN      0      100       [::]:8009                  [::]:*                  
LISTEN      0      100       [::]:8080                  [::]:*      # tomcat成功启动


# 打业务镜像
[root@worker-01 ~]# cd /opt/k8s-data/dockerfile/web/magedu
[root@worker-01 magedu]#cd tomcat-app1/
[root@worker-01 tomcat-app1]#ls
app1.tar.gz       Dockerfile                 myapp
build-command.sh  filebeat-7.5.1-x86_64.rpm  run_tomcat.sh
catalina.sh       filebeat.yml               server.xml

# 生产中，这个脚本通常由开发提供
[root@worker-01 tomcat-app1]#cat run_tomcat.sh 
#!/bin/bash
#echo "nameserver 223.6.6.6" > /etc/resolv.conf
#echo "192.168.7.248 k8s-vip.example.com" >> /etc/hosts

#/usr/share/filebeat/bin/filebeat -e -c /etc/filebeat/filebeat.yml -path.home /usr/share/filebeat -path.config /etc/filebeat -path.data /var/lib/filebeat -path.logs /var/log/filebeat &
su - nginx -c "/apps/tomcat/bin/catalina.sh start"
tail -f /etc/hosts

[root@worker-01 tomcat-app1]#cat Dockerfile 
#tomcat web1
FROM harbor.mysticalrecluse.com/pub-images/tomcat-base:v8.5.43 

ADD catalina.sh /apps/tomcat/bin/catalina.sh
ADD server.xml /apps/tomcat/conf/server.xml
#ADD myapp/* /data/tomcat/webapps/myapp/
ADD app1.tar.gz /data/tomcat/webapps/myapp/
ADD run_tomcat.sh /apps/tomcat/bin/run_tomcat.sh
#ADD filebeat.yml /etc/filebeat/filebeat.yml 
RUN chown  -R nginx.nginx /data/ /apps/
#ADD filebeat-7.5.1-x86_64.rpm /tmp/
#RUN cd /tmp && yum localinstall -y filebeat-7.5.1-amd64.deb

EXPOSE 8080 8443

CMD ["/apps/tomcat/bin/run_tomcat.sh"]

[root@worker-01 tomcat-app1]# vim build-command.sh
#!/bin/bash
TAG=$1
nerdctl build -t  harbor.mysticalrecluse.com/myserver/tomcat-app1:${TAG} .
sleep 3
nerdctl push  harbor.mysticalrecluse.com/myserver/tomcat-app1:${TAG}

# 打业务镜像
[root@worker-01 tomcat-app1]#bash build-command.sh v1

# 验证新打的业务镜像
[root@haproxy1 ~]#docker run -it -d --rm -p 8080:8080 harbor.mysticalrecluse.com/myserver/tomcat-app1:v1
a8f682fcf70a722ccd47d4bc6b780c91677318a239b2f9b2790deecbe1ae8516

[root@haproxy1 ~]#curl 10.0.0.209:8080/myapp/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Magedu 门户网站</title>
</head>
<body>
<h1>magedu linux40 v111111111111</h1>
<h1>magedu linux40 v222222222222</h1>
<h1>magedu linux40 v333333333333</h1>
<h1>magedu linux40 v444444444444</h1>
<h1>magedu linux40 v555555555555</h1>
<h1>magedu linux40 v666666666666</h1>
<h1>magedu linux40 v777777777777</h1>
<h1>magedu linux40 v888888888888</h1>
<h1>magedu linux40 v999999999999</h1>
<h1>magedu linux40 v100000000000</h1>
<h1>magedu linux40 v111111111111</h1>
<h1>magedu linux40 v222222222222</h1>
</body>
</html>

# 业务镜像成功

# 镜像打完后，创建yaml文件
[root@master-01 ~]#kubectl create ns proc-test
[root@worker-01 tomcat-app1]#cat tomcat-app1.yaml 
kind: Deployment
#apiVersion: extensions/v1beta1
apiVersion: apps/v1
metadata:
  labels:
    app: magedu-tomcat-app1-deployment-label
  name: magedu-tomcat-app1-deployment
  namespace: proc-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: magedu-tomcat-app1-selector
  template:
    metadata:
      labels:
        app: magedu-tomcat-app1-selector
    spec:
      containers:
      - name: magedu-tomcat-app1-container
        image: harbor.mysticalrecluse.com/myserver/tomcat-app1:v1
        #command: ["/apps/tomcat/bin/run_tomcat.sh"]
        #imagePullPolicy: IfNotPresent
        imagePullPolicy: Always
        ports:
        - containerPort: 8080
          protocol: TCP
          name: http
        env:
        - name: "password"
          value: "123456"
        - name: "age"
          value: "18"
        resources:
          limits:
            cpu: 1
            memory: "512Mi"
          requests:
            cpu: 500m
            memory: "512Mi"
        volumeMounts:
        - name: magedu-images-pvc
          mountPath: /usr/local/nginx/html/webapp/images
          readOnly: false
        - name: magedu-static-pvc
          mountPath: /usr/local/nginx/html/webapp/static
          readOnly: false
      volumes:
      - name: magedu-images-pvc
        persistentVolumeClaim:
          claimName: magedu-images
      - name: magedu-static-pvc
        persistentVolumeClaim:
          claimName: magedu-static
#      nodeSelector:
#        project: magedu
#        app: tomcat
---
kind: Service
apiVersion: v1
metadata:
  labels:
    app: magedu-tomcat-app1-service-label
  name: magedu-tomcat-app1-service
  namespace: proc-test
spec:
  type: NodePort
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 8080
    nodePort: 30003
  selector:
    app: magedu-tomcat-app1-selector

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: magedu-images
  namespace: proc-test
spec:
  storageClassName: sc-nfs # 需要和前面创建的storageClass名称相同
  accessModes: ["ReadWriteMany", "ReadOnlyMany"]
  resources:
    requests:
      storage: 2Gi
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: magedu-static
  namespace: proc-test
spec:
  storageClassName: sc-nfs # 需要和前面创建的storageClass名称相同
  accessModes: ["ReadWriteMany", "ReadOnlyMany"]
  resources:
    requests:
      storage: 2Gi

# 查看
[root@master-01 ~]#kubectl get svc -n proc-test 
NAME                         TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
magedu-tomcat-app1-service   NodePort   10.100.229.89   <none>        80:30003/TCP   21s

[root@master-01 ~]#kubectl get pod -n proc-test 
NAME                                             READY   STATUS    RESTARTS   AGE
magedu-tomcat-app1-deployment-7495bc9c64-knwhn   1/1     Running   0          3m59s

# 访问svc进行测试
[root@master-01 ~]#curl 10.0.0.211:30003/myapp/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Magedu 门户网站</title>
</head>
<body>
<h1>magedu linux40 v111111111111</h1>
<h1>magedu linux40 v222222222222</h1>
<h1>magedu linux40 v333333333333</h1>
<h1>magedu linux40 v444444444444</h1>
<h1>magedu linux40 v555555555555</h1>
<h1>magedu linux40 v666666666666</h1>
<h1>magedu linux40 v777777777777</h1>
<h1>magedu linux40 v888888888888</h1>
<h1>magedu linux40 v999999999999</h1>
<h1>magedu linux40 v100000000000</h1>
<h1>magedu linux40 v111111111111</h1>
<h1>magedu linux40 v222222222222</h1>
</body>
</html>

# 配置Nginx做反向代理和静态服务器
# 打 nginx base 镜像
[root@worker-01 nginx-base]#ls
build-command.sh  Dockerfile  nginx-1.18.0.tar.gz

# 查看 Dockerfile 文件
[root@worker-01 nginx-base]#cat Dockerfile 
#Nginx Base Image
FROM harbor.mysticalrecluse.com/baseimages/mystical-centos-base:7.9.2009

MAINTAINER  mystical mysticalrecluse@gmail.com

RUN yum install -y vim wget tree  lrzsz gcc gcc-c++ automake pcre pcre-devel zlib zlib-devel openssl openssl-devel iproute net-tools iotop
ADD nginx-1.18.0.tar.gz /usr/local/src/
RUN cd /usr/local/src/nginx-1.18.0 && ./configure  && make && make install && ln -sv  /usr/local/nginx/sbin/nginx /usr/sbin/nginx  &&rm -rf /usr/local/src/nginx-1.18.0.tar.gz 

# 查看 build-command.sh 文件
[root@worker-01 nginx-base]#cat build-command.sh 
#!/bin/bash
nerdctl build -t harbor.mysticalrecluse.com/pub-images/nginx-base:v1.18.0  .
sleep 1
nerdctl push harbor.mysticalrecluse.com/pub-images/nginx-base:v1.18.0


# 在nginx-base镜像的基础上，打自己需要的镜像，基础镜像既没有资源也没有配置
[root@worker-01 nginx]#ls
app1.tar.gz  build-command.sh  Dockerfile  index.html  nginx.conf  webapp


# 查看Dockerfile
[root@worker-01 nginx]#cat Dockerfile 
#Nginx 1.18.0
FROM harbor.mysticalrecluse.com/pub-images/nginx-base:v1.18.0 

ADD nginx.conf /usr/local/nginx/conf/nginx.conf
ADD app1.tar.gz  /usr/local/nginx/html/webapp/
ADD index.html  /usr/local/nginx/html/index.html

#静态资源挂载路径
RUN mkdir -p /usr/local/nginx/html/webapp/static /usr/local/nginx/html/webapp/images 

EXPOSE 80 443

CMD ["nginx"] 

# 查看nginx.conf
[root@worker-01 nginx]#cat nginx.conf 
user  nginx nginx;
worker_processes  auto;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;
daemon off;

events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

upstream  tomcat_webserver {
        server  magedu-tomcat-app1-service.proc-test.svc.cluster.local; # 这里写service名称 
}

    server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
        }

        location /webapp {
            root   html;
            index  index.html index.htm;
        }

        location /myapp {
             proxy_pass  http://tomcat_webserver;
             proxy_set_header   Host    $host;
             proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Real-IP $remote_addr;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}


# 查看build-command.sh
[root@worker-01 nginx]#vim build-command.sh 
#!/bin/bash
TAG=$1
nerdctl build -t harbor.mysticalrecluse.com/myserver/nginx-web1:${TAG} .
echo "镜像构建完成，即将上传到harbor"
sleep 1
nerdctl push harbor.mysticalrecluse.com/myserver/nginx-web1:${TAG}
echo "镜像上传到harbor完成"

# 构建镜像
[root@worker-01 nginx]#bash build-command.sh v1

# 编写yaml文件，并部署在Kubernetes上
[root@worker-01 nginx]#vim nginx.yaml
kind: Deployment
apiVersion: apps/v1
metadata:
  labels:
    app: magedu-nginx-deployment-label
  name: magedu-nginx-deployment
  namespace: proc-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: magedu-nginx-selector
  template:
    metadata:
      labels:
        app: magedu-nginx-selector
    spec:
      containers:
      - name: magedu-nginx-container
        image: harbor.magedu.net/magedu/nginx-web1:v3
        #command: ["/apps/tomcat/bin/run_tomcat.sh"]
        #imagePullPolicy: IfNotPresent
        imagePullPolicy: Always
        ports:
        - containerPort: 80
          protocol: TCP
          name: http
        - containerPort: 443
          protocol: TCP
          name: https
        env:
        - name: "password"
          value: "123456"
        - name: "age"
          value: "20"
        resources:
          limits:
            cpu: 2
            memory: 2Gi
          requests:
            cpu: 500m
            memory: 1Gi

        volumeMounts:
        - name: magedu-images-pvc
          mountPath: /usr/local/nginx/html/webapp/images
          readOnly: false
        - name: magedu-static-pvc
          mountPath: /usr/local/nginx/html/webapp/static
          readOnly: false
      volumes:
      - name: magedu-images-pvc
        persistentVolumeClaim:
          claimName: magedu-images
      - name: magedu-static-pvc
        persistentVolumeClaim:
          claimName: magedu-static

      #  group: magedu

---
kind: Service
apiVersion: v1
metadata:
  labels:
    app: magedu-nginx-service-label
  name: magedu-nginx-service
  namespace: proc-test
spec:
  type: NodePort
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
    nodePort: 40002
  - name: https
    port: 443
    protocol: TCP
    targetPort: 443
    nodePort: 40443
  selector:
    app: magedu-nginx-selector

# 启用pod
[root@master-01 ~]#kubectl apply -f nginx.yaml 

# 查看
[root@master-01 ~]#kubectl get all -n proc-test 
NAME                                                 READY   STATUS    RESTARTS      AGE
pod/magedu-nginx-deployment-7455c575bc-92qs9         1/1     Running   0             34m
pod/magedu-tomcat-app1-deployment-7495bc9c64-knwhn   1/1     Running   1 (97m ago)   12h

NAME                                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/magedu-nginx-service         NodePort    10.100.135.150   <none>        80:30002/TCP,443:30443/TCP   34m
service/magedu-tomcat-app1-service   ClusterIP   10.100.229.89    <none>        80/TCP                       12h

# 测试
[root@master-01 ~]#curl 10.0.0.211:30002
nginx web1 n56 v1
```



### 业务容器化案例之三PV与PVC及zookeeper

zookeeper集群的每个实例的存储是独立的，因此建议使用openebs的host-path



**整体流程**

- 构建zookeeper镜像
- 测试zookeeper镜像
- 创建PV/PVC
- 运行zookeeper集群
- 验证集群状态

```bash
# 拉取slim_java:8,java环境的基础镜像，并上传至私有harbor
[root@worker-01 ~]#nerdctl pull elevy/slim_java:8
[root@worker-01 ~]#nerdctl tag elevy/slim_java:8 harbor.mysticalrecluse.com/baseimages/slim_java:8
[root@worker-01 ~]#nerdctl push harbor.mysticalrecluse.com/baseimages/slim_java:8

# 打zookeeper的镜像
[root@worker-01 zookeeper]#ls
bin               entrypoint.sh                     zookeeper-3.4.14.tar.gz
build-command.sh  KEYS                              zookeeper-3.4.14.tar.gz.asc
conf              repositories
Dockerfile        zookeeper-3.12-Dockerfile.tar.gz

# 查看Dockerfile
[root@worker-01 zookeeper]#cat Dockerfile 
#FROM harbor-linux38.local.com/linux38/slim_java:8 
FROM harbor.mysticalrecluse.com/baseimages/slim_java:8

ENV ZK_VERSION 3.4.14
ADD repositories /etc/apk/repositories 
# Download Zookeeper
COPY zookeeper-3.4.14.tar.gz /tmp/zk.tgz
COPY zookeeper-3.4.14.tar.gz.asc /tmp/zk.tgz.asc
COPY KEYS /tmp/KEYS
RUN apk add --no-cache --virtual .build-deps \
      ca-certificates   \
      gnupg             \
      tar               \
      wget &&           \
    #
    # Install dependencies
    apk add --no-cache  \
      bash &&           \
    #
    #
    # Verify the signature
    export GNUPGHOME="$(mktemp -d)" && \
    gpg -q --batch --import /tmp/KEYS && \
    gpg -q --batch --no-auto-key-retrieve --verify /tmp/zk.tgz.asc /tmp/zk.tgz && \
    #
    # Set up directories
    #
    mkdir -p /zookeeper/data /zookeeper/wal /zookeeper/log && \
    #
    # Install
    tar -x -C /zookeeper --strip-components=1 --no-same-owner -f /tmp/zk.tgz && \
    #
    # Slim down
    cd /zookeeper && \
    cp dist-maven/zookeeper-${ZK_VERSION}.jar . && \
    rm -rf \
      *.txt \
      *.xml \
      bin/README.txt \
      bin/*.cmd \
      conf/* \
      contrib \
      dist-maven \
      docs \
      lib/*.txt \
      lib/cobertura \
      lib/jdiff \
      recipes \
      src \
      zookeeper-*.asc \
      zookeeper-*.md5 \
      zookeeper-*.sha1 && \
    #
    # Clean up
    apk del .build-deps && \
    rm -rf /tmp/* "$GNUPGHOME"

COPY conf /zookeeper/conf/
COPY bin/zkReady.sh /zookeeper/bin/
COPY entrypoint.sh /

ENV PATH=/zookeeper/bin:${PATH} \
    ZOO_LOG_DIR=/zookeeper/log \
    ZOO_LOG4J_PROP="INFO, CONSOLE, ROLLINGFILE" \
    JMXPORT=9010

ENTRYPOINT [ "/entrypoint.sh" ]

CMD [ "zkServer.sh", "start-foreground" ]

EXPOSE 2181 2888 3888 9010


# 查看entrypoint.sh
[root@worker-01 zookeeper]#cat entrypoint.sh 
#!/bin/bash

echo ${MYID:-1} > /zookeeper/data/myid

if [ -n "$SERVERS" ]; then
	IFS=\, read -a servers <<<"$SERVERS"
	for i in "${!servers[@]}"; do 
		printf "\nserver.%i=%s:2888:3888" "$((1 + $i))" "${servers[$i]}" >> /zookeeper/conf/zoo.cfg
	done
fi

cd /zookeeper
exec "$@"

[root@worker-01 zookeeper]#cat build-command.sh 
#!/bin/bash
TAG=$1
nerdctl build -t harbor.mysticalrecluse.com/myserver/zookeeper:${TAG} .
sleep 1
nerdctl push  harbor.mysticalrecluse.com/myserver/zookeeper:${TAG}

# 打镜像
[root@worker-01 zookeeper]#bash build-command.sh 
```

```yaml
# 准备yaml文件
[root@worker-01 zookeeper]#cat zookeeper.yaml 
apiVersion: v1
kind: Service
metadata:
  name: zookeeper
  namespace: proc-test
spec:
  ports:
    - name: client
      port: 2181
  selector:
    app: zookeeper
---
apiVersion: v1
kind: Service
metadata:
  name: zookeeper1
  namespace: proc-test
spec:
  type: NodePort        
  ports:
    - name: client
      port: 2181
      nodePort: 32181
    - name: followers
      port: 2888
    - name: election
      port: 3888
  selector:
    app: zookeeper
    server-id: "1"
---
apiVersion: v1
kind: Service
metadata:
  name: zookeeper2
  namespace: proc-test
spec:
  type: NodePort        
  ports:
    - name: client
      port: 2181
      nodePort: 32182
    - name: followers
      port: 2888
    - name: election
      port: 3888
  selector:
    app: zookeeper
    server-id: "2"
---
apiVersion: v1
kind: Service
metadata:
  name: zookeeper3
  namespace: proc-test
spec:
  type: NodePort        
  ports:
    - name: client
      port: 2181
      nodePort: 32183
    - name: followers
      port: 2888
    - name: election
      port: 3888
  selector:
    app: zookeeper
    server-id: "3"
---
kind: Deployment
#apiVersion: extensions/v1beta1
apiVersion: apps/v1
metadata:
  name: zookeeper1
  namespace: proc-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: zookeeper
  template:
    metadata:
      labels:
        app: zookeeper
        server-id: "1"
    spec:
      volumes:
        - name: data
          emptyDir: {}
        - name: wal
          emptyDir:
            medium: Memory
      containers:
        - name: server
          image: harbor.mysticalrecluse.com/myserver/zookeeper:v3.4.14
          imagePullPolicy: Always
          env:
            - name: MYID
              value: "1"
            - name: SERVERS
              value: "zookeeper1,zookeeper2,zookeeper3"
            - name: JVMFLAGS
              value: "-Xmx2G"
          ports:
            - containerPort: 2181
            - containerPort: 2888
            - containerPort: 3888
          volumeMounts:
          - mountPath: "/zookeeper/data"
            name: zookeeper-datadir-pvc-1 
      volumes:
        - name: zookeeper-datadir-pvc-1 
          persistentVolumeClaim:
            claimName: zookeeper-datadir-pvc-1
---
kind: Deployment
#apiVersion: extensions/v1beta1
apiVersion: apps/v1
metadata:
  name: zookeeper2
  namespace: proc-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: zookeeper
  template:
    metadata:
      labels:
        app: zookeeper
        server-id: "2"
    spec:
      volumes:
        - name: data
          emptyDir: {}
        - name: wal
          emptyDir:
            medium: Memory
      containers:
        - name: server
          image: harbor.mysticalrecluse.com/myserver/zookeeper:v3.4.14
          imagePullPolicy: Always
          env:
            - name: MYID
              value: "2"
            - name: SERVERS
              value: "zookeeper1,zookeeper2,zookeeper3"
            - name: JVMFLAGS
              value: "-Xmx2G"
          ports:
            - containerPort: 2181
            - containerPort: 2888
            - containerPort: 3888
          volumeMounts:
          - mountPath: "/zookeeper/data"
            name: zookeeper-datadir-pvc-2 
      volumes:
        - name: zookeeper-datadir-pvc-2
          persistentVolumeClaim:
            claimName: zookeeper-datadir-pvc-2
---
kind: Deployment
#apiVersion: extensions/v1beta1
apiVersion: apps/v1
metadata:
  name: zookeeper3
  namespace: proc-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: zookeeper
  template:
    metadata:
      labels:
        app: zookeeper
        server-id: "3"
    spec:
      volumes:
        - name: data
          emptyDir: {}
        - name: wal
          emptyDir:
            medium: Memory
      containers:
        - name: server
          image: harbor.mysticalrecluse.com/myserver/zookeeper:v3.4.14
          imagePullPolicy: Always
          env:
            - name: MYID
              value: "3"
            - name: SERVERS
              value: "zookeeper1,zookeeper2,zookeeper3"
            - name: JVMFLAGS
              value: "-Xmx2G"
          ports:
            - containerPort: 2181
            - containerPort: 2888
            - containerPort: 3888
          volumeMounts:
          - mountPath: "/zookeeper/data"
            name: zookeeper-datadir-pvc-3
      volumes:
        - name: zookeeper-datadir-pvc-3
          persistentVolumeClaim:
           claimName: zookeeper-datadir-pvc-3
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: zookeeper-datadir-pvc-1
  namespace: proc-test
spec:
  storageClassName: openebs-hostpath-dynamic
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: zookeeper-datadir-pvc-2
  namespace: proc-test
spec:
  storageClassName: openebs-hostpath-dynamic
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: zookeeper-datadir-pvc-3
  namespace: proc-test
spec:
  storageClassName: openebs-hostpath-dynamic
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
      
# 创建
[root@master-01 ~] # kubectl apply -f zookeeper.yaml

# 查看
[root@master-01 ~] # kubectl get all -n proc-test 
NAME                                                 READY   STATUS    RESTARTS     AGE
pod/magedu-nginx-deployment-7455c575bc-92qs9         1/1     Running   0            8h
pod/magedu-tomcat-app1-deployment-7495bc9c64-knwhn   1/1     Running   1 (9h ago)   20h
pod/zookeeper1-98785f44d-xr7cs                       1/1     Running   0            3m32s
pod/zookeeper2-54d4775745-hrnrc                      1/1     Running   0            3m32s
pod/zookeeper3-5d699cb6d6-pvv8m                      1/1     Running   0            3m31s

NAME                                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                        AGE
service/magedu-nginx-service         NodePort    10.100.135.150   <none>        80:30002/TCP,443:30443/TCP                     8h
service/magedu-tomcat-app1-service   ClusterIP   10.100.229.89    <none>        80/TCP                                         20h
service/zookeeper                    ClusterIP   10.100.62.34     <none>        2181/TCP                                       3m32s
service/zookeeper1                   NodePort    10.100.222.44    <none>        2181:32181/TCP,2888:30203/TCP,3888:30170/TCP   2m38s
service/zookeeper2                   NodePort    10.100.42.100    <none>        2181:32182/TCP,2888:32757/TCP,3888:32659/TCP   2m37s
service/zookeeper3                   NodePort    10.100.194.154   <none>        2181:32183/TCP,2888:30362/TCP,3888:30488/TCP   2m37s

NAME                                            READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/magedu-nginx-deployment         1/1     1            1           8h
deployment.apps/magedu-tomcat-app1-deployment   1/1     1            1           20h
deployment.apps/zookeeper1                      1/1     1            1           3m32s
deployment.apps/zookeeper2                      1/1     1            1           3m32s
deployment.apps/zookeeper3                      1/1     1            1           3m32s

NAME                                                       DESIRED   CURRENT   READY   AGE
replicaset.apps/magedu-nginx-deployment-7455c575bc         1         1         1       8h
replicaset.apps/magedu-tomcat-app1-deployment-7495bc9c64   1         1         1       20h
replicaset.apps/zookeeper1-98785f44d                       1         1         1       3m32s
replicaset.apps/zookeeper2-54d4775745                      1         1         1       3m32s
replicaset.apps/zookeeper3-5d699cb6d6                      1         1         1       3m31s

# 查看集群状态
[root@master-01 ~]#kubectl exec -it -n proc-test zookeeper1-98785f44d-xr7cs -- bash
bash-4.3# cd /zookeeper/bin/
bash-4.3# ls
zkCleanup.sh        zkEnv.sh            zkServer.sh
zkCli.sh            zkReady.sh          zkTxnLogToolkit.sh
bash-4.3# zkServer.sh status
ZooKeeper JMX enabled by default
ZooKeeper remote JMX Port set to 9010
ZooKeeper remote JMX authenticate set to false
ZooKeeper remote JMX ssl set to false
ZooKeeper remote JMX log4j set to true
Using config: /zookeeper/bin/../conf/zoo.cfg
Mode: follower
```



### 业务容器化案例之四Redis-Cluster—StatefulSet

```bash
# 构建redis镜像
# 查看目录文件
[root@worker-01 redis]#ls
build-command.sh  Dockerfile  redis-4.0.14.tar.gz  redis.conf  run_redis.sh

# 查看Dockerfile
[root@worker-01 redis]#cat Dockerfile 
#Redis Image
FROM harbor.mysticalrecluse.com/baseimages/mystical-centos-base:7.9.2009 

MAINTAINER mystical "mysticalrecluse@gmail.com"

ADD redis-4.0.14.tar.gz /usr/local/src
RUN ln -sv /usr/local/src/redis-4.0.14 /usr/local/redis && cd /usr/local/redis && make && cp src/redis-cli /usr/sbin/ && cp src/redis-server  /usr/sbin/ && mkdir -pv /data/redis-data 
ADD redis.conf /usr/local/redis/redis.conf 
ADD run_redis.sh /usr/local/redis/run_redis.sh

EXPOSE 6379

CMD ["/usr/local/redis/run_redis.sh"]

# 查看run_redis.sh
[root@worker-01 redis]#cat run_redis.sh 
#!/bin/bash

/usr/sbin/redis-server /usr/local/redis/redis.conf

tail -f  /etc/hosts

# 查看build-command.sh
[root@worker-01 redis]#cat build-command.sh 
#!/bin/bash
TAG=$1
nerdctl build -t harbor.mysticalrecluse.com/myserver/redis:${TAG} .
sleep 3
nerdctl push  harbor.mysticalrecluse.com/myserver/redis:${TAG}

[root@worker-01 redis]# bash build-command.sh v4.0.14
```

```bash
[root@worker-01 redis]#ls
pv  pvc.yaml  redis.conf  redis.yaml

# 查看redis.conf
[root@worker-01 redis]#cat redis.conf 
appendonly yes
cluster-enabled yes
cluster-config-file /var/lib/redis/nodes.conf
cluster-node-timeout 5000
port 6379


# 基于redis.conf创建configmap
[root@master-01 ~]#kubectl create cm -n proc-test redis-conf --from-file=redis.conf
configmap/redis-conf created

# 查看redis-cluster.yaml
[root@master-01 ~]#cat redis-cluster.yaml 
apiVersion: v1
kind: Service
metadata:
  name: redis              # 无头服务的名称必须和sts的名称一致
  namespace: proc-test
  labels:
    app: redis
spec:
  clusterIP: None    # 这里必须是无头服务，否则pod的名称无法被解析
  selector:
    app: redis
    appCluster: redis-cluster
  ports:
  - name: redis-access
    protocol: TCP
    port: 6379
    targetPort: 6379

---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis
  namespace: proc-test
spec:
  serviceName: redis
  replicas: 6
  selector:
    matchLabels:
      app: redis
      appCluster: redis-cluster
  template:
    metadata:
      labels:
        app: redis
        appCluster: redis-cluster
    spec:
      terminationGracePeriodSeconds: 20  # 控制 Pod 优雅终止（graceful termination） 的时长
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values: 
                  - redis
              topologyKey: kubernetes.io/hostname
      containers:
      - name: redis
        image:  harbor.mysticalrecluse.com/myserver/redis:v4.0.14
        command:
        - "redis-server"
        args:
        - "/etc/redis/redis.conf"
        - "--protected-mode"
        - "no"
        resources:
          requests:
            cpu: "500m"
            memory: "500Mi"
        ports:
        - containerPort: 6379
          name: redis
          protocol: TCP
        - containerPort: 16379
          name: cluster
          protocol: TCP
        volumeMounts:
        - name: conf
          mountPath: /etc/redis
        - name: data
          mountPath: /var/lib/redis
      volumes:
      - name: conf
        configMap:
          name: redis-conf
          items:
          - key: redis.conf
            path: redis.conf
  volumeClaimTemplates:
  - metadata:
      name: data
      namespace: proc-test
    spec:
      storageClassName: sc-nfs
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 2Gi

# 创建初始化pod，来初始化redis-cluster集群
# 注意redis-cluster需要手动初始化，或者自己写自动交互的脚本
# 将Roby升级到 >= 2.5
# 安装依赖
yum install -y git gcc bzip2 openssl-devel readline-devel zlib-devel

# 安装 rbenv 和 ruby-build
cd /usr/local/
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init - bash)"' >> ~/.bashrc
source ~/.bashrc

# 安装 ruby-build 插件
git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build

# 安装新版本 Ruby（比如 2.7.8）
rbenv install 2.7.8
rbenv global 2.7.8

# 确认版本
ruby -v

# 执行命令加入，构建redis-cluster集群
[root@redis-0 local]# /usr/local/redis/src/redis-trib.rb create --replicas 1 `dig +short redis-0.redis.proc-test.svc.cluster.local`:6379 `dig +short redis-1.redis.proc-test.svc.cluster.local`:6379 `dig +short redis-2.redis.proc-test.svc.cluster.local`:6379 `dig +short redis-3.redis.proc-test.svc.cluster.local`:6379 `dig +short redis-4.redis.proc-test.svc.cluster.local`:6379 `dig +short redis-5.redis.proc-test.svc.cluster.local`:6379
>>> Creating cluster
>>> Performing hash slots allocation on 6 nodes...
Using 3 masters:
10.200.129.54:6379
10.200.171.22:6379
10.200.37.196:6379
Adding replica 10.200.129.55:6379 to 10.200.129.54:6379
Adding replica 10.200.37.197:6379 to 10.200.171.22:6379
Adding replica 10.200.171.24:6379 to 10.200.37.196:6379
M: 39e9771fd059575af855f2efda5e5112948a41e8 10.200.129.54:6379
   slots:0-5460 (5461 slots) master
M: 26f2ce3bcfd07f4b87e01898c54439a0811af48a 10.200.171.22:6379
   slots:5461-10922 (5462 slots) master
M: 218842546042fac985f2402879e9c314e4dbbee8 10.200.37.196:6379
   slots:10923-16383 (5461 slots) master
S: 6c69be742223206fa3ce23726569be32a56ac4c6 10.200.171.24:6379
   replicates 218842546042fac985f2402879e9c314e4dbbee8
S: e70cedcbbb13fc6e387c1e959238526848d529d1 10.200.129.55:6379
   replicates 39e9771fd059575af855f2efda5e5112948a41e8
S: 7ce117f59196f58de867ab06456e4aee578b6496 10.200.37.197:6379
   replicates 26f2ce3bcfd07f4b87e01898c54439a0811af48a
Can I set the above configuration? (type 'yes' to accept): yes    # 选择yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join...
>>> Performing Cluster Check (using node 10.200.129.54:6379)
M: 39e9771fd059575af855f2efda5e5112948a41e8 10.200.129.54:6379
   slots:0-5460 (5461 slots) master
   1 additional replica(s)
S: e70cedcbbb13fc6e387c1e959238526848d529d1 10.200.129.55:6379
   slots: (0 slots) slave
   replicates 39e9771fd059575af855f2efda5e5112948a41e8
M: 218842546042fac985f2402879e9c314e4dbbee8 10.200.37.196:6379
   slots:10923-16383 (5461 slots) master
   1 additional replica(s)
S: 6c69be742223206fa3ce23726569be32a56ac4c6 10.200.171.24:6379
   slots: (0 slots) slave
   replicates 218842546042fac985f2402879e9c314e4dbbee8
S: 7ce117f59196f58de867ab06456e4aee578b6496 10.200.37.197:6379
   slots: (0 slots) slave
   replicates 26f2ce3bcfd07f4b87e01898c54439a0811af48a
M: 26f2ce3bcfd07f4b87e01898c54439a0811af48a 10.200.171.22:6379
   slots:5461-10922 (5462 slots) master
   1 additional replica(s)
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.

# 检查redis集群效果，-c启用集群模式，Redis CLI 会自动跟随 MOVED 跳转到正确的节点。
root@redis-0 local]# redis-cli -c -a 123456
Warning: Using a password with '-a' option on the command line interface may not be safe.
127.0.0.1:6379> set key1 value1
-> Redirected to slot [9189] located at 10.200.171.22:6379
OK
10.200.171.22:6379> set key2 value2
-> Redirected to slot [4998] located at 10.200.129.54:6379
OK
10.200.129.54:6379> get key1
-> Redirected to slot [9189] located at 10.200.171.22:6379
"value1"
10.200.171.22:6379> get key1
"value1"
10.200.171.22:6379> get key2
-> Redirected to slot [4998] located at 10.200.129.54:6379
"value2"
```



### 业务容器化案例之五MySQL一主多从

![image-20250421171035342](../markdown_img/image-20250421171035342.png)



#### 准备镜像

```bash
# 上传mysql镜像
[root@worker-01 mysql]#nerdctl pull mysql:5.7.36
[root@worker-01 mysql]#nerdctl tag mysql:5.7.36 harbor.mysticalrecluse.com/myserver/mysql:5.7.36
[root@worker-01 mysql]#nerdctl push harbor.mysticalrecluse.com/myserver/mysql:5.7.36

# 上传xtrabackup镜像
[root@worker-01 mysql]#nerdctl pull yizhiyong/xtrabackup:latest
[root@worker-01 mysql]#nerdctl tag yizhiyong/xtrabackup:latest harbor.mysticalrecluse.com/myserver/xtrabackup:1.0
[root@worker-01 mysql]#nerdctl push harbor.mysticalrecluse.com/myserver/xtrabackup:1.0
```



####  准备yaml清单文件

```bash
# configmap文件
[root@worker-01 mysql]#cat mysql-configmap.yaml 
apiVersion: v1
kind: ConfigMap
metadata:
  name: mysql
  namespace: magedu
  labels:
    app: mysql
data:
  master.cnf: |
    # Apply this config only on the master.
    [mysqld]
    log-bin
    log_bin_trust_function_creators=1
    lower_case_table_names=1
  slave.cnf: |
    # Apply this config only on slaves.
    [mysqld]
    super-read-only
    log_bin_trust_function_creators=1
    
# 准备statefulSet
[root@worker-01 mysql]#cat mysql-statefulset.yaml 
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
  namespace: proc-test
spec:
  selector:
    matchLabels:
      app: mysql
  serviceName: mysql
  replicas: 3
  template:
    metadata:
      labels:
        app: mysql
    spec:
      initContainers:
      - name: init-mysql
        image: harbor.mysticalrecluse.com/myserver/mysql:5.7.36
        command:
        - bash
        - "-c"
        - |
          set -ex
          # Generate mysql server-id from pod ordinal index.
          [[ `hostname` =~ -([0-9]+)$ ]] || exit 1
          # BASH_REMATCH 是 Bash 的一个内置变量，只有在使用 [[ string =~ regex ]] 正则匹配语法时才会自动创建和赋值。
          # BASH_REMATCH[0]：整个正则匹配到的内容
          # BASH_REMATCH[1]：第一个括号捕获组
          ordinal=${BASH_REMATCH[1]}
          echo [mysqld] > /mnt/conf.d/server-id.cnf
          # Add an offset to avoid reserved server-id=0 value.
          echo server-id=$((100 + $ordinal)) >> /mnt/conf.d/server-id.cnf
          # Copy appropriate conf.d files from config-map to emptyDir.
          if [[ $ordinal -eq 0 ]]; then
            cp /mnt/config-map/master.cnf /mnt/conf.d/
          else
            cp /mnt/config-map/slave.cnf /mnt/conf.d/
          fi
        volumeMounts:
        - name: conf
          mountPath: /mnt/conf.d
        - name: config-map
          mountPath: /mnt/config-map
      - name: clone-mysql
        image: harbor.mysticalrecluse.com/myserver/xtrabackup:1.0 
        command:
        - bash
        - "-c"
        - |
          set -ex
          # Skip the clone if data already exists.
          [[ -d /var/lib/mysql/mysql ]] && exit 0
          # Skip the clone on master (ordinal index 0).
          [[ `hostname` =~ -([0-9]+)$ ]] || exit 1
          ordinal=${BASH_REMATCH[1]}
          [[ $ordinal -eq 0 ]] && exit 0
          # Clone data from previous peer.
          ncat --recv-only mysql-$(($ordinal-1)).mysql 3307 | xbstream -x -C /var/lib/mysql
          # Prepare the backup.
          xtrabackup --prepare --target-dir=/var/lib/mysql
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
          subPath: mysql
        - name: conf
          mountPath: /etc/mysql/conf.d
      containers:
      - name: mysql
        image: harbor.mysticalrecluse.com/myserver/mysql:5.7.36 
        env:
        - name: MYSQL_ALLOW_EMPTY_PASSWORD
          value: "1"
        ports:
        - name: mysql
          containerPort: 3306
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
          subPath: mysql
        - name: conf
          mountPath: /etc/mysql/conf.d
        resources:
          requests:
            cpu: 500m
            memory: 1Gi
        livenessProbe:
          exec:
            command: ["mysqladmin", "ping"]
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
        readinessProbe:
          exec:
            # Check we can execute queries over TCP (skip-networking is off).
            command: ["mysql", "-h", "127.0.0.1", "-e", "SELECT 1"]
          initialDelaySeconds: 5
          periodSeconds: 2
          timeoutSeconds: 1
      - name: xtrabackup
        image: harbor.mysticalrecluse.com/myserver/xtrabackup:1.0 
        ports:
        - name: xtrabackup
          containerPort: 3307
        command:
        - bash
        - "-c"
        - |
          set -ex
          cd /var/lib/mysql
          # Determine binlog position of cloned data, if any.
          if [[ -f xtrabackup_slave_info ]]; then
            # XtraBackup already generated a partial "CHANGE MASTER TO" query
            # because we're cloning from an existing slave.
            mv xtrabackup_slave_info change_master_to.sql.in
            # Ignore xtrabackup_binlog_info in this case (it's useless).
            rm -f xtrabackup_binlog_info
          elif [[ -f xtrabackup_binlog_info ]]; then
            # We're cloning directly from master. Parse binlog position.
            [[ `cat xtrabackup_binlog_info` =~ ^(.*?)[[:space:]]+(.*?)$ ]] || exit 1
            rm xtrabackup_binlog_info
            echo "CHANGE MASTER TO MASTER_LOG_FILE='${BASH_REMATCH[1]}',\
                  MASTER_LOG_POS=${BASH_REMATCH[2]}" > change_master_to.sql.in
          fi
          # Check if we need to complete a clone by starting replication.
          if [[ -f change_master_to.sql.in ]]; then
            echo "Waiting for mysqld to be ready (accepting connections)"
            until mysql -h 127.0.0.1 -e "SELECT 1"; do sleep 1; done
            echo "Initializing replication from clone position"
            # In case of container restart, attempt this at-most-once.
            mv change_master_to.sql.in change_master_to.sql.orig
            mysql -h 127.0.0.1 <<EOF
          $(<change_master_to.sql.orig),
            MASTER_HOST='mysql-0.mysql',
            MASTER_USER='root',
            MASTER_PASSWORD='',
            MASTER_CONNECT_RETRY=10;
          START SLAVE;
          EOF
          fi
          # Start a server to send backups when requested by peers.
          exec ncat --listen --keep-open --send-only --max-conns=1 3307 -c \
            "xtrabackup --backup --slave-info --stream=xbstream --host=127.0.0.1 --user=root"
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
          subPath: mysql
        - name: conf
          mountPath: /etc/mysql/conf.d
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
      volumes:
      - name: conf
        emptyDir: {}
      - name: config-map
        configMap:
          name: mysql
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      storageClassName: openebs-hostpath-dynamic
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 2Gi

# 准备service
[root@worker-01 mysql]#cat mysql-services.yaml 
# Headless service for stable DNS entries of StatefulSet members.
apiVersion: v1
kind: Service
metadata:
  namespace: proc-test
  name: mysql
  labels:
    app: mysql
spec:
  ports:
  - name: mysql
    port: 3306
  clusterIP: None
  selector:
    app: mysql
---
# Client service for connecting to any MySQL instance for reads.
# For writes, you must instead connect to the master: mysql-0.mysql.
apiVersion: v1
kind: Service
metadata:
  name: mysql-read
  namespace: proc-test
  labels:
    app: mysql
spec:
  ports:
  - name: mysql
    port: 3306
  selector:
    app: mysql
```

```bash
# 启用清单文件
[root@master-01 ~]# kubectl apply -f mysql-cm.yaml 
[root@master-01 ~]#kubectl apply -f mysql-sts.yaml
[root@master-01 ~]#kubectl apply -f mysql-service.yaml

# 测试集群是否ok
[root@master-01 ~]#kubectl exec -it -n proc-test mysql-0 bash
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
Defaulted container "mysql" out of: mysql, xtrabackup, init-mysql (init), clone-mysql (init)
root@mysql-0:/# mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 124
Server version: 5.7.36-log MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show processlist;
+-----+------+---------------------+------+-------------+------+---------------------------------------------------------------+------------------+
| Id  | User | Host                | db   | Command     | Time | State                                                         | Info             |
+-----+------+---------------------+------+-------------+------+---------------------------------------------------------------+------------------+
|  44 | root | 10.200.129.57:57592 | NULL | Binlog Dump |  137 | Master has sent all binlog to slave; waiting for more updates | NULL             |
|  87 | root | 10.200.37.199:58828 | NULL | Binlog Dump |   67 | Master has sent all binlog to slave; waiting for more updates | NULL             |
| 124 | root | localhost           | NULL | Query       |    0 | starting                                                      | show processlist |
+-----+------+---------------------+------+-------------+------+---------------------------------------------------------------+------------------+
3 rows in set (0.00 sec)

mysql> exit
Bye
```



### 业务容器化案例之六Java应用-Jenkins



![image-20250421222125054](../markdown_img/image-20250421222125054.png)



#### 构建java17基础镜像

```bash
[root@worker-01 jdk-17]#ls
build-command.sh  Dockerfile  jdk-17.0.15_linux-x64_bin.tar.gz  profile

# 查看profile
[root@worker-01 jdk-17]#cat profile 
# /etc/profile

# System wide environment and startup programs, for login setup
# Functions and aliases go in /etc/bashrc

# It's NOT a good idea to change this file unless you know what you
# are doing. It's much better to create a custom.sh shell script in
# /etc/profile.d/ to make custom changes to your environment, as this
# will prevent the need for merging in future updates.

pathmunge () {
    case ":${PATH}:" in
        *:"$1":*)
            ;;
        *)
            if [ "$2" = "after" ] ; then
                PATH=$PATH:$1
            else
                PATH=$1:$PATH
            fi
    esac
}


if [ -x /usr/bin/id ]; then
    if [ -z "$EUID" ]; then
        # ksh workaround
        EUID=`/usr/bin/id -u`
        UID=`/usr/bin/id -ru`
    fi
    USER="`/usr/bin/id -un`"
    LOGNAME=$USER
    MAIL="/var/spool/mail/$USER"
fi

# Path manipulation
if [ "$EUID" = "0" ]; then
    pathmunge /usr/sbin
    pathmunge /usr/local/sbin
else
    pathmunge /usr/local/sbin after
    pathmunge /usr/sbin after
fi

HOSTNAME=`/usr/bin/hostname 2>/dev/null`
HISTSIZE=1000
if [ "$HISTCONTROL" = "ignorespace" ] ; then
    export HISTCONTROL=ignoreboth
else
    export HISTCONTROL=ignoredups
fi

export PATH USER LOGNAME MAIL HOSTNAME HISTSIZE HISTCONTROL

# By default, we want umask to get set. This sets it for login shell
# Current threshold for system reserved uid/gids is 200
# You could check uidgid reservation validity in
# /usr/share/doc/setup-*/uidgid file
if [ $UID -gt 199 ] && [ "`/usr/bin/id -gn`" = "`/usr/bin/id -un`" ]; then
    umask 002
else
    umask 022
fi

for i in /etc/profile.d/*.sh /etc/profile.d/sh.local ; do
    if [ -r "$i" ]; then
        if [ "${-#*i}" != "$-" ]; then 
            . "$i"
        else
            . "$i" >/dev/null
        fi
    fi
done

unset i
unset -f pathmunge
export LANG=en_US.UTF-8
export HISTTIMEFORMAT="%F %T `whoami` "

export JAVA_HOME=/usr/local/jdk
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.$CLASSPATH:$JAVA_HOME/lib

# 查看Dockerfile
[root@worker-01 jdk-17]#cat Dockerfile 
#JDK Base Image
FROM harbor.mysticalrecluse.com/baseimages/mystical-centos-base:7.9.2009

MAINTAINER Mystical "mysticalrecluse@gmail.com"

ADD jdk-17.0.15_linux-x64_bin.tar.gz /usr/local/src/
RUN ln -sv /usr/local/src/jdk-17.0.15 /usr/local/jdk
ADD profile /etc/profile


ENV JAVA_HOME /usr/local/jdk
ENV CLASSPATH $JAVA_HOME/lib/
ENV PATH $PATH:$JAVA_HOME/bin

# 查看build-command.sh
[root@worker-01 jdk-17]#cat build-command.sh 
#!/bin/bash
nerdctl build -t harbor.mysticalrecluse.com/pub-images/jdk-base:v17.0.15 .
sleep 1
nerdctl push harbor.mysticalrecluse.com/pub-images/jdk-base:v17.0.15

# 构建镜像
[root@worker-01 jdk-17]#bash build-command.sh

# 测试镜像
[root@worker-01 jdk-17]#nerdctl run -it --rm --name jdk17 harbor.mysticalrecluse.com/pub-images/jdk-base:v17.0.15 /bin/bash
[root@af6cab8c3b75 /]# 
[root@af6cab8c3b75 /]# 
[root@af6cab8c3b75 /]# java -version 
java version "17.0.15" 2025-04-15 LTS
Java(TM) SE Runtime Environment (build 17.0.15+9-LTS-241)
Java HotSpot(TM) 64-Bit Server VM (build 17.0.15+9-LTS-241, mixed mode, sharing)
[root@af6cab8c3b75 /]# exit
exit
```



#### 构建业务镜像

```bash
# 使用版本为java17 + jenkins2.492
[root@worker-01 jenkins]#ls
build-command.sh  Dockerfile  jenkins.war  run_jenkins.sh

#查看Dockerfile
[root@worker-01 jenkins]#cat Dockerfile 
#Jenkins Version 2.492
FROM harbor.mysticalrecluse.com/pub-images/jdk-base:v17.0.15

MAINTAINER mystical mysticalrecluse@gmail.com

RUN yum install -y \
    freetype \
    freetype-devel \
    fontconfig \
    fontconfig-devel && \
    yum clean all

ADD jenkins.war /apps/jenkins/
ADD run_jenkins.sh /usr/bin/
RUN chmod +x /usr/bin/run_jenkins.sh


EXPOSE 8080 

CMD ["/usr/bin/run_jenkins.sh"]

# 查看run_jenkins.sh
[root@worker-01 jenkins]#cat run_jenkins.sh 
#!/bin/bash
# 注意： --webroot=/apps/jenkins/jenkins-data，这个目录不能作为挂载卷，比如pv/pvc，因为jenkins在初始化的时候，会清空该目录，而且里面通常保持的都是jenkins的缓存临时文件，没有持久化的必要
cd /apps/jenkins && java -server -Xms1024m -Xmx1024m -Xss512k -jar jenkins.war --webroot=/apps/jenkins/jenkins-data --httpPort=8080

# 查看build-command.sh
[root@worker-01 jenkins]#cat build-command.sh 
#!/bin/bash
nerdctl build -t  harbor.mysticalrecluse.com/myserver/jenkins:v2.492 .
echo "镜像制作完成，即将上传至Harbor服务器"
sleep 1
nerdctl push harbor.mysticalrecluse.com/myserver/jenkins:v2.492
echo "镜像上传完成"
```



#### 创建yaml清单文件

```yaml
[root@master-01 ~]#cat jenkins.yaml 
kind: Deployment
#apiVersion: extensions/v1beta1
apiVersion: apps/v1
metadata:
  labels:
    app: magedu-jenkins
  name: magedu-jenkins-deployment
  namespace: proc-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: magedu-jenkins
  template:
    metadata:
      labels:
        app: magedu-jenkins
    spec:
      containers:
      - name: magedu-jenkins-container
        image: harbor.mysticalrecluse.com/myserver/jenkins:v2.492
        #imagePullPolicy: IfNotPresent
        imagePullPolicy: Always
        ports:
        - containerPort: 8080
          protocol: TCP
          name: http
        volumeMounts:
        - mountPath: "/root/.jenkins"
          name: jenkins-root-datadir
      securityContext:                          # 这里要授权，否则jenkins没有权限会403
        runAsUser: 0
      volumes:
        - name: jenkins-root-datadir
          persistentVolumeClaim:
            claimName: jenkins-root-data-pvc

---
kind: Service
apiVersion: v1
metadata:
  labels:
    app: magedu-jenkins
  name: magedu-jenkins-service
  namespace: proc-test
spec:
  type: NodePort
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 8080
    nodePort: 30880
  selector:
    app: magedu-jenkins

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: jenkins-root-data-pvc
  namespace: proc-test
spec:
  storageClassName: sc-nfs
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```



#### 在Kubernetes起jenmins服务

```bash
[root@master-01 ~]#kubectl apply -f jenkins.yaml

# 查看
[root@master-01 ~]#kubectl get pod -n proc-test magedu-jenkins-deployment-666d865657-f5ctn 
NAME                                         READY   STATUS    RESTARTS   AGE
magedu-jenkins-deployment-666d865657-f5ctn   1/1     Running   0          14m
```



### 业务容器化案例之七dubbo微服务

![image-20250422103507993](../markdown_img/image-20250422103507993.png)



#### 微服务目录结构

```bash
[root@worker-01 dubbo]#ls
consumer  dubboadmin  provider
```



#### 构建生产者Provider镜像

```bash
# provider镜像目录
[root@worker-01 provider]#ls
build-command.sh  dubbo-demo-provider-2.1.5                  run_java.sh
Dockerfile        dubbo-demo-provider-2.1.5-assembly.tar.gz

# 修改provider的配置，配制注册中心的地址
[root@worker-01 conf]#pwd
/opt/k8s-data/dockerfile/web/magedu/dubbo/provider/dubbo-demo-provider-2.1.5/conf

[root@worker-01 conf]#cat dubbo.properties 
##
# Copyright 1999-2011 Alibaba Group.
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##
dubbo.container=log4j,spring
dubbo.application.name=demo-provider
dubbo.application.owner=
#dubbo.registry.address=multicast://224.5.6.7:1234
# 这里的地址写的是zookeeper的service
dubbo.registry.address=zookeeper://zookeeper1.proc-test.svc.cluster.local:2181 | zookeeper://zookeeper2.proc-test.svc.cluster.local:2181 | zookeeper://zookeeper3.proc-test.svc.cluster.local:2181
#dubbo.registry.address="zookeeper://zookeeper1.linux36.svc.linux36.local:2181,"
#dubbo.registry.address=zookeeper://zookeeper1.linux36.svc.linux36.local:2181 | zookeeper2.linux36.svc.linux36.local:2181 | zookeeper3.linux36.svc.linux36.local:2181
#dubbo.registry.address=redis://127.0.0.1:6379
#dubbo.registry.address=dubbo://127.0.0.1:9090
dubbo.monitor.protocol=registry
dubbo.protocol.name=dubbo
dubbo.protocol.port=20880
dubbo.log4j.file=logs/dubbo-demo-provider.log
dubbo.log4j.level=WARN

# 查看Dockerfile
[root@worker-01 provider]#cat Dockerfile 
#Dubbo provider
FROM harbor.mysticalrecluse.com/pub-images/jdk-base:v8.212 

MAINTAINER mystical "mysticalrecluse@gmail.com"

RUN yum install file nc -y
RUN mkdir -p /apps/dubbo/provider
ADD dubbo-demo-provider-2.1.5/  /apps/dubbo/provider
ADD run_java.sh /apps/dubbo/provider/bin 
RUN chown nginx.nginx /apps -R
RUN chmod a+x /apps/dubbo/provider/bin/*.sh

CMD ["/apps/dubbo/provider/bin/run_java.sh"]


# 查看
[root@worker-01 provider]#cat run_java.sh 
#!/bin/bash
#echo "nameserver 223.6.6.6" > /etc/resolv.conf
#/usr/share/filebeat/bin/filebeat -c /etc/filebeat/filebeat.yml -path.home /usr/share/filebeat -path.config /etc/filebeat -path.data /var/lib/filebeat -path.logs /var/log/filebeat  &
su - nginx -c "/apps/dubbo/provider/bin/start.sh"
tail -f /etc/hosts

# 查看build-command.sh
[root@worker-01 provider]#cat build-command.sh 
#!/bin/bash
nerdctl build -t harbor.mysticalrecluse.com/myserver/dubbo-demo-provider:v1  .
sleep 3
nerdctl push harbor.mysticalrecluse.com/myserver/dubbo-demo-provider:v1

# 构建镜像
[root@worker-01 provider]#bash build-command.sh
```



#### 使用yaml清单文件启用Provider

```bash
[root@worker-01 provider]#cat provider.yaml 
kind: Deployment
#apiVersion: extensions/v1beta1
apiVersion: apps/v1
metadata:
  labels:
    app: magedu-provider
  name: magedu-provider-deployment
  namespace: proc-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: magedu-provider
  template:
    metadata:
      labels:
        app: magedu-provider
    spec:
      containers:
      - name: magedu-provider-container
        image: harbor.mysticalrecluse.com/myserver/dubbo-demo-provider:v1 
        #command: ["/apps/tomcat/bin/run_tomcat.sh"]
        #imagePullPolicy: IfNotPresent
        imagePullPolicy: Always
        ports:
        - containerPort: 20880
          protocol: TCP
          name: http

---
kind: Service
apiVersion: v1
metadata:
  labels:
    app: magedu-provider
  name: magedu-provider-spec
  namespace: proc-test
spec:
  type: NodePort
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 20880
    #nodePort: 30001
  selector:
    app: magedu-provider
    
# 启用
[root@master-01 ~]#kubectl apply -f provider.yaml
```



#### 构建消费者consumer镜像

```bash
# 查看目录结构
[root@worker-01 consumer]#ls
build-command.sh  dubbo-demo-consumer-2.1.5                  run_java.sh
Dockerfile        dubbo-demo-consumer-2.1.5-assembly.tar.gz

# 查看Dockerfile
[root@worker-01 consumer]#cat Dockerfile 
#Dubbo consumer
FROM harbor.mysticalrecluse.com/pub-images/jdk-base:v8.212 

MAINTAINER mystical "mysticalrecluse@gmail.com"

RUN yum install file -y
RUN mkdir -p /apps/dubbo/consumer 
ADD dubbo-demo-consumer-2.1.5  /apps/dubbo/consumer
ADD run_java.sh /apps/dubbo/consumer/bin 
RUN chown nginx.nginx /apps -R
RUN chmod a+x /apps/dubbo/consumer/bin/*.sh

CMD ["/apps/dubbo/consumer/bin/run_java.sh"]

# 更改consumer配置集中的注册中心地址
[root@worker-01 consumer]#cat dubbo-demo-consumer-2.1.5/conf/dubbo.properties 
##
# Copyright 1999-2011 Alibaba Group.
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##
dubbo.container=log4j,spring
dubbo.application.name=demo-consumer
dubbo.application.owner=
#dubbo.registry.address=multicast://224.5.6.7:1234
# 这里更改为zookeeper的service地址
dubbo.registry.address=zookeeper://zookeeper1.proc-test.svc.cluster.local:2181 | zookeeper://zookeeper2.proc-test.svc.cluster.local:2181 | zookeeper://zookeeper3.proc-test.svc.cluster.local:2181
#dubbo.registry.address=redis://127.0.0.1:6379
#dubbo.registry.address=dubbo://127.0.0.1:9090
dubbo.monitor.protocol=registry
dubbo.log4j.file=logs/dubbo-demo-consumer.log
dubbo.log4j.level=WARN

# 查看启动脚本run_java.sh 
[root@worker-01 consumer]#cat run_java.sh 
#!/bin/bash
#echo "nameserver 223.6.6.6" > /etc/resolv.conf
#/usr/share/filebeat/bin/filebeat -c /etc/filebeat/filebeat.yml -path.home /usr/share/filebeat -path.config /etc/filebeat -path.data /var/lib/filebeat -path.logs /var/log/filebeat  &
su - nginx -c "/apps/dubbo/consumer/bin/start.sh"
tail -f /etc/hosts

# 查看代码构建脚本
[root@worker-01 consumer]#cat build-command.sh 
#!/bin/bash
nerdctl build -t harbor.mysticalrecluse.com/myserver/dubbo-demo-consumer:v1  .
sleep 3
nerdctl push harbor.mysticalrecluse.com/myserver/dubbo-demo-consumer:v1

# 构建镜像
[root@worker-01 consumer]#bash build-command.sh
```



#### 使用清单文件启用consumer

```yaml
[root@worker-01 consumer]#cat consumer.yaml 
kind: Deployment
#apiVersion: extensions/v1beta1
apiVersion: apps/v1
metadata:
  labels:
    app: magedu-consumer
  name: magedu-consumer-deployment
  namespace: proc-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: magedu-consumer
  template:
    metadata:
      labels:
        app: magedu-consumer
    spec:
      containers:
      - name: magedu-consumer-container
        image: harbor.mysticalrecluse.com/myserver/dubbo-demo-consumer:v1 
        #command: ["/apps/tomcat/bin/run_tomcat.sh"]
        #imagePullPolicy: IfNotPresent
        imagePullPolicy: Always
        ports:
        - containerPort: 80
          protocol: TCP
          name: http

---
kind: Service
apiVersion: v1
metadata:
  labels:
    app: magedu-consumer
  name: magedu-consumer-server
  namespace: proc-test
spec:
  type: NodePort
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
    #nodePort: 30001
  selector:
    app: magedu-consumer
```

```bash
# 启用consumer，并测试
[root@master-01 ~]#kubectl apply -f consumer.yaml
[root@master-01 ~]#kubectl exec -it -n proc-test magedu-consumer-deployment-c98b7cb48-5bkc7 -- bash
[root@magedu-consumer-deployment-c98b7cb48-5bkc7 /]# cd /apps/dubbo/consumer/
[root@magedu-consumer-deployment-c98b7cb48-5bkc7 consumer]# ls
bin  conf  lib  logs
[root@magedu-consumer-deployment-c98b7cb48-5bkc7 consumer]# cd logs
[root@magedu-consumer-deployment-c98b7cb48-5bkc7 logs]# ls
dubbo-demo-consumer.log  stdout.log
[root@magedu-consumer-deployment-c98b7cb48-5bkc7 logs]# tail -f stdout.log 
[11:37:17] Hello world71, response form provider: 10.200.171.42:20880
[11:37:19] Hello world72, response form provider: 10.200.171.42:20880
[11:37:21] Hello world73, response form provider: 10.200.171.42:20880
[11:37:23] Hello world74, response form provider: 10.200.171.42:20880

# 增加生产者provider的副本数
[root@master-01 ~]#kubectl scale deployment -n proc-test magedu-provider-deployment --replicas 3
deployment.apps/magedu-provider-deployment scaled

# 查看消费者，消费者会自动从配置中心找到生产者的地址，并进行消费
[root@master-01 ~]#kubectl exec -it -n proc-test magedu-consumer-deployment-c98b7cb48-5bkc7 -- bash
[root@magedu-consumer-deployment-c98b7cb48-5bkc7 /]# tail -f /apps/dubbo/consumer/logs/stdout.log 
[11:40:26] Hello world165, response form provider: 10.200.171.42:20880
[11:40:28] Hello world166, response form provider: 10.200.129.3:20880
[11:40:30] Hello world167, response form provider: 10.200.171.42:20880
[11:40:32] Hello world168, response form provider: 10.200.37.210:20880
[11:40:34] Hello world169, response form provider: 10.200.129.3:20880
[11:40:36] Hello world170, response form provider: 10.200.171.42:20880
[11:40:38] Hello world171, response form provider: 10.200.37.210:20880
[11:40:40] Hello world172, response form provider: 10.200.129.3:20880
[11:40:42] Hello world173, response form provider: 10.200.171.42:20880
[11:40:44] Hello world174, response form provider: 10.200.37.210:20880
[11:40:46] Hello world175, response form provider: 10.200.129.3:20880
[11:40:48] Hello world176, response form provider: 10.200.171.42:20880
[11:40:50] Hello world177, response form provider: 10.200.37.210:20880

```



#### 构建生产者/消费者的管理端镜像

```bash
# 查看目录
[root@worker-01 dubboadmin]#ls
build-command.sh  Dockerfile  dubboadmin.war      logging.properties  server.xml
catalina.sh       dubboadmin  dubboadmin.war.bak  run_tomcat.sh

# 查看Dockerfile
[root@worker-01 dubboadmin]#cat Dockerfile 
#Dubbo dubboadmin
#FROM harbor.magedu.local/pub-images/tomcat-base:v8.5.43 
FROM harbor.mysticalrecluse.com/pub-images/tomcat-base:v8.5.43 

MAINTAINER mystical "mysticalrecluse@gmail.com"

RUN yum install unzip -y  
ADD server.xml /apps/tomcat/conf/server.xml
ADD logging.properties /apps/tomcat/conf/logging.properties
ADD catalina.sh /apps/tomcat/bin/catalina.sh
ADD run_tomcat.sh /apps/tomcat/bin/run_tomcat.sh
RUN chmod +x /apps/tomcat/bin/run_tomcat.sh
RUN chmod +x /apps/tomcat/bin/catalina.sh
ADD dubboadmin.war  /data/tomcat/webapps/dubboadmin.war
RUN cd /data/tomcat/webapps && unzip dubboadmin.war && rm -rf dubboadmin.war && chown -R nginx.nginx /data /apps
RUN sed -ir 's@dubbo.registry.address=zookeeper://zookeeper1.magedu.svc.magedu.local:2181@dubbo.registry.address=zookeeper://zookeeper1.proc-test.svc.cluster.local:2181@' /data/tomcat/webapps/dubboadmin/WEB-INF/dubbo.properties

EXPOSE 8080 8443

CMD ["/apps/tomcat/bin/run_tomcat.sh"]


# 查看run_tomcat.sh
[root@worker-01 dubboadmin]#cat run_tomcat.sh 
#!/bin/bash

su - nginx -c "/apps/tomcat/bin/catalina.sh start"
su - nginx -c "tail -f /etc/hosts"

# 查看logging.properties 
[root@worker-01 dubboadmin]#cat logging.properties 
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

handlers = 1catalina.org.apache.juli.AsyncFileHandler, 2localhost.org.apache.juli.AsyncFileHandler, 3manager.org.apache.juli.AsyncFileHandler, 4host-manager.org.apache.juli.AsyncFileHandler, java.util.logging.ConsoleHandler

.handlers = 1catalina.org.apache.juli.AsyncFileHandler, java.util.logging.ConsoleHandler

############################################################
# Handler specific properties.
# Describes specific configuration info for Handlers.
############################################################

1catalina.org.apache.juli.AsyncFileHandler.level = FINE
1catalina.org.apache.juli.AsyncFileHandler.directory = /data/tomcat/logs
1catalina.org.apache.juli.AsyncFileHandler.prefix = catalina.

2localhost.org.apache.juli.AsyncFileHandler.level = FINE
2localhost.org.apache.juli.AsyncFileHandler.directory = /data/tomcat/logs 
2localhost.org.apache.juli.AsyncFileHandler.prefix = localhost.

3manager.org.apache.juli.AsyncFileHandler.level = FINE
3manager.org.apache.juli.AsyncFileHandler.directory = /data/tomcat/logs
3manager.org.apache.juli.AsyncFileHandler.prefix = manager.

4host-manager.org.apache.juli.AsyncFileHandler.level = FINE
4host-manager.org.apache.juli.AsyncFileHandler.directory = /data/tomcat/logs
4host-manager.org.apache.juli.AsyncFileHandler.prefix = host-manager.

java.util.logging.ConsoleHandler.level = FINE
java.util.logging.ConsoleHandler.formatter = org.apache.juli.OneLineFormatter


############################################################
# Facility specific properties.
# Provides extra control for each logger.
############################################################

org.apache.catalina.core.ContainerBase.[Catalina].[localhost].level = INFO
org.apache.catalina.core.ContainerBase.[Catalina].[localhost].handlers = 2localhost.org.apache.juli.AsyncFileHandler

org.apache.catalina.core.ContainerBase.[Catalina].[localhost].[/manager].level = INFO
org.apache.catalina.core.ContainerBase.[Catalina].[localhost].[/manager].handlers = 3manager.org.apache.juli.AsyncFileHandler

org.apache.catalina.core.ContainerBase.[Catalina].[localhost].[/host-manager].level = INFO
org.apache.catalina.core.ContainerBase.[Catalina].[localhost].[/host-manager].handlers = 4host-manager.org.apache.juli.AsyncFileHandler

# For example, set the org.apache.catalina.util.LifecycleBase logger to log
# each component that extends LifecycleBase changing state:
#org.apache.catalina.util.LifecycleBase.level = FINE

# To see debug messages in TldLocationsCache, uncomment the following line:
#org.apache.jasper.compiler.TldLocationsCache.level = FINE

# 查看server.xml
[root@worker-01 dubboadmin]#cat server.xml 
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
--><!-- Note:  A "Server" is not itself a "Container", so you may not
     define subcomponents such as "Valves" at this level.
     Documentation at /docs/config/server.html
 --><Server port="8005" shutdown="SHUTDOWN">
  <Listener className="org.apache.catalina.startup.VersionLoggerListener"/>
  <!-- Security listener. Documentation at /docs/config/listeners.html
  <Listener className="org.apache.catalina.security.SecurityListener" />
  -->
  <!--APR library loader. Documentation at /docs/apr.html -->
  <Listener SSLEngine="on" className="org.apache.catalina.core.AprLifecycleListener"/>
  <!-- Prevent memory leaks due to use of particular java/javax APIs-->
  <Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener"/>
  <Listener className="org.apache.catalina.mbeans.GlobalResourcesLifecycleListener"/>
  <Listener className="org.apache.catalina.core.ThreadLocalLeakPreventionListener"/>

  <!-- Global JNDI resources
       Documentation at /docs/jndi-resources-howto.html
  -->
  <GlobalNamingResources>
    <!-- Editable user database that can also be used by
         UserDatabaseRealm to authenticate users
    -->
    <Resource auth="Container" description="User database that can be updated and saved" factory="org.apache.catalina.users.MemoryUserDatabaseFactory" name="UserDatabase" pathname="conf/tomcat-users.xml" type="org.apache.catalina.UserDatabase"/>
  </GlobalNamingResources>

  <!-- A "Service" is a collection of one or more "Connectors" that share
       a single "Container" Note:  A "Service" is not itself a "Container",
       so you may not define subcomponents such as "Valves" at this level.
       Documentation at /docs/config/service.html
   -->
  <Service name="Catalina">

    <!--The connectors can use a shared executor, you can define one or more named thread pools-->
    <!--
    <Executor name="tomcatThreadPool" namePrefix="catalina-exec-"
        maxThreads="150" minSpareThreads="4"/>
    -->


    <!-- A "Connector" represents an endpoint by which requests are received
         and responses are returned. Documentation at :
         Java HTTP Connector: /docs/config/http.html (blocking & non-blocking)
         Java AJP  Connector: /docs/config/ajp.html
         APR (HTTP/AJP) Connector: /docs/apr.html
         Define a non-SSL/TLS HTTP/1.1 Connector on port 8080
    -->
    <Connector connectionTimeout="20000" port="8080" protocol="HTTP/1.1" redirectPort="8443"/>
    <!-- A "Connector" using the shared thread pool-->
    <!--
    <Connector executor="tomcatThreadPool"
               port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
    -->
    <!-- Define a SSL/TLS HTTP/1.1 Connector on port 8443
         This connector uses the NIO implementation that requires the JSSE
         style configuration. When using the APR/native implementation, the
         OpenSSL style configuration is required as described in the APR/native
         documentation -->
    <!--
    <Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"
               maxThreads="150" SSLEnabled="true" scheme="https" secure="true"
               clientAuth="false" sslProtocol="TLS" />
    -->

    <!-- Define an AJP 1.3 Connector on port 8009 -->
    <Connector port="8009" protocol="AJP/1.3" redirectPort="8443"/>


    <!-- An Engine represents the entry point (within Catalina) that processes
         every request.  The Engine implementation for Tomcat stand alone
         analyzes the HTTP headers included with the request, and passes them
         on to the appropriate Host (virtual host).
         Documentation at /docs/config/engine.html -->

    <!-- You should set jvmRoute to support load-balancing via AJP ie :
    <Engine name="Catalina" defaultHost="localhost" jvmRoute="jvm1">
    -->
    <Engine defaultHost="localhost" name="Catalina">

      <!--For clustering, please take a look at documentation at:
          /docs/cluster-howto.html  (simple how to)
          /docs/config/cluster.html (reference documentation) -->
      <!--
      <Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"/>
      -->

      <!-- Use the LockOutRealm to prevent attempts to guess user passwords
           via a brute-force attack -->
      <Realm className="org.apache.catalina.realm.LockOutRealm">
        <!-- This Realm uses the UserDatabase configured in the global JNDI
             resources under the key "UserDatabase".  Any edits
             that are performed against this UserDatabase are immediately
             available for use by the Realm.  -->
        <Realm className="org.apache.catalina.realm.UserDatabaseRealm" resourceName="UserDatabase"/>
      </Realm>

      <Host appBase="/data/tomcat/webapps" autoDeploy="true" name="localhost" unpackWARs="true">

        <!-- SingleSignOn valve, share authentication between web applications
             Documentation at: /docs/config/valve.html -->
        <!--
        <Valve className="org.apache.catalina.authenticator.SingleSignOn" />
        -->

        <!-- Access log processes all example.
             Documentation at: /docs/config/valve.html
             Note: The pattern used is equivalent to using pattern="common" -->
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" pattern="%h %l %u %t &quot;%r&quot; %s %b" prefix="localhost_access_log" suffix=".txt"/>

        <Context docBase="dubboadmin" path="/" reloadable="true" source="org.eclipse.jst.jee.server:dubboadmin"/>

	</Host>
    </Engine>
  </Service>
</Server>

# 查看catalina.sh
[root@worker-01 dubboadmin]#cat catalina.sh 
#!/bin/sh

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -----------------------------------------------------------------------------
# Control Script for the CATALINA Server
#
# Environment Variable Prerequisites
#
#   Do not set the variables in this script. Instead put them into a script
#   setenv.sh in CATALINA_BASE/bin to keep your customizations separate.
#
#   CATALINA_HOME   May point at your Catalina "build" directory.
#
#   CATALINA_BASE   (Optional) Base directory for resolving dynamic portions
#                   of a Catalina installation.  If not present, resolves to
#                   the same directory that CATALINA_HOME points to.
#
#   CATALINA_OUT    (Optional) Full path to a file where stdout and stderr
#                   will be redirected.
#                   Default is $CATALINA_BASE/logs/catalina.out
#
#   CATALINA_OPTS   (Optional) Java runtime options used when the "start",
#                   "run" or "debug" command is executed.
#                   Include here and not in JAVA_OPTS all options, that should
#                   only be used by Tomcat itself, not by the stop process,
#                   the version command etc.
#                   Examples are heap size, GC logging, JMX ports etc.
#
#   CATALINA_TMPDIR (Optional) Directory path location of temporary directory
#                   the JVM should use (java.io.tmpdir).  Defaults to
#                   $CATALINA_BASE/temp.
#
#   JAVA_HOME       Must point at your Java Development Kit installation.
#                   Required to run the with the "debug" argument.
#
#   JRE_HOME        Must point at your Java Runtime installation.
#                   Defaults to JAVA_HOME if empty. If JRE_HOME and JAVA_HOME
#                   are both set, JRE_HOME is used.
#
#   JAVA_OPTS       (Optional) Java runtime options used when any command
#                   is executed.
#                   Include here and not in CATALINA_OPTS all options, that
#                   should be used by Tomcat and also by the stop process,
#                   the version command etc.
#                   Most options should go into CATALINA_OPTS.
#
#   JAVA_ENDORSED_DIRS (Optional) Lists of of colon separated directories
#                   containing some jars in order to allow replacement of APIs
#                   created outside of the JCP (i.e. DOM and SAX from W3C).
#                   It can also be used to update the XML parser implementation.
#                   Defaults to $CATALINA_HOME/endorsed.
#
#   JPDA_TRANSPORT  (Optional) JPDA transport used when the "jpda start"
#                   command is executed. The default is "dt_socket".
#
#   JPDA_ADDRESS    (Optional) Java runtime options used when the "jpda start"
#                   command is executed. The default is localhost:8000.
#
#   JPDA_SUSPEND    (Optional) Java runtime options used when the "jpda start"
#                   command is executed. Specifies whether JVM should suspend
#                   execution immediately after startup. Default is "n".
#
#   JPDA_OPTS       (Optional) Java runtime options used when the "jpda start"
#                   command is executed. If used, JPDA_TRANSPORT, JPDA_ADDRESS,
#                   and JPDA_SUSPEND are ignored. Thus, all required jpda
#                   options MUST be specified. The default is:
#
#                   -agentlib:jdwp=transport=$JPDA_TRANSPORT,
#                       address=$JPDA_ADDRESS,server=y,suspend=$JPDA_SUSPEND
#
#   CATALINA_PID    (Optional) Path of the file which should contains the pid
#                   of the catalina startup java process, when start (fork) is
#                   used
#
#   LOGGING_CONFIG  (Optional) Override Tomcat's logging config file
#                   Example (all one line)
#                   LOGGING_CONFIG="-Djava.util.logging.config.file=$CATALINA_BASE/conf/logging.properties"
#
#   LOGGING_MANAGER (Optional) Override Tomcat's logging manager
#                   Example (all one line)
#                   LOGGING_MANAGER="-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager"
# -----------------------------------------------------------------------------
# 优化jvm
JAVA_OPTS="-server -Xms512m -Xmx512m -Xss512k -Xmn1g -XX:CMSInitiatingOccupancyFraction=65  -XX:+UseFastAccessorMethods -XX:+AggressiveOpts -XX:+UseBiasedLocking -XX:+DisableExplicitGC -XX:MaxTenuringThreshold=10 -XX:NewSize=2048M -XX:MaxNewSize=2048M -XX:NewRatio=2 -XX:PermSize=128m -XX:MaxPermSize=512m -XX:CMSFullGCsBeforeCompaction=5 -XX:+ExplicitGCInvokesConcurrent -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+CMSParallelRemarkEnabled -XX:+UseCMSCompactAtFullCollection -XX:LargePageSizeInBytes=128m -XX:+UseFastAccessorMethods"

# OS specific support.  $var _must_ be set to either true or false.
cygwin=false
darwin=false
os400=false
case "`uname`" in
CYGWIN*) cygwin=true;;
Darwin*) darwin=true;;
OS400*) os400=true;;
esac

# resolve links - $0 may be a softlink
PRG="$0"

while [ -h "$PRG" ]; do
  ls=`ls -ld "$PRG"`
  link=`expr "$ls" : '.*-> \(.*\)$'`
  if expr "$link" : '/.*' > /dev/null; then
    PRG="$link"
  else
    PRG=`dirname "$PRG"`/"$link"
  fi
done

# Get standard environment variables
PRGDIR=`dirname "$PRG"`

# Only set CATALINA_HOME if not already set
[ -z "$CATALINA_HOME" ] && CATALINA_HOME=`cd "$PRGDIR/.." >/dev/null; pwd`

# Copy CATALINA_BASE from CATALINA_HOME if not already set
[ -z "$CATALINA_BASE" ] && CATALINA_BASE="$CATALINA_HOME"

# Ensure that neither CATALINA_HOME nor CATALINA_BASE contains a colon
# as this is used as the separator in the classpath and Java provides no
# mechanism for escaping if the same character appears in the path.
case $CATALINA_HOME in
  *:*) echo "Using CATALINA_HOME:   $CATALINA_HOME";
       echo "Unable to start as CATALINA_HOME contains a colon (:) character";
       exit 1;
esac
case $CATALINA_BASE in
  *:*) echo "Using CATALINA_BASE:   $CATALINA_BASE";
       echo "Unable to start as CATALINA_BASE contains a colon (:) character";
       exit 1;
esac

# Ensure that any user defined CLASSPATH variables are not used on startup,
# but allow them to be specified in setenv.sh, in rare case when it is needed.
CLASSPATH=

if [ -r "$CATALINA_BASE/bin/setenv.sh" ]; then
  . "$CATALINA_BASE/bin/setenv.sh"
elif [ -r "$CATALINA_HOME/bin/setenv.sh" ]; then
  . "$CATALINA_HOME/bin/setenv.sh"
fi

# For Cygwin, ensure paths are in UNIX format before anything is touched
if $cygwin; then
  [ -n "$JAVA_HOME" ] && JAVA_HOME=`cygpath --unix "$JAVA_HOME"`
  [ -n "$JRE_HOME" ] && JRE_HOME=`cygpath --unix "$JRE_HOME"`
  [ -n "$CATALINA_HOME" ] && CATALINA_HOME=`cygpath --unix "$CATALINA_HOME"`
  [ -n "$CATALINA_BASE" ] && CATALINA_BASE=`cygpath --unix "$CATALINA_BASE"`
  [ -n "$CLASSPATH" ] && CLASSPATH=`cygpath --path --unix "$CLASSPATH"`
fi

# For OS400
if $os400; then
  # Set job priority to standard for interactive (interactive - 6) by using
  # the interactive priority - 6, the helper threads that respond to requests
  # will be running at the same priority as interactive jobs.
  COMMAND='chgjob job('$JOBNAME') runpty(6)'
  system $COMMAND

  # Enable multi threading
  export QIBM_MULTI_THREADED=Y
fi

# Get standard Java environment variables
if $os400; then
  # -r will Only work on the os400 if the files are:
  # 1. owned by the user
  # 2. owned by the PRIMARY group of the user
  # this will not work if the user belongs in secondary groups
  . "$CATALINA_HOME"/bin/setclasspath.sh
else
  if [ -r "$CATALINA_HOME"/bin/setclasspath.sh ]; then
    . "$CATALINA_HOME"/bin/setclasspath.sh
  else
    echo "Cannot find $CATALINA_HOME/bin/setclasspath.sh"
    echo "This file is needed to run this program"
    exit 1
  fi
fi

# Add on extra jar files to CLASSPATH
if [ ! -z "$CLASSPATH" ] ; then
  CLASSPATH="$CLASSPATH":
fi
CLASSPATH="$CLASSPATH""$CATALINA_HOME"/bin/bootstrap.jar

if [ -z "$CATALINA_OUT" ] ; then
  CATALINA_OUT="$CATALINA_BASE"/logs/catalina.out
fi

if [ -z "$CATALINA_TMPDIR" ] ; then
  # Define the java.io.tmpdir to use for Catalina
  CATALINA_TMPDIR="$CATALINA_BASE"/temp
fi

# Add tomcat-juli.jar to classpath
# tomcat-juli.jar can be over-ridden per instance
if [ -r "$CATALINA_BASE/bin/tomcat-juli.jar" ] ; then
  CLASSPATH=$CLASSPATH:$CATALINA_BASE/bin/tomcat-juli.jar
else
  CLASSPATH=$CLASSPATH:$CATALINA_HOME/bin/tomcat-juli.jar
fi

# Bugzilla 37848: When no TTY is available, don't output to console
have_tty=0
if [ "`tty`" != "not a tty" ]; then
    have_tty=1
fi

# For Cygwin, switch paths to Windows format before running java
if $cygwin; then
  JAVA_HOME=`cygpath --absolute --windows "$JAVA_HOME"`
  JRE_HOME=`cygpath --absolute --windows "$JRE_HOME"`
  CATALINA_HOME=`cygpath --absolute --windows "$CATALINA_HOME"`
  CATALINA_BASE=`cygpath --absolute --windows "$CATALINA_BASE"`
  CATALINA_TMPDIR=`cygpath --absolute --windows "$CATALINA_TMPDIR"`
  CLASSPATH=`cygpath --path --windows "$CLASSPATH"`
  JAVA_ENDORSED_DIRS=`cygpath --path --windows "$JAVA_ENDORSED_DIRS"`
fi

# Set juli LogManager config file if it is present and an override has not been issued
if [ -z "$LOGGING_CONFIG" ]; then
  if [ -r "$CATALINA_BASE"/conf/logging.properties ]; then
    LOGGING_CONFIG="-Djava.util.logging.config.file=$CATALINA_BASE/conf/logging.properties"
  else
    # Bugzilla 45585
    LOGGING_CONFIG="-Dnop"
  fi
fi

if [ -z "$LOGGING_MANAGER" ]; then
  LOGGING_MANAGER="-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager"
fi

# Uncomment the following line to make the umask available when using the
# org.apache.catalina.security.SecurityListener
#JAVA_OPTS="$JAVA_OPTS -Dorg.apache.catalina.security.SecurityListener.UMASK=`umask`"

# ----- Execute The Requested Command -----------------------------------------

# Bugzilla 37848: only output this if we have a TTY
if [ $have_tty -eq 1 ]; then
  echo "Using CATALINA_BASE:   $CATALINA_BASE"
  echo "Using CATALINA_HOME:   $CATALINA_HOME"
  echo "Using CATALINA_TMPDIR: $CATALINA_TMPDIR"
  if [ "$1" = "debug" ] ; then
    echo "Using JAVA_HOME:       $JAVA_HOME"
  else
    echo "Using JRE_HOME:        $JRE_HOME"
  fi
  echo "Using CLASSPATH:       $CLASSPATH"
  if [ ! -z "$CATALINA_PID" ]; then
    echo "Using CATALINA_PID:    $CATALINA_PID"
  fi
fi

if [ "$1" = "jpda" ] ; then
  if [ -z "$JPDA_TRANSPORT" ]; then
    JPDA_TRANSPORT="dt_socket"
  fi
  if [ -z "$JPDA_ADDRESS" ]; then
    JPDA_ADDRESS="localhost:8000"
  fi
  if [ -z "$JPDA_SUSPEND" ]; then
    JPDA_SUSPEND="n"
  fi
  if [ -z "$JPDA_OPTS" ]; then
    JPDA_OPTS="-agentlib:jdwp=transport=$JPDA_TRANSPORT,address=$JPDA_ADDRESS,server=y,suspend=$JPDA_SUSPEND"
  fi
  CATALINA_OPTS="$JPDA_OPTS $CATALINA_OPTS"
  shift
fi

if [ "$1" = "debug" ] ; then
  if $os400; then
    echo "Debug command not available on OS400"
    exit 1
  else
    shift
    if [ "$1" = "-security" ] ; then
      if [ $have_tty -eq 1 ]; then
        echo "Using Security Manager"
      fi
      shift
      exec "$_RUNJDB" "$LOGGING_CONFIG" $LOGGING_MANAGER $JAVA_OPTS $CATALINA_OPTS \
        -Djava.endorsed.dirs="$JAVA_ENDORSED_DIRS" -classpath "$CLASSPATH" \
        -sourcepath "$CATALINA_HOME"/../../java \
        -Djava.security.manager \
        -Djava.security.policy=="$CATALINA_BASE"/conf/catalina.policy \
        -Dcatalina.base="$CATALINA_BASE" \
        -Dcatalina.home="$CATALINA_HOME" \
        -Djava.io.tmpdir="$CATALINA_TMPDIR" \
         -Djava.awt.headless=true \
        org.apache.catalina.startup.Bootstrap "$@" start
    else
      exec "$_RUNJDB" "$LOGGING_CONFIG" $LOGGING_MANAGER $JAVA_OPTS $CATALINA_OPTS \
        -Djava.endorsed.dirs="$JAVA_ENDORSED_DIRS" -classpath "$CLASSPATH" \
        -sourcepath "$CATALINA_HOME"/../../java \
        -Dcatalina.base="$CATALINA_BASE" \
        -Dcatalina.home="$CATALINA_HOME" \
        -Djava.io.tmpdir="$CATALINA_TMPDIR" \
         -Djava.awt.headless=true \
        org.apache.catalina.startup.Bootstrap "$@" start
    fi
  fi

elif [ "$1" = "run" ]; then

  shift
  if [ "$1" = "-security" ] ; then
    if [ $have_tty -eq 1 ]; then
      echo "Using Security Manager"
    fi
    shift
    eval exec "\"$_RUNJAVA\"" "\"$LOGGING_CONFIG\"" $LOGGING_MANAGER $JAVA_OPTS $CATALINA_OPTS \
      -Djava.endorsed.dirs="\"$JAVA_ENDORSED_DIRS\"" -classpath "\"$CLASSPATH\"" \
      -Djava.security.manager \
      -Djava.security.policy=="\"$CATALINA_BASE/conf/catalina.policy\"" \
      -Dcatalina.base="\"$CATALINA_BASE\"" \
      -Dcatalina.home="\"$CATALINA_HOME\"" \
      -Djava.io.tmpdir="\"$CATALINA_TMPDIR\"" \
       -Djava.awt.headless=true \
      org.apache.catalina.startup.Bootstrap "$@" start
  else
    eval exec "\"$_RUNJAVA\"" "\"$LOGGING_CONFIG\"" $LOGGING_MANAGER $JAVA_OPTS $CATALINA_OPTS \
      -Djava.endorsed.dirs="\"$JAVA_ENDORSED_DIRS\"" -classpath "\"$CLASSPATH\"" \
      -Dcatalina.base="\"$CATALINA_BASE\"" \
      -Dcatalina.home="\"$CATALINA_HOME\"" \
      -Djava.io.tmpdir="\"$CATALINA_TMPDIR\"" \
       -Djava.awt.headless=true \
      org.apache.catalina.startup.Bootstrap "$@" start
  fi

elif [ "$1" = "start" ] ; then

  if [ ! -z "$CATALINA_PID" ]; then
    if [ -f "$CATALINA_PID" ]; then
      if [ -s "$CATALINA_PID" ]; then
        echo "Existing PID file found during start."
        if [ -r "$CATALINA_PID" ]; then
          PID=`cat "$CATALINA_PID"`
          ps -p $PID >/dev/null 2>&1
          if [ $? -eq 0 ] ; then
            echo "Tomcat appears to still be running with PID $PID. Start aborted."
            echo "If the following process is not a Tomcat process, remove the PID file and try again:"
            ps -f -p $PID
            exit 1
          else
            echo "Removing/clearing stale PID file."
            rm -f "$CATALINA_PID" >/dev/null 2>&1
            if [ $? != 0 ]; then
              if [ -w "$CATALINA_PID" ]; then
                cat /dev/null > "$CATALINA_PID"
              else
                echo "Unable to remove or clear stale PID file. Start aborted."
                exit 1
              fi
            fi
          fi
        else
          echo "Unable to read PID file. Start aborted."
          exit 1
        fi
      else
        rm -f "$CATALINA_PID" >/dev/null 2>&1
        if [ $? != 0 ]; then
          if [ ! -w "$CATALINA_PID" ]; then
            echo "Unable to remove or write to empty PID file. Start aborted."
            exit 1
          fi
        fi
      fi
    fi
  fi

  shift
  touch "$CATALINA_OUT"
  if [ "$1" = "-security" ] ; then
    if [ $have_tty -eq 1 ]; then
      echo "Using Security Manager"
    fi
    shift
    eval "\"$_RUNJAVA\"" "\"$LOGGING_CONFIG\"" $LOGGING_MANAGER $JAVA_OPTS $CATALINA_OPTS \
      -Djava.endorsed.dirs="\"$JAVA_ENDORSED_DIRS\"" -classpath "\"$CLASSPATH\"" \
      -Djava.security.manager \
      -Djava.security.policy=="\"$CATALINA_BASE/conf/catalina.policy\"" \
      -Dcatalina.base="\"$CATALINA_BASE\"" \
      -Dcatalina.home="\"$CATALINA_HOME\"" \
      -Djava.io.tmpdir="\"$CATALINA_TMPDIR\"" \
       -Djava.awt.headless=true \
      org.apache.catalina.startup.Bootstrap "$@" start \
      >> "$CATALINA_OUT" 2>&1 "&"

  else
    eval "\"$_RUNJAVA\"" "\"$LOGGING_CONFIG\"" $LOGGING_MANAGER $JAVA_OPTS $CATALINA_OPTS \
      -Djava.endorsed.dirs="\"$JAVA_ENDORSED_DIRS\"" -classpath "\"$CLASSPATH\"" \
      -Dcatalina.base="\"$CATALINA_BASE\"" \
      -Dcatalina.home="\"$CATALINA_HOME\"" \
      -Djava.io.tmpdir="\"$CATALINA_TMPDIR\"" \
       -Djava.awt.headless=true \
      org.apache.catalina.startup.Bootstrap "$@" start \
      >> "$CATALINA_OUT" 2>&1 "&"

  fi

  if [ ! -z "$CATALINA_PID" ]; then
    echo $! > "$CATALINA_PID"
  fi

  echo "Tomcat started."

elif [ "$1" = "stop" ] ; then

  shift

  SLEEP=5
  if [ ! -z "$1" ]; then
    echo $1 | grep "[^0-9]" >/dev/null 2>&1
    if [ $? -gt 0 ]; then
      SLEEP=$1
      shift
    fi
  fi

  FORCE=0
  if [ "$1" = "-force" ]; then
    shift
    FORCE=1
  fi

  if [ ! -z "$CATALINA_PID" ]; then
    if [ -f "$CATALINA_PID" ]; then
      if [ -s "$CATALINA_PID" ]; then
        kill -0 `cat "$CATALINA_PID"` >/dev/null 2>&1
        if [ $? -gt 0 ]; then
          echo "PID file found but no matching process was found. Stop aborted."
          exit 1
        fi
      else
        echo "PID file is empty and has been ignored."
      fi
    else
      echo "\$CATALINA_PID was set but the specified file does not exist. Is Tomcat running? Stop aborted."
      exit 1
    fi
  fi

  eval "\"$_RUNJAVA\"" $LOGGING_MANAGER $JAVA_OPTS \
    -Djava.endorsed.dirs="\"$JAVA_ENDORSED_DIRS\"" -classpath "\"$CLASSPATH\"" \
    -Dcatalina.base="\"$CATALINA_BASE\"" \
    -Dcatalina.home="\"$CATALINA_HOME\"" \
    -Djava.io.tmpdir="\"$CATALINA_TMPDIR\"" \
     -Djava.awt.headless=true \
    org.apache.catalina.startup.Bootstrap "$@" stop

  # stop failed. Shutdown port disabled? Try a normal kill.
  if [ $? != 0 ]; then
    if [ ! -z "$CATALINA_PID" ]; then
      echo "The stop command failed. Attempting to signal the process to stop through OS signal."
      kill -15 `cat "$CATALINA_PID"` >/dev/null 2>&1
    fi
  fi

  if [ ! -z "$CATALINA_PID" ]; then
    if [ -f "$CATALINA_PID" ]; then
      while [ $SLEEP -ge 0 ]; do
        kill -0 `cat "$CATALINA_PID"` >/dev/null 2>&1
        if [ $? -gt 0 ]; then
          rm -f "$CATALINA_PID" >/dev/null 2>&1
          if [ $? != 0 ]; then
            if [ -w "$CATALINA_PID" ]; then
              cat /dev/null > "$CATALINA_PID"
              # If Tomcat has stopped don't try and force a stop with an empty PID file
              FORCE=0
            else
              echo "The PID file could not be removed or cleared."
            fi
          fi
          echo "Tomcat stopped."
          break
        fi
        if [ $SLEEP -gt 0 ]; then
          sleep 1
        fi
        if [ $SLEEP -eq 0 ]; then
          echo "Tomcat did not stop in time."
          if [ $FORCE -eq 0 ]; then
            echo "PID file was not removed."
          fi
          echo "To aid diagnostics a thread dump has been written to standard out."
          kill -3 `cat "$CATALINA_PID"`
        fi
        SLEEP=`expr $SLEEP - 1 `
      done
    fi
  fi

  KILL_SLEEP_INTERVAL=5
  if [ $FORCE -eq 1 ]; then
    if [ -z "$CATALINA_PID" ]; then
      echo "Kill failed: \$CATALINA_PID not set"
    else
      if [ -f "$CATALINA_PID" ]; then
        PID=`cat "$CATALINA_PID"`
        echo "Killing Tomcat with the PID: $PID"
        kill -9 $PID
        while [ $KILL_SLEEP_INTERVAL -ge 0 ]; do
            kill -0 `cat "$CATALINA_PID"` >/dev/null 2>&1
            if [ $? -gt 0 ]; then
                rm -f "$CATALINA_PID" >/dev/null 2>&1
                if [ $? != 0 ]; then
                    if [ -w "$CATALINA_PID" ]; then
                        cat /dev/null > "$CATALINA_PID"
                    else
                        echo "The PID file could not be removed."
                    fi
                fi
                echo "The Tomcat process has been killed."
                break
            fi
            if [ $KILL_SLEEP_INTERVAL -gt 0 ]; then
                sleep 1
            fi
            KILL_SLEEP_INTERVAL=`expr $KILL_SLEEP_INTERVAL - 1 `
        done
        if [ $KILL_SLEEP_INTERVAL -lt 0 ]; then
            echo "Tomcat has not been killed completely yet. The process might be waiting on some system call or might be UNINTERRUPTIBLE."
        fi
      fi
    fi
  fi

elif [ "$1" = "configtest" ] ; then

    eval "\"$_RUNJAVA\"" $LOGGING_MANAGER $JAVA_OPTS \
      -Djava.endorsed.dirs="\"$JAVA_ENDORSED_DIRS\"" -classpath "\"$CLASSPATH\"" \
      -Dcatalina.base="\"$CATALINA_BASE\"" \
      -Dcatalina.home="\"$CATALINA_HOME\"" \
      -Djava.io.tmpdir="\"$CATALINA_TMPDIR\"" \
       -Djava.awt.headless=true \
      org.apache.catalina.startup.Bootstrap configtest
    result=$?
    if [ $result -ne 0 ]; then
        echo "Configuration error detected!"
    fi
    exit $result

elif [ "$1" = "version" ] ; then

    "$_RUNJAVA"   \
      -classpath "$CATALINA_HOME/lib/catalina.jar" \
      org.apache.catalina.util.ServerInfo

else

  echo "Usage: catalina.sh ( commands ... )"
  echo "commands:"
  if $os400; then
    echo "  debug             Start Catalina in a debugger (not available on OS400)"
    echo "  debug -security   Debug Catalina with a security manager (not available on OS400)"
  else
    echo "  debug             Start Catalina in a debugger"
    echo "  debug -security   Debug Catalina with a security manager"
  fi
  echo "  jpda start        Start Catalina under JPDA debugger"
  echo "  run               Start Catalina in the current window"
  echo "  run -security     Start in the current window with security manager"
  echo "  start             Start Catalina in a separate window"
  echo "  start -security   Start in a separate window with security manager"
  echo "  stop              Stop Catalina, waiting up to 5 seconds for the process to end"
  echo "  stop n            Stop Catalina, waiting up to n seconds for the process to end"
  echo "  stop -force       Stop Catalina, wait up to 5 seconds and then use kill -KILL if still running"
  echo "  stop n -force     Stop Catalina, wait up to n seconds and then use kill -KILL if still running"
  echo "  configtest        Run a basic syntax check on server.xml - check exit code for result"
  echo "  version           What version of tomcat are you running?"
  echo "Note: Waiting for the process to end and use of the -force option require that \$CATALINA_PID is defined"
  exit 1

fi

# 查看启动脚本
[root@worker-01 dubboadmin]#cat build-command.sh 
#!/bin/bash
TAG=$1
nerdctl build -t harbor.mysticalrecluse.com/myserver/dubboadmin:${TAG}  .
sleep 3
nerdctl push  harbor.mysticalrecluse.com/myserver/dubboadmin:${TAG}

# 执行构建
[root@worker-01 dubboadmin]#bash build-command.sh v1
```



#### 使用清单文件启用管理镜像

```yaml
[root@worker-01 dubboadmin]#cat dubboadmin.yaml 
kind: Deployment
#apiVersion: extensions/v1beta1
apiVersion: apps/v1
metadata:
  labels:
    app: magedu-dubboadmin
  name: magedu-dubboadmin-deployment
  namespace: proc-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: magedu-dubboadmin
  template:
    metadata:
      labels:
        app: magedu-dubboadmin
    spec:
      containers:
      - name: magedu-dubboadmin-container
        image: harbor.mysticalrecluse.com/myserver/dubboadmin:v1 
        #command: ["/apps/tomcat/bin/run_tomcat.sh"]
        #imagePullPolicy: IfNotPresent
        imagePullPolicy: Always
        ports:
        - containerPort: 8080
          protocol: TCP
          name: http

---
kind: Service
apiVersion: v1
metadata:
  labels:
    app: magedu-dubboadmin
  name: magedu-dubboadmin-service
  namespace: proc-test
spec:
  type: NodePort
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 8080
    nodePort: 30080
  selector:
    app: magedu-dubboadmin
    
# 启用
[root@master-01 ~]#kubectl apply -f dubboadmin.yaml

# 查看服务端口是否打开
[root@master-01 ~]#kubectl exec -n proc-test magedu-dubboadmin-deployment-55859f66-nvvxw -- ss -nlt
State      Recv-Q Send-Q Local Address:Port               Peer Address:Port              
LISTEN     0      100       [::]:8009                  [::]:*                  
LISTEN     2      100       [::]:8080                  [::]:*  

# 服务启动成功，访问节点IP:30080,输入账号密码：root/root，即可登录管理页面
```