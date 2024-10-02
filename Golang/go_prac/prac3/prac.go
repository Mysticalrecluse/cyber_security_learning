package main

import (
	"errors"
	"fmt"
)

func test(a []int) {
	for i := 0; i < len(a); i++ {
		fmt.Println(a[i])
	}

}

func div(args ...float64) (float64, error) {
	if len(args) == 0 {
		//return 0, errors.New("divide by zero")
		return 0, fmt.Errorf("")
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

func main() {
	//var mp = map[int]bool{1: true, 2: true, 3: true, 4: true, 5: true}

	//if _, exists := mp[1]; exists {
	//	fmt.Println("1 exists")
	//}
	//if _, exists := mp[14]; exists {
	//	fmt.Println("1 exists")
	//} else {
	//	fmt.Println("14 does not exist")
	//}
	//arr := []int{1, 2, 3}
	//for _, k := range arr {
	//	if _, exists := mp[k]; exists {
	//		fmt.Printf("%d,it's exists\n", k)
	//	}
	//}

	//slc := []int{1, 2, 3, 4, 5}
	//test(slc)
	defer_exe_time()

}
