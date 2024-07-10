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

## switch
```go
func break_switch() {
    for i := 0; i < 8; i++ {
        switch i {
            case 4:
                break // 想退出for得用Label
            default:
                fmt.Println(i)
        }
    }
}

// 示例2
func switch_type() {
    var num interface{} = 6.5
    switch num.(type) { // 获取interface的具体类型。.(type)只能用在switch后面
    case int:
        fmt.Println("int")
    case float32:
        fmt.Println("float32")
    case float64:
        fmt.Println("float64")
    case byte:
        fmt.Println("byte")
    default:
        fmt.Println("neither")
    }
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

#### 指针数组与数组指针
判别数组指针和指针数组的方法，看*标记在哪里
```go
// 传数组的指针 
func update_array2(arr *[5]int) {
    fmt.Prinf("array in function, address is %p\n", &((*arr)[0]))
    arr[0] = 888
}

// 传指针构成的数组
func update_array3(arr [5]*int) {
    *arr[0] = 888
}
```

#### 数组的截取
```go
array := [...]int{1,2,3,4,5}
brr := array[2:4] // 截取数组，得到切片， 这里的重点是得到的切片扩容
brr := array // 这种情况下，arr是数组，brr也是数组
brr := array[:] // 这种情况下，arr是数组，brr是切片， 只不过是截取全部
crr := brr[1:2:4] // len=2-1, cap=4-1
// 这里1:2表示截取的元素是第2个，4表示当前截取后的容量是4-1
```
补充说明：arr[a:b:c] 表达式中的切片容量是从索引 a 到索引 c 的长度。这意味着切片的容量将等于 c - a。
具体来说：
- a 是切片的起始索引（包含）。
- b 是切片的结束索引（不包含）。
- c 是切片的容量上限（从起始索引 a 开始计算）

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
### 切片作为函数参数
```go
// go语言函数传参，传的都是值，即传切片会把切片的{arrayPointer, len, cap}这3个值拷贝一份传进来
// 由于传的是底层数组的指针，所以可以直接修改底层数组里的元素
func update_slice(s []int) {
    s[0] = 888
}

// 切片指针作为传参
// 向尾部添加一个元素
func appendEle(s *[]int) {
    *s = append(*s, 9)
}

// 情况2
// 这种情况下，切片传进函数，但是函数结束后，切片未发生改变
func appendEle(s []int) {
    s = append(s, 9) // 底层指针指向的数组增加了一个9，但是函数过后切片长度不变
}
```

### 切片的遍历
```go
// 遍历slice, 本质是遍历底层的数组，而这个数组在一开始就固定了下来，即使切片动态改变，for range遍历的目标数组也不变
func iter_slice() {
    s := make([]int, 4, 5)
    for i, ele := range s {
        fmt.Printf("i=%d ele=%d\n", i, ele)
    }
    fmt.Printf("len=%d, cap=%d\n", len(s), cap(s)) // len=4, cap=5
    fmt.Println(strings.Repeat("-", 50))

    // 遍历的时候添加元素，for range遍历的范围不受影响
    for i, ele := range s {
        fmt.Printf("i=%d ele=%d\n", i, ele)
        // 依次输出0,3,0,0
        if i == 0 {
            s = append(s, 1)
            s[1] = 3
        }
    }
    fmt.Printf("len=%d, cap=%d\n", len(s), cap(s)) // len=5, cap=5
    fmt.Println(strings.Repeat("-", 50))

    // 遍历的时候减少元素，for range遍历的范围不受影响
    for i, ele := range s {
        fmt.Printf("i=%d ele=%d\n", i, ele)
        // 依次输出：0, 4, 0, 0, 1
        if i == 0 {
            s[1] = 4
            s = s[3:]
        }
    }
    fmt.Printf("len=%d, cap=%d\n", len(s), cap(s)) // len=2, cap=2
    fmt.Println(strings.Repeat("-", 50))

    // 遍历的时候发生扩容，切片指向新的数组，for range遍历的还是老数组
    for i, ele := range s {
        fmt.Printf("i=%d ele=%d\n", i, ele)
        // 依次输出0,1
        if i == 0 {
            s = append(s, 1)
            s[1] = 5 // 发生了扩容，新数组下标2的元素变为5，但是老数组不变，因此遍历的时候，初始阶段，数组就已经固定下来了, 遍历的就是老数组，新申请的内存上的改动不会影响老数组的遍历
        }
    }
    fmt.Printf("len=%d, cap=%d\n", len(s), cap(s)) // len=3, cap=4
    fmt.Println(strings.Repeat("-", 50))
}
```

### 数组和切片区别总结
- 数组长度固定，切片可以通过append()，长度不断增加，但是增加到超过容量，会发生扩容，扩容的本质是申请一个新的内存空间


## 字符串
### 字符串特性

字符串与切片的区别
- 不可变性：
  - 字符串是不可变的。这意味着一旦创建，字符串的内容不能被修改。而 []byte 切片是可变的。
- 只读访问：
  - 字符串在内存中是只读的，而 []byte 切片是可读可写的。

#### 总结
由于字符串是不可变的，任何对字符串的修改都会创建一个新的字符串，而不会改变原有的字符串。

### 字符串的底层实现
```go
package main

