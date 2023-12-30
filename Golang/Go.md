# Golang简介
## Golang应用领域
### 区块链应用
- 区块链技术，简称BT，也称之为<font color=tomato>分布式账本技术</font>，是一种互联网数据库技术，其特点是去中心化、公开透明，让每个人均可参与数据库记录

### 后端服务器应用
- 美团后台流量支撑程序
  - 支撑主站后台流量（排序，推荐，搜索等），提供负载均衡，cache，容错，按条件分流，统计运行指标（qps, latency）等功能

### 云计算/云服务后台应用
- 盛大云CDN
  - 应用范围：CDN的调用系统，分发系统、监控系统、短域名服务、CDN内部开放平台、运营报表系统以及其他一些小工具等

- 京东消息推送云服务/京东分布式文件系统
  - 应用范围：后台所有服务全部用go实现 

## Go语言概述
### Go的语言特点
- Go语言的每一个文件都要属于一个包，而不能单独存在
```go
package main // 特点2：一个go文件需要再一个包中

import "fmt"  // 引包

//go语言的指针使用特点
func testPtr(num *int) {
    *num = 20
}

func sayOk() {
    fmt.println("ok")
}
```

- 垃圾回收机制，内存自动回收，不需要开发人员管理

- <font color=tomato>天然并发（重要特点）</font>
  - 从语言层面支持并发，实现简单
  - goroutine, 轻量级线程，可实现大并发处理，高效利用多核
  - 基于CPS并发模型(Communicating Sequential Processes)实现

- 管道通信机制channel
  - 可以实现不同的goroute之间的相互通信

- 函数返回多个值
```go
// 写一个函数，实现同时返回和，差
// go函数支持返回多个值
func getSumAndSub (num1 int, num2, int) (int，int) {// 返回值列表 

    sum := n1 + n2 // go语句后面不带分号，编译器编译的时候，自动加分号
    sub := n1 - n2
    return sum, sub
}
```

- 新的创新：切片slice、延时执行defer等

## Go语言开发环境搭建
### 安装和配置SDK
- SDK：软件开发工具包
  - 安装网址：https://go.dev/

- 配置环境变量
  - GOROOT 指定SDK的安装路径 d:/~/go
  - Path 指定SDK的/bin目录
  - GOPATH 工作目录，将来我们的go项目的工作路径

- Linux安装
  - 64位系统：go1.9.2linux-amd64.tar.gz
  - SDK安装目录建议：/opt目录下
  - 安装时，解压即可，使用的是tar.gz
  ```
  tar -zxvf go1.~.tar.gz
  ```
  - Linux下配置环境变量
  ```
  /etc/profile文件下添加三条语句

  export GOROOT=/opt/go
  export PATH=$PATH:$GOROOT/bin
  export GOPATH=$HOME/goprojects
  ```

- Mac下配置环境变量
```shell
su root

# 输入密码后：
vi /etc/profile
将环境配置的文本写到末尾，同linux
```

### 开发步骤
- 开发程序项目时，go的目录结构
```
goproject/src/go_code/project01/main
goproject/src/go_code/project01/package - 一个文件夹对应一个包
```

- 代码示例
```go
// 表示hello.go文件所在的包是main, 
//在go中，每个文件必须归属于一个包
package main

// 表示引入一个包名为fmt的包
// 引入该包后，就可以使用fmt包的函数
import "fmt"

// func是关键字，表示后面是一个函数
// main是函数名，表示主函数，即程序的入口 
func main() {
	fmt.Println("Hello World!")
}
```

- 通过go build命令对该go文件进行编译，生成.exe文件

- 在dos命令行下，执行.exe文件就可以看到运行效果

- 通过go run命令可以直接执行hello.go程序（类似执行一个脚本程序）

### 编译和运行
- 指定生成的二进制文件名
```
go build -o <filename>.exe  // 后缀必须是exe
```

### Go程序开发注意
- Go语言严格区分大小写

- Go方法由一条一条语句构成，每个语句不需要分号（Go语言会在每行自动加分号），这也体现出Golang的简洁性

- Go编译器是一行行进行编译的，因此我们一行就写一条语句，不能把多条语句写在同一行，否则报错

- go语言定义的变量或者import的包如果没有使用到，代码不能编译通过

- 正确的缩进
```
gofmt -w <filename>
```

- 运算符两边习惯性各加一个空格
```
eg: 2 + 3 * 4
```

- 一行最长不超过80个字符，超过的请用换行展示，尽量保持格式优雅
```go
package main
import "fmt"
func main() {
    fmt.Println("HelloWorldHelloWorldHelloWorldHelloWorldHelloWorld",
        "HelloWorldHelloWorldHelloWorldHelloWorldHelloWorldHelloWorld",
        "HelloWorldHelloWorldHelloWorldHelloWorldHelloWorldHelloWorld",
        "HelloWorldHelloWorldHelloWorldHelloWorldHelloWorldHelloWorld",
        "HelloWorldHelloWorldHelloWorldHelloWorldHelloWorld")
} // 超长字符换行展示，用逗号拼接
```

