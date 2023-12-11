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
```php
$arr1 = Array(1,2,3);
$arr2 = &$arr1;
$arr2[0] = 4;
echo '<hr/>';
print_r($arr1);
echo '<hr/>';
print_r($arr2);
// 和js不同的是，数组的赋值并不是指向地址，也是开启一个新的内存空间
// 如果要将新变量指向同一个地址，和基本类型一样，也要使用&
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
// $GLOBALS[] 超全局数组;
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

## 数据类型
### 整型-进制转换
- 整型
```php
// 八进制 -> 十进制
$num = 777;
echo octdec($num);

// 十六进制 -> 十进制
echo hexdec($num);
```

### 布尔型
- 对象无论是否为空，都为真
- 空数组是假，null值为假
- 同Javascript

### php手册
- php.net 在线手册

### 字符串
- 双引号可以加变量
```php
$string = "houdunren.com";
echo "后盾人的网址 {$string}";
// echo "后盾人的网址$string"; 效果相同
// 双引号内可以直接引用变量
// 单引号不行

```
- 如果出现乱码，可以加header响应头解决编码问题
```php
header('Content-type:text/html;charset=utf-8');
```

- 字符串定界符
```php
$str = <<<php  
<h1 style="color:red;">mystical-recluse</h1>
php;
// php 可以替换为其他字符
echo $str;
```

- 字符串连接
```php
$str1 = "mystical";
$str2 = "recluse";
echo $str1.'-'.$str2;
```

- 字符串的函数

  - 获取字符串长度
  ```php
  // 获取字符串的长度
  $string = "mysticalrecluse" //15
  echo strlen($string);
  echo strlen('神秘隐士'); // 12 宽字节一个汉字占3个字节

  // 显示汉字(宽字节)的数量
  echo mb_strlen('神秘隐士','utf8');

  //
  ```
  - 删除左右字符数据
  ```php
  // trim(); 默认删除字符串两边的空格
  $string = ' mysticalrecluse '; // 15
  echo strlen($string);
  echo strlen(trim($string)); // 13
  echo strlen(trim($string,' esum'));  
  // 这里第二个参数表示左右删除的指定字符，以单个字符进行判定

  $str = " mysticalrecluse ";
  $str1 = trim($str,' emysr');
  echo $str.'<hr/>'; // mysticalrecluse
  echo $str1; // ticalreclu

  // 只删除左边的指定字符ltrim()

  // 只删除右边的指定字符rtrim()
  ```
  - 转大小写
  ```php
  $str = "HelloWorld";
  strtolower(); // 指定字符转换为小写
  echo strtolower($str);

  strtoupper(); // 指定字符转换为大写
  echo strtoupper($str);

  ucfirst() // 指定字符首字母大写

  ucwords() // 每个单词首字母大写，默认空格是分隔符
  // ucwords(字符串，分隔符)
  echo ucwords('hello,world',',');
  ```
  - md5加密（hash为一个32位的字符）
  ```php
  $passwd = "mystical";
  echo md5($passwd);
  ```
  - 字符串拆分
  ```php
  // explode(分隔符,字符串)
  // 生成数组
  print_r(explode('-','mystical-recluse')); 
  // Array ( [0] => mystical [1] => recluse ) 
  // 相当于Javascript中的split()
  ```
  - 字符串的合并
  ```php
  // implode(分隔符，数组)
  $arr = ['email','3140394153@qq.com'];
  echo implode(':',$arr);
  // 相当于JavaScript中的join()
  ```
  - 字符串截断
  ```php
  // substr(字符串，起始位置(索引), 终止到第几个字符);
  $str = "mystical";
  echo substr($str,0,3); // mys

  $ad = "大家好"
  echo mb_substr($ad,0,1,'utf-8')
  ```

### php常量
- define()定义常量
```php
<?php>
define('NAME', 'mystical');
define('NAME', 'mystical', true);
// 第3个参数表示常量标识符是否区分大小写
// true不区分， false严格区分
define('NAME', 'mystical', false);
echo name; // 报错
``` 

- const定义常量
```php
//...
const URL = "mystical.com"
```

- 常量不受访问限制
```php
const NAME = 'mytical';
function show() {
  echo NAME;
}
show(); // mystical
// 变量的话，函数内部无法访问函数外部
// 函数外部依然无法访问函数内部的常量
```

- 常量的检测
```php
define('URL', 'hd.cms');
var_dump(defined('URL'));  // true
var_dump(defined('URL_NAME'));  // false
```

- 系统常量
```php
echo PHP_VERSION // 打印php版本
echo PHP_OS // 打印服务器操作系统

