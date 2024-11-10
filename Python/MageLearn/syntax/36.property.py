# 属性装饰器

# 1. 为什么要使用属性装饰器
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):  # 管获取属性值的方法叫getter方法
        return self._name

    def set_name(self, new_name): # 管设置属性值的方法叫setter方法
        self._name = new_name


tom = Person('Tom')
# print(tom._name) # 不推荐直接访问，_name是保护成员
print(tom.get_name())

# tom._name = 'jerry' # 不推荐直接访问，_name是保护成员
tom.set_name('jerry')
print(tom.get_name())

# 2. 使用属性装饰器
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self): # getter方法
        return self._name

    @name.setter
    def name(self, new_name): # setter方法
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name

tom = Person('Tom')
print(tom.name)
tom.name = 'Jerry'
print(tom.name)

# del tom.name # 删除属性, 会报错，因为没有定义deleter方法

del tom.name # 删除属性, 不会报错， 因为定义了deleter方法

# print(tom.name) # 会报错，因为属性已经被删除


class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self, formatter: str = None):
        if formatter:
            return "{0} {1} {0}".format(formatter, self.__name)
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    name = property(get_name, set_name)

tom = Person('Tom')
print(tom.get_name()) # Tom
print(tom.get_name('*'))  # * Tom *
print(tom.name) # Tom

# 3. 使用属性装饰器,简写
class Person:
    def __init__(self, name):
        self.__name = name
    name = property(lambda self: self.__name)

tom = Person('Tom')
print(tom.name) # Tom


# 封装总结
## 将数据和操作组织到类中，即属性和方法
## 将数据隐藏起来，给使用者提供操作（方法）。使用者通过操作就可以获取或修改数据。getter和setter方法
## 通过访问控制，暴露适当的数据和操作给用户，给隐藏的隐藏起来，例如保护成员或私有成员