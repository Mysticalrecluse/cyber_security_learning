#字符串格式化
# 1. %运算符
# 2. format()方法
# 3. f-string
# 4. r"" 原始字符串
# 5. 模板字符串(string.Template)

# 1. %运算符
name = "tom"
age = 18
print("My name is %s, I'm %d years old" % (name, age))
# My name is tom, I'm 18 years old

# 格式化字符串，可以通过字典传递参数
print("My name is %(name)s, I'm %(age)d years old" % {'name':'tom', 'age':20})

# 2. format()方法
name = "tom"
age = 18
print("My name is {}, I'm {} years old".format(name, age))
# My name is tom, I'm 18 years old
print("My name is {1}, I'm {0} years old".format(age, name)) # 通过索引指定参数
# My name is tom, I'm 18 years old
print("{} {} {} {a} {b}".format(1, 2, 3, a=100, b=200))
print("{} +++ {}".format(*(1,22))) # 参数解包

#面向对象，通过对象的属性访问
class A:
    def __init__(self):
        self.x = 5
        self.y = 7

a = A()
print("{} {}".format(a.x, a.y))

# format()方法的高级用法
# 1. 对齐，填充
print("{:>10}".format("hello")) #       hello，右对齐，总长度为10
print("{:<10}".format("hello")) # hello      左对齐，总长度为10

# 2. 精度
print("{:.2f}".format(3.1415926)) # 3.14

# 3. 对时间处理，时间格式化
import datetime
d = datetime.datetime.now()
print("{}".format(d))
print("{:%y %Y}".format(d)) # 年
print("{:%m}".format(d)) # 月
print("{:%d %H %M %S}".format(d)) # 日 时 分 秒

# 进制
print("{0:b} {0:x} {0:X} {0:o}".format(10)) # 1010 a A 12

# 浮点数，宽度和精度，优先保证精度
print("{:5.2f}".format(1.3234)) # 1.32

# 3. f-string, Python 3.6+版本
name = "tom"
age = 18
print(f"My name is {name}, I'm {age} years old")

# 4. 模板字符串(string.Template) 用的比较少
from string import Template
t = Template("My name is $name, I'm $age years old")
s = t.substitute(name="tom", age=18)
print(s) # My name is tom, I'm 18 years old