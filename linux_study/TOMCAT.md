## 企业级WEB应用服务器TOMCAT

### Java动态网页技术

#### servlet

- Servlet是Java编程语言的一种服务端程序，主要用于扩展Web服务器的功能。Servlet运行在Web服务器中，接收并响应来自客户端（通常是Web浏览器）的请求

- 如果要用Servlet构建Web应用，则需要将Html标签嵌套在Java的逻辑代码中，而Html代码有要频繁迭代，相应的，需要重新编译，这种开发模式非常不方便


#### JSP

- JSP（Java Server Pages）是一种用于创建动态Web页面的Java技术，与Servlet一样，JSP也是在服务器端执行的，但其主要目标是简化Web页面的开发，允许开发者在Html页面中嵌入Java代码

- 以下是一些关键的JSP特性和与Servlet的区别
  - 页面描述语言：JSP使用一种称为JSP标记的页面描述语言，允许开发者在HTML页面中嵌入Java代码片段。这些标记以<% %>为界，使得在页面中嵌入动态内容变得更加容易。
  - 易读性：JSP的语法更接近HTML，因此对于前端开发者来说更易读写，开发者可以在HTML页面中嵌入Java代码，而无需像Servlet那样在Java代码中嵌套HTML字符串
  - 简化开发：JSP旨在简化动态WEB页面的开发，使得将Java代码嵌入HTML更加直观，相对于Servlet，JSP提供了更高层次的对象
  - 隔离逻辑和展示：Servlet通常在Java代码中生成HTML，而JSP允许在HTML中插入Java代码，这有助于更好地隔离逻辑和展示
  - 自定义标签库：JSP允许开发者定义和使用自定义标签库，以便将特定的逻辑模块化，提高代码的可重用性
  - 独立性：Servlet是一个独立的Java类，而JSP页面实际上在首次访问时被Servlet容器翻译成Java代码并编译成Servlet。因此，从本质上说，Servlet和JSP最终都是以Servlet的形式在服务器上执行

- 虽然Servlet和JSP在某些方面有区别，但他们通常一起使用，Servlet用于处理业务逻辑，而JSP用于呈现用户界面。在实际的WEB应用中，Servlet和JSP经常一起协同工作，已达到更好的代码组织和可维护性。


#### MVC

- MVC（Model-View-Controller）是一种设计模式，使得每个组件可以独立地变化而不影响其他组件。这种分离有助于提高代码的可维护性，可扩展性和复用性。常见的应用场景包括Web开发框架，图形用于界面GUI应用程序等

- 模型（Model）：模型表示应用程序的数据和业务逻辑。它负责处理数据的存储，检索和更新，同时包含应用程序的业务规则。模型通常不包含有关用户界面或展示方式的信息，而是专注于处理数据

- 视图（View）；视图负责用户界面的呈现和展示，它接收来自模型的数据，并将其以用户友好的方式显示。视图不负责处理数据。而只关注展示和用户交互

- 控制器（Control）：控制器充当模型和视图之间的协调者。它接收用户的输入（通常来自用户界面），然后根据输入更新模型或视图。控制器负责处理用户请求，更新模型的状态以及选择适当的视图进行展示

#### REST

- REST是一种基于网络的软件架构风格，代表"Representational State Transfer"（表示层状态转移）。它是由RoyFielding在他的博士论文中提出的，并成为构建分布式系统和网络应用程序的一种设计原则



#### JDK和JRE

jRE(Java Runtime Environment)和JDK（Java Development Kit）是Java平台中两个不同但相关的组件，他们之间有以下关系:

- JDK包含JRE：JDK是Java开发工具包，它是Java开发的完整包。JDK包括了JRE，以及用于Java开发的一系列工具和库，比如编译器（javac）、调试器（jdb）、文档生成器（javadoc）等。因此，可以说JRE是JDK的一个子集

- JRE用于运行Java程序：JRE是Java运行时环境，提供了在计算机上运行Java应用程序所需的所有组件。它包含Java虚拟机（JVM）、Java类库、Java命令行工具和其他支持文件。当用户仅需要运行Java程序时，安装JRE就足够了

- JDK用于开发和运行Java程序：JDK不仅包含了JRE，还包含了用于开发Java应用程序的工具和库。开发人员使用JDK中的工具编写、编译和调试Java代码、JDK是面向Java开发人员的完整工具包、而JRE主要面向终端用户，用于执行Java应用程序。

总而言之，JDK是适用于Java开发的完整套件，包含JRE和其他开发工具，而JRE则是仅包含运行时环境的一部分，如果你只是希望运行Java程序，安装JRE就是足够了。如果你要进行Java应用程序的开发，那么你需要安装JDK。


#### Oracle JDK

```shell
# Ubuntu中安装
dpkg -i jdk-11.0.22_linux_x64_bin.deb

# Rocky中安装
rpm -ivh jdk-11.0.22_linux-x64_bin.rpm
```


#### OpenJDK

```shell
# Ubuntu安装
apt update; apt list openjdk*
apt install openjdk-11-jdk -y

# rokcy安装
yum list java*openjdk*
yum install java-11-openjdk -y
```



### Tomcat基本使用

#### Tomcat介绍

Tomcat(全程为Apache—Tomcat)是一个开源的、轻量级的应用服务器，由Apache软件基金会开发和维护，它实现了Java—Servlet、JavaServerPages(JSP)和Java Expression Language（EL）等Java EE规范。并提供了一个运行这些Web应用程序的环境。在使用Tomcat时，将javaWeb应用程序（包括Servlet、JSP等文件）部署到TOmcat服务器中，然后通过HTTP协议访问这些应用程序，Tomcat提供了一个简单而强大的方式来托管和运行JavaWeb应用程序

Tomcat具有以下一些特点

- Servlet容器：Tomcat是一个Servlet容器，负责处理和执行Java Servlet。Servlet是一种用Java编写的服务器端程序。用于处理Web请求和生成动态Web内容；

- JSP支持：Tomcat还支持JSP，一种将Java代码嵌入HTML中的技术，用于创建动态WEB页面

- 轻量级：Tolsmcat是轻量级应用服务器，易于安装和配置。它专注于基本的Servlet和JSP支持

- 开源

- 连接器支持：Tomcat支持多种连接器，可以与不同的Web服务器进行集成。最常见的是与Apache Http服务器一起使用的AJP连接器

- 管理工具

- 安全性

- 跨平台性


#### jar包和war包

- Jar包可以直接在JVM上运行

- War包则必须部署在tomcat上


#### Tomcat安装

- Ubuntu中安装

```shell
# Ubuntu
apt install tomcat9*

systemctl status tomcat9.service

# tomcat默认使用8080端口

# 浏览器上使用IP:8080查看

# ubuntu中的包安装版tomcat存在Bug（无法将资源配置到catalina.base目录之外）
# 因此使用手动下载官方软件包，然后编译安装

wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.87/bin/apache-tomcat-9.0.87.tar.gz

tar xf apache-tomcat-9.0.87.tar.gz -C /usr/local/

cd /usr/local

ln -sv apache-tomcat-9.0.87/ tomcat

# 添加环境变量
ln -sv /usr/local/tomcat/bin/* /usr/local/bin/

# 启动
catalina.sh start

# 访问http://IP:8080/查看

# 用脚本停止
shutdown.sh

# 添加用户并修改文件属主属组
useradd -r -s /sbin/nologin tomcat
chown -R tomcat.tomcat /usr/local/tomcat/

# 服务脚本
cat /lib/systemd/system/tomcat/service
[Unit]
Description=Tomcat
After=syslog.target.network.target

[Service]
Type=forking
Environment=Java_HOME=/usr/lib/jvm/jdk-11-oracle-x64/
ExecStart=/usr/local/tomcat/bin/startup.sh
ExecStop=/usr/local/tomcat/bin/shutdown.sh
PrivateTmp=true
User=tomcat
Group=tomcat

[Install]
WantedBy=multi-user.target

# 加载到daemon
systemctl daemon-reload

# 查看tomcat状态
systemctl status tomcat.service
```

- Rocky中安装

```shell
wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.87/bin/apache-tomcat-9.0.87.tar.gz

tar xf apache-tomcat-9.0.87.tar.gz -C /usr/local/

ln -sv /usr/local/apache-tomcat-9.0.86/ /usr/local/tomcat

# 主要使用的脚本
ls /usr/local/tomcat/bin/

# 加环境变量
cat /etc/profile.d/tomcat.sh

#!/bin/bash
PATH=/usr/local/tomcat/bin:$PATH

# 执行该脚本
source /etc/profile.d/tomcat.sh

# 创建用户
useradd -r -s /sbin/nologin tomcat
chown -R tomcat.tomcat /usr/local/tomcat/

# 服务脚本
cat /lib/systemd/system/tomcat.service
[Unit]
Description=Tomcat
After=syslog.target network.target

[Service]
Type=forking
Environment=JAVA_HOME=/usr/bin/jvm/jdk-11-oracle-x64/
ExecStart=/usr/local/tomcat/bin/startup.sh
ExecStop=/usr/local/tomcat/bin/shutdown.sh
PrivateTmp=true
User=tomcat
Group=tomcat

[Install]
WantedBy=multi-user.target

# 加载服务脚本
systemctl daemon-reload

# 查看状态
systemctl status tomcat.service

# 先用脚本停止，再用服务管理启动
shutdown.sh

systemctl start tomcat.service

# 加开机启动项
systemctl enable tomcat.service
```

#### Tomcat组成

```shell
ls -l /usr/local/tomcat/
bin                       # 管理脚本文件目录
BUILDING.txt  
conf                      # 配置文件目录
CONTRIBUTING.md
lib                       # 库文件目录
LICENSE
logs                      # 日志目录
NOTICE
README.md
RUNNING.txt
temp                      # 临时文件目录
webapps                   # 应用程序目录   相当于/var/www/html
work                      # Jsp编译后的结果文件，建议提前预热访问，升级应用后，删除此目录数据才能更新
```

#### tomcat和catalina的关系

Tomcat的核心分为三个部分

- Web容器：用于处理静态页面
- JSP容器：把jsp翻译成一般的Servlet
- catalina：是一个Servlet容器，用于处理Servlet

#### tomcat组件

每一个组件都有一个Java类实现，在配置文件中通常用className来指定


### Tomcat常用配置项

```shell
tree /usr/local/tomcat/conf/
Catalina ---localhost    # 每个项目的单独配置文件存放目录
catalina.policy          # java程序对各目录的权限配置
catalina.properties      # tomcat环境变量配置以及jvm调优相关参数
context.xml              # web项目默认的上下文配置，包括数据库连接池，JNDI资源，会话管理等，每个项目也可以单独设置
jaspic-provider.xml      # jaspic配置
jaspic-providers.xsd     # 上述文件中的标签取值约束
logging.properties       # tomcat的日志配置，定义日志级别，格式等
server.xml               # 主配置文件，用于配置整个Tomcat服务器的全局设置，包括连接器，虚拟主机，引擎等，定义了Tomcat基本结构和行为
tomcat-users.xml         # 用户配置文件，用于配置Tomcat的用户，角色和其对应的权限
tomcat-users.xsd         # 上述文件中的标签取值约束
web.xml              
```

