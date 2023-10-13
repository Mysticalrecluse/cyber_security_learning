# Javascript进阶补充
## 变量
- 变量的声明
```js
function hd(){
    if(false){
        var web = 'houdunren.com'
    }
    console.log(web); // undefined 发生变量提升
    // 相当于
    /* var web
    if(false){
        var web = 'houdunren.com'
    } */
    
    // 变量提升不受块作用域的影响
}
```
- 临时性死区：
  - 临时性死区 (Temporal Dead Zone, 简称 TDZ) 是 ES6 引入的概念，与 let、const 和 class 这几个声明方式相关。TDZ 的存在是为了解决某些与变量提升 (hoisting) 相关的问题，并使代码更具可预测性。

- 全局污染的实际场景
```html
<body>
    <script src="test.js"></script>
    <script>
        web = "someting";
        show() // show()函数来自test.js
        console.log(web) // 'noting'
        // 假设在test.js中的show()函数也声明了变量web，且没有加任何var之类的声明，是全局变量
        // 那么这个web的全局变量，在js文件被引用时，会污染其他代码，导致出现一些预期外的错误
        // 这种现象就是全局污染
        // 使用var,let,consts声明后，该变量在函数执行后，会被销毁，
        // 作用域仅在函数内有效，因此不会出现全局污染
    </script>
</body>
```

- 关于基本数据类型的变量赋值的底层逻辑：
  - 当你为一个基本数据类型的变量赋一个新值时，以下是实际发生的情况：
    - 分配新的内存空间：对于基本数据类型，JavaScript 会在内存中为新值分配新的空间。
    - 保存新值：新的值会被保存在这块新的内存空间中。
    - 更新变量的引用：变量不再引用旧值的内存空间，而是直接指向新值的内存空间。对于基本数据类型，变量实际上保存了这个值本身，而不是一个地址。

- var的作用域
  - var和let对于window的影响是不同的
```js
var screenLeft = 88;
console.log(window.screenLeft); // 88; var的声明是全局于window的
// 会把window本身的属性，screenLeft更改了

let screenLeft = 88
console.log(window.screenLeft) // 浏览器于左侧屏幕的边界距离实际值
console.log(screenLeft) // 88
```

- 对于引用类型的数据的冻结
  - 对于引用类型来说，const由于记录的是地址信息，所以地址内的数据是可以修改的，只要地址不变就行，如果想要让数据也不可修改...
  ```js
  const HOST = {
    url: "https://www.houdunren.com/api",
    port: 443
  };
  Object.freeze(HOST);
  HOST.port: 80; // 后于上面的freeze锁住了HOST的数据，因此，HOST的数据无法修改
  // 但是不会报错，如果使用"use strict" 严格模式，则会有报错提醒
  console.log(HOST); // 443
  ```

- 传值与传址
  - 基本数据类型的数据传递是传值
  ```js
  let a = 1;
  let b = a;
  // 这种情况下，a相当于复制了一个数据空间，里面的值指向b
  ```
  - 引用数据类型则是传址
  ```js
  let e = {}
  let f = e // 此时，e不会复制一份数据，而是把相同的数据地址复制给f
  // 此时，如果e中的数据更改，f的数据也会更改
  ```
  - 如果就想复制一份数据赋值给新的变量，而不是仅仅是地址的话，涉及到对象的深拷贝和浅拷贝的知识点

 
## 循环-打标签
```js
houdunren: for (let i = 1; i <= 10; i++) {
    hdcms: for (let n = 1; n <= 10; n++) {
        if (n % 2 == 0) {
            console.log(i,n);
        }
        if (n + 1 > 10) {
            break houdunren; // 当达成条件之后，退出外部循环 
        }
    }
}
```
### for...in...
```js
let hd = [
    {title: "第一章 走进Javascript", lesson: 3},
    {title: "ubuntu19.10 配置好用的编程工作站", lesson: 5},
    {title: "媒体查询响应式布局", lesson: 8}
];

document.write(
    `
    <table border="1" width="100%">
    <thead><th>标签</th><th>课程数量</th></thead>
    `
    );

for (let i in hd) {
    document.write(
        `
        <tr><td>${hd[i].title}</td><td>${hd[i].lesson}</td></tr>
        `
    );
}

document.write("</table>");

// 实际上，for in 中 i 遍历的是对象的key或者数组的索引值
```

### for...of...
```js
let houdunren = ["hdcms", "houdunren.com"];
for (const value of houdunren) {
    // for...of...主要是处理值
    console.log(value) 
    // hdcms;
    // houdunren.com 
}
```

