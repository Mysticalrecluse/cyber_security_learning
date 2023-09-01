# JavaScript基础语法
## JS的组成
- ECMAScript（JavaScript语言基础）
- Web APIs
  - DOM 页面文档对象模型
  - BOM 浏览器对象模型

## JS的书写位置（同CSS）
- 行内 Javascript
  - 后面vue框架会用这种模式
- 内部Javascript
  - 规范：script标签写在&lt;/body&gt;上面
  - 扩展：alter('你好，js')页面弹出警告对话框
- 外部JavaScript
  - &lt;script src='./js/my.js'&gt;&lt;/script&gt;
  
## JS的注释
- /* */ 多行注释
- // 单行注释

## 输入输出语法
```javascript
/*输出语法*/
document.write('要出的内容')
document.write('<h1>一级标题</h1>') //允许打印标签
// document.write无自动换行功能
alert('要出的内容') // 弹出窗口，只有确定
confirm('要出得内容') // 弹出对话框，和alert对比多了个取消得选择
console.log('控制台打印') // 程序员调试使用，页面不显示，只显示在控制台

/*输入语法*/
prompt('请输入你的年龄')
```

## 变量
- 变量的声明
  - 创建变量：let 变量名
- 变量的赋值
  - 变量 = 值
```javascript
let age // 声明一个变量
age = 18 //赋值
alert(age)

let age = 18 // 声明的同时直接赋值
let age = 18,uname = 'pink' //一次声明多个变量，用逗号隔开，但是不建议
```
- 变量的引用：
  - 模板字符串
  - 使 用：&#96;${ 所引用变量 }&#96;
  - 模式
```js
var name = 'GeekTime';
var age = '26';

console.log('name:'+ name + ',age:' + age); //传统写法
console.log(`我是${name},age:${age}.`); //ES6写法
```
## 数组（Array）
```javascript
let arr = [1,2,3,4,5]
console.log(arr[0])
console.log(arr.length) //返回数组的长度
```

## 常量
  - 概念：使用const声明的变量称为：“常量”
  - 注意：常量不允许重新赋值，声明的时候必须赋值（初始化）
```javascript
// 声明一个常量
const G = 9.8
console.log(G)
```

## 数据类型
- 分类：基本数据类型；引用数据类型
- 基本数据类型和引用数据类型的区别
  - 基本数据类型：参数赋值的时候，传数值。
  - 引用数据类型；参数赋值的时候，传地址（修改的同一片内存空间）
- 基本数据类型（值类型）
  - number 数字型
    - 算术运算符：+ - * / %
    - 数值范围：由于内存限制，ECMAScript并不能保存世界上所有的数值。
      - 最大值：Number.MAX_VALUE，这个值为：1.7976931348623157e+308
      - 最小值：Number.MIN_VALUE，这个值为：5e-324
    - 如果使用Number表示的变量超过了最大值，则会返回Infinity。
      - 无穷大（正无穷）：Infinity
      - 无穷小（负无穷）：-Infinity
    - 注意：typeof Infinity的返回结果是number

  - string字符串型
    - 模板拼接：反引号在最外围括住，变量则使用${}
    -   ```js 
        let age = 30
        document.write(`我今年他妈的${age}岁了`)

        let name = prompt('input your name:')
        let age = prompt('input your age:')
        document.write(`大噶好，我叫${name}，今年${age}岁了`)
        ```
    - 模板字符串支持嵌套使用
        ```js
        const nameList = ['极客时间','渗透测试','网络安全']；

        function myTemplate(){
          //join('')的意思是，把数组里的内容合并成一个字符串
          return `<ul>
          ${nameList
            .map((item) => `<li>${item}</li>`)
            .join('')}
          </ul>`;
        }
        document.body.innerHTML = myTemplate();
        ```

  - boolean 布尔型
    - true | false
  - undefined 未定义类型
    - 只有一个值：undefined
    - 只声明变量，不赋值的情况下，默认变量为undefined
    - 工作场景：
      - 开发过程中，经常声明一个变量，等待传送过来的数据。<br>如果我们不知道这个数据是否传递过来，此时我们可以通过检测这个变量是不是undefined，就判断用户是否有数据传递过来。
  - null 空类型
    -  null和undefined的区别
       -  undefined 表示没有赋值
       -  null 表示赋值了，但是内容为空
    - null 开发中的使用场景
      - 官方解释：把null作为尚未创建的对象
      - 人话：将来有个变量里面存放的是一个<em>对象</em>,但是对象还没创建好，可以先给个null。
