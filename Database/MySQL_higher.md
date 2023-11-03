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

```sql
DDL: 数据定义语言
CREATE \ ALTER \ DROP \ RENAME \ TRUNCATE

DML: 数据操作语言
INSERT \ DELETE \ UPDATE \ SELECT (重中之重)

DCL: 数据控制语言
COMMIT \ ROLLBACK \ SAVEPOINT \ GRANT \ REVOKE +
```

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
  IS NOT NULL        不为空运算符
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
### 排序与分页
- 排序数据
  - 排序规则
  ```sql
  # 使用ORDER BY对查询到的数据进行排序

  SELECT employee_id,last_name,salary FROM employees ORDER BY salary;
  -- 升序：ASC 默认
  -- 降序：DESC

  # 我们可以使用列的别名，进行排序

  SELECT employee_id,salary,salary*12 as annual_sal FROM employees ORDER BY annual_sal;

  # 列的别名只能在ORDER BY中使用，不能在WHERE中使用
  SELECT employee_id salary,salary*12 as annual_sal FROM employees WHERE annual_sal > 81600;
  -- 会报错

  -- 数据表的查询顺序：
  -- 先执行FROM table_name;
  -- 再执行 where 条件；
  -- 然后执行，select后要查找的字段（包含别名）
  -- 最后看order by排序
  -- 也因此，where不能使用别名，但是order by可以，因为再执行where的时候，还没有执行到字段的别名。

  # 二级排序
  示例：显示员工信息，按照department_id的降序排列，department_id相同的情况下，按照salary的升序排列

  SELECT employee_id,salary,department_id FROM employees ORDER BY department_id DESC,salary ASC;
  -- 多个排序嵌套查询，各级之间用逗号排序

  ```

- 分页
  - 规则实现
  ```sql
  # 使用LIMIT实现数据的分页显示

  # 需求1：每页显示20条记录，此时显示第1页
  SELECT employee_id, last_name FROM employees LIMIT 0，20；

  # 需求2：每页显示20条记录，此时显示第2页
  SELECT employee_id, last_name FROM employees LIMIT 20，20；
  
  -- 格式：LIMIT 位置偏移量, 条目数量;

  # WHERE ... ORDER BY ... LIMIT 声明顺序如下；
  SELECT employee_id, last_name, salary FROM employees
  WHERE salary > 6000
  ORDER BY salary DESC
  LIMIT 0,10;

  # MySQL8.0新特性：LIMIT ... OFFSET ...
  -- 与老版本相反，LIMIT 条目数量 OFFSET 位置偏移量
  SELECT employee_id, last_name, salary FROM employees
  WHERE salary > 6000
  ORDER BY salary DESC
  LIMIT 10 OFFSET 0;
  ```
  - 注意：LIMIT必须放在整个SELECT语句的最后！


### 多表查询 
- 定义：也称为关联查询，指两个或更多个表一起完成查询操作
- 前提条件：这些一起查询的表之间是有关系的（一对一、一对多），它们之间一定是关联字段，这个关联字段可能建立了外键，也可能没有建立外键。比如：员工表和部门表，这两个表依靠“部门编号”进行关联

- 多表查询的实现
```SQL
笛卡尔积错误

-- 错误的实现方式：每个员工与每个部门都匹配了一遍
SELECT employee_id,department_name
FROM employees,departments;
-- 错误的原因：缺少了多表的链接条件

-- 等同于笛卡尔积错误的交叉的查询
SELECT employee_id,department_name
From employees CROSS JOIN departments;

-- 多表查询的正确方式：需要有连接条件(关联查询)
SELECT employee_id,department_name
From employees,departments
-- 两个表的连接条件
WHERE employees.department_id = departments.department_id;

-- 如果查询语句中出现了多个表中都存在的字段，则必须指明此字段所在的表
SELECT employee_id,department_name,employees.department_id
FROM employees,departments
WHERE employees.department_id = departments.department_id;
-- 建议：从sql优化的角度，建议多表查询时，每个字段都指名其所在的表
SELECT employees.employee_id,departments.department_name,employees.department_id
FROM employees,departments
WHERE employees.department_id = departments.department_id;
-- 可读性太差，表明过长的话，所以可以给表起别名，在SELECT和WHERE中使用表的别名
SELECT emp.employee_id,dept.department_name,emp.department_id
FROM employees emp,departments dept
WHERE emp.department_id = dept.department_id;
-- 起别名的方法和给字段起别名一样，都是空格直接加别名
-- 如果给表起来别名，一但在SELECT或WHERE中使用表明的话，则必须使用表的别名，不能再使用原名

-- 三表(多表)查询
SELECT e.employee_id,e.last_name,d.department_name,l.city
FROM employees e,departments d,locations l
WHERE e.department_id = d.department_id
AND d.location_id = l.location_id;
-- 如果有n个表实现多表的查询，则需要至少n-1个连接条件

/*
演绎式：提出问题1 --> 解决问题1 --> 提出问题2 --> 解决问题2 ...
归纳式：总 -- 分 -- 总
*/

-- 多表查询的分类
-- 角度1：等值连接 vs 非等值连接

-- 角度2：自连接 vs 非自连接

-- 角度3：内连接 vs 外连接 

等值连接 vs 非等值连接

-- 非等值连接的例子

SELECT e.last_name,e.salary,j.grade_level
FROM employees e,job_grades j
WHERE e.salary between j.lowest_sal and j.highest_sal;

-- 自连接

SELECT emp.last_name employee,mgr.last_name manager
FROM employees emp,employees mgr
WHERE emp.manager_id = mgr.employee_id;

内连接 vs 外连接

内连接定义：；只把满足查询条件的数据列出来，而未满足查询条件的没有列出来，就叫内连接

外连接定义：处理包含多表匹配行之外，还查询到了多个表中不匹配的行，这种查询情况叫外连接

外连接分类：
左外连接
两个表在连接过程中除了返回满足连接条件的行以外，还返回左表中不满足条件的行
右外连接
两个表在连接过程中除了返回满足连接条件的行以外，还返回右表中不满足条件的行
满外连接 

SQL92中的内连接：见上，略

SQL92中的外连接：使用 +  

SELECT employee_id,department_name
From employees e,departments d
WHERE e.department_id = d.department_id(+);
-- MySQL不支持SQL92语法中的外连接写法，支持oracle

SQL99中的外连接：使用JOIN...ON的方式实现多表查询，MySQL支持SQL99这种方式

SQL99中的内连接：

SELECT last_name,department_name
FROM employees e (INNER) JOIN departments d
on e.department_id = d.department_id
-- 两个表内连接查询

SELECT last_name,department_name,city
FROM employees e JOIN departments d
on e.department_id = d.department_id
JOIN location l
ON d.location_id = l.location_id;
-- 三表（多表）内连接查询

SQL99中的外连接

-- 左外连接
SELECT last_name,department_name
FROM employees e LEFT (OUTER) JOIN departments d
ON e.department_id = d.department_id;

-- 右外连接
SELECT last_name,department_name
FROM employees e RIGHT (OUTER) JOIN departments d
ON e.department_id = d.department_id;

-- 满外连接
SELECT last_name,department_name
FROM employees e FULL (OUTER) JOIN departments d
ON e.department_id = d.department_id;
-- 不支持mysql,支持oracle

UNION的使用

合并查询结果
利用UNION关键字，可以给出多条SELECT语句，并将它们的结果组合成单个结果集。<font color=tomato>合并时，两个表对应的列数和数据类型必须相同，并且相互对应。</font>各个SELECT语句之间使用UNION 或UNION ALL关键字分割  

SELECT column, ... FROM table1
UNION [ALL]
SELECT column, ... FROM table2

UNION操作符
返回两个查询的结果集的并集，去除重复记录

UNION操作符
返回两个查询的结果集的并集。对于两个结果集的重复部分不去重。


```
![Alt text](image.png)

```sql
七种JOIN的实现

中图：内连接
SELECT employee_id, department_name
FROM employees e Join Departments d
ON e.department_id = d.department_id;

左上图：左外连接
SELECT employee_id,department_name
FROM  employees e LEFT JOIN departments d
ON e.department_id = d.department_id;

右上图：右外连接
SELECT employee_id,department_name
FROM  employees e RIGHT JOIN departments d
ON e.department_id = d.department_id;

左中图：
SELECT employee_id,department_name
FROM  employees e LEFT JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_id IS NULL;

右中图：
SELECT employee_id,department_name
FROM  employees e RIGHT JOIN departments d
ON e.department_id = d.department_id
WHERE e.department_id IS NULL;

左下图（满外连接）
方式一：左上图 UNION ALL 右中图
SELECT employee_id,department_name
FROM  employees e LEFT JOIN departments d
ON e.department_id = d.department_id
UNION ALL
SELECT employee_id,department_name
FROM  employees e RIGHT JOIN departments d
ON e.department_id = d.department_id
WHERE e.department_id IS NULL;

方式2：左中图 UNION ALL 右上图
详情：略

右下图：左中图 UNION ALL 右中图
详情：略
```

- 多表查询扩展：SQL99语法新特性
```sql
自然连接：NATURAL JOIN
SQL92：
SELECT employee_id,last_name,department_name
FROM employees e JOIN departments d
ON e.department_id = d.department_id
AND e.manager_id = d.manager_id;

-- NATURAL JOIN : 它会帮你自动查询两张连接表中所有相同字段，然后进行等值连接
SQL99语法新特性1:NATURAL JOIN
SELECT employee_id,last_name,department_name
FROM employees e NATURAL JOIN departments d;

SQL99语法新特性1:USING
-- 当匹配字段名称相同的时候使用
SELECT employee_id,last_name,department_name
FROM employees e JOIN departments d
USING (department_id);
```

### 单行函数
- 特点：
  - 操作数据对象
  - 接收参数返回一个结果
  - 只对一行进行变换
  - 每行返回一个结果
  - 可以嵌套
  - 参数可以是一列或一个值

#### 数值函数
- 基本函数
  - ABS(x) 返回x的绝对值
  - SIGN(x) 返回x的符号，正数返回1，负数返回-1，0返回0
  - PI() 返回圆周率的值
  - CEIL(x),CEILNG(x) 返回大于或等于某个值的最小整数
  - FLOOR(x) 返回小于或等于某个值的最大整数
  - LEAST(e1,e2,e3) 返回列表中的最小值
  - GREATEST(e1,e2,e3) 返回列表中的最大值
  - MOD(x,y) 返回x除以y的余数
  - RAND() 返回0~1的随机数
  - RAND(x) 返回一个随机数，x作为种子或因子，当x的值相同时，随机数产生的值必然相同
  - ROUND(x) 返回一个对x进行四舍五入后的整数
  - ROUND(x,y) 返回一个对x进行四舍五入，后保留到小数点后y位的数（y的值可正可负，负值表示向前移位进行判断，比如ROUND(123,-1) 结果为120）
  - TRUNCATE(x,y) 返回数字x截断为y位小数的结果
  - SQRT(x) 返回x的平方根，当x的值为负数时，返回NULL

