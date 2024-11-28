# Linux基础



## 命令使用帮助

### tldr-too long don't read

#### 执行以下脚本

``````bash
https://www.mysticalrecluse.com/script/Shell/tldr.sh
bash tldr.sh
``````

![image-20241128162756667](C:\Users\31403\AppData\Roaming\Typora\typora-user-images\image-20241128162756667.png)



## 查看日期时间



### 系统时间

``````bash
date  # 查看系统时间

date -R # 显示时区信息

date +%s  # 显示时间戳（从1970年1月1日到当前时间，经过的秒数）

date +"%F %T" # 时间戳格式化，年月日时分秒

# 输出时间
# -d的基本用法：
# date -d "string"

date -d "yesterday"
date -d "now"
date -d "next friday"
date -d "last month"
date -d "2 weeks ago"
# 格式化输出
date -d "2024-01-01" +"%Y-%m-%d"
date -d "next year" +"%A, %d %B %Y"
# 时间计算
date -d "-3 day" +%F

# 修改时间
# date -s "string"

date -s "-1day"
date -s "-1year"
``````



#### 使用`date -s`时间修改失败的原因

![image-20241128163600922](C:\Users\31403\AppData\Roaming\Typora\typora-user-images\image-20241128163600922.png)

``````bash
将NTP service改为inactive即可
timedatectl set-ntp false
``````





### 硬件时间

#### 主板上的BIOS时间

``````bash
clock # 显示系统时钟

hwclock # 显示硬件时钟
``````



#### 硬件时钟和系统时钟的区别和含义

- 硬件时间
  - 物理设备
    - 硬件时钟是计算机主板上的一个实际的物理设备，有时被称为 CMOS 时钟。
  - 独立供电
    - 它通常由一个小电池供电，这意味着即使计算机断电或关闭，硬件时钟也会继续运行。
  - 持久性
    - 硬件时钟保存了日期和时间信息，并在系统启动时提供给操作系统。这个时间通常在计算机启动时由 BIOS 或 UEFI 读取
  - 精度
    - 硬件时钟的精度相对较低，可能会因电池老化或其他原因逐渐偏离准确时间。



#### 对钟

``````bash
hwclock -s | --hctosys  # 以硬件时钟为准，校正系统时间

hwclock -w | --sysohc   # 以系统时钟为准，矫正硬件时间
``````



### 设置时区

``````bash
timedatectl list-timezones  # 列出所有时区

timedatectl set-timezone <时区> #设置时区
# 示例：timedatectl set-timezone Asia/Shanghai
``````



### 显示日历

``````bash
# Ubuntu下载 apt install -y ncal
# Rocky不用下载

cal

cal 2 2024 # 显示指定月份日历

cal 2024 # 显示指定年份的12个月的所有日历
``````



## 会话管理

### screen

``````bash
# 启动并命名一个screen会话
screen -S session_name

# 分离(Detach)当前会话
Ctrl + A, D

# 列出所有会话
screen -ls

# 重新连接到一个会话
screen -r session_name
screen -r session_id

# 创建窗口
Ctrl + A, C

# 查看所有窗口
Ctrl + A, "

# 切换窗口向下
Ctrl + A, N

# 切换窗口向上
Ctrl + A, P

# 重命名窗口
Ctrl + A, A

# 关闭当前窗口
exit

# 强制关闭会话
screen -X -S session_name quit

# 上下切分窗口（不好用，不推荐，会卡）
Ctrl + A, S

# 移动到新的分屏
Ctrl + A, Tab

# 在分屏中启动新的会话
Ctrl + A, C

# 关闭分屏窗口
Ctrl + A, Q
``````



### Tmux

``````bash
# 安装tmux
wget https://www.mysticalrecluse.com/script/Shell/tmux_seting.sh
bash tmux_seting.sh

# 常见用法
# 新建会话
tmux new -s hdcms
# 查看会话
ctrl+b s
# 重命名会话
Ctrl+b $

# 退出会话
Ctrl+b D

# 列出会话
tmux ls
tmux attach -t session_name

# 创建窗口
Ctrl+b c

# 关闭当前窗口
Ctrl+b x

# 移动窗口
# 向前移动
Ctrl+b p

# 向后移动
Ctrl+b n

#  给窗口重命名
Ctrl+b ,

# 查看所有窗口
Ctrl+b w

# 分屏操作
# 上下分屏
Ctrl+b "

# 左右分屏
Ctrl+b %

# 切换面板
Ctrl+b o

# 将当前屏幕放大
Ctrl+b z

``````



## Linux目录结构

