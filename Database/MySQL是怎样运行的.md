# 初识MySQL
## 在类UNIX中的服务器程序
- mysqld
- mysqld_safe
  - 是一个启动脚本，间接调用mysqld并持续监控服务器运行状态。
  - 服务器出错时，帮忙重启
  - 输出错误日志（默认写到.err文件）
- mysql.server
  - 一个启动脚本，间接调用mysqld_safe
- mysqld.multi
  
总结：mysqld_safe,mysql.server,mysqld.multi本质都是一个shell脚本


## 客户端程序
- mysqladmin
- mysqldump
- mysqlcheck



## 客户端与服务端连接的过程
- TCP/IP
- 命名管道和共享内存（Windows）
- UNIX域套接字


## 服务器处理客户端请求
- 连接管理
  - 处理连接

- 解析与优化
  - 查询缓存
  - 语法解析
  - 查询优化

- 存储引擎


## 关于存储引擎的一些操作
```shell
# 查看当前服务器支持的存储引擎
SHOW ENGINES

# 创建表时指定表的存储引擎
CREATE TABLE 表格 (
    建表语句;
) ENGINE=存储引擎名称;

# 修改表的存储引擎
ALTER TABLE 表名 ENGINE = 存储引擎名称
```

# MySQL的调控按钮——启动选项和系统变量

## 命令行上使用选项
```shell
mysqld  --启动选项1[=值1] --启动选项2[=值2]
```

范例
```shell
mysqld --skip-networking

mysqld --default-storage-engine=MyISAM
```

## 配置文件中使用选项

### 配置文件的路径（类UNIX）

- /etc/my.cnf
- /etc/mysql/my.cnf
- SYSCONFDIR/my.cnf
- $MYSQL_HOME/my.cnf
  - 仅限服务端     
- defaults-extra-file
  - 命令行指定的额外的配置文件路径
- ~/.my.cnf
- ~/.mylogin.cnf
  - 仅限客户端

### 配置文件的内容
```shell
[server]
（具体启动选项）

[mysqld]
（具体启动选项）

[mysqld_safe]
（具体启动选项）

[client]
（具体启动选项）

[mysql]
（具体启动选项）

[mysqladmin]
（具体启动选项）
```

### 程序对应类别和能读的组
- mysqld
  - [mysqld],[server]
- mysqld_safe
  - [mysqld],[mysqld_safe],[server]
- mysql.server
  - [mysqld],[mysql.server],[server]
- mysql
  - [mysql],[client]
- mysqladmin
  - [mysqladmin],[client]
- mysqldump
  - [mysqldump],[client]

总结：mysqld_safe和mysql.server能识别mysqld的原因是基本中都调用了mysqld

### 配置文件优先级
- /etc/my.cnf
- /etc/mysql/my.cnf
- SYSCONFDIR/my.cnf
- $MYSQL_HOME/my.cnf
  - 仅限服务端     
- defaults-extra-file
  - 命令行指定的额外的配置文件路径
- ~/.my.cnf
- ~/.mylogin.cnf
  - 仅限客户端

后面的优先级高


### 同一个配置文件中多个组优先级

按顺序，下面的优先级高

### defaults-file的使用

如果不想让MySQL到默认路径下搜索配置文件，可以在命令行指定defaults-file
```shell
mysqld --defaults-file=/tmp/myconfig.txt
```


## 系统变量
### 查看系统变量
```shell
# 查看系统变量及当前值
SHOW VARIABLES [LIKE 匹配的模式];

# 示例
SHOW VARIABLES LIKE 'default_storage_engine'

SHOW VARIABLES LIKE 'max_connections'

## 支持模糊查询
SHOW VARIABLES LIKE 'default%';
```

### 设置系统变量

#### 通过启动选项设置

- 通过命令行添加启动选项
```shell
mysqld --default-storage-engine=MyISAM --max-connection=10
```

- 通过配置文件添加启动选项
```shell
[server]
default-storage-engine=MyISAM 
max-connection=10
```

