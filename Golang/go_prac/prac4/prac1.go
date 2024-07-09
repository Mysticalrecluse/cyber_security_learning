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
	fmt.Println(t0.Unix()) // 时间戳 int64
	time.Sleep(50 * time.Millisecond)
	t1 := time.Now()
	// Time - Time = Duration
	diff := t1.Sub(t0)
	// Sub()是time.Time这个结构体的方法
	// 用来计算时间差
	fmt.Println(diff.Milliseconds())

	// 从t0时刻到此刻
	fmt.Println(time.Since(t0).Milliseconds())

	// 计算时间的加法
	// Time + Duration = Time
	d := time.Duration(2 * time.Sencond)
	t2 := t0.Add(d)
	fmt.Println(t2.Unix()) // 时间戳 int64

}