- 检测数据类型
  - 作为运算符：typeof X (常用写法)
  - 函数形式：typeof(x)
- 引用数据类型（引用类型）
  - object 对象类型：内置对象Function，Array，Date，RegExp，Error等都是属于Object类型。也就是说，除了那物种基本数据类型之外，其他的，都称之为Object类型。
    - Dirct类型（相当于字典）由键值对组成得无需集合
      - {键名1:值1,键名2:值2,...}
      - 注意：在js中，键一般是字符串，值可以是任意数据类型
      - 取值方式
      ```js
      let a = {'name':'lucy','age':19}
      document.write('g变量中name得值：',g.name,'<br>')
      document.write('g变量中age得值：',g.['age'],'<br>')
      // 对象类型得两种取值方式
      ```
  
## 类型转换
- 隐式转换
  - <span id="sum">加号两边，只要有一侧是字符串，默认都是字符串</span>
  - 2 - '2' 减法自动转换为数字型 = 0，（减，乘，除，都一样）
  - + '123' 单用加号，将数字类得字符串，转换为数字型
- 显式转换
  - 转换为数字型
    - Number(数据)
      - 如果字符串内容里有非数字，转换失败时结果为NaN，即不是一个数字
      - NaN也是number类型的数据，代表非数字
    - +变量
        ```javascript
        let str = '123'
        typeof +str
        // 输出类型为number
        ```
    
    - parseInt（数据）   
        ```javascript
        //只保留整数部分
        console.log(parseInt('12px')) //输出结果为12
        console.log(parseInt('12.94px')) //输出结果为12
        ```
    - parseFloat（数据）
        ```javascript
        //可以保留小数
        console.log(parseFloat('12px')) //输出结果为12
        console.log(parseFloat('12.94px')) //输出结果为12.94
        ```
### <a href='prac/数据转换类型.html'>练习1：计算两数之和</a>
## 运算符
- 算数运算符
- 自增/自减运算符
- 一元运算符
- 逻辑运算符
- 赋值运算符
- 比较运算符
- 三元运算符
  
### 算术运算符
<table>
  <thead>
    <th>
        运算符
    </th>
    <th>
        描述
    </th>
  </thead>
  <tbody>
    <tr>
      <td>
        +
      </td>
      <td>
        加，字符串连接
      </td>
    </tr>
    <tr>
      <td>
        -
      </td>
      <td>
        减
      </td>
    </tr>
    <tr>
      <td>
        *
      </td>
      <td>
        乘
      </td>
    </tr>
    <tr>
      <td>
        /
      </td>
      <td>
        除
      </td>
    </tr>
    <tr>
      <td>
        %
      </td>
      <td>
        获取余数（取余，取模）
      </td>
    </tr>
  </tbody>
</table>
- 注意事项：浮点数运算的精度问题

  - 在JS中，整数中的运算基本可以保证精确，但是小数的运算，可能会得到一个不精确的结果。所以，千万不要使用JS进行对精确度要求比较高的运算。
  
  - 处理方法
  
    - 如果只是一些简单的精度问题，可以使用toFix()方法进行小数的截取。
  
      ```javascript
      number.toFixed([digits])
      ```
      - digits 是一个可选参数，它指定要保留的小数位数。它应该是0到20之间的整数（包含0和20）
      - 遵循四舍五入，而不是单纯的截取
      - 不指定digits时，默认为0，即四舍五入到最近的整数
  
    - 在实际开发中，关于浮点数计算的精度问题，往往比较复杂。市面上有很对针对数学运算的开源库，比如decimal.js、Math.js。这些开源库都比较成熟，我们可以直接拿来用。
      - Math.js：属于很全面的运算库，文本很大，压缩后的文件就有500kb。如果你的项目涉及到大型的复杂运算，可以使用Math.js
      - decimal.js：属于轻量级的运算库，压缩后的文件只有32kb，大多数项目的数月运算，使用decimal.js足够了。
    - 在使用这几个开源库时，既可以用cdn的方式引入，也可以用npm包的方式引入。
    ```html
    <script src="https://cdn.bootcdn.net/ajax/libs/decimal.js/10.2.0/decimal.min.js"></script>
    <script>
      console.log('加法：');
      var a = 0.1;
      var b = 0.2;
      console.log(a + b)
      console.log(new Decimal(a).add(new Decimal(b)).toNumber());

      console.log('减法：');
      var a = 0.1;
      var b = 0.2;
      console.log(a - b)
      console.log(new Decimal(a).sub(new Decimal(b)).toNumber());

      console.log('乘法：');
      var a = 0.1;
      var b = 0.2;
      console.log(a * b)
      console.log(new Decimal(a).mul(new Decimal(b)).toNumber());

      console.log('除法：');
      var a = 0.1;
      var b = 0.2;
      console.log(a / b)
      console.log(new Decimal(a).div(new Decimal(b)).toNumber());

    </script>
    ```

    - 在正常的开发过程中，一般复杂的计算不会在前端进行，而是在后端计算好后，将值传给前端。 
  
