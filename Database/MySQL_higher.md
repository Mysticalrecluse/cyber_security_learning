# 数据库概述
## 使用数据库的原因
- 保证数据的持久化
- 对于海量数据，数据库处理的效率更高，而且有多种方法可以针对性进行优化

## 数据库与数据库管理系统
- DB：数据库（Database）
<br>即存储数据的“仓库”，其本质是一个文件系统。它保存了一系列有组织的数据。
- DBMS：数据库管理系统（Database Management System）
<br>是一种操纵和管理数据库的大型软件，用于建立，使用和维护数据库，对数据库进行统一管理和控制。用户通过数据库管理系统访问数据库中表内的数据。
- SQL：结构化查询语言（Structured Query Language）
<br>专门用来与数据库通信的语言

## 关系型数据库（RDBMS）
- 实质
  - 这种类型的数据是最古老的数据库类型，关系型数据库模型是把复杂的数据结构归结为简单的二元关系（即二维表格形式）
  - 关系型数据库以行(row)和(column)的形式存储数据，以便于用户理解。这一系列的行和列被称为表(table)，一组表组成了一个库(database)。
  - 表与表之间的数据记录有关系(relationship)。现实世界中的各种实体以及实体之间的各种联系均用关系模型来表示。关系型数据库，就是建立在关系模型基础上的数据库
  
- 优势
  - 复杂查询
  <br>可以用SQL语句方便的在一个表以及多个表之间做非常复杂的数据查询
  - 事务支持
  <br>使得对于安全性能很高的数据访问要求得以实现。

- 关系型数据库设计规则
  - 关系型数据库的典型数据结构就是数据表，这些数据表的组成都是结构化的（Structured）
  - 将数据放到表中，表再放到库中
  - 一个数据库中可以有多个表，每个表都有一个名字，用来标识自己。表名具有唯一性。
  - 表具有一些特性，这些特性定义了数据在表中如何存储，类似java和python中类的设计。

- 表 、记录、字段
  - E-R(entity-relationship,实体-联系)模型中有三个主要概念：实体集、属性、联系集
  - 一个实体集(class)对应于数据库中的一个表(table)，一个实体(instance)则对应于数据表中的一行(row)，也称为一条记录(record)。一个属性(attribute)对应于数据库表中的一列，也成为字段(field)

- 表的关联关系
  - 表与表之间的数据记录有关系(relationship)。现实世界中的各种实体以及实体之间的各种联系均用关系模型来表示。
  - 四种：一对一关联、一对多关联、多对多关联、自我引用

- 一对一关联 (one-to-one)
  - 在实际开发中应用不多，因为一对一可以创建成一张表
  - 两种建表原则：
    - 外键唯一：主表的主键和从表的外键（唯一），形成主外键关系，外键唯一。
    - 外键是主键：主表的主键和从表的主键，形成主外键关系。

- 一对多关系 (one-to-many)
  - 常见实例场景：客户表和订单表，分类表和商品表，部门表和员工表。
  - 一对多建表原则：在从表(多方)创建一个字段，字段作为外键指向主表(一方)的主键

- 多对多关系（many-to-many）
  - 要表示多对多的关系，必须创建第三个表，该表通常称为连接表，它将多对多关系划分位两个一对多关系。将这两个表的主键都插入到第三个表中。

- 自我引用
  - 暂略


## 非关系型数据库
- 介绍
<br>非关系型数据库，可以看成传统关系型数据库的功能阉割版，基于键值对存储数据，不需要经过SQL层的解析，性能非常高。同时，通过减少不常用的功能，进一步提高性能。

- 非关系型数据库的种类
  - 键值型数据库
  - 文档型数据库
  - 搜索引擎
  - 列存储（必学HBase）
  - 图形数据库

# MySQL
## MySQL环境搭建
### MySQL的卸载（Windows端）
- 查看宿主机是否安装MySQL
  - cmd -> 进入命令行
  - mysql --version 观察命令行响应即可
  - 也可以查看环境变量中，是否有SQL路径
  - 此电脑(我的电脑) -> 管理 -> 查看服务，是否有mysql运行

- 卸载步骤
  - 停止MySQL服务：按“Ctrl + Alt + Delete”组合键，打开“任务管理器”对话框，找到MySQL服务，停止服务
  - 卸载软件
    - 通过控制面板，在控制面板找到应用双击卸载
    - 通过安装包提供的卸载功能卸载

  - 删除数据文件（在存放数据文件的对应文件夹）
  - 删除MySQL环境变量

### MySQL的下载、安装、配置
- MySQL的4大版本
  - MySQL Community Server 社区版本
  <br>开源免费，自由下载，但不提供官方技术支持，适用于大多数普通用户
  - MySQL Enterprise Edition 企业版本
  <br>需付费，不能在线下载，可以试用30天。提供了更多功能和更完备的技术支持，更适合于对数据库的功能和可靠性要求较高的企业客户。
  - MySQL Cluster 集群版
  <br>开源免费。用于架设集群服务器，可将几个MySQL Server封装成一个Server。需要在社区版或企业版的基础上使用。
  - MySQL Cluster CGE 高级集群版
  <br>需付费