#### /usr/local/tomcat/conf/web.xml

`/usr/local/tomcat/conf/web.xml`文件是Apache Tomcat中用于配置Web应用程序的部署描述符（Deployment Description）文件，采用XML格式。在这个文件中，可以配置许多与WEB应用程序相关的设置。

- 常见的配置及其含义

```xml
<!-- mime类型-->
<mime-mapping>
  ...
</mime-mapping>
...
<mime-mapping>
    <extension>zirz</extension>
    <mime-type>application/vnd.zul</mime-type>
</mime-mapping>
<mime-mapping>
    <extension>zmm</extension>
    <mime-type>application/vnd.handheld-entertainment+xml</mime-type>
</mime-mapping>

<!-- 默认主页-->
<welcome-file-list>
    <welcome-file>index.html</welcome-file>
    <welcome-file>index.htm</welcome-file>
    <welcome-file>index.jsp</welcome-file>
</welcome-file-list>

<!-- 错误页面，后续详解-->
<error-page>
</error-page>
```

#### /usr/local/tomcat/conf/server.xml

/usr/local/tomcat/conf/server.xml文件是Apache Tomcat中的主要配置文件之一，用于配置Tomcat服务器的全局设置，连接器(Connectors)，虚拟主机(Virtual Hosts)等。以下是一些server.xml文件中可能包含的主要配置项及其含义的简要解释


server.xml的组件结构

- Server: 服务器，Tomcat运行的进程实例，一个Server中可以有多个service，但通常就一个
- Service：服务，用来组织Engine和Connector的对应关系，一个Service中只有一个Engine
- Connector：连接器，负责客户端的HTTP、HTTPS、AJP等协议连接，一个Connector只属于某一个Engine
- Engine：引擎，用来响应并处理用户请求，一个Engine上可以绑定多个Connector
- Host：虚拟主机，可以实现多虚拟主机，例如使用不同的主机头区分
- Context：应用的上下文，配置特定url路径映射和目录的映射关系：url=>directory

- 总结：
  - 一个Service中只有一个Engine，
  - 一个Engine可以有多个Conector，
  - 但是一个Conector只属于一个Engine

server.xml文件解析

```xml
<!-- 最外层 -->
<!-- Server其他参数
  className   指定实现此组件的java类，默认org.apache.catalina.core.StandardServer
  address     监听端口绑定的地址，不指定默认为 localhost
-->
<!-- 因此可以通过telnet在本地连接8005，通过SHUTDOWN关闭tomcat
    telnet 127.0.0.1 8005
    > 输入SHUTDONW
    > tomcat即可被关闭
-->
<Server port="8005" shutdown="SHUTDOWN"> 

  <!-- 监听器 -->
  <Listener className="" />
  <!-- 配置全局命名资源 -->
  <GlobalNamingResources>
      <Resource key="value" key="value"... />
  </GlobalNamingResources>
...

  <!-- 
    元素定义了Tomcat中的一个服务（实例），一个tomcat服务器可以开多个实例，不同实例可以监听不同的端口，使用不同的配置和部署不同的Web应用程序，每个实例被定义成一个Service，一个Service可以包含多个连接器和多个虚拟主机
  -->

  <!--
      className   指定实现的Java类，默认org.apache.catalina.core.StandardService
      name        指定实例名称
  -->
  <Service className="" name="">
      <!--
          <Executor>      用于配置Service的共享线程池
          className       指定实现的Java类，默认org.apache.catalina.core.StandardThreadExecutor
          name            指定线程池名称，其他组件通过名称引用线程池
          threadPriority  线程优先级，默认值为5
          daemon          线程是否以daemon的方式运行，默认为true
          namePrefix      执行器创建每个线程时的名称前缀，最终线程的名称为namePrefix+threadNumber
          maxThreads      线程池激活的最大线程数量，默认为200
          minSpareThreads 线程池中最少空闲的线程数量，默认为25
          maxIdleTime     空闲线程被销毁的保留时长，默认60000ms,即空闲线程要保留一分钟才销毁
          maxQueueSize    可执行任务的最大列数，达到队列上限时的连接请求将被拒绝
          prestartminSpareThreads  在启动executor时是否立即创建minSpreThreads个线程，默认false，即需要时才创建 
      -->
      <Executor className="" name="" threadPriority="" daemon="" namePrefix="" maxThreads="" minSpareThreads="" maxIdleTime="" maxQueueSize="" prestartminSpareThreads="" />

      <!--
          <Connector ... /> 
          用于配置Tomcat的连接器，负责处理客户端与Tomcat之间的通信，一个service中可以有多个connector,每个connector定义了一个端口和协议的组合，允许Tomcat在不同的端口上监听不同的网络协议或配置不同的连接器属性

          port                指定监听端口
          address             指定监听IP，默认本机所有IP
          protocol            协议版本
          connectionTimeout   超时时长
          redirectPort        安全连接重定向的端口
          executor            指定共享线程池
          acceptCount         等待队列的最大长度，通常在tomcat所有处理线程均处于繁忙状态时，新发来的请求将被放置于等待队列中
          maxConnections      允许建立的最大连接数，当maxConnections小于acceptCount时，超出maxConnections的连接请求将被接收，但不会与之建立连接
          keepAliveTimeout    长连接状态的超时时间。超出该值时，长连接将关闭
          enableLookups       是否通过DNS查询获取客户端的主机名，默认为true，应设置为false可减少资源消耗
          compression         是否压缩数据。默认为off。on 表示只压缩text文本，force表示压缩所有内容
          useSendfile         是否启用sendfile的功能，默认为true，启用该属性将会禁止compression属性
          URIEncoding         用于指定编码URI的字符编码，默认UTF-8

      -->
      <Connector port="" protocol="" conectionTimeout="" redirectPort="" maxParameterCount="" />

      <!--
          <Engine...> </Engine>
          engine是service组件中用来分析协议的引擎机器，它从一个或多个connector上接收请求，并将请求交给对应的虚拟主机进行处理，最后返回完整的响应数据给connector,通过connector将响应数据返回给客户端
          engine元素必须嵌套在每个service中，且engine必须在其所需要关联的connector之后，这样在engine前面的connector都可以被此engine关联，而在engine后面的connector则被忽略。
          一个service只允许有一个engine，其内可以嵌套一个或多个Host作为虚拟主机，且至少一个host要和engine中的默认虚拟主机名称对应。除了host，还可以嵌套releam和valve组件

          className    指定实现的Java类，默认org.apache.catalina.core.StandardEngine
          defaultHost  默认虚拟主机，在Engine中定义的多个虚拟主机的主机名称中至少有一个跟defaultHost定义的主机名称相同（相当于nginx上的default_server）
          name         指定组件名称
          jvmRoute     在启用session粘性时指定使用哪种负载均衡的标识符。所有的tomcat server实例中该标识符必须唯一，它会追加在session标识符的尾部，因此能让前端代理总是将特定的session转发至同一个tomcat实例上。
      -->
      <Engine className="" defaultHost="" name="" jvmRoute="">

          <!-- 
              在Engine内部配置了一个安全领域（Realm）用于身份验证和授权，该配置对Engine下的所有Host生效

              classNmae     指定实现的java类，不同的类表示组件功能不同，属性不同
              常用类：
                    JAASRealm    基于java Authintication and Authorization Service实现用户认证
                    JDBCRealm    通过JDBC访问某关系型数据库表，实现用户认证
                    JNDIRealm    基于JNDI使用目录服务实现用户信息的获取
                    MemoryRealm  查找tomcat-user.xml文件实现用户信息的获取
                    UserDatabaseRealm 基于UserDatabase文件（通常是tomcat-user.xml）实现用户认证
          -->
          <Releam className="">
          </Releam>

          <!--
              <Host></Host>
              host容器用来定义虚拟主机，engine从connector接收到请求进行分析后，会将相关的属性参数传递给对应的（筛选方式是从请求首部的host字段和虚拟主机名进行匹配）虚拟host进行处理。如果没有合适的虚拟主机，则传递给默认虚拟主机。因此每个容器中必须至少定义一个虚拟主机，且必须有一个虚拟主机和engine容器中定义的默认虚拟主机名称相同，其下级标签包括：Alias, Cluster, Listener, valve, Realm, Context

              常用参数
              className      指定实现的java类，默认org.apache.catalina.core.StandardHost
              name           指定主机名，忽略大小写，可以使用通配符，匹配优先级低
              appBase        此项目的程序目录（网站家目录）
              xmlBase        此虚拟主机上的context xml目录
              autoDeploy     Tomcat处于运行状态时放置于appBase目录中的应用程序文件是否自动进行部署，默认true
              unpackWARs     自动解压缩war包
              workDir        该虚拟主机的工作目录，每个Webapp都有自己的临时IO目录，默认该工作目录为$CATALINA_BASE/work
          -->
          <Host>

              <!--
                  定义一个特定功能的组件，可以有多条，按照定义顺序生效
                  className   指定实现的Java类，不同的class组件功能不同，属性不同

                  常用功能：
                  AccessLogValve        访问日志
                  ExtendedAccessValve   扩展功能的访问日志
                  RequestDumperValve    请求转储
                  RemoteAddrValve       基于远程地址的控制访问(类似Nginx的allow和deny)
                  RemoteHostValve       基于远程主机名的访问控制
                  ......
              -->
              <Valve>

              </Valve>

              <Valve>

              </Valve>
              ......

          </Host>

          <!--
              <Context></Context>
              配置WEBAPP的上下文，tomcat对请求uri与context中定义的path进行最大匹配前缀的规则进行挑选，从中选出使用哪个Context来处理该HTTP请求，必须要有一个context的path为空字符串，用于处理无法被现有规则命中的URI
              类似于locaiton / {}

              常用参数
              className          指定实现的java类，默认值 org.apache.catalina.core.StandardContext
              cookie             默认为true，表示启用cookie来标识session
              path               定义生效的URL路径规则，如果配置是独立文件，此属性可以为空，tomcat可以用文件名来推出path
              ...

          -->
          <Context>
          
          </Context>

      </Engine>

  </Service>
</Server>
```

### Tomcat工作原理

1. 客户端向服务器发请求
2. 由连接器接受这个请求到指定端口
   - 连接器就是server.xml中的<Connector>
   - 通常连接器有两种
     - HTTP, 默认8080
     - AJP, 默认8009
3. 连接器接收数据后，交给引擎处理
4. 将访问的资源解析到虚拟主机Host
5. 通过Host的name进行匹配
   1. 匹配后，通过context获取请求，并通过mapping table找到-=-------匹配【·								v  对应的servlet
   2. servlet（server applet）:是以servlet编码方式写的一个tomcat的服务器端 
   3. servlet是在web.xml 里定义的

6. 由servlet去封装request和response
7. 封装好后将结果返回引擎，再从引擎返回到连接区，在返回给客户端

​	

### **各组件的作用及关系**

#### **1. Server**

- **顶层组件**：`<Server>` 是 Tomcat 配置文件的顶层组件，用来定义整个 Tomcat 服务器实例的配置。