class Demo{
    public function show(){
        echo __CLASS__; // 打印当前类名, 系统常量
        echo __METHOD__; // 打印当前方法名
    }
}

(new Demo())->show();
// Demo::show

echo __FILE__; // 打印当前文件路
```
- 查询源代码中，用户自定义的所有常量
```php
define('NAME', 'mystical');
const URL = 'hd.cms';
print_r(get_defined_constants(true)['user']);
// true参数的作用是分组显示，如何不填写，会比较凌乱
```

### 逻辑运算
```php
$a = 0;
$b = false;
var_dump($a == $b); // 会转换类型后比较：true
var_dump($a === $b); // 不转换类型：false
var_dump($a != $b); // false
var_dump($a !== $b); // true
```

### 三元表达式
```php
// ? :

// ??
$name = 0;
echo $name ? 'YES' : 'NO'; // NO
echo $name?:"NO"; // NO
// 如果 : 前面没值，若为真，则返回变量原本的值
echo $name ?? 'NO'; // 0
// ??前的变量存在且不为空，则在输入原值，如果为空或不存在输入??后的值

@(20/0) 忽略掉，屏蔽报错
echo 1; // 后面的echo正常执行
```

## 流程控制
### if语句
```php
if(true) {
  echo 'YES';
} 
else {
  echo 'NO';
}
// C语言风格可以正常识别

$status = false;
if($status):
    echo 'YES';
else:
    echo 'NO';
endif;
// 使用场景：
<?php
$status = false;
if ($status):
?>
<h1>hello, mystical</h>
<?php
else:
?>
<h1>please input a number</h1>
<?php
endif;
?>
// 当分支语句中，穿插html的时候，不用花括号会简洁一些
// 现在已很少使用·

// 多条件
$age = 10;
if ($age < 15) {
    echo 'child';
}
else if ($age < 30) {
    echo 'tee';
}
else if ($age < 50) {
    echo 'mid';
}
else {
    echo 'old';
}
```

### switch语句
```php
// 可以用C语言风格
$a = 98;
switch ($a % 3) {
    case 0: {
        echo "a % 3 = 0";
    }; break;
    case 1: {
        echo "a % 3 = 1";
    }; break;
    case 2: {
        echo "a % 3 = 2";
    }; break;
}

// 也可以使用php自己的风格，都差不多

switch ($a % 3) {
    case 0:
        echo "a % 3 = 0";
        break;
    case 1:
        echo "a % 3 = 1";
        break;
    case 2:
        echo "a % 3 = 2";
        break;
    default:
        // TODO
}

// 也可以用endswitch替代花括号
switch ($a % 3) :
    case 0:
        echo "a % 3 = 0";
        break;
    case 1:
        echo "a % 3 = 1";
        break;
    case 2:
        echo "a % 3 = 2";
        break;
    default:
        // TODO
endswitch;
```

### while循环
```php
$n = 5;
while ($n--) {
    echo 11;
}

// 这里的花括号可以变为endwhile
while ($n--):
    echo 11;
endwhile

echo "<hr/>"
do {
    echo 11;
} while ($n--)
// 这段代码是死循环，因为经过第一个while语句，$n的值已经为0
// 后面再进行$n--,n的值变为-1,任何非0值都为true，因此是死循环

