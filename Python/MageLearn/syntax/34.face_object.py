# 面向对象
# 类 class
# 对象 instance, object
# 类的属性：对对象状态的抽象，用数据结构来描述
# 类的方法：对对象行为的抽象，用函数来描述

# 面向对象三要输：封装、继承、多态
# 封装：
    # 组装：将数据和操作组装到一起
    # 隐藏数据：对外只暴露一些接口，通过接口访问对象，比如驾驶员使用汽车，不需要知道汽车的内部结构，只需要知道如何驾驶汽车

# 继承：
    # 多复用，继承来的就不用自己写了
    # 多继承少修改，OCP(Open Close Principle)，使用继承来改变，来体现个性

# 多态
    # 面向对象编程最灵活的地方，动态绑定, 一个对象可以以多种形态出现


# 封装
# class 类名(ClassName):
    # 属性
    # 方法

# 示例
class Person:  # 定义类对象, Persion也是标识符
    """Person doc"""  # 文档字符串
    x = 123
    y = 'abc'
    def eat(self):  # 方法,self指当前实例本身
        print('eat', __class__, __name__)

print(Person)  # <class '__main__.Persion'> __main__表示当前模块
print(Person.__doc__, Person.__name__) # Person doc Person

print(Person.x)

print(Person.eat)


# 实例化对象
# 对象 = 类名()
p1 = Person() # 对Person这个抽象概念进行实例化，创建一个具体的对象,即实例化对象
print(p1) # <__main__.Person object at 0x000001D3D3D3A4C0>
print(type(p1)) # <class '__main__.Person'>

p2 = Person() # 创建另一个对象
print(p2) # <__main__.Person object at 0x000001D3D3D3A4F0>

class Person:
    def __init__(self): # 初始化方法，创建对象时自动调用, self指当前实例本身, 不能省略, 不能有返回值, 可以有多个参数
        # 初始化实例,习惯上叫构造器，构造方法
        print('init')

# 实例化指由类构造实例的过程
# 在构造一个对象的过程中，要完成两个阶段，
# 第一个阶段就是造实例，  __new__方法，创建对象时自动调用，返回当前对象的引用
# 第二个阶段就是初始化实例，对当前实例本身进行配置，2个对象完成后返回实例
# 总结：__new__方法是创建对象(实例化)，__init__方法是初始化对象(初始化)

class Persons:
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age
    def showme(self):
        print("i'm {self.name}, {self.age} years old")

curry = Persons('curry', 28) # init, 创建对象时自动调用__init__方法
james = Persons('james', 36) # 实例调用方法时，就不用在方法中直接写入对应的实例了，自动将绑定的实力注入给第一形参self

curry.showme() # i'm curry, 28 years old, 方法绑定到对象上，对象调用方法时，自动传入self参数
print(curry.showme) # <bound method Persons.showme of <__main__.Persons object at 0x000001D3D3D3A4C0>>
james.showme() # i'm james, 36 years old

print(curry.name, curry.age) # curry 28


class Person:
    def __init__(self):
        print(1,'init',id(self))
    def showme(self):\
        print(2, 'showme', id(self))

p1 = Person()
print(3, id(p1))

p1.showme() # 3个id相同，说明是同一个对象

# 类属性和实例属性
class Person:
    age = 3 # 类属性, 所有实例共享
    def __init__(self, name):
        self.name = name # 实例属性

tom = Person('tom')
print(tom.age) # 3
print(tom.name) # tom
print(Person.age) # 3

# 特殊属性
# __name__ 含义：对象名
print("Person.__name__", Person.__name__) # Person.__name__ Person

# __doc__ 含义：类的文档字符串

# __module__ 含义：类定义所在的模块
print("Person.__module__", Person.__module__) # Person.__module__ __main__

# __class__ 含义：对象所属的类
print("tom.__class__", tom.__class__) # tom.__class__ <class '__main__.Person'>

# __dict__ 含义：类或对象的属性字典
print("Person.__dict__", Person.__dict__) # 类字典
# Person.__dict__ {
# '__module__': '__main__',
# 'age': 3,
# '__init__': <function Person.__init__ at 0x000001D3D3D3A670>,
# 'showme': <function Person.showme at 0x000001D3D3D3A700>,
# '__dict__': <attribute '__dict__' of 'Person' objects>,
# '__weakref__': <attribute '__weakref__' of 'Person' objects>,
# '__doc__': None
# }

