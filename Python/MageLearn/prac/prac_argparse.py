import argparse
from argparse import ArgumentParser
import sys

# 拿到脚本参数

print(sys.argv[1:]) # 终端执行 python prac/prac_argparse.py --help
# 输出 ['--help']
describe="""
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
This my test!
"""

parse = argparse.ArgumentParser('ls',
description=describe,
formatter_class=argparse.RawTextHelpFormatter,
add_help=True) # 创建一个ArgumentParser对象
# -h ,human-readable
# add_help建议设置False,后续自己添加-h/--help选项
# formatter_class=argparse.RawTextHelpFormatter, 保留换行，十分有用

# prog=None, # 程序的名称，默认是sys.argv[0]
# usage=None, # 描述程序用途的字符串，默认是从add_argument()中生成
# description=None, # 描述程序的字符串，默认是None
# epilog=None, # 描述程序的结尾字符串，默认是None
# argument_default=None, # 参数的默认值，默认是None

# parser.parse_args()解析参数

# 控制，实现对参数的解析，如果参数不存在，返回None，如果参数存在，返回一个Namespace对象
# parse_args(args=None, namespace=None) -> Namespace
# args: 要解析的参数列表，默认是sys.argv[1:],如果没有定义列表中的参数，返回None，并打印error信息


# 添加参数
# add_argument(
# name or flags..., # 参数的名称或者选项 位置参数
# action=None, # 参数的行为，默认是store
# nargs=None, # 参数的数量，默认是1, 0表示不需要参数，'+'表示1到多个参数，'*'表示0到多个参数
# const=None, # 保存的常量
# default=None, # 默认值
# type=None, # 类型
# choices=None, # 选项
# required=False, # 是否必须
# help=None, # 帮助信息
# metavar=None, # 参数的名称
# dest=None) # 参数的目标
# name or flags: 参数的名称或者选项
# action: 参数的行为，默认是store
# nargs: 参数的数量，默认是1, 0表示不需要参数，'+'表示1到多个参数，'*'表示0到多个参数
# const: 保存的常量
# default: 默认值
#)


# 位置参数
parse.add_argument('path1') # 位置参数，必须传入
# x = parse.parse_args(['abc']) # 也可以这样传入参数
#parse.add_argument('-l',nargs='?',default='.') # 可选参数，0或1个参数
#parse.add_argument('path2', nargs='*', default='.') # 位置参数，0到多个参数
#parse.add_argument('path3', nargs='+', default='.') # 位置参数，1到多个参数
#parse.add_argument('path4', nargs='2', default='.') # ls [-h] path4 path4

parse.add_argument('-a', help='all thing') # 可选参数, 传入-a,ls [-h] [-a A], 传入-a 1, -a 后面必须跟一个参数

parse.add_argument('-l', nargs="?"), # 可选参数，0或1个参数，-l = 一个参数或none

parse.add_argument('-i', '--inode', action='store_true') # 可选参数，传入-i,ls [-h] [-i]

# help: 参数的帮助信息

x = parse.parse_args() # 执行python3 prac/prac_argparse.py abc
print(x) # Namespace(path='abc')
parse.print_help() # 打印帮助信息,并退出

# 使用传参的数值进行操作
print(x.l)
print(x.path1)