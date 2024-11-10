# os.path模块
# os模块常用的函数
import os
from os import path

print(path)
# <module 'posixpath' from '/home/python/.pyenv/versions/3.8.16/lib/python3.8/posixpath.py'>
print(os.path is path) # True
p = path.join('/etc', 'passwd') # 拼接路径
print(type(p), p) # <class 'str'> /etc/passwd
print(path.exists(p)) # True, 判断路径是否存在

print(path.split(p)) # ('/etc', 'passwd'), 拆分路径, 返回元组
# print(path.splitdrive('o:/temp/test')) # windows方法，
print(path.dirname(p), path.basename(p)) # /etc passwd, 返回路径和文件名

print(path.abspath(''), path.abspath('.')) # 绝对路径, 返回当前目录的绝对路径
# /home/python/project/learn/syntax /home/python/project/learn/syntax

print(path.isdir('/etc')) # True, 判断是否是目录
print(path.isfile('/etc')) # False, 判断是否是文件
print(path.isabs('/etc')) # True, 判断是否是绝对路径


# 扩展
# 当前模块的名称
print(__name__) # __main__
# 当前模块的路径
print(__file__) # syntax/26.os_path_module.py

print("----------------------")

parent = path.dirname(__file__)

while parent != '/':
    print(parent)
    parent = path.dirname(parent)

