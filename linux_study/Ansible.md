# Ansible

## Ansible工作原理


## Ansible安装
在Rocky中安装ansible
```shell
# 需要先安装epel源
yum install -y epel-release

# yum install -y ansible

# Rocky9
rpm -q ansible
```

在Ubuntu中用pip安装
```shell
pip3.10 install -i https:/pypi.tuna.tsinghua.edu.cn/simple-ansible
```

在Ubuntu中安装ansible
```shell
apt update; apt install -y ansible
```

在Ubuntu中安装ansible-core
```shell
apt update; apt install ansible-core
```

ansible和ansible-core
- ansible-core包中仅包含核心功能和核心模块，ansible包中除了核心功能之外还包含大量外围功能模块
- 在当前学习环境中（Ubuntu2204），ansible和ansible-core不能同时共存，都不提供配置文件，且ansible-core的版本更新
- 我们用ansible-core来学习

```shell
# 查看版本
ansible --version
```

## Ansible配置文件
```shell
# 创建目录
mkdir -pv /etc/ansible/roles

# 创建主机清单配置文件
touch /etc/ansible/hosts

# 生成配置文件
ansible-config init -t all -disabled > /etc/ansible/ansible.cfg
```

整个配置文件的目录结构如下
```shell
[root@rocky ~]# tree /etc/ansible/
 /etc/ansible/
 ├── ansible.cfg
 ├── hosts
 └── roles
 1 directory, 2 files
```
### 主配置文件

Ansible的主配置文件可以有多个，分别存放于不同目录，其优先级如下
```shell
ANSIBLE_CONFIG   # 环境变量，此变量中指向的文件必须存在才生效，指向的文件要以.cfg结尾

# 示例：
touch /tmp/test.cfg
export ANSIBLE_CONFIG=/tmp/test.cfg

./ansible.cfg    # 当前目录下的ansible.cfg，一般一个项目对应一个专用配置文件，推荐使用

~/.ansible.cfg   # 当前用户家目录下的，ansible.cfg

/etc/ansible/ansible.cfg   # ansible默认配置文件，主配置文件
```
### 主机清单配置文件

注意
- 生产建议在每个项目目录下创建项目独立的hosts文件
- 通过项目目录下的ansible.cfg文件中的inventory=./hosts实现

总结
- 生产最佳实践是每个项目目录都对应一个专用的配置文件`ansible.cfg`和主机清单配置文件`hosts`

hosts文件写法
```shell
# 写明主机名或IP
10.0.0.108

node1.linux-magedu.com

# 区间写法
198.168.10.[101:108]
198.168.[21:31].[68:70]

node[1:10].m5[0:9]-magedu.com

# 分组定义
[group1]
10.0.0.10[2:8]

[group2]
192.168.16[1:5].10
group2.m5[2:4]-magedu.com

# 继承写法group3继承自group1和group2
[group3:childen]
group1
group2

# 多重继承写法，group4继承自group3，group3继承自group1和group2

# 分组中定义别名
[group1]
node1 ansible-ssh-host=10.0.0.101
node2 ansible-ssh-host=10.0.0.102

[group1:vars]
ansible_ssh_password=123456
```

常见可定义配置项
```shell
ansible_ssh_host=IP|hostname
ansible_ssh_port=PORT
ansible_ssh_user=UNAME
ansible_ssh_pass=PWD            
ansible_sudo_pass=PWD
ansible_sudo_exe=/PATH/CMD                    # 显示指定SUDO密码
ansible_connection=local|ssh|paramkio|docker  # 与主机连接类型
```

## 常用Ansible工具
```shell
/usr/bin/ansible-doc      # 帮助手册，查看帮助文档
/usr/bin/ansible-pull     # playbook获取工具
/usr/bin/ansible-vault    # 文档加密工具
/usr/bin/ansible-galaxy   # 线上role管理工具
/usr/bin/ansible-playbook # playbook管理工具
```
### Ansible-doc命令用法

ansible-doc工具用来查看ansible文档

格式
```shell
ansible-doc [options] [module...]

# 常用选项
-h|--help           # 显示帮助
-l|--list           # 显示所有可用模块
-t|--type           # 指定模块类型
-v|--verbose        # 显示详细信息，最多可以-vvvvv（5v）
```

### Ansible-console命令用法
略

### Ansible-vault
此工具可以用于加密解密yml文件
```shell
ansible-vault encrypt hello.yaml       # 加密
ansible-vault decrypt hello.yaml       # 解密
ansible-vault view hello.yaml          # 查看
ansible-vault edit hello.yaml          # 编辑加密文件
ansible-vault rekey hello.yaml         # 修改口令
ansible-vault create new.yaml          # 创建新文件
```

### ansible-console(交互命令)
此工具可交互执行命令，支持tab，ansible2.0+新增
提示符格式
```shell
执行用户@当前操作的主机组(当前组的主机数量)[f:并发数]$
```
常用子命令：
- 设置并发数：forks n 例如：forks 10
- 切换组：cd 主机组 例如：cd web
- 列出当前组主机列表：list
- 列出所有的内置命令：?或help

```shell

```


## Ansible命令用法

ansible工具一般用来执行单条命令，使用频率高

格式
```shell
ansible <host-pattern> [-m module_name] [-a args]

# 常用选项
--list-hosts       # 列出远程主机，可以写成 --list
-m module          # 指定模块，默认模块为command，默认模块式，可省略不写
-a|--args          # 指定模块选项
-e|--extra-vars    # 指定执行选项（变量）
-C|--check         # 检测语句是否正确，并不立即执行
-k|--ask-pass      # 提示输入ssh密码，默认用sshkey验证
-u|--user=UNAME    # 执行远程执行的用户，默认root
--become-usr=USERNAME  # 指定sudo的runas用户，默认为root
-K|--ask-become-pass   # 提示输入sudo时的口令
-f|--forks N           # 指定并发同时执行ansible任务的主机数
-i|--inventory /PATH/FILE   # 指定主机清单文件
-v|vv|...(5)v               # 显示详细执行过程
```

### ansible主配置文件
```shell
[defaults]
#
```

### Ansible命令基础用法

查看主机
```shell
ansible all --list-hosts
ansible --list all

ansible --list Ubuntu
```

远程执行命令，要下载sshpass
```shell
apt install -y sshpass
```

在ansible.cfg中将选项改掉，使其自动接收公钥
```shell
[ssh_connection]
host_ssh_checking=False
```

将hosts文件中设置全局ssh密码
```shell
[group1:vars]
ansible_ssh_password=123456
```

删除~/.ansible目录
```shell
rm -rf ~/.ansible
```

#### host-pattern规则
```shell
# 所有主机
ansible all --list

# 指定组
ansible group3 --list

# 直接指定主机
ansible "10.0.0.108 10.0.0.107" --list

# 通配符
## 通配符表示所有主机
ansible "*" --list

# 逻辑或
ansible "test1:test2" --list
ansible "test1 test2" --list  # 默认逻辑或

# 逻辑与
ansible "test1:&test2" --list

# 逻辑非
ansible "test1:!test2" --list
```

## Ansible常用模块

帮助文档
```shell
https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html  #2.9

https://docs.ansible.com/ansible/lastest/module_plugin_guide/index.html  #最新版本
```

### command模块

此模块为ansible默认模块，可以省略-m选项，该模块用来在远程主机执行shell命令[其中，管道，重定向，通配符不支持，不支持多条命令]

此模块不具备幂等性
```shell
#常用选项
chdir=dir     # 执行命令前，先切换到目录dir
creates=file  # 当file不存在时才会执行
removes=file  # 当file存在时才会执行
```
#### playbook写法
```yaml
- hosts: 
  ...
  tasks:
  - name: test command
    command: ls
    # 常用选项写在args中
    args:
      chdir: /etc/
```

范例
```shell
# 当/root/test/abc不存在时执行
ansible group1 -a "chdir=/root/test creates=/root/test/abc touch abc"
```

