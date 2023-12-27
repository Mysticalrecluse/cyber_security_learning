# thinkphp6概述
## thinkphp6的安装
- 详情见composer教程

- Linux或Mac中，runtime目录权限设置为777

- 进入下载好的工程目录后，运行
```php
php think run // 可以把首页自动指向public
php think run -p 80 // 可以向端口指向80
```

## 开发规范
- ThinkPHP6遵循的是PSR-2的命名规范和PSR-4的自动加载

- 目录和文件的规范如下
  - 目录名（小写+下划线）；
  - 类库和函数文件统一以.php为后缀
  - 类的文件名均以命名空间定义，并且命名空间的路径和类库文件所在路径一致
  - 类（包含接口和Trait）文件采用驼峰命名（首字母大写），其他采用小写+下划线命名；
  - 类名和文件名保持一致，统一采用驼峰式命名（首字母大写）； 

- 其他如类，常量，函数方法等规范和php基础中一致

## 目录结构
- ThinkPHP6.0支持多应用模式部署，app是应用目录

- 生产环境下，只确保对外可访问的仅public目录 

## 调试与配置文件
- 开启调式
  - 在开发阶段，建议开启框架的调试模式
  - 调试模式开启后，会牺牲一些执行效率，但大大提高了开发排错的能力
  - 当项目部署到生产环境时，再关闭调试模式即可
  - 没开启调试模式，出现错误之后，只会提示“页面错误，请稍后重试”，无其他有用信息
  - 开启调试模式过程
    - 将根目录文件.example..env更改为.env即可
    - 通过.env文件中APP_DEBUG=true|false开控制调试模式的开启与关闭
  - 开启调试模式的优势
    - 记录系统运行流程的执行过程
    - 展示错误和调试信息，并开启日志记录
    - 模板修改可以即使生效（不会被缓存干扰）
    - 启动右下角的Trace调试功能，更强大
    - 发生异常时，也会显示异常信息
  - 简化调试模式：关闭调试模式，也可以显示简要的错误信息
    - 关闭调试模式：APP_DEBUG = false;
    - 然后根目录config的app.php最后一项设置为：
    ```php
    'show_error_msg' => true,
    ```

- 配置信息
  - 配置文件有两种，.env是一种，适合本地
  - 另一种配置文件：根目录下config目录中的文件，适合部署
  - <font color=tomato>官方手册明确标识：.env环境变量用于本地开发测试，部署后会被忽略</font>
  - 关于这两种配置文件的优先级，在本地测试时，env优先于config;
  - 从config配置中可以看出，先读取.env，然后再默认配置一个自己的
  - 而到了部署环境，.env会被忽略，则自动切换到config配置

## URL访问模式
### URL解析
- ThinkPHP框架非常多的操做都是通过URL来实现的；

#### 多应用
- 多应用：`http://serverName/index.php/应用/控制器/操做/参数/值`

- 多应用扩展安装 
```
composer require topthink/think-multi-app
```

- 安装后，composer.json文件内
```php
"require": {
        "php": ">=7.2.5",
        "topthink/framework": "^6.1.0",
        "topthink/think-orm": "^2.0",
        "topthink/think-filesystem": "^1.0",
        "topthink/think-multi-app": "^1.0"
    }
```

- 修改目录结构
  - 在app目录下，创建多个文件目录，每个目录即一个应用目录
  - 在新建的应用目录下，创建一个controller目录，并在里创建一个控制器文件
  ```php
  namespace app\mystical\controller;

  // 空间名和文件夹一致
  // 类名和文件名一致 类名遵守大驼峰规则
  // 目的：实现自动加载

  // 使用其他类时，需要先将类引入，使用use
  use app\BaseController;

  // 一般的控制器，都会继承基础控制器类
  // 基础控制器中，定义公共方法和属性，使得所有继承它的类都能够是使用
  class Mystical extends BaseController{
        // 方法名遵守小驼峰规则
        public function index()
        {
            echo 333;
        }
  }
  ```
  - URL重写
  ```php
  // 在开放接口页面的同级目录下，更改或创建.htaccess文件
  <IfModule mod_rewrite.c>
    Options +FollowSymlinks -Multiviews
    RewriteEngine On

    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ index.php [L,E=PATH_INFO:$1]
  </IfModule>
  ```
  