- 角度与弧度的互换
  - RADIANS(x) 将角度转化为弧度，其中参数x为角度值
  - DEGREES(x) 将弧度转化为角度，其中参数x为弧度值

- 三角函数
  - SIN(x)
  - ASIN(x) 相当于SIN(x)的反函数，返回值为弧度值，建议使用DEGREES转换为角度值，方便阅读
  - COS(x)
  - ACOS(x)
  - TAN(x)
  - ATAN(x)
  - COT(x)

- 指数和对数
  - POW(x,y) 返回x**y的值
  - POWER(x,y) 同POW(x,y)
  - EXP(x) 返回一个以e为底，x为n次幂的值，e为2.71828
  - LN(x) 返回一个以e为底，求x的对数
  - LOGN(x) 返回一个以N为底，求x的对数，比如LOG10(10) 结果为1

- 进制间转换
  - BIN(x) 返回x的二进制编码
  - HEX(x) 返回x的十六进制编码
  - OCT(x) 返回x的八进制编码
  - CONV(x,f1,f2) 返回f1进制的数x，转换为f2进制的数，比如CONV(10,2,8) 结果为2，因为：2进制数10，在8进制中，结果是2

#### 字符串函数
- ASCII(S) 返回字符串S中的第一个字符的ASCII码值
- CHAR_LENGTH(s) 返回字符串s的字符数。作用与CHARARTER_LENGTH(s)相同
- LENGTH(s) 返回字符串s的字节数，和字符集有关
- CONCAT(s1,s2,…,sn) 连接s1,s2……,sn为一个字符串
- CONCAT_WS(x,s1,s2,…,sn) 同CONCAT()函数，但是每个字符串之间要加上x
- INSERT(str,idx,len,replacestr) 将字符串str从第idx位置开始，len个字符长的子串替换为字符串replacestr
  - <font color=tomato> SQL中字符串的索引idx是从1开始的</font>
- REPLACE(str,a,b)  用字符串b替换字符串str中所有出现的字符串a
- UPPER(s)或UCASE(s) 将字符串s的所有字母转化为大写字母
- LOWER(s)或LCASE(s) 将字符串s的所有字母转换成小写字母
- LEFT(str,n)  返回字符串str最左边的n个字符
- RIGHT(str,n)  返回字符串str最右边的n个字符
- LPAD(str,len,pad) 用pad的字符并将字符串str补全到len的长度，左补
- RPAD(str,len,pad) 用pad的字符并将字符串str补全到len的长度，右补
- LTRIM(s) 去掉字符串s左侧的空格
- RTRIM(s) 去掉字符串s右侧的空格
- TRIM(s) 去掉字符串s两侧的空格
- TRIM(s1 FROM s) 去掉字符串s开始与结尾的s1
- TRIM(LEADING s1 FROM s) 去掉字符串开始处的s1
- TRIM(TRAILING s1 FROM s) 去掉字符串结尾处的s1
- REPEAT(str,n) 返回str重复n次的结果
- SPACE(n) 返回n个空格
- STRCMP(s1,s2) 比较字符串s1,s2的ASCII码值的大小
  - 返回值1，表示前面的值大，-1表示后面的值大，0表示一样大
- SUBSTR(s,index,len) 返回从字符串s的index位置其len个字符
- LOCATE(substr,str) 返回字符串substr在字符串str中首次出现的位置
  - 未找到，则返回0
  - 等同于position(substr,str)和INSTR(substr,str)
- ELT(m,s1,s2,...,sn) 返回指定位置的字符串，如果m=1，则返回s1，如果m=2,则返回s2，以此类推
- FIELD(s,s1,s2,...,sn) 返回字符串s在字符串列表第一次出现的位置
- FIND_IN_SET(s1,s2) 返回字符串s1在字符串s2中出现的位置。其中，字符串s2是一个以逗号分隔的字符串
- REVERSE(s) 返回反转后的字符串
- NULLIF(value1,value2) 比较两个字符串，如果value1与value2相同，则返回NULL，否则返回value1

#### 日期和时间函数
- 获取日期、时间
  - CURDATE(),CURRENT_DATE()
    - 返回当前日期，只包含年、月、日
  - CURTIME(),CURRENT_TIME()
    - 返回当前时间，只包含时、分、秒
  - NOW()/SYSDATE()/CURRENT_TIMESTAMP()/LOCALTIME()/LOCALTIMESTAMP() 
    - 返回当前系统时间和日期
  - UTC_DATE() 返回UTC(时间标准时间)日期
  - UTC_TIME() 返回UTC(时间标准时间)时间

- 日期与时间戳的转换
  - UNIX_TIMESTAMP()
    - 以UNIX时间戳的形式返回当前时间
  - UNIX_TIMESTAMP(date)
    - 将时间date以UNIX时间戳的形式返回
  - FROM_UNIXTIME(timestamp) 
    - 将UNIX时间戳的时间转换为普通格式的时间

- 获取月份、星期、星期数、天数等函数   
  - YEAR(date)/MONTH(date)/DAY(date)
    - 返回具体的日期值
  - HOUR(time)/MINUTE(time)/SECOND(time)
    - 返回具体的时间值
  - MONTHNAME(date)
    - 返回月份：january...
  - DAYNAME(date)
    - 返回星期几：MONDAY，TUESDAY...
  - WEEKDAY(date)
    - 返回周几，注意，周一是0，周二是1...
  - QUARTER(date)
    - 返回日期对应的季节，范围为1~4
  - WEEK(date),WEEKOFYEAR(date)
    - 返回一年中的第几周
  - DAYOFYEAR(date)
    - 返回日期是一年中的第几天
  - DAYOFMONTH(date)
    - 返回日期位于所在月份的第几天
  - DAYOFWEEK(date)
    - 返回周几，注意：周日是1，周一是2...周六是7

- 日期的操作函数
  - EXTRACT(type FROM date)
    - 返回指定日期中特定的部分，type指定返回的值
    - type取值
      - MICROSECOND 返回毫秒数
      - SECOND 返回秒数
      - MINUTE 返回分钟数
      - HOUR 返回小时数
      - DAY 返回天数
      - WEEK 返回日期在一年中的第几个星期
      - MONTH 返回日期在一年中的第几个月
      - QUARTER 返回日期在一年中的第几个季度
      - YEAR 返回日期的年份
      - 多个参数组合，使用下划线拼接
        - SECOND_MICROSECOND
        - HOUR_SECOND

- 时间和秒钟转换的函数
  - TIME_TO_SEC(time)
    - 将time转化为秒并返回结果值，转化公式为小时*3600+分钟*60+秒
  - SEC_TO_TIME(seconds)

- 计算日期和时间的函数（较常用）
  - DATE_ADD(datetime,INTERVAL expr type),ADDDATE(date,INTERVAL expr type)
    - 返回与给定日期时间相差INTERVAL时间段的日期时间
  - DATE_SUB(datetime,INTERVAL expr type),SUBDATE(date,INTERVAL expr type)
    - 返回与给定日期时间相差INTERVAL时间段的日期时间
  - ADDTIME(time1,time2)
    - 返回time1加上time2的时间。当time2为一个数字时，代表的是秒，可以为负数
  - SUBTIME(time1,time2)
    - 返回time1减去time2后的时间。当time2为一个数字时，代表的是秒，可以为负数
  - DATEDIFF(date1,date2)
    - 返回date1-date2的日期间隔天数
  - TIMEDIFF(time1,time2)
    - 返回time1-time2的时间间隔
  - FROM_DAY(N) 
    - 返回从0000年1月1日，N天以后的日期
  - TO_DAYS(date)
    - 返回日期date距离0000年1月1号的天数
  - LAST_DAT(date) 
    - 返回date所在月份的最后一天的日期
  - MAKEDATE(year,n) 
    - 针对给定年份与所在年份中的天数返回一个日期
  - MAKETIME(hour,minute,second)
    - 将给定的小时，分钟和秒组合成时间并返回
  - PERIOD_ADD(time,n)
    - 返回time加上n后的时间

- 日期的格式化与解析
  - DATE_FORMAT(date,fmt)
    - 按照字符串fmt格式化日期date值
    - 例：SELECT DATE_FORMAT(CURDATE(),'%Y-%M-%D')
  - TIME_FORMAT(time,fmt)
    - 按照字符串fmt格式化时间time值
  - GET_FORMAT(date_type,format_type)
    - 返回日期字符串的显示格式
  - STR_TO_DATE(str,fmt)
    - 按照字符串fmt对str进行解析，解析为一个日期
  - fmt参数的常用格式符
    - %Y：4位数字表示年份
    - %y：两位数字表示年份
    - %M：月名表示月份(January)
    - %m：两位数字表示月份(01,02,03...)
    - %b：缩写的月名(Jan,Feb...)
    - %c：数字表示月份(1,2,3)
    - %D：英文后缀表示月中的天数(1st,2nd,3rd)
    - %d：两位数字表示月中的天数(01,02...)
    - %e：数字形式表示月中的天数(1,2,3,4...)
    - %H：两位数表示小时，24小时制(01,02...)
    - %h和%I：两位数表示小时，12小时制(01,02...)
    - %k:数字形式的小时，24小时制(1,2,3)
    - %l：数字形式的小时，12小时制(1,2,3,4...)
    - %i：两位数字表示分钟(00,01,02)
    - %S和%s：两位数字表示秒(00,01,02...)
    - %W：一周中的星期名称(Sunday...)
    - %a：一周中的星期缩写(Sun,Mon,Tues,...)
    - %w：以数字表示周中的天数(0=Sunday,1=Monday...)
    - %j：以3位数字表示年中的天数(001,002...)
    - %U：以数字表示年中的第几周，(1,2,3...)其中Sunday为周中的第一天
    - %u：以数字表示年中的第几周，(1,2,3...)其中Monday为周中的第一天


#### 流程控制函数 
- IF(value,value1,value2)
  - 如果value的值为TRUE，返回value1，否则返回value2
- IFNULL(value1,value2)
  - 如果value1不为NULL，返回value1,否则返回value2
- CASE WHEN 条件1 THEN 结果1 WHEN 条件2 THEN 结果2...[ELSE resultn] END
  - 整理：CASE WHEN...THEN...WHEN...THEN...ELSE...END
  - 相当于Java的if...elseif...else...
  - 示例：
  ```sql
  SELECT last_name,salary,CASE WHEN salary >= 15000 THEN '白骨精'
                               WHEN salary >= 10000 THEN '潜力股'
                               WHEN salary >= 8000 THEN '小屌丝'
                               ELSE '草根' END "details"
  FROM employees;
  ```
- CASE expr WHEN 常量值1 THEN 值1 WHEN 常量值2 THEN 值2...[ELSE 值n] END
  - 相当于JAVA的switch... case...

