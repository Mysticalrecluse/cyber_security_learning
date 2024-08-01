'''
for var in iterable:
    statement
    statement
else:
    statement
'''

# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) # apple \nbanana \ncherry

# pass语句
# for循环不能为空，但是如果你想保留一个空的for循环，可以使用pass语句。
for x in [0, 1, 2]:
    pass
# pass语句不执行任何操作，只是一个空操作。它通常用于保持代码结构的完整性。
# 以下是一些使用pass的情况
# 1. 空函数或方法的定义
def my_function():
    pass
# 2. 空类的定义
class MyClass:
    pass

# 3. 占位的循环或条件语句
'''
for item in some_list:
    if condition(item):
        pass
    else:
        process(item)
'''

# 4. 保持代码结构的完整性