# 斐波那契数列

#def function(a):
#    if a == 1 or a == 2:
#        return 1
#    else:
#        return function(a-1) + function(a-2)
#
#print(function(101)) # 34


#def fibonacci(n, memo={}):
#    if n in memo:
#        return memo[n]
#    if n <= 1:
#        return n
#    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
#    return memo[n]
#
#print(fibonacci(100)) # 354224848179261915075

#a = 1
#b = 1
#count = 1
#print(count, b)
#while True:
#    count += 1
#    if count == 100:
#        break
#    a, b = b, a + b
#    print(count, b)

def fib4(n, a=1, b=1):
    if n < 3:
        return b
    a, b = b, a+b
    return fib4(n-1, b, a+b)

print(fib4(100)) # 354224848179261915075


import sys

print(sys.getrecursionlimit()) # 1000

# 猴子吃桃

def eat(n):
    if n == 1:
        return 1
    return (eat(n-1) + 1) * 2 # 递归公式, f(n) = (f(n-1) + 1) * 2

print(eat(10))

def f(n):
    if n == 1:
        return 1
    return f(n-1) * n

print(f(5)) # 120