- 文件系统的目录结构

  - bin：给普通用户使用的工具(二进制可执行文件)

  - boot：开启启动的文件，包含linux内核
    - linux内核：`vmlinuz-5.14.0-284.11.1.el9_2.x86_64`
    - grub,开机引导加载程序

  - dev：硬件设备，比如：硬盘

  - etc：类似于注册表，核心！各种配置文件

  - home：用户的数据，各个用户在家目录

  - root：root用户的家目录

  - run：运行过程中生成的临时文件

  - sbin：给管理员使用的工具

  - sbin：给管理员使用的工具（二进制可执行文件）

  - tmp：临时文件

  - usr：操作系统下自带的文件，大多在usr

  - var：网页文件，日志等不断会变化的文件

  - lib/lib64:库文件，很多应用程序共同依赖的库文件

  - mnt/media：实现外围设备的挂载用的

  - proc/sys：内存中的数据

  - opt/srv：外部下载的一些程序软件，如果不下载的话，一般为空

  - proc/sys：内存中的数据，虚拟文件系统，内存映射到硬盘的数据

  - opt：外部下载的一些程序软件，如果不下载的话，一般为空

  - srv：系统上运行的服务用到的数据



## 文件类型

- 概述：
  - 磁盘中存放的每个文件可以分为两个部分
    - 一部分为文件的内容：即文件的数据部分，此部分内容存放在磁盘中专门的数据空间(data block)中。
    - 一部分为文件的属性信息，即元数据(meta data)，比如；文件的大小，类型，节点号，权限，时间等，此部门内容存放在磁盘中专门的节点空间(inode block)中

- 普通文件（白色）
  - 纯文本文件：
    - `ls -l /etc/issue`
  - 二进制可执行文件（绿色）：
    - 概述：二进制可执行文件是有特殊格式的可执行程序，其文件内容表现为不可直接读懂的字符，用cat查看，会出现乱码。在Linux中有很多二进制可执行文件，比如很多的外部命令都是二进制可执行文件
    - `ls -l /bin/cat`
  - 数据格式文件
    - 概述：数据格式文件是一些程序在运行过程中需要读取的存放在某些特定格式的数据文件，比如：图片文件，压缩文件，日志文件。通常需要特定的工具打开
    - 举例：用户登录时，系统会将登录的信息记录在/var/log.wtmp文件中，这个就是一个数据文件。需要使用`last`命令打开此文件查看内容
    - `ls -l /var/log/wtmp` -> `last`(直接在/var/log目录下使用last命令)

- 目录文件（蓝色）
  - 概述：目录文件即文件夹，通过`ls -l`查看文件属性时，第一个属性表现为d

- 链接文件（浅蓝色）
  - 概述：即将两个文件建立关联关系，这种操作实际上是给系统中已有的某个文件指定另外一个可用于访问它的不同文件名称。
  - `ls -l`查看文件属性时，第一个属性表现为l
  - 分类：
    - 硬链接
    - 软链接
    - 关于硬链接和软链接的区别和定义，后面详解

- 管道文件（暗黄色）
  - 概述：管道pipe文件是一种特殊的文件类型，其本质是一个伪文件（本质是内核缓冲区）。其主要目的是实现进程间通讯的问题。由于管道文件是一个与进程没有“血缘关系”的，真正独立的文件，所以它可以在任意进程之间实现通信。
  - 局限性：
    - 自己写的数据不能自己读
    - 数据一旦被读后，便不在管道中存在，不可反复读取
    - 管道采用半双工通信方式
  - `ls -l`查看文件属性时，第一个属性表现为p
  - FIFO: 队列的数据结构，先进先出
  - 更多细节后续详解

- 字符设备文件（明黄色）
  - 通常是一些串行接口设备在用户空间的体现，像键盘、鼠标。字符设备是按字符为单位进行输入输出的，且按一定的顺序进行
  - `ls -l`查看文件属性时，第一个属性表现为c
  - 举例；我们登录到Linux主机，系统会提供一个终端文件tty供我们登录。

- 块设备文件（明黄色）
  - 块文件设备，就是一些以“块为单位”，如：4096个字节，访问数据，提供随机访问的接口设备，例如磁盘、硬盘、U盘
  - `ls -l`查看文件属性时，第一个属性表现为b

- 套接字文件（粉色）
  - 概述：数据接口文件，通常被用在基于网络的数据通讯使用。
  - 当两个进程在同一台主机上，但是像通过网络方式通信，可基于socket方式进行数据通信，可基于全双工方式实现，即可支持同时双向传输数据。
  - `ls -l`查看文件属性时，第一个属性表现为s



## 文件类型颜色的配置文件

``````bash
# CentOS
/etc/DIR_COLORS

# Ubuntu
Ubuntu 中与颜色设置相关的文件和命令包括：

~/.dircolors 或 ~/.dir_colors:

用户级别的配置文件。如果存在，dircolors 命令会使用这个文件中的配置。如果你想定制自己的颜色配置，可以在你的用户目录中创建这个文件。
/etc/dircolors:

