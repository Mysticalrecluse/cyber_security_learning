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
  ```js
  let n = 10;  // 分配内存，并存储值10
  n = 20;      // 重新为n分配内存，并存储新的值20
  ```
  - 在这个例子中，变量 n 最初存储了数字 10。当我们将 n 重新赋值为 20 时，存储在 n 中的值从 10 改变为 20。这个过程中，改变的是 a 所存储的值，而非 n 所指向的内存地址。变量 n 依然指向同一个内存位置，但是该位置的内容已经更新。

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

let arr = [1,2,3];
for (let value of arr) {
    value += 10;
}
console.log(arr);

// 当数组的元素是值得时候，for...of...对元素得修改不影响原数组

let arr = [{name:1},{name:2},{name:3}];
for (let value of arr) {
    value.name += 10;
}
console.log(arr);

// 当数组的元素是对象，即引用类型时，对元素的修改会影响原数组的值
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
// 参数2：表示从第几个字符开始查找，这里的几是索引值

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
- 封装日期的格式化函数
```js
const date = new Date("1992-2-12 10:22:18");
console.log(date);
console.log(date.getFullYear()); //获得年份 1992
console.log(date.getMonth() + 1); // 获得月份，从0开始，所以要+1 1
console.log(date.getDate());  // 获得日 12
console.log(date.getHours()); // 获得小时 10
console.log(date.getMinutes()); // 获得分钟 22
console.log(date.getSeconds()); // 获得秒 18

const = `${date.getFullYear()}年${date.getMonth()+1}月`

function dateFormat(date, format="YYYY-MM-DD HH:mm:ss") {
    const config = {
        YYYY:date.getFullYear(),
        MM:date.getMonth() + 1,
        DD:date.getDate(),
        HH:date.getHours(),
        mm:date.getMinutes(), 
        ss:date.getSeconds()
    }
    for (const key in config) {
        format = format.replace(key, config[key]);
    }
    return format;
}

console.log(dateFormat(date, "YYYY年MM日DD日，HH时mm分ss秒"));
```

## 数组

### 数组的查看方式
```js
const hd = [1,2,3,4];
console.log(hd);
console.table(hd); // 以表格的方式更清晰的展示数组
```
### 数组的方法
```js
// 获取数组长度
let array = [1,2,3,4];
console.log(array.length);

// 数组创建，如果只有一个值
let cms = new Array(6); // 6个空元素
console.log(cms.length); // 6

// 为了避免这种情况，新版js推出了Array.of
let arr = Array.of(6); // [6]
console.log(arr.length); // 1

// 判断一个对象是否是数组
console.log(Array.isArray(23)); // false
console.log(Array.isArray([1,2,3])); // true

// 数组转换成字符串
// js的数组在其他语言是不通用的，但是转换成字符串，就可以通用，方便数据传递
let hd = String([1,2,3]); // 1,2,3
let hd = [1,2,3].toString(); // 1,2,3
let hd = [1,2,3].join('-'); // 1-2-3

// 字符串转换成数组
let str = "hdcms";
console.log(str.split('')); // ['h','d','c','m','s']
let str2 = "hdcms,houdunren"
console.log(str2.split(",")); // ["hdcms","houdunren"]

console.log(Array.from(str)); // ['h','d','c','m','s']
// 一般来说，只要有length属性，就能使用Array.from()转换成数组
let obj = {
    0: "hdcms",
    1: "houdunren"
};
console.log(Array.from(obj)) // [] 并不能转换成数组

let obj = {
    0: "hdcms",
    1: "houdunren",
    length: 2
};
console.log(Array.from(obj)) // ["hdcms","houdunren"]，成功转换成数组  

// Array.from(非数组,函数(用来对数组里的元素进行遍历操作))
// 作用：将有length属性的对象转换为数组，并对其元素进行二次处理
let divs = document.querySelectorAll("div");
console.log(
    Array.from(divs,function(item) {
        item.style.backgroundColor="red";
        return item;
    })
);
```

### 展开语法
```js
let arr = ["hdcmd","houdunren"];
let hd = ["js","css"];
arr = [...arr, ...hd]; // ["hdcmd","houdunren","js","css"] 

function sum(...args) {
    console.log(args);
    return args.reduce((s,v) => {
        return (s += v);
    },0);

}

console.log(sum(1,2)); // [1,2]  3

// 展开语法也能将伪数组转换成数组
const div = document.querySelectorAll('div');
[...div].map((item) => {
    item.addEventListener('click',function() {
        this.classList.toggle("hide");
    })
})
```

### 解构语法
- 将数组里的值批量的赋值给变量
```js
let arr = ['后盾人,2010'];
let name = arr[0];
let year = arr[1];
console.log(name,year);

// 解构赋值
let [name,year] = arr // 等同于：let name = arr[0]; let year = arr[1];

function get() {
    return ["后盾人", 2010];
}
let [name,year] = get();

let [name, ...args] = ['mystical', 1,2,3,4];
console.log(name); // mystical
console.log(args); // [1,2,3,4]

// 设置解构的默认值
let [name, year = 2000] = ['mystical'];
console.log(year) // 2000
```

### 数组中添加元素的多种技巧
```js
// 添加元素方法1
let array = [1,2,3,4];
array[array.length] = 5; // [1, 2, 3, 4, 5]
array[array.length] = 6; // [1, 2, 3, 4, 5, 6]

// 合并多个数组
let array1 = [1,2,3];
let array2 = [4,5,6];
let array3 = [7,8,9];
let arraySum = [...array1,...array2,...array3];
console.log(arraySum)

// 使用push合并数组，push会自动返回总长度
length = array1.push[...array2,array3];
console.log(array1);
console.log(length);
```
- 添加和删除总结：
  - 添加：push, unshift (都返回长度)
  - 删除：pop, shift (都返回值)，pop和shift不接受任何参数

