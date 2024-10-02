# python中字符串是比字符数组更高级的数据结构
# 字符串是不可变的，字符串的内容不能被修改，可以通过组合，切片，连接等操作来生成新的字符串

# 字符串可以通过索引访问
s = 'hello'
print(s[0])  # h

# 创建字符串
# 单引号
s = 'hello'
print(type(s)) # <class 'str'>
s = 'i said \'wow\''
print(s) # i said 'wow'
# 双引号
s = "hello"
print(type(s)) # <class 'str'>

# 结尾 \
quote = "Linus Torvalds once said, \
'Any program is only as good as it is useful.'"
print(quote)

# python3中字符串是unicode编码的,这意味着你可以使用几乎任何语言的字符，甚至是emoji

# 多行字符串, 使用三个单引号或者双引号
s = '''hello
world'''
print(s)

# str() 构造函数，将其他类型转换为字符串
s = str(42)
print(s) # 42
print(type(s)) # <class 'str'>

# 切片slice
# s[start:end:step]
b = "hello, world"
print(b[2:5]) # llo, 理解小技巧：end是不包含的,可以理解为个数
print(b[2:10:2]) # lo o, ; 2是步长

# 字符串的内部实现
# 1. 结构： python中的字符串是由PyUnicodeObject结构体表示的，这个结构体包含了许多与字符串相关的信息
# 比如：字符串的长度，字符串的引用计数，字符串的hash值等，实际数据的指针等

# 2. 存储： Python的字符串以不同的编码方式存储在内存中，这些编码方式包括ASCII，UTF-8，UTF-16等
# 在Python3中，字符串是以Unicode编码存储的，这意味着Python3中的字符串是不定长的，不同的字符占用不同的字节数

# 3. 不可变性： Python中的字符串是不可变的，这意味着字符串的内容不能被修改，可以通过组合，切片，连接等操作来生成新的字符串

# 4. 内部哈希： Python中的字符串是不可变的，所以他们的hash值可以在创建时计算出来并且缓存起来，这样可以提高字典的查找效率

# 5. 字符串驻留：为了提高效率和内存使用，Python使用了一个技术叫做字符串驻留，字符串驻留是指Python在内存中缓存了一些字符串对象
# 这样当你创建一个新的字符串对象时，Python会首先检查缓存中是否已经存在相同值的字符串对象，如果存在，那么就会重用这个对象
# 这样可以节省内存,这主要通过sys.intern()函数来实现

# 6. 字符串方法： Python中的字符串是一个类，所以它有很多方法可以调用, 这些方法都是在底层C语言实现的，所以效率很高