import (
	"fmt"
	"unsafe"
)

// 模拟 Go 语言中的字符串实现
type StringHeader struct {
	Data uintptr
	Len  int
}

func main() {
	// 创建一个字符串
	str := "hello, world"
	
	// 获取字符串的底层实现
	strHeader := (*StringHeader)(unsafe.Pointer(&str))
	
	// 打印字符串的底层信息
	fmt.Printf("String: %s\n", str)
	fmt.Printf("Data: %x\n", strHeader.Data)
	fmt.Printf("Length: %d\n", strHeader.Len)
	
	// 将字符串转换为 []byte
    // 这里的底层实现：
    // 为新的 []byte 切片分配内存。这个内存的大小与字符串的长度相同，因为每个字符在 UTF-8 编码中占用一个或多个字节。
    // 数据复制：将字符串中的字节数据复制到新分配的 []byte 切片中。
	byteSlice := []byte(str)
	
	// 修改字节切片
	byteSlice[0] = 'H'
	
	// 将修改后的 []byte 转换回字符串
	newStr := string(byteSlice)
	
	// 打印新的字符串
	fmt.Printf("Modified string: %s\n", newStr)
}
```

### 反引号
```go
func asign_string() {
    s1 := "He say: \" i'm fine. \" \n \\Thank\tyou." // 包含转义字符
    s2 := `here is first line.
    
    there is third line
    ` // 反引号里的转义字符无效，反引号里的原封不动地输出，包括空白符和换行符
}
``` 

### 字符串拼接
```go
func string_join() {
    s1 := "Hello"
    s2 := "how"
    s3 := "are"
    s4 := "you"
    merged := s1 + " " + s2 + " " + s3 + " " + s4 // 方法1
    fmt.Println(merged)
    merged = fmt.Sprintf("%s %s %s %s", s1, s2, s3, s4) // 方法2
    fmt.Println(merged)
    merged = strings.join([]string{s1, s2, s3, s4}, " ") // 方法3
    fmt.Println(merged)
    // 当有大量的string需要拼接时，用strings.Builder效率最高
    sb := strings.Builder{}
    sb.WriteString(s1) // 方法4
    sb.WriteString(" ")
    sb.WriteString(s2)
    sb.WriteString(" ")
    sb.WriteString(s3)
    sb.WriteString(" ")
    sb.WriteString(s4)
    sb.WriteString(" ")
    merged = sb.String()
    fmt.Println(merged)
}
```


## Rune类型
### rune的本质
在GO语言中，rune 是一个特殊的数据类型，用于表示 Unicode 代码点。rune 本质上是一个别名，定义如下：
```go
type rune = int32
```
这意味着 rune 实际上是一个 32 位的整数，能够表示所有的 Unicode 代码点。每个 Unicode 代码点表示一个字符，包括 ASCII 字符和其他语言的字符。

### rune的原理
rune 主要用于处理 Unicode 字符。Unicode 是一种字符编码标准，能够表示几乎所有语言的字符。每个字符都有一个唯一的代码点。因为 Go 语言的字符串是 UTF-8 编码的字节序列，直接操作字符串可能会复杂且容易出错，尤其是在处理多字节字符时。因此，rune 提供了一种更方便、更安全的方式来处理单个 Unicode 字符。

### rune和字符串的关系
```go
package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	// 一个包含多字节字符的字符串
	str := "Hello, 世界"

	// 遍历字符串中的每个字符，默认使用 rune类型
	for i, r := range str {
		fmt.Printf("Index: %d, Rune: %c, Unicode: %U\n", i, r, r)
	}

	// 获取字符串中的 rune 切片
	runes := []rune(str)
	fmt.Println("Runes:", runes)

	// 将 rune 切片转换回字符串
	newStr := string(runes)
	fmt.Println("New String:", newStr)

	// 计算字符串的长度（以字符为单位）
	fmt.Println("Length (runes):", utf8.RuneCountInString(str))
}

```

## 结构体
```go
type Human struct {
    Age int
    Height float32
    Sex bool
}

func main() {
    var a Human
    // 结构体赋值
    a = Human{Age:18, Height: 1.80, Sex: false}
    // a = Human{18, 1.80, false} 与上面等价 
    // 简写：a:=Human{18, 1.80, false}
    // 变量的使用
    fmt.Printf("%d %.2f %t", a.Age, a.Height, a.Sex)
    // 直接输出结构体
    fmt.Printf("%v\n", a) // {18 1.80 false}
    fmt.Printf("%+v\n", a) // 更加详细 {Age:18, Height:1.80, Sex:false}
    fmt.Printf("%#v\n", a) // 更更加详细 main.Human{Age:18, Height:1.80, Sex:false}
}
```

### 结构体方法的定义
在Go中，方法是通过在函数定义时指定接受者来定义的。接受者可以是结构体类型，也可以是其他类型
```go
// 定义一个结构体
type Mystruct struct {
    value int
}