- 数组的填充
```js
console.log(Array(5)) // emypt*5
console.log(Array(5).fill(1)) // [1,1,1,1,1]
console.log(Array(5).fill(1,1,3)) // [empty,1,1,empty*2]
// 参数1：填充的值，参数2，从索引几开始填充，参数3：填充到第几个
```

- 数组的截取
```js
// 场景1：slice
let arr = [1,2,3,4,5];
let hd = arr.slice(1,2); // [2]
console.log(arr) // [1,2,3,4,5]

// 场景2：splice
let arr = [1,2,3,4,5];
let hd = arr.splice(1,3);
console.log(hd); // [2,3,4]
console.log(arr); // [1,5]

// splice实现从中间添加元素
let arr = [1,2,3,4,5];
let hd = arr.splice(1,3,'a');  
// 第三个带后面的参数是在删除的地方填充指定元素

// 使用splice实现在数组中间添加元素
let arr = [1,2,3,4,5];
let hd = arr.splice(1,0,'a','b','c');
console.log(hd) [] // splice是返回一个数组，元素是删除的数组元素
console.log(arr) [1, 'a', 'b', 'c', 2, 3, 4, 5]
总结：
slice是提取指定子数组，对原数组无影响
splice是截取指定子数组，指定的子数组会从源数组中删除
```

### 数组元素移动的函数案例
```js
function move(array,from,to) {
    if (from < 0 | to >= array.length) {
        console.error("参数错误")
        return;
    }
    const newArray = [...array];
    let item = newArray.splice(from,1);
    newArray.splice(to,0,...item);
    return newArray;
}

let array = [1,2,3,4];
console..table(move(array,1,3)) // [1,3,4,2]

```

### 清空数组的多种方式
```js
let hd = [1,2,3,4,5];
let arr = hd;
hd = [];
// 此时相当于开辟一个新的空间，存放空数组，然后将hd指向新的空间，但是arr的数组不变
console.log(arr) // [1,2,3,4,5]
console.log(hd) // []

let hd = [1,2,3,4,5];
let arr = hd;
hd.length = 0;
// 此时相当于将原数组的值清空，arr和hd都变成了空数组
console.log(arr); //[]
console.log(hd); //[]
```

### 数组的拆分和合并
```js
// 拆分
let str = "mystical";
console.log(str.split('')); // ['m','y','s','t','i','c','a','l']
let str2 = "mystical,recluse";
console.log(str.split(',')); // ['mystical','recluse']

// 合并
let str = "mystical,recluse";
let hd = str.split(',');
console.log(hd.join('-')); // mystical-recluse

let arr = ["mystical","recluse"];
let hd = [1,2,3,4];
let cms = ["shop","cms"];
arr = arr.concat(hd,cms);
arr = [...arr,...hd,...cms];

// 将数组的指定元素复制到指定位置
let hd = [1,2,3,4,5,6];
console.log(hd.copyWithin(3,1,3)); // [1,2,3,2,3,6]
// 参数1：复制到的位置（索引值）
// 参数2：从第几个元素开始复制（索引值）
// 参数3：复制到第几个（元素个数）
```

### 查找元素基本使用
```js
// indexOf() 和 lastIndexOf()
// 两个参数，第一个参数是查找的元素，第二个参数是查找的起始点
let arr = [1,2,3,4,2];
console.log(arr.indexOf(2)) // 1
console.log(arr.lastIndexOf(2)) // 4
console.log(arr.indexOf(-9))  // 查询不到的都返回-1
console.log(arr.indexOf(2,2)) // 4

// includes()
console.log(arr.includes(2)); // true 返回布尔类型
// includes()不适用于引用数据类型
```

### includes的实现原理
```js
let arr = [1,2,3,4,5];
function includes(array,find) {
    for (const value of array) if (value===find) return true;
    return false;
}
console.log(includes(arr,99)); // false
```

### find与findIndex新增方法
```js
let arr = [1,2,3,4,5];
let res = arr.find(function(item){
    return item ==200;
})
console.log(res); // undefined

// find()函数返回的是值，

// find()可以查询引用数据类型是否在列表中，includes不行
let lessons = [{name:"js"},{name:"css"},{name:"mysql"}];
let status = lessons.find(function(item){
    return item.name == "css";
});
console.log(status); // 返回{name:"css"}

// findIndex()返回索引值

let index = lessons.findIndex(function(item){
    return item.name=="mysqll";
});
console.log(index); // 2
```

### find函数的实现方法
```js
function find(array,callback){
    for(const value of array) {
        if (callback(value)) return value;
    }
    return undefined;
}
```
- 箭头函数有一个特点：如果函数体只有一条语句，而且没有使用大括号 {} 包裹，那么这条语句的执行结果会被自动返回。这就是所谓的 "implicit return"（隐式返回）

### 数组排序技巧
```js
let arr = [1,4,6,2,3];
arr = arr.sort(function(a,b)) {
    // a-b为负数，从小到大
    // a-b为正数，从大到小
    return a - b; // 从小到大排序
    return b - a; // 从大到小排序
}
console.log(arr);

// 对象排序示例
let cart = [
    {name:"iphone",price:12000},
    {name:"imac",price:18000},
    {name:"ipad",price:3200}
];
cart = cart.sort(function(a,b) {
    return a.price - b.price;
});
console.log(cart); // 按价格升序排列
```

### sort排序算法原理实现
```js
let arr = [1,5,3,9,7];

function sort(array,callback) {
    for (const n in array) {
        for (const m in array) {
            if (callback(array[n],array[m]) < 0) {
                const temp array[n];
                array[n] = array[m];
                array[m] = temp;
            }
        }
    }
    return array;
}
arr = sort(arr,function(a,b) {
    return a - b;
});
console.log(arr);
```
- 正常冒泡排序的用法
```js
function sort(array, callback) {
    for (let i = 0; i < array.length - 1; i++) {        // 外部循环，对应于每一轮的“冒泡”
        for (let j = 0; j < array.length - 1 - i; j++) {    // 内部循环，对应于每一对相邻元素的比较
            if (callback(array[j], array[j + 1]) > 0) { 
                // 使用回调函数比较元素，如果array[j] > array[j+1]，则返回值为正数
                const temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;  // 交换元素位置
            }
        }
    }
    return array;
}

let arr = [5, 1, 4, 2, 8];
arr = sort(arr, function(a, b) {
    return a - b;  // 对于升序排列
});
console.log(arr);  // 输出：[1, 2, 4, 5, 8]

```