系统级别的默认配置文件。这个文件可能在某些系统中不存在，或者命名可能有所不同。
dircolors 命令:

这个命令用于初始化颜色配置。它会检查 ~/.dircolors 或 ~/.dir_colors 文件，如果这些文件不存在，它会使用默认的颜色配置。你通常会在你的 shell 初始化文件中（比如 ~/.bashrc）看到类似于以下的命令：
test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"

如果你想要调整 Ubuntu 中 ls 命令输出的颜色，你可以创建或编辑 ~/.dircolors 文件，并在该文件中定义你的颜色配置。然后，确保你的 shell 初始化文件（如 ~/.bashrc）中包含处理 dircolors 的命令。这样，每次你打开一个新的 shell 时，都会应用这些颜色设置。
``````



## 管理目录类文件相关命令

- 查看当前目录

  - 命令：`pwd`

  ``````bash
  pwd -P # 输出真实物理路径
  pwd -L # 默认，输出链接路径
  ``````

  

- 基名与文件名

``````bash
bashename <dir> #只输出文件名
# 示例：
basename `which cat`

dirname <dir>  # 只输出路径
# 示例：
dirname `which cat`
``````



- 路径间移动
  - 命令：`cd`

``````
cd -P  # 移动到真实物理路径
# 示例
cd -P /bin  # 实际移动到/usr/bin

cd ~  # 移动到家目录
cd ~username  # 移动到指定用户的家目录

cd -  # 移动到上次所在的目录，之所以能移动到上次所在目录是因为有系统变量记录了这个数据
# $OLDPWD 记录上次所在目录；$PWD 记录当前所在目录
``````



- 查看目录
  - 命令: `tree`

``````bash
# 查看指定目录数的层级
tree -L 1 /


# 每个文件和目录前显示完整的相对路径
tree -f
[Sun Oct 15 10:08:22 7] root@rocky9:~ #tree -f /Storage/
/Storage
└── /Storage/test
    ├── /Storage/test/baidu.html
    ├── /Storage/test/ps_demo.txt
    ├── /Storage/test/rename.txt
    └── /Storage/test/robots.txt

1 directory, 4 files


1 directory, 4 files

# 每个文件和目录前显示最新更改时间
tree -D
[Sun Oct 15 10:10:36 11] root@rocky9:~ #tree -D /Storage/
/Storage/
└── [Oct 14 09:12]  test
    ├── [Sep 27 12:03]  baidu.html
    ├── [Oct 13 20:48]  ps_demo.txt
    ├── [Jan  3  2020]  rename.txt
    └── [Jan  3  2020]  robots.txt

1 directory, 4 files


1 directory, 4 files

# 每个文件和目录前显示文件大小
tree -s
[Sun Oct 15 10:08:30 8] root@rocky9:~ #tree -s /Storage/
/Storage/
└── [         79]  test
    ├── [       2381]  baidu.html
    ├── [        270]  ps_demo.txt
    ├── [       2814]  rename.txt
    └── [       2814]  robots.txt


# 每个文件和目录前显示文件/目录拥有者
tree -u
[Sun Oct 15 10:09:28 9] root@rocky9:~ #tree -u /Storage/
/Storage/
└── [root    ]  test
    ├── [root    ]  baidu.html
    ├── [root    ]  ps_demo.txt
    ├── [root    ]  rename.txt
    └── [root    ]  robots.txt


# 每个文件和目录前显示权限标示
tree -p
[Sun Oct 15 10:11:18 12] root@rocky9:~ #tree -p /Storage/
/Storage/
└── [drwxr-xr-x]  test
    ├── [-rw-r--r--]  baidu.html
    ├── [-rw-r--r--]  ps_demo.txt
    ├── [-rw-r--r--]  rename.txt
    └── [-rw-r--r--]  robots.txt


# 使用通配符对tree的目录进行筛选
tree -P pattern 这里的pattern不支持正则表达式，仅支持通配符
[Sun Oct 15 10:33:09 26] root@rocky9:~ #tree -P 'r*.txt' /Storage/
/Storage/
└── test
    ├── rename.txt
    └── robots.txt

1 directory, 2 files


1 directory, 2 files

常用通配符:
* 匹配任意数量的字符（包括零个）。
? 匹配任意一个字符。
[...] 匹配方括号中的任意一个字符。
``````



- 创建目录
  - 命令：`mkdir`

``````bash
语法格式：mkdir [pv] [-m mode] directory_name...

# mkdir在指定路径创建目录
mkdir /Storage/test   # 在Storage目录下创建一个test目录

# 默认在当前路径创建目录
mkdir dir1    # 在当前目录下创建名为dir1的目录

# 一次创建多个同级目录，每个目录间用空格隔开
mkdir dir1 dir2 dir3

# 创建多级目录
mkdir -p dir1/dir2/dir3


