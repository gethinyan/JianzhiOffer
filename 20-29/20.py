# -*- coding:utf-8 -*-
# 题目: 包含min函数的栈


class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.minStack or self.minStack[-1] >= node:
            self.minStack.append(node)

    def pop(self):
        # write code here
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]
