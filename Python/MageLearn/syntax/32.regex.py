# 正则表达式
'''
# 元字符
.       匹配任意字符,除了换行符之外
[abc]   匹配a或b或c
[^abc]  匹配除a,b,c之外的任意字符
[a-z]   匹配a到z之间的任意字符

\b  匹配单词边界
\B  匹配非单词边界
\d  匹配数字字符
\D  匹配非数字字符
\s  匹配空白字符
\S  匹配非空白字符
\w  匹配单词字符数字
\W  匹配非单词字符数字

# 量词
*   0-无数个
+   1-无数个
？  0 或 1个
{N} N次
{0，}   *
{1，}   +
{0,1}   ?

# 或
x | y   匹配x或者y

# 分组引用
## 分组
(pattern)

## 引用
\数字 $数字

## 取消分组
(?:pattern)

## 命名分组
(?<name>exp)
(?'name'exp)  后续可以使用命名的分组
(?P<name>exp)  re中使用命名分组，需要加P

# 断言
## 零宽断言
(?=exp)   断言exp一定在匹配的右边出现，也就是说断言后面一定跟个exp, f(?=oo) f后面一定有oo出现
(?<=exp)  断言exp一定出现在匹配的左边出现，也就是说前面一定有个exp前缀，(?<=f)ood、(?<=t)ook分别匹配ood，ook,ook前一定t出现

## 负向零宽断言
(?!exp)   零宽度负预测先行断言，断言exp一定不会出现在右侧
(?<!exp)   零宽度负回顾后发断言，断言exp一定不能出现在左侧

# 注释
(?#commnet)   示例f(?=oo)(?#这个后断言不捕获)

# 贪婪
默认贪婪
在量词后面加？表示非贪婪，匹配最少
示例：v.*?y  匹配very very soory 匹配2次，两个very，因为是非贪婪模式

#引擎选项
IgnoreCase   匹配时忽略大小写                                                         python: re.l re.IGNORECASE
Singleline   单行模式，可以匹配所有字符，包括\n，表示dotall，使.能够匹配\n                   python: re.S  re.DOTALL
Multiline    多行模式 ^行首、$行尾                                                    python: re.M  re.MULTILINE
IgnorePatternWhitespace   忽略表达式中的空白字符，如果要使用空白字符用转移，#可以用来做注释    python: re.X  re.VERBOSE

# 普通模式：就是一个长长的字符串
# 多行模式，普通模式改为以\n为换行的多行文本，只影响^$
# 单行模式：DOTALL,一串到底
'''

# re模块
import re

# 如果多个模式共存，可以使用|分隔
# eg:re.I|re.M

s = "bottle\nbag\napple"

# 先编译
# re.compile(pattern, flags=0),返回一个正则表达式对象
# 作用是将正则表达式编译成一个正则表达式对象，以便在后面的匹配中复用
regex = re.compile('\d')


# 单次匹配
# match(pattern, string, flags=0, pos=0, endpos=0) # pos, endpos, 从pos到endpos匹配
m = re.match('b', s, re.M) # 匹配开头
print(type(m), m) # <class 're.Match'> <re.Match object; span=(0, 1), match='b'>

# 全文搜索，findall()返回一个列表
# findall(pattern, string, flags=0, pos=0, endpos=0) # 返回一个列表
m = re.findall('b\w+', s, re.M)
# regex = re.compile('b\w+')
# m = regex.findall(s)
# print(type(m), m) # <class 'list'> ['bottle', 'bag']
print(type(m), m) # <class 'list'> ['bottle', 'bag']

# search()返回一个匹配对象,在字符串中搜索匹配，从0或指定位置开始，向后搜索，返回第一个匹配的对象
# fullmatch()返回一个匹配对象,从字符串开头到结尾匹配,类似贪婪模式
# finditer()返回一个迭代器，迭代器中的每个元素是一个匹配对象

m = re.finditer('b\w+', s, re.M)
print(type(m), m)
for i in m:
    print(type(i), i, i[0], i.start(), i.end(), i.string)
    # <class 're.Match'> <re.Match object; span=(0, 6), match='bottle'> bottle 0 6 bottle
    # i.string的意思是匹配的字符串，这里是s
    # i.start()匹配的开始位置
    # i.end()匹配的结束位置

# 匹配替换
x = re.sub('b\w', 'MMM', s, re.M) # 替换所有匹配的字符串
print(type(x), x) # <class 'str'> MMottle\nMMag\napple

x = re.subn('b\w', 'MMM', s, re.M) # 返回一个元组，第一个元素是替换后的字符串，第二个元素是替换次数
# re.subn(pattern, repl, string, count=0, flags=0)
print(type(x), x)

# 分组
m = re.search('(b\w+)', s)
print(type(m), m) # <class 're.Match'> <re.Match object; span=(0, 6), match='bottle'>
print(m.groups()) # ('bottle',),groups()返回一个元组,元组中是匹配的字符串
print(m.group(0)) # bottle,group(0)返回匹配的字符串


# 分组匹配,如果有多个分组，返回一个元组，如果1组，返回一个字符串
x = re.findall('(b)(\w+)', s)
for i in x:
    print(i) # ('b', 'ottle') ('b', 'ag'),返回一个元组，元组中是分组匹配的字符串

x = re.finditer('(b)(\w+)', s)
for i in x:
    print(i.groups(), i.group(0), i.group(1), i.group(2)) # ('b', 'ottle') bottle b ottle

x = re.match('(?P<name1>b\w+)\s(?P<name2>b\w+)', s)
print(x.groups())
print(x.groupdict()) # {'name1': 'bottle', 'name2': 'bag'}
print(x.group('name2'), x['name1']) # bag bottle

# 字符切割
s = """\
os.path.abspath(path)
normpath(join(os.getcwd(), path)).
"""

x = re.split('[.(),\s]+', s) # 返回一个列表
#['os', 'path', 'abspath', 'path', 'normpath', 'join', 'os', 'getcwd', 'path', '']
print(x)

print(*filter(None, re.split('[.(),\s]+', s))) # filter(None, list)过滤掉空字符串
# None 表示过滤掉空字符串，返回一个迭代器


