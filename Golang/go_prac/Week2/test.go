package main

import "fmt"

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
