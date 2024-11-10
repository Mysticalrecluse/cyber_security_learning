# set 集合
# 集合是一个无序的不重复元素的可变序列

# 创建集合
# 1. 使用set()创建
# 2. 集合推导式，类似于列表推导式，但是使用{}创建，eg: {x for x in 'abcabcabc'}
x = {x for x in 'abcabcabc'}
print(x) # {'a', 'b', 'c'}

y = {*range(5)}
print(y) # {0, 1, 2, 3, 4}

# 集合不能放列表，字典，集合，但是可以放元组，因为元组是不可变的

# 集合的操作
# 添加元素
# add() 添加一个元素
x = set()
x.add(1)
print(x) # {1}

# update() 添加多个元素
x.update(range(5))
print(x) # {0, 1, 2, 3, 4}
x.update("abc")
print(x) # {0, 1, 2, 3, 4, 'a', 'b', 'c'}

# hash() 集合是不可哈希的，因为集合是可变的
# hash() 用于返回对象的哈希值
print(hash(1),hash('abc'))  # 1 2306086927453445731

# 集合的迭代
for i in x:
    print(i, end=" ")   # 0 1 2 3 4 a b c

# 集合的删除
# remove() 删除元素，如果元素不存在则会抛出异常
x.remove(1)
print(x) # {0, 2, 3, 4, 'a', 'b', 'c'}
# pop() 删除元素，如果集合为空则会抛出异常
y = x.pop()
print(y)
print(x) # {2, 3, 4, 'a', 'b', 'c'}

# discard() 删除元素，如果元素不存在则不会抛出异常
x.discard(2)
print(x) # {3, 4, 'a', 'b', 'c'}

# clear() 清空集合
x.clear()
print(x) # set()

# 判断元素是否在集合中
x = {1,2,3,4}
print(1 in x) # True
print(5 in x) # False

# 集合的运算
# 并集
x = {1,2,3}
y = {3,4,5}
z = x | y    # 返回新的集合
k = x.union(y) # 返回新的集合
print(z) # {1, 2, 3, 4, 5}
print(k) # {1, 2, 3, 4, 5}
x.update(y) # 将y合并到x中, x会改变
# 等价于 x |= y
print("x")
print(x)

# 交集
z = x & y
k = x.intersection(y) # 返回新的集合
# a.intersection_update(b) 将a和b的交集赋值给a, a会改变
# 等价于 a &= b
print(z) # {3}
print(k) # {3}

# 差集
z = x - y
k = x.difference(y)
# a.difference_update(b) 将a和b的差集赋值给a, a会改变
# 等价于 a -= b
print(z) # {1, 2}
print(k) # {1, 2}

# 对称差集
z = x ^ y
k = x.symmetric_difference(y)
# a.symmetric_difference_update(b) 将a和b的对称差集赋值给a, a会改变
# 等价于 a ^= b
# 如果x, y 无交集，则对称差集等价于并集
print(z) # {1, 2, 4, 5}
print(k) # {1, 2, 4, 5}

# set1 < set2 判断set1是否set2的子集
# isdisjoint() 判断两个集合是否有交集
# issubset() 判断一个集合是否是另一个集合的子集