### shell模块

shell模块比command模块强大，对于在command模块中不支持的功能，此处均可支持。此模块也不具有幂等性

在调用shell模块执行命令时，复杂的命令也有可能执行失败，类似于包含多重管道，正则表达式这些，这种情况下，我们需要写成shell脚本，用copy模块直接推送到远程执行

```shell
# 查看帮助
ansible-doc -s shell

# 常用选项
chdir=dir       # 执行命令前，先切换至目录dir
creates=file    # 当file不存在时才会执行
removes=file    # 当file存在时才会执行
```

#### playbook写法示例
```yaml
- hosts: test
  gather_facts: no
  remote_user: root
  tasks:
  - name: build dir
    shell: mkdir test
    args:
      chdir: /
      # 可以把creates和removes当做判断，手动实现幂等性
      creates: /test   
  - name: write file
    shell: echo hello > 1.txt
    args:
      chdir: /test
      creates: /test/1.txt
```
#### 将shell改为默认模块
```shell
# 修改配置文件ansible.cfg
module_name = command
# 修改为
module_name = shell
```

还原Ansible工作原理
```shell
# 开始执行
ansible 10.0.0.108 -m shell -a "sleep 50; echo 123"

# ansible主机
tree .ansible
.ansible
 ├── cp
 │   └── 01622bc8ee
 └── tmp
    └── ansible-local-2904o3re9rpa

# 远程主机
tree .ansible/
.ansible/
 └── tmp
    └── ansible-tmp-1686975946.0248253-2907-249866542891908
        └── AnsiballZ_command.py
2 directories, 1 file

# 当命令执行完成后，临时脚本会被删除

# 可以开启配置文件中的配置项，保留远程主机上的脚本，也可以观察
keep_remote_files=True
```
### script模块

script模块可以在远程主机上运行ansible机器上的脚本（而且脚本文件可以没有执行权限），这里的脚本并不仅仅只是shell脚本，只要远程主机上能执行的，都可以，包括但不限于php,sh,py等

```shell
ansible-doc -s script

# 常用选项
cmd=script     # 写本地脚本路径
chdir=dir      # 执行命令前，先切换至目录dir
creates=file   # 当file不存在时才会执行
removes=file   # 当file存在时才会执行
```

范例
```shell
# 查看本机脚本
cat test.sh
hostname -I > /tem/ansible-script.log
hostname -I
```

#### playbook示例
```yaml
- hosts: ubuntu2204
  gather_facts: no
  remote_user: root
  tasks:
  - name: switch ali source
    script: /root/mytool/switchsource -a
```

### copy模块 

copy模块将ansible主机上的文件复制到远程主机，此模块具有`幂等性`

```shell
# 查看帮助
ansible-doc -s copy

# 常用选项
src=/path/file         # ansible主机文件路径
src=/path/             # 如果/作为结尾，则会copy文件夹内的所有文件，不包含目录本身
dest=/path/file        # 远程主机文件路径
                       # 必须是远程绝对路径
                       # 如果源是文件夹，则它也必须是文件夹
directory_mode=        # 是否决定递归复制
content="context"      # 指定内容直接生成目标文件
owner=UNAME            # 新文件属主
group=GNAME            # 新文件权限
backup=yes|no          # 是否备份，默认为no
remote_src=yes|no      # no是默认值，表示src文件在ansible主机
                       # yes表示src文件在远程主机
```

范例
```shell
# 将ansible主机上的文件copy到远程主机
ansible 10.0.0.206 -m copy -a "src=/root/test.txt dest=/tmp/test.txt.bak"

# 源和目标都在远程主机
ansible group1 -m copy -a "src /root/abc.txt dest=/root/from-ansible.txt remote_src=yes"

# 拷贝目录
## 将ansible主机的/etc/ansible目录复制到远程主机，保存到/tmp/下
ansible 10.0.0.206 -m copy -a 'src=/etc/ansible dest=/tmp/'

## 复制目录下所有文件，将ansible主机的/etc/ansible/目录下所有文件复制到远程主机，保存到/tmp/ansible/中
ansible group1 -m copy -a 'src=/etc/ansible/ dest=/tmp/ansible-2'
```

#### playbook示例
```yaml
- hosts: test
  gather_facts: no
  tasks:
    - name: Create a configuration file on the remote host
      copy:
        dest: /etc/example.conf
        content: |
          [main]
          name = example
          value = 42
# 注意：content：|,"|"这个符号是表示多行文本确保保留换行符和缩进
# 注意2：缩进，yaml对缩进非常敏感，所有内容要比content缩进2个空格
```
### get_url模块

该模块可以将网络上的资源下载到指定主机，支持http,https,ftp协议

```shell
# 查看帮助
ansible-doc -s get_url

# 常用选项
url="http://www.a.com/b.txt"       # 下载文件URL
dest=/tmp/c.txt                    # 保存文件路径（绝对路径）
owner=UNAME                        # 指定属主
group=GNAME                        # 指定属组
mode=777                           # 指定权限
force=yes|no                       # 默认yes，如果目标文件存在，则覆盖，no表示只有目标不存在才下载
checksum="algorithm:str"           # 指定目标文件摘要值，下载完成后算出文件摘要再对比，确认文件是否完整

url_username=UNAME                 # http 认证用户名
url_password=PWD                   # http 认证密码
validate_certs=yes|no              # no表示不验证SSL证书合法性
timeout=10                         # URL请求的超时时间，默认10s
```

范例
```shell
ansible 10.0.0.108 -m get_url -a "url=http://www.jose-404.com.aini.jpg dest=/tmp/a.jpg"
```

### fetch模块

从远程主机提取文件至ansible的主控端，copy相反，不支持目录

```shell
# 查看帮助
ansible-doc -s fetch

# 常用选项
src=/path/file               # 远程主机上的文件路径
fail_on_missing=yes|no       # 默认yes，无法获取远程主机文件时，显示失败
dest=/path                   # ansible主机上的保存路径，不存在会自动创建
```

范例
```shell
ansible "10.0.0.206 10.0.0.150" -m fetch -a "src=/etc/issue 
dest=./ansible-fetch"

[root@ubuntu ~]# tree ansible-fetch/
ansible-fetch/
├── 10.0.0.150
│   └── etc
│       └── issue
└── 10.0.0.206
    └── etc
        └── issue
```

### file模块

file模块主要提供文件管理功能，比如创建文件和目录，修改文件和目录，设置文件权限和属性，设置链接等

```shell
# 查看帮助
ansible-doc -s file

# 常用选项
path=/path/file                  # 目标文件路径
owner=USER                       # 属主
group=GROUP                      # 属组
mode=777                         # 权限
state=file|touch|directory|link|hard|absent # 具体操作，如果是link，源用src指定
recurse=yes|no    # yes表示递归操作，仅在state=directory时生效,创建目录的时候默认递归
```

范例
```shell
# 递归创建目录
ansible 10.0.0.107 -m file -a "path=/root/ansible/test state=directory"

# 递归设置属性
ansible 10.0.0.107 -m file -a "path=/root/ansible/dir2/dir3 state=directory owner=tom group=mage recure=yes"

# 创建文件
ansible 10.0.0.107 -m file -a "path=/root/ansible/test/test.txt state=touch owner=mystical group=root mode 777"

# 获取文件信息
ansible 10.0.0.107 -m file -a "path=/root/ansible/test/test.sh state=file"

# 创建链接
## 链接文件可以用dest|name来指定
ansible 10.0.0.107 -m file -a "src=/root/ansible/test/test.sh dest=/root/ansible/test/test.link state=link owner=root group=root"

## 示例2
ansible ubuntu2204 -m file -a "src=/etc/fstab dest=/root/fstab.link state=link owner=root group=root"

# 删除文件
ansible 10.0.0.107 -m file -a "path=/ansible/test/test.link state=absent"
```

### stat/win_stat模块

