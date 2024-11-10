# 函数
# add是标识符，函数名，指向一个函数对象
# def是关键字，用来定义函数,define,定义时
# (参数列表)，参数列表，用来接收参数，可以有n个参数，这些参数都是形参
def add(x,y):
    return x + y

# 因此add后续也可以赋值位别的
add = 1

print(add)

def add(x,y):
    print(f"x = {x}, y = {y}")
    return x + y

# 函数的引用，调用时
# 在函数标识符后面加括号，就是调用，执行called，调用时
# 这里的4，5是实参，实际参数，传递给函数的值，调用时
print(add(4,5)) # 9

# callable()函数，判断一个对象是否是可调用对象
print(callable(add)) # True

# 函数的签名
# 函数的签名是指函数的名字和参数列表，比如add(x,y)的签名是add(x,y)
print(add) # <function add at 0x7f9a2c3d5e50>

# 传实参
## 1. 按位置传参
add(4,5)
## 2. 按关键字传参
add(y = 3, x = 9)

## 二者可以混合使用，但是位置参数必须在关键字参数之前

# 形参，有缺省值，定义时，如果没有提供该参数，自动用缺省值
def add(x=4,y=5):
    return x + y
print(add(10)) # 15

def login(host='local', port=3306, username='root', password='123'):
    con_str = "mysql://{}:{}@{}:{}".format(username, password, host, port)
    return con_str
print(login()) # mysql://root:123@local:3306
print(login('192.168.10.1', 3306, 'admin', '123')) # mysql://admin:admin@

#def add(x=4, y):
#    return x + y
# 上述代码会报错，因为有缺省值的参数必须在没有缺省值的参数之后，缺省值应该放后面

# 可变参数
# 可变参数没有缺省值
# *args，可变参数，接收任意个参数，是一个元组
# 只能接受位置参数，不能接受关键字参数
def add(*args):
    print(args, type(args)) # (1, 2, 3) <class 'tuple'>

add(1,2,3)

def add(*args):
    s = 0
    for i in args:
        s += i
    return s

print(add(1,2,3)) # 6

print(add(*range(5))), # 10，*range(5)相当于1,2,3,4，使用*解构

# **kwargs，可变关键字参数，接收任意个关键字参数，是一个字典
def add(**kwargs):
    print(kwargs, type(kwargs))

add(a=1,b=2,c=3) # {'a': 1, 'b': 2, 'c': 3} <class 'dict'>

# keyword-only参数
# 在*args之后的参数，必须使用关键字传参
# 普通参数的默认值必须放在位置参数之后，否则会报错
# keyword-only参数的默认值之间没有顺序要求
def foo(*args, x, y):
    print(x, y, args)

foo(1, 2, 3, x=4, y=5) # 4 5 (1, 2, 3)

def fn(*, x, y): # *表示后面的参数必须使用关键字传参
    print(x, y)

fn(x=1, y=2) # 1 2 , 必须使用关键字传参

# /，分隔符，/之前的参数必须使用位置参数传参
# positional-only参数
def fn(x, y, /, z, w):
    print(f"x = {x}, y = {y}, z = {z}, w = {w}")

fn(1, 2, 3, w=4) # 1 2 3 4

# 综合示例
# sorted(iterable, /, *, key=func, reverse=False) -> list
# iterable，可迭代对象
# key，排序规则
# reverse，是否降序
def sort(iterable, /, *, key=None, reverse=False):
    return sorted(iterable, key=key, reverse=reverse)


# 示例2
# 定义函数时，把重要的参数放在前面，不重要的参数放在后面，因为不重要的参数可以使用缺省值
def config(host, username='mystical', password='mystical', port=3306, **options):
    # dbname = options.get('db','test')
    dbname = options.pop('db', 'test')
    print(f"mysql://{username}:{password}@{host}:{port}/{dbname}")

config('192.168.10.2') # mysql://mystical:mystical@192.168.10.2:3306/test

# 参数解构
# func(*iterable) ,将可迭代对象解构为位置参数
# func(**dict) ,将字典解构为关键字参数
def add(*nums):
    s = 0
    for i in nums:
        s += i
    return s
res = add(*range(5)) # 10
print(res)

def x(a, b):
    return a + b

print(x(*{'a':1, 'b':2})) # ab
print(x(*{'a':1, 'b':2}.values())) # 3