# mkdir在指定路径创建目录
mkdir /Storage/test   # 在Storage目录下创建一个test目录

# 默认在当前路径创建目录
mkdir dir1    # 在当前目录下创建名为dir1的目录

# 一次创建多个同级目录，每个目录间用空格隔开
mkdir dir1 dir2 dir3

# 创建多级目录
mkdir -p dir1/dir2/dir3

# -v 会显示创建每个目录的详细信息 
[Sun Oct 15 11:12:00 39] root@rocky9:/ #mkdir -pv /Storage/test/dir1/dir2/dir3
mkdir: created directory '/Storage/test/dir1'
mkdir: created directory '/Storage/test/dir1/dir2'
mkdir: created directory '/Storage/test/dir1/dir2/dir3'
``````



### 目录的本质

- 在Unix和类Unix的文件系统中，每个文件或目录都有一个与之关联的inode（索引节点）。

- 这个inode包含了关于文件的元数据，例如文件的权限、大小、修改时间、拥有者、所用的数据块的位置等，但注意，<font color=tomato>它不包含文件名</font>。

- 目录中的数据部分，包含了文件名与inode编号的映射关系

  ```
  fileA -> inode34
  fileB -> inode57
  ```

- 因此目录下文件的元数据（非文件名的改变）并不会导致目录中数据部分的内容发生改变，因为：文件元数据的改变，会导致inode的数据部分发生变化，但是inode的编号/值不变。这样，文件名和对应的inode编号的映射关系就没有发生变化，所以目录数据内容无变化

- 目录的大小跟文件大小无关，仅跟目录的数据部门，即目录下文件和inode映射关系的大小有关

#### 创建初始目录的时候，硬链接数初始为2的原因

- 在UNIX和Linux文件系统中，目录的硬链接数从2开始是有特定的原因的。当你创建一个目录（例如dir1），初始的两个硬链接代表：
  - 引用该目录的名字：这就是你所创建的目录名，如dir1。自身是一个硬链接
  - .（点）：每个目录都有一个特殊的名字.，它引用自身。当你进入dir1并列出内容时，你会看到一个.目录，它实际上指向dir1自身。
  - 当你在dir1内创建子目录时，dir1的硬链接数会增加。这是因为每个子目录都有一个名为..（双点）的特殊目录名，它指向其父目录。因此，每当你在dir1内创建一个子目录，dir1的硬链接数就会增加1。



### 管理文件的相关命令

- 查看文件列表

  - 命令：`ls`

  ```shell
  语法格式：ls [OPTION]... [FILE]...
  
  # -a 显示包含隐藏文件在内的所有内容
  ls -a
  
  # -i 显示文件索引节点(inode)
  ls -i 
  [Sun Oct 15 11:39:16 65] root@rocky9:test #ls -i
  136601235 baidu.html  137507906 ps_demo.txt  136601225 rename.txt  136601224 robots.txt
  
  # -l 以长格式显示目录下内容列表
  # 长格式输出信息：文件名、文件类型、权限、硬链接数、所有者、组、文件大小、修改时间
  ls -l
  [Sun Oct 15 11:39:28 67] root@rocky9:test #ls -l
  total 16
  -rw-r--r--. 1 root root 2381 Sep 27 12:03 baidu.html
  -rw-r--r--. 1 root root  270 Oct 13 20:48 ps_demo.txt
  -rw-r--r--. 1 root root 2814 Jan  3  2020 rename.txt
  -rw-r--r--. 1 root root 2814 Jan  3  2020 robots.txt
  
  # 用文件目录的更改时间排序
  ls -t
  [Sun Oct 15 11:45:06 73] root@rocky9:test #ls -tl
  total 16
  -rw-r--r--. 1 root root  270 Oct 13 20:48 ps_demo.txt
  -rw-r--r--. 1 root root 2381 Sep 27 12:03 baidu.html
  -rw-r--r--. 1 root root 2814 Jan  3  2020 rename.txt
  -rw-r--r--. 1 root root 2814 Jan  3  2020 robots.txt
  
  # 按文件大小，从大到小排序
  ls -S
  mystical@mystical 0101 #ll-Sh  
  total 60K
  -rwxrwxr-x 1 mystical mystical  17K Jan  1 23:05 a.out
  -rw-rw-r-- 1 mystical mystical 1.6K Jan  1 22:29 7.struct.c
  -rw-rw-r-- 1 mystical mystical  861 Jan  1 21:12 6.ifdef.c
  -rw-rw-r-- 1 mystical mystical  536 Jan  1 23:05 8.union.c
  -rw-rw-r-- 1 mystical mystical  529 Jan  1 14:49 2.array.c
  -rw-rw-r-- 1 mystical mystical  521 Jan  1 10:47 1.demo.c
  -rw-rw-r-- 1 mystical mystical  445 Jan  1 16:45 3.string.c
  -rw-rw-r-- 1 mystical mystical  404 Jan  1 17:14 4.pointer.c
  -rw-rw-r-- 1 mystical mystical  402 Jan  1 20:53 5.ifdef.c
  -rw-rw-r-- 1 mystical mystical  375 Jan  1 14:55 3.address.c
  -rw-rw-r-- 1 mystical mystical   44 Jan  2 15:00 website.txt
  
  # ls后面支持通配符过滤，不加单引号
  [Sun Oct 15 11:49:26 80] root@rocky9:test #ls -l *.txt
  -rw-r--r--. 1 root root  270 Oct 13 20:48 ps_demo.txt
  -rw-r--r--. 1 root root 2814 Jan  3  2020 rename.txt
  -rw-r--r--. 1 root root 2814 Jan  3  2020 robots.txt
  
  ls -l <file>
  #如果file是目录，则直接查询该目录下的内容，要查询目录使用
  ls -dl <file>
  # 如果file是普通文件，则正常查看list
  
  ```

