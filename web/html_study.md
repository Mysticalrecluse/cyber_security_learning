# HTML5基础
## 基础框架
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
</html>
```
## 基础框架组成
- 文档类型声明
- &lt;html&gt;&lt;/html&gt;
- &lt;head&gt;&lt;/head&gt;
- &lt;body&gt;&lt;/body&gt;

## 文档类型声明
```html
<!DOCTYPE HTML> 
<!--文档类型声明，默认触发浏览器标准模式-->
```

## html标签
```html
<html lang='en'></html>
<!-- langs属性的作用是告诉浏览器当前页面的语言类型，这里的“en”表示【英文模式】
中文模式是”zh-CN“，如果你的浏览器的默认语言模式跟你的设置不一样，会弹出窗口，询问是否翻译 -->
```

## head头部结构 
### 网页标题
```html
<head>
<title>网页标题</title>
</head>
```
### 网页元信息
- 针对搜索引擎检索
    ```html
    <head>
        <meta name="description" content="描述内容"> <!--定义网页的描述信息-->
        <meta name="keywords" content="关键词1，关键词2，关键词3...">  <!--定义网页的关键词-->
    </head>
    ```
- 其他补充信息
    ```html
    <head>
        <meta name="author" content="网页作者">  <!--设置网页作者-->
        <meta name="copyright" content="网页版权">  <!--设置网页版权-->
        <meta name="date" content="2019-01-12T20:50:30+00:00">  <!--设置创建时间-->
        <!--
            遵循 ISO 8601 标准的日期和时间表示方法
            2019-01-12：表示日期
            T：是日期与时间之间的分隔符
            20:50:30：表示时间
            +00:00：这是时间的时区偏移。它表示这个时间与协调世界时（UTC）相差 0 小时 0 分钟。所以这个时间就是 UTC 时间。

        -->
        <meta name="robots" content="none">  <!--设置禁止搜索引擎检索-->
    </head>
    ```
- 字符编码
    ```html
    <head>
        <meta charset="utf-8">
    </head>
    ```
- 定义文档视口(解决移动web的视口问题)
    ```html
    <head>
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <!--
            width=device-width将layout viewport(布局视口)的宽度设置ideal viewport（理想视口）的宽度
            initial-scale=1表示将layout viewport(布局视口)的宽度设置ideal viewport（理想视口）的宽度
        -->
    </head>
    ```
- <small>注意：像刷新或者缓存策略等功能，现在更多的是在web框架或者ajax中实现。网页元信息更多的是针对于搜索引擎优化</small>
  
## body主体结构
### 通用属性
- id
  - 功能：
    - 文档结构大部分使用&lt;div&gt;标签来完成，为了能够识别不同的结构，一般通过定义id或class赋予它们额外的语义
    - 给css样式提供有效的“钩子”
  - 特性；
    - id名必须是唯一的。
    - id名应该用于语义相似的元素以避免混淆。
- class
  - 功能于id相同
  - 特性
    - class可以用于页面上任意数量的元素，因此class非常适合标识样式相同的对象。
    - id和class的名称一定要保持语义性，并与表现方式无关。
- title
  - 可以为文档中任何部分加提示标签。如果将鼠标指针指向加了说明标签的元素时，就会显示title。
### HTML注释
```html
<!--  注释内容  -->
```
### 语义化结构
- 定义页眉header
    ```html
    <header role="banner"> <!--页面级页眉-->
        <nav role="navigation"><!--导航-->
            <ul>
                <li>导航内容</li>
                <li>导航内容</li>
                <li>导航内容</li>
                <li>导航内容</li>
            </ul>
        </nav>
    </header>
    <!--
        role="banner"(可选)
        并不适用于所有的页眉。他明确定义该页眉为页面级页眉，因此可以提高访问权重。
        header也适合对页面深处的一组介绍性或导航性内容进行标记。例如；一个区块的目录
    -->
    ```

- 定义导航nav
  - 一般习惯使用ul或ol元素对链接进行结构化。
  - 一般应该将网站全局导航标记为nav,让用户可以跳至网站各个主要部分的导航。这种nav通常出现在页面级的header元素里面。

- 定义主要区域main
  ```html
  <header>
    <nav role="navigation">包含多个链接的ul</nav>
  </header>
  <main role="main">
    <article>
        <h1 id="gaudi"></h1>
        <p>页面主要区域其他内容</p>
    </article>
  </main>
  <aside role="complementary">
    <h1>侧边标题</h1>
    <p>附注栏的其他内容</p>
  </aside>
  <footer role="info">[版权]</footer>
  ```
  - 在main开始标签中加上role="main",可以帮助屏幕阅读器定位页面上的主要区域
  - 一个页面只有一个部分代表其主要内容，该元素在一个页面仅使用一次

- 定义文章块article
  - 在html5中，article元素表示文档，页面，应用或网站中一个独立的容器，原则上是可独立分配或可再用的，就像聚合内容的各个部分。

- 定义区块section
    ```html
    <main role="main">
        <h1>主要标题</h1>
        <section>
            <h2>区块标题</h2>
            <ul>标题列表</ul>
        </section>
        <section>
            <h2>区块标题</h2>
            <ul>标题列表</ul>
        </section>
        <section>
            <h2>区块标题</h2>
            <ul>标题列表</ul>
        </section>
    </main>
    ```
    - section是具有相似主题的一组内容
    - section定义通用区块，但不要将它和div混淆。从语义上讲，section标记的是页面中的特定区域，而div则不传达任何语义。

- 定义流内容
    ```html
    <figure>
    <img src="path-to-image.jpg" alt="Description of image">
    <figcaption>This is an image of something interesting.</figcaption>
    </figure>
    ```
    - `<figure>`用于标识内容，这些内容可以单独地引用或引入文档的其他部分；流内容是由页面上的文本引述出来的
    - `<figcaption>`元素用于提供对 `<figure>` 的简短描述。

- 定义附栏aside
    ```html
    <header role="banner">
        <nav role="navigation">包含多个链接</nav>
    </header>
    <main role="main">
        <article>
            <h1></h1>
        </article>
    </main>
    <aside role="complementary"> <!--complementary意思是补充性内容-->
        <h1>次要标题</h1>
    </aside>
    <footer role="contentinfo">
        <p><small>版权信息</small></p>
    </footer>
    ```
    - 附栏内容aside放在main的内容之后。出于搜索引擎优化SEC和可访问性的目的，最好将重要的内容放在前面。可以通过CSS改变它们在浏览器中的显示位置。

- 定义页脚footer
  - 只能对页面级页脚使用role="contentinfo"
### 文本编辑
- 标题文本
    ```html
   <h1></h1> ~ <h6></h6> <!--重点是语义，不是样式-->
    ```
- 段落文本
    ```html
   <p> 文本内容 </p> <!--无视回车和空格，统一按一个空格处理-->
    ```
- 预定义文本
    ```html
    <pre>
		  静夜思
	    作者：李白
    床前明月光，疑是地上霜
    举头望明月，低头思故乡
    </pre>
    <!--在html中可以使用<pre>预定义标签来保留写的格式，
        原封不动的展示文字（会保留空格）-->
    ```
- 文本格式化
  
    <table border="1">
        <thead>
            <th>标签功能</th>
            <th>关键字单词</th>
        </thead>
        <tbody>
            <tr>
                <td>粗体显示</td>
                <td>Strong(表重要程度)、b</td>               
            </tr>
            <tr>
                <td>斜体显示</td>
                <td>em(推荐，表强调)、i</td>               
            </tr>
            <tr>
                <td>删除线显示</td>
                <td>del</td>               
            </tr>
            <tr>
                <td>下划线显示</td>
                <td>ins</td>               
            </tr>
            <tr>
                <td>上标</td>
                <td>sup</td>               
            </tr>
            <tr>
                <td>下标</td>
                <td>sub</td>               
            </tr>
            <tr>
                <td>小字号显示</td>
                <td>small</td>               
            </tr>
            <tr>
                <td>文本引用</td>
                <td>q</td>               
            </tr>
        </tbody>
    </table>

- <span id="zhuanyi">转义文本</span>

    <table border="1">
        <thead>
            <th>字符</th>
            <th>转义字符</th>
        </thead>
        <tbody>
            <tr>
                <td>"</td>
                <td>& quot ;</td>               
            </tr>
            <tr>
                <td>&</td>
                <td>& amp ;</td>               
            </tr>
            <tr>
                <td><</td>
                <td>& lt ;</td>               
            </tr>
            <tr>
                <td>></td>
                <td>& gt ;</td>               
            </tr>
            <tr>
                <td>空格</td>
                <td>& nbsp ;</td>               
            </tr>
            <tr>
                <td>全角空格</td>
                <td>& emsp ;</td>               
            </tr>
            <tr>
                <td>&copy</td>
                <td>& copy ;</td>               
            </tr>
            <tr>
                <td>￥</td>
                <td>& yen ;</td>               
            </tr>
            <tr>
                <td>&trade;商标</td>
                <td>& trade ;</td>               
            </tr>
            <tr>
                <td>平方</td>
                <td>& sup2 ;</td>               
            </tr>
            <tr>
                <td>立方</td>
                <td>& sup3 ;</td>               
            </tr>
        </tbody>
    </table>
- 换行显示
    ```html
    <br>
    ```
- 文本解释
    ```html
    <abbr title="解释说明">内容</abbr>
    ```
- 修饰文本
    ```html
    <span></span>
    ```
### 图像和多媒体
#### 非响应式图像
- 图像—客户端图像映射应用示例（非响应式）
  
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Client-side Image Map Example</title>
    </head>
    <body>

    <img src="example-image.jpg" alt="Example Map" usemap="#examplemap">

    <map name="examplemap">
        <area shape="rect" coords="10,10,100,100" href="link1.html" alt="Link 1" title="Link 1">
        <area shape="circle" coords="200,200,50" href="link2.html" alt="Link 2" title="Link 2">
        <area shape="poly" coords="400,10,500,10,450,100" href="link3.html" alt="Link 3" title="Link 3">
    </map>

    </body>
    </html>

    ```
    - 图像：img标签
    ```html
    <img src="URL" alt="图像描述">
    ```
      - src：指向显示图像的URL
      - alt：设置图像的替代文本
      - ismap：服务器端图像映射（基本已过时，不建议使用）
      - usemap：客户端图像映射，此属性的值应该与你想要引用的<map>标签的name属性相匹配。注意，它前面有一个#符号。
    - 映射：map标签
    ```html
    <map name="">
        <area>
        <area>
        <area>
    </map>
    ```
      - name：定义了此映射的名字，用来匹配对应的图片
    - 点击区域：area标签
    ```html
    <area shape="" coords="" href="" alt=""> 
    ```
      - shape：定义了点击区域的形状
        - rect：矩形
        - circle：圆形
        - poly：多边形
      - coords：定义了形状的坐标
        - 对于矩形，这是左上角和右下角的坐标：x1,y1,x2,y2。
        - 对于圆形，这是圆心和半径的坐标：x,y,r。
        - 对于多边形，这是每个顶点的坐标：x1,y1,x2,y2,...。
      - href：指向链接的目标
      - alt：设置替代文本

