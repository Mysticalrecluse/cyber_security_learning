# XML技术
## XML简介
- XML(eXtensible Markup Language, 可扩展标记语言)可以定义自己的一组标签
- 基于文本格式，所以XML可以跨平台，跨语言
- 标签没有预定义，需要自定义
- XML用来保存和传输数据，不是用来显示数据的（HTML用来显示数据）
- XML是元语言（可以通过此语言创造其他语言的语言称为元语言）

## XML文档结构
```xml
<!-- 放这里是错误的，注释不能放在声明之前 -->
<?xml version="1.0" encoding="utf-8"?>  <!-- xml声明 -->
<!-- 包括版本和字符编码，版本默认1.0 -->

<class>
    <stu>
        <name>李白</name>
        <sex>男</sex>
        <url>
            <a href="www.php.com">我的个人主页</a>
        </url>
    </stu>

</class>

```
- XML文档必须包含根元素
- XML节点的分类
  - 文档节点（相当于JS中的document）
  - 元素节点
  - 属性节点
  - 值节点
  - 注释节点

- 数据的分类
  - PCDATA(parse character data) 可解析字符数据
    - 有解析器解析 
    - 默认采用PCDATA
  - CDATA(character data) 不解析字符数据
    - 不会有解析器解析
    ```xml
    <url>
        <![CDATA[
            <a href="www.php.com">我的个人主页</a>
        ]]>
    </url>
    ```
  - 总结：
    - 元素后一般是PCDATA
    - 属性后一般是CDATA


## 创建XML文档规则
- 至少需要一个元素
- XML标签区分大小写（HTML不区分大小写）
- 必须是容器标记，不允许空标记的存在
- 标记的嵌套必须正确
- 合法的标签：字母、下划线、冒号开头，后面在字母、数字、下划线、冒号、句号、连字符。
- 标签长度取决于CPU的处理能力

## 注释
- 语法：`<!-- -->`
- 注释不能放在XML声明之前
- 注释不能嵌套

## 格式良好和有效
- 文档满足最低规范（保存不报错）被视为格式良好的XML文档
- 如果文档格式不良好，此文档不能被解析
- 有效：满足约束的要求称为有效
- 通过DTD验证XML文档是否有效

### DTD
- 概述：
  - DTD(document type definition) 文档类型定义
  - DTD可以是一个独立的文件，也可以是嵌套在XML文档中

- 作用：
  - DTD用来验证XML文档是否有效

#### DTD结构
- 声明混合内容
```xml
<!ELEMENT note (to+,from,header,message*,#PCDATA)>
```
- 序列
  - `<!ELEMENT A(B)>` 表示A元素下有一个B元素
  - `<!ELEMENT A(B,C)>` 表示A元素下有B和C元素
  - `<!ELEMENT A(B,(C|D),E)>` 表示A元素下有B,C,E或者B,D,E元素
- 选择子元素和/或子组
  - `<!ELEMENT A(B|C)>` 表示A元素下有B元素或C元素
  - `<!ELEMENT A(B|C|(D,E))>` 表示A元素下有B元素或C元素或D，E元素


#### 元素声明
- 语法：
```xml
<!DOCTYPE 根元素名 [
    <!ELEMENT 元素 (子元素)>
    <!ELEMENT 元素 (#PCDATA)>
    <!ELEMENT 元素 EMPTY> 
    <!ELEMENT 元素 ANY>
]>
<!-- 空标记，例如<br/> -->
<!-- EMPTY：用来声明空标记 -->
<!-- ANY：表示此元素下可以任意摆放已经定义的元素 -->
```

