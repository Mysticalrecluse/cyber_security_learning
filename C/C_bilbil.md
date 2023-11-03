# C语言应试部分
## 环境配置
### Windows
- 相关软件安装
  - DEV CPP 6.7.5
    - 安装时，直接根据引导，走默认配置，即可安装成功
    - 安装后，软件配置
    ```
    工具 -> 编辑器选项 -> 更改tab缩进，改为自动计算缩进量，1个tab等于4个空格

    原因：不同的编译环境，tab键的宽度可能不同，为了让代码在不同的环境下显示不一样，因此统一改为一个tab等于4个space
    ```
    - 注意事项：如果后期发现，代码逻辑和程序执行结果不一致，在代码正确的情况下，删除之前生成的可执行程序，重新编译运行即可
### Linux
- 配置云主机
```bash
在购买云主机(Ubuntu2004)，安装好tabby，并实现远程连接之后

1. 执行以下命令，确保自己在root用户下执行命令
sudo -i

2. 执行下面的命令
apt update
apt upgrade -y
apt install wget -y
wget http://123.57.102.65/data/init_env.sh

3. 执行下面的命令，完成环境配置
bash init_env.sh
```

- 查看C语言使用方法
  - man手册
  ```bash
  man -f < C_command >

  man -K command # 查看带command关键字的命令

  # 在vim中直接查看man手册
  shift + [n]K # 默认n=1，查看第n章手册

  # 彩色man手册
  - 配置 ~.bashrc
  搜索：plugins
  插入新插件
  plugins=(... colored-man-pages)
  ```
  - tldr (too long don't read)
    - 更好用的命令手册，只能查询shell命令

## C语言参考
- 查询手册网站：`zh.cppreference.com`

## 编码规范
  