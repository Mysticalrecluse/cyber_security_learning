# LINUX 基础
## 用户组和权限管理
### 用户和组相关文件
- 用户：Linux中每个用户是通过 User Id(UID)来唯一标识的
  - 管理员：root, UID=0
  - 普通用户：1-60000自动分配
    - 系统用户：1-499(Centos 6以前)，1-999(Centos 7以后) 对守护进程获取资源进行权限分配
    - 登录用户：500+(Centos 6以前)，1000+(Centos 7以后) 给用户进行交互式登录使用
    ```
    守护进程的名称来源

    "Daemon" 这个词在计算领域中指的是后台运行的进程，但它的起源和意义比计算领域的用法要古老得多。

    在古希腊语中，"δαίμων" (daimōn) 的意思是神、命运之神或守护之神。它通常被描述为一种位于神和凡人之间的超自然存在，有时候是好的，有时候是中性的，但它通常在人们察觉不到的情况下起作用，影响人类的命运或行为。这与计算机中的守护进程的概念相似，后者在后台静默地运行，而用户通常不直接与之互动。

    在计算的早期历史中，MIT的研究人员开始使用"daemon"这个词来描述在背后处理各种任务的计算机进程。有一个有趣的历史小故事称，它是由 PDP-10 的操作员 Fernando J. Corbató 和 Victor A. Vyssotsky 创造的。他们将这种程序称为 "disk and execution MONitor"，并使用 "DAEMON" 作为其缩写。无论如何，该术语已经在计算社区中被广泛接受，并被用来描述后台进程。

    因此，"daemon" 这个词用于描述后台进程是因为这些进程默默地、在后台工作，而不需要用户的直接干预，很像古希腊神话中的守护之神在幕后影响事物的方式。
    ```

- 用户组：Linux中可以将一个或多个用户加入用户组中，用户组是通过Group ID(GID)来唯一标识的。(不起实质作用)

- 用户和组的关系
  - 用户的主要组(primary group)：用户必须属于一个且只有一个主组，默认创建用户时自动创建和用户名同名的组，做为用户的主要组，由于此组中只有一个用户，又称为私有组
  - 用户的附加组（supplementary group）：一个用户可以属于零个或多个辅助组，附属组

- 安全上下文
  -  Linux安全上下文Context：运行中的程序，即进程（process）,以进程发起者的身份运行，进程所能访问资源的权限取决于进程的运行者身份；
  -  比如：分别以root和wang的身份运行/bin/cat /etc shadow，得到的结果是不同的，资源能否被访问，是由运行者的身份决定，非程序本身

