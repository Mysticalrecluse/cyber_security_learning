import random
# randint() function generates a random number between the two numbers you provide.

# randint(a, b) generates a random number between a and b (inclusive).
for i in range(10):
    print(random.randint(0,9), end=" ")

print("")
# randrange() function returns a randomly selected element from the specified range.
for i in range(10):
    print(random.randrange(0,100,2), end=" ")

print("")

# random.choice() ，在指定的迭代器范围内随机选择元素
x = [1, 0, 4, 5, 2]
y = [1, 1, 2, 2, 2]
for i in range(5):
    print(random.choice(x), end=" ")

print("")
# random.choices(x, y, k=1); y表示权重，和前面的x一一对应，x和y的列表元素数量必须一致，否则报错; 默认k=1， k表示随机取N个值的列表，列表中的值可以重复取
# x是指定元素，y指定权重，k表示生成列表的元素数量
for i in range(5):
    print(random.choices(x, y, k=7))


# random.sample(x, k=1)，sample和choices的区别是sample采样,x中每个值只拿1次，且采样数量不能超过x的数量
for i in range(5):
    print(random.sample(x, k=2))