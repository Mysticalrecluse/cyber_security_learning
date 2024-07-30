# Python入门
## Python介绍
<h4>Python是一门动态强类型语言</h4>
<b>动态</b>： 
指python在赋值的时候不需要指定变量类型，因为在python中，变量的本质是数据的指针（正确说法是对对象的引用）<span style="color: darkgreen; font-weight: 700;">在 Python 中，所有的数据都是对象，变量则是对这些对象的引用。</span>

<b>强类型</b>：
指python变量一旦被赋值，类型就确定了，除非进行强制转换，否则不会被当作其他类型使用

<h4>Python是拥有<span style="color: darkgreen; font-weight: 700;">“编译时间”</span>和<span style="color: darkgreen; font-weight: 700;">“运行时间”</span>两个阶段的解释型语言。</h4>
编译过程：
源代码(.py) -（Python解释器）-> 字节码(.pyc) -(Python虚拟机)-> 机器执行

- 在源代码（.py） -> 经过Python解释器翻译成 -> 字节码（.pyc）
    - 这个过程：解析源代码，将高级语言解析成低级语言（字节码）
    - 这个过程类似"编译"
- 将字节码（.pyc）-> 经过Python虚拟机（PVM），PVM是解释器，字节码被PVM逐行指令翻译执行

<span style="color: darkgreen; font-weight: 700;">Tip: 解释执行的过程</span>
<div style="background-color: #96ffcf; margin-top: -10px; padding: 10px; font-size: 14px; color: darkgreen; border: 1px solid darkgreen;">PVM并不直接与硬件进行交互，而是通过调用操作系统提供的API接口，以操作系统为中介，最终达到间接与硬件交互的结果。实际调动硬件的是操作系统</div>

### .pyc文件的详情
<b>优化加载时间</b>
- 将Python源码转换为字节码是一个耗时的过程，  为了优化多次执行同一个程序的时间，Python会在第一次执行.py文件的时候，将生成的字节码缓存到.pyc文件中。这样，下次执行该程序时，如果源代码没有更改，Python文件可以直接加载.pyc文件，跳过编译步骤，从而更快地开始执行。

<b>存储位置 </b>
- 在Python3.2之前，`.pyc`文件与其对应的`.py`文件存放在同一目录下。
- 从Python3.2开始，`.pyc`文件存放在`__pychache__`目录下，并带有解释器版本信息，这样不同版本的解释器可以并存，并不会相互干扰

<b>与平台无关</b>
- 只要不同系统上的Python解释器的版本相同，就可以跨平台运行.pyc文件

<b>.pyc是非加密文件</b>
- 存在工具可以反编译.pyc文件以恢复原始python源代码，如果需要保护，请选用其他方法，如：代码混淆

<b>运行时无需`.py`文件</b>
- 一旦`.pyc`文件被创建，即使删除或移动原始的`.py`文件，只要`.pyc`文件存在，程序仍可执行

<b style="color: darkgreen; font-weight: 700;">Python执行模式</b>
- 当Python运行一个模块时，首先检查是否存在与该文件对应的`.pyc`文件，且该文件是最新的。
    - 如果存在最新的`.pyc`文件，Python会加载这个字节码文件
    - 否则，Python会重新编译源文件，并保存新的`.pyc`文件

### Python的多个实现版本
- Cpython
    - python官方版本，使用C语言实现，使用最为广泛，CPython实现会将源代码转换为字节码文件，然后运行在虚拟机中。

- Jython
    - Python的java实现，Jython会将Python代码动态编译成java字节码，然后再JVM上运行。

- IronPython
    - Python的C#实现，IronPython将Python源码编译成C#字节码，然后再CLR上运行

- PyPY
    - Python实现的Python，将Python的字节码再编译成机器码

## 软件环境搭建(Windows)
### 安装Anaconda
Anaconda是一个用于科学计算的Python发行版
### 下载安装包
```shell
https://www.anaconda.com
```
```shell
# 安装后，运行anaconda prompt
# 创建虚拟环境，环境名称自定义，这里示例中使用mypython
conda create -n mypython python=3.12
# 安装成功后激活
conda activate mypython
# 下载使用jupyter
jupyter notebook
```
### 安装python