### 用户和组管理命令
- Linxu中和用户有关的文件
  ```shell
  ll /etc/passwd  /etc/shadow

  getent passwd = cat /etc/passwd #直接在屏幕上打印出passwd的信息
  getent passwd <用户名>

  root:x:0:0:root:/root:/bin/bash
  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
  bin:x:2:2:bin:/bin:/usr/sbin/nologin
  sys:x:3:3:sys:/dev:/usr/sbin/nologin
  sync:x:4:65534:sync:/bin:/bin/sync
  games:x:5:60:games:/usr/games:/usr/sbin/nologin
  man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
  lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
  mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
  ...
  #后续省略


  //每一个上都是一个用户信息，有几行，就有几个用户，大部分是程序服务作为用户的信息
  //这里的每个信息都用“:”隔开，一共7个信息，分别是：
  //name,password(密码被迁到别的地方存储),UID,GID,GECOS（描述）,directory(家目录),shell类型


  /etc/shadow #存放指令的文件，密码，日期

  root@ubuntu2004:/etc# cat shadow
  root:$6$CNc6y8cEgE3pNLSo$U6Nk1J2hmcMAf8y4yAPZLoXY12sWtBvO62z1l67OjetuR0Ndv9CL29SaSn7ZXRJFRHu0jgE5aJso1NYvopYgG0:19503:0:99999:7:::
  daemon:*:19430:0:99999:7:::
  bin:*:19430:0:99999:7:::
  sys:*:19430:0:99999:7:::
  sync:*:19430:0:99999:7:::
  games:*:19430:0:99999:7:::
  man:*:19430:0:99999:7:::
  lp:*:19430:0:99999:7:::
  mail:*:19430:0:99999:7:::
  ...
  # 此处省略
  mystical:$6$74dN0tlhGHDsqcyd$/tZTWDJMRdMdYREiF9npwh9nSHhbKb4hVW/kA15jCyzBtocgp1s3MhDP21hnsULwOaBkb3.QXfEZNIklTopuh/:19503:0:99999:7:::
  lxd:!:19503::::::
  rtkit:*:19529:0:99999:7:::
  dnsmasq:*:19529:0:99999:7:::
  avahi:*:19529:0:99999:7:::
  cups-pk-helper:*:19529:0:99999:7:::
  pulse:*:19529:0:99999:7:::
  geoclue:*:19529:0:99999:7:::
  saned:*:19529:0:99999:7:::
  colord:*:19529:0:99999:7:::
  gdm:*:19529:0:99999:7:::
    ...
  # 此处省略


  //组成：密码（加密后），时间（以1970年以基准到更改密码的天数），最短有效期（0代表可随时更改）,密码有效期，密码以前几天提醒，再过几天账号锁定
  //账号有效期


  /etc/group    

  root:x:0:
  daemon:x:1:
  bin:x:2:
  sys:x:3:
  adm:x:4:syslog,mystical
  tty:x:5:syslog
  disk:x:6:
  lp:x:7:
  mail:x:8:
  news:x:9:
  ...
  # 后续省略

  //组的文件组成：组名，密码，id，成员

  /etc/gshadow

  root:*::
  daemon:*::
  bin:*::
  sys:*::
  adm:*::syslog,mystical
  tty:*::syslog
  ...
  # 后续省略

  //组名，组的口令，管理员账号（管理员可以在组中增删用户）
  ```



## 文本处理
### Awk
#### Awk基础
- Awk语法
```shell
awk [option] 'pattern[action]' file ...
# options：awk可选参数
# pattern：模式
# {action}：动作； 最常用的动作是 print 和 printf
# file：文件/数据
```
- Awk场景
```shell
[Mon Aug 14 09:16:05 -bash 24] root@parrot:Storage #cat prac1.txt
root x 0 0 root /root /bin/bash
daemon x 1 1 daemon /usr/sbin /usr/sbin/nologin
bin x 2 2 bin /bin /usr/sbin/nologin
sys x 3 3 sys /dev /usr/sbin/nologin
sync x 4 65534 sync /bin /bin/sync
games x 5 60 games /usr/games /usr/sbin/nologin
man x 6 12 man /var/cache/man /usr/sbin/nologin
lp x 7 7 lp /var/spool/lpd /usr/sbin/nologin
mail x 8 8 mail /var/mail /usr/sbin/nologin
news x 9 9 news /var/spool/news /usr/sbin/nologin
inetsim x 132 138  /var/lib/inetsim /usr/sbin/nologin
_gvm x 133 140  /var/lib/openvas /usr/sbin/nologin
beef-xss x 134 141  /var/lib/beef-xss /usr/sbin/nologin
mystical x 1000 1003 mystical /home/mystical /bin/bash
saned x 135 142  /var/lib/saned /usr/sbin/nologin
[Mon Aug 14 09:16:21 -bash 25] root@parrot:Storage #cat prac1.txt | awk '{print $1}'
root
daemon
bin
sys
sync
games
man
lp
mail
news
inetsim
_gvm
beef-xss
mystical
saned
```
- 简单规则：
  - awk默认以空格为分隔符，且多个空格也识别为一个空格，作为分隔符
  - awk是按行处理文件，一行处理完毕，处理下一行，根据用户指定的分隔符去工作，没有指定则默认空格

