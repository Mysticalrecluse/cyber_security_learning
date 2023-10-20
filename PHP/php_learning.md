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

### php标记
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

### php注释
```php
<?php
    // 单行注释
    # 单行注释

    /*

    多行注释

    */
?>
```
### php特性
- php可以多语言混编
- php5版本以前，php代码的最后一个代码，可以不写`;`，后面的版本不行，会报错
### 输出函数
- 命令：`echo`
  - 用法：
    - echo 是一个语言结构，而不是函数，所以你可以不使用括号来调用它（尽管使用括号也是可以的）。
    - 用于输出一个或多个字符串。
  - 示例
  ```php
  echo "Hello, World!"; 
  echo "<br>";
  echo "This ", "string ", "was ", "made ", "with multiple parameters.";
  // This string was made with multiple parameters.多个字符串自动拼接

  $a = 1
  $b = 2
  echo $a,'+',$b,'=',$a+$b; // 1+2=3
  ```
  - 对于echo、print_r、var_dump来说，php解析空白字符和转义字符但是浏览器不会解析，浏览器默认解析的是HMTL。 证明php可以解析，可以再命令行中，执行以下代码
  ```php
  echo "  hello\nworld" //在命令行中显示如下
  //  hello
  //world
  ```
  - 特点：
    - 只能用于输出字符串。
    - 不能输出数组或对象的结构。

- 命令：`print_r`
  - 用法：
    - 打印关于变量的易于理解的信息，特别适合于输出数组内容。
    - 如果为 print_r() 提供第二个参数并设置为 true，则不会输出信息，而是返回信息。
  - 示例：
  ```php
  $arr = array('a', 'b', 'c');
  print_r($arr);

  // 使用返回值而不是输出
  $output = print_r($arr, true); // 返回值的类型是String
  ```
  - 特点：
    - 可以输出数组和对象的内容。
    - 输出的结构较为简洁。
    - 适用于调试目的。

- 命令：`var_dump`
  - 用法：
    - 输出变量的内容、类型和值。
    - 它提供比 print_r() 更详细的信息，如字符串的长度、对象的属性等。
  - 示例：
  ```php
  $arr = array('a', 'b', 'c');
  var_dump($arr);
  ```
  - 特点：
    - 可以输出数组、对象、资源等的详细内容。
    - 显示数据类型和数据大小。
    - 适用于更详细的调试。

### php弱类型说明与传值传址详解
- 变量
```php
$name = 'houdunren.com' // php是弱类型语言，不用事先声明数据类型

// 变量：$名称 = 赋值

// 为三种变量赋值
$myCounter = 1;  //数字
$myString = "Hello";  // 字符串 
$myArray = array("One","Two","Three"); // 数组
```

- 显示变量内容
  - 命令：`echo`
```php
$username = "mystical";
echo $username;
```

### 数组
- 创建数组
```php
// array();
$team = array('Bill','Mary','Chris','Anne','Mike');

// 显示数组中的元素
echo $team[3]; // 显示Anne
```

- 二维数组
```php
$oxo = array(
    array('x',' ','o'),
    array('o','o','x'),
    array('x','o',' ')
);

// 返回指定数组的内容
echo array[0][2] // 'o'
```

- 数据的传值
```php
$a = 1;
$b = $a;
$b = 3;
echo $a; // 1
echo $b; // 2

// 原理和Javascript中基本数据类型的赋值相同
// $a 和 $b 分别在内存空间中开辟了不同地址存放数据，二者互不影响
```

- 数据的传址
```php
$a = 1;
$b = &$a; // 此时$b指向了$a的数据存储空间，二者执行的数据地址相同 
$b = 3;
echo $a; // 3
echo $b; // 3
echo '<hr/>'; //支持解析html标签
$a = 9;
echo $b; // 9
echo $a; // 9
```

### 可变变量与变量作用域
- 可变变量
```php
$name = 'word';
$$name = 'houdunren.com'; // 等同于$word = "houdunren.com"
echo $word; // 或者 echo $$name;
```
- 超全局变量
  - 概述：代码的任何位置都可以访问的变量
<table>
    <thead>
        <th style="background-color:darkred;color:white;">变量</th>
        <th style="background-color:darkred;color:white;">说明</th>
    </thead>
    <tbody>
        <tr>
            <td>$_GET</td>
            <td>地址栏GET提交</td>
        </tr>
        <tr>
            <td>$_POST</td>
            <td>表单POST提交</td>
        </tr>
        <tr>
            <td>$_FILES</td>
            <td>文件上传变量</td>
        </tr>
        <tr>
            <td>$_SESSION</td>
            <td>会话变量</td>
        </tr>
        <tr>
            <td>$_COOKIE</td>
            <td>cookie值变量/td>
        </tr>
        <tr>
            <td>$_GLOBALS</td>
            <td>全局变量</td>
        </tr>
        <tr>
            <td>$_REQUEST</td>
            <td>包含$_GET、$_POST、$_COOKIE</td>
        </tr>
        <tr>
            <td>$_SERVER</td>
            <td>服务器环境变量</td>
        </tr>
    </tbody>
</table>

```php
// var_dump($_GET);

function show() {
    print_r($GET) // 所谓超全局变量，在任何地方都可以直接调用
    //不受作用域影响
}
```

- 全局变量
```php
$name = "mystical";
function show() {
    echo $name;
}
show(); // 报错，php中函数内部无法使用函数外部声明的变量

// 如果一定要使用需要使用global进行声明
function show() {
    global $name; // 不推荐使用，防止全局污染
    echo $name;
    echo $GLOBALS['name']; //也能在函数内部直接调用函数外部的变量
}
// 这里$GLOBALS[]无法调用函数内部的声明
```

- 变量检测
  - 命令：`isset(变量)`
  - 作用：用来检测变量是否存在
  - 代码示例
  ```php
  $name = 'houdunren.com';
  var_dump(isset($name)); // 打印boolean:true说明变量存在
  var_dump(isset($noting)); // 打印boolean:false说明变量没声明过
  ```

- 删除变量
  - 命令`unset`
  - 代码示例：
  ```php
  unset($name);
  var_dump(isset($name)); // 之前删除了$name，所以打印结果为false

  场景2：
  $name = 'mystical';
  
  function make() {
    global $name;
    echo $name;
    unset($name);
  }
  make();
  echo $name; // mystical 在函数内部删除变量，不会影响到函数外部
  // 影响范围仅在函数内部
  ```

- 函数的静态变量
  - 关键字：`static`
  - 作用：将数据在函数体内持久保存
  - 代码示例：
  ```php
  function make()
  {
    $name = 1;
    $name += 1;
    return $name.'<hr/>';
  }
  echo make();
  echo make();
  echo make();

  function make(){
    static $num = 1; // 将$name的数据固定
    // static之后，函数的声明执行一次，后续再调用，不会再重新声明
    // 而不是每次执行完函数后，变量空间被回收，下次执行函数，重新赋值
    $num = $num + 1;
    return $num.'<hr/>';
  }
  echo make();
  echo make();
  echo make();
  ```