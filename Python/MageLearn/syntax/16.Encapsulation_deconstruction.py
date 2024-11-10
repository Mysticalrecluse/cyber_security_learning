# 封装与解构
# 使用封装和解构可以使代码更加简洁，易读，易维护
# 使用封装解构的方法交换数据
a = 1
b = 2
print(a,b)
a, b = b, a
print(a,b)

# 封装：1,2等价于(1,2)
a = 1,2
print(a) # (1, 2)

# 示例
a, b, c = range(3)
print(a) # 0
print(b) # 1
print(c) # 2

# 字符串是可迭代对象，也可以解构
a,b,c="tom"
print(a)
print(b)
print(c)

# 重点：左右两边元素个数相同

# rest变量
a, *rest, b = range(10) # rest参数解构，*rest表示剩余的元素，返回列表
print(a)
print(b)
print(rest) # 返回列表，[1, 2, 3, 4, 5, 6, 7, 8]

a, *r, b = b'abc'
print(r)

# 下划线变量，表示不需要的变量，可以使用下划线代替，但是下划线变量不会被赋值，只是一个占位符
_, *a, _ = range(5)
print(_) # 4
print(a) # [1, 2, 3]
print(_) # 4

# 列表的解构
x = [*(1,2)]
print(x) # [1, 2]

_,[*_,c],_ = [1,[2,3],4]
print(c) # 3

path = r'c:\windows\nt\drives\etc'
*_,a,b = path.split('\\')
print(a) # drives
print(b) # etc

dirname,_,basename = path.rpartition('\\')
print(dirname) # c:\windows\nt\drives
print(basename) # etc


