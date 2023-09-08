# 基础语法
## 数据类型
### 数字类型
- 数字类型的种类
  - 整数
  - 浮点数
  - 复数
- 组成
  - 数字是由数字自字面值或内置函数与运算符的结果创建的
  - 常见数字函数
  <table>
    <thead>
        <th style="background-color:darkred;color:white">函数</th>
        <th style="background-color:darkred;color:white">描述</th>
    </thead>
    <tbody>
        <tr>
            <td>abs(x)</td>
            <td>x的绝对值或大小</td>
        </tr>
        <tr>
            <td>int(x)</td>
            <td>将x转换为整数</td>
        </tr>
        <tr>
            <td>float(x)</td>
            <td>将x转换为浮点数</td>
        </tr>
        <tr>
            <td>complex(re,im)</td>
            <td>一个带有实部re和虚部im的复数，im默认为0</td>
        </tr>
        <tr>
            <td>c.conjugate()</td>
            <td>复数c的共轭</td>
        </tr>
        <tr>
            <td>divmod(x,y)</td>
            <td>(x // y, x % y)</td>
        </tr>
        <tr>
            <td>pow(x,y)</td>
            <td>x的y次幂</td>
        </tr>
        <tr>
            <td>x ** y</td>
            <td>x的y次幂</td>
        </tr>
    </tbody>
  </table>

- 数字与字符串的类型转换
  - Python是强类型编程语言
  - 使用type()函数可以得知对象的类型
  - int(),float()函数可以进行数字类型之间的转换
  - str()函数能够将数字转换为字符串
  - int()函数可以将只含有整数的字符串转换为整数，否则报错kv
### 字符串类型
- 使用形式
  - ' '单引号 ；可以在单引号中，输出双引号（不支持换行）
  - " "双引号 ；也可以在双引号中，输出单引号（同样不支持换行）
  - ''' ''' 三引号 ； 更适用于多行文本输出（支持换行以及单引号和双引号）;同时也用作多行注释

- 字符串中嵌入变量
  - 占位符%s（通用），%d（整数），%f（浮点数，默认小数点后6位）
    - 特殊：%(可填字符) 6d表示6为整数，不足6位，默认空格
    - 特殊：可填字符中，-表示空格在后，默认在前，0可以在整型和浮点型使用，字符串不能加，用途是补0
    ```python
    print("我叫%s"%"张艺峰")
    print("我今年%d岁，我爸爸%d岁"%(12,48)) #老用法
    ```

  - 占位符{}{}.format()
  ```python
  print("我今年{}岁，我爸爸{}岁".format(12,48))

  x = 12
  y = 48
  print("我今年{}岁，我爸爸{}岁".format(x,y))
  # 控制位数

  print('我今年{:3d}岁，我爸爸{:.2f}岁'.format(12,48))
  # :3d表示一共有3位整数，不足补空格
  # :.2f 表示小数点后两位
  ```

  - f-strings用法 （在python3.6以上版本实现）
  ```python
  x = 123
  print(f"x的变量是{x}")
  print(f"x的变量是{x:.2f}") 
  # 比较新的用法,{x:.2f}可以通过：.+nf控制浮点数在位数为n
  ```

- 字符串的基本操作
  - 成员运算
    - x in s 正确返回True，错误返回False
    - x not in s
  - 连接运算
    - s + t（左右两个字符串进行连接）
    - s * t（将左边的字符串，重复右边t次）
  - 字符串切片操作
    - s[i],取s的第i像，起始为0
    - s[i:j] s从i到j的切片
    - s[i:j:k]  s从i到j步长为k的切片
    - s[-i] 取倒数第i项的值，倒数起始为1
  - 字符串常用方法
  ```python
  判断系列

  str.isalnum()
  # 如果字符串中的所有字符都是字母或者数字，且至少有一个字符，
  # 那么返回True，否则返回False
  # 用途：比如判断邮箱或者用户名的输入是否合法
  =========================================================
  str.isalpha()
  # 如果字符串中的所有字符都是字母，那么返回True，否则返回False
  =========================================================
  str.isdigit()
  # 如果字符串中的所有字符都是数字，那么返回True，否则返回False
  =========================================================
  str.startswith()
  # 三个参数，分别是profix，给定前缀；start, end, 指定字符串区间
  # 三个参数之间用逗号隔开

  示例1：基础用法
  text = "Hello, world!"
  result = text.startswith("Hello")
  print(result)  # 输出 True，因为字符串确实是以 "Hello" 开始的。

  result = text.startswith("world")
  print(result)  # 输出 False，因为字符串并不是以 "world" 开始的。

  示例2：使用元组检查多个前缀
  text = "Hello, world!"
  result = text.startswith(("Hello", "Hi", "Hey"))
  print(result)  # 输出 True，因为字符串是以 "Hello" 开始的，而 "Hello" 是元组中的一个元素。

  示例3：
  text = "Hello, world!"
  result = text.startswith("world", 7, 12)
  print(result)  # 输出 True，因为从索引 7 到 12 的子字符串确实是以 "world" 开始的。
  ============================================================
  str.islower()
  # 对字符串是否都是小写进行判定
  ============================================================
  str.isupper()
  # 对字符串是否都是大写进行判定
  ============================================================
  str.istitle()
  # 对字符串是否是首字母大写，后面小写进行判定

  返回值系列

  str.join(iterable)
  # 作用：返回一个由iterable中的字符串，拼接而成的字符串
  
  示例：
  x = "helloworldisgood"
  y = ",".join(x) # 用逗号连接字符串
  print(y)
  ============================================================
  str.split(sep=None,maxsplit=-1)
  # 作用：返回一个由字符串单词组成的列表，使用sep分割字符串

  示例：
  x = "helloworldisgood"
  y = ",".join(x) # 用逗号连接字符串
  print(y)
  list1 = y.split(",") # 用逗号分割字符串
  print(list1)
  list2 = y.split(",", 3)
  print(list2) # ['h', 'e', 'l', 'l,o,w,o,r,l,d,i,s,g,o,o,d'] 
  # 用逗号分割字符串，分割3次

  拓展：
  str.rsplit(sep=None,maxsplit=-1)
  # 和str.split一样，区别是maxsplit的值是从右边开始分割

  示例：
  x = "31415926"
  y = ",".join(x)
  print(y.rsplit(",",3)) # ['3,1,4,1,5', '9', '2', '6']
  ============================================================
  str.lstrip([chars])
  # 作用：返回原字符串的副本，移除其中的前导字符；chars参数为指定要移除的字符
  # 注意：chars参数并非指定单个前缀，而是移除原字符串中的所有参数值

  示例：
  x = "www.example.com"
  print(x.lstrip("w.exampl")) # com
  print(x) # www.example.com

  ============================================================
  str.replace(old,new,count)
  作用：返回字符串副本，将其中所有子字符串old替换为new，替换前count次

  示例：
  x = "www.example.com"
  print(x.replace(".","-",1)) # www-example.com
  =============================================================
  str.lower()
  # 将字符串转化为小写

  str.upper()
  # 将字符串转化为大写

  str.title()
  # 将字符串转化为首字母大写

  str.capitalize()
  # 将字符串转换为首字符大写
  ===============================================================
  ```
### 列表
### 字典
### 元组
### 集合 