- 单应用：`http://serverName/index.php/控制器/操做/参数/值`
  - index.php这个文件，是根目录下public下的index.php（入口文件）
  - 控制器：app目录下有一个controller控制器目录的Test.php（类名与文件名必须一致）
  - 操做：控制器类里面的方法
  - public/index.php中的index.php可以省略，只要设置url重写即可
    - httpd.conf配置文件中加载了mod_rewrite.so模块；
    - AllowOverride None 将None 改为 All；
    - 此时路径中可以省略index.php
  
- TP6.0默认单应用模式


## 控制器
### 控制器的控制方式
- 控制器即controller，控制器文件存放在controller目录下
  
- 如果想改变系统默认的控制器文件目录，可以在config下route.php配置
  
- 如果创建双字母组合，比如class HelloWorld，访问URL如下：
  - http://localhost:port/test/pulic/helloworld
  - http://localhost:port/test/pulic/hello_world

- 如果你想避免引入同类名时的冲突，可以route.php设置控制器后缀
```php
'controller_suffix' => true,
// 此时Test.php就必须改成TestController.php，并且类名也需要增加后缀
```

### 渲染输出
- TP直接采用方法中的return方式就直接输出了

- 使用json输出，直接采用json函数
```php
使用json输出，直接采用json函数
$data = array('a'=>1, 'b'=>2, 'c'=>3);
return json($data);
```

- 如果中断代码测试，不推荐使用die,exit等php方法，推荐助手函数halt()
```php
halt('中断测试');
```

### 基础控制器
- 一般来说，创建控制器后，推荐继承基础控制器来获得更多的方法
- 基础控制器仅仅提供了控制器验证功能，并注入了think\App和think\Request；
- 这两个对象后面会有章节详细讲解，下面我们继承并简单使用一下；
```php
namespace app\controller;
use app\BaseController;

class Test extends BaseController
{
    public function index()
    {
        // 返回实际路径
        return $this->app->getBasePath();
        // 返回当前方法名
        return $this->request->action();
    }
}
```

### 空控制器
- 在单应用模式下，我们可以给项目定义一个Error控制类，来提醒错误；
```php
class Error
{
    public function index()
    {
        return '当前控制器不存在';
    }
}
```

### 多级控制器
- 所谓多级控制器，就是在控制器controller目录下再建立目录并创建控制器

- 我们在controller目录下创建group目录，并创建Blog.php控制器
  - 此时我们需要访问地址：http://localhost:8000/group.blog