- awk内置变量
<table>
    <thead>
        <th style="background-color: darkred; color: white;">内置变量</th>
        <th style="background-color: darkred; color: white;">解释</th>
    </thead>
    <tbody>
        <tr>
            <td>$n</td>
            <td>指定分隔符后，当前记录的第n个字段</td>
        </tr>
        <tr>
            <td>$0</td>
            <td>表示整行</td>
        </tr>
        <tr>
            <td>FS</td>
            <td>字段分隔符，默认是空格</td>
        </tr>
        <tr>
            <td>NF(Number of fields)</td>
            <td>分割后，当前一共有多少个字段</td>
        </tr>
        <tr>
            <td>NR(Number of records)</td>
            <td>当前记录数，行数</td>
        </tr>
        <tr>
            <td>更多详情查看man手册</td>
            <td>man awk</td>
        </tr>
    </tbody>
</table>

- 一次性输出多列信息
  - 示例：awk '{print $1,$4,$5}' prac1.txt
  - ',' 逗号代表空格分隔显示

- 自定义输出内容
  - awk，必须外层用单引号，内层用双引号
  - 示例：awk '{print "第一列",$1,"第二列",$2}' prac1.txt
  - 内层双引号代表字符串

- awk参数
<table>
    <thead>
        <th style="background-color: darkred; color: white;">参数</th>
        <th style="background-color: darkred; color: white;">解释</th>
    </thead>
    <tbody>
        <tr>
            <td>-F</td>
            <td>指定分割字段符</td>
        </tr>
        <tr>
            <td>-v</td>
            <td>定义或修改一个awk内部的变量</td>
        </tr>
        <tr>
            <td>-f</td>
            <td>从脚本文件中读取awk命令</td>
        </tr>
    </tbody>
</table>

- 输出指定行信息
  - 示例：awk 'NR==5{print $0}' prac1.txt 输出第5行数据
  - 示例2：awk 'NR==5,NR==10{print $0}' prac1.txt 输出第5-10行数据
  - 示例3：awk 'NR==5,NR==10{print NR,$0}' prac1.txt 输出第5-10行数据，并给每一行的内容添加行号

- awk变量
  - 内置变量
  <table>
    <thead>
        <th style="background-color: darkred; color: white;">内置变量</th>
        <th style="background-color: darkred; color: white;">解释</th>
    </thead>
    <tbody>
        <tr>
            <td>$n</td>
            <td>指定分隔符后，当前记录的第n个字段</td>
        </tr>
        <tr>
            <td>$0</td>
            <td>表示整行</td>
        </tr>
        <tr>
            <td>NF(Number of fields)</td>
            <td>分割后，当前一共有多少个字段</td>
        </tr>
        <tr>
            <td>NR(Number of records)</td>
            <td>当前记录数，行数</td>
        </tr>
        <tr>
            <td>FS</td>
            <td>输入字段分隔符，默认为空格</td>
        </tr>
        <tr>
            <td>OFS</td>
            <td>输出字段分隔符，默认为空格</td>
        </tr>
        <tr>
            <td>RS</td>
            <td>输入记录分隔符，指定输入时的换行符</td>
        </tr>
        <tr>
            <td>ORS</td>
            <td>输出记录分隔符，输出指定的换行符</td>
        </tr>
        <tr>
            <td>FNR</td>
            <td>各文件分别计数的行号</td>
        </tr>
        <tr>
            <td>FILENAME</td>
            <td>FILENAME：当前文件名</td>
        </tr>
        <tr>
            <td>ARGC</td>
            <td>命令行参数个数</td>
        </tr>
        <tr>
            <td>ARGV</td>
            <td>数组，保存命令行所给定的各参数</td>
        </tr>

    </tbody>
  </table>

  - 自定义变量
    - 方法一：-v varName=value
    - 示例：awk -v myname="峰哥" 'BEGIN{print "我的名字是？",myname}'
    - 方法二：在程序中直接定义