### 数组的迭代
- 数组遍历操作时，元素是值类型或引用类型的区别
```js
let arr = [1,2,3,4];
for (let i of arr) {
    i += 10;
}
console.log(arr); // [1,2,3,4]
// 当数组元素是值类型的时候，对于数组元素的遍历改变，不会影响数组
// 底层原理是值类型的赋值改变，是另开辟一块内存空间存储更改后的值，
// 而不是在直接更改原数组空间内的数据

let arr2 = [{n:1}, {n:2}, {n:3}]
for (let j of arr2) {
    j.n += 10;
}
console.log(arr2); // [{n:11}, {n:12}, {n:13}]
// 如果是引用类型，则会更改数组中的值

```
```js
let arr = [1,2,3,4];
keys = arr.keys()
console.log(keys) // Array Iterator {}
// 生成一个可迭代对象

while(({value, done} = keys.next()) && !done) {
    console.log(value, done)
}
// 遍历keys.next中的value和done的值
// 0 false
// 1 false
// 2 false
// 3 false

entries = arr.entries()
console.log(entries) // Array Iterator {}
// 生成一个可迭代对象

while(({value, done} = entries.next()) && !done) {
    console.log(value, done)
}
// 遍历keys.next中的value和done的值
// [0,1] false
// [1,2] false
// [2,3] false
// [3,4] false

for(let e of entries){
    console.log(e) // [0,1] [1,2] [2,3] [3,4]
}
```
### 高效处理数组方法
```js
// every方法
const user = [
    {name: "李四"， js: 89},
    {name: "王五"， js: 99},
    {name: "张三"， js: 55}
];
const res = user.every(function(item) {
    console.log(item);
    // 为保证性能，只要遇到一个假，后面就不在遍历
    return item.js >= 60
});
// every方法的遍历中，有一个为假，则返回结果为false
console.log(res ? "全部同学都及格" : "有同学没及格");

// some方法
const user = [
    {name: "李四"， js: 89},
    {name: "王五"， js: 99},
    {name: "张三"， js: 55}
];
const res = user.some(function(item) {
    console.log(item);
    // 为保证性能，只要遇到一个真，后面就不在遍历
    return item.js >= 60
});
// some方法的遍历中，有一个为真，则返回结果为真
console.log(res ? "有同学及格了" : "所有同学都没及格");

```
- some方法的实战案例(判断敏感词)
```html
<body>
    <input type="text", name="title"><span></span>
    <script>
        keywords = ["php", "js"];
        title = document.querySelector("input[name=title]");
        title.addEventListener("keyup", function() {
            const res = keywords.some(keyword => {
                return title.value.indexOf(keyword) !== -1;
            });
            document.querySelector("span").innerHTML = res ? "有敏感词" : "没有敏感词";
            })
    </script>
</body>
```
- filter方法基本结构
```js
let arr = ['hdcms', 'houdunren.com'];
let newArray = arr.filter(function(value, index, arr){
    return true;
});
// 如果返回结果为真，则将该值返回到新数组中
```
- filter实战案例（课程检索）
```js
let lessons = [
    {title: "媒体查询响应式布局", category: "css"},
    {title: "FLEX 弹性盒模型", category: "css"},
    {title: "MYSQL多表查询随意操作", category: "mysql"}
];
const cssLessons = lessons.filter(function(lesson){
    return lesson.category == 'css'
})
console.table(cssLessons);
```
- 自定义模拟filter()函数的过程
```js
hd = [1,2,3,4];
function filter(array, callback) {
    let newArray = [];
    for (const value of array) {
        if (callback(value) === true) {
            newArray.push(value);
        }
    }
    return new Array;
}
console.log(
    fileter(hd, function(value){
        return value > 2;
    })
)
```

- reduce()
```js
let arr = [1,2,3,4,5];
arr.reduce(function(pre,value,index,array){
    console.log(pre,value);
})
// 1  2
// undefined  3
// undefined  4
// undefined  5
// 第一次遍历，pre是数组的第一个元素，value是第二个元素
// 后面pre是function的返回值，而value是下一个元素

arr.reduce(function(pre,value,index,array){
    console.log(pre,value);
    return 99
}， 0) // 这里第二个参数0是pre的初始返回值，这样value就是第一个元素
// 0 1
// 99 2
// 99 3
// 99 4
// 99 5
```

- 实战示例 - 统计数组中元素出现次数
```js
let arr = [1,2,3,1,1];
function arrayCount(array, item) {
    array.reduce(function(total, cur) {
        total += item == cur ? 1 : 0;
        return total;
    }, 0)
}
console.log(arrayCount(arr, 1))
```

- 实战示例2 - 统计数组中的最大值
```js
let arr = [1,2,3,5,3,66];
function arrayMax(array){
    return array.reduce(function(pre,cur){
        return pre > cur ? pre : cur;
    })
}
console.log(arrayMax(arr));
```
- 实战示例3 - 购物车汇总与获取最贵商品
```js
let cart = [
    {name: "iphone", price: 12000},
    {name: "imac", price: 25000},
    {name: "ipad", price: 3600}
];
function maxPrice(goods){
    return goods.reduce(function(pre, cur){
        return pre.price > cur.price ? pre : cur;
    })
}
console.log(maxPrice(cart));
function sum(goods){
    return goods.reduce(function(pre, cur){
        return pre + cur.price;
    }, 0)
}
console.log(sum(cart));
function betterOneWan(goods){
    return goods.filter(function(item){
        return item.price > 10000
    })
}
console.log(betterOneWan(cart));

function getNameByPrice(goods, price) {
    return goods.reduce(function(arr, cur){
        if (cur.price > price) arr.push(cur);
        return arr
    },[]).map((item) => item.name)
}
console.log(getNameByPrice(cart));
```