#### 响应式图像
##### 方法一：使用picture标签
- picture使用示例
    ```html
    <picture>
        <source media="(min-width:650px)" srcset="url01链接">
        <source media="(min-width:465px)" srcset="url02链接">
        <!--img标签用于不支持picture元素的浏览器-->
        <img src="url" alt="替代文本" id="">
    </picture>
    ```
    - `<picture>`标签仅作为容器，可以包含多个`<srouce>`子标签；建议在`<picture>`标签尾部添加`<img>`标签，用来兼容不支持`<picture>`标签的浏览器
    - `<srouce>`可以加载多个媒体源
      - srcset：必须，设置图片文件路径或逗号分隔的用像素密度描述的图片路径
    `srcset="img/minpic.png,img/maxpic.png 2x"`
      - media：设置媒体查询 
      - type：设置MIME类型。
      - 浏览器将根据`<srouce>`的列表顺序，使用第一个合适的`<srouce>`元素，并根据这些设置属性，加载具体的图片源，同时忽略后面的`<srouce>`标签
    ```html
    <!--横屏与竖屏显示-->
    <source media="(orientation:portrait)" srcset="images/kitten-medium.png"> <!--竖屏显示-->
    <source media="(orientation:landscape)" srcset="images/kitten-large.png"> <!--横屏显示-->

    <!--根据分辨率不同显示-->
    <source media="(min-width:320px)and(max-width:640px)" srcset="images/minpic_retina.png 2x">
    <source media="(min-width:640px)" srcset="img/middle.png,img/middle_retina.png 2x">  <!--同时判定视口大小和分辨率-->

    <!--根据格式不同显示-->
    <source type="image/webp" srcset="images/picture.webp">
    <img src="images/piture.png" alt="this is a picture">
    ```
