# -*- coding:utf-8 -*-
# 题目: 调整数组顺序使奇数位于偶数前面


class Solution:
    def reOrderArray(self, array):
        # write code here
        oddArr = []
        evenArr = []
        for item in array:
            if item % 2 == 0:
                evenArr.append(item)
            else:
                oddArr.append(item)
        return oddArr + evenArr


obj = Solution()
print(obj.reOrderArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
