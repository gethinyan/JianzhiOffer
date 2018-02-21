# -*- coding:utf-8 -*-
# 题目: 数组中出现次数超过一半的数字


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        numDic = {}
        for item in numbers:
            if not numDic.has_key(item):
                numDic[item] = 1
            else:
                numDic[item] += 1
        for key, value in numDic.items():
            if value > (len(numbers) // 2):
                return key
        return 0


obj = Solution()
print(obj.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