- 文件的时间属性

  - atime: 记录最后一次的访问时间
    - atime的更新策略：连续在24小时内访问读取atime,24小时内不会更新atime；但在更改文件内容的时候会顺便更新atime
  - mtime: 记录最后一次文件数据部分的修改时间
  - ctime: 记录最后一次文件元数据的修改时间
  - 注意：mtime的改变一定会引起ctime的改变
  - <font color=tomato>对于目录这种特殊文件</font>
    - 其目录文件的数据部分(data block)存放的就是目录中的文件名等信息。所以在目录中创建，删除文件会改变目录的mtime，而目录的mtime的改变一定会引起ctime的改变，但其文件内容的改变，并不会引起目录mtime和ctime的改变
    - 当你访问一个目录（例如列出其内容）时，目录的 atime（访问时间）会被更新。如果你修改了目录中的一个文件，那么在大多数文件系统配置下，为了访问并修改该文件，你首先需要“访问”该目录，从而导致目录的 atime 被更新。所以修改一个目录下的文件，那么这个目录的atime通常情况下，是会更新的。但是...
    - 出于性能原因，一些现代的文件系统或挂载选项可能会默认禁用 atime 的更新。这种设置被称为noatime，它可以减少磁盘I/O，特别是在频繁读取文件但不经常修改它们的系统上。因此，如果<font color=tomato>文件系统</font>是以 noatime 选项挂载的，那么访问文件或目录不会更新其 atime。
  - ls查看文件的3个时间属性

  ```shell
  # 默认显示文件的mtime
  ls -l
  
  # 显示文件的ctime
  ls -l --time=ctime
  
  # 显示文件的atime
  ls -l --time=atime
  ```

  - 关于atime的挂载选项
    - 'noatime'
      - 访问文件/目录不会更新atime
    - 'relatime'
      - 满足两个条件之一才更新atime
        - 文件的atime时间超过一天
        - 文件的mtime比atime更晚

- 查看文件属性信息

  - 命令：`stat`
  - 作用：用于显示文件的详细属性

  ```shell
  语法格式：stat [文件或目录]
  
  # 查看文件属性
  [Sun Oct 15 14:35:09 93] root@rocky9:test #stat rename.txt
  File: rename.txt
  Size: 2814      	Blocks: 8          IO Block: 4096   regular file
  Device: fd00h/64768d	Inode: 136601225   Links: 1
  Access: (0664/-rw-rw-r--)  Uid: (    0/    root)   Gid: (    0/    root)
  Context: unconfined_u:object_r:default_t:s0
  Access: 2023-10-13 20:36:29.807941125 +0800
  Modify: 2020-01-03 16:33:48.000000000 +0800
  Change: 2023-10-15 14:34:30.473235676 +0800
  Birth: 2023-09-27 11:57:14.168869373 +0800
  ```

  - 命令：`file`
  - 作用：使用`file`辨识文件的类型

  ```shell
  语法格式：file [OPTION] file_name
  
  # -i 查看文件的MIME类型
  [Sun Oct 15 14:46:28 102] root@rocky9:test #file -i test.log
  test.log: text/plain; charset=us-ascii
  
  # -b 省略文件名称，直接打印结果
  mystical@ubuntu2204:~/C_coding/2024/jan/0128$ file 1.for.c
  1.for.c: C source, Unicode text, UTF-8 text
  
  mystical@ubuntu2204:~/C_coding/2024/jan/0128$ file -b 1.for.c
  C source, Unicode text, UTF-8 text
  
  # -f 从一个文件中，获取数据进行处理
  mystical@ubuntu2204:~/test$ file -f studyvim.txt
  /bin:        symbolic link to usr/bin
  /etc/passwd: ASCII text
  /home/:      directory
  ```

