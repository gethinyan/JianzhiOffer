# -*- coding:utf-8 -*-
# 一个数组有 N 个元素，求连续子数组的最大和。
# 例如：[-1,2,1]，和最大的连续子数组为[2,1]，其和为 3


class Solution:
    def maxSum(self, L):
        if L is None or len(L) == 0:
            return
        maxSum, curSum = 0, 0
        for item in L:
            curSum += item
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
        return maxSum


obj = Solution()
print(obj.maxSum([2, -1, 2, 1]))
