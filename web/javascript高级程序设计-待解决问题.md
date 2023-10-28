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
  ```js
  let x = 10;  // 分配内存，并存储值10
  x = 20;      // 重新为x分配内存，并存储新的值20
  ```

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