print(x(**{'a':1, 'b':2})) # 3 , **将字典解构为关键字参数,a = 1, b = 2


# 返回值 return
# return语句用于从函数中返回一个或多个值
# return 等价于 return None
# return 1,2,3 等价于 return (1,2,3)
def a():
    return
print(a())

def b():
    print('-----')
    return 1 # return后面的代码不会执行
    print('+++++')
    return 2


# 函数作用域
# 函数内部定义的变量，只能在函数内部使用，函数外部无法访问
'''
def fn():
   x = 100
   print(x)
print(x) # NameError: name 'x' is not defined
'''
# 函数外部定义的变量，可以在函数内部使用，但是不能修改
''' 
x = 100
def fn():
    print(x)
    x = 200
print(x) # 100
'''

# 作用域分类
# 全局作用域，局部作用域
# 全局作用域：
# 1. 在整个程序运行环境中都可见
# 2. 全局作用域中的变量称为全局变量global

# 局部作用域
# 1. 在函数，类内部可见
# 2. 局部作用域中的变量称为局部变量，只能在函数内部使用
# 3. 也称为本地作用域local


# 函数嵌套
def outer():
    x = 100
    def inner():
        print(f'in inner, x = {x+200}')
    inner()
    print(f'in outer, x = {x}')

outer() # in inner, x = 300 in outer, x = 100

## 报错
'''
z = 100
def fn3():
    print(z) # 使用的时候，没有被定义，这里的z被看作局部变量z,他是在后面的z=z+1中被定义的
    m = z + 1
    print(m)
    z = z + 1
    print(z)  # UnboundLocalError: local variable 'z' referenced before assignment
    # 原因：在函数内部，对变量进行赋值操作，会将变量当成局部变量，但是在赋值之前，变量没有被定义，所以会报错
    # 解决方案：在函数内部，使用global关键字声明变量是全局变量
'''
# 更改后
z = 100
def fn3():
    global z # 不到万不得已，不要使用global关键字，会破坏函数的封装性，可能会导致全局污染
    print(z)
    m = z + 1
    print(m)
    z = z + 1
    print(z)

fn3() # 100 101 101
print(z) # 101，全局变量z被修改

z = 100
def fn4():
    print(z) # 100, z是全局变量，可以在函数内部访问，但是不能修改，如果修改，会被当成局部变量


# 函数的销毁
# 函数执行完毕后，函数的内部变量会被销毁
# 函数的内部变量的生命周期和函数的生命周期一样

# LEGB规则
# local -> enclosing(外层函数局部变量) -> global(当前模块中的全局变量) -> built-in(内建函数的生命周期和解释器相同)


# 匿名函数
# 单行函数
# lambda表达式
# lambda args: expression

print((lambda : 0)()) # 0  # 该匿名函数恒定为0

print((lambda x: 100)(1)) # 100, x是形参，返回值是100

def a():
    return None

# 等价于
a = lambda : None

print(a()) # None

# 示例
b = lambda x, y = 10: x + y
print(b(1)) # 11
print(b(1,2)) # 3

c = lambda *args: [i+1 for i in args]
# print(c(range(5))  这里会报错，因为range(5)是一个可迭代对象，不是一个元组，需要使用*解构
# 这里相当于传进一个(range(5),)的元组,所以会报错
print(c(*range(5))) # [1, 2, 3, 4, 5])


# 示例2
d = lambda *args: (i for i in args)
print(d(*range(5))) # 返回的是一个生成器对象

# 示例3
print(dict(map(lambda x: (x, x+1), range(5)))) # {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

# 示例4：一个字典，kv对，key对应的value必须是列表
d1 = {k:[] for k in 'abcde'} # {'a': [], 'b': [], 'c': [], 'd': [], 'e': []}

d2 = dict(map(lambda x: (x, []), 'abcde')) # {'a': [], 'b': [], 'c': [], 'd': [], 'e': []}

d3 = dict.fromkeys('abcde',[]) # {'a': [], 'b': [], 'c': [], 'd': [], 'e': []}
# 但是这里的value是同一个列表，所以修改一个，其他的也会被修改，而d1和d2是不同的列表