- windows与unix格式文本之间的相互转换

  - Windows和Unix文本差异：
    - Windows每行末尾是回车符加换行符
    - Unix的每行末尾只有换行符结束
  - 相互转换需要使用dos2unix

  ```Shell
  sudo apt install dos2unix
  # Windows文本格式转Unix
  dos2unix test.txt
  
  # Unix文本格式转Windows
  unix2dos test.txt
  ```

- 创建或刷新文件

  - 命令：`touch`

  ```shell
  # 如果文件存在则刷新时间，如果不存在则创建空文件
  
  touch -a    # 改变atime, ctime
  touch -m    # 改变mtime, ctime
  touch -h    # 刷新链接文件本身，默认刷新目标文件
  touch -c    # 只刷新已存在的文件，如果文件不存在，也不会创建文件 
  touch --time=STRING  # 修改指定时间，如：--time=atime
  touch -r    # 使用某个文件的修改时间作为当前文件的修改时间
  # 改变atime和mtime并刷新ctime
  touch -t    # 修改atime,mtime到指定日期时间
  # 比如01020304，指2024-01-02 03:04:00
  # 比如0102030405， 指2001-02-03 04:05:00
  
  # 示例
  touch `date +%F-%T`.txt
  2024-01-30-18:08:58.txt 
  ```

- 复制文件

  - 命令：`cp`

  ```shell
  语法格式：cp [OPTION] SOURCE DEST
  
  # -b 覆盖已存在的目标前先对其做备份，后缀为~
  [Sun Oct 15 15:03:16 108] root@rocky9:test #cp -b newtest.txt test.log
  cp: overwrite 'test.log'? y
  [Sun Oct 15 15:03:32 109] root@rocky9:test #ls
  baidu.html  dir1  dir2  dir3  newtest.txt  ps_demo.txt  rename.txt  robots.txt  test.log  test.log~
  
  # -S 指定备份文件的后缀名
  [Sun Oct 15 15:10:53 123] root@rocky9:test #cp -S .bak dir1/cptext.txt  cptext.txt 
  cp: overwrite 'cptext.txt'? y
  [Sun Oct 15 15:11:10 124] root@rocky9:test #tree .
  .
  ├── baidu.html
  ├── cptext.txt
  ├── cptext.txt.bak
  ├── dir1
  │   └── cptext.txt
  ├── dir2
  ├── dir3
  ├── dir_cp
  │   └── cptext.txt
  ├── newtest.txt
  ├── ps_demo.txt
  ├── rename.txt
  ├── robots.txt
  ├── test.log
  └── test.log~
  
  4 directories, 11 files
  
  # -i 覆盖前会先询问用户（推荐使用）
  cp -i file cp_file
  
  # -r 递归处理，将目录及其中的为文件一同复制
  cp -r dir cp_dir
  
  # -a 复制特殊文件，使用-a
  cp -a /dev/zero  /home/mystical 
  ```

- 移动及重命名文件

  - 命令：`mv`
    - 语法：`mv 目标文件 目标路径`
    - 语法2：`mv -t 目标路径 目标文件`
    - 语法3：`mv -bi 目标文件 目标路径`
      - i: 如果会覆盖文件则提示
      - b: 覆盖文件时会备份被覆盖的文件

  - 命令：`rename`

  ```shell
  关于批量创建和批量修改文件名
  
  # 批量创建文件与批量重命名
  # rename <要改的字段> <改之后的字段> <使用通配符表示改的程度>
  [Sun Oct 15 15:34:07 129] root@rocky9:py_test #touch pydemo{1..9}.txt
  [Sun Oct 15 15:34:35 130] root@rocky9:py_test #ls
  pydemo1.txt  pydemo2.txt  pydemo3.txt  pydemo4.txt  pydemo5.txt  pydemo6.txt  pydemo7.txt  pydemo8.txt  pydemo9.txt
  [Sun Oct 15 15:34:38 131] root@rocky9:py_test #rename .txt .py *.txt
  [Sun Oct 15 15:35:23 132] root@rocky9:py_test #ls
  pydemo1.py  pydemo2.py  pydemo3.py  pydemo4.py  pydemo5.py  pydemo6.py  pydemo7.py  pydemo8.py  pydemo9.py
  [Sun Oct 15 15:35:25 133] root@rocky9:py_test #rename py python py*
  [Sun Oct 15 15:35:43 134] root@rocky9:py_test #ls
  pythondemo1.py  pythondemo2.py  pythondemo3.py  pythondemo4.py  pythondemo5.py  pythondemo6.py  pythondemo7.py  pythondemo8.py  pythondemo9.py
  
  ```

