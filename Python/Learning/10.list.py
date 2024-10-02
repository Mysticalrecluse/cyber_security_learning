# 列表
students = ['ben', 'tom', 'jerry', 'mike']
for student in students:
    print("Hello, " + student.title() + "!")

# 命名和定义一个列表
# 一个列表是一个有序的集合，可以包含任意数量的元素。
# 列表中的元素可以是任何数据类型，甚至是不同的数据类型。

# 可以使用python的list()构造函数创建一个列表，或者使用方括号[]定义一个列表。
# 示例：将字符串转换为单字符字符串的列表
L = list("hello")
print(L) # ['h', 'e', 'l', 'l', 'o']

# 示例：将元组转换为列表
T = (1, 2, 3)
L = list(T)
print(L) # [1, 2, 3]