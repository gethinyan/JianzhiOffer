# -*- coding:utf-8 -*-
# 题目: 和为s的两个数字


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return array
        low = 0
        high = len(array) - 1
        while array[low] + array[high] != tsum and low < high:
            if array[low] + array[high] < tsum:
                low += 1
            else:
                high -= 1
        if array[low] + array[high] == tsum:
            return [array[low], array[high]]
        return []
