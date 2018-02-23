# -*- coding:utf-8 -*-
# 题目: 求1+2+3+...+n


class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        def qiusum(n):
            self.sum += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)
        qiusum(n)
        return self.sum


obj = Solution()
print(obj.Sum_Solution(10))