// 定义一个方法，接收者是Mystruct
// Display方法有一个接受者`Mystruct`，它是值接收者。
// 这意味着在方法内部对接收者的修改将不会影响原结构体
func (m Mystruct) DisplayValue() {
    fmt.Println("Value:", m.value)
}

// 定义一个方法，接收者是Mystruct的指针
// SetValue方法有一个接收者`*Mystruct`，它是指针接收者
// 这意味着方法内部对接受者的修改会影响原结构体
func (m *Mystruct) SetValue(newValue int) {
    m.value = newValue
}
```

### 深入了解方法接受者工作机制

值接收者与指针接收者
- 值接收者：当方法的接收者是一个值（例如`Mystruct`），方法在调用时会接收这个值的副本。对这个副本进行的任何修改不会影响到原始的结构体实例

- 指针接收者：当方法的接收者是一个指针（例如`*Mystruct`），方法在调用时会接收这个指针的副本。通过这个指针对结构体进行的任何修改都会直接影响到原始的结构体实例

#### 示例代码
```go
package main

import "fmt"

// 定义一个结构体
type MyStruct struct {
	value int
}

// 值接收者方法
func (m MyStruct) DisplayValue() {
	fmt.Printf("Inside DisplayValue: %p, %v\n", &m, m.value)
	m.value = 20 // 尝试修改
}

// 指针接收者方法
func (m *MyStruct) SetValue(newValue int) {
    // 这里使用m.value, 而不是(*m).value原因在于
    // 自动解引用：
    // Go编译器在处理指针接收者的方法时，自动解引用指针以简化语法，也就是说
    // 当你写`m.value`，编译器实际执行的是`(*m).value`
	fmt.Printf("Inside SetValue: %p, %v\n", m, m.value)
	m.value = newValue // 修改结构体的字段值
}

func main() {
	myStruct := MyStruct{value: 10}

	// 调用值接收者方法
	fmt.Printf("Before DisplayValue: %p, %v\n", &myStruct, myStruct.value)
    // Before DisplayValue: 0xc00000e028, 10
	myStruct.DisplayValue()
    // Inside DisplayValue: 0xc00000e040, 10
	fmt.Printf("After DisplayValue: %p, %v\n", &myStruct, myStruct.value)
    // After DisplayValue: 0xc00000e028, 10

	// 调用指针接收者方法
	fmt.Printf("Before SetValue: %p, %v\n", &myStruct, myStruct.value)
    // Before SetValue: 0xc00000e028, 10
	myStruct.SetValue(30)
    // Inside SetValue: 0xc00000e028, 10
	fmt.Printf("After SetValue: %p, %v\n", &myStruct, myStruct.value)
    // After SetValue: 0xc00000e028, 30
}

```

### 方法的实现
当你调用结构体的方法时，Go编译器会自动将接收者作为第一个参数传递给方法。其幕后等同于以下函数
```go
func DisplayValue(m MyStruct) {
	fmt.Println("Value:", m.value)
}

func SetValue(m *MyStruct, newValue int) {
	m.value = newValue
}
```

#### 完整定义与实现示例
```go
package main

import "fmt"

// 定义一个结构体
type MyStruct struct {
	value int
}

// 定义一个方法，接收者是 MyStruct
func (m MyStruct) DisplayValue() {
	fmt.Println("Value:", m.value)
}

// 定义一个方法，接收者是 MyStruct 的指针
func (m *MyStruct) SetValue(newValue int) {
	m.value = newValue
}

func main() {
	// 创建一个 MyStruct 实例
	myStruct := MyStruct{value: 10}

	// 调用 DisplayValue 方法
	myStruct.DisplayValue() // 输出: Value: 10

	// 调用 SetValue 方法
	myStruct.SetValue(20)

	// 再次调用 DisplayValue 方法
	myStruct.DisplayValue() // 输出: Value: 20
}

```

## 接口
```go
package main

import (
    "fmt"
)

// 接口的本质是一组行为规范的集合
type Human interface {
    // 接口中定义函数
    Say(int, int) int
    //Think(string) (string,err) 

}

// 这里定义一个空接口，则任何结构体都实现Human2
type Human2 interface {

}

func foo(h Human) {
    c:=h.Say(3, 6)
    fmt.Println("c=", c)
}

func main() {
    // 这里
    var a Human
    var b interface{} // 这里interface{}这个组合表示一个类型
    var c string
    b=c // 因为b是空接口的,所以任何类型都可以是b的实现

    t:=Tom{}
    a=t

    j:=Jim{}
    a=j

    foo(a)
}

type Tom struct{
}

func (Tom)Say(a int, b int) int {
    return a-b
}

type Jim struct{
}

func (Jim)Say(a int, b int) int {
    return a+b
}
```

## map

### map基本使用

```go
// map的声明
var m map[string]int // string是key的类型，int是value的类型
// 任何类型都可以是value
// 大部分类型可以用作key，但是函数不行
m = make(map[string]int, 100)  // 和切片一样，使用make对内存进行申请
// 100表示该map中最多包含100个键值对，超过会发生扩容，影响性能