## 数据库
### 连接数据库
- 修改配置文件config目录下的database.php
- 同步更改.env里的数据库配置信息
- 在controller下创建一个DatabaseTest.php文件，内容如下，测试数据库是否连接成功
```php
namespace app\controller;

use think\facade\Db;

class DatabaseTest
{
    public function index()
    {
        $user = Db::table('users')->select();
        return json($user);
    }
}
```
- 连接多个数据库
- 在database.php配置文件下，添加多个数据库信息
```php
<?php

return [
    // 默认使用的数据库连接配置
    'default'         => env('database.driver', 'mysql'),

    // 自定义时间查询规则
    'time_query_rule' => [],

    // 自动写入时间戳字段
    // true为自动识别类型 false关闭
    // 字符串则明确指定时间字段类型 支持 int timestamp datetime date
    'auto_timestamp'  => true,

    // 时间字段取出后的默认时间格式
    'datetime_format' => 'Y-m-d H:i:s',

    // 时间字段配置 配置格式：create_time,update_time
    'datetime_field'  => '',

    // 数据库连接配置信息
    'connections'     => [
        'mysql' => [
            // 数据库类型
            'type'            => env('database.type', 'mysql'),
            // 服务器地址
            'hostname'        => env('database.hostname', '127.0.0.1'),
            // 数据库名
            'database'        => env('database.database', 'tptest'),
            // 用户名
            'username'        => env('database.username', 'root'),
            // 密码
            'password'        => env('database.password', ''),
            // 端口
            'hostport'        => env('database.hostport', '3306'),
            // 数据库连接参数
            'params'          => [],
            // 数据库编码默认采用utf8
            'charset'         => env('database.charset', 'utf8'),
            // 数据库表前缀
            'prefix'          => env('database.prefix', ''),

            // 数据库部署方式:0 集中式(单一服务器),1 分布式(主从服务器)
            'deploy'          => 0,
            // 数据库读写是否分离 主从式有效
            'rw_separate'     => false,
            // 读写分离后 主服务器数量
            'master_num'      => 1,
            // 指定从服务器序号
            'slave_no'        => '',
            // 是否严格检查字段是否存在
            'fields_strict'   => true,
            // 是否需要断线重连
            'break_reconnect' => false,
            // 监听SQL
            'trigger_sql'     => env('app_debug', true),
            // 开启字段缓存
            'fields_cache'    => false,
        ],
        // 添加新数组，连接多个数据库
        'mysql2' => [
            // 数据库类型
            'type'            => env('database.type', 'mysql'),
            // 服务器地址
            'hostname'        => env('database.hostname', '127.0.0.1'),
            // 数据库名
            'database'        => env('database.database2', 'atguigudb'),
            // 用户名
            'username'        => env('database.username', 'root'),
            // 密码
            'password'        => env('database.password2', 'Zyf646130..'),
            // 端口
            'hostport'        => env('database.hostport2', '3308'),
            // 数据库连接参数
            'params'          => [],
            // 数据库编码默认采用utf8
            'charset'         => env('database.charset', 'utf8'),
            // 数据库表前缀
            'prefix'          => env('database.prefix', ''),

            // 数据库部署方式:0 集中式(单一服务器),1 分布式(主从服务器)
            'deploy'          => 0,
            // 数据库读写是否分离 主从式有效
            'rw_separate'     => false,
            // 读写分离后 主服务器数量
            'master_num'      => 1,
            // 指定从服务器序号
            'slave_no'        => '',
            // 是否严格检查字段是否存在
            'fields_strict'   => true,
            // 是否需要断线重连
            'break_reconnect' => false,
            // 监听SQL
            'trigger_sql'     => env('app_debug', true),
            // 开启字段缓存
            'fields_cache'    => false,
        ],

        // 更多的数据库配置信息
    ],
];
```
- 然后即可在控制器中连接查询多个数据库
```php
namespace app\controller;

use think\facade\Db;

class DatabaseTest
{
    public function index()
    {
        $user = Db::table('users')->select();
        return json($user);
    }
    public function guigu()
    {
        $employee = Db::connect('mysql2')->table('employees')->select();
        return json($employee);
    }
}
```

### 初探模型
- 在app目录下创建一个model目录，并创建User.php的模型类;
```php
namespace app\model;
use think\Model;

class User extends Model
{
    protected $connection = 'demo';
}
```
- 然后再控制器端的调用如下
```php
public function getUser()
{
    $user = User::select();
    return json($user);
}
```

### 数据查询
#### 单数据查询
- Db::table()中table必须指定完整数据包（包含前缀）；

- 如果希望只查询一条数据，可以使用find()方法，需指定where条件
```php
// 只查询一条
Db::table('employees')->where('id', 101)->find();
// 查询所有
Db::table('employees')->where('id', 101)->select();
```
- Db::getLastsql()方法，可以得到最近一条SQL查询的原生语句；