#### 加密与解密函数
- 概述：加密与解密函数主要用于对数据库中的数据进行加密和解密处理，以防止数据被他人窃取。这些函数在保证数据库安全是非常有用。
- PASSWORD(str)
  - 返回字符串str的加密版本，41位长的字符串。加密结果不可逆，常用于用户的密码加密
  - <font color=tomato>MySQL8.0中弃用</font>
- MD5(str)
  - 返回字符串str的MD5加密后的值，也是一种加密方式。若参数为NULL，则会返回NULL
- SHA(str)
   - 从原明文密码str计算并返回加密后的密码字符串，当参数为NULL时，返回NULL。SHA加密算法比MD5更加安全
- ENCODE(value,password_seed)
  - 返回使用password_seed作为加密密码加密value
  - <font color=tomato>MySQL8.0中弃用</font>
- DECODE(value,password_seed)
  - 返回使用password_seed作为加密密码解密value
  - <font color=tomato>MySQL8.0中弃用</font>

#### MySQL信息函数
- VERSION()
  - 返回当前MYSQL的版本号
- CONNECTION_ID()
  - 返回当前MySQL服务器的连接数
- DATABASE(),SCHEMA()
  - 返回MySQL命令行当前所在的数据库
- USER(), CURRENT_USER(), SYSTEM_USER(), SESSION_USER()
  - 返回当前连接MySQL的用户名，返回结果格式为“主机名@用户名”
- CHARSET(valuse)
  - 返回字符串value自变量的字符集
- COLLATION(value)
  - 返回字符串value的比较规则

#### 其他函数
- FORMAT(value,n)
  - 返回对数字value机型格式化后的结果数据。n表示四舍五入后保留小数点后n位
  - 如果n的值小于或者等于0，则只保留整数
- CONV(value,from,to)
  - 将value的值进行不同进制之间的转换
- INET_ATON(ipvalue)
  - 将以点分隔的IP地址转化为一个数字
- INET_NTON(value)
  - 将数字形式的IP转化为以点分隔的IP地址
- BENCHMARK(n,expr)
  - 将表达式expr重复执行n次。用于测试MySQL处理expr表达式所耗费的时间
- CONVERT(value USING char_code)
  - 将value所使用的字符编码修改为char_code


### 聚合函数
- 概述：什么是聚合函数
  - 作用于一组数据，并对一组数据返回一个值
    - 比如；一组数据中，在多个数据里选出最大值，就是一个聚合函数

- 常用聚合函数类型
  - AVG()
  - SUM()
  - MAX()
  - MIN()
  - COUNT()
  - 注意：
    - AVG()和SUM()只适用于数值类型的字段（或变量）
    - COUNT(*)和COUNT(1)能够查看表中有多少条记录
    - COUNT(具体字段)不能准确查出，因为COUNT()无法识别NULL

#### GROUP BY的使用
- 示例：
  ```sql
  # 需求：查询各个部门的平均工资，最高工资
  SELECT department_id,AVG(salary),MAX(salary)
  FROM employees
  GROUP BY department_id;
  ```
 - 使用多个列分组
  ```sql
  # 需求：查询各个department_id,job_id的平均工资
  SELECT department_id,job_id,AVG(salary)
  FROM employees
  GROUP BY department_id,job_id;

  当字段和GROUP BY 的分组不匹配时，MySQL的给出的信息是错误的，Oracle会报错
  SELECT department_id,job_id,AVG(salary)
  FROM employees
  GROUP BY department_id; -- oracle报错
  ```
  - 结论1：SELECT中出现的非组函数的字段必须声明在GROUP BY中。反之，Group BY中声明的字段可以不出现在SELECT中。
  - 结论2：GROUP BY声明在FROM和WHERE后面，ORDER BY和LIMIT的前面
  - MYSQL中GROUP BY使用WITH ROLLUP
  ```sql
  -- 使用WITH ROLLUP关键字之后，在所有查询出的分组记录之后增加一条记录，该记录计算查询出的所有记录的总和(即，按照所有数据，去得出聚合函数的值)，即统计记录数量
  # MYSQL中GROUP BY使用WITH ROLLUP
  SELECT department_id,AVG(salary)
  FROM employees
  GROUP BY department_id WITH ROLLUP;
  -- WITH ROLLUP和ORDER BY不能同时使用，否则会报错。 
  ```

#### HAVING的使用
- 用来过滤数据的
```sql
  # 需求：查询部门最高工资比10000高的部门
  SELECT department_id,MAX(salary)
  FROM employees
  GROUP BY department_id
  HAVING MAX(salary) > 10000;

  -- 要求1：如果过滤条件中使用了聚合函数，则必须使用HAVING来替换WHERE。否则，报错！！
  -- 要求2：如果使用了HAVING，HAVING必须声明在GROUP BY的后面
  -- 要求3：开发中，我们使用HAVING的前提是SQL中使用了GROUP BY

  # 需求：查询部门id为10,20,30,40个部门中最高工资比10000高的部门信息
  -- 方式一：推荐，执行效率高于方式二
  SELECT department_id,MAX(salary)
  FROM employees
  WHERE department_id IN (10,20,30,40)
  GROUP BY department_id
  HAVING MAX(salary > 10000);

  -- 方式二：
  SELECT department_id,MAX(salary)
  FROM employees
  GROUP BY department_id
  HAVING department_id IN (10,20,30,40) AND MAX(salary) > 10000;

  -- 结论：当过滤条件中有聚合函数时，则此过滤条件必须声明在HAVING中
  -- 当过滤条件中，没有聚合函数时，则此过滤条件声明在where中或HAVING中都可以，但是建议声明在WHERE中

  /*
    WHERE 与 HAVING 的对比
    1.HAVING的适用范围更广
    2.如果过滤条件是非聚合函数，这种情况下，WHERE的执行效率要高于HAVING

  */
```

#### SQL底层执行原理
- SELECT语句的完整结构
```sql
# SQL92语法：
SELECT ...,...,...(存在聚合函数)
FROM ...,...
WHERE 多表的连接条件 AND 不包含聚合函数的过滤条件
GROUP BY ...,...
HAVING 包含聚合函数的过滤条件
ORDER BY ...,...(ASC/DESC)
LIMIT ...,...

#SQL99语法：
SELECT ...,...,...(存在聚合函数)
FROM ...(LEFT/RIGHT/INNER)JOIN...ON... 多表连接条件
JOIN...ON...
WHERE 不包含聚合函数的过滤条件
GROUP BY ...,...
HAVING 包含聚合函数的过滤条件
ORDER BY ...,...(ASC/DESC)
LIMIT ...,...

# SQL语句的执行过程
1. FROM <left_table>
2. ON <join_condition>
3. <join_type> JOIN <right_table>
4. WHERE <where_condition>
5. GROUP BY <group_by_list>
6. HAVING <having_condition>
7. SELECT
8. DISTINCT <select_list>
9. ORDER BY <order_by_condition>
10. LIMIT <limit_number>

```

### 子查询
- 概述： 
  - 子查询指一个查询语句嵌套在另一个查询语句内部的查询，这个特性从MYSQL4.1开始引入
  - SQL中子查询的使用大大增强了SELECT查询的能力，因为很多时候查询需要从结果集中获取数据，或者需要从同一个表中先计算得出一个数据结果，然后与这个数据结果（可能是某个标量，也可能是某个集合）进行比较
#### 需求分析与问题解决
- 实际问题 
  - 问：谁的工资比Abel的高？
    - 问题拆解：先求出Abel的工资，然后查询比Abel工资高的员工
```sql
-- 方式1：
SELECT salary
FROM employees
WHERE last_name = 'Abel' -- 查询到：Abel的工资是11000

SELECT last_name,salary
FROM employees
WHERE salary > 11000;  -- 得出超过Abel工资的员工

-- 方式2（自连接）：
SELECT last_name,salary
FROM employees e1,employees e2
WHERE e2.salary > e1.salary AND e1.last_name = 'Abel';

-- 方式3（子查询）：
SELECT last_name,salary
FROM employees
WHERE salary > (
  SELECT salary
  FROM employees
  WHERE last_name = 'Abel'
);

```

#### 称谓的规范
- 外查询和内查询
  - 外查询：也叫主查询
  - 内查询：也叫子查询
    - 子查询在主查询之前一次执行完成
    - 子查询的结果被主查询(外查询)使用。

- 注意：
  - 子查询要包含在括号内
  - 将子查询放在比较条件的右侧
  - 单行操作符对应单行子查询，多行操作符对应多行子查询

- 子查询分类
  - 角度1：内查询返回的结果的条目数
    - 单行子查询
    - 多行子查询
  - 角度2：内查询是否被执行多次
    - 相关子查询
    - 不相关子查询

```sql
-- 相关子查询；
-- 查询工资大于本部门平均工资的员工信息
-- 内查询的平均工资，和外查询的员工部门有关联性


-- 不相关子查询
-- 查询工资大于本公司平均工资的员工信息
-- 不相关原因：无论查询哪个员工的工资，本公司的平均工资恒定
```

#### 单行子查询
- 单行操作符
  - `=`      equal to
  - `！=`    not equal to
  - `>`      greater than
  - `<`      less than
  - `>=`     greater than or equal to
  - `<=`     less than or equal to
  - `<>`     not equal to

- 子查询编写技巧
  - 从里往外写
  - 从外往里写

```sql
-- 题目：查询与141号员工的manager_id和department_id相同的其他员工的employee_id, manager_id,department_id
-- 方式1
SELECT employee_id,manager_id,department_id
FROM employees
WHERE manager_id = (
      SELECT manager_id
      FROM employees
      WHERE employee_id = 141
)
AND department_id = (
      SELECT department_id
      FROM employees
      WHERE employee_id = 141
)
AND employee_id <> 141;

-- 方式2
-- 方式1中，查询的表格和过滤条件都一样，仅有查询字段不同，可以同时将两个字段一起查询
SELECT employee_id,manager_id,department_id
FROM employees
WHERE (manager_id,department_id) = (
      SELECT manager_id,department_id
      FROM employees
      WHERE employee_id = 141
)
AND employee_id <> 141;
```

- HAVING中的子查询
  - 首先执行子查询
  - 向主查询中的HAVING子句返回结果 

```sql
-- 题目：查询最低工资大于50号部门最低工资的部门id和其最低工资
SELECT department_id,MIN(salary)
FROM employees
WHERE department_id IS NOT NULL 
GROUP BY department_id
HAVING MIN(salary) > (
        SELECT MIN(salary)
        FROM employees
        WHERE department_id = 50
);

-- 题目：显示员工的employee_id,last_name和location
-- 其中，如果员工department_id与location_id为1800的department_id相同，则location为'Canada'，其余则为'USA'
SELECT employee_id,last_name,CASE department_id WHEN (
        SELECT department_id
        FROM departments
        WHERE location_id = 1800
) THEN 'Canada'
ELSE 'USA' END "location"
FROM employees;

```

