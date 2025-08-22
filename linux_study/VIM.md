# kkVIM 基础操作



## 常用模式



- **正常（normal）模式**

  > （也称为普通模式），缺省的编辑模式；如果不加特殊说明，一般提到的命令都直接在正常模式下输入；在任何其他模式中，都可以通过键盘上的 Esc 键回到正常模式。

- **插入（insert）模式**

  > 输入文本时使用；比如在正常模式下键入 i（insert）或 a（append）即可进入插入模式。

- **可视（visual）模式**

  > 用于选定文本块；教程中已经提到可以用键 v（小写）来按字符选定，Vim 里也提供其他不同的选定方法，包括按行和按列块。

- **命令行（command-line）模式**

  > 用于执行较长、较复杂的命令；在正常模式下键入冒号（:）即可进入该模式；使用斜杠（/）和问号（?）开始搜索也算作命令行模式。命令行模式下的命令要输入回车键（Enter）才算完成。





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







# VIM Script









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
API_KEY="${DEEPSEEK_API_KEY}"jjj
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





# vim集成C语言语法补全



## coc.nvim 的 vim 版本要求

- **Vim ≥ 9.0.0438**（带完整 `vim9script` 功能）

- **Neovim ≥ 0.8.0**



直接升级vim的方法

```bash
sudo add-apt-repository ppa:jonathonf/vim
sudo apt update
sudo apt install vim
```



## coc.nvim 的 Node.js 版本要求

- 官方要求：**Node.js ≥ 14**
- 推荐：**Node.js 16 / 18 LTS**（稳定且长期支持）

安装升级版的nodejs

```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
apt install -y nodejs
```

```bash
[root@ubuntu2204 ~]#node -v
v18.20.8
```



## 在 Minpac 中添加 coc.nvim

在你的 `.vimrc` 里 **Minpac 初始化块**中添加：

```bash
# 添加下行
call minpac#add('neoclide/coc.nvim', {'branch': 'release'})

# 运行安装
:PackUpdate
```



## **配置 coc.nvim**

安装后需要基本配置，例如：

```bash
"  让 coc.nvim 自动启动
filetype plugin indent on
syntax on

"  解决补全菜单行为
set completeopt=menu,menuone,noselect

"  启用回车确认补全
inoremap <expr> <CR> pumvisible() ? coc#_select_confirm() : "\<CR>"
```



## **安装 C 语言支持（clangd）**

安装 LSP 服务器：

```bash
apt install clangd
```

然后在 Vim 里执行：

```bash
:CocInstall coc-clangd
```



## 按键映射推荐

```bash
# 向下使用ctrl + n
inoremap <expr> <Tab>   pumvisible() ? "\<C-p>(<BS>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

# 正统的方法，但实测有问题
" ✅ Tab 选择下一个补全项 / Enter 确认
inoremap <expr> <Tab>   pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
inoremap <expr> <CR>    pumvisible() ? coc#_select_confirm() : "\<CR>"
```











# 通过插件实现全语言补齐



## 实现方案

**C/C++ / Python / Go / Rust / Java 等** → 由 **YCM** 负责（快速、稳定）

**Shell (`sh`, `bash`)** → 由 **coc.nvim + coc-sh** 负责（智能补全）



### 冲突解决方案

**只在 Shell 文件启用 coc.nvim**

在 `.vimrc` 里：

```bash
# 只为 sh/bash 文件加载 coc.nvim
autocmd FileType sh,Bash packadd coc.nvim
```

**或者禁用 YCM 在 Shell 文件**

```bash
autocmd FileType sh let g:ycm_filetype_blacklist = {'sh': 1}
```

这样 YCM 不会在 `sh` 文件干扰补全。



### 注意事项

使用普通用户下载安装，后续使用软连接让root用户使用配置

让 root **读取普通用户的 Vim 配置**：

```bash
ln -sf /home/youruser/.vimrc /root/.vimrc
ln -sf /home/youruser/.vim /root/.vim
```



## 提前安装全部依赖

