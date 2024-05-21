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