do {
    if(!isset($num)) {
        $num = 10;
    } 
    echo ($num--)."<hr/>";
} while ($num--);
```

### for循环
```php
for ($num = 0; $num < 10; $num++) {
    echo $num;
} // 0123456789
```

## 文件引入
### include
```php
$name = 'mystical'
include '1.html'; 
// 作用相当于C语言中的#include
// 如果引用文件不存在，可以用@抑制警告，正常往下执行

if (!@include 'index.html') {
    include 'default.html';
}
```

### require强加载
```php
$name = 'mystical'
require ('index.html'); // 如果文件不存在，报错，致命错误
// 程序不会再往下执行
echo 333;
```

### include_once
```php
/**** 场景1：****/
include '2.php';
include "function.php";
echo show();
// 如果2.php和function.php中都含有show()，
// 则会因为重复定义相同函数导致报错

include_once '2.php';
include_once "function.php";
echo show();
// 如果重复则只加载一次
// 默认加载第一次，后面有重复的调用的，不再加载
```

### require_once
```
拥有require特性的include_once，重复调用，只加载第一次
// 有其他方法可以实现这个*_once特性
如果文件不存在，报致命错误
```

## 函数
### 函数定义
```php
function user() {
    //DOTO
}
user();
// 函数一定有返回值，在不适用return指定返回值的时候，系统默认返回NULL
```

### 简述命名空间
- 后面详解
```php
namespace User;
function make() {
    echo 'user';
} // user.php
```
```php
namespace model;
function make() {
    echo "model";  
} // model.php
```
```php
include 'user.php';
include 'model.php';
// 正常会报错，因为定义show()函数，但是可以用命名空间解决这个问题
/*
命名空间：
作用：将函数分组，不同组的同名函数可以一起使用
*/
User\make();
Model\make();
```

### 函数的参数传值
```php
function mobile($tel) {
    return substr($tel, 0, -4)."****";
}
echo mobile('13613600362');

/* 优化后 */
function mobile($tel, $num = 4, $fix = '*') {
    return substr($tel, 0, $num * -1).str_repeat($fix, $num);
}
echo mobile('13613600363', 4, '#');
```

### 函数的参数传址
```php
function show(&$var) {
    $var++;
    echo $var;
}
$var = 1;
show(&$var);
echo "<hr/>";
echo $var;
```

### 不定长参数-点语法
```php
function sum(...$var) {
    print_r($var);
}
sum(12,3,4,54,5); // 打印数组
```

### 函数参数的类型约束
```php
function show(int $num) {
  return $num
}
var_dump(show('2')); // int 2; 返回的是数字类型的2
// 如果传入的是字母，则报错，必须类型为int
// 在普通模式下，传递'2'会自动转换，不会报错
// 严格模式下会报错

declare(strict_types = 1);
function show(int $num) {
  return $num
}
var_dump(show('2')); // 报错
```

### 函数返回值约束
```php
function sum(): int
{
    return 'mystical'; //报错，上面要求返回值约束，必须是int
}
sum(); // 报错

function sum(): ?string
{
    return 'mystical'; 
    // 返回空值的话，必须指明null,eg: return null;
}
sum(); // ?string表示返回值可以是空值或字符串，

function sum(): void
{
    // void表示可以无返回值
}
```
```php
function sum(int ...$nums): int
{
    static $sum = 0;
    return $sum += array_sum($nums);
}
echo sum(1,2,3); // 6
echo "<hr/>";
echo sum(1,2,3); //12
```

### 变量函数
```php
function sum() {
    return 'function sum';
}
$callback = 'sum';
echo $callback();
```
```php
$file = "hdcms.jpg";
$type = trim(strrchr($file, '.'), '.');
$action = strtolower($type);
echo $type;

function jpg() {
    return 'jpg function';
}

function png() {
    return 'png function';
}
if (function_exists($action)):
    echo $action($file);
else :
  echo "NO";
endif;
```

## 数组
### 数组的声明
```php
$arr = array(
  1,2,3
);
print_r($arr);

