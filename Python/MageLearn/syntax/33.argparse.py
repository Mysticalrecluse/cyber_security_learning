# argparse模块
# argparse模块是python3.2版本新增的一个命令行解析模块，用于解析命令行参数。

import sys
print(sys.argv[0]) # /home/python/project/learn/syntax/33.argparse.py
print("========================================================")

# sys.argv是一个列表，包含了命令行参数
# sys.argv的作用是获取命令行参数，sys.argv[0]是脚本名称，sys.argv[1:]是脚本的参数

# argparse模块的使用步骤：
# 创建一个ArgumentParser对象
# 调用add_argument()方法添加参数
# 使用parse_args()解析参数

# 其目的是为了更方便的解析命令行参数，提供了更多的功能，比如自动生成帮助信息，支持子命令等

import argparse

# ArgumentParser()创建一个ArgumentParser对象
# ArgumentParser(
# prog=None, # 程序的名称，默认是sys.argv[0]
# usage=None, # 描述程序用途的字符串，默认是从add_argument()中生成
# description=None, # 描述程序的字符串，默认是None
# epilog=None,
# parents=[],
# formatter_class=argparse.HelpFormatter,
# prefix_chars='-',
# fromfile_prefix_chars=None,
# argument_default=None,
# conflict_handler='error',
# add_help=True, # 是否添加-h/--help选项，默认是True
# allow_abbrev=True)
parser = argparse.ArgumentParser('ls', description='show file list', add_help=False) # argparse.ArgumentParser()创建一个ArgumentParser对象

# parser.print_help() # 打印帮助信息

# parser.parse_args()解析参数
# parse_args(args=None, namespace=None) -> Namespace
# args: 要解析的参数列表，默认是sys.argv[1:]
# namespace: 一个可选的Namespace对象，用于存储解析的结果
# 返回一个Namespace对象，包含解析的结果

#x = parser.parse_args(['-l', '-a'])
#print(type(x), x) # <class 'argparse.Namespace'> Namespace()

# add_argument()添加参数
# add_argument(
# name or flags..., # 参数的名称或者选项
# action=None,
# nargs=None,
# const=None,
# default=None,
# type=None,
# choices=None,
# required=False,
# help=None,
# metavar=None,
# dest=None)
# name or flags: 参数的名称或者选项
# action: 参数的行为，默认是store
# nargs: 参数的数量，默认是1, 0表示不需要参数，'+'表示1到多个参数，'*'表示0到多个参数
# const: 保存的常量
# default: 默认值
# )

# parser.add_argument() # 添加参数
# parser.add_argument(
# '-l', # 参数的名称
# '--long', # 参数的选项
# action='store_true', # 参数的行为，默认是store
# help='show long list') # 参数的帮助信息
# )

parser.add_argument('path1', nargs='?', default='.') # 位置参数，必须传入
parser.add_argument('-l', '--list',action='store_true', help='show list')
parser.add_argument('-a', '--all',action='store_true', dest='longfmt', help='long format string')
# 可选参数，不传入时，默认为False,传入时为True,默认是store,存储参数值
# store_true: 如果传入了参数，则为True，否则为False
# store_false: 如果传入了参数，则为False，否则为True
# store_const: 保存const参数的值, const参数默认是None
# 示例：parser.add_argument('-f', action='store_const', const = 200, help='show list')
# 相当于给-f参数赋值200
# 结合prac_argparse.py中的例子，进行学习

# dest: 存储参数的属性名称，默认是参数的名称


parser.print_help() # 打印帮助信息
print('=' * 30)

# parser.parse_args()解析参数,返回一个Namespace对象，包含解析的结果
args = parser.parse_args(['/etc', '-l'])
print(args) # Namespace(l=' 123', path1='/etc')
print(args.longfmt, args.path1) # False True /etc

from pathlib import Path
filename = '/etc'
p = Path(filename)
print(p.stat())
print(p.group())
print(p.owner())




