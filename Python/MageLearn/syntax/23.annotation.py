# 注解annotation
## 类型注解
def add(x:int, y:int) -> int:
    return x + y

print(add) # <function add at 0x7f8b1c3b7d30>
print(add.__annotations__) # {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

## 类型检查
### inspect模块
import inspect
from functools import wraps

x = inspect.isfunction(add) # True
print(x)

### 示例
#### inspect.isfunction(object) 判断object是否是函数
#### inspect.ismethod(object) 判断object是否是方法
#### inspect.isroutine(object) 判断object是否是函数或方法
#### inspect.isclass(object) 判断object是否是类
#### inspect.ismodule(object) 判断object是否是模块
#### inspect.isbuiltin(object) 判断object是否是内置函数
#### inspect.isgeneratorfunction(object) 判断object是否是生成器函数
#### inspect.isgenerator(object) 判断object是否是生成器

sig = inspect.signature(add) # signature(add)返回一个inspect.Signature对象
# signature作用是提取函数的签名信息，包括参数和返回值
# signature对象有两个属性, parameters和return_annotation
print(sig) # (x:int, y:int) -> int

# parameters是一个有序字典，key是参数名，value是inspect.Parameter对象
params = sig .parameters
returns = sig.return_annotation
print(returns) # <class 'int'>

print(params) # OrderedDict([('x', <Parameter "x:int">), ('y', <Parameter "y:int">)])

print(type(params)) # <class 'mappingproxy'>
print(params['x']) # x:int

for k, v in params.items():
    print(type(k), k, type(v), v)

# parameter对象有四个属性
# v.name: 参数名
# v.default: 默认值
# v.annotation: 注解
# v.kind: 参数类型，有5种类型，POSITIONAL_ONLY, POSITIONAL_OR_KEYWORD, VAR_POSITIONAL, KEYWORD_ONLY, VAR_KEYWORD
for k, v in params.items():
    print(v.name, v.default, v.annotation, v.kind)

def check(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        params = inspect.signature(fn).parameters
        #name = tuple(params.keys())
        #for i, v in enumerate(args):
        #    if not isinstance(v, params[name[i]].annotation):
        #        print(f"参数{name[i]}类型不匹配")
        for v, p in zip(args, params.values()):
            if p.annotaion != p.empty and not isinstance(v, p.annotation):
                print(f"参数{p.name}类型不匹配")

        for k, v in kwargs.items():
            if params[k].annotation != inspect._empty and not isinstance(v, params[k].annotation):
                print(f"参数{k}类型不匹配")
        ret = fn(*args, **kwargs)
        if not isinstance(ret,inspect.signature(fn).return_annotation):
            print("返回值类型不匹配")
        return ret
    return wrapper

@check
def add(x:int , y:int) -> int:
    return x + y

print(add(x=4,y=5))