# Lua基础
## Lua介绍
### Lua语言有应用场景
- 游戏开发-用来做热更
- 独立软件 Photoshop，部分功能扩展
- WEB开发
- WEB服务器中间件
  - nginx支持扩展，lua写个扩展
- 数据库操作脚本
- 缓存操作脚本
  - redis秒杀（本质上是把一个非原子操作转变为一个原子操作）
  - 锁（分布式锁）

### Lua官网(标准C写的语言)
```shell
官网：https://www.lua.org/
```

### 开发环境配置与hello world
- 下载源码包
- 编译
- 加环境变量
- 测试lua -v
```shell
curl -L -R -O https://www.lua.org/ftp/lua-5.4.6.tar.gz
tar zxf lua-5.4.6.tar.gz
cd lua-5.4.6
make all test
```
- 写一个脚本，直接用lua执行  
- 注意：lua生成可执行文件，-o写在前面
```shell
luac -o abc a.lua 
```

### lua注释
- mysql相同
```lua
-- 这是个注释
--[[
    多行注释
]]--
```

### Lua基础语法
#### 变量命名规范
- 弱类型语言、动态类型语言
  - 定义变量不需要声明类型
  - 每行代码结束，可以不需要分号，有没有都行
  - 变量类型可以随时改变
  - 命名规范，同C即可

- 变量类型
  - 全局变量
    - 默认创建都是全局变量
  - 局部变量
    - 用local修饰，类似shell
    ```lua
    local x = 123;

    -- 代码块/作用域
    do
        --
    end
    ``` 
  - 表字段


#### lua官方文档
- lua中，8种基本数据类型
  - nil
  - boolean（true；false）
  - number（包括整型和浮点型）
  - string
  - function (函数)
  - usredata（自定义数据格式）
  - thread（携程?）
  - table（表）


- 库函数type()
  - 返回一个描述给定值类型的字符串

- 注意：<span style="color:red">在lua中，只有false和nil表示假</span>


#### function 
- function在lua中一个基本的数据类型，是第一类值
```lua
-- 格式
function funcName()
    --
end

-- 示例
function func1()
    print("这里是func1");
end

func1();

-- 传参示例
function func2(a, b, c) 
    print(a, b, c);
end;

-- 带返回值
function func3(a, b, c)
    return a + b + c 
end

-- 可变参
function fun4(...) 
    --
end;

-- 函数当右值
-- 把匿名函数传递给变量
sum1 = function(a, b)
    return a+b;
end;
print(sum1(1, 2))

sum2 = sum1
print(sum2(11,22))

-- 当其他函数的参数（回调函数）
function func4(functionName, a, b) 
    return functionName(a,b);
end

print(fun4(sum1, 111, 222));
```

#### table
- table表，是一种数据类型，类似于map，用k-v方式来表现
- 格式：
```lua
tableName={}

-- 示例
info = {
    id = 123,
    name = tom,
    gender = male
}

for k, v in (info) do
    print(k,v);
end
```