```bash
# Ubuntu
apt install -y build-essential cmake python3-dev clangd libclang-dev golang rustc cargo openjdk-17-jdk nodejs npm mono-complete libncurses-dev perl libperl-dev ruby-dev liblua5.3-dev git

# Rocky
dnf install -y gcc gcc-c++ make automake autoconf libtool binutils \
  cmake python3-devel clang clang-tools-extra libclang-devel \
  golang rust cargo java-17-openjdk-devel nodejs npm \
  ncurses-devel perl perl-devel ruby-devel lua-devel git

# 如需 C# 补全（Mono）
dnf install -y epel-release
dnf install -y mono-complete
```





## 升级GO

YCM 需要一个 **较新的 Go 版本**（至少 1.20+）来构建 gopls。



### 使用官方 tar.gz 安装 Go 1.22

```bash
# 下载安装
wget https://go.dev/dl/go1.22.5.linux-amd64.tar.gz
rm -rf /usr/local/go
tar -C /usr/local -xzf go1.22.5.linux-amd64.tar.gz

# 设置环境变量（添加到 ~/.bashrc）：
export PATH=/usr/local/go/bin:$PATH

# 验证
go version
# go version go1.22.5 linux/amd64
```



## 升级 Node.js（推荐）

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

```bash
# 查看
[root@ubuntu2204 ~]#node -v
v20.19.4
[root@ubuntu2204 ~]#npm -v
10.8.2
```





## 卸载默认vim，并编译安装新版vim91

```bash
# 卸载
apt remove vim -y

# 编译安装vim91
git clone https://github.com/vim/vim.git
cd vim
./configure \
  --with-features=huge \
  --enable-multibyte \
  --enable-cscope \
  --enable-terminal \
  --enable-perlinterp=yes \
  --enable-python3interp=yes \
  --with-python3-command=python3 \
  --enable-rubyinterp=yes \
  --enable-luainterp=yes \
  --enable-gui=no \
  --without-x \
  --prefix=/usr/local

make -j$(nproc)
make install
```

```bash
# 编译成功后查看
[root@ubuntu2204 YouCompleteMe]#vim --version
VIM - Vi IMproved 9.1 (2024 Jan 02, compiled Jul 30 2025 10:47:46)
Included patches: 1-1591
Compiled by root@ubuntu2204.wang.org
Huge version without GUI.  Features included (+) or not (-):
+acl               +find_in_path      +multi_byte        +termguicolors
+arabic            +float             +multi_lang        +terminal
+autocmd           +folding           -mzscheme          +terminfo
+autochdir         -footer            +netbeans_intg     +termresponse
-autoservername    +fork()            +num64             +textobjects
-balloon_eval      -gettext           +packages          +textprop
+balloon_eval_term -hangul_input      +path_extra        +timers
-browse            +iconv             +perl              +title
++builtin_terms    +insert_expand     +persistent_undo   -toolbar
+byte_offset       +ipv6              +popupwin          +user_commands
+channel           +job               +postscript        +vartabs
+cindent           +jumplist          +printer           +vertsplit
-clientserver      +keymap            +profile           +vim9script
-clipboard         +lambda            -python            +viminfo
+cmdline_compl     +langmap           +python3           +virtualedit
+cmdline_hist      +libcall           +quickfix          +visual
+cmdline_info      +linebreak         +reltime           +visualextra
+comments          +lispindent        +rightleft         +vreplace
+conceal           +listcmds          +ruby              -wayland
+cryptv            +localmap          +scrollbind        -wayland_clipboard
+cscope            -lua               +signs             +wildignore
+cursorbind        +menu              +smartindent       +wildmenu
+cursorshape       +mksession         -sodium            +windows
+dialog_con        +modify_fname      -sound             +writebackup
+diff              +mouse             +spell             -X11
+digraphs          -mouseshape        +startuptime       +xattr
-dnd               +mouse_dec         +statusline        -xfontset
-ebcdic            -mouse_gpm         -sun_workshop      -xim
+emacs_tags        -mouse_jsbterm     +syntax            -xpm
+eval              +mouse_netterm     +tabpanel          -xsmp
+ex_extra          +mouse_sgr         +tag_binary        -xterm_clipboard
+extra_search      -mouse_sysmouse    -tag_old_static    -xterm_save
-farsi             +mouse_urxvt       -tag_any_white     
+file_in_path      +mouse_xterm       -tcl               
   system vimrc file: "$VIM/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
 3rd user vimrc file: "~/.config/vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
  fall-back for $VIM: "/usr/local/share/vim"
Compilation: gcc -c -I. -Iproto -DHAVE_CONFIG_H -g -O2 -D_REENTRANT -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 
Linking: gcc -Wl,-E -L/usr/local/lib -Wl,--as-needed -o vim -lm -ltinfo -Wl,-E -fstack-protector-strong -L/usr/local/lib -L/usr/lib/x86_64-linux-gnu/perl/5.34/CORE -lperl -ldl -lm -lpthread -lcrypt -L/usr/lib/python3.10/config-3.10-x86_64-linux-gnu -lpython3.10 -lcrypt -ldl -lm -lm -lruby-3.0 -lm -L/usr/lib 
```



