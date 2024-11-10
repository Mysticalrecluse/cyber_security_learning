# pathlib.Path类
# Path对象是一个纯面向对象的路径操作类，它的实例可以代表文件系统中的文件或目录。
# Path对象的方法和属性可以让我们更方便地操作文件和目录。
from formatter import NullWriter
from pathlib import Path

print(Path()) # . , 当前目录

print(type(Path())) # <class 'pathlib.PosixPath'>, PosixPath是Path的子类
# Path() 等价于 Path('.'),Path('') 表示当前目录

# 路径拼接
print(Path('/etc', 'passwd')) # /etc/passwd
print(Path('/etc') / 'passwd') # /etc/passwd

p1 = Path('/etc') / 'passwd'
# p1是repr的结果,repr是一个内建函数，它返回一个对象的字符串表示形式。
print(type(p1), p1) # <class 'pathlib.PosixPath'> /etc/passwd
print(str(p1)) # /etc/passwd

print(p1.parent) # /etc

p1 = p1 / 'test'/ 'test1'/ 'test2.txt'
print(p1) # /etc/passwd/test/test1/test2
print(p1.parent.parent) # /etc/passwd/test

p2 = p1.joinpath('a/b/c') # 返回一个新的Path对象,不会改变原来的Path对象
print(p2) # /etc/passwd/test/test1/test2/a/b/c
print(type(p1), p1) # <class 'pathlib.PosixPath'> /etc/passwd/test/test1/test2

# 打印后缀
print(p1.suffix) # .txt
# 打印文件后缀名前面的部分
print(p1.stem) # test2

# 文件名 = stem + suffix

# 打印基名
print(p1.name) # test2 ,返回字符串

print(p1) # /etc/passwd/test/test1/test2.txt

# with_name() 方法，替换文件名
print(p1.with_name('test3.txt')) # /etc/passwd/test/test1/test3.txt

print("-------------------------")
# parents属性，返回值不是生成器，而是一个路径对象，可迭代，可以使用for循环

print(p1.parents) # <PosixPath.parents>
for parent in p1.parents:
    print(parent, type(parent))

# 扩展：print() 等价于 print(str()), repr() 等价于 print(repr())

# 变量注解
p1:Path = Path('/etc') / 'passwd'
print(p1) # /etc/passwd

# 全局方法
# Path.cwd() 返回当前工作目录
# Path.home() 返回当前用户的家目录
print(Path.cwd()) # /home/python/project/learn/syntax
print(Path.home()) # /home/python

# Path.exists() 判断路径是否存在

# Path.is_dir() 判断是否是目录
# Path.is_file() 判断是否是文件
# Path.is_symlink() 判断是否是符号链接
# Path.is_block_device() 判断是否是块设备
# 默认情况下，如果路径不存在，is_dir() 和 is_file() 都会返回 False，会拼接路径cwd进行判断
# Path.is_absolute() 判断是否是绝对路径

# Path.mkdir() 创建目录
# Path.mkdir(parents=True, exist_ok=True) 创建多级目录 等价于mkdir -p , exist_ok=True表示如果目录已经存在，不会报错
# Path.rmdir() 删除目录
# Path.resolve() 返回绝对路径,解析符号链接,返回一个新的Path对象,不会改变原来的Path对象,递归解析符号链接

# (p1 / 'mysql.ini').touch() 创建文件

# 遍历
p2 = Path('/home/python/project/learn/syntax')
p3 = p2.parent.iterdir() # 返回一个迭代器，遍历目录下的文件和目录, 不会递归遍历
next(p3)
print([i for i in next(p3).iterdir()] == False) # False表示不为空

print('--------------------------------------------------')
# 判断一个目录下的目录是否为空
for x in Path('/home/python/project/learn').iterdir():
    if x.is_dir():
        print(x.name, 'dir')
        for y in x.iterdir():
            print(y.name, 'not empty')
            break;
        else:
            print(x.name, 'empty')
    else:
        print(x.name, 'file')


# 通配符
print('--------------------------------------------------')
p4 = Path('/home/python/project/learn')
print(type(p4.glob('*'))) # <class 'generator'>
print(list(p4.glob('*'))) # 返回一个列表，包含所有的文件和目录
print([i.name for i in p4.glob('**/*')]) # **表示递归遍历

print(list(p4.glob('**/*.py'))) # 递归遍历，返回所有的.py文件

# 通配符
# ? 匹配一个字符
# * 匹配0个或多个字符
# [abc] 匹配a或b或c

# p4.rglob('*') 等价于 p4.glob('**/*')，rglob()是glob()的递归版本

# stat() 返回一个stat_result对象，包含文件的元数据信息
