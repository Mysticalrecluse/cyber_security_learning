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
```
查看版本信息
python3 -V

版本切换(全局切换)
alternatives --config python3
```

#### virtualenv虚拟环境
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

virtualenv 命令 # 默认当前版本创建虚拟环境

virtualenv -p 指定python版本，默认当前版本
示例：
virtualenv -p /usr/bin/python3.6 venvs36
# 执行后，创建一个目录在当前目录下

virtualenv <环境名称>

. ~/venvs/v36/bin/activate  # 激活虚拟环境
# 在项目目录下，使用虚拟环境
```

#### pyenv多版本管理
- 官网:https://github.com/pyenv/pyenv

- 快捷安装：https://github.com/pyenv/pyenv#the-automatic-installer
```bash
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

如果前面没有出现（v3816）类似这种设置好的自定义虚拟环境名称
在.bash_profile的文件中，添加下列内容
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

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
print("%d+%d=%d"%(a,b,a+b))
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
  - 注意：python没有三目运算符（a?b:c）

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
  - `//`

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
# 返回：True

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