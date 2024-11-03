# Python开发环境搭建

## 部署Anaconda
Anaconda下载地址
```shell
https://www.anaconda.com/download/success
```

修改指定环境的默认路径
```shell
conda config --add envs_dirs D:/anaconda/envs
```

查看当前的默认路径
```shell
conda config --show envs_dirs
```

创建环境并安装openai软件包
```shell
conda create -n deepseek python=3.11 openai
# 格式：conda create -n <环境名称> python=<版本号> 安装的包
```

激活环境
```shell
conda activate deepseek
```

取消环境激活
```shell
conda deactivate
```

环境变量修改
```shell
export PATH=/path/to/python:$PATH
```

重要文档
```shell
python文档：https://docs.python.org/zh-cn/3.13/index.html
```

查看当前环境下，python安装了哪些第三方模块
```shell
pip freeze
```

安装第三方模块
```shell
pip install <第三方模块名>
```