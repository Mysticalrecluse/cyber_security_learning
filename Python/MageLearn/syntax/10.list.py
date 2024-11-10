# 列表
# python采用顺序表实现列表，列表是一个有序的集合，可以包含任意数量的元素。
# 列表中的元素可以是任何数据类型，甚至是不同的数据类型。
# 列表是可变的，可以通过索引访问和修改列表中的元素。
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

# 构造一个空列表
L = []
K = list()
print(L) # []
print(K) # []

# 使用len()函数获取列表的长度,len()的时间复杂度是O(1)。
# 正索引范围是0到len()-1，负索引范围是-len()到-1。
students = ['ben', 'tom', 'jerry', 'mike']
print(len(students)) # 4

# 列表元素的查询方法
# index(), count()
students = ['ben', 'tom', 'jerry', 'mike', 'tom']
print(students.index('tom')) # 1
print(students.count('tom')) # 2

# index()和count()方法的区别
# index()方法返回指定元素的索引，如果元素不存在，会引发ValueError异常。
# count()方法返回指定元素的数量，如果元素不存在，返回0。
'''index()和count()的时间复杂度都是O(n)。因此，如果需要频繁查询元素的索引或数量，可以考虑使用字典。'''

# 列表元素的增加方法
# append(), extend(), insert()
# 上述函数无返回值，直接修改原列表。
# append()方法用于在列表的末尾添加一个元素。效率高，时间复杂度是O(1)。
students = ['ben', 'tom', 'jerry', 'mike']
students.append('lucy')
print(students) # ['ben', 'tom', 'jerry', 'mike', 'lucy']


# extend()方法用于在列表的末尾添加多个元素。效率高，时间复杂度是O(k)。
students.extend(['lily', 'lucy'])
print(students) # ['ben', 'tom', 'jerry', 'mike', 'lucy', 'lily', 'lucy']

# insert()方法用于在指定位置插入一个元素。效率低，时间复杂度是O(n)。
students.insert(1, 'lily')
print(students) # ['ben', 'lily', 'tom', 'jerry', 'mike', 'lucy', 'lily', 'lucy']


# +重载
#
x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(z) # [1, 2, 3, 4, 5, 6]

# *重载
# 使用*运算符可以复制一个列表，返回一个新的列表。生成的新列表是原列表的拷贝，原列表不变。
x = [1, 2, 3]
y = x * 3
print(y) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 特殊情况
z = [[1]] * 3
print(z) # [[1], [1], [1]]
z[1] = 300
print(z) # [[1], 300, [1]]

a = [[1]] * 3
print(a) # [[1], [1], [1]]
a[1][0] = 300
print(a) # [[300], [300], [300]]
# 原因：列表的复制是浅拷贝，即复制的是引用。因此，当修改一个列表的元素时，其他列表的元素也会被修改。

# 列表元素的删除方法
# remove(), pop(), clear()
# remove()方法用于删除列表中的指定元素，如果元素不存在，会引发ValueError异常。
# remove()方法只删除第一个匹配的元素。
# remove()就地删除，不返回任何值。
students = ['ben', 'tom', 'jerry', 'mike']
students.remove('tom')
print(students) # ['ben', 'jerry', 'mike']

# pop()方法用于删除列表中的指定索引的元素，并返回删除的元素。如果索引不存在，会引发IndexError异常。
# pop()默认删除最后一个元素。
students = ['ben', 'tom', 'jerry', 'mike']
student = students.pop(1)
print(student) # tom
print(students) # ['ben', 'jerry', 'mike']:w

# clear()方法用于清空列表，等价于del students[:]。
students = ['ben', 'tom', 'jerry', 'mike']
students.clear()
print(students) # []

# 列表反转
# reverse()方法用于反转列表中的元素。效率低，时间复杂度是O(n)。
# reverse()就地反转，不返回任何值。
students = ['ben', 'tom', 'jerry', 'mike']
students.reverse()
print(students) # ['mike', 'jerry', 'tom', 'ben']

# 直接实现反转
students = ['ben', 'tom', 'jerry', 'mike']
students = students[::-1]
print(students) # ['mike', 'jerry', 'tom', 'ben']


