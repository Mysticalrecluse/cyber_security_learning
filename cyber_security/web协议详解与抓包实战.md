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

## 基于ABNF语义定义的HTTP消息格式
- HTTP协议格式
  - start-line
  - header-field
  - message-body

![Alt text](images/image17.png)

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
```ABNF
HTTP-message = start-line*(hearder-field CRLF)CRLF[message-body]
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
  - 参与制订URL规范 (1998.8)
  - 主导制订HTTP/1.1规范 (1999.6)
  - 2000年发布指导HTTP/1.1规范制订的论文
    - 《Architectural Style and the Design of Network-based Software Architectures》即我们常谈的Representational State Transfer(REST)架构
  - Apache基金会 (The Apache Software Foundation) 共同创始人
    - 参与开发Apache httpd服务 

- 万维网创始人：Tim Berners Lee
  - Web's major goal was to be a shared information space through which people and machines could communicate.

- 解决www信息交互必须面对的需求
  - 低门槛
  - 可扩展性：巨大的用户群体，超长的寿命
  - 分布式系统下的Hypermedia：大粒度数据的网络传输
  - Internet模式
    - 无法控制的scalability
      - 不可预测的负载、非法格式的数据、恶意消息
      - 客户端不能保持所有服务器信息，服务器不能保持多个请求间的状态信息
    - 独立的组件部署：新老组件并存
  - 向前兼容：自1993年起HTTP0.9/1.0（1996）已经被广泛使用

## 评估Web架构的七大关键属性
- HTTP协议应当在以下属性中取得可接受的均衡：
  - 性能performance：影响高可用的关键因素
  - 可伸缩性Scalability：支持部署可以相互交互的大量组件
  - 简单性Simplicity：易理解、易实现、易验证
  - 可见性Visiable：对两个组件间的交互进行监视或者仲裁的能力。如缓存、分层设计等
  - 可移植性Portability：在不同的环境下运行的能力
  - 可靠性Reliability：出现部分故障时，对整体影响的程度
  - 可修改性Modifiability：对系统做出修改的难以程度，由可进化性、可定制性、可扩展性、可配置性、可重用性构成

### 性能
- 网络性能 Network Performance
  - Throughput吞吐量：小于等于带宽Bandwidth
  - Overhead开销：首次开销，每次开销
- 用户感知到的性能 User-perceived Performance
  - Latency延迟：发起请求到接收到响应的时间
  - Completion完成时间：完成一个应用动作所花费的时间
- 网络效率 Network Efficiency
  - 重用缓存、减少交互次数、数据传输距离更近(CDN)、COD

### 可修改性
- 可进化型Evolvability：一个组件独立升级而不影响其他组件
- 可扩展性Extensibility：向系统添加功能，而不会影响到系统的其他部分
- 可定制性Customizability：临时性、定制性地更改某一要素来提供服务，不对常规客户产生影响
- 可配置性Configurability：应用部署后可通过修改配置提供新的功能
- 可重用性Reusability：组件可以不做修改在其他应用上使用

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
    - 201 Created：有新资源在服务器端被成功创建
    - 202 Accepted：服务器接收并开始处理请求，但请求未处理完成。这样一个模糊的概念是有意如此设计的，可以覆盖更多的场景。例如：异步，需要长时间处理的任务
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
  - 401 Unauthorized：用户认证信息缺失或者不正确，导致服务器无法处理请求
  - 407 Proxy Authentication Required：对需要经由代理的请求，认证信息未通过代理服务器的验证
  - 403 Forbidden：服务器理解请求的含义，但没有权限执行此请求
  - 404 Not Found：服务器没有找到对应的资源
  - 410 Gone：服务器没有找到对应的资源，且明确的知道该位置永久性找不到该资源
  - 405 Method Not Allowed: 服务器不支持请求行中的method方法
  - 406 Not Acceptable：对客户端指定的资源表述不存在（例如对语言或编码有要求），服务器返回表述列表供客户端选择
  - 408 Request Timeout：服务器接收请求超时
  - 409 Conflict：资源冲突，例如上传文件时目标位置已经存在版本更新的资源
  - 411 Length Required：如果请求含有包体且未携带Content-Length头部，且不属于chunk类请求时，返回411
  - 412 Precondition Failed：复用缓存时传递的If-Unmodified-Since或If-None-Match头部不被满足
  - 413 Payload Too Large/Request Entity Too Large：请求的包体超出服务器能处理的最大长度
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
  - 503 Service Unavailable：服务器资源尚未准备好处理当前请求
  - 504 Gateway Timeout：代理服务器无法及时的从上游获得响应
  - 505 HTTP Version Not Supported：请求使用的HTTP协议版本不支持
  - 507 Insufficient Storage：服务器没有足够的空间处理请求
  - 508 Loop Detected：访问资源时检测到循环
  - 511 Network Authentication Required：代理服务器发现客户端需要进行身份验证才能获得网络访问权限

## 长连接与短连接
```shell
Connection:keep-live / close
# 如果是keep-live，就表示长连接，即持续连接
# 如果是close，就表示短链接，即非持续连接
```
- 如果是非常老的，无法识别Connection头部信息的代理服务器，就用Proxy-Connection来替代Connection来处理长连接