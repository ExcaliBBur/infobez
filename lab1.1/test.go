package main

import "fmt"

func main() {
	test()
}

func test() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("panic recover")
		}
	}()
	abra := func() {
		panic("new panic")
	}
	abra()
}
