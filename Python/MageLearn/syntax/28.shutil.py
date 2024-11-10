# shutil module
# 高级文件操作
# shutil模块提供了一些用于高级文件操作的函数，包括文件的复制、删除、移动等操作。

# Copy复制
import shutil
from shutil import copy, copyfile, copytree, copyfileobj,copy2
from pathlib import Path

# copyfileobj(src, dst)：将文件src复制到文件dst，核心代码，操作文件对象，复制文件内容

# copyfile(src, dst)：判断文件是否相同，不同则复制，相同则不复制，核心调用copyfileobj，操作文件对象，复制文件内容

# copymode(src, dst)：仅复制权限，内容、组、用户均不变

# copy2(src, dst)： copystat(src, dst) + copyfile(src, dst) + copymode(src, dst)：复制文件内容和权限,及其他元数据

# print(Path.cwd(),type(Path.cwd()))
x = (Path.cwd())/'test2.txt'
y = (Path.cwd())/'test3.txt'
print(x,type(x))

print(x.is_file())

copy2('test2.txt','test3.txt')

print(y.is_file())

# copytree(src, dst)：递归复制目录，包括子目录和文件，类似于cp -r命令

# shutil.rmtree()：递归删除目录，类似于rm -rf命令

Path.mkdir(Path.cwd()/'test',exist_ok=True) # 创建目录,exist_ok=True表示如果目录已经存在，不会报错
shutil.rmtree('test')

def fn(x, y):
    print(x, y)
    return set()
src = '/home/python/project/learn/syntax/test1'
dest = '/home/python/project/learn/syntax/test2'
#Path.mkdir(Path.cwd()/'test1'/'subtest1',exist_ok=True) # 创建目录,exist_ok=True表示如果目录已经存在，不会报错
#copytree(src, dest, ignore=fn) # ignore参数，指定一个函数，用于过滤文件，返回一个集合，集合中的文件不会被复制e
# shutil.rmtree('test2', ignore_errors=True) # ignore_errors=True表示如果目录不存在，不会报错)

"""
示例
def fn(x, names):
    s = set()
    for name in names:
        if name.endswith('.py'):
            s.add(name)
    return s # 这里不能是惰性求值，必须是一个集合，否则会返回异常结果
    # 等价于{name for name in names if name.endswith('.py')}
# 复制test1目录到test2目录，过滤掉.py文件:w
copytree('test1', 'test2', ignore=fn)
"""
p4=Path.cwd().parent
print(*p4.rglob('*'),sep='\n')