- awk格式化
  - printf 格式化输出
  - printf 和 print 的区别
  ```
  format的使用

  要点：
  1.其与print命令的最大不同是，printf需要指定format
  2.format用于指定后面的每个item的输出格式
  3.printf语句不会自动打印换行符；\n

  format格式的指示符都以%开头，后跟一个字符；如下：
  %c: 显示字符的ASCLL码；
  %d, %i：十进制整数；
  %e, %E：科学计数法显示数值；
  %f：显示浮点数；
  %s：显示字符串；
  %u：显示无符号整数；
  %%：显示%自身

  printf修饰符
  -：左对齐，默认右对齐；
  +：显示数值符号； printf"%+d"

  ```

- awk模式pattern
  - BEGIN：处理文本前，先执行BEGIN模式指定的动作
  - END：处理完指定文本后，需要执行的动作
    <table>
        <thead>
            <th style="background-color: darkred; color: white;">关系运算符</th>
            <th style="background-color: darkred; color: white;">解释</th>
            <th style="background-color: darkred; color: white;">示例</th>
        </thead>
        <tbody>
            <tr>
                <td><</td>
                <td>小于</td>
                <td>x < y </td>
            </tr>
            <tr>
                <td><=</td>
                <td>小于等于</td>
                <td> x <= y </td>
            </tr>
            <tr>
                <td>==</td>
                <td>等于</td>
                <td> x == y </td>
            </tr>
            <tr>
                <td>!=</td>
                <td>不等于</td>
                <td> x != y </td>
            </tr>
            <tr>
                <td> >= </td>
                <td>大于等于</td>
                <td> x >= y </td>
            </tr>
            <tr>
                <td>></td>
                <td>大于</td>
                <td> x > y </td>
            </tr>
            <tr>
                <td>~</td>
                <td>匹配正则</td>
                <td>x~/正则/</td>
            </tr>
            <tr>
                <td>!~</td>
                <td>不匹配正则</td>
                <td> x!~/正则/ </td>
            </tr>
        </tbody>
    </table>

- awk使用正则语法
  - awk '/正则表达式/{动作}' file


### Sed (Stream EDitor)
#### Sed工作原理
- Sed是从文件或管道中读取一行，处理一行，输出一行；再读取一行，再处理一行，再输出一行，直到最后一行。每当处理一行时，把当前处理的行存储在临时缓冲区中，称为<strong>模式空间(Pattern Space)</strong>,接着用sed命令处理缓冲区中的内容，处理完成后，把缓冲区的内容送往屏幕。接着处理下一行，这样不断重复，直到文件末尾。

#### Sed基本用法
- 格式：
```shell
sed [option]...'script;script;...' [inputfile...]
```
- 常用选项
```
-n          不输出模式空间内容到屏幕，即不自动打印
-e          多点编辑
-f FILE     从指定文件中读取编辑脚本
-r,-E       使用扩展正则表达式
-i.bak      备份文件并原处编辑
-s          将多个文件视为独立文件，而不是单个连续的长文件流

#说明：
-ir         不支持
-i -r       支持
-ri         支持
-ni         危险选项，会清空文件
```

- script格式：
```
'地址格式'

1. 不给地址：对全文进行处理
2. 单地址：
    #：指定的行，$:最后一行
    /pattern/：被此处模式所能够匹配到的每一行
3. 地址范围；
    #,#     #从#行到第#行，3，6 从第3行到第6行
    #,+#    #从#行到+#行，3，+4 表示从3行到第7行
    /pat1/,/pat2/
    #,/pat/
    /pat/,#
4. 步进：~
    1~2  奇数行
    2~2  偶数行

'命令格式'

 ▪ -p           打印当前模式空间内容，追加到默认输出之后
 ▪ -Ip          忽略大小写输出
 ▪ -d           删除模式空间匹配的行，并立即启用下一轮循环
 ▪ a [\]text    在指定行后面追加文本，支持使用\n实现多行追加
 ▪ i [\]text    在行前面插入文本
 ▪ c [\]text    替换行为单行或多行文本
 ▪ w file       保存模式匹配的行至指定文件
 ▪ r file       读取指定文件的文本至模式空间中匹配到的行后
 ▪ =            为模式空间中的行打印行号
 ▪ ！           模式空间中匹配行取反处理
 ▪ q            结束或退出sed
```
- 扩展：
```
sed命令:
eg:sed ' '
在不写地址的时候，默认对全文处理
在不写指令的时候，默认自动打印

sed ' ' < /etc/passwd  
在无任何地址，指令的情况下，默认打印输入的所有内容

使用-n，可以关闭这种自动打印，使其只打印指定内容

CentOS 安装后必须所做的初始化操作

#关闭SELINUX
sed -i '/^SELINUX=/c SELINUX=disabled' /etc/selinux/config
#关闭防火墙
systemctl disable --now firewalld

Ubuntu开启root远程登录功能
#sudo -i
#passwd root
#sed -i '/PermitRootLogin/c PermitRootLogin yes' /etc/ssh/sshd_config
#systemctl restart sshd
```