// 初始化的同时赋值
m = map[string]int{"a":3, "b":5}
// 向map实例中添加值
m["c"] = 9

// 修改map中的值
m["a"] = 4

// 删除map实例中的key
delete(m, "a")
fmt.Println(m["a"]) // 返回0
// 这里有个问题，就是明明删掉了key，但还是能返回值，虽然是0
// 在Go语言中，如果map中某个键不存在，则它对应的value为该类型的0值

// 改进写法
if v, exists:=m["a"]; exists {
    fmt.Println(v)
} else {
    fmt.Println("map中不存在a这个key")
}
```

### map常见用法——判断值是否存在
```go
arr := []int{1, 2, 3}
mp := map[int]bool{1:true, 2:true, 3:true}
for _, k := range  arr{
    if _, exists := mp[k]; exists {
        fmt.Printf("%d,it's exists\n",k)
    }
}
```

### map的遍历
```go
m := map[string]int{"a": 1, "b": 2}
// 使用for range
// 遍历的时候无序
for k, v range m {
    fmt.Printf("k: %v, v: %v", k, v)
}
```

## 单元测试与基准测试
单元测试的目的：
- 证明一段函数，它的逻辑是正确的
### 单元测试

- 文件名称必须以`_test.go`结尾
- 函数名必须以`Test`开头
- 函数参数必须是`*testing.T`
```go
package main

import (
    "fmt"
    "encoding/json"
    "github.com/bytedance/sonic"
    "testing"
)

type Student struct {
    Name string
    Age int
    Gender bool
}

type Class struct {
    Id string
    Students []Student
}

var(
    s=Student{"张三", 18, true}
    c=Class{
        Id: "1(2)班"，
        Students: []Student{s,s,s}
    }
)
func TestJson(t *testing.T) {
    bytes,err := json.Marshal(c)
    if err!=nil{
        t.Fail()
    }
    var c2 Class
    err=json.Unmarshal(bytes,&c2)
    if err!=nil{
        t.Fail()
    }
    if !c.Id==C2.Id && len(c.Students)==len(c2.Student) {
        t.Fail()
    }
    fmt.Println("json没毛病")
}
```

### 运行单元测试
```shell
go test json_test.go -v -run=^TESTJson$

# 选项
-v    # 使得println正常输出
-run  # 后跟正则表达式，指定要运行的函数
```


### 基准测试（性能测试）
- 文件名以`_test.go`结尾
- 函数名以`BenchMark`开头
- 函数参数为`b *testing.B`

```go
// 基准测试
func BenchMark(b *testing.B) {
    for i:=0; i<b.N; i++ { // N是一个很大的值，系统随机根据运行时间指定
        bytes,err := json.Marshal(c)
        var c2 Class
        json.Unmarshal(bytes,&c2)
        fmt.Println("json没毛病")
    }
}
```

### 运行基准测试
```shell
go test -bench=Json json_test.go

# 选项
-bench  # 指定测试的函数
-benchmem # 测试每次运行的内存申大小，以及运行时申请的内存次数
```

## defer

- 这里注意defer的两个过程
    - defer的注册
    - defer的执行

```go
package main

import (
    "fmt"
)

func foo() int {
    a, b:=3, 5
    c := a + b
    defer fmt.Println("111", c) // defer的注册, 输出111 8
    fmt.Println(c)
    defer fmt.Println("222", c) // 如果defer后面跟的是go语句，而不是函数，则变量在注册的时候就已经计算好了，此时值已固定
    defer func() {
        fmt.Println("333", c) // 输出333 100
        // 如果defer后面跟的是一个匿名函数，函数体里涉及的变量是defer执行的时候才去计算的
    }()
    c = 100
    return c
}

func main() {
    foo()
    // 输出 8， 222， 111 ，defer后注册的先执行
}
```


## 接口

```go
package main

import (
    "fmt"
)

type Human interface{
    // 结构体与接口的区别
    // 结构体里定义的是成员变量，而接口中定义的是函数 
    // 接口的本质是一组行为规范的集合
    // 接口是一组行为规范的集合
    Say(int, int) int
    Think(string) (string, error)
}

func foo(h Human) {
    c := h.Say(3, 6)
    fmt.Println("c=",c)
}

func main() {
    var a Human

}
```


## 依赖管理

项目目录结构
```shell
golang_test_project/
├── go.mod
├── go.sum
├── main
│   └── d.go
└── util
    ├── a.go
    └── math
        ├── b.go
        └── c.go

3 directories, 6 files
# 上述目录结构，文件依赖关系如下
c.go -> 调用 -> b.go
d.go(入口main函数) -> 调用 -> a.go, c.go, 第三方库
```

### 创建go.mod

在项目目录golang_test_project下，使用`go mod init <mod名称>`初始化项目, 执行此命令后，该目录下会生成一个go.mod的文件
```shell
go mod init g6
```

- go.mod
```go
module g6  // g6是模块的名称，将来所有依赖都会依赖于模块的名称

