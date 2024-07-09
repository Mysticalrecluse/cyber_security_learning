package main

import (
	"fmt"
	"time"
)

func main() {
	//fmt.Println("Starting program")
	//f1()
	//fmt.Println("This will be printed")
	a := g1()
	a()
	a()
}

func f1() {
	fmt.Println("In f1")
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f1:", r)
		}
	}()

	f2()
}

func f2() {
	fmt.Println("In f2")
	panic("Something went wrong in f2")
}

func g1() func() {
	a := 1
	g2 := func() func() {
		b := 1
		a++
		g3 := func() {
			b += 2
			fmt.Printf("%d %d\n", a, b)
		}
		return g3
	}
	c := g2()
	return c
}

func timeStudy() {
	t0 := time.Now()
	fmt.Println(t0.Unix())
}
