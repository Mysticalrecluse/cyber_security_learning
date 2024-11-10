'''
if condition:
    statement
    statement
'''

x, y = 7, 5
if x > y:
    print("x is greater than y")

'''
if condition:
    statement
    statement
else:
    statement
    statement
'''

x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")

'''
if condition:
    statement
    statement
elif condition:
    statement
    statement
else:
    statement
    statement
'''

# 注意：python没有switch-case语句

# 使用字典实现switch-case语句
def option_a():
    return "You chose option A"

def option_b():
    return "You chose option B"

switch_dict = {
    "a": option_a,
    "b": option_b
}

result = switch_dict.get("a", lambda: "Invalid option")()
# 字典的get方法。get方法的第一个参数是你希望从字典中获取的键，第二个参数是如果键不存在时返回的默认值
print(result) # You chose option A


# 条件表达式（三元运算符）
# value1 is true branch, value2 is false branch
# variable = value1 if condition else value2
x , y = 7, 5
print("x is greater") if x > y else print("y is greater")   # x is greater

x = input("input a number:")
y = print("x is odd") if x % 2 else print("x is even") # x is odd
print(y)
