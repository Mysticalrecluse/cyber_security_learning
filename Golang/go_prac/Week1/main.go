package main

import (
	"fmt"
)

func int2binary(a uint64) {
	var i uint64 = 1 << 63
	for j := 0; j < 64; j++ {
		if a&i == i {
			fmt.Print(1)
		} else {
			fmt.Print(0)
		}
		i >>= 1
	}
}

func main() {
	// test()
	var a uint64
	fmt.Scan(&a)
	int2binary(a)
}

// go run .
