# HTTP/1.1协议
## Web浏览器发起HTTP请求得典型场景
![Alt text](images/image01.png)
- 详解过程
  - 首先服务器监听打开了443或者80端口
  - 浏览器从url中解析出域名
  - 根据域名查询DNS，获取域名对应得IP地址
  - 浏览器根据ip地址，和服务器三次握手建立TCP链接，https会额外完成TLS/SSL的握手
  - 构造HTTP请求，在构造请求的过程中，填充相应的HTTP头部，包括上下文所需要的信息，至头部中
  - 通过链接发起HTTP请求
  - 服务器接收到HTTP请求后，完成资源的表述，把客户端请求的文件如html页面作为包体返回给浏览器
  - 浏览器在渲染引擎中解析响应，根据这个响应中一些其他的超链接资源去构造其他HTTP请求

- Hypertext Transfer Protocol(HTTP)协议
![Alt text](images/image02.png)

- a `stateless` application-level `request/response` protocol that uses `extensible semantics` and `self-descriptive` message payloads for flexibale interaction with network-based `hypertext information` systems
(https://tools.ietf.org/html/rfc7230)

- 推荐书籍
  - 《HTTPS权威指南》
  - 《TCP/IP协议详解》

- RFC文档是对所有协议的最权威的定义  

## 基于ABNF语义定义的HTTP消息格式

- 使用的理由
  - 根据ABNF语义描述的HTTP是最为严谨的，可以避免工作中的很多问题
- HTTP协议格式
  - start-line
    - request-line
    - status-line
  - header
    - header-field1
    - header-field2
    - ...
  - message-body

![Alt text](images/image17.png)

- ABNF——一种定义语法的元语言，可以防止不同服务器在处理http数据的时候，出现基于具有格式问题导致的解析解结果不同，比如空格和制表符或者其他空白符，短横线和下滑线等等一系列由于不规范导致的问题

- ABNF——常用于定义协议语法

- ABNF (扩充巴克斯-瑙尔范式) 操作符
  - 包含两部分
    - 操作符
    - 核心语法规则
  - 操作符
    - 空白字符: 用来分隔定义中的各个元素
      - 例：`method SP request-target SP HTTP-version CRLF`
    - 选择/: 表示多条规则都是可供选择的规则
      - 例：`start-line = request-line/status-line`
    - 值范围 `%c##-##`
      - 例：`OCTAL = "0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"` 与 `%x30-37` 等价（十六进制30-37对照ascll码，即字符0-7）
    - 序列组合(): 将规则组合起来，视为单个元素
    - 不定量重复m*n：
      - `*` 元素表示零个或更多元素：*(header-field CRLF)
      - `1*` 元素一个或更多元素
      - `2*4` 表示两个至四个元素
    - 可选序列[]
      - [message-body]
  - 核心规则
  ![Alt text](images/image18.png)

- 基于ABNF描述的HTTP协议格式
```shell
# HTTP完整格式
HTTP-message = start-line*(hearder-field CRLF)CRLF[message-body]
# 详细解读
  start-line = request-line/status-line
    request-line = method SP request-target SP HTTP-version CRLF
    status-line = HTTP-version SP status-code SP reason-phrase CRLF
  header-field = field-name ":" OWS field-valus OWS
    OWS = *(SP / HTAB)
    field-name = token
    field-value = *(field-content/obs-fold)
  message-body = *OCTET
```
- 可以通过telnet进行对指定网站发送请求，收到响应值
  - 响应信息无法观看隐藏字符，隐藏字符可以通过wireshark进行观测
  ```shell
  [root@ubuntu2204 ~]#telnet www.feng.org 80
  Trying 10.0.0.200...
  Connected to www.feng.org.
  Escape character is '^]'.
  GET / HTTP/1.1
  Host: www.feng.org

  HTTP/1.1 200 OK
  Server: nginx/1.18.0 (Ubuntu)
  Date: Sun, 23 Jun 2024 04:06:22 GMT
  Content-Type: text/html
  Content-Length: 26
  Last-Modified: Sun, 23 Jun 2024 04:00:08 GMT
  Connection: keep-alive
  ETag: "66779dc8-1a"
  Accept-Ranges: bytes

  i'm test-10.0.0.200-index
  ```

![alt text](th_images/image1.png)

### ABNF（Augmented BNF）官方文档的学习
- <a href="./ABNF_ietf.org_rfc_rfc5234.txt">官方文档原文</a>
- 上面的ABNF总结其实够用，下方少许补充信息，
- 学习总结：
  - 规则形式：`name = elements crlf`
    - name: the name of the rule
    - elements: one or more rule names or terminal specifications/values
    - crlf: the end-of-line indicator (carriage return followed by line feed)
  - Terminal Values
    - Rules resolve into a string of terminal values, sometimes called characters. 
    - 在 ABNF 中，字符仅仅是一个非负整数。   在某些上下文中，将指定值到字符集（例如 ASCII）的特定映射（编码） 。   终端由一个或多个数字字符指定，并   明确指示这些字符的基本解释。
      - b = 二进制
      - d = 十进制
      - x = 十六进制
      - 实例(映射ASCLL码)：
        - CR = %d13
        - CR = %xOD (两个值在ascll码中都表示回车)
    - 使用句点`.`来表示该值内的字符分隔
      - 例如；`rulename = %d97 %d98 %d99` 等同于 `rulename = %97.98.99`
        - CRLF = %d13.10 等同于 CRLF = %d13 %d10
        - 只有在单独指定字符时，如上案例才区分大小写
    - ABNF 允许直接指定文本字符串，并且用引号括起来
      - 格式：`command = "command string"`
      - 例如：`rulename = "abc"` 且等同于 `rulename = "aBC"...`
      - 注意：
        - ABNF字符串不区分大小写
        - 这些字符串的字符集是US-ASCII
  - 运算符
    - 连接：规则1 规则2
      - 可以通过列出规则名称序列来定义简单、有序的值字符串（即连续字符的拼接）
    ```python
    foo = %x61 # a
    bar = %x62 # b
    mumber = foo bar foo
    # 等于mumber = "aba"
    ```
    - 替代：规则1 / 规则2
      - `mumber = foo / bar` 表示 `mumber = foo 或 mumber = bar`
    - 值范围：`%c##-##`
      - 例：`OCTAL = "0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"` 与 `%x30-37` 等价（十六进制30-37对照ascll码，即字符0-7）
    - 序列组：将规则组合起来，视为单个元素，其内容严格排序
    ```python
    elem (foo / bar) blat
    # 等同于：匹配elem foo blat 或 elem bar blat
    elem foo /bar blat
    # 匹配 elem foo 或 elem bar blat
    ```

## HTTP解决了什么问题
- HTTP/1.1 创始人：Roy Thomas Fielding
  - 参与制订HTTP/1.0规范 (1996.5)
  - 参与制订URI规范 (1998.8)
  - 主导制订HTTP/1.1规范 (1999.6)
  - 2000年发布指导HTTP/1.1规范制订的论文
    - 《Architectural Style and the Design of Network-based Software Architectures》即我们常谈的Representational State Transfer(REST)架构
  - Apache基金会 (The Apache Software Foundation) 共同创始人
    - 参与开发Apache httpd服务 

- Form Follws Function (形式一定是为功能服务的)
```shell
GET / HTTP/1.1
Host: developer.mozilla.org
Accept-Language: fr
# 思考：http报文，为什么是这种形式
```

- 万维网创始人：Tim Berners Lee
  - Web's major goal was to be a shared information space through which people and machines could communicate.

- 解决www信息交互必须面对的需求
  - 低门槛
  - 可扩展性：巨大的用户群体，超长的寿命
  - 分布式系统下的Hypermedia：大粒度数据的网络传输
  - Internet模式
    - 无法控制的scalability(可扩展性)
      - 不可预测的负载、非法格式的数据、恶意消息
      - 客户端不能保持所有服务器信息，服务器不能保持多个请求间的状态信息
    - 独立的组件部署：新老组件并存
  - 向前兼容：自1993年起HTTP0.9/1.0（1996）已经被广泛使用

## 评估Web架构的七大关键属性
- HTTP协议应当在以下属性中取得可接受的均衡：
  - 性能performance：影响高可用的关键因素
  - 可伸缩性Scalability：支持部署可以相互交互的大量组件
  - 简单性Simplicity：易理解、易实现、易验证(一个复杂的设计通常不是最好的解决方案)
  - 可见性Visiable：对两个组件间的交互进行监视或者仲裁的能力。如缓存、分层设计等
  - 可移植性Portability：在不同的环境下运行的能力
  - 可靠性Reliability：出现部分故障时，对整体影响的程度
  - 可修改性Modifiability：对系统做出修改的难以程度，由可进化性、可定制性、可扩展性、可配置性、可重用性构成

### 性能
- 网络性能 Network Performance
  - Throughput吞吐量：小于等于带宽Bandwidth(高并发下，每秒处理的请求数等)
  - Overhead开销：首次开销，每次开销
    - 比如：http建立长连接，首次连接会有三次握手的开销，后续的开销就会比较小，而在http2.0，后续开销还会少传一些http头部，因为2.0中的后续每次开销可以复用首次开销中传递过的http的头部
- 用户感知到的性能 User-perceived Performance
  - Latency延迟：发起请求到接收到响应的时间
  - Completion完成时间：完成一个应用动作所花费的时间
- 网络效率 Network Efficiency
  - 重用缓存、减少交互次数、数据传输距离更近(CDN)、COD(按需代码)

### 可修改性
- 可进化型Evolvability：一个组件独立升级而不影响其他组件
- 可扩展性Extensibility：向系统添加功能，而不会影响到系统的其他部分
  - (比如TLS的加入，并不影响不使用TLS加密的http网站的使用，这就是可扩展性)
- 可定制性Customizability：临时性、定制性地更改某一要素来提供服务，不对常规客户产生影响
- 可配置性Configurability：应用部署后可通过修改配置提供新的功能
- 可重用性Reusability：组件可以不做修改在其他应用上使用
  - 比如：浏览器渲染引擎，可以在多个浏览器IE,chrome使用，这就是可重用性的体现

## 从五种架构风格推导出HTTP的REST架构
### 5种架构风格
- 导论：核心章节，难度过大，后面再进行详细的说明和补充
- 数据流风格 Data-flow Styles
  - 优点：简单性、可进化性、可扩展性、可配置性、可重用性
- 复制风格 Replication Styles
  - 优点：用户可察觉的性能、可伸缩性、网络效率、可靠性也可以得到提升
- 分层风格 Hierarchical Styles
  - 优点：简单性、可进化性、可伸缩性
- 移动代码风格 Mobile Code Styles
  - 优点：可移植性、可扩展性、网络效率
- 点对点风格：Peer-to-Peer Styles
  - 优点：可进化型、可重用性、可扩展性、可配置性

#### 数据流风格 Data-flow Style
- 管道与过滤器Pipe And Filter,PF
  - 每个Filter都有输入和输出端，只能从输入端读取数据，处理后再从输出端产生数据
  - 比如：协议：tcp->ip->数据链路层协议... 是一个单向的，
- 统一接口的管道与过滤器(Uniform Pipe And Filter,UPF)
  - 在PF上增加了同一接口的约束，所有Filter过滤器必须具备同样的接口

#### 复制风格 Replicated Repository,RR
- 多个进程提供相同的服务，通过反向代理对外提供集中服务
  - 比如：mysql的主从备份，Web集群等

- 缓存 $
  - RR的变体，通过复制请求的结果，为后续请求复用

#### 分层风格 Hierarchical Styles
- 客户端服务器 Client-Server, CS
  - 由Client触发请求，Server监听到请求后产生响应，Client一直等待收到响应后，会话结束
  - 分离关注点隐藏细节，良好的简单性，可伸缩性，可进化性
    - 分离关注点解读：Server只关注资源响应的深层，资源的管理，Client关注网路结果，可视化渲染,无论是客户端还是服务端都向对方隐藏了各自的细节，因此简单性比较好

- 分层系统 Layered System,LS
  - 每层为其之上的层服务，并使用在其之下的层所提供的服务，例如TCP/IP

- 分层客户端服务器架构Layered Client-Server,LCS
  - LS+CS，例如正常代理，反向代理，从空间上分为外部和内部

- 无状态，客户端服务器Client-Stateless-Server,CSS
  - 基于CS，服务器上不允许有session state会话状态
  - 提升了可见性，可伸缩性，可靠性，但重复数据会降低网络性能

- 缓存，无状态，客户端服务器（Client-Stateless-Server CSS）C$SS
 - 提性能

- 分层、缓存、无状态、客户端服务器Layered-Client-Cache-Stateless-Server, LC$SSo

- 远程会话 Remote Session,RS
  - CS变体，服务器保存Application state应用状态
  - 可伸缩性，可见性差

- 远程数据访问 Remote Date Access，RDA
  - CS变体，Application State应用状态同时分布在客户端和服务端
  - 巨大的数据集有可能通过迭代而减少
  - 简单小，可伸缩性差

#### 移动代码风格 Mobile Code Styles
- 虚拟机Virtual Machine VM
  - 分离指令与实现

- 远程求值Remote Evaluation,REV
  - 基于CS的VM，将代码发送至服务器执行

- 按需代码Code on Demand, COD
  - 服务器在响应中发回处理代码，在客户端执行(js,javascript)
  - 优秀的可扩展性和可配置型，提成用户察觉性能和网络效率

- 分层，需要带代码，缓存，无状态，客户端服务器
  - LCODC$SS: Layered-Code-on-Demand-Client-Cache-Stateless-Server
  - LC$SS + COD

- 移动代理Mobile Agent, MA
  - 相当于REV+COD

#### 点对点风格Peer-to-Peer Style
- Event-based Intergration EBI
  - 基于事件集成系统，类似kafka这样的消息系统+分发订阅来消除耦合
  - 优秀的可重用性，可扩展性，可进化性
  - 缺乏可理解性
  - 由于消息广播等因素造成的消息风暴，可伸缩性差

- Chiron-2 C2
  - 相当于EBI+LCS，控制了消息的方向

- Distributed Object，DO
  - 组件结对交互

- Brokered Distrubuted Object BDO
  - 引入名字解析组件，来简化DO，例如CORBA

## Chrome抓包，快速定位HTTP协议问题
- 快捷键：Contorl + Shift + I

### Chrome抓包：Network面板
- 控制器：控制面板的外观和功能
- 过滤器：过滤请求列表中显示的资源
  - 按ctrl，然后点击过滤器可以同时选择多个过滤器
- 概览：显示HTTP请求，响应时间轴
- 请求列表：默认时间排序，可选择显示列
- 概要：请求总数，总数据量，总花费时间

### 过滤器
- domain: 仅显示来自指定域的资源。你可以使用通配符(*)纳入多个域
- has-response-header: 显示包含指定HTTP响应标头的资源
- is：
  - `is: running`可以查找WebSocket资源，
  - `is:from-cache`可以查找缓存读出的资源
- larger-than: 显示`大于`指定大小的资源(以字节为单位)。
- method: 显示通过指定HTTP方法类型检索的资源
- mime-type: 显示指定MIME类型资源
- mixed-content: 显示所有混合内容资源（mixed-content:all），或者仅显示当前显示的资源（mixed-content:displayed）
- scheme: 显示通过未保护HTTP（scheme:http）或受保护HTTPS(scheme:https)检索的资源
- set-cookie-domain: 显示具有Set-Cookie标头并且Domain属性与指定值匹配的资源
- set-cookie-name: 显示具有set-cookie标头并且名称与指定值匹配的资源
- set-cookie-value: 显示具有set-cookie标头并且值与指定值匹配的资源
- status-code: 仅显示HTTP状态代码与指定代码匹配的资源

- tip: 想要过滤多个条件，各个条件间用空格隔开(and操作)


### 请求列表的排序
- 时间排序，默认
- 按列排序
- 按活动时间排序（右键->Waterfall->..）
  - Start Time：发出的第一个请求位于顶部
  - Response Time: 开始下载的第一个请求位于顶部
  - End Time: 完成的第一个请求位于顶部
  - Total Duration: 连接设置时间和请求/响应时间最短的请求位于顶部
  - Latency：等待最短响应时间的请求位于顶部 

### 预览请求内容
- 查看头部
- 查看cookie
- 预览响应正文，查看图像用
- 查看响应正文
- 时间详细分布
- 导出数据为HAR格式
- 查看请求上下游：按住`shift`键悬停请求上，绿色是上游，红色是下游

### 浏览器加载时间
- 触发流程
  - 解析HTML结构
  - 加载外部脚本和样式表文件
  - 解析并执行脚本代码 //部分脚本会阻塞页面加载
  - DOM树构建完成 // DOMContentLoaded事件
  - 加载图片等外部文件
  - 页面记载完毕 // load事件

### 请求时间详情分布
![alt text](th_images/image2.png)

- Queueing: 浏览器在以下情况下对请求排队
  - 存在更高优先级的请求
  - 此源已打开六个TCP连接，达到限值，仅适用HTTP/1.0和HTTP/1.1
  - 浏览器正在短暂分配磁盘缓存中的空间
- Stalled：请求可能会因Queueing中描述的任何原因而停止
- DNS Lookup：浏览器正在解析请求的IP地址
- Proxy Negotiation：浏览器正在与代理服务器协商请求
- Request sent：正在发送请求
- ServiceWorker Preparation: 浏览器正在启动Service Worker（真正负责网络相关的进程）
- Request to ServiceWorker：正在将请求发送到Service Worker
- Waiting（TTFB）：浏览器正在等待响应的第一个字节。TTFB表示Time To First Byte（至第一字节的时间）。此时间包括1次往返延迟时间及服务器准备响应所用的时间
- Content Download：浏览器正在接受响应
- Receiving Push：浏览器正在通过HTTP/2服务器推送接收此响应的数据
- Reading Push：浏览器正在读取之前收到的本地数据


## URL和URI的区别
### 什么是URI
- URL: RFC1738 (1994.12) , Uniform Resource Locator
  - 标识资源的位置，期望提供查找资源的方法

- URN: RFC2141 (1997.5) , Uniform Resource Name
  - 期望为资源提供持久的、位置无关的标识方式，并允许简单地将多个命名空间映射到单个URN命名空间
  - 例如：磁力链接 magnet:?xt=urn:sha1:YNCKHTQC5C

- URI: RFC1630 (1994.6)、RFC3986 (2005.1，取代RFC2396和RFC2732) ，Uniform Resource Identifier
  - 用以区分资源，是URL和URN的超集，用以取代URL和URN概念

- Uniform Resource Identifier URI统一资源标识符的定义
  - Resource 资源
    - 可以是图片、文档、今天杭州的温度（信息数据）等，也可以是不能通过互联网访问的实体，例如人、公司、实体书、也可以是抽象的概念，例如亲属关系或者数学符号
    - 一个资源可以有多个URI
  - Identifier 标识符
    - 将当前资源与其他资源区分开的名称
  - Uniform 统一
    - 允许不同种类的资源在同一上下文中出现
    - 对不同种类的资源标识符可以使用同一种语义进行解读
    - 引用新标识符时，不会对已有标识符产生影响
    - 允许同一资源标识符在不同的、Internet规模下的上下文中出现

- URI的组成
  - 组成：schema, user information, host, post, path, query, fragment
  ![Alt text](images/image19.png)
  - eg: https://tools.ietf.org/html/rfc7231?test=1#page-7

- URI格式
```shell
URI = scheme ":" hier-part ["?" query] ["#" fragment]
scheme = ALPHA *(ALPHA/DIGIT/"+"/"-"/".")
# 例如：http, https, ftp, mailto, rtsp, file, telnet
query = *(pchar/"/"/"?")
fragment = *(pchar/"/"/"?")

# 示例：https://tools.ietf.org/html/rfc7231?test=1#page-7

hier-part = "//" authority path-abempty/path-absolute/path-rooless/path-empty
  authority = [userinfo "@"] host [":" port]
  host = IP-Literal/IPv4address/reg-name
  port = *DIGIT

# 示例：https://tom:pass@localhost:8080/index.html

path = path=abempty/path-absolue/path-noscheme/path-rootless/path-empty
  path-abempty = *("/"segment)
  # 以/开头的路径或者空路径
  path-absolute = "/" [segment-nz*("/"segment)]
  # 以/开头的路径，但不能以//开头
  path-noscheme = segment-nz-nc*("/"segment)
  # 以非:号开头的路径
  path-rootless = segment-nz*("/"segment)
  # 相对path-noscheme，增加允许以:号开头的路径
  path-empty = 0<pchar>
  # 空路径
```
- 相对URI
```shell
URI-reference = URI/relative-ref
relative-ref = relative-part ["?" query] ["#" fragment]
  relative-part = "//" authority path-abempty/path-absolute/path-noscheme/path-empty

# 示例：https://tools.ietf.org/html/rfc7231?test=1#page-7
# 相对URI：/html/rfc7231?test=1#page-7
```

## URI编码
- URI编码的原因
  - 传递数据中，存在用作分隔符的保留字符
    - 例如：http://www.baidu.com/s?wd=?#! (这里?和#都是分隔符，直接搜索会出现问题)
  - 对可能产生歧义性的数据编码
    - 不在ASCII码范围内的字符
    - ASCII码中不可显示的字符
    - URI中规定的保留字符
    - 不安全字符(传输环节中可能会被不正确处理)，如空格、引号、尖括号等

- URI百分号编码
  - pct-encoded = "%" HEXDIG HEXDIG
    - US_ASCII: 128个字符（95个可显示字符，33个不可显示字符）
    - 参见：http://zh.wikipedia.org/wiki/ASCII
  - 对于HEXDIG十六进制中的字母，大小写等价

- 非ASCII码字符（例如中文）：建议先UTF8编码，再US-ASCII编码
- 对URI合法字符，编码与不编码是等价的
  - 例如："URI转换"既可以"URI%e8%bd%ac%e6%8d%a",也可以"%55%52%49%e8%bd%ac%e6%8d%a"

## 详解HTTP请求行
- 请求行：`request-line = method SP request-target SP HTTP-version CRLF`

- request-target = origin-form/absolute-form/authority-form/asterisk-form
  - origin-form = absolute-path ["?" query]
    - 向origin server发起的请求，path为空时必须传递/
  - absolute-form = absolute-URI
    - 仅用于正向代理proxy发起请求时，详见正向代理与隧道 
  - authority-form = authority
    - 仅用于CONNECT方法，例如CONNECT www.example.com:80 HTTP/1.1
    - 通常建立隧道的时候使用
  - asterisk-form:"*" 
    - 仅用于OPTIONS方法


- HTTP-version
  - 版本号发展历史：https://www.w3.org/Protocols/History.html
    - HTTP/0.9：只支持GET方法，过时
    - HTTP/1.0：RFC1945，1996，常见使用与代理服务器（例如Nginx默认配置）
    - HTTP/1.1：RFC2616，1999
    - HTTP/2.0：2015.5正式发布


- Method常见方法
  - GET：主要的获取信息方法，大量的性能优化都针对该方法，幂等方法
    - 幂等方法：在 HTTP/1.1 协议中，当我们说某个方法是幂等的，我们是指多次执行该方法对资源产生的效果与执行一次是相同的。这意味着客户端可以安全地多次重复同一请求，而不必担心导致不同的效果或产生意外的副作用。
    - 幂等方法的实际应用场景：
      - 例如，如果一个客户端发送了一个 DELETE 请求，但没有收到响应（可能因为网络问题），则由于 DELETE 是幂等的，客户端可以安全地重发该请求，知道这不会产生意外的副作用。
  - HEAD：类似GET方法，但服务器不发送BODY，用以获取HEAD元数据，幂等方法
  - POST：常用于提交HTML FORM表单，新增资源等
  - PUT：更新资源，带条件时是幂等方法
  - DELECT：删除资源，幂等方法
  - CONNECT：建立tunnel隧道
  - OPTIONS：显示服务器对访问资源支持的方法，幂等方法
  - TRACE：回显服务器收到的请求，用于定位问题，有安全风险，已被Nignx弃用

- 用于文档管理的WEBDAV方法
  - PROPFIND：从Web资源中，检索以XML格式存储的属性。它也被重载，以允许一个检索远程系统的集合结构（也叫目录层次结构）
  - PROPPATCH：在单个原子性动作中更改和删除资源的多个属性
  - MKCOL：创建集合或目录
  - COPY：将资源从一个URI复制到另一个URI
  - MOVE：将资源从一个URI移动到另一个URI
  - LOCK：锁定一个资源。WebDAV支持共享锁和互斥锁
  - UNLOCK：解除资源锁定

## HTTP的正确响应码
- HTTP响应行
```shell
status-line = HTTP-version SP status-code SP reason-phrase CRLF
  status-code = 3DIGIT
  reason-phrase = *(HTAB/SP/VCHAR/obs-text)
```

- 响应码分类
  - 1XX（请求已接受到，需要进一步处理才能完成，HTTP1.0不支持）
    - 100 Continue：上传大文件前使用
      - 客户端在上传一个大文件前，先告诉服务器，让服务器做好准备
      - 比如：迅雷
      - 有客户端发起请求中携带Expect：100-continue头部触发
    - 101 Switch Protocols：协议升级使用
      - 由客户端发起请求中携带Upgrade：头部触发，如升级websocket 或者 http/2.0
    - 102 Processing：WebDAV请求可能包含许多涉及文件操作的子请求，需要长时间才能完成请求。该代码表示服务器已经收到并正在处理请求，但无响应可用。这样可以防止客户端超时，并假设请求丢包

  - 2XX（成功处理请求）
    - 200 OK：成功返回响应
    - 201 Created：有新资源在服务器端被成功创建, 通常是上传了一个新的文件，很多PUT请求是201
    - 202 Accepted：服务器接收并开始处理请求，但请求未处理完成。这样一个模糊的概念是有意如此设计的，可以覆盖更多的场景。例如：异步，需要长时间处理的任务, 常用于RESTfulAPI的设计
    - 203 Non-Authoritative Information：当代理服务器修改了origin server的原始响应包体时（例如更换了HTML中的元素值）代理服务器可以通过修改200为203的方式告知客户端这一事实，方便客户端为这一行为做出相应的处理。203相应可以被缓存
      - 很多的代理服务器并不支持这个203规范
    - 204 No Content：成功执行了请求且不携带响应包体，并暗示客户端无需更新当前的页面视图
    - 205 Reset Content：成功执行了请求且不携带响应包体，并指名客户端需要更新当前页面视图
    - 206 Partial Content：使用range协议时返回部分响应内容时的响应码
    - 207 Multi-Status：RFC4918，在WEBDAV协议中以XML返回多个资源的状态
    - 208 Already Reported：RFC5842，为避免相同集合下资源在207响应码下重复上报，使用208可以使用父集合的响应码

- 3XX（重定向）
  - 简介：重定向使用Location执行的资源或者缓存中的资源。在RFC2068中规定客户端重定向次数不应超过5次，以防止死循环
  - 300 Multiple Choices：资源有多种表述，通过300返回给客户端后由其自行选择访问哪一种表述。由于缺乏明确的细节，300很少使用
  - 301 Moved Permanently：资源永久性的重定向到另一个URI中
    - 浏览器一般会对永久性的重定向直接缓存
  - 302 Found：资源临时重定向到另一个URI中
  - 303 See Other：重定向到其他资源，常用于Post/Put等方法的响应中
  - 304 Not Modified：当客户端拥有可能过期的缓存时，会携带缓存的标识etag、时间等信息询问服务器缓存是否仍可复用，而304是告诉客户端可以复用缓存
  - 307 Temporary Redirect：类似302，但明确定向后请求方法必须与原请求方法相同，不能改变
  - 308 Permanent Redirect: 类似301，但明确重定向后请求方法必须与原请求方法相同，不得改变

## HTTP的错误响应码
- 4XX：客户端出现错误
  - 400 Bad Request：服务器认为客户端出现了错误，但不能明确判断为以下哪种错误时，使用此错误码。例如HTTP请求格式错误
```shell
mystical@mystical ~ % telnet www.baidu.com 80
Trying 110.242.68.3...
Connected to www.a.shifen.com.
Escape character is '^]'.
GET / reqwrwq  # 故意构造一个不合法的GET请求，从而得到400的响应码
HTTP/1.1 400 Bad Request
```
  - 401 Unauthorized：用户认证信息缺失或者不正确，导致服务器无法处理请求
  - 407 Proxy Authentication Required：对需要经由代理的请求，认证信息未通过代理服务器的验证
  - 403 Forbidden：服务器理解请求的含义，但没有权限执行此请求, 访问服务器中的某个资源，但是没有权限
  - 404 Not Found：服务器没有找到对应的资源
  - 410 Gone：服务器没有找到对应的资源，且明确的知道该位置永久性找不到该资源
  - 405 Method Not Allowed: 服务器不支持请求行中的method方法, 比如Trace方法
  - 406 Not Acceptable：对客户端指定的资源表述不存在（例如对语言或编码有要求），服务器返回表述列表供客户端选择
  - 408 Request Timeout：服务器接收请求超时
  - 409 Conflict：资源冲突，例如上传文件时目标位置已经存在版本更新的资源
  - 411 Length Required：如果请求含有包体且未携带Content-Length头部，且不属于chunk类请求时，返回411
  - 412 Precondition Failed：复用缓存时传递的If-Unmodified-Since或If-None-Match头部不被满足
  - 413 Payload Too Large/Request Entity Too Large：请求的包体超出服务器能处理的最大长度
    - 比如搭建WordPress博客，要求上传附件不超过2M，如果不调整的话，在上传大附件的时候就会触发该错误
  - 414 URI Too Long：请求的URI超出服务器能接受的最大长度
  - 415 Unsupported Media Type：上传的文件类型不被服务器支持
  - 416 Range Not Satisfiable：无法提供Range请求中指定的那段包体
  - 417 Expectation Failed：对于Expect请求头部期待的情况无法满足时的响应码
    - 比如：100状态码，是上传一个超大文件，告诉服务器做好准备，但服务器本身无法满足接收这个超大文件的时候，就会返回这个状态码
  - 421 Misdirected Request：服务器认为这个请求不该发给它，因为它没有能力处理
    - 几乎很少出现
  - 426 Upgrade Required：服务器拒绝基于当前HTTP协议提供服务，通过Upgrade头部告知客户端必须升级协议才能继续处理
    - 比如请求的版本是http/1.1，但是服务端要求至少要web socket或者http/2.0，就会返回这个信息
  - 428 Precondition Required：用户请求中缺失了条件类头部，例如If-Match
  - 429 Too Many Requests：客户端发送请求的速率过快
    - 一般这个信息，会被503取代
  - 431 Request Header Fields Too Large：请求的HEADER头部大小超过限制
    - 这个一般会返回414，URI和头部一般在同一个缓存测处理
  - 451 Unavailable For Legal Reason：RFC7725，由于法律原因资源不可访问


- 5XX：服务器端出现错误
  - 500 Internal Server Error：服务器内部错误，且不属于以下错误类型
  - 501 Not Implemented：服务器不支持实现请求所需要的功能
  - 502 Bad Gateway：代理服务器无法获取到合法响应
  - 503 Service Unavailable：服务器资源尚未准备好处理当前请求,比如服务端做资源的限速
  - 504 Gateway Timeout：代理服务器无法及时的从上游获得响应
  - 505 HTTP Version Not Supported：请求使用的HTTP协议版本不支持
  - 507 Insufficient Storage：服务器没有足够的空间处理请求
  - 508 Loop Detected：访问资源时检测到循环
  - 511 Network Authentication Required：代理服务器发现客户端需要进行身份验证才能获得网络访问权限

## 长连接与短连接
```shell
# http请求包中，如果有Connection字段，
Connection:keep-live / close
# 如果是keep-live，就表示长连接，即持续连接
# 如果是close，就表示短链接，即非持续连接
```
- 如果是非常老的，无法识别Connection头部信息的代理服务器，就用Proxy-Connection来替代Connection来处理长连接

- Connection头部
  - Keep-Alive: 长连接
    - 客户端请求长连接（请求包）
      - Connection: Keep-Alive
    - 服务端表示支持长连接（响应包）
      - Connection: Keep-Alive
    - 客户端复用连接
    - `HTTP/1.1默认支持长连接`
      - Connection: Keep-Alive无意义
  - Close: 短连接

- 当整个访问链路存在代理服务器，则Connection仅针对当前链接有效

## Host头部
- Host = uri-host[":"port]
  - HTTP/1.1规范要求，不传递Host头部则返回400错误响应码
  - 为防止陈旧的代理服务器，发向正向代理的请求request-target必须以absolut-form出现
    - request-line = method SP request-target SP HTTP-version CRLF
    - absolute-form=absolute-URI
      - absolute-URI= scheme":"hier-part["?" query]
### Host头部与消息路由
- 建立TCP连接
  - 确认服务器IP地址
- 服务器接收请求
- 寻早虚拟主机
  - 匹配Host头部与域名
- 寻找URI的处理代码
  - 匹配URI
- 执行处理请求代码
- 生成HTTP响应
- 发送HTTP响应
- 记录访问日志


## 当访问链路中存在很多代理服务器，如何传递IP
- 场景
```shell
用户（内网IP：192.168.0.x） ---->  ADSL(运营商公网IP：115.204.33.1) ----> 正向代理（IP地址1.1.1.1）----> CDN(2.2.2.) ----> 反向代理（得到用户地址115.204.33.1, remote_addr变量：2.2.2.2）

# 这里正向代理到CDN
X-Forwarded-For: 115.204.33.1
X-Real-IP: 115.204.33.1

# CDN到反向代理

X-Forwarded-For: 115.204.33.1, 1.1.1.1
X-Real-IP: 115.204.33.1
```


### 消息的转发
- Cache-Control: no-transform
  - 禁止代理服务器修改响应包体

- Via头部
  - 指明经过的代理服务器名称及版本

## 请求与响应的上下文
- UA(User-Agent)

### 请求的上下文Referer
浏览器对某一页面的请求自动添加的头部
- Referer = absolute-URI / partial-URI
`
- 示例
```shell
Referer: https://developer.mozilla.org/...
```

### Referer详解
`referer`字段用于标识当前请求的来源页面
- 示例
```shell
假设用户在浏览器访问https://example.com/page1.html，并在该页面上点击一个链接，该链接指向https://example.com/page2.html,浏览器会发送如下HTTP请求

GET /page2.html HTTP/1.1
Host: example.com
Referer: https://example.com/page1.html
```

- 注意事项
  - 隐私和安全：Referer字段可能会泄漏用户隐私信息，例如在URL包含的查询参数。为了保护用户隐私，某些浏览器或插件可能会对referer字段进行截断或省略敏感信息
  - 跨域请求：在跨域请求中，浏览器可能会限制`referer`字段的内容
    - 例如：对于跨站点请求，浏览器可能会仅发送源站点，而不包含完整的路径和查询参数
  - 安全和防护：通过检查`referer`，服务器可以防止跨站请求伪造(CSRF)攻击，确保请求是从信任的来源发出的
  
- Referer不会被添加的场景
  - 来源页面采用的协议为本地文件file或dataURI
  - 当前请求页面采用的是http协议，来源页面采用的是https协议

- 服务端常用于统计分析，缓存优化，防盗链等功能


### 请求上下文`Referer-Policy`

通过设置`referer-Policy，网站可以指定在什么情况下以及如何发送Referer
示例
```shell
Referer-Policy: no-referer
```
其他`referer-policy`选项包括
- `no-referer`：不发送referer信息
- `no-referer-when-downgrade`：在跨协议（如从HTTPS到HTTP）的请求中不发送referer
- `origin`：只发送源站点信息，不包括查询路径和参数
- `same-origin`：只有在同一站点内的请求才发送`referer`
- `strict-origin`：仅在同协议的站点请求中发送源站点信息
- `unsafe-url`：始终发送完整的URL(不推荐)

### 请求上下文：From
- 主要用于网络爬虫，告诉服务器如何通过email到爬虫负责人
- From = mailbox

### 响应的上下文：Server
- 指明服务器上用的web软件，用于帮助客户端定位问题或统计数据
```shell
# 例如
Server:nginx
Server: openresty/1.13.6.2
```

### 响应上下文 Allow与Accept-Ranges




