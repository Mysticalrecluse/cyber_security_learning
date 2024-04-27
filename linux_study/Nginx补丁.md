### Nginx编译安装
```shell
# 安装依赖包
# Ubuntu
apt update && apt -y install gcc make libpcre3 libpcre3-dev openssl libssl-dev zlib1g-dev

# 红帽系统
yum -y install gcc pcre-devel openssl-devel zlib-devel
yum -y install gcc make gcc-c++ libtool pcre pcre-devel zlib zlib-devel openssl openssl-devel perl-ExtUtils-Embed

# 创建用户和组
useradd -s /sbin/nologin nginx

cd /usr/local/src/

wget http://nginx.org/download/nginx-1.18.0.tar.gz

tar xf nginx-1.18.0.tar.gz

cd nginx-1.18.0/

./configure --prefix=/apps/nginx \
--use=nginx \
--group=nginx \
--with-http_ssl_module \
--with-http_v2_module \
--with-http_realip_module \
--with-http_stub_status_module \
--with-http_gzip_static_module \
--with-pcre \
--with-stream \
--with-stream-ssl_module \
--with-stream_realip_module

make && make install

chown -R nginx.nginx /apps/nginx
```

#### 创建Nginx自启动文件
```shell
# 复制同一版本的nginx的yum安装生成的service文件
vim /lib/systemd/system/nginx.service

# nginx.service内容
[Unit]
Description=nginx -high preformance web server
Documentation=http://nginx.org/en/docs/
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
# 指定pid文件的目录，默认在log目录下，可选配置
PIDFile=/apps/nginx/run/nginx.pid
# Nginx主程序 -c Nginx配置文件路径
ExecStart=/apps/nginx/sbin/nginx -c /apps/nginx/conf/nginx.conf
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
LimitNOFILE=100000

[Install]
WantedBy=multi-user.target

# 创建pid文件存放的目录
mkdir /apps/nginx/run/

# 修改配置文件
vim /apps/nginx/conf/nginx.conf
pid  /apps/nginx/run/nginx.pid;
```

#### 验证Nginx自启动文件
```shell
systemctl daemon-reload
systemctl enable --now nginx
```

#### Nginx自动编译脚本
- 老王的视频：【马哥教育】2024年最新Nginx教程入门精讲 ---- P7 Nginx包安装和编译安装 37:00

#### 问题1
- 为什么Nginx的master是root用户运行，而work是普通账号运行
    - master进程会对外监听80端口，接收用户请求，然后交给子进程worker处理
    - 80端口是特权端口，只有root账号有权限使用，普通用户无法监听1023以内的端口
    - nc命令，实现指定端口监听
    ```shell
    # 监听1234
    nc -l 1234  # 假设10.0.0.108开启监听

    nc 10.0.0.108   # 连接该主机，实现主机间通信

    su - mystical
    nc -l 1023  #报错，1023以内，特权端口，只有root可以监听，普通用户不能监听
    ```

### Nginx命令常见用法
```shell
# 可以发送信号
nginx -s signal

# 常见信号signal
stop            # 退出，强退
quit            # 优雅退出
reopen
reload          # 重新加载配置文件，会加载新的进程，平滑关闭旧的worker进程

# 以前台方式运行 
nginx -g 'daemon off;'
```

#### 平滑升级流程
- 平滑升级4个阶段
    - 只有旧版nginx的master和worker进程
    - 旧版和新版nginx的master和worker进程并存，由旧版nginx接收处理用户的新请求
    - 旧版和新版nginx的master和worker进程并存，由新版ngnix接收处理用户的新请求
    - 只有新版nginx的master和worker进程