- 实战示例4 - 数组去重
```js
let arr = [1,2,2,1,2,4,5,3,5,7];
let newArray = arr.reduce(function(pre, cur){
    if (pre.includes(cur) === false) pre.push(cur);
    return pre;
},[]);
console.log(newArray);
```
- reduce()最终实战-炫酷Logo
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        *{
            padding: 0; margin: 0;
        }

        body{
            display: flex;
            width: 100vh;
            height: 100vh;
            justify-content: center;
            align-items: center;
            background-color: rgb(120, 123, 125);
        }

        div{
            font-size:5em;
            font-weight: bold;
            text-transform: uppercase;
            color:blueviolet
        }

        div > span {
            position: relative;
            display: inline-block;
        }

        .color {
            animation-name: color;
            animation-duration: 1s;
            animation-iteration-count: 2;
            animation-timing-function: linear;
            animation-direction: alternate;
        }
        @keyframes color {
            50%{
                color: #f1c40f;
                transform: scale(2);
            }
            to{
                color: #e74c3c
                transform: scale(0.5);
            }
        }

        .color2 {
            color: blue;
        }
    </style>
</head>
<body>
    <div>hello,Mystical</div>
    <script>
        let div = document.querySelector('div');
        [...div.textContent].reduce(function(pre, cur, index){
            pre == index && (div.innerHTML = "");
            let span = document.createElement('span');
            span.innerHTML = cur;
            div.appendChild(span);
            span.addEventListener("mouseover", function(){
                this.classList.add("color");
            })
            span.addEventListener("animationend", function(){
                this.classList.remove("color");
            })
        }, 0)
    </script>
</body>
</html>
```

## Symbol
- 功能：
  - Symbol 的主要特点是每个创建的 Symbol 都是唯一的，即使你用相同的参数创建两个 Symbol，它们也是不同的。这个特性使得 Symbol 成为了一种非常有用的工具，特别是在涉及到对象属性键（property keys）的场景中。

- 特点
  - 唯一性：
    - 每个 Symbol 都是完全唯一的，这提供了一种安全的方法来创建私有或唯一的对象属性。
  - 不可枚举性：
    - 在默认情况下，用 Symbol 作为对象属性的键时，这些属性不会出现在常规的枚举中，如 for...in 循环或 Object.keys() 方法中。
  - 不可更改性：
    - Symbol 一旦被创建，就不能被修改。

- 基本使用方法
```js
let hd = Symbol();
console.log(typeof(hd)); // symbol

let hd = Symbol(); 
let edu = Symbol();
console.log(hd == edu); // false

let hd = Symbol('后盾人在线教程'); // Symbol的括号内，可以添加描述
console.log(hd.description);

let cms = Symbol.for("hdcms");
let edu = Symbol.for("hdcms");
console.log(cms == edu);
// Symbol.for()，可以是一个symbol类型赋予多个变量
console.log(Symbol.keyFor(cms)) // hdcms
// 使用Symbol.for定义的Symbol类型数据，可以使用Symbol.keyFor()拿到描述
// Symbol("")这种普通定义的，不能使用Symbol.keyFor()展示描述
// Symbol.for()是全局声明，因此后续多次声明，都是使用一个Symbol数据
```

- 实际应用
```js
let grade = {
    李四： {js: 100, css: 89},
    李四： {js: 35, css: 55}
};
console.log(grade);
// 李四:{js: 35, css: 55}
// 键相同的情况下，后面的值会把前面的覆盖掉

let user1 = "李四";
let user2 = "李四";
let grade = {
    [user1]： {js: 100, css: 89},
    [user2]： {js: 35, css: 55}
};
console.log(grade);
// 如果对象的键要引入变量的值的话，需要用中括号括起来
// 变量值相同的情况下，后面的值依然会把前面的覆盖掉

// 解决方法
let user1 = {
    name: "李四",
    key: Symbol()
};
let user2 = {
    name: "李四",
    key: Symbol()
};
let grade = {
    [user1.key]: {js: 100, css: 89},
    [user2.key]: {js: 35, css: 55}
};
console.log(grade);
console.log(grade[user2.key]);
console.log(grade[user1.key]);
```

- Symbol在缓存容器中的使用
```js
class Cache{
    static data = {};
    static set(name, value) {
        return (this.data[name] = value)
    }
    static get(name){
        return this.data[name];
    }
}

let user = {
    name: "apple",
    desc: "user_info"
};
let cart = {
    name: "apple",
    desc: "cart"
};
Cache.set('apple',user);
Cache.set('apple',cart);
console.log(Cache.get("apple")); // 此时用户的数据被购物车的数据覆盖了

let user = {
    name: "apple",
    desc: "user_info",
    key: Symbol("user_info")
};
let cart = {
    name: "apple",
    desc: "cart",
    key: Symbol("cart")
};
Cache.set(user.key,user);
Cache.set(cart.key,cart);
console.log(Cache.get(user.key)); // 此时就不会被覆盖，Symbol()永远不相同 
```

- 扩展特性与对象属性保护
```js
let symbol = Symbol("这是一个Symbol类型");
let hd = {
    name: "后盾人",
    [symbol]: "houdunren.com"
};
for (const key in hd) {
    console.log(key);
} // 无法读取到symbol，只能读取到name

for (const key of Object.keys(hd)) {
    console.log(key);
} // 依然无法读取到symbol，只能读取到name

for (const key of Object.getOwnPropertySymbols(hd)) {
    console.log(key);
} // 只能遍历到Symbol属性

for (const key of Reflect.ownKeys(hd)) {
    console.log(key);
} // 可以遍历到所有属性
``` 
```js
let site = Symbol('这是一个Symbol');
class User{
    constructor(name) {
        this.name = name;
        this[site] = "后盾人";
    }
    getName() {
        return `${this[site]} ${this.name}`;
    }
}
let lisi = new User("李四");
console.log(lisi.getName());
```

## Set与WeaksSet类型
### Set与Array、Object对比
- set基础用法
```js
// set类型的变量声明
let set = new Set();
set.add(1);
set.add(1);
console.log(set); // Set(1) {1} set类型的值不能重复
// array可以重复

