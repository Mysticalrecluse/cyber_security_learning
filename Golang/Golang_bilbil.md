# Golang

## Go前置知识

Go语言特点

- 强类型静态语言
- 语法简单
- 垃圾回收
- 快速编译
- 简单的依赖管理
- 优秀的并发处理能力

## 变量

完整代码演示
```go
package main

// 引用fmt包
import (
    "fmt"
)

func main() {
    fmt.Println("Hello World")
}
```


### 整型
```go
package main

import (
    "fmt"
)

func main() {
    // 变量的声明
    var a int
    var b int
    var c int
    var age byte
    var gender bool
    var price float32
    var money float64

    // 变量的赋值
    a = 10
    b = 20
    c = a + b  // 30

    fmt.Println(c)

    // 未显式赋值的变量，其值为0

}
```

## if分支
```go
if a, b := 3, 8; b > a + 2 {
    fmt.Println("ok")
} else {
    fmt.Println("no")
}

// go常见if使用场景
if v, err:=ff(); err!=nil {
    // TODO
} 
```


## for循环（基本for循环）
```go
for m:=4; m < 10; m = m + 3 {
    fmt.Println(m)
}

// for后面什么都不跟，则恒为真
n := 2
for {
   n += 2 
   fmt.Println(n)
   if n > 12 {
        break;
   }
}
```

## 数组与切片
### 数组
#### 初始化数组
```go
// 数组的表示方法
var arr [5]int // 数组一定要指明长度和类型，且长度和类型指定后不可改变
// 数组初始化
var arr [5]int{2, 9, 7, 3, 5}
// 数组局部初始化
var arr [5]int{2, 9}  // 后3位默认为0
// 给前2个元素赋值
var arr = [5]int{3, 2}
// 给指定index赋值, 第3位是15，第5位是30，其他位为0
var arr = [5]int{2: 15, 4: 30}
// 根据{}里元素的个数，推断出数组的长度
var arr = [...]int {3, 2, 5, 6, 4}
```

#### 遍历数组
```go
// go语言中通过range遍历数组
for i, ele := range arr5 {
    fmt.Printf("index=%d, element=%d\n", i, ele)
}
// 类似其他语言中遍历
for i:=0; i < len(arr5); i++ {
    fmt.Printf("index=%d, element=%d\n", i, arr5[i])
}
```

### 切片
```go
// 切片定义，本质是一个结构体
// 该切片大小为3*8=24字节
type slice struct {
    array unsafe.Pointer  // 指向数组首地址的指针
    len int  // 已使用长度
    cap int  // 容量
}

// 切片初始化
arr := make([]int, 3, 5) // 这种写法表示初始创建的切片中，已有3个元素，3个元素都是0
arr := make([int, 3]) // 只有一个数值，表示该切片的长度和容量相等
// 工作中常见用法
arr := make([int, 0, 5]) // 表示长度为0，容量为5
```

- 重点：go语言中，不管是等号赋值还是函数传参，本质上都要发生拷贝

```go
arr:=make([]int, 3, 5) // 推荐用法
arr[0], arr[1], arr[2] = 2,9,7
brr := arr  // 这个过程中，brr相当于复制了一个arr的结构体，而其访问的数组还是同一个内存的数组

// 下面用法中，生成的切片长度容量都是0
arr := []int  // 也是生成切片的用法，但是不推荐
var arr []int  
```
```go
func slice_init() {
	var s []int
	fmt.Printf("len %d, cap %d\n", len(s), cap(s))
    s = []int{1,2,3,4,5} // 初始化，len=cap=5
}
// 这里len()和cap()是go语言中，少数可以直接使用的函数,不需要在前面指定包名
```

### 经典示例1
```go
arr := make([]int, 3, 5)
arr[0] = 2, arr[1] = 9, arr[2] = 7
append(arr, 8) // 这里的逻辑是在数组后面添加一个8，但是这里的arr，即结构体本身不变
brr := append(arr, 8) // 这里brr的len为4，arr的len依旧为3
brr = append(brr, 8)
brr = append(brr, 8) // 此时数组需要扩容，也就是在此之后，arr和brr所指的底层数组不再是一个，因为切片扩容，本质上是拷贝出一个新的内存地址
```

##