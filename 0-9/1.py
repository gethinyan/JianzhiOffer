# -*- coding:utf-8 -*-
# 题目: 二维数组中的查找


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array) - 1
        col = 0
        while row >= 0 and col < len(array[0]):
            if array[row][col] > target:
                row -= 1
            elif array[row][col] < target:
                col += 1
            else:
                return True
        return False


obj = Solution()
print(obj.Find(7, [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15],
]))