// 声明的时候，直接初始化元素
let set = new Set([1,2,3,4,5]);
console.log(set); // {1,2,3,4,5}

let set1 = new Set();
set.add(1);
set.add("1");
console.log(set1); // {1, "1"}, set类型中属性类型严格区分

let obj = {
    1: "houdunren",
    "1": "hdcms"
};
console.log(obj); // {1: "houdunren"}
// 在对象中，所有属性都会自动转化成字符串，且相同属性，后项值覆盖前项
```

### Set元素的检测与管理
```js
let set1 = new Set("hdcms");
console.log(set1); // ['h'.'d'.'c'.'m'.'s']
// 只传入一个字符串的话，等价于Set([..."hdcms"])，会将字符串展开

let set2 = new Set(["hdcms","houdunren"])
console.log(set2.size); // 2
// 返回set中值得数量
console.log(set.has("hdmms.com")) // false
// 判断set中成员是否存在，返回布尔值
console.log(set.delete("hdcms")); // 删除set中得元素,删除成功返回true
console.log(set.size); // 1

console.log(set.values()); // {"houdunren"}
// 查看set中得值

set.clear(); // 清空set中得值
console.log(set.size); // 0
```

### 关于Set类型的类型转换
```js
// set 转 数组array
let set = new Set(['hdcms','houdunren']);
console.log(Array.from(set)); // ['hdcms','houdunren']
console.log([...set]); // ['hdcms','houdunren']

// 实际应用 - 对set的值进行过滤
let hd = new Set("123456789"); // {"1","2","3","4","5","6","7","8","9"}
let arr = [...hd].filter(function(item){
    return item < 5;
});
hd = new Set(arr);
/*
    优化后：
    let hd = new Set([...hd].filter(item => item < 5>));
*/
console.log(hd); // {"1","2","3","4"}

// 实际应用2：数组去重
let array = [1,2,3,4,5,2,3,1];
array = [... new Set(array)];
console.log(array); // [1,2,3,4,5]
```

### set的遍历方式
```js
let set = new Set(["hdcms","houdunren"]);
set.forEach(function(value, key, set) {
    console.log(value);
    console.log(key);
    console.log(set);
}) ;

for (const value of set) {
    console.log(value);
}
// 在set中value和key的值是一样的，可以看entries的值就可以显示出来
```

### 使用Set处理网站关键词
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            padding: 200px;
        }
        ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        li {
            border: solid 1px #ccc;
            padding: 10px;
        }
        li:nth-of-type(odd) {
            background: yellowgreen;
        }
    </style>
</head>
<body>
    <input type="text" name="hd" />
    <ul></ul>
    <script>
        let obj = {
            data: new Set(),
            keyword(word) {
                this.data.add(word);
            },
            show() {
                let ul = document.querySelector('ul');
                ul.innerHTML = '';
                this.data.forEach(function(value){
                    ul.innerHTML += `<li>${value}</li>`;
                });
            }
        }
        let input = document.querySelector("[name='hd']");
        input.addEventListener('blur', function(){
            obj.keyword(this.value);
            obj.show();
        })
    
    </script>
</body>
</html>
```

### 并集，交集，差集算法实现
```js
let a = new Set([1,2,3,4,5]);
let b = new Set([4,5,2,9]);
console.log(new Set([...a, ...b])); // 并集

// 差集
console.log(
    new Set([...a].filter(function(item){
        return !b.has(item);
    }))
);

// 交集
console.log(
    new Set([...a].filter(function(item){
        return b.has(item);
    }))
);
```

### WeakSet语法介绍
```html
<body>
    <div></div>
    <div></div>
    <script>
        let nodes = new WeakSet();
        let divs = document.querySelectorAll('div');
        divs.forEach(node => nodes.add(node));
        console.log(nodes);
        nodes.delete(divs[0]);
        console.log(nodes.has(divs[0]));
        console.log(nodes);
        
    </script>
</body>
```

### WeakSet的弱引用特性
```js
let hd = {name: "houdunren"} // 引用计数器 +1 = 1
let edu = hd;  // 引用计数器 +1 = 2
let hd = null; // 引用计数器 -1 = 1
let edu = null; // 引用计数器 -1 = 0 ,垃圾回收机制将内存销毁

let hd = {name: "houdunren"} // 引用计数器 +1 = 1
let set = new WeakSet();
set.add(hd); // 此时引用计数器并不增加（弱引用）
// 因此Weakset类型不支持遍历

```

## 函数
### 函数的声明形式
```js
// 函数和字符串本质上都是对象
let func = new Function('title','console.log(title)');
func();

// 方式2：
function hd(title) {
    console.log(title);
}
hd("houdunren");

// 方式3：函数返回值赋值
let cms = function(title) {
    console.log(title);
}; // 赋值语句，结尾加引号
cms("houdunren"); // houdunren

// 方式4：
let user = {
    name: null,
    setUsername: function(name) {
        this.name = name;
    },
    /*
        简写形式；
        setUsername(name) {
            this.name = name;
        }
    */
    getUsername: function(){
        return this.name;
    }
    /*
        简写形式；
        getUsername() {
            this.name = name;
        }
    */
};
```

### 全局函数
```js
function hd() {
    console.log("后盾人")；
}
hd();
window.hd(); // 函数创建完后，默认会把该函数作为windows对象中的方法存在
// 如果window中原有属性和全局函数的函数名一样，会被其覆盖
// 因此建议使用模块化构建函数

let cms = function() {
    console.log("mystical");
};
cms(); // 将匿名函数赋值给let变量，通过调用变量来调用函数，可以防止被压入window对象的情况发生

// 还是建议将函数放入类中，尽量避免全局函数的情况
```

