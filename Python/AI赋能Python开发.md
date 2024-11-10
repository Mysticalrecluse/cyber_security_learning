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

# 基于指定路径创建
conda create -p /path/to/your/environment
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

删除环境
```shell
conda remove <环境名称> --all
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

## 安装Cursor
下载地址
```shell
cursor.com
```

提示词示例
```shell
# LangChain Python 推理后端的人工智能规则
您是Python、LangChain和可扩展AI应用开发方面的专家

# 关键词原则
- 提供简洁、技术性的响应，并附上准确的Python示例代码，使用LangChain v0.2
- 优先考虑函数式和声明式编程，尽可能避免使用类
- 使用LangChain表达式语言(LCEL)进行链实现
- 使用描述性变量名，例如：is_retrieval_enabled, has_context.
- 目录和文件名使用小写字母加下划线，例如：chains/reg_chain.py
- 链接器、检索器和实用功能应首选命名导出
- 如果对LangChain不确定，可以参考[概念指南](https://python.langchain.com/v0.2/docs/concepts/)。
```

常用快捷键
- CTRL/CMD + L 打开对话框
  - a. 选中代码块，然后CTRL/CMD + L 根据代码块对话
- CTRL/CMD + K：打开生成窗口
- CTRL/CMD + I：打开Composer，用于多文件修改
  - 在同一窗口完成
- CTRL/CMD + Y：直接在代码中应用生成的代码

@注记
- @Files：传递指定代码文件上下文
- @Code：传递指定代码块(函数和类)上下文
- @Docs：从官方文档获取上下文(需先在配置文件添加文档)
- @Web：从搜索引擎结果获取上下文
- @Folders：传递文件目录信息上下文
- @Chat：传递对话窗口内容上下文(仅限代码生成窗口)
- @Git：传递Git仓库commit历史(仅限对话窗)
- @Codebase：在代码仓里扫描文件传入(仅限对话窗口)

## OpenAI API文档与key的创建
重要文档
```shell
https://platform.openai.com/docs/overview
KEY: https://platform.openai.com/api-keys
```

## 平替网站：Deepseek
```shell
https://platform.deepseek.com/api_keys
```

# 利用LLM代码学习Python数据类型
## 目标
- 借助大模型与开源项目，回顾Python语法和内置数据类型
- 借助大模型实现从数据结构到数据类型的转化
- 借助开源项目了解数据类型的使用
- 通过大模型编写的生成器表达式与迭代器协议
- 通过LLM生成符合PEP8规范的代码注释和类型提示o

## 模仿Python内置类型
len()函数对应的魔术方法是__len__()。当你调用函数时，Python实际上会调用对象__len__()方法来获取长度。
```python
class MyCollection:
    def __init__(self, items):
        self.items = items
    def __len__(self): len对应的魔术方法
        return len(self.items)

# 创建一个自定义集合对象
my_collection = MyCollection([1,2,3,4])

# 使用len()函数
print(f"自定义集合的长度：{len(my_collection)}")
```