- 注意：
  - 如果是启动选项名有多个单词组成，各个单词之间用短划线或者下划线都可以
  - 但是系统变量只能用下划线


#### 系统变量的作用范围

- GLOBAL(全局范围)：
  - 影响服务器的整体操作

- SESSION(会话范围)：
  - 影响某个客户端连接的操作
  
```sql
-- 作用范围GLOBAL
SET GLOBAL default_storage_engine = MyISAM;
SET @@GLOBAL.default_storage_engine = MyISAM;

-- 作用范围SESSION
SET SESSION default_storage_engine = MyISAM;
SET @@SESSION default_storage_engine = MyISAM;
-- 默认作用范围是SESSION
SET default_storage_engine = MyISAM
```


查看不同作用范围的系统变量
```shell
# 默认SESSION
# 如果某个系统变量没有GLOBAL作用范围，则不显示
SHOW [GLOBAL|SESSION] VARIABLES [LIKE 匹配模式];
```

注意事项
- 并不是所有的系统变量都具有GLOBAL和SESSION的作用范围
  - 有一些系统变量只有GLOBAL作用范围，比如max_connections
    - 它表示服务器程序支持同时最多多少个客户端程序进行连接
  - 有一些系统变量只具有SESSION作用范围，比如insert_id
    - 它表示在对某个包含AUTO_INCREMENT列的表记性插入时，该列最初始的值
  - 大部分系统变量是同时具有GLOBAL作用范围和SESSION作用范围，比如default_storage_engine

- 有些系统变量只读，不能设置值
  - 比如version

启动选项和系统变量的区别
- 启动选项
  - 在程序启动时，由用户传递的一些参数


- 系统变量
  - 影响服务器程序运行的变量


#### 状态变量

为了让我们更好地了解服务器程序的运行情况，MySQL服务器程序中维护了好多关于程序运行状态的变量，它们被称为状态变量。

示例：
1. Threads_connected表示当前有多少客户端服务器建立了连接
2. Innodb_rows_updated表示更新了多少条以InnoDB为存储引擎的表中的记录。等等


状态变量的值只能由服务器程序自己设置，状态变量也有GLOBAL和SESSION两个作用范围

查看状态变量
```shell
SHOW [GLOBAL|SESSION] STATUS [LIKE 匹配的模式];

# 示例
SHOW STATUS LIKE 'thread%';
```

# 字符集和比较规则

## MySQL中支持字符集和比较规则

### MySQL中utf8和utf8mb4

- utf8mb3:
  - 阉割过的UTF-8字符集，只使用了1~3字节表示字符

- utf8mb4:
  - 正宗的UTF-8字符集，使用1~4字节表示字符（一些emoji表情使用4字节编码）


### 字符集的查看

查看当前MySQL中支持的字符集
```shell
# CHARACTER和CHARACTER SET等价
SHOW (CHARACTER SET|CHARSET) [LIKE 匹配的模式];
```

常用字符集和Maxlen最大长度
- acsii --------> 1字节
- Latin --------> 1字节
- GB2312--------> 2字节
- GBK ----------> 2字节
- utf8 ---------> 3字节（MySQL中utf8是utf8mb3的别名）
- utf8mb4 ------> 4字节


### 比较规则的查看

比较规则：比较两个字符对应二进制编码的大小
- 将两个大小写不同的字符全部都转为大写或小写
- 再比较这两个字符对应的二进制数据。

```shell
SHOW COLLATION [LIKE 匹配的模式]
```

### 字符集和比较规则的应用

#### 各级别的字符集和比较规则

MySQL有4个级别的字符集和比较规则
- 服务器级别
- 数据库级别
- 表级别
- 列级别



<span style="color:tomato;font-weight:700">服务器级别</span>
- MySQL提供了两个系统变量来表示服务器级别的字符集和比较规则
```shell
character_set_server  # 服务器级别的字符集
collation_server    # 服务器级别的比较规则
```

