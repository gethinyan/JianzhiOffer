# -*- coding:utf-8 -*-
# 题目: 变态跳台阶


class Solution:
    def jumpFloorII(self, number):
        # write code here
        result = [1, 2]
        index = 2
        while index < number:
            sumNum = 0
            for num in result:
                sumNum += num
            sumNum += 1
            result.append(sumNum)
            index += 1
        return result[number - 1]


obj = Solution()
print(obj.jumpFloorII(6))