go 1.22.3  // go的版本
```

- b.go
```go
// 同一目录下的go文件，package名称必须保持一致
// 包的名称和目录的名称没有必然关系，可以不一致
package maths

// 小写开头的函数(变量)，尽在本包内可见
func sub(a,b int) int {
    return a - b
}
```
- c.go
```go
package maths

// 大写开头的函数(变量)可以在其他包调用，是可见的
func Add(a,b,c int) int {
    return a + sub(b, c)
}
```
- a.go
```go
package util

var (
    Name="大脸猫"
)

func Add(a,b int) int{
    return a+b
}
```

- d.go(程序入口)
```go
package main // 入口函数包名和函数名必须叫main,目录名和文件名可以不叫main

import (
    "fmt"
    "g6/util" // MODLUE名称/目录名称
    math "g6/util/math"
    "github.com/bytedance/sonic" // 要使用第三方库，需要将第三方库放入go.mod文件中
)

func main() {
    a, b, c := 1, 2, 3
    fmt.Println(util.Name) // 这里uil是包名和目录名无任何关系
    fmt.Println(util.Add(a,b))
    fmt.Println(math.Add(a, b, c))
    bytes,_:=sonic.Marshal("hello")
    fmt.Println(string(bytes))
}
```

#### 将第三方库放入go.mod
- 方法1
```shell
# 执行go get
go get github.com/bytedance/sonic           
go: downloading github.com/bytedance/sonic v1.11.9
go: downloading github.com/cloudwego/base64x v0.1.4
go: downloading golang.org/x/arch v0.0.0-20210923205945-b76863e36670
go: downloading github.com/bytedance/sonic/loader v0.1.1
go: downloading github.com/klauspost/cpuid/v2 v2.0.9
go: downloading github.com/twitchyliquid64/golang-asm v0.15.1
go: downloading github.com/cloudwego/iasm v0.2.0
go: added github.com/bytedance/sonic v1.11.9
go: added github.com/bytedance/sonic/loader v0.1.1
go: added github.com/cloudwego/base64x v0.1.4
go: added github.com/cloudwego/iasm v0.2.0
go: added github.com/klauspost/cpuid/v2 v2.0.9
go: added github.com/twitchyliquid64/golang-asm v0.15.1
go: added golang.org/x/arch v0.0.0-20210923205945-b76863e36670

# 执行go get之后，
cat go.mod
module g6

go 1.22.3

require (
        github.com/bytedance/sonic v1.11.9 // indirect
        github.com/bytedance/sonic/loader v0.1.1 // indirect
        github.com/cloudwego/base64x v0.1.4 // indirect
        github.com/cloudwego/iasm v0.2.0 // indirect
        github.com/klauspost/cpuid/v2 v2.0.9 // indirect
        github.com/twitchyliquid64/golang-asm v0.15.1 // indirect
        golang.org/x/arch v0.0.0-20210923205945-b76863e36670 // indirect
)
```


#### 注意1:

- 同一个目录下面的package名称必须一致【包的名称和目录的名称可以不同,比如上述目录是math，包名却还maths】
- 同一个目录下面，这些go文件属于同一个package，同一个package内部，可以自由随意的互相调用
- 大写开头的函数，可以在其他的package里调用，小写开头的函数仅在本包内可见
- 同理，大写开头的全局变量，可以在其他package使用，小写开头的全局变量，仅在本包内可用


## 函数
### 基本格式
```go
func return1(a, b int) int {
    a = a + b
    c := a // 声明并初始化一个变量c
    return c // 函数返回，return后面的语句不会再执行
}
```
### 函数格式2
```go
func return2(a, b int) (c int) {// 返回变量c已经声明好了
    a = a + b
    c = a //可以直接使用c，不要再次声明
    return  // 此处必须显式写return
    // return c 这里写c也ok
}
```

### 不定长参数
```go
func variable_length_arg(a int, other ...int) int {
    // 调用该函数时，other可以对应0个参数也可以对应多个参数
    sum := a
    // 不定长参数实际上是slice类型
    for _, ele := range other {
        sum += ele
    }
    if len(other) > 0 {
        fmt.Printf("first ele %d len %d cap %d\n", other[0], len(other, cap(other)))
    } else {
        fmt.Printf("len %d cap %d\n", len(other), cap(other))
    }
}
```
- 调用varable_length_arg
```go
func main() {
    variable_length_arg(1)
    variable_length_arg(1, 2)
    variable_length_arg(1, 2, 3)
    slc := []int{4,5,6}
    variable_length_arg(1, slc...)
    // 将一个切片传递给一个接受不定长参数的函数时，确实需要在切片后面加上 ... 来展开切片。这种用法允许你将切片的元素逐一传递给函数，而不是将整个切片作为一个单独的参数传递。
}
```

### 总结`...``的三种用法
- 数组
```go
arr := [...]int{1, 2, 3}
```
- 不定长参数
```go
func test (a int, other ...int) int {}
```