## Python注释
### 单行注释
```python
# This line is a comment.
print("This line is not a comment, it is code.")
```

### 多行注释
使用三个单引号`'''`或者三个双引号`"""`
```python
'''This 
is 
a 
multiple
line 
comments'''
print("This line is not a comment, it is code.")
```

```python
"""This 
is 
a 
multiple
line 
comments"""
print("This line is not a comment, it is code.")
```

## Python变量
### 变量特性
变量共有三个特性
- id: 变量值的内存空间地址。内存地址不同，id就不相同。可以使用id()来查看变量的内存地址。
- type: 不同类型的值记录事物的状态有所不同，这就是Python的数据类型。可以使用type()来查看。
- 变量值: 就是存储值本身

```python
a = 5
print(id(a)) # 140704840825400
print(type(a)) # <class 'int'>
print(a) # 5
```
<h4 style="color:red">!! Python中一切皆对象(Everything is Object) !!</h4>

<div style="background-color: #96ffcf; margin-top: -10px; padding: 10px; font-size: 14px; color: darkgreen; border: 1px solid darkgreen;">Python 采用了“一切皆对象”的设计哲学，这意味着无论是简单的数据类型（如整数、字符串）还是复杂的数据结构（如列表、字典、函数等），都是以对象的形式存在的。因此，这些对象都具有以下特点：
<br><br>
<b>类型信息：</b>对象知道它是什么类型的，比如 int、str、list 等。
身份：每个对象都有一个唯一的标识符（可以通过 id() 函数获得），用于区分不同的对象。<br><br>
<b>值：</b>对象包含的数据值。<br><br>
<b>方法和属性：</b>与对象类型相关的操作和信息。例如，整数对象具有一些方法，如 bit_length()，用于返回整数所需的位数。</div>


## 输入输出
### 输出函数print()
```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```
- <b style="color: darkgreen">sep参数：</b>默认为空格，可以指定字符串之间的分隔符
```python
a = 'apple'
b = 'banana'
c = 'cherry'
print(a, b, c, sep='-') # apple-banana-cherry
```

- <b style="color: darkgreen">end参数：</b>默认为换行符，指定末尾添加的字符
- <b style="color: darkgreen">flush参数：</b>
    - 作用：默认情况下，flush 设置为 False，这意味着输出可能会在缓冲区中积累，直到缓冲区被填满或程序结束时才实际写入到文件或终端。当 flush 设置为 True 时，print 函数将确保所有输出都被立即强制写出，不经过缓冲区直接输出。
    - 用法：flush 参数通常在需要即时看到输出时使用，例如在实时日志记录或更新用户界面时。
```python
import time

# 使用 flush=True 确保输出立即显示
for i in range(10):
    print('.', end=' ', flush=True)
    time.sleep(0.5)  # 模拟耗时操作
```

- <b style="color: darkgreen">file参数：</b>将输出重定向到文件
```python
# 将输出重定向到文件
with open('output.txt', 'w') as f:
    print('Hello, world!', file=f)
```

### 输入函数input()
```python
input(prompt)
```
- If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:

- For Example:
```python
s = input('--> ')  
>>> --> Monty Python's Flying Circus
s  
>>>"Monty Python's Flying Circus"
```

## 字符串类型
### 字符串的特点
<b>1. 字符串可视为字符数组：</b>但在Python中，虽然可以像操作数组那样使用索引访问字符串中的字符，字符串其实是更高级的数据结构，提供了大量的方法和操作。

<b>2. 字符串不可更改(immutable): </b>这是一个非常重要的特性，一旦创建了字符串，就不能更改它。如果试图更改某个位置的字符串，Python会报错。但可以通过组合、切片等操作创建新的字符串。