- 没有查询到任何值，返回null；

- 使用findOrFail()方法同样可以查询一条数据，在没有数据时，抛出异常；
```php
Db::table('users')->where('age > 20')->findOrFail()
```

- 使用findOrEmpty()方法也可以查询一条数据，但在没有数据时返回一个空数组；
```php
Db::table('users')->where('id', 1)->findOrEmpty();
```

#### 指定字段
```php
Db::table('users')->field('uid')->select();
// 多字段查询
Db::table('employees')->field('employee_id, first_name')->select();
// 带别名查询
Db::table('employees')->field('employee_id id, first_name name')->select();
```

#### 数据集查询
```php
// 查询所有数据，如果查询不到任何值，返回空数组
Db::table('users')->where('age > 20')->select();

// 多列数据在查询不到任何数据时抛出异常
Db::table('users')->where('age > 100')->selectOrFail();

// 在select方法后再使用toArray()方法，可以将数据集对象转换为数组
$user = Db::table('users')->where('age > 20')->select()->toArray();
dump($user);

// 当在数据库配置文件中设置了前缀，那么我们可以使用name()方法忽略前缀；
Db::name('user')->select(); // 此时name()替代table()
```

#### 其他查询
```php
// 通过value()方法，可以查询指定字段的值（字符串）（单个），没有数据返回null
$employee = Db::table('employees')->where('id', 101)->value('first_name');
return $employee // Neena

// 通过column()方法，可以查询指定列的所有值，返回索引数组，没有数据返回空
$employee = Db::table('employees')->column('first_name');

// 返回employee_id为键，first_name为值得关联数组
$employee = Db::table('employees')->column('first_name', 'employee_id');
dump($employee); 
```

- 优化：当数据过大时，为了节省内存开销，使用chunk()分批处理
```php
Db::table('employees')->chunk(5, function($users){
    foreach ($users as $user) {
        dump($user);
    }
});
```

- 优化方案2：可以利用游标查询功能，可以大幅度减少海量数据的内存开销，它利用了PHP生成器特性。每次查询只读一行，然后再读取时，自动定位到下一行继续读取
```php
$cursor = Db::table('employees')->cursor();
foreach($cursor as $user) {
    dump($user);
}
```

#### 数据库链式查询
- 将连接到数据表的值赋给变量，防止多次查询反复创建实例
```php
$userConnection = Db::connect('mysql2');
$userQuery = $userQuery->table('employees');

// 多次调用进行查询的时候，变量会记录查询状态
// 需要使用removeOption进行初始化
$data1 = $userQuery->order('employees_id', 'desc')->select();
$data2 = $userQuery->removeOption('order')->select();
return $userConnection->getlastsql(); // 多数据库连接的时候，注意当前数据库的实例
// Db::默认Db::contect('mysql')
```

### 数据新增
#### 单数据新增
```php
$data = [
    'name'  =>  'james',
    'age'   =>  39,
    'gender'=>  'male', 
    'hobby' =>  'exercise'
];
// 添加不存在的字段会抛出异常
$insert = Db::table('users')->insert($data); // 返回新增行数

// 如果数据中有不存在字段，但是不报错，忽略错误字段继续执行添加操做
Db::table('users')->strict(false)->insert($data);

// insert和replace写入的区别：
// insert添加主键的时候，如果数据相同，则报错，因为主键非空唯一
// replace，如果需要添加主键数据相同的情况，不报错，而是需改主键数据为新添加的数据
Db::table('users')->insert($data);
Db::table('users')->replace()->insert($data);

// 使用insertGetId()方法，可以在新增成功后返回当前数据ID;
// 如果表格中无id字段，则返回1
Db::table('users')->insertGetId($data);
```


