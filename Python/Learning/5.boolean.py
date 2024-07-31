# 布尔值表示两个值之一，True和False，注意大小写

# bool()函数可以评估任何值，并给出True或False
print(bool("Hello")) # True
print(bool(15)) # True

# 以下值被评估为False:
# 1. 任何值为0的数字
# 2. 任何空的容器，如列表、元组、集合、字典
# 3. 任何空的字符串
# 4. None

# isinstance()函数可以用来检查一个对象是否是一个特定的数据类型
# isinstance()函数特别有用，尤其当你想要确保函数或方法的输入是预期的数据类型时
x = 5
print(isinstance(x, int)) # True

# Python布尔类型的内部实现
# Python中的布尔值实际上是整数，True的值为1，False的值为0，这意味着你可以在数学运算中使用布尔值
print(True + True) # 2
print(True + False) # 1

# 以下是相关细节
# 1. 子类化：在Python源代码中，布尔类型是这样定义的
'''
PyTypeObject PyBool_Type = {
    ...
    "bool",                /* tp_name */
    sizeof(PyLongObject), /* tp_basicsize */
    ...
}
'''
# 这里，PyBool_Type继承自PyInt_Type，PyInt_Type是整数类型的基类，这意味着布尔类型是整数类型的子类

# 2. 单例实现：为了效率和内存使用，Python只有两个布尔对象，True和False。这两个对象在Python启动时被创建，并在整个生命周期中被重复使用

# 3. 整数等价性：在Python中，True等价于整数1，False等价于整数0。这意味着你可以在数学运算中使用布尔值

# 4. 布尔运算：Python中的布尔运算符是and、or和not。这些运算符的行为如下：
'''
and: 如果两个操作数都是True，则结果为True，否则为False
or: 如果两个操作数至少一个是True，则结果为True，否则为False
not: 如果操作数为True，则结果为False，否则为True
'''

# 5. 短路求值：Python中的布尔运算符是短路求值的，这意味着如果表达式的值可以确定，那么Python将不再计算表达式的其余部分
# 例如：在and运算中，如果第一个操作数为False，那么整个表达式的值就是False，Python将不再计算第二个操作数

# 6. 布尔运算符的优先级：not > and > or

# 7. 存储：由于单例性，它们实际上占用的内存可能比普通的整数要少