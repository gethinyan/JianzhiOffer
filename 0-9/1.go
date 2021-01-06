package main

import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param target int整型
 * @param array int整型二维数组
 * @return bool布尔型
 */
func Find(target int, array [][]int) bool {
	// write code here
	height := len(array)
	if height <= 0 {
		return false
	}
	width := len(array[0])
	i := height - 1
	j := 0

	for i >= 0 && j <= width-1 {
		if array[i][j] == target {
			return true
		} else if array[i][j] > target {
			i--
		} else if array[i][j] < target {
			j++
		}
	}

	return false
}

func main() {
	array := [][]int{{1, 2, 8, 9}, {2, 4, 9, 12}, {4, 7, 10, 13}, {6, 8, 11, 15}}
	target := 7

	fmt.Println(Find(target, array))
}