### 匿名函数
```js
let hd = function() {
    console.log("mystical");
}
hd();
// 匿名函数不能函数提升
let cms = hd;
cms(); // mystical
//因为函数本质也是一个对象，对象引用地址赋值，指针传递
```
- 函数的提升
```js
show();
function show() {
    console.log("mystical");
}
// 函数自动提升
```

### 立即执行函数
```js
(function(window) {
    function hd() {
        console.log("4.1.js-hd");
    }
    function show() {
        console.log("4.1.js-show");
    }
    window.js1 = [hd, show];
}) (window)

// 使用块级作用域防止不同外部文件的函数名重名，污染全局变量的问题
{
    let hd = function() {
        console.log("4.1.js-hd");
    };
    let show = function() {
        console.log("4.1.js-show")
    };
    window.js1 = {hd, show};
}

// 还是建议使用类，模块化的方式，函数私有化，防止出现全局污染
```

### 默认参数的方式
```js
function avg(total, year) {
    year = year || 1; // 用短路运算，达到默认参数的效果
    console.log(year);
    return Math.round(total / year);
}
console.log(avg(2000));

// 方式2：
function avg(total, year = 1) {
    console.log(year);
    return Math.round(total / year);
}
console.log(avg(2000));

function sortArray(array, type = "asc") {
    return array.sort((a, b) => type == "asc" ? a - b : b - a;)
}
console.log(sortArray([3,1,5,4,2], "desc"));
```

### 函数参数与arguments
- 函数参数
```js
function hd(a) {
    return a <= 3;
}
let arr = [1,2,3,4,5,6,7].filter(hd);
console.log(arr);

// 案例2
let i = 0;
function cms() {
    console.log(++i);
}
setInterval(cms, 1000)

// 案例3
function event() {
    alert(this.innerHTML)
}
document.getElementById("hd").addEventListener("click", event);
```
- 不定长参数
```js
// 老版本方法
function sum() {
    let total = 0;
    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i];
    }
    return total;
    /*
        优化后：
        return [...arguments].reduce((a, b) => a + b);
    */
}
console.log(sum(1,23,3,42,45,53));

// 新版本，使用点语法
function sum(...args) {
    return args.reduce((a, b) => a + b);
}
console.log(sum(1,23,3,42,45,53));
```

### 箭头函数
```js
let hd = () => 1 + 2;
console.log(hd());

let hd2 = [1,2,3,4,5,5,6,7,8].filter(value => value <= 3);
console.log(hd2);
// 只有一个参数，不用加括号
// 如果只有一个表达式，且有return，也都可以省略
```

### 递归函数
```js
function res(n) {
    return n == 1 ? 1 : n * res(n - 1);  
}
console.log(res(4));
```

### 展开语法
```js
let hd = [1,2,3];
let [a, b, c] = [...hd];
console.log(a); // 1
console.log([...hd]); // [1,2,3]

let [a, ...edu] = [1,2,3,4];
console.log(edu); // [2,3,4]

function sum(...args) {
    console.log(args);
    return args.reduce((a, b) => a + b);
}
console.log(sum(1,2,3,4,5));
```

### 函数与方法中this的不同
```js
let obj = {
    name: 'houdunren',
    show: function() {
        return this.name; // 表当前对象的引用
    }
};
console.log(obj.show());

let obj = {
    name: 'houdunren',
    show: function() {
        console.log(this); // {name : ...}这里this指当前对象
        function render() {
            console.log(this); // 这里，当它作为函数而不是对象的方法时
            // this指代的就是window
        }
        render();
    }
};

function User(name) {
    this.name = name;
    this.show = function() {
        return this.name;
    };
}
let lisi = new User("李四");
console.log(lisi.show()); // 李四
// 构造函数本身就是一个特殊的对象

let Lesson = {
    site: "后盾人"，
    lists = ["js","css","mysql"],
    show: function() {
        const self = this;
        return this.lists.map(function(value) {
            console.log(this); // 这里this指代 window
            console.log(self.site); // “后盾人”
        /*
            return this.lists.map(function(value){
                return `${this.site}-${value}`;
            }, this);
            // map中第二个参数可以将this的指针从window指向上级方法的对象
        */
        })
    }
}

// 箭头函数中的this
let Lesson = {
    site: "后盾人"，
    lists = ["js","css","mysql"],
    show: function() {
        const self = this;
        return this.lists.map(title => console.log(this));
        // 箭头函数的this指向父级元素的上下文
    }
};
```

### 构造函数的特征
```
构造函数

用途：构造函数通常用于创建特定类型的对象。它们定义了对象的初始状态和方法。

命名约定：构造函数通常首字母大写（这是一种约定，并非强制性规则）。

使用 new 关键字调用：当使用 new 关键字调用函数时，该函数表现为构造函数。这会创建一个新的对象实例，并将 this 绑定到这个新对象上。

返回值：如果构造函数没有显式返回一个对象，则会自动返回 this（即新创建的对象实例）。如果构造函数返回一个对象，则会返回该对象而不是 this。

普通函数
用途：普通函数用于执行特定任务或计算值。

命名约定：普通函数通常采用小写字母开始的驼峰命名法。

调用方式：普通函数直接调用，而不使用 new 关键字。在这种情况下，this 指向全局对象（在严格模式下为 undefined）。

返回值：普通函数可以返回任何类型的值。如果没有返回值，则默认返回 undefined。
```

