# logging模块
import logging # 模块加载，并且执行模块，模块的顶层代码会被执行

# 重要模块

# 类：Logger，RootLogger(父类：Logger)，Handler，Filter，Formatter

# 1. Logger，日志记录器
# 2. RootLogger，根日志记录器
# 3. Handler，处理器,日志的实际处理者，有众多处理器子类
# 4. Filter，过滤器，在logger实例或Handler实例上过滤日志记录
# 5. Formatter，格式化器，指明日志的最终输出格式


# 1. Logger，日志记录器
logging.info('test info ~~~') # 不会输出，因为默认级别是warning

logging.warning('test warning ~~~') # 输出 WARNING:root:test warning ~~~，输出的内容叫message

log1 = logging.Logger('m1') # logger类 -> 日志记录器
print(log1) # <Logger m1 (NOTSET)>， 表示logger的名字是m1，级别是NOTSET，无设置

log2 = logging.Logger('m1')

print(log2, type(log2))

print(log1 == log2) # False，

log3 = logging.getLogger('m1') # getXXX方法，也叫工厂方法
# 获取logger对象，如果没有就创建一个, 一般使用这种方式获取logger对象, 这样可以保证同一个名字的logger是同一个对象
# 字典m1 -> logger对象
log4 = logging.getLogger('m1') # 获取logger对象，如果没有就创建一个, 一般使用这种方式获取logger对象
print(type(log4)) # <class 'logging.Logger'>，getlogger是logger类的方法，返回的是logger对象
#print(log3) # <Logger m1 (WARNING)>
#print(log4) # <Logger m1 (WARNING)>
#print(log1 == log3) # True
#print(log2 == log3) # True
#
#print(log3 == log4) # True
#print(log3 is log4) # True

#==============================================================================

# 2. RootLogger，根日志记录器
"""
root = RootLogger(WARNING)
Logger.root = root
Logger.manager = Manager(Logger.root) # Logger.manager是一个Manager对象

# WARNING是级别，本质上是常量，是一个整数
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

def getLogger(name=None):
    if name:
        return Logger.manager.getLogger(name)
    else:
        return root
"""

#root = logging.root # root是一个全局变量，是一个RootLogger对象
#root = logging.Logger.root
root = logging.getLogger() # 获取root对象

print("log3", log3, log3.parent, log3.parent is root) # <RootLogger root (WARNING)> True
# log3.parent是root对象，log3.parent是RootLogger对象，是一个全局对象

log5 = logging.getLogger('m1.m2') # m1 -> m2, m1是m2的父logger
print(log3, log5, "log5.parent is log3", log5.parent,log5.parent is log3) # True

## 总结：logger对象之间是有父子关系的，父logger可以传递日志记录给子logger

# 层次关系
# 记录器的名称另一个作用就是表示logger之间的层次关系
# logger的名字是以点号分割的，例如：m1.m2.m3, m1是m2的父logger，m2是m3的父logger


# 级别
# WARNING是级别，本质上是常量，是一个整数
#CRITICAL = 50
#FATAL = CRITICAL
#ERROR = 40
#WARNING = 30
#WARN = WARNING
#INFO = 20
#DEBUG = 10
#NOTSET = 0

## 总共有三种级别：日志消息级别，logger级别， handler级别