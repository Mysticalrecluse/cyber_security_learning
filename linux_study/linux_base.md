# LINUX 基础
## Linux文件基本操作
### 登录前提示
```bash
/etc/issue # 里面的内容会在登录前出现在终端加载页面
```
### 编辑用户展示公告（登录后提示）
- 概述：
  - /etc/motd 文件的全称是 "Message of the Day"（当日消息）。在Linux和Unix系统中，这个文件的内容会在用户登录到系统后显示在他们的终端上。这为系统管理员提供了一个简单的方法来为登录到系统的用户展示公告、重要消息或任何其他信息。
  - 配置文件
  ```bash
  /etc/motd
  ```
- 在VIM中输出彩色字体
  - 步骤：
  ```
  1. 打开一个新的或现有的 Vim 编辑器：vim filename
  2. 按下 i 进入插入模式。
  3. 按 Ctrl+V 进入 Vim 的特殊字符插入模式。
  4. 接着按 Ctrl+[。这会插入一个 ^[，这实际上是一个转义字符。
  5. 然后直接输入 [32;1m。
  6. 继续输入你的文本，如：Hello, Welcome To My Home - Mystical。
  7. 然后再次按 Ctrl+V 和 Ctrl+[ 插入另一个转义字符。
  8. 接着输入 [0m 来结束彩色输出。
  ```
  - 示例：
  ```shell
  ^[[32;1mHello, Welcome To My Home - Mystical^[[0m
  ```
### Prompt提示符
```shell
# 格式如下：
PS1="提示符格式命令"

# 格式命令如下：
\[  <提示符样式>  \]  # 这个提示符样式外的\[ \] 可以省略

# 提示符样式如下：
\e[ 样式 + 内容 \e[0m # 以 \e[ 开始，\e[0m 表示关闭设置

# 样式分3部分
格式：F;B;Sm
F: 表示前景色
30 黑色，31 红色，32 绿色，33 黄色，34 蓝色，35 紫色，36 青色，37 白色

B：表示背景色，背景色数值 = F + 10

S：显示的样式如下
0：表示关闭颜色设置
1：表示粗体
4：表示加下划线
5：表示闪烁
7：表示前景色，背景色互换
8：表示隐藏

# 内容：
\u: 表示当前用户
\h: 表示主机名简称
\W: 表示当前工作目录基名
\$: 表示提示符(普通用户$ root用户#) 实测在rocky9不好用
\H: 表示完整主机名
\w: 表示完整工作路径
\t: 表示24小时时间格式为：时：分：秒
\A: 表示24小时时间格式为：时：分
\#: 表示开机命令历史数
\d: 表示日期，格式为：星期 月 日
\v: 表示BASH的版本信息
```
```shell
示例：
PS1="PS1="\e[32;40;1m[\d \t \e[31;40;1m\#] \e[33;40;1m\u@\h:\W \$\e[0m""
注意：
实测\$不好用，可以直接在root的目录下的.bashrc文件中改为#
```
### 查看用户登录信息
- whoami命令：显示当前登录有效用户
- who命令：显示当前所有的登录会话
- w：显示系统当前所有的登录会话及其所做的操作
```shell
[Fri Oct 13 22:16:15 59] root@rocky9:/ #w
 22:20:10 up 1 day,  4:39,  2 users,  load average: 0.00, 0.00, 0.00
USER     TTY        LOGIN@   IDLE   JCPU   PCPU WHAT
root     pts/0     21:40    0.00s  0.07s  0.00s w
root     pts/1     21:56    7:22   0.03s  0.01s vim ps_demo.txt

```
### 操作系统版本
- 查看操作系统版本的配置文件
```bash
/etc/os-release  # 操作系统详细信息

/etc/redhat-release  # 操作系统版本
```
- 扩展
  - 可以在字符串中直接添加shell命令运行结果
  ```bash
  echo `cat /etc/redhat-release ` is OS-Version
  ```

### 显示模式切换
- 查看显示模式
```bash
runlevel
```
- 切换显示模式
```bash
init 3 # 切换到字符界面

init 5 # 切换到图形化界面
```

### 设置主机名hostname
- 配置文件
```bash
/etc/hostname
```
- 注意：主机名不要使用下划线
```bash
# 临时设置主机名
hostname 新主机名 
```
- ubuntu直接通过命令修改hostname配置文件
```bash
hostnamectl set-hostname ubuntu1804.magedu.org
```


### 显示字符echo
- 说明：echo会将字符串显示在标准输出即屏幕上。
- 语法：echo [SHORT-OPTION] [STRING]
- SHORT-OPTION说明：
  - -n: 不自动附加换行符；即都在一行显示
  - -e: 启用转义符，能使用转义符\
- 注意：echo后面的字符串建议用单引号括住
```shell
echo -e hello\nworld   # 显示hellonworld
echo -e 'hello\nworld' # 此时转义符生效，符合预期
```

### 命令分类
- 判断命令的类别
```shell
# 使用type命令

[Sat Oct 14 08:04:11 4] root@rocky9:~ #type type
type is a shell builtin 
# 出现这个提示，即可判断该命令是内部命令，type本身也是一个内部命令

[Sat Oct 14 08:04:21 5] root@rocky9:~ #type hostname
hostname is /usr/bin/hostname
# 上述提示，即可判断hostname是外部命令
```
- 内部命令
  - 概述：指集成在特定shell中的命令，当用户登陆时，会自动启用shell，而对应的shell程序中包含一些常见工具。默认的/bin/bash shell中就集成了很多内部命令，可以通过enable命令查看所有内部命令
  ```shell
  # 通过enable命令查看所有内部命令
  [Sat Oct 14 08:07:33 8] root@rocky9:bin #enable
  enable .
  enable :
  enable [
  enable alias
  enable bg
  enable bind
  enable break
  enable builtin
  enable caller
  enable cd
  enable command
  enable compgen
  enable complete
  enable compopt
  enable continue
  enable declare
  enable dirs
  enable disown
  enable echo
  enable enable
  enable eval
  enable exec
  enable exit
  enable export
  enable false
  enable fc
  enable fg
  enable getopts
  enable hash
  enable help
  enable history
  enable jobs
  ...
  ```
- 外部命令
  - 概述；所谓外部命令，就是没有集成在shell程序中。具体表现为一个独立的可执行文件。所以外部命令都能在磁盘中找到对应文件
  - 系统查找外部命令的方式：
    - 在系统中有一个叫PATH的变量，里面保存外部命令存放的路径。具体路径可以通过下面命令查看，当执行一个外部命令时，系统会按PATH中存放的目录路径顺序来查找，一旦在某个目录中找到，就停止继续往下找，并执行此外部命令
  ```
  [Sat Oct 14 08:15:25 9] root@rocky9:bin #echo $PATH
  /root/.local/bin:/root/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin
  ```
  - 查看外部命令存放路径
    - which
    - whereis：除了命令外，还显示和命令相关的帮助文档等文件路径
  ```shell
  [Sat Oct 14 08:21:50 29] root@rocky9:bin #which gcc
  /usr/bin/gcc

  [Sat Oct 14 08:23:59 30] root@rocky9:bin #whereis gcc
  gcc: /usr/bin/gcc /usr/lib/gcc /usr/libexec/gcc /usr/share/man/man1/gcc.1.gz /usr/share/info/gcc.info.gz
  ```
  - 当第一次执行外部命令后，系统会自动将外部的路径记录到内存缓存区中，下次再执行此外部命令，将会从缓存区中找到路径，直接到对应的磁盘路径找到此命令并执行。通过hash命令可以查看到已执行过的外部命令及路径
  ```shell
  [Sat Oct 14 08:24:24 31] root@rocky9:bin #hash
  hits	command
   7	  /usr/bin/ls
   3	  /usr/bin/whereis
  ```
- 别名
  - 概述：所谓别名，就是将一些常用的内部或外部命令，起一个较短的名称，这样每次执行这些常用命令时，就可以用别名替代
  - 管理和查看别名
  ```shell
  # 查看所有别名
  $ alias

  # 查看指定别名
  $ alias 别名

  # 定义别名
  $ alias 别名="命令"

  # 取消别名
  $ unlias 别名
  ```
  - 上述命令都是使别名临时生效，如果要使别名永久生效，需要写入配置文件(.bashrc)中
    - 仅对当前用户有效，写入 ~/.bashrc
    - 对所有人有效，写入 /etc/.bashrc
    - 启用配置文件
      - `source 文件名` 或 `. 文件名`
  - 执行和别名相同的命令时，需要 `\别名` 或`'别名'`

### 命令的使用帮助
- Whatis-查看命令简要说明
  - 概述：Whatis可以快速查看到命令或相关内容的简短功能
  - 注意：在使用`whatis`之前，需要先使用`mandb`创建数据库

- 内部命令的使用帮助
  - `help COMMAND`

- 外部命令的使用帮助
  - `COMMAND --help` | `COMMAND -h`

- man帮助
  - 大部分命令对应的手册通常存储在/usr/share/man里，几乎每个外部命令都有man手册
  - man命令的配置文件
    - `/etc/man_db.conf`
  - man命令的语法格式
  ```shell
  man 命令语法格式；
  man [section] WORD
  格式说明：
  section: 表示1-9的章节数
  1 - 用户命令
  2 - 系统调用
  3 - C库调用
  4 - 设备文件及特殊文件
  5 - 配置文件格式
  6 - 游戏
  7 - 杂项
  8 - 管理类命令
  9 - Linux内核API

  WORD：查看帮助的关键字，如：命令，文件名，函数名

  man -f COMMAND
  # 如果有多个相同的命令的话，可以使用-f分别进行查看
  # 比如查看C语言的printf和bash命令的printf
  ```
### Linux目录结构
- 文件系统的目录结构
  - bin：给普通用户使用的工具
  - boot：开启启动的文件，包含linux内核
    - linux内核：`vmlinuz-5.14.0-284.11.1.el9_2.x86_64`
  - dev：硬件设备，比如：硬盘
  - etc：类似于注册表，核心！各种配置文件
  - home：用户的数据，各个用户在家目录
  - root：root用户的家目录
  - run：运行过程中生成的临时文件
  - sbin：给管理员使用的工具
  - tmp：临时文件
  - usr：操作系统下自带的文件，大多在usr
  - var：网页文件，日志等不断会变化的文件
  - lib/lib64:库文件，很多应用程序共同依赖的库文件
  - mnt/media：实现外围设备的挂载用的
  - proc/sys：内存中的数据
  - opt/srv：外部下载的一些程序软件，如果不下载的话，一般为空

### 文件类型
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

### 管理目录类文件相关命令
- 查看目录
  - 命令: `tree`
  ```shell
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

  常用通配符:
  * 匹配任意数量的字符（包括零个）。
  ? 匹配任意一个字符。
  [...] 匹配方括号中的任意一个字符。
  ```

- 创建目录
  - 命令：`mkdir`
  ```shell
  语法格式：mkdir [pv] [-m mode] directory_name...

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

  # -m mod 指定创建文件的权限
  [Sun Oct 15 11:19:39 45] root@rocky9:demo #mkdir -m 644 demo2
  [Sun Oct 15 11:20:12 46] root@rocky9:demo #ll
  total 0
  drwxr-xr-x. 2 root root  6 Oct 15 11:19 demo1
  drw-r--r--. 2 root root  6 Oct 15 11:20 demo2
  drwxr-xr-x. 3 root root 18 Oct 15 10:43 dir1
  ```

- 删除目录
  - 命令：`rmdir`
  - 注意：用于删除空目录，此命令要删除的目录内，不能有文件存在
  ```shell
  # 删除单一目录，注意：删除目录内不能有文件
  rmdir <dirctory_name>

  # 同时删除同级多个目录，每个目录用空格隔开
  rmdir dir1 dir2 dir3

  # -p 删除多级目录
  rmdir -p dir1/dir2/dir3  # 同时删除dir1及其子目录dir2,dir3
  ```
#### 目录的本质
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

  # ls后面支持通配符过滤，不加单引号
  [Sun Oct 15 11:49:26 80] root@rocky9:test #ls -l *.txt
  -rw-r--r--. 1 root root  270 Oct 13 20:48 ps_demo.txt
  -rw-r--r--. 1 root root 2814 Jan  3  2020 rename.txt
  -rw-r--r--. 1 root root 2814 Jan  3  2020 robots.txt

  ```

- 文件的时间属性
  - atime: 记录最后一次的访问时间
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

  ```

- 创建文件
  - 命令：`touch`

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

  ```

- 移动及重命名文件
  - 命令：`mv`
    - 语法：`mv 目标文件 目标路径`
    - 语法2：`mv -t 目标路径 目标文件`
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

  # -i 在删除每个文件之前请求确认

  # -r 递归删除，目标是目录的话，整个目录文件全部删除
  ```
  - `rm`是危险命令，建议用以下命令替换
  ```shell
  alias rm='dir=/Storage/backup/data`date +%F%T`;mkdir $dir;mv -t $dir'
  # 将所有要删除的文件，移动到创建的垃圾箱目录中
  ```

### 文件元数据和节点表结构
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


## Bash Shell特性
### 命令历史
- 概述：
- 使用bash shell,执行过的命令会记录到history对应的缓存区中。当用户注销时，会将history缓存区中的命令历史追加到`~/.bash_history`文件中。
- 当下次登录shell时，系统会读取命令历史文件中记录的命令到命令缓存区。

### history命令
```shell
# 语法：
history -c  
# 清空历史命令，仅清空命令缓存区的命令，不影响.bash_history

history -d offset
[Tue Oct 17 10:52:59 22] root@rocky9:~ #history | tail -n 10
 1011  cat .bash_history 
 1012  cat oldfile.txt 
 1013  getent passwd root
 1014  getent passwd | tail -n 10
 1015  getent passwd
 1016  history
 1017  history -d 999
 1018  history | tail -n 20 # 1018
 1019  history | tail -n 30
 1020  history | tail -n 10
[Tue Oct 17 10:54:14 23] root@rocky9:~ #history -d 1017
[Tue Oct 17 10:54:35 24] root@rocky9:~ #history | tail -n 10
 1012  cat oldfile.txt 
 1013  getent passwd root
 1014  getent passwd | tail -n 10
 1015  getent passwd
 1016  history
 1017  history | tail -n 20 # 1017
 1018  history | tail -n 30
 1019  history | tail -n 10
 1020  history -d 1017
 1021  history | tail -n 10

# 删除命令缓存区中指定编号的历史命令
# 删除后，后面的命令编号会依次往前提

history n  # 显示最近的n条命令，等同于history|tail -n <num>

history -a # 立即追加命令缓存区中的命令到历史文件中

history -w # 将命令缓存区的当前内容覆盖到.bash_history文件。
history -w <new_file> # 将命令缓存区中的内容存储到指定文件中

history -r # 从.bash_history读取命令到命令缓存区，通常在开始新会话时使用。
history -r <new_file> # 从指定文件中读取命令到缓存区

history -p <指定历史命令> # 将指定的数据显示在标准输出
# 输出的指令不会执行，也不会出现在历史缓存区中
[Tue Oct 17 14:13:14 50] root@rocky9:Storage #history
    1  ls
    2  touch test2.txt
    3  echo "hello" >> test2.txt 
    4  cat test2.txt 
    5  history
[Tue Oct 17 14:13:22 51] root@rocky9:Storage #history -p \!-2
cat test2.txt 

history -s # 将参数作为单独的条目添加到历史列表的末尾。
# 这允许你将一个或多个命令手动添加到历史记录中。
history -s "echo hello" # 将echo hello加入历史缓存区，但是不会执行

```