- call()的用法
```js
function User(name) {
    this.name = name;
}
let lisi = new User("lisi"); // 生成构造函数
let hdcms = {url: "hdcms.com"}
User.call(hdcms, "开源系统")；
console.log(hdcms); // {url: "hdcms.com", name: "开源系统"}
// this指向发生变化
// call()的第一个参数；构造函数的this指向对象
// call()的第二个参数：构造函数的形参
```
```js
let lisi = {
    name: "李四"
};
let wangwu = {
    name: "王五"
};
function User(web, url) {
    console.log(web + url + this.name);
}
User.call(lisi); // 将this指向lisi对象，并立即执行函数
User.call(lisi, "后盾人", "houdunren.com");
User.apply(lisi, ["后盾人", "houdunren.com"]);
// apply和call作用基本一致，区别在于传递函数参数的时候
// call()需要依次传值，而apply则是传递一个数组
```
- call()利用改变this指向实例
```js
function show() {
    alert(this.innerHTML);
}
let buttons = document.querySelectorAll("button");
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", event => {
        show.call(event.target);
    });
}
```
- 构造函数的属性继承
```js
function Request() {
    this.get = function(params) {
        let str = Object.keys(params)
        .map(k => `${k}=${params[k]}`)
        .join("&");
        let url = `https://houdunren.com${this.url}/${str}`
        console.log(url);
    };
}
function Article() {
    this.url = "article/lists";
    Request.call(this)
}
let a = new Article();
a.get({id: 1, cat: "js"});

function User() {
    this.url = "user/lists";
    Request.call(this)
}
let user = new User();
user.get({id: 2, role: "admin"});
```

- bind()用法
```js
function show() {
    console.log(this.name);
}
show.bind({name: "hdcms"})();
// 和call类似，但是不直接执行函数，而是生成一个函数
// 要执行，需要再次调用
```
- bind实例
```js
function Color(elem) {
    this.elem = elem;
    this.color = ['#f1c40f', '#e67e22', '#e74c3c', '#8e44ad', '#2980b9', '#16a085'];
     this.run = function() {
        setInterval(function(){
            let i = Math.floor(Math.random() * this.color.length);
            this.elem.style.backgroundColor = this.color[i];
        }.bind(this)
        , 1000);
    }
}
let obj = new Color(document.body);
obj.run();
```

## 闭包与作用域 
```js
function hd() {
    let n = 1;
    return function sum() {
        console.log(++n);
    }
}
let f = hd();
f(); // 2
f(); // 3
f(); // 4
```
```js
function hd() {
    let n = 1;
    return function sum() {
        let m = 1;
        return function show() {
            console.log(++m);
            console.log(++n);
        };
    };
}
let a = hd()();
a(); // 2, 2
a(); // 3, 3
```
- 构造函数的回收机制
```js
function Hd() {
    let n = 1;
    this.sum = function() {
        console.log(++n);
    };
}
let hd = new Hd(); 
// 构造函数，有隐式返回值this指向的对象
// this指向新创建的实例对象上。
// 因此，函数内部的值，仍被外部使用，不会销毁
hd.sum();
hd.sum();
```

- 在for循环中, let, var的执行原理
  - 感觉从堆栈的内存存储角度思考更容易理解

### 闭包
- 概述：当前函数能访问其他函数作用域的数据，就称为闭包
```js
function outerFunction() {
    var outerVariable = 100;

    function innerFunction() {
        console.log(outerVariable);
    }

    return innerFunction;
}

var myClosure = outerFunction(); // outerFunction 执行完毕
myClosure(); // 输出: 100

```
- 闭包的关键特性
  - <font color=tomato>函数嵌套函数</font>：闭包通常涉及到一个函数内部定义另一个函数。
  - <font color=tomato>访问外部变量</font>：内部函数可以访问外部函数的变量，即使外部函数已经执行完毕。
  - <font color=tomato>保持变量状态</font>：即使外部函数的执行上下文已经消失，内部函数仍然可以引用外部函数的变量。这意味着闭包可以保持变量的状态。

- 实战应用实例
```js
function between(a, b) {
    return function(v) {
        return v.price >= a && v.price <= b;
    };
}
console.table(lessons.filter(between(10,100)));
```
- 通过闭包做移动按钮
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        button {
            position: absolute;
        }    
    </style>
</head>
<body>
    <button message="hdcms">hdcms</button>
    <button message="houdunren">houdunren</button>
    <script>
        let btns = document.querySelectorAll('button');
        btns.forEach(function(item) {
            item.addEventListener('click', function() {
                let left = 1;
                setInterval(function() {
                    left += 1;
                    item.style.left = left + 'px';
                }, 5);
            });
        });
    </script>
</body>
</html>
```
- 按钮滑动优化后
```js
let btns = document.querySelectorAll('button');
let bind = false;
btns.forEach(function(item) {
    item.addEventListener('click', function() {
        if (!bind) { // 不管点击几次，只触发一次
            let left = 1;
            bind = true;
            setInterval(function() {
            item.style.left = left++ + 'px';
            }, 100);
        }                
    });
});
```

## JS对象
- 使用字面量形式创建对象
```js
let user = {
    name: "mystical",
    grade: [
        {name: "js", score: "99"},
        {name: "docker", score: "76"}
    ],
    average() {
        // 使用this精简代码，括号里不用写参数，可以直接调用this指向的方法中的参数
        let total = this.grade.raduce((t, l) => t + l.score, 0);
        return `${this.name}的平均成绩是：${total / this.grade.length}`;
    }
};
console.log(user.average());
```
### 属性的操作方法
```js
// 调用对象的属性
let user = {
    name: "mystical",
    "my age": 18
};
console.log(user.name) // 使用点语法, 推荐
console.log(user["name"]) // 中括号中使用字符形式,如果属性是字符形式，不能用点语法

// 添加属性
user.age = 19;
user.get = function() {
    return `${this.name}的年龄是${this.age}`;
};
console.log(user.get());

// 删除属性
delete.user.age;
console.log(user.age) // undefined
```

### 对象中的展开语法 
```js
let user = {name: "mystical", age: 22};
let hd = {...user, lang: "zh"};
console.log(hd);
```
- 展开语法的应用（配置默认与自定义配置）
```js
function upload(params) {
    let config = {
        type: "*.jpeg, *.png",
        size: 10000
    };
    config = {...config, ...params};
    console.log(config);
}
console.log(upload({size: 99, type: "*.gif"}));
// 自定义配置，会把默认配置覆盖
```

