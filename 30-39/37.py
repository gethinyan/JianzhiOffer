# -*- coding:utf-8 -*-
# 题目: 数字在排序数组中出现的次数


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data or data[0] > k or data[-1] < k:
            return 0
        index = -1
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) >> 1
            if data[mid] == k:
                index = mid
                break
            elif data[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        if index == -1:
            return 0
        low = index - 1
        high = index + 1
        count = 1
        while low >= 0 and data[low] == k:
            low = low - 1
            count += 1
        while high <= len(data) - 1 and data[high] == k:
            high += 1
            count += 1
        return count
