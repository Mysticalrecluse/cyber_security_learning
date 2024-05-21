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