$arr = [1,2,3]; // 推荐方法
```

### 数组分类
```php
/* 索引数组 */
$arr = [1,2,3];
// Array ( [0] => 1 [1] => 2 [2] => 3 )

/* 关联数组 */ // 类似字典
$article = [
    'title' => 'Visual Studio Code',
    'create_at' => "2020-2-22"
];

/* 同时使用 */
$lessons = [
    ['title' => 'Visual Studio Code', 'create_at' => '2030-2-22'],
    ['title' => 'Laravel 5.6', 'create_at' => '2030-12-12']
];
echo $lessons[0]['title']
```

### 通过指针读取数组元素
```php
$arr = ['xiaoming'];
$arr[] = 'lisi';
$arr[] = 'xiangjun';
$arr[] = 'xiaoli';
// 索引自动递增
```
```php
/* key */
// 获取数组第一个的下标/键
$arr = ['mystical', 'hdcms'];
echo key($arr); // 0

/* current */
// 获取数组第一个值 
echo current($arr); // mystical

/* next */
// 指针向下移动一位，并返回当前元素
echo next($arr); 

/* prev */
// 指针向上移动一位，并返回当前值
echo prev($arr);
// 如果指针向下或向上移动后，没有值，则返回false
```
- 练习代码
```php
$users = [
  ['name' => 'mystical', "age" => '16'],
  ['name' => 'curry', "age" => '19'],
  ['name' => 'kobe', "age" => '23'],
  ['name' => 'jamse', "age" => '16']
];
<table border="1">
    <tr>
        <th>编号</th>
        <th>姓名</th>
        <th>年龄</th>
    </tr>
    <?php while($user = current($users)):?>
    <tr>
        <td><?php echo key($users) + 1;?></td>
        <td><?php echo $user['name'];?></td>
        <td><?php echo $user['age'];?></td>
    </tr>
    <?php next($users); endwhile;?>
</table>
```

### 数组遍历
- list
```php
$arr = ['mystical', 'hdcms'];
list($a, $b); = $arr;

$user = ['name'=>'mystical', 'age'=>33];
list('name'=>$name, 'age'=>$age) = $user;
echo $age;// 33

/* 只取数组的某一个值 */
$arr = ['mystical', 'kobe', 'curry'];
list(,,$web) = $arr;
echo $web; // curry

/* 遍历数组 */
$users = [
  ['name' => 'mystical', "age" => '16'],
  ['name' => 'curry', "age" => '19'],
  ['name' => 'kobe', "age" => '23'],
  ['name' => 'jamse', "age" => '16']
];
while(list('name'=>$name, 'age'=>$age) = current($users)):
    echo "name:{$name}, age:{$age} <br/>";
    next($users);
endwhile;
```

- foreach
```php
/* 遍历索引数组 */
foreach($users as $user){
    printf($user);
}

/* 遍历关联数组 */
foreach($users as $key=>$user){
    $user['age'] += 50;
}
echo $users
//仅遍历，对函数外部的数据无影响 

/* 传值，数据二次处理 */
foreach($users as $key=>&$user){
  //$users[$key]['age'] += 50;
    $user['age'] += 50;
}
echo $users
```

### 数组函数
```php
$users = ['mystical', 'curry'];
/* arr_push() */
// 在结尾增加一个值，改变原数组，$user传的是地址
array_push($users, 'lisi');

/* array_pop() */
// 从结尾弹出一个值，改变原数组，返回值是弹出的值
$user = array_pop($users);

/* array_unshift() */
// 在开头添加一个值， 改变原数组
array_unshift($users, 'kobe');

/* array_shift() */
// 弹出开头的值，并返回
$start = array_shift($users);
print_r($users);
echo $start;

/* count() */
// 返回数组元素个数
echo count($users);

