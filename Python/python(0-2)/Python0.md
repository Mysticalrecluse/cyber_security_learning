<style> 
.tip {
    background-color: #EEEEEE; 
    margin-top: -10px; 
    padding: 10px;
    font-size: 15px;
}

.focus {
    color: tomato;
    font-weight: 700;
}

.greentip {
    background-color: #96ffcf; 
    margin-top: -10px; 
    padding: 10px;
    font-size: 14px;
    color: darkgreen;
    border: 1px solid darkgreen;
}
</style>
# Python入门
## Python介绍
<h4>Python是一门动态强类型语言</h4>
<b>动态</b>： 
指python在赋值的时候不需要指定变量类型，因为在python中，变量的本质是数据的指针（正确说法是对对象的引用）<span class="focus">在 Python 中，所有的数据都是对象，变量则是对这些对象的引用。</span>

<b>强类型</b>：
指python变量一旦被赋值，类型就确定了，除非进行强制转换，否则不会被当作其他类型使用

<h4>Python是拥有<span class="focus">“编译时间”</span>和<span class="focus">“运行时间”</span>两个阶段的解释型语言。</h4>
编译过程：
源代码(.py) -（Python解释器）-> 字节码(.pyc) -(Python虚拟机)-> 机器执行

- 在源代码（.py） -> 经过Python解释器翻译成 -> 字节码（.pyc）
    - 这个过程：解析源代码，将高级语言解析成低级语言（字节码）
    - 这个过程类似"编译"
- 将字节码（.pyc）-> 经过Python虚拟机（PVM），PVM是解释器，字节码被PVM逐行指令翻译执行

<span class="focus">Tip: 解释执行的过程</span>
<div class="greentip">PVM并不直接与硬件进行交互，而是通过调用操作系统提供的API接口，以操作系统为中介，最终达到间接与硬件交互的结果。实际调动硬件的是操作系统</div>

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

<b class="focus">Python执行模式</b>
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

<div class="greentip">Python 采用了“一切皆对象”的设计哲学，这意味着无论是简单的数据类型（如整数、字符串）还是复杂的数据结构（如列表、字典、函数等），都是以对象的形式存在的。因此，这些对象都具有以下特点：
<br><br>
<b>类型信息：</b>对象知道它是什么类型的，比如 int、str、list 等。
身份：每个对象都有一个唯一的标识符（可以通过 id() 函数获得），用于区分不同的对象。<br><br>
<b>值：</b>对象包含的数据值。<br><br>
<b>方法和属性：</b>与对象类型相关的操作和信息。例如，整数对象具有一些方法，如 bit_length()，用于返回整数所需的位数。</div>

## 字符串
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
<scan style='font-size: 20px'>单引号和双引号</scan>
<scan style='font-size: 15px'>字符串包含单引号或双引号。</scan>
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

<scan style='font-size: 20px'>多行字符串</scan>
<scan style='font-size: 15px'>如果需要创建一个多行字符串，可以使用三重引号。</scan>
```python
multiline_string = '''This is a string where I 
can comfortably write on multiple lines
without worrying about to use the escape character "\\" as in
the previous example. 
As you'll see, the original string formatting is preserved.
'''

print(multiline_string)
```

<scan style='font-size: 20px'>str()构造函数</scan>
<scan style='font-size: 15px'>可以使用str()的类型构造函数将Python中的几乎所有对象转换为字符串</scan>
```python
S = str(35)
print(S) # '35'

dic = {'a': 1, 'b': 2}
str_dic = str(dic)
print(str_dic)  # 输出: "{'a': 1, 'b': 2}"
```

### 字符串操作
<scan style='font-size: 20px'>使用索引访问字符串中的字符</scan>
<scan style='font-size: 15px'>方括号可用于访问字符串中的元素</scan>
```python
# Indexing
S = 'ABCDEFGHI'
print(S[0])     # A
print(S[4])     # E
print(S[-1])    # I
print(S[-6])    # D
```
<hr>

<scan style='font-size: 20px'>切片 (Slicing)</scan>
<scan style='font-size: 15px'>可以使用slice语法返回一定范围的字符。
指定开始索引和结束索引，以冒号分隔，以返回字符串的一部分。</scan>
```python
b = "Hello, World!"
print(b[2:5]) #llo
```
<div class='greentip'>在Python中使用切片时，开始索引是包含的（inclusive），而结束索引是不包含的（exclusive）。</div>
<br>
该设计的合理的处：

1. 当两个相邻的切片相连时，它们之间没有重叠，例如s[:2]和s[2:]会恰好将字符串分为两部分。
2. 当使用范围来计算切片长度时，如s[i:j]，长度是j-i
3. 为字符串或列表等数据结构设置一个默认结束索引时，可以轻松地获取其余所有元素，例如s[2:]从索引2开始，直到字符串的末尾。

<hr>

<scan style='font-size: 20px'>负索引 (Negative Indexing)</scan>
<scan style='font-size: 15px'>使用负索引从字符串末尾开始切片：</scan>
```python
b = "Hello, World!"
print(b[-1])  # '!'
print(b[-5:-2])
```
