# Desc: 输入一组整数，输出升序数列
#count = int(input("选择输出的整数个数："))
#list1 = []
#for i in range(count):
#   a = int(input("输入一个整数："))
#   list1.append(a)
#
#print("输出升序数列：", end="")
#for i in sorted(list1):
#    print(i, end=" ")

# 有一个列表lst = [1,4,9,16,2,5,10,15],生成一个新列表，要求新列表是1st相邻2项的和
lst = [1,4,9,16,2,5,10,15]
new_list=[lst[i] + lst[i+1] for i in range(len(lst)-1)]
print(new_list)

# 随机100个产品ID，ID格式如下
## 顺序的数字6位，分隔符点号，10个随机小写英文字符
## 例如：000001.aqweqweqwe

# ascii 97-122
import random
for i in range(100):
    print('{}.{}'.format(str(i).zfill(6),"".join([chr(random.randint(97, 122)) for x in range(10)])))