# Go基础语法
## 变量
### 定义声明变量
```go
package main
import "fmt"
func main() {
    // 定义变量/声明变量
    var i int
    // 给i赋值
    i = 10
    // 使用变量
    fmt.Println("i=", i)
}
```

### 输出api
- Println():
  - 操做数之间自动添加一个空格，并在最后附加换行符
- Printf():
  - 和C语言用法相同

### Golang变量的三种使用方式
- 指定变量类型，声明后不赋值，则使用默认值
```go
package main
import "fmt"
func main() {
    // golang的变量使用方式1
    // 第一种，指定变量类型，声明后若不赋值，使用默认值
    // int 的默认值为0
    var i int
    fmt.Println("i=", i) // i= 0

    // 第二种，根据值自行判断变量类型（类型推导）
    var num = 10.11 // num自动为浮点型

    // 第三种使用方式
    // 省略var，注意 :=左侧的变量不应该是声明过的，否则会导致编译错误
    // := 冒号不能省略
    name := "tom" // num = "tom", 没声明就赋值，报错
}
```

### 多变量声明
```go
package main
import "fmt"

// 一次性声明并赋值多个全局变量
var (
    n4 = 300
    n5 = 900
    name2 = "mary"
)

func main() {
    // 演示golang如何一次性声明多个变量
    var n1, n2, n3 int
    fmt.Println("n1=", n1, "n2=", n2, "n3=", n3)

    // 一次性声明多个变量方式2
    var a1, name, a2 = 100, "tom", 888 // 对应赋值
    fmt.Println("a1=", a1, "name=", name, "a2=", a2)

    // 方式3
    var b1, b2, b3 := 100, "tom", 888 // 对应赋值
    fmt.Println("b1=", b1, "b2=", b2, "b3=", b3)

    fmt.Println("n4=", n4, "n5=", n5, "name2=", name2)
}
```

## 数据类型
### 数据类型的分类
- 基本数据类型
  - 数值型
    - 整数类型（int, int8, int16, int32(rune), int64, uint..., byte）
      - rune可以用来存放中文字符
    ```
    rune和int32的区别

    在Go语言中，rune 是 int32 的别名。它们在内存中占用的空间和表示的数值范围是一样的。然而，rune 在语义上用于表示一个Unicode码点，而 int32 是一个普通的整型。这意味着当你看到 rune 类型时，可以理解为它被用来处理字符（尤其是Unicode字符），而 int32 则是用来进行一般的整数运算。尽管它们在技术上是相同的，但这种语义区别有助于开发者更好地理解代码的用途和意图。
    ```
      - int所占大小和操做系统有关，32位占4字节，64位占8字节
      - byte和unit8等价，当存储字符是，选用byte
    - 浮点类型（float32, float64）
      - Golang的浮点类型，默认float64
  - 字符型（没有专门的字符型，使用byte来保存单个字母字符）
    - Golang的字符串由字节组成
    ```
    在Go语言中，字符串实际上是一个字节的切片。当存储汉字或其他多字节字符时，Go语言会按照每个字符所需的字节进行存储。例如，使用UTF-8编码，一个汉字可能占用多个字节。Go语言在内部将这些字节串联起来，形成一个连续的字节序列来表示整个字符串。因此，一个字符串在Go语言中可能由不同长度的字节序列组成，这取决于它包含的字符
    
    tips: 字节序列的概念
    在计算机科学中，"字节序列"是指一连串的字节（bytes），它们按照特定的顺序排列以表示数据。每个字节由8位（bit）组成，可以存储一个数值（通常是0到255）。

    在C语言中，字符串的处理与Go语言有所不同。C语言中的字符串通常是以单字节字符组成的数组，并以特殊的空字符（'\0'）结束。这意味着在原生C语言中，每个字符（包括汉字）通常被视为一个单字节。然而，由于汉字不能用一个单字节表示，所以在C语言中处理汉字时通常需要依赖于特定的编码方案（如GBK或UTF-8），这些编码方案使得一个汉字可能占用多个字节。但在这种情况下，C语言的字符串处理并不是原生支持的，需要额外的处理和转换 
    ```
  - 布尔型（bool）
  - 字符串（string）


- 派生/复杂数据类型
  - 指针（Pointer）
  - 数组
  - 结构体 (struct) 
  - 管道 (Channel)
  - 函数
  - 切片 (slice)
  - 接口 (interface)
  - map

### 查看数据类型的方法
- 使用fmt.Printf()格式化输出得到数据类型
```go
package main
import "fmt"
func main() {
    n1 := 100
    fmt.Printf("n1's type is %T", n1)
}
```

- unsafe.Sizof(n1) 是unsafe包的一个函数，可以返回n1变量占用的字节数 
```go
package main
import (
    "fmt"
    "unsafe"
)
func main() {
    n1 := 100
    fmt.Printf("n1's type is %T", n1)
    fmt.Printf("n1's type is %T, and byte is %d", n1, unsafe.Sizeof(n1))
}
```