- 详细描述数据在历史缓冲区和.bash_history的过程
  - 在一个新的bash会话中开始时，.bash_history 文件中的历史命令会被加载到命令缓存区。(假设.bash_history初始没有数据)
  - 执行了10个bash命令。
  - 退出bash，这10个命令写入到 .bash_history
  - 开始一个新的bash会话，这10个命令加载到命令缓存区。
  - 新的bash会话中，你执行了一个新的命令
  - 退出bash，命令缓存区中的11个命令会 替换 .bash_history 文件中的内容。
  - 最终.bash_history中共有11条命令

- 问题2：`history -a`的原理
  - 纯粹从底层操作角度看，history -a是追加到文件的，不是覆盖。
  - 当我们在日常使用中考虑整个会话的上下文时，情况会变得复杂。每当开始一个新的bash会话，它都会从.bash_history读取历史记录到命令缓存区。这意味着，命令缓存区现在包含了从.bash_history文件加载的命令加上在当前会话中输入的新命令。
  - 所以，尽管history -a实际上是追加行为，但在一个常规的bash会话中，由于命令缓存区已经从.bash_history加载了历史，看起来就像是被覆盖了。
  - 但就底层原理来说：尽管history -a实际上是追加行为，但在一个常规的bash会话中，由于命令缓存区已经从.bash_history加载了历史，看起来就像是被覆盖了(真正的覆盖操作是history -w)。

- 命令历史的快捷方式使用
  - `!` 历史扩展的开始标识符。
    - 在配合`history -p`使用时，需要使用`\!`转义
    - `!!` 重复执行前一个命令
    - `!:0` 执行前一个不含参数的命令
    - `!n` 执行缓冲区序号n的命令
    - `!-n` 执行缓冲区序号倒数第n个命令
    - `!string` 执行前一个以string开头的命令
    - `!?string` 执行前一个包含string的命令
    - `:p`打印命令，不执行
      - `!string:p`
      - `!$:p` 打印输出 `!$`(上一个命令的最后一个参数)的内容
      - `!*:p` 打印输出 `!*`(上一个命令的所有参数)的内容
    - `^` 删除替换
      - `^string` 删除上一个命令的第一个string
      - `^sting1^stirng2` 将上一个命令的string1替换为string2
      - `!:gs/string1/string2` 将上一个命令的所有string1替换为string2
  - 调用历史参数
    - `command !^` 调用上一个命令的第一个参数作为command的参数
    - `command !$` 调用上一个命令的最后一个参数
    - `command !*` 调用上一个命令的所有参数
    - `command !:n` 调用上一个命令的第n个参数
    - `command !n:^` 调用第n条命令的第一个参数
    - `command !n:$` 调用第n条命令的最后一个参数
    - `command !n:m` 调用第n条命令的第m个参数
    - `command !n:*` 调用第n条命令的第*个参数
    - `command !string:^` 调用以string开头的命令，获取它的第一个参数
    - ...

- 历史命令快捷键
  - `ctrl + R` 进入历史命令搜索模块
  - `ctrl + G` 退出历史命令搜索

- history命令相关的shell变量
  - $HISTSIZE：历史缓存区的条数限制，默认1000
  - $HISTFILE：指定历史文件，默认为~/.bash_history
  - $HISTFILESIZE：历史文件的条数限制，默认1000
  - $HISTTIMEFORMAT：显示时间，示例：HISTTIMEFORMAT="%F %T"
  - $HISTIGNORE：历史缓存区忽略指定命令，多个命令用冒号:分隔
    - 示例：`export HISTIGNORE = "ls:pwd"`
  - $HISTCONTROL:控制历史命令记录的方式
    - 值为ignoredups：默认，忽略重复的命令，连续且相同认为重复
    - 值为ignorespace：忽略所有以空白开头的命令
    - 值为ignoreboth：相同于ignoreboth：相当于ignoredunps和ignorespace组合
    - 值为erasedups：删除重复命令

- 提示：如果要持久保存上述变量，需要将上面指令存放在etc/profile或者~/.bash_profile中

### 命令行展开
- 所谓命令行展开，即把命令行中给定的特殊符号自动替换为相应字符串的机制。在Bash Shell中有些符号有特殊含义
  - `~` : 自动替换为用户家目录
  - `~USERNAME`: 自动替换为指定用户的家目录
  - `{}`: 可包含一个以逗号分隔的字符串或序列，能够将其展开为多个字符串
  ```shell
  a{d,c,b}e  # ade, ace, abe
  /tmp/{a,b,c}  # /tmp/a, /tmp/b, /tmp/c
  /tmp/{a,b}/z  # /tmp/a/z, /tmp/b/z
  {1..6}  # 1,2,3,4,5,6
  {1..10..2}  # 1,3,5,7,9
  {a..d}  # a,b,c,d
  ```

### 标志I/O重定向和管道
#### 三种I/O设备
- Linux给程序提供三种I/O设备
  - 标准输入(STDIN)  -0  默认接受来自终端窗口的输入
  - 标准输出(STDOUT) -1  默认输出到终端窗口
  - 标准错误(STDERR) -2  默认输出到终端窗口

- 每创建一个新的会话，/dev/pts下就会创建一个新的伪终端，以数字序号命名，三种I/O设备都会指向这些伪终端

- 数据流向有输入流(称为标准输入)、输出流，默认数据的输入流由键盘实现。默认的输出流是到当前的终端屏幕上，Linux系统里输出流又分为错误输出（称为标准错误输出）和正确的输出（称为标准输出）

- 当一个程序刚启动时，会自动打开三个I/O设备文件：标准输入文件STDIN(STD即standard标准，IN即input输入)，标准输出文件STDOUT，标准错误输出文件STDERR。分别得到文件描述符0，1，2.如果此时打开一个新的文件，它的文件描述符会是3

- 因为0，1，2都指向终端窗口，即
```shell
lrwx------. 1 root root 64 Oct 22 21:01 0 -> /dev/pts/3
lrwx------. 1 root root 64 Oct 22 21:01 1 -> /dev/pts/3
lrwx------. 1 root root 64 Oct 22 21:01 2 -> /dev/pts/3
```
所以输入输出都在终端窗口显示

#### 文件描述符
- 在Linux中每一个打开的文件，系统都会给这个打开的文件分配一个唯一的文件描述符(本质上是一个软链接)，指向正在打开的文件。
- 文件描述符是一个非负整数，是内核为了高效管理已被打开的文件所创建的索引。所有执行I/O操作的系统调用都需要文件描述符
- 因此可以通过查询一个的程序中的文件描述符，来发现这个程序打开了几个文件
```shell
cd /proc
# 在proc中能看到所有的进程pid的目录，进入这个目录
cd /5005
# 里面有允许该程序的文件路径和fd目录(即打开的文件描述符目录)
cd /fd
# 进入fd目录，就可以发现多个软链接，指向程序打开的文件
```

- 扩展：
  - 使用`$$`可以发现当前打开shell的pid
  - 当打开一个新的会话，，创建一个伪终端，就是进入shell程序，使用`echo $SHELL`可以查询当前使用的shell类型

#### 重定向技术
- 概述：更改数据流向
- 标准输出和错误的重定向
  - STDOUT和STDERR可以被重定向到指定文件，而非默认的当前终端
  - 格式：
  ```
  命令  操作符号  文件名
  ```
  - 支持的操作符号包括
  ```
  1> 或 >    把STDOUT重定向到文件
  >|         强制覆盖（允许在set -C的情况下，强制覆盖）
  2>         把STDERR重定向到文件
  &>         把所有输出(标准输出和错误输出)重定向到文件

  以上如果文件已经存在，文件内容会被覆盖
  ```
  ```shell
  set -C 禁止将内容覆盖已有文件，但可追加
  set +C 允许覆盖，默认

  # 该知识点仅作了解
  ```
  - 追加：>>可以在原有内容上，追加内容
  - 合并多个程序进行重定向：
    - `(CMD1;CMD2...)`合并多个程序的STDOUT
    - `{CMD1;CMD2;..}`使用花括号，记得结尾加分号；

  - 将标准输出和标准错误同时输出到指定文件
  ```shell
  方法1：
  ls python/ err/ &> all.log

  方法2：
  1s python/ err/ > all.log 2>&1
  ```
  - `&`符号的作用：
    - 表示要操作的是文件描述符而非文件或命令。
    - 例如&1这里指的是文件描述符1
    - 文件描述符的本质是软链接，软链接的本质是指向目标文件的路径，而1指向的是/dev/pts/0即伪终端，因此:`2>&1`的意思就是标准错误输出到描述符1指向的路径中

- 标准输入的重定向
  - 标准输入符号：`<` 后面各跟文件
  ```shell
  bc < file
  # 将需要计算的内容输入到指定文件中，然后标准输入到bc中
  ```

- 管道
  - 管道符：`|`
  ```shell
  seq -s+ 1 100 | bc   # 5050 
  ```

- 单行重定向与多行重定向
```shell
单行重定向：
cat > cat.log

多行重定向：
cat > cat2.log <<EOF  # EOF是结束符

# 单行重定向在回车启用命令是，就已经创建了文件，然后每输入一行，回车后，内容就流入指定文件
# 多行重定向是在所有命令都输入完之后，遇到EOF结束时，才一起执行所有命令
```

#### 支持标准输入的常用命令
- `seq`
  - 作用：用于生成某个范围内的整数
  - 语法：`seq [选项]...[首数][增量][尾数]`
  - 选项：`-s`, `-f`, `-w`
  - 示例：
  ```shell
  # -f：格式化数据，使用%g表示整数，例如%g aaa%03g。
  root@ubuntu2004:/Storage$ seq -f "id:%06g" 1 5
  id:000001
  id:000002
  id:000003
  id:000004
  id:000005

  # 使所有数据同宽，位数小的前面补零，不能和-f同时使用
  root@ubuntu2004:/Storage$ seq -w 2 30 140
  002
  032
  062
  092
  122

  # -s：指定字符分隔产生的所有数字，默认为\n
  root@ubuntu2004:/Storage$ seq -s '+' 1 9
  1+2+3+4+5+6+7+8+9

  ```

- `s-nail`(原mailx)
  - 配置（与外网邮箱互通 ）
  - 在家目录下，创建.mailrc配置文件
  ```shell
  # .mailrc内容如下
  set v15-compat
  set smtp-auth=login
  set from="昵称<qq号@qq.com>"
  set mta=smtps://qq号:qq邮箱授权码@smtp.qq.com:465
  ```
  - 文件配置好后后，使用s-nail发送到外网的邮件，发件人为配置的qq邮箱
  - 本机的邮箱默认位置
  ```
  /var/spool/mail/
  ```

- `tr`
  - 作用：转换和删除字符
  - 语法`tr [OPTION].. SET1 [SET2]`
  - 选项：
  ```
  -d --delete：删除所有属于第一字符集的字符
  -s --squeeze-repeats：把连续重复的字符以单独一个字符表示，即去重
  -t --truncate-set1：将 第一个字符集对应字符转换为第二个字符集对应的字符，如果第一个字符集的字符数量多于第二字符集数量，超出部分忽略
  -c -C --complement：取字符集的补集

  [:alnum:]：字母和数字
  [:alpha:]：字母
  [:digit:]：数字
  [:lower:]：小写字母
  [:upper:]：大写字母
  [:space:]：空白字符
  [:print:]：可打印字符
  [:punct:]：标点符号
  [:graph:]：图形字符
  [:cntrl:]：控制(非打印)字符
  [:xdigit:]：十六进制字符
  ```
  - 示例：
  ```bash
  tr 'a-z' 'A-Z' < /etc/issue

  tr [:lower:] [:upper:] < /etc/issue

  tr -d 'abc'  # 删除字符中的abc

  tr -dc 'abc'  # 只保留字符中的abc，程序完全结束后返回结果

  df|tr -s ' '  # 将df的返回结果中的空格去重
  ```

- `tee`
  - 作用：在 Linux 中用于从标准输入读取数据，并将其内容输出到标准输出和一个或多个文件中。这使得你能够查看数据的同时，将其保存到文件中。
  - 基本用法
  ```shell
  command1 | tee file1
  ```
  - 示例
  ```shell
  ls -l | tee output1.txt

  ls -l | tee -a output1.txt  # 追加内容到output1.txt，而不是覆盖

  ls -l /bin |tee output1.txt|cat -n
  ```
#### 重定向与管道案例
- 案例1
```shell
ls /data /err 2>&1 | tr 'a-z' 'A-Z'
# 同时将标准输入和标准错误通过管道符，输入给tr进行处理

ls /data /err |& tr 'a-z' 'A-Z'  # 相对比较新的写法
```
- 案例2
```bash
# 设置用户口令
echo magedu | passwd --stdin wang &> /dev/null
# --stdin  read new tokens from stdin (root only)
```


## 用户组和权限管理
### Linux安全模型
- 3A资源分派
  - Authentication：认证，验证用户身份
    - 常见的通过用户名和口令，来区分验证用户信息
  - Authorization：授权，不同的用户设置不同的权限
    - 比如，某个文件，张三有访问权限，而李四没有
  - Accouting|Auditon：审计
    - 记录不同用户的操作记录

- 当用户登录成功时，系统会自动分配命令token，包括用户标识和组成员等信息
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
  后续省略

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
  此处省略
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
  此处省略
  
  // 密码的组成：
  同时使用三个$符号分隔成3字段。
  // 第一字段代表加密使用的单向加密算法，使用数字表示，1表示MD5算法，6表示SHA512算法。
  // 第二字段代表加密算法使用的随机因子，一般称为salt盐，salt和加密算法一起构成了密码最终的加密方式。
  // 第三字段代表加密后的结果，即密文
  // 组成：密码（加密后）
  // 更改/创建口令时间（以1970年以基准到更改密码的天数）
  // 最短有效期,即有效期内无法更改口令（0代表可随时更改）（该有效期仅针对普通用户，对root用户无效）
  // 密码有效期，
  // 密码以前几天提醒，
  // 超过密码有效期，再过几天账号锁定
  // 账号有效期

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
  后续省略

  //组的文件组成：组名，密码，id，成员

  /etc/gshadow

  root:*::
  daemon:*::
  bin:*::
  sys:*::
  adm:*::syslog,mystical
  tty:*::syslog
  ...
  后续省略

  //组名，组的口令，管理员账号（管理员可以在组中增删用户）
  // 附加组成员
  ```

- 用户管理常用命令
```sql
useradd     新建用户