- 删除文件

  - 命令：`rm`

  ```shell
  语法格式：rm [OPTION]...FILE...
  
  # -f 强制删除文件，即在删除文件时不提示确认，并自动忽略不存在的文件
  # -r 递归删除，目标是目录的话，整个目录文件全部删除
  ```

  - `rm`是危险命令，建议用以下命令替换

  ```
  alias rm='dir=/Storage/backup/data`date +%F%T`;mkdir $dir;mv -t $dir'
  # 将所有要删除的文件，移动到创建的垃圾箱目录中
  ```

### 文件元数据和节点表结构

- 作用：df 命令用于显示文件系统的磁盘空间使用情况

- 查看不同分区的节点编号使用情况

  - 命令：df -i

  ```
  生产案例1：提示空间满NO space left on device，但df可以看到空间很多，为什么
  
  答：
  节点编号不足，一个文件能被创建需要同时满足两个前提
  足够的空间，以及该文件系统下还有剩余的节点编号
  
  生产案例2：为什么cp /dev/zero /boot/test.img会把/boot的空间撑满
  
  答：
  1./dev/zero 是一个特殊的设备文件，它可以生成无限的零字节。当你尝试从它读取数据时，它会持续不断地返回零字节。
  
  2.cp 命令的作用是复制文件或目录。在这种情况下，它从 /dev/zero 复制数据并尝试写入 /boot/test.img。
  
  3.因为 /dev/zero 提供了无限的零字节，cp 会持续写入数据到 /boot/test.img，直到 /boot 分区没有更多的空间可用。
  
  生产案例3：当test.img被访问时，管理员在主服务器删除test.img后，为什么，空间依然是满的
  
  答：
  因为当一个文件被使用时，在另一侧删除该文件，该空间并不会被立即释放，只有当这个文件不被使用时，才会释放这个空间
  
  解决方法：
  cat /def/null > /boot/test.img; rm -rf /boot/test.img
  把文件清空后删除即可、
  echo -n '' > /boot/test.img 结果和上述cat /def/null...相同
  ```

### 硬链接与软链接

- 硬链接：
  - 概述：本质上是多个文件名共用一个inode
  - 命令：`ln a.txt aa.txt`
  - 注意：
    - 因为本质是共用一个inode，所以不能跨分区创建硬链接，因为不同分区有独立的inode表
    - 同理，为了防止inode循环利用，所以目录也不能创建硬链接，但是在创建目录及其子目录的时候，系统会自动创建.和..这种目录的硬链接
    - 硬链接数本质上是inode计数器的值

- 软链接：
  - 概述：也叫符号链接，软链接的本质是创建了一个新文件，该文件的内容是源文件的路径，所以访问软连接文件，实质上系统访问指向了源文件
  - 命令：`ln -s 目标文件 软链接文件`
    - 注意：根据软链接的本质，软连接文件中的内容实际上是指向目标文件的路径，因此目标文件的路径如果是相对路径，那么一定是相对软链接的路径 
    - 注意2：删除软链接的时候，不要加tab键补全，如果软连接文件后跟/,删除的时候，比如rm -rf /Storage/test/test/ 实际上是把原始目录中的内容一起删除



## Inode

``````C
struct inode {
    umode_t i_mode;                 // 文件的类型和权限（如文件、目录、符号链接等）
    unsigned short i_opflags;
    kuid_t i_uid;                   // 文件的用户 ID（所有者）
    kgid_t i_gid;                   // 文件的组 ID（所属组）
    unsigned int i_flags;
    struct timespec64 i_atime;      // 最后访问时间
    struct timespec64 i_mtime;      // 最后修改时间
    struct timespec64 i_ctime;      // 元数据最后修改时间
    unsigned int i_nlink;           // 硬链接数
    blkcnt_t i_blocks;              // 分配给该文件的块数
    loff_t i_size;                  // 文件的大小（字节）
    
    struct super_block *i_sb;       // 指向超级块的指针
    struct address_space *i_mapping;// 关联文件数据的地址空间
    // ... 其他成员
};
``````

- inode 是一个数据结构，它包含了多种信息，包括文件的元数据和指向数据块的指针。因此，inode 的主要作用是管理文件的元数据，而不仅仅是指向文件的物理位置。
- node 中包含多个指针：inode 中包含了多个指向磁盘上数据块的指针，用来定位文件的实际内容。文件的大小决定了需要多少个数据块来存储文件内容，而 inode 结构中的指针帮助文件系统找到这些数据块



### 如何通过inode查找文件位置

当文件系统需要访问文件内容时，它首先会通过目录项找到文件名对应的 inode 号。然后，文件系统通过 inode 号找到对应的 inode 结构，接着通过 inode 中存储的指针找到文件实际存储的磁盘块。这个过程包括以下几个步骤：

- inode 是数据结构：inode 包含了文件的元数据和指向文件数据块的指针，而不仅仅是一个指向数据块的引用。
- 指针是单一的地址引用：指针通常只是一个地址，指向某个特定的内存位置或磁盘位置。而 inode 是一个数据结构，包含多个指针来管理和访问文件的多个数据块。