#### 多行子查询
- 特点：
  - 内查询返回多行
  - 使用多行比较操作符

- 多行比较操作符
<table>
  <thead>
    <th style="background-color:darkred;color:white">操作符</th>
    <th style="background-color:darkred;color:white">含义</th>
  </thead>
  <tbody>
    <tr>
      <td>IN</td>
      <td>等于列表中的任意一个</td>
    </tr>
    <tr>
      <td>ANY</td>
      <td>需要和单行比较操作符一起使用，和子查询返回的某一个值比较</td>
    </tr>
    <tr>
      <td>ALL</td>
      <td>需要和单行比较操作符一起使用给，和子查询返回的所有值比较</td>
    </tr>
    <tr>
      <td>SOME</td>
      <td>实际上是ANY别名，作用相同，一般使用ANY</td>
    </tr>
  </tbody>
</table>

```sql
-- IN 举例:
SELECT employee_id, last_name
FROM employees
WHERE salary IN (
        SELECT MIN(salary)
        FROM employees
        GROUP BY department_id
);

-- ANY/ALL
-- 题目：返回其他job_id中比job_id为'IT_PROG'部门任一工资低的员工的员工号，姓名，job_id以及salary
SELECT employee_id,last_name,job_id,salary
FROM employees
WHERE job_id <> 'IT_PROG'
AND salary < ANY (
        SELECT salary
        FROM employees
        WHERE job_id = 'IT_PROG'
);

-- 题目：返回其他job_id中比job_id为'IT_PROG'部门所有工资低的员工的员工号，姓名，job_id以及salary
SELECT employee_id,last_name,job_id,salary
FROM employees
WHERE job_id <> 'IT_PROG'
AND salary < ALL (
        SELECT salary
        FROM employees
        WHERE job_id = 'IT_PROG'
);

-- 题目：查询平均工资最低的部门id
-- 方法1：
SELECT department_id
FROM employees
GROUP BY department_id
ORDER BY AVG(salary) ASC
LIMIT 0,1

-- 单行函数可以嵌套，聚合函数不支持嵌套

-- 方法2：
SELECT department_id
FROM employees
GROUP BY department_id
HAVING AVG(salary) = (
	SELECT MIN(avg_sal) 
  -- 聚合函数不支持嵌套，但是可以将结果作为一张新表，然后再用聚合函数计算
  FROM(
        SELECT AVG(salary) avg_sal,department_id
        FROM employees
        GROUP BY department_id
      )dept_avg_sal
);

-- 方式3：

SELECT department_id
FROM employees
GROUP BY department_id
HAVING AVG(salary) <= ALL(
	SELECT AVG(salary) avg_sal
	FROM employees
	GROUP BY department_id
); 
```

#### 相关子查询
- 相关子查询执行流程：
  - 如果子查询的执行依赖于外部查询，通常情况下都是因为子查询中的表用到了外部的表，并进行了条件关联，因此每执行一次外部查询，子查询都要重新计算一次，这样的子查询就称之为关联子查询
  - 步骤：
    - GET：从主查询中获取候选列
    - EXECUTE：子查询使用主查询的数据
    - USE：如果满足子查询的条件则返回该行

- 总结：类似于编程中的for循环嵌套

```sql
-- 题目：查询员工中工资大于本部门平均工资的员工的last_name,salary和其department_id
-- 方式1：
SELECT last_name,salary,department_id
FROM employees e1
WHERE salary > (
        SELECT AVG(salary)
        FROM employees e2
        WHERE e2.department_id = e1.department_id
);

-- 方式2：在FROM中声明子查询
SELECT e.last_name,e.salary,e.department_id
FROM employees e,(
        SELECT department_id,AVG(salary) avg_sal
        FROM employees
        GROUP BY department_id
) t_dept_avg_sal
WHERE e.department_id = t_dept_avg_sal.department_id
AND e.salary > t_dept_avg_sal.avg_sal;

-- 在ORDER BY中使用子查询
-- 题目：查询员工的id，salary，按照department_name排序
SELECT employee_id,salary
FROM employees e
ORDER BY  (
  SELECT department_name
  FROM departments d
  WHERE e.department_id = d.department_id
);

```

- EXISTS与NOT EXISTS关键字
  - 概述：关联查询通常也会和EXISTS操作符一起使用给，用来检查在子查询中是否存在满足条件的行
  - 如果在子查询中不存在满足条件的行
    - 条件返回FALSE
    - 继续在子查询中查找
  - 如果在子查询中存在满足条件的行
    - 不在子查询中继续查找
    - 条件返回TRUE

```sql
-- 题目：查询公司管理者的employee_id,last_name,job_id,department_id信息
-- 方式1：
SELECT DISTINCT mgr.employee_id,mgr.last_name,mgr.job_id,mgr.department_id
FROM employees emp JOIN employees mgr
ON emp.manager_id = mgr.employee_id

-- 方式2：子查询
SELECT employee_id,last_name,job_id,department_id
FROM employees
WHERE employee_id IN (
          SELECT DISTINCT manager_id
          FROM employees
);

-- 方式3：使用EXISTS
SELECT employee_id,last_name,job_id,department_id
FROM employees
WHERE EXISTS (
          SELECT *
          FROM employees e2
          WHERE e1.employee_id = e2.manager_id  
)

-- 题目：查询departments表中，不存在于employees表中的部门的department_id和department_name
-- 方式1：
SELECT d.department_id,d.department_name
FROM demployees e RIGHT JOIN departments d
ON e.department_id = d.department_id
WHERE e.department_id IS NULL

-- 方式2：使用NOT EXISTS
SELECT department_id,department_name
FROM departments d
WHERE NOT EXISTS (
          SELECT *
          FROM employees e
          WHERE e.department_id = d.department_id
);
```

## 创建和管理表
### 基础知识
- 一条数据存储的过程（4步）：
  - 创建数据库
  - 确认字段
  - 创建数据表
  - 插入数据
 
- 标识符命名规则
  - 数据库名、表名不得超过30各字符，变量名限制为29个
  - 必须只能包含A-Z、a-z、0-9、_，共63个字符
  - 数据库名、表名、字段名等对象名中间不要包含空格
  - 同一个MySQL软件中
    - 数据库不能同名；
    - 同一个库中，表不能重名；
    - 同一个表中字段不能重名
  - 必须保证你的字段没有和保留字、数据库系统或常用方法冲突。如果坚持使用，请在SQL语句中使用" ` "(着重号)引起来
  - 保持字段名和类型的一致性：
    - 在命名字段并为其指定数据类型的时候一定要保证一致性，假如数据类型在一个表里是整数，那在另一个表里可就别变成字符型了

- 数据类型

### 创建和管理数据库
- 创建数据库
```sql
# 方式1：创建数据库
CREATE DATABASE 数据库名;

# 方式2：创建数据库并指定字符集
CREATE DATABASE 数据库名 CHARACTER SET 字符集;

-- 查看数据库管理系统字符集信息
SHOW variables like 'character_%';

# 方式3：判断数据库是否已经存在，不存在则创建数据库（推荐）
CREATE DATABASE IF NOT EXISTS 数据库名;
-- 如果MySQL中已经存在相关数据库，则忽略创建语句，不再创建数据库

SQL5.7及以前版本建议将字符集改为utf8,默认：ai_ci(拉丁)
CREATE DATABASE IF NOT EXISTS 数据库名 CHARACTER SET 'utf8';

-- 注意：
-- DATABASE不能改名。一些可视化工具可以改名
-- 原理：创建一个新库 -> 把所有表复制到新库 -> 再删掉就库
-- 本质上依然没有实现真正的直接改名

# 查看创建数据库的结构
SHOW CREATE DATABASE 数据库名;
```

- 管理数据库
```sql
# 查看当前所有的数据库
SHOW DATABASES;

# 查看当前正在使用的数据库
SELECT database();

# 指名/切换数据库
USE 数据库名；

# 查看当前数据库中保存的数据表
SHOW TABLES;

# 查看指定数据库下保存的数据表
SHOW TABLES FROM 数据库名;
```

- 修改数据库
```sql
# 更改数据库字符集
ALTER DATABASE 数据库名 CHARACTER set 字符集; -- 比如：gbk、utf8等
```

- 删除数据库
```sql
# 方式1：删除指定的数据库
DROP DATABASE 数据库名；

# 方式2：删除指定数据库名(推荐)
DROP DATABASE IF EXISTS 数据库名;
```
### 数据类型简述
<table>
<thead>
  <th style="background-color:darkred;color:white">类型</th>
  <th style="background-color:darkred;color:white">类型举例</th>
</thead>
<tbody>
  <tr>
    <td>整数类型</td>
    <td>TINYINT、SMALLINT、MEDIUMINT、<span style="font-weight:700;color:red">INT(或INTEGER)</span>、BIGINT</td>
  </tr>
  <tr>
    <td>浮点类型</td>
    <td>FLOAT、DOUBLE</td>
  </tr>
  <tr>
    <td>定点数类型</td>
    <td><span style="font-weight:700;color:red">DECIMAL</span></td>
  </tr>
  <tr>
    <td>位类型</td>
    <td>BIT</td>
  </tr>
  <tr>
    <td>日期时间类型</td>
    <td>YEAR、TIME、<span style="font-weight:700;color:red">DATE</span>、DATETIME、TIMESTAMP</td>
  </tr>
  <tr>
    <td>文本字符串类型</td>
    <td>CHAR、<span style="font-weight:700;color:red">VARCHAR</span>、TINYTEXT、TEXT、MEDIUMTEXT、LONGTEXT</td>
  </tr>
  <tr>
    <td>枚举类型</td>
    <td>ENUM</td>
  </tr>
  <tr>
    <td>集合类型</td>
    <td>SET</td>
  </tr>
  <tr>
    <td>二进制字符串类型</td>
    <td>BINARY、VARBINARY、TINYBLOB、BLOB、MEDIUMBLOB、LONGBLOB</td>
  </tr>
  <tr>
    <td>JSON类型</td>
    <td>JSON对象、JSON数组</td>
  </tr>
  <tr>
    <td>空间数据类型</td>
    <td>单值：GEOMETRY、POINT、LINESTRING、POLYGON;</br>集合：MULTIPOINT、MULTILINESTRING、MULTIPOLYGON、GEOMETRYCOLLECTION</td>
  </tr>
</tbody>
</table>

### 数据类型精讲
- 字符集
  - 属性：character set name
  - 代码示例
  ```sql
  # 创建数据库时指明字符集
  CREATE DATABASE IF NOT EXISTS dbtest12 CHARACTER SET 'utf8';

  # 创建表的时候，指明表的字符集
  CREATE TABLE temp (
    id INT
  ) CHARACTER SET 'utf8';

  # 创建表，指明表中的字段时，可以指定字段的字符集
  CREATE TABLE temp1 (
    id INT,
    `name` VARCHAR(15) CHARACTER SET 'gbk'
  );
  ```