- 将一个切片传递给不定长参数
```go
slc := []int{1,2,3}
test(4, slc...)
```

### 函数类型的变量
```go
// FV是一个函数类型的变量
var FV = func(arg int) {
    fmt.Printf("%d la %d\n", arg, 2*arg)
}
FV(3)

// FT是一种类型(FT没有成员变量)
type FT func(arg int)

// 类型可以有自己的成员方法
func (ft FT) Hello (arg int) {
    ft(arg)
}

// 类型可以实现接口
type IFC interface {
    Hello(arg int)  // 此时FT就实现了Hello()
}

// 因此ft就可以赋值给IFC类型的变量

// 类型之间的继承
type byte = uint8  // 表示这两个类型完全等价

type uintptr uintptr // 表示左边的类型是基于右边的类型发展的
// 右边类型的功能，左边都有，而且左边还可以有自己的额外功能
```

### 参数是函数
```go
func funcCallBack(f func(arg int), arg int) {
    f(arg)
}
```

### 参数是接口
```go
func funcInterface(i IFC, arg int) {
    i.Hello(arg)
}
// 所有实现该接口的类型都可以作为参数传进来，比如
```

### 闭包函数
```go
func g1() func() {
    a := 1
    g2 := func() {
        a++
        fmt.println(a)
    }
    return g2
}
```

### 回调函数


## 异常处理
如果一个函数内可能出现异常，建议在参数最后添加error参数，做异常处理
常见异常
- 除零异常
- 数组溢出
  
```go
// 递归实现所有参数乘积的倒数
// error一般作为最后一个返回值
func div(args ...float64) (float64, error) {
    if len(args) == 0 {
        //return 0, errors.New("divide by zero")
        return 0, fmt.Errorf("divide by zero %s %d", "abc", 4)
    }
    first := args[0]
    if first == 0 {
        return 0, errors.New("divide by zero")
    }
    if len(args) == 1 {
        return 1 / first, nil
    }
    remain := args[1:]
    res, err := div(remain...)
    if err != nil {
        return 0, err
    } else {
        return 1 / first * res, nil
    }
}
```


### error类型
error本质上是一个接口
```go
type error interface {
    Error() string
}

func (e *errorString) Error() string {
    return e.s
}
```

`errors.New()`解析
```go
package errors

func New(text string) error {
    // 这里是返回一个结构体
    return &errorString{text}
}

// errorStrings是一个结构体
type errorString struct {
    s string
}

```


## 补充
### panic()用法
panic()的作用：
- 立即停止函数执行
```go
func defer_exe_time() (i int) {
    i = 9
    defer func() {
        fmt.Printf("first i=%d\n", i)
    }()
    defer func(i int) {
        fmt.Printf("sencond i=%d\n", i)
        panic("zcy")
    }
    defer fmt.Printf("third i = %d\n", i) 

    return 5
}

// 执行后输出
/* 
   third i = 9
   second i = 9
   first i = 5
   panic: zcy

   goroutine 1 [running]:
   main.defer_exe_time.fun2(0x32f2e8?)
          D:/go_project/go2career/function/defer.go:27 +0x6a
   main.defer_exe_time()
          D:/go_project/go2career/function/defer.go:30 +0x10c
   main.main()
          D:/go_project/go2career/function/main.go:11 +0xf
*/
```
```go
func defer_exe_time() (i int) {
	i = 9
	defer func() {
		fmt.Printf("first i=%d\n", i)
	}()
	defer func(i int) {
		fmt.Printf("sencond i=%d\n", i)
	}(i)
	panic("zcy")
	defer fmt.Printf("third i = %d\n", i)

	return 5
}

/*
    sencond i=9
    first i=9
    panic: zcy
    
    goroutine 1 [running]:
    main.defer_exe_time()
            D:/git_repository/cyber_security_learning/Golang/go_prac/prac3/prac.go:44 +0xac
    main.main()
            D:/git_repository/cyber_security_learning/Golang/go_prac/prac3/prac.go:70 +0xf
    exit status 2
/*
```

#### 总结：panic与defer的关系
当`panic`发生时，程序会立刻停止正常执行，开始运行`defer`语句中的代码，然后再传播`panic`事件。如果在`defer`语句中再次发生`panic`，则新的`panic`会替代旧的`panic`