# __weakref__ 含义：对象的弱引用, 弱引用不会增加对象的引用计数，当对象的引用计数为0时，对象会被销毁

# __qualname__ 含义：类的限定名, 限定名是指类的全名，包括模块名
print("Person.__qualname__", Person.__qualname__) # Person.__qualname__ Person

print(Person.__class__, type(Person), type(int)) # <class 'type'> <class 'type'> <class 'type'>
# type是所有类的元类，所有类都是type的实例


print(tom.__dict__) # 实例字典, {'name': 'tom'}

# 可以动态的为实例和类添加属性


class A:
    # 普通函数定义，这种定义禁用
    def general_function():
        print('general_function')

A.general_function() # general_function, 类调用方法时，不需要传入self参数
a = A()
# 方法绑定,一旦调佣a，就会自动将a绑定到方法的第一个参数self上
# a.general_function() # TypeError: general_function() takes 0 positional arguments but 1 was given, 实例调用方法时，需要传入self参数


class B:
    # 普通方法定义,这种方法最好实例调用
    def showme(self):
        print('我是普通方法：me={}'.format(self))

b = B()
b.showme() # 我是普通方法：me=<__main__.B object at 0x000001D3D3D3A4C0>


# 类方法装饰器装饰过的方法,使用实例或者类访问方法时，会绑定当前类
# 调用时会自动注入第一参数为当前类
class C:
    # 用的不多，通常在通过实例或者类访问方法时，方法内只需要类就可以的时候，通常是工具方法
    @classmethod   #内建装饰器，将普通方法转换为类方法,test = classmethod(test)
    def test(cls):
        print('test', cls)

C.test() # test <class '__main__.C'>

c = C()
print(c.test()) # test <class '__main__.C'>, 实例调用方法时，也会绑定到类上

# 静态方法
class D:
    # 静态方法装饰器，将普通方法转换为静态方法，使用很少，通常是工具方法
    # 静态方法只能说明这个方法和类有关系，但是不需要绑定到类或者实例上
    @staticmethod
    def test():
        print('i am static method')

z = D()
z.test() # i am static method, 静态方法不会绑定到类或者实例上

# 访问控制
## public # 默认, 公有的, 可以在类的内部和外部访问
## protected ：_<name> 保护的，只能在类的内部和子类中访问,python没有实现，社区定义的，等效于public
## private：__<name> 私有的，只能在类的内部访问

# private
# __<name> 包括类属性，实例属性，都属于私有的，仅限于类内部访问,私有的属性和方法，统一叫做私有member成员
class Person:
    def __init__(self, name, age=20):
        self.__name = name  # 私有属性，只能在类内部访问
        self.__age = age
    def __showme(self): # 私有方法，只能在类内部访问
        return 'name={}, age={}'.format(self.__name, self.__age)
    def showme(self):
        # 对__showme进行封装，外部调用showme方法，间接调用__showme方法，这样就可以访问私有方法，并对其增强
        r = '** {} **'.format(self.__showme())
        return r

tom = Person('Tom')

#print(tom.__age) # AttributeError: 'Person' object has no attribute '__age'

print(tom.showme()) # ** name=Tom, age=20 **

# 通过__dict__查看私有变量
print(tom.__dict__) # output: {'_Person__name': 'Tom', '_Person__age': 20}, 私有属性会被改名，_类名__属性名,因此无法直接访问

# public
class Person:
    def __init__(self, name, age=18):
        self.__name = name   # 私有成员
        self.__age = age
    def showme(self):
        return 'name={}, age={}'.format(self.__name, self.__age)


jerry = Person('jerry', 20)
jerry_age = 30
print(jerry.__dict__) # {'_Person__name': 'jerry', '_Person__age': 20}, 私有属性会被改名，_类名__属性名,因此无法直接访问
print(jerry._Person__name) # jerry, 通过这种方式可以访问私有属性,但是不推荐

# protected
class Person:
    def __init__(self, name, age=18):
        self._name = name  # 保护成员
        self._age = age
    def showme(self):
        return 'name={}, age={}'.format(self._name, self._age)

jerry = Person('jerry', 20)
print(jerry._name) # jerry, 保护成员可以直

print(jerry.__dict__) # {'_name': 'jerry', '_age': 20}, 保护成员不会被改名，可以直接访问

## 保护成员不是python的语法，是社区约定的，实际上是public的，可以直接访

