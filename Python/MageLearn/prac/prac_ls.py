import argparse
from pathlib import Path


name = 'ls'
describe = """
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
"""

parse = argparse.ArgumentParser(
    prog=name,
    description=describe,
    formatter_class=argparse.RawTextHelpFormatter,
    add_help=False
)

parse.add_argument('path', nargs='?', default='.')
parse.add_argument('-a',
                   '--all',
                   action='store_true',
                   dest='all',
                   help='do not ignore entries starting with .'
                   )

parse.add_argument('-d',
                   '--directory',
                   action='store_true',
                   dest='directory',
                   help='list directories themselves, not their contents'
                   )


parse.add_argument('-i',
                   '--inode',
                   action='store_true',
                   dest='inode',
                   help='print the index number of each file'
                   )


parse.add_argument('-l',
                   '--list',
                   action='store_true',
                   dest='list',
                   help='use a long listing format'
                   )

parse.add_argument('--help',
                   action='store_true',
                   dest='help',
                   help=' show this help message and exit'
                   )

#parse.print_help()

args = parse.parse_args()

# 给real_path，赋值路径
if (args.path == '.'):
    real_path=Path.cwd()
else:
    real_path=args.path

def output_all():
    p = Path(real_path).iterdir()
    for x in p:
        print("%s%s\t"%(x.stem, x.suffix), end=" ")
    print("")

def output_default():
    p = Path(real_path).iterdir()
    for x in p:
        if (x.stem[0] == "." ):
            continue
        else:
            print("%s%s\t" % (x.stem, x.suffix), end=" ")
    print("")


if args.all:
    output_all()

if args.help:
    parse.print_help()

if args.directory:
    p = Path(real_path).iterdir()
    for x in p:
        if x.is_dir():
            print("%s%s"%(x.stem,x.suffix), end="\t")
    print("")

if args.all or args.directory or args.help or args.list or args.inode:
    pass
else:
    output_default()