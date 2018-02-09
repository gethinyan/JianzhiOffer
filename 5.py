# -*- coding:utf-8 -*-
# 题目: 用两个栈实现队列


class Solution:
    def __init__(self):
        self.firstStack = []
        self.secondStack = []

    def push(self, node):
        # write code here
        self.firstStack.append(node)

    def pop(self):
        # return xx
        if self.secondStack:
            return self.secondStack.pop()
        elif not self.firstStack:
            return None
        else:
            while self.firstStack:
                self.secondStack.append(self.firstStack.pop())
            return self.secondStack.pop()


obj = Solution()
obj.push(1)
obj.push(2)
print(obj.pop())