# reversed()函数, 返回一个反转的迭代器, 不改变原列表, 适用于大数据量,效率高
students = ['ben', 'tom', 'jerry', 'mike']
students = list(reversed(students))
print(students) # ['mike', 'jerry', 'tom', 'ben']


# 排序,方法
# sort(*, key=None, reverse=False)
# sort()方法无返回值，直接修改原列表。
# sort()方法用于对列表中的元素进行排序，默认升序排序。

x = [1, 3, 2, 6, 4, 3]
print(x)
x.sort()
print(x) # [1, 2, 3, 3, 4, 6]

# sorted()函数, 返回一个新的列表, 不改变原列表, 适用于大数据量,效率高
x = [1, 3, 2, 6, 4, 3]
y = sorted(x)
print(x) # [1, 3, 2, 6, 4, 3]
print(y) # [1, 2, 3, 3, 4, 6]

a = [1, 3, 2, 6, 4, 3]
b = sorted(a, reverse=True)
print(a) # [1, 3, 2, 6, 4, 3]
print(b) # [6, 4, 3, 3, 2, 1]

# 列表的复制
a = [1,2]
b = [1,2]
print(id(a),id(b)) # 140239366004992 140239366005056 内存地址不同
print(id(a[1]),id(b[1])) # 140239366005056 140239366005056 内存地址相同,因为是不可变对象,指向同一个内存地址
a == b # True

# 所以==比较的是值是否相等, is比较的是内存地址是否相等
print(a[1] is b[1])

a[1] = 3
print(a,b) # [1, 3] [1, 2]
print(id(a[1]),id(b[1]))

# copy()方法用于复制一个列表，返回一个新的列表。生成的新列表是原列表的拷贝，原列表不变。
# copy()方法是浅拷贝， 因此，当修改一个列表的元素时，其他列表的元素不会被修改。
# 浅拷贝的意思是复制的是引用，而不是对象本身。

a = [1,3,5]
b = a.copy()
print(id(a),id(b)) # 140239366005056 140239366005120 内存地址不同
a[1] = 9
print(b)
c = a
print(id(a),id(c)) # 140239366005056 140239366005056 内存地址相同
a[1] = 10
print(c)

# 深拷贝
# 深拷贝是指复制对象的所有元素，包括对象的元素，以及对象的元素的元素。
# 深拷贝的时间复杂度是O(n)，因为需要复制对象的所有元素。
import copy
a = [1,[1,2,3],5]
b = copy.deepcopy(a)
a[1][1] = 9
print(b)
print(a==b)


# 扩展：垃圾回收：引用计数
# python使用引用计数来跟踪内存中的对象。当对象的引用计数为0时，对象的内存会被释放。虚拟机会定期检查引用计数，在合适的时候释放引用计数为0的对象。
# 引用计数的优点是实现简单，缺点是无法处理循环引用的情况。
# 垃圾回收： 会整理内存，解决内存碎片问题，提高内存利用率。
# python的垃圾回收机制主要有两种：分代回收和循环垃圾回收。

# 垃圾回收会触发STW：Stop The World，即停止所有用户线程，只保留一个GC线程在运行。
# 所以尽量减少垃圾回收的次数，可以提高程序的性能。也就是说，尽量减少对象的创建和销毁，尽量减少循环引用的情况。
# python中列表的结构体是一个数组，数组中的元素是指针，指向对象的内存地址。
# 当列表中的元素是不可变对象时，列表的元素是对象的引用。
# 当列表中的元素是可变对象时，列表的元素是对象的引用的引用。
# 因此，当列表中的元素是可变对象时，修改一个元素会影响其他元素。
# python中的列表是一个动态数组，当数组的容量不足时，会重新分配一个更大的数组，并将原数组的元素复制到新数组中。
# python中列表的C语言结构体定义如下：
# typedef struct {
#     PyObject_VAR_HEAD
#     PyObject **ob_item;
#     Py_ssize_t allocated;
# } PyListObject;
# ob_item是一个指针数组，指向对象的内存地址。allocated是数组的容量，即数组的长度。
# 当数组的长度小于allocated时，数组的容量不足，需要重新分配一个更大的数组。
# 当数组的长度大于allocated时，数组的容量充足，不需要重新分配数组。