#### 批量数据新增
- 使用insertAll()方法，可以批量新增数据，但要保持数组结构一致
```php
public function insertAll()
{
    $dataAll = [
        [
            'name'  =>  'Xiaoming',
            'age'   =>  20,
            'gender'=>  'male', 
            'hobby' =>  'computer'
        ],
        [
            'name'  =>  'Xiaohong',
            'age'   =>  16,
            'gender'=>  'female', 
            'hobby' =>  'Pets'
        ]
    ];

    return Db::table('users')->insertAll($dataAll);
}

// 批量新增也支持replace()方法，相同和之前一样
Db::table('users')->replace()->insertAll($dataAll);
```

#### save()新增
- save()方法是一个通用方法，可以自行判断是新增还是修改（更新数据）；
- save()方法判断是否为新增或修改的依据是，是否存在主键，不存在即新增；

### 数据修改
- 使用update()方法来修改数据，修改成功返回影响行数，没有修改返回0；
```php
$data = [
    'name' => 'leiou'
];
return Db::table('users')->where('age', 12)->update($data);
```

- 如果修改数据包含主键信息，比如id，那么可以省略掉where条件
```php
$data = [
    'id'    =>      2,
    'name'  =>      'leiou'
];
return Db::table('users')->update($data);
```

- 如果想让一些字段修改时执行SQL函数操做，可以使用exp()方法实现
```php
Db::table('users')->where('id', 232)
->exp('email', 'UPPER(email)')->update();
```

- 如果要自增/自减某个字段，可以使用inc/dec方法，并支持自定义步长
```php
Db::table('users')->where(id, 232)
                  ->inc('price')
                  ->dec('status', 2)
                  ->update();
```

- 也可以使用raw()方法实现SQL函数操做和自增自减
```php
Db::table('users')->where('id', 232)
                  ->update([
                    'email'     =>      Db::raw('UPPER(email)'),
                    'price'     =>      Db::raw('price + 1'),
                    'status'    =>      Db::raw('status - 2')
                  ]);
```

- 使用save()方法进行修改数据，这里必须指定主键才能实现修改功能
```php
Db::table('users')-> where('id', 232)->save(['username'=>'Leihei']);
```

### 数据删除
- 极简删除可以根据主键直接删除，删除成功返回影响行数，否则0
```php
Db::table('users')->delete(51);
```

- 根据主键，还可以删除多条记录
```php
Db::table('users')->delete([48, 49, 50]);
```

- 正常情况下，通过where()方法来删除；
```php
Db::table('users')->where('id', 47)->delete();
```

- 通过true参数删除数据表所有数据
```php
Db::table('users')->delete(true);
```

### 数据查询表达式
#### 比较查询
- 查询表达式支持大部分常用SQL语句，语法如下
```php
where('字段名', '查询表达式', '查询条件');
```

- 在查询数据进行筛选时，我们采用where()方法，比如id=80；
```php
Db::table('users')->where('id', 80)->find();
Db::table('users')->where('id', '=', 80)->find();
```

- 使用`<>、>、<、>=、<=`可以筛选出各种符合比较值得数据列表
```php
Db::table('users')->where('id', '<>', 80)->select();
```

#### 区间查询
- 使用like表达式进行模糊查询
```php
Db::table(users)->where('email', 'like', 'xiao%')->select();
```

- like表达式支持数组传递进行模糊查询
```php
Db::table('users')->where('email', 'like', ['xiao%', 'wu%'], 'or')->select();
// SELECT * FROM users WHERE (email LIKE 'xiao%' OR 'email' LIKE 'wu%');
// 不写第四个参数，默认是'and'
```

- like表达式具有两个快捷方式whereLike()和whereNoLike();
```php
Db::table('users')->whereLike('email', 'xiao%')->select();
Db::table('users')->whereNoLike('email', 'xiao%')->select();
```

- between表达式具有两个快捷方式whereBetween()和whereNotBetween();
```php
Db::table('users')->where('id', 'between', '19,25')->select();
Db::table('users')->where('id', 'between', [19, 25])->select();
Db::table('users')->whereBetween('id', '19, 25')->select();
Db::table('users')->whereNotBetween('id', '19, 25')->select();
```