```go
package main

import "fmt"

func main() {
    fmt.Println("Starting program")
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered in main:", r)
        }
    }()
    f1()
    fmt.Println("This will be printed")
}

func f1() {
    fmt.Println("In f1")
    f2()
}

func f2() {
    fmt.Println("In f2")
    panic("Something went wrong in f2")
}
// 程序执行流程如下
/*
启动程序
注册defer
调用f1
调用f2
在f2中引发panic
panic传播到f1
panic传播到main
recover捕获了panic，之后打印"Recovered in main..."
程序停止
*/
```
- 设计使其能够继续向下执行main函数中后面的程序
```go
import "fmt"

func main() {
	fmt.Println("Starting program")
	f1()
	fmt.Println("This will be printed")
}

func f1() {
	fmt.Println("In f1")
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f1:", r)
		}
	}()
    // 这里的重点是，一定要让defer在f2()之前，也就是在触发panic之前，已经注册了defer，后续才会执行

	f2()
    // 如果将defer放在f2之后，根本不会被注册，会直接传播f2->f1->main->退出
}

func f2() {
	fmt.Println("In f2")
	panic("Something went wrong in f2")
}
/*
   程序执行路径如下
   开始执行
   执行f1
   注册f1的defer
   执行f2
   触发f2的panic
   panic传播到f1
   因为之前已注册过defer
   执行defer后的匿名函数
   捕获panic
   f1执行结束，同时，成功截获panic
   程序在main中继续执行
*/

/*
   最终结果是
   Starting program
   In f1
   In f2
   Recovered in f1: Something went wrong in f2
   This will be printed
*/
```


## 时间相关函数
```go
package main

import (
    "fmt"
    "time"
)

const (
    DATE="2006-01-02" // 等价于YYYY-mm-dd
    TIME="2006-01-02 15:04:05" // 等价于 H:M:S, 时:分:秒
)

func main() {
    // 获取当前时间
    t0 := time.Now()  // t0是time.Time数据类型, 本质是一个结构体
    /*
        type Time struct {
          wall uint64
          ext  int64
          loc *Location
        }
    */
    fmt.Println(t0.Unix()) // 时间戳 int64
    time.Sleep(50*time.Millisecond)
    t1 := time.Now()
    // Time - Time = Duration
    // type Duration int64, 源码中Duration继承自int64
    diff := t1.Sub(t0)
    // Sub()是time.Time这个结构体的方法
    // 用来计算时间差
    fmt.Println(diff.Milliseconds())
    //func (d Duration) Abs() Duration
    //func (d Duration) Hours() float64
    //func (d Duration) Microseconds() int64
    //func (d Duration) Milliseconds() int64
    //func (d Duration) Minutes() float64
    //func (d Duration) Nanoseconds() int64
    //func (d Duration) Seconds() int64

    // 从t0时刻到此刻
    fmt.Println(time.Since(t0).Milliseconds())

    // 计算时间的加法
    // Time + Duration = Time
    d := time.Duration(2*time.Sencond)
    t2 := t0.Add(d)
    fmt.Println(t2.Unix()) // 时间戳 int64

    // 时间的格式化和时间的解析
    fmt.Println(t0.Format(DATE))
    s:=t0.Format(TIME)
    fmt.Println(s)

    // 字符串解析成time类型: Parse

    // time.Parse(时间格式，字符串)返回值是时间
    t3,_:=time.Parse(TIME, s)  // t3 Time数据类型
    // t3,err:=time.Parse(TIME, s)  // t3 Time数据类型
    // 当字符串和时间格式不一致时，就会解析出错，此时err值为!nil
    fmt.Println(t3.Unix())
    // 建议使用Parse的时候，加上时区
    loc,_:=time.LoadLocation("Asia/Shanghai") // 该函数也有err返回值，防止字符串拼写错误
    t4,_:=time.ParseInLocation(Time,s,loc)
}
```

### 时间的格式化
```go
const (
    DATE="2006-01-02" // 等价于YYYY-mm-dd
    TIME="2006-01-02 15:04:05" // 等价于 H:M:S, 时:分:秒
)
```

## Json序列化

Go语言中的Json序列化，就是把一个对象，转换成一个二进制流，即[]byte(切片)

在Go语言中，如果要引用第三方库，需要使用go.mod进行包的管理
```
go mod init g6
go get github.com/bytedance/sonic
```

```go
package main

import (
    "fmt"
    "encoding/json"
    // bytedance/sonic库，更高效的序列化反序列化函数库
    "github.com/bytedance/sonic"
)

type Student struct {
    Name string
    Age int
    Gender bool
}

type Class struct {
    Id string
    Students []Student
}

func main() {
    s:=Student{"张三", 18, true}
    c:=Class {
        Id: "1(2)班",
        Students: []Student{s,s,s},
    }

    // 将实例c转换成二进制流
    bytes,err:=json.Marshal(c)  // json序列化
    if err!=nil{
        fmt.Println("json序列化失败"，err)
        return
    }

    // 将byte切片通过强制类型转换，转换为字符串
    str:=string(bytes)
    fmt.println(str)

    // 反序列化，将二进制字节流转换为结构体
    // 声明一个结构体，后续用来承接反序列化生成的对象
    var c2 Class
    // json.Unmarshal(bytes切片，承接对象的结构体)
    err=json.Unmarshal(bytes, &c2) // 要在函数成员内部改变函数参数，必须传递指针
    if err!=nil{
        fmt.Println("json反序列化失败"，err)
        return
    }
    fmt.Println("%+v", c2)// 要打印一个结构体，使用%v或者%+v
    // 在go语言中，如果要在函数内部修改一个结构体，必须传递指针，否则所有修改仅在函数内部生效

    // 使用sonic进行序列化和反序列化
    bytes,err:=sonic.Marshal(c)  // json序列化
    if err!=nil{
        fmt.Println("json序列化失败"，err)
        return
    }

    err=sonic.Unmarshal(bytes, &c2) // 要在函数成员内部改变函数参数，必须传递指针
    if err!=nil{
        fmt.Println("json反序列化失败"，err)
        return
    }
}
```

