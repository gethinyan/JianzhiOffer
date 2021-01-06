# -*- coding:utf-8 -*-
# 题目: 最小的k个数


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or len(tinput) == 0 or k > len(tinput):
            return []
        sortedList = self.quickSort(tinput)
        return sortedList[:k]

    def quickSort(self, L):
        if not L or len(L) == 0:
            return L
        sentry = L[-1]
        i, j = 0, 0
        while j < len(L) - 1:
            if L[j] < sentry:
                L[i], L[j] = L[j], L[i]
                i += 1
                j += 1
            else:
                j += 1
        return self.quickSort(L[:i]) + [sentry] + self.quickSort(L[i:len(L) - 1])


obj = Solution()
print(obj.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4))