# useradd wileson   -- 创建一个新用户wileson
#
# id wileson    -- 使用id 用户名，可以查看该用户是否存在
uid=1001(wilson) gid=1001(wilson) 组=1001(wilson)
#
# 参数
# useradd -d 路径  -- 指定家目录 ‘ -d ’
# useradd -s /sbin/nologin  -- 指定shell类型 ‘ -s ’ 
-- nologin还是给服务使用的，用户一般是使用/bin/bash
# useradd -g postfix  -- 指定主组 ‘ -g ’;postfix是指定的组名
# useradd -G [,GROUP2...]  -- 指定附加组 ‘ -G ’
-- 注意添加的时候，要保证组存在
# useradd -N  -- 不创建和用户同名的私用组作为主组
# useradd -r -- 创建系统用户，CentOS 6：id<500，CentOS7及以上：id<1000
# useradd -M  -- 不创建家目录 ‘ -M ’
# useradd -m  -- 创建家目录  ‘ -m ’
# useradd -u 1088  -- 指定UID ‘ -u ’
# useradd -c 'COMMENT' -- 新的注释信息
总结：
useradd [option...] user_name 

！！！（面试题）所有的新建用户，系统自带的配置文件，都是复制 /etc/skel的文件，
因此，如果在这个目录下新增文件，则所有的新建账户下，都会默认自带新增文件
--------------------------------------------------
userdel     删除用户

# userdel wilson    -- 删除指定用户（保留家目录）
# userdel -r wilson   -- 删除用户（不保留家目录）
# userdel -rf wilson  -- 强制删除

--------------------------------------------------
passwd      修改用户密码

# passwd wilson   --更改指定用户的密码
# passwd    --直接用passwd，默认更改root用户密码

-------------------------------------------------
usermod     修改用户属性

-- usermod -d 指定路径 用户名
# usermod -md /home/wile1 wilson   -- 更改指定用户家目录，新家目录不会自动创建
-- 如果要创建新家目录并移动原家数据，同时使用-m选项
-- -md 原家目录被删除，替换为新指定的目录并转移数据
-- 如果不想要创建家目录的时候自带的配置文件，可以创建的时候使用-M，然后使用usermod -d 指定目录
-- 效果：
-- 1.登录后自动进入该家目录
-- 2. 对用户相关的配置文件也放在了该家目录

# usermod -u UID  -- 更改uid
# usermod -g GID  -- 更改gid
# usermod -G [..GROUP2...GROUPN]  --更改附加组
-- 原来的附加组会被覆盖；若要保留原有的附加组，则要同时使用-a选项
# usermod -s SHELL  -- 更改shell类型
# usermod -l login_name   --更改新的用户名
# usermod -e YYYY-MM-DD   -- 指明用户账号过期日期
# usermod -f INACTIVE  -- 设置非活动期限，即宽限时间
# usermod -L -- lock指用户，在/etc/shadow密码栏增加！ 

--------------------------------------------------

chage       修改用户属性

# 
```

- useradd的默认属性的文件
```bash
[Mon Oct 30 16:10:21 104] root@rocky9:spool $ cat /etc/default/useradd 
# useradd defaults file
GROUP=100 # 100表示users组的编号
# 如果使用useradd -N，不创建私用组的话，就用users(GID100)作为主组
HOME=/home
INACTIVE=-1  # -1表示其实口令到期也不锁账号，如果是10表示口令到期10天后锁账号
EXPIRE=  #-- 表示账户有效期
SHELL=/bin/bash
SKEL=/etc/skel # /etc/skel目录下的内容表示创建新用户时，家目录自带的文件
# /etc/skel实际上是新建账号的模板文件夹
CREATE_MAIL_SPOOL=yes # 默认创建账号邮箱
```

- 新建用户的相关文件
```bash
/etc/default/useradd
/etc/skel/*
/etc/login.defs  # 控制账号口令，即shadow后面配置的默认定义
``` 

- 批量创建用户
```
newusers passwd 格式文件
```

- 批量更改用户口令
```bash
cat <格式文件> | chpasswd

格式文件内容：
user_name : password

示例：
mystical:12346
user1:admin123

在ubuntu中，由于Ubuntu不支持--stdin的选项，因此无法像CentOS一样使用如下命令
echo password | passwd --stdin <user_name>

因此，可以使用如下口令实现非交互式更改口令：
echo user_name:passwd | chpasswd

```

- 查看用户相关的ID信息
  - id命令可以查看用户的UID，GID等信息
  ```bash
  id [OPTION]... [USER]
  ```
  - 常见选项
  ```bash
  -u : 显示UID
  -g : 显示GID
  -G : 显示用户所属组ID
  -n : 显示名称，需配合ugG使用，例如：-un;-gn;-Gn
  ```

- 组管理命令
```
groupadd 新建用户组

格式：groupadd [OPTION]... group_name

常见选项：
-g GID 指明GID号; [GID_MIN,GIDMAX]
-r 创建系统组，CentOS6之前：ID<500, CentOS 7以后：ID<1000

注意：
如果你知道你要创建的是一个系统组，并且你想确保它在系统组的 GID 范围内，那么使用 -r 选项是一个好的实践。如果你只是想创建一个具有特定 GID 的组，不管它是否是系统组，那么只使用 -g 选项就足够了。

添加 -r 选项是为了明确表达你的意图，并确保组被正确地分类为系统组。不过，如果你手动指定了一个在系统组 GID 范围内的 GID，即使没有使用 -r 选项，该组在某种程度上也被视为系统组。

范例：
groupadd -g 48 -r apache
```
```
groupmod 组属性修改

格式：groupmod [OPTION]... group

常见选项：
-n <新组名> <原组名>: 新名字
-g GID : 新的GID

示例：groupmod -n www apache
```
```
groupdel  group_name    删除用户组
```
- 关于脚本中写组和用户的创建的示例
```bash
getent group apache > /dev/null || groupadd -g 48 -r apache
getent passwd apache > /dev/null || \
  useradd -r -u 48 -g apache -s /sbin/nologin -d /var/www -c "Apache" apache
exit 0
```

### 理解并设置文件权限
- Linux指令权限管理
```sql
su <用户名>     -- 切换为用户名的身份权限
-- 不完全切换，身份切换了，但是环境还是之前的root路径下
su - <用户名>   -- 完全切换，身份和所在路径都切换了
su - <用户名> -c 'cmd' 
-- 以切换的指定身份执行命令，但本身不切换身份，依然是当前用户
exit    -- 切换回上一个身份

--------------------------------------------------
su 和 sudo 的区别

su              -- 切换用户
su -USERNAME    -- 使用login shell方式切换用户

sudo            -- 以其他用户身份执行命令
visudo          -- 设置需要使用sudo的用户(组)

sudo的意义：
可以授权普通用户使用sudo命令去执行指定的root权限才能进行的被允许普通用户也可以执行的命令

场景一
-- root用户执行：
# shutdown -h 30    -- 30分钟后系统自动关闭
-- 如果普通用户想要停止这个操作，需要执行
# shutdown -c   -- 停止关闭指令
-- 但是普通用户没有这个命令的执行权限
-- 因此需要root用户通过sudo配置给普通用户授权

具体的授权操作：
使用visudo进入配置文件
配置操作共3段指令

第一段：确定授权的用户/组；
-- 用户：直接输入名称
-- 组：‘%’ 加‘组名’

第二段：给哪些用户授权哪些命令
-- 命令形式
-- 远程登录的话：
ALL=授权的指令
-- 本地服务器登录：
localhost=授权的指令
-- 如果是多条命令的话，中间用逗号‘ ，’隔开
-- 被授权的命令需要填写具体的命令地址，地址的查询使用which指令
例如：授权的指令为shotdown，但是不知道shotdown指令的地址
# which shutdown；
/sbin/shutdown --返回结果
-- 查询 shutdown 的地址为/sbin/shutdown，这个地址就可以写在授权命令中

第三段：判定普通用户在使用管理员授权的命令时，是否需要输入密码
-- 不需要的话：
NOPASSWD: ALL (不建议)

整个示例的命令为：
# zhangyifeng ALL=/sbin/shutdown -c

最后保存退出

总结：使用visudo，配置visudo的信息，可以达到给普通用户授权使用root权限指定命令的效果。很好用哦

```
- Linux文件权限管理
```shell
root@clem:~# ll
total 32
drwx------  4 root root 4096 Jun 27 08:54 ./
drwxr-xr-x 20 root root 4096 Jun 28 20:32 ../
-rw-------  1 root root  458 Jun 28 22:20 .bash_history
-rw-r--r--  1 root root 3204 Jun 27 08:38 .bashrc
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwx------  3 root root 4096 Dec 21  2022 snap/
drwx------  2 root root 4096 Dec 21  2022 .ssh/

解析：-文件类型 权限 链接数 所属账号 所属主组 大小 时间 文件名
```
```sql
chown   -- 更改文件用户权限/更改所有权限

# chown user_name file_name
-- 将file文件的用户权限改为user_name

# chown user_name.group_name file_name
# chown user_name:group_name file_name
-- 将该文件所属的用户名，组名一起变更。

# chown -R user_name.group_name dir
-- 将文件夹下，所有文件的所属账号和组都一起变更，危险命令

chgrp   --仅更改文件所属组权限

# chgrp group_name file_name
-- 更改所属组

```
- 文件权限类型
  - r Readable 读
  - w Writable 写
  - x eXcutable 执行
```shell
示例：
-rw-r--r--  1 root root  161 Dec  5  2019 .profile

- rw- r-- r--
第一个‘-’ 不在权限标识中，仅指文件类型
第一组‘rw-’ 标明所属用户权限
第二组‘r--’ 同组其他用户权限
第三组‘r--’ 其他用户权限，通用权限，所有人基本都能用
```

- rwx对于目录的权限意义（与文件不同）
  - r：可以使用ls查看此目录中文件名列表，但无法看到文件的属性meta信息，包括inode号，不能查看文件的内容
  - w：可以在此目录中创建文件，也可以删除此目录中的文件，而和此被删除的文件的权限无关。
  - x：如果，没有该目录的执行权限，用户将无法访问这个目录下的所有文件，所以执行权限是目录访问的基本权限，没有执行就无法进入，是的，连目录进都进不去！
    - 如果只有x,没有r的话，对于目录来说，就是只能访问，但是看不到ls，就是没有访问目录下文件名的权限，但是如果这个文件你知道名称，且这个文件的通用权限有读权限，那么对于普通用户来说，只是无法浏览目录下文件名及文件元信息，但是依然可以cat到文件内的内容

- 更改文件的读写权限
```sql
chmod   -- 模式法和数字法

模式法：
chmod who opt per file
-- who：u,g,o,a 
-- u(所属者)，g(所属组)，o(other),a(all)
-- opt:+,-,=
-- per:r,w,x

示例：
chmod o+r file  -- 表示file文件的通用权限中增加r权限

数字法：
rwx rw- --- a.txt
111 110 000 a.txt
7   6   0
chmod 760 a.txt
```

- 默认权限
  - 定义：当创建一个文件或文件夹时，会默认一个权限，这个默认权限时如何产生的，如何修改
```sql
umask  -- 这个指令可以修改新建文件/文件夹的权限

# umask -- 查看当前umask的值
-- root权限的默认umask值022
-- 普通用户的默认umask值002
-----------------------------------------------
修改默认权限的实现方式

指定新建文件的默认权限
666-umask，如果所得结果某位存在执行（奇数）权限，则将其权限+1，偶数不变

将权限+1的原因：
文件的执行时危险的！！！，如果没有执行权限，root也无法直接执行，但是没有读写权限，root依然能够进行读写

基于安全考虑，默认新建的文件不允许有执行权限！！

umask 的内在机制

666
123   -- umask值

110110110
001010011     -- mask
110100100
644
------------------------------------------------
指定新建目录的默认权限

777-umask
------------------------------------------------
修改默认权限
# umask <更改后的数字>    -- 临时修改

永久修改：
root目录下，.bashrc文件内修改，添加umask <数值>，保存退出后，. .bashrc或者重启
-- 全局设置：/etc/bashrc 不建议，这里修改会影响全局所有用户
-- 用户设置：~/.bashrc 只影响当前用户

```

- 特殊权限
```sql
SUID
用于二进制可执行文件，执行命令时取得文件属主权限或root权限

表现形式
# ls -l /usr/bin/passwd
-rwsr-xr-x. 1 root root 33424 Apr 20  2022 /usr/bin/passwd

-- 表示这个文件，即使普通用户也能执行修改

实现SUID的指令
# chmod 4755 file_name


SGID
用于目录，在该目录下创建新的文件和目录，权限自动更改为该目录的属组

应用场景：文件共享



SBIT
保证该文件只有root和自己可以删除150

实现SBIT的指令
# chmod 1777 file_name
```
- 特殊属性（限制管理员-root）
```sql
# chattr +i a.txt   -- 添加i属性限制root

# lsattr a.txt    -- 查看i属性

# chattr -i     -- 删除i属性

# chattr +a     -- 只能追加，不能修改，不能删除

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
# 禁止本机被ping的配置文件
echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all

ping 10.0.0.8
ping -f -s <ip地址> -c1
#-f 表示泛洪，就是最大功率无限制发送数据包
#-s 指定发送包的大小，最大不能超过65507
#-c(num) ping的次数
```

### ARP协议(Address Resolution Protocol)
- ARP协议 （第二层协议）
  - 定义：APR地址解析协议，由互联网工程任务组(IETF)在1982年11月发布的RFC826中描述制定，是根据IP地址获取物理地址的一个TCP/IP协议
  - 作用：根据IP地址寻找对应的物理地址
  - 原理：显示发送一个包含有IP地址的请求广播给局域网的所有主机，对应IP的主机会返回一个数据包给发送请求的主机，该数据包中含有这个主机的MAC地址，交换机上记载着MAC地址对应的交换机接口，从而实现物理地址的寻址
  - 本质：在于IP地址到MAC地址的转换
  ```sql
  查询ip地址与mac地址对应关系的指令
  # arp -n
  -- 只有发生过通讯，才会显示
  -- 可以通过ping，来做实验，观察发生过通讯的虚拟机双方记录的ip和mac的对应关系
  ```
  - 因为arp是通过广播实现的ip与mac地址的转换，因此，arp是不能跨网段的，因为路由器会屏蔽清除掉广播信息
  - 判断广播的方法：数据链路层的目标地址是48个1，即ffffff，就说明是广播
  - 详细过程：
    - 第一步：源主机广播发送一个请求数据包，询问谁是xxxip,同时数据包携带源主机的IP和MAC地址
    - 第二步：目标主机收到数据包后，发现ip与自己一致，于是记录下源主机的IP和mac地址，同时向这个地址发送响应数据包，上面携带自己的ip和mac地址。注意!!! 这次目标主机对源主机的响应式单播
    - 第三步，源主机收到目标主机的响应包后，将目标主机的IP所对应的mac地址记录下来，实现ip到mac的转换 
  - ARP存在的安全问题
    - 由于是广播机制，同时没有任何校验，因此很容易被黑客进行apr欺骗，造成流量劫持，
    ```sql
    KALI系统实现arp欺骗上网流量劫持
    
    -- 启动路由转发功能
    # echo 1 > /proc/sys/net/ipv4/ip_forward
    
    -- 安装包
    # apt-get install dsniff
    
    -- 欺骗目标主机，本机是网关
    # arpspoof -i eth0 -t 被劫持的目标主机ip 网关ip
    
    -- 欺骗网关，本机是目标主机
    # arpspoof -i eth0 -t 网关ip 被劫持目标主机ip 
    ```
  - 解决方法：
    - ARP静态绑定可以防止ARP欺骗，提前绑定好目标ip和mac地址的对应关系，直接进行单播通讯，同时也不会发送询问报文进行询问，避免apr欺骗
  ```sql
  arp -s 10.0.0.6 00:0c:29:32:80:38
  -- arp -s ip地址  mac地址
  
  删除arp中ip和mac的对应关系
  # apr -d ip地址
  ```

- Gratuitous ARP
  - 定义：也称为免费ARP
  - 作用：验证IP是否冲突
  - 原理：自问自答
    - 第一步：机器启动时，向网络中发送一个谁是xxip的报文，xxip是机器自己的ip
    - 第二步：如果无冲突ip，则机器再次发送一个响应ip，回复我是xxip,才而验证网络中无ip冲突

- Reverse Address Resolution Protocol
  - RARP即反向地址解析协议，将MAC地址转换为ip地址
  - 作用：主要用于无盘环境

### Internet协议
- IP PDU报头
  ![Alt text](images/image06.png)

  - 版本：占4位，指IP协议的版本，目前的IP协议版本号是4
  - IPV4的源地址是32位，所以，共有2^32个地址，约为43亿个
  - 首部长度：占4位，可表示的最大数值是15个单位，一个单位为4个字节，因此IP的首部长度最大值是60个字节
  - 分区服务：占8位
  - 总长度；占16位，是报文头+数据部分的总长度，单位是字节，因此数据包的最大长度是65535字节，总长度必须不超过最大传送单元MTU
  - 标识：占16位，同一个打包，分片多个小包，每个分片的标识是一样的
  - 标志：占3位，标志同一个包，分片的序号，目前只有后两位有意义
  - 片偏移：13位，制定了数据包的偏移量，即较长的分组在分片后，该分片在原分组中的相对位置，片偏移以8个字节偏移单位
  - 生存期：TTL(timetolive),标识数据包允许经过的路由器的数量，不是时间，例如TTL=64;说明这个数据包允许经过64个路由器
    - TTL常见的3个默认值：64(linux)，128，255
    - 修改ttl默认值
    ```sql
    # echo (num) > /proc/sys/net/ipv4/ip_default_ttl
    ```
  - 协议：占8位，指出此数据包携带的数据，使用何种协议以便目的主机的ip层将数据部分上交到上层哪个协议处理（1 表示为ICMP协议，2表示为IGMP协议，6表示为TCP协议，17表示为UDP协议）
  - 首部校验和：占16位，判断数据包是否被破坏
  - 源地址：占32位
  - 目的地址：占32位
  
- ipv4和ipv6的区别
```
IPv4和IPv6是两种不同的互联网协议，用于数据在网络中的传输。下面是它们之间的主要区别：

地址长度：

IPv4：32位地址，通常以点分十进制格式显示，如192.168.1.1。
IPv6：128位地址，通常以冒号分隔的十六进制格式显示，如2001:0db8:85a3:0000:0000:8a2e:0370:7334。
地址空间：

IPv4：大约有43亿个地址。
IPv6：具有近乎无限的地址空间，是IPv4的数千倍。
头部复杂性：

IPv4：头部通常更加复杂，有多个字段。
IPv6：头部设计得更简洁，许多不必要的字段被去掉或者移到扩展头中。
自动配置：

IPv4：需要额外的协议如DHCP来实现自动地址配置。
IPv6：支持地址的自动配置。
安全性：

IPv4：安全是可选的，依赖于IPSec等技术。
IPv6：设计时考虑到了安全性，IPSec的支持是必选的。
广播：

IPv4：使用广播来发送数据到同一网络的所有设备。
IPv6：没有传统的广播模式，而是使用多播和其他新机制来实现类似的功能。
报文头的具体区别：

IPv4报文头字段（至少包含以下内容）：

版本
头部长度
服务类型
总长度
标识
标志
片偏移
生存时间 (TTL)
协议
头部校验和
源IP地址
目的IP地址
选项（可选）
IPv6报文头字段（固定大小为40字节，包含以下内容）：

版本
通信量类别
流标签
有效载荷长度
下一个头部
跳数限制（相当于IPv4的TTL）
源地址
目的地址


IPv6相比IPv4更加先进和健壮，设计时考虑了未来的扩展性、安全性和其他网络挑战。但由于IPv4的广泛部署和兼容性问题，两种协议仍然共存，尽管大量的努力正在推动向IPv6的过渡。
```
- ip地址的组成
```sql
给一个网卡配置多个ip （临时配置，重启后回复）

# ip a a 10.0.0.7/24 dev eth0 label eth0:1
-- 给这台机器的网卡的子接口添加一个10.0.0.7的ip

解析；
/* ip：这是Linux下的一个命令，用于显示或操作路由、网络设备、策略路由和隧道。
它是ifconfig命令的现代替代者。*/

