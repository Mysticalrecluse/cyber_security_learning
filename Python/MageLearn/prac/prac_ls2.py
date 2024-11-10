import argparse
from datetime import datetime
from pathlib import Path

name = 'ls'
describe=""""
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
This my test!
"""
parse = argparse.ArgumentParser(prog=name,
                                description=describe,
                                formatter_class=argparse.RawTextHelpFormatter,
                                add_help=False
                                )


parse.add_argument('path',nargs='?',default='.', help='dir name')
parse.add_argument('-a', '--all', action='store_true', dest='all', help='do not ignore entries starting with .')
parse.add_argument('-l', '--list', action='store_true', dest='list', help='use a long listing format')
parse.add_argument('-i', '--inode', action='store_true', dest='inode', help='print the index number of each file')
parse.add_argument('-r', '--reverse', action='store_true', dest='reverse', help='print the index number of each file')

args = parse.parse_args()


# 判断该目录是否存在

# 列出指定路径下的文件
def listdir(path, all=False):
    p = Path(path)
    for f in p.iterdir():
        if not all and f.name.startswith('.'):
            continue
        # print(str(f.name))
        yield f.name
   # yield from (f.name for f in p.iterdir() if all or not f.name.startswith('.'))
   # yield from map(lambda x: x.name, filter(lambda f: all or not f.name.startswith('.'), p.iterdir()))


# 显示长格式
def listdir(path, all=False, list=False, reverse=False):
    def _listdir(path, all, list):
        p = Path(path)
        for f in p.iterdir():
            if not all and f.name.startswith('.'):
                continue
            if list:
                st = f.stat()
                import stat
                mode = stat.filemode(st.st_mode)
                yield (mode, st.st_nlink, st.st_uid, st.st_gid, st.st_size, datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S"), f.name)
            else:
                yield f.name
    yield from sorted(_listdir(path, all, list), key=lambda x: x[-1], reverse=reverse)

print(*(listdir(args.path, all=args.all, list=args.list, reverse=args.reverse)), sep='\n')