stat用来获取目标文件状态，对于windows主机，要使用win_stat模块

```shell
# 查看帮助
ansible-doc -s stat

# 常用选项
path=/path/file           # 指定目标文件路径
follow=true/false         # 是否跟随链接，默认false，不跟随
```

范例
```shell
ansible 10.0.0.107 -m stat -a "path=/root/ansible/test/test.sh"
```

### unarchive模块

unarchive模块主要用来解压缩或解包，将ansible主机或者其他主机上的压缩包复制到指定主机，再解压到某个目录

在使用此模块时，要保证远程主机能解压对应的压缩包

```shell
# 查看帮助
ansible-doc -s unarchive

# 常用选项
src=/path/file   # 包文件路径，可以是ansible主机上的包文件，也可以是远程主机上的文件
dest=/path/dir   # 目标路径
remote_src=yes|no  # yes表示包文件在远程主机或第三方主机上，no表示包文件在ansible主机上，默认是no
copy=yes|no        # 已废弃，和remote_src一样
creates=/path/file # 此文件不存在才执行
mode=777           # 设置目标权限
owner=USER         # 设置目标属主
group=GROUP        # 设置目标属组 
```

范例
```shell
# 压缩并打包文件
tar acvf dira.tar.gz dira/

# 将ansible主机上的压缩包解压至远程主机，远程目录必须存在
ansible 10.0.0.107 -m unarchive -a "src=/root/txt.tar.gz dest=/root/ansible/test/ owner=mystical"

# 将第三方包解压至指定主机
ansible 10.0.0.107 -m unarchive -a "src=http://www.jose
404.com/web-dir.tar dest=/tmp remote_src=yes mode=777"
```
#### playbook示例
```yaml
# 可用于安装部署服务时，下载自动解压使用
- hosts: ubuntu2204
  gather_facts: no
  remote_user: root
  tasks:
  - name: test unarchive
    unarchive: 
      src: https://www.mysticalrecluse.com/script/tools/apache-tomcat-9.0.89.tar.gz
      remote_src: yes
      dest: /root/
```

### archive模块

archive模块在远程主机上执行压缩打包命令，此模块的源和目标在远程主机上
```shell
# 需要先安装此模块
pip install -Ivvv "resolvelib >= 0.5.3, < 0.6.0"
# 这里要将ansible.cfg文件中的galaxy的下载源路径改为old-$PATH
ansible-galaxy collection install community.general  --no-cache

# 查看
ansible-doc -s archive

# 常用选项
path=/path/dir         # 源目录或文件路径
dest=/path/file        # 目标的文件路径
remove=false|true      # 是否删除源文件，默认false
mode=777 
owner=USER
gruop=GROUP
format=bz2|gz|tar|xz|zip   # 指定压缩算法，默认gz
```

范例
```shell
# 有一台主机上没有要打包的目录
```

### hostname模块

此模块主要用于修改远程主机的主机名，修改后永久生效

```shell
ansible 10.0.0.107 -m hostname -a "name=test-name"
```

### cron模块

cron模块用于管理远程主机上的crontab定时任务

```shell
# 查看帮助
ansible-doc -s cron

# 常用选项
name=str               # 任务名称
job=/path/cmd args     # 具体任务命令
disabled=yes|no        # 是否禁用，默认false
state=absent|present   # absent 删除，默认present
env=yes|no             # yes设置环境变量，no设置定时任务，默认no
special_time=annually|daily|hourly|montyly|reboot|weekly|yearly # 指定特殊事件
```

示例
```shell
ansible ubuntu2204 -m cron -a "minute=*/5 job='/usr/sbin/ntpdata ntp.aliyun.com &> /dev/null' name=synctime"
```

### yum模块和apt模块

yum模块和apt模块用于在远程主机上管理软件包，yum模块适用于redhat系列，apt适用于debian系列

```shell
# 查看帮助
ansible-doc -s yum

# 常用选项
name=packagename       # 指定包名 name1, name2
# absent|remove 删除，installed|present安装，lastest升级到最新版
state=absent | installed | lastest | presnet |removed
# 此选项与name选项互斥，写具体包名相当于执行yum list --
list=packagename|installed|updates|available|repos

showduplicates packagename
download_dir=/path       # 指定下载目录
download_only=yes|no     # 只下载不安装，默认no
```

范例
```shell
# 列出指定软件包，相当于yum list --showduplicates nginx
ansible Rocky -m yum -a "list=nginx"

# 列出所有的repo
ansible Rocky -m yum -a "list=repos"

# 安装和卸载
## 卸载
ansible Rocky -m yum -a 'name=sos state=removed'
## 安装
ansible Rocky -m yum -a 'name=httpd state=present'

## 从指定源安装
ansible Rocky -m yum -a 'name=sos enablerepo=baseos'
```

apt模块
```shell
# 查看帮助
ansible-doc -s apt

# 常用选项
name=packagename    # 指定包名，可用通配符，默认安装
autoclean=yes|no    # 清除本地安装包，只删除已卸载软件的deb包
deb=/path/file.deb  # 指定deb包，可以是本地，也可以是网络
autoremove=yes|no   # 卸载依赖包，默认no
# absent 卸载，build-dep 安装依赖包，lastest 安装或升级到最新版， present 安装，fixed 修复
state=absent|build-dep|lastest|present|fixed
update_cache=yes|no  # 更新索引

# 安装和卸载
## 安装指定版本
ansible Ubuntu -m apt -a "name=nginx=1.18.0-6ubuntu14.3 state=present"

## 卸载
ansible Ubuntu -m apt -a 'name=nginx* state=absent'
```

### yum_repository模块

此模块用来对远程主机上的yum仓库配置进行管理

```shell
# 查看帮助
ansible-doc -s yum_repository

# 常用选项
name=repoid              # repoid
description=desc         # 描述信息
baseurl=url              # 仓库地址
enabled=yes|no           # 是否启用
gpgcheck=yes|no          # 是否启用gpgcheck,没有默认值，默认跟随/etc/yum.conf中的全局配置
gpgkey=/path/key         # gpgkey路径
state=absent|present     # absent 删除，present安装，默认present
timeout=30               # 超时时长，默认30s
```

范例：创建和删除
```shell
# 添加yum源
ansible 10.0.0.107 -m yum_repository -a 'name=nginx description=nginx-desc baseurl="http://nginx.org/packages/centos/$releasever/$basearch/" gpgcheck=1 enabled=1 gpgkey=https://nginx.org/keys/nginx_signing.key'

# 删除
ansible 10.0.0.107 -m yum_repository -a "name=nginx state=absent"
```

### service模块

service模块主要用于对远程主机的服务进行管理

```shell
# 查看帮助
ansible-doc -s service

# 常用选项
name=servicename                            # 服务名
enabled=yes|no                              # 是否是开机启动
state=reloaded|restarted|started|stopped    # 具体操作
args=val                                    # 参数

# 启动服务
ansible 10.0.0.107 -m service -a "name=nginx state=started"

# 重载
ansible 10.0.0.107 -m service -a "name=nginx state=reloaded"

# 加开机启动
ansible 10.0.0.107 -m service -a 'name=nginx enabled=yes'
```

### user模块

此模块用于对远程主机进行用户管理

```shell
# 查看帮助 
ansible-doc -s user

# 常用选项
name=USERNAME           # 指定用户名
comment=str             # 用户描述信息
create_home=yes|no      # 是否创建家目录，默认yes
group=GROUPNAME         # 指定私有组
groups=group1,group2... # 指定附加组 
home=/path              # 指定家目录路径
shell=SHELL             # 指定shell
state=absent|present    # absent删除用户，present 创建用户，默认present
system=yes|no           # 是否创建系统账号，默认no
uid=UID                 # 手动指定UID
remove=yes|no           # 是否删除家目录，默认no
generate_ssh_key=yes|no # 是否创建私钥，默认no
ssh_key_bits=2048       # 指定私钥位数
ssh_key_file=/path/file # 指定文件位置，默认 .ssh/id_rsa
```