-- 第一个a：这是ip命令的缩写形式，实际上应该是addr或address，意为“地址”，用于管理网络地址

-- 第二个a：这是add的缩写，表示添加

/* 10.0.0.7/24：这是CIDR格式的IP地址。
10.0.0.7是IP地址，/24表示其子网掩码的前24位是1，对应于子网掩码255.255.255.0。*/

-- dev：这是“device”的缩写，意为“设备”，表示接下来要指定的是哪个网络设备。

-- eth0：这是网络设备(网卡)的名称，通常是Ethernet适配器的默认名称

-- label：标签，用于给配置的IP地址提供一个别名或标识。这在你给单个物理接口配置多个IP地址时非常有用。

/* eth0:1：这是给新添加的IP地址10.0.0.7的标签。
它告诉系统这个地址是eth0的一个别名或虚拟接口。
通常，可以为一个物理接口配置多个虚拟接口，每个虚拟接口有其自己的IP地址。*/


# ip a      -- 查看网卡信息
```
- 探测ip冲突的情况
```sql
# arping ip地址
```

### ip地址
- ip地址的意义
  - ip地址可以实现逻辑上的管理功能
- ip地址组成
  - 网络ID：表示网络，每个网段分配一个网络ID，处于高位
    - 作用：体现ip所在的网段（位置）
  - 主机ID：表示单个主机，由组织分配给各设备，处于低位

- IP地址的分类（早期分类）
  ![Alt text](images/image07.png)

  - A类：1-126.X.X.X
    - 0开头，表示未知地址，不能用
    - 127开头，表示回环地址，不能用
  - B类：128-191.X.X.X
  - C类：192-223.X.X.X
  - D类：224-239.X.X.X（多播）
  - E类：略（留给科学家使用）
- 公式
  - 网络数 = 2^可变的网络ID数
  - 主机数 = 2^(32-可变网络ID数，即主机数)-2
    - 主机数全为0，则是该网段的编号
    - 主机数全为1，则是该网段的广播ip
  - 网络ID = IP和子网掩码netmask做'与运算'

- 不分类的IP(现代方式)
  - 优势：早期的分类方法过于僵化，不利于ip地址的灵活管理
  - 网络ID的位数按需分配
  - CIDR表示法：表示网络ID的位数
    - IP/网络ID的位数
  - 子网掩码表示：可以用来表示网络ID的位数，32位二进制，对应于网络ID的位为1，对应于主机ID的位为0

- 公共和私有IP地址 
  - 私有IP地址：不直接用于互联网，通常在局域网中使用
  ![Alt text](images/image08.png)
  - 公共IP地址：互联网上设备拥有的唯一地址
  ![Alt text](images/image09.png)
  - 公共IP地址世界唯一，可以通过互联网访问，私有地址不能通过互联网访问

- 特殊地址
  - 0.0.0.0
  <br>0.0.0.0 不是一个真正意义上的IP地址。它表示所有不清楚的主机和目的网络
  - 255.255.255.255
  <br>限制广播地址。对本机来说，这个地址指本网段内（同一广播域）的所有主机
  - 224.0.0.0到239.255.255.255
  <br>组播地址，224.0.0.1特指所有主机，224.0.0.2特指所有路由器。224.0.0.5指OSPF路由器，地址多用于一些特殊的程序以及多媒体程序
  - 169.254.x.x
  <br>如果Windows主机使用了DHCP自动分配IP地址，而又无法从DHCP服务器获取地址，系统会为主机分配这样的地址

- 判断两个IP是否在一个网段
  - 示例A:10.0.1.1/16; B:10.0.2.2/24
  - 分析步骤：
    - 如果A访问B，则A和自己的netmask做与运算
    - B和A的netmask做与运算
    - 两个结果进行比较，相同则在同一网段，反之不在。
    - 如果B访问A，则比较结果不相同，则不在同一网段
    <br>（如果在一个网段，则可以直接arp寻址通讯；如果不在同一网段，则需要借助路由网关进行寻址通讯）


- 划分子网
  - 定义：将一个大的网络(主机数多)划分成多个小的网络(主机数少)，主机ID位数变少，网络ID位数变多，网络ID位向主机ID位借n位，将划分2^n个子网
  - 公式：网络ID向主机ID借位，如果借n位，则划分2^n个子网 
  ```sql
  试题：中国移动10.0.0.0/8 给32个各省子公司划分对应子网
  
  1.每个省公司的子网netmask?
  
  -- 255.248.0.0
  
  2.每个省公司的子网的主机数是多少？
  
  -- 524286
  
  3.河南省得到第10个子网，网络ID？
  
  -- 10.72.0.0/13
  
  4.河南省得到第10个子网的最小IP和最大IP？
  
  -- 最小IP：10.72.0.1；最大IP：10.79.255.254
  
  5.所有子网中最大，最小的子网的net id？
  
  -- 最小ip: 10.0.0.0/13; 最大ip: 10.248.0.0/13
  ```

- 优化IP地址分配
  - 合并超网：将多个网络合并成一个大网，主机ID位向网络ID位借位，主要实现路由聚合功能

- 动态主机配置协议DHCP

### 网络配置
- 基本网络配置
  - 将Linux主机接入网络，需要配置网络相关设置，一般包括
    - 主机名
    - IP/netmask
    - 路由：默认网关
    - DNS服务器
      - 主DNS服务器
      - 次DNS服务器
      - 第三个DNS服务器
  ```sql
  -- 配置主机名
  # hostnamectl set-hostname <新主机名> -- centos7之后使用
  # cat /etc/hostname   -- centos7之后，主机名配置文件
  
  -- centos6之前
  # vim /etc/sysconfig/network  -- 更改主机名配置文件
  # hostname centos6.magedu.org   -- 启用主机名
  ```

- 网卡名称
```sql
更改网卡名

-- centos6及以前
永久修改网卡名-更改文件
# vim /etc/udev/rules.d/70-persistent-net.rules
-- 删除多余网卡信息
-- 将现有网卡信息的名称改为eth0

使用指令‘临时’修改网卡名
# ip link set <网卡名> down   --禁用网卡
# ip link set <旧网卡名> name <新网卡名>  --更改网卡名
# ip link set <新网卡名> up   -- 启用网卡

-- centos7及以后
永久修改网卡名-修改配置文件
# vim /etc/default/grub
GRUB_CMDLINE_LINUX="... net.ifnames=0"
--进入文件，这行最后，添加net.ifnames=0

# grub2-mkconfig -o /boot/grub2/grub.cfg
-- 执行之后重启即可

-- ubuntu的修改和centos7类似
# vim /etc/default/grub
GRUB_CMDLINE_LINUX="net.ifnames=0"
--进入文件，这行最后，添加net.ifnames=0

# grub-mkconfig -o /boot/grub/grub.cfg
-- 执行之后重启即可

```

- ip地址修改
```sql
Centos网卡配置文件：
# /etc/sysconfig/network
-- 更改主机名hostname
# /etc/sysconfig/network-scripts/
-- 进入网卡配置目录
# ifcfg-eth0
-- 找到这个文件或新建这个文件（内容自己写）-网卡接口配置文件
-- 文件名必须以ifcfg开头，横杠后叫什么无所谓，建议和网卡名一致

文件配置内容：

DEVICE=eth0 | HWADDR=00:0c:29:88:37:b8 (MAC地址) 二选一
-- 两种方式都可以用来表示选择配置哪块网卡
MACADDR=<mac地址> --(非必选)，可以用来更改mac地址
NAME=eth0
BOOTPROTO=dhcp  --动态配置

BOOTPROTO=static 或者none  --静态配置
IPADDR=10.0.0.88
NETMASK=255.255.255.0 或者 PREFIX=24
GATEWAY=10.0.0.2 --配置网关，根据网络规划写
-- 查看默认网关，执行ip route 或者 route -n
DNS1=10.0.0.2 
DNS2=100.76.76.76
-- 填写DNS服务器地址，网上可以查到一些著名的DNS服务器地址，都可以用
-- 比如阿里的：223.6.6.6
-- 百度的：180.76.76.76
-- 移动的：114.114.114.114
-- 谷歌的：8.8.8.8 
-- 验证DNS，查看文件/etc/resolv.conf

DOMAIN=<要修改的后缀名>
-- 默认ping www 后面自动补充一个域名，该域名是hostname的后缀，如果不想修改hostname后缀，可以在网卡配置文件中加入：


ONBOOT=yes  --是否启动这个网卡，默认yes

-- 保存配置文件

--centos8及之上执行这两条命令
# nmcli connection reload
# nmcli connection up eth0 -- 启用设置好的网卡
-- 如果是多块网卡同时设置后启用，可以用空格隔开
-- nmcli connection up eth0 eth1

--centos7执行
# systemctl restart network
```

- ifconfig命令
```
查看启用网卡

# ifconfig

查看所有网卡

# ifconfig -a

启用网卡

# ifconfig eth0 up

禁用网卡

# ifconfig eth0 down

更改网卡ip

# ifconfig eth0 <新ip地址>

临时清空ip地址

# ifconfig eth0 0.0.0.0/0

保留一个网卡的情况下，增加新地址，实现一个网卡多个ip

# ifconfig eth0:1 <新ip地址>  //网卡别名

查看网卡吞吐量和状态

# ifconfig -s

# watch -n1 ifconfig -s

删除网卡别名

# ifconfig eth0:1 down