- 作用

  ：

  - 代表整个服务器的运行实例。
  - 包含一个或多个 `<Service>`。
  - 负责监听服务器生命周期（启动和关闭）事件。
  - 通过 `port` 属性配置一个端口（通常是 `8005`），用于监听关闭命令。

- 关键属性

  ：

  - `port`：监听关闭命令的端口号。
  - `shutdown`：接收关闭命令的字符串。

```
xmlCopy code<Server port="8005" shutdown="SHUTDOWN">
    ...
</Server>
```

#### **2. Service**

- **中间组件**：`<Service>` 是 Server 的子组件，一个 Server 可以包含一个或多个 Service。

- 作用

  ：

  - 表示一个具体的服务实例。
  - 负责将 `Connector` 和 `Engine` 组合在一起工作。
  - 允许在同一个服务器中运行多个服务（比如一个服务处理 HTTP，另一个处理 HTTPS）。

- 关键属性

  ：

  - `name`：Service 的名称。

```
xmlCopy code<Service name="Catalina">
    ...
</Service>
```

#### **3. Engine**

- **核心组件**：`<Engine>` 是 Service 的子组件，一个 Service 必须包含一个 Engine。

- 作用

  ：

  - 表示整个服务的核心引擎，负责将来自 Connector 的请求分发到正确的 Web 应用（Context）。
  - 每个 Engine 必须配置一个默认的 `Host`，以便处理请求时无法匹配具体虚拟主机的情况。

- 关键属性

  ：

  - `name`：Engine 的名称。
  - `defaultHost`：默认虚拟主机的名称，用于处理无法匹配到其他 Host 的请求。

```
xmlCopy code<Engine name="Catalina" defaultHost="localhost">
    ...
</Engine>
```

#### **4. Connector**

- **通信组件**：`<Connector>` 是 Service 的子组件，用于定义服务的通信方式。

- 作用

  ：

  - 负责监听特定的协议端口（如 HTTP、HTTPS、AJP 等），将收到的请求传递给 Engine。
  - 一个 Service 可以包含多个 Connector，以支持不同协议或端口。

- 关键属性

  ：

  - `port`：监听的端口号。
  - `protocol`：通信协议（如 HTTP/1.1、AJP/1.3）。
  - `URIEncoding`：编码方式（如 UTF-8）。

```
xml


Copy code
<Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />
```

------



#### **组件之间的关系**

1. **`Server → Service`**
   - 一个 Server 可以包含多个 Service，每个 Service 是一个独立的服务实例。
2. **`Service → Engine`**
   - 每个 Service 必须包含一个 Engine，Engine 是整个服务的核心。
3. **`Service → Connector`**
   - 每个 Service 可以包含多个 Connector，负责监听不同协议或端口的请求。
4. **`Engine → Host → Context`**
   - Engine 负责请求分发，它包含一个或多个虚拟主机（Host）。
   - 每个 Host 代表一个虚拟主机（比如不同的域名）。
   - 每个 Host 包含多个 Web 应用（Context），每个 Context 对应一个部署的应用。

------



#### **工作流程**

1. **启动阶段**：
   - `Server` 启动后，初始化所有 `Service`。
   - 每个 `Service` 初始化对应的 `Engine` 和 `Connector`。
2. **请求处理阶段**：
   - `Connector` 监听特定端口，接收来自客户端的请求。
   - `Connector` 将请求交给 `Engine`。
   - `Engine` 根据请求的域名（Host Header）选择对应的 `Host`。
   - `Host` 根据请求的 URI，将请求分发到对应的 `Context`（Web 应用）。
   - `Context` 将请求交给具体的 Servlet 或资源处理。



#### **示例配置**

```xml
<Server port="8005" shutdown="SHUTDOWN">
    <!-- 定义一个服务 -->
    <Service name="Catalina">

        <!-- 定义一个 HTTP 协议的连接器 -->
        <Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />

        <!-- 定义一个 AJP 协议的连接器 -->
        <Connector port="8009" protocol="AJP/1.3" redirectPort="8443" />

        <!-- 定义服务的核心引擎 -->
        <Engine name="Catalina" defaultHost="localhost">

            <!-- 定义一个虚拟主机 -->
            <Host name="localhost" appBase="webapps" unpackWARs="true" autoDeploy="true">

                <!-- 定义一个 Web 应用 -->
                <Context path="" docBase="ROOT" />
                <Context path="/app1" docBase="app1" />
            </Host>

        </Engine>
    </Service>
</Server>
```

------



#### **总结**

- **Server** 是顶层容器，负责管理多个 Service 的运行。
- **Service** 将 Connector 和 Engine 绑定在一起，管理整个服务的通信和请求分发。
- **Engine** 是 Service 的核心组件，负责请求的分发。
- **Connector** 负责网络通信，将请求转发给 Engine。
- 各组件紧密协作，构成了 Tomcat 的请求处理体系。

### 日志配置

自定义日志内容配置的转义字符说明

```shell
https://tomcat.apache.org/tomcat-9.0-doc/config/valve.html
```

默认Web访问日志

```xml
<Host name="localhost"  appBase="webapps"
            unpackWARs="true" autoDeploy="true">

        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
               prefix="localhost_access_log" suffix=".txt"
               pattern="%h %l %u %t &quot;%r&quot; %s %b" />

</Host>
```

上述配置解析

```shell
className="org.apache.catalina.valves.AccessLogValve"    # 日志类
directory="logs"                                         # 日志文件目录
prefix="localhost_access_log"                            # 日志文件前缀
suffix=".txt"                                            # 日志文件后缀
pattern="%h %l %u %t &quot; %s %b"                       # 日志文件内容格式
```

更改为json格式的日志配置

```xml
<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
 prefix="localhost_access_log" suffix=".txt" pattern="
 {&quot;clientip&quot;:&quot;%h&quot;,&quot;ClientUser&quot;:&quot;%l&quot;,&quot
 ;authenticated&quot;:&quot;%u&quot;,&quot;AccessTime&quot;:&quot;%t&quot;,&quot;
 method&quot;:&quot;%r&quot;,&quot;status&quot;:&quot;%s&quot;,&quot;SendBytes&qu
 ot;:&quot;%b&quot;,&quot;Query?
 string&quot;:&quot;%q&quot;,&quot;partner&quot;:&quot;%
 {Referer}i&quot;,&quot;AgentVersion&quot;:&quot;%{User-Agent}i&quot;}" />
```

```shell
# 重新加载配置文件
systemctl restart tomcat.service

# 使用jp查看
tail -n 1 /usr/local/tomcat/logs/localhost_access_log.2024-0323.txt | jq
```


### 应用部署

Tomcat部署应用有三种方式：

- 以文件或war包直接部署
  - 将应用文件夹或war包文件直接复制到tomcat的webapps目录下，这样tomcat启动的时候会将webapps目录下的文件夹或war文件的内容当做应用部署

- 编辑/usr/local/tomcat/conf/server.xml配置文件，添加Context标签
  - 在tomcat的server.xml配置文件中的Host节点下增加Context子节点，配置域名，文件路径

- 在/usr/local/tomcat/conf/[Engine]/[Host]目录下创建独立配置
  - 在该目录下新建xml文件，文件名为应用名，然后在配置文件中添加Context子节点，配置域名，文件路径等

注意事项

- 访问10.0.0.150/doc

```shell
<Host name="localhost"  appBase="webapps"
            unpackWARs="true" autoDeploy="true">
# 虽然配置文件上是指定在webapps
# 如果访问10.0.0.150:8080/test.html,实际访问路径是webapps/ROOT/test.html
# 如果访问10.0.0.150:8080/docs[examples, host-manager, manager]
# 实际访问路径是webapps/docs[examples, host-manager, manager]
# 如果ROOT目录下有同名的docs等，外面的优先级更高
# 只有直接在10.0.0.150:8080/file，只有在/后直接加文件名，则会从ROOT目录下找文件
# 如果/后是目录名，则该目录与ROOT同级
```

访问10.0.0.150:8080/docs,返回403的原因

```shell
# 该目录下有一个context.xml文件
cd /usr/local/apache-tomcat-9.0.88/webapps/docs/META-INF

vim context.xml

<Context antiResourceLocking="false" >
  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
</Context>

# 这个内容限制了该页面只有本机127网段的ip才能访问，把它注释掉即可
```

访问jsp等动态文件，会在/usr/local/apache-tomcat-9.0.88/work目录下生成servlet代码

```shell
[root@mystical /usr/local/apache-tomcat-9.0.88] $tree work/
work/
└── Catalina
    └── localhost
        ├── docs
        ├── examples
        ├── host-manager
        ├── manager
        │   └── org
        │       └── apache
        │           └── jsp
        │               └── WEB_002dINF
        │                   └── jsp
        │                       ├── _403_jsp.class
        │                       └── _403_jsp.java
        ├── ROOT
        │   └── org
        │       └── apache
        │           └── jsp
        │               ├── index_jsp.class
        │               └── index_jsp.java
        └── test
```

- 所以如果修改jsp文件后，再次在浏览器访问，如果没有生效，可以尝试将worker下的缓存文件清除，再重新访问，即可生效

#### 默认端口和默认主页

```shell
# 全局默认端口配置，可以修改端口，或增加connector
vim conf/server.xml

<Connector port="8080" protocol="HTTP/1.1"        # 此处改成80无效
          connectionTimeout="20000"               # 因为tomcat服务器以tomcat身份运行
          redirectPort="8443"                     # 无法使用特权端口
          maxParameterCount="1000"
          />

<Connector port="8000" protocol="HTTP/1.1"        # 增加一个connector,监听8000,重启服务
          connectionTimeout="20000"               
          redirectPort="8443"                     
          maxParameterCount="1000"
          />

systemctl restart tomcat.servicecd .     
```

```shell
# /conf/web.xml
# 默认全局配置
# 可以在这里更改或添加默认主页
i<>
```

在单独项目目录设置默认主页

```shell
tree webapps/test/
test
    ├── index.html
    ├── index.txt
    └── WEB-INF          # 创建WEB-INF
        └── web.xml      # 输出web.xml

# 注意xml文件的格式，注意清除隐藏字符
cat web.xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" version="4.0" metadata-complete="true">

<welcome-file-list>
    <welcome-file>index.txt</welcome-file>
    <welcome-file>index.html</welcome-file>
    <welcome-file>index.htm</wesslcome-file>
    <welcome-file>index.jsp</welcome-file>
</welcome-file-list>
```

#### 部署独立域名的WEB服务

```shell
# 创建文件目录
mkdir -pv /data/webapps/ROOT

# 向文件中添加文件
cp index.{html,jsp} /data/webapps/ROOT/

# 修改权限：只要给jsp文件w权限即可

# 新增域名配置
<Host name="java.fenge.org" appBase="/data/webapps" unpackWARs="true" utoDeploy="true">
</Host>

# 重启服务，在客户端配置域名解析，并测试
systemctl restart tomcat.service
```

#### 以war格式压缩包部署

