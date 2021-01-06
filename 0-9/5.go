package main

import "fmt"

var stack1 []int
var stack2 []int

func Push(node int) {
	stack1 = append(stack1, node)
}

func Pop() int {
	result := 0
	if len(stack2) > 0 {
		result = stack2[len(stack2)-1]
		stack2 = stack2[:len(stack2)-1]
	} else if len(stack1) > 0 {
		for i := len(stack1) - 1; i >= 0; i-- {
			stack2 = append(stack2, stack1[i])
		}
		result = stack2[len(stack2)-1]
		stack2 = stack2[:len(stack2)-1]
		stack1 = []int{}
	}

	return result
}

func main() {
	Push(1)
	Push(2)
	fmt.Println(Pop())
}
