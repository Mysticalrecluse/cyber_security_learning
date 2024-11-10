import logging
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self._hobby = "coding"
        # 保护变量，不能被外部直接访问，
    
    @property
    def name(self):
        return self.__name

    def say_hello(self):
        print(f"Hello, my name is {self.__name} and I am {self.__age} years old.")


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

john = Person("John", 30)

# 通过__dict__查看私有变量
print(john.__dict__) # output: {'_Person__name': 'John', '_Person__age': 30}

# 不推荐访问保护变量
print(john._hobby) # output: coding
print(john.name) # output: John

# 通过property访问私有变量
print(john.name) # output: John
"""
@property
    def manager(self):
        return self.logger.manager

    @manager.setter
    def manager(self, value):
        self.logger.manager = value
"""


root1 = logging.root
root2 = logging.getLogger()
root3 = logging.Logger.root

print(root1 == root2) # output: True
print(root3 == root2) # output: True


# 简化代码
_loggerClass = logging.Logger

class Manager(object):  # object类是所有类的基类, 可以省略
    def __init__(self, rootnode):
        self.root = rootnode
        self.loggerDict = {}
        self.loggerClass = None

    def getLogger(self, name):
        rv = None
        if name in self.loggerDict:
            rv = self.loggerDict[name]
        else:
            rv = (self.loggerClass or _loggerClass)(name)
            rv.manager = self
            self.loggerDict[name] = rv
        return rv

def getLogger(name=None):
    if name:
        return logging.Logger.manager.getLogger(name)
    else:
        return logging.Logger.manager.root

root = logging.RootLogger(30)
logging.Logger.root = root
logging.Logger.manager = Manager(root)

# 简化代码 - 解析logger.manager
class Logger:
    manager = None  # 初始化管理器

class Manager:
    def __init__(self):
        self.loggerDict = {}  # 存储日志记录器的字典

    def getLogger(self, name):
        if name in self.loggerDict:
            return self.loggerDict[name]
        else:
            logger = Logger()
            self.loggerDict[name] = logger
            return logger

# 初始化管理器
Logger.manager = Manager()

def getLogger(name=None):
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    """
    if name:
        return Logger.manager.getLogger(name)
    else:
        return Logger.manager.root