- 下载
<br>下载地址：www.mysql.com

- 启动
  - 在计算机管理中，右键选择mysql服务启动
  - 使用命令行工具
  ```shell
  # Windows
  # 启动 MySQL 服务命令：
  net start MySQL服务名

  # 停止 MySQL 服务命令：
  net stop MySQL服务名

  # Linux
  # 查看服务状态
  service mysql status

  # 启动服务
  service mysql start

  # 停止服务
  service mysql stop

  # 重启服务
  service mysql restart
  ```

- 登录
```shell
# Windows 和 Linux 相同
mysql -u <用户名> -p

# 完整版
mysql -u <用户名> -P <端口号> -p

# 远程访问其他主机
mysql -u <用户名> -P <端口号> -h <ip地址> -p

```
- 查看版本
```sql
SELECT version(); 
```

### MySQL图形化管理工具
- 建议下载：
  - SQLyog
  - DBeaver（大数据）

## 基本的SELECT语句
### SQL概述
- SQL背景知识（略）
- SQL分类
  - <font color=royalblue>DDL(Data Definition Languages、数据定义语言)</font>
  <br>这些语句定义了不同的数据库、表、视图、索引等数据库对象，还可以用来创建、删除、修改数据库和数据表的结构。
  <br>主要的语句关键字包括<font color=tomato>CREATE、DROP、ALTER</font>等

  - <font color=royalblue>DML(Data Manipulation Language、数据操作语言)</font>
  <br>用于添加、删除、更新和查询数据库记录，并检查数据完整性。
  <br>主要的语句关键字包括 <font color=tomato>INSERT、DELETE、UPDATE、SELECT</font>等。
  <br><font color=tomato>SELECT是SQL语言的基础，最为重要。</font>

  - <font color=royalblue>DCL(Data Control Language、数据控制语言)</font>
  <br>用于定义数据库、表、字段、用户的访问权限和安全级别。
  <br>主要的语句关键字包括<font color=tomato>GRANT、REVOKE、COMMIT、ROLLBACK、SAVEPOINT</font>等。

### SQL语言的规则与规范
- 基本规则
  - SQL可以写在一行或者多行。为了提高可读性，各子句分行写，必要时使用缩进
  - 每条命令以；或\g或\G结束
  - 关键字不能被缩写也不能分行
  - 关于标点符号
    - 必须保证所有的(),单引号,双引号是成对出现
    - 必须使用英文状态下的半角输入方式
    - 字符串型和日期时间类型的数据可以使用单引号('')表示
    - 列的别名，尽量使用双引号("")，不建议省略as

- SQL大小写规范(建议遵守)
  - MySQL在Windows环境下是大小写不敏感的
  - MySQL在Linux环境下是大小写敏感的
    - 数据库名、表名、表的别名、变量名是严格区分大小写的
    - 关键字、函数名、列名(或字段名)、列的别名(字段别名)是忽略大小写的
  - <font color=tomato>推荐采用统一的书写规范</font>
    - 数据库名，表名，表别名，字段名，字段别名等都小写
    - SQL关键字、函数名、绑定变量等都大写

- 注释
```SQL
单行注释：# 注释文字，单行注释(MySQL特有的方式)
单行注释：-- 注释文字 （--后面必须包含一个空格）
多行注释：/* */
```
- 导入现有的数据表
  - 方式1：source 文件全路径名
  - 方式2：基于具体的图形化界面的工具可以导入数据
  <br>比如：SQLyog中，选择“工具”->"执行sql脚本"，选中xxx.sql即可。

### 最基本的SELECT语句
```SQL
/* SELECT 字段1,字段2,... FROM 表名 */

SELECT 1 + 1, 3 * 2 FROM DUAL; -- dual:伪表
SELECT * FROM employee; -- *表示全部数据


/* 列的别名 (3种方式) */

SELECT employee_id emp_id, last_name AS lname, department_id "部门id" fROM employees;
-- 别名：用空格隔开 
-- 用AS连接
-- 列的别名可以用双引号“”引起来


/* 去除重复行 */

SELECT DISTINCT department_id FROM employees;
-- DISTINCT 可以去除重复数据


/* 空值参与运算 */

-- 所有运算符或列值遇到null值，运算结果都为null 
-- null 不等同于 0
SELECT employee_id, salary "月工资", 
salary * (1 + commission_pct) * 12 "年工资", commission_pct
FROM employees; -- comission_pct的值为null
-- 则年工资的计算结果为null
-- 解决方案（如果想将null看作0去计算）：引入IFNULL
SELECT employee_id, salary "月工资", 
salary * (1 + IFNULL(commission_pct,0)) * 12 "年工资", commission_pct
FROM employees;


/* 着重号 `` 即反引号*/

SELECT * FROM `order`;
-- 当字段或表名与关键字发生冲突的时候，可以使用反斜杠包裹，防止报错


/* 查询常数 */

SELECT '常数'， employee_id, last_name FROM employees;
-- 常数会和表格的字段的每个记录都进行匹配


/* 显示表结构 */

DESCRIBE employees;
DESC employees;
-- 显示了表中字段的详细信息


/* 过滤数据 WHERE */

-- 查询90号部分的员工信息
SELECT * FROM employees WHERE department_id = 90；
-- 查询last_name为'King'的员工信息
SELECT * FROM employees WHERE last_name = 'King'; 
-- WHERE声明在FROM结构的后面
```

