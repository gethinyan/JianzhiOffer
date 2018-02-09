# -*- coding:utf-8 -*-
# 题目: 二进制中1的个数


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        for i in range(0, 32):
            if n & 1:
                count = count + 1
            n = n >> 1
        return count


obj = Solution()
print(obj.NumberOf1(-13))