#### 整数数据类型
- 以MYSQL5.7为主，进行测试
<table>
  <thead>
    <th style="background:darkred;color:white;">整数类型</th>
    <th style="background:darkred;color:white;">字节</th>
    <th style="background:darkred;color:white;">有符号数取值范围</th>
    <th style="background:darkred;color:white;">无符号数取值范围</th>
  </thead>
  <tbody>
    <tr>
      <td>TINYINT</td>
      <td>1</td>
      <td>-128~127</td>
      <td>0~255</td>
    </tr>
    <tr>
      <td>SMALLINT</td>
      <td>2</td>
      <td>-32768~32767</td>
      <td>0~65535</td>
    </tr>
    <tr>
      <td>MEDIUMINT</td>
      <td>3</td>
      <td>-8388608~8388607</td>
      <td>0~16777215</td>
    </tr>
    <tr>
      <td>INT(INTEGER)</td>
      <td>4</td>
      <td>-2147483648~2147483647</td>
      <td>0~4294967295</td>
    </tr>
    <tr>
      <td>BIGINT</td>
      <td>8</td>
      <td>-2^63~2^63-1</td>
      <td>0~2^64</td>
    </tr>
  </tbody>
</table>

```sql
USE dbtest12;

CREATE TABLE test_int1 (
  fl TINYINT,
  f2 SMALLINT,
  f3 MEDIUMINT,
  f4 INTEGER,
  f5 BIGINT
);

-- Out of range value for column 'f1' at row 1
INSERT INTO test_int1(f1)
VALUES(128); // 超出范围，报错

DESC test_int1;
-- 5.7版本中，type的类型后面会有(num),eg: tinyint(4), 这里4指的是显示宽度
-- 因为tinyint共占1个字节，无符号数范围是0~256,正好是4位
-- 8.0版本不显示数字

# (M)和ZEROFILL参数

CREATE TABLE test_int2 (
  f1 INT,
  f2 INT(5), -- 括号里的数字表示显示宽度，但是单独一个参数，并没有意义，还是以数据本身范围为依据
  f3 INT(5) ZEROFILL
  -- 配合ZEROFILL，表示不足(M)位，其余位数用0填充，超出位数，正常显示
  -- 使用ZEROFILL的时候，默认是unsigned无符号数字
)

INSERT INTO test_int2(f1,f2)
VALUES (123,123),(123456,123456);

CREATE TABLE test_int3(
  f1 INT UNSIGNED // 如果数据不包含负数，建议使用UNSIGNED
)
```

#### 浮点类型
- 分类：
  - FLOAT(M,D) // 非标准语法，标准语法仅是FLOAT
  - DOUBLE(M,D)
    - M：精度= 整数位+小数位
    - D：标度= 小数位
```sql
CREATE TABLE test_double1(
  f1 FLOAT,
  f2 FLOAT(5,2),
  f3 DOUBLE,
  f4 DOUBLE(5,2)
);

-- 浮点是数不准确的，所以我们要避免使用‘=’来判断两个浮点数是否相等
```

#### 定点数
- DECIMAL
- 数据类型：
  - DECIMAL(M,D) | DEC | NUMERIC
    - M：精度：0 <= M <= 65
    - D: 标度：0 <= D <= 30
    - D < M
  - 字节数：M+2字节
  - 有效范围：由M和D决定
- 定点数在MySQL内部是以`字符串`的形式进行存储的，这就决定了它一定是精准的
- 当DECIMAL类型不指定精度和标度时，默认为DECIMAL(10,0)。当数据的精度超出了定点数类型的范围时，MySQL同样会进行四舍五入

- 浮点数和定点数的使用场景：
  - 如果对于精度的要求极高，建议使用定点数
  - 浮点数相对于定点数的优点是在长度一定的情况下，浮点数的取值范围大，但不精确，适用于需要取值范围大，又可以容忍微小误差的科学计算场景（比如计算化学，分子建模，流体力学等）


#### 位类型：BIT(M)
- BIT类型中存储的是二进制值，类似010110
- BIT类型，如果没有指定(M)，默认是1位。这个1位，表示只能存1位二进制数。这里(M)表示二进制的位数，位数最小为1，最大为64
- 占用空间：约为(M+7)/8个字节
```sql
CREATE TABLE test_bit1(
  f1 BIT,
  f2 BIT(5),
  f3 BIT(64)
);

INSERT INTO test_bit1 (f1)
VALUES(2);

INSERT INTO test_bit1 (f2)
VALUES(31);

SELECT BIT(f1),BIT(f2),HEX(f1),HEX(f2)
FROM test_bit1;

-- 此时+0以后，数据可以以十进制显示
SELECT f1 + 0,f2 + 0
FROM test_bit1;

```

#### 日期与时间类型
- 数据类型：
  - YEAR类型，通常用来表示年
    - 字节：1
    - 日期格式：YYYY或YY
    - 最小值1901，最大值2155，受限于只有1个字节，所以只能表示256年
    - 推荐用4位表示
    - 注意：2位表示时
      - 当取值01到69，表示2001到2069；
      - 当取值70到99，表示1970到1999；
      - 当取值整数的0或00添加的话，那么是0000年
      - 当取值是日期/字符串的'0'添加的话，是2000年
  - DATE类型，通常用来表示年、月、日
    - 字节：3
    - 日期格式：YYYY-MM-DD（推荐） | YY-MM-DD
    - 最小值：1000-01-01；最大值：9999-12-03
  - TIME类型，通常用来表示时、分、秒
    - 字节：3
    - 日期格式：HH:MM:SS
    - 最小值：-838:59:59；最大值：838:59:59
    - 注意：为什么时间类型TIME的取值范围不是-23:59:59到23:59:59?
      - 原因是MySQL设计的TIME类型，不光表示一天之内的时间，而且可以用来表示一个时间间隔，这个时间间隔可以超过24小时
  - DATETIME类型，通常用来表示，年、月、日、时、分、秒
    - 字节：8
    - 日期格式：YYYY-MM-DD HH:MM:SS
    - 范围：1000-01-01 00:00:00；到 9999-12-31 23:59:59
  - TIMESTMAP类型，通常用来表示带时区的年、月、日、时、分、秒
    - 字节：4
    - 日期格式：YYYY-MM-DD HH:MM:SS
    - 范围：1970-10-10 00:00:00UTC; 到2038-10-19 03:14:07UTC
    - 修改当前时区`SET time_zone = '+9:00';`

- 开发中经验
  - 在实际项目中，尽量用DATETIME类型。因为这个数据类型包括了完整的日期和时间信息，取值范围也最大，使用起来比较方便。
  - 一般存注册时间，商品发布时间等，不建议使用DATETIME存储，而是使用时间戳，因为DATETIME虽然直观，但不便于计算
  ```sql
  SELECT UNIX_TIMESTAMP();
  -- 用数字类型存储，比如BIGINT

  SELECT FROM_UNIXTIME(`TIMESTAMP`);
  -- FROM_UNIXTIME()将时间戳转换为时间格式
  ```

```sql
CREATE TABLE test_year(
  f1 YEAR,
  f2 YEAR(4) -- 不推荐后面加(4)，因为默认位4位
);

INSERT INTO test_year(f1)
VALUES('2021'),(2022); -- 建议加单引号使用 
-- 建议写4位，不写2位

CREATE TABLE test_date1(
  f1 DATE
);

INSERT INTO test_data1
VALUES('2020-10-01'),('20201001'),(20201001); -- 三种结果相同，推荐第一种

INSERT INTO test_data1
VALUES(CURDATE()),(CURRENT_DATE()),(NOW()); -- 记录当前时间

CREATE TABLE test_time1(
  f1 TIME
);

INSERT INTO test_time1
VALUES('2 12:30:29'),('12:35:29'),('12:40'),('2 12:40'),('1 05'),('45');
-- D HH:MM:SS ; HH:MM:SS ; HH:MM ; D HH:MM ; D HH ; SS
```

#### 文本字符串类型
- MYSQL中，文本字符串总体上分为CHAR、VARCHAR、TINYTEXT、TEXT、LONGTEXT、ENUM、SET等类型

<table>
  <thead>
    <th style="background-color:darkred;color:white;">文本字符串类型</th>
    <th style="background-color:darkred;color:white;">值的长度</th>
    <th style="background-color:darkred;color:white;">长度范围</th>
    <th style="background-color:darkred;color:white;">占用的存储空间</th>
  </thead>
  <tbody>
    <tr>
      <td>CHAR(M)</td>
      <td>M</td>
      <td>0<=M<=255</td>
      <td>M个字节</td>
    </tr>
    <tr>
      <td>VARCHAR(M)</td>
      <td>M</td>
      <td>0<=M<=65535</td>
      <td>M+1个字节</td>
    </tr>
    <tr>
      <td>TINYTEXT</td>
      <td>L</td>
      <td>0<=L<=255</td>
      <td>L+2个字节</td>
    </tr>
    <tr>
      <td>TEXT</td>
      <td>L</td>
      <td>0<=L<=65535</td>
      <td>L+2个字节</td>
    </tr>
    <tr>
      <td>MEDIUMTEXT</td>
      <td>L</td>
      <td>0<=L<=16777215</td>
      <td>L+3个字节</td>
    </tr>
    <tr>
      <td>LONGTEXT</td>
      <td>L</td>
      <td>0<=L<=4294967295</td>
      <td>L+4个字节</td>
    </tr>
    <tr>
      <td>ENUM枚举</td>
      <td>L</td>
      <td>1<=L<=65535</td>
      <td>1或2个字节</td>
    </tr>
    <tr>
      <td>SET</td>
      <td>L</td>
      <td>0<=L<=64</td>
      <td>1,2,3,4或8个字节</td>
    </tr>
  </tbody>
</table>

- char(M)类型
  - 没有指名M的情况下，默认一个字符
  - 固定长度
  - 如果保存时，数据的实际长度比CHAR类型声明的长度小，则会在右侧填充空格以达到指定的长度。当MySQL检索CHAR类型的数据时，CHAR类型的字段会去除尾部的空格

- VARCHAR(M)类型
  - VARCHAR(M)定义时，必须指定长度M，否则报错
  - MySQL4.0版本以下，varchar(20): 指的是20字节。如果存放UTF8汉字时，只能存6个(每个汉字3字节)
  - MySQL5.0版本以上，varchar(20): 指的是20字符
  - 检索VARCHAR类型的字段数据时，会保留数据尾部的空格。VARCHAR类型的字段所占用的存储空间为字符串实际长度加1个字节