范例
```shell
 ansible 10.0.0.206 -m user -a 'name=user1 comment="ansible user" 
uid=2048 home=/user1/'
```

### group模块


### lineinfile模块

lineinfile模块主要用于修改远程主机上的文件

ansible提供了两个常用的文件修改模块，其中lineinfile主要对文件单行进行替换修改，replace模块主要进行多行替换和修改

如果使用ansible调用sed进行文件修改时，经常会遇到需要转义的情况，而且在对特殊符号进行时，有可能会失败

```shell
# 查看帮助
ansible-doc -s lineinfile

# 常用选项
path=/path/file            # 远程主机文件路径
regexp=                    # 正则，用来锚定要被修改的内容
insertafter=               # 正则，在指定内容后的新行中增加line里面的内容，与regex同时使用时，只有regex没匹配才生效
insertbefore=              # 正则，在指定内容前的新行中增加line里面的内容
line=str                   # 修改后的内容
state=absent|present       # absent 删除，present 不存在先创建
backup=yes|no              # 修改前先备份，默认no
create=yes|no              # 不存在先创建，默认no
backrefs=yes|no            # 是否支持引用，默认no不支持
mode=666                   # 设置权限
owner=USER
group=GROUP

# 使用regexp配合正则表达式来锚定要被修改的内容时，如果有多行被匹配，则只有最后一行会被替换，如果删除，则匹配到的行都会被删除
```

范例
```shell
# 在远程主机上查看
cat -n test.txt
1 aaaa
2 bbbb
3 tom-123
4 tom-456
5 tom-789
6 jerry-123
7 jerry-456

# 替换
ansible 10.0.0.107 -m lineinfile -a 'path=/root/test.txt regexp="^tom" line="TOM"'

# 追加一行
ansible 10.0.0.107 -m lineinfile -a 'path=/root/test.txt line="abcdefg"'

# 在指定行后添加一行
ansible 10.0.0.107 -m lineinfile -a 'path=/root/ansible/test/test.txt insertafter="^b+$" line="hello"'

# 删除文件中所有以tom开头的行，修改前先备份
ansible 10.0.0.107 -m lineinfile -a 'path=/root/test.txt regexp="^tom" backup=yes state=absent'

# 匹配引用
cat -n test2.txt
AAAAA
abc
ABCDEFG
BBBBB
abcdefg
ABC123

ansible 10.0.0.107 -m lineinfile -a 'path=/root/ansible/test/test2.txt regexp="^ABC(.*)$" backrefs=yes line="XYZ\1"'
```
### blockinfile模块
blockinfile 模块。这个模块允许你插入、替换或删除文本块，而不是单行文本。
```shell
# 查看帮助
ansible-doc -s blockinfile

# 常用选项
insertafter       # 在指定正则之后添加，如果EOF,表示在结尾添加
insertbefore      # 在指定正则之前添加
state             # absent删除
block:            # 添加的内容
```

#### playbook示例
```yaml
- hosts: ubuntu2204
  gather_facts: no
  remote_user: root
  tasks:
  - name: test blockinfile
    blockinfile:
      path: /root/a.txt
      insertafter: EOF
      block: |
        [end]
        i'm end test
        i don't care
```

### replace模块

该模块功能与lineinfile模块功能类似，也是基于正则匹配的模式来修改文件，但与lineinfile不同的是replace模块用于多行匹配和修改

```shell
# 查看帮助
ansible-doc -s replace

# 常用选项
path=/path/file       # 远程主机文件路径
regexp=               # 正则，用来锚定要被修改的内容
replace=STR           # 用来替换的内容
after=STR             # 从STR之后开始处理
before=STR            # 处理到STR之前
backup=yes|no         # 修改前是否备份，默认no
mode=666              # 设置权限
owner=USER            # 指定属主
group=GROUP           # 指定属组
```

范例
```shell
cat -n test2.txt
123
456
789
abcdefg
ABCDEFG
123root

# 替换所有3个数字的行
ansible 10.0.0.107 -m replace -a 'path=/root/test2.txt regexp="^([0-9]{3})$" replace="\1------\1" backup=yes'
```

### reboot模块

reboot模块主要用于对远程主机进行重启操作
```shell
# 查看帮助
ansible-doc -s reboot

# 常用选项
msg=str           # 广播重启提示信息，默认为空
test_command=str  # 重启后执行验证命令，默认whoami
reboot_timeout=600  # 超时时长，默认600s
pre_reboot_delay=0  # 执行重启前等待时长，如果小于60s，此字段会被置0，也就是无效
post_reboot_delay=0 # 重启后等待一个时长后再验证是否重启完成

# 实现最简单的重启
ansible 10.0.0.107 -m reboot
```

### mount模块

mount模块用于管理远程主机的挂载

```shell
# 查看帮助
ansible-doc -s mount

# 常用选项
src=/path/device    # 要挂载的设备路径，可以是网络地址
path=/path/point    # 挂载点
state=absent|mounted|present|unmounted|remounted
# absent    取消挂载，并删除永久挂载中的配置
# mounted   永久挂载，立即生效，挂载点不存在会自动创建
# present   永久挂载，写配置文件，但不会立即生效
# unmounted 临时取消挂载，但不改变配置
# remounted 重新挂载，但不会改变配置文件

fstab=/path/file    # 指定挂载配置文件路径，默认/etc/fstab
fstype=str          # 设备文件系统xfs|ext4|swap|iso9660
opt=str             # 挂载选项
```

范例
```shell
# 挂载光盘，永久挂载，并立即生效
ansible 10.0.0.107 -m mount -a 'src=/dev/sr0 path=/mnt/ state=mounted fstype=iso9660'

# 取消挂载，永久生效
absible 10.0.0.107 -m mount -a 'src=/dev/sr0 path=/mnt state=absent'
```

### sysctl 模块

sysctl模块用来修改远程主机上的内核参数
```shell
# 查看帮助
ansible-doc -s sysctl

# 常用选项
name=str                # 参数名称
val=str                 # 参数值
reload=yes|no           # 默认yes，调用/sbin/sysctl -p 生效
state=present|absent    # 是否保存到文件，默认present
sysctl_file=/path/file  # 指定保存文件路径，默认/etc/sysctl.conf
```

范例
```shell
# 修改内核参数，并写文件
ansible 10.0.0.107 -m sysctl -a 'name=net.ipv4.ip_forward value=1'
```
### setup模块
功能：setup模块来收集主机的系统信息，这些facts信息可以直接以变量的形式使用，但是如果主机较多，会影响执行速度，可以使用`gather_facts:no`来禁止Ansible收集facts信息
```shell
ansible all -m setup -a "filter=ansible_nodename"
```

### debug模块
debug模块主要用于调试时使用，通常的作用是将一个变量的值打印出来
```shell
# 常用参数：
var                # 直接打印一个指定的变量
msg                # 打印一段可以格式化的字符串

# 示例
ansible all -i hosts -m debug -a "var=role" -e "role=web"
```

#### playbook演示
```yaml
# 打印指定变量
- hosts: ubuntu2204
  gather_facts: no
  remote_user: root
  vars:
    role: web
  tasks:
  - name: test debug
    debug:
      var: role

---
# msg打印一段可以格式化的字符串
- hosts: ubuntu2204
  gather_facts: no
  remote_user: root
  vars:
    role: web
  tasks:
  - name: test debug
    debug:
      #var: role
      msg: role is {{ role }}
```

### set_fact模块
set_fact模块用于在Ansible中动态设置变量。这些变量(或“事实”)在任务执行期间可以被后续任务引用。通过`set_fact`，你可以在Ansible playbook中创建或更新变量，甚至构建复杂的数据结构。

#### 基本用法
```yaml
- name: Set a simple fact
  set_fact:
    my_var: "Hello, World"
```

#### 设置多个变量
```yaml
- name: Set multiple facts
  set_fact:
    var1: "Value 1"
    var2: "Value 2"
```

