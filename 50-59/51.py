# -*- coding:utf-8 -*-
# 题目: 构建乘积数组


class Solution:
    def multiply(self, A):
        # write code here
        res = []
        for i in range(len(A)):
            curRes = 1
            for j in range(len(A)):
                if j != i:
                    curRes *= A[j]
            res.append(curRes)
        return res


obj = Solution()
print(obj.multiply([1, 2, 3, 4, 5]))