## 字符串 
- 模板字面量-标签函数
    - 定义：标签函数（Tagged Template Literals）是一个高级用法，允许你通过一个函数来解析模板字符串。这个特性可以用于创建自定义的字符串操作函数，用于处理内嵌表达式和字符串文字等。
    - 用法
    ```js
    function myTag(strings, ...values) {
    // ...
    }

     const variable = 'world';
     const result = myTag`Hello ${variable}!`;
     // myTag 是一个标签函数。当一个模板字符串 Hello ${variable}! 被该标签函数标记时，该模板字符串的文字和表达式会分别被传递给 myTag 函数的 strings 和 values 参数。

     参数详解：
     1. strings：这是一个包含所有字符串文字的数组。例如，对于模板字符串 Hello ${variable}!，strings 数组会是 ['Hello ', '!']。
     2. ...values：这是一个包含所有内嵌表达式求值结果的数组。对于上面的模板字符串，values 数组会是 [ 'world' ]。

     示例：
     function myTag(strings, ...values) { // ...表示不定长参数，不能省略
       let str = '';
       for(let i = 0; i < strings.length; i++) {
         str += strings[i];
         if(i < values.length) {
           str += values[i];
         }
       }
       return str.toUpperCase();
     }

     const name = 'John';
     const result = myTag`Hello ${name}`;
     console.log(result);  // 输出 "HELLO JOHN"

     // 标签函数，就是将字符串中的字符和变量分别以数组的形式存入参数，再在函数内部，进行操作。

     ```
     - 示例2：
    ```js
    let lessons = [
        {title: "后盾人媒体查询", author: "后盾人向军"},
        {title: "FLEX 弹性盒子模型", author: "后盾人"},
        {title: "GRID 栅格系统", author: "顾老师"}
        ];



        function template(){
            return `<ul>
                ${lessons.map((item)=>
                    link`<li>作者:${item.author}, 课程:${item.title}</li>`
                ).join('')}
            </ul>
            `
        };

        function link(strings,...values){
            return strings.map((str,key)=>{
                return str+(values[key]?values[key].replace('后盾人','<a href="#">后盾人</a>'):'')
            }).join('')

            }
        

        document.body.innerHTML += template();
    ```

### 字符串函数
```js
// 字符串字符提取
str.charAt(index)
str[index]

// 字符串提取
let hd = "houdunren.com";

console.log(hd.slice(1)); // oudunren.com
console.log(hd.slice(1,3)); // ou 第二个参数表示截取的位置
console.log(hd.substring(1)); // oudunren.com
console.log(hd.substring(1,3)); // ou 第二个参数表示截取的位置
console.log(hd.substr(1)); // oudunren.com
console.log(hd.substr(1,3)); // oud 第二个参数表示截取的字符个数

//字符串检索
// indexOf()
const hd = "houdunren.com";
hd.indexOf("o") // 1，参数1：返回第一个字母的索引值
hd.indexOf("o",8) // 11 , 参数2：表示从第几个字符开始查找
hd.indexOf("t") // -1，找不到的情况下，返回-1

// lastIndexOf() 从右往左查找，参数和用法和indexOf()相同

// includes()
console.log(hd.includes("h",num)); // true
// includes()方法，返回布尔值，存在true，不存在false
// 参数2：表示从第几个字符开始查找

// startsWith()
console.log(hd.startsWith("h")); // 判断字符串是否是以h开头，返回布尔值

// endsWith() 判断以什么字符结束

// 字符串替换: replace()
console.log(hd.replace("houdunren","hdcms")) // hdcms.com
```
- 小案例：电话号模糊处理
```js
function phone(mobile,len=3) {
    //return String(mobile).slice(0,len*-1) + "*".repeat(len)
    return mobile.toString().slice(0,len*-1) + "*".repeat(len)
}

console.log(phone(13613600632,9))
```

## Boolean隐式转换原理
```js
const boolean = new Boolean(true);
console.log(typeof boolean); // Object
console.log(boolean.valueOf());
if (boolean.valueOf()) {
    console.log("houdunren.com")
}

let hd = true;
console.log(typeof hd); // boolean

let num = 99;
console.log(99 == true); // false
// 数值和boolean值进行比较，boolean隐式转换为数值类型，然后比较
// true转换为数值为1，所以不等于99，返回true

无论是字符串，数组或者对象和布尔值比较，两边都会先隐式转换为数字类型，然后比较

let array = []; // 空数组转换为数值类型，结果为0
let array1 = [1]; // 当数组只有一个值的时候，转换为数值为1
let array2 = [1,2,3] // 当数组中有多个数值的时候，转换为数值为NaN
console.log(array == false); true

console.log(Boolean([])); // 空数组直接转换为boolean值得时候，为true
console.log(Boolean({})); // 空对象也为真
```

## number类型的函数
```js
Number.isInteger(number)
//  判断number是否为整数，返回boolean值

number.toFixed(保留位数)
// 保留小数点位数，进行四舍五入

let number = 99.556
console.log(number.toFixed(2)) // 99.56

Number.isNaN(2/"houdunren")
// 判断表达式结果是否为NaN 

天花板/地板函数
Math.ceil()
Math.floor()

最大，最小函数
Math.max() // 不支持数组，只支持多参数，可以使用apply()对数组进行转换
Math.min()

舍入
Math.round()


```

## date日期时间
- 计算脚本执行时间
```js
const start = Date.now(); // Date.now() 时间戳
for (let i = 0; i < 2000000; i++) {};
const end = Date.now();
console.log((end-start)/1000 + 's');

// 展开语法
const param = [1990,2,22,13,22,19];
const date = new Date(...param); // 展开语法，将数组展开为独立的参数
console.log(date)
```
- ISO时间格式 <-> 时间戳 的转换
```js
const date = new Date("1996-7-12 08:22:12");
// 得到时间戳的方法
console.log(date * 1);
console.log(Number(date));
console.log(date.valueOf());
console.log(data.getTime());

cost timestamp = date.valueOf();
// 时间戳转换为ISO时间格式
console.log(new Date(timestamp));


```