### 对象的解构
- 作用：结构的分解处理
```js
let user = {name: "mystical", age: 18};
let {name, age} = user;
console.log(age);

// 函数的返回值也可以进行解构
function hd() {
    return {name: "mystical", age: 18};
}
let {name, age} = hd();
console.log(name, age);

// 外界传参的解构用法
function user({name, age}) {
    console.log(name, age);
}
user({name: "mystical", age: 12});

// 内置对象的解构
let {random} = Math; // 可以只解构部分属性或方法
console.log(random()); // 可以直接使用random

// 变量解构
let name = "mystical", url = "houdunren.com"
let opt = {name, url};
console.log(opt); // {name: "mystical", url: "houdunren.com"}
```
- 严格模式下的解构
```js
"use strict"
let {random} = Math // 正常运行
({random} = Math) // 严格模式下，报错
// 普通模式下，正常运行，不推荐
```
- 多层对象解构
```js
let hd = {
    name: "mystical",
    lesson: {
        title: "javascript"
    }
};
let {
    name,
    lesson: {title}
} = hd;
console.log(name, title); // mysical, javascript 成功解构
```

- 解构默认值实现配置项合并
```js
function createElement(options={}) {
    let {width = 200, height = 100, backgroundColor = "red"} = options;
    const div = document.createElement("div");
    div.style.width = width + "px";
    div.style.height = height + "px";
    div.style.backgroundColor = backgroundColor;
    document.body.appendChild(div);
}
createElement({width: 60, height: 30, backgroundColor: "green"});
```

- 函数参数的解构特性技巧
```js
function hd({name, age}){
    console.log(name, age);
}
hd({name: "mystical", age: 18});

// 解构和参数混合使用
function hd(name, {sex, age}){
    console.log(name, age);
}
hd("mystical", {sex: "male", age: 18}); // mystical male 18
```

### 属性的操作
```js
// 添加
let hd = {};
hd.name = "mystical";
hd["age"] = 18;

// 属性的删除
delete hd.name;
console.log(hd.name); // undefined

// 检测属性
console.log(hd.hasOwnProperty("name")); // false ,因为上面删除了
```

### 属性检测详解
```js
// 情况1：对象上检测
let arr = ["houdunren.com", "hdcms"];
console.log(arr);
console.log(arr.hasOwnProperty("length")); 
// true 只看自己，实例本身，不看原型(父级)
console.log(arr.hasOwnProperty("concat")); // false

console.log("concat" in arr); 检查整个原型链

// 简单介绍原型，可以看成是父级
let a = {name: "mystical"};
let b = {url: "houdunren.com"};
Object.setPrototypeOf(a, b);
// 将a设置为b的原型
console.log(a);
/*
    Object
        name: "mystical"
        [[Prototype]]: Object
        url: "houdunren.com"
        [[Prototype]]: bject
*/
console.log(a.hasOwnProperty("url")); // false
console.log("url" in a); // true
```
### 属性的计算和assign使用
```js
let id = 0;
let hd = {};
hd[`id-${++id}`] = id;
hd[`id-${++id}`] = id;
hd[`id-${++id}`] = id;
hd[`id-${++id}`] = id;
console.log(hd); // {id-1: 1, id-2: 2, id-3: 3, id-4: 4}

// assign 将两个对象进行合并
let hd = Object.assign({a: 1}, {b: 2});
console.log(hd) // {a: 1, b: 2}

// 实例
function upload(params) {
    let options = {
        size: 19999
    };
    options = Object.assign(options, params);
    console.log(JSON.stringify(options, null, 2));
}
upload({size: 99, type: "jpeg"});
```

### 遍历操作与DOM绘制
```js
let hd = {
    name: "mystical",
    year: 2010
};
console.log(Object.keys(hd));
// 获取所有的键 ["name", "year"]
console.log(object.values(hd));
// 获得所有的值 ["mystical", 2010]
console.log(object.entries(hd))
// 获得所有的键值，以数组的形式返回 [["name", "mystical"], ["year", 2010]]
```
- DOM绘制
```js
let lessons = [
    {name: "js", click: 999},
    {name: "node", click: 127}
];
let ul = document.createElement("ul"); // 创建DOM元素
for (const lesson of lessons) {
    let li = document.createElement("li");
    li.innerHTML = `课程：${lesson.name}, 点击数：${lesson.click}`; 
    // 向DOM添加内容
    ul.appendChild(li);
    // 将创建的DOM元素加入ul中
}
document.body.appendChild(ul); // 将创建的ul加入body
```

### 对象的复制（深浅拷贝）
```js
// 正常的对象复制是传址，一个对象的改变会影响另一个
// 通过循环遍历，赋值到新对象可以避免这个问题
let hd = {name: "msytical", url: "houdunren.com"};
let obj = {};
for (const key in hd) {
    obj[key] = hd[key];
}
obj.name ="yahoo";
console.log(hd) // hd无变化
console.log(obj) //仅obj发生改变 {name: "yahoo", url: "houdunren.com"}

// 听过assign实现复制新对象
let hd = {name: "msytical", url: "houdunren.com"};
let obj = Object.assign({},hd);

// 使用展开语法实现复制新对象
let hd = {name: "msytical", url: "houdunren.com"};
let obj = {...hd};
```
- 深拷贝多层次分析
```js
function deepcopy(obj) {
    if (obj === null) return null;
    let res = obj instanceof Array ? [] : {};
    for (const [k, v] of Object.entries(obj)) {
        res[k] = typeof v == "object" ? deepcopy(v) : v;
    }
    return res
}
```

### 使用工厂函数创建对象
```js
// 用于生成对象的工厂函数
function user(name) {
    return {
        name,
        show() {
            console.log(this.name + `-houdunren`);
        }
    };
}
let xj = user("mystical") // 生成对象{name: "mystical", func...}
// 使用工厂函数，可以统一对方法进行修改
```
### 通过构造函数创建对象
```js
function User(name) {
    this.name = name
    this.show = function(){
        console.log(this.name);
    };
    // 构造函数，不设return时，自动返回return
}
let xj = new User("mystical");
console.log(xj);
xj.show();
```