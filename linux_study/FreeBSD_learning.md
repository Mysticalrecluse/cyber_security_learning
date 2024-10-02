# FreeBSD
## shell切换
```shell
# 查看shell列表
cat /etc/shells

# 下载需要的shell
pkg install bash （如果下载bash）

# 切换指定shell
chsh -s /usr/local/bin/bash
```

## ssh远程配置文件
```shell
/etc/ssh/sshd_config
# 更改
PasswordAuthentication yes
```

## .bashrc配置

- 配置.bashrc
```shell
# 原BSD的ls更改文件显示颜色
export CLICOLOR=1
export LSCOLORS='ExfxcxdxCxegedabagacad'

alias ls='gls --color=auto'

# 更改gls显示的文件颜色
export LS_COLORS='*.zip=01;31:*.tar=01;31:*.gz=01;31:*.bz2=01;31:*.xz=01;31'
```

- 让.profile引用.bashrc文件
```shell
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi
```

- 在bsd中安装GNU的ls
```shell
sudo pkg install coreutils
# 安装之后，命令的名称是gls
# 可以写个别名更改为ls
```

### FreeBSD的文件颜色更改
- LSCOLORS 环境变量在 FreeBSD 和 macOS 的 ls 命令中用于控制不同类型文件的显示颜色。
```shell
文件类型/状态 对应
a：目录
b：符号链接
c：socket
d：管道
e：可执行文件
f：块设备
g：字符设备
h：不可执行的文件或目录（且被设置了 SGID）
i：可写的目录（且被设置了 STICKY 位，但不被设置了其他写权限）
j：可写的目录（且被设置了 STICKY 位，同时被设置了其他写权限）
k：符号链接（指向不存在的文件）
l：不可执行的文件或目录（且被设置了 SUID）
m：不可执行的文件或目录（且被设置了 SUID、SGID）
n：不可执行的文件或目录（且被设置了 SGID）
颜色代码
a：黑色
b：红色
c：绿色
d：黄色（棕色）
e：蓝色
f：洋红色（紫红色）
g：青色（蓝绿色）
h：灰色
A：暗黑色
B：亮红色
C：亮绿色
D：亮黄色
E：亮蓝色
F：亮洋红色
G：亮青色
H：白色
x：默认颜色
例子
假设 LSCOLORS 设置为 exfxcxdxbxegedabagacad，具体含义如下：

ex：目录的前景色为蓝色，背景色为默认色。
fx：符号链接的前景色为洋红色，背景色为默认色。
cx：socket 的前景色为绿色，背景色为默认色。
dx：管道（命名管道）的前景色为黄色，背景色为默认色。
bx：可执行文件的前景色为红色，背景色为默认色。
依此类推。
```