清除网卡ip
# ifconfig eth0 0
```

- 路由route
  - route: 路由表管理命令
  - 路由表:作用是导航，地图，不仅仅在路由器有，在任何通信的主机都有
  ```
  查看路由表
  # route -n

  Kernel IP routing table
  Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
  0.0.0.0         192.168.56.2    0.0.0.0         UG    100    0        0 eth0
  # 默认路由，在通向未知网段，目标路由设为0.0.0.0
  192.168.56.0    0.0.0.0         255.255.255.0   U     100    0        0 eth0
  # 直连网段的路由会自动生成
  192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0

  每一行描述的是一个网络的路径
  Destination：表示需要达到的目标网络，Destination配合Genmask（子网掩码）表示具体网络地址
  0.0.0.0 表示未知网络

  iface接口：如果要达到目标网络ID，需要从本机的哪个接口将数据包发出

  Gateway网关：如果目标网络不直接相连，需要将数据包发送到下一个路由器邻近的接口的IP，即网关；如果网络和本主机直连，则无需网关 

  网关的功能：让主机通过网关访问别的网段的机器，所以网关的接口地址，一定和主机网卡在同一网段

  Metric(费用)；数值越低，优先级越高，路径越优；同一目标地址可能有多条路径，根据Metric的数值，可以看出最优路径

  ---------------------------------------------------

  给路由表添加信息（静态路由）

  # route add [-net|-host|default] target[netmask Nm] [gw Gw] [[dev] If]

  实例：
  仅主机路由
  # route add -host 192.168.1.3 gw 172.16.0.1 dev eth0

  默认路由
  #route add -net 0.0.0.0 netmask 0.0.0.0 gw 172.16.0.1
  #route add default gw 172.16.0.1
  
  网络路由
  # route add -net 179.20.0.0/16 gw 172.18.0.201 dev eth1

  查看虚拟机转发功能状态，默认不开启，如果接收到的数据包，目标地址不是该主机，则直接抛弃，不会转发

  # cat /proc/sys/net/ipv4/ip_forward
  0

  0表示不开启数据包转发功能
  修改这个ip_forward文件可以临时开启数据转发

  永久开启

  修改文件sysctl.conf

  # vim /etc/sysctl.conf
  在最后一行，添加：net.ipv4.ip_forward=1
  保存退出
  # sysctl -p 
  使文件sysctl.conf 生效 

  使用mtr工具，可以查看主机到目标机器之间经过的路由

  # mtr <目标ip>

  使用tracepath 和traceroute，都能查看主机到目标经过的路由
  # tracepath <目标ip>
  # traceroute <目标ip>

  配置动态路由（了解即可，后续有时间再深入了解）

  通过守护进程获取动态路由
  安装quagga包，通过命令vtysh配置
  支持多种路由协议：RIP、OSPF和BGP
  RIP协议算法：经过的路由器越少（步跳），路线越优
  OSPF协议算法：除了路由数量，还会考虑带宽

  netstat工具(和ss选项基本一致)
  netstat和ifconfig都来自于net-tools
  其中 ifconfig建议使用ip代替；netstat建议使用ss代替
  ip和ss都来自于iproute

  常用选项
  -t：tcp协议相关
  -u：udp协议相关
  -w：raw socket相关
  -l：处于监听状态
  -a：所有状态
  -n：以数字显示IP和端口
  -e：扩展格式
  -p：显示相关进车给及PID

  常用组合

  -tan
  -uan
  -tnl
  -unl

  显示路由表，类似于route -n

  # netstat -rn

  # netstat -Ieht0 
  -I和网卡名之间没有空格，作用和ifconfig -s 相同，用于查看网卡吞吐量

  ---------------------------------------

  ip 工具

  链路层指令

  # ip link    查看链路层，网卡的状态

  # ip link set <网卡名> up/down    禁用/启动网卡

  使用指令‘临时’修改网卡名

  # ip link set <网卡名> down   --禁用网卡
  # ip link set <旧网卡名> name <新网卡名>  --更改网卡名
  # ip link set <新网卡名> up   -- 启用网卡

  网络层指令

  # ip address    显示网络层相关地址

  # ip address add 10.0.0.100/24 dev eth0 label eth0:1
  建议加label标签，这样可以和ifconfig兼容
  新增网卡ip地址

  # ip addr del 1.1.1.1/24 dev eth0   删除ip地址

  # ip addr flush dev eth0    清空网卡下所有ip地址
  # nmcli connection up eth0 重新加载eth0的原始ip地址

  # ip route  查看路由表，相当于route -n

  # ip route add 路由表信息   新增路由网段

  # ip route del 路由表信息   删除路由网段信息
  ```
- 回环网卡：lo
  - 回环网卡的地址不会出现在路由表中
  - 所有和回环网卡同一网啊的地址，都看作是本机之间的通讯
  - 回环地址默认不参与网络通信
  - 但是如果给回环网卡加上路由信息，也能实现网络通讯

- ip地址的三种工作范围
  - global：全局有效
  - link：仅该网卡链路有效
  - host：仅主机有效

- 虚拟机的三种网络连接类型
  - 桥接 (Bridge) - vmnet0:
    - 桥接模式下的虚拟机将被视为与主机处于同一物理网络中的另一台独立的计算机。它会直接连接到主机的物理网络。
    - 虚拟机会从网络的 DHCP 服务器（可能是家庭路由器或公司网络的 DHCP 服务器）获取其 IP 地址。
    - 这种模式使得虚拟机可以像其他物理计算机一样与网络中的其他设备通信。
  - NAT (Network Address Translation) - vmnet8:
    - NAT 模式下的虚拟机将与外部网络通信，但它不是直接连接的。而是通过 VMware 的 NAT 服务，该服务在主机上运行。
    - 虚拟机将从 VMware NAT 服务的 DHCP 获取 IP 地址，而不是从外部网络。
    - 这种设置提供了一种隔离，因为虚拟机不会在主网络上直接可见。但是，它仍然可以访问外部网络，例如进行互联网浏览或下载文件。
  - 仅主机 (Host-only) - vmnet1:
    - 仅主机模式下的虚拟机只能与主机通信。它不能访问外部网络
    - 这提供了一种高度的隔离，适用于那些您不希望暴露给网络但仍想在主机上进行交互的虚拟机。
    - 虚拟机会从 VMware 仅主机网络的 DHCP 服务获取 IP 地址。

### 路由相关配置文件
```
/etc/sysconfig/network-scripts/route-IFACE

# route-IFACE 默认不存在，需要手工创建,IFACE是网卡名

两种风格：
(1) TARGET via GW
如：10.0.0.0/8 via 172.16.0.1

(2) 每三行定义一条路由（#表示数字，不推荐）
ADDRESS#=TARGET
NETMASK#=mask
GATEWAT#=GW
```
- 重启网络服务
  - CentOS 6 ：service network restart
    - CentOS 6 记得关闭NetworkManager
  - CentOS 7及以后：systemctl restart netwrok

- 注意：
  - 网卡别名必须配置静态地址

### 多网卡bonding  
- 将多块网卡绑定同一IP地址对外提供服务，可以实现高可用或者负载均衡。直接给两块网卡设置同一IP是不可以的。通过bonding，虚拟一块网卡对外提供连接，物理网卡的被修改为相同的MAC地址
- 共7种模式
  - Mode0(balance-rr): 轮询(Round-Robin)策略，从头到尾顺序的在每个slave接口上面发送数据包。本模式提供负载均衡和容错能力。
  - Mode1(active-backup): 活动备份(主备)策略，只有一个slave被激活，当且仅当活动的slave接口失败时才会激活其他slave，为了避免交换机发生混乱，此时绑定的MAC地址只有一个外部端口上可见
  - Mode3(broadcast): 广播策略，在所有的slave接口上传送所有的报文，提供容错能力 

- 说明：
  - active-backup、balance-tlb和balance-alb模式不需要交换机的任何特殊配置。其他绑定模式需要配置交换机以便整合链接。如：Cisco交换价需要在模式0、2和3中使用Ether Channel，但在模式4中需要LACP和Ether Channel

- Bonding配置
```shell
创建bonding设备的配置文件
/etc/sysconfig/network-scripts/ifcfg-bond0
# 其中ifcfg-bond0文件需手工配置，文件名后面必须是bond加数字

TYPE=bond
DEVICE=bond0
BOOTPROTO=none
IPADDR=10.0.0.100
PREFIX=8
# miimon指定链路监测时间间隔。如果miimon=100，那么系统每100ms监测一次链路连接状态，如果有一条线路不通就转入另一条线路
BONDING_OPTS="mode=1 miimon=100"

/etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
BOOTPROTO=none
MASTER=bond0
SLAVE=yes
ONBOOT=yes

/etc/sysconfig/network-scripts/ifcfg-eth1
DEVICE=eth1
BOOTPROTO=none
MASTER=bond0
SLAVE=yes
ONBOOT=yes
```
- 查看bond0状态：
  - `/proc/net/bonding/bond0`
- 删除bond0
  - `ifconfig bond0 down`
  - `rmmod bonding` 

### CentOS7以上版网络配置
- 概述：CentOS6之前，网络接口使用连续号码命名：eth0、eth1等，当增加或删除网卡时，名称可能会发生变化CentOS7以上版使用基于硬件，设备拓扑和设备类型命名
- 网卡命名机制
  - 如果Firmware（固件）或BIOS为主板上集成的设备提供的索引信息可用，且可预测则根据此索引进行命名，如：eno1
    - 翻译：如果你的计算机主板上有一个内置的网络接口（网卡），系统可以从固件或BIOS中获取一些信息来给它命名。这种命名是基于该网络接口在主板上的位置或其他硬件信息。例如，它可以被命名为“eno1”，其中“eno”表示它是一个嵌入式网络输出，并且“1”是它的编号或索引。
  - 如果Firmware或BIOS为PCI-E扩展槽所提供的索引信息可用，且可预测，则根据此索引进行命名，如：ens1
    - 翻译：如果你在计算机上安装了一个额外的网络接口卡（例如，通过一个PCI-E扩展槽），系统也可以从固件或BIOS中获取一些信息来给它命名。这种命名是基于该网络接口卡在扩展槽中的位置或其他硬件信息。例如，它可以被命名为“ens1”，其中“ens”表示它是一个PCI-E网络输出，而“1”是它的编号或索引。
  - 如果硬件接口的物理位置信息可用，则根据此信息命名，如：enp2s0
    - 翻译：如果系统能够获取到网络接口在计算机内部的物理位置信息（例如，它连接到第2个PCI总线上的第0个插槽），它就会使用这些信息来给网络接口命名。在这个例子中，“enp2s0”是基于网络接口的物理位置来命名的，其中“p2”表示PCI总线2，而“s0”表示插槽0。
  - 如果用户显示启动，也可根据MAC地址进行命名，如：enx2387a1dc56
    - 翻译：如果用户明确要求（通常是通过配置文件设定），系统可以使用网络接口的MAC地址来命名它。MAC地址是一个网络接口的唯一标识符。在这个例子中，“enx2387a1dc56”是基于网络接口的MAC地址来命名的，其中“2387a1dc56”是该接口的MAC地址。
  - 上述均不可用时，使用传统命名机制

- 网卡组成格式
  - en：Ethernet 有线局域网
  - wl：wlan 无线局域网
  - ww：wwan 无线广域网
  - o&lt;index&gt;: 集成设备的设备索引号
  - s&lt;slot&gt;: 扩展槽的索引号
  - x&lt;MAC&gt;: 基于MAC地址的命名
  - p&lt;bus&gt;s&lt;slot&gt;: enp2s1

- 更改网卡命名，使用传统命名方式
  - <a href="#网络配置">更改方法</a>

- 主机名hostname（CentOS7及以上）
  - 配置文件：`/etc/hostname`
  - 默认没有此文件，通过DNS反向解析获取主机名，主机名默认为：localhost.localdomain
  - 设置主机名：`hostnamectl set-hostname centos7.magedu.com`
  - 删除文件/etc/hostname，恢复主机名localhost.localdomain
  - 显示主机名
    - `hostname`
    - `hostnamectl status`

- 网络配置工具nmcli
  - 依赖NetworkManager服务，此服务是管理和监控网络设置的守护进程
  - nmcli命令
  ```shell
  nmcli connection  # 查看网卡连接

  # 更改网卡名称(name)
  nmcli connection modify <旧网卡名> con-name <新网卡名> # 更改后自动生成配置文件

  # 更改网卡配置
  nmcli connection modify <网卡名> ipv4.addresses <ip地址> ipv4.gateway <网关地址> ipv4.dns <dns地址> ipv4.method manual
  # 这里ipv4.method manual表示采用静态地址，默认不写是auto，表示动态地址
  # 示例：
  nmcli connection modify eth1-home ipv4.addresses 192.168.0.100/24 ipv4.gateway 192.168.0.1 ipv4.dns 233.6.6.6 ipv4.method manual

  配置改好后，重新加载网卡，然后重新启用配置好的网卡
  nmcli connection reload
  nmcli connection up eth1-home

  # 删除配置的网卡
  nmcli connection delete <网卡名>

  -----------------------------------------------------------------
  使用nmcli实现bonding模式

  nmcli connection add con-name mybond0 ifname bond0 type bond mode active-backup
  # 添加一个bond类型的虚拟网卡，起名为mybond0,mode定义bond模式

  nmcli connection add con-name mybond0 ifname bond0 type bond mode active-backup ipv4.addresses 10.0.0.100/24 ...
  # 配置的时候添加ip地址，方式，网关等

  nmcli connection add con-name mybond0-eth1 ifname eth1 type bond-slave master bond0
  # 将eth1添加到bonding中

  nmcli connection delete <eth1之前的配置文件>
  # 删掉之前的eth1的配置文件，自动启用新配置的绑定bonding的eth1

  cat /proc/net/bonding/bond0
  # 查看bond0的绑定情况

  ```

- 网络组 NetWork Teaming
  - 网络组：是将多个网卡聚合在一起方法，从而实现容错和提高吞吐量，网络组不同于旧版的bonding技术，提供更好的性能和扩展性网络组由内核驱动和teamd守护进程实现
  - 多种方式 runner
    - broadcast
    - roundrobin
    - activebackup
    - loadbalance
    - lacp(implements the 802.3ad Link Aggregation Control Protocol)

  - 创建网络组示例：
  ```shell
  # 创建网络组接口
  nmcli con add type team con-name CNAME ifname INAME [config JSON]

  CNAME 连接名
  INAME 接口名
  JSON 指定runner方式，格式：'{"runner":{"name":"METHOD"}}'
  METHOD 可以是broadcast, roundrobin, activebackup, loadbalance, lacp

  # 创建port接口
  nmcli con add type team-slave con-name CNAME ifname INAME master TEAM

  CNAME 连接名，连接名若不指定，默认为team-slave-IFACE
  INAME 网络接口名
  TEAM 网络组接口名

  # 断开和启动
  nmcli dev dis INAME
  nmcli con up CNAME

  ----------------------------------------------------------------
  网络组示例：
  nmcli con add type team con-name myteam0 ifname team0 config '{"runner":{"name":"loadbalance"}}' ipv4.addresses 192.168.1.100/24 ipv4.method manual

  nmcli con add con-name team0-eth1 type team-slave ifname eth1 master team0

  nmcli con add con-name team0-eth2 type team-slave ifname eth2 master team0

  nmcli con up myteam0
  nmcli con up team0-eth1
  nmcli con up team0-eth2

  查看team状态
  teamdctl team0 state
  ``

- 网桥
  - 作用：网桥的作用是将多个设备串联在一起，实现通讯，隔离冲突域，相当于交换机
  - 配置实现网桥
  ```shell
  # 下载bridge-utils CentOS 8 无此包
  yum -y install bridge-utils

  # 查看网桥
  brctl show

  # 查看CAM(content addressable memory 内容可寻址存储器)表
  brctl showmacs br0

  # 添加和删除网桥
  brctl addbr | delbr br0

  # 添加和删除网桥中的网卡
  brctl addif | delif bro eth0

  # 默认br0 是down，必须启用
  ifconfig br0 up

  # 启用STP协议
  brctl stp br0 on
  ```
  - STP（生成树协议）
    - 交换机上的协议，用来防止广播风暴(回环)