/* array_key_exists() */
// 检测数组的键名是否存在
$allowImageType = ['jpeg'=>20000, 'jpg'=>20000, 'png'=>2000];
$file = 'hdcms.txt';
$ext = strtolower(substr(strrchr($file, '.'), 1));
echo $ext; 
if (!array_key_exists($ext, $allowImageType)) {
    echo 'wrong';
} else {
    echo 'success';
}

/* in_array() */
// 检测数组的值是否在数组中
$allowImageType = ['jpeg', 'jpg', 'png'];
$file = 'hdcms.txt';
$ext = strtolower(substr(strrchr($file,'.'), 1));
if(!in_array($ext, $allowImageType)) {
    echo "error";
} else {
    echo "success";
}

/* array_keys()*/
// 将数组中的所有键组成一个新数组
$allowImageType = ['jpeg'=>20000, 'jpg'=>20000, 'png'=>20000];
$file = 'hdcms.txt';
$ext = strtolower(substr(strrchr($file,'.'), 1));
if(!in_array($ext, array_keys($allowImageType))) {
    echo "error";
} else {
    echo "success";
}

/* array_filter() */
// 数组筛选
$users = [
  ['name' => 'mystical', "age" => '16'],
  ['name' => 'curry', "age" => '19'],
  ['name' => 'kobe', "age" => '23'],
  ['name' => 'jamse', "age" => '16']
];
$filterUsers = array_filter($users, function($user) {
    return $user['age'] > 20;
});
print_r($filterUsers);

/* arraymap */
// 对数组中每个元素进行操作后，返回新数组
$mapUsers = array_map(function($user){
    unset($user['age']);
    return $user;
},$users);
print_r($mpaUsers);

/* array_values */
// 去元素的值，生成新的数组
$stringUsers = array_map(function($user){
    return implode('-', array_values($user));
}, $users)

/* array_merge() */
// 数组的合并，有相同值，会被覆盖
$arr = ['host'=>'localhost', 'port'=>3306, 'user'=>'root'];
print_r(
    array_merge($arr, ['passwd'=>'admin123'])
);

/* array_change_key_case() */
// 将数组的键名全部更改大小写，CASE_UPPER: 1,CASE_LOWER: 0 
$database = include 'config/database.php';
$database = array_change_key_case($database, 1);
print_r($database);

// 使用递归改变多层数组键名
$database = include '../49/config/database.php'
function hd_array_change_key_case(array $data,int $type=CASE_UPPER):array{
    foreach ($data as $key=>$value):
      $action = $type==CASE_UPPER?'strtoupper':'strtolower';
      unset($data[$key]);
      $data[$action($key)] = is_array($value)?hd_array_change_key_case($value, $type):$value;
    endforeach;
    return $data;
}
```

###  超高效的数组值多维操作
```php
/* array_walk_recursive() */
// 操作数组中的键值（能深入到子数组）
// array_walk_recursive 只对数组的值进行操作，不改变键
$database = include 'database.php';
function array_change_value(array &$data, int $type=CASE_UPPER):array{
    array_walk_recursive($data, function(&$value, $key, $type) {
        $action = $type == CASE_UPPER ? 'strtoupper' : 'strtolower';
        $value = $action($value);
    }, $type);
    return $data;
}
array_change_value($database, CASE_UPPER);
print_r($database);
```

### var_export()
- 作用：将数组转换为合法的php语法格式的字符串
```php
$database = include 'database.php';
$config = var_export($database, true);
// true表示有返回值，返回值为合法的字符串
file_put_contents('database.php', '<?php return'.$config);
// var_export()的作用是生成的php语法的字符串，在别的文件中，依然可以被php环境引用执行
```

### 序列化与反序列化
```php
/* serialize() */
// 序列化
$database = include 'database.php';
$cache =  serialize($database);
// 将php语法的数组，序列化转换为所有语言都能识别的字符串

