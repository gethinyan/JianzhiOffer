package main

import "fmt"

// 题目: 斐波拉契数列

// Fibonacci ...
/**
 *
 * @param n int整型
 * @return int整型
 */
func Fibonacci(n int) int {
	// write code here
	if n == 0 {
		return 0
	}
	numOne := 0
	numTwo := 1
	for i := 0; i < n; i++ {
		numOne, numTwo = numTwo, numOne+numTwo
	}

	return numOne
}

func main() {
	fmt.Println(Fibonacci(4))
}
