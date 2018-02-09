# -*- coding:utf-8 -*-
# 题目: 旋转数组的最小数字


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        i = 0
        while rotateArray[i] >= rotateArray[0] and i < len(rotateArray):
            i += 1
        i = i % len(rotateArray)
        return rotateArray[i]


obj = Solution()
print(obj.minNumberInRotateArray([3, 4, 5, 1, 2]))
