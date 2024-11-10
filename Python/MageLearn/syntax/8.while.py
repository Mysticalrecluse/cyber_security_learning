'''
while condition:
    statement
    statement
else:
    statement
'''

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("i is no longer less than 6")

# 在python中，while-else语句是合法的。else语句块只有在循环正常终止时才会执行，即循环条件为False时。
# 如果循环被break语句终止，else语句块不会执行。