- in表达式具有两个快捷方式whereIn()和whereNotIn();
```php
Db::table('users')->where('id', 'in', '19, 21, 29')->select();
Db::table('users')->where('id', 'in', [19, 21, 29])->select();
Db::table('users')->whereIn('id', '19, 21, 29')->select();
Db::table('users')->whereNotIn('id', '19, 21, 29')->select();
```

- null表达式具有两个快捷方式whereNull()和whereNotNull();
```php
Db::table('users')->where('uid', 'null')->select();
Db::table('users')->where('uid', 'not null')->select();
Db::table('users')->whereNull('uid')->select();
Db::table('users')->whereNotNull('uid')->select();
```

#### Exp查询
- 使用exp可以自定义字段后的SQL语句
```php
Db::table('users')->where('id', 'exp', 'IN (19, 21, 25)')->select();
Db::table('users')->whereExp('id', 'IN (19, 21, 25)')->select();
```

### 聚合.原生.子查询
#### 聚合查询
- 使用count()方法，求出所查询数据的数量
```php
Db::table('users')->count();
// count()可以指定字段，但是如果字段中有null数据，则不会计算这部分数量
```

- 使用max()方法，求出所查询数据字段的最大值
```php
Db::table('users')->max('price');
// 子查询案例
$maxSalary = $employees->max('salary');
$query = $employees->where('salary', $maxSalary)->select();
// $query = $employees->whereExp('salary', '=(select max(salary) from employees)')->select();
```

- 使用min()方法，求出所查询数据字段的最小值
```php
Db:table('users')->min('price');
```

- 使用avg()方法，求出所查询字段的平均值
```php
Db:table('users')->avg('price');
```

- 使用sum()方法，求出所查询数据字段的总和
```php
Db:table('users')->sum('price');
```

#### 子查询
```php
$res = Db:table('users')->fetchSql(true)->select();
// fetch()参数为true，则返回sql语句，不执行
// fetch()参数为false，则执行sql语句，默认为false

// 使用buildSql()
$res = Db:table('users')->buildSql(true);
// 返回带括号的sql语句，方便子查询拼接
```

- 使用闭包函数进行子查询
```php
$res = Db::table('users')->where('id', 'in', function($query){
    $query->table('two')->field('uid')->where('gender', 'male');
})->select();
```

#### 原生查询
- 使用query()方法，进行原生SQL语句查询
```php
Db::query('select * from employees');
```

- 使用execute()方法，进行原生SQL更新写入等执行操做
```php
Db::execute('upodate users set age = 15 where name = \'kobe\'');
```

### 链式查询方法
#### where详解
- 表达式查询，就是where()方法的基础查询方式
```php
// 上述常用的方式
Db::table('employees')->where('employee_id', '>', 150)->select();
```

- 关联数组查询，通过键值对数组键值对比配的方式查询
```php
$user = Db::table('employees')->where([
    ['department_id', '=', 90],
    ['salary', '>', 10000]
])->select();
// 数组之间取并集
```

- 将复杂的数组组装后，通过变量传递，将增加可读性
```php
$map[] = ['department_id', '=', 90];
$map[] = ['salary', '>', 10000];
$query = Db::table('employees')->where($map)->select();
```

- 字符串形式传递，简单粗暴的查询方式，whereRaw()支持复杂字符串格式；
```php
Db::table('employees')->whereRaw('department_id = 90 OR salary > 10000')->select();
```

- 如果SQL查询采用了预处理模式，比如id=:id，也能够支持；
```php
Db::table('employees')->whereRaw('employee_id=:id', ['id'=>20])->select();
$query = $employees->whereRaw('department_id=?', [20] )->select();
$query = $employees->whereRaw('department_id = ? OR salary > ?', [30, 5000])->select();
```