/* unserialize() */
// 反序列化
$database = include 'database.php';
$cache = serialize($database);
print_r(unserialize($cache));
```

### 序列化与反序列化的实际应用
```php
// 缓存
function cache(string $name, array $data=null) {
    $file = 'cache'.DIRECTORY_SEPARATOR.md5($name).'.php';
    // DIRECTORY_SEPARATOR是表示php中目录分隔符/的常量
    if(is_null($data)) {
        // 取缓存
        $content = is_file($file)?file_get_contents($file):null;
        return unserialize($content)?:null;
    } else {
        return file_put_content($file, serialize($data));
        // 存缓存
    }
}
$config = include "database.php";
cache('database', $config);
```

## 日期与时间
### 时区
```php
// PRC Asia/chongqing  Asiz/shanghai Asia/urumqi
/* 修改默认时区 */
date_default_timezone_set('Asia/shanghai');

/* 查看当前时间 */
echo dete('Y-m-d H:i:s'); // 如果不修改默认时区，则默认伦敦时间
echo dete('Y年m月d日 H时i分s秒');

/* 指定时间*/
echo date('Y年m月d日 H时i分s秒', time()-3600*24)
// 第二个参数通过设置时间戳数值，来修改到指定时间

// 实际工作中，上述函数基本用不到，因为都是框架开发，直接改配置文件
```

### 时间戳
```php
// 从1970-1-1 0：0：0开始，到现在的秒数
data_default_timezone_set('Asia/shanghai');

echo time(); // 输出时间戳

echo microtime(true); // 返回微秒
/* 一般用来计算程序执行时间 */
function runtime($start = null, $end = null) {
    static $cache=[];
    if (is_null($start)) {
        return $cache;
    } elseif (is_null($end)) {
        return $chache[$start] = microtime(true);
    } else {
        $end = $cache[$end]??microtime(true);
        return round($end - $cache[$start]);
    }  
}
```

- getdate()
```php
print_r(getdate());
// getdate()得到一个数值，可以通过遍历数组和取数组的值，来获得时间元素
/*

Array
(
    [seconds] => 59
    [minutes] => 39
    [hours] => 11
    [mday] => 6
    [wday] => 3
    [mon] => 12
    [year] => 2023
    [yday] => 339
    [weekday] => Wednesday
    [month] => December
    [0] => 1701862799
)

*/

```

- iso字符串和时间戳的转换
```php
// iso -> 时间戳
strtotime(1995-04-08);

echo strtotime("now"), "\n";
echo strtotime("10 September 2000"), "\n";
echo strtotime("+1 day"), "\n";
echo strtotime("+1 week"), "\n";
echo strtotime("+1 week 2 days 4 hours 2 seconds"), "\n";
echo strtotime("next Thursday"), "\n";
echo strtotime("last Monday"), "\n";

// 综合实例
echo date("Y-m-d", strtotime("+7 day"));
```

### 日期相关类
```php
// DataTime, DataInterval, DataTimezone
$prc = new DateTimezone('PRC');
$dateTime = new DateTime(); // 由类得到实例对象
print_r($dateTime);
$dateTime->setTimezone($prc);
$dateTime->setDate(2019, 2, 12);
$dateTime->setTime(12, 22, 12);
echo "<br/>";
echo $dateTime->format('Y-m-d H:i:s');
echo "<br/>";
echo $dateTime->setTimestamp(time());

/* 计算两个日期相差的差值 */
$dateTime1 = new DateTime();
$dateTime2 = new DateTIme("2024-3-1");
$interval = $dateTime1->diff($dateTime2);
$format = '距离结课还有<span style="color:red">%m个月%d天</span>, 共有%a天';
echo $interval->format($format);

/* 增加时间 */
$dateTime = new DateTime();
$interval = new DateInterval('P2DT2H5M');
// 参数以P开头，日期和时间用T分隔
echo $dateTime->format('Y-m-d H:i:s');
echo "<br/>";
$dateTime->add($interval);// 增加
echo $dateTime->format('Y-m-d H:i:s');
$dateTime = sub($interval);// 减少
echo "<br/>";
echo $dateTime->format('Y-m-d H:i:s');

```


