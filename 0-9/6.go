package main

import "fmt"

/**
 *
 * @param rotateArray int整型一维数组
 * @return int整型
 */
func minNumberInRotateArray(rotateArray []int) int {
	// write code here
	result := 0
	if len(rotateArray) == 0 {
		return result
	}
	if rotateArray[0] < rotateArray[len(rotateArray)-1] {
		result = rotateArray[0]
	} else {
		i := 0
		for i < len(rotateArray)-1 && rotateArray[i] <= rotateArray[i+1] {
			i++
		}
		result = rotateArray[i+1]
	}

	return result
}

func main() {
	fmt.Println(minNumberInRotateArray([]int{3, 4, 5, 1, 2}))
}
