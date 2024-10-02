# 字符串长度len()
a = "Hello, World"
print(len(a)) # 12

# 改变大小写
a = "Hello, World"
print(a.upper()) # HELLO, WORLD
print(a.lower()) # hello, world
print(a.title()) # Hello, World, 每个单词首字母大写
print(a.capitalize()) # Hello, world
print(a.swapcase()) # hELLO, wORLD, 大小写反转

# 注意：这些方法不会改变原字符串，而是返回一个新的字符串

# 检查字符串(Check Sring)
a = "Hello, World"
print(a.isalpha()) # False, 是否全是字母
print(a.isdigit()) # False, 是否全是数字
print(a.isspace()) # False, 是否全是空格
print(a.islower()) # False, 是否全是小写
print(a.isupper()) # False, 是否全是大写
print(a.istitle()) # True, 是否是标题化的
print(a.startswith("Hello")) # True, 是否以Hello开头
print(a.endswith("World")) # True, 是否以World结尾

b = "hello" in a
print(b) # True, 是否包含hello
b = "hello" not in a
print(b) # False, 是否不包含hello

# 字符串替换
a = "Hello, World"
b = a.replace("World", "Python")
print(b) # Hello, Python

# 字符串拼接
first_name = "Hello"
last_name = "World"
full_name = first_name + " " + last_name
print(full_name) # Hello World

parts = ["Hello", "World"]
full_name = " ".join(parts) # str.join(iterable) -> str 将可迭代对象中的元素以指定的字符连接生成一个新的字符串
print(full_name) # Hello World

# 遍历字符串
a = "Hello, World"
for i in a:
    print(i, end=" ")
# H e l l o ,   W o r l d

# 去除空白字符
name = ' eric '
print(name.strip()) # eric  去除两边空格
print(name.lstrip()) # eric  去除左边空格
print(name.rstrip()) #  eric 去除右边空格