### TCPdump的使用
- 概述：
  - TCPdump,全称dump the traffic on a network，是一个运行在linux平台可以根据使用需求对网络上传输的数据包进行捕获的抓包工具
- 功能：
  - 在Linux平台将网络中传输的数据包全部捕获过来进行分析
  - 支持网络层、传输层协议等协议捕获过滤
  - 数据发送和接收的主机、网卡和端口等各种过滤捕获数据规则
  - 提供and、or、not等语句进行逻辑组合捕获数据包或去掉不同的信息
  - 结合wireshark工具分析捕获的报文
```shell
# 不指定任何参数，默认监听第一块网卡经过的数据包。
tcpdump

# 监听特定网卡
tcpdump -i eth0

# 监听特定主机，监听主机10.0.0.100的通信包，注意：出入包都会被监听
tcpdump host 10.0.0.100

# 特定来源、目标地址的通信
# 特定来源
tcpdump src host hostname
# 特定目标
tcpdump dst host hostname
# 如果不指定src跟dst，那么来源或者目标是hostname的通信都会被监听
tcpdump host hostname

# 特定端口
tcpdump port 3000

# 监听tcp/udp，服务器上不同服务分别用了tcp，udp作为传输层
tcpdump tpc # 监听tcp协议报文

# 来源主机+端口+tcp，监听来自主机10.0.0.100在端口22上的tcp数据包
tcpdump tcp port 22 and src host 10.0.0.100

# 监听特定主机之间的通信
tcpdump ip host 10.0.0.101 and 10.0.0.102

# 10.0.0.101和除了10.0.0.1之外的主机之间的通信
tcpdump ip host 10.0.0.101 and ! 10.0.0.1

# 将tcpdump的数据包，重定向到一个文件中
tcpdump -i eth0 -nn port ! 22 -w test.cap
sz test.cap # 将虚拟机的文件传到本地

```

### curl工具
- 介绍：curl命令来自于英文词组"Commandline URL"的缩写，其功能是用于在shell终端界面中基于URL规则进行的文件传输工作，curl是一款综合的传输工具，可以上传，也可以下载，支持HTTP，HTTPS，FTP等三十余种常见协议

- 语法：`curl [options] <url>`
```shell
curl <url> 
# 获取指定网站的网页源码，默认GET请求

curl -v <url>
# 表示输出连接详情 

curl -O <url>
# 下载指定网站中的文件

curl -o filename <url>
# 将网页源码保存到指定文件中

curl -I https://www.baidu.com
# 打印指定网站的HTTP响应头信息

curl -Iv <rul>
# 同时打印HTTP请求和响应头信息

curl -i -X <Method> <url>
# 指定请求HTTP方法,并返回响应信息
```

### wget工具
- 介绍：Linux下的下载命令
- 语法：`wget [options] <url>`
```shell
wget <url>
# 将链接文件直接下载到当前路径

wget -O filename <url>
# 表示output输出为文件，后接文件名参数
```

### ubuntu网络配置
- 主机名
```shell
# 和CentOS7之后版本的指令，配置文件都一样
hostnamectl set-hostname ubuntu1804.magedu.org
# 用这个指令更改主机名后，配置文件hostname里的主机名会自动被更改

cat /etc/hostname
ubuntu1804.magedu.org
```

- 网卡名称
  - 默认ubuntu的网卡名称和CentOS 7类似
  - 修改网卡名称为传统命名方式：
  ```shell
  # 修改配置文件为下面形式
  vim /etc/default/grub
  GRUB_GMDLINE_LINUX="net.ifnames=0"
  # 或者sed修改
  sed -i.bak '/^GRUB_CMDLINE_LINUX=/s#"$#net.ifnames=0"#' /etc/default/grub

  # 生效新的grub.cfg文件
  grub-mkconfig -o /boot/grub/grub.cfg # 本质上是修改grub.cfg文件，在上面添加 net.ifnames=0的信息

  # 本质：grub文件相当与一个修改模板，通过grub-mkconfig指令使其调用grub模板去更改grub.cfg文件
  # 所以，实际上可以只修改grub.cfg文件，讲所有linux开头的行后添加net.ifnames=0，是一样的

  # 或者使用
  update-grub # 作用等同于grub-mkconfig -o /boot/grub/grub.cfg

  reboot # 最后重启生效
  ```

- 网卡配置
  ```shell
  # ubuntu20.04的网卡配置文件采用yaml格式，要求各级缩进必须严格统一

  # 官方文档参考：https//ubuntu.com/server/docs/network-configuration

  # ubuntu20.04网卡配置文件路径
  /etc/netplan/01-netcfg.yaml  # 配置文件命名格式：数字-netcfg.yaml

  # 配置文件内容 (严格控制缩进)
  network:
    ethernets:
      ens33:    # 更改网卡名
        dncp4:true   # 这个就是自动分配，动态网卡地址
    version:2
    renderer:networkd   # 选填

  # 配置之后，需要执行命令生效：
  netplan apply   # NAT模式下生效，桥接模式，需要配置动态地址

  # yaml格斯的常见数据结构：列表和字段
  # ubuntu20.04静态地址配置
  network:
    version: 2  #冒号后面要加空格
    renderer: networkd
    ethernets:
    eth0:
      addresses: [192.168.8.10/24,10.0.0.10/8] # 或者用下面两行，两种格式不能混用
      - 192.168.8.10/24 # 横线加空格，也是yaml中列表中元素的一种表现形式
      - 10.0.0.10/8
      gateway4: 192.168.8.1
      nameservers:
        search: [magedu.com, magedu.org]
        addresses: [180.76.76.76, 8.8.8.8, 1.1.1.1]
  ```
- 查看ip和gateway
```shell
ip addr
route -n
```

- 查看DNS
```shell
# 使用指令来看
systemd-resolve --status
```

- 配置多网卡静态ip并添加静态路由
```shell
# 编辑配置文件
vim /etc/netplan/01-eth1cfg.yaml

# 内容
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0: 
    dhcp4: no
    dhcp6: no
    addresses: [10.0.0.18/16]
    gateways:10.0.0.2
    nameservers:
      addresses: [223.6.6.6]
    eth1:
      dhcp4: no
      dhcp6: no
      addresses: [10.20.0.18/16]
      routes:
      - to: 10.30.0.0/16
        via: 10.20.0.1/16
      - to: 10.40.0.0/16
        via: 10.20.0.1/16
      - to: 10.50.0.0/16
        via: 10.20.0.1/16
      - to: 10.60.0.0/16
        via: 10.20.0.1/16

```
- 双网卡绑定
```
支持多网卡绑定其中模式

第一种模式：mod=0,即：（balance-rr） Round-robin policy（平衡论循环策略）
特点：传输数据包顺序是依次传输（即：第1个包走eth0，下一个包就走eth1...一直循环下去，知道最后一个传输完毕），此模式提供负载平衡和容错能力

第二种模式：mod=1,即：（active-backup）Active-backup policy（主-备份策略）
特点：只有一个设备处于活动状态，当一个宕机另一个马上由备份转换为主设备。mac地址是外部可见的，从外面看来，bond的mac地址是唯一的，以避免switch发生混乱。此模式只提供了容错能力；由此可见此算法的优点是提供网络连接的可用性，但是它的资源利用率较低，只有一个接口处于工作状态，在有N个网络接口的情况下，资源利用率为1/N。

第三种模式：mod=2，即：（balance-xor）XOR policy（平衡策略）
特点：基于指定的传输HASH策略传输数据包。缺省的策略是：（源MAC地址 XOR 目标MAC地址） % salve数量。其他的传输策略可以通过xmit_hash_policy选项指定，此模式提供负载平衡和容错能力

第四种模式：mod=3，即：broadcast（广播策略）
特点：在每个slave接口上传输每个数据包，此模式提供了容错能力

第五种模式：mod=4，即：（802.3ad）IEEE 802.3ad Dynamic link aggregation (IEEE 802.3ad 动态链接聚合)
特点：创建一个聚合组，它们共享同样的速率和双工设定。根据802.3ad规范将多个slave工作在同一个激活的聚合体下。
该模式必要条件：
条件1：ethtool持获取每个slave的速率和双工设定
条件2：switch支持IEEE 802.3ad Dynamic link aggregation
条件3；多数switch需要经过特定配置才能支持802.3ad模式

第六种模式：mod=5，即：（blance-tlb）Adaptive transmit load balancing （适配器传输负载均衡）
特点：不需要任何特别的switch支持的通道bonding。在每个slave上根据当前的负载（根据速度计算）分配外出流量。如果正在接收数据的slave出故障了，另一个slave接管失败的slave的MAC地址。
该模式的必要条件：
ethtool支持获取每个slave的速率

第七种模式：mod=6，即：（balance-alb）Adaption load balancing（适配器适应性负载均衡）
特点：该模式包含了balance-tlb模式，同时加上了针对IPV4流量的接收负载均衡（receive load balance，rlb），而不需要任何switch的支持
```
```shell
# 在Ubuntu中启用多网卡绑定，需要直接写文件
vim /etc/netplan/01-netcfg.yaml

# 配置文件内容
# This file describes the network interfaces available on your system
# for more information, see netplan(5)
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: no
      dhcp6: no
    eth1:
      dhcp4: no
      dhcp6: no

  bonds:
    bond0:
      interfaces:
        - eth0
        - eth1
      addresses: [10.0.0.18/16]
      gateways: 10.0.0.1
      nameservers:
        addresses: [223.6.6.6, 223.5.5.5]
      parameters:
        mode: active-backup
        mii-monitor-interval: 100  # 监控间隔

# 使其配置生效
netplan apply
```
```shell
# 查看生成的bond信息文件
cat /proc/net/bonding/bond0

``` 
- 网络测试诊断工具

  - 测试网络连通性
    - ping
  - 显示正确的路由表
    - ip route
  - 跟踪路由
    - traceroute
    - tracepath
    - mtr
  - 确定名称服务器使用
    - nslookup
    - host
    - dig
  - 抓包工具
    - tcpdump
    - wireshark
  - 安全扫描工具
    - nmap
    - netcat: 网络界的瑞士军刀

### NAT（Network Address Translation）技术。
- 前置知识科普
  - 私网ip：
    - 私有IP地址，如192.168.x.x、10.x.x.x、172.16.x.x至172.31.x.x
    - 特点：
      - 只能在内网/局域网通信，无法和互联网通信
  - 公网ip
    - 查询方式
      - Windows: 打开命令提示符（cmd），然后输入`nslookup myip.opendns.com resolver1.opendns.com`。这将使用OpenDNS的解析器来返回你的公网IP。
      - Linux/Unix/Mac: 打开终端，然后输入`dig +short myip.opendns.com @resolver1.opendns.com`。
- 概述：
  - NAT是一种在IP数据包通过路由器或防火墙时重新映射IP地址的技术。它允许一个内网（通常使用私有IP地址，如192.168.x.x、10.x.x.x、172.16.x.x至172.31.x.x）的多台设备共享一个公网IP地址进行外部通信。这样可以实现资源共享，也为IPv4地址的不足提供了临时解决方案。

- NAT(网络地址转换)的主要类型
  - 静态NAT
    - 为内部IP地址提供一个一对一的公网IP地址映射。通常用于需要对外提供服务的设备，如web服务器。
  - 动态NAT
    - 从一个可用的公网IP地址池中为内部设备动态分配公网IP地址。
  - PAT（Port Address Translation）/ NAPT (Network Address Port Translation)
    - 这是最常见的NAT类型，也经常被称为"端口转发"。在此类型的NAT中，多台内部设备共享单个公网IP地址。区分不同设备的方式是通过不同的源端口号。因此，这种方法不仅会转换IP地址，还会转换端口号。
    - 端口转发的工作流程
      - 当内部设备想要与外部世界通信时，它会发送一个数据包到NAT设备（通常是家用路由器）。
      - NAT设备将内部私有IP地址和端口号更改为公网IP地址和一个新的端口号，然后将数据包发送到外部网络。
      - 当外部服务器响应时，它会发送数据包回到路由器的公网IP地址和之前分配的端口号。
      - 路由器使用NAT表查找原始的内部IP地址和端口，然后将响应转发给正确的内部设备。
  
- 端口映射的应用场景
  - 内网服务器对外发布
  - 内网设备，从外部进行远程管理
  - 内网监控视频，从外部取流


## 软件管理
- 内容概述
  - 软件运行环境
  - 软件包基础
  - rpm包管理
  - yum和dnf管理
  - 定制yum仓库
  - 编译安装
  - Ubuntu软件管理

### 软件运行和编译
- 软件相关概念
  - ABI：Application Binary Interface（应用程序的二进制接口）
  - Windows与Linux不兼容
    - ELF（Executable and Linkable Format）Linux
    - PE（Portable Executable）Windows
    - 解释；在不同的系统中，二进制的格式是不同的，比如同一段二进制数据，可能含义不同，有的代指指令，有的指代数值。
    ```
    查看软件的文件信息（包含二进制格式）

    # file /bin/hostname
    ```

  - API：Application Programming Interface（应用程序的开发接口）
    - API可以在各种不同的操作系统上实现给应用程序提供完全相同的接口，由于在Linux和Windows上的API是不同的，导致软件在两个操作系统上无法兼容，为了实现兼容，出现了POSIX
  - POSIX：Portable Operating System Interface
    - 可移植操作系统接口，定义了操作系统应该为应用程式提供的接口标准，是IEEE为要在各种UNIX操作系统上运行的软件而定义的一系列API标准的总称。Linux和Windows都要实现基本的POSIX标准，程序就在源代码级别可移植了。
  - 开发语言
    - 系统级开发语言：汇编语言；C；C++
    - 应用级开发语言：java； Python； go； PHP； Perl； delphi； basic； ruby； bash
  
- C语言程序的实现过程
  - 整体过程：
    - C程序源代码 -> 预处理 -> 编译 -> 汇编 -> 链接
  - 预处理(pre-processing)
    - 将所有的#define删除，并且展开所有的宏定义
    - 处理所有的条件预编译指令，比如#ifdef #elif #else #endif等
    - 处理#include预编译指令，将被包含的文件插入到预编译指令的位置。
    - 删除所有的注释"/ /"和"/* */"
    - 添加行号和文件标识，以便编译时产生调试用的行号及编译错误警告行号
    - 保留所有的#pragma编译指令，因为编译器需要使用它们
    - 预处理之后，形成如：hello.i的（文本）文件
  - 编译(Compiling)
    - 编译过程就是把预处理完的文件进行一系列的词法分析，语法分析，语义分析及优化后，最后生成相应的汇编代码
    - 编译后，形成如：hello.s的汇编程序的文本文件
  - 汇编(Assembling)
    - 汇编器是将汇编代码转变成机器可以执行的命令，每一个汇编语句几乎都对应一条机器指令。汇编相对于编译过程比较简单，根据汇编指令和机器指令的对照表一一翻译即可。
    - 汇编之后,形成如；hello.o的二进制文件
  - 链接(Linking)
    - 通过调用链接器id来链接程序运行需要的一大堆目标文件，以及所依赖的其它库文件，最后生成可执行文件
  ``` bash
  范例：gcc编译过程
  
  # 分步骤编译运行
  gcc -E hello.c -o hello.i   # 对hello.c文件进行预处理，生成hello.i文件
  gcc -S hello.i -o hello.s   # 对预处理文件进行编译，生成了汇编文件
  gcc -C hello.s -o hello.o   # 对汇编文件进行编译，生成了目标文件
  gcc hello.o -o hello    # 对目标文件进行链接，生成可执行文件

  # 一步实现编译过程
  gcc hello.c -o hello  # 直接编译链接成可执行目标文件
  ```