##### 方法二：使用img的srcset属性
- 在响应式图像的上下文中，HTML5 提供了一种方法，使开发者能够提供多个图像源，以便浏览器可以根据设备和环境条件选择最合适的图像。这是通过 <img> 元素的 srcset 属性实现的。在 srcset 属性中，我们可以使用两种描述符：x 描述符和 w 描述符。
  - x 描述符：像素比 (Pixel Density Descriptor)
    - 含义：x 描述符用于定义图像的像素比。这与设备的物理像素和逻辑像素之间的关系有关。例如，一个像素比为2的设备会在同样的屏幕空间内拥有双倍的物理像素。
    - 使用场景：当你知道你要为不同的屏幕像素密度提供不同的图像时。
  - w 描述符：图像的像素宽度 (Width Descriptor)
    - 含义： w 描述符表示图像的自然宽度，单位是像素。这使得浏览器可以计算图像的大小，并选择一个与视口和设备像素密度最匹配的图像。
    - 使用场景：当你希望根据设备的宽度和视口的大小提供不同的图像时。
  ```html
  <!--自适应性价比-->
  <img width="500" srcset="
        images/2500.png 5x,
        images/1500.png 3x,
        images/1000.png 2x,
        images/500.png 1x"
    src="images/500.png"
  >

  <!--自适应视图宽-->
  <img width="500" srcset="
        images/2000.png 2000w,
        images/1500.png 1500w,
        images/1000.png 1000w,
        images/500.png 500w"

    size="
        (max-width:500px) 500px,
        (max-width:1000px) 1000px,
        (max-width:1500px) 1500px,
        2000px"
    
    src="images/500.png"
  >

  <!--使用百分比来设置视口宽度-->
  <img width="500" srcset="
        images/2000.png 2000w,
        images/1500.png 1500w,
        images/1000.png 1000w,
        images/500.png 500w"

    size="
        (max-width:500px) 100vm,
        (max-width:1000px) 80vm,
        (max-width:1500px) 50vm,
        2000px"
    
    src="images/500.png"
  >
  ```

