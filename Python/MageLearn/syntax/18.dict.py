# Dict即Dictory，也称为mapping
# 字典是可变的，无序的，key不重复的键值对的集合
# 构造函数dict()可以直接从键值对序列中构建字典
# 空字典
from typing import OrderedDict

x = dict()
print(x)

y = {}
print(y)
# 创建字典
x = dict(a=1, b='c')
print(x)

k = dict({'a':1, 'b':2, 'c':3} , a=100, d=4) # 重复的key会被覆盖, 不重复的key会被添加，必须是字典放前面
print(k)

g = dict([('a', 1), [1, 100]], a=2)  # 字典中的二元结构，会自动解构，变为key-value
print(g) # {'a': 2, 1: 100}

g = dict([[1,2]])  # 字典中的二元结构，会自动解构，变为key-value
print(g) # {1: 2}

h = dict.fromkeys('abc')
print(h) # {'a': None, 'b': None, 'c': None}
h = dict.fromkeys('abc', 1)
print(h) # {'a': 1, 'b': 1, 'c': 1}

k = dict.fromkeys('abc', [1])
print(k) # {'a': [1], 'b': [1], 'c': [1]}
k['a'][0] = 100
print(k) # {'a': [100], 'b': [100], 'c': [100]} # 会改变所有的值,因为是引用, 指向同一个内存地址，浅拷贝
print('d' in k) # False


# 用一个字典构造一个新字典
x = {'a':1,'b':2}
y = dict(x)
print(y)

# 遍历字典
# d = {}
# for k, v in iterable:
#     d[k] = v
# 遍历key
print("遍历key:")
d = {'a': 1, 'b': 2, 'c': 3}
for k in d.keys():
    print(d[k], end=" ")
print("")

# d1.keys() 可以看做 set-like，因此可以和集合做运算，dict.values()不行，不能和集合运算
print("dict和set做集合运算：")
print(d.keys() & {'d','a',1,2})
# 这里将d.items看做一个二元组集合
# ([('a',1),('b',2),('c',3)])
print(d.items() & {'d','a', 1, 2})


# 遍历values
print("遍历value：")
for v in d.values():
    print(v, end=" ")

print("")





# 字典取值
x = {'a':1, 'b':2}
print(x.get('a')) # 1
print(x.get('d')) # None, 不会报错，但是返回None，使用x['d']则会报错
# d1.get(key,default)
print(x.get('d',1)) # 1, 如果没有则返回默认值


# setdefault() 如果key不存在，则添加key-value，如果存在则返回value
d1 = {'a': 1, 'b': 'abc', 'c': False, 'd': None}
print(d1.setdefault('e', 100))
print(d1) # {'a': 1, 'b': 'abc', 'c': False, 'd': None, 'e': 100}
print(d1.setdefault('g')) # None 如果没有则返回默认值

# 新增和修改
d1['a'] = 2
print(d1) # {'a': 2, 'b': 'abc', 'c': False, 'd': None, 'e': 100}

# dict.update()
d1 = {'a': 1, 'b': 'abc', 'c': False, 'd': None}
print(d1.setdefault('e', 100))
print(d1) # {'a': 1, 'b': 'abc', 'c': False, 'd': None, 'e': 100}
print(d1.setdefault('g')) # None 如果没有则返回默认值

# 删除
del d1['a']
print(d1) # {'b': 'abc', 'c': False, 'd': None, 'e': 100}
d1['a'] = 2
# 存在即修改，不存在即添加
print(d1) # {'a': 2, 'b': 'abc', 'c': False, 'd': None, 'e': 100}

# pop(), 必须指定key，如果key不存在则会抛出异常
print(d1.pop('a')) # 2
print(d1) # {'b': 'abc', 'c': False, 'd': None, 'e': 100}

# popitem() 随机删除一个元素
print(d1.popitem()) # ('e', 100)
print(d1) # {'b': 'abc', 'c': False, 'd': None}

print(len(d1)) # 3， len()，返回字典的长度
# clear() 清空字典
d1.clear()
print(d1) # {}

import sys
# sys.getrefcount() 返回对象的引用计数
count = sys.getrefcount([1])
print(count)  # 1，等待垃圾回收

d1 = {'a': 1, 'b': 2}

# 字典的遍历
# 字典的key要可hash，所以key不能是列表，字典，集合
for key in d1:
    print(type(key), key)

d2 = {'a':[1,2], 'b':(3,)}

# 使用解构
for k, (v,*_) in d2.items():
    print( v) # 1 3

# 情况1：在遍历的过程中修改key的值
for k,_ in d2.items():
    d2[k] = 100

print(d2) # {'a': 100, 'b':100}

#for k in d2:
#    d2.pop(k) # 报错，因为在遍历的过程中修改了字典的大小

# 在for循环中，不要修改可迭代对象的大小

# 在以keys,values,items遍历字典时，不要修改字典的大小
while len(d2):
    d2.popitem()

print(d2) # {}，清空字典

# 要将字典中的指定键弹出，不能直接弹，要借用列表，因为字典遍历过程中不能修改长度
d2 = dict(a=100, b=200, c=300, d=400)
keys=[]

print(f"d2:{d2}")
for k in d2.keys():
    if d2[k] > 200:
        keys.append(k)
print("超过200t弹出：")
for k in keys:
    print(d2.pop(k))

# from collections import OrderedDict 有序字典，这里有序指的是录入的顺序
# python3.8之后，字典自动呈现该特性，但是如果希望向下兼容，可以使用该函数
from collections import OrderedDict
d3 = OrderedDict()
d3.update(a=1, b="abc")
print(d3)
d3.update({'a':100, 'd':3},d=4,c=5)
print(d3)