#### 动态生成变量
```yaml
# 可以基于其他变量或条件来动态设置变量
- name: Set a fact based on a condition
  set_fact:
    result: "{{ 'Success' if my_var == 'Hello' else 'Failure' }}"
```



### template模块
template模块使用jinjia2格式作为文件模版，可以进行文档内容变量的替换
它的每次使用都会被ansible标记为changed。文件以`.jin2`结果
```shell
# 常用参数
src         # 指定ansible控制端的文件路径
dest        # 指定ansible被控端的文件路径
owner       # 指定文件的属主
group       # 指定文件的属组
mode        # 指定文件的权限
backup      # backup创建了一个包含时间戳信息的备份文件，这样如果您以某种方式错误的破话了原始文件，就可以将其恢复原状。yes/no

# 示例
# 建立一个Template文件，名为hello_world.j2
Hello {{var}}!

# 执行命令，并且设置变量var的值为world
ansible all -i hosts -m template -a "src=hello_world.j2 dest=/tmp/hello.txt" -e "var=world"
```

### 其他模块

除了上述模块之外，ansible还提供了很多其他的模块，在我们需要使用时，可以再进行查询
```shell
ansible-doc -l | grep "模块关键字"

ansible-doc 模块名
```

## YAML
- 在单一文件第一行，用连续三个连字号"-"开始，还有选择性的连续三个点号(...)用来表示文件的结尾
- 此行开始正常写Playbook的内容，一般建议写明该Playbook的功能
- 使用#号注释代码
- 缩进必须统一，不能空格和tab混用
- 多个key/value可同行写也可换行写，同行使用`,`分隔
- v可以是个字符串也可是另一个列表
- 一个完整的代码块功能需最少元素需包括`name`和`task`
- 一个name只能包括一个task
- YAML文件扩展名通常为yaml或yml

### YAML的数据结构
#### List列表
列表由多个元素组成，每个元素放在不同行，且元素前均使用"-"打头，或者将所有元素用[]括起来放在同一行
```yaml
# 不同行
# A list of tasty fruits
- Apple
- Orange
- Strawberry
- Mango

# 同一行
[Apple,Orange,Strawberry,Mango]
```

#### 扩展：三种常见的数据格式
- XML：Extensible Markup Language, 可扩展标记语言，可用于数据交换和配置
- JSON：JavaScript Object Notation, JavaScript对象标记法，主要用来数据交换和配置，不支持注释
- YAML：YAML Ain't Markup Language YAML 不是一种标记语言，主要用来配置，大小写敏感，不支持tab

#### Dictionary字典
字典由多个key与value构成，key和value之间用`:`分隔，所有k/v可以放在一行，或者每个k/v分别放在不同行
```yaml
# 不同行
# An employee record
name: Example Developer
job: Developer
skill: Elite

# 同一行，也可以将key:value放置于{}中进行表示，分","逗号分隔多个key:value
# An employee record
{name: "Example Developer", job: "Developer", skill: "Elite"}
```

## Ansible中的Playbook


### Playbook基础

module和playbook的区别
- Playbook是对多个AD-Hoc的一种编排组合的是实现方式
- Playbook是能控制任务执行的先后顺序
- Playbook可以持久保存到文件中从而方便多次调用运行，而Ad-Hoc只能临时运行
- Playbook适合负责的重复性的任务，而Ad-Hoc适合做快速简单的一次性任务

playbook文件规范
- 扩展名为yaml或yml
- 使用#作为注释
- 大小写敏感
- 缩进统一
- 使用"-" + "一个空格"来表示单个列表项
- 使用":" + "空格"来表示一个键值对
- 使用"{}"来表示一个键值表
- 一个name只能有一个task

样例
```yaml
- host: 10.0.0.107
  remote_user: root
  task: 
    - name: test-playbook-task-1
      ping: 
```

#### YAML格式详解
```yaml
#[{hosts: test, gather_facts: no, remote_user: root, tasks: [{name: test command, command: ls, args: {chdir: /etc/}}]}]

- hosts: test
  gather_facts: no
  remote_user: root
  tasks:
  - name: test command
    command: ls
    args:
      chdir: /etc/
   # 缩进统一即可，上下两种写法都OK
   #- name: test command
   #  command: ls
   #  args:
   #    chdir: /etc/
  - name: test ping
    # ping模块没有值，可以空着
    ping:
```

### Playbook的构成
Playbook是由一个或多个"play"组成的`列表`。playbook的主要功能在于，将多个play组织在一个playbook文件中，让多台预定义的主机按照playbook中编排的内容来完成一系列复杂的功能

主要由以下几个部分构成
- <span style="color:tomato;font-weight:700">facts</span>
  - 默认会自动调用的模块，获取远程主机的一些信息，可以在下面的任务中使用，相当于构造函数，可以禁用；
- <span style="color:tomato;font-weight:700">hosts</span>
  - 指定要执行任务的远程主机，其值可以是通配符，主机或组，但一定是要在主机清单中定义过的(/etc/ansible/hosts),可以用-i选项指定自定义的主机清单文件
  ```shell
  one.example.com         #域名
  192.168.1.50
  192.168.1.*             # 网段
  Websrvs:dbsrvs          # 或者，两个组的并集
  Websrvs:&dbsrvs         # 与，两个组的交集
  Websrvs:!phoenix        # 在websrvs组，但不在dbsrvs组
  ```
- <span style="color:tomato;font-weight:700">remote_usr</span>
  - 指定任务在远程主机上执行时，所使用的用户，可以是任意用户，也可以sudo，但前提是用户是存在的，默认root，可以不写
- <span style="color:tomato;font-weight:700">variables</span>
  - 定义playbook运行时需要的使用的变量，有多种定义方式
- <span style="color:tomato;font-weight:700">templates</span>
  - 模板模块，配合变量，模板文件，可以实现批量执行时，在不同主机上用同一个模板生成不同配置文件的功能
- <span style="color:tomato;font-weight:700">tasks</span>
  - 定义要在远程主机上执行的任务列表，各任务按顺序在hosts中指定的主机上执行，即所有主机做完当前的任务，才会开始下一个任务，task的模式是执行指定模块，后面跟上预定参数，参数中可以使用变量，模块的执行是幂等的。这意味着多次执行时安全的，因为其结果均一致，如果执行过程中发生错误，则会全部回滚（包括前面已执行成功的）；每个task都应该定义name，用于执行结果的输出，如果没有指定name，则action的结果将用于输出
- <span style="color:tomato;font-weight:700">tags</span>
  - 定义哪些代码可以被忽略，就用tags跳过部分代码；
- <span style="color:tomato;font-weight:700">notify/handlers</span>
  - 一般配合使用，可以达到一种触发调用的效果

### Playbook命令

ansible-playbook
```shell
ansible-playbook <filename.yaml> ... [options]

# 常用选项
--syntax-check|--syntax         # 语法检查
-C|--check                      # 模拟执行，只检测可能发生的变化，但不真正执行
-i|--inventory|--inventory-file # 指定主机清单文件
-e|--extra-vars                 # 定义变量
--bacome-usr                    # 指定用户执行
--list-hosts                    # 列出所有主机
--list-tags                     # 列出playbook中所有tag
-skip-tags                      # 跳过指定的tags
-t|--tags                       # 只执行特定tag对应的task
--start-at-task                 # 从指定task开始执行
--list-task                     # 列出所有task
```

示例
```yaml
- hosts: group3                         # 指定主机分组
  gather_facts: no                      # 不收集主机信息
  remote_user: root                     # 远程执行用户
  tasks:                                # task列表
    - name: task-cmd                    # task名称
      command: echo "hello ansible"     # 具体执行的命令和参数

    - name: task-shell
      shell: id
      remote_user: tom
```

#### ansible-vault文档加解密命令

