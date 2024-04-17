## 计划任务
### 一次性任务
#### at
- 指定时间点，执行一次性任务
- at 工具
    - 由包at提供
    - 依赖与atd服务，需要启动才能实现at任务
    - at队列存放在/var/spool/at目录中

- 使用前需要确认atd.service处于running状态
```shell
systemctl status atd.service
```

- at命令
```shell
at [option] TIME    # ctrl + D 结束并完成任务设置

# 常用选项
-l          # 列出未执行的一次性任务， 等价于atq命令
-c <编号>    # 查看指定编号的计划任务的具体内容
-d <编号>    # 删除指定编号的计划任务， 等价于atrm + 编号 
-f file     # at -f a.txt 15:20 等机于at 15:20 < a.txt
-m          # 当任务完成后，即使没有标准输出，也会给用户发邮件 

# 非交互方式实现计划任务
echo hello | at 14:30

echo wall hello | at 14:30 # wall 命令是广播，会在所有终端屏幕上出现
```

- at 时间格式
```shell
HH:MM               # 若时刻以过，则明天的此时执行任务

HH:MM  YYYY-MM-DD   # 规定某年某月 某天的特殊时刻执行该任务，不支持到秒，最小到分钟

now+#{minutes, hours, days, OR weeks}

```

- 注意：
    - 作业执行命令的结果中的标准输出和错误以执行任务的用户的身份，发邮件通知给root
    - 默认CentOS8最小化安装没有安装邮件服务，需自行安装
    ```shell
    dnf install postfix -y
    systemctl enable --now postfix

    # 安装mail
    sudo apt install mailutils
    ```
    - 创建的at任务，文件在`/var/spool/at`目录下 
    - 执行任务时，PATH变量和当前定义任务的用户身份一致

-  /etc/at.{allow, deny} 控制用户是否能执行at任务
    - 白名单：/etc/at.allow , 默认不存在，只有该文件中的用户才能执行at命令
    - 黑名单：默认存在，拒绝文件中的用户执行at命令
    - 如果两个文件都不存在，则只有root能够执行at命令 
    - 白名单的优先级高于黑名单



#### batch
- 系统自行选择空闲时间去执行此处指定的任务


### 周期性计划任务cron
- 周期性计划任务cron相关的程序包
    - cronie：主程序包，提供crond守护进程及相关辅助工具
    - crontabs：包含CentOS提供系统维护任务
    - cronie-anacron:cronie的补充程序，用于监控cronie的任务执行状态，如：cronie中的任务在过去该运行的时间点未能正常运行，则anacron会随后启动一次任务

- cron依赖于crond服务，确保crond守护处于运行状态

#### CentOS中的cron
- 有/etc/cron.deny，可以给cron设置黑名单 （Ubuntu默认没有该文件）
- run-parts <dir>  立即执行目录中所有脚本，要求目录内脚本有执行权限 （Ubuntu默认没有该文件）

- cron任务分为
    - 系统cron任务：系统维护作业， /etc/crontab（总配置文件） /etc/cron.d/目录下，自行创建 (子配置文件 )
    - 用户cron任务：保存在/var/spool/cron/USERNAME, 利用crontab命令管理
    
- 计划任务日志：`/var/log/cron`

- cron配置文件编辑
```shell
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

# 支持时间格式
1. 逗号分隔
2. 范围，eg：1-10
3. 频率，eg：/5
```

#### 普通用户创建计划任务
- 使用crontab命令
```shell
crontab -e 创建计划任务
```




## 系统启动和内核管理
### 硬件启动POST


### 启动加载器bootloader
- Linux的bootloader：GRUB
- CentOS7以后使用GRUB2.02 
    - 查看GRUB版本
    ```shell
    rpm -qi grub2
    ```
    
- GRUB启动阶段
    - stage 1： MBR前446字节 （grub程序的一部分 ）
    - stage 1.5: 在MBR后续的扇区中，让stage 1中的bootloader能识别stage2所在分区上的文件系统（解决文件系统的驱动问题 ）
        - 问题：stage 2识别文件系统，进入/boot/grub目录，需要内核处理，但是此时，内核还未被加载，如何识别stage2所在分区上的文件系统 
        - 修复一阶段和1.5阶段，在救援模式，使用grub-install /dev/sda
    - stage 2: 通常放置于一个基本磁盘分区

