# PYTHON 基础
## 环境安装
- 官方现在https://www.python.org
### Linux中安装和切换python
- 安装
```
CentOS:
yum install python36 python38
```

- 版本切换与查看
```shell
查看版本信息
python3 -V

版本切换(全局切换)
alternatives --config python3
# 新版本 
update-alternatives --config python3

如果Python 版本未被 alternatives 管理，你需要手动添加它
示例：
sudo alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2

# 四个参数，第一个参数：软链接地址，第二个参数name,第三个参数，实际二进制文件路径，第四个参数：优先级

# 移除python3版本
sudo update-alternatives --remove python3 /usr/bin/python3.8
```

### pip管理
```shell
# 更换pip源
# 相当于修改/root/.pip/pip.conf
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

#### virtualenv虚拟环境
- 虚拟环境的意义
```
每个环境之间相互隔离，互不干扰，可以轻松实现多版本管理开发
建议：
每个不同的项目，单独配一个虚拟环境，并为该虚拟环境指定特定的python版本
```
- 安装
```
安装虚拟环境
# pip3 install virtualenv
```
- 如果pip出现损坏，可使用以下方法修复
```
重新安装
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
python3 get-pip.py

修复和升级pip
python3 -m pip install --upgrade pip

升级pip（简写版）
pip install -U
```
- pip通用配置
```bash
Windows配置文件：~/pip/pip.ini。Windows家目录，在“运行”中键入
Linux配置文件：~/.pip/pip.conf
新Linux配置文件：~/.config/pip/pip.conf

# 如果是新下载的python，需要手动在对应目录下创建pip.conf，然后手动添加内容

参照http://mirrors.aliyun.com

[global]
index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com

用命令更改pip3的下载源
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

直接执行上述命令可能会报错：ERROR: unknown command "config"
解决方法：升级pip，pip的config命令用于管理本地和全局配置文件，但它是在较新版本的pip中引入的。
```
- 新建一个普通用户
```
# useradd python
# echo python | passwd --stdin python
或者
# echo "python:python" | chpasswd
# su - python
```
- 创建工程目录，并设置虚拟环境
``` bash
创建项目工程目录和虚拟环境目录
mkdir -p projects/cmdb

mkdir venvs

cd venvs

virtualenv <dir> # 默认当前版本创建虚拟环境

virtualenv -p 指定python版本，默认当前版本
示例：
virtualenv -p /usr/bin/python3.6 venvs36
# 执行后，创建一个目录在当前目录下

virtualenv <环境名称(dir)>
示例：
virtualenv vcmdb

创建好虚拟环境目录后回到项目目录
cd ~/projects/cmdb/

source ~/venvs/v36/bin/activate  # 激活虚拟环境
# 在项目目录下，使用虚拟环境

# 退出虚拟环境，在当前虚拟环境目录下
deactivate
```

#### pyenv多版本管理
- 官网:https://github.com/pyenv/pyenv

- 快捷安装：https://github.com/pyenv/pyenv#the-automatic-installer
```bash
# 适用于CentOS 7,8
# yum install git curl

python编译依赖如下
# yum install git gcc make patch gdbm-devel openssl-devel
# yum sqlite-devel readline-devel zlib-devel bzip2-devel

创建普通用户
# useradd python
# su - python

在python用户下安装
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

也可以使用项目源码文件，直接bash运行

# CentOS 9以上版本安装pyenv

pyenv 需要一些依赖来编译 Python 版本。打开一个终端并执行以下命令来安装所需的依赖：

sudo dnf update -y
sudo dnf install -y @development zlib-devel bzip2 bzip2-devel readline-devel sqlite \
sqlite-devel openssl-devel xz xz-devel libffi-devel findutils

从 GitHub 克隆 pyenv 仓库到 ~/.pyenv 目录：
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

如果出现如下报错：
Cloning into '/home/python/.pyenv'...
fatal: unable to access 'https://github.com/pyenv/pyenv.git/': OpenSSL SSL_read: Connection reset by peer, errno 104

使用以下命令绕过SLL证书验证
git -c http.sslVerify=false clone https://github.com/pyenv/pyenv.git ~/.pyenv