## YouCompleteMe

### 手动安装YCM（推荐）

```bash
# 选择安装目录
mkdir -p ~/.vim/pack/my/start
cd ~/.vim/pack/my/start
git clone --recurse-submodules --shallow-submodules https://github.com/ycm-core/YouCompleteMe.git

# 查看
[root@ubuntu2204 YouCompleteMe]#ls
autoload  codecov.yml  CODE_OF_CONDUCT.md  CONTRIBUTING.md  COPYING.txt  doc  install.py  install.sh  plugin  print_todos.sh  python  README.md  run_tests.py  test  third_party  tox.ini  update-vim-docs  vimrc_ycm_minimal

#使用install.py安装，安装全部
python3 install.py --all --clangd-completer

# 安装成功
[mystical@ubuntu2204 YouCompleteMe]$python3 install.py --all --clangd-completer
Generating ycmd build configuration...OK
Compiling ycmd target: ycm_core...OK
Building watchdog module...OK
Building regex module...OK
Installing Omnisharp for C# support...OK
Building gopls for go completion...OK
Setting up Tern for JavaScript completion...OK
Installing rust-analyzer "nightly-2024-06-11" for Rust support...OK
Installing jdt.ls for Java support...OK
Setting up TSserver for TypeScript completion...OK
Setting up Clangd completer...OK
```



### 安装实时缩进插件并配置

```bash
# 安装格式化代码软件 clang-format
apt install clang-format -y

# 下载插件
call minpac#add('dense-analysis/ale')

# 自动缩进
set autoindent
set smartindent
set cindent

" 智能补全
let g:ycm_semantic_triggers =  {
\   'c' : ['->', '.', 're!^\s*[a-zA-Z_]\w{1,}$'],
\   'cpp,objcpp' : ['->', '.', '::', 're!^\s*[a-zA-Z_]\w{1,}$']    
\ }     
        
" 保存时修复 
let g:ale_fix_on_save = 1
 
" 触发 clang-format 作为修复工具
let g:ale_fixers = {
\   'c': ['clang-format'],
\   'cpp': ['clang-format']
\ }     
        
" （可选）实时缩进：插入模式退出或文本变化时自动修复
autocmd TextChanged,InsertLeave *.c,*.cpp ALEFix
        
inoremap <C-l> <ESC>$a

```



### 代码浏览工具Cscope

```bash
# 在.vimrc添加插件
call minpac#add('adah1972/cscope_maps.vim') 

# 添加下列语句
" quickfix窗口
set cscopequickfix=s-,-,c-,d-,i-,t-,e-,a-

if !cscope_connection(1, expand("cscope.out"))
    cs add cscope.out 
endif
```



```bash
# Ubuntu
apt install -y cscope

# CentOS
yum install -y cscope

# 创建cscope 数据库
# 在项目的根目录执行
cscpoe -R -b

# 进入代码文本
# 执行下列语句查询跳转
<C-\>g
|g
||g
```

- g：查找一个符号的全局定义（global definition）
- s：查找一个符号（symbol）的引用
- d：查找被这个函数调用（called）的函数
- c：查找调用（call）这个函数的函数
- t：查找这个文本（text）字符串的所有出现位置
- e：使用 egrep 搜索模式进行查找
- f：按照文件（file）名查找（和 Vim 的 gf、f 命令相似）
- i：查找包含（include）这个文件的文件
- a：查找一个符号被赋值（assigned）的地方



### Go 语言补全（gopls）