- 分组与后项引用
```
#查找替代
s/pattern/string/修饰符
替换修饰符：
g       行内全局替换
p       显示替换成功的行
w       /PATH/FILE 将替换成功的行保存至文件中
I，i    忽略大小写

#查找替换，支持使用其他分隔符，可以是其他形式：s@@@,s###

#正则表达式：后项引用
示例：
echo 123456789 -> 456123789
echo 123456789|sed -rn 's/(123)(456)(789)/\2\1\3/p'
#用括号分组
用反斜杠'\'+数字表示分组的代号
```

## 网络协议和管理
 - OSI网络国际标准
   - 由ISO国际标准化组织定义
   - 应用层：Application
   - 表示层：Presentation
     - 实现资源的格式与转换，包括压缩，解压缩，加密，解密等 
   - 会话层：Session
   - 传输层：Transport
     - 实现应用进程间的安全可靠的通信
   - 网络层：Network
     - 负责端到端的路径的选择，同时实现跨网域通信
   - 数据链路层：Data Link
     - 根据目标和源的mac地址，进行点与点之间的通信
   - 物理层：Physical
 - Mac地址
   - 由48位二进制数或12位16进制数组成
   - 示例：00:0c:29:21:ac:a1
  
- 网络通信的过程
  - 协议数据单元PDU：Protocol Data Unit，协议数据单元是指对等层次之间传递的数据单位。
    - 物理层的PDU是数据位 bit
    - 数据链路层的PDU是数据帧 frame
    - 网络层的PDU是数据包 Packet
    - 传输层的PDU是数据段 segment
    - 应用层的PDU是message
  - 三种通讯模式
    - unicast：单播：目标设备是一个
    - broadcast：广播，目标设备是所有
    - multicast：多播，组播，目标设备是多个
  - 冲突域和广播域
    - 冲突域：两个网络设备同时发送数据，如果发生了冲突，则两个设备处于同一个冲突域，反之，则各自处于不同的冲突域。
    - 广播域：一个网络设备发送广播，另一个设备收到了，则两个设备处于同一个广播域，反之，则各自处于不同过的广播域。
  - 三种通讯机制
    - 单工通信：只有一个方向的通信。比如：收音机
    - 半双工通信：通信双方都可以发送和接收信息，但不能同时发送，也不能同时接收，比如：对讲机
    - 全双工通信：通信双方可以同时发送和同时接收，比如：手机
  ```shell
  mii-tool eth0(网卡名)
  >>> eth0: negotiated 1000baseT-FD flow-control,link ok
  <!-- 可以查询到网卡是否连通 -->

  ethtool eth0(网卡名)
  <!-- 能够返回网卡的状态 -->
  ```
### 局域网
- 标准：关注定义了数据链路层和物理层
- 局域网中主流的设备是交换机，如果需要连接外网，才需要路由器

- 集线器与交换机
  - 集线器(hub)：所有连接集线器得机器都在同一个冲突域中，也同时在同一个广播域中，所以集线器有很严重得安全隐患，因为，一台机器向另一个机器发送数据得时候，集线器会把数据广播给所有机器，工作在物理层
  - 交换机(二层设备)：只有第一次发送数据会产生广播，后续将机器mac地址和端口一一记录后，以后得数据发送，都是点对点得数据发送，避免了广播得问题

