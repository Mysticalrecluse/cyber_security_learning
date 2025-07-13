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

















# vim集成DeepSeek

**在.bashrc里，放入环境变量，保证 deepseek 的 api keys 可以被调用**

```bash
export DEEPSEEK_API_KEY="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```



**在PATH路径中，创建 deepseek-query.sh 脚本文件**

```bash
root@localhost:~# echo $PATH
/root/.local/bin:/root/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin

# 在/root/bin下，创建deepseek-query.sh
root@localhost:~# mkdir bin

# 写脚本文件
root@localhost:~# cat bin/deepseek-query.sh 
#!/bin/bash

# === 配置 ===
API_KEY="${DEEPSEEK_API_KEY}"
MODEL="deepseek-chat"
ENDPOINT="https://api.deepseek.com/v1/chat/completions"

if [[ -z "$API_KEY" ]]; then
  echo "[error] 请先导出 DEEPSEEK_API_KEY 环境变量"
  exit 1
fi

#PROMPT="$*"

if [[ -n "$1" ]]; then
  PROMPT="$1"
else
  read -r PROMPT
fi


#DATA=$(cat <<EOF
#{
#  "model": "$MODEL",
#  "messages": [
#    {"role": "user", "content": "$PROMPT"}
#  ]
#}
#EOF
#)


DATA=$(jq -n --arg prompt "$PROMPT" --arg model "$MODEL" '
{
  model: $model,
  messages: [
    { role: "user", content: $prompt }
  ]
}')


#curl -sS "$ENDPOINT" \
#  -H "Content-Type: application/json" \
#  -H "Authorization: Bearer $API_KEY" \
#  -d "$DATA" | jq -r '.choices[0].message.content'

response=$(curl -sS "$ENDPOINT" \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $API_KEY" \
  -d "$DATA")

echo "$response" | jq -r '.choices[0].message.content'
```



**在.vimrc中配置，调用deepseek脚本**

```bash

" -------------- DeepSeek 集成 -----------------
" Leader 键：\  （可自行 let mapleader = "," …）
nnoremap <leader>ds :call DeepSeek_Query_Cursor()<CR>
vnoremap <leader>ds :<C-u>call <SID>DeepSeek_Query_Visual()<CR>
"vnoremap <leader>ds :<C-u>call DeepSeek_Query_Visual()<CR>

" 关闭浮窗的快捷键
nnoremap <silent> <leader>q :call popup_close(popup_list()[0])<CR>
"
"function! s:popup_show(msg) abort
"  if has('popupwin')          " Vim 8.2+ 推荐用浮窗
"    call popup_create(a:msg, #{minwidth:60, minheight:8, line:2, col:2,
"          \ border:[1], borderchars:['─']})
"  else                        " 老版本退化为只读新缓冲
"    new
"    setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile
"    call setline(1, split(a:msg, "\n"))
"  endif
"endfunction
"
"" 普通模式：取光标所在行（或函数名等），可自行改成 expand('<cword>')
"function! DeepSeek_Query_Cursor() abort
""  let l:text = getline('.')
""  let l:answer = system('echo '.shellescape(l:text).' | ~/bin/deepseek-query.sh')
""  call <SID>popup_show(l:answer)
"   let l:prompt = input('🤖 请输入你的问题: ')
"   if empty(l:prompt)
"     echohl WarningMsg | echo '[❌] 已取消，问题为空' | echohl None
"     return
"   endif
""   let l:answer = system('echo '.shellescape(l:prompt).' | ~/bin/deepseek-query.sh')
"   let l:answer = system("echo " . shellescape(l:prompt) . " | bash ~/bin/deepseek-query.sh")
"   call <SID>popup_show(l:answer)
"endfunction
"
"" 可视模式：取选区
"function! DeepSeek_Query_Visual() abort
"  " 保存选区两端
"  let l_save = @@
"  normal! "vy
"  let l:text = @@
"  let @@ = l_save
"
"  let l:answer = system('echo '.shellescape(l:text).' | ~/bin/deepseek-query.sh')
"  call <SID>popup_show(l:answer)
"endfunction


let mapleader = "\\"

" === 快捷键 ===
nnoremap <leader>ds :call DeepSeek_Query_Cursor()<CR>
vnoremap <leader>ds :<C-u>call <SID>DeepSeek_Query_Visual()<CR>
nnoremap <silent> <leader>q :call popup_close(popup_list()[0])<CR>

" === 浮窗显示函数 ===
function! s:popup_show(msg) abort
  if has('popupwin')
    call popup_create(a:msg, {
          \ 'minwidth': 60, 'minheight': 8,
          \ 'line': 2, 'col': 2,
          \ 'border': [1], 'borderchars': ['─'],
          \ })
  else
    new
    setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile
    call setline(1, split(a:msg, "\n"))
  endif
endfunction

" === 核心提问函数 ===
function! s:deepseek_query_and_popup(text) abort
  if empty(a:text)
    echohl WarningMsg | echo '[❌] 内容为空，未发送' | echohl None
    return
  endif
  let l:answer = system('bash ~/bin/deepseek-query.sh ' . shellescape(a:text))
  call s:popup_show(l:answer)
endfunction

" === 普通模式：输入问题 ===
function! DeepSeek_Query_Cursor() abort
  let prompt = input('🤖 请输入你的问题: ')
  if empty(prompt)
    echohl WarningMsg | echo '[取消发送]' | echohl None
    return
  endif
  call s:deepseek_query_and_popup(prompt)
endfunction

" === 可视模式：选择提问 ===
"function! s:DeepSeek_Query_Visual() abort
"  let l:save_reg = @@
"  normal! "vy
"  let l:text = @@
"  let @@ = l:save_reg
"  call s:deepseek_query_and_popup(l:text)
"endfunction

"function! s:DeepSeek_Query_Visual() abort
"  " 获取可视选区范围（行号）
"  let start = getpos("'<")[1]
"  let end = getpos("'>")[1]
"
"  " 获取选中内容的所有行
"  let lines = getline(start, end)
"
"  " 将多行拼接成一行（避免 JSON 解析失败）
"  let text = join(lines, ' ')
"
"  call s:deepseek_query_and_popup(text)
"endfunction

function! s:DeepSeek_Query_Visual() abort
  " 保存剪贴板内容
  let l:save_reg = @@

  " 复制可视选区内容
  normal! "vy
  let l:selected = @@

  " 恢复剪贴板
  let @@ = l:save_reg

  " 手动输入提问内容
  let l:prompt = input('🤖 请输入你的问题（选中内容将附在末尾）：')
  if empty(l:prompt)
    echohl WarningMsg | echo '[❌] 已取消，问题为空' | echohl None
    return
  endif

  " 拼接用户问题和选中内容
  let l:final_prompt = l:prompt . "\n\n" . l:selected

  " 执行查询
  call s:deepseek_query_and_popup(l:final_prompt)
endfunction 
```



