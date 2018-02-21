# -*- coding:utf-8 -*-
# 题目: 数组中的逆序对


class Solution:
    def InversePairs(self, data):
        # write code here
        res = 0
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    res += 1
        return res


obj = Solution()
print(obj.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