### 自增/自减运算符
- 自增分为两种：`a++` 和 `++a`
- 二者区别：
  - `a++`：先用再加
  - `++a`：先加再用
- 自减：`a--` 和 `--a`
- 二者区别：与自增相同

### 一元运算符
- typeof
- <a href="#sum">`+`：详情见隐式转换，点击查看</a>
- `-`：对数字取反

### 逻辑运算符
- 逻辑运算符有3个
  - && 与
  - || 或
  - ! 非

- 非布尔值的与或运算【重要】
  - 之所以重要，是因为在实际开发中，我们经常用这种代码做容错处理或兜底处理（SQL注入中常用）
  - 非布尔值进行与或运算时，会先将其转换为布尔值，然后再运算，但返回结果是原值。比如说：
  ```js
  var result = 5 && 6; // 运算过程：true && true;
  console.log('result：' + result); // 打印结果：6（也就是说最后面的那个值。）
  ```
  - 与运算的返回结果：（以多个非布尔值的运算为例）
    - 如果第一个值为false，则执行第一条语句，并直接返回第一个值；不会再往后执行。
    - 如果第一个值为true，则继续执行第二条语句，并返回第二个值（如果所有的值都为true，则返回的是最后一个值）。
  - 或运算的返回结果：（以多个非布尔值的运算为例）
    - 如果第一个值为true，则执行第一条语句，并直接返回第一个值；不会再往后执行。
    - 如果第一个值为false，则继续执行第二条语句，并返回第二个值（如果所有的值都为false，则返回的是最后一个值）。
  
### 赋值运算
- 可以将符号右侧的值赋值给符号左侧的变量。
  - `=`直接赋值。比如 var a = 5
  - `+=` 。a += 5 等价于 a = a + 5
  - `-=` 。a -= 5 等价于 a = a - 5
  - `*=` 。a *= 5 等价于 a = a * 5
  - `/=` 。a /= 5 等价于 a = a / 5
  - `%=` 。a %= 5 等价于 a = a % 5

- `==` 和 `===`
  - `==`：只判断值，不判断数据类型
  - `===`：既判断值，也判断数据类型
  
### <a href="#sanyuan">三元运算符</a>
- 详情点击标题，跳转至分支语句

## 扩展内容1
- Unicode编码的使用
  - 在字符串中可以使用转义字符输入Unicode编码。格式如下：
  - `\u四位编码`
  - 可以在一定程度上，规避网站对特殊符号的限制

- 事件句柄
  - HTML 4.0 的新特性之一是有能力使 HTML 事件触发浏览器中的动作action），比如当用户点击某个HTML 元素时启动一段 JavaScript。下面是一个属性列表，这些属性可插入 HTML 标签来定义事件动作，相当于是在 HTML 标签中插入了事件句柄，可以接收JS代码并执行。
  - ![Alt text](image/image01.png)

## 语句
### 分支语句
- 分支语句包含
  - if分支语句
  - 三元运算符
  - switch语句

- if语句
  - 语法
  ```js
  if (条件){
      满足条件要执行的代码
  }
  else {
      不满足条件执行的代码
  }
  ```
  - 0和空字符串""都是false
  - 多分枝if语法
  ```js
  if (条件1) {
      代码1
  }else if (条件2) {
      代码2
  }else if (条件3) {
      代码3
  }else{
      代码n
  }
  ```
- <span id="sanyuan">三元运算符</span>
  - 使用场景：是比if双分支更简单的写法，可以使用三元表达式
  - 语法
  ```js
  条件 ? 满足条件执行的代码 : 不满足条件执行的代码
  ```
  - 一般用来取值

