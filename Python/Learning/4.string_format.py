#字符串格式化
# 1. %运算符
# 2. format()方法
# 3. f-string
# 4. 模板字符串(string.Template)

# 1. %运算符
name = "tom"
age = 18
print("My name is %s, I'm %d years old" % (name, age))
# My name is tom, I'm 18 years old

# 2. format()方法
name = "tom"
age = 18
print("My name is {}, I'm {} years old".format(name, age))
# My name is tom, I'm 18 years old
print("My name is {1}, I'm {0} years old".format(age, name)) # 通过索引指定参数
# My name is tom, I'm 18 years old

# 3. f-string, Python 3.6+版本
name = "tom"
age = 18
print(f"My name is {name}, I'm {age} years old")

# 4. 模板字符串(string.Template) 用的比较少
from string import Template
t = Template("My name is $name, I'm $age years old")
s = t.substitute(name="tom", age=18)
print(s) # My name is tom, I'm 18 years old