### 运算符
- 算数运算符
  - 加：+ (加号在SQL中，没有拼接作用，只表示 加法运算)
  - 减：-
  - 乘：*
  - 除：/ 或 DIV
  - 取余：% 或 MOD
  ```sql
  SELECT 100, 100 + 0, 100 - 0, 100 + 50 - 30, 100 + 35.5, 100 - 35.5
  FROM DUAL;

  -- DUAL 伪表

  SELECT 100 + '1'
  FROM DUAL;
  -- 在SQL中，+没有连接作用，只表示加法运算。此时，会将字符串转换为数值(隐式转换)

  SELECT 100 + 'a'
  FROM DUAL;
  -- 此时将'a'看作0处理

  SELECT 100 + NULL
  FROM DUAL；
  -- null值参与运算，结果为null

  SELECT employee_id, last_name, salary
  FROM employees
  WHERE employee_id % 2 = 0;
  -- 查询员工id为偶数的员工信息
  -- 这里比较运算符用一个等于号
  ```

- 比较运算符
  - 符号： =； <=>; <> !=; <; <=; >; >=
  ```sql
  SELECT 1 = NULL, NULL = NULL
  FROM DUAL;
  -- 只要有null参与判断，结果就为null

  SELECT last_name, salary, commission_pct
  FROM employees
  WHERE commission_pct = NULL;
  -- 此时执行，不会有任何结果
  -- 原理：将WHERE后面的式子，逐行匹配，只保留返回结果为1的值，因为NULl和任何数，包括自己的返回值都为NULL，所以无法筛选任何信息。

  -- 安全等于 <=>   记忆技巧：为NULL而生。
  -- 安全等于可以判断包含null的公式
  -- 如果 NULL <=> NULL,返回值为1，和其他比返回值为0
  SELECT 1 <=> NULL, NULL <=> NULL
  FROM DUAL;
  ```

  - 关键字：
  ```sql
  IS NULL           为空运算符
  IS NOTNULL        不为空运算符
  LEAST             最小值运算符（函数）
  GREATEST          最大值运算符（函数）
  BETWEEN AND       两值之间运算符
  ISNULL            为空运算符（函数）
  IN                属于运算符
  NOT IN            不属于运算符
  LIKE              模糊匹配运算符
  REGEXP            正则表达式运算符
  RLIKE             正则表达式运算符

  -- ISNULL函数的使用
  SELECT last_name, salary, commission_pct
  FROM employees
  WHERE ISNULL(commission_pct);
  -- 等同于
  SELECT last_name, salary, commission_pct
  FROM employees
  WHERE commission_pct IS NULL;

  -- LEAST() / GREATEST()
  SELECT LEAST('g','b','t','m'),GREATEST('g','b','t','m')
  FROM DUAL;

  -- BETWEEN...AND
  -- 查询工资在6000到8000的员工信息
  SELECT employee_id,last_name,salary
  FROM employees
  WHERE salary BETWEEN 6000 AND 8000;
  -- 包含边际数值

  -- IN(set) / NOT IN(set)
  -- 查询部门为10，20，30部门的员工信息
  SELECT last_name,salary,department_id
  FROM employees
  WHERE department_id IN (10,20,30);

  -- LIKE 模糊查询
  -- 查询last_name中包含字符'a'的员工信息
  SELECT last_name
  FROM employees
  WHERE last_name LIKE '%a%';
  -- % ，代表零个、一个或多个字符
  -- '_'，代表一个单一的字符

  -- 正则表达式 REGEXP/RLIKE
  SELECT last_name
  FROM employees
  WHERE REGEXP '正则表达式';
  
  ```

- 逻辑运算符
  ```sql
  NOT 或 ！
  AND 或 &&
  OR 或 ||
  XOR 逻辑异或 异或两侧，不一样则为真
  ```
- 位运算符
  ```sql
  &     按位与
  |     按位或
  ^     按位异或
  ~     按位取反
  >>    按位右移
  <<    按位左移
  ```