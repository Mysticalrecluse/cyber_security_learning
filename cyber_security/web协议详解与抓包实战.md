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