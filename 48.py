# -*- coding:utf-8 -*-
# 题目: 不用加减乘除做加法


class Solution:
    def Add(self, num1, num2):
        # write code here
        return sum([num1, num2])

    def Add1(self, num1, num2):
        # write code here
        num3 = (num1 & num2) << 1
        num4 = num1 ^ num2
        while num3 and num4:
            num1, num2 = num3, num4
            num3 = (num1 & num2) << 1
            num4 = num1 ^ num2
        return num1 | num2


obj = Solution()
print(obj.Add(-3, 7))
