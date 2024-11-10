#装饰器
## 可迭代对象
### 内建函数
#### iter()函数,iter(iterable) -> iterator, 把一个可迭代对象转换为迭代器
#### next()函数,next(iterator) -> next value, 返回迭代器的下一个值
#### reversed()函数,reversed(sequence) -> reverse iterator, 返回一个反向迭代器
#### enumerate()函数,enumerate(iterable, start=0) -> iterator, 返回一个迭代器，迭代器的元素是一个元组，元组的第一个元素是索引，第二个元素是值
from datetime import datetime

## 迭代器
### 特殊的对象，一定是可迭代对象，但是可迭代对象不一定是迭代器
### 生成器对象，就是迭代器对象。但是迭代器对象不一定是生成器对象

# iter()函数,用于包装可迭代对象(非迭代器)，返回一个迭代器对象
x = [1,2,3]
y = iter(x)
print(y) # <list_iterator object at 0x7f9a2c3d5d60>o

print(1 in x) # True
print(1 in y) # True
# -------------------------------
print(1 in x) # True
print(1 in y) # False, 迭代器只能迭代一次,之前已经迭代了1
# -------------------------------

x = [1,2,3,4,5]
y = iter(x)

print(-1 in y) # False
print(1 in x) # True
print(1 in y) # False ,在查找-1时，迭代器已经到头了，所以1不在迭代器中，此时迭代器为空



# reversed()函数,返回一个反向迭代器
x = [1,2,3]
y = reversed(x)
print(y) # <list_reverseiterator object at 0x7f9a2c3d5d60>

# enumerate()函数,返回一个迭代器，迭代器的元素是一个元组，元组的第一个元素是索引，第二个元素是值
x = [1,2,3]
y = enumerate(x)
print(y) # <enumerate object at 0x7f9a2c3d5d60>
print(next(y))



# 内建函数
# 排序
# sorted(iterable, key=func, reverse=False) -> list
x = [1, '2', 3]
sorted(x, key=str) # [1, 3, '2']，返回新列表，不改变原列表
x.sort(key=str) # [1, 3, '2']，改变原列表

# 过滤
# filter(func, iterable) -> filter object

x2 = filter(None, range(1, 10))
print(x2) # <filter object at 0x7f9a2c3d5d60> ,返回一个迭代器
print(next(x2)) # 1

print(list(filter(None, range(-3, 3)))), # [-3, -2, -1, 1, 2],None相当于bool()函数，返回True的元素

print(list(filter(lambda x: x % 3 == 0, [1, 123, 300, 456, 780, 31]))) # [123, 300, 456, 780]

# map(func, *iterables) -> map object
x3 = map(str, range(5))
print(x3) # <map object at 0x7f9a2c3d5d60>，返回一个迭代器
print(list(map(lambda *args: args, range(5), 'abcd', '1234')))
# [(0, 'a', '1'), (1, 'b', '2'), (2, 'c', '3'), (3, 'd', '4')]

# zip(*iterables) -> zip object
x4 = zip(range(5), 'abc')
print(x4) # <zip object at 0x7f9a2c3d5d60>，返回一个迭代器
print(list(zip(range(5), 'abc'))) # [(0, 'a'), (1, 'b'), (2, 'c')]

print(zip('abcd', range(5), '12345')) # <zip object at 0x7f9a2c3d5d60>
print(list(zip('abcd', range(5), '12345')))
# [('a', 0, '1'), ('b', 1, '2'), ('c', 2, '3'), ('d', 3, '4')]

# 高阶函数
# 高阶函数应当满足以下两个条件之一：
# 1. 函数接受一个或多个函数作为参数
# 2. 函数返回一个函数

def conter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc
f1 = conter(5)
f2 = conter(5)
print(f1 == f2)  # False
print(f1 is f2) # False

# 柯里化
# 柯里化是指将接受多个参数的函数转换为接受一个参数的函数的过程
# 柯里化是一个闭包函数
# 示例：
def add(x, y):
    return x + y
print(add(4, 5)) # 9

def add(x):
    def _add(y):
        return x + y
    return _add

print(add(4)(5)) # 9


# 示例2
def add(x, y, z):
    return x + y + z

