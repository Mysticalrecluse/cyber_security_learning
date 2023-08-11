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
alert('要出的内容') // 弹出窗口
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
- 基本数据类型
  - number 数字型
    - 算术运算符：+ - * / %
  - string字符串型
    - 模板拼接：反引号在最外围括住，变量则使用${}
    -   ```js 
        let age = 30
        document.write(`我今年他妈的${age}岁了`)

        let name = prompt('input your name:')
        let age = prompt('input your age:')
        document.write(`大噶好，我叫${name}，今年${age}岁了`)
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
  
## 类型转换
- 隐式转换
  - 加号两边，只要有一侧是字符串，默认都是字符串
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
### <a href='prac/prac1.html'>练习1：计算两数之和</a>