### grub legacy管理
- 配置文件：/boot/grub/grub.conf <---- /etc/grub.conf

-  grub.conf由anaconda程序生成

- grub.conf,中，系统内核来讲，内核中并没有文件系统驱动，文件系统驱动在/lib/modules/...内核版本/kernel/fs/...   ，但是要挂载根需要文件系统驱动，而文件系统驱动在根里，怎么办
    -  解决办法：initeramfs-....img (初始化的虚拟文件系统文件 ，该文件是一个打包压缩文件)
    - file initeramfs... 查看文件会发现这是一个gzip类型的文件 
    - mv initeramfs...img initerams...img.gz (添加。gz后缀)，然后使用gunzip解压
    - 再次使用file查看解压后文件，可以发现是cpio类型文件（cpio是一个打包文件，类似于tar ）
    -  cpio -tv <filename> 预览cpio包内的文件
    -  cpio -i 解包，可发现initernmfs本质上是一个小的linux，通过这个小的操作系统，来使内核挂载真正的根在硬盘的分区上 
    - 如果interam。。。文件被破坏如何修复
        - 进入救援模式
            - 方法1：切根，然后重新安装内核的包
            - 方法2: 使用mkinitrd /boot/initramfs-$(uname -r).img $(uname -r), 重新生产initramfs。。。文件，多使用几次sync，


-------------------------------------------------------------------------------------------------------------------------------

### 内核模块管理和编译
#### 内核模块命令
- lsmod命令
    - 显示由核心已经装载的内核模块
    - 显示的内容来自于：/proc/modules文件