## 抽象
### 关于抽象的小案例
```go
package main

import (
    "fmt"
)

// 定义一个结构体Account
type Account struct {
    AccountNo string
    Pwd string
    Balance float64
}

// 方法
// 1.存款
func (account *Account) Deposite(money float64, pwd string) {
    // 看下输入的密码是否正确
    if pwd != account.Pwd {
        fmt.Println("你输入的密码不正确")
        return
    }

    // 查看存款金额是否正确
    if money <= 0 {
        fmt.Println("你输入的金额不正确")
        return
    }

    account.Balance += money
    fmt.Println("存款成功")
}

// 2.取款
func (account *Account) WithDraw(money float64, pwd string) {
    // 看下输入的密码是否正确
    if pwd != account.Pwd {
        fmt.Println("你输入的密码不正确")
        return
    }

    // 查看存款金额是否正确
    if money <= 0 || money > account.Balance {
        fmt.Println("你输入的金额不正确")
        return
    }

    account.Balance -= money
    fmt.Println("取款成功")
}

// 查询余额
func (account *Account) Query(pwd string) float64 {
    if pwd != account.Pwd {
        fmt.Println("你输入的密码不正确")
        return
    }
    return account.Balance
}
```

## 面向对象基本特性
### 封装
封装(encapsulation)就是把抽象出的`字段和对字段的操作`封装在一起，数据被保护在内部，程序的其他包只有通过被授权的操作(方法)，才能对字段进行操作

封装的好处
- 隐藏实现细节
- 它可以对数据进行验证，保证安全合理

如何体现封装
- 对结构体中的属性进行封装
- 通过方法、包实现封装

封装实现的步骤
1. 将结构体、字段(属性)的`首字母小写`(不能导出了，其他包不能使用，类似private)
2. 给结构体所在包提供一个工厂模式的函数，首字母大写，类似一个构造函数
3. 提供一个首字母大写的Set方法（类似其他语言的public），用于对属性判断并赋值
```go
func (var 结构体类型名) SetXxx(参数列表) (返回值列表) {
    // 加入数据验证的业务逻辑
    var.字段 = 参数
}
```
4. 提供一个首字母大写的Get方法(类似其他语言的public)，用于获取属性的值
```go
func(var 结构体类型名) GetXxx() {
    return var.字段
}
```

#### 封装案例
设计一个程序，不能随便查看人的年龄，工资等隐私，并对输入年龄进行合理验证
```go
// 目录结构设计
// encapsulate>(main, model(person.go))
package model

type person struct {
    Name string
    age int  // 其他包不能直接访问呢
    sal float64
}

// 写一个工厂模式的函数，相当于构造函数
func NewPerson(name string) *person {
    return &person {
        Name: name,
    }
}

// 为了访问age和sal我们编写一对SetXxx的方法和GetXxx的方法
func (p *person) SetAge(age int) {
    if age >=0 && age < 150 {
        p.age = age
    } else {
        fmt.Println("年龄范围不正确..")
        // 也可以给个默认值
    }
}

func (p *person) GetAge() int {
    return p.age
}

func (p *person) SetSal(age float64) {
    if sal >= 3000 && sal < 30000 {
        p.sal = sal
    } else {
        fmt.Println("薪水范围不正确..")
    }
}

func (p *person) GetSal() float64 {
    return p.sal
}
```

### 继承

```go
// 小学生
type Pupil struct {
    Name string
    Age int
    Score int
}

// 显示成绩
func (p *Pupil) ShowInfo() {
    fmt.Printf("学生名=%v 年龄=%v 成绩=%v\n", p.Name, p.Age, p.Score)
}

func (p *Pupil) SetScore(socre int) {
    // 业务判断
    p.Score = score
}

func (p *Pupil) testing() {
    fmt.Println("小学生正在考试...")
}

// 大学生，研究生...
// 这里如果重写大学生的结构体和方法，就会发生代码冗余，因此这里使用继承

func main() {
    // 测试
    var pupil = &Pupil{
        Name : "tom",
        Age : 10
    }
    pupil.testing()
    pupil.SetScore(90)
    pupil.ShowInfo()
}
```

### Go中继承的实现
通过匿名结构体实现继承
在结构体中嵌入一个匿名结构体实现继承

#### 总结
在Golang中，如果一个struct嵌套了另一个匿名结构体，那么这个结构体可以直接访问匿名结构体的字段和方法，从而实现了继承特性。

#### 嵌套匿名结构体的基本语法
```go
type Goods struct {
    Name string
    Price int
}

type Book struct {
    Goods // 这里就是嵌套匿名结构体，这里只有类型，没有名称
    Writer string
}
// 此时Book也能使用Goods的属性和方法
```