- CHAR或VARCHAR如何选择
  - 情况1：存储很短的信息，比如门牌号码101，102等，这样很短的信息应该用char，因为varchar还要占个byte用于存储信息长度，得不偿失
  - 情况2：固定长度的。比如uuid作为主键，那用char更合适
  - 情况3：十分频繁更改column。因为varchar每次存储都要有额外的计算，得到长度等工作，如果一个非常频繁改变的，那就要有很多精力用于计算，而这些对char来说是不需要的
  - 情况4：具有存储引擎的情况
    - MyISAM(MySQL5.5之前的)数据存储引擎和数据列：MyISAM数据表，最好使用固定长度(CHAR)的数据列代替可变长度(VARCHAR)的数据列。这样使得整个表静态化，从而使数据检索更快，用空间换时间。
    - MEMORY(内存的)存储引擎和数据列：MEMORY数据表目前都使用固定长度的数据行存储，因此无论使用CHAR或VARCHAR列都没有关系，两者都有作为CHAR类型处理的
    - InnoDB(MySQL5.5之后版本)存储引擎，建议使用VARCHAR类型。因为对于InnoDB数据表，内部的行存储格式并没有区分固定长度和可变长度(所有数据行都是用指向数据列值的头指针)，而且<font color=tomato>主要影响性能的因素是数据行使用的存储总量</font>，由于char平均占用的空间多于varchar，所以除了简短并固定长度的，其他考虑varchar。这样节省空间，对磁盘I/O和数据存储总量比较好。

- TEXT类型
  - MySQL不允许用TEXT类型做主键
  - 开发经验：TEXT文本类型，可以存比较大的文本段，搜索速度稍慢，因此如果不是特别大的内容，建议使用CHAR、VARCHAR来代替。
  - 而且TEXT和BLOB类型的数据删除后容易导致“空洞”，使得文件碎片比较多，所以频繁使用的表不建议包含TEXT类型字段，建议单独分出去，单独用一个表

- ENUM类型（枚举）
  - 当ENUM类型包含1~255个成员时，需要1个字节的存储空间；
  - 当ENUM类型包含256~65535个成员时，需要2个字节的存储空间
  - ENUM类型的成员个数上限是65535
  - ENUM的值忽略大小写
  - 也可以直接使用索引还调用枚举元素
  ```sql
  CREATE TABLE test_enum (
    season ENUM('春','夏','秋','冬','unknow')
  );

  INSERT INTO test_enum
  VALUE (1),(3) --  春，秋 可以直接用索引调用枚举元素

  INSERT INTO test_enum
  VALUE ('UNKNOW') -- unknow 不区分大小写

  INSERT INTO test_enum
  VALUE (NULL); -- 没有限制非空的情况下，可以添加null
  ```

- SET类型
  - SET表示一个字符串对象，可以包含0个或多个成员，但成员个数的上限为64.设置字段值时，可以取取值范围内的0个或多个值
  ```sql
  CREATE TABLE test_set(
    s SET ('A','B','C')
  );

  INSERT INTO test_set (s) VALUES ('A'), ('A,B');

  INSERT INTO test_set (s) VALUES ('A,B,C,A');
  -- MySQL会自动删除重复的成员
  ```

#### 二进制字符类型
- BINARY类型和VARBINARY类型 （实际生产中用的很少）
  - 代码演示
  ```sql
  CREATE TABLE test_binary1(
    f1 BINARY, -- 不指明长度，默认为1
    f2 BINARY(3),
    -- f3 VARBINARY, VARBINARY后面必须指定长度
    f4 VARBINARY(10)
  );
  ```

- BLOB类型
  - BLOB是一个二进制大对象，可以容纳可变数量的数据
  - MySQL中的BLOB类型包括TINYBLOB、BLOB、MEDIUMBLOB和lONGBLOB 4种类型，它们可以容纳的最大长度不同。可以存储一个二进制的大对象，比如图片，音频和视频等
  - 需要注意的是，在实际工作中，往往不会在MySQL数据库中使用BLOB类型存储大对象数据，通常会将图片，音频和视频文件存储到服务器的磁盘上，并将图片、音频和视频的访问路径存储到MySQL中

#### JSON类型 
- JSON(JavaScript Object Notation)是一种轻量级的数据交换格式。简洁和清晰的层次结构使得JSON称为理想的数据交换语言。它易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输的效率。
  - <font color=tomato>JSON可以将JavaScript对象中表示的一组数据转换为字符串，然后就可以在网络或者程序之间轻松的传递这个字符串，并在需要的时候将它还原为各编程语言所支持的数据格式。</font>
  - 在MySQL5.7中，就已经支持JSON数据类型。在MySQL8.x版本中，JSON类型提供了可以自动验证的JSON文档和优化的存储结构，使得在MySQL中存储和读取JSON类型的数据更加方便和高效
  ```sql
  CREATE TABLE test_json(
    js json
  );

  INSERT INTO test_json (js)
  VALUES ('{"name":"zhangYF","age":18,"address":{"province":"HeiLongjiang","city":"Harbin"}}');
  ```
  - 提取JSON中的值
  ```sql
  SELECT js -> '$.name' AS NAME,
  js -> '$.age' AS age,
  js -> '$.address.province' AS province,
  js -> '$.address.city' AS city
  FROM test_json;
  ```

#### 空间类型
- 暂略

#### 小结及选择建议
- 在定义数据类型时
  - 如果确定是整数，就用INT
  - 如果确定是小数，就用DECIMAL(M,D)
  - 如果是日期与时间，就用DATETIME

- <font color=tomato>阿里巴巴《Java开发手册》之MySQL数据库：</font>
  - 任何字段如果为非负数，必须是UNSIGNED
  - 【强制】小数类型为DECIMAL，禁止使用FLOAT和DOUBLE
    - 说明：在存储的时候，FLOAT和DOUBLE都存在精度损失的问题，很可能在比较值的时候，得到不正确的结果。如果存储的数据范围超过DECIMAL的范围，建议将数据拆成整数和小数分开存储
  - 【强制】如果存储的字符串长度几乎相同，使用CHAR定长字符串类型
  - 【强制】VARCHAR是可变长字符串，不预先分配存储空间，长度不要超过5000.如果存储长度大于此值，定义字段类型为TEXT，独立出来一张表，用主键来对应，避免影响其他字段索引效率


### 创建数据表
```sql
# 方式1
CREATE TABLE [IF NOT EXISTS] 表名 (
        字段1 数据类型 [约束条件] [默认值],
        字段1 数据类型 [约束条件] [默认值],
        字段1 数据类型 [约束条件] [默认值],
        ...
        [约束条件]
);  -- 需要用户具备创建表的权限

-- 必须指定：表名、列名（或字段名）、数据类型、长度
-- 可选指定：约束条件、默认值

# 查看表结构
DESC 表名；
SHOW CREATE TABLE 表名；
-- 如果创建表时没有指明使用的字符集，则默认使用所在数据库的字符集

# 查看表数据
SELECT * FROM 表名;

--------------------------------------------------------------------------

# 方式2：基于现有的表
CREATE TABLE mytest2
AS
SELECT employee_id,last_name,salary
FROM employees;


-- 说明1：查询语句中字段的别名，可以作为新创建的表的字段名。
-- 说明2：此时的查询语句可以结构比较丰富，使用前面章节讲过的个各种SELECT

# 练习1：创建一个表employees_copy,实现对employees表的复制，包括表数据
CREATE TABLE employees_copy
AS
SELECT * 
FROM atguigudb.employees;

# 练习2：创建一个表employees_col,实现对employees表的复制，不包括表数据
CREATE TABLE employees_col
AS
SELECT * 
FROM atguigudb.employees
WHERE employee_id = NULL;
-- WHERE 1 = 2; 
```

### 修改数据表
```sql
-- 修改表 --> ALTER TABLE
# 添加一个字段
ALTER TABLE 表名 ADD [column] 字段名 字段类型 [FIRST|AFTER 字段名];

ALTER TABLE mytest
ADD salary DOUBLE(10,2); -- 整数位有8位，小数位有2位，一共10位

ALTER TABLE mytest
ADD phone_number VARCHAR(20) FIRST;

ALTER TABLE mytest
ADD email VARCHAR(50) AFTER emp_name;

# 修改一个字段
ALTER TABLE mytest
MODIFY emp_name VARCHAR(25);

# 重命名一个字段
ALTER TABLE mytest
CHANGE salary monthly_salary DOUBLE(10,2);
-- 改名的同时，也可以同时更改数据类型及长度

# 删除一个字段
ALTER TABLE mytest
DROP COLUMN phone_number;

# 重命名表
# 方式1：使用RENAME
RENAME TABLE emp
TO myemp

# 方式2：使用ALTER
ALTER TABLE emp
RENAME [TO] myemp; -- [T0]可以省略

# 删除表
DROP TABLE [IF EXISTS] 表名;
-- 删除表这个操作不能回滚（撤销）

# 清空表
TRUNCATE TABLE 表名：
-- 删除表中的所有数据
-- 释放表的存储空间
```

### DCL中的COMMIT和ROLLBACK
- COMMIT
  - 作用：提交数据，一旦执行COMMIT，则数据就被永久保存在数据库中，不能回滚

- ROLLBACK
  - 作用：一旦执行ROLLBACK，可以实现数据回滚，回滚到最近的一次COMMIT之后

- 对比 TRUNCATE TABLE 和 DELECT FROM
  - 相同点：都可以实现对表中所有数据的删除，同时保留表结构
  - 不同点：
    - TRUNCATE TABLE：一旦执行此操作，表数据全部清除，且数据不可回滚
    - DELECT FROM：一旦执行此操作，表数据可以全部清除，同时数据可以实现回滚

- DDL 和 DML 的说明
  - DDL的操作：一旦执行，不可回滚
    - 原理：DDL操作不能回滚的原因是：在执行DDL操作之后，一定会自动执行一次COMMIT，同时这次COMMIT不受`SET autocommit = FALSE` 影响
    - 操作DDL的时候，一定要慎重
  - DML的操作：默认情况下，一旦执行，不可回滚。
    - 但是，如果在执行DML之前，执行了`SET autocommit = FALSE`，则可以实现归滚

- 演示：DELECT FROM
```sql
COMMIT; --先提交一下，COMMIT就相当于存档

SET autocommit = FALSE;
-- 执行autocommit = FALSE

DELETE FROM employees_copy; -- 清除表中数据

SELECT * FROM employees_copy;

ROLLBACK; -- 数据回滚
```

### MySQL8.0新特性：DDL原子化
- DDL原子化：
  - 要么执行成功，要么回滚

- 演示：
```sql
CREATE DATABASE mytest;

USE mytest;

CREATE TABLE book1(
  book_id INT,
  book_name VARCHAR(255)
);

SHOW TABLES;

DROP TABLE book1,book2;

-- 在mysql5.7中，执行此操作，由于mytest数据库中没有表book2,因此会报错
-- 但是，在报错的同时，表book1仍然会被删除

-- 在mysql8.0中，执行此操作，依然会报错，但是book1不会删除，即原子化
-- 原子化：要么成功，要么回滚
```

