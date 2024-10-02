# 变量的特性
# 1. id() 函数
# 2. type() 函数
# 3. 变量的赋值

# id() 函数
# id() 函数用于获取对象的内存地址
a = 10
print(id(a))  #140703271566040

# type() 函数
# type() 函数用于获取对象的类型
a = 5
print(type(a))  #<class 'int'>
x = True
print(type(x))  #<class 'bool'>

x = b"hello"
print(type(x)) #<class 'bytes'>

# 指定特定数据类型
x = int(20)
x = float(20)

# 变量是对象的引用
# 在python中，变量不直接存储值，而是存储值的内存地址，变量是对象的引用
a = 10
b = a
print(id(a))  #140703271566040
print(id(b))  #140703271566040
b = 3
print(id(b))  #140703271565976
# 可以看到，a和b的内存地址是一样的，当b重新赋值时，b的内存地址发生了变化
# 在python中，整数是不可变对象，当b重新赋值时，b指向了一个新的内存地址

# python中可变数据类型：列表、字典、集合
# python中不可变数据类型：数字、字符串、元组