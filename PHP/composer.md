# Composer安装与基本使用
## 概述
- 作用：Composer解决了项目的依赖关系，快速下载且实现了自动加载
  - 应用：ThinkPHP、Laravel均使用Composer自动加载体系

## Composer三大组成部分
- 第一部分：仓库、公共库和私有库，添加自己的类包到公共库分享出来

- 第二部分：命令行下载器，安装和使用命令

- 第三部分：自动加载代码，包依赖管理和使用自动加载，PSR-0和PSR-4自动加载规范


## Composer基本使用
- 首先（通常也是唯一）应该做的事情就是在你的composer.json文件中告诉Composer你的项目所依赖

- 下载：https://getcomposer.org/
  - 内含windows和Linux的下载方法

- 下载后，更改软件库下载源
```
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```

- 第一次玩，可以尝试下载thinkphp
```php
composer create-project topthink/think
// 下载路径为当前路径
```