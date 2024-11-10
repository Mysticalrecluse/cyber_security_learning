def mymap(func, iterable, /):
    res = []
    for i in iterable:
        res.append(func(i))
    return res


x = [1,2,3]
print(mymap(str, x)) # [1, 4, 9]