#### 音频
```html
<audio src="音频的URL"> </audio>
```
- 常见属性：
  - controls：显示音频控制面板
  - loop：循环播放
  - autoplay： 自动播放（为提升用户体验，浏览器一般会禁用自动播放功能）
#### 视频
```html
<video src="视频的URL"> </video>
```
- 常见属性
  - controls：显示音频控制面板
  - loop：循环播放
  - autoplay：自动播放（为提升用户体验，浏览器一般会禁用自动播放功能，但是视频中，添加了muted静音播放，浏览器就会允许自动播放）
  - muted：自动播放
### 超链接
```html
<!--普通链接-->
<a href="" rel="" target="">链接内容</a>
```
- 常见属性：
  - href：链接指向的页面url
  - rel：规定当前文档和被链接文档之间的关系
  - target：规定何处打开链接文档
    - _blank
    - _self
```html
<!--锚点链接-->
<body>
    <p><a href="#p4">查看图片4</a></p>
    <h2>图片1</h2>
    <p><img src="images/1.jpg"></p>
    <h2>图片2</h2>
    <p><img src="images/2.jpg"></p>
    <h2>图片3</h2>
    <p><img src="images/3.jpg"></p>
    <h2 id="p4">图片4</h2>
    <p><img src="images/4.jpg"></p>
    <h2>图片5</h2>
    <p><img src="images/5.jpg"></p>
</body>
```
- id值就是锚定，链接指向id值，前面加#，就是#id
### 列表
#### 无序列表
```html
<ul type="">
    <li></li>
    <li></li>
    <li></li>
</ul>
```
- 无序列表属性（可以在ul列表的开始标签处使用type属性，去设置编号）
  - 实心圆（默认）：disc；
  - 实心方块：square；
  - 空心圆：circle