范例
```shell
mysql> SHOW VARIABLES LIKE 'character_set_server'
    -> ;
+----------------------+---------+
| Variable_name        | Value   |
+----------------------+---------+
| character_set_server | utf8mb4 |
+----------------------+---------+
1 row in set (0.00 sec)

mysql> SHOW VARIABLES LIKE 'collation_server';
+------------------+--------------------+
| Variable_name    | Value              |
+------------------+--------------------+
| collation_server | utf8mb4_0900_ai_ci |
+------------------+--------------------+
1 row in set (0.00 sec)
```

在启动服务器程序时，可以通过启动选项或者在服务器程序运行过程中使用SET语句来修改这两个变量的值
```shell
[server]
character_set_server=gb2312
collation_server=gb2312_chinese_ci

# 在服务器运行过程中使用SET语句修改
SET collation_server=utf8_general_ci;
```


<span style="color:tomato;font-weight:700">数据库级别</span>

在创建和修改数据库时可以指定该数据库的字符集和比较规则
```shell
# DEFAULT可是省略
CREATE DATABASE 数据库名
    [[DEFAULT] CHARACTER SET 字符集名称]
    [[DEFAULT] COLLATE 比较规则名称];

ALTER DATABASE 数据库名
    [[DEFAULT] CHARACTER SET 字符集名称]
    [[DEFAULT] COLLATE 比较规则名称];
```

查看数据库级别的字符集和比较规则
```shell
# 要先使用use进入指定数据库，然后执行命令
SHOW VARIABLES LIKE 'character_set_database'

SHOW VARIABLES LIKE 'collation_database'
```

注意:
- 修改字符集和比较规则应使用上述的命令，而不是直接修改`characgter_set_database`和`collation_database`这两个变量的值，这两个变量只是用来告诉用户当前数据库的字符集和比较规则是什么


```shell
# 默认使用服务器级别的字符集和比较规则作为数据库的字符集和比较规则
CREATE DATABASE 数据库名
```

<span style="color:tomato;font-weight:700">表级别</span>

在创建和修改表的时候指定标的字符集和比较规则
```shell
CREATE TABLE 表名 (列的信息)
    [[DEFAULT] CHARACTER SET 字符集名称]
    [[DEFAULT] COLLATE 比较规则名称];

ALTER TABLE 表名
    [[DEFAULT] CHARACTER SET 字符集名称]
    [[DEFAULT] COLLATE 比较规则名称];
```

<span style="color:tomato;font-weight:700">列级别</span>


在创建和修改列的时候可以指定该列的字符集和比较规则
```shell
CREATE TABLE 表名 (
    列名 字符串类型 [CHARACTER SET 字符集名称] [COLLATE 比较规则名称]
    其他列...
);

ALTER TABLE 表名 MODIFY 列名 字符串类型 [CHARACTER SET 字符集名称] [COLLATE 比较规则名称];
```

注意：由于字符集和比较规则之间相互关联，因此仅修改字符集或仅修改比较规则，对应的比较规则或字符集也会随之更改。

## 客户端和服务端通信过程中使用的字符集

### 字符集转换的概念

- 如果接受0xE68891这个字节序列的程序按照UTF-8字符集进行解码
- 然后又把它按照GBK字符集进行编码，则编码后的字节序列就是0xCED2。
- 我们把这个过程称为字符集的转换。
- 也就是字符串'我'从UTF-8字符集转换为GBK字符集

### MySQL中的字符集转换过程

如果把MySQL当做一个软件

那么从用户的角度来看，客户端发送的请求以及服务器返回的响应都是一个字符串

从机器的角度来看，客户端发送请求和服务器返回的响应本质上就是一个字节序列。在这个“客户端发送请求，服务端返回响应”的过程中，其实经历了多次字符集转换，详细过程如下

