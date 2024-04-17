# VIM 基础操作
## 光标移动
- hjkl: 上下左右
- Ff：跳到当前行指定字符
- Tt：跳到当前行字符前，比如""
- ；：重复前一个f/t的结果
- ，：重复后一个f/t的结果
- / + 指定字符，可以跳到当前位置之后的自定字符位置，后可以使用n/N进行跳转
- ? + 指定字符, 可以跳转到当前位置之前的指定字符位置
- wW,eE,bB，单词进行跳转
- () 在句子间进行跳转
- {} 在段落间进行跳转
- `[{` `]}`  或`[(` `])`在代码的{}或()段间进行跳转, 前面加数字可以进行嵌套跳转
- 0 跳转到行首
- ^ 跳转到非空行首
- $ 跳转到行尾
- % 在就近的（）之间跳转
- `*` 找到所有光标所在单词，并向后跳转，使用n/N可以重复该动作
- `#` 找到所有光标所在单词，并向前跳转，使用n/N可以重复该动作
- H: 跳到该屏幕中的首行行首
- L：跳到该屏幕的尾行行首
- M: 跳到该屏幕的中间行首
- `反引号 + 标记字符：跳到指定标记处
- '单引号 + 标记字符：跳到指定标记的所在行的开头
- `m + 标记字符`: 设置标记，a-z为local标记， A-Z为global标记
- `:marks`: 查看所有标记
- `:delm + 标记字符` 删除该标记
- `|` ：[count] + `|` 跳转到指定列数
- `:num`：跳到指定行数
- gg： 跳到首行
- G：跳到最后一行开头
- `:b+num 或 文件名`：跳转到指定文件中

## 操作
- y: 复制
    - Y/yy: 复制当前行所有字符
- d: 删除（结果存入寄存器中）
    - D: 类似于d$
    - dd：删除当前行
- c: 修改（删除并进入insert模式）
    - C/cc：删除一整行，并进入insert模式
- p: 粘贴在后面，或下行
- P（大写）: 粘贴在前面，或者上行 
- s: 删除当前字符，并进入insert模式
- S: 删除一整行，并进入insert模式，类似于C/cc
- r: 替换单个字符
- ~：更改所在字符大小写
- x：删除当前字符
- X: 删除后一个字符
- 操作字符（ydc + i/a + w/s/p）
    - i: 不包含特殊字符
    - a: 包含特殊字符
    - w: 单词
    - s: 句子
    - p: 段落
- `.` 点：重复最后一次操作
- `" + [0-9,a-z]`: 将指定文本复制进指定寄存器
- `"[A-Z]`: 表示追加字符到指定a-z的对应寄存器中
- `:reg`：查看寄存器内容
- `:w`: 保存
- ZZ：保存后退出
- ZQ：不保存退出
- u：撤销

## 视窗
- zz: 窗口移动到中间
- zt：窗口对顶
- zb：窗口对底

## 切换insert模式
- i: 进入insert模式，并且光标移动到指定字符之前
- I：进入insert模式，并且光标移动到当前行开头
- a: 进入insert模式，并且光标移动到指定字符之后
- A：进入insert模式，并且光标移动到行尾
- o：进入insert模式，光标移动到下面，新起一行
- O: 进入insert模式，光标移动到上面，新起一行

## 扩展命令模式
### 基本命令
- w: 保存文件
- x: 等价于wq（保存退出）
- X：加密
- w + 文件名： 文件另存为
- q：退出
- ！：强制执行
- r + 文件名：读取指定文件内容到光标下
- !command：执行指令
- r!command：读取执行命令的结果

### 地址定界格式
```
M
M, N
.
$
.,$-1
/pattern/
/part1/,/part2/
```

### 操作
```shell
p               #输出
d               #删除
y               #复制
w file          #将范围内的行另存至指定文件中
r file          #在指定位置插入指定文件中的所有内容
t行号            #将前面指定的行复制到N行后
m行号            #将前面指定的行移动到N行后
```

### 查找并替换
```shell
s/pattern/替换字符/修饰符
%s              #全文查找替换
```

### 定制VIM工作特性
- 配置文件
    - 全局：/etc/vimrc
    - 个人：~/.vimrc

- 行号
```
set nu | number
set nonu | nonumber
```

- 忽略字符大小写
```
set ic | ignorecase
set noic
```

- 自动缩进
```
set ai | autoindent
set noai | noautoindent
```

- 复制保留格式
```
set paste
set nopaste
```

- 显示Tab(^I)和换行符($)
```
set list
set nolist
```

- 语法高亮
```
syntax on
syntax off
```
- 实时REX高亮匹配
```
set incsearch
```

- 高亮搜索
```
set hlsearch
set nohlsearch|nohl
```

- 文件格式
```
set ff=dos      #启用Windows格式
set ff=unix     #启用Unix格式
```

- Tab键用空格代替
```
set expandtab | et
set noexpandtab | noet
```

- 用指定空格数代替Tab
```
set tabstop=N| ts=N     # 指定N个空格代替tab键
```

- 设置缩进宽度
```
<<
>>

set shiftwidth=4
```

- 设置光标所在行标识线
```
set cursorline| cul
set nocursorline| nocul
```

- 加密
```
set key=passwd  # 文件加密，相当于X
set key=        # 取消加密
```

## 可视化模式
```
ctrl + v 进入块模式
选定好后，使用i\shift + i
输入添加的字符
按ESC
```


## 多窗口模式
```
单文件分屏
ctrl + w + v   # 水平分屏
ctrl + w + s   # 垂直分屏
ctrl + w + q   # 取消相邻分屏
ctrl + w + o   # 取消全部分屏
ctrl + w + hjk;| arrow # 切换窗口
```

```
多文件分屏打开
vim -o|O file1 file2
```