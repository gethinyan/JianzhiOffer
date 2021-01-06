# -*- coding:utf-8 -*-
# 题目: 整数中1出现的次数


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        tmp = n
        base = 1
        while tmp:
            last = tmp % 10
            tmp = tmp / 10
            res += tmp * base
            if last == 1:
                res += n % base + 1
            elif last > 1:
                res += base
            base *= 10
        return res


obj = Solution()
print(obj.NumberOf1Between1AndN_Solution(1000))
