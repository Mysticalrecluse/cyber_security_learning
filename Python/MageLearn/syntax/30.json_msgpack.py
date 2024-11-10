# JSON
# JSON(Javascript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。
# 采用完全独立于编程语言的文本格式来存储和表示数据

# Json的数据类型
# 值： 字符串(必须用双引号)、数值、对象(复合类型，类似字典,key必须是字符串)、数组、布尔值、null
# Json 有两种数据结构：
# 1. 名称/值对的集合（对象）
# 2. 值的有序列表（数组）

"""
JSON示例
{
  “person” : [
    {
      "name": "tom",
      "age" : 18
    },
    {
      "name": "jerry",
      "age" : 20
    }
  ]
  "total": 2
}
"""

# Json模块
# Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。

import json
import msgpack

d = {'name': 'tom', 'age': 18, 'interest':('music', 'movie'), 'class':['python']}

x = json.dumps(d) # 序列化, 返回字符串

print(x, type(x))

# 反序列化
y = json.loads(x) # 返回字典
print(y, type(y)) # {'name': 'tom', 'age': 18, 'interest': ['music', 'movie'], 'class': ['python']} <class 'dict'>
# 注意，元组被转换为列表，因为json只支持列表,字典，字符串，数字，布尔值，None,不支持元组,集合等,千万注意


# msgpack,二进制序列化协议
d = {'name': 'tom', 'age': 18, 'interest':('music', 'movie'), 'class':['python']}

methods = (json, msgpack)

for i, m in enumerate(methods):
    x = m.dumps(d)
    print(i + 1,m.__name__, type(x), len(x), x)

print("==================================")
print(x)
print(msgpack.loads(x)) # loads()函数将二进制数据反序列化为原始数据,在msgpack中，是unpackb的别名