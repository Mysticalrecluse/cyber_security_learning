package main

import (
	"fmt"
	"strings"
	"unsafe"
)

func add(a int, b int) int {
	return a + b
}

func forPrac() {
	m := 4
	for m < 10 {
		fmt.Println(m)
		m += 3
	}
	fmt.Println(m)
}
func forPrac2() {
	n := 2
	for {
		n += 2
		fmt.Println(n)
		if n > 12 {
			break
		}
	}
}

func slice_init() {
	var s []int
	fmt.Printf("len %d, cap %d\n", len(s), cap(s))
}

func slice_test1() {
	arr := make([]int, 3, 5)
	arr[0] = 1
	arr[1] = 2
	arr[2] = 3
	brr := append(arr, 8)
	brr = append(brr, 8)
	brr = append(brr, 8) // 此事发生因为切片扩容，底层数组进行了拷贝
	fmt.Printf("len %d, cap %d\n", len(brr), cap(brr))
	// 执行结果：len 6, cap 10
}

func update_array1(arr [5]int) {
	for i := 0; i < len(arr); i++ {
		arr[i] += 10
		fmt.Println(arr[i])
	}
}

func appendEle(s *[]int) {
	*s = append(*s, 9)
}

type StringHeader struct {
	Data uintptr
	Len  int
}

func byte2string() {
	// 创建一个字符串
	str := "hello, world"

	// 获取字符串的底层实现
	strHeader := (*StringHeader)(unsafe.Pointer(&str))

	// 打印字符串的底层信息
	fmt.Printf("String: %s\n", str)
	fmt.Printf("Data: %x\n", strHeader.Data)
	fmt.Printf("Length: %d\n", strHeader.Len)

	// 将字符串转换为 []byte
	byteSlice := []byte(str)

	// 修改字节切片
	byteSlice[0] = 'H'

	// 将修改后的 []byte 转换回字符串
	newStr := string(byteSlice)

	// 打印新的字符串
	fmt.Printf("Modified string: %s\n", newStr)
}

func string_join() {
	s1 := "Hello"
	s2 := "how"
	s3 := "are"
	s4 := "you"
	merged := s1 + " " + s2 + " " + s3 + " " + s4 // 方法1
	fmt.Println(merged)
	merged = fmt.Sprintf("%s %s %s %s", s1, s2, s3, s4) // 方法2
	fmt.Println(merged)
	merged = strings.Join([]string{s1, s2, s3, s4}, " ") // 方法3
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

func map_prac() {
	m := map[string]int{"a": 1, "b": 2}
	for k, v := range m {
		fmt.Printf("key: %v, value: %v\n", k, v)
	}

}
