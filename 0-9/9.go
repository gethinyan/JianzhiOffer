package main

import "fmt"

// 题目: 变态跳台阶

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param number int整型
 * @return int整型
 */
func jumpFloorII(number int) int {
	// write code here
	if number == 0 {
		return 0
	}
	tempStep := 0
	result := []int{1, 2}
	for i := 2; i < number; i++ {
		tempStep = 1
		for _, step := range result {
			tempStep += step
		}
		result = append(result, tempStep)
	}

	return result[number-1]
}

func main() {
	fmt.Println(jumpFloorII(3))
}