```shell
# 注意权限问题，war里的文件属主属组要是tomcat
# 创建文件

cd /data/webapps/ROOT 

# 将ROOT下的文件打成war包
cp jar -cvf ../../test.war *

# 此时test.war和webapps平级目录
# 将test.war移动进webapps
# 自动解包部署
[root@mystical /data/webapps] $ls
ROOT  test  test.war

[root@mystical /data/webapps] $tree test
test
├── index.html
├── index.jsp
└── META-INF
    ├── MANIFEST.MF
    └── war-tracker
```

#### 实验：部署jpress 


#### 默认应用管理

```shell
# 在META-INF目录下的context.xml里将10网段加进去
<Valve className="org.apache.catalina.valves.RemoteAddrValve"
      allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1|10\.\d+\.\d+\.\d+" />

# 然后在conf/tomcat-users.xml里将用户密码的设置添加进去
<role rolename="manager-gui"/>
<user username="tomcat" password="123456" roles="manager-gui"/>

# role 说明
# manager-gui       
# manager-status    
# manager-script    
# manager-jmx       
以HTML 显示 status 页面
仅显示 status 页面
以文本显示 status 页面内容   
以 xml 显示页面内容 

# 重启服务
systemctl restart tomcat:

# host-manager
<role rolename="manager-gui"/>
<role rolename="admin-gui"/>
<user username="tomcat" password="123456" roles="manager-gui,admin-gui"/>
```

### Tomcat的多实例部署

本质是将主程序目录和数据目录分离，使用一个主程序控制多个数据目录，每个数据目录可以是不同的项目

目录结构

```shell
# 主程序目录只有两个目录，一个是主程序bin目录，一个是函数库lib目录
[root@ubuntu2204 ~]#ls /usr/local/tomcat
bin  BUILDING.txt  CONTRIBUTING.md  lib  LICENSE  NOTICE  README.md  RELEASE-NOTES  RUNNING.txt

# 实例数据目录
[root@ubuntu2204 ~]#ls /www/tomcat1
conf  logs  temp  webapps  work
[root@ubuntu2204 ~]#ls /www/tomcat2
conf  logs  temp  webapps  work

# 使用脚本控制多实例
# 开启多实例
bash start_tomcat.sh /www/tomcat1
bash start_tomcat.sh /www/tomcat2

# 注意修改tomcat数据目录中server.xml中的端口，防止端口冲突
# 比如tomcat1使用默认的8080端口访问（server标签），使用8085（connector标签）控制
# tomcat2使用默认的8081端口访问，使用8086控制
```

控制脚本内容

```shell
# 确定主程序目录
export CATALINA_HOME=/usr/local/tomcat/
# 确定数据目录地址
export CATALINA_BASE=${1%/}

TOMCAT_ID=`ps aux | grep "java"|grep "Dcatalina.base=$CATALINA_BASE "|grep -v "grep"|awk '{ print $2 }'`

if [ -n "$TOMCAT_ID" ] ; then
echo "tomcat(${TOMCAT_ID}) still running now . please shutdown it first";
exit 2;
fi

# 使用startup.sh开启tomcat，将startup改成shutdown即可实现关闭指定tocmat实例
TOMCAT_START_LOG=`$CATALINA_HOME/bin/startup.sh`

if [ "$?" = "0" ]; then
    echo "$0 $1 start successed"
else
    echo "$0 ${1%/} start faild"
    echo $TOMCAT_START_LOG
fi
```


### 反向代理中部署Tomcat

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image45.png)

#### Nginx单机反向代理实现

在同一台服务器上部署Nginx和Tomcat，Nginx监听80端口，将请求转发至后端Tomcat的8080端口进行处理

```shell
# tomcat配置
cat conf/server.xml

<Host name="java.fenge.org" appBase="/data/webapps" unpackWARs="true" utoDeploy="true">
</Host>

systemctl restart tomcat.service

# nginx配置
cat /etc/nginx/conf.d/java.fenge.org.conf

server {
    listen 80;
    server_name java.fenge.org;

    location / {
        proxy_pass http://10.0.0.150:8080;
        proxy_set_header host $http_host;
    }
}

# 在nginx中配置动静分离

server {
        listen 80;
        server_name java.fenge.org;
        root /data/nginx/html/jhtml;


        location ~* \.jsp$ {
                proxy_pass http://10.0.0.150:8080;
                proxy_set_header host $http_host;
        }
}
```

#### Nginx代理多台Tomcat实现

实验准备

- Nginx --------- 10.0.0.180
- Tomcat -------- 10.0.0.150
- Tomcat -------- 10.0.0.151

```shell
# tomcat部署，两台配置一样

<Host name="java.fenge.org"  appBase="/data/webapps"  unpackWARs="true" autoDeploy="true">
</Host>

# Tomcat 10.0.0.151 配置
upstream group11 {
        server 10.0.0.151:8080;
        server 10.0.0.150:8080;
}

server {
        listen 80;
        server_name java.fenge.org;
        root /data/nginx/html/jhtml;


        location ~* \.jsp$ {
                proxy_pass http://group11;
                proxy_set_header host $http_host;
        }
}
```

#### 实现会话保持

```shell
# 实现客户端会话绑定
[root@ubuntu ~]# cat /etc/nginx/conf.d/java.m99-magedu.com.conf 
upstream tomcat {
    ip_hash;
    hash $remoute_addr;     
    hash $cookie_JSESSION consistent;   # 三选一
    
    server 10.0.0.208:8080;
    server 10.0.0.210:8080;
}
```

#### 配置https监听转发到后端http

```shell
#先使用easy-rsa生成证书文件
# Nginx上的配置
upstream group1 {
        server 10.0.0.118:8080;
        server 10.0.0.128:8080;
}

server {
        server_name java.feng.org;
        root /data/html/java;
        return 302 https://$host$request_uri;
}


server {
        listen 443 ssl;
        server_name java.feng.org;
        root /data/html/java;

        ssl_certificate /usr/share/easy-rsa/pki/java.feng.org.pem;
        ssl_certificate_key /usr/share/easy-rsa/pki/private/java.feng.org.key;
        ssl_session_cache shared:sslcache:20m;
        ssl_session_timeout 10m;

        location ~* \.jsp$ {
                proxy_pass http://group1;
                proxy_set_header host $http_host;
        }
}
```

#### 实现真实客户端IP地址透传

```shell
# 在Nginx服务器上添加X-Forwarded-For
 location ~* \.jsp$ {
                proxy_pass http://group1;
                proxy_set_header host $http_host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

# 在tomcat的server.xml上更改日志，查看效果
<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
               prefix="java.feng.org_access_log" suffix=".txt"
                pattern="%h %l %u %t &quot;%r&quot; %s %b %{x-forwarded-for}i" />

```

#### Tomcat Session 复制集群

在上述Nginx代理多机Tomcat的架构中，我们在Nginx代理节点通过调度算法实现会话绑定，将来自同一客户端的请求调度到相同的后端服务器上，在这种情况下，如果后端Tomat服务不可用，Nginx在检测后会将请求调度到可用的节点，则原来的Session数据还是会丢失

我们可以使用Tomcat中的session复制功能，实现在多台Tomcat服务器上复制Session的功能，这种配置下，任何一台Tomcat服务器都会有全量的session数据

```xml
<!-- 在 server.xml 中 指定的 Host 标签内添加下列内容 -->
<Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster" channelSendOptions="8">
    <Manager className="org.apache.catalina.ha.session.DeltaManager" expireSessionsOnShutdown="false" notifyListenersOnReplication="true"/>

    <!-- Channel定义了用于节点间通信的通道 -->
    <Channel className="org.apache.catalina.tribes.group.GroupChannel">
    <!-- 定义集群相关配置，集群中每个节点此处配置相同，才表示是同一个集群，此处配置用来做心跳检测 -->
    <Membership className="org.apache.catalina.tribes.membership.McastService" address="228.0.0.4" port="45564" frequency="500" dropTime="3000"/>
    <!-- 定义集群节点接收消息的配置 -->  
    <Receiver className="org.apache.catalina.tribes.transport.nio.NioReceiver" address="auto"  port="4000" autoBind="100" selectorTimeout="5000"  maxThreads="6"/>

    <Sender className="org.apache.catalina.tribes.transport.ReplicationTransmitter">
        <Transport className="org.apache.catalina.tribes.transport.nio.PooledParallelSender"/>
    </Sender>
    <Interceptor className="org.apache.catalina.tribes.group.interceptors.TcpFailureDetector"/>
    <Interceptor className="org.apache.catalina.tribes.group.interceptors.MessageDispatchInterceptor"/>
    </Channel>
    <Valve className="org.apache.catalina.ha.tcp.ReplicationValve"  filter=""/>
    <Valve className="org.apache.catalina.ha.session.JvmRouteBinderValve"/>
    <Deployer className="org.apache.catalina.ha.deploy.FarmWarDeployer" tempDir="/tmp/war-temp/" deployDir="/tmp/war-deploy/" watchDir="/tmp/war-listen/" watchEnabled="false"/>
    <ClusterListener className="org.apache.catalina.ha.session.ClusterSessionListener"/>
 </Cluster>
```

- 在项目的web.xml中添加` <distributable/>`

```shell
cp -r webapps/ROOT/WEB-INF/ /data/webapps/ROOT/

cat /data/webapps/ROOT/WEB-INF/web.xml 
<?xml version="1.0" encoding="UTF-8"?>
 <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee 
http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
 version="4.0" metadata-complete="true">
<display-name>Welcome to Tomcat</display-name>
  <description>
     Welcome to Tomcat
  </description>
 <distributable />  # 添加此行       
</web-app>

# 保证权限
chown -R tomcat.tomcat /data/html/ROOT/WEB-INF/

systemctl restart tomcat.service

# 成功
# 中途失败可能
1. 目录权限
2. 配置文件

# 集群日志总结：
Replication member added:[org.apache.catalina.tribes.membership.MemberImpl[tcp://{10, 0, 0, 128}:4000,{10, 0, 0, 128},4000, alive=14089, securePort=-1, UDP Port=-1, id={73 9 60 -82 -42 28 78 -98 -114 -73 -89 127 17 117 -42 106 }, payload={}, command={}, domain={}]]
# 这段表面集群成员添加成功，表明一个集群成员（IP 地址为 10.0.0.128 端口 4000）已经成功被添加到集群中

Done sleeping, membership established, start level:[4]
# 集群建立完成

Deploying web application directory [/data/html/ROOT]
# 部署web应用，部署到指定的/data/html/ROOT目录

Manager []: In reply to the 'Get all session data' message sent at [5/5/24, 7:19 PM], a 'No matching context manager' message was received after [118] ms.
# 会话管理警告，得到了所有的数据，但是指出在集群中的某个节点上缺少有效的会话管理器配置。
# 这种情况下，基本可以确定是web.xml所在上下文的问题，要吗是这个文件本身配置写错了，要不就是上下文的权限有问题
```



### Memcached 实现Session共享

#### Memcached基础

Memcached(Memory Cache Daemon)是一种开源的，高性能的分布式内存对象缓存系统，主要用于减轻数据库负载，提高动态Web应用的性能。它最初由Brad Fitzpatrick开发，现在由一个开源社区维护

