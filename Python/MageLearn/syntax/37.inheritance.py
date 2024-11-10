# 继承
# 从父类继承，子类可以使用父类的方法和属性，这样可以减少代码的重复。子类也可以定义自己的方法和属性。
from shlex import quote


class Animal:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name

    def shout(self):
        print("{} shouts".format(self._name))

class Cat(Animal):
    pass

class Dog(Animal):
    pass

dog = Dog('Wangcai')
dog.shout() # Wangcai shouts

cat = Cat('Mimi')
cat.shout() # Mimi shouts

"""
继承的格式
class 子类名(父类名):
    pass
    
class A:
    pass
# 等价于
class A(object):
    pass
"""

# 继承的特殊属性和方法
# __bases__ 含义：类的基类元组
print("Dog.__bases__", Dog.__bases__) # Dog.__bases__ (<class '__main__.Animal'>,)

# __base__ 含义：类的基类, 只能获取第一个基类
print("Dog.__base__", Dog.__base__) # Dog.__base__ <class '__main__.Animal'>

# __mro__ 含义：类的层次结构元组，显示放阿飞查找顺序，基类的元组
print("Dog.__mro__", Dog.__mro__)
# Dog.__mro__ (<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)

# mro() 含义：类的层次结构列表，显示放阿飞查找顺序，基类的列表
print("Dog.mro()", Dog.mro())
# Dog.mro() [<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>]

# __subclasses__ 含义：类的子类列表
print("Animal.__subclasses__", Animal.__subclasses__)
# Animal.__subclasses__ <built-in method __subclasses__ of type object at 0x000001D3D3C7E9D0>


## 继承中的访问控制
class Animal:
    __a = 10  # 相当于_Animal__a
    _b = 20
    c = 30
    __g = 500

    def __init__(self):
        self.__d = 40
        self._e = 50
        self.f = 60
        self.__a += 1 # 相当于self._Animal__a += 1

    def showa(self):
        print(self.__a) # 相当于self._Animal__a , 这里是实例的私有属性
        print(self.__class__.__a)  # 相当于Cat._Animal__a, 这里是类的私有属性


    def __showb(self):
        print(self._b)
        print(self.__a)
        print(self.__class__.__a)


class Cat(Animal):
    __a = 100
    _b = 200

c = Cat()
c.showa()
c._Animal__showb()
print('c.__dict__', c.__dict__) # c.__dict__ {'_Animal__d': 40, '_e': 50, 'f': 60}



# 实例属性的查找顺序
# 实例的__dict__ ->  类的__dict__ -> 父类的__dict__ -> 父类的父类的__dict__ -> object的__dict__

# 方法的重写、覆盖override
class Animal:
    def shout(self):
        print('Animal shouts')
class Cat(Animal):
    def shout(self):
        print('Cat shouts')

a = Animal()
a.shout() # Animal shouts

c = Cat()
c.shout()

# 子类调用父类的方法
class Animal:
    def shout(self):
        print('Animal shouts')
class Cat(Animal):
    def shout(self):
        super().shout()  # 调用父类的方法, super()返回的是一个super对象
        # super() -> same as super(__class__, <first argument>)
        # 等价于 super(Cat, self).shout()
        # 等价于 Animal.shout(self)
        # 等价于 self.__class__.mro()[1].shout(self)
        print('Cat shouts')

d = Cat()
d.shout()

# 继承与初始化
class A:
    def __init__(self, a):
        self.a1 = a
class B(A):
    # 子类初始化方法应该尽可能调用父类的初始化方法
    # 因为父类的初始化方法可能会对父类的属性进行初始化
    def __init__(self, b, c):
        super().__init__(b) # 调用父类的初始化方法
        # 等价于 A.__init__(self, b), 等价于 super(B, self).__init__(b)
        # 等价于 super().__init__(b)
        self.b1 = b
        self.b2 = c

    def showme(self):
        print(self.b1, self.b2)
        print(self.a1)

c = B(1, 2)
c.showme()

## 总结
### 如果在子类中覆盖了父类的__init__方法，那么在子类的__init__方法中，应该显示调用父类的__init__方法
### Python中并不限制在子类的__init__方法中调用父类的__init__方法，但是一般都应该尽早的调用
### 推荐使用super().__init__()或者super(子类名, self).__init__()来调用父类的__init__方法

# 多态
class Animal:
    def __init__(self, name):
        self._name = name
    def shout(self):
        print('Animal shouts')

class Cat(Animal):
    def shout(self):
        print('miaomiao')

class Dog(Animal):
    def shout(self):
        print('wangwang')

c = Cat('Mimi')
d = Dog('Wangcai')
c.shout() # miaomiao
d.shout() # wangwang

# 使用同样的接口，不同的对象调用同样的方法，产生不同的结果，这就是多态
# 多态的前提：继承，方法重写


# 多继承
# 一个类可以有多个父类，称为多继承
"""
class ClassName(基类1, 基类2, ...):
    pass
"""

class A:
    def show(self):
        print('A.show')
class B:
    def show(self):
        print('B.show')
class C(A, B):
    pass

c = C()
c.show() # A.show, 优先调用第一个父类的方法

# Mixin
# Mixin是一种设计模式，通过多继承来实现
class Document: # 抽象基类
    # 在其他语言中，抽象基类是一种特殊的类，不能实例化，只能被继承
    def __init__(self, content):
        self.content = content

    # 定义一个抽象方法, 子类必须实现这个方法
    def print(self):
        raise NotImplementedError("print not implemented")

# Word和Pdf是Document的子类,也是抽象类
# 抽象类用来规范子类的行为，子类必须实现抽象类中的抽象方法，抽象类不能实例化
class Word(Document): pass
class Pdf(Document): pass

class PrintableWord(Word):
    def print(self):
        print("[ {} ]".format(self.content))

class PrintablePdf(Pdf):
    def print(self):
        print("** {} **".format(self.content))

w = PrintableWord('test word string')  # 重写了父类的print方法
w.print()


y = PrintablePdf('test word string')  # 重写了父类的print方法
y.print()

# 需求场景
# Doc类只管内容，不管打印，子类也不是必须，有些类如需打印，自行实现
# word需要打印，pdf不需要打印，word\pdf父类是Doc
# word需要A B C 三个功能，pdf需要B D两个功能
# X 不是Doc的子类，但是需要A C D三个功能

# 缺什么补什么，不要多继承，不要重复继承，可以使用Mixin/装饰器来实现

# Mixin的使用
# Mixin是一种设计模式，通过多继承来实现

# 调用函数，返回返回值，调用类，返回类的实例
# 将类作为可调用对象使用

# 装饰器实现
"""
@A # a = A()
def a():
    pass
"""

# Mixin实现
class PrintableMixin:
    def print(self):
        print("**** {} ****".format(self.content))

# Mixin类的名字通常以Mixin结尾，并且写在继承列表的第一个，最前面，这样可以保证调用顺序
# 这里使用Mixin类用来增强Word类的功能
# Mixinx类通常不会单独使用，而是和其他类一起使用，放在前面，要么补充，要么覆盖。
class PrintableWord(PrintableMixin, Word): pass
print(PrintableWord.__bases__)
print(PrintableWord.mro())

# Mixin类和装饰器，都可以实现对类的功能增强，但是Mixin类更加灵活，可以实现多个功能增强，而装饰器只能实现一个功能增强，且可继承。