#### 有序列表
```html
<ol type="">
    <li></li>
    <li></li>
    <li></li>
</ol>
```
- 属性：
  - reversed：定义列表顺序为降序
  - start="number"：定义有序列表起始值
  - type=[1，A，a，i，I]
#### 自定义列表
```html
<dl> <!--标识描述列表-->
	<dt> </dt> <!--标识词条-->
	<dd> </dd> <!--标识解释-->
	<dt> </dt>
	<dd> </dd>
	<dt> </dt>
	<dd> </dd> 
</dl>
```
### 表格
- 在html中，表格标签用`<table>` `</table>`表示
- table内部子标签的结构
  - 页眉：`<thead>` `<th>`(列头，字段名)
  - 主体：`<tbody>` `<tr>`（行数） `<td>`（单元格）
  - 页脚：`<tfoot>` 一般省略
```html
<table>
	<thead>
		<th>id</th>
		<th>name</th>
		<th>sex</th>
	</thead>
	<tbody>
		<tr>
			<td>01</td>
			<td>lucy</td>
			<td>women</td>
		</tr>
		<tr>
			<td>02</td>
			<td>curyy</td>
			<td>men</td>
		</tr>
	</tbody>
</table>
```
- `<table>`的属性
  - border：加边框，border="0"表示无边框（默认无边框）
  - bgcolor：添加表格背景颜色
  - summary：定义表格摘要，该属性值不会显示，但是屏幕阅读器可以利用该属性，也方便机器进行内容检索

- `<tr>`的属性
  - dir属性：设置这一行单元格内容的排列方式
    - 从左到右（默认）：ltr
    - 从右到左：rtl
  - bgcolor属性：设置【这一行】的背景颜色
  - align属性（内容水平方向排列）：left；right；center
- `<td>`的属性
  - bgcolor属性
  - align属性

- 合并单元格
  - 横向合并
    - 设置colspan属性
    - `<td colspan='2'>`表示当前格子在水平方向要占据两个格子的位置
  - 纵向合并
    - 设置rowspan属性
    - `<td rowspan='2'>`表示当前格子在垂直方向要占据两个格子的位置