### DML（数据处理之增删改）
- 添加数据
  - 方式1：一条一条添加
  - 代码示例
  ```sql
  # 方式1: 没有指名添加字段
  INSERT INTO emp1
  VALUES (1,'Tom','2020-12-21',3500); -- 按声明的字段的先后顺序添加

  # 方式2：指名添加字段
  INSERT INTO emp1 (id,hire_date,salary,`name`)
  VALUES (2,'1999-09-09',4000,'Jerry');

  # 方式3：同时插入多条数据 (推荐)
  INSERT INTO table_name (column1,column2...columnn)
  VALUE
  (value1 [,value2,..., valuen]),
  (value1 [,value2,..., value n]),
  ...
  (value1 [,value2,..., valuen]);
  ```
  - 方式2：将查询结果插入表中
  - 代码演示
  ```sql
  INSERT INTO emp1(id,`name`,salary,hire_date)
  SELECT employee_id,last_name,salary,hire_date -- 查询语句
  -- 查询的字段一定要与添加到表的字段一一对应
  FROM employees
  WHERE department_id IN (70,60);

  -- 说明：emp1表中添加的数据的范围不能低于employees表中查询的字段长度 
  ```

- 更新数据（或修改数据）
  - UPDATE ... SEST ... WHERE...
  - 代码示例
  ```sql
  UPDATE emp1
  SET hire_date = CURDATE()
  WHERE id = 5;

  # 同时修改一条数据的多个字段
  UPDATE emp1
  SET hire_date = CURDATE(),salary = 6000
  WHERE id = 4;
  ```

- 删除数据
  - DELETE FROM ... WHERE ...
  - 代码示例
  ```sql
  DELETE FROM emp1
  WHERE id = 1;
  ```

- 小结：
  - DML操作默认情况下，执行完以后都会自动提交数据
  - 如果希望执行完成以后，不自动提交数据，则需要使用`SET autocommit = FALSE`

- MySQL8新特性：计算列
  - 概念：某一列的值是通过别的列计算得来的
  - MySQL8.0中，CREATE TABLE和ALTER TABLE都支持增加计算列
  - 代码演示
  ```sql
  CREATE TABLE test1 (
    a INT
    b INT
    C INT GENERATED ALWAYS AS (a + b) VIRTUAL  -- c即为计算列
  )

  INSERT INTO test1 (a,b)
  VALUES (10,20);
  ```


## 数据完整性与约束
- 约束(constraint)概述
  - 为什么需要约束
    - 数据完整性(Data Integrity)是指数据的精确性(Accuracy)和可靠性(Reliability)。它是防止数据库中存在不符合语义规定的数据和防止因错误信息的输入输出造成无效操作或错误信息而提出的
    - 为了保证数据的完整性，SQL规范以约束的方式对<font color=red>表数据进行额外的条件限制</font>。从以下四个方面考虑：
      - <font color=tomato>实体完整性(Entity Integrity)</font>: 例如，同一个表中，不能存在两条完全相同无法区分的记录
      - <font color=tomato>域完整性(Domain Integrity)</font>: 例如：年龄范围0-120，性别范围“男/女”
      - <font color=tomato>引用完整性(Referential Integrity)</font>: 例如：员工所在部门，在部门表中要能找到这个部门
      - <font color=tomato>用户自定义完整性(User-defined Integrity)</font>: 例如：用户名唯一，密码不能为空等，本部门经理的工资不得高于本部门职工的平均工资的5倍

- 什么是约束
  - 约束是表级的强制规定
  - 可以在创建表时规定约束 (<font color=red>通过CREATE TABLE语句</font>)，或者在表创建之后通过<font color=red>ALTER TABLE</font>语句规定约束

### 约束的分类
- 角度1：约束的字段个数
  - 单列约束
  - 多列约束

- 角度2：约束的作用范围
  - 列级约束
    - 将此约束声明在字段后面
  - 表级约束
    - 在表中所有字段都声明完之后，在所有字段的后面声明的约束

- 角度3：约束的作用
  - `not null`  非空约束
  - `unique`  唯一性约束
  - `primary key`  主键约束
  - `foreign key`  外键约束
  - `check`  检查约束
  - `default`  默认值约束

- 如何查看表中的约束
```sql
SELECT * FROM information_schema.table_constraints
WHERE table_name='表名称';
```

### 非空约束
- 作用：限定某个字段/某列的值不允许为空

- 关键字：`NOT NULL`

- 特点：
  -  默认，所有的类型的值都可以是NULL，包括INT、FLOAT等数据类型
  -  非空约束只能出现在表对象的列上，只能某个列单独限定非空，不能组合非空
  -  一个表可以有很多列都分别限制非空
  -  空字符''不等于NULL，0也不等于NULL

- 添加非空约束
  - 建表时
  ```sql
  CREATE TABLE 表名称(
    字段名 数据类型,
    字段名 数据类型 NOT NULL,
    字段名 数据类型 NOT NULL
  );
  ```
  - 示例
  ```sql
  CREATE DATABASE dbtest;
  USE dbtest;

  CREATE TABLE test1(
    id INT NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    email VARCHAR(25),
    salary DECIMAL(10,2)
  )

  INSERT INTO test1
  VALUES(1,'Tom','tom@123.com',3400);

  INSERT INTO test1(id,email,salary)
  VALUES(2,'tom@123.com',3400); -- 因为last_name未填值，默认为NULL
  -- 又因为在创建表单的时候添加了非空约束，因此报错
  ```
  - 在ALTER TABLE时添加非空约束
  ```sql
  ALTER TABLE test1
  Modify salary DECIMAL(10,2) NOT NULL;
  ```

### 唯一性约束
- 作用：用来限制某个字段/某列的值不能重复

- 关键字：`UNIQUE`

- 特点：
  - 同一个表可以有多个唯一约束
  - 唯一约束可以是某一个列的值唯一，也可以多个列组合的值唯一
  - 唯一性约束允许列值为空
  - 在创建唯一约束的时候，如果不给唯一约束命名，就默认和列名相同
  - <font color=red>MySQL会给唯一约束的列上默认创建一个唯一索引</font>

- 添加唯一性约束
  - 建表时
  ```sql
  CREATE TABLE test2(
    id INT UNIQUE, -- 列级约束
    last_name VARCHAR(15),
    email VARCHAR(25) UNIQUE,
    salary DECIMAL(10,2)
  );

  CREATE TABLE test2(
    id INT, 
    last_name VARCHAR(15),
    email VARCHAR(25),
    salary DECIMAL(10,2),

    -- 表级约束
    CONSTRAINT uk_test2_email UNIQUE(email)
    -- 给email字段添加UNIQUE约束，约束名为uk_test2_email
    UNIQUE(id)
    -- 也可以不加约束名，直接给字段添加唯一约束，约束名默认和字段名相同
  );
  ```
  - 建表后指定唯一约束
  ```sql
  -- 方式1：
  -- 可以创建多字段，复合唯一，即多个字段的组合是唯一的
  ALTER TABLE 表名称 ADD UNIQUE KEY(字段列表);
  ```
  ```sql
  -- 方式2：
  ALTER TABLE 表名称 MODIFY 字段名 UNIQUE;
  ```

  - 删除唯一性约束
    - 添加唯一性约束的列上也会自动创建唯一索引
    - 删除唯一约束只能通过删除唯一索引的方式删除
    - 删除时需要指定唯一索引名，唯一索引名和唯一约束名相同
    - 如果创建唯一约束时未指定名称，如果是单列，就默认和列名相同；如果是组合列，那么默认和()中排在第一个的列名相同。也可以自定义唯一性约束名
  - 删除唯一索引示例：
  ```sql
  -- 如何删除唯一性索引
  ALTER TABLE test2
  DROP INDEX last_name; -- INDEX后面接唯一约束名
  ```

### 主键约束(PRIMARY KEY)
- 作用：用来唯一标识表中的一行记录

- 关键字：`PRIMARY KEY`

- 特点：
  - 主键约束相当于唯一约束+非空约束的组合，主键约束列不允许重复，也不允许出现空值
  - <font color=tomato>一个表最多只能有一个主键约束</font>，建立主键约束可以在列级别创建，也可以在表级别上创建
  - 主键约束对应着表中的一列或者多列（复合主键）
  - 如果是多列组合的复合主键约束，那么这些列都不允许为空值，并且组合的值不允许重复
  - <font color=tomato>MySQL主键名总是PRIMARY，就算自己命名了主键约束名也没用</font>
  - 当创建主键约束时，系统默认会在所在的列或列组合上建立对应的主键索引（能够根据主键查询的，就根据主键查询，效率更高）。如果删除主键约束了，主键约束对应的索引就自动删除了
  - 需要注意的一点是，不要修改主键字段的值。因为主键是数据记录的唯一标识，如果修改了主键的值，就有可能会破环数据的完整性。

- 添加主键约束
  - 在CREATE TABLE时添加约束
  ```sql
  CREATE TABLE test3(
    id INT PRIMARY KEY,  -- 列级约束
    last_name VARCHAR(15),
    salary DECIMAL(10,2),
    email VARCHAR(25)
  );

   CREATE TABLE test3(
    id INT,
    last_name VARCHAR(15),
    salary DECIMAL(10,2),
    email VARCHAR(25),

    PRIMARY KEY(id)  -- 表级约束，没有必要起名字 
  );
  ```
  ```sql
  -- 创建复合主键
  CREATE TABLE user1(
    id INT,
    `name` VARCHAR(15),
    `password` VARCHAR(25),

    PRIMARY KEY(`name`,`password`)
  );
  ```
  - 在ALTER TABLE时添加约束
  ```sql
  CREATE TABLE test6(
    id INT,
    last_name VARCHAR(15),
    salary DECIMAL(10,2),
    email VARCHAR(25)
  );

  ALTER TABLE test6
  ADD PRIMARY KEY(id);
  ```
  - 删除主键约束
  ```sql
  ALTER TABLE 表名称 DROP PRIMARY KEY;
  ```
  - <font color=tomato>在实际开发中，不会去删除表中的主键约束</font>


### 自增列：AUTO_INCREMENT
- 作用：某个字段的值自增

- 关键字：`AUTO_INCREMENT`

- 特点和要求
  - <font color=tomato>一个表最多只能有一个自增长列</font>
  - 当需要产生唯一标识符或顺序值时，可设置自增长
  - 自增长列约束的列必须是键列(主键列，唯一键列)
  - 自增约束的列的数据类型必须是整数类型
  - 如果自增长列指定了0和null，会在当前最大值的基础上自增；如果自增列手动指定了具体值，直接赋值为具体值

- 创建自增长列
  - 在CREATE TABLE时添加
  ```sql
  CREATE TABLE test7(
    id INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(15)
  );
  -- 开发中，通常将自增长列添加到主键约束上
  ```
  - 在ALTER TABLE时添加
  ```sql
  ALTER TABLE test7
  MODIFY id INT AUTO_INCREMENT;
  ```

