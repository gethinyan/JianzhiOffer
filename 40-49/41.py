# -*- coding:utf-8 -*-
# 题目: 和为S的连续数字
import math


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        end = int(math.sqrt(tsum))
        res = []
        for i in range(end, tsum + 1):
            if tsum % i == 0:
                tmp = []
                if i % 2 == 1:
                    if i // 2 - tsum // i + 1 > 0:
                        for j in range(i // 2 - tsum // i + 1, i // 2 + tsum // i + 1):
                            tmp.append(j)
                    if len(tmp) > 1:
                        res.append(tmp)
                tmp = []
                if tsum // i % 2 == 1:
                    if i - tsum // i // 2 > 0:
                        for j in range(i - tsum // i // 2, i + tsum // i // 2 + 1):
                            tmp.append(j)
                    if len(tmp) > 1:
                        res.append(tmp)
        return sorted(res)


obj = Solution()
print(obj.FindContinuousSequence(100))
