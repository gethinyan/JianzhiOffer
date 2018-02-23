# -*- coding:utf-8 -*-
# 题目: 孩子们的游戏(圆圈中最后剩下的数)


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not m or not n:
            return -1
        res = [i for i in range(n)]
        index = 0
        while len(res) > 1:
            index = (m + index - 1) % len(res)
            res.pop(index)
        return res[0]


obj = Solution()
print(obj.LastRemaining_Solution(5, 3))
