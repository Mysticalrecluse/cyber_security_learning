x = 'abc'
print(bytes(x, 'utf-8')) # b'abc'

print(bytes(range(97, 100))) # b'abc'

print(bytes([97, 98, 99])) # b'abc'

print(bytes(range(97,100))[0])

"""
bytes(range(97,100))[0] = 65 # TypeError: 'bytes' object does not support item assignment, bytes是不可变序列
"""

print(bytearray(range(97,100))[0]) # 97

y = bytearray(range(97,100))
y[0] = 65 # bytearray是可变序列：w

print(y, type(y)) # bytearray(b'Abc') <class 'bytearray'>

print()