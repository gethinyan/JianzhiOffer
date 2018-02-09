# -*- coding:utf-8 -*-
# 题目：矩形覆盖


class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        firstNum = 1
        secondNum = 2
        index = 2
        while index <= number:
            firstNum, secondNum = secondNum, firstNum + secondNum
            index += 1
        return firstNum


obj = Solution()
print(obj.rectCover(6))