YCM 支持 Go 语言，通过 **gopls（Go 官方 LSP 服务器）**：

#### **安装 gopls**

```bash
go install golang.org/x/tools/gopls@latest
```

> 确保 `$GOPATH/bin` 在 `$PATH` 中。



####  YCM 配置 gopls

```bash
let g:ycm_language_server += [
\ { 'name': 'gopls',
\   'cmdline': [ 'gopls' ],
\   'filetypes': [ 'go' ] }
\ ]
```



### Python 补全

```bash
[root@ubuntu2204 ~]#apt install python3-pip
[root@ubuntu2204 ~]#pip install 'python-lsp-server[all]'
```



```bash
let g:ycm_language_server += [
\ { 'name': 'pylsp',
\   'cmdline': [ 'pylsp' ],
\   'filetypes': [ 'python' ] }
\ ]
```



### Lua 补全（lua-language-server）

Lua 需要 **lua-language-server（sumneko/lua-language-server）**：

#### 安装 lua-language-server

```bash
apt install lua5.3
apt install ninja-build
# 安装 LSP（使用系统包或 GitHub 预编译）
git clone https://github.com/LuaLS/lua-language-server.git
cd lua-language-server
./make.sh   # 或按照官方文档安装
```



#### 配置 YCM 让它用 lua-language-server

```bash
let g:ycm_language_server += [
\ { 'name': 'lua_ls',
\   'cmdline': [ '/path/to/lua-language-server' ],
\   'filetypes': [ 'lua' ] }
\ ]
```



### ALE 格式化支持多语言

在 ALE 中同时添加：

```bash
let g:ale_fixers = {
\   'c': ['clang-format'],
\   'cpp': ['clang-format'],
\   'python': ['black'],
\   'go': ['gofmt'],
\   'lua': ['stylua']
\ }

```

并安装

```bash
pip install black        # Python 格式化
go install golang.org/x/tools/cmd/gofmt@latest  # Go 格式化
cargo install stylua     # Lua 格式化
```



## **最终整合配置（C + Go + Python + Lua）**

```bash
let g:ycm_auto_trigger = 1

" 智能补全
let g:ycm_semantic_triggers =  {
\   'c' : ['->', '.', 're!^\s*[a-zA-Z_]\w{1,}$'],
\   'cpp,objcpp' : ['->', '.', '::', 're!^\s*[a-zA-Z_]\w{1,}$'],
\   'go' : ['re!.*'],
\   'python': ['re!.*'],
\   'lua' : ['.']
\ }


" LSP 后端配置
let g:ycm_language_server = [
\ { 'name': 'gopls',  'cmdline': ['gopls'],  'filetypes': ['go'] },
\ { 'name': 'pylsp',  'cmdline': ['/usr/local/bin/pylsp'],  'filetypes': ['python'] },
\ { 'name': 'lua_ls', 'cmdline': ['/usr/local/src/lua-language-server/bin/lua-language-server', '-E', '/usr/local/src/lua-language-server/main.lua', '--logpath=~/.cache/lua-language-server/log', '--metapath=~/.cache/lua-language-server/meta', '--cwd', expand('%:p:h')], 'filetypes': ['lua'] }
\ ]


" 保存时修复
let g:ale_fix_on_save = 1

" 触发 clang-format 作为修复工具
let g:ale_fixers = {
\   'c': ['clang-format'],
\   'cpp': ['clang-format'],
\   'python': ['black'],
\   'go': ['gofmt'],
\   'lua': ['stylua']
\ }

" （可选）实时缩进：插入模式退出或文本变化时自动修复
"autocmd TextChanged,InsertLeave *.c,*.cpp ALEFix
"autocmd TextChanged,InsertLeave *.c,*.cpp,*.py,*.go,*.lua ALEFix

```



## 配置运行显示终端输出

