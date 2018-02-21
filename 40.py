# -*- coding:utf-8 -*-
# 题目: 数组中只出现一次的数字


class Solution:
    # 返回[a, b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        arrayDic = {}
        res = []
        for item in array:
            if item in arrayDic:
                arrayDic[item] += 1
            else:
                arrayDic[item] = 1
        for item in array:
            if arrayDic[item] == 1:
                res.append(item)
        return res

    def FindNumsAppearOnce1(self, array):
        res = []
        for item in array:
            if item in res:
                res.remove(item)
            else:
                res.append(item)
        return res


obj = Solution()
print(obj.FindNumsAppearOnce([1, 2, 3, 4, 5, 4, 3, 1]))
print(obj.FindNumsAppearOnce1([1, 2, 3, 4, 5, 4, 3, 1]))