```shell
ansible-vault [-h]

# 子命令
create             # 新建加密文件
decrypt            # 去掉加密文件密码
edit               # 编辑
view               # 查看
encrypt            # 加密文件
rekey              # 修改口令

# 创建"新"文件
ansible-vault create test2.yaml

# 输入密码后查看
ansible-vault view test2.yaml

# 输入密码后编辑
ansible-vault edit test2.yaml

# 去掉密码保护
ansible-vault decrypt test2.yaml

# 加密执行，指定密码文件
ansible-playbook --vault-password-file pwd.txt test2.yaml
```

### playbook案例




### Playbook中的nofify和handlers

Handlers本质上也是task list, 也定义了一系列的task，每个task中同样调用指定模块执行操作，只不过Handlers中定义的task，不会主动执行，需要配合notify，让notify通知相应的Handers中的task，让task才会执行，而且，Handers中的task，是在playbook的tasks中所有的task都执行完成之后才调用，这样是为了避免多次触发同一个Hander导致多次调用。

notify配合handlers，可以实现在特定条件下触发某些操作，特别适用于类似于服务重启，重载等场景。

注意
- 如果多个task通知了相同的handlers，此hanzXdlers仅会在所有task结束后运行一次
- 只有notify对应的task发生改变了才会通知handlers，没有改变则不会触发handlers
- handlers是在所有前面的tasks都成功执行才会执行，如果前面任何一个task失败，会导致hankler跳过执行

范例
```yaml
- hosts: rocky
  gather_facts: no
  tasks:
    - name: config file
      copy: src=/root/nginx_v2/linux.magedu.com.conf dest=/etc/nginx/conf.d/
      notify: restart service   # 当配置文件发生了变化时，通知重启服务

  handlers: 
    - name: restart service
      service: name=nginx state=restart
```

### 忽略错误ignore_errors

在同一个playbook中，如果一个task出错，则默认不会在继续执行后续的其它task，利用`ignore_error:yes`可以忽略此task的错误，继续执行其他task，此项也可以配置为全局配置

范例
```yaml
- hosts: Rocky
  gather_facts: no
  ignore_errors: yes
  tasks:
    - name: task-1
      shell: echo "task-1"

    - name: task-2
      shell: echo00 "task-2"

    - name: task-3
      shell: echo "task-3"
```

### Playbook中的tags

默认情况下，Ansible在执行一个playbook时，会执行playbook中所有的任务在playbook文件中，可以利用tags组件，为特定task指定标签，当在执行playbook时，可以只执行特定tags的task，而非整个playbook文件

可以一个task对应多个tag，也可以多个task对应一个tag

还有三个内置的tag， all表示所有任务，tagged表示所有被tag标记的任务，untagged表示所有没有被标记的任务

tags主要被用于调试环境

范例
```yaml
- hosts: group1
  gather_facts: no
  tasks:
    - name: task-1-tag1-tag11
      shell: echo "task-1"
      tags: [tag1, tag11]

    - name: task-2-tag1-tag2
      shell: echo "task-2"
      tags: [tag1, tag2]

    - name: task-3-tag3
      shell: echo "task-3"
      tags: [tag3]

    - name: task-4-no-tags
      shell: echo "task-4"
```

```shell
# 列出所有tags
ansible-playbook 2.tags.yaml --list-tags

# 执行特定tags
ansible-playbook 2.tags.yaml -t tag1 tag2

# 跳过特定tag
ansible-playbook 2.tags.yaml --skip-tags tag1

# 跳过所有有tag的task
ansible-playbook 2.tags.yaml --skip-tags tagged
```

### playbook中的变量

使用变量
- 通过{{ variable_name }}调用变量，且变量名前后建议加空格，在某些情况下需要加双引号，写成`"{{ variable_name }}"`

变量来源
1. 使用setup facts获取的远程主机的信息都放在变量中，可以直接使用
2. 在命令行执行ansible-playbook时，可以使用`-e`选项设置变量，这种变量的优先级最高
3. 在playbook文件中定义变量
4. 在单独的变量文件中定义变量，再在playbook中引用该文件
5. 在主机清单文件中定义，当单独主机的变量与分组的变量有冲突时，单独定义的主机的变量，优先级更高
6. 在主机变量目录（host_vars）和主机分组目录（group_vars）中创建以主机名或分组名为文件名的文件，在该文件中定义
7. 使用register将其它task或模块的执行的输出内容保存到变量中，供别的task来使用
8. 在role中定义


范例
```yaml
- hosts: Rocky
  gather_facts: yes
  tasks:
    - name: show-facts
      debug: msg={{ ansible_facts }}

    - name: show-facts-hostname
      debug: msg={{ ansible_hostname }}

    - name: show-facts-ipv4-A
      debug: msg={{ ansible_facts["eth0"]["ipv4"]["address"] }}--{{ ansible_facts.eth0.ipv4.address }}

    - name: show-facts-ipv4-B
      debug: msg={{ ansible_eth0["ipv4"]["address"] }}--{{ ansible_eth0.ipv4.address }}

    - name: show-facts-ipv4-C
      debug: msg={{ ansible_default_ipv4["address"] }}--{{ ansible_default_ipv4.address }}
```

#### facts配置说明

在ansible-playbook中，facts信息收集默认是开启的，如果不需要，则要在playbook中显示指定，关闭后执行性能更好
```shell
- hosts: all
  gather_facts: no
```

如果需要收集远程主机的信息，那么合理的配置facts信息的本地缓存策略，也能加速性能
```shell
cat /etc/ansible/ansible.cfg

[defaults]
# facts策略，默认smart，新版默认implicit
# smart 远程主机信息如果有本地缓存，则使用缓存，如果没有，就去抓取，再存到缓存中，下次就直接使用缓存信息
# implicit 不使用缓存，每次都抓取新的
# explicit 不收集主机信息，除非在playbook中用gather_facts: yes显示指定
gathering = smart|implicit|explicit
fact_caching_timeout = 86400  # 本地缓存时长，默认86400s
fact_caching = memeory|jsonfile|redis  # 缓存类型，默认memory，如果是jsonfile，需要指定文件路径
fact_caching_connection=/path/to/cachedir  # 本地缓存路径
```

范例：配置facts信息本地缓存
```shell
cat /etc/ansible/ansible.cfg
gatering=smart
fact_caching=jsonfile
fact_caching_connection=/tmp/ansible-facts/
fact_caching_timeout=30
```

#### 在命令行中定义变量
```yaml
- hosts: Rocky
  gather_facts: no
  tasks:
    - name: show-val
      debug: msg={{ uname }}--{{ age }}

    - name: notify
      shell: echo "123"
      notify: handler-1

  handlers:
    - name: handler-1
      debug: msg={{ gender }}
```

范例
```shell
# 多个变量一起定义
ansible-playbook -e "uname=tom age=18 gender=M" 4.var.yaml

# 从文件中读取
cat var.txt
uname: jerry
age: 20
gender: F

# 文件前面要加@
ansible-playbook -e "@/root/ansible/var.txt 4.var.yaml"
```

#### 在playbook文件定义变量

在playbook文件中定义的变量，只能在当前playbook中使用，属于私有变量

```yaml
- hosts: Rocky
  gather_facts: no
  vars:
    uname: tom
    age: 20
    gender: F

  tests: 
    - name: show-val
      debug: msg={{ uname }}--{{ age }}
    - name: notify
      shell: echo "123"
      notify: handler-1
    
  handlers:
    - name handler-l
      debug: msg={{ gender }}

```

#### 在单独文件中定义变量

在单独的变量文件中定义变量，再在playbook中引用该文件，在单独文件中，定义的变量优先级比playbook中定义的变量优先级高

范例
```shell
cat var4_file_start.yaml

var1: var-file-1
var2: var2-file-2

cat var4_file_end.yaml

var4: var2-file-4

cat var4.yaml
```

```yaml
- hosts: group1
  gather_facts: no
  vars_files:
    - var4_file_start.yaml               # 相对路径算法
    - /root/var4_file_end.yaml           # 绝对路径喜才算
```


