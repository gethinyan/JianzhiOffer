package main

import "fmt"

// 题目: 重建二叉树

// TreeNode ...
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param pre int整型一维数组
 * @param vin int整型一维数组
 * @return TreeNode类
 */
func reConstructBinaryTree(pre []int, vin []int) *TreeNode {
	// write code here
	if len(pre) != len(vin) {
		return nil
	}
	if len(pre) == 0 {
		return nil
	}
	rootVal := pre[0]
	index := getIndex(rootVal, vin)
	if index == -1 {
		return nil
	}
	result := &TreeNode{
		Val:   pre[0],
		Left:  reConstructBinaryTree(pre[1:index+1], vin[:index]),
		Right: reConstructBinaryTree(pre[index+1:], vin[index+1:]),
	}

	return result
}

func getIndex(target int, numList []int) int {
	for index, value := range numList {
		if target == value {
			return index
		}
	}

	return -1
}

func main() {
	fmt.Println(reConstructBinaryTree([]int{1, 2, 3, 4, 5, 6, 7}, []int{3, 2, 4, 1, 6, 5, 7}))
}