<span style="font-weight:700">以下是Memcached的一些关键特性</span>

1. 分布式缓存：Memcached可以在多台服务器上运行，形成一个分布式缓存系统，这意味着它可以横向扩展以处理大量的请求和数据存储需求
2. 内存存储：Memcached将数据存储在内存中，这使得它能够提供快速的读写操作。内存存储也是其高性能的主要原因之一
3. 简单的键值存储：Memcached是一个键值对存储系统，每个键对应一个值，这使得它非常适合存储简单的数据结构，如：对象，字符串等
4. 缓存有效期：可以为存储在Memcached中的数据设置生存时间，一旦超过该时间，数据被自动删除。这有助于确保缓存中的数据不会过期，同时减少了需要手动清理缓存的工作
5. 高性能：由于数据存储在内存中，Memcached提供了非常快速的读写操作。这使得它成为处理高并发，大规模应用的理想选择
6. 分布式哈希表：Memcached使用一致性哈希算法来确定数据存储在哪个节点，这确保了在添加和删除节点时，数据的迁移量被最小化，同时保持了负载均衡。
7. 支持多种编程语言


<span style="font-weight:700">以下是Memcached的限制</span>

1. 由于基于内存存储，存储容量受到物理内存的限制
2. 不具备持久性存储能力，数据一般在服务重启后会丢失。



<span style="font-weight:700">Memcached和Redis的比较</span>

相同点：

- 内存存储
- 键值存储
- 数据结构支持


不同点：

- 数据持久化
- 功能：Redis提供了许多附加功能，例如发布/订阅、事务、Lua脚本等，使得它不仅仅是一个缓存系统，还可以用作消息队列，计数器等。而Memcached更专注于作为分布式缓存的角色，功能相对简单
- 数据类型处理：Redis能处理更复杂的数据结构
- 性能：由于Redis提供了更多的功能和数据类型支持，因此在某方面可能略逊于Memcached。然而，具体性能取决于使用场景，数据访问模式以及部署配置等因素。


#### Memcached 工作机制

Memcached采用Slab Allocator机制来分配、管理内存

- Page：分配给Slab的内存空间，默认为1MB，分配后就得到一个Slab，Slab分配之后内存安装固定字节大小等分成chunk
- Chunk：用于缓存记录k/v值的内存空间，Memcached会根据数据大小选择存到哪一个chunk中，假设 chunk 有 128bytes、64bytes等多种，数据只有 100bytes 存储在 128bytes 中，存在少许浪费。chunk 增长因子 default: 1.25，Chunk 最大就是一个 Page 大小，所以 Memcached 无法存储单个 K/V 超过 1M的数据
- Slab Class：Slab 按照 Chunk 的大小分组，就组成不同的 Slab Class，第一个 Chunk 大小为 96B 的 Slab 为 Class1，Chunk 120B 为Class 2，如果有 100bytes 要存，那么 Memcached 会选择下图中Slab Class 2 存储，因为它是120 bytes 的 Chunk，Slab 之间的差异可以使用 Growth Factor控制，默认 1.25

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image46.png)

- 可控参数：Page大小（默认1M），chunk的成长因子（默认1.25）

懒过期
memcached不会监视数据是否过期，而是在取数据时才看是否过期，如果过期，把数据有效期表示为0，并不清楚该数据，以后可以覆盖该位置存储其他数据

LRU（最近最少使用算法）

集群
Memcached集群，成为基于客户端的分布式集群，即由客户端实现集群功能，即Memcached本身不支持集群，Memcached集群内部并不相互通信，一切都需要客户端连接到Memcached服务器后自行组织这些节点，并确定数据存储的点

#### 为什么Memcached是基于客户端的分布式集群

1. 无中心协调：Memcached服务器本身不维护关于其他服务器状态或数据存放位置的信息，它们独立运行，不需要彼此通信来处理缓存数据
2. 客户端决策：数据在哪里存储（哪台Memcached服务器）由客户端决定。客户端使用一致性hash等算法选择数据应该存储在哪个服务器上，这种方法减少了单点故障的风险，因为没有一个中央节点是关键的
3. 简单性和性能：这种模式使Memcached非常简单和高效。服务器仅仅响应客户端的请求，所有智能决策都由客户端完成。这减轻了服务器的计算负担，使系统能更快地响应。


#### 安装和启动

```shell
# 下载安装memcached
apt update; apt install memcached -y

# 查看memcached的状态
systemctl status memcached.service

# 启动脚本和配置文件
[root@ubuntu ~]# systemctl cat memcached.service | grep Exec
ExecStart=/usr/share/memcached/scripts/systemd-memcached-wrapper /etc/memcached.conf

# 注释掉-l, 使其对外监听所有设备
#-l 127.0.0.1

[root@mystical ~] $ss -tpln
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process                                      
LISTEN   0        128              0.0.0.0:22              0.0.0.0:*       users:(("sshd",pid=916,fd=3))               
LISTEN   0        1024             0.0.0.0:11211           0.0.0.0:*       users:(("memcached",pid=3124,fd=22)) 

# 使用nc可以连接memcached进行测试

nc 10.0.0.181 11211
>> stats    # 输入stats
STAT pid 3124
STAT uptime 126
STAT time 1714996697
STAT version 1.6.14
STAT libevent 2.1.12-stable
STAT pointer_size 64
STAT rusage_user 0.024244
STAT rusage_system 0.036366
STAT max_connections 1024
STAT curr_connections 2
STAT total_connections 3
STAT rejected_connections 0
STAT connection_structures 3
...

# 指定增长因子，每个chunk2倍大小增长
memcached -p 11211 -f 2 -u memcache -vv
# -f <num>   指定增长因子
# -p         指定端口
# -u         指定运行用户
# -P         指定pid文件路径
```

#### Memcached常用操作命令

在memcached中，根据功能不同可以将命令划分为存储、检索、删除、增加/减少、统计、清空等六个部分

```shell
# 命令格式
<command name> <key> <flag> <exptime> <bytes> [noreply]\r\n<data block>\r\n

# <command name>              具体命令
# <key>                       任意字符串，用于存取数据的标识
# <flag>                      任意一个无符号整型数学，该字段对服务器不透明，客户端可将其作为位域来存储数据特定信息
# <exptime>                   缓存有效期，以秒为单位
# <bytes>                     此次写入数据占用的空间大小
# [noreply]                   可选，表示服务器不用返回任何数据

# 常用命令
# stats                       显示当前memcached服务状态
# set                         设置一个key/value
# add                         key不存在时，新增一个key/value
# replace                     替换一个已存在的key中的内容
# append                      追加数据到key的尾部
# prepend                     插入数据到key的头部
# get                         获取key的flag及value
# delete                      删除一个key
# incr                        对key做自增1，key保存的必须是整数
# decr                        对key做自减1，key保存的必须是整数
# flush_all                   清空所有数据

# memcached的使用示例
[root@ubuntu ~]# telnet 10.0.0.206 11211
Trying 10.0.0.206...
Connected to 10.0.0.206.
Escape character is '^]'.
set test 1 30 3             # 设置一个 key/value ， key=test，flag=1，exp=30S，
bytes=3 
abc                         # 此处只能存3字节，不能多也不能少
STORED
get test                    # 获取数据
VALUE test 1 3
abc
END
get test                    # 30S 后数据消失
END
```



#### MSM介绍和安装

MSM(msmcached session manager) 提供将Tomcat的session保持到memcached或Redis的程序，可以实现高可用（该项目看在github上）

#### 基于Sticky模式实现Session共享集群

sticky模式即前端tomcat和后端memcached有关联（粘性）关系

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image47.png)

```shell
# nginx节点测试 Memcached远程访问

# 安装python包管理器pypi
apt install -y python3-pip

# 安装python客户端工具
pip install python-memcached

# 写一个memcache测试脚本
vim test.py

#!/usr/bin/python3

import memcache
client = memcache.Client(['10.0.0.150:11211','10.0.0.151:11211'],debug=True)

for i in client.get_stats('items'):
    print(i)

print('-' * 35)

for i in client.get_stats('cachedump 5 0'):
    print(i)

# 执行python脚本
[root@mystical ~] $python3 test.py 
('10.0.0.150:11211 (1)', {})
('10.0.0.151:11211 (1)', {})
-----------------------------------
('10.0.0.150:11211 (1)', {})
('10.0.0.151:11211 (1)', {})

# 显示无任何数据

# 配置（150的session写到151的memcached; 151的session写到150的memcached）
# tomcat节点配置session共享

# 10.0.0.150

# 下载相关jar包
cd /usr/local/tomcat/lib

wget https://repo1.maven.org/maven2/org/ow2/asm/asm/5.2/asm-5.2.jar
wget https://repo1.maven.org/maven2/com/esotericsoftware/kryo/3.0.3/kryo-3.0.3.jar
wget https://repo1.maven.org/maven2/de/javakaffee/kryo-serializers/0.45/kryo-serializers-0.45.jar
wget https://repo1.maven.org/maven2/de/javakaffee/msm/memcached-session-manager/2.3.2/memcached-session-manager-2.3.2.jar
wget https://repo1.maven.org/maven2/de/javakaffee/msm/memcached-session-manager-tc9/2.3.2/memcached-session-manager-tc9-2.3.2.jar
wget https://repo1.maven.org/maven2/com/esotericsoftware/minlog/1.3.1/minlog-1.3.1.jar
wget https://repo1.maven.org/maven2/de/javakaffee/msm/msm-kryo-serializer/2.3.2/msm-kryo-serializer-2.3.2.jar
wget https://repo1.maven.org/maven2/org/objenesis/objenesis/2.6/objenesis-2.6.jar
wget https://repo1.maven.org/maven2/com/esotericsoftware/reflectasm/1.11.9/reflectasm-1.11.9.jar
wget https://repo1.maven.org/maven2/net/spy/spymemcached/2.12.3/spymemcached-2.12.3.jar

# 修改配置
cat /usr/local/tomcat/conf/context.xml

# 添加下列内容
# 10.0.0.150
<Manager className="de.javakaffee.web.msm.MemcachedBackupSessionManager" memcachedNodes="m1:10.0.0.150:11211,m2:10.0.0.151:11211" failoverNodes="m1" requestUriIgnorePattern=".*\.(ico|png|gif|jpg|css|js)$" transcoderFactoryClass="de.javakaffee.web.msm.serializer.kryo.KryoTranscoderFactory"/>

# 10.0.0.151
<Manager className="de.javakaffee.web.msm.MemcachedBackupSessionManager" memcachedNodes="m1:10.0.0.150:11211,m2:10.0.0.151:11211" failoverNodes="m2" requestUriIgnorePattern=".*\.(ico|png|gif|jpg|css|js)$" transcoderFactoryClass="de.javakaffee.web.msm.serializer.kryo.KryoTranscoderFactory"/>

# 150和151都重启tomcat服务
systemctl restart tomcat
```

#### 基于非Sticky模式实现Session共享集群