# 补充
# defaultdict()函数,参数是一个函数，返回一个字典，当访问一个不存在的key时，会自动调用该函数创建一个默认值
from collections import defaultdict
d4 = defaultdict(list) # defaultdict(<class 'list'>, {})
d4['a'].extend(range(5)) # 如果key不存在，会自动添加key，并且创建d4[key] = list()
print(d4) # defaultdict(<class 'list'>, {'a': [0, 1, 2, 3, 4]})

d5 = defaultdict(set) # defaultdict(<class 'set'>, {})
d5['a'].add('1') # 如果key不存在，会自动添加key，并且创建d5[key] = set()
print(d5) # defaultdict(<class 'set'>, {'a': {'1'}})

d6 = defaultdict(lambda : {100})
d6['a'].add(1)
d6['c'].add(101)
print(d6) # defaultdict(<function <lambda> at 0x7f9a2c3d5d30>, {'a': {1}})

x = ['a', 'b', 'c', 1, 2, 3]
print(sorted(x,key=lambda x: int(x, 16) if isinstance(x, str) else x)) # [1, 2, 3, 'a', 'b', 'c']

# 生成器函数
# 生成器函数是一种特殊的函数，用来生成一个生成器对象
# 只要有yield关键字的函数，就是生成器函数
def inc():
    count = 0
    while True:
        count += 1
        yield count

x = inc()
print(x) # <generator object inc at 0x7f9a2c3d5d60> , 生成器对象

# 示例2
def inc():
    for i in range(5):
        yield i + 1

print(inc()) # <generator object inc at 0x7f9a2c3d5d60> , 生成器对象
print(1, next(inc())) # 1 1
print(2, next(inc())) # 2 1

# 正确用法
x = inc()
print(1, next(x)) # 1 1
print(2, next(x)) # 2 2

# 生成器函数的特点
# 1. 生成器函数使用yield关键字返回一个生成器对象
# 2. 生成器函数是一个特殊的函数，可以暂停执行，然后继续执行

# 生成器函数的应用
def foo():
    print(1)
    yield 2
    print(3)
    yield 4
    print(5)
    return 6
    yield 7

x = foo()   # 生成器函数，每一次执行到yield关键字时，会暂停执行，然后返回一个值
print(next(x)) # 1 2
print(next(x))

y = foo()
print(y)
for i in y:
    print(i, end=" ") # 1 /n 2  3 /n 4  5

def bar():
    if False:
        yield
print(bar()) # <generator object bar at 0x7f9a2c3d5d60> , 生成器对象
# 只要有yield关键字的函数，就是生成器函数，即使yield执行不到，也是生成器函数

# 生成器函数的应用
# 惰性本身是推荐的，还有它用在了协程上，协程是一种比线程更轻量级的并发编程方式

## 1. 无限序列, 也可以作为计数器
def fib():
    count = 0
    while True:
        count += 1
        yield count


## 2.计数器
def inc():
    def foo():
        count = 0
        while True:
            count += 1
            yield count
    c = foo()
    return lambda : next(c)

x = inc()
print(x()) # 1
print(x()) # 2

# 示例：斐波那契数列
def fib(x):
    def fibs():
       a, b = 0, 1
       while True:
           yield a
           a, b = b, a + b
    f = fibs()
    if x < 1:
        return -1
    elif x == 1:
        return 0
    else:
        for i in range(x-1):
            next(f)
        return next(f)

print(fib(101))


# 协程 Coroutine
# 生成器的高级用法
# 它比进程和线程更轻量级，占用资源更少，是在用户空间调度函数的一种实现
# python3 asyncio模块，提供了对协程的支持，已加入到python标准库中
# python3.5使用async和await关键字直接支持原生协程
# 协程调度器实现思路
# 1.有两个生成器A, B
# 2. next(A)后，A执行到yield关键字，暂停执行
# 3. next(B)后，B执行到yield关键字，暂停执行
# 4. 交替执行next(A)和next(B)函数，实现协程调度
# 5. 可以引入一个调度器，自动调度协程的执行
# 协程是一种非抢占式调度


# yield from用法
def foo():
    for i in range(5):
        yield i
for x in foo():
    print(x, end=" ") # 0 1 2 3 4

# 等价于
def foo():
    yield from range(5)
for x in foo():
    print(x, end=" ") # 0 1 2 3 4

# yield from iterable
# iterable是一个可迭代对象，yield from会自动迭代iterable，将iterable中的元素返回