- 不停机更新Nginx二进制文件
```shell
# 服务端创建一个大文件
dd if=/dev/zero of=/apps/nginx/html/test.img bs=1M count=10

# 客户端下载该文件，保证有进程在工作
wget --limit-rate=1k http://10.0.0.200/test.img

# 编译新版本，得到新版本的二进制文件
wget http://nginx.org/download/nginx.1.24.0.tar.gz
tar xf nginx.1.24.0.tar.gz
cd nginx-1.24.0/

# 参考老版本的编译选项，去编译新版本
# 查看老版本
nginx -V
./configure --prefix=/apps/nginx --user=nginx --group=nginx ...
make # 只执行make，不执行make install
# 在objs/nginx -v

# 把之前的nginx命令备份
cp /apps/nginx/sbin/nginx opt/nginx.old

#  把新版的nginx复制过去，覆盖旧版的文件，需要-f选项，强制覆盖，否则会提示Text file busy

# 启动新版本
kill -USER2 `cat /apps/nginx/logs/nginx.pid`   #-USER2,并来实现USR2

# 此时如果旧版worker进程有用户的旧的请求，会一直等待处理完后才会关闭，即平滑关闭
kill -WINCH `cat /apps/nginx/logs/nginx.pid.oldbin`

# 如果有新请求，则由新版本提供服务

# 经过一段时间测试，如果新版本没问题，最后发送QUIT信号，退出老的master，完成全部升级过程
kill -QUIT `cat /apps/nginx/logs/nginx.pid.oldbin`

############### 回滚 ####################
#如果升级的新版本发现问题，需要回滚，可以发送HUP信号，重新拉起旧版本的worker
kill -HUP `cat /apps/nginx/logs/nginx.pid.oldbin`

# 最后关闭新版的master和worker，如果不执行上面的HUP信号，此步QUIT信号也可以重新拉起旧版本的woker进程
kill -QUIT `cat /apps/nginx/logs/nginx/pid`
# 恢复旧的文件
mv /opt/nginx.old   /apps/nginx/sbin
```