- 在ALTER TABLE时删除
```sql
ALTER TABLE test7
MODIFY id INT; -- 修改时不添加，则自动删除自增长
```

- MySQL8.0新特性-自增变量的持久化
  - MYSQL5.7演示
  ```sql
  CREATE TABLE test9(
    id INT PRIMARY KEY AUTO_INCREMENT
  );

  INSERT INTO test9
  VALUES(0),(0),(0),(0);

  SELECT * FROM test9; -- id的列值为1，2，3，4

  DELETE FROM test9
  WHERE id = 4;

  INSERT INTO test9
  VALUES(0); -- id的值为1，2，3，5

  DELETE FROM test9
  WHERE id = 5;

  重启MySQL

  SELECT * FROM test9;  -- 此时id的值为1,2,3

  INSERT INTO test9
  VALUES(0);  -- id的值为1，2，3，4

  原理：重启后，内存中的数据不在了，id依然从3开始自增
  ```
  - MySQL8.0演示
  ```sql
  CREATE TABLE test9(
    id INT PRIMARY KEY AUTO_INCREMENT
  );

  INSERT INTO test9
  VALUES(0),(0),(0),(0);

  SELECT * FROM test9; -- id的列值为1，2，3，4

  DELETE FROM test9
  WHERE id = 4;

  INSERT INTO test9
  VALUES(0); -- id的值为1，2，3，5

  DELETE FROM test9
  WHERE id = 5;

  重启MySQL

  SELECT * FROM test9;  -- 此时id的值为1,2,3

  INSERT INTO test9
  VALUES(0);  -- id的值为1，2，3，6
  ```
  - MySQL8.0持久化自增原理
    -  原理：MySQL8.0将自增主键计数器持久化到重做日志中，每次计数器发生变化，都会将其写入重做日志中。如果 数据库重启，InnoDB会根据重做日志的信息来初始化计算器的内存值


### 外键约束-FOREIGN KEY
- 作用：
  - 限定某个表的某个字段的引用完整性
  - 比如：员工表的员工所在部门的选择，必须在部门表能找到对应的部分

- 关键字：`FOREIGN KEY`

- 主表和从表/父表和子表
  - 主表(父表)：被引用的表，被参考的表
  - 从表(子表)：引用别人的表，参考别人的表
  - 例如：员工表的员工所在部门这个字段的值要参考部门表：部门表是主表，员工表是从表

- 特点：
  1. 从表的外键列，必须引用/参考主表的键主键或唯一约束的列
    - 为什么：因为被依赖/被参考的值必须唯一
  2. 在创建外键约束时，如果不给外键约束命名，默认不是列名，而是自动产生一个外键名(例如:student_ibfk_1;)，也可以指定外键约束名
  3. 创建(CREATE)表时就指定外键的话，先创建主表，再创建从表
  4. 删表时，先删从表(或先删除外键约束)，再删主表
  5. 当主表的记录被从表参照时，主表的记录将不允许删除，如果要删除数据，需要先删除从表中依赖该记录的数据，然后才可以删除主表的数据
  6. 在“从表”中指定外键约束，并且一个表可以建立多个外键约束
  7. 从表的外键与主表被参照的列名称可以不相同，但是数据类型必须一样，逻辑意义一致。如果类型不一样，创建子表时，就会出现报错
  8. 当创建外键约束时，系统默认会在所在的列上建立对应的普通索引。但是索引名是列名，不是外键的约束名（根据外键查询效率很高）
  9. 删除外键约束后，必须手动删除对应的索引

- 添加外键约束
  - 在CREATE TABLE时添加
  ```sql
  -- 主表和从表；父表和子表
  -- 先创建主表
  CREATE TABLE dept1(
    dept_id INT,
    dept_name VARCHAR(15)
  );

  -- 再创建从表
  CREATE TABLE emp1(
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(15),
    department_id INT,

    -- 表级约束
    CONSTRAINT fk_emp1_dept_id FOREIGN kEY (department_id) REFERENCES dept1(dept_id)
  )
  -- 上述操作报错，因为主表中的dept_id上没有主键约束或唯一性约束
  添加
  ALTER TABLE dept1
  ADD PRIMARY KEY(dept_id);

  -- 重新创建从表
  CREATE TABLE emp1(
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(15),
    department_id INT,

    -- 表级约束
    CONSTRAINT fk_emp1_dept_id FOREIGN kEY (department_id) 
    REFERENCES dept1(dept_id)
  )
  ```
  - 演示外键效果
  ```sql
  INSERT INTO emp1
  VALUES (1001,'TOM',10);
  -- 出现报错
  -- 因为主表中的department_id还没有数据，因此从表添加失败

  INSERT INTO dept1
  VALUES(10,'IT');
  INSERT INTO emp1
  VALUES(1001,'TOM',10);

  -- 删除失败
  DELETE FROM dept1
  WHERE dept_id = 10;

  -- 更新失败
  UPDATE dept1
  SET dept_id = 20
  WHERE dept_id = 10;

  -- 在从表的外键数据还在使用主表的数据时，主表的数据不能删除或更新，否则报错
  ```
  - ALTER TABLE时添加外键约束
  ```sql
  CREATE TABLE dept2(
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(15)
  );

  ALTER TABLE emp2
  ADD CONSTRAINT fk_emp2_dept_id FOREIGN KEY(department_id)
  REFERENCES dept2(dept_id);
  ```

- 约束等级
  - <font color=tomato>Cascade方式</font>：在父表上update/delete记录时，同步update/delete掉子表的匹配记录
  - <font color=tomato>Set null方式</font>：在父表上update/delete记录时，将子表上匹配记录的列设为null，但要注意子表的外键列表不能为NOT NULL
  - <font color=tomato>No action方式</font>：如果子表中有匹配的记录，则不允许对父表对应候选键进行udpate/delete操作
  - <font color=tomato>Restrict方式</font>：同no action，都是立即检查外键约束
  - <font color=tomato> Set default方式</font>：（在可视化工具SQLyog中可能显示空白）：父表有变更时，子表将外键设置成一个默认的值，但Innodb不能识别
  - 如果没有指定等级，就相当于Restrict方式
  - 对于外键约束，最好是采用：ON UPDATE CASCADE ON DELETE RESTRICT的方式
  - 演示
  ```sql
  CREATE TABLE dept(
    did INT PRIMARY KEY,
    dname VARCHAR(50)
  );

  CREATE TABLE emp(
    eid INT PRIMARY KEY,
    ename VARCHAR(5),
    deptid INT,
    FOREIGN KEY(deptid) REFERENCES dept(did)
    ON UPDATE CASCADE ON DELETE SET NULL -- 添加约束等级
  )
  ```
  - 推荐使用：`ON UPDATE CASCADE ON DELETE RESTRICT`


- 删除外键约束
  - 删除流程
  ```sql
  -- 第一步：先查看约束名和删除外键约束
  SELECT * FROM information_schema.table_constraints
  WHERE table_name = '表名称' -- 查看某个表的约束名

  ALTER TABLE 从表名 DROP FOREIGN KEY 赛健约束名;

  -- 第二步：查看索引名和删除索引，（注意只能手动删除）
  SHOW INDEX FROM 表名称;   -- 查看某个表的索引名
  ALTER TBALE 从表名 DROP INDEX 索引名;
  ```

- 开发场景：
  - 问题1：建和不建外键约束有什么区别？
  ```
  答：
  建外键约束，你的操作（创建表、删除表、添加、修改、删除）会受到限制，从语法层面受到限制。例如：在员工表中不可能添加一个员工信息，它的部门的值在部门表中找不到

  不建外键约束，你的操作（创建表、删除表、添加、修改、删除）不受限制，要保证数据的引用完整性，只能依靠程序员的自觉，或者是在Java程序中进行限定。例如：在员工表中，可以添加一个员工的信息，它的部门指定为一个完全不存在的部门
  ```
  - 问题2：建和不建外键约束和查询有没有关系
  ```
  答：没有
  在MySQL里，外键约束是有成本的，需要消耗系统资源。对于大并发的SQL操作，有可能不适合。比如大型网站的中央数据库，可能会因为外键约束的系统开销而变得非常慢。所以，MySQL允许你不使用系统自带的外键约束，在应用层面完成检查数据一致性的逻辑。也就是说，即使你不用外键约束，也要有办法通过应用层面的附加逻辑，来实现外键约束的功能，确保数据的一致性
  ```

- 阿里开发规范
  - 【强制】不得使用外键与级联，一切外键概念必须在应用层解决
    - 说明：(概念解释)学生表中的student_id是主键，那么成绩表中的student_id则为外键。如果更新学生表中的student_id,同时触发成绩表中的student_id更新，即为级联更新。外键与级联更新更适用于单机低并发，不适合分布式，高并发集群；级联更新是强阻塞，存在数据库更新风暴的风险；外键影响数据库的插入速度

### CHECK约束
- 作用：检查某个字段的值是否符合xxx要求，一般指值的范围

- 关键字：`CHECK`

- 说明：MySQL5.7不支持
  - MySQL5.7可以使用check约束，但check约束对数据验证没有任何作用。添加数据时，没有任何错误和警告
  - <font color=tomato>但是MySQL8.0中可以使用check约束了</font>
  ```sql
  CREATE TABLE employee(
    eid INT PRIMARY KEY,
    ename VARCHAR(5),
    gender CHAR CHECK(gender = '男' OR gender = '女')
  );
  -- check后面的选值必须落实到具体的字段

  CREATE TABLE test10(
    id INT,
    last_name VARCHAR(15),
    salary DECIMAL(10,2) CHECK(salary > 2000)
  );
  ```

- 如果要修改或删除检查约束所约束的字段时，需要先修改或删除检查约束

- 删除检查约束
```sql
ALTER TABLE table_name DROP CONSTRAINT constraint_name;
```

- 查看检查约束名constraint_name
```sql
SHOW CREATE TABLE table_name;
```

- 修改检查约束
```sql
ALTER TABLE table_name DROP CONSTRAINT constraint_name;
ALTER TABLE table_name ADD CONSTRAINT new_constraint_name CHECK (condition);
```

### DEFAULT约束
- 作用：给某个字段/某列指定默认值，一旦设置默认值，在插入数据时，如果此字段没有显示赋值，则赋值为默认值

- 关键字：`DEFAULT`

- 给字段加默认值
  - CREATE TABLE时添加约束
  ```sql
  CREATE TABLE test11(
    id INT,
    last_name VARCHAR(15),
    salary DECIMAL(10,2) DEFAULT 2000
  );
  ```
  - ALTER TABLE时添加约束
  ```sql
  ALTER TABLE test
  MODIFY salary DECIMAL(10,2) DEFAULT 2500;
  ```

- 删除默认值约束
```sql
ALTER TABLE test
MODIFY salary DECIMAL(10,2);
-- 不加DEFAULT，表示删除默认值 
```
