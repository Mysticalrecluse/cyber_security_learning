# 序列化和反序列化

# 序列化serialization  数据结构 -> 二进制
# 把变量从内存中变成可存储或传输的过程称之为序列化

# 反序列化deserialization  二进制 -> 数据结构

# Python提供了pickle模块来实现序列化

# pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None) 将对象obj保存到文件file中去
# pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None) 将对象序列化为bytes对象
# pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None) 从文件中读取一个字符串，并将它重构为原来的python对象
# pickle.loads(data, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None) 从bytes对象中读取一个字符串，并将它重构为原来的python对象

# 序列化应用
# 一般来说，本地序列化的情况，应用较少，一般用于网络传输，或者存储到数据库中
# 将数据序列化后通过网络传输到远程节点，远程服务器上的服务将接收到的数据反序列化后，进行处理
# 要注意一点，远程接收端，反序列化时必须有对应的数据类型，否则会报错
# 大多数项目都不是单机的，也不是单服务的，需要多个程序之间配合。需要通过网络将数据传送到其他节点上去，这就需要大量的序列化，反序列化过程
# 通常，python程序之间可以都使用pickle模块来序列化和反序列化数据，如果跨平台，跨语言，就需要使用json，xml等其他序列化方式
# 不同协议，效率不同，学习曲线不同，适用场景不同

# 目前来说，字符序列化，json是最常用的序列化方式，因为json是跨平台的，几乎所有语言都支持json
# 二进制序列化，msgpack，protobuf，avro，thrift等，这些都是二进制序列化协议，效率比json高，但是学习曲线陡峭，适用场景有限
# 其中，msgpack是最简单的二进制序列化协议，也是最快的，但是只支持python和ruby



from pathlib import Path
import pickle

"""
# 示例
a = 99
b = 'c'
c = list('abc')
d = {'a': 127, 'b': 'abc', 'c': [1,2,3]}
filename = '/opt/ser.bin'
with open(filename, 'wb') as f:
    pickle.dump(a,f) 
    pickle.dump(b,f) 
    pickle.dump(c,f) 
    pickle.dump(d,f) 
    # 序列化后，依靠协议，将数据序列化后 -> 数据本体必须在，必须有类型，必须有边界

# 反序列化
with open(filename, 'rb') as f:
    a = pickle.load(f)
    b = pickle.load(f)
    c = pickle.load(f)
    d = pickle.load(f)
    print(a,b,c,d)
"""