- 软件模块的静态和动态链接
  - 定义：链接主要作用是把各个模块之间相互引用的部分处理好，使得各个模块之间能够正确的衔接，分为静态和动态链接
  - 静态链接
    - 将程序和依赖文件打包成一个文件
  - 动态链接
    - 每个依赖文件是一个个独立文件，程序按需调用这些依赖文件
    ```
    查询文件所依赖的所有依赖库

    # ldd <要查询的文件>
    ```

### 软件包和包管理器  
- 软件包介绍：开源软件最初只提供了打包的源码文件，用户必须自己编译每个想在GNU/LINUX上运行的软件。用户急需系统能提供一种更加便利的方法来管理这些软件，当Debian诞生时，这样一个管理工具dpkg也就应运而生,可用来管理deb后缀的“包”文件。
<br>从而著名的“package”概念第一次出现在GNU/Linux系统中，稍后Red Hat才开发自己的rpm包管理系统

- 软件包位置：
  - 一般在光盘的Appstream和BaseOS中
  - 查看光盘内文件：先挂载光盘再查看
  ```
  mount /dev/sr0 /mnt
  ```

- 软件包中的文件分类
  - 二进制文件
  - 库文件
  - 配置文件
  - 帮助文件
  ```
  范例：利用cpio工具查看包文件列表

  # rpm2cpio 包文件|cpio -itv     预览包内文件
  # rpm2cpio 包文件|cpio -id "*.conf" 释放包内文件

  在Rocky中，一般cpio和rpm2cpio都是安装好的
  ```

- 程序包管理器
  - 功能：将编译好的应用程序的各组成文件打包一个或几个程序包文件，利用包管理器可以方便快捷地实现程序包的安装，卸载，查询，升级，校验等管理操作。
  - 主流的程序包管理器
    - redhat:rpm文件，rpm包管理器
    - debian:deb文件，dpkg包管理器

- 包命名
  - rpm包命名方式：
    - name-VERSION-release.arch.rpm
    - 即：[名称]-[版本]-[发布].[架构].rpm
    - 名称 (Name)：这是软件/包的名称。例如，对于 httpd (Apache HTTP 服务器) 的 RPM，名称就是 httpd
    - 版本 (Version): 这表示软件的主版本号。例如，如果 Apache HTTP 服务器的版本是 2.4.6，则版本号就是 2.4.6。
    - 发布 (Release): 这表示软件的发行版或修订版。当软件包维护者对软件进行修改，例如修复 bug 或进行优化，但没有更改主版本号时，就会更改这个数字。例如，对于第一次打包的 2.4.6 版本的 Apache，发布版本可能是 1。如果该包稍后被重新打包（例如，由于一个修复），则发布版本可能会增加到 2。
    - 架构 (Architecture): 这描述了软件编译的目标硬件架构。常见的值包括：
      - i386, i686 - 用于 32 位 Intel/AMD 处理器
      - x86_64 - 用于 64 位 Intel/AMD 处理器
      - noarch - 表示软件是架构无关的，例如纯脚本软件包
      - 还有其他的，例如 arm, ppc 等，表示其他硬件架构
    - .rpm: 这是文件的扩展名，表明这是一个 RPM 文件。

- 包的分类
  - Application-VERSION-ARCH.rpm: 主包
  - Application-devel-VERSION-ARCH.rpm: 开发子包
  - Application-utils-VERSION-ARCH.rpm: 其他子包
  - Appllication-libs-VERSION-ARCH.rpm: 其他子包

- 包的依赖
  - 软件包之间可能存在依赖关系，甚至循环依赖，即：A包依赖B包，B包依赖C包，C包依赖A包。安装软件包时，会因为缺少依赖的包，而导致安装包的失败。
  - 解决依赖包管理工具：
    - yum:rpm包管理器的前端工具
    - dnf：Fedora 18+ rpm包管理器前端管理工具，CentOS 8版本代替yum
    - apt：deb包管理器前端工具
    - zypper：suse上的rpm包管理工具

- 程序包管理器相关文件
  - 包文件组成（每个包独有）
    - 包内文件
    - 元素据，如：包的名称，版本，依赖性，描述等
    - 可能会有包安装或卸载时运行的脚本
  - 数据库（公共）：/var/lib/rpm
    - 程序包名称及版本
    - 依赖关系
    - 功能说明
    - 包安装后生成的各文件路径及校验码信息

- 第三方组织提供
  - Fedora-EPEL：Extra Packages for Enterprise Linux
  ``` 
  https://fedoraproject.org/wiki/EPEL
  https://mirrors.aliyun.com/epel/
  https://mirrors.cloud.tencent.com/epel/
  ```
  - SCL:Software Collections，提供较高版本的第三方软件
  ```
  https://wiki.centos.org/SpecialInterestGroup/SCLo
  ```
  - Community Enterprise Linux Repository:支持最新的内核和硬件相关包
  ```
  http://www.elrepo.org
  ```

- 软件项目官方站点
```shell
http://yum.mariadb.org/10.4/centos8-amd64/rpms/
http://repo.mysql.com/yum/mysql-8.0-community/el/8/x86_64/
```

- 搜索引擎
```
http://pkgs.org
http://rpmfind.net
http://rpm.pbone.net
https://sourceforge.net/
```

- 自己制作
  - 将源码文件，利用工具，如：rpmbuild,fpm等工具制作成rpm包文件。


### rpm包管理器
- CentOS系统上使用rpm命令管理程序包
- 功能：安装，卸载，升级，查询，校验，数据库维护
  - 问题：一般来说，rpm管理器更多的是使用查询功能，而很少使用安装功能，因为rpm包管理器不支持包的依赖关系
  ```
  使用rpm包管理器 - 安装

  # rpm -i <rpm包名>
  # rpm -ivh <rpm包名>  -- 能够看到安装过程

  查询安装是否成功

  # rpm -q <软件名>   -- 这里不是包名，仅仅是开头的软件名
  # rpm -qa | grep '软件名'
  -- 使用qa查询所有安装过的包，通过grep筛选确认是否安装成功

  rpm管理器 - 卸载

  # rpm -e <软件名>
  -- 还是因为依赖关系问题，所以一般不使用rpm管理器进行安装，卸载

  重点：rpm管理器 - 查询

  # rpm -ql <软件名>
  -- 查询这个软件包中包含的文件列表

  # rpm -q --scripts <软件名>
  -- 查看这个软件包中的脚本文件

  # rpm -qi <软件名>
  -- 查看软件包的详细信息

  # rpm -qf <软件名>
  -- 可以查询到磁盘文件来源于哪个包

  # rpm -qc <软件名>
  -- 只查看软件包里的配置文件

  # rpm -qd <软件名>
  -- 只查看软件包里的文档

  # rpm -qa --last
  -- 查看最近安装的所有包
  ```

- 包校验
```
# rpm -K <软件名>
-- 查看软件的rpm包是否合法

# rpm -V <软件名>
-- 查看软件在安装后，是否被改过

# rpm -Va
-- 系统所有包，安装后，被改过的都列出来
```

### yum和dnf
- 作用：CentOS使用yum,dnf解决rpm的包依赖关系
- YUM：Yellowdog Update Modifier，rpm的前端程序，可解决软件包相关依赖性，可在多个库之间定位软件包，up2date的替代工具，CentOS8用dnf代替了yum，不过保留了和yun的兼容性，配置也是通用的
- yum和rpm的关系：
  - yum依赖于rpm，安装时间接调用rpm，如果rpm被破环，yum也会失效
- yum/dnf 工作原理
  - yum/dnf是基于C/S模式
    - yum 服务器存放rpm包和相关包的元数据库
    - yum 客户端访问yum服务器进行安装或查询等
  - yum 实现过程：先在yum服务器上创建yum repository（仓库），在仓库中事先存储了众多rpm包（一般放在Packages目录下），以及包的相关的元数据文件（放置在特定目录repodata下），当yum客户端利用yum/dnf工具进行安装时，会自动下载repodata中的元数据，查询元数据是否存在相关的包及依赖关系，自动从仓库中找到相关包下载并安装。
- yum客户端配置
  - yum客户端配置文件
  ```txt

  # /etc/yum.conf      为所有仓库提供公共配置
  # /etc/yum.repos.d/*.repo:    为每个仓库提供配置文件

  每个仓库对应一个配置文件
  ```
  - repo仓库配置文件内容
  ```shell
  [repositoryID]
  name=Some name for this repository
  baseurl=url://path/to/repository
  enabled={1|0}   默认为1，0表示禁用该仓库
  gpgcheck={1|0}  默认1，检查包是否合法,0表示不检查

  gpgcheck必须配合gpgkey使用，否则就设置0，不检查

  gpgkey=URL

  注意：yum仓库指向路径一定必须是repodata目录所在目录

  ----------------------------------------------

  相关变量

  yum的repo配置文件中可用的变量
  $releasever: 当前OS的发行版的主版本号，如：8，7，6
  $arch: CPU架构，如：aarch64,i586,i686,x86_64
  $basearch: 系统基础平台；i386,x86_64
  $contentdir: 表示目录，比如：centos-8,centos-7
  $YUM0-$YUM9: 自定义变量
  ```

  - yum相关指令
  ```txt
  # yum install <软件名>    下载软件

  # yum remove <软件名>     卸载软件

  # yum list <软件名>     查询软件
  支持模糊查询，通配符，比如：msm* 表示msm开头的软件
  如果查询到的yum源前面有@，说明已经安装，反之，没安装

  # yum provides <软件名路径>  查询硬盘上没安装的软件来自于哪个包

  # yum -y install --downloadonly --downloaddir=路径 <软件名>
  下载某个软件的包到指定目录，但是不安装

  # yum -y install /data/httpd/*.rpm
  使用yum下载目录下的所有rpm包

  # yum info <软件名>
  查询软件说明，相当于rpm -qi
  
  # yum search [string1] 
  搜索和关键词相关的包

  # dnf repoquery -l <软件包>
  查看未安装的软件包，安装后会在硬盘生成哪些文件

  # dnf clean all
  清理软件包元信息缓存

  # yum history
  查看安装的历史

  # yum history info <history的编号>
  根据编号查看历史下载的具体细节

  # yum updatefinfo
  查看互联网上新版本的软件信息

  # yum grouplist
  查看包组

  # yum groupinstall <包组名>
  安装包组

  # yum groupremove <包组名>
  卸载包组
  ```

- yum安装失败的原因
  - yum 配置格式有错
  - yum 元数据过旧，清理缓存
  - yum 源出问题，或网络有问题

### 实现私用yum仓库
```
步骤一：安装阿帕奇httpd,使其拥有web共享功能

步骤二：web共享的目录在 /var/www/html 下

步骤三：将需要的yum源下载到该目录下
```
### 程序包编译
- C、C++的源码编译：使用make项目管理器
<br>configure脚本 --> Makefile.in --> Makefile
  - 相关开发工具
    - autoconf: 生成configure脚本
    - automake：生成Makefile.in
  
- java的源码编译：使用maven
- 源码编译的好处
  - 可以实现软件功能的私人定制
  - 可以控制安装路径
- C语言源代码编译安装过程
<br>利用编译工具，通常只需要三个大的步骤
  - ./configure
    - 通过选项传递参数，指定安装路径、启用特性等；执行时会参考用户的指定以及Makefile.in文件生成Makefile
    - 检查依赖到的外部环境，如依赖的软件包
  - make 根据Makefile文件，会检车依赖的环境，进行构建应用程序
  - make install 复制文件到相应路径

- 编译安装实战案例（tree安装）：
```
1. 到官网使用wget download_url，下载新版tree的源码到当前目录并解压

# wget download_url
# tar xvf tree-1.8.0.tgz

2. 进入解压后的目录，阅读README和INSTALL

# cd tree-1.8.0/
# less README
# less INSTALL

3. 编译准备，修改自定义安装地址，或指定功能

# vim Makefile
由于tree文件源码比较简单，因此不需要自己生成Makefile文件，解压目录下直接有
# prefix = /apps/tree
指定安装到这个目录下

4.编译

# make

5 安装

# make install

6. 修改PATH变量

6-1:方法一 使用软链接
# echo $PATH
# ln -s 软件安装路径 环境变量路径

6-2：方法二 修改配置文件
# vim /etc/profile.d/tree.sh
添加PATH=/apps/tree/bin:$PATH
# ./etc/profile.d/tree.sh  使文件生效

7.清除缓存

# hash -r
```

### Ubuntu软件包管理工具
- 概述
```
dpkg  相当于rpm，不支持包的依赖关系的解决
apt   相当于yum，支持包的依赖解决
```
- dpkg 包管理器
```
帮助参看：man dpkg

安装包，不支持包的依赖

# dpkg -i package.deb

删除包（包括配置文件）

# dpkg -P package

列出当前已安装的包，类似rpm -qa

# dpkg -l package

列出该包中所包含的所有文件 类似rpm -ql

# dpkg -L package

查看包的具体信息

# dpkg -s package

查询软件来自于哪个包

# dpkg -S software_name
```

- apt
```
安装软件包

# apt install

卸载移除软件包及其配置文件

# apt purge

刷新存储库索引

# apt update

升级所有可升级的软件包

# apt upgrade

搜索应用程序

# apt search


```
- Ubuntu 配置文件
```
ubuntu软件源的下载地址，默认外网
/etc/apt/sources.list

更改国内资源的方式：直接copy，

```

## Service and Process Management
### GRUB
- 什么是grub：GRUB (Grand Unified Bootloader) 是一个多操作系统引导程序。它是许多Unix和Linux系统上的默认引导加载器。GRUB的主要功能是允许用户在计算机启动时选择多个操作系统或不同的内核配置。
- grub 配置文件
  - /ect/default/grub   设置基本的grub配置
  - /etc/grub.d   设置更详细的引导设置
  - /boot/grub2/grub.cfg 
  - grub2-mkconfig -o /boot/grub2/grub.cfg
  ```
  /etc/default/grub 默认配置文件参数

  GRUB_TIMEOUT=5
  GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
  GRUB_DEFAULT=saved
  GRUB_DISABLE_SUBMENU=true
  GRUB_TERMINAL_OUTPUT="console"
  GRUB_CMDLINE_LINUX="crashkernel=1G-4G:192M,4G-64G:256M,64G-:512M resume=/dev/mapper/rl_192-swap rd.lvm.lv=rl_192/root rd.lvm.lv=rl_192/swap net.ifnames=0" 
  (net.ifnames=0 是修改网卡名称eth0的参数设置)
  GRUB_DISABLE_RECOVERY="true"
  GRUB_ENABLE_BLSCFG=true

  ----------------------------------------------

  查看默认引导内核的版本号
  
  # grub2-editenv list

  ```