#### field详解
- 使用field()方法，可以指定要查询的字段
```php
Db::table('users')->field('name, age, gender')->select()
Db::table('users')->field(['name', 'age', 'gender'])->select()
```

- 使用field()方法，给指定字段设置别名
```php
Db::table('users')->field('id, username as name')->select();
Db::table('users')->field(['id', 'username' => 'name'])->select();
```

- 在fieldRaw()方法里，可以直接给字段设置MySQL函数
```php
Db::table('employees')->field('first_name, MAX(salary)')->select();
$query = $employees->fieldRaw('department_id, AVG(salary), MAX(salary)')->group('department_id')->select();
```

- 使用field(true)的布尔参数，可以显式的查询获取所有字段，而不是*
```php
Db::table('employees')->field(true)->select();
// 在getLastSql()后可以看到与field()的区别，一个是*,一个是显示性全部显示
```

- 使用withoutField()方法中字段排除，可以屏蔽掉想要不显示的字段
```php
Db::table('employees')->withoutField('commission_pct')->select();
```

- 使用field()方法在新增时，验证字段的合法性
```php
Db::table('employees')->field('first_name, department_id')->insert($data);
```

#### alias
- 使用alias()方法，给数据库起一个别名
```php
Db::table('employees')->alias('a')->select();
```

#### limit详解
- 使用limit()方法，限制获取输出数据的个数
```php
Db::table('employees')->limit(5)->select();
```

- 实现分页，需要严格计算每页显示的条数，然后从第几条开始
```php
// 第一页
Db::table('employees')->limit(0, 5)->select();
// 第二页
Db::table('employees')->limit(5, 5)->select();
```

#### page
- page()分页方法，优化了limit()方法，无须计算分页条数
```php
// 第一页
Db::table('employees')->page(1, 5)->select();
// 第二页
Db::table('employees')->page(2, 5)->select();
```

#### order
- 使用order()方法，可以指定排序方式，没有指定第二参数，默认asc
```php
Db::table('employees')->order('department_id', 'desc')->select();
```

- 支持数组的方式，对多个字段进行排序
```php
$dbConnection = Db::connect('mysql2');
$employees = $dbConnection->table('employees');
$query = $employees->order(['department_id'=>'asc', 'salary'=>'desc'])->select();
```

- 使用orderRaw()方法，支持排序的时候指定MySQL函数
```php
Db::table('users')->orderRaw('FILE(name, "curry") DESC')->select();
```

#### group
- 使用group()方法，给性别不同的人进行price字段的总和统计
```php
Db::name('user')->fieldRaw('gender, SUM(Price)')->group('gender')->select();
```
- 也可以进行多字段分组统计

#### having
- 使用group()分组之后，再使用having()进行筛选
```php
$dbConnection = Db::connect('mysql2');
$employees = $dbConnection->table('employees');
$query = $employees->fieldRaw('department_id, AVG(salary)')
                   ->group('department_id')
                   ->having('AVG(salary) > 5000')
                   ->select();
```

### 数据库高级查询
- 使用|（OR）或&（AND）来实现where条件的高级查询，where支持多个连缀
```php
$user = Db::table('user')
            ->where('username|email', 'like', '%xiao%')
            ->where('price&uid', '>', 0)
            ->select();
// 生成的SQL语句
/*
SELECT *
FROM user
WHERE (username LIKE '%xiao%' OR email LIKE '%xiao%')
AND (price > 0 AND uid > 0);
*/
```

- 关联数组方式，可以在where进行多个字段进行查询
```php
$user = Db::table('user')->where([
    ['id', '>', 0],
    ['status', '=', 1],
    ['price', '>=', 80],
    ['email', 'like', '%163%']
])->select();
// 生成SQL语句
/*
SELECT *
FROM user
WHERE id > 0
AND status = 1
AND price >= 80
AND email like '%163%';
*/
```