- 路由器router
  - 作用：把一个数据包从一个设备发送到不同网络里得另一个设备中（跨网域）。路由器只关心网络得状态和决定网络中的最佳路径。路由的实现依靠路由器中的路由表来完成。
  - 功能
    - 工作在网络层
    - 分隔广播域和冲突域
    - 选择路由表中到达目录最好的路径
    - 维护和检查路由信息

- 以太网技术
  - 概述：以太网(Ethernet)是一种产生较早且使用相当广泛的局域网，由美国Xerox(施乐)公司的Palo Alto研究中心(简称PARC)于20世纪70年代初期开始研究，并于1975年研制成功。
  - 以太网MAC帧格式
  ![Alt text](images/image01.png)
    - Preamble：8个字节前导信息（检测是否网络冲突）
    - Destination Address：6个字节的目标MAC地址
    - Source Address: 6个字节的源MAC地址
    - Type：2个字节的要传给上层的协议类型
    - Data：46-1500字节的数据
    - FCS：4个字节的校验位

  - MAC地址
    - 共6个字节，48位bit，前3个字节由网卡的厂商定义，后3个字节可由工厂自定义
    - 可以通过standards-oui.ieee.org/oui/oui.txt查询各大厂商的mac前3字节的值
  - 在虚拟机中，不同机器的相当于连接在集线器hub上，因此，可以在windows上通过抓包，把虚拟机之间的通信数据包抓取
  - Linux中的抓包工具：tcpdump
  ```shell
  tcpdump -i eth0 -nn icmp

  -i 指定抓取哪个网卡的包
  -nn 表示ip以数字形式展示
  icmp 表示抓取哪个协议的数据包
  ```

- VLan原理-虚拟局域网
  - 虚拟局域网VLAN是由一些局域网网段构成的与物理位置无关的逻辑组，实在在交换机内进行局域网隔离的效果

- VXLAN
  - 云环境下，进行虚拟局域网隔离

### TCP/IP协议栈
- TCP包头结构
![Alt text](images/image02.png)
  - 端口号
    - 0-1023：系统端口或特权端口（仅管理员可用），众所周知，永久分配给固定的系统应用使用，22/tcp(ssh)，80/tcp(http)，443/tcp(https)
    - 1024-49151:用户端口或注册端口，但要求并不严格，分配给程序员注册为某应用使用，1433/tcp(SqlServer)，1521/tcp(oracle)，3306/tcp(MySQL)
    - 49151-65535：动态或私有端口，客户端随意使用端口，范围定义：/proc/sys/net/ipv4/ip_local_port_range（可以通过重定向更改这个端口值得范围）
    - 查看当前正在使用的端口号
    ```shell
    <!-- 去检索 /etc/services -->
    grep <端口号> /etc/services

    监听端口号的使用
    ss -tntl
    ```
  - 序号(4个字节)：
    - 表示本报文段所发送数据的第一个字节编号。在TCP连接中所传诵的字节流的每个字节都会按顺序编号。由于序列号由32位表示，所以每2^32个字节，就会出现序列回绕，再次从0开始
  - 确认号：
    - 表示接收方期望收到的发送方下一个报文段的第一个字节数据的编号
    - 通过序号和确认号，保证数据包可靠有序的发送
  - 数据偏移(4bit)
    - 表示tcp头部的长度
  - 保留（6bit）：没用到的空间
  - <font color=tomato>关于tcp连接握手的重要的6位</font>
    - URG(紧急指针)
      - 如果URG为1表示紧急指针数据有效，为0则无效
    - <font color=tomato>ACK</font>
    - PSH
      - 如果为1，表示接收到报文后不等待，立即发送给上层应用程序，如果为0，则报文会在缓冲区存放一段时间，在传给上层应用程序
    - RST(重置位)
      - 如果是0,则正常通信，如果是1，表示报文有问题，需要重新发送
    - <font color=tomato>SYN</font>
    - <font color=tomato>FIN</font>

