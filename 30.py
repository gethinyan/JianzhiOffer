# -*- coding:utf-8 -*-
# 题目: 连续子数组的最大和


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return
        maxNum = array[0]
        maxTmp = 0
        for item in array:
            maxTmp += item
            if maxTmp > maxNum:
                maxNum = maxTmp
            if maxTmp <= 0:
                maxTmp = 0
        return maxNum


obj = Solution()
print(obj.FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2]))