- 条件字符串复杂封装，比如使用exp自定义条件，然后使用raw()方法
```php
$user = Db::table('user')->where([
    ['status', '=', 1],
    ['price', 'exp', Db::raw('>80')]
    // 这里直接使用['price', 'exp', '>80']会报错
])->select();
```

- 如果使用$map变量接收数组，然后传参给where，后面的where不会将$map的条件作为整体，如果需要作为整体的话，需要给$map添加中括号[]
```php
$map = [
    ['id', '>', 0],
    ['price', '>=', 80],
    ['email', 'like', '%163%']
];

$user = Db::table('user')->where([$map])
                        ->where('status', '=', 1)
                        ->select();
```
- 如果，条件中有多次出现一个字段，并且需要OR来左右筛选，可以用whereOr;
```php
$map1 = [...];
$mpa2 = [...];
$user = Db::table('user')->whereOr([$map1, $map2])->select();
```

- 闭包查询可以连缀，会自动加上括号，更清晰，如果是OR，请用whereOR()
```php
$user = Db::table('user')->where(function ($query) {
    $query->where('id', '>', 10);
})->whereOr(function ($query){
    $query->where('username', 'like', '%xiao%');
})->select();
```

- 对于比较复杂或不知道如何拼接SQL条件，可以直接使用whereRAW()
```php
$user = Db::table('user')
            ->whereRaw('(username LIKE "%xiao%" AND email LIKE "%163%")
            OR (price > 80)')
            ->select();
```

- whereRaw()也支持预编译
```php
$user = Db::table('user')
            ->whereRaw('(username LIKE :username AND email LIKE :email)
            OR (price > :price)', 
            ['username'=>'%xiao%', 'email'=>'%163%', 'price'=>80])
            ->select();
```

- whereColumn()方法，比较两个字段的值，符合的就筛选出来；
```php
$user = Db::table('usr')
            ->whereColumn('update_time', '>=', 'create_time')
            ->select();
// 相等的话可以简化
whereColumn('update_time', 'create_time');
```

- whereFieldName()方法，查询某个字段的值，注意：FieldName是字段名
```php
Db::table('user')->whereEmail('xiaoxin@163.com')->find();
Db::table('user')->whereUsername('xiaohong')->find();
// 如果字段是create_time,则whereCreateTime,驼峰式写法
```

- getByFieldname()方法，查询某个字段的值，只能查询一条，不需要find()
```php
Db::table('user')->getByEmail('xiaoxin@163.com');
```

#### 根据条件判断执行不同的sql语句
```php
Db::table('user')->when(false, function($query){...}, function($query){...})->select();
// 根据第一个参数的布尔值，为真的话，执行第一个sql语句，为假的话执行第二个sql语句
```

### 数据库事务处理
```php
// 自动实现事务归滚
public function getter() {
    Db::Transaction(function () {
        Db::table('user')->where('id', 19)->save(['price'=>Db::raw('price + 3')]);
        Db::table('user')->where('id', 20)->save(['price'=>Db::raw('price - 3')]);
    });
}

// 手动实现事务回滚
Db::startTrans();
try {
    Db::table('user')->where('id', 19)->save(['price'=>Db::raw('price + 3')]);
    Db::table('user')->where('id', 20)->save(['price'=>Db::raw('price - 3')]);

    Db::commit();
}catch (Exception $e) {
    echo '执行SQL失败，开始回滚数据'；
    Db::rollback();
}
```

### 获取器
- 获取器的意思就是，将数据的字段进行转换处理再进行操做
```php
$user = Db::table('users')->withAttr('name', function ($value, $data) {
    return strtoupper($value);
})->select();
```

## 模型

### 模型的定义
```php
namespace app\model;
use think\Model;

class Employees extends Model
{
    protected $connection = 'mysql2';

    // 设置当前模型对应的完整数据表名称
    protected $name = 'departments';

    // 设置主键
    protected $pk = 'id'
} 
```