- 三次握手和四次挥手
  - 三次握手（建立连接）
![Alt text](images/image03.png)
  - 第一次：客户端向服务端发送报文；此时，SYN=1，seq即序列号为x
  - 第二次：服务端收到报文，响应客户端，发送报文；此时，SYN=1，ACK=1，序列号seq=y，确认号ack=x+1
  - 第三次：客户端再次向服务端发送报文；此时ACK=1，seq=x+1，ack=y+1
  - 三次握手的原因：
    - 第一次握手，保证了A发送数据包，B接收数据包
    - 第二次握手，保证了A接收到B发送的响应包，证明了A端数据包的有去有回，但是此时无法保证B端的响应包能够有去有回，因此需要第三次握手
    - 第三次握手，A接收到B的响应包后，再次给B发送数据包，B接收数据包，实现了B端数据包的有去有回
    - 总结：因此，tcp面向连接，实现连接达成需要至少需要经历3次握手；核心在于，只有数据有去有回才能证明通信一端的达成
    - 除了数据包外，还要注意客户端和服务端的网络状态的改变，通过下面的命令可以查看到
    ```shell
    ss -nalt

    // 同时能够查看到处于监听状态的所有端口

    ss -ntlp
    lsof -i :<端口号>

    // 能够查看到占用端口的具体程序
    ```
    - 正常通信，SYN-SENT和SYN-RECV的状态，持续很短，很难看到
      - SYN-SENT观测到的方法：是服务端在接收到客户端发送过来的数据后，屏蔽掉客户端，不向客户端响应数据，这样客户端就会停在SYN-SENT的状突，不会向ESTAB-LISTEN(建立连接的状态)转变
      - SYN-RECV的观测方法：客户端不接受服务器端的响应,在服务器端在发送数据包后，由LISTEN状态变成SYN-RECV状态，后续由于没有收到客户端后续发送的数据包，因此维持下SYN-RECV的状态，不会向ESTAB转变
      - 上述过程，需要使用到iptables的命令工具

  - 四次挥手（退出连接）
  ![Alt text](images/image04.png)

- 半连接队列和全连接队列

    ```shell
    /proc/sys/net/ipv4/tcp_max_syn_backlog    # 未完成连接队列大小，默认值128，建议调整大小为1024以上

    /proc/sys/net/core/somaxconn  # 完成连接队列大小，默认值128，建议调整大小为1024以上
    ```

  - 半连接队列：在三次握手建立连接的时候，服务器收到了第一次握手时，客户端发来的数据包，并在第二次握手的时候进行了回复，在等待客服端再次发送数据包的服务器的第三次握手之前，会将这个时候的连接状态，放到syns queue的队列中，如果，服务器收到了第三次握手中客户端发来的数据包，则会把半连接状态的数据从队列中清除，如果没收到第三次握手时，客户端发来的数据包，则此次半连接状态会一直缓存在syns queue即半连接队列中
  
    ```
    SYN洪水攻击”（SYN Flood Attack）

    在 SYN 洪水攻击中，攻击者连续地发送大量的 SYN 请求到服务器，但故意不响应服务器的 SYN+ACK，从而不完成三次握手。因此，这些半建立的连接会占据半连接队列（SYN Queue）。如果这些请求足够多，会导致队列迅速填满。当半连接队列满时，新的正常用户请求也无法被放入队列，从而无法与服务器建立连接。

    Linux 有一个特性叫做 SYN cookies，它是一个防止 SYN 洪水攻击的策略。当 SYN 队列快要满时，服务器可以选择不使用队列，而是为每个 SYN 包计算一个特殊的值（称为 SYN cookie）并发送回 SYN+ACK。这样，即使队列已满，服务器仍然可以响应新的连接请求。当服务器后续收到客户端的 ACK 时，它可以使用 SYN cookie 来验证并建立连接，而不需要查询 SYN 队列。
    ```

  - 全连接队列：在三次握手完成后，服务器会将连接已建立的状态的信息数据放入accept queue即全连接队列中，用户在3次握手建立连接后，第四次发送数据包请求时，服务器端有一个accept()函数，来接收用户请求，接收到之后，会将accept queue队列中之前缓存的连接建立状态的数据包清除掉，如果accept()没有接收到第四次客户的请求，建立连接状态的数据包就会一直在accept queue中排队
    ```
    连接泄露/连接耗尽攻击

    攻击者通过正常地进行三次握手与服务器建立连接，但在连接建立后不进行实质性的数据交换或请求，从而占用服务器的资源。当攻击者建立了大量这样的“空闲”连接后，服务器的 ACCEPT 队列可能会被填满，导致正常用户无法与服务器建立新的连接。

    简单地说，攻击者的策略是：

    正常执行三次握手，与服务器建立连接。
    在连接建立后，不进行实际的数据传输或请求，使连接保持空闲。
    重复上述步骤，创建大量空闲连接，从而耗尽服务器的资源或填满 ACCEPT 队列。
    这种策略的目的是耗尽服务器的资源（如文件描述符、内存）或填满 ACCEPT 队列，从而使得正常用户无法与服务器建立新的连接。与 SYN 洪水攻击不同，这种攻击已经完成了完整的三次握手，因此会被视为有效的连接，使得对其进行检测和防护更为困难。

    为了防范此类攻击，以下是一些建议：

    连接超时：为连接设置一个合理的超时，确保长时间未活跃的连接会被关闭。
    限制源 IP 的连接数：可以配置防火墙或其他安全设备，限制来自单一源 IP 的并发连接数量。
    监控：监控服务器的资源使用情况，如文件描述符、内存等。当资源使用接近上限时，可以及时采取措施。
    负载均衡器和防火墙：使用负载均衡器或防火墙进行前端流量过滤，拒绝异常的连接请求。
    ```