- 忘记root密码，如何重置
  - 步骤一：在启动选择项时，选择需要引导的内核，然后按e进入选择编辑项
  ![Alt text](images/image10.png)
  - 步骤二：找到内核参数，在后面填写rd.break，然后按Ctrl-x进行启动
  ![Alt text](images/image11.png)
  - 步骤三：启动之后，目前的根目录是挂载在内存中虚拟的文件系统上，应该挂载到硬盘的根目录上，使用mount
  - 步骤四：进入硬盘的根目录后，就可以重置passwd了使用：echo <密码> | passwd --stdin root


### 进程管理
#### 进程的概念与进程查看
- 进程的概念：进程是运行中的程序，从程序开始运行到终止的整个生命周期是可管理的
  - 例如C程序的启动是从main函数开始
    - int main(int agrc,char*argv[])
  - 终止的方式并不唯一，分为正常终止和异常终止
    - 正常终止也分为从main返回，调用exit等方式
    - 异常终止分为abort、接收信号等
- 进程的查看
  - 查看命令
    - ps(process status)
    ```
    查看所有进程的状态

    # ps -e

    查看所有进程状态的详细信息
    
    # ps -ef

    示例：
    UID          PID    PPID  C STIME TTY          TIME CMD
    root           1       0  0 Aug27 ?        00:00:02 /usr/lib/systemd/systemd --switched-root --system --deserialize 31
    root           2       0  0 Aug27 ?        00:00:00 [kthreadd]
    root           3       2  0 Aug27 ?        00:00:00 [rcu_gp]
    root           4       2  0 Aug27 ?        00:00:00 [rcu_par_gp]
    root           5       2  0 Aug27 ?        00:00:00 [slub_flushwq]
    root           6       2  0 Aug27 ?        00:00:00 [netns]
    root           8       2  0 Aug27 ?        00:00:00 [kworker/0:0H-events_highpri]
    root          10       2  0 Aug27 ?        00:00:00 [kworker/0:1H-events_highpri]

    参数详解：

    UID：有效用户id
    PID：进程id
    PPID：父进程id

    查看线程情况

    # ps -eLf


    ```
    - pstree
    - top 更全面的看到进程的运行状态
    ```
    top的详解

    示例：
    top - 10:58:20 up 19:40,  3 users,  load average: 0.00, 0.00, 0.00
    Tasks: 224 total,   1 running, 223 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
    MiB Mem :   1750.8 total,    697.8 free,    531.6 used,    688.5 buff/cache
    MiB Swap:   2072.0 total,   2072.0 free,      0.0 used.   1219.2 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                                 
    17 root      20   0       0      0      0 I   0.3   0.0   0:01.94 rcu_preempt                                                                                             
    836 root      20   0  241000  11256   7496 S   0.3   0.6   1:08.54 vmtoolsd                                                                                                
    1 root      20   0  107588  17084  10600 S   0.0   1.0   0:02.61 systemd                                                                                                 
    2 root      20   0       0      0      0 S   0.0   0.0   0:00.03 kthreadd                                                                                                
    3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp                                                                                                  
    4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp 

    参数详解：

    up 19:40：意味着系统已经运行了19小时40分钟。

    3 users：表示当前系统有两个用户正在登录

    load average：平均负载，后面跟3个值，分别表示1分钟，5分钟，15分钟的负载情况，1表示满负荷，用来查看系统的繁忙程度

    Load Average 是如何计算的？
    load average的值反映了在特定时间段内的平均就绪进程数。"就绪"意味着进程要么正在运行，要么在等待CPU时间来运行。这也包括等待I/O的进程（例如，等待硬盘、网络等）
    
    如何解释 Load Average？
    解释这些数字最简单的方法是与你的CPU核心数进行比较。

    如果你的系统只有一个CPU核心，那么load average为1意味着你的系统完全饱和。
    如果你有4个CPU核心，那么数字4.00意味着所有核心都被完全利用。

    一些基本的解读规则：

    如果1分钟的负载（第一个数字）远高于5或15分钟的负载，系统的负载可能正在增加。
    如果1分钟的负载（第一个数字）远低于5或15分钟的负载，系统的负载可能正在减少。
    负载高于你的CPU核心数可能意味着系统上有竞争或者某种瓶颈。

    这个数字是好是坏？
    如果load average低于核心数，通常意味着系统有剩余的计算能力。
    如果load average和核心数大致相等，系统可能达到了它的最大吞吐量。
    如果load average远大于核心数，这可能意味着系统过载。

    Tasks:224 total :表示共有224个进程在运行

    %Cpu(s)：后面的数据表示Cpu资源使用和分配的百分比；（s）表示多核cpu的使用平均值，按数字1,可以分开显示每个cpu的使用情况

    MiB Mem：表示内存的使用分配情况
    MiB Swap：表示swap虚拟内存的使用情况

    默认每3s更新依次数据，按s键可以自定义输入更新的频率时间


    ```
  - 结论
    - 进程也是树形结构
    - 进程和权限有着密不可分的关系
#### 进程的控制命令
-  前置知识：
   - 程序：由程序员编写的一组稳定的指令，存在磁盘中，他可能会也可能不会成为作业
   - 作业：从一个程序被选中执行，到其运行结束并执行下一程序这个过程中，该程序被成为作业
     - 作业的几种状态：
       - 被选中后，驻留在磁盘上等待被调入内存
       - 在内存中，等待CPU执行
       - 驻留在内存或磁盘中，等待IO事件
       -  在CPU中执行（进程）
   - 进程：运行中的程序，在运行中等待被CPU调用，或正在被CPU执行的作业，只要作业装入内存就成为一个进程
   - 三者之间的关系：
     - 作业是一种特殊状态的程序，即被选中的程序
     - 进程是一种特殊状态的作业，即进入内存的作业
- 进程的优先级调整
  - nice 范围从-20到19，值越小优先级越高，抢占资源越多
  ```
  更改进程执行的优先级

  # nice -n 数值 ./程序名称
  ```
  - renice重新设置优先级
  ```
  更改正在运行的进程执行的优先级
  
  # renice -n 数值 ./程序名称

  ```
- 进程的作业控制
  - jobs
  - &符号
  ```
  将进程调整为后台运行，这样前台的终端仍然能执行其他指令

  # ./a.sh &

  将后台的进程调回前台运行

  # jobs      先查看后台运行的进程
  # fg 数值   这个数值是jobs查询后，进程前边的显示数值

  将前台进程调回后台，同时停止

  组合键：ctrl + z

  重新启动停止的进程，并在后台运行（在前台运行是fg）

  # bg 数值
  ```
#### 进程的通信方式——信号
- 信号是进程间通信方式之一，典型用法：终端用户输入终端命令，通过信号机制停止一个程序的运行
- 使用信号的常用快捷键和命令
```
查看信号

# kill -l

其中；SIGINT 通知前台进程组终止进程 ctrl + c
SiGKILL立即结束程序，不能被阻塞和处理 kill -9 pid
```

#### screen和系统日志
- screen
  - 作用：
    - 会话持久性：即使你断开SSH连接或关闭终端，screen 会话中运行的程序仍然可以继续运行。这对于长时间运行的任务或持久服务非常有用。
    - 多窗口管理：你可以在一个screen会话内创建多个窗口，并在它们之间轻松切换。
    - 会话分享与附加：你可以随时从不同的终端附加到一个正在运行的screen会话。这对于多用户协作或远程故障排查非常有用。
    - 
```
启动一个新的会话

# screen

列出当前所有的screen会话

# screen -ls

重新连接到一个已经存在的screen会话。

# screen -r [session_id]

创建一个新会话，并给它命名

# screen -S [session_name]

从当前会话中断（但不停止会话）

Ctrl a + d
```

- 系统日志
```
系统常规日志

# ls /var/log/messages

内核启动信息

# ls /var/log/dmesg

系统安全日志

# ls /var/log/secure

journalctl - 日志查看工具

# journalctl -u sshd --no-pager

-u：查看指定服务的日志
--no-pager：默认使用分页模式查看日志，使用no-pager之后，可以将内容重定向到文件或使用管道，进行文本处理
```

#### 服务管理工具systemctl
- 服务（提供常见功能的守护进程）集中管理工具
  - service CentOS 6及以前
  - systemctl CentOS 7之后
  ```
  systemctl 常见操作

  # systemctl status service_name

  # systemctl start service_name

  # systemctl stop service_name

  # systemctl restart service_name

  # systemctl reload service_name

  # systemctl enable service_name  //开机自动启动

  # systemctl disable service_name

  服务级别

  配置文件：/lib/systemd/system/*.target

  runlevel[0-6].target -> 不同的状态

  查看当前服务的级别

  # systemctl get-default

  修改当前服务级别
  # systemctl set-default multi-user.target
  ```

### 进程，系统性能和计划任务
#### 进程和内存管理
- 内核功能：进程管理、内存管理、文件系统、网络功能、驱动程序、安全功能等
- 什么是进程：
  - Process：运行中的程序的一个副本，是被载入内存的一个指令的集合，是资源分配的单位
    - 进程ID(Process ID，PID)号码被用来标记各个进程(系统自动分配)
    - UID、GID、和SElinux语境决定对文件系统的存取和访问权限
    - 通常从执行进程的用户来继承
    - 存在生命周期
  - 进程创建
    - init：第一个进程（从CentOS 7之后，为systemd）
    - 进程：都是由其父进程创建，fork()，父子关系，COW(copy on wirte)
      - 一般来说，进程是由父进程调用fork()函数创建的，创建的时候基于COW机制
      - 前期，子进程和父进程共有一个内存空间，当数据发生变化的时候，子进程拷贝父进程的信息，生成子进程会给子进程分配新的内存空间
      - COW详解：Copy-On-Write 是一种计算机程序优化策略，它最大限度地延迟数据的复制，直到真正需要时才进行。当 fork() 被调用时，父进程的页表（内存页的索引）会被复制到子进程，但是物理内存页并不复制。取而代之的是，父进程和子进程都使用相同的物理页，这些页都标记为只读。
      <br>
      <br>只有当父进程或子进程试图修改这些只读页中的某个值时，操作系统才会为写操作创建一个新的物理页（实际的复制操作），然后更新相应的页表条目以指向新的物理页。这就是为什么它被称为 Copy-On-Write：只有在真正需要写入时，数据才被复制。

- 进程，线程和协程
![Alt text](images/image12.png)
  - 进程 (Process)
    - 定义：进程是计算机中的程序关于其运行时的状态的一个实例。它是系统进行资源分配和调度的基本单位。每个进程都有自己的私有地址空间、代码、开放的文件、挂起的信号等。
    - 隔离：每个进程在其自己的地址空间中运行，这意味着一个进程不能直接访问另一个进程的变量和数据结构。如果一个进程需要另一个进程的数据，它们必须通过进程间通信（IPC）机制，例如管道、信号、套接字等。
  - 线程 (Thread)
    - 定义：线程是进程内部的执行单位。一个进程可以拥有多个线程，这些线程共享进程的地址空间和资源，但每个线程都有自己的程序计数器、寄存器集和栈。
    - 多线程：在多线程应用中，进程中的所有线程可以同时访问进程级的资源如堆。这允许更快的数据交换，但也增加了同步的复杂性，因为线程需要避免争用条件和其他并发相关的问题。
  - 协程 (Coroutine)
    - 定义：协程是一种轻量级的"线程"，但它的调度完全由用户控制，而不是由操作系统内核控制。协程为并发操作提供了方便，但没有真正的并行执行线程或进程那样的开销。
    - 优势：由于协程的调度不涉及内核模式和用户模式之间的切换，因此上下文切换通常比线程更快、更轻便。协程也能有效地管理大量的并发任务，因为它们在内存使用和开销上比线程更为轻量。
  - 关系：
    - 进程与线程：线程是进程的子集。每个进程至少有一个线程（通常称为主线程），但可以有更多线程。线程共享父进程的内存空间。
    - 线程与协程：协程可以被认为是“轻量级线程”。与线程不同，所有协程都运行在一个线程之内，并且由该线程的代码明确地调度。
    - 进程与协程：协程为实现进程内部的并发提供了一种手段，但与进程相比，它们共享相同的地址空间。
  - 区别：
    - 进程和线程的执行顺序是由操作系统决定和控制的
    - 协程的执行则是由程序员可以去控制的
  ```
  线程的查看

  # pstree -p     其中花括号形式的就是线程，没有花括号则说明是单线程

  通过文件查看线程信息

  # cat /proc/PID/status | grep -i threads

  通过进程PID，查找该进程文件所在路径
  
  # ll /proc/PID/exe

  直接查找指定程序的进程PID

  # pidof 程序名
  ```

- 进程结构（后续补全，暂略）
- 进程相关概念
  - Page Frame：页框，给进程分配的内存最小单位
  ```
  查看page的大小

  # getconf -a | grep -i size
  ```

  - 物理地址空间和虚拟地址空间 
    - MMU：Memory Management Unit 负责虚拟地址转换为物理地址（MMU是CPU的一个硬件组件）
    - 程序在访问一个内存地址指向的内存时，CPU不是直接把这个地址送到内存总线上，而是送到MMU，然后把这个内存地址映射到实际物理内存地址上，然后通过总线再去访问内存，程序操作的地方称为虚拟内存地址
    - TLB：Translation Lookaside Buffer 翻译后备缓冲器，用于保存虚拟地址和物理地址映射关系的缓存
  
  - 用户和内核空间
    - 例如：32位的操作系统，最大内存空间是4G，其中0-3G是用户空间（进程虚拟内存空间），3-4G是内核空间
    - 内存的结构
      - VMA_1:代码段
      - VMA_2:数据段,BSS,堆
      - VMA_3：栈
    - 每个进程都包括5种不同的数据段
      - 代码段：用来存放可执行文件的操作指令，也就是说它是可执行程序在内存中的镜像。代码段需要防止在运行时被非法修改，所以只准许读取操作，而不允许写入(修改)操作--它不是可写的
      - 数据段：用来存放可执行文件中已初始化全局变量，换句话说就是存放程序静态分配的变量和全局变量
      - BSS段：包含了程序中未初始化的全局变量，在内存中bss段全部置零
      - 堆(heap)：存放数组和对象，堆适用于存放进程运行中被动态分配的内存段，它的大小并不固定，可动态扩张或缩减。当进程调用malloc等函数分配内存时，新分配的内存就被动态添加到堆上；当利用free等函数释放内存时，被释放的内存从堆中被剔除
      - 栈：栈是用户存放程序临时创建的局部变量，也就是说我们函数括弧{}中定义的变量如：函数体中local声明的变量。除此之外，在函数被调用时，其参数也会被压入发起调用的进程栈中，并且待到调用结束后，函数的返回值也会被存放会栈中。由于栈的后进先出的特点，所以特别方便用来保存/恢复调用现场。可以把堆栈看成一个寄存、交换临时数据的内存区
    ![Alt text](images/image13.png)
    ![Alt text](images/image14.png)
