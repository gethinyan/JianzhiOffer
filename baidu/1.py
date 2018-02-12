# -*- coding:utf-8 -*-
# 假设有一个数组，里面有10个元素 int a[10]={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}。
# 请写一个算法，得到a数组的一个随机排列。要求时间复杂度尽量小，可以使用random函数。
# 例如输出的随机序列可以是：3 6 2 4 5 1 9 8 0
import random


class Solution:
    def randomSerialize(self, L):
        lenL = len(L) - 1
        result = []
        for i in range(lenL, -1, -1):
            randomNum = random.randint(0, lenL)
            result.append(L[randomNum])
            L[randomNum], L[lenL] = L[lenL], L[randomNum]
            lenL -= 1
        return result


obj = Solution()
print(obj.randomSerialize([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