```bash
" 通用运行函数
" ========= 通用 RunCodeInTerminal =========
function! RunCodeInTerminal(cmd)
  " 1. 关闭已有 terminal 窗格（避免多个）
  for w in range(1, winnr('$'))
    if getbufvar(winbufnr(w), '&buftype') ==# 'terminal'
      exec w . 'wincmd c'
    endif
  endfor

  " 2. 在底部打开一个 12 行高 terminal 窗格
  "botright new | resize 12
  execute 'terminal' a:cmd| resize 12
  " 3. 自动回到代码窗格
  wincmd p
endfunction


" ========= 语言自动识别 & 运行 =========
function! RunCurrentFile()
  let l:file = expand('%:p')
  let l:ext = expand('%:e')

  if l:ext ==# 'py'
    call RunCodeInTerminal('python3 ' . fnameescape(l:file))
  elseif l:ext ==# 'c'
    let l:exe = expand('%:p:r')
    call RunCodeInTerminal('sh -c "gcc ' . fnameescape(l:file) . ' -o ' . l:exe . ' && ' . l:exe . '"')
  elseif l:ext ==# 'lua'
    call RunCodeInTerminal('lua ' . fnameescape(l:file))
  elseif l:ext ==# 'go'
    call RunCodeInTerminal('go run ' . fnameescape(l:file))
  elseif l:ext ==# 'sh'
    call RunCodeInTerminal('bash ' . fnameescape(l:file))
  else
    echo "⚠️ 不支持的文件类型: " . l:ext
  endif
endfunction


" ========= 绑定快捷键 =========
" F5 运行当前文件
nnoremap <C-y> :w<CR>:call RunCurrentFile()<CR>
```





# 实用插件介绍



### Rainbow

代码中括号多了，有时候眼睛就有点看不过来，需要有个更好的颜色提示。因此，就有了很多彩虹效果的 Vim 插件。

```bash
call minpac#add('frazrepo/vim-rainbow')
```

效果默认不自动启用，可以用 :RainbowToggle 命令来切换，或用 :RainbowLoad 命令来加载。

```bash
" 自动启用RainboxToggle
autocmd VimEnter * RainbowToggle
```





### Markdown Preview

你如果像我一样常常写 Markdown 的话，你应该会喜欢 Markdown Preview 这个插件。Markdown 本来最适用的场景就是浏览器，纯文本的 Vim 只能编辑，没有好的预览终究是很不足的。Markdown Preview 解决了这个问题，让你在编辑的同时，可以在浏览器里看到实际的渲染效果。更令我吃惊的是，这个预览是完全实时、同步的，无需存盘，而且预览页面随着光标在 Vim 里移动而跟着滚动，效果相当酷。你可以直接到 Markdown Preview 的主页上看一下官方的示意图，我就不在这里放动图了。

这个插件唯一需要特别注意的是，你不能直接把 iamcco/markdown-preview.nvim 放到你的包管理器里了事。原因是它里面包含了需要编译的前端组件，需要下载或编译才行。在它的主页上描述了在不同包管理器里的安装方式，你只要跟着照做就行

它的配置在主页上也有列表，但默认设置就已经完全可用了。如果有需求的话，你可以修改其中部分值，如 g:mkdp_browser 可以用来设定你希望打开页面的浏览器（我目前设的是 'firefox'）。



### Calendar

Calendar 是一个很简单的显示日历的 Vim 插件，在包管理器里的名字是 mattn/calendar-vim。它的功能应该就不需要解释了，效果可以直接查看下图。

`mattn/calendar-vim` 是一个 Vim 的日历插件，可以在 Vim 里直接查看日历、查看节假日、管理 Google Calendar 事件（需要配置 API），支持月视图、周视图、日视图等。



####  **安装**

如果你用 **minpac** 管理插件：

```bash
call minpac#add('mattn/calendar-vim')
```

然后执行：

```bash
:PackUpdate
```



####  **基本用法**

✅ **打开日历**

```bash
:Calendar
```

- 默认显示 **月视图**。
- 使用 `hjkl` 在日期间移动。



✅ **打开周视图**

```bash
:Calendar -view=week
```



✅ **打开日视图**

```bash
:Calendar -view=day
```



✅ **打开 Google Calendar（日程管理）**

```bash
:Calendar -google
```

> 需要提前配置 Google API Key 和 OAuth（见下方进阶）。



####  **键位操作**

在日历窗口中：

- `q` 退出日历
- `Enter` 打开当天的事件（或日视图）
- `h/j/k/l` 在日期间导航
- `H/L` 上个月 / 下个月
- `K/J` 上一年 / 下一年



#### **进阶功能**

