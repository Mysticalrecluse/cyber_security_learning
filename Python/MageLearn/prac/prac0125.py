print("hello")

listA = [1,2,3,5]

print(len(listA))

# index(), count()

listA.insert(1,'9')

print(listA)

listA.extend(['a', 'm'])
print(listA)

listA.remove(3)
print(listA)

var1 = listA.pop()
print(listA)
print(var1)
var2 = listA.pop(2)
print(listA)
print(var2)


a = [1,2]
b = [1,2]
print(id(a),id(b)) # 140239366004992 140239366005056 内存地址不同
print(id(a[1]),id(b[1])) # 140239366005056 140239366005056 内存地址相同,因为是不可变对象,指向同一个内存地址
a == b # True

a = [[1], [2]]
b = a.copy()

a[0][0]=8
print(b)

import copy, random
c = copy.deepcopy(a)
a[0][0]=5
print(c)
print(a)

for i in range(10):
    print(random.randint(0,9), end=" ")

print("")
# randrange() function returns a randomly selected element from the specified range.
for i in range(10):
    print(random.randrange(0,100,2), end=" ")

print("")

alpList = ['a', 'c', 'd']
for i in range(5):
    print(random.choice(alpList), end=" ")

print("")

x = list(range(10))

print(random.sample(x,k=5))

binaryStr = "abc".encode()
print(binaryStr.decode())


*a, b,r = "hell0"
print(a)
print(b)
print(r)

a, *r, b = b'abc'
print(r)
print(type(r[0]))
print(type(a),type(b),type(b'abc'))
print((b'abc'))

a = b'abc'
for i in a:
    print(i)

print(a.decode())

_,a1,_ = a
print(a1)

name2 = '\r\n\t eric \r\n\t '
print(name2.strip("\r\t ").encode())

list1 = [[1],[2],[3]]
list2 = list1.copy()
list1[0][0]=9
print(id(list1[0]),id(list2[0]))

import copy
list1 = [[1],[2],[3]]
list2 = copy.deepcopy(list1)
list1[0][0]=9
print(id(list1[0]),id(list2[0]))

