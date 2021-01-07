package main

import "fmt"

// 题目: 跳台阶

/**
 *
 * @param number int整型
 * @return int整型
 */
func jumpFloor(number int) int {
	// write code here
	if number == 0 {
		return 0
	}
	numOne := 1
	numTwo := 2
	for i := 2; i <= number; i++ {
		numOne, numTwo = numTwo, numOne+numTwo
	}

	return numOne
}

func main() {
	fmt.Println(jumpFloor(4))
}
