# 闭包
## 自由变量：未在本地作用域中定义的变量。比如定义在内层函数外的外层函数的作用域中的变量。
## 闭包：就是一个概念，出现在嵌套函数中，指的是内层函数引用到了外层函数的自由变量，就形成了闭包
def counter():
    c = [0]
    def inc():
        c[0] += 1 # 仅是因为这里如果不使用列表，相当于从新定义了一个局部变量，而不是引用外部变量，所以需要使用列表
        return c[0]
    return inc

foo = counter()
print(foo(),foo()) # 1 2

print(foo.__name__) # 1
print(foo.__closure__) # (<cell at 0x000001F3D3D3D1F0: list object at 0x000001F3D3D3D040>,)
print(foo.__closure__[0].cell_contents) # [2]

print(foo()) # 4

if foo.__closure__:
    for index, cell in enumerate(foo.__closure__):
        print(f"\nCell {index}:")
        print("Type:", type(cell))
        print("Available methods and attributes:", dir(cell))
        # dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
        print("Content:", cell.cell_contents)

# python使用引用计数来管理内存，如果一个函数（或闭包）仍然被某个变量引用，那么它的引用计数就不会为0，所以它所占用的内存就不会被释放
# 在python中，只要函数没有被回收，函数的内部变量就不会被回收
# foo.__closure__ 会返回一个元组，元组中的每个元素是一个cell对象，cell对象的cell_contents属性就是闭包中的自由变量的值
# 这里的cell对象是一个特殊的对象，它会引用外部函数的局部变量，所以即使外部函数执行完毕，cell对象也会保留外部函数的局部变量的引用
# 也就是说变量c的引用计数不会为0，是因为cell对象引用了变量c，所以变量c的引用计数不会为0，所以变量c所占用的内存不会被释放


def inc():
    global c # global仅影响当前函数，不会影响内层函数
    c = 0
    def inner():
        #c += 1  # 这里会报错，因为c是一个局部变量，但是在局部作用域中没有定义c，所以会报错
        return c
    return inner

# nonlocal关键字
# LEGB规则：local -> enclosing -> global -> built-in
def counter():
    c = 0
    def inc():
        nonlocal c  # 使用nonlocal关键字，可以在内层函数中修改外层函数的局部变量,但是不能修改全局变量
        c += 1
        return c
    return inc

foo = counter()
print(foo(),foo()) # 1 2