-----------------------------------------------------------
在~/.bash_profile文件的开头添加
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
-----------------------------------------------------------
在~/.basrc的末尾添加：
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
-----------------------------------------------------------
重启你的终端或者加载配置文件：
source .bashrc

如果出现提示：pyenv: no such command `virtualenv-init'

使用如下命令下载插件：
git -c http.sslVerify=false clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
如果下载失败，请多次尝试

以后更新pyenv使用
$ pyenv update

pyenv常用命令

pyenv version  # 查看当前版本
pyenv versions # 查看所有版本

pyenv install -l # 列出所有的python解释器版本
pyenv install 3.6.9 -vvv # 下载python3.6.9

更改pyenv下载配置(目的是在非官方下载)
在.pyenv目录下，创建cache文件夹
将官网下载的python的tar包放入cache目录下
运行 pyevn install <tar包的版本号>
# 即可下载对应python

安装好python之后，创建项目目录projects
mkdir -p projects/cmdb

pyenv local <python版本号> # 为该目录设置python环境

pyenv virtualenv <python版本号> <虚拟环境目录名称>

可以在使用pyenv versions查看当前创建的所有虚拟环境版本之后
使用pyevn local 进行切换

```
#### 使用pycharm连接linux
```
和在linux上一样，
先连接虚拟机上的interface，(提示：existing)
1. 在virtualenv中，
interface在virtualenv -p /usr/bin/python3.6 venvs36
在venvs36目录下
2. 在pyenv中
interface在.pyenv/versions创建的虚拟环境下
虚拟环境的创建：
pyenv virtualenv 版本号 切换昵称
示例： pyenv virtualenv 3.8.16 v3816(本质是创建一个软链接)
然后再远程同步工程目录：tools -> Deployment -> configuration
```
#### 总结
- 重点掌握使用虚拟环境进行多版本隔离
  - 在使用virtualenv的命令
    - 需要分别创建projects目录存放项目代码
    - 还需要创建一个目录，用来引入虚拟环境的python对应版本解释器
    - 在virtualenv中，使用`virtualenv -p /usr/bin/python3.6 venvs36 `,然后，在对应项目目录下，进行虚拟环境激活 `. ~/venvs/venvs36/bin/activate`
    - 退出需要`deactivate`
  - 使用pycharm（windows系统）
    - 在setting中进行设置，原理和Linux中相同
  - 多版本管理工具：pyenv
    - 可以更方便的进行多版本的管理和多项目的隔离

- 核心思想
  - 项目和环境分开，每个项目单独配一个环境目录
  - 在pycharm远程连接时，先环境interface连接，然后项目目录同步，

- 轻量级练习，建议使用jupyter
  - 安装：`pip install jupyter`
  - 进入：`jupyter notebook` 
  - jupyter快捷键
    - L  增加行号
    - a  之前插入代码块
    - b  之后插入代码块
    - shift + enter  运行当前代码块
    - dd  删除选中的代码块

## 基础语法
### 数据类型
- 整数int
  - Python3开始不再区分long,int,long被重命名为int，所以只有int类型
  - 进制表示：
    - 十进制：10
    - 十六进制：0x10
    - 八进制：0o10
    - 二进制：0b10
  - bool类型：
    - True
    - False

- 浮点数float
  - 本质上使用C语言的double

