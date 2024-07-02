package main

import "fmt"

func test() {
	a := 100
	{
		fmt.Println(a)
		a = a + 100
		fmt.Println(a)
	}
	fmt.Println(a)
}
