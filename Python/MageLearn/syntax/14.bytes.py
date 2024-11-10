# 字节序列
# bytes, bytearray
# bytes: 不可变序列
# bytearray: 可变序列

# 编码与解码
# 编码: 字符串 -> 字节序列
# 解码: 字节序列 -> 字符串

# encode()
print("abc".encode())   # 缺省为utf-8编码
print("啊".encode('utf-8'))

# decode()
print(b'abc'.decode('utf-8')) # 缺省为utf-8解码

# 空bytes
print(bytes()) # b''

# bytes()
print(bytes(5)) # b'\x00\x00\x00\x00\x00', 5个0字节

# bytes(可迭代对象)
# 可迭代对象中的元素必须是0-255之间的整数
# 0-255之间的整数对应ascll码表
print(bytes([65, 66, 67])) # b'ABC'
print(bytes(range(0x61,0x64))) # b'abc'

# bytes(字符串, 编码)
print(bytes("abc", 'utf-8')) # b'abc'

# bytes()，字节序列中取值，一般为0-255之间的整数
b1 = bytes(range(0x61,0x64))
print(b1[0]) # 97
print(type(b1[1])) # <class 'int'>

print('abc' == b'abc') # False

# unicode 两字节
# utf-8 三字节
# gbk 两字节

# python3中字符串是unicode编码

# 常用ascll编码：
# 0x00 -> Null
# 0x20 -> 空格
# 0x0a -> 换行'\n'
# 0x0d -> 回车'\r'
# 0x09 -> 制表符'\t'
# 0x31 -> '1'
# 0x41 -> 'A'
# 0x61 -> 'a'

# bytearray 可变序列
# bytearray() -> bytearray
# bytearray(可迭代对象) -> bytearray
# bytearray(整数) -> bytearray
# bytearray(字符串, 编码) -> bytearray
# bytearray(字节序列) -> bytearray
# bytearray(字节序列, 编码) -> bytearray
# bytearray(字节序列, 编码, errors) -> bytearray
b2 = b'abc'
b2 = bytearray(b2)
print(b2) # bytearray(b'abc')

b2.append(67)
print(b2) # b'abcC'

b2.extend(range(0x64, 0x67))
print(b2) # bytearray(b'abcCdef')


