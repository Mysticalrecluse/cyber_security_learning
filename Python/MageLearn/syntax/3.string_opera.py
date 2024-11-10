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
print(a.startswith("e", 1)) # True, 是否从索引1开始以e开头
print(a.endswith("World")) # True, 是否以World结尾
print(a.isidentifier()) # False, 是否是一个合法的标识符

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

# 去除空白字符，不单单是空格，还包括换行符，制表符等
name = ' eric '
name2 = '\r\n\t eric \r\n\t '
name3 = 'abcda'
print(name.strip()) # eric  去除两边空格
print(name2.strip("\r\t ")) # \n\t eric \n  去除指定字符
print(name3.strip("a")) # bcd  去除指定字符
print(name3.strip("bda")) # c
print(name.lstrip()) # eric  去除左边空格
print(name.rstrip()) #  eric 去除右边空格

# string.find()方法，返回子串的索引，如果没有找到返回-1
# S.find(sub[, start[, end]]) -> int
# 默认从头开始查找，可以指定开始和结束位置
a = "Hello, World"
print(a.find("World")) # 7
print(a.find('l', 3, 8)) # 3

# string.rfind()方法，返回子串的索引，如果没有找到返回-1
# rfind()方法从右边开始查找
print(a.rfind('l')) # 10

# string.index()方法，返回子串的索引，如果没有找到会抛出异常
# S.index(sub[, start[, end]]) -> int
# index()和find()方法类似，但是如果没有找到会抛出异常
print(a.index('World')) # 7

# string.rindex()方法，返回子串的索引，如果没有找到会抛出异常
# rindex()方法从右边开始查找
print(a.rindex('l')) # 10

# string.count()方法，返回子串出现的次数
# S.count(sub[, start[, end]]) -> int
print(a.count('l')) # 3

# ''.join()方法，将可迭代对象中的元素以指定的字符连接生成一个新的字符串
# str.join(iterable) -> str
print(",".join('abc')) # a,b,c
print(",".join(map(str, range(5))))
print(",".join(['1','2','3'])) # 1,2,3 ; join()方法只能连接字符串，如果是数字需要先转换为字符串

# map()函数，将一个函数作用于一个可迭代对象的所有元素
# map(function, iterable, ...) -> map object
# 返回一个迭代器
a = map(str, range(5))
print(list(a)) # ['0', '1', '2', '3', '4']

b = map(int, ['1', '2', '3'])
print(list(b)) # [1, 2, 3]


# string.split()方法，将字符串分割成一个列表
# S.split(sep=None, maxsplit=-1) -> list of strings
# 默认以空格分割，可以指定分隔符
# split()方法返回一个列表
a = "Hello, World"
print(a.split()) # ['Hello,', 'World']
print(",".join('abc').split("b")) # ['a,', ',c']

# string.rsplit()方法，从右边开始分割
# rsplit()方法从右边开始分割
b = 'a,b,c'
print(b.rsplit(",", 1)) # ['a,b', 'c']
print(r"c:\windows\system32".rsplit("\\", 1)) # ['c:\\windows', 'system32']

print("a\nb\r\nd".split()) # ['a', 'b', 'd'] 默认以空白字符，尽可能长的进行分割

# string.slitlines()方法，将字符串分割成一个列表,默认按“\n”,"\r","\r\n"分割
# S.splitlines([keepends]) -> list of strings
# 默认不保留换行符
a = "Hello\nWorld\r\nPython"
print(a.splitlines()) # ['Hello', 'World', 'Python']

# string.partition()方法，将字符串分割成三部分
# S.partition(sep) -> tuple
# 返回一个元组,第一个元素是sep之前的部分，第二个元素是sep，第三个元素是sep之后的部分
a = "Hello, World"
print(a.partition(',')) # ('Hello', ',', ' World')

# string.rpartition()方法，从右边开始分割
# rpartition()方法从右边开始分割
a = "a, b, c"
print(a.rpartition(',')) # ('a, b',',',' c')

# string.replace()方法，替换字符串中的子串
# S.replace(old, new[, count]) -> str
# count是替换的次数
a = "Hello, World"
print(a.replace("World", "Python")) # Hello, Python

b = "a, b, c"
print(b.replace(", ", ":", 1)) # a:b, c