<b>3. 支持Unicode字符：</b>Python 3默认支持Unicode，这意味着可以在字符串中使用几乎任何语言的字符，甚至是表情符号。这使Python在处理多种语言和字符集时非常强大。

<b>4. 字符串是有序的：</b>字符串中的字符按照它们被添加到字符串中的顺序进行存储。因此，"hello"和"olleh"是两个完全不同的字符串。

<b>5. 通过索引访问：</b>可以使用索引访问字符串中的各个字符，其中0是第一个字符的索引，1是第二个字符的索引，依此类推。你还可以使用负数索引从字符串的末尾开始访问字符。
```python
s = "hello"
print(s[0])  # 输出: h
print(s[-1])  # 输出: o
```

### 创建字符串
<div style='font-size: 20px'>单引号和双引号</div>
<div style='font-size: 15px'>字符串包含单引号或双引号。</div>

```python
my_string = "This is a double-quoted string."
print(my_string) # This is a double-quoted string.
print(type(my_string)) # <class 'str'>
```
```python
my_string = 'This is a single-quoted string.'
print(my_string) # This is a single-quoted string.
print(type(my_string)) # <class 'str'>
```
```python
s1 = "This is a long string that \
      spans multiple lines in the source code."

s2 = "This is a long string that spans multiple lines in the source code."
# s1和s2代码等效，\的作用是告诉 Python 解释器忽略字符串的实际换行。
```

<div style='font-size: 20px'>多行字符串</div>
<div style='font-size: 15px'>如果需要创建一个多行字符串，可以使用三重引号。</div>

```python
multiline_string = '''This is a string where I 
can comfortably write on multiple lines
without worrying about to use the escape character "\\" as in
the previous example. 
As you'll see, the original string formatting is preserved.
'''

print(multiline_string)
```

<div style='font-size: 20px'>str()构造函数</div>
<div style='font-size: 15px'>可以使用str()的类型构造函数将Python中的几乎所有对象转换为字符串</div>

```python
S = str(35)
print(S) # '35'

dic = {'a': 1, 'b': 2}
str_dic = str(dic)
print(str_dic)  # 输出: "{'a': 1, 'b': 2}"
```

### 字符串操作
<div style='font-size: 20px'>使用索引访问字符串中的字符</div>
<div style='font-size: 15px'>方括号可用于访问字符串中的元素</div>


```python
# Indexing
S = 'ABCDEFGHI'
print(S[0])     # A
print(S[4])     # E
print(S[-1])    # I
print(S[-6])    # D
```
<hr>

<div style='font-size: 20px'>切片 (Slicing)</div>
<div style='font-size: 15px'>可以使用slice语法返回一定范围的字符。
指定开始索引和结束索引，以冒号分隔，以返回字符串的一部分。</div>

```python
b = "Hello, World!"
print(b[2:5]) #llo
```
<div style="background-color: #96ffcf; margin-top: -10px; padding: 10px; font-size: 14px; color: darkgreen; border: 1px solid darkgreen;">在Python中使用切片时，开始索引是包含的（inclusive），而结束索引是不包含的（exclusive）。</div>

该设计的合理的处：

1. 当两个相邻的切片相连时，它们之间没有重叠，例如s[:2]和s[2:]会恰好将字符串分为两部分。
2. 当使用范围来计算切片长度时，如s[i:j]，长度是j-i
3. 为字符串或列表等数据结构设置一个默认结束索引时，可以轻松地获取其余所有元素，例如s[2:]从索引2开始，直到字符串的末尾。

<hr>

<div style='font-size: 20px'>负索引 (Negative Indexing)</div>
<div style='font-size: 15px'>使用负索引从字符串末尾开始切片：</div>

```python
b = "Hello, World!"
print(b[-1])  # '!'
print(b[-5:-2])
```

<hr>

<div style='font-size: 20px'>字符串长度 (String Length)</div>
<div style='font-size: 15px'>要获取字符串的长度，请使用len()函数。</div>

```python
a = "Hello, World!"
print(len(a)) # 13
```

### 字符串常用方法

