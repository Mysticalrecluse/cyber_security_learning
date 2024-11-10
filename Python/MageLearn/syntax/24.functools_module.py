# functools模块
from functools import reduce, partial, lru_cache
import inspect

# reduce函数
# reduce(function, iterable[, initializer]) -> value

def add(x, y):
    print(x, y)
    return x + y
print(reduce(add, range(4)))

'''
结果：
0 1
1 2
3 3
'''

print(reduce(lambda x, y: print(x, y), range(1, 5), 100))
'''
结果：
100 1, 100是initializer
None 2
None 3
None 4
'''

# 阶乘
print(reduce(lambda x, y: x * y, range(1, 6))) # 24

# 偏函数
# functools.partial函数，返回一个新函数，这个新函数固定住了原函数的部分参数
# partial(func, *args, **keywords) -> newfunc
def add(x:int, y:int) -> int:
    return x + y

newadd = partial(add, 4)

print(newadd(3)) # 7, 相当于add(4, 3)
print(inspect.signature(newadd)) # (y:int) -> int

## 偏函数的解释性函数
"""
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        ret = func(*args, *fargs, **newkeywords)
        return ret
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
"""

# lru_cache函数
# lru_cache(maxsize=128, typed=False) -> decorator
# least recently used cache，最近最少使用缓存

import time

@lru_cache  # 等价于@lru_cache()，不传参数时，maxsize=128, typed=False
# 如果maxsize设置为None，则禁用LRU功能，并且缓存可以无限增长。当maxsize是2的幂时，LRU功能效果最好
# 如果typed设置为True，则不同参数类型的调用将被缓存.例如，f(3)和f(3.0)将被视为不同的调用
# lru_cache内部做了处理，去判断是否传了参数
def add(x, y):
    time.sleep(2)
    return x + y

print(add(4, 5)) # 9, 要等2秒
print(add(4, 5)) # 9, 不用等2秒，因为缓存了

# lru_cache本质
# 内部实现了一个字典，用来存储函数的参数和返回值
# key是由_make_key函数生成的

# lru_cache中的make_key函数,后续要走读源码，重点函数_make_key，从元组到列表，再到字典的转化过程

# 附加题：自己实现一个make_key函数;
# 1. 传入参数是一个函数和一个元组，返回一个字典
# 2. 字典的键是函数的参数名，值是参数值
# 3. 函数的参数名和参数值是一一对应的
# 4. 函数的参数名和参数值是从元组中获取的

# def add(x=4, y=5): pass
# add(4, 5); add(x=4, y=5); add(y=5, x=4);add(); add(4, y=5);在这几种情况下，make_key函数的返回值是一样的


@lru_cache
def fibo(n):
    if n == 1 or n== 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(100)) # 354224848179261915075，因为缓存了，所以不用等很久