- 当标签内既有数据，又有子元素，如何定义DTD
  - 示例：
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <!DOCTYPE html[
    <!ELEMENT html (body)>
    <!ELEMENT strong (#PCDATA)>
    <!ELEMENT body (#PCDATA | strong)*> <!-- 混合元素，必须加*号 -->
  ]>

  <html>
    <body>
        锄禾日当午，<strong>汗滴禾下土</strong>
    </body>
  </html>
  ```

- 元素的声明
  - 量词：（和正则表达式相同）
    - `+`  描述：大于等于1个
    - `*`  描述：大于等于0个
    - `?`  描述：等于1或等于0


- 引用外部DTD
  - 引用外部DTD的两个关键字
    - SYSTEM:`<!DOCTYPE movies SYSTEM "1-demo.dtd">`
      - 引用自定义的dtd
    - PUBLIC：引用互联网上公开的dtd
    ```xml
    <!DOCTYPE html PUBLIC "-//w3c//DTD XHTML 1.0 Transitional //EN"
    "http://www.w3.org/TR/xhmtl1/DTD/xhtml1-transtional.dtd">
    ```

- 示例：写出如下XML的DTD
```xml
<?xml version="1.0" encoding="utf-8"?> 
<!DOCTYPE movies SYSTEM "1-demo.dtd"> <!-- 引用外部DTD -->
<movies>
    <movie id="001" type="冒险片">
        <title>空中监狱</title>
        <actor>尼古拉斯 凯奇</actor>
        <rating>家长指引</rating>
    </movie>
    <movie id="002" type="恐怖片">
        <title>幽灵</title>
        <actor>黛米 摩尔</actor>
        <actor>帕特里克 斯威兹</actor>
        <rating>家长指引</rating>
    </movie>
</movies>
```
```xml
<?xml version="1.0" encoding="utf-8"?> 
<!ELEMENT movies (movie+)>
<!ELEMENT movie (title,actor+,rating)>
<!ELEMENT title (#PCDATA)> <!-- ELEMENT后面只能跟PCDATA，不能接CDATA -->
<!ELEMENT actor (#PCDATA)>
<!ELEMENT rating (#PCDATA)>
```
- 总结：
  - 第一步：新建DTD文件
  - 第二步：按照XML格式显示DTD
  - 第三步：新建XML文档，并引入DTD验证
  ```xml
  <!DOCTYPE movies SYSTEM "1-demo.dtd"> <!-- 引用外部DTD -->
  ```
  - 第四步：根据DTD的约束，书写XML

- 内部写入DTD
```xml
<?xml version="1.0" encoding="utf-8"?> 
<!DOCTYPE movies[
    <!ELEMENT movies (movie+)>
    <!ELEMENT movie (title,actor+,rating)>
    <!ELEMENT title (#PCDATA)>
    <!ELEMENT actor (#PCDATA)>
    <!ELEMENT rating (#PCDATA)>
]>
<movies>
    <movie id="001" type="冒险片">
        <title>空中监狱</title>
        <actor>尼古拉斯 凯奇</actor>
        <rating>家长指引</rating>
    </movie>
    <movie id="002" type="恐怖片">
        <title>幽灵</title>
        <actor>黛米 摩尔</actor>
        <actor>帕特里克 斯威兹</actor>
        <rating>家长指引</rating>
    </movie>
</movies>
```
#### 属性声明
- 语法：`<!ATTLIST 元素名 属性名 [数据类型] 约束>`

- 关键字
  - REQUIRED  必填
    - 示例：`<!ATTLIST 元素名 属性名 CDATA #REQUIRED>`
  - IMPLIED  选填
    - 示例：`<!ATTLIST 元素名 属性名 CDATA #IMPLIED>`
  - DEFAULT 默认值
    - 示例：`<!ATTLIST 元素名 属性名 CDATA "默认值">`
  - FIXED 固定值
    - 示例：`!ATTLIST 元素名 属性名 CDATA #FIXED '固定值'`
  - ENUM 枚举
    - 示例：`!ATTLIST 元素名 属性名 (枚举1|枚举2|...)'默认枚举'`
  - ID 唯一
    - 示例：`!ATTLIST 元素名 属性名 ID#REQUIRED`

- 示例：
```xml
<!DOCTYPE books SYSTEM "demo.dtd">
<books>
    <book id="B001" medium="纸质" type="计算机" pub="北京出版色" pagesize="300">
        <name>XML</name>
    </book>
</books>
```
```xml
<!ELEMENT books (book+)>
<!ELEMENT book (name)>
<!ELEMENT name (#PCDATA)>
<!ATTLIST book id ID #REQUIRED>
<!ATTLIST book medium CDATA #FIXED "纸质">
<!ATTLIST book type CDATA "计算机">
<!ATTLIST book pub (北京出版色|上海出版社|新华出版社) "新华出版社">
<!ATTLIST book pagesize CDATA #IMPLIED>
```

#### 实体
- 概述：
  - 实体是XML的存储单元

- 分类：
  - 一般实体(类似于常量)
    - 预定义实体
    - 自定义实体
  - 参数实体(类似于变量)

- 预定义实体
<table>
    <thead>
        <th style="background-color:darkred;color:white;">实体名称</th>
        <th style="background-color:darkred;color:white;">单词</th>
        <th style="background-color:darkred;color:white;">中文</th>
        <th style="background-color:darkred;color:white;">字符</th>
    </thead>
    <tbody>
        <tr>
            <td>lt</td>
            <td>less than</td>
            <td>小于</td>
            <td><</td>
        </tr>
        <tr>
            <td>gt</td>
            <td>greater than</td>
            <td>大于</td>
            <td>></td>
        </tr>
        <tr>
            <td>amp</td>
            <td>ampersand</td>
            <td>&记号的名称</td>
            <td>&</td>
        </tr>
        <tr>
            <td>quot</td>
            <td>quotation</td>
            <td>引号</td>
            <td>""</td>
        </tr>
        <tr>
            <td>apos</td>
            <td>apostrophe</td>
            <td>单引号</td>
            <td>''</td>
        </tr>
    </tbody>
</table>

- 示例：
```xml
<?xml version="1.0" encoding="utf-8"?> 
<item value="&quot;他说：&apos;1&lt;2&apos;&quot;"></item>
```

- 自定义实体
  - 语法：`<!ENTITY 实体名 实体值>`
  - 调用实体
    - 语法：`&实体名;`
  - 元素，属性，实体的综合练习：
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <!DOCTYPE book SYSTEM "demo.dtd"[
    <!ENTITY bj "北京大学出版社">
    <!ENTITY qh "清华大学出版社">
  ]> 
  <book>
    <detail id="B001">
        <name>道教的起源</name>
        <author>正清小子</author>
        <publication>&bj;</publication>
        <price>25</price>
        <url>
            <![CDATA[
                <a href="book1.php">连接地址</a>
            ]]>
        </url>
        <content>&book1;</content>
    </detail>
    <detail id="B002">
        <name>佛教的起源</name>
        <author>达摩祖师</author>
        <publication>&qh;</publication>
        <price>32</price>
        <url>
            <![CDATA[
                <a href="book2.php">连接地址</a>
            ]]>
        </url>
        <content>&book2;</content>
    </detail>
  </book>
  ```
  - 注意新版本自定义实体不能写外面，写在外部无法加载
  - 内部可以引用
  - DTD文档
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <!ELEMENT book (detail+)>
  <!ELEMENT detail (name,author,publication,price,url,content)>
  <!ELEMENT name (#PCDATA)>
  <!ELEMENT author (#PCDATA)>
  <!ELEMENT publication (#PCDATA)>
  <!ELEMENT price (#PCDATA)>
  <!ELEMENT url (#PCDATA)>
  <!ELEMENT content (#PCDATA)>
  <!ATTLIST detail id ID #REQUIRED>
  <!ENTITY bj "北京大学出版社">  <!-- 外部引用不生效 -->
  <!ENTITY qh "清华大学出版色" >
  ```

- 参数实体 
  - 概述：参数实体和一般实体声明的时候很相似，区别是参数实体前面有"%"
  - 语法：`<!ENTITY % 实体名 '实体默认值'>` 
  - 参数实体可以写在外部，外部可以加载参数实体
  - 示例
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <!-- 使用参数实体 -->
  <!DOCTYPE roster SYSTEM "demo.dtd"[
    <!ENTITY % p "teacher">
  ]>

  <roster>
    <teacher id="t001">
        <name>张老师</name>
        <sex>女</sex>
        <birthday>1977.8.2</birthday>
        <skill>ASP</skill>
        <skill>PHP</skill>
    </teacher>
    <teacher id="t002">
        <name>李老师</name>
        <sex>男</sex>
        <birthday>1976.5.11</birthday>
        <skill>NET</skill>
        <skill>Oracle</skill>
    </teacher>
  </roster>
  ```
  
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <!DOCTYPE roster SYSTEM "demo.dtd"[
    <!ENTITY % p "student">
  ]>
  <roster>
    <student id="s001">
        <name>张前景</name>
        <sex>男</sex>
        <birthday>1999.2.13</birthday>
        <score>78</score>
        <skill>JavaScript</skill>
    </student>
    <student id="s002">
        <name>李盈莹</name>
        <sex>女</sex>
        <birthday>1989.12.16</birthday>
        <score>88</score>
        <skill>C#</skill>
    </student>
  </roster>
  ```
  - 分析：这两个XML文档有相同的结构，只是`<roster>`下元素名不一样，我们可以将`<student>`和`<teacher>`用参数实体代替
  - DTD示例
  ```xml
  <!ENTITY % p 'test'>
  <!ELEMENT roster (%p;)+>
  <!ELEMENT %p; (name,sex,birthday,score?,skill+)>
  <!ELEMENT name (#PCDATA)>
  <!ELEMENT sex (#PCDATA)>
  <!ELEMENT birthday (#PCDATA)>
  <!ELEMENT score (#PCDATA)>
  <!ELEMENT skill (#PCDATA)>
  <!ATTLIST %p; id ID #REQUIRED>
  ```

#### 命名空间
- 作用：用来修饰限定元素，命名空间不能重复
- 示例
```xml
<?xml version="1.0" encoding="utf-8"?>
<sample xmlns:study='http://www.aa.com' xmlns:tea='http://www.bb.com'>
    <study:batch-list>
        <study:batch>第一批PHP培训</study:batch>
        <study:batch>第二批PHP培训</study:batch>
    </study:batch-list>
    <tea:batch-list>
        <tea:batch>第一批茶叶</tea:batch>
        <tea:batch>第二批茶叶</tea:batch>
    </tea:batch-list>
</sample>
```
- DTD缺点：
  - 只要带命名空间的XML，DTD无法写
  - DTD不可扩展

- DTD优点：
  - 很简洁的验证XML文档

### Schema（模式）
- 优点：
  - 是XML语法编写的
  - 支持命名空间
  - 支持很多数据类型（整型，浮点型，日期等等）
  - 可扩展

- 缺点：
  - 繁琐，没有DTD简洁