🔹 **支持 Google Calendar**

1. 需要安装 `curl` 和 `python3`。
2. 在 `.vimrc` 设置：

```bash
let g:calendar_google_calendar = 1
let g:calendar_google_task = 1
```

1. 运行 `:Calendar -google`，第一次会提示 OAuth 授权。



#### 结合工作流使用

- **快速查看日历**：`nnoremap <leader>ca :CalendarH<CR>`
- **查看某天事件**：光标移动到某天按 `Enter`
- **记录 TODO / 日志**：可以和 `vimwiki` / `taskwarrior` 结合



### Fzf 模糊文件查找

你知道文件名或其中的关键部分，但你不知道或不关心文件在哪里。这种情况下，Fzf 的模糊匹配就非常有用了

```bash
apt install fzf
```

加载插件

```bash
call minpac#add('junegunn/fzf', {'do': {-> fzf#install()}})
call minpac#add('junegunn/fzf.vim')
```



设置快捷键

```bash
nnoremap <leader>f :Files<CR>          " 搜索文件
nnoremap <leader>b :Buffers<CR>        " 搜索已打开缓冲区
nnoremap <leader>l :BLines<CR>         " 搜索当前 buffer 行
nnoremap <leader>h :History<CR>        " 搜索历史命令
nnoremap <leader>g :Rg<SPACE>          " 使用 ripgrep 搜索关键词
```



指定目录查找

```bash
:Files <dir>
```



基本操作

```bash
C-j            # 向下
C-k            # 向上
C-q            # 退出
```



### NERDTree 插件

加载插件

```bash
call minpac#add('preservim/nerdtree')
```



推荐映射

```bash
" 打开/关闭 NERDTree
nnoremap <leader>n :NERDTreeToggle<CR>

" 定位当前文件
nnoremap <leader>nf :NERDTreeFind<CR>

" 直接打开 NERDTree 并聚焦
nnoremap <leader>ne :NERDTreeFocus<CR>
```



**常见命令**

| 命令              | 功能                     |
| ----------------- | ------------------------ |
| `:NERDTree`       | 打开文件树窗口           |
| `:NERDTreeToggle` | 打开/关闭文件树          |
| `:NERDTreeFind`   | 定位到当前文件           |
| `:NERDTreeFocus`  | 让光标回到 NERDTree 窗口 |
| `:NERDTreeClose`  | 关闭 NERDTree 窗口       |



**NERDTree 窗口常用快捷键**

| 键位 | 作用                             |
| ---- | -------------------------------- |
| `o`  | 打开/关闭文件或目录              |
| `go` | 打开文件但光标不跳过去           |
| `t`  | 在新 tab 打开文件                |
| `T`  | 在新 tab 打开目录                |
| `i`  | 在水平分割中打开文件             |
| `s`  | 在垂直分割中打开文件             |
| `C`  | 将根目录切换到当前目录           |
| `u`  | 返回上级目录                     |
| `r`  | 刷新当前目录                     |
| `R`  | 递归刷新整个树                   |
| `m`  | 打开菜单（创建/删除/重命名文件） |
| `q`  | 关闭 NERDTree 窗口               |





### NERDCommenter

它提供的是又一个开发常用的功能，对某个代码块或代码行加上注释，及反过来把注释去掉。



#### 安装和配置

我们需要在包管理器中安装 `preservim/nerdcommenter`。然后，我一般在 vimrc 配置文件中加入下面的代码，让 NERDCommenter 不要在终端 Vim 中加入菜单，干扰我使用 查看最近的文件：

```bash
if !has('gui_running')
  let g:NERDMenuMode = 0
endif
```



#### 使用

NERDTree 提供的命令，有些可以工作于当前行或选定的行内部分字符，有些则只能工作于整行，即使用可视模式的话选行内部分字符相当于选了整行。能够适用于行内的有下面这些命令（也能适用于整行）：

- `<Leader>cc` 把代码变为注释
- `<Leader>cu` 把注释起止符剥掉，恢复原先的代码



下面这些则只能工作于完整的一行或多行上：



- `<Leader>c<Space>` 用来切换注释和非注释
- `<Leader>cb` 用来切换注释和非注释
- `<Leader>cs`\用来切换注释和非注释