- 客户端发送请求
  - 我们把从MySQL客户端与服务器进行通信的过程中事先规定好的数据格式（即指明请求和响应的每一个字节分别代表什么意思）称为MySQL通信协议。
  - 该协议可以通过Wireshark等抓包软件来分析这个协议。
  - 理论上在了解了MySQL通讯协议之后，我们甚至可以动手制作自己的客户端软件
  - -------------------------------------
  - 一般情况下，客户端编码请求字符串时使用的字符集与操作系统当前使用的字符集一致
  - 当使用类UNIX操作系统时
    - LC_ALL
    - LC_CTYPE
    - LANG
    - 这三个环境变量决定了操作系统当前使用的是哪种字符集。这三个变量的优先级如下
    ```shell
    LC_ALL > LC_CTYPE > LANG
    
    # 如果这3个环境变量都没有设置，那么操作系统当前使用的字符集就是默认的字符集
    ```
  - Windows系统中，字符集叫代码页，可以在命令行中执行chcp进行查看
  ```shell
  chcp
  ```
    - Windows的客户端可以通过如下命令启动客户端来指定客户端字符集
    ```shell
    mysql --default-character-set=utf8  
    ```


- 服务器接受请求
  - 从本质上来说，服务器接受到的请求就是一个字节序列。
  - 服务器将这个字节序列看作是使用系统变量<span style="color:red">character_set_client</span>代表的字符集进行编码的字符序列（每个客户端与服务器建立连接后，服务器都会为该客户端维护一个单独的character_set_client变量，这个变量是SESSION级别的）
  - 综上所述，可以清楚的意识到一个事情：
    - <span style="color:tomato">客户端在编码请求字符串时实际使用的字符集，与服务器收到一个字节序列后认为该字节序列所采用的编码字符集，是两个独立的字符集</span>


- 服务器处理请求
  - 服务器解码客户端发过来的字节序列是根据`character_set_client`的字符集来解码
  - 但是服务端内部处理的时候，是根据SESSION级别的`character_set_connection`来处理的
  - 也就是说，解码后，服务端会对这个字节序列进行二次编码，按照`character_set_connection`的字符集
  
- 服务器生成响应
  - 服务端发给客户端的字节序列，是根据`character_set_results`的值，将其表中编码的字节系列中转换为character_set_results额字符集对应的字节序列，然后发给客户端

总结：
- character_set_client
  - 服务器认为请求是按照该系统变量指定的字符集进行编码的,因此也会按照该字符集进行解码
- character_set_connection
  - 服务器在处理请求时，会把请求字节序列从`character_set_client`转换为`character_set_connection`
- character_set_results
  - 服务器采用该系统变量指定的字符集对返回给客户端的字符串进行编码

这3个系统变量在服务器中的作用范围都是SESSION级别。每个客户端在与服务器连接后，服务器都会为这个链接维护这3个变量 

在连接服务器时，客户端会将默认字符集信息，与用户名、密码等信息一起发给服务器，服务器在收到后会将上述3个变量初始化为客户端的默认字符集

在客户端成功连接到服务器之后，可以使用SET语句分别修改`character_set_client`，`character_set_connection`，`character_set_results`系统变量的值

也可以一次性修改这几个变量
```shell
SET NAMES charset_name;
```

- 客户端接受响应
  - 一般使用客户端默认字符集
  - 过程
    - 比如：操作系统当前使用的字符集的UTF8,我们在启动MySQL客户端时使用了`--default_character-set=gbk`
    - 那么客户端默认字符集被设置为gbk，服务器的character_set_results也会被初始化为gbk
    - 因此服务器响应客户端使用的字符编码就是gbk
    - 对于类UNIX操作系统来说，会把接收到的字节序列直接写到根据操作系统默认字符集(UTF8)写到终端
    - 因此就会出现乱码

总结：上述一共5个过程
- 客户端发送的字节序列，使用哪种字符集编码
  - 操作系统默认字符集
- 服务端接收到请求字节序列后，采用那种字符集进行解码
  - character_set_client
- 服务器在运行过程中，把请求来的字节序列，按照哪种字符集重新编码
  - character_set_connection
- 服务器向客户端返回字节序列，采用哪种字符集编码
  - character_set_results
- 客户端收到响应字节序列后，输出到终点，使用哪种字符集
  - - 操作系统默认字符集                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