- TCP超时重传
  - 定义：异常网络状况下(开始出现超时或丢包)，TCP控制数据传输以保证其承诺的可靠服务
  <br>TCP服务必须能够重传超时时间内未收到确认的TCP报文段。为此，TCP模块为每个TCP报文段都维护一个重传定时器，该定时器在tcp报文段第一次被发送时启动。如果超时时间内未收到接收方的应答，TCP模块将重传TCP报文段并重置定时器。
  <br>至于下次重传的超时时间如何选择，以及最多执行多少次重传，就是TCP重传策略
  <br>
  <br>与TCP超时重传相关的两个内核参数
    ```shell
    /proc/sys/net/ipv4/tcp_retries1     # 指定在底层IP接管之前TCP最少执行的重传次数，默认是3

    /proc/sys/net/ipv4/tcp_retries2     # 指定连接放弃前TCP最多可以执行的重传次数，默认值15(对应13-30min)
    ```
- 拥塞控制
- 内核TCP参数优化（建议后续深入了解）

### UDP协议(User Datagram Protocol)
- UDP特性
  - 工作在传输层
  - 提供不可靠的网络访问
  - 非面向连接协议
  - 有限的错误检查
  - 传输性能高
  - 无数据恢复特性
- UDP包头
  ![Alt text](images/image05.png)

### Internet层
### ICMP协议(Internet Control Message Protocol)
- 范例：利用ICMP协议判断网络状态
```shell
ping 10.0.0.8
ping -f -s <ip地址>
-f 表示泛洪，就是最大功率无限制发送数据包
-s 指定发送包的大小，最大不能超过65507
```

### ARP协议(Address Resolution Protocol)
- ARP协议
  - 定义：APR地址解析协议，由互联网工程任务组(IETF)在1982年11月发布的RFC826中描述制定，是根据IP地址获取物理地址的一个TCP/IP协议
  - 作用：根据IP地址寻找对应的物理地址
  - 原理：显示发送一个包含有IP地址的请求广播给局域网的所有主机，对应IP的主机会返回一个数据包给发送请求的主机，该数据包中含有这个主机的MAC地址，交换机上记载着MAC地址对应的交换机接口，从而实现物理地址的寻址
  - 本质：在于IP地址到MAC地址的转换