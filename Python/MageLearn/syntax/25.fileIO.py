# 文件IO操作
# open() 函数, 说明：打开
# read() 函数, 说明：读取
# write() 函数, 说明：写入
# close() 函数, 说明：关闭
# readline() 函数, 说明：读取一行
# readlines() 函数, 说明：读取多行

import os,inspect
print(os.path.abspath(__file__))

print(open('IOtest.txt'))   # 文件对象

f = open('IOtest.txt')
# <_io.TextIOWrapper name='IOtest.txt' mode='r' encoding='UTF-8'>
print(str(inspect.signature(open)).replace(',','\n')) # (file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) -> TextIO
'''
(file
 mode='r'
 buffering=-1
 encoding=None
 errors=None
 newline=None
 closefd=True
 opener=None) -> TextIO
'''

# mode: r, w, a, b, t, +, x
# 主模式：r, w, a, x    只能读或者写，不能同时读写
# mode = r, 只读，读取文件, 文件存在：OK, 文件不存在：FileNotFoundError
# mode = w, 只写，写入文件, 文件存在："清空"文件内容，文件不存在：创建文件
# mode = a, 追加，只写，写入文件, 文件存在：在文件末尾追加内容，文件不存在：创建文件
# mode = x, 创建，只写，写入文件, 文件存在：FileExistsError, 文件不存在：创建文件

# 次模式：b, t, +    可以和主模式组合使用, 但是次模式不能单独使用
# mode = t, 文本模式，默认模式, 读写的是字符串
# mode = b, 二进制模式, 读写的是字节
# mode = +, 读写模式, 可读可写

# 组合
# mode = r+， 读写，文件存在：OK, 文件不存在：FileNotFoundError, 读写文件，文件指针在文件开头
# 文件指针：指向文件中的某个位置，读写文件时，文件指针会移动
# mode = w+, 读写，文件存在："清空"文件内容，文件不存在：创建文件, 读写文件，文件指针在文件开头，内容为空
print(f.readable()) # True, 是否可读
print(f.writable()) # False, 是否可写
f.close() # 关闭文件, 释放资源，分别做了flush,归还文件描述符，关闭文件

print(f.closed) # True, 表示文件已经关闭

f1 = open("test2.txt","a")
f1.write("hello, world\n")
print(f1.readable()) # False
print(f1.writable()) # True
print(os.path.abspath(f1.name))
f1.close()

f1 = open("test2.txt","wb")
f1.write(b"hello, world\n")
f1.close()

# 调整文件指针
# seek(offset, whence), 调整文件指针, offset: 偏移量, whence: 从哪里开始偏移
# whence: 0, 文件开头, 1, 当前位置, 2, 文件末尾, 默认值是0

# tell() 函数, 获取文件指针的位置, 返回值是一个整数
# seek() 和 tell() 都是以字节为单位进行指针的移动和获取

f1 = open("test2.txt","r+")
print(f1.tell()) # 0
print(f1.read()) # hello
print(f1.tell()) # 13

f1.seek(0, 0) # 从文件开头偏移0个字节
print(f1.tell()) # 0
f1.write("world")
print(f1.tell()) # 5

f1.seek(0, 0)
print(f1.read()) # world, world


f2 = open("IOtest.txt","w+")
f2.write("world\nhello")
f2.seek(0, 0)
print(f2.readline()) # world
print(f2.readline()) # hello
f2.close()

# readline() 函数, 读取一行
# readlines() 函数, 读取多行

f3 = open("IOtest.txt","r")
print(f3.readlines()) # ['world\n', 'hello']
# f3.readlines()返回值是一个列表，列表中的每一个元素是文件中的一行
f3.close()

# 上下文管理 context manager
# with open() as f:

