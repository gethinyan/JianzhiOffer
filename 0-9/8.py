# -*- coding:utf-8 -*-
# 题目: 跳台阶

class Solution:
    def jumpFloor(self, number):
        # write code here
        firstNum = 1
        secondNum = 2
        index = 2
        while index <= number:
            firstNum, secondNum = secondNum, firstNum + secondNum
            index += 1
        return firstNum


obj = Solution()
print(obj.jumpFloor(6))
