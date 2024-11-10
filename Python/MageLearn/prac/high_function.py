print(sorted([1,'100','2','39'], key=int))

"""
def fn(x):
    return int(x)
fn(x) === int(x)

sorted([1,'100','2','39'], key=fn)
sorted([1,'100','2','39'], key=int)
"""

print(sorted(['a', 'Ab', '2', 'Abc'], key=str.lower))
"""
def fn(x):
    return x.lower() # str.lower(x)
    # return str.lower(x)
fn(x) === str.lower(x)
"""

a