- switch语句
  - 作用：利用switch执行满足条件的语句
  - 语法
  ```js
  switch (数据) {
    case 值1:
        代码1
        break
    case 值1:
        代码1
        break
    default:
        代码n
        break
  }
  ```
  - 注意：
    - switch一定要注意，必须是===全等，一定注意数据类型，同时注意break，否则会有穿透效果。
    - switch case语句一般用于等值判断，不适合于区间判断
    - switch case一般需要配合break关键字使用 没有break会造成case穿透
  - 总结switch和if...else...的区别
    - 当分支比较少时，if...else语句执行效率高
    - 当分支比较多时，switch语句执行效率高，而且结构更清晰。

### 循环语句
- while循环
  - 基本语法
  ```js
  while (循环条件) {
      要重复执行的代码(循环体)
  }
  ```
  - while循环三要素：
    - 循环的本质就是以某个变量为起始值，然后不断产生变化量，慢慢靠近终止条件的过程。
  - 示例
  ```js
  let i = 1
  while (i <= 3) {
      document.write('我会循环3次<br>')
      i++
  }
  ```
  - 循环的退出
    - break：退出循环
    - continue：结束本次循环，继续下次循环

- for循环
  - 基本语法
  ```js
  for (变量起始值；终止条件；变量变化量) {
      //循环体
  }
  ```
  - 示例
  ```js
  // 利用for循环输出三句话 月薪过万
  for (let i = 1; i <= 3; i++) {
      document.write('月薪过万')
  }
  ```
  - 遍历数组
  ```js
  let arr = [1,2,3,4,5,6]
  for (let i = 0; i < arr.length; i++) {
      document.write(arr[i]+"<br>")
  }
  ```
  - 退出循环
    - continue 退出本次循环，一般用于排除或者跳过某一个选项的时候，可以使用continue
    - break 退出整个for循环，一般用于结果已经得到，后续的循环不需要的时候可以使用

  - 循环嵌套
  ```js
  for (外部声明记录循环次数的变量； 循环条件；变化量) {
      for (内部声明记录循环次数的变量；循环条件； 变化量) {
          //循环体
      }
  }
  ```
### <a href='prac/九九乘法表.html'>练习2：九九乘法表</a>

## Array详解
- 数组的基本使用
  
  - 声明数组
  ```js
  // 字面量声明数组
  let 数组名 = [数据1, 数组2, ..., 数组n]

  // 使用 new Array 构造函数声明
  let arr = new Array(数据1, 数组2, ..., 数组n)
  ```
- 操作数组
  - 修改数组的值
  ```js
  // 修改
  let arr = ['curry','james','kobi']
  console.log(arr)
  for (let i )

  // 进阶：遍历修改
  let arr = ['curry','james','kobi']
  console.log(arr)
  for (let i = 0; i < arr.length; i++) {
      arr[i] = arr[i] + 'teacher'
  }
  console.log(arr)
  ```

  - 数组中添加新数据
  ```js
  //数组.push()：将一个或多个元素添加到数组的末尾，并返回该数组的新长度（重点）
  arr.push(元素1,元素2,...,元素n)

  // 示例：
  let arr = ['red','green']
  let length = arr.push('pink')
  console.log(arr) //  ['red','green','pink']
  console.log(length) // 返回值：3（新数组长度）

  //数组.unshift(新增内容)
  // 将一个或多个元素添加到数组开头，并返回数组长度
  // 示例：
  let arr = ['red','green']
  let length = arr.unshift('pink')
  console.log(arr) //  ['pink','red','green']
  console.log(length) // 返回值：3（新数组长度）
  ```

- 删除数组中数据
```js
// 数组.pop()
//从数组中删除最后一个元素，并返回该元素的值

//示例：
let arr = ['red','green','blue']
val = arr.pop()
console.log(arr) //['red', 'green']
console.log(val) // blue

//数组.shift()
// 删除第一个元素，并返回该元素的值

//示例：
let arr = ['red','green','blue']
val = arr.shift()
console.log(arr) //['green', 'blue']
console.log(val) // red

// 数组.splice(start, deleteCount)
// deleteCount可选；默认删除到最后
// 删除指定元素

//示例：
let arr = ['red','green','blue']
arr.splice(1,1)
console.log(arr) //['red', 'blue']

```

- 查询数组中的数据
```js
// 数组.indexOf('value')
//查询数组中的指定元素的索引

//示例：
let arr = ['red','green','blue']
num = arr.indexOf('green')
console.log(num) // 1

``` 

## <a href='prac/数据可视化案例.html'>综合练习1：数据可视化案例</a>

## 函数