```shell
# 将之前的数据改为
 <Manager className="de.javakaffee.web.msm.MemcachedBackupSessionManager"
 memcachedNodes="m1:10.0.0.150:11211,m2:10.0.0.151:11211"
 sticky="false"
 sessionBackupAsync="false"
 lockingMode="uriPattern:/path1|/path2"
 requestUriIgnorePattern=".*\.(ico|png|gif|jpg|css|js)$"
 transcoderFactoryClass="de.javakaffee.web.msm.serializer.kryo.KryoTranscoderFactory" />
```


### Redis实现Session共享

#### 基于MSM实现Session共享

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image48.png)

```shell
# 安装redis，并开发端口
apt install -y redis-server

# /etc/redis/redis.conf 里面的bind 127.0.0.1:6379注释掉

# 重启redis

#在/usr/local/tomcat/lib/下载jar包
wget https://repo1.maven.org/maven2/redis/clients/jedis/3.0.0/jedis-3.0.0.jar

# 在context.xml中添加
 <Manager className="de.javakaffee.web.msm.MemcachedBackupSessionManager"
 memcachedNodes="redis://10.0.0.181"
 sticky="false"
 sessionBackupAsync="false"
 lockingMode="uriPattern:/path1|/path2"
 requestUriIgnorePattern=".*\.(ico|png|gif|jpg|css|js)$"
 transcoderFactoryClass="de.javakaffee.web.msm.serializer.kryo.KryoTranscoderFactory" />
```



### Tomcat性能优化

#### CG垃圾收集器

当需要分配的内存空间不再使用的时候，JVM将调用垃圾回收机制来回收内存空间

在堆内存中如果创建的对象不再使用,仍占用着内存,此时即为垃圾.需要即使进行垃圾回收,从而释放内存空间给其它对象使用

其实不同的开发语言都有垃圾回收问题,C,C++需要程序员人为回收,造成开发难度大,容易出错等问题,但执行效率高,而JAVA和Python中不需要程序员进行人为的回收垃圾,而由JVM或相关程序自动回收垃圾,减轻程序员的开发难度,但可能会造成执行效率低下

堆内存里面经常创建、销毁对象，内存也是被使用、被释放。如果不妥善处理，一个使用频繁的进程，可能会出现虽然有足够的内存容量，但是无法分配出可用内存空间，因为没有连续成片的内存了，内存全是碎片化的空间

所以需要有合适的垃圾回收机制,确保正常释放不再使用的内存空间,还需要保证内存空间尽可能的保持一
定的连续



#### Garbage垃圾确定方法

- 引用计数：每一个堆内对象上都与一个私有引用计数器，记录着被引用的次数，引用计数清零，该对象所占用堆内存就可以被回收。循环引用的对象都无法将引用计数器清零，就无法清楚。

- 根搜索(可达)算法：Root Searching


#### 垃圾回收基本算法

<span style="font-weight:700">标记-清除Mark-Sweep</span>

分垃圾标记阶段和内存释放两个阶段

  - 标记阶段，找到所有可访问对象打个标记，清理阶段，遍历整个堆
  - 对未标记对象（即不再使用的对象）逐一进行清理

特点：算法简单，不会浪费内存空间，效率较高，但会形成内存碎片

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image49.png)
<span style="font-weight:700">标记-压缩（压实）Mark-Compact</span>

分垃圾标记阶段

- 标记阶段，找到所有可访问对象打个标记
- 内存清理阶段时，整理时将对象内存一端移动，整理后存活对象连续的集中在内存一端

特点：整理后的内存空间是连续的，有大段的连续内存可分配，没有内存碎片，缺点是内存整理过程有消耗，效率相对低下

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image50.png)

<span style="font-weight:700">复制Copying</span>

先将可用内存分为大小相同两块区域A和B，每次只用其中一块，比如A。当A用完后，则将A中存活的对象复制到B。复制到B的时候连续的使用内存，最后将A一次性清除干净

特点：好处是没有碎片，复制过程中保证对象使用连续空间，且一次性清除所有垃圾，所以即使对象很多，收回效率也很高，缺点是比较浪费内存，只能使用原来一般内存，因为内存对半划分


三种算法的特点与比较

- 效率：复制算法>标记清除算法> 标记压缩算法
- 内存整齐度：复制算法=标记压缩算法> 标记清除算法
- 内存利用率：标记压缩算法=标记清除算法>复制算法

#### 分代堆内存CG策略

堆内存分代: 将heap内存空间分为三个不同类别，年轻代，老年代，持久代

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image51.png)


<span style="font-weight:700">年轻代Young：Young Generation</span>
伊甸园eden: 只有一个，刚刚创建的对象
幸存(存活区)Servivor Space：有2个幸存区，一个是from区，一个是to区。大小相等，地位相同、可互换

<span style="font-weight:700">老年代Tenured：Old Generation</span>
 长时间存活对象

<span style="font-weight:700">永久代Tenured：Old Generation</span>

JDK1.7之前使用，即Method Area方法区，保存 JVM 自身的类和方法，存储 JAVA 运行时的环境信息，JDK1.8 后改名为 MetaSpace，此空间不存在垃圾回收，关闭JVM会释放此区域内存，此空间物理上不属于heap内存，但逻辑上存在于heap内存

<span style="font-weight:700">默认空间大小比例：</span>
默认JVM试图分配最大内存的总内存的1/4,初始化默认总内存为总内存的1/64,年青代中heap的1/3，老年代占2/3

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image52.png)

<span style="font-weight:700">规律：一般情况99%的对象都是临时对象</span>


### Tomcat监控与调优

#### status

status监控步骤

1. 配置用户及角色

```shell
#更改访问权限
#/tomcat/webapps/manager/META-INF/context.xml
#/tomcat/webapps/host-manager/META-INF/context.xml
# 在META-INF目录下的context.xml里将10网段加进去
<Valve className="org.apache.catalina.valves.RemoteAddrValve"
      allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1|10\.\d+\.\d+\.\d+" />

# 然后在conf/tomcat-users.xml里将用户密码的设置添加进去
<role rolename="manager-gui"/>
<user username="tomcat" password="123456" roles="manager-gui"/>

# role 说明
# manager-gui       
# manager-status    
# manager-script    
# manager-jmx       
以HTML 显示 status 页面
仅显示 status 页面
以文本显示 status 页面内容   
以 xml 显示页面内容 

# 重启服务
systemctl restart tomcat:

# host-manager
<role rolename="manager-gui"/>
<role rolename="admin-gui"/>
<user username="tomcat" password="123456" roles="manager-gui,admin-gui"/>
```

- 这里角色role相当于权限的概念
  - admin-gui角色
  - manager-gui角色

设置角色后就可以进入监控页
![alt text](D:\git_repository\cyber_security_learning\markdown_img\image93.png)




#### probe探针

1. 配置用户及角色
2. 配置好角色（manager-gui角色）后重启服务器
3. 进入监控页面

```shell
# 在GitHub上下载probe.war部署在服务器上
# PsiProbe 的 web.xml 文件可能在 WEB-INF 目录下。查找是否有 <security-constraint> 配置强制 HTTPS。,如果有，将其更改成NONE
如果存在 <transport-guarantee>CONFIDENTIAL</transport-guarantee>，需要修改为 NONE 或者删除相关配置。

修改 server.xml

删除或设置 redirectPort="0"
```

**application**

**查看资源请求情况详情**
![alt text](D:\git_repository\cyber_security_learning\markdown_img\image109.png)

**通过request插看**
![alt text](D:\git_repository\cyber_security_learning\markdown_img\image108.png)

**Session**
![alt text](D:\git_repository\cyber_security_learning\markdown_img\image110.png)


**线程池数据（连接数）**

- 根据下列指标即可看出线程池是否够用，是否需要增加线程池的线程数量
  ![alt text](D:\git_repository\cyber_security_learning\markdown_img\image94-1755239352854-1.png)

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image95.png)


**内存数据**

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image111.png)

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image96.png)

根据图表，内存一定是一上一下成锯齿状波动的，如果是一条横线就一定是出现问题了

因为存在垃圾回收机制，所以

- 锯齿状图形：表示垃圾回收机制正常工作，定期回收内存。
- 水平状态：可能指示垃圾回收未能有效释放内存，需关注内存管理
- 优化和监控：通过调整 JVM 参数、分析堆转储、持续监控和优化代码来改进垃圾回收和内存使用。

整体的优化过程基本是围绕着`通过调整JVM参数，去进行垃圾回收行为的优化，和通过分析堆转储找到内存泄漏和高内存使用的原因`

连接器

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image97.png)

重点关注类似点击率（每隔多少时间有多少请求数）和吞吐量

#### probe重点关注数据总结

- 请求数，分析是按个站点的请求内容比较多，如果出问题的话是哪个类引起的，这些都可以从下图看出，虽然运维看的不是特别明确但是开发是看的懂的，哪个类在消耗，开发自身应该很清楚
- ![alt text](D:\git_repository\cyber_security_learning\markdown_img\image98-1755239352854-3.png)
- 通过线程池数据分析线程数，看线程够不够用，如果线程用满了就即使去增大，防止出现排队，出现排队超时
- ![alt text](D:\git_repository\cyber_security_learning\markdown_img\image94-1755239352854-1.png)
- 观察内存中内存分布的情况（青年态，老年态）
  - （可以在catalina.sh的文件中指定内存的大小），后期根据实际情况去调整内存的分布,防止内存溢出和产生频发回收机制（比如年轻态过小，就会频繁出发回收，而频繁的GC会消耗系统资源）
    ![alt text](D:\git_repository\cyber_security_learning\markdown_img\image99-1755239352854-2.png)
  - 通过看系统资源的情况分析，比如由于内存过小，导致频繁出发GC，导致CPU使用率增高
  - JMP CPU UTILIZATION过高，就会导致CPU负载变高
  - FILE DESCRIPTIONS变高，又或者发生频繁的读取文件，频繁导致磁盘IO变高
    ![alt text](D:\git_repository\cyber_security_learning\markdown_img\image100-1755239352854-4.png)
- 观察（http）连接器里的点击率和吞吐量
  ![alt text](D:\git_repository\cyber_security_learning\markdown_img\image112-1755239352854-5.png)

### JVM调优

JVM当前有三家公司在开发分别是

- SUN（ORCLE）
- BEA
- IBM

#### JVM工作原理