<div style='font-size: 20px'>改变大小写</div>

```python
S = 'Hello, World!'
print(S.lower())       # hello, world!
S = 'Hello, World!'
print(S.upper())       # HELLO, WORLD!
S = 'Hello, World!'
print(S.capitalize())  # Hello, world! 只有第一个单词首字母大写
S = 'Hello, World!'
print(S.swapcase())    # hELLO, wORLD! 大小写反转
S = 'hello, world!'
print(S.title())       # Hello, World! 每个单词首字母都大写
```

<div style="background-color: #96ffcf; margin-top: -10px; padding: 10px; font-size: 14px; color: darkgreen; border: 1px solid darkgreen;">这些方法都不会修改原始字符串，而是返回一个新的修改过的字符串。这是因为在 Python 中，字符串是不可变的。</div>

<hr>

<div style='font-size: 20px'>检查字符串 (Check String)</div>
<div style='font-size: 15px'>要检查字符串中是否存在特定短语或字符，可以使用`in`或`not in`关键字。</div>

```python
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) # True

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)  # False
```

<hr>

<div style='font-size: 20px'>字符串替换</div>
<div style='font-size: 15px'><b style="color: darkgreen">replace( )</b>方法将一个字符串替换为另一个字符串：</div>

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```

<hr>

<div style='font-size: 20px'>字符串分割</div>
<div style='font-size: 15px'><b style="color: darkgreen">split( )</b>方法在找到分隔符的实例时将字符串拆分为子字符串：</div>

```python
a = "Hello, World!"
print(a.split(","))  # ["Hello", "World"]
```

<hr>

<div style='font-size: 20px'>合并（拼接）字符串</div>

```python
# 使用"+"拼接
first_name = 'ada'
last_name = 'lee'

full_name = first_name + ' ' + last_name
print(full_name.title()) # Ada Lee
```

```python
parts = ['hello', 'world']
s = " ".join(parts) 
# str.join()：使用给定的字符串作为分隔符，连接列表中的字符串
print(s)  # 输出: hello world
```

<hr>

<div style='font-size: 20px'>遍历字符串</div>
<div style='font-size: 15px'>要遍历字符串的字符，可使用简单的for循环。</div>

```python
#Example: Print each character in a string

S = 'Hello, World!'
for letter in S:
    print(letter, end=' ')
# H e l l o ,   W o r l d ! 
```

<hr>

<div style='font-size: 20px'>去除空白字符</div>
<div style='font-size: 15px'>可以从字符串的左侧、右侧或两侧剥离空白。</div>

```python
name = ' eric '

print('-' + name.lstrip() + '-')  # -eric -
print('-' + name.rstrip() + '-')  # - eric-
print('-' + name.strip() + '-')   # -eric-
```

<hr>

<div style='font-size: 20px'>原始字符串 (Raw String )</div>
<div style='font-size: 15px'>如果不希望将\开头的字符解释为特殊字符(即不对其转义)，则可以通过在第一引号之前添加r来使用原始字符串。</div>

```python
#Example:

S = r'C:\new\text.txt'
print(S)
# C:\new\text.txt
```

### 字符串格式化
Python中几种常见的字符串格式化方法：
1. <b style="color: darkgreen">使用 % 运算符（老式的方式）:</b>

```python
# Use printf-style % string formatting
S = '%s is %d years old.' % ('Bob', 25)
print(S)

name = "Alice"
age = 28
print("My name is %s and I am %d years old." % (name, age))
# My name is Alice and I am 28 years old.
```

2. <b style="color: darkgreen">使用 str.format() 方法:</b>

```python
name = "Bob"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# Use format() Built-in Method
S = '{1} is {0} years old.'.format(25, 'Bob')
print(S)

string_template = 'The result of the calculation of {calc} is {res}'
print("String Template: ", string_template)