### Nginx核心模块
#### 配置文件说明
- Nginx的配置文件的组成部分：
    - 主配置文件：nginx.conf
    - 子配置文件：include conf.d/*.conf
    - fastcgi, uwsgi, scgi等协议相关配置文件
    - mime.types：支持的mime类型，MIME多用途互联网邮件扩展类型，MIME消息包含文本，图像，音频，视频以及其他应用程序专用的数据，是设定某种扩展名的文件用一种应用程序来打开的方式类型，当该扩展名文件被访问时，浏览器会自动使用指定应用程序来打开。多用于指定一些客户自定义的文件名，以及一些媒体文件打开方式


- 主配置文件结构：四部分
```shell
# 全局配置段
main block: 主配置段，即全局配置段，对http，mail都有效

# 事件驱动相关的配置
event {
    ...
}

#http/https 协议相关配置段
http {
    ...
}

# 默认配置文件不包括下面两个块
#mail相关配置段
mail {
    ...
}

# stream 服务器相关配置段
stream {
    ...
}
```   

#### 主块main
```shell
# 全局配置段，对全局生效，主要设置nginx的启动用户/组，启动的工作进程数量，工作模式，Nginx的PID路径，日志路径等
user    nginx nginx    # worker进程
worker_processes  1;   #启动工作进程数数量,建议设为CPU核数，EPOLL模型，多路复用，一个进程可以处理多个IO请求
# auto选项，自动根据CPU核数，使用进程数

# pid文件保存路径
pid     /apps/nginx/logs/nginx.pid;

# worker进程优先级
worker_priority 0 

# 所有worker进程能打开的文件数量上限
worker_rlimit_nofile 65536 
```
- 重新加载nginx配置文件
```shell
nginx -s reload
```

- 通过亲源机制，把CPU和进程进行绑定（面试题：nginx优化手段之一）
```shell
# 将Nginx工作进程绑定到指定的CPU核心，默认Nginx是不进行绑定的，绑定并不是意味着当前Nginx进程独占一核CPU，但是可以保证
# 此进程不会运行在其他核心，这就减少了nginx的工作进程在不同cpu核心上的来回跳转，可以有效提升nginx服务器的性能
worker_cpu_affinity 00000001 00000010 00000100 00001000 | auto ;
#CPU MASK: 00000001 0号CPU
#          00000010 1号CPU

# 示例
worker_processes 4;
worker_cpu_affinity 00000010 00001000 00100000 1000000
ps axo pid,cmd,psr |grep nginx

# auto 自动，随机结亲源
worker_processes auto;
worker_cpu_affinity auto;
```

- 压力测试
```shell
# ab命令
# ab命令参数
# -n：总请求数； -c：模拟的并发数  -k：以持久连接模式测试
# Ubuntu在apache2-utils
ab -c 1000 -n 10000 http://10.0.0.200/
# 表示一次发1000个请求，总共发10000次

# 在10.0.0.200使用watch命令观察
```

- 面试重点：top命令


#### event模块
```shell
worker_connection 65535 # 设置单个工作进程的最大并发连接数
user epoll      # 使用epoll事件驱动
accept mutex on    # 惊群，推荐on，on为同一时刻一个请求轮流由worker进程处理，而防治被同时唤醒所有worker
# 默认为off，新请求会唤醒所有的worker进程
```

#### http模块
- http协议相关的配置结构
```shell
http {
    ...
    ...   # server的公共配置
    server {   # 每个server用于定义一个虚拟主机，第一个server为默认虚拟服务器
        ...
    }
    server {
        ...
        server_name  # 虚拟主机名
        root         # 主目录
        alias        # 路径别名
        location [OPERATOR] URL {      # 指定URL的特性
            ...
            if CONDITION {
                ...
            }
        }
    }
}
```
- http协议配置说明
```shell
# 是否在响应报文的Server首部显示nginx版本
server_tokens on | off
```
4月26日
---------------------------------------------------------------------------------------
#### 检测文件是否存在
- 语法格式
```shell
# 语法格式1
Syntax: try_files file... uri;
# 语法格式2
Syntax：try_files file... =code;
# 如果自定义的状态码，则会显示在返回数据的状态码中
```

#### 长连接配置
```shell
Syntax: keepalive_requests number;
# 示例
keepalive_requests 1000;

Syntax: keepalive_time time;
#示例
keepalive_time 1h;

Syntax: keepalive_timeout timeoout [header_timeout];
# 这里head_timeout在响应报文里会有，纯诈骗
# 示例
keepalive_timeout 75s;

keepalive_time time; 限制对一个请求处理的最长时间，到时间后续的再有新的请求会断开连接，默认1h;
keepalive_timeout timeout [heaker_timeout]: 设置保持空闲的连接超时时长，0表示禁止连接，默认为75s，通常配置在http字段作为站点全局配置
keepalive_requests number: 在一次长连接上所允许请求的资源的最大数量，默认为1000次
```

#### 作为下载服务器配置
- ngx_http_autoindex_module模块处理以斜杠字符“/”结尾的请求，并生成目录列表，可以做为下载服务器配置使用
- 类似镜像源的网站
```shell
Syntax: autoindex on | off;

# 其他参数
autoindex on|off    # 自动文件索引功能，默认为off
autoindex_exact_size on | off # 计算文件确切大小（单位byte），off是显示大概大小（单位K，M），默认on
autoindex_localtime on | off # 显示本机时间而非GMT时间，默认off
charset charset｜off  # 指定字符编码，默认为off，中文会乱码，指定为utf8
autoindex｜format html | xml | json | jsonp   # 显示索引的页面文件风格，默认html
limit_rate rate;    # 限制响应客户端传输速率（除GET和HEAD 以外的所有方法），单位B/s，即Bytes/second,默认值0，表示无限制，此指令由ngx_http_core_module提供
set $limit_rate 4k; # 也可以通过变量限速，单位B/s，同时设置，此项优先级高 
```

#### 做为上传服务器
- 以下指令控制上传数据
```shell
client_max_body_size 1m;  # 设置允许客户端上传单个文件的最大值，默认值为1m，上传文件超过此值会出413错误
client_body_buffer_size size;  # 用于接收每个客户请求报文的body部分的缓冲区大小；默认16k；超出此大小时，其将暂存到磁盘上的由client_body_temp_path指令定义的位置
client_body_temp_path path [level1 level2...] # 设定存储客户端请求报文的body部分的临时存储路径及子目录结构和数量，目录名为16进制的数字，使用hash之后的值从后往前截取1位，2位，2位做为目录名

1级目录占1位16进制，即2^4=16个目录 0-f
2级目录占2位16进制，即2^8=256个目录 00-ff
3级目录占2位16进制，即2^8=256个目录 00-ff
```

####  Nginx中的变量
- Nginx变量可以在配置文件中使用，用作判断或定义日志格式的源等产景，Nginxbian
- Nginx内置变量
    – Nginx内置噶数据是Nginx自行ID定义的

- 常用内置变量
- 用户自定义变量
- 在Nginx中，除了内置变量外，我们还可以使用set指令来自定义变量
```shell
# 格式：
set $variable value;
```

#### Nginx状态页
```shell
stub_status; # 添加此指令后可开启Nginx状态页，作用域server，location

# 示例
location /status {
    sub_status;
}
```

### Nginx第三方模块使用
- 示例
```shell
https://github.com/vozlt/nginx-module-vts   # 第三方流量监控软件
https://github.com/openresty/echo-nginx-module  #echo模块，可以直接输出
```

- 使用过程
```shell
# 安装编译工具链
apt update && apt install -y make gcc libpcre3 libpcre3-dev openssl libssl-dev zliblg-dev

# 创建运行用户
useradd -r -s /usr/sbin/nologin.nginx

# 下载最新版源码并解压，并上传到Linux服务器
wget   https://nginx.org/download/nginx-1.22.1.tar.gz

# 连带新的模块，重新安装
wge


# 修改目录属性/apps.gncinx  ｜  gz

# 加载配置i示例
```Shell


#### 面试重点
- 全局配置（性能优化）
- 平滑升级回滚

### Nginx反向代理
```shell
Syntax: proxy_pass URL;

```

#### Nginx压缩功能
- 语法格式
```shell
gzip on | off  #启用或禁用压缩功能，默认off
gzip_buffers number size; # nginx在压缩时要想服务器申请的缓存空间个数和大小
```

#### favicon 图标配置
```shell
# 给出文件favicon
location = /favicon.ico {
    root /var/www/html/www.m99-magedu.com/static;
    expires 7d;  # 首次请求缓存后，7天内不能发请求，：
}
```


#### Nginx实现Https
- Nginx中的Https功能需要ngx_http_ssl_module模块支持，使用Yum/apt安装的Nginx中已经包含了该模块功能。如果是自行编译的Nignx，需要在编译的时候指定相关的编译项
```shell
# 常用选项
ssl on|off      

ssl_certificate file;  # 当前虚拟主机的证书文件，通常是PEM格式（两个证书合二为一）
ssl_certificate_key file;   # 当前虚拟主机的私钥文件路径

ssl_session_cache off|none [builtin[:size]][shared:name:size]
# 配置SSL缓存，作用域http，server
# off 禁用SSL/TLS会话缓存
# none 通知客户端可以重用会话，但并没有缓存相关数据，默认值
# builtin[:size] 使用openssl内建缓存，可指定大小，每个worker进程独享
# 【share:name:size] 使用共享缓存，每个worke共享该缓存中的数据可以指定name和大小

ssl_session_timeout time; # 配置SSL/TLS会话缓存的超时时间，默认值为5m
# 使用SSL/TLS会话缓存有助于减少服务器的加密和解密负担，提高HTTPS连接的响应速度，启用缓存需要ssl_session_cache,ssl_session_timeout 两个选项一起使用

#SSL/TLS会话缓存存储的是SSL/TLS握手过程中生成的会话数据。在SSL/TLS握手过程中，服务器和客户端 会交换一系列数据，其中包括协商的密钥、加密算法、会话标识符等信息。这些信息用于确保安全通信，并在 建立连接后用于加密和解密通信的数据
#SSL/TLS会话缓存中存储的主要数据包括 会话标识符(Session Identifier),主密钥(Master Secret),加密算法和参数

#通过存储这些会话数据，SSL/TLS会话缓存允许服务器在处理新连接时，如果客户端提供了先前使用过的会 话标识符，就可以重用这些数据，避免重新执行完整的SSL/TLS握手。这样可以大幅度减少握手过程中的计算 和通信开销，提高性能和响应速度。同时，它还有助于减少服务器的负担，因为不需要重新生成新的密钥和协 商参数
```


#### Nginx中配置防盗链
- 语法格式
```shell
valid_referers none | blocked | server_names | string... ;

# none: 请求头中没有referers则 $invalid_referer,值为空
# static：请求头中，有referer字段，但其值不合法（不是http或https协议），则值为空
# server_name：具体主机名，支持正则表达式，匹配成功，则值为空
```
- 示例
```shell
server {
    listen 80;
    server_name www.abc-234.com;
    root /var/www/html/www.abc-123.com;
    valid_referers none blocked server_names *.test.com ~\.baidu\. ~\.bing\. ~\.so\.;
    if ($invalid_referer) {
        return 403 "Forbidden Access" 
    }
}
```

#### Nginx中的Rewrite
- 在Nginx中，rewrite指令用于重写URI，允许Nginx修改客户端请求的URI，基于此，可用该指令实现URI重定向，修改请求参数，改变请求含义，改变URL结构等
- 该指令来自于ngx_http_rewrite_module 模块
- 主要作用：允许管理员通过配置文件来修改客户端的请求URI，从而实现重新URI，重定向请求，更改请求参数等操作

- 相关指令说明
```shell
break;  # 跳出serer，后续的ngx_http_rewrite_module模块的其他命令都不生效，只中断这个模块，其他模块正常执行
last;  # 跳出当前location，继续从头开始匹配

if (condition) {
    ...
}
# 仅能做单次判断，不支持if-else多分支
# if ($var) {} 仅0和空字符为false
# 支持运算符
# =     比较变量和字符串是否相等，非赋值
# !=    比较变量和字符串是否不等
# ～    区分大小写，是否正则匹配
# ～*   不区分大小写
# !～*  不区分大小写，是否不匹配
# -f|!-f   判断文件是否存在｜不存在
# -d|!-d   判断目录是否存在｜不存在
# -x|!-x   判断是否可执行｜不可执行
# -e|!-e   判断文件（包括文件，目录，软连接）是否存在｜不存在

return code [text]
return code url;
return url    # 不写code， 默认302
              # return后的指令不再执行

rewrite regex replacement [flag];
# flag: last|break|redirect(客户端)|permanent（同redirect）
# redirect（302）和permanent（301）几乎一样，一个301，一个302

rewrite_log on|off   # 是否记录ngx_http_rewrite_module模块产生的日志到error_log中，默认off

set $variable value;  设置变量，给变量赋值
```

- 示例
```shell
location /scheme {
    if ($scheme = http) {
        return 200 "http"
    }
    if ($scheme = https) {
        return 200 "https"
    }
}

location /file {
    if (!-e $request_filename) {
        return 200 "$request_file file not exists";
    }
}
```


- 利用set实现指定限速
```shell
set $slow 1;
location = /test.img {
    if ($slow) {
        limit_rate 10k;
    }
}
```

- return实现浏览器判断
```shell
location /return {
    if ($http_user_agent ~* curl|wget|ApacheBench) {
        return 403 "agent error";
    }
    return 200 "success";
}
```

- rewrite 指令测试
```shell
server {
    listen 80;
    server_name www.feng.org;
    root /var/www/html;

    location /{
        rewrite /1.html /2.html;
        rewrite /2.html /3.html;
    }

    location /2.html {
        rewrite /2.html /a.html;
    }

    location /3.html {
        rewrite /3.html /b.html;
    }
}
```

### Nginx反向代理
#### 实现http协议反向代理
- 相关指令和参数
```shell
proxy_pass URL;    # 转发的后端服务器地址，可以写主机名，域名，IP地址。也可以额外指定端口

proxy_hide_header field;  # 显示指定不回传的响应头字段

proxy_pass_header field;  # 显示指定要回传给客户端的响应头字段

proxy_pass_request_body on|off  # 是否向后端服务器发送客户端http请求的body，默认on

proxy_connect_timeout time;     # Nginx与后盾服务器建立连接超时时长，默认60s，超时会向客户返回504

proxy_read_timeout time;        # Nginx等待后端服务器返回数据的超时时长，默认60sd，超时返回504

proxy_send_timeout time;        # Nginx向后端服务器返回数据的超时时长

proxy_set_body value;           # 重新定义传给后端服务器的请求正文，可以包含文本，变量等

proxy_set_header field value;   # 更改或添加请求头字段并发送到后端服务器

proxy_http_version 1.0|1.1;     # 设置向后端服务器发送请求时，http协议版本，默认1.0

proxy_ignore_client_abort on|off # 客户端中断连接，Nginx是否继续执行与后端的连接，默认off，客户端中断，Nginx也中断与服务端的连接，  on表示客户端中断，Nginx还会继续处理与服务端连接

proxy_headers_hash_buket_size size;  # 当配置了proxy_hide_header和proxy_set_header的时候，用于设置nginx保存HTTP报文头hash表大小，默认64

proxy_headers_hash_max_size size;  # 上一个参数的上限，默认值512


```
















