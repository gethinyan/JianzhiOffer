package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param head ListNode类
 * @return int整型一维数组
 */
func printListFromTailToHead(head *ListNode) []int {
	// write code here
	result := []int{}
	for head != nil {
		result = append([]int{head.Val}, result...)
		head = head.Next
	}

	return result
}

func main() {
	head := &ListNode{
		Val: 67,
		Next: &ListNode{
			Val: 0,
			Next: &ListNode{
				Val: 24,
				Next: &ListNode{
					Val:  58,
					Next: nil,
				},
			},
		},
	}
	fmt.Println(printListFromTailToHead(head))
}