### 表单
- 表单框架
```html
<h1>表单标题</h1>
<form method="post" action="show-data.php">
    <fieldset>
        <h2 class="hdr-account">字段分组标题</h2>
        ...用户名字段...
    </fieldset>
    <fieldset>
        <h2 class="hdr-address">字段分组标题</h2>
        ...联系地址字段...
    </fieldset>
    <fieldset>
        <h2 class="hdr-pulic-profile">字段分组标题</h2>
        ...公共字段...
        <div class="row">
            <fieldset class="radios">
                <legend>性别：</legend>
                <input type="redio" id="gender-male" name="gender" vaule="male">
                <label for="gender-male">男士</label>
                <input type="redio" id="gender-female" name="gender" vaule="female">
                <label for="gender-female">女士</label>
            </fieldset>
        </div>
    </fieldset>
    <fieldset>
        <h2 class="hdr-emails">电子邮箱</h2>
        ...Email字段...
    </fieldset>
    <input type="submit" value="提交表单" class="btn">
</form>
```
- 结构标签
  - `<form>` `</form>`
    - 每个表单都以`<form>`标签开始，以`</form>`标签结束。两个标签之间是各种标签和控件。
    - 每个控件都有一个name属性，用于提交表单时标识数据。
    - 常用属性：
      - action：值为URL，规定当提交表单时向何处发送表单数据
      - method：值为get或post，规定用于发送数据的HTTP方法
        - 如果使用method="get"方式提交表单，表单中的数据会显示在浏览器的地址栏里。
        - 如果使用method="post",表单中的数据不会显示在浏览器的地址栏里，这样比较安全，而且使用post可以向服务器发送更多的数据。因此，如果需要在数据库中增删改查，就应该选择post方式提交数据。
      - target：设置提交表单之后的显示页面（在何处显示响应）
        - _self属性值（默认）：在当前页面窗口刷新打开
        - _blank属性值：另弹出一个新窗口打开页面
  
  - `<fieldset>` `</fieldset>`
    - 使用`<fieldset>`标签可以组织表单结构，为表单对象进行分组，这样表单会更容易理解。在默认状态下，分组的表单对象外面会显示一个包围框。
  
  - `<legend>` `</legend>`
    - 使用`<legend>`标签可以定义每组的标题，描述每个分组的目的，有时这些描述还可以使用h1~h6标题。默认显示在`<fieldset>`包含框的左上角。


- 表单控件
  - `<input>`
    - 示例：`<input type="text" placeholder="提示信息">`
    - 属性：
      - type:type的值不同，功能不同
      - name：服务器端的脚本使用name获取访问者在填选的值
      - value：预设的值
      - placeholder：占位文本，提示信息
      - required：必填
      - pattern：值为正则表达式，匹配用户输入内容，以便进行验证
    - type属性详解：
      - text：文本框，用于输入单行文本
      - radio：单选按钮
        - name：控件名称；控件分组，同时只能选中一个（单选功能）同一组单选按钮的name属性必须相同
        - checked：默认选中
      - password：密码框
      - checkbox：复选框
        - checked：默认选中
      - file：上传文件
        - multiple属性允许上传多个文件
      - hidden：隐藏字段


  - 下拉菜单
    ```html
    <select>
        <option> </option>
        <option> </option>
        <option> </option>
        <option> </option>
        <option> </option>
    </select>
    ```
    - 标签：`<select>`  `</select>`嵌套 `<option>` `</option>`
      - option是下拉菜单的每一项
      - `<optgroup>` `</optgroup>`：对选择项目进行分组
  
    ```html
    <select name="选择城市">
        <optgroup label="山东省">
        <option value="潍坊">潍坊</option>
        <option value="青岛" selected>青岛</option>
        </optgroup>
        <optgroup label="山西省">
        <option value="太原">太原</option>
        <option value="榆次">榆次</option>
        </optgroup>
    </select>
    ```
    - select常用属性
      - selected：默认选中

  - 文本域
    - 作用：多行输入文本的表单控件
    - `<textarea>默认提示文字</textarea>`

  - `<label>`标签
    - 作用：描述表单字段用途的文本
    - label有一个特殊的属性：for。如果for的值与一个表单字段的id值相同，该label就与该字段显式地关联了
    - 开发经验：一般用label标签绑定文字和表单控件的关系，增大表单控件的点击范围
    - 示例：
    ```html
    <input type="radio" id="man">
    <label for="man">男</label>
    ```

- 按钮：`<button>`
    - 示例：`<button type=" "> 按钮 </button>`
    - type属性值
      - submit：提交按钮，点击后提交数据到后台（默认功能）
      - reset：重置按钮，点击后将表单控件恢复默认值
      - button：普通按钮，默认没有功能，配合js使用

- 按钮2：按钮的第二种方法
  - `<input type=submit>`
  - type属性值和方法一相同


- 如何把表单数据进行提交
  - 表单控件的专用属性（必备）
    - name属性的概念和功能：这个属性是用来提交信息的，也就是如果要将每个控件接收到的数据【传递】到【数据库或服务器】中去保存时，必须要设置这个那么属性，如果不设置name属性，那么控件的数据是不能传到服务器上面去保存的！！！

  