- modinfo命令
    - 功能：管理内核模块
    - 配置文件: /etc/modprobe.conf, /etc/modprobe.d/*.conf 
    ```shell
    -n          # 只显示模块文件路径
    -p          # 显示模块参数
    -a          # 作者
    -d          # 描述
    ```

- modprobe命令
    - 功能：加载或卸载内核模块
    ```shell
    
    ```

#### 内核编译与管理




### systemd
#### systemd特性
- systemd：从CentOS7版本之后开始用systemd实现init进程，系统启动和服务器守护进程管理器，负责在系统启动运行时，激活系统资源，服务器进程和其他进程


- systemd新特性
    - 系统引导时，实现服务并行启动（并不是完全并行，有依赖关系的会有前后顺序）
    - 按需启动守护进程
    - 自动化的服务依赖关系管理
    - 同时采用socket式与D-Bus总线式激活服务
    - 向后兼容sysv，init脚本
    - 使用systemctl命令管理，systemctl命令固定不变，不可扩展，非由systemd启动的服务，systemd无法与之通信和控制
    - 系统状态快照

#### systemd核心概念：unit
- 查看unit类型
```shell
systemctl -t help

#service unit,  文件扩展名为.service, 用于定义系统服务
# Target unit，文件扩展名为.target, 用于模拟实现运行级别
# Device unit，用于定义内核识别的设备
# Mode unit， 定义文件系统挂载点
# Socket unit， 定义进程间通信用的socket文件，也可在系统启动时，延迟驱动服务，实现按需分配
# Snapshot， 管理系统快照
# Swap 用于标识swap设备
# Automount unit：automessage，文件系统的自动挂载点
# Path unit ：.path,用于定义文件系统中的一个文件，或目录使用, 常用用于文件系统变化时，延迟激活服务，入伍微信，spool目录
```

- unit的配置文件
```shell
/usr/lib/systemd/system; # 每个服务最主要的启动脚本设置，类似于之前的/etc/init.d
/lib/systemd/system      # ubuntu的对应目录
/run/systemd/system； # 系统执行过程中所产生的服务脚本，比上面目录优先运行（内存中）
/etc/systemd/system；   # 管理员建立的执行脚本，比上面目录优先运行
```

#### systemctl管理系统服务service unit
- 命令：`systemctl COMAMND name.service`
```shell
# 启动，相当于service name start
systemctl start name.service

# 停止，相当于service name stop
systemctl stop name.service

# 重启，相当于service name restart
systemctl restart name.service 

# 查看状态，相当于service name status
systemctl status name.service

# 禁止自动和手动启动
systemctl mask name.service

# 取消禁止
systemctl unmask name.service

# 查看某服务当前激活与否的状态
systemctl in-active name.service

# 查看下会开机，是否自启
systemctl is-enabled name.service

# 查看所有已激活的服务
systemctl list-units --type|-t service

# 查看所有服务
systemctl list-units --type service --all|-a

# 设置某服务开机自启，相当于chkconfig name on
systemctl enable [--now] name.service

# 设置某服务开机禁止启动，相当于chkconfig name off
systemctl disable [--now] name.service

# 查看所有服务的开机自启状态
systemctl list-units-files --type service

# 重新加载systemctl的状态    
systemctl daemon-reload

# 列出失败的服务
systemctl --failed --type=service

# 查看服务的依赖关系
systemctl list-dependencies name.service

# 杀掉进程
systemctl kill unitname
```

#### service unit文件格式
```shell
/etc/systemd/system       # 系统管理员和用户使用
/usr/lib/systemd/system     # 发行版打包者使用
```

#### 实现Ubuntu开机启动
- 创建可执行文件：/etc/rc.local
- /etc/rc.local内的脚本程序，会实现开机直接运行

- 注意：实现rc.local能够开机运行的服务：/lib/systemd/system/rc.local.service


#### 运行级别
- target units: 相当于CentOS6之前的runlevel， unit配置文件：.target
```shell
ls /usr/lib/systemd/system/*.target
```

- 查看不同级别target的下会加载的服务
```shell
systemctl list-dependencies graphical.target
```

- 级别切换
```shell
systemctl isolate name.target
```

- 设置开机进入的默认target
```shell
systemctl set-default name.target
```

- 查看当前的默认target
```shell
systemctl get-default
```

- 切换至紧急救援模式
```shell
systemctl rescue
```

- 禁用ctrl+alt+delete（重启快捷键）
```shell
systemctl mask ctrl_alt_del.target

# 使其生效
init q      # 等价于systemctl deamon reload
```

### CentOS7之后版本的引导顺序
- 完整过程
```shell
1. UEFI或BIOS初始化，进行POST开机自检
2. 选择启动设备
3. 引导装载程序，CentOS7是grub2加载装载程序的配置文件：
/etc/grub.d
/etc/default/grub
/boot/grub2/grub.cfg
4. 加载initramfs驱动模块
5. 加载内核选项
6. 内核初始化，CentOS7使用systemd代替init
7. 执行initrd.target所有单元，包括挂载/etc/fatab
8. 从initramfs根文件系统切换到磁盘根目录
9. systemd执行默认target配置，配置文件/etc/etc/systemd/default.target
10. systemd执行sysinit.target初始化系统及basic.target准备操作系统
11. systemd启动multi-user.target下的本机与服务器程序
12. systemd执行multi-user.target下的/etc/rc.d/rc.local
13. systemd执行multi-user.target下的getty.target及登陆服务
14. systemd执行graphical需要的服务
```

- 通过systemd-analyze工具可以了解启动详情
```shell
systemd-analyze plot > boot.html 

# 或者
systemd-analyze blame
```

- 通过设置内核参数进入救援模式
```shell
启动时，到启动菜单，按e键，找到linux开头的行，后添加systemd.unit=rescue.target
```

#### 破解CentOS7，8的root密码
```shell
# 方法1
在grub界面，按e进入编辑模式
光标移动linux开始的行，添加内核参数rd.break
按ctrl-x启动
mount -o remount , rw /sysroot  # 因为当前的操作系统是只读，无法修改文件，因此需要重新挂载
chroot /sysroot
passwd root

# 如果selinux启用，需添加下面的命令
touch /.autorelabel

# 方法2
在linux开始的行，改为rw init=/sysroot/bin/sh
按ctrl-x启动
chroot  /sysroot
passwd root
```

#### 实现grub2安全
```shell
添加grub密码
grub2-setpassword

# 添加密码后会在/boot/grub2目录下，添加user.cfg文件，里面是密码
echo "" > user.cfg      # 可以清空密码
```

#### 修复grub2
- 主要配置文件：/boot/grub2/grub.cfg
- 修复配置文件：grub2-mkconfig > /boot/grub2/grub.cfg

- 修复grub
```shell
grub2-install /dev/sda  # BIOS环境
grub2-install           # UEFI环境
```

- 设置默认启动内核
```shell
# 以下命令是修改 /boot/grub2/grubenv实现
# 查看内核信息
ls /boot/loader/entries/
# 可以将需要设置的默认内核信息，添加替换至/boot/grub2/grubenv的saved_entry=后面，将它后面的替换掉 
grub2-set-default 0
# 或者
vim /etc/default/grub
GRUB_DEFAULT=0
```

- 实战案例1
```shell
# 破坏前446字节的引导信息
dd if=/dev/zero of=/dev/sda bs=1 count=446 
# 光盘进入救援模式
grub2-install --root-directory=/mnt/sysimage /dev/sda
```

- 实战案例2
```shell
# 删除/boot/grub2/*所有内容，进行修复
光盘进入救援模式
chroot /mnt/sysimage
grub2-install /dev/sda
grub2-mkconfig -o /boot/grub2/grub.cfg
```

- 实战案例3
```shell
# 清空/boot下文件，进行修复
光盘进入救援模式
# 特别说明，CentOS8必须先grub，再安装kernel，否则安装kernel-core时会提示grub出错
chroot /mnt/sysimage
mount /dev/sr0 /mnt
grub2-install /dev/sda

2. 安装kernel
rpm -ivh <安装包路径> --force

3. 修复grub.cfg
grub2-mkconfig -o /boot/grub2/grub.cfg

4. 退出重启
exit
exit
```


### Bind
```shell
rndc reload = systemctl reload named， # 这两条命令等价
```
- 重启服务

- 在`/etc/named.conf`配置文件中
```shell
allow-query  { localhost;10.0.0.0/24; };  # 这个位置可以写网段,表示这个网段内的所有设备都可以通过该DNS服务器实现域名查询
allow-query { any; };    # any是DNS配置文件的关键字，这里表示任何人都可以使用这台DNS服务器进行域名查询，该服务器是DNS公共服务器 

# 更简单的方法
将listen on port 53  { localhost; };和allow-query，这两个字段注释掉，结果和localhost； any; 是一样的
```

### DNS服务器的类型
- 主DNS服务器
    - 管理和维护所负责解析的域内解析库的服务器

#### 主DNS服务器实现
- 要创建维护一个magedu.org的域，就要创建一个解析magedu.org的域的数据库
    - 该数据库单独存放 ，这个数据库文件里面记录所有magedu.org为后缀的域以及IP的对应关系
    - 一个区域数据库对应一个域 
    - 该区域数据库由一行一行的区域记录组合而成（RR，资源记录）

- 区域解析库：由众多RR组成
    - 各种资源记录：RR（Resource Record）
    - 记录类型：A，AAAA，PTR， SOA， NS， CNAME， MX
    - SOA：Start Of Authority，起始授权记录：一个区域解析库有且仅能有一个SOA记录，必须位于解析库的第一条记录
    - A：internet Address，作用：FQDN -> IP
    - AAAA: FQDN -> IPv6
    - PTR: IP -> FQDN
    - NS: Name Service,专用于标明当前区域的DNS服务，还是很轻的
    - CNAME：Canonical Name，别名记录
    - MX：邮件交换器
    - TXT：对域名进行标识和说明的一种方式，

- 资源记录定义的格式
```shell
name [TTL] IN rr_type value
```
- 注意：
    - TTL可从全局继承
    - 使用@符号可用于引用当前区域的名字

- SOA
```shell
$TTL 86400
# 一个小时做一次拉操作，如果失败了10分钟后重试, 当重服务器和主服务器实时无法同步，一天之后，从主将无法对外提供服务, 最后一个参数，错误结果的缓存时间
@ IN SOA ns1.magedu.org admin.magedu.org (123, 1h, 10m 1D, 12h)
ns1.magedu.org IN A 10.0.0.8
``` 

- 存放DNS数据库的路径`/var/named`
    - 创建该数据库，并在里面添加内容
    ```shell
    cp -p named.localhost magedu.org.zonn  

    # 编辑
    ```

- 通过文件，加载到`/var/named`让百度知道 


### openssl命令

- 查看openssl的版本
```shell
openssl version
```

#### openssl对称加密
- 工具：`openssl enc, gpg`
- 算法：`3des, aes, blowfish, twofish`
- enc命令帮助：`man enc`
```shell
# 加密
openssl enc -e -des3 -a -salt -in testfile -out testfile.cipher
# -e 加密
# -des3 对称加密算法
# -a 使用base64输出可见字符
# -salt 加盐（随机生成，默认）
# - in 后面加要处理的文件
# -out 将加密后的信息输出到指定文件

# 解密
openssl enc -d -des3 -a -salt -in testfile.cipher -out testfile 
```

#### openssl命令单向加密
- 工具：openssl dgst
- 算法：md5sum, sha1sum, sha224sum, sha256sum
```shell
openssl dgst -md5 /PATH/FILENAME
md5sum /PATH/FILE
```

#### openssl生成用户密码
```shell
openssl passwd -l -salt SALT(最多8位)
openssl passwd -6 -salt SALT value
```

#### openssl 生成随机数
- 随机数生成器：伪随机数字，块终中断生成随机数
- 调用：/dev/random； /dev/urandom
```shell
openssl rand -base64 8
# 8 表示8个字节  

openssl rand -base64 10 ｜ head -c10
```

#### openssl命令实现PKI
- 公钥加密
    - 算法：RSA, ELGama
    - 工具：gpg, openssl rsautl
- 生成私钥
```shell
openssl genrsa -out /PATH/TO/FILENAME [-des3 ] NUM_BITS # (默认2048位)

#示例
# 生成对称密钥加密的私钥
(umask 077; openssl gensra -out test.key -des3 2048) # genrsa就是用rsa算法生成的私钥

# 将加密对称密钥key解密
openssl rsa -in test.key -out test2.key

# 从私钥中提起出公钥
openssl rsa -in PRIVATEKEYFILE -pubout -out PUBLICKEYFILE
```

### 建立私有CA实现证书申请颁发
- 证书申请及签署步骤
    - 生成申请请求
    - RA核验
    - CA签署
    - 获取证书

- openssl的配置文件
```shell
/etc/pki/tls/openssl.cnf
```

- 三种策略
    - match匹配、optional可选、supplied提供
    - match：要求申请填写的信息跟CA设置信息必须一致
    - optional：可有可无，跟CA设置信息可以不一致
    - supplied：必须填写这项申请信息

```shell
cat /etc/pki/tls/openssl.cnf

...
# 一个设备可以创建多个CA，下面的是默认CA
[ ca ]
default_ca = CA_default         # the default ca section

[ ca_default ]
dir = /etc/pki/CA       # 所有创建CA相关文件都放在这里 ，如果该目录不存在，则需要手工创建
certs = $dir/certs       # 存放发布的证书
crl_dir = $dir/crl      # 证书的吊销列表
database = $dir/index.txt       # 需要手工创建 

new_certs_dir = $dir/newcerts       # 默认颁发的新证书放在这里
certificate = $dir/cacert.pem       # 存放CA的证书（RootCA，自签名）
serial = $dir/serial                # 证书的当前序号，下一个颁发证书的编号 
crlnumber = $dir/crlnumber          # 吊销的编号

crl = $dir/crl.pem                          # 吊销列表
private_key = $dir/private/cakey.pem    # 自己的私钥
RANDFILE = $dir/private/.rand

x509_extensions = usr_cert

name_opt = ca_default
cert_opt = ca_default

default_days = 365              # 默认有效期
default_crl_days = 30
default_md = sha256
preserve = no

policy = policy_match    # 证书颁发策略

[ policy_match ]        # match意味着，CA信息和客户端向CA申请的信息必须一致
countryName = match
stateOrProvinceName = match
OrganizationName = match
OrganizationalUnitName = optional
commonName = supplied           # 通常是网站域名
emailaddress = optional

[ policy_match ]        
countryName = optional
stateOrProvinceName = optional
OrganizationName = optional
OrganizationalUnitName = optional
commonName = supplied           # 通常是网站域名
emailaddress = optional
```

#### 创建私有CA
- 创建CA所需的文件
```shell
# 生成证书索引数据库文件
touch /etc/pki/CA/index.txt

# 指定第一个颁发证书的系列号
echo 01 > /etc/pki/CA/serial
```

- 生成CA私钥
```shell
cd /etc/pki/CA/

(umask 066; openssl genrsa -out private/cakey.pem 2048)  # 文件名要和配置文件对上
```

- 生成CA自签名证书
```shell
openssl req -new -x509 -key /etc/pki/CA/private/cakey.pem -days 3650 -out /etc/pki/CA/cacert.pem

# -new： 生成新证书签署请求
# -x509：专用于CA生成自签证书
# -key：生成请求时用到的私钥文件
# -days：证书有效期
# -out：证书的保存路径
```
- 国家代码：https://country-code.cl/（中国CN）

- 以文本形式查看证书内容
```shell
openssl x509 -in /etc/pki/CA/cacert.pam -noout -text
```



### HTTP相关技术与术语
#### MIME
- 多用途因特网邮件扩展
- 文件：`/etc/mime.types`,来自于mailcap包
- MIME格式：type/subtype


#### URI/URL
- URI：统一资源标识（Uniform Resource Identifier）分为URL和URN

- URN：统一资源命名（Uniform Resource Naming）
    - P2P中的磁力链接是URN的一种实现

- URL：统一资源定位符（Uniform Resource Locator）,用于描述某服务器某特定资源位置

- URN和URL的区别
    - URN定义某事物身份，URL提供查找该事物的方法
    - URN仅用于命名，而不指定地址

- 详细信息看Web协议详解与抓包实战


#### 网站访问量
- 网站访问量统计的重要指标
    - IP（独立IP）：指独立IP数，一天内来自相同客户机IP地址只计算一次，记录远程客户机IP地址的计算机访问网站的次数。是衡量网站的重要指标
    - PV（访问量）：即Page View，页面浏览量或点击量，用户每次刷新即计算一次，PV反应流量某网站的页面数，PV与来访者数量成正比，PV不会页面的来访者数量，而是网站被访问的页面数量
    - UV（独立访客）：UNique Visitor，访问网站的一台电脑为一个访客，一天内相同的客户端只被计算一次，可以理解为访问某网站的电脑数量，网站判断来访电脑的身份是通过cookie来实现的。如果更换IP，但是不清除cookie，再次访问网站，则UV不变。


#### HTTP工作机制
- http请求：http request
- http响应：http reponse

- 资源类型
    - 静态资源
    - 动态资源

#### 一次完整的HTTP请求处理过程
- 建立连接：接收或拒绝连接请求
- 接收请求：接收客户端请求报文中对某资源的一次请求的过程
    - Web访问响应模型
        - 单进程I/O模型：启动一个进程处理用户请求，而且一次只处理一个，多个请求被串行响应
        - 多进程I/O模型：并行启动多个进程，每个进程响应一个连接请求
        - 复用I/O结构：启用一个进程，同时响应N个连接请求
        - 复用的多进程I/O模型：启动M个进程，每个进程响应N个连接，同时接收M*N个请求

- 处理请求
    - 常用请求Method：POST，GET，HEAD，PUT，DELETE
- 访问资源
- 构建响应报文
- 发送响应报文
- 记录日志

#### HTTP协议报文头部结构
- 请求报文由三个部分组成：即开始行，首部行和实体主体
    - 在请求报文中，开始行就是请求行
    - 查看请求报文
    ```shell
    curl -v www.baidu.com
    ```

- 响应报文






