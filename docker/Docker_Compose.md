# Docker Compose简明指南
## 编排和部署
### 编排(orchestration)
编排指根据被部署的对象之间的耦合关系，以及被部署对象对环境的依赖，制定部署流程中各个动作的执行顺序，部署过程所需要的依赖文件和被部署文件的存储位置和获取方式，以及如何验证部署成功。
这些信息都会在编排工具中以指定的格式(比如配置文件或特定的代码)来要求运维人员定义并保存起来，从而保证这个流程能够随时在全新的环境中可靠有序地重现出来

### 部署(deployment)
部署是指按照编排所指定的内容和流程，在目标机器上执行环境初始化，存放特定的依赖文件，运行指定的部署动作，最终按照编排的规则来确认部署成功


## Compose文件
docker-compose命令默认于当前目录中搜索docker-compose.yaml配置文件，除了version以外，该文件主要由三个顶级参数组成：services、networks和volumes.

- Services:
  - 用于定义组成每个服务的容器的相关配置，，相关配置项类似于传递给docker container creatre命令的相关参数； 每个服务启动的容器实例可能不止一个，而每个容器依赖的镜像要么通过二级指令image指定位置直接获取，要么由二级指令build指定的Docker临时构建；另外，服务中可内嵌networks指令引用顶级指令networks中定义的网络，以及内嵌volumnes引用顶级指令volumes中定义的存储卷

  - networks：用户定义容器网络，相关配置项类似于传递给docker network create命令的相关参数
  - volumes：用于定义容器存储卷，相关配置项类似于传递给docker volume create命令的相关参数

## Services的常用命令
### build
用于定义构建镜像的相关配置，它自身可以直接以是上下文路径为参数，例如`build ./dir`即为于当前目录下的dir子目录中搜索Dockerfile配置文件。不过，也可以使用二级参数context来完成此类功能。它常用的二级参数如下：

- context: 包含Dockerfile的目录的路径，或者是git仓库的url；相对路径通常意味着以docker-composer.yaml文件所在的目录为起始目录；
- dockerfile：备用的Dockerfile文件，此指令依赖于context指令；
- args：构建参数，常用于向Dockerfile中由ARG指令定义的构建参数传值
- cache_from：解析缓存时使用的镜像列表，由3.2版本引入
- labels：向镜像添加元数据的标签
- target：基于多阶段镜像构建方式构建镜像时指定目标阶段

### command和entrypoint

基于镜像启动容器时，command指定的命令覆盖镜像上默认的由CMD定义要运⾏的命令，⽽entrypoint指定的命令则覆盖镜像上由ENTRYPOINT定义要运⾏的命令，⼆者命令格式分别同Dockerfile的CMD和ENTRYPOINT

### cap_add和cap_drop

用于调整容器操作内核的权利与能力，cap_add用于添加容器运行时可用的能力，而cap_drop则相反。集群模式(swarm)会忽略此参数
```yaml
version: '3'
services:
  phpfpm_test:
    cap_add:
      - ALL
    cap_drop: 
      - NET_ADMIN
      - SYS_ADMIN
```

### depends_on

定义该服务的依赖关系；在启动该服务时，被依赖的每个服务必须处于运行状态（已启动而非就绪）；启动和关闭时过程以对称的方式进行，即启动时先启动被依赖的服务，而关闭时要先关闭依赖方。
例如：对于下列的示例定义的服务列表，启动web时要先启动db和redis服务，而停止时需要先停止web服务

```yaml
version: "3.7"
services:
  web: 
    build: 
    depands_on: 
      - db
      - redis
  redis:
    image: redis
  db: 
    images: postgres
```

### deploy

定义服务的部署机制，不过，这仅在将服务器部署到`swarm`集群时有效。
```yaml
version: "3.7"
services:
  redis:
    image: redis:alpine
    deploy:
      replica: 6
      update_config:
        parallelism: 2
        delay: 10s
      restart_policy: 
        condition: on-failure
```

deploy支持多个二级参数，例如replicas用于定义容器实例的个数，update_config用于定义更新策略，而restart_policy则用于指定重启策略

### environment和env_file

environment用于向容器添加环境变量，支持列表和字典格式。任何布尔值，包括true,false,yes和no,都需要使用引号，以确保YAML解析器不会将它们转换为True和False。以下示例使用了列表的格式

```yaml
evnironment: 
  - RACK_ENV=development
  - SHOW=true
  - SESSION_SECRET
```

而env_file则从指定的文件导入环境变量，路径为相对路径时表示起始于`docker-compose.yaml`文件所在目录。他同样支持单值或列表格式。
```yaml
env_file: 
  - ./common.env
  - ./apps/web_env
  - /opt/secrets.env
```

需要注意的是，如果同时使用了environment和env_file，则文件中加载的同名环境变量会被environment定义的环境变量值所覆盖

