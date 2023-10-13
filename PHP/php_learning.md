# PHP基础
## 初始PHP
- 什么是PHP
  - 超文本预处理器
  - php是一种服务器端的脚本语言
  - 是嵌入到HTML中的语言

- php版本
  - php5
  - php7(7.4为分水岭)
  - php8

- php使用方式
```php
# 需要标记开始和结束
# 格式1：
<?php
    php代码
?>

# 格式2：短标签
<?
    php代码
?>
# 这种情况需要在php.ini的配置文件中，设置short_open_tag = on，默认为off
# 查找配置文件路径
# 创建一个php探针文件
<?php phpinfo(); // 它可以查看当前php的版本及当前环境相关信息

# 格式3：asp风格
<% 
    php代码
%> # php7之后不支持

# 格式4：脚本语言风格
<script language=`php`>php代码</script>
# php7之后不支持
```
```php
# 一个php文件内，可以有多个标记
<?php
    php代码
?>

<p>文本</p>

<?php
    php代码
?>
```
```php
# 如果文件中都是php代码，那么可以只写开始，不写结束
<?php php代码
```