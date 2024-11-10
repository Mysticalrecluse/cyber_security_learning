# 取整的技巧

# // 除法取整(向下取整)
print(10 // 3)  # 3
print(-10 // 3)  # -4

# int
print(int(10 / 3))  # 3

# math.floor()函数
import math
print(math.floor(10 / 3))  # 3

# math.ceil()函数
print(math.ceil(10 / 3))  # 4

# round()函数, 四舍五入
print(round(10 / 3))  # 3
print(round(7 / 2)) # 4

# round()函数，都是.5时向偶数取整
print(round(2.5))  # 2
print(round(3.5)) # 4