```java
public class MyMath { 
    public static final int INIT_DATA = 666; 
    public static User user = new User();  

    public int compute() { // 一个方法对应一块栈帧内存区域
        int a = 1;
        int b = 2;
        int c = (a + b) * 10;
        return c;
    }

    public static void main(String[] args) {
        MyMath math = new MyMath(); 
        int result = math.compute(); 
        System.out.println("计算结果为: " + result); // 输出结果
    }
}

class User {
    private String name;

    public User() {
        this.name = "Default User";
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image116.png)

**java程序编译执行流程**

- 第一步：通过**javac**指令将Math.java变成字节码文件，在通过**java**命令去运行
- 第二步：执行java命令后，字节码文件加载到**类装载子系统**，通过类装载子系统将字节码加载到JVM的第二块组成部分（内存区域或运行时数据区）
- 第三步：通过JVM第三个组成部分：**字节码执行引擎**来执行内存区域里的代码

我们学的堆，栈，元空间等概念都仅仅指的是内存区域组成部分的一小块内容
我们的JVM调优，主要调的就是内存区域



**jVM内存区域详解**

- 堆（Heap）
  - 通常new的实例都在堆中

- 栈（Java Virtual Machine Stacks）
  - 也叫线程栈
  - 当我们的**main方法**开始运行，就会启用一个线程运行，而在线程运行过程中，局部变量需要有内存去存放，而这些局部变量都是放在线程栈
  - 只要有一个线程开始运行，JVM就会给这个线程分配一个**专属的**栈内存区域，用来放局部变量

  - **栈帧**
    - 当我们的线程开始运行，JVM就会给这个线程分配一块自己专属的线程栈
    - 而局部变量的作用范围通常只在方法内部有效，比如上述代码的中变量a，b，c，只在方法compute执行的过程中有效，
    - 而math只在main方法执行的过程中生效，方法一结束，这个局部变量肯定就没有了
      - 实现过程：
      - 只要我们的线程开始执行方法，马上会给这个方法在我们的线程栈内存区域分配一个块方法对应的内存区域，用来存放方法内部的局部变量
      - 当调用compute方法的时候，也会给这个方法分配一块自己内部的内存区域，我们把方法对应的这个内存区域就叫**栈帧**

  - **数据结构的栈和这个栈空间的关系是什么**
    - 栈的特点是FILO(First IN Last Out)
    - 我们的线程栈这块内存区放栈帧的这个数据结构，就是用的数据结构里的栈
    - 根据上述代码，我们的程序在运行过程中，他的内存分配如下  
      - 先是线程开始运行，分配一大块内存区域（线程栈）
      - 然后开始执行main方法，然后分配一块main方法的栈帧内存区域，然后执行compute方法，compute方法又会被分配一块栈帧内存区域
      - compute方法一旦运行完，它对应的栈帧局部内存空间全部都会被释放掉，也就是所谓的出栈
      - 然后在回到mian方法继续执行，main方法执行完，一样的也会把main方法对应的栈帧内存空间销毁掉，说白了就是出栈
    - 这也就是为什么要用栈这种数据结构来存储我们的方法，因为他跟我们程序的嵌套调用的先后顺序完全一致。

```java
// 通过javap -c MyMath > MyMath.txt，得到java字节码的反汇编
// 对上述代码生成的字节码进行反汇编
// 可以通过对照Orcle上面的JVM指令码手册，进行阅读
Compiled from "MyMath.java"
public class MyMath {
  public static final int INIT_DATA;

  public static User user;

  public MyMath();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public int compute();
    Code:
       0: iconst_1                         // iconst_1 将int类型常量1压入操作数栈，操作数栈内部也是栈结构来存储数据
       1: istore_1                         // 将int类型的值存入局部变量1，这里也就是将操作栈中的常量1出栈，然后给局部变量a开辟一个内存空间，然后将常量1存入局部变量a的内存空间中
       2: iconst_2                         // iconst_2 将int类型常量2压入操作数栈
       3: istore_2
       4: iload_1                          // iload 从局部变量中装载int类型值1
       5: iload_2
       6: iadd                             // iadd 从操作数栈中，弹出两个值，做加法，得到的结果，重新压回操作数栈
       7: bipush        10                 // bipush 将一个8位带符号整数(10)压入栈
       9: imul
      10: istore_3
      11: iload_3
      12: ireturn