### 目录项

目录项是指文件系统中记录文件或子目录名称与其对应的文件控制块（如 inode）之间关系的数据结构。目录本质上也是一种文件，其内容就是多个目录项的集合

目录项包含的信息：

- 文件名：文件或子目录的名称。
- 文件控制块的引用：通常是文件的 inode 号（或其他系统实现中的文件控制块标识符）。

目录项的本质

- 在 Unix/Linux 文件系统中，目录的内容实际上是一个包含文件名和 inode 号的表。例如，目录 /home/user 的内容可能包含 file1.txt、file2.txt 的文件名及其对应的 inode 号。

```rust
file1.txt -> inode 12345
file2.txt -> inode 67890
```

目录项的作用

- 文件名与文件控制块的映射：目录项实现了文件名到文件控制块（如 inode）的映射。当用户在某个目录下操作文件时（如打开、修改文件），操作系统会通过目录项查找到文件名对应的文件控制块，再根据文件控制块中的信息进行具体操作。
- 层次结构的组织：目录项使得文件系统可以形成层次化的目录结构（如 /home/user/file1.txt），使文件的组织和访问更加有序和高效。
- 硬链接：在 Unix 系统中，多个目录项可以指向同一个文件控制块（inode），这就实现了所谓的 硬链接。例如，文件 file1.txt 可能存在于 /home/user/ 和 /tmp/ 目录下，而它们实际上指向同一个 inode。这样，删除其中一个目录项并不会删除实际的文件数据，只有当所有指向该 inode 的目录项都被删除时，文件数据才会被清除。



### Inode表

每当在文件系统中创建一个新文件或目录时，文件系统会在 inode 表 中分配一个 inode，并为该文件生成一个 inode 结构体，存储该文件的元数据。这些 inode 是在 文件系统初始化时（通常是格式化时）预留的，保存在磁盘上的 inode 表中。
详细过程

- 文件系统初始化（格式化）：
  - 当文件系统（如 ext4）被初始化或格式化时，文件系统会在磁盘上划分出一定的空间，用来存储 inode 表。
  - inode 表中的 inode 数量是有限的，是在文件系统创建时确定的。例如，如果你创建一个文件系统并指定 10,000 个 inode，那么这个文件系统最多只能支持 10,000 个文件或目录（即使磁盘空间没有用完）。
  - inode 表会被分配固定大小的空间。例如，一个 inode 大约占用 128 或 256 字节，这取决于文件系统的配置。格式化时会计算 inode 表所需的空间，并在磁盘上预留这些空间。

- 创建文件时的 inode 分配：
  - 每当你创建一个新文件或目录时，文件系统会从 inode 表中分配一个空闲的 inode，用于存储该文件的元数据。
  - inode 分配后，文件系统会将文件的相关元数据（如权限、所有者、时间戳、数据块指针等）填入该 inode，并更新文件系统的目录项，将文件名与该 inode 关联。
  - 随着文件的增加，inode 表中的空闲 inode 逐渐减少；一旦 inode 耗尽，文件系统将无法创建新文件或目录，尽管磁盘上可能还有剩余空间。

- inode 表的有限性：
  - inode 表在文件系统创建时确定大小，之后通常不可动态调整。这意味着文件系统可以存储的文件数量受限于 inode 数量，而不仅仅是磁盘容量。
    对于存储大量小文件的场景，inode 数量可能比磁盘容量更早耗尽。因此在格式化文件系统时，可以通过调整 inode 数量来优化文件系统的使用。
  - 

### 索引块

一个索引块里面包含着一个索引表，这个索引表是一个数组，每个元素使指向物理块的指针,这个指针可能指向

索引分配允许文件离散地分配在各个磁盘块中，系统会为每个文件建立一张索引表`，索引表中记录了文件的各个逻辑块对应的物理块（建立逻辑块和物理块之间的映射关系）。

存放索引表的磁盘块称为索引块。存放文件数据的磁盘块称为数据块

inode 是一个结构体，所有的 inode 被存放在 inode 表中，而 inode 位图用于管理 inode 表的使用状态，指示哪些 inode 是空闲的、哪些被占用。



### 文件创建的整体工作流程

- 创建文件时：
  - 文件系统查找 inode 位图，找到一个空闲的 inode（位图中的某位为 0）。
  - 在 inode 表中找到相应位置的 inode 条目，并在其中写入新文件的元数据。
  - 将 inode 位图中的相应位置设置为 1，表示该 inode 已被使用。

- 访问文件时：
  - 文件系统根据文件的路径找到对应的 inode 号。
  - 在 inode 表中找到该 inode 条目，并读取其中的元数据和数据块指针，访问文件内容。