- 字符串
  - 使用'"单双引号引用的字符的序列
  - '''|"""单双三引号，可以跨行，可以在其中自由的使用单双引号
  - r前缀：在字符串前面加上r或R前缀，表示该字符串不做特殊处理
  - f前缀：3.6版本开始，新增f前缀，格式化字符串
  - 转义字符
  ```
  \n 换行符newline  Linux
  \r 回车符return   Mac
  \r\n 回车换行符   Windows

  \t tab 向右偏8个或4个单位
  注意：转义字符占1个字符长度，和表现形式无关
  ```

- 续行
```
当源代码一行写不下时，可以使用'\'续行
print("abc"\
"123")

# abc123
```

### 字符串
#### 字符串格式化（simple）
```python
用法1：
a = 1
b = 3
print("{},{},{},{}".format(a,b,100,a+b))
# 1,3,100,4

用法2：
print(f"{a}+{b}={a+b}")
# 1+3=4

老用法：

```

### 标识符
- 示例：
```python
a = 1
# 这里a就是标识符，1是存储在内存中的数据
# a实际上存储的是整数对象1的内存地址
# a可以看作是内存地址的助记符

b = 1
b = 'a'
# 在这个过程中，数据1的地址和之值都没变
# 而是b存储的内存地址发生了改变，变为了'a'所在的内存地址
```
- 注意：
  - 标识符不能使用数字开头
  - 全部小写，多个单词使用下划线

- 变量与常量
  - 变量：标识符可以被重新赋值，改变指向的内存地址
  - 常量：一旦定义，就不能改变标识符指向的内存地址
    - python无法定义常量
    - 但是python中有字面量，字面量不可变
    ```python
    a = 1
    a = a + 1

    过程说明：
    在Python中，整数是不可变的数据类型。这意味着你不能改变整数对象的值。当你执行 a = a + 1 时，实际上发生了以下几个步骤：

    计算表达式 a + 1 的结果，这产生了一个新的整数对象，其值为2。
    将变量 a 重新绑定到这个新创建的整数对象。
    如果没有其他引用指向之前的整数对象1，它将成为垃圾，稍后由垃圾回收器回收。
    在这个过程中，变量 a 的内存地址确实发生了改变。它最初指向值为1的整数对象，最后指向值为2的整数对象。而整数对象1本身并没有发生变化，因为整数是不可变的。

    这个过程和javascript中类似，和PHP不同
    在PHP中，当你改变变量的值时，它可能会直接更新变量的内存地址上的数据，或者可能会在不同的内存地址上创建一个新的值，这取决于变量的类型和它是如何被使用的。PHP使用一种称为“引用计数”的机制来跟踪变量的引用，并在不再需要时释放内存。
    ```
    ```python
    n1 = 1
    n2 = n1
    n1 += 1
    print(n1, n2) # 2, 1

    底层原理：
    变量赋值（n1 = 1）：

    当执行 n1 = 1 时，Python首先检查整数对象 1 是否已经存在。
    Python对小的整数和短字符串有特殊处理，通常它们是预先创建并重用的（这是一种内存优化）。因此，当你创建一个值为 1 的变量时，Python实际上会将 n1 指向已经存在的整数对象 1 的内存地址。
    
    变量赋值（n2 = n1）：

    接着执行 n2 = n1 时，Python会使 n2 也指向 n1 指向的那个内存地址。
    在这个例子中，n1 和 n2 实际上是指向同一个整数对象 1 的内存地址。这是因为整数在Python中是不可变的，所以共享同一个对象是安全的。
    ```

#### tip1
- javascript和PHP和python在变量赋值和引用传递方面，它们表现出相似的行为。当你给变量赋一个新的值时，你实际上是改变了这个变量引用的内存地址。
- C语言不同，在C语言中，变量赋值并不涉及改变变量引用的内存地址，而是直接改变存储在该内存地址上的值。
```
在C语言中，每个变量都占用内存中的一个特定地址，这个地址在变量的生命周期内是不变的。当你改变一个变量的值时，你是在改变存储在这个内存地址上的数据，而不是改变变量的内存地址。
```
```C
int a = 5;  // 'a'被赋值为5，它存储在内存中的某个特定地址上
a = 10;     // 现在，相同的内存地址上存储的值被改变为10
```
- python是动态语言，强类型语言
```
静态语言：java, C, C++
int a = 200;
a = 100
a = 'a'// 会转换成int类型后存储

a = "abc" // 报错，abc是字符串，是指针类型，无法转换成int类型

需要指定声明标识符类型，之后不可以改变类型赋值
静态语言编译的时候会检查类型

动态语言：python
a = 1
a = 'abc'

不需要事先声明类型，赋值的一刹那决定了类型

总结：动态语言中变量赋值后之所以可以改变类型，本质上是因为，变量赋值是内存地址指向的改变，而静态语言不是
```
- 类型注解
```python
a:int = 5 # 仅仅注释，无法实质作用
# 但是在pycharm中，标注了类型注释后
# 如果变量的类型后期发生改变，pycharm会高亮提示
```

- 强类型语言
  - 不同类型之间操作，必须先强制类型转换为同一类型
  ```python
  print('a'+1) # 报错
  ```

- 弱类型语言
  - 不同类型间可以操作，自动隐式转换，JavaScript中console.log('a'+1)
  - 注意：强弱是一个相对概念，即使是强类型语言也支持隐式类型转换

### 布尔值
- False等价布尔值，相当于bool(value)
  - 空容器（仅限python）（js中为真）
    - 空集合set
    - 空字典dict
    - 空列表list
    - 空元组tuple
  - 空字符串
  - None
  - 0

### 运算符Operator
#### 算数运算符
- +、-、*、/、//向下取整整除、%取模、**幂
- 注：在Python2中/和//都是整除

#### 位运算符
- `&` 位与
- `|` 位或
- `^` 异或
- `<<` 左移
- `>>` 右移
- `~` 按位取反，包括符号位

#### 短路运算符
```python
a = True and 1 
# a = 1,type(a) -> int

a = True and 1 and ''
# a = ''

a = True and 1 and '' and 'abc'
# a = ''
# and运算，当遇到假时，整个公式必然为假，因此停在''

a = ?
i = a or 'abc'
# 'abc'为i的缺省值，如果a为空，则i的值是'abc'，否则值为a的值

x and y and a and b
# 当遇到一长串短路运算的时候，把决定性数据放在前面
# 因为越早短路越高效，短路后面的数据不会执行
```
- 总结：
  - and 运算，当遇到假的值的时候，为决定性数值，停留在此
  - or 运算，当遇到真的值的时候，为决定性数值，停留在此
  - 把最频繁使用的，做最少计算就可以知道结果的条件放前面，如果它能短路，将大大减少计算量
  - 注意：python没有三目运算符（a?b:c），C语言支持

#### 赋值运算符
```python
a = 1
a += 100 # 赋值即定义
# 101
```
- 符号：
  - `+=`
  - `-=`
  - `*=`
  - `/=`
  - `%=`
  - `//` 整除

#### 成员运算符
- in、not in，用来判断是否是容器的元素，返回布尔值

#### 身份运算符
- is、is not，用来判断是否是同一个对象

### 内置函数
#### 强制类型转换
- str()
  - 本质是把内容用人看得懂得字符串文件表达
- bool()
- int()
- float()
- 
#### 输入函数
- 命令：`input`
```python
a = input('please input a num')
print(a)
```
#### type
```python
type(str) # 返回：type

# type是元类，str, list, int...都是type构造的类 
# type是所有类（包括自定义类）的元类
```

#### isinstance
```python
语法：isinstance(1,str) # 是谁的实例吗？
# 这句化的意思是1是str的实例吗
# 返回：False

isinstance(False, (str,int,bool))
# 返回：True
# 因为True是元组中bool的实例
```

#### print
```python
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# sep='?' 用来确定分隔符，默认以空格为分隔符
# end='\n' 生成的字符串结尾是\n

print(1,end='')
print(2)
# 12

# 示例：
x = input('>>>')
print(1,100,sep=x or '/t')
```

### 程序控制
#### 分支语句
- if 语句
```python
# 搭框架阶段，在没想好if后面些什么的时候可以用pass占位且不报错
# 用使用注释标注好将来要完成的功能
# 单分支
if True:
    pass #TODO

# 双分支
if True:
    pass
else:
    pass

# 双分支特殊写法（这种写法的时候，if语句是表达式，可以赋值）
pass1 if True else pass2

#示例：
a = int(input('请给我一个整数: '))
print('a小于等于5') if a <= 5 else print('a大于5') 

# 多分支
if True:
    pass
elif True:
    pass
elif True:
    pass
else:
    pass
```
- 示例
```python
a = 5
if a > 0:
    print(a,'positive')
elif a == 0:
    print('zero')
else:
    print('negative')
```

- match 语句（仅支持3.10以上版本）
```python
match http_response_status:
    case 400:
      print("Bad request")
    case 404:
      print("No found")
    case 418:
      print("i'm a teapot")
    case _:
      print("Something's wrong with the internet") 
      #变量名“_”为通用匹配符，确保match必定被匹配成功。

# match语句组合模式
match http_response_status:
    case 400|403|404: #可以使用“|”在一个模式中组合多个字面值
      print("4XX error")
    case 500|501|503:
      print("5XX error")
    case _:
      print("strange wrong")
```

#### 循环语句
- While 
```python
while True: # 进入循环体
    pass
```
- 示例：
```python
'''模拟cat命令'''
while True:
    x = input('~ #') # 输入命令后，进入，退出，未知
    match x:
        case 'cat': # 进入程序后，启动程序
            a = input('>>>')
            while a != 'exit':
                print(a)
                a = input('>>>')
        case 'quit':
            print('shotdown')
            break
        case _:
            print("not found command")
```

- for 循环
```python
for i in ['可迭代对象']: # 遍历
# 示例：
for i in range(10): # 运行10次
    print('hello')

# range(开始，结束，步长)
for i in range(1,10,2): 
    print(i) # 1,3,5,7,9

# 奇数判断：使用位运算
for i in range(10):
    if i & 1: # 位运算
        print(i)

for i in range(8,-3,-1):
    if i: # 忽略0
        print(i)

for i in range(10):
    print(i)
else:
    print("end")
# for循环中的else在全部遍历后执行，如果中途跳出则不执行
```
#### 扩展1：字典遍历
```python

friends = ['tim','brown','gess']
for friend in friends:
	print(friend.capitalize())#名字首字母大写

movie = {'name':'friend','language':'En',"other name":'Six of one'}
for title in movie.keys: #keys可以换成values来遍历值
	print

 

for i in enumerage(movie.items()) #enumerage()返回值是一个枚举类型，（enumerage,at,0x104b85d00）
	print(i)
	>>>
	(0,('name','Friend'))
	(1,('language','En'))
	(2,('other name','Six of one'))
#返回带排列序号的元组
```

#### 扩展2：for循环实现推导式
- 作用：从一个序列构造另一个序列
```python

list1 = [i for i in (1,2,3,4)] # 列表推导式
list2 = [i*i for i in (1,2,3,4)] # 列表推导式
list3 = [i*i for i in (1,2,3,4)if i < 3] #输出>>>[1,4]

# 示例2：
list = [1,2,3,4]
list2 = [i*i for i in list]
print(list2) #[1, 4, 9, 16]
```

### 常用数值处理函数
- min()、max()
- abs()
- pow(x, y) == x ** y
- math.sqrt() == x ** 0.5
- bin()、oct()、hex()
- math.pi
- math.floor()
- math.ceil()

### 线性数据结构 —— 线性表
- 线性表：
  - 线性表（简称表），是一种抽象的数学概念，是一组元素的序列的抽象，它由有穷个元素组成（0个或任意个）
  - 顺序表：使用一大块连续的内存顺序存储表中的元素，这样实现的表称为顺序表，或者称为连续表
    - 在顺序表中，元素的关系使用顺序表的存储顺序自然地表示
  - 链接表：在存储空间中将分散存储的元素链接起来，这种实现称为链接表，简称链表

- 顺序表特点：
  - 顺序表，开辟空间后，首地址不变

- 顺序表的操作
  - 增
    - 头部增加insert，引起后面所有的数据挪动
    - 中间插入insert，引起其后数据的挪动
    - 尾部追加，推荐
  - 删：
    - 头部删，引起其后数据的挪动
    - 中间删，引起其后元素挪动
    - 尾部删，推荐
  - 改：（内存寻址：顺序表首地址 + 索引 * 4字节(int)）
    - 通过index直接定位元素，覆盖即可
  - 查：
    - 通过索引找人

- 链表特点
  - head，首地址可变
  - ，每个元素除了记录本身的值以外，还记录prev(前一个地址)，next(后一个地址)

- 链接的操作
  - 增
    - 头部增：head，首地址改变，然后新填元素和原首地址元素互指
    - 中间增：断开手，拉新手
    - 尾部增：动（tail-尾部标记），拉手 
  - 删：
    - 头删：首地址改变，效率高
    - 中间删：重新拉手，效率高
    - 尾删：动tail，效率高
  - 改：有索引，使用索引查找，相对顺序表效率有点差
  - 查：有索引，使用索引查找，相对顺序表效率有点差

### 队列（queue）
- 概念：一般情况下，队列的操作只在某一端，或者同时两端
  - FIFO（先进先出）
    - 适合使用链接表实现
  - LIFO（后进先出）栈（stack）
    - 使用顺序表和链接表都可以实现，python中使用顺序表（其他语言中多数是链接表实现）
  - 优先  
  - 双端队列：
    - 使用链接表实现