  public static void main(java.lang.String[]);
    Code:
       0: new           #2                  // class MyMath
       3: dup
       4: invokespecial #3                  // Method "<init>":()V
       7: astore_1
       8: aload_1

```

  - **局部变量表与操作数栈**
    - 在我们的栈帧中，有一个表结构来存放我们的局部变量，也就是**局部变量表**
    - 整个栈帧中除了有**局部变量表**，**操作数栈**，**动态链接**，**方法出口**
    - **局部变量表**就是存放局部变量的数据存储结构
    - **操作数栈**临时存放局部变量值的地方
    - **程序计数器**每个线程从程序计数器的内存空间中，取一部分作为自己的程序计数器内存空间，内部存放的数据是记录我们的代码执行到什么位置（方法区的内存地址）
      - 程序计数器的意义: 为什么JVM的程序设计人员要设计它：当线程时间片用完，产生线程间切换的时候，该程序计数器记录线程运行的位置，在后续切换回来的时候使用
      - Math.class在java运行的时候，要将其加载到方法区（也就是元空间），加载到元空间后，由字节码执行引擎执行
      - 程序计数器上记录了代码执行的位置，而这个程序计数器的值由字节码执行引擎处理
    - **动态链接**：涉及C++底层源码，java程序是由C++写的，
      - 大概意思：我们的函数名，方法名，看做一个符号，比如compute就是一个符号，动态链接实质上就是程序在运行过程中，根据这个符号找到这个方法所在的方法区内的内存地址，根据这些内存地址作为入口，找到这个方法的代码进行执行
      - 所以动态链接放的就是我们的方法对应的在方法区内的解析之后的入口的内存地址，根据这个内存地址可以找到compute方法的具体代码
    - **方法出入口**：记录compute代码执行完后，返回到main方法的哪个位置
    - 每个栈帧都有上述的这四个部分，即：局部变量表，操作数栈，动态链接，方法出入口
    - **main方法内的局部变量表**：有些不同的地方：就是Math.math接受的值是一个对象( new Math() ),而这个对象是被分配在堆里的，而我们的局部变量比如：a=1是被分配在局部变量表中
    - 那么局部变量表中的变量和堆中的math对象有什么区别：也就是局部变量表中的数值是存放的常量，而对象则是存放的堆中存放该对象数据的地址，即指针
    - **方法区（元空间）**：方法区内放常量，静态变量，类元信息，
      - **常量**：`public static final int initData = 666;`
      - **静态变量**：`public static User user = new User();`，而这个变量的值是一个变量，因此也是一个指针指向堆内的user对象，这也就是方法区和堆之中的关系
      - **本地方法栈**：本地方法就是native方法，底层是C++写的，这部分native方法就是从本地方法栈分配的内存空间
        - 和线程栈比较类似，线程栈是java语言实现的方法，它的内存空间是从栈空间分配的
        - 对于本地方法（native方法），底层是C++/C语言实现的，而这些方法的内存空间从本地方法中分配


**堆**

- 对象new出来时放在Eden区，当我们不断new对象，将Eden区撑满，会触发minor GC，minor GC本质上是字节码执行引擎开启的一个线程，专门用来做垃圾对象回收，
- **GC底层垃圾回收的过程**：
  - **可达性分析算法**
    - 将"GC Roots"对象作为起点，从这些节点开始向下搜索引用的对象，找到的对象都标记为非垃圾对象，其余未标记的对象都是垃圾对象，
      - 比如：可以以math变量作为GC ROOT,看math变量有没有成员变量，如果有引用成员变量，继续向下找，直到找到最后一个对象，它没有任何引用的成员变量，整个链上的所有变量对打一个标记，记为非垃圾，而所有的非垃圾会复制到survivor上去，所有没有GC ROOT指向的对象，也就是垃圾对象，直接销毁掉
      - 一个对象在经历过GC后，他的分代年龄会加1，假设程序一直在运行，下一次，Eden区又放满了，会再次出发minor GC，minor GC实质上回收的是整个年轻代，它不仅会回收Eden区，还会回收Survivor区的对象，如果第二次回收，survivor区域中还有对象存活，它会被复制到另一块survivor区域，即s1区，如果eden区还有对象存活，也会复制到s1区，剩下的edne去和s0区里的所有对象直接清空，效率非常高
      - 对象的组成：对象中除了实例数据（比如：成员变量外），还有对象头（Object Header），包含对象的一些附属信息，比如：锁状态，数组长度（只有数组对象才有），分代年龄（用4bit存储）
      - 每经过一次minor GC，分代年龄都会加1，当分代年龄变为15后，直接移到老年代（这里的15不是绝对的，不同的垃圾回收器的值不同）
      - 在web应用中，向数据库连接池，对象缓存池，静态变量这些最终都会移到老年代
    - GC Roots根节点：线程栈的本地变量，静态变量，本地方法栈的变量等等

**总结：三种对象从青年代移动到老年代的原因**

- 对象的年龄超过阈值（默认15，具体看JVM实现）

  - 当对象在 Survivor 区的年龄超过了阈值，JVM 会将对象移动到老年代
  - 过程解释
    - 在年轻代中，内存划分为 Eden、Survivor from (S0) 和 Survivor to (S1) 三部分。
    - 新创建的对象首先分配在 Eden 区
    - 当 Eden 区内存满时，Minor GC 触发
    - 存活的对象将被移入 Survivor S0 区。
    - 在接下来的 GC 中，存活的对象会从 S0 → S1，它们的“年龄”会增加 1。
    - 当对象的年龄达到某个阈值 (默认为15)，JVM 就会将该对象移入老年代。
  - **年龄阈值**
    - JVM 中的对象年龄由 MaxTenuringThreshold 决定，默认值是15。
    - 也就是说，如果一个对象的年龄达到 15（在 S0/S1 之间存活了 15 次 GC），这个对象就会被移到老年代
  - **修改阈值**

  ```bash
  -XX:MaxTenuringThreshold=10
  # 将对象的“最大生存代数”调整为 10。也就是说，当对象在 Survivor 区经历了 10 次 GC 后，它就会被移入老年代。
  ```

- 对象的年龄超过阈值

  - 大对象（通常是大数组或大字符串）会直接分配到老年代，而不会经历年轻代的过程。
  - **为什么要直接进入老年代？**
    - 如果一个大对象（比如一个大数组或大字符串）被分配到 Eden 区，可能会很快填满 Eden 区，频繁触发 GC。这种频繁的 GC 会导致性能问题。为了解决这个问题，JVM 提供了一种机制，大对象直接进入老年代。
  - **如何定义大对象的大小？**
    - JVM 使用 `PretenureSizeThreshold` 参数来决定大对象的最小大小。
    - 只要对象的大小大于 PretenureSizeThreshold，它就会被直接分配到老年代。
  - **如何设置大对象的阈值？**

  ```bash
  # 表示大于 1MB 的对象将直接分配到老年代。
  -XX:PretenureSizeThreshold=1M
  ```

- 特殊情况：Survivor 区满了的情况

  - 如果 Survivor 区满了，存活的对象也会被直接送入老年代。
  - **为什么会发生？**
    - 在 GC 过程中，如果 Survivor 区中的空间不足以存放所有 Eden 和 Survivor 中存活的对象，那么一部分对象会直接被分配到老年代。
    - 这有点像应急转移的机制。
  - 这种情况在高并发场景中常见，比如网络高并发请求，瞬时大量对象创建导致 Survivor 区不够用。


**堆满时，老年代如何分配？**

- 当老年代也满了时，JVM 将触发 Full GC。
- Full GC 触发后，如果无法回收老年代中的对象，JVM 会抛出：

```bash
java.lang.OutOfMemoryError: Java heap space
```

### JVM调优工具

#### 使用jvisualvm监控内存

jvisualvm一款图形化的内存监控工具，在jdk-8u361之前的版本中是内置的组件，但在之后的JDK版本中已经取消了该组件，要单独下载并配置

```bash
# 安装依赖
apt install libxrender1 libxrender1 libxtst6 libxi6 fontconfig -y

wget https://github.com/oracle/visualvm/releases/download/2.1.8/visualvm_218.zip

unzip visualvm_218.zip

# 在windows中开启Xmanager - Passive
export DISPLAY=10.0.0.1:0.0

# 执行，在windows中能看到GUI界面，在GUI中点击Tools菜单，Plugins，然后安装VisualGC插件
```

**测试程序**

```java
// HeapOom.java
import java.util.ArrayList;
import java.util.List;
public class HeapOom {
    public static void main(String[] args) {
        List<byte[]> list = new ArrayList<byte[]>();
        int i = 0;
        boolean flag = true;
        while(flag) {
            try {
                i++;
                list.add(new byte[1024 * 1024]); // 每次增加一个1M大小的数组对象
                Thread.sleep(1000);
            } catch (Throwable e ) {
                e.printStackTrace();
                flag = false;
                System.out.println("count="+i); // 记录运行次数
            }
        }
    }
}
```

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image118.png)
![alt text](D:\git_repository\cyber_security_learning\markdown_img\image117.png)

老年代放满后，会触发**Full GC**，它会回收整个堆的内存空间，但是由于上述代码的对象一直在被列表引用，FUll GC无法回收，因此会触发OOM

```bash
java.lang.OutOfMemoryError: Java heap space
```

#### 阿里巴巴内部JVM调优工具Arthas详解

启动Demo

```bash
curl -o https://arthas.aliyun.com/arthas-boot.jar
java -jar arthas-demo.jar
```

**Arthas使用场景**
得益于Arthas强大且丰富的功能，让Arthas能做的事情超乎想象。下面仅仅例举几项常见的使用情况，更多的使用场景可以在熟悉了Arthas之后自行探索

- 是否有一个全局视角来查看系统的运行状况？
- 为什么CPU又升高了，到底是哪里占用了CPU？
- 运行的多线程有死锁吗？有阻塞吗？
- 程序运行耗时很长，是哪里耗时比较长呢？如何监测呢？
- 这个类从哪个jar包加载的？为什么会报各种类相关的Exception？
- 我改的代码为什么没有执行到？难道是我没commit?分支搞错了？
- 遇到问题无法在线上debug，难道只能通过加日志再重新发布吗？
- 有什么办法可以监控到JVM的实时运行状态？


![alt text](D:\git_repository\cyber_security_learning\markdown_img\image119.png)

**执行dashboard**

```bash
# 把当前的监控进程里面的所有的线程执行的情况，全部打出来，包括内存的分配情况
dashboard
```

![alt text](D:\git_repository\cyber_security_learning\markdown_img\image120.png)

**thread <线程号>**

```bash
# 定位这个线程占用CPU执行的具体的代码
thread 18
```

**更多的用法**：查看Arthas官网的更多详细高阶用法

#### JVM虚拟机调优的目的

尽可能的减少GC，不论是FULL GC还是MINOR GC，减少GC，特别是FULL GC的目的是尽量减少STW（Stop The World）
SWT一旦发生，在客户端的影响就是，用户会发现卡顿

**JVM的开发人员为什么要设计SWT机制**

使用反证法，假设JVM在做GC的过程中，不STW，没有STW机制，后台线程在做GC的过程中，同时用户线程也继续在执行，会发生什么效果

- 如果用户线程不暂停，程序一直在执行，则对象的状态会一直变，可能GC在或变量检查时，还不是垃圾对象，但是GC可能还没检测完，而程序线程运行外，导致之前的部分非垃圾对象变为垃圾对象，此时怎么办？GC重新遍历检测吗？
- 所以为了防止这个情况发生，就需要SWT机制，在GC触发时，暂停线程运行，直到GC结束
- 不同的垃圾收集器的SWT会有区别


#### 通过案例讲解JVM优化  

**亿级流量电商场景**
![alt text](D:\git_repository\cyber_security_learning\markdown_img\image121.png)




#### 堆和栈的区别

程序执行需要加载到内存，内存中分堆和栈的目的是将数据类型进行区分，`将不同的对象放到不同的内存中，用不同的数据结构去组织，已达到高效的目的 `

栈是运行单位，所有的运行对象，都是在栈中，当程序运行时，JVM会为每个线程分配一个栈大小。每个线程栈是不通用的，因为每个任务都有一个独立的线程执行。

堆是存储单位，所以有需要使用的数据都在堆中，堆是可以共享的。也就是说，堆是处理数据的地方，栈是用来处理逻辑的地方。

之所以区分堆和栈，这样的好处是可以将业务逻辑和数据进行分离，同时也可以提高数据的共享程度。


堆中有垃圾回收机制GC，因此要继续对堆内存进行划分

- 年轻代（Young Generation）
- 年老代（Old Generation）
- 持久代（Permanent Generation）
  - JDK8之后，不再叫持久代，而叫做元空间(metaspace)
  - 持久代在JVM的内存中，而元空间在本地内存中

#### JVM的三代（内存）

所谓的jVM的调优，本质上就是设置内存的使用

#### GC回收方法

- GC回收的是堆内的内存，主要对3代进行回收

Java中GC回收机制有两种，Scavenge GC和Full GC

- Scavenge GC回收机主要是对年轻代进行回收，或者说年轻代主要使用ScavengeGC来回收内存，年轻代分为一个edan区和两个Survivo区

- Scavenge GC首先是对edan区的对象进行回收，如果回收结束后还是存活对象，我们会将他放入Survivo区，由于edan区的对象变化很频繁，所以在年轻代中经常使用Scanvenge进行回收

- Full GC是指对整个堆内存的对象进行回收，对年轻代，老年代和持久代都会进行回收，但是堆Java8的版本已经没有持久代，被metaspace所替代。由于Full GC回收的内容比较多，所以一般不可能频繁触发Full GC回收
  - 年老代被写满
  - 持久代被写满
  - system.gc()被调用
  - 上一次GC后，heap分配的策略发生变化


#### GC的算法

引用计数、标记清除算法

- 对每个对象进行计数，如果对象引用一次，那么计数+1，如果这个引用释放那减1，如果计数为0，那么表示这个对象要消除

- 标记清除算法会不断扫描GC Roots，将存活的对象标记出来，等到不用的时候再清除

复制算法

将内存分为两份，每次只用一份，通过来回复制来解决碎片的问题


#### 垃圾收集的算法

通常GC回收的算法有三种，串行收集器，并行收集器，并发收集器

### JVM的参数设置

- 实际上是设置每个代的大小

#### 修改JVM参数的方法

修改JVM的方法通常有三种

- 使用eclipse进行设置
- 使用java小程序来设置
- 修改配置疑问还能来设置JVM
  - 使用bin/catalina.sh;
  - 修改bin/startup.sh

修改JVM的语法有三种

```shell
#第一种语法
set CATALINA_OPTS=-Xmx512m -Xms512m -Xmn64m -Xss2m

# 第二种语法
set JAVA_OPTS=-Xmx512 -Xms512 -Xmn64m -Xss2m

# 第三种
JAVA_OPTS="-Xms512 -Xmx1024m -Xmn512m"

# 堆相关参数
-Xms：        # 初始堆大小
-Xmx：        # 最大堆大小
# 初始堆大小一般会设置与最大堆大小一致，对于32位操作系统来说，-Xmx设置为1.5G-2.5G即可，如果是64位则一般不做限制
-XX:NewSize=n;    # 设置年轻代大小
-XX:MaxNewSize    # 设置新生代最大空间大小
-XX:NewRatio=n    # 设置年轻代和老年代的比值，如为3，代表年轻代与老年代的比例是1:3
-XX:SurvivorRatio=n;  # 如果值为3:2，表示Eden:Survive=3:2
-XX:MaxPermSize:n     # 设置持久代大小
-Xss: #设置每个线程的堆大小
```

metaspace参数设置

```shell
-XX:MetaspaceSize   # 初始空间大小，达到该值就会触发垃圾回收机制进行类卸载，同时GC会对该值进行调整，如果释放了大量的空间，就适当降低该值，如果释放了很少的空间，那么不超过MaxMetaspaceSize时，适当提高该值
-XX:MaxMetaspaceSize # 最大空间，默认没有上线
-XX:MinMetaSpaceFreeRatio  # 在GC之后，最小的Metasapce剩余的空间容量的百分比，减少为分配空间所导致的垃圾收集
-XX:MaxMetaspaceFreeRatio  # 在GC之后，最大的Metaspace剩余空间容量的百分比，减少为释放空间所导致的垃圾收集
```

并行收集器

```shell
-XX:ParallelGCThreads=n  # 设置并行收集器时使用的CPU数，并行收集线程数
-XX:MaxGCPauseMillis=n   # 设置并行收集最大暂停时间
-XX:GCTimeRatio=n        # 设置垃圾回收时间占程序运行时间的百分比，公式为1/(1+n)
```

并发收集器

```shell
-XX:+CMSIncrementalMode  #设置为增量模式，适用于单CPU
-XX:ParallelGCTreads=n   # 设置并发收集器年轻代收集方式为并行收集时，使用的CPU数，
```

### 连接器

Http连接器

AJP连接器

#### 问题：jpress的验证码无法识别

问题出现的原因：Java 图形处理功能在 Linux 系统上找不到有效的字体配置时会发生。

解决方案

```shell
# 1. 安装基础字体和字体配置包
# ubuntu
sudo apt-get update
sudo apt-get install -y fontconfig ttf-mscorefonts-installer
# CentOS
sudo yum install -y fontconfig dejavu-sans-fonts
# 重建字体缓存
sudo fc-cache -fv

# 2. 检查并配置字体路径(这个的可能性比较大)
# 将这个变量赋值写入.bashrc或者catalina.sh
export JAVA_FONTS=/usr/share/fonts

# 3. 验证字体配置
# 查看这些文件配置是否完整，尤其是/etc/fonts/font.conf
ls /etc/fonts
ls /etc/fonts/conf.d/

# 如果依然解决不了
#  安装或更新 JDK
# ubuntu
sudo apt-get install -y openjdk-11-jdk
# centos
sudo yum install -y java-11-openjdk-devel

# 设置默认 Java 版本
#使用 update-alternatives 设置默认的 Java 版本：
sudo update-alternatives --config java

# 使用脚本验证是否成功
```

图形验证脚本TestFont.java

```java
import java.awt.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;

public class TestFont {
    public static void main(String[] args) {
        int width = 150, height = 50;
        BufferedImage bufferedImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);

        Graphics g = bufferedImage.getGraphics();
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, width, height);
        g.setColor(Color.BLACK);
        g.setFont(new Font("Arial", Font.BOLD, 40));
        g.drawString("Test", 20, 40);

        try {
            ImageIO.write(bufferedImage, "png", new File("testfont.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

测试

```shell
javac TestFont.java
java TestFont
```