print(string_template.format(calc='(3*4)+2', res=(3*4)+2))
# String Template:  The result of the calculation of {calc} is {res}
# The result of the calculation of (3*4)+2 is 14
```

3. <b style="color: darkgreen">使用 f-string (Python 3.6及更高版本):</b>

```python
name = "Charlie"
age = 25
print(f"My name is {name} and I am {age} years old.")

calculation = '(3*4)+2'
result = (3*4)+2
string_template = f'The result of the calculation of {calculation} is {result}'
print("String Template: ", string_template)
# String Template:  The result of the calculation of (3*4)+2 is 14
```

4. <b style="color: darkgreen">使用模板字符串（string.Template 类）:</b>

```python
from string import Template
t = Template("My name is $name and I am $age years old.")
print(t.substitute(name="David", age=35))
```

### Python字符串的内部实现

1. <b style="color: darkgreen">结构： </b>Python中的字符串是由<mark>PyUnicodeObject</mark>结构体表示的。这个结构体包含了许多与字符串相关的信息，例如其长度、哈希值和实际数据的指针。

```C
// PyUnicodeObject 结构体
typedef struct {
    PyObject_HEAD
    Py_ssize_t length;        // 字符串的长度
    Py_hash_t hash;           // 字符串的哈希值
    wchar_t *str;             // 指向字符串数据的指针
    // 可能还有其他字段，取决于 Python 的版本和编译选项
} PyUnicodeObject;
```
- PyObject_HEAD 是一个宏，包含了引用计数和指向类型对象的指针。
- length 表示字符串的字符数。
- hash 存储字符串的哈希值，如果字符串尚未被哈希过，则为 -1。
- str 是一个指向宽字符数组的指针，该数组存储了字符串的实际数据。

举例：

```python
s = "hello"
```

```C
// （简化版）
PyUnicodeObject {
    PyObject_HEAD: {...},
    length: 5,
    hash: -1,  // 假设字符串尚未被哈希过
    str: 0x0042a3d4  // 假设的内存地址
}
// 在内存地址 0x0042a3d4 处，我们将找到一个宽字符数组，存储着字符串 "hello" 的 Unicode 编码。
```

- length 字段告诉我们字符串有 5 个字符。
- hash 字段的值是 -1，意味着字符串的哈希值还没有被计算。在 Python 中，字符串对象是不可变的，因此它们的哈希值只需计算一次，之后可以被缓存。当字符串第一次被用作字典的键时，其哈希值会被计算并存储在这里。
- str 字段指向实际存储字符串数据的内存位置。在这个例子中，它是一个指向 "hello" 的 Unicode 编码的宽字符数组的指针。

<b style="color: darkgreen">类型对象（PyTypeObject）</b>
每个 Python 对象在其结构的开头都有一个 PyObject_HEAD 宏，其中包含了一个指向其类型对象的指针。对于字符串对象（PyUnicodeObject），这个指向的是 Unicode 字符串类型的类型对象。

- 类型对象（PyTypeObject）定义了该类型的许多属性，包括：
    - 类型名称
    - 类型大小
    - 类型的方法表，包含该类型所有可用的方法和函数
    - 基本类型操作（如分配、释放等）
    - 类型的属性（字段）、方法和其他特性的描述

<b style="color: darkgreen">方法表</b>
类型对象中的方法表列出了该类型支持的所有方法。这个表是一系列函数指针的集合，每个指针对应一个 Python 层面可调用的方法。当你调用一个字符串的方法时，比如 s.upper()，Python 解释器会查找字符串类型的类型对象，找到 upper 方法对应的函数指针，并执行它。

<hr>

2. <b style="color: darkgreen">存储： </b>Python的字符串是以不同的编码格式存储的。对于只包含ASCII字符的字符串，它们可能仅使用1个字节来存储每个字符。但是，对于包含非ASCII字符的字符串，例如Unicode字符，Python可能会使用2到4个字节来存储每个字符，具体取决于字符的范围。

<hr>

3. <b style="color: darkgreen">不可变性： </b>字符串在Python中是不可变的。这意味着当你创建一个字符串时，你不能更改它。这种不可变性提供了几个优势：

    - 字符串可以被安全地用作字典的键。
    - 多个变量可以引用同一个字符串对象，从而节省内存。
    - 不可变性使得某些操作（例如切片）非常快速，因为它们不需要创建新的字符串对象，只需要提供新的视图或引用到现有的字符串上。

<hr>

4. <b style="color: darkgreen">内部哈希： </b>由于字符串是不可变的，所以它们的哈希值可以在创建时计算并缓存起来。当字符串被用作字典的键时，这可以加速查找。

<hr>

5. <b style="color: darkgreen">字符串驻留： </b>为了提高效率和内存使用，Python使用了一个技术叫做字符串驻留。这意味着对于短的、常用的字符串，Python可能会保留一个单一的、固定的内部引用，而不是为每个新的同样的字符串实例创建一个新的对象。这主要是通过sys.intern()实现的。

<hr>

6. <b style="color: darkgreen">字符串方法： </b>Python的字符串提供了大量的内置方法，如split(), replace(), upper(), find()等，这些方法都是在底层C代码中实现的，所以它们的执行速度非常快。

总之，虽然在高层次上，Python的字符串可以被视为字符数组，但在底层，它们是高度优化且功能丰富的对象。这种设计使Python的字符串操作既强大又高效。

## 布尔类型

布尔值表示两个值之一：True或False。

Python中的布尔值是布尔数据类型的实例，首字母大写（True和False），而不是小写（不是true和false）。

### 评估值和变量 (Evaluate Values and Variables )

`bool()`函数可评估任何值，并返回`True`或`False`

```python
print(bool("Hello"))
print(bool(15))
```

### False和True
在Python中，以下值在经过bool()函数评估时被视为`False`：
1. None
2. False (布尔False本身)
3. 任何数值类型的零（0, 0.0, 0j等）
4. 空的数据结构，如""（空字符串）、[]（空列表）和{}（空字典）
5. 其他表示"空值"或"无效"的情况，如set()（空集合）

除上述值外，几乎所有其他的值都会被评估为`True`。

### Python布尔类型的内部实现
在Python中，布尔（Boolean）类型是int（整数）的一个子类，而布尔值True和False分别等同于整数值1和0。因此，布尔值可以参与算数运算并表现得像其整数等价物。
1. <b style="color: darkgreen">子类化：</b>在Python的源代码中，布尔类型是这样定义的：
```C
PyTypeObject PyBool_Type = {
    ...
    "bool",                   /* tp_name */
    sizeof(PyIntObject),      /* tp_basicsize */
    ...
}
// 这里，PyBool_Type继承自PyInt_Type，这意味着在C语言级别，布尔类型是整数类型的子类。
```
2. <b style="color: darkgreen">单例实现：</b>为了效率和内存使用，Python中只有两个布尔对象：True和False。这两个对象在Python启动时就被创建，并在整个Python进程生命周期中被复用。

3. <b style="color: darkgreen">整数等价：</b>因为布尔类型是整数的子类，True和False的整数值分别是1和0。这也意味着你可以进行诸如True + 2这样的操作，结果是3。

4. <b style="color: darkgreen">布尔运算：</b>Python提供了基于整数运算的布尔运算符，如and、or和not。这些运算符在内部使用整数运算，但返回的仍然是布尔对象。

5. <b style="color: darkgreen">从其他类型到布尔的转换：</b>内建的bool()函数可以将其他类型的值转换为布尔值。这在内部通常是通过检查对象的真实性（truthiness）来实现的。例如，空的集合、空的字符串、数值0等都被视为“假”（False），而非空值或非零值被视为“真”（True）。

6. <b style="color: darkgreen">存储：</b>虽然布尔值在很多方面都像整数，但由于其单例性，它们实际上占用的内存可能比普通的整数小。

## 运算符
- 算数运算符 （略）

- 比较运算符 （略）

- 逻辑运算符
    - `and`： 逻辑与
    - `or`: 逻辑或
    - `not`: 逻辑非

- 位运算符 （略）

- 赋值运算符 （略）

- 成员运算符
    - `in`: 如果在指定的序列中找到值返回 True，否则返回 False
    - `not in` : 如果在指定的序列中没有找到值返回 True，否则返回 False

- 身份运算符
    - `is`: 如果两个变量指向同一对象则条件成立
    - `is not`: 如果两个变量不指向同一个对象则条件成立

## 流程控制
### 分支语句
<b style="font-size: 20px; color: darkgreen;">if 语句</b>
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

### 循环语句
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
### 扩展1：字典遍历
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

### 扩展2：for循环实现推导式
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

## 组合数据类型 - 容器
Python中的容器类型用于存储多个项。

<div style='font-size: 20px; font-weight: 700'>容器和序列的联系和区别</div>

<div style='font-size: 18px; margin-top: 5px; margin-bottom: 5px;'>容器 (Containers)</div>
<p style="font-size: 13px">容器是一个广泛的概念，指的是可以包含一个或多个元素的对象。这些元素可以是任何类型的数据。</p>

<b>特点:</b>

- 可以测试成员资格，即可以检查某个元素是否包含在容器中（使用 in 和 not in 操作符）。

<b>常见的容器包括:</b>

- 列表 (list)
- 元组 (tuple)
- 字典 (dict)
- 集合 (set)
- 字符串 (str)
- 其他更多...
<div style='font-size: 18px; margin-top: 5px; margin-bottom: 5px'>序列 (Sequences)</div>
<p style="font-size: 13px">序列是容器的子集，具有以下附加特性。</p>

<b>特点:</b>

- 元素有序排列。
- 可以通过索引访问元素。
- 可以进行切片操作，取序列的一部分。
- 支持迭代。
- 有一个确定的长度（可以使用 len() 函数来获取）。

<b>常见的序列类型包括:</b>

- 列表 (list)
- 元组 (tuple)
- 字符串 (str)
- 字节 (bytes)
- 字节数组 (bytearray)
<div style='font-size: 18px; margin-top: 5px; margin-bottom: 5px'>关联和区别:</div>

<b>关联:</b>

- 所有序列都是容器，但并非所有容器都是序列。

<b>区别:</b>

- 容器的主要特点是成员资格测试，而序列增加了顺序、索引、切片和长度的概念。
- 不是所有的容器都支持索引和切片操作。例如，集合 (set) 和字典 (dict, 在键上) 就不支持索引和切片。
- 序列的元素是有序的，而某些容器（如集合）是无序的。

了解容器和序列的区别及其之间的关系可以帮助Python开发者更加有效地使用这些数据结构。

### 列表
<div style='font-size: 20px; margin-top: 5px; margin-bottom: 5px'>列表的创建 (2种)</div>

```python
# 方法1：
fruits = ['apple', 'banana', 'cherry']

# 方法2：使用构造函数
list1 = list('abc') # 输出：['a', 'b', 'c']
list2 = list((boy, girl)) # 元组->列表
```

<div style='font-size: 20px; margin-top: 5px; margin-bottom: 5px'>遍历列表 </div>

```python
fruits = ['apple', 'banana', 'cherry']

# enumerate()函数
print("Results for the fruit show are as follows:\n")
for index, fruit in enumerate(fruits):
    place = str(index)
    print("Place: " + place + " Fruit: " + fruit.title())
```
`enumerate()`函数是Python的内置函数，用于在迭代一个序列时获取元素及其对应的索引。
默认情况下，`enumerate()`从0开始计数，但如果想从其他数字开始，可以提供一个可选的`start`参数。例如，`enumerate(fruits, start=1)`将从1开始计数。

### Python中List的内部实现
详情见jupyter文档

<div style="background-color: #96ffcf; margin-top: -10px; padding: 10px; font-size: 14px; color: darkgreen; border: 1px solid darkgreen;">总的来说，Python的list是一个高度优化的、动态的、连续的内存块，存储指向对象的指针。其内部实现是为了在多种常见用途下都能提供良好的性能。</div>