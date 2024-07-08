package hw3

import (
	"fmt"
	"testing"
)

// TestRm tests the Rm2 function
func TestRm(t *testing.T) {
	tests := []struct {
		arr      []int
		mp       map[int]bool
		expected map[int]bool
	}{
		{
			// 测试用例1：arr中的元素都在mp中
			arr:      []int{1, 2, 3},
			mp:       map[int]bool{1: true, 2: true, 3: true},
			expected: map[int]bool{},
		},
		{
			// 测试用例2：arr中的元素部分在mp中
			arr:      []int{1, 2, 3, 5},
			mp:       map[int]bool{1: true, 2: true, 3: true, 4: true},
			expected: map[int]bool{4: true},
		},
		{
			// 测试用例3：arr中的元素都不在mp中
			arr:      []int{1, 2, 3},
			mp:       map[int]bool{4: true},
			expected: map[int]bool{4: true},
		},
	}

	for _, test := range tests {
		actual := Rm2(test.arr, test.mp)
		// 检查长度是否相等
		if len(actual) != len(test.expected) {
			fmt.Printf("Rm2(%v, %v) = %v; expected %v", test.arr, test.mp, actual, test.expected)
		}
		// 检查元素是否相等
		for k, v := range test.expected {
			if actual[k] != v {
				fmt.Printf("Rm2(%v, %v) = %v; expected %v", test.arr, test.mp, actual, test.expected)
			}
		}

	}

}

/*
PS D:\git_remote\cyber_security_learning\Golang\go_prac> go test -run=TestRm -v ./Week3
=== RUN   TestRm
--- PASS: TestRm (0.00s)
PASS
ok      homework/Week3  0.534s
*/

func BenchmarkRm(b *testing.B) {
	for n := 0; n < b.N; n++ {
		arr := make([]int, 0, 10000)
		for i := 0; i < 10000; i++ {
			arr = append(arr, i)
		}
	}
}

func BenchmarkRm2(b *testing.B) {
	for n := 0; n < b.N; n++ {
		brr := make([]int, 0)
		for i := 0; i < 10000; i++ {
			brr = append(brr, i)
		}
	}
}

//运行结果：
/*
goos: windows
goarch: amd64
pkg: homework/Week3
cpu: 13th Gen Intel(R) Core(TM) i7-13700H
BenchmarkRm-20             47677             26586 ns/op
BenchmarkRm2-20            12854             95877 ns/op
PASS
ok      homework/Week3  7.414s
*/