### expose和ports

expose指令仅暴露容器端口，而不会将它们发布到主机，这意味着它们只能被连接的服务所访问，因此也仅能指定内部端口。下面的指令以列表格式定义了要暴露的两个端口
```yaml
expose:
  - "3000"
  - "8000"
```

而ports指令则用于定义要暴露到主机外部的端口，它支持长短两种语法格式。整体语法格式如下
```shell
[host:][start_port[-end_port]:][con_start_port-]con_end_port
```
完整使用示例
```yaml
ports:
  - "3000"
  - "3000-3005"
  - "8000:8000"
  - "9090-9091:8080-8081"
  - "49100:22"
  - "127.0.0.1:8001:8001"   # 主机地址、端口和容器端口
  - "127.0.0.1:5000-5010:5000-5010"
  - "6060:6060/udp"   # 主机端口、容器端口和协议
```

而长格式的使用语法中，端口的相应各属性需要以专用参数给出

- target: 容器的端口
- published: 暴露的端口
- protocol：端口协议（tcp或udp）
- mode：host用于在每个节点上发布主机端口，或者使用ingress用于负载平衡的群集模式端口；

下面的示例中实现了把容器的80/tcp端口暴露到主机的8080/tcp端口
```yaml
ports:
  - target: 80
    published: 8080
    protocol: tcp
    mode: host

# 注意：ports指令与"network:host"互斥
```

- expose Directive:
  - 作用: 指定容器内部应该开放的端口，供 Docker 网络中的其他容器使用。
  - 无法访问外部: expose 的端口不会被绑定到宿主机的网络接口，外部主机无法通过宿主机的 IP 地址直接访问这些端口。
  - 用例: 适合需要容器之间通信而不需要外部直接访问的场景。
- ports Directive:
  - 作用: 将容器的端口映射到宿主机的端口，从而使得外部网络可以通过宿主机的 IP 地址和映射端口访问容器服务。
  - 外部可访问: 容器的服务被暴露到宿主机的端口，任何网络可以通过宿主机的 IP 和映射端口访问容器内的服务。
  - 用例: 适合需要外部客户端访问容器内部服务的场景，例如 Web 应用、API 服务器等。


### image

指定用于启动容器的镜像文件，支持标识容器镜像的各种形式
```yaml
image: redis
image: ubuntu:14.04
image: tutum/influxdb
image: example-registry.com:4000/postgresql
image: a4bc65fd
```

### networks

network指令用于定义要加入的网络，他需要以名称格式引用同名的顶级指令networks下定义的网络
下面的示例格式中的服务引用了some-network和other-network两个网络，这两个网络必须定义的顶级networks之下
```yaml
services:
  some-service: 
    networks: 
      - some-network
      - other-network
```

在服务中引用网络时还可以在加入的网络上给当前容器赋予一到多个别名(alias)，随后，同一网络上的其他容器就可以使用服务名称或容器的别名连接到服务中的容器。需要注意的是，同一个容器在不同网络上可以使用不同的名称。
```yaml
services:
  some-service:
    networks:
      some-network:
        aliases:
          - alias1
          - alias2
      other-network:
        aliases:
          - alias2
```

另外，也可以为容器在加入的网络中使用ipv4_addresses或ipv6_addresses指定使用的静态ip地址，不过这种功能要求在顶级networks配置段中必须定义了ipam驱动且指定的相关的CIDR格式的网络地址范围
```yaml
version: "3.7"

services:
  app:
    image: nginx:alpine
    networks:
      app_net:
        ipv4_address: 172.16.238.10
        ipv6_address: 2001.3984:3989::10

networks: 
  app_net: 
    ipam: 
      driver: default
      config: 
        - subnet: "172.16.238.0/24"
        - subnet: "2001:3984:3989::/64"
```


#### --network-alias和--link的区别

--network-alias用于在自定义网络中为容器设置别名，是其他容器可以通过别名访问该容器
```shell
docker run --network <network-name> --network-alias <alias-name> <image>
```

--network-alias主要特点
- 作用范围
  - 别名在特定的Docker自定义网络中生效。在同一个网络中的所有容器都可以通过别名访问该容器
- 动态解析
  - 容器的别名动态解析。别名指向当前网络中最新的IP地址，支持容器的动态IP分配
- 服务发现
  - 主要用于容器间服务发现和简化容器间通信。不需要预定义链接
- DNS解析
  - 使用Docker内部的Docker服务解析别名。适用于Docker Compose和Docker Swarm等服务编排场景

-- link用于将一个容器链接到另一个容器，使其可以通过指定的别名访问目标容器。连接是静态的
```shell
docker run --link <container-name-or-id>:<alias-name> <image>
```



## 通过案例学习compose
```yaml

```