#### 在主机清单中定义变量


#### 在项目目录中定义变量

在不同的项目中添加hosts_vars, group_vars目录，在hosts_vars目录下添加主机名或ip命名的文件，将该主机的变量写在此文件中，在group_vars目录中添加以分组命名的文件，将该组的变量写在此文件中

```shell
cat /etc/ansible/hosts

[all:vars]
var1=all-var1
var2=all-var2
var3=all-var3

[group1]
10.0.0.106
10.0.0.157

[group1:vars]
ansible_python_interpreter=/usr/bin/python3
ansible_ssh_password='123456'
var2=group1-var2
var3=group1-var3

[group2:children]
group1


[group2:vars]
var3=group2-var3
var4=group2-var4
```

tips: group_vars和hosts_vars目录和yaml文件在同一级目录

在项目目录下，添加gruop_vars目录和hosts_vars目录，然后在里面创建文件
```shell
group_vars
    - gruop1
host_var2
    - 10.0.0.166
var6.yaml
var7.yaml
```

在host_vars 目录中定义的变量优先，group_vars次之，hosts,最次之

#### 全局变量
全局变量，是我们使用ansible或使用ansible-playbook时，手动通过-e参数传递给Ansible的变量
```shell
# ansible|ansible_play -h | grep var
-e EXTRA_VARS, --extra-vars=EXTRA_VARS

# 示例
ansible all -i localhost, -m debug -a "msg='my key is {{ key }}'" -e "key=value"

# 示例2：传递一个YAML/JSON的形式(注意不管什么形式，最终一定要是一个字典)
# cat a.json
{"name":"magedu","type":"school"}
ansible all -i localhost, -m debug -a "msg='name is {{ name }}, type is {{ type }}'" -e @a.json

# 示例3：传递YAML格式的文件，作为key/value传递
# cat var.yaml
student:
  name: curry
  age: 18
  gender: male

# 引用yaml文件传递变量
ansible ubuntu2204 -m debug -a "msg='name is {{ student.name }}, age is {{ student.age }}'" -e @var.yaml
```

#### 剧本变量
- 通过PLAY属性vars定义
```yaml
- hosts: ubuntu2204
  gather_facts: no
  remote_user: root
  vars:
    user: mystical
    home: /home/mystical 
```
- 通过PLAY属性vars_files定义
```yaml
- hosts: ubuntu2204
  gather_facts: no
  remote_user: root
  vars_files:
  - vars/users.yaml   # 可以引用多个文件，使用相对路径
  - vars/groups.yaml
```

#### 在Playbook中使用变量的注意点
```yaml
# 引用变量的时候记得加双引号
"{{ user }}"
```

#### 资产变量
```yaml
# 资产变量分为主机变量和主机组变量，分别针对单个主机和主机组
# 主机变量
cat hosts
[webservers]
10.0.0.131  user=mystical age=12 ... #多个变量使用空格隔开

# 主机组变量
[websevers:vars]       # group_name:vars
home="/home/mystical"

# 主机和主机组变量key重名，主机变量的优先级更高
```

#### 变量的继承
```yaml
# 资产继承的同时，对应的变量也发生了继承
[web]
10.0.0.131
[db]
10.0.0.132
[allserv]
[allserv:children]
web
db

[allserv:vars]     # web和db都继承该变量
user=mystical
```

#### facts变量
```shell
# 取facts变量的值使用点
- hosts: ubuntu2204
  gather_facts: yes
  remote_user: root
  tasks:
 # - name: user var
 #   setup: 
 #     filter: ansible_nodename
 #   register: hostname
  - name: print var
    debug:
      # 字典就.key，列表使用.index, eg: .0, .1, ...
      msg: "memory free is {{ ansible_memory_mb.real.free }}"
```
#### register注册变量

在playbook中可以使用register将捕获命令的输出保存在临时变量中，方便后续调用此变量

```yaml
- hosts: 10.0.0.166
  gather_facts: no
  tasks:
    - name: register
      shell: hostname
      register: hostname_rs

    - name: reg-rs-all
      debug: msg={{ hostname_rs }}

    - name: reg-rs
      debug: msg={{ hostsname_rs.stdout }}
```

## Ansible中的Templates

Ansible中的模板

狭义来讲，就是一个特定后缀的文本文件，在使用时，可以根据此文件，将部分关键内容进行替换，生成新的文件，以达到在不同的主机中，使用不同配置的作用，其中的逻辑部分或动态代码，用jinja2来实现

广义来讲，要模板文件，变量，变量文件，参数，条件判断，流程控制，playbook中的template模块调用时相互配合，来实现预期的效果


## Ansible任务控制
### 条件判断
#### 实战案例
- Nginx语法校验
```yaml
- name: check nginx syntax
  shell: /usr/sbin/nginx -t
```

- 获取Task任务结果
```yaml
- name: check nginx syntax
  shell: /usr/sbin/nginx -t
  register: nginxsyntax
```

- 通过debug模块取确认返回的结果的数据结构
```yaml
- name: print nginx syntax result
  debug: var=nginxsyntax
  # 根据返回结果判断：如果nginxsyntax.rc == 0则表示执行成功
```

- 根据返回结果执行或不执行nginx服务启动
```shell
- name: start nginx server
  service: name=nginx state=started
  when: nginxsyntax.rc == 0
```
- 多分支可以写多个when
```yaml
- hosts: all
  tasks:
    - name: Install package on Ubuntu
      apt:
        name: vim
        state: present
      when: ansible_distribution == "Ubuntu"

    - name: Install package on CentOS
      yum:
        name: vim
        state: present
      when: ansible_distribution == "CentOS"

    - name: Install package on Debian
      apt:
        name: vim
        state: present
      when: ansible_distribution == "Debian"
```

- when支持的运算符
```shell
==
!=
> >=
< <=
is defined
is not defined
true
false
支持逻辑运算符：and, or
```

### 循环控制
在playbook中使用`with_items`去实现循环控制，且循环时的中间变量只能是关键字item，不能随意定义
```yaml
- hosts: ubuntu2204
  gather_facts: no
  vars:
    createuser:
      - tomcat
      - www
      - mysql
  tasks:
    - name: create user
      user: name={{ item }} state=present
      with_items: "{{ createuser }}"
```

- 新版本循环
```yaml
# 使用loop
- hosts: ubuntu2204
  gather_facts: no
  vars:
    some_list:
      - a
      - b
      - c
  tasks:
    - name: show item
      debug:
        var: {{ item }}
      loop: {{ some_list }}  # 就是使用loop替代了with-items
```
#### 字典循环
```yaml
- hosts: localhost
  tasks:
    - name: Example of with_dict
      debug:
        msg: "Key: {{ item.key }}, Value: {{ item.value }}"
      with_dict:
        my_dict:
          key1: value1
          key2: value2
          key3: value3
```

#### 嵌套循环
```yaml
- hosts: ubuntu2204
  gather_facts: no
  remote_user: root
  vars:
    users:
      - name: Alice
        roles:
          - admin
          - user
      - name: Bob
        roles:
          - user
          - guest
  tasks:
  - name: test loop
    debug:
      msg: " {{ item.0 }}"
    with_subelements:
      - "{{ users }}"  
      - roles
```

### Jinja2语言

Jinja2是Python下一个被广泛应用的模板引擎，他的设计思想来源于Django的模板引擎，并扩展了其语法和一系列强大的功能

#### jinja2的条件判断
```jinja
{% if EXPR %}
...
{% endif %}
-----------------------
{% if EXPR %}
...
{% else %}
...
{% endif %}
----------------------
{% if EXPR %}
...
{% elif EXPR %}
...
{% else %}
...
{% endif %}
```

#### jinja2在playbook中的分支和短路运算
```yaml
- name: Set a fact based on a condition
  set_fact:
    result: "{{ 'Success' if my_var == 'Hello' else 'Failure' }}"

---

{{ value1 and value2 }}   # 短路与
{{ value1 or value2 }}    # 短路或
```

#### Jiaja中的流程控制

For循环
```jinja
{% for i in EXPR %}
...
{% endfor %}
```

### jinja2常用函数
#### map()
`map()`函数用于将一个函数应用到一个可迭代对象的每个元素上。常见的用途包括从一组字典中提取某个字段的值

- 基本语法
```jinja
{{ list | map('function_name', *args) | list }}
```
- `list`: 要处理的列表或其他可迭代对象
- `function_name`：要应用于列表中每个元素的函数或过滤器
- `*args`：可选参数，根据具体的函数或过滤器需求传递

- 常用函数与`map()`的组合
1. `map('extract', hostvars, 'var_name')`
`extract`函数用于从字典中提取指定键的值。与`hostvars`结合使用时，可以从每个主机的变量中提取特定的量
```yaml
- name: Get IP addresses of all hosts in a group
  debug:
    msg: "{{ groups['webservers'] | map('extract', hostvars, 'ansible_default_ipv4') | map(attribute='address') | list }}"
# `groups['webservers']`返回webservers组中的所有主机
# map('extract', hostvars, 'ansible_default_ipv4')从hostvars中提取每个主机的ansible_default_ipv4变量
# map(attribute='address')从提取的ansible_default_ipv4结果中进一步提取address字段
# 最终输出是一个包含所有webservers组主机的IP地址的列表
```

2. `map('upper')`
`upper`函数将字符串转换为大写。与`map()`结合使用时，可以将列表中每个字符串转换为大写
```yaml
- name: Convert all items in a list to uppercase
  debug:
    msg: "{{ ['apple', 'banana', 'cherry'] | map('upper') | list }}"
```
3. `map(lower)` 
同上

4. `map(replace, old, new)`
`replace`函数用于替换字符串中的子字符串。与`map()`结合时，可以对列表中的每个字符串进行替换操作
```yaml
- name: Replace '-' with '_' in a list of strings
  debug:
    msg: "{{ ['a-b-c', 'd-e-f', 'g-h-i'] | map('replace', '-', '_') | list }}"
# 最终输出为 ['a_b_c', 'd_e_f', 'g_h_i']
```

5. `map('regex_replace', pattern, replacement)`
`regex_replace`函数用于使用正则表达式进行替换。与`map()`结合时，可以对列表中的每个字符串进行正则替换
```yaml
- name: Replace digits in strings with '*'
  debug:
    msg: "{{ ['abc123', 'def456', 'ghi789'] | map('regex_replace', '\\d', '*') | list }}"
# 最终输出为：['abc***', 'def***', 'ghi***']
```

6. `map(attribute='attribute_name')`
这个形式允许直接访问列表中每个元素的某个属性或字典值
```yaml
- name: Get FQDN of all hosts
  debug:
    msg: "{{ groups['all'] | map(attribute='ansible_fqdn') | list }}"
# 最终输出将返回所有主机的FQDN列表
```

#### to_json()和to_yaml()
这些函数用于将数据结构转换为JSON或YAML格式的字符串

#### dafault()
`default`函数用于在变量为空或未定义时提供默认值
- 示例
```yaml
- name: Use default value if variable is undefined
  debug:
    msg: "{{ my_var | default('default_value') }}"
```
#### selectattr()和rejectattr()
这些函数用于基于属性值筛选列表中的字典。`selectattr`选择符合条件的项，`rejectattr`则排除符合条件的项

#### sort()
`sort()`用于对列表进行排序

#### join()
`join()`用于将列表中的元素连接成一个字符串


#### regex_replace()
`regex_replace()`用于使用正则表达式替换字符串的内容

#### unique()
`unique`用于去除列表中的重复元素


#### select()
`select()`函数会对列表中的每个元素应用一个表达式，并返回满足该表达式的元素

- 常见的条件表达式
```shell
odd                 # 选择奇数
even                # 选择偶数
greaterthan         # 选择大于某个值的元素
lessthan            # 选择小于某个值的元素
equalto             # 选择等于某个值的元素
string              # 选择非空字符串
defined             # 选择已定义的元素(即不为`None`)
```

- 示例
```yaml
- name: Select even numbers from the list
  debug:
    msg: "{{ [1, 2, 3, 4, 5, 6] | select('odd') | list }}"
# 输出结果为[1,3,5]

---

# 自定义条件，使用Lambda表达式作为条件
- name: Select numbers greater than 3
  debug:
    msg: "{{ [1, 2, 3, 4, 5, 6] | select('greaterthan', 3) | list }}"
# 输出结果为[4,5,6]
```


### Template的使用规范


template文件建议存放在playbook文件同级目录的templates目录下，且以.j2结尾，这样在playbook中使用模板文件时，就不需要指定模板文件路径。

范例
```shell
.
 ├── templates
 │   └── test.j2      #模板文件      
└── test.yaml         #playbook文件        

1 directory, 2 files
```

### Template的基本替换
```shell
# test-1.yaml
- hosts: group1
  gather_facts: yes
  vars:
    var1: 'abcd'
    var2: 3
    var3: 3.14

  tasks:
    - name: template-task-1
      template: src=test-1.j2 dest=/tmp/ansible-test-1.txt

# templates/test-1.j2
string----{{ var }}---{{ var1*3 }}

int----{{ var2 }}----{{ var2+10 }}----{{ var2-10 }}----{{ var2*10 }}

float-------{{ var3 }}---{{ var3+10 }}---{{ var3-10 }}---{{ var3*10 }}---{{ var3/10 }}---{{ var3//10 }}---{{ var3**2 }}

facts-------{{ ansible_default_ipv4.address }}
```






## Ansible中的Role

role(角色)用来实现代码的组织管理功能，将实现各种不同功能的playbook文件，变量文件，模板文件，handlers文件根据约定，分别放置在不同的目录，分门别类的管理起来，使其看起来更像一个项目，其主要用来解决多文件之间的相互包含，引用，组合等问题，将各个功能模块进行拆分，使其原子化，要实现一个大型复杂需求时，再用include指令来引用不同的功能

角色一般用于基于主机构建服务的场景中，但也可以是用于构建守护进程等场景中，复杂的场景中，建议使用roles，代码复用度高


### Role工作原理和组成

## Ansible自定义过滤器
自定义过滤器允许你在Jinja2模版中使用自定义的Python函数。通常，你可以通过在Ansible项目的`filter_plugins`目录中创建一个Python文件来实现自定义过滤器

### 创建自定义过滤器
- 创建一个`filter_plugins`目录
  - 在你的Ansible项目根目录下创建一个名为`filter_plugins`的目录
- 编写Python过滤器
  - 在`filter_plugins`目录中，创建一个Python文件(例如：`custom_filter.py`)，并在其中定义你的过滤器函数
```python
# custom_filters.py

def reverse_string(value):
    """Reverse a string."""
    return value[::-1]

def multiply(value, multiplier):
    """Multiply a number by a multiplier"""
    return value * multiplier

class FilterModule(object):
    """Ansible custom filters."""

    def filters(self):
        return {
            'reverse_string': reverse_string
            'multiply': multiply
        }
``` 

### 使用自定义过滤器
```yaml
- name: Use custom reverse_string filter
  debug:
    msg: "{{ 'hello' | reverse_string }}"

- name: Use custom multiply filter
  debug:
    msg: "{{ 5 | multiply(3) }}"
```

## Ansible自定义模块
### 创建`library`目录
在你的Ansible项目根目录下创建一个名为`library`的目录用于存放定义模块

### 编写Python模块
在`library`目录中创建一个Python文件，并编写你的逻辑模块
```yaml
# custom_module.py

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        message='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    name = module.params['name']

    result['message'] = f'Hello, {name}!'

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
```

### 使用自定义模块
```yaml
- name: Use custom module
  custom_module:
    name: "Ansible"
```