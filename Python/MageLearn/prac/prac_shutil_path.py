import os
import random
from pathlib import Path
from shutil import copyfile, copytree, rmtree

p = Path.cwd()
Path.mkdir(p/'a'/'b'/'c'/'d', exist_ok=True, parents=True) # parents=True, 递归创建目录, exist_ok=True, 目录存在不报错

print(bytes(range(97,100)).decode('ascii'))


for i in range(50):
    list_x = [random.randrange(97, 123) for i in range(4)]
    random_str = str(bytes(list_x).decode('ascii'))
    (p/'a'/random_str).touch()
    (p/'a'/'b'/random_str).touch()
    (p/'a'/'b'/'c'/random_str).touch()
    (p/'a'/'b'/'c'/'d'/random_str).touch()

def fn(x, y):
    s = set()
    for name in set(y):
        # 非x, y, z开头文件
        if not name.startswith(('x', 'y', 'z')):
            s.add(name)
            # 集合中排除a,b,c
            if name in ('a', 'b', 'c', 'd'):
                s.remove(name)
    return s

copytree(p/'a', p/'dest',ignore=fn)







