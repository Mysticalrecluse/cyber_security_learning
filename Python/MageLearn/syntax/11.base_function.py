# 强制类型转换
# int() # 将一个数值或字符串转换为整数
# float() # 将一个字符串转换为浮点数
# str() # 将指定的值转换为字符串
from xmlrpc.client import boolean

# 1. str() 构造函数，将其他类型转换为字符串


# input()函数
# input()函数接受一个标准输入数据，返回为string类型

# isinstance()函数
# isinstance()函数可以用来检查一个对象是否是一个特定的数据类型

print(isinstance(False, int))  # True

print(isinstance(False, (str, int, bool)))  # True

# print()函数
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# sep=' ' 用来分隔多个值，默认是空格
# end='\n' 用来在输出值的结尾添加一个换行符
# file=sys.stdout 指定输出的文件，默认是标准输出
# flush=False 是否立即将输出刷新到文件，默认是False