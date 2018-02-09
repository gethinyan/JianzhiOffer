# -*- coding:utf-8 -*-
# 题目: 斐波拉契数列


class Solution:
    def Fibonacci(self, n):
        # write code here
        firstNum = 0
        secondNum = 1
        index = 0
        while index < n:
            firstNum, secondNum = secondNum, firstNum + secondNum
            index += 1
        return firstNum


obj = Solution()
print(obj.Fibonacci(6))