def add1(x):
    def add1_inner(y, z):
        return x + y + z
    return add1_inner

def add2(x, y):
    def add2_inner(z):
        return x + y + z
    return add2_inner

def add3(x):
    def add3_inner(y):
        def add3_inner2(z):
            return x + y + z
        return add3_inner2
    return add3_inner
print(add3(4)(5)(6)) # 15

# 装饰器
# 装饰器是一种高阶函数，接受一个函数作为参数，返回一个函数
# 装饰器的作用是在不改变原函数的情况下，为原函数添加新的功能

# 补充知识
import time  # 时间底层模块
#print('-------')
#time.sleep(10)  # 休眠10秒,阻塞效果，程序暂停10秒
#print('*******')
#
import datetime # 时间高层模块
#print(datetime.datetime.now()) # 2021-09-02 17:11:45.583560
#
#start = datetime.datetime.now()
#time.sleep(2)
#end = datetime.datetime.now()
#
#print(end - start)  # 返回一个timedelta对象，表示时间差
#print((end - start).total_seconds())  # total_seconds()方法，返回时间差的秒数
#print(type((end-start).total_seconds()))  # <class 'float'>

# 装饰器的应用
# 1. 日志
def add(x, y, z):
    return x + y + z

def logger(fn, *args, **kwargs):
    print(fn.__name__, '参数', *args, kwargs)
    print("执行前可以做一些操作")
    ref = fn(*args, **kwargs)
    print("执行后可以做一些操作")
    return ref

# 柯里化
def logger2(fn):
    def wrapper(*args, **kwargs):
        print(fn.__name__, '参数', *args, kwargs)
        print("执行前可以做一些操作")
        ref = fn(*args, **kwargs)
        print("执行后可以做一些操作")
        return ref
    return wrapper

add = logger2(add)
print(add(1,2,3))

print("------------------")

## 整理为装饰器
def logger2(fn):
    def wrapper(*args, **kwargs):
        #print("执行前可以做一些操作")
        start = datetime.datetime.now()
        ref = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(f"函数{fn.__name__}执行时间为{delta}")
        #print("执行后可以做一些操作")
        return ref
    return wrapper

@logger2  # 等价于add = logger2(add)，logger等效为单参函数
def add(x, y, z):
    return x + y + z

# @装饰器语法：@标识符，把这一行下面的函数作为参数传递给标识符，然后把返回值赋值给下面的函数

print(add.__name__) # wrapper，装饰器会改变原函数的元信息，所以需要使用functools.wraps装饰器
print(add(1,2,3))

## 总结:无参装饰器
### 1. 上述的装饰器语法，称为无参装饰器
### 2. @符号后面是一个函数
### 3. 虽然是无参装饰器，但是实际上是一个单参函数，这个单参函数的参数是被装饰的函数
### 4. 上述的logger函数是一个高阶函数，接受一个函数作为参数，返回一个函数


print("---------函数元数据：文档---------")
# 带参数装饰器
## 文档：add.__doc__ 表示函数的文档字符串
## 函数文档必须写在函数第一行
## 类的文档必须写在类的第一行
## 模块的文档必须写在模块的第一行
def add(x, y):
    """这是一个加法函数"""
    pass

print("文档：",add.__doc__) # 这是一个加法函数
print("name: ",add.__name__) # 这是一个加法函数

from functools import update_wrapper, wraps

def logger(wrapped):
    @wraps(wrapped)  # 等价于wrapper=wraps(wrapped)(wrapper),partial函数
    def wrapper(*args, **kwargs):
        print("执行前可以做一些操作")
        ref = wrapped(*args, **kwargs)
        print("执行后可以做一些操作")
        return ref
    #update_wrapper(wrapper, wrapped), # 等效于@wraps(wrapped)
    return wrapper

@logger
def add(x, y: int): # 函数注解
    """这是一个加法函数!!!"""
    return x + y

print("文档：",add.__doc__) # 这是一个加法函数!!!
print(add.__annotations__) # {'y': <class 'int'>},add.__annotations__表示函数的注解
print(add(3,5))

# 带参数装饰器
# @之后不是单独的标识符，是一个函数调用
# 函数调用的返回值是一个函数，此函数是一个无参装饰器